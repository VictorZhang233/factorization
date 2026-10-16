import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp, numpy as np, mpmath as mp

print("=== E14 (a) massless bubble: Symanzik polynomials ===")
a1, a2, p2 = sp.symbols('alpha1 alpha2 p2', real=True)
# lines q1 = k, q2 = k - p ; D = a1 (k^2) + a2 (k-p)^2 = U k^2 - 2 a2 k.p + a2 p^2
U = a1 + a2
# stationary point k_c = a2 p / U ; D(k_c) = a2 p2 - a2^2 p2/U = a1 a2 p2 / U
Dkc = sp.simplify(a2*p2 - a2**2*p2/U)
F = sp.simplify(-U*Dkc)   # Minkowski convention F = U * sum a_j (m_j^2 - q_j^2) at k_c
print("U =", U, "  F =", sp.factor(F))
H = sp.hessian(F, (a1, a2))
print("Hessian of F in alpha:", H, " -> at p2=0:", H.subs(p2, 0))
print("Landau eqs (alpha_j dF/dalpha_j):", [sp.factor(a1*sp.diff(F, a1)), sp.factor(a2*sp.diff(F, a2))])

print("\n=== E14 (b) momentum-space Landau equations ===")
# k = (k+, k-, kT) light-front; use generic 4-vector components
k0,k1,k2,k3,P0,P3,lam1,lam2 = sp.symbols('k0 k1 k2 k3 P0 P3 lam1 lam2', real=True)
def md(a,b): return a[0]*b[0]-a[1]*b[1]-a[2]*b[2]-a[3]*b[3]
k = [k0,k1,k2,k3]; p = [P0,0,0,P3]
pk = [p[i]-k[i] for i in range(4)]
# lam1 * d(k^2)/dk + lam2 * d((p-k)^2)/dk = 2 lam1 k - 2 lam2 (p-k) = 0
eqs = [lam1*k[i] - lam2*pk[i] for i in range(4)]
sol = sp.solve(eqs, [k0,k1,k2,k3], dict=True)
print("loop equation solution:", sol)
ks = [s.subs(sol[0]) for s in k]
print("k^2 on the solution:", sp.factor(md(ks,ks)), "  (p-k)^2:", sp.factor(md([p[i]-ks[i] for i in range(4)],[p[i]-ks[i] for i in range(4)])))
print("=> both on shell requires p^2 = P0^2-P3^2 = 0; then k = x p with x = lam2/(lam1+lam2) in [0,1] for lam>=0")

print("\n=== E14 (c) mixed momentum-parameter representation ===")
al = sp.symbols('alpha', real=True)
# D(k,alpha) = k^2 - 2 alpha k.p + alpha p^2 ; stationary k = alpha p ; value:
Dst = sp.expand((al**2*p2) - 2*al*(al*p2) + al*p2)
print("D at k=alpha p:", sp.factor(Dst), " -> zero for 0<alpha<1 only if p2 = 0")

print("\n=== E14 (d) pure-parameter representation, n = 4-2eps ===")
eps = sp.symbols('epsilon')
n = 4-2*eps
alpha_int = sp.gamma(n/2-1)**2/sp.gamma(n-2)    # int_0^1 [alpha(1-alpha)]^{n/2-2} = B(n/2-1,n/2-1)
print("alpha integral = B(n/2-1,n/2-1) =", sp.simplify(alpha_int), " (p-independent constant)")
# numeric check of the alpha integral at eps = 0.2
e = 0.2
num = mp.quad(lambda x: (x*(1-x))**(-e), [0, 1])
print("numeric alpha integral at eps=0.2:", num, " vs Beta:", mp.beta(1-e, 1-e))
print("=> Pi(p) = i Gamma(eps) (-p^2-i0)^(-eps) B(1-eps,1-eps)/(4pi)^(2-eps): singular p^2-dependence only in prefactor")

print("\n=== E14 (e) non-relativistic example (Collins App. D.2) ===")
# int domega 1/[(1-2a) omega + c + i eps]^2 = 0 for a != 1/2 (contour closed on the side without the pole)
# analytic: antiderivative -1/(a(a w + b)) is regular on the real axis since Im b > 0
a_, b_, w_, L_ = sp.symbols('a b w L')
prim = -1/(a_*(a_*w_+b_))
for aval in (sp.Rational(1,5), sp.Rational(2,5), sp.Rational(9,20)):
    lim = sp.limit((prim.subs(w_, L_) - prim.subs(w_, -L_)).subs({a_: 1-2*aval, b_: sp.Rational(7,10)+sp.I/10}), L_, sp.oo)
    print("alpha=%s: int domega 1/[(1-2alpha)omega+b]^2 =" % aval, lim)
# alpha-integrated version: int_0^1 dalpha 1/[(1-2alpha)omega+b]^2 = 1/(b^2-omega^2); then int domega = -i pi/b
al_, om_ = sp.symbols('alpha omega', real=True)
bb = sp.symbols('bb')
inner = sp.integrate(1/((1-2*al_)*om_+bb)**2, (al_, 0, 1))
print("int_0^1 dalpha ... =", sp.simplify(inner))
bnum = 0.7+0.1j
val = mp.quad(lambda w: 1/(bnum**2 - w**2), [-mp.inf, -1, 0, 1, mp.inf])
print("int domega 1/(b^2-omega^2) numeric:", complex(val), " -i pi/b:", complex(-1j*mp.pi/bnum))
# full integral check: int domega 1/[(omega-A+i0)(E-omega-B+i0)] = -2 pi i/(E-A-B+i0)
A_, B_, E_ = 0.3, 0.5, 1.4
epsv = 1e-3
f = lambda w: 1/((w - A_ + 1j*epsv)*(E_ - w - B_ + 1j*epsv))
val = mp.quad(f, [-1e5, -10, A_, E_-B_, 10, 1e5])
print("direct omega integral:", complex(val), " expected -2 pi i/(E-A-B+2i eps):", complex(-2j*mp.pi/(E_-A_-B_+2j*epsv)))
# pinch location: Landau with D1 = (1, -k/m), D2 = (-1, (p-k)/m), lam1=lam2 -> p = 2k ; E = p^2/(4m)
m, kk, pp, E = sp.symbols('m k p E', positive=True)
s_ = sp.solve([sp.Eq(-kk/m + (pp-kk)/m, 0)], [kk], dict=True)[0]
w_ = kk**2/(2*m)
Ecrit = sp.simplify((w_ + (pp-kk)**2/(2*m)).subs(s_))
print("non-relativistic pinch: k =", s_[kk], " E_crit =", Ecrit)
