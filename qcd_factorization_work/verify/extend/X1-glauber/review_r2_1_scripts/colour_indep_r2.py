# Round-2 reviewer #1: independent colour checks for L4 (b), (c), (d1), (d2) of the X1 report (fix round 1).
# Own construction (does not import the author's colour library):
#   - fundamental: Gell-Mann/2; antifundamental: -T^*; octet: traceless part of 3 x 3bar, with a RANDOM real
#     orthogonal basis of the octet subspace (tests basis independence of the norms);
#   - singlet / DY subspaces from null spaces of real symmetric Casimir matrices.
# Checks:
#   (S) side-sum algebra of L4(b) under two conventions for the one-exchange amplitude (sign of [X1,X2]);
#   (C) L4(c): [X1,X2] = 0 on the singlet space of (i,j1,j2) alone;
#   (D1) L4(d1): <psi|[X1,X2]|psi> = -kappa_i <psi| i f T_j1 T_j2 sum_k T_k |psi>, and = 0 when B-rem={j1,j2};
#   (D2) L4(d2): [X1,X2] real antisymmetric in the real product basis -> zero on real psi;
#   (N) operator norms ||P[X1,X2]P|| for the four DY remnant spaces quoted in L4(d3), all (j1,j2) choices.
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
rng = np.random.default_rng(20261011)

gm = np.zeros((8, 3, 3), dtype=complex)
gm[0][0, 1] = gm[0][1, 0] = 1
gm[1][0, 1], gm[1][1, 0] = -1j, 1j
gm[2][0, 0], gm[2][1, 1] = 1, -1
gm[3][0, 2] = gm[3][2, 0] = 1
gm[4][0, 2], gm[4][2, 0] = -1j, 1j
gm[5][1, 2] = gm[5][2, 1] = 1
gm[6][1, 2], gm[6][2, 1] = -1j, 1j
gm[7] = np.diag([1, 1, -2])/np.sqrt(3)
F = gm/2
Fb = -F.conj()
# structure constants from [T^a,T^b] = i f^{abc} T^c, Tr(T^a T^b) = delta/2
fabc = np.zeros((8, 8, 8))
for a, b, c in itertools.product(range(8), repeat=3):
    fabc[a, b, c] = np.real(-2j*np.trace((F[a] @ F[b] - F[b] @ F[a]) @ F[c]))
# octet: traceless part of 3 x 3bar, random real orthonormal basis
G9 = np.array([np.kron(F[a], np.eye(3)) + np.kron(np.eye(3), Fb[a]) for a in range(8)])
sing = np.eye(3).reshape(9)/np.sqrt(3)
Pq = np.eye(9) - np.outer(sing, sing)
w, U = np.linalg.eigh(Pq)
B8 = U[:, w > 0.5]                                        # real 9x8
Q, _ = np.linalg.qr(rng.normal(size=(8, 8)))             # random real rotation inside the octet
B8 = B8 @ Q
O = np.array([B8.T @ G9[a] @ B8 for a in range(8)])
R = {'3': F, '3b': Fb, '8': O}
for nm, T in R.items():
    cas = sum(T[a] @ T[a] for a in range(8))
    lie = max(np.max(np.abs(T[a] @ T[b] - T[b] @ T[a] - 1j*sum(fabc[a, b, c]*T[c] for c in range(8))))
              for a in range(8) for b in range(8))
    print(f"rep {nm}: dim {T.shape[1]}, Casimir {np.real(cas[0,0]):.4f}, Lie-algebra residual {lie:.1e}")
s = np.array([1, -1, 1, 1, -1, 1, -1, 1])
for nm, T in R.items():
    print(f"  real structure (T^a)^* = s_a T^a for rep {nm}: residual "
          f"{max(np.max(np.abs(T[a].conj() - s[a]*T[a])) for a in range(8)):.1e}")

def ops(labels):
    dims = [R[l].shape[1] for l in labels]
    out = []
    for p, l in enumerate(labels):
        mats = []
        for a in range(8):
            M = np.ones((1, 1))
            for q, d in enumerate(dims):
                M = np.kron(M, R[l][a] if q == p else np.eye(d))
            mats.append(M)
        out.append(np.array(mats))
    return out

