# W26 / Ch23 -- s06: two-loop heavy-light kernel: gamma~_H^(2) from the anomalous-dimension algebra, ln H^(2) from the
# RGE, c_H numerics, n_f parts vs large-beta0 (Liu-Su), AD algebra identities and DGLAP consistency, gamma~_J^(2)
# (prop:yzliu-hard-kernel (c), prop:yzliu-ad-algebra, thm:yzliu-jet-continuation; VF-YZL-7, VF-YZL-9, VF-YZL-10)
# JHEP-2023 convention: mu d/dmu, alpha_s expansion, d alpha/dln mu = -beta0b alpha^2, beta0b = 11 C_A/(6pi) - n_f/(3pi)
# Inputs: Ji-Liu-Su App. A eqs. (A.1)-(A.5) (rendered pages 19-20 checked), T_F = 1/2 there.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

CF, CA, nf, al, L = sp.symbols('C_F C_A n_f alpha L_zeta')
z3, pi = sp.zeta(3), sp.pi
u = al**2/(16*pi**2)
Gcusp = al*CF/pi + al**2/pi**2*((sp.Rational(67, 36) - pi**2/12)*CA*CF - sp.Rational(5, 18)*CF*nf)       # (A.1)
gF = 3*al*CF/(4*pi) + u*((sp.Rational(49, 6) - 2*pi**2/3)*CA*CF - (sp.Rational(5, 2) - 8*pi**2/3)*CF**2 - sp.Rational(5, 3)*CF*nf)  # (A.2)
gV = -3*CF*al/(2*pi) + u*(CF*CA*(-sp.Rational(961, 27) - 11*pi**2/3 + 52*z3) + CF**2*(-3 + 4*pi**2 - 48*z3) + CF*nf*(sp.Rational(130, 27) + 2*pi**2/3))  # (A.3)
gs = u*(CF*CA*(sp.Rational(808, 27) - 11*pi**2/9 - 28*z3) + CF*nf*(-sp.Rational(112, 27) + 2*pi**2/9))     # (A.4)
gHL = -CF*al/(2*pi) + u*(CF*CA*(sp.Rational(110, 27) + pi**2/18 - 18*z3) + CF*nf*(sp.Rational(4, 27) + pi**2/9))  # (A.5)

gHH = sp.expand(2*gHL - gs)
gHH_ref = -al*CF/pi + al**2/pi**2*(CF*CA*(-sp.Rational(49, 36) + pi**2/12 - z3/2) + sp.Rational(5, 18)*CF*nf)
print('gamma_HH = 2 gHL - gs  ==  (A.6):', sp.simplify(gHH - gHH_ref) == 0)
gHt = sp.expand(gV + 2*gF + 2*gHL - gs)                                                                   # (A.11)
gHt2_ref = (1188*z3 - 99*pi**2 - 1108)/(432*pi**2)*CF*CA - (36*z3 + 6 - 7*pi**2)/(12*pi**2)*CF**2 + (sp.Rational(1, 24) + 10/(27*pi**2))*CF*nf
print('gamma~_H^(1) =', sp.simplify(gHt.coeff(al, 1)), ' ; (A.11) two-loop == (A.13):', sp.simplify(gHt.coeff(al, 2) - gHt2_ref) == 0)
gJt = sp.expand(2*gHL - 2*gs)                                                                              # (A.10)
gJt2_units = sp.expand(gJt.coeff(al, 2)*16*pi**2)
print('gamma~_J^(1) =', gJt.coeff(al, 1), ' ; gamma~_J^(2) in (alpha/4pi)^2 =', sp.simplify(gJt2_units))
assert sp.simplify(gJt2_units - (CF*CA*(-sp.Rational(1396, 27) + 23*pi**2/9 + 20*z3) + CF*nf*(sp.Rational(232, 27) - 2*pi**2/9))) == 0
gphi = -gV/2 - gs/2; gJthr = gV/2 - gs/2
print('DGLAP consistency 2 gphi + gH~ - gJ~ - 2 gF =', sp.simplify(2*gphi + gHt - gJt - 2*gF))
print('gamma_phi^(1) =', sp.simplify(gphi.coeff(al, 1)), ' (P_qq end point: 2 Gamma_cusp/(1-z)_+ + 2 gamma_phi delta(1-z) in d/dlnmu normalisation)')
print('gamma_V + gamma_phi - gamma_J^thr =', sp.simplify(gV + gphi - gJthr))
# PLB 811 eq. (26) value (wrong) vs (A.13): difference
a1 = 60*z3 - 19*pi**2/3 + sp.Rational(68, 27); a2 = -48*z3 + 28*pi**2/3 - 8; a3 = 2*pi**2/3 - sp.Rational(62, 27)
gC_PLB = (a1*CF*CA + a2*CF**2 + a3*CF*nf)/(16*pi**2)
d = sp.expand(gHt2_ref - gC_PLB)
print('(A.13) - PLB(26) =', sp.factor(d), ' ; -2 gamma_HH^(2)... check:', sp.simplify(d - (2*gHH_ref.coeff(al, 2) - CF*nf/(24*pi**2))))
# numerics for n_f = 4
print('gamma~_H^(2) numeric (SU(3), n_f=4): A.13 =', sp.N(gHt2_ref.subs({CF: sp.Rational(4, 3), CA: 3, nf: 4}), 6),
      ' PLB(26) =', sp.N(gC_PLB.subs({CF: sp.Rational(4, 3), CA: 3, nf: 4}), 6))

