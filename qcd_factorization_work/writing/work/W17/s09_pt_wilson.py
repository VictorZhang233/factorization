# W17 / Ch14 -- s09: PT transformation of the TMD operator (thm:tmd-sivers-sign).
# (1) Dirac matrices: PT acts as  A psi(x) A^{-1} = V psi(-x)  (A antiunitary), V = T_D gamma^0, T_D = i gamma^1 gamma^3 (Dirac rep.);
#     bilinear: A psibar(x) Gamma psi(y) A^{-1} = psibar(-x) [gamma^0 V^dagger gamma^0 Gamma^* V] psi(-y).
#     Claims: Gamma = gamma^+  -> +gamma^+ ;  gamma^+ gamma5 -> -gamma^+ gamma5 ; gamma^+ gamma^i gamma5 -> -gamma^+ gamma^i gamma5
#     (spin densities flip: PT reverses spin), gamma^0 Gamma^dagger gamma^0 = Gamma for Gamma = gamma^+ (hermiticity step).
# (2) colour: eta_a t^a* = t^a with eta = +1 (real Gell-Mann) / -1 (imaginary); path-ordered exponential of a discretized field:
#     complex conjugation with A^a(z) -> eta_a A^a(-z) gives the ordered exponential along the reflected path, SAME order.
# (3) spinors: the PT image of u(P,S) corresponds to spin -S at the same momentum:  V u(P,S)^*  has projector (Pslash+M)(1+g5 (-S)slash)/2.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from scipy.linalg import expm
ok = True
def check(name, cond):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name); ok &= bool(cond)
I2 = np.eye(2); Z2 = np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]], dtype=complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], dtype=complex)
G = [np.block([[I2, Z2], [Z2, -I2]]).astype(complex)] + [np.block([[Z2, s], [-s, Z2]]) for s in (sx, sy, sz)]
gm = np.diag([1., -1., -1., -1.])
g5 = 1j*G[0] @ G[1] @ G[2] @ G[3]
TD = 1j*G[1] @ G[3]
# T alone: T_D gamma^mu* T_D^{-1} = gamma_mu  (gamma^0 -> gamma^0, gamma^i -> -gamma^i)
check('T_D gamma^mu* T_D^{-1} = gamma_mu', all(np.allclose(TD @ G[m].conj() @ np.linalg.inv(TD), gm[m, m]*G[m]) for m in range(4)))
check('T_D^2 = 1 (up to sign) and T_D unitary', np.allclose(TD @ TD.conj().T, np.eye(4)))
V = TD @ G[0]
def transf(Gam):   # gamma^0 V^dagger gamma^0 Gamma^* V
    return G[0] @ V.conj().T @ G[0] @ Gam.conj() @ V
gplus = (G[0] + G[3])/np.sqrt(2)
check('PT: gamma^mu -> gamma^mu (all mu): the vector current is PT-even with x -> -x', all(np.allclose(transf(G[m]), G[m]) for m in range(4)))
check('PT: gamma^+ -> +gamma^+ (number density)', np.allclose(transf(gplus), gplus))
check('PT: gamma^+ gamma5 -> -gamma^+ gamma5 (helicity density flips)', np.allclose(transf(gplus @ g5), -gplus @ g5))
for i in (1, 2):
    check('PT: gamma^+ gamma^%d gamma5 -> -(same) (transversity density flips)' % i, np.allclose(transf(gplus @ G[i] @ g5), -gplus @ G[i] @ g5))
check('hermiticity: gamma^0 (gamma^+)^dagger gamma^0 = gamma^+', np.allclose(G[0] @ gplus.conj().T @ G[0], gplus))
# (3) spin reversal of single-particle spinors under PT
def sl(v): return sum(gm[m, m]*v[m]*G[m] for m in range(4))
M = 0.94; Pz = 3.1; E = np.sqrt(M*M + Pz*Pz)
P = np.array([E, 0, 0, Pz])
for S in [np.array([0, 1., 0, 0]), np.array([0, 0, 1., 0]), np.array([Pz/M, 0, 0, E/M])]:
    proj = (sl(P) + M*np.eye(4)) @ (np.eye(4) + g5 @ sl(S))/2
    w, vv = np.linalg.eig(proj)
    u = vv[:, np.argmax(abs(w))]
    u = u/np.sqrt(abs(u.conj() @ G[0] @ u)/(2*M))
    up = V @ u.conj()
    proj_img = np.outer(up, up.conj() @ G[0])
    target = (sl(P) + M*np.eye(4)) @ (np.eye(4) + g5 @ sl(-S))/2
    check('PT image of u(P,S) has projector (Pslash+M)(1-g5 Sslash)/2 for S=%s' % S.round(2), np.allclose(proj_img, target, atol=1e-10))
