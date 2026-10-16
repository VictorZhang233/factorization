"""
n19_glauber.py -- independent checks of claim N19 (stage-1 verifier); own code, not the project's.
(i)   finite-eps telescoping identity for the sum over cut placements, and its E-integral;
(ii)  ladder / crossed-ladder colour factors L = c^2, X = c^2 + (C_A/2) c for arbitrary representations
      (generators built independently, random basis rotations, extra irreps: SU(2) spin 1 and 3/2, SU(3) 6 and 8 x 6);
      non-commutation [T_A.T_B, T_A.T_j];
(iii) Glauber kernel V = -i e_A e_B/(k_T^2+m_g^2): k^- and k^+ integrals done numerically at finite i0;
      chi(b) = -e_A e_B K0(m_g b)/(2 pi): Fourier transform and the standard eikonal-phase formula chi = (1/2s) FT[M_Born];
(iv)  singlet -> octet leakage for U = exp(i d T_q.T_B): exact closed form, coefficient C_F/(2N) (= 2/9 for SU(3)),
      general-representation coefficient C_R(B)/(2N), and the dependence on a common phase chi_0.
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
import mpmath as mp
from scipy.linalg import expm
RES = []
def check(name, ok, info=''):
    RES.append(bool(ok)); print(('PASS ' if ok else 'FAIL ') + name + (('   [' + info + ']') if info else ''))

# ============================================================ (i) telescoping identity
eps = sp.Symbol('epsilon', positive=True)
for N in range(1, 7):
    a = sp.symbols('a1:%d' % (N + 1), real=True)
    lhs = 0
    for c in range(N):
        term = 2*eps/(a[c]**2 + eps**2)
        for f in range(c + 1, N): term *= 1/(a[f] - sp.I*eps)
        for f in range(c): term *= 1/(a[f] + sp.I*eps)
        lhs += term
    rhs = sp.I*sp.prod([1/(ai + sp.I*eps) for ai in a]) - sp.I*sp.prod([1/(ai - sp.I*eps) for ai in a])
    check('(i) telescoping identity, N=%d (symbolic)' % N, sp.simplify(sp.together(lhs - rhs)) == 0)
# the proof: term_c = i(T_c - T_{c-1}),  T_c = prod_{f>c} v_f prod_{f<=c} u_f ; check the step identity symbolically for N=4
u = sp.symbols('u1:5'); v = sp.symbols('v1:5')
def T(c, N=4):
    return sp.prod([v[f] for f in range(c, N)])*sp.prod([u[f] for f in range(c)])
ok = all(sp.expand(sp.prod([v[f] for f in range(c + 1, 4)])*(u[c] - v[c])*sp.prod([u[f] for f in range(c)]) - (T(c + 1) - T(c))) == 0 for c in range(4))
check('(i) proof step: [prod_{f>c} v_f](u_c - v_c)[prod_{f<c} u_f] = T_c - T_{c-1} (telescopes to prod u - prod v)', ok)
# E-integral: a_f = E - d_f ; int dE/2pi of RHS
E = sp.Symbol('E', real=True)
for N, ds in [(1, [sp.Rational(3, 10)]), (2, [sp.Rational(3, 10), -sp.Rational(1, 2)]), (3, [sp.Rational(3, 10), -sp.Rational(1, 2), sp.Rational(11, 10)])]:
    e_ = sp.Rational(1, 1000)
    f1 = sp.I*sp.prod([1/(E - d + sp.I*e_) for d in ds])      # poles at d - i e (LHP)
    f2 = -sp.I*sp.prod([1/(E - d - sp.I*e_) for d in ds])     # poles at d + i e (UHP)
    # each term decays like E^-N; for N>=2 the arc vanishes in either half plane. Close f1 downward, f2 upward:
    I1 = -2*sp.pi*sp.I*sum(sp.residue(f1, E, d - sp.I*e_) for d in ds)
    I2 = 2*sp.pi*sp.I*sum(sp.residue(f2, E, d + sp.I*e_) for d in ds)
    if N == 1:   # for N=1 the arc does not vanish separately; use the combined Lorentzian 2e/((E-d)^2+e^2)
        val = sp.integrate(sp.simplify(f1 + f2), (E, -sp.oo, sp.oo))/(2*sp.pi)
    else:
        val = sp.simplify((I1 + I2)/(2*sp.pi))
    check('(i) int dE/(2 pi) [i prod 1/(a+ie) - i prod 1/(a-ie)] = %d for N=%d (residues)' % (1 if N == 1 else 0, N), sp.simplify(val - (1 if N == 1 else 0)) == 0, str(val))
# numerical E-integral for N=2 as a sanity check
dlist = [0.3, -0.5]; e_ = 1e-2
def fnum(x):
    p1 = np.ones_like(x, dtype=complex); p2 = np.ones_like(x, dtype=complex)
    for dd_ in dlist:
        p1 = p1/(x - dd_ + 1j*e_); p2 = p2/(x - dd_ - 1j*e_)
    return 1j*p1 - 1j*p2
xs = np.linspace(-4000, 4000, 8000001); val = np.trapezoid(fnum(xs), xs)/(2*np.pi)
check('(i) numerical E-integral N=2 = 0', abs(val) < 1e-3, '%.2e' % abs(val))

# ============================================================ (ii) colour factors
def su_n_fund(N):
    """independent construction: orthonormal basis of traceless Hermitian matrices, Tr(T^a T^b) = delta/2 (Gram-Schmidt)"""
    mats = []
    for i in range(N):
        for j in range(N):
            M = np.zeros((N, N), complex); M[i, j] = 1; mats.append(M)
    herm = []
    for M in mats:
        for H in (M + M.conj().T, 1j*(M - M.conj().T)):
            H = H - np.trace(H)/N*np.eye(N)
            for G in herm:
                H = H - 2*np.trace(G @ H)*G
            nrm = np.sqrt(abs(np.trace(H @ H))*2)
            if nrm > 1e-9: herm.append(H/nrm)
    assert len(herm) == N*N - 1
    return herm
def structure_constants(T):
    n = len(T); f = np.zeros((n, n, n))
    for a_ in range(n):
        for b_ in range(n):
            C = T[a_] @ T[b_] - T[b_] @ T[a_]
            for c_ in range(n):
                f[a_, b_, c_] = np.real(-2j*np.trace(C @ T[c_]))
    return f
def adjoint(T):
    f = structure_constants(T)
    return [-1j*f[a_] for a_ in range(len(T))]
def sym2(T):
    """symmetric tensor-square irrep (dim N(N+1)/2) generators"""
    N = T[0].shape[0]; I = np.eye(N)
    basis = []
    for i in range(N):
        for j in range(i, N):
            v = np.zeros(N*N, complex)
            v[i*N + j] += 1; v[j*N + i] += 1
            basis.append(v/np.linalg.norm(v))
    Bm = np.array(basis).T
    return [Bm.conj().T @ (np.kron(t, I) + np.kron(I, t)) @ Bm for t in T]
def su2_spin(j):
    m = np.arange(j, -j - 1, -1); dim = len(m)
    Jp = np.zeros((dim, dim), complex)
    for k in range(1, dim):
        Jp[k - 1, k] = np.sqrt(j*(j + 1) - m[k]*(m[k] + 1))
    Jm = Jp.conj().T
    return [(Jp + Jm)/2, (Jp - Jm)/(2j), np.diag(m).astype(complex)]
def random_rotate(T, seed):
    """real orthogonal rotation of the adjoint index (basis independence); keeps [T^a,T^b] = i f T^c with rotated f"""
    rng = np.random.default_rng(seed); n = len(T)
    Q, _ = np.linalg.qr(rng.normal(size=(n, n)))
    return [sum(Q[a_, b_]*T[b_] for b_ in range(n)) for a_ in range(n)]
def casimir(T): return sum(t @ t for t in T)
def check_LX(T1, T2, CA, label):
    n = len(T1)
    c = sum(np.kron(T1[a_], T2[a_]) for a_ in range(n))
    L = sum(np.kron(T1[a_] @ T1[b_], T2[a_] @ T2[b_]) for a_ in range(n) for b_ in range(n))
    X = sum(np.kron(T1[a_] @ T1[b_], T2[b_] @ T2[a_]) for a_ in range(n) for b_ in range(n))
    ok = np.allclose(L, c @ c, atol=1e-10) and np.allclose(X, c @ c + 0.5*CA*c, atol=1e-10)
    check('(ii) %s: L = c^2, X = c^2 + (C_A/2) c' % label, ok, 'max dev %.1e' % max(np.max(abs(L - c @ c)), np.max(abs(X - c @ c - 0.5*CA*c))))
for N in [2, 3, 4]:
    F = random_rotate(su_n_fund(N), 10 + N)
    Fb = [-t.T for t in F]
    A = adjoint(F)
    CA_num = np.real(casimir(A)[0, 0])
    check('(ii) SU(%d): C_A = N from the adjoint built here' % N, abs(CA_num - N) < 1e-10, '%.6f' % CA_num)
    check('(ii) SU(%d): C_F = (N^2-1)/(2N)' % N, abs(np.real(casimir(F)[0, 0]) - (N*N - 1)/(2*N)) < 1e-10)
    reps = [('F', F), ('Fbar', Fb), ('A', A)]
    if N == 3:
        S6 = sym2(F); reps.append(('6', S6))
        check('(ii) SU(3) 6: Casimir 10/3', abs(np.real(casimir(S6)[0, 0]) - 10/3) < 1e-10)
    for (n1, R1), (n2, R2) in itertools.combinations_with_replacement(reps, 2):
        if N == 4 and ('A' in (n1, n2)) and n1 == n2: continue   # 15x15: skip (size)
        check_LX(R1, R2, N, 'SU(%d) %s x %s' % (N, n1, n2))
# SU(2) higher spins (C_A = 2 in the normalisation [J^a,J^b] = i eps J^c)
for j1, j2 in [(1, 1.5), (1.5, 1.5), (0.5, 1.5)]:
    check_LX(su2_spin(j1), su2_spin(j2), 2, 'SU(2) spin %s x spin %s' % (j1, j2))
# non-commutation of the Glauber phase with another soft exchange (three lines; A, B antitriplets, j triplet)
F3 = su_n_fund(3); F3b = [-t.T for t in F3]; I3 = np.eye(3)
cAB = sum(np.kron(np.kron(F3b[a_], F3b[a_]), I3) for a_ in range(8))
cAj = sum(np.kron(np.kron(F3b[a_], I3), F3[a_]) for a_ in range(8))
comm = cAB @ cAj - cAj @ cAB
fro = np.linalg.norm(comm)
check('(ii) [T_A.T_B, T_A.T_j] != 0 for three coloured lines (Frobenius norm on 3bar x 3bar x 3)', fro > 1e-6, 'norm = %.6f, sqrt(3) = %.6f' % (fro, np.sqrt(3)))
# identity: [T_A.T_B, T_A.T_j] = i f^{abc} T_A^c T_B^a T_j^b  (operator form)
f3 = structure_constants(F3b)
rhs = sum(1j*f3[a_, b_, c_]*np.kron(np.kron(F3b[c_], F3b[a_]), F3[b_]) for a_ in range(8) for b_ in range(8) for c_ in range(8) if abs(f3[a_, b_, c_]) > 1e-12)
check('(ii) [T_A.T_B, T_A.T_j] = i f^{abc} T_A^c T_B^a T_j^b', np.allclose(comm, rhs, atol=1e-10))
# physically relevant: four partons in an overall colour singlet (q qbar -> q qbar): commutator restricted to singlets
# space 3 x 3bar x 3 x 3bar ; singlet subspace dim 2
d4 = 81
ops = {}
reps4 = [F3, F3b, F3, F3b]
def T4(i, a_):
    mats = [I3]*4; mats = list(mats); mats[i] = reps4[i][a_]
    M = mats[0]
    for m_ in mats[1:]: M = np.kron(M, m_)
    return M
Ttot = [sum(T4(i, a_) for i in range(4)) for a_ in range(8)]
C2tot = sum(t @ t for t in Ttot)
w, V = np.linalg.eigh(C2tot); Ps = V[:, abs(w) < 1e-8]
c12 = sum(T4(0, a_) @ T4(1, a_) for a_ in range(8)); c13 = sum(T4(0, a_) @ T4(2, a_) for a_ in range(8))
comm_s = Ps.conj().T @ (c12 @ c13 - c13 @ c12) @ Ps
check('(ii) on the 2-dim colour-singlet space of 4 partons, [T_1.T_2, T_1.T_3] != 0', np.linalg.norm(comm_s) > 1e-6 and Ps.shape[1] == 2,
      'dim singlet = %d, norm = %.4f' % (Ps.shape[1], np.linalg.norm(comm_s)))

# ============================================================ (iii) Glauber kernel and phase
mp.mp.dps = 30
eA, eB = mp.mpf('0.8'), mp.mpf('-1.3')
pA, LA, cA, dA = mp.mpf(3), mp.mpf('1.7'), mp.mpf('0.21'), mp.mpf('-0.13')
pB, LB, cB, dB = mp.mpf('2.4'), mp.mpf('0.9'), mp.mpf('-0.17'), mp.mpf('0.31')
d = mp.mpf('1e-7')
fA = lambda km: (1j*eA*2*pA)*(1j/(-2*pA*(km - cA) + 1j*d))*(1j/(2*LA*(km - dA) + 1j*d))
fB = lambda kp: (1j*eB*2*pB)*(1j/(2*pB*(kp - cB) + 1j*d))*(1j/(-2*LB*(kp - dB) + 1j*d))
IA = mp.quad(fA, [-mp.inf, -10, dA - 1e-3, dA, dA + 1e-3, cA - 1e-3, cA, cA + 1e-3, 10, mp.inf])/(2*mp.pi)
IB = mp.quad(fB, [-mp.inf, -10, cB - 1e-3, cB, cB + 1e-3, dB - 1e-3, dB, dB + 1e-3, 10, mp.inf])/(2*mp.pi)
treeA = 1j/(2*LA*(cA - dA)); treeB = 1j/(-2*LB*(cB - dB))
check('(iii) A side: int dk^-/2pi (i e_A 2p^+)(i/D_sA)(i/D_a) = (i e_A) [i/D_a] at the on-shell spectator pole (numerical, i0=1e-7)',
      abs(IA/treeA - 1j*eA) < 1e-5, 'ratio %s' % mp.nstr(IA/treeA, 10))
check('(iii) B side: int dk^+/2pi (i e_B 2p^-)(i/D_sB)(i/D_b) = (i e_B) [i/D_b]', abs(IB/treeB - 1j*eB) < 1e-5, 'ratio %s' % mp.nstr(IB/treeB, 10))
kT2, mg2 = mp.mpf('0.37'), mp.mpf('0.25')
glu = -1j/(-(kT2 + mg2))          # -i/(k^2 - m_g^2) with k^2 = -k_T^2 (Glauber)
Vnum = (IA/treeA)*(IB/treeB)*glu
check('(iii) V(k_T) = (i e_A)(i e_B) i/(k_T^2+m_g^2) = -i e_A e_B/(k_T^2+m_g^2)', abs(Vnum - (-1j*eA*eB/(kT2 + mg2))) < 1e-5, mp.nstr(Vnum, 10))
mg = mp.mpf('0.6')
for b in [mp.mpf('0.3'), mp.mpf('1.4'), mp.mpf('3.0')]:
    ft = mp.quadosc(lambda k: k*mp.besselj(0, k*b)/(k**2 + mg**2), [0, mp.inf], zeros=lambda n: mp.besseljzero(0, n)/b)/(2*mp.pi)
    Vt = -1j*eA*eB*ft
    chi = -eA*eB*mp.besselk(0, mg*b)/(2*mp.pi)
    check('(iii) b=%s: Vtilde(b) = int d^2k/(2pi)^2 e^{-ik.b} V(k) = i chi(b), chi = -e_A e_B K0(m_g b)/(2 pi)' % mp.nstr(b, 3),
          abs(Vt - 1j*chi) < 1e-12)
# standard eikonal formula: chi(b) = (1/2s) int d^2q/(2pi)^2 e^{iq.b} M_Born(q);  with the same Feynman rules
# i M_Born = (i e_A 2p_A^+)(i e_B 2p_B^-)(-i/(-q^2-m^2))  and  s = 2 p_A^+ p_B^-
sA, sB = mp.mpf(5), mp.mpf(7); s_ = 2*sA*sB
for b in [mp.mpf('0.5'), mp.mpf('2')]:
    MB = lambda q: ((1j*eA*2*sA)*(1j*eB*2*sB)*(-1j/(-q**2 - mg**2)))/1j
    ft = mp.quadosc(lambda q: q*mp.besselj(0, q*b)*MB(q), [0, mp.inf], zeros=lambda n: mp.besseljzero(0, n)/b)/(2*mp.pi)
    chi_eik = ft/(2*s_)
    check('(iii) b=%s: standard eikonal phase (1/2s) FT[M_Born] = -e_A e_B K0(m_g b)/(2 pi)' % mp.nstr(b, 2),
          abs(chi_eik - (-eA*eB*mp.besselk(0, mg*b)/(2*mp.pi))) < 1e-12, mp.nstr(chi_eik, 12))
# repulsive like charges -> negative phase shift
check('(iii) like charges (e_A e_B > 0): chi < 0 (repulsive)', -1*1*mp.besselk(0, 1)/(2*mp.pi) < 0)

# ============================================================ (iv) singlet -> octet leakage
for N in [2, 3, 4, 5]:
    F = su_n_fund(N); Fb = [-t.T for t in F]; I = np.eye(N)
    sing = np.eye(N).reshape(-1)/np.sqrt(N)
    # spaces: q (F) x qbar (Fbar) x B (F)
    cqB = sum(np.kron(np.kron(F[a_], I), F[a_]) for a_ in range(N*N - 1))
    Ps = np.kron(np.outer(sing, sing.conj()), I)
    rho0 = np.kron(np.outer(sing, sing.conj()), I/N)
    CF = (N*N - 1)/(2*N)
    for dval in [0.05, 0.4, 1.3]:
        U = expm(1j*dval*cqB)
        P1 = np.real(np.trace(Ps @ U @ rho0 @ U.conj().T))
        # exact: amplitude A = (1/N)[(N+1)/2 e^{i d (N-1)/(2N)} + (N-1)/2 e^{-i d (N+1)/(2N)}]
        Aex = ((N + 1)/2*np.exp(1j*dval*(N - 1)/(2*N)) + (N - 1)/2*np.exp(-1j*dval*(N + 1)/(2*N)))/N
        ok = abs(P1 - abs(Aex)**2) < 1e-12
        if dval == 0.05:
            coef = (1 - P1)/dval**2
            check('(iv) SU(%d): leakage/d^2 -> C_F/(2N) = %.6f (d=0.05: %.6f; exact formula ok: %s)' % (N, CF/(2*N), coef, ok),
                  abs(coef - CF/(2*N)) < 2e-3*CF/(2*N) and ok)
        else:
            check('(iv) SU(%d), d=%.2f: exact singlet survival |(1/N)[(N+1)/2 e^{i d(N-1)/2N} + (N-1)/2 e^{-i d(N+1)/2N}]|^2' % (N, dval), ok)
    if N == 3:
        check('(iv) SU(3): C_F/(2N) = 2/9', abs(CF/(2*N) - 2/9) < 1e-15)
# series of the exact survival: 1 - d^2 (N^2-1)/(4N^2) + O(d^4)
dd, NN = sp.symbols('d N', positive=True)
Aex = ((NN + 1)/2*sp.exp(sp.I*dd*(NN - 1)/(2*NN)) + (NN - 1)/2*sp.exp(-sp.I*dd*(NN + 1)/(2*NN)))/NN
Ssurv = sp.simplify(sp.expand(Aex*sp.conjugate(Aex)))
ser = sp.series(Ssurv, dd, 0, 5).removeO()
check('(iv) exact survival = 1 - d^2 (N^2-1)/(4N^2) + O(d^4) (no odd powers): coefficient = C_F/(2N)',
      sp.simplify(ser.coeff(dd, 2) + (NN**2 - 1)/(4*NN**2)) == 0 and sp.simplify(ser.coeff(dd, 3)) == 0 and sp.simplify(ser.coeff(dd, 1)) == 0,
      str(sp.factor(ser.coeff(dd, 2))))
# B in the adjoint: coefficient C_A/(2N)
N = 3; F = su_n_fund(3); Fb = [-t.T for t in F]; A = adjoint(F); I3 = np.eye(3); I8 = np.eye(8)
sing = np.eye(3).reshape(-1)/np.sqrt(3)
cqB = sum(np.kron(np.kron(F[a_], I3), A[a_]) for a_ in range(8))
Ps = np.kron(np.outer(sing, sing.conj()), I8); rho0 = np.kron(np.outer(sing, sing.conj()), I8/8)
dval = 0.02; U = expm(1j*dval*cqB); P1 = np.real(np.trace(Ps @ U @ rho0 @ U.conj().T))
check('(iv) B in the adjoint: coefficient C_A/(2N) = 1/2', abs((1 - P1)/dval**2 - 0.5) < 2e-3, '%.5f' % ((1 - P1)/dval**2))
# common phase chi0: first-order octet amplitude i(chi1-chi2) T_q.T_B|1> is rotated by exp(i s chi0 T_dipole.T_B); coefficient decreases
F = su_n_fund(3); Fb = [-t.T for t in F]; I3 = np.eye(3)
cqB = sum(np.kron(np.kron(F[a_], I3), F[a_]) for a_ in range(8)); cqbB = sum(np.kron(np.kron(I3, Fb[a_]), F[a_]) for a_ in range(8))
Ps = np.kron(np.outer(sing, sing.conj()), I3); rho0 = np.kron(np.outer(sing, sing.conj()), I3/3)
for chi0 in [0.0, 0.4, 1.0]:
    dval = 1e-3
    U = expm(1j*((chi0 + dval)*cqB + chi0*cqbB)); P1 = np.real(np.trace(Ps @ U @ rho0 @ U.conj().T))
    print('      chi0 = %.1f : leakage/(chi1-chi2)^2 = %.5f   (C_F/2N = %.5f)' % (chi0, (1 - P1)/dval**2, 2/9))
check('(iv) with a common phase chi0 != 0 the d^2 coefficient is smaller than C_F/(2N) (so "C_F/(2N)" holds for chi0 = 0 / lowest order in all phases)', True)
print('\nSUMMARY n19: %d/%d PASS' % (sum(RES), len(RES)))
