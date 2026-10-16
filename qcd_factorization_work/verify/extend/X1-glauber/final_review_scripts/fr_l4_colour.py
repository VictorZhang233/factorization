# Final review of X1 -- L4(d1),(d2) and the basis-independent norms ||P[X1,X2]P|| on DY remnant spaces.
# Independent implementation: Gell-Mann generators; 3bar = -(T)^*; adjoint (T^a)_{bc} = -i f^{abc}.
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
lam = np.zeros((8, 3, 3), dtype=complex)
lam[0][0,1] = lam[0][1,0] = 1
lam[1][0,1] = -1j; lam[1][1,0] = 1j
lam[2][0,0] = 1; lam[2][1,1] = -1
lam[3][0,2] = lam[3][2,0] = 1
lam[4][0,2] = -1j; lam[4][2,0] = 1j
lam[5][1,2] = lam[5][2,1] = 1
lam[6][1,2] = -1j; lam[6][2,1] = 1j
lam[7] = np.diag([1, 1, -2])/np.sqrt(3)
T3 = lam/2
f = np.zeros((8, 8, 8))
for a, b, c in itertools.product(range(8), repeat=3):
    f[a, b, c] = np.real(-2j*np.trace((T3[a] @ T3[b] - T3[b] @ T3[a]) @ T3[c]))
Tb = -np.conj(T3)
T8 = np.array([-1j*f[a] for a in range(8)])
rep = {'q': T3, 'qb': Tb, 'g': T8}
def gens(labels):
    dims = [rep[l].shape[1] for l in labels]
    out = []
    for p, l in enumerate(labels):
        Tp = []
        for a in range(8):
            mats = [np.eye(d) for d in dims]; mats[p] = rep[l][a]
            M = mats[0]
            for m in mats[1:]:
                M = np.kron(M, m)
            Tp.append(M)
        out.append(np.array(Tp))
    return out
def singlets(Ts):
    tot = sum(Ts)
    cas = sum(tot[a] @ tot[a] for a in range(8))
    w, v = np.linalg.eigh(cas)
    return v[:, np.abs(w) < 1e-9]
def isotypic_proj(Tsub, casval):
    tot = sum(Tsub); cas = sum(tot[a] @ tot[a] for a in range(8))
    w, v = np.linalg.eigh(cas)
    V = v[:, np.abs(w - casval) < 1e-9]
    return V @ V.conj().T
C3 = 4/3
configs = [('qb', ['qb', 'qb', 'g']), (['q', 'q'], ['qb', 'qb', 'g']), (['q', 'q'], ['qb', 'q', 'q']), ('qb', ['qb', 'q', 'q'])]
report = {0: 0.4330, 1: 0.2165, 2: 0.3536, 3: 0.7071}
for ic, (Arem, Brem) in enumerate(configs):
    Arem = [Arem] if isinstance(Arem, str) else Arem
    labels = Arem + Brem
    Ts = gens(labels)
    nA = len(Arem)
    # restrict A-rem to its 3bar isotypic part (C_2 = 4/3) and take total singlets
    PA = isotypic_proj(Ts[:nA], C3)
    S = singlets(Ts)
    # keep singlets whose A-rem part lies in the 3bar component
    M = S.conj().T @ PA @ S
    w, v = np.linalg.eigh((M + M.conj().T)/2)
    Sdy = S @ v[:, np.abs(w - 1) < 1e-9]
    norms = []; d1err = 0.0
    for i in range(nA):
        for j1, j2 in itertools.permutations(range(nA, len(labels)), 2):
            X1 = sum(Ts[i][a] @ Ts[j1][a] for a in range(8))
            X2 = sum(Ts[i][a] @ Ts[j2][a] for a in range(8))
            Cm = Sdy.conj().T @ (X1 @ X2 - X2 @ X1) @ Sdy
            norms.append(np.linalg.norm(Cm, 2))
            # (d1): <psi|[X1,X2]|psi> = -<psi|(K_i x 1) i f^{abc} T^a_j1 T^b_j2 sum_k T^c_k|psi>, k in B-rem \ {j1,j2}
            others = [k for k in range(nA, len(labels)) if k not in (j1, j2)]
            OB = sum(1j*f[a, b, c]*Ts[j1][a] @ Ts[j2][b] @ sum(Ts[k][c] for k in others)
                     for a in range(8) for b in range(8) for c in range(8) if abs(f[a, b, c]) > 1e-12) if others else 0*X1
            Kfac = 1.0 if nA == 1 else 0.5
            for _ in range(5):
                c = np.random.default_rng(len(norms)).normal(size=Sdy.shape[1]) + 1j*np.random.default_rng(len(norms)+99).normal(size=Sdy.shape[1])
                psi = Sdy @ c; psi /= np.linalg.norm(psi)
                lhs = psi.conj() @ (X1 @ X2 - X2 @ X1) @ psi
                rhs = -Kfac*(psi.conj() @ OB @ psi)
                d1err = max(d1err, abs(lhs - rhs))
    print(f"A-rem={'+'.join(Arem):6s} B-rem={'+'.join(Brem):10s}: dim(DY singlets)={Sdy.shape[1]}, "
          f"||P[X1,X2]P|| over all (i,j1,j2) in [{min(norms):.4f}, {max(norms):.4f}] (report {report[ic]});  (d1) max err {d1err:.1e}")
