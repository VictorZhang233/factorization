# library for the NE rank diagnostics (exec'd by c2_ne_dcheck.py and c2_ne_relation.py)
import itertools, random
import numpy as np
import sympy as sp
from fractions import Fraction
from math import gcd

P = 2147483647
random.seed(2024)

def perfect_matchings(items):
    items = list(items)
    if not items:
        yield []
        return
    a = items[0]
    for i in range(1, len(items)):
        rest = items[1:i] + items[i+1:]
        for m in perfect_matchings(rest):
            yield [(a, items[i])] + m

def structures(n, S, rp):
    out = []
    vs = list(range(S))
    for ZD in ([0, 1] if rp >= 1 else [0]):
        Asets = ([('z',) + c for c in itertools.combinations(vs, rp-1)] if ZD == 1
                 else [c for c in itertools.combinations(vs, rp)])
        for A in Asets:
            usedA = [a for a in A if a != 'z']
            rem = [v for v in vs if v not in usedA]
            nz = n - ZD
            if nz > len(rem): continue
            for zp in itertools.combinations(rem, nz):
                left = [v for v in rem if v not in zp]
                if len(left) % 2: continue
                for m in perfect_matchings(left):
                    out.append((A, zp, tuple(m)))
    return out

def rand_null_D(D):
    k = D//2
    x = [random.randint(-99, 99) for _ in range(k)]
    while all(v == 0 for v in x): x = [random.randint(-99, 99) for _ in range(k)]
    A = sp.zeros(k, k)
    for i in range(k):
        for j in range(i+1, k):
            # rational skew entries with a wide range: the rotation parameter must take many values,
            # otherwise high-degree polynomials in z are not detected (first version used integers in [-5,5]
            # -> only 11 rotations in D=4 -> spurious rank deficiencies for n>=6)
            a = sp.Rational(random.randint(-997, 997), random.randint(1, 991)); A[i, j] = a; A[j, i] = -a
    I = sp.eye(k)
    R = (I - A) * (I + A).inv()
    y = list(R * sp.Matrix(x))
    z = [sp.Rational(v) for v in x] + y
    L = 1
    for v in z: L = L * sp.Rational(v).q // gcd(L, sp.Rational(v).q)
    zi = [int(v * L) for v in z]
    assert sum(zi[i]**2 for i in range(k)) - sum(zi[k+i]**2 for i in range(k)) == 0
    return zi

def dot_D(u, v, D):
    k = D//2
    return sum(u[i]*v[i] for i in range(k)) - sum(u[k+i]*v[k+i] for i in range(k))

def det_int(M):
    n = len(M)
    if n == 0: return 1
    if n == 1: return M[0][0]
    if n == 2: return M[0][0]*M[1][1]-M[0][1]*M[1][0]
    s = 0
    for j in range(n):
        minor = [row[:j]+row[j+1:] for row in M[1:]]
        s += (-1)**j * M[0][j] * det_int(minor)
    return s

def wedge_int_D(vecs, D):
    r = len(vecs)
    if r == 0: return [1]
    return [det_int([[v[i] for i in idx] for v in vecs]) for idx in itertools.combinations(range(D), r)]

def rank_mod_p(rows):
    A = np.array(rows, dtype=np.int64) % P
    nr, nc = A.shape
    rank = 0
    for col in range(nc):
        if rank == nr: break
        nzr = np.nonzero(A[rank:, col])[0]
        if len(nzr) == 0: continue
        piv = rank + nzr[0]
        if piv != rank: A[[rank, piv]] = A[[piv, rank]]
        inv = pow(int(A[rank, col]), P-2, P)
        A[rank] = (A[rank] * inv) % P
        others = np.nonzero(A[:, col])[0]
        others = others[others != rank]
        if len(others):
            f = A[others, col].reshape(-1, 1)
            A[others] = (A[others] - (f * A[rank]) % P) % P
        rank += 1
    return rank

def eval_rows(st, n, S, rp, D, npts, exact=False):
    ncomp = len(list(itertools.combinations(range(D), rp)))
    cols = []
    for _ in range(npts):
        z = rand_null_D(D)
        vs = [[random.randint(-30, 30) for _ in range(D)] for _ in range(S)]
        block = []
        for (A, zp, m) in st:
            vecs = [z if a == 'z' else vs[a] for a in A]
            val = 1
            for v in zp: val = val * dot_D(z, vs[v], D)
            for (a, b) in m: val = val * dot_D(vs[a], vs[b], D)
            w = wedge_int_D(vecs, D)
            block.append([val * c if exact else (val * c) % P for c in w])
        cols.append(block)
    return [[c for blk in cols for c in blk[i]] for i in range(len(st))]

def test_D(n, S, rp, D, npts=None):
    st = structures(n, S, rp)
    ns = len(st)
    if ns == 0: return 0, 0
    ncomp = len(list(itertools.combinations(range(D), rp)))
    if npts is None: npts = ns // ncomp + 8
    rows = eval_rows(st, n, S, rp, D, npts)
    return ns, rank_mod_p(rows)
