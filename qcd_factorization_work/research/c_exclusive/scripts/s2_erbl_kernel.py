# -*- coding: utf-8 -*-
"""
s2_erbl_kernel.py -- item (1): one-loop derivation of the ERBL kernel in Feynman gauge with the light-like
Wilson line, for the partonic matrix element <0| dbar(w) g^+ g5 W[w,0] u(0) |u(y p) dbar(ybar p)>.

Method (p^+ = 1, external partons exactly collinear and on shell):
  * the k^- integral of each graph is done by residues (exact, sympy) and cross-checked by direct numerical
    integration at finite i0 (mpmath);
  * after the k^- integral each graph is  (alpha_s/2pi) * V_graph(x,y) * int dk_T^2/k_T^2  (pure log; in DR the
    log is 1/eps_UV - 1/eps_IR), so V_graph is the graph's contribution to the kernel;
  * Dirac numerators are reduced with explicit 4x4 matrices between the collinear projectors.
Run:  python3 -I s2_erbl_kernel.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
import mpmath as mp

ck = Checker('s2_erbl_kernel')
x, y, km, kT, lp, s, w, c, l = sp.symbols('x y k_m k_T l_p s w c l', real=True)
k1, k2, kTx, kTy = sp.symbols('k1 k2 kTx kTy', real=True)

Pu = sp.Rational(1, 2) * gm * gp   # u(k1) = Pu u(k1)  (gamma^- u = 0)
Pv = sp.Rational(1, 2) * gp * gm   # vbar(k2) = vbar(k2) Pv
Gam = gp * g5                      # operator Dirac structure gamma^+ gamma_5

print('=== 1. Wilson-line one-gluon vertex in momentum-fraction space ===')
# int_0^1 ds w e^{i(c - s l) w} = (i/l)[e^{i(c-l)w} - e^{icw}]
ln_, wn_ = sp.symbols('l_nz w_nz', real=True, nonzero=True)   # l^+ != 0 (the identity is analytic in l^+)
lhs = sp.integrate(wn_ * sp.exp(I * (c - s * ln_) * wn_), (s, 0, 1))
rhs = I / ln_ * (sp.exp(I * (c - ln_) * wn_) - sp.exp(I * c * wn_))
ck.zero('int_0^1 ds w^- e^{i(c - s l^+) w^-} = (i/l^+)[e^{i(c-l^+)w^-} - e^{i c w^-}]', sp.simplify(sp.expand(lhs - rhs)))
print('   => one-gluon vertex: (g t^a n^mu / l^+) [delta(x - (k^+ + l^+)) - delta(x - k^+)] Gamma  (p^+=1),')
print('      k = quark momentum entering the vertex at 0, l = gluon momentum absorbed by the Wilson line.')

print('=== 2. Dirac numerators between collinear projectors ===')
k = lc(x, km, kTx, kTy)            # loop momentum, k^+ = x
p = lc(1, 0)
kT2 = kTx ** 2 + kTy ** 2          # |k_T|^2 (Euclidean)
# (a) gluon exchange between quark and antiquark legs: gamma^alpha (pslash-kslash) Gamma kslash gamma_alpha
Xa = sp.zeros(4)
for a_ in range(4):
    Xa += G[a_] * slash(sub(p, k)) * Gam * slash(k) * GL[a_]
ck.check('(a) Pv [g^a (p-k)sl g+ g5 ksl g_a] Pu = 2 |k_T|^2 Pv g+ g5 Pu   (no k^- dependence)',
         sp.simplify(sp.expand(Pv * Xa * Pu - 2 * kT2 * Pv * Gam * Pu)) == sp.zeros(4))
# (b) Wilson line -- quark leg: Gamma nslash ... : gamma^+ g5 (k1-l)sl gamma^+ = 2 (k1-l)^+ gamma^+ g5  (exact matrix identity)
lm, lTx, lTy, yy = sp.symbols('l_m lTx lTy yy', real=True)
lvec = lc(lp, lm, lTx, lTy)
k1v = lc(yy, 0)
Xb = Gam * slash(sub(k1v, lvec)) * gp
ck.check('(b) g+ g5 (k1-l)sl g+ = 2 (k1-l)^+ g+ g5   (matrix identity, no l^-, l_T dependence)',
         sp.simplify(sp.expand(Xb - 2 * (yy - lp) * Gam)) == sp.zeros(4))
# (c) Wilson line -- antiquark leg: gamma^+ (k2-l)sl gamma^+ g5 = 2 (k2-l)^+ gamma^+ g5
k2v = lc(1 - yy, 0)
Xc = gp * slash(sub(k2v, lvec)) * Gam
ck.check('(c) g+ (k2-l)sl g+ g5 = 2 (k2-l)^+ g+ g5', sp.simplify(sp.expand(Xc - 2 * (1 - yy - lp) * Gam)) == sp.zeros(4))


print('=== 3. k^- integrals by residues (exact) and numerically at finite i0 ===')
def minus_integral(dens, kvar):
    """int_{-inf}^{inf} dk^- prod_i 1/(a_i k^- + b_i + i0), dens = list of (a_i, b_i) with numeric a_i != 0.
    Pole of factor i at k = -(b_i + i0)/a_i lies in the upper half plane iff a_i < 0.
    Close the contour in the lower half plane: result = -2 pi i * sum of residues of poles with a_i > 0."""
    res = 0
    for i, (ai, bi) in enumerate(dens):
        if ai > 0:
            kpole = -bi / ai
            r = 1 / ai
            for j, (aj, bj) in enumerate(dens):
                if j != i:
                    r *= 1 / (aj * kpole + bj)
            res += r
    return sp.simplify(-2 * sp.pi * I * res)


def num_integral(dens, eta=1e-3):
    f = lambda t: 1 / mp.fprod([complex(ai) * t + complex(bi) + 1j * eta for (ai, bi) in dens])
    poles = sorted([float(-bi / ai) for (ai, bi) in dens])
    pts = [-mp.inf] + poles + [mp.inf]
    return complex(mp.quad(f, pts, maxdegree=10))


KT2 = sp.Rational(7, 5)    # sample |k_T|^2
samples = [(sp.Rational(1, 5), sp.Rational(3, 5)), (sp.Rational(7, 10), sp.Rational(3, 10)),
           (sp.Rational(-1, 5), sp.Rational(1, 2)), (sp.Rational(6, 5), sp.Rational(1, 2)),
           (sp.Rational(2, 5), sp.Rational(9, 10)), (sp.Rational(19, 20), sp.Rational(1, 4))]
ok_exact = True
ok_num = True
for xv, yv in samples:
    # D1 = k^2 = 2 x k^- - kT^2 ; D2 = (p-k)^2 = -2(1-x) k^- - kT^2 ; D3 = (k1-k)^2 = -2(y-x) k^- - kT^2
    dens = [(2 * xv, -KT2), (-2 * (1 - xv), -KT2), (-2 * (yv - xv), -KT2)]
    val = minus_integral(dens, km)
    if 0 < xv < yv:
        expct = -sp.pi * I * xv / (yv * KT2 ** 2)
    elif yv < xv < 1:
        expct = -sp.pi * I * (1 - xv) / ((1 - yv) * KT2 ** 2)
    else:
        expct = 0
    if sp.simplify(val - expct) != 0:
        ok_exact = False
    nv = num_integral(dens)
    if abs(nv - complex(expct)) > 5e-3 * max(1, abs(complex(expct))):
        ok_num = False
        print('   numerical mismatch', xv, yv, nv, complex(expct))
ck.check('(a) int dk^- 1/(D1 D2 D3) = -i pi [x/y th(y-x) + xbar/ybar th(x-y)] th(x) th(1-x) / kT^4  (exact residues)', ok_exact)
ck.check('(a) same, direct numerical integration along the real axis with i0 -> i*1e-3', ok_num)
# (b): Dg = l^2 = 2 l^+ l^- - lT^2 ; Dq = (k1-l)^2 = -2(y - l^+) l^- - lT^2
ok_exact = True
ok_num = True
for lv, yv in [(sp.Rational(1, 5), sp.Rational(3, 5)), (sp.Rational(7, 10), sp.Rational(3, 5)), (sp.Rational(-1, 5), sp.Rational(1, 2))]:
    dens = [(2 * lv, -KT2), (-2 * (yv - lv), -KT2)]
    val = minus_integral(dens, km)
    expct = sp.pi * I / (yv * KT2) if 0 < lv < yv else 0
    if sp.simplify(val - expct) != 0:
        ok_exact = False
    nv = num_integral(dens)
    if abs(nv - complex(expct)) > 5e-3 * max(1, abs(complex(expct))):
        ok_num = False
        print('   numerical mismatch', lv, yv, nv, complex(expct))
ck.check('(b),(c) int dl^- 1/(Dq Dg) = i pi th(l^+) th(y_parton - l^+)/(y_parton lT^2)  (exact residues)', ok_exact)
ck.check('(b),(c) same, numerically', ok_num)

print('=== 4. assemble: coefficient of (alpha_s/2pi) int dk_T^2/k_T^2 ===')
# prefactors: graph (a): i g^2 C_F * int d^4k/(2pi)^4 delta(x-k^+) * 2 kT^2 /(D1 D2 D3)
#  int d^4k = int dk^+ dk^- d^2k_T,  d^2k_T = pi dk_T^2,  g^2 = 4 pi alpha_s
g2, aS, CF = sp.symbols('g2 alpha_s C_F', positive=True)
KT2s = sp.symbols('KT2s', positive=True)
pref = lambda: 1 / (2 * sp.pi) ** 4 * sp.pi      # d^4k/(2pi)^4 -> dk^- dk_T^2 * pi/(2pi)^4 (dk^+ eaten by delta)
xs, ys = sp.symbols('xs ys', positive=True)
# region 0<x<y
Ia = -sp.pi * I * xs / (ys * KT2s ** 2)
Va = sp.simplify(I * g2 * CF * pref() * 2 * KT2s * Ia * KT2s / (aS / (2 * sp.pi)) * 1)  # times KT2s: d k_T^2/k_T^2 measure
Va = sp.simplify(Va.subs(g2, 4 * sp.pi * aS))
ck.zero('(a) region x<y: V_a = C_F x/y', Va - CF * xs / ys)
# graph (b) real part: i g^2 C_F * (-1) * (1/l^+) * 2 (y-l^+) * [i pi/(y lT^2)] with l^+ = y - x
Ib = sp.pi * I / (ys * KT2s)
lpv = ys - xs
Vb = sp.simplify((I * g2 * CF * pref() * (-1) / lpv * 2 * (ys - lpv) * Ib * KT2s / (aS / (2 * sp.pi))).subs(g2, 4 * sp.pi * aS))
ck.zero('(b) real part, 0<x<y: V_b = C_F x/(y (y-x))', Vb - CF * xs / (ys * (ys - xs)))
# graph (c) real part: -i g^2 C_F * (1/l^+) * 2 (ybar - l^+) * [i pi/(ybar lT^2)], l^+ = x - y > 0
Ic = sp.pi * I / ((1 - ys) * KT2s)
lpv = xs - ys
Vc = sp.simplify((-I * g2 * CF * pref() / lpv * 2 * (1 - ys - lpv) * Ic * KT2s / (aS / (2 * sp.pi))).subs(g2, 4 * sp.pi * aS))
ck.zero('(c) real part, y<x<1: V_c = C_F (1-x)/((1-y)(x-y))', Vc - CF * (1 - xs) / ((1 - ys) * (xs - ys)))
# virtual parts: graph (b) delta(x-y) term = + i g^2 C_F delta(x-y) int dl^+ (1/l^+) 2(y-l^+) [i pi/(y lT^2)] (0<l^+<y)
lpp = sp.symbols('lpp', positive=True)
virt_b_integrand = sp.simplify((I * g2 * CF * pref() * 1 / lpp * 2 * (ys - lpp) * (sp.pi * I / (ys * KT2s)) * KT2s / (aS / (2 * sp.pi))).subs(g2, 4 * sp.pi * aS))
real_b_at = (CF * xs / (ys * (ys - xs))).subs(xs, ys - lpp)      # V_b^real(x,y) at x = y - l^+  (dx = dl^+ in magnitude)
ck.zero('(b) virtual integrand (per dl^+) = - V_b^real(x = y - l^+, y): virtual = -delta(x-y) int_0^y dx V_b^real(x,y)', virt_b_integrand + real_b_at)
virt_c_integrand = sp.simplify((-I * g2 * CF * pref() * (-1) / lpp * 2 * (1 - ys - lpp) * (sp.pi * I / ((1 - ys) * KT2s)) * KT2s / (aS / (2 * sp.pi))).subs(g2, 4 * sp.pi * aS))
real_c_at = (CF * (1 - xs) / ((1 - ys) * (xs - ys))).subs(xs, ys + lpp)
ck.zero('(c) virtual integrand (per dl^+) = - V_c^real(x = y + l^+, y): virtual = -delta(x-y) int_y^1 dx V_c^real(x,y)', virt_c_integrand + real_c_at)
# i.e. the virtual parts are minus the x-integral of the real parts:
#   (b) virtual = -delta(x-y) int_0^y dt  C_F t/(y(y-t)),  (c) virtual = -delta(x-y) int_y^1 dt C_F (1-t)/((1-y)(t-y))
print('   (b),(c) virtual parts = -delta(x-y) x [x-integral of the real parts]  => plus distributions')

print('=== 5. self-energy term and vector-current conservation ===')
# graph (a) integrates to 1/2:
ck.zero('int_0^1 dx [x/y th(y-x) + xbar/ybar th(x-y)] = 1/2',
        sp.integrate(xs / ys, (xs, 0, ys)) + sp.integrate((1 - xs) / (1 - ys), (xs, ys, 1)) - sp.Rational(1, 2))
print('   => with the external-leg factor (Z_2 - 1) delta(x-y) = -(alpha_s/4pi) C_F (1/eps_UV - 1/eps_IR) delta(x-y)')
print('      [Feynman gauge] = -(1/2) C_F delta(x-y) in units of (alpha_s/2pi) L, the sum of all graphs is')
print('      V = C_F [ x/y (1 + 1/(y-x)) th(y-x) + xbar/ybar (1 + 1/(x-y)) th(x-y) ]_+')
# Conservation of the local vector/axial current (n=0 moment) <=> int dx V(x,y) = 0 <=> self-energy coefficient = -1/2
zcoef = sp.symbols('zcoef')
cons = sp.integrate(xs / ys, (xs, 0, ys)) + sp.integrate((1 - xs) / (1 - ys), (xs, ys, 1)) + zcoef   # (b),(c) integrate to 0
ck.check('int dx V(x,y) = 0 (axial-current conservation) fixes the external-leg delta coefficient to -1/2 C_F, '
         'i.e. delta Z_2 = -alpha_s C_F/(4 pi eps) (Feynman gauge, standard)', sp.solve(cons, zcoef) == [-sp.Rational(1, 2)])

print('=== 6. hermiticity w.r.t. the weight x(1-x) ===')
Vfun = lambda X, Y, below: (X / Y * (1 + 1 / (Y - X))) if below else ((1 - X) / (1 - Y) * (1 + 1 / (X - Y)))
# x<y : V(x,y) y ybar  vs  V(y,x) x xbar  (for V(y,x) the first argument y is > second argument x)
ck.zero('V(x,y) y(1-y) = V(y,x) x(1-x)   (x<y; the case x>y follows by x->1-x, y->1-y)',
        sp.simplify(Vfun(xs, ys, True) * ys * (1 - ys) - Vfun(ys, xs, False) * xs * (1 - xs)))
ck.zero('symmetry V(1-x,1-y) = V(x,y)', sp.simplify(Vfun(1 - xs, 1 - ys, False) - Vfun(xs, ys, True)))

ck.summary()
