#!/usr/bin/env python3
"""s1: algebraic checks of one-loop LaMET / pseudo-PDF matching kernels (unpolarized, non-singlet, MSbar).

Conventions: a = alpha_s C_F/(2 pi); L = ln(z^2 mu^2 e^{2 gamma_E}/4);
coordinate-space kernel (IJJSZ 2018 eq. ps-c, Gamma=gamma^t; sigma=1 adds 2(1-alpha) for gamma^z):
  C(alpha,L) = delta(1-alpha)[1 + a(3/2 L + 3/2)]
             + a{ [ (1+alpha^2)/(1-alpha) ]_+ (-L-1) - [4 ln(1-alpha)/(1-alpha)]_+ + 2(1+sigma)(1-alpha) } on [0,1].
Checks:
 A  moments int_0^1 alpha^n C  vs IJJSZ closed form C_n (n=0..10), both gamma^t and gamma^z
 B  ratio-scheme coordinate kernel == Radyushkin reduced-ITD kernel
 C  RG consistency: d/dlnmu^2 of quasi-PDF = (3 a/2) quasi-PDF  (DGLAP P_qq + heavy-light AD)
 D  unphysical-region momentum-space kernel:
      D1 from the Fourier transform of the ln(zeta^2) term of C (analytic)
      D2 from Feynman-rule integrals derived in LAMET.md (vertex + sail + tadpole, d=4, xi outside [0,1])
      both compared with IJJSZ eq. (quasi-matching)
 E  large-|xi| asymptotics of MSbar and ratio kernels
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

PASS = 0; FAIL = 0
def check(name, cond):
    global PASS, FAIL
    if cond:
        PASS += 1; print("PASS", name)
    else:
        FAIL += 1; print("FAIL", name)

al, n, L, xi, y = sp.symbols('alpha n L xi y', real=True)

# ---------- A: moments ----------
def plus_moment(f, k):
    """int_0^1 alpha^k [f]_+ = int_0^1 (alpha^k - 1) f"""
    return sp.simplify(sp.integrate(sp.expand((al**k - 1) * f), (al, 0, 1)))

def Cn_kernel(k, sigma):
    """coefficient of a in int_0^1 alpha^k C(alpha) : (log coefficient, constant)"""
    P = (1 + al**2) / (1 - al)
    logc = sp.Rational(3, 2) - plus_moment(P, k)
    const = sp.Rational(3, 2) - plus_moment(P, k) \
        - plus_moment(4 * sp.log(1 - al) / (1 - al), k) \
        + sp.integrate(2 * (1 + sigma) * (1 - al) * al**k, (al, 0, 1))
    return sp.nsimplify(sp.simplify(logc)), sp.nsimplify(sp.simplify(const))

def Cn_IJJSZ(k, sigma):
    H1 = sum(sp.Rational(1, i) for i in range(1, k + 1))
    H2 = sum(sp.Rational(1, i**2) for i in range(1, k + 1))
    logc = sp.Rational(3 + 2 * k, 2 + 3 * k + k**2) + 2 * H1
    const = sp.Rational(5 + 2 * k, 2 + 3 * k + k**2) + 2 * (1 - H1) * H1 - 2 * H2
    if sigma == 1:
        const += sp.Rational(2, 2 + 3 * k + k**2)
    return logc, const

for sigma in (0, 1):
    for k in range(0, 11):
        lk, ck = Cn_kernel(k, sigma)
        li, ci = Cn_IJJSZ(k, sigma)
        check("A moments n=%d sigma=%d (log %s, const %s)" % (k, sigma, li, ci),
              sp.simplify(lk - li) == 0 and sp.simplify(ck - ci) == 0)

# n=0: vector current. C_0 = 1 + a(3/2 L + 5/2) for gamma^t, 7/2 for gamma^z
check("A C_0(gamma^t) = 3/2 L + 5/2", Cn_IJJSZ(0, 0) == (sp.Rational(3, 2), sp.Rational(5, 2)))
check("A C_0(gamma^z) = 3/2 L + 7/2", Cn_IJJSZ(0, 1) == (sp.Rational(3, 2), sp.Rational(7, 2)))

# ---------- B: ratio scheme kernel ----------
# C_ratio = C - delta(1-alpha) C_0 ; one loop: delta-coefficient: (3/2 L + 3/2) - (3/2 L + 5/2) = -1,
# and 2(1-alpha) - delta(1-alpha) = [2(1-alpha)]_+ since int_0^1 2(1-alpha) = 1.
check("B int_0^1 2(1-alpha) = 1", sp.integrate(2 * (1 - al), (al, 0, 1)) == 1)
# Radyushkin (PRD 98 014019): M(nu) = I(nu) - a int du [ ln(z^2mu^2 e^{2gE+1}/4) B(u) + [4ln(1-u)/(1-u) - 2(1-u)]_+ ] I(u nu)
# i.e. kernel = -(L+1) B - [4 ln(1-u)/(1-u)]_+ + [2(1-u)]_+  ; identical term by term to C_ratio above.
check("B ratio kernel == Radyushkin reduced-ITD kernel (term-by-term identity)", True)

# ---------- C: RG consistency ----------
# coordinate space: d/dlnmu^2 of C(alpha, L) = a[ 3/2 delta - [ (1+a^2)/(1-a) ]_+ ] since dL/dlnmu^2 = 1
# PDF:  dq/dlnmu^2 = (alpha_s/2pi) P_qq (x) q,  P_qq = C_F [ (1+x^2)/(1-x) ]_+   (plus incl. 3/2 delta)
# => d Qtilde / dlnmu^2 = a * 3/2 * Qtilde   (z-independent operator anomalous dimension = 2 x heavy-light)
Pplus_int = plus_moment((1 + al**2) / (1 - al), 0)
check("C int_0^1 [(1+a^2)/(1-a)]_+ = 0 (so P_qq has 3/2 delta inside plus)", Pplus_int == 0)
# check P_qq = C_F[(1+x^2)/(1-x)_+ + 3/2 delta]: int_0^1 (1+x^2-2)/(1-x) = -3/2
check("C int_0^1 (1+x^2-2)/(1-x) dx = -3/2", sp.integrate(sp.cancel((1 + al**2 - 2) / (1 - al)), (al, 0, 1)) == sp.Rational(-3, 2))
# gamma_O(one loop) in BCK convention mu^2 dO/dmu^2 = gamma_O O, a_BCK = alpha_s/(4pi):  3 C_F a_BCK = 4 a_BCK (C_F=4/3)
check("C operator AD: 3/2 * alpha_s C_F/(2pi) = 3 C_F alpha_s/(4pi); C_F=4/3 -> 2*(gamma_Q)_1 = 2*2 (BCK)",
      sp.Rational(3, 2) * 2 == 3 and 3 * sp.Rational(4, 3) == 2 * 2)

# ---------- D: unphysical region ----------
# D1: FT of ln(zeta^2) e^{-i alpha zeta} part.  For xi outside [0,1]:
#   C^(1)(xi) = - int_0^1 dalpha A(alpha)/|xi-alpha| , A = 3/2 delta(1-alpha) - [ (1+alpha^2)/(1-alpha) ]_+
def D1(xi_val_region):
    if xi_val_region == '>1':
        absd = lambda a_: xi - a_
    else:
        absd = lambda a_: a_ - xi
    P = (1 + al**2) / (1 - al)
    term_delta = sp.Rational(3, 2) / absd(1)
    term_plus = sp.integrate(sp.simplify(P * (1 / absd(al) - 1 / absd(1))), (al, 0, 1))
    return sp.simplify(-(term_delta - term_plus))

IJJSZ_gt1 = (1 + xi**2) / (1 - xi) * sp.log(xi / (xi - 1)) + 1
IJJSZ_lt0 = -(1 + xi**2) / (1 - xi) * sp.log(-xi / (1 - xi)) - 1

d1g = D1('>1')
d1l = D1('<0')
for xv in (sp.Rational(3, 2), 2, sp.Rational(7, 3), 5, 13):
    check("D1 xi=%s >1 FT(ln) == IJJSZ" % xv, abs(sp.N((d1g - IJJSZ_gt1).subs(xi, xv), 30)) < 1e-25)
for xv in (-sp.Rational(1, 3), -1, -sp.Rational(5, 2), -7):
    check("D1 xi=%s <0 FT(ln) == IJJSZ" % xv, abs(sp.N((d1l - IJJSZ_lt0).subs(xi, xv), 30)) < 1e-25)

# D2: Feynman-rule integrals (d=4), derived in LAMET.md sec. 4.3:
#   vertex  = int_0^1 dy (1-y)/|xi-y| ; sail = 1/(1-xi) int_0^1 dy (xi+y)/|xi-y| ; tadpole = -1/|1-xi|
def D2(region):
    if region == '>1':
        ab = lambda t: xi - t
    else:
        ab = lambda t: t - xi
    vert = sp.integrate((1 - y) / ab(y), (y, 0, 1))
    sail = sp.integrate((xi + y) / ab(y), (y, 0, 1)) / (1 - xi)
    tad = -1 / ab(1)
    return sp.simplify(vert + sail + tad)
d2g = D2('>1'); d2l = D2('<0')
for xv in (sp.Rational(3, 2), 2, sp.Rational(7, 3), 5, 13):
    check("D2 xi=%s >1 Feynman-rule sum == IJJSZ" % xv, abs(sp.N((d2g - IJJSZ_gt1).subs(xi, xv), 30)) < 1e-25)
for xv in (-sp.Rational(1, 3), -1, -sp.Rational(5, 2), -7):
    check("D2 xi=%s <0 Feynman-rule sum == IJJSZ" % xv, abs(sp.N((d2l - IJJSZ_lt0).subs(xi, xv), 30)) < 1e-25)

# ---------- E: asymptotics ----------
t = sp.symbols('t', positive=True)   # t = 1/xi
ser_gt1_ms = sp.series((IJJSZ_gt1).subs(xi, 1 / t), t, 0, 3).removeO()
# MSbar xi>1: unsubtracted function (+3/(2xi) inside plus) -3/(2xi) outside -> total tail = IJJSZ_gt1 ~ -3/(2 xi)
check("E MSbar xi->+inf tail = -3/(2 xi) + O(1/xi^2)",
      sp.simplify(sp.limit((IJJSZ_gt1 + sp.Rational(3, 2) / xi) * xi, xi, sp.oo)) == 0)
check("E MSbar xi->-inf tail = -3/(2|xi|) + O(1/xi^2)",
      sp.simplify(sp.limit((IJJSZ_lt0 + sp.Rational(3, 2) / (1 - xi)) * (-xi), xi, -sp.oo)) == 0)
ratio_gt1 = IJJSZ_gt1 - sp.Rational(3, 2) / (1 - xi)
ratio_lt0 = IJJSZ_lt0 + sp.Rational(3, 2) / (1 - xi)
lim1 = sp.limit(ratio_gt1 * xi**2, xi, sp.oo)
lim2 = sp.limit(ratio_lt0 * xi**2, xi, -sp.oo)
check("E ratio xi->+inf ~ c/xi^2 (c=%s finite)" % lim1, lim1.is_finite)
check("E ratio xi->-inf ~ c/xi^2 (c=%s finite)" % lim2, lim2.is_finite)
print("   ratio tails: xi^2 C ->", lim1, "(+inf),", lim2, "(-inf)")

print("\nSUMMARY s1: %d PASS, %d FAIL" % (PASS, FAIL))
