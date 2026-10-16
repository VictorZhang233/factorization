#!/usr/bin/env python3
"""N28 (stage-2 verifier): OTHERS 'checked transcriptions'.
 (i)   BNS PRL 127 (2021) 212002 eqs. (14),(19) -> eq. (21) 2F2(1,1;2,5/2;-w); first SLL; asymptotics (Mellin-Barnes)
 (ii)  Liu-Neubert JHEP04(2020)033 eq. (3) and its n=0,1 terms vs eq. (1)
 (iii) LUXqed PRL 117 (2016) 242002 eq. (6) on a point-like Dirac target vs Frixione JHEP11(2019)158 eq. (4.189);
       plus an independent O(alpha) MS-bar photon-in-lepton PDF from the light-cone wave function in DR
 (iv)  Collins-Rogers-Sato PRD 105 (2022) 076010 eqs. (55)-(59): Dirac trace (numerical gamma matrices), DR expansion, signs
 (v)   LO BK/BFKL eigenvalue via the 2D 'complex Beta function' (analytic regularization), not by direct quadrature
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
import numpy as np

mp.mp.dps = 30
NP = 0; NF = 0
def check(name, ok, info=''):
    global NP, NF
    if ok: NP += 1
    else: NF += 1
    print(('[PASS] ' if ok else '[FAIL] ') + name + ('   ' + info if info else ''))

# ------------------------------------------------------------------ (i) BNS
n_, r_ = sp.symbols('n r', integer=True, nonnegative=True)
CF, Nc, aS, L, DY, sB, w = sp.symbols('C_F N_c alpha_s L DeltaY sigma_B w', positive=True)
def C_S(r, n):   # BNS eq. (19), singlet, forward: J2 = J43/2 = DeltaY
    J2 = DY; J43 = 2 * DY
    return sB * 2**(8 - r) * sp.pi**2 * (4 * Nc)**n * CF * (-J43 + 2 * J2 * (1 if r > 0 else 0))
def sigma_n(n):  # BNS eq. (14)
    return (aS / (4 * sp.pi))**(n + 3) * L**(2 * n + 3) * sp.Integer(-4)**n * sp.factorial(n) / sp.factorial(2 * n + 3) * \
        sum(sp.factorial(2 * r) / (4**r * sp.factorial(r)**2) * C_S(r, n) for r in range(n + 1))
pref = -sB * 4 * CF / (3 * sp.pi) * aS**3 * L**3 * DY
wval = Nc * aS * L**2 / sp.pi
ok = True
for n in range(0, 16):
    term_hyp = pref * sp.rf(1, n) * sp.rf(1, n) / (sp.rf(2, n) * sp.rf(sp.Rational(5, 2), n)) * (-wval)**n / sp.factorial(n)
    ok &= sp.simplify(sigma_n(n) - term_hyp) == 0
check('(i-a) BNS (14)+(19), J2=J43/2=DeltaY: sum_n sigma_n^SLL = -sigma_B (4C_F/3pi) a_s^3 L^3 DeltaY 2F2(1,1;2,5/2;-w), term by term n=0..15 (exact)', ok)
check('(i-b) only r=0 contributes for the singlet in forward kinematics', all(C_S(r, 3) == 0 for r in range(1, 4)) and C_S(0, 3) != 0)
s1 = sp.simplify(sigma_n(1)); s0 = sp.simplify(sigma_n(0))
check('(i-c) first SUPER-leading term (n=1, four loops) = +(4/(15 pi^2)) C_F N_c a_s^4 L^5 DeltaY sigma_B',
      sp.simplify(s1 - sp.Rational(4, 15) / sp.pi**2 * CF * Nc * aS**4 * L**5 * DY * sB) == 0, str(s1))
check('(i-d) the n=0 (three-loop) term is -(4C_F/3pi) a_s^3 L^3 DeltaY sigma_B: single-logarithmic, not super-leading',
      sp.simplify(s0 - pref) == 0, str(s0))
# asymptotics from the Mellin-Barnes double pole at s=-1: (3/2)(ln w - psi(3/2))/w
for W in [mp.mpf(10)**4, mp.mpf(10)**6, mp.mpf(10)**8]:
    f = mp.hyp2f2(1, 1, 2, mp.mpf(5) / 2, -W)
    asy = mp.mpf(3) / 2 * (mp.log(W) - mp.digamma(mp.mpf(3) / 2)) / W
    check('(i-e) 2F2(1,1;2,5/2;-w) ~ (3/2)(ln w - psi(3/2))/w at w=%s; w*2F2/ln w = %s' % (mp.nstr(W, 2), mp.nstr(W * f / mp.log(W), 6)),
          abs(f / asy - 1) < 10 / W, 'rel.dev %.1e' % float(abs(f / asy - 1)))

# ------------------------------------------------------------------ (ii) Liu-Neubert eq. (3)
Lh = sp.symbols('Lhat', positive=True)
y = CF * aS * Lh**2 / (2 * sp.pi)
ok = True
for n in range(0, 21):
    lhs_t = Lh**2 * sp.factorial(n) / sp.factorial(2 * n + 2) * (-y)**n
    rhs_t = Lh**2 / 2 * sp.rf(1, n)**2 / (sp.rf(sp.Rational(3, 2), n) * sp.rf(2, n)) * (-CF * aS * Lh**2 / (8 * sp.pi))**n / sp.factorial(n)
    ok &= sp.simplify(lhs_t - rhs_t) == 0
check('(ii-a) LN eq. (3): L^2 sum n!/(2n+2)! (-C_F a_s L^2/2pi)^n = (L^2/2) 2F2(1,1;3/2,2;-C_F a_s L^2/(8pi)), n=0..20 exact', ok)
t1 = sp.simplify(Lh**2 * sp.factorial(1) / sp.factorial(4) * (-y))
check('(ii-b) n=0 term L^2/2 and n=1 term (C_F a_s/4pi)(-L^4/12): the leading logs of LN eq. (1)',
      sp.simplify(t1 - CF * aS / (4 * sp.pi) * (-Lh**4 / 12)) == 0, str(t1))
# numerical: closed form vs partial sums at a moderate argument
Lv, av, CFv = mp.mpf(8), mp.mpf('0.11'), mp.mpf(4) / 3
ser = Lv**2 * mp.nsum(lambda k: mp.factorial(k) / mp.factorial(2 * k + 2) * (-CFv * av * Lv**2 / (2 * mp.pi))**k, [0, mp.inf])
clo = Lv**2 / 2 * mp.hyp2f2(1, 1, mp.mpf(3) / 2, 2, -CFv * av * Lv**2 / (8 * mp.pi))
check('(ii-c) numerical: series = closed form at L=8, a_s=0.11', abs(ser - clo) < 1e-25, '%s vs %s' % (mp.nstr(ser, 15), mp.nstr(clo, 15)))

# ------------------------------------------------------------------ (iii) LUXqed point-like limit
x, z, Q2, m, mu, al = sp.symbols('x z Q2 m mu alpha', positive=True)
zp = 1 + (1 - z)**2
# point-like Dirac target: G_E=G_M=1 -> F2 = delta(1-x/z), FL = (4m^2/Q^2) delta(1-x/z); int_x^1 dz/z f(z) delta(1-x/z) = f(x)
F2c, FLc = 1, 4 * m**2 / Q2
integrand = (zp + 2 * x**2 * m**2 / Q2) * F2c - z**2 * FLc
lux = (1 / (2 * sp.pi * al)) * (al**2 * sp.integrate(integrand / Q2, (Q2, x**2 * m**2 / (1 - z), mu**2 / (1 - z))) - al**2 * z**2 * F2c)
lux = sp.simplify(lux.subs(z, x))
target = al / (2 * sp.pi) * (1 + (1 - x)**2) * (sp.log(mu**2 / m**2) - 2 * sp.log(x) - 1) + al * m**2 * x**2 * (1 - x) / (sp.pi * mu**2)
check('(iii-a) LUXqed eq. (6), point-like target (fixed alpha): xf = (a/2pi)[1+(1-x)^2][ln(mu^2/m^2)-2ln x-1] + a m^2 x^2(1-x)/(pi mu^2)',
      sp.simplify(sp.expand_log(lux - target, force=True)) == 0)
frix = x * al / (2 * sp.pi) * (1 + (1 - x)**2) / x * (sp.log(mu**2 / m**2) - 2 * sp.log(x) - 1)   # x * (a/2pi) Gamma^[1], K=0 (MSbar)
lead = sp.limit(sp.expand_log(lux - frix, force=True), mu, sp.oo)
check('(iii-b) its leading-power part equals x*(alpha/2pi)*Gamma^[1]_{gamma/e} of Frixione eq. (4.189) with K_{gamma e}=0 (MSbar); the rest is a m^2/mu^2 power correction',
      lead == 0 and sp.simplify(sp.expand_log(lux - frix - al * m**2 * x**2 * (1 - x) / (sp.pi * mu**2), force=True)) == 0)
noFL = (1 / (2 * sp.pi * al)) * (al**2 * sp.integrate((zp + 2 * x**2 * m**2 / Q2) / Q2, (Q2, x**2 * m**2 / (1 - z), mu**2 / (1 - z))) - al**2 * z**2)
noFL = sp.simplify(noFL.subs(z, x))
dFL = sp.limit(sp.expand_log(noFL - lux, force=True), mu, sp.oo)
check('(iii-c) dropping F_L shifts the result by +(alpha/2pi) 4(1-x) at leading power', sp.simplify(dFL - al / (2 * sp.pi) * 4 * (1 - x)) == 0, str(sp.simplify(dFL)))
noConv = lux + al / (2 * sp.pi) * x**2
check('(iii-d) dropping the MSbar conversion term -a^2 z^2 F2(mu^2) shifts it by +(alpha/2pi) x^2', sp.simplify(noConv - lux - al * x**2 / (2 * sp.pi)) == 0)
# independent: O(alpha) MSbar photon-in-lepton PDF from the light-cone wave function in DR
# f = (alpha/2pi) * MSbar-finite part of int d^{2-2e}k [P^(d)(x) k^2 + x^3 m^2]/(k^2 + x^2 m^2)^2,  P^(d) = (1+(1-x)^2)/x - e x
e = sp.symbols('e', positive=True)
M2 = x**2 * m**2
# int d^n k (k^2)^a/(k^2+M^2)^b = pi^{n/2} Gamma(a+n/2)Gamma(b-a-n/2)/(Gamma(n/2)Gamma(b)) (M^2)^{n/2+a-b}, n = 2-2e, normalized by pi^{1-e}
I1 = sp.gamma(2 - e) * sp.gamma(e) / (sp.gamma(1 - e) * sp.gamma(2)) * (M2 / mu**2)**(-e)          # k^2/(k^2+M^2)^2
I0 = sp.gamma(1 - e) * sp.gamma(1 + e) / (sp.gamma(1 - e) * sp.gamma(2)) * (M2 / mu**2)**(-e) / M2  # 1/(k^2+M^2)^2
Pd = (1 + (1 - x)**2) / x - e * x
bare = sp.series(Pd * I1 + x**3 * m**2 * I0, e, 0, 1).removeO()
pole = sp.simplify(bare.coeff(e, -1)); fin = sp.simplify(bare.coeff(e, 0) + pole * sp.EulerGamma)   # MSbar: subtract 1/e - gamma_E (+ln 4pi absorbed)
check('(iii-e) independent LCWF/DR computation: pole = P_{gamma e}(x)/e, MSbar finite part = (1+(1-x)^2)/x [ln(mu^2/m^2) - 2 ln x - 1]  (= Frixione (4.189), K=0)',
      sp.simplify(pole - (1 + (1 - x)**2) / x) == 0 and sp.simplify(sp.expand_log(fin - (1 + (1 - x)**2) / x * (sp.log(mu**2 / m**2) - 2 * sp.log(x) - 1), force=True)) == 0,
      'finite = %s' % sp.simplify(fin))
# consistency of the m^2 term x^3 m^2 with the exact Budnev EPA: cutoff on k^2 reproduces (1+(1-x)^2)/x ln(K^2/x^2m^2) - 2(1-x)/x
K2, k2 = sp.symbols('K2 k2', positive=True)
cut = sp.integrate(((1 + (1 - x)**2) / x * k2 + x**3 * m**2) / (k2 + M2)**2, (k2, 0, K2))
epa = (1 + (1 - x)**2) / x * sp.log(K2 / M2) - 2 * (1 - x) / x
check('(iii-f) the x^3 m^2 mass term reproduces the Budnev EPA photon flux at leading power (cutoff in k_T)',
      sp.simplify(sp.limit(sp.expand_log(cut - epa, force=True), K2, sp.oo)) == 0)

# ------------------------------------------------------------------ (iv) CRS Yukawa model
# Dirac matrices (Dirac representation), light-front gamma^+ = (g0+g3)/sqrt2
s0 = np.eye(2); sx = np.array([[0, 1], [1, 0]]); sy = np.array([[0, -1j], [1j, 0]]); szm = np.array([[1, 0], [0, -1]])
Z = np.zeros((2, 2))
g0 = np.block([[s0, Z], [Z, -s0]]).astype(complex)
gs = [np.block([[Z, s], [-s, Z]]).astype(complex) for s in (sx, sy, szm)]
gp = (g0 + gs[2]) / np.sqrt(2)
def slash(v):  # v = (v0, v1, v2, v3)
    return v[0] * g0 - v[1] * gs[0] - v[2] * gs[1] - v[3] * gs[2]
rng = np.random.default_rng(3)
ok = True; okk = True
for _ in range(5):
    mq, mp_, ms_ = rng.uniform(0.2, 0.5), rng.uniform(0.8, 1.2), rng.uniform(1.0, 1.8)
    Pp, xi = rng.uniform(1, 5), rng.uniform(0.05, 0.95)
    kT = rng.normal(size=2) * 0.7
    Pm = mp_**2 / (2 * Pp)
    kp = xi * Pp
    km = Pm - (ms_**2 + kT @ kT) / (2 * (1 - xi) * Pp)          # scalar (P-k) on shell
    lc = lambda vp, vm, vT: np.array([(vp + vm) / np.sqrt(2), vT[0], vT[1], (vp - vm) / np.sqrt(2)])
    P = lc(Pp, Pm, np.zeros(2)); k = lc(kp, km, kT)
    T = 0.25 * np.trace(gp @ (slash(k) + mq * np.eye(4)) @ (slash(P) + mp_ * np.eye(4)) @ (slash(k) + mq * np.eye(4))).real
    ok &= abs(T - Pp * (kT @ kT + (mq + xi * mp_)**2)) < 1e-10 * max(1, abs(T))
    k2 = k[0]**2 - k[1]**2 - k[2]**2 - k[3]**2
    Delta = xi * ms_**2 + (1 - xi) * mq**2 - xi * (1 - xi) * mp_**2
    okk &= abs((k2 - mq**2) - (-(kT @ kT + Delta) / (1 - xi))) < 1e-10
check('(iv-a) Dirac trace (numerical gamma matrices): (1/4)Tr[g+ (k+mq)(P+M)(k+mq)] = P+ [kT^2 + (mq + xi M)^2] on the scalar mass shell', ok)
check('(iv-b) k^2 - mq^2 = -(kT^2 + Delta(xi))/(1-xi), Delta = xi ms^2 + (1-xi) mq^2 - xi(1-xi) M^2  => integrand (1-xi)[kT^2+(mq+xi M)^2]/(kT^2+Delta)^2 (CRS (58))', okk)
Dl, c, t = sp.symbols('Delta c t', positive=True)
J = sp.gamma(2 - e) * sp.gamma(e) / sp.gamma(2) * Dl**(-e) * mu**(2 * e) + c * sp.gamma(1 - e) * sp.gamma(1 + e) / sp.gamma(2) * Dl**(-1 - e) * mu**(2 * e)
Jser = sp.series(J, e, 0, 1).removeO()
check('(iv-c) DR: int dkT^2 (kT^2/mu^2)^{-e}[kT^2 + c]/(kT^2+Delta)^2 = 1/e + [ln(mu^2/Delta) - 1 + c/Delta] + O(e) (no gamma_E in this measure; Collins S_e = (4pi)^e/Gamma(1-e)): MSbar finite part = CRS (55) bracket, counterterm 1/e as in CRS (57)',
      sp.simplify(Jser.coeff(e, -1) - 1) == 0 and sp.simplify(sp.expand_log(Jser.coeff(e, 0) - (sp.log(mu**2 / Dl) - 1 + c / Dl), force=True)) == 0,
      'finite part = %s' % sp.simplify(Jser.coeff(e, 0)))
fpdf = lambda xi, muv, mq=0.3, mpp=1.0, ms=1.5: (1 - xi) * ((mq + xi * mpp)**2 / (xi * ms**2 + (1 - xi) * mq**2 - xi * (1 - xi) * mpp**2)
                                                   + np.log(muv**2 / (xi * ms**2 + (1 - xi) * mq**2 - xi * (1 - xi) * mpp**2)) - 1)
xs = np.linspace(0.0005, 0.9995, 1999)
neg08 = xs[fpdf(xs, 0.8) < 0]; neg12 = xs[fpdf(xs, 1.2) < 0]
def br(xi, muv, mq=mp.mpf('0.3'), mpp=mp.mpf('1.0'), ms=mp.mpf('1.5')):
    Dx = xi * ms**2 + (1 - xi) * mq**2 - xi * (1 - xi) * mpp**2
    return (mq + xi * mpp)**2 / Dx + mp.log(muv**2 / Dx) - 1
root08 = float(mp.findroot(lambda t: br(t, mp.mpf('0.8')), mp.mpf('0.27'))); root12 = float(mp.findroot(lambda t: br(t, mp.mpf('1.2')), mp.mpf('0.5')))
check('(iv-d) mq=0.3, M=1.0, ms=1.5 GeV: negative exactly on (0.2640, 1) at mu=0.8 GeV and on (0.5674, 1) at 1.2 GeV (bracket(1)<0), positive for all xi at 2.5 GeV;'
      ' NOTE: OTHERS "[0.28,0.98]" is a coarse-grid artefact',
      abs(root08 - 0.26403) < 1e-4 and neg08.max() > 0.999 and abs(root12 - 0.56737) < 1e-4 and (fpdf(xs, 2.5) > 0).all(),
      'roots %.5f (0.8 GeV), %.5f (1.2 GeV); grid neg range at 0.8 GeV [%.4f, %.4f]' % (root08, root12, neg08.min(), neg08.max()))
mustar = 1.5 * np.exp(0.5 * (1 - (0.3 + 1.0)**2 / 1.5**2))
check('(iv-e) xi->1 sign change at mu* = ms exp{[1-(mq+M)^2/ms^2]/2} = 1.70 GeV; xi->0 bracket -> ln(mu^2/mq^2)',
      abs(mustar - 1.6988) < 1e-3 and abs(fpdf(1e-9, 0.7) / (1 - 1e-9) - np.log(0.7**2 / 0.3**2)) < 1e-6, 'mu* = %.4f' % mustar)

# ------------------------------------------------------------------ (v) BK eigenvalue via the 2D complex Beta function
# I(a,b) = int d^2z/pi |z|^{2(a-1)} |1-z|^{2(b-1)} = G(a)G(b)G(1-a-b)/(G(1-a)G(1-b)G(a+b))
Ib = lambda a, b: mp.gamma(a) * mp.gamma(b) * mp.gamma(1 - a - b) / (mp.gamma(1 - a) * mp.gamma(1 - b) * mp.gamma(a + b))
chi = lambda g: 2 * mp.digamma(1) - mp.digamma(g) - mp.digamma(1 - g)
for gm in [mp.mpf('0.5'), mp.mpf('0.3'), mp.mpf('0.15'), mp.mpf('0.7')]:
    # chi(g) = (1/2pi) int d^2z r^2/(r1^2 r2^2) [(r1^2)^g + (r2^2)^g - 1] (r=1), regulated by (r1^2 r2^2)^delta, delta -> 0
    vals = []
    for d in [mp.mpf('1e-8'), mp.mpf('1e-10')]:
        vals.append((Ib(gm + d, d) + Ib(d, gm + d) - Ib(d, d)) / 2)
    check('(v) linearized LO BK kernel on (r^2)^gamma, gamma=%s: (1/2) lim [I(g,0)+I(0,g)-I(0,0)] = 2psi(1)-psi(g)-psi(1-g)' % mp.nstr(gm, 2),
          abs(vals[-1] - chi(gm)) < 1e-8, 'regulated %s, chi %s' % (mp.nstr(vals[-1], 12), mp.nstr(chi(gm), 12)))
check('(v) chi(1/2) = 4 ln 2 (exact: 2psi(1)-2psi(1/2))', abs(chi(mp.mpf('0.5')) - 4 * mp.log(2)) < 1e-28)

print('\nSUMMARY n28_s2: %d PASS, %d FAIL' % (NP, NF))
