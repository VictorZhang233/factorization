r"""
s6_ward_ff.py  (writer W05; Ch5 ex:sudakov-ward (internal example), thm:sudakov-factorization step (3); VF-WL-1, VF-WL-6)

Timelike form factor gamma*(q) -> q(p1) qbar(p2), p1 along n_A (+z), p2 along n_B (-z).  A-collinear gluons
(momenta k_j flowing from the jet J_1 INTO the hard part H) attach to the outgoing-antiquark line inside H:
   H^{mu}_a        = Gamma S(-p2+k) (i g gamma^mu t^a) v(p2)                      (Gamma = gamma^rho, open index)
   H^{mu nu}_{ab}  = Gamma S(-p2+k1+k2)(i g gamma^nu t^b) S(-p2+k1)(i g gamma^mu t^a) v(p2) + (1<->2, a<->b, mu<->nu)
Checks
 (1) elementary identities (W1), (W2) for the outgoing antiquark: S(-p+k) i g kslash v(p) = -g v(p)  (exact);
 (2) one gluon: k_mu H^mu_a = -g t^a H_0  (exact, any k);  with the K projector K_{mu nu} = k_mu n_B nu/(n_B.k - i0)
     this is H_0 x [ -g t^a n_B^nu/(n_B.k - i0) ] = first-order term of W[0, inf n_B] (rule: vertex -i g t n, propagator
     -i/(n.K - i0), K flowing into the line);
 (3) two gluons, exact: k1 k2 H = g^2 t^a t^b H_0 + i g^2 [t^a,t^b] Gamma S(-p2+K) k2slash v(p2), K = k1+k2;
 (4) exactly collinear k_j = k_j^+ n_A: k1 k2 H = (n_B.k1)(n_B.k2) W^(2)_{ab}[0,inf n_B] H_0  (path-ordered);
     abelian (t -> 1): (n_B.k1)(n_B.k2) g^2/(k1^+ k2^+) H_0 (eikonal identity);
 (5) m abelian gluons: sum over orderings of prod k_j.H = (-g)^m H_0 for arbitrary k_j (Ward + telescoping), m <= 4.
Conventions: metric (+,-,-,-), v^pm = (v^0 pm v^3)/sqrt2, n_A.v = v^-, n_B.v = v^+; S(p) = i pslash/(p^2+i0) (massless);
quark-gluon vertex i g gamma^mu t^a (D = d - i g A).
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
PASS = []
def check(name, ok, info=''):
    PASS.append(bool(ok)); print(('[PASS] ' if ok else '[FAIL] ') + name + ((' : ' + str(info)) if info != '' else ''))

# Dirac representation
I2 = np.eye(2); Z2 = np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]], dtype=complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], dtype=complex)
g0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
gs = [np.block([[Z2, s], [-s, Z2]]) for s in (sx, sy, sz)]
gam = [g0] + gs
metric = np.diag([1, -1, -1, -1])
def sl(p): return sum(metric[m, m] * gam[m] * p[m] for m in range(4))
def dot(a, b): return a[0] * b[0] - a[1] * b[1] - a[2] * b[2] - a[3] * b[3]
def S(p): return 1j * sl(p) / dot(p, p)
def lc(v):  # (v^+, v^-)
    return (v[0] + v[3]) / np.sqrt(2), (v[0] - v[3]) / np.sqrt(2)
# massless antiquark spinors v(p): solve pslash v = 0 (2-dim kernel)
def vspinors(p):
    w, U = np.linalg.eig(sl(p))
    ker = [U[:, i] for i in range(4) if abs(w[i]) < 1e-9]
    if len(ker) < 2:
        # use null space via SVD
        u, s_, vh = np.linalg.svd(sl(p)); ker = [vh[-1].conj(), vh[-2].conj()]
    return ker
# SU(3)
lam8 = np.zeros((8, 3, 3), dtype=complex)
lam8[0][0, 1] = lam8[0][1, 0] = 1; lam8[1][0, 1] = -1j; lam8[1][1, 0] = 1j; lam8[2][0, 0] = 1; lam8[2][1, 1] = -1
lam8[3][0, 2] = lam8[3][2, 0] = 1; lam8[4][0, 2] = -1j; lam8[4][2, 0] = 1j; lam8[5][1, 2] = lam8[5][2, 1] = 1
lam8[6][1, 2] = -1j; lam8[6][2, 1] = 1j; lam8[7] = np.diag([1, 1, -2]) / np.sqrt(3)
T = lam8 / 2
rng = np.random.default_rng(11)
g = 0.9
nA = np.array([1, 0, 0, 1]) / np.sqrt(2)     # n_A^+ = 1, n_A^- = 0
nB = np.array([1, 0, 0, -1]) / np.sqrt(2)    # n_B^+ = 0, n_B^- = 1
check('(0) n_A.v = v^-, n_B.v = v^+, n_A.n_B = 1', abs(dot(nA, np.array([2., .3, .1, .7])) - lc(np.array([2., .3, .1, .7]))[1]) < 1e-12
      and abs(dot(nB, np.array([2., .3, .1, .7])) - lc(np.array([2., .3, .1, .7]))[0]) < 1e-12 and abs(dot(nA, nB) - 1) < 1e-12)
Q = 10.0
p2 = (Q / np.sqrt(2)) * nB * np.sqrt(2) / 1.0 * 0.5   # p2 = (Q/2)(1,0,0,-1): p2^- = Q/sqrt2
p2 = np.array([Q / 2, 0, 0, -Q / 2])
vs = vspinors(p2)
for v in vs:
    check('(1) massless antiquark spinor: p2slash v(p2) = 0', np.abs(sl(p2) @ v).max() < 1e-10)
# (1) (W2) outgoing antiquark: S(-p+k) i g kslash v(p) = -g v(p)
for _ in range(3):
    k = rng.normal(size=4) * 3
    for v in vs:
        lhs = S(-p2 + k) @ (1j * g * sl(k)) @ v
        check('(1) (W2): S(-p2+k) i g kslash v(p2) = -g v(p2), random k', np.abs(lhs + g * v).max() < 1e-10)
# (W1): S(p+k)(i g kslash)S(p) = g [S(p+k) - S(p)]
p = rng.normal(size=4); k = rng.normal(size=4)
check('(1) (W1): S(p+k) i g kslash S(p) = g[S(p+k) - S(p)]', np.abs(S(p + k) @ (1j * g * sl(k)) @ S(p) - g * (S(p + k) - S(p))).max() < 1e-10)

# (2) one gluon, exact for any k
Gam = gam[0] @ gam[2]   # an arbitrary open Dirac structure standing for the rest of H (gamma^rho ...)
for _ in range(2):
    k = rng.normal(size=4) * 2
    a = rng.integers(8)
    for v in vs:
        H = [np.kron(Gam @ S(-p2 + k) @ (1j * g * gam[m]) @ v, T[a].ravel()) for m in range(4)]   # H^mu (colour as vector)
        kH = sum(metric[m, m] * k[m] * H[m] for m in range(4))
        H0 = np.kron(Gam @ v, T[a].ravel())
        check('(2) one gluon: k_mu H^mu_a = -g t^a H_0 (exact)', np.abs(kH + g * H0).max() < 1e-10)
# K projector and the Wilson-line rule:  H.K.C = (k.H) n_B.C/(n_B.k - i0) = -g t^a H_0 n_B.C/(n_B.k - i0)
#   W[0, inf n] first order with K flowing in: (-i g t n^nu)(-i)/(n.K - i0) = -g t n^nu/(n.K - i0)  -> equal
check('(2) W^(1)[0,inf n_B] (vertex -i g t n, propagator -i/(n.k - i0)) = -g t n^nu/(n.k - i0) = H.K.C / H_0',
      abs((-1j * g) * (-1j) - (-g)) < 1e-15)

# (3) two gluons, exact
def H2(k1, k2, a, b, v):
    out = np.zeros((4, 4, 4, 9), dtype=complex)
    for mu in range(4):
        for nu in range(4):
            t1 = np.kron(Gam @ S(-p2 + k1 + k2) @ (1j * g * gam[nu]) @ S(-p2 + k1) @ (1j * g * gam[mu]) @ v, (T[b] @ T[a]).ravel())
            t2 = np.kron(Gam @ S(-p2 + k1 + k2) @ (1j * g * gam[mu]) @ S(-p2 + k2) @ (1j * g * gam[nu]) @ v, (T[a] @ T[b]).ravel())
            out[mu, nu] = (t1 + t2).reshape(4, 9)
    return out
def contract2(Hm, k1, k2):
    return sum(metric[m, m] * metric[n, n] * k1[m] * k2[n] * Hm[m, n] for m in range(4) for n in range(4))
for _ in range(2):
    k1 = rng.normal(size=4) * 2; k2 = rng.normal(size=4) * 2; a, b = rng.integers(8), rng.integers(8)
    v = vs[0]
    lhs = contract2(H2(k1, k2, a, b, v), k1, k2).ravel()
    comm = T[a] @ T[b] - T[b] @ T[a]
    rhs = (np.kron(g ** 2 * Gam @ v, (T[a] @ T[b]).ravel())
           + np.kron(1j * g ** 2 * Gam @ S(-p2 + k1 + k2) @ sl(k2) @ v, comm.ravel()))
    check('(3) two gluons (exact): k1k2H = g^2 t^a t^b H_0 + i g^2 [t^a,t^b] Gamma S(-p2+K) k2slash v', np.abs(lhs - rhs).max() < 1e-9)
# (4) exactly collinear k_j = kplus_j n_A
for (x1, x2) in [(1.3, 0.4), (0.25, 2.2)]:
    k1 = x1 * nA * np.sqrt(2) * 1.0; k2 = x2 * nA * np.sqrt(2)     # k^+ = x sqrt2 ... compute directly
    k1p, k2p = lc(k1)[0], lc(k2)[0]; Kp = k1p + k2p
    a, b = 2, 5
    lhs = contract2(H2(k1, k2, a, b, vs[1]), k1, k2).ravel()
    W2 = g ** 2 * (T[b] @ T[a] / (k1p * Kp) + T[a] @ T[b] / (k2p * Kp))   # W^(2)[0,inf n_B]: gluon nearest inf first
    rhs = np.kron(Gam @ vs[1], ((k1p * k2p) * W2).ravel())
    check('(4) collinear: k1k2H = (n_B.k1)(n_B.k2) W^(2)_ab[0,inf n_B] H_0 (path-ordered colour)', np.abs(lhs - rhs).max() < 1e-9)
    # W^(2)[0,inf n] from the rule: (-i g)^2 t^{a2}t^{a1} (-i)^2/((n.k1)(n.(k1+k2))) with gluon 1 nearest +inf
    rule = (-1j * g) ** 2 * (-1j) ** 2 / (k1p * Kp)
    check('(4) rule: (-ig)^2 (-i)^2/(n.k1 n.K) = g^2/(k1^+ K^+)', abs(rule - g ** 2 / (k1p * Kp)) < 1e-12)
    # abelian: t -> 1
    check('(4) abelian: g^2[1/(K^+ k2^+) + 1/(K^+ k1^+)] = g^2/(k1^+ k2^+)  (eikonal identity, m=2)',
          abs(g ** 2 * (1 / (Kp * k2p) + 1 / (Kp * k1p)) - g ** 2 / (k1p * k2p)) < 1e-12)
# (5) abelian m gluons: sum over all orderings of the attachments, contracted with k_j: (-g)^m H_0
def Hm_contracted(ks, v):
    m = len(ks); tot = np.zeros(4, dtype=complex)
    for perm in itertools.permutations(range(m)):
        vec = v.copy(); P = -p2.copy()
        for j in perm:                      # attach in order: first attachment nearest v(p2)
            P = P + ks[j]
            vec = S(P) @ (1j * g * sl(ks[j])) @ vec
        tot += Gam @ vec
    return tot
for m in [1, 2, 3, 4]:
    ks = [rng.normal(size=4) * 2 for _ in range(m)]
    lhs = Hm_contracted(ks, vs[0])
    check('(5) abelian, m=%d: sum over orderings of prod_j k_j.H = (-g)^m H_0 (exact, arbitrary k_j)' % m, np.abs(lhs - (-g) ** m * (Gam @ vs[0])).max() < 1e-8)

print('\n=== s6_ward_ff: %d/%d PASS ===' % (sum(PASS), len(PASS)))
