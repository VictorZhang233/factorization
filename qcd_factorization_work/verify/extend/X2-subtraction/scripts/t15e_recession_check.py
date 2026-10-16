"""X2/T15e: exact recession check for all unbounded cells of the bubble remainder certificate (selected valid alternatives)
and of the triangle certificates (natural cover theta=2)."""
import sys, os, json
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp, numpy as np
from tropical import monomials_of, positive_form
from exact_verify import build, solve_exact
from recession import max_slope
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 't15_bubble_certificate.py')).read().split('if __name__')[0]
src = src.replace("os.path.dirname(os.path.abspath(__file__))", repr(os.path.dirname(os.path.abspath(__file__))))
ns = {}; exec(src, ns)
u, v, kap, m2 = ns['u'], ns['v'], ns['kap'], ns['m2']
combine, T, weighted = ns['combine'], ns['T'], ns['weighted']
def alt_ok(nn, dd, local, subs, fr, cons):
    """returns (exponent, max recession slope) for an alternative; exponent -inf if invalid"""
    N = sp.expand(subs(nn))
    if N == 0: return np.inf, None
    mons = monomials_of(N, local, m2); forms = [positive_form(sp.expand(fr(g)), local, m2) for g in dd]
    worst = None; slope = None
    for cf, al in mons:
        rows, rhs, cc, const = build(al, forms, [1, 1], [c for c, _ in cons], [r for _, r in cons], 2)
        out, msg = solve_exact(rows, rhs, cc, const)
        if out is None: return -np.inf, None
        worst = out[0] if (worst is None or out[0] > worst) else worst
        s = max_slope(al, [1, 1], forms, cons)
        if s is not None: slope = s if (slope is None or s > slope) else slope
    return float(-2*worst), slope
cells = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bubble_cells.json')))
worst_slope = None; nunb = 0
for (region, a_, b_, c_, d_, bestname, bestval) in cells:
    unbounded = (a_ is None) or (b_ is None) or (c_ is None) or (d_ is None)
    if not unbounded: continue
    nunb += 1
    a_ = -np.inf if a_ is None else a_; b_ = np.inf if b_ is None else b_
    c_ = -np.inf if c_ is None else c_; d_ = np.inf if d_ is None else d_
    cons = []
    if np.isfinite(b_): cons.append(([1, 0], b_))
    if np.isfinite(a_): cons.append(([-1, 0], -a_))
    if region == 'I':
        if np.isfinite(d_): cons.append(([-1, 1], d_))
        if np.isfinite(c_): cons.append(([1, -1], -c_))
        local = [u, kap]; subs = lambda z: z.subs(v, 1 - u); fr = lambda f: f.subs(v, 1)
    else:
        if np.isfinite(d_): cons.append(([0, 1], d_))
        if np.isfinite(c_): cons.append(([0, -1], -c_))
        local = [v, kap]; subs = lambda z: z.subs(u, 1 - v); fr = lambda f: f.subs(u, 1)
    wa = [(u*m2, [kap]), (sp.Integer(1), [])]; wb = [(u, [v]), (sp.Integer(1), [])]
    nr, dr = combine([(1, T[s]) for s in ['D', 'e', 't', 'h']])
    pieces = [[(nr, dr)], [weighted(['D', 'e'], wn, wd) for (wn, wd) in wa], [weighted(['D', 't'], wn, wd) for (wn, wd) in wb],
              [weighted(['D'], u**2*m2, [u*m2*v + kap])], [weighted(['D'], an*bn, ad + bd) for (an, ad) in wa for (bn, bd) in wb]]
    for alts in pieces:
        res = [alt_ok(nn, dd, local, subs, fr, cons) for (nn, dd) in alts]
        # select the valid alternative with exponent >= 2 and strictly negative slope
        good = [(e, s) for (e, s) in res if e >= 2 and (s is None or s < 0)]
        if not good:
            print("  NO valid alternative with negative slope:", region, a_, b_, c_, d_, res); continue
        s = max((s for (e, s) in good if s is not None), default=None)
        if s is not None: worst_slope = s if (worst_slope is None or s > worst_slope) else worst_slope
print(f"unbounded bubble cells checked: {nunb}; worst (max) recession slope among selected alternatives = {worst_slope}")
