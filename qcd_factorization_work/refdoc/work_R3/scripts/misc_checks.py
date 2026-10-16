# Small checks of refdoc pp.63-70 numbers
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
x,y,c,eps,Y,yA,yB,yn,a,cc = sp.symbols('x y c epsilon Y y_A y_B y_n a c', real=True)
CF, NC = sp.Rational(4,3), 3
# (11.6): gamma_n^(0) and exponent for n=2, nf=3
def gam(n): return CF*(1 - sp.Rational(2,(n+1)*(n+2)) + 4*sum(sp.Rational(1,m) for m in range(2,n+2)))
b0 = 11 - sp.Rational(2,3)*3
print("gamma_0 =", gam(0), "; gamma_2/beta0 =", gam(2)/b0, "(refdoc: 50/81)", "; gamma_4/beta0 =", gam(4)/b0)
# (11.3)-(11.4): Q^2 F_pi with asymptotic DA
phi = 6*x*(1-x)
I = sp.integrate(phi/(1-x),(x,0,1))
alpha, f = sp.symbols('alpha_s f_pi', positive=True)
Q2F = 16*sp.pi*CF*alpha/(8*NC)*f**2*I**2
print("int phi/xbar =", I, "; Q^2F_pi =", sp.simplify(Q2F), "; numeric (alpha=0.35, f=0.1304 GeV):", float(Q2F.subs({alpha:0.35,f:0.1304})), "GeV^2")
# Fig 44(c): area of {xbar*ybar < c} in unit square
u,v = sp.symbols('u v', positive=True)
area = c + sp.integrate(c/u,(u,c,1))
print("area{u v<c} =", sp.simplify(area), " (~ c ln(1/c) for small c)")
# Prop 10.4 algebra: ln S(y1,y2)= a + (y1-y2) c ; (1/2)[lnS(L,yn)-lnS(L,yB)-lnS(yn,yB)] with L -> +inf placeholder
L = sp.symbols('L')
lnS = lambda y1,y2: a + (y1-y2)*cc
expr = sp.Rational(1,2)*(lnS(L,yn)-lnS(L,yB)-lnS(yn,yB))
print("(1/2)[...] =", sp.expand(expr), "  d/dyn =", sp.diff(expr,yn))
# (10.8) consistency: d/dlnQ of exponent equals gamma(Q) + K(b;Q) given dK/dlnmu=-gK (one-loop fixed coupling test)
lnQ, lnmub, t = sp.symbols('lnQ lnmu_b t', real=True)
g0, gK0, K0 = sp.symbols('g0 gK0 K0')   # constant gamma, gamma_K (fixed coupling) and K(b;mu_b)
expo = (lnQ-lnmub)*K0 + sp.integrate(g0 - (lnQ - t)*gK0, (t, lnmub, lnQ))
lhs = sp.diff(expo, lnQ); KQ = K0 - gK0*(lnQ-lnmub)
print("d(exponent)/dlnQ - [gamma + K(b;Q)] =", sp.simplify(lhs - (g0 + KQ)))
# zeta_A zeta_B = Q^4
xA,xB,MA,MB,yPA,yPB = sp.symbols('x_A x_B M_A M_B y_PA y_PB', positive=True)
zA = (xA*MA)**2*sp.exp(2*(yPA-yn)); zB = (xB*MB)**2*sp.exp(2*(yn-yPB))
s_ = MA*MB*sp.exp(yPA-yPB)   # s = 2 P_A^+ P_B^- for massive hadrons along +-z (leading in M^2/s)
print("zeta_A zeta_B / (x_A x_B s)^2 =", sp.simplify(zA*zB/(xA*xB*s_)**2))
