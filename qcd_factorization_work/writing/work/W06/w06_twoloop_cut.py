r"""
w06_twoloop_cut.py -- writer W06: checks of the Euclidean two-loop correlator (VF-EE-7), its MS-bar
renormalisation, the Adler function, the exact-in-eps cutting identity (VF-EE-8, re-proved here with the
real and virtual cuts that W06 recomputed from scratch in w06_ee_oneloop.py), and the IBP lemma of App C.

 T1  G(a,b) of lem:appC-bubble from Feynman parameters (numerical check of the closed form, Euclidean)
 T2  G(1+eps,1) closed form
 T3  IBP triangle rule derived symbolically (the integrand identity) and Ihat(1,1,1,1,1) = 6 zeta_3 + O(eps)
 P1  one-loop Pi_0 (VF-EE-3) and its MS-bar form (N_c e_q^2/12pi^2)(5/3 - L)
 P2  two-loop bare Pi in MS-bar units: 3/(8 eps) + 55/16 - 3 zeta_3 - (3/4) L + O(eps)
 P3  Pi_MS through O(alpha_s);  mu^2 dPi/dmu^2 and the Adler function
 X1  exact cutting identity, term by term (r1 G11^2 <-> rho_V, r2 G11 G(1+eps,1) <-> rho_R)
 X2  LO cutting identity rho_0 = 2(D-1) s Im Pi_0(s+i0), exact
Run: python3 -I w06_twoloop_cut.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w06_series import laurent

e = sp.Symbol('eps')
D = 4 - 2 * e
R = []


def check(name, cond):
    R.append((name, bool(cond)))
    print(('PASS  ' if cond else 'FAIL  ') + name)


def G(a, b):
    return sp.gamma(a + b - D / 2) * sp.gamma(D / 2 - a) * sp.gamma(D / 2 - b) / (sp.gamma(a) * sp.gamma(b) * sp.gamma(D - a - b))


# ------------------------------------------------------------------ T1: G(a,b) from Feynman parameters (Euclidean)
# int d^Dk/pi^{D/2} 1/[(k^2)^a ((k-q)^2)^b] = G(a,b) (Q^2)^{D/2-a-b};
# Feynman: Gamma(a+b)/(Gamma(a)Gamma(b)) int_0^1 dx x^{a-1}(1-x)^{b-1} Gamma(a+b-D/2)/Gamma(a+b) [x(1-x)Q^2]^{D/2-a-b}
mp.mp.dps = 30
okT1 = True
for (a_, b_, ev) in ((1, 1, 0.13), (2, 1, -0.21), (1.3, 0.8, 0.07), (2, 1.17, -0.4)):   # points inside the convergence domain
    Dv = 4 - 2 * mp.mpf(ev)
    al_, be_ = Dv / 2 - b_ - 1, Dv / 2 - a_ - 1        # x-integrand x^al (1-x)^be after the Feynman-parameter steps
    # remove the endpoint singularities by x = w^{1/(al+1)} on [0,1/2] and 1-x = w^{1/(be+1)} on [1/2,1]
    g1 = lambda w: (1 - w ** (1 / (al_ + 1))) ** be_ / (al_ + 1)
    g2 = lambda w: (1 - w ** (1 / (be_ + 1))) ** al_ / (be_ + 1)
    half = mp.mpf(1) / 2
    feyn = mp.gamma(a_ + b_ - Dv / 2) / (mp.gamma(a_) * mp.gamma(b_)) * (mp.quad(g1, [0, half ** (al_ + 1)]) + mp.quad(g2, [0, half ** (be_ + 1)]))
    closed = mp.gamma(a_ + b_ - Dv / 2) * mp.gamma(Dv / 2 - a_) * mp.gamma(Dv / 2 - b_) / (mp.gamma(a_) * mp.gamma(b_) * mp.gamma(Dv - a_ - b_))
    okT1 &= abs(feyn / closed - 1) < 1e-12
    print('      T1 point', (a_, b_, ev), 'rel. diff %.1e' % float(abs(feyn / closed - 1)))
check('T1  G(a,b) = Gamma(a+b-D/2)Gamma(D/2-a)Gamma(D/2-b)/(Gamma(a)Gamma(b)Gamma(D-a-b)) from Feynman parameters (numerical)', okT1)
G1e = sp.gamma(2 * e) * sp.gamma(1 - 2 * e) * sp.gamma(1 - e) / (sp.gamma(1 + e) * sp.gamma(2 - 3 * e))
check('T2  G(1+eps,1) = Gamma(2eps)Gamma(1-2eps)Gamma(1-eps)/(Gamma(1+eps)Gamma(2-3eps))', sp.simplify(sp.gammasimp(G(1 + e, 1) / G1e)) == 1)
# ------------------------------------------------------------------ T3: IBP
# integrand identity: d/dk.( (k-r)/(D1^a1 D2^a2 D5^a5) ) with D1=k^2, D2=(k-q)^2, D5=(k-r)^2, D3=r^2, D4=(r-q)^2
k = sp.symbols('k0:4'); r = sp.symbols('r0:4'); q = sp.symbols('q0:4')
a1, a2, a5 = sp.symbols('a1 a2 a5')
Dd = sp.Symbol('Dd')   # treat the divergence d/dk.(k-r) = Dd symbolically in "Dd" dimensions via the Euclidean dot product
dotE = lambda u, w: sum(ui * wi for ui, wi in zip(u, w))
D1 = dotE(k, k); D2 = dotE([ki - qi for ki, qi in zip(k, q)], [ki - qi for ki, qi in zip(k, q)])
D3 = dotE(r, r); D4 = dotE([ri - qi for ri, qi in zip(r, q)], [ri - qi for ri, qi in zip(r, q)])
D5 = dotE([ki - ri for ki, ri in zip(k, r)], [ki - ri for ki, ri in zip(k, r)])
F = D1 ** (-a1) * D2 ** (-a2) * D5 ** (-a5)
div = sum(sp.diff((k[i] - r[i]) * F, k[i]) for i in range(4))      # in 4 Euclidean components: divergence of (k-r) = 4
lhs = sp.simplify(div / F - 4)                                     # strip the "4" -> replaced by D below
rhs = (-a1 * (D1 + D5 - D3) / D1 - a2 * (D2 + D5 - D4) / D2 - 2 * a5)
import random
random.seed(11)
okT3a = True
for _ in range(5):
    vals = {sym: sp.Rational(random.randint(3, 17), 7) for sym in list(k) + list(r) + list(q)}
    vals.update({a1: sp.Rational(13, 10), a2: sp.Rational(7, 10), a5: sp.Rational(19, 10)})
    okT3a &= abs(sp.N((lhs - rhs).subs(vals), 40)) < 1e-30
check('T3a IBP integrand identity: (k-r).d_k F = F[-a1(D1+D5-D3)/D1 - a2(D2+D5-D4)/D2 - 2a5] (exact rational points)', okT3a)
# hence (D - a1 - a2 - 2a5) I = a1[I(1+5-) - I(1+3-)] + a2[I(2+5-) - I(2+4-)]; at a=(1,1,1,1,1):
# I(2,1,1,1,0) = G(2,1)G(1,1), I(2,1,0,1,1) = G(1,1)G(2,1+eps) (and the mirror images)
Ihat = -1 / e * G(1, 1) * (G(2, 1) - G(2, 1 + e))
ser = laurent(Ihat, e, 1)
check('T3b Ihat(1,1,1,1,1) = -(1/eps) G(1,1)[G(2,1) - G(2,1+eps)] = 6 zeta_3 + O(eps)', sp.simplify(ser.coeff(e, 0) - 6 * sp.zeta(3)) == 0 and ser.coeff(e, -1) == 0)
print('      O(eps) coefficient of Ihat(1,1,1,1,1):', sp.nsimplify(sp.simplify(ser.coeff(e, 1))))
fnum = sp.lambdify(e, sp.gammasimp(Ihat), 'mpmath')
mp.mp.dps = 80
check('T3c numerical (80 digits): Ihat at eps=1e-12 equals 6 zeta(3) = 7.2123... to 1e-10', abs(fnum(mp.mpf('1e-12')) - 6 * mp.zeta(3)) < 1e-10)
mp.mp.dps = 30

# ------------------------------------------------------------------ P1, P2, P3
L = sp.Symbol('L')       # L = ln(Q^2/mu^2)
Nc, eq, CF, a_s, g2 = sp.symbols('N_c e_q C_F alpha_s g2', positive=True)
# MS-bar factor of the correlator: mu^{2eps} S_eps^{-1}: (4pi)^{-eps} e^{eps gamma} mu^{2eps}; g0^2 = 4 pi a_s mu^{2eps} S^{-1}
msf = sp.exp(e * sp.EulerGamma) * (4 * sp.pi) ** (-e) * sp.exp(-e * L)        # mu^{2eps}(Q^2)^{-eps} -> e^{-eps L}
Pi0 = 2 * (D - 2) / (D - 1) * G(1, 1) / (4 * sp.pi) ** (D / 2)                   # per N_c e_q^2, times (Q^2)^{-eps}
P0ser = laurent(Pi0 * msf * 12 * sp.pi ** 2, e, 0)
check('P1  one-loop: (12 pi^2) mu^{2eps}S^{-1} Pi_0 = 1/eps + 5/3 - L + O(eps)', sp.simplify(P0ser - (1 / e + sp.Rational(5, 3) - L)) == 0)
r1 = -4 * (1 - e) * (2 - e + 2 * e ** 2) / (e * (3 - 2 * e))
r2 = 16 * (1 - e) * (1 - 2 * e) * (2 - 2 * e + e ** 2) / (e * (3 - 2 * e) * (2 - 3 * e))
# Pi1_bare = C_F g0^2 (Q^2)^{-2eps}/(4pi)^D [r1 G11^2 + r2 G11 G(1+eps,1)] per N_c e_q^2; g0^2 (Q^2)^{-2eps} mu-factors:
# with g0^2 = 4 pi a_s mu^{2eps} e^{eps gamma}(4pi)^{-eps} and the correlator factor mu^{2eps} e^{eps gamma}(4pi)^{-eps}:
msf2 = (4 * sp.pi) * sp.exp(2 * e * sp.EulerGamma) * (4 * sp.pi) ** (-2 * e) * sp.exp(-2 * e * L)
Pi1 = (r1 * G(1, 1) ** 2 + r2 * G(1, 1) * G1e) / (4 * sp.pi) ** D * msf2      # per C_F a_s N_c e_q^2
units = 1 / sp.pi * 1 / (12 * sp.pi ** 2)                                       # (a_s/pi) C_F N_c e_q^2/(12 pi^2)
P1ser = laurent(Pi1 / units, e, 0)
check('P2  two-loop bare (MS-bar factors): 3/(8eps) + 55/16 - 3 zeta_3 - (3/4) L + O(eps); no 1/eps^2, local pole',
      sp.simplify(P1ser - (sp.Rational(3, 8) / e + sp.Rational(55, 16) - 3 * sp.zeta(3) - sp.Rational(3, 4) * L)) == 0)
# Pi_MS = (N_c e_q^2/12pi^2)[5/3 - L + (a_s/pi)(3C_F/4)(55/12 - 4zeta3 - L)]
fin = (sp.Rational(55, 16) - 3 * sp.zeta(3) - sp.Rational(3, 4) * L)
check('P3a two-loop MS-bar finite part = (3/4)(55/12 - 4 zeta_3 - L) per C_F', sp.simplify(fin - sp.Rational(3, 4) * (sp.Rational(55, 12) - 4 * sp.zeta(3) - L)) == 0)
# RG: Pi_bare = mu^{-2eps}... ; the counterterm Z = z0/eps + a_s z1/eps; mu^2 dPi_MS/dmu^2 = -dPi_MS/dL (at this order)
PiMS = (sp.Rational(5, 3) - L) + a_s / sp.pi * sp.Rational(3, 4) * CF * (sp.Rational(55, 12) - 4 * sp.zeta(3) - L)   # units N_c e_q^2/(12 pi^2)
adler = sp.simplify(-12 * sp.pi ** 2 * sp.diff(PiMS, L) / (12 * sp.pi ** 2))      # D = -12 pi^2 Q^2 dPi/dQ^2 = -12pi^2 dPi/dL (units N_c e_q^2)
check('P3b Adler function D = N_c e_q^2 (1 + (3C_F/4) a_s/pi), L-independent', sp.simplify(adler - (1 + sp.Rational(3, 4) * CF * a_s / sp.pi)) == 0)
# continuation L -> ln(s/mu^2) - i pi : 12 pi Im Pi = N_c e_q^2 (1 + 3 C_F a_s/(4 pi))
ell = sp.Symbol('ell', real=True)
ImPi = sp.im(sp.expand(PiMS.subs(L, ell - sp.I * sp.pi)))
check('P3c R = 12 pi Im Pi(s+i0) = N_c e_q^2 (1 + (3C_F/4) a_s/pi)  [units N_c e_q^2/(12pi^2) -> times 12pi/(12pi^2)]',
      sp.simplify(12 * sp.pi * ImPi / (12 * sp.pi ** 2) - (1 + sp.Rational(3, 4) * CF * a_s / sp.pi)) == 0)
# pole terms: z0/eps with z0 = 1 (units N_c e_q^2/12pi^2), z1: (3/8)C_F/pi per a_s -> mu^2 dPi/dmu^2 = z0 + 2 a_s z1 (eps->0)
z0 = 1; z1 = sp.Rational(3, 8) * CF / sp.pi
check('P3d mu^2 dPi/dmu^2 from the poles: z0 + 2 z1 a_s = 1 + (3C_F/4) a_s/pi (q-independent)',
      sp.simplify(z0 + 2 * z1 * a_s - (1 + sp.Rational(3, 4) * CF * a_s / sp.pi)) == 0)

# ------------------------------------------------------------------ X1, X2: cutting identities, exact in eps
s = sp.Symbol('s', positive=True)
cG = sp.gamma(1 + e) * sp.gamma(1 - e) ** 2 / sp.gamma(1 - 2 * e)
Phi2 = 1 / (8 * sp.pi) * (4 * sp.pi / s) ** e * sp.gamma(1 - e) / sp.gamma(2 - 2 * e)
rho0 = 2 * (D - 2) * s * Phi2                         # per N_c e_q^2
fe = -(2 - e + 2 * e ** 2) / (e ** 2 * (1 - 2 * e))
# W06's own results (w06_ee_oneloop.py, checks C1, D3): bare coupling g2 = g0^2 (mu0 = 1)
rhoV = rho0 * (g2 / (4 * sp.pi)) * CF / (2 * sp.pi) * (4 * sp.pi / s) ** e * cG * sp.cos(sp.pi * e) * fe
rhoR = rho0 * (g2 / (4 * sp.pi)) * CF / (2 * sp.pi) * (4 * sp.pi / s) ** e * 2 * (1 - 2 * e) * (2 - 2 * e + e ** 2) * sp.gamma(1 - e) ** 2 / (e ** 2 * (1 - 3 * e) * (2 - 3 * e) * sp.gamma(1 - 3 * e))
im2 = s ** (-2 * e) * sp.sin(2 * sp.pi * e)          # Im (-s - i0)^{-2eps} = s^{-2eps} sin(2 pi eps)
lhsV = 2 * (D - 1) * s * im2 * CF * g2 * r1 * G(1, 1) ** 2 / (4 * sp.pi) ** D
lhsR = 2 * (D - 1) * s * im2 * CF * g2 * r2 * G(1, 1) * G1e / (4 * sp.pi) ** D


mp.mp.dps = 50
def numratio(expr, vals):
    return [abs(sp.N(expr.subs({e: sp.Rational(*vv), s: sp.Rational(7, 3), g2: 1}), 45) - 1) for vv in vals]
EPS = [(1, 41), (-6, 41), (9, 41), (13, 41), (-17, 41), (1, 1000)]
dV = numratio(lhsV / rhoV, EPS)
dR = numratio(lhsR / rhoR, EPS)
print('      max |ratio-1|: virtual %.1e, real %.1e  (45 digits, 6 values of eps)' % (max(dV), max(dR)))
okX1 = max(dV) < 1e-40 and max(dR) < 1e-40
# analytic: reduce each ratio with the reflection formula by hand (sin 2 pi eps = 2 sin pi eps cos pi eps)
qV = sp.gammasimp(sp.expand_trig(lhsV / rhoV))
qR = sp.gammasimp(sp.expand_trig(lhsR / rhoR))
print('      gammasimp(virtual ratio) =', sp.simplify(qV), ';  gammasimp(real ratio) =', sp.simplify(qR))
check('X1  2(D-1) s Im Pi1_bare(s+i0) = rho_V + rho_R exactly in eps, term by term', okX1)
# LO: 2(D-1) s Im Pi_0(s+i0) = rho_0
lhs0 = 2 * (D - 1) * s * 2 * (D - 2) / (D - 1) * G(1, 1) / (4 * sp.pi) ** (D / 2) * s ** (-e) * sp.sin(sp.pi * e)
q0 = sp.simplify(sp.gammasimp(sp.expand_trig(lhs0 / rho0)))
check('X2  LO: 2(D-1) s Im Pi_0(s+i0) = rho_0 = 2(D-2) s Phi_2 N_c e_q^2, exactly in eps', q0 == 1 or all(abs(sp.N((lhs0 / rho0).subs({e: sp.Rational(kk, 37), s: 3}), 40) - 1) < 1e-35 for kk in (1, -5, 7)))
check('X3  4D: Im Pi_0 = N_c e_q^2/(12 pi)', sp.simplify(sp.limit(2 * (D - 2) / (D - 1) * G(1, 1) / (4 * sp.pi) ** (D / 2) * sp.sin(sp.pi * e), e, 0) - 1 / (12 * sp.pi)) == 0)

print()
print('SUMMARY: %d/%d checks passed' % (sum(p for _, p in R), len(R)))
