"""
f1_forward_graphs.py  --  structural hypotheses of Theorem F (forward on-shell expansion) checked on
explicit forward Compton graphs (1, 2 and 3 loops) and on random graphs.

For a connected graph with N internal lines, L loops and external momenta
    p (in) at vertex P1, -p at P2, q (in) at J1, -q at J2      (p^2 = 0, q^2 = -Q^2, Q^2 = 1, 2p.q = omega Q^2)
we build the Symanzik polynomials
    U = sum_{spanning trees T} prod_{e not in T} a_e
    F = sum_{spanning 2-forests (T1,T2)} prod_{e not in T1 u T2} a_e * ( - P_{T1}^2 )
and check:
  (C1)  F = F0 + omega*F1 with F0, F1 having the properties used in Lemma F.1:
        every monomial of F1 is a monomial of F0 and |coef_F1| <= coef_F0   (domination);
  (C2)  the Lee-Pomeransky polynomial G = U + F0 has a full-dimensional Newton polytope in R^N
        (=> nonempty convergence domain of the analytically regularized integral, Schultka Thm 3.1);
  (C3)  "DR admissibility": every facet of Newt(G) whose primitive inward normal u has d_u(G) = 0
        satisfies <1,u> > 0, so that no polar hyperplane <a,u> - (D/2) d_u(G) = -k (k = 0,1,2,...)
        contains the DR line a = (1,...,1);
  (C4)  Newt(U + F0 + omega F1) = Newt(U + F0) for |omega| < 1 (no vertex coefficient can vanish).
Degenerate graphs (C2 fails) are classified (self-loop / zero-momentum bridge / bridge carrying exactly p).
REVISION NOTES (fix round 1):
  * (C1) and (C4) hold identically by Lemma F.0 (every F0 coefficient is c_q^2 = 1, every F1 coefficient is
    -c_p c_q in {0,+-1}); the random tests of (C1), (C4) only check the code, they add no evidence.
  * (C2), (C3) and the classification of degenerate graphs below are heuristic sampling; they are superseded by
    Lemma F.6 of the revised report (Newt(U+F0) = projected base polytope of the cographic matroid of
    G + {J1J2}: full-dimensional iff G + {J1J2} is loopless and 2-connected; every facet with d_u = 0 is a
    coordinate facet), checked exactly in f3_matroid_lemma.py.
  * A bridge carrying exactly +-p is an on-shell external-leg correction, excluded by amputation (the on-shell
    massless self-energy is scaleless, the LSZ factor is 1 in DR); it is labelled accordingly.
Run:  python3 -I f1_forward_graphs.py
"""
import sys, os, itertools, random
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from fractions import Fraction
from math import gcd
from functools import reduce
from scipy.spatial import ConvexHull

# ------------------------------------------------------------------ graph polynomials
class DSU:
    def __init__(self, n):
        self.p = list(range(n))
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        self.p[ra] = rb
        return True


def forests(nv, edges, k):
    """all spanning forests with exactly k trees: edge subsets of size nv-k without cycles"""
    out = []
    for S in itertools.combinations(range(len(edges)), nv - k):
        d = DSU(nv)
        ok = True
        for i in S:
            u, v = edges[i]
            if not d.union(u, v):
                ok = False
                break
        if ok:
            comps = {}
            for v in range(nv):
                comps.setdefault(d.find(v), []).append(v)
            out.append((S, list(comps.values())))
    return out


def symanzik(nv, edges, ext):
    """ext: dict vertex -> (cp, cq) incoming momentum cp*p + cq*q.
    Returns U, F0, F1 as dicts {exponent tuple: integer coefficient} (Q^2 = 1, F = F0 + omega F1)."""
    N = len(edges)
    U, F0, F1 = {}, {}, {}
    for S, comps in forests(nv, edges, 1):
        m = tuple(0 if i in S else 1 for i in range(N))
        U[m] = U.get(m, 0) + 1
    for S, comps in forests(nv, edges, 2):
        m = tuple(0 if i in S else 1 for i in range(N))
        c1 = comps[0]
        cp = sum(ext.get(v, (0, 0))[0] for v in c1)
        cq = sum(ext.get(v, (0, 0))[1] for v in c1)
        # -P^2 = cq^2 Q^2 - cp cq (2 p.q) = cq^2 - cp*cq*omega   (Q^2 = 1)
        a0, a1 = cq * cq, -cp * cq
        if a0:
            F0[m] = F0.get(m, 0) + a0
        if a1:
            F1[m] = F1.get(m, 0) + a1
    return U, F0, F1


