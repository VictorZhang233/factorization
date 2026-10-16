# -*- coding: utf-8 -*-
"""
s5_cv.py -- Ch20 prop:heavy-nrqcd-matching (b) and ex:heavy-cv: one-loop matching coefficient c_v of the
 heavy-quark vector current at threshold in dimensional regularization (D = 4 - 2 eps, UV and IR), Feynman gauge.
 * vertex correction projected on the S-wave spin-triplet threshold state (p1 = p2 = p, p^2 = m^2), exact in eps,
   with our Feynman rules (vertex i g gamma^mu t^a, quark i(pslash+m)/(p^2-m^2), gluon -i g_{mu nu}/k^2);
 * on-shell wave-function renormalization delta Z_2^OS from Sigma(pslash), exact in eps;
 * c_v = 1 + delta_V + delta Z_2  (NRQCD side scaleless at threshold);  expected (VF-NRQ-4):
   delta_V = a (3/eps - 4 + 3 L), delta Z_2 = -a (3/eps + 4 + 3 L), a = alpha_s C_F/(4 pi), L = ln(mu^2/m^2),
   c_v = 1 - 2 C_F alpha_s/pi,  |c_v|^2 = 1 - 4 C_F alpha_s/pi = 1 - 16 alpha_s/(3 pi) (N_c = 3).
 * pole structure: the vertex pole 3/eps = 1/eps_UV + 2/eps_IR (UV part from the l^2 term, IR part from the
   Coulomb pinch of the Feynman-parameter integral at a = 0).
D-dimensional Dirac algebra: contraction identities for gamma^alpha ... gamma_alpha and the recursive trace of
 slashed D-vectors (Tr 1 = 4); loop-momentum tensor reduction l^mu l^nu -> l^2 g^{mu nu}/D.
Run: python3 -I s5_cv.py
"""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w23common import *

ck = Check('s5_cv: one-loop c_v at threshold in DR (vertex + on-shell Z_2), exact in eps')

eps = sp.symbols('epsilon')
D = 4 - 2 * eps
m, mu = sp.symbols('m mu', positive=True)
a = sp.symbols('a', real=True)                 # Feynman-parameter combination a = x1 - x2

# ---------------------------------------------------------------- vectors and dot products
# vectors: p (p^2 = m^2), e (polarization of the current, e.p = 0), f (spin polarization of the QQbar state, f.p = 0),
# l (loop momentum after the shift k = l + a p).  'k' is expanded as l + a p at the dot-product level.
ef, ee_, ff, lp, le, lf, ll = sp.symbols('ef ee ff lp le lf ll')
def dot(x, y):
    key = tuple(sorted((x, y)))
    table = {('p', 'p'): m**2, ('e', 'p'): 0, ('f', 'p'): 0, ('e', 'f'): ef, ('e', 'e'): ee_, ('f', 'f'): ff,
             ('l', 'p'): lp, ('e', 'l'): le, ('f', 'l'): lf, ('l', 'l'): ll}
    if 'k' in key:
        other = key[0] if key[1] == 'k' else key[1]
        if other == 'k':
            return dot('l', 'l') + 2 * a * dot('l', 'p') + a**2 * dot('p', 'p')
        return dot('l', other) + a * dot('p', other)
    return table[key]

from functools import lru_cache
@lru_cache(maxsize=None)
def trace(vs):
    """Tr of a product of slashed D-vectors (tuple of names); Tr 1 = 4."""
    n = len(vs)
    if n == 0:
        return sp.Integer(4)
    if n % 2 == 1:
        return sp.Integer(0)
    res = 0
    for j in range(1, n):
        sign = (-1)**(j - 1)
        rest = vs[1:j] + vs[j + 1:]
        res += sign * dot(vs[0], vs[j]) * trace(rest)
    return sp.expand(res)

# Dirac strings: dict {tuple(vectors): coefficient}
def S(*terms):
    d = {}
    for coeff, vec in terms:
        d[vec] = d.get(vec, 0) + coeff
    return d
def mul(A, B):
    out = {}
    for va, ca in A.items():
        for vb, cb in B.items():
            out[va + vb] = out.get(va + vb, 0) + ca * cb
    return out
def add(*As):
    out = {}
    for A in As:
        for v_, c in A.items():
            out[v_] = out.get(v_, 0) + c
    return out
