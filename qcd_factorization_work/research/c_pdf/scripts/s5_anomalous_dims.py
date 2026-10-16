"""
s5_anomalous_dims.py -- item (5): one-loop anomalous dimensions of the twist-2 operators, computed from the
LOCAL operators (UV poles of their one-loop on-shell matrix elements), including quark-gluon mixing.

Operators (n.v = v^+ up to normalisation; here n = (1,0,0,-1) so n.v = v^0 + v^3 = sqrt2 v^+ -- every operator is
homogeneous of degree N in n, so the normalisation of n cancels in all ratios one-loop/tree):
    O_q^{(N)} = psibar nslash (i n.D)^{N-1} psi                       (one flavour)
    O_g^{(N)} = G^{a, n nu} [(i n.D)^{N-2}]^{ab} G^b_nu^{ n} = - g_{lam rho} G^{a,n lam} [(i n.D)^{N-2} G]^{a, n rho}
Matrix elements (spin/polarisation averaged, forward, on shell, massless):
    <q|O_q|q>^(0) = 2 (n.p)^N ,   <g|O_g|g>^(0) = [1+(-1)^N] (n.p)^N = 2 (n.p)^N for even N.
Renormalisation:  O_i^R = sum_j Z_ij O_j,  Z = 1 - (alpha_s/2pi)(1/eps) Gamma,  d O^R/d ln mu^2 = (alpha_s/2pi) Gamma O^R.
Hence  UV pole of <j|O_i|j>_bare^(1) (LSZ incl. external residues) / <j|O_j|j>^(0) = (alpha_s/2pi)(1/eps) Gamma_ij.
Comparison with DGLAP (moments gamma_ij(N) = int_0^1 z^{N-1} P_ij):
    Gamma_{q_k q_k} = gamma_qq,  Gamma_{q_k g} = 2 gamma_qg (quark + antiquark),  Gamma_{g q_k} = gamma_gq,
    Gamma_gg = gamma_gg.

Method: UV poles from the large-l expansion (fourd.uv_coeff): exact for one-loop UV poles; independent of the
IR regulator; the numerator algebra in 4 dimensions suffices for the 1/eps coefficient.
Feynman gauge.  g = 1 in the code; every diagram value below is the coefficient of (alpha_s/4pi)(1/eps).
Colour: quark diagrams carry C_F or T_F by hand; gluon diagrams use explicit SU(2) colour (f^{abc} = eps^{abc},
C_A = 2) and are divided by C_A at the end (each one-loop gluon diagram is proportional to f f = C_A delta).
"""
import sys, os, time
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import random
import sympy as sp
import fourd as F
from fourd import uv_coeff, GAM, METRIC, slash, dot, vadd, vscale, basis, O_gluon, L_YM_cubic, LV, t

results = []


def report(name, ok, detail=''):
    results.append((name, bool(ok)))
    print('%-84s %s %s' % (name, 'PASS' if ok else 'FAIL', detail), flush=True)


I = sp.I
ZERO = [0, 0, 0, 0]
nvec = [1, 0, 0, -1]
pvec = [t, 0, 0, t]                      # on shell, p^2 = 0, n.p = 2t
POLS = [[0, 1, 0, 0], [0, 0, 1, 0]]       # physical transverse polarisations (real): eps.p = n.eps = 0
NSL = slash(nvec)
E4 = sp.eye(4)


def nd(v):
    return dot(nvec, v)


def tr(M):
    return sp.expand(M.trace())


def uv(num, shifts):
    """C such that the UV pole of int d^Dl/(2pi)^D num / prod_j (l + a_j)^2 equals i C /(16 pi^2 eps)."""
    num = sp.expand(num)
    if num == 0:
        return sp.Integer(0)
    deg = sp.Poly(num, *F.GEN).homogeneous_order()
    assert deg is not None, 'numerator not homogeneous'
    T = deg - 2 * len(shifts) + 4
    if T < 0:
        return sp.Integer(0)
    re = sp.expand(num.subs(I, 0))
    im = sp.expand((num - re) / I)
    c = (uv_coeff(re, shifts, T) if re != 0 else 0) + I * (uv_coeff(im, shifts, T) if im != 0 else 0)
    return sp.expand(c * t ** T)


