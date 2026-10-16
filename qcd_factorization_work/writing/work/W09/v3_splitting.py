"""W09 / v3: LO splitting functions from the operator definitions (light-cone gauge A^+ = 0, W = 1).
 (a) D-dimensional real-emission kernels hat P_ij(z;eps) for q<-q, g<-q, q<-g, g<-g, computed with an
     explicit D-dimensional Minkowski algebra at integer D = 4,5,6,7 (CDR: Tr 1 = 4; gluon average
     1/(D-2), quark average 1/2) and compared with VF-PDF-6 exactly in D (rational in D);
 (b) delta(1-z) coefficients from quark-number and momentum conservation; the independent quark-column
     momentum check;
 (c) Mellin moments gamma_ij(N) (VF-PDF-8): direct integration N=1..12, non-integer N, large N;
 (d) N=2 singlet matrix, eigenvalues, asymptotic momentum fractions (VF-PDF-9);
 (e) one-loop f_{Q/g} with a heavy-quark mass (MS-bar), and the effect of the gluon polarisation average.
Normalisation (VF-PDF-6): f^real_{i/j}(xi) = g^2/(2pi)^{D-1} int d^{D-2}l_T hatP_ij(xi;eps)/l_T^2.
"""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
import mpmath as mp

npass = 0; nfail = 0
def check(name, ok):
    global npass, nfail
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)
    if ok: npass += 1
    else: nfail += 1

# ---------------- D-dimensional numeric Minkowski algebra --------------------------------------
class Mink:
    def __init__(self, Dd):
        self.D = Dd
        self.eta = np.diag([1.0] + [-1.0] * (Dd - 1))
    def dot(self, a, b):
        return a @ self.eta @ b
    def lc(self, vp, vm, vT):
        """vector from light-front components; vT = transverse components (length D-2) along axes 1..D-2;
        the longitudinal axis is the last one (index D-1)."""
        v = np.zeros(self.D, dtype=complex)
        v[0] = (vp + vm) / np.sqrt(2); v[self.D - 1] = (vp - vm) / np.sqrt(2)
        v[1:self.D - 1] = vT
        return v
    def basis(self):
        return [np.eye(self.D)[m].astype(complex) for m in range(self.D)]
    def trace(self, vecs):
        """CDR trace (Tr 1 = 4) of a product of slashed vectors."""
        n = len(vecs)
        if n == 0:
            return 4.0
        if n % 2:
            return 0.0
        a = vecs[0]; s = 0.0
        for k in range(1, n):
            s += (-1) ** (k - 1) * self.dot(a, vecs[k]) * self.trace(vecs[1:k] + vecs[k + 1:])
        return s

