"""E28 -- independent check of the Sterman-Weinberg O(alpha_s) two-jet cross section.

Written from scratch for the verifier (does not reuse research/c_ee/sw_jets.py).

Setup (massless partons, x_i = 2E_i/sqrt(s), x1+x2+x3 = 2, parton 3 = gluon):
  d sigma / (dx1 dx2) = sigma_0 (C_F alpha_s / 2 pi) (x1^2 + x2^2) / ((1-x1)(1-x2)),
  sigma_tot = sigma_0 (1 + (3/4) C_F alpha_s/pi).
Sterman-Weinberg definition: an event is two-jet if SOME pair of back-to-back cones of
half-angle delta contains all the energy except at most eps*sqrt(s) (eps = fraction of the
TOTAL energy). For three partons this is equivalent to
  (a) some opening angle theta_ij <= 2 delta, or
  (b) some x_k <= 2 eps and pi - theta_ij <= 2 delta for the other two partons.
With y_ij = (p_i+p_j)^2/s: x_k = 1 - y_ij and 1 - cos theta_ij = 2 y_ij/(x_i x_j).
Write a = y13 = 1-x2, b = y23 = 1-x1, d = sin^2 delta.  All conditions are linear or quadratic
in b at fixed a; the b-integral of the matrix element is done analytically between
breakpoints, and the a-integral numerically (composite Gauss-Legendre, geometric panels).

sigma_2j/sigma_0 = 1 + (C_F alpha_s/pi) * c2j,   c2j = 3/4 - I3j/2,
I3j = int_{3-jet} dx1 dx2 (x1^2+x2^2)/((1-x1)(1-x2)).
Claim E28: c2j = -[4 ln(delta) ln(2 eps) + 3 ln(delta) + pi^2/3 - 5/2] + power corrections.
"""
import sys, os, math
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np


def quad_roots(A, B, C):
    """real roots of A b^2 + B b + C = 0"""
    out = []
    if abs(A) < 1e-300:
        if abs(B) > 0:
            out.append(-C / B)
        return out
    disc = B * B - 4 * A * C
    if disc < 0:
        return out
    s = math.sqrt(disc)
    # numerically stable
    q = -0.5 * (B + math.copysign(s, B))
    if q != 0:
        out.append(q / A)
        out.append(C / q)
    else:
        out.append(-B / (2 * A))
    return out


def is_two_jet(a, b, eps, d):
    x1, x2 = 1 - b, 1 - a
    x3 = 2 - x1 - x2
    y12, y13, y23 = 1 - x3, a, b
    if y13 <= d * x1 * x3: return True
    if y23 <= d * x2 * x3: return True
    if y12 <= d * x1 * x2: return True
    if x3 <= 2 * eps and y12 >= (1 - d) * x1 * x2: return True
    if x1 <= 2 * eps and y23 >= (1 - d) * x2 * x3: return True
    if x2 <= 2 * eps and y13 >= (1 - d) * x1 * x3: return True
    return False


def prim(a, b):
    # antiderivative in b of ((1-b)^2 + (1-a)^2)/(a b)
    return ((1 + (1 - a) ** 2) * math.log(b) - 2 * b + 0.5 * b * b) / a


def inner(a, eps, d):
    """int over b in (0, 1-a) of the 3-jet part, analytically between breakpoints"""
    bmax = 1 - a
    pts = [0.0, bmax]
    # C13: -d b^2 + d(1-a) b + (d a - a) = 0
    pts += quad_roots(-d, d * (1 - a), d * a - a)
    # C23 (linear), C12 (linear)
    pts.append(d * a * (1 - a) / (1 - d * (1 - a)))
    pts.append((1 - a) * (1 - d) / (1 - d * (1 - a)))
    # S3: a+b = 2 eps ; b = d(1-a)/(d + (1-d) a)
    pts.append(2 * eps - a)
    pts.append(d * (1 - a) / (d + (1 - d) * a))
    # S1: b = 1-2eps ; b = (1-d)(1-a) a/(1-(1-d)(1-a))
    pts.append(1 - 2 * eps)
    pts.append((1 - d) * (1 - a) * a / (1 - (1 - d) * (1 - a)))
    # S2: a >= (1-d)(1-b)(a+b):  (1-d)[(1-b)(a+b)] - a = 0 -> -(1-d) b^2 + (1-d)(1-a) b + ((1-d) a - a) = 0
    pts += quad_roots(-(1 - d), (1 - d) * (1 - a), (1 - d) * a - a)
    pts = sorted(p for p in pts if 0.0 <= p <= bmax)
    tot = 0.0
    for lo, hi in zip(pts[:-1], pts[1:]):
        if hi - lo <= 0:
            continue
        mid = 0.5 * (lo + hi)
        if not is_two_jet(a, mid, eps, d):
            if lo <= 0:
                raise RuntimeError('3-jet region touches b=0')
            tot += prim(a, hi) - prim(a, lo)
    return tot


