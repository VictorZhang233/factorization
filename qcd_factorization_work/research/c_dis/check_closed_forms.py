"""verify compact closed forms of the exact D-dim partonic results (used in DERIVATION.md)"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import io, contextlib
import sympy as sp
with contextlib.redirect_stdout(io.StringIO()):
    import dis_nlo as m
z, eps, gE = m.z, m.eps, sp.EulerGamma
R = m.RESULTS
forms = {
 'R_2^q': (R['G2q'] * (1 - z) ** (-1 - eps),
           sp.exp(eps*gE)*sp.gamma(-eps)/(2*sp.gamma(2-2*eps)) * z**eps*(1-z)**(-1-eps)*(2*(1+z**2) - eps*(7-2*z) + eps**2)),
 'R_L^q': (R['RLq'], sp.exp(eps*gE)*sp.gamma(2-eps)/sp.gamma(2-2*eps) * 2*z*(z/(1-z))**eps),
 'R_2^g': (R['R2g'], 2*sp.exp(eps*gE)*sp.gamma(-eps)/sp.gamma(2-2*eps)*(z/(1-z))**eps*((z**2+(1-z)**2) - 3*eps + 4*eps**2 - 2*eps**3)/(1-eps)**2),
 'R_L^g': (R['RLg'], sp.exp(eps*gE)*sp.gamma(1-eps)/sp.gamma(2-2*eps)*8*z*(1-z)*(z/(1-z))**eps/(1 - eps)),
}
for k, (a, b) in forms.items():
    vals = [sp.N((a - b).subs({z: zz, eps: ee}), 30) for zz in (sp.Rational(1, 7), sp.Rational(5, 9)) for ee in (sp.Rational(-3, 10), sp.Rational(2, 11))]
    print(k, 'max |diff| =', max(abs(v) for v in vals))