def kernels_at(Dd, z, lTmag, pplus=1.3):
    M = Mink(Dd)
    eps = (4 - Dd) / 2
    nT = Dd - 2
    lTdir = np.zeros(nT); lTdir[0] = 0.6; lTdir[1 % nT] += 0.8
    lTdir = lTdir / np.linalg.norm(lTdir)
    lTv = lTmag * lTdir
    p = M.lc(pplus, 0.0, np.zeros(nT))           # massless target along +z
    n = M.lc(0.0, 1.0, np.zeros(nT))             # n.v = v^+   (our n_B)
    nbar = M.lc(1.0, 0.0, np.zeros(nT))          # nbar.v = v^-  (our n_A)
    lp = (1 - z) * pplus
    l = M.lc(lp, lTmag ** 2 / (2 * lp), lTv)     # on-shell massless final parton
    k = p - l                                    # parton entering the operator, k^+ = z p^+
    k2 = M.dot(k, k)
    E = M.basis()
    g_up = np.linalg.inv(M.eta)
    def lower(v): return M.eta @ v
    # transverse metric (upper indices) g_perp^{mu nu}
    gperp = g_up - np.outer(n, nbar) - np.outer(nbar, n)
    # physical polarisation sum of an on-shell gluon q in light-cone gauge: d^{mu nu}(q) = -g + (q n + n q)/n.q
    def dpol(q):
        return -g_up + (np.outer(q, n) + np.outer(n, q)) / M.dot(n, q)
    phase = 1.0 / ((2 * np.pi) ** (Dd - 1))     # we return density per g^2 per d^{D-2}l_T/(2pi)^{D-1}: drop this
    out = {}
    # ---- q <- q : (1/2) Tr[pslash gamma^nu kslash gamma^+ kslash gamma^mu] d_{mu nu}(l) /(k^2)^2 ; C_F
    s = 0.0
    dl = dpol(l)
    for mu in range(Dd):
        for nu in range(Dd):
            c = dl[mu, nu]                        # d^{mu nu}: slashed E[mu] is gamma_mu (lower index)
            if abs(c) < 1e-15: continue
            s += c * M.trace([p, E[nu], k, n, k, E[mu]])
    sq = 0.5 * s / k2 ** 2
    # f = sum_X (1/2) delta(...) ... ; one-parton phase space 1/(2 l^+) ; (1/2) from int dw/(4pi): total factor 1/(2 l+) * 1/2
    out['qq'] = sq / (2 * lp) * 0.5 * lTmag ** 2      # times l_T^2 -> hat P_qq / C_F
    # ---- g <- q : (1/(xi p+)) * (1/(2 l+)) * (1/2)sum_spins sum_j |ubar(l) gamma_rho u(p) V^{j rho}|^2 /(k^2)^2 ; C_F
    # V^{j rho} = k^+ g^{rho j} - n^rho k^j   (gluon operator vertex with the light-cone-gauge numerator)
    # sum_j V V = -(k+)^2 g_perp + k+ (n kperp + kperp n) + n n k_T^2 ; kperp = transverse part of k
    kplus = M.dot(n, k); kT2 = -M.dot(k - kplus * nbar - M.dot(nbar, k) * n, k - kplus * nbar - M.dot(nbar, k) * n)
    kperp = k - kplus * nbar - M.dot(nbar, k) * n
    T = -kplus ** 2 * gperp + kplus * (np.outer(n, kperp) + np.outer(kperp, n)) + np.outer(n, n) * kT2
    # (1/2) Tr[lslash gamma_rho pslash gamma_rho'] = 2 (l_rho p_rho' + l_rho' p_rho - g_rho rho' l.p)
    lL = lower(l); pL = lower(p)
    Tr4 = 2 * (np.outer(lL, pL) + np.outer(pL, lL) - M.eta * M.dot(l, p))
    sg = np.sum(T * Tr4)
    out['gq'] = sg / k2 ** 2 / (z * pplus) / (2 * lp) * lTmag ** 2
    # ---- q <- g : (1/2)(1/(2 l+)) Tr[gamma^+ kslash gamma^mu lslash gamma^nu kslash] (avg over D-2 pol: -g_perp/(D-2)) /(k^2)^2 ; T_F
    # final antiquark l: sum v vbar = lslash ; initial gluon p polarisation average: sum eps^mu eps^nu* = -g_perp^{mu nu}
    s = 0.0
    for mu in range(Dd):
        for nu in range(Dd):
            c = -gperp[mu, nu] / (Dd - 2)          # upper indices (slashed E[mu] = gamma_mu)
            if abs(c) < 1e-15: continue
            s += c * M.trace([n, k, E[mu], l, E[nu], k])
    out['qg'] = 0.5 * s / k2 ** 2 / (2 * lp) * lTmag ** 2
    # ---- g <- g : (1/(xi p+))(1/(2 l+)) sum_j |X^j . P(k) . V3(p, -l, -k) . eps(p) eps'(l)|^2 /(k^2)^2 ; C_A
    # three-gluon vertex, all momenta incoming: V^{abc}_{mu nu rho}(q1,q2,q3) = g f^{abc}[g_{mu nu}(q1-q2)_rho + g_{nu rho}(q2-q3)_mu + g_{rho mu}(q3-q1)_nu]
    def V3(q1, q2, q3):
        q1L, q2L, q3L = lower(q1), lower(q2), lower(q3)
        V = np.zeros((Dd, Dd, Dd), dtype=complex)
        for a_, b_, c_ in itertools.product(range(Dd), repeat=3):
            V[a_, b_, c_] = (M.eta[a_, b_] * (q1L - q2L)[c_] + M.eta[b_, c_] * (q2L - q3L)[a_] + M.eta[c_, a_] * (q3L - q1L)[b_])
        return V  # lower indices
    # incoming momenta at the vertex: target gluon p (in), final gluon l (outgoing => -l incoming), operator gluon k (outgoing => -k)
    V = V3(p, -l, -k)    # indices (mu: target, nu: final l, rho: k-line)
    # k-line: light-cone propagator numerator P^{rho sigma} = g^{rho sigma} - (k n + n k)/n.k ; operator vertex V^{j}_sigma -> as above
    Pk = g_up - (np.outer(k, n) + np.outer(n, k)) / M.dot(n, k)
    # transverse unit vectors e_j (upper index, spatial components 1..D-2 = +1): A^j = e_j^rho ... use V^{j rho} = k+ e_j^rho... careful:
    # G^{+j} -> k^+ A^j - k^j A^+ ; A^j = component j (upper) = -e_{j rho} A^rho? we use contravariant component directly:
    # A^j = (unit vector u_j)_rho-lower contraction: A^j = delta^j_rho A^rho.
    amp2 = 0.0
    dP = -gperp      # target polarisation sum (upper) for p along z
    dL = dpol(l)
    # build for each transverse j the operator tensor O^j_rho (acting on A^rho): k^+ delta^j_rho - k^j n_rho
    Oj = []
    for j in range(1, Dd - 1):
        o = np.zeros(Dd, dtype=complex)
        o[j] += kplus                 # delta^j_rho (contravariant component j)
        o += -k[j] * lower(n)         # - k^j n_rho
        Oj.append(o)
    # amplitude tensor A^{j}_{mu nu} = O^j_rho P^{rho sigma} V_{mu nu sigma} ; then |A|^2 with pol sums dP^{mu mu'} dL^{nu nu'}
    for o in Oj:
        w = o @ Pk                    # w^sigma (upper)
        A = np.einsum('mns,s->mn', V, w)     # lower mu nu
        amp2 += np.einsum('mn,ab,ma,nb->', A, np.conj(A), dP, dL)
    out['gg'] = (amp2 / (Dd - 2)) / k2 ** 2 / (z * pplus) / (2 * lp) * lTmag ** 2
    return out, eps

