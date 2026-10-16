#!/usr/bin/env python3
"""N09 independent check: large-|xi| tails of the one-loop quasi-PDF kernels and the small-y domain of the convolution.

Kernels as printed in IJJSZ arXiv:1801.03917 eqs. (quasi-matching), (quasi-matching-alt) (read in the arXiv source),
hybrid kernel as printed in Ji et al. arXiv:2008.03886 eq. (hybridm2) with lambda_S = z_S p^z, p^z = parton momentum.
Work with a = 1 (alpha_s C_F/(2 pi) factored out).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

res = []
def rep(name, ok, extra=""):
    ok = bool(ok); res.append(ok)
    print(("PASS " if ok else "FAIL ") + name + ((" : " + extra) if extra else ""))

xi = sp.symbols('xi')
w = sp.symbols('w', positive=True)    # w = 1/|xi|
# functions for xi>1 and xi<0 (outside the plus prescriptions; the subtraction at xi=1 does not affect the tails)
CMS_pos = (1+xi**2)/(1-xi)*sp.log(xi/(xi-1)) + 1           # = [..+3/(2xi)] - 3/(2xi)
CMS_neg = -(1+xi**2)/(1-xi)*sp.log(-xi/(1-xi)) - 1         # = [..+3/(2(1-xi))] - 3/(2(1-xi))
CR_pos = (1+xi**2)/(1-xi)*sp.log(xi/(xi-1)) + 1 - sp.Rational(3, 2)/(1-xi)
CR_neg = -(1+xi**2)/(1-xi)*sp.log(-xi/(1-xi)) - 1 + sp.Rational(3, 2)/(1-xi)
def tail(expr, sign):
    e = sp.simplify(expr.subs(xi, sign/w))
    return sp.series(e, w, 0, 4).removeO()
t1 = tail(CMS_pos, 1); t2 = tail(CMS_neg, -1); t3 = tail(CR_pos, 1); t4 = tail(CR_neg, -1)
print("   C_MS(xi->+inf) =", sp.expand(t1), "  [w = 1/|xi|]")
print("   C_MS(xi->-inf) =", sp.expand(t2))
print("   C_ratio(xi->+inf) =", sp.expand(t3))
print("   C_ratio(xi->-inf) =", sp.expand(t4))
rep("MSbar tail -> -3/(2|xi|) at xi->+inf", sp.simplify(t1.coeff(w, 1) + sp.Rational(3, 2)) == 0 and t1.coeff(w, 0) == 0)
rep("MSbar tail -> -3/(2|xi|) at xi->-inf", sp.simplify(t2.coeff(w, 1) + sp.Rational(3, 2)) == 0 and t2.coeff(w, 0) == 0)
rep("MSbar next term: -17/(6 xi^2) (+inf), +17/(6 xi^2) (-inf)", sp.simplify(t1.coeff(w, 2) + sp.Rational(17, 6)) == 0 and sp.simplify(t2.coeff(w, 2) - sp.Rational(17, 6)) == 0)
rep("ratio tail -> -4/(3 xi^2) at +inf (no 1/xi term)", t3.coeff(w, 1) == 0 and sp.simplify(t3.coeff(w, 2) + sp.Rational(4, 3)) == 0)
rep("ratio tail -> +4/(3 xi^2) at -inf (no 1/xi term)", t4.coeff(w, 1) == 0 and sp.simplify(t4.coeff(w, 2) - sp.Rational(4, 3)) == 0)
# independent route: coordinate kernel; tail of ratio kernel = coefficient int_0^1 alpha B(alpha) = int (1+a^2)(a-1)/(1-a) = -4/3
al = sp.symbols('alpha')
rep("coordinate route: int_0^1 alpha [(1+a^2)/(1-a)]_+ da = -4/3", sp.integrate(-(1+al**2), (al, 0, 1)) == sp.Rational(-4, 3))

# ---- small-y behaviour of the convolution int dy/|y| C(x/y) f(y) ----
mp.mp.dps = 30
def CMS(x):
    x = mp.mpf(x)
    if x > 1:  return (1+x**2)/(1-x)*mp.log(x/(x-1)) + 1
    if x < 0:  return -(1+x**2)/(1-x)*mp.log(-x/(1-x)) - 1
    raise ValueError
def CR(x):
    x = mp.mpf(x)
    if x > 1:  return CMS(x) - mp.mpf(3)/(2*(1-x))
    if x < 0:  return CMS(x) + mp.mpf(3)/(2*(1-x))
    raise ValueError
def Chyb(x, lamS):     # ratio + (3/2)[-1/|1-xi| + 2 Si((1-xi) lamS)/(pi (1-xi))], away from xi = 1
    x = mp.mpf(x); u = 1-x
    return CR(x) + mp.mpf(3)/2*(-1/abs(u) + 2*mp.si(u*lamS)/(mp.pi*u))
x0 = mp.mpf('0.3'); Lam = mp.mpf(3)      # Lam = z_S P^z (hadron); lambda_S = Lam*|y| (parton momentum |y|P^z)
def partial(kernel, f, eps, ymax=None, neg=False):
    ymax = ymax or x0/4
    if not neg:
        return mp.quad(lambda y: kernel(x0/y, y)/y*f(y), [eps, eps*10, eps*100, ymax])
    return mp.quad(lambda t: kernel(-x0/t, t)/t*f(-t), [eps, eps*10, eps*100, ymax])   # y = -t
kMS = lambda xi_, y: CMS(xi_)
kR = lambda xi_, y: CR(xi_)
kH = lambda xi_, y: Chyb(xi_, Lam*abs(y))
f0 = lambda y: 1/abs(y)                  # Regge-like, delta = 0 (one sign only: quark, no antiquark)
print("   f(y) = 1/y on (0, x/4], x = 0.3, z_S P^z = 3:")
vals = {}
for name, k in [('MSbar', kMS), ('ratio', kR), ('hybrid', kH)]:
    vals[name] = [partial(k, f0, mp.mpf(10)**(-n)) for n in (3, 5, 7)]
    print("     %-6s partial integrals eps=1e-3,1e-5,1e-7:" % name, [mp.nstr(v, 10) for v in vals[name]])
slopeMS = (vals['MSbar'][2]-vals['MSbar'][1])/mp.log(100)
slopeH = (vals['hybrid'][2]-vals['hybrid'][1])/mp.log(100)
predMS = -mp.mpf(3)/(2*x0)
predH = mp.mpf(3)/(2*x0)*(2/mp.pi*mp.si(x0*Lam) - 1)
rep("MSbar: log-divergent with slope -3/(2x) per unit ln(1/eps)", abs(slopeMS-predMS) < 1e-4, "%s vs %s" % (mp.nstr(slopeMS, 8), mp.nstr(predMS, 8)))
d1 = vals['ratio'][1]-vals['ratio'][0]; d2 = vals['ratio'][2]-vals['ratio'][1]
rep("ratio: converges (successive differences shrink ~ eps, tail integrand -> -4/(3x^2) const)", abs(d2/d1) < 0.02 and abs(d2 - (-4/(3*x0**2))*(mp.mpf('1e-5')-mp.mpf('1e-7'))) < 1e-6,
    "d(1e-3->1e-5)=%s, d(1e-5->1e-7)=%s" % (mp.nstr(d1, 4), mp.nstr(d2, 4)))
rep("hybrid: log-divergent too, slope (3/(2x))[(2/pi)Si(x z_S P^z) - 1]  (contradicts 'ratio/hybrid need only int|yf|')",
    abs(slopeH-predH) < 1e-4 and abs(predH) > 0.1, "%s vs %s" % (mp.nstr(slopeH, 8), mp.nstr(predH, 8)))
for L_ in ['1', '3', '10', '30']:
    print("     coefficient [1 - (2/pi)Si(x z_S P^z)] at x z_S P^z = %s: %s" % (L_, mp.nstr(1-2/mp.pi*mp.si(mp.mpf(L_)), 6)))

# physical quark + antiquark: f(y) = q(y) (y>0), -qbar(|y|) (y<0), with q = qbar ~ y^{-1-delta} (C-even sea, strange-like)
delta = mp.mpf('0.3')
fq = lambda y: y**(-1-delta)
print("   C-even sea q = qbar = y^(-1.3):")
for name, k in [('MSbar', kMS), ('hybrid', kH), ('ratio', kR)]:
    seq = []
    for n in (3, 5, 7):
        e = mp.mpf(10)**(-n)
        Iq = partial(k, fq, e)                                   # quark part, y>0
        Iqb = partial(k, lambda yy: -fq(-yy) if yy < 0 else 0, e, neg=True)   # antiquark part: y<0, f(y) = -qbar(|y|)
        seq.append(Iq + Iqb)
        if n == 7:
            print("     %-6s quark-only partial (eps=1e-7): %s" % (name, mp.nstr(Iq, 8)))
    print("     %-6s quark+antiquark partial integrals eps=1e-3,1e-5,1e-7:" % name, [mp.nstr(v, 10) for v in seq])
    d1 = seq[1]-seq[0]; d2 = seq[2]-seq[1]
    rep("%s: quark+antiquark combination converges for C-even Regge sea (delta=0.3): differences shrink like eps^0.7" % name,
        abs(d2/d1 - mp.mpf(100)**(-0.7)) < 0.01, "d1=%s d2=%s ratio=%s (expect 100^-0.7=%s)" % (mp.nstr(d1, 4), mp.nstr(d2, 4), mp.nstr(d2/d1, 4), mp.nstr(mp.mpf(100)**(-0.7), 4)))
print("SUMMARY n09: %d/%d PASS" % (sum(res), len(res)))
