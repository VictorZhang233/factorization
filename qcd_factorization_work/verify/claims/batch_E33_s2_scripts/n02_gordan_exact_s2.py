# N02 stage-2: Collins' Thm 3 (arXiv:2007.04085, thm:main.geom) = Gordan's alternative, checked with EXACT
# rational arithmetic and per-instance CERTIFICATES (stage 1 and the project script used floating point).
#  * Exact min-norm point w of K = conv{D_j}: enumerate affinely independent subsets S, solve the KKT system
#    [G 1; 1^T 0][mu; nu] = [0; 1] in Fractions, keep mu >= 0, and certify global optimality by the variational
#    inequality <w, D_j - w> >= 0 for all j (w = projection of 0 onto K).
#  * Certificates:  w = 0  ->  lambda = mu (on S) is a Landau point (sum lambda_j D_j = 0, lambda >= 0, sum = 1);
#                   w != 0 ->  v = w is a good direction with D_j.w >= |w|^2 > 0 for all j (the claimed margin).
#    Both cannot hold (if v good and lambda Landau: 0 = sum lambda_j D_j(v) > 0), so each instance is classified
#    rigorously.  Independent cross-check of the classification: floating-point LP (scipy.optimize.linprog).
import sys, os, itertools, random
from fractions import Fraction as Fr
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from scipy.optimize import linprog

def dot(u, v): return sum(a*b for a, b in zip(u, v))

def solve(M, b):
    """exact Gauss-Jordan; returns None if singular"""
    n = len(M); A = [row[:] + [b[i]] for i, row in enumerate(M)]
    for c in range(n):
        p = next((r for r in range(c, n) if A[r][c] != 0), None)
        if p is None: return None
        A[c], A[p] = A[p], A[c]
        piv = A[c][c]; A[c] = [x/piv for x in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]; A[r] = [x - f*y for x, y in zip(A[r], A[c])]
    return [A[i][n] for i in range(n)]

def rank(vecs):
    M = [list(v) for v in vecs]; r = 0
    if not M: return 0
    cols = len(M[0])
    for c in range(cols):
        p = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]/M[r][c]; M[i] = [x - f*y for x, y in zip(M[i], M[r])]
        r += 1
    return r

def minnorm(D):
    N, d = len(D), len(D[0])
    for k in range(1, min(N, d + 1) + 1):
        for S in itertools.combinations(range(N), k):
            P = [D[i] for i in S]
            if k > 1 and rank([[a - b for a, b in zip(P[i], P[0])] for i in range(1, k)]) < k - 1: continue
            M = [[dot(P[i], P[j]) for j in range(k)] + [Fr(1)] for i in range(k)] + [[Fr(1)]*k + [Fr(0)]]
            sol = solve(M, [Fr(0)]*k + [Fr(1)])
            if sol is None: continue
            mu = sol[:k]
            if any(m < 0 for m in mu): continue
            w = [sum(mu[i]*P[i][c] for i in range(k)) for c in range(d)]
            ww = dot(w, w)
            if all(dot(w, Dj) >= ww for Dj in D):
                lam = [Fr(0)]*N
                for i, s in enumerate(S): lam[s] = mu[i]
                return w, ww, lam
    raise RuntimeError("no certified face")

def lp_class(D):
    """float LP: max t s.t. D_j.v >= t, -1<=v<=1, t<=1 ; type I iff t* > 1e-9"""
    A = np.array([[float(x) for x in Dj] for Dj in D]); N, d = A.shape
    res = linprog(np.r_[np.zeros(d), -1.0], A_ub=np.c_[-A, np.ones(N)], b_ub=np.zeros(N),
                  bounds=[(-1, 1)]*d + [(None, 1)], method='highs')
    return -res.fun > 1e-9

random.seed(20261011)
cases = []
for _ in range(600):
    d = random.choice([2, 3, 4, 5]); N = random.choice([2, 3, 4, 5, 6, 7])
    cases.append([[Fr(random.randint(-3, 3)) for _ in range(d)] for _ in range(N)])
extra = [[[1, 0], [-1, 0]], [[0, 0], [1, 2]], [[1, 1], [1, 1], [2, 2]], [[1, 0, 0], [0, 1, 0], [-1, -1, 0]],
         [[1, 0, 0], [0, 1, 0], [0, 0, 1]], [[1, 2], [2, 4], [-1, -2]], [[3, -1], [-1, 3], [1, 1]],
         [[1, 0], [0, 1], [-1, 1]], [[1, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, -1], [-1, 0, 0, 1]],
         # massless self-energy at a collinear point: D_1 = 2k, D_2 = -2(p-k) with k = p/5 (light-cone comps.)
         [[2*Fr(1, 5), 2*Fr(1, 5)], [-2*Fr(4, 5), -2*Fr(4, 5)]]]
cases += [[[Fr(x) for x in Dj] for Dj in D] for D in extra]
nI = nII = bad = disagree = 0; worst = None
for D in cases:
    w, ww, lam = minnorm(D)
    if ww == 0:
        nII += 1
        ok = all(l >= 0 for l in lam) and sum(lam) == 1 and all(sum(lam[j]*D[j][c] for j in range(len(D))) == 0 for c in range(len(D[0])))
        bad += (not ok)
        disagree += lp_class(D)          # LP must say: no good direction
    else:
        nI += 1
        m = min(dot(Dj, w) - ww for Dj in D)
        bad += (m < 0)
        worst = m if worst is None else min(worst, m)
        disagree += (not lp_class(D))
print(f"instances: {len(cases)}   type I (good direction, certificate v=w): {nI}   type II (Landau point, certificate lambda): {nII}")
print(f"certificate failures (exact): {bad}    disagreements with an independent float LP classification: {disagree}")
print(f"min over type-I instances of min_j (D_j.w - |w|^2), exact rational: {worst}")