def hatP(z, eps):
    return {'qq': (1 + z ** 2) / (1 - z) - eps * (1 - z),
            'gq': (1 + (1 - z) ** 2) / z - eps * z,
            'qg': 1 - 2 * z * (1 - z) / (1 - eps),
            'gg': 2 * (z / (1 - z) + (1 - z) / z + z * (1 - z))}
colour = {'qq': 'C_F', 'gq': 'C_F', 'qg': 'T_F', 'gg': 'C_A'}
for Dd in (4, 5, 6, 7):
    for z in (0.23, 0.61):
        for lT in (0.37, 1.9):
            res, e = kernels_at(Dd, z, lT)
            ref = hatP(z, e)
            for ch in ('qq', 'gq', 'qg', 'gg'):
                val = res[ch].real
                check('(a) D=%d z=%.2f lT=%.2f: l_T^2 x density[%s]/%s = %.10f vs hatP = %.10f' % (Dd, z, lT, ch, colour[ch], val, ref[ch]),
                      abs(val - ref[ch]) < 1e-9 * max(1, abs(ref[ch])))

# ---------------- (b) delta terms from conservation laws ------------------------------------------
z = sp.symbols('z', positive=True)
CF, CA, TF, nf = sp.symbols('C_F C_A T_F n_f', positive=True)
bq, bg = sp.symbols('b_q b_g')
def plus_int(gexpr, hexpr):
    """int_0^1 [g]_+ h = int g (h - h(1))"""
    return sp.integrate(sp.simplify(gexpr * (hexpr - hexpr.subs(z, 1))), (z, 0, 1))
