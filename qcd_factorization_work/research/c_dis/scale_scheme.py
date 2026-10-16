"""
scale_scheme.py -- factorisation-scale (and renormalisation-scale) independence of F_2 at O(alpha_s),
and the MS-bar -> DIS scheme transformation.

Normalisation: a = alpha_s(mu)/(2 pi);  DGLAP  d f_i/d ln mu^2 = a sum_j P_ij (x) f_j ;
d a/d ln mu^2 = -(beta_0/2) a^2 + O(a^3),  beta_0 = 11/3 C_A - 4/3 T_F n_f.
F_2/x = sum_q e_q^2 [ (q+qbar) + a ( C_2^q(mu) (x) (q+qbar) + 2 C_2^g(mu) (x) g ) ],
C_2^i(z, mu) = C_2^i(z) + ln(Q^2/mu^2) P_qi(z)   (derived from the D-dim result in dis_nlo.py, section 5).
"""
import sys, os, io, contextlib
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
import numpy as np
import mpmath as mp
with contextlib.redirect_stdout(io.StringIO()):
    import moments as mo

ok_all = True


def report(name, ok):
    global ok_all
    ok_all &= bool(ok)
    print(f'  [{"PASS" if ok else "FAIL"}] {name}')


t, Q2 = sp.symbols('t Q2', real=True)            # t = ln mu^2
b0 = sp.Symbol('beta_0')
nf = sp.Symbol('n_f')
Cq, Cg, Pqq, Pqg, Pgq, Pgg, CLq, CLg = sp.symbols('C_q C_g P_qq P_qg P_gq P_gg C_Lq C_Lg')   # N-space numbers
a = sp.Function('a')(t)
qs = sp.Function('qs')(t)        # (q + qbar)_N of one flavour
g = sp.Function('g')(t)          # g_N
Sig = sp.Function('Sigma')(t)    # Sigma_N = sum_q (q+qbar)_N
lam = sp.Symbol('lambda')        # order-counting parameter: a -> lam a

print('=' * 78)
print('A. mu_F independence of F_2 at O(as), Mellin space, generic moments')
L = sp.log(Q2) - t
F = qs + a * ((Cq + L * Pqq) * qs + 2 * (Cg + L * Pqg) * g)
rules = {sp.Derivative(qs, t): a * (Pqq * qs + 2 * Pqg * g),
         sp.Derivative(g, t): a * (Pgq * Sig + Pgg * g),
         sp.Derivative(a, t): -b0 / 2 * a ** 2}
dF = sp.expand(sp.diff(F, t).subs(rules))
dF_lam = sp.expand(dF.subs(a, lam * a))
o1 = dF_lam.coeff(lam, 1)
o2 = dF_lam.coeff(lam, 2)
print('   dF_N/d ln mu^2 at O(a)   :', sp.simplify(o1))
print('   dF_N/d ln mu^2 at O(a^2) :', sp.factor(o2), '  (cancelled by the O(a^2) coefficient functions)')
report('O(a) term of dF_2/dln mu_F^2 vanishes identically', sp.simplify(o1) == 0)
# renormalisation scale separately: a(mu_R) in front of the O(a) term, PDFs at mu_F fixed
tR = sp.Symbol('t_R')
aR = sp.Function('a')(tR)
FR = qs + aR * (Cq * qs + 2 * Cg * g)
dFR = sp.expand(sp.diff(FR, tR).subs(sp.Derivative(aR, tR), -b0 / 2 * aR ** 2))
report('d F_2/d ln mu_R^2 = O(a^2)  (= -(beta_0/2) a^2 (C_q qs + 2 C_g g))',
       sp.simplify(dFR + b0 / 2 * aR ** 2 * (Cq * qs + 2 * Cg * g)) == 0)
# the same for F_L: no log at O(a) since F_L starts at O(a)
FL = a * (CLq * qs + 2 * CLg * g)
dFL = sp.expand(sp.diff(FL, t).subs(rules).subs(a, lam * a))
report('F_L: d/dln mu^2 starts at O(a^2) (no mu-dependence of C_L at this order)', dFL.coeff(lam, 1) == 0)

