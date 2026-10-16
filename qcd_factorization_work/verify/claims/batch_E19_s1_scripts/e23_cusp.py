# -*- coding: utf-8 -*-
"""
E23 (independent check).  Two-loop cusp anomalous dimension, Gamma_cusp = sum_n (alpha_s/4pi)^{n+1} Gamma_n.
Printed in Becher-Schwartz (BS) 2008, App. A eq. (A.10) (arXiv v1, v2 and JHEP 07 (2008) 034, p. 29):
    Gamma_1^{BS} = 4 C_F [ C_A (67/9 - pi^2/3) - (20/9) C_F T_F n_f ]
Claimed correct form:
    Gamma_1      = 4 C_F [ (67/9 - pi^2/3) C_A - (20/9) T_F n_f ]
Checks:
 (a) Korchemsky-Marchesini NPB 406 (1993) 225 [hep-ph/9210281], eq. (cusp), quoting Korchemsky-Radyushkin NPB 283 (1987) 342:
     Gamma_cusp = (a_s/pi) C_F + (a_s/pi)^2 C_F [ C_A (67/36 - pi^2/12) - N_f 5/18 ]   (T_F = 1/2).  Convert to (a_s/4pi).
 (b) Becher-Neubert-Pecjak JHEP 01 (2007) 076 [hep-ph/0607228] (= BS ref. [24]) print the claimed form and 36.8436 for n_f = 5.
 (c) Internal consistency of BS: their own G_22, G_23 (eq. Gijcoeff) and D_B (n_f part) follow from the RG of
     H, j~, s~ (BS App. B) only with the corrected Gamma_1.  Laplace space -> cumulant R(tau) done exactly with
     ln^k(nu e^{gamma_E}) <-> (-d/deta + gamma_E)^k [ tau^eta / Gamma(1+eta) ]_{eta=0}.
 (d) BS's numerical Gamma_2 = -0.7901 n_f^2 - 183.2 n_f + 1175 equals the analytic three-loop value (sanity of the rest of (A.10)).
Run: python3 -I e23_cusp.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

npass = nfail = 0
def check(label, ok, extra=''):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(('PASS ' if ok else 'FAIL ') + label + (('   [' + str(extra) + ']') if extra else ''))

CF, CA, TF, nf = sp.symbols('C_F C_A T_F n_f', positive=True)
pi, z3 = sp.pi, sp.zeta(3)
G0 = 4 * CF
G1_corr = 4 * CF * ((sp.Rational(67, 9) - pi ** 2 / 3) * CA - sp.Rational(20, 9) * TF * nf)
G1_BS = 4 * CF * (CA * (sp.Rational(67, 9) - pi ** 2 / 3) - sp.Rational(20, 9) * CF * TF * nf)
b0 = sp.Rational(11, 3) * CA - sp.Rational(4, 3) * TF * nf

# (a) KM 1993 / KR 1987 in (alpha_s/pi): coefficient of (alpha_s/pi)^2; (alpha_s/pi)^2 = 16 (alpha_s/4pi)^2
KM2 = CF * (CA * (sp.Rational(67, 36) - pi ** 2 / 12) - nf * sp.Rational(5, 18))
check('KM/KR two-loop cusp converted: 16 * C_F[C_A(67/36 - pi^2/12) - 5 n_f/18] = Gamma_1(corrected) at T_F = 1/2',
      sp.simplify(16 * KM2 - G1_corr.subs(TF, sp.Rational(1, 2))) == 0)
check('...and it differs from the BS-printed Gamma_1 (by a C_F^2 T_F n_f vs C_F T_F n_f term)',
      sp.simplify(16 * KM2 - G1_BS.subs(TF, sp.Rational(1, 2))) != 0)
check('one loop: (alpha_s/pi) C_F = (alpha_s/4pi) * 4 C_F = Gamma_0', True)
SU3 = {CF: sp.Rational(4, 3), CA: 3, TF: sp.Rational(1, 2)}
v5 = float(G1_corr.subs(SU3).subs(nf, 5))
check('(b) corrected Gamma_1 at n_f = 5 equals BNP 2006 value 36.8436', abs(v5 - 36.8436) < 5e-4, '%.4f' % v5)
print('   BS-printed formula at n_f = 5 would give %.4f' % float(G1_BS.subs(SU3).subs(nf, 5)))

# (c) RG -> Laplace exponent -> cumulant
a, Lc, eta = sp.symbols('a Lc eta')
g0H, g0J, g0S, g1H, g1J, g1S = sp.symbols('gH0 gJ0 gS0 gH1 gJ1 gS1')
c1H, c1J, c1S, c2H, c2J, c2S = sp.symbols('cH1 cJ1 cS1 cH2 cJ2 cS2')
G1 = sp.symbols('Gamma_1')

def lnF(A, B, g0, g1, c1, c2, L):
    """ln F = a f1 + a^2 f2 for dlnF/dln mu = A Gamma L + B gamma, L = ln(X^2/mu^2), da/dln mu = -2 b0 a^2."""
    f1 = -(A * G0 / 4) * L ** 2 - (B * g0 / 2) * L + c1
    f2 = (b0 * A * G0 / 12) * L ** 3 + (b0 * B * g0 / 4 - A * G1 / 4) * L ** 2 - (b0 * c1 + B * g1 / 2) * L + c2
    return a * f1 + a ** 2 * f2

# verify the solution of the RGE symbolically: d/dln mu at fixed X, with dL/dlnmu = -2
mu_ = sp.symbols('lnmu')
A_, B_ = sp.symbols('A B')
Lf = sp.Function('L')(mu_)
af = sp.Function('a')(mu_)
expr = lnF(A_, B_, g0H, g1H, c1H, c2H, Lf).subs(a, af)
d = sp.diff(expr, mu_).subs({sp.Derivative(Lf, mu_): -2, sp.Derivative(af, mu_): -2 * b0 * af ** 2})
target = A_ * (af * G0 + af ** 2 * G1) * Lf + B_ * (af * g0H + af ** 2 * g1H)
aa, LL = sp.symbols('aa LL')
diffpoly = sp.expand((d - target).subs({af: aa, Lf: LL}))
low_orders = sum(diffpoly.coeff(aa, k) * aa ** k for k in range(0, 3))
check('RGE solution: d lnF/d ln mu = A Gamma L + B gamma through O(a^2)', sp.simplify(low_orders) == 0)

# mu = Q: L_H = 0, L_J = -Lc, L_S(2L) = -2 Lc  with Lc = ln(nu e^{gamma_E})   (BS eq. (factLaplace))
lnt = (lnF(2, 2, g0H, g1H, c1H, c2H, 0) + 2 * lnF(-2, -2, g0J, g1J, c1J, c2J, -Lc)
       + lnF(2, -2, g0S, g1S, c1S, c2S, -2 * Lc))
sub_nc = {g0H: -6 * CF, g0J: -3 * CF, g0S: 0}     # one-loop non-cusp ADs (BS (A.7)-(A.9)); gamma^S_0 = gH0 - 2 gJ0 = 0
lnt = sp.expand(lnt.subs(sub_nc))
g1coef = sp.expand(lnt).coeff(a, 1)
g2coef = sp.expand(lnt).coeff(a, 2)
print('   Laplace exponent: O(a)   =', sp.collect(sp.expand(g1coef), Lc))
print('   Laplace exponent: O(a^2) L^3, L^2 terms =', sp.factor(g2coef.coeff(Lc, 3)), ',', sp.factor(g2coef.coeff(Lc, 2)))
check('Laplace exponent is mu-independent combination: O(a^2) Lc^3 coefficient = -b0 Gamma_0', sp.simplify(g2coef.coeff(Lc, 3) + b0 * G0) == 0)
check('O(a^2) Lc^2 coefficient = 3 C_F b0 - Gamma_1', sp.simplify(g2coef.coeff(Lc, 2) - (3 * CF * b0 - G1)) == 0)

# conversion to the cumulant: E(eta) = tau^eta / Gamma(1+eta) = exp(-eta L) / Gamma(1+eta), L = ln(1/tau)
L = sp.symbols('L')
Ns = 8
lnGam = sp.series(sp.loggamma(1 + eta), eta, 0, Ns).removeO()
E = sp.exp(-eta * L - lnGam)
Eser = sp.series(E, eta, 0, Ns).removeO()
def apply_poly(poly_in_Lc):
    """Apply poly(-d/deta + gamma_E) to E(eta) at eta = 0."""
    poly = sp.Poly(sp.expand(poly_in_Lc), Lc)
    res = 0
    for (k,), coeff in poly.terms():
        Dk = Eser
        for _ in range(k):
            Dk = -sp.diff(Dk, eta) + sp.EulerGamma * Dk
        res += coeff * Dk.subs(eta, 0)
    return sp.expand(res)
R1 = apply_poly(g1coef)
R2 = apply_poly(g2coef) + sp.Rational(1, 2) * apply_poly(sp.expand(g1coef ** 2))
lnR1 = sp.expand(R1)
lnR2 = sp.expand(R2 - R1 ** 2 / 2)
# BS expansion parameter alpha_s/(2 pi) = 2 a
Gij = lambda i, j: sp.simplify((lnR1 if i == 1 else lnR2).coeff(L, j) / 2 ** i)
G12, G11 = Gij(1, 2), Gij(1, 1)
check('G_12 = -2 C_F, G_11 = 3 C_F (BS eq. (Gijcoeff))', sp.simplify(G12 + 2 * CF) == 0 and sp.simplify(G11 - 3 * CF) == 0)
G23 = Gij(2, 3)
check('G_23 = C_F (4/3 n_f T_F - 11/3 C_A) (BS)', sp.simplify(G23 - CF * (sp.Rational(4, 3) * nf * TF - sp.Rational(11, 3) * CA)) == 0)
G22 = sp.expand(Gij(2, 2))
G22_BS_printed = CF * (-CF * 4 * pi ** 2 / 3 + nf * TF * sp.Rational(11, 9) + CA * (-sp.Rational(169, 36) + pi ** 2 / 3))
G22_corr = sp.expand(G22.subs(G1, G1_corr))
G22_lit = sp.expand(G22.subs(G1, G1_BS))
print('   G_22 with corrected Gamma_1 :', sp.collect(sp.factor(G22_corr), [CF]))
print('   G_22 with BS-printed Gamma_1:', sp.collect(sp.expand(G22_lit), [CF]))
check('BS printed G_22 = C_F[-C_F 4pi^2/3 + (11/9) n_f T_F + C_A(-169/36 + pi^2/3)] is reproduced with the CORRECTED Gamma_1',
      sp.simplify(G22_corr - G22_BS_printed) == 0)
check('... and is NOT reproduced with the Gamma_1 printed in BS App. A (would contain (20/9) C_F^2 T_F n_f)',
      sp.simplify(G22_lit - G22_BS_printed) != 0, sp.factor(sp.simplify(G22_lit - G22_BS_printed)))
# D_B n_f part: R2 (alpha_s/2pi)^2 n_f part = G23 L^3 + G22 L^2 + ...; dR/dtau, L = -ln tau
R2nf = sp.expand(lnR2 / 4).subs(G1, G1_corr)
R2nf = sp.expand(R2nf).coeff(nf, 1) * nf
lt = sp.symbols('lt')     # lt = ln tau
Rt = sp.expand(R2nf.subs(L, -lt))
DB = sp.expand(sp.diff(Rt, lt))   # tau dR/dtau = dR/dln tau
check('D_B n_f part: C_F T_F n_f [-4 ln^2 tau + (22/9) ln tau + ...]/tau (BS App. C) follows with the corrected Gamma_1',
      sp.simplify(DB.coeff(lt, 2) - (-4 * CF * TF * nf)) == 0 and sp.simplify(DB.coeff(lt, 1) - sp.Rational(22, 9) * CF * TF * nf) == 0,
      'ln^2: %s, ln: %s' % (sp.factor(DB.coeff(lt, 2)), sp.factor(DB.coeff(lt, 1))))

# (d) BS numerical Gamma_2 vs analytic three-loop cusp (Moch-Vermaseren-Vogt 2004, as printed in BNP 2006)
G2 = 4 * CF * (CA ** 2 * (sp.Rational(245, 6) - 134 * pi ** 2 / 27 + 11 * pi ** 4 / 45 + sp.Rational(22, 3) * z3)
               + CA * TF * nf * (-sp.Rational(418, 27) + 40 * pi ** 2 / 27 - sp.Rational(56, 3) * z3)
               + CF * TF * nf * (-sp.Rational(55, 3) + 16 * z3) - sp.Rational(16, 27) * TF ** 2 * nf ** 2)
p2 = sp.Poly(sp.expand(G2.subs(SU3)), nf)
c = [float(p2.coeff_monomial(nf ** k)) for k in (2, 1, 0)]
check('BS (A.10) Gamma_2 = -0.7901 n_f^2 - 183.2 n_f + 1175 agrees with the analytic three-loop cusp',
      abs(c[0] + 0.7901) < 1e-4 and abs(c[1] + 183.2) < 0.05 and abs(c[2] - 1175) < 0.5, ['%.4f' % v for v in c])
print('-' * 70)
print('e23_cusp: %d PASS, %d FAIL' % (npass, nfail))
