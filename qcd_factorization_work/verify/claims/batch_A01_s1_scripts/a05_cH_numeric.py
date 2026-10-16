# A05(v): numerical values of the two-loop constant c_H of Ji-Liu-Su, JHEP 08 (2023) 037, eq. for c_H
# (coefficients of C_F C_A, C_F^2, C_F n_f T_F), and the n_f identity with Liu-Su (2.41)-(2.42) quoted in YZLIU.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
z3, pi = sp.zeta(3), sp.pi
cFA = 241*z3/(144*pi**2) + 11*pi**2/320 - sp.Rational(559, 1728) - 971/(324*pi**2)
cFF = (-45*z3 - 2*pi**4 + 30*pi**2 - 30)/(24*pi**2)
cFn = (36*z3 + 51*pi**2 + 1312)/(1296*pi**2)
print('c_H|CFCA  =', sp.N(cFA, 8), '(paper: -0.0840)')
print('c_H|CF^2  =', sp.N(cFF, 8), '(paper:  0.0725)')
print('c_H|CFnfTF=', sp.N(cFn, 8), '(paper:  0.1453)')
# YZLIU identity: (1/24 + 10/(27 pi^2)) = (80 + 9 pi^2)/(216 pi^2)
print('identity gamma_H nf:', sp.simplify(sp.Rational(1, 24) + 10/(27*pi**2) - (80 + 9*pi**2)/(216*pi**2)))
# N_m = C_F e^{5/6}/pi
print('N_m = C_F e^(5/6)/pi =', sp.N(sp.Rational(4, 3)*sp.exp(sp.Rational(5, 6))/pi, 6), '(paper: 0.977)')
