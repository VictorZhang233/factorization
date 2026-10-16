#!/usr/bin/env python3
"""
power_counting.py -- numerical checks of IR power counting (research/c_regions)

Conventions: light-cone v^pm=(v^0 pm v^3)/sqrt2, v.w = v^+w^- + v^-w^+ - v_T.w_T; region scalings are written
(k^+, k^-, k_T) ~ (lambda^a, lambda^b, lambda^c) Q   ("SCET lambda"; Sterman's lambda_S = lambda^2).
A region's contribution scales as lambda^p, p = (a+b+2c) + sum_j(-A_j) + (numerator powers); p=0: logarithmic.

P1  massless on-shell vertex (lines k^2,(p1-k)^2,(p2+k)^2): hard, coll-1 (0,2,1), coll-2 (2,0,1), soft (1,1,1),
    ultrasoft (2,2,2), Glauber (2,2,1) all give p=0; contrasting scalings (0,1,1)->1, (2,2,3)->2
P2  off-shell vertex (task convention: k^2,(k+p1)^2,(k+p2)^2, p_i^2=-P^2=-lambda^2 Q^2):
      collinear family (0,2c,c): p = 0 (c<=1), 2c-2 (c>=1);  soft family (c,c,c): p = 0 (c<=2), 2c-4 (c>=2)
P3  eikonal approximation  (p1-k)^2 ~ -2 p1.k : relative error ~ lambda (soft), lambda^2 (ultrasoft), O(1) (Glauber)
P4  real emission gamma*->q qbar g: (i) explicit Dirac traces reproduce |M|^2 ~ (x1^2+x2^2)/((1-x1)(1-x2));
    (ii) quark-emission squared numerator ~ lambda^2 in the collinear limit (numerator suppression), so
    |M|^2 ~ lambda^-2 and with phase space lambda^2 -> lambda^0
P5  Feynman-gauge vertex numerator in the collinear-1 region: J^+H^- ~ lambda^0, J_T.H_T ~ lambda^1, J^-H^+ ~ lambda^2;
    J.H = (J^+/k^+)(k.H) + O(lambda)  (scalar / K-gluon dominance -> Ward identity -> Wilson line)
P6  Glauber region: vertex k^- integral has a single pole (not trapped, CSS 1989 eq.138); a k^- integral with an
    incoming and an outgoing collinear line is trapped at |k^-|~k_T^2/p^+, where the eikonal approximation fails
P7  omega(R) from the boost/dimension formula (Feynman gauge), table of examples; comparison with Sterman's
    direct count n_T (TASI'95 eqs. 63-66) for soft-exchange examples
Run:  python3 -I power_counting.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import mpmath as mp
from fractions import Fraction as Fr

PASS = []
def check(name, cond):
    PASS.append((name, bool(cond))); print(('PASS ' if cond else 'FAIL ') + name)

rng = np.random.default_rng(2024)
mp.mp.dps = 40
SQ2 = mp.sqrt(2)

def lcdot(a, b):  # a=(plus, minus, T1, T2)
    return a[0]*b[1] + a[1]*b[0] - a[2]*b[2] - a[3]*b[3]

def fit_exponent(fun, lams):
    vals = [mp.log(abs(fun(l))) for l in lams]
    A = np.vstack([[float(mp.log(l)) for l in lams], np.ones(len(lams))]).T
    sl, _ = np.linalg.lstsq(A, np.array([float(v) for v in vals]), rcond=None)[0]
    return sl

LAMS = [mp.mpf(10)**(-e) for e in (4, 5, 6, 7, 8)]

# ------------------------------------------------------------------------------- P1 on-shell massless vertex
print('=== P1: massless on-shell vertex, exponent p of (measure x integrand) ===')
p1 = (1/SQ2, mp.mpf(0), mp.mpf(0), mp.mpf(0))     # along +  (Q^2 = 2 p1^+ p2^- = 1)
p2 = (mp.mpf(0), 1/SQ2, mp.mpf(0), mp.mpf(0))     # along -
def integrand_onshell(k):
    D0 = lcdot(k, k)
    pm = tuple(p1[i]-k[i] for i in range(4)); D1 = lcdot(pm, pm)
    pp = tuple(p2[i]+k[i] for i in range(4)); D2 = lcdot(pp, pp)
    return 1/(D0*D1*D2)
regions = {'hard (0,0,0)': (0, 0, 0, 0), 'coll-1 (0,2,1)': (0, 2, 1, 0), 'coll-2 (2,0,1)': (2, 0, 1, 0),
           'soft (1,1,1)': (1, 1, 1, 0), 'ultrasoft (2,2,2)': (2, 2, 2, 0), 'Glauber (2,2,1)': (2, 2, 1, 0),
           'non-leading (0,1,1)': (0, 1, 1, 1), 'non-leading (2,2,3)': (2, 2, 3, 2)}
okP1 = True
for name, (a, b, c, pred) in regions.items():
    sls = []
    for trial in range(4):
        kh = [mp.mpf(float(v)) for v in rng.uniform(0.2, 0.9, 4)] if a == 0 else [mp.mpf(float(v)) for v in rng.uniform(0.2, 0.9, 4)]
        sgn = [1, -1 if trial % 2 else 1, 1, 1]
        def fun(l, kh=kh, sgn=sgn):
            k = (sgn[0]*kh[0]*l**a, sgn[1]*kh[1]*l**b, kh[2]*l**c, kh[3]*l**c)
            meas = l**(a + b + 2*c)
            return meas*integrand_onshell(k)
        sls.append(fit_exponent(fun, LAMS))
    sl = np.mean(sls)
    print(f'   {name:24s} fitted p = {sl:+.4f}   predicted {pred}')
    okP1 &= abs(sl - pred) < 2e-3
check('P1 on-shell vertex: all leading regions log (p=0), contrasting scalings suppressed as predicted', okP1)

# ------------------------------------------------------------------------------- P1b massless box
print('=== P1b: massless scalar box (lines k, k+p1, k+p1+p2, k-p4), soft corners and collinear edges ===')
th = mp.mpf('0.9'); E = mp.mpf('0.5')
def cartv(t0, x, y, z): return (t0, x, y, z)
def mdot4(a, b): return a[0]*b[0] - a[1]*b[1] - a[2]*b[2] - a[3]*b[3]
P1c = cartv(E, 0, 0, E); P2c = cartv(E, 0, 0, -E)                       # incoming along +z, -z
P3c = cartv(-E, -E*mp.sin(th), 0, -E*mp.cos(th)); P4c = cartv(-E, E*mp.sin(th), 0, E*mp.cos(th))   # all-incoming convention
def addv(*vs): return tuple(sum(v[i] for v in vs) for i in range(4))
def scal(c, v): return tuple(c*x for x in v)
def box_integrand(k):
    q0 = k; q1 = addv(k, P1c); q2 = addv(k, P1c, P2c); q3 = addv(k, scal(-1, P4c))
    return 1/(mdot4(q0, q0)*mdot4(q1, q1)*mdot4(q2, q2)*mdot4(q3, q3))
def lc_to_cart(kp, km, k1, k2): return (( kp + km)/SQ2, k1, k2, (kp - km)/SQ2)
okB = True
# soft corner: line 0 soft, k ~ lambda^2 (all components); measure lambda^8
for trial in range(3):
    kh = [mp.mpf(float(v)) for v in rng.uniform(-0.9, 0.9, 4)]
    sl = fit_exponent(lambda l: l**8*box_integrand(tuple(l**2*x for x in kh)), LAMS)
    okB &= abs(sl) < 2e-3
print(f'   soft corner (line 0 at zero momentum): fitted p = {sl:+.4f} (predicted 0)')
# collinear edge (0,1): k = -x p1 + (k^- ~ lambda^2, k_T ~ lambda) in the light-cone frame of p1 (p1 along +z)
for trial in range(3):
    xx = mp.mpf(float(rng.uniform(0.15, 0.85))); kap = mp.mpf(float(rng.uniform(-1, 1))); t1, t2 = [mp.mpf(float(v)) for v in rng.uniform(-1, 1, 2)]
    p1p = SQ2*E
    sl = fit_exponent(lambda l: l**4*box_integrand(lc_to_cart(-xx*p1p, l**2*kap, l*t1, l*t2)), LAMS)
    okB &= abs(sl) < 2e-3
print(f'   collinear edge (lines 0,1 || p1): fitted p = {sl:+.4f} (predicted 0)')
# s-channel cut surface (lines 0 and 2 on shell, not pinched): generic scaling of a 'thin shell' is not logarithmic
check('P1b massless box: soft corners and collinear edges are logarithmic (p = 0)', okB)

# ------------------------------------------------------------------------------- P2 off-shell vertex scans
print('=== P2: off-shell vertex (P^2 = lambda^2 Q^2), scans of collinear and soft scalings ===')
def integrand_offshell(k, lam):
    P2 = lam**2
    q1 = (1/SQ2, -P2/(2*(1/SQ2)), mp.mpf(0), mp.mpf(0))   # p1^2 = -P^2, along +
    q2 = (-P2/(2*(1/SQ2)), 1/SQ2, mp.mpf(0), mp.mpf(0))   # p2^2 = -P^2, along -
    D0 = lcdot(k, k)
    a1 = tuple(k[i]+q1[i] for i in range(4)); D1 = lcdot(a1, a1)
    a2 = tuple(k[i]+q2[i] for i in range(4)); D2 = lcdot(a2, a2)
    return 1/(D0*D1*D2)
okP2 = True
for fam in ('coll', 'soft'):
    for cexp in (mp.mpf('0.5'), mp.mpf(1), mp.mpf('1.5'), mp.mpf(2), mp.mpf(3)):
        if fam == 'coll':
            a, b, c = 0, 2*cexp, cexp; pred = 0 if cexp <= 1 else float(2*cexp - 2)
        else:
            a, b, c = cexp, cexp, cexp; pred = 0 if cexp <= 2 else float(2*cexp - 4)
        sls = []
        for trial in range(4):
            kh = [mp.mpf(float(v)) for v in rng.uniform(0.2, 0.9, 4)]
            def fun(l, kh=kh):
                k = (kh[0]*l**a, kh[1]*l**b, kh[2]*l**c, kh[3]*l**c)
                return l**(a + b + 2*c)*integrand_offshell(k, l)
            sls.append(fit_exponent(fun, [mp.mpf(10)**(-e) for e in (6, 7, 8, 9, 10)]))
        sl = np.mean(sls)
        print(f'   {fam:4s} c={float(cexp):3.1f}: fitted p = {sl:+.4f}   predicted {pred:+.1f}')
        okP2 &= abs(sl - pred) < 5e-3
check('P2 off-shell vertex: collinear logs for k_T between P and Q, soft logs for k between P^2/Q and Q', okP2)

# ------------------------------------------------------------------------------- P3 eikonal approximation
print('=== P3: relative error of the eikonal approximation (p1-k)^2 -> -2 p1.k ===')
def eik_err(k):
    pm = tuple(p1[i]-k[i] for i in range(4))
    exact = lcdot(pm, pm); eik = -2*lcdot(p1, k)
    return abs(exact/eik - 1)
okP3 = True
for name, (a, b, c, pred) in {'soft (1,1,1)': (1, 1, 1, 1), 'ultrasoft (2,2,2)': (2, 2, 2, 2), 'Glauber (2,2,1)': (2, 2, 1, 0)}.items():
    kh = [mp.mpf(float(v)) for v in rng.uniform(0.2, 0.9, 4)]
    sl = fit_exponent(lambda l: eik_err((kh[0]*l**a, kh[1]*l**b, kh[2]*l**c, kh[3]*l**c)), LAMS)
    ex = eik_err((kh[0]*LAMS[-1]**a, kh[1]*LAMS[-1]**b, kh[2]*LAMS[-1]**c, kh[3]*LAMS[-1]**c))
    print(f'   {name:18s} rel.error ~ lambda^{sl:.3f} (predicted {pred}); value at lambda=1e-8: {mp.nstr(ex, 4)}')
    okP3 &= abs(sl - pred) < 1e-2
check('P3 eikonal approximation valid in soft/ultrasoft regions, fails (O(1) error) in the Glauber region', okP3)

# ------------------------------------------------------------------------------- Dirac algebra (numpy, complex)
I2 = np.eye(2); Z2 = np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
g0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
gi = [np.block([[Z2, s_], [-s_, Z2]]) for s_ in (sx, sy, sz)]
GAM = [g0] + gi                                   # gamma^mu, upper index, Dirac rep.
METRIC = np.diag([1., -1., -1., -1.])
def slash(p):  # p: contravariant Cartesian 4-vector (t,x,y,z)
    return sum(METRIC[m, m]*p[m]*GAM[m] for m in range(4))
def mink(a, b): return a[0]*b[0] - a[1]*b[1] - a[2]*b[2] - a[3]*b[3]
def cart(plus, minus, t1, t2):
    return np.array([(plus+minus)/np.sqrt(2), t1, t2, (plus-minus)/np.sqrt(2)])

# ------------------------------------------------------------------------------- P4 real emission
print('=== P4: gamma* -> q(p1) qbar(p2) g(k): traces and numerator suppression ===')
def msq_real(P1, P2, K):
    """sum over spins/pols (-g for gluon and photon) of |M|^2 / (e^2 g^2 C_F N_c ...) up to a constant:
       M = ubar(p1)[ g^nu (p1+k)slash g^mu /(p1+k)^2 - g^mu (p2+k)slash g^nu /(p2+k)^2 ] v(p2)  (relative sign from
       the antiquark-line propagator S(-(p2+k)))"""
    S1 = slash(P1 + K)/mink(P1 + K, P1 + K); S2 = slash(P2 + K)/mink(P2 + K, P2 + K)
    tot = 0
    for mu in range(4):
        for nu in range(4):
            A = GAM[nu] @ S1 @ GAM[mu] - GAM[mu] @ S2 @ GAM[nu]
            Abar = GAM[mu] @ S1 @ GAM[nu] - GAM[nu] @ S2 @ GAM[mu]   # gamma^0 A^dagger gamma^0 for real momenta
            tot += METRIC[mu, mu]*METRIC[nu, nu]*np.trace(slash(P1) @ A @ slash(P2) @ Abar)
    return tot.real
def three_body(x1, x2, phi=0.3):
    """massless 3-body final state in the q rest frame, sqrt(s)=1: energies x_i/2."""
    E1, E2 = x1/2, x2/2; E3 = 1 - E1 - E2
    # cos(theta_12) from (p1+p2)^2 = s(1-x3) = 2 E1 E2 (1-cos12)
    x3 = 2 - x1 - x2
    cos12 = 1 - (1 - x3)/(2*E1*E2)
    sin12 = np.sqrt(max(0., 1 - cos12**2))
    P1 = E1*np.array([1, 0, 0, 1.])
    P2 = E2*np.array([1, sin12*np.cos(phi), sin12*np.sin(phi), cos12])
    K = np.array([1., 0, 0, 0]) - P1 - P2
    return P1, P2, K
ratios = []
for x1, x2 in ((0.6, 0.7), (0.9, 0.5), (0.75, 0.95), (0.55, 0.62)):
    P1, P2, K = three_body(x1, x2)
    assert abs(mink(K, K)) < 1e-12
    ratios.append(msq_real(P1, P2, K)/((x1**2 + x2**2)/((1 - x1)*(1 - x2))))
print('   |M|^2 / [(x1^2+x2^2)/((1-x1)(1-x2))] =', np.round(ratios, 10))
print('   (constant = %.10f for sqrt(s)=1, photon and gluon polarisation sums -g, couplings/colour stripped)' % ratios[0])
check('P4(i) trace reproduces the known x-dependence (x-independent ratio)', np.allclose(ratios, ratios[0], rtol=1e-10))
# collinear limit k || p1 at fixed z: numerator of the quark-emission squared term
def num_quark_emission(P1, P2, K):
    S = slash(P1 + K); tot = 0
    for mu in range(4):
        for nu in range(4):
            tot += METRIC[mu, mu]*METRIC[nu, nu]*np.trace(slash(P1) @ GAM[nu] @ S @ GAM[mu] @ slash(P2) @ GAM[mu] @ S @ GAM[nu])
    return tot.real
z = 0.35; vals_num, vals_den, vals_full = [], [], []
lam_list = [1e-2, 1e-3, 1e-4, 1e-5]
for lam in lam_list:
    kT = lam; kp = z; km = kT**2/(2*kp)              # massless gluon, collinear to p1 along +
    P1 = cart(1.0, 0., 0., 0.); P2 = cart(0., 1.0, 0., 0.); K = cart(kp, km, kT, 0.)
    vals_num.append(abs(num_quark_emission(P1, P2, K))); vals_den.append(mink(P1 + K, P1 + K)**2)
    vals_full.append(abs(msq_real(P1, P2, K)))
sl_num = np.polyfit(np.log(lam_list), np.log(vals_num), 1)[0]
sl_den = np.polyfit(np.log(lam_list), np.log(vals_den), 1)[0]
sl_full = np.polyfit(np.log(lam_list), np.log(vals_full), 1)[0]
print(f'   quark-emission^2 numerator ~ lambda^{sl_num:.4f}; denominator ((p1+k)^2)^2 ~ lambda^{sl_den:.4f}; full |M|^2 ~ lambda^{sl_full:.4f}')
check('P4(ii) numerator suppression: numerator ~ lambda^2, |M|^2 ~ lambda^-2 (log after lambda^2 phase space)',
      abs(sl_num - 2) < 1e-3 and abs(sl_den - 4) < 1e-6 and abs(sl_full + 2) < 1e-3)

# ------------------------------------------------------------------------------- P5 vertex numerator, collinear-1
print('=== P5: Feynman-gauge vertex numerator in the collinear-1 region ===')
def null_spinor(P):
    # p-slash is nilpotent for light-like p: take its null space from the SVD (rank 2)
    u_, sv, vh = np.linalg.svd(slash(P))
    assert sv[2] < 1e-12 and sv[1] > 1e-6
    return vh[2:].conj().T
P1 = cart(1.0, 0., 0., 0.); P2 = cart(0., 1.0, 0., 0.)
U1 = null_spinor(P1); V2 = null_spinor(P2)
# choose the spinor combination with non-zero tree current ubar(p1) gamma^1 v(p2)
best = None
for i in range(2):
    for j in range(2):
        ub = U1[:, i].conj() @ g0
        tree = ub @ GAM[1] @ V2[:, j]
        if best is None or abs(tree) > abs(best[2]):
            best = (ub, V2[:, j], tree)
ubar1, v2, tree = best
mu_ext = 1                                   # photon index mu = x (transverse)
def pieces(K):
    """J^nu = ubar(p1) gamma^nu (p1-k)slash ;  H^nu = gamma^mu (-(p2+k))slash gamma^nu v(p2) (upper indices)."""
    J = np.array([ubar1 @ GAM[n] @ slash(P1 - K) for n in range(4)])           # 4 x 4(spinor row)
    H = np.array([GAM[mu_ext] @ slash(-(P2 + K)) @ GAM[n] @ v2 for n in range(4)])  # 4 x 4(spinor col)
    Jn = np.array([J[n] @ H[m] for n in range(4) for m in range(4)]).reshape(4, 4)  # Jn[n,m] = J^n H^m (scalar)
    def comp(T, i):  # light-cone components of upper-index vectors
        return {'+': (T[0] + T[3])/np.sqrt(2), '-': (T[0] - T[3])/np.sqrt(2), 'T1': T[1], 'T2': T[2]}[i]
    # J^+ H^- etc. built from the bilinear matrix Jn[n,m] = J^n H^m
    def bil(i, j):
        A = np.zeros(4); B = np.zeros(4)
        base = {'+': np.array([1, 0, 0, 1])/np.sqrt(2), '-': np.array([1, 0, 0, -1])/np.sqrt(2),
                'T1': np.array([0, 1, 0, 0.]), 'T2': np.array([0, 0, 1, 0.])}
        return base[i] @ Jn @ base[j]
    JpHm = bil('+', '-'); JmHp = bil('-', '+'); JTHT = -(bil('T1', 'T1') + bil('T2', 'T2'))
    full = sum(METRIC[n, n]*Jn[n, n] for n in range(4))
    kH = np.array([sum(METRIC[m, m]*K[m]*H[m][s_] for m in range(4)) for s_ in range(4)])   # k_nu H^nu (spinor col)
    Jplus = (J[0] + J[3])/np.sqrt(2)
    kplus = (K[0] + K[3])/np.sqrt(2)
    Kgluon = (Jplus @ kH)/kplus
    return JpHm, JmHp, JTHT, full, Kgluon
x_ = 0.37; kap = -0.8; tau = (0.6, -0.45)
lams = np.array([1e-2, 1e-3, 1e-4, 1e-5])
rows = np.array([pieces(cart(x_*1.0, lam**2*kap, lam*tau[0], lam*tau[1])) for lam in lams])
check('P5 light-cone decomposition J.H = J^+H^- + J^-H^+ - J_T.H_T', np.allclose(rows[:, 3], rows[:, 0] + rows[:, 1] + rows[:, 2], rtol=1e-9, atol=1e-14))
def expo(col):
    a = abs(col)
    if np.all(a < 1e-14*np.max(abs(rows[:, 3]))):
        return np.inf                                  # identically zero (to machine precision)
    return np.polyfit(np.log(lams), np.log(a), 1)[0]
sl = [expo(rows[:, i]) for i in range(3)]
rel = abs(rows[:, 3] - rows[:, 4])/abs(rows[:, 3])
sl_rel = np.polyfit(np.log(lams), np.log(rel), 1)[0]
print(f'   exact light-like axis: J^+H^- ~ lambda^{sl[0]:.3f},  J^-H^+ ~ lambda^{sl[1]},  J_T.H_T ~ lambda^{sl[2]}  (inf = identically 0)')
print(f'   |J.H - (J^+/k^+)(k.H)|/|J.H| ~ lambda^{sl_rel:.3f}   (values {np.array2string(rel, precision=2)})')
print('   note: J^- = ubar(p1) gamma^- (...) = 0 exactly; J_T.H_T = 0 in D=4 because sum_{i=1,2} g^i g^j g^i = 0 (O(eps) in D dims)')
check('P5 collinear region (axis along +): J^+H^- ~ lambda^0 and the other pieces are suppressed by >= the predicted powers',
      abs(sl[0]) < 1e-2 and sl[1] >= 2 - 1e-2 and sl[2] >= 1 - 1e-2 and sl_rel >= 1 - 2e-2)
# variant: jet axis tilted by theta ~ lambda (p1 and k rotated about the y axis) -> generic scalings appear
def roty(v, th):
    c, s_ = np.cos(th), np.sin(th)
    return np.array([v[0], c*v[1] + s_*v[3], v[2], -s_*v[1] + c*v[3]])
rows2, comps = [], []
P1_save = P1.copy()
for lam in lams:
    th = 0.7*lam
    P1r = roty(P1_save, th); Kr = roty(cart(x_*1.0, lam**2*kap, lam*tau[0], lam*tau[1]), th)
    U1r = null_spinor(P1r)
    best2 = None
    for i in range(2):
        ub = U1r[:, i].conj() @ g0; tr = ub @ GAM[mu_ext] @ v2
        if best2 is None or abs(tr) > abs(best2[1]):
            best2 = (ub, tr)
    ub_r = best2[0]
    J = np.array([ub_r @ GAM[n] @ slash(P1r - Kr) for n in range(4)])      # jet tensor J^nu (row spinors)
    H = np.array([GAM[mu_ext] @ slash(-(P2 + Kr)) @ GAM[n] @ v2 for n in range(4)])
    Jp = (J[0] + J[3])/np.sqrt(2); Jm = (J[0] - J[3])/np.sqrt(2)
    comps.append((np.linalg.norm(Jp), np.linalg.norm(np.r_[J[1], J[2]]), np.linalg.norm(Jm)))
    Jn = np.array([[J[n] @ H[m] for m in range(4)] for n in range(4)])
    base = {'+': np.array([1, 0, 0, 1])/np.sqrt(2), '-': np.array([1, 0, 0, -1])/np.sqrt(2),
            'T1': np.array([0, 1, 0, 0.]), 'T2': np.array([0, 0, 1, 0.])}
    b_ = lambda a, b: base[a] @ Jn @ base[b]
    rows2.append((b_('+', '-'), b_('-', '+'), -(b_('T1', 'T1') + b_('T2', 'T2'))))
comps = np.array(comps); rows2 = np.array(rows2)
slc = [np.polyfit(np.log(lams), np.log(comps[:, i]), 1)[0] for i in range(3)]
print(f'   tilted axis (theta=0.7 lambda), jet tensor components: |J^+| ~ lambda^{slc[0]:.3f}, |J_T| ~ lambda^{slc[1]:.3f}, |J^-| ~ lambda^{slc[2]:.3f}')
check('P5 boost argument: jet-tensor components scale as lambda^0 (+), lambda^1 (T), lambda^2 (-)',
      abs(slc[0]) < 2e-2 and abs(slc[1] - 1) < 2e-2 and abs(slc[2] - 2) < 2e-2)
def expo2(col):
    a_ = abs(col)
    if np.all(a_ < 1e-14*np.max(abs(rows2[:, 0]))):
        return np.inf
    return np.polyfit(np.log(lams), np.log(a_), 1)[0]
sl2 = [expo2(rows2[:, i]) for i in range(3)]
print(f'   tilted axis, contractions with H: J^+H^- ~ lambda^{sl2[0]:.3f}, J^-H^+ ~ lambda^{sl2[1]}, J_T.H_T ~ lambda^{sl2[2]:.3f}')
print('   (H^+ = gamma^mu(...)gamma^+ v(p2) = 0 because p2 is exactly along -, and the O(lambda) part of J_T.H_T')
print('    cancels by the D=4 identity: the contractions are MORE suppressed than the bound -- consistent)')
check('P5 tilted axis: contractions obey the bounds (J^-H^+ >= lambda^2, J_T.H_T >= lambda^1)',
      abs(sl2[0]) < 5e-2 and sl2[1] >= 2 - 5e-2 and sl2[2] >= 1 - 5e-2)

# ------------------------------------------------------------------------------- P6 Glauber trapping
print('=== P6: Glauber region -- trapped vs untrapped k^- contours ===')
# (a) vertex: in the Glauber region D1 ~ -2 p1^+ k^- - kT^2 depends on k^-, D0 ~ -kT^2 and D2 ~ 2 k^+ p2^- - kT^2 do not:
#     a single pole in k^- -> contour can be moved to |k^-| ~ kT (soft region) where the eikonal approximation holds.
# (b) toy with an incoming and an outgoing A-collinear line carrying k: poles on opposite sides at |k^-| ~ kT^2/p^+
pA, pAp = mp.mpf(1), mp.mpf('0.7')
def toy_exact(kT):
    eps = kT**2*mp.mpf('1e-9')
    f = lambda km: 1/((-2*pA*km - kT**2 + 1j*eps)*(2*pAp*km - kT**2 + 1j*eps))
    zU = (-kT**2)/(2*pA); zL = kT**2/(2*pAp)
    nodes = sorted([-mp.inf, mp.inf, 0] + [z0 + d for z0 in (zU, zL) for d in (-10*eps, 0, 10*eps)])
    return mp.quad(f, nodes, maxdegree=10)
def toy_residue(kT):   # close in the UHP: pole of the first factor at km = (-kT^2 + i eps)/(2 pA)
    km = -kT**2/(2*pA)
    return 2j*mp.pi/((-2*pA)*(2*pAp*km - kT**2))
okP6 = True
for kT in (mp.mpf('0.1'), mp.mpf('0.01')):
    ex = toy_exact(kT); rs = toy_residue(kT)
    print(f'   toy, kT={float(kT)}: numeric {mp.nstr(ex, 12)}  residue {mp.nstr(rs, 12)}  kT^2*value = {mp.nstr(kT**2*rs, 8)}')
    okP6 &= abs(ex - rs) < 1e-6*abs(rs)
check('P6 trapped Glauber k^- integral is finite ~ 1/k_T^2, dominated by |k^-| ~ k_T^2/p^+', okP6)
# eikonal version: 1/((-2 pA km + i0)(2 pAp km + i0)) has both poles at km=0 from opposite sides -> pinch at km=0
eps_list = [mp.mpf(10)**(-e) for e in (3, 4, 5, 6)]
eikvals = []
for e_ in eps_list:
    f = lambda km: 1/((-2*pA*km + 1j*e_)*(2*pAp*km + 1j*e_))
    eikvals.append(abs(mp.quad(f, [-mp.inf, -10*e_, 0, 10*e_, mp.inf])))
sl_eik = np.polyfit([float(mp.log(e)) for e in eps_list], [float(mp.log(v)) for v in eikvals], 1)[0]
print(f'   eikonal (k_T^2 dropped) version grows as eps^{sl_eik:.3f} when i0 -> 0 (pinch at k^- = 0)')
check('P6 in the trapped Glauber region the eikonal approximation is singular (~1/eps): it cannot be used there',
      abs(sl_eik + 1) < 1e-2)

# ------------------------------------------------------------------------------- P7 omega(R) table
print('=== P7: omega(R) (Sterman units, lambda_S = lambda^2) from the boost/dimension formula, Feynman gauge ===')
def omega(jets, b_SH=0, f_SH=0):
    """jets: list of dicts with keys fg (good quark lines to H), fb (bad-component quark lines), bp (scalar-
    polarized gluons, J^+ component), bT (transverse gluons), bm (minus gluons), e (1 amplitude / 2 cut or forward),
    sb, sf (soft gluon / soft quark attachments to the jet)."""
    w = Fr(0)
    for J in jets:
        w += Fr(J.get('fg', 0) + J.get('bT', 0) + 2*J.get('bm', 0) + 2*J.get('fb', 0) - J['e'], 2)
        w += Fr(J.get('sf', 0), 2)
    return w + b_SH + Fr(3, 2)*f_SH
examples = [
    ('1-loop vertex, soft gluon between jets', [dict(fg=1, e=1, sb=1), dict(fg=1, e=1, sb=1)], 0, 0, 0),
    ('1-loop vertex, coll-1, scalar-pol. gluon into H', [dict(fg=1, bp=1, e=1), dict(fg=1, e=1)], 0, 0, 0),
    ('same, transverse gluon into H (twist-3 like)', [dict(fg=1, bT=1, e=1), dict(fg=1, e=1)], 0, 0, Fr(1, 2)),
    ('same, minus-polarized gluon into H', [dict(fg=1, bm=1, e=1), dict(fg=1, e=1)], 0, 0, 1),
    ('jet with 3 quark lines into H (twist-4 like)', [dict(fg=3, e=1), dict(fg=1, e=1)], 0, 0, 1),
    ('soft quark exchanged between the two jets', [dict(fg=1, e=1, sf=1), dict(fg=1, e=1, sf=1)], 0, 0, 1),
    ('soft gluon from a jet into H', [dict(fg=1, e=1, sb=1), dict(fg=1, e=1)], 1, 0, 1),
    ('soft quark from a jet into H', [dict(fg=1, e=1, sf=1), dict(fg=1, e=1)], 0, 1, 2),
    ('e+e- cut, 2 quark jets (Born-like)', [dict(fg=2, e=2), dict(fg=2, e=2)], 0, 0, 0),
    ('e+e- cut, quark jets + n scalar gluons + soft gluons', [dict(fg=2, bp=5, e=2, sb=3), dict(fg=2, bp=2, e=2, sb=3)], 0, 0, 0),
    ('e+e- cut, gluon jet with 2 transverse gluons', [dict(bT=2, e=2), dict(fg=2, e=2), dict(fg=2, e=2)], 0, 0, 0),
    ('gluon jet: 1 transverse + scalar only (super-leading)', [dict(bT=1, bp=1, e=2)], 0, 0, Fr(-1, 2)),
    ('DIS target jet: 1 quark each side + scalar gluons', [dict(fg=2, bp=3, e=2)], 0, 0, 0),
    ('DY: two incoming jets + soft gluons between them', [dict(fg=2, bp=1, e=2, sb=2), dict(fg=2, e=2, sb=2)], 0, 0, 0),
    ('DY: soft gluon into H', [dict(fg=2, e=2, sb=1), dict(fg=2, e=2)], 1, 0, 1),
]
okP7 = True
for name, jets, bSH, fSH, expected in examples:
    w = omega(jets, bSH, fSH)
    print(f'   {name:52s} omega = {str(w):5s} (lambda^{2*w} in SCET units)  expected {expected}')
    okP7 &= (w == expected)
check('P7 omega(R) table reproduces the standard leading/suppressed classification', okP7)
# Sterman TASI'95 eq.(64): n_T = M_J + M_J' + 2L_J + 2L_J' - N_J - N_J' + s'_T,  s'_T >= (V3J+V3J'-MJ-MJ')/2.
# (eq.(63) with 4(L_S+M_J+M_J'-1) assumes a connected soft subgraph; (64) follows for any number of components
#  because 4 L_S - 2 N_S + s_S = dim(S) = sum_a (4 - 3 M_a) and the number of soft loops linking S to the jets is M - c_S.)
def nT_sterman64(MJ, MJp, LJ, LJp, NJ, NJp, V3J, V3Jp):
    return MJ + MJp + 2*LJ + 2*LJp - NJ - NJp + Fr(V3J + V3Jp - MJ - MJp, 2)
n1 = nT_sterman64(MJ=1, MJp=1, LJ=0, LJp=0, NJ=1, NJp=1, V3J=1, V3Jp=1)        # one soft gluon (any soft self-energies)
n2 = nT_sterman64(MJ=2, MJp=2, LJ=0, LJp=0, NJ=2, NJp=2, V3J=2, V3Jp=2)        # two-gluon ladder or crossed ladder
n3 = nT_sterman64(MJ=3, MJp=1, LJ=0, LJp=0, NJ=3, NJp=1, V3J=3, V3Jp=1)        # three soft gluons from J merging (3g vertex) into one on J'
print(f"   Sterman eq.(64) lower bounds: 1 soft gluon n_T>={n1}; 2-gluon ladder n_T>={n2}; 3g->1g soft web n_T>={n3}")
check("P7 Sterman's direct count (TASI'95 eq.64) gives n_T >= 0 with equality for soft-gluon webs, = omega", n1 == 0 and n2 == 0 and n3 == 0)

print('\nSUMMARY: %d/%d checks passed' % (sum(p for _, p in PASS), len(PASS)))
