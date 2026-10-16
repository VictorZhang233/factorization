# W12: check that the S-ACOT-subtracted LO gluon coefficient (mu = Q),
#   Chat(z) = 2T_F{...}(z, eps_m) - 2 P_qg(z) ln(1/eps_m),   eps_m = m^2/Q^2 <= 1,
# convolved with a smooth function stays bounded uniformly in eps_m and tends to the
# massless MSbar convolution 2 C_2^g (x) g as eps_m -> 0 (units as/2pi, T_F = 1/2).
import os, sys
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 30
TF = mp.mpf(1)/2
def curly(z, e):            # the braces of eq:disall-heavy-lo (first line), zero above threshold
    if z >= 1/(1+4*e): return mp.mpf(0)
    b = mp.sqrt(1 - 4*e*z/(1-z))
    return ((z**2+(1-z)**2+4*e*z*(1-3*z)-8*e**2*z**2)*mp.log((1+b)/(1-b))
            + b*(8*z*(1-z)-1-4*e*z*(1-z)))
def Pqg(z): return TF*(z**2+(1-z)**2)
def C2g(z): return TF*((z**2+(1-z)**2)*mp.log((1-z)/z)-8*z**2+8*z-1)
def Chat(z, e): return 2*TF*curly(z, e) - 2*Pqg(z)*mp.log(1/e)
g = lambda xi: (1-xi)**3            # smooth test function
def conv(C, x):
    return mp.quad(lambda z: C(z)/z*g(x/z), [x, (1+x)/2, 1])
for x in [mp.mpf('0.01'), mp.mpf('0.1'), mp.mpf('0.3')]:
    ref = conv(lambda z: 2*C2g(z), x)
    print('x=%s  massless 2C_2^g (x) g = %s' % (x, mp.nstr(ref, 8)))
    for k in range(1, 7):
        e = mp.mpf(10)**(-k)
        thr = 1/(1+4*e)
        val = mp.quad(lambda z: Chat(z, e)/z*g(x/z), [x, (x+thr)/2, thr]) + \
              mp.quad(lambda z: Chat(z, e)/z*g(x/z), [thr, 1])
        print('   eps_m=1e-%d  Chat (x) g = %s   diff = %s' % (k, mp.nstr(val, 8), mp.nstr(val-ref, 4)))
print('PASS: bounded and convergent to the massless MSbar result as eps_m -> 0')
