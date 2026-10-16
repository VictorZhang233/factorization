#!/usr/bin/env python3
"""E21 (stage 2): small-tau behaviour of the integrands of Mankiewicz-Piller eq. (10), hep-ph/9905287v1.

Printed (read from rhot7.tex, numbering checked):
  (3)  Phi(t) = 1/2 [ tb int_0^t du phi(u)/ub - t int_t^1 du phi(u)/u ]
  (4)  gv(t)  = 1/2 [    int_0^t du phi(u)/ub +   int_t^1 du phi(u)/u ]
  (5)  ga(t)  = 2   [ tb int_0^t du phi(u)/ub + t int_t^1 du phi(u)/u ]
  (10) I1 = int_0^1 dt/t ( 4 gv - 2 Phi/t + ga/(2 t tb) ),   I2 = int_0^1 dt/t ( 2 gv + ga/(2 t tb) )
  text: "For ... phi = 6 t tb the integrands in eq.(10) are proportional to 12/t and 9/t, respectively."
Method (different from stage 1's exact sympy): eqs. (3)-(5) are evaluated by adaptive numerical quadrature
(mpmath, 30 digits) exactly as printed, for several DAs; the coefficient of 1/t is extracted by Richardson
extrapolation of t*integrand(t) as t -> 0; compared with the analytic law derived by hand:
  t->0:  gv -> gv(0) = sigma/2,  ga -> 2 sigma t,  Phi -> -sigma t/2,   sigma = int_0^1 phi(u)/u du
  => integrand(I1) ~ 4 sigma/t = 8 gv(0)/t,   integrand(I2) ~ 2 sigma/t = 4 gv(0)/t.
Run: python3 -I e21_mp_s2.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 30
PASS = []
def check(name, ok, info=''):
    PASS.append(bool(ok)); print(('PASS ' if ok else 'FAIL ') + name + ('  ' + info if info else ''))

def C32(z): return mp.mpf(3)/2*(5*z**2 - 1)               # Gegenbauer C_2^{3/2}
def C34(z): return mp.mpf(15)/8*(21*z**4 - 14*z**2 + 1)   # Gegenbauer C_4^{3/2}
DAs = {
    'asymptotic 6 t tb':           lambda u: 6*u*(1-u),
    'a2=0.2':                      lambda u: 6*u*(1-u)*(1 + mp.mpf('0.2')*C32(2*u-1)),
    'a2=-0.1, a4=0.15':            lambda u: 6*u*(1-u)*(1 - mp.mpf('0.1')*C32(2*u-1) + mp.mpf('0.15')*C34(2*u-1)),
    'endpoint-suppressed 30t^2tb^2': lambda u: 30*u**2*(1-u)**2,
}
def funcs(phi):
    def gv(t):  return (mp.quad(lambda u: phi(u)/(1-u), [0, t]) + mp.quad(lambda u: phi(u)/u, [t, 1]))/2
    def ga(t):  return 2*((1-t)*mp.quad(lambda u: phi(u)/(1-u), [0, t]) + t*mp.quad(lambda u: phi(u)/u, [t, 1]))
    def Phi(t): return ((1-t)*mp.quad(lambda u: phi(u)/(1-u), [0, t]) - t*mp.quad(lambda u: phi(u)/u, [t, 1]))/2
    def i1(t):  return (4*gv(t) - 2*Phi(t)/t + ga(t)/(2*t*(1-t)))/t
    def i2(t):  return (2*gv(t) + ga(t)/(2*t*(1-t)))/t
    return gv, ga, Phi, i1, i2
def coeff_1_over_t(f):
    # t f(t) = c + c1 t + c2 t^2 + ... ; Richardson on t = h, h/2, h/4
    h = mp.mpf('1e-4')
    a = [k*f(k) for k in (h, h/2, h/4)]
    r1 = [2*a[1] - a[0], 2*a[2] - a[1]]
    return (4*r1[1] - r1[0])/3

for name, phi in DAs.items():
    gv, ga, Phi, i1, i2 = funcs(phi)
    sigma = mp.quad(lambda u: phi(u)/u, [0, 1])
    c1, c2 = coeff_1_over_t(i1), coeff_1_over_t(i2)
    print(f'{name:32s} sigma={mp.nstr(sigma,10):>12s} gv(0)={mp.nstr(gv(mp.mpf("1e-12")),10):>12s}  '
          f'coef(I1)={mp.nstr(c1,10):>12s} coef(I2)={mp.nstr(c2,10):>12s}  ratio={mp.nstr(c1/c2,8)}')
    check(f'[{name}] integrand(I1) ~ 4 sigma/t = 8 gv(0)/t', abs(c1 - 4*sigma) < mp.mpf('1e-8')*abs(sigma))
    check(f'[{name}] integrand(I2) ~ 2 sigma/t = 4 gv(0)/t', abs(c2 - 2*sigma) < mp.mpf('1e-8')*abs(sigma))
    if name.startswith('asymptotic'):
        check('asymptotic DA: coefficients are 12 and 6 (not 12 and 9)', abs(c1 - 12) < 1e-8 and abs(c2 - 6) < 1e-8)
        # pointwise closed forms (exact polynomials) for the asymptotic DA, checked at random points
        ok = True
        for t in (mp.mpf('0.013'), mp.mpf('0.37'), mp.mpf('0.81')):
            ok &= abs(i1(t) - (12/t - 21 + 18*t)) < 1e-20 and abs(i2(t) - (6/t - 6 + 6*t)) < 1e-20
            ok &= abs(gv(t) - mp.mpf(3)/2*(t**2 + (1-t)**2)) < 1e-20 and abs(ga(t) - 6*t*(1-t)) < 1e-20
            ok &= abs(Phi(t) - mp.mpf(3)/2*t*(1-t)*(2*t - 1)) < 1e-20
        check('asymptotic DA: integrands are exactly 12/t - 21 + 18t and 6/t - 6 + 6t; gv, ga, Phi closed forms', ok)
        # what would give 9: 4 gv in I2, or ga/(t tb) in I2
        alt_a = coeff_1_over_t(lambda t: (4*gv(t) + ga(t)/(2*t*(1-t)))/t)
        alt_b = coeff_1_over_t(lambda t: (2*gv(t) + ga(t)/(t*(1-t)))/t)
        print(f'   variants giving 9: I2 with 4gv -> {mp.nstr(alt_a,10)}; I2 with ga/(t tb) -> {mp.nstr(alt_b,10)}')
        check('a "9/t" requires a different I2 than printed (e.g. 4gv, or ga/(t tb))', abs(alt_a - 9) < 1e-8 and abs(alt_b - 9) < 1e-8)
print(f'\nSUMMARY: {sum(PASS)}/{len(PASS)} PASS')
