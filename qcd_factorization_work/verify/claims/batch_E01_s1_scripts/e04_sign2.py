import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 30
# one-loop quasi-PDF (units of a), unphysical region xi>1, diagram decomposition (LAMET 4.6(b), consistent conventions)
def parts(xi):
    qv = mp.quad(lambda y: (1-y)/abs(xi-y), [0, 1])
    qs = mp.quad(lambda y: (xi+y)/abs(xi-y), [0, 1])/(1-xi)
    qt = -1/abs(1-xi)
    return qv, qs, qt
target = lambda xi: (1+xi**2)/(1-xi)*mp.log(xi/(xi-1)) + 1
for xi in [mp.mpf('1.5'), mp.mpf(3), mp.mpf(10), mp.mpf(100)]:
    qv, qs, qt = parts(xi)
    print(f"xi={float(xi)}: consistent={mp.nstr(qv+qs+qt,12)} target={mp.nstr(target(xi),12)} | sail-flipped={mp.nstr(qv-qs+qt,12)}  xi*flipped={mp.nstr(xi*(qv-qs+qt),8)}  xi*consistent={mp.nstr(xi*(qv+qs+qt),8)}")
