# R-ratio O(a^2) coefficient (a = alpha_s/pi, MSbar, mu^2 = s) and Bjorken sum rule O(a^2) coefficient;
# check of the (generalized) Crewther relation  C_Bjp(a) * D_NS(a) = 1 + (beta(a)/a) K(a),
# with mu^2 da/dmu^2 = beta(a) = -(beta0/4) a^2 + ..., beta0 = 11 - 2 n_f/3  (CONTEXT normalization).
import sys,os; sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
a,nf=sp.symbols('a n_f'); z3=sp.zeta(3)
d2=sp.Rational(365,24)-11*z3-nf*(sp.Rational(11,12)-sp.Rational(2,3)*z3)   # R = R0 (1 + a + d2 a^2 + ...)
c2=-(sp.Rational(55,12)-nf/3)                                              # C_Bjp = 1 - a + c2 a^2 + ...
print("d2 =",sp.nsimplify(d2),"  numerically:",[sp.N(d2.subs(nf,k),6) for k in (3,4,5)], " ~ 1.9857 - 0.1153 n_f:",sp.N(d2.subs(nf,0),6),sp.N(-sp.diff(d2,nf),6))
print("c2 (n_f=3) =",sp.N(c2.subs(nf,3),6))
prod=sp.expand(sp.series((1+a+d2*a**2)*(1-a+c2*a**2),a,0,3).removeO())
beta0=11-sp.Rational(2,3)*nf
k2=sp.simplify(prod.coeff(a,2)/beta0)
print("C*D = 1 +",sp.simplify(prod.coeff(a,1)),"a + beta0*(",sp.simplify(k2),") a^2   [n_f-independent ratio => Crewther-consistent]")
K1=sp.simplify(-4*k2); CF=sp.Rational(4,3)
print("K_1 =",K1," ; compare C_F(-21/8+3 zeta3) =",sp.simplify(CF*(-sp.Rational(21,8)+3*z3)), " equal:",sp.simplify(K1-CF*(-sp.Rational(21,8)+3*z3))==0)
