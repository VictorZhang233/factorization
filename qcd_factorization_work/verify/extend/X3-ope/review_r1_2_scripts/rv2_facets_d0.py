import sys, os, random
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rv2_newton.py')).read().split("if __name__ == '__main__':")[0]
exec(src)
graphs = [("q2 planar ladder", 6, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 5), (1, 4)], merge((0, P), (2, Qi), (3, Qo), (5, Mq))),
          ("q2 crossed ladder", 6, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 4), (1, 5)], merge((0, P), (2, Qi), (3, Qo), (5, Mq))),
          ("q2 3-gluon vertex", 6, [(0, 1), (1, 2), (2, 3), (3, 4), (0, 5), (4, 5), (5, 2)], merge((0, P), (1, Qi), (3, Qo), (4, Mq))),
          ("q3 crossed ladder + extra rung", 8, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (0, 6), (1, 7), (2, 5)], merge((0, P), (3, Qi), (4, Qo), (7, Mq)))]
for name, nv, edges, ext in graphs:
    U, F0, F1 = polys_forest(nv, edges, ext)
    G = dict(U)
    for m, c in F0.items():
        G[m] = G.get(m, 0) + c
    fac = facets_exact(sorted(G))
    N = len(edges)
    d0 = sorted(u for u, d in fac.items() if d == 0)
    coord = [u for u in d0 if sorted(u) == [0] * (N - 1) + [1]]
    other = [u for u in d0 if u not in coord]
    dpos = sorted((u, d) for u, d in fac.items() if d != 0)
    print("%-32s facets=%d  d=0: %d (coordinate %d, other %s)" % (name, len(fac), len(d0), len(coord), other))
    print("     d!=0 facets (normal, d):", dpos)
# random sample: are all d=0 facet normals coordinate vectors?
rng = random.Random(31337)
cnt = dict(full=0, only_coord=0)
examples = []
for trial in range(800):
    nv = rng.choice([3, 4, 5, 6])
    L = rng.choice([1, 2, 3])
    ne = nv - 1 + L
    if ne > 9:
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
    U, F0, F1 = polys_forest(nv, edges, ext)
    G = dict(U)
    for m, c in F0.items():
        G[m] = G.get(m, 0) + c
    pts = sorted(G)
    if int_rank(pts) != ne:
        continue
    cnt['full'] += 1
    fac = facets_exact(pts)
    d0 = [u for u, dd in fac.items() if dd == 0]
    if all(sorted(u) == [0] * (ne - 1) + [1] for u in d0):
        cnt['only_coord'] += 1
    else:
        examples.append((nv, edges, ext, [u for u in d0 if sorted(u) != [0] * (ne - 1) + [1]]))
print("random full-dimensional graphs:", cnt)
for ex in examples[:5]:
    print("   non-coordinate d=0 facets:", ex)