def scal(c, A):
    return {v_: c * cc for v_, cc in A.items()}
def tr(A):
    return sp.expand(sum(c * trace(v_) for v_, c in A.items()))
one = S((1, ()))
def sl(*lin):            # slash of a linear combination: sl((c1,'p'),(c2,'k'))
    return S(*[(c, (n,)) for c, n in lin])

# ---------------------------------------------------------------- contraction identities (D dims)
def contract_3(A_, X_, B_):
    """gamma^alpha Aslash Xslash Bslash gamma_alpha = -2 Bslash Xslash Aslash + (4-D) Aslash Xslash Bslash for single vectors"""
    raise NotImplementedError
# We apply the identities on the expanded numerator directly: N = gamma^alpha (Aslash + m) eslash (Bslash + m) gamma_alpha,
# A = p - k, B = -p - k (single slashed vectors after linear expansion).
def g_contract(vs):
    """gamma^alpha [product of slashed vectors vs] gamma_alpha, as a Dirac string (len(vs) <= 3)."""
    n = len(vs)
    if n == 0:
        return S((D, ()))
    if n == 1:
        return S((-(D - 2), vs))
    if n == 2:
        return S((4 * dot(vs[0], vs[1]), ()), (-(4 - D), vs))
    if n == 3:
        return S((-2, (vs[2], vs[1], vs[0])), ((4 - D), vs))
    raise ValueError

def gamma_sandwich(Astr):
    """gamma^alpha (Dirac string) gamma_alpha, linear in the string."""
    out = {}
    for vs, c in Astr.items():
        for v2, c2 in g_contract(vs).items():
            out[v2] = out.get(v2, 0) + c * c2
    return out

# ---------------------------------------------------------------- self-test of the trace engine vs explicit 4x4 (D = 4)
import numpy as np
I2 = np.eye(2); Z2 = np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
G = [np.block([[I2, Z2], [Z2, -I2]]).astype(complex)] + [np.block([[Z2, s], [-s, Z2]]) for s in (sx, sy, sz)]
met = np.diag([1., -1, -1, -1])
rng = np.random.default_rng(1)
vecs = {n: rng.normal(size=4) for n in ['p', 'e', 'f', 'l']}
def slm(v_):
    vl = met @ v_
    return sum(G[i] * vl[i] for i in range(4))
dnum = lambda x, y: vecs[x] @ met @ vecs[y]
okt = True
for vs in [('p', 'e'), ('p', 'e', 'f', 'l'), ('p', 'l', 'e', 'p', 'f', 'l'), ('e', 'p', 'l', 'f', 'p', 'e', 'l', 'p')]:
    sym = trace(vs)
    subs = {m**2: dnum('p', 'p'), ef: dnum('e', 'f'), ee_: dnum('e', 'e'), ff: dnum('f', 'f'), lp: dnum('l', 'p'),
            le: dnum('l', 'e'), lf: dnum('l', 'f'), ll: dnum('l', 'l')}
    # the symbolic table assumes e.p = f.p = 0: choose numerical vectors with that property
    okt = okt and True
# use orthogonalized numerical vectors for the check
pnum = np.array([1.3, 0.2, -0.4, 0.5])
def orth(v_):
    return v_ - (v_ @ met @ pnum) / (pnum @ met @ pnum) * pnum
vecs = {'p': pnum, 'e': orth(rng.normal(size=4)), 'f': orth(rng.normal(size=4)), 'l': rng.normal(size=4)}
for vs in [('p', 'e'), ('p', 'e', 'f', 'l'), ('p', 'l', 'e', 'p', 'f', 'l'), ('e', 'p', 'l', 'f', 'p', 'e', 'l', 'p')]:
    sym = trace(vs)
    subs = {m: np.sqrt(dnum('p', 'p')), ef: dnum('e', 'f'), ee_: dnum('e', 'e'), ff: dnum('f', 'f'), lp: dnum('l', 'p'),
            le: dnum('l', 'e'), lf: dnum('l', 'f'), ll: dnum('l', 'l')}
    val = complex(sym.subs(subs))
    M_ = np.eye(4, dtype=complex)
    for n in vs:
        M_ = M_ @ slm(vecs[n])
    okt = okt and abs(val - np.trace(M_)) < 1e-9
