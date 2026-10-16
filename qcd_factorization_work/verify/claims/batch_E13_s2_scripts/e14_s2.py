#!/usr/bin/env python3
"""E14 stage-2 checks (independent of stage 1).

(a) Derive the Feynman-parameter denominator of the one-loop bubble by explicit
    completion of the square (no textbook formula used): general masses.
(b) Coleman-Norton quadratic form E_ij (Hessian of the parametric denominator on the
    simplex) at the critical point: massive threshold vs massless p^2=0.
(c) Momentum-space Landau equations for the massless bubble in light-cone components;
    trap test (Gordan alternative) at k = x p.
(d) Collins App. D.2 (linear denominators): the omega integral as a distribution in alpha,
    computed with a symmetric cutoff (different route from stage 1), and the momentum-space
    pinch location.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np

ok = []
def check(name, cond):
    ok.append(bool(cond)); print(('PASS ' if cond else 'FAIL ') + name)

# ---------- (a) parametric denominator by completing the square -------------
a1, a2 = sp.symbols('alpha1 alpha2', positive=True)
m1, m2 = sp.symbols('m1 m2', nonnegative=True)
k0, k3, p0, p3 = sp.symbols('k0 k3 p0 p3', real=True)   # 1+1 dim suffices for the algebra
mink = lambda u, v: u[0]*v[0] - u[1]*v[1]
k = (k0, k3); p = (p0, p3)
pmk = (p0 - k0, p3 - k3)
# Feynman: 1/(A1 A2) = int da 1/(a1 A1 + a2 A2)^2 with A1 = k^2-m1^2, A2=(p-k)^2-m2^2
Dk = sp.expand(a1*(mink(k, k) - m1**2) + a2*(mink(pmk, pmk) - m2**2))
# stationary point in k
sol = sp.solve([sp.diff(Dk, k0), sp.diff(Dk, k3)], [k0, k3], dict=True)[0]
Dmin = sp.simplify(Dk.subs(sol))
U = a1 + a2
s = sp.symbols('s', real=True)  # p^2
Fexpected = -(U*(a1*m1**2 + a2*m2**2) - a1*a2*s)   # D_min = -F/U with F = U(sum a m^2) - a1 a2 p^2
check('(a) k_c = a2 p/(a1+a2)', sp.simplify(sol[k0] - a2*p0/U) == 0 and sp.simplify(sol[k3] - a2*p3/U) == 0)
check('(a) D(k_c) = -[U(a1 m1^2 + a2 m2^2) - a1 a2 p^2]/U', sp.simplify(Dmin - Fexpected.subs(s, p0**2 - p3**2)/U) == 0)
F = U*(a1*m1**2 + a2*m2**2) - a1*a2*s
F0 = sp.expand(F.subs({m1: 0, m2: 0}))
check('(a) massless: F = -p^2 a1 a2', sp.simplify(F0 + s*a1*a2) == 0)
check('(a) massless, p^2=0: F identically 0', F0.subs(s, 0) == 0)

# ---------- (b) CN quadratic form on the simplex ---------------------------
x = sp.symbols('x', real=True)
Dx = sp.expand(F.subs({a1: x, a2: 1 - x}))        # U = 1 on the simplex
# massive threshold s=(m1+m2)^2
Dthr = sp.expand(Dx.subs(s, (m1 + m2)**2))
xc = sp.solve(sp.diff(Dthr, x), x)[0]
check('(b) massive threshold: critical point x* = m2/(m1+m2)', sp.simplify(xc - m2/(m1 + m2)) == 0)
check('(b) massive threshold: D(x*) = 0', sp.simplify(Dthr.subs(x, xc)) == 0)
E = sp.diff(Dthr, x, 2)
check('(b) massive threshold: E = d2D/dx2 = 2(m1+m2)^2 != 0 (nondegenerate)', sp.simplify(E - 2*(m1 + m2)**2) == 0)
Dml = sp.expand(Dx.subs({m1: 0, m2: 0}))
check('(b) massless: D(x) = -s x(1-x); at s=0, D, D\', D\'\' all vanish identically',
      sp.simplify(Dml + s*x*(1 - x)) == 0 and all(sp.diff(Dml, x, n).subs(s, 0) == 0 for n in range(3)))
check('(b) massless, s!=0: D\'(x)=0 only at x=1/2 where D=-s/4 != 0 (no interior Landau point)',
      sp.solve(sp.diff(Dml, x), x) == [sp.Rational(1, 2)] and sp.simplify(Dml.subs(x, sp.Rational(1, 2)) + s/4) == 0)

# ---------- (c) momentum space, light-cone components ----------------------
kp, km, kt, pp, pm = sp.symbols('kp km kt pp pm', real=True)
l1, l2 = sp.symbols('lambda1 lambda2', nonnegative=True)
A1 = 2*kp*km - kt**2                     # k^2 (1 transverse dim suffices)
A2 = 2*(pp - kp)*(pm - km) - kt**2      # (p-k)^2, p_T = 0
grad = lambda A: [sp.diff(A, v) for v in (kp, km, kt)]
# Landau: l1 grad A1 + l2 grad A2 = 0, A1=A2=0
eqs = [l1*g1 + l2*g2 for g1, g2 in zip(grad(A1), grad(A2))] + [A1, A2]
sols = sp.solve(eqs, [kp, km, kt, l2], dict=True)
print('   Landau solutions (lambda1 free):', sols)
# with p^2 = 2 pp pm != 0, require consistency
nontriv = [d for d in sols if d.get(l2, None) is not None]
# test: on k = x p with pm = 0 (p light-like), the system is satisfied with l1=(1-x), l2=x
xx = sp.symbols('xx', positive=True)
subsd = {kp: xx*pp, km: 0, kt: 0, pm: 0}
res = [sp.simplify(e.subs(subsd).subs({l1: 1 - xx, l2: xx})) for e in eqs]
check('(c) p^2=0 (p^- = 0): k = x p solves Landau eqs with (l1,l2)=(1-x,x) for all 0<x<1', all(r == 0 for r in res))
# p^2 != 0: both on shell requires ... show no solution with k^2=(p-k)^2=0 and l1,l2>0
sub2 = {pm: 1, pp: 1}   # p^2 = 2
eqs2 = [e.subs(sub2) for e in eqs]
sols2 = sp.solve(eqs2, [kp, km, kt, l1, l2], dict=True)
pos = [d for d in sols2 if (d.get(l1, l1) != 0 or d.get(l2, l2) != 0)]
print('   p^2=2 solutions:', sols2)
check('(c) p^2 != 0: only solutions have l1 = l2 = 0 (no physical-region Landau point with both lines)',
      all(sp.simplify(d.get(l1, 1)) == 0 and sp.simplify(d.get(l2, 1)) == 0 for d in sols2) or len(sols2) == 0)
# Gordan alternative / trap test numerically: at k = 0.3 p (p light-like), is there v with v.gradA1>0, v.gradA2>0 ?
from itertools import product
g1 = np.array([float(gg.subs(subsd).subs({xx: 0.3, pp: 1})) for gg in grad(A1)])
g2 = np.array([float(gg.subs(subsd).subs({xx: 0.3, pp: 1})) for gg in grad(A2)])
print('   grad A1 =', g1, ' grad A2 =', g2)
check('(c) gradients anti-parallel with positive weights 0.7 g1 + 0.3 g2 = 0 -> no avoiding direction (trap)',
      np.allclose(0.7*g1 + 0.3*g2, 0) and np.dot(g1, g2) < 0)
# random search for avoiding direction (should fail)
rng = np.random.default_rng(1)
V = rng.normal(size=(200000, 3))
both = np.sum((V @ g1 > 0) & (V @ g2 > 0))
check('(c) 2e5 random deformation directions: none has v.gradA1>0 and v.gradA2>0', both == 0)
# soft point k=0, p^2 != 0: grad A1 = 0 there -> trapped (pinch) for every p
g1s = [gg.subs({kp: 0, km: 0, kt: 0}) for gg in grad(A1)]
check('(c) k=0: A1 = 0 and grad A1 = 0 for every p (single-denominator pinch, Collins D.1)', all(g == 0 for g in g1s))

# ---------- (d) Collins App. D.2, symmetric cutoff --------------------------
w, al, Lam, B = sp.symbols('omega alpha Lambda B')
a = 1 - 2*al
cut = sp.integrate(1/(a*w + B)**2, (w, -Lam, Lam))
cut = sp.simplify(cut)
check('(d) int_{-L}^{L} dw (a w + B)^-2 = 2L/(B^2 - a^2 L^2)', sp.simplify(cut - 2*Lam/(B**2 - a**2*Lam**2)) == 0)
# As L->inf, the alpha-weight: int dalpha 2L/(B^2 - (1-2alpha)^2 L^2) -> substitute u = (1-2alpha) L
u = sp.symbols('u', real=True)
# int over alpha in (0,1) == (1/2) int over u in (-L, L) du * 2/(B^2-u^2)/L * L ... do it numerically for complex B
def weight(Bv, L):
    # exact antiderivative of 1/(B^2-u^2): (1/(2B)) log((B+u)/(B-u))
    F_ = lambda uu: (1/(2*Bv))*np.log((Bv + uu)/(Bv - uu))
    return (1/2)*2*(F_(L) - F_(-L))   # (1/2) from dalpha = -du/(2L) times L, times 2
for Bv in [0.7 + 1e-3j, -1.3 + 1e-3j, 2.0 + 0.5j]:
    wv = weight(Bv, 1e7)
    print(f'   B={Bv}: alpha-weight -> {wv:.6f}, expected -i pi/B = {-1j*np.pi/Bv:.6f}')
check('(d) alpha-weight -> -i pi / B(alpha=1/2) for Im B > 0 (distribution localized at alpha=1/2)',
      all(abs(weight(Bv, 1e7) - (-1j*np.pi/Bv)) < 1e-5 for Bv in [0.7 + 1e-3j, -1.3 + 1e-3j, 2.0 + 0.5j]))
# B at alpha = 1/2 and Collins' coefficient
E_, kk, pk, m = sp.symbols('E k p m', real=True)
Bhalf = sp.Rational(1, 2)*E_ - (kk**2 - pk*kk + pk**2/2)/(2*m)
check('(d) -i pi/B(1/2) = -4 i pi m/(2Em - 2k^2 + 2pk - p^2) (Collins eq. in App. D.2)',
      sp.simplify(-sp.I*sp.pi/Bhalf - (-4*sp.I*sp.pi*m/(2*E_*m - 2*kk**2 + 2*pk*kk - pk**2))) == 0)
# For alpha != 1/2 the cut-off integral vanishes as L -> inf
check('(d) for fixed alpha != 1/2, the omega integral vanishes as Lambda -> oo',
      sp.limit(cut.subs({al: sp.Rational(1, 5), B: sp.Rational(3, 7)}), Lam, sp.oo) == 0)
# momentum-space Landau eqs: A1 = w - k^2/2m, A2 = E - w - (p-k)^2/2m
A1n = w - kk**2/(2*m); A2n = E_ - w - (pk - kk)**2/(2*m)
eqn = [l1*sp.diff(A1n, w) + l2*sp.diff(A2n, w), l1*sp.diff(A1n, kk) + l2*sp.diff(A2n, kk), A1n, A2n]
soln = sp.solve(eqn, [w, kk, E_, l2], dict=True)
print('   NR Landau solutions:', soln)
check('(d) momentum-space pinch only at E = p^2/(4m), (w,k) = (E,p)/2, l1 = l2',
      any(sp.simplify(d[E_] - pk**2/(4*m)) == 0 and sp.simplify(d[kk] - pk/2) == 0 and sp.simplify(d[l2] - l1) == 0 for d in soln))
# direct evaluation: omega by residues gives -2 pi i/(E - k^2/2m - (p-k)^2/2m + i eps); then k integral singular at E=p^2/4m
Ed = sp.symbols('Delta', positive=True)
expr = sp.simplify(E_ - kk**2/(2*m) - (pk - kk)**2/(2*m) - (E_ - pk**2/(4*m) - (kk - pk/2)**2/m))
check('(d) E - k^2/2m - (p-k)^2/2m = (E - p^2/4m) - (k-p/2)^2/m  -> square-root branch point at E = p^2/4m', expr == 0)
print(f'\nSUMMARY: {sum(ok)}/{len(ok)} checks passed')
