"""
fix1_homogeneity.py  (X3 final2, Fix 1: Proposition F.5, step 2 -- identification lim R^S = lim R^C)

Checks, on the explicit one-loop example of a quadratically divergent subgraph (Omega_H = omega_H = 2), the two
analytic facts used in step 2 of the revised proof:

  (H1) joint homogeneity + MS structure: the IR-subtraction coefficient
           c_0(eta, mu, D) = (1 - C)[ mu^{4-D} S_eta(0) ] ,   S_eta(0) = int d^Dk/pi^{D/2} (2k)^2/(k^2+eta)^2
                           = 2 D Gamma(1-D/2) eta^{D/2-1}
       (C = pole part at D = 4, eta = BM's damping parameter acting as a common mass^2 of all lines) is a finite sum
       of terms mu^{(4-D) h_t} eta^{(Omega - j - (4-D) h_t)/2} g_t(D) (here h_t in {0, 1}: the pole term -8 eta/delta
       has h_t = 0) ; hence
         (a) c_0 is analytic at D = 4 (the Laurent coefficient of order -1 vanishes; checked by a contour integral),
         (b) sup_{|D-4| = 2r} |c_0(eta, mu, D)| <= K eta^{1 - r} -> 0 as eta -> 0 (r = 0.2 here), so all Taylor
             coefficients in (D-4) vanish as eta -> 0 (Cauchy),
         (c) at D = 4:  c_0(eta, mu, 4) = eta^{(Omega-j)/2} P(ln(mu^2/eta)) with P a polynomial with constant
             coefficients (here P(x) = 8 gamma_E - 4 - 8 x):  c_0/eta depends on (eta, mu) only through eta/mu^2 and
             is affine in ln(eta/mu^2).
  (H2) the functional-equation argument: a function of (eta, mu) jointly homogeneous of degree d > 0 in (sqrt eta, mu)
       and polynomial of degree K in ln mu is eta^{d/2} P(ln(mu^2/eta)); checked on c_0 with d = Omega - j = 2.
Run: python3 -I fix1_homogeneity.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 30
ok_all = True
gE = mp.euler

def c0(eta, mu, delta):
    """(1-C)[mu^{2 delta} S_eta(0)], D = 4 - 2 delta; pole part of the bracket at delta = 0 is -8 eta / delta"""
    D = 4 - 2 * delta
    return mu**(2 * delta) * 2 * D * mp.gamma(1 - D / 2) * eta**(D / 2 - 1) + 8 * eta / delta

# (a) analyticity at D = 4: residue of c0 in delta at 0 (contour |delta| = rho)
a_ok = True
for eta, mu in ((mp.mpf('0.01'), mp.mpf(1)), (mp.mpf('1e-4'), mp.mpf(3))):
    rho = mp.mpf('0.1')
    res = mp.quad(lambda th: c0(eta, mu, rho * mp.e**(1j * th)) * rho * mp.e**(1j * th), [0, 2 * mp.pi]) / (2 * mp.pi)
    a_ok &= abs(res) < mp.mpf(10)**-20
    print("(a) eta=%.0e mu=%s : residue of c_0 at D=4 = %.1e  (analytic at D = 4: %s)" % (float(eta), mu, float(abs(res)), abs(res) < 1e-20))
ok_all &= a_ok

# (b) uniform vanishing on the circle |delta| = r  (|D - 4| = 2r)
r = mp.mpf('0.2')
sups = []
for eta in (mp.mpf('1e-2'), mp.mpf('1e-4'), mp.mpf('1e-6'), mp.mpf('1e-8')):
    s = max(abs(c0(eta, mp.mpf(1), r * mp.e**(1j * 2 * mp.pi * k / 64))) for k in range(64))
    sups.append(s)
    print("(b) eta=%.0e : sup_{|D-4|=0.4} |c_0| = %.3e ;  ratio to eta^(1-r) = %.3f" % (float(eta), float(s), float(s / eta**(1 - r))))
b_ok = all(sups[i + 1] < sups[i] for i in range(len(sups) - 1)) and max(sups[i] / [mp.mpf('1e-2'), mp.mpf('1e-4'), mp.mpf('1e-6'), mp.mpf('1e-8')][i]**(1 - r) for i in range(4)) < 100
print("    decreasing to 0, bounded by K eta^(1-r): %s" % b_ok)
ok_all &= b_ok

# Taylor coefficients in delta at delta = 0 (orders 0..3) via Cauchy integrals: all -> 0 with eta, like
# eta (1+|ln eta|)^(m+1) (the m-th coefficient of eta^{1-delta} mu^{2 delta} Gamma(-1+delta) carries ln^{m+1} eta)
t_ok = True
etas = (mp.mpf('1e-3'), mp.mpf('1e-6'), mp.mpf('1e-9'), mp.mpf('1e-12'))
for m in range(4):
    vals = []; ratios = []
    for eta in etas:
        rho = mp.mpf('0.1')
        cm = mp.quad(lambda th: c0(eta, mp.mpf(1), rho * mp.e**(1j * th)) * (rho * mp.e**(1j * th))**(-m), [0, 2 * mp.pi]) / (2 * mp.pi)
        vals.append(abs(cm)); ratios.append(abs(cm) / (eta * (1 + abs(mp.log(eta)))**(m + 1)))
    t_ok &= all(vals[i + 1] < vals[i] for i in range(len(vals) - 1)) and max(ratios) < 20
    print("    Taylor coefficient of order %d in delta: |c| at eta = 1e-3, 1e-6, 1e-9, 1e-12 : %s ; max |c|/(eta(1+|ln eta|)^%d) = %.3f"
          % (m, ", ".join("%.2e" % float(v) for v in vals), m + 1, float(max(ratios))))
print("    all Taylor coefficients (orders 0..3) decrease to 0 like eta |ln eta|^(m+1): %s" % t_ok)
ok_all &= t_ok

# (c) + (H2): structure at D = 4
def c0_at4(eta, mu):
    return mp.limit(lambda d: c0(eta, mu, d), 0) if False else mp.diff(lambda d: d * c0(eta, mu, d), 0)   # = lim_{delta->0} c0
c_ok = True
pts = [(mp.mpf('1e-2'), mp.mpf(1)), (mp.mpf('1e-2') * 9, mp.mpf(3)), (mp.mpf('1e-4'), mp.mpf('0.5')), (mp.mpf('3e-5'), mp.mpf(2))]
for eta, mu in pts:
    val = c0_at4(eta, mu)
    pred = eta * (8 * gE - 4 - 8 * mp.log(mu**2 / eta))
    c_ok &= abs(val - pred) < mp.mpf(10)**-15 * max(1, abs(pred))
    print("(c) eta=%.1e mu=%s : c_0(D=4) = %.10e ; eta*(8 gE - 4 - 8 ln(mu^2/eta)) = %.10e" % (float(eta), mu, float(val), float(pred)))
# homogeneity: (eta, mu) -> (lambda^2 eta, lambda mu) multiplies c_0(D=4) by lambda^2 (degree Omega - j = 2)
lam = mp.mpf('1.7')
h = abs(c0_at4(lam**2 * mp.mpf('1e-3'), lam * mp.mpf('0.8')) - lam**2 * c0_at4(mp.mpf('1e-3'), mp.mpf('0.8')))
c_ok &= h < mp.mpf(10)**-15
print("    joint homogeneity of degree 2 in (sqrt(eta), mu): deviation = %.1e ; polynomial (affine) in ln(mu^2/eta): %s" % (float(h), c_ok))
ok_all &= c_ok
print("RESULT:", "PASS" if ok_all else "FAIL")