ck('trace engine agrees with explicit 4x4 Dirac matrices (D = 4)', okt)
# contraction identities at D = 4 vs explicit
okc = True
for vs in [('p',), ('p', 'l'), ('p', 'e', 'l')]:
    lhs = sum(G[al] @ np.linalg.multi_dot([slm(vecs[n]) for n in vs] + [np.eye(4)]) @ G[al] * met[al, al] for al in range(4))
    rhs = np.zeros((4, 4), complex)
    for v2, c in g_contract(vs).items():
        cnum = complex(sp.sympify(c).subs({eps: 0, m: np.sqrt(dnum('p', 'p')), ef: dnum('e', 'f'), lp: dnum('l', 'p'),
                                            le: dnum('l', 'e'), lf: dnum('l', 'f'), ll: dnum('l', 'l')}))
        Mv = np.eye(4, dtype=complex)
        for n in v2:
            Mv = Mv @ slm(vecs[n])
        rhs += cnum * Mv
    okc = okc and np.allclose(lhs, rhs)
ck('gamma^alpha ... gamma_alpha contraction identities agree with explicit matrices at D = 4', okc)

# ---------------------------------------------------------------- vertex numerator
Aslash = sl((1, 'p'), (-1, 'k'))      # p - k  (quark line between gluon vertex and current, momentum p1 - k)
Bslash = sl((-1, 'p'), (-1, 'k'))     # -p - k (antiquark side, momentum -p2 - k)
eslash = sl((1, 'e'))
X1 = add(Aslash, scal(m, one)); X2 = add(Bslash, scal(m, one))
inner = mul(mul(X1, eslash), X2)                 # (Aslash + m) eslash (Bslash + m)
Nvert = gamma_sandwich(inner)                    # gamma^alpha ... gamma_alpha
proj = mul(mul(add(sl((1, 'p')), scal(-m, one)), sl((1, 'f'))), add(sl((1, 'p')), scal(m, one)))   # (pslash - m) fslash (pslash + m)
T_loop = tr(mul(Nvert, proj))
T_tree = tr(mul(eslash, proj))
ck('tree: Tr[eslash (pslash - m) fslash (pslash + m)] = -8 m^2 (e.f)', sp.simplify(T_tree + 8 * m**2 * ef) == 0, sp.factor(T_tree))
# tensor reduction in l: odd terms vanish; lp^2, le^2, ... -> ll (u.w)/D
T = sp.expand(T_loop)
poly = sp.Poly(T, lp, le, lf, ll)
red = 0
for (e1, e2, e3, e4), c in poly.terms():
    deg = e1 + e2 + e3 + 2 * e4
    if deg == 0:
        red += c
    elif deg % 2 == 1:
        continue
    elif deg == 2:
        if e4 == 1:
            red += c * ll
        else:
            # pair of (l.u)(l.w): u,w from p,e,f
            us = ['p'] * e1 + ['e'] * e2 + ['f'] * e3
            red += c * ll * dot(us[0], us[1]) / D
    else:
        raise ValueError('unexpected l power')
red = sp.expand(red)
T0 = sp.expand(red.subs(ll, 0)); T2 = sp.expand(sp.diff(red, ll))
ck('numerator after reduction is T0(a) + T2 * l^2 (no higher powers)', sp.expand(red - T0 - T2 * ll) == 0)
# normalize by the tree: ratios r0 = T0/T_tree, r2 = T2/T_tree (both independent of e.f)
r0 = sp.simplify(T0 / T_tree); r2 = sp.simplify(T2 / T_tree)
print('   T0/T_tree =', sp.factor(r0)); print('   T2/T_tree =', sp.factor(r2))
ck('ratios independent of the polarizations', not r0.has(ef) and not r2.has(ef))

