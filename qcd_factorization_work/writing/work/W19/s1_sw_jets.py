r"""
W19 / Ch16 -- s1_sw_jets.py : Sterman--Weinberg two-jet cross section at O(alpha_s).

Independent re-derivation for prop:jets-sw and ex:jets-sw (book conventions):
  * two-jet criterion: there is a pair of back-to-back cones of half-angle delta (free axis) such that the
    energy outside both cones is < eps*sqrt(s), eps = fraction of the TOTAL c.m. energy (not of the beam energy).
  * O(alpha_s) matrix element (VF-EE-5, 4D):  (1/sigma0) dsigma/dx1 dx2 = (C_F as/2pi) (x1^2+x2^2)/((1-x1)(1-x2)).
  * sigma_tot = sigma0 (1 + 3 C_F as/(4 pi))  (VF-EE-6).

Checks
  G1  the exact geometric criterion (a)/(b) [pigeonhole + bisector argument] agrees with an exact brute-force
      criterion built from arcs of allowed in-plane axes, on 200000 random three-parton events;
  G2  ... and with a direct scan over in-plane cone axes (2*10^4 axis angles), except within a tolerance of
      the boundaries (grid resolution);
  G3  the reduction to in-plane axes: random 3D axes never beat the best in-plane axis;
  A1  sympy: int_0^1 (2-2x+x^2) ln(1-x)/x dx = 5/4 - pi^2/3 ;
  A2  sympy: assembled asymptotics I_3j = 4 ln d ln(2 eps) + 3 ln d + 2 pi^2/3 - 7/2, d = sin^2 delta,
      and sigma_2j/sigma0 = 1 - (C_F as/pi)[4 ln delta ln 2eps + 3 ln delta + pi^2/3 - 5/2] (+O(delta^2 ln eps));
  N1  independent numerical integration of I_3j (boundaries located by bisection on the geometric predicates,
      v-integral in closed form, x3-integral by composite Gauss--Legendre) vs the asymptotic formula;
  N2  same numbers vs the semi-analytic routine of research/c_ee/sw_jets.py (independent implementation);
  N3  two-jet coefficient c_2j = (sigma_2j/sigma0 - 1)/(C_F as/pi): ln(2 eps) form vs ln(eps) form;
  N4  eps' = 2 eps (fraction of the beam energy) turns the formula into 4 ln delta ln eps';
  N5  BNRS (Becher et al. 2016) normalization: with beta = 2 eps, sigma = sigma0[1 + (C_F as/4pi)(-16 ln delta
      ln beta - 12 ln delta + c0)], c0 = 10 - 4 pi^2/3;
  N6  eps >> delta: the formula fails.
Run:  python3 -I s1_sw_jets.py
"""
import sys, os, math
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
import mpmath as mp

RES = []
def check(name, cond, info=''):
    RES.append((name, bool(cond)))
    print(('PASS  ' if cond else 'FAIL  ') + name + (('   [' + info + ']') if info else ''))

rng = np.random.default_rng(20261014)

# ----------------------------------------------------------------------------------------------
# kinematics of a three-parton event, all in the event plane (x-y), Q = 2 so that E_i = x_i
# ----------------------------------------------------------------------------------------------
def event(x1, x2):
    x3 = 2.0 - x1 - x2
    # cos theta_ij = 1 - 2 y_ij/(x_i x_j), y_ij = 1 - x_k
    c12 = 1 - 2 * (1 - x3) / (x1 * x2)
    th12 = math.acos(max(-1.0, min(1.0, c12)))
    p1 = np.array([x1, 0.0])
    p2 = x2 * np.array([math.cos(th12), math.sin(th12)])
    p3 = -(p1 + p2)
    return np.array([p1, p2, p3]), np.array([x1, x2, x3])

def angle(u, v):
    c = np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))
    return math.acos(max(-1.0, min(1.0, c)))

def twojet_rule(P, X, eps, delta):
    """criterion (a)/(b) of the text"""
    th = {(i, j): angle(P[i], P[j]) for i in range(3) for j in range(3) if i < j}
    if any(t <= 2 * delta for t in th.values()):
        return True
    for k in range(3):
        i, j = [m for m in range(3) if m != k]
        if X[k] < 2 * eps and math.pi - th[(i, j)] <= 2 * delta:
            return True
    return False

