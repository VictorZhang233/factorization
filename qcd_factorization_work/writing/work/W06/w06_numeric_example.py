r"""
w06_numeric_example.py -- writer W06: numbers for the illustration in ex:ee-pi2.

alpha_s(M_Z) = 0.1180 (PDG 2024, VF-QCD-7), M_Z = 91.19 GeV, n_f = 5; exact two-loop running
   mu^2 d a_s/d mu^2 = -beta0/(4pi) a_s^2 - beta1/(4pi)^2 a_s^3,  beta0 = 23/3, beta1 = 116/3,
to sqrt(s) = 20 GeV (compare the VF-QCD-7 table: 0.1533).  Then a = alpha_s/pi and the terms of
   R/R_0 = 1 + a + r2 a^2 + r3 a^3,  r2 = 1.9857 - 0.1153 n_f,  r3 = -12.805 (n_f = 5, incl. singlet),
and the split of r3 a^3 into the pi^2 term -(pi^2/3) b0^2 a^3 and d3 a^3.
Run: python3 -I w06_numeric_example.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp

mp.mp.dps = 30
RES = []


def check(name, cond):
    RES.append((name, bool(cond)))
    print(('PASS  ' if cond else 'FAIL  ') + name)


nf = 5
beta0 = mp.mpf(11) - mp.mpf(2) * nf / 3
beta1 = mp.mpf(102) - mp.mpf(38) * nf / 3
check('beta0 = 23/3, beta1 = 116/3 for n_f = 5', abs(beta0 - mp.mpf(23) / 3) < 1e-25 and abs(beta1 - mp.mpf(116) / 3) < 1e-25)


def run(alpha0, mu0, mu):
    # integrate in tau = -ln mu^2 (increasing when running down from mu0 to mu < mu0)
    f = lambda tau, y: [(beta0 / (4 * mp.pi)) * y[0] ** 2 + (beta1 / (4 * mp.pi) ** 2) * y[0] ** 3]
    sol = mp.odefun(f, -mp.log(mu0 ** 2), [alpha0])
    return sol(-mp.log(mu ** 2))[0]


aMZ = mp.mpf('0.1180')
a20 = run(aMZ, mp.mpf('91.19'), mp.mpf(20))
print('alpha_s(20 GeV), exact two loop =', mp.nstr(a20, 6))
check('alpha_s(20 GeV) = 0.1533 (VF-QCD-7 table)', abs(a20 - mp.mpf('0.1533')) < 5e-5)
a = a20 / mp.pi
r2 = mp.mpf('1.9857') - mp.mpf('0.1153') * nf
r3 = mp.mpf('-12.805')
b0 = beta0 / 4
pi2 = mp.pi ** 2 / 3 * b0 ** 2
d3 = r3 + pi2
terms = [a, r2 * a ** 2, r3 * a ** 3]
print('a =', mp.nstr(a, 6), ' terms:', [mp.nstr(t, 4) for t in terms], ' R/R0 =', mp.nstr(1 + sum(terms), 6))
print('pi^2 part of r3 a^3:', mp.nstr(-pi2 * a ** 3, 4), '  d3 part:', mp.nstr(d3 * a ** 3, 4), ' (pi2 =', mp.nstr(pi2, 6), ')')
check('terms: a = 0.0488, r2 a^2 = 0.0034, r3 a^3 = -0.0015', abs(terms[0] - mp.mpf('0.0488')) < 5e-5 and
      abs(terms[1] - mp.mpf('0.0034')) < 5e-5 and abs(terms[2] + mp.mpf('0.0015')) < 5e-5)
check('pi^2 part of the a^3 term = -0.0014, d3 part = -0.0001', abs(-pi2 * a ** 3 + mp.mpf('0.0014')) < 5e-5
      and abs(d3 * a ** 3 + mp.mpf('0.0001')) < 5e-5)
npass = sum(1 for _, c in RES if c)
print(f'\nSUMMARY: {npass}/{len(RES)} checks passed')
