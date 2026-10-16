# N19 (stage-2 verifier): independent checks of the four c_glauber results.
# (i)  telescoping identity: exact polynomial identity (sympy, N<=6, cleared denominators) + induction step proved
#      symbolically for general N (recursion S_{N+1} = v_{N+1} S_N + i(u_{N+1}-v_{N+1}) prod_{f<=N} u_f);
#      E-integral by exact residues (sympy) for N=1..4.
# (ii) L=c^2, X=c^2+(C_A/2)c with EXACT matrices (sympy): SU(2) spins 1/2..2, SU(3) 3, 3bar, 8 (from exact f^{abc}), 6.
# (iii) V(k_T) from exact residues (sympy), chi(b) by Hankel transform (mpmath), sign by the eikonal formula.
# (iv) leakage: exact closed form 1-P = (N^2-1)/N^2 sin^2(d/2) (projector argument) vs explicit matrices;
#      common-phase dependence (sinc^2 average).
import sys, os, itertools, random
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
import numpy as np
from scipy.linalg import expm

res = []
def check(name, cond, info=''):
    res.append(bool(cond)); print(('PASS ' if cond else 'FAIL ') + name + (('   [' + info + ']') if info else ''))

# ------------------------------------------------------------------ (i)
I = sp.I
for Nn in range(1, 6):
    a = sp.symbols('a1:%d' % (Nn+1), real=True); e = sp.symbols('epsilon', positive=True)
    u = [1/(ai + I*e) for ai in a]; v = [1/(ai - I*e) for ai in a]
    lhs = 0
    for c in range(Nn):
        term = 2*e/(a[c]**2 + e**2)
        for f in range(c+1, Nn): term *= v[f]
        for f in range(c): term *= u[f]
        lhs += term
    rhs = I*sp.prod(u) - I*sp.prod(v)
    den = sp.prod([(ai**2 + e**2) for ai in a])
    diff = sp.expand(sp.cancel((lhs - rhs)*den))
    check('telescoping identity exact for N=%d (polynomial identity after clearing denominators)' % Nn, diff == 0)
    # opposite overall sign fails
    if Nn == 1:
        check('opposite overall sign (as in Collins 2011 eq. (14.30) per stage 1) fails for N=1', sp.simplify(lhs + rhs) != 0)
# induction step for general N: with S_N = sum_{c<=N} [prod_{c<f<=N} v_f] i(u_c-v_c) [prod_{f<c} u_f],
# S_{N+1} = v_{N+1} S_N + i(u_{N+1}-v_{N+1}) U_N  (U_N = prod_{f<=N} u_f, V_N = prod v_f).  If S_N = i(U_N - V_N) then
# S_{N+1} = i v (U_N - V_N) + i(u - v) U_N = i(u U_N - v V_N) = i(U_{N+1} - V_{N+1}).
U, V, uu, vv = sp.symbols('U V u v')
step = sp.expand(vv*I*(U - V) + I*(uu - vv)*U - I*(uu*U - vv*V))
check('induction step S_{N+1} = v_{N+1} S_N + i(u_{N+1}-v_{N+1}) U_N closes the identity for all N', step == 0)
# E integral of RHS for a_f = E - d_f by residues (close in the UHP: poles of 1/(E-d+i e) are in the LHP)
E = sp.symbols('E')
for Nn in range(1, 5):
    d = sp.symbols('d1:%d' % (Nn+1), real=True); e = sp.symbols('epsilon', positive=True)
    rhs = I*sp.prod([1/(E - di + I*e) for di in d]) - I*sp.prod([1/(E - di - I*e) for di in d])
    # second product has poles at E = d + i e (UHP); first has none in UHP.  integral/2pi = i * sum Res_UHP
    tot = 0
    for di in set(d):
        tot += sp.residue(-I*sp.prod([1/(E - dj - I*e) for dj in d]), E, di + I*e)
    val = sp.simplify(I*tot) if Nn > 1 else sp.simplify(I*tot)
    if Nn >= 2:
        # generic distinct d's; check numerically too
        vnum = complex(val.subs({di: random.uniform(-2, 2) for di in d}).subs(e, 0.3))
        check('int dE/2pi RHS = 0 for N=%d (residues; numeric value %.1e)' % (Nn, abs(vnum)), abs(vnum) < 1e-12)
    else:
        check('int dE/2pi RHS = 1 for N=1', sp.simplify(val - 1) == 0)
