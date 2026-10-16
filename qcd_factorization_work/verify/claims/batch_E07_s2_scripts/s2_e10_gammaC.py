# E10 stage-2 check: two-loop non-cusp anomalous dimension gamma_C of the quasi-TMD matching kernel H,
#   mu dlnH/dmu = Gamma_cusp ln(zeta_z/mu^2) + gamma_C    (PLB 811 eq. (23); JHEP 08 (2023) 037 eq. (4.4), gamma~_H = gamma_C).
# Route used here (different from stage 1): H = C_HL^+ C_HL^- (product of two heavy-light Sudakov form factors);
# the matching coefficient of the HQET heavy-light current onto the SCET heavy-to-light current has
#   dlnC_HL/dlnmu = (1/2)Gamma_cusp ln(zeta/mu^2) + gamma' - gamma~_J,
# because the QCD b->u current matches as J_QCD = C(mu) J_SCET with dlnC/dlnmu = Gamma_cusp ln(u m_b/mu) + gamma'
# (Bell NPB 812 (2009) 264, arXiv:0810.5695, eqs. (39)-(42)), and J_QCD = C_m(mu) J~_HQET(mu) with
# J~(mu) = Z~_J^{-1} J~_0, gamma~_J = dlnZ~_J/dlnmu (Broadhurst-Grozin PRD 52 (1995) 4082, arXiv:hep-ph/9410240, eq. (2.1)).
# Hence gamma_C = 2 (gamma' - gamma~_J). One-loop check: 2(-5 CF + 3 CF) a = -4 CF a = -CF as/pi.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
CF, CA, nf, TF = sp.symbols('C_F C_A n_f T_F')
pi, z3 = sp.pi, sp.zeta(3)
z2 = pi**2/6
a = sp.Symbol('a')  # a = alpha_s/(4 pi)
gp1 = -5*CF
gp2 = CF**2*(2*pi**2 - sp.Rational(3, 2) - 24*z3) + CA*CF*(22*z3 - sp.Rational(1549, 54) - 7*pi**2/6) + nf*TF*CF*(sp.Rational(250, 27) + 2*pi**2/3)
gJ1 = -3*CF
gJ2 = CF*(CF*(sp.Rational(5, 2) - 16*z2) + CA*(sp.Rational(-49, 6) + 4*z2) + sp.Rational(10, 3)*TF*nf)
gC1 = 2*(gp1 - gJ1)            # coefficient of a
gC2 = 2*(gp2 - gJ2)            # coefficient of a^2
# convert to coefficients of alpha_s, alpha_s^2:  a = alpha_s/(4pi)
gC1_as = sp.simplify(gC1/(4*pi)); gC2_as = sp.expand(gC2/(16*pi**2))
print('gamma_C^(1) (coeff of alpha_s) =', gC1_as)
# JHEP 2023 (A.12)-(A.13)
A13 = (1188*z3 - 99*pi**2 - 1108)/(432*pi**2)*CF*CA - (36*z3 + 6 - 7*pi**2)/(12*pi**2)*CF**2 + (sp.Rational(1, 24) + 10/(27*pi**2))*CF*nf
print('gamma_C^(2)[Bell + Broadhurst-Grozin, T_F=1/2] - JHEP(A.13) =', sp.simplify(gC2_as.subs(TF, sp.Rational(1, 2)) - A13))
# PLB 811 eq. (26)
a1 = 60*z3 - 19*pi**2/3 + sp.Rational(68, 27)
a2 = -48*z3 + 28*pi**2/3 - 8
a3 = 2*pi**2/3 - sp.Rational(62, 27)
PLB = (a1*CF*CA + a2*CF**2 + a3*CF*nf)/(16*pi**2)
gHH2 = CF/pi**2*(CA*(sp.Rational(-49, 36) + pi**2/12 - z3/2) + sp.Rational(5, 18)*nf)      # T_F = 1/2
d = sp.simplify(PLB - A13)
print('PLB(26) - correct =', sp.factor(d))
print('PLB(26) - correct - (-2 gamma_HH^(2) + C_F n_f/(24 pi^2)) =', sp.simplify(d - (-2*gHH2 + CF*nf/(24*pi**2))))
print('C_F^2 parts: PLB', sp.simplify(sp.expand(PLB).coeff(CF, 2)), ' correct', sp.simplify(sp.expand(A13).coeff(CF, 2)), ' difference', sp.simplify(sp.expand(PLB - A13).coeff(CF, 2)))
num = {CF: sp.Rational(4, 3), CA: 3, nf: 4}
print('numerics (n_f=4): correct gamma_C^(2) =', sp.N(A13.subs(num), 8), '; PLB(26) =', sp.N(PLB.subs(num), 8))
# consistency with gamma' = gamma^q + gamma^Q (Becher-Neubert), i.e. gamma_C = gamma_V + 2 gamma_F + gamma_HH:
gq1 = CF**2*(-sp.Rational(3, 2) + 2*pi**2 - 24*z3) + CF*CA*(-sp.Rational(961, 54) - 11*pi**2/6 + 26*z3) + CF*TF*nf*(sp.Rational(130, 27) + 2*pi**2/3)
gQ1 = CF*CA*(2*pi**2/3 - sp.Rational(98, 9) - 4*z3) + sp.Rational(40, 9)*CF*TF*nf
print("check gamma'^(2) = gamma^q_1 + gamma^Q_1 :", sp.simplify(gp2 - gq1 - gQ1))
