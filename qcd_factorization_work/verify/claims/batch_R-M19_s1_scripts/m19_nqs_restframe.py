# R-M19: check the rest-frame reduction of the NQS NNLO pole (PLB 613 (2005) 45, eqs. (gn),(gn1) of hep-ph/0501235)
#   Sigma^(2) = alpha_s^2 * 4/(3 eps) * [ (P.q)^2/P^4 - q^2/P^2 ]
# In the pair rest frame with c(P/2+q), cbar(P/2-q) both on shell (mass m_c):  P.q = 0, P^2 = 4 E^2,
# q = (0, qvec).  NQS write  = alpha_s^2 * 4/(3 eps) * qvec^2/(4 m_c^2) = alpha_s^2 * 1/(3 eps) * v^2/4,
# with v the relative velocity.  We verify both equalities (to leading order in v, P^2 ~ 4 m_c^2,
# relative velocity v = 2|qvec|/m_c).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

mc, qv, eps, als = sp.symbols('m_c q_v epsilon alpha_s', positive=True)
E = sp.sqrt(mc**2 + qv**2)
# four-vectors (t,x,y,z) metric (+,-,-,-)
P = sp.Matrix([2*E, 0, 0, 0])
q = sp.Matrix([0, 0, 0, qv])
g = sp.diag(1, -1, -1, -1)
dot = lambda a, b: (a.T*g*b)[0]
# on-shell check of the constituents
p1 = P/2 + q; p2 = P/2 - q
print('p1^2 - m^2 =', sp.simplify(dot(p1, p1) - mc**2), '; p2^2 - m^2 =', sp.simplify(dot(p2, p2) - mc**2))
Sigma = als**2*sp.Rational(4, 3)/eps*(dot(P, q)**2/dot(P, P)**2 - dot(q, q)/dot(P, P))
print('Sigma (exact, rest frame) =', sp.simplify(Sigma))
# leading order in v: P^2 -> 4 m_c^2
Sigma_LO = sp.series(Sigma, qv, 0, 3).removeO()
print('Sigma to O(q^2)         =', sp.simplify(Sigma_LO))
v = sp.symbols('v', positive=True)
Sigma_v = sp.simplify(Sigma_LO.subs(qv, v*mc/2))
print('with q = v m_c/2        =', Sigma_v, ' ; NQS (gn1): alpha_s^2/(3 eps) * v^2/4 =', als**2/(3*eps)*v**2/4)
print('difference              =', sp.simplify(Sigma_v - als**2/(3*eps)*v**2/4))
# PRD 72 (2005) 114012 eq. (IIIdivergence):  2 Re III = - alpha_s^2/(3 eps) v^2/4  (sign convention of that paper)
print('=> the uncancelled NNLO pole is proportional to alpha_s^2 v^2/eps (magnitude alpha_s^2 v^2/(12 eps)), as claimed.')
