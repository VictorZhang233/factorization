import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 40
# antiquark region: q(x) = -qbar(-x) for x<0, qbar(s) = s^-0.5 (1-s)^5
q  = lambda x: -((-x)**mp.mpf(-0.5)*(1+x)**5)
dq = lambda x: mp.diff(q, x)
kpar = lambda y: y + (1-y)*mp.log(1-y) if y < 1 else mp.mpf(1)
def F(x):
    ax = abs(x)
    return mp.quad(lambda y: kpar(y)/y*q(x/y), [ax, (1+ax)/2, 1])
for x in [mp.mpf('-0.3'), mp.mpf('-0.6')]:
    ax = abs(x)
    x2F2 = x**2*mp.diff(F, x, 2)
    # [0,1]-plus: int_{|x|}^1 dy/y y^2/[1-y]_+ q(x/y) = int_{|x|}^1 dy (y q(x/y) - q(x))/(1-y) + q(x) ln(1-|x|)
    I = mp.quad(lambda y: (y*q(x/y) - q(x))/(1-y), [ax, (1+ax)/2, 1]) + q(x)*mp.log(1-ax)
    with_x   = I + q(x) - x*dq(x)
    with_abs = I + q(x) - ax*dq(x)
    print(f"x={float(x)}: x^2F''={mp.nstr(x2F2,15)}  [-x q']={mp.nstr(with_x,15)}  [-|x| q']={mp.nstr(with_abs,15)}")
