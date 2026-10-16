import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

a, Lb, Lz, Lzeta, c = sp.symbols('a L_b L_z L_zeta c', real=True)
pi = sp.pi

# One-loop delta(1-x) coefficients as printed in RMP (arXiv v3 eqs. (185),(200),(207)) / PLB 811 (eqs. (13),(19)):
#   L_b = ln(mu^2 b^2 e^{2 gE}/4), L_z = ln(zeta_z/mu^2), L_zeta = ln(zeta/mu^2), a = alpha_s C_F/(2 pi)
ftilde1 = a*(-Lb**2/2 + Lb*(sp.Rational(5,2) - Lz) - sp.Rational(3,2) - Lz**2/2 + Lz)   # quasi-TMD (RMP eq. 200)
fTMD1   = a*(-Lb**2/2 + (sp.Rational(3,2) - Lzeta)*Lb + sp.Rational(1,2) - pi**2/12)   # TMD (RMP eq. 185)
# Off-light-cone soft function S_DY^(1) = a [2 - 2(Y+Y')] L_b and S_DY = exp[(Y+Y')K + D], S_r = e^{-D}
Y = sp.symbols('Y', real=True)
SDY1 = a*(2 - 2*Y)*Lb
K1 = sp.diff(SDY1, Y)              # coefficient of (Y+Y')
D1 = SDY1.subs(Y, 0)
Sr1 = -D1
print("K^(1) =", sp.simplify(K1), "   S_r^(1) =", sp.simplify(Sr1))

# PLB-type form:  ftilde * sqrt(S_r) = H * exp[c K ln(zeta_z/zeta)] * f^TMD ;  at one loop:
#   ftilde1 + Sr1/2 = H1 + c*K1*(Lz - Lzeta) + fTMD1
H1 = sp.symbols('H1')
eq = sp.expand(ftilde1 + Sr1/2 - (H1 + c*K1*(Lz - Lzeta) + fTMD1))
# H must be independent of L_b and L_zeta; collect
poly = sp.Poly(eq, Lb, Lzeta)
print("coefficients (in L_b, L_zeta):")
for mon, co in zip(poly.monoms(), poly.coeffs()):
    print("  ", mon, sp.factor(co))
sol_c = sp.solve([poly.coeff_monomial(Lb), poly.coeff_monomial(Lb*Lzeta)], c, dict=True)
print("solution for c from L_b and L_b*L_zeta terms:", sol_c)
H1sol = sp.solve(eq.subs(c, sp.Rational(1,2)), H1)[0]
print("H^(1) with c=1/2:", sp.factor(sp.expand(H1sol)))
print("compare a(-2+pi^2/12 - Lz^2/2 + Lz):", sp.simplify(H1sol - a*(-2 + pi**2/12 - Lz**2/2 + Lz)))
resid_c1 = sp.expand(eq.subs(c, 1).subs(H1, H1sol))
print("residual if c=1 (printed form):", sp.factor(resid_c1))

# General (all-order) argument: LHS independent of zeta; d/d ln zeta of RHS = -c K + (1/2) K  (since 2 zeta d ln f/d zeta = K)
Ksym = sp.symbols('K')
print("d/dln(zeta) of ln RHS =", sp.simplify(-c*Ksym + Ksym/2), " -> vanishes iff c = 1/2")
# momentum RGE: P^z d/dP^z ln ftilde = K + G ; zeta_z = (2 x P^z)^2 => d ln zeta_z/d ln P^z = 2
print("P^z d/dP^z of c K ln zeta_z =", 2*c*Ksym, " -> equals K iff c = 1/2")

# Ratio formula (RMP eq. 210 printed with exponent K):  ftilde(z1)/ftilde(z2) = H2/H1 * (zeta_z1/zeta_z2)^{cK}
P1, P2 = sp.symbols('P1 P2', positive=True)
x = sp.symbols('x', positive=True)
expo = c*Ksym*sp.log((2*x*P1)**2/(2*x*P2)**2)
print("ln of CS factor in ratio:", sp.simplify(sp.expand_log(expo, force=True)), "; with c=1/2 ->", sp.simplify(sp.expand_log(expo.subs(c, sp.Rational(1,2)), force=True)))

# One-loop check of K extraction (ESZ form): K = ln[ C(xP2) ftilde(P1) / (C(xP1) ftilde(P2)) ] / ln(P1/P2)
mu = sp.symbols('mu', positive=True)
LzP = lambda P: sp.log((2*x*P)**2/mu**2)
ft = lambda P: ftilde1.subs(Lz, LzP(P))
Cq = lambda P: (a*(-2 + pi**2/12 - Lz**2/2 + Lz)).subs(Lz, LzP(P))
Kext = sp.simplify(sp.expand_log((ft(P1) - Cq(P1)) - (ft(P2) - Cq(P2)), force=True)/sp.log(P1/P2))
print("one-loop K from ESZ ratio:", sp.simplify(sp.expand_log(Kext, force=True)))

# LFWF (N=1), real parts: quasi-WF  a{-Lb^2/2 + Lb[5/2 - (1/2)ln(zz zzb/mu^4)] - 3/2 - pi^2/2 + [-(1/4)l^2 + (1/2) l + (zz->zzb)]}
#                          LFWF     a{-Lb^2/2 + Lb[3/2 - (1/2)ln(ze zeb/mu^4)] + 1/2 - pi^2/12}
# with zeta_z/zeta = zetabar_z/zetabar (same boost) ; check coefficient of the CS exponent from L_b terms
lz, lzb, lze, lzeb = sp.symbols('lz lzb lze lzeb', real=True)
psit_Lb = a*Lb*(sp.Rational(5,2) - (lz + lzb)/2)
psi_Lb = a*Lb*(sp.Rational(3,2) - (lze + lzeb)/2)
lhs = psit_Lb + Sr1/2
rhs = c*K1*(lz - lze) + psi_Lb
d = sp.expand((lhs - rhs).subs(lzb, lz - lze + lzeb))
print("LFWF L_b residual:", sp.factor(d), " -> zero iff c = 1/2:", sp.solve(sp.Poly(d, Lb).coeffs()[0], c))
