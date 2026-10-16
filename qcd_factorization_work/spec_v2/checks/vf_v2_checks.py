"""Checks behind the new spec-v2 entries of VERIFIED_FORMULAS_v2.md (groups VF-QCD and figure data).

Run:  python3 -I vf_v2_checks.py > vf_v2_checks.log
Every check prints PASS/FAIL; the last line summarizes.  numpy 2.0, sympy 1.14, mpmath (sympy dependency).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import itertools
import numpy as np
import sympy as sp
import mpmath as mp

RES = []
def check(name, ok, info=''):
    RES.append(bool(ok))
    print(('PASS ' if ok else 'FAIL ') + name + ((' : ' + info) if info else ''))

# ------------------------------------------------------------------ Q1  SU(N) algebra (N = 2, 3)
def gellmann():
    l = np.zeros((8, 3, 3), dtype=complex)
    l[0][0, 1] = l[0][1, 0] = 1
    l[1][0, 1] = -1j; l[1][1, 0] = 1j
    l[2][0, 0] = 1; l[2][1, 1] = -1
    l[3][0, 2] = l[3][2, 0] = 1
    l[4][0, 2] = -1j; l[4][2, 0] = 1j
    l[5][1, 2] = l[5][2, 1] = 1
    l[6][1, 2] = -1j; l[6][2, 1] = 1j
    l[7] = np.diag([1, 1, -2]) / np.sqrt(3)
    return l / 2
def pauli():
    s = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]], dtype=complex)
    return s / 2
for N, T in ((2, pauli()), (3, gellmann())):
    n = N * N - 1
    tr = np.array([[np.trace(T[a] @ T[b]) for b in range(n)] for a in range(n)])
    check('Q1a SU(%d) Tr(t^a t^b) = delta/2' % N, np.allclose(tr, np.eye(n) / 2))
    f = np.zeros((n, n, n)); d = np.zeros((n, n, n))
    for a, b, c in itertools.product(range(n), repeat=3):
        comm = T[a] @ T[b] - T[b] @ T[a]
        anti = T[a] @ T[b] + T[b] @ T[a]
        f[a, b, c] = (-2j * np.trace(comm @ T[c])).real
        d[a, b, c] = (2 * np.trace(anti @ T[c])).real
    ok = all(np.allclose(T[a] @ T[b] - T[b] @ T[a], 1j * sum(f[a, b, c] * T[c] for c in range(n))) for a in range(n) for b in range(n))
    check('Q1b SU(%d) [t^a,t^b] = i f^{abc} t^c, f totally antisymmetric' % N, ok and np.allclose(f, -np.transpose(f, (1, 0, 2))) and np.allclose(f, -np.transpose(f, (0, 2, 1))))
    CF = (N * N - 1) / (2 * N)
    check('Q1c SU(%d) t^a t^a = C_F 1, C_F=(N^2-1)/(2N)' % N, np.allclose(sum(T[a] @ T[a] for a in range(n)), CF * np.eye(N)))
    ff = np.einsum('acd,bcd->ab', f, f)
    check('Q1d SU(%d) f^{acd} f^{bcd} = C_A delta, C_A=N' % N, np.allclose(ff, N * np.eye(n)))
    lhs = np.einsum('aij,akl->ijkl', T, T)
    rhs = 0.5 * (np.einsum('il,kj->ijkl', np.eye(N), np.eye(N)) - np.einsum('ij,kl->ijkl', np.eye(N), np.eye(N)) / N)
    check('Q1e SU(%d) Fierz t^a_ij t^a_kl = (d_il d_kj - d_ij d_kl / N)/2' % N, np.allclose(lhs, rhs))
    ok = all(np.isclose(np.trace(T[a] @ T[b] @ T[c]), 0.25 * (d[a, b, c] + 1j * f[a, b, c])) for a, b, c in itertools.product(range(n), repeat=3))
    check('Q1f SU(%d) Tr(t^a t^b t^c) = (d^{abc} + i f^{abc})/4' % N, ok)
    # component form of the field strength: -ig[A_mu,A_nu] = g f^{abc} A^b_mu A^c_nu t^a
    rng = np.random.default_rng(1)
    A1 = rng.normal(size=n); A2 = rng.normal(size=n); g = 0.7
    M1 = sum(A1[a] * T[a] for a in range(n)); M2 = sum(A2[a] * T[a] for a in range(n))
    lhs = -1j * g * (M1 @ M2 - M2 @ M1)
    rhs = sum(g * f[a, b, c] * A1[b] * A2[c] * T[a] for a in range(n) for b in range(n) for c in range(n))
    check('Q1g SU(%d) -ig[A_mu,A_nu] = g f^{abc} A^b_mu A^c_nu t^a (D = d - igA)' % N, np.allclose(lhs, rhs))

# ------------------------------------------------------------------ Q2  [D_mu, D_nu] = -i g G_mu_nu  (abelian-free check in 2D, SU(2))
x, y, g = sp.symbols('x y g', real=True)
Afun = [[sp.Function('A%d_%d' % (mu, a))(x, y) for a in range(3)] for mu in range(2)]
T2 = [sp.Matrix([[0, 1], [1, 0]]) / 2, sp.Matrix([[0, -sp.I], [sp.I, 0]]) / 2, sp.Matrix([[1, 0], [0, -1]]) / 2]
Amat = [sum((Afun[mu][a] * T2[a] for a in range(3)), sp.zeros(2)) for mu in range(2)]
psi = sp.Matrix([sp.Function('p1')(x, y), sp.Function('p2')(x, y)])
X = [x, y]
def D(mu, v):
    return v.diff(X[mu]) - sp.I * g * Amat[mu] * v
comm = D(0, D(1, psi)) - D(1, D(0, psi))
G01 = Amat[1].diff(x) - Amat[0].diff(y) - sp.I * g * (Amat[0] * Amat[1] - Amat[1] * Amat[0])
check('Q2 [D_mu,D_nu] psi = -i g G_mu_nu psi, G = dA - dA - ig[A,A]', sp.simplify(comm + sp.I * g * G01 * psi) == sp.zeros(2, 1))

# ------------------------------------------------------------------ Q3  one-loop Z factors: Slavnov-Taylor consistency (units alpha_s/(4 pi eps))
CA, CF, TF, nf, xi = sp.symbols('C_A C_F T_F n_f xi')
dZ2 = -CF * xi
dZ3 = (sp.Rational(13, 6) - xi / 2) * CA - sp.Rational(4, 3) * TF * nf
dZ1F = -(xi * CF + (3 + xi) / 4 * CA)
dZt3 = CA * (3 - xi) / 4
dZt1 = -CA * xi / 2
dZ1 = (sp.Rational(17, 12) - 3 * xi / 4) * CA - sp.Rational(4, 3) * TF * nf
dZ4 = (sp.Rational(2, 3) - xi) * CA - sp.Rational(4, 3) * TF * nf
beta0 = sp.Rational(11, 3) * CA - sp.Rational(4, 3) * TF * nf
routes = {'quark-gluon vertex Z1F/(Z2 Z3^1/2)': dZ1F - dZ2 - dZ3 / 2,
          'ghost vertex Zt1/(Zt3 Z3^1/2)': dZt1 - dZt3 - dZ3 / 2,
          'three-gluon Z1/Z3^3/2': dZ1 - sp.Rational(3, 2) * dZ3,
          'four-gluon Z4^1/2/Z3': dZ4 / 2 - dZ3}
for k, v in routes.items():
    check('Q3 delta Z_g via %s = -beta0/2 (xi independent)' % k, sp.simplify(v + beta0 / 2) == 0)
check('Q3 Feynman gauge: dZ1F = -(C_F + C_A), dZ2 = -C_F, dZ3 = (5/3)C_A - (4/3)T_F n_f',
      sp.simplify(dZ1F.subs(xi, 1) + CF + CA) == 0 and sp.simplify(dZ2.subs(xi, 1) + CF) == 0 and sp.simplify(dZ3.subs(xi, 1) - sp.Rational(5, 3) * CA + sp.Rational(4, 3) * TF * nf) == 0)

# ------------------------------------------------------------------ Q4  beta coefficients: group form vs SU(3)
su3 = {CA: 3, CF: sp.Rational(4, 3), TF: sp.Rational(1, 2)}
beta1 = sp.Rational(34, 3) * CA**2 - 4 * CF * TF * nf - sp.Rational(20, 3) * CA * TF * nf
beta2 = (sp.Rational(2857, 54) * CA**3 + 2 * CF**2 * TF * nf - sp.Rational(205, 9) * CF * CA * TF * nf
         - sp.Rational(1415, 27) * CA**2 * TF * nf + sp.Rational(44, 9) * CF * TF**2 * nf**2 + sp.Rational(158, 27) * CA * TF**2 * nf**2)
check('Q4a beta0(SU3) = 11 - 2 n_f/3', sp.expand(beta0.subs(su3) - (11 - sp.Rational(2, 3) * nf)) == 0)
check('Q4b beta1(SU3) = 102 - 38 n_f/3', sp.expand(beta1.subs(su3) - (102 - sp.Rational(38, 3) * nf)) == 0)
check('Q4c beta2(SU3) = 2857/2 - 5033 n_f/18 + 325 n_f^2/54', sp.expand(beta2.subs(su3) - (sp.Rational(2857, 2) - sp.Rational(5033, 18) * nf + sp.Rational(325, 54) * nf**2)) == 0)
check('Q4d asymptotic freedom: beta0 > 0 iff n_f < 11 C_A/(4 T_F) = 33/2 for SU(3)', sp.solve(sp.Eq(beta0.subs(su3), 0), nf) == [sp.Rational(33, 2)])
# beta1 > 0 for n_f <= 8, < 0 for n_f >= 9 (SU(3))
b1 = sp.lambdify(nf, beta1.subs(su3))
check('Q4e beta1(SU3) > 0 for n_f <= 8 and < 0 for n_f >= 9', all(b1(k) > 0 for k in range(0, 9)) and all(b1(k) < 0 for k in range(9, 17)))

# ------------------------------------------------------------------ Q5  running coupling numbers (n_f = 5, alpha_s(M_Z) = 0.1180)
mp.mp.dps = 30
MZ = mp.mpf('91.1876'); aZ = mp.mpf('0.1180')
b0 = mp.mpf(23) / 3; b1v = mp.mpf(116) / 3   # 102 - 38*5/3 = 116/3
def a1loop(Q):
    return aZ / (1 + b0 * aZ / (4 * mp.pi) * mp.log(Q**2 / MZ**2))
def a2loop_exact(Q):
    # mu^2 d a/d mu^2 = -b0 a^2/(4 pi) - b1 a^3/(4 pi)^2 is separable:
    # ln(Q^2/MZ^2) = (4 pi/b0) [ 1/a - c ln((1+c a)/a) ]_{aZ}^{a},  c = b1/(4 pi b0)   (exact two-loop running)
    c = b1v / (4 * mp.pi * b0)
    F = lambda a: (4 * mp.pi / b0) * (1 / a - c * mp.log((1 + c * a) / a))
    return mp.findroot(lambda a: F(a) - F(aZ) - mp.log(Q**2 / MZ**2), a1loop(Q))
L1 = MZ * mp.e**(-2 * mp.pi / (b0 * aZ))       # one-loop Lambda: alpha = 4 pi/(b0 ln(Q^2/Lambda^2))
def a2loop_formula(Q, Lam):
    L = mp.log(Q**2 / Lam**2)
    return 4 * mp.pi / (b0 * L) * (1 - b1v / b0**2 * mp.log(L) / L)
Lam2 = mp.findroot(lambda La: a2loop_formula(MZ, La) - aZ, mp.mpf('0.2'))
print('     n_f=5: beta0 = 23/3, beta1 = 116/3; Lambda(1-loop) = %s GeV; Lambda(2-loop, truncated formula) = %s GeV' % (mp.nstr(L1, 6), mp.nstr(Lam2, 6)))
tab = []
for Q in (5, 10, 20, 50, 91.1876, 200, 500, 1000):
    Q = mp.mpf(Q)
    tab.append((Q, a1loop(Q), a2loop_exact(Q), a2loop_formula(Q, Lam2)))
    print('     Q = %8s GeV: alpha_s 1-loop = %s ; 2-loop exact ODE = %s ; 2-loop truncated formula = %s ; 1/alpha_s(1-loop) = %s' %
          (mp.nstr(Q, 6), mp.nstr(tab[-1][1], 5), mp.nstr(tab[-1][2], 5), mp.nstr(tab[-1][3], 5), mp.nstr(1 / tab[-1][1], 6)))
check('Q5a one-loop alpha_s(10 GeV) = 0.1731 (n_f=5 from 0.1180)', abs(a1loop(10) - mp.mpf('0.17309')) < 2e-5, mp.nstr(a1loop(10), 6))
check('Q5b 1/alpha_s(Q) linear in ln Q^2 with slope beta0/(4 pi) = 0.61009', abs((1 / a1loop(1000) - 1 / a1loop(10)) / mp.log(mp.mpf(1000)**2 / 100) - b0 / (4 * mp.pi)) < 1e-12, mp.nstr(b0 / (4 * mp.pi), 6))
check('Q5c truncated 2-loop formula within 1.5% of the exact 2-loop ODE for 5 <= Q <= 1000 GeV',
      all(abs(r[3] / r[2] - 1) < 0.015 for r in tab), 'max dev %s' % mp.nstr(max(abs(r[3] / r[2] - 1) for r in tab), 3))

# ------------------------------------------------------------------ Q6  CRS Yukawa-model MSbar pdf (VF-FRO-10)
mq, mpr, ms = mp.mpf('0.3'), mp.mpf('1.0'), mp.mpf('1.5')
def Delta(xi):
    return xi * ms**2 + (1 - xi) * mq**2 - xi * (1 - xi) * mpr**2
def fren(xi, mu):  # in units of a_lambda
    return (1 - xi) * (mp.log(mu**2 / Delta(xi)) - 1 + (mq + xi * mpr)**2 / Delta(xi))
check('Q6a Delta(xi) > 0 on [0,1] for the CRS masses (stable target)', all(Delta(mp.mpf(k) / 200) > 0 for k in range(201)))
zeros = []
prev = None
for k in range(1, 1000):
    xv = mp.mpf(k) / 1000
    s = fren(xv, mp.mpf('0.8')) < 0
    if prev is not None and s != prev: zeros.append(xv)
    prev = s
x08 = mp.findroot(lambda xv: fren(xv, mp.mpf('0.8')), mp.mpf('0.26'))
x12 = mp.findroot(lambda xv: fren(xv, mp.mpf('1.2')), mp.mpf('0.57'))
check('Q6b mu = 0.8 GeV: single sign change at xi = 0.265, negative on (0.265, 1) (OTHERS grid 0.02..0.98 reports [0.28, 0.98])',
      len(zeros) == 1 and abs(x08 - mp.mpf('0.265')) < 0.002 and fren(mp.mpf('0.999'), mp.mpf('0.8')) < 0, 'zero at %s' % mp.nstr(x08, 4))
check('Q6b2 mu = 1.2 GeV: negative on (%s, 1)' % mp.nstr(x12, 3), fren(mp.mpf('0.999'), mp.mpf('1.2')) < 0 and fren(x12 - mp.mpf('0.01'), mp.mpf('1.2')) > 0)
check('Q6c at mu = 2.5 GeV the pdf is positive for all 0 < xi < 1', all(fren(mp.mpf(k) / 400, mp.mpf('2.5')) > 0 for k in range(1, 400)))
mustar = ms * mp.e**(mp.mpf(1) / 2 * (1 - (mq + mpr)**2 / ms**2))
check('Q6d xi -> 1 sign-change scale mu* = m_s exp{[1-(m_q+m_p)^2/m_s^2]/2} = 1.70 GeV', abs(mustar - mp.mpf('1.70')) < 0.006, mp.nstr(mustar, 5))
print('     CRS curves (units a_lambda): xi, f(mu=0.8), f(mu=1.2), f(mu=2.5)')
for k in (5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95):
    xv = mp.mpf(k) / 100
    print('       %4s  %9s  %9s  %9s' % (mp.nstr(xv, 2), mp.nstr(fren(xv, mp.mpf('0.8')), 4), mp.nstr(fren(xv, mp.mpf('1.2')), 4), mp.nstr(fren(xv, mp.mpf('2.5')), 4)))

# ------------------------------------------------------------------ Q7  triangle remainder data (fig:appN-triangle-remainder; VF-REF-2/3)
mp.mp.dps = 40
def Phi1(t):
    rho = 2 / (1 - 2 * t + mp.sqrt(1 - 4 * t))
    return (4 * mp.polylog(2, -rho * t) + mp.log(rho * t)**2 + mp.pi**2 / 3) / mp.sqrt(1 - 4 * t)
def rem_over_t(t):
    s = 2 * t / (1 - 2 * t + mp.sqrt(1 - 4 * t))      # s = m^2 / Qt^2
    Qt2 = t / s                                       # Q^2 = 1, m^2 = t
    r = Phi1(t) - (mp.log(Qt2 / t)**2 + mp.pi**2 / 3) / Qt2
    return r / t
def nlp_I(t):
    L = mp.log(1 / t)
    return (Phi1(t) - L**2 - mp.pi**2 / 3) / t
print('     triangle: t, Q^2 r/t (exact), -4 + t(L^2-15+pi^2/3), NLP coefficient of Q^2 I: (Q^2 I - L^2 - pi^2/3)/t, 2L^2-4L-4+2pi^2/3')
okr = True
for t in ('1e-5', '3e-5', '1e-4', '3e-4', '1e-3', '3e-3', '0.01', '0.02', '0.05', '0.1', '0.15', '0.2'):
    t = mp.mpf(t); L = mp.log(1 / t)
    y = rem_over_t(t); ya = -4 + t * (L**2 - 15 + mp.pi**2 / 3)
    z = nlp_I(t); za = 2 * L**2 - 4 * L - 4 + 2 * mp.pi**2 / 3
    print('       %7s  %10s  %10s  %10s  %10s' % (mp.nstr(t, 2), mp.nstr(y, 6), mp.nstr(ya, 6), mp.nstr(z, 6), mp.nstr(za, 6)))
    if t <= mp.mpf('1e-3'): okr &= abs(y - ya) < 50 * t**2 * L**2 + mp.mpf('1e-30')
check('Q7 remainder Q^2 r/t -> -4 with correction t(L^2-15+pi^2/3) (no logarithm at NLP)', okr)

# ------------------------------------------------------------------ Q8  Glauber direction e_G (VF-REF-7) and future/past identity (VF-REF-11)
lp, lm, l1, l2, m, t, f, s = sp.symbols('l_p l_m l_1 l_2 m t f sigma', real=True)
def dot(a, b):  # (plus, minus, T1, T2)
    return a[0] * b[1] + a[1] * b[0] - a[2] * b[2] - a[3] * b[3]
eG = (-1, 1, 0, 0); nA = (1, 0, 0, 0); nB = (0, 1, 0, 0)
lvec = (lp, lm, l1, l2)
shifted = tuple(lvec[i] + sp.I * t * s * f * eG[i] for i in range(4))
expr = sp.expand(dot(shifted, shifted) - m**2 - ((dot(lvec, lvec) - m**2 + 2 * t**2 * f**2 * s**2) + 2 * sp.I * t * s * f * (lp - lm)))
check('Q8a e_G = n_B - n_A: e_G^2 = -2, n_A.e_G = 1, n_B.e_G = -1, (l + i t s f e_G)^2 - m^2 identity', dot(eG, eG) == -2 and dot(nA, eG) == 1 and dot(nB, eG) == -1 and expr == 0)
k, e0, Qa = sp.symbols('k epsilon Q_a', real=True)
lhs = sp.I * Qa / (k + sp.I * e0) + sp.I * (-Qa) * (1 / (k + sp.I * e0) - 1 / (k - sp.I * e0))
check('Q8b iQ_a/(k+i0) + iQ_s[1/(k+i0) - 1/(k-i0)] = iQ_a/(k-i0) for Q_s = -Q_a', sp.simplify(lhs - sp.I * Qa / (k - sp.I * e0)) == 0)

print('SUMMARY: %d/%d checks pass' % (sum(RES), len(RES)))
