import sys,os; sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
CF,CA,nf=sp.symbols('C_F C_A n_f'); z3=sp.zeta(3); pi=sp.pi
u=1/(16*pi**2)   # (alpha_s/4pi)^2 in units of alpha_s^2
gV = u*(CF*CA*(-sp.Rational(961,27)-11*pi**2/3+52*z3) + CF**2*(-3+4*pi**2-48*z3) + CF*nf*(sp.Rational(130,27)+2*pi**2/3))
gF = u*(CA*CF*(sp.Rational(49,6)-2*pi**2/3) - CF**2*(sp.Rational(5,2)-8*pi**2/3) - sp.Rational(5,3)*CF*nf)
gHL= u*(CF*CA*(sp.Rational(110,27)+pi**2/18-18*z3) + CF*nf*(sp.Rational(4,27)+pi**2/9))
gs = u*(CF*CA*(sp.Rational(808,27)-11*pi**2/9-28*z3) + CF*nf*(-sp.Rational(112,27)+2*pi**2/9))
GS = sp.expand(2*gHL-gs)
GS_A6 = (CF*CA*(-sp.Rational(49,36)+pi**2/12-z3/2) + sp.Rational(5,18)*CF*nf)/pi**2
print('2 gHL - gs - (A.6) =', sp.simplify(GS-GS_A6))
gH = sp.expand(gV+2*gF+2*gHL-gs)
gH_A13 = (1188*z3-99*pi**2-1108)/(432*pi**2)*CF*CA - (36*z3+6-7*pi**2)/(12*pi**2)*CF**2 + (sp.Rational(1,24)+10/(27*pi**2))*CF*nf
print('(A.11) - (A.13) =', sp.simplify(gH-gH_A13))
# PLB eq.(26) gamma_C^(2)
a1=60*z3-19*pi**2/3+sp.Rational(68,27); a2=-48*z3+28*pi**2/3-8; a3=2*pi**2/3-sp.Rational(62,27)
gC_PLB=(a1*CF*CA+a2*CF**2+a3*CF*nf)/(16*pi**2)
d=sp.expand(gH_A13-gC_PLB)
print('JHEP2023(A.13) - PLB2020(26) =', sp.nsimplify(sp.simplify(d)))
de=sp.expand(d)
print('   numerically: CA:',sp.N(de.coeff(CA).subs(CF,1)),' CF^2:',sp.N(de.coeff(CF**2)),' nf:',sp.N(de.coeff(nf).subs(CF,1)))
GSe=sp.expand(2*GS_A6)
print('   compare +2*gamma_HH^(2) [A.6 two-loop]: CA:',sp.N(GSe.coeff(CA).subs(CF,1)),' nf:',sp.N(GSe.coeff(nf).subs(CF,1)), ' => (A.13)-(PLB 26) = 2*gamma_HH^(2) - CF*nf/(24 pi^2): PLB used the wrong sign of the two-loop Gamma_S plus an extra nf term')
# what PLB would get with GS sign flipped:
print('PLB(26) + 2*GS(A.6) - A.13 =', sp.simplify(gC_PLB + 2*GS_A6 - gH_A13))
print('PLB(26) - 2*GS(A.6) - A.13 =', sp.simplify(gC_PLB - 2*GS_A6 - gH_A13))
