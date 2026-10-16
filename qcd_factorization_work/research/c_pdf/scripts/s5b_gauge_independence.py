"""
s5b_gauge_independence.py -- item (5), cross-check: the same one-loop UV poles as s5, but in a general covariant
gauge with gluon propagator  -i [g^{mu nu} - (1 - xi_g) k^mu k^nu / k^2] delta^{ab} / k^2.

Each internal gluon line is split into its 'g' part and its 'kk' part; a 'kk' line contributes
(-i)(-(1-xi_g)) (X.k)(Y.k) and one extra power of 1/k^2 (its shift is appended to the propagator list).
Diagram value = sum over subsets S of lines in 'kk' mode of (-(1-xi_g))^{|S|} * UV[...].
Checks:
  delta Z_2(xi) = -(alpha_s/4pi) C_F xi_g /eps ;  delta Z_3(xi) = (alpha_s/4pi)(1/eps)[(13/6 - xi_g/2) C_A - (4/3) T_F n_f]
  Gamma_qq, Gamma_gq, Gamma_gg (C_A part) independent of xi_g and equal to the moments of P_ij.
"""
import sys, os, time, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
import fourd as F
from fourd import uv_coeff, GAM, METRIC, slash, dot, vadd, vscale, basis, O_gluon, LV, t

results = []


def report(name, ok, detail=''):
    results.append((name, bool(ok)))
    print('%-88s %s %s' % (name, 'PASS' if ok else 'FAIL', detail), flush=True)


I = sp.I
xi = sp.Symbol('xi_g')
ZERO = [0, 0, 0, 0]
nvec = [1, 0, 0, -1]
pvec = [t, 0, 0, t]
pm = vscale(-1, pvec)
POLS = [[0, 1, 0, 0], [0, 0, 1, 0]]
NSL = slash(nvec)
PSL = slash(pvec)
l = list(LV)


def nd(v):
    return dot(nvec, v)


def tr(M):
    return sp.expand(M.trace())


def uv(num, shifts):
    num = sp.expand(num)
    if num == 0:
        return sp.Integer(0)
    deg = sp.Poly(num, *F.GEN).homogeneous_order()
    assert deg is not None
    T = deg - 2 * len(shifts) + 4
    if T < 0:
        return sp.Integer(0)
    re = sp.expand(num.subs(I, 0))
    im = sp.expand((num - re) / I)
    c = (uv_coeff(re, shifts, T) if re != 0 else 0) + I * (uv_coeff(im, shifts, T) if im != 0 else 0)
    return sp.expand(c * t ** T)


def S(k):
    return I * slash(k)


def f3(a, b, c):
    return F.f3(a, b, c)


def V3(q1, c1, e1, q2, c2, e2, q3, c3, e3):
    ff = f3(c1, c2, c3)
    if ff == 0:
        return sp.Integer(0)
    return ff * sp.expand(dot(e1, e2) * dot(vadd(q1, vscale(-1, q2)), e3) + dot(e2, e3) * dot(vadd(q2, vscale(-1, q3)), e1)
                          + dot(e3, e1) * dot(vadd(q3, vscale(-1, q1)), e2))


def modes(nlines):
    return list(itertools.product(('g', 'kk'), repeat=nlines))


def choices(mode, kline):
    """list of (vector to insert on both ends, weight) for one line."""
    if mode == 'g':
        return [(basis(m), METRIC[m]) for m in range(4)]
    return [(kline, 1)]


def gauge_sum(builder, lines, base_shifts):
    """builder(list_of_inserted_vectors) -> numerator (without propagator factors).
       lines: list of (momentum of the line, shift of its propagator).
       Returns sum_S (-(1-xi))^{|S|} UV[...]; each line carries (-i)."""
    tot = 0
    for md in modes(len(lines)):
        num = 0
        for combo in itertools.product(*[choices(m, ln[0]) for m, ln in zip(md, lines)]):
            vecs = [c[0] for c in combo]
            w = 1
            for c in combo:
                w *= c[1]
            num += w * builder(vecs)
        num = num * (-I) ** len(lines)
        shifts = list(base_shifts) + [ln[1] for m, ln in zip(md, lines) if m == 'kk']
        nkk = sum(1 for m in md if m == 'kk')
        tot += (-(1 - xi)) ** nkk * uv(num, shifts)
    return sp.expand(tot)


def units(Cval, tree):
    r = sp.simplify(I * Cval / tree / 2)
    return sp.expand(r)


# ------------------------------------------------------------------ quark self-energy
q_off = [2 * t, t, 0, t]
plq = vadd(q_off, vscale(-1, l))


def b_sigma(v):
    e, = v
    return tr(NSL * (I * slash(e)) * S(plq) * (I * slash(e)))


