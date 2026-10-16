"""
Reviewer check R1 (independent of f1_forward_graphs.py: supports by deletion-contraction, exact facet normals by
rational elimination; only qhull is shared, and is used only to propose candidate facets).

Reviewer's claims tested:
  (a) supp(F1) subset supp(F0), |F1| <= F0 coefficientwise (domination)        -- trivial, checked in f1
  (b) Newt(U + F0) full-dimensional  <=>  G° := G + {J1--J2} is loopless and 2-connected (matroid-connected).
      Reason: F0/Q^2 = U(G/{J1=J2}) and U(G°) = x_q U(G) + U(G/{J1=J2}); so supp(U+F0) is an affine bijective
      image of supp U(G°) (= complements of spanning trees of G° = bases of the cographic matroid), and the
      matroid base polytope has dimension |E| - #components.
  (c) if (b) holds, the only facets of Newt(U+F0) with d_u = 0 are coordinate facets u = e_i (so <u,1> = 1 > 0:
      the DR line a = (1,...,1) is never contained in a D-independent polar hyperplane) -- from the facet
      description of connected matroid base polytopes (coordinate facets and flacet inequalities).
"""
import sys, os, random
from fractions import Fraction
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from scipy.spatial import ConvexHull


def spanning_trees(nv, edges):
    """edges: list of (id, u, v). Returns list of frozensets of edge ids (deletion-contraction)."""
    nonloop = [e for e in edges if e[1] != e[2]]
    if not nonloop:
        return [frozenset()] if nv == 1 else []
    eid, u, v = nonloop[0]
    rest = [e for e in edges if e[0] != eid]
    # deletion
    out = list(spanning_trees(nv, rest)) if connected(nv, rest) else []
    # contraction: merge v into u, relabel
    m = {}
    k = 0
    for w in range(nv):
        if w == v:
            continue
        m[w] = k
        k += 1
    m[v] = m[u]
    rest_c = [(i, m[a], m[b]) for (i, a, b) in rest]
    out += [T | {eid} for T in spanning_trees(nv - 1, rest_c)]
    return out


def connected(nv, edges):
    par = list(range(nv))
    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    for _, a, b in edges:
        par[f(a)] = f(b)
    return len({f(w) for w in range(nv)}) == 1


def support_U(nv, edges):
    N = len(edges)
    E = [(i, a, b) for i, (a, b) in enumerate(edges)]
    return {tuple(0 if i in T else 1 for i in range(N)) for T in spanning_trees(nv, E)}


def support_F0(nv, edges, J1, J2):
    """F0/Q^2 = U(G/{J1=J2}): complements of spanning trees of the merged graph = 2-forests separating J1,J2"""
    N = len(edges)
    m = {}
    k = 0
    for w in range(nv):
        if w == J2:
            continue
        m[w] = k
        k += 1
    m[J2] = m[J1]
    E = [(i, m[a], m[b]) for i, (a, b) in enumerate(edges)]
    return {tuple(0 if i in T else 1 for i in range(N)) for T in spanning_trees(nv - 1, E)}


def loopless_2connected(nv, edges):
    if any(a == b for a, b in edges):
        return False
    E = [(i, a, b) for i, (a, b) in enumerate(edges)]
    if not connected(nv, E):
        return False
    if nv <= 2:
        return True
    for w in range(nv):
        m = {}
        k = 0
        for z in range(nv):
            if z == w:
                continue
            m[z] = k
            k += 1
        Ew = [(i, m[a], m[b]) for (i, a, b) in E if a != w and b != w]
        if not connected(nv - 1, Ew):
            return False
    return True


