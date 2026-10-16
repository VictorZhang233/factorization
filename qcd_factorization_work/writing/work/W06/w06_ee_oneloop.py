r"""
w06_ee_oneloop.py -- writer W06: independent re-derivation of every O(alpha_s) ingredient of Ch6 / App C.
(Uses only w06_dtrace.py, written by W06; no code from research/c_ee.)

 A  Born: -g_{mu nu} sum <0|j^mu|q qbar><q qbar|j^nu|0> = 2(D-2) s N_c e_q^2 ; 4D sigma_0, R_0.
 B  D-dim phase space: general two-body formula with one massive leg (z = M^2/s), its massless total,
    the three-body formula from iterating two-body phase spaces, the Dirichlet integral.
 C  one-loop massless quark form factor, exact in eps, computed from scratch (Feynman parameters).
 D  real emission gamma* -> q qbar g: D-dim matrix element (trace engine), exact Dirichlet integration.
 E  real + virtual in one normalization: poles cancel, R = R_0 (1 + 3 C_F a_s/(4 pi)).
 F  KLN illustration: the quark energy spectrum, moments n = 0..3 of the 1/eps coefficient.
Run: python3 -I w06_ee_oneloop.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
import mpmath as mp
from w06_dtrace import trace, contract, dot, D as Dsym
from w06_series import laurent

e = sp.Symbol('eps')
s = sp.Symbol('s', positive=True)
D = 4 - 2 * e
RESULTS = []


def check(name, cond):
    RESULTS.append((name, bool(cond)))
    print(('PASS  ' if cond else 'FAIL  ') + name)


def ser(x, n=2):
    return sp.series(sp.simplify(x), e, 0, n).removeO()


cG = sp.gamma(1 + e) * sp.gamma(1 - e) ** 2 / sp.gamma(1 - 2 * e)

# ======================================================================================== A. Born
print('=== A. Born ===')
# <0|j^mu|q(p1) qbar(p2)> = e_q vbar(p2) gamma^mu u(p1); sum over spins: Tr[p2 g^mu p1 g^nu]
tr = contract(trace([('p', 'p2'), ('i', 'm'), ('p', 'p1'), ('i', 'n')]) * (-1) * sp.Symbol('g_m_n'))
tr = sp.expand(tr.subs(Dsym, D))
# contract -g_{mu nu}: our engine contracts repeated symbolic g_m_n with the open indices
rho0_density = sp.simplify(tr.subs(dot('p1', 'p2'), s / 2))
check('A1  -g_{mu nu} Tr[p2 g^mu p1 g^nu] = 2(D-2) s', sp.simplify(rho0_density - 2 * (D - 2) * s) == 0)
# 4D: e+ e- -> q qbar, spin-summed |M|^2 and sigma_0
t_, u_ = sp.symbols('t u')
lep = contract(trace([('p', 'k2'), ('i', 'm'), ('p', 'k1'), ('i', 'n')]) * trace([('p', 'p1'), ('i', 'm'), ('p', 'p2'), ('i', 'n')]))
lep = sp.expand(lep.subs(Dsym, 4))
kin = {dot('k1', 'k2'): s / 2, dot('p1', 'p2'): s / 2, dot('k1', 'p1'): -t_ / 2, dot('k2', 'p2'): -t_ / 2,
       dot('k1', 'p2'): -u_ / 2, dot('k2', 'p1'): -u_ / 2}
lep = sp.simplify(lep.subs(kin))
check('A2  4D trace product = 8 (t^2 + u^2)', sp.simplify(lep - 8 * (t_ ** 2 + u_ ** 2)) == 0)
# dsigma/dOmega = |M|^2/(64 pi^2 s), |M|^2 = (e^4 e_q^2 N_c/s^2)(1/4) 8 (t^2+u^2), t = -s(1-c)/2, u = -s(1+c)/2
c = sp.Symbol('c'); alpha, Nc, eq = sp.symbols('alpha N_c e_q', positive=True)
M2 = (4 * sp.pi * alpha) ** 2 * eq ** 2 * Nc / s ** 2 * sp.Rational(1, 4) * 8 * ((s * (1 - c) / 2) ** 2 + (s * (1 + c) / 2) ** 2)
sigma0 = sp.integrate(M2 / (64 * sp.pi ** 2 * s) * 2 * sp.pi, (c, -1, 1))
check('A3  sigma_0 = 4 pi alpha^2 N_c e_q^2/(3 s)', sp.simplify(sigma0 - 4 * sp.pi * alpha ** 2 * Nc * eq ** 2 / (3 * s)) == 0)
for nf, R0 in ((3, sp.Rational(2)), (4, sp.Rational(10, 3)), (5, sp.Rational(11, 3))):
    charges = [sp.Rational(2, 3), -sp.Rational(1, 3), -sp.Rational(1, 3), sp.Rational(2, 3), -sp.Rational(1, 3)][:nf]
    check('A4  R_0 = N_c sum e_q^2 = %s for n_f = %d' % (R0, nf), 3 * sum(q ** 2 for q in charges) == R0)

# ======================================================================================== B. phase space
print('=== B. phase space ===')
z, v = sp.symbols('z v', positive=True)
# two-body: dPhi_2 = (2pi)^{2-D} kappa^{D-3}/(4 sqrt s) dOmega_{D-1}, kappa = sqrt(s)(1-z)/2,
# dOmega_{D-1} = Omega_{D-2} 2^{1-2eps} [v(1-v)]^{-eps} dv,  Omega_n = 2 pi^{n/2}/Gamma(n/2)
Omega = lambda n: 2 * sp.pi ** (n / 2) / sp.gamma(n / 2)
kappa = sp.sqrt(s) * (1 - z) / 2
dPhi2_derived = (2 * sp.pi) ** (2 - D) * kappa ** (D - 3) / (4 * sp.sqrt(s)) * Omega(D - 2) * 2 ** (1 - 2 * e) * (v * (1 - v)) ** (-e)
dPhi2_formula = 1 / (8 * sp.pi) * (4 * sp.pi / s) ** e * (1 - z) ** (1 - 2 * e) / sp.gamma(1 - e) * (v * (1 - v)) ** (-e)
ratio = sp.simplify(sp.powsimp(sp.expand_power_base(dPhi2_derived / dPhi2_formula, force=True), force=True))
okB1 = all(abs(complex(ratio.subs({e: ev, s: 3.7, z: 0.31, v: 0.2}).evalf()) - 1) < 1e-12 for ev in (0.1, -0.23, 0.37))
check('B1  dPhi_2 = (1/8pi)(4pi/s)^eps (1-z)^{1-2eps}/Gamma(1-eps) [v(1-v)]^{-eps} dv  (from kappa^{D-3} dOmega_{D-1})', okB1)
# the angular measure integrates to the full solid angle Omega_{D-1}
ang = Omega(D - 2) * 2 ** (1 - 2 * e) * sp.gamma(1 - e) ** 2 / sp.gamma(2 - 2 * e)
okB2 = all(abs(complex((ang / Omega(D - 1)).subs(e, ev).evalf()) - 1) < 1e-12 for ev in (0.1, -0.3, 0.45))
check('B2  Omega_{D-2} 2^{1-2eps} B(1-eps,1-eps) = Omega_{D-1}', okB2)
Phi2 = 1 / (8 * sp.pi) * (4 * sp.pi / s) ** e * sp.gamma(1 - e) / sp.gamma(2 - 2 * e)
check('B3  massless total Phi_2 = (1/8pi)(4pi/s)^eps Gamma(1-eps)/Gamma(2-2eps)',
      sp.simplify(sp.integrate((dPhi2_formula.subs(z, 0)).subs(e, sp.Rational(1, 7)), (v, 0, 1)) - Phi2.subs(e, sp.Rational(1, 7))) == 0
      or abs(complex(sp.Integral(dPhi2_formula.subs({z: 0, e: sp.Rational(1, 7), s: 2}), (v, 0, 1)).evalf()) - complex(Phi2.subs({e: sp.Rational(1, 7), s: 2}).evalf())) < 1e-10)
# three-body by iteration: dPhi_3 = (dM^2/2pi) dPhi_2(P -> p1 + Q23; z = y23, integrated over angles) dPhi_2(Q23 -> p2 p3; z=0, v*)
y12, y13, y23 = sp.symbols('y12 y13 y23', positive=True)
M2s = s * y23
Phi2_P_full = 1 / (8 * sp.pi) * (4 * sp.pi / s) ** e * (1 - y23) ** (1 - 2 * e) / sp.gamma(1 - e) * sp.gamma(1 - e) ** 2 / sp.gamma(2 - 2 * e)
vstar = y12 / (1 - y23)
dPhi2_Q = 1 / (8 * sp.pi) * (4 * sp.pi / M2s) ** e / sp.gamma(1 - e) * (vstar * (1 - vstar)) ** (-e)
# measure: dM^2 = s dy23 ; dv* = dy12/(1-y23)
dPhi3_iter = (s / (2 * sp.pi)) * Phi2_P_full * dPhi2_Q / (1 - y23)
dPhi3_formula = (4 * sp.pi) ** (2 * e - 3) * s ** (1 - 2 * e) / (2 * sp.gamma(2 - 2 * e)) * (y12 * y13 * y23) ** (-e)
rat3 = (dPhi3_iter / dPhi3_formula).subs(y13, 1 - y12 - y23)
okB4 = all(abs(complex(rat3.subs({e: ev, s: 2.9, y12: 0.21, y23: 0.33}).evalf()) - 1) < 1e-12 for ev in (0.11, -0.27, 0.4))
check('B4  dPhi_3 = (4pi)^{2eps-3} s^{1-2eps}/(2 Gamma(2-2eps)) dy13 dy23 (y12 y13 y23)^{-eps}  (iterated two-body)', okB4)
Phi3_tot = dPhi3_formula.subs({y12: 1, y13: 1, y23: 1}) * sp.gamma(1 - e) ** 3 / sp.gamma(3 - 3 * e)
check('B5  4D limit of the total three-body volume = s/(256 pi^3)', sp.simplify(Phi3_tot.subs(e, 0) - s / (256 * sp.pi ** 3)) == 0)
# Dirichlet integral check (numerical) int_{simplex} y12^{a-1} y13^{b-1} y23^{c-1} = G(a)G(b)G(c)/G(a+b+c)
mp.mp.dps = 30
aa, bb, cc = mp.mpf('0.7'), mp.mpf('1.3'), mp.mpf('2.1')
num = mp.quad(lambda x2: mp.quad(lambda x3: (1 - x2 - x3) ** (aa - 1) * x2 ** (bb - 1) * x3 ** (cc - 1), [0, 1 - x2]), [0, 1])
check('B6  Dirichlet integral Gamma(a)Gamma(b)Gamma(c)/Gamma(a+b+c) (numerical)', abs(num - mp.gamma(aa) * mp.gamma(bb) * mp.gamma(cc) / mp.gamma(aa + bb + cc)) < 1e-20)

# ======================================================================================== C. form factor
print('=== C. one-loop form factor from scratch ===')
x, y = sp.symbols('x y', positive=True)
# Lambda^mu = -i g^2 C_F Int d^Dl/(2pi)^D gamma^a (p1-l) gamma^mu (-p2-l) gamma_a / [l^2 (p1-l)^2 (p2+l)^2]
# Feynman parameters x (for (p1-l)^2), y (for (p2+l)^2), 1-x-y (for l^2): l = L + x p1 - y p2,
# denominator L^2 + x y s ;  numerator slashed vectors:
A_vec = {'p1': 1 - x, 'p2': y, 'L': -1}          # p1 - l = (1-x) p1 + y p2 - L
B_vec = {'p1': -x, 'p2': -(1 - y), 'L': -1}     # -p2 - l = -x p1 - (1-y) p2 - L
num_tr = 0
for na, ca in A_vec.items():
    for nb, cb in B_vec.items():
        slots = [('p', 'p1'), ('i', 'a'), ('p', na), ('i', 'm'), ('p', nb), ('i', 'a'), ('p', 'p2'), ('i', 'm')]
        num_tr += ca * cb * trace(slots)
num_tr = contract(num_tr)
num_tr = sp.expand(num_tr.subs(Dsym, D))
Lsq = sp.Symbol('Lsq')
# L-integration rules: odd powers -> 0 ; L.a L.b -> Lsq a.b/D ; L.L -> Lsq
num_tr = num_tr.subs(dot('L', 'L'), Lsq)
poly = sp.Poly(num_tr, dot('L', 'p1'), dot('L', 'p2'))
num_int = 0
for (i1, i2), cf in poly.terms():
    if i1 + i2 == 0:
        num_int += cf
    elif i1 + i2 == 2:
        pa = ['p1'] * i1 + ['p2'] * i2
        num_int += cf * Lsq * dot(pa[0], pa[1]) / D
num_int = sp.expand(num_int.subs({dot('p1', 'p1'): 0, dot('p2', 'p2'): 0, dot('p1', 'p2'): s / 2}))
c2 = num_int.coeff(Lsq, 1)
c0 = sp.expand(num_int - c2 * Lsq)
# Minkowski integrals: Int d^DL/(2pi)^D 1/(L^2-Del)^3 = -i/(4pi)^{D/2} Gamma(1+eps)/2 Del^{-1-eps}
#                      Int d^DL/(2pi)^D L^2/(L^2-Del)^3 = i/(4pi)^{D/2} (D/2) Gamma(eps)/2 Del^{-eps}, Del = -x y s
Q2 = sp.Symbol('Q2', positive=True)      # Euclidean point s -> -Q2 : Del = x y Q2 > 0
c0E, c2E = c0.subs(s, -Q2), c2.subs(s, -Q2)
Del = x * y * Q2
I3 = -sp.I / (4 * sp.pi) ** (D / 2) * sp.gamma(1 + e) / 2 * Del ** (-1 - e)
I3L = sp.I / (4 * sp.pi) ** (D / 2) * (D / 2) * sp.gamma(e) / 2 * Del ** (-e)
# Feynman-parameter factor 2 (= Gamma(3)) and the simplex integral over (x, y)


def simplex(expr):
    """int_0^1 dx int_0^{1-x} dy of a sum of monomials x^a y^b (a, b symbolic) = Gamma(a+1)Gamma(b+1)/Gamma(a+b+3)"""
    expr = sp.expand(sp.expand_power_base(sp.expand(expr), force=True), power_base=True, force=True)
    out = 0
    for term in (expr.args if isinstance(expr, sp.Add) else [expr]):
        pa, pb = 0, 0
        rest = 1
        for f in (term.args if isinstance(term, sp.Mul) else [term]):
            b_, ex_ = f.as_base_exp()
            if b_ == x:
                pa += ex_
            elif b_ == y:
                pb += ex_
            else:
                rest *= f
        out += rest * sp.gamma(pa + 1) * sp.gamma(pb + 1) / sp.gamma(pa + pb + 3)
    return out


g2, CF = sp.symbols('g2 C_F', positive=True)


def simplex_monomial(poly_expr, power):
    """int_simplex dx dy  poly(x,y) * (x y)^power  via Dirichlet: x^i y^j (xy)^p -> G(i+p+1)G(j+p+1)/G(i+j+2p+3)"""
    P = sp.Poly(sp.together(sp.expand(poly_expr)).as_numer_denom()[0], x, y)
    den = sp.together(sp.expand(poly_expr)).as_numer_denom()[1]
    assert not den.has(x) and not den.has(y)
    out = 0
    for (i, j), cf in P.terms():
        out += cf * sp.gamma(i + power + 1) * sp.gamma(j + power + 1) / sp.gamma(i + j + 2 * power + 3)
    return out / den


pref3 = -sp.I / (4 * sp.pi) ** (D / 2) * sp.gamma(1 + e) / 2 * Q2 ** (-1 - e)
pref3L = sp.I / (4 * sp.pi) ** (D / 2) * (D / 2) * sp.gamma(e) / 2 * Q2 ** (-e)
LamTr = -sp.I * g2 * CF * 2 * (pref3 * simplex_monomial(c0E, -1 - e) + pref3L * simplex_monomial(c2E, -e))
denomTr = sp.expand(contract(trace([('p', 'p1'), ('i', 'm'), ('p', 'p2'), ('i', 'm')])).subs(Dsym, D).subs(dot('p1', 'p2'), -Q2 / 2))
F1 = LamTr / denomTr
# compare with VF-EE-4 / VF-SUD-1:  F1 = -(alpha_s C_F/4pi)(4pi mu0^2/Q^2)^eps c_Gamma (2-eps+2eps^2)/(eps^2(1-2eps))
mu0 = sp.Symbol('mu0', positive=True)
F1_ref = -(g2 / (4 * sp.pi)) * CF / (4 * sp.pi) * (4 * sp.pi / Q2) ** e * cG * (2 - e + 2 * e ** 2) / (e ** 2 * (1 - 2 * e))
rat = F1 / F1_ref
okC1 = all(abs(sp.N(rat.subs({e: ev, Q2: sp.Rational(19, 10)}), 30) - 1) < 1e-25 for ev in (sp.Rational(1, 10), sp.Rational(-3, 10), sp.Rational(2, 7), sp.Rational(1, 1000)))
print('      F1/F1_ref at eps=0.1:', sp.N(rat.subs({e: sp.Rational(1, 10), Q2: 2}), 25))
check('C1  vertex graph (Feynman parameters) = -(a_s C_F/4pi)(4pi mu0^2/Q^2)^eps c_Gamma (2-eps+2eps^2)/(eps^2(1-2eps)), exact in eps', okC1)
f_eps = -(2 - e + 2 * e ** 2) / (e ** 2 * (1 - 2 * e))
check('C2  bracket expansion: -2/eps^2 - 3/eps - 8 - 16 eps - 32 eps^2', sp.expand(sp.series(f_eps, e, 0, 3).removeO() - (-2 / e ** 2 - 3 / e - 8 - 16 * e - 32 * e ** 2)) == 0)
# MS-bar normalisation: (4pi mu0^2)^eps -> mu^2 e^{gamma_E}: factor e^{eps gamma} c_Gamma
L = sp.Symbol('L')
msf = sp.exp(e * sp.EulerGamma) * cG * sp.exp(-e * L) * f_eps
msser = laurent(msf, e, 1)
target = -2 / e ** 2 + (2 * L - 3) / e - L ** 2 + 3 * L - 8 + sp.pi ** 2 / 6
diffC3 = sp.expand(msser - target)
check('C3  MS-bar form: -2/eps^2 + (2L-3)/eps - L^2 + 3L - 8 + zeta_2 + O(eps)', all(sp.simplify(diffC3.coeff(e, k)) == 0 for k in (-2, -1, 0)))
o1 = sp.simplify(sp.expand(msser).coeff(e, 1).subs(L, 0))
check('C4  O(eps) coefficient at L=0: -16 + 3 zeta_2/2 + 14 zeta_3/3', sp.simplify(o1 - (-16 + sp.Rational(3, 2) * sp.pi ** 2 / 6 + sp.Rational(14, 3) * sp.zeta(3))) == 0)
# timelike continuation: (Q^2)^{-eps} -> (-s - i0)^{-eps} = s^{-eps} e^{i pi eps};  2 Re F1 = ... cos(pi eps)
vir = 2 * sp.cos(sp.pi * e) * cG * f_eps     # units (a_s C_F/4pi)(4pi mu0^2/s)^eps  -> per (a_s C_F/2pi): cos * cG * f
virN = laurent(sp.cos(sp.pi * e) * f_eps, e, 0)
check('C5  2 Re F1 = (a_s C_F/2pi)(4pi mu0^2/s)^eps c_Gamma cos(pi eps) f(eps) = N_eps[-2/eps^2 - 3/eps - 8 + pi^2 + O(eps)]',
      sp.simplify(virN - (-2 / e ** 2 - 3 / e - 8 + sp.pi ** 2)) == 0)
ell = sp.Symbol('ell', real=True)
msT = laurent(sp.exp(e * sp.EulerGamma) * cG * f_eps * sp.exp(-e * (ell - sp.I * sp.pi)), e, 0)
msTc = msT.subs(sp.I, -sp.I)                       # complex conjugate (all other symbols real)
reF = sp.expand((msT + msTc) / 2)
imF = sp.expand((msT - msTc) / (2 * sp.I))
check('C6  Im F1 = (a_s C_F/4pi)[-2pi/eps + 2pi ell - 3pi]', sp.simplify(imF - (-2 * sp.pi / e + 2 * sp.pi * ell - 3 * sp.pi)) == 0)
check('C7  2 Re F1 per (a_s C_F/2pi): -2/eps^2 + (2ell-3)/eps - ell^2 + 3ell - 8 + zeta_2 + pi^2',
      sp.simplify(reF - (-2 / e ** 2 + (2 * ell - 3) / e - ell ** 2 + 3 * ell - 8 + sp.pi ** 2 / 6 + sp.pi ** 2)) == 0)

# ======================================================================================== D. real emission
print('=== D. real emission ===')
# M^{mu,alpha} = -g t^a ubar(p1)[g^a (p1+k) g^mu / s13 - g^mu (p2+k) g^a / s23] v(p2)   (k = p3, the gluon)
s13, s23 = sp.symbols('s13 s23', positive=True)
amp = [(1 / s13, ['al', 'p1+k', 'mu']), (-1 / s23, ['mu', 'p2+k', 'al'])]
cnj = [(1 / s13, ['nu', 'p1+k', 'be']), (-1 / s23, ['be', 'p2+k', 'nu'])]


def slot(n):
    return ('i', n) if n in ('al', 'mu', 'be', 'nu') else ('p', n)


def expand_slots(names):
    """replace 'p1+k' by p1 + k (linear): returns list of (coeff, slots)"""
    out = [(1, [])]
    for n in names:
        if n == 'p1+k':
            out = [(c_, sl + [('p', 'p1')]) for c_, sl in out] + [(c_, sl + [('p', 'k')]) for c_, sl in out]
        elif n == 'p2+k':
            out = [(c_, sl + [('p', 'p2')]) for c_, sl in out] + [(c_, sl + [('p', 'k')]) for c_, sl in out]
        else:
            out = [(c_, sl + [slot(n)]) for c_, sl in out]
    return out


T = 0
for ca, na in amp:
    for cb, nb in cnj:
        for c1, sl1 in expand_slots(na):
            for c2_, sl2 in expand_slots(nb):
                T += ca * cb * c1 * c2_ * trace([('p', 'p1')] + sl1 + [('p', 'p2')] + sl2)
# contract with (-g_{mu nu}) (-g_{al be}): multiply by g_mu_nu g_al_be (signs: (-1)(-1) = +1)
T = contract(sp.expand(T * sp.Symbol('g_mu_nu') * sp.Symbol('g_al_be')))
T = sp.expand(T.subs(Dsym, D))
kinR = {dot('p1', 'p1'): 0, dot('p2', 'p2'): 0, dot('k', 'k'): 0,
        dot('p1', 'p2'): s * y12 / 2, dot('k', 'p1'): s * y13 / 2, dot('k', 'p2'): s * y23 / 2}
T = sp.simplify(T.subs(kinR).subs({s13: s * y13, s23: s * y23}))
# times g^2 Tr(t^a t^a) = g^2 C_F N_c and e_q^2
ME_ref = 8 * (1 - e) * ((1 - e) * (y13 / y23 + y23 / y13) + 2 * y12 / (y13 * y23) - 2 * e)
check('D1  -g_{mu nu}(-g_{al be}) sum M M* / (g^2 C_F N_c e_q^2) = 8(1-eps)[(1-eps)(y13/y23+y23/y13) + 2y12/(y13y23) - 2eps]',
      sp.simplify((T - ME_ref).subs(y12, 1 - y13 - y23)) == 0)
# 4D limit vs (x1^2+x2^2)/((1-x1)(1-x2)), x1 = 1-y23, x2 = 1-y13
x1, x2 = sp.symbols('x1 x2')
check('D2  4D: proportional to (x1^2+x2^2)/((1-x1)(1-x2))',
      sp.simplify((ME_ref.subs(e, 0) / 8).subs({y12: x1 + x2 - 1, y13: 1 - x2, y23: 1 - x1}) - (x1 ** 2 + x2 ** 2) / ((1 - x1) * (1 - x2))) == 0)
# Dirichlet integration of ME * (y12 y13 y23)^{-eps}
Dir = lambda a, b, cc_: sp.gamma(a) * sp.gamma(b) * sp.gamma(cc_) / sp.gamma(a + b + cc_)
Sum = (1 - e) * 2 * Dir(1 - e, 2 - e, -e) + 2 * Dir(2 - e, -e, -e) - 2 * e * Dir(1 - e, 1 - e, 1 - e)
# rho_R/rho_0 = [s/(2(4pi)^3)(4pi/s)^{2eps}/Gamma(2-2eps)] 8(1-eps) g^2 C_F Sum / [4(1-eps) s Phi_2]
pref = (s / (2 * (4 * sp.pi) ** 3) * (4 * sp.pi / s) ** (2 * e) / sp.gamma(2 - 2 * e)) * 8 * (1 - e) * g2 * CF / (2 * (D - 2) * s * Phi2)
realR = pref * Sum
real_ref = (g2 / (4 * sp.pi)) * CF / (2 * sp.pi) * (4 * sp.pi / s) ** e * 2 * (1 - 2 * e) * (2 - 2 * e + e ** 2) * sp.gamma(1 - e) ** 2 / (e ** 2 * (1 - 3 * e) * (2 - 3 * e) * sp.gamma(1 - 3 * e))
rr = realR / real_ref
okD3 = all(abs(sp.N(rr.subs({e: ev, s: sp.Rational(13, 10)}), 30) - 1) < 1e-25 for ev in (sp.Rational(1, 10), sp.Rational(-2, 9), sp.Rational(3, 11), sp.Rational(1, 1000)))
print('      gammasimp(real/ref) =', sp.simplify(sp.gammasimp(rr)))
check('D3  rho_R/rho_0 = (a_s C_F/2pi)(4pi mu0^2/s)^eps 2(1-2eps)(2-2eps+eps^2)Gamma(1-eps)^2/(eps^2(1-3eps)(2-3eps)Gamma(1-3eps)), exact', okD3)
Kr = sp.gamma(1 - e) ** 2 / sp.gamma(1 - 3 * e)
check('D4  Gamma(1-eps)^2/Gamma(1-3eps) = c_Gamma (1 - pi^2 eps^2/2 + O(eps^3))',
      sp.simplify(laurent(Kr / cG, e, 2) - (1 - sp.pi ** 2 * e ** 2 / 2)) == 0)
realN = laurent(2 * (1 - 2 * e) * (2 - 2 * e + e ** 2) / (e ** 2 * (1 - 3 * e) * (2 - 3 * e)) * Kr / cG, e, 0)
check('D5  real in N_eps normalisation: 2/eps^2 + 3/eps + 19/2 - pi^2 + O(eps)', sp.simplify(realN - (2 / e ** 2 + 3 / e + sp.Rational(19, 2) - sp.pi ** 2)) == 0)
realK = laurent(2 * (1 - 2 * e) * (2 - 2 * e + e ** 2) / (e ** 2 * (1 - 3 * e) * (2 - 3 * e)), e, 0)
check('D6  same real in the Gamma(1-eps)^2/Gamma(1-3eps) normalisation: 2/eps^2 + 3/eps + 19/2 (no pi^2)', sp.simplify(realK - (2 / e ** 2 + 3 / e + sp.Rational(19, 2))) == 0)

# ======================================================================================== E. real + virtual
print('=== E. real + virtual ===')
tot = cG * sp.cos(sp.pi * e) * f_eps + 2 * (1 - 2 * e) * (2 - 2 * e + e ** 2) * Kr / (e ** 2 * (1 - 3 * e) * (2 - 3 * e))
totser = laurent(tot, e, 1)
check('E1  1/eps^2 and 1/eps cancel exactly in rho_V + rho_R', totser.coeff(e, -2) == 0 and sp.simplify(totser.coeff(e, -1)) == 0)
check('E2  finite part 3/2  =>  R = R_0 (1 + (3 C_F/4) a_s/pi)', sp.simplify(totser.coeff(e, 0) - sp.Rational(3, 2)) == 0)
o1 = sp.simplify(totser.coeff(e, 1))
print('      O(eps) term of the sum per (a_s C_F/2pi)(4 pi mu0^2/s)^eps:', o1)
mp.mp.dps = 40
f_num = sp.lambdify(e, tot, 'mpmath')
check('E3  numerical: exact sum at eps = 1e-8 equals 3/2 to 1e-6', abs(f_num(mp.mpf('1e-8')) - mp.mpf(1.5)) < 1e-6)

# ======================================================================================== F. quark energy spectrum
print('=== F. quark energy spectrum (KLN illustration) ===')
X = sp.Symbol('X', positive=True)
B = lambda a, b: sp.gamma(a) * sp.gamma(b) / sp.gamma(a + b)
dens = X ** (1 - 2 * e) * (1 - X) ** (-e) * ((1 - e) * (X / (1 - X) * B(2 - e, 1 - e) + (1 - X) / X * B(-e, 1 - e))
                                         + 2 / (1 - X) * B(-e, 2 - e) - 2 * e * B(1 - e, 1 - e))
# per (a_s C_F/2pi)(4pi mu0^2/s)^eps: (1/sigma0) dsigma_R/dX = dens/Gamma(1-eps) ; virtual = c_G cos f delta(1-X)


def moment(n):
    # int_0^1 X^n dens dX term by term (Beta functions)
    m = ((1 - e) * (B(n + 3 - 2 * e, -e) * B(2 - e, 1 - e) + B(n + 1 - 2 * e, 2 - e) * B(-e, 1 - e))
         + 2 * B(n + 2 - 2 * e, -e) * B(-e, 2 - e) - 2 * e * B(n + 2 - 2 * e, 1 - e) * B(1 - e, 1 - e))
    return m / sp.gamma(1 - e) + cG * sp.cos(sp.pi * e) * f_eps


expect = {0: 0, 1: sp.Rational(4, 3), 2: sp.Rational(25, 12), 3: sp.Rational(157, 60)}
okF = True
for n in range(4):
    mser = laurent(moment(n), e, 0)
    c2_, c1_ = sp.simplify(mser.coeff(e, -2)), sp.simplify(mser.coeff(e, -1))
    Pn = sp.integrate((X ** n - 1) * (1 + X ** 2) / (1 - X), (X, 0, 1))
    good = (c2_ == 0) and sp.simplify(c1_ - expect[n]) == 0 and sp.simplify(c1_ + Pn) == 0
    okF &= good
    print('      n=%d: 1/eps^2 coeff %s, 1/eps coeff %s  (= -int x^n [(1+x^2)/(1-x)]_+ = %s)' % (n, c2_, c1_, -Pn))
check('F1  moments n=0..3: 1/eps^2 cancels, 1/eps = -int x^n [(1+x^2)/(1-x)]_+ = 0, 4/3, 25/12, 157/60 (x C_F, units a_s/2pi)', okF)
# pointwise collinear pole at X<1: residue of dens/Gamma(1-eps) at eps=0 equals -(1+X^2)/(1-X) * (1/eps)
res = sp.simplify(sp.limit(e * sp.gammasimp(dens / sp.gamma(1 - e)), e, 0))
check('F2  x<1 pointwise pole: (1/sigma0) dsigma/dx -> -(1/eps)(a_s C_F/2pi)(1+x^2)/(1-x)', sp.simplify(res + (1 + X ** 2) / (1 - X)) == 0)

print()
print('SUMMARY: %d/%d checks passed' % (sum(p for _, p in RESULTS), len(RESULTS)))