# random complex numerical check up to N=12
rng = np.random.default_rng(1)
worst = 0
for Nn in range(1, 13):
    for trial in range(20):
        a = rng.normal(size=Nn); e = rng.uniform(0.01, 1)
        u = 1/(a + 1j*e); v = 1/(a - 1j*e)
        lhs = sum(np.prod(v[c+1:])*2*e/(a[c]**2 + e**2)*np.prod(u[:c]) for c in range(Nn))
        rhs = 1j*np.prod(u) - 1j*np.prod(v)
        worst = max(worst, abs(lhs - rhs)/max(1e-300, abs(rhs)))
check('telescoping identity numerically, N<=12, 240 random configurations', worst < 1e-10, 'max rel dev %.1e' % worst)

# ------------------------------------------------------------------ (ii)
# EXACT rational arithmetic in a Cartan-Weyl basis (no square roots): c = sum_{ab} g^{ab} T1(X_a) (x) T2(X_b),
# g_ab = 2 tr_F(X_a X_b) (so that an orthonormal basis has Tr(t^a t^b) = delta/2).  This is basis independent.
from fractions import Fraction as Fr
def mat(rows): return np.array([[Fr(x) for x in r] for r in rows], dtype=object)
def mm(A, B): return np.dot(A, B)
def zeros(n, m=None): return np.array([[Fr(0)]*(m or n) for _ in range(n)], dtype=object)
def eye(n):
    Z = zeros(n)
    for i in range(n): Z[i, i] = Fr(1)
    return Z
def Eij(n, i, j):
    Z = zeros(n); Z[i, j] = Fr(1); return Z
