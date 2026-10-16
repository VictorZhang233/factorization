"""R-OUR1 (OUR-3, OUR-4) and R-OUR2 (OUR-5, OUR-6) auxiliary checks.

OUR-3: rest frame P=(M,0); Euclidean q = (i q4, qvec), q^2 = -Q^2:  omega = 2 P.q/Q^2 = 2 i M q4/Q^2 is purely imaginary;
       |omega| <= 2M/Q in general and <= sqrt(3) M/Q under the reference's restriction |qvec| >= Q/2 ((C.31)).
OUR-4: Glauber k = (lam^2, lam^2, lam): deforming only k^- by i kappa |k_T| leaves |k^+ k^-| ~ lam^3 << k_T^2 (still in G_delta);
       simultaneous deformation along e_G = nbar - n (Im k^+ = -kappa|kT|, Im k^- = +kappa|kT|) gives |k^+||k^-| >= kappa^2 kT^2
       and keeps Re k^2 <= -(1-2 delta-2 kappa^2) kT^2 < 0.
OUR-5: invariants of an unpolarized (spin-averaged) forward matrix element with P_T = n_T = 0 and b = (0^+, b^-, b_T)
       depend on b_T only through b_T^2  =>  no O(b_T) term in the small-b expansion of unpolarized TMDs.
OUR-6: a function analytic in the cut omega plane can be uniformly small on a real segment [-rho, rho] (and even on a disc)
       while its discontinuity on [1, 2] is O(1) pointwise.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
import mpmath as mp

# ---- OUR-3 ----
M, Q = 0.94, 10.0
rng = np.random.default_rng(3)
mx_all, mx_restr = 0.0, 0.0
for _ in range(200000):
    q4 = rng.uniform(-Q, Q)
    qv = np.sqrt(Q**2 - q4**2)
    om = 2*M*q4/Q**2           # omega/i
    mx_all = max(mx_all, abs(om))
    if qv >= Q/2: mx_restr = max(mx_restr, abs(om))
print(f"OUR-3: max|omega| (Euclidean q, rest frame) = {mx_all:.5f}  vs 2M/Q = {2*M/Q:.5f};  with |qvec|>=Q/2: {mx_restr:.5f} vs sqrt3 M/Q = {np.sqrt(3)*M/Q:.5f}")

# ---- OUR-4 ----
print()
for lam in [1e-1, 1e-2, 1e-3]:
    kp, km, kT = 0.7*lam**2, -0.4*lam**2, lam
    kappa, delta = 0.3, 0.1
    km1 = km + 1j*kappa*kT                     # one-component deformation
    kp2, km2 = kp - 1j*kappa*kT, km + 1j*kappa*kT
    one = abs(kp*km1)/kT**2
    two = abs(kp2)*abs(km2)/kT**2
    rek2 = (2*kp2*km2 - kT**2).real/kT**2
    print(f"OUR-4: lam={lam:.0e}: one-component |k+k-|/kT^2 = {one:.2e} (~lam); two-component |k+||k-|/kT^2 = {two:.3f} (>= kappa^2={kappa**2:.2f});"
          f" Re k^2/kT^2 = {rek2:.3f}")

# ---- OUR-5 ----
print()
Pp, Mm, bm, b1, b2 = sp.symbols('Pp M bm b1 b2', real=True)
def dot(u, v): return u[0]*v[1] + u[1]*v[0] - u[2]*v[2] - u[3]*v[3]
P = (Pp, Mm**2/(2*Pp), 0, 0)          # hadron along +z, P_T = 0
n = (0, 1, 0, 0)                       # Wilson-line direction (n_T = 0)
b = (0, bm, b1, b2)                    # b^+ = 0
inv = {'P.b': dot(P, b), 'n.b': dot(n, b), 'b.b': dot(b, b), 'P.n': dot(P, n), 'P.P': dot(P, P), 'n.n': dot(n, n)}
for k_, v in inv.items():
    print(f"OUR-5: {k_:4s} = {sp.simplify(v)}")
print("       every invariant depends on (b1,b2) only via b1^2+b2^2: odd powers of b_T need a transverse vector")
print("       (spin S_T, P_T or n_T), absent for the unpolarized f_1 => first power correction O(b_T^2) (up to logs).")

# ---- OUR-6 ----
print()
mp.mp.dps = 20
for K in [10, 100, 1000]:
    sigma = lambda w: mp.sin(K*(w - 1))
    r = lambda om: mp.quad(lambda w: sigma(w)/(w - om), mp.linspace(1, 2, 2*K+2))/mp.pi
    seg = max(abs(r(om)) for om in np.linspace(-0.8, 0.8, 9))
    disc = max(abs(sigma(w)) for w in np.linspace(1, 2, 201))
    print(f"OUR-6: K={K:5d}: max_|omega|<=0.8 |r(omega)| = {mp.nstr(seg, 4)};  max |Im r(omega+i0)| on [1,2] = {mp.nstr(disc, 3)}")
print("       => real-segment bounds do not control the discontinuity (the x-space structure function) pointwise.")
