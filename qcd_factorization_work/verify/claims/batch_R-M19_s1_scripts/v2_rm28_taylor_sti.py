# R-M28 (illustration, verifier s1 v2): momentum-space Taylor subtraction (BPHZ-type, Euclidean subtraction point,
# one of the two options the reference's (U1) allows for massless lines) breaks the simplest Slavnov-Taylor identity,
# transversality of the gluon self-energy p_mu Pi^{mu nu}(p) = 0, by LOCAL non-transverse terms, including a
# mass-like constant term.  Restoring transversality needs a finite counterterm that is NOT of the form of a finite
# redefinition of couplings/fields of the massless gauge-invariant Lagrangian (a gluon mass term cannot be generated
# that way; a separate rescaling of the longitudinal part conflicts with the unrenormalized gauge-fixing term in a
# BRST-invariant scheme).  In DR + MS-bar the same self-energy is exactly transverse.
#
# One-loop structure (Euclidean): Pi_DR^{mu nu}(p) = (p^2 d^{mu nu} - p^mu p^nu) [A/eps + B ln(p^2/mu^2) + C].
# BPHZ (degree-2 Taylor subtraction at p0):  Pi_R = Pi_DR - T_{p0}^{(2)} Pi_DR   (subtraction commutes with DR).
# Polynomial parts are reproduced by their own Taylor polynomial, so only B*T[(p^2 d - p p) ln p^2] matters.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

D = 4
p = sp.symbols('p1:5', real=True)
m = sp.symbols('m', positive=True)
p0 = (0, 0, 0, m)                                  # Euclidean subtraction point, |p0| = m
psq = sum(pi**2 for pi in p)

def F(mu, nu, pp):
    s = sum(x**2 for x in pp)
    return (s * (1 if mu == nu else 0) - pp[mu] * pp[nu]) * sp.log(s)

def taylor2(mu, nu):
    sub = dict(zip(p, p0))
    expr = F(mu, nu, p)
    val = expr.subs(sub)
    grad = [sp.diff(expr, p[a]).subs(sub) for a in range(D)]
    hess = [[sp.diff(expr, p[a], p[b]).subs(sub) for b in range(D)] for a in range(D)]
    dp = [p[a] - p0[a] for a in range(D)]
    return sp.expand(val + sum(grad[a] * dp[a] for a in range(D))
                     + sp.Rational(1, 2) * sum(hess[a][b] * dp[a] * dp[b] for a in range(D) for b in range(D)))

T = [[taylor2(mu, nu) for nu in range(D)] for mu in range(D)]
# check: exact transversality of F itself
print('p_mu F^{mu nu} (should be 0):', [sp.simplify(sum(p[mu] * F(mu, nu, p) for mu in range(D))) for nu in range(D)])
viol = [sp.factor(sp.expand(sum(p[mu] * T[mu][nu] for mu in range(D)))) for nu in range(D)]
print('p_mu T^{mu nu}(p) for nu = 1..4:')
for nu in range(D):
    print('   nu=%d:' % (nu + 1), viol[nu])
T0 = [[sp.simplify(T[mu][nu].subs(dict(zip(p, (0, 0, 0, 0))))) for nu in range(D)] for mu in range(D)]
print('constant (p-independent, mass-like) term T^{mu nu}(0) =')
sp.pprint(sp.Matrix(T0))
print('=> Pi_R = Pi_DR - T Pi_DR violates p_mu Pi_R^{mu nu} = 0 by local polynomials (degree <= 3 in p) and contains a')
print('   constant non-transverse term ~ m^2: the BPHZ-subtracted self-energy differs from the (transverse) MS-bar one by')
print('   finite NON-INVARIANT local terms.')

# contrast: zero-momentum Taylor subtraction of an amplitude that is analytic and transverse at p = 0
# (massive electron loop in QED): (p^2 d - p p) Pi(p^2) with Pi analytic -> degree-2 Taylor polynomial (p^2 d - pp) Pi(0).
c0, c1 = sp.symbols('c0 c1')
G = lambda mu, nu: (psq * (1 if mu == nu else 0) - p[mu] * p[nu]) * (c0 + c1 * psq)
T2zero = [[sp.expand(sp.series(sp.series(sp.series(sp.series(G(mu, nu), p[0], 0, 3).removeO(), p[1], 0, 3).removeO(), p[2], 0, 3).removeO(), p[3], 0, 3).removeO()) for nu in range(D)] for mu in range(D)]
# keep only total degree <= 2
def deg_le2(e):
    poly = sp.Poly(e, *p)
    return sum(coef * sp.prod([v**k for v, k in zip(p, mon)]) for mon, coef in zip(poly.monoms(), poly.coeffs()) if sum(mon) <= 2)
T2zero = [[deg_le2(T2zero[mu][nu]) if T2zero[mu][nu] != 0 else 0 for nu in range(D)] for mu in range(D)]
print('zero-momentum Taylor (analytic transverse amplitude): p_mu T^{mu nu} =',
      [sp.simplify(sum(p[mu] * T2zero[mu][nu] for mu in range(D))) for nu in range(D)], ' (transverse)')
