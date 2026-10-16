# R-M20 (independent colour-algebra checks, verifier s1 v2)
# Checks of the statements of CdFR (JHEP 07 (2012) 026, Sec. 6.2) and FSS (JHEP 11 (2012) 066, Sec. 5):
#  A. f_abc T_i^a T_j^b T_k^c = -i [T_i.T_j, T_i.T_k]  (distinct partons; operator identity) and it is Hermitian.
#  B. CdFR (2partcorrcan):  Sp0^dag f_abc T_1^a T_2^b Sp0 = 0  for q->qg, g->gg, g->qqbar  (=> Delta_P^(2) drops out of
#     P^(2) for n = 4 partons).
#  C. CdFR (2partticharge): Sp0^dag T_i^a Sp0 = T_(i)P^a P0, with T_(g)q = C_A/(2C_F) T_q, T_(q)q = (1-C_A/(2C_F)) T_q,
#     T_(g)g = T_g/2, T_(q)g = (T_g + d_g)/2.
#  D. n = 5 (q g collinear, reduced q qbar q' qbar'):  Sp0^dag f T_2 T_3 T_4 Sp0 = (C_A/2C_F) f T_P T_3 T_4 P0 is a NON-zero
#     Hermitian operator on the reduced singlet space; in the real trace basis it is imaginary antisymmetric, so its
#     expectation value vanishes for relatively real colour vectors (FSS: pure-QCD trees) but not for complex ones
#     (CdFR general case; FSS: QCD+EW phases).
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np

# ---------------- SU(3) ----------------
lam = np.zeros((8, 3, 3), dtype=complex)
lam[0][[0, 1], [1, 0]] = 1
lam[1][0, 1], lam[1][1, 0] = -1j, 1j
lam[2][0, 0], lam[2][1, 1] = 1, -1
lam[3][[0, 2], [2, 0]] = 1
lam[4][0, 2], lam[4][2, 0] = -1j, 1j
lam[5][[1, 2], [2, 1]] = 1
lam[6][1, 2], lam[6][2, 1] = -1j, 1j
lam[7] = np.diag([1, 1, -2]) / np.sqrt(3)
t = lam / 2
f = np.zeros((8, 8, 8))
d = np.zeros((8, 8, 8))
for a, b, c in itertools.product(range(8), repeat=3):
    f[a, b, c] = (-2j * np.trace((t[a] @ t[b] - t[b] @ t[a]) @ t[c])).real
    d[a, b, c] = (2 * np.trace((t[a] @ t[b] + t[b] @ t[a]) @ t[c])).real
CF, CA = 4 / 3, 3.0
assert np.allclose(sum(t[a] @ t[a] for a in range(8)), CF * np.eye(3))
Tadj = np.array([-1j * f[a] for a in range(8)])          # (T_g^a)_{bc} = -i f_abc
assert np.allclose(sum(Tadj[a] @ Tadj[a] for a in range(8)), CA * np.eye(8))
dmat = np.array([d[:, a, :] for a in range(8)])          # (d^a)_{bc} = d_bac  (CdFR notation)

def gen(kind, a):
    return {'q': t[a], 'qb': -t[a].T, 'g': Tadj[a]}[kind]

def dims_of(kinds):
    return [3 if k in ('q', 'qb') else 8 for k in kinds]

def embed(op, pos, dims):
    out = np.array([[1.0 + 0j]])
    for i, dd in enumerate(dims):
        out = np.kron(out, op if i == pos else np.eye(dd))
    return out

def charges(kinds):
    dims = dims_of(kinds)
    return [[embed(gen(k, a), i, dims) for a in range(8)] for i, k in enumerate(kinds)]

def TT(T, i, j):
    return sum(T[i][a] @ T[j][a] for a in range(8))

def fTTT(T, i, j, k):
    return sum(f[a, b, c] * T[i][a] @ T[j][b] @ T[k][c]
               for a in range(8) for b in range(8) for c in range(8) if f[a, b, c] != 0)

