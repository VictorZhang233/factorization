import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 40
# r1-term of A_3^i with asymptotic DAs (integrand as in the project script): 12 x ybar / (y (1 - x ybar))
def I_dbl(delta):
    d = mp.mpf(delta)
    # analytic x-integral over [0, 1-d], then y over [d, 1]
    f = lambda y: -(1-d)/y - mp.log(y + d*(1-y))/(y*(1-y))
    return 12*mp.quad(f, [d, 10*d, 100*d, 1e-3, 0.5, 1])
def I_dbl_direct(delta):
    d = mp.mpf(delta)
    g = lambda x, y: 12*x*(1-y)/(y*(1-x*(1-y)))
    return mp.quad(g, [0, 0.5, 1-1000*d, 1-d], [d, 1000*d, 0.5, 1])
for delta in ['1e-4', '1e-6', '1e-8']:
    d = mp.mpf(delta); XA = mp.log(1/d)
    bn = 6*(XA**2 - 2*XA + mp.pi**2/3)
    v = I_dbl(d)
    print('delta', delta, 'X_A', mp.nstr(XA, 8), 'I_dbl', mp.nstr(v, 15), 'BN', mp.nstr(bn, 15), 'shift', mp.nstr(v-bn, 12), ' (-pi^2 =', mp.nstr(-mp.pi**2, 8), ')')
print('direct 2D (delta=1e-4):', mp.nstr(I_dbl_direct('1e-4'), 12))
