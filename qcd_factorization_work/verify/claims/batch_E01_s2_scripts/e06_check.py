# E06: (a) parton-momentum argument with a toy smooth coordinate kernel (exact numerics);
#      (b) O(alpha_s) change of the IJJSZ MSbar kernel when |y|P^z -> P^z.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import sympy as sp
mp.mp.dps = 20
mu, P = mp.mpf('0.7'), mp.mpf(2)
f = lambda y: (abs(y)**mp.mpf(0.6)*(1-abs(y))**3)*(1 if y > 0 else -0.3) if abs(y) < 1 else 0  # quark + small antiquark part
I = lambda lam: mp.quad(lambda y: mp.e**(1j*lam*y)*f(y), [-1, 0, 1])
# coordinate factorization with toy kernel  Ccoord(alpha, z^2 mu^2) = delta(1-alpha) exp(-z^2 mu^2),  z = lam/P
def qt_direct(x):
    g = lambda lam: (mp.e**(-1j*x*lam)*mp.e**(-(lam/P)**2*mu**2)*I(lam)).real/(2*mp.pi)
    return 2*mp.quad(g, [0, 5, 10, 20, 40])
# momentum kernel: C(xi, mu/p) = int dl/(2pi) e^{-i xi l} e^{i l} e^{-l^2 mu^2/p^2} = p/(2 mu sqrt(pi)) exp(-(1-xi)^2 p^2/(4 mu^2))
C = lambda xi, p: p/(2*mu*mp.sqrt(mp.pi))*mp.e**(-(1-xi)**2*p**2/(4*mu**2))
def qt_conv(x, parton=True):
    return mp.quad(lambda y: C(x/y, abs(y)*P if parton else P)*f(y)/abs(y), [-1, -0.5, 0, 0.2, 0.5, 1])
for x in [mp.mpf('0.3'), mp.mpf('0.6'), mp.mpf('-0.2')]:
    print("x=%s  direct FT=%s  conv with |y|P^z=%s  conv with P^z=%s" % (mp.nstr(x,2), mp.nstr(qt_direct(x),12), mp.nstr(qt_conv(x),12), mp.nstr(qt_conv(x,False),12)))
# (b) IJJSZ eq.(quasi-matching): mu-dependence only via -(1+xi^2)/(1-xi) ln(mu^2/(y^2P^2)) in [..]^{[0,1]}_{+(1)}
#     and +(3/2) ln(mu^2/(4y^2P^2)) delta(1-xi).  Replace yP -> P:  Delta C/a = -ln(y^2)[(1+xi^2)/(1-xi)]_+ + (3/2) ln(y^2) delta
xi, t = sp.symbols('xi t')
h = sp.Function('h')
# test-function action of [(1+xi^2)/(1-xi)]_+  minus  (1+xi^2)/(1-xi)_+  on h: should be (3/2) h(1)
expr = sp.integrate(sp.simplify(((1+t**2) - 2)/(1-t)), (t, 0, 1))
print("int_0^1 [(1+t^2)-2]/(1-t) dt =", expr, " => [(1+xi^2)/(1-xi)]_+ = (1+xi^2)/(1-xi)_+ + (3/2) delta(1-xi)")
print("hence Delta C = -2 a ln|y| (1+xi^2)/(1-xi)_+ theta(0<xi<1) = -(alpha_s/pi) ln|y| [P_qq(xi) - (3/2) C_F delta(1-xi)]")
