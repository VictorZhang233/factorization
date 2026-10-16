"""
h1_hadronic_checks.py -- checks of the elementary identities and inequalities used in Part III (hadron-level
DIS moment theorem) of the report.

 (a) Lemma 3.4 (Jensen): J(y) = (1/2pi) int_0^{2pi} log|y + 2 sin th| dth = log max(1,|w_+|,|w_-|) >= 0,
     w^2 + i y w - 1 = 0 ; J = 0 for |y| <= 2.
 (b) projector: T = -gt T1 + Ph Ph T2/nu  =>  T2 = nu (3 PPT - Ph^2 gT)/(2 (Ph^2)^2),  T1 = (PPT - Ph^2 gT)/(2 Ph^2)
     (D = 4, symbolic, generic complex q) ; transversality of both structures.
 (c) Euclidean segment: q = (i q4, qvec), Q^2 = q4^2 + |qvec|^2 : Ph^2 = M^2 |qvec|^2/Q^2 ; |qvec| >= Q/2 =>
     Ph^2 >= M^2/4 and |omega| <= sqrt(3) M/Q ; every point of I_Q is attained.
 (d) removable point Ph^2 = 0 (q = (iQ, 0)): with T^{ij} = a delta + b q^i q^j, T^{0i} = c q^i, T^{00} = e and
     transversality, the projector formula equals T2 = (q^2)^2 (b - a/q^2)/nu identically (=> regular at qvec -> 0).
 (e) slice geometry: q(w) = (w,0,0,s), s^2 = w^2 + Q^2, Re s > 0, Im w > 0  =>  Im q in V+ and
     (Im w - |Im s|) >= Im w * Q^2 / (2 (|w|^2 + Q^2))   [Delta(Im q) = (Im w - |Im s|)/sqrt 2].
 (f) dispersion relation with subtractions for a test structure function (elastic point + continuum):
     T2(omega) = sum_{n<n0} t_n omega^{n-1} + 4 omega^{n0-1} int x^{n0-2} F2/(1 - x^2 omega^2)  and the jump
     T2(omega+i0) - T2(omega-i0) = 4 pi i F2(1/omega) (as densities in omega, omega > 1).
 (g) descending identity (low moments): for the order-k dispersion relation,
     T2(iy)/(iy) = sum_{n<k-2} t_n (iy)^{n-2} + (iy)^{k-4} [ t_{k-2} - 4 int x^{k-4} F2 x^2y^2/(1+x^2y^2) ].
 (h) coefficient inequality on the segment (Lemma 3.7): for odd polynomials of degree <= Dg, |h_k| r^k <= c_Dg sup_{|y|<=r}|h(iy)|
     with c_Dg <= 2 (1+sqrt2)^Dg (V.A. Markov / Chebyshev bound) -- numerically extremal ratios.
 (i) upper bound of the projector coefficient on I_Q: |nu/(Ph^2)^2| * |P-type tensors| <= C Q/M.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
import mpmath as mp
from numpy.polynomial import chebyshev as C

rng = np.random.default_rng(12345)
ok_all = True

# ---------------- (a) Jensen
def J_num(y):
    # split the circle at the (integrable) logarithmic singularities sin(th) = -y/2
    y = mp.mpf(y)
    pts = [mp.mpf(0), 2 * mp.pi]
    if abs(y) <= 2:
        th0 = mp.asin(-y / 2)
        for t in (th0, mp.pi - th0):
            t = t % (2 * mp.pi)
            pts.append(t)
    pts = sorted(set(pts))
    f = lambda th: mp.log(abs(y + 2 * mp.sin(th)) + mp.mpf(10) ** (-60))
    return mp.quad(f, pts) / (2 * mp.pi)

def J_jensen(y):
    w = np.roots([1, 1j * y, -1])
    return max(0.0, max(np.log(abs(w))))

maxdev = 0
for y in [0.0, 0.5, 1.9, 2.0, 2.5, 4.0, 10.0, -3.3, 37.0]:
    jn, jj = float(J_num(y)), J_jensen(y)
    maxdev = max(maxdev, abs(jn - jj))
    if jn < -1e-7:   # J = 0 exactly for |y| <= 2; quadrature noise ~1e-9
        ok_all = False
print("(a) Jensen J(y): max |numeric - Jensen| = %.2e ; J(y) >= 0 at all test points: %s ; J(1.9) = %.2e, J(10) = %.6f"
      % (maxdev, ok_all, J_jensen(1.9), J_jensen(10.0)))

# ---------------- (b) projector identities (D = 4)
g = sp.diag(1, -1, -1, -1)
q = sp.Matrix(sp.symbols('q0:4'))
Pv = sp.Matrix(sp.symbols('P0:4'))
T1, T2 = sp.symbols('T1 T2')
def dot(a, b):
    return (a.T * g * b)[0]
q2, nu, P2 = dot(q, q), dot(Pv, q), dot(Pv, Pv)
gup = g.inv()
gt = gup - q * q.T / q2
Ph = Pv - nu / q2 * q
Ph2 = sp.simplify(dot(Ph, Ph))
Tmn = -gt * T1 + Ph * Ph.T * T2 / nu
lower = lambda v: g * v
PPT = sp.simplify((lower(Pv).T * Tmn * lower(Pv))[0])
gT = sp.simplify(sum(g[i, j] * Tmn[i, j] for i in range(4) for j in range(4)))
T2rec = sp.simplify(nu * (3 * PPT - Ph2 * gT) / (2 * Ph2 ** 2))
T1rec = sp.simplify((PPT - Ph2 * gT) / (2 * Ph2))
transv = sp.simplify((lower(q).T * Tmn)).applyfunc(sp.simplify)
print("(b) T2 reconstructed - T2 =", sp.simplify(T2rec - T2), "; T1 reconstructed - T1 =", sp.simplify(T1rec - T1),
      "; q_mu T^{mu nu} = 0:", all(x == 0 for x in transv))

# ---------------- (c) Euclidean segment
M, Qs = 0.938, 7.0
worst_P, worst_om = 1e9, 0
for _ in range(20000):
    qvn = rng.uniform(Qs / 2, Qs)
    q4 = np.sqrt(Qs ** 2 - qvn ** 2) * rng.choice([-1, 1])
    nu_ = 1j * M * q4
    Ph2_ = M ** 2 - nu_ ** 2 / (-Qs ** 2)
    om = 2 * nu_ / Qs ** 2
    worst_P = min(worst_P, Ph2_.real / M ** 2)
    worst_om = max(worst_om, abs(om) / (np.sqrt(3) * M / Qs))
print("(c) Euclidean segment: min Ph^2/M^2 = %.4f (>= 1/4) ; max |omega|/(sqrt3 M/Q) = %.4f (<= 1)" % (worst_P, worst_om))

# ---------------- (d) removable point P-hat^2 = 0 : rest frame, general qvec, decomposition a,b,c,e
a_, b_, c_, Mm, w0 = sp.symbols('a b c M w0')
qx, qy, qz = sp.symbols('qx qy qz')
qq = sp.Matrix([w0, qx, qy, qz])
zeta = qx ** 2 + qy ** 2 + qz ** 2
e_ = c_ * zeta / w0                                   # transversality, nu = 0 component
a_sol = w0 * c_ - b_ * zeta                           # transversality, nu = j components: w0 c = a + b zeta
Tm = sp.zeros(4, 4)
qv = [qx, qy, qz]
Tm[0, 0] = e_
for i in range(3):
    Tm[0, i + 1] = c_ * qv[i]
    Tm[i + 1, 0] = c_ * qv[i]
    for j in range(3):
        Tm[i + 1, j + 1] = (a_sol if i == j else 0) + b_ * qv[i] * qv[j]
Prest = sp.Matrix([Mm, 0, 0, 0])
q2r = dot(qq, qq)
nur = dot(Prest, qq)
Phr = Prest - nur / q2r * qq
Ph2r = sp.simplify(dot(Phr, Phr))
PPTr = (lower(Prest).T * Tm * lower(Prest))[0]
gTr = sum(g[i, j] * Tm[i, j] for i in range(4) for j in range(4))
T2r = sp.simplify(nur * (3 * PPTr - Ph2r * gTr) / (2 * Ph2r ** 2))
claim = sp.simplify(q2r ** 2 * (b_ - a_sol / q2r) / nur)
transv_r = (lower(qq).T * Tm).applyfunc(sp.simplify)
print("(d) projector T2 - (q^2)^2 (b - a/q^2)/nu =", sp.simplify(T2r - claim),
      "; transversality:", all(sp.simplify(x) == 0 for x in transv_r))

# ---------------- (e) slice geometry
worst = 1e9
viol = 0
for _ in range(50000):
    Qv = rng.uniform(0.1, 10)
    w = complex(rng.normal() * rng.uniform(0.01, 30), abs(rng.normal()) * rng.uniform(1e-4, 30))
    s = np.sqrt(w * w + Qv * Qv)
    if s.real < 0:
        s = -s
    lhs = w.imag - abs(s.imag)
    rhs = w.imag * Qv ** 2 / (2 * (abs(w) ** 2 + Qv ** 2))
    if lhs <= 0 or lhs < rhs * (1 - 1e-9):
        viol += 1
    worst = min(worst, lhs / rhs)
print("(e) slice geometry: violations = %d / 50000 ; min ratio (Im w - |Im s|)/bound = %.4f" % (viol, worst))

# ---------------- (f) dispersion relation for a test F2 (continuum x^0.3 (1-x)^3 plus elastic point c delta(1-x))
mp.mp.dps = 25
cel = mp.mpf('0.2')
F2c = lambda x: x ** mp.mpf('0.3') * (1 - x) ** 3
def mom(n):          # int_0^1 x^{n-2} F2 dx incl. elastic point
    return mp.quad(lambda x: x ** (n - 2) * F2c(x), [0, 1]) + cel
def T2_disp(om, n0):
    s = sum(4 * mom(n) * om ** (n - 1) for n in range(2, n0, 2))
    s += 4 * om ** (n0 - 1) * (mp.quad(lambda x: x ** (n0 - 2) * F2c(x) / (1 - x * x * om * om), [0, 1])
                               + cel / (1 - om * om))
    return s
def T2_full(om):     # unsubtracted form, valid here since int F2 < infinity
    return 4 * om * (mp.quad(lambda x: F2c(x) / (1 - x * x * om * om), [0, 1]) + cel / (1 - om * om))
om_test = mp.mpc('0.3', '0.4')
vals = [T2_disp(om_test, n0) for n0 in (2, 4, 6, 8)]
print("(f) subtracted dispersion relations n0=2,4,6,8 agree:", mp.nstr(max(abs(v - vals[0]) for v in vals), 3),
      "; vs unsubtracted:", mp.nstr(abs(vals[0] - T2_full(om_test)), 3))
# jump at omega = 1.7 (x0 = 1/1.7): compare (T2(om+i eta) - T2(om-i eta)) with 4 pi i F2(1/om)
om0 = mp.mpf('1.7')
eta = mp.mpf('1e-6')
def T2_cont(om):
    # continuum part only, principal-value-safe by splitting at x0
    x0 = 1 / om.real
    return 4 * om * mp.quad(lambda x: F2c(x) / (1 - x * x * om * om), [0, x0 - mp.mpf('0.05'), x0, x0 + mp.mpf('0.05'), 1])
jump = T2_cont(om0 + 1j * eta) - T2_cont(om0 - 1j * eta)
print("(f) jump/(4 pi i F2(1/omega)) at omega = 1.7 (eta = 1e-6):", mp.nstr(jump / (4j * mp.pi * F2c(1 / om0)), 8))

# ---------------- (g) descending identity
y, k = sp.symbols('y k', positive=True)
xs = sp.symbols('x', positive=True)
# check pointwise in x (integrand level): for even k, 4 (iy)^{k-2} x^{k-2}/(1+x^2y^2)  ==  (iy)^{k-4} * (-4 x^{k-4} x^2 y^2/(1+x^2y^2))
ok_g = True
for kk in [4, 6, 8, 10]:
    lhs = 4 * (sp.I * y) ** (kk - 2) * xs ** (kk - 2) / (1 + xs ** 2 * y ** 2)
    rhs = (sp.I * y) ** (kk - 4) * (-4 * xs ** (kk - 4) * xs ** 2 * y ** 2 / (1 + xs ** 2 * y ** 2))
    ok_g &= sp.simplify(lhs - rhs) == 0
print("(g) descending identity (integrand level, k = 4..10):", ok_g)

# ---------------- (h) coefficient inequality on the segment for odd polynomials
def max_coeff_ratio(Dg, trials=4000):
    worst = 0
    ks = list(range(1, Dg + 1, 2))
    tt = np.linspace(-1, 1, 801)
    for _ in range(trials):
        h = rng.normal(size=len(ks)) + 1j * rng.normal(size=len(ks))
        vals = sum(h[i] * (1j * tt) ** k for i, k in enumerate(ks))
        sup = np.max(np.abs(vals))
        worst = max(worst, np.max(np.abs(h)) / sup)
    return worst
for Dg in [1, 3, 5, 7, 9, 11]:
    cheb = np.max(np.abs(C.cheb2poly([0] * Dg + [1])))
    # sharpness: h(i r t) = T_Dg(t) has sup 1 on the segment and max|h_k| r^k = max |coeff of T_Dg|
    r = max_coeff_ratio(Dg)
    print("(h) Dg=%2d : random worst |h_k|/sup = %.3f ; Chebyshev max coeff = %.0f ; bound 2(1+sqrt2)^Dg = %.0f ; ok: %s"
          % (Dg, r, cheb, 2 * (1 + np.sqrt(2)) ** Dg, r <= 2 * cheb + 1e-9 and cheb <= (1 + np.sqrt(2)) ** Dg))

# ---------------- (i) projector size on I_Q: components of nu*Ph^m Ph^n/(Ph^2)^2 and nu*g/(Ph^2) for q Euclidean
worst = 0
for _ in range(20000):
    Qv = rng.uniform(3, 50)
    qvn = rng.uniform(Qv / 2, Qv)
    q4 = np.sqrt(Qv ** 2 - qvn ** 2)
    nu_ = 1j * M * q4
    Ph2_ = M ** 2 * qvn ** 2 / Qv ** 2
    # rest-frame components of Ph: Ph0 = -M zeta/q^2 with zeta = qvec^2 (complex q0 = i q4), |Phvec| = M |q0| |qvec|/Q^2
    Ph0 = M * qvn ** 2 / Qv ** 2
    Phs = M * q4 * qvn / Qv ** 2
    comp = abs(nu_) * max(Ph0, Phs) ** 2 / Ph2_ ** 2 + abs(nu_) / Ph2_
    worst = max(worst, comp / (Qv / M))
print("(i) max over I_Q of |projector components| / (Q/M) = %.3f  (bounded => C Q/M)" % worst)
