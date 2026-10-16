# -*- coding: utf-8 -*-
"""
s4_bbns.py -- Part (4): QCD factorization (BBNS) for B -> M1 M2: power counting of the two
leading-power terms, scale-independence of the O(alpha_s) vertex term (origin of 12 ln(m_b/mu)),
the vertex kernel convolutions (Gegenbauer coefficients), hard-spectator virtualities and endpoint
behaviour, annihilation endpoint divergences and the X_A, X_H parametrization, colour transparency.

Sources (read from the arXiv source files): BBNS NPB 606 (2001) 245 [hep-ph/0104110] eqs. (fact),
(ai), (FM), (vgegenb), (Hiexpr), (Xdef), (XAdef), (XHparam), (XAparam); Beneke-Neubert NPB 675
(2003) 333 [hep-ph/0308039] eqs. (XAdef), (XAmodel), (XHparam); BPS PRL 87 (2001) 201806.
Run:  python3 -I s4_bbns.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
import scipy.integrate as si
from mpmath import mp, polylog, quad as mquad, log as mlog, pi as mpi, mpf
mp.dps = 30

ck = Check('s4_bbns: QCDF power counting, RG of V_M, vertex kernel, spectator & annihilation endpoints')

# ======================================================================== A. power counting
Lam, mb = sp.symbols('Lambda m_b', positive=True)
F_Bpi = (Lam / mb) ** sp.Rational(3, 2)            # heavy-to-light form factor at large recoil (endpoint-suppressed)
fB = Lam ** sp.Rational(3, 2) / mb ** sp.Rational(1, 2)
fpi = Lam; lamB = Lam
termI = F_Bpi * mb ** 2 * fpi                        # F^{B->M1} m_B^2 f_M2 T^I*Phi
termII = fB * fpi * fpi * (mb / lamB)                # f_B f_M1 f_M2 T^II*Phi_B*Phi*Phi, int dxi Phi_B/xi = m_B/lambda_B
ck('form-factor term ~ hard-spectator term ~ Lambda^{5/2} m_b^{1/2}: both leading power (spectator term O(alpha_s))',
   sp.simplify(termI / termII) == 1, f'term I ~ {sp.simplify(termI)}, term II ~ {sp.simplify(termII)}')
ck('H_{M2M1} = f_B f_M1/(m_B lambda_B F^{B->M1}(0)) [...] = O(1) in the heavy-quark limit',
   sp.simplify(fB * fpi / (mb * lamB * F_Bpi)) == 1)
# heavy-to-heavy B -> D pi (BBNS 2000 eqs. (abd), (specd)): A_lead ~ G_F m_b^2 F^{B->D}(0) f_pi ~ G_F m_b^2 Lambda;
# soft remainder of spectator graphs ~ G_F alpha_s f_pi f_D f_B int dxi Phi_B/xi int deta Phi_D/eta int du Phi_pi/u
fD = Lam ** sp.Rational(3, 2) / mb ** sp.Rational(1, 2)          # heavy-meson decay constants (m_c ~ m_b scaling)
A_lead = mb ** 2 * 1 * fpi
A_spec = fpi * fD * fB * (mb / Lam) * (mb / Lam) * 1
ck('B -> D pi: A_lead ~ m_b^2 Lambda, spectator graphs ~ alpha_s m_b Lambda^2 => suppressed by Lambda/m_b (no T^II term) [BBNS 2000]',
   sp.simplify(A_spec / A_lead - Lam / mb) == 0, f'A_spec ~ {sp.simplify(A_spec)}')
# BPS: F^{B->D}(0) = (1/2)(m_D/m_B)^{1/2}(1 + m_B/m_D) xi(w) = (m_B + m_D)/(2 sqrt(m_B m_D)) xi(w)
mB, mD = sp.symbols('m_B m_D', positive=True)
ck('F^{B->D}(0) = (1/2) sqrt(m_D/m_B)(1 + m_B/m_D) xi = (m_B+m_D)/(2 sqrt(m_B m_D)) xi  [heavy-quark limit]',
   sp.simplify(sp.Rational(1, 2) * sp.sqrt(mD / mB) * (1 + mB / mD) - (mB + mD) / (2 * sp.sqrt(mB * mD))) == 0)

# ======================================================================== B. RG: 12 ln(m_b/mu) from operator mixing
# Q1 = (pbar b)_{V-A}(sbar p)_{V-A},  Q2 = (pbar_i b_j)(sbar_j p_i);  dC/dln mu = (alpha_s/4pi) gamma^T C,
# gamma0 = [[-6/N, 6],[6, -6/N]]  (eigenvalues gamma_+ = 6(N-1)/N, gamma_- = -6(N+1)/N for C_pm = C1 pm C2)
N = sp.Symbol('N_c', positive=True)
C1, C2, a4 = sp.symbols('C1 C2 a4')      # a4 = alpha_s/(4 pi)
CFN = (N ** 2 - 1) / (2 * N)
gam = sp.Matrix([[-6 / N, 6], [6, -6 / N]])
dC = a4 * gam.T * sp.Matrix([C1, C2])
ck('one-loop ADM: C_pm = C1 pm C2 have gamma_+ = 6(N-1)/N, gamma_- = -6(N+1)/N',
   sp.simplify((gam * sp.Matrix([1, 1]))[0] - 6 * (N - 1) / N) == 0 and sp.simplify((gam * sp.Matrix([1, -1]))[0] + 6 * (N + 1) / N) == 0)
cV = sp.Symbol('c_V')    # V_M = cV * ln(m_b/mu) + const  => dV/dln mu = -cV
for name, lo, coef in (('a1', C1 + C2 / N, C2), ('a2', C2 + C1 / N, C1)):
    idx_lo = sp.diff(lo, C1) * dC[0] + sp.diff(lo, C2) * dC[1]
    d_corr = a4 * CFN / N * coef * (-cV)
    sol = sp.solve(sp.expand(idx_lo + d_corr), cV)
    ck(f'mu-independence of {name} = {lo} + (C_F alpha_s/4pi)/N C V_M at O(alpha_s)  =>  V_M = 12 ln(m_b/mu) + ...  (any N_c)',
       sol == [12], f'c_V = {sol}')
ck('BBNS Wilson coefficients at mu = m_b: C1 = 1.081, C2 = -0.190 => C_+ = 0.891 < 1 < C_- = 1.271 (consistent with gamma_+ > 0 > gamma_-)',
   1.081 - 0.190 < 1 < 1.081 + 0.190)

# ======================================================================== C. vertex kernel g(x)
def g_vertex(x):
    x = mpf(x); xb = 1 - x
    def part(x, xb):
        return 2 * polylog(2, x) - mlog(x) ** 2 + 2 * mlog(x) / (1 - x) - (3 + 2j * mpi) * mlog(x)
    return 3 * ((1 - 2 * x) / (1 - x) * mlog(x) - 1j * mpi) + part(x, xb) - part(xb, x)
def conv(phi):
    return mquad(lambda x: g_vertex(x) * phi(x), [0, 0.5, 1])
C1g = lambda u: 3 * u
C2g = lambda u: mpf(3) / 2 * (5 * u * u - 1)
asym = lambda x: 6 * x * (1 - x)
I0 = conv(asym)
I1 = conv(lambda x: asym(x) * C1g(2 * x - 1))
I2 = conv(lambda x: asym(x) * C2g(2 * x - 1))
ck('int g(x) Phi_asym = -1/2 - 3 i pi   [BBNS 2001 eq. (vgegenb)]', abs(I0 - (-0.5 - 3j * mpi)) < 1e-20, f'{complex(I0):.15f}')
ck('alpha_1 coefficient: int g 6x xbar C_1^{3/2}(2x-1) = 11/2 - 3 i pi', abs(I1 - (5.5 - 3j * mpi)) < 1e-20, f'{complex(I1):.15f}')
ck('alpha_2 coefficient: int g 6x xbar C_2^{3/2}(2x-1) = -21/20', abs(I2 - (-mpf(21) / 20)) < 1e-20, f'{complex(I2):.15f}')
I0p = mquad(lambda x: g_vertex(1 - x) * asym(x), [0, 0.5, 1])
ck('symmetric DA: int g(1-x) Phi = int g(x) Phi  =>  V_pi\' = V_pi + 12 (constants -6 vs -18, NDR)', abs(I0p - I0) < 1e-20)
V_asym = complex(-18 + I0)
ck('V_M(mu = m_b, asymptotic DA) = -18.5 - 3 i pi : O(alpha_s) strong phase Im V = -3 pi (perturbative, leading power)',
   abs(V_asym - (-18.5 - 3j * np.pi)) < 1e-12)

# ======================================================================== D. hard spectator: virtualities and endpoints
# B at rest, p_B = m_B v; M1 along n: p1 = (m_B/2) n ; M2 along nbar: p2 = (m_B/2) nbar ; massless mesons.
# spectator antiquark l = xi p_B (soft, xi ~ Lambda/m_B) ends in M1 with momentum ybar p1 ;
# emitted pair of M2: x p2 (quark), xbar p2 (antiquark).
mBv = 5.28
v_ = np.array([1.0, 0, 0, 0]); p1 = mBv / 2 * NVEC; p2 = mBv / 2 * NBVEC
xi_, xv, yv = 0.07, 0.4, 0.3
l_ = xi_ * mBv * v_
kg = (1 - yv) * p1 - l_                         # spectator gluon momentum
virt_g = mdot(kg, kg)
virt_q1 = mdot(xv * p2 + kg, xv * p2 + kg)
virt_q2 = mdot((1 - xv) * p2 + kg, (1 - xv) * p2 + kg)
ck('spectator gluon virtuality k^2 = -ybar xi m_B^2 + O(xi^2 m_B^2) ~ m_b Lambda  (hard-collinear, not hard)',
   abs(virt_g - (-(1 - yv) * xi_ * mBv ** 2 + xi_ ** 2 * mBv ** 2)) < 1e-12, f'k^2 = {virt_g:.4f} GeV^2')
ck('quark propagators at the emission vertex: (x p2 + k)^2 ~ x ybar m_B^2, (xbar p2 + k)^2 ~ xbar ybar m_B^2 (hard)',
   abs(virt_q1 / (xv * (1 - yv) * mBv ** 2) - 1) < 0.3 and abs(virt_q2 / ((1 - xv) * (1 - yv) * mBv ** 2) - 1) < 0.3,
   f'{virt_q1:.3f} vs {xv*(1-yv)*mBv**2:.3f}; {virt_q2:.3f} vs {(1-xv)*(1-yv)*mBv**2:.3f}')
# twist-2 convolutions finite, twist-3 endpoint divergent
inv_xbar = si.quad(lambda x: 6 * x * (1 - x) / (1 - x), 0, 1)[0]
inv_x = si.quad(lambda x: 6 * x * (1 - x) / x, 0, 1)[0]
ck('<xbar^-1>_asym = <x^-1>_asym = 3 : twist-2 hard-spectator convolution H ~ [9 + 3 r_chi X_H] (asymptotic DAs)',
   abs(inv_xbar - 3) < 1e-12 and abs(inv_x - 3) < 1e-12)
def XH_cut(delta):
    return si.quad(lambda y: 1.0 / (1 - y), 0, 1 - delta)[0]      # Phi_p = 1 (asymptotic twist-3)
d1, d2 = 1e-3, 1e-6
ck('twist-3 spectator: X_H = int_0^1 dy Phi_p(y)/(1-y), Phi_p = 1: logarithmically divergent (= ln(1/delta) with cutoff)',
   abs(XH_cut(d1) - np.log(1 / d1)) < 1e-9 and abs(XH_cut(d2) - np.log(1 / d2)) < 1e-6)
mB_, Lh = 5.279, 0.5
ck('default X_H = X_A = ln(m_B/Lambda_h) with Lambda_h = 0.5 GeV  ~ 2.4  [BBNS 2001, BN 2003]', abs(np.log(mB_ / Lh) - 2.357) < 2e-3,
   f'ln(m_B/Lambda_h) = {np.log(mB_/Lh):.4f}')

# ======================================================================== E. annihilation endpoint integrals (BBNS 2001 integrands)
Phi = lambda u: 6 * u * (1 - u)
q1 = lambda f, a, b: si.quad(f, a, b, limit=400, epsabs=1e-13, epsrel=1e-13)[0]
fin = si.dblquad(lambda y, x: 36 * x * (1 - x) * (1 - y) / (1 - x * (1 - y)), 0, 1, lambda x: 0, lambda x: 1, epsabs=1e-12, epsrel=1e-12)[0]
ck('finite piece: 36 int int x xbar ybar/(1 - x ybar) = 18(pi^2/3 - 3)', abs(fin - 18 * (np.pi ** 2 / 3 - 3)) < 1e-9, f'{fin:.12f}')
okA = True; okF = True; det = []
for delta in (1e-8, 1e-10):
    XA = np.log(1 / delta)
    # A_1^i (BBNS 2001): tw2 = finite piece + [int_0^{1-d} 6x/xbar dx][int_0^1 6 ybar dy] ; tw3 = 2 [int dx/xbar][int dy/y]
    tw2 = fin + q1(lambda x: 6 * x / (1 - x), 0, 1 - delta) * q1(lambda y: 6 * (1 - y), 0, 1)
    tw3 = 2 * q1(lambda x: 1 / (1 - x), 0, 1 - delta) * q1(lambda y: 1 / y, delta, 1)
    okA &= abs(tw2 - 18 * (XA - 4 + np.pi ** 2 / 3)) < 1e-5 and abs(tw3 - 2 * XA ** 2) < 1e-5
    # A_3^f (r1 = r2 = r_chi): both terms factorize
    t1 = q1(lambda x: Phi(x) * 2 * (2 - x) / (1 - x) ** 2, 0, 1 - delta) * q1(lambda y: 1 / y, delta, 1)
    t2 = q1(lambda x: 1 / (1 - x), 0, 1 - delta) * q1(lambda y: Phi(y) * 2 * (1 + y) / y ** 2, delta, 1)
    okF &= abs(t1 + t2 - 12 * (2 * XA ** 2 - XA)) < 1e-4
    det.append(f'delta={delta:.0e}: tw2-18(X-4+pi^2/3)={tw2 - 18*(XA - 4 + np.pi**2/3):.1e}, A3f-12(2X^2-X)={t1 + t2 - 12*(2*XA**2 - XA):.1e}')
ck('A_1^i = pi alpha_s [18(X_A - 4 + pi^2/3) + 2 r_chi^2 X_A^2], X_A = int_0^1 dy/y  [BBNS 2001 (XAdef); = 2pi a_s[9(...)+r1 r2 X_A^2], BN 2003]',
   okA, det[0])
ck('A_3^f = 12 pi alpha_s r_chi (2 X_A^2 - X_A)   [BBNS 2001; = 6 pi alpha_s (r1 + r2)(2X_A^2 - X_A), BN 2003]', okF, det[1])
# A_3^i r1-term: x-integral converges for y > 0: int_0^1 x dx/(1 - x ybar) = -1/ybar - ln y/ybar^2 ; then the
# divergent y-integral with the BN rules (int dy/y -> X_A, int dy ln y/y -> -X_A^2/2), realized by a y-cutoff
okI = True
for delta in (1e-8, 1e-10):
    XA = np.log(1 / delta)
    inner = lambda y: -1 / (1 - y) - np.log(y) / (1 - y) ** 2
    chk = abs(q1(lambda x: x / (1 - x * (1 - 0.3)), 0, 1) - inner(0.3)) < 1e-12
    val = 12 * q1(lambda y: (1 - y) / y * inner(y), delta, 1)
    okI &= chk and abs(val - 6 * (XA ** 2 - 2 * XA + np.pi ** 2 / 3)) < 1e-4
ck('A_3^i r1-term = 6 pi alpha_s r1 (X_A^2 - 2X_A + pi^2/3) with the BN prescription; A_3^i = 0 for r1 = r2  [BN 2003 (XAmodel)]', okI)
# prescription dependence: cutting ALSO x at 1 - delta (a different regulator of the same divergent integral)
delta = 1e-6; XA = np.log(1 / delta)
dbl = 12 * si.dblquad(lambda y, x: x * (1 - y) / (y * (1 - x * (1 - y))), 0, 1 - delta, lambda x: delta, lambda x: 1.0,
                      epsabs=1e-10, epsrel=1e-10)[0]
shift = dbl - 6 * (XA ** 2 - 2 * XA + np.pi ** 2 / 3)
ck('regulator dependence: a double cutoff (x < 1-delta, y > delta) changes the X_A^2/X_A/constant terms of A_3^i: the X_A model is prescription-dependent',
   abs(shift) > 1.0, f'double-cutoff minus BN-rule result = {shift:.3f} at X_A = {XA:.2f}')
# endpoint-cutoff vs BN rule consistency
ck('cutoff realization of the BN rules: int_delta^1 dy/y = X_A, int_delta^1 ln y/y = -X_A^2/2',
   abs(si.quad(lambda y: np.log(y) / y, 1e-6, 1)[0] + 0.5 * np.log(1e6) ** 2) < 1e-6)
# parametrization X = (1 + rho e^{i phi}) ln(m_B/Lambda_h), rho <= 1: the modulus can vary from 0 to 2 ln(m_B/Lambda_h)
phis = np.linspace(0, 2 * np.pi, 361)
Xs = (1 + np.exp(1j * phis)) * np.log(mB_ / Lh)
ck('X_A = (1 + rho_A e^{i phi_A}) ln(m_B/Lambda_h), rho_A <= 1: |X_A| ranges over [0, 2 ln(m_B/Lambda_h)] (100% uncertainty; arbitrary phase)',
   abs(np.min(np.abs(Xs))) < 1e-12 and abs(np.max(np.abs(Xs)) - 2 * np.log(mB_ / Lh)) < 1e-12)

# ======================================================================== F. colour transparency (soft gluon on the emitted pair)
# emitted colour-singlet pair q(x p + k_T) qbar(xbar p - k_T); soft gluon k_s couples eikonally:
# J = g t^a [ p_q.eps/(p_q.k_s) - p_qb.eps/(p_qb.k_s) ]  -> 0 for k_T -> 0 ;  O(k_T/E) dipole otherwise
errs = []
for kT in (0.05, 0.005, 0.0005):
    E = 2.6
    p = E * NBVEC
    kTv = np.array([0, kT, 0.3 * kT, 0])
    def onshell(v3):
        return np.array([np.linalg.norm(v3), *v3])
    pq = onshell(0.4 * p[1:] + kTv[1:]); pqb = onshell(0.6 * p[1:] - kTv[1:])
    ks = np.array([0.4, 0.1, -0.25, 0.2])        # soft gluon, ~ Lambda
    eps = np.array([0.3, 0.6, 0.3j, 0.4])         # generic: p.eps = E(eps0 + eps3) not accidentally small
    Jpair = mdot(pq, eps) / mdot(pq, ks) - mdot(pqb, eps) / mdot(pqb, ks)
    Jsingle = mdot(pq, eps) / mdot(pq, ks)
    errs.append(abs(Jpair) / abs(Jsingle))
ck('colour transparency: soft-gluon couplings to the collinear q qbar pair cancel; remainder ~ k_T/E (dipole), i.e. Lambda/m_b',
   errs[2] < 1e-2 and 8 < errs[0] / errs[1] < 12 and 8 < errs[1] / errs[2] < 12, f'|J_pair/J_quark| = {["%.1e" % e for e in errs]}')

ok = ck.summary()
sys.exit(0 if ok else 1)
