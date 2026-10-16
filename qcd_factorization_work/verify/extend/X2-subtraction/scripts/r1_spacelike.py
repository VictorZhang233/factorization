"""X2 fix round 1 / r1_spacelike.py -- space-like rapidity regulators in the soft subtraction term of the massive-photon
vertex (model M3): there is NO Landau pinch; the real-base fibered density has a simple pole with a definite i0, which is
integrable as a distribution and removed by deforming k+ into the upper half plane; what fails is only absolute
integrability on the real fibered base ((H3^phi) in this fibration).  Replaces the '[R] (pinch analysis)' of X2-Prop3.14.

C_S = 1/(G h1Y h2Y),  G = M^2 - k^2 - i0,  h1Y = 2P(k^- - e^{-2Y}k^+) - i0,  h2Y = 2P'(k^+ - e^{-2Y}k^-) - i0  (t16, sgn=-1).
(a) Landau equations, symbolic.  (b) closed form of rho_{C_S}(x,kap) vs the lcpt engine.  (c) |rho| not integrable
across x0(kap) = sqrt((M^2+kap) e^{2Y}/2); the integral along the real axis with the i0 prescription equals the integral
along a contour deformed into Im x > 0 (finite, smooth integrand)."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, sympy as sp, mpmath as mp
import t16_massive_regulated as T16

# ---------------- (a) Landau analysis ----------------
print("(a) Landau equations for C_S with space-like n_A, n_B:")
P_, Pp_, Y_ = sp.symbols('P Pp Y', positive=True)
nA = sp.Matrix([2*P_, -2*P_*sp.exp(-2*Y_)])     # (n^+, n^-):  n_A.k = n^+ k^- + n^- k^+ = 2P(k^- - e^{-2Y} k^+)
nB = sp.Matrix([-2*Pp_*sp.exp(-2*Y_), 2*Pp_])    # n_B.k = 2P'(k^+ - e^{-2Y} k^-)
dot = lambda a, b: a[0]*b[1] + a[1]*b[0]          # light-cone part (transverse components of n vanish)
gram = sp.Matrix([[dot(nA, nA), dot(nA, nB)], [dot(nA, nB), dot(nB, nB)]])
print("   n_A^2 =", sp.simplify(dot(nA, nA)), "  n_B^2 =", sp.simplify(dot(nB, nB)), "  (both < 0: space-like)")
print("   Gram determinant =", sp.factor(sp.simplify(gram.det())), "  (non-zero for Y > 0)")
print("   (i) {G, h1Y}: -2 a_G k + a_1 n_A = 0  =>  k = (a_1/2a_G) n_A  =>  k^2 = (a_1/2a_G)^2 n_A^2 <= 0,  but G = 0 needs"
      " k^2 = M^2 > 0: no solution; a_G = 0 forces a_1 = 0.")
print("   (ii) {G, h1Y, h2Y}: k = (a_1 n_A + a_2 n_B)/2a_G with n_A.k = n_B.k = 0  =>  Gram.(a_1,a_2) = 0  =>  a_1 = a_2 = 0,"
      " k = 0, G = M^2 != 0: no solution.  (iii) {h1Y}, {h2Y}, {h1Y,h2Y} alone: gradients n_A, n_B independent: none.")
print("   => no pinch (no Landau singularity at finite k) of the 4D integral of C_S.")

# ---------------- (b) closed form of the fibered density ----------------
P = Pp = 1/np.sqrt(2)
def rho_closed(x, kap, M2, Y, eta=0.0):
    """residue at the h1Y pole (upper half plane), x > 0:  rho = (2/(2P)) / [(M2 + kap - 2 e^{-2Y} x^2 - i eta) 2P' x (1 - e^{-4Y})]"""
    e = np.exp(-2*Y)
    return (1.0/P)/((M2 + kap - 2*e*x**2 - 1j*eta)*2*Pp*x*(1 - e*e))
M2, Y, kap = 1e-3, 3.0, 0.01
x0 = np.sqrt((M2 + kap)*np.exp(2*Y)/2)
xs = x0*(1 + np.array([-0.3, -1e-2, -1e-3, 1e-3, 1e-2, 0.3]))
eng = T16.rho('C_S', xs, kap*np.ones_like(xs), M2, Y, -1)
print("\n(b) closed form vs lcpt engine (space-like, M2=1e-3, Y=3, kap=0.01, x0=%.6f):" % x0)
for x_, e_ in zip(xs, eng):
    print(f"   x/x0 = {x_/x0:.4f}: engine {e_:+.6e}   closed {np.real(rho_closed(x_, kap, M2, Y)):+.6e}")

# ---------------- (c) non-absolute integrability on the real base vs deformed base ----------------
mp.mp.dps = 30
def f_c(z):      # analytic continuation of rho in x (pole at x0, other singularities at x = 0, -x0)
    e = mp.e**(-2*Y)
    return (1/mp.mpf(P))/((M2 + kap - 2*e*z**2)*2*Pp*z*(1 - e*e))
a, b = x0/2, 2*x0
print("\n(c) x-integral over [x0/2, 2 x0] at fixed kap:")
for d in [1e-2, 1e-4, 1e-6, 1e-8]:
    I_abs = mp.quad(lambda t: abs(f_c(t)), [a, x0*(1 - d)]) + mp.quad(lambda t: abs(f_c(t)), [x0*(1 + d), b])
    print(f"   int |rho| dx excluding |x-x0| < {d:g} x0 : {mp.nstr(I_abs, 8)}   (grows like 2|Res| ln(1/d): not absolutely integrable)")
# real axis with the -i0 of G (pole at x0 - i0'): PV + i pi * (residue contribution with the correct sign)
eps_ = 1e-12
pv = mp.quad(f_c, [a, x0*(1 - 1e-9)]) + mp.quad(f_c, [x0*(1 + 1e-9), b])
res = mp.limit(lambda z: (z - x0)*f_c(z), x0) if False else (1/mp.mpf(P))/((-4*mp.e**(-2*Y)*x0)*2*Pp*x0*(1 - mp.e**(-4*Y)))
# 1/(c(x) - i0) with c decreasing through x0:  = Res/(x - x0 + i0)  -> PV - i pi Res delta
I_i0 = pv - 1j*mp.pi*res
for eta in [1e-4, 1e-6, 1e-8]:
    I_eta = mp.quad(lambda t: (1/mp.mpf(P))/((M2 + kap - 2*mp.e**(-2*Y)*t**2 - 1j*eta)*2*Pp*t*(1 - mp.e**(-4*Y))), [a, x0*(1-1e-3), x0, x0*(1+1e-3), b])
    print(f"   real axis, finite i*eta = {eta:g} in G:  {mp.nstr(I_eta, 10)}")
print(f"   PV - i pi Res (eta -> 0 limit)       :  {mp.nstr(I_i0, 10)}")
# deformed contour: a -> b along the upper semicircle centred at x0 with radius r = x0/2 (passes ABOVE the pole x0 - i0)
r = x0/2
arc = mp.quad(lambda th: f_c(x0 + r*mp.e**(1j*th))*1j*r*mp.e**(1j*th), [mp.pi, 0])
I_def = mp.quad(f_c, [a, x0 - r]) + arc + mp.quad(f_c, [x0 + r, b])
print(f"   contour deformed into Im x > 0         :  {mp.nstr(I_def, 10)}   (integrand bounded on the contour)")
print("   => equality: the real-base pole is a removable (deformable) singularity, not a pinch; only the absolute"
      " integrability on the REAL fibered base fails ((H3^phi) in this fibration).")
# time-like comparison: no pole on the real base
xs2 = x0*(1 + np.array([-1e-2, 1e-2]))
print("\n   time-like rho_{C_S} near the same x (bounded):", T16.rho('C_S', xs2, kap*np.ones_like(xs2), M2, Y, +1))
