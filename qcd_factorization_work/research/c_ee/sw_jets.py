"""
sw_jets.py -- Sterman-Weinberg two-jet cross section at O(alpha_s), exact numerics vs asymptotic formula.

Definition (Sterman & Weinberg 1977): an event is "2-jet" if there exists a pair of oppositely directed
cones of half-angle delta containing all of the energy except at most a fraction eps of the TOTAL
c.m. energy sqrt(s).  (Axis free.)  At O(alpha_s) (partons q, qbar, g with x_i = 2E_i/sqrt(s)):
   2-jet  <=>  (a) some pair (i,j) has opening angle theta_ij <= 2 delta     [all in the cones], or
               (b) some parton k has x_k < 2 eps and the other two satisfy pi - theta_ij <= 2 delta.
(Proof of (a): -p_k = p_i + p_j lies on the arc between n_i and n_j, so the minimal cone containing
 n_i, n_j, -n_k has half-angle theta_ij/2.)

sigma_2jet = sigma_tot - sigma_3jet,  sigma_tot = sigma_0 (1 + 3 C_F alpha_s/(4 pi)),
sigma_3jet = sigma_0 (C_F alpha_s/2pi) Int_{3-jet} dx1 dx2 (x1^2 + x2^2)/((1-x1)(1-x2))   (finite, D = 4).
Variables: x3 and v with y13 = 1-x2 = x3 v, y23 = 1-x1 = x3 (1-v); Jacobian x3, and
   M dx1 dx2 = [N0(x3)/(v(1-v)) - 2 x3^2] dx3 dv / x3,  N0 = 1 + (1-x3)^2  (exact identity).
All region boundaries in v at fixed x3 are closed-form (DERIVATION.md section 5), the v-integral is
done analytically, the x3-integral numerically (mpmath, high precision).

Analytic result derived in DERIVATION.md (eps < delta << 1, d = sin^2 delta):
   Int_{3-jet} M = 4 ln d ln(2eps) + 3 ln d + 2 pi^2/3 - 7/2 + O(eps ln d, d ...)
=> sigma_2jet = sigma_0 { 1 - (C_F alpha_s/pi)[ 4 ln delta ln(2 eps) + 3 ln delta + pi^2/3 - 5/2 ] }.
Run:  python3 -I sw_jets.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp

mp.mp.dps = 30
PASS = []


def check(name, cond):
    PASS.append((name, bool(cond)))
    print(('PASS  ' if cond else 'FAIL  ') + name)


def intervals_3jet(x3, eps, d):
    """list of v-intervals (in (0,1)) belonging to the 3-jet region at fixed x3"""
    # (i),(ii): theta_13 > 2delta  <=>  v > a ;  theta_23 > 2delta <=> 1 - v > a
    a = d * (1 - x3) / (1 - x3 * d)
    allowed = [(a, 1 - a)] if a < 0.5 else []

    def remove(ivs, lo, hi):
        out = []
        for (p, q) in ivs:
            if hi <= p or lo >= q:
                out.append((p, q))
                continue
            if lo > p:
                out.append((p, lo))
            if hi < q:
                out.append((hi, q))
        return out
    # (iii) theta_12 <= 2delta  <=>  (1 - x3) <= d x1 x2 ,  x1 x2 = (1-x3) + x3^2 v(1-v)
    #        <=> x3^2 v(1-v) >= (1-x3)(1-d)/d
    c12 = (1 - x3) * (1 - d) / (d * x3 ** 2)
    if c12 <= 0.25:
        rt = mp.sqrt(1 - 4 * c12)
        allowed = remove(allowed, (1 - rt) / 2, (1 + rt) / 2)
    # (iv) b3: x3 < 2 eps and pi - theta_12 <= 2 delta <=> x3^2 v(1-v) <= d (1-x3)/(1-d)
    if x3 < 2 * eps:
        c3 = d * (1 - x3) / ((1 - d) * x3 ** 2)
        if c3 >= 0.25:
            allowed = []
        else:
            rt = mp.sqrt(1 - 4 * c3)
            allowed = remove(allowed, 0, (1 - rt) / 2)
            allowed = remove(allowed, (1 + rt) / 2, 1)
    # (v) b1: x1 < 2 eps <=> v < 1 - (1-2eps)/x3 ; antiquark-gluon back-to-back <=> v <= d/(1-(1-d) x3)
    vb = min(1 - (1 - 2 * eps) / x3, d / (1 - (1 - d) * x3))
    if vb > 0:
        allowed = remove(allowed, 0, vb)
    # (vi) b2: mirror image v -> 1-v
    if vb > 0:
        allowed = remove(allowed, 1 - vb, 1)
    return allowed


def v_integral(x3, ivs):
    N0 = 1 + (1 - x3) ** 2
    tot = mp.mpf(0)
    for (p, q) in ivs:
        if q <= p:
            continue
        tot += N0 * (mp.log(q / (1 - q)) - mp.log(p / (1 - p))) - 2 * x3 ** 2 * (q - p)
    return tot


def I3jet(eps, delta):
    d = mp.sin(delta) ** 2
    # breakpoints in x3 where the interval structure changes
    bps = {mp.mpf(0), mp.mpf(1), 2 * eps, 1 - 2 * eps}
    # where c12 = 1/4: (1-x3)(1-d) = d x3^2/4  -> root near 1
    f12 = lambda x: (1 - x) * (1 - d) - d * x ** 2 / 4
    bps.add(mp.findroot(f12, 1 - d / 4))
    # where c3 = 1/4 (only relevant below 2 eps)
    f3 = lambda x: d * (1 - x) - (1 - d) * x ** 2 / 4
    r3 = mp.findroot(f3, 2 * mp.sqrt(d))
    if 0 < r3 < 1:
        bps.add(r3)
    # where b1 switches between its two conditions: 1-(1-2eps)/x3 = d/(1-(1-d)x3)
    g = lambda x: 1 - (1 - 2 * eps) / x - d / (1 - (1 - d) * x)
    try:
        rb = mp.findroot(g, 1 - eps)
        if 0 < rb < 1:
            bps.add(rb)
    except Exception:
        pass
    pts = sorted(bps)
    pts = [p for p in pts if 0 <= p <= 1]
    tot = mp.mpf(0)
    for lo, hi in zip(pts[:-1], pts[1:]):
        if hi - lo < mp.mpf(10) ** (-25):
            continue
        # log variable for the 1/x3 behaviour
        if lo == 0:
            lo = mp.mpf(10) ** (-30)
        f = lambda u: v_integral(mp.e ** u, intervals_3jet(mp.e ** u, eps, d))
        tot += mp.quad(f, [mp.log(lo), mp.log(hi)])
    return tot


def asym(eps, delta, exact_d=True):
    d = mp.sin(delta) ** 2 if exact_d else delta ** 2
    return 4 * mp.log(d) * mp.log(2 * eps) + 3 * mp.log(d) + 2 * mp.pi ** 2 / 3 - mp.mpf(7) / 2


print('   eps      delta     Int_3jet(numeric)      asymptotic          diff     (eps ln d)')
rows = []
for (e, dl) in [(1e-2, 0.1), (3e-3, 0.1), (1e-3, 0.1), (1e-3, 0.03), (1e-4, 0.03), (1e-4, 0.01), (1e-5, 0.01),
                (1e-6, 0.003)]:
    e, dl = mp.mpf(e), mp.mpf(dl)
    num = I3jet(e, dl)
    an = asym(e, dl)
    rows.append((e, dl, num, an))
    print('  %7.1e  %7.4f  %18.10f  %18.10f  %10.2e  %9.2e' % (e, dl, num, an, num - an, e * abs(mp.log(mp.sin(dl) ** 2))))
check('S1  numeric Int_3jet -> 4 ln d ln 2eps + 3 ln d + 2pi^2/3 - 7/2 (residual <= 30 (eps|ln d| + d|ln eps|) on all points)',
      all(abs(n - a) <= 30 * (e * abs(mp.log(mp.sin(dl) ** 2)) + mp.sin(dl) ** 2 * abs(mp.log(e))) for e, dl, n, a in rows))
check('S2  residual decreases toward the asymptotic limit (last point |diff| < 1e-3)', abs(rows[-1][2] - rows[-1][3]) < 1e-3)

# two-jet coefficient:  sigma_2jet/sigma_0 = 1 + (C_F as/pi) c2 ;  c2 = 3/4 - Int_3jet/2
print()
print('  two-jet coefficient c2 = (sigma_2jet/sigma_0 - 1)/(C_F alpha_s/pi):')
for e, dl, num, an in rows[-3:]:
    c2 = mp.mpf(3) / 4 - num / 2
    sw = -(4 * mp.log(dl) * mp.log(2 * e) + 3 * mp.log(dl) + mp.pi ** 2 / 3 - mp.mpf(5) / 2)
    sw_beam = -(4 * mp.log(dl) * mp.log(e) + 3 * mp.log(dl) + mp.pi ** 2 / 3 - mp.mpf(5) / 2)
    print('    eps=%7.1e delta=%6.3f  c2(numeric)=%14.8f   SW[ln 2eps]=%14.8f   [ln eps]=%14.8f' % (e, dl, c2, sw, sw_beam))
e, dl, num, an = rows[-1]
c2 = mp.mpf(3) / 4 - num / 2
check('S3  c2 = -(4 ln delta ln 2eps + 3 ln delta + pi^2/3 - 5/2) with eps = fraction of TOTAL energy sqrt(s)',
      abs(c2 + (4 * mp.log(dl) * mp.log(2 * e) + 3 * mp.log(dl) + mp.pi ** 2 / 3 - mp.mpf(5) / 2)) < 1e-3)
check('S4  the variant "4 ln delta ln eps" (eps = fraction of total energy) is NOT correct: differs by 4 ln2 |ln delta|',
      abs(c2 + (4 * mp.log(dl) * mp.log(e) + 3 * mp.log(dl) + mp.pi ** 2 / 3 - mp.mpf(5) / 2)) > 1)

# beam-energy definition: E_out < eps' * (sqrt(s)/2)  <=> eps = eps'/2 : formula with ln(eps')
ep = mp.mpf('2e-6')
num_b = I3jet(ep / 2, mp.mpf('0.003'))
c2b = mp.mpf(3) / 4 - num_b / 2
check('S5  with eps\' = fraction of the BEAM energy sqrt(s)/2 the formula reads 4 ln delta ln eps\' (numerically)',
      abs(c2b + (4 * mp.log(mp.mpf('0.003')) * mp.log(ep) + 3 * mp.log(mp.mpf('0.003')) + mp.pi ** 2 / 3 - mp.mpf(5) / 2)) < 1e-3)

# regime eps > delta: the formula fails (extra logs of eps/delta from recoil/acollinearity)
e2, d2 = mp.mpf('0.05'), mp.mpf('0.005')
num2 = I3jet(e2, d2)
print('   eps>delta example: eps=%.3g delta=%.3g numeric=%.6f asym=%.6f' % (e2, d2, num2, asym(e2, d2)))
check('S6  for eps >> delta the SW asymptotic formula does not apply (deviation > 1)', abs(num2 - asym(e2, d2)) > 1)

print()
print('SUMMARY: %d/%d checks passed' % (sum(p for _, p in PASS), len(PASS)))
