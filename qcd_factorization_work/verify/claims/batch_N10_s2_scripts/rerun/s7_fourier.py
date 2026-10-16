#!/usr/bin/env python3
"""s7: two elementary but rigorous statements about the Fourier transform step (LAMET.md section 7):
 (P1) truncation bound: if |h(lambda)| <= A exp(-m|lambda|/P) for |lambda|>lambda_L, the truncation error of
      qtilde(x) = int dlambda/2pi e^{-i x lambda} h(lambda) is <= A P/(pi m) exp(-m lambda_L/P)   (checked on an example)
 (P2) degrees of freedom of the pseudo-PDF/ITD inverse problem (Slepian/Landau-Widom): the time-frequency limiting
      operator (Kf)(x) = int_{-1}^{1} sin(c(x-y))/(pi(x-y)) f(y) dy, c = lambda_L, has ~ 2c/pi eigenvalues close to 1;
      the remaining ones decay super-exponentially -> exponential instability of the inversion beyond ~2 lambda_L/pi modes.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from scipy import integrate
PASS=0; FAIL=0
def check(n, ok):
    global PASS, FAIL
    print(("PASS " if ok else "FAIL ")+n); PASS+=ok; FAIL+=(not ok)
# (P1) example h(lambda) = A exp(-m|lambda|/P) cos(0.7 lambda): exact tail contribution at x
A, m, P = 0.8, 0.5, 2.0
for lamL in (5.0, 10.0, 20.0):
    for x in (0.2, 0.6):
        tail = 2*integrate.quad(lambda l: np.cos(x*l)*A*np.exp(-m*l/P)*np.cos(0.7*l), lamL, np.inf, limit=400)[0]/(2*np.pi)
        bound = A*P/(np.pi*m)*np.exp(-m*lamL/P)
        check("P1 truncation tail |%.3e| <= bound %.3e (lambda_L=%.0f, x=%.1f)" % (tail, bound, lamL, x), abs(tail) <= bound*(1+1e-12))
# numbers quoted in the text: m = 0.5 GeV, z_L = 1 fm
hbarc = 0.1973269804
print("   e^{-m z_L} for m=0.5 GeV, z_L=1 fm: %.4f ; z_L=1.5 fm: %.4f" % (np.exp(-0.5/hbarc*1.0), np.exp(-0.5/hbarc*1.5)))
# (P2) Slepian counting
def eigs(c, n=600):
    xg, wg = np.polynomial.legendre.leggauss(n)
    X, Y = np.meshgrid(xg, xg, indexing='ij')
    D = X - Y
    with np.errstate(divide='ignore', invalid='ignore'):
        K = np.where(np.abs(D) > 1e-14, np.sin(c*D)/(np.pi*D), c/np.pi)
    sw = np.sqrt(wg)
    M = sw[:, None]*K*sw[None, :]
    ev = np.linalg.eigvalsh(M)[::-1]
    return ev
for c in (5.0, 10.0, 15.0, 25.0):
    ev = eigs(c)
    nhalf = int(np.sum(ev > 0.5))
    pred = 2*c/np.pi
    print("   c=lambda_L=%5.1f: #eig>0.5 = %d, 2c/pi = %.2f, eigenvalues: %s" % (c, nhalf, pred, " ".join("%.1e" % v for v in ev[:int(pred)+5])))
    check("P2 number of eigenvalues > 1/2 within 1 of 2c/pi (c=%.0f)" % c, abs(nhalf - pred) <= 1.0)
    # super-exponential decay beyond the plunge: eigenvalue at index 2c/pi + 6 is < 1e-3
    k = int(np.ceil(pred)) + 6
    check("P2 eigenvalue #%d < 1e-3 (c=%.0f): %.2e" % (k, c, ev[k]), ev[k] < 1e-3)
print("\nSUMMARY s7: %d PASS, %d FAIL" % (PASS, FAIL))
