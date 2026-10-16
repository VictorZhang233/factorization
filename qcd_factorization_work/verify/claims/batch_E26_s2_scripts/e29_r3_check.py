"""
e29_r3_check.py -- stage-2 verifier (batch E26_s2), claim E29 (corrected O(alpha_s^3) R-ratio).

Source of the analytic input (read from the arXiv source, not recalled): Surguladze & Samuel,
Rev. Mod. Phys. 68 (1996) 259 [hep-ph/9508351], eqs. (Ranalytic0) (general group, light-by-light term)
and (Ranalytic1) (SU(3), MS-bar, mu^2 = s, a = alpha_s(s)/pi):
  R = 3 sum Q^2 { 1 + a + a^2 [365/24 - 11 z3 - N(11/12 - 2/3 z3)]
        + a^3 [87029/288 - 121/8 z2 - 1103/4 z3 + 275/6 z5
               + N(-7847/216 + 11/6 z2 + 262/9 z3 - 25/9 z5) + N^2(151/162 - 1/18 z2 - 19/27 z3)] }
      + (sum Q)^2 a^3 [55/72 - 5/3 z3]
  general group singlet term: (alpha_s/4pi)^3 (sum Q)^2 (d_abc/4)^2 [176/3 - 128 z3].
Checks against the claim: -6.63694 - 1.20013 nf - 0.00518 nf^2 - 1.2395 eta, eta = (sum Q)^2/(3 sum Q^2);
against GKL 1991 (PLB 259, 144; abstract): R = 11/3 [1 + a + 1.409 a^2 - 12.805 a^3] for nf = 5;
against PDG 2025 (QCD review eq. (9.9b)): c3 = -6.63694 - 1.20013 nf - 0.00518 nf^2 - 1.240 eta.
Run: python3 -I e29_r3_check.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np

N = sp.symbols('n_f')
z2, z3, z5 = sp.zeta(2), sp.zeta(3), sp.zeta(5)
ok_all = []


def ok(name, cond):
    ok_all.append(bool(cond))
    print(('PASS  ' if cond else 'FAIL  ') + name)


r2 = sp.Rational(365, 24) - 11 * z3 - N * (sp.Rational(11, 12) - sp.Rational(2, 3) * z3)
r3 = (sp.Rational(87029, 288) - sp.Rational(121, 8) * z2 - sp.Rational(1103, 4) * z3 + sp.Rational(275, 6) * z5
      + N * (-sp.Rational(7847, 216) + sp.Rational(11, 6) * z2 + sp.Rational(262, 9) * z3 - sp.Rational(25, 9) * z5)
      + N ** 2 * (sp.Rational(151, 162) - sp.Rational(1, 18) * z2 - sp.Rational(19, 27) * z3))
rS = sp.Rational(55, 72) - sp.Rational(5, 3) * z3

c = sp.Poly(sp.expand(r3), N).all_coeffs()[::-1]
cn = [sp.N(x, 15) for x in c]
print('r3 (non-singlet) = %.6f + (%.6f) nf + (%.7f) nf^2' % tuple(float(x) for x in cn))
ok('non-singlet constant  -6.63694', abs(float(cn[0]) + 6.63694) < 5e-6)
ok('non-singlet nf coeff  -1.20013', abs(float(cn[1]) + 1.20013) < 5e-6)
ok('non-singlet nf^2 coeff -0.00518', abs(float(cn[2]) + 0.00518) < 5e-6)
print('singlet 55/72 - 5/3 zeta3 = %.6f' % float(sp.N(rS, 15)))
ok('singlet coefficient -1.2395 (PDG: -1.240)', abs(float(sp.N(rS)) + 1.2395) < 5e-5)
c2 = sp.Poly(sp.expand(r2), N).all_coeffs()[::-1]
print('r2 = %.4f + (%.4f) nf' % (float(sp.N(c2[0])), float(sp.N(c2[1]))))
ok('r2 = 1.9857 - 0.1153 nf', abs(float(sp.N(c2[0])) - 1.9857) < 5e-5 and abs(float(sp.N(c2[1])) + 0.1153) < 5e-5)

# pi^2 terms are the analytic-continuation terms -(pi^2/3) beta0^2, beta0 = (11 - 2nf/3)/4
beta0 = (11 - sp.Rational(2, 3) * N) / 4
z2part = sp.expand(r3).coeff(z2) if False else sp.expand(sp.expand(r3).subs({z3: 0, z5: 0}) - sp.expand(r3).subs({z2: 0, z3: 0, z5: 0}))
ok('zeta2 terms of r3 = -(pi^2/3) beta0^2', sp.simplify(z2part + sp.pi ** 2 / 3 * beta0 ** 2) == 0)

# general-group singlet term -> SU(3):  (1/64)(dabc dabc/16)(176/3 - 128 z3) with dabc dabc = 40/3
l = np.zeros((8, 3, 3), dtype=complex)
l[0][0, 1] = l[0][1, 0] = 1
l[1][0, 1] = -1j; l[1][1, 0] = 1j
l[2][0, 0] = 1; l[2][1, 1] = -1
l[3][0, 2] = l[3][2, 0] = 1
l[4][0, 2] = -1j; l[4][2, 0] = 1j
l[5][1, 2] = l[5][2, 1] = 1
l[6][1, 2] = -1j; l[6][2, 1] = 1j
l[7] = np.diag([1, 1, -2]) / np.sqrt(3)
d = np.zeros((8, 8, 8))
for a in range(8):
    for b in range(8):
        ac = l[a] @ l[b] + l[b] @ l[a]
        for cc in range(8):
            d[a, b, cc] = np.real(np.trace(ac @ l[cc])) / 4      # {l_a,l_b} = 4/3 delta + 2 d_abc l_c
dd = np.sum(d * d)
print('d_abc d_abc (SU(3), numeric) = %.12f' % dd)
ok('d_abc d_abc = 40/3', abs(dd - 40 / 3) < 1e-10)
rS_gen = sp.Rational(1, 64) * (sp.Rational(40, 3) / 16) * (sp.Rational(176, 3) - 128 * z3)
ok('general-group singlet term reduces to 55/72 - 5/3 zeta3', sp.simplify(rS_gen - rS) == 0)

# eta normalisation and totals
quarks = [sp.Rational(2, 3), -sp.Rational(1, 3), -sp.Rational(1, 3), sp.Rational(2, 3), -sp.Rational(1, 3), sp.Rational(2, 3)]
print('\n nf   eta        r3_total(a^3 coefficient of R/(3 sum Q^2))')
tot = {}
for nf in range(3, 7):
    Q = quarks[:nf]
    sQ, sQ2 = sum(Q), sum(q * q for q in Q)
    eta = sQ ** 2 / (3 * sQ2)
    # (sum Q)^2 rS = 3 sum Q^2 * eta * rS
    ok('nf=%d: (sum Q)^2 rS == 3 sum Q^2 * eta * rS' % nf, sp.simplify(sQ ** 2 * rS - 3 * sQ2 * eta * rS) == 0)
    val = sp.N(r3.subs(N, nf) + eta * rS, 12)
    tot[nf] = float(val)
    claim = -6.63694 - 1.20013 * nf - 0.00518 * nf ** 2 - 1.2395 * float(eta)
    print('  %d  %-9s  %.6f   (claim formula: %.6f)' % (nf, str(eta), float(val), claim))
ok('nf = 5 total -12.805 (GKL 1991 abstract)', abs(tot[5] + 12.805) < 5e-4)
print('\nALL PASS' if all(ok_all) else '\nSOME CHECKS FAILED')
