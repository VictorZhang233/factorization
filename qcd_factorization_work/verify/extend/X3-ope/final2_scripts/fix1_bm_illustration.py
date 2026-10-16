"""
fix1_bm_illustration.py  (X3 final2, Fix 1: Remark F.5 / prop:appM-zero-momentum-insertion)

ILLUSTRATIONS (not proofs) of the Breitenlohner-Maison mechanics used in the revised Remark F.5.  Euclidean
one-loop integrals, D = 4 - 2*delta, measure d^Dk / pi^(D/2).  BM's epsilon (here: eps) is the damping parameter
of the alpha-representation, exp(-eps * sum alpha), i.e. every massless denominator k^2 -> k^2 + eps
(eps has mass dimension 2; BM I, Sect. III: "eps ... acts like a mass term").  The dimension is D (BM: n).

 (a) alpha-representation: int_0^inf d alpha exp(-alpha (k^2 + eps)) = 1/(k^2 + eps)  (damping <-> eps-shift).
 (b) a quadratically divergent subgraph (scalar-QED-type trace) S(p) = int (2k+p)^2 / ((k^2+eps)((k+p)^2+eps)):
     omega = 2, so the BM II IR subtraction is T^{Omega-1} = T^1 (value and first derivative at p = 0; the first
     derivative vanishes by O(4) invariance).  S(0) = 2 D Gamma(1-D/2) eps^(D/2-1): its pole part is -8 eps/delta
     (an eps-proportional counterterm, BM I proof of Thm 1), and
        T^1 (1-C) S = (1-C) S(0) = eps (8 ln eps + 8 gamma_E - 4) -> 0   (degree 1 in eps up to logs).
 (c) such an eps-proportional vertex, c*eps*ln(eps), inserted on a massless line of a one-loop bubble at
     Euclidean p^2 = 1: c eps ln(eps) * J(eps),  J = int d^4k/pi^2 1/((k^2+eps)^2 ((k+p)^2+eps))
                                                  = int_0^1 dx (1-x)/(x(1-x)+eps) ~ ln(1/eps)    ->  contribution -> 0.
 (d) a zero-momentum insertion (exceptional configuration) mimicking a twist-2 vertex: numerator (Delta.k)^m k^2,
     Delta null, two propagators at the same momentum k:
        I_eps(p) = int (Delta.k)^m k^2 / ((k^2+eps)^2 ((p-k)^2+eps)) = (Delta.p)^m [ I1 - eps I2 ],
        I1 = Gamma(delta) int_0^1 x^m L^(-delta),  I2 = Gamma(1+delta) int_0^1 x^m (1-x) L^(-1-delta),
        L = x(1-x)p^2 + eps   (Feynman parameters; Delta^2 = 0 kills all l-dependence of the numerator).
     Pole part 1/((m+1) delta), eps-independent.  Finite part (1-C) I_eps at D = 4:
        -gamma_E/(m+1) - int x^m ln L - eps int x^m (1-x)/L   ->   (1-C) I_0 = F'(0),
        I_0 = (p^2)^(-delta) Gamma(delta) Gamma(1+m-delta) Gamma(1-delta)/Gamma(2+m-2 delta) = F(delta)/delta (undamped DR).
     On p^2 > 0 (Euclidean = Minkowski p^2 < 0): (1-C) I_0 = (Delta.p)^m [c0 + c1 ln p^2], c1 = -1/(m+1).
Run: python3 -I fix1_bm_illustration.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 30
ok_all = True
gE = mp.euler

# (a)
a_ok = True
for k2, eps in ((mp.mpf('0.7'), mp.mpf('0.01')), (mp.mpf(3), mp.mpf('1e-4'))):
    val = mp.quad(lambda a: mp.e**(-a * (k2 + eps)), [0, mp.inf])
    a_ok &= abs(val - 1 / (k2 + eps)) < mp.mpf(10)**-20
print("(a) int_0^inf exp(-alpha (k^2+eps)) d alpha = 1/(k^2+eps): %s" % a_ok, flush=True)
ok_all &= a_ok

# (b) Laurent coefficients of S(0) via Taylor expansion of delta*S0(delta)
b_ok = True
for eps in (mp.mpf('1e-2'), mp.mpf('1e-4'), mp.mpf('1e-6')):
    g = lambda d: 2 * (4 - 2 * d) * mp.gamma(1 + d) / (d - 1) * eps**(1 - d)   # = d * S0(d), using d Gamma(d-1) = Gamma(1+d)/(d-1)
    c = mp.taylor(g, 0, 1)          # c[0] = pole coefficient, c[1] = finite part
    pole, fin = c[0], c[1]
    pred_pole = -8 * eps; pred_fin = eps * (8 * mp.log(eps) + 8 * gE - 4)
    good = abs(pole - pred_pole) < mp.mpf(10)**-20 and abs(fin - pred_fin) < mp.mpf(10)**-20
    b_ok &= good
    print("(b) eps=%.0e : pole of S(0) = %.6e (-8 eps) ; (1-C)S(0) = %.6e (= eps(8 ln eps + 8 gE - 4) = %.6e) %s"
          % (float(eps), float(pole), float(fin), float(pred_fin), good), flush=True)
ok_all &= b_ok

# (c)
c_vals = []
for eps in (mp.mpf('1e-2'), mp.mpf('1e-4'), mp.mpf('1e-6'), mp.mpf('1e-8')):
    J = mp.quad(lambda x: (1 - x) / (x * (1 - x) + eps), [0, eps, mp.sqrt(eps), mp.mpf('0.5'), 1])
    contrib = eps * mp.log(eps) * J
    c_vals.append(abs(contrib))
    print("(c) eps=%.0e : J = %.4f (ln(1/eps) = %.4f) ; eps ln(eps) J = %.3e" % (float(eps), float(J), float(-mp.log(eps)), float(contrib)), flush=True)
c_ok = all(c_vals[i + 1] < c_vals[i] for i in range(len(c_vals) - 1)) and c_vals[-1] < mp.mpf('1e-5')
print("    contribution decreases monotonically to 0: %s" % c_ok, flush=True)
ok_all &= c_ok

# (d)
def fin_damped(eps, m, P2):
    L = lambda x: x * (1 - x) * P2 + eps
    pts = [0, eps / (P2 + eps), mp.mpf('0.5'), 1 - eps / (P2 + eps), 1]
    A = mp.quad(lambda x: x**m * mp.log(L(x)), pts)
    B = mp.quad(lambda x: x**m * (1 - x) / L(x), pts)
    return -gE / (m + 1) - A - eps * B
def fin_undamped(m, P2):
    F = lambda d: P2**(-d) * mp.gamma(1 + d) * mp.gamma(1 + m - d) * mp.gamma(1 - d) / mp.gamma(2 + m - 2 * d)
    return mp.diff(F, 0), F(0)
d_ok = True
for m in (1, 3):
    for P2 in (mp.mpf(1), mp.mpf(5)):
        f0, pole0 = fin_undamped(m, P2)
        devs = [abs(fin_damped(eps, m, P2) - f0) for eps in (mp.mpf('1e-3'), mp.mpf('1e-5'), mp.mpf('1e-7'), mp.mpf('1e-9'))]
        conv = all(devs[i + 1] < devs[i] for i in range(len(devs) - 1)) and devs[-1] < mp.mpf('1e-6')
        d_ok &= conv and abs(pole0 - mp.mpf(1) / (m + 1)) < mp.mpf(10)**-25
        print("(d) m=%d p^2=%s: pole = %.6f (1/(m+1)); |(1-C)I_eps - (1-C)I_0| at eps=1e-3,1e-5,1e-7,1e-9: %s"
              % (m, P2, float(pole0), ", ".join("%.1e" % float(x) for x in devs)), flush=True)
    f1 = fin_undamped(m, mp.mpf(1))[0]; f2 = fin_undamped(m, mp.mpf(5))[0]; f3 = fin_undamped(m, mp.mpf(25))[0]
    slope = (f2 - f1) / mp.log(5); lin = abs((f3 - f2) / mp.log(5) - slope) < mp.mpf(10)**-20
    d_ok &= lin and abs(slope + mp.mpf(1) / (m + 1)) < mp.mpf(10)**-20
    print("    (1-C)I_0 = (Delta.p)^m [c0 + c1 ln p^2], c1 = %.6f (-1/(m+1) = %.6f), exactly linear in ln p^2: %s"
          % (float(slope), -1 / (m + 1), lin), flush=True)
ok_all &= d_ok
print("RESULT:", "PASS" if ok_all else "FAIL")