def twojet_arcs(P, X, eps, delta):
    """exact brute force: cone pair <-> axis line; particle i inside the pair iff the line distance
    (angle mod pi) between axis and p_i is <= delta. Enumerate the sets allowed outside."""
    psi = np.array([math.atan2(p[1], p[0]) % math.pi for p in P])
    def linedist(a, b):
        d = abs(a - b) % math.pi
        return min(d, math.pi - d)
    def common_axis(idx):
        # exists phi with linedist(phi, psi_i) <= delta for all i in idx ?
        if len(idx) <= 1:
            return True
        # candidate phis: psi_i +- delta (endpoints of the arcs) -- intersection of arcs, if nonempty,
        # contains an endpoint of one of the arcs
        cands = [(psi[i] + s * delta) % math.pi for i in idx for s in (-1, 1)]
        return any(all(linedist(ph, psi[i]) <= delta + 1e-13 for i in idx) for ph in cands)
    for out in [(), (0,), (1,), (2,), (0, 1), (0, 2), (1, 2)]:
        # E_out = sum of x_i (units Q/2): the condition E_out <= eps*sqrt(s) reads sum x_i <= 2 eps
        Eout = sum(X[i] for i in out)
        if Eout > 2 * eps:
            continue
        inside = [i for i in range(3) if i not in out]
        if common_axis(inside):
            return True
    return False

def twojet_scan(P, X, eps, delta, nphi=20000):
    phis = np.linspace(0, math.pi, nphi, endpoint=False)
    psi = np.array([math.atan2(p[1], p[0]) for p in P])
    d = np.abs((phis[:, None] - psi[None, :]) % math.pi)
    d = np.minimum(d, math.pi - d)
    inside = d <= delta
    Eout = ((~inside) * X[None, :]).sum(axis=1)
    return bool((Eout <= 2 * eps).any())

def margin(P, X, eps, delta):
    """distance of the configuration from the boundaries of the criterion (for the scan tolerance)"""
    ths = [angle(P[i], P[j]) for i, j in ((0, 1), (0, 2), (1, 2))]
    m = min(min(abs(t - 2 * delta), abs(math.pi - t - 2 * delta)) for t in ths)
    m = min(m, min(abs(x - 2 * eps) for x in X))
    return m

print('== G: geometry of the two-jet criterion ==')
ok_rule = True; nmis_scan = 0; nmis_scan_far = 0
eps_d = [(0.01, 0.1), (0.05, 0.08), (0.002, 0.03), (0.1, 0.35)]
Ntot = 0
for (eps, delta) in eps_d:
    n = 50000
    x1 = rng.uniform(0, 1, n); x2 = rng.uniform(0, 1, n)
    m = (x1 + x2 > 1)
    x1, x2 = x1[m], x2[m]
    # oversample the singular corners (small x3, small 1-x1, 1-x2)
    for a, b in zip(x1, x2):
        P, X = event(a, b)
        r1 = twojet_rule(P, X, eps, delta); r2 = twojet_arcs(P, X, eps, delta)
        if r1 != r2:
            ok_rule = False
        Ntot += 1
    for a, b in zip(x1[:4000], x2[:4000]):
        P, X = event(a, b)
        r1 = twojet_rule(P, X, eps, delta); r3 = twojet_scan(P, X, eps, delta)
        if r1 != r3:
            nmis_scan += 1
            if margin(P, X, eps, delta) > 2e-3:
                nmis_scan_far += 1
# corner events (near the two-jet boundaries)
for (eps, delta) in eps_d:
    for _ in range(20000):
        x3 = 10 ** rng.uniform(-5, 0); v = rng.uniform(0, 1)
        x1 = 1 - x3 * (1 - v); x2 = 1 - x3 * v
        if x1 <= 0 or x2 <= 0:
            continue
        P, X = event(x1, x2)
        if twojet_rule(P, X, eps, delta) != twojet_arcs(P, X, eps, delta):
            ok_rule = False
        Ntot += 1
