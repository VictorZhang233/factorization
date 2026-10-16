"""W12 (Ch10) -- kinematics of def:disall-breit and the D-dimensional projectors.

Checks:
 1. light-front frame with target mass: q^+ = -x_N P^+, q^- = Q^2/(2 x_N P^+), x_N = 2x/(1+rho),
    rho^2 = 1 + 4 x^2 M^2/Q^2  =>  q^2 = -Q^2 and 2 P.q = Q^2/x exactly; brick-wall frame P^+ = Q/(sqrt2 x_N).
    The naive frame q^+ = -x P^+ gives 2P.q = Q^2/x - x M^2 (only leading power).
 2. (xi P + q)^2 = Q^2 (xi - x)/x for a massless target; in the unphysical region |omega|<1 every line
    k+q with k^+ = xi P^+ (0 < xi <= 1) is off shell by at least Q^2 (1-|omega|) (here x -> 1/omega).
 3. projectors (massless and massive target) by contracting the tensor decomposition in D dimensions
    (VF-DIS-2), and the Born term exact in D (VF-DIS-1).
 4. normalization chain of prop:disall-h2: int dk^- d^{D-2}k_T/(2pi)^D Tr[gamma^+ J] = 2 f, and the LO
    handbag reproduces F_2 = sum e_q^2 x (q + qbar) with the 1/(4 pi) normalization of W.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

x, M, Q, Pp, xi, om = sp.symbols('x M Q P_plus xi omega', positive=True)
eps = sp.Symbol('epsilon')
D = 4 - 2 * eps

def lf_dot(a, b):
    # a = (a+, a-, aT) with aT = 0 here
    return a[0] * b[1] + a[1] * b[0]

print('1. frame with target mass')
rho = sp.sqrt(1 + 4 * x ** 2 * M ** 2 / Q ** 2)
xN = 2 * x / (1 + rho)
P = (Pp, M ** 2 / (2 * Pp))
q = (-xN * Pp, Q ** 2 / (2 * xN * Pp))
print('   q^2 + Q^2           =', sp.simplify(2 * q[0] * q[1] + Q ** 2))
print('   2P.q - Q^2/x        =', sp.simplify(sp.radsimp(2 * lf_dot(P, q) - Q ** 2 / x)))
qn = (-x * Pp, Q ** 2 / (2 * x * Pp))
print('   naive frame: 2P.q   =', sp.simplify(2 * lf_dot(P, qn)), '  (= Q^2/x - x M^2)')
print('   x_N expansion       =', sp.series(xN, M, 0, 4))
q0 = (q[0] + q[1]) / sp.sqrt(2)
PpB = sp.solve(sp.Eq(q0, 0), Pp)
print('   brick wall: q^0 = 0 at P^+ =', [sp.simplify(v) for v in PpB], ' (= Q/(sqrt2 x_N));',
      ' q^3 there =', sp.simplify(((q[0] - q[1]) / sp.sqrt(2)).subs(Pp, PpB[0])))

print('2. current-jet virtuality')
P0 = (Pp, 0)
q0m = (-x * Pp, Q ** 2 / (2 * x * Pp))
k = (xi * Pp, 0)
v = 2 * lf_dot(k, q0m) - Q ** 2
print('   (xi P + q)^2        =', sp.factor(v), ' ; expected Q^2 (xi - x)/x :', sp.simplify(v - Q ** 2 * (xi - x) / x) == 0)
# unphysical region: x = 1/omega, |omega| < 1 -> |xi*omega - 1| >= 1 - |omega|
vv = sp.simplify(v.subs(x, 1 / om) / Q ** 2)
print('   (k+q)^2/Q^2 at x = 1/omega:', vv, ' -> |.| >= 1 - |omega| for 0 < xi <= 1, |omega| < 1')
import random
mn = min(abs(xx * oo - 1) - (1 - abs(oo)) for xx in [random.random() for _ in range(2000)] for oo in [2 * random.random() - 1 for _ in range(10)])
print('   numerical min of |xi omega - 1| - (1-|omega|) over random points:', round(mn, 6), '(>= 0)')
# complex omega in the disc |omega| <= r: |xi omega - 1| >= 1 - xi |omega| >= 1 - r
import cmath
mn = min(abs(xx * r * cmath.exp(1j * th) - 1) - (1 - r) for xx in [random.random() for _ in range(500)]
         for r in [0.95 * random.random() for _ in range(5)] for th in [6.283 * random.random() for _ in range(5)])
print('   complex disc: min of |xi omega - 1| - (1 - |omega|) =', round(mn, 6), '(>= 0)')

print('3. projectors in D dimensions')
F1, F2, FL = sp.symbols('F1 F2 FL')
# contractions of W = (-g + qq/q^2) F1 + Pt Pt F2/(P.q), Pt = P - (P.q/q^2) q, q^2 = -Q^2, P.q = Q^2/(2x)
Pq = Q ** 2 / (2 * x)
def contractions(M2):
    Pt2 = M2 - Pq ** 2 / (-Q ** 2)          # Pt.Pt = M^2 + (P.q)^2/Q^2
    PPt = Pt2                                 # P.Pt = Pt.Pt
    gW = -(D * F1 - F1) + (-1) * 0            # placeholder (replaced below)
    mgW = (D - 1) * F1 - Pt2 / Pq * F2        # -g_{mu nu} W^{mu nu}
    PWP = (-M2 + Pq ** 2 / (-Q ** 2)) * F1 + PPt ** 2 / Pq * F2
    return sp.simplify(mgW), sp.simplify(PWP)
mgW0, PWP0 = contractions(0)
FL0 = F2 - 2 * x * F1
print('   massless: F_L/x = 8x^2/Q^2 PWP           :', sp.simplify(8 * x ** 2 / Q ** 2 * PWP0 - FL0 / x) == 0)
print('   massless: F_2/x = [ -gW + (3-2e) 4x^2/Q^2 PWP ]/(1-e) :',
      sp.simplify((mgW0 + (3 - 2 * eps) * 4 * x ** 2 / Q ** 2 * PWP0) / (1 - eps) - F2 / x) == 0)
mgWM, PWPM = contractions(M ** 2)
r2 = 1 + 4 * x ** 2 * M ** 2 / Q ** 2
FLM = r2 * F2 - 2 * x * F1
print('   massive : F_L/x = 8x^2/(Q^2 rho^2) PWP   :', sp.simplify(8 * x ** 2 / (Q ** 2 * r2) * PWPM - FLM / x) == 0)
print('   massive : rho^2 F_2/x = [2(-gW)+(D-1)F_L/x]/(D-2) :', sp.simplify((2 * mgWM + (D - 1) * FLM / x) / (D - 2) - r2 * F2 / x) == 0)

print('4. Born term and handbag normalization')
# Born: What = (1/4pi) 2pi delta((p+q)^2) (1/2) e^2 Tr[pslash g^mu (pslash+qslash) g^nu]
# -g contraction: (D-2) 4 p.q ;  p p contraction: 0
z, Q2 = sp.symbols('z Q2', positive=True)
pq = Q2 / (2 * z)
delta_factor = z ** 2 / Q2      # delta(Q2 (1-z)/z) = delta(1-z) * z^2/Q2 evaluated at the support (z=1 -> 1/Q2)
F2hat_over_z = (1 / (1 - eps)) * sp.Rational(1, 4) / sp.pi * 2 * sp.pi * sp.Rational(1, 2) * (D - 2) * 4 * pq * delta_factor
print('   Fhat_2/z (coefficient of e_q^2 delta(1-z)) at z=1:', sp.simplify(F2hat_over_z.subs(z, 1)))
print('   convolution: int dxi/xi f(xi) delta(1 - x/xi) = f(x)  [delta(1-x/xi) = x delta(xi - x)]')
# normalization chain: int dk^- d^2k_T/(2pi)^4 e^{i k.w} -> delta(w^+) delta^2(w_T)/(2pi); with the PDF
# f = int dw^-/(4 pi) e^{-i xi P^+ w^-} <..>, the k-integral of Tr[gamma^+ J] equals (1/2pi) * 4 pi f = 2 f
print('   normalization chain: (1/2pi) * (4 pi) =', sp.Rational(1, 2) / sp.pi * 4 * sp.pi, '  -> int Tr[gamma^+ J] = 2 f')
# LO: W = (1/4pi) P^+ int dxi (1/4) Tr[H gamma^-] 2 f = int dxi/xi f (1/4pi)(1/2) Tr[H xi P^+ gamma^-]
print('   P^+ (1/4) 2 = (1/2) * xi P^+ / xi :', sp.simplify(Pp * sp.Rational(1, 4) * 2 - sp.Rational(1, 2) * xi * Pp / xi) == 0)
