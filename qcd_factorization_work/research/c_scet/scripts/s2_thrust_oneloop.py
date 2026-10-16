# -*- coding: utf-8 -*-
"""
s2_thrust_oneloop.py -- Part (2a): one-loop ingredients of the thrust factorization theorem,
computed from scratch, exactly in eps:

  (i)   massless quark vector form factor (Feynman gauge, Feynman parameters, D-dim traces)
        -> SCET matching coefficient C_V, hard function H = |C_V|^2 (timelike)
  (ii)  quark jet function J(p^2) from the real-emission cut of <0|chi_n chi_n-bar|0>
  (iii) thrust (hemisphere-sum) soft function S_T(k) from the eikonal cut
  (iv)  MSbar renormalization, star-distribution form, Laplace transforms, anomalous dimensions

Conventions: D = 4 - 2 eps; g^2 = 4 pi alpha_s mu^{2eps} e^{eps gamma_E} (4 pi)^{-eps} (MSbar);
a = C_F alpha_s/(4 pi).  Star distributions on [0, mu^2] (jet) / [0, mu] (soft):
  int_0^{mu^2} ds [ln^n(s/mu^2)/s]_* f(s) = int_0^{mu^2} ds ln^n(s/mu^2)/s (f(s)-f(0)) .

Run:  python3 -I s2_thrust_oneloop.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

ck = Check('s2_thrust_oneloop: form factor -> H ; jet function J ; soft function S (one loop, exact in eps)')
eps = sp.Symbol('epsilon')
gE = sp.EulerGamma
z2 = sp.zeta(2)
CF = sp.Symbol('C_F', positive=True)
als = sp.Symbol('alpha_s', positive=True)
mu, Q = sp.symbols('mu Q', positive=True)
x, y = sp.symbols('x y', positive=True)
Dsub = {D: 4 - 2 * eps}

def same(e1, e2, pts=(sp.Rational(-3, 10), sp.Rational(-7, 50), sp.Rational(11, 100), sp.Rational(23, 100))):
    """exact-in-eps equality tested at several rational eps values with 30 digits (plus symbolic try)"""
    try:
        if sp.simplify(sp.expand_func(sp.gammasimp(e1 - e2))) == 0:
            return True
    except Exception:
        pass
    for p_ in pts:
        v = complex(sp.N((e1 - e2).subs(eps, p_), 30))
        sc = max(1.0, abs(complex(sp.N(e2.subs(eps, p_), 30))))
        if abs(v) > 1e-20 * sc:
            return False
    return True

def ev(e):
    """evaluate polygamma/zeta at rational arguments and simplify"""
    return sp.nsimplify(sp.simplify(sp.expand_func(e)), [sp.pi ** 2, sp.zeta(3)]) if False else sp.simplify(sp.expand_func(e))

# =====================================================================================================
# (i) massless form factor:  dGamma^mu = -i g^2 C_F int d^Dk/(2pi)^D gamma^a (p2-k) gamma^mu (p1-k) gamma_a
#                                         / [k^2 (k-p2)^2 (k-p1)^2]
#     F1 = Tr[p2 dGamma^mu p1 gamma_mu] / Tr[p2 gamma^mu p1 gamma_mu]
# Feynman parameters: x (k-p2)^2 + y (k-p1)^2 + (1-x-y) k^2 = l^2 - Delta, k = l + x p2 + y p1,
#                     Delta = 2 x y p1.p2 = x y Q^2   (spacelike q = p2 - p1, Q^2 = -q^2 = 2 p1.p2)
P12 = sp.Symbol('P12', positive=True)    # p1.p2 = Q^2/2
dotsub = {dot('p1', 'p1'): 0, dot('p2', 'p2'): 0, dot('p1', 'p2'): P12}
# numerator with k = l + x p2 + y p1 : expand gamma strings linearly in vectors {l, p1, p2}
def kvec_terms(sign_p2, sign_p1):
    """(p2-k) or (p1-k) expressed as list of (coef, vector) with k = l + x p2 + y p1"""
    pass

# (p2 - k) = -l + (1-x) p2 - y p1 ;  (p1 - k) = -l - x p2 + (1-y) p1
A_terms = [(-1, 'l'), (1 - x, 'p2'), (-y, 'p1')]
B_terms = [(-1, 'l'), (-x, 'p2'), (1 - y, 'p1')]
num = sp.Integer(0)
for ca, va in A_terms:
    for cb, vb in B_terms:
        tr = dtrace(('p2', 'a', va, 'mu', vb, 'a', 'p1', 'mu'), indices=('a', 'mu'))
        num += ca * cb * tr
num = sp.expand(num)
# symmetric integration: odd powers of l vanish; l.v l.w -> l^2 v.w / D ; l.l -> l^2
L2 = sp.Symbol('L2')   # l^2
def sym_int(expr):
    expr = sp.expand(expr)
    out = sp.Integer(0)
    for t in sp.Add.make_args(expr):
        ls = [s for s in t.free_symbols if s.name.startswith('l.') or s.name == 'l^2']
        pw = 0
        facs = sp.Mul.make_args(t)
        lfac = sp.Integer(1); rest = sp.Integer(1); ldots = []
        for f_ in facs:
            base, e = f_.as_base_exp()
            if isinstance(base, sp.Symbol) and (base.name.startswith('l.') or base.name == 'l^2'):
                ldots += [base] * int(e)
            else:
                rest *= f_
        nl = sum(2 if b.name == 'l^2' else 1 for b in ldots)
        if nl == 0:
            out += rest
        elif nl == 2:
            if len(ldots) == 1:      # l^2
                out += rest * L2
            else:                     # l.v l.w
                v = [b.name.split('.')[1] if b.name.split('.')[0] == 'l' else b.name.split('.')[0] for b in ldots]
                out += rest * L2 * dot(v[0], v[1]) / D
        elif nl % 2 == 1:
            continue
        else:
            raise ValueError('l^4 terms not expected')
    return sp.expand(out)
num_s = sym_int(num).subs(dotsub)
den = dtrace(('p2', 'mu', 'p1', 'mu'), indices=('mu',)).subs(dotsub)      # (2-D) 4 p1.p2
N0 = sp.expand(num_s.coeff(L2, 0))
N2 = sp.expand(num_s.coeff(L2, 1))
# Minkowski integrals (D = 4 - 2 eps), (4 pi)^{-D/2} factored as (4pi)^{-2+eps}:
#  int d^Dl/(2pi)^D 1/(l^2-Delta)^3     = -i/(4pi)^{D/2} Gamma(1+eps)/2 Delta^{-1-eps}
#  int d^Dl/(2pi)^D l^2/(l^2-Delta)^3   = +i/(4pi)^{D/2} (D/2) Gamma(eps)/2 Delta^{-eps}
# Minkowski integrals (D = 4 - 2 eps):
#  int d^Dl/(2pi)^D 1/(l^2-Delta)^3     = -i/(4pi)^{D/2} Gamma(1+eps)/2 Delta^{-1-eps}
#  int d^Dl/(2pi)^D l^2/(l^2-Delta)^3   = +i/(4pi)^{D/2} (D/2) Gamma(eps)/2 Delta^{-eps}
# with Delta = x y (2 P12).  F1 (4pi)^{D/2}/(g^2 C_F mu^{2eps}) = -i * 2 * int_simplex [N0 I3_0 + N2 I3_2]/den
def simplex_monomials(poly_expr, shift):
    """int_simplex poly(x,y) * (x y)^shift dx dy, poly given as sympy expression polynomial in x,y"""
    P = sp.Poly(sp.expand(poly_expr), x, y)
    tot = sp.Integer(0)
    for (i_, j_), c in P.terms():
        a_, b_ = i_ + shift, j_ + shift
        tot += c * sp.gamma(a_ + 1) * sp.gamma(b_ + 1) / sp.gamma(a_ + b_ + 3)
    return tot
denD = sp.expand(den.subs(Dsub))
part0 = (-sp.I) * 2 * (-sp.I) * sp.gamma(1 + eps) / 2 * (2 * P12) ** (-1 - eps) * simplex_monomials(N0.subs(Dsub), -1 - eps) / denD
part2 = (-sp.I) * 2 * (sp.I) * ((4 - 2 * eps) / 2) * sp.gamma(eps) / 2 * (2 * P12) ** (-eps) * simplex_monomials(N2.subs(Dsub), -eps) / denD
F1_red = part0 + part2
R = sp.simplify(F1_red * (2 * P12) ** eps)
R = sp.simplify(sp.gammasimp(R))
cG = sp.gamma(1 + eps) * sp.gamma(1 - eps) ** 2 / sp.gamma(1 - 2 * eps)
R_over_cG = sp.simplify(sp.gammasimp(R / cG))
print('   exact form factor: F1 = (alpha_s C_F/4pi) (4 pi mu^2/Q^2)^eps c_Gamma * [', sp.factor(R_over_cG), ']')
ref_exact = -(2 / eps ** 2 + 3 / eps + 8) + 0  # leading terms only; exact form tested below
exact_guess = -(2 / eps ** 2 + 3 / eps + 8) / 1  # check whether a closed form exists:
closed = -(2 - eps + 2 * eps ** 2) / (eps ** 2 * (1 - 2 * eps))   # candidate closed form
ck('closed form: c_Gamma^-1 R = -(2 - eps + 2 eps^2)/(eps^2 (1 - 2 eps))  [exact in eps]',
   same(R_over_cG, closed), str(sp.factor(R_over_cG)))
R_over_cG = closed     # use the verified closed form below
ser = sp.expand(sp.series(closed, eps, 0, 2).removeO())
ck('F_1^(1) = (a_s C_F/4pi)(4pi mu^2/Q^2)^eps c_Gamma [-2/eps^2 - 3/eps - 8 - 16 eps + O(eps^2)]',
   sp.simplify(ser - (-2 / eps ** 2 - 3 / eps - 8 - 16 * eps)) == 0, f'series: {ser}')

# MSbar: alpha_s bare -> alpha_s mu^{2eps} e^{eps gE}(4pi)^{-eps}: F1 = a (mu^2/Q^2)^eps e^{eps gE} c_Gamma R/cG
Lh = sp.Symbol('L')       # L = ln(Q^2/mu^2) for spacelike q^2 = -Q^2  (general: ln(-q^2-i0)/mu^2)
F1_ms = sp.exp(-eps * Lh) * sp.exp(eps * gE) * cG * R_over_cG
F1_ser = sp.expand(sp.series(F1_ms, eps, 0, 1).removeO())
poles = sp.expand(F1_ser.coeff(eps, -2) / eps ** 2 + F1_ser.coeff(eps, -1) / eps)
fin = sp.simplify(sp.expand_func(F1_ser.coeff(eps, 0)))
Fq = sp.expand(sp.series(sp.exp(eps * gE) * cG * closed, eps, 0, 2).removeO())
ck('MSbar Laurent series at mu^2 = Q^2: -2/eps^2 - 3/eps - 8 + zeta2 + eps(-16 + 3zeta2/2 + 14zeta3/3)  [agrees with c_dis]',
   sp.simplify(sp.expand_func(Fq) - (-2 / eps ** 2 - 3 / eps - 8 + z2 + eps * (-16 + sp.Rational(3, 2) * z2 + sp.Rational(14, 3) * sp.zeta(3)))) == 0,
   str(sp.expand_func(Fq)))
ck('IR poles of F (= UV poles of SCET current): -2/eps^2 + (2L - 3)/eps', sp.simplify(poles - (-2 / eps ** 2 + (2 * Lh - 3) / eps)) == 0, str(poles))
CV1 = sp.expand(fin)
ck('C_V(-q^2,mu) = 1 + a[-L^2 + 3L - 8 + zeta_2],  L = ln(-q^2/mu^2)', sp.simplify(CV1 - (-Lh ** 2 + 3 * Lh - 8 + z2)) == 0, str(CV1))
# anomalous dimension of C_V : dC/dln mu = [Gamma_cusp L + gamma^V] C,  dL/dln mu = -2
dCV = sp.expand(sp.diff(CV1, Lh) * (-2))
ck('dC_V/dln mu = a[4 L - 6]  => Gamma_0 = 4 C_F, gamma^V_0 = -6 C_F', sp.simplify(dCV - (4 * Lh - 6)) == 0)
# hard function (timelike q^2 = Q^2 > 0):  L -> ln(Q^2/mu^2) - i pi ,  H = |C_V|^2
LQ = sp.Symbol('L_Q', real=True)
CV_t = CV1.subs(Lh, LQ - sp.I * sp.pi)
H1 = sp.expand(sp.simplify(2 * sp.re(sp.expand(CV_t))))
ck('H(Q^2,mu) = 1 + a[-2 L_Q^2 + 6 L_Q - 16 + 7 pi^2/3],  L_Q = ln(Q^2/mu^2)  [Becher-Schwartz 2008]',
   sp.simplify(H1 - (-2 * LQ ** 2 + 6 * LQ - 16 + 7 * sp.pi ** 2 / 3)) == 0, str(H1))

# =====================================================================================================
# (ii) jet function: J(s) from  sum_X (2pi)^D delta(p - p_X) <0|chi_n|X><X|chibar_n|0> = 2 pi (nslash/2) nbar.p J(s)
#  one-loop real emission q(k1) g(k2):  <X|chibar_n|0> = g t^a ubar(k1)[ -gamma^nu pslash/s + nbar^nu/nbar.k2 ] P_nbar eps*_nu
#  J^(1)(s) = 1/(4 pi nbar.p N_c) * (-g^2 C_F N_c) * int dPhi_2  T ,
#  T = tr[ (nbarslash/2)(-pslash gamma_nu/s + nbar_nu/nbar.k2) k1slash (-gamma^nu pslash/s + nbar^nu/nbar.k2) ]
s_, nbp = sp.symbols('s nbp', positive=True)
xg = sp.Symbol('x', positive=True)      # gluon light-cone fraction nbar.k2/nbar.p
jsub = {dot('k1', 'k1'): 0, dot('k2', 'k2'): 0, dot('k1', 'k2'): s_ / 2, dot('nb', 'nb'): 0,
        dot('k2', 'nb'): xg * nbp, dot('k1', 'nb'): (1 - xg) * nbp}
Tt = sp.Integer(0)
# p = k1 + k2
for pa in ('k1', 'k2'):
    for pb in ('k1', 'k2'):
        Tt += sp.Rational(1, 2) * dtrace(('nb', pa, 'nu', 'k1', 'nu', pb), indices=('nu',)) / s_ ** 2
for pa in ('k1', 'k2'):
    Tt += -sp.Rational(1, 2) * dtrace(('nb', pa, 'nb', 'k1')) / (s_ * xg * nbp)
    Tt += -sp.Rational(1, 2) * dtrace(('nb', 'k1', 'nb', pa)) / (s_ * xg * nbp)
Tt = sp.simplify(sp.expand(Tt.subs(jsub)).subs(Dsub))
ck('jet trace T = -(nbar.p/s)[4(1-eps) x + 8(1-x)/x]', sp.simplify(Tt + (nbp / s_) * (4 * (1 - eps) * xg + 8 * (1 - xg) / xg)) == 0, str(sp.factor(Tt)))
# with the physical polarization sum -g_{nu nu'}:  -T = (4 nbar.p/s) * P_gq(x)/C_F,  P_gq(x)/C_F = (1+(1-x)^2)/x - eps x  (D-dim splitting fn)
ck('projected |M|^2 (pol. sum -g): -T = (4 nbar.p/s)[(1+(1-x)^2)/x - eps x] = (4 nbar.p/s) P_gq(x)/C_F  (D-dim)',
   sp.simplify(-Tt - 4 * nbp / s_ * ((1 + (1 - xg) ** 2) / xg - eps * xg)) == 0)
# 2-body phase space at fixed p (p_perp = 0):  int dPhi_2 = (1/8pi)(4pi/s)^eps/Gamma(1-eps) int_0^1 dx (x(1-x))^{-eps}
# (derived in DERIVATION.md; verified numerically below for eps -> 0 normalization 1/(8pi))
# int_0^1 dx (x xbar)^{-eps} x^k = B(k+1-eps, 1-eps)   (analytic continuation from eps < 0)
poly_x = sp.expand(-Tt * s_ / nbp * xg)          # = x * (4(1-eps)x + 8(1-x)/x) : polynomial in x
Px = sp.Poly(poly_x, xg)
ints = sum(c * sp.gamma(k_[0] - 1 + 1 - eps) * sp.gamma(1 - eps) / sp.gamma(k_[0] - 1 + 2 - 2 * eps) for k_, c in Px.terms())
# J^(1) = (g^2 C_F mu^{2eps}/(4 pi nbar.p)) (1/8pi) (4pi/s)^eps /Gamma(1-eps) * int (x xbar)^-eps (-T)
#       = (alpha_s C_F/(4pi)) (4 pi mu^2)^eps s^{-1-eps} * Jhat(eps),   with g^2 = 4 pi alpha_s (bare)
Jhat = sp.gammasimp(sp.simplify(sp.Rational(1, 2) * ints / sp.gamma(1 - eps)))
Jclosed = -(4 - eps) / eps * sp.gamma(2 - eps) / sp.gamma(2 - 2 * eps)
ck('J^(1)_bare(s) = (a_s C_F/4pi)(4 pi mu^2)^eps s^{-1-eps} * [-(4-eps)/eps * Gamma(2-eps)/Gamma(2-2eps)]  (exact)',
   same(Jhat, Jclosed), str(sp.simplify(Jhat)))

# distribution expansion: mu^{2eps} s^{-1-eps} = -delta(s)/eps + sum_n (-eps)^n/n! [ln^n(s/mu^2)/s]_*
def dist_expand(coef_eps, power_factor, nmax=2):
    """coef_eps(eps) * mu^{p eps} X^{-1-p eps} with p = power_factor; returns dict of Laurent coefficients
       for basis {delta, [1/X]_*, [ln X/X]_*, [ln^2 X/X]_*} through eps^0."""
    p = power_factor
    res = {}
    # mu^{p eps} X^{-1 - p eps} = -delta/(p eps) + sum_n (-p eps)^n/n! [ln^n/X]_*  (ln of X/mu^{...})
    basis = {'delta': -1 / (p * eps)}
    for nn in range(0, nmax + 1):
        basis[f'L{nn}'] = (-p * eps) ** nn / sp.factorial(nn)
    for k_, v in basis.items():
        res[k_] = sp.expand(sp.series(coef_eps * v, eps, 0, 1).removeO())
    return res

Jcoef_ms = sp.exp(eps * gE) * Jclosed                 # MSbar: (4pi)^eps e^{eps gE}... -> e^{eps gE}
Jd = dist_expand(Jcoef_ms, 1)
ck('bare jet: delta(s) coefficient = 4/eps^2 + 3/eps + 7 - pi^2', sp.simplify(Jd['delta'] - (4 / eps ** 2 + 3 / eps + 7 - sp.pi ** 2)) == 0, str(Jd['delta']))
ck('bare jet: [1/s]_* coefficient = -4/eps - 3 ;  [ln(s/mu^2)/s]_* coefficient = 4', sp.simplify(Jd['L0'] - (-4 / eps - 3)) == 0 and sp.simplify(Jd['L1'] - 4) == 0,
   f"{Jd['L0']}, {Jd['L1']}")
fin_d = sp.simplify(Jd['delta'].coeff(eps, 0)); fin0 = sp.simplify(Jd['L0'].coeff(eps, 0)); fin1 = sp.simplify(Jd['L1'].coeff(eps, 0))
ck('renormalized (MSbar) J(s,mu) = delta(s) + a[(7 - pi^2) delta(s) - 3[1/s]_* + 4[ln(s/mu^2)/s]_*]  [Bauer-Manohar 2004; Becher-Neubert 2006]',
   sp.simplify(fin_d - (7 - sp.pi ** 2)) == 0 and fin0 == -3 and fin1 == 4, f'finite parts: {fin_d}, {fin0}, {fin1}')
# Laplace transform: jt(L) = int_0^inf ds exp(-s/(e^gE Q_J^2)) J(s),  L = ln(Q_J^2/mu^2)
LJ = sp.Symbol('L_J')
jt_bare = sp.exp(eps * gE) * Jclosed * sp.gamma(-eps) * sp.exp(-gE * eps) * sp.exp(-eps * LJ)
jt_ser = sp.expand(sp.series(jt_bare, eps, 0, 1).removeO())
jt1 = sp.simplify(jt_ser.coeff(eps, 0))
ck('Laplace jet: jt(L) = 1 + a[2L^2 - 3L + 7 - 2pi^2/3]', sp.simplify(jt1 - (2 * LJ ** 2 - 3 * LJ + 7 - 2 * sp.pi ** 2 / 3)) == 0, str(sp.expand(jt1)))
djt = sp.expand(sp.diff(jt1, LJ) * (-2))
ck('d jt/dln mu = a[-8L + 6] = -2 Gamma_0 L - 2 gamma^J_0  => gamma^J_0 = -3 C_F', sp.simplify(djt - (-8 * LJ + 6)) == 0)
jt_poles = sp.expand(jt_ser.coeff(eps, -2) / eps ** 2 + jt_ser.coeff(eps, -1) / eps)
ck('Laplace jet Z-factor poles: 4/eps^2 + (3 - 4 L)/eps', sp.simplify(jt_poles - (4 / eps ** 2 + (3 - 4 * LJ) / eps)) == 0, str(jt_poles))

# =====================================================================================================
# (iii) thrust soft function, one real gluon (virtual graphs scaleless):
#   |M|^2 = 4 g^2 C_F/(n.k nbar.k) ;  measure int d^Dk delta+(k^2)/(2pi)^{D-1} = (1/2)(pi^{1-eps}/Gamma(1-eps))/(2pi)^{3-2eps}
#            int d(n.k) d(nbar.k) (n.k nbar.k)^{-eps} ;  hemisphere: k in R (nbar.k > n.k) contributes n.k
nk, nbk, ell = sp.symbols('nk nbk ell', positive=True)
pref = 4 * sp.pi * als * CF * 4 * sp.Rational(1, 2) * sp.pi ** (1 - eps) / ((2 * sp.pi) ** (3 - 2 * eps) * sp.gamma(1 - eps))
hemi = sp.integrate(nbk ** (-1 - eps), (nbk, ell, sp.oo), conds='none') * ell ** (-1 - eps)   # nk = ell
S1_bare = sp.simplify(2 * pref * hemi)       # times mu^{2eps} e^{eps gE}(4pi)^{-eps} (MSbar)
S1_red = sp.simplify(S1_bare * sp.exp(eps * gE) * (4 * sp.pi) ** (-eps) / (als * CF / (4 * sp.pi)) * ell ** (1 + 2 * eps))
S1_red = sp.simplify(sp.powsimp(sp.expand_power_base(S1_red, force=True), force=True))
ck('S^(1)_bare(ell) = a * 8 e^{eps gE}/(eps Gamma(1-eps)) mu^{2eps} ell^{-1-2eps}', sp.simplify(S1_red - 8 * sp.exp(eps * gE) / (eps * sp.gamma(1 - eps))) == 0, str(S1_red))
Sd = dist_expand(8 * sp.exp(eps * gE) / (eps * sp.gamma(1 - eps)), 2)
ck('bare soft: delta coefficient = -4/eps^2 + pi^2/3 ; [1/ell]_*: 8/eps ; [ln(ell/mu)/ell]_*: -16',
   sp.simplify(Sd['delta'] - (-4 / eps ** 2 + sp.pi ** 2 / 3)) == 0 and sp.simplify(Sd['L0'] - 8 / eps) == 0 and sp.simplify(Sd['L1'] + 16) == 0,
   f"{Sd['delta']}, {Sd['L0']}, {Sd['L1']}")
LS = sp.Symbol('L_S')
st_bare = 8 * sp.exp(eps * gE) / (eps * sp.gamma(1 - eps)) * sp.gamma(-2 * eps) * sp.exp(-2 * gE * eps) * sp.exp(-2 * eps * LS)
st_ser = sp.expand(sp.series(st_bare, eps, 0, 1).removeO())
st1 = sp.simplify(st_ser.coeff(eps, 0))
ck('Laplace soft: st(L) = 1 + a[-8 L^2 - pi^2],  L = ln(Q_S/mu)', sp.simplify(st1 - (-8 * LS ** 2 - sp.pi ** 2)) == 0, str(sp.expand(st1)))
dst = sp.expand(sp.diff(st1, LS) * (-1))
ck('d st/dln mu = a[16 L] = 4 Gamma_0 L - 2 gamma^S_0  => gamma^S_0 = 0', sp.simplify(dst - 16 * LS) == 0)

# =====================================================================================================
# numerical sanity checks of the D-dim phase-space normalization (eps -> 0) and of the soft integral
import scipy.integrate as si
# 4-dim two-body phase space for massless particles: int dPhi_2 = 1/(8 pi)
# D-dim two-body phase space: light-cone result (1/8pi)(4pi/s)^eps/Gamma(1-eps) int (x xbar)^-eps
#   vs rest-frame evaluation  Omega_{D-1}/(2pi)^{D-2} (sqrt(s)/2)^{D-2}/(2 s)
Dd = 4 - 2 * eps
Omega = 2 * sp.pi ** ((Dd - 1) / 2) / sp.gamma((Dd - 1) / 2)
rest = Omega / (2 * sp.pi) ** (Dd - 2) * (sp.sqrt(s_) / 2) ** (Dd - 2) / (2 * s_)
lc = (4 * sp.pi / s_) ** eps / (8 * sp.pi) / sp.gamma(1 - eps) * sp.gamma(1 - eps) ** 2 / sp.gamma(2 - 2 * eps)
ck('D-dim 2-body phase space: light-cone parametrization = rest-frame formula (exact in eps)',
   same(sp.simplify(rest.subs(s_, sp.Rational(7, 3))), sp.simplify(lc.subs(s_, sp.Rational(7, 3)))),
   'Phi_2 = (1/8pi)(4pi/s)^eps Gamma(1-eps)/Gamma(2-2eps)')

# save results for s2_thrust_rg.py
import json
res = {'H1': str(H1), 'CV1': str(CV1), 'jt1': str(sp.expand(jt1)), 'st1': str(sp.expand(st1)),
       'J_delta': '7 - pi**2', 'J_L0': '-3', 'J_L1': '4', 'S_delta': 'pi**2/3', 'S_L1': '-16'}
json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs', 's2_oneloop_results.json'), 'w'), indent=1)
ok = ck.summary()
sys.exit(0 if ok else 1)
