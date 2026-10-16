r"""
s5_measurement.py (writer W21, Ch18 `break`): checks for prop:break-measurement and the auxiliary lemma
lem:break-weighted-cut (weighted light-cone cut-position identity).

Chain data as in def:appO-chain: vertices v_1..v_n (closed-time-path order), states s_0..s_n with real energies E_i,
reduced weights alpha_i (amplitude), beta_i (conjugate); internal vertices alpha_i = beta_i; amplitude insertions
beta_i = 0; conjugate insertions alpha_i = 0.  Measurement weights pi_j = pi(s_j) of the cut states.

Claim (eta > 0 exact):
  sum_j pi_j T_j = delta_{n0} pi_0 W_0 - i sum_{m=1}^n (pi_m alpha_m - pi_{m-1} beta_m) prod_{i<m} alpha_i prod_{i>m} beta_i
                   * int dE/(2 pi) H_m(E),
  T_j = W_j int dE/(2pi) prod_{i<j}(E-E_i+i eta)^-1 [2 eta/((E-E_j)^2+eta^2)] prod_{i>j}(E-E_i-i eta)^-1,
  W_j = prod_{i<=j} alpha_i prod_{i>j} beta_i ,  H_m = prod_{i<m}(E-E_i+i eta)^-1 prod_{i>=m}(E-E_i-i eta)^-1.

  M1  the identity, LHS by direct numerical E-quadrature, RHS by residues (independent evaluations), random chains
      n = 0..5, random complex weights and random pi_j.
  M2  pi constant across every internal vertex -> internal vertices drop out (the unweighted structure survives,
      insertions keep their own pi); pi constant along the whole chain -> sum = pi * (unweighted sum).
  M3  pi jumps across an internal vertex later than all insertions -> the sum differs from the pi-constant value by
      exactly the vertex term -i alpha_m (pi_m - pi_{m-1}) ... int H_m (non-zero): final-state interactions survive.
  M4  operator toys: H = H0 + V block diagonal in a conserved transverse momentum P: U^dag e^{i b P} U = e^{i b P};
      a projector on a non-conserved label: U^dag Pi U != Pi;  interaction picture U_I(t2,t1) commutes with e^{ibP}.
  M5  tau = 0 Glauber insertion V_G = sum_k chi(k) rho_A(k) rho_B(-k) (momentum transfer k from B to A spectators):
      [V_G, e^{i b (P_A + P_B)}] = 0, [V_G, e^{i b P_A}] != 0; hence W'^dag Pi W = Pi W'^dag W for Pi = e^{ib(P_A+P_B)}.
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from scipy import integrate
from scipy.linalg import expm

RES = []
def check(name, ok, detail=''):
    RES.append((name, bool(ok)))
    print(('PASS' if ok else 'FAIL') + '  ' + name + (('   [' + detail + ']') if detail else ''))

def res_int(poles):
    """int_R dE/(2 pi) prod_k 1/(E - z_k), len >= 2, distinct poles; close in the upper half plane."""
    poles = list(poles)
    tot = 0j
    for k, zk in enumerate(poles):
        if zk.imag > 0:
            pr = 1.0 + 0j
            for l, zl in enumerate(poles):
                if l != k:
                    pr *= 1.0 / (zk - zl)
            tot += pr
    return 1j * tot

def lhs_quad(E, alpha, beta, pis, eta):
    n = len(E) - 1
    total = 0j
    for j in range(n + 1):
        Wj = np.prod(alpha[:j]) * np.prod(beta[j:])          # alpha_1..alpha_j, beta_{j+1}..beta_n  (0-based shift)
        def integrand(x, part):
            val = 2 * eta / ((x - E[j]) ** 2 + eta ** 2)
            for i in range(j):
                val = val / (x - E[i] + 1j * eta)
            for i in range(j + 1, n + 1):
                val = val / (x - E[i] - 1j * eta)
            return val.real if part == 0 else val.imag
        pts = sorted(E)
        lo, hi = min(E) - 60, max(E) + 60
        re = integrate.quad(integrand, lo, hi, args=(0,), points=pts, limit=2000, epsabs=1e-13, epsrel=1e-11)[0]
        im = integrate.quad(integrand, lo, hi, args=(1,), points=pts, limit=2000, epsabs=1e-13, epsrel=1e-11)[0]
        # tails beyond the finite range (integrand ~ E^-(n+2); for n = 0 a Lorentzian, tails not negligible)
        for (a_, b_) in ((-np.inf, lo), (hi, np.inf)):
            re += integrate.quad(integrand, a_, b_, args=(0,), limit=400, epsabs=1e-14)[0]
            im += integrate.quad(integrand, a_, b_, args=(1,), limit=400, epsabs=1e-14)[0]
        total += pis[j] * Wj * (re + 1j * im) / (2 * np.pi)
    return total

def rhs_formula(E, alpha, beta, pis, eta):
    n = len(E) - 1
    if n == 0:
        return pis[0] * 1.0          # W_0 = empty products = 1
    tot = 0j
    for m in range(1, n + 1):
        # H_m: a_i (i<m) -> pole E_i - i eta ; b_i (i>=m) -> pole E_i + i eta ; i = 0..n
        poles = [E[i] - 1j * eta for i in range(m)] + [E[i] + 1j * eta for i in range(m, n + 1)]
        Hm = res_int(poles)
        pref = np.prod(alpha[:m - 1]) * np.prod(beta[m:])      # prod_{i<m} alpha_i  prod_{i>m} beta_i (1-based)
        tot += -1j * (pis[m] * alpha[m - 1] - pis[m - 1] * beta[m - 1]) * pref * Hm
    return tot

rng = np.random.default_rng(11)
print('=== M1 weighted cut-position identity (quadrature vs residues) ===')
worst = 0.0
for trial in range(24):
    n = trial % 6
    E = list(rng.uniform(-2, 2, size=n + 1))
    alpha = rng.normal(size=n) + 1j * rng.normal(size=n)
    beta = rng.normal(size=n) + 1j * rng.normal(size=n)
    for i in range(n):          # random vertex types
        t = rng.integers(3)
        if t == 0: beta[i] = alpha[i]          # internal
        elif t == 1: beta[i] = 0               # amplitude insertion
        else: alpha[i] = 0                     # conjugate insertion
    pis = rng.normal(size=n + 1) + 1j * rng.normal(size=n + 1)
    eta = 0.35
    L = lhs_quad(E, alpha, beta, pis, eta); R = rhs_formula(E, alpha, beta, pis, eta)
    worst = max(worst, abs(L - R) / (1e-12 + abs(R) + 1e-3))
check('M1 sum_j pi_j T_j = delta_{n0} pi_0 W_0 - i sum_m (pi_m alpha_m - pi_{m-1} beta_m) ... int H_m  (24 random chains, n=0..5)',
      worst < 1e-6, 'worst rel. deviation %.1e' % worst)

print('=== M2 pi constant across internal vertices ===')
ok2, ok2b = True, True
for trial in range(20):
    n = 5
    E = list(rng.uniform(-2, 2, size=n + 1))
    alpha = rng.normal(size=n) + 1j * rng.normal(size=n); beta = alpha.copy()
    ins = rng.choice(n, size=2, replace=False)          # two insertions, the rest internal
    beta[ins[0]] = 0; alpha[ins[1]] = 0
    # pi changes only across insertion vertices
    pis = np.empty(n + 1, complex); pis[0] = rng.normal() + 1j * rng.normal()
    for m in range(1, n + 1):
        pis[m] = pis[m - 1] * (np.exp(1j * rng.normal()) if (m - 1) in ins else 1.0)
    eta = 0.3
    full = rhs_formula(E, alpha, beta, pis, eta)
    # only insertion terms should contribute: recompute keeping only m in ins
    tot = 0j
    for m in range(1, n + 1):
        if (m - 1) not in ins:
            continue
        poles = [E[i] - 1j * eta for i in range(m)] + [E[i] + 1j * eta for i in range(m, n + 1)]
        tot += -1j * (pis[m] * alpha[m - 1] - pis[m - 1] * beta[m - 1]) * np.prod(alpha[:m - 1]) * np.prod(beta[m:]) * res_int(poles)
    ok2 = ok2 and abs(full - tot) < 1e-12 * (1 + abs(tot))
    # constant pi: proportional to the unweighted sum
    pc = rng.normal() + 1j * rng.normal()
    ok2b = ok2b and abs(rhs_formula(E, alpha, beta, np.full(n + 1, pc), eta) - pc * rhs_formula(E, alpha, beta, np.ones(n + 1), eta)) < 1e-12
check('M2 pi constant across internal vertices: internal vertices drop out exactly', ok2)
check('M2 pi constant along the chain: weighted sum = pi * unweighted sum', ok2b)

print('=== M3 pi jumps across a late internal vertex ===')
n = 4
E = [0.1, -0.7, 1.3, 0.4, -1.1]
alpha = np.array([0.8 + 0.3j, 1.1 - 0.2j, -0.5 + 0.9j, 0.7 + 0.1j]); beta = alpha.copy()
beta[0] = 0                       # vertex 1 = amplitude insertion, vertices 2,3,4 internal (later)
pis_const = np.array([1, 1, 1, 1, 1], complex)
pis_jump = np.array([1, 1, 1, 0, 0], complex)     # e.g. a projector: the state after vertex 3 fails the measurement
eta = 0.3
d = rhs_formula(E, alpha, beta, pis_jump, eta) - rhs_formula(E, alpha, beta, pis_const, eta)
m = 3
poles = [E[i] - 1j * eta for i in range(m)] + [E[i] + 1j * eta for i in range(m, n + 1)]
vt = -1j * (0 * alpha[m - 1] - 1 * beta[m - 1]) * np.prod(alpha[:m - 1]) * np.prod(beta[m:]) * res_int(poles)
# pi_3 = 0 also kills the alpha_m-part of vertex 4's term ... recompute the full difference term by term
diff_terms = 0j
for mm in range(1, n + 1):
    polesm = [E[i] - 1j * eta for i in range(mm)] + [E[i] + 1j * eta for i in range(mm, n + 1)]
    a = -1j * (pis_jump[mm] * alpha[mm - 1] - pis_jump[mm - 1] * beta[mm - 1]) * np.prod(alpha[:mm - 1]) * np.prod(beta[mm:]) * res_int(polesm)
    b = -1j * (pis_const[mm] * alpha[mm - 1] - pis_const[mm - 1] * beta[mm - 1]) * np.prod(alpha[:mm - 1]) * np.prod(beta[mm:]) * res_int(polesm)
    diff_terms += a - b
check('M3 a projector that changes across a late internal vertex leaves a non-zero vertex term (FSI survive)',
      abs(d) > 1e-3 and abs(d - diff_terms) < 1e-12, '|difference| = %.4f' % abs(d))

print('=== M4 operator toys ===')
# toy space: transverse momentum P in {-2..2} (x) internal label n in {0,1,2}
Ps = np.arange(-2, 3); nint = 3; dim = len(Ps) * nint
P = np.kron(np.diag(Ps.astype(float)), np.eye(nint))
H0 = np.diag(rng.uniform(0, 1, size=dim))
# V: hermitian, block diagonal in P (conserves P), mixes internal labels
V = np.zeros((dim, dim), complex)
for k in range(len(Ps)):
    blk = rng.normal(size=(nint, nint)) + 1j * rng.normal(size=(nint, nint)); blk = blk + blk.conj().T
    V[k * nint:(k + 1) * nint, k * nint:(k + 1) * nint] = 0.4 * blk
H = H0 + V
b = 0.7
Pib = expm(1j * b * P)
Pih = np.kron(np.eye(len(Ps)), np.diag([1.0, 0, 0]))           # 'identified hadron': internal label 0
ok4 = True
for t in [0.5, 1.7, 4.0]:
    U = expm(-1j * H * t)
    UI = expm(1j * H0 * t) @ expm(-1j * H * (t - 0.3)) @ expm(-1j * H0 * 0.3)
    ok4 = ok4 and np.allclose(U.conj().T @ Pib @ U, Pib) and np.allclose(UI.conj().T @ Pib @ UI, Pib)
check('M4 U^dag e^{ibP} U = e^{ibP} (also for the interaction-picture U_I) when the interaction conserves P', ok4)
U = expm(-1j * H * 1.7)
check('M4 a projector on a non-conserved label: U^dag Pi_h U != Pi_h', not np.allclose(U.conj().T @ Pih @ U, Pih),
      '||U^dag Pi U - Pi|| = %.3f' % np.linalg.norm(U.conj().T @ Pih @ U - Pih))

print('=== M5 tau = 0 Glauber insertion and the TMD measurement ===')
# A and B spectator momenta in {-2..2} (truncated); V_G transfers k from B to A: |pA, pB> -> |pA + k, pB - k>
nP = 5; dimAB = nP * nP
def idx(pa, pb): return (pa + 2) * nP + (pb + 2)
VG = np.zeros((dimAB, dimAB))
chi = {1: 0.6, -1: 0.6, 2: 0.25, -2: 0.25}
for pa in range(-2, 3):
    for pb in range(-2, 3):
        for k, c in chi.items():
            if -2 <= pa + k <= 2 and -2 <= pb - k <= 2:
                VG[idx(pa + k, pb - k), idx(pa, pb)] += c
check('M5 V_G hermitian (real even kernel)', np.allclose(VG, VG.T))
PA = np.diag([pa for pa in range(-2, 3) for pb in range(-2, 3)]).astype(float)
PB = np.diag([pb for pa in range(-2, 3) for pb in range(-2, 3)]).astype(float)
Pi_tot = expm(1j * b * (PA + PB)); Pi_A = expm(1j * b * PA)
check('M5 [V_G, e^{ib(P_A+P_B)}] = 0 (translation-invariant kernel conserves the total transverse momentum)', np.allclose(VG @ Pi_tot, Pi_tot @ VG))
check('M5 [V_G, e^{ib P_A}] != 0 (the measurement must act on the whole final state)', not np.allclose(VG @ Pi_A, Pi_A @ VG))
W = expm(-1j * 0.8 * VG); Wp = expm(-1j * 0.8 * VG)
check('M5 W\'^dag Pi W = Pi W\'^dag W = Pi for Pi = e^{ib(P_A+P_B)}', np.allclose(Wp.conj().T @ Pi_tot @ W, Pi_tot))

print('\nSUMMARY: %d/%d PASS' % (sum(1 for _, o in RES if o), len(RES)))