def pole_in_units(Cval, tree):
    """diagram = (g^2) i C/(16pi^2 eps) = (alpha_s/4pi)(1/eps) (i C).  Return (i C)/tree / 2, i.e. the coefficient of
    (alpha_s/2pi)(1/eps) relative to the tree matrix element."""
    r = sp.simplify(I * Cval / tree / 2)
    assert r.is_Rational, r
    return r


# ======================================================================================= 0. validation of Feynman rules
def f3(a, b, c):
    return F.f3(a, b, c)


def V3(q1, c1, e1, q2, c2, e2, q3, c3, e3):
    """three-gluon vertex (Peskin-Schroeder), all momenta incoming, g = 1:
       f^{c1c2c3} [ (e1.e2)(q1-q2).e3 + (e2.e3)(q2-q3).e1 + (e3.e1)(q3-q1).e2 ]"""
    ff = f3(c1, c2, c3)
    if ff == 0:
        return sp.Integer(0)
    return ff * sp.expand(dot(e1, e2) * dot(vadd(q1, vscale(-1, q2)), e3) + dot(e2, e3) * dot(vadd(q2, vscale(-1, q3)), e1)
                          + dot(e3, e1) * dot(vadd(q3, vscale(-1, q1)), e2))


random.seed(7)


def rvec():
    return [sp.Rational(random.randint(-9, 9), random.randint(1, 5)) for _ in range(4)]


ok = True
for trial in range(12):
    q1, q2 = rvec(), rvec()
    q3 = vscale(-1, vadd(q1, q2))
    e1, e2, e3 = rvec(), rvec(), rvec()
    cols = random.choice([(0, 1, 2), (1, 0, 2), (2, 1, 0), (0, 0, 1), (1, 2, 0)])
    ins = [(1, cols[0], e1, q1), (2, cols[1], e2, q2), (3, cols[2], e3, q3)]
    ok &= sp.simplify(L_YM_cubic(ins) - V3(q1, cols[0], e1, q2, cols[1], e2, q3, cols[2], e3)) == 0
report('triple-gluon vertex from i(-1/4)G.G (plane waves) = PS rule g f[g(k-p)+...] (12 random configs)', ok)


def Xvec(q, e):
    return vadd(vscale(nd(q), e), vscale(-nd(e), q))


ok = True
for N in range(2, 7):
    for trial in range(4):
        q1, q2, e1, e2 = rvec(), rvec(), rvec(), rvec()
        v = O_gluon(N, [(1, 0, e1, q1), (2, 0, e2, q2)], nvec)
        hand = sp.expand(dot(Xvec(q1, e1), Xvec(q2, e2)) * (nd(q1) ** (N - 2) + nd(q2) ** (N - 2)))
        ok &= sp.simplify(v - hand) == 0
        ok &= O_gluon(N, [(1, 0, e1, q1), (2, 1, e2, q2)], nvec) == 0
report('O_g 2-gluon vertex = delta^{ab} X1.X2 [(n.q1)^{N-2}+(n.q2)^{N-2}],  X = n.q e - n.e q (N=2..6)', ok)

ok = True
for trial in range(6):
    qs = [rvec(), rvec()]
    qs.append(vscale(-1, vadd(qs[0], qs[1])))
    es = [rvec(), rvec(), rvec()]
    cols = (0, 1, 2)
    v = O_gluon(2, [(i + 1, cols[i], es[i], qs[i]) for i in range(3)], nvec)
    hand = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if len({i, j, k}) == 3:
                    hand += 2 * I * f3(cols[i], cols[j], cols[k]) * nd(es[j]) * dot(Xvec(qs[i], es[i]), es[k])
    ok &= sp.simplify(v - sp.expand(hand)) == 0
    # colour antisymmetry
    v2 = O_gluon(2, [(1, 1, es[0], qs[0]), (2, 0, es[1], qs[1]), (3, 2, es[2], qs[2])], nvec)
    ok &= sp.simplify(v + v2) == 0
report('O_g^(2) 3-gluon vertex = 2i f^{c_i c_j c_k}(n.e_j)(X_i.e_k) summed; antisymmetric in colour', ok)

# ======================================================================================= 1. self energies: delta Z_2, delta Z_3
l = list(LV)


def S(k):
    """quark propagator numerator  i kslash  (denominator handled by uv())"""
    return I * slash(k)


