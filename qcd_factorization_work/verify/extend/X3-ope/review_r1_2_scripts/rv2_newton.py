"""
rv2_newton.py -- reviewer #2 (X3, round 1): INDEPENDENT re-implementation of the structural checks behind
"Theorem F" (forward on-shell expansion), written without reusing f1_forward_graphs.py.

 * U, F0, F1 are computed by the matrix (electrical-network) method: with conductances 1/x_e,
   U = prod(x) det(Lred),  F/U = sum_{v,w} P_v.P_w (Lred^{-1})_{vw}   (Euclidean P, reference vertex removed),
   P_v = cp_v p + cq_v q,  q_E^2 = 1,  p_E^2 = 0,  2 p_E.q_E = -omega   =>  F = F0 + omega F1 .
   (independent of the spanning-forest enumeration used in f1)  -- cross-checked against my own forest code.
 * full-dimensionality of Newt(U+F0) by EXACT integer rank;
 * my combinatorial criterion (Lemma R2.1 of the review): Newt(U+F0) is full-dimensional  <=>  every edge lies in the
   block (2-connected component) of Gamma + {virtual edge J1J2} that contains the virtual edge;
 * facets of Newt(U+F0) from qhull, each candidate re-verified EXACTLY (integer normal, support value, affine rank
   N-1 of the points on it); DR admissibility: every facet with d_u = 0 has <1,u> > 0;
 * domination |F1_m| <= F0_m monomialwise.
Run: python3 -I rv2_newton.py
"""
import sys, os, itertools, random
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
from fractions import Fraction
from math import gcd
from functools import reduce
from scipy.spatial import ConvexHull


def polys_matrix(nv, edges, ext):
    """U, F0, F1 as dicts {exponent tuple: int} via the network method (sympy, exact)."""
    N = len(edges)
    xs = sp.symbols('x0:%d' % N, positive=True)
    L = sp.zeros(nv, nv)
    for e, (u, v) in enumerate(edges):
        if u == v:
            continue                      # self-loop: no contribution to the Laplacian
        w = 1 / xs[e]
        L[u, u] += w; L[v, v] += w; L[u, v] -= w; L[v, u] -= w
    r = nv - 1                            # reference vertex removed
    Lr = L[:r, :r]
    X = sp.Mul(*xs)
    det = sp.together(Lr.det(method='berkowitz'))
    U = sp.factor(sp.expand(sp.cancel(det * X)))
    adj = Lr.adjugate(method='berkowitz')
    cp = [ext.get(v, (0, 0))[0] for v in range(nv)]
    cq = [ext.get(v, (0, 0))[1] for v in range(nv)]
    # momentum conservation: reference vertex momentum is -(sum of the others); its potential is 0, so only v,w<r enter
    S0 = 0
    S1 = 0
    for v in range(r):
        for w in range(r):
            S0 += cq[v] * cq[w] * adj[v, w]
            S1 += -sp.Rational(1, 2) * (cp[v] * cq[w] + cq[v] * cp[w]) * adj[v, w]
    F0 = sp.expand(sp.cancel(S0 * X))
    F1 = sp.expand(sp.cancel(S1 * X))
    U = sp.expand(U)

    def todict(P):
        d = {}
        if P == 0:
            return d
        for mon, c in sp.Poly(P, *xs).terms():
            d[tuple(int(t) for t in mon)] = int(c)
        return d
    # self-loops: U and F carry a factor x_e for every self-loop (never in a tree); the Laplacian ignores them,
    # so multiply back (X already contains x_e, and det does not contain 1/x_e) -> nothing to do: X*det has x_e^1.
    return todict(U), todict(F0), todict(F1)


class DSU:
    def __init__(self, n):
        self.p = list(range(n))
    def f(self, a):
        while self.p[a] != a:
            self.p[a] = self.p[self.p[a]]
            a = self.p[a]
        return a
    def u(self, a, b):
        a, b = self.f(a), self.f(b)
        if a == b:
            return False
        self.p[a] = b
        return True


