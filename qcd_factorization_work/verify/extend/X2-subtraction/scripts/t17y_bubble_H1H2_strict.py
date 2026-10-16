"""X2/T17y: strict exact check (bounded exact optimum for every monomial + strictly negative recession slopes) of the
bubble-class (H1)/(H2) pieces at theta = 2; for each piece the best valid alternative is selected."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.argv = [sys.argv[0], '2']
import sympy as sp, numpy as np
from fractions import Fraction
import t17_bubble_H1H2 as B
from tropical import monomials_of, positive_form
from exact_verify import build, solve_exact
from recession import max_slope
u, v, kap, m2 = B.u, B.v, B.kap, B.m2
def strict(num, dens, region, cons):
    if region == 'I':
        N = sp.expand(num.subs(v, 1 - u)); loc = [u, kap]; dl = [sp.expand(f.subs(v, 1)) for f in dens]
    else:
        N = sp.expand(num.subs(u, 1 - v)); loc = [v, kap]; dl = [sp.expand(f.subs(u, 1)) for f in dens]
    if N == 0: return np.inf
    forms = [positive_form(g, loc, m2) for g in dl]
    G = [[Fraction(x).limit_denominator(100) for x in c] for c, _ in cons]; h = [Fraction(r).limit_denominator(100) for _, r in cons]
    worst = None
    for cf, a in monomials_of(N, loc, m2):
        rows, rhs, cc, const = build(a, forms, [1, 1], G, h, 2)
        out, msg = solve_exact(rows, rhs, cc, const)
        if out is None: return -np.inf
        s = max_slope(a, [1, 1], forms, cons)
        if s is not None and s >= 0: return -np.inf
        worst = out[0] if (worst is None or out[0] > worst) else worst
    return float(-2*worst)
def piece(items, region, cons, weight=None):
    num, dens = B.combine(items)
    alts = [strict(num, dens, region, cons)]
    if weight is not None:
        wn, wd = B.W[weight]
        alts.append(strict(sp.expand(wn*num), list(wd) + list(dens), region, cons))
    return max(alts)
worst = np.inf
for U, names in B.CHECK.items():
    for nm in names:
        if nm == '(H1)_C2 G-S-C2': continue
        main, corr = B.ITEMS[nm]
        for (region, cons) in B.REGIONS[U]:
            es = [piece(main, region, cons)] + [piece(its, region, cons, weight=pair) for (pair, its) in corr]
            e = min(es); worst = min(worst, e)
            print(f"{U:5s} {nm:18s} {region}: {es} -> lambda^{e}", flush=True)
print("strict minimal exponent (theta=2):", worst)