# quark self-energy  -i Sigma(p) = int (i g^mu)(i (p-l)slash)(i g_mu)(-i)/((p-l)^2 l^2) C_F ; p off shell
q_off = [2 * t, t, 0, t]
pl = vadd(q_off, vscale(-1, l))
M = sp.zeros(4)
for mu in range(4):
    M += METRIC[mu] * (I * GAM[mu]) * S(pl) * (I * GAM[mu])
M = M * (-I)
# -i Sigma = sum; Sigma = p-slash Sigma_V ;  Tr[nslash Sigma] = 4 n.p Sigma_V
C_mSigma = uv(tr(NSL * M), [ZERO, vscale(-1, q_off)])
SigmaV_UV = sp.simplify((I * C_mSigma) / (-I) / (4 * nd(q_off)))       # coefficient of (alpha_s/4pi) C_F /eps
report('quark self-energy: Sigma_V^UV = -(alpha_s/4pi) C_F/eps  => delta Z_2 = -(alpha_s/4pi)C_F/eps [PS 16.?; Feynman gauge]',
       SigmaV_UV == -1, 'coef=%s' % SigmaV_UV)
dZ2 = sp.Rational(1, 2) * SigmaV_UV       # in units (alpha_s/2pi) C_F / eps


# gluon self-energy, p off shell, external colours a1 = a2 = 0, polarisation x (transverse to p)
pq = [t, 0, 0, 0]
ex = [0, 1, 0, 0]
cols = range(3)
# (G1) gluon loop: X(p,a1,ex; -k,c1,mu; -(p-k),c2,nu) Y(k,c1,mu; p-k,c2,nu; -p,a2,ex) (-i)^2 M M /2
k = l
pmk = vadd(pq, vscale(-1, k))
num = 0
for c1 in cols:
    for c2 in cols:
        if f3(0, c1, c2) == 0:
            continue
        for mu in range(4):
            for nu in range(4):
                Xv = V3(pq, 0, ex, vscale(-1, k), c1, basis(mu), vscale(-1, pmk), c2, basis(nu))
                Yv = V3(k, c1, basis(mu), pmk, c2, basis(nu), vscale(-1, pq), 0, ex)
                num += Xv * Yv * (-I * METRIC[mu]) * (-I * METRIC[nu])
C_G1 = uv(num / 2, [ZERO, vscale(-1, pq)])
# (G2) ghost loop: -1 * [-f^{c' a1 c}((k+p).ex)] [-f^{c a2 c'}(k.ex)] * i * i ; props k^2, (k+p)^2
num = 0
kp = vadd(k, pq)
for c in cols:
    for cp in cols:
        num += -1 * (-f3(cp, 0, c) * dot(kp, ex)) * (-f3(c, 0, cp) * dot(k, ex)) * I * I
C_G2 = uv(num, [ZERO, pq])
# (G3) quark loop (one flavour, colour T_F by hand): -Tr[(i ex) S(k+p) (i ex) S(k)]
num = -tr((I * slash(ex)) * S(kp) * (I * slash(ex)) * S(k))
C_G3 = uv(num, [ZERO, pq])
# sum of 1PI = i (p^2 g - p p) Pi ; contracted with ex ex : i(-p^2) Pi  -> Pi_UV = (i C)/(i (-p^2))
p2 = dot(pq, pq)
Pi_glue = sp.simplify((I * (C_G1 + C_G2)) / (I * (-p2)) / 2)    # SU(2): C_A = 2 -> coefficient of C_A
Pi_quark = sp.simplify((I * C_G3) / (I * (-p2)))                # coefficient of T_F (per flavour)
report('gluon self-energy (gluon+ghost loops): Pi_UV = (5/3) C_A (alpha_s/4pi)/eps', Pi_glue == sp.Rational(5, 3), 'coef=%s' % Pi_glue)
report('gluon self-energy (quark loop): Pi_UV = -(4/3) T_F n_f (alpha_s/4pi)/eps', Pi_quark == -sp.Rational(4, 3), 'coef=%s' % Pi_quark)
# transversality of the UV pole: contract with the longitudinal polarisation (p itself)
num_long = 0
for c1 in cols:
    for c2 in cols:
        if f3(0, c1, c2) == 0:
            continue
        for mu in range(4):
            for nu in range(4):
                Xv = V3(pq, 0, [1, 0, 0, 0], vscale(-1, k), c1, basis(mu), vscale(-1, pmk), c2, basis(nu))
                Yv = V3(k, c1, basis(mu), pmk, c2, basis(nu), vscale(-1, pq), 0, [1, 0, 0, 0])
                num_long += Xv * Yv * (-I * METRIC[mu]) * (-I * METRIC[nu])
