"""X2 final revision / r3_M1_infrared.py -- infrared behaviour of the massless super-renormalizable model (M1) beyond one
loop at fixed m (reviews r3_1 required fix 2, r3_2 required fixes 2-3; supersedes the claim of round-2 Cor 2.11 for (M1)).
Combines and extends the reviewers' checks (review_r3_1_scripts/r3_M1_infrared.py; review r3_2 chk/c7_M1_IR.py).

(a) Triangle with the exchanged phi line raised to a power nu (nu = 1: triangle; nu = 2: MS-bar counterterm part of a
    one-loop psi-bubble insertion, [g^2] = mass^2; nu = 2 + eps: bare bubble insertion; nu = 3 + 2 eps: UV-finite massless
    two-loop 'kite' self-energy, Sigma_2(k^2) = K(eps) (-k^2)^{-1-2eps}, K(0) = 6 zeta(3) x couplings > 0):
        I(nu) = Gamma(nu + 2 - d/2)/Gamma(nu) int_simplex a_g^{nu-1} F^{d/2-nu-2},  F = a1 a2 Q^2 + m^2 a_g (a1 + a2).
    Corner a1, a2 -> 0 (soft phi): F ~ m^2 r, r = a1 + a2, contribution int r^{d/2-nu-1} dr: absolutely convergent iff
    nu < d/2 = 2 - eps.  For nu = 3 + 2 eps: convergent only for eps < -1/3; the continued value is finite at eps = 0.
(b) Corner-cut integrals at eps = 0: const (nu = 1), ln(1/delta) (nu = 2), ln^2 (nu = 2 with the renormalized log), 1/delta
    (nu = 3).
(c) Fibered positive densities of 1/(D_g^n D_1 D_2) on 0 < k+ < P (closing on the D_1 pole): rho_n = (P-x)^{n-1}/(A^n D2hat),
    A = x m2 (1-x/P) + P kappa;  int_{x > delta} rho_n grows like ln(1/delta) (n = 2) and 1/delta (n = 3): the positive
    density of the three-loop kite graph (proportional to n = 3 + 2 eps) is not integrable for any eps in [0, eps0],
    although its DR value is finite at eps = 0  =>  'int |rho| = |int rho| = I_Gamma < oo' fails.
(d) Soft power counting at fixed m: a set S of internal lines that can be simultaneously soft, with connected complement,
    V_S all-soft (cubic) vertices and n_a endpoints on non-soft vertices:  2 I_S = 3 V_S + n_a, L_S = I_S - V_S, and
        (M1), d = 4:  omega_IR = 4 L_S - 2 I_S = n_a - V_S ;     (M2), d = 6:  omega_IR = 6 L_S - 2 I_S = 2 n_a > 0.
    omega_IR <= 0 means divergence (positive integrand after the parametric representation)."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import sympy as sp
mp.mp.dps = 20

print("(a) parametric corner exponent: integrand ~ r^(d/2 - nu - 1) near the soft corner; convergence iff nu < 2 - eps")
e = sp.Symbol('epsilon')
for lab, nu in [('triangle', 1), ('bubble counterterm', 2), ('bare bubble', 2 + e), ('kite', 3 + 2*e)]:
    expo = sp.simplify((2 - e) - nu - 1)
    crit = sp.solve(sp.Eq(expo, -1), e)
    print(f"   {lab:20s}: nu = {nu}; corner integrand r^({expo}) dr; boundary of convergence eps = {crit};"
          f" convergent at eps = 0: {bool(expo.subs(e, 0) > -1)}")
print("   kite: Gamma(nu+2-d/2) = Gamma(3+3eps) finite; only the corner pole at eps = -1/3 -> DR value finite at eps = 0")

print("\n(b) corner-cut integrals J(nu, delta) at eps = 0 (Q^2 = 1, m^2 = 0.01):")
Q2 = mp.mpf(1); m2 = mp.mpf('0.01')
def J(nu, delta, logpow=0):
    def f(r, s):
        a1 = r*s; a2 = r*(1 - s); ag = 1 - r
        F = a1*a2*Q2 + m2*ag*(a1 + a2)
        return r*ag**(nu - 1)*F**(-nu)*(abs(mp.log(F)))**logpow
    return mp.quad(lambda r: mp.quad(lambda s: f(r, s), [0, mp.mpf(1)/2, 1]), [delta, 10*delta, 100*delta, mp.mpf(1)/10, 1])
for nu, lp, lab in [(1, 0, 'nu=1 (triangle)'), (2, 0, 'nu=2 (bubble counterterm)'),
                    (2, 1, 'nu=2 with |ln F| (renormalized bubble)'), (3, 0, 'nu=3 (kite)')]:
    vals = [J(nu, mp.mpf(10)**(-k), lp) for k in (4, 6, 8)]
    print(f"   {lab:40s}: delta = 1e-4, 1e-6, 1e-8 -> {[mp.nstr(v, 8) for v in vals]}", flush=True)

print("\n(c) fibered positive densities rho_n of 1/(D_g^n D1 D2), 0 < x < P (P = P' = 1/sqrt2, m^2 = 0.01):")
P = Pp = 1/mp.sqrt(2); Qt2 = 2*P*Pp
def rho(n, x, k):
    u = x/P; A = P*k + x*m2*(1 - u); e2 = m2 + 2*Pp*x
    D2 = e2*(1 + m2/Qt2 + k/(Qt2*(1 - u))) + k
    return (P - x)**(n - 1)/(A**n*D2)
def Ix(n, d):
    f = lambda x: mp.quad(lambda k: rho(n, x, k), [0, x*m2, 1, mp.inf])
    pts = [d] + [mp.mpf(10)**j for j in range(int(mp.log10(d)) + 1, 0) if mp.mpf(10)**j < P] + [P]
    return mp.quad(f, pts)
for n in [1, 2, 3]:
    vals = [Ix(n, mp.mpf(d)) for d in ['1e-3', '1e-5', '1e-7']]
    print(f"   n={n}: int_(x > 1e-3, 1e-5, 1e-7) rho_n = {[mp.nstr(v, 8) for v in vals]}", flush=True)

print("\n(d) soft power counting (connected hard complement): (M1) omega = n_a - V_S ; (M2) omega = 2 n_a")
examples = [  # (description, I_S, V_S, n_a)
    ('single soft phi (triangle)', 1, 0, 2),
    ('two soft rungs (planar/crossed two-loop ladder)', 2, 0, 4),
    ('soft psi line + adjacent soft rung impossible (2 soft lines at a non-external vertex force the third)', None, None, None),
    ('one-loop psi-bubble on a soft phi (bubble lines soft)', 4, 2, 2),
    ('two-loop kite self-energy on a soft phi', 7, 4, 2),
    ('one-loop psi self-energy on a soft psi line (k -> p1)', 4, 2, 2),
    ('soft psi triangle with three soft phi legs on the external psi lines (3 loops)', 6, 3, 3),
    ('soft psi box with four soft phi legs (4 loops)', 8, 4, 4),
]
for d_, I_, V_, n_ in examples:
    if I_ is None:
        print(f"   {d_}"); continue
    assert 2*I_ == 3*V_ + n_, d_
    print(f"   {d_:78s}: I_S={I_}, V_S={V_}, n_a={n_}:  omega(M1) = {n_ - V_:+d}   omega(M2) = {2*n_:+d}")
print("   (M1): omega <= 0 for every self-energy insertion on a line that can be soft and for soft vertex/box subgraphs;"
      "\n   (M2) (phi^3_6, renormalizable): omega = 2 n_a > 0 for every soft subgraph with connected complement.")