print('=' * 78)
print('B. numerical illustration (Mellin space, exact LO evolution, one-loop running, n_f = 4, mu_0 = Q)')
CFn, CAn, TFn, nfn = 4.0 / 3, 3.0, 0.5, 4
b0n = 11.0 / 3 * CAn - 4.0 / 3 * TFn * nfn
sub = {mo.CF: sp.Rational(4, 3), mo.TF: sp.Rational(1, 2)}


def S1(n): return float(sum(1.0 / j for j in range(1, n + 1)))


def gamma_matrix(n):
    pqq = float(mo.Pqq_N(n).subs(sub))
    pqg = float(mo.Pqg_N(n).subs(sub))
    pgq = CFn * (n * n + n + 2) / ((n - 1) * n * (n + 1))
    pgg = 2 * CAn * (-S1(n) + 1.0 / (n * (n - 1)) + 1.0 / ((n + 1) * (n + 2))) + b0n / 2
    return np.array([[pqq, 2 * nfn * pqg], [pgq, pgg]])


# momentum sum rule check of the LO kernels at N = 2: columns of Gamma_2 sum to zero
G2 = gamma_matrix(2)
report('LO kernels: momentum conservation  P_qq(2) + P_gq(2) = 0,  2n_f P_qg(2) + P_gg(2) = 0',
       abs(G2[0, 0] + G2[1, 0]) < 1e-14 and abs(G2[0, 1] + G2[1, 1]) < 1e-14)


def evolve(vec0, n, a0, ratio_mu2):
    """exact LO solution from mu_0 to mu (mu^2 = ratio_mu2 mu_0^2) with one-loop a(mu)"""
    a1 = a0 / (1 + b0n / 2 * a0 * np.log(ratio_mu2))
    G = gamma_matrix(n)
    w, V = np.linalg.eig(G)
    expo = V @ np.diag((a1 / a0) ** (-2 * w / b0n)) @ np.linalg.inv(V)
    return expo.real @ vec0, a1


def F2_singlet(n, a0, ratio_mu2, vec0, e2avg=10.0 / 36):
    """<e^2>[ (1 + a C_q(mu)) Sigma + a 2 n_f C_g(mu) g ],  L = ln(Q^2/mu^2) = -ln(ratio_mu2), mu_0 = Q"""
    (Sg, gg), a1 = evolve(vec0, n, a0, ratio_mu2)
    Lq = -np.log(ratio_mu2)
    cq = float(mo.C2q_N(n).subs(sub)) + Lq * float(mo.Pqq_N(n).subs(sub))
    cg = float(mo.C2g_N(n).subs(sub)) + Lq * float(mo.Pqg_N(n).subs(sub))
    return e2avg * ((1 + a1 * cq) * Sg + a1 * 2 * nfn * cg * gg)


vec0 = np.array([0.55, 0.45])        # toy (Sigma_N, g_N) at mu_0 = Q
print('   N   alpha_s(Q)   F(mu=Q/2)-F(mu=2Q)    ratio to alpha_s^2')
okB = True
for n in (2, 4, 6):
    rows = []
    for al in (0.2, 0.1, 0.05, 0.025):
        a0 = al / (2 * np.pi)
        d = F2_singlet(n, a0, 0.25, vec0) - F2_singlet(n, a0, 4.0, vec0)
        rows.append(d / al ** 2)
        print(f'   {n}   {al:6.3f}       {d: .4e}          {d / al ** 2: .5f}')
    # ratio must approach a constant: successive differences shrink ~ linearly in alpha_s
    okB &= abs(rows[-1] - rows[-2]) < 0.6 * abs(rows[-2] - rows[-3]) + 1e-12
report('scale variation of F_2 moments is O(alpha_s^2) (ratio to alpha_s^2 converges)', okB)

