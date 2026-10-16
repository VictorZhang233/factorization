# R-M20: independent numerical check of the colour algebra behind CdFR (JHEP 07 (2012) 026, Sec. 6.2) and
# FSS (JHEP 11 (2012) 066, Sec. 5):
#  (1) f_abc T_i^a T_j^b T_k^c  =  -i [T_i.T_j , T_i.T_k]   (identity), and it is Hermitian;
#  (2) in the trace (colour-flow) basis of the colour-singlet space the matrices of all T_i.T_j are REAL;
#  (3) hence <M| f T_i T_j T_k |M> = 0 for every colour vector M with relatively real components in that basis
#      (FSS: pure-QCD tree amplitudes), but it is generically non-zero for complex components (CdFR's general case);
#  (4) CdFR eq. (2partcorrcan): Sp0^dagger f_abc T_1^a T_2^b Sp0 = 0 for the tree-level q -> q g splitting.
# Process for (1)-(3): n = 5 partons  q(1) qbar(2) q(3) qbar(4) g(5)  (all outgoing convention), colour space 3x3b x3x3b x8.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import itertools

# Gell-Mann matrices
l = np.zeros((8, 3, 3), dtype=complex)
l[0][0, 1] = l[0][1, 0] = 1
l[1][0, 1] = -1j; l[1][1, 0] = 1j
l[2][0, 0] = 1; l[2][1, 1] = -1
l[3][0, 2] = l[3][2, 0] = 1
l[4][0, 2] = -1j; l[4][2, 0] = 1j
l[5][1, 2] = l[5][2, 1] = 1
l[6][1, 2] = -1j; l[6][2, 1] = 1j
l[7][0, 0] = l[7][1, 1] = 1/np.sqrt(3); l[7][2, 2] = -2/np.sqrt(3)
t = l/2
f = np.zeros((8, 8, 8))
for a, b, c in itertools.product(range(8), repeat=3):
    f[a, b, c] = np.real(-2j*np.trace((t[a] @ t[b] - t[b] @ t[a]) @ t[c]))
# checks: [t^a,t^b] = i f_abc t^c
err = max(np.abs(t[a] @ t[b] - t[b] @ t[a] - 1j*np.einsum('c,cij->ij', f[a, b], t)).max() for a in range(8) for b in range(8))
print('[t^a,t^b]-i f t^c max err =', err)
Fadj = np.array([-1j*f[a] for a in range(8)])   # (T_g^a)_{bc} = -i f_abc
err2 = max(np.abs(Fadj[a] @ Fadj[b] - Fadj[b] @ Fadj[a] - 1j*np.einsum('c,cij->ij', f[a, b], Fadj)).max() for a in range(8) for b in range(8))
print('adjoint rep algebra max err =', err2)

kinds = ['q', 'qb', 'q', 'qb', 'g']
dims = [3 if k != 'g' else 8 for k in kinds]
D = int(np.prod(dims))

def gen(kind, a):
    if kind == 'q':
        return t[a]
    if kind == 'qb':
        return -t[a].T
    return Fadj[a]

def embed(op, pos):
    mats = [np.eye(d) for d in dims]
    mats[pos] = op
    out = mats[0]
    for m in mats[1:]:
        out = np.kron(out, m)
    return out

T = [[embed(gen(kinds[i], a), i) for a in range(8)] for i in range(5)]
Ttot = [sum(T[i][a] for i in range(5)) for a in range(8)]

