"""X2/T15c: resolve the exact-dual failures of T15b(ii) by exact vertex enumeration (2D): the max of the concave
piecewise-linear psi_a over the cell U is attained at a vertex of the arrangement formed by U's boundary lines and the
switching lines <b-b',X> = b_m - b'_m of each denominator factor; all candidates are evaluated in exact rationals.

*** INVALID (X2 fix round 1, review r1_2 Thm 3.9(d)): the four failing LPs are UNBOUNDED; a vertex maximum ignores the
recession directions, so 'resolved by exact vertex enumeration' is not a certificate (and the printed exponents -2, -4, -6
are not suppressions anyway).  The corner cell II {Xv<=-3, Xk<=-4} is handled shell by shell in t15f / r1_bubble_recert.py;
this script is kept only for the record and is not part of any proof. ***"""
import sys, os, json, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp, numpy as np
from fractions import Fraction as Fr
from tropical import monomials_of, positive_form
from exact_verify import build, solve_exact
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 't15_bubble_certificate.py')).read().split('if __name__')[0]
src = src.replace("os.path.dirname(os.path.abspath(__file__))", repr(os.path.dirname(os.path.abspath(__file__))))
ns = {}; exec(src, ns)
u, v, kap, m2 = ns['u'], ns['v'], ns['kap'], ns['m2']
combine, T, weighted = ns['combine'], ns['T'], ns['weighted']

def psi_exact(a, forms, X):
    val = Fr(int(a[0]) + 1)*X[0] + Fr(int(a[1]) + 1)*X[1] - Fr(int(a[2]))
    for fl in forms:
        val -= max(Fr(int(b[0]))*X[0] + Fr(int(b[1]))*X[1] - Fr(int(b[2])) for b in fl)
    return val

def vertex_max(a, forms, cons):
    lines = [(Fr(c[0]).limit_denominator(100), Fr(c[1]).limit_denominator(100), Fr(r).limit_denominator(100)) for c, r in cons]
    for fl in forms:
        for b1, b2 in itertools.combinations(fl, 2):
            A = Fr(int(b1[0]) - int(b2[0])); B = Fr(int(b1[1]) - int(b2[1])); C = Fr(int(b1[2]) - int(b2[2]))
            if A != 0 or B != 0: lines.append((A, B, C))
    pts = []
    for (a1, b1, c1), (a2, b2, c2) in itertools.combinations(lines, 2):
        det = a1*b2 - a2*b1
        if det == 0: continue
        X = ((c1*b2 - c2*b1)/det, (a1*c2 - a2*c1)/det)
        if all(Fr(c[0]).limit_denominator(100)*X[0] + Fr(c[1]).limit_denominator(100)*X[1] <= Fr(r).limit_denominator(100) for c, r in cons):
            pts.append(X)
    if not pts: return None
    return max(psi_exact(a, forms, X) for X in pts)

cells = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bubble_cells.json')))
nfail = 0; resolved = 0; worst = None
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
    for alts in pieces:
        for (nn, dd) in alts:
            N = sp.expand(subs(nn))
            if N == 0: continue
            mons = monomials_of(N, local, m2); forms = [positive_form(sp.expand(fr(g)), local, m2) for g in dd]
            for cf, al in mons:
                rows, rhs, cc, const = build(al, forms, [1, 1], [c for c, _ in cons], [r for _, r in cons], 2)
                out, msg = solve_exact(rows, rhs, cc, const)
                if out is None:
                    nfail += 1
                    vm = vertex_max(al, forms, cons)
                    print(f"  failure: cell {region} [{a_},{b_}]x[{c_},{d_}] monomial {al}: {msg}; exact vertex max psi = {vm} -> exponent {(-2*vm) if vm is not None else None}")
                    if vm is not None: resolved += 1
print(f"failures: {nfail}, resolved by exact vertex enumeration: {resolved}")
