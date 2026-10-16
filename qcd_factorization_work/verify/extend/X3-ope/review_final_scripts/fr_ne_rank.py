"""
fr_ne_rank.py  (final reviewer, X3)
Independent numerical test of Lemma NE(ii)(gamma): in the twist-2 blocks B^{+-}_n, no D=4-only linear
relation exists among the formal-D tensor monomials of the multidegree in which projected tree vertices live.

Model of a projected tree vertex for field string Phi (D11 / Def. A.2):
  polynomial in vectors  z (null, degree n), [w1, w2 degree 1 each for B^-_n],
  gluon polarisations eps_i (degree 1 each), momenta p_i (total degree K = d - 3b - #A - #c - 2#B),
  Clifford-valued gamma^[r](distinct vectors) with r odd <= 3 for quark sectors (b = 1).
Formal-D basis: products of scalar products (z.z excluded, no eps.eps self / w.w self) times gamma^[r].
Test: evaluate every monomial at random complex vectors in D=4 (Euclidean bilinear form, z null) and in a
large-D proxy (D=10); rank deficiency at D=4 with full rank at D=10 would be a D=4-only relation.
Controls: (1) five generic vectors each of degree 2 (Gram determinant) -> deficiency 1;
          (2) gamma^[5] of five vectors -> vanishes at D=4.
Run: python3 -I fr_ne_rank.py
"""
import sys, os, itertools, math
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np

rng = np.random.default_rng(20261011)

def gammas(D):
    s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.array([[1, 0], [0, -1]], complex)
    I2 = np.eye(2)
    def kron(ms):
        out = np.eye(1)
        for x in ms: out = np.kron(out, x)
        return out
    gs = []
    npair = D // 2
    for j in range(npair):
        pre = [s3] * j; post = [I2] * (npair - j - 1)
        gs.append(kron(pre + [s1] + post)); gs.append(kron(pre + [s2] + post))
    return gs

GAM = {D: gammas(D) for D in (4, 10)}

def slash(v, D):
    return sum(v[a] * GAM[D][a] for a in range(D))

def gamma_r(vs, D):
    r = len(vs)
    dim = GAM[D][0].shape[0]
    if r == 0: return np.eye(dim, dtype=complex)
    sl = [slash(v, D) for v in vs]
    out = np.zeros((dim, dim), complex)
    for perm in itertools.permutations(range(r)):
        sgn = np.linalg.det(np.eye(r)[list(perm)])
        m = np.eye(dim, dtype=complex)
        for i in perm: m = m @ sl[i]
        out += sgn * m
    return out / math.factorial(r)

def rand_vec(D, null=False):
    v = rng.normal(size=D) + 1j * rng.normal(size=D)
    if null:
        v[-1] = 1j * np.sqrt(np.sum(v[:-1] ** 2))
    return v

def pair_monomials(deg):
    """all multisets of unordered pairs (i<=j) of vector labels with prescribed degrees; z.z (label 'z',
    degree constraint) excluded; self-pairs only allowed for labels with degree >= 2 and not 'z'."""
    labels = sorted(k for k in deg if deg[k] > 0)
    pairs = [(a, b) for ia, a in enumerate(labels) for b in labels[ia:] if not (a == b and (a == 'z' or deg[a] < 2))]
    res = []
    def rec(idx, rem, cur):
        if all(v == 0 for v in rem.values()):
            res.append(tuple(cur)); return
        if idx == len(pairs): return
        a, b = pairs[idx]
        # choose multiplicity m of this pair
        maxm = min(rem[a], rem[b]) if a != b else rem[a] // 2
        for m in range(maxm, -1, -1):
            r2 = dict(rem)
            if a == b: r2[a] -= 2 * m
            else: r2[a] -= m; r2[b] -= m
            rec(idx + 1, r2, cur + [(a, b)] * m)
    rec(0, dict(deg), [])
    return res

def monomials(deg, ranks):
    """Clifford-valued monomials: gamma^[r](S) * pair monomial, S a set of distinct labels."""
    labels = sorted(k for k in deg if deg[k] > 0)
    out = []
    for r in ranks:
        for S in itertools.combinations(labels, r):
            d2 = dict(deg)
            for s in S: d2[s] -= 1
            for pm in pair_monomials(d2):
                out.append((S, pm))
    return out

def evaluate(monos, deg, D, nsamp, clifford):
    labels = sorted(deg)
    rows = []
    for _ in range(nsamp):
        vec = {k: rand_vec(D, null=(k == 'z')) for k in labels}
        gcache = {}
        vals = []
        for S, pm in monos:
            sc = 1.0 + 0j
            for a, b in pm: sc *= np.dot(vec[a], vec[b])
            if clifford:
                if S not in gcache: gcache[S] = gamma_r([vec[s] for s in S], D).reshape(-1)
                vals.append(sc * gcache[S])
            else:
                vals.append(np.array([sc]))
        rows.append(np.array(vals).T)   # shape (entries, nmono)
    M = np.vstack(rows)
    return M

def nsamples(monos, clifford):
    """within one sample, Clifford monomials sharing the same gamma^[r](S) are proportional, so the number
    of samples must exceed the largest number of monomials sharing an S (plus margin)."""
    if not clifford: return int(1.5 * len(monos)) + 5
    from collections import Counter
    c = Counter(S for S, pm in monos)
    return max(c.values()) + 6

