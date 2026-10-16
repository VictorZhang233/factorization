"""
e1_ee_checks.py -- checks for Part IV (e+e- total cross section and Adler function).

 (a) int_0^inf 2 t sin t /(t^2+b^2)^2 dt = (pi/2) e^{-b}/b                                   (Prop. 4.6)
 (b) R(s) = R0 [1 + kappa sin(sqrt(s)/Lambda)]  =>  D(Q^2) = Q^2 int R/(s+Q^2)^2 ds
                                                        = R0 [1 + kappa (pi/2)(Q/Lambda) e^{-Q/Lambda}]
 (c) Euclidean moments M_k = k Q^{2k} int R/(s+Q^2)^{k+1}:  M_1 = D,  M_{k+1} = M_k - (Q^2/k) dM_k/dQ^2 (checked from
     the definition for R = s^(1/3) in (c')),  and with
     D = R0(1 + d1 a + d2 a^2 + d3 a^3), Q^2 da/dQ^2 = -b0 a^2 - b1 a^3:
     M_k = R0 (1 + d1 a + (d2 + H_{k-1} b0 d1) a^2 + O(a^3)),  H_m = 1 + 1/2 + ... + 1/m        (Thm 4.5)
 (d) Cesaro mean of the oscillating model: (1/s) int_0^s R = R0[1 + 2 kappa (sin T - T cos T)/T^2], T = sqrt(s)/Lambda
     -> R0 (rate O(1/T))                                                                       (Thm 4.7 illustration)
 (e) PQW smearing for constant R0: (1/pi) int_0^inf R0 Delta/((s'-s)^2+Delta^2) ds' = R0 (1 - arctan(Delta/s)/pi)
     = 12 pi Im Pi(s + i Delta) with Pi = -(R0/12 pi^2) ln(-q^2/mu^2), and the sector contour formula
     Rbar = (1/2 pi i) int_C D(Q^2) dQ^2/Q^2 over the arc |Q^2| = |s+i Delta| from arg -(pi-th) to (pi-th).   (Thm 4.8)
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import sympy as sp

mp.mp.dps = 30

# (a)
for b in [0.5, 1.0, 3.0, 7.5]:
    num = mp.quadosc(lambda t: 2 * t * mp.sin(t) / (t * t + b * b) ** 2, [0, mp.inf], omega=1)
    print("(a) b = %4.1f : integral = %s ; (pi/2) e^{-b}/b = %s" % (b, mp.nstr(num, 15), mp.nstr(mp.pi / 2 * mp.e ** (-b) / b, 15)))

# (b)
R0, kap, Lam = mp.mpf(2), mp.mpf('0.6'), mp.mpf(1)
for Q in [2, 5, 10, 20]:
    Q = mp.mpf(Q)
    # substitute s = Lam^2 t^2 : ds = 2 Lam^2 t dt
    osc = mp.quadosc(lambda t: 2 * Lam ** 2 * t * mp.sin(t) / (Lam ** 2 * t * t + Q * Q) ** 2, [0, mp.inf], omega=1)
    D = R0 + kap * R0 * Q * Q * osc
    pred = R0 * (1 + kap * mp.pi / 2 * (Q / Lam) * mp.e ** (-Q / Lam))
    print("(b) Q = %5.1f : D(Q^2) = %s ; prediction = %s ; D - R0 = %s"
          % (Q, mp.nstr(D, 18), mp.nstr(pred, 18), mp.nstr(D - R0, 6)))

# (c)
a, Q2 = sp.symbols('a Q2', positive=True)
d1, d2, d3, b0, b1, R0s = sp.symbols('d1 d2 d3 b0 b1 R0')
af = sp.Function('af')
Dexpr = R0s * (1 + d1 * a + d2 * a ** 2 + d3 * a ** 3)
beta_a = -b0 * a ** 2 - b1 * a ** 3          # Q^2 da/dQ^2
def Q2d(expr):                                # Q^2 d/dQ^2 acting on functions of a (and explicit Q2-independence)
    return sp.expand(sp.diff(expr, a) * beta_a)
Mk = {1: Dexpr}
for kk in range(1, 6):
    Mk[kk + 1] = sp.expand(Mk[kk] - Q2d(Mk[kk]) / kk)
ok = True
for kk in range(1, 7):
    ser = sp.series(Mk[kk], a, 0, 3).removeO()
    Hm = sum(sp.Rational(1, j) for j in range(1, kk))
    pred = R0s * (1 + d1 * a + (d2 + Hm * b0 * d1) * a ** 2)
    good = sp.simplify(ser - pred) == 0
    ok &= good
    print("(c) M_%d = %s   [matches H_{k-1} formula: %s]" % (kk, sp.factor(sp.collect(ser / R0s, a)), good))
print("(c) all Euclidean-moment formulas verified:", ok)
# (c') independent check of the recursion M_{k+1} = M_k - (Q^2/k) dM_k/dQ^2 directly from the definition
#      M_k = k Q^{2k} int_0^inf R(s)/(s+Q^2)^{k+1} ds, for the test spectral function R = s^(1/3)
#      (closed form M_k = k Gamma(g+1) Gamma(k-g)/Gamma(k+1) (Q^2)^g, g = 1/3).   [revision: this block previously
#      only printed M_k and checked nothing]
s_, k_ = sp.symbols('s k', positive=True)
g0 = sp.Rational(1, 3)
Mdef = {}
for kk in [1, 2, 3, 4]:
    Mdef[kk] = sp.simplify(kk * Q2 ** kk * sp.integrate(s_ ** g0 / (s_ + Q2) ** (kk + 1), (s_, 0, sp.oo), conds='none'))
okc = True
for kk in [1, 2, 3]:
    print("(c') M_%d for R = s^(1/3): %s" % (kk, sp.simplify(Mdef[kk])))
    closed = kk * sp.gamma(g0 + 1) * sp.gamma(kk - g0) / sp.gamma(kk + 1) * Q2 ** g0
    rec = sp.simplify(Mdef[kk] - Q2 / kk * sp.diff(Mdef[kk], Q2))
    good_closed = sp.simplify(sp.gammasimp(Mdef[kk] - closed)) == 0
    good_rec = sp.simplify(sp.gammasimp(rec - Mdef[kk + 1])) == 0
    okc &= good_closed and good_rec
    print("(c')     closed form k Gamma(g+1)Gamma(k-g)/Gamma(k+1) Q^(2g): %s ; recursion gives M_%d: %s"
          % (good_closed, kk + 1, good_rec))
print("(c') recursion verified from the definition for k = 1, 2, 3:", okc)

# (d)
for T in [10, 100, 1000, 10000]:
    T = mp.mpf(T)
    s = (Lam * T) ** 2
    exact = R0 * (1 + 2 * kap * (mp.sin(T) - T * mp.cos(T)) / T ** 2)
    num = (R0 * s + kap * R0 * 2 * Lam ** 2 * mp.quad(lambda t: t * mp.sin(t), mp.linspace(0, T, int(T) // 3 + 2))) / s
    print("(d) T = sqrt(s)/Lambda = %6d : Cesaro mean = %s (closed form %s) ; deviation*T = %s"
          % (T, mp.nstr(num, 12), mp.nstr(exact, 12), mp.nstr((num - R0) * T, 6)))

# (e)
R0v = mp.mpf(1)
for (sv, Dl) in [(10, 1), (10, 10), (100, 30)]:
    sv, Dl = mp.mpf(sv), mp.mpf(Dl)
    smeared = mp.quad(lambda x: R0v * Dl / ((x - sv) ** 2 + Dl ** 2), [0, sv, mp.inf]) / mp.pi
    closed = R0v * (1 - mp.atan(Dl / sv) / mp.pi)
    Pi = lambda q2: -(R0v / (12 * mp.pi ** 2)) * mp.log(-q2)
    fromPi = 12 * mp.pi * mp.im(Pi(sv + 1j * Dl))
    th = mp.atan(Dl / sv)
    r = abs(sv + 1j * Dl)
    contour = mp.quad(lambda phi: R0v * 1j, [-(mp.pi - th), mp.pi - th]) / (2j * mp.pi)   # D = R0: dQ^2/Q^2 = i dphi
    print("(e) s=%5.1f Delta=%5.1f : smeared = %s ; R0(1-atan(D/s)/pi) = %s ; 12 pi Im Pi(s+iD) = %s ; contour = %s"
          % (sv, Dl, mp.nstr(smeared, 12), mp.nstr(closed, 12), mp.nstr(fromPi, 12), mp.nstr(mp.re(contour), 12)))
