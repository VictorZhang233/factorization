"""X2/T15d: strict exact re-verification of all bubble remainder cells: an alternative is valid only if EVERY monomial LP
is bounded and exactly certified; the piece exponent is the max over valid alternatives."""
import sys, os, json
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp, numpy as np
from tropical import monomials_of, positive_form
from exact_verify import build, solve_exact
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 't15_bubble_certificate.py')).read().split('if __name__')[0]
src = src.replace("os.path.dirname(os.path.abspath(__file__))", repr(os.path.dirname(os.path.abspath(__file__))))
ns = {}; exec(src, ns)
u, v, kap, m2 = ns['u'], ns['v'], ns['kap'], ns['m2']
combine, T, weighted = ns['combine'], ns['T'], ns['weighted']
def strict(nn, dd, local, subs, fr, cons):
    N = sp.expand(subs(nn))
    if N == 0: return np.inf
    mons = monomials_of(N, local, m2); forms = [positive_form(sp.expand(fr(g)), local, m2) for g in dd]
    worst = None
    for cf, al in mons:
        rows, rhs, cc, const = build(al, forms, [1, 1], [c for c, _ in cons], [r for _, r in cons], 2)
        out, msg = solve_exact(rows, rhs, cc, const)
        if out is None: return -np.inf          # invalid alternative
        worst = out[0] if (worst is None or out[0] > worst) else worst
    return float(-2*worst)
cells = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bubble_cells.json')))
minexp = np.inf
for (region, a_, b_, c_, d_, bestname, bestval) in cells:
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
    cell = min(max(strict(nn, dd, local, subs, fr, cons) for (nn, dd) in alts) for alts in pieces)
    minexp = min(minexp, cell)
    if cell < 2: print("  cell below 2:", region, a_, b_, c_, d_, cell)
print(f"strict exact verification over {len(cells)} cells: minimal exponent = {minexp}")
