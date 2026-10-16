import sys,os; sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
Lb,Lz,Lzeta=sp.symbols('L_b L_z L_zeta')
pi=sp.pi
# all in units of alpha_s C_F/(2 pi); delta(1-x) (virtual+soft) coefficients only; real part F(x) identical in both
ft   = -sp.Rational(1,2)*Lb**2 + Lb*(sp.Rational(5,2)-Lz) - sp.Rational(3,2) - sp.Rational(1,2)*Lz**2 + Lz   # APPB (39)
fTMD = -sp.Rational(1,2)*Lb**2 + (sp.Rational(3,2)-Lzeta)*Lb + sp.Rational(1,2) - pi**2/12              # APPB (23)
lnSI = -2*Lb            # S_I=e^{-D}, D^(1)=(as CF/pi) Lb  (APPB (79),(51))
K    = -2*Lb            # K^(1) = -(as CF/pi) Lb  (APPB (16))
H    = -2 + pi**2/12 - Lz**2/2 + Lz                       # APPB (85)
for c,name in [(sp.Rational(1,2),'exp[(1/2) K ln(zeta_z/zeta)]  (APPB eq.52)'),(1,'exp[K ln(zeta_z/zeta)]  (APPB eq.75 / PLB eq.22)')]:
    lhs = ft + sp.Rational(1,2)*lnSI
    rhs = H + c*K*(Lz-Lzeta) + fTMD
    print(name, ' -> LHS-RHS =', sp.simplify(lhs-rhs))
# check H^(1) against Ebert-Stewart-Zhao form (as CF/4pi)[-Lz^2+2Lz-4+pi^2/6]
print('H vs ESZ form:', sp.simplify(H - sp.Rational(1,2)*(-Lz**2+2*Lz-4+pi**2/6)))
# check PLB (25): ln H^(1) = c1 + CF/2pi (Lz - Lz^2/2), c1 = CF/2pi(-2+pi^2/12)
print('PLB(25) vs APPB(85):', sp.simplify((-2+pi**2/12 + Lz - Lz**2/2) - H))
# RG check: d lnH/d ln mu^2 at one loop = (1/2)Gamma_cusp Lz + gamma_C/2 ; Lz=ln(zeta_z/mu^2): d/dlnmu^2 Lz = -1
dH = -sp.diff(H,Lz)  # times (as CF/2pi)
print('mu^2 d lnH/d mu^2 (units as CF/2pi):', sp.expand(dH), '=> (1/2)Gamma_cusp*Lz with Gamma_cusp=as CF/pi -> coefficient of Lz must be 1:', sp.expand(dH).coeff(Lz))
# gamma_C^(1) = 2 gamma_F - Gamma_S + 2 gamma_J  with gamma_F^(1)= ? from ft: mu^2 d/dmu^2 ln ft: Lb->+1, Lz->-1
dft = sp.expand(sp.diff(ft,Lb) - sp.diff(ft,Lz)); print('mu^2 d ln ft/dmu^2 (units as CF/2pi):', dft)
