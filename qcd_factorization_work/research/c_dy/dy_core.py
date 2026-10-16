# -*- coding: utf-8 -*-
"""
dy_core.py -- exact-in-epsilon building blocks of the O(alpha_s) Drell-Yan coefficient functions.

Normalisation (see DERIVATION.md section 2.1):
    shat dsigma_ij/dQ^2 = sigma_0 e_q^2 (1-eps) Delta_ij^bare(z, eps),   sigma_0 = 4 pi alpha^2/(3 N_c Q^2),
    Delta_ij^bare = N_c/(2 pi e_q^2 (1-eps)) * int dPhi_{gamma* X} <-g_{mu nu} H^mu H^nu*>,
i.e. everything is divided by the D-dimensional Born (the factor (1-eps) is the D-dim Born trace (D-2)/2;
the lepton tensor is kept in 4 dimensions and cancels in the ratio).
Bare coupling: g0^2 = 4 pi alpha_s mu^{2 eps} e^{eps gamma_E} (4 pi)^{-eps}   (CONTEXT: MS-bar, S_eps).
All results are returned in units of a = alpha_s/(2 pi); L = ln(mu^2/Q^2).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
import mpmath as mp
from dtrace import V, I, D, string_product, make_trace

eps = sp.Symbol('epsilon')
z = sp.Symbol('z', positive=True)
v = sp.Symbol('v', positive=True)
x, y = sp.symbols('x y', positive=True)
L = sp.Symbol('L', real=True)          # ln(mu^2/Q^2)
CF, TF = sp.symbols('C_F T_F', positive=True)
s, t, u = sp.symbols('s t u')
EG = sp.EulerGamma


# =====================================================================  matrix elements
def T_qqbar():
    """sum over spins of |vbar(p2) Gamma^{mu a} u(p1)|^2 contracted with (-g_{mu nu})(-g_{ab}),
    q(p1) qbar(p2) -> gamma*(q) g(k);  t=(p1-k)^2, u=(p2-k)^2, s=(p1+p2)^2 (couplings stripped)."""
    dots = {('p1', 'p1'): 0, ('p2', 'p2'): 0, ('k', 'k'): 0, ('p1', 'p2'): s / 2, ('p1', 'k'): -t / 2, ('p2', 'k'): -u / 2}
    tr = make_trace(lambda a, b: dots[(a, b)] if (a, b) in dots else dots[(b, a)])
    A1 = {'p1': 1, 'k': -1}; A2 = {'k': 1, 'p2': -1}
    G = [([I('mu'), A1, I('a')], 1 / t), ([I('a'), A2, I('mu')], 1 / u)]
    Gb = [([I('a'), A1, I('mu')], 1 / t), ([I('mu'), A2, I('a')], 1 / u)]
    T = sum(c1 * c2 * tr(string_product([V('p2')] + g1 + [V('p1')] + g2)) for g1, c1 in G for g2, c2 in Gb)
    return sp.factor(sp.simplify(T.subs(D, 4 - 2 * eps)))


def T_qg():
    """q(p1) g(p2) -> gamma*(q) q(k);  s=(p1+p2)^2, t=(p2-k)^2, u=(p1-k)^2 (couplings stripped)."""
    dots = {('p1', 'p1'): 0, ('p2', 'p2'): 0, ('k', 'k'): 0, ('p1', 'p2'): s / 2, ('p1', 'k'): -u / 2, ('p2', 'k'): -t / 2}
    tr = make_trace(lambda a, b: dots[(a, b)] if (a, b) in dots else dots[(b, a)])
    B1 = {'p1': 1, 'p2': 1}; B2 = {'k': 1, 'p2': -1}          # p1 - q = k - p2
    G = [([I('mu'), B1, I('a')], 1 / s), ([I('a'), B2, I('mu')], 1 / t)]
    Gb = [([I('a'), B1, I('mu')], 1 / s), ([I('mu'), B2, I('a')], 1 / t)]
    T = sum(c1 * c2 * tr(string_product([V('k')] + g1 + [V('p1')] + g2)) for g1, c1 in G for g2, c2 in Gb)
    return sp.factor(sp.simplify(T.subs(D, 4 - 2 * eps)))


# =====================================================================  phase space
def beta_int(expr):
    """exact int_0^1 dv [v(1-v)]^{-eps} expr(v) for expr = polynomial(v)/(v^a (1-v)^b), a,b in {0,1}."""
    num, den = sp.fraction(sp.together(expr))
    num = sp.expand(num)
    a = 1 if sp.simplify(den.subs(v, 0)) == 0 else 0
    b = 1 if sp.simplify(den.subs(v, 1)) == 0 else 0
    rest = sp.simplify(den / (v**a * (1 - v)**b))
    assert not rest.has(v), rest
    poly = sp.Poly(sp.expand(num / rest), v)
    tot = 0
    # write v^n (1-v)^0 ; integral of v^{n-a-eps} (1-v)^{-b-eps}
    for (n,), c in poly.terms():
        tot += c * sp.gamma(n - a + 1 - eps) * sp.gamma(1 - b - eps) / sp.gamma(n - a + 2 - b - 2 * eps)
    return tot


def real_qqbar_exact():
    """Delta^R_{q qbar}(z,eps) / a  as  C_F e^{eps L} * Pref(eps) * z^eps (1-z)^{-1-2eps} * Greg(z,eps).
    Returns (Pref, Greg) with Greg regular at z=1."""
    T = T_qqbar()
    # T depends only on ratios (s Q^2/(t u) etc.), so the overall scale s drops out once t,u are expressed via z,v
    Tv = sp.simplify(T.subs({t: -s * (1 - z) * v, u: -s * (1 - z) * (1 - v)}))
    assert not Tv.has(s)
    Iv = sp.simplify(beta_int(Tv))
    # Delta^R/a = C_F (mu^2/shat)^eps e^{eps gE}/Gamma(1-eps) (1-z)^{1-2eps}/(8(1-eps)) Iv ; (mu^2/shat)^eps = e^{eps L} z^eps
    Pref = sp.exp(eps * EG) / sp.gamma(1 - eps)
    Greg = sp.simplify((1 - z)**2 * Iv / (8 * (1 - eps)))      # (1-z)^{1-2eps} = (1-z)^{-1-2eps} (1-z)^2
    return Pref, Greg, T, Iv


def real_qg_exact():
    """Delta^R_{qg}(z,eps)/a = T_F e^{eps L} Pref z^eps (1-z)^{-2 eps} Hreg(z,eps)."""
    T = T_qg()
    Tv = sp.simplify(T.subs({t: -s * (1 - z) * (1 - v), u: -s * (1 - z) * v}))
    assert not Tv.has(s)
    Iv = sp.simplify(beta_int(Tv))
    Pref = sp.exp(eps * EG) / sp.gamma(1 - eps)
    Hreg = sp.simplify((1 - z) * Iv / (8 * (1 - eps)**2))      # (1-z)^{1-2eps} = (1-z)^{-2eps}(1-z)
    return Pref, Hreg, T, Iv


# =====================================================================  virtual: one-loop vertex
def vertex_exact():
    """One-loop q qbar gamma* vertex, massless, Feynman gauge, bare, D dims.
    Returns f(eps) with  F^(1) = (alpha_s/4pi) C_F (mu^2/X)^eps f(eps),  X = -q^2 - i0 ."""
    S = sp.Symbol('S', positive=True)  # S = q^2 = 2 p1.p2 (only appears via Delta = x y (-S))
    dots = {('p1', 'p1'): 0, ('p2', 'p2'): 0, ('p1', 'p2'): S / 2}
    tr = make_trace(lambda a, b: dots[(a, b)] if (a, b) in dots else dots[(b, a)])
    # k = l - x p2 + y p1 ; (-p2 - k) = -l - (1-x) p2 - y p1 ; (p1 - k) = -l + (1-y) p1 + x p2
    A0 = {'p2': -(1 - x), 'p1': -y}
    B0 = {'p1': (1 - y), 'p2': x}
    N0 = tr(string_product([V('p2'), I('al'), A0, I('mu'), B0, I('al'), V('p1'), I('mu')]))
    # l-slash ... l-slash -> (l^2/D) gamma^rho ... gamma_rho   [(-l)(-l) = +]
    N2 = tr(string_product([V('p2'), I('al'), I('rho'), I('mu'), I('rho'), I('al'), V('p1'), I('mu')])) / D
    Tr0 = tr(string_product([V('p2'), I('mu'), V('p1'), I('mu')]))
    N0 = sp.expand(sp.simplify((N0 / Tr0).subs(D, 4 - 2 * eps)))
    N2 = sp.expand(sp.simplify((N2 / Tr0).subs(D, 4 - 2 * eps)))
    # integrals (Peskin A.44/A.45), with Delta = x y X, X = -S - i0:
    #   int d^Dl/(2pi)^D 1/(l^2-Delta)^3     = -i/(4pi)^{D/2} Gamma(1+eps)/2 Delta^{-1-eps}
    #   int d^Dl/(2pi)^D l^2/(l^2-Delta)^3   =  i/(4pi)^{D/2} (D/4) Gamma(eps) Delta^{-eps}
    # Gamma_1 = -i g0^2 C_F * 2 int dF [...];  g0^2/(4pi)^{D/2} = alpha_s mu^{2eps} e^{eps gE}/(4pi)
    # => F1 = (alpha_s/4pi) C_F e^{eps gE} mu^{2eps} * 2 int dF [ -N0 Gamma(1+eps)/2 (xyX)^{-1-eps} + N2 (D/4)Gamma(eps)(xyX)^{-eps} ]
    # N0 is proportional to S = -X: write N0 = S*n0(x,y) -> -N0 X^{-1-eps} = S X^{-1-eps} n0 ... = -X^{-eps} n0 * (S/(-X)) ; S/(-X)=1
    n0 = sp.expand(sp.simplify(N0 / S))
    assert not n0.has(S) and not N2.has(S)

    def fint(poly, shift):
        # 2 * int_0^1 dx int_0^{1-x} dy poly(x,y) (x y)^{shift}
        P = sp.Poly(sp.expand(poly), x, y)
        tot = 0
        for (i, j), c in P.terms():
            a = i + shift + 1; b = j + shift + 1
            tot += c * sp.gamma(a) * sp.gamma(b) / sp.gamma(a + b + 1)
        return 2 * tot
    # term1: -N0 Gamma(1+eps)/2 (xy)^{-1-eps} X^{-1-eps} = -(S n0) X^{-1-eps}(...) = +n0 X^{-eps} (since S = -X)
    term1 = sp.gamma(1 + eps) / 2 * fint(n0, -1 - eps)
    term2 = (4 - 2 * eps) / 4 * sp.gamma(eps) * fint(N2, -eps)
    f = sp.exp(eps * EG) * (term1 + term2)      # F1 = (alpha_s/4pi) C_F (mu^2/X)^eps * f
    return sp.simplify(sp.gammasimp(f)), n0, N2


# =====================================================================  distributions on [0,1]
class Dist:
    """a*delta(1-z) + sum_k b_k D_k(z) + reg(z),   D_k = [ln^k(1-z)/(1-z)]_+ ,  b_k, a constants."""
    def __init__(self, delta=0, plus=None, reg=0):
        self.delta = sp.sympify(delta)
        self.plus = {k: sp.sympify(c) for k, c in (plus or {}).items()}
        self.reg = sp.sympify(reg)

    def __add__(self, o):
        p = dict(self.plus)
        for k, c in o.plus.items():
            p[k] = p.get(k, 0) + c
        return Dist(self.delta + o.delta, p, self.reg + o.reg)

    def __sub__(self, o):
        return self + o.scale(-1)

    def scale(self, c):
        return Dist(c * self.delta, {k: c * b for k, b in self.plus.items()}, c * self.reg)

    @staticmethod
    def g_times_Dk(g, k):
        """g(z) * D_k  (g smooth at z=1) in canonical form."""
        g1 = sp.simplify(g.subs(z, 1))
        rem = sp.simplify(sp.cancel((g - g1) / (1 - z)))
        return Dist(0, {k: g1}, rem * sp.log(1 - z)**k)

    def simplify(self):
        return Dist(sp.simplify(self.delta),
                    {k: sp.simplify(c) for k, c in self.plus.items() if sp.simplify(c) != 0},
                    sp.simplify(self.reg))

    def subs(self, d):
        return Dist(self.delta.subs(d), {k: c.subs(d) for k, c in self.plus.items()}, self.reg.subs(d))

    def act(self, h, dps=30):
        """numerical <Dist, h> for a python/mpmath function h on [0,1]."""
        mp.mp.dps = dps
        val = mp.mpf(sp.N(self.delta, dps)) * h(mp.mpf(1))
        for k, c in self.plus.items():
            ck = mp.mpf(sp.N(c, dps))
            val += ck * mp.quad(lambda w: (h(w) - h(1)) * mp.log(1 - w)**k / (1 - w), [0, 0.5, 1])
        if self.reg != 0:
            f = sp.lambdify(z, self.reg, 'mpmath')
            val += mp.quad(lambda w: f(w) * h(w), [0, 0.5, 1])
        return val

    def __repr__(self):
        return 'Dist(delta=%s, plus=%s, reg=%s)' % (self.delta, self.plus, self.reg)


def dist_equal(A, B, tests=None, tol=1e-20):
    """exact comparison of canonical forms + numerical test-function comparison."""
    dd = sp.simplify(A.delta - B.delta) == 0
    keys = set(A.plus) | set(B.plus)
    dp = all(sp.simplify(A.plus.get(k, 0) - B.plus.get(k, 0)) == 0 for k in keys)
    w_ = sp.Symbol('w_', positive=True)       # w_ = 1-z > 0 lets sympy expand ln((1-z)^2/z)
    diff_reg = sp.expand_log(sp.expand((A.reg - B.reg).subs(z, 1 - w_)), force=True)
    dr = sp.simplify(diff_reg) == 0
    if not dr:  # numerical fallback for the regular part (random values for any other parameters)
        other = sorted((diff_reg.free_symbols - {w_}), key=str)
        vals = {sym: sp.Rational(3 + 2 * i, 7 + i) for i, sym in enumerate(other)}
        f = sp.lambdify(z, (A.reg - B.reg).subs(vals), 'mpmath')
        mp.mp.dps = 40
        dr = all(abs(f(mp.mpf(w))) < 1e-30 for w in ['0.013', '0.21', '0.5', '0.77', '0.991'])
    num = True
    if tests:
        for h in tests:
            num = num and abs(A.act(h) - B.act(h)) < tol
    return dd, dp, dr, num


def expand_plus(Hz, order):
    """(1-z)^{-1-2eps} * Hz(z,eps)  ->  dict {power of eps: Dist}, up to eps^order (inclusive).
    Uses (1-z)^{-1-2eps} = -delta(1-z)/(2eps) + sum_k (-2eps)^k/k! D_k  (exact as distributions on [0,1])."""
    res = {}
    # delta part: -1/(2 eps) * Hz(1, eps)
    H1 = sp.series(Hz.subs(z, 1), eps, 0, order + 2).removeO()
    for p in range(-3, order + 1):
        c = sp.expand(H1).coeff(eps, p + 1)
        if c != 0:
            res.setdefault(p, Dist())
            res[p] = res[p] + Dist(delta=-c / 2)
    Hser = sp.series(Hz, eps, 0, order + 1).removeO()
    Hser = sp.expand(Hser)
    for k in range(0, order + 3):
        for j in range(-3, order + 1):
            p = j + k
            if p > order:
                continue
            hj = Hser.coeff(eps, j)
            if hj == 0:
                continue
            term = Dist.g_times_Dk(sp.simplify(hj * (-2)**k / sp.factorial(k)), k)
            res.setdefault(p, Dist())
            res[p] = res[p] + term
    return res


def expand_regular(Hz, order):
    """pointwise Laurent expansion of a function regular-in-z (no distributions needed)."""
    ser = sp.expand(sp.series(Hz, eps, 0, order + 1).removeO())
    res = {}
    for p in range(-3, order + 1):
        c = ser.coeff(eps, p)
        if c != 0:
            res[p] = Dist(reg=sp.simplify(c))
    return res


# 4-dim LO splitting functions (P = sum_n (alpha_s/2pi)^n P^(n)), canonical form
def P_qq():
    return Dist(delta=CF * sp.Rational(3, 2), plus={0: 2 * CF}, reg=-CF * (1 + z))


def P_qg():
    return Dist(reg=TF * (z**2 + (1 - z)**2))