num_gh_long = sum(-1 * (-f3(cp, 0, c) * dot(kp, [1, 0, 0, 0])) * (-f3(c, 0, cp) * dot(k, [1, 0, 0, 0])) * I * I
                  for c in cols for cp in cols)
tot_long = uv(num_long / 2, [ZERO, vscale(-1, pq)]) + uv(num_gh_long, [ZERO, pq])
report('   UV pole transverse: p_mu Pi^{mu nu} p_nu = 0 (gluon + ghost loops together)', sp.simplify(tot_long) == 0)
dZ3_CA = sp.Rational(1, 2) * Pi_glue     # units (alpha_s/2pi)/eps : 5/6 C_A
dZ3_nf = sp.Rational(1, 2) * Pi_quark    # -2/3 T_F n_f


# ======================================================================================= 2. operator matrix elements
def S1(Nv):
    return sum(sp.Rational(1, j) for j in range(1, Nv + 1))


def gam(Nv):
    return {'qq': sp.Rational(3, 2) + sp.Rational(1, Nv * (Nv + 1)) - 2 * S1(Nv),                    # x C_F
            'qg': sp.Rational(Nv ** 2 + Nv + 2, Nv * (Nv + 1) * (Nv + 2)),                          # x T_F
            'gq': sp.Rational(Nv ** 2 + Nv + 2, (Nv - 1) * Nv * (Nv + 1)),                          # x C_F
            'gg_CA': 2 * (sp.Rational(1, Nv * (Nv - 1)) + sp.Rational(1, (Nv + 1) * (Nv + 2)) - S1(Nv)) + sp.Rational(11, 6),
            'gg_nfTF': -sp.Rational(2, 3)}


def Oq3_sum(N, kin_, q):
    """sum_{j=0}^{N-2} (n.(k+q))^j (n.k)^{N-2-j}   (quark k in, gluon q in); vertex = g t^a n^mu nslash * sum"""
    return sum(nd(vadd(kin_, q)) ** j * nd(kin_) ** (N - 2 - j) for j in range(N - 1))


PSL = slash(pvec)
pm = vscale(-1, pvec)


def quark_in_quark(N):
    """<q|O_q^{(N)}|q>: A1 vertex, A2/A3 operator-gluon graphs.  Returns per-diagram coefficients of (alpha_s/2pi)C_F/eps."""
    tree = sp.expand(tr(PSL * NSL) / 2 * nd(pvec) ** (N - 1))
    kq = vadd(pvec, vscale(-1, l))            # internal quark k = p - l ; gluon l
    # A1: ubar (i g^nu)(i kslash) nslash (n.k)^{N-1} (i kslash)(i g_nu) u (-i)
    M = sp.zeros(4)
    mid = S(kq) * NSL * S(kq)
    for mu in range(4):
        M += METRIC[mu] * (I * GAM[mu]) * mid * (I * GAM[mu])
    numA1 = tr(PSL * M) / 2 * nd(kq) ** (N - 1) * (-I)
    A1 = pole_in_units(uv(numA1, [ZERO, pm, pm]), tree)
    # A2: ubar [n-slash sum(n.p)^j (n.k)^{N-2-j}] (i kslash)(i nslash) u (-i)   (gluon from the incoming leg)
    if N >= 2:
        numA2 = tr(PSL * NSL * S(kq) * (I * NSL)) / 2 * Oq3_sum(N, kq, l) * (-I)
        numA3 = tr(PSL * (I * NSL) * S(kq) * NSL) / 2 * Oq3_sum(N, pvec, vscale(-1, l)) * (-I)
        A2 = pole_in_units(uv(numA2, [ZERO, pm]), tree)
        A3 = pole_in_units(uv(numA3, [ZERO, pm]), tree)
    else:
        A2 = A3 = 0
    return A1, A2, A3


