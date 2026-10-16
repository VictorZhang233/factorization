"""
rv21_box.py  (round-2 reviewer #1, independent check of Theorem F (F1),(F2) on a graph with MIXED-SIGN F1hat)

One-loop forward box, Euclidean, Q^2 = 1, lines (powers): e1 = k (a1), e2 = k+p (a2), e3 = k+p+q (a3), e4 = k+q (a4),
external: p in at V1, q in at V2, -p at V3, -q at V4;  p^2 = 0, omega = 2 p.q/Q^2 (Minkowski) = -2 p_E.q_E.
2-forests:  F = x2x3 + x1x4 + (1-omega) x1x3 + (1+omega) x2x4   (both signs of c_p c_q occur).

(A) parametric side.  With x1+x2 = s, x1 = s y, x3 = (1-s) z:  F = s(1-s) [1 - omega (y+z-1)], U = 1, so
    I(omega) = Gamma(c)/prod Gamma(a_i) * B(a1+a2-c, a3+a4-c) * K(omega),   c = a - D/2,
    K(omega) = int_0^1 int_0^1 y^{a1-1}(1-y)^{a2-1} z^{a3-1}(1-z)^{a4-1} [1 - omega(y+z-1)]^{-c} dy dz.
    (y+z-1 in [-1,1]: the bracket vanishes only for real omega with |omega| >= 1 -> holomorphic on the cut plane.)
    Parametric Taylor coefficients:  K_n = (c)_n/n! * M_n,  M_n = sum_{r+s+t=n} n!/(r!s!t!) (-1)^t B(a1+r,a2) B(a3+s,a4).
(B) momentum side (independent): naive Taylor expansion of 1/((k+p)^2)^{a2} 1/((k+p+q)^2)^{a3} in p (p^2 = 0),
    reduced with the one-loop traceless tensor formula
      int d^Dk/pi^{D/2} (k.p)^m / [(k^2)^al ((k+q)^2)^be] = (-q.p)^m (q^2)^{D/2-al-be} G(al,be;m),
      G = Gamma(al+be-D/2) Gamma(m+D/2-al) Gamma(D/2-be) / (Gamma(al) Gamma(be) Gamma(m+D-al-be)).
    The formula itself is re-derived numerically below (Feynman-parameter check).
Checks: (1) tensor formula; (2) c_n(momentum) == c_n(parametric) for n = 0..10 at random complex (a_i, D);
        (3) full parametric integral at complex omega (|omega| < 1) == sum_n c_n omega^n;
        (4) evaluation at omega in the cut plane outside the unit disk (holomorphy, F1) vs. a Pade-free check:
            analytic continuation of the series via the Euler transform omega -> omega/(omega-1)... not needed;
            instead compare K(omega) with its own Cauchy integral around a small circle (consistency of holomorphy).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import random

mp.mp.dps = 30
rng = random.Random(7)

def G(al, be, m, D):
    return (mp.gamma(al + be - D/2) * mp.gamma(m + D/2 - al) * mp.gamma(D/2 - be)
            / (mp.gamma(al) * mp.gamma(be) * mp.gamma(m + D - al - be)))

def binom_gen(x, k):
    # generalized binomial coefficient binom(x, k), x complex, k integer >= 0
    r = mp.mpf(1)
    for i in range(k):
        r *= (x - i) / (i + 1)
    return r

# ---------------------------------------------------------------- (1) tensor formula, Feynman-parameter check
def tensor_feynman(al, be, m, D):
    # int (k.p)^m/[(k^2)^al ((k+q)^2)^be]  = (-q.p)^m (q^2)^{..} * this, by shifting k = l - x q (p^2 = 0)
    f = lambda x: x**(m + be - 1) * (1 - x)**(al - 1) * (x * (1 - x))**(D/2 - al - be)
    return mp.gamma(al + be - D/2) / (mp.gamma(al) * mp.gamma(be)) * mp.quad(f, [0, 1])

print("(1) one-loop traceless tensor formula vs Feynman-parameter integral (convergent points)")
for (al, be, m, D) in [(1.3, 1.1, 0, 5.1), (1.2, 1.4, 2, 5.6), (1.05, 1.25, 5, 5.9)]:
    a, b = G(al, be, m, D), tensor_feynman(al, be, m, D)
    print("   al=%.2f be=%.2f m=%d D=%.2f  formula=%s  quad=%s  rel=%.1e" % (al, be, m, D, mp.nstr(a, 15), mp.nstr(b, 15), abs(a/b - 1)))

# ---------------------------------------------------------------- (2) naive momentum-space terms vs parametric terms
def c_mom(n, a1, a2, a3, a4, D):
    tot = mp.mpf(0)
    for i in range(n + 1):
        j = n - i
        pre = binom_gen(-a2, i) * binom_gen(-a3, j)
        s = mp.mpf(0)
        for l in range(j + 1):
            # 2^n (k.p)^i ((k.p)+(q.p))^j, (-q.p) = omega/2, (q.p) = -omega/2 :  2^n (1/2)^{i+l} (-1/2)^{j-l} = (-1)^{j-l}
            s += mp.binomial(j, l) * (-1)**(j - l) * G(a1 + a2 + i, a3 + a4 + j, i + l, D)
        tot += pre * s
    return tot

def B(x, y):
    return mp.gamma(x) * mp.gamma(y) / mp.gamma(x + y)

def c_par(n, a1, a2, a3, a4, D):
    a = a1 + a2 + a3 + a4
    c = a - D/2
    pref = mp.gamma(c) / (mp.gamma(a1) * mp.gamma(a2) * mp.gamma(a3) * mp.gamma(a4)) * B(a1 + a2 - c, a3 + a4 - c)
    Mn = mp.mpf(0)
    for r in range(n + 1):
        for s in range(n + 1 - r):
            t = n - r - s
            Mn += mp.factorial(n) / (mp.factorial(r) * mp.factorial(s) * mp.factorial(t)) * (-1)**t \
                  * B(a1 + r, a2) * B(a3 + s, a4)
    return pref * mp.rf(c, n) / mp.factorial(n) * Mn

print("\n(2) omega^n coefficient: momentum-space naive term / parametric Taylor term (random complex a_i, D)")
worst = 0
for trial in range(4):
    a1, a2, a3, a4 = [mp.mpc(rng.uniform(0.6, 1.6), rng.uniform(-0.3, 0.3)) for _ in range(4)]
    D = mp.mpc(rng.uniform(4.6, 6.4), rng.uniform(-0.3, 0.3))
    for n in range(0, 11):
        cm, cp = c_mom(n, a1, a2, a3, a4, D), c_par(n, a1, a2, a3, a4, D)
        rel = abs(cm / cp - 1)
        worst = max(worst, rel)
    print("   trial %d: max_n<=10 |ratio-1| so far = %.2e" % (trial, worst))
print("   RESULT (2): worst |c_mom/c_par - 1| over 4 points x 11 orders = %.2e" % worst)

# ---------------------------------------------------------------- (3) full integral at complex omega vs series
# NOTE: the alternating sums in c_mom lose roughly n digits; coefficients are therefore computed at 100 digits
# (a first run at 20 digits gave a spurious 7e-6 mismatch at omega = 0.8i, which disappears at high precision).
mp.mp.dps = 100
a1, a2, a3, a4, D = mp.mpf('1.0'), mp.mpf('1.2'), mp.mpf('0.9'), mp.mpf('1.1'), mp.mpf('5.3')
a = a1 + a2 + a3 + a4
c = a - D/2
pref = mp.gamma(c) / (mp.gamma(a1) * mp.gamma(a2) * mp.gamma(a3) * mp.gamma(a4)) * B(a1 + a2 - c, a3 + a4 - c)

def K(om):
    f = lambda y, z: y**(a1 - 1) * (1 - y)**(a2 - 1) * z**(a3 - 1) * (1 - z)**(a4 - 1) * (1 - om * (y + z - 1))**(-c)
    return mp.quad(f, [0, 0.5, 1], [0, 0.5, 1])

coef = [c_mom(n, a1, a2, a3, a4, D) for n in range(0, 121)]
mp.mp.dps = 20
print("\n(3) a=(1,1.2,0.9,1.1), D=5.3: parametric integral vs sum of momentum-space naive terms")
for om in [mp.mpc(0.3, 0), mp.mpc(-0.5, 0.2), 0.6 * mp.exp(1j * mp.pi / 3), mp.mpc(0.0, 0.8)]:
    full = pref * K(om)
    ser = mp.fsum(coef[n] * om**n for n in range(len(coef)))
    print("   omega=%-28s  full=%-34s series=%-34s rel=%.1e" % (mp.nstr(om, 6), mp.nstr(full, 12), mp.nstr(ser, 12), abs(full/ser - 1)))

# ---------------------------------------------------------------- (4) outside the unit disk, inside the cut plane
print("\n(4) omega outside |omega|<1 but in the cut plane: parametric integral is finite and holomorphic")
for om in [mp.mpc(1.5, 0.7), mp.mpc(-2.0, 0.5), mp.mpc(0.0, 2.5)]:
    # holomorphy check: value vs mean over a small circle (mean value property), radius 0.1
    val = pref * K(om)
    circ = mp.fsum(pref * K(om + 0.1 * mp.exp(2j * mp.pi * k / 8)) for k in range(8)) / 8
    print("   omega=%-14s I=%-36s  |I - circle mean|/|I| = %.1e (8-point trapezoid; O(r^8) for holomorphic I)"
          % (mp.nstr(om, 4), mp.nstr(val, 12), abs(val - circ) / abs(val)))
print("   |c_n| at n = 20, 60, 120: %s  (power-law decay; radius of convergence 1)" % [mp.nstr(abs(coef[n]), 5) for n in (20, 60, 120)])
