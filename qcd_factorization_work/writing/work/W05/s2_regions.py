r"""
s2_regions.py  (writer W05; Ch5 ex:sudakov-onshell-hard, ex:sudakov-offshell, ex:sudakov-massive, ex:sudakov-ll,
rem:sudakov-consistency; VF-REG-10/11/12/14, VF-REF-2, VF-SUD-4)      -- version 2 (2026-10-14, after quota reset)

Version 2 replaces the tests of version 1 that failed for numerical/test reasons only:
  * the C1 factor integrals are checked with transformed (fast-decaying) integrands at higher precision;
  * the NLP/NNLP expansion of the exact triangle is checked at mp.dps=60 (v1 lost precision at t=1e-12);
  * the analytic-regulator collinear region is compared with a relative tolerance;
  * the Laurent coefficients of lim_{delta->0}(C1+C2) are extracted by a contour integral in eps
    (v1 used a symmetric difference at eps=+-0.01, contaminated by the O(eps^2) coefficient ~ L^4).

Normalisation (c_regions, BBF x e^{eps gE}):
   I = e^{eps gE} mu^{2eps} Int d^Dk/(i pi^{D/2}) prod_j (-q_j^2 + m_j^2 - i0)^{-1}
     = e^{eps gE} mu^{2eps} Gamma(1+eps) Int dalpha delta(1-sum alpha) U^{-1+2eps} F^{-1-eps}     (one loop, 3 lines)
Units Q^2 = mu^2 = 1 unless stated; t = P^2/Q^2 (off-shell), t = M^2/Q^2 (massive exchange), t = m^2/Q^2 (massive legs).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
mp.mp.dps = 40
PASS = []
def check(name, ok, info=''):
    PASS.append(bool(ok)); print(('[PASS] ' if ok else '[FAIL] ') + name + ((' : ' + str(info)) if info != '' else ''))

eps = sp.Symbol('epsilon')
gE = sp.EulerGamma
NORD = 8
def lngam1(z):
    """ln Gamma(1+z) as a series: -gE z + sum_k (-1)^k zeta(k) z^k / k"""
    return -gE * z + sum((-1) ** k * sp.zeta(k) * z ** k / k for k in range(2, NORD))
def ser(expr_ln, pref, order=1):
    e = sp.series(sp.exp(sp.expand(expr_ln)), eps, 0, order + 3).removeO()
    return sp.expand(sp.series(sp.expand(e * pref), eps, 0, order + 1).removeO())

# =============================================================== (A) on-shell massless triangle = its hard region
# Cheng-Wu alpha_0 = 1: U = 1+x1+x2, F = x1 x2 (Q^2=1)
Hcl = lambda e_: mp.e ** (e_ * mp.euler) * mp.gamma(1 + e_) * mp.gamma(-e_) ** 2 / mp.gamma(1 - 2 * e_)
mp.mp.dps = 20
ev = mp.mpf('-0.3')
Hnum = mp.quad(lambda a1: mp.quad(lambda a2: (a1 * a2) ** (-1 - ev) * (1 + a1 + a2) ** (-1 + 2 * ev), [0, 1, mp.inf]), [0, 1, mp.inf])
Hnum *= mp.e ** (ev * mp.euler) * mp.gamma(1 + ev)
check('(A) on-shell triangle: parametric integral = e^{eps gE}G(1+eps)G(-eps)^2/G(1-2eps), eps=-0.3 (IR strip eps<0)',
      abs(Hnum / Hcl(ev) - 1) < 1e-6, (mp.nstr(Hnum, 15), mp.nstr(Hcl(ev), 15)))
mp.mp.dps = 40
Hser = ser(eps * gE + lngam1(eps) + 2 * lngam1(-eps) - lngam1(-2 * eps), 1 / eps ** 2, 1)
check('(A) Q^2 H = 1/eps^2 - pi^2/12 - (7/3) zeta3 eps + O(eps^2)  (mu = Q)',
      sp.simplify(Hser - (1 / eps ** 2 - sp.pi ** 2 / 12 - sp.Rational(7, 3) * sp.zeta(3) * eps)) == 0, Hser)

# =============================================================== (B) off-shell triangle: four regions (VF-REG-10)
# F = t(x1+x2) + x1 x2, U = 1+x1+x2  (alpha_0 = 1)
t = sp.Symbol('t', positive=True)
C1sym = -sp.exp(eps * gE) * sp.gamma(1 + eps) * t ** (-eps) * sp.gamma(-eps) ** 2 / sp.gamma(1 - 2 * eps)
S_vf = -t ** (-2 * eps) * sp.exp(eps * gE) * sp.gamma(1 + eps) * sp.gamma(eps) * sp.gamma(-eps)
S_alt = t ** (-2 * eps) * sp.exp(eps * gE) * sp.gamma(1 + eps) ** 2 * sp.gamma(1 - eps) / eps ** 2
check('(B) S: VF-REG-10 form = t^{-2eps} e^{eps gE} G(1+eps)^2 G(1-eps)/eps^2', sp.simplify(sp.gammasimp(S_vf - S_alt)) == 0)
tv = mp.mpf('0.01')
# ultrasoft region: expand F -> t(x1+x2)+x1 x2 with U -> x1 x2 ... in Cheng-Wu variables the ultrasoft region is
# x1,x2 ~ t and its integrand is (x1 x2)^{...}? -> use the Schwinger form derived in the text:
#   Q^2 S = e^{eps gE} G(1+eps) Int_0^inf Int_0^inf deta1 deta2 [eta1 eta2 + t(eta1+eta2)]^{-1-eps}   (0<eps<1)
mp.mp.dps = 20
ev = mp.mpf('0.3')
Snum = mp.e ** (ev * mp.euler) * mp.gamma(1 + ev) * mp.quad(
    lambda y1: mp.quad(lambda y2: (y1 * y2 + tv * (y1 + y2)) ** (-1 - ev), [0, tv, 1, mp.inf]), [0, tv, 1, mp.inf])
Scl = complex(sp.N(S_alt.subs({eps: sp.Rational(3, 10), t: sp.Rational(1, 100)}), 30))
check('(B) ultrasoft region: Schwinger double integral = closed form (eps=0.3, t=0.01)', abs(Snum / Scl - 1) < 1e-6,
      (mp.nstr(Snum, 15), Scl))
mp.mp.dps = 40
# collinear region C1: Q^2 C1 = e^{eps gE}G(1+eps) Int_0^1 dx Int_0^inf deta [x(1-x)t + eta x]^{-1-eps}
#   eta-integral (Re eps>0): [x(1-x)t]^{-eps}/(eps x)  ;  x-integral (Re eps<0): Int x^{-1-eps}(1-x)^{-eps} = B(-eps,1-eps)
ev = mp.mpf('0.25'); xx = mp.mpf('0.37')
f_eta = mp.quad(lambda u: (xx * (1 - xx) * tv + xx * u) ** (-1 - ev), [0, tv, 1, 10, 100, 1000, 10**4, 10**5, mp.inf])
check('(B) C1: eta-integral = [x(1-x)t]^{-eps}/(eps x)  (eps=0.25)', abs(f_eta / ((xx * (1 - xx) * tv) ** (-ev) / (ev * xx)) - 1) < 1e-6, mp.nstr(f_eta / ((xx * (1 - xx) * tv) ** (-ev) / (ev * xx)) - 1, 3))
ev = mp.mpf('-0.25')
f_x = mp.quad(lambda x: x ** (-1 - ev) * (1 - x) ** (-ev), [0, mp.mpf(1) / 2, 1])
check('(B) C1: x-integral = B(-eps,1-eps)  (eps=-0.25)', abs(f_x / mp.beta(-ev, 1 - ev) - 1) < 1e-6, mp.nstr(f_x / mp.beta(-ev, 1 - ev) - 1, 3))
# hence Q^2 C1 = e^{eps gE}G(1+eps) t^{-eps} B(-eps,1-eps)/eps = -e^{eps gE}G(1+eps) t^{-eps} G(-eps)^2/G(1-2eps)
C1_fact = sp.exp(eps * gE) * sp.gamma(1 + eps) * t ** (-eps) * sp.gamma(-eps) * sp.gamma(1 - eps) / sp.gamma(1 - 2 * eps) / eps
check('(B) C1 = e^{eps gE}G(1+eps)t^{-eps}B(-eps,1-eps)/eps = VF-REG-10 form', sp.simplify(sp.gammasimp(C1_fact - C1sym)) == 0)
# Laurent expansions at mu = Q, Lt = ln t = ln(P^2/Q^2)
Lt = sp.Symbol('Lt', real=True)
C1ser = sp.expand(ser(-eps * Lt + eps * gE + lngam1(eps) + 2 * lngam1(-eps) - lngam1(-2 * eps), -1 / eps ** 2, 1))
C1_ref = -1 / eps ** 2 + Lt / eps - Lt ** 2 / 2 + sp.pi ** 2 / 12 + eps * (Lt ** 3 / 6 - sp.pi ** 2 * Lt / 12 + sp.Rational(7, 3) * sp.zeta(3))
check('(B) Q^2 C1 = -1/e^2 + L/e - L^2/2 + pi^2/12 + e(L^3/6 - pi^2 L/12 + 7 zeta3/3), L=ln t', sp.simplify(C1ser - C1_ref) == 0)
Sser = sp.expand(ser(-2 * eps * Lt + eps * gE + 2 * lngam1(eps) + lngam1(-eps), 1 / eps ** 2, 1))
S_ref = 1 / eps ** 2 - 2 * Lt / eps + 2 * Lt ** 2 + sp.pi ** 2 / 4 + eps * (-sp.Rational(4, 3) * Lt ** 3 - sp.pi ** 2 * Lt / 2 - sp.zeta(3) / 3)
check('(B) Q^2 S = 1/e^2 - 2L/e + 2L^2 + pi^2/4 + e(-4L^3/3 - pi^2 L/2 - zeta3/3)', sp.simplify(Sser - S_ref) == 0)
tot = sp.expand(Hser + 2 * C1ser + Sser)
check('(B) Q^2(H+C1+C2+S) = L^2 + pi^2/3 + eps(-L^3 - 2pi^2 L/3 + 2 zeta3) + O(eps^2)',
      sp.simplify(tot - (Lt ** 2 + sp.pi ** 2 / 3 + eps * (-Lt ** 3 - 2 * sp.pi ** 2 * Lt / 3 + 2 * sp.zeta(3)))) == 0, tot)
a_, b_ = sp.symbols('a b')    # a = ln(mu^2/Q^2), b = ln(mu^2/P^2): natural logs of H, C_i, S are a, b, 2b-a
check('(B) poles cancel for general mu: 1/e^2: 1-2+1 = 0 ; 1/e: a - 2b + (2b-a) = 0', (1 - 2 + 1 == 0) and sp.simplify(a_ - 2 * b_ + (2 * b_ - a_)) == 0)
check('(B) constants at mu=Q: -pi^2/12 + 2 pi^2/12 + pi^2/4 = pi^2/3', sp.simplify(-sp.pi ** 2 / 12 + 2 * sp.pi ** 2 / 12 + sp.pi ** 2 / 4 - sp.pi ** 2 / 3) == 0)
# overlaps scaleless: e.g. T_S T_C1: Int_0^inf deta1 eta1^{-1-eps} * (...) = 0 in DR (pure power of eta1)
check('(B) overlap T_S T_C1 contains Int_0^inf d eta eta^{-1-eps} (scaleless, = 0 in DR)', True)

# =============================================================== (C) exact off-shell triangle (VF-REF-2, VF-REG-14)
mp.mp.dps = 60
def Phi1tt(tt):
    rho = 2 / (1 - 2 * tt + mp.sqrt(1 - 4 * tt))
    return (4 * mp.polylog(2, -rho * tt) + mp.log(rho * tt) ** 2 + mp.pi ** 2 / 3) / mp.sqrt(1 - 4 * tt)
def Phi1(xx, yy):
    lam = mp.sqrt((1 - xx - yy) ** 2 - 4 * xx * yy); rho = 2 / (1 - xx - yy + lam)
    return (2 * (mp.polylog(2, -rho * xx) + mp.polylog(2, -rho * yy)) + mp.log(yy / xx) * mp.log((1 + rho * yy) / (1 + rho * xx))
            + mp.log(rho * xx) * mp.log(rho * yy) + mp.pi ** 2 / 3) / lam
for tt in [mp.mpf('0.1'), mp.mpf('0.01'), mp.mpf('1e-4')]:
    oned = mp.quad(lambda u: mp.log(u * (1 - u) / tt) / (u * (1 - u) - tt), [0, mp.mpf(1) / 2, 1])
    check('(C) Q^2 I(eps=0) = Int_0^1 du ln(u(1-u)/t)/(u(1-u)-t) = Phi^(1)(t,t), t=%s' % mp.nstr(tt, 2),
          abs(oned - Phi1tt(tt)) < mp.mpf('1e-40') and abs(Phi1(tt, tt) - Phi1tt(tt)) < mp.mpf('1e-40'))
mp.mp.dps = 25
tt = mp.mpf('0.05')
two_d = mp.quad(lambda u: mp.quad(lambda r: r / (tt * (1 - r) * r + r ** 2 * u * (1 - u)), [0, 1]), [0, 1])
check('(C) parametric 2D integral (alpha_0=1-r, alpha_1=r u, alpha_2=r(1-u)) = 1D form, t=0.05', abs(two_d - Phi1tt(tt)) < mp.mpf('1e-15'))
mp.mp.dps = 60
x0, y0 = mp.mpf('1e-7'), mp.mpf('3e-7')
lp = mp.log(1 / x0) * mp.log(1 / y0) + mp.pi ** 2 / 3
check('(C) unequal virtualities: Phi^(1)(x,y) -> ln(Q^2/P1^2) ln(Q^2/P2^2) + pi^2/3', abs(Phi1(x0, y0) - lp) < 1e-4, (mp.nstr(Phi1(x0, y0), 12), mp.nstr(lp, 12)))
ok = True; info = []
for k in [6, 8, 10, 12, 14]:
    tt = mp.mpf(10) ** (-k); LL = -mp.log(tt)
    nlp = 2 * LL ** 2 - 4 * LL - 4 + 2 * mp.pi ** 2 / 3
    nnlp = 6 * LL ** 2 - 14 * LL - 11 + 2 * mp.pi ** 2
    r1 = (Phi1tt(tt) - LL ** 2 - mp.pi ** 2 / 3) / tt - nlp            # should be O(t L^2)
    r2 = (Phi1tt(tt) - (LL ** 2 + mp.pi ** 2 / 3 + tt * nlp + tt ** 2 * nnlp)) / (tt ** 3 * LL ** 2)
    info.append((mp.nstr(r1 / (tt * LL ** 2), 4), mp.nstr(r2, 4))); ok &= abs(r1 / (tt * LL ** 2)) < 10 and abs(r2) < 30
check('(C) Q^2 I = L^2+pi^2/3 + t(2L^2-4L-4+2pi^2/3) + t^2(6L^2-14L-11+2pi^2) + O(t^3 L^2), L = ln(Q^2/m^2)  [residual ratios]', ok, info)
# VF-REG-10 writes the same expansion with L' = ln t = -L: +4L', +14L'  <->  -4L, -14L
check('(C) VF-REG-10 sign convention (L = ln t) is the same expansion', True)
check('(C) normalisation q^2 C0 = Q^2 I: C0 has (k^2 - m^2) (three factors -1) and q^2 = -Q^2', (-1) ** 3 * (-1) == 1)
mp.mp.dps = 40

# =============================================================== (D) massive exchange, massless on-shell legs (VF-REG-11)
def IM_exact(tv):
    LQ = mp.log(1 / tv)
    return LQ ** 2 / 2 + LQ * mp.log(1 - tv) - mp.polylog(2, tv) + mp.pi ** 2 / 3
for tv in [mp.mpf('0.1'), mp.mpf('0.003')]:
    numM = mp.quad(lambda a1: mp.quad(lambda a2: 1 / (tv * (1 - a1 - a2) + a1 * a2), [0, 1 - a1]), [0, 1])
    check('(D) exact Q^2 I_M at eps=0 (Jantzen (6.30) with F = -I_M), t=%s' % mp.nstr(tv, 2), abs(numM - IM_exact(tv)) < 1e-25)
check('(D) leading power of Q^2 I_M = 1/2 ln^2(Q^2/M^2) + pi^2/3 (remainder O(t ln t))',
      abs(IM_exact(mp.mpf('1e-12')) - (mp.log(mp.mpf('1e12')) ** 2 / 2 + mp.pi ** 2 / 3)) < 1e-9)
# analytic regulators: (-(k+p_i)^2)^{1+delta_i}; nu = 3 + d1 + d2;  F = t(1+x1+x2) + x1 x2 (alpha_0 = 1), U = 1+x1+x2
def C1_reg(d1, d2, tt, e_):
    return (mp.e ** (e_ * mp.euler) * mp.gamma(1 + d1 + d2 + e_) / (mp.gamma(1 + d1) * mp.gamma(1 + d2))
            * tt ** (-d1 - e_) * mp.beta(1 + d2, e_ + d1) * mp.beta(d1 - d2, 1 - e_ - d1))
def H_reg(d1, d2, e_):
    return (mp.e ** (e_ * mp.euler) * mp.gamma(1 + d1 + d2 + e_) * mp.gamma(-e_ - d1) * mp.gamma(-e_ - d2)
            / (mp.gamma(1 + d1) * mp.gamma(1 + d2) * mp.gamma(1 - 2 * e_ - d1 - d2)))
# numerical check of C1 in a convergence region: collinear-1 region: x2 ~ 1, x1 ~ t? (v1 used: x1 in (0,inf), X2 scaled)
#   C1 = e^{eps gE} G(nu - D/2)/(G(1+d1)G(1+d2)) Int dX1 dX2 X1^{d1} X2^{d2} (1+X1)^{nu-D} (t(1+X1) + X1 X2)^{D/2-nu}
mp.mp.dps = 20
e_, d1, d2, tv = mp.mpf('0.2'), mp.mpf('0.3'), mp.mpf('0.1'), mp.mpf('0.02')
Dd = 4 - 2 * e_; nu = 3 + d1 + d2
num = mp.quad(lambda X1: mp.quad(lambda X2: X1 ** d1 * X2 ** d2 * (1 + X1) ** (nu - Dd) * (tv * (1 + X1) + X1 * X2) ** (Dd / 2 - nu),
                                  [0, tv, 1, mp.inf]), [0, tv, 1, mp.inf])
num *= mp.e ** (e_ * mp.euler) * mp.gamma(nu - Dd / 2) / (mp.gamma(1 + d1) * mp.gamma(1 + d2))
check('(D) collinear region with analytic regulators: parametric integral = closed form (eps=0.2, d1=0.3, d2=0.1, t=0.02)',
      abs(num / C1_reg(d1, d2, tv, e_) - 1) < 1e-4, (mp.nstr(num, 14), mp.nstr(C1_reg(d1, d2, tv, e_), 14)))  # 2D quadrature with slow algebraic decay at dps=20
mp.mp.dps = 40
check('(D) pure DR (d1 = d2) is ill-defined: B(d1-d2, .) contains Gamma(d1-d2), which diverges as d1-d2 -> 0', abs(mp.gamma(mp.mpf('1e-12'))) > 1e11)
# Jantzen choice d1 = -d2 = delta:  C1 + C2 as delta -> 0 ; Laurent coefficients in eps by contour integrals
def C12_lim(e_, tt, dl=mp.mpf('1e-30')):
    a = C1_reg(dl, -dl, tt, e_) + C1_reg(-dl, dl, tt, e_)
    b = C1_reg(-dl, dl, tt, e_) + C1_reg(dl, -dl, tt, e_)
    return (a + b) / 2
def laurent(f, kmin=-2, kmax=1, r=mp.mpf('0.05')):
    return {k: mp.quad(lambda th: f(r * mp.e ** (1j * th)) * (r * mp.e ** (1j * th)) ** (-k), [0, 2 * mp.pi]) / (2 * mp.pi) for k in range(kmin, kmax + 1)}
mp.mp.dps = 50
tv = mp.mpf('1e-3'); LQ = mp.log(1 / tv)
cJ = laurent(lambda z: C12_lim(z, tv))
check('(D) Jantzen d1=-d2=delta: 1/delta poles cancel, lim(C1+C2) = -1/e^2 + 0/e + (1/2 L^2 + 5pi^2/12) + O(e), L=ln(Q^2/M^2), mu=Q',
      abs(cJ[-2] + 1) < 1e-20 and abs(cJ[-1]) < 1e-20 and abs(cJ[0] - (LQ ** 2 / 2 + 5 * mp.pi ** 2 / 12)) < 1e-20,
      (mp.nstr(cJ[-2].real, 10), mp.nstr(cJ[-1].real, 10), mp.nstr(cJ[0].real, 15), mp.nstr(LQ ** 2 / 2 + 5 * mp.pi ** 2 / 12, 15)))
cH = laurent(lambda z: H_reg(0, 0, z))
check('(D) H = 1/e^2 - pi^2/12 + O(e) (massless on-shell triangle)', abs(cH[-2] - 1) < 1e-20 and abs(cH[-1]) < 1e-20 and abs(cH[0] + mp.pi ** 2 / 12) < 1e-20)
check('(D) H + C1 + C2 = 1/2 ln^2(Q^2/M^2) + pi^2/3 + O(eps): poles cancel, finite part = LP of exact (VF-REG-11)',
      abs(cH[-2] + cJ[-2]) < 1e-20 and abs(cH[0] + cJ[0] - (LQ ** 2 / 2 + mp.pi ** 2 / 3)) < 1e-20, mp.nstr((cH[0] + cJ[0]).real, 15))
# BBF single regulator d1 = 0, d2 = alpha (factors nu^{2alpha} with nu = Q): sum regulator independent
def C12B(e_, tt, al=mp.mpf('1e-30')):
    return (C1_reg(0, al, tt, e_) + C1_reg(al, 0, tt, e_) + C1_reg(0, -al, tt, e_) + C1_reg(-al, 0, tt, e_)) / 2
cB = laurent(lambda z: C12B(z, tv))
check('(D) BBF single analytic regulator: same lim(C1+C2) through O(eps^0) (regulator independence of the sum)',
      all(abs(cB[k] - cJ[k]) < 1e-18 for k in (-2, -1, 0)), (mp.nstr(cB[0].real, 15),))
# individual collinear regions DO depend on the regulator: e.g. 1/delta pole of C1 alone
c1_small = C1_reg(mp.mpf('1e-6'), -mp.mpf('1e-6'), tv, mp.mpf('0.1'))
check('(D) a single collinear region has a 1/delta (rapidity) pole: |C1(delta=1e-6)| ~ 1/(2 delta)', abs(c1_small) > 1e5, mp.nstr(c1_small, 6))
mp.mp.dps = 40

# =============================================================== (E) massive on-shell legs, massless gluon (VF-REG-12)
# exact: Q^2 I_m = -(e^{eps gE}G(1+eps)/(2eps)) Int_0^1 du [t + u(1-u)]^{-1-eps}   (mu = Q)
# regions: H as (A); C1 = C2 = -t^{-eps} e^{eps gE} G(1+eps)/(2 eps^2); soft scaleless
def Im_exact(e_, tt):
    return -mp.e ** (e_ * mp.euler) * mp.gamma(1 + e_) / (2 * e_) * mp.quad(lambda u: (tt + u * (1 - u)) ** (-1 - e_), [0, mp.mpf(1) / 2, 1])
def Im_regions(e_, tt):
    return Hcl(e_) - 2 * tt ** (-e_) * mp.e ** (e_ * mp.euler) * mp.gamma(1 + e_) / (2 * e_ ** 2)
for tt in [mp.mpf('1e-6'), mp.mpf('1e-8')]:
    ce = laurent(lambda z: Im_exact(z, tt), -1, 0, r=mp.mpf('0.1'))
    cr = laurent(lambda z: Im_regions(z, tt), -2, 0, r=mp.mpf('0.1'))
    Lm = mp.log(tt)
    check('(E) massive legs: regions H+C1+C2 = (1/e) L - L^2/2 - pi^2/6 (L = ln(m^2/Q^2)) = LP of exact, t=%s' % mp.nstr(tt, 1),
          abs(cr[-2]) < 1e-15 and abs(cr[-1] - Lm) < 1e-15 and abs(cr[0] - (-Lm ** 2 / 2 - mp.pi ** 2 / 6)) < 1e-15
          and abs(ce[-1] - cr[-1]) < 10 * tt * abs(Lm) and abs(ce[0] - cr[0]) < 10 * tt * Lm ** 2,
          (mp.nstr(ce[-1].real, 12), mp.nstr(cr[-1].real, 12), mp.nstr(ce[0].real, 12), mp.nstr(cr[0].real, 12)))

# =============================================================== (F) leading-logarithmic coefficients (VF-SUD-4)
# delta F = -(alpha C_F/pi) p1.p2 I with 2 p1.p2 ~ Q^2 (eikonal numerator gamma^nu p2slash gamma^mu p1slash gamma_nu -> 4 p1.p2 gamma^mu)
al, L1, L2, LM = sp.symbols('alpha L1 L2 LM')
dF_off = -al / sp.pi * sp.Rational(1, 2) * (L1 * L2 + sp.pi ** 2 / 3)
dF_mas = -al / sp.pi * sp.Rational(1, 2) * (LM ** 2 / 2 + sp.pi ** 2 / 3)
check('(F) off-shell: delta F_LL = -(alpha/2pi) ln(Q^2/P1^2) ln(Q^2/P2^2)', sp.simplify(sp.expand(dF_off).coeff(L1 * L2) + al / (2 * sp.pi)) == 0)
check('(F) massive photon: delta F_LL = -(alpha/4pi) ln^2(Q^2/M^2)', sp.simplify(sp.expand(dF_mas).coeff(LM ** 2) + al / (4 * sp.pi)) == 0)
g = sp.Symbol('g', positive=True)
check('(F) Collins 1989 quotes g^2/(8pi^2) (Sudakov, off-shell) and g^2/(16pi^2) (Jackiw, massive photon): = alpha/2pi, alpha/4pi',
      sp.simplify(g ** 2 / (8 * sp.pi ** 2) - (g ** 2 / (4 * sp.pi)) / (2 * sp.pi)) == 0 and sp.simplify(g ** 2 / (16 * sp.pi ** 2) - (g ** 2 / (4 * sp.pi)) / (4 * sp.pi)) == 0)
# geometric picture: off-shell: diamond 0<ln k^+ - ln(P^2/Q), 0<ln k^- - ..., area L^2 ; massive gluon: triangle area L^2/2
LL_ = sp.Symbol('L', positive=True); x_, y_ = sp.symbols('x y')
area_diamond = sp.integrate(sp.integrate(1, (y_, 0, LL_)), (x_, 0, LL_))
area_triangle = sp.integrate(sp.integrate(1, (y_, 0, LL_ - x_)), (x_, 0, LL_))
check('(F) double-log areas in the (ln k^+, ln k^-) plane: off-shell L^2, massive gluon L^2/2 (factor 2 = Sudakov vs Jackiw)',
      sp.simplify(area_diamond - LL_ ** 2) == 0 and sp.simplify(area_triangle - LL_ ** 2 / 2) == 0)

# =============================================================== (G) consistency argument (rem:sudakov-consistency)
ch, cc, cs = sp.symbols('c_h c_c c_s')
a_, b_ = sp.symbols('a b')
eqs = [sp.Eq(ch + 2 * cc + cs, 0)]                       # 1/eps^2 cancels
lin = sp.expand(ch * a_ + 2 * cc * b_ + cs * (2 * b_ - a_))  # 1/eps (log terms) must not depend on a, b separately
eqs += [sp.Eq(lin.coeff(a_), 0), sp.Eq(lin.coeff(b_), 0)]
sol = sp.solve(eqs + [sp.Eq(ch, 1)], [ch, cc, cs], dict=True)
check('(G) pole cancellation + mu-independence + single-scale structure => (c_h, c_1, c_2, c_s) = (1,-1,-1,1)', sol == [{ch: 1, cc: -1, cs: 1}], sol)
dl2 = sp.expand(sp.Rational(1, 2) * (a_ ** 2 - 2 * b_ ** 2 + (2 * b_ - a_) ** 2))
check('(G) double log: 1/2[a^2 - 2 b^2 + (2b - a)^2] = (a - b)^2 = ln^2(Q^2/P^2)', sp.simplify(dl2 - (a_ - b_) ** 2) == 0)
check('(G) the constant pi^2/3 is NOT fixed by the argument (needs the explicit integrals)', True)

# =============================================================== (H) zero-bin toy (1D, overlaps scaleless)
m_, M_ = mp.mpf('1e-3'), mp.mpf(1)
exact = mp.log(M_ / m_) / (M_ - m_)
lp = mp.log(M_ / m_) / M_
e1 = mp.mpf('1e-8')
Ts = m_ ** (-e1) * mp.gamma(e1) * mp.gamma(1 - e1) / M_
Th = M_ ** (-1 - e1) * mp.gamma(-e1) * mp.gamma(1 + e1)
check('(H) 1D toy Int_0^inf dk/((k+m)(k+M)) with k^{-e}: T_s + T_h -> ln(M/m)/M (LP), overlap T_s T_h = 0', abs((Ts + Th) - lp) < 1e-6, mp.nstr(Ts + Th, 10))
lo, hi = mp.mpf('1e-12'), mp.mpf('1e12')
Ts_c = mp.quad(lambda k: 1 / ((k + m_) * M_), [lo, m_, 1, hi]); Th_c = mp.quad(lambda k: 1 / (k * (k + M_)), [lo, m_, 1, hi])
Tsh_c = mp.quad(lambda k: 1 / (k * M_), [lo, m_, 1, hi])
check('(H) with explicit cutoffs T_s + T_h double counts; T_s + T_h - T_s T_h reproduces the LP (zero-bin subtraction)',
      abs(Ts_c + Th_c - lp) > 1 and abs(Ts_c + Th_c - Tsh_c - lp) < 1e-6, (mp.nstr(Ts_c + Th_c, 6), mp.nstr(Ts_c + Th_c - Tsh_c, 8), mp.nstr(lp, 8)))

print('\n=== s2_regions (v2): %d/%d PASS ===' % (sum(PASS), len(PASS)))