check('G1  rule (a)/(b) == exact arc criterion on %d random three-parton events' % Ntot, ok_rule)
check('G2  rule (a)/(b) == axis scan (mismatches only within 2e-3 of a boundary)', nmis_scan_far == 0,
      'mismatches %d, all near boundaries' % nmis_scan)

# G3: 3D axes never better than in-plane axes
def eout_axis3(n3, P3, X, delta):
    out = 0.0
    for p, x in zip(P3, X):
        c = abs(np.dot(n3, p)) / np.linalg.norm(p)
        if math.acos(min(1.0, c)) > delta:
            out += x
    return out
worse = 0
for _ in range(600):
    x1, x2 = rng.uniform(0.5, 1, 2)
    if x1 + x2 <= 1:
        continue
    P, X = event(x1, x2)
    P3 = [np.array([p[0], p[1], 0.0]) for p in P]
    delta = rng.uniform(0.05, 0.4)
    best_plane = min(eout_axis3(np.array([math.cos(f), math.sin(f), 0.0]), P3, X, delta)
                     for f in np.linspace(0, math.pi, 720, endpoint=False))
    for _k in range(20):
        n3 = rng.normal(size=3); n3 /= np.linalg.norm(n3)
        if eout_axis3(n3, P3, X, delta) < best_plane - 1e-12:
            # check projected axis
            npj = np.array([n3[0], n3[1], 0.0]); npj /= np.linalg.norm(npj)
            if eout_axis3(npj, P3, X, delta) > eout_axis3(n3, P3, X, delta) + 1e-12:
                worse += 1
check('G3  projecting a cone axis onto the event plane never increases the energy outside', worse == 0)

# ----------------------------------------------------------------------------------------------
# A: analytic asymptotics (sympy)
# ----------------------------------------------------------------------------------------------
print('== A: analytic asymptotics ==')
x, e, d = sp.symbols('x epsilon d', positive=True)
N0 = 1 + (1 - x) ** 2
# (2 - 2x + x^2)/x = 2/x + (x - 2): int_0^1 2 ln(1-x)/x = -2 Li2(1) = -pi^2/3 ; int_0^1 (x-2) ln(1-x) = 5/4
J1a = -2 * sp.polylog(2, 1)
J1b = sp.integrate((x - 2) * sp.log(1 - x), (x, 0, 1))
J1 = sp.simplify(J1a + J1b)
mp.mp.dps = 30
J1num = mp.quad(lambda s: (2 - 2 * s + s * s) * mp.log(1 - s) / s, [0, 1])
check('A1  int_0^1 (2-2x+x^2) ln(1-x)/x dx = 5/4 - pi^2/3', sp.simplify(J1 - (sp.Rational(5, 4) - sp.pi ** 2 / 3)) == 0
      and abs(J1num - (mp.mpf(5) / 4 - mp.pi ** 2 / 3)) < 1e-25, str(J1) + ' ; numeric ' + mp.nstr(J1num, 20))
# I_3j ~ int_{2eps}^1 dx/x [ 2 N0 ( -ln d - ln(1-x) ) - 2 x^2 ]   (a -> d(1-x) at d -> 0)
J2 = sp.integrate(sp.expand(N0) / x, (x, 2 * e, 1))
J2s = sp.series(J2, e, 0, 1).removeO()
I3 = -2 * sp.log(d) * J2s - 2 * J1 - 2 * sp.Rational(1, 2)
target = 4 * sp.log(d) * sp.log(2 * e) + 3 * sp.log(d) + 2 * sp.pi ** 2 / 3 - sp.Rational(7, 2)
check('A2a I_3j -> 4 ln d ln 2eps + 3 ln d + 2pi^2/3 - 7/2', sp.simplify(sp.expand_log(I3 - target, force=True)) == 0)
delta = sp.symbols('delta', positive=True)
c2 = sp.Rational(3, 4) - (target / 2).subs(d, delta ** 2)          # sigma_2j/sigma0 = 1 + (CF as/pi) c2
c2_target = -(4 * sp.log(delta) * sp.log(2 * e) + 3 * sp.log(delta) + sp.pi ** 2 / 3 - sp.Rational(5, 2))
delta_s = delta   # keep the sympy symbol (the name delta is reused for floats below)
check('A2b sigma_2j/sigma0 - 1 = -(C_F as/pi)[4 ln delta ln 2eps + 3 ln delta + pi^2/3 - 5/2]',
      sp.simplify(sp.expand_log(c2 - c2_target, force=True)) == 0)