def gluon_op_in_quark(N):
    """<q|O_g^{(N)}|q> (colour C_F): ubar (i g^s)(i kslash)(i g^n) u (-i)^2 V(l, -l)."""
    tree_q = sp.expand(tr(PSL * NSL) / 2 * nd(pvec) ** (N - 1))
    kq = vadd(pvec, vscale(-1, l))
    # operator vertex components V[nu][sig]: leg1 (momentum l in) <-> gamma^nu, leg2 (momentum -l in) <-> gamma^sig
    Vt = [[O_gluon(N, [(1, 0, basis(a), l), (2, 0, basis(b), vscale(-1, l))], nvec) for b in range(4)] for a in range(4)]
    M = sp.zeros(4)
    for a in range(4):
        for b in range(4):
            if Vt[a][b] != 0:
                M += (I * GAM[b]) * S(kq) * (I * GAM[a]) * Vt[a][b]
    num = tr(PSL * M) / 2 * (-I) * (-I)
    return pole_in_units(uv(num, [ZERO, ZERO, pm]), tree_q)


def quark_op_in_gluon(N):
    """<g|O_q^{(N)}|g> per flavour (colour T_F): two orientations of the quark loop (+ graphs with the operator's
    quark-quark-gluon vertex, which are proportional to n.eps = 0)."""
    vals = []
    for e in POLS:
        assert nd(e) == 0
        Esl = slash(e)
        GO = NSL * nd(l) ** (N - 1)
        c1 = -tr(GO * S(l) * (I * Esl) * S(vadd(l, pm)) * (I * Esl) * S(l))
        c2 = -tr(GO * S(l) * (I * Esl) * S(vadd(l, pvec)) * (I * Esl) * S(l))
        vals.append((uv(c1, [ZERO, ZERO, pm]), uv(c2, [ZERO, ZERO, pvec])))
    C1 = sum(v[0] for v in vals) / 2
    C2 = sum(v[1] for v in vals) / 2
    tree_g = 2 * nd(pvec) ** N
    return pole_in_units(C1, tree_g), pole_in_units(C2, tree_g)


def gluon_in_gluon(N):
    """<g|O_g^{(N)}|g> (explicit SU(2) colour; external colour 0): D1 (operator 2-vertex + two 3-gluon vertices),
    D2/D3 (operator 3-vertex at the incoming/outgoing external gluon, symmetry factor 1/2).  Returns coefficients
    of (alpha_s/2pi) C_A / eps (divided by C_A = 2)."""
    k_ = l
    pmk = vadd(pvec, vscale(-1, k_))
    mk, mpmk = vscale(-1, k_), vscale(-1, pmk)
    O2 = [[O_gluon(N, [(1, 0, basis(a), k_), (2, 0, basis(b), mk)], nvec) for b in range(4)] for a in range(4)]
    tree = sp.Integer(0)
    D1 = D2 = D3 = sp.Integer(0)
    for e in POLS:
        tree += O_gluon(N, [(1, 0, e, pvec), (2, 0, e, pm)], nvec) / 2
        n1 = 0
        for c1 in range(3):
            for c2 in range(3):
                if f3(0, c1, c2) == 0:
                    continue
                X = [[V3(pvec, 0, e, mk, c1, basis(a), mpmk, c2, basis(b)) for b in range(4)] for a in range(4)]
                # D1: X(c1,c2)[mu][nu] O2[mu][rho] Y(c3=c1, c2)[rho][nu]
                Y = [[V3(k_, c1, basis(a), pmk, c2, basis(b), pm, 0, e) for b in range(4)] for a in range(4)]
                for mu in range(4):
                    for nu in range(4):
                        if X[mu][nu] == 0:
                            continue
                        for rho in range(4):
                            if O2[mu][rho] == 0 or Y[rho][nu] == 0:
                                continue
                            n1 += X[mu][nu] * O2[mu][rho] * Y[rho][nu] * (-I * METRIC[mu]) * (-I * METRIC[nu]) * (-I * METRIC[rho])
        D1 += uv(n1, [ZERO, ZERO, pm]) / 2
        n2 = 0
        n3 = 0
        for c1 in range(3):
            for c2 in range(3):
                if f3(0, c1, c2) == 0:
                    continue
                for a in range(4):
                    for b in range(4):
                        Yv = V3(k_, c1, basis(a), pmk, c2, basis(b), pm, 0, e)
                        if Yv != 0:
                            Op3 = O_gluon(N, [(1, 0, e, pvec), (2, c1, basis(a), mk), (3, c2, basis(b), mpmk)], nvec)
                            n2 += Op3 * Yv * (-I * METRIC[a]) * (-I * METRIC[b]) / 2
                        Xv = V3(pvec, 0, e, mk, c1, basis(a), mpmk, c2, basis(b))
                        if Xv != 0:
                            Op3p = O_gluon(N, [(1, 0, e, pm), (2, c1, basis(a), k_), (3, c2, basis(b), pmk)], nvec)
                            n3 += Xv * Op3p * (-I * METRIC[a]) * (-I * METRIC[b]) / 2
        D2 += uv(n2, [ZERO, pm]) / 2
        D3 += uv(n3, [ZERO, pm]) / 2
    tree = sp.expand(tree)
    CAsu2 = 2
    return (pole_in_units(D1, tree) / CAsu2, pole_in_units(D2, tree) / CAsu2, pole_in_units(D3, tree) / CAsu2, tree)


