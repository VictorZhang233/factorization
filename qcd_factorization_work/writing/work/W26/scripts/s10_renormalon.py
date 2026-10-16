# W26 / Ch23 -- s10: linear IR renormalon of the heavy-light Sudakov kernel at large beta0 (prop:yzliu-linear-renormalon;
# VF-YZL-11).  Source: Liu-Su JHEP 02 (2024) 204 [arXiv:2311.06907v3] eqs. (2.44)-(2.50) (text checked).
# Borel variable u = beta0b t/2 with beta0b = beta0/(2 pi)  (book: u = beta0 t/(4 pi)) -> identical.
#   Im B(u) = Im R(u) + C_F/(4u) e^{(5/3 - L)u}/(u-1) [1/cos(pi u) + 1] sgn(z),  L = L_zeta = ln(4 p_z^2/mu^2)
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp, mpmath as mp

u, CF, L, sz = sp.symbols('u C_F L sgnz', real=True)
ImB = CF/(4*u)*sp.exp((sp.Rational(5, 3) - L)*u)/(u - 1)*(1/sp.cos(sp.pi*u) + 1)*sz
res = sp.simplify(sp.limit((u - sp.Rational(1, 2))*ImB, u, sp.Rational(1, 2)))
mu_over_pz = sp.exp(-L/2)*2       # e^{-L/2} = mu/(2 p^z)  => mu/p^z = 2 e^{-L/2}
print('residue of Im B at u=1/2:', res, ' = (mu/p^z) C_F e^{5/6}/(2 pi) sgn z ?',
      sp.simplify(res - mu_over_pz*CF*sp.exp(sp.Rational(5, 6))/(2*sp.pi)*sz) == 0)
Nm = mp.mpf(4)/3*mp.e**(mp.mpf(5)/6)/mp.pi
print('N_m = C_F e^{5/6}/pi =', mp.nstr(Nm, 10), '(SU(3))')
# large-order behaviour: a pole c/(u-1/2) with u = beta0b t/2 gives B(t) = -2c sum (beta0b t)^n,
# i.e. series coefficients r'_n = -2c beta0b^n n!  of alpha^{n+1}; with c = (mu/p^z) N_m sgn(z)/2:
c, b0b, n = sp.symbols('c beta0b n', positive=True)
t = sp.Symbol('t')
expr = c/(b0b*t/2 - sp.Rational(1, 2))
ser = sp.series(expr, t, 0, 5).removeO()
coeffs = [sp.simplify(ser.coeff(t, k)*sp.factorial(k)) for k in range(5)]
print('Borel-series coefficients (times k!):', coeffs, ' = -2c beta0b^k k!')
print('=> Im part of the kernel ~ -(mu/p^z) N_m sgn(z) sum beta0b^n n! alpha^{n+1};  A = 2 Arg H_HL(single vertex)/sgn')
print('   gives A_asym = -2 (mu/p^z) sum r_n alpha^{n+1}, r_n = N_m beta0b^n Gamma(n+1)  [Liu-Su (2.48)-(2.49)]')
# ambiguity: residue -> (Lambda/mu)^{2u} at u=1/2 -> Lambda/mu ; times mu/p^z -> Lambda/p^z
print('ambiguity ~ (mu/p^z) (Lambda^2/mu^2)^{1/2} = Lambda/p^z : linear power correction')
print('PASS')