def dot(A, B):
    return sum(A[a] @ B[a] for a in range(8))

def nullspace_real(M, tol=1e-9):
    M = 0.5*(M + M.conj().T)
    assert np.max(np.abs(M.imag)) < 1e-10
    w, V = np.linalg.eigh(M.real)
    return V[:, np.abs(w) < tol]

# ---------------- (S) side-sum algebra of L4(b) -------------------------------------------------------
# random commuting Hermitian "colour operators": X1 = Ti.Tj1, X2 = Ti.Tj2 on 3 x 3 x 8
Ti, Tj1, Tj2 = ops(['3', '3b', '8'])
X1, X2 = dot(Ti, Tj1), dot(Ti, Tj2)
comm = X1 @ X2 - X2 @ X1
print("(C0) [X1,X2] - i f^{abc} T_i^c T_j1^a T_j2^b:",
      np.max(np.abs(comm - 1j*sum(fabc[a, b, c]*Ti[c] @ Tj1[a] @ Tj2[b]
                                  for a, b, c in itertools.product(range(8), repeat=3) if fabc[a, b, c] != 0))))
W12 = 0.5 - 0.0306j; W21 = 1 - W12
for conv in ('M1 = c X (c complex = -i chi)', 'M1 = -i c X (c real)'):
    chi1, chi2 = 0.37, 0.81
    if conv.startswith('M1 = c X'):
        c1, c2 = -1j*chi1, -1j*chi2; A1, A2 = c1*X1, c2*X2; pref = c1*c2
    else:
        c1, c2 = chi1, chi2; A1, A2 = -1j*c1*X1, -1j*c2*X2; pref = c1*c2
    # amplitude side: 'line 1 first on i' carries X2 X1 (later insertion to the left)
    if conv.startswith('M1 = c X'):
        M2 = c1*c2*(W12*X2 @ X1 + W21*X1 @ X2)
    else:
        M2 = (-1j)**2*c1*c2*(W12*X2 @ X1 + W21*X1 @ X2)
    side = M2 + M2.conj().T + A1.conj().T @ A2 + A2.conj().T @ A1
    pred = 2j*pref*np.imag(W12)*comm
    print(f"(S) {conv:30s}: side-sum = 2i c1c2 ImW12 [X1,X2] ? residual {np.max(np.abs(side - pred)):.2e};"
          f"  = -2i c1c2 ImW12 [X1,X2] ? residual {np.max(np.abs(side + pred)):.2e}")

# ---------------- (C) singlet space of (i,j1,j2) alone --------------------------------------------------
for lab in (['3', '3b', '8'], ['8', '8', '8'], ['3', '3', '3'], ['3b', '8', '3']):
    T = ops(lab); tot = [sum(t[a] for t in T) for a in range(8)]
    S = nullspace_real(sum(t @ t for t in tot))
    X1, X2 = dot(T[0], T[1]), dot(T[0], T[2])
    c = X1 @ X2 - X2 @ X1
    print(f"(C) singlets of (i,j1,j2)={tuple(lab)}: dim {S.shape[1]}, ||P[X1,X2]P|| = "
          f"{(np.linalg.norm(S.T @ c @ S, 2) if S.shape[1] else 0):.2e}")

# ---------------- (D) DY remnant spaces -----------------------------------------------------------------
def dy_space(arem, brem):
    labels = list(arem) + list(brem)
    T = ops(labels)
    nA = len(arem)
    TA = [sum(T[p][a] for p in range(nA)) for a in range(8)]
    TB = [sum(T[p][a] for p in range(nA, len(labels))) for a in range(8)]
    Ctot = sum((TA[a] + TB[a]) @ (TA[a] + TB[a]) for a in range(8))
    S = nullspace_real(Ctot)
    CA = sum(TA[a] @ TA[a] for a in range(8))
    m = S.T @ CA @ S
    m = 0.5*(m + m.T)
    w, V = np.linalg.eigh(np.real(m))
    D = S @ V[:, np.abs(w - 4/3) < 1e-8]                 # A-rem part in the 3 or 3bar isotypic component
    return T, TA, TB, D

