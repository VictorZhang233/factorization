"""
f7_clifford_slots.py  (X3 final revision)
(a) Euclidean contraction Gamma^(5)_{a1..a5} Gamma^(5)a1..a5 = (-1)^{10} D!/(D-5)! = +D(D-1)(D-2)(D-3)(D-4)
    (explicit matrices, D = 5, 6, 7); erratum to the sign printed in earlier rounds.
(b) Specialisation step of Remark B.1: in even n (4, 6) the 2^n antisymmetrised products gamma^[A] are
    linearly independent; in odd n (5) gamma^[1..n] is central and gamma^[r] is proportional to gamma^[n-r]
    on the irreducible module, so independence fails -> n must be even.
(c) Slot count of Lemma NE (twist-2 block): for 4D dimension d = n+2 enumerate field contents
    (b quark bilinears, a gauge fields, g ghost fields, B auxiliary fields, k derivatives) and the maximal
    number y of mutually symmetric free slots (k + a + b: each bilinear gives at most one slot of a given
    symmetric set).  Check: y >= n  =>  b <= 1; b = 1 => no ghosts/B and a + k = n - 1;
    four-quark contents (b = 2) have y <= n - 2.
Run: python3 -I f7_clifford_slots.py
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np

def euclid_gammas(D):
    s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.array([[1, 0], [0, -1]], complex)
    I2 = np.eye(2)
    def kron(*m):
        out = np.eye(1)
        for x in m: out = np.kron(out, x)
        return out
    gs = []
    npair = D // 2
    for j in range(npair):
        pre = [s3] * j; post = [I2] * (npair - j - 1)
        gs.append(kron(*(pre + [s1] + post))); gs.append(kron(*(pre + [s2] + post)))
    if D % 2 == 1:
        gs.append(kron(*([s3] * npair)))
    return gs

def asym(gs, idx):
    # antisymmetrised product gamma^[i1..ir] for distinct indices = ordered product
    m = np.eye(gs[0].shape[0], dtype=complex)
    for i in idx: m = m @ gs[i]
    return m

ok_all = True
# (a)
for D in (5, 6, 7):
    gs = euclid_gammas(D)
    cliff = all(np.allclose(gs[i] @ gs[j] + gs[j] @ gs[i], 2 * (i == j) * np.eye(gs[0].shape[0])) for i in range(D) for j in range(D))
    tot = np.zeros_like(gs[0])
    for idx in itertools.permutations(range(D), 5):
        g = asym(gs, idx)
        # Gamma_{a1..a5} Gamma^{a1..a5} summed over all ordered distinct tuples (Euclidean, indices raised trivially)
        tot = tot + g @ g
    pred = (+1) * np.prod([D - k for k in range(5)])
    ok = cliff and np.allclose(tot, pred * np.eye(gs[0].shape[0]))
    ok_all &= ok
    print("(a) D=%d: Gamma^(5).Gamma_(5) = %+.1f * 1 ; +D(D-1)(D-2)(D-3)(D-4) = %+d : %s" % (D, tot[0, 0].real, pred, ok))

# (b)
for n in (4, 5, 6):
    gs = euclid_gammas(n)
    mats = []
    for r in range(n + 1):
        for idx in itertools.combinations(range(n), r):
            mats.append(asym(gs, idx).reshape(-1))
    M = np.array(mats)
    rank = np.linalg.matrix_rank(M)
    top = asym(gs, range(n))
    central = all(np.allclose(top @ g, g @ top) for g in gs)
    print("(b) n=%d: #gamma^[A] = %d, rank = %d, independent = %s ; gamma^[1..n] central = %s" % (n, len(mats), rank, rank == len(mats), central))
    if n % 2 == 0:
        ok_all &= (rank == len(mats)) and not central
    else:
        # check gamma^[r] proportional to gamma^[n-r] (complementary index sets) on the irreducible module
        prop = True
        for r in range(n + 1):
            for idx in itertools.combinations(range(n), r):
                comp = [i for i in range(n) if i not in idx]
                A = asym(gs, idx); B = asym(gs, comp)
                c = np.vdot(B.reshape(-1), A.reshape(-1)) / np.vdot(B.reshape(-1), B.reshape(-1))
                prop &= np.allclose(A, c * B)
        print("    n=%d odd: gamma^[r] proportional to gamma^[n-r] for all index sets: %s" % (n, prop))
        ok_all &= (rank < len(mats)) and central and prop

# (c)
viol = 0; maxy4q = {}
for n in range(2, 13):
    d = n + 2
    for b in range(0, d // 3 + 1):
        for a in range(0, d + 1):
            for g in range(0, d + 1):
                for nB in range(0, d // 2 + 1):
                    k = d - 3 * b - a - g - 2 * nB
                    if k < 0: continue
                    if b + a + g + nB < 2: continue          # at least two fields (non-identity operator)
                    y = k + a + b
                    if b == 2: maxy4q[n] = max(maxy4q.get(n, -1), y)
                    if y >= n:
                        if b > 1: viol += 1
                        if b == 1 and not (g == 0 and nB == 0 and a + k == n - 1): viol += 1
                        if b == 0 and (g + 2 * nB + max(0, (a + k) - (a + k))) > 2: viol += 1
print("(c) violations of [y >= n => b <= 1; b = 1 => twist-2 bilinear content] for n = 2..12: %d" % viol)
print("(c) max symmetric rank of four-quark contents at d = n+2: %s (all equal n-2: %s)"
      % (maxy4q, all(v == n - 2 for n, v in maxy4q.items())))
ok_all &= (viol == 0) and all(v == n - 2 for n, v in maxy4q.items())
print("RESULT:", "PASS" if ok_all else "FAIL")