def rank_of(points):
    P = np.array(points, dtype=float)
    if len(P) < 2:
        return 0
    return np.linalg.matrix_rank(P[1:] - P[0])


def primitive(v):
    fr = [Fraction(x).limit_denominator(1000) for x in v]
    den = reduce(lambda a, b: a * b // gcd(a, b), [f.denominator for f in fr], 1)
    ints = [int(f * den) for f in fr]
    g = reduce(gcd, [abs(x) for x in ints if x != 0], 0)
    return tuple(x // g for x in ints) if g else tuple(ints)


def facet_normals(points):
    P = np.array(points, dtype=float)
    hull = ConvexHull(P, qhull_options='Qx')
    normals = set()
    for eq in hull.equations:
        n = -eq[:-1]                      # qhull: n.x + c <= 0 inside ; inward normal = -n
        n = n / np.max(np.abs(n))
        normals.add(primitive(n))
    return sorted(normals)


def check_graph(name, nv, edges, ext, verbose=True):
    N = len(edges)
    L = N - nv + 1
    U, F0, F1 = symanzik(nv, edges, ext)
    # (C1) domination
    dom = all((m in F0) and abs(c) <= F0[m] for m, c in F1.items())
    # (C4) vertex coefficients of F0 + omega F1 never vanish for |omega|<1: coefficient = F0[m] + omega F1[m]
    c4 = all(abs(F1.get(m, 0)) <= F0[m] for m in F0) and dom
    G = dict(U)
    for m, c in F0.items():
        G[m] = G.get(m, 0) + c
    pts = list(G.keys())
    rk = rank_of(pts)
    full = (rk == N)
    dr_ok = None
    nfac = None
    if full:
        try:
            normals = facet_normals(pts)
            nfac = len(normals)
            dr_ok = True
            for u in normals:
                d = min(sum(ui * mi for ui, mi in zip(u, m)) for m in pts)
                if d == 0 and sum(u) <= 0:
                    dr_ok = False
        except Exception as e:
            dr_ok = 'qhull-error: %s' % e
    if verbose:
        print(f"{name:42s} N={N} L={L} |U|={len(U):4d} |F0|={len(F0):5d} |F1|={len(F1):5d} "
              f"dom={dom} C4={c4} fulldim={full} (rank {rk}) facets={nfac} DR-admissible={dr_ok}")
    return dom, c4, full, dr_ok


# ------------------------------------------------------------------ explicit QCD forward Compton topologies
P, Mq = (1, 0), (-1, 0)        # incoming p, outgoing p
Qi, Qo = (0, 1), (0, -1)       # incoming q, outgoing q

def merge(*pairs):
    d = {}
    for v, mom in pairs:
        a = d.get(v, (0, 0))
        d[v] = (a[0] + mom[0], a[1] + mom[1])
    return d

graphs = []
# tree handbag: J1(p,q) -- J2(-q,-p): one line, no loop (skipped: L=0)
# ---- 1 loop, quark target
# box: A(p) -J1(q)- J2(-q) - B(-p), gluon A-B ; vertices A=0,J1=1,J2=2,B=3
graphs.append(("q 1L box (direct)", 4, [(0, 1), (1, 2), (2, 3), (0, 3)], merge((0, P), (1, Qi), (2, Qo), (3, Mq))))
graphs.append(("q 1L box (crossed photons)", 4, [(0, 1), (1, 2), (2, 3), (0, 3)], merge((0, P), (1, Qo), (2, Qi), (3, Mq))))
# vertex correction at J1: A(p)-J1(q)-C-J2(-q,-p); gluon A-C ; A=0,J1=1,C=2,J2=3
graphs.append(("q 1L vertex at J1", 4, [(0, 1), (1, 2), (2, 3), (0, 2)], merge((0, P), (1, Qi), (3, Qo), (3, Mq))))
# vertex correction at J2: J1(p,q)-C-J2(-q)-B(-p); gluon C-B ; J1=0,C=1,J2=2,B=3
graphs.append(("q 1L vertex at J2", 4, [(0, 1), (1, 2), (2, 3), (1, 3)], merge((0, P), (0, Qi), (2, Qo), (3, Mq))))
# self-energy on hard line: J1(p,q)-C=D-J2(-q,-p) ; J1=0,C=1,D=2,J2=3
graphs.append(("q 1L hard self-energy", 4, [(0, 1), (1, 2), (1, 2), (2, 3)], merge((0, P), (0, Qi), (3, Qo), (3, Mq))))
# ---- 1 loop, gluon target: quark box, three orderings of (G1,G2,J1,J2) on the cycle
for name, order in [("g 1L quark box G1 J1 G2 J2", ['G1', 'J1', 'G2', 'J2']),
                    ("g 1L quark box G1 J1 J2 G2", ['G1', 'J1', 'J2', 'G2']),
                    ("g 1L quark box G1 G2 J1 J2", ['G1', 'G2', 'J1', 'J2'])]:
    idx = {v: i for i, v in enumerate(order)}
    edges = [(i, (i + 1) % 4) for i in range(4)]
    ext = merge((idx['G1'], P), (idx['G2'], Mq), (idx['J1'], Qi), (idx['J2'], Qo))
    graphs.append((name, 4, edges, ext))
# ---- 2 loops, quark target
# planar double ladder: P->A1->A2->J1->J2->B2->B1->out ; rungs A1-B1, A2-B2
# vertices A1=0,A2=1,J1=2,J2=3,B2=4,B1=5
graphs.append(("q 2L planar ladder", 6, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 5), (1, 4)],
               merge((0, P), (2, Qi), (3, Qo), (5, Mq))))
