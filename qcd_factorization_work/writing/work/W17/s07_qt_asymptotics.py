# W17 / Ch14 -- s07: O(alpha_s) Drell-Yan q_T distribution: exact fixed order vs the O(alpha_s) expansion of TMD
# factorization (ex:tmd-qt-asymptotics, def:tmd-kin).  Independent of research/c_tmd: matrix elements from explicit
# 4x4 Dirac traces, own derivation of the hadronic phase-space formula, own Fourier identities.
#   exact:  dsigma/(dQ^2 dy d^2qT) = sum int dx_a/|x_a s - sqrt(s) M_T e^{y}| f(x_a) f(x_b) (alpha/(3 pi Q^2)) (1/(2 shat)) (1/(8 pi^2)) <|M|^2>
#   TMD at O(alpha_s), qT>0:  dsigma/(dQ^2 dy dqT^2) = (sigma0/s)(alpha_s/2pi)(1/qT^2){[2A1 ln(Q^2/qT^2)+2B1] q qb + (Pqq x q) qb + q (Pqq x qb) + (Pqg x g) qb}
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import mpmath as mp
from scipy.integrate import quad
ok = True
def check(name, cond):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name); ok &= bool(cond)
Nc, CF, TF = 3.0, 4.0/3.0, 0.5
# ---------------- (1) matrix elements by explicit Dirac traces
I2 = np.eye(2); Z2 = np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]], dtype=complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], dtype=complex)
G = [np.block([[I2, Z2], [Z2, -I2]]).astype(complex)] + [np.block([[Z2, s], [-s, Z2]]) for s in (sx, sy, sz)]
gm = np.diag([1., -1., -1., -1.])
def sl(v): return sum(gm[m, m]*v[m]*G[m] for m in range(4))
def mdot(a, b): return a[0]*b[0] - a[1:].dot(b[1:])
rng = np.random.default_rng(7)
def massless(E, th, ph): return np.array([E, E*np.sin(th)*np.cos(ph), E*np.sin(th)*np.sin(ph), E*np.cos(th)])
def sum_msq_qqbar(pa, pb, k):
    """sum over spins/pols (-g for gluon and photon) of |vbar(pb) Gamma^{mu nu} u(pa)|^2, couplings stripped; colour separately"""
    q = pa + pb - k
    tot = 0
    for mu in range(4):
        for nu in range(4):
            Gam = G[mu] @ sl(pa - k) @ G[nu]/mdot(pa - k, pa - k) + G[nu] @ sl(k - pb) @ G[mu]/mdot(pb - k, pb - k)
            Gb = G[0] @ Gam.conj().T @ G[0]
            tot += gm[mu, mu]*gm[nu, nu]*np.trace(sl(pb) @ Gam @ sl(pa) @ Gb)
    return tot.real
for trial in range(4):
    E1, E2 = 5 + rng.random(), 4 + rng.random()
    pa = massless(E1, 0, 0); pb = massless(E2, np.pi, 0)
    # gluon momentum: random massless with energy below threshold such that Q^2 = (pa+pb-k)^2 > 0
    kk = massless(1.0 + rng.random(), rng.random()*np.pi, rng.random()*2*np.pi)
    s = mdot(pa + pb, pa + pb); t = mdot(pa - kk, pa - kk); u = mdot(pb - kk, pb - kk); Q2 = s + t + u
    if Q2 <= 0: continue
    lhs = sum_msq_qqbar(pa, pb, kk)
    rhs = 8*(t/u + u/t + 2*s*Q2/(t*u))
    check('Dirac trace: sum|M|^2(q qb -> gamma* g)/(e^2 e_q^2 g^2) = 8[t/u+u/t+2sQ^2/(tu)] x colour  (%.6f vs %.6f)' % (lhs, rhs), abs(lhs/rhs - 1) < 1e-10)
