# R-M24 (illustration, verifier s1 v2) of the Collins-Scalise mechanism (PRD 50 (1994) 4117, Sec. 4.4):
# an operator inserted at ZERO momentum transfer on an internal massless line doubles that propagator; the resulting
# Green function behaves like 1/p^2 as the external (massless) leg goes on shell, which compensates the factor p^2
# (inverse propagator) used in the LSZ/BRST-Ward-identity argument that 'the matrix element vanishes on shell'.
# For non-zero momentum transfer the two propagators carry different momenta and no 1/p^2 enhancement arises.
# Standard massless one-loop integral (Minkowski, after Wick rotation), d^Dk/(i pi^{D/2}):
#   G(a,b) = int 1/[(-k^2)^a (-(k+p)^2)^b] = (-p^2)^{D/2-a-b} Gamma(a+b-D/2) Gamma(D/2-a) Gamma(D/2-b)
#                                                         / [Gamma(a) Gamma(b) Gamma(D-a-b)]
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

eps, P2 = sp.symbols('epsilon P2', positive=True)      # P2 = -p^2 > 0 (Euclidean side)
Dd = 4 - 2 * eps

def G(a, b):
    return P2**(Dd / 2 - a - b) * sp.gamma(a + b - Dd / 2) * sp.gamma(Dd / 2 - a) * sp.gamma(Dd / 2 - b) / (
        sp.gamma(a) * sp.gamma(b) * sp.gamma(Dd - a - b))

single = sp.simplify(G(1, 1))
double = sp.simplify(G(2, 1))
print('G(1,1) =', single)
print('G(2,1) (doubled propagator = zero-momentum insertion) =', double)
print('(-p^2) * G(2,1) =', sp.simplify(P2 * double))
ser = sp.series(sp.simplify(P2 * double), eps, 0, 1).removeO()
print('   expanded at fixed p^2 != 0:', sp.simplify(sp.expand(ser)))
ser1 = sp.expand(sp.series(sp.simplify(P2 * single), eps, 0, 1).removeO())
print('(-p^2) * G(1,1) expanded       :', sp.simplify(ser1))
for name, e in (('(-p^2) G(1,1)', ser1), ('(-p^2) G(2,1)', sp.expand(ser))):
    cm1 = sp.simplify(e.coeff(eps, -1)); c0 = sp.simplify(e.coeff(eps, 0))
    print('   %s: coefficient of 1/eps = %s (limit p^2->0: %s);  eps^0 coefficient = %s (limit p^2->0: %s)'
          % (name, cm1, sp.limit(cm1, P2, 0, '+'), c0, sp.limit(c0, P2, 0, '+')))
print('=> p^2 x G(1,1) -> 0 on shell (log at worst), but (-p^2) x G(2,1) = -1/eps + ln(-p^2) + gamma_E + O(eps) does NOT vanish as p^2 -> 0:')
print('   the "factor of zero" is compensated exactly when the insertion carries zero momentum (forward kinematics).')
