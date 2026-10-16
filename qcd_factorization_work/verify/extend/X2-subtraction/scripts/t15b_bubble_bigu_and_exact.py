"""X2/T15b: bubble class, (i) region u>1 (shells e,h only): rho^(j) = sum_n C(j,n) l_h^{j-n} a^n T_e + l_h^j rho_r;
pieces rho_r and w_a |T_e|; (ii) exact rational re-verification (dual certificates) of every LP used in T15 and here."""
import sys, os, json
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp, numpy as np
from fractions import Fraction
from tropical import monomials_of, positive_form
from exact_verify import build, solve_exact
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 't15_bubble_certificate.py')).read().split('if __name__')[0]
src = src.replace("os.path.dirname(os.path.abspath(__file__))", repr(os.path.dirname(os.path.abspath(__file__))))
ns = {}; exec(src, ns)
u, v, kap, m2 = ns['u'], ns['v'], ns['kap'], ns['m2']
combine, T = ns['combine'], ns['T']

def exact_exponent(num, dens, local, subsfun, cons):
    N = sp.expand(subsfun(num))
    if N == 0: return None, 0
    dl = [sp.expand(ns_sub(f, local)) for f in dens]
    mons = monomials_of(N, local, m2)
    forms = [positive_form(g, local, m2) for g in dl]
    G = [list(c) for c, _ in cons]; h = [r for _, r in cons]
    worst = None; fails = 0
    for c, a in mons:
        rows, rhs, cc, const = build(a, forms, [1]*len(local), G, h, len(local))
        out, msg = solve_exact(rows, rhs, cc, const)
        if out is None:
            fails += 1; continue
        val = out[0]
        worst = val if (worst is None or val > worst) else worst
    return (None if worst is None else -2*worst), fails

def ns_sub(f, local):
    g = f
    if u not in local: g = g.subs(u, 1)
    if v not in local: g = g.subs(v, 1)
    return g

# (i) region u > 1 (no v): T_e, T_h as in T15 but with v-free forms; rho_r(u>1) = T_e + T_h
Te = (m2, [u, m2 + u, u*m2 + kap]); Th = T['h']
y_edges = [-np.inf, -4, -3, -2, -1.5, -1.25, -1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 1, 2, np.inf]
x_edges = [0, 0.25, 0.5, 1, np.inf]
minexp = np.inf; tot_fail = 0
for (a, b) in zip(x_edges[:-1], x_edges[1:]):
    for (c, d) in zip(y_edges[:-1], y_edges[1:]):
        cons = [([-1, 0], -a)]
        if np.isfinite(b): cons.append(([1, 0], b))
        if np.isfinite(d): cons.append(([-1, 1], d))
        if np.isfinite(c): cons.append(([1, -1], -c))
        nr, dr = combine([(1, Te), (1, Th)])
        e0, f0 = exact_exponent(nr, dr, [u, kap], lambda z: z, cons)
        best1 = None
        for (wn, wd) in [(u*m2, [kap]), (sp.Integer(1), [])]:
            e1, f1 = exact_exponent(sp.expand(wn*Te[0]), list(wd) + list(Te[1]), [u, kap], lambda z: z, cons)
            tot_fail += f1
            if e1 is not None and (best1 is None or e1 > best1): best1 = e1
        tot_fail += f0
        cell = min(x for x in [e0, best1] if x is not None)
        minexp = min(minexp, cell)
        if cell < 2: print("  u>1 cell below 2:", a, b, c, d, e0, best1)
print(f"(i) region u>1: minimal exact exponent over cells = {minexp}, exact-dual failures = {tot_fail}")

# (ii) exact re-verification of all 0<u<1 cells of T15
cells = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bubble_cells.json')))
weighted = ns['weighted']
minexp2 = np.inf; fails2 = 0; ncell = 0
for (region, a, b, c, d, bestname, bestval) in cells:
    a = -np.inf if a is None else a; b = np.inf if b is None else b
    c = -np.inf if c is None else c; d = np.inf if d is None else d
    cons = []
    if np.isfinite(b): cons.append(([1, 0], b))
    if np.isfinite(a): cons.append(([-1, 0], -a))
    if region == 'I':
        if np.isfinite(d): cons.append(([-1, 1], d))
        if np.isfinite(c): cons.append(([1, -1], -c))
        local = [u, kap]; subs = lambda z: z.subs(v, 1 - u)
    else:
        if np.isfinite(d): cons.append(([0, 1], d))
        if np.isfinite(c): cons.append(([0, -1], -c))
        local = [v, kap]; subs = lambda z: z.subs(u, 1 - v)
    pieces = []
    nr, dr = combine([(1, T[s]) for s in ['D', 'e', 't', 'h']]); pieces.append([(nr, dr)])
    wa = [(u*m2, [kap]), (sp.Integer(1), [])]; wb = [(u, [v]), (sp.Integer(1), [])]
    pieces.append([weighted(['D', 'e'], wn, wd) for (wn, wd) in wa])
    pieces.append([weighted(['D', 't'], wn, wd) for (wn, wd) in wb])
    pieces.append([weighted(['D'], u**2*m2, [u*m2*v + kap])])
    pieces.append([weighted(['D'], an*bn, ad + bd) for (an, ad) in wa for (bn, bd) in wb])
    cellmin = np.inf
    for alts in pieces:
        best = None
        for (nn, dd) in alts:
            e_, f_ = exact_exponent(nn, dd, local, subs, cons); fails2 += f_
            if e_ is None: e_ = np.inf
            best = e_ if (best is None or e_ > best) else best
        cellmin = min(cellmin, best)
    minexp2 = min(minexp2, cellmin); ncell += 1
    if cellmin < 2: print("  cell below 2 (exact):", region, a, b, c, d, cellmin)
print(f"(ii) exact re-verification of {ncell} cells (0<u<1): minimal exact exponent = {minexp2}; exact-dual failures = {fails2}")
