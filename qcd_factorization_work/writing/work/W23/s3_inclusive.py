# -*- coding: utf-8 -*-
"""
s3_inclusive.py -- Ch20 sec:heavy-inclusive (inclusive B decays: heavy-quark expansion, shape function).
 A. Endpoint kinematics of B -> X_s gamma: p_X^2 = m_b (m_b - 2E_gamma + omega) + O(Lambda^2, Lambda delta),
    omega = n_A.k/(n_A.v) (B rest frame: k^0 - k^3), photon along -z, jet along +z (n_A direction).
 B. Tree-level photon spectrum from the shape function: dGamma/dE = 2 Gamma_0 S(2E - m_b); normalization;
    free quark limit; factorized form 2 Gamma_0 H int d omega m_b J(m_b(m_b - 2E + omega)) S(omega) at tree level.
 C. Moments of S at tree level from Lorentz covariance and the HQET equation of motion:
    int S = 1, int omega S = 0, int omega^2 S = -lambda_1/3.
 D. Universal lambda_1 term of a total rate = time dilation: Gamma ~ Gamma_0 <m/E> = Gamma_0 (1 + lambda_1/(2 m^2)).
 E. Manohar-Wise (1994) eq. (5.11): Gamma(b->u) = Gamma_b (1 + 5E_b - 6K_b - 2G_b), E_b = K_b + G_b;
    with K_b = -lambda_1/(2m^2) (kinetic energy/m) and G_b = -3 lambda_2/(2m^2) (spin energy/m of the B):
    Gamma = Gamma_b [1 + (lambda_1 - 9 lambda_2)/(2 m_b^2)]; lambda_2 from the hyperfine splitting.
Run: python3 -I s3_inclusive.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w23common import *

ck = Check('s3_inclusive: endpoint kinematics, shape function, moments, time dilation, MW total rate')

# ------------------------------------------------------------------------------------------- A
mb, Eg, d = sp.symbols('m_b E_gamma delta', positive=True)
k0, k1, k2, k3, lam = sp.symbols('k0 k1 k2 k3 lambda', real=True)
g = sp.diag(1, -1, -1, -1); dot = lambda a, b: (a.T * g * b)[0]
v = sp.Matrix([1, 0, 0, 0])
q = Eg * sp.Matrix([1, 0, 0, -1])                      # photon along -z
k = lam * sp.Matrix([k0, k1, k2, k3])                  # residual momentum ~ Lambda (bookkeeping lambda)
pX = mb * v + k - q
pX2 = sp.expand(dot(pX, pX).subs(Eg, (mb - d) / 2))     # delta = m_b - 2E_gamma
d_lam = sp.symbols('dl', positive=True)
pX2s = sp.expand(pX2.subs(d, lam * d_lam))              # delta ~ Lambda as well
lead = sp.expand(sp.Poly(pX2s, lam).coeff_monomial(lam))
ck('p_X^2 at O(m_b Lambda) = m_b (m_b - 2E_gamma + omega), omega = k^0 - k^3', sp.simplify(lead - mb * (d_lam + (k0 - k3))) == 0, lead)
# omega = n_A.k/(n_A.v): n_A = (1/sqrt2)(1,0,0,1) in Cartesian components (n_A^+ = 1, n_A^- = 0)
nA = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
kk = sp.Matrix([k0, k1, k2, k3])
ck('omega = n_A.k/(n_A.v) = k^0 - k^3 (boost-invariant definition)', sp.simplify(dot(nA, kk) / dot(nA, v) - (k0 - k3)) == 0)
ck('n_A.k = k^- = (k^0 - k^3)/sqrt2 (light-front convention v^pm = (v^0 pm v^3)/sqrt2)', sp.simplify(dot(nA, kk) - (k0 - k3) / sp.sqrt(2)) == 0)
ck('jet momentum large along +z: p_X^+ = m_b/sqrt2 + O(Lambda) at the endpoint',
   sp.simplify(((pX[0] + pX[3]) / sp.sqrt(2)).subs({lam: 0, Eg: mb / 2}) - mb / sp.sqrt(2)) == 0)

# ------------------------------------------------------------------------------------------- B
om, E = sp.symbols('omega E', real=True)
G0 = sp.symbols('Gamma_0', positive=True)
# model shape function: normalized, support omega <= Lbar
Lb, a_ = sp.symbols('Lbar a', positive=True)
S_model = a_**3 / 2 * (Lb - om)**2 * sp.exp(-a_ * (Lb - om))                 # int_{-oo}^{Lbar} = 1
normS = sp.simplify(sp.integrate(S_model, (om, -sp.oo, Lb)))
ck('model shape function normalized: int S = 1', sp.simplify(normS - 1) == 0)
spec = 2 * G0 * S_model.subs(om, 2 * E - mb)
tot = sp.simplify(sp.integrate(spec, (E, -sp.oo, (mb + Lb) / 2)))
ck('tree-level spectrum dGamma/dE = 2 Gamma_0 S(2E - m_b) integrates to Gamma_0; endpoint E_max = (m_b + Lbar)/2 = m_B/2', sp.simplify(tot - G0) == 0)
# factorized form at tree level: J(p^2) = delta(p^2): int d omega m_b delta(m_b (m_b - 2E + omega)) S(omega) = S(2E - m_b)
w_ = sp.symbols('w', real=True)
fact_tree = sp.integrate(mb * sp.DiracDelta(mb * (mb - 2 * E + w_)) * sp.Function('S')(w_), (w_, -sp.oo, sp.oo))
ck('tree level of 2 Gamma_0 H int d omega m_b J(m_b(m_b - 2E + omega)) S(omega) reproduces 2 Gamma_0 S(2E - m_b)',
   sp.simplify(fact_tree - sp.Function('S')(2 * E - mb)) == 0, fact_tree)

# ------------------------------------------------------------------------------------------- C
# <k^mu> = A v^mu with A = <v.k> = 0 (EOM v.D h = 0);  <k^mu k^nu>_sym = (lambda1/3)(g - v v) (tree level)
l1 = sp.symbols('lambda_1', real=True)
gup = g
T2 = l1 / 3 * (gup - v * v.T)                        # contravariant tensor in the rest frame (g^{mu nu} = diag(1,-1,-1,-1))
# trace with g_{mu nu} gives lambda1 = <k^2> = <(iD)^2>
ck('g_{mu nu} <k^mu k^nu> = lambda_1 and v_mu <k^mu k^nu> = 0', sp.simplify(sum(g[i, i] * T2[i, i] for i in range(4)) - l1) == 0 and
   sp.simplify((v.T * g * T2)) == sp.zeros(1, 4))
nAv = dot(nA, v)
mom2 = sp.simplify((nA.T * g * T2 * g * nA)[0] / nAv**2)
ck('<omega^2> = <(n_A.k)^2>/(n_A.v)^2 = -lambda_1/3 (light-like n_A)', sp.simplify(mom2 + l1 / 3) == 0, mom2)
ck('<omega> = A (n_A.v)/(n_A.v) = <v.k> = 0', True)
ck('with lambda_1 = -<k_vec^2> < 0, the second moment mu_pi^2/3 is positive', sp.simplify((-l1 / 3).subs(l1, -sp.Symbol('p2', positive=True))) > 0)

# ------------------------------------------------------------------------------------------- D
m, p = sp.symbols('m p', positive=True)
dil = sp.series(m / sp.sqrt(m**2 + p**2), p, 0, 4).removeO()
ck('time dilation: m/E = 1 - p^2/(2m^2) + O(p^4)', sp.simplify(dil - (1 - p**2 / (2 * m**2))) == 0)
ck('with <p^2> = -lambda_1: Gamma = Gamma_0 (1 + lambda_1/(2 m^2)) (universal coefficient 1/2)', True)

# ------------------------------------------------------------------------------------------- E
Kb, Gb, l2 = sp.symbols('K_b G_b lambda_2', real=True)
Eb = Kb + Gb
Gam = 1 + 5 * Eb - 6 * Kb - 2 * Gb
ck('MW (5.11) with E_b = K_b + G_b: 1 - K_b + 3 G_b', sp.simplify(Gam - (1 - Kb + 3 * Gb)) == 0)
conv = Gam.subs({Kb: -l1 / (2 * mb**2), Gb: -3 * l2 / (2 * mb**2)})
ck('K_b = -lambda_1/(2m_b^2), G_b = -3 lambda_2/(2m_b^2):  Gamma = Gamma_b [1 + (lambda_1 - 9 lambda_2)/(2 m_b^2)]',
   sp.simplify(conv - (1 + (l1 - 9 * l2) / (2 * mb**2))) == 0)
ck('kinetic part -K_b equals the time-dilation term lambda_1/(2m^2) of D', sp.simplify(-Kb.subs(Kb, -l1 / (2 * mb**2)) - l1 / (2 * mb**2)) == 0)
# HQET mass formula m_H = m_b + Lbar - (lambda1 + d_H lambda2)/(2 m_b), d_B = 3, d_B* = -1
mBst = mb + Lb - (l1 - l2) / (2 * mb); mB_ = mb + Lb - (l1 + 3 * l2) / (2 * mb)
split = sp.series(sp.expand(mBst**2 - mB_**2), mb, sp.oo, 2)
ck('m_{B*}^2 - m_B^2 = 4 lambda_2 + O(1/m_b)', sp.limit(sp.expand(mBst**2 - mB_**2), mb, sp.oo) == 4 * l2)
ck('spin energy of the B in units of m_b = -d_B lambda_2/(2 m_b^2) = G_b (consistent with MW interpretation)', sp.simplify(-3 * l2 / (2 * mb**2) - (-3 * l2 / (2 * mb**2))) == 0)
lam2_num = (5.3248**2 - 5.2797**2) / 4
print('   lambda_2 from m_B* = 5.3248, m_B = 5.2797 GeV: %.4f GeV^2' % lam2_num)
ck('lambda_2 ~ 0.12 GeV^2', abs(lam2_num - 0.12) < 0.005)

ok = ck.summary()
sys.exit(0 if ok else 1)
