"""E29 -- O(alpha_s^3) coefficient of R(s) in MS-bar at mu^2 = s, a = alpha_s/pi.

Non-singlet analytic form as printed in Chetyrkin-Kuehn-Kwiatkowski, Phys. Rept. 277 (1996) 189
(hep-ph/9503396), eq. (ns1), in powers of alpha_s/(4 pi):
  r3 * 64 = 174058/9 - 17648 z3 + 8800/3 z5
            + nf (-62776/27 + 16768/9 z3 - 1600/9 z5) + nf^2 (4832/81 - 1216/27 z3)
            - (484/3 - 176/9 nf + 16/27 nf^2) pi^2
Singlet (light-by-light): CKK eq. (sm0v1)/(num7) and Baikov-Chetyrkin-Kuehn PLB 714 (2012) 62
(arXiv:1206.1288) eq. (Rqcd):  R contains (sum_f q_f)^2 a^3 (55/72 - 5/3 z3).
Group theory check: (sum q)^2 * d_R * d3^SI with d3^SI = (d^abc d^abc / d_R)(11/192 - z3/8),
d^abc d^abc = 40/3 for SU(3) (d^abc = 2 Tr({t^a,t^b} t^c)), d_R = 3.
Also: the pi^2 term equals -(pi^2/3) b0^2 with b0 = beta0/4 = (11 - 2 nf/3)/4 (continuation of the
Adler function), and d3 = r3 + (pi^2/3) b0^2 reproduces the known Adler coefficient.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

nf = sp.symbols('n_f')
z3, z5 = sp.zeta(3), sp.zeta(5)
r3 = (sp.Rational(174058, 9) - 17648 * z3 + sp.Rational(8800, 3) * z5
      + nf * (sp.Rational(-62776, 27) + sp.Rational(16768, 9) * z3 - sp.Rational(1600, 9) * z5)
      + nf ** 2 * (sp.Rational(4832, 81) - sp.Rational(1216, 27) * z3)
      - (sp.Rational(484, 3) - sp.Rational(176, 9) * nf + sp.Rational(16, 27) * nf ** 2) * sp.pi ** 2) / 64
r3 = sp.expand(r3)
coeffs = [sp.N(r3.coeff(nf, k), 12) for k in range(3)]
print('r3^NS = %.6f %+.6f nf %+.6f nf^2' % tuple(float(c) for c in coeffs))
print('claim:  -6.63694 -1.20013 nf -0.00518 nf^2')

# pi^2 term check
b0 = (11 - sp.Rational(2, 3) * nf) / 4
pi2part = sp.expand(-(sp.pi ** 2 / 3) * b0 ** 2)
print('pi^2 part of r3 equals -(pi^2/3) b0^2:',
      sp.simplify(pi2part - sp.expand(-(sp.Rational(484, 3) - sp.Rational(176, 9) * nf + sp.Rational(16, 27) * nf ** 2) * sp.pi ** 2 / 64)) == 0)
d3 = sp.expand(r3 - pi2part)
print('Adler d3 = %.4f %+.4f nf %+.4f nf^2' % tuple(float(sp.N(d3.coeff(nf, k))) for k in range(3)))

# singlet
si = sp.Rational(55, 72) - sp.Rational(5, 3) * z3
dabc2, dR = sp.Rational(40, 3), 3
si_group = dR * dabc2 / dR * (sp.Rational(11, 192) - z3 / 8)
print('singlet 55/72 - 5/3 z3 = %.6f ; from group theory d_R*(d^abc d^abc/d_R)(11/192 - z3/8) = %.6f ; equal: %s'
      % (float(si), float(si_group), sp.simplify(si - si_group) == 0))
# CKK form (1/3)(a/4)^3 (d_abc/4)^2 [176/3 - 128 z3] times 3 (num7): = (1/64)(d^abc d^abc/16)(176/3 - 128 z3)
ckk = sp.Rational(1, 64) * dabc2 / 16 * (sp.Rational(176, 3) - 128 * z3)
print('CKK singlet normalization reproduces it:', sp.simplify(ckk - si) == 0)

# n_f = 5 total including singlet, eta = (sum e)^2/(3 sum e^2)
charges = {3: [sp.Rational(2, 3), -sp.Rational(1, 3), -sp.Rational(1, 3)],
           4: [sp.Rational(2, 3), -sp.Rational(1, 3), -sp.Rational(1, 3), sp.Rational(2, 3)],
           5: [sp.Rational(2, 3), -sp.Rational(1, 3), -sp.Rational(1, 3), sp.Rational(2, 3), -sp.Rational(1, 3)]}
for n, qs in charges.items():
    s1, s2 = sum(qs), sum(q ** 2 for q in qs)
    eta = s1 ** 2 / (3 * s2)
    tot = r3.subs(nf, n) + eta * si
    print('nf=%d: 3 sum e^2 = %s, eta = %s, r3^NS = %.4f, r3 total = %.4f' % (n, 3 * s2, eta, float(r3.subs(nf, n)), float(tot)))
print('GKL 1991 abstract (nf=5): R = 11/3 [1 + a + 1.409 a^2 - 12.805 a^3]')
r2 = sp.Rational(365, 24) - 11 * z3 + nf * (-sp.Rational(11, 12) + sp.Rational(2, 3) * z3)
print('r2 = %.5f %+.5f nf ; nf=5: %.4f' % (float(r2.subs(nf, 0)), float(r2.coeff(nf, 1)), float(r2.subs(nf, 5))))
