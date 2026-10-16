import sys,os; sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
CF, CA, nf, TF = sp.symbols('C_F C_A n_f T_F', positive=True)
pi, z2, z3, z4 = sp.pi, sp.pi**2/6, sp.zeta(3), sp.pi**4/90
half = sp.Rational(1, 2)
# ---------- (1) building blocks from literature NOT by Liu et al. (all in (alpha_s/4pi)^2 units, mu d/dmu convention)
# Becher-Neubert JHEP06(2009)081 [0903.1126] App.A: gamma^q_1 ; gamma^V = 2 gamma^q
gq1 = CF**2*(-sp.Rational(3,2)+2*pi**2-24*z3) + CF*CA*(-sp.Rational(961,54)-11*pi**2/6+26*z3) + CF*TF*nf*(sp.Rational(130,27)+2*pi**2/3)
gV2 = 2*gq1
# Chetyrkin-Grozin NPB666(2003)289 eq.(13): HQET heavy-light current  gamma~_j1 ; matrix element runs with -gamma~_j
gj1 = CF*(CF*(-16*z2+sp.Rational(5,2)) + CA*(4*z2-sp.Rational(49,6)) + TF*nf*sp.Rational(10,3))
gF2 = -gj1
# Becher-Neubert PRD79(2009)125004 eq.(13): gamma^Q_1 ; large-angle constant gamma_HH = 2 gamma^Q (checked vs Kidonakis, GHKM)
gQ1 = CF*CA*(2*pi**2/3-sp.Rational(98,9)-4*z3) + sp.Rational(40,9)*CF*TF*nf
gHH2 = 2*gQ1
gC2_indep = sp.expand((gV2 + 2*gF2 + gHH2)/(16*pi**2))     # coefficient of alpha_s^2
gC2_indep = gC2_indep.subs(TF, half)
# ---------- (2) printed values
gH_A13 = (1188*z3-99*pi**2-1108)/(432*pi**2)*CF*CA - (36*z3+6-7*pi**2)/(12*pi**2)*CF**2 + (sp.Rational(1,24)+10/(27*pi**2))*CF*nf
a1 = 60*z3-19*pi**2/3+sp.Rational(68,27); a2 = -48*z3+28*pi**2/3-8; a3 = 2*pi**2/3-sp.Rational(62,27)
gC_PLB = (a1*CF*CA+a2*CF**2+a3*CF*nf)/(16*pi**2)
print('(1) independent [BN09 gamma^V + 2(-CG03 gamma~_j) + 2 BN09 gamma^Q]  -  JHEP(A.13) =', sp.simplify(gC2_indep-gH_A13))
# ---------- (3) extract from del Rio-Vladimirov PRD108(2023)114009 eq.(26) (direct NNLO computation), a_s = alpha_s/(4pi)
Lp, a = sp.symbols('L_p a')
N = nf
c1 = CF*(-Lp**2-2*Lp-4+z2)
c2 = CF*( CF/2*Lp**4 + Lp**3*(2*CF-sp.Rational(11,9)*CA+sp.Rational(2,9)*N)
        + Lp**2*(CF*(6-z2)+CA*(-sp.Rational(100,9)+2*z2)+sp.Rational(16,9)*N)
        + Lp*(CF*(4+26*z2-24*z3)+CA*(-sp.Rational(950,27)-sp.Rational(22,3)*z2+22*z3)+N*(sp.Rational(304,54)+sp.Rational(4,3)*z2))
        + CF*(-12+116*z2-30*z3-sp.Rational(475,4)*z4)+CA*(-sp.Rational(3884,81)-sp.Rational(559,18)*z2+sp.Rational(241,9)*z3+sp.Rational(99,2)*z4)
        + N*(sp.Rational(656,81)+sp.Rational(17,9)*z2+sp.Rational(2,9)*z3) )
lnC = a*c1 + a**2*sp.expand(c2 - c1**2/2)
b0 = sp.Rational(11,3)*CA - sp.Rational(2,3)*N             # d a/d ln mu^2 = -b0 a^2
Gc = 4*a*CF + a**2*CF*(CA*(sp.Rational(268,9)-8*z2)-sp.Rational(40,9)*N)
dlnC = sp.expand(sp.diff(lnC, Lp) + sp.diff(lnC, a)*(-b0*a**2))
rhs_log = -Gc/2*Lp
rem = sp.expand(dlnC - rhs_log)          # must be L_p independent: = non-cusp AD per d ln mu^2
print('(3) dRV(26): residual L_p dependence at a^1, a^2 (must vanish):', sp.simplify(rem.coeff(a,1).diff(Lp)), '|', sp.simplify(rem.coeff(a,2).diff(Lp)))
G1 = sp.simplify(rem.coeff(a,1).subs(Lp,0)); G2 = sp.simplify(rem.coeff(a,2).subs(Lp,0))
print('    non-cusp AD (per d ln mu^2), a_s^1:', G1, ' -> mu d/dmu, alpha_s units:', sp.simplify(2*G1/(4*pi)))
gC2_dRV = sp.expand(2*G2/(16*pi**2))     # mu d/dmu and alpha_s^2 units
print('    dRV-extracted gamma_C^(2) - JHEP(A.13) =', sp.simplify(gC2_dRV-gH_A13))
print('    dRV-extracted gamma_C^(2) - PLB(26)    =', sp.simplify(gC2_dRV-gC_PLB))
# ---------- (4) PLB - correct, and decomposition
gHH2_al = sp.expand(gHH2.subs(TF, half)/(16*pi**2))
d = sp.simplify(gC_PLB - gH_A13)
print('(4) PLB(26) - correct =', sp.factor(d))
print('    PLB(26) - correct - (-2 gamma_HH^(2) + C_F n_f/(24 pi^2)) =', sp.simplify(d - (-2*gHH2_al + CF*nf/(24*pi**2))))
print('    C_F^2 parts: PLB', sp.nsimplify(sp.expand(gC_PLB).coeff(CF**2)), ' A13', sp.nsimplify(sp.expand(gH_A13).coeff(CF**2)), ' equal:', sp.simplify(sp.expand(gC_PLB).coeff(CF**2)-sp.expand(gH_A13).coeff(CF**2))==0)
print('    numeric (C_F=4/3,C_A=3,n_f=4): A13 =', sp.N(gH_A13.subs({CF:sp.Rational(4,3),CA:3,nf:4})), ' PLB =', sp.N(gC_PLB.subs({CF:sp.Rational(4,3),CA:3,nf:4})))
# ---------- (5) Liu-Su JHEP02(2024)204 large-beta0 n_f parts (2.41)-(2.42) printed forms, compare n_f coefficient of A13
print('(5) n_f coeff of (A.13):', sp.nsimplify(sp.expand(gH_A13).coeff(nf)/CF), ' = (80+9 pi^2)/(216 pi^2)?', sp.simplify(sp.expand(gH_A13).coeff(nf)/CF - (80+9*pi**2)/(216*pi**2))==0)
