"""W13 / s8: (A) LO collinear SIDIS (thm:coll-sidis, text); (B) final-state pole structure and the simultaneous
deformation (lem:coll-final-poles, prop:coll-sia-regions).
(A) Breit-frame kinematics: z = P.p_h/P.q equals the light-cone fraction of the struck quark carried by h at LO;
    d sigma/(dx dQ^2 dz) = (2 pi alpha^2/(x Q^4)) [1+(1-y)^2] sum_q e_q^2 x [q(x) d_{h/q}(z) + qbar(x) d_{h/qbar}(z)];
    momentum sum rule: sum_h int dz z (...) = LO DIS cross section (2 pi alpha^2/(x Q^4)) [1+(1-y)^2] F2.
(B) tree-level final-state jet with V_H -> l1 -> v1 (emits final p2) -> l2 -> v2 (soft k injected, exits as p1):
    covariant denominators l^2 + i0 have their k^- zeros in Im k^- > 0 (standard flow l2 = p1 - k, l1 = p1+p2-k);
    LCOPT denominators D_i = A_i - k^- + i eps; deformation k^- -> k^- - i kappa never crosses a zero.
    Simultaneous deformation for a soft line between jets along w_1, w_2: k -> k + i t (w_1 - w_2):
    w_1.Im k = -t w1.w2 < 0, w_2.Im k = t w1.w2 > 0; for k in the Glauber region and t <= |k_T|/2 the soft
    propagator k^2 stays at Re k^2 < 0 and the deformed momentum leaves G_delta (|k^+ k^-| >= t^2 >= delta k_T^2).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np

npass = 0; nfail = 0
def check(name, ok):
    global npass, nfail
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)
    if ok: npass += 1
    else: nfail += 1

# (A) Breit frame (light-cone): P = (P+, 0, 0), q = (-x P+, Q^2/(2 x P+), 0)
Pp, x, Q, z = sp.symbols('P_plus x Q z', positive=True)
def lcdot(a, b): return a[0]*b[1] + a[1]*b[0] - a[2]*b[2]
P = (Pp, 0, 0); q = (-x*Pp, Q**2/(2*x*Pp), 0)
check('(A) q^2 = -Q^2, x = Q^2/(2P.q)', sp.simplify(lcdot(q, q) + Q**2) == 0 and sp.simplify(Q**2/(2*lcdot(P, q)) - x) == 0)
kq = (x*Pp, 0, 0)                     # struck quark xi P with xi = x at LO
pout = tuple(sp.simplify(kq[i] + q[i]) for i in range(3))
check('(A) outgoing quark p\' = k + q is on shell and moves along -z: p\'^+ = 0', sp.simplify(pout[0]) == 0 and sp.simplify(lcdot(pout, pout)) == 0)
ph = tuple(z*c for c in pout)         # collinear fragmentation p_h = z p'
check('(A) z = P.p_h / P.q for p_h = z p\'', sp.simplify(lcdot(P, ph)/lcdot(P, q) - z) == 0)
# LO cross section and momentum sum rule
alpha, y = sp.symbols('alpha y', positive=True)
qx, qbx = sp.symbols('q qbar'); d1, d2 = sp.Function('d_q')(z), sp.Function('d_qbar')(z)
sig_sidis = 2*sp.pi*alpha**2/(x*Q**4)*(1 + (1 - y)**2)*x*(qx*d1 + qbx*d2)
# momentum sum rule sum_h int z d = 1 for each parton:
sig_sum = sig_sidis.subs({d1: 1, d2: 1}).subs(z, 1)  # replace int z d by 1
sig_dis = 2*sp.pi*alpha**2/(x*Q**4)*(1 + (1 - y)**2)*x*(qx + qbx)
check('(A) sum_h int dz z dsigma^h = LO DIS cross section (per flavour, e_q^2 stripped)', sp.simplify(sig_sum - sig_dis) == 0)

# (B) pole structure, numerically
rng = np.random.default_rng(7)
def E_on(lp, lT2, m2=0.0, eta=0.0):
    return (lT2 + m2 - 1j*eta)/(2*lp)
ok_cov = True; ok_lc = True
for trial in range(50):
    p1p, p2p = rng.uniform(0.3, 1.0, 2); p1T = rng.normal(0, 0.2, 2); p2T = rng.normal(0, 0.2, 2)
    kp = rng.uniform(-0.01, 0.01); kT = rng.normal(0, 0.05, 2)
    E1 = (p1T @ p1T)/(2*p1p); E2 = (p2T @ p2T)/(2*p2p)      # on-shell final energies (massless)
    # covariant: l2 = p1 - k, l1 = p1 + p2 - k ; l^2 = 2 l+ l- - lT^2, l- = p1- - k- etc.
    l2p = p1p - kp; l1p = p1p + p2p - kp
    l2T = p1T - kT; l1T = p1T + p2T - kT
    # zero of l2^2 + i0 in k^-: 2 l2+ (E1 - k^-) - l2T^2 + i0 = 0 -> k^- = E1 - l2T^2/(2 l2+) + i0/(2 l2+)
    eta = 1e-6
    kz2 = E1 - (l2T @ l2T)/(2*l2p) + 1j*eta/(2*l2p)
    kz1 = E1 + E2 - (l1T @ l1T)/(2*l1p) + 1j*eta/(2*l1p)
    ok_cov &= (kz1.imag > 0 and kz2.imag > 0)
    # LCOPT: D1 = (E1 + E2 - k^-) - E(l1), D2 = (E1 - k^-) - E(l2) with E(l) = (lT^2 - i eta)/(2 l+)
    D1 = lambda km: E1 + E2 - km - E_on(l1p, l1T @ l1T, eta=eta)
    D2 = lambda km: E1 - km - E_on(l2p, l2T @ l2T, eta=eta)
    for kap in (0.0, 0.01, 0.1, 1.0):
        for kre in np.linspace(-1, 1, 21):
            km = kre - 1j*kap
            ok_lc &= (D1(km).imag > 0 and D2(km).imag > 0)
check('(B) covariant propagators of the all-final-state jet: k^- zeros in Im k^- > 0 (50 random configurations)', ok_cov)
check('(B) LCOPT denominators: Im D > 0 on the deformed contours k^- -> k^- - i kappa', ok_lc)
# simultaneous deformation: w1 = n_A, w2 = n_B : k -> k + i t (n_A - n_B), i.e. k^+ += i t, k^- -= i t
kp_, km_, kT_, t = sp.symbols('k_p k_m k_T t', real=True)
kpd = kp_ + sp.I*t; kmd = km_ - sp.I*t
k2 = sp.expand(2*kpd*kmd - kT_**2)
check('(B) k^2 -> 2k+k- + 2t^2 - k_T^2 + 2 i t (k- - k+)', sp.simplify(k2 - (2*kp_*km_ + 2*t**2 - kT_**2 + 2*sp.I*t*(km_ - kp_))) == 0)
ok = True
for trial in range(200):
    kT = rng.uniform(0.01, 1.0); kpv, kmv = rng.uniform(-1, 1, 2)*0.05*kT**2   # deep Glauber: |k+ k-| << kT^2
    for tv in np.linspace(0, kT/2, 11):
        re = 2*kpv*kmv + 2*tv**2 - kT**2
        ok &= re < 0
        if tv == kT/2:
            ok &= abs((kpv + 1j*tv)*(kmv - 1j*tv)) >= tv**2 - 1e-15 and tv**2 >= kT**2/8 - 1e-15
check('(B) for t <= k_T/2 the soft propagator keeps Re k^2 < 0 (no crossing) and at t = k_T/2 |k+ k-| >= k_T^2/4 > k_T^2/8',
      ok)
nA = sp.Matrix([1, 0]); nB = sp.Matrix([0, 1])   # (plus, minus) components
def lcd(a, b): return a[0]*b[1] + a[1]*b[0]
check('(B) w1.Im k = -t w1.w2 < 0 and w2.Im k = t w1.w2 > 0 for Im k = t(w1 - w2), (w1,w2) = (n_A,n_B)',
      lcd(nA, t*(nA - nB)) == -t*lcd(nA, nB) and lcd(nB, t*(nA - nB)) == t*lcd(nA, nB))
print('\nSUMMARY s8: %d PASS, %d FAIL' % (npass, nfail))
