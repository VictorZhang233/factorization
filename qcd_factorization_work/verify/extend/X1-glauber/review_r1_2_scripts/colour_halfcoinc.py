# Reviewer-2: colour matrix elements of the half-coincident commutator [X1,X2] = i f^{abc} T_i^c T_j1^a T_j2^b
# (i) operator norm on the total-singlet space (cf. X1's L4(d)); (ii) expectation value in physically natural
# valence colour states (baryon diquark + antibaryon anti-diquark; meson + baryon).
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
def su3():
    l = np.zeros((8, 3, 3), dtype=complex)
    l[0][0,1] = l[0][1,0] = 1; l[1][0,1] = -1j; l[1][1,0] = 1j; l[2][0,0] = 1; l[2][1,1] = -1
    l[3][0,2] = l[3][2,0] = 1; l[4][0,2] = -1j; l[4][2,0] = 1j; l[5][1,2] = l[5][2,1] = 1
    l[6][1,2] = -1j; l[6][2,1] = 1j; l[7][0,0] = l[7][1,1] = 1/np.sqrt(3); l[7][2,2] = -2/np.sqrt(3)
    return l/2
T3 = su3(); T3b = np.array([-t.T for t in T3])
f = np.zeros((8, 8, 8))
for a, b, c in itertools.product(range(8), repeat=3):
    f[a, b, c] = np.real(-2j*np.trace((T3[a] @ T3[b] - T3[b] @ T3[a]) @ T3[c]))
def adj(): return np.array([-1j*f[a] for a in range(8)])   # (T^a)_{bc} = -i f^{abc}
T8 = adj()
REP = {'3': T3, '3b': T3b, '8': T8}
def op(Ts, slot, n_slots, dims):
    """embed generator array Ts (8,d,d) acting on slot into the tensor space"""
    out = []
    for a in range(8):
        mats = [np.eye(d) for d in dims]; mats[slot] = Ts[a]
        M = mats[0]
        for m in mats[1:]: M = np.kron(M, m)
        out.append(M)
    return np.array(out)
def commutator_ops(labels, i=0, j1=1, j2=2):
    dims = [REP[l].shape[1] for l in labels]
    Ti = op(REP[labels[i]], i, len(labels), dims)
    Tj1 = op(REP[labels[j1]], j1, len(labels), dims)
    Tj2 = op(REP[labels[j2]], j2, len(labels), dims)
    X1 = sum(Ti[a] @ Tj1[a] for a in range(8)); X2 = sum(Ti[a] @ Tj2[a] for a in range(8))
    Ttot = sum(op(REP[l], s, len(labels), dims) for s, l in enumerate(labels))
    return X1 @ X2 - X2 @ X1, Ttot
def singlets(Ttot):
    C = sum(Ttot[a].conj().T @ Ttot[a] for a in range(8))   # Casimir (hermitian, PSD)
    w, V = np.linalg.eigh((C + C.conj().T)/2)
    return V[:, np.abs(w) < 1e-9]
# (i) operator norm on singlet space
for labels in (('3b', '3b', '3b', '8'), ('3', '3b', '3b', '3'), ('3b', '3', '3b', '3'), ('3', '3b', '3b', '3b', '3b')):
    Cm, Tt = commutator_ops(labels)
    S = singlets(Tt)
    M = S.conj().T @ Cm @ S
    ev = np.linalg.eigvals(M) if M.size else []
    print(f"(i) spectators (i,j1,j2,...) = {labels}: dim singlet = {S.shape[1]}, ||P_S [X1,X2] P_S|| = {max(abs(np.array(ev))) if len(ev) else 0:.4f}")
# (ii) natural valence states:
# baryon A: active quark + spectators (i, i') in 3x3 -> 3bar (eps); antibaryon B: active antiquark + (j1, j2) in 3bx3b -> 3 (eps).
# After V_H (q qbar -> singlet), spectators (i, i', j1, j2) are in Psi = eps_{a b g} eps_{r s g} / norm.
eps = np.zeros((3, 3, 3))
for p in itertools.permutations(range(3)):
    eps[p] = np.linalg.det(np.eye(3)[list(p)])
Psi = np.einsum('abg,rsg->abrs', eps, eps).reshape(-1); Psi = Psi/np.linalg.norm(Psi)
labels = ('3', '3', '3b', '3b')         # slots: i, i', j1, j2
dims = [3, 3, 3, 3]
Ti = op(T3, 0, 4, dims); Tj1 = op(T3b, 2, 4, dims); Tj2 = op(T3b, 3, 4, dims)
X1 = sum(Ti[a] @ Tj1[a] for a in range(8)); X2 = sum(Ti[a] @ Tj2[a] for a in range(8))
Cm = X1 @ X2 - X2 @ X1
Ttot = sum(op(REP[l], s, 4, dims) for s, l in enumerate(labels))
print("(ii) baryon-antibaryon valence state: total colour of Psi =", np.round(np.real(Psi.conj() @ sum(Ttot[a] @ Ttot[a] for a in range(8)) @ Psi), 12),
      " <Psi|[X1,X2]|Psi> =", np.round(Psi.conj() @ Cm @ Psi, 14))
# same with i coupled to j1 and to the OTHER B spectator replaced by passive i': lines i-j1, i-j2 are what T3 needs.
# also a "generic" singlet in the same space:
S = singlets(Ttot); rng = np.random.default_rng(1)
for t in range(3):
    v = S @ (rng.normal(size=S.shape[1]) + 1j*rng.normal(size=S.shape[1])); v = v/np.linalg.norm(v)
    print(f"     generic singlet #{t}: <v|[X1,X2]|v> = {v.conj() @ Cm @ v:.6f}")
print("     real singlet basis vectors:", [np.round(S[:, k].conj() @ Cm @ S[:, k], 12) for k in range(S.shape[1])])
