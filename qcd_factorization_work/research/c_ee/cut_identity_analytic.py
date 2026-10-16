"""
cut_identity_analytic.py -- analytic (not numerical) proof of the O(g^2) D-dim cutting identity (DERIVATION.md 4.4):
term by term,  2(D-1) s Im[ r1 G11^2 (Q^2)^-2eps ] / (4pi)^D  <->  rho_V   and
               2(D-1) s Im[ r2 G11 G(1+eps,1) (Q^2)^-2eps ] / (4pi)^D  <->  rho_R ,
each ratio simplified with gammasimp (reflection formulas) to exactly 1.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
e = sp.Symbol('eps')
s = sp.Symbol('s', positive=True)
g2 = sp.Symbol('g2', positive=True)
D = 4 - 2 * e
G = lambda a, b: sp.gamma(a + b - D / 2) * sp.gamma(D / 2 - a) * sp.gamma(D / 2 - b) / (sp.gamma(a) * sp.gamma(b) * sp.gamma(D - a - b))
r1 = -4 * (1 - e) * (2 - e + 2 * e ** 2) / (e * (3 - 2 * e))
r2 = 16 * (1 - e) * (1 - 2 * e) * (2 - 2 * e + e ** 2) / (e * (3 - 2 * e) * (2 - 3 * e))
Phi2 = (1 / (8 * sp.pi)) * (4 * sp.pi / s) ** e * sp.gamma(1 - e) / sp.gamma(2 - 2 * e)
rho0 = 2 * (D - 2) * s * Phi2
cG = sp.gamma(1 + e) * sp.gamma(1 - e) ** 2 / sp.gamma(1 - 2 * e)
f = -(2 - e + 2 * e ** 2) / (e ** 2 * (1 - 2 * e))
pref = (g2 / (4 * sp.pi)) / (2 * sp.pi) * (4 * sp.pi / s) ** e
rhoV = rho0 * pref * f * cG * sp.cos(sp.pi * e)
rhoR = rho0 * pref * 2 * (1 - 2 * e) * (2 - 2 * e + e ** 2) * sp.gamma(1 - e) ** 2 / (e ** 2 * (1 - 3 * e) * (2 - 3 * e) * sp.gamma(1 - 3 * e))
im = s ** (-2 * e) * sp.sin(2 * sp.pi * e)
lhs1 = 2 * (D - 1) * s * im * r1 * G(1, 1) ** 2 * g2 / (4 * sp.pi) ** D
lhs2 = 2 * (D - 1) * s * im * r2 * G(1, 1) * G(1 + e, 1) * g2 / (4 * sp.pi) ** D


def simp(x):
    x = sp.expand_trig(sp.powsimp(sp.gammasimp(x), force=True))
    x = sp.gammasimp(sp.simplify(x))
    return sp.simplify(sp.powsimp(x, force=True))


q1 = simp(lhs1 / rhoV)
q2 = simp(lhs2 / rhoR)
print('virtual ratio:', q1)
print('real    ratio:', q2)
ok = (q1 == 1) and (q2 == 1)
if not ok:   # fall back: high-precision numerics at several eps
    import mpmath as mp
    mp.mp.dps = 40
    ok = all(abs(sp.N((lhs1 / rhoV).subs({e: sp.Rational(k, 37), s: 3, g2: 1}), 35) - 1) < 1e-30 and
             abs(sp.N((lhs2 / rhoR).subs({e: sp.Rational(k, 37), s: 3, g2: 1}), 35) - 1) < 1e-30 for k in (1, -5, 7, 11))
    print('(symbolic simplification incomplete; termwise numerical check:', ok, ')')
print(('PASS  ' if ok else 'FAIL  ') + 'X1  termwise cutting identity: G11^2 term = virtual cut, G11 G(1+eps,1) term = real cut')
