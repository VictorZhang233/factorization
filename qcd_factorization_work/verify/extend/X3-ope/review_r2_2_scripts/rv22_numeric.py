"""
rv22_numeric.py -- independent numerical checks by adversarial reviewer #2 (round 2) of the revised X3 report.
Written from scratch; imports nothing from the X3 scripts.

(F) Theorem F / Lemma F.6(d): for w in the cut plane C = C \ ((-inf,-1] u [1,inf)) the coefficient set
    {1, 1+w, 1-w} lies in an open half-plane (open strongly convex cone), including |Re w| > 1, Im w != 0;
    it fails on the cuts.  (grid scan; the margin is the opening angle < pi.)
(G) Corollary F.2(b): for random Euclidean q = (i q4, qvec) and real light-like p:
    |omega| <= 2 sqrt2 p0/|q|  and  |Phat|_E <= 2 sqrt2 p0 (< 3 p0).
(W) Prop 5.6 step 6': local wedge in (w, Q^2).  Exact Im s for s^2 = w^2 + Q^2 vs. the first-order cone
    |eta_Q + 2 x eta_w| < 2 sqrt(x^2+Q^2) eta_w; the fixed-Q^2 approach (1,0) and the 4D approach
    (x+i eta, Q^2+eta^2-2 i x eta) both satisfy the exact tube condition |Im s| < Im w for small eta.
(H) Lemma F.6(b),(c) by brute force, independent of qhull and of matroid theory: supports of U and F0hat from
    direct enumeration of spanning trees / J1-J2-separating 2-forests; full-dimensionality vs. the criterion
    "G0 = G + J1J2 loopless and 2-connected"; all facets by exhaustive search over N-subsets of support points,
    exact integer verification; claim: d_u = min <u,x> = 0 only for coordinate facets.
Run: python3 -I rv22_numeric.py
"""
import sys, os, itertools, random, math
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from fractions import Fraction

rng = np.random.default_rng(20261011)

# ------------------------------------------------------------------ (F) half-plane property
def max_gap_angle(zs):
    """largest angular gap between the arguments of the complex numbers zs; they lie in an open half-plane iff
    the largest gap exceeds pi"""
    a = sorted(np.angle(zs))
    gaps = [a[i + 1] - a[i] for i in range(len(a) - 1)] + [a[0] + 2 * np.pi - a[-1]]
    return max(gaps)

worst = 10.0
bad = 0
for x in np.linspace(-6, 6, 241):
    for y in np.concatenate([-np.logspace(-6, 1, 60), np.logspace(-6, 1, 60)]):
        wv = complex(x, y)
        g = max_gap_angle(np.array([1.0, 1 + wv, 1 - wv]))
        worst = min(worst, g - np.pi)
        if g <= np.pi:
            bad += 1
on_cut = [max_gap_angle(np.array([1.0, 1 + t, 1 - t])) > np.pi for t in (1.5, 3.0, -2.0)]
print("(F) grid points off the real axis violating the half-plane property:", bad,
      "; min (largest gap - pi) =", "%.3e" % worst, "(>0: open half-plane)")
print("(F) on the cut (w = 1.5, 3, -2): half-plane property holds?", on_cut, "(expected all False)")
okF = (bad == 0) and (not any(on_cut))

# ------------------------------------------------------------------ (G) Corollary F.2(b) constants
okG = True
mx_w, mx_P = 0.0, 0.0
for _ in range(20000):
    p0 = 1.0
    nvec = rng.normal(size=3); nvec /= np.linalg.norm(nvec)
    p = np.array([p0, *(p0 * nvec)])                        # light-like, metric (+,-,-,-)
    qE = rng.normal(size=4) * 10 ** rng.uniform(0, 3)      # Euclidean components (q4, qvec)
    q = np.array([1j * qE[0], qE[1], qE[2], qE[3]])       # q^0 = i q4
    mdot = lambda a, b: a[0] * b[0] - a[1] * b[1] - a[2] * b[2] - a[3] * b[3]
    Q2 = -mdot(q, q)                                        # = q4^2 + |qvec|^2 > 0
    nrm = np.sqrt(np.sum(np.abs(qE) ** 2))
    om = 2 * mdot(p, q) / Q2
    Phat = p - (mdot(p, q) / mdot(q, q)) * q
    r_w = abs(om) * nrm / (2 * np.sqrt(2) * p0)
    r_P = np.sqrt(np.sum(np.abs(Phat) ** 2)) / (2 * np.sqrt(2) * p0)
    mx_w, mx_P = max(mx_w, r_w), max(mx_P, r_P)
    okG = okG and abs(Q2.imag) < 1e-9 * abs(Q2) and r_w <= 1 + 1e-12 and r_P <= 1 + 1e-12
