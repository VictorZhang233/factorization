# X1 fix round 1 -- independent colour checks for L4(d) / T3(e) (half-coincident residual colour factor).
#
# Residual colour operator: [X1, X2] = i f^{abc} T^c_i T^a_{j1} T^b_{j2},  X_e = T_i . T_{j_e}
# (i in the remnant of hadron A, j1 != j2 in the remnant of hadron B).
#
# Claims checked (all numerically, SU(3)):
#  (R)  Real structure: in a common real weight basis of 3, 3bar, 8 one has (T^a)^* = s_a T^a with the SAME
#       signs s_a for every irrep; hence every X_e is real symmetric, [X1,X2] is real antisymmetric, and
#       <psi|[X1,X2]|psi> = 0 for every real psi (any real colour density matrix).
#  (I)  Operator identity  f^{abc} T^a_{j1} T^b_{j2} (T^c_{j1} + T^c_{j2}) = 0  for j1 != j2 in any irreps.
#  (DY) For Drell-Yan remnant states psi (hadron A = active quark + A-rem, hadron B = active antiquark + B-rem,
#       q qbar -> colour-singlet gamma*), <psi|[X1,X2]|psi> = 0 for ALL psi whenever B-rem = {j1, j2}
#       (the hadron containing j1, j2 has no further remnant parton), whatever A-rem is.
#       Non-zero values need both a further B-remnant parton and complex relative phases.
#  (N)  Basis-independent operator norms ||P [X1,X2] P|| on the DY remnant spaces and on the full singlet
#       spaces of the four-parton configurations quoted in the original report.
# Singlet spaces are computed inside the zero-weight subspace (C_tot restricted there), which avoids the
# 4096x4096 complex eigh that crashed scripts/check_halfcoinc_singlets.py.
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np

rng = np.random.default_rng(20261011)
ok_all = True
def check(name, cond):
    global ok_all
    print(("PASS " if cond else "FAIL ") + name, flush=True)
    ok_all = ok_all and bool(cond)

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

for nm, R in reps.items():
    alg = all(np.allclose(R[a] @ R[b] - R[b] @ R[a], 1j*sum(f[a, b, c]*R[c] for c in range(8)))
              for a in range(8) for b in range(8))
    real = all(np.allclose(R[a].conj(), s[a]*R[a]) for a in range(8))
    cas = sum(R[a] @ R[a] for a in range(8))
    cval = {'3': 4/3, '3b': 4/3, '8': 3.0}[nm]
    cartan = np.allclose(R[2], np.diag(np.diag(R[2]))) and np.allclose(R[7], np.diag(np.diag(R[7])))
    check(f"rep {nm:2s}: Lie algebra, Casimir={cval:.4f}, real structure (T^a)^*=s_a T^a, Cartan diagonal",
          alg and np.allclose(cas, cval*np.eye(len(cas))) and real and cartan)
check("signs: s_a s_b s_c = -1 for every nonzero f^{abc}",
      all(s[a]*s[b]*s[c] == -1 for a in range(8) for b in range(8) for c in range(8) if abs(f[a, b, c]) > 1e-12))

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

# ---------- (I) operator identity f T_{j1} T_{j2} (T_{j1}+T_{j2}) = 0
for pair in (('3', '3'), ('3', '3b'), ('8', '3'), ('8', '8'), ('3b', '8')):
    Ts, D = embed(pair)
    op = sum(f[a, b, c]*Ts[0][a] @ Ts[1][b] @ (Ts[0][c] + Ts[1][c])
             for a in range(8) for b in range(8) for c in range(8) if abs(f[a, b, c]) > 1e-12)
    check(f"(I) f^abc T^a_j1 T^b_j2 (T^c_j1 + T^c_j2) = 0 for (j1,j2) in {pair}", np.allclose(op, 0))

# ---------- (R) X_e real symmetric in the product basis
Ts, D = embed(('3', '3b', '8'))
X1 = X(Ts[0], Ts[1]); X2 = X(Ts[0], Ts[2]); K = X1 @ X2 - X2 @ X1
check("(R) X1, X2 real symmetric and [X1,X2] real antisymmetric in the product basis (i,j1,j2)=(3,3b,8)",
      np.allclose(X1.imag, 0) and np.allclose(X1, X1.T) and np.allclose(X2.imag, 0) and np.allclose(K.imag, 0)
      and np.allclose(K, -K.T))
Fop = sum(f[a, b, c]*Ts[0][c] @ Ts[1][a] @ Ts[2][b] for a in range(8) for b in range(8) for c in range(8)
          if abs(f[a, b, c]) > 1e-12)
check("[X1,X2] = i f^{abc} T^c_i T^a_j1 T^b_j2", np.allclose(K, 1j*Fop))

# ---------- (DY) Drell-Yan remnant states
def dy_space(Arem, Brem):
    """DY remnant states: hadron A singlet of (q=3) x Arem, hadron B singlet of (qbar=3b) x Brem,
    q qbar contracted into the colour-singlet gamma* vertex. Returns orthonormal real basis of the span
    in V(Arem) x V(Brem), plus the embedded generators of Arem+Brem."""
    SA, _ = singlets(('3',) + Arem); SB, _ = singlets(('3b',) + Brem)
    dA = SA.shape[0]//3; dB = SB.shape[0]//3
    vecs = []
    for m in range(SA.shape[1]):
        PA = SA[:, m].reshape(3, dA)
        for n in range(SB.shape[1]):
            PB = SB[:, n].reshape(3, dB)
            psi = sum(np.kron(PA[c], PB[c]) for c in range(3))      # sum_c |c>_q |cbar>_qbar contracted
            vecs.append(psi)
    M = np.array(vecs).T
    U, sv, _ = np.linalg.svd(M, full_matrices=False)
    Psi = U[:, sv > 1e-10*sv[0]]
    Ts, D = embed(Arem + Brem)
    tot = sum(Ts)
    assert max(np.max(np.abs(tot[a] @ Psi)) for a in range(8)) < 1e-9     # remnant state is a colour singlet
    return Psi, Ts

