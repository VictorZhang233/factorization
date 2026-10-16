# -*- coding: utf-8 -*-
"""
E21 (independent check).  Mankiewicz-Piller, arXiv:hep-ph/9905287v1 (PRD 61 (2000) 074013), eqs. (3)-(5) and (10),
transcribed from the arXiv LaTeX source (rhot7.tex, lines 258-262, 272-281, 403-410):
  (3)  Phi(t)  = (1/2)[ tb int_0^t du phi(u)/ub - t int_t^1 du phi(u)/u ]
  (4)  g^v(t)  = (1/2)[ int_0^t du phi(u)/ub + int_t^1 du phi(u)/u ]
  (5)  g^a(t)  = 2 [ tb int_0^t du phi(u)/ub + t int_t^1 du phi(u)/u ]
  (10) I_1 = int_0^1 dt/t ( 4 g^v - 2 Phi/t + g^a/(2 t tb) ),   I_2 = int_0^1 dt/t ( 2 g^v + g^a/(2 t tb) )
Text after (10): "For the asymptotic distribution amplitude phi = 6 t tb the integrands in eq.(10) are proportional to
12/tau and 9/tau, respectively."
Run: python3 -I e21_mp.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

npass = nfail = 0
def check(label, ok, extra=''):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(('PASS ' if ok else 'FAIL ') + label + (('   [' + str(extra) + ']') if extra else ''))

t, u = sp.symbols('tau u', positive=True)
def build(phi):
    A0 = sp.integrate(phi.subs(t, u) / (1 - u), (u, 0, t))
    A1 = sp.integrate(phi.subs(t, u) / u, (u, t, 1))
    Phi = sp.Rational(1, 2) * ((1 - t) * A0 - t * A1)
    gv = sp.Rational(1, 2) * (A0 + A1)
    ga = 2 * ((1 - t) * A0 + t * A1)
    i1 = (4 * gv - 2 * Phi / t + ga / (2 * t * (1 - t))) / t
    i2 = (2 * gv + ga / (2 * t * (1 - t))) / t
    return [sp.simplify(e) for e in (Phi, gv, ga, i1, i2)]

phi_as = 6 * t * (1 - t)
Phi, gv, ga, i1, i2 = build(phi_as)
print('phi = 6 t(1-t):  g^v =', sp.factor(gv), ';  g^a =', sp.factor(ga), ';  Phi =', sp.factor(Phi))
check('g^v = (3/2)(t^2 + tb^2)', sp.simplify(gv - sp.Rational(3, 2) * (t ** 2 + (1 - t) ** 2)) == 0)
check('g^a = 6 t tb', sp.simplify(ga - 6 * t * (1 - t)) == 0)
check('Phi = (3/2) t tb (2t - 1)', sp.simplify(Phi - sp.Rational(3, 2) * t * (1 - t) * (2 * t - 1)) == 0)
print('   integrand I_1 =', sp.expand(sp.simplify(i1)), ' ;  integrand I_2 =', sp.expand(sp.simplify(i2)))
c1 = sp.limit(t * i1, t, 0); c2 = sp.limit(t * i2, t, 0)
check('integrand of I_1 ~ 12/tau (tau -> 0)', c1 == 12, c1)
check('integrand of I_2 ~ 6/tau (tau -> 0), NOT 9/tau as stated in the MP text', c2 == 6, c2)
check('exact: integrand I_1 = 12/t - 21 + 18 t ; integrand I_2 = 6/t - 6 + 6 t',
      sp.simplify(i1 - (12 / t - 21 + 18 * t)) == 0 and sp.simplify(i2 - (6 / t - 6 + 6 * t)) == 0)

# general DA in the WW approximation: endpoint constants 8 g^v(0) and 4 g^v(0), g^v(0) = (1/2) int phi/u
a2, a4 = sp.symbols('a2 a4', real=True)
C2 = lambda z: sp.Rational(3, 2) * (5 * z ** 2 - 1)                     # Gegenbauer C_2^{3/2}(z)
C4 = lambda z: sp.Rational(15, 8) * (21 * z ** 4 - 14 * z ** 2 + 1)      # C_4^{3/2}(z)
phi_gen = 6 * t * (1 - t) * (1 + a2 * C2(2 * t - 1) + a4 * C4(2 * t - 1))
Phi_g, gv_g, ga_g, i1_g, i2_g = build(phi_gen)
gv0 = sp.simplify(gv_g.subs(t, 0)) if gv_g.subs(t, 0) != sp.nan else sp.limit(gv_g, t, 0)
gv0 = sp.simplify(sp.limit(gv_g, t, 0))
sig = sp.simplify(sp.integrate(phi_gen / t, (t, 0, 1)))
check('g^v(0) = (1/2) int_0^1 phi(u)/u du  (general a2, a4)', sp.simplify(gv0 - sig / 2) == 0, sp.factor(gv0))
c1g = sp.simplify(sp.limit(t * i1_g, t, 0)); c2g = sp.simplify(sp.limit(t * i2_g, t, 0))
check('general WW: integrand I_1 ~ 8 g^v(0)/tau', sp.simplify(c1g - 8 * gv0) == 0, sp.factor(c1g))
check('general WW: integrand I_2 ~ 4 g^v(0)/tau  (ratio of endpoint constants = 2 for every DA)', sp.simplify(c2g - 4 * gv0) == 0, sp.factor(c2g))
# what would give 9 for the asymptotic DA: 6 g^v(0) = 9 -> e.g. 4 g^v (instead of 2 g^v) in I_2, or g^a/(t tb) instead of g^a/(2 t tb)
alt1 = sp.limit(t * ((4 * gv + ga / (2 * t * (1 - t))) / t), t, 0)
alt2 = sp.limit(t * ((2 * gv + ga / (t * (1 - t))) / t), t, 0)
print('   (alternatives reproducing "9": 4g^v in I_2 ->', alt1, '; g^a/(t tb) in I_2 ->', alt2, ')')
check('the printed eq.(10) cannot give 9/tau for phi = 6 t tb; either the text or eq.(10) is misprinted', c2 != 9 and alt1 == 9)
# endpoint-suppressed DA: still log divergent
Phi_s, gv_s, ga_s, i1_s, i2_s = build(30 * t ** 2 * (1 - t) ** 2)
check('endpoint-suppressed phi = 30 t^2 tb^2: constants 10 and 5 (log divergence persists)',
      sp.limit(t * i1_s, t, 0) == 10 and sp.limit(t * i2_s, t, 0) == 5)
print('-' * 70)
print('e21_mp: %d PASS, %d FAIL' % (npass, nfail))