Cs = gauge_sum(b_sigma, [(l, ZERO)], [ZERO, vscale(-1, q_off)])
SigmaV = sp.expand((I * Cs) / (-I) / (4 * nd(q_off)))
report('Sigma_V^UV = -(alpha_s/4pi) C_F xi_g/eps  (general covariant gauge)', sp.simplify(SigmaV + xi) == 0, str(SigmaV))
dZ2 = SigmaV / 2

# ------------------------------------------------------------------ gluon self-energy (gluon loop; ghost loop is xi-independent)
pq = [t, 0, 0, 0]
ex = [0, 1, 0, 0]
k = l
pmk = vadd(pq, vscale(-1, k))


def b_glue(v):
    e1, e2 = v
    s = 0
    for c1 in range(3):
        for c2 in range(3):
            if f3(0, c1, c2):
                s += V3(pq, 0, ex, vscale(-1, k), c1, e1, vscale(-1, pmk), c2, e2) * V3(k, c1, e1, pmk, c2, e2, vscale(-1, pq), 0, ex)
    return s / 2


C_G1 = gauge_sum(b_glue, [(k, ZERO), (pmk, vscale(-1, pq))], [ZERO, vscale(-1, pq)])
kp = vadd(k, pq)
C_G2 = uv(sum(-1 * (-f3(cp, 0, c) * dot(kp, ex)) * (-f3(c, 0, cp) * dot(k, ex)) * I * I for c in range(3) for cp in range(3)), [ZERO, pq])
p2 = dot(pq, pq)
Pi_CA = sp.expand((I * (C_G1 + C_G2)) / (I * (-p2)) / 2)
report('Pi_UV|_CA = (13/6 - xi_g/2) C_A (alpha_s/4pi)/eps  (general covariant gauge)', sp.simplify(Pi_CA - (sp.Rational(13, 6) - xi / 2)) == 0, str(Pi_CA))
dZ3_CA = Pi_CA / 2


# ------------------------------------------------------------------ operators
def S1(Nv):
    return sum(sp.Rational(1, j) for j in range(1, Nv + 1))


def gam(Nv):
    return {'qq': sp.Rational(3, 2) + sp.Rational(1, Nv * (Nv + 1)) - 2 * S1(Nv),
            'gq': sp.Rational(Nv ** 2 + Nv + 2, (Nv - 1) * Nv * (Nv + 1)),
            'gg_CA': 2 * (sp.Rational(1, Nv * (Nv - 1)) + sp.Rational(1, (Nv + 1) * (Nv + 2)) - S1(Nv)) + sp.Rational(11, 6)}


def Oq3_sum(N, kin_, q):
    return sum(nd(vadd(kin_, q)) ** j * nd(kin_) ** (N - 2 - j) for j in range(N - 1))


def Gamma_qq(N):
    tree = sp.expand(tr(PSL * NSL) / 2 * nd(pvec) ** (N - 1))
    kq = vadd(pvec, vscale(-1, l))

    def bA1(v):
        e, = v
        return tr(PSL * (I * slash(e)) * S(kq) * NSL * S(kq) * (I * slash(e))) / 2 * nd(kq) ** (N - 1)

    def bA2(v):
        e, = v       # operator vertex carries n.e ; QCD vertex i eslash
        return tr(PSL * NSL * S(kq) * (I * slash(e))) / 2 * Oq3_sum(N, kq, l) * nd(e)

    def bA3(v):
        e, = v
        return tr(PSL * (I * slash(e)) * S(kq) * NSL) / 2 * Oq3_sum(N, pvec, vscale(-1, l)) * nd(e)

    A1 = units(gauge_sum(bA1, [(l, ZERO)], [ZERO, pm, pm]), tree)
    A2 = units(gauge_sum(bA2, [(l, ZERO)], [ZERO, pm]), tree) if N >= 2 else 0
    A3 = units(gauge_sum(bA3, [(l, ZERO)], [ZERO, pm]), tree) if N >= 2 else 0
    return A1, A2, A3


def Gamma_gq(N):
    tree = sp.expand(tr(PSL * NSL) / 2 * nd(pvec) ** (N - 1))
    kq = vadd(pvec, vscale(-1, l))

    def bB(v):
        e1, e2 = v   # e1: line with momentum l into the operator (attached to the first QCD vertex), e2: line out
        Vop = O_gluon(N, [(1, 0, e1, l), (2, 0, e2, vscale(-1, l))], nvec)
        if Vop == 0:
            return 0
        return tr(PSL * (I * slash(e2)) * S(kq) * (I * slash(e1))) / 2 * Vop

    return units(gauge_sum(bB, [(l, ZERO), (l, ZERO)], [ZERO, ZERO, pm]), tree)


