#!/usr/bin/env python3
"""W24 / Ch21 -- Borel transform basics (def:power-borel, lem:power-borel-pole), Adler u=2 ambiguity,
pole-mass u=1/2 renormalon from the static self-energy, Liu-Su normalisation.

Conventions: R = sum_n r_n alpha^{n+1}, B[R](t) = sum_n r_n t^n/n!, u = beta0 t/(4 pi),
mu^2 d alpha/d mu^2 = -beta0/(4 pi) alpha^2 (one loop), alpha(mu) = 4 pi/(beta0 ln(mu^2/Lambda^2)).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

OK = True
def check(name, cond):
    global OK
    print(("PASS " if cond else "FAIL ") + name)
    OK = OK and bool(cond)

t, al, u, b0, mu, Lam, K, u0 = sp.symbols('t alpha u beta0 mu Lambda K u0', positive=True)
n = sp.symbols('n', integer=True, nonnegative=True)

# (1) termwise Borel integral
check("(1) int_0^oo dt e^{-t/alpha} t^n/n! = alpha^{n+1} (n=0..6)",
      all(sp.simplify(sp.integrate(sp.exp(-t/al)*t**k/sp.factorial(k), (t, 0, sp.oo)) - al**(k+1)) == 0 for k in range(7)))

# (2) one loop: exp(-t/alpha(mu)) = (Lambda^2/mu^2)^u
alpha_mu = 4*sp.pi/(b0*sp.log(mu**2/Lam**2))
expr = sp.expand_log(sp.log(sp.exp(-t/alpha_mu)) - (b0*t/(4*sp.pi))*sp.log(Lam**2/mu**2), force=True)
check("(2) exp(-t/alpha(mu)) = (Lambda^2/mu^2)^u with u = beta0 t/(4pi)", sp.simplify(expr) == 0)

# (3) pole of order m+1 at u0: B = K/(u0-u)^{m+1} -> b_n = K u0^{-1-m-n} binom(n+m,m); r_n = n! (beta0/4pi)^n b_n
uu = sp.symbols('uu')
for m in [0, 1]:
    B = K/(u0 - uu)**(m+1)
    ser = sp.series(B, uu, 0, 8).removeO()
    okm = all(sp.simplify(ser.coeff(uu, k) - K*u0**(-1-m-k)*sp.binomial(k+m, m)) == 0 for k in range(8))
    check(f"(3) Taylor coefficients of K/(u0-u)^{m+1} are K u0^(-1-{m}-n) binom(n+{m},{m})", okm)
# asymptotic form r_n ~ K n! n^m (beta0/(4 pi u0))^n / (m! u0^{1+m})
for m in [0, 1]:
    rat = [mp.binomial(N+m, m)/(mp.mpf(N)**m/mp.factorial(m)) for N in [10, 100, 1000, 10000]]
    print(f"   m={m}: binom(n+m,m)/(n^m/m!) for n=10..10^4:", [mp.nstr(x, 8) for x in rat])
    check(f"(3') binom(n+{m},{m}) ~ n^{m}/{m}! (ratio -> 1)", abs(rat[-1] - 1) < 2e-4)

# (4) ambiguity: R_pm = (4pi/beta0) int_0^oo du e^{-4 pi u/(beta0 alpha)} B(u pm i0); simple pole
#     R_+ - R_- = 2 pi i K (4 pi/beta0) e^{-4 pi u0/(beta0 alpha)}  (contour above minus below = clockwise loop)
mp.mp.dps = 30
b0v, alv, Kv, u0v = mp.mpf(9), mp.mpf('0.35'), mp.mpf('1.7'), mp.mpf(2)
w = 4*mp.pi/(b0v*alv)
Bf = lambda z: Kv*mp.exp(-z/3)/(u0v - z)        # extra decaying factor e^{-u/3}
def R(sign, eta=mp.mpf('0.25')):
    # path: 0 -> i*sign*eta -> (L + i sign eta) -> L (L large); integrand analytic off the real axis near u0
    L = mp.mpf(60)
    f = lambda z: (4*mp.pi/b0v)*mp.exp(-w*z)*Bf(z)
    p1 = mp.quad(lambda s: f(1j*sign*s)*1j*sign, [0, eta])
    p2 = mp.quad(lambda x: f(x + 1j*sign*eta), [0, u0v, L])
    p3 = mp.quad(lambda s: f(L + 1j*sign*(eta - s))*(-1j*sign), [0, eta])
    return p1 + p2 + p3
diff = R(+1) - R(-1)
pred = 2j*mp.pi*Kv*mp.exp(-u0v/3)*(4*mp.pi/b0v)*mp.exp(-w*u0v)
print("   R_+ - R_- =", mp.nstr(diff, 15), " predicted:", mp.nstr(pred, 15))
check("(4) simple pole: R_+ - R_- = 2 pi i (4pi/beta0) Res-coefficient e^{-4 pi u0/(beta0 alpha)}", abs(diff - pred) < 1e-20)
# double pole: B = K/(u0-u)^2 * e^{-u/3}: difference = 2 pi i (4pi/beta0) d/du [-(e^{-w u} e^{-u/3}) K] ... computed directly
Bf2 = lambda z: Kv*mp.exp(-z/3)/(u0v - z)**2
def R2(sign, eta=mp.mpf('0.25')):
    L = mp.mpf(60)
    f = lambda z: (4*mp.pi/b0v)*mp.exp(-w*z)*Bf2(z)
    p1 = mp.quad(lambda s: f(1j*sign*s)*1j*sign, [0, eta])
    p2 = mp.quad(lambda x: f(x + 1j*sign*eta), [0, u0v, L])
    p3 = mp.quad(lambda s: f(L + 1j*sign*(eta - s))*(-1j*sign), [0, eta])
    return p1 + p2 + p3
diff2 = R2(+1) - R2(-1)
# clockwise loop: -2 pi i Res[ (4pi/b0) e^{-wz} K e^{-z/3}/(z-u0)^2 ] = -2 pi i (4pi/b0) K d/dz[e^{-(w+1/3) z}]_{u0}
pred2 = -2j*mp.pi*(4*mp.pi/b0v)*Kv*(-(w + mp.mpf(1)/3))*mp.exp(-(w + mp.mpf(1)/3)*u0v)
print("   double pole: R_+ - R_- =", mp.nstr(diff2, 15), " predicted:", mp.nstr(pred2, 15))
check("(5) double pole: difference carries the extra factor 4pi/(beta0 alpha) (+1/3 from the test factor)", abs(diff2 - pred2) < 1e-20)

# (6) Adler function, large beta0, u=2 pole: B[D/R0-1] = (3 C_F/4pi) Bhat, Bhat ~ 2 e^{10/3}/(2-u) (mu=Q)
CF = sp.Rational(4, 3)
Im_over_pi = (4*sp.pi/b0)*(3*CF/(4*sp.pi))*2*sp.exp(sp.Rational(10, 3))  # times (Lambda/Q)^4
print("   Im(D/R0)/pi from u=2 =", sp.simplify(Im_over_pi), "* Lambda^4/Q^4  (= 6 C_F e^{10/3}/beta0 for general C_F)")
for nfv, Lv in [(3, 0.215)]:
    val = float(Im_over_pi.subs(b0, 11 - sp.Rational(2, 3)*nfv))*Lv**4
    print(f"   n_f={nfv}, Lambda={Lv} GeV: {val:.4f} GeV^4/Q^4   [Beneke 1999 eq. (5.12): same expression, ~0.06 GeV^4/Q^4]")
    dG2 = val*3/(2*float(sp.pi)**2)
    print(f"   corresponding shift of <(alpha_s/pi) G^2> = Im/pi / (2 pi^2/N_c) = {dG2:.5f} GeV^4  (Beneke (5.13): condensate term 0.08 GeV^4/Q^4)")
    check("(6) ambiguity estimate 0.053 GeV^4/Q^4 and condensate shift 0.0081 GeV^4", abs(val - 0.0532) < 5e-4 and abs(dG2 - 0.00809) < 1e-4)
# Beneke's form: (2/|beta0_B|) e^{10/3} Lambda^4/(pi Q^4), beta0_B = -beta0/(4 pi)
ben = 2*(4*sp.pi/b0)*sp.exp(sp.Rational(10, 3))/sp.pi
check("(6') identical to Beneke (5.12): -(2/beta0_B) e^{10/3}/pi with beta0_B = -beta0/(4pi), C_F = 4/3", sp.simplify(ben - Im_over_pi) == 0)

# (7) pole mass: IR part of the static self-energy, dm = (1/2) int d^3k/(2pi)^3 4 pi C_F alpha(k)/k^2 = (C_F/pi) int dk alpha(k)
kk, CFs = sp.symbols('k C_F', positive=True)
radial = sp.Rational(1, 2)*(4*sp.pi*CFs)/(2*sp.pi)**3*4*sp.pi   # (1/2)*4piC_F/(2pi)^3 * 4pi k^2 dk / k^2
check("(7a) static self-energy: (1/2) int d^3k/(2pi)^3 4 pi C_F alpha/k^2 = (C_F/pi) int dk alpha", sp.simplify(radial - CFs/sp.pi) == 0)
# large beta0: alpha(k^2 e^{-5/3}) -> Borel kernel (k^2 e^{-5/3}/mu^2)^{-u}; IR part int_0^{k0} dk k^{-2u} = k0^{1-2u}/(1-2u)
# near u=1/2: B[dm] ~ (C_F/pi) mu e^{5/6} /(1-2u) = (C_F e^{5/6} mu/(2 pi)) /(1/2-u)
Kpm = CFs*sp.exp(sp.Rational(5, 6))*mu/(2*sp.pi)
# large order: r_n = (K/u0) n! (beta0/(4 pi u0))^n with u0=1/2 -> (C_F e^{5/6} mu/pi) n! (beta0/(2 pi))^n  [Beneke (5.84)]
check("(7b) large-order r_n = (C_F e^{5/6}/pi) mu (beta0/(2pi))^n n!  [Beneke 1999 eq. (5.84), -2 beta0_B = beta0/(2pi)]",
      sp.simplify(Kpm/sp.Rational(1, 2) - CFs*sp.exp(sp.Rational(5, 6))*mu/sp.pi) == 0)
amb = (4*sp.pi/b0)*Kpm*sp.sqrt(Lam**2/mu**2)    # Im/pi = (4pi/beta0) K (Lambda^2/mu^2)^{1/2}
check("(7c) ambiguity Im/pi = (2 C_F/beta0) e^{5/6} Lambda", sp.simplify(amb - 2*CFs/b0*sp.exp(sp.Rational(5, 6))*Lam) == 0)
print("   N_m = C_F e^{5/6}/pi (VF-YZL-11) =", sp.N(sp.Rational(4, 3)*sp.exp(sp.Rational(5, 6))/sp.pi, 5))

# (8) Liu-Su normalisation (WRITER_SPEC row 45(b)): beta0^(b) = beta0/(2pi); u_LS = beta0^(b) t/2 = beta0 t/(4pi) = u
check("(8) u_LS = beta0^(b) t/2 equals u = beta0 t/(4pi)", sp.simplify((b0/(2*sp.pi))*t/2 - b0*t/(4*sp.pi)) == 0)

# (9) e^{-c/alpha} is o(alpha^K) for every K (used in prop:power-rearrangement(b))
for Kp in [1, 5, 20]:
    lim = sp.limit(sp.exp(-1/al)/al**Kp, al, 0, '+')
    check(f"(9) lim_{{alpha->0+}} e^{{-1/alpha}}/alpha^{Kp} = 0", lim == 0)
print("ALL PASS" if OK else "SOME CHECKS FAILED")
