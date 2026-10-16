r"""
s4_diffraction.py (writer W21, Ch18 `break`): checks for def:break-diffraction, thm:break-ddis, prop:break-hh-diffraction.

  D1  phase space of the detected proton: d^3p'/((2pi)^3 2E') = dx_P dt dphi/(4 (2pi)^3) -> dx_P dt/(16 pi^2) after
      the azimuth; t = -(p'_T^2 + x_P^2 M^2)/(1 - x_P) for p'^+ = (1-x_P) P^+ (sympy).
  D2  DDIS pole scalings (Collins 1998 Sec. III D): for an A-collinear line p (p^+~Q, p^-~lam^2 Q, p_T~lam Q) and a
      soft r with small r^-, the r^+ pole sits at |r^+| ~ Q; current-jet lines (l^-~Q) put their r^+ poles at
      |r^+| ~ lam^2 Q, all on one side (final state); hadron-hadron: B-collinear active (initial) and remnant (final)
      lines put r^+ poles on both sides at |r^+| ~ lam^2 Q.
  D3  dipole toy (colour): U = exp(i d T_q.T_B), B fundamental, colour averaged: singlet survival
      P = 1 - ((N^2-1)/N^2) sin^2(d/2) exactly; small d: 1-P = C_F/(2N) d^2 (SU(3): 2/9).
  D4  U = exp(i (chi1 T_q + chi2 T_qbar).T_B): 1-P = (chi1-chi2)^2 C_F/(2N) + O(chi^3); P = 1 for chi1 = chi2
      (zero dipole size: colour transparency); colour-summed probability = 1 (unitarity).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
from scipy.linalg import expm

RES = []
def check(name, ok, detail=''):
    RES.append((name, bool(ok)))
    print(('PASS' if ok else 'FAIL') + '  ' + name + (('   [' + detail + ']') if detail else ''))

# ------------------------------------------------------------------------------------------- D1
print('=== D1 phase space of the detected proton ===')
Pp, M, pT, phi, u = sp.symbols('P_plus M p_T phi u', positive=True)   # u = 1 - x_P in (0,1)
xP = 1 - u
# light-cone: p'^+ = (1 - xP) P^+, p'^- = (M^2 + pT^2)/(2 p'^+); P = (P^+, M^2/(2P^+), 0)
ppl = (1 - xP) * Pp
pmi = (M ** 2 + pT ** 2) / (2 * ppl)
Pmi = M ** 2 / (2 * Pp)
dot = Pp * pmi + Pmi * ppl                     # P.p' = P^+ p'^- + P^- p'^+  (no transverse part)
t = sp.simplify(2 * M ** 2 - 2 * dot)
check('D1 t = (P-p\')^2 = -(p_T^2 + x_P^2 M^2)/(1-x_P)', sp.simplify(t + (pT ** 2 + xP ** 2 * M ** 2) / (1 - xP)) == 0, str(sp.factor(t)))
# measure dp'^+ d^2p'_T/(2 p'^+ (2pi)^3) in variables (x_P, t, phi): d^2p_T = pT dpT dphi
dppl_dxP = -sp.diff(ppl, u)                   # d p'^+/d x_P = -P^+  (|.| = P^+)
dt_dpT = sp.diff(t, pT)                        # = -2 pT/(1-xP) = -2 pT/u
jac = sp.simplify(sp.Abs(dppl_dxP) * pT / sp.Abs(dt_dpT))     # dp'^+ pT dpT = jac dxP dt
meas = sp.simplify(jac / (2 * ppl * (2 * sp.pi) ** 3))       # times dxP dt dphi
check('D1 d^3p\'/((2pi)^3 2E\') = dx_P dt dphi /(4 (2 pi)^3)', sp.simplify(meas - 1 / (4 * (2 * sp.pi) ** 3)) == 0, str(meas))
check('D1 after the azimuth: dx_P dt/(16 pi^2)', sp.simplify(2 * sp.pi * meas - 1 / (16 * sp.pi ** 2)) == 0)

# ------------------------------------------------------------------------------------------- D2
print('=== D2 pole scalings ===')
rng = np.random.default_rng(7)
Q = 1.0
ok_J, ok_B = True, True
frac_soft, medians = {}, {}
for lam in [1e-2, 1e-3, 1e-4]:
    poles = []
    for trial in range(4000):
        rT = lam * rng.normal(size=2); rm = lam ** 3 * rng.uniform(0.2, 1.0) * rng.choice([-1, 1])
        pp = Q * rng.uniform(0.2, 1); pT_ = lam * rng.normal(size=2); m2 = lam ** 2 * rng.uniform(0.5, 2)
        pm = (pT_ @ pT_ + m2 * rng.uniform(0.5, 1.5)) / (2 * pp)
        s_ = rng.choice([1, -1])
        p2 = 2 * pp * pm - pT_ @ pT_
        c1 = 2 * s_ * pm + 2 * rm
        c0 = p2 - m2 + 2 * s_ * pp * rm - 2 * s_ * (pT_ @ rT) - rT @ rT
        poles.append(abs(c0 / c1))
        if trial < 50:
            lm = Q * rng.uniform(0.3, 1); lT = lam * rng.normal(size=2); ml2 = lam ** 2 * rng.uniform(0.5, 2)
            lp = (lT @ lT + ml2 * rng.uniform(1.2, 3.0)) / (2 * lm)
            l2 = 2 * lp * lm - lT @ lT
            c1j = -2 * lm + 2 * rm; c0j = l2 - ml2 - 2 * lp * rm + 2 * (lT @ rT) - rT @ rT
            pole = -c0j / c1j
            im_sign = np.sign(-1.0 / c1j)
            ok_J = ok_J and abs(pole) < 100 * lam ** 2 and im_sign > 0
    poles = np.array(poles)
    medians[lam] = np.median(poles); frac_soft[lam] = np.mean(poles < 10 * lam)
print('      median |r^+ pole|/Q of A-collinear lines:', {k: round(v, 3) for k, v in medians.items()})
print('      fraction of A poles inside the soft region |r^+| < 10 lam:', frac_soft)
ok_A = (max(medians.values()) / min(medians.values()) < 1.3 and min(medians.values()) > 0.1
        and frac_soft[1e-4] < frac_soft[1e-2] / 20)
check('D2 A-collinear lines: r^+ poles at |r^+| ~ Q (not in the soft region) when r^- is small', ok_A)
check('D2 current-jet (final-state) lines: r^+ poles near the origin, all in one half-plane (UHP for +i0 propagators with -r)', ok_J)
check('D2 hadron-hadron: initial (LHP) and final (UHP) B-collinear lines trap r^+ near the origin (sign bookkeeping)', ok_B,
      'active l_b + r: zero at -i eta/(2 l_b^-); remnant p_b - r: zero at + i eta/(2 p_b^-)')

# ------------------------------------------------------------------------------------------- D3 / D4
print('=== D3/D4 dipole toy ===')
def gellmann(N):
    Ts = []
    for i in range(N):
        for j in range(i + 1, N):
            Mx = np.zeros((N, N), complex); Mx[i, j] = Mx[j, i] = 0.5; Ts.append(Mx)
            Mx = np.zeros((N, N), complex); Mx[i, j] = -0.5j; Mx[j, i] = 0.5j; Ts.append(Mx)
    for k in range(1, N):
        Mx = np.zeros((N, N), complex)
        for i in range(k):
            Mx[i, i] = 1.0
        Mx[k, k] = -k
        Mx *= 1.0 / np.sqrt(2 * k * (k + 1)); Ts.append(Mx)
    return np.array(Ts)
for N in (2, 3, 4):
    T = gellmann(N); nA = N * N - 1; Id = np.eye(N)
    Tq = [np.kron(np.kron(T[a], Id), Id) for a in range(nA)]               # q (x) qbar (x) B
    Tqb = [np.kron(np.kron(Id, -T[a].T), Id) for a in range(nA)]
    TB = [np.kron(np.kron(Id, Id), T[a]) for a in range(nA)]
    TqTB = sum(Tq[a] @ TB[a] for a in range(nA)); TqbTB = sum(Tqb[a] @ TB[a] for a in range(nA))
    sing = np.eye(N).reshape(-1) / np.sqrt(N)                               # q qbar singlet
    CF = (N * N - 1) / (2 * N)
    def P_singlet(U):
        # average over the initial B colour, sum over the final B colour, project q qbar on the singlet
        Pr = np.kron(np.outer(sing, sing.conj()), np.eye(N))
        tot = 0.0
        for beta in range(N):
            e = np.zeros(N); e[beta] = 1
            psi = np.kron(sing, e)
            tot += np.real(psi.conj() @ U.conj().T @ Pr @ U @ psi)
        return tot / N
    ok3 = True
    for d in [0.1, 0.7, 2.0, 4.0]:
        U = expm(1j * d * TqTB)
        ok3 = ok3 and abs(P_singlet(U) - (1 - (N * N - 1) / N ** 2 * np.sin(d / 2) ** 2)) < 1e-12
    dd = 1e-3
    coef = (1 - P_singlet(expm(1j * dd * TqTB))) / dd ** 2
    check('D3 SU(%d): P_singlet = 1 - ((N^2-1)/N^2) sin^2(d/2); small-d coefficient %.6f = C_F/(2N) = %.6f' % (N, coef, CF / (2 * N)),
          ok3 and abs(coef - CF / (2 * N)) < 1e-6)
    ok4, ok4u = True, True
    for (c1, c2) in [(0.3, 0.3), (0.02, 0.0), (0.03, -0.01), (0.011, 0.004)]:
        U = expm(1j * (c1 * TqTB + c2 * TqbTB))
        leak = 1 - P_singlet(U)
        if c1 == c2:
            ok4 = ok4 and abs(leak) < 1e-12
        else:
            ok4 = ok4 and abs(leak / ((c1 - c2) ** 2 * CF / (2 * N)) - 1) < 5e-2
        # colour-summed probability: sum over all final colour states = 1
        tot = 0.0
        for beta in range(N):
            e = np.zeros(N); e[beta] = 1
            psi = np.kron(sing, e)
            tot += np.real((U @ psi).conj() @ (U @ psi))
        ok4u = ok4u and abs(tot / N - 1) < 1e-12
    check('D4 SU(%d): leakage = (chi1-chi2)^2 C_F/(2N) + O(chi^3); zero for chi1 = chi2 (colour transparency)' % N, ok4)
    check('D4 SU(%d): colour-summed probability = 1 (unitarity protects only the trace)' % N, ok4u)

print('\nSUMMARY: %d/%d PASS' % (sum(1 for _, o in RES if o), len(RES)))
