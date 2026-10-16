# R-M19 (independent re-derivation, verifier s1 v2)
# NQS PLB 613 (2005) 45 [hep-ph/0501235], eqs. (gn), (gn1):
#   Sigma^(2)(P,q,l) = alpha_s^2 * 4/(3 eps) * [ (P.q)^2/P^4 - q^2/P^2 ]          (invariant form)
#   rest frame:      = alpha_s^2 * 4/(3 eps) * qvec^2/(4 m_c^2) = alpha_s^2 * 1/(3 eps) * v^2/4
# NQS PRD 72 (2005) 114012 [hep-ph/0509021], eq. (IIIdivergence):  2 Re III = - alpha_s^2/(3 eps) * v^2/4
# Checks: (1) invariant bracket is Lorentz invariant (evaluate in rest frame and in a boosted frame);
#         (2) rest-frame value to O(q^2) and the identification v = relative velocity = 2|q|/m;
#         (3) hence the uncancelled pole is O(alpha_s^2 v^2 / eps), i.e. NNLO and relative order v^2.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

m, qv, eps, als, eta = sp.symbols('m q_v epsilon alpha_s eta', positive=True)
g = sp.diag(1, -1, -1, -1)
dot = lambda a, b: sp.simplify((a.T * g * b)[0])

E = sp.sqrt(m**2 + qv**2)
P = sp.Matrix([2 * E, 0, 0, 0])          # pair rest frame
q = sp.Matrix([0, qv / sp.sqrt(3), qv / sp.sqrt(3), qv / sp.sqrt(3)])   # arbitrary direction, |q| = q_v
p1, p2 = P / 2 + q, P / 2 - q
assert sp.simplify(dot(p1, p1) - m**2) == 0 and sp.simplify(dot(p2, p2) - m**2) == 0

def bracket(P, q):
    return sp.simplify(dot(P, q)**2 / dot(P, P)**2 - dot(q, q) / dot(P, P))

b_rest = bracket(P, q)
# boost along z with rapidity eta
B = sp.Matrix([[sp.cosh(eta), 0, 0, sp.sinh(eta)], [0, 1, 0, 0], [0, 0, 1, 0], [sp.sinh(eta), 0, 0, sp.cosh(eta)]])
b_boost = bracket(B * P, B * q)
print('bracket (rest frame)      =', b_rest)
print('bracket (boosted) - rest  =', sp.simplify(b_boost - b_rest))
Sigma = als**2 * sp.Rational(4, 3) / eps * b_rest
Sigma_LO = sp.series(Sigma, qv, 0, 3).removeO()
print('Sigma to O(q^2)           =', sp.simplify(Sigma_LO))
# single-quark velocity |q|/E ~ |q|/m, relative velocity v = 2|q|/m (NQS: "relative velocity of the heavy quark pair")
v = sp.symbols('v', positive=True)
Sigma_v = sp.simplify(Sigma_LO.subs(qv, v * m / 2))
target = als**2 / (3 * eps) * v**2 / 4
print('Sigma(v)                  =', Sigma_v, '   NQS (gn1) =', target, '   diff =', sp.simplify(Sigma_v - target))
print('Exact (all orders in q):  Sigma = alpha_s^2 q^2/(3 eps (m^2+q^2)) ->', sp.simplify(Sigma - als**2 * qv**2 / (3 * eps * (m**2 + qv**2))))
print('=> uncancelled single IR pole of order alpha_s^2 v^2/eps (magnitude alpha_s^2 v^2/(12 eps)); NNLO, relative order v^2.')
