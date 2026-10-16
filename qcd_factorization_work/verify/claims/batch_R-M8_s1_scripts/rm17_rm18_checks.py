# R-M17: Wandzura-Wilczek twist-3 DAs of a transversely polarised vector meson (Ball-Braun 1996 relations as printed in
# Mankiewicz-Piller, PRD 61 (2000) 074013, eqs. for g^v, g^a, Phi_par) and the endpoint behaviour of the MP integrals
#   I_1 = int dtau/tau [4 g^v - 2 Phi/tau + g^a/(2 tau taubar)],   I_2 = int dtau/tau [2 g^v + g^a/(2 tau taubar)].
# R-M18: colour factor of the Rogers-Mulders double-Sivers graphs, Tr[t^a t^b] Tr[t^b t^a] = T_F^2 (N_c^2 - 1).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np

u, t, v = sp.symbols('u tau v', positive=True)
def ww(phi):
    gv = sp.Rational(1, 2) * (sp.integrate(phi.subs(u, v) / (1 - v), (v, 0, t)) + sp.integrate(phi.subs(u, v) / v, (v, t, 1)))
    ga = 2 * ((1 - t) * sp.integrate(phi.subs(u, v) / (1 - v), (v, 0, t)) + t * sp.integrate(phi.subs(u, v) / v, (v, t, 1)))
    Ph = sp.Rational(1, 2) * ((1 - t) * sp.integrate(phi.subs(u, v) / (1 - v), (v, 0, t)) - t * sp.integrate(phi.subs(u, v) / v, (v, t, 1)))
    return sp.simplify(gv), sp.simplify(ga), sp.simplify(Ph)

for name, phi in [('asymptotic 6u(1-u)', 6 * u * (1 - u)), ('endpoint-suppressed 30u^2(1-u)^2', 30 * u**2 * (1 - u)**2),
                  ('a2 = 0.3 Gegenbauer', 6 * u * (1 - u) * (1 + sp.Rational(3, 10) * sp.Rational(3, 2) * (5 * (2 * u - 1)**2 - 1)))]:
    gv, ga, Ph = ww(phi)
    sigma = sp.integrate(phi / u, (u, 0, 1))
    gv0 = sp.limit(gv, t, 0)
    i1 = sp.limit(4 * gv - 2 * Ph / t + ga / (2 * t * (1 - t)), t, 0)   # tau * integrand of I_1
    i2 = sp.limit(2 * gv + ga / (2 * t * (1 - t)), t, 0)
    print('%-34s sigma_phi = int phi/u = %s ; g^v(0) = %s (= sigma/2: %s) ; tau*[I_1 integrand] -> %s ; tau*[I_2 integrand] -> %s'
          % (name, sigma, gv0, sp.simplify(gv0 - sigma / 2) == 0, sp.simplify(i1), sp.simplify(i2)))
    # normalisation checks of the WW DAs: int g^v = 1, int g^a = 1 (Ball-Braun normalisation), and symmetry
    print('   int_0^1 g^v = %s, int_0^1 g^a = %s, g^v symmetric: %s' % (sp.simplify(sp.integrate(gv, (t, 0, 1))),
          sp.simplify(sp.integrate(ga, (t, 0, 1))), sp.simplify(gv - gv.subs(t, 1 - t)) == 0))
print('=> the endpoint integrands behave like const/tau: logarithmic divergence, present for any phi with int phi/u != 0,')
print('   including phi ~ u^2 at the endpoint; for phi = 6u(1-u) the constants are 12 and 6 (MP print 12 and 9).')
print('   For comparison int dz phi(z)/z^2 with phi = 6z(1-z) is also log divergent (coefficient 6), but it CONVERGES')
print('   for phi = 30 z^2 (1-z)^2, whereas the WW twist-3 integrals still diverge: the "phi/z^2" description misses this.')
print('   int_0^1 30 z^2(1-z)^2/z^2 dz =', sp.integrate(30 * (1 - u)**2, (u, 0, 1)))

# ---------------------------------------------------------------- R-M18 colour factor
lam = np.zeros((8, 3, 3), complex)
lam[0][0, 1] = lam[0][1, 0] = 1
lam[1][0, 1] = -1j; lam[1][1, 0] = 1j
lam[2][0, 0] = 1; lam[2][1, 1] = -1
lam[3][0, 2] = lam[3][2, 0] = 1
lam[4][0, 2] = -1j; lam[4][2, 0] = 1j
lam[5][1, 2] = lam[5][2, 1] = 1
lam[6][1, 2] = -1j; lam[6][2, 1] = 1j
lam[7][0, 0] = lam[7][1, 1] = 1 / np.sqrt(3); lam[7][2, 2] = -2 / np.sqrt(3)
T = lam / 2
cf = sum(np.trace(T[a] @ T[b]) * np.trace(T[b] @ T[a]) for a in range(8) for b in range(8))
print('SU(3): sum_ab Tr[t^a t^b] Tr[t^b t^a] = %.12f ; T_F^2 (N_c^2-1) = %.12f' % (cf.real, 0.25 * 8))
single = [np.trace(T[a]) for a in range(8)]
print('Tr[t^a] = 0 for all a (single-gluon colour-traced Wilson loop vanishes):', np.allclose(single, 0))
CF = sum(T[a] @ T[a] for a in range(8))
print('C_F check: sum_a t^a t^a = %.6f * 1' % CF[0, 0].real)
