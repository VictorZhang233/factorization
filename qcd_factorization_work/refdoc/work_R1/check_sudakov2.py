import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 40
def I_exact(t):
    # Q^2 I = 2 * int_0^{1/2} du ln(a/t)/(a-t), a=u(1-u); substitute u = exp(-s) near 0 to tame the log endpoint
    def g(u):
        a = u*(1-u)
        d = a - t
        if abs(d) < mp.mpf(10)**(-30):
            return 1/t
        return mp.log(a/t)/d
    u0 = mp.mpf(1)/2 - mp.sqrt(mp.mpf(1)/4 - t)   # a = t here (removable point)
    # pieces: [0,u0] via u = u0*exp(-s), s in [0,inf); [u0,1/2] direct
    p1 = mp.quad(lambda s: g(u0*mp.e**(-s))*u0*mp.e**(-s), [0, 1, 5, 20, mp.inf])
    p2 = mp.quad(g, [u0, 2*u0, 10*u0, mp.mpf(1)/2])
    return 2*(p1+p2)
for t in ['1e-2','1e-4','1e-6','1e-8','1e-10']:
    t = mp.mpf(t); v = I_exact(t); L = mp.log(1/t)
    print(f"t={mp.nstr(t,3):>7}  Q^2 I={mp.nstr(v,18):>24}  ln^2+pi^2/3={mp.nstr(L**2+mp.pi**2/3,18):>24}  (diff)/(t ln^2 t)={mp.nstr((v-L**2-mp.pi**2/3)/(t*L**2),8)}")
