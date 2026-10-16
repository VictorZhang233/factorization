#!/usr/bin/env python3
"""
N04 (stage-2 verifier): elementary pieces of the moment-reduction argument (OTHERS Prop. 8.1).
 (a) one loop: the MS-bar renormalization constants of the local twist-2 quark operators are the Mellin moments of
     a distribution on [0,1] (existence of Z_OO at this order):  int_0^1 z^{N-1} [(1+z^2)/(1-z)]_+ dz
     = 3/2 + 1/(N(N+1)) - 2 S_1(N)  for all N (both parities)  -- derived here by sympy, not quoted;
 (b) uniqueness statements: on [-1,1] with ALL integer moments a compactly supported distribution is fixed
     (polynomials dense);  restricted to [0,1] with only odd (resp. even) powers, distributions supported at z=0
     can be invisible: delta(z) has zero odd moments, delta'(z) has zero even moments  (Muentz-Szasz is uniqueness
     only up to such terms; irrelevant for convolutions at x>0);
 (c) the generating-function step: for a compactly supported f, the Fourier transform is entire and its Taylor
     coefficients are the moments (H3 is exact for compact support) -- numerical illustration;
 (d) two parity sectors cannot share one [0,1] kernel once their anomalous dimensions differ (they do from two
     loops on, P^v_{q qbar} = O(alpha_s^2), MVV hep-ph/0403192): if Z^+ (even N) != Z^- (odd N) analytically,
     a single kernel on [0,1] is overdetermined -- illustrated with a toy pair of kernels.
Run: python3 -I n04_moment_reduction.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np
from scipy import integrate

PASS = FAIL = 0
def check(name, ok, info=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(("PASS " if ok else "FAIL ") + name + ("   " + info if info else ""))

z = sp.symbols('z', positive=True)
ok = True
for N in range(1, 11):
    # plus prescription: int_0^1 (1+z^2)/(1-z) (z^{N-1} - 1) dz
    val = sp.integrate(sp.cancel((1 + z**2) * (z**(N - 1) - 1) / (1 - z)), (z, 0, 1))
    S1 = sum(sp.Rational(1, k) for k in range(1, N + 1))
    ok &= sp.simplify(val - (sp.Rational(3, 2) + sp.Rational(1, N * (N + 1)) - 2 * S1)) == 0
check("(a) Mellin moments of [(1+z^2)/(1-z)]_+ = 3/2 + 1/(N(N+1)) - 2 S1(N), N=1..10 (one-loop Z^(N) are moments of a [0,1] distribution)", ok)
check("(a) N=1 moment vanishes (vector current conservation)", sp.Rational(3, 2) + sp.Rational(1, 2) - 2 == 0)

# (b) moments of delta(z) and delta'(z):  <delta, z^m> = 0^m ; <delta', z^m> = -m 0^{m-1}
def mom_delta(m): return 1 if m == 0 else 0
def mom_ddelta(m): return -1 if m == 1 else 0
odd = [mom_delta(m) for m in range(1, 20, 2)]
even = [mom_ddelta(m) for m in range(0, 20, 2)]
check("(b) delta(z) is invisible to all odd powers z^1, z^3, ... (C-even sector moments N even)", all(v == 0 for v in odd))
check("(b) delta'(z) is invisible to all even powers z^0, z^2, ... (C-odd sector moments N odd)", all(v == 0 for v in even))
check("(b) on [-1,1] with all powers both are visible (delta: m=0, delta': m=1)", mom_delta(0) != 0 and mom_ddelta(1) != 0)

# (c) generating function: F(l) = int_{-1}^1 e^{i x l} f(x) dx entire, Taylor coefficients = i^n/n! moments
f = lambda x: (1 - x**2)**2 * (1 + 0.3 * x) if abs(x) <= 1 else 0.0
moms = [integrate.quad(lambda x: x**n * f(x), -1, 1)[0] for n in range(40)]
for l in [0.7, 3.0, 9.0]:
    F = integrate.quad(lambda x: np.cos(x * l) * f(x), -1, 1)[0] + 1j * integrate.quad(lambda x: np.sin(x * l) * f(x), -1, 1)[0]
    T = sum((1j * l)**n / np.math.factorial(n) * moms[n] for n in range(40)) if hasattr(np, 'math') else None
    if T is None:
        import math
        T = sum((1j * l)**n / math.factorial(n) * moms[n] for n in range(40))
    check(f"(c) Taylor series of the Fourier transform with moment coefficients converges to it at lambda={l}", abs(F - T) < 1e-9, f"|diff|={abs(F-T):.1e}")

# (d) toy: Z+(N) = moments of g+(z)=2z on even N, Z-(N) = moments of g-(z)=1 on odd N; a single kernel on [0,1]
# with odd-N moments of g- is g- itself (Muentz uniqueness on (0,1]); its even moments differ from those of g+.
gp = lambda zz: 2 * zz; gm = lambda zz: 1.0
diffs = [integrate.quad(lambda zz: zz**(N - 1) * (gp(zz) - gm(zz)), 0, 1)[0] for N in range(2, 12, 2)]
check("(d) toy: two sectors with different kernels -> even moments of the odd-sector kernel do not reproduce Z+ (needs per-sector kernels or a [-1,1] kernel)",
      all(abs(d) > 1e-6 for d in diffs), str([round(d, 4) for d in diffs]))

print(f"\nSUMMARY n04: {PASS} PASS, {FAIL} FAIL")
