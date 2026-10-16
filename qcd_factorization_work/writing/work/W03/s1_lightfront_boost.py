"""W03 / Ch3 sec:prelim-lightfront, App A sec:appA-lightfront, sec:appA-dirac.
Checks (binding conventions: metric (+,-,-,-), v^pm=(v^0 pm v^3)/sqrt2, gamma_5 = i g0 g1 g2 g3):
  L1  v.w = v^+ w^- + v^- w^+ - vT.wT ; n_A.v = v^-, n_B.v = v^+ ; g^{+-}=1, v_+ = v^-
  L2  Jacobian d^4k = dk^+ dk^- d^2k_T (|det|=1); k^2 = 2k^+k^- - kT^2 ; on-shell k^pm = mT e^{pm y}/sqrt2
  L3  Sudakov decomposition k = alpha p_A + beta p_B + k_T with p_A = p_A^+ n_A, p_B = p_B^- n_B
  L4  SCET dictionary: n = sqrt2 n_A, nbar = sqrt2 n_B, nbar.p = sqrt2 p^+, n.p = sqrt2 p^-, p = nbar.p n/2 + n.p nbar/2 + p_perp
  B1  boost along z with rapidity eta: v^pm -> e^{pm eta} v^pm, vT fixed
  B2  S = exp(eta/2 g0 g3) satisfies S^-1 g^mu S = Lambda^mu_nu g^nu ; S = e^{eta/2} P_+ + e^{-eta/2} P_-
  B3  P_+ = 1/2 g^- g^+, P_- = 1/2 g^+ g^- : projectors, hermitian, P_+ + P_- = 1, P_+ = (1+g0g3)/2
  B4  (g^pm)^2 = 0, {g^+,g^-}=2, (g^+)^dagger = g^-, g^0 g^pm g^0 = g^mp, g^+ P_+ = g^+, g^+ P_- = 0, P_- g^+ = g^+
  B5  g^0 g^+ = sqrt2 P_+  =>  psibar g^+ psi = sqrt2 |P_+ psi|^2 >= 0
  B6  collinear momentum Q(1,lam^2,lam) = boost of a rest-frame momentum ~ lam Q (1,1,1) with e^eta = 1/lam
  F1  collinear Fierz: P_+ M P_- = 1/4[Tr(g^+ M) g^- + Tr(g^+ g5 M) g5 g^- + sum_j Tr(g^+ g^j M) g^- g^j]
      for random complex M; the four structures satisfy P_+ X P_- = X; Tr(Gamma_i M) = Tr(Gamma_i P_+ M P_-)
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp

PASS = []
def check(name, ok, info=''):
    PASS.append(bool(ok))
    print(('PASS  ' if ok else 'FAIL  ') + name + ('   ' + info if info else ''))

# ---------------- Dirac matrices (Dirac representation) ----------------
I2 = np.eye(2); Z2 = np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
g0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
def gi(s): return np.block([[Z2, s], [-s, Z2]]).astype(complex)
g = [g0, gi(sx), gi(sy), gi(sz)]
g5 = 1j * g[0] @ g[1] @ g[2] @ g[3]
one = np.eye(4, dtype=complex)
metric = np.diag([1., -1., -1., -1.])
gp = (g[0] + g[3]) / np.sqrt(2)   # gamma^+
gm = (g[0] - g[3]) / np.sqrt(2)   # gamma^-
Pp = 0.5 * gm @ gp
Pm = 0.5 * gp @ gm
def close(a, b, tol=1e-12): return np.allclose(a, b, atol=tol)

# ---------------- L1-L4 symbolic light-cone algebra ----------------
v0, v1, v2, v3, w0, w1, w2, w3 = sp.symbols('v0 v1 v2 v3 w0 w1 w2 w3', real=True)
vp, vm = (v0 + v3) / sp.sqrt(2), (v0 - v3) / sp.sqrt(2)
wp, wm = (w0 + w3) / sp.sqrt(2), (w0 - w3) / sp.sqrt(2)
dot = v0 * w0 - v1 * w1 - v2 * w2 - v3 * w3
check('L1 v.w = v+w- + v-w+ - vT.wT', sp.simplify(dot - (vp * wm + vm * wp - v1 * w1 - v2 * w2)) == 0)
# n_A = (1^+,0^-,0_T): n_A^0 = n_A^3 = 1/sqrt2 ; n_B = (0^+,1^-): n_B^0 = 1/sqrt2, n_B^3 = -1/sqrt2
nA = (1 / sp.sqrt(2), 0, 0, 1 / sp.sqrt(2)); nB = (1 / sp.sqrt(2), 0, 0, -1 / sp.sqrt(2))
def mdot(a, b): return a[0] * b[0] - a[1] * b[1] - a[2] * b[2] - a[3] * b[3]
vv = (v0, v1, v2, v3)
check('L1 n_A.v = v^-, n_B.v = v^+, n_A^2 = n_B^2 = 0, n_A.n_B = 1',
      sp.simplify(mdot(nA, vv) - vm) == 0 and sp.simplify(mdot(nB, vv) - vp) == 0
      and sp.simplify(mdot(nA, nA)) == 0 and sp.simplify(mdot(nB, nB)) == 0 and sp.simplify(mdot(nA, nB) - 1) == 0)
J = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
check('L2 Jacobian |d(k+,k-)/d(k0,k3)| = 1', sp.Abs(J.det()) == 1)
check('L2 k^2 = 2k+k- - kT^2', sp.simplify(mdot(vv, vv) - (2 * vp * vm - v1**2 - v2**2)) == 0)
mT, y = sp.symbols('m_T y', positive=True)
kp = mT * sp.exp(y) / sp.sqrt(2); km = mT * sp.exp(-y) / sp.sqrt(2)
check('L2 on-shell k^pm = mT e^{pm y}/sqrt2: 2k+k- = mT^2, (1/2)ln(k+/k-) = y',
      sp.simplify(2 * kp * km - mT**2) == 0 and sp.simplify(sp.log(kp / km) / 2 - y) == 0)
# Sudakov decomposition
al, be, pAp, pBm, kx, ky = sp.symbols('alpha beta p_A^+ p_B^- k_x k_y', real=True)
pA = tuple(pAp * c for c in nA); pB = tuple(pBm * c for c in nB)
k = tuple(al * pA[i] + be * pB[i] + (0, kx, ky, 0)[i] for i in range(4))
kplus = (k[0] + k[3]) / sp.sqrt(2); kminus = (k[0] - k[3]) / sp.sqrt(2)
check('L3 Sudakov: alpha = k^+/p_A^+, beta = k^-/p_B^-, k^2 = 2 alpha beta pA.pB - kT^2',
      sp.simplify(kplus - al * pAp) == 0 and sp.simplify(kminus - be * pBm) == 0
      and sp.simplify(mdot(k, k) - (2 * al * be * mdot(pA, pB) - kx**2 - ky**2)) == 0
      and sp.simplify(mdot(pA, pB) - pAp * pBm) == 0)
n_scet = (1, 0, 0, 1); nb_scet = (1, 0, 0, -1)
p0, p1, p2, p3 = sp.symbols('p0 p1 p2 p3', real=True)
pp_ = (p0 + p3) / sp.sqrt(2); pm_ = (p0 - p3) / sp.sqrt(2)
pvec = (p0, p1, p2, p3)
recon = [mdot(nb_scet, pvec) * n_scet[i] / 2 + mdot(n_scet, pvec) * nb_scet[i] / 2 + (0, p1, p2, 0)[i] for i in range(4)]
check('L4 SCET: n = sqrt2 n_A, nbar = sqrt2 n_B, nbar.p = sqrt2 p+, n.p = sqrt2 p-, p reconstructed',
      all(sp.simplify(n_scet[i] - sp.sqrt(2) * nA[i]) == 0 for i in range(4))
      and all(sp.simplify(nb_scet[i] - sp.sqrt(2) * nB[i]) == 0 for i in range(4))
      and sp.simplify(mdot(nb_scet, pvec) - sp.sqrt(2) * pp_) == 0 and sp.simplify(mdot(n_scet, pvec) - sp.sqrt(2) * pm_) == 0
      and all(sp.simplify(recon[i] - pvec[i]) == 0 for i in range(4)))

# ---------------- B1-B6 boosts ----------------
eta = 0.731
ch, sh = np.cosh(eta), np.sinh(eta)
Lam = np.array([[ch, 0, 0, sh], [0, 1, 0, 0], [0, 0, 1, 0], [sh, 0, 0, ch]])
v = np.array([1.3, -0.4, 0.9, 0.25])
vpb = Lam @ v
vplus = lambda u: (u[0] + u[3]) / np.sqrt(2)
vminus = lambda u: (u[0] - u[3]) / np.sqrt(2)
check('B1 v^pm -> e^{pm eta} v^pm, vT fixed',
      np.isclose(vplus(vpb), np.exp(eta) * vplus(v)) and np.isclose(vminus(vpb), np.exp(-eta) * vminus(v))
      and np.allclose(vpb[1:3], v[1:3]))
from scipy.linalg import expm
K = 0.5 * g[0] @ g[3]
S = expm(eta * K)
Sinv = np.linalg.inv(S)
ok = all(close(Sinv @ g[mu] @ S, sum(Lam[mu, nu] * g[nu] for nu in range(4))) for mu in range(4))
check('B2 S^-1 gamma^mu S = Lambda^mu_nu gamma^nu with S = exp(eta g0 g3 /2)', ok)
check('B2 S = e^{eta/2} P_+ + e^{-eta/2} P_-', close(S, np.exp(eta / 2) * Pp + np.exp(-eta / 2) * Pm))
check('B3 P_pm projectors, orthogonal, complete, hermitian; P_+ = (1+g0g3)/2',
      close(Pp @ Pp, Pp) and close(Pm @ Pm, Pm) and close(Pp @ Pm, 0 * one) and close(Pp + Pm, one)
      and close(Pp.conj().T, Pp) and close(Pm.conj().T, Pm) and close(Pp, 0.5 * (one + g[0] @ g[3])))
check('B4 (g^pm)^2=0, {g+,g-}=2, (g+)^dag=g-, g0 g^pm g0 = g^mp',
      close(gp @ gp, 0 * one) and close(gm @ gm, 0 * one) and close(gp @ gm + gm @ gp, 2 * one)
      and close(gp.conj().T, gm) and close(g[0] @ gp @ g[0], gm) and close(g[0] @ gm @ g[0], gp))
check('B4 g+ P_+ = g+, g+ P_- = 0, P_- g+ = g+, P_+ g+ = 0 (g+ = P_- g+ P_+)',
      close(gp @ Pp, gp) and close(gp @ Pm, 0 * one) and close(Pm @ gp, gp) and close(Pp @ gp, 0 * one)
      and close(Pm @ gp @ Pp, gp))
check('B5 g0 g+ = sqrt2 P_+', close(g[0] @ gp, np.sqrt(2) * Pp))
rng = np.random.default_rng(7)
psi = rng.normal(size=4) + 1j * rng.normal(size=4)
lhs = (psi.conj() @ g[0]) @ gp @ psi
rhs = np.sqrt(2) * np.vdot(Pp @ psi, Pp @ psi)
check('B5 psibar g+ psi = sqrt2 |P_+ psi|^2 (real, >= 0)', np.isclose(lhs, rhs) and abs(lhs.imag) < 1e-12 and lhs.real >= 0)
# spinor good/bad components under the boost: P_+ S psi = e^{eta/2} P_+ psi
check('B5 P_+ (S psi) = e^{eta/2} P_+ psi, P_- (S psi) = e^{-eta/2} P_- psi',
      close(Pp @ S @ psi, np.exp(eta / 2) * Pp @ psi) and close(Pm @ S @ psi, np.exp(-eta / 2) * Pm @ psi))
# B6: collinear scaling: boost a rest-frame momentum lam*Q*(a,b,c) (light-cone comps) with e^eta = 1/lam
lam = sp.Symbol('lambda', positive=True); Q = sp.Symbol('Q', positive=True)
a_, b_, c_ = sp.symbols('a b c', positive=True)
rest = (lam * Q * a_, lam * Q * b_, lam * Q * c_)   # (k^+, k^-, kT)
boosted = (rest[0] / lam, rest[1] * lam, rest[2])
check('B6 Q(1,lam^2,lam) scaling from rest-frame lam Q (a,b,c) boosted with e^eta = 1/lam',
      sp.simplify(boosted[0] / Q - a_) == 0 and sp.simplify(boosted[1] / (Q * lam**2) - b_) == 0
      and sp.simplify(boosted[2] / (Q * lam) - c_) == 0)
# gluon field components scale like the momentum: A^+ -> e^eta A^+
A = np.array([0.2, 0.7, -0.3, 0.5])
Ab = Lam @ A
check('B6 A^+ -> e^eta A^+, A^- -> e^-eta A^-, A_T fixed (vector field)',
      np.isclose(vplus(Ab), np.exp(eta) * vplus(A)) and np.isclose(vminus(Ab), np.exp(-eta) * vminus(A)) and np.allclose(Ab[1:3], A[1:3]))

# ---------------- F1 collinear Fierz ----------------
M = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
gT = [g[1], g[2]]
rhsF = 0.25 * (np.trace(gp @ M) * gm + np.trace(gp @ g5 @ M) * g5 @ gm + sum(np.trace(gp @ gj @ M) * gm @ gj for gj in gT))
check('F1 P_+ M P_- = 1/4[Tr(g+M) g- + Tr(g+ g5 M) g5 g- + sum_j Tr(g+ g^j M) g- g^j] (random M)', close(Pp @ M @ Pm, rhsF, 1e-10))
structs = [gm, g5 @ gm, gm @ g[1], gm @ g[2]]
check('F1 the four structures satisfy P_+ X P_- = X', all(close(Pp @ X @ Pm, X) for X in structs))
Gams = [gp, gp @ g5, gp @ g[1], gp @ g[2]]
check('F1 Tr(Gamma_i M) = Tr(Gamma_i P_+ M P_-) for Gamma in {g+, g+g5, g+g^j}',
      all(np.isclose(np.trace(G @ M), np.trace(G @ Pp @ M @ Pm)) for G in Gams))
# dual basis: Tr(Gamma_i X_j)/4 = delta_ij  (note Tr(g+ g5 g5 g-) and Tr(g+ g^k g- g^j) = 4 delta^{kj})
D = np.array([[np.trace(Gams[i] @ structs[j]) / 4 for j in range(4)] for i in range(4)])
# Gamma for the g5 g- structure is g+ g5 (as in the lemma: Tr(g+ g5 M) multiplies g5 g-)
check('F1 dual basis Tr(Gamma_i X_j)/4 = delta_ij', np.allclose(D, np.eye(4)), str(np.round(D.real, 12)))
# dimension count of the block P_+ (.) P_-
basis = []
for i in range(4):
    for j in range(4):
        E = np.zeros((4, 4), dtype=complex); E[i, j] = 1
        basis.append((Pp @ E @ Pm).flatten())
rank = np.linalg.matrix_rank(np.array(basis), tol=1e-10)
check('F1 dim of the block P_+ Mat_4 P_- equals 4', rank == 4, 'rank=%d' % rank)
print('\nSUMMARY s1: %d/%d PASS' % (sum(PASS), len(PASS)))
