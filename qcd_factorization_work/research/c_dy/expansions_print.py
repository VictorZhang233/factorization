# -*- coding: utf-8 -*-
"""expansions_print.py -- Laurent expansions of the individual O(alpha_s) pieces (for DERIVATION.md), using the
closed forms verified in nlo_checks.py.  Units a = alpha_s/(2pi); L = ln(mu^2/Q^2); D_k = [ln^k(1-z)/(1-z)]_+."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
from dy_core import eps, z, L, CF, TF, EG, expand_plus, expand_regular, Dist

Kr = sp.exp(eps * EG) * sp.gamma(1 - eps) / sp.gamma(1 - 2 * eps)
Kv = sp.exp(eps * EG) * sp.gamma(1 + eps) * sp.gamma(1 - eps)**2 / sp.gamma(1 - 2 * eps)
print('K_r =', sp.series(Kr, eps, 0, 4))
print('K_v =', sp.series(Kv, eps, 0, 4))
real = CF * sp.exp(eps * L) * z**eps * (-2 / eps) * Kr * (1 + z**2 + 2 * eps**2 * (1 - z)**2 / (1 - 2 * eps))
R = expand_plus(real, 0)
for p in sorted(R):
    d = R[p].simplify()
    print('REAL qqbar eps^%d: delta: %s | plus: %s | reg: %s' % (p, sp.factor(d.delta), {k: sp.factor(c) for k, c in d.plus.items()}, sp.simplify(d.reg)))
fvirt = -Kv * (2 - eps + 2 * eps**2) / (eps**2 * (1 - 2 * eps))
V = sp.expand(sp.series(CF * sp.exp(eps * L) * sp.cos(sp.pi * eps) * fvirt, eps, 0, 1).removeO())
for p in range(-2, 1):
    print('VIRTUAL (2 Re F) eps^%d: delta coefficient = %s' % (p, sp.simplify(V.coeff(eps, p))))
print('2Re F exact = C_F (mu^2/Q^2)^eps cos(pi eps) f(eps),  f = -K_v (2-eps+2eps^2)/(eps^2(1-2eps))')
print('   |F|^2 check: cos(pi eps)*K_v =', sp.series(sp.cos(sp.pi * eps) * Kv, eps, 0, 3))
qg = TF * sp.exp(eps * L) * z**eps * (1 - z)**(-2 * eps) * (-Kr / (2 * eps)) * (2 * (z**2 + (1 - z)**2) - eps * (5 * z**2 - 6 * z + 7) + eps**2 * (1 + z)**2) / ((1 - eps) * (1 - 2 * eps))
G = expand_regular(qg, 0)
for p in sorted(G):
    print('REAL qg eps^%d: %s' % (p, sp.factor(sp.expand_log(G[p].reg, force=True))))
# D-dimensional collinear limits (splitting functions) read off from the exact forms
print('collinear limit q qbar (one leg): -(1/eps) C_F (1+z^2 - eps(1-z)^2)/(1-z) expected from P_qq(z,eps);')
print('  exact bracket [1+z^2+2eps^2(1-z)^2/(1-2eps)] is the SUM of both legs incl. angular integration -- not a splitting function')