def rank(M):
    # normalise columns, then numerical rank
    nrm = np.linalg.norm(M, axis=0); nrm[nrm == 0] = 1
    s = np.linalg.svd(M / nrm, compute_uv=False)
    return int(np.sum(s > 1e-8 * s[0])), s

def compositions(K, k):
    if k == 0:
        if K == 0: yield ()
        return
    for c in itertools.product(range(K + 1), repeat=k):
        if sum(c) == K: yield c

def test_sector(name, n, nA, nc, nB, b, minus):
    """sector of B^{+/-}_n: b quark bilinears (0/1), nA gluon legs, nc ghost pairs legs (c and cbar count 2),
    nB B legs; momentum legs = 2b + nA + nc + nB (all independent)."""
    d = n + 2
    K = d - 3 * b - nA - nc - 2 * nB
    if K < 0: return None
    nlegs = 2 * b + nA + nc + nB
    base = {'z': n}
    if minus: base['w1'] = 1; base['w2'] = 1
    for i in range(nA): base['e%d' % i] = 1
    ranks = (1, 3) if b == 1 else (0,)
    worst = (0, 0, 0)
    nmult = 0; tot = 0; defic = 0
    for comp in compositions(K, nlegs):
        deg = dict(base)
        for i, c in enumerate(comp): deg['p%d' % i] = c
        monos = monomials(deg, ranks)
        if not monos: continue
        nm = len(monos)
        ns = nsamples(monos, b == 1)
        r4, _ = rank(evaluate(monos, deg, 4, ns, b == 1))
        r10, _ = rank(evaluate(monos, deg, 10, ns, b == 1))
        nmult += 1; tot += nm
        defic += (nm - r4)
        if r10 != nm: print("   WARNING formal proxy rank deficient", name, n, comp, nm, r10)
        worst = max(worst, (nm - r4, nm, r10))
    return nmult, tot, defic

if __name__ == "__main__":
    print("Controls:")
    deg = {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2}
    monos = monomials(deg, (0,))
    nm = len(monos)
    r4, _ = rank(evaluate(monos, deg, 4, 3 * nm, False)); r10, _ = rank(evaluate(monos, deg, 10, 3 * nm, False))
    print("  (1) 5 vectors x degree 2: #mono=%d rank(D=4)=%d rank(D=10)=%d -> D=4 deficiency %d (Gram det expected 1)" % (nm, r4, r10, nm - r4))
    deg = {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}
    monos = monomials(deg, (5,))
    M4 = evaluate(monos, deg, 4, 3, True); M10 = evaluate(monos, deg, 10, 3, True)
    print("  (2) gamma^[5](a,b,c,d,e): max|.| at D=4 = %.1e, at D=10 = %.1e" % (np.abs(M4).max(), np.abs(M10).max()))
    deg = {'z': 2, 'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}
    monos = monomials(deg, (3,))
    nm = len(monos); ns = nsamples(monos, True); r4, _ = rank(evaluate(monos, deg, 4, ns, True)); r10, _ = rank(evaluate(monos, deg, 10, ns, True))
    print("  (3) rank-3 Dirac, z^2 + 5 vectors deg 1 (non-z supply 5 = n+3 meets demand): #mono=%d rank4=%d rank10=%d deficiency=%d (>=1 expected)" % (nm, r4, r10, nm - r4))
    deg = {'z': 4, 'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}
    monos = monomials(deg, (3,))
    nm = len(monos); ns = nsamples(monos, True); r4, _ = rank(evaluate(monos, deg, 4, ns, True)); r10, _ = rank(evaluate(monos, deg, 10, ns, True))
    print("  (4) rank-3 Dirac, z^4 + 5 vectors deg 1 (supply 5 < n+3 = 7): #mono=%d rank4=%d rank10=%d deficiency=%d (0 expected)" % (nm, r4, r10, nm - r4))
    print()
    print("Twist-2 blocks: sectors (b, #A, #ghost legs, #B) ; total monomials, D=4 deficiency (0 means no D=4-only relation)")
    allok = True
    for minus in (False, True):
        for n in (2, 3, 4, 5):
            for (nm_, nA, nc, nB, b) in [("AA", 2, 0, 0, 0), ("AAA", 3, 0, 0, 0), ("AAAA", 4, 0, 0, 0), ("cc", 0, 2, 0, 0),
                                         ("ccA", 1, 2, 0, 0), ("BA", 1, 0, 1, 0), ("BAA", 2, 0, 1, 0),
                                         ("qq", 0, 0, 0, 1), ("qqA", 1, 0, 0, 1), ("qqAA", 2, 0, 0, 1)]:
                if b == 1 and n > 4 and nA >= 1:  # keep Clifford cases small
                    continue
                res = test_sector(nm_, n, nA, nc, nB, b, minus)
                if res is None: continue
                nmult, tot, defic = res
                if nmult == 0: continue
                allok &= (defic == 0)
                print("  B^%s_%d  %-5s multidegrees=%3d  monomials=%5d  D=4 deficiency=%d" % ('-' if minus else '+', n, nm_, nmult, tot, defic))
    print("RESULT:", "PASS (no D=4-only relation in any tested twist-2 sector)" if allok else "FAIL")
