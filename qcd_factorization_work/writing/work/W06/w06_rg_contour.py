r"""
w06_rg_contour.py -- writer W06: RG structure of Pi and R, the contour formula, the pi^2 terms and the
numerical higher-order coefficients quoted in Ch6 (cor:ee-R-alphas, ex:ee-pi2).

Conventions: a = alpha_s(mu)/pi, mu^2 da/dmu^2 = -b0 a^2 - b1 a^3 - b2 a^4, b0 = beta0/4, b1 = beta1/16, b2 = beta2/64.
L = ln(Q^2/mu^2) (Q^2 = -q^2), D(Q^2) = -12 pi^2 Q^2 dPi/dQ^2 = R0 d(a(Q^2)), d = 1 + d1 a + d2 a^2 + ...

 G1  a(Q^2) in terms of a(mu) and L through a^4 (solves the RGE), D mu-independent
 G2  Pi_MS = Pi(0) - (R0/12pi^2) int_0^L d: degree max(1,n) in L at order a^n
 G3  R via L -> ln(s/mu^2) - i pi  ==  contour formula (1/2pi) int_{-pi}^{pi} dtheta D(s e^{i theta})
 G4  r1 = d1, r2 = d2, r3 = d3 - (pi^2/3) b0^2 d1, r4 = d4 - pi^2 (b0^2 d2 + (5/6) b0 b1 d1)
 G5  R^{(n)} in a(mu): polynomial of degree <= n-1 in ln(s/mu^2)
 N1  SU(3) values (pi^2/3) b0^2 = 16.655, 14.279, 12.086 (n_f = 3,4,5)
 N2  r2: general group (BCK 2010, d2 printed there) -> SU(3) 365/24 - 11 zeta3 - n_f(11/12 - 2/3 zeta3) = 1.9857 - 0.1153 n_f
 N3  d3 (BCK 2010 general group, SU(3)) and r3 = d3 - (pi^2/3) b0^2 d1 -> -6.63694 - 1.20013 n_f - 0.00518 n_f^2
     (the literature r3 of GKL 1991 / Surguladze-Samuel 1991; E29 verdict), plus the singlet 55/72 - 5/3 zeta3
 N4  numbers for ex:ee-pi2 (r3, pi^2 term, d3 for n_f = 3,4,5) and the singlet coefficient for n_f=5
 S1  contour formula as an identity for an arbitrary analytic Pi: 2 i Im Pi(s+i0) = Pi(s+i0)-Pi(s-i0) = -(1/12pi^2) int D
Run: python3 -I w06_rg_contour.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

a, L, ell, th = sp.symbols('a L ell theta', real=True)
b0, b1, b2 = sp.symbols('b0 b1 b2', real=True)
d1, d2, d3, d4 = sp.symbols('d1 d2 d3 d4', real=True)
N = 4
RES = []


def check(name, cond):
    RES.append((name, bool(cond)))
    print(('PASS  ' if cond else 'FAIL  ') + name)


def trunc(ex, n=N):
    ex = sp.expand(ex)
    return sum(ex.coeff(a, k) * a ** k for k in range(0, n + 1))


# G1: a(Q^2) as a series in a=a(mu) and L, from da/dL = -b0 a^2 - b1 a^3 - b2 a^4 with a(L=0) = a
cs = [sp.Symbol('c%d' % k) for k in range(N + 1)]
aQ = a
for kk in range(2, N + 1):
    ck = sp.Function('c%d' % kk)(L)
    trial = aQ + ck * a ** kk
    eq_ = sp.expand(sp.diff(trial, L) + b0 * trial ** 2 + b1 * trial ** 3 + b2 * trial ** 4).coeff(a, kk)
    sol = sp.dsolve(sp.Eq(eq_, 0), ck, ics={ck.subs(L, 0): 0})
    aQ = sp.expand(aQ + sol.rhs * a ** kk)
check('G1a a(Q^2) = a - b0 L a^2 + (b0^2 L^2 - b1 L) a^3 + (-b0^3 L^3 + 5/2 b0 b1 L^2 - b2 L) a^4',
      sp.simplify(aQ - (a - b0 * L * a ** 2 + (b0 ** 2 * L ** 2 - b1 * L) * a ** 3 + (-b0 ** 3 * L ** 3 + sp.Rational(5, 2) * b0 * b1 * L ** 2 - b2 * L) * a ** 4)) == 0)
dfun = trunc(1 + d1 * aQ + d2 * aQ ** 2 + d3 * aQ ** 3 + d4 * aQ ** 4)
beta = -(b0 * a ** 2 + b1 * a ** 3 + b2 * a ** 4)
# mu^2 d/dmu^2 at fixed Q^2:  dL/d ln mu^2 = -1
check('G1b d(a(mu),L) is mu-independent through a^4: (-d/dL + beta(a) d/da) d = O(a^5)', trunc(-sp.diff(dfun, L) + beta * sp.diff(dfun, a)) == 0)
# G2: Pi in units R0/(12 pi^2): -dPi/dL = d  =>  Pi(L) = Pi(0) - int_0^L d
Pi = sp.expand(-sp.integrate(dfun, (L, 0, L)))
okG2 = True
for kk in range(0, N + 1):
    ck = sp.expand(Pi.coeff(a, kk))
    okG2 &= ck.is_polynomial(L) and sp.degree(ck, L) == max(1, kk)
check('G2  Pi_MS - Pi_MS(L=0) at order a^n is a polynomial in L of degree max(1,n) (n = 0..4)', okG2)
# G3: continuation vs contour formula
R_cont = sp.expand(sp.im(sp.expand(Pi.subs(L, ell - sp.I * sp.pi))) / sp.pi)      # R/R0 = 12pi Im Pi /R0, Pi in R0/(12pi^2)
R_contour = sp.expand(sp.integrate(sp.expand(dfun.subs(L, ell + sp.I * th)), (th, -sp.pi, sp.pi)) / (2 * sp.pi))
check('G3  R via L -> ln(s/mu^2) - i pi  ==  (1/2pi) int_{-pi}^{pi} dtheta D(s e^{i theta}) through a^4', sp.simplify(R_cont - R_contour) == 0)
Rs = sp.expand(R_cont.subs(ell, 0))
r = [sp.expand(Rs.coeff(a, kk)) for kk in range(N + 1)]
check('G4  r1 = d1, r2 = d2, r3 = d3 - (pi^2/3) b0^2 d1, r4 = d4 - pi^2 (b0^2 d2 + (5/6) b0 b1 d1)',
      sp.simplify(r[1] - d1) == 0 and sp.simplify(r[2] - d2) == 0 and sp.simplify(r[3] - (d3 - sp.pi ** 2 / 3 * b0 ** 2 * d1)) == 0
      and sp.simplify(r[4] - (d4 - sp.pi ** 2 * (b0 ** 2 * d2 + sp.Rational(5, 6) * b0 * b1 * d1))) == 0)
okG5 = all((sp.degree(sp.expand(R_cont.coeff(a, kk)), ell) if sp.expand(R_cont.coeff(a, kk)).has(ell) else 0) <= kk - 1 for kk in range(1, N + 1))
check('G5  R in a(mu): coefficient of a^n is a polynomial of degree <= n-1 in ln(s/mu^2)', okG5)
print('      R^(2) in a(mu):', sp.factor(sp.expand(R_cont.coeff(a, 2))))
print('      R^(3) in a(mu):', sp.collect(sp.expand(R_cont.coeff(a, 3)), ell))
# S1: the contour identity for a generic polynomial in L at fixed order (already covered by G3); show the sign:
# Pi(s+i0) - Pi(s-i0) with L = ln(s/mu^2) -/+ i pi:  = -int_{L=ell+i pi}^{ell-i pi} ... check on Pi = -L (LO): 2 i Im = 2 i pi
check('S1  LO check: Pi = 5/3 - L gives R/R0 = 1 (Im Pi(s+i0) = pi/(12 pi^2) R0)', sp.simplify(sp.im(sp.Rational(5, 3) - (ell - sp.I * sp.pi)) / sp.pi - 1) == 0)

# ------------------------------------------------------------------ numbers (SU(3))
z3, z5 = sp.zeta(3), sp.zeta(5)
CF, CA, TF = sp.Rational(4, 3), sp.Integer(3), sp.Rational(1, 2)
nf = sp.Symbol('n_f')
beta0 = sp.Rational(11, 3) * CA - sp.Rational(4, 3) * TF * nf
beta1 = sp.Rational(34, 3) * CA ** 2 - 4 * CF * TF * nf - sp.Rational(20, 3) * CA * TF * nf
pi2b0 = sp.pi ** 2 / 3 * (beta0 / 4) ** 2
vals = [float(pi2b0.subs(nf, n)) for n in (3, 4, 5)]
print('      (pi^2/3) b0^2 for n_f=3,4,5:', ['%.4f' % v for v in vals])
check('N1  (pi^2/3) b0^2 = 16.66, 14.28, 12.09 for n_f = 3,4,5', all(abs(v - t) < 0.006 for v, t in zip(vals, (16.655, 14.279, 12.086))))
# r2 general group (Baikov-Chetyrkin-Kuehn PRL 104 (2010) 132004, text before eq. (9): T_f = T n_f)
Tf = TF * nf
d2gen = -sp.Rational(3, 32) * CF ** 2 + CF * Tf * (z3 - sp.Rational(11, 8)) + CF * CA * (sp.Rational(123, 32) - sp.Rational(11, 4) * z3)
check('N2a general-group d2 (= r2) reduces to 365/24 - 11 zeta3 - n_f (11/12 - 2/3 zeta3) for SU(3)',
      sp.simplify(d2gen - (sp.Rational(365, 24) - 11 * z3 - nf * (sp.Rational(11, 12) - sp.Rational(2, 3) * z3))) == 0)
c0n, c1n = float(d2gen.subs(nf, 0)), float(sp.diff(d2gen, nf))
print('      r2 = %.4f %+.4f n_f' % (c0n, c1n))
check('N2b r2 = 1.9857 - 0.1153 n_f', abs(c0n - 1.9857) < 5e-5 and abs(c1n + 0.1153) < 5e-5)
# d3 general group (BCK 2010, display before eq. (9)); non-singlet
d3gen = (-sp.Rational(69, 128) * CF ** 3
         + CF ** 2 * Tf * (-sp.Rational(29, 64) + sp.Rational(19, 4) * z3 - 5 * z5)
         + CF * Tf ** 2 * (sp.Rational(151, 54) - sp.Rational(19, 9) * z3)
         + CF ** 2 * CA * (-sp.Rational(127, 64) - sp.Rational(143, 16) * z3 + sp.Rational(55, 4) * z5)
         + CF * Tf * CA * (-sp.Rational(485, 27) + sp.Rational(112, 9) * z3 + sp.Rational(5, 6) * z5)
         + CF * CA ** 2 * (sp.Rational(90445, 3456) - sp.Rational(2737, 144) * z3 - sp.Rational(55, 24) * z5))
d3p = sp.Poly(sp.expand(d3gen), nf)
print('      d3 (SU(3), non-singlet) = %.4f %+.4f n_f %+.5f n_f^2' % tuple(float(d3p.coeff_monomial(nf ** kk)) for kk in (0, 1, 2)))
d1v = sp.Rational(3, 4) * CF
r3ns = sp.expand(d3gen - sp.pi ** 2 / 3 * (beta0 / 4) ** 2 * d1v)
r3p = sp.Poly(r3ns, nf)
rc = tuple(float(r3p.coeff_monomial(nf ** kk)) for kk in (0, 1, 2))
print('      r3 (non-singlet) from d3 - (pi^2/3) b0^2 d1 = %.5f %+.5f n_f %+.5f n_f^2' % rc)
check('N3a r3(non-singlet) = -6.63694 - 1.20013 n_f - 0.00518 n_f^2 (GKL 1991 / SS 1991) reproduced from BCK d3 + pi^2 term',
      abs(rc[0] + 6.63694) < 5e-5 and abs(rc[1] + 1.20013) < 5e-5 and abs(rc[2] + 0.00518) < 5e-5)
sing = sp.Rational(55, 72) - sp.Rational(5, 3) * z3
check('N3b singlet coefficient 55/72 - (5/3) zeta3 = -1.2395', abs(float(sing) + 1.2395) < 5e-5)
# ex:ee-pi2 numbers
for n in (3, 4, 5):
    charges = [sp.Rational(2, 3), -sp.Rational(1, 3), -sp.Rational(1, 3), sp.Rational(2, 3), -sp.Rational(1, 3)][:n]
    eta = sum(charges) ** 2 / (3 * sum(q ** 2 for q in charges))
    print('      n_f=%d: r3_ns = %.3f, pi^2 term = -%.3f, d3_ns = %.3f, eta = %s, singlet = %.4f, r3_total = %.3f' % (
        n, float(r3ns.subs(nf, n)), float(pi2b0.subs(nf, n)), float(d3gen.subs(nf, n)), eta, float(eta * sing), float(r3ns.subs(nf, n) + eta * sing)))
check('N4  n_f = 5: r3 total = -12.805 (E29 printable value)', abs(float(r3ns.subs(nf, 5) + sp.Rational(1, 33) * sing) + 12.805) < 5e-4)
# d1 general group and R expansion check with a(s) at O(a)
check('N5  d1 = r1 = (3/4) C_F = 1 for SU(3)', d1v == 1)
print()
print('SUMMARY: %d/%d checks passed' % (sum(p for _, p in RES), len(RES)))
