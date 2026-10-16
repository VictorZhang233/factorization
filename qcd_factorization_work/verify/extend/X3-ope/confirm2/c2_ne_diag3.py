#!/usr/bin/env python3
"""Diagnostic 3: b=0 (r'=0), n=7, S=11 -- is the deficiency found with npts=ns+10 genuine?
 (i) D=4 with npts = ns+400, two different primes; (ii) D=6, 8 with npts = ns+50."""
import sys, os, itertools, random
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'c2_ne_lib.py')).read())
import numpy as np

def rank_mod(rows, p):
    A = np.array(rows, dtype=object)
    A = np.array([[int(x) % p for x in r] for r in rows], dtype=np.int64)
    nr, nc = A.shape; rank = 0
    for col in range(nc):
        if rank == nr: break
        nzr = np.nonzero(A[rank:, col])[0]
        if len(nzr) == 0: continue
        piv = rank + nzr[0]
        if piv != rank: A[[rank, piv]] = A[[piv, rank]]
        inv = pow(int(A[rank, col]), p-2, p)
        A[rank] = (A[rank] * inv) % p
        others = np.nonzero(A[:, col])[0]; others = others[others != rank]
        if len(others):
            f = A[others, col].reshape(-1, 1)
            A[others] = (A[others] - (f * A[rank]) % p) % p
        rank += 1
    return rank

def rows_exact(n, S, rp, D, npts, seed):
    random.seed(seed)
    st = structures(n, S, rp); ns = len(st)
    comps = list(itertools.combinations(range(D), rp))
    rows = [[0]*npts for _ in range(ns)]
    for j in range(npts):
        z = rand_null_D(D)
        vs = [[random.randint(-1000, 1000) for _ in range(D)] for _ in range(S)]
        xi = [random.randint(-50, 50) for _ in comps]
        for i, (A, zp, m) in enumerate(st):
            vecs = [z if a == 'z' else vs[a] for a in A]
            val = 1
            for v in zp: val *= dot_D(z, vs[v], D)
            for (a, b) in m: val *= dot_D(vs[a], vs[b], D)
            w = wedge_int_D(vecs, D)
            rows[i][j] = val * sum(c*x for c, x in zip(w, xi))
    return ns, rows

for (n, S, rp, D, extra, seed) in [(7, 11, 0, 4, 400, 1), (7, 11, 0, 4, 400, 2), (7, 11, 0, 6, 60, 3), (6, 10, 0, 4, 200, 4)]:
    ns, rows = rows_exact(n, S, rp, D, ns_ := None or (len(structures(n, S, rp)) + extra), seed)
    for p in [2147483647, 2305843009213693951 % (2**31) and 1000000007]:
        rk = rank_mod(rows, p)
        print(f"n={n} S={S} r'={rp} D={D} npts={ns+extra} p={p}: #struct={ns} rank={rk} {'FULL' if rk==ns else 'deficiency '+str(ns-rk)}", flush=True)