# collinear boundary a = d(1-x3)/(1-d x3): exact ln((1-a)/a) - (-ln d - ln(1-x3)) = O(d)
a_ex = d * (1 - x) / (1 - d * x)
diff = sp.series(sp.log((1 - a_ex) / a_ex) + sp.log(d) + sp.log(1 - x), d, 0, 2).removeO()
ok_a3 = all(abs(float(diff.subs({x: xv, d: 0}))) < 1e-14 and
            abs(float(sp.diff(diff, d).subs({x: xv, d: 0})) + 1) < 1e-12 for xv in (0.1, 0.5, 0.9))
check('A3  ln((1-a)/a) = -ln d - ln(1-x3) - d + O(d^2) for 0 < x3 < 1', ok_a3)

# ----------------------------------------------------------------------------------------------
# N: independent numerical integration of the three-jet region
# ----------------------------------------------------------------------------------------------
print('== N: numerics ==')
def atoms(x3, v, eps, dd):
    """atomic predicates (arrays) of the two-jet criterion in (x3, v); dd = delta (angle). Q = 2."""
    x1 = 1 - x3 * (1 - v); x2 = 1 - x3 * v
    y12 = 1 - x3; y13 = x3 * v; y23 = x3 * (1 - v)
    c12 = 1 - 2 * y12 / (x1 * x2); c13 = 1 - 2 * y13 / (x1 * x3); c23 = 1 - 2 * y23 / (x2 * x3)
    cd2 = math.cos(2 * dd)
    # A_ij: theta_ij <= 2 delta ; B_ij: pi - theta_ij <= 2 delta ; E_k: x_k < 2 eps (E_k < eps sqrt(s))
    return {'A12': c12 >= cd2, 'A13': c13 >= cd2, 'A23': c23 >= cd2,
            'B12': c12 <= -cd2, 'B13': c13 <= -cd2, 'B23': c23 <= -cd2,
            'E1': x1 < 2 * eps, 'E2': x2 < 2 * eps, 'E3': np.full(np.shape(v), x3 < 2 * eps)}

def threejet_mask(x3, v, eps, dd):
    """vectorized exact three-jet predicate in (x3, v): complement of rule (a)/(b)"""
    A = atoms(x3, v, eps, dd)
    two = A['A12'] | A['A13'] | A['A23'] | (A['E3'] & A['B12']) | (A['E1'] & A['B23']) | (A['E2'] & A['B13'])
    return ~two

def active_atoms(x3, u_b, eps, dd, h=1e-7):
    """which atomic predicates flip across the boundary at u = u_b (kink bookkeeping)"""
    vl = 1.0 / (1.0 + math.exp(-(u_b - h))); vr = 1.0 / (1.0 + math.exp(-(u_b + h)))
    Al = atoms(x3, np.array([vl]), eps, dd); Ar = atoms(x3, np.array([vr]), eps, dd)
    return tuple(sorted(k for k in Al if bool(Al[k][0]) != bool(Ar[k][0])))

def v_intervals(x3, eps, delta, ngrid=6000):
    # grid in u = logit(v), refine every sign change by bisection on the predicate itself
    u = np.concatenate([np.linspace(-60, -8, 800), np.linspace(-8, 8, ngrid), np.linspace(8, 60, 800)])
    v = 1.0 / (1.0 + np.exp(-u))
    m = threejet_mask(x3, v, eps, delta)
    edges = []
    def bis(ua, ub, ma):
        for _ in range(80):
            um = 0.5 * (ua + ub)
            vm = 1.0 / (1.0 + math.exp(-um))
            mm = bool(threejet_mask(x3, np.array([vm]), eps, delta)[0])
            if mm == ma:
                ua = um
            else:
                ub = um
        return 0.5 * (ua + ub)
    ivs = []
    start = u[0] if m[0] else None
    for k in range(1, len(u)):
        if m[k] != m[k - 1]:
            ub = bis(u[k - 1], u[k], bool(m[k - 1]))
            if m[k]:
                start = ub
            else:
                ivs.append((start, ub)); start = None
    if start is not None:
        ivs.append((start, u[-1]))
    return ivs

