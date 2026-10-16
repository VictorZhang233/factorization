# Does the half-coincident colour residual [X1,X2] = i f^{abc} T_i^c T_j1^a T_j2^b vanish on colour-singlet
# spectator states?  (a) three spectators (i, j1, j2): yes, identically (X1, X2 are functions of T_j1.T_j2
# on singlets).  (b) with a fourth, passive spectator: compute the singlet-space matrix.
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
def su3():
    l = np.zeros((8, 3, 3), dtype=complex)
    l[0][0,1] = l[0][1,0] = 1; l[1][0,1] = -1j; l[1][1,0] = 1j; l[2][0,0] = 1; l[2][1,1] = -1
    l[3][0,2] = l[3][2,0] = 1; l[4][0,2] = -1j; l[4][2,0] = 1j; l[5][1,2] = l[5][2,1] = 1
    l[6][1,2] = -1j; l[6][2,1] = 1j; l[7][0,0] = l[7][1,1] = 1/np.sqrt(3); l[7][2,2] = -2/np.sqrt(3)
    return l/2
F3 = su3(); F3b = np.array([-t.T for t in F3])
fabc = np.zeros((8, 8, 8))
for a in range(8):
    for b in range(8):
        cm = F3[a] @ F3[b] - F3[b] @ F3[a]
        for c in range(8): fabc[a, b, c] = np.real(-2j*np.trace(cm @ F3[c]))
Adj = np.array([-1j*fabc[a] for a in range(8)])        # (T^a_adj)_{bc} = -i f^{abc}
reps = {'3': F3, '3b': F3b, '8': Adj}
def embed(mats, pos, dims):
    out = []
    for a in range(8):
        ops = [np.eye(d) for d in dims]; ops[pos] = mats[a]
        M = ops[0]
        for o in ops[1:]: M = np.kron(M, o)
        out.append(M)
    return out
def analyse(labels):
    dims = [reps[l].shape[1] for l in labels]
    Ts = [embed(reps[l], p, dims) for p, l in enumerate(labels)]
    tot = [sum(Ts[p][a] for p in range(len(labels))) for a in range(8)]
    C = sum(t @ t for t in tot)
    w, V = np.linalg.eigh(C); S = V[:, np.abs(w) < 1e-8]
    X1 = sum(Ts[0][a] @ Ts[1][a] for a in range(8)); X2 = sum(Ts[0][a] @ Ts[2][a] for a in range(8))
    K = X1 @ X2 - X2 @ X1
    M = S.conj().T @ K @ S if S.shape[1] else np.zeros((0, 0))
    print(f"spectators (i, j1, j2{', passive' if len(labels) > 3 else ''}) = {labels}: #singlets = {S.shape[1]}, "
          f"max|<S'|[X1,X2]|S>| = {np.max(np.abs(M)) if M.size else 0:.3e}")
for labels in [('3b','3b','3b'), ('3','3','3'), ('3b','8','3'), ('8','8','8'), ('8','3','3b'),
               ('3b','3b','3b','8'), ('3','3b','3b','3'), ('3b','3','3b','3'), ('8','8','8','8'), ('3b','8','8','3')]:
    analyse(labels)
