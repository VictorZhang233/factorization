"""
Reviewer check R2: targeted test of claim (c) of R1 on random 2-connected loopless (multi)graphs G° built by
ear decompositions; one random edge of G° is declared the q-line J1--J2, G = G° minus that edge, and the p-legs are
put on random vertices (irrelevant for U + F0).  Expect: Newt(U+F0) full-dimensional, and all facets with d_u = 0
are coordinate facets (DR admissible).
"""
import sys, random, time
sys.path.insert(0, sys.argv[1])
import r1_matroid_criterion as R


def random_2connected(rng, n_edges_target):
    # start with a cycle (or a double edge), then add ears (paths between existing vertices, possibly length 1)
    k = rng.choice([2, 3, 4])
    nv = k
    edges = [(i, (i + 1) % k) for i in range(k)] if k > 2 else [(0, 1), (0, 1)]
    while len(edges) < n_edges_target:
        a, b = rng.sample(range(nv), 2) if nv >= 2 else (0, 0)
        ln = rng.choice([1, 1, 2, 2, 3])
        ln = min(ln, n_edges_target - len(edges))
        if ln == 1:
            edges.append((a, b))
        else:
            prev = a
            for j in range(ln - 1):
                edges.append((prev, nv))
                prev = nv
                nv += 1
            edges.append((prev, b))
    return nv, edges


rng = random.Random(4242)
ntr = int(sys.argv[2]) if len(sys.argv) > 2 else 40
cnt = dict(n=0, full=0, crit=0, auto=0)
fails = []
t0 = time.time()
for t in range(ntr):
    nE = rng.choice([4, 5, 6, 7, 8, 9, 10, 11])
    nv, Gq = random_2connected(rng, nE)
    iq = rng.randrange(len(Gq))
    J1, J2 = Gq[iq]
    G = [e for i, e in enumerate(Gq) if i != iq]
    if len(G) > 10:
        continue
    ext = {}
    for v, mom in [(rng.randrange(nv), (1, 0)), (rng.randrange(nv), (-1, 0)), (J1, (0, 1)), (J2, (0, -1))]:
        a = ext.get(v, (0, 0))
        ext[v] = (a[0] + mom[0], a[1] + mom[1])
    if [m[1] for m in ext.values()].count(1) != 1:
        continue
    res = R.analyse(nv, G, ext)
    cnt['n'] += 1
    cnt['full'] += res['full']
    cnt['crit'] += res['crit']
    if res['full'] and res['dr_auto']:
        cnt['auto'] += 1
    else:
        fails.append((nv, G, (J1, J2), res['full'], res['dr_auto']))
print('targeted 2-connected samples:', cnt, '; failures:', fails[:5], '; time %.0fs' % (time.time() - t0))