# trace-basis singlets  c[i1,j2,i3,j4,a5]
d = np.eye(3)
basis = []
basis.append(np.einsum('ij,akl->ijkla', d, t).reshape(-1))        # delta_{1 2} (t^a)_{3 4}
basis.append(np.einsum('aij,kl->ijkla', t, d).reshape(-1))        # (t^a)_{1 2} delta_{3 4}
basis.append(np.einsum('il,akj->ijkla', d, t).reshape(-1))        # delta_{1 4} (t^a)_{3 2}
basis.append(np.einsum('ail,kj->ijkla', t, d).reshape(-1))        # (t^a)_{1 4} delta_{3 2}
Cb = np.array(basis).T   # D x 4
sing_err = max(np.abs(Ttot[a] @ Cb).max() for a in range(8))
print('colour conservation on trace basis: max |sum_i T_i^a c| =', sing_err)
# dimension of the singlet space
Mstack = np.vstack(Ttot)
sv = np.linalg.svd(Mstack, compute_uv=False)
print('singlet-space dimension (null space of sum_i T_i^a) =', int(np.sum(sv < 1e-10)) + max(0, D - Mstack.shape[1]))
G = Cb.conj().T @ Cb
print('Gram matrix real?  max|Im G| =', np.abs(G.imag).max(), '; rank =', np.linalg.matrix_rank(G))
Ginv = np.linalg.inv(G)

def TdotT(i, j):
    return sum(T[i][a] @ T[j][a] for a in range(8))

maxim = 0.0
for i in range(5):
    for j in range(5):
        if i == j:
            continue
        A = Ginv @ (Cb.conj().T @ TdotT(i, j) @ Cb)
        maxim = max(maxim, np.abs(A.imag).max())
        # T.T must map the singlet space into itself
        resid = np.abs(TdotT(i, j) @ Cb - Cb @ A).max()
        assert resid < 1e-10, resid
print('max |Im| of T_i.T_j matrices in the trace basis =', maxim)

rng = np.random.default_rng(1)
worst_real, best_complex = 0.0, 0.0
for (i, j, k) in itertools.permutations(range(5), 3):
    F = sum(f[a, b, c]*T[i][a] @ T[j][b] @ T[k][c] for a in range(8) for b in range(8) for c in range(8) if f[a, b, c] != 0)
    # identity (1) and hermiticity, restricted to singlets
    comm = TdotT(i, j) @ TdotT(i, k) - TdotT(i, k) @ TdotT(i, j)
    idr = np.abs((F - (-1j)*comm) @ Cb).max()
    herm = np.abs(Cb.conj().T @ (F - F.conj().T) @ Cb).max()
    assert idr < 1e-10 and herm < 1e-10, (idr, herm)
    for trial in range(3):
        mr = rng.normal(size=4)
        M = Cb @ mr
        worst_real = max(worst_real, abs(M.conj() @ F @ M)/np.linalg.norm(M)**2)
        mc = rng.normal(size=4) + 1j*rng.normal(size=4)
        Mc = Cb @ mc
        best_complex = max(best_complex, abs(M.conj() @ F @ M) if False else abs(Mc.conj() @ F @ Mc)/np.linalg.norm(Mc)**2)
print('identity f T_i T_j T_k = -i[T_i.T_j, T_i.T_k] and hermiticity: verified for all 60 ordered triples (on singlets)')
print('max |<M|f T T T|M>|/|M|^2 over REAL trace-basis components   =', worst_real)
print('max |<M|f T T T|M>|/|M|^2 over COMPLEX trace-basis components =', best_complex)

# (4) CdFR eq. (2partcorrcan) for q -> q g: Sp0 colour part (Sp)_{(i1,a2), iP} = (t^{a2})_{i1 iP}
Sp = np.zeros((3*8, 3), dtype=complex)
for i1 in range(3):
    for a2 in range(8):
        for iP in range(3):
            Sp[i1*8 + a2, iP] = t[a2][i1, iP]
T1 = [np.kron(t[a], np.eye(8)) for a in range(8)]
T2 = [np.kron(np.eye(3), Fadj[a]) for a in range(8)]
worst = 0.0
for c in range(8):
    X = sum(f[a, b, c]*Sp.conj().T @ T1[a] @ T2[b] @ Sp for a in range(8) for b in range(8) if f[a, b, c] != 0)
    worst = max(worst, np.abs(X).max())
print('CdFR (2partcorrcan), q->qg: max |Sp0^+ f_abc T_1^a T_2^b Sp0| =', worst)
