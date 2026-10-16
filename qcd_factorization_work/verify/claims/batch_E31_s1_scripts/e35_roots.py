import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 30
MQ, MP, MS = mp.mpf('0.3'), mp.mpf('1.0'), mp.mpf('1.5')
def Dl(x): return x*MS**2 + (1-x)*MQ**2 - x*(1-x)*MP**2
def br(x, m): return mp.log(m**2/Dl(x)) - 1 + (MQ + x*MP)**2/Dl(x)
def bis(f, a, b):
    fa = f(a)
    for _ in range(200):
        c = (a+b)/2; fc = f(c)
        if (fc < 0) == (fa < 0): a, fa = c, fc
        else: b = c
    return (a+b)/2
for m in ['0.3', '0.5', '0.8', '1.0', '1.2', '1.5', '1.69', '1.7', '2.5']:
    m = mp.mpf(m); n = 4000
    xs = [mp.mpf(i)/n for i in range(1, n)]
    s = [br(x, m) < 0 for x in xs]
    roots = []
    for i in range(1, len(xs)):
        if s[i] != s[i-1]: roots.append(bis(lambda x: br(x, m), xs[i-1], xs[i]))
    print(f"mu={mp.nstr(m,4)}: sign at xi=0.001: {'-' if s[0] else '+'}, sign changes at xi = {[mp.nstr(r,5) for r in roots]}, sign at xi=0.99975: {'-' if s[-1] else '+'}")
