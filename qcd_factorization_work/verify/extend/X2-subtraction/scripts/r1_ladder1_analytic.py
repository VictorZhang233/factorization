"""X2 fix round 1 / r1_ladder1_analytic.py -- (i) leading coefficient of the full light-cone norm of the one-rung DIS
ladder remainder:  int|rho_r| = c1(x) lambda + o(lambda),  c1(x) = 4 int_0^1 dxi xi^{1/2}(1-xi)^{3/2}/(1-xi/x)^2
(from the angle-odd term -2k.q/A^2 [kappa_1 - kappa_0], <|cos|>_{S^3} = 4/(3 pi), int_0^oo (2y+1) y^{-1/2}(1+y)^{-2} dy = 3 pi/2);
compare with t6b (1.26329 lambda at m2 = 1e-7, x = 2).  (ii) Lemma 5.3: closed form of the S^3 average
<1/(a + b cos th)> = 2/(a + sqrt(a^2 - b^2)) (a > |b|), checked by quadrature."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 30
for x in [2, 1.3, 5]:
    c1 = 4*mp.quad(lambda xi: mp.sqrt(xi)*(1 - xi)**1.5/(1 - xi/x)**2, [0, 1])
    print(f"x = {x}: c1 = {mp.nstr(c1, 10)}")
print("check of the two auxiliary integrals:",
      mp.nstr(mp.quad(lambda th: abs(mp.cos(th))*mp.sin(th)**2, [0, mp.pi/2, mp.pi])/(mp.pi/2), 12), "vs 4/(3pi) =", mp.nstr(4/(3*mp.pi), 12), ";",
      mp.nstr(mp.quad(lambda y: (2*y + 1)/(mp.sqrt(y)*(1 + y)**2), [0, 1, mp.inf]), 12), "vs 3pi/2 =", mp.nstr(3*mp.pi/2, 12))
for a, b in [(1, 0.5), (1, 0.99), (3.2, -2.1), (0.7, 0.0)]:
    avg = mp.quad(lambda th: mp.sin(th)**2/(a + b*mp.cos(th)), [0, mp.pi])/(mp.pi/2)
    print(f"S^3 average 1/(a+b cos): a={a}, b={b}: quadrature {mp.nstr(avg, 12)}  closed form {mp.nstr(2/(a + mp.sqrt(a*a - b*b)), 12)}")
