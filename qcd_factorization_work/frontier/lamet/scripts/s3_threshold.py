#!/usr/bin/env python3
"""s3: one-loop check of the threshold factorization of the quasi-PDF matching kernel
(Ji-Liu-Su, JHEP 08 (2023) 037; Liu-Su JHEP 02 (2024) 204):
   in coordinate space, at large |lambda| (lambda = z p^z, fixed p^z):
   e^{i lambda} Gtilde(lambda) = 1 + a [ H1 + Jf1 ] + O(ln|lambda|/|lambda|),
   H1  = -2 + pi^2/12 - L_z^2/2 + L_z                         (heavy-light Sudakov hard kernel, real part)
   Jf1 = l_z^2/2 + l_z + pi^2/12 + 2 + i sign(lambda) pi (L_z - 1)   (space-like jet fn incl. phase)
   l_z = ln(e^{2gE} mu^2 z^2/4) = 2 ln|lambda| + 2 gE - L_z,   L_z = ln(4 p_z^2/mu^2),  a = alpha_s C_F/(2pi).
Exact one-loop MSbar (gamma^t):  Gtilde(lambda) = int_0^1 dalpha C(alpha, l_z) e^{-i alpha lambda},
   C = delta(1-alpha) 3/2 (l_z+1) - (l_z+1)[(1+alpha^2)/(1-alpha)]_+ - [4 ln(1-alpha)/(1-alpha)]_+ + 2(1-alpha).
All alpha-integrals are evaluated in closed form (Ci, Si) plus convergent Fourier tails (QAWF), so that
lambda up to 1e5 is reachable; the residual must scale like ln(lambda)/lambda."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from scipy import integrate, special

gE = np.euler_gamma
PASS = 0; FAIL = 0

def tail_logu_over_u(lam):
    """T(lam) = int_1^inf ln(u)/u e^{i u lam} du  (lam>0), via QAWF"""
    f = lambda u: np.log(u) / u
    c, _ = integrate.quad(f, 1, np.inf, weight='cos', wvar=lam, limlst=200)
    s, _ = integrate.quad(f, 1, np.inf, weight='sin', wvar=lam, limlst=200)
    return c + 1j * s

def exact_shifted(lam, Lz):
    """returns e^{i lam} Gtilde(lam) (one-loop coefficient) for lam>0"""
    lz = 2 * np.log(lam) + 2 * gE - Lz
    si, ci = special.sici(lam)
    E0 = ci - gE - np.log(lam) + 1j * si                       # int_0^1 (e^{iu lam}-1)/u du
    # int_0^1 (u-2)(e^{iu lam}-1) du
    iu = lambda k: integrate.quad(lambda u: u**k * np.cos(lam * u), 0, 1, weight=None, limit=2000)[0] \
        + 1j * integrate.quad(lambda u: u**k * np.sin(lam * u), 0, 1, limit=2000)[0]
    # closed forms: int_0^1 e^{iu lam} du = (e^{i lam}-1)/(i lam); int_0^1 u e^{iu lam} du = e^{i lam}/(i lam) + (e^{i lam}-1)/lam^2
    J0 = (np.exp(1j * lam) - 1) / (1j * lam)
    J1 = np.exp(1j * lam) / (1j * lam) + (np.exp(1j * lam) - 1) / lam**2
    E1 = (J1 - 0.5) - 2 * (J0 - 1)
    I1s = 2 * E0 + E1                                           # e^{i lam} I1
    # F = int_0^1 ln(u)(e^{iu lam}-1)/u du = 1/2 (Lc+gE)^2 + pi^2/12 - T(lam),  Lc = ln(-i lam) = ln lam - i pi/2
    Lc = np.log(lam) - 1j * np.pi / 2
    F = 0.5 * (Lc + gE)**2 + np.pi**2 / 12 - tail_logu_over_u(lam)
    I2s = F                                                     # e^{i lam} I2 with ln(1-alpha)=ln u
    # int_0^1 2(1-alpha) e^{-i alpha lam} = 2 int_0^1 u e^{-i(1-u) lam} du => e^{i lam}*I3 = 2 J1
    I3s = 2 * J1
    return 1.5 * (lz + 1) - (lz + 1) * I1s - 4 * I2s + I3s

def predicted(lam, Lz):
    lz = 2 * np.log(abs(lam)) + 2 * gE - Lz
    H1 = -2 + np.pi**2 / 12 - Lz**2 / 2 + Lz
    Jf1 = lz**2 / 2 + lz + np.pi**2 / 12 + 2 + 1j * np.sign(lam) * np.pi * (Lz - 1)
    return H1 + Jf1

# cross-check exact_shifted against brute-force quadrature at moderate lambda
def brute(lam, Lz):
    lz = 2 * np.log(lam) + 2 * gE - Lz
    ez = np.exp(-1j * lam)
    def cq(f):
        r = integrate.quad(lambda a: f(a).real, 0, 1, limit=4000, epsabs=1e-13)[0]
        i = integrate.quad(lambda a: f(a).imag, 0, 1, limit=4000, epsabs=1e-13)[0]
        return r + 1j * i
    I1 = cq(lambda al: (1 + al**2) / (1 - al) * (np.exp(-1j * al * lam) - ez) if al < 1 else 0j)
    I2 = cq(lambda al: np.log(1 - al) / (1 - al) * (np.exp(-1j * al * lam) - ez) if al < 1 else 0j)
    I3 = cq(lambda al: 2 * (1 - al) * np.exp(-1j * al * lam))
    return (1.5 * (lz + 1) * ez - (lz + 1) * I1 - 4 * I2 + I3) * np.exp(1j * lam)

for lam in (7.3, 31.0):
    b = brute(lam, 0.4); e = exact_shifted(lam, 0.4)
    ok = abs(b - e) < 1e-8
    print(("PASS" if ok else "FAIL") + " closed-form vs brute-force at lambda=%.1f: %s vs %s" % (lam, b, e))
    PASS += ok; FAIL += (not ok)

for Lz in (0.0, 1.3, -0.8):
    rows = []
    for lam in (1e2, 1e3, 1e4, 1e5):
        d = exact_shifted(lam, Lz) - predicted(lam, Lz)
        rows.append((lam, d))
        print("Lz=%5.2f lambda=%8.0e  exact-pred = %+.3e %+.3ej   |d|*lambda/ln(lambda) = %.3f"
              % (Lz, lam, d.real, d.imag, abs(d) * lam / np.log(lam)))
    ok = all(abs(d) * lam / np.log(lam) < 10 for lam, d in rows) and abs(rows[-1][1]) < 1e-3
    print(("PASS" if ok else "FAIL") + " threshold factorization at one loop, Lz=%.2f (residual O(ln lam/lam))" % Lz)
    PASS += ok; FAIL += (not ok)

# lambda<0: e^{i lambda} Gtilde(lambda) is the complex conjugate structure; Gtilde(-lam) = conj(Gtilde(lam)) for real kernel
d = np.conj(exact_shifted(1e5, 0.7)) - predicted(-1e5, 0.7)
ok = abs(d) < 1e-3
print(("PASS" if ok else "FAIL") + " lambda<0 phase sign: |d| = %.2e" % abs(d))
PASS += ok; FAIL += (not ok)

# momentum space singular terms near xi -> 1 (MSbar, gamma^t), residual must vanish like (1-xi) ln(1-xi)
for eps in (1e-4, 1e-6, 1e-8):
    xv = 1 + eps
    g1 = (1 + xv**2) / (1 - xv) * np.log(xv / (xv - 1)) + 1
    pred = np.log((1 - xv)**2) / abs(1 - xv)
    r1 = abs((g1 - pred) * eps)
    xv = 1 - eps; Lz = 0.9
    g2 = (1 + xv**2) / (1 - xv) * (Lz + np.log(xv * (1 - xv))) - xv * (1 + xv) / (1 - xv)
    pred2 = np.log((1 - xv)**2) / abs(1 - xv) + (Lz - 1) * (1 / (1 - xv) + 1 / abs(1 - xv))
    r2 = abs((g2 - pred2) * eps)
    ok = r1 < 50 * eps * abs(np.log(eps)) and r2 < 50 * eps * abs(np.log(eps))
    print(("PASS" if ok else "FAIL") + " momentum-space (1-xi)^{-1} terms, |1-xi|=%.0e: residual*(|1-xi|) = %.2e, %.2e" % (eps, r1, r2))
    PASS += ok; FAIL += (not ok)

print("\nSUMMARY s3: %d PASS, %d FAIL" % (PASS, FAIL))