# ---------------- A: identity and hermiticity (on the full tensor space) ----------------
kinds5 = ['q', 'g', 'qb', 'q', 'qb']      # partons 1..5 (all-outgoing labels); 1,2 = collinear pair (q,g)
T5 = charges(kinds5)
worstA = 0.0
for (i, j, k) in itertools.permutations(range(5), 3):
    F = fTTT(T5, i, j, k)
    comm = TT(T5, i, j) @ TT(T5, i, k) - TT(T5, i, k) @ TT(T5, i, j)
    worstA = max(worstA, np.abs(F + 1j * comm).max(), np.abs(F - F.conj().T).max())
print('A. max |fTTT + i[Ti.Tj,Ti.Tk]|, |fTTT - fTTT^dag| over 60 triples (full space, n=5):', worstA)

# ---------------- B, C: tree-level splitting matrices ----------------
def sp_qqg():      # P = q (index iP) -> 1 = q (i1), 2 = g (a2):  (t^{a2})_{i1 iP}
    S = np.zeros((3 * 8, 3), dtype=complex)
    for i1, a2, iP in itertools.product(range(3), range(8), range(3)):
        S[i1 * 8 + a2, iP] = t[a2][i1, iP]
    return S, ['q', 'g'], 'q'

def sp_ggg():      # P = g (aP) -> 1 = g (a1), 2 = g (a2):  f_{a1 a2 aP} (overall phase irrelevant)
    S = np.zeros((64, 8), dtype=complex)
    for a1, a2, aP in itertools.product(range(8), repeat=3):
        S[a1 * 8 + a2, aP] = f[a1, a2, aP]
    return S, ['g', 'g'], 'g'

def sp_gqq():      # P = g (aP) -> 1 = q (i1), 2 = qbar (j2):  (t^{aP})_{i1 j2}
    S = np.zeros((9, 8), dtype=complex)
    for i1, j2, aP in itertools.product(range(3), range(3), range(8)):
        S[i1 * 3 + j2, aP] = t[aP][i1, j2]
    return S, ['q', 'qb'], 'g'

for name, (S, ck, parent) in [('q->qg', sp_qqg()), ('g->gg', sp_ggg()), ('g->qqbar', sp_gqq())]:
    T2 = charges(ck)
    P0 = S.conj().T @ S
    norm = P0[0, 0].real
    assert np.allclose(P0, norm * np.eye(P0.shape[0]))
    # colour conservation in the splitting: (T1+T2) Sp = Sp T_P   (with T_P the parent charge in the same convention)
    cons = max(np.abs((T2[0][a] + T2[1][a]) @ S - S @ gen(parent, a)).max() for a in range(8))
    # B
    worstB = max(np.abs(S.conj().T @ sum(f[a, b, c] * T2[0][a] @ T2[1][b] for a in range(8) for b in range(8)) @ S).max()
                 for c in range(8))
    # C
    res = []
    for i in range(2):
        X = [S.conj().T @ T2[i][a] @ S / norm for a in range(8)]
        res.append(X)
    if name == 'q->qg':
        pred = [[(1 - CA / (2 * CF)) * t[a] for a in range(8)], [CA / (2 * CF) * t[a] for a in range(8)]]
    elif name == 'g->gg':
        pred = [[0.5 * Tadj[a] for a in range(8)], [0.5 * Tadj[a] for a in range(8)]]
    else:
        pred = [[0.5 * (Tadj[a] + dmat[a]) for a in range(8)], [0.5 * (Tadj[a] - dmat[a]) for a in range(8)]]
    worstC = max(np.abs(res[i][a] - pred[i][a]).max() for i in range(2) for a in range(8))
    # if the d-term sign/convention differs, report the alternative too
    alt = None
    if name == 'g->qqbar':
        predalt = [[0.5 * (Tadj[a] - dmat[a]) for a in range(8)], [0.5 * (Tadj[a] + dmat[a]) for a in range(8)]]
        alt = max(np.abs(res[i][a] - predalt[i][a]).max() for i in range(2) for a in range(8))
    print('%-9s P0 = %.4f*1 ; colour conservation err %.1e ; B: max|Sp^dag f T1 T2 Sp| = %.1e ; C: T_(i)P check err = %.1e%s'
          % (name, norm, cons, worstB, worstC, '' if alt is None else ' (with d -> -d: %.1e)' % alt))