# qg -> gamma* q by crossing: q(pa) g(pb) -> gamma* q(k): sum|M|^2 = -8[s/t + t/s + 2Q^2 u/(st)], t=(pa-q)^2... verify directly
def sum_msq_qg(pa, pg, k):
    q = pa + pg - k
    tot = 0
    for mu in range(4):
        for nu in range(4):
            # ubar(k) [ gamma^mu (pa+pg)slash gamma^nu/s + gamma^nu (pa - q)slash gamma^mu/(pa-q)^2 ] u(pa)
            Gam = G[mu] @ sl(pa + pg) @ G[nu]/mdot(pa + pg, pa + pg) + G[nu] @ sl(pa - q) @ G[mu]/mdot(pa - q, pa - q)
            Gb = G[0] @ Gam.conj().T @ G[0]
            tot += gm[mu, mu]*gm[nu, nu]*np.trace(sl(k) @ Gam @ sl(pa) @ Gb)
    return tot.real
for trial in range(3):
    pa = massless(5 + rng.random(), 0, 0); pg = massless(4 + rng.random(), np.pi, 0)
    kk = massless(1.0 + rng.random(), rng.random()*np.pi, rng.random()*2*np.pi)
    q = pa + pg - kk
    s = mdot(pa + pg, pa + pg); t = mdot(pa - q, pa - q); u = mdot(pg - q, pg - q); Q2 = mdot(q, q)
    if Q2 <= 0: continue
    lhs = sum_msq_qg(pa, pg, kk); rhs = -8*(s/t + t/s + 2*Q2*u/(s*t))
    check('Dirac trace: sum|M|^2(q g -> gamma* q) = -8[s/t+t/s+2Q^2u/(st)], t=(p_q-q)^2, u=(p_g-q)^2 (%.6f vs %.6f)' % (lhs, rhs), abs(lhs/rhs - 1) < 1e-10)
# colour/spin averages: qqbar: C_F N_c/(4 N_c^2) ; qg: T_F (N_c^2-1)/(4 N_c (N_c^2-1)) = T_F/(4 N_c)
alpha, alphas, eq = 1.0, 1.0, 1.0
e2, g2 = 4*np.pi*alpha, 4*np.pi*alphas
def avg_qqbar(s, t, u, Q2): return e2*eq**2*g2*CF*Nc/(4*Nc**2)*8*(t/u + u/t + 2*s*Q2/(t*u))
def avg_qg(s, t, u, Q2):    return -e2*eq**2*g2*TF/(4*Nc)*8*(s/t + t/s + 2*Q2*u/(s*t))
# ---------------- (2) toy PDFs and kinematics (same toy set as the c_tmd configuration 1, for comparison)
qA = lambda x: x**-0.3*(1 - x)**3
qbB = lambda x: 0.5*x**-0.2*(1 - x)**5
gA = lambda x: 2.0*x**-0.9*(1 - x)**5
def exact(Q, y, qT, rs, chan):
    s = rs**2; Q2 = Q*Q; MT = np.sqrt(Q2 + qT**2)
    xamin = (rs*MT*np.exp(y) - Q2)/(s - rs*MT*np.exp(-y))
    def integrand(xa):
        den = xa*s - rs*MT*np.exp(y)
        xb = (xa*rs*MT*np.exp(-y) - Q2)/den
        if xb <= 0 or xb >= 1: return 0.0
        sh = xa*xb*s
        ta = Q2 - xa*rs*MT*np.exp(-y)     # (p_a - q)^2
        tb = Q2 - xb*rs*MT*np.exp(y)      # (p_b - q)^2
        if chan == 'qqbar':
            m = avg_qqbar(sh, ta, tb, Q2); f = qA(xa)*qbB(xb)
        else:   # g(A) qbar(B) -> gamma* qbar : |M|^2 = that of q g with the quark momentum p_b: t=(p_b-q)^2=tb, u=(p_a-q)^2=ta
            m = avg_qg(sh, tb, ta, Q2); f = gA(xa)*qbB(xb)
        return f/abs(den)*(alpha/(3*np.pi*Q2))/(2*sh)/(8*np.pi**2)*m
    xA = Q/rs*np.exp(y)
    v, _ = quad(integrand, xamin, 1, points=[xA, min(1, xA*1.0001), min(1, xA*1.01)], limit=4000, epsabs=0, epsrel=1e-11)
    return np.pi*v          # dsigma/dqT^2 = pi dsigma/d^2qT