def polys_forest(nv, edges, ext):
    """my own forest enumeration (cross-check)"""
    N = len(edges)
    U, F0, F1 = {}, {}, {}
    for k, target in ((1, U), (2, None)):
        for S in itertools.combinations(range(N), nv - k):
            d = DSU(nv)
            if not all(d.u(*edges[i]) for i in S):
                continue
            m = tuple(0 if i in S else 1 for i in range(N))
            if k == 1:
                U[m] = U.get(m, 0) + 1
            else:
                root = d.f(0)
                cp = sum(ext.get(v, (0, 0))[0] for v in range(nv) if d.f(v) == root)
                cq = sum(ext.get(v, (0, 0))[1] for v in range(nv) if d.f(v) == root)
                if cq * cq:
                    F0[m] = F0.get(m, 0) + cq * cq
                if cp * cq:
                    F1[m] = F1.get(m, 0) - cp * cq
    return U, F0, F1


def int_rank(points):
    pts = [list(p) for p in points]
    if len(pts) < 2:
        return 0
    M = sp.Matrix([[a - b for a, b in zip(p, pts[0])] for p in pts[1:]])
    return M.rank()


def blocks_criterion(nv, edges, J1, J2):
    """True iff every edge lies in the block of Gamma+{J1J2} containing the virtual edge (Tarjan, multigraph)."""
    if J1 == J2:
        return False
    E = list(edges) + [(J1, J2)]
    virt = len(E) - 1
    adj = {v: [] for v in range(nv)}
    for i, (a, b) in enumerate(E):
        if a == b:
            continue
        adj[a].append((b, i)); adj[b].append((a, i))
    disc, low = {}, {}
    stack, comp_of = [], {}
    t = [0]
    ncomp = [0]
    sys.setrecursionlimit(10000)

    def dfs(v, pe):
        disc[v] = low[v] = t[0]; t[0] += 1
        for (w, i) in adj[v]:
            if i == pe:
                continue
            if w not in disc:
                stack.append(i)
                dfs(w, i)
                low[v] = min(low[v], low[w])
                if low[w] >= disc[v]:
                    c = ncomp[0]; ncomp[0] += 1
                    while True:
                        j = stack.pop(); comp_of[j] = c
                        if j == i:
                            break
            elif disc[w] < disc[v]:
                stack.append(i)
                low[v] = min(low[v], disc[w])
    for v in range(nv):
        if v not in disc:
            dfs(v, None)
    cv = comp_of.get(virt)
    for i, (a, b) in enumerate(E[:-1]):
        if a == b or comp_of.get(i) != cv:
            return False
    return True


