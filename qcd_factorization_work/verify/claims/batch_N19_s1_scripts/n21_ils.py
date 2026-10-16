"""
n21_ils.py -- independent check of claim N21 (Isgur-Llewellyn Smith soft fractions), own sympy derivation.
R(c) = int int_{xbar ybar < c} phi(x)phi(y)/(xbar ybar) / int int phi(x)phi(y)/(xbar ybar),  c = mu0^2/Q^2 <= 1.
With u = xbar, v = ybar: phi(x)/xbar = g(u) := phi(1-u)/u ; region u v < c in [0,1]^2.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
RES = []
def check(name, ok, info=''):
    RES.append(bool(ok)); print(('PASS ' if ok else 'FAIL ') + name + (('   [' + info + ']') if info else ''))
u, v, c = sp.symbols('u v c', positive=True)
x = sp.Symbol('x', positive=True)
DAs = {'as': 6*x*(1 - x), 'CZ': 30*x*(1 - x)*(2*x - 1)**2}
claims = {'as': c*(5*c - 2*(c + 2)*sp.log(c) - 4),
          'CZ': c*(456*c**3 + 352*c**2 - 675*c - 132 - (144*c**3 + 768*c**2 + 450*c + 36)*sp.log(c))}
for name, phi in DAs.items():
    check('%s DA normalised: int_0^1 phi = 1' % name, sp.integrate(phi, (x, 0, 1)) == 1)
    g = sp.simplify(phi.subs(x, 1 - u)/u)        # phi(x)/xbar as a function of u = xbar
    G1 = sp.integrate(g, (u, 0, 1))
    tot = G1**2
    # region u v < c:  u in (0,c): v in (0,1);  u in (c,1): v in (0, c/u)
    gv = g.subs(u, v)
    part1 = sp.integrate(g, (u, 0, c))*sp.integrate(gv, (v, 0, 1))
    inner = sp.integrate(gv, (v, 0, c/u))
    part2 = sp.integrate(sp.expand(g*inner), (u, c, 1))
    R = sp.simplify(sp.expand((part1 + part2)/tot))
    diff = sp.simplify(sp.expand(R - claims[name]))
    check('R_%s(c) derived here equals the claimed closed form' % name, diff == 0, 'R = %s' % sp.factor(R))
    check('R_%s(1) = 1' % name, sp.simplify(claims[name].subs(c, 1)) == 1)
    lead = sp.limit(claims[name]/(c*sp.log(1/c)), c, 0)
    print('      c->0: R_%s / (c ln(1/c)) -> %s' % (name, lead))
    # numerical cross-check by 2D quadrature
    f = sp.lambdify((u, v), g*g.subs(u, v)/tot, 'mpmath')
    for cv in [mp.mpf('0.25'), mp.mpf('0.1')]:
        num = mp.quad(lambda uu: mp.quad(lambda vv: f(uu, vv), [0, min(1, cv/uu)]), [0, cv, 1])
        an = sp.N(claims[name].subs(c, sp.Rational(str(cv))), 20)
        check('R_%s(%s): 2D quadrature = closed form' % (name, mp.nstr(cv, 3)), abs(num - an) < 1e-12, '%s vs %s' % (mp.nstr(num, 12), an))
    # monotonic on (0,1]
    dR = sp.diff(claims[name], c)
    vals = [sp.N(dR.subs(c, sp.Rational(k, 200))) for k in range(1, 200)]
    check('R_%s increasing: dR/dc > 0 on a grid in (0,1), dR/dc = 0 at c = 1' % name, all(vv > 0 for vv in vals) and sp.simplify(dR.subs(c, 1)) == 0)
check('c->0 leading terms: R_as ~ 4 c ln(1/c), R_CZ ~ 36 c ln(1/c)',
      sp.limit(claims['as']/(c*sp.log(1/c)), c, 0) == 4 and sp.limit(claims['CZ']/(c*sp.log(1/c)), c, 0) == 36)
print('      numbers for mu0^2 = 1 GeV^2:')
want = {'as': [0.87, 0.62, 0.15], 'CZ': [0.98, 0.90, 0.48]}
for name in ['as', 'CZ']:
    vals = [float(sp.N(claims[name].subs(c, sp.Rational(1, Q2)))) for Q2 in (4, 10, 100)]
    print('      %s: Q^2 = 4, 10, 100 -> %s' % (name, ['%.4f' % w for w in vals]))
    check('numbers %s round to %s' % (name, want[name]), all(round(w, 2) == t for w, t in zip(vals, want[name])))
# Yeh (hep-ph/0107192) quotes, for the asymptotic DA, f(eps) = 1 - R(eps) "reaches 90% for eps = 1/150"
f150 = 1 - float(sp.N(claims['as'].subs(c, sp.Rational(1, 150))))
csol = sp.nsolve(claims['as'] - sp.Rational(1, 10), c, 0.006)
print('      1 - R_as(1/150) = %.4f ; R_as(c) = 0.10 at c = %.5f = 1/%.1f' % (f150, float(csol), 1/float(csol)))
check('consistent with Yeh 2001: 1 - R_as(1/150) ~ 0.9 (0.892)', abs(f150 - 0.9) < 0.01)
print('\nSUMMARY n21: %d/%d PASS' % (sum(RES), len(RES)))
