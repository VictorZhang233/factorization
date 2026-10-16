#!/usr/bin/env python3
"""s5: numerical illustrations of three elementary lemmas formulated in LAMET.md
 (L1) Fourier lemma: if r(lambda) = int_{-1}^{1} dalpha e^{i alpha lambda} rho(alpha), then at fixed P^z
      FT_lambda[ (lambda/P^z)^2 r(lambda) ](x) = -(1/P_z^2) rho''(x)  for x in (0,1)     [z = -lambda/P^z]
      => relative enhancement rho''/rho ~ a(a-1)/x^2 (x->0), b(b-1)/(1-x)^2 (x->1) for rho ~ x^a (1-x)^b.
 (L2) Domain of the one-loop MSbar momentum-space matching: the convolution int dy/|y| C(x/y) q(y) converges
      iff int_0 |q(y)| dy < infinity  (MSbar tail C ~ -3/(2|xi|));  ratio/hybrid tail ~ xi^{-2} -> needs int_0 |y q(y)| dy < inf.
 (L3) Analyticity strip: |h(lambda)| <= A e^{-m|lambda|/P^z}  =>  q~(x) analytic for |Im x| < m/P^z (illustrated by
      the exact transform of a pure exponential).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import mpmath as mp
from scipy import integrate

PASS = 0; FAIL = 0
def check(name, ok):
    global PASS, FAIL
    print(("PASS " if ok else "FAIL ") + name)
    if ok: PASS += 1
    else: FAIL += 1

# ---------- L1 ----------
mp.mp.dps = 25
a, b = mp.mpf('3.5'), mp.mpf('4.5')
B = mp.beta(a + 1, b + 1)
rho = lambda x: x**a * (1 - x)**b / B
rho2 = lambda x: mp.diff(rho, x, 2)
def r(lam):   # int_0^1 e^{i alpha lam} rho(alpha) dalpha = 1F1(a+1; a+b+2; i lam)
    return mp.hyp1f1(a + 1, a + b + 2, 1j * lam)
def ft_lam2r(x):
    # int dlam/(2pi) e^{-i x lam} lam^2 r(lam); integrand ~ lam^{2-(a+1)} = lam^{-1.5} at large lam (absolutely convergent)
    f = lambda lam: (mp.e**(-1j * x * lam) * lam**2 * r(lam)).real / mp.pi   # combine +/- lam (real part, even)
    return mp.quadosc(f, [0, mp.inf], omega=max(x, 1 - x) if x != 0.5 else 0.5)
for x in (mp.mpf('0.3'), mp.mpf('0.5'), mp.mpf('0.7')):
    lhs = ft_lam2r(x)
    rhs = -rho2(x)
    print("   x=%s : FT[lambda^2 r] = %s ,  -rho''(x) = %s" % (x, mp.nstr(lhs, 12), mp.nstr(rhs, 12)))
    check("L1 Fourier lemma at x=%s" % x, abs(lhs - rhs) < 1e-6 * max(1, abs(rhs)))
# enhancement factors
for xs, expect in ((mp.mpf('1e-4'), a * (a - 1)), (1 - mp.mpf('1e-4'), b * (b - 1))):
    ratio = rho2(xs) / rho(xs) * (xs**2 if xs < 0.5 else (1 - xs)**2)
    check("L1 endpoint enhancement rho''/rho -> %s / (endpoint distance)^2 (found %s)" % (mp.nstr(expect, 4), mp.nstr(ratio, 6)),
          abs(ratio - expect) < 2e-3 * expect)

# ---------- L2 ----------
def ms_tail(xi):     # leading large-|xi| behaviour of the one-loop MSbar kernel (coefficient of a)
    return -1.5 / abs(xi)
def ratio_tail(xi):
    return -4.0 / (3.0 * xi**2) * np.sign(xi)
x = 2.0   # a point outside the support, where only the tail region |x/y| large matters as y->0
for delta in (-0.5, 0.0, 0.3):
    q = lambda y: y**(-1 - delta) if y > 0 else 0.0     # small-y behaviour y^{-1-delta}
    def conv(tail, ymin):
        return integrate.quad(lambda lt: tail(x / np.exp(lt)) * q(np.exp(lt)), np.log(ymin), np.log(0.1), limit=800)[0]
    ms = [conv(ms_tail, 10.0**(-k)) for k in (8, 12, 16)]
    ra = [conv(ratio_tail, 10.0**(-k)) for k in (8, 12, 16)]
    ms_conv = abs(ms[2] - ms[1]) < 1e-3 * (1 + abs(ms[1]))
    ra_conv = abs(ra[2] - ra[1]) < 1e-3 * (1 + abs(ra[1]))
    print("   q ~ y^{-1-(%.1f)}: MSbar partial convolutions %s ; ratio %s" % (delta, ["%.4g" % v for v in ms], ["%.4g" % v for v in ra]))
    check("L2 MSbar convolution converges iff delta<0 (delta=%.1f -> %s)" % (delta, ms_conv), ms_conv == (delta < 0))
    check("L2 ratio-scheme convolution converges for delta<1 (delta=%.1f -> %s)" % (delta, ra_conv), ra_conv)

# ---------- L3 ----------
# h(lambda) = e^{-m|lambda|/P}: q~(x) = int dl/2pi e^{-i x l} h = (m/P)/(pi((m/P)^2 + x^2)): poles at x = +- i m/P
m, P = 0.5, 2.0
qt = lambda x: (m / P) / (np.pi * ((m / P)**2 + x**2))
num = integrate.quad(lambda l: np.cos(0.37 * l) * np.exp(-m * abs(l) / P), -np.inf, np.inf)[0] / (2 * np.pi)
check("L3 exact transform of e^{-m|lambda|/P} = Lorentzian with poles at +-i m/P (num %.10f vs %.10f)" % (num, qt(0.37)),
      abs(num - qt(0.37)) < 1e-9)

print("\nSUMMARY s5: %d PASS, %d FAIL" % (PASS, FAIL))
