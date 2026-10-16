"""
f3_matroid_lemma.py -- independent check of Lemma F.6 of the revised X3 report ("discharge of (F-DR)").

For a connected forward graph G (N lines, L loops; p at P1, -p at P2, q at J1, -q at J2, J1 != J2) let
G0 = G + {virtual line e_q joining J1 and J2}.  Lemma F.6 states:
  (a) F0hat = U(G/{J1=J2})   and   U(G0) = x_q U(G) + U(G/{J1=J2})       (deletion-contraction on e_q);
      hence supp(U + F0hat) = pi(supp U(G0)), pi = "drop the x_q coordinate", injective on supp U(G0);
      supp U(G0) = indicator vectors of the bases of the cographic matroid M*(G0) (complements of spanning trees).
  (b) dim Newt(U + F0hat) = N + 1 - c(M(G0))  (Feichtner-Sturmfels Prop. 2.4; c = number of connected components
      of the matroid, equal for M and M*), so Newt is full-dimensional iff M(G0) is connected iff G0 is loopless
      and has no cut vertex (2-connected).
  (c) every facet of a full-dimensional Newt(U + F0hat) is one of
        u = e_e        d = 0                       (coordinate facet)
        u = -1         d = -(L+1)                  (from x_q >= 0)
        u = -1_F       d = -r*(F)    F a flat of M*(G0) with q not in F   (d < 0 since G0 has no bridges)
        u = 1_{E\F'}   d = L+1-r*(F' u {q})        F' u {q} a flat of M*(G0)  (d > 0 unless F' u q = E0)
      (Feichtner-Sturmfels Prop. 2.3: P_M = {x >= 0, x(E0) = rank, x(F) <= rank(F) for flats F}).
      Consequence: d_u = 0 only for coordinate facets, so no polar hyperplane <u,a> - (D/2) d_u = -k of the
      meromorphically continued Lee-Pomeransky integral is D-independent except a_e in -N0: DR is admissible
      for every choice of positive line powers a_e (Tarasov shifts, Taylor terms).
Checks: the 21 explicit QCD forward topologies of f1 and random multigraphs (loops, multi-edges, coinciding
external vertices allowed; J1 != J2).  Facets are computed with qhull and then verified EXACTLY (integer normal,
exact value d, exact affine rank N-1 of the tight point set, exact validity on all points).
Run:  python3 -I f3_matroid_lemma.py
"""
import sys, os, itertools, random
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction
import numpy as np
import f1_forward_graphs as f1          # graph list, forest enumeration, Symanzik polynomials, qhull facets


# ------------------------------------------------------------------ exact linear algebra
def exact_rank(rows):
    """rank over Q of a list of integer vectors (fraction-free Gaussian elimination)"""
    M = [[Fraction(x) for x in r] for r in rows]
    if not M:
        return 0
    rank, ncol = 0, len(M[0])
    for c in range(ncol):
        piv = None
        for r in range(rank, len(M)):
            if M[r][c] != 0:
                piv = r
                break
        if piv is None:
            continue
        M[rank], M[piv] = M[piv], M[rank]
        for r in range(len(M)):
            if r != rank and M[r][c] != 0:
                f = M[r][c] / M[rank][c]
                M[r] = [a - f * b for a, b in zip(M[r], M[rank])]
        rank += 1
    return rank


def affine_rank(points):
    pts = list(points)
    if len(pts) <= 1:
        return 0
    p0 = pts[0]
    return exact_rank([[a - b for a, b in zip(p, p0)] for p in pts[1:]])


# ------------------------------------------------------------------ graphic / cographic matroid
def n_components(nv, edge_subset):
    d = f1.DSU(nv)
    for (u, v) in edge_subset:
        d.union(u, v)
    return len({d.find(w) for w in range(nv)})


def graphic_rank(nv, edges, S):
    return nv - n_components(nv, [edges[i] for i in S])


def cographic_rank(nv, edges, S):
    E0 = set(range(len(edges)))
    rE = graphic_rank(nv, edges, E0)
    return len(S) - rE + graphic_rank(nv, edges, E0 - set(S))


