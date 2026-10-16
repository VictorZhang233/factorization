"""Spec v2.1 checks for the VF entries added in v2.1 (log: vf_v21_checks.log).
Run: python3 -I vf_v21_checks.py

E1  VF-EXC-14: Isgur-Llewellyn Smith soft fraction of the LO pion form factor (u-line integral),
    R(c) = int_{xbar*ybar < c} phi(x)phi(y)/(xbar ybar) / int phi(x)phi(y)/(xbar ybar),  c = mu0^2/Q^2 <= 1,
    for the asymptotic DA 6 x xbar and the CZ DA 30 x xbar (2x-1)^2: exact closed forms, R(1)=1, small-c behaviour,
    numbers at mu0^2 = 1 GeV^2; cross-check by direct 2D numerical quadrature.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np

log = []
def chk(name, ok, info=''):
    log.append('%s %s %s' % ('PASS' if ok else 'FAIL', name, info))

u, v, c = sp.symbols('u v c', positive=True)
def R_exact(g):
    # g(u) = phi(x)/xbar with u = xbar; soft region u*v < c, 0 < c <= 1
    inner_full = sp.integrate(g.subs(u, v), (v, 0, 1))
    part1 = sp.integrate(g * inner_full, (u, 0, c))
    inner_cut = sp.integrate(g.subs(u, v), (v, 0, c / u))
    part2 = sp.integrate(sp.expand(g * inner_cut), (u, c, 1))
    total = inner_full ** 2
    return sp.simplify((part1 + part2) / total)

g_as = 6 * (1 - u)                      # phi_as(x)/xbar = 6x, x = 1-u
g_cz = 30 * (1 - u) * (1 - 2 * u) ** 2  # phi_CZ(x)/xbar = 30 x (2x-1)^2
R_as = R_exact(g_as)
R_cz = R_exact(g_cz)
R_as_claim = c * (5 * c - 2 * (c + 2) * sp.log(c) - 4)
R_cz_claim = c * (456 * c**3 + 352 * c**2 - 675 * c - 132 - (144 * c**3 + 768 * c**2 + 450 * c + 36) * sp.log(c))
chk('E1a R_as closed form', sp.simplify(sp.expand(R_as - R_as_claim)) == 0, str(sp.factor(R_as)))
chk('E1b R_CZ closed form', sp.simplify(sp.expand(R_cz - R_cz_claim)) == 0, '')
chk('E1c R(1)=1 (both)', sp.simplify(R_as_claim.subs(c, 1)) == 1 and sp.simplify(R_cz_claim.subs(c, 1)) == 1)
lim_as = sp.limit(R_as_claim / (c * sp.log(1 / c)), c, 0, '+')
lim_cz = sp.limit(R_cz_claim / (c * sp.log(1 / c)), c, 0, '+')
chk('E1d small c: R_as ~ 4 c ln(1/c), R_CZ ~ 36 c ln(1/c)', lim_as == 4 and lim_cz == 36, 'limits %s %s' % (lim_as, lim_cz))
fa = sp.lambdify(c, R_as_claim, 'math'); fz = sp.lambdify(c, R_cz_claim, 'math')
vals = [(Q2, fa(1.0 / Q2), fz(1.0 / Q2)) for Q2 in (4.0, 10.0, 100.0)]
exp_as = (0.87, 0.62, 0.15); exp_cz = (0.98, 0.90, 0.48)
ok = all(abs(round(a, 2) - e) < 1e-9 for (_, a, _), e in zip(vals, exp_as)) and all(abs(round(z, 2) - e) < 1e-9 for (_, _, z), e in zip(vals, exp_cz))
chk('E1e numbers at mu0^2=1 GeV^2, Q^2=4,10,100', ok, ' '.join('Q2=%g: R_as=%.4f R_CZ=%.4f' % x for x in vals))
# monotonicity on (0,1]: in double precision the closed forms lose ~1e-13 near c = 1 (large cancelling terms, and
# R'(1) = 0), so the check uses 40-digit arithmetic
import mpmath as mp
mp.mp.dps = 40
fam = sp.lambdify(c, R_as_claim, 'mpmath'); fzm = sp.lambdify(c, R_cz_claim, 'mpmath')
grid = [mp.mpf(k) / 2000 for k in range(1, 2001)]
ra = [fam(x) for x in grid]; rz = [fzm(x) for x in grid]
mono = all(ra[i + 1] > ra[i] for i in range(len(ra) - 1)) and all(rz[i + 1] > rz[i] for i in range(len(rz) - 1))
bounds = min(ra) > 0 and min(rz) > 0 and max(ra) <= 1 and max(rz) <= 1
dR1 = (mp.diff(fam, 1), mp.diff(fzm, 1))
chk('E1f R strictly increasing on (0,1], 0<R<=1 (40 digits), R\'(1)=0', mono and bounds and all(abs(d) < mp.mpf(10) ** -30 for d in dR1),
    "R'(1) = %s, %s" % (mp.nstr(dR1[0], 5), mp.nstr(dR1[1], 5)))
# direct numerical quadrature (midpoint grid) at c = 0.1 (independent of the symbolic route)
N = 4000
gr = (np.arange(N) + 0.5) / N
U, V = np.meshgrid(gr, gr, indexing='ij')
for name, gf, f in (('as', lambda w: 6 * (1 - w), fa), ('CZ', lambda w: 30 * (1 - w) * (1 - 2 * w) ** 2, fz)):
    W2 = gf(U) * gf(V)
    num = W2[U * V < 0.1].sum() / W2.sum()
    chk('E1g quadrature R_%s(0.1)' % name, abs(num - f(0.1)) < 2e-3, 'grid %.5f closed %.5f' % (num, f(0.1)))

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vf_v21_checks.log')
npass = sum(1 for l in log if l.startswith('PASS'))
log.append('RESULT: %d/%d pass' % (npass, len(log)))
open(out, 'w').write('\n'.join(log) + '\n')
print('\n'.join(log))
