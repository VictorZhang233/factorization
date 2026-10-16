# -*- coding: utf-8 -*-
"""
s8_review.py -- Ch20 (heavy): second, independent re-derivation of the formulas printed in the revised chapter.
Different methods from s1-s7 wherever possible:
  A  B -> D pi: naive factorization N, kinematics (E_pi, w, HQ-limit prefactor) with PDG masses
  B  colour transparency: eikonal dipole expansion (sympy series in a book-keeping parameter)
  C  QCDF: RG origin of 12 ln(m_b/mu) (sympy, general N_c); a_{1,I}, a_{2,I} numbers with alpha_s(m_b) from
     an independent two-loop running (RK4 in ln mu^2)
  D  g(x) Gegenbauer integrals (mpmath quad, own implementation of g and C_n^{3/2})
  E  annihilation: exact integral 36 int int x xb yb/(1 - x yb) = 18 (pi^2/3 - 3) (sympy, analytic), the
     X_A replacements for A_1^i and A_3^f (sympy), X_H divergence
  F  inclusive: p_X^2 expansion, shape-function moments from <k k> = (lambda_1/3)(g - v v), MW total rate,
     lambda_2 from the B*-B splitting
  G  NRQCD: LO widths from Im f and <O_1> = 2 N_c |psi(0)|^2; 1S0 -> gamma gamma trace with explicit 4x4 Dirac
     matrices (numpy); exact-in-eps c_v (sympy) from the Feynman-parameter representation re-derived by hand
     (r0, r2 inserted, integrals done independently); numerical check of the analytic continuation of the
     a-integral of the r0 term at eps < -1/2; Sommerfeld expansion.
Run: python3 -I s8_review.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w23common import *
import numpy as np

ck = Check('s8_review: independent re-derivation of the formulas of the revised Ch20')

# ----------------------------------------------------------------------------------------------- A
mB, mD = 5.27966, 1.86966                     # PDG 2024: B0, D+ (GeV)
Epi = (mB**2 - mD**2) / (2 * mB)
w = (mB**2 + mD**2) / (2 * mB * mD)
pref = (mB + mD) / (2 * np.sqrt(mB * mD))
print('   E_pi = %.4f GeV, w = %.4f, (mB+mD)/(2 sqrt(mB mD)) = %.4f' % (Epi, w, pref))
ck('A1 E_pi = 2.309 GeV, w = 1.589, prefactor 1.138', abs(Epi - 2.309) < 5e-4 and abs(w - 1.589) < 5e-4 and abs(pref - 1.138) < 5e-4)
MB, MD, Fz, fpi = sp.symbols('m_B m_D F f_pi', positive=True)
# <pi^-| dbar gamma_mu P_L u |0> = -(1/2) (-i f p_mu) = (i/2) f p_mu ; q.<D|V|B> = (mB^2 - mD^2) F0(0); P_L -> 1/2
first = sp.I / 2 * fpi
second = sp.Rational(1, 2) * (MB**2 - MD**2) * Fz
N = sp.simplify(first * second)
Epi_s = (MB**2 - MD**2) / (2 * MB)
ck('A2 N F = (i/2) m_B E_pi f_pi F', sp.simplify(N - sp.I / 2 * MB * Epi_s * fpi * Fz) == 0)
# (p+p').q = p^2 - p'^2 with q = p - p'
p0, p1, p2, p3, r0_, r1_, r2_, r3_ = sp.symbols('p0 p1 p2 p3 r0 r1 r2 r3')
dot4 = lambda a, b: a[0] * b[0] - a[1] * b[1] - a[2] * b[2] - a[3] * b[3]
P = (p0, p1, p2, p3); Pp = (r0_, r1_, r2_, r3_)
q = tuple(P[i] - Pp[i] for i in range(4)); s = tuple(P[i] + Pp[i] for i in range(4))
ck('A3 (p+p).q = p^2 - p^2 (F_+ term drops out)', sp.expand(dot4(s, q) - dot4(P, P) + dot4(Pp, Pp)) == 0)
# w at q^2 = 0 : q^2 = mB^2 + mD^2 - 2 mB mD w
ww = sp.symbols('w')
ck('A4 w(q^2=0) = (mB^2 + mD^2)/(2 mB mD)', sp.simplify(sp.solve(MB**2 + MD**2 - 2 * MB * MD * ww, ww)[0] - (MB**2 + MD**2) / (2 * MB * MD)) == 0)

# ----------------------------------------------------------------------------------------------- B
t, x = sp.symbols('t x', positive=True)
k = sp.symbols('k0:4'); pp = sp.symbols('P0:4'); l = sp.symbols('l0:4')
pvec = list(pp); kvec = list(k); lvec = list(l)
p1v = [x * pvec[i] + t * lvec[i] for i in range(4)]
p2v = [(1 - x) * pvec[i] - t * lvec[i] for i in range(4)]
def d(a, b): return a[0] * b[0] - a[1] * b[1] - a[2] * b[2] - a[3] * b[3]
J = [p1v[m] / d(p1v, kvec) - p2v[m] / d(p2v, kvec) for m in range(4)]
J1 = [sp.series(J[m], t, 0, 2).removeO() for m in range(4)]
pred = [(1 / x + 1 / (1 - x)) / d(pvec, kvec) * (t * lvec[m] - pvec[m] * t * d(lvec, kvec) / d(pvec, kvec)) for m in range(4)]
ck('B1 eikonal dipole: zeroth order vanishes, first order = (1/x + 1/xb)[l - p (l.k)/(p.k)]/(p.k)',
   all(sp.simplify(J1[m] - pred[m]) == 0 for m in range(4)))
ck('B2 dipole remainder is conserved: k.J1 = 0', sp.simplify(d(kvec, pred)) == 0)

# ----------------------------------------------------------------------------------------------- C
Nc, a_s, C1, C2, L = sp.symbols('N_c alpha_s C_1 C_2 L')
gam = sp.Matrix([[-6 / Nc, 6], [6, -6 / Nc]])
Cv = sp.Matrix([C1, C2])
dC = a_s / (4 * sp.pi) * gam.T * Cv
CF = (Nc**2 - 1) / (2 * Nc)
d_a1 = dC[0] + dC[1] / Nc
ck('C1 d(C1 + C2/N)/dln mu = (as/4pi)(12 C_F/N) C2', sp.simplify(d_a1 - a_s / (4 * sp.pi) * 12 * CF / Nc * C2) == 0)
d_a2 = dC[1] + dC[0] / Nc
ck('C2 d(C2 + C1/N)/dln mu = (as/4pi)(12 C_F/N) C1', sp.simplify(d_a2 - a_s / (4 * sp.pi) * 12 * CF / Nc * C1) == 0)
# derivative of (C2/N)(C_F as/4pi) 12 ln(m_b/mu) wrt ln mu = -(C2/N)(C_F as/4pi) 12
ck('C3 the 12 ln(m_b/mu) term cancels it for any N_c', sp.simplify(d_a1 + C2 / Nc * CF * a_s / (4 * sp.pi) * (-12)) == 0)
ev = gam.eigenvals()
ck('C4 eigenvalues +-6(N-+1)/N', set(sp.simplify(e) for e in ev) == {sp.simplify(6 * (Nc - 1) / Nc), sp.simplify(-6 * (Nc + 1) / Nc)})
# two-loop running alpha_s from M_Z (nf = 5), RK4 in ln mu^2
def beta_fn(a, nf=5):
    b0 = 11 - 2 * nf / 3.; b1 = 102 - 38 * nf / 3.
    return -(b0 / (4 * np.pi)) * a**2 - (b1 / (4 * np.pi)**2) * a**3
def run(a0, mu0, mu1, n=4000):
    tt = np.log(mu0**2); h = (np.log(mu1**2) - tt) / n; a = a0
    for _ in range(n):
        k1 = beta_fn(a); k2 = beta_fn(a + h * k1 / 2); k3 = beta_fn(a + h * k2 / 2); k4 = beta_fn(a + h * k3)
        a += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return a
amb = run(0.1180, 91.1876, 4.2)
print('   alpha_s(4.2 GeV), two-loop from 0.1180: %.4f' % amb)
ck('C5 alpha_s(m_b = 4.2 GeV) = 0.223', abs(amb - 0.223) < 1e-3)
c1v, c2v = 1.081, -0.190
fac = (4 / 3) * amb / (4 * np.pi)
Vpi = -18.5 - 3j * np.pi
a1 = c1v + c2v / 3 * (1 + fac * Vpi); a2 = c2v + c1v / 3 * (1 + fac * Vpi)
print('   C_F as/4pi = %.4f ; a1I = %.4f%+.4fi ; a2I = %.4f%+.4fi ; C2 + C1/3 = %.4f' % (fac, a1.real, a1.imag, a2.real, a2.imag, c2v + c1v / 3))
ck('C6 a1I ~ 1.045 + 0.014 i, a2I ~ 0.012 - 0.080 i, tree a2 = 0.170',
   abs(a1 - (1.045 + 0.014j)) < 1.5e-3 and abs(a2 - (0.012 - 0.080j)) < 1.5e-3 and abs(c2v + c1v / 3 - 0.170) < 1e-3)
ck('C7 C_+ = 0.891 < 1 < C_- = 1.271 at mu = m_b', abs(c1v + c2v - 0.891) < 1e-9 and abs(c1v - c2v - 1.271) < 1e-9)

# ----------------------------------------------------------------------------------------------- D
mp.mp.dps = 30
def g(xv):
    xv = mp.mpf(xv); xb = 1 - xv
    def br(y):
        return 2 * mp.polylog(2, y) - mp.log(y)**2 + 2 * mp.log(y) / (1 - y) - (3 + 2j * mp.pi) * mp.log(y)
    return 3 * ((1 - 2 * xv) / (1 - xv) * mp.log(xv) - 1j * mp.pi) + br(xv) - br(xb)
C1g = lambda u: 3 * u
C2g = lambda u: mp.mpf(3) / 2 * (5 * u**2 - 1)
I0 = mp.quad(lambda xv: g(xv) * 6 * xv * (1 - xv), [0, 0.5, 1])
I1 = mp.quad(lambda xv: g(xv) * 6 * xv * (1 - xv) * C1g(2 * xv - 1), [0, 0.5, 1])
I2 = mp.quad(lambda xv: g(xv) * 6 * xv * (1 - xv) * C2g(2 * xv - 1), [0, 0.5, 1])
print('   int g 6x xb =', mp.nstr(I0, 15), '; alpha_1 coeff =', mp.nstr(I1, 15), '; alpha_2 coeff =', mp.nstr(I2, 15))
ck('D1 int g Phi = -1/2 - 3 i pi + (11/2 - 3 i pi) alpha_1 - 21/20 alpha_2',
   abs(I0 - (-0.5 - 3j * mp.pi)) < 1e-15 and abs(I1 - (5.5 - 3j * mp.pi)) < 1e-15 and abs(I2 - (-mp.mpf(21) / 20)) < 1e-15)
ck('D2 V_pi(mu = m_b, asymptotic) = -18.5 - 3 i pi', abs(-18 + I0 - (-18.5 - 3j * mp.pi)) < 1e-15)

# ----------------------------------------------------------------------------------------------- E
X, Y = sp.symbols('x y', positive=True)
inner = sp.integrate(X * (1 - X) * (1 - Y) / (1 - X * (1 - Y)), (X, 0, 1))
Ifin = sp.simplify(sp.integrate(sp.simplify(inner), (Y, 0, 1)))
print('   int int x xb yb/(1 - x yb) =', Ifin, '=', sp.N(Ifin, 15))
ck('E1 36 int int x xb yb/(1 - x yb) = 18 (pi^2/3 - 3) (exact)', sp.simplify(36 * Ifin - 18 * (sp.pi**2 / 3 - 3)) == 0)
XA, r = sp.symbols('X_A r')
A1i = 18 * (sp.pi**2 / 3 - 3) + 18 * (XA - 1) + 2 * r**2 * XA**2
ck('E2 A_1^i/(pi as) = 18 (X_A - 4 + pi^2/3) + 2 r^2 X_A^2', sp.simplify(A1i - (18 * (XA - 4 + sp.pi**2 / 3) + 2 * r**2 * XA**2)) == 0)
ck('E3 x/(1-x) = 1/(1-x) - 1 ; x(1+xb)/xb = 1/xb - xb ; yb(1+y)/y = 1/y - y',
   sp.simplify(X / (1 - X) - (1 / (1 - X) - 1)) == 0 and sp.simplify(X * (2 - X) / (1 - X) - (1 / (1 - X) - (1 - X))) == 0
   and sp.simplify((1 - Y) * (1 + Y) / Y - (1 / Y - Y)) == 0)
# A_3^f: term 1: r1 int dx 6 x xb 2(1+xb)/xb^2 int dy/y = 12 r1 (X_A - 1/2) X_A (each divergent int -> X_A)
term = 12 * r * (XA - sp.Rational(1, 2)) * XA
ck('E4 each A_3^f term = 6 pi as r (2 X_A^2 - X_A)', sp.simplify(term - 6 * r * (2 * XA**2 - XA)) == 0)
dl = sp.symbols('delta', positive=True)
ck('E5 X_H with Phi_p = 1: int_0^{1-delta} dy/(1-y) = ln(1/delta)', sp.simplify(sp.integrate(1 / (1 - Y), (Y, 0, 1 - dl)) - sp.log(1 / dl)) == 0)
ck('E6 twist-2 hard-spectator convolution <ybar^-1> = 3 for the asymptotic DA', sp.integrate(6 * Y * (1 - Y) / (1 - Y), (Y, 0, 1)) == 3)
ck('E7 default ln(m_B/Lambda_h) = 2.36', abs(np.log(5.280 / 0.5) - 2.357) < 1e-3)

# ----------------------------------------------------------------------------------------------- F
mb, Eg, k0, k3, k1, k2 = sp.symbols('m_b E_gamma k0 k3 k1 k2', real=True)
pX = [mb + k0 - Eg, k1, k2, k3 + Eg]          # q = (E, 0, 0, -E) along -z ; p_b = m_b v + k
pX2 = sp.expand(pX[0]**2 - pX[1]**2 - pX[2]**2 - pX[3]**2)
ref = sp.expand(mb**2 - 2 * mb * Eg + 2 * mb * k0 - 2 * Eg * (k0 + k3) + (k0**2 - k1**2 - k2**2 - k3**2))
ck('F1 p_X^2 = m_b^2 - 2 m_b E + 2 m_b k0 - 2 E (k0 + k3) + k^2', sp.simplify(pX2 - ref) == 0)
De = sp.symbols('Delta')                       # 2E = m_b + Delta, Delta ~ Lambda
lead = sp.expand(ref.subs(Eg, (mb + De) / 2))
lead_mb = sp.expand(sum(term for term in lead.as_ordered_terms() if sp.degree(term, mb) >= 1))
ck('F2 O(m_b Lambda) part = m_b (m_b - 2E + k0 - k3)', sp.simplify(lead_mb - mb * (-De + k0 - k3)) == 0)
lam1 = sp.symbols('lambda_1')
gmat = sp.diag(1, -1, -1, -1)
v = sp.Matrix([1, 0, 0, 0]); nA = sp.Matrix([1, 0, 0, -1]) / sp.sqrt(2)     # n_A: (n^0, n^3) = (1, -1)/sqrt2 -> n.k = k^-
kk = lam1 / 3 * (gmat - v * v.T)          # <k^mu k^nu> (upper indices)
low = lambda vec: gmat * vec
nAk2 = (low(nA).T * kk * low(nA))[0]
nAv = (low(nA).T * v)[0]
ck('F3 <omega^2> = <(n_A.k)^2>/(n_A.v)^2 = -lambda_1/3', sp.simplify(nAk2 / nAv**2 + lam1 / 3) == 0)
ck('F4 trace: g_{mu nu}<k k> = lambda_1, v_mu <k k> = 0', sp.simplify((gmat * kk).trace() - lam1) == 0 and sp.simplify((low(v).T * kk)) == sp.zeros(1, 4))
lam2, m = sp.symbols('lambda_2 m', positive=True)
Kb = -lam1 / (2 * m**2); Gb = -3 * lam2 / (2 * m**2); Eb = Kb + Gb
ck('F5 MW (5.11): 1 + 5E - 6K - 2G = 1 + (lambda_1 - 9 lambda_2)/(2 m^2)', sp.simplify(1 + 5 * Eb - 6 * Kb - 2 * Gb - (1 + (lam1 - 9 * lam2) / (2 * m**2))) == 0)
mBs, mB0 = 5.32475, 5.27966
l2 = (mBs**2 - mB0**2) / 4
print('   lambda_2 = %.4f GeV^2 ; -9 lambda_2/(2 m_b^2) at m_b = 4.8: %.4f' % (l2, -9 * l2 / (2 * 4.8**2)))
ck('F6 lambda_2 ~ 0.12 GeV^2, -9 lambda_2/(2 m_b^2) ~ -2.3%', abs(l2 - 0.12) < 0.005 and abs(-9 * l2 / (2 * 4.8**2) + 0.023) < 1e-3)
pq = sp.symbols('p2', positive=True)
ck('F7 time dilation <m/E> = 1 - p^2/(2m^2) + O(p^4)', sp.simplify(sp.series(m / sp.sqrt(m**2 + pq), pq, 0, 2).removeO() - (1 - pq / (2 * m**2))) == 0)

# ----------------------------------------------------------------------------------------------- G
alpha, eQ, psi0, NcS, mQ = sp.symbols('alpha e_Q psi0 N_c m_Q', positive=True)
O1 = 2 * NcS * psi0**2
G_ee = 2 * (sp.pi * eQ**2 * alpha**2 / 3) * O1 / mQ**2
G_gg = 2 * (sp.pi * eQ**4 * alpha**2) * O1 / mQ**2
M = 2 * mQ
ck('G1 2 Im f_ee <O_1>/m^2 = (16 pi N_c/3) e_Q^2 alpha^2 |psi0|^2/M^2', sp.simplify(G_ee - 16 * sp.pi * NcS / 3 * eQ**2 * alpha**2 * psi0**2 / M**2) == 0)
ck('G2 2 Im f_gg <O_1>/m^2 = 16 pi N_c e_Q^4 alpha^2 |psi0|^2/M^2', sp.simplify(G_gg - 16 * sp.pi * NcS * eQ**4 * alpha**2 * psi0**2 / M**2) == 0)
R0 = sp.symbols('R0', positive=True)
ck('G3 R(0) forms: N_c e_Q^2 alpha^2 |R|^2/(3 m^2) and 4 N_c e_Q^4 alpha^2 |R|^2/M^2',
   sp.simplify(G_ee.subs(psi0, R0 / sp.sqrt(4 * sp.pi)) - NcS * eQ**2 * alpha**2 * R0**2 / (3 * mQ**2)) == 0
   and sp.simplify(G_gg.subs(psi0, R0 / sp.sqrt(4 * sp.pi)) - 4 * NcS * eQ**4 * alpha**2 * R0**2 / M**2) == 0)
# width from the amplitude: Gamma = (1/2M)(1/8pi) |M|^2_avg with |M|^2_avg = (2M/(4m^2)) N_c |psi|^2 e^4 e_Q^2 * 8 m^2 * (4/3) M^2 / M^4
e2 = 4 * sp.pi * alpha
Mavg = (2 * M / (4 * mQ**2)) * NcS * psi0**2 * e2**2 * eQ**2 * 8 * mQ**2 * sp.Rational(4, 3) * M**2 / M**4
Gam_amp = Mavg / (2 * M) / (8 * sp.pi)
ck('G4 amplitude route: Gamma = N_c e^4 e_Q^2 |psi|^2/(3 pi M^2) = VF-NRQ-2', sp.simplify(Gam_amp - NcS * e2**2 * eQ**2 * psi0**2 / (3 * sp.pi * M**2)) == 0 and sp.simplify(Gam_amp - G_ee) == 0)
# 1S0 -> gamma gamma: explicit 4x4 Dirac matrices
I2 = np.eye(2); Z2 = np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
G0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
Gs = [G0] + [np.block([[Z2, s_], [-s_, Z2]]) for s_ in (sx, sy, sz)]
G5 = 1j * Gs[0] @ Gs[1] @ Gs[2] @ Gs[3]
met = np.diag([1., -1, -1, -1])
def sl(vec): vl = met @ vec; return sum(Gs[i] * vl[i] for i in range(4))
mq = 1.3
pv = np.array([mq, 0, 0, 0.])
Pi0 = (sl(pv) + mq * np.eye(4)) @ G5 @ (sl(pv) - mq * np.eye(4)) / (2 * np.sqrt(2) * mq)
Pi0bar = Gs[0] @ Pi0.conj().T @ Gs[0]
ck('G5 Tr[Pibar_0 Pi_0] = -4 m^2', abs(np.trace(Pi0bar @ Pi0) + 4 * mq**2) < 1e-12)
k1v = np.array([mq, 0.3 * mq, 0.4 * mq, np.sqrt(1 - 0.09 - 0.16) * mq]); k2v = 2 * pv - k1v
def SQ(qv): return (sl(qv) + mq * np.eye(4)) / (qv @ met @ qv - mq**2)   # propagator without the factor i
T = np.zeros((4, 4), complex)
for mu in range(4):
    for nu in range(4):
        T[mu, nu] = np.trace((Gs[nu] @ SQ(pv - k1v) @ Gs[mu] + Gs[mu] @ SQ(pv - k2v) @ Gs[nu]) @ Pi0)
import itertools
def eps4(a, b, c, dd):
    perm = [a, b, c, dd]
    if len(set(perm)) < 4: return 0
    sgn = 1
    for i in range(4):
        for j in range(i + 1, 4):
            if perm[i] > perm[j]: sgn = -sgn
    return sgn
k1l = met @ k1v; k2l = met @ k2v
Tpred = np.zeros((4, 4), complex)
for mu in range(4):
    for nu in range(4):
        Tpred[mu, nu] = 1j * np.sqrt(2) * sum(eps4(mu, nu, a, b) * k1l[a] * k2l[b] for a in range(4) for b in range(4)) / mq**2
ck('G6 Compton-type trace = i sqrt2 eps^{mu nu a b} k1_a k2_b/m^2 (eps^{0123} = +1)', np.allclose(T, Tpred, atol=1e-10))
# polarization sum: T^{mu nu} T*_{mu nu} with lowered indices
Tlow = met @ T @ met
polsum = np.sum(T * Tlow.conj()).real
k1k2 = k1v @ met @ k2v
ck('G7 sum over photon polarizations = 4 (k1.k2)^2/m^4', abs(polsum - 4 * k1k2**2 / mq**4) < 1e-9)
# c_v exact in eps from the hand-derived Feynman-parameter representation
ep = sp.symbols('epsilon')
D = 4 - 2 * ep
r0 = lambda av: -2 * (2 - (1 - ep) * av**2)          # in units of m^2 (overall m^2 factored)
r2 = 2 * (1 - ep)**2 / (2 - ep)
# a-integrals:  int_{-1}^{1} da (1-|a|) |a|^p = 2/((p+1)(p+2))
Ia = lambda pw: 2 / ((pw + 1) * (pw + 2))
# delta_V/(a_s e^{eps gE} (mu^2/m^2)^eps) = int da (1-|a|) [ -(r0/2) Gamma(1+eps) a^{-2-2eps} + (D/4) r2 Gamma(eps) a^{-2eps} ]
dV = (-(sp.Rational(1, 2)) * sp.gamma(1 + ep) * (-2) * (2 * Ia(-2 - 2 * ep) - (1 - ep) * Ia(-2 * ep))
      + D / 4 * r2 * sp.gamma(ep) * Ia(-2 * ep))
dV_print = sp.gamma(ep) * (1 - ep) / (1 - 2 * ep) + sp.gamma(1 + ep) * (2 / (ep * (1 + 2 * ep)) - 1 / (1 - 2 * ep))
ck('G8 hand-derived delta_V equals the printed closed form (exact in eps)', sp.simplify(sp.gammasimp(dV - dV_print)) == 0)
dZ = -sp.gamma(ep) * (3 - 2 * ep) / (1 - 2 * ep)
tot = sp.gammasimp(sp.simplify(dV_print + dZ))
ck('G9 delta_V + delta Z_2 = -8 Gamma(1+eps)/(1 - 4 eps^2) exactly', sp.simplify(sp.gammasimp(tot + 8 * sp.gamma(1 + ep) / (1 - 4 * ep**2))) == 0)
Lm = sp.symbols('L')
pref_s = sp.exp(ep * sp.EulerGamma) * sp.exp(ep * Lm)        # e^{eps gE} (mu^2/m^2)^eps, L = ln(mu^2/m^2)
ser_V = sp.series(pref_s * dV_print, ep, 0, 1).removeO()
ser_Z = sp.series(pref_s * dZ, ep, 0, 1).removeO()
ck('G10 expansions: delta_V = 3/eps - 4 + 3L, delta Z_2 = -(3/eps + 4 + 3L)',
   sp.simplify(ser_V - (3 / ep - 4 + 3 * Lm)) == 0 and sp.simplify(ser_Z + (3 / ep + 4 + 3 * Lm)) == 0)
ck('G11 c_v - 1 -> -8 a_s = -2 C_F alpha_s/pi', sp.limit(-8 * sp.gamma(1 + ep) / (1 - 4 * ep**2), ep, 0) == -8 and sp.simplify(-8 * 1 / (4 * sp.pi) * sp.pi) == -2)
# pole bookkeeping at mu = m: r2-term = 1/eps_UV + 1 ; r0-term = 2/eps_IR - 5
s_r2 = sp.series(sp.exp(ep * sp.EulerGamma) * sp.gamma(ep) * (1 - ep) / (1 - 2 * ep), ep, 0, 1).removeO()
s_r0 = sp.series(sp.exp(ep * sp.EulerGamma) * sp.gamma(1 + ep) * (2 / (ep * (1 + 2 * ep)) - 1 / (1 - 2 * ep)), ep, 0, 1).removeO()
ck('G12 r2 term = 1/eps + 1, r0 term = 2/eps - 5 (mu = m)', sp.simplify(s_r2 - (1 / ep + 1)) == 0 and sp.simplify(s_r0 - (2 / ep - 5)) == 0)
# numerical check of the analytic continuation of the r0 a-integral: at eps = -0.8 the integral converges
epv = mp.mpf('-0.8')
num = mp.quad(lambda av: 2 * (1 - av) * av**(-2 - 2 * epv) * (2 - (1 - epv) * av**2), [0, 1])
ana = 2 * 2 / ((-1 - 2 * epv) * (-2 * epv)) - (1 - epv) * 2 / ((1 - 2 * epv) * (2 - 2 * epv))
ck('G13 r0 a-integral: numerical (eps = -0.8) = analytic continuation', abs(num - ana) < 1e-12, '%s vs %s' % (mp.nstr(num, 12), mp.nstr(ana, 12)))
# Sommerfeld: X/(1 - e^{-X}) = 1 + X/2 + ..., X = pi C_F as/beta ; amplitude pi C_F as/(4 beta) doubled
Xs = sp.symbols('X')
ck('G14 Sommerfeld factor = 1 + X/2 + O(X^2), X = pi C_F as/beta (= 2 x amplitude term pi^2/(4 beta) (C_F as/pi))',
   sp.simplify(sp.series(Xs / (1 - sp.exp(-Xs)), Xs, 0, 2).removeO() - (1 + Xs / 2)) == 0)
ck('G15 |c_v|^2 = 1 - 4 C_F as/pi = 1 - 16 as/(3 pi) for N_c = 3; 16*0.25/(3 pi) = 0.42', abs(16 * 0.25 / (3 * np.pi) - 0.4244) < 1e-3)

ok = ck.summary()
sys.exit(0 if ok else 1)
