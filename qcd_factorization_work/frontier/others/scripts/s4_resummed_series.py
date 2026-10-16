#!/usr/bin/env python3
"""
s4_resummed_series.py -- series identities quoted in OTHERS.md.

(A) Becher-Neubert-Shao, PRL 127 (2021) 212002 [arXiv:2107.01212]:
    Eq.(14): sigma_n^SLL = (as/4pi)^(n+3) L^(2n+3) (-4)^n n!/(2n+3)! sum_{r=0}^n (2r)!/(4^r r!^2) C_rn
    Eq.(19): singlet  C_rn^(S) = sigma_B 2^(8-r) pi^2 (4Nc)^n CF [ -J43 + 2 J2 (1-delta_r0) ],
             forward scattering J2 = J43/2 = DeltaY.
    Claim Eq.(21): sum_n sigma_n^SLL = - sigma_B (4 CF/(3 pi)) as^3 L^3 DeltaY 2F2(1,1;2,5/2;-w),
             w = Nc as L^2/pi ;  and f(w) ~ (ln w)/w at large w.
(B) Liu-Neubert, JHEP 04 (2020) 033 [arXiv:1912.08818], Eq.(3) (LDL series of the b-quark induced
    h->gamma gamma amplitude, Kotsky-Yakovlev / Akhoury-Wang-Zakharov):
    M_b|LDL = M0 Lh^2 sum_n n!/(2n+2)! (-CF as Lh^2/(2pi))^n = M0 (Lh^2/2) 2F2(1,1;3/2,2;-CF as Lh^2/(8pi)),
    and the n=1 term must match the -L^4/12 term of the NLO amplitude, Eq.(1).
Run: python3 -I s4_resummed_series.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

PASS = FAIL = 0
def check(name, ok, info=""):
    global PASS, FAIL
    if ok: PASS += 1
    else:  FAIL += 1
    print(("[PASS] " if ok else "[FAIL] ") + name + ("  " + info if info else ""))

a_s, L, Nc, CF, sB, DY = sp.symbols('alpha_s L N_c C_F sigma_B DeltaY', positive=True)
n, r = sp.symbols('n r', integer=True, nonnegative=True)

def C_S(rr, nn):
    J2 = DY; J43 = 2 * DY
    return sB * 2**(8 - rr) * sp.pi**2 * (4 * Nc)**nn * CF * (-J43 + 2 * J2 * (1 if rr > 0 else 0))

def sigma_n(nn):
    s = sum(sp.factorial(2 * rr) / (4**rr * sp.factorial(rr)**2) * C_S(rr, nn) for rr in range(nn + 1))
    return (a_s / (4 * sp.pi))**(nn + 3) * L**(2 * nn + 3) * (-4)**nn * sp.factorial(nn) / sp.factorial(2 * nn + 3) * s

w = Nc * a_s * L**2 / sp.pi
closed_term = lambda nn: -sB * sp.Rational(4, 3) * CF / sp.pi * a_s**3 * L**3 * DY * \
    (sp.rf(1, nn) * sp.rf(1, nn) / (sp.rf(2, nn) * sp.rf(sp.Rational(5, 2), nn))) * (-w)**nn / sp.factorial(nn)
ok = all(sp.simplify(sigma_n(k) - closed_term(k)) == 0 for k in range(0, 9))
check("BNS (14)+(19) term by term = -sigma_B (4CF/3pi) as^3 L^3 DY 2F2(1,1;2,5/2;-w), n = 0..8 (Eq. 21)", ok)
s1 = sp.simplify(sigma_n(1))
check("first super-leading term (n=1): sigma_B (4/15) CF Nc as^4 L^5 DeltaY / pi^2",
      sp.simplify(s1 - sB * sp.Rational(4, 15) * CF * Nc * a_s**4 * L**5 * DY / sp.pi**2) == 0, f"sigma_1 = {s1}")
s0 = sp.simplify(sigma_n(0))
check("n=0 term is single-logarithmic (as^3 L^3): not super-leading", sp.simplify(s0 / (a_s**3 * L**3)).has(L) is False,
      f"sigma_0 = {s0}")
# numerical check of the resummed function and its asymptotics
mp.mp.dps = 30
F = lambda ww: mp.hyp2f2(1, 1, 2, mp.mpf(5) / 2, -ww)
partial = lambda ww, N: mp.nsum(lambda k: (mp.rf(1, k)**2 / (mp.rf(2, k) * mp.rf(mp.mpf(5) / 2, k))) * (-ww)**k / mp.factorial(k), [0, N])
check("2F2(1,1;2,5/2;-w) series vs mpmath at w = 3", abs(partial(3, 80) - F(3)) < 1e-20)
ratios = [(ww, F(ww) * ww / mp.log(ww)) for ww in [1e2, 1e4, 1e6, 1e8]]
check("large-w behaviour: w*2F2/ln w -> 3/2 (i.e. f(w) ~ ln w / w, much slower than Sudakov e^{-cw})",
      abs(ratios[-1][1] - 1.5) < 0.1, "ratios: " + ", ".join(f"w={float(a):.0e}: {float(b):.4f}" for a, b in ratios))

# (B) Liu-Neubert LDL series
Lh = sp.symbols('Lhat', positive=True)
aa = CF * a_s * Lh**2 / (2 * sp.pi)
lhs_term = lambda nn: Lh**2 * sp.factorial(nn) / sp.factorial(2 * nn + 2) * (-aa)**nn
zz = CF * a_s * Lh**2 / (8 * sp.pi)
rhs_term = lambda nn: Lh**2 / 2 * sp.rf(1, nn)**2 / (sp.rf(sp.Rational(3, 2), nn) * sp.rf(2, nn)) * (-zz)**nn / sp.factorial(nn)
check("Liu-Neubert Eq.(3): Lh^2 sum n!/(2n+2)! (-CF as Lh^2/2pi)^n = (Lh^2/2) 2F2(1,1;3/2,2;-CF as Lh^2/8pi), n=0..10",
      all(sp.simplify(lhs_term(k) - rhs_term(k)) == 0 for k in range(11)))
t1 = sp.simplify(lhs_term(1) / (CF * a_s / (4 * sp.pi)))
check("n=1 LDL term = (CF as/4pi) * (-Lh^4/12): matches the NLO amplitude Eq.(1)", sp.simplify(t1 + Lh**4 / 12) == 0,
      f"coefficient = {t1}")
t0 = sp.simplify(lhs_term(0))
check("n=0 LDL term = Lh^2/2 (matches the leading L^2/2 of Eq.(1))", sp.simplify(t0 - Lh**2 / 2) == 0)
print(f"\nTOTAL: {PASS} PASS, {FAIL} FAIL")
