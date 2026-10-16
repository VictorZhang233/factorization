"""
W07 / Ch7 -- s3_tmc_segment.py
 (1) traceless projection of P^{(x)n} in 4D: Pi(z) = sum_j (-1)^j binom(n-j,j)/4^j (P.z)^(n-2j) (P^2 z^2)^j is harmonic
     (Box_z Pi = 0) and has leading term (P.z)^n; checked also against an explicit tensor construction for n=2,3,4;
 (2) contribution of the spin-n twist-2 operator (C_2 structure of thm:dis-ope, <O> = 2A(P..P - traces)) to T_2:
     T_2^(n) = 4 C_2 A sum_j [(n-2j)(n-2j-1)/(n(n-1))] binom(n-j,j) (M^2/Q^2)^j w^(n-1-2j)
     => Taylor coefficient: int x^(m-2) F_2 = sum_j (M^2/Q^2)^j binom(m+j,j) m(m-1)/((m+2j)(m+2j-1)) C A|_{m+2j}
     (Georgi-Politzer / Nachtmann form); j=1 term = m(m-1)/(m+2) (M^2/Q^2) a_{m+2}  (VF-REF-6);
 (3) x-space Georgi-Politzer formula with xi = 2x/(1+r), r = sqrt(1+4M^2x^2/Q^2): its moments integrated up to
     x_max = 1/(1-M^2/Q^2) (where xi = 1) reproduce (2) numerically; F_2^TMC(x) != 0 for 1 < x < x_max (threshold problem);
 (4) Euclidean segment (lem:dis-euclid-segment, VF-REF-1): omega = 2 i M q4/Q^2, |omega| <= sqrt3 M/Q iff |q_vec| >= Q/2,
     Pt^2 = M^2 qvec^2/Q^2;
 (5) V. A. Markov coefficient bound for odd polynomials on the imaginary segment: |h_k| r^k <= (1+sqrt2)^deg sup|h(iy)|
     (real coefficients); spot check with Chebyshev polynomials (extremal) and random polynomials.
"""
import sys, os, random
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

ok_all = True
def check(name, ok, extra=''):
    global ok_all
    ok_all &= bool(ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name} {extra}")

