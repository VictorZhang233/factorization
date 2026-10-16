# W17 / Ch14 -- s03: distributional limit of the regulated Wilson-line graphs as delta -> 0, delta^2 = e^{2y_B}kT^2/(2p+^2),
#  F_b -> 2x[1/(1-x)]_+ + delta(1-x) ln(1/delta^2)  (time-like s=+1, and space-like s=-1 with principal value),
#  F_c(s=+1) -> -delta(1-x);  and the b-space vanishing of the remainder (FT = 2 pi^2/(Lambda_B b) -> 0).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 30
ok = True
def check(name, cond):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name); ok &= bool(cond)

def Fb(x, d, s):
    return 2*x*(1 - x)/((1 - x)**2 + s*d*d)
def Fc(x, d, s):
    return -2*s*d*d*(1 - x)/((1 - x)**2 + s*d*d)**2

# closed forms of the x integrals
for d in [mp.mpf('1e-2'), mp.mpf('1e-3')]:
    I_t = mp.quad(lambda x: Fb(x, d, 1), [0, 1 - d, 1])
    cf_t = mp.log(1 + d**-2) + 2*d*mp.atan(1/d) - 2
    check('int F_b(time-like) closed form, delta=%s' % mp.nstr(d, 2), abs(I_t - cf_t) < mp.mpf('1e-20'))
    # principal value for space-like: pole at x = 1-d ; PV via symmetric excision
    eta = mp.mpf('1e-12')
    f = lambda x: Fb(x, d, -1)
    I_s = mp.quad(f, [0, 1 - d - d/2, 1 - d - eta]) + mp.quad(f, [1 - d + eta, 1 - d + d/2, 1])
    # analytic: ln(1-d^2) - ln d^2 - 2 - d ln((1-d)/(1+d))
    cf_s = mp.log(1 - d*d) - mp.log(d*d) - 2 - d*mp.log((1 - d)/(1 + d))
    check('PV int F_b(space-like) closed form, delta=%s' % mp.nstr(d, 2), abs(I_s - cf_s) < 1e-8)
    I_c = mp.quad(lambda x: Fc(x, d, 1), [0, 1 - d, 1])
    check('int F_c(time-like) = -1/(1+delta^2)', abs(I_c + 1/(1 + d*d)) < mp.mpf('1e-20'))

# distributional limit against test functions h
tests = {'h=1': lambda x: 1, 'h=x^2': lambda x: x**2, 'h=e^x': lambda x: mp.e**x, 'h=sqrt(x)': lambda x: mp.sqrt(x)}
for name, h in tests.items():
    for d in [mp.mpf('1e-3'), mp.mpf('1e-4')]:
        lhs = mp.quad(lambda x: Fb(x, d, 1)*h(x), [0, 1 - 10*d, 1 - d, 1])
        plus = mp.quad(lambda x: (2*x*h(x) - 2*h(1))/(1 - x), [0, 1])      # <2x[1/(1-x)]_+, h>
        rhs = plus + h(1)*mp.log(1/d**2)
        err = abs(lhs - rhs)
        check('F_b -> 2x[1/(1-x)]_+ + delta(1-x) ln(1/delta^2) [%s, delta=%s] err=%s' % (name, mp.nstr(d, 1), mp.nstr(err, 3)), err < 20*d)
        lc = mp.quad(lambda x: Fc(x, d, 1)*h(x), [0, 1 - 10*d, 1 - d, 1])
        check('F_c(s=+1) -> -delta(1-x) [%s, delta=%s]' % (name, mp.nstr(d, 1)), abs(lc + h(1)) < 20*d)

# remainder of the delta(1-x) part, D(kappa) = ln(1+kappa^2) + 2 kappa arctan(1/kappa), kappa = kT/Lambda_B
check('exact-minus-limit = D(kappa)', abs((mp.log(1 + mp.mpf('0.01')**-2) + 2*mp.mpf('0.01')*mp.atan(100) - 2) - (-2 + mp.log(1/mp.mpf('0.01')**2)) - (mp.log(1 + mp.mpf('0.0001')) + 2*mp.mpf('0.01')*mp.atan(100))) < 1e-25)
# 2D Fourier transform of D(k/Lambda)/k^2 :  2 pi int_0^inf dkappa/kappa J0(kappa z) D(kappa),  z = Lambda b ; claim -> 2 pi^2/z
def ftD(z):
    f = lambda kap: mp.besselj(0, kap*z)*(mp.log(1 + kap**2) + 2*kap*mp.atan(1/kap))/kap
    return 2*mp.pi*mp.quadosc(f, [0, mp.inf], omega=z)
for z in [20, 200]:
    v = ftD(mp.mpf(z))
    check('FT of remainder = 2 pi^2/(Lambda_B b) at z=%d (ratio %s)' % (z, mp.nstr(v*z/(2*mp.pi**2), 10)), abs(v*z/(2*mp.pi**2) - 1) < 1e-6)
print('ALL PASS' if ok else 'SOME FAIL')
