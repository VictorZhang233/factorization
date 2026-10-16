r"""
w06_pi2_table.py -- writer W06: numbers for ex:ee-pi2 (tab:ee-pi2).
r3 (literature; GKL 1991 / Surguladze-Samuel 1991, verified as E29): r3 = -6.63694 - 1.20013 nf - 0.00518 nf^2 - 1.2395 eta,
eta = (sum e_q)^2/(3 sum e_q^2); pi^2 term from the contour formula: -(pi^2/3) b0^2 d1, b0 = beta0/4, d1 = 1 (SU(3));
d3 = r3 + (pi^2/3) b0^2 d1 (writer-derived from the structural relation of VF-EE-9).
Also r2 = 365/24 - 11 zeta3 - nf (11/12 - 2/3 zeta3) and the exact singlet coefficient 55/72 - 5/3 zeta3.
Run: python3 -I w06_pi2_table.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
z3 = sp.zeta(3)
charges = [sp.Rational(2, 3), -sp.Rational(1, 3), -sp.Rational(1, 3), sp.Rational(2, 3), -sp.Rational(1, 3)]
sing = sp.Rational(55, 72) - sp.Rational(5, 3) * z3
print('singlet coefficient 55/72 - 5/3 zeta3 = %.5f' % float(sing))
for nf in (3, 4, 5):
    ch = charges[:nf]
    eta = sum(ch) ** 2 / (3 * sum(q ** 2 for q in ch))
    b0 = (11 - sp.Rational(2, 3) * nf) / 4
    pi2 = sp.pi ** 2 / 3 * b0 ** 2
    r3ns = -6.63694 - 1.20013 * nf - 0.00518 * nf ** 2
    r3s = float(sing * eta)
    r3 = r3ns + r3s
    d3 = r3 + float(pi2)
    r2 = sp.Rational(365, 24) - 11 * z3 - nf * (sp.Rational(11, 12) - sp.Rational(2, 3) * z3)
    R0 = 3 * sum(q ** 2 for q in ch)
    print('nf=%d: R0=%s eta=%s b0=%s  (pi^2/3)b0^2=%.3f  r2=%.4f  r3_ns=%.3f  r3_singlet=%.4f  r3=%.3f  d3=%.3f  pi2/|r3|=%.2f'
          % (nf, R0, eta, b0, float(pi2), float(r2), r3ns, r3s, r3, d3, float(pi2) / abs(r3)))
