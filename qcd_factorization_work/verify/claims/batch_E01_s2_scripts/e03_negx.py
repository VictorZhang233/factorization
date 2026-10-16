# x<0 check of the BVZ braces: is it "+q - |x| q'" (as printed in (61)) or "+q - x q'"?
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 30
qf = lambda u: (-u)**mp.mpf(0.5)*(1+u)**3 if u < 0 else u**mp.mpf(-0.5)*(1-u)**3   # model, antiquark part for u<0
def F(xx):
    k = lambda yy: yy + (1-yy)*mp.log(1-yy)
    return mp.quad(lambda yy: k(yy)*qf(xx/yy)/yy, [abs(xx), 1])
for xx in [mp.mpf('-0.3'), mp.mpf('-0.6')]:
    lhs = xx**2*mp.diff(F, xx, 2)
    q0 = qf(xx); qp = mp.diff(qf, xx)
    plus = mp.quad(lambda yy: (yy*qf(xx/yy) - q0)/(1-yy), [abs(xx), 1]) + q0*mp.log(1-abs(xx))
    print("x=%s  x^2F''=%s   braces(-|x|q')=%s   braces(-x q')=%s" % (mp.nstr(xx,2), mp.nstr(lhs,12), mp.nstr(plus + q0 - abs(xx)*qp, 12), mp.nstr(plus + q0 - xx*qp, 12)))