print('\n--- per-diagram UV poles, coefficients of (alpha_s/2pi)(1/eps) x colour factor, relative to tree ---', flush=True)
table = {}
NLIST = [int(a) for a in (sys.argv[1:] or ['1', '2', '3', '4', '5', '6', '8', '10', '12', '14'])]
for N in [Nv for Nv in NLIST if Nv % 2 == 1]:
    # odd N: C-odd (non-singlet q - qbar) sector; O_g^{(N)} has vanishing forward matrix elements
    t0 = time.time()
    A1, A2, A3 = quark_in_quark(N)
    C1, C2 = quark_op_in_gluon(N)
    Bq = gluon_op_in_quark(N) if N >= 3 else 0     # O_g^{(N)} is defined for N >= 2 only
    G = gam(N)
    print('N=%d (%.0fs): A1=%s A2=%s A3=%s | C1=%s C2=%s | B=%s' % (N, time.time() - t0, A1, A2, A3, C1, C2, Bq), flush=True)
    Gqq = A1 + A2 + A3 + dZ2
    report('N=%d (odd)  Gamma_qq = A1+A2+A3+dZ2 = gamma_qq(N)  (non-singlet, C-odd)' % N, sp.simplify(Gqq - G['qq']) == 0, str(Gqq))
    report('N=%d (odd)  per diagram: A1 = 1/(N(N+1)), A2 = A3 = -(S_1(N)-1)' % N,
           sp.simplify(A1 - sp.Rational(1, N * (N + 1))) == 0 and sp.simplify(A2 + S1(N) - 1) == 0 and sp.simplify(A3 + S1(N) - 1) == 0)
    report('N=%d (odd)  <g|O_q|g>: the two quark-loop orientations cancel (C1 = -C2), no mixing' % N
           + ('  [N=1: Furry, <g|J^+|g> = 0]' if N == 1 else ''), sp.simplify(C1 + C2) == 0)
    if N >= 3:
        report('N=%d (odd)  <q|O_g|q> = 0 (O_g^{(N)} odd: forward vertex vanishes)' % N, Bq == 0)
