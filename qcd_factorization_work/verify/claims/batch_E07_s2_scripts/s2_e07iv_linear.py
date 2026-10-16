# E07(iv) stage-2 check: origin and coefficient of the linear divergence Lambda/((1-x)^2 P^z) in the
# one-loop quasi-PDF with a transverse-momentum cutoff |k_perp| < Lambda (Xiong-Ji-Zhang-Zhao 2014, eq. (7):
# (as C_F/2pi) * mu/((1-x)^2 P^z), mu = transverse cutoff), derived independently from the Feynman-gauge
# self-energy of the straight space-like Wilson line.
#   log W(z) = -g^2 C_F int d^3k/((2pi)^3 2|k|) (1 - cos(k_z z))/k_z^2       (one loop, Feynman gauge, n^2=-1)
#   qtilde_tad(x) = P^z/(2pi) int dz e^{i(x-1)P^z z} log W(z)   (tree level normalised to delta(1-x))
# For x != 1 the cos term gives  g^2 C_F P^z/q^2 int_{|k_perp|<Lambda} d^2k_perp/((2pi)^3 2 sqrt(k_perp^2+q^2)),
# q = (x-1) P^z.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
kp, q, Lam, Pz, x, aS, CF = sp.symbols('k_p q Lambda P_z x alpha_s C_F', positive=True)
g2 = 4*sp.pi*aS
I_perp = sp.integrate(2*sp.pi*kp/(2*sp.sqrt(kp**2 + q**2)), (kp, 0, Lam))   # int d^2k_perp /(2 sqrt(k^2+q^2))
qt = sp.simplify(g2*CF*Pz/q**2 * I_perp/(2*sp.pi)**3)
print('qtilde_tad(x != 1) =', qt)
ser = sp.series(qt.subs(q, (1 - x)*Pz), Lam, sp.oo, 2)
print('large-Lambda expansion:', sp.simplify(ser))
lin = sp.limit(qt.subs(q, (1 - x)*Pz)/Lam, Lam, sp.oo)
print('coefficient of Lambda:', sp.factor(lin), ' ;  expected (as C_F/(2 pi)) /((1-x)^2 P_z):',
      sp.simplify(lin - aS*CF/(2*sp.pi)/((1 - x)**2*Pz)) == 0)
# delta m from the coordinate-space picture: log W = -dm |z| + ..., dm = g^2 C_F int_0^inf ds D(s) = g^2 C_F Lambda/(8 pi)
dm = g2*CF*Lam/(8*sp.pi)
print('delta m =', sp.simplify(dm), ' ; FT of -dm|z| with P^z/(2pi): dm/(pi (1-x)^2 P_z) =', sp.simplify(dm/(sp.pi*(1 - x)**2*Pz)))
