"""Inline coordinate tables for the pgfplots figures of FIGURES_INDEX_v2 (run: python3 -I fig_data.py)."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 40
def Phi1(t):
    rho = 2 / (1 - 2 * t + mp.sqrt(1 - 4 * t))
    return (4 * mp.polylog(2, -rho * t) + mp.log(rho * t)**2 + mp.pi**2 / 3) / mp.sqrt(1 - 4 * t)
def rem_over_t(t):
    s = 2 * t / (1 - 2 * t + mp.sqrt(1 - 4 * t))
    Qt2 = t / s
    return (Phi1(t) - (mp.log(Qt2 / t)**2 + mp.pi**2 / 3) / Qt2) / t
def nlp_I(t):
    L = mp.log(1 / t)
    return (Phi1(t) - L**2 - mp.pi**2 / 3) / t
ts = [mp.mpf(10)**(-5 + k * mp.mpf('0.25')) for k in range(0, 17)] + [mp.mpf('0.15'), mp.mpf('0.2')]
print('% fig:appN-triangle-remainder, panel (a): (t, Q^2 r / t)')
print('coordinates {' + ' '.join('(%s,%s)' % (mp.nstr(t, 6), mp.nstr(rem_over_t(t), 6)) for t in ts) + '};')
print('% panel (b): (t, (Q^2 I - L^2 - pi^2/3)/t)')
print('coordinates {' + ' '.join('(%s,%s)' % (mp.nstr(t, 6), mp.nstr(nlp_I(t), 6)) for t in ts) + '};')
