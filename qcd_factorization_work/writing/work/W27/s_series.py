#!/usr/bin/env python3
"""
W27 / Ch24 -- series identities and closed forms (writer re-derivations):
 (A) prop:front-sll-closed-form, ex:front-sll-first: from BNS eq.(14) and the singlet colour factor eq.(19)
     C_rn^(S) = sB 2^(8-r) pi^2 (4Nc)^n CF [ -J43 + 2 J2 (1-delta_r0) ],  J2 = J43/2 = DeltaY (forward),
     only r = 0 survives and sigma_n = -sB (8CF/pi) as^3 L^3 DY (-4w)^n n!/(2n+3)!.  The identity
     4^k k!/(2k+3)! = 1/(6 (k+1) (5/2)_k) proves the closed form FOR ALL n (not only n <= 8).
     Large-w behaviour: 2F2(1,1;2,5/2;-w) = Int_0^1 dt 1F1(1;5/2;-wt) ~ (3/2)(ln w - psi(3/2) + ...)/w.
 (B) ex:front-hgg-ldl: (3/2)_k = (2k+1)!/(4^k k!) and the LDL series = (L^2/2) 2F2(1,1;3/2,2;-CF as L^2/(8 pi)),
     with the NLO match.
 (C) ex:front-luxqed-pointlike: LUXqed master formula on a point-like Dirac fermion (G_E=G_M=1), fixed alpha.
 (D) prop:front-smallx-helicity: decimal values of the two intercepts from the closed forms quoted for
     Borden-Kovchegov (4/3^(1/3)) sqrt(Re[(-9+i sqrt111)^(1/3)]) and BER sqrt((17+sqrt97)/2).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

PASS = FAIL = 0
def check(name, ok, info=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(("[PASS] " if ok else "[FAIL] ") + name + (("  " + info) if info else ""))

# ---------------- (A) SLL tower, singlet exchange ----------------
a_s, L, Nc, CF, sB, DY, w = sp.symbols('alpha_s L N_c C_F sigma_B DeltaY w', positive=True)
k = sp.symbols('k', integer=True, nonnegative=True)
def C_S(r, n):
    J2 = DY; J43 = 2 * DY
    return sB * 2**(8 - r) * sp.pi**2 * (4 * Nc)**n * CF * (-J43 + 2 * J2 * (0 if r == 0 else 1))
def sigma_n(n):
    s = sum(sp.factorial(2 * r) / (4**r * sp.factorial(r)**2) * C_S(r, n) for r in range(n + 1))
    return (a_s / (4 * sp.pi))**(n + 3) * L**(2 * n + 3) * (-4)**n * sp.factorial(n) / sp.factorial(2 * n + 3) * s
check("(A1) forward singlet: C_rn = -sB 2^9 pi^2 (4Nc)^n CF DY delta_r0",
      all(sp.simplify(C_S(r, n) - (-sB * 2**9 * sp.pi**2 * (4 * Nc)**n * CF * DY if r == 0 else 0)) == 0
          for n in range(6) for r in range(n + 1)))
wdef = Nc * a_s * L**2 / sp.pi
check("(A2) sigma_n = -sB (8CF/pi) as^3 L^3 DY (-4w)^n n!/(2n+3)!  (n = 0..12)",
      all(sp.simplify(sigma_n(n) - (-sB * 8 * CF / sp.pi * a_s**3 * L**3 * DY * (-4 * wdef)**n
                                    * sp.factorial(n) / sp.factorial(2 * n + 3))) == 0 for n in range(13)))
# general-k identity via Legendre duplication: (2k+3)! = 3*2^(2k+1) (k+1)! (5/2)_k
lhs = sp.gamma(2 * k + 4)
rhs = 3 * 2**(2 * k + 1) * sp.gamma(k + 2) * sp.rf(sp.Rational(5, 2), k)
ratio = sp.simplify(sp.gammasimp(sp.combsimp(lhs / rhs).rewrite(sp.gamma)))
check("(A3) (2k+3)! = 3 2^(2k+1) (k+1)! (5/2)_k for ALL k (Legendre duplication)", sp.simplify(ratio - 1) == 0,
      f"ratio = {ratio}")
check("(A3') numerical spot checks k=0..30",
      all(sp.factorial(2 * j + 3) == 3 * 2**(2 * j + 1) * sp.factorial(j + 1) * sp.rf(sp.Rational(5, 2), j) for j in range(31)))
# => Sum_n (-4w)^n n!/(2n+3)! = (1/6) Sum_n (-w)^n/((n+1)(5/2)_n) = (1/6) 2F2(1,1;2,5/2;-w)
term_ok = all(sp.simplify((-4 * w)**j * sp.factorial(j) / sp.factorial(2 * j + 3)
                          - sp.Rational(1, 6) * (-w)**j / ((j + 1) * sp.rf(sp.Rational(5, 2), j))) == 0 for j in range(20))
check("(A4) term-by-term: (-4w)^n n!/(2n+3)! = (1/6)(-w)^n/((n+1)(5/2)_n)", term_ok)
check("(A5) 2F2(1,1;2,5/2;-w) Pochhammer form: (1)_n(1)_n/((2)_n(5/2)_n n!) = 1/((n+1)(5/2)_n)",
      all(sp.simplify(sp.rf(1, j)**2 / (sp.rf(2, j) * sp.rf(sp.Rational(5, 2), j) * sp.factorial(j))
                      - 1 / ((j + 1) * sp.rf(sp.Rational(5, 2), j))) == 0 for j in range(20)))
s1 = sp.simplify(sigma_n(1)); s0 = sp.simplify(sigma_n(0))
check("(A6) first SLL (n=1): sB (4/(15 pi^2)) CF Nc as^4 L^5 DY",
      sp.simplify(s1 - sB * sp.Rational(4, 15) * CF * Nc * a_s**4 * L**5 * DY / sp.pi**2) == 0, f"{s1}")
check("(A7) n=0 term: -sB (4CF/(3pi)) as^3 L^3 DY (single-logarithmic)",
      sp.simplify(s0 + sB * sp.Rational(4, 3) * CF / sp.pi * a_s**3 * L**3 * DY) == 0, f"{s0}")
check("(A8) series 2F2 = 1 - w/5 + 4w^2/105 - ...",
      sp.simplify(sum((-w)**j / ((j + 1) * sp.rf(sp.Rational(5, 2), j)) for j in range(3)) - (1 - w / 5 + 4 * w**2 / 105)) == 0)
mp.mp.dps = 40
F = lambda x: mp.hyp2f2(1, 1, 2, mp.mpf(5) / 2, -x)
# integral representation 2F2 = Int_0^1 1F1(1;5/2;-x t) dt
for x in [mp.mpf('0.7'), mp.mpf(3), mp.mpf(25)]:
    iv = mp.quad(lambda t: mp.hyp1f1(1, mp.mpf(5) / 2, -x * t), [0, 1])
    check(f"(A9) 2F2(1,1;2,5/2;-w) = Int_0^1 1F1(1;5/2;-wt) dt at w={mp.nstr(x,3)}", abs(iv - F(x)) < 1e-25)
for x in [mp.mpf(10)**2, mp.mpf(10)**4, mp.mpf(10)**8]:
    r1 = F(x) * x / mp.log(x)
    r2 = F(x) * x / (mp.mpf(3) / 2 * (mp.log(x) - mp.digamma(mp.mpf(3) / 2)))
    print(f"   info: w={mp.nstr(x,3)}: w F/ln w = {mp.nstr(r1, 6)};  F / [(3/2)(ln w - psi(3/2))/w] = {mp.nstr(r2, 8)}")
check("(A10) w*2F2/ln w = 1.497 at w=1e8 (-> 3/2)", abs(F(mp.mpf(10)**8) * mp.mpf(10)**8 / mp.log(mp.mpf(10)**8) - mp.mpf('1.497')) < 5e-4)
check("(A11) refined asymptotics 2F2 ~ (3/2)(ln w - psi(3/2))/w  (ratio -> 1 at w=1e8 within 1e-6)",
      abs(F(mp.mpf(10)**8) * mp.mpf(10)**8 / (mp.mpf(3) / 2 * (mp.log(mp.mpf(10)**8) - mp.digamma(mp.mpf(3) / 2))) - 1) < 1e-6)
print(f"   info: psi(3/2) = {mp.nstr(mp.digamma(mp.mpf(3)/2), 10)} = 2 - gamma_E - 2 ln 2 = {mp.nstr(2-mp.euler-2*mp.log(2),10)}")
# ---------------- (B) LDL series of h -> gamma gamma (b loop) ----------------
Lh = sp.symbols('Lhat', positive=True)
check("(B1) (3/2)_k = (2k+1)!/(4^k k!)  (k=0..30)",
      all(sp.rf(sp.Rational(3, 2), j) == sp.factorial(2 * j + 1) / (4**j * sp.factorial(j)) for j in range(31)))
lhs_t = lambda n: Lh**2 * sp.factorial(n) / sp.factorial(2 * n + 2) * (-CF * a_s * Lh**2 / (2 * sp.pi))**n
rhs_t = lambda n: Lh**2 / 2 * sp.rf(1, n)**2 / (sp.rf(sp.Rational(3, 2), n) * sp.rf(2, n) * sp.factorial(n)) \
                  * (-CF * a_s * Lh**2 / (8 * sp.pi))**n
check("(B2) Lh^2 sum n!/(2n+2)! (-CF as Lh^2/2pi)^n = (Lh^2/2) 2F2(1,1;3/2,2;-CF as Lh^2/8pi)  (n=0..20)",
      all(sp.simplify(lhs_t(n) - rhs_t(n)) == 0 for n in range(21)))
check("(B3) coefficient identity (1/2) k!/((3/2)_k (k+1)!) 4^(-k) = k!/(2k+2)!",
      all(sp.simplify(sp.Rational(1, 2) * sp.factorial(j) / (sp.rf(sp.Rational(3, 2), j) * sp.factorial(j + 1)) / 4**j
                      - sp.factorial(j) / sp.factorial(2 * j + 2)) == 0 for j in range(25)))
check("(B4) n=0: Lh^2/2;  n=1: -(CF as/(48 pi)) Lh^4 = (CF as/4pi)(-Lh^4/12)",
      sp.simplify(lhs_t(0) - Lh**2 / 2) == 0 and sp.simplify(lhs_t(1) - CF * a_s / (4 * sp.pi) * (-Lh**4 / 12)) == 0)
# ---------------- (C) LUXqed point-like limit ----------------
x, z, Q2, mu2, m2, al = sp.symbols('x z Q2 mu2 m2 alpha', positive=True)
# F2(x/z) = delta(1 - x/z) = x delta(z - x) ; the z-integral Int dz/z [...] then sets z = x with weight (1/x)*x = 1
zp = 1 + (1 - x)**2                                  # z p_{gamma q}(z) at z = x
F2c = 1                                              # coefficient of the delta function after the z integral
FLc = 4 * m2 / Q2                                    # F_L = (G_E^2/tau) delta, tau = Q2/(4 m2)
Qmin = x**2 * m2 / (1 - x); Qmax = mu2 / (1 - x)
inner = sp.integrate(((zp + 2 * x**2 * m2 / Q2) * F2c - x**2 * FLc) / Q2, (Q2, Qmin, Qmax))
xf = sp.simplify(1 / (2 * sp.pi * al) * (al**2 * inner - al**2 * x**2 * F2c))
target = al / (2 * sp.pi) * (1 + (1 - x)**2) * (sp.log(mu2 / m2) - 2 * sp.log(x) - 1) + al * m2 * x**2 * (1 - x) / (sp.pi * mu2)
check("(C1) LUXqed (G_E=G_M=1, fixed alpha): x f = (alpha/2pi)[1+(1-x)^2][ln(mu^2/m^2) - 2ln x - 1] + alpha m^2 x^2(1-x)/(pi mu^2)",
      sp.simplify(sp.expand_log(xf - target, force=True)) == 0)
inner_noFL = sp.integrate(((zp + 2 * x**2 * m2 / Q2) * F2c) / Q2, (Q2, Qmin, Qmax))
xf_noFL = sp.simplify(1 / (2 * sp.pi * al) * (al**2 * inner_noFL - al**2 * x**2 * F2c))
d1 = sp.simplify(sp.expand_log(xf_noFL - xf, force=True))
check("(C2) dropping F_L: shift by (alpha/2pi) 4(1-x) (leading power) ",
      sp.simplify(sp.series(d1, m2, 0, 1).removeO() - al / (2 * sp.pi) * 4 * (1 - x)) == 0, f"shift = {sp.factor(d1)}")
xf_noconv = sp.simplify(1 / (2 * sp.pi * al) * (al**2 * inner))
d2 = sp.simplify(xf_noconv - xf)
check("(C3) dropping the MS-bar conversion term: shift by (alpha/2pi) x^2", sp.simplify(d2 - al / (2 * sp.pi) * x**2) == 0)
# the identity -2(1-x) - x^2 = -[1 + (1-x)^2] used in the text
check("(C4) -2(1-x) - x^2 = -[1+(1-x)^2]", sp.expand(-2 * (1 - x) - x**2 + 1 + (1 - x)**2) == 0)
# delta-function weight: Int_x^1 dz/z x delta(z-x) g(z) = g(x)
check("(C5) delta(1 - x/z) = x delta(z - x)  (|d/dz (1-x/z)| = x/z^2 = 1/x at z = x)",
      sp.simplify(sp.diff(1 - x / z, z).subs(z, x) - 1 / x) == 0)
# ---------------- (D) small-x helicity intercepts ----------------
mp.mp.dps = 30
c = mp.cbrt(mp.mpc(-9, mp.sqrt(111)))   # principal cube root
aBK = 4 / mp.cbrt(3) * mp.sqrt(mp.re(c))
aBER = mp.sqrt((17 + mp.sqrt(97)) / 2)
check("(D1) Borden-Kovchegov closed form -> 3.66074", abs(aBK - mp.mpf('3.66074')) < 5e-6, f"{mp.nstr(aBK, 10)}")
check("(D2) BER closed form -> 3.66394", abs(aBER - mp.mpf('3.66394')) < 5e-6, f"{mp.nstr(aBER, 10)}")
print(f"   info: relative difference (BER - BK)/BK = {mp.nstr((aBER - aBK)/aBK, 4)}")
print(f"\nTOTAL: {PASS} PASS, {FAIL} FAIL")
