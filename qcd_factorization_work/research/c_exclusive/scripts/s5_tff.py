# -*- coding: utf-8 -*-
"""
s5_tff.py -- item (2): LO gamma* gamma -> pi0 transition form factor.

Definition (the normalization in which the decay width is Gamma(pi0->gg) = pi alpha^2 m^3 |F(0,0)|^2/4):
  T^{mu nu} = int d^4z e^{-i q1.z} <pi0(p)| T{J^mu(z) J^nu(0)} |0> = -i eps^{mu nu alpha beta} q1_alpha q2_beta F(Q1^2,Q2^2)
  (q1, q2 incoming photon momenta, p = q1 + q2, Q_i^2 = -q_i^2), so that the amplitude is
  M(g* g -> pi0) = e^2 F eps^{mu nu alpha beta} eps1_mu eps2_nu q1_alpha q2_beta.
LO: T^{mu nu} = sum_q e_q^2 c_q int dy Tr[(g^mu S(q2 - ybar p) g^nu + g^nu S(q1 - ybar p) g^mu) M_out(y)],
  M_out(y) = (i f/4) pslash g5 phi(y),   c_u = 1/sqrt2, c_d = -1/sqrt2  (pi0 = (u ubar - d dbar)/sqrt2),
  <0|(ubar g^mu g5 u - dbar g^mu g5 d)/sqrt2|pi0(p)> = i f p^mu with the same f ~ 130 MeV as for pi+.
Run:  python3 -I s5_tff.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
import numpy as np

ck = Checker('s5_tff')
y, P, f, Q1s, Q2s = sp.symbols('y P f Q1s Q2s', positive=True)
yb = 1 - y

print('=== 1. pi0 projector normalization ===')
p0 = lc(P, 0)
Mu = I * f / 4 * g5 * slash(p0) / sqrt2      # <0|ubar_b u_a|pi0>
Md = -I * f / 4 * g5 * slash(p0) / sqrt2     # <0|dbar_b d_a|pi0>
ok = all(sp.simplify((tr(G[m] * g5 * Mu) - tr(G[m] * g5 * Md)) / sqrt2 - I * f * p0[m]) == 0 for m in range(4))
ck.check('<0|(ubar g^mu g5 u - dbar g^mu g5 d)/sqrt2|pi0> = i f p^mu with projectors +-(1/sqrt2)(i f/4) g5 pslash', ok)


def T_munu(q1, q2, p, phi_factor=1):
    """LO T^{mu nu} (all mu,nu) per unit phi(y), flavour factor (e_u^2 - e_d^2)/sqrt2 included"""
    Mout = I * f / 4 * slash(p) * g5
    fl = (sp.Rational(4, 9) - sp.Rational(1, 9)) / sqrt2
    k1 = sub(q2, scal(yb, p))
    k2 = sub(q1, scal(yb, p))
    S1 = I * slash(k1) / dot(k1, k1)
    S2 = I * slash(k2) / dot(k2, k2)
    T = [[sp.simplify(fl * tr((G[m] * S1 * G[n] + G[n] * S2 * G[m]) * Mout)) for n in range(4)] for m in range(4)]
    return T


print('=== 2. real photon: Q2^2 = 0 ===')
# p along +, q2 real along -, q1 = p - q2 with q1^2 = -Q^2
Q = sp.symbols('Q', positive=True)
q2 = lc(0, Q ** 2 / (2 * P))
q1 = sub(p0, q2)
ck.zero('kinematics: q1^2 = -Q^2, q2^2 = 0, p^2 = 0', (dot(q1, q1) + Q ** 2) ** 2 + dot(q2, q2) ** 2 + dot(p0, p0) ** 2)
T = T_munu(q1, q2, p0)
low = lambda v: [METRIC[i] * v[i] for i in range(4)]
q1l, q2l = low(q1), low(q2)
epsT = [[sum(levi(m, n, a, b) * q1l[a] * q2l[b] for a in range(4) for b in range(4)) for n in range(4)] for m in range(4)]
# extract F from the (1,2) component and check all components
Fy = sp.simplify(T[1][2] / (-I * epsT[1][2]))
ok = all(sp.simplify(T[m][n] - (-I) * epsT[m][n] * Fy) == 0 for m in range(4) for n in range(4))
ck.check('T^{mu nu} = -i eps^{mu nu alpha beta} q1_alpha q2_beta F for all 16 components (LO, per unit phi(y))', ok)
print('   F integrand (per phi(y)) =', sp.factor(Fy))
ck.zero('F(Q^2) = (sqrt2 f/6) int dy phi(y) [1/(ybar Q^2) + 1/(y Q^2)]', sp.simplify(Fy - sqrt2 * f / 6 * (1 / (yb * Q ** 2) + 1 / (y * Q ** 2))))
phi_as = 6 * y * yb
F_as = sp.simplify(sp.integrate(sp.expand(Fy * phi_as), (y, 0, 1)))
ck.zero('asymptotic DA: Q^2 F -> sqrt2 f_pi  (f_pi ~ 130 MeV)  [= 2 F_pi with F_pi ~ 93 MeV]', sp.simplify(Q ** 2 * F_as - sqrt2 * f))
a2, a4 = sp.symbols('a2 a4', real=True)
Cg = lambda n, t: sp.gegenbauer(n, sp.Rational(3, 2), t)
phi_g = 6 * y * yb * (1 + a2 * Cg(2, 2 * y - 1) + a4 * Cg(4, 2 * y - 1))
F_g = sp.simplify(sp.integrate(sp.expand(Fy * phi_g), (y, 0, 1)))
ck.zero('Gegenbauer DA: Q^2 F = sqrt2 f (1 + a_2 + a_4) = (sqrt2 f/3) int phi(y)/y', sp.simplify(Q ** 2 * F_g - sqrt2 * f * (1 + a2 + a4)))
print('   sqrt2 f_pi = %.4f GeV for f_pi = 130.2 MeV' % (np.sqrt(2) * 0.1302))

print('=== 3. general virtualities ===')
# q1^2 = -Q1s, q2^2 = -Q2s ; p = q1 + q2 massless along +.  Parametrize q2 = (a P, b, 0) ...
aa, bb = sp.symbols('aa bb', real=True)
q2g = lc(aa * P, bb)
q1g = sub(p0, q2g)
sol = sp.solve([sp.Eq(dot(q1g, q1g), -Q1s), sp.Eq(dot(q2g, q2g), -Q2s)], [aa, bb], dict=True)
s0 = sol[0]
q2g = [sp.simplify(sp.sympify(c_).subs(s0)) for c_ in q2g]
q1g = sub(p0, q2g)
Tg = T_munu(q1g, q2g, p0)
q1l, q2l = low(q1g), low(q2g)
epsG = [[sp.simplify(sum(levi(m, n, a_, b_) * q1l[a_] * q2l[b_] for a_ in range(4) for b_ in range(4))) for n in range(4)] for m in range(4)]
Fg = sp.simplify(Tg[1][2] / (-I * epsG[1][2]))
ok = all(sp.simplify(Tg[m][n] - (-I) * epsG[m][n] * Fg) == 0 for m in range(4) for n in range(4))
ck.check('general Q1^2, Q2^2: same Lorentz structure', ok)
ck.zero('F(Q1^2,Q2^2) = (sqrt2 f/6) int dy phi(y) [1/(ybar Q1^2 + y Q2^2) + 1/(y Q1^2 + ybar Q2^2)]',
        sp.simplify(Fg - sqrt2 * f / 6 * (1 / (yb * Q1s + y * Q2s) + 1 / (y * Q1s + yb * Q2s))))
# symmetric point: the frame above is singular at Q1^2 = Q2^2 (p.q2 = 0 forces q2^- = 0); use a frame with
# transverse photon momenta: q2 = (P/2, 0, Q, 0), q1 = p - q2  =>  q1^2 = q2^2 = -Q^2
q2s = lc(P / 2, 0, Q, 0)
q1s = sub(p0, q2s)
ck.zero('symmetric-point kinematics q1^2 = q2^2 = -Q^2', (dot(q1s, q1s) + Q ** 2) ** 2 + (dot(q2s, q2s) + Q ** 2) ** 2)
Ts = T_munu(q1s, q2s, p0)
q1l, q2l = low(q1s), low(q2s)
epsS = [[sp.simplify(sum(levi(m, n, a_, b_) * q1l[a_] * q2l[b_] for a_ in range(4) for b_ in range(4))) for n in range(4)] for m in range(4)]
mn = [(m, n) for m in range(4) for n in range(4) if epsS[m][n] != 0][0]
Fs_y = sp.simplify(Ts[mn[0]][mn[1]] / (-I * epsS[mn[0]][mn[1]]))
ok = all(sp.simplify(Ts[m][n] - (-I) * epsS[m][n] * Fs_y) == 0 for m in range(4) for n in range(4))
ck.check('symmetric point: T^{mu nu} = -i eps q1 q2 F (all components, transverse-momentum frame)', ok)
ck.zero('symmetric point: F integrand = sqrt2 f/(3 Q^2), independent of y  => Q^2 F = sqrt2 f/3 for ANY DA with int phi = 1',
        sp.simplify(Fs_y - sqrt2 * f / (3 * Q ** 2)))

print('=== 4. consistency with the anomaly normalization and the Brodsky-Lepage interpolation ===')
Fpi = sp.symbols('F_pi', positive=True)    # F_pi = f/sqrt2 ~ 92 MeV
F0 = 1 / (4 * sp.pi ** 2 * Fpi)              # anomaly: F(0,0) = 1/(4 pi^2 F_pi) in this normalization
alpha, m = sp.symbols('alpha m', positive=True)
Gam = sp.pi * alpha ** 2 * m ** 3 * F0 ** 2 / 4
ck.zero('Gamma(pi0 -> gg) = pi alpha^2 m^3 F(0)^2/4 = alpha^2 m^3/(64 pi^3 F_pi^2)  (standard width formula)', sp.simplify(Gam - alpha ** 2 * m ** 3 / (64 * sp.pi ** 3 * Fpi ** 2)))
# check the width formula from the amplitude: sum_pol |eps_{mu nu a b} e1 e2 k1 k2|^2 = (k1.k2)^2 * 2 ... done by hand in DERIVATION.md;
# numerical: Gamma = 7.7 eV for F_pi = 92.2 MeV
GamNum = float((alpha ** 2 * m ** 3 / (64 * sp.pi ** 3 * Fpi ** 2)).subs({alpha: 1 / 137.036, m: 0.1349768, Fpi: 0.0922}))
print('   Gamma(pi0->gg) (anomaly, F_pi = 92.2 MeV) = %.3f eV' % (GamNum * 1e9))
ck.check('anomaly width ~ 7.7-7.8 eV (cf. measured ~7.8 eV)', 7.5 < GamNum * 1e9 < 8.0)
QQ = sp.symbols('QQ', positive=True)
FBL = F0 / (1 + QQ / (8 * sp.pi ** 2 * Fpi ** 2))
ck.zero('Brodsky-Lepage interpolation F(0)/(1 + Q^2/(8 pi^2 F_pi^2)): Q^2 F -> 2 F_pi = sqrt2 f  (matches the LO pQCD limit)',
        sp.limit(QQ * FBL, QQ, sp.oo) - 2 * Fpi)

print('=== 5. sum over polarizations used for the width (explicit) ===')
# sum_{pol} |eps_{mu nu a b} e1^mu e2^nu k1^a k2^b|^2 with -g polarization sums
# explicit massless back-to-back photons in the pi0 rest frame
mpi = sp.symbols('mpi', positive=True)
k1v = [mpi / 2, 0, 0, mpi / 2]
k2v = [mpi / 2, 0, 0, -mpi / 2]
tot = 0
k1l, k2l = low(k1v), low(k2v)
Eps = lambda a_, b_: sum(levi(a_, b_, c_, d_) * k1l[c_] * k2l[d_] for c_ in range(4) for d_ in range(4))   # eps^{a b c d} k1_c k2_d
for a_ in range(4):
    for b_ in range(4):
        tot += METRIC[a_] * METRIC[b_] * Eps(a_, b_) ** 2     # contract with g_{a a'} g_{b b'} (-g)(-g) = + g g
ck.zero('sum_pol |eps^{mu nu a b} e1_mu e2_nu k1_a k2_b|^2 = 2 (k1.k2)^2', sp.simplify(tot - 2 * dot(k1v, k2v) ** 2))
ck.zero('  = m^4/2 in the pi0 rest frame  => Gamma = (1/2m)(1/2)(1/8pi) e^4 F^2 m^4/2 = pi alpha^2 m^3 F^2/4',
        sp.simplify(tot - mpi ** 4 / 2) + 0 * sp.simplify(sp.Rational(1, 2) / mpi * sp.Rational(1, 2) / (8 * sp.pi) * (4 * sp.pi * alpha) ** 2 * mpi ** 4 / 2 - sp.pi * alpha ** 2 * mpi ** 3 / 4))
ck.zero('  phase-space algebra (1/2m)(1/2)(1/8pi)(4 pi alpha)^2 m^4/2 = pi alpha^2 m^3/4',
        sp.simplify(sp.Rational(1, 2) / mpi * sp.Rational(1, 2) / (8 * sp.pi) * (4 * sp.pi * alpha) ** 2 * mpi ** 4 / 2 - sp.pi * alpha ** 2 * mpi ** 3 / 4))

ck.summary()
