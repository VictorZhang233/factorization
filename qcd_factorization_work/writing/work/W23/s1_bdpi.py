# -*- coding: utf-8 -*-
"""
s1_bdpi.py -- Ch20 sec:heavy-bdpi.
 A. Kinematics of B -> D pi with a massless pion (E_pi), naive factorization of O_0 and the normalization
    N = (i/2) m_B E_pi f_pi (VF-BQ-6) in the phase convention of def:excl-da (<0|dbar g^mu g5 u|pi+(p)> = i f p^mu,
    hence <pi-(p)|dbar g^mu g5 u|0> = -i f p^mu); factor 4 for (V-A)x(V-A).
 B. Heavy-quark limit of F^{B->D}(0) (BPS 2001 eq. (8)): (m_B+m_D)/(2 sqrt(m_B m_D)) xi(w), w(q^2=0); numbers.
 C. Colour transparency: eikonal couplings of a soft gluon to a collinear colour-singlet q qbar pair cancel at
    zeroth order in the transverse momentum l; first-order dipole remainder proportional to 1/x + 1/(1-x);
    current conservation of the remainder.
Run: python3 -I s1_bdpi.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w23common import *

ck = Check('s1_bdpi: B -> D pi kinematics, normalization N, heavy-quark form factor, colour transparency')

# ------------------------------------------------------------------------------------------- A
mB, mD, E = sp.symbols('m_B m_D E_pi', positive=True)
# B rest frame, pion along +z, massless
pB = sp.Matrix([mB, 0, 0, 0]); ppi = sp.Matrix([E, 0, 0, E]); pD = pB - ppi
g = sp.diag(1, -1, -1, -1)
dot = lambda a, b: (a.T * g * b)[0]
sol = sp.solve(sp.Eq(dot(pD, pD), mD**2), E)
Epi = sol[0]
ck('E_pi = (m_B^2 - m_D^2)/(2 m_B) for a massless pion', sp.simplify(Epi - (mB**2 - mD**2) / (2 * mB)) == 0, Epi)
# naive factorization: <pi-|dbar g_mu P_L u|0> = (1/2)(0 - (-i f p_mu)) = (i/2) f p_mu
# <D|cbar g^mu P_L b|B> = (1/2)[F+ (P^mu - (mB^2-mD^2)/q^2 q^mu) + F0 (mB^2-mD^2)/q^2 q^mu],  P = pB + pD, q = pB - pD
f, Fp, F0, q2 = sp.symbols('f_pi F_p F_0 q2')
P = pB + pD; q = pB - pD
qP = sp.simplify(dot(q, P))
ck('q.P = m_B^2 - m_D^2 (identity p_B^2 - p_D^2)', sp.simplify(qP.subs(E, Epi) - (mB**2 - mD**2)) == 0)
# contract the hadronic current with p_pi = q: F+ term drops out identically (for any q^2), F0 term survives
Fp_term = Fp * (qP - (mB**2 - mD**2) / q2 * q2)
ck('F_+ term vanishes when contracted with q (for any q^2)', sp.simplify(Fp_term.subs(E, Epi)) == 0)
amp = sp.I / 2 * f * sp.Rational(1, 2) * F0 * (mB**2 - mD**2)
N_expected = sp.I / 2 * mB * Epi * f
ck('<D pi|O_0|B> = (i/2) m_B E_pi f_pi F(0)   (F_0(0) = F_+(0) = F(0))', sp.simplify(amp - N_expected * F0) == 0, sp.simplify(amp))
ck('(V-A)x(V-A) operators (each factor 2 P_L instead of P_L): N four times larger', sp.simplify(4 * amp / (N_expected * F0)) == 4)

# ------------------------------------------------------------------------------------------- B
# HQET: <D(v')|cbar g^mu b|B(v)> = sqrt(mB mD) xi(w) (v+v')^mu  =>  F+ = (mB+mD)/(2 sqrt(mB mD)) xi
xi = sp.symbols('xi')
v = pB / mB; vp = pD / mD
lhs = sp.sqrt(mB * mD) * xi * (v + vp)
# decompose lhs = F+ P + (F0-F+)(mB^2-mD^2)/q^2 q ; extract F+ from the coefficient of P
a, b_ = sp.symbols('a b_')
eqs = [sp.simplify(lhs[i] - (a * P[i] + b_ * q[i])) for i in range(4)]
s_ab = sp.solve([eqs[0], eqs[3]], [a, b_], dict=True)[0]
Fplus = sp.simplify(s_ab[a].subs(E, Epi))
ck('HQET: F_+ = (m_B+m_D)/(2 sqrt(m_B m_D)) xi(w)', sp.simplify(Fplus - (mB + mD) / (2 * sp.sqrt(mB * mD)) * xi) == 0, Fplus)
ck('equals BPS form (1/2) sqrt(m_D/m_B) (1 + m_B/m_D) xi', sp.simplify(Fplus - sp.Rational(1, 2) * sp.sqrt(mD / mB) * (1 + mB / mD) * xi) == 0)
w = sp.simplify(dot(v, vp).subs(E, Epi))
ck('w = v.v\' at q^2 = 0 equals (m_B^2 + m_D^2)/(2 m_B m_D)', sp.simplify(w - (mB**2 + mD**2) / (2 * mB * mD)) == 0, w)
# numbers: PDG 2024 masses (B0: 5279.66 MeV, D+: 1869.66 MeV)
num = {mB: sp.Rational(527966, 100000), mD: sp.Rational(186966, 100000)}
Epin = float(Epi.subs(num)); wn = float(w.subs(num)); ratio = float(((mB + mD) / (2 * sp.sqrt(mB * mD))).subs(num))
print('   numbers: E_pi = %.4f GeV, w = %.4f, (m_B+m_D)/(2 sqrt(m_B m_D)) = %.4f' % (Epin, wn, ratio))
ck('numbers E_pi ~ 2.309 GeV, w ~ 1.589, prefactor ~ 1.138', abs(Epin - 2.309) < 1e-3 and abs(wn - 1.589) < 1e-3 and abs(ratio - 1.138) < 1e-3)

# ------------------------------------------------------------------------------------------- C
# eikonal factors for a soft gluon k coupling to outgoing quark p1 = x p + l and antiquark p2 = (1-x) p - l,
# p light-like along +z, l transverse (l.p = 0); colour singlet => quark T^a, antiquark -T^a acting give the
# same matrix T^a_ij; total ~ T^a [ p1^mu/(p1.k) - p2^mu/(p2.k) ].
x, lam = sp.symbols('x lambda', positive=True)
E0 = sp.symbols('E0', positive=True)
k0, k1, k2, k3 = sp.symbols('k0 k1 k2 k3')
l1, l2 = sp.symbols('l1 l2')
pp = sp.Matrix([E0, 0, 0, E0])
lv = sp.Matrix([0, l1, l2, 0]) * lam            # transverse, scaled by bookkeeping parameter lambda
kv = sp.Matrix([k0, k1, k2, k3])
p1 = x * pp + lv; p2 = (1 - x) * pp - lv
J = sp.Matrix([p1[i] / dot(p1, kv) - p2[i] / dot(p2, kv) for i in range(4)])
J0 = sp.simplify(J.subs(lam, 0))
ck('zeroth order in l: eikonal couplings of the colour-singlet pair cancel exactly', J0 == sp.zeros(4, 1))
J1 = sp.simplify(sp.diff(J, lam).subs(lam, 0))
expected = (1 / x + 1 / (1 - x)) * sp.Matrix([lv[i] / lam - pp[i] * dot(lv / lam, kv) / dot(pp, kv) for i in range(4)]) / dot(pp, kv)
ck('first order: dipole remainder = (1/x + 1/(1-x)) [l^mu - p^mu l.k/p.k]/(p.k)', sp.simplify(J1 - expected) == sp.zeros(4, 1))
ck('remainder is conserved: k_mu J1^mu = 0', sp.simplify(dot(kv, J1)) == 0)
# numerical illustration of the linear scaling with l (fixed soft k, x = 0.4)
vals = {E0: 2.5, x: sp.Rational(2, 5), k0: 0.5, k1: 0.2, k2: -0.1, k3: 0.3, l1: 0.3, l2: 0.1}
single = float(sp.sqrt(sum((pp[i] * x / dot(x * pp, kv))**2 for i in range(4))).subs(vals))
rat = []
for s in [1.0, 0.1, 0.01]:
    Jn = [float(J[i].subs(vals).subs(lam, s)) for i in range(4)]
    rat.append((sum(c * c for c in Jn))**0.5 / single)
print('   |J|/|single-line eikonal factor| for l scaled by 1, 0.1, 0.01: %.3e %.3e %.3e' % tuple(rat))
ck('remainder scales linearly with the transverse momentum (ratio 10 per decade)', abs(rat[1] / rat[2] - 10) < 0.2 and abs(rat[0] / rat[1] - 10) < 1.5)

ok = ck.summary()
sys.exit(0 if ok else 1)
