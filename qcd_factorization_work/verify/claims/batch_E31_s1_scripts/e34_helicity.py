"""
E34(iv) independent check (verifier stage 1, batch E31): small-x helicity, large-N_c (pure glue), abar = alpha_s N_c/(2 pi).
 (1) BER pure-glue reduction: from BER Z.Phys. C72 (1996) 627 [hep-ph/9603204] eq. (4.8),
       F0/(4 pi^2 omega) = 1 - sqrt(1 - g^2/(2 (pi omega)^2) M0 + g^2/(4 pi (pi omega)^3) G0 F8),
     with F8 = N g^2 d/domega ln(e^{z^2/4} D_p(z)), z = omega/omega0, omega0^2 = N g^2/(8 pi^2) = abar,
     pure glue: M0 = 4N, G0 = N, p = lambda8/N = 2C_A/N = 2  ->  check that
       F0/(8 pi^2) = (omega/2)[1 - sqrt(1 - (16 abar/omega^2)(1 - 3 abar/omega^2)/(1 - abar/omega^2))]   (BK 2023, eq. BER_anom_dim)
 (2) expansions of the BK (2304.06161 eq. (anomalous_dim)) and BER resummed Delta gamma_GG in abar/omega^2;
 (3) intercepts: rightmost branch points; BK analytic form (4/3^{1/3}) sqrt(Re[(-9+i sqrt111)^{1/3}]).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

w, a, g, N = sp.symbols('omega abar g N', positive=True)
z = sp.Symbol('z', positive=True)
# (1) parabolic cylinder D_2(z) = (z^2-1) e^{-z^2/4}; check via the defining ODE y'' + (p + 1/2 - z^2/4) y = 0
D2 = (z**2 - 1)*sp.exp(-z**2/4)
print("(1) D_2 satisfies Weber's equation:", sp.simplify(sp.diff(D2, z, 2) + (2 + sp.Rational(1, 2) - z**2/4)*D2) == 0,
      "; D_2 = 2^{-1} e^{-z^2/4} H_2(z/sqrt2):", sp.simplify(D2 - sp.Rational(1, 2)*sp.exp(-z**2/4)*sp.hermite(2, z/sp.sqrt(2))) == 0)
omega0 = sp.sqrt(N*g**2/(8*sp.pi**2))
F8 = N*g**2*sp.diff(sp.log(sp.exp(z**2/4)*D2).subs(z, w/omega0), w)
M0, G0 = 4*N, N
arg = 1 - g**2/(2*(sp.pi*w)**2)*M0 + g**2/(4*sp.pi*(sp.pi*w)**3)*G0*F8
F0_over_8pi2 = w/2*(1 - sp.sqrt(arg))
gsub = sp.sqrt(8*sp.pi**2*a/N)          # g such that omega0^2 = abar
arg_a = sp.simplify(arg.subs(g, gsub))
target_arg = 1 - (16*a/w**2)*(1 - 3*a/w**2)/(1 - a/w**2)
print("    BER pure-glue square-root argument minus BK's transcription:", sp.simplify(arg_a - target_arg))

# (2) expansions
eps = sp.Symbol('epsilon', positive=True)   # abar -> eps*abar bookkeeping
BK = w/2*(1 - sp.sqrt(1 - (16*a/w**2)*sp.sqrt(1 - 4*a/w**2)))
BER = w/2*(1 - sp.sqrt(target_arg))
for name, expr in [("BK ", BK), ("BER", BER)]:
    s = sp.series(expr.subs(a, eps*a), eps, 0, 6).removeO()
    coeffs = [sp.simplify(s.coeff(eps, k)/(a**k/w**(2*k - 1))) for k in range(1, 6)]
    print(f"(2) {name}: Delta gamma_GG = sum_k c_k abar^k/omega^(2k-1), c_1..c_5 =", coeffs)

# (3) intercepts
u = sp.Symbol('u', positive=True)
# BK: 1 = (16/u) sqrt(1 - 4/u)  ->  u^3 - 256 u + 1024 = 0 (u = omega^2/abar), need u > 4
polyBK = sp.Poly(u**3 - 256*u + 1024, u)
rootsBK = [r for r in polyBK.nroots(n=30) if r.is_real and r > 4]
uBK = max(rootsBK)
check = 1 - (16/uBK)*mp.sqrt(1 - 4/uBK)
alphaBK_closed = 4/mp.cbrt(3)*mp.sqrt(mp.re(mp.cbrt(mp.mpc(-9, mp.sqrt(111)))))
print("(3) BK  : largest root u =", sp.N(uBK, 15), " alpha_h/sqrt(abar) = sqrt(u) =", sp.N(sp.sqrt(uBK), 10),
      " closed form (4/3^{1/3}) sqrt(Re[(-9+i sqrt111)^{1/3}]) =", mp.nstr(alphaBK_closed, 10), " residual:", mp.nstr(check, 3))
uBER = (17 + sp.sqrt(97))/2
print("    BER : u = (17+sqrt97)/2 =", sp.N(uBER, 15), " alpha_h/sqrt(abar) =", sp.N(sp.sqrt(uBER), 10),
      " check u^2-17u+48 =", sp.simplify(uBER**2 - 17*uBER + 48))
print("    relative difference of intercepts:", sp.N((sp.sqrt(uBER) - sp.sqrt(uBK))/sp.sqrt(uBK), 5))