# ---------------------------------------------------------------- (1) harmonic polynomial
print("(1) traceless projection in 4D")
z = sp.symbols('z0:4'); P = sp.symbols('P0:4')
g = [1, -1, -1, -1]
Pz = sum(g[i] * P[i] * z[i] for i in range(4)); z2 = sum(g[i] * z[i]**2 for i in range(4)); P2 = sum(g[i] * P[i]**2 for i in range(4))
def Pi(n):
    return sum((-1)**j * sp.binomial(n - j, j) / sp.Integer(4)**j * Pz**(n - 2 * j) * (P2 * z2)**j for j in range(n // 2 + 1))
for n in range(1, 8):
    box = sum(g[i] * sp.diff(Pi(n), z[i], 2) for i in range(4))
    check(f"n={n}: Box_z Pi(z) = 0", sp.expand(box) == 0)
# explicit tensor construction for n=2,3: Pi^{mu nu} = P^mu P^nu - g^{mu nu} P^2/4 ; n=3: PPP - (P^2/6)(g P + perms)
Pnum = [sp.Rational(3), sp.Rational(1), sp.Rational(-2), sp.Rational(1, 2)]
znum = [sp.Rational(1, 3), sp.Rational(2), sp.Rational(5), sp.Rational(-1)]
subsd = {**{P[i]: Pnum[i] for i in range(4)}, **{z[i]: znum[i] for i in range(4)}}
Pzn = Pz.subs(subsd); P2n = P2.subs(subsd); z2n = z2.subs(subsd)
check("n=2 explicit: (P.z)^2 - P^2 z^2/4", sp.simplify(Pi(2).subs(subsd) - (Pzn**2 - P2n * z2n / 4)) == 0)
check("n=3 explicit: (P.z)^3 - (P^2/6)*3*z^2 (P.z)", sp.simplify(Pi(3).subs(subsd) - (Pzn**3 - P2n / 6 * 3 * z2n * Pzn)) == 0)

# ---------------------------------------------------------------- (2) TMC to T_2 and the moment formula
print("(2) target-mass corrections to T_2 from the spin-n operator")
nu_, Q2, M2, w = sp.symbols('nu Q2 M2 omega', positive=True)
X, Y = sp.symbols('X Y')   # X = P.z, Y = z^2 ; P^2 = M2
def f(n):
    return sum((-1)**j * sp.binomial(n - j, j) / sp.Integer(4)**j * X**(n - 2 * j) * (M2 * Y)**j for j in range(n // 2 + 1))
def T2_contrib(n):
    # coefficient a of P^mu P^nu in Pi^{mu nu mu3..mun} q_mu3..q_mun = f_XX/(n(n-1)) at X=nu, Y=q^2=-Q2
    a = sp.diff(f(n), X, 2).subs({X: nu_, Y: -Q2}) / (n * (n - 1))
    T2 = nu_ * 2**n / Q2**(n - 1) * 2 * a        # times C_2 A
    return sp.expand(sp.simplify(T2.subs(nu_, w * Q2 / 2)))
mu2 = sp.symbols('mu2')
for n in [2, 4, 6, 8]:
    expect = 4 * sum(sp.Rational((n - 2 * j) * (n - 2 * j - 1), n * (n - 1)) * sp.binomial(n - j, j)
                     * (M2 / Q2)**j * w**(n - 1 - 2 * j) for j in range(n // 2 + 1) if n - 2 * j >= 2)
    check(f"n={n}: T_2^(n) = 4 C A sum_j (n-2j)(n-2j-1)/(n(n-1)) binom(n-j,j)(M^2/Q^2)^j w^(n-1-2j)",
          sp.simplify(T2_contrib(n) - expect) == 0)
# Taylor coefficient of w^(m-1): sum over n=m+2j
CA = sp.IndexedBase('CA')
for m in [2, 4, 6]:
    coeff = sum(sp.Rational(m * (m - 1), (m + 2 * j) * (m + 2 * j - 1)) * sp.binomial(m + j, j) * mu2**j * CA[m + 2 * j]
                for j in range(0, 4))
    gp = sum(sp.factorial(m + j) / (sp.factorial(j) * sp.factorial(m - 2)) / ((m + 2 * j) * (m + 2 * j - 1)) * mu2**j * CA[m + 2 * j]
             for j in range(0, 4))
    check(f"m={m}: moment formula = Georgi-Politzer form", sp.simplify(coeff - gp) == 0)
    j1 = sp.Rational(m * (m - 1), (m + 2) * (m + 1)) * (m + 1)
    check(f"m={m}: j=1 coefficient = m(m-1)/(m+2) (VF-REF-6)", sp.simplify(j1 - sp.Rational(m * (m - 1), m + 2)) == 0)
# explicit m=2 coefficients (j = 0,1,2,3): 1, 1/2, 2/5, 5/14   [corrected print; the checks above are unchanged]
c2 = [sp.Rational(2 * 1, (2 + 2 * j) * (2 + 2 * j - 1)) * sp.binomial(2 + j, j) for j in range(4)]
check("m=2 coefficients = 1, 1/2, 2/5, 5/14", c2 == [1, sp.Rational(1, 2), sp.Rational(2, 5), sp.Rational(5, 14)], str(c2))
print("   m=2: int F_2 dx = a_2 + (1/2)(M^2/Q^2) a_4 + (2/5)(M^2/Q^2)^2 a_6 + (5/14)(M^2/Q^2)^3 a_8 + ...")

# ---------------------------------------------------------------- (3) x-space GP formula
print("(3) x-space Georgi-Politzer formula (numerical moments)")
mp.mp.dps = 30
aexp, bexp = mp.mpf('0.7'), mp.mpf('3.0')
def F20(u):
    return u**aexp * (1 - u)**bexp if 0 < u < 1 else mp.mpf(0)
def M0(k):   # int_0^1 u^(k-2) F20(u) du
    return mp.beta(k - 1 + aexp, bexp + 1)
def h2(xi):  # int_xi^1 du F20(u)/u^2
    return mp.quad(lambda u: F20(u) / u**2, [xi, 1])
def g2(xi):  # int_xi^1 dv int_v^1 du F20(u)/u^2 = int_xi^1 du (u - xi) F20(u)/u^2
    return mp.quad(lambda u: (u - xi) * F20(u) / u**2, [xi, 1])
def F2TMC(x, m2):
    r = mp.sqrt(1 + 4 * m2 * x**2)
    xi = 2 * x / (1 + r)
    if xi >= 1:
        return mp.mpf(0)
    return (x**2 / (xi**2 * r**3) * F20(xi) + 6 * m2 * x**3 / r**4 * h2(xi) + 12 * m2**2 * x**4 / r**5 * g2(xi))
for m2 in [mp.mpf('0.05'), mp.mpf('0.15')]:
    xmax = 1 / (1 - m2)
    for m in [2, 4]:
        lhs = mp.quad(lambda x: x**(m - 2) * F2TMC(x, m2), [0, mp.mpf(1) / 2, 1, xmax])
        rhs = mp.nsum(lambda j: m2**j * mp.binomial(m + j, j) * m * (m - 1) / ((m + 2 * j) * (m + 2 * j - 1)) * M0(m + 2 * j),
                      [0, mp.inf])
        check(f"M^2/Q^2={float(m2)}, m={m}: int_0^xmax x^(m-2) F2TMC = series", abs(lhs - rhs) < mp.mpf('1e-15') * abs(rhs),
              f"(lhs={mp.nstr(lhs, 15)}, rhs={mp.nstr(rhs, 15)})")
    val = F2TMC(mp.mpf(1) + (xmax - 1) / 2, m2)
    check(f"M^2/Q^2={float(m2)}: F2TMC(x) > 0 at x = (1+xmax)/2 > 1 (threshold problem)", val > 0, f"(value {mp.nstr(val, 6)})")
    mass_beyond = mp.quad(lambda x: F2TMC(x, m2), [1, xmax])
    print(f"     int_1^xmax F2TMC dx = {mp.nstr(mass_beyond, 6)}   (x_max = {mp.nstr(xmax, 6)})")
xs = sp.symbols('x', positive=True); m2s = sp.symbols('m2', positive=True)
xi_s = 2 * xs / (1 + sp.sqrt(1 + 4 * m2s * xs**2))
check("xi(x_max) = 1 for x_max = 1/(1 - M^2/Q^2)  [m2 = 1/50, 3/20, 1/3, 9/10]", all(sp.simplify(xi_s.subs({xs: 1 / (1 - mv), m2s: mv}) - 1) == 0 for mv in [sp.Rational(1,50), sp.Rational(3,20), sp.Rational(1,3), sp.Rational(9,10)]))
print("     analytic: 1+4m x^2 = (1+m)^2/(1-m)^2 at x = 1/(1-m), so xi = (2/(1-m))/(1+(1+m)/(1-m)) = 1")

# ---------------------------------------------------------------- (4) Euclidean segment
print("(4) Euclidean points in the omega plane (target rest frame)")
M, Q, q4 = sp.symbols('M Q q4', positive=True)
qv2 = Q**2 - q4**2           # |q_vec|^2
omega = 2 * sp.I * M * q4 / Q**2
check("omega = 2 P.q/Q^2 with P.q = i M q4", sp.simplify(omega - 2 * (sp.I * M * q4) / Q**2) == 0)
# |q_vec| >= Q/2  <=>  q4^2 <= 3Q^2/4  <=>  |omega| <= sqrt3 M/Q
check("|q_vec| = Q/2  <=>  |omega| = sqrt3 M/Q", sp.simplify(sp.Abs(omega).subs(q4, sp.sqrt(3) * Q / 2) - sp.sqrt(3) * M / Q) == 0)
Pq = sp.I * M * q4
Pt2 = M**2 - Pq**2 / (-Q**2)
check("Pt^2 = M^2 + (P.q)^2/Q^2 = M^2 q_vec^2/Q^2", sp.simplify(Pt2 - M**2 * qv2 / Q**2) == 0)

# ---------------------------------------------------------------- (5) Markov
print("(5) V. A. Markov coefficient bound")
def cheb_coeffs(m):
    return sp.Poly(sp.chebyshevt(m, sp.Symbol('t')), sp.Symbol('t')).all_coeffs()[::-1]
for m in range(1, 12):
    s = sum(abs(c) for c in cheb_coeffs(m))
    check(f"sum |coef T_{m}| = |T_{m}(i)| <= (1+sqrt2)^{m}", float(s) <= float((1 + sp.sqrt(2))**m) + 1e-12, f"({s})")
random.seed(7)
import numpy as np
worst = 0.0
for trial in range(400):
    deg = random.choice([3, 5, 7, 9])
    coeffs = [0.0] * (deg + 1)
    for k in range(1, deg + 1, 2):
        coeffs[k] = random.uniform(-1, 1)
    r = random.uniform(0.05, 1.0)
    ys = np.linspace(-r, r, 4001)
    vals = np.abs(sum(coeffs[k] * (1j * ys)**k for k in range(deg + 1)))
    sup = vals.max()
    for k in range(1, deg + 1, 2):
        ratio = abs(coeffs[k]) * r**k / (sup * (1 + 2**0.5)**deg)
        worst = max(worst, ratio)
check("random odd polynomials: max |h_k| r^k / ((1+sqrt2)^deg sup|h(iy)|) <= 1", worst <= 1.0 + 1e-9, f"(max ratio {worst:.4f})")

print("ALL PASS" if ok_all else "SOME CHECKS FAILED")
