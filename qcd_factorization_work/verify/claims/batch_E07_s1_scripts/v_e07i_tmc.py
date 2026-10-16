import sys,os; sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
from math import comb
mp.mp.dps = 30
# test PDF supported in [0,1] (quark-only, valence-like), normalised arbitrarily
a_, b_ = mp.mpf('0.5'), mp.mpf('3')
def q(x):
    x = mp.mpf(x)
    if x <= 0 or x >= 1: return mp.mpf(0)
    return x**a_*(1-x)**b_
def mom(f, n, lo, hi):   # int x^{n-1} f(x) dx
    return mp.quad(lambda x: x**(n-1)*f(x), [lo, 0, hi] if lo < 0 < hi else [lo, hi])
for c in [mp.mpf('0.05'), mp.mpf('0.25')]:          # c = mu = M^2/(4 Pz^2)
    K = lambda n: sum(comb(n-i, i)*c**i for i in range(n//2+1))   # exact moment ratio K_n (Chen eq.23 / Alexandrou eq.4)
    # ---- Alexandrou et al. PRD92 eq.(11): qt(x) = q0(xi)/(1+mu xi^2), xi = 2x/(1+sqrt(1+4 mu x^2))
    def qt_A(x):
        x = mp.mpf(x); xi = 2*x/(1+mp.sqrt(1+4*c*x**2)); return q(xi)/(1+c*xi**2)
    # x-range: xi in (0,1) <-> x in (0, 1/(1-c))
    xmaxA = 1/(1-c)
    # ---- Chen et al. NPB911 eq.(61): qt(x) = [f+/2 q(2x/f+) - f-/2 q(-2x/f-)]/sqrt(1+4c)
    fp, fm = mp.sqrt(1+4*c)+1, mp.sqrt(1+4*c)-1
    def qt_C(x):
        x = mp.mpf(x); return (fp/2*q(2*x/fp) - fm/2*q(-2*x/fm))/mp.sqrt(1+4*c)
    print('c =', c)
    for n in [1, 2, 3, 4]:
        exact = K(n)*mom(q, n, 0, 1)
        A = mom(qt_A, n, 0, xmaxA)
        C = mom(qt_C, n, -fm/2, fp/2)
        print('  n=%d  K_n*<x^{n-1}>_q = %s   Alexandrou(11): %s   Chen(61): %s' % (n, mp.nstr(exact, 12), mp.nstr(A, 12), mp.nstr(C, 12)))
    # Alexandrou: int qt dx = int dxi q0(xi)/(1-mu xi^2)^2 = sum_m (m+1) mu^m <x^{2m}>
    alt = mp.quad(lambda xi: q(xi)/(1-c*xi**2)**2, [0, 1])
    print('  Alexandrou norm via change of variables: int q0/(1-mu xi^2)^2 =', mp.nstr(alt, 12), '  vs  int q0 =', mp.nstr(mom(q, 1, 0, 1), 12))
