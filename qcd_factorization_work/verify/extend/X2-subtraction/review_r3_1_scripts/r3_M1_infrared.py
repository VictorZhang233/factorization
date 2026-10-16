"""Review r3_1 -- infrared behaviour of (M1) beyond one loop (massless super-renormalizable model, [g] = mass^1, d = 4).

(a) Exact statement used in the review.  The one-loop triangle with the exchanged phi line raised to a power nu
    (nu = 1: bare triangle; nu = 2 + eps: one bare psi-bubble insertion, since B0 ~ (-k^2)^-eps and [g^2] = mass^2;
    nu = 2: the MS-bar counterterm part of a renormalized bubble insertion; nu = 3: the UV-finite two-loop 'kite'
    self-energy insertion Pi_2 = c/(-k^2), c > 0) has the parametric representation
        I(nu) = Gamma(nu + 2 - d/2)/Gamma(nu) int_simplex alpha_g^(nu-1) F^(d/2 - nu - 2),
        F = alpha_1 alpha_2 Q^2 + m^2 alpha_g (alpha_1 + alpha_2)    (U = 1).
    At the corner alpha_1, alpha_2 -> 0 (the soft phi momentum k -> 0) F ~ m^2 r, r = alpha_1 + alpha_2, so the corner
    contributes int r dr r^(d/2 - nu - 2): absolutely convergent iff nu < d/2 = 2 - eps.
    Hence every self-energy insertion on the exchanged phi (nu >= 2) is IR divergent at fixed m for eps in [0, eps0].
(b) Numerical illustration at d = 4 (eps = 0): corner-cut integrals J(nu, delta) = int_{r > delta} ... grow like
    const (nu = 1), ln(1/delta) (nu = 2), 1/delta (nu = 3); with the renormalized log, nu = 2 with ln F -> ln^2.
(c) Soft power counting for (M1) at fixed m: a soft subgraph with V_S internal (all-soft) cubic vertices and n_a
    endpoints on non-soft lines has IR degree omega_IR = n_a - V_S (d = 4); omega_IR <= 0 is divergent.
    Examples: single phi exchange (V_S = 0, n_a = 2): +2; one-loop phi self-energy: 0; kite: -2; psi box coupled to
    four soft phi's attached to the two external quark lines (no self-energy insertion at all): 0.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 20
Q2 = mp.mpf(1); m2 = mp.mpf('0.01')

def J(nu, delta, logpow=0):
    # simplex alpha_g = 1 - r, alpha_1 = r s, alpha_2 = r (1-s), Jacobian r; d = 4
    def f(r, s):
        a1 = r*s; a2 = r*(1 - s); ag = 1 - r
        F = a1*a2*Q2 + m2*ag*(a1 + a2)
        return r*ag**(nu - 1)*F**(-nu)*(abs(mp.log(F)))**logpow
    return mp.quad(lambda r: mp.quad(lambda s: f(r, s), [0, mp.mpf(1)/2, 1]), [delta, 10*delta, 100*delta, mp.mpf(1)/10, 1])

for nu, lp, lab in [(1, 0, 'nu=1 (triangle)'), (2, 0, 'nu=2 (counterterm part of bubble insertion)'),
                    (2, 1, 'nu=2 with |ln F| (renormalized bubble log)'), (3, 0, 'nu=3 (kite insertion)')]:
    vals = [J(nu, mp.mpf(10)**(-k), lp) for k in (4, 6, 8, 10)]
    print(f"{lab:45s}: J(delta=1e-4,1e-6,1e-8,1e-10) = {[mp.nstr(v, 8) for v in vals]}", flush=True)
print("criterion: corner integral converges iff nu < d/2; at d = 4 only nu = 1 converges.")
