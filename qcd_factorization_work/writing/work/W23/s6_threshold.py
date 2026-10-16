# -*- coding: utf-8 -*-
"""
s6_threshold.py -- Ch20 ex:heavy-cv: independent numerical check of the region structure near threshold.
 Full one-loop QED vertex (Feynman gauge, photon mass mu_g as IR regulator, on-shell renormalization;
 Peskin-Schroeder eq. (6.56) parametrization, with ln(Delta(0)/Delta(q^2)) for the subtracted log) for the
 time-like current gamma* -> f fbar at q^2 = 4 m^2/(1-beta^2), beta = velocity of each fermion in the c.m. frame.
 At threshold only G_M = F1 + F2 survives (S wave), so the amplitude correction is K(beta) = Re (dF1 + F2)/(alpha/pi).
 Expected (hard region = c_v, potential region = Coulomb exchange):
     K(beta) = pi^2/(4 beta) - 2 + O(beta)    [=> |amplitude|^2 = 1 + alpha (pi/(2 beta) - 4/pi) + O(alpha beta)],
 i.e. the constant -2 (alpha/pi) = c_v - 1 at C_F alpha_s -> alpha, and the Sommerfeld term pi alpha/(4 beta).
 The t-integral is done analytically (principal value), the z-integral numerically (mpmath).
Run: python3 -I s6_threshold.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w23common import *

ck = Check('s6_threshold: full one-loop vertex near threshold vs Coulomb + hard (c_v) decomposition')
mp.mp.dps = 30
m = mp.mpf(1)

def K_of_beta(beta, mug):
    q2 = 4 * m**2 / (1 - beta**2)
    def integrand(w):
        z = 1 - w
        A = w**2 * m**2 + mug**2 * z
        B = w**2 * q2
        D0 = w**2 * m**2 + mug**2 * z               # Delta at q^2 = 0 (t independent)
        r = 4 * A / B
        if r < 1:
            b = mp.sqrt(1 - r)
            tp, tm = (1 + b) / 2, (1 - b) / 2
            Ia = -(2 / (B * b)) * mp.log((1 + b) / (1 - b))
            J = lambda c: (1 - c) * mp.log(1 - c) + c * mp.log(c) - 1
            Ic = mp.log(B) + J(tp) + J(tm)
        else:
            c = mp.sqrt(r - 1)
            Ia = 4 * mp.atan(1 / c) / (B * c)
            Ic = mp.log(B) + mp.log((1 + c**2) / 4) - 2 + 2 * c * mp.atan(1 / c)
        # PV int dt t(1-t)/Delta = (A Ia - 1)/B
        Itt = (A * Ia - 1) / B
        Ib = (1 - w) * Ia + w**2 * Itt               # int dt (1-x)(1-y)/Delta, x = w t, y = w (1-t)
        n1 = m**2 * (1 - 4 * z + z**2)
        dF1 = mp.log(D0) - Ic + n1 * Ia + q2 * Ib - n1 / D0
        F2 = 2 * m**2 * z * (1 - z) * Ia
        return w * (dF1 + F2)                       # measure: dx dy delta(...) = w dt dz
    wc2 = 4 * mug**2 / (q2 - 4 * m**2)              # approx boundary where real roots appear (w^2 ~ wc2)
    wc = mp.sqrt(wc2)
    pts = [mp.mpf(0)] + [wc * f for f in (mp.mpf('0.5'), 1, 2, 10, 100, 1000)] + [mp.mpf(10)**k for k in range(-8, 0)] + [mp.mpf(1)]
    pts = sorted(set([p for p in pts if p <= 1]))
    val = mp.quad(integrand, pts, maxdegree=10)
    return val / 2                                    # (alpha/2pi) -> units of alpha/pi

betas = [mp.mpf(x) for x in ('0.01', '0.02', '0.04', '0.08')]
mug = mp.mpf('1e-14')
Ks = []
for bt in betas:
    Kv = K_of_beta(bt, mug)
    Ks.append(Kv)
    print('   beta = %s : K = %s ;  K - pi^2/(4 beta) = %s' % (mp.nstr(bt, 3), mp.nstr(Kv, 12), mp.nstr(Kv - mp.pi**2 / (4 * bt), 8)))
# fit K = c_{-1}/beta + c0 + c1 beta + c2 beta^2 using the four points
Mtx = mp.matrix([[1 / b, 1, b, b**2] for b in betas])
coef = mp.lu_solve(Mtx, mp.matrix(Ks))
print('   fit: c_-1 = %s (pi^2/4 = %s), c0 = %s, c1 = %s' % (mp.nstr(coef[0], 8), mp.nstr(mp.pi**2 / 4, 8), mp.nstr(coef[1], 8), mp.nstr(coef[2], 6)))
ck('Coulomb coefficient c_-1 = pi^2/4 (Sommerfeld: |psi(0)|^2 = 1 + pi alpha/(2 beta) + ...)', abs(coef[0] - mp.pi**2 / 4) < 1e-3)
ck('hard constant c0 = -2 (= c_v - 1 in units of alpha/pi, C_F alpha_s -> alpha)', abs(coef[1] + 2) < 2e-3)
# IR-regulator independence of the constant at small beta (mu_g varied by 10^4)
K2 = K_of_beta(mp.mpf('0.02'), mp.mpf('1e-10'))
print('   beta = 0.02, mu_g = 1e-10 m: K = %s (vs %s at 1e-14)' % (mp.nstr(K2, 10), mp.nstr(Ks[1], 10)))
ck('IR sensitivity at threshold is O(beta^2 ln mu_g): small at beta = 0.02', abs(K2 - Ks[1]) < 0.02)

ok = ck.summary()
sys.exit(0 if ok else 1)