print("(G) max |omega| |q| / (2 sqrt2 p0) = %.6f ; max |Phat|_E / (2 sqrt2 p0) = %.6f  (both <= 1): %s" % (mx_w, mx_P, okG))

# ------------------------------------------------------------------ (W) local wedge of Prop 5.6 step 6'
okW = True
for x in (-3.0, -0.7, 0.0, 0.4, 2.5):
    for Q2r in (0.3, 1.0, 4.0):
        s0 = np.sqrt(x * x + Q2r)
        for (dw, dQ) in ((1.0, 0.0), (1.0, -2 * x), (1.0, 0.5 * (2 * s0 - 2 * x) - 0.3), (1.0, -0.5 * (2 * s0 + 2 * x) + 0.3)):
            lin = abs(dQ + 2 * x * dw) < 2 * s0 * dw            # first-order cone
            for eta in (1e-3, 1e-5):
                wv = complex(x, eta * dw)
                if (dw, dQ) == (1.0, -2 * x):                     # exact 4D approach: Q^2 = s0^2 - (x + i eta)^2
                    Qc = s0 ** 2 - wv ** 2
                else:
                    Qc = complex(Q2r, eta * dQ)
                s = np.sqrt(wv ** 2 + Qc)
                if s.real < 0:
                    s = -s
                exact = abs(s.imag) < wv.imag
                okW = okW and (exact == lin)
print("(W) exact tube condition |Im s| < Im w agrees with the first-order cone (incl. the 4D approach (1,-2x),"
      " which gives Im s = 0 exactly) on all test points:", okW)

# ------------------------------------------------------------------ (H) Lemma F.6 by brute force
def components(nv, es):
    par = list(range(nv))
    def f(a):
        while par[a] != a:
            par[a] = par[par[a]]; a = par[a]
        return a
    for (u, v) in es:
        par[f(u)] = f(v)
    return [f(a) for a in range(nv)]

def supports(nv, edges, J1, J2):
    """supp U (complements of spanning trees) and supp F0hat (complements of spanning 2-forests separating J1,J2)"""
    N = len(edges)
    L = N - nv + 1
    SU, SF = set(), set()
    for T in itertools.combinations(range(N), nv - 1):
        comp = components(nv, [edges[i] for i in T])
        if len(set(comp)) == 1:
            SU.add(tuple(0 if i in T else 1 for i in range(N)))
    for T in itertools.combinations(range(N), nv - 2):
        comp = components(nv, [edges[i] for i in T])
        if len(set(comp)) == 2 and comp[J1] != comp[J2]:
            SF.add(tuple(0 if i in T else 1 for i in range(N)))
    return SU, SF, L

def two_connected_loopless(nv, edges):
    if any(u == v for (u, v) in edges) or len(edges) < 2:
        return False
    used = sorted({a for e in edges for a in e})
    if len(set(components(nv, edges)[a] for a in used)) != 1:
        return False
    for wv in used:
        rest = [(u, v) for (u, v) in edges if u != wv and v != wv]
        others = [a for a in used if a != wv]
        comp = components(nv, rest)
        if len(set(comp[a] for a in others)) > 1:
            return False
    return True

def exact_rank(rows):
    M = [[Fraction(x) for x in r] for r in rows]
    rk, nc = 0, (len(M[0]) if M else 0)
    for c in range(nc):
        piv = next((r for r in range(rk, len(M)) if M[r][c] != 0), None)
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        for r in range(len(M)):
            if r != rk and M[r][c] != 0:
                fct = M[r][c] / M[rk][c]
                M[r] = [a - fct * b for a, b in zip(M[r], M[rk])]
        rk += 1
    return rk

