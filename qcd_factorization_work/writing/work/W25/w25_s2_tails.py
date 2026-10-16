#!/usr/bin/env python3
"""W25 / Ch22 -- s2: full re-derivation of prop:lamet-tails, in particular item (iii) (lead-author decision LA-11).

One loop, a = alpha_s C_F/(2 pi) set to 1.  Quasi-PDF  q~(x) = int_{-1}^{1} dy/|y| C(x/y, mu/(|y|P^z)) f(y),
physical quark distribution f(y) = q(y) (y>0), f(y) = -qbar(-y) (y<0).
Kernels: VF-LAM-8 (MSbar, ratio; gamma^0), VF-LAM-10 (hybrid, lambda_S = z_S |y| P^z).

Method (independent of the verification record batch_N07_s1):
 T1  symbolic small-y expansion of (1/|y|) C(x/y) for y -> 0+ and y -> 0-, x of either sign (sympy series in y)
 T2  exact identity: the hybrid correction, written in hadron variables, depends on y only through x - y:
       (1/|y|) (3/2)[-1/|1-xi| + 2 Si((1-xi) lambda_S)/(pi (1-xi))] = (3/2)[-1/|y-x| + 2 Si(z_S P^z (y-x))/(pi (y-x))]
     (checked symbolically and numerically), hence its y -> 0 limit (3/(2|x|))[(2/pi) Si(|x| z_S P^z) - 1]
 T3  pairing y <-> -y: the O(1) terms combine into q - qbar, the O(y) terms into y (q + qbar)
 T4  numerics with a test distribution different from the verification record:
       q = y^-1.5 (1-y)^3, qbar = y^-1.5 (1-y)^7  (Regge-like sea, delta = 0.5; q - qbar ~ 4 y^-0.5)
     quark-only partial integrals diverge like eps^-0.5 (MSbar, hybrid), converge for ratio; the paired combination
     converges for all three schemes with differences shrinking like eps^0.5
 T5  large-|x| tails of the quasi-PDF (MSbar: -(3/(2|x|)) int f; ratio: -(4/3) sgn(x) <y>_{q+qbar}/x^2) numerically
 T6  zeros of the hybrid coefficient (isolated points where Si(|x| z_S P^z) = pi/2)
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

# ------------------------------------------------------------------ kernels away from xi = 1
xi = sp.Symbol('xi', real=True)
CMS_pos = (1 + xi**2) / (1 - xi) * sp.log(xi / (xi - 1)) + 1           # xi > 1  (the +-3/(2xi) inside/outside cancel off xi = 1)
CMS_neg = -(1 + xi**2) / (1 - xi) * sp.log(-xi / (1 - xi)) - 1         # xi < 0
CR_pos = CMS_pos - sp.Rational(3, 2) / (1 - xi)
CR_neg = CMS_neg + sp.Rational(3, 2) / (1 - xi)

# ------------------------------------------------------------------ T1: small-y expansions
yy = sp.Symbol('y', positive=True)       # |y|
X = sp.Symbol('X', positive=True)        # |x|
def small_y(Cpos, Cneg, sx, sy):
    """(1/|y|) C(x/y) for sign(x)=sx, sign(y)=sy, as a series in |y|"""
    xi_val = sx * X / (sy * yy)
    Cexpr = Cpos if xi_val.subs({X: 1, yy: 1}) > 0 else Cneg
    e = sp.simplify(Cexpr.subs(xi, xi_val) / yy)
    return sp.expand(sp.series(e, yy, 0, 3).removeO())
res = {}
for name, (cp, cn) in {'MS': (CMS_pos, CMS_neg), 'ratio': (CR_pos, CR_neg)}.items():
    for sx in (1, -1):
        for sy in (1, -1):
            res[(name, sx, sy)] = small_y(cp, cn, sx, sy)
            print("   %-5s sgn x=%+d sgn y=%+d : (1/|y|)C(x/y) = %s" % (name, sx, sy, res[(name, sx, sy)]))
ok_ms = all(sp.simplify(res[('MS', sx, sy)].coeff(yy, 0) + sp.Rational(3, 2) / X) == 0 for sx in (1, -1) for sy in (1, -1))
check("T1 MSbar: (1/|y|)C(x/y) = -3/(2|x|) + O(y) for both signs of x and y", ok_ms)
ok_ms1 = all(sp.simplify(res[('MS', sx, sy)].coeff(yy, 1) - (-sp.Rational(17, 6) * sx * sy / X**2)) == 0
             for sx in (1, -1) for sy in (1, -1))
check("T1 MSbar O(y) term: -(17/6) sgn(x) y / x^2 (odd in y)", ok_ms1)
ok_r = all(res[('ratio', sx, sy)].coeff(yy, 0) == 0 and
           sp.simplify(res[('ratio', sx, sy)].coeff(yy, 1) - (-sp.Rational(4, 3) * sx * sy / X**2)) == 0
           for sx in (1, -1) for sy in (1, -1))
check("T1 ratio: (1/|y|)C(x/y) = -(4/3) sgn(x) y / x^2 + O(y^2) (no O(1) term)", ok_r)

# ------------------------------------------------------------------ T2: hybrid correction in hadron variables
mp.mp.dps = 25
def hyb_parton(x, y, ZS):          # (1/|y|) * (3/2)[-1/|1-xi| + 2 Si((1-xi) lam_S)/(pi (1-xi))], lam_S = ZS*|y|, ZS = z_S P^z
    xi_ = x / y; u = 1 - xi_; lamS = ZS * abs(y)
    return 1 / abs(y) * mp.mpf(3) / 2 * (-1 / abs(u) + 2 * mp.si(u * lamS) / (mp.pi * u))
def hyb_hadron(x, y, ZS):
    d = y - x
    return mp.mpf(3) / 2 * (-1 / abs(d) + 2 * mp.si(ZS * d) / (mp.pi * d))
ok = True
for (x, y, ZS) in [(0.3, 0.05, 3), (0.3, -0.2, 3), (-0.6, 0.4, 7), (0.8, -0.9, 1.5), (0.45, 0.9, 12), (1.7, 0.3, 4)]:
    ok &= abs(hyb_parton(mp.mpf(x), mp.mpf(y), mp.mpf(ZS)) - hyb_hadron(mp.mpf(x), mp.mpf(y), mp.mpf(ZS))) < mp.mpf('1e-20')
check("T2 hybrid correction: parton form (lambda_S = z_S|y|P^z) == function of (y-x) with fixed z_S P^z", ok)
# symbolic: sgn(y) Si(ZS (y-x) sgn(y)) = Si(ZS (y-x)) by oddness of Si
t = sp.Symbol('t', real=True)
check("T2 Si is odd (used for sgn(y) Si(sgn(y) w) = Si(w))", sp.simplify(sp.Si(-t) + sp.Si(t)) == 0)
for x, ZS in [(0.3, 3), (-0.3, 3), (0.7, 1.1)]:
    lim = hyb_hadron(mp.mpf(x), mp.mpf('1e-14'), mp.mpf(ZS))
    pred = mp.mpf(3) / (2 * abs(x)) * (2 / mp.pi * mp.si(abs(x) * ZS) - 1)
    check("T2 y->0 limit of hybrid correction at x=%.1f, z_S P^z=%g equals (3/(2|x|))[(2/pi)Si(|x|z_S P^z)-1]" % (x, ZS),
          abs(lim - pred) < 1e-10, mp.nstr(pred, 10))
# the coordinate-space origin: the one-loop hybrid correction (3a/2) delta(1-alpha) ln(z^2/z_S^2) theta(|z|-z_S) multiplies
# I(lambda) itself, and ln(z^2/z_S^2) = ln(lambda^2/(z_S P^z)^2) depends on the HADRON momentum -> additive convolution in x.
check("T2 coordinate origin: ln(z_3^2/z_S^2) = ln(lambda^2/(z_S P^z)^2) along the quasi-PDF ray (z_3 = |lambda|/P^z)",
      sp.simplify(sp.log((sp.Symbol('lam')**2 / sp.Symbol('Pz')**2) / sp.Symbol('zS')**2)
                  - sp.log(sp.Symbol('lam')**2 / (sp.Symbol('zS') * sp.Symbol('Pz'))**2)) == 0)

# ------------------------------------------------------------------ T3: pairing y <-> -y
q, qb, qd, qbd = sp.symbols('q qbar dq dqbar')   # values at t and the derivative-type O(t) coefficients
c0, c1 = sp.symbols('c0 c1')                     # (1/|y|)C = c0 + c1*y + ...
# y = +t : f = q(t)      ; y = -t : f = -qbar(t)
paired = sp.expand((c0 + c1 * t) * q + (c0 - c1 * t) * (-qb))
check("T3 paired integrand = c0 (q - qbar) + c1 t (q + qbar) + O(t^2)", sp.simplify(paired - (c0 * (q - qb) + c1 * t * (q + qb))) == 0)

# ------------------------------------------------------------------ T4: numerics with a Regge-like sea, delta = 0.5
x0 = mp.mpf('0.3'); ZS = mp.mpf(3)
qf = lambda y: y**mp.mpf(-1.5) * (1 - y)**3
qbf = lambda y: y**mp.mpf(-1.5) * (1 - y)**7
def C_MS(xi_):
    return (1 + xi_**2) / (1 - xi_) * mp.log(xi_ / (xi_ - 1)) + 1 if xi_ > 1 else -(1 + xi_**2) / (1 - xi_) * mp.log(-xi_ / (1 - xi_)) - 1
def C_R(xi_):
    return C_MS(xi_) - mp.mpf(3) / (2 * (1 - xi_)) if xi_ > 1 else C_MS(xi_) + mp.mpf(3) / (2 * (1 - xi_))
def integrand(scheme, y):        # (1/|y|) C(x0/y) * f(y)  for small |y| (|y| < x0/2: only regular kernels)
    xi_ = x0 / y
    base = C_MS(xi_) if scheme == 'MS' else C_R(xi_)
    val = base / abs(y)
    if scheme == 'hyb':
        val += hyb_hadron(x0, y, ZS)
    f = qf(y) if y > 0 else -qbf(-y)
    return val * f
ymax = x0 / 4
def partial(scheme, eps, which):
    pts = [eps, eps * 10, eps * 100, eps * 1000, ymax] if eps * 1000 < ymax else [eps, ymax]
    Iq = mp.quad(lambda t: integrand(scheme, t), pts)
    Iqb = mp.quad(lambda t: integrand(scheme, -t), pts)
    return {'q': Iq, 'qbar': Iqb, 'pair': Iq + Iqb}[which]
epsl = [mp.mpf('1e-4'), mp.mpf('1e-6'), mp.mpf('1e-8')]
for scheme in ('MS', 'hyb', 'ratio'):
    qonly = [partial(scheme, e, 'q') for e in epsl]
    pair = [partial(scheme, e, 'pair') for e in epsl]
    print("   %-5s quark-only partials (eps=1e-4,1e-6,1e-8): %s" % (scheme, [mp.nstr(v, 8) for v in qonly]))
    print("   %-5s paired partials     (eps=1e-4,1e-6,1e-8): %s" % (scheme, [mp.nstr(v, 10) for v in pair]))
    d1 = pair[1] - pair[0]; d2 = pair[2] - pair[1]
    check("T4 %s: paired (quark + antiquark) integral converges, differences shrink like eps^0.5 (ratio %s; eps steps of 100 -> expect 100^-0.5 = 0.1)"
          % (scheme, mp.nstr(d2 / d1, 5)), abs(d2 / d1 - mp.mpf('0.1')) < 2e-3)
    if scheme in ('MS', 'hyb'):
        r = (qonly[2] - qonly[1]) / (qonly[1] - qonly[0])
        check("T4 %s: quark-only integral diverges like eps^-0.5 (successive increments ratio %s; eps steps of 100 -> expect 100^0.5 = 10)"
              % (scheme, mp.nstr(r, 6)), abs(r - 10) < 0.05)
        # coefficient: quark-only ~ c * int_eps q ~ c * 2 eps^-0.5
        c = -mp.mpf(3) / (2 * x0) if scheme == 'MS' else mp.mpf(3) / (2 * x0) * (2 / mp.pi * mp.si(x0 * ZS) - 1)
        pred_inc = c * 2 * (epsl[2]**mp.mpf(-0.5) - epsl[1]**mp.mpf(-0.5))
        check("T4 %s: coefficient of the divergence = predicted O(1) coefficient (%s)" % (scheme, mp.nstr(c, 8)),
              abs((qonly[2] - qonly[1]) / pred_inc - 1) < 1e-3, mp.nstr((qonly[2] - qonly[1]) / pred_inc, 8))
    else:
        d1q = qonly[1] - qonly[0]; d2q = qonly[2] - qonly[1]
        check("T4 ratio: quark-only integral converges already (int |y f| < infinity), increments ratio %s (expect 0.1)"
              % mp.nstr(d2q / d1q, 5), abs(d2q / d1q - mp.mpf('0.1')) < 0.02)

# ------------------------------------------------------------------ T5: large-|x| tails of the quasi-PDF
fq = lambda y: y**mp.mpf(0.5) * (1 - y)**3
fqb = lambda y: mp.mpf('0.3') * y**mp.mpf(0.5) * (1 - y)**6
def qtilde(scheme, x):          # |x| > 1: no plus-subtraction (f(x) = 0), only regular kernels
    Kf = C_MS if scheme == 'MS' else C_R
    Iq = mp.quad(lambda y: Kf(x / y) / y * fq(y), [0, 1])
    Iqb = mp.quad(lambda t: Kf(-x / t) / t * (-fqb(t)), [0, 1])
    return Iq + Iqb
intf = mp.quad(fq, [0, 1]) - mp.quad(fqb, [0, 1])
mom1 = mp.quad(lambda y: y * fq(y), [0, 1]) + mp.quad(lambda y: y * fqb(y), [0, 1])
for x in (mp.mpf(30), mp.mpf(-30), mp.mpf(300)):
    ms = qtilde('MS', x) * abs(x); rt = qtilde('ratio', x) * x * abs(x)
    check("T5 x=%s: |x| q~_MS -> -(3/2) int f (%s vs %s)" % (mp.nstr(x, 4), mp.nstr(ms, 7), mp.nstr(-1.5 * intf, 7)),
          abs(ms + 1.5 * intf) < 0.1 * abs(1.5 * intf))
    check("T5 x=%s: x|x| q~_ratio -> -(4/3)<y>_{q+qbar} (%s vs %s)" % (mp.nstr(x, 4), mp.nstr(rt, 7), mp.nstr(-4 * mom1 / 3, 7)),
          abs(rt + 4 * mom1 / 3) < 0.12 * abs(4 * mom1 / 3))

# ------------------------------------------------------------------ T6: isolated zeros of the hybrid coefficient
f6 = lambda v: 2 / mp.pi * mp.si(v) - 1
zeros = [mp.findroot(f6, v0) for v0 in (1.9, 4.9, 7.8)]
print("   zeros of (2/pi)Si(v) - 1 (v = |x| z_S P^z):", [mp.nstr(z, 8) for z in zeros])
check("T6 the hybrid O(1) coefficient vanishes only at isolated points v = |x| z_S P^z (first zero %s)" % mp.nstr(zeros[0], 6),
      all(abs(f6(z)) < 1e-20 for z in zeros) and zeros[0] > 1.9 and zeros[0] < 2.0)
for v in (1, 3, 10, 30):
    print("   1 - (2/pi)Si(v) at v=%d : %s" % (v, mp.nstr(-f6(mp.mpf(v)), 6)))

print("\nSUMMARY w25_s2_tails: %d PASS, %d FAIL" % (NP, NF))