def analyse_dy(Arem, Brem, tag):
    Psi, Ts = dy_space(Arem, Brem)
    nA = len(Arem)
    Ti, Tj1, Tj2 = Ts[0], Ts[nA], Ts[nA + 1]
    Kc = X(Ti, Tj1) @ X(Ti, Tj2) - X(Ti, Tj2) @ X(Ti, Tj1)
    M = Psi.T @ Kc @ Psi
    assert np.allclose(M.imag, 0) and np.allclose(M, -M.T)
    norm = np.max(np.abs(np.linalg.eigvals(M))) if M.size else 0.0
    vals_c = []
    for _ in range(4):
        c = rng.normal(size=Psi.shape[1]) + 1j*rng.normal(size=Psi.shape[1]); c /= np.linalg.norm(c)
        psi = Psi @ c
        vals_c.append(psi.conj() @ Kc @ psi)
    c = rng.normal(size=Psi.shape[1]); c /= np.linalg.norm(c)
    psir = Psi @ c
    val_r = psir @ Kc @ psir
    # reviewer-1 formula with the B-remnant spectators k != j1, j2:  <[X1,X2]> = - <K_i x i f T_j1 T_j2 sum_k T_k>;
    # for dim(mult. space of 3bar in Arem) = 1, K_i = kappa_i (scalar) obtained from <T_i . T_Arem>/C_F
    others = [Ts[nA + k] for k in range(2, len(Brem))]
    rhs_vals = None
    SA, _ = singlets(('3',) + Arem)
    if SA.shape[1] == 1:
        TotA = sum(Ts[p] for p in range(nA))
        psi = Psi @ (rng.normal(size=Psi.shape[1]) + 1j*rng.normal(size=Psi.shape[1])); psi /= np.linalg.norm(psi)
        kappa = np.real(psi.conj() @ X(Ti, TotA) @ psi)/(4/3)
        if others:
            Op = sum(f[a, b, c]*Tj1[a] @ Tj2[b] @ sum(o[c] for o in others)
                     for a in range(8) for b in range(8) for c in range(8) if abs(f[a, b, c]) > 1e-12)
            rhs = -kappa*(psi.conj() @ (1j*Op) @ psi)
        else:
            rhs = 0.0
        lhs = psi.conj() @ Kc @ psi
        rhs_vals = (lhs, rhs, kappa)
    print(f"[{tag}] A-rem={Arem} B-rem={Brem}: dim DY space={Psi.shape[1]}, ||P[X1,X2]P||={norm:.6f}, "
          f"real psi: {abs(val_r):.1e}, complex psi: " + ", ".join(f"{v.imag:+.4f}i" for v in vals_c)
          + (f";  W-E check lhs={rhs_vals[0].imag:+.6f}i rhs={np.imag(rhs_vals[1]):+.6f}i (kappa_i={rhs_vals[2]:.4f})"
             if rhs_vals else ""), flush=True)
    return norm, abs(val_r), rhs_vals

cases = [
    (('3b',), ('3b', '3b'), 'meson A (q qbar) + antibaryon B, B-rem = {j1,j2}'),
    (('3', '3'), ('3b', '3b'), 'valence p pbar, B-rem = {j1,j2}'),
    (('3', '3', '8'), ('3b', '3b'), 'A-rem = q q g, B-rem = {j1,j2}'),
    (('3b', '8'), ('3b', '3b'), 'A-rem = qbar g (meson with a gluon), B-rem = {j1,j2}'),
    (('3b',), ('3b', '3b', '8'), 'A-rem = qbar, B-rem = qbar qbar g'),
    (('3', '3'), ('3b', '3b', '8'), 'A-rem = diquark, B-rem = qbar qbar g'),
    (('3', '3'), ('3b', '3', '3'), 'A-rem = diquark, B-rem = qbar q q'),
    (('3b',), ('3b', '3', '3'), 'A-rem = qbar, B-rem = qbar q q'),
]
for Arem, Brem, tag in cases:
    norm, vr, rv = analyse_dy(Arem, Brem, tag)
    check(f"(R) real DY state gives 0  [{tag}]", vr < 1e-12)
    if len(Brem) == 2:
        check(f"(DY) B-rem = {{j1,j2}}: [X1,X2] vanishes on the whole DY space  [{tag}]", norm < 1e-12)
    if rv is not None:
        check(f"(W-E) <[X1,X2]> = -kappa_i <i f T_j1 T_j2 sum_(k in B-rem minus j1,j2) T_k>  [{tag}]",
              abs(rv[0] - rv[1]) < 1e-10)

# ---------- (N) the four-parton configurations quoted in the original L4(d): full singlet space norms and
# their DY readings (passive parton in A-rem or in B-rem)
for lab in (('3b', '3b', '3b', '8'), ('3', '3b', '3b', '3'), ('3b', '3', '3b', '3')):
    S, Ts = singlets(lab)
    Kc = X(Ts[0], Ts[1]) @ X(Ts[0], Ts[2]) - X(Ts[0], Ts[2]) @ X(Ts[0], Ts[1])
    M = S.T @ Kc @ S
    nrm = np.max(np.abs(np.linalg.eigvals(M)))
    print(f"(N) (i,j1,j2,passive)={lab}: #singlets={S.shape[1]}, basis-dependent max|M_kl|={np.max(np.abs(M)):.4f}, "
          f"operator norm={nrm:.4f}", flush=True)
print("ALL PASS" if ok_all else "SOME CHECK FAILED")
