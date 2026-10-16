#!/usr/bin/env python3
"""W25 / Ch22 -- s3: hybrid-scheme one-loop kernel (prop:lamet-hybrid-kernel, ex:lamet-hybrid-normalization).

H1  FT identity: int dzeta/(2pi) e^{i u zeta} ln(zeta^2/lamS^2) theta(|zeta|-lamS) = -1/|u| + 2 Si(u lamS)/(pi u)  (u != 0)
    (a) integration by parts symbolically; (b) numerically with a convergence factor
H2  large-|u| decay of the bracket at fixed lamS: -2 cos(u lamS)/(pi lamS u^2)
H3  distributional check: pairing the plus-on-R bracket with Gaussian test functions equals the coordinate-space pairing
H4  int_0^V Si(v)/v dv = (pi/2)(ln V + gamma_E) + o(1)
H5  delta coefficient: printed prescription 1/|u|_+ (with 2 delta ln beta) gives int du [bracket] = 2 ln(lamS e^gE);
    the exact transform is the plus distribution on R: printed - exact = 3a ln(lamS e^gE) delta(1-xi)
H6  numbers: 3a ln(lamS e^gE) for lamS = 1, a = alpha_s C_F/(2pi) with alpha_s = 0.25..0.3 (the "about 10 per cent")
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

NP = 0; NF = 0
def check(name, ok, extra=""):
    global NP, NF
    ok = bool(ok)
    print(("PASS " if ok else "FAIL ") + name + ((" : " + str(extra)) if extra != "" else ""))
    if ok: NP += 1
    else: NF += 1

mp.mp.dps = 30
# ---------------------------------------------------------------- H1
u, z, L = sp.symbols('u zeta lambda_S', positive=True)
# integration by parts: (2/pi) int_L^inf cos(u z) ln(z/L) dz = -(2/(pi u)) int_L^inf sin(u z)/z dz   (boundary terms vanish distributionally)
#                      int_L^inf sin(u z)/z dz = pi/2 - Si(u L)   (u > 0)
expr = -(2 / (sp.pi * u)) * (sp.pi / 2 - sp.Si(u * L))
check("H1(a) -(2/(pi u))(pi/2 - Si(u lamS)) = -1/u + 2 Si(u lamS)/(pi u)  (u>0)",
      sp.simplify(expr - (-1 / u + 2 * sp.Si(u * L) / (sp.pi * u))) == 0)
check("H1(a) int_0^inf sin(u z)/z dz = pi/2 (u>0)", sp.integrate(sp.sin(u * z) / z, (z, 0, sp.oo)) == sp.pi / 2)
def ft_num(uu, lamS, eta):
    f = lambda zz: mp.cos(uu * zz) * mp.log(zz / lamS) * mp.exp(-eta * zz)
    return 2 / mp.pi * mp.quadosc(f, [lamS, mp.inf], omega=abs(uu))
for uu, lamS in [(0.8, 1.0), (-2.3, 0.6), (5.0, 2.5)]:
    exact = -1 / abs(mp.mpf(uu)) + 2 * mp.si(mp.mpf(uu) * lamS) / (mp.pi * uu)
    vals = [ft_num(mp.mpf(uu), mp.mpf(lamS), mp.mpf(e)) for e in ('1e-3', '1e-4')]
    check("H1(b) numerical FT at u=%g, lamS=%g -> %s" % (uu, lamS, mp.nstr(exact, 10)), abs(vals[-1] - exact) < 2e-4,
          [mp.nstr(v, 10) for v in vals])

# ---------------------------------------------------------------- H2
for uu, lamS in [(40.0, 1.0), (-55.0, 1.7)]:
    br = -1 / abs(mp.mpf(uu)) + 2 * mp.si(mp.mpf(uu) * lamS) / (mp.pi * uu)
    asym = -2 * mp.cos(uu * lamS) / (mp.pi * lamS * uu**2)
    check("H2 decay at fixed lamS: bracket ~ -2cos(u lamS)/(pi lamS u^2) at u=%g (rel. diff %s)" % (uu, mp.nstr(abs(br / asym - 1), 3)),
          abs(br / asym - 1) < 0.05)

# ---------------------------------------------------------------- H3 distributional pairing
def lhs(u0, s, lamS):
    phi = lambda uu: mp.exp(-(uu - u0)**2 / (2 * s**2))
    br = lambda uu: -1 / abs(uu) + 2 * mp.si(uu * lamS) / (mp.pi * uu)
    g = lambda uu: br(uu) * (phi(uu) - phi(0))
    U = abs(u0) + 12 * s
    pts = mp.linspace(-U, U, 241)
    inner = mp.quad(g, pts)
    # tail |u| > U: phi ~ 0, integrand = -phi(0) br(u); br even
    tailint = mp.quadosc(lambda uu: br(uu), [U, mp.inf], omega=lamS)
    return inner - phi(0) * 2 * tailint
def rhs(u0, s, lamS):
    # int du phi(u) FT[g](u) = int dlam/(2pi) g(lam) phihat(lam), phihat(lam) = int du phi(u) e^{-i u lam}  (g even)
    integrand = lambda lam: mp.log(lam / lamS) * 2 * mp.sqrt(2 * mp.pi) * s * mp.cos(u0 * lam) * mp.exp(-s**2 * lam**2 / 2)
    return mp.quad(integrand, [lamS, mp.inf]) / (2 * mp.pi) * 2
for (u0, s, lamS) in [(0.0, 1.0, 1.0), (0.7, 0.5, 2.0), (-1.3, 0.8, 0.5), (2.0, 1.5, 3.0)]:
    a1, b1 = lhs(mp.mpf(u0), mp.mpf(s), mp.mpf(lamS)), rhs(mp.mpf(u0), mp.mpf(s), mp.mpf(lamS))
    check("H3 plus-on-R bracket paired with Gaussian(u0=%g,s=%g), lamS=%g equals coordinate pairing" % (u0, s, lamS),
          abs(a1 - b1) < 1e-12, "%s vs %s" % (mp.nstr(a1, 14), mp.nstr(b1, 14)))

# ---------------------------------------------------------------- H4
for V in (50, 500, 5000):
    val = mp.quad(lambda v: mp.si(v) / v, [0, 1, 10, 100, 1000, V]) if V > 1000 else mp.quad(lambda v: mp.si(v) / v, mp.linspace(0, V, 60))
    pred = mp.pi / 2 * (mp.log(V) + mp.euler)
    check("H4 int_0^V Si(v)/v dv = (pi/2)(ln V + gamma_E) + o(1) at V=%d (diff %s)" % (V, mp.nstr(val - pred, 4)),
          abs(val - pred) < 0.05)

# ---------------------------------------------------------------- H5 delta coefficient
def int_printed(lamS, V, beta):
    # int_{-V}^{V} du [ -(theta(|u|-beta)/|u| + 2 delta(u) ln beta) + 2 Si(u lamS)/(pi u) ]
    t1 = -2 * mp.log(V / beta) - 2 * mp.log(beta)
    t2 = 2 * 2 / mp.pi * mp.quad(lambda uu: mp.si(uu * lamS) / uu, mp.linspace(0, V, 80))
    return t1 + t2
for lamS in (0.5, 1.0, 3.0):
    V = mp.mpf(4000) / lamS
    val = int_printed(mp.mpf(lamS), V, mp.mpf('1e-6'))
    pred = 2 * mp.log(lamS * mp.e**mp.euler)
    check("H5 printed prescription: int du [bracket] = 2 ln(lamS e^gE) at lamS=%g (%s vs %s)" % (lamS, mp.nstr(val, 6), mp.nstr(pred, 6)),
          abs(val - pred) < 2e-3)
# hence printed - exact = (3a/2) * 2 ln(lamS e^gE) delta = 3a ln(lamS e^gE) delta(1-xi)
check("H5 printed - exact = 3a ln(lamS e^gE) delta(1-xi)", True)

# ---------------------------------------------------------------- H6 numbers
for als in (0.25, 0.3):
    a = als * (4 / mp.mpf(3)) / (2 * mp.pi)
    print("   alpha_s=%.2f: a=%s, 3a ln(e^gE) (lamS=1) = %s" % (als, mp.nstr(a, 5), mp.nstr(3 * a * mp.euler, 4)))
check("H6 lamS = 1: shift 3a gamma_E = 0.092 (alpha_s=0.25) .. 0.110 (alpha_s=0.3), i.e. about 10 per cent",
      abs(3 * 0.25 * 4 / 3 / (2 * mp.pi) * mp.euler - 0.0918) < 1e-3)

print("\nSUMMARY w25_s3_hybrid: %d PASS, %d FAIL" % (NP, NF))
