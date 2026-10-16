import sys,os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 40
for e in [mp.mpf('0.3'), mp.mpf('0.7'), mp.mpf('0.9')]:
    p = 1/(1-e)
    # I1 = int_0^{1/2} v^{-1-e}((1-v)^{-e}-1) dv, v = s^p
    def f1(s):
        v = s**p
        return v**(-1-e)*mp.expm1(-e*mp.log1p(-v))*p*s**(p-1)
    I1 = mp.quad(f1, [0, mp.mpf('0.5')**(1/p)], maxdegree=12)
    def g(w):
        u = w**p
        return (1-u)**(-1-e)*(1 - u/w)/(1-e)
    I2 = mp.quad(g, [0, mp.mpf('0.5')**(1-e)], maxdegree=12)
    J = I1 + I2 - 1/e
    print(mp.nstr(e,3), mp.nstr(J, 25), mp.nstr(mp.gamma(-e)*mp.gamma(1-e)/mp.gamma(1-2*e), 25))