def v_integral(x3, ivs):
    N0 = 1 + (1 - x3) ** 2
    tot = 0.0
    for (ua, ub) in ivs:
        va = 1 / (1 + math.exp(-ua)); vb = 1 / (1 + math.exp(-ub))
        tot += N0 * (ub - ua) - 2 * x3 ** 2 * (vb - va)     # int N0 dv/(v(1-v)) = N0 * du
    return tot

def _structure(x3, eps, delta):
    """signature of the interval structure at fixed x3: for every interval end, the atomic predicates that
    define it (a change of the defining predicate is a kink of the x3-integrand even if the number of
    intervals does not change)"""
    ivs = v_intervals(x3, eps, delta, ngrid=2500)
    sig = []
    for (ua, ub) in ivs:
        for uu in (ua, ub):
            if abs(uu) < 59.9:
                sig.append(active_atoms(x3, uu, eps, delta))
            else:
                sig.append(('end',))
    return tuple(sig)

def _integrate_piece(xfun, jac, zlo, zhi, eps, delta, nsub, ng, ngrid_bp):
    """integrate F(x3(z)) * jac(z) dz over [zlo, zhi], F = v-integral; breakpoints of the interval
    structure detected on a grid in z and refined by bisection"""
    zg = np.linspace(zlo, zhi, ngrid_bp)
    sig = [_structure(xfun(z), eps, delta) for z in zg]
    bps = [zlo]
    for k in range(1, len(zg)):
        if sig[k] != sig[k - 1]:
            a, b = zg[k - 1], zg[k]
            sa = sig[k - 1]
            for _ in range(48):
                m = 0.5 * (a + b)
                if _structure(xfun(m), eps, delta) == sa:
                    a = m
                else:
                    b = m
            bps.append(0.5 * (a + b))
    bps.append(zhi)
    bps = sorted(set(bps))
    gx, gw = np.polynomial.legendre.leggauss(ng)
    tot = 0.0
    for lo, hi in zip(bps[:-1], bps[1:]):
        if hi - lo < 1e-15:
            continue
        edges = np.linspace(lo, hi, nsub + 1)
        for a, b in zip(edges[:-1], edges[1:]):
            for xg, wg in zip(gx, gw):
                z = 0.5 * (b - a) * xg + 0.5 * (a + b)
                x3 = xfun(z)
                tot += 0.5 * (b - a) * wg * jac(z, x3) * v_integral(x3, v_intervals(x3, eps, delta))
    return tot

def I3jet_num(eps, delta, nsub=8, ng=20):
    """I_3j = int M dx1 dx2 over the three-jet region, with M dx1 dx2 = [N0/(v(1-v)) - 2 x3^2] dv dx3/x3.
    lower half x3 in (x3min, 1/2]: z = ln x3 (dx3/x3 = dz); upper half x3 in (1/2, 1): z = -ln(1-x3)
    (dx3/x3 = (1-x3)/x3 dz)."""
    x3min = min(2 * eps, 1e-3) * 1e-3
    lower = _integrate_piece(lambda z: math.exp(z), lambda z, x3: 1.0,
                             math.log(x3min), math.log(0.5), eps, delta, nsub, ng, 700)
    upper = _integrate_piece(lambda z: 1 - math.exp(-z), lambda z, x3: (1 - x3) / x3,
                             math.log(2.0), 13 * math.log(10.0), eps, delta, nsub, ng, 900)
    return lower + upper

def asym(eps, delta):
    dd = math.sin(delta) ** 2
    return 4 * math.log(dd) * math.log(2 * eps) + 3 * math.log(dd) + 2 * math.pi ** 2 / 3 - 3.5