graphs.append(("q 2L crossed ladder", 6, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 4), (1, 5)],
               merge((0, P), (2, Qi), (3, Qo), (5, Mq))))
# box + vertex correction at J1: A(p)-V-J1(q)-C-J2(-q)-B(-p); gluons A-B, V-C
# A=0,V=1,J1=2,C=3,J2=4,B=5
graphs.append(("q 2L box x vertex(J1)", 6, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 5), (1, 3)],
               merge((0, P), (2, Qi), (4, Qo), (5, Mq))))
# box + self-energy on the hard line: A(p)-J1(q)-C=D-J2(-q)-B(-p); gluon A-B
graphs.append(("q 2L box x hard self-energy", 6, [(0, 1), (1, 2), (2, 3), (2, 3), (3, 4), (4, 5), (0, 5)],
               merge((0, P), (1, Qi), (4, Qo), (5, Mq))))
# box with self-energy on the exchanged gluon: A(p)-J1-J2-B(-p); gluon A-E=F-B
graphs.append(("q 2L box x gluon self-energy", 6, [(0, 1), (1, 2), (2, 3), (0, 4), (4, 5), (4, 5), (5, 3)],
               merge((0, P), (1, Qi), (2, Qo), (3, Mq))))
# box with three-gluon vertex: A(p)-J1-J2-B(-p) ; gluons A-T, B-T, T-C where C on the hard line J1-C-J2
# A=0,J1=1,C=2,J2=3,B=4,T=5
graphs.append(("q 2L box with 3-gluon vertex", 6, [(0, 1), (1, 2), (2, 3), (3, 4), (0, 5), (4, 5), (5, 2)],
               merge((0, P), (1, Qi), (3, Qo), (4, Mq))))