# P_qq = C_F (1+z^2)[1/(1-z)]_+ + b_q delta ;   quark number: int P_qq = 0
eq_q = CF * sp.integrate(sp.cancel((1 + z ** 2 - 2) / (1 - z)), (z, 0, 1)) + bq
sol_bq = sp.solve(eq_q, bq)[0]
check('(b) quark number => b_q = 3/2 C_F', sp.simplify(sol_bq - sp.Rational(3, 2) * CF) == 0)
# P_gg = 2C_A[z[1/(1-z)]_+ + (1-z)/z + z(1-z)] + b_g delta ; momentum (gluon column): int z [P_gg + 2 n_f P_qg] = 0
Pqg = TF * (z ** 2 + (1 - z) ** 2)
Pgq = CF * (1 + (1 - z) ** 2) / z
mom_g = 2 * CA * (sp.integrate(sp.cancel((z ** 2 - 1) / (1 - z)), (z, 0, 1)) + sp.integrate(z * ((1 - z) / z + z * (1 - z)), (z, 0, 1))) + bg + 2 * nf * sp.integrate(z * Pqg, (z, 0, 1))
sol_bg = sp.solve(mom_g, bg)[0]
check('(b) momentum (gluon column) => b_g = 11/6 C_A - 2/3 n_f T_F = beta0/2', sp.simplify(sol_bg - (sp.Rational(11, 6) * CA - sp.Rational(2, 3) * nf * TF)) == 0)
# independent check: quark column  int z [P_qq + P_gq] = 0, with P_qq = C_F[(1+z^2)/(1-z)]_+ (plus on the whole)
intzPqq = CF * sp.integrate(sp.cancel((1 + z ** 2) * (z - 1) / (1 - z)), (z, 0, 1))
intzPgq = sp.integrate(z * Pgq, (z, 0, 1))
check('(b) quark column: int z P_qq = -4/3 C_F, int z P_gq = +4/3 C_F, sum = 0 (no free parameter)',
      sp.simplify(intzPqq + sp.Rational(4, 3) * CF) == 0 and sp.simplify(intzPgq - sp.Rational(4, 3) * CF) == 0)
# the two forms of P_qq agree: (1+z^2)[1/(1-z)]_+ + 3/2 delta
hs = [lambda t: t ** 2, lambda t: mp.exp(t), lambda t: 1 / (1 + t), lambda t: t ** 5]
for i, hh in enumerate(hs):
    lhs = mp.quad(lambda t: (1 + t ** 2) * (hh(t) - hh(1)) / (1 - t), [0, 1])
    rhs = mp.quad(lambda t: ((1 + t ** 2) * hh(t) - 2 * hh(1)) / (1 - t), [0, 1]) + 1.5 * hh(1)
    check('(b) [(1+z^2)/(1-z)]_+ = (1+z^2)[1/(1-z)]_+ + 3/2 delta (test %d)' % i, abs(lhs - rhs) < 1e-12)
# ---------------- (c) Mellin moments ---------------------------------------------------------------
N = sp.symbols('N', positive=True, integer=True)
def S1(n): return sum(sp.Rational(1, j) for j in range(1, n + 1))
gam = {
 'qq': lambda n: CF * (sp.Rational(3, 2) + sp.Rational(1, n * (n + 1)) - 2 * S1(n)),
 'qg': lambda n: TF * sp.Rational(n ** 2 + n + 2, n * (n + 1) * (n + 2)),
 'gq': lambda n: CF * sp.Rational(n ** 2 + n + 2, (n - 1) * n * (n + 1)),
 'gg': lambda n: 2 * CA * (sp.Rational(1, n * (n - 1)) + sp.Rational(1, (n + 1) * (n + 2)) - S1(n)) + sp.Rational(11, 6) * CA - sp.Rational(2, 3) * nf * TF,
}
def mom(ch, n):
    if ch == 'qq':
        return CF * sp.integrate(sp.cancel((z ** (n - 1) - 1) * (1 + z ** 2) / (1 - z)), (z, 0, 1)) + 0
    if ch == 'qg':
        return sp.integrate(z ** (n - 1) * Pqg, (z, 0, 1))
    if ch == 'gq':
        return sp.integrate(z ** (n - 1) * Pgq, (z, 0, 1))
    if ch == 'gg':
        reg = 2 * CA * (sp.integrate(sp.cancel((z ** n - 1) / (1 - z)), (z, 0, 1)) + sp.integrate(z ** (n - 1) * ((1 - z) / z + z * (1 - z)), (z, 0, 1)))
        return reg + sp.Rational(11, 6) * CA - sp.Rational(2, 3) * nf * TF
for ch in ('qq', 'qg', 'gq', 'gg'):
    ok = True
    for n in range(1 if ch in ('qq', 'qg') else 2, 13):
        if sp.simplify(mom(ch, n) - gam[ch](n)) != 0:
            ok = False; print('   mismatch', ch, n)
    check('(c) gamma_%s(N) closed form = direct Mellin integral, N up to 12' % ch, ok)
