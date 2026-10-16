import sys,os; sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
a, Lb, CF, CA, nf, TF, c2, b1 = sp.symbols('alpha L_b C_F C_A n_f T_F c_2 beta_1')
pi, z3 = sp.pi, sp.zeta(3)
b0 = sp.Rational(11,3)*CA - sp.Rational(4,3)*TF*nf                     # CONTEXT beta_0
dadlnmu2 = -b0/(4*pi)*a**2 - b1/(16*pi**2)*a**3                          # mu^2 d alpha/d mu^2
gHH1 = -CF/pi
gHH2hat = CF/pi**2*(CA*(-sp.Rational(49,36)+pi**2/12-z3/2) + sp.Rational(5,9)*TF*nf)   # verified (BN, Kidonakis, GHKM)
gHH = gHH1*a + gHH2hat*a**2
def dlnmu2(F): return sp.expand(sp.diff(F, a)*dadlnmu2 + sp.diff(F, Lb))
def trunc(e, n=2): return sum(sp.expand(e).coeff(a, k)*a**k for k in range(1, n+1))
# --- corrected formula (claim E11)
lnSI = -a*CF/pi*Lb + a**2*(-CF*b0/(8*pi**2)*Lb**2 + gHH2hat*Lb + c2)
print('corrected: mu^2 dlnS_I/dmu^2 - gamma_HH  (through alpha^2) =', sp.simplify(trunc(dlnmu2(lnSI) - gHH)))
# --- APPB eq.(81) as printed: lnS_I^(2) = c2 - Gamma_S^(2) L_b + alpha^2 beta0^APPB C_F/(2 pi) L_b^2, with
#     Gamma_S^(2) printed = (alpha^2/pi^2)[C_F C_A(-49/36+pi^2/12-z3/2) + C_F N_F 5/18]  (= +gamma_HH^(2) for T_F=1/2)
b0A = -(sp.Rational(11,3)*CA - sp.Rational(4,3)*nf*TF)/(2*pi)
GS2_APPB = a**2*CF/pi**2*(CA*(-sp.Rational(49,36)+pi**2/12-z3/2) + nf*sp.Rational(5,18))
lnSI_APPB = -a*CF/pi*Lb + c2*a**2 - GS2_APPB*Lb + a**2*b0A*CF/(2*pi)*Lb**2
res = sp.simplify(trunc(dlnmu2(lnSI_APPB) - gHH).subs(TF, sp.Rational(1,2)))
print('APPB(81) printed: residual of RGE through alpha^2 =', sp.factor(res))
print('   L_b-coefficient of residual / (C_F beta0/(4 pi^2) alpha^2) =', sp.simplify(sp.expand(res).coeff(Lb)/(CF*b0.subs(TF,sp.Rational(1,2))/(4*pi**2)*a**2)))
print('   constant part of residual / (-2 gamma_HH^(2)) =', sp.simplify(sp.expand(res).subs(Lb,0)/(-2*gHH2hat.subs(TF,sp.Rational(1,2))*a**2)))
# --- RMP eq.(208): D^(2) = c2 + Gamma_S^(2) L_b - alpha^2 beta0 C_F/(2 pi) L_b^2, ln S_r = -D,
#     Gamma_S^(2) printed = -(alpha^2/pi^2)[C_F C_A(-49/36+pi^2/12-z3/2) + C_F N_F 5/18] (= -gamma_HH^(2))
GS2_RMP = -GS2_APPB
D_RMP = a*CF/pi*Lb + c2*a**2 + GS2_RMP*Lb - a**2*b0A*CF/(2*pi)*Lb**2
res2 = sp.simplify(trunc(dlnmu2(-D_RMP) - gHH).subs(TF, sp.Rational(1,2)))
print('RMP(208) printed: residual of RGE for ln S_r through alpha^2 =', sp.factor(res2), '   (only an L_b term: factor-2 L_b^2 error; single log correct)')
# --- D^(1) from RMP (203),(204),(207) and the RMP RGE (205) sign
Y = sp.symbols('Y')
S1 = a*CF/(2*pi)*(2-2*Y)*Lb      # (207), Y = Y+Y'
K1 = sp.diff(S1, Y)               # coefficient of (Y+Y')
D1 = sp.expand(S1 - Y*K1)
print('RMP: K^(1) =', K1, ';  D^(1) =', D1, ';  ln S_r^(1) = -D^(1) =', -D1, ';  mu^2 d lnS_r/dmu^2 at O(alpha) =', sp.diff(-D1, Lb))
