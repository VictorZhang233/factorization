# -*- coding: utf-8 -*-
"""plus_trap.py -- notational trap: (1+z^2) [ln(1-z)/(1-z)]_+  vs  [(1+z^2) ln(1-z)/(1-z)]_+  (CONTEXT plus definition),
and decomposition of the pi^2 in the MS-bar delta(1-z) coefficient."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import sympy as sp
mp.mp.dps = 30
h = lambda w: mp.exp(w) * mp.cos(2 * w)          # generic test function
A = mp.quad(lambda w: ((1 + w**2) * h(w) - 2 * h(1)) * mp.log(1 - w) / (1 - w), [0, 1])   # (1+z^2) D_1
B = mp.quad(lambda w: (1 + w**2) * (h(w) - h(1)) * mp.log(1 - w) / (1 - w), [0, 1])          # [(1+z^2) L/(1-z)]_+
print('(1+z^2)D_1 - [(1+z^2)ln(1-z)/(1-z)]_+  =  c * delta(1-z) with c =', mp.nstr((A - B) / h(1), 20), ' (expected 7/4)')
print('=> 4(1+z^2)D_1 = 4[(1+z^2)ln(1-z)/(1-z)]_+ + 7 delta(1-z): with the plus on the whole term the MS-bar delta coefficient would read C_F(2pi^2/3 - 1)')
z = sp.Symbol('z')
print('symbolic: int_0^1 (1+z) ln(1-z) dz =', sp.integrate((1 + z) * sp.log(1 - z), (z, 0, 1)))
# pi^2 bookkeeping in the q qbar delta coefficient (units a C_F):
#   real K_r = 1 - (pi^2/4) eps^2 times 2/eps^2  -> -pi^2/2 ;  virtual K_v = 1 - (pi^2/12)eps^2 times -2/eps^2 -> +pi^2/6 ;
#   timelike continuation cos(pi eps) = 1 - pi^2 eps^2/2 times -2/eps^2 -> +pi^2
tot = -sp.pi**2 / 2 + sp.pi**2 / 6 + sp.pi**2
print('pi^2 bookkeeping: real -pi^2/2, virtual Gamma-functions +pi^2/6, timelike continuation +pi^2 ; total =', sp.simplify(tot), '(= 2pi^2/3)')