# two vertex corrections (J1 and J2), nested: A(p)-J1(q)-C-D-J2(-q)-B(-p); gluons A-D? (overlapping) and C-B
graphs.append(("q 2L overlapping vertex pair", 6, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 3), (2, 5)],
               merge((0, P), (1, Qi), (4, Qo), (5, Mq))))
# quark-loop (light-by-light-like) singlet: target quark exchanges two gluons with a quark loop that carries both currents
# target line A(p)-B(-p)... A=0,B=1 with line A-B ; gluons A-X, B-Y ; loop X-J1-Y-J2-X ; X=2,J1=3,Y=4,J2=5
graphs.append(("q 2L singlet (2 gluons to quark loop)", 6, [(0, 1), (0, 2), (1, 4), (2, 3), (3, 4), (4, 5), (5, 2)],
               merge((0, P), (1, Mq), (3, Qi), (5, Qo))))
# ---- 2 loops, gluon target: quark box with internal gluon (two placements)
# cycle G1=0,a=1,J1=2,b=3,G2=4,J2=5 ; quark lines around, gluon a-b
graphs.append(("g 2L quark box + gluon (a-b)", 6, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0), (1, 3)],
               merge((0, P), (4, Mq), (2, Qi), (5, Qo))))
graphs.append(("g 2L quark box + gluon (G-side)", 6, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0), (1, 5)],
               merge((0, P), (3, Mq), (2, Qi), (4, Qo))))
# gluon target with three-gluon vertex: G1(p)-T-G2(-p)?? : T attached to quark loop by a gluon; loop X-J1-Y-J2-X
# G1/G2 attach at T1,T2 on a gluon line T1-T2 ... : vertices T1=0 (p), T2=1 (-p), X=2, J1=3, Y=4, J2=5
graphs.append(("g 2L 3-gluon vertices to quark loop", 6, [(0, 1), (0, 2), (1, 4), (2, 3), (3, 4), (4, 5), (5, 2)],
               merge((0, P), (1, Mq), (3, Qi), (5, Qo))))
# ---- 3 loops (a few)
graphs.append(("q 3L planar triple ladder", 8, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (0, 7), (1, 6), (2, 5)],
               merge((0, P), (3, Qi), (4, Qo), (7, Mq))))
# planar double ladder with a self-energy on the hard line: A1(p)-A2-J1(q)-C=D-J2(-q)-B2-B1(-p), rungs A1-B1, A2-B2
# A1=0,A2=1,J1=2,C=3,D=4,J2=5,B2=6,B1=7
graphs.append(("q 3L ladder x hard self-energy", 8, [(0, 1), (1, 2), (2, 3), (3, 4), (3, 4), (4, 5), (5, 6), (6, 7), (0, 7), (1, 6)],
               merge((0, P), (2, Qi), (5, Qo), (7, Mq))))


def degenerate_reason(nv, edges, ext):
    reasons = []
    if all(ext.get(v, (0, 0))[1] == 0 for v in range(nv)):
        reasons.append('no q flow (both currents at one vertex: q-independent, scaleless)')
    if any(u == v for u, v in edges):
        reasons.append('self-loop (massless tadpole)')
    for i, (u, v) in enumerate(edges):
        rest = [e for j, e in enumerate(edges) if j != i]
        d = DSU(nv)
        for a, b in rest:
            d.union(a, b)
        if d.find(u) != d.find(v):           # bridge
            comp = [w for w in range(nv) if d.find(w) == d.find(u)]
            cp = sum(ext.get(w, (0, 0))[0] for w in comp)
            cq = sum(ext.get(w, (0, 0))[1] for w in comp)
            if cp == 0 and cq == 0:
                reasons.append('zero-momentum bridge')
            elif cq == 0:
                reasons.append('bridge carrying exactly +-p (external-leg correction, excluded by amputation)')
    # cut vertices w: a block K u {w} attached only at w with zero net external momentum and only p-type
    # (or no) legs inside K is a scaleless factor (its integral depends on p^2 = 0 only)
    for w in range(nv):
        rest = [(a, b) for (a, b) in edges if a != w and b != w]
        others = [x for x in range(nv) if x != w]
        d = DSU(nv)
        for a, b in rest:
            d.union(a, b)
        comps = {}
        for x in others:
            comps.setdefault(d.find(x), []).append(x)
        if len(comps) < 2:
            continue
        for K in comps.values():
            cp = sum(ext.get(x, (0, 0))[0] for x in K)
            cq = sum(ext.get(x, (0, 0))[1] for x in K)
            has_q = any(ext.get(x, (0, 0))[1] != 0 for x in K)
            nlines = sum(1 for (a, b) in edges if (a in K or b in K))
            if not has_q and nlines > 0:
                reasons.append('cut-vertex block with only p-type legs (scaleless factor, depends on p^2=0 only)')
                break
        # complementary situation: block containing both currents and no p-legs, attached at w:
        # then the other side (with p,-p) is the scaleless factor -- also caught above when the p-side is a component
    return reasons or ['other']


