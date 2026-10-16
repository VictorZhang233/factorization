# Stage-2 check of E02 (quasi-TMD part). Units a = as CF/(2pi); Lb = ln(mu^2 b^2 e^{2gE}/4),
# Lz = ln(zeta_z/mu^2), Lzeta = ln(zeta/mu^2).  Only delta(1-x) parts are needed (the x-dependent
# F(x) parts of f~ and f^TMD are identical: RMP eqs. (185), (200)).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
Lb, Lz, Lze, c, Y = sp.symbols('L_b L_z L_zeta c Y', real=True)
pi = sp.pi
# (A) RMP arXiv v2 inputs
ft  = -Lb**2/2 + Lb*(sp.Rational(5,2) - Lz) - sp.Rational(3,2) - Lz**2/2 + Lz     # (200)
f   = -Lb**2/2 + (sp.Rational(3,2) - Lze)*Lb + sp.Rational(1,2) - pi**2/12        # (185)
SDY = (2 - 2*Y)*Lb                                                              # (207), Y := Y+Y'
K   = sp.diff(SDY, Y)            # S_DY = exp[(Y+Y')K + D]  ->  K = d S^(1)/dY
D   = SDY.subs(Y, 0)
Sr  = -D                         # (204): S_r = e^{-D}
print("K^(1) =", K, "   S_r^(1) =", Sr)
hRMP = -2 + pi**2/12 - Lz**2/2 + Lz                                              # (213), H_RMP = e^{-h}
# PLB/JLL form: f~ sqrt(S_r) = H e^{c K ln(zeta_z/zeta)} f ; at one loop H^(1) = h^(1) (H_PLB = 1/H_RMP)
res = sp.expand(ft + Sr/2 - (hRMP + c*K*(Lz - Lze) + f))
print("residual(c) =", sp.factor(res))
print("  c=1/2 ->", sp.simplify(res.subs(c, sp.Rational(1,2))), " ;  c=1 ->", sp.factor(res.subs(c, 1)))
# CS-equation consistency: 2 zeta d/dzeta ln f = K  <=> 2 d f^(1)/dLzeta = K
print("2 df/dLzeta =", sp.diff(2*f, Lze), " (should equal K)")
print("2 df~/dLz   =", sp.diff(2*ft, Lz), " = K + G with G^(1) =", sp.expand(sp.diff(2*ft, Lz) - K))
# (B) ESZ (PRD 99 034505) inputs: f~naive = C * gS * exp[1/2 gamma_zeta ln(zeta~/zeta)] * f
C_ESZ = sp.Rational(1,2)*(-Lz**2 + 2*Lz - 4 + pi**2/6)       # (as CF/4pi) C^(1) in units of a
gS    = Lb
ft_ESZ = sp.expand(C_ESZ + gS + sp.Rational(1,2)*K*(Lz - Lze) + f)
print("ESZ-built naive quasi-TMD delta term:", sp.expand(ft_ESZ), "\n   minus RMP (200):", sp.simplify(ft_ESZ - ft))
# ratio formula: f~(z1)/f~(z2) = [H(z1)/H(z2)] (zeta_z1/zeta_z2)^{cK}; ESZ: gamma = ln[...]/ln(P1/P2) -> c = 1/2
L1, L2 = sp.symbols('L1 L2', real=True)
lhs = ft.subs(Lz, L1) - ft.subs(Lz, L2)
rhs = hRMP.subs(Lz, L1) - hRMP.subs(Lz, L2) + c*K*(L1 - L2)
print("ratio residual(c) =", sp.factor(sp.expand(lhs - rhs)))
# ESZ estimator: gamma = [ln f~1 - ln f~2 - (ln C1 - ln C2)] / ln(P1/P2) with ln(P1/P2) = (L1-L2)/2
gam = sp.simplify((lhs - (C_ESZ.subs(Lz, L1) - C_ESZ.subs(Lz, L2)))/((L1 - L2)/2))
print("ESZ ratio estimator returns gamma_zeta^(1) =", gam, " (K^(1) =", K, ")")