# ---- ln H to two loops from the RGE: d lnH/d ln mu = Gcusp L + gamma~_H, dL/dln mu = -2, d alpha/dln mu = -b alpha^2
b = sp.Symbol('beta0b')
c1 = CF/(2*pi)*(-2 + pi**2/12)
h1 = -CF/(4*pi)*L**2 + CF/(2*pi)*L + c1
A3, A2, A1, cH = sp.symbols('A3 A2 A1 c_H')
lnH = al*h1 + al**2*(A3*L**3 + A2*L**2 + A1*L + cH)
dlnH = sp.diff(lnH, al)*(-b*al**2) + sp.diff(lnH, L)*(-2)
rhs = Gcusp*L + al*(-CF/pi) + al**2*sp.Symbol('g2')
G2 = sp.Symbol('Gamma2')
rhs = (al*CF/pi + al**2*G2)*L - al*CF/pi + al**2*sp.Symbol('gH2')
eq = sp.expand(dlnH - rhs)
assert sp.simplify(eq.coeff(al, 1)) == 0
sol = sp.solve([eq.coeff(al, 2).coeff(L, k) for k in range(3)], [A3, A2, A1], dict=True)[0]
print('ln H^(2): A3 =', sp.simplify(sol[A3]), '; A2 =', sp.simplify(sol[A2]), '; A1 =', sp.simplify(sol[A1]))
gH2 = sp.Symbol('gH2')
assert sp.simplify(sol[A3] - CF*b/(24*pi)) == 0
assert sp.simplify(sol[A2] + (G2 + CF*b/(2*pi))/4) == 0
assert sp.simplify(sol[A1] + (CF*b/(4*pi)*(-2 + pi**2/12) + gH2/2)) == 0
print('VF-YZL-7 log structure reproduced')
# c_H closed form and numerics
cH_ref = ((241*z3/(144*pi**2) + 11*pi**2/320 - sp.Rational(559, 1728) - 971/(324*pi**2))*CF*CA
          + (-45*z3 - 2*pi**4 + 30*pi**2 - 30)/(24*pi**2)*CF**2 + (36*z3 + 51*pi**2 + 1312)/(1296*pi**2)*CF*nf*sp.Rational(1, 2)*2)
TF = sp.Symbol('T_F')
cH_ref = ((241*z3/(144*pi**2) + 11*pi**2/320 - sp.Rational(559, 1728) - 971/(324*pi**2))*CF*CA
          + (-45*z3 - 2*pi**4 + 30*pi**2 - 30)/(24*pi**2)*CF**2 + (36*z3 + 51*pi**2 + 1312)/(1296*pi**2)*CF*nf*TF)
print('c_H coefficients: C_F^2 %s ; C_F C_A %s ; C_F n_f T_F %s' % (
    sp.N(cH_ref.coeff(CF**2), 6), sp.N(sp.expand(cH_ref).coeff(CA).subs(CF, 1), 6), sp.N(sp.expand(cH_ref).coeff(nf).subs({CF: 1, TF: 1}), 6)))
# n_f parts vs Liu-Su JHEP 02 (2024) 204 eqs. (2.41)-(2.42) (large beta0, T_F=1/2)
print('n_f part of gamma~_H^(2): (1/24+10/(27pi^2)) - (80+9pi^2)/(216 pi^2) =',
      sp.simplify(sp.Rational(1, 24) + 10/(27*pi**2) - (80 + 9*pi**2)/(216*pi**2)))
print('n_f part of c_H (T_F=1/2) - (36z3+1312+51pi^2)/(2592pi^2) =',
      sp.simplify((36*z3 + 51*pi**2 + 1312)/(1296*pi**2)/2 - (36*z3 + 1312 + 51*pi**2)/(2592*pi**2)))
print('PASS')
