import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp, mpmath as mp
# 1) exact change of variables (coordinate -> momentum), symbolic check of the argument
lam, lamp, y, x, P, mu, alpha = sp.symbols('lambda lambdap y x P mu alpha', positive=True)
Ccoord = sp.Function('Cc')
integrand = sp.exp(-sp.I*x*lam)*sp.exp(sp.I*alpha*y*lam)*Ccoord(alpha, mu**2*lam**2/P**2)
sub = integrand.subs(lam, lamp/y)*(1/y)     # d lambda = d lambda'/|y| (y>0)
print("after lambda'=y*lambda:", sp.simplify(sub))
# 2) mu/p^z dependence of the one-loop MSbar kernel (IJJSZ): physical region term
#    a{ [ (1+xi^2)/(1-xi) (-l_p + ...) ]_+^{[0,1]} + delta(1-xi)(3/2 l_p + 5/2) },  l_p = ln(mu^2/(4 p_z^2))
#    difference p_z=|y|P vs p_z=P:  Delta l = -2 ln|y|
#    Delta C = 2 a ln|y| [ (1+xi^2)/(1-xi) ]_+  - 3 a ln|y| delta(1-xi) = 2 a ln|y| (1+xi^2)/(1-xi)_+
# verify the last identity on test functions: int_0^1 [g]_+ h - (3/2) h(1) == int_0^1 (1+xi^2)(h-h(1))/(1-xi)
xi = sp.symbols('xi')
for h in [xi**2, sp.exp(xi), 1/(1+xi)]:
    lhs = sp.integrate(sp.simplify((1+xi**2)/(1-xi)*(h - h.subs(xi,1))), (xi,0,1)) - sp.Rational(3,2)*h.subs(xi,1) + sp.Rational(3,2)*h.subs(xi,1)
    # [(1+xi^2)/(1-xi)]_+ (total-integral-zero plus) paired with h equals int (1+xi^2)/(1-xi) (h-h(1))
    plus_pair = sp.integrate(sp.simplify((1+xi**2)/(1-xi)*(h - h.subs(xi,1))), (xi,0,1))
    # (1+xi^2)/(1-xi)_+ paired with h = int ((1+xi^2) h - 2 h(1))/(1-xi)
    std_pair = sp.integrate(sp.simplify(((1+xi**2)*h - 2*h.subs(xi,1))/(1-xi)), (xi,0,1))
    print("h=",h,": [ ]_+ - (3/2)delta  vs (1+xi^2)/(1-xi)_+ :", sp.N(plus_pair - sp.Rational(3,2)*h.subs(xi,1) - std_pair, 15))
# 3) size of the O(alpha_s) difference for a model PDF
mp.mp.dps = 30
f = lambda t: t**mp.mpf(-0.5)*(1-t)**3
aS, CF = mp.mpf('0.3'), mp.mpf(4)/3
def dq(xx):
    # (alpha_s C_F/pi) int_x^1 dy/y ln y (1+xi^2)/(1-xi)_+ f(y), xi=x/y; plus at xi=1 <-> y=x
    # write as integral over xi in [x,1]: dy/y = dxi/xi, y = x/xi
    g = lambda s: mp.log(xx/s)*f(xx/s)/s
    val = mp.quad(lambda s: ((1+s**2)*g(s) - 2*g(1))/(1-s), [xx, 1]) - 2*g(1)*mp.log(1/(1-xx)) * 0
    # plus distribution on [0,1] in xi, but g(s)=0 for s<x (y>1): add -2 g(1) int_0^x ds/(1-s) = 2 g(1) ln(1-x)
    val += 2*g(1)*mp.log(1-xx)
    return aS*CF/mp.pi*val
for xx in [mp.mpf('0.3'), mp.mpf('0.5'), mp.mpf('0.7')]:
    print(f"x={float(xx)}: Delta qtilde / f = {mp.nstr(dq(xx)/f(xx),6)}")