configs = [
    (('3b',), ('3b', '3b', '8'), 'A-rem=qbar ; B-rem=qbar qbar g'),
    (('3', '3'), ('3b', '3b', '8'), 'A-rem=qq ; B-rem=qbar qbar g'),
    (('3', '3'), ('3b', '3', '3'), 'A-rem=qq ; B-rem=qbar q q'),
    (('3b',), ('3b', '3', '3'), 'A-rem=qbar ; B-rem=qbar q q'),
    (('3', '3'), ('3b', '3b'), 'A-rem=qq ; B-rem=qbar qbar (valence p pbar)'),
    (('3', '3', '8'), ('3b', '3b'), 'A-rem=qqg ; B-rem=qbar qbar'),
    (('3b', '8'), ('3b', '3b'), 'A-rem=qbar g ; B-rem=qbar qbar'),
    (('3b',), ('3b', '8', '8'), 'A-rem=qbar ; B-rem=qbar g g'),
]
allok = True
for arem, brem, name in configs:
    T, TA, TB, D = dy_space(arem, brem)
    nA = len(arem)
    i = 0                                                  # spectator i = first A-remnant parton
    # kappa_i from Wigner-Eckart (only meaningful if the multiplicity space is 1-dimensional)
    PA = D @ D.T
    num = sum(np.trace(D.T @ T[i][a] @ TA[a] @ D) for a in range(8))
    den = sum(np.trace(D.T @ TA[a] @ TA[a] @ D) for a in range(8))
    kappa = np.real(num/den)
    res = []
    for j1, j2 in itertools.permutations(range(nA, nA + len(brem)), 2):
        if j1 > j2:
            continue
        X1, X2 = dot(T[i], T[j1]), dot(T[i], T[j2])
        c = X1 @ X2 - X2 @ X1
        Mred = D.T @ c @ D
        nrm = np.linalg.norm(Mred, 2) if D.shape[1] else 0.0
        anti = np.max(np.abs(Mred + Mred.T)) if D.shape[1] else 0.0
        realpart = np.max(np.abs(Mred.imag)) if D.shape[1] else 0.0
        # (D1) on random complex states in the DY space
        others = [k for k in range(nA, nA + len(brem)) if k not in (j1, j2)]
        Ob = [1j*sum(fabc[a, b, cc]*T[j1][a] @ T[j2][b] for a in range(8) for b in range(8) if fabc[a, b, cc] != 0)
              for cc in range(8)]
        Sk = [sum(T[k][cc] for k in others) if others else 0*T[0][cc] for cc in range(8)]
        maxdev = 0.0; maxval = 0.0
        for trial in range(4):
            psi = D @ (rng.normal(size=D.shape[1]) + 1j*rng.normal(size=D.shape[1]))
            psi /= np.linalg.norm(psi)
            lhs = psi.conj() @ c @ psi
            rhs = -kappa*sum(psi.conj() @ Ob[cc] @ Sk[cc] @ psi for cc in range(8))
            maxdev = max(maxdev, abs(lhs - rhs)); maxval = max(maxval, abs(lhs))
            # (D2) real psi
        psir = D @ rng.normal(size=D.shape[1]); psir /= np.linalg.norm(psir)
        zr = abs(psir @ c @ psir)
        res.append((j1, j2, nrm, anti, realpart, maxdev, maxval, zr, len(others)))
    print(f"[{name}] dim DY space = {D.shape[1]}, kappa_i = {kappa:.4f}")
    for (j1, j2, nrm, anti, rp, dev, mv, zr, nothers) in res:
        print(f"    (j1,j2)=({j1},{j2}) [#further B-rem partons={nothers}]: ||P[X1,X2]P||={nrm:.4f}; "
              f"P[X1,X2]P real antisym: imag {rp:.1e}, sym part {anti:.1e}; (D1) |lhs-rhs| max {dev:.1e} "
              f"(|lhs| up to {mv:.3f}); real psi -> {zr:.1e}")
        if nothers == 0 and nrm > 1e-9:
            allok = False
        if zr > 1e-9 or rp > 1e-9 or anti > 1e-9:
            allok = False
print("ALL PASS" if allok else "SOME CHECK FAILED")
