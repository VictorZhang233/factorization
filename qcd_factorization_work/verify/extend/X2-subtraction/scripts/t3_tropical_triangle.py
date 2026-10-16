"""X2/T3: monomial (tropical) majorant of the triangle remainder density on 0<x<P and x>P.
|rho_r| <= M(x,kap) := sum_monomials |c| mon / |den|  (exact den, all factors of fixed sign on the range).
Check numerically that int M ~ lambda^2 L, i.e. the majorant is sharp up to a constant; then the rigorous
bound reduces to an LP (Newton polytope) argument (REPORT Lemma B.6)."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp, numpy as np, warnings
from scipy import integrate
warnings.filterwarnings('ignore')
x, kap, m2 = sp.symbols('x kap m2', positive=True)
P = sp.sqrt(2)/2; Pp = sp.sqrt(2)/2       # Qt^2 = 1
A = x*m2*(1 - x/P) + P*kap
B = x*m2 + P*kap
e2 = m2 + 2*Pp*x; h2 = 2*Pp*x
Dhat2 = e2*(1 + m2 + kap/(1 - x/P)) + kap
rG = 1/(A*Dhat2); rS = 1/(B*e2); rC1 = x*m2/(A*B); rC2 = -(1/P)/((e2 + kap)*e2)
rH = -x/(P*(h2 + kap)*(h2*(P - x) + P*kap))
for name, expr in [('mid', rG - rS - rC1 - rC2 - rH), ('big', -rS + 1/(h2*B) - rC2 - 1/(P*(h2+kap)*h2))]:
    num, den = sp.fraction(sp.together(expr))
    num = sp.expand(num); den = sp.factor(den)
    poly = sp.Poly(num, x, kap, m2)
    absnum = sum(abs(float(c))*x**i*kap**j*m2**k for (i, j, k), c in zip(poly.monoms(), poly.coeffs()))
    fM = sp.lambdify((x, kap, m2), absnum/sp.Abs(den), 'numpy')
    fr = sp.lambdify((x, kap, m2), num/den, 'numpy')
    print(f"range {name}: numerator has {len(poly.coeffs())} monomials; den = {den}")
    Pv = float(P)
    for k in [4, 6, 8, 10]:
        lam2 = 10.0**(-k); L = np.log(1/lam2)
        xlo, xhi = (1e-30, Pv) if name == 'mid' else (Pv, 1e12)
        def g(lk, lx, f):
            xx = np.exp(lx); kk = np.exp(lk)
            return abs(f(xx, kk, lam2))*xx*kk
        vals = []
        for f in (fM, fr):
            v, e = integrate.dblquad(lambda lk, lx: g(lk, lx, f), np.log(xlo), np.log(xhi), lambda lx: np.log(1e-40), lambda lx: np.log(1e14), epsrel=1e-7)
            vals.append(v)
        print(f"   lam2=1e-{k}: int M = {vals[0]:.4e} = {vals[0]/(lam2*L):.4f} lam2 L ;  int|r| = {vals[1]:.4e} = {vals[1]/(lam2*L):.4f} lam2 L ; ratio M/|r| = {vals[0]/vals[1]:.3f}")
