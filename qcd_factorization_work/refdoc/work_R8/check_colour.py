"""R8 checks: colour algebra of Example E.38, Lemma E.48, Remark E.49 (refdoc pp. 203-204, 217-218).

Checks
 C1  ladder colour factor  sum_ab (T_A^b T_A^a)(T_B^b T_B^a) = X^2
 C2  crossed colour factor sum_ab (T_A^b T_A^a)(T_B^a T_B^b) = X^2 + C_A/2 X
 C3  sum_ab {T^a,T^b}{T'^a,T'^b} = 4X^2 + C_A X        (proof of Lemma E.48(d))
 C4  sum_ab [T^a,T^b][T'^a,T'^b] = -C_A X              (Remark E.49(2): "propto C_A X")
 C5  (E.36): M2 + M2^dag + M1^dag M1 = -(1/2) C_A chi^2 Re(p_opp) X  for complex p_opp
 C6  (E.51): independent symmetric cut-offs (four orderings, weight 1/4) -> residual -(1/4) C_A chi^2 X
 C7  common ordering (Lemma E.48(c)) with two A and two B bystanders and different time profiles:
     (1+A1+A2)^dag (1+A1+A2) = 1 + O(chi^3)   (unitarity of the T-exponential at O(chi^2))
 C8  value of the residual on a colour-singlet q qbar pair: X = -C_F, residual = +C_A C_F chi^2/4
Representations: F x F, F x Fbar, F x A, A x A for SU(2), SU(3), SU(4).
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np

def gellmann(N):
    """Hermitian generators of SU(N) in the fundamental, Tr(t^a t^b) = delta/2."""
    gens = []
    for i in range(N):
        for j in range(i + 1, N):
            m = np.zeros((N, N), complex); m[i, j] = m[j, i] = 0.5; gens.append(m)
            m = np.zeros((N, N), complex); m[i, j] = -0.5j; m[j, i] = 0.5j; gens.append(m)
    for k in range(1, N):
        m = np.zeros((N, N), complex)
        for i in range(k):
            m[i, i] = 1.0
        m[k, k] = -k
        m *= 1.0 / np.sqrt(2 * k * (k + 1))
        gens.append(m)
    return gens

def structure_constants(t):
    n = len(t)
    f = np.zeros((n, n, n))
    for a in range(n):
        for b in range(n):
            comm = t[a] @ t[b] - t[b] @ t[a]
            for c in range(n):
                # [t^a,t^b] = i f^{abc} t^c ; Tr(t^c t^d) = delta/2
                f[a, b, c] = np.real(-2j * np.trace(comm @ t[c]))
    return f

def adjoint(f):
    n = f.shape[0]
    return [(-1j) * f[a] for a in range(n)]  # (T^a)_{bc} = -i f^{abc}

def kron_ops(TA, TB):
    dA, dB = TA[0].shape[0], TB[0].shape[0]
    IA, IB = np.eye(dA), np.eye(dB)
    A = [np.kron(x, IB) for x in TA]
    B = [np.kron(IA, y) for y in TB]
    return A, B

def run(N):
    t = gellmann(N)
    f = structure_constants(t)
    CA = N
    CF = (N * N - 1) / (2 * N)
    tbar = [-(x.T) for x in t]
    Tadj = adjoint(f)
    # sanity: algebra in each rep
    for rep, name in [(t, 'F'), (tbar, 'Fbar'), (Tadj, 'A')]:
        for a in range(len(t)):
            for b in range(len(t)):
                lhs = rep[a] @ rep[b] - rep[b] @ rep[a]
                rhs = 1j * sum(f[a, b, c] * rep[c] for c in range(len(t)))
                assert np.allclose(lhs, rhs), (N, name)
    reps = {'FxF': (t, t), 'FxFbar': (t, tbar), 'FxA': (t, Tadj), 'AxA': (Tadj, Tadj)}
    ok = True
    for name, (TA0, TB0) in reps.items():
        A, B = kron_ops(TA0, TB0)
        n = len(A)
        X = sum(A[a] @ B[a] for a in range(n))
        X2 = X @ X
        ladder = sum(A[b] @ A[a] @ B[b] @ B[a] for a in range(n) for b in range(n))
        crossed = sum(A[b] @ A[a] @ B[a] @ B[b] for a in range(n) for b in range(n))
        anti = sum((A[a] @ A[b] + A[b] @ A[a]) @ (B[a] @ B[b] + B[b] @ B[a]) for a in range(n) for b in range(n))
        comm = sum((A[a] @ A[b] - A[b] @ A[a]) @ (B[a] @ B[b] - B[b] @ B[a]) for a in range(n) for b in range(n))
        c1 = np.allclose(ladder, X2)
        c2 = np.allclose(crossed, X2 + 0.5 * CA * X)
        c3 = np.allclose(anti, 4 * X2 + CA * X)
        c4 = np.allclose(comm, -CA * X)
        # C5: (E.36) with random complex p_opp
        rng = np.random.default_rng(1)
        chi = 0.37
        okc5 = True
        for _ in range(3):
            p = complex(rng.normal(), rng.normal())
            M1 = -1j * chi * X
            M2 = ((-1j * chi) ** 2 / 2) * (X2 + p * 0.5 * CA * X)
            M2d = ((-1j * chi) ** 2 / 2).conjugate() * (X2 + np.conj(p) * 0.5 * CA * X)  # X hermitian
            lhs = M2 + M2d + M1.conj().T @ M1
            rhs = -0.5 * CA * chi ** 2 * p.real * X
            okc5 &= np.allclose(lhs, rhs)
            # also check M2d really is the hermitian conjugate of M2
            okc5 &= np.allclose(M2d, M2.conj().T)
        # C6: four orderings each weight 1/4 (Lemma E.48(d))
        A2 = ((-1j * chi) ** 2 / 2) * 0.25 * anti
        A1 = -1j * chi * X
        res = A1.conj().T @ A1 + A2 + A2.conj().T
        c6 = np.allclose(res, -0.25 * CA * chi ** 2 * X)
        ok_rep = c1 and c2 and c3 and c4 and okc5 and c6
        ok &= ok_rep
        print(f"SU({N}) {name:7s}: C1 {c1} C2 {c2} C3 {c3} C4 {c4} C5 {okc5} C6 {c6}")
    # C8: colour-singlet q qbar: X = -C_F on the singlet
    A, B = kron_ops(t, tbar)
    n = len(A)
    X = sum(A[a] @ B[a] for a in range(n))
    singlet = np.eye(N).reshape(N * N) / np.sqrt(N)  # delta_{ij}/sqrt(N) (q in F, qbar in Fbar with T=-t^T)
    xval = np.vdot(singlet, X @ singlet).real
    c8 = np.isclose(xval, -CF)
    resval = -0.25 * CA * 1.0 * xval
    print(f"SU({N}) singlet q qbar: <X> = {xval:.6f} (-C_F = {-CF:.6f}) -> {c8}; residual (chi=1) = {resval:.6f} = C_A C_F/4 = {CA*CF/4:.6f}")
    ok &= c8
    return ok

def common_ordering_unitarity(N=3):
    """C7: two A bystanders (F, F) and two B bystanders (Fbar, F); common ordering with pair-dependent
    time profiles h_ij(t); build A1, A2 from (E.50) with w = P(time order) and check unitarity at O(chi^2)."""
    t = gellmann(N)
    tbar = [-(x.T) for x in t]
    n = len(t)
    d = N
    I = np.eye(d)
    def op(pos, gen):
        mats = [I, I, I, I]
        mats[pos] = gen
        out = mats[0]
        for m in mats[1:]:
            out = np.kron(out, m)
        return out
    TA = [[op(0, t[a]) for a in range(n)], [op(1, t[a]) for a in range(n)]]
    TB = [[op(2, tbar[a]) for a in range(n)], [op(3, t[a]) for a in range(n)]]
    rng = np.random.default_rng(7)
    chi = {(i, j): rng.normal() for i in range(2) for j in range(2)}
    # exponential time profiles h_ij(t) = r_ij exp(-r_ij t), t>0 (normalised); P(t_e < t_e') analytic
    r = {(i, j): rng.uniform(0.5, 3.0) for i in range(2) for j in range(2)}
    pairs = list(chi.keys())
    dim = d ** 4
    eps = 0.05
    A1 = sum(-1j * eps * chi[p] * sum(TA[p[0]][a] @ TB[p[1]][a] for a in range(n)) for p in pairs)
    # A2 = (-i)^2/2! sum_{p,q} chi_p chi_q [ P(t_q > t_p) V_q V_p + P(t_p > t_q) V_p V_q ]
    V = {p: sum(TA[p[0]][a] @ TB[p[1]][a] for a in range(n)) for p in pairs}
    A2 = np.zeros((dim, dim), complex)
    for p in pairs:
        for q in pairs:
            # P(t_q > t_p) for independent exponentials with rates r_p, r_q
            P_qlater = r[p] / (r[p] + r[q])
            A2 += ((-1j * eps) ** 2 / 2) * chi[p] * chi[q] * (P_qlater * V[q] @ V[p] + (1 - P_qlater) * V[p] @ V[q])
    U2 = np.eye(dim) + A1 + A2
    dev = U2.conj().T @ U2 - np.eye(dim)
    # O(eps^2) part must vanish; the remainder is O(eps^3)
    o2 = A1.conj().T @ A1 + A2 + A2.conj().T
    c7 = np.allclose(o2, 0, atol=1e-12)
    print(f"C7 common ordering, 2x2 bystanders, SU({N}): O(chi^2) unitarity defect max = {np.abs(o2).max():.2e} -> {c7}")
    # contrast: independent orderings (weights 1/4) with the same configuration
    A2i = np.zeros((dim, dim), complex)
    for p in pairs:
        for q in pairs:
            for a in range(n):
                for b in range(n):
                    pass
    # independent orderings: (1/2)(-i eps)^2 sum_{p,q} chi_p chi_q (1/4){V^A}{V^B} structure
    for p in pairs:
        for q in pairs:
            Aside = [[0.5 * (TA[p[0]][a] @ TA[q[0]][b] + TA[q[0]][b] @ TA[p[0]][a]) for b in range(n)] for a in range(n)]
            Bside = [[0.5 * (TB[p[1]][a] @ TB[q[1]][b] + TB[q[1]][b] @ TB[p[1]][a]) for b in range(n)] for a in range(n)]
            A2i += ((-1j * eps) ** 2 / 2) * chi[p] * chi[q] * sum(Aside[a][b] @ Bside[a][b] for a in range(n) for b in range(n))
    o2i = A1.conj().T @ A1 + A2i + A2i.conj().T
    print(f"     independent symmetric orderings, same configuration: O(chi^2) defect max = {np.abs(o2i).max():.2e} (non-zero expected)")
    return c7

if __name__ == '__main__':
    allok = True
    for N in (2, 3, 4):
        allok &= run(N)
    allok &= common_ordering_unitarity(3)
    print('ALL PASS' if allok else 'SOME FAIL')