# ---------------- D: n = 5 -> reduced n = 4 ----------------
S, ck, parent = sp_qqg()
kinds_red = ['q', 'qb', 'q', 'qb']        # reduced: P(q), 3(qb), 4(q), 5(qb)
Tr = charges(kinds_red)
dims_red = dims_of(kinds_red)
Dred = int(np.prod(dims_red))
# full 5-parton charges in the ordering (1,2 | 3,4,5); lift Sp to the full space: Sp_full = Sp (x) 1_{3,4,5}
Sfull = np.kron(S, np.eye(int(np.prod(dims_red[1:]))))
F234 = fTTT(T5, 1, 2, 3)                  # f T_2 T_3 T_4  (python indices 1,2,3 = partons 2,3,4)
lhs = Sfull.conj().T @ F234 @ Sfull
rhs = (CA / (2 * CF)) * CF * fTTT(Tr, 0, 1, 2)   # P0 = CF * 1 for q->qg
print('D. max|Sp^dag f T2 T3 T4 Sp - (C_A/2C_F) C_F f T_P T_3 T_4| =', np.abs(lhs - rhs).max())
# real trace basis of the reduced singlet space: c1 = delta_{P 3} delta_{4 5},  c2 = delta_{P 5} delta_{4 3}
e = np.eye(3)
c1 = np.einsum('ij,kl->ijkl', e, e).reshape(-1)
c2 = np.einsum('il,kj->ijkl', e, e).reshape(-1)
C = np.array([c1, c2]).T.astype(complex)
Ttot = [sum(Tr[i][a] for i in range(4)) for a in range(8)]
print('   singlet check max|sum_i T_i^a c| =', max(np.abs(Ttot[a] @ C).max() for a in range(8)))
G = C.conj().T @ C
w, V = np.linalg.eigh(G.real)
Ghalf_inv = V @ np.diag(w**-0.5) @ V.T                 # real symmetric
On = C @ Ghalf_inv                                    # orthonormal basis built with REAL coefficients
M_TT = [[On.conj().T @ TT(Tr, i, j) @ On for j in range(4)] for i in range(4)]
print('   max |Im T_i.T_j| in the real orthonormal basis =', max(np.abs(M_TT[i][j].imag).max() for i in range(4) for j in range(4) if i != j))
Fred = On.conj().T @ rhs @ On
print('   reduced operator (C_A/2) f T_P T_3 T_4 in that basis:\n', np.round(Fred, 6))
print('   Hermitian:', np.allclose(Fred, Fred.conj().T), '; purely imaginary antisymmetric:',
      np.allclose(Fred.real, 0) and np.allclose(Fred, -Fred.T), '; norm =', np.abs(Fred).max())
rng = np.random.default_rng(7)
mr = rng.normal(size=2)
mc = rng.normal(size=2) + 1j * rng.normal(size=2)
print('   <M|F|M>/|M|^2 for a real colour vector    =', (mr @ Fred @ mr / (mr @ mr)).real)
print('   <M|F|M>/|M|^2 for a complex colour vector =', (mc.conj() @ Fred @ mc / np.vdot(mc, mc)).real)
print('   with relative phase phi: <M|F|M> = 2 |m1 m2| sin(phi) * F12/i ->',
      [(np.array([1, np.exp(1j * ph)]).conj() @ Fred @ np.array([1, np.exp(1j * ph)])).real for ph in (0.0, np.pi / 2)])
