"""f6_evanescent_tree.py -- X3 fix round 2: evanescent Dirac structures in the
D-dimensional J^mu J^nu OPE (Theorem A, hypothesis (NE)).

Checks, with explicit Euclidean Clifford matrices:
 (a) the totally antisymmetric product gamma^[a1 .. a5] vanishes identically
     in D = 4 and is non-zero in D = 5, 6 (so rank-5 structures are
     evanescent);
 (b) the tree-level hard part of the quark line with the two currents and one
     soft gluon (index alpha, momentum l), at first order in the soft momenta
     (k = soft quark momentum), s- plus u-channel,
        X = g^nu (k+l)sl g^alpha q sl g^mu + g^nu q sl g^alpha k sl g^mu
          + g^mu (k+l)sl g^alpha (-q)sl g^nu + g^mu (-q)sl g^alpha k sl g^nu
     (numerators only; the common 1/q^4 is dropped; terms with two q's have
     no rank-5 part), has rank-5 component exactly 2 g^[nu l alpha q mu]:
     the k-terms cancel, the l-terms add.  It is antisymmetric in (mu nu); its
     (mu nu)-symmetric part has no rank-5 component.  Hence the D-dimensional
     OPE contains, already at tree level (order g), the evanescent dimension-5
     operator  psibar gamma^[nu sigma alpha rho mu] q_rho F_{sigma alpha} psi
     (coefficient ~ q_rho/q^4), in the (mu nu)-antisymmetric channel only.
 (c) the rank-5 component is zero when all vectors and indices lie in a 4-dim
     subspace (D = 6 matrices, 4-dim kinematics).
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np

rng = np.random.default_rng(11)
s0 = np.eye(2); s1 = np.array([[0, 1], [1, 0]], complex)
s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.array([[1, 0], [0, -1]], complex)

def kron(*ms):
    out = np.array([[1.0 + 0j]])
    for m in ms:
        out = np.kron(out, m)
    return out

def clifford(D):
    """Hermitian Euclidean gammas {g_a, g_b} = 2 delta_ab, dimension 2^{floor(D/2)}"""
    k = D // 2
    gs = []
    for j in range(k):
        gs.append(kron(*([s3] * j + [s1] + [s0] * (k - j - 1))))
        gs.append(kron(*([s3] * j + [s2] + [s0] * (k - j - 1))))
    if D % 2 == 1:
        gs.append(kron(*([s3] * k)))
    return gs[:D]

def fact(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

def antisym5(gs, idxs):
    n = len(idxs)
    out = np.zeros_like(gs[0])
    for perm in itertools.permutations(range(n)):
        sign = round(np.linalg.det(np.eye(n)[list(perm)]))
        m = np.eye(gs[0].shape[0], dtype=complex)
        for p in perm:
            m = m @ gs[idxs[p]]
        out += sign * m
    return out / fact(n)

print("f6_evanescent_tree")
# (a)
for D in (4, 5, 6):
    gs = clifford(D)
    for a in range(D):
        for b in range(D):
            ac = gs[a] @ gs[b] + gs[b] @ gs[a]
            assert np.allclose(ac, 2 * (a == b) * np.eye(gs[0].shape[0]))
    mx = 0.0
    for combo in itertools.combinations(range(D), 5) if D >= 5 else []:
        mx = max(mx, np.abs(antisym5(gs, list(combo))).max())
    # in D = 4 every 5-tuple has a repeated index -> antisymmetrisation vanishes
    if D == 4:
        mx4 = 0.0
        for combo in itertools.product(range(4), repeat=5):
            mx4 = max(mx4, np.abs(antisym5(gs, list(combo))).max())
        print(f"(a) D=4: max |gamma^[a1..a5]| over all index tuples = {mx4:.1e}")
        assert mx4 < 1e-12
    else:
        print(f"(a) D={D}: max |gamma^[a1..a5]| over distinct tuples = {mx:.3f}")
        assert mx > 0.5

# (b), (c) in D = 6
D = 6
gs = clifford(D)
dim = gs[0].shape[0]
def sl(v):
    return sum(v[a] * gs[a] for a in range(D))

def rank5_component(X):
    """projection of X onto span{gamma^[a1..a5]}: sum over 5-subsets of
    tr(X G^dagger)/tr(G G^dagger) G, with G the antisymmetrised product"""
    out = np.zeros_like(X)
    for combo in itertools.combinations(range(D), 5):
        G = antisym5(gs, list(combo))
        nrm = np.trace(G @ G.conj().T)
        out += np.trace(X @ G.conj().T) / nrm * G
    return out

def ten5(vs):
    """gamma^[v1 v2 v3 v4 v5] for vectors/unit vectors vs (contracted)"""
    out = np.zeros((dim, dim), complex)
    for combo in itertools.product(range(D), repeat=5):
        c = np.prod([vs[i][combo[i]] for i in range(5)])
        if abs(c) < 1e-15:
            continue
        out += c * antisym5(gs, list(combo))
    return out

def unit(a):
    e = np.zeros(D); e[a] = 1.0; return e

maxdev = 0.0; maxsym = 0.0; minnorm = 1e9
for trial in range(3):
    q = rng.normal(size=D); l = rng.normal(size=D); k = rng.normal(size=D)
    mu, nu, al = 0, 1, 2
    gmu, gnu, gal = gs[mu], gs[nu], gs[al]
    X = (gnu @ sl(k + l) @ gal @ sl(q) @ gmu + gnu @ sl(q) @ gal @ sl(k) @ gmu
         + gmu @ sl(k + l) @ gal @ sl(-q) @ gnu + gmu @ sl(-q) @ gal @ sl(k) @ gnu)
    R5 = rank5_component(X)
    target = 2 * ten5([unit(nu), l, unit(al), q, unit(mu)])
    maxdev = max(maxdev, np.abs(R5 - target).max())
    minnorm = min(minnorm, np.abs(target).max())
    # symmetric part in (mu nu): swap mu <-> nu and add
    Xs = (gmu @ sl(k + l) @ gal @ sl(q) @ gnu + gmu @ sl(q) @ gal @ sl(k) @ gnu
          + gnu @ sl(k + l) @ gal @ sl(-q) @ gmu + gnu @ sl(-q) @ gal @ sl(k) @ gmu)
    maxsym = max(maxsym, np.abs(rank5_component(X + Xs)).max())
print(f"(b) D=6: max |rank5(X) - 2 gamma^[nu l alpha q mu]| = {maxdev:.1e}; "
      f"min |2 gamma^[nu l alpha q mu]| = {minnorm:.3f}")
print(f"(b) D=6: max |rank5 of the (mu nu)-symmetrised X| = {maxsym:.1e}")
assert maxdev < 1e-10 and minnorm > 1e-3 and maxsym < 1e-10

# (c) 4-dimensional kinematics inside the D=6 algebra
q = np.r_[rng.normal(size=4), 0, 0]; l = np.r_[rng.normal(size=4), 0, 0]
k = np.r_[rng.normal(size=4), 0, 0]
X = (gs[1] @ sl(k + l) @ gs[2] @ sl(q) @ gs[0] + gs[1] @ sl(q) @ gs[2] @ sl(k) @ gs[0]
     + gs[0] @ sl(k + l) @ gs[2] @ sl(-q) @ gs[1] + gs[0] @ sl(-q) @ gs[2] @ sl(k) @ gs[1])
r5 = np.abs(rank5_component(X)).max()
print(f"(c) D=6 matrices, 4-dim vectors and indices: max |rank5(X)| = {r5:.1e}")
assert r5 < 1e-10
print("RESULT: tree-level evanescent dimension-5 structure present in D dims (antisymmetric (mu nu) channel only).")
