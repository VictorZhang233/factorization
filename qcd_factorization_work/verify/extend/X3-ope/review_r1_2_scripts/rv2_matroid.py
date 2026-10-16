"""Check: supp(U + F0hat) == projection of the bases of the cographic matroid of Gamma+ = Gamma + {J1J2}
(complements of spanning trees of Gamma+, with the virtual-edge coordinate dropped); hence Newt(U+F0hat) is
affinely isomorphic to the matroid base polytope B(M*(Gamma+)) and Edmonds' description gives all facets."""
import sys, os, random, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
here = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(here, 'rv2_newton.py')).read().split("if __name__ == '__main__':")[0])
f1 = "/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/scripts/f1_forward_graphs.py"
src = open(f1).read()
ns = {}
exec(src[src.index("P, Mq = (1, 0), (-1, 0)"):src.index("def degenerate_reason")], ns)
def spanning_trees(nv, edges):
    out = []
    for S in itertools.combinations(range(len(edges)), nv - 1):
        d = DSU(nv)
        if all(d.u(*edges[i]) for i in S):
            out.append(set(S))
    return out
def check(nv, edges, ext):
    J1 = [v for v in range(nv) if ext.get(v, (0, 0))[1] > 0][0]
    J2 = [v for v in range(nv) if ext.get(v, (0, 0))[1] < 0][0]
    U, F0, F1 = polys_forest(nv, edges, ext)
    supp = set(U) | set(F0)
    E = len(edges)
    plus = list(edges) + [(J1, J2)]
    proj = set()
    for T in spanning_trees(nv, plus):
        comp = tuple(0 if i in T else 1 for i in range(E))   # drop the virtual coordinate
        proj.add(comp)
    return supp == proj, len(supp)
allok = True
for name, nv, edges, ext in ns['graphs']:
    ok, n = check(nv, edges, ext)
    allok &= ok
print("f1 explicit graphs: supp(U+F0hat) == projected cographic bases of Gamma+ for all 21:", allok)
rng = random.Random(2718)
good = tot = 0
for trial in range(300):
    nv = rng.choice([3, 4, 5, 6]); L = rng.choice([1, 2, 3]); ne = nv - 1 + L
    if ne > 9: continue
    while True:
        edges = [(rng.randrange(nv), rng.randrange(nv)) for _ in range(ne)]
        d = DSU(nv)
        for a, b in edges: d.u(a, b)
        if len({d.f(v) for v in range(nv)}) == 1: break
    vs = [rng.randrange(nv) for _ in range(4)]
    if vs[2] == vs[3]: continue
    ext = merge((vs[0], P), (vs[1], Mq), (vs[2], Qi), (vs[3], Qo))
    ok, n = check(nv, edges, ext)
    tot += 1; good += ok
print("random graphs (J1 != J2, self-loops/multi-edges allowed): identity holds in %d / %d" % (good, tot))
