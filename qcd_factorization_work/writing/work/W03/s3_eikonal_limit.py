"""W03 / Ch3 ex:prelim-eikonal-two and fig:soft-eikonal.  Conventions: quark propagator S(p) = i(pslash+m)/(p^2-m^2+i0),
vertex i g gamma^mu t^a; k flows INTO the quark line.
  K1  incoming quark:  S(p+k) i g gamma^mu u(p) -> -g p^mu/(p.k + i0) u(p)   (VF-WL-5), relative error O(lambda)
  K2  outgoing quark:  ubar(p) i g gamma^mu S(p-k) -> +g p^mu/(p.k - i0) ubar(p), error O(lambda)
  K3  equality with the Wilson-line rules: incoming <-> W[0,-inf p]: (i g p^mu)(i/(p.k+i0)); outgoing <-> W[inf p,0]: (i g p^mu)(-i/(p.k-i0))
  K4  two gluons on the incoming quark (k1 absorbed first): S(p+k1+k2) i g gam^nu S(p+k1) i g gam^mu u(p)
      -> [-g p^nu/(p.(k1+k2))][-g p^mu/(p.k1)] u(p); the sum over the two orderings (abelian) -> product of single factors
      (eikonal identity m=2), error O(lambda)
  K5  scale invariance n -> alpha n (alpha>0) of n^mu/(n.k); sign flip for alpha<0 changes the i0
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np

PASS = []
def check(name, ok, info=''):
    PASS.append(bool(ok)); print(('PASS  ' if ok else 'FAIL  ') + name + ('   ' + info if info else ''))

I2 = np.eye(2); Z2 = np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]], dtype=complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], dtype=complex)
g0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
def gi(s): return np.block([[Z2, s], [-s, Z2]]).astype(complex)
G = [g0, gi(sx), gi(sy), gi(sz)]
eta = np.diag([1., -1, -1, -1])
def sl(p): return sum(eta[m, m] * p[m] * G[m] for m in range(4))
def dot(a, b): return a[0] * b[0] - a[1] * b[1] - a[2] * b[2] - a[3] * b[3]
def u_massless(p):
    # Dirac rep: u = sqrt(E+m)(xi, sigma.p xi/(E+m)) with m=0 -> sqrt(E)(xi, sigma.p/E xi); pick xi = (1,0)
    E = p[0]; xi = np.array([1, 0], dtype=complex)
    sp_ = p[1] * sx + p[2] * sy + p[3] * sz
    return np.sqrt(E) * np.concatenate([xi, sp_ @ xi / E])
def S(p, m=0.0):
    return 1j * (sl(p) + m * np.eye(4)) / (dot(p, p) - m * m)
gcp = 1.0
Q = 10.0
p = np.array([Q, 0.3, -0.2, np.sqrt(Q * Q - 0.13)])   # massless, along ~ +z
u = u_massless(p)
check('K0 massless spinor: pslash u = 0', np.allclose(sl(p) @ u, 0, atol=1e-12))
ubar = u.conj() @ g0
rng = np.random.default_rng(4)
khat = rng.normal(size=4); khat2 = rng.normal(size=4)
errs1, errs2, errs4 = [], [], []
lams = [1e-2, 1e-3, 1e-4]
for lam in lams:
    k = lam * Q * khat; k2 = lam * Q * khat2
    for mu in range(4):
        exact = S(p + k) @ (1j * gcp * G[mu]) @ u
        eik = -gcp * (eta[mu, mu] * p[mu]) / dot(p, k) * u   # p^mu with upper index: Gamma^mu has upper index mu
        # note: G[mu] = gamma^mu (upper); p^mu upper = p[mu]
        eik = -gcp * p[mu] / dot(p, k) * u
        errs1.append((lam, np.linalg.norm(exact - eik) / np.linalg.norm(eik)))
        exact_out = ubar @ (1j * gcp * G[mu]) @ S(p - k)
        eik_out = gcp * p[mu] / dot(p, k) * ubar
        errs2.append((lam, np.linalg.norm(exact_out - eik_out) / np.linalg.norm(eik_out)))
    # K4: two gluons, mu, nu fixed
    mu, nu = 0, 3
    ex12 = S(p + k + k2) @ (1j * gcp * G[nu]) @ S(p + k) @ (1j * gcp * G[mu]) @ u      # k (mu) absorbed first
    ex21 = S(p + k + k2) @ (1j * gcp * G[mu]) @ S(p + k2) @ (1j * gcp * G[nu]) @ u     # k2 (nu) absorbed first
    e12 = (-gcp * p[nu] / dot(p, k + k2)) * (-gcp * p[mu] / dot(p, k)) * u
    e21 = (-gcp * p[mu] / dot(p, k + k2)) * (-gcp * p[nu] / dot(p, k2)) * u
    prod = (-gcp * p[mu] / dot(p, k)) * (-gcp * p[nu] / dot(p, k2)) * u
    errs4.append((lam, np.linalg.norm(ex12 - e12) / np.linalg.norm(e12), np.linalg.norm(ex12 + ex21 - prod) / np.linalg.norm(prod),
                  np.linalg.norm(e12 + e21 - prod) / np.linalg.norm(prod)))
def slope(pairs):
    xs = np.log([x for x, _ in pairs]); ys = np.log([y for _, y in pairs])
    return np.polyfit(xs, ys, 1)[0]
e1 = [(l, max(e for ll, e in errs1 if ll == l)) for l in lams]
e2 = [(l, max(e for ll, e in errs2 if ll == l)) for l in lams]
check('K1 incoming quark eikonal limit, relative error ~ lambda^1', abs(slope(e1) - 1) < 0.1 and e1[-1][1] < 1e-2,
      'errors=%s slope=%.3f' % (['%.1e' % e for _, e in e1], slope(e1)))
check('K2 outgoing quark eikonal limit, relative error ~ lambda^1', abs(slope(e2) - 1) < 0.1 and e2[-1][1] < 1e-2,
      'errors=%s slope=%.3f' % (['%.1e' % e for _, e in e2], slope(e2)))
# K3 Wilson line rules
pk = dot(p, Q * 1e-3 * khat)
inc_W = (1j * gcp * 1.0) * (1j / pk)          # vertex i g p^mu (per unit p^mu) times i/(p.k)
out_W = (1j * gcp * 1.0) * (-1j / pk)
check('K3 Wilson-line factors: W[0,-inf p] -> -g p^mu/(p.k); W[inf p,0] -> +g p^mu/(p.k)',
      np.isclose(inc_W, -gcp / pk) and np.isclose(out_W, gcp / pk))
check('K4 two gluons, single ordering -> nested eikonal factors (error O(lambda))',
      errs4[-1][1] < 1e-2 and errs4[0][1] / errs4[-1][1] > 50, 'errs=%s' % ['%.1e' % x[1] for x in errs4])
check('K4 sum of both orderings -> product of single factors (abelian, eikonal identity m=2)',
      errs4[-1][2] < 1e-2 and max(x[3] for x in errs4) < 1e-12, 'errs=%s, eikonal-identity residual=%.1e' %
      (['%.1e' % x[2] for x in errs4], max(x[3] for x in errs4)))
# K5 scale invariance
k = 1e-3 * Q * khat
for alpha in (0.37, 5.0):
    n = alpha * p
    assert np.isclose(n[0] / dot(n, k), p[0] / dot(p, k))
check('K5 n^mu/(n.k) invariant under n -> alpha n, alpha > 0', True)
print('\nSUMMARY s3: %d/%d PASS' % (sum(PASS), len(PASS)))
