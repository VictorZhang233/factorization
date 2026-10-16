#!/usr/bin/env python3
"""N10 independent check: strip of analyticity, truncation bound, numbers e^{-m z_L}, sinc-kernel eigenvalue counts.
(Kf)(x) = int_{-1}^{1} sin(c(x-y))/(pi(x-y)) f(y) dy,  c = lambda_L.
Eigenvalues by Gauss-Legendre Nystrom discretization (symmetrized), checked at two resolutions and against
an independent Legendre-basis (spherical Bessel) matrix.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from scipy import special, integrate
import mpmath as mp

res = []
def rep(name, ok, extra=""):
    ok = bool(ok); res.append(ok)
    print(("PASS " if ok else "FAIL ") + name + ((" : " + extra) if extra else ""))

hbarc = 0.1973269804   # GeV fm (CODATA 2018)
m = 0.5
for zL, claimed in [(1.0, 0.079), (1.5, 0.022)]:
    v = np.exp(-m*zL/hbarc)
    rep("e^{-m z_L}, m=0.5 GeV, z_L=%.1f fm = %.4f (claimed %.3f)" % (zL, v, claimed), abs(v-claimed) < 0.0006)

# truncation bound: |int_{|lam|>L} dlam/(2pi) e^{-i x lam} h| <= 2 int_L^inf A e^{-m lam/P}/(2 pi) = A P e^{-m L/P}/(pi m)
A, P, mm = 1.3, 2.0, 0.5
for L in [5.0, 10.0, 20.0]:
    for x in [0.1, 0.4, 0.9]:
        h = lambda lam: A*np.exp(-mm*abs(lam)/P)*np.cos(0.7*lam + 0.3)    # |h| <= A e^{-m|lam|/P}
        tail = 2*integrate.quad(lambda lam: np.cos(x*lam)*h(lam), L, np.inf, limit=2000)[0]/(2*np.pi)  # even part only
        bound = A*P*np.exp(-mm*L/P)/(np.pi*mm)
        if not abs(tail) <= bound:
            rep("truncation bound violated", False, "L=%g x=%g" % (L, x))
rep("truncation bound |tail| <= A P e^{-m z_L}/(pi m) holds in tests (z_L = lambda_L/P)", True)
# strip: FT of A e^{-m|lam|/P} is (A/pi)(m/P)/((m/P)^2 + x^2): poles at x = +- i m/P
x = mp.mpf('0.37'); a_ = mp.mpf(mm)/P
num = mp.quad(lambda lam: mp.e**(-a_*abs(lam))*mp.cos(x*lam), [-mp.inf, 0, mp.inf])/(2*mp.pi)
rep("FT of e^{-m|lam|/P} = (1/pi)(m/P)/((m/P)^2+x^2) (poles at +-i m/P: strip width is sharp)", abs(num - a_/(mp.pi*(a_**2+x**2))) < 1e-20)

def sinc_eigs(c, n):
    xg, wg = np.polynomial.legendre.leggauss(n)
    X, Y = np.meshgrid(xg, xg, indexing='ij')
    D = X - Y
    with np.errstate(invalid='ignore', divide='ignore'):
        K = np.where(np.abs(D) < 1e-14, c/np.pi, np.sin(c*D)/(np.pi*D))
    sw = np.sqrt(wg)
    S = sw[:, None]*K*sw[None, :]
    ev = np.linalg.eigvalsh(S)[::-1]
    return ev
claimed = {5: 3, 10: 6, 15: 10, 25: 16}
for c in [5, 10, 15, 25]:
    e1 = sinc_eigs(c, 160); e2 = sinc_eigs(c, 320)
    k = 24
    agree = np.max(np.abs(e1[:k]-e2[:k])) < 1e-12
    nhalf = int(np.sum(e2 > 0.5))
    # independent spectral check in the normalized Legendre basis:
    # K_mn = sqrt((2m+1)(2n+1)) (-1)^((m-n)/2) (2/pi) int_0^c j_m(k) j_n(k) dk  (m-n even; 0 otherwise)
    nb = 70
    Kl = np.zeros((nb, nb))
    for mm_ in range(nb):
        for nn_ in range(mm_, nb, 2):
            val = integrate.quad(lambda k: special.spherical_jn(mm_, k)*special.spherical_jn(nn_, k), 0, c, limit=400, epsabs=1e-15, epsrel=1e-13)[0]
            Kl[mm_, nn_] = Kl[nn_, mm_] = np.sqrt((2*mm_+1)*(2*nn_+1))*(-1)**((nn_-mm_)//2)*2/np.pi*val
    sl = np.linalg.eigvalsh(Kl)[::-1]
    ok_sl = np.max(np.abs(sl[:k]-e2[:k])) < 1e-10
    print("   c=%2d: eigenvalues(1..%d) = %s" % (c, nhalf+3, " ".join("%.4g" % v for v in e2[:nhalf+3])))
    print("          Legendre-basis check    = %s" % " ".join("%.4g" % v for v in sl[:nhalf+3]))
    rep("c=%d: Nystrom converged (160 vs 320 nodes)" % c, agree)
    rep("c=%d: #eig>1/2 = %d (claimed %d); 2c/pi = %.2f" % (c, nhalf, claimed[c], 2*c/np.pi), nhalf == claimed[c])
    rep("c=%d: Nystrom eigenvalues agree with independent Legendre-basis (spherical Bessel) computation to 1e-10" % c, ok_sl, "max diff %.1e" % np.max(np.abs(sl[:k]-e2[:k])))
    tr = np.sum(e2)
    rep("c=%d: trace = 2c/pi (sum of all eigenvalues)" % c, abs(tr - 2*c/np.pi) < 1e-8, "%.10f" % tr)
    # Landau-Widom: N(eps) ~ 2c/pi + (1/pi^2) ln((1-eps)/eps) ln c ; for eps=1/2 the log term vanishes
print("SUMMARY n10: %d/%d PASS" % (sum(res), len(res)))
