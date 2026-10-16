#!/usr/bin/env python3
"""Landau-Widom check: #{eig in (a, 1-a)} grows like (2/pi^2) ln((1-a)/a) ln c  (sinc kernel on [-1,1], band c)."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
def eigs(c, n):
    xg, wg = np.polynomial.legendre.leggauss(n)
    D = xg[:, None]-xg[None, :]
    with np.errstate(invalid='ignore', divide='ignore'):
        K = np.where(np.abs(D) < 1e-14, c/np.pi, np.sin(c*D)/(np.pi*D))
    sw = np.sqrt(wg)
    return np.linalg.eigvalsh(sw[:, None]*K*sw[None, :])[::-1]
for a in [1e-2, 1e-4]:
    rows = []
    for c in [50, 200, 800]:
        e = eigs(c, int(1.2*c)+200)
        Nmid = int(np.sum((e > a) & (e < 1-a)))
        Na = int(np.sum(e > a))
        rows.append((c, Nmid, Na - 2*c/np.pi))
    print("a=%g:" % a, ["c=%d: #(a,1-a)=%d, N(a)-2c/pi=%.2f" % r for r in rows])
    slope = (rows[2][1]-rows[0][1])/np.log(16)
    print("   slope d#(a,1-a)/d ln c = %.3f ; Landau-Widom (2/pi^2) ln((1-a)/a) = %.3f" % (slope, 2/np.pi**2*np.log((1-a)/a)))
    slope2 = (rows[2][2]-rows[0][2])/np.log(16)
    print("   slope d[N(a)-2c/pi]/d ln c = %.3f ; Landau-Widom (1/pi^2) ln((1-a)/a) = %.3f" % (slope2, 1/np.pi**2*np.log((1-a)/a)))
