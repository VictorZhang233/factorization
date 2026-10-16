"""X2 final2 -- f2v_conv_intervals.py: EXACT pure-DR (delta = 0) convergence intervals of projective (Feynman)
parametric integrals  J(eps) = int_{simplex} x^{a-1} U^{|a|-3t} F^{2t-|a|},  t = d/2 = 2 - eps,  a = (1,...,1),
for the full planar and crossed two-loop vertex of (M1) (Prop E.5) and for the singles HH and SS (Prop E.4(e)).

Criterion (Lemma E.6 of the report): U, F have positive coefficients, so the integrand is comparable to
exp(psi_eps(X)) in log coordinates, psi_eps(r) = <1,r> + 3 eps h_U(r) - (2 + 2 eps) h_F(r); psi is linear on every cone
of the normal fan of the Minkowski sum N = Newt(U) + Newt(F); hence J converges iff psi_eps(r_k) < 0 for every OUTER
facet normal r_k of N (taken in the 5-dimensional affine hull of N; r is defined modulo (1,...,1)).
Each condition reads A_k + eps B_k < 0, A_k = <1,r_k> - 2 h_F(r_k), B_k = 3 h_U(r_k) - 2 h_F(r_k): the convergence set is
an exact open interval.
Facets: scipy ConvexHull (Qhull) on the projected points, then EXACT verification of every facet (rational normal, all
points on one side) and a COMPLETENESS CERTIFICATE: every ridge of every facet (computed from the facet's own hull and
verified exactly) is contained in exactly two facets of the list.
Input polynomials: f2v_UF_polytopes.json (singles) and recomputed here for the full vertices (same code as f2v_*).
Run: python3 -I f2v_conv_intervals.py  (log: ../final2_logs/f2v_conv_intervals.log)"""
import sys, os, json, itertools
from fractions import Fraction as Fr
from math import gcd
from functools import reduce
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from scipy.spatial import ConvexHull
import sympy as sp
import functools
print = functools.partial(print, flush=True)
HERE = os.path.dirname(os.path.abspath(__file__))
LOGDIR = os.path.join(os.path.dirname(HERE), 'final2_logs')
sys.path.insert(0, HERE)
import f2v_UF_polytopes as V   # independent f2v code (U, F of the full vertices)  -- re-runs its checks on import

ALL_OK = True
def report(name, ok):
    global ALL_OK
    ALL_OK &= bool(ok)
    print(f"   [{'PASS' if ok else 'FAIL'}] {name}")

def rank_q(rows):
    M = [[Fr(v) for v in r] for r in rows]; rk = 0; ncol = len(M[0]) if M else 0
    for col in range(ncol):
        piv = next((i for i in range(rk, len(M)) if M[i][col] != 0), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]
        for i in range(len(M)):
            if i != rk and M[i][col] != 0:
                f = M[i][col]/M[rk][col]; M[i] = [a - f*b for a, b in zip(M[i], M[rk])]
        rk += 1
    return rk
def affdim(pts): return 0 if len(pts) < 2 else rank_q([[a - b for a, b in zip(p, pts[0])] for p in pts[1:]])
def kernel_q(rows, n):
    M = [[Fr(v) for v in r] for r in rows]; piv = []; rk = 0
    for col in range(n):
        p_ = next((i for i in range(rk, len(M)) if M[i][col] != 0), None)
        if p_ is None: continue
        M[rk], M[p_] = M[p_], M[rk]; pv = M[rk][col]; M[rk] = [a/pv for a in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][col] != 0:
                f = M[i][col]; M[i] = [a - f*b for a, b in zip(M[i], M[rk])]
        piv.append(col); rk += 1
    free = [c for c in range(n) if c not in piv]; basis = []
    for fc in free:
        y = [Fr(0)]*n; y[fc] = Fr(1)
        for r, pc in enumerate(piv): y[pc] = -M[r][fc]
        basis.append(y)
    return basis