def conv_Pqq(f, x):         # (P_qq (x) f)(x), P_qq = C_F[(1+z^2)/(1-z)]_+
    a_, _ = quad(lambda z: (1 + z*z)/(1 - z)*(f(x/z)/z - f(x)), x, 1, limit=600, epsabs=0, epsrel=1e-12)
    # subtraction term: -f(x) int_0^x (1+z^2)/(1-z) dz
    return CF*(a_ - f(x)*(-x - x*x/2 - 2*np.log(1 - x)))
def conv_Pqg(f, x):
    a_, _ = quad(lambda z: TF*(z*z + (1 - z)**2)*f(x/z)/z, x, 1, limit=600, epsabs=0, epsrel=1e-12)
    return a_
def tmd(Q, y, qT, rs, chan, A1=CF, B1=-1.5*CF):
    s = rs**2; xA, xB = Q/rs*np.exp(y), Q/rs*np.exp(-y)
    sigma0 = 4*np.pi*alpha**2/(3*Nc*Q*Q)*eq**2
    Lq = np.log(Q*Q/qT**2)
    if chan == 'qqbar':
        br = (2*A1*Lq + 2*B1)*qA(xA)*qbB(xB) + conv_Pqq(qA, xA)*qbB(xB) + qA(xA)*conv_Pqq(qbB, xB)
    else:
        br = conv_Pqg(gA, xA)*qbB(xB)
    return sigma0/s*alphas/(2*np.pi)/qT**2*br
# check of the subtraction identity used in conv_Pqq: int_0^x (1+z^2)/(1-z) dz = -x - x^2/2 - 2 ln(1-x)
for x in [0.1, 0.5]:
    v, _ = quad(lambda z: (1 + z*z)/(1 - z), 0, x)
    check('int_0^x (1+z^2)/(1-z) = -x - x^2/2 - 2ln(1-x) at x=%.1f' % x, abs(v - (-x - x*x/2 - 2*np.log(1 - x))) < 1e-12)
Q, y, rs = 10.0, 0.3, 200.0
print('Q=%.0f GeV, y=%.1f, sqrt(s)=%.0f GeV ; ratio exact/TMD-expansion' % (Q, y, rs))
rows = []
for r in [0.2, 0.1, 0.03, 0.01, 0.003, 0.001]:
    qT = r*Q
    rq = exact(Q, y, qT, rs, 'qqbar')/tmd(Q, y, qT, rs, 'qqbar')
    rg = exact(Q, y, qT, rs, 'qg')/tmd(Q, y, qT, rs, 'qg')
    rows.append((r, rq, rg))
    print('   qT/Q = %-6g  q qbar: %.7f    g qbar: %.7f' % (r, rq, rg))
check('ratio -> 1 as qT/Q -> 0 (both channels; |r-1| < 1e-4 at qT/Q = 1e-3)', abs(rows[-1][1] - 1) < 1e-4 and abs(rows[-1][2] - 1) < 1e-4)
# deviation roughly ~ (qT/Q)^2 (times logs)
d1, d2 = abs(rows[2][1] - 1), abs(rows[3][1] - 1)
check('q qbar deviation decreases ~ (qT/Q)^2: ratio of deviations at 0.03 and 0.01 = %.2f (expect ~ 9 up to logs)' % (d1/d2), 4 < d1/d2 < 20)
qT = 1e-3*Q
alt = tmd(Q, y, qT, rs, 'qqbar', B1=0.0)
rB0 = exact(Q, y, qT, rs, 'qqbar')/alt
print('   control: B1 = 0 -> ratio at qT/Q=1e-3 = %.4f' % rB0)
check('control B1 = 0 gives ratio 0.896 at qT/Q = 1e-3 (c_tmd value reproduced: %.4f)' % rB0, abs(rB0 - 0.896) < 0.0015)
altA = tmd(Q, y, qT, rs, 'qqbar', A1=0.9*CF)
print('   control: A1 = 0.9 C_F -> ratio at qT/Q=1e-3 = %.4f' % (exact(Q, y, qT, rs, 'qqbar')/altA))
# ---------------- (3) Fourier identities from the generating function
#  int d^2b/(2pi)^2 e^{iq.b} (Q^2 b^2/b0^2)^eta = -(eta/(pi q^2)) (Q^2/q^2)^eta e^{2 gamma eta} Gamma(1+eta)/Gamma(1-eta),  -1 < eta < -1/4
mp.mp.dps = 30
b0 = 2*mp.e**(-mp.euler)
def lhs_gen(eta, q, Qv):
    f = lambda bb: bb*mp.besselj(0, q*bb)*(Qv**2*bb**2/b0**2)**eta
    # [0,1]: algebraic end-point singularity b^{1+2 eta} handled by tanh-sinh; [1,inf): oscillatory tail
    return (mp.quad(f, [0, mp.mpf('0.5'), 1]) + mp.quadosc(f, [1, mp.inf], omega=q))/(2*mp.pi)
