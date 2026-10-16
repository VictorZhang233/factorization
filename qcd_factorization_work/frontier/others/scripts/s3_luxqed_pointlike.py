#!/usr/bin/env python3
"""
s3_luxqed_pointlike.py -- check of the LUXqed master formula (Manohar-Nason-Salam-Zanderighi,
PRL 117 (2016) 242002, Eq. (6); JHEP 12 (2017) 046) on a point-like target.

LUXqed (fixed alpha for this check):
 x f_gamma(x,mu^2) = 1/(2 pi alpha) Int_x^1 dz/z { Int_{x^2 m^2/(1-z)}^{mu^2/(1-z)} dQ^2/Q^2 alpha^2
        [ (z p_gq(z) + 2 x^2 m^2/Q^2) F2(x/z,Q^2) - z^2 FL(x/z,Q^2) ]  - alpha^2 z^2 F2(x/z,mu^2) },
 z p_gq(z) = 1 + (1-z)^2.
For a point-like Dirac fermion of unit charge and mass m (elastic only, G_E = G_M = 1):
 F2 = [G_E^2 + tau G_M^2]/(1+tau) delta(1-x') = delta(1-x'),   FL = G_E^2/tau delta(1-x') = 4 m^2/Q^2 delta(1-x').
Expected: the O(alpha) MS-bar photon distribution of a lepton (Frixione, JHEP 11 (2019) 158, Eq. (4.189)):
 x f_gamma = alpha/(2 pi) [1 + (1-x)^2] [ ln(mu^2/m^2) - 2 ln x - 1 ]  + O(m^2/mu^2).
Run: python3 -I s3_luxqed_pointlike.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

PASS = FAIL = 0
def check(name, ok, info=""):
    global PASS, FAIL
    if ok: PASS += 1
    else:  FAIL += 1
    print(("[PASS] " if ok else "[FAIL] ") + name + ("  " + info if info else ""))

x, m, mu, Q2, al = sp.symbols('x m mu Q2 alpha', positive=True)
z = x                                    # delta(1 - x/z) = x delta(z - x);  Int dz/z g(z) x delta(z-x) = g(x)
pgq = 1 + (1 - z)**2                     # = z p_gq(z)
F2 = 1
FL = 4 * m**2 / Q2
Qmin2 = x**2 * m**2 / (1 - z)
Qmax2 = mu**2 / (1 - z)
inner = sp.integrate(al**2 * ((pgq + 2 * x**2 * m**2 / Q2) * F2 - z**2 * FL) / Q2, (Q2, Qmin2, Qmax2))
xf = sp.simplify((inner - al**2 * z**2 * 1) / (2 * sp.pi * al))
expected = al / (2 * sp.pi) * (1 + (1 - x)**2) * (sp.log(mu**2 / m**2) - 2 * sp.log(x) - 1)
diff = sp.simplify(sp.expand_log(xf - expected, force=True))
# leading-power: the difference must vanish as m/mu -> 0
lim = sp.limit(diff.subs(mu, m / sp.Symbol('r', positive=True)), sp.Symbol('r', positive=True), 0)
check("LUXqed on point-like elastic target reproduces the O(alpha) MS-bar photon-in-lepton pdf "
      "(Frixione 2019 Eq. 4.189) at leading power", sp.simplify(lim) == 0,
      f"difference = {sp.simplify(diff)}")
# without the F_L (longitudinal) term the constant would be wrong by 4(1-x): shows F_L is essential
inner_noFL = sp.integrate(al**2 * ((pgq + 2 * x**2 * m**2 / Q2) * F2) / Q2, (Q2, Qmin2, Qmax2))
xf_noFL = sp.simplify((inner_noFL - al**2 * z**2) / (2 * sp.pi * al))
d2 = sp.simplify(sp.expand_log(xf_noFL - expected, force=True))
lim2 = sp.simplify(sp.limit(d2.subs(mu, m / sp.Symbol('r', positive=True)), sp.Symbol('r', positive=True), 0))
check("dropping F_L changes the constant by alpha/(2 pi) * 4(1-x)", sp.simplify(lim2 - al/(2*sp.pi)*4*(1-x)) == 0,
      f"(LP difference without F_L = {lim2})")
# without the MS-bar conversion term (-alpha^2 z^2 F2(mu^2)) the constant is off by -x^2 alpha/(2 pi):
xf_noconv = sp.simplify(inner / (2 * sp.pi * al))
d3 = sp.simplify(sp.limit(sp.expand_log(xf_noconv - expected, force=True).subs(mu, m / sp.Symbol('r', positive=True)),
                          sp.Symbol('r', positive=True), 0))
check("the 'MS-bar conversion' term of LUXqed contributes exactly -x^2 alpha/(2pi) here", sp.simplify(d3 - al/(2*sp.pi)*x**2) == 0,
      f"(LP difference without conversion term = {d3})")
print(f"\nTOTAL: {PASS} PASS, {FAIL} FAIL")
