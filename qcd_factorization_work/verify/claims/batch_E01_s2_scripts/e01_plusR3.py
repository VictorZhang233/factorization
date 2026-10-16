# plus-on-R and printed pairings with Lorentzian test functions; cancellation-free phi differences
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 25
def G_pw(u, lS): return -1/abs(u) + 2*mp.si(u*lS)/(mp.pi*u)
def phi(u, R, u0): return R**2/(R**2+(u-u0)**2)
def dphi_sym(u, R, u0):
    # phi(u)+phi(-u)-2phi(0), computed without cancellation
    D0 = R**2+u0**2
    return R**2*(u*(2*u0-u)/((R**2+(u-u0)**2)*D0) - u*(2*u0+u)/((R**2+(u+u0)**2)*D0))
def exact_pair(R, u0, lS):
    w = mp.mpc(R, -u0); return 2*R*mp.re(mp.e1(w*lS)/w)
def tail_int(p0, lS, Ue):
    x = lS*Ue
    c2 = mp.cos(x)/x - (mp.pi/2 - mp.si(x))
    # next term (4p0/pi) int_x^inf sin t/t^3 dt = O(x^-3) at x = n pi: dropped
    return (4*p0/(mp.pi*lS))*lS*c2
def plusR_pair(R, u0, lS, U=2000):
    p0 = phi(0, R, u0)
    f = lambda u: G_pw(u, lS)*dphi_sym(u, R, u0)
    n = int(U*lS/mp.pi)+1
    pts = [mp.mpf(0)] + [k*mp.pi/lS for k in range(1, n+1)]
    return mp.quad(f, pts) + tail_int(p0, lS, pts[-1])
def printed_pair(R, u0, lS):
    p0 = phi(0, R, u0)
    A = mp.quad(lambda u: dphi_sym(u, R, u0)/u, [0, 1]) + mp.quad(lambda u: (phi(u, R, u0)+phi(-u, R, u0))/u, [1, 10, 100, mp.inf])
    B = mp.quad(lambda u: 2*mp.si(u*lS)/(mp.pi*u)*(phi(u, R, u0)+phi(-u, R, u0)), [0, 1, 10, 100, 1000, mp.inf])
    return -A + B
rows = []
for (R, u0, lS) in [(1, 0, 1), (2, 0.7, 0.5), (0.5, -1.3, 3.7), (3, 2.0, 2.0), (1, 0, 0.2), (0.7, 0.4, 1.0)]:
    R, u0, lS = mp.mpf(R), mp.mpf(u0), mp.mpf(lS)
    ex = exact_pair(R, u0, lS); pl = plusR_pair(R, u0, lS); pr = printed_pair(R, u0, lS)
    pred = 2*mp.log(lS*mp.e**mp.euler)*phi(0, R, u0)
    print("R=%s u0=%s lS=%s | exact=%s | plusR-exact=%s | (printed-exact)/[2ln(lS e^gE)phi(0)]=%s" % (
        mp.nstr(R,3), mp.nstr(u0,3), mp.nstr(lS,3), mp.nstr(ex, 14), mp.nstr(pl-ex, 3), mp.nstr((pr-ex)/pred, 13)))
