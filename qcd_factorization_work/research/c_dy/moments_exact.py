# -*- coding: utf-8 -*-
"""moments_exact.py -- Mellin moments N=1,2 of the MS-bar coefficient functions (mu_F = Q, units alpha_s/2pi),
compared with the closed forms (derived by hand in DERIVATION.md 3.7) to 50 significant digits."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 50
z2 = mp.zeta(2)
def mom_qq(N):   # in units of C_F:  8 D_1 - 4(1+z)ln(1-z) - 2(1+z^2) ln z/(1-z) + (2pi^2/3 - 8) delta
    d1 = mp.quad(lambda z: (z**(N - 1) - 1) * mp.log(1 - z) / (1 - z), [0, 0.5, 1])
    r = mp.quad(lambda z: (-4 * (1 + z) * mp.log(1 - z) - 2 * (1 + z**2) * mp.log(z) / (1 - z)) * z**(N - 1), [0, 0.5, 1])
    return 8 * d1 + r + 2 * mp.pi**2 / 3 - 8
def mom_qg(N):   # in units of T_F
    return mp.quad(lambda z: ((z**2 + (1 - z)**2) * (2 * mp.log(1 - z) - mp.log(z)) + mp.mpf(1) / 2 + 3 * z - mp.mpf(7) / 2 * z**2) * z**(N - 1), [0, 0.5, 1])
closed = {('qq', 1): 8 * z2 - mp.mpf(7) / 2, ('qq', 2): 8 * z2 + mp.mpf(13) / 18, ('qg', 1): mp.mpf(1) / 9, ('qg', 2): -mp.mpf(11) / 18}
ok = True
for N in (1, 2):
    for ch, f in (('qq', mom_qq), ('qg', mom_qg)):
        val = f(N); d = abs(val - closed[(ch, N)])
        ok = ok and d < mp.mpf(10)**-40
        print('N=%d %s: numeric %s ; closed form %s ; |diff| = %s' % (N, ch, mp.nstr(val, 25), mp.nstr(closed[(ch, N)], 25), mp.nstr(d, 3)))
print('closed forms: Delta_qq: N=1 C_F(8 zeta2 - 7/2) = C_F(4pi^2/3 - 7/2), N=2 C_F(8 zeta2 + 13/18); Delta_qg: N=1 T_F/9, N=2 -11 T_F/18')
print('[%s] Mellin moments N=1,2 equal the closed forms to 40 digits' % ('PASS' if ok else 'FAIL'))