check('(c) gamma_qq(1) = 0', sp.simplify(gam['qq'](1)) == 0)
check('(c) gamma_qq(2) + gamma_gq(2) = 0', sp.simplify(gam['qq'](2) + gam['gq'](2)) == 0)
check('(c) 2 n_f gamma_qg(2) + gamma_gg(2) = 0', sp.simplify(2 * nf * gam['qg'](2) + gam['gg'](2)) == 0)
# non-integer N with S1(N) = psi(N+1) + gamma_E (numerical, C_F = 1)
for Nv in (1.37, 2.5, 3.91, 7.25):
    direct = mp.quad(lambda t: (t ** (Nv - 1) - 1) * (1 + t ** 2) / (1 - t), [0, 1])
    closed = 1.5 + 1 / (Nv * (Nv + 1)) - 2 * (mp.digamma(Nv + 1) + mp.euler)
    check('(c) gamma_qq(N)/C_F at non-integer N=%.2f: %.12f vs %.12f' % (Nv, direct, closed), abs(direct - closed) < 1e-10)
# key integral int (z^{N-1}-1)/(1-z) = -S1(N-1) at complex N
for Nv in (mp.mpc(2.3, 1.1), mp.mpc(0.7, -2.0)):
    direct = mp.quad(lambda t: (t ** (Nv - 1) - 1) / (1 - t), [0, 1])
    closed = -(mp.digamma(Nv) + mp.euler)
    check('(c) int (z^{N-1}-1)/(1-z) = -S1(N-1) at complex N=%s' % Nv, abs(direct - closed) < 1e-10)
# large N: gamma_qq -> -2 C_F (ln N + gE) + 3/2 C_F
for Nv in (1e3, 1e5):
    v = 1.5 + 1 / (Nv * (Nv + 1)) - 2 * (mp.digamma(Nv + 1) + mp.euler)
    a = -2 * (mp.log(Nv) + mp.euler) + 1.5
    check('(c) large N: gamma_qq/C_F + 2(ln N + gE) - 3/2 -> 0 (N=%g: %.2e)' % (Nv, v - a), abs(v - a) < 2.0 / Nv)

# ---------------- (d) N = 2 singlet matrix ----------------------------------------------------------
Mat = sp.Matrix([[gam['qq'](2), 2 * nf * gam['qg'](2)], [gam['gq'](2), gam['gg'](2)]])
check('(d) N=2 matrix = [[-4/3 C_F, 2/3 n_f T_F],[4/3 C_F, -2/3 n_f T_F]]',
      sp.simplify(Mat - sp.Matrix([[-sp.Rational(4, 3) * CF, sp.Rational(2, 3) * nf * TF], [sp.Rational(4, 3) * CF, -sp.Rational(2, 3) * nf * TF]])) == sp.zeros(2))
ev = Mat.eigenvals()
check('(d) eigenvalues {0, -(4C_F + 2 n_f T_F)/3}', set(sp.simplify(e) for e in ev) == {0, sp.simplify(-(4 * CF + 2 * nf * TF) / 3)})
# asymptotic fractions: eigenvector of eigenvalue 0: (Sigma, g) ~ (2 n_f T_F/3, 4C_F/3) normalised
null = Mat.nullspace()[0]
frac = sp.simplify(null[0] / (null[0] + null[1]))
fr3 = sp.simplify(frac.subs({CF: sp.Rational(4, 3), TF: sp.Rational(1, 2)}))
check('(d) <x>_Sigma -> 3 n_f/(16+3 n_f) for SU(3): %s' % fr3, sp.simplify(fr3 - 3 * nf / (16 + 3 * nf)) == 0)
print('   (d) n_f=5: <x>_Sigma = %s = %.4f, <x>_g = %.4f' % (fr3.subs(nf, 5), float(fr3.subs(nf, 5)), 1 - float(fr3.subs(nf, 5))), flush=True)
# NS LO evolution exponent: M_n(Q) = M_n(Q0) [as(Q)/as(Q0)]^{-2 gamma_qq(n)/beta0}
print('   (d) n=2: -2 gamma_qq(2)/beta0 = 8 C_F/(3 beta0); SU(3), n_f=4: %.6f' % (float(8 * sp.Rational(4, 3) / (3 * (11 - sp.Rational(8, 3))))), flush=True)

# ---------------- (e) massive-quark f_{Q/g}; polarisation average ------------------------------------
# massive q<-g in D dims: (1/2)(1/(2l+)) Tr[g+ (k+m) g^mu (l-m) g^nu (k+m)] (-g_perp^{mu nu}/(D-2)) /(k^2-m^2)^2 ; T_F
def mtrace(M, factors):
    """CDR trace of a product of factors, each factor a list of (coef, vector or None) (None = identity)."""
    tot = 0.0
    for combo in itertools.product(*factors):
        c = 1.0; vecs = []
        for (cf, v) in combo:
            c *= cf
            if v is not None: vecs.append(v)
        if c != 0: tot += c * M.trace(vecs)
    return tot
