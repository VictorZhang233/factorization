# N12: C_H at larger eps, cancellation-safe evaluation.  Write the C_H bracket as an iterated difference:
#   g(a,b) = [(1+a+b)^s - (1+b)^s] - [(1+a)^s - 1],  s = -1+2eps
# and integrate the inner b-integral first in closed-form-free numerics with the tail map, at higher precision.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
A_ = lambda e: mp.gamma(1+e)*mp.gamma(1-e)**2/(e**2*mp.gamma(1-2*e))
for dps in (20, 40):
    mp.mp.dps = dps
    e = mp.mpf('0.45'); s = -1 + 2*e
    Qt2 = mp.mpf('2.08')
    def bracket(a, b):
        # use expm1/log1p forms to avoid cancellation
        t1 = (1+b)**s*mp.expm1(s*mp.log1p(a/(1+b)))   # (1+a+b)^s - (1+b)^s
        t2 = mp.expm1(s*mp.log1p(a))                    # (1+a)^s - 1
        return t1 - t2
    def f(a, b):
        return bracket(a, b)*(a*b*Qt2)**(-1-e)
    def mapped(seg):
        if seg == 0: return lambda y: (y, mp.mpf(1))
        return lambda y: (y**(-1/e), y**(-1/e-1)/e)
    tot = 0
    for sa in (0, 1):
        for sb in (0, 1):
            ma, mb = mapped(sa), mapped(sb)
            tot += mp.quad(lambda y, z: f(ma(y)[0], mb(z)[0])*ma(y)[1]*mb(z)[1], [0, mp.mpf('0.5'), 1], [0, mp.mpf('0.5'), 1])
    ch = mp.gamma(1+e)*tot
    ex = (1/Qt2)**e*A_(e)/Qt2
    print("dps=%d eps=0.45: C_H num %s  exact %s  rel.diff %s" % (dps, mp.nstr(ch, 16), mp.nstr(ex, 16), mp.nstr(ch/ex-1, 3)))