def is_flat(nv, edges, S, rankfun):
    S = set(S)
    r = rankfun(nv, edges, S)
    return all(rankfun(nv, edges, S | {e}) > r for e in range(len(edges)) if e not in S)


def matroid_components(nv, edges):
    """connected components of the cycle matroid M(G): e ~ f iff a circuit (simple cycle, or a loop) contains both"""
    m = len(edges)
    dsu = f1.DSU(m)
    for k in range(1, m + 1):
        for S in itertools.combinations(range(m), k):
            sub = [edges[i] for i in S]
            if k == 1:
                if sub[0][0] == sub[0][1]:
                    pass                      # a loop is a circuit by itself
                continue
            # circuit test: every vertex touched has degree 2, connected, |S| = |V(S)|, no loops inside
            if any(u == v for (u, v) in sub):
                continue
            deg = {}
            for (u, v) in sub:
                deg[u] = deg.get(u, 0) + 1
                deg[v] = deg.get(v, 0) + 1
            if any(dg != 2 for dg in deg.values()) or len(deg) != k:
                continue
            verts = sorted(deg)
            idx = {v: i for i, v in enumerate(verts)}
            d = f1.DSU(len(verts))
            for (u, v) in sub:
                d.union(idx[u], idx[v])
            if len({d.find(i) for i in range(len(verts))}) != 1:
                continue
            for i in S[1:]:
                dsu.union(S[0], i)
    return len({dsu.find(i) for i in range(m)})


def loopless_2connected(nv, edges):
    """graph-theoretic criterion (no loops, at least 2 edges, connected, no cut vertex among touched vertices)"""
    if any(u == v for (u, v) in edges) or len(edges) < 2:
        return False
    used = sorted({x for e in edges for x in e})
    if n_components(nv, edges) - (nv - len(used)) != 1:
        return False
    for w in used:
        rest = [(u, v) for (u, v) in edges if u != w and v != w]
        others = [x for x in used if x != w]
        d = f1.DSU(nv)
        for (u, v) in rest:
            d.union(u, v)
        if len({d.find(x) for x in others}) > 1:
            return False
    return True


# ------------------------------------------------------------------ the lemma on one graph
def spanning_tree_poly(nv, edges):
    """U polynomial as dict {exponent tuple: coefficient}: monomial = product of lines NOT in the tree"""
    U = {}
    for S, comps in f1.forests(nv, edges, 1):
        m = tuple(0 if i in S else 1 for i in range(len(edges)))
        U[m] = U.get(m, 0) + 1
    return U


def contract(nv, edges, a, b):
    """identify vertices a and b (b -> a), relabel to 0..nv-2"""
    lab = {}
    k = 0
    for v in range(nv):
        if v == b:
            continue
        lab[v] = k
        k += 1
    lab[b] = lab[a]
    return nv - 1, [(lab[u], lab[v]) for (u, v) in edges]