def fQg_densityD(Dd, z, lT, mq, pplus=1.1):
    M = Mink(Dd); nT = Dd - 2
    p = M.lc(pplus, 0.0, np.zeros(nT)); n = M.lc(0.0, 1.0, np.zeros(nT)); nbar = M.lc(1.0, 0.0, np.zeros(nT))
    lp = (1 - z) * pplus
    lTv = np.zeros(nT); lTv[0] = 0.6 * lT; lTv[1 % nT] += 0.8 * lT
    l = M.lc(lp, (lT ** 2 + mq ** 2) / (2 * lp), lTv)
    k = p - l
    den = (M.dot(k, k) - mq ** 2) ** 2
    g_up = np.linalg.inv(M.eta)
    gperp = g_up - np.outer(n, nbar) - np.outer(nbar, n)
    E = M.basis()
    s = 0.0
    for mu in range(Dd):
        for nu in range(Dd):
            c = -gperp[mu, nu] / (Dd - 2)
            if abs(c) < 1e-15: continue
            s += c * mtrace(M, [[(1, n)], [(1, k), (mq, None)], [(1, E[mu])], [(1, l), (-mq, None)], [(1, E[nu])], [(1, k), (mq, None)]])
    return (0.5 * s / den / (2 * lp)).real
for Dd in (4, 5, 6):
    e = (4 - Dd) / 2
    for z0 in (0.3, 0.7):
        for lT in (0.2, 1.5):
            mq = 0.4
            val = fQg_densityD(Dd, z0, lT, mq)
            guess = ((1 - 2 * z0 * (1 - z0) / (1 - e)) * lT ** 2 + mq ** 2) / (lT ** 2 + mq ** 2) ** 2
            check('(e) D=%d massive q<-g density = [ hatP_qg(z,eps) l_T^2 + m^2 ]/(l_T^2+m^2)^2 (z=%.1f lT=%.1f): %.10f vs %.10f' % (Dd, z0, lT, val, guess), abs(val - guess) < 1e-10)
eps = sp.symbols('epsilon')
zz = sp.symbols('zz', positive=True)
mm = sp.symbols('m2', positive=True)
d = 2 - 2 * eps
def master(a, b, M2):
    return sp.pi ** (d / 2) * sp.gamma(a + d / 2) * sp.gamma(b - a - d / 2) / (sp.gamma(d / 2) * sp.gamma(b)) * M2 ** (a + d / 2 - b)
hatPqg = 1 - 2 * zz * (1 - zz) / (1 - eps)
bare = hatPqg * master(1, 2, mm) + mm * master(0, 2, mm)
mu2 = sp.symbols('mu2', positive=True)
expr = sp.exp(eps * sp.EulerGamma) * mu2 ** eps * bare / sp.pi ** (1 - eps)
ser = sp.series(expr, eps, 0, 1).removeO()
pole = sp.simplify(ser.coeff(eps, -1))
finite = sp.simplify(ser.coeff(eps, 0))
Pqg0 = zz ** 2 + (1 - zz) ** 2
check('(e) f_{Q/g}: UV pole = P_qg/T_F (units alpha_s/2pi T_F 1/eps)', sp.simplify(pole - Pqg0) == 0)
check('(e) f_{Q/g}: MS-bar finite part = (P_qg/T_F) ln(mu^2/m^2), no constant  [got %s]' % finite,
      sp.simplify(sp.expand(sp.expand_log(finite - Pqg0 * sp.log(mu2 / mm), force=True))) == 0)
# polarisation average: averaging over 2 instead of D-2 multiplies the q<-g kernel by (1-eps)
zz = sp.symbols('zz')
diff = sp.series(TF * (1 - 2 * zz * (1 - zz) / (1 - eps)) * (1 - eps) - TF * (1 - 2 * zz * (1 - zz) / (1 - eps)), eps, 0, 2).removeO()
check('(e) 2-polarisation average shifts the kernel by -eps P_qg + O(eps^2): (1-eps)hatP - hatP = %s' % sp.simplify(diff),
      sp.simplify(diff + eps * TF * (zz ** 2 + (1 - zz) ** 2)) == 0)
print('\nSUMMARY v3: %d PASS, %d FAIL' % (npass, nfail), flush=True)
