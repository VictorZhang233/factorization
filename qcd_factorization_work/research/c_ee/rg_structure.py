"""
rg_structure.py -- RG + analyticity structure of the massless vector correlator to all orders (here: through a^4).

Conventions: a = alpha_s(mu)/pi ;  mu^2 da/dmu^2 = -b0 a^2 - b1 a^3 - b2 a^4 - ...,  b0 = beta_0/4, b1 = beta_1/16, ...
(CONTEXT.md: mu^2 d alpha_s/dmu^2 = -(beta_0/4pi) alpha_s^2 + ...).
Pi^{mu nu} = (q^mu q^nu - q^2 g^{mu nu}) Pi,  L = ln(Q^2/mu^2) = ln(-q^2/mu^2).
Inhomogeneous RG (additive renormalisation of Pi; conserved current => no anomalous dimension):
     mu^2 dPi/dmu^2 = gamma(a)  (q-independent)  <=>  Adler function D(Q^2) := -12 pi^2 Q^2 dPi/dQ^2 is RG invariant,
     D = R_0 d(a(Q^2)),  d(a) = 1 + d1 a + d2 a^2 + d3 a^3 + d4 a^4 + ... .
Claims checked:
  G1  at each order a^n the renormalised Pi is a polynomial in L (degree max(1,n)), with finite coefficients;
  G2  R(s) = 12 pi Im Pi(s+i0) obtained by L -> ln(s/mu^2) - i pi equals the contour formula
      R(s) = (1/2pi) Int_{-pi}^{pi} dtheta D(s e^{i theta})   (both derived in DERIVATION.md);
  G3  in terms of a(s):  r1 = d1, r2 = d2, r3 = d3 - (pi^2/3) b0^2 d1, r4 = d4 - pi^2 (b0^2 d2 + (5/6) b0 b1 d1);
  G4  R expressed in a(mu) is a polynomial of degree n-1 in ln(s/mu^2) at order a^n.
Run: python3 -I rg_structure.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

a, L, ell, th = sp.symbols('a L ell theta', real=True)
b0, b1, b2, b3 = sp.symbols('b0 b1 b2 b3', real=True)
d1, d2, d3, d4 = sp.symbols('d1 d2 d3 d4', real=True)
N = 4
PASS = []


def check(name, cond):
    PASS.append((name, bool(cond)))
    print(('PASS  ' if cond else 'FAIL  ') + name)


def trunc(ex, n=N):
    ex = sp.expand(ex)
    return sum(ex.coeff(a, k) * a ** k for k in range(0, n + 1))


# running coupling a(Q^2) as a series in a = a(mu) and L, from da/dL = -b0 a^2 - b1 a^3 - b2 a^4
# ansatz a_Q = sum_k c_k(L) a^k, solve order by order
c = [sp.Integer(0), sp.Integer(1)]
aQ = a
for k in range(2, N + 1):
    ck = sp.Function('c%d' % k)(L)
    trial = aQ + ck * a ** k
    lhs = sp.diff(trial, L)
    rhs = -(b0 * trial ** 2 + b1 * trial ** 3 + b2 * trial ** 4)
    eq = sp.expand(lhs - rhs).coeff(a, k)
    sol = sp.dsolve(sp.Eq(eq, 0), ck, ics={ck.subs(L, 0): 0})
    aQ = sp.expand(aQ + sol.rhs * a ** k)
print('a(Q^2) =', sp.collect(aQ, a))
Dfun = trunc(1 + d1 * aQ + d2 * aQ ** 2 + d3 * aQ ** 3 + d4 * aQ ** 4)        # units R_0
# check RG invariance of D: dD/dln mu^2 = 0  <=>  -dD/dL + beta(a) dD/da = 0  (L = ln Q^2 - ln mu^2)
beta = -(b0 * a ** 2 + b1 * a ** 3 + b2 * a ** 4)
check('G0  D(a(mu), L) is mu-independent through a^4  (-dD/dL + beta(a) dD/da = O(a^5))',
      trunc(-sp.diff(Dfun, L) + beta * sp.diff(Dfun, a)) == 0)
# Pi (units R_0/(12 pi^2)):  -dPi/dL = D  =>  Pi(L) = Pi(0) - Int_0^L D
P0 = sp.Function('P0')(a)
Pi = sp.expand(-sp.integrate(Dfun, (L, 0, L)))
okpoly = True
for k in range(0, N + 1):
    ck = sp.expand(Pi.coeff(a, k))
    deg = sp.degree(ck, L) if ck != 0 else -1
    okpoly &= ck.is_polynomial(L) and deg == max(1, k)
check('G1  renormalised Pi at order a^n is a polynomial in L of degree max(1,n)  (n = 0..4)', okpoly)
# R from analytic continuation: L -> ell - i pi  (ell = ln(s/mu^2)); R/R_0 = 12 pi Im Pi /(R_0/(12 pi^2)) ... :
# R = 12 pi Im[Pi] with Pi in units R_0/(12 pi^2)  =>  R/R_0 = Im[Pi_units]/pi
R_cont = sp.expand(sp.im(sp.expand(Pi.subs(L, ell - sp.I * sp.pi))) / sp.pi)
# contour formula: R = (1/2pi) Int_{-pi}^{pi} D(s e^{i theta}) dtheta ;  L = ln(Q^2/mu^2) = ell + i theta
R_contour = sp.expand(sp.integrate(sp.expand(Dfun.subs(L, ell + sp.I * th)), (th, -sp.pi, sp.pi)) / (2 * sp.pi))
check('G2  R via L -> ln(s/mu^2) - i pi  ==  contour formula (1/2pi) Int dtheta D(s e^{i theta})',
      sp.simplify(R_cont - R_contour) == 0)
# coefficients in terms of a(s): set ell = 0 (mu^2 = s)
Rs = sp.expand(R_cont.subs(ell, 0))
r = [sp.expand(Rs.coeff(a, k)) for k in range(N + 1)]
print('r1 =', r[1]); print('r2 =', r[2]); print('r3 =', r[3]); print('r4 =', r[4])
check('G3  r1=d1, r2=d2, r3=d3-(pi^2/3) b0^2 d1, r4=d4-pi^2(b0^2 d2+(5/6) b0 b1 d1)',
      sp.simplify(r[1] - d1) == 0 and sp.simplify(r[2] - d2) == 0
      and sp.simplify(r[3] - (d3 - sp.pi ** 2 / 3 * b0 ** 2 * d1)) == 0
      and sp.simplify(r[4] - (d4 - sp.pi ** 2 * (b0 ** 2 * d2 + sp.Rational(5, 6) * b0 * b1 * d1))) == 0)
okdeg = all((sp.degree(sp.expand(R_cont.coeff(a, k)), ell) if sp.expand(R_cont.coeff(a, k)).has(ell) else 0) <= k - 1
            for k in range(1, N + 1))
check('G4  R in terms of a(mu): coefficient of a^n is a polynomial of degree <= n-1 in ln(s/mu^2)', okdeg)
# numerical illustration (SU(3)): size of the pi^2 term in r3 for nf = 3,4,5
for nf in (3, 4, 5):
    beta0 = sp.Rational(11) - sp.Rational(2, 3) * nf
    print('   nf=%d: (pi^2/3) b0^2 = %.4f' % (nf, float(sp.pi ** 2 / 3 * (beta0 / 4) ** 2)))
print()
print('SUMMARY: %d/%d checks passed' % (sum(p for _, p in PASS), len(PASS)))
