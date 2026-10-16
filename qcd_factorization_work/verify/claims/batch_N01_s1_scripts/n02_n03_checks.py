# Independent checks for N02 (Gordan / min-norm margin) and N03 (momentum-space Landau / Coleman-Norton).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from scipy.optimize import linprog

rng = np.random.default_rng(777)

def wolfe_mnp(P, tol=1e-12, maxit=10000):
    """Wolfe (1976) minimum-norm-point algorithm for conv{rows of P}. Returns (x, weights)."""
    N, d = P.shape
    j = int(np.argmin(np.sum(P**2, axis=1)))
    S = [j]; lam = np.array([1.0])
    x = P[j].copy()
    for _ in range(maxit):
        # major cycle: find point minimizing <x, p>
        k = int(np.argmin(P @ x))
        if x @ x - x @ P[k] <= tol * max(1.0, np.max(np.sum(P**2, axis=1))) or k in S:
            break
        S.append(k); lam = np.append(lam, 0.0)
        while True:   # minor cycle
            Q = P[S]
            # affine minimizer of the support: solve [Q Q^T 1; 1^T 0][mu; t] = [0; 1]
            G = Q @ Q.T; m = len(S)
            A = np.zeros((m + 1, m + 1)); A[:m, :m] = G; A[:m, m] = 1; A[m, :m] = 1
            b = np.zeros(m + 1); b[m] = 1
            mu = np.linalg.lstsq(A, b, rcond=None)[0][:m]
            if np.all(mu > tol):
                lam = mu; x = lam @ Q; break
            # move toward mu until a weight hits zero
            idx = mu <= tol
            th = np.min(lam[idx] / (lam[idx] - mu[idx]))
            lam = lam + th * (mu - lam)
            keep = lam > tol
            S = [s for s, kk in zip(S, keep) if kk]; lam = lam[keep]; lam = lam / lam.sum()
            x = lam @ P[S]
    w = np.zeros(N); w[S] = lam
    return x, w

def lp_landau(D):
    N, d = D.shape
    r = linprog(np.zeros(N), A_eq=np.vstack([D.T, np.ones((1, N))]),
                b_eq=np.concatenate([np.zeros(d), [1.0]]), bounds=[(0, None)] * N, method='highs')
    return r.status == 0

nI = nII = bad = 0; worst = np.inf
for trial in range(600):
    d = int(rng.integers(1, 8)); N = int(rng.integers(1, 10))
    D = rng.normal(size=(N, d))
    mode = trial % 4
    if mode == 1 and N >= 2:          # force a Landau point
        l = rng.dirichlet(np.ones(N)); D[-1] = -(l[:-1] @ D[:-1]) / l[-1]
    elif mode == 2:                   # a zero dual vector (soft-line analogue)
        D[0] = 0.0
    elif mode == 3 and N >= 2:        # duplicates
        D[1] = D[0]
    x, w = wolfe_mnp(D)
    nx = np.linalg.norm(x); landau = lp_landau(D)
    if nx > 1e-8:
        nI += 1
        marg = np.min(D @ x) - nx**2
        worst = min(worst, marg / nx**2)
        if marg < -1e-9 * nx**2 or landau:
            bad += 1
    else:
        nII += 1
        if not landau:
            bad += 1
print(f"N02: {nI} good-direction cases, {nII} Landau cases, inconsistencies = {bad}, worst relative margin (D_j.w-|w|^2)/|w|^2 = {worst:.2e}")

# ---------------- N03: loop equations <=> vertex positions (graph theory) ----------------
def random_graph(nv, ne):
    edges = [(i, int(rng.integers(0, i))) for i in range(1, nv)]       # spanning tree
    while len(edges) < ne:
        a, b = rng.integers(0, nv, size=2)
        if a != b: edges.append((int(a), int(b)))
    return edges
ok = True; cnt = 0
for trial in range(300):
    nv = int(rng.integers(2, 8)); ne = int(rng.integers(nv - 1, nv + 6))
    E = random_graph(nv, ne)
    Inc = np.zeros((ne, nv))
    for j, (h, t) in enumerate(E):
        Inc[j, h] += 1; Inc[j, t] -= 1
    # cycle space basis = null space of Inc^T (edge vectors c with sum_j c_j Inc[j,:] = 0)
    u, s, vt = np.linalg.svd(Inc.T)
    rank = int(np.sum(s > 1e-10)); C = vt[rank:].T          # ne x L, columns span the cycle space ("eta")
    for case in range(2):
        if case == 0:   # displacements from a potential => loop equations hold
            X = rng.normal(size=(nv, 4)); disp = Inc @ X
        else:           # generic displacements
            disp = rng.normal(size=(ne, 4))
        loop_ok = np.allclose(C.T @ disp, 0, atol=1e-9) if C.shape[1] > 0 else True
        sol, res, rk, sv = np.linalg.lstsq(Inc, disp, rcond=None)
        pos_ok = np.allclose(Inc @ sol, disp, atol=1e-8)
        ok &= (loop_ok == pos_ok); cnt += 1
print(f"N03: loop equations <=> existence of vertex positions on {cnt} random graph instances: {ok}")

# toy: gluon k (k^2+i0), Wilson line (n.k+i0), quark (p-k)^2+i0; loop momentum k, eta = (+1,+1,-1)
eta = np.diag([1.0, -1, -1, -1])
n = np.array([1.0, 0, 0, -1.0]); p = np.array([1.0, 0, 0, 1.0])
for alpha in [-0.7, 0.7]:
    k = alpha * n
    D = []
    if abs(k @ eta @ k) < 1e-12: D.append(2 * eta @ k)                 # gluon on shell
    if abs(n @ eta @ k) < 1e-12: D.append(eta @ n)                     # eikonal denominator vanishes
    q = p - k
    if abs(q @ eta @ q) < 1e-12: D.append(-2 * eta @ q)                # quark on shell
    D = np.array(D)
    print(f"N03 toy: k = {alpha:+.1f} n  ->  Landau point (trapped by Collins Thm 1): {lp_landau(D)}")
