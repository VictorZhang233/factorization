# W26 / Ch23 -- s05: one-loop quasi-TMD matching, the factor 1/2 in the CS exponent, H = C+ C-, phases, RGEs
# (prop:yzliu-qtmd-powercount (iv), prop:yzliu-hard-kernel (a),(b), ex:yzliu-hl-decomposition; VF-LAM-15, VF-YZL-5/6)
# a = alpha_s C_F/(2 pi); L_zeta = ln(zeta_z/mu^2); lz = ln(zeta/mu^2); L_b = ln(mu^2 b^2/b0^2)
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

a, Lb, Lz, lz, c, h = sp.symbols('a L_b L_zeta l_zeta c h', real=True)
ft1 = a*(-sp.Rational(1, 2)*Lb**2 + Lb*(sp.Rational(5, 2) - Lz) - sp.Rational(3, 2) - sp.Rational(1, 2)*Lz**2 + Lz)   # quasi-TMD
f1 = a*(-sp.Rational(1, 2)*Lb**2 + (sp.Rational(3, 2) - lz)*Lb + sp.Rational(1, 2) - sp.pi**2/12)                # Collins TMD
Sr1 = -2*a*Lb; K1 = -2*a*Lb
res = sp.expand(ft1 + Sr1/2 - (h + c*K1*(Lz - lz) + f1))
sol = sp.solve([res.coeff(Lb, 1).coeff(Lz, 1), res.coeff(Lb, 1).coeff(lz, 1)], [c], dict=True)
print('coefficient of K ln(zeta_z/zeta) fixed by L_b L_zeta and L_b l_zeta terms: c =', sol)
assert sol == [{c: sp.Rational(1, 2)}]
H1 = sp.solve(res.subs(c, sp.Rational(1, 2)), h)[0]
print('H^(1) =', sp.factor(H1), '=', sp.expand(H1))
assert sp.simplify(H1 - a*(-2 + sp.pi**2/12 - Lz**2/2 + Lz)) == 0
print('with the printed exponent (c=1) the residual is', sp.factor(sp.expand(res.subs(c, 1) - res.subs(c, sp.Rational(1, 2)))))
# Ebert-Stewart-Zhao form
assert sp.simplify(H1 - a/2*(-Lz**2 + 2*Lz - 4 + sp.pi**2/6)) == 0
# momentum evolution: 2 zeta_z d/dzeta_z ln f~ = K + G, G = 2 zeta_z d ln H / d zeta_z ; d/dln zeta_z = d/dL_zeta
G1 = 2*sp.diff(H1, Lz)
print('G^(1) = 2 dH/dL_zeta =', sp.factor(G1), ' (= (alpha_s C_F/pi)(1-L_zeta))')
assert sp.simplify(G1 - 2*a*(1 - Lz)) == 0
assert sp.simplify(2*sp.diff(ft1, Lz) - (K1 + G1)) == 0
print('check 2 zeta_z dln f~/dzeta_z = K^(1) + G^(1): OK')
# RGE of H (Liu/JLS convention mu d/dmu = 2 mu^2 d/dmu^2; dL_zeta/dln mu = -2):
dH = sp.diff(H1, Lz)*(-2)
Gcusp, gC = sp.symbols('Gamma_cusp gamma_C')
print('mu dH^(1)/dmu =', sp.expand(dH), ' => Gamma_cusp = 2a = alpha_s C_F/pi, gamma_C^(1) = -2a = -alpha_s C_F/pi')
assert sp.simplify(dH - (2*a*Lz - 2*a)) == 0
# heavy-light decomposition H = C+ C-, C+- = 1 + (alpha_s C_F/(8pi)) (-4 - 5pi^2/6 + 2L - L^2), L = L_zeta +- i pi
Lp, Lm = Lz + sp.I*sp.pi, Lz - sp.I*sp.pi
Cp1 = a/4*(-4 - 5*sp.pi**2/6 + 2*Lp - Lp**2)
Cm1 = a/4*(-4 - 5*sp.pi**2/6 + 2*Lm - Lm**2)
print('C+^(1) + C-^(1) - H^(1) =', sp.simplify(sp.expand(Cp1 + Cm1 - H1)))
assert sp.simplify(sp.expand(Cp1 + Cm1 - H1)) == 0
ImCp = sp.simplify(sp.im(sp.expand(Cp1.subs({a: sp.Symbol('A', positive=True)}))))
print('Im C+^(1) =', ImCp, ' (A = a) -> (alpha_s C_F/4)(1-L_zeta)')
assert sp.simplify(ImCp - sp.Symbol('A', positive=True)*sp.pi/2*(1 - Lz)) == 0
print('phase of (C+)^2 at one loop = 2 Im C+^(1) = (alpha_s C_F/2)(1 - L_zeta)')
# identities used in ex:yzliu-hl-decomposition
print('L+ + L- =', sp.simplify(Lp + Lm), ';  L+^2 + L-^2 =', sp.expand(Lp**2 + Lm**2))
# LFWF-type kernel (C+-)^2 ; JLS threshold phase: A^(1) = (alpha_s C_F/2)(L_zeta - 1) = -2 Im C+^(1) ... sign conventions:
# Liu-Su (2.3): H_HL depends on ln(-2 i p_z sigma/mu) <=> 2 ln(...) = L_zeta - i pi sigma, i.e. sigma=+1 <-> C-
Am = 2*sp.im(sp.expand(Cm1.subs({a: sp.Symbol('A', positive=True)})))
print('sigma=+1: sigma A = 2 Arg C- =', sp.simplify(Am), ' -> A^(1) = (alpha_s C_F/2)(L_zeta-1) (Liu-Su (2.43): A(L=0) = -alpha C_F/2)')
print('PASS')