def brute_facets(pts):
    """all facets of the full-dimensional polytope conv(pts) in R^N, by exhaustive search over N-subsets;
    returns {primitive integer inward normal: d}"""
    P = np.array(pts, dtype=float)
    n = P.shape[1]
    facets = {}
    idx_all = range(len(pts))
    for S in itertools.combinations(idx_all, n):
        A = P[list(S[1:])] - P[S[0]]
        if np.linalg.matrix_rank(A) < n - 1:
            continue
        u = np.linalg.svd(A)[2][-1]
        k = np.argmax(np.abs(u))
        u = u / u[k]
        # rationalise: entries of facet normals of 0/1 polytopes in low dimension are small rationals
        fr = [Fraction(x).limit_denominator(60) for x in u]
        den = math.lcm(*[f.denominator for f in fr])
        ui = [int(f * den) for f in fr]
        g = math.gcd(*ui)
        ui = [a // g for a in ui]
        vals = [sum(a * b for a, b in zip(ui, p)) for p in pts]
        mn, mxv = min(vals), max(vals)
        for sgn, dd in ((1, mn), (-1, -mxv)):
            uu = tuple(sgn * a for a in ui)
            vv = [sgn * v for v in vals]
            if min(vv) != dd:
                continue
            tight = [p for p, v in zip(pts, vv) if v == dd]
            if len(tight) >= n and all(v >= dd for v in vv):
                p0 = tight[0]
                if exact_rank([[a - b for a, b in zip(t, p0)] for t in tight[1:]]) == n - 1:
                    facets[uu] = dd
    return facets

def check_graph(name, nv, edges, J1, J2, verbose=True):
    SU, SF, L = supports(nv, edges, J1, J2)
    pts = sorted(SU | SF)
    N = len(edges)
    p0 = pts[0]
    dim = exact_rank([[a - b for a, b in zip(t, p0)] for t in pts[1:]])
    crit = two_connected_loopless(nv, edges + [(J1, J2)])
    res = {'dim': dim, 'N': N, 'full': dim == N, 'crit': crit, 'crit_ok': (dim == N) == crit}
    if dim == N:
        fac = brute_facets(pts)
        bad = [u for u, d in fac.items() if d == 0 and sorted(abs(a) for a in u) != [0] * (N - 1) + [1]]
        # classification by the report's four types (in terms of 0/1/-1 normals and d)
        types_ok = all(set(u) <= {-1, 0, 1} and ((d == 0 and sum(u) == 1) or (d < 0 and max(u) <= 0) or (d > 0 and min(u) >= 0))
                       for u, d in fac.items())
        res.update({'facets': len(fac), 'd0_noncoordinate': len(bad), 'types_ok': types_ok})
    if verbose:
        print("   %-34s N=%d L=%d |supp|=%d %s" % (name, N, L, len(pts), res))
    return res

print("(H) explicit forward graphs (vertex labels: J1, J2 marked; P1, P2 may coincide with them):")
explicit = [
    ("1L triangle (J2=P2)", 3, [(0, 1), (1, 2), (2, 0)], 0, 1),
    ("1L box P1-J1-J2-P2", 4, [(0, 1), (1, 2), (2, 3), (3, 0)], 1, 2),
    ("1L self-energy on hard line", 4, [(0, 1), (1, 2), (1, 2), (2, 3)], 0, 3),
    ("1L vertex correction at J1", 4, [(0, 1), (1, 2), (0, 2), (2, 3)], 1, 3),
    ("2L triangle + bubble", 4, [(0, 1), (1, 2), (2, 3), (3, 0), (3, 0)], 0, 1),
    ("2L box + rung", 5, [(0, 1), (1, 2), (2, 3), (3, 0), (1, 4), (4, 3)], 1, 2),
    ("2L sunset-like hard part", 3, [(0, 1), (0, 1), (1, 2), (2, 0), (2, 0)], 0, 1),
    ("not 2-conn: tadpole on line", 4, [(0, 1), (1, 2), (2, 0), (2, 3), (3, 3)], 0, 1),
    ("not 2-conn: p-side bubble", 4, [(0, 1), (1, 2), (2, 0), (2, 3), (2, 3)], 0, 1),
]
okH = True
for (nm, nv, es, a, b) in explicit:
    r = check_graph(nm, nv, es, a, b)
    okH = okH and r['crit_ok'] and (not r['full'] or (r['d0_noncoordinate'] == 0 and r['types_ok']))

print("(H) random multigraphs (N <= 6 lines, loops/multi-edges allowed, J1 != J2):")
random.seed(7)
nfull, ntot = 0, 0
for trial in range(400):
    nv = random.randint(2, 4)
    N = random.randint(nv, 6)
    es = [tuple(random.sample(range(nv), 2)) if random.random() > 0.08 else (lambda v: (v, v))(random.randrange(nv))
          for _ in range(N)]
    if len(set(components(nv, es))) != 1:
        continue
    J1, J2 = random.sample(range(nv), 2)
    SU, SF, L = supports(nv, es, J1, J2)
    if not SU or not SF or len(SU | SF) > 22:
        continue
    r = check_graph("rand%d" % trial, nv, es, J1, J2, verbose=False)
    ntot += 1
    nfull += r['full']
    ok = r['crit_ok'] and (not r['full'] or (r['d0_noncoordinate'] == 0 and r['types_ok']))
    if not ok:
        print("   FAIL", trial, nv, es, J1, J2, r)
    okH = okH and ok
print("(H) random graphs tested: %d (full-dimensional: %d); all checks passed: %s" % (ntot, nfull, okH))

print("\nSUMMARY  F:%s  G:%s  W:%s  H:%s" % (okF, okG, okW, okH))
