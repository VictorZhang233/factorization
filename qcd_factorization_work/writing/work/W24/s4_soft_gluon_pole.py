#!/usr/bin/env python3
"""W24 / Ch21 -- soft-gluon-pole mechanism (ex:power-sgp).

Conventions: v^pm = (v^0 pm v^3)/sqrt2, v.w = v^+w^- + v^-w^+ - vT.wT; hadron A along +z: P_A = (P^+, 0^-, 0_T)
(massless approximation). A collinear gluon from A carries k = x_g P_A, x_g = x2 - x1.
 (1) final-state line c (p_c^2=0): (p_c - x_g P_A)^2 + i0 = -2 x_g p_c.P_A + i0 = -2 p_c.P_A (x_g - i0)  [p_c.P_A>0]
 (2) initial-state line b (p_b incoming, p_b^2=0): (p_b + x_g P_A)^2 + i0 = 2 x_g p_b.P_A + i0 = 2 p_b.P_A (x_g + i0)
 (3) Sokhotski-Plemelj: 1/(x -+ i0) = P(1/x) +- i pi delta(x); the delta parts are opposite -> opposite phases (FSI vs ISI).
 (4) eikonal form: future-pointing line along n_B: -i/(n_B.k - i0), past-pointing: i/(n_B.k + i0) (WRITER_SPEC row 28);
     their difference: i/(k^+ + i0) - (-i/(k^+ - i0)) ... the one-gluon difference future - past = 2 pi i delta(k^+) times vertex.
     VF-WL-12: 1/(k + i0) - 1/(k - i0) = -2 pi i delta(k).
 (5) SIDIS struck quark moves along -z: p_c ~ (0^+, p_c^-, 0): p_c.k = p_c^- k^+ -> pole in k^+ = x_g P^+.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

OK = True
def check(name, cond):
    global OK
    print(("PASS " if cond else "FAIL ") + name)
    OK = OK and bool(cond)

def dot(a, b):   # light-front components (plus, minus, x, y)
    return a[0]*b[1] + a[1]*b[0] - a[2]*b[2] - a[3]*b[3]
Pp, xg, pcm, pcp, pcx, pcy = sp.symbols('P^+ x_g p_c^- p_c^+ p_cx p_cy', real=True)
PA = (Pp, 0, 0, 0)
# massless p_c: p_c^+ = (pcx^2+pcy^2)/(2 p_c^-)
pc = (sp.Rational(1, 1)*(pcx**2 + pcy**2)/(2*pcm), pcm, pcx, pcy)
kg = tuple(xg*comp for comp in PA)
lhs = dot(tuple(pc[i] - kg[i] for i in range(4)), tuple(pc[i] - kg[i] for i in range(4)))
check("(1) (p_c - x_g P_A)^2 = -2 x_g p_c.P_A for massless p_c, P_A", sp.simplify(lhs - (-2*xg*dot(pc, PA))) == 0)
print("   p_c.P_A =", sp.simplify(dot(pc, PA)), " (= p_c^- P^+ > 0)")
pb = (sp.Rational(1, 1)*0, pcm, 0, 0)    # incoming antiquark from B along -z: only minus component
lhs2 = dot(tuple(pb[i] + kg[i] for i in range(4)), tuple(pb[i] + kg[i] for i in range(4)))
check("(2) (p_b + x_g P_A)^2 = +2 x_g p_b.P_A", sp.simplify(lhs2 - 2*xg*dot(pb, PA)) == 0)

# (3) Sokhotski-Plemelj numerically: int dx f(x)/(x - i eta) -> PV + i pi f(0)
mp.mp.dps = 30
f = lambda x: mp.exp(-(x - mp.mpf('0.3'))**2)*(1 + x/3)
for eta, sgn in [(mp.mpf('1e-8'), -1), (mp.mpf('1e-8'), +1)]:
    val = mp.quad(lambda x: f(x)/(x + sgn*1j*eta), [-mp.inf, -1, -eta*10, 0, eta*10, 1, mp.inf])
    pv = mp.quad(lambda x: (f(x) - f(-x))/x, [0, 1, mp.inf])   # PV int f(x)/x = int_0^oo (f(x)-f(-x))/x
    expect = pv - sgn*1j*mp.pi*f(0)
    print(f"   1/(x {'+' if sgn>0 else '-'} i0): numeric {mp.nstr(val, 12)}, PV {'-' if sgn>0 else '+'} i pi f(0) = {mp.nstr(expect, 12)}")
    check(f"(3) Sokhotski-Plemelj for 1/(x {'+' if sgn>0 else '-'} i0)", abs(val - expect) < 1e-6)

# (4) eikonal: future-pointing  -i/(k-i0), past-pointing  i/(k+i0); future - past = -i/(k-i0) - i/(k+i0)
#     = -i [P/k + i pi delta] - i [P/k - i pi delta] = -2i P/k ... ; and (row 28 statement) the FULL Wilson-line
#     difference at the same point  W_future - W_past = 2 pi i g t^a n.A(k) delta(n.k): one-gluon terms
#     g t^a n.A/(n.k - i0) - g t^a n.A/(n.k + i0) = g t^a n.A (2 pi i delta(n.k))   (VF-WL-1 one-gluon terms)
kk = sp.symbols('k', real=True)
# represent distributions by their action on a test function via Sokhotski-Plemelj symbols
Pk, dk = sp.symbols('P_k delta_k')     # P(1/k), delta(k)
inv_minus = Pk + sp.I*sp.pi*dk         # 1/(k - i0)
inv_plus = Pk - sp.I*sp.pi*dk          # 1/(k + i0)
check("(4) one-gluon terms: 1/(n.k - i0) - 1/(n.k + i0) = 2 pi i delta(n.k)  [future minus past, VF-WL-1 / row 28]",
      sp.simplify(inv_minus - inv_plus - 2*sp.I*sp.pi*dk) == 0)
check("(4') VF-WL-12: 1/(k + i0) - 1/(k - i0) = -2 pi i delta(k)", sp.simplify(inv_plus - inv_minus + 2*sp.I*sp.pi*dk) == 0)
# (5) eikonal factors from the Dirac algebra (massless, p^2=0, k soft, k flowing INTO the quark line):
#   outgoing quark:  ubar(p) (i g gamma^mu t) i(pslash - kslash)/((p-k)^2 + i0) ~ ubar(p) * g t p^mu/(p.k - i0)
#   incoming quark:  i(pslash + kslash)/((p+k)^2 + i0) (i g gamma^mu t) u(p) ~ -g t p^mu/(p.k + i0) u(p)   [VF-WL-5]
#   using ubar(p) gamma^mu pslash = 2 p^mu ubar(p), pslash gamma^mu u(p) = 2 p^mu u(p) and (p -+ k)^2 = -+ 2 p.k.
g = sp.symbols('g', positive=True)
pk = sp.symbols('pk', real=True)          # p.k
eps0 = sp.symbols('eta', positive=True)   # i0
out_fac = sp.simplify(sp.I*g*sp.I*2/(-2*pk + sp.I*eps0))     # coefficient of t p^mu  (ubar side)
in_fac = sp.simplify(sp.I*2*sp.I*g/(2*pk + sp.I*eps0))       # coefficient of t p^mu  (u side)
check("(5a) outgoing quark: eikonal factor = g/(p.k - i0)", sp.simplify(out_fac - g/(pk - sp.I*eps0/2)) == 0)
check("(5b) incoming quark: eikonal factor = -g/(p.k + i0)", sp.simplify(in_fac + g/(pk + sp.I*eps0/2)) == 0)
# decompose with Sokhotski-Plemelj: outgoing  g[P + i pi delta], incoming -g[P - i pi delta]
out_sp = sp.expand(g*(Pk + sp.I*sp.pi*dk)); in_sp = sp.expand(-g*(Pk - sp.I*sp.pi*dk))
ratio_out = sp.simplify(out_sp.coeff(dk)/out_sp.coeff(Pk)); ratio_in = sp.simplify(in_sp.coeff(dk)/in_sp.coeff(Pk))
print("   pole/PV ratio: outgoing (FSI)", ratio_out, " incoming (ISI)", ratio_in)
check("(5c) pole part relative to the principal-value part has opposite sign for FSI and ISI", sp.simplify(ratio_out + ratio_in) == 0)
# Wilson-line form: W[inf n,0] one-gluon term +g/(n.k - i0) (future), W[0,-inf n] one-gluon term -g/(n.k + i0) (past, VF-WL-5)
# -> identical to (5a),(5b): the FSI of the struck quark builds the future-pointing line, the ISI the past-pointing one.
print("ALL PASS" if OK else "SOME CHECKS FAILED")
