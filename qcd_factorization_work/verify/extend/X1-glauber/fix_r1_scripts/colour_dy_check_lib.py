# Shared colour library for the X1 fix-round-1 checks: SU(3) irreps 3, 3bar, 8 in a common real weight
# basis; embedding into tensor products; real singlet bases via the zero-weight subspace.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np

# ---------- irreps in a common real weight basis
lam = np.zeros((8, 3, 3), dtype=complex)
lam[0][0, 1] = lam[0][1, 0] = 1
lam[1][0, 1] = -1j; lam[1][1, 0] = 1j
lam[2][0, 0] = 1; lam[2][1, 1] = -1
lam[3][0, 2] = lam[3][2, 0] = 1
lam[4][0, 2] = -1j; lam[4][2, 0] = 1j
lam[5][1, 2] = lam[5][2, 1] = 1
lam[6][1, 2] = -1j; lam[6][2, 1] = 1j
lam[7][0, 0] = lam[7][1, 1] = 1/np.sqrt(3); lam[7][2, 2] = -2/np.sqrt(3)
T3 = lam/2
T3b = np.array([-t.conj() for t in T3])                     # conjugate rep  -T^*
f = np.zeros((8, 8, 8))
for a in range(8):
    for b in range(8):
        cm = T3[a] @ T3[b] - T3[b] @ T3[a]
        for c in range(8):
            f[a, b, c] = np.real(-2j*np.trace(cm @ T3[c]))
# adjoint inside 3 x 3bar: real basis {e_i ebar_j (i != j), (e1e1-e2e2)/sqrt2, (e1e1+e2e2-2e3e3)/sqrt6}
V = np.zeros((9, 8))
col = 0
for i in range(3):
    for j in range(3):
        if i != j:
            V[3*i + j, col] = 1; col += 1
V[0, 6] = 1/np.sqrt(2); V[4, 6] = -1/np.sqrt(2)
V[0, 7] = V[4, 7] = 1/np.sqrt(6); V[8, 7] = -2/np.sqrt(6)
T8 = np.array([V.T @ (np.kron(T3[a], np.eye(3)) + np.kron(np.eye(3), T3b[a])) @ V for a in range(8)])
reps = {'3': T3, '3b': T3b, '8': T8}
s = np.array([1, -1, 1, 1, -1, 1, -1, 1])                   # (T^a)^* = s_a T^a


def embed(labels):
    dims = [reps[l].shape[1] for l in labels]
    out = []
    for p, l in enumerate(labels):
        mats = []
        for a in range(8):
            ops = [np.eye(d) for d in dims]; ops[p] = reps[l][a]
            M = ops[0]
            for o in ops[1:]:
                M = np.kron(M, o)
            mats.append(M)
        out.append(np.array(mats))
    return out, int(np.prod(dims))

def singlets(labels):
    """real orthonormal basis of the colour-singlet subspace (columns), via the zero-weight subspace"""
    Ts, D = embed(labels)
    tot = sum(Ts)
    h3 = np.real(np.diag(tot[2])); h8 = np.real(np.diag(tot[7]))
    Z = np.where((np.abs(h3) < 1e-9) & (np.abs(h8) < 1e-9))[0]
    CZ = sum(tot[a][:, Z].conj().T @ tot[a][:, Z] for a in range(8))
    assert np.allclose(CZ.imag, 0)
    w, U = np.linalg.eigh(CZ.real)
    S = np.zeros((D, int(np.sum(np.abs(w) < 1e-9))))
    S[Z, :] = U[:, np.abs(w) < 1e-9]
    if S.shape[1]:
        assert max(np.max(np.abs(tot[a] @ S)) for a in range(8)) < 1e-9
    return S, Ts

def X(Ti, Tj):
    return sum(Ti[a] @ Tj[a] for a in range(8))

