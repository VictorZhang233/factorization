"""W09 / v2: one-loop quark-in-quark PDF from the operator definition, Feynman gauge, gluon mass m
(IR) and DR (UV).  Re-derives VF-PDF-3 step by step:
 (a) the D-dim trace for the real graphs R1 (ladder) and R2 (+h.c.) and R3 = 0;
 (b) transverse integrals -> f_R = A_eps [ (1-eps)^2 (1-xi) xi^{-eps} + 2 xi^{1-eps}/(1-xi) ];
 (c) the MS-bar normalisation g0^2/(2pi)^{3-2eps} pi^{1-eps} = (alpha_s/2pi) mu^{2eps} e^{eps gE};
 (d) the l^- contour integral of the virtual Wilson-line graph V1 (numerical);
 (e) Sigma_V(0) = -A_eps (1-eps)/(2-eps) from Feynman parameters;
 (f) quark number exactly in eps, UV poles graph by graph, MS-bar finite part, int f^(1) = 0;
 (g) light-cone-gauge ladder alone gives hat P_qq;
 (h) numbers for the worked example.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w9lib import *
import sympy as sp
import mpmath as mp

npass = 0; nfail = 0
def check(name, ok):
    global npass, nfail
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)
    if ok: npass += 1
    else: nfail += 1

eps, xi, lT2, m2, x, pp, g = sp.symbols('epsilon xi l_T2 m2 x p_plus g', positive=True)
Dd = 4 - 2 * eps

# ---------------- (a) trace for the real emission -------------------------------------------
# amplitude (emission of gluon l, colour a, index mu from the incoming quark p, then the operator
# vertex with the Wilson-line term):  -g t^a eps*_mu [ kslash gamma^mu / k^2 + n^mu/(n.l) ] u(p),
# k = p - l.  Squared with sum eps eps* -> -g_{mu nu}:  (1/2) Tr[ pslash Gbar^nu gamma^+ Gamma^mu ] (-g_{mu nu})
# where Gamma^mu = kslash gamma^mu/k^2 + n^mu/n.l and Gbar^nu = gamma^nu kslash/k^2 + n^nu/n.l.
# Vectors: p, k, n (n.v = v^+, n^2 = 0, nslash = gamma^+). Dot products in terms of xi, l_T^2, m^2:
#   l = ((1-xi)p+, (lT^2+m^2)/(2(1-xi)p+), l_T);  k = p - l;  n.k = xi p+;  n.p = p+;  p^2 = 0
#   k^2 = -(lT^2 + xi m^2)/(1-xi);  p.k = (p^2 + k^2 - l^2)/2 = (k^2 - m^2)/2
k2 = -(lT2 + xi * m2) / (1 - xi)
dots = {('k', 'k'): k2, ('k', 'n'): xi * pp, ('k', 'p'): (k2 - m2) / 2,
        ('n', 'n'): 0, ('n', 'p'): pp, ('p', 'p'): 0}
nl = (1 - xi) * pp   # n.l
# R1: (1/2) Tr[ p gamma^nu k n k gamma_nu ] (-1) / (k^2)^2   (the -g_{mu nu} gives -gamma^nu...gamma_nu)
t_R1 = -sp.Rational(1, 2) * dtrace([('v', 'p'), ('i', 'a'), ('v', 'k'), ('v', 'n'), ('v', 'k'), ('i', 'a')], dots) / k2 ** 2
# R2 + h.c.: cross terms: (1/2) Tr[p (n^nu/nl) n k gamma^mu/k^2](-g_{mu nu}) + mirror
#   = -(1/2) Tr[p n k nslash ... ] careful: -g_{mu nu} n^nu gamma^mu = -nslash
t_R2a = -sp.Rational(1, 2) * dtrace([('v', 'p'), ('v', 'n'), ('v', 'k'), ('v', 'n')], dots) / (k2 * nl)
t_R2b = -sp.Rational(1, 2) * dtrace([('v', 'p'), ('v', 'n'), ('v', 'k'), ('v', 'n')], dots) / (k2 * nl)  # mirror (equal)
# R3: n^mu n^nu (-g_{mu nu}) = -n^2 = 0
t_R3 = 0
T_total = sp.simplify(t_R1 + t_R2a + t_R2b)
target = pp * (4 * (1 - eps) * (1 - xi) ** 2 * lT2 / (lT2 + xi * m2) ** 2 + 8 * xi / (lT2 + xi * m2))
check('(a) (1/2)Tr[...](-g) = p+[4(1-eps)(1-xi)^2 lT^2/(lT^2+xi m^2)^2 + 8 xi/(lT^2+xi m^2)]',
      sp.simplify(T_total.subs(D, Dd) - target) == 0)
check('(a) R1 part alone = 4(1-eps)(1-xi)^2 lT^2 p+/(lT^2+xi m^2)^2',
      sp.simplify(t_R1.subs(D, Dd) - pp * 4 * (1 - eps) * (1 - xi) ** 2 * lT2 / (lT2 + xi * m2) ** 2) == 0)

# ---------------- (b),(c): phase space and transverse integrals --------------------------------
# f(xi) = sum_X (1/2) delta(xi p+ - (p - p_X)^+) <...> ; one gluon: int dl+ d^{D-2}lT /((2pi)^{D-1} 2 l+)
# colour C_F; coupling g^2 ; delta fixes l+ = (1-xi)p+ -> 1/(2 l+) * (1/2) * T * g^2 C_F
integrand = sp.Rational(1, 2) * T_total.subs(D, Dd) / (2 * nl)   # per d^{D-2}lT /(2pi)^{D-1}, times g^2 C_F
integrand = sp.simplify(integrand)
expect = (1 - eps) * (1 - xi) * lT2 / (lT2 + xi * m2) ** 2 + 2 * xi / ((1 - xi) * (lT2 + xi * m2))
check('(b) integrand per g^2 C_F d^{D-2}lT/(2pi)^{D-1} = (1-eps)(1-xi)lT^2/(..)^2 + 2xi/((1-xi)(..))',
      sp.simplify(integrand - expect) == 0)
# Euclidean master integral in d = 2-2eps:  int d^d l (l^2)^a/(l^2+M^2)^b = pi^{d/2} G(a+d/2)G(b-a-d/2)/(G(d/2)G(b)) M^{2(a+d/2-b)}
def master(a, b, d, M2):
    return sp.pi ** (d / 2) * sp.gamma(a + d / 2) * sp.gamma(b - a - d / 2) / (sp.gamma(d / 2) * sp.gamma(b)) * M2 ** (a + d / 2 - b)
d = 2 - 2 * eps
I1 = master(1, 2, d, xi * m2)   # l^2/(l^2+M^2)^2
I0 = master(0, 1, d, xi * m2)   # 1/(l^2+M^2)
check('(b) int d^{2-2e}l l^2/(l^2+M^2)^2 = pi^{1-e}(1-e)Gamma(e) M^{-2e}',
      sp.simplify(sp.gammasimp(I1 / (sp.pi ** (1 - eps) * (1 - eps) * sp.gamma(eps) * (xi * m2) ** (-eps))) - 1) == 0)
check('(b) int d^{2-2e}l 1/(l^2+M^2) = pi^{1-e} Gamma(e) M^{-2e}',
      sp.simplify(sp.gammasimp(I0 / (sp.pi ** (1 - eps) * sp.gamma(eps) * (xi * m2) ** (-eps))) - 1) == 0)
# numerical check of the master formula at non-integer d
for (a, b, dd, M2) in ((1, 2, 1.37, 0.8), (0, 1, 1.21, 2.0), (0, 2, 2.6, 1.3)):
    num = mp.quad(lambda r: 2 * mp.pi ** (dd / 2) / mp.gamma(dd / 2) * r ** (dd - 1) * r ** (2 * a) / (r ** 2 + M2) ** b, [0, 1, mp.inf])
    ana = mp.pi ** (dd / 2) * mp.gamma(a + dd / 2) * mp.gamma(b - a - dd / 2) / (mp.gamma(dd / 2) * mp.gamma(b)) * M2 ** (a + dd / 2 - b)
    check('(b) master formula numerically, a=%d b=%d d=%.2f' % (a, b, dd), abs(num / ana - 1) < 1e-10)
# (c) MS-bar: g0^2 = 4 pi alpha_s mu^{2eps} e^{eps gE} (4pi)^{-eps}
als, mu2, gE = sp.symbols('alpha_s mu2 gamma_E', positive=True)
g02 = 4 * sp.pi * als * mu2 ** eps * sp.exp(eps * gE) * (4 * sp.pi) ** (-eps)
ratio = sp.simplify(g02 / (2 * sp.pi) ** (3 - 2 * eps) * sp.pi ** (1 - eps) / (als / (2 * sp.pi) * mu2 ** eps * sp.exp(eps * gE)))
check('(c) g0^2/(2pi)^{3-2eps} pi^{1-eps} = (alpha_s/2pi) mu^{2eps} e^{eps gamma_E}', sp.simplify(sp.powsimp(sp.expand_power_base(ratio, force=True), force=True)) == 1)
Aeps = als / (2 * sp.pi) * sp.exp(eps * gE) * sp.gamma(eps) * (mu2 / m2) ** eps   # times C_F
fR = (g02 / (2 * sp.pi) ** (3 - 2 * eps)) * ((1 - eps) * (1 - xi) * I1 + 2 * xi / (1 - xi) * I0)
fR_expect = Aeps * ((1 - eps) ** 2 * (1 - xi) * xi ** (-eps) + 2 * xi ** (1 - eps) / (1 - xi))
check('(b) f_R/C_F = A_eps[(1-eps)^2(1-xi)xi^{-eps} + 2 xi^{1-eps}/(1-xi)]',
      abs(complex(sp.N((fR / fR_expect).subs({eps: sp.Rational(1, 7), xi: sp.Rational(2, 5), m2: sp.Rational(3, 2), mu2: sp.Rational(5, 3), als: 1, gE: sp.EulerGamma}))) - 1) < 1e-12)
# A_eps expansion
Aser = sp.series(sp.exp(eps * sp.EulerGamma) * sp.gamma(eps), eps, 0, 2).removeO()
check('(b) e^{eps gE} Gamma(eps) = 1/eps + O(eps) (no constant)', sp.simplify(Aser - 1 / eps - sp.series(sp.exp(eps * sp.EulerGamma) * sp.gamma(eps), eps, 0, 2).removeO() + 1 / eps) == 0
      and sp.simplify(sp.series(sp.exp(eps * sp.EulerGamma) * sp.gamma(eps) - 1 / eps, eps, 0, 1).removeO()) == 0)

# ---------------- (d) V1: l^- contour integral --------------------------------------------------
# I(l+) = int dl^- 1/((2 l+ l^- - lT^2 - m^2 + i0)(-2(p+ - l+) l^- - lT^2 + i0)) = pi i theta(0<l+<p+)/(p+(lT^2 + x m^2)), l+ = (1-x)p+
def Iminus(lp, ppv, lt2, mm2, delta):
    l1 = (lt2 + mm2 - 1j * delta) / (2 * lp)
    l2 = (-lt2 + 1j * delta) / (2 * (ppv - lp))
    f = lambda lm: 1 / ((2 * lp * lm - lt2 - mm2 + 1j * delta) * (-2 * (ppv - lp) * lm - lt2 + 1j * delta))
    pts = sorted([float(np.real(l1)), float(np.real(l2))])
    return mp.quad(f, [-mp.inf, pts[0] - 1, pts[0], pts[1], pts[1] + 1, mp.inf])
def Iminus_residue(lp, ppv, lt2, mm2, delta):
    # exact value at finite delta (both poles simple)
    l1 = (lt2 + mm2 - 1j * delta) / (2 * lp)
    l2 = (-lt2 + 1j * delta) / (2 * (ppv - lp))
    if lp > 0 and ppv - lp > 0:   # l1 lower, l2 upper half plane: close upwards
        return 2j * np.pi / ((2 * lp * l2 - lt2 - mm2 + 1j * delta) * (-2 * (ppv - lp)))
    return 0.0
ppv, lt2v, mm2v = 1.3, 0.7, 0.45
for lp in (0.2, 0.9, 1.25):
    xval = 1 - lp / ppv
    num = complex(Iminus(lp, ppv, lt2v, mm2v, 0.02))
    res = complex(Iminus_residue(lp, ppv, lt2v, mm2v, 0.02))
    lim = complex(Iminus_residue(lp, ppv, lt2v, mm2v, 1e-12))
    ana = np.pi * 1j / (ppv * (lt2v + xval * mm2v))
    check('(d) l^- integral at l+=%.2f: quadrature %s = residue %s; delta->0 limit %s = pi i/(p+(lT^2+x m^2)) %s'
          % (lp, np.round(num, 6), np.round(res, 6), np.round(lim, 6), np.round(ana, 6)), abs(num - res) < 1e-8 and abs(lim - ana) < 1e-9)
for lp in (-0.3, 1.6):
    num = complex(Iminus(lp, ppv, lt2v, mm2v, 0.02))
    check('(d) l^- integral vanishes outside 0<l+<p+ (l+=%.2f): |I|=%.1e' % (lp, abs(num)), abs(num) < 1e-8)
# assembly: V1/tree = i g^2 C_F int d^Dl/(2pi)^D 2(p+ - l+)/((l+)(l^2-m^2)((p-l)^2)) ; after l^-:
#  = i g^2 C_F (pi i) /(2pi)^D int dl+ d^{D-2}lT 2(p+-l+)/(l+ p+ (lT^2+x m^2))  ->  -g^2 C_F/(2(2pi)^{D-1}) int dx 2x/(1-x) int d^{D-2}lT/(lT^2+x m^2)
xs = sp.symbols('x_s', positive=True)
lplus = (1 - xs) * pp
jac = pp   # dl+ = p+ dx
expr = 2 * (pp - lplus) / (lplus * pp) * jac
check('(d) 2(p+-l+)/(l+ p+) dl+ = 2x/(1-x) dx', sp.simplify(expr - 2 * xs / (1 - xs)) == 0)
check('(d) i * (pi i)/(2pi)^D = -1/(2 (2pi)^{D-1})', sp.simplify(sp.I * sp.pi * sp.I / (2 * sp.pi) ** Dd + 1 / (2 * (2 * sp.pi) ** (Dd - 1))) == 0)
# Dirac identity gamma^+ (pslash - lslash) gamma^+ = 2 (p^+ - l^+) gamma^+ (numerically)
pv = lc_to_cart(1.3, 0.0, 0, 0); lv = lc_to_cart(0.4, 0.77, 0.3, -0.2)
check('(d) g+ (p-l)slash g+ = 2(p+-l+) g+', np.allclose(GPLUS @ sl(pv - lv) @ GPLUS, 2 * (plus(pv) - plus(lv)) * GPLUS))
# gauge invariance of the one-gluon amplitude: l_mu [kslash gamma^mu/k^2 + n^mu/n.l] u(p) = 0
U = spinors_massless_z(1.3)
for h in U:
    kv = pv - lv
    lv_on = lc_to_cart(0.4, (0.3 ** 2 + 0.2 ** 2) / (2 * 0.4), 0.3, -0.2)   # massless on-shell l
    kv = pv - lv_on
    amp = (sl(kv) @ sl(lv_on) / dot(kv, kv) + np.eye(4)) @ U[h]
    check('(d) l_mu [kslash gamma^mu/k^2 + n^mu/n.l] u = 0 (h=%+.1f)' % h, np.allclose(amp, 0))

# ---------------- (e) self-energy ----------------------------------------------------------------
y = sp.symbols('y', positive=True)
# Sigma = -(D-2) g0^2 C_F/(4pi)^{D/2} Gamma(eps) int dy (1-y) [(1-y) m^2]^{-eps}  pslash
SigmaV = -(Dd - 2) * g02 / (4 * sp.pi) ** (Dd / 2) * sp.gamma(eps) * sp.integrate((1 - y) ** (1 - eps), (y, 0, 1)) * m2 ** (-eps)
check('(e) Sigma_V(0) = -A_eps (1-eps)/(2-eps) (per C_F)',
      abs(complex(sp.N((SigmaV / (-Aeps * (1 - eps) / (2 - eps))).subs({eps: sp.Rational(1, 9), m2: sp.Rational(7, 5), mu2: sp.Rational(2, 3), als: 1, gE: sp.EulerGamma}))) - 1) < 1e-12)
pole_SigmaV = sp.limit(eps * (1 / eps) * (-(1 - eps) / (2 - eps)), eps, 0)
check('(e) UV pole of Sigma_V = -(alpha_s/4pi) C_F/eps  (i.e. -1/2 in units alpha_s/2pi C_F/eps)', pole_SigmaV == -sp.Rational(1, 2))

# ---------------- (f) bare result, quark number, poles, finite part ---------------------------
tests = [lambda t: t ** 2, lambda t: mp.exp(t), lambda t: 1 / (1 + t), lambda t: t ** 3 * (1 - t) + 1, lambda t: mp.cos(3 * t)]
qn = sp.simplify(sp.gammasimp((1 - eps) ** 2 * sp.gamma(1 - eps) * sp.gamma(2) / sp.gamma(3 - eps)) - (1 - eps) / (2 - eps))
check('(f) quark number: (1-eps)^2 int (1-xi)xi^{-eps} = (1-eps)/(2-eps)  => int f^(1)_bare = 0', qn == 0)
def plus_apply(gfun, hfun):
    return mp.quad(lambda t: gfun(t) * (hfun(t) - hfun(1)), [0, 1])
for i, hf in enumerate(tests):
    lhs = mp.quad(lambda t: (1 - t) * hf(t), [0, 1]) + plus_apply(lambda t: 2 * t / (1 - t), hf) - 0.5 * hf(1)
    rhs = plus_apply(lambda t: (1 + t ** 2) / (1 - t), hf)
    rhs3 = mp.quad(lambda t: ((1 + t ** 2) * hf(t) - 2 * hf(1)) / (1 - t), [0, 1]) + 1.5 * hf(1)
    check('(f) poles: (1-xi)+[2xi/(1-xi)]_+ - delta/2 = [(1+xi^2)/(1-xi)]_+  (test %d)' % i, abs(lhs - rhs) < 1e-12)
    check('(f) [(1+xi^2)/(1-xi)]_+ = (1+xi^2)[1/(1-xi)]_+ + 3/2 delta  (test %d)' % i, abs(rhs - rhs3) < 1e-12)
    lhs2 = plus_apply(lambda t: 2 * t / (1 - t), hf)
    rhs4 = mp.quad(lambda t: (2 * t * hf(t) - 2 * hf(1)) / (1 - t), [0, 1]) + 2 * hf(1)
    check('(f) [2xi/(1-xi)]_+ = 2xi[1/(1-xi)]_+ + 2 delta (test %d)' % i, abs(lhs2 - rhs4) < 1e-12)
# finite part: expand the bracket B(eps) = (1-eps)^2 (1-xi) xi^{-eps} + [2 xi^{1-eps}/(1-xi)]_+ - (1-eps)/(2-eps) delta to O(eps)
B1_regular = sp.diff((1 - eps) ** 2 * (1 - xi) * xi ** (-eps), eps).subs(eps, 0)
check('(f) d/deps[(1-eps)^2(1-xi)xi^{-eps}]_0 = -(1-xi)(2+ln xi)', sp.simplify(B1_regular + (1 - xi) * (2 + sp.log(xi))) == 0)
check('(f) d/deps[2 xi^{1-eps}]_0 = -2 xi ln xi', sp.simplify(sp.diff(2 * xi ** (1 - eps), eps).subs(eps, 0) + 2 * xi * sp.log(xi)) == 0)
check('(f) -d/deps[(1-eps)/(2-eps)]_0 = +1/4', sp.simplify(-sp.diff((1 - eps) / (2 - eps), eps).subs(eps, 0) - sp.Rational(1, 4)) == 0)
# int_0^1 of the renormalised finite part vanishes: int (1-xi)(2+ln xi) = 1/4 ; the plus term integrates to 0
check('(f) int_0^1 (1-xi)(2+ln xi) dxi = 1/4  => int f^(1)_ren = 0', sp.simplify(sp.integrate((1 - xi) * (2 + sp.log(xi)), (xi, 0, 1)) - sp.Rational(1, 4)) == 0)
# full numeric check of the O(eps^0) term of <f_bare^(1), h> with A_eps expansion, against the closed form
for hf, hs in ((lambda t: t ** 2, lambda t: t ** 2), (lambda t: mp.exp(t), lambda t: sp.exp(t))):
    def Bnum(e):
        e = mp.mpf(e)
        r1 = (1 - e) ** 2 * mp.quad(lambda t: (1 - t) * t ** (-e) * hf(t), [0, 1])
        r2 = mp.quad(lambda t: 2 * t ** (1 - e) / (1 - t) * (hf(t) - hf(1)), [0, 1])
        r3 = -(1 - e) / (2 - e) * hf(1)
        return r1 + r2 + r3
    b1 = (Bnum(1e-5) - Bnum(-1e-5)) / (2e-5)
    closed = (-mp.quad(lambda t: (1 - t) * (2 + mp.log(t)) * hf(t), [0, 1])
              - mp.quad(lambda t: 2 * t * mp.log(t) * (hf(t) - hf(1)) / (1 - t), [0, 1]) + 0.25 * hf(1))
    check('(f) O(eps) coefficient of <B,h> equals <-(1-xi)(2+ln xi) - [2 xi ln xi/(1-xi)]_+ + delta/4, h>  (%.8f vs %.8f)' % (b1, closed), abs(b1 - closed) < 1e-6)

# ---------------- (g) light-cone gauge ladder ---------------------------------------------------
# numerator d_{mu nu}(l) = -g + (l n + n l)/n.l ; amplitude kslash gamma^mu u/k^2 ; massless gluon: m=0
# (1/2) Tr[pslash gamma^nu kslash gamma^+ kslash gamma^mu] d_{mu nu} /(k^2)^2 ; check l_T^2 x integrand = hatP_qq/C_F
dots0 = {('k', 'k'): -lT2 / (1 - xi), ('k', 'n'): xi * pp, ('k', 'p'): -lT2 / (2 * (1 - xi)),
         ('n', 'n'): 0, ('n', 'p'): pp, ('p', 'p'): 0, ('l', 'l'): 0, ('l', 'n'): (1 - xi) * pp,
         ('l', 'p'): lT2 / (2 * (1 - xi)), ('k', 'l'): None}
# l = p - k : k.l = k.p - k.k
dots0[('k', 'l')] = dots0[('k', 'p')] - dots0[('k', 'k')]
nl0 = (1 - xi) * pp
k20 = dots0[('k', 'k')]
trA = -dtrace([('v', 'p'), ('i', 'a'), ('v', 'k'), ('v', 'n'), ('v', 'k'), ('i', 'a')], dots0)
trB = dtrace([('v', 'p'), ('v', 'l'), ('v', 'k'), ('v', 'n'), ('v', 'k'), ('v', 'n')], dots0) / nl0
trC = dtrace([('v', 'p'), ('v', 'n'), ('v', 'k'), ('v', 'n'), ('v', 'k'), ('v', 'l')], dots0) / nl0
lc_num = sp.Rational(1, 2) * (trA + trB + trC) / k20 ** 2
lc_density = sp.simplify(lc_num.subs(D, Dd) / (2 * nl0) * sp.Rational(1, 2) * 2)   # (1/2)*(1/(2l+)) * 2 ... per g^2 C_F d^{D-2}l/(2pi)^{D-1}
# compare: f^real = g^2/(2pi)^{D-1} int d^{D-2}l hatP/l^2  ->  density * l^2 = hatP_qq/C_F
lcd = sp.simplify(sp.Rational(1, 2) * lc_num.subs(D, Dd) / (2 * nl0) * lT2)
check('(g) light-cone-gauge ladder: lT^2 x density = (1+xi^2)/(1-xi) - eps(1-xi)',
      sp.simplify(lcd - ((1 + xi ** 2) / (1 - xi) - eps * (1 - xi))) == 0)
# Feynman gauge massless limit: lT^2 x (R1 + R2) density
fg = sp.simplify(expect.subs(m2, 0) * lT2)
check('(g) Feynman gauge (m=0): lT^2 x (R1+R2) = (1-eps)(1-xi) + 2xi/(1-xi) = same kernel',
      sp.simplify(fg - ((1 + xi ** 2) / (1 - xi) - eps * (1 - xi))) == 0)

# ---------------- (h) numbers for the worked example ------------------------------------------
xi0 = sp.Rational(1, 2)
fin = -(1 - xi0) * (2 + sp.log(xi0)) - 2 * xi0 * sp.log(xi0) / (1 - xi0)
print('   (h) regular part of C_F[...] at xi=1/2 (excluding delta and plus subtraction): %.6f' % float(fin))
print('   (h) P_qq(1/2)/C_F (regular part) = %.6f' % float((1 + xi0 ** 2) / (1 - xi0)))
c_plus = mp.quad(lambda t: 2 * t * mp.log(t) / (1 - t), [0, 1])
check('(h) int_0^1 2 xi ln xi/(1-xi) dxi = 2 - pi^2/3 (%.10f)' % float(c_plus), abs(c_plus - (2 - mp.pi ** 2 / 3)) < 1e-12)
print('\nSUMMARY v2: %d PASS, %d FAIL' % (npass, nfail))