def I3j(eps, delta, npan=3000, ngl=16):
    d = math.sin(delta) ** 2
    # outer variable: a in (amin, 1). 3-jet region needs a > ~ d*x1*x3 >~ d*(2eps)... use a_min tiny.
    amin = 1e-14
    edges = np.geomspace(amin, 1.0, npan + 1)
    xg, wg = np.polynomial.legendre.leggauss(ngl)
    tot = 0.0
    for lo, hi in zip(edges[:-1], edges[1:]):
        # integrate in t = ln a for smoothness
        tlo, thi = math.log(lo), math.log(hi)
        for xi, wi in zip(xg, wg):
            t = 0.5 * (thi - tlo) * xi + 0.5 * (thi + tlo)
            a = math.exp(t)
            tot += 0.5 * (thi - tlo) * wi * a * inner(a, eps, d)
    return tot


def c2j_formula(eps, delta, two=True):
    L = math.log(2 * eps) if two else math.log(eps)
    return -(4 * math.log(delta) * L + 3 * math.log(delta) + math.pi ** 2 / 3 - 2.5)


if __name__ == '__main__':
    # sanity check of the region logic against brute-force Monte Carlo at a moderate point
    rng = np.random.default_rng(1)
    eps, delta = 0.05, 0.25
    d = math.sin(delta) ** 2
    # MC in (x1,x2) of M * 1_{3jet}
    N = 400000
    x1 = rng.random(N); x2 = rng.random(N)
    m = x1 + x2 >= 1
    x1, x2 = x1[m], x2[m]
    val = np.zeros_like(x1)
    for i in range(len(x1)):
        a, b = 1 - x2[i], 1 - x1[i]
        if a <= 0 or b <= 0: continue
        if not is_two_jet(a, b, eps, d):
            val[i] = (x1[i] ** 2 + x2[i] ** 2) / (a * b)
    mc = val.sum() / N  # area of unit square = 1
    mcerr = val.std() * math.sqrt(len(val)) / N
    an = I3j(eps, delta, npan=600)
    print('region/integration sanity (eps,delta)=(%.2f,%.2f): MC %.4f +- %.4f   semi-analytic %.6f' % (eps, delta, mc, mcerr, an))
    print()
    print('ROUGH fixed-grid pass (no panel edges at the jumps a = 2eps, 1-2eps: accurate only to ~1e-3; see the adaptive pass below)')
    print('%10s %8s %14s %14s %14s %12s' % ('eps', 'delta', 'c2j numeric', 'ln(2eps) form', 'ln(eps) form', 'resid(2eps)'))
    for eps, delta in [(1e-2, 0.1), (1e-3, 0.03), (1e-4, 0.01), (1e-5, 0.005), (1e-6, 0.003)]:
        vals = []
        for npan in (2000, 4000):
            vals.append(0.75 - 0.5 * I3j(eps, delta, npan=npan))
        c = vals[-1]
        f2 = c2j_formula(eps, delta, True)
        f1 = c2j_formula(eps, delta, False)
        print('%10.0e %8.3f %14.6f %14.6f %14.6f %12.2e   (conv: %.1e)' % (eps, delta, c, f2, f1, c - f2, abs(vals[1] - vals[0])))
    eps, delta = 1e-6, 0.003
    print()
    print('difference of the two forms at (1e-6,0.003): %.4f ; 4 ln2 |ln delta| = %.4f' % (
        c2j_formula(eps, delta, True) - c2j_formula(eps, delta, False), 4 * math.log(2) * abs(math.log(delta))))


# ---------------------------------------------------------------------------------------
# High-precision pass: adaptive QUADPACK (scipy.integrate.quad) in t = ln a on geometric
# panels, which resolves the kinks of the a-integrand (where breakpoints cross).
def I3j_adaptive(eps, delta, npan=200, tol=1e-13):
    from scipy.integrate import quad
    d = math.sin(delta) ** 2
    # The a-integrand JUMPS at a = 2 eps (condition S3 needs a + b <= 2 eps) and at a = 1 - 2 eps
    # (condition S2 switches on): these points must be panel edges (QUADPACK alone can miss
    # a jump inside a panel; this is what made the fixed-grid results above inaccurate).
    edges = sorted(set(list(np.geomspace(1e-14, 1.0, npan + 1)) + [2 * eps, 1 - 2 * eps]))
    tot, err = 0.0, 0.0
    f = lambda t: math.exp(t) * inner(math.exp(t), eps, d)
    for lo, hi in zip(edges[:-1], edges[1:]):
        v, e = quad(f, math.log(lo), math.log(hi), epsabs=tol, epsrel=tol, limit=500)
        tot += v; err += e
    return tot, err


if __name__ == '__main__':
    print()
    print('adaptive pass:')
    print('%10s %8s %16s %16s %12s %10s' % ('eps', 'delta', 'c2j numeric', 'ln(2eps) form', 'resid', 'quad err'))
    for eps, delta in [(1e-2, 0.1), (1e-3, 0.03), (1e-4, 0.01), (1e-5, 0.005), (1e-6, 0.003)]:
        I, e = I3j_adaptive(eps, delta)
        c = 0.75 - 0.5 * I
        f2 = c2j_formula(eps, delta, True)
        print('%10.0e %8.3f %16.7f %16.7f %12.3e %10.1e' % (eps, delta, c, f2, c - f2, 0.5 * e))