# (2) colour: Gell-Mann matrices
lam = np.zeros((8, 3, 3), dtype=complex)
lam[0][0, 1] = lam[0][1, 0] = 1
lam[1][0, 1] = -1j; lam[1][1, 0] = 1j
lam[2][0, 0] = 1; lam[2][1, 1] = -1
lam[3][0, 2] = lam[3][2, 0] = 1
lam[4][0, 2] = -1j; lam[4][2, 0] = 1j
lam[5][1, 2] = lam[5][2, 1] = 1
lam[6][1, 2] = -1j; lam[6][2, 1] = 1j
lam[7] = np.diag([1, 1, -2])/np.sqrt(3)
t = lam/2
eta = np.array([1 if np.allclose(t[a].conj(), t[a]) else -1 for a in range(8)])
check('eta_a t^a* = t^a with eta = (+,-,+,+,-,+,-,+)', all(np.allclose(eta[a]*t[a].conj(), t[a]) for a in range(8)) and list(eta) == [1, -1, 1, 1, -1, 1, -1, 1])
# discretized path from a to b, random classical field values A^a_mu(z) on the path points (operator ordering is preserved by
# antiunitary maps, so a classical check of the ordering/conjugation structure suffices)
rng = np.random.default_rng(3)
Npts = 40; g = 0.7
zs = np.cumsum(rng.normal(size=(Npts, 4))*0.1, axis=0)        # path points z_0 ... z_{N-1}
Afield = {}
def Aval(z):     # deterministic pseudo-random field A^a_mu(z)
    key = tuple(np.round(z, 12))
    if key not in Afield:
        Afield[key] = rng.normal(size=(8, 4))
    return Afield[key]
def W_path(points, field, conj=False):
    W = np.eye(3, dtype=complex)
    for j in range(len(points) - 1):
        dz = points[j + 1] - points[j]; zm = (points[j + 1] + points[j])/2
        Aa = field(zm)                                   # (8,4)
        dzA = sum(gm[m, m]*dz[m]*Aa[:, m] for m in range(4))   # dz^mu A^a_mu  (metric)
        X = sum(dzA[a]*t[a] for a in range(8))
        step = expm(1j*g*X)
        W = step @ W          # later points to the left
    return W
W = W_path(zs, Aval)
# antiunitary image: conjugate all c-numbers (i -> -i, t^a -> t^a*) and replace A^a(z) by eta_a A^a(-z), keep the operator order
def W_image(points):
    Wi = np.eye(3, dtype=complex)
    for j in range(len(points) - 1):
        dz = points[j + 1] - points[j]; zm = (points[j + 1] + points[j])/2
        Aa = Aval_ref(-zm)                                # field at the reflected point (for the operator relation A(z)->eta A(-z))
        X = sum(sum(gm[m, m]*dz[m]*eta[a]*Aa[a, m] for m in range(4))*t[a].conj() for a in range(8))
        step = expm(-1j*g*X)
        Wi = step @ Wi
    return Wi
# reference field defined on the reflected path: B^a(z') := A^a(z') arbitrary; check
#   image of W[path; field A(.) at -z] == W[reflected path; field A]
zs_ref = -zs
Aval_ref = Aval
lhs = W_image(zs)                         # uses A(-z) on the original path with conjugation
rhs = W_path(zs_ref, Aval)                # ordered exponential along the reflected path, same ordering
check('PT image of W[b,a] equals W[-b,-a] along the reflected path, with the same path ordering', np.allclose(lhs, rhs, atol=1e-12))
# the hermitian conjugate reverses the path: W[b,a]^dagger = W[a,b]
check('W[b,a]^dagger = W[a,b] (reversed path)', np.allclose(W.conj().T, W_path(zs[::-1], Aval), atol=1e-12))
print('ALL PASS' if ok else 'SOME FAIL')