# reference: research/c_ee/sw_jets.py semi-analytic routine (imported without running its checks)
ref = {}
try:
    import importlib.util
    cee = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'research', 'c_ee', 'sw_jets.py')
    src = open(cee).read().split("print('   eps      delta")[0]
    ns = {}
    exec(compile(src, 'c_ee_sw_jets_defs', 'exec'), ns)
    ref_fun = ns['I3jet']
except Exception as exc:
    ref_fun = None
    print('   (c_ee reference not available: %s)' % exc)

pts = [(1e-2, 0.1), (1e-3, 0.03), (1e-4, 0.01), (1e-5, 0.01), (1e-6, 0.003)]
rows = []
print('   eps      delta    I3j(our numerics)   I3j(c_ee)        asymptotic     num-asym')
for (eps, delta) in pts:
    num = I3jet_num(eps, delta)
    r = float(ref_fun(mp.mpf(eps), mp.mpf(delta))) if ref_fun else float('nan')
    an = asym(eps, delta)
    rows.append((eps, delta, num, r, an))
    print('  %7.0e  %6.3f  %16.8f  %16.8f  %14.8f  %10.2e' % (eps, delta, num, r, an, num - an))
check('N1  numerics -> asymptotic formula (|diff| <= 30(eps|ln d| + d|ln eps|) at every point)',
      all(abs(n - a) <= 30 * (e_ * abs(math.log(math.sin(dl) ** 2)) + math.sin(dl) ** 2 * abs(math.log(e_)))
          for e_, dl, n, r, a in rows))
if ref_fun:
    check('N2  our integration == c_ee semi-analytic routine (rel. 1e-7)',
          all(abs(n - r) <= 1e-7 * abs(r) for e_, dl, n, r, a in rows))

print('   two-jet coefficient c_2j = (sigma_2j/sigma0 - 1)/(C_F as/pi):')
tab = []
for (eps, delta, num, r, an) in rows:
    c2n = 0.75 - num / 2
    sw = -(4 * math.log(delta) * math.log(2 * eps) + 3 * math.log(delta) + math.pi ** 2 / 3 - 2.5)
    swb = -(4 * math.log(delta) * math.log(eps) + 3 * math.log(delta) + math.pi ** 2 / 3 - 2.5)
    tab.append((eps, delta, c2n, sw, swb))
    print('    eps=%7.0e delta=%6.3f  c2j(num)=%12.4f  [ln 2eps]=%12.4f  [ln eps]=%12.4f' % (eps, delta, c2n, sw, swb))
e6 = tab[-1]
check('N3  (1e-6,0.003): c2j(num) = %.4f agrees with the ln(2eps) form %.4f, not with ln(eps) %.2f'
      % (e6[2], e6[3], e6[4]), abs(e6[2] - e6[3]) < 1e-3 and abs(e6[2] - e6[4]) > 10)
# N4 beam-energy fraction
epsb = 2e-6
numb = I3jet_num(epsb / 2, 0.003)
c2b = 0.75 - numb / 2
swb2 = -(4 * math.log(0.003) * math.log(epsb) + 3 * math.log(0.003) + math.pi ** 2 / 3 - 2.5)
check("N4  eps' = 2e-6 of the beam energy (=1e-6 of sqrt(s)): formula with ln eps' holds", abs(c2b - swb2) < 1e-3,
      '%.4f vs %.4f' % (c2b, swb2))
# N5 BNRS normalization
b = sp.symbols('beta', positive=True)
bnrs = (-16 * sp.log(delta_s) * sp.log(b) - 12 * sp.log(delta_s) + 10 - 4 * sp.pi ** 2 / 3) / 4   # in units CF as/pi
check('N5  BNRS form with beta = 2 eps, c0 = 10 - 4pi^2/3, equals our formula',
      sp.simplify(sp.expand_log(bnrs.subs(b, 2 * e) - c2_target, force=True)) == 0)
# N6 eps >> delta
num6 = I3jet_num(0.05, 0.005)
check('N6  eps=0.05 >> delta=0.005: |I3j - asymptotic| > 1 (formula not applicable)', abs(num6 - asym(0.05, 0.005)) > 1,
      '%.4f vs %.4f' % (num6, asym(0.05, 0.005)))

print()
print('SUMMARY: %d/%d checks passed' % (sum(p for _, p in RES), len(RES)))
