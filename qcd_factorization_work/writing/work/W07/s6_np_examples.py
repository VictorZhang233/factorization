"""
W07 / Ch7 -- s6_np_examples.py  (prop:dis-low-moments, rem:dis-pt-growth, ex:dis-segment-numbers,
                                  ex:dis-tmc-n2, thm:dis-bjorken numbers)
 (1) descending-induction identity (prop:dis-low-moments): if
        T_2(w) = sum_{n<k} t_n w^{n-1} + 4 w^{k-1} int_0^1 x^{k-2} F(x)/(1 - x^2 w^2) dx
     then for real y
        T_2(iy)/(iy) = sum_{n<k-2} t_n (iy)^{n-2} + (iy)^{k-4} [ t_{k-2} - 4 int x^{k-4} F x^2y^2/(1+x^2y^2) dx ];
     checked numerically for a test measure F dx = (smooth) + (elastic delta at x=1), k = 4, 6.
 (2) fixed pole: T_2 -> T_2 + c w changes t_2 by c, is invisible in F_2 (Disc unchanged), and for the
     n_0 = 2 representation plus c w one has T_2(iy)/(iy) -> c: the growth condition fails iff c != 0.
 (3) non-integrable F ~ x^{-6/5}: the n_0 = 4 representation exists (int x^2 F < inf), int F = inf and
     T_2(iy)/(iy) grows like y^{1/5}: growth condition fails, momentum-type sum rule meaningless.
 (4) Euclidean segment half-length sqrt3 M/Q for the proton, Q = 2, 10, 100 GeV.
 (5) target-mass correction of the n = 2 moment for a toy twist-2 F_2^(0) = x^0.7 (1-x)^3:
     int F_2 = a_2 + (1/2)(M^2/Q^2) a_4 + (2/5)(M^2/Q^2)^2 a_6 + ...; numbers at Q^2 = 2, 5, 10 GeV^2.
 (6) Bjorken coefficient at a = alpha_s/pi = 0.1, n_f = 3 (VF-POL-1).
Run: python3 -I s6_np_examples.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp

mp.mp.dps = 30
ok_all = True
def check(name, ok, extra=''):
    global ok_all
    ok_all &= bool(ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name} {extra}")

# ------------------------------------------------------------------ (1)
print("(1) descending-induction identity")
el = mp.mpf('0.15')                         # elastic weight at x = 1
fs = lambda x: x**mp.mpf('0.4') * (1 - x)**3   # smooth part
def mom(j):                                 # int x^j F dx (elastic included)
    return mp.quad(lambda x: x**j * fs(x), [0, 1]) + el
def T2(w, k, tsub):
    # representation with n_0 = k and given subtraction constants t_n (n<k, even)
    I = mp.quad(lambda x: x**(k - 2) * fs(x) / (1 - x**2 * w**2), [0, 1]) + el / (1 - w**2)
    return sum(tsub[n] * w**(n - 1) for n in tsub if n < k) + 4 * w**(k - 1) * I
for k in (4, 6):
    tsub = {n: 4 * mom(n - 2) for n in range(2, k, 2)}   # sum rules satisfied
    for y in (mp.mpf(3), mp.mpf(40)):
        lhs = T2(1j * y, k, tsub) / (1j * y)
        br = tsub[k - 2] - 4 * (mp.quad(lambda x: x**(k - 4) * fs(x) * x**2 * y**2 / (1 + x**2 * y**2), [0, 1])
                                + el * y**2 / (1 + y**2))
        rhs = sum(tsub[n] * (1j * y)**(n - 2) for n in tsub if n < k - 2) + (1j * y)**(k - 4) * br
        check(f"k={k}, y={float(y)}: identity", abs(lhs - rhs) < mp.mpf('1e-20') * (1 + abs(lhs)), f"(|lhs|={mp.nstr(abs(lhs), 8)})")
# with all low sum rules satisfied, T_2(iy)/(iy) -> 0
tsub = {2: 4 * mom(0), 4: 4 * mom(2)}
vals = [abs(T2(1j * mp.mpf(y), 6, tsub) / (1j * mp.mpf(y))) for y in (10, 100, 1000, 10000)]
check("sum rules satisfied => |T_2(iy)/(iy)| -> 0", vals[-1] < vals[0] / 50, f"{[mp.nstr(v, 5) for v in vals]}")

# ------------------------------------------------------------------ (2)
print("(2) fixed pole c*w")
c = mp.mpf('0.3')
def T2fp(w):
    return 4 * w * (mp.quad(lambda x: fs(x) / (1 - x**2 * w**2), [0, 1]) + el / (1 - w**2)) + c * w
t2 = mp.diff(lambda w: T2fp(w), 0)          # Taylor coefficient of w^1
check("t_2 - 4 int F_2 = c (fixed pole shifts the n=2 Taylor coefficient)", abs(t2 - 4 * mom(0) - c) < mp.mpf('1e-15'),
      f"(t_2={mp.nstr(t2, 12)}, 4M_2={mp.nstr(4 * mom(0), 12)})")
for y in (100, 10000):
    v = T2fp(1j * mp.mpf(y)) / (1j * mp.mpf(y))
    print(f"     T_2(iy)/(iy) at y={y}: {mp.nstr(v, 10)}")
check("T_2(iy)/(iy) -> c", abs(T2fp(1j * mp.mpf(10**6)) / (1j * mp.mpf(10**6)) - c) < mp.mpf('1e-4'))
print("     Disc T_2 is unchanged by c w (entire, real): F_2 cannot see the fixed pole")

# ------------------------------------------------------------------ (3)
print("(3) non-integrable F_2 ~ x^(-6/5)")
fn = lambda x: x**(-mp.mpf(6) / 5) * (1 - x)**3
def T2n(w):   # n_0 = 4 representation, t_2 chosen arbitrarily (=1)
    return 1 * w + 4 * w**3 * mp.quad(lambda x: x**2 * fn(x) / (1 - x**2 * w**2), [0, mp.mpf('1e-30'), 1e-6, 1e-3, 1])
r = []
for y in (1e2, 1e4, 1e6):
    v = T2n(1j * mp.mpf(y)) / (1j * mp.mpf(y))
    r.append(v)
    print(f"     y={y:.0e}: T_2(iy)/(iy) = {mp.nstr(v, 8)},  divided by y^(1/5): {mp.nstr(v / mp.mpf(y)**(mp.mpf(1)/5), 8)}")
# asymptotics: T_2(iy)/(iy) = -4 [ (pi/2)/sin(0.9 pi) ] y^(1/5) + const + o(1)   (x = u/y in the k=4 form)
slope = (r[2] - r[1]) / (mp.mpf(1e6)**(mp.mpf(1)/5) - mp.mpf(1e4)**(mp.mpf(1)/5))
pred = -4 * (mp.pi / 2) / mp.sin(mp.mpf('0.9') * mp.pi)
check("T_2(iy)/(iy) = -4 (pi/2)/sin(0.9pi) y^(1/5) + const + o(1): diverges, growth condition fails",
      abs(slope.real - pred) < 0.01 * abs(pred), f"(slope {mp.nstr(slope.real, 6)}, predicted {mp.nstr(pred, 6)})")

# ------------------------------------------------------------------ (4)
print("(4) Euclidean segment I_Q = {iy: |y| <= sqrt3 M/Q}, proton M = 0.938 GeV")
M = mp.mpf('0.938')
for Q in (2, 10, 100):
    print(f"     Q = {Q:>3} GeV: sqrt3 M/Q = {mp.nstr(mp.sqrt(3) * M / Q, 4)}")
check("sqrt3*0.938/10 = 0.1625", abs(mp.sqrt(3) * M / 10 - mp.mpf('0.16247')) < 1e-4)

# ------------------------------------------------------------------ (5)
print("(5) target-mass correction of the n=2 moment, toy F_2^(0) = x^0.7 (1-x)^3")
a = lambda n: mp.beta(n - 1 + mp.mpf('0.7'), 4)       # a_n = int x^{n-2} F_2^(0)
coef = lambda m, j: mp.binomial(m + j, j) * m * (m - 1) / ((m + 2 * j) * (m + 2 * j - 1))
check("coefficients m=2: 1, 1/2, 2/5, 5/14", all(abs(coef(2, j) - v) < 1e-25 for j, v in
      enumerate([1, mp.mpf(1) / 2, mp.mpf(2) / 5, mp.mpf(5) / 14])))
print(f"     a_4/a_2 = {mp.nstr(a(4) / a(2), 6)}  (exact (2.7*1.7)/(6.7*5.7) = {mp.nstr(mp.mpf('2.7') * mp.mpf('1.7') / (mp.mpf('6.7') * mp.mpf('5.7')), 6)})")
check("a_4/a_2 = (2.7 1.7)/(6.7 5.7)", abs(a(4) / a(2) - mp.mpf('2.7') * mp.mpf('1.7') / (mp.mpf('6.7') * mp.mpf('5.7'))) < 1e-25)
for Q2 in (2, 5, 10):
    m2 = M**2 / Q2
    first = coef(2, 1) * m2 * a(4) / a(2)
    full = mp.nsum(lambda j: coef(2, j) * m2**j * a(2 + 2 * j), [1, mp.inf]) / a(2)
    print(f"     Q^2 = {Q2:>2} GeV^2: M^2/Q^2 = {mp.nstr(m2, 4)}; first-order rel. correction {mp.nstr(first, 4)}, all orders {mp.nstr(full, 4)}")

# ------------------------------------------------------------------ (6)
print("(6) Bjorken coefficient")
aval = mp.mpf('0.1'); nf = 3
Cb = 1 - aval - (mp.mpf(55) / 12 - mp.mpf(nf) / 3) * aval**2
print(f"     C_Bjp(a=0.1, n_f=3) = 1 - 0.1 - 3.5833*0.01 = {mp.nstr(Cb, 6)}")
check("a^2 coefficient at n_f=3 = -3.5833", abs(-(mp.mpf(55) / 12 - 1) + mp.mpf('3.58333333')) < 1e-7)

print("ALL PASS" if ok_all else "SOME CHECKS FAILED")