def Gamma_gg(N):
    k_ = l
    pmk_ = vadd(pvec, vscale(-1, k_))
    mk, mpmk = vscale(-1, k_), vscale(-1, pmk_)
    tree = 0
    D1 = D2 = D3 = 0
    for e in POLS:
        tree += O_gluon(N, [(1, 0, e, pvec), (2, 0, e, pm)], nvec) / 2

        def bD1(v):
            a, b, c = v      # a: X-op line (momentum k), b: X-Y line (p-k), c: op-Y line (k)
            Vop = O_gluon(N, [(1, 0, a, k_), (2, 0, c, mk)], nvec)
            if Vop == 0:
                return 0
            s = 0
            for c1 in range(3):
                for c2 in range(3):
                    if f3(0, c1, c2):
                        s += V3(pvec, 0, e, mk, c1, a, mpmk, c2, b) * V3(k_, c1, c, pmk_, c2, b, pm, 0, e)
            return s * Vop

        def bD2(v):
            a, b = v
            s = 0
            for c1 in range(3):
                for c2 in range(3):
                    if f3(0, c1, c2):
                        Yv = V3(k_, c1, a, pmk_, c2, b, pm, 0, e)
                        if Yv != 0:
                            s += O_gluon(N, [(1, 0, e, pvec), (2, c1, a, mk), (3, c2, b, mpmk)], nvec) * Yv
            return s / 2

        def bD3(v):
            a, b = v
            s = 0
            for c1 in range(3):
                for c2 in range(3):
                    if f3(0, c1, c2):
                        Xv = V3(pvec, 0, e, mk, c1, a, mpmk, c2, b)
                        if Xv != 0:
                            s += Xv * O_gluon(N, [(1, 0, e, pm), (2, c1, a, k_), (3, c2, b, pmk_)], nvec)
            return s / 2

        D1 += gauge_sum(bD1, [(k_, ZERO), (pmk_, pm), (k_, ZERO)], [ZERO, ZERO, pm]) / 2
        D2 += gauge_sum(bD2, [(k_, ZERO), (pmk_, pm)], [ZERO, pm]) / 2
        D3 += gauge_sum(bD3, [(k_, ZERO), (pmk_, pm)], [ZERO, pm]) / 2
    tree = sp.expand(tree)
    return units(D1, tree) / 2, units(D2, tree) / 2, units(D3, tree) / 2


NLIST = [int(a) for a in (sys.argv[1:] or ['1', '2', '3', '4', '5', '6', '8'])]
for N in NLIST:
    t0 = time.time()
    A1, A2, A3 = Gamma_qq(N)
    Gqq = sp.expand(A1 + A2 + A3 + dZ2)
    print('N=%d: A1=%s | A2=%s | A3=%s | dZ2=%s' % (N, A1, A2, A3, dZ2), flush=True)
    report('N=%d  Gamma_qq(xi_g) = gamma_qq(N), xi_g-independent' % N, sp.simplify(Gqq - gam(N)['qq']) == 0, str(Gqq))
    report('N=%d  per diagram: A1 = 1/(N(N+1)) + (xi_g-1)/2,  A2 = A3 = -(S_1(N)-1)' % N,
           sp.simplify(A1 - sp.Rational(1, N * (N + 1)) - (xi - 1) / 2) == 0
           and sp.simplify(A2 + (S1(N) - 1)) == 0 and sp.simplify(A3 + (S1(N) - 1)) == 0)
    if N >= 2 and N % 2 == 0:
        B = Gamma_gq(N)
        report('N=%d  Gamma_gq(xi_g) = gamma_gq(N), xi_g-independent (single graph)' % N, sp.simplify(B - gam(N)['gq']) == 0, str(B))
        D1, D2, D3 = Gamma_gg(N)
        Ggg = sp.expand(D1 + D2 + D3 + dZ3_CA)
        print('N=%d: D1=%s | D2=%s | D3=%s | dZ3=%s  (%.0fs)' % (N, D1, D2, D3, dZ3_CA, time.time() - t0), flush=True)
        report('N=%d  Gamma_gg|_CA(xi_g) = gamma_gg|_CA(N), xi_g-independent' % N, sp.simplify(Ggg - gam(N)['gg_CA']) == 0, str(Ggg))
        D1F = sp.Rational(2, N * (N - 1)) + sp.Rational(2, (N + 1) * (N + 2)) + sp.Rational(1, N + 1)
        D2F = -(S1(N) - 1) - sp.Rational(N + 2, 2 * (N + 1))
        report('N=%d  per diagram: D1 = D1|_F + (xi_g-1)/2,  D2 = D3 = D2|_F - (xi_g-1)/8,  dZ3 = 5/6 - (xi_g-1)/4' % N,
               sp.simplify(D1 - D1F - (xi - 1) / 2) == 0 and sp.simplify(D2 - D2F + (xi - 1) / 8) == 0
               and sp.simplify(D3 - D2F + (xi - 1) / 8) == 0 and sp.simplify(dZ3_CA - sp.Rational(5, 6) + (xi - 1) / 4) == 0)

print()
print('SUMMARY s5b: %d/%d PASS' % (sum(1 for _, o in results if o), len(results)))