def primitive(v):
    den = reduce(lambda a, b: a*b//gcd(a, b), [Fr(x).denominator for x in v], 1)
    iv = [int(Fr(x)*den) for x in v]; g = reduce(gcd, [abs(x) for x in iv if x != 0], 0) or 1
    return tuple(x//g for x in iv)

def hull_facets_exact(pts):
    """pts: list of integer tuples spanning an affine space of dim n (= len(pts[0]) is NOT assumed; we project).
    Returns list of (inward normal in ambient coords, nu, frozenset of point indices on the facet), exact."""
    P0 = pts[0]; D = [[a - b for a, b in zip(p, P0)] for p in pts]
    n = affdim(pts); amb = len(pts[0])
    # choose n coordinates on which the projection is injective on the affine hull
    for cols in itertools.combinations(range(amb), n):
        if rank_q([[d[c] for c in cols] for d in D]) == n: break
    proj = np.array([[d[c] for c in cols] for d in D], float)
    hull = ConvexHull(proj, qhull_options='Qt')
    # linear relations that hold on the affine hull (to lift normals): affine hull directions
    facets = {}
    for simp in hull.simplices:
        Q = [D[i] for i in simp]
        if affdim(Q) != n - 1: continue
        # normal within the affine hull: mu in ambient space, orthogonality to the facet directions and defined modulo
        # the orthogonal complement of the affine hull; take mu as a functional on the projected coordinates
        rows = [[q[c] - Q[0][c] for c in cols] for q in Q[1:]]
        ker = kernel_q(rows, n)
        if len(ker) != 1: continue
        mu_p = primitive(ker[0])
        vals = [sum(m*d[c] for m, c in zip(mu_p, cols)) for d in D]
        v0 = sum(m*Q[0][c] for m, c in zip(mu_p, cols))
        if all(v >= v0 for v in vals): pass
        elif all(v <= v0 for v in vals): mu_p = tuple(-m for m in mu_p); vals = [-v for v in vals]; v0 = -v0
        else: continue
        on = frozenset(i for i, v in enumerate(vals) if v == v0)
        mu_amb = [0]*amb
        for m, c in zip(mu_p, cols): mu_amb[c] = m
        nu = sum(a*b for a, b in zip(mu_amb, P0)) + v0
        facets[on] = (tuple(mu_amb), nu)
    return [(mu, nu, on) for on, (mu, nu) in facets.items()], n, cols

def ridges_of(pts_idx, pts, n):
    """ridges (as frozensets of indices) of the (n-1)-dim polytope conv(pts[i] for i in pts_idx)"""
    sub = [pts[i] for i in sorted(pts_idx)]
    fl, m, _ = hull_facets_exact(sub)
    assert m == n - 1
    idx = sorted(pts_idx)
    return [frozenset(idx[j] for j in on) for _, _, on in fl]

def minkowski_facets(SU, SF):
    S = sorted(set(tuple(a + b for a, b in zip(u, f)) for u in SU for f in SF))
    fl, n, cols = hull_facets_exact(S)
    # completeness certificate: each ridge of each facet lies in exactly two facets
    count = {}
    for mu, nu, on in fl:
        for rdg in ridges_of(on, S, n):
            count[rdg] = count.get(rdg, 0) + 1
    complete = all(c == 2 for c in count.values())
    return S, fl, n, complete, len(count)

def h(S, r): return max(sum(a*b for a, b in zip(v, r)) for v in S)

def interval(SU, SF, label):
    S, fl, n, complete, nr = minkowski_facets(SU, SF)
    lo, hi = Fr(-10**9), Fr(10**9); empty = False; bind_lo = bind_hi = None
    for mu, nu, on in fl:
        r = tuple(-m for m in mu)                         # outer normal
        A = sum(r) - 2*h(SF, r); B = 3*h(SU, r) - 2*h(SF, r)
        if B > 0:
            if Fr(-A, B) < hi: hi = Fr(-A, B); bind_hi = r
        elif B < 0:
            if Fr(-A, B) > lo: lo = Fr(-A, B); bind_lo = r
        elif A >= 0: empty = True
    ok = complete and n == 5
    res = None if (empty or lo >= hi) else (lo, hi)
    report(f"{label}: |N points| = {len(S)}, dim N = {n}, facets = {len(fl)}, ridges = {nr}, completeness certificate: "
           f"{complete}; exact convergence set of J at delta = 0: {('(' + str(res[0]) + ', ' + str(res[1]) + ')') if res else 'EMPTY'}"
           f"{'' if not res else '  [binding outer normals: lo ' + str(bind_lo) + ', hi ' + str(bind_hi) + ']'}", ok)
    return res

print("\n================ exact convergence intervals (f2v_conv_intervals.py) ================")
res = {}
for kind in ['planar', 'crossed']:
    d = V.FULL[kind]
    res[kind] = interval(d['SU'], d['SF'], f"full {kind} vertex")
    if res[kind]:
        report(f"full {kind} vertex: [0, 1/108] is contained in the exact interval {res[kind]}",
               res[kind][0] < 0 and res[kind][1] > Fr(1, 108))
for R in ['HH', 'SS', 'HC1', 'C1C1', 'HS', 'C1S']:
    d = V.SDATA[R]
    res[R] = interval(d['SU'], d['SF'], f"single {R}")
report("HH: (Schwinger form = J-interval intersected with w = 2 + 2 eps > 0) = (-1, 0)",
       res['HH'] is not None and max(res['HH'][0], Fr(-1)) == -1 and res['HH'][1] == 0)
report("SS: J-interval = (0, 1)", res['SS'] == (Fr(0), Fr(1)))
report("HC1, C1C1, HS, C1S: no eps (empty)", all(res[R] is None for R in ['HC1', 'C1C1', 'HS', 'C1S']))
print("\nALL CHECKS PASS (f2v_conv_intervals)" if ALL_OK else "\nSOME CHECK FAILED (f2v_conv_intervals)")