def primitive_int(v):
    fr = [Fraction(float(x)).limit_denominator(2000) for x in v]
    den = reduce(lambda a, b: a * b // gcd(a, b), [f.denominator for f in fr], 1)
    ints = [int(f * den) for f in fr]
    g = reduce(gcd, [abs(x) for x in ints if x], 0)
    return tuple(x // g for x in ints) if g else tuple(ints)


def facets_exact(points):
    P = np.array(points, dtype=float)
    hull = ConvexHull(P, qhull_options='Qx')
    N = P.shape[1]
    out = {}
    for eq in hull.equations:
        u = primitive_int(-eq[:-1] / np.max(np.abs(eq[:-1])))
        if u in out:
            continue
        vals = [sum(a * b for a, b in zip(u, m)) for m in points]
        d = min(vals)
        on = [m for m, val in zip(points, vals) if val == d]
        if int_rank(on) != N - 1:
            raise RuntimeError('candidate normal %s failed exact facet verification' % (u,))
        out[u] = d
    return out


def analyse(nv, edges, ext, method='forest'):
    J = [v for v in range(nv) if ext.get(v, (0, 0))[1] != 0]
    qv = {v: ext[v][1] for v in J}
    J1 = [v for v in qv if qv[v] > 0]
    J2 = [v for v in qv if qv[v] < 0]
    J1 = J1[0] if J1 else None
    J2 = J2[0] if J2 else None
    U, F0, F1 = (polys_matrix if method == 'matrix' else polys_forest)(nv, edges, ext)
    dom = all(m in F0 and abs(c) <= F0[m] for m, c in F1.items())
    G = dict(U)
    for m, c in F0.items():
        G[m] = G.get(m, 0) + c
    pts = sorted(G)
    N = len(edges)
    full = int_rank(pts) == N
    crit = blocks_criterion(nv, edges, J1, J2) if (J1 is not None and J2 is not None) else False
    dr = None
    nfac = None
    if full:
        fac = facets_exact(pts)
        nfac = len(fac)
        dr = all(not (d == 0 and sum(u) <= 0) for u, d in fac.items())
        neg0 = [u for u, d in fac.items() if d == 0 and any(x < 0 for x in u)]
    else:
        neg0 = []
    return dict(U=U, F0=F0, F1=F1, dom=dom, full=full, crit=crit, dr=dr, nfac=nfac, neg0=neg0)


P, Mq, Qi, Qo = (1, 0), (-1, 0), (0, 1), (0, -1)


def merge(*pairs):
    d = {}
    for v, mom in pairs:
        a = d.get(v, (0, 0))
        d[v] = (a[0] + mom[0], a[1] + mom[1])
    return d


if __name__ == '__main__':
    # ---------- (1) cross-check matrix method vs forest method on small graphs
    rng = random.Random(777)
    nmis = 0
    ntest = 0
    for trial in range(60):
        nv = rng.choice([3, 4, 5])
        L = rng.choice([1, 2])
        ne = nv - 1 + L
        while True:
            edges = [(rng.randrange(nv), rng.randrange(nv)) for _ in range(ne)]
            d = DSU(nv)
            for a, b in edges:
                d.u(a, b)
            if len({d.f(v) for v in range(nv)}) == 1 and all(a != b for a, b in edges):
                break
        vs = [rng.randrange(nv) for _ in range(4)]
        ext = merge((vs[0], P), (vs[1], Mq), (vs[2], Qi), (vs[3], Qo))
        A = polys_matrix(nv, edges, ext)
        B = polys_forest(nv, edges, ext)
        ntest += 1
        if A != B:
            nmis += 1
            print('MISMATCH', nv, edges, ext)
    print('(1) matrix-tree method == forest enumeration on %d random loopless graphs: mismatches = %d' % (ntest, nmis))

    # ---------- (2) explicit QCD-like forward graphs (f1 list re-entered by hand + additional topologies)
    G = []
    G.append(("q1 box(direct)", 4, [(0, 1), (1, 2), (2, 3), (0, 3)], merge((0, P), (1, Qi), (2, Qo), (3, Mq))))
    G.append(("q1 box(crossed photons)", 4, [(0, 1), (1, 2), (2, 3), (0, 3)], merge((0, P), (1, Qo), (2, Qi), (3, Mq))))
    G.append(("q1 vertex J1", 4, [(0, 1), (1, 2), (2, 3), (0, 2)], merge((0, P), (1, Qi), (3, Qo), (3, Mq))))
    G.append(("q1 hard self-energy", 4, [(0, 1), (1, 2), (1, 2), (2, 3)], merge((0, P), (0, Qi), (3, Qo), (3, Mq))))
    G.append(("g1 quark box G1 J1 G2 J2", 4, [(0, 1), (1, 2), (2, 3), (3, 0)], merge((0, P), (2, Mq), (1, Qi), (3, Qo))))
    G.append(("q2 planar ladder", 6, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 5), (1, 4)], merge((0, P), (2, Qi), (3, Qo), (5, Mq))))
    G.append(("q2 crossed ladder", 6, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 4), (1, 5)], merge((0, P), (2, Qi), (3, Qo), (5, Mq))))
    G.append(("q2 3-gluon vertex", 6, [(0, 1), (1, 2), (2, 3), (3, 4), (0, 5), (4, 5), (5, 2)], merge((0, P), (1, Qi), (3, Qo), (4, Mq))))
    G.append(("q2 singlet (quark loop)", 6, [(0, 1), (0, 2), (1, 4), (2, 3), (3, 4), (4, 5), (5, 2)], merge((0, P), (1, Mq), (3, Qi), (5, Qo))))
    # additional topologies not in f1:
    # (a) vertex correction at the target-gluon vertex A of the box: A(p)-V-J1-J2-B(-p), gluon V-B, extra gluon A-W on gluon line?
    #     realised as: target quark A(p)->V, gluons A-W, V-W? -> triangle at the incoming quark-gluon vertex
    #     vertices A=0,V=1,J1=2,J2=3,B=4,W=5 ; quark A-V-J1-J2-B ; gluon W-B (exchanged) ; gluons A-W, V-W (vertex corr.)
    G.append(("q2 target-vertex correction (3g)", 6, [(0, 1), (1, 2), (2, 3), (3, 4), (5, 4), (0, 5), (1, 5)], merge((0, P), (2, Qi), (3, Qo), (4, Mq))))
    # (b) quartic gluon vertex: gluon target G1(p), G2(-p) meet a 4-gluon vertex X with two gluons to a quark loop with currents
    #     X=0 (p in, -p out at the same vertex) ; loop Y-J1-Z-J2-Y ; gluons X-Y, X-Z    (p-legs at one vertex: no p flow)
    G.append(("g2 quartic vertex to quark loop", 5, [(0, 1), (0, 2), (1, 3), (3, 2), (2, 4), (4, 1)], merge((0, P), (0, Mq), (3, Qi), (4, Qo))))
    # (c) degenerate control case: a one-loop block attached to vertex 1 only (cut vertex, no q flow) -> must be non-full-dimensional
    G.append(("g2 DEGENERATE test: extra loop at a cut vertex (tadpole block)", 6, [(0, 1), (1, 2), (2, 3), (3, 0), (1, 4), (4, 5), (5, 1)], merge((0, P), (2, Mq), (1, Qi), (3, Qo))))
    # (d) three-loop non-planar: crossed ladder + rung between hard line and target line
    G.append(("q3 crossed ladder + extra rung", 8, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (0, 6), (1, 7), (2, 5)], merge((0, P), (3, Qi), (4, Qo), (7, Mq))))
    # (e) three-loop: box with two-loop gluon self-energy (nested bubble) on the exchanged gluon
    G.append(("q3 box x 2L gluon self-energy", 7, [(0, 1), (1, 2), (2, 3), (0, 4), (4, 5), (4, 6), (5, 6), (5, 6), (6, 3)], merge((0, P), (1, Qi), (2, Qo), (3, Mq))))
    # (f) gluon target, three-loop: quark box with gluon ladder rungs
    G.append(("g3 quark box with two rungs", 8, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 0), (1, 7), (2, 6)], merge((0, P), (4, Mq), (3, Qi), (5, Qo))))
    allok = True
    for name, nv, edges, ext in G:
        A = analyse(nv, edges, ext, method='forest')
        if len(edges) <= 8:
            Am = analyse(nv, edges, ext, method='matrix')
            same = (Am['U'], Am['F0'], Am['F1']) == (A['U'], A['F0'], A['F1'])
        else:
            same = 'n/a'
        print('(2) %-38s N=%2d dom=%s full=%s crit=%s DR=%s facets=%s neg-normal d=0 facets=%s matrix==forest:%s'
              % (name, len(edges), A['dom'], A['full'], A['crit'], A['dr'], A['nfac'], A['neg0'], same))
        allok &= A['dom'] and (A['full'] == A['crit']) and (A['dr'] in (True, None))
    print('(2) all explicit graphs: domination, full<=>criterion, DR-admissible where full:', allok)

    # ---------- (3) random multigraphs: full-dimensionality <=> block criterion ; DR admissibility
    rng = random.Random(4242)
    stats = dict(n=0, full=0, agree=0, dr=0, dom=0, neg0=0)
    disagree = []
    for trial in range(1500):
        nv = rng.choice([3, 4, 5, 6, 7])
        L = rng.choice([1, 2, 3, 4])
        ne = nv - 1 + L
        if ne > 10:
            continue
        while True:
            edges = [(rng.randrange(nv), rng.randrange(nv)) for _ in range(ne)]
            d = DSU(nv)
            for a, b in edges:
                d.u(a, b)
            if len({d.f(v) for v in range(nv)}) == 1:
                break
        vs = [rng.randrange(nv) for _ in range(4)]
        ext = merge((vs[0], P), (vs[1], Mq), (vs[2], Qi), (vs[3], Qo))
        try:
            A = analyse(nv, edges, ext)
        except RuntimeError as e:
            print('facet verification failure', e, nv, edges, ext)
            continue
        stats['n'] += 1
        stats['dom'] += A['dom']
        stats['full'] += A['full']
        stats['agree'] += (A['full'] == A['crit'])
        if A['full']:
            stats['dr'] += bool(A['dr'])
            stats['neg0'] += bool(A['neg0'])
        if A['full'] != A['crit']:
            disagree.append((nv, edges, ext, A['full'], A['crit']))
    print('(3) random graphs:', stats)
    for x in disagree[:10]:
        print('    disagreement:', x)
