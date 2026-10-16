import sys, os, random
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
here = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(here, 'rv2_newton.py')).read().split("if __name__ == '__main__':")[0])
# the 21 explicit graphs of the X3 script f1 (read as data: only the 'graphs' list construction is executed)
f1 = "/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/scripts/f1_forward_graphs.py"
src = open(f1).read()
start = src.index("P, Mq = (1, 0), (-1, 0)")
stop = src.index("def degenerate_reason")
ns = {}
exec(src[start:stop], ns)
glist = ns['graphs']
def d0_report(nv, edges, ext):
    U, F0, F1 = polys_forest(nv, edges, ext)
    G = dict(U)
    for m, c in F0.items():
        G[m] = G.get(m, 0) + c
    pts = sorted(G)
    N = len(edges)
    if int_rank(pts) != N:
        return None
    fac = facets_exact(pts)
    d0 = [u for u, d in fac.items() if d == 0]
    noncoord = [u for u in d0 if sorted(u) != [0] * (N - 1) + [1]]
    return len(fac), len(d0), noncoord
ok = 0
for name, nv, edges, ext in glist:
    r = d0_report(nv, edges, ext)
    ok += (r is not None and not r[2])
    print("%-42s facets=%s d0=%s non-coordinate d0 facets=%s" % (name, r and r[0], r and r[1], r and r[2]))
print("f1 explicit graphs with only coordinate d=0 facets: %d / %d" % (ok, len(glist)))
rng = random.Random(8086)
cnt = dict(tested=0, full=0, only_coord=0)
for trial in range(700):
    nv = rng.choice([4, 5, 6, 7])
    L = rng.choice([2, 3, 4])
    ne = nv - 1 + L
    if ne > 10:
        continue
    while True:
        edges = [(rng.randrange(nv), rng.randrange(nv)) for _ in range(ne)]
        d = DSU(nv)
        for a, b in edges:
            d.u(a, b)
        if len({d.f(v) for v in range(nv)}) == 1 and all(a != b for a, b in edges):
            break
    vs = [rng.randrange(nv) for _ in range(4)]
    ext = merge((vs[0], P), (vs[1], Mq), (vs[2], Qi), (vs[3], Qo))
    cnt['tested'] += 1
    r = d0_report(nv, edges, ext)
    if r is None:
        continue
    cnt['full'] += 1
    cnt['only_coord'] += (not r[2])
    if r[2]:
        print("  COUNTEREXAMPLE candidate:", nv, edges, ext, r)
print("random loopless graphs (N<=10, L=2..4):", cnt)
