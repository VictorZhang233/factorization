"""
ee_nlo.py -- e+e- -> hadrons at LO and O(alpha_s) in conventional dimensional regularisation.

Conventions (CONTEXT.md): metric (+,-,-,-), quark-gluon vertex  i g gamma^mu t^a,  D = 4 - 2 eps,
Tr 1 = 4, Feynman gauge, alpha_s = g^2/(4 pi).  The bare coupling is kept as g (mu = 1); MS-bar
factors are irrelevant at O(alpha_s) because the poles cancel.

Hadronic objects (all for one quark flavour of charge e_q, colour N_c; sum over flavours at the end):
  W^{mu nu}(q) = sum_X (2pi)^D delta^D(q - p_X) <0|j^mu|X><X|j^nu|0>,   j^mu = e_q qbar gamma^mu q
  rho(s)       = -g_{mu nu} W^{mu nu}     (the D-dim "spectral weight"; rho = 2 (D-1) s Im Pi)
  R = 12 pi Im Pi(s+i0)  ==>  R^{(1)}/R_0 = lim_{eps->0} (rho_V + rho_R)/rho_LO .

Parts:
  A. LO:  -g_{mu nu} Tr[p1 g^mu p2 g^nu] = 2(D-2) s;  sigma_0 from the full 2->2 matrix element in 4D;
     D-dim two-body phase space; exact LO cutting identity  rho_LO = 2 (D-1) s Im Pi_LO .
  B. one-loop massless timelike quark form factor F(s+i0), exact in eps.
  C. real emission gamma* -> q qbar g: D-dim matrix element (trace engine) and D-dim three-body
     phase space; exact-in-eps Dirichlet integrals.
  D. sum: cancellation of 1/eps^2 and 1/eps poles;  R = R_0 (1 + 3 C_F alpha_s/(4 pi)).
  E. KLN illustrations: exclusive pieces divergent; the quark-energy spectrum keeps a collinear
     pole  -(1/eps) (alpha_s/2pi) P_qq(x)  (not IR safe), whose integral over x vanishes.
Run:  python3 -I ee_nlo.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
import mpmath as mp
from diracD import D, dot, slash, gam, lc_mul, lc_add, scal, trace

eps = sp.Symbol('eps')
s = sp.Symbol('s', positive=True)
g, CF, Nc = sp.symbols('g C_F N_c', positive=True)
PASS = []


def check(name, cond):
    PASS.append((name, bool(cond)))
    print(('PASS  ' if cond else 'FAIL  ') + name)


def _clean(ex):
    ex = ex.replace(lambda e: isinstance(e, sp.polygamma), lambda e: sp.expand_func(e))
    return sp.expand(sp.nsimplify(sp.expand(ex), [sp.pi, sp.zeta(3), sp.EulerGamma]) if False else sp.expand(ex))


def _pg(m, r):
    """polygamma(m, r) for integer m>=1 and r a positive integer or half-integer, in closed form"""
    m = int(m)
    r = sp.Rational(r)
    if r.q == 1:
        base, z0 = (-1) ** (m + 1) * sp.factorial(m) * sp.zeta(m + 1), sp.Integer(1)
    elif r.q == 2:
        base, z0 = (-1) ** (m + 1) * sp.factorial(m) * (2 ** (m + 1) - 1) * sp.zeta(m + 1), sp.Rational(1, 2)
    else:
        return sp.polygamma(m, r)
    val, z = base, z0
    while z < r:
        val += (-1) ** m * sp.factorial(m) / z ** (m + 1)
        z += 1
    return sp.expand(val)


def laurent(expr, n=2, var=None):
    """Laurent expansion in eps up to and including eps^n (sympy series), polygammas evaluated."""
    var = var or eps
    ex = sp.expand(sp.series(expr, var, 0, n + 1).removeO())
    ex = ex.replace(lambda e: isinstance(e, sp.polygamma) and e.args[1].is_Rational and e.args[0].is_Integer
                    and e.args[0] >= 1, lambda e: _pg(e.args[0], e.args[1]))
    ex = ex.replace(lambda e: isinstance(e, sp.zeta) and e.args[0] in (2, 4, 6), lambda e: sp.expand_func(e))
    return sp.expand(ex)


def coeffs(expr, lo=-2, hi=1):
    ex = laurent(expr, hi)
    return {k: sp.nsimplify(sp.simplify(ex.coeff(eps, k))) for k in range(lo, hi + 1)}


# ==============================================================================================
# A. Leading order
# ==============================================================================================
print('=== A. leading order ===')
Tlo = trace(lc_mul(slash(p1=1), gam('m'), slash(p2=1), gam('m')))       # Tr[p1 g^m p2 g_m]
rho_LO_trace = sp.expand(-Tlo.subs({dot('p1', 'p2'): s / 2}))
check('A1  -g_mn Tr[p1 g^m p2 g^n] = 2(D-2) s', sp.simplify(rho_LO_trace - 2 * (D - 2) * s) == 0)

# full 2->2 matrix element in 4D:  e-(k1) e+(k2) -> q(p1) qbar(p2), photon propagator -i g/s
# sum_spins |M|^2 = (e^4 e_q^2 N_c / s^2) Tr[k2 g^m k1 g^n] Tr[p1 g_m p2 g_n]
# Tr[k2 g^m k1 g^n] = 4 (k2^m k1^n + k2^n k1^m - g^{mn} k1.k2)  (valid in any D), contracted with Tr[p1 g_m p2 g_n]:
Lt = 4 * (trace(lc_mul(slash(p1=1), slash(k2=1), slash(p2=1), slash(k1=1)))
          + trace(lc_mul(slash(p1=1), slash(k1=1), slash(p2=1), slash(k2=1)))
          - dot('k1', 'k2') * trace(lc_mul(slash(p1=1), gam('m'), slash(p2=1), gam('m'))))
t, u, alpha, eq = sp.symbols('t u alpha e_q', real=True)
kin = {dot('k1', 'k2'): s / 2, dot('p1', 'p2'): s / 2, dot('k1', 'p1'): -t / 2, dot('k2', 'p2'): -t / 2,
       dot('k1', 'p2'): -u / 2, dot('k2', 'p1'): -u / 2, D: 4}
M2 = sp.expand(Lt.subs(kin))
check('A2  sum|M|^2 (4D) = 8 e^4 e_q^2 N_c (t^2+u^2)/s^2  [trace part = 8(t^2+u^2)]',
      sp.simplify(M2 - 8 * (t ** 2 + u ** 2)) == 0)
c = sp.Symbol('c')
e2 = 4 * sp.pi * alpha
M2avg = sp.Rational(1, 4) * e2 ** 2 * eq ** 2 * Nc / s ** 2 * M2.subs({t: -s * (1 - c) / 2, u: -s * (1 + c) / 2})
# dsigma/dOmega = |M|^2/(64 pi^2 s) for massless 2->2 in the CM frame
sigma0 = sp.integrate(M2avg / (64 * sp.pi ** 2 * s) * 2 * sp.pi, (c, -1, 1))
check('A3  sigma_0 = 4 pi alpha^2 N_c e_q^2/(3 s)', sp.simplify(sigma0 - 4 * sp.pi * alpha ** 2 * Nc * eq ** 2 / (3 * s)) == 0)
# muon pair: N_c e_q^2 -> 1, so R_0 = N_c sum e_q^2
print('      sigma_0 =', sp.simplify(sigma0))

# D-dim two-body phase space for massless particles (derived in DERIVATION.md section 2.2)
Phi2 = (1 / (8 * sp.pi)) * (4 * sp.pi / s) ** eps * sp.gamma(1 - eps) / sp.gamma(2 - 2 * eps)
Om = lambda n: 2 * sp.pi ** (n / 2) / sp.gamma(n / 2)        # area of unit sphere S^{n-1} in R^n
Phi2_direct = (2 * sp.pi) ** (2 - (4 - 2 * eps)) * Om(3 - 2 * eps) * (sp.sqrt(s) / 2) ** (-2 * eps) / 8
check('A4  Phi_2 = (1/8pi)(4pi/s)^eps Gamma(1-eps)/Gamma(2-2eps)  (vs direct S^{D-2} integration)',
      all(abs(sp.N((Phi2 - Phi2_direct).subs({eps: ev, s: sp.Rational(37, 10)}), 30)) < 1e-25 for ev in [sp.Rational(1, 10), sp.Rational(-23, 100), sp.Rational(37, 100)]))

# LO spectral weight in D dims and the one-loop correlator:  Pi_LO = N_c e_q^2 2(D-2)/(D-1) G(1,1) (-q^2)^-eps /(4pi)^{D/2}
Dd = 4 - 2 * eps
G11 = sp.gamma(eps) * sp.gamma(1 - eps) ** 2 / sp.gamma(2 - 2 * eps)
rho_LO = 2 * (Dd - 2) * s * Phi2                                   # per N_c e_q^2
ImPi_LO = 2 * (Dd - 2) / (Dd - 1) * G11 * s ** (-eps) * sp.sin(sp.pi * eps) / (4 * sp.pi) ** (Dd / 2)
check('A5  exact LO cutting identity  rho_LO = 2(D-1) s Im Pi_LO(s+i0)  for all eps',
      sp.simplify(sp.gammasimp(rho_LO - 2 * (Dd - 1) * s * ImPi_LO)) == 0
      or all(abs(sp.N((rho_LO - 2 * (Dd - 1) * s * ImPi_LO).subs({eps: ev, s: sp.Rational(23, 10)}), 30)) < 1e-25
             for ev in [sp.Rational(11, 100), sp.Rational(-3, 10), sp.Rational(41, 100)]))
# 4D: rho_LO = s/(2 pi) N_c e_q^2  => Im Pi = rho/(6 s) = N_c e_q^2/(12 pi) => R_0 = 12 pi Im Pi = N_c e_q^2
check('A6  4D: Im Pi_LO = N_c e_q^2/(12 pi)  =>  R_0 = N_c sum e_q^2',
      sp.simplify(sp.limit(ImPi_LO, eps, 0) - 1 / (12 * sp.pi)) == 0)

# ==============================================================================================
# B. one-loop vertex (timelike form factor), exact in eps
# ==============================================================================================
print('=== B. one-loop massless quark form factor ===')
# Lambda^mu = -i g^2 C_F Int d^Dl/(2pi)^D  g^a (p1-l) g^mu (-p2-l) g_a / [ l^2 (p1-l)^2 (p2+l)^2 ]
# F1 = Tr[p1 Lambda^mu p2 g_mu] / Tr[p1 g^mu p2 g_mu]
num = trace(lc_mul(slash(p1=1), gam('a'), slash(p1=1, l=-1), gam('m'), slash(p2=-1, l=-1), gam('a'),
                   slash(p2=1), gam('m')))
Da, Db, Dc = sp.symbols('D_a D_b D_c')   # l^2, (p1-l)^2, (p2+l)^2
sub_ff = {dot('p1', 'p1'): 0, dot('p2', 'p2'): 0, dot('p1', 'p2'): s / 2, dot('l', 'l'): Da,
          dot('l', 'p1'): (Da - Db) / 2, dot('l', 'p2'): (Dc - Da) / 2}
numD = sp.expand(num.subs(sub_ff))
den_tree = sp.expand(trace(lc_mul(slash(p1=1), gam('m'), slash(p2=1), gam('m'))).subs(sub_ff))   # = -2(D-2)s
# one-loop integrals J(na,nb,nc) = Int d^Dl/(2pi)^D Da^-na Db^-nb Dc^-nc, in units of i/(4pi)^{D/2},
# as coefficient of (-s-i0)^{D/2-na-nb-nc}.  Needed: J(1,1,1), J(0,1,1), J(-1,1,1); the others are scaleless.
J111 = -sp.gamma(1 + eps) * sp.gamma(-eps) ** 2 / sp.gamma(1 - 2 * eps)        # coefficient of (-s)^{-1-eps}
J011 = G11                                                                    # coefficient of (-s)^{-eps}
# J(-1,1,1) = -(s/2) J(0,1,1) (shift + symmetric integration); in (-s)^{1-eps} units: +(1/2) J011
J_m111 = sp.Rational(1, 2) * G11


def J(na, nb, nc):
    if (na, nb, nc) == (1, 1, 1):
        return J111
    if (na, nb, nc) == (0, 1, 1):
        return J011
    if (na, nb, nc) == (-1, 1, 1):
        return J_m111
    if nb <= 0 or nc <= 0:        # remaining denominators depend on one light-like momentum only
        return 0
    raise ValueError((na, nb, nc))


poly = sp.Poly(numD, Da, Db, Dc)
loop = 0     # coefficient of i/(4pi)^{D/2} (-s)^{-eps}; (-s)^{...} powers made explicit with ms = -s
ms = sp.Symbol('ms')   # stands for (-s - i0)
for (ia, ib, ic), cf in poly.terms():
    na, nb, nc = 1 - ia, 1 - ib, 1 - ic
    val = J(na, nb, nc)
    if val == 0:
        continue
    loop += cf * val * ms ** (2 - na - nb - nc)          # times (ms)^{-eps}
loop = sp.expand(loop.subs(s, -ms))
# F1 = -i g^2 C_F * [ i/(4pi)^{D/2} * loop * ms^-eps ] / den_tree
F1_coef = sp.simplify((-sp.I) * sp.I * loop / den_tree.subs(s, -ms))   # times g^2 C_F ms^-eps/(4pi)^{D/2}
F1_coef = sp.simplify(F1_coef.subs(D, Dd))
print('      F1 = g^2 C_F (-s-i0)^-eps/(4pi)^{D/2} *', sp.factor(sp.gammasimp(F1_coef)))
# normalise:  F1 = (alpha_s C_F/4pi) (4pi)^eps (-s-i0)^-eps c_Gamma * f(eps),  c_Gamma = G(1+e)G(1-e)^2/G(1-2e)
cG = sp.gamma(1 + eps) * sp.gamma(1 - eps) ** 2 / sp.gamma(1 - 2 * eps)
# g^2/(4pi)^{D/2} = (alpha_s/4pi) (4pi)^eps * 4pi*4pi/(4pi)^2 ... : g^2/(4pi)^{2-eps} = 4 pi alpha_s (4pi)^eps/(4pi)^2 = (alpha_s/(4 pi)) (4pi)^eps
f_ff = sp.simplify(sp.gammasimp(F1_coef / cG))
print('      f(eps) =', sp.factor(f_ff))
f_exact = -(2 - eps + 2 * eps ** 2) / (eps ** 2 * (1 - 2 * eps))
check('B0  exact: f(eps) = -(2 - eps + 2 eps^2)/(eps^2 (1-2eps))  (numerically at 4 values of eps)',
      all(abs(sp.N((f_ff - f_exact).subs(eps, ev), 30)) < 1e-25 for ev in [sp.Rational(1, 10), sp.Rational(-27, 100), sp.Rational(33, 100), sp.Rational(51, 1000)]))
f_ff = f_exact
check('B1  F1 = (alpha_s C_F/4pi) c_Gamma (4pi mu^2/(-s-i0))^eps * [-2/eps^2 - 3/eps - 8 - 16 eps + O(eps^2)]',
      sp.simplify(laurent(f_ff, 1) - (-2 / eps ** 2 - 3 / eps - 8 - 16 * eps)) == 0)
print('      f(eps) series:', laurent(f_ff, 2))
# MS-bar normalisation check: c_Gamma (4pi)^eps = (4pi)^eps e^{-eps gamma}(1 - zeta2 eps^2/2 + ..)
fMS = laurent(f_ff * cG * sp.exp(eps * sp.EulerGamma), 0)
check('B2  in MS-bar normalisation [(4pi)^eps e^{-eps gamma_E}]: -2/eps^2 - 3/eps - 8 + zeta_2',
      sp.simplify(fMS - (-2 / eps ** 2 - 3 / eps - 8 + sp.pi ** 2 / 6)) == 0)

# 2 Re F1(s+i0):  (-s-i0)^-eps = s^-eps e^{i pi eps}
twoReF1 = 2 * f_ff * cG * sp.cos(sp.pi * eps)          # times (alpha_s C_F/4pi)(4pi/s)^eps
print('      2ReF1 /[(alpha_s C_F/4pi)(4pi/s)^eps c_Gamma] =', laurent(2 * f_ff * sp.cos(sp.pi * eps), 0))
check('B3  2 Re F1 = (alpha_s C_F/2pi) c_Gamma (4pi/s)^eps [-2/eps^2 - 3/eps - 8 + pi^2 + O(eps)]',
      sp.simplify(laurent(f_ff * sp.cos(sp.pi * eps), 0) - (-2 / eps ** 2 - 3 / eps - 8 + sp.pi ** 2)) == 0)

# MS-bar expanded form with L = ln(-(s+i0)/mu^2) = ln(s/mu^2) - i pi :
#   F1 = (as CF/4pi) e^{eps gE} (mu^2/(-s-i0))^eps c_Gamma f(eps)   [g0^2 = 4 pi as mu^2eps e^{eps gE}(4pi)^-eps]
Lc = sp.Symbol('L')
F1MS = laurent(sp.exp(eps * sp.EulerGamma) * cG * f_ff * sp.exp(-eps * Lc), 1)
expectF = -2 / eps ** 2 + (2 * Lc - 3) / eps - Lc ** 2 + 3 * Lc - 8 + sp.pi ** 2 / 6
check('B4  F1 = (as CF/4pi)[-2/eps^2 + (2L-3)/eps - L^2 + 3L - 8 + zeta_2 + O(eps)],  L = ln(s/mu^2) - i pi',
      sp.simplify(sum(F1MS.coeff(eps, k) * eps ** k for k in (-2, -1, 0)) - expectF) == 0)
check('B5  O(eps) term of the MS-bar bracket at L=0: -16 + 3 zeta_2/2 + 14 zeta_3/3 (cf. Moch-Vermaseren-Vogt 2005)',
      sp.simplify(F1MS.coeff(eps, 1).subs(Lc, 0) - (-16 + sp.pi ** 2 / 4 + sp.Rational(14, 3) * sp.zeta(3))) == 0)
ell = sp.Symbol('ell', real=True)
epsr = sp.Symbol('epsr', real=True, nonzero=True)
ImF = sp.expand(sp.im(sp.expand(expectF.subs(eps, epsr).subs(Lc, ell - sp.I * sp.pi)))).subs(epsr, eps)
ReF = sp.expand(sp.re(sp.expand(expectF.subs(eps, epsr).subs(Lc, ell - sp.I * sp.pi)))).subs(epsr, eps)
print('      Im F1/(as CF/4pi) =', ImF, ' ;  Re F1/(as CF/4pi) =', ReF)
check('B6  timelike: Re F1 gains +pi^2 relative to the spacelike value at the same |q^2|  (Re L^2 = ell^2 - pi^2)',
      sp.simplify(ReF - expectF.subs(Lc, ell) - sp.pi ** 2) == 0)

# ==============================================================================================
# C. real emission gamma* -> q(p1) qbar(p2) g(k)
# ==============================================================================================
print('=== C. real emission ===')
s13, s23, s12 = sp.symbols('s13 s23 s12', positive=True)
# M^nu = -g t^a ubar(p1)[ g^a (p1+k) g^nu / s13 - g^nu (p2+k) g^a / s23 ] v(p2) eps*_a
A1 = lc_mul(gam('a'), slash(p1=1, k=1), gam('m'), scal(1 / s13))
A2 = lc_mul(gam('m'), slash(p2=1, k=1), gam('a'), scal(-1 / s23))
Gam = lc_add(A1, A2)
B1 = lc_mul(gam('m'), slash(p1=1, k=1), gam('a'), scal(1 / s13))     # Dirac conjugate (reversed)
B2 = lc_mul(gam('a'), slash(p2=1, k=1), gam('m'), scal(-1 / s23))
Gbar = lc_add(B1, B2)
# (-g_{mu nu}) (-g_{alpha beta}) Tr[p1 Gam^{alpha mu} p2 Gbar^{beta nu}] : same index names => contracted with + sign
TR = trace(lc_mul(slash(p1=1), Gam, slash(p2=1), Gbar))
sub_r = {dot('p1', 'p1'): 0, dot('p2', 'p2'): 0, dot('k', 'k'): 0, dot('p1', 'p2'): s12 / 2,
         dot('k', 'p1'): s13 / 2, dot('k', 'p2'): s23 / 2}
TR = sp.simplify(TR.subs(sub_r).subs(s12, s - s13 - s23))
y13, y23, y12 = sp.symbols('y13 y23 y12', positive=True)
TRy = sp.simplify(TR.subs({s13: s * y13, s23: s * y23}).subs(D, Dd))
expected = 8 * (1 - eps) * ((1 - eps) * (y13 / y23 + y23 / y13) + 2 * (1 - y13 - y23) / (y13 * y23) - 2 * eps)
check('C1  -g_mn (-g_ab) sum|M|^2/(g^2 C_F N_c) = 8(1-eps)[(1-eps)(y13/y23+y23/y13) + 2 y12/(y13 y23) - 2 eps]',
      sp.simplify(TRy - expected) == 0)
check('C2  4D limit: (x1^2+x2^2)/((1-x1)(1-x2)) structure', sp.simplify(
    (expected.subs(eps, 0) / 8 - ((1 - y23) ** 2 + (1 - y13) ** 2) / (y13 * y23))) == 0)
# three-body phase space: dPhi3 = (4pi)^{2eps-3} s^{1-2eps}/(2 Gamma(2-2eps)) dy13 dy23 (y12 y13 y23)^-eps
# (normalisation derived by iterating two-body phase spaces; checked here against that iteration)
Phi3_tot_formula = (4 * sp.pi) ** (2 * eps - 3) * s ** (1 - 2 * eps) / (2 * sp.gamma(2 - 2 * eps)) * \
    sp.gamma(1 - eps) ** 3 / sp.gamma(3 - 3 * eps)
M2s = sp.Symbol('M2', positive=True)
Phi2m = Phi2 * (1 - M2s / s) ** (1 - 2 * eps)                 # q -> massless + mass M
Phi3_iter = sp.Integral(1 / (2 * sp.pi) * Phi2m * Phi2.subs(s, M2s), (M2s, 0, s))
vals = []
for ev in [0.1, -0.2]:
    f_num = sp.lambdify(M2s, (1 / (2 * sp.pi) * Phi2m * Phi2.subs(s, M2s)).subs({eps: ev, s: 1.7}), 'mpmath')
    vals.append(abs(mp.quad(f_num, [0, 1.7]) - sp.N(Phi3_tot_formula.subs({eps: ev, s: 1.7}), 20)))
check('C3  Phi_3 normalisation: iterated two-body phase space == formula (eps=0.1,-0.2)', max(vals) < 1e-12)


def dirichlet(a, b, c):
    """Int dy12 dy13 dy23 delta(1-sum) y12^(a-1) y13^(b-1) y23^(c-1)"""
    return sp.gamma(a) * sp.gamma(b) * sp.gamma(c) / sp.gamma(a + b + c)


# Int [dy](y12 y13 y23)^-eps * { (1-eps)(y13/y23 + y23/y13) + 2 y12/(y13 y23) - 2 eps }
Ireal = (1 - eps) * 2 * dirichlet(1 - eps, 2 - eps, -eps) + 2 * dirichlet(2 - eps, -eps, -eps) \
    - 2 * eps * dirichlet(1 - eps, 1 - eps, 1 - eps)
# rho_R/rho_LO = (alpha_s C_F/16pi)(4pi/s)^eps * Int T_R /((1-eps) Gamma(1-eps))   [DERIVATION.md eq. (2.14)]
#             = (alpha_s C_F/2pi)(4pi/s)^eps * Ireal/Gamma(1-eps)
realR = sp.gammasimp(Ireal / sp.gamma(1 - eps))      # times (alpha_s C_F/2pi)(4pi/s)^eps
print('      real (exact):  rho_R/rho_LO = (alpha_s C_F/2pi)(4pi mu^2/s)^eps *', sp.factor(realR))
# verify the prefactor algebra independently (numerically, eps = 0.13)
pref = (g ** 2 * CF * Phi3_tot_formula / sp.gamma(1 - eps) ** 3 * sp.gamma(3 - 3 * eps)) / rho_LO  # dPhi3 density / rho_LO
pref_claim = (g ** 2 / (4 * sp.pi)) * CF / (16 * sp.pi) * (4 * sp.pi / s) ** eps / ((1 - eps) * sp.gamma(1 - eps)) / s ** 0
check('C4  prefactor  g^2 C_F dPhi3/rho_LO = (alpha_s C_F/16pi)(4pi/s)^eps/((1-eps)Gamma(1-eps)) [per unit Int(...)dy]',
      abs(sp.N((pref - pref_claim).subs({eps: 0.13, s: 2.9, g: 1.1, CF: 1}), 20)) < 1e-15)
real_exact = 2 * (1 - 2 * eps) * (2 - 2 * eps + eps ** 2) * sp.gamma(1 - eps) ** 2 / (
    eps ** 2 * (1 - 3 * eps) * (2 - 3 * eps) * sp.gamma(1 - 3 * eps))
check('C4b exact: real = 2(1-2e)(2-2e+e^2) Gamma(1-e)^2/(e^2 (1-3e)(2-3e) Gamma(1-3e))',
      all(abs(sp.N((realR - real_exact).subs(eps, ev), 30)) < 1e-25 for ev in [sp.Rational(1, 10), sp.Rational(-27, 100), sp.Rational(23, 100)]))
realR = real_exact
real_norm = realR / cG           # relative to c_Gamma
print('      real / c_Gamma series:', laurent(real_norm, 1))
check('C5  real = (alpha_s C_F/2pi) c_Gamma (4pi/s)^eps [2/eps^2 + 3/eps + 19/2 - pi^2 + O(eps)]',
      sp.simplify(laurent(real_norm, 0) - (2 / eps ** 2 + 3 / eps + sp.Rational(19, 2) - sp.pi ** 2)) == 0)

# ==============================================================================================
# D. sum and R
# ==============================================================================================
print('=== D. real + virtual ===')
total = sp.gammasimp(realR + 2 * f_ff * cG * sp.cos(sp.pi * eps) / 2)   # both in units (alpha_s C_F/2pi)(4pi/s)^eps
# note 2ReF1 = (alpha_s C_F/4pi)*2 f cG cos = (alpha_s C_F/2pi) f cG cos
tot_ser = laurent(total, 1)
print('      (rho_R+rho_V)/rho_LO /[(alpha_s C_F/2pi)(4pi/s)^eps] =', tot_ser)
check('D1  1/eps^2 poles cancel', sp.simplify(tot_ser.coeff(eps, -2)) == 0)
check('D2  1/eps poles cancel', sp.simplify(tot_ser.coeff(eps, -1)) == 0)
check('D3  finite part = 3/2  =>  R = R_0 (1 + 3 C_F alpha_s/(4 pi)) = R_0(1 + alpha_s/pi) for C_F = 4/3',
      sp.simplify(tot_ser.coeff(eps, 0) - sp.Rational(3, 2)) == 0)
print('      O(eps) term of the sum (irrelevant at eps->0):', sp.nsimplify(tot_ser.coeff(eps, 1)))
# numerical spot check of the exact expressions (mpmath, eps -> small)
fnum = sp.lambdify(eps, total, 'mpmath')
mp.mp.dps = 40
vals = [fnum(mp.mpf(e)) for e in ['1e-6', '-1e-6']]
check('D4  numerical: exact (real+virtual) at eps=+-1e-6 equals 3/2 to 1e-5', all(abs(v - 1.5) < 1e-5 for v in vals))

# ==============================================================================================
# E. KLN illustrations
# ==============================================================================================
print('=== E. KLN: exclusive vs inclusive ===')
virt_ser = laurent(f_ff * cG * sp.cos(sp.pi * eps), 0)
real_ser = laurent(realR, 0)
print('      sigma(q qbar)   exclusive, O(as) part / [(as CF/2pi)(4pi/s)^eps]:', virt_ser)
print('      sigma(q qbar g) exclusive, O(as) part / [(as CF/2pi)(4pi/s)^eps]:', real_ser)
check('E1  each exclusive piece has a 1/eps^2 pole (soft-collinear), only the sum is finite',
      virt_ser.coeff(eps, -2) != 0 and real_ser.coeff(eps, -2) != 0)

# quark energy spectrum x = x1 = 2E_q/sqrt(s): real density at fixed x (y23 = 1-x, y13 = x v, y12 = x(1-v));
# the v-integrals are Beta functions:
x = sp.Symbol('x', positive=True)
B = lambda a, b: sp.gamma(a) * sp.gamma(b) / sp.gamma(a + b)
dens = x ** (1 - 2 * eps) * (1 - x) ** (-eps) * (
    (1 - eps) * x / (1 - x) * B(2 - eps, 1 - eps) + (1 - eps) * (1 - x) / x * B(-eps, 1 - eps)
    + 2 / (1 - x) * B(-eps, 2 - eps) - 2 * eps * B(1 - eps, 1 - eps))
# (1/rho_LO) d rho_R/dx = (as CF/2pi)(4pi/s)^eps dens(x)/Gamma(1-eps)
pole_x = sp.simplify(sp.limit(eps * dens / sp.gamma(1 - eps), eps, 0))
print('      residue at eps=0 of the x<1 real density:', sp.factor(pole_x))
check('E2  quark energy spectrum (x<1): collinear pole -(1/eps)(as CF/2pi)(1+x^2)/(1-x) = -(1/eps)(as/2pi) P_qq(x)',
      sp.simplify(pole_x + (1 + x ** 2) / (1 - x)) == 0)
# consistency: Int_0^1 dens dx /Gamma(1-eps) = total real
tot_from_dens = sp.Integer(0)
n = sp.Symbol('n')


def xmom(nn):
    """Int_0^1 x^nn dens(x) dx, exact (Beta functions)"""
    return ((1 - eps) * B(nn + 3 - 2 * eps, -eps) * B(2 - eps, 1 - eps)
            + (1 - eps) * B(nn + 1 - 2 * eps, 2 - eps) * B(-eps, 1 - eps)
            + 2 * B(nn + 2 - 2 * eps, -eps) * B(-eps, 2 - eps)
            - 2 * eps * B(nn + 2 - 2 * eps, 1 - eps) * B(1 - eps, 1 - eps))


check('E3  Int_0^1 dx (x-spectrum) = total real emission (exact, numerically at eps=-0.2,-0.31)',
      all(abs(sp.N((xmom(0) / sp.gamma(1 - eps) - realR).subs(eps, ev), 25)) < 1e-20 for ev in [sp.Rational(-2, 10), sp.Rational(-31, 100)]))
# Mellin moments of the full O(as) spectrum (real + virtual delta(1-x)) and their collinear poles
virt = f_ff * cG * sp.cos(sp.pi * eps)          # units (as CF/2pi)(4pi/s)^eps, multiplies delta(1-x)
gam_n = lambda nn: -sum(sp.Rational(1, k + 1) + sp.Rational(1, k + 3) for k in range(nn))   # Int x^n [(1+x^2)/(1-x)]_+
okE = True
for nn in range(0, 4):
    Mn = laurent(xmom(nn) / sp.gamma(1 - eps) + virt, 0)
    c2, c1 = sp.simplify(Mn.coeff(eps, -2)), sp.simplify(Mn.coeff(eps, -1))
    print('      moment n=%d: 1/eps^2 coeff = %s, 1/eps coeff = %s (expected %s)' % (nn, c2, c1, -gam_n(nn)))
    okE &= (c2 == 0) and sp.simplify(c1 + gam_n(nn)) == 0
check('E4  moments n=0..3 of dsigma/dx_q: 1/eps^2 cancels; 1/eps = -Int x^n [(1+x^2)/(1-x)]_+ (n=0: finite = total)', okE)

print()
print('SUMMARY: %d/%d checks passed' % (sum(p for _, p in PASS), len(PASS)))