def tr(A): return sum(A[i, i] for i in range(A.shape[0]))
def inv_rational(M):
    n = M.shape[0]; A = [[Fr(M[i, j]) for j in range(n)] + [Fr(int(i == j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        piv = next(r for r in range(col, n) if A[r][col] != 0); A[col], A[piv] = A[piv], A[col]
        pv = A[col][col]; A[col] = [x/pv for x in A[col]]
        for r in range(n):
            if r != col and A[r][col] != 0:
                f = A[r][col]; A[r] = [a - f*b for a, b in zip(A[r], A[col])]
    return np.array([row[n:] for row in A], dtype=object)
def algebra_su(n):
    X = [Eij(n, i, j) for i in range(n) for j in range(n) if i != j]
    X += [Eij(n, k, k) - Eij(n, k+1, k+1) for k in range(n-1)]
    g = np.array([[2*tr(mm(A, B)) for B in X] for A in X], dtype=object)
    return X, g, inv_rational(g)
def coords(Y, X, ginv):
    v = [2*tr(mm(A, Y)) for A in X]
    return [sum(ginv[c, d]*v[d] for d in range(len(X))) for c in range(len(X))]
def adjoint(X, ginv):
    out = []
    for A in X:
        M = zeros(len(X))
        for b, Bm in enumerate(X):
            cc = coords(mm(A, Bm) - mm(Bm, A), X, ginv)
            for c in range(len(X)): M[c, b] = cc[c]
        out.append(M)
    return out
def sym2(Xf):
    n = Xf[0].shape[0]; idx = [(i, j) for i in range(n) for j in range(i, n)]; pos = {p: k for k, p in enumerate(idx)}
    out = []
    for A in Xf:
        M = zeros(len(idx))
        for k, (i, j) in enumerate(idx):
            # A acts on e_i e_j -> (A e_i) e_j + e_i (A e_j)
            for r in range(n):
                if A[r, i] != 0: M[pos[tuple(sorted((r, j)))], k] += A[r, i]
                if A[r, j] != 0: M[pos[tuple(sorted((i, r)))], k] += A[r, j]
        out.append(M)
    return out
def homog_su2(twoj):
    # spin j = twoj/2 on polynomials x^(2j-k) y^k, k=0..2j :  E = x d/dy, F = y d/dx, H = x d/dx - y d/dy
    d = twoj + 1
    E = zeros(d); F = zeros(d); H = zeros(d)
    for k in range(d):
        if k >= 1: E[k-1, k] = Fr(k)                 # x d/dy (x^(2j-k) y^k) = k x^(2j-k+1) y^(k-1)
        if k <= twoj - 1: F[k+1, k] = Fr(twoj - k)   # y d/dx
        H[k, k] = Fr(twoj - 2*k)
    return [E, F, H]
def is_rep(T, X, ginv):
    # check T([X_a,X_b]) = [T(X_a),T(X_b)] using structure constants from the fundamental
    ok = True
    for a in range(len(X)):
        for b in range(len(X)):
            cc = coords(mm(X[a], X[b]) - mm(X[b], X[a]), X, ginv)
            lhs = mm(T[a], T[b]) - mm(T[b], T[a])
            rhs = sum((cc[c]*T[c] for c in range(len(X))), zeros(T[0].shape[0]))
            ok = ok and np.all(lhs == rhs)
    return ok
def LX(T1, T2, ginv):
    n = len(T1); d1 = T1[0].shape[0]; d2 = T2[0].shape[0]
    T2up = [sum((ginv[a, b]*T2[b] for b in range(n)), zeros(d2)) for a in range(n)]
    c = sum((np.kron(T1[a], T2up[a]) for a in range(n)), zeros(d1*d2))
    L = sum((np.kron(mm(T1[a], T1[b]), mm(T2up[a], T2up[b])) for a in range(n) for b in range(n)), zeros(d1*d2))
    Xc = sum((np.kron(mm(T1[a], T1[b]), mm(T2up[b], T2up[a])) for a in range(n) for b in range(n)), zeros(d1*d2))
    return c, L, Xc
# SU(3)
X3, g3, gi3 = algebra_su(3)
F3 = X3; F3bar = [-A.T for A in X3]; A8 = adjoint(X3, gi3); S6 = sym2(X3)
for name, T in [('3', F3), ('3bar', F3bar), ('8', A8), ('6', S6)]:
    check('SU(3) rep %s: exact rational representation of sl(3) (commutators reproduced)' % name, is_rep(T, X3, gi3))
# Casimirs: C_F = 4/3, C_A = 3, C_6 = 10/3
for name, T, Cval in [('3', F3, Fr(4, 3)), ('8', A8, Fr(3)), ('6', S6, Fr(10, 3))]:
    C2 = sum((gi3[a, b]*mm(T[a], T[b]) for a in range(8) for b in range(8)), zeros(T[0].shape[0]))
    check('SU(3) Casimir of %s = %s exactly (metric normalisation Tr t^a t^b = delta/2)' % (name, Cval), np.all(C2 == Cval*eye(T[0].shape[0])))
reps3 = {'3': F3, '3bar': F3bar, '8': A8, '6': S6}
for p, q in [('3', '3'), ('3', '3bar'), ('3', '8'), ('8', '8'), ('3bar', '6'), ('6', '8'), ('6', '6')]:
    c, L, Xc = LX(reps3[p], reps3[q], gi3)
    okL = np.all(L == mm(c, c)); okX = np.all(Xc == mm(c, c) + Fr(3, 2)*c)
    check('SU(3) %s x %s (dim %d): L = c^2 and X = c^2 + (C_A/2) c, exact rationals' % (p, q, c.shape[0]), okL and okX)
# SU(2), spins 1/2 .. 2 in the polynomial basis
X2, g2, gi2 = algebra_su(2)   # basis E12, E21, H = E11-E22
su2 = {k: homog_su2(k) for k in (1, 2, 3, 4)}
# reorder homog basis [E,F,H] to match algebra_su(2) order [E12, E21, H]
for k, T in su2.items():
    check('SU(2) spin %s: polynomial-basis matrices represent sl(2)' % Fr(k, 2), is_rep(T, X2, gi2))
for p, q in [(1, 1), (1, 3), (2, 4), (3, 3), (4, 4)]:
    c, L, Xc = LX(su2[p], su2[q], gi2)
    okL = np.all(L == mm(c, c)); okX = np.all(Xc == mm(c, c) + Fr(2, 2)*c)
    check('SU(2) spin %s x spin %s: L = c^2 and X = c^2 + (C_A/2) c with C_A = 2, exact' % (Fr(p, 2), Fr(q, 2)), okL and okX)
# commutator [T_A.T_B, T_A.T_j] on 3bar (x) 3bar (x) 3, and its restriction to the colour-singlet subspace
def cop(Ti, Tj, slot_i, slot_j, reps, ginv):
    n = len(Ti)
    Tjup = [sum((ginv[a, b]*Tj[b] for b in range(n)), zeros(Tj[0].shape[0])) for a in range(n)]
    out = None
    for a in range(n):
        facs = [eye(r[0].shape[0]) for r in reps]
        facs[slot_i] = Ti[a]; facs[slot_j] = Tjup[a]
        k = np.kron(np.kron(facs[0], facs[1]), facs[2])
        out = k if out is None else out + k
    return out
reps = [F3bar, F3bar, F3]
cAB = cop(F3bar, F3bar, 0, 1, reps, gi3); cAj = cop(F3bar, F3, 0, 2, reps, gi3)
Cm = mm(cAB, cAj) - mm(cAj, cAB)
fro = float(sum(Fr(x)*Fr(x) for x in Cm.flatten()))**0.5   # matrix is real in this basis? compute Frobenius of the rational matrix
check('[T_A.T_B, T_A.T_j] != 0 on 3bar x 3bar x 3 (exact; Frobenius norm in this non-orthonormal basis %.4f)' % fro, fro > 0.5)
# basis-independent size: eigenvalues of i[.,.] ; spectrum of the Hermitian combination in an orthonormal basis equals that of the rational matrix
ev = np.linalg.eigvals(np.array(Cm, dtype=float))
print('      eigenvalues of [T_A.T_B, T_A.T_j] (3bar x 3bar x 3):', np.round(np.sort_complex(ev), 6))
fro_inv = np.sqrt(np.sum(np.abs(ev)**2))
check('basis-independent norm sqrt(sum|eig|^2) of the commutator = sqrt(3) = 1.732 (matches c_glauber 1.73)', abs(fro_inv - np.sqrt(3)) < 1e-9, '%.6f' % fro_inv)

# ------------------------------------------------------------------ (iii)
km, cA, dA, pAp, laP, eA = sp.symbols('k_minus c_A d_A pAplus laplus e_A', real=True)
eta = sp.symbols('eta', positive=True)
# D_sA = -2 p_A'^+ (k^- - c_A) + i eta,  D_a = 2 l_a^+ (k^- - d_A) + i eta ; close in the UHP: only the D_sA pole (k^- = c_A + i eta/(2p^+))
pAp_v = sp.Rational(7, 3); laP_v = sp.Rational(5, 4)
integrand = (I*eA*2*pAp_v)*(I/(-2*pAp_v*(km - cA) + I*eta))*(I/(2*laP_v*(km - dA) + I*eta))
pole = cA + I*eta/(2*pAp_v)
resid = sp.residue(integrand, km, pole)
val = sp.simplify(I*resid)    # int dk/(2pi) = (2 pi i/2pi) Res
target = (I*eA)*(I/(2*laP_v*(pole - dA) + I*eta))
check('k^- integral by exact residue = (i e_A)[i/D_a]_{spectator on shell}', sp.simplify(val - target) == 0)
# Glauber propagator -i/(k^2 - m^2) with k^2 ~ -k_T^2 -> i/(k_T^2+m^2); V = (i e_A)(i e_B) i/(k_T^2+m^2) = -i e_A e_B/(k_T^2+m^2)
kT2, m2, eB = sp.symbols('kT2 m2 e_B', positive=True)
Vk = sp.simplify((I*eA)*(I*eB)*(-I/(-kT2 - m2)))
check('V(k_T) = (i e_A)(i e_B)(-i)/(k^2-m^2)|_{k^2=-k_T^2} = -i e_A e_B/(k_T^2+m_g^2)', sp.simplify(Vk + I*eA*eB/(kT2 + m2)) == 0)
# chi(b): Vtilde(b) = int d^2k/(2pi)^2 e^{-ik.b} V(k) = (-i e_A e_B)(1/2pi) int_0^inf dk k J0(kb)/(k^2+m^2) = -i e_A e_B K0(mb)/(2pi) = i chi
mp.mp.dps = 30
for (mg, b) in [(0.5, 0.7), (1.0, 2.3), (0.2, 5.0)]:
    hank = mp.quadosc(lambda k: k*mp.besselj(0, k*b)/(k**2 + mg**2), [0, mp.inf], omega=b)
    check('Hankel: (1/2pi) int k J0(kb)/(k^2+m^2) dk = K0(mb)/(2pi) at m=%.1f b=%.1f' % (mg, b), abs(hank - mp.besselk(0, mg*b)) < 1e-15)
# sign: classical eikonal for a Yukawa potential  V(r) = e_A e_B e^{-m r}/(4 pi r) (repulsive for like charges):
# chi = -(1/v_rel) int dz V with the relativistic (1 - v1.v2) = 2 factor and v_rel = 2 -> chi = -int dz V = -e_A e_B K0(mb)/(2pi)
for (mg, b) in [(0.5, 0.7), (1.0, 2.3)]:
    mg, b = mp.mpf(str(mg)), mp.mpf(str(b))
    line = mp.quad(lambda z: mp.exp(-mg*mp.sqrt(b**2 + z**2))/(4*mp.pi*mp.sqrt(b**2 + z**2)), [-mp.inf, 0, mp.inf])
    check('line integral of Yukawa potential = K0(mb)/(2pi)  (m=%.1f b=%.1f): chi=-e_Ae_B K0/(2pi) is the repulsive (like-charge) sign' % (mg, b),
          abs(line - mp.besselk(0, mg*b)/(2*mp.pi)) < 1e-20)

# ------------------------------------------------------------------ (iv)
def leak_exact(Nc, d):
    a = (Nc + 1)/(2*Nc); bb = (Nc - 1)/(2*Nc)
    P = abs(a*np.exp(1j*d*(Nc - 1)/(2*Nc)) + bb*np.exp(-1j*d*(Nc + 1)/(2*Nc)))**2
    return 1 - P
def gens(n):
    g = []
    for i in range(n):
        for j in range(i+1, n):
            m = np.zeros((n, n), complex); m[i, j] = m[j, i] = .5; g.append(m)
            m = np.zeros((n, n), complex); m[i, j] = -.5j; m[j, i] = .5j; g.append(m)
    for k in range(1, n):
        m = np.zeros((n, n), complex); m[:k, :k] = np.eye(k); m[k, k] = -k; g.append(m/np.sqrt(2*k*(k+1)))
    return g
def leak_matrix(Nc, chi1, chi2):
    t = gens(Nc); Id = np.eye(Nc)
    # space: q (x) qbar (x) B ; T_q = t, T_qbar = -t^T, T_B = t (fundamental)
    Hq = sum(np.kron(np.kron(ta, Id), ta) for ta in t)
    Hqb = sum(np.kron(np.kron(Id, -ta.T), ta) for ta in t)
    U = expm(1j*(chi1*Hq + chi2*Hqb))
    s = np.zeros(Nc*Nc, complex)
    for i in range(Nc): s[i*Nc + i] = 1/np.sqrt(Nc)
    Ps = 0
    for beta in range(Nc):
        vin = np.kron(s, np.eye(Nc)[beta])
        out = U @ vin
        for bp in range(Nc):
            Ps += abs(np.vdot(np.kron(s, np.eye(Nc)[bp]), out))**2
    return 1 - Ps/Nc
for Nc in (2, 3, 4, 5):
    for d in (0.05, 0.7, 2.1):
        ex = leak_exact(Nc, d); closed = (Nc**2 - 1)/Nc**2*np.sin(d/2)**2; mat = leak_matrix(Nc, d, 0.0)
        check('N=%d d=%.2f: 1-P_singlet = (N^2-1)/N^2 sin^2(d/2) (projectors) = explicit matrices' % (Nc, d),
              abs(ex - closed) < 1e-13 and abs(mat - closed) < 1e-12, '%.10f' % closed)
Nc = 3
small = leak_matrix(3, 1e-3, 0.0)/1e-6
check('SU(3): leakage/d^2 -> C_F/(2N) = 2/9 for U = exp(i d T_q.T_B)', abs(small - 2/9) < 1e-6, '%.8f' % small)
# common phase chi0 with small difference delta: coefficient C_F/(2N) <sinc^2(chi0 lambda_R/2)> < 2/9
for chi0 in (0.0, 0.4, 1.0):
    dl = 1e-3
    coef = leak_matrix(3, chi0 + dl/2, chi0 - dl/2)/dl**2
    print('      chi0=%.1f: leakage/delta^2 = %.6f' % (chi0, coef))
    if chi0 == 0.0:
        check('second order in all phases: leakage = (chi1-chi2)^2 C_F/(2N) at chi0=0', abs(coef - 2/9) < 1e-6)
    else:
        check('common phase chi0=%.1f reduces the delta^2 coefficient below 2/9 (qualifier needed)' % chi0, coef < 2/9 - 1e-3)
# unitarity: colour-summed probability = 1
t = gens(3); Id = np.eye(3)
Hq = sum(np.kron(np.kron(ta, Id), ta) for ta in t); Hqb = sum(np.kron(np.kron(Id, -ta.T), ta) for ta in t)
U = expm(1j*(0.9*Hq - 0.3*Hqb))
check('U unitary (colour-summed probability conserved)', np.allclose(U.conj().T @ U, np.eye(27)))

print('\nSUMMARY: %d/%d checks passed' % (sum(res), len(res)))
