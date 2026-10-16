"""
e28_sw_geometric.py  -- stage-2 verifier (batch E26_s2), claim E28 (Sterman-Weinberg).

Independent evaluation of the O(alpha_s) Sterman-Weinberg (SW) two-jet cross section.

What is different from the two earlier computations
  (research/c_ee/sw_jets.py: algebraic region boundaries in (x3,v), analytic v-integral;
   stage-1 script: algebraic boundaries in (y13,y23), analytic inner integral):
  * the two-jet test is implemented DIRECTLY from the SW definition by explicit event geometry,
    with no derived algebraic boundary formulas:
        a set S of parton directions fits into a pair of opposite cones of half-angle delta
        <=> the LINES through the directions (angles mod pi, a circle of length pi) fit into an
            arc of length 2 delta  <=>  L(S) = pi - (largest circular gap) <= 2 delta.
        2-jet  <=>  L({1,2,3}) <= 2 delta   or   exists k: E_k <= eps*sqrt(s) and L({i,j}) <= 2 delta
    (all but a fraction eps of the TOTAL energy sqrt(s) inside the cones; at O(alpha_s) at most one
     parton can be outside since 2 partons outside would need E_in >= (1-eps) sqrt(s) > sqrt(s)/2);
  * region boundaries are located numerically (dense scan + bisection of the geometric classifier);
  * logistic variable t for the energy-sharing variable, outer integral by adaptive Gauss-Kronrod
    in log variables;
  * an explicit check that the geometric classifier agrees with the algebraic conditions
    (a) some theta_ij <= 2 delta, or (b) x_k <= 2 eps and pi - theta_ij <= 2 delta,
    used by the earlier computations (random sample);
  * the same machinery with eps defined as a fraction of the BEAM energy (x_k <= eps_b).

Kinematics: x_i = 2E_i/sqrt(s) (1 = q, 2 = qbar, 3 = g), a = y13 = 1-x2, b = y23 = 1-x1,
u = x3 = a+b, r = a/u = 1/(1+exp(-t)).  Exactly:
   f dx1 dx2 = (x1^2+x2^2)/((1-x1)(1-x2)) da db = (1/u) [ N0(u) dt - 2u^2 dr ] du,  N0 = 1+(1-u)^2.
c2j = (sigma_2j/sigma_0 - 1)/(C_F alpha_s/pi) = 3/4 - I3/2,  I3 = int_{3-jet} f dx1 dx2,
since sigma_tot = sigma_0 (1 + 3 C_F alpha_s/(4 pi)) and d sigma_real = sigma_0 (C_F alpha_s/2pi) f dx1 dx2.
Run: python3 -I e28_sw_geometric.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import math
import numpy as np
from scipy import integrate

PI = np.pi


def kin(xi, t):
    """xi = 1-u (passed separately for precision near u -> 1), t = logistic variable (array ok).
    Returns x1, x2, x3 and the three opening angles, from exactly rewritten, well-conditioned
    half-angle formulas (y_ij = x_i x_j sin^2(theta_ij/2), and x_i x_j - y_ij simplified using xi+u=1):
       sin^2(th13/2) = r/x1,        cos^2(th13/2) = xi (1-r)/x1
       sin^2(th23/2) = (1-r)/x2,    cos^2(th23/2) = xi r/x2
       sin^2(th12/2) = xi/(x1 x2),  cos^2(th12/2) = r (1-r) u^2/(x1 x2)."""
    u = 1.0 - xi
    r = 1.0 / (1.0 + np.exp(-t))
    omr = 1.0 / (1.0 + np.exp(t))            # 1 - r, computed without cancellation
    x1 = xi + r * u                           # = 1 - b
    x2 = xi + omr * u                         # = 1 - a
    x3 = u + 0.0 * t
    th13 = 2.0 * np.arctan2(np.sqrt(r / x1), np.sqrt(xi * omr / x1))
    th23 = 2.0 * np.arctan2(np.sqrt(omr / x2), np.sqrt(xi * r / x2))
    th12 = 2.0 * np.arctan2(np.sqrt(xi / (x1 * x2)), np.sqrt(r * omr * u * u / (x1 * x2)))
    return x1, x2, x3, th12, th13, th23


def L2(th):
    """distance of the two LINES through directions with opening angle th (circle of length pi)"""
    return np.minimum(th, PI - th)


def L3(th13, th23):
    """three momenta summing to zero surround the origin: put p1 at 0, p3 at th13, p2 at th13+th23
    (consecutive angles th13, th23, th12 = 2pi - th13 - th23). Lines = directions mod pi."""
    f1 = np.zeros_like(th13)
    f3 = np.mod(th13, PI)
    f2 = np.mod(th13 + th23, PI)
    A = np.sort(np.stack([f1, f2, f3], axis=-1), axis=-1)
    g1 = A[..., 1] - A[..., 0]
    g2 = A[..., 2] - A[..., 1]
    g3 = PI - (A[..., 2] - A[..., 0])
    return PI - np.maximum(np.maximum(g1, g2), g3)


def is_two_jet(xi, t, eps, delta, beam=False):
    """geometric SW classifier. eps = fraction of total energy (x_k <= 2 eps), or of the beam energy
    (x_k <= eps) if beam=True."""
    x1, x2, x3, th12, th13, th23 = kin(xi, t)
    xcut = eps if beam else 2.0 * eps
    tj = L3(th13, th23) <= 2.0 * delta
    tj |= (x1 <= xcut) & (L2(th23) <= 2.0 * delta)
    tj |= (x2 <= xcut) & (L2(th13) <= 2.0 * delta)
    tj |= (x3 <= xcut) & (L2(th12) <= 2.0 * delta)
    return tj


TGRID = np.unique(np.concatenate([np.linspace(-75.0, 75.0, 15001), [0.0]]))


def is_two_jet_scalar(xi, t, eps, delta, beam=False):
    """scalar (pure-python) version of is_two_jet, used in the bisection."""
    u = 1.0 - xi
    if t >= 0:
        e = math.exp(-t); r = 1.0 / (1.0 + e); omr = e / (1.0 + e)
    else:
        e = math.exp(t); r = e / (1.0 + e); omr = 1.0 / (1.0 + e)
    x1 = xi + r * u
    x2 = xi + omr * u
    x3 = u
    th13 = 2.0 * math.atan2(math.sqrt(r / x1), math.sqrt(xi * omr / x1))
    th23 = 2.0 * math.atan2(math.sqrt(omr / x2), math.sqrt(xi * r / x2))
    th12 = 2.0 * math.atan2(math.sqrt(xi / (x1 * x2)), math.sqrt(r * omr * u * u / (x1 * x2)))
    f = sorted([0.0, th13 % math.pi, (th13 + th23) % math.pi])
    l3 = math.pi - max(f[1] - f[0], f[2] - f[1], math.pi - (f[2] - f[0]))
    xcut = eps if beam else 2.0 * eps
    tw = 2.0 * delta
    if l3 <= tw:
        return True
    if x1 <= xcut and min(th23, math.pi - th23) <= tw:
        return True
    if x2 <= xcut and min(th13, math.pi - th13) <= tw:
        return True
    if x3 <= xcut and min(th12, math.pi - th12) <= tw:
        return True
    return False


def three_jet_intervals(xi, eps, delta, beam=False):
    two = is_two_jet(xi, TGRID, eps, delta, beam)
    if not two[0] or not two[-1]:
        raise RuntimeError('3-jet region reaches the scan edge')
    idx = np.nonzero(two[1:] != two[:-1])[0]
    edges = []
    for i in idx:
        lo, hi = float(TGRID[i]), float(TGRID[i + 1])
        vlo = bool(two[i])
        if is_two_jet_scalar(xi, lo, eps, delta, beam) != vlo:
            raise RuntimeError('scalar/vector classifier mismatch')
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if mid == lo or mid == hi:
                break
            if is_two_jet_scalar(xi, mid, eps, delta, beam) == vlo:
                lo = mid
            else:
                hi = mid
        edges.append(0.5 * (lo + hi))
    ivs = []
    state = True           # two[0] is True
    start = None
    for e in edges:
        if state:          # 2-jet -> 3-jet
            start = e
        else:              # 3-jet -> 2-jet
            ivs.append((start, e))
        state = not state
    if not state:
        raise RuntimeError('unterminated 3-jet interval')
    return ivs


def G(xi, eps, delta, beam=False):
    """u * (inner integral) = sum over 3-jet t-intervals of [N0 dt - 2u^2 dr]."""
    u = 1.0 - xi
    N0 = 1.0 + xi * xi
    tot = 0.0
    for (ta, tb) in three_jet_intervals(xi, eps, delta, beam):
        ra, rb = 1.0 / (1.0 + np.exp(-ta)), 1.0 / (1.0 + np.exp(-tb))
        tot += N0 * (tb - ta) - 2.0 * u * u * (rb - ra)
    return tot


def I3(eps, delta, beam=False, umin=None, verbose=False):
    ucut = eps if beam else 2.0 * eps
    if umin is None:
        umin = ucut
    # part 1: u in [umin, 1/2], variable w = ln u, F du = G dw
    f1 = lambda w: G(1.0 - np.exp(w), eps, delta, beam)
    pts1 = [np.log(ucut)] if umin < ucut else None
    A1, e1 = integrate.quad(f1, np.log(umin), np.log(0.5), points=pts1, limit=800,
                            epsabs=1e-11, epsrel=1e-13)
    # part 2: u in [1/2, 1), variable v = -ln(1-u), xi = e^{-v}, F du = G (1-u)/u dv ... (1-u) = xi
    def f2(v):
        xi = np.exp(-v)
        return G(xi, eps, delta, beam) * xi / (1.0 - xi)
    # candidate kinks: xi = ucut (soft q or qbar can be outside) and xi ~ sin^2(delta)/4 (q qbar cone)
    kinks = sorted(set([-np.log(ucut), -np.log(np.sin(delta) ** 2 / 4.0)]))
    vmax = 45.0
    A2, e2 = integrate.quad(f2, np.log(2.0), vmax, points=[k for k in kinks if np.log(2.0) < k < vmax],
                            limit=800, epsabs=1e-11, epsrel=1e-13)
    if verbose:
        print('    quad parts: %.12f (+-%.1e), %.12f (+-%.1e)' % (A1, e1, A2, e2))
    return A1 + A2


def formula(eps, delta, two=True):
    le = np.log(2 * eps) if two else np.log(eps)
    return -(4 * np.log(delta) * le + 3 * np.log(delta) + PI ** 2 / 3 - 2.5)


def check_classifier(eps, delta, n=200000, seed=1):
    """(i) consistency of the angle formulas (th12+th13+th23 = 2 pi, x1+x2+x3 = 2, momentum balance);
    (ii) compare the geometric classifier with the algebraic conditions (a)/(b) on random events."""
    rng = np.random.default_rng(seed)
    xi = np.where(rng.uniform(0, 1, n) < 0.5, rng.uniform(0, 1, n) ** 3, 1 - rng.uniform(0, 1, n) ** 3 * (1 - 1e-9))
    t = rng.normal(0, 6, n)
    x1, x2, x3, t12, t13, t23 = kin(xi, t)
    sumang = np.max(np.abs(t12 + t13 + t23 - 2 * PI))
    # momentum balance with p1 at 0, p3 at th13, p2 at th13+th23
    px = x1 + x3 * np.cos(t13) + x2 * np.cos(t13 + t23)
    py = x3 * np.sin(t13) + x2 * np.sin(t13 + t23)
    bal = np.max(np.hypot(px, py))
    geo = is_two_jet(xi, t, eps, delta)
    geo_s = np.array([is_two_jet_scalar(xi[i], t[i], eps, delta) for i in range(3000)])
    assert np.all(geo_s == geo[:3000]), 'scalar/vector classifier disagree'
    alg = (np.minimum(np.minimum(t12, t13), t23) <= 2 * delta)
    alg |= (x1 <= 2 * eps) & (PI - t23 <= 2 * delta)
    alg |= (x2 <= 2 * eps) & (PI - t13 <= 2 * delta)
    alg |= (x3 <= 2 * eps) & (PI - t12 <= 2 * delta)
    near = (np.abs(np.minimum(np.minimum(t12, t13), t23) - 2 * delta) < 1e-12)
    for tt in (t12, t13, t23):
        near |= np.abs(PI - tt - 2 * delta) < 1e-12
    mism = int(np.sum((geo != alg) & ~near))
    return n, int(np.sum(geo)), mism, float(sumang), float(bal)


if __name__ == '__main__':
    print('E28 stage-2 check: Sterman-Weinberg 2-jet cross section, geometric classifier\n')
    for (eps, delta) in [(0.05, 0.25), (1e-3, 0.03)]:
        n, n2, mism, sa, bal = check_classifier(eps, delta, n=200000)
        print('classifier check (eps,delta)=(%g,%g): %d random events, %d two-jet, mismatches with '
              'algebraic (a)/(b): %d ; max|sum of angles - 2pi| = %.1e, max|sum p| = %.1e'
              % (eps, delta, n, n2, mism, sa, bal))
    print()
    print('%-16s %16s %16s %16s %12s' % ('(eps, delta)', 'c2j numeric', 'ln(2eps) form', 'ln(eps) form', 'num-form'))
    rows = [(1e-2, 0.1), (1e-3, 0.03), (1e-4, 0.01), (1e-5, 0.005), (1e-6, 0.003)]
    res = {}
    for (eps, delta) in rows:
        I = I3(eps, delta, verbose=True)
        c = 0.75 - 0.5 * I
        res[(eps, delta)] = (I, c)
        print('%-16s %16.6f %16.6f %16.4f %12.2e' % (str((eps, delta)), c, formula(eps, delta, True),
                                                       formula(eps, delta, False), c - formula(eps, delta, True)))
    # stability of the main point: start the u-integral below 2 eps (classifier must give no 3-jet events)
    eps, delta = 1e-6, 0.003
    I_low = I3(eps, delta, umin=1e-3 * eps)
    print('\n(1e-6,0.003) with u-integration started at 1e-3*eps: c2j = %.6f' % (0.75 - 0.5 * I_low))
    print('I3(1e-6,0.003) = %.10f' % res[(eps, delta)][0])
    # beam-energy convention: E_k <= eps_b * sqrt(s)/2  (x_k <= eps_b)
    Ib = I3(1e-6, 0.003, beam=True)
    cb = 0.75 - 0.5 * Ib
    print('\nbeam-energy convention eps_b = 1e-6, delta = 0.003: c2j = %.6f ; ln(eps_b) form %.6f ; '
          'ln(2 eps_b) form %.6f' % (cb, formula(1e-6, 0.003, False), formula(1e-6, 0.003, True)))
    d = 4 * np.log(2) * abs(np.log(0.003))
    print('difference of the two forms at delta = 0.003: 4 ln2 |ln delta| = %.6f' % d)
