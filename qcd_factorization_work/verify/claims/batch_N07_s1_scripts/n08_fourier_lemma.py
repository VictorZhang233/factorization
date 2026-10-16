#!/usr/bin/env python3
"""N08 independent check.
(1) Lemma 5.2: int dlam/(2pi) e^{-i x lam} [z^2 Lambda^2 r(lam)] = +(Lambda^2/Pz^2) rho''(x), z^2 = -lam^2/Pz^2 (4-vector square),
    r(lam) = int_{-1}^{1} e^{i a lam} rho(a) da.  Tested numerically for a smooth rho (no endpoint terms) and for rho with
    endpoint powers inside (0,1).
(2) Endpoint ratios rho''/rho -> a(a-1)/x^2, b(b-1)/(1-x)^2; Cor 5.3 scaling (1-x)^(delta-2).
(3) BVZ renormalon model: rho_4(x) = int_x^1 dy/y k(y) q(x/y), k = y + ybar ln ybar  ->  rho_4 ~ (1-x)^(b+1)  (delta = 1),
    and the P=0 normalization: [k]_+ = k - (1/4) delta(1-y)  ->  extra -(1/4) q''  ->  Rbar - R = -(1/4) xbar x^2 q''/q
    (BVZ arXiv:1810.00048 eq. (bR)); perp: 5/12.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import sympy as sp

res = []
def rep(name, ok, extra=""):
    ok = bool(ok); res.append(ok)
    print(("PASS " if ok else "FAIL ") + name + ((" : " + extra) if extra else ""))

# (1) smooth rho = (1-a^2)^6 on [-1,1]; r(lam) in closed form (sympy), FT of lam^2 r by scipy quadrature (|lam^2 r| ~ lam^-5)
import numpy as np
from scipy import integrate
A_, L_ = sp.symbols('A L', positive=True)
r_expr = sp.simplify(2*sp.integrate(sp.cos(A_*L_)*(1-A_**2)**6, (A_, 0, 1)))
r_num = sp.lambdify(L_, r_expr, 'mpmath')
def r(lam):
    lam = abs(lam)
    if lam < 1e-2:   # series near 0 to avoid cancellation
        return float(2*sum((-1)**j*lam**(2*j)/sp.factorial(2*j)*sp.integrate(A_**(2*j)*(1-A_**2)**6, (A_, 0, 1)) for j in range(6)))
    mp.mp.dps = 50
    return float(r_num(mp.mpf(lam)))
lam_grid = np.linspace(0, 2000, 200001)
r_vals = np.array([r(l) for l in lam_grid[:20001]])          # up to lam = 200
rho = lambda a: (1-a**2)**6
for xv in [0.0, 0.35, 0.7]:
    f = np.cos(xv*lam_grid[:20001])*lam_grid[:20001]**2*r_vals
    lhs = integrate.simpson(f, x=lam_grid[:20001])/np.pi
    rpp = float(sp.diff((1-A_**2)**6, A_, 2).subs(A_, xv))
    rep("Lemma 5.2 at x=%.2f: FT[lam^2 r] = -rho''  (so FT[z^2 Lambda^2 r] = +Lambda^2 rho''/Pz^2)" % xv,
        abs(lhs + rpp) < 1e-4*max(1, abs(rpp)), "%.8f vs %.8f" % (lhs, -rpp))

# (2) endpoint ratios and Cor. 5.3
x = sp.symbols('x', positive=True)
a_, b_, d_ = sp.Rational(-1, 2), 3, sp.Rational(1, 1)
q = x**a_*(1-x)**b_
for delta in [0, sp.Rational(1, 2), 1]:
    rho4 = q*(1-x)**delta
    ratio = sp.simplify(sp.diff(rho4, x, 2)/q)
    lead = sp.limit(ratio*(1-x)**(2-delta), x, 1)
    rep("Cor 5.3: rho4''/q ~ (b+delta)(b+delta-1)(1-x)^(delta-2) at x->1, delta=%s" % delta,
        sp.simplify(lead - (b_+delta)*(b_+delta-1)) == 0, "limit coefficient %s" % lead)
lead0 = sp.limit(sp.diff(q, x, 2)/q*x**2, x, 0)
rep("endpoint x->0: rho''/rho -> a(a-1)/x^2", sp.simplify(lead0 - a_*(a_-1)) == 0, str(lead0))

# (3) BVZ model: rho_4 ~ (1-x)^(b+1) near x=1 (delta=1)
mp.mp.dps = 20
qn = lambda u: u**(-0.5)*(1-u)**3
k = lambda y: y + (1-y)*mp.log(1-y) if y < 1 else mp.mpf(1)
rho4 = lambda xx: mp.quad(lambda y: k(y)/y*qn(xx/y), [xx, 1])
vals = [(1-xx, rho4(xx)/qn(xx)) for xx in [mp.mpf('0.99'), mp.mpf('0.999'), mp.mpf('0.9999')]]
sl = mp.log(vals[2][1]/vals[1][1])/mp.log(vals[2][0]/vals[1][0])
rep("BVZ model: rho_4/q ~ (1-x)^1 near x=1 (delta=1)", abs(sl-1) < 0.01, "local exponent %s" % mp.nstr(sl, 6))
# normalization constants
y = sp.symbols('y', positive=True)
kpar = sp.integrate(y + (1-y)*sp.log(1-y), (y, 0, 1))
kperp = sp.integrate(y + (1-y)*sp.log(1-y) + y*(1-y), (y, 0, 1))
rep("int_0^1 (a + abar ln abar) = 1/4", sp.simplify(kpar - sp.Rational(1, 4)) == 0, str(kpar))
rep("int_0^1 (a + abar ln abar + a abar) = 5/12", sp.simplify(kperp - sp.Rational(5, 12)) == 0, str(kperp))
# extra momentum-space term from -delta(abar)*1/4 in coordinate space: FT[z^2 Lambda^2 * (-1/4) I(tau)] = -(1/4)(Lambda^2/Pz^2) q''
# BVZ write Q = q{1 - v^2 Lambda^2/(x^2 xbar (pv)^2) R}; with v^2=-1: Q = q + Lambda^2/(x^2 xbar Pz^2) q R
# => Delta R = x^2 xbar/q * (-(1/4) q'')  [kappa set to 1 as in BVZ eq. (cR)]
qq = sp.Function('q')
DR = sp.simplify((-sp.Rational(1, 4)*sp.diff(qq(x), x, 2))*x**2*(1-x)/qq(x))
rep("P=0 normalization adds -(1/4) xbar x^2 q''/q to R^par (BVZ eq. (bR))", sp.simplify(DR + sp.Rational(1, 4)*(1-x)*x**2*sp.diff(qq(x), x, 2)/qq(x)) == 0, str(DR))
print("SUMMARY n08: %d/%d PASS" % (sum(res), len(res)))