# ---------------------------------------------------------------- integrals
# Lambda = -i g^2 C_F mu^{2eps} S_eps^{-1} * 2 int dF int d^Dl/(2pi)^D [T0 + T2 l^2]/(l^2 - Delta)^3, Delta = a^2 m^2
# int d^Dl/(2pi)^D 1/(l^2-Delta)^3 = -i/(4pi)^{D/2} Gamma(1+eps)/2 Delta^{-1-eps}
# int d^Dl/(2pi)^D l^2/(l^2-Delta)^3 = +i/(4pi)^{D/2} (D/2) Gamma(eps)/2 Delta^{-eps}
# g^2 mu^{2eps} S_eps^{-1}/(4pi)^{D/2} = (alpha_s/(4pi)) mu^{2eps} e^{eps gamma_E}
# => delta_V = (alpha_s C_F/4pi) e^{eps gE} mu^{2eps} * 2 int dF [ -Gamma(1+eps)/2 r0 Delta^{-1-eps} + (D/2)Gamma(eps)/2 r2 Delta^{-eps} ] * (-i)(i)(sign)
# prefactor: -i * (-i) = -1 for the T0 term; -i * (+i) = +1 for the T2 term.
gE = sp.EulerGamma
# Feynman measure: 2 int dx1 dx2 f(x1-x2) = 2 * int_{-1}^{1} da (1-|a|)/2 f(a) = 2 int_0^1 da (1-a) f_even(a)
def fp_integral(poly_a, p_exp):
    """2 int_0^1 da (1 - a) [even part of poly_a(a)] * a^p_exp   (the measure 2 int dx1 dx2 over the simplex,
    written in a = x1 - x2; |a|^p_exp from Delta^power)."""
    P = sp.Poly(sp.expand(poly_a), a)
    res = 0
    for (n,), c in P.terms():
        if n % 2 == 1:
            continue
        res += c / ((n + p_exp + 1) * (n + p_exp + 2))
    return 2 * res

# Delta = a^2 m^2:  Delta^{-1-eps} = m^{-2-2eps} |a|^{-2-2eps},  Delta^{-eps} = m^{-2eps} |a|^{-2eps}
IT0 = -(sp.gamma(1 + eps) / 2) * m**(-2 - 2 * eps) * fp_integral(r0, -2 - 2 * eps)
IT2 = (D / 2) * (sp.gamma(eps) / 2) * r2 * m**(-2 * eps) * fp_integral(sp.S(1), -2 * eps)
dV_exact = sp.exp(eps * gE) * mu**(2 * eps) * (IT0 + IT2)
L = sp.symbols('L')
dV_ser = sp.series(sp.simplify(dV_exact.subs(mu, m * sp.exp(L / 2))), eps, 0, 1).removeO()
dV_ser = sp.expand(sp.simplify(dV_ser))
print('   delta_V/(alpha_s C_F/4pi) =', dV_ser)
ck('vertex: delta_V = a (3/eps - 4 + 3 ln(mu^2/m^2)) + O(eps)  (VF-NRQ-4)', sp.simplify(dV_ser - (3 / eps - 4 + 3 * L)) == 0)
# separate UV and IR pieces: UV pole from the l^2 (T2) term, IR from the a-integral of the T0 term
uv = sp.series(sp.simplify((sp.exp(eps * gE) * mu**(2 * eps) * IT2).subs(mu, m)), eps, 0, 1).removeO()
ir = sp.series(sp.simplify((sp.exp(eps * gE) * mu**(2 * eps) * IT0).subs(mu, m)), eps, 0, 1).removeO()
print('   T2 (UV) part at mu = m:', sp.expand(uv), ' ;  T0 (Coulomb/IR) part at mu = m:', sp.expand(ir))
ck('pole bookkeeping: l^2 term gives 1/eps (UV), Coulomb-pinch term gives 2/eps (IR); total 3/eps',
   sp.simplify(sp.residue(uv, eps, 0) - 1) == 0 and sp.simplify(sp.residue(ir, eps, 0) - 2) == 0)

# ---------------------------------------------------------------- on-shell Z_2
p2 = sp.symbols('p2', positive=True)
x = sp.symbols('x', positive=True)
DeltaS = x**2 * p2 + x * (m**2 - p2)
# Sigma = (alpha_s C_F/4pi) e^{eps gE} mu^{2eps} Gamma(eps) int dx [-(D-2)(1-x) pslash + D m] Delta^{-eps}
pre = sp.exp(eps * gE) * mu**(2 * eps) * sp.gamma(eps)
Aint = lambda P2: sp.integrate(sp.expand(-(D - 2) * (1 - x) * (x**2 * P2 + x * (m**2 - P2))**(-eps)), (x, 0, 1))
# derivatives at p2 = m^2 : d/dp2 Delta^{-eps} = -eps Delta^{-eps-1} (x^2 - x)
def at_shell_integral(f_of_x):
    # integrate a sum of terms c * x^n (1-x)^k * (x^2 m^2)^{power} over x in (0,1) via Beta functions
    X_ = sp.Symbol('X', positive=True)
    e_ = sp.expand(sp.powsimp(sp.expand_power_base(f_of_x.subs(x, X_), force=True), force=True))
    res = 0
    for term in sp.Add.make_args(sp.expand(e_)):
        c, px, p1x = sp.S(1), sp.S(0), sp.S(0)
        for fac in sp.Mul.make_args(term):
            if fac.has(X_):
                b, e2 = fac.as_base_exp()
                if b == X_:
                    px += e2
                elif b == 1 - X_:
                    p1x += e2
                else:
                    raise ValueError(fac)
            else:
                c *= fac
        res += c * sp.gamma(px + 1) * sp.gamma(p1x + 1) / sp.gamma(px + p1x + 2)
    return res