for N in [Nv for Nv in NLIST if Nv % 2 == 0]:
    t0 = time.time()
    A1, A2, A3 = quark_in_quark(N)
    Bq = gluon_op_in_quark(N)
    C1, C2 = quark_op_in_gluon(N)
    D1, D2, D3, treeg = gluon_in_gluon(N)
    table[N] = dict(A1=A1, A2=A2, A3=A3, B=Bq, C1=C1, C2=C2, D1=D1, D2=D2, D3=D3)
    G = gam(N)
    print('N=%d (%.0fs): A1=%s A2=%s A3=%s | B=%s | C1=%s C2=%s | D1=%s D2=%s D3=%s | tree_g=%s'
          % (N, time.time() - t0, A1, A2, A3, Bq, C1, C2, D1, D2, D3, treeg), flush=True)
    report('N=%d  tree <g|O_g|g> = 2 (n.p)^N (polarisation averaged)' % N, sp.simplify(treeg - 2 * nd(pvec) ** N) == 0)
    report('N=%d  vertex graph A1 = C_F/(N(N+1))   [= s4 ladder-moment pole]' % N, sp.simplify(A1 - sp.Rational(1, N * (N + 1))) == 0)
    report('N=%d  operator-gluon graphs A2+A3 = -2 C_F sum_{j=2}^N 1/j   [= s4 Wilson-line graphs]' % N,
           sp.simplify(A2 + A3 + 2 * (S1(N) - 1)) == 0 and sp.simplify(A2 - A3) == 0)
    Gqq = A1 + A2 + A3 + dZ2
    report('N=%d  Gamma_qq = A1+A2+A3+dZ2 = gamma_qq(N) = C_F[3/2+1/(N(N+1))-2S_1(N)]' % N, sp.simplify(Gqq - G['qq']) == 0, str(Gqq))
    report('N=%d  Gamma_gq = B = gamma_gq(N) = C_F (N^2+N+2)/((N-1)N(N+1))' % N, sp.simplify(Bq - G['gq']) == 0, str(Bq))
    report('N=%d  Gamma_{q_k g} = C1+C2 = 2 gamma_qg(N) = 2 T_F (N^2+N+2)/(N(N+1)(N+2))  (C1 = C2)' % N,
           sp.simplify(C1 + C2 - 2 * G['qg']) == 0 and sp.simplify(C1 - C2) == 0, str(C1 + C2))
    Ggg = D1 + D2 + D3 + dZ3_CA
    report('N=%d  Gamma_gg|_CA = D1+D2+D3+dZ3 = 2[1/(N(N-1))+1/((N+1)(N+2))-S_1]+11/6' % N, sp.simplify(Ggg - G['gg_CA']) == 0, str(Ggg))
    report('N=%d  Gamma_gg|_{nf T_F} = dZ3|_nf = -2/3 (no 1PI quark graph at one loop)' % N, sp.simplify(dZ3_nf - G['gg_nfTF']) == 0)
    # per-diagram closed forms (Feynman gauge), read off from N = 2..10 and tested at every N run
    D1f = sp.Rational(2, N * (N - 1)) + sp.Rational(2, (N + 1) * (N + 2)) + sp.Rational(1, N + 1)
    D2f = -(S1(N) - 1) - sp.Rational(N + 2, 2 * (N + 1))
    report('N=%d  per diagram: D1 = 2/(N(N-1))+2/((N+1)(N+2))+1/(N+1),  D2 = D3 = -(S_1-1)-(N+2)/(2(N+1))' % N,
           sp.simplify(D1 - D1f) == 0 and sp.simplify(D2 - D2f) == 0 and sp.simplify(D3 - D2f) == 0)
    report('N=%d  per diagram: C1 = C2 = T_F(N^2+N+2)/(N(N+1)(N+2)),  B = C_F(N^2+N+2)/((N-1)N(N+1))' % N,
           sp.simplify(C1 - G['qg']) == 0 and sp.simplify(Bq - G['gq']) == 0)

# N = 2 mixing matrix & conservation of T^{++}
if 2 in table:
    CF, CA, TF, nf = sp.symbols('C_F C_A T_F n_f', positive=True)
    tb = table[2]
    Gam = sp.Matrix([[CF * (tb['A1'] + tb['A2'] + tb['A3'] + dZ2), nf * TF * (tb['C1'] + tb['C2'])],
                     [CF * tb['B'], CA * (tb['D1'] + tb['D2'] + tb['D3'] + dZ3_CA) + nf * TF * dZ3_nf]])
    print('N=2 singlet mixing matrix (rows: Sigma = sum_k O_{q_k}, O_g ; columns: Sigma, O_g):', Gam)
    report('N=2 matrix = [[-4C_F/3, 2n_fT_F/3],[4C_F/3, -2n_fT_F/3]] (= s3 moments of P_ij)',
           sp.simplify(Gam - sp.Matrix([[-4 * CF / 3, 2 * nf * TF / 3], [4 * CF / 3, -2 * nf * TF / 3]])) == sp.zeros(2))
    report('T^{++} = Sigma + O_g conserved: column sums of Gamma vanish', sp.simplify(Gam[0, 0] + Gam[1, 0]) == 0 and sp.simplify(Gam[0, 1] + Gam[1, 1]) == 0)

print()
print('SUMMARY s5: %d/%d PASS' % (sum(1 for _, o in results if o), len(results)))
