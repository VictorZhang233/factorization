"""
checks_setup.py -- independent checks of the ingredients that fix the overall normalisation:

 (a) D-dimensional projectors onto F_2 and F_L (symbolic in D, and numerically with explicit
     components in D = 4,5,6,7), including the massive-target generalisation;
 (b) Born normalisation:  Fhat_2^(0)/z = e_q^2 delta(1-z),  Fhat_L^(0) = 0  (exact in D);
 (c) D-dimensional two-body phase space  Phi_2 = (1/8pi)(4pi/s)^eps/Gamma(1-eps) int_0^1 dy [y(1-y)]^(-eps),
     checked against the direct solid-angle evaluation;
 (d) assembly of the overall prefactor of the real-emission contribution.

Conventions (binding, CONTEXT.md): metric (+,-,...,-), D = 4 - 2 eps,
   W^{mu nu} = (-g^{mu nu} + q^mu q^nu/q^2) F_1 + Ptilde^mu Ptilde^nu F_2/(P.q),
   Ptilde = P - (P.q/q^2) q,   F_L = F_2 - 2 x F_1  (massless target),
   W^{mu nu} = (1/4pi) int d^4z e^{iqz} <P|[J^mu(z), J^nu(0)]|P>   (spin averaged; this normalisation
   is what reproduces the parton-model formula F_2 = sum_q e_q^2 x (q + qbar), see (b)).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import sympy as sp
import mpmath as mp
import dirac_d as dd

ok_all = True


def report(name, ok):
    global ok_all
    ok_all &= bool(ok)
    print(f'  [{"PASS" if ok else "FAIL"}] {name}')


D, eps = sp.symbols('D epsilon')
F1, F2, FL = sp.symbols('F_1 F_2 F_L')
Q2, M2, pq = sp.symbols('Q2 M2 Pq', positive=True)

print('=' * 78)
print('(a) projectors')
# contractions of the two tensor structures (exact, any D):
#   T1 = -g + q q/q^2 ,  T2 = Pt Pt /(P.q)
# with q^2 = -Q2, P^2 = M2, Pt^2 = M2 + Pq^2/Q2, P.Pt = Pt^2
q2 = -Q2
Pt2 = M2 - pq ** 2 / q2
mg_T1 = -(-D + 1)            # -g_{mu nu}(-g^{mu nu} + q^mu q^nu/q^2) = D - 1
mg_T2 = -Pt2 / pq            # -g_{mu nu} Pt^mu Pt^nu/(P.q)
pp_T1 = -M2 + pq ** 2 / q2   # P_mu P_nu (-g + q q/q^2)
pp_T2 = Pt2 ** 2 / pq
x = Q2 / (2 * pq)
rho2 = 1 + 4 * M2 * x ** 2 / Q2
# massive target: F_L = rho^2 F_2 - 2 x F_1  ->  F_1 = (rho^2 F_2 - F_L)/(2x)
F1_of = (rho2 * F2 - FL) / (2 * x)
gW = sp.simplify(mg_T1 * F1_of + mg_T2 * F2)
ppW = sp.simplify(pp_T1 * F1_of + pp_T2 * F2)
proj_L = sp.simplify(8 * x ** 2 / (Q2 * rho2) * ppW)
proj_2 = sp.simplify((2 * gW + (D - 1) * proj_L) / ((D - 2) * rho2))
report('massive target: (8x^2/(Q^2 rho^2)) P.W.P = F_L/x   with F_L = rho^2 F_2 - 2xF_1, rho^2 = 1+4M^2x^2/Q^2',
       sp.simplify(proj_L - FL / x) == 0)
report('massive target: [2(-g.W) + (D-1) F_L/x]/((D-2) rho^2) = F_2/x', sp.simplify(proj_2 - F2 / x) == 0)
# massless case, D = 4 - 2 eps : the projectors used in real_me.py / dis_nlo.py
gW0 = gW.subs(M2, 0)
ppW0 = ppW.subs(M2, 0)
P2 = sp.simplify(((gW0 + (3 - 2 * eps) * 4 * x ** 2 / Q2 * ppW0) / (1 - eps)).subs(D, 4 - 2 * eps))
PL = sp.simplify(8 * x ** 2 / Q2 * ppW0)
report('massless: Pi_2 = [-g + (3-2eps)(4x^2/Q^2) P P]/(1-eps) gives F_2/x', sp.simplify(P2 - F2 / x) == 0)
report('massless: Pi_L = (8x^2/Q^2) P P gives F_L/x', sp.simplify(PL - FL / x) == 0)

# explicit-component check in integer D (independent of the contraction formulas above)
rng = np.random.default_rng(7)
okn = True
for Dn in (4, 5, 6, 7):
    eta = np.diag([1.0] + [-1.0] * (Dn - 1))
    for M2n in (0.0, 0.37):
        # random q (spacelike), random P with P^2 = M2n
        while True:
            qv = rng.normal(size=Dn)
            if qv @ eta @ qv < -0.2:
                break
        Psp = rng.normal(size=Dn - 1)
        P = np.concatenate([[np.sqrt(Psp @ Psp + M2n)], Psp])
        if P @ eta @ qv <= 0:
            P[1:] *= -1
            P[0] = np.sqrt(Psp @ Psp + M2n)
        Pq_ = P @ eta @ qv
        if Pq_ <= 0:
            continue
        Q2n = -(qv @ eta @ qv)
        xn = Q2n / (2 * Pq_)
        f1, f2 = 0.731, 1.913
        ginv = eta                                    # g^{mu nu} = g_{mu nu} numerically (diag +-1)
        Pt = P - (Pq_ / (qv @ eta @ qv)) * qv
        W = (-ginv + np.outer(qv, qv) / (qv @ eta @ qv)) * f1 + np.outer(Pt, Pt) * f2 / Pq_
        Pl = eta @ P                                  # lower index
        gW_n = -np.einsum('mn,mn->', eta, W)
        ppW_n = Pl @ W @ Pl
        r2 = 1 + 4 * M2n * xn ** 2 / Q2n
        fL = r2 * f2 - 2 * xn * f1
        projL = 8 * xn ** 2 / (Q2n * r2) * ppW_n
        proj2 = (2 * gW_n + (Dn - 1) * projL) / ((Dn - 2) * r2)
        okn &= abs(projL - fL / xn) < 1e-9 * (1 + abs(fL / xn)) and abs(proj2 - f2 / xn) < 1e-9 * (1 + abs(f2 / xn))
report('explicit components, D = 4,5,6,7, M^2 = 0 and M^2 != 0', okn)

print('=' * 78)
print('(b) Born term (gamma* q -> q), exact in D')
# W^{mu nu}_Born = (1/4pi) * 2pi delta((p+q)^2) * (1/2 spin avg) e_q^2 Tr[p g^mu (p+q) g^nu];
# (p+q)^2 = Q^2 (1-z)/z  ->  delta((p+q)^2) = (z/Q^2) delta(1-z) = delta(1-z)/Q^2.  Set Q^2 = 1.
zz = sp.Symbol('z', positive=True)
dd.set_dots({('p', 'p'): 0, ('q', 'q'): -1, ('p', 'q'): 1 / (2 * zz)})
I, V = dd.I, dd.V
trg = -dd.tr([V(p=1), I('m'), V(p=1, q=1), I('m')])          # -g_{mu nu} Tr[...]
trpp = dd.tr([V(p=1), V(p=1), V(p=1, q=1), V(p=1)])           # p_mu p_nu Tr[...]
norm = sp.Rational(1, 4) * sp.Rational(1, 2) * 2              # (1/4pi)(2pi)(1/2)
gW_B = (norm * trg).subs(zz, 1)
ppW_B = (norm * trpp).subs(zz, 1)
F2B = sp.simplify(((gW_B + (3 - 2 * eps) * 4 * ppW_B) / (1 - eps)).subs(dd.D, 4 - 2 * eps))
FLB = sp.simplify(8 * ppW_B)
print('   coefficient of e_q^2 delta(1-z):  F_2/z ->', F2B, ';  F_L/z ->', FLB)
report('Fhat_2^(0)/z = e_q^2 delta(1-z) (exact in eps), Fhat_L^(0) = 0', F2B == 1 and FLB == 0)
# factorisation formula at LO:  F_2/x = sum_j int dxi/xi f_j(xi) Fhat_2^j(x/xi)/(x/xi) = sum e_q^2 q(x)  (parton model)

print('=' * 78)
print('(c) D-dimensional two-body phase space')
s = sp.Symbol('s', positive=True)
Dd = 4 - 2 * eps
Omega = lambda n: 2 * sp.pi ** (sp.Rational(1, 2) * n) / sp.gamma(sp.Rational(1, 2) * n)   # area of S^{n-1}
# direct: int d^{D-1}k/((2pi)^{D-1} 2|k|) 2pi delta((P-k)^2), P = (sqrt s, 0):
#   = (2pi)^{2-D} Omega_{D-1} int d|k| |k|^{D-3}/2 delta(s - 2 sqrt(s)|k|) = (2pi)^{2-D} Omega_{D-1} (sqrt(s)/2)^{D-3}/(4 sqrt s)
direct = (2 * sp.pi) ** (2 - Dd) * Omega(Dd - 1) * (sp.sqrt(s) / 2) ** (Dd - 3) / (4 * sp.sqrt(s))
formula = 1 / (8 * sp.pi) * (4 * sp.pi / s) ** eps * sp.gamma(1 - eps) / sp.gamma(2 - 2 * eps)
vals = [abs(sp.N((direct / formula - 1).subs({s: sv, eps: ev}), 30))
        for sv in (sp.Rational(3, 7), sp.Integer(5)) for ev in (sp.Rational(-3, 10), sp.Rational(1, 7), sp.Rational(2, 5))]
report('Phi_2 = (1/8pi)(4pi/s)^eps Gamma(1-eps)/Gamma(2-2eps)  [= (1/8pi)(4pi/s)^eps/Gamma(1-eps) int dy (y(1-y))^-eps]',
       max(vals) < 1e-25)
# angular measure: Omega_{D-1} = Omega_{D-2} int_0^pi sin^{D-3}th dth, and sin^{D-3}th dth = 2*4^{-eps}(y(1-y))^{-eps} dy
mp.mp.dps = 30
okang = True
Om = lambda n: 2 * mp.pi ** (n / 2) / mp.gamma(n / 2)
for ev in ('-0.3', '0.15', '0.4'):
    ev = mp.mpf(ev)
    lhs = mp.quad(lambda th: mp.sin(th) ** (1 - 2 * ev), [0, mp.pi])
    rhs = 2 * mp.mpf(4) ** (-ev) * mp.quad(lambda yy: (yy * (1 - yy)) ** (-ev), [0, 1])
    D_ = 4 - 2 * ev
    okang &= abs(lhs - rhs) < 1e-15 and abs(Om(D_ - 1) - Om(D_ - 2) * lhs) < 1e-15
report('angular measure  dOmega_{D-1} = Omega_{D-2} 2^{1-2eps} [y(1-y)]^{-eps} dy  (y = (1-cos th)/2)', okang)

print('=' * 78)
print('(d) prefactor of the real emission')
# W = (1/4pi) * (1/2) [spin] * C_F [colour] * g0^2 * e_q^2 * int dPhi_2 (projected trace)
# g0^2 = 4 pi as mu^{2eps} e^{eps gE}/(4pi)^eps   (MS-bar)
a_s, mu2 = sp.symbols('alpha_s mu2', positive=True)
g02 = 4 * sp.pi * a_s * mu2 ** eps * sp.exp(eps * sp.EulerGamma) / (4 * sp.pi) ** eps
pref = sp.Rational(1, 4) / sp.pi * sp.Rational(1, 2) * g02 * 1 / (8 * sp.pi) * (4 * sp.pi / s) ** eps / sp.gamma(1 - eps)
target = a_s / (2 * sp.pi) * sp.Rational(1, 8) * (mu2 / s) ** eps * sp.exp(eps * sp.EulerGamma) / sp.gamma(1 - eps)
report('(1/4pi)(1/2) g0^2 (1/8pi)(4pi/s)^eps/Gamma(1-eps) = (as/2pi) (1/8) (mu^2/s)^eps e^{eps gE}/Gamma(1-eps)',
       sp.simplify(sp.powsimp(sp.expand_power_base(pref / target, force=True), force=True)) == 1)
print('   gluon target: colour average 1/(N_c^2-1) * Tr(t^a t^a) = T_F ; polarisation average 1/(D-2) = 1/(2(1-eps))')

print('=' * 78)
print('SETUP CHECKS:', 'ALL PASS' if ok_all else 'SOME FAILED')
