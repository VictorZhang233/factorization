"""X2/T17x: exact rational re-verification of the bubble-class (H1)/(H2) certificates of T17 at theta = 2."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.argv = [sys.argv[0], '2']
import sympy as sp, numpy as np
from fractions import Fraction
import t17_bubble_H1H2 as B
from tropical import monomials_of, positive_form
from exact_verify import build, solve_exact
u, v, kap, m2 = B.u, B.v, B.kap, B.m2
def expo_exact(num, dens, region, cons):
    if region == 'I':
        N = sp.expand(num.subs(v, 1 - u)); loc = [u, kap]; dl = [sp.expand(f.subs(v, 1)) for f in dens]
    else:
        N = sp.expand(num.subs(u, 1 - v)); loc = [v, kap]; dl = [sp.expand(f.subs(u, 1)) for f in dens]
    if N == 0: return np.inf, 0
    mons = monomials_of(N, loc, m2); forms = [positive_form(g, loc, m2) for g in dl]
    G = [[Fraction(x).limit_denominator(100) for x in c] for c, _ in cons]; h = [Fraction(r).limit_denominator(100) for _, r in cons]
    worst = None; fails = 0
    for c, a in mons:
        rows, rhs, cc, const = build(a, forms, [1, 1], G, h, 2)
        out, msg = solve_exact(rows, rhs, cc, const)
        if out is None: fails += 1; continue
        worst = out[0] if (worst is None or out[0] > worst) else worst
    return (-2*worst if worst is not None else np.inf), fails
def piece_exact(items, region, cons, weight=None):
    num, dens = B.combine(items)
    eL, f1 = expo_exact(num, dens, region, cons)
    if weight is None: return eL, f1
    wn, wd = B.W[weight]
    er, f2 = expo_exact(sp.expand(wn*num), list(wd) + list(dens), region, cons)
    return max(eL, er), f1 + f2
worst = np.inf; totf = 0
for U, names in B.CHECK.items():
    for nm in names:
        if nm == '(H1)_C2 G-S-C2': continue          # superseded by the 'alt' decomposition
        main, corr = B.ITEMS[nm]
        for (region, cons) in B.REGIONS[U]:
            e0, f = piece_exact(main, region, cons); totf += f; es = [e0]
            for (pair, its) in corr:
                e1, f = piece_exact(its, region, cons, weight=pair); totf += f; es.append(e1)
            e = min(es); worst = min(worst, e)
            print(f"{U:5s} {nm:18s} {region}: exact exponents {[str(x) for x in es]} -> lambda^{e}", flush=True)
print(f"exact minimal exponent (theta=2, all (H1)/(H2) items, log-insertion class): {worst}; exact-dual failures: {totf}")