def nullspace_1(rows, n):
    """exact rational nullspace of an integer matrix (rows), expected dimension 1"""
    A = [[Fraction(x) for x in r] for r in rows]
    piv = []
    r = 0
    for c in range(n):
        p = next((i for i in range(r, len(A)) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [x - f * y for x, y in zip(A[i], A[r])]
        piv.append(c)
        r += 1
        if r == len(A):
            break
    free = [c for c in range(n) if c not in piv]
    if len(free) != 1:
        return None
    fc = free[0]
    u = [Fraction(0)] * n
    u[fc] = Fraction(1)
    for i, c in enumerate(piv):
        u[c] = -A[i][fc]
    den = 1
    for x in u:
        den = den * x.denominator // np.gcd(den, x.denominator)
    ui = [int(x * den) for x in u]
    g = 0
    for x in ui:
        g = np.gcd(g, abs(x))
    return [x // g for x in ui]


def exact_facets(points):
    P = np.array(points, dtype=float)
    hull = ConvexHull(P, qhull_options='Qx')
    out = set()
    seen = set()
    for eq in hull.equations:
        key = tuple(np.round(eq / np.max(np.abs(eq[:-1])), 6))
        if key in seen:
            continue
        seen.add(key)
        n, c = eq[:-1], eq[-1]
        on = np.nonzero(np.abs(P @ n + c) < 1e-7)[0]
        # pick an affinely spanning subset of the on-facet points (greedy rank growth) to keep elimination small
        base = [on[0]]
        cur = np.zeros((0, P.shape[1]))
        for i in on[1:]:
            cand = np.vstack([cur, P[i] - P[on[0]]])
            if np.linalg.matrix_rank(cand) > cur.shape[0]:
                cur = cand
                base.append(i)
            if cur.shape[0] == P.shape[1] - 1:
                break
        rows = [[a - b for a, b in zip(points[i], points[on[0]])] for i in base[1:]]
        u = nullspace_1(rows, len(points[0]))
        if u is None:
            raise RuntimeError('degenerate facet')
        vals = [sum(a * b for a, b in zip(u, m)) for m in points]
        if min(vals) < vals[on[0]]:
            u = [-x for x in u]
            vals = [-v for v in vals]
        assert min(vals) == vals[on[0]], 'not a supporting hyperplane'
        out.add((tuple(u), min(vals)))
    return sorted(out)


def analyse(nv, edges, ext):
    N = len(edges)
    J1 = [v for v, (cp, cq) in ext.items() if cq == 1][0]
    J2 = [v for v, (cp, cq) in ext.items() if cq == -1][0]
    SU = support_U(nv, edges)
    SF = support_F0(nv, edges, J1, J2) if J1 != J2 else set()
    pts = sorted(SU | SF)
    P = np.array(pts, dtype=float)
    rk = np.linalg.matrix_rank(P[1:] - P[0]) if len(P) > 1 else 0
    full = (rk == N)
    crit = (J1 != J2) and loopless_2connected(nv, edges + [(J1, J2)])
    dr_auto = dr_ok = None
    if full:
        fac = exact_facets(pts)
        bad = [(u, d) for (u, d) in fac if d == 0 and sorted(u) != [0] * (N - 1) + [1]]
        dr_auto = not bad
        dr_ok = all(sum(u) > 0 for (u, d) in fac if d == 0)
    return dict(full=full, crit=crit, dr_auto=dr_auto, dr_ok=dr_ok, SU=SU, SF=SF)


def random_graph(rng, nv, ne):
    while True:
        edges = [(rng.randrange(nv), rng.randrange(nv)) for _ in range(ne)]
        if connected(nv, [(i, a, b) for i, (a, b) in enumerate(edges)]):
            return edges


if __name__ == '__main__':
    sys.path.insert(0, '/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/scripts')
    import importlib
    f1 = importlib.import_module('f1_forward_graphs')
    agree = True
    for name, nv, edges, ext in f1.graphs:
        U1, F01, F11 = f1.symanzik(nv, edges, ext)
        res = analyse(nv, edges, ext)
        ok = (set(U1) == res['SU']) and (set(F01) == res['SF']) and all(v == 1 for v in U1.values()) \
            and all(v == 1 for v in F01.values())
        agree &= ok
        print('%-40s supports agree with f1: %s ; full=%s  G+J1J2 loopless&2-conn=%s  DR-auto=%s'
              % (name, ok, res['full'], res['crit'], res['dr_auto']))
    print('ALL explicit graphs: supports agree with f1 (and all coefficients of U, F0 equal 1):', agree)

    ntrial = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    rng = random.Random(777)
    st = dict(n=0, full=0, match=0, mm=[], auto=0, autofail=[], drfail=[])
    P_, M_, Qi, Qo = (1, 0), (-1, 0), (0, 1), (0, -1)
    for trial in range(ntrial):
        nv = rng.choice([2, 3, 4, 5, 6, 7])
        L = rng.choice([1, 2, 3, 4])
        ne = nv - 1 + L
        if ne > 11:
            continue
        edges = random_graph(rng, nv, ne)
        vs = [rng.randrange(nv) for _ in range(4)]
        ext = {}
        for v, mom in zip(vs, [P_, M_, Qi, Qo]):
            a = ext.get(v, (0, 0))
            ext[v] = (a[0] + mom[0], a[1] + mom[1])
        if [m[1] for m in ext.values()].count(1) != 1 or [m[1] for m in ext.values()].count(-1) != 1:
            continue   # both currents at one vertex: no q flow (degenerate, trivially)
        res = analyse(nv, edges, ext)
        st['n'] += 1
        st['full'] += res['full']
        if res['full'] == res['crit']:
            st['match'] += 1
        else:
            st['mm'].append((nv, edges, ext))
        if res['full']:
            if res['dr_auto']:
                st['auto'] += 1
            else:
                st['autofail'].append((nv, edges, ext))
            if not res['dr_ok']:
                st['drfail'].append((nv, edges, ext))
    print('random graphs (2..7 vertices, 1..4 loops, <= 11 lines):', st['n'], '; full-dimensional:', st['full'])
    print('(b) full-dim <=> G+{J1J2} loopless and 2-connected :', st['match'], '/', st['n'], '; mismatches:', st['mm'][:3])
    print('(c) full-dim graphs whose only d_u = 0 facets are coordinate facets:', st['auto'], '/', st['full'],
          '; failures:', st['autofail'][:3])
    print('    DR-admissibility (all d_u = 0 facets have <u,1> > 0) failures:', st['drfail'][:3])
