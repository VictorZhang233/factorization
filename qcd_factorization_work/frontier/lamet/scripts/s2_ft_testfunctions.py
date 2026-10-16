#!/usr/bin/env python3
"""s2: distributional check of momentum-space one-loop quasi-PDF matching kernels against the Fourier
transform of the coordinate-space (pseudo/ITD) kernels, using Gaussian test functions.

  <C, phi> = int dxi C(xi) phi(xi)        (momentum-space formula as printed in the literature)
  must equal
  int dzeta/(2pi) G(zeta) Phi(zeta),  G(zeta) = int_0^1 dalpha Ccoord(alpha, L(zeta)) e^{-i alpha zeta},
  Phi(zeta) = int dxi phi(xi) e^{i xi zeta},  L(zeta) = ln(zeta^2) + ell + 2 gamma_E,  ell = ln(mu^2/(4 p_z^2)).

Schemes: MSbar (IJJSZ eq. quasi-matching), ratio (IJJSZ eq. quasi-matching-alt), hybrid
(Ji et al. NPB 964 (2021) eq. hybridm2 with their 1/|1-xi|_+ definition  vs  Su et al. NPB 991 (2023)
form with [..]_+ over the whole real line).  gamma^t (sigma=0) and gamma^z (sigma=1).
All kernels are the O(a) coefficient, a = alpha_s C_F/(2 pi).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from scipy import integrate, special

gE = np.euler_gamma
PASS = 0; FAIL = 0
def check(name, a, b, tol=2e-6):
    global PASS, FAIL
    ok = abs(a - b) <= tol * max(1.0, abs(a), abs(b))
    print(("PASS " if ok else "FAIL ") + name + ":  momentum=%.10f  coord-FT=%.10f  diff=%.2e" % (a, b, a - b))
    if ok: PASS += 1
    else: FAIL += 1
    return ok

def quad(f, a, b, **kw):
    v, e = integrate.quad(f, a, b, limit=400, epsabs=1e-12, epsrel=1e-11, **kw)
    return v

# ---------------- coordinate-space side ----------------
def G(zeta, ell, sigma, scheme, lamS=None):
    """one-loop coordinate kernel convolved with e^{-i alpha zeta}; returns complex"""
    L = np.log(zeta**2) + ell + 2 * gE
    ez = np.exp(-1j * zeta)
    def re_im(fun):
        r = quad(lambda al: fun(al).real, 0, 1)
        i = quad(lambda al: fun(al).imag, 0, 1)
        return r + 1j * i
    I1 = re_im(lambda al: (1 + al**2) / (1 - al) * (np.exp(-1j * al * zeta) - ez) if al < 1 else 0j)
    I2 = re_im(lambda al: np.log(1 - al) / (1 - al) * (np.exp(-1j * al * zeta) - ez) if al < 1 else 0j)
    I3 = re_im(lambda al: 2 * (1 - al) * np.exp(-1j * al * zeta))
    if scheme == 'msbar':
        return 1.5 * (L + 1) * ez - (L + 1) * I1 - 4 * I2 + (1 + sigma) * I3
    # ratio: delta coefficient -(1+sigma); [2(1-al)]_+ (1+sigma)
    Gr = -(L + 1) * I1 - 4 * I2 + (1 + sigma) * (I3 - ez)
    if scheme == 'ratio':
        return Gr
    if scheme == 'hybrid':
        extra = 1.5 * np.log(zeta**2 / lamS**2) * ez if abs(zeta) > lamS else 0j
        return Gr + extra
    raise ValueError

def coord_pairing(xi0, s, ell, sigma, scheme, lamS=None):
    Phi = lambda z: np.sqrt(2 * np.pi) * s * np.exp(1j * xi0 * z - 0.5 * s**2 * z**2)
    Z = 12.0 / s
    f = lambda z: (G(z, ell, sigma, scheme, lamS) * Phi(z)).real / (2 * np.pi)
    pts = [-lamS, lamS] if (scheme == 'hybrid') else None
    # integrand is real-even in combination; integrate over (-Z,0) and (0,Z)
    if pts:
        segs = [(-Z, -lamS), (-lamS, 0), (0, lamS), (lamS, Z)]
    else:
        segs = [(-Z, 0), (0, Z)]
    return sum(quad(f, a, b) for a, b in segs)

# ---------------- momentum-space side ----------------
def g1(x):  # xi>1, inside plus
    return (1 + x**2) / (1 - x) * np.log(x / (x - 1)) + 1
def g2(x, ell):  # 0<xi<1
    return (1 + x**2) / (1 - x) * (-ell + np.log(x * (1 - x))) - x * (1 + x) / (1 - x)
def g3(x):  # xi<0
    return -(1 + x**2) / (1 - x) * np.log(-x / (1 - x)) - 1

def mom_pairing(phi, ell, sigma, scheme, lamS=None, hybrid_form='su'):
    p1 = phi(1.0)
    tot = 0.0
    if scheme == 'msbar':
        # xi>1: [g1 + 3/(2xi)]_+ - 3/(2xi)
        tot += quad(lambda x: (g1(x) + 1.5 / x) * (phi(x) - p1), 1, 2) \
             + quad(lambda x: (g1(x) + 1.5 / x) * (phi(x) - p1), 2, np.inf)
        tot += -quad(lambda x: 1.5 / x * phi(x), 1, np.inf)
        tot += quad(lambda x: g2(x, ell) * (phi(x) - p1), 0, 1)
        tot += quad(lambda x: (g3(x) + 1.5 / (1 - x)) * (phi(x) - p1), -np.inf, 0)
        tot += -quad(lambda x: 1.5 / (1 - x) * phi(x), -np.inf, 0)
        tot += (1.5 * ell + 2.5) * p1
        if sigma == 1:   # Delta C = 2(1-xi) theta(0<xi<1) (not plus)
            tot += quad(lambda x: 2 * (1 - x) * phi(x), 0, 1)
        return tot
    # ratio scheme (IJJSZ quasi-matching-alt)
    r1 = lambda x: g1(x) - 1.5 / (1 - x)
    r2 = lambda x: (1 + x**2) / (1 - x) * (-ell + np.log(x * (1 - x)) - 1) + 1 + 1.5 / (1 - x)
    r3 = lambda x: g3(x) + 1.5 / (1 - x)
    tot += quad(lambda x: r1(x) * (phi(x) - p1), 1, 2) + quad(lambda x: r1(x) * (phi(x) - p1), 2, np.inf)
    tot += quad(lambda x: r2(x) * (phi(x) - p1), 0, 1)
    tot += quad(lambda x: r3(x) * (phi(x) - p1), -np.inf, 0)
    if sigma == 1:
        tot += quad(lambda x: 2 * (1 - x) * (phi(x) - p1), 0, 1)
    if scheme == 'ratio':
        return tot
    # hybrid extra: 3/2 * [ -1/|u| + 2 Si(u lamS)/(pi u) ] , u = xi-1
    h = lambda u: -1.0 / abs(u) + 2 * special.sici(u * lamS)[0] / (np.pi * u)
    if hybrid_form == 'su':      # plus over the whole real line
        # int h(u)[phi(1+u)-phi(1)] = int_{|u|<1} h (phi-p1) + int_{|u|>1} h phi - p1 * int_{|u|>1} h,
        # with int_{|u|>1} h(u) du = 2[ ln lamS + gamma_E - (2/pi) int_0^lamS Si(v)/v dv ]  (exact)
        ex = quad(lambda u: h(u) * (phi(1 + u) - p1), -1, 0) + quad(lambda u: h(u) * (phi(1 + u) - p1), 0, 1)
        ex += quad(lambda u: h(u) * phi(1 + u), -np.inf, -1) + quad(lambda u: h(u) * phi(1 + u), 1, np.inf)
        siint = quad(lambda v: special.sici(v)[0] / v if v > 0 else 1.0, 0, lamS)
        ex -= p1 * 2 * (np.log(lamS) + gE - 2 / np.pi * siint)
    elif hybrid_form == 'ji2020':  # -1/|u|_+ with 2 delta ln(beta)  +  2Si/(pi u) unsubtracted
        ex = -quad(lambda u: (phi(1 + u) - p1) / abs(u), -1, 0) - quad(lambda u: (phi(1 + u) - p1) / abs(u), 0, 1) \
             - quad(lambda u: phi(1 + u) / abs(u), -np.inf, -1) - quad(lambda u: phi(1 + u) / abs(u), 1, np.inf)
        si = lambda u: 2 * special.sici(u * lamS)[0] / (np.pi * u) if u != 0 else 2 * lamS / np.pi
        ex += sum(quad(lambda u: si(u) * phi(1 + u), a_, b_) for a_, b_ in [(-np.inf, -1), (-1, 0), (0, 1), (1, np.inf)])
    else:
        raise ValueError
    return tot + 1.5 * ex

# ---------------- run ----------------
cases = [(0.4, 0.35, 0.3), (1.0, 0.5, -0.7), (2.0, 0.8, 0.0), (-0.5, 0.6, 1.2), (0.8, 1.2, -1.5)]
for sigma in (0, 1):
    for (xi0, s, ell) in cases:
        phi = lambda x, xi0=xi0, s=s: np.exp(-(x - xi0)**2 / (2 * s**2))
        for scheme in ('msbar', 'ratio'):
            m = mom_pairing(phi, ell, sigma, scheme)
            c = coord_pairing(xi0, s, ell, sigma, scheme)
            check("%-6s sigma=%d xi0=%.2f s=%.2f ell=%.2f" % (scheme, sigma, xi0, s, ell), m, c)

print("\n--- hybrid scheme (gamma^t) ---")
for (xi0, s, ell) in cases[:4]:
    for lamS in (0.5, 1.0, 2.5):
        phi = lambda x, xi0=xi0, s=s: np.exp(-(x - xi0)**2 / (2 * s**2))
        c = coord_pairing(xi0, s, ell, 0, 'hybrid', lamS)
        msu = mom_pairing(phi, ell, 0, 'hybrid', lamS, 'su')
        mji = mom_pairing(phi, ell, 0, 'hybrid', lamS, 'ji2020')
        check("hybrid[Su2022 plus-over-R] xi0=%.2f s=%.2f lamS=%.2f" % (xi0, s, lamS), msu, c)
        delta_pred = 1.5 * 2 * np.log(lamS * np.exp(gE)) * phi(1.0)
        print("     Ji2020-form minus coordinate-FT = %.10f ; predicted 3 ln(lamS e^gE) phi(1) = %.10f"
              % (mji - c, delta_pred))
        check("hybrid[Ji2020 printed form] - FT == 3 ln(lamS e^gammaE) phi(1)", mji - c, delta_pred)

print("\nSUMMARY s2: %d PASS, %d FAIL" % (PASS, FAIL))