def rhs_gen(eta, q, Qv):
    return -(eta/(mp.pi*q**2))*(Qv**2/q**2)**eta*mp.e**(2*mp.euler*eta)*mp.gamma(1 + eta)/mp.gamma(1 - eta)
for eta in [mp.mpf('-0.4'), mp.mpf('-0.7')]:
    l, rr = lhs_gen(eta, mp.mpf('1.3'), mp.mpf(10)), rhs_gen(eta, mp.mpf('1.3'), mp.mpf(10))
    check('generating function at eta=%s: %s vs %s' % (eta, mp.nstr(l, 12), mp.nstr(rr, 12)), abs(l/rr - 1) < 1e-10)
import sympy as sp
et, qq, QQ = sp.symbols('eta q Q', positive=True)
R = -(et/(sp.pi*qq**2))*(QQ**2/qq**2)**et*sp.exp(2*sp.EulerGamma*et)*sp.gamma(1 + et)/sp.gamma(1 - et)
FT1 = sp.simplify(sp.diff(R, et).subs(et, 0)); FT2 = sp.simplify(sp.diff(R, et, 2).subs(et, 0)); FT3 = sp.simplify(sp.diff(R, et, 3).subs(et, 0))
check('FT[L] = -1/(pi q^2)', sp.simplify(FT1 + 1/(sp.pi*qq**2)) == 0)
check('FT[L^2] = -(2/pi) ln(Q^2/q^2)/q^2', sp.simplify(sp.expand_log(FT2 + 2/sp.pi*sp.log(QQ**2/qq**2)/qq**2, force=True)) == 0)
check('FT[L^3] = -(3/pi) ln^2(Q^2/q^2)/q^2', sp.simplify(sp.expand(sp.expand_log(FT3 + 3/sp.pi*sp.log(QQ**2/qq**2)**2/qq**2, force=True))) == 0)
# ---------------- (4) symbolic O(alpha_s) expansion of W~ -> coefficients 2A1 ln + 2B1
# W~ at mu=Q, zeta=Q^2 :  a{-L^2 qqb - L[(p (x) q) qb + q (p (x) qb)]} - (alpha_s T_F/2pi) L (Pg (x) g) qb + ... ; a p = (alpha_s/2pi)(P_qq - 3/2 C_F delta)
Lsym, als = sp.symbols('L alpha_s')
# coefficient structure after FT (units (alpha_s/2pi)/(pi q^2)):  -C_F FT[L^2]*pi q^2 - FT[L]*pi q^2 * (P(x)q + ...) + 3 C_F FT[L] pi q^2
lnQ = sp.Symbol('lnQ')
term_L2 = -CF*(-2*lnQ)            # -C_F * FT[L^2] in units 1/(pi q^2)
term_PF = 1                       # -FT[L] = +1 in units 1/(pi q^2), multiplying (P x q) qb etc.
term_B = 3*CF*(-1)                # +3 C_F * FT[L]
check('coefficient of q qb: 2 C_F ln(Q^2/q^2) - 3 C_F = 2A1 ln + 2B1', sp.simplify(term_L2 + term_B - (2*CF*lnQ - 3*CF)) == 0 and term_PF == 1)
print('ALL PASS' if ok else 'SOME FAIL')