def random_graph(rng, nv, nedges):
    while True:
        edges = []
        for _ in range(nedges):
            u = rng.randrange(nv)
            v = rng.randrange(nv)
            edges.append((u, v))
        d = DSU(nv)
        for u, v in edges:
            d.union(u, v)
        if len({d.find(w) for w in range(nv)}) == 1:
            return edges


if __name__ == '__main__':
    print("=== explicit forward Compton topologies ===")
    allok = True
    for name, nv, edges, ext in graphs:
        dom, c4, full, dr = check_graph(name, nv, edges, ext)
        allok &= dom and c4 and full and (dr is True)
    print("ALL explicit graphs satisfy C1-C4:", allok)

    print("\n=== random connected graphs (external vertices random, possibly coinciding) ===")
    rng = random.Random(20261010)
    stats = {'n': 0, 'dom': 0, 'c4': 0, 'full': 0, 'dr': 0}
    degen = {}
    for trial in range(400):
        nv = rng.choice([3, 4, 5, 6])
        L = rng.choice([1, 2, 3])
        nedges = nv - 1 + L
        if nedges > 9:
            continue
        edges = random_graph(rng, nv, nedges)
        vs = [rng.randrange(nv) for _ in range(4)]
        ext = merge((vs[0], P), (vs[1], Mq), (vs[2], Qi), (vs[3], Qo))
        dom, c4, full, dr = check_graph('rand', nv, edges, ext, verbose=False)
        stats['n'] += 1
        stats['dom'] += dom
        stats['c4'] += c4
        stats['full'] += full
        stats['dr'] += (dr is True)
        if not full:
            for r in degenerate_reason(nv, edges, ext):
                degen[r] = degen.get(r, 0) + 1
        elif dr is not True:
            degen['full-dim but DR-inadmissible'] = degen.get('full-dim but DR-inadmissible', 0) + 1
    print(stats)
    print("classification of degenerate random graphs:", degen)
    print("(C1) domination must hold for every graph:", stats['dom'] == stats['n'])


def report_other(nmax=8):
    """print a few degenerate random graphs that the simple classifier cannot explain"""
    rng = random.Random(20261010)
    shown = 0
    for trial in range(400):
        nv = rng.choice([3, 4, 5, 6])
        L = rng.choice([1, 2, 3])
        nedges = nv - 1 + L
        if nedges > 9:
            continue
        edges = random_graph(rng, nv, nedges)
        vs = [rng.randrange(nv) for _ in range(4)]
        ext = merge((vs[0], P), (vs[1], Mq), (vs[2], Qi), (vs[3], Qo))
        dom, c4, full, dr = check_graph('rand', nv, edges, ext, verbose=False)
        if not full and degenerate_reason(nv, edges, ext) == ['other']:
            print('  unexplained degenerate graph: nv=%d edges=%s ext=%s' % (nv, edges, ext))
            shown += 1
            if shown >= nmax:
                break
    print('  number of unexplained degenerate graphs shown:', shown)


if __name__ == '__main__':
    print("\n=== degenerate random graphs not explained by self-loops / special bridges / scaleless cut-vertex blocks ===")
    report_other()
