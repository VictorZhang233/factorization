#!/usr/bin/env python3
"""
N06 (stage-2 verifier): one-loop threshold factorization of the LaMET kernel.

Conventions (LAMET §1.1): lambda = P.z = -P^z z (so sgn(z) = -sgn(lambda)), tree ITD = e^{i lambda},
  h(lambda) = int_0^1 d alpha C(alpha, l) e^{i alpha lambda}  for a quark target,
  C = [1 + a(3/2 l + 3/2)] delta(1-alpha) + a{ [(1+alpha^2)/(1-alpha)]_+ (-l-1) - [4 ln(1-alpha)/(1-alpha)]_+ + 2(1-alpha) }
  (gamma^t, IJJSZ), l = ln(-z^2 mu^2 e^{2 gE}/4) (= JLS l_z),  L = ln(4 p_z^2/mu^2) (= JLS L_z),  l + L = 2 Lam,
  Lam = ln|lambda| + gE.
Claim: e^{-i lambda} h(lambda) -> 1 + a[H1 + J1 + i pi sgn(z)(L-1)] as |lambda| -> oo, with
  H1 = -2 + pi^2/12 - L^2/2 + L,  J1 = l^2/2 + l + pi^2/12 + 2   (JLS eqs. (hardoneloop), (jetoneloop), (JetoneloopIM)).
Methods (different from stage 1 and from s3):
  (a) exact asymptotics from the Mellin/eps representation  int_0^1 b^{eps-1}(e^{-i b lam}-1) = (i lam)^{-eps} gamma_low(eps, i lam) - 1/eps,
      expanded symbolically (sympy),
  (b) numerics at |lambda| = 1e2..1e5, both signs, with mpmath: exponential integral E1 for the 1/beta term and the
      eps-derivative of the lower incomplete gamma function for the ln(beta)/beta term (cross-checked against the
      3F3 series representation at moderate lambda and against direct quadrature),
  (c) RG consistency of the summed one-loop anomalous dimensions,
  (d) H1 against the quasi-TMD hard kernel as printed by ESZ 2019 (eq. C_nlo) and JLL 2020 (c_1 and ln H^(1)).
Run: python3 -I n06_threshold.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

PASS = FAIL = 0
def check(name, ok, info=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(("PASS " if ok else "FAIL ") + name + ("   " + info if info else ""))

# ---------------- (a) exact asymptotics ----------------
eps, Lc = sp.symbols('epsilon Lc')          # Lc = ln(i lambda) (complex log)
gE = sp.EulerGamma
# int_0^1 b^{eps-1}(e^{-i b lam}-1) db = Gamma(eps)(i lam)^{-eps} - 1/eps + O(1/lam)
Jser = sp.series(sp.gamma(eps) * sp.exp(-eps * Lc) - 1 / eps, eps, 0, 3).removeO()
E0 = sp.simplify(Jser.coeff(eps, 0))          # int (e^{-ib lam}-1)/b
E1 = sp.simplify(Jser.coeff(eps, 1))          # int ln b (e^{-ib lam}-1)/b
check("asymptotic int_0^1 (e^{-i b lam}-1)/b db = -(ln(i lam)+gE)", sp.simplify(E0 + Lc + gE) == 0, str(E0))
check("asymptotic int_0^1 ln b (e^{-i b lam}-1)/b db = (ln(i lam)+gE)^2/2 + pi^2/12",
      sp.simplify(E1 - ((Lc + gE)**2 / 2 + sp.pi**2 / 12)) == 0, str(sp.expand(E1)))
lam_abs_log, s = sp.symbols('Lambda s', real=True)   # Lambda = ln|lam| + gE ; s = sgn(lambda)
l, L = sp.symbols('l L', real=True)
sub = {Lc: lam_abs_log - gE + sp.I * sp.pi / 2 * s}
E0a = sp.expand(E0.subs(sub)); E1a = sp.expand(E1.subs(sub))
# plus distribution [(1+a^2)/(1-a)]_+ paired with e^{-i(1-a)lam}:  int_0^1 db (1+(1-b)^2)/b (e^{-ib lam}-1)
B_as = 2 * E0a + sp.Rational(3, 2)                    # + int_0^1 (b-2)(e^{-ib lam}-1) -> -int(b-2) = 3/2
K_as = E1a
G_as = sp.Rational(3, 2) * l + sp.Rational(3, 2) + (-l - 1) * B_as - 4 * K_as   # 2(1-alpha) term -> O(1/lam)
G_as = sp.expand(G_as.subs(s**2, 1))
G_as = sp.expand(G_as.subs(lam_abs_log, (l + L) / 2))
H1 = -2 + sp.pi**2 / 12 - L**2 / 2 + L
J1 = l**2 / 2 + l + sp.pi**2 / 12 + 2
sgn_z = -s
target = H1 + J1 + sp.I * sp.pi * sgn_z * (L - 1)
diff = sp.simplify(sp.expand(G_as - target).subs(s**2, 1))
check("exact large-|lambda| limit of e^{-i lam} h = 1 + a[H1 + J1 + i pi sgn(z)(L-1)]  (symbolic)", diff == 0, str(diff))

# ---------------- (b) numerics ----------------
mp.mp.dps = 40
def Efun(lam):          # int_0^1 (e^{-i b lam}-1)/b db = -Ein(i lam)
    z = mp.mpc(0, lam)
    return -(mp.e1(z) + mp.log(z) + mp.euler)
def Kfun_gamma(lam):    # d/deps [ (i lam)^{-eps} gamma_low(eps, i lam) - 1/eps ] at eps=0
    z = mp.mpc(0, lam)
    f = lambda e: z**(-e) * mp.gammainc(e, 0, z) - 1 / e
    # derivative at 0 via symmetric differences around eps=0 is singular termwise; use Richardson on f'(e) near 0
    return mp.diff(lambda e: f(e), mp.mpf('1e-12'), h=mp.mpf('1e-14')) if False else mp.diff(f, 0 + mp.mpf(10)**-25, method='step', h=mp.mpf(10)**-20)
def Kfun_series(lam):   # -(-i lam) 3F3(1,1,1;2,2,2;-i lam)
    z = mp.mpc(0, -lam)
    return -z * mp.hyper([1, 1, 1], [2, 2, 2], z)
def Kfun_quad(lam):
    f = lambda b: mp.log(b) * (mp.exp(mp.mpc(0, -b * lam)) - 1) / b
    n = int(abs(lam) / mp.pi) + 4
    pts = [mp.mpf(k) / n for k in range(n + 1)]
    return mp.quad(f, pts)
def Bfun(lam):          # int_0^1 (1+(1-b)^2)/b (e^{-ib lam}-1) = 2E + int_0^1 (b-2)(e^{-ib lam}-1)
    w = mp.mpc(0, -lam)
    I_b = (mp.exp(w) * (w - 1) + 1) / w**2            # int_0^1 b e^{w b}
    I_1 = (mp.exp(w) - 1) / w                           # int_0^1 e^{w b}
    return 2 * Efun(lam) + (I_b - 2 * I_1) - (mp.mpf(1) / 2 - 2)
def Tfun(lam):          # int_0^1 b e^{-ib lam}
    w = mp.mpc(0, -lam)
    return (mp.exp(w) * (w - 1) + 1) / w**2
# cross-check K representations at moderate lambda
for lam in [7.3, -12.1, 40.0]:
    k1, k2, k3 = Kfun_gamma(lam), Kfun_series(lam), Kfun_quad(lam)
    check(f"ln(b)/b transform at lambda={lam}: gammainc-derivative vs 3F3 vs quadrature agree",
          abs(k1 - k2) < mp.mpf(10)**-15 and abs(k1 - k3) < mp.mpf(10)**-15, f"{mp.nstr(k1, 15)}")
def G1(lam, lval):      # one-loop coefficient of e^{-i lam} h
    return (mp.mpf(3) / 2 * lval + mp.mpf(3) / 2 + (-lval - 1) * Bfun(lam) - 4 * Kfun_gamma(lam) + 2 * Tfun(lam))
for Lval in [0, 1.3, -0.8]:
    for lam in [1e2, -1e2, 1e3, -1e3, 1e4, -1e4, 1e5, -1e5]:
        Lam = mp.log(abs(lam)) + mp.euler
        lval = 2 * Lam - Lval
        sz = -mp.sign(lam)
        tgt = (-2 + mp.pi**2 / 12 - mp.mpf(Lval)**2 / 2 + Lval) + (lval**2 / 2 + lval + mp.pi**2 / 12 + 2) \
              + mp.mpc(0, 1) * mp.pi * sz * (Lval - 1)
        d = G1(lam, lval) - tgt
        bound = 12 * (abs(lval) + 2) * (Lam + 2) / abs(lam)
        check(f"L={Lval:+.1f} lambda={lam:+.0e}: |G1 - [H1+J1+i pi sgn(z)(L-1)]| = {mp.nstr(abs(d), 4)}  (Im d = {mp.nstr(d.imag, 3)})",
              abs(d) < bound)
# the residual decays ~ ln|lambda|/|lambda|: check ratio between 1e4 and 1e5
Lval = 1.3
r = []
for lam in [1e4, 1e5]:
    Lam = mp.log(lam) + mp.euler; lval = 2 * Lam - Lval
    tgt = (-2 + mp.pi**2 / 12 - mp.mpf(Lval)**2 / 2 + Lval) + (lval**2 / 2 + lval + mp.pi**2 / 12 + 2) - mp.mpc(0, 1) * mp.pi * (Lval - 1)
    r.append(abs(G1(lam, lval) - tgt) * lam / (Lam**2))
check("residual * |lambda|/Lambda^2 stays O(1) between 1e4 and 1e5 (power-suppressed, log-enhanced)", r[1] < 3 * r[0] and r[1] < 50,
      f"{[mp.nstr(t, 4) for t in r]}")
# sign of the phase flips with lambda
lam = 1e5; Lam = mp.log(lam) + mp.euler; lval = 2 * Lam - 1.3
im_p = G1(lam, lval).imag; im_m = G1(-lam, lval).imag
check("Im part flips sign with lambda and equals -pi sgn(lambda)(L-1) = +pi sgn(z)(L-1) at L=1.3",
      abs(im_p + mp.pi * 0.3) < 1e-2 and abs(im_m - mp.pi * 0.3) < 1e-2, f"Im(+)={mp.nstr(im_p, 8)}, Im(-)={mp.nstr(im_m, 8)}")

# ---------------- (c) anomalous dimensions ----------------
mu = sp.symbols('mu', positive=True); pz, z = sp.symbols('p_z z', positive=True)
a = sp.symbols('a', positive=True)
Lmu = sp.log(4 * pz**2 / mu**2); lmu = sp.log(sp.exp(2 * gE) * mu**2 * z**2 / 4)
lnH = a * (-2 + sp.pi**2 / 12 - Lmu**2 / 2 + Lmu)
lnJt = a * (lmu**2 / 2 + lmu + sp.pi**2 / 12 + 2)
phase = a * sp.pi * (Lmu - 1)                   # Im ln J_f for sgn z = +1
gH = sp.simplify(mu * sp.diff(lnH, mu)); gJ = sp.simplify(mu * sp.diff(lnJt, mu)); gph = sp.simplify(mu * sp.diff(phase, mu))
Gcusp = 2 * a          # = alpha_s C_F/pi
check("d lnH/d ln mu = Gcusp L + gamma_H with gamma_H = -2a (= -alpha_s C_F/pi)", sp.simplify(gH - (Gcusp * Lmu - 2 * a)) == 0, str(sp.simplify(gH)))
check("d ln Jtilde/d ln mu = Gcusp l - gamma_J with gamma_J = -2a (JLS eq. resulttildegammaJ at one loop)",
      sp.simplify(gJ - (Gcusp * lmu + 2 * a)) == 0, str(sp.simplify(gJ)))
check("d(phase)/d ln mu = -pi Gcusp (sgn z = +1)", sp.simplify(gph + sp.pi * Gcusp) == 0)
tot = sp.simplify(gH + gJ)
check("sum of the real anomalous dimensions = Gcusp ln(lambda^2 e^{2 gE}) (mu-independent; non-cusp parts cancel at one loop)",
      sp.simplify(tot - Gcusp * sp.log(sp.exp(2 * gE) * pz**2 * z**2)) == 0 and sp.diff(tot, mu) == 0, str(tot))
# consistency with the threshold limit of the kernel RGE dC/d ln mu^2 = a[3/2 delta - B]:
# pairing with e^{-i(1-alpha)lam} gives a[3/2 - B_as] for d/dln mu^2, i.e. 2a[3/2 - B_as] for d/dln mu
rge_thr = sp.expand(2 * (sp.Rational(3, 2) - B_as))
rge_thr = sp.expand(rge_thr.subs(lam_abs_log, (l + L) / 2))
claim = 2 * ((l + L) - sp.I * sp.pi * (-s))   # Gcusp/a [ln(lam^2 e^{2gE}) - i pi sgn z]
check("threshold limit of kernel RGE = Gcusp[ln(lambda^2 e^{2gE}) - i pi sgn z]", sp.simplify(rge_thr - claim) == 0, str(rge_thr))

# ---------------- (d) universality with the quasi-TMD hard kernel (formulas as printed, read from the sources) ---------------
# ESZ 2019 eq. (C_nlo): C = 1 + (as CF/4pi)(-ln^2(zeta/mu^2) + 2 ln(zeta/mu^2) - 4 + pi^2/6), zeta = (2xP^z)^2
Lz = sp.symbols('L_z', real=True)
C_esz = sp.Rational(1, 2) * (-Lz**2 + 2 * Lz - 4 + sp.pi**2 / 6)            # in units of as CF/(2pi)
# JLL 2020 (arXiv:1911.03840, l.416-418): ln H^(1) = as[c1 + CF/(2pi)(ln(zeta/mu^2) - ln^2/2)], c1 = CF/(2pi)(-2+pi^2/12)
H_jll = (-2 + sp.pi**2 / 12) + (Lz - Lz**2 / 2)
H_jls = -2 + sp.pi**2 / 12 - Lz**2 / 2 + Lz
check("H1 (JLS threshold) = ESZ quasi-TMD C^(1) = JLL ln H^(1)", sp.simplify(C_esz - H_jls) == 0 and sp.simplify(H_jll - H_jls) == 0)
# JLS: H = |H_HL|, H^pm_LFWF = 1 + (as CF/4pi)(-4 - 5pi^2/6 + 2 L_pm - L_pm^2), L_pm = L_z +- i pi
Lp = Lz + sp.I * sp.pi
modH = sp.simplify(sp.re(sp.expand(sp.Rational(1, 2) * (-4 - 5 * sp.pi**2 / 6 + 2 * Lp - Lp**2))))
check("Re of the LFWF/heavy-light Sudakov kernel at one loop = H1", sp.simplify(modH - H_jls) == 0, str(modH))
imH = sp.simplify(sp.im(sp.expand(sp.Rational(1, 2) * (-4 - 5 * sp.pi**2 / 6 + 2 * Lp - Lp**2))))
check("Im H^+_LFWF = -pi(L_z-1) (units a); with H_HL(sgn z)=H_LFWF^{-sgn z}: Arg H_HL = +pi sgn(z)(L_z-1) = Im J_f^(1) of JLS (JetoneloopIM)",
      sp.simplify(imH + sp.pi * (Lz - 1)) == 0, str(imH))

print(f"\nSUMMARY n06: {PASS} PASS, {FAIL} FAIL")
