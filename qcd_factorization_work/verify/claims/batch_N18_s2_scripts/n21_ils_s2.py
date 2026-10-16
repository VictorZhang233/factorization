# N21 (stage-2 verifier): Isgur-Llewellyn Smith soft fractions by a DIFFERENT method:
# R(c) = P(U V < c) for iid U, V with density f(u) ∝ phi(1-u)/u  (u = xbar, v = ybar), computed through the
# Mellin transform: M_W(s) = M_U(s)^2 is rational, the density of W = UV is the sum of residues of M_W(s) w^{-s}
# (double poles at s = 0, -1, -2, ...), and R(c) = int_0^c f_W.  Cross-checked by 1D mpmath quadrature of
# int f(u) F(c/u) du (CDF form) and by Monte Carlo.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
import numpy as np
res = []
def check(name, cond, info=''):
    res.append(bool(cond)); print(('PASS ' if cond else 'FAIL ') + name + (('   [' + info + ']') if info else ''))

u, s, w, c = sp.symbols('u s w c', positive=True)
x = sp.symbols('x')
phis = {'as': 6*x*(1 - x), 'CZ': 30*x*(1 - x)*(2*x - 1)**2}
claims = {'as': c*(5*c - 2*(c + 2)*sp.log(c) - 4),
          'CZ': c*(456*c**3 + 352*c**2 - 675*c - 132 - (144*c**3 + 768*c**2 + 450*c + 36)*sp.log(c))}
Rfun = {}
for name, phi in phis.items():
    check('%s DA normalised: int phi = 1' % name, sp.integrate(phi, (x, 0, 1)) == 1)
    g = sp.expand(sp.simplify((phi/(1 - x)).subs(x, 1 - u)))      # phi(x)/xbar at x = 1-u, a polynomial in u
    Z = sp.integrate(g, (u, 0, 1)); f = sp.expand(g/Z)
    print('   %s: density of u = xbar: f(u) = %s   (normalisation int phi/xbar = %s)' % (name, f, Z))
    M = sp.simplify(sp.integrate(f*u**(s - 1), (u, 0, 1), conds='none'))
    M = sp.factor(sp.together(M))
    MW = sp.factor(M**2)
    poles = sorted(set(sp.roots(sp.denom(sp.together(MW)), s).keys()))
    fW = 0
    for p0 in poles:
        fW += sp.residue(MW*w**(-s), s, p0)
    fW = sp.simplify(sp.expand(fW))
    check('%s: density of W = UV integrates to 1' % name, sp.simplify(sp.integrate(fW, (w, 0, 1)) - 1) == 0)
    R = sp.simplify(sp.integrate(fW, (w, 0, c)))
    Rfun[name] = R
    check('%s: Mellin/residue result R(c) equals the claimed closed form' % name, sp.simplify(sp.expand(R - claims[name])) == 0,
          'R = %s' % sp.factor(sp.expand(R)))
    check('%s: R(1) = 1' % name, sp.simplify(R.subs(c, 1) - 1) == 0)
    dR = sp.simplify(sp.diff(R, c))
    check('%s: dR/dc = f_W(c) >= 0 (monotonic) and dR/dc(1) = 0' % name,
          sp.simplify(dR.subs(c, 1)) == 0 and all(float(dR.subs(c, cv)) >= 0 for cv in np.linspace(1e-4, 0.9999, 400)))
    # small-c asymptotics: R ~ f(0)^2 c ln(1/c)
    lead = sp.limit(R/(c*sp.log(1/c)), c, 0)
    check('%s: R(c) ~ %s c ln(1/c) as c->0 (= f(0)^2 = %s)' % (name, lead, f.subs(u, 0)**2), lead == f.subs(u, 0)**2)
# independent 1D quadrature (CDF form) and Monte Carlo
mp.mp.dps = 30
def R_quad(phi_expr, cv):
    g = sp.lambdify(u, sp.expand((phi_expr/(1 - x)).subs(x, 1 - u)), 'mpmath')
    Z = mp.quad(g, [0, 1])
    F = lambda t: mp.quad(g, [0, min(t, 1)])/Z
    return mp.quad(lambda uu: g(uu)/Z*F(cv/uu), [0, cv, 1])
for name in phis:
    for cv in (mp.mpf('0.25'), mp.mpf('0.1'), mp.mpf('0.01'), mp.mpf(1)/150):
        q = R_quad(phis[name], cv); a = mp.mpf(sp.N(Rfun[name].subs(c, sp.Rational(str(cv)) if cv != mp.mpf(1)/150 else sp.Rational(1, 150)), 30))
        check('%s: 1D quadrature of int f(u)F(c/u)du = closed form at c=%s (%s)' % (name, mp.nstr(cv, 4), mp.nstr(q, 10)), abs(q - a) < 1e-20)
rng = np.random.default_rng(7)
nmc = 2_000_000
# sample u with density 2(1-u): u = 1 - sqrt(1-U)
U1 = 1 - np.sqrt(1 - rng.random(nmc)); U2 = 1 - np.sqrt(1 - rng.random(nmc))
for cv in (0.25, 0.1, 0.01):
    mc = np.mean(U1*U2 < cv); ex = float(Rfun['as'].subs(c, cv))
    check('as: Monte Carlo P(UV<c) at c=%.2f: %.4f vs %.4f' % (cv, mc, ex), abs(mc - ex) < 5*np.sqrt(ex*(1 - ex)/nmc))
# numbers quoted in the claim
print('   mu0^2 = 1 GeV^2:  Q^2      R_as        R_CZ')
vals = {}
for Q2 in (4, 10, 100):
    ra = float(Rfun['as'].subs(c, sp.Rational(1, Q2))); rc = float(Rfun['CZ'].subs(c, sp.Rational(1, Q2)))
    vals[Q2] = (ra, rc); print('                    %5d   %.6f   %.6f' % (Q2, ra, rc))
check('quoted numbers 0.87, 0.62, 0.15 (as) and 0.98, 0.90, 0.48 (CZ) are the correct roundings',
      [round(vals[q][0], 2) for q in (4, 10, 100)] == [0.87, 0.62, 0.15] and [round(vals[q][1], 2) for q in (4, 10, 100)] == [0.98, 0.90, 0.48])
# ILS fraction function f(eps) = 1 - R(eps): Yeh 2001 quotes "90% at eps = 1/150" for AS
fe = 1 - float(Rfun['as'].subs(c, sp.Rational(1, 150)))
check('ILS fraction f(eps)=1-R_as(eps) at eps=1/150 = %.4f, consistent with Yeh 2001 "90%%"' % fe, abs(fe - 0.9) < 0.01)
print('\nSUMMARY: %d/%d checks passed' % (sum(res), len(res)))