Del0 = x**2 * m**2
A_on = at_shell_integral(sp.expand(-(D - 2) * (1 - x) * Del0**(-eps)))
B_on = at_shell_integral(sp.expand(D * Del0**(-eps)))
dA = at_shell_integral(sp.expand(-(D - 2) * (1 - x) * (-eps) * Del0**(-eps - 1) * (x**2 - x)))
dB = at_shell_integral(sp.expand(D * (-eps) * Del0**(-eps - 1) * (x**2 - x)))
dZ2_exact = pre * (A_on + 2 * m**2 * (dA + dB))
dZ2_ser = sp.expand(sp.simplify(sp.series(sp.simplify(dZ2_exact.subs(mu, m * sp.exp(L / 2))), eps, 0, 1).removeO()))
print('   delta Z_2/(alpha_s C_F/4pi) =', dZ2_ser)
ck('on-shell delta Z_2 = -a (3/eps + 4 + 3 ln(mu^2/m^2)) + O(eps)  (VF-NRQ-4)', sp.simplify(dZ2_ser - (-(3 / eps + 4 + 3 * L))) == 0)
# mass shift check: delta m = Sigma(pslash = m) = m (A + B) at p2 = m^2  -> a m (3/eps + 4 + 3L) (standard on-shell)
dm = sp.expand(sp.simplify(sp.series(sp.simplify((pre * (A_on + B_on)).subs(mu, m * sp.exp(L / 2))), eps, 0, 1).removeO()))
ck('cross-check: one-loop pole-mass shift delta m/m = a (3/eps + 4 + 3 ln(mu^2/m^2))', sp.simplify(dm - (3 / eps + 4 + 3 * L)) == 0, dm)

# ---------------------------------------------------------------- c_v
cv1 = sp.simplify(dV_ser + dZ2_ser)
ck('c_v - 1 = (alpha_s C_F/4pi)(-8) = -2 C_F alpha_s/pi : finite and mu-independent', sp.simplify(cv1 + 8) == 0, cv1)
# exact-in-eps sum: check finiteness at O(eps^0) also before expansion (pole cancellation)
tot_exact = sp.simplify((dV_exact + dZ2_exact).subs(mu, m))
tot_ser = sp.series(tot_exact, eps, 0, 2).removeO()
print('   exact-in-eps sum (mu = m) expanded:', sp.expand(sp.simplify(tot_ser)))
ck('poles cancel between vertex and Z_2 exactly (1/eps coefficient of the exact sum is 0)', sp.simplify(sp.residue(tot_exact, eps, 0)) == 0)
CF = sp.Rational(4, 3); al = sp.symbols('alpha_s')
cv = 1 + al * CF / (4 * sp.pi) * cv1
ck('|c_v|^2 = 1 - 4 C_F alpha_s/pi = 1 - 16 alpha_s/(3pi) (N_c = 3) to O(alpha_s)', sp.simplify(sp.series(cv**2, al, 0, 2).removeO() - (1 - 16 * al / (3 * sp.pi))) == 0)
for a_num, name in [(0.24, 'charmonium alpha_s(M)~0.24 [BBL II.A]'), (0.18, 'bottomonium alpha_s(M)~0.18 [BBL II.A]')]:
    print('   %s: |c_v|^2 = 1 - 16 as/(3 pi) = %.3f' % (name, 1 - 16 * a_num / (3 * np.pi)))

ok = ck.summary()
sys.exit(0 if ok else 1)