def check(name, nv, edges, ext, verbose=True):
    J1 = [v for v in range(nv) if ext.get(v, (0, 0))[1] == 1]
    J2 = [v for v in range(nv) if ext.get(v, (0, 0))[1] == -1]
    if len(J1) != 1 or len(J2) != 1:
        return None                               # both currents at one vertex: no q flow (not a QCD graph)
    J1, J2 = J1[0], J2[0]
    N = len(edges)
    L = N - nv + 1
    U, F0, F1 = f1.symanzik(nv, edges, ext)
    G0 = edges + [(J1, J2)]                       # virtual line e_q has index N
    U0 = spanning_tree_poly(nv, G0)
    ncv, cedges = contract(nv, edges, J1, J2)
    Uc = spanning_tree_poly(ncv, cedges)
    res = {}
    # (a) deletion-contraction and support identity
    rhs = {}
    for m, c in U.items():
        rhs[m + (1,)] = rhs.get(m + (1,), 0) + c
    for m, c in Uc.items():
        rhs[m + (0,)] = rhs.get(m + (0,), 0) + c
    res['F0=U(G/J1J2)'] = (F0 == Uc)
    res['U(G0)=xqU+U(G/J1J2)'] = (U0 == rhs)
    supp = set(U) | set(F0)
    proj = [m[:N] for m in U0]
    res['supp=proj, injective'] = (set(proj) == supp and len(set(proj)) == len(proj))
    res['all coefficients 1'] = all(c == 1 for c in list(U.values()) + list(F0.values()))
    # (b) dimension formula and criterion
    pts = sorted(supp)
    dim = affine_rank(pts)
    cM = matroid_components(nv, G0)
    crit = loopless_2connected(nv, G0)
    res['dim = N+1-c(M(G0))'] = (dim == N + 1 - cM)
    res['full <=> loopless&2-conn'] = ((dim == N) == crit)
    full = (dim == N)
    nfac = None
    if full:
        # (c) facets: qhull normals, then exact verification and classification
        normals = f1.facet_normals(pts)
        nfac = len(normals)
        ok_exact, ok_class, ok_d0 = True, True, True
        rE0 = graphic_rank(nv, G0, set(range(N + 1)))
        rstar = lambda S: cographic_rank(nv, G0, S)
        assert rstar(set(range(N + 1))) == L + 1
        for u in normals:
            vals = [sum(ui * mi for ui, mi in zip(u, m)) for m in pts]
            d = min(vals)
            tight = [m for m, vv in zip(pts, vals) if vv == d]
            if affine_rank(tight) != N - 1:
                ok_exact = False
            ent = set(u)
            if d == 0 and not (sorted(u).count(1) == 1 and ent <= {0, 1}):
                ok_d0 = False                     # a d = 0 facet that is not a coordinate facet
            if ent <= {0, 1} and sum(u) == 1:     # u = e_e : facet of the simplex (x_e >= 0)
                good = (d == 0)
            elif ent <= {0, 1} and sum(u) >= 2:   # u = 1_{E \ F'} with F' u {q} a flat of M*(G0)
                Fp = {e for e in range(N) if u[e] == 0} | {N}
                good = is_flat(nv, G0, Fp, cographic_rank) and d == L + 1 - rstar(Fp) and d > 0
            elif ent <= {0, -1} and sum(u) <= -1:
                Fs = {e for e in range(N) if u[e] == -1}
                if len(Fs) == N:                  # u = -1 : from x_q >= 0
                    good = (d == -(L + 1))
                else:
                    good = is_flat(nv, G0, Fs, cographic_rank) and d == -rstar(Fs) and d < 0
            else:
                good = False
            ok_class &= good
        res['facets exact'] = ok_exact
        res['facets of matroid type'] = ok_class
        res['d=0 => coordinate'] = ok_d0
    if verbose:
        flags = ' '.join('%s=%s' % (k, v) for k, v in res.items())
        print("%-40s N=%2d L=%d full=%s facets=%s %s" % (name, N, L, full, nfac, flags))
    return res, full


if __name__ == '__main__':
    print("=== explicit QCD forward topologies (f1) ===")
    allok = True
    for name, nv, edges, ext in f1.graphs:
        r = check(name, nv, edges, ext)
        res, full = r
        allok &= all(res.values()) and full
    print("ALL explicit graphs: every check true and full-dimensional:", allok)

    print("\n=== random connected multigraphs (loops, multi-edges, coinciding external vertices allowed; J1 != J2) ===")
    rng = random.Random(20261011)
    stats = {'graphs': 0, 'full': 0}
    fails = {}
    for trial in range(1500):
        nv = rng.choice([2, 3, 4, 5, 6])
        L = rng.choice([1, 2, 3])
        ne = nv - 1 + L
        if ne > 9:
            continue
        edges = f1.random_graph(rng, nv, ne)
        vs = [rng.randrange(nv) for _ in range(4)]
        if vs[2] == vs[3]:
            continue
        ext = f1.merge((vs[0], f1.P), (vs[1], f1.Mq), (vs[2], f1.Qi), (vs[3], f1.Qo))
        r = check('rand', nv, edges, ext, verbose=False)
        if r is None:
            continue
        res, full = r
        stats['graphs'] += 1
        stats['full'] += full
        for k, v in res.items():
            if not v:
                fails[k] = fails.get(k, 0) + 1
    print(stats)
    print("failed checks (count):", fails if fails else "none")
