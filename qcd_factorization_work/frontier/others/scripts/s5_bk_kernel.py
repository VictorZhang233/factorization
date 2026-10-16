#!/usr/bin/env python3
"""
s5_bk_kernel.py -- check of the LO Balitsky-Kovchegov kernel as transcribed in OTHERS.md.

LO BK (dipole S-matrix S_xy = tr[U_x U_y^dagger]/Nc, rapidity Y, abar = alpha_s Nc/pi):
  dS_xy/dY = (abar/2pi) Int d^2z  (x-y)^2/[(x-z)^2 (z-y)^2]  [ S_xz S_zy - S_xy ].
Linearised (N = 1 - S):  dN_xy/dY = (abar/2pi) Int d^2z K [ N_xz + N_zy - N_xy ]  (+ O(N^2)).
On N = ((x-y)^2)^gamma the linear kernel has eigenvalue abar * chi(gamma),
  chi(gamma) = 2 psi(1) - psi(gamma) - psi(1-gamma)   (LO BFKL characteristic function).
We check this numerically for several gamma in (0,1); chi(1/2) = 4 ln 2.
Run: python3 -I s5_bk_kernel.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from scipy.integrate import quad
from scipy.special import digamma

PASS = FAIL = 0
def check(name, ok, info=""):
    global PASS, FAIL
    if ok: PASS += 1
    else:  FAIL += 1
    print(("[PASS] " if ok else "[FAIL] ") + name + ("  " + info if info else ""))

def chi_num(g):
    # x = (0,0), y = (1,0); by the x<->y reflection symmetry integrate over Re z < 1/2 and double.
    def radial(theta):
        c, s = np.cos(theta), np.sin(theta)
        def f(r):
            d2 = (r * c - 1.0)**2 + (r * s)**2          # |z - y|^2
            return (r**(2 * g) + d2**g - 1.0) / (r * d2)  # (1/(r^2 d2)) [..] * r  (polar measure)
        if c > 1e-14:
            R = 0.5 / c
            return quad(f, 0, R, limit=400, epsabs=1e-12, epsrel=1e-11)[0]
        val1 = quad(f, 0, 1, limit=400, epsabs=1e-12, epsrel=1e-11)[0]
        val2 = quad(lambda t: f(1.0 / t) / t**2, 0, 1, limit=400, epsabs=1e-12, epsrel=1e-11)[0]
        return val1 + val2
    tot = quad(radial, 0, 2 * np.pi, limit=400, epsabs=1e-10, epsrel=1e-10, points=[np.pi / 2, 3 * np.pi / 2])[0]
    return 2.0 * tot / (2 * np.pi)

chi = lambda g: 2 * digamma(1.0) - digamma(g) - digamma(1.0 - g)
for g in [0.5, 0.3, 0.7, 0.15]:
    cn, ce = chi_num(g), chi(g)
    check(f"linearised LO BK kernel eigenvalue on (x-y)^(2 gamma), gamma={g}: chi_num = chi(gamma)",
          abs(cn - ce) < 1e-6 * max(1, abs(ce)), f"num={cn:.9f}  exact={ce:.9f}")
check("chi(1/2) = 4 ln 2 (BFKL intercept omega_P = abar 4 ln 2)", abs(chi(0.5) - 4 * np.log(2)) < 1e-13)
print(f"\nTOTAL: {PASS} PASS, {FAIL} FAIL")
