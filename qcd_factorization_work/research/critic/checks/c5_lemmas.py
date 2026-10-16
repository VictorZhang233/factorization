# (a) Moments O(1/Q^2) for every fixed n do NOT imply pointwise O(1/Q^2): R(x)=sin(Q^2 x) on [0,1].
# (b) Even moments do not determine a distribution with support at x=0: delta'(x) has all even moments 0.
# (c) Continuation in n is not unique without growth bounds: sin(pi n) vanishes on all integers (type pi),
#     (1-cos(pi n))/2 vanishes on even integers -> the +/- (even/odd) continuations can differ (P_NS^+ != P_NS^-).
import sys,os; sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp, sympy as sp
mp.mp.dps=25
xx,kk=sp.symbols('x k',positive=True)
closed={n:sp.lambdify(kk,sp.integrate(xx**n*sp.sin(kk*xx),(xx,0,1)),'mpmath') for n in (0,2,4)}  # exact antiderivatives
for Q2 in [10**2,10**4,10**6,10**8]:
    mom=[closed[n](mp.mpf(Q2)) for n in (0,2,4)]
    print(f"Q^2={Q2:.0e}: Q^2*moments(n=0,2,4) = {[mp.nstr(Q2*m,5) for m in mom]} (bounded)  but sup|R| = 1")
x,m=sp.symbols('x m',positive=True)
# <delta', x^(2m)> = -d/dx x^(2m) at 0 :
vals=[-sp.diff(x**(2*k),x).subs(x,0) for k in range(0,6)]
print("even moments of delta'(x):",vals,"; first odd moment:",-sp.diff(x,x).subs(x,0))
print("sin(pi n) at n=0..5:",[sp.sin(sp.pi*k) for k in range(6)],"; (1-cos(pi n))/2 at even n:",[(1-sp.cos(sp.pi*k))/2 for k in range(0,10,2)])
