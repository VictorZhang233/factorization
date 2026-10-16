# Reviewer r3_2: check the O15 parametric form of the 0<x<P part of the fibered triangle Gamma, and the sliver part.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 20
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c1_triangle_id import setup, rho_Gamma, cov_Gamma

def fib_part(s, lo, hi):
    eps = s['eps']
    g = mp.gamma(eps)*mp.gamma(1-eps)
    # kappa-integral in closed form K2 for 1/((P k + al1)(c k + b)) = 1/(P c (k+al)(k+be))
    P, Pp, m2, Qt2 = s['P'], s['Pp'], s['m2'], s['Qt2']
    def inner(x):
        u = x/P; e2 = m2 + 2*Pp*x
        c = 1 + e2/(Qt2*(1-u)); b = e2*(1 + m2/Qt2)
        al = x*m2*(1-u)/P; be = b/c
        return g*(al**(-eps) - be**(-eps))/((be - al)*P*c)
    return mp.quad(inner, [lo, (lo+hi)/2, hi])/mp.gamma(1-eps)

def O15(s):
    eps, m2, Qt2 = s['eps'], s['m2'], s['Qt2']
    f = lambda u: mp.quad(lambda y: (1-u)**(-eps)*(m2*(1-y+y*u) + (1-y)*Qt2*u)**(-1-eps), [0, 1])
    return mp.gamma(1+eps)*(Qt2/(Qt2+m2))*mp.quad(f, [0, mp.mpf('0.5'), 1])

for (P, Pp, m2, eps) in [(0.8, 1.3, 0.1, 0.3), (0.5, 0.9, 0.02, 0.15)]:
    s = setup(P, Pp, m2, eps)
    a = s['m2']/s['Pp']
    main = fib_part(s, mp.mpf(0), s['P'])
    o15 = O15(s)
    # sliver by 2D quadrature
    eps_ = s['eps']
    sl = mp.quad(lambda x: mp.quad(lambda k: k**(-eps_)*rho_Gamma(s, x, k), [0, 1, mp.inf]), [-a/2, 0])/mp.gamma(1-eps_)
    cov = cov_Gamma(s)
    print(f"P={P},P'={Pp},m2={m2},eps={eps}: fibered(0<x<P) = {mp.nstr(main,15)}  O15 form = {mp.nstr(o15,15)}  rel = {mp.nstr(abs(main/o15-1),3)}")
    print(f"     sliver = {mp.nstr(sl,15)}; total fibered = {mp.nstr(main+sl,15)}; covariant = {mp.nstr(cov,15)}; rel = {mp.nstr(abs((main+sl)/cov-1),3)}")
