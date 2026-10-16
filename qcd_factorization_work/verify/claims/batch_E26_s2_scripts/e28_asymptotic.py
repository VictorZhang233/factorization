"""
e28_asymptotic.py -- stage-2 verifier (batch E26_s2), claim E28: analytic small-(eps,delta) limit.
Leading-power 3-jet region (eps <~ delta << 1, eps = fraction of TOTAL energy):
   u = x3 > 2 eps,  r0 < r < 1 - r0,  r0 = sigma(1-u),  sigma = sin^2 delta   (u = x3, r = y13/x3)
(soft q/qbar corners, the q-qbar cone and O(sigma) shifts of the edges give O(eps ln delta, delta^2 ln) only.)
With f dx1 dx2 = [N0/(r(1-r)) - 2u^2] du dr / u,  N0 = 1+(1-u)^2  (checked below), the r-integral is
   2 N0 ln((1-r0)/r0) - 2u^2 (1-2r0)  ->  2 N0 (-ln sigma - ln(1-u)) - 2u^2 + O(sigma),
so I3 = 2(-ln sigma) int_{2eps}^1 N0 du/u + 2 int_0^1 N0 (-ln(1-u)) du/u - 2 int_0^1 u du + o(1).
Run: python3 -I e28_asymptotic.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
u, r, r0, e, sig, dl = sp.symbols('u r r0 epsilon sigma delta', positive=True)
N = (1 - (1 - r) * u) ** 2 + (1 - r * u) ** 2
N0 = 1 + (1 - u) ** 2
print('N - [N0 - 2u^2 r(1-r)] =', sp.expand(N - (N0 - 2 * u ** 2 * r * (1 - r))))
# inner integral: N/(r(1-r)) = N0/r + N0/(1-r) - 2u^2
inner_integrand_check = sp.simplify(N / (r * (1 - r)) - (N0 / r + N0 / (1 - r) - 2 * u ** 2))
print('N/(r(1-r)) - [N0/r + N0/(1-r) - 2u^2] =', inner_integrand_check)
inner = N0 * (sp.log(1 - r0) - sp.log(r0)) + N0 * (sp.log(1 - r0) - sp.log(r0)) - 2 * u ** 2 * (1 - 2 * r0)
print('=> inner r-integral = 2 N0 ln((1-r0)/r0) - 2u^2 (1-2r0)')
T1 = sp.integrate(sp.expand(N0 / u), (u, 2 * e, 1))
T1lim = sp.limit(T1 - (-2 * sp.log(2 * e)), e, 0) - 2 * sp.log(2 * e)
print('int_{2eps}^1 N0/u du  ->', sp.simplify(T1lim), ' + O(eps)')
mp.mp.dps = 30
T2num = mp.quad(lambda x: (2 - 2 * x + x * x) * (-mp.log(1 - x)) / x, [0, 0.5, 1])
T2 = sp.pi ** 2 / 3 - sp.Rational(5, 4)
print('int_0^1 N0 (-ln(1-u))/u du = %s ; pi^2/3 - 5/4 = %s' % (mp.nstr(T2num, 25), mp.nstr(mp.pi ** 2 / 3 - mp.mpf(5) / 4, 25)))
I3 = 2 * ((-sp.log(sig)) * T1lim + T2) - 1          # -2 int_0^1 u du = -1
I3 = sp.expand(sp.expand_log(I3.subs(sig, dl ** 2), force=True))
print('I3 asymptotic =', I3)
c2j = sp.expand(sp.Rational(3, 4) - I3 / 2)
SW = -(4 * sp.log(dl) * sp.log(2 * e) + 3 * sp.log(dl) + sp.pi ** 2 / 3 - sp.Rational(5, 2))
print('c2j(asymptotic) - SW bracket with ln(2 eps) =', sp.simplify(sp.expand_log(c2j - sp.expand(sp.expand_log(SW, force=True)), force=True)))
