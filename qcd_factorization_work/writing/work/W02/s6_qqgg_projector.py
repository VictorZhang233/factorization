"""W02 / Ch2 check s6 (ex:qcd-qqbar-gg, prop:appJ-ghost-cuts): the intermediate identities used in the printed
derivation of  sum_phys |A|^2 = sum_{-g,-g} |A|^2 - 2 sum |A_gh|^2  for q qbar -> g g (on-shell gluons):
  (i)   A^{mu nu} k2_nu = k1^mu A_gh     and   k1_mu A^{mu nu} = k2^nu A_gh   (on shell, any polarisation of the other gluon)
  (ii)  A_gh = g^2 f^{abc} (k1.J_c)/Q^2 = -g^2 f^{abc} (k2.J_c)/Q^2   (current conservation Q.J = 0)
  (iii) the projector P^{mu mu'} = -g + (k kbar + kbar k)/(k.kbar) = sum over the two transverse polarisations
  (iv)  term-by-term: (-g)(-g) part, the two cross parts (-2|A_gh|^2 each) and the Delta Delta part (+2|A_gh|^2),
        summed over spins and colours.
Feynman rules of def:prelim-feynman-rules (D = d - i g A, vertex i g gamma^mu t^a), Feynman gauge for the s-channel gluon.
Run: python3 -I s6_qqgg_projector.py
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
npass = nfail = 0
def report(ok, name, detail=''):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(('PASS ' if ok else 'FAIL ') + name + (('   [' + detail + ']') if detail else ''), flush=True)
eta = np.diag([1., -1, -1, -1])
I2 = np.eye(2); Z2 = np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
g0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
gam = [g0] + [np.block([[Z2, s], [-s, Z2]]) for s in (sx, sy, sz)]
def sl(p): return sum(eta[m, m] * p[m] * gam[m] for m in range(4))
def dot(a, b): return a @ eta @ b
lam = np.zeros((8, 3, 3), complex)
lam[0][0, 1] = lam[0][1, 0] = 1; lam[1][0, 1] = -1j; lam[1][1, 0] = 1j; lam[2][0, 0] = 1; lam[2][1, 1] = -1
lam[3][0, 2] = lam[3][2, 0] = 1; lam[4][0, 2] = -1j; lam[4][2, 0] = 1j; lam[5][1, 2] = lam[5][2, 1] = 1
lam[6][1, 2] = -1j; lam[6][2, 1] = 1j; lam[7] = np.diag([1, 1, -2]) / np.sqrt(3)
T = lam / 2
f = np.zeros((8, 8, 8))
for a, b, c in itertools.product(range(8), repeat=3):
    f[a, b, c] = np.real(-2j * np.trace((T[a] @ T[b] - T[b] @ T[a]) @ T[c]))
g = 1.0
def V3(k, mu, a, p, nu, b, q, rho, c):
    return g * f[a, b, c] * (eta[mu, nu] * (k - p)[rho] + eta[nu, rho] * (p - q)[mu] + eta[rho, mu] * (q - k)[nu])
def S(p): return 1j * sl(p) / dot(p, p)
def Dg(k): return -1j / dot(k, k) * np.linalg.inv(eta)
def amplitude(p1, p2, k1, k2, a, b):
    A = np.zeros((4, 4, 12, 12), complex); Q = p1 + p2; Dq = Dg(Q)
    for mu in range(4):
        for nu in range(4):
            M = np.kron(1j * g * gam[nu] @ S(p1 - k1) @ (1j * g * gam[mu]), T[b] @ T[a])
            M += np.kron(1j * g * gam[mu] @ S(p1 - k2) @ (1j * g * gam[nu]), T[a] @ T[b])
            for c in range(8):
                if f[c, a, b] == 0: continue
                for r in range(4):
                    v = V3(Q, r, c, -k1, mu, a, -k2, nu, b)
                    if v == 0: continue
                    M += np.kron(1j * g * gam[r], T[c]) * (eta[r, r] * Dq[r, r] * eta[r, r]) * v
            A[mu, nu] = M
    return A
def massless(E, th, ph): return E * np.array([1, np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)])
p1 = massless(3.0, 0.4, 0.9); p2 = massless(2.0, 2.2, 3.5); Q = p1 + p2
M = np.sqrt(dot(Q, Q)); bb = Q[1:] / Q[0]; gm_ = 1 / np.sqrt(1 - bb @ bb)
def boost(v):
    t0 = v[0]; x = v[1:]; bp = bb @ x
    return np.concatenate([[gm_ * (t0 + bp)], x + ((gm_ - 1) * bp / (bb @ bb) + gm_ * t0) * bb])
th, ph = 1.1, 0.7
k1 = boost(M / 2 * np.array([1, np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)]))
k2 = boost(M / 2 * np.array([1, -np.sin(th) * np.cos(ph), -np.sin(th) * np.sin(ph), -np.cos(th)]))
def kbar(k): return np.array([k[0], -k[1], -k[2], -k[3]])
def transverse(k):
    n = k[1:] / np.linalg.norm(k[1:]); t1 = np.cross(n, [0.3, 0.1, 0.9]); t1 /= np.linalg.norm(t1); t2 = np.cross(n, t1)
    return [np.concatenate([[0], t1]), np.concatenate([[0], t2])]
eps1 = transverse(k1); eps2 = transverse(k2)
# (iii) projector
for k, eps in ((k1, eps1), (k2, eps2)):
    kb = kbar(k)
    P = -np.linalg.inv(eta) + (np.outer(k, kb) + np.outer(kb, k)) / dot(k, kb)     # upper indices
    Ps = sum(np.outer(e, e) for e in eps)
    report(np.allclose(P, Ps), '(iii) -g^{mu nu} + (k kbar + kbar k)/(k.kbar) = sum_{lambda=1,2} eps^mu eps^nu (on-shell k, kbar = (k0,-k))')
up = sl(p1) @ np.array([1, 0.3, -0.2j, 0.5], complex); vp = sl(p2) @ np.array([0.2, 1, 0.4j, -0.3], complex)
vbar = vp.conj() @ g0
colq = np.array([0.3 + 0.1j, -0.7, 0.2j]); colqb = np.array([0.5, 0.1 - 0.4j, 0.9])
def sand(Mx): return np.kron(vbar, colqb.conj()) @ Mx @ np.kron(up, colq)
lower = lambda v: eta @ v
ok1 = ok2 = ok3 = True
for a, b in [(0, 1), (2, 4), (3, 6), (7, 5)]:
    A = amplitude(p1, p2, k1, k2, a, b)
    Agh = sum(g**2 * f[a, b, c] / dot(Q, Q) * sand(np.kron(sl(k1), T[c])) for c in range(8))
    Agh2 = sum(-g**2 * f[a, b, c] / dot(Q, Q) * sand(np.kron(sl(k2), T[c])) for c in range(8))
    ok3 &= np.isclose(Agh, Agh2)
    for mu in range(4):
        lhs = sand(sum(A[mu, n] * lower(k2)[n] for n in range(4)))
        ok1 &= np.isclose(lhs, k1[mu] * Agh)
    for nu in range(4):
        lhs = sand(sum(A[m, nu] * lower(k1)[m] for m in range(4)))
        ok2 &= np.isclose(lhs, k2[nu] * Agh)
report(ok1, '(i) A^{mu nu} k2_nu = k1^mu A_gh (on-shell gluons, quark spinors on shell)')
report(ok2, '(i) k1_mu A^{mu nu} = k2^nu A_gh')
report(ok3, '(ii) A_gh = g^2 f^{abc} k1.J_c/Q^2 = -g^2 f^{abc} k2.J_c/Q^2 (Q.J = 0 on shell)')
# (iv) term-by-term decomposition, summed over spins (traces) and colours
def tr_pair(M1, M2):
    """sum over spins and colours of (vbar M1 u)(vbar M2 u)^*"""
    M2b = np.kron(g0, np.eye(3)) @ M2.conj().T @ np.kron(g0, np.eye(3))
    return np.trace(M1 @ np.kron(sl(p1), np.eye(3)) @ M2b @ np.kron(sl(p2), np.eye(3)))
def contract(A, e1, e2): return sum(A[m, n] * lower(e1)[m] * lower(e2)[n] for m in range(4) for n in range(4))
gg = gD = Dg_ = DD = phys = gh2 = 0
P1 = -np.linalg.inv(eta) + (np.outer(k1, kbar(k1)) + np.outer(kbar(k1), k1)) / dot(k1, kbar(k1))
P2 = -np.linalg.inv(eta) + (np.outer(k2, kbar(k2)) + np.outer(kbar(k2), k2)) / dot(k2, kbar(k2))
D1 = P1 + np.linalg.inv(eta); D2 = P2 + np.linalg.inv(eta); mg = -np.linalg.inv(eta)
def quad(A, X1, X2):
    """sum_{mu mu' nu nu'} A_{mu nu} A*_{mu' nu'} X1^{mu mu'} X2^{nu nu'} (indices lowered on A) summed over spins/colours"""
    Al = np.einsum('mnij,m,n->mnij', A, np.diag(eta), np.diag(eta))
    tot = 0
    for m, mp, n, np_ in itertools.product(range(4), repeat=4):
        w = X1[m, mp] * X2[n, np_]
        if w == 0: continue
        tot += w * tr_pair(Al[m, n], Al[mp, np_])
    return tot
for a in range(8):
    for b in range(8):
        A = amplitude(p1, p2, k1, k2, a, b)
        gg += quad(A, mg, mg); gD += quad(A, mg, D2); Dg_ += quad(A, D1, mg); DD += quad(A, D1, D2)
        for e1 in eps1:
            for e2 in eps2:
                Mx = contract(A, e1, e2); phys += tr_pair(Mx, Mx)
        Mgh = sum(g**2 * f[a, b, c] / dot(Q, Q) * np.kron(sl(k1), T[c]) for c in range(8))
        gh2 += tr_pair(Mgh, Mgh)
gg, gD, Dg_, DD, phys, gh2 = [np.real(x) for x in (gg, gD, Dg_, DD, phys, gh2)]
report(np.isclose(gD, -2 * gh2) and np.isclose(Dg_, -2 * gh2), '(iv) each cross term (-g) x Delta = -2 sum|A_gh|^2', f'{gD:.8f}, {Dg_:.8f}, -2gh = {-2*gh2:.8f}')
report(np.isclose(DD, 2 * gh2), '(iv) Delta x Delta term = +2 sum|A_gh|^2', f'{DD:.8f} vs {2*gh2:.8f}')
report(np.isclose(phys, gg + gD + Dg_ + DD) and np.isclose(phys, gg - 2 * gh2), '(iv) phys = (-g)(-g) - 2|A_gh|^2 - 2|A_gh|^2 + 2|A_gh|^2 = (-g)(-g) - 2 sum|A_gh|^2')
s = dot(Q, Q); t = dot(p1 - k1, p1 - k1); u = dot(p1 - k2, p1 - k2)
report(np.isclose(phys / 36, g**4 * (32 / 27 * (t**2 + u**2) / (t * u) - 8 / 3 * (t**2 + u**2) / s**2)), '(1/36) phys = g^4[32/27 (t^2+u^2)/(tu) - 8/3 (t^2+u^2)/s^2]  (VF-WL-9)')
print(f'\nSUMMARY: {npass}/{npass + nfail} PASS')