print('=' * 78)
print('C. DIS scheme')
# per flavour q (and separately qbar):  q^DIS = q + a (C_2^q (x) q + C_2^g (x) g)
# gluon (Diemoz-Ferroni-Longo-Martinelli choice, momentum sum rule preserved):
#   g^DIS = g - a ( C_2^q (x) Sigma + 2 n_f C_2^g (x) g )
qN, qbN, gN, SigN = sp.symbols('q_N qbar_N g_N Sigma_N')
a0s = sp.Symbol('a')
qD = qN + a0s * (Cq * qN + Cg * gN)
qbD = qbN + a0s * (Cq * qbN + Cg * gN)
F2_ms = (qN + qbN) + a0s * (Cq * (qN + qbN) + 2 * Cg * gN)
report('F_2/x = sum e_q^2 (q^DIS + qbar^DIS) + O(a^2), i.e. C_2^{q,DIS} = C_2^{g,DIS} = 0',
       sp.expand(F2_ms - (qD + qbD)) == 0)
SigD = SigN + a0s * (Cq * SigN + 2 * nf * Cg * gN)
gD = gN - a0s * (Cq * SigN + 2 * nf * Cg * gN)
report('momentum sum rule: Sigma^DIS_2 + g^DIS_2 = Sigma_2 + g_2 exactly (any N, in particular N = 2)',
       sp.expand(SigD + gD - SigN - gN) == 0)
# F_L in the DIS scheme: F_L/x = a (C_L^q (x) (q+qbar) + 2 C_L^g (x) g) + O(a^2): unchanged at O(a)
FLms = a0s * (CLq * (qN + qbN) + 2 * CLg * gN)
FLdis = a0s * (CLq * (qD + qbD) + 2 * CLg * gN)
report('C_L^{q,g} are unchanged at O(as) by the transformation', sp.expand(FLdis - FLms).coeff(a0s, 1) == 0)
# transformation of the NLO kernels: f' = (1 + a Z) f  =>  P'^(1) = P^(1) + [Z, P^(0)] - (beta_0/2) Z
z11, z12, z21, z22, p11, p12, p21, p22, r11, r12, r21, r22 = sp.symbols('z11 z12 z21 z22 p11 p12 p21 p22 r11 r12 r21 r22')
Zm = sp.Matrix([[z11, z12], [z21, z22]])
P0 = sp.Matrix([[p11, p12], [p21, p22]])
P1 = sp.Matrix([[r11, r12], [r21, r22]])
fvec = sp.Matrix([sp.Function('f1')(t), sp.Function('f2')(t)])
av = sp.Function('a')(t)
fprime = fvec + av * Zm * fvec
drule = {sp.Derivative(fvec[0], t): (av * (P0 + av * P1) * fvec)[0],
         sp.Derivative(fvec[1], t): (av * (P0 + av * P1) * fvec)[1],
         sp.Derivative(av, t): -b0 / 2 * av ** 2}
lhs = sp.diff(fprime, t).subs(drule)
P1p = P1 + Zm * P0 - P0 * Zm - b0 / 2 * Zm
rhs = av * (P0 + av * P1p) * fprime
diff = (lhs - rhs).applyfunc(lambda e: sp.expand(e.subs(av, lam * av)))
report("P'^(1) = P^(1) + Z P^(0) - P^(0) Z - (beta_0/2) Z  (up to O(a^3) in the evolution equation)",
       all(sp.simplify(d.coeff(lam, 1)) == 0 and sp.simplify(d.coeff(lam, 2)) == 0 for d in diff))
print('   Z^(1) for the DFLM DIS scheme in the (Sigma, g) basis, N-space:  [[C_2^q, 2 n_f C_2^g], [-C_2^q, -2 n_f C_2^g]]')
print('   non-singlet: P_NS^(1),DIS = P_NS^(1),MSbar - (beta_0/2) C_2^q   (convolutions commute)')

print('=' * 78)
print('SCALE/SCHEME CHECKS:', 'ALL PASS' if ok_all else 'SOME FAILED')
