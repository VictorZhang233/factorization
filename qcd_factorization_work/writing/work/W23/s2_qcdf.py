# -*- coding: utf-8 -*-
"""
s2_qcdf.py -- Ch20 sec:heavy-qcdf (QCD factorization for charmless B -> M1 M2).
 A. One-loop RG of (C1, C2) [BBNS 2001 operator basis]: d(C1 + C2/N)/dln mu = (as/4pi)(12 C_F/N) C2 and the
    analogous relation for a2; hence V_M must contain 12 ln(m_b/mu) for any N (VF-BQ-1); eigenvalues of gamma.
 B. Vertex kernel g(x) (BBNS 2001 eq. (47)): Gegenbauer integrals (eq. (48), VF-BQ-2) with mpmath; V' - V = 12
    for a symmetric DA; V_pi(mu = m_b) for the asymptotic DA; numerical a_{1,I}, a_{2,I} (illustration).
 C. Power counting of the two terms of the factorization formula; hard-spectator gluon virtuality.
 D. Twist-2 inverse moments <xbar^-1> = <x^-1> = 3 (asymptotic DA); twist-3 X_H divergence (VF-BQ-3).
 E. Annihilation building blocks A_1^i, A_3^f (BBNS 2001 eq. (62)) evaluated with the BN 2003 rules (eq. (56)):
    reproduce VF-BQ-5 (BBNS eq. (63), BN eq. (57)).
 F. ln(m_B/Lambda_h) = 2.36 (App Q item 7 / VF-BQ-4).
Run: python3 -I s2_qcdf.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w23common import *

ck = Check('s2_qcdf: RG origin of 12 ln(m_b/mu), g(x) integrals, power counting, endpoints, annihilation')

# ------------------------------------------------------------------------------------------- A
N, a = sp.symbols('N alpha_s', positive=True)
C1, C2 = sp.symbols('C1 C2')
CF = (N**2 - 1) / (2 * N)
gam = sp.Matrix([[-6 / N, 6], [6, -6 / N]])          # dC/dln mu = (as/4pi) gamma^T C
dC = (a / (4 * sp.pi)) * gam.T * sp.Matrix([C1, C2])
d_a1 = sp.simplify(dC[0] + dC[1] / N)
d_a2 = sp.simplify(dC[1] + dC[0] / N)
ck('d(C1 + C2/N)/dln mu = (as/4pi)(12 C_F/N) C2', sp.simplify(d_a1 - a / (4 * sp.pi) * 12 * CF / N * C2) == 0, d_a1)
ck('d(C2 + C1/N)/dln mu = (as/4pi)(12 C_F/N) C1', sp.simplify(d_a2 - a / (4 * sp.pi) * 12 * CF / N * C1) == 0, d_a2)
mu, mb = sp.symbols('mu m_b', positive=True)
term = (C2 / N) * (CF * a / (4 * sp.pi)) * 12 * sp.log(mb / mu)
ck('mu-derivative of (C2/N)(C_F as/4pi) 12 ln(m_b/mu) cancels it (any N)', sp.simplify(sp.diff(term, mu) * mu + d_a1) == 0)
ev = gam.eigenvects()
evals = sorted([sp.simplify(e[0]) for e in ev], key=lambda z: float(z.subs(N, 3)))
ck('eigenvalues gamma_pm = +-6(N-+1)/N for C_pm = C1 +- C2', set(evals) == {sp.simplify(6 * (N - 1) / N), sp.simplify(-6 * (N + 1) / N)}, evals)
C1n, C2n = 1.081, -0.190      # BBNS 2001 Table 1, NLO NDR, mu = m_b
ck('C_+ = 0.891 < 1 < C_- = 1.271 consistent with gamma_+ > 0 > gamma_-', abs(C1n + C2n - 0.891) < 1e-9 and abs(C1n - C2n - 1.271) < 1e-9)

# ------------------------------------------------------------------------------------------- B
mp.mp.dps = 30
def g(x):
    x = mp.mpf(x)
    xb = 1 - x
    t1 = 3 * ((1 - 2 * x) / (1 - x) * mp.log(x) - 1j * mp.pi)
    def br(y):
        yb = 1 - y
        return 2 * mp.polylog(2, y) - mp.log(y)**2 + 2 * mp.log(y) / (1 - y) - (3 + 2j * mp.pi) * mp.log(y)
    return t1 + br(x) - br(xb)
C1g = lambda u: 3 * u
C2g = lambda u: mp.mpf(3) / 2 * (5 * u**2 - 1)
phi = lambda x: 6 * x * (1 - x)
I0 = mp.quad(lambda x: g(x) * phi(x), [0, mp.mpf('0.5'), 1])
I1 = mp.quad(lambda x: g(x) * phi(x) * C1g(2 * x - 1), [0, mp.mpf('0.5'), 1])
I2 = mp.quad(lambda x: g(x) * phi(x) * C2g(2 * x - 1), [0, mp.mpf('0.5'), 1])
print('   int g Phi:', mp.nstr(I0, 18), ' alpha1 coeff:', mp.nstr(I1, 18), ' alpha2 coeff:', mp.nstr(I2, 18))
ck('int_0^1 g(x) 6x(1-x) = -1/2 - 3 i pi', abs(I0 - (-0.5 - 3j * mp.pi)) < 1e-20)
ck('alpha_1 coefficient = 11/2 - 3 i pi', abs(I1 - (mp.mpf(11) / 2 - 3j * mp.pi)) < 1e-20)
ck('alpha_2 coefficient = -21/20', abs(I2 - (-mp.mpf(21) / 20)) < 1e-20)
# g(1-x): odd Gegenbauer coefficients change sign
I1r = mp.quad(lambda x: g(1 - x) * phi(x) * C1g(2 * x - 1), [0, mp.mpf('0.5'), 1])
I0r = mp.quad(lambda x: g(1 - x) * phi(x), [0, mp.mpf('0.5'), 1])
ck('with g(1-x): alpha_1 coefficient changes sign, alpha_0 term unchanged', abs(I1r + I1) < 1e-20 and abs(I0r - I0) < 1e-20)
V = -18 + I0            # mu = m_b, asymptotic DA
Vp = -6 + I0r
ck('V_pi(mu = m_b, asymptotic DA) = -18.5 - 3 i pi;  V\' - V = 12 for a symmetric DA', abs(V - (-18.5 - 3j * mp.pi)) < 1e-20 and abs(Vp - V - 12) < 1e-20, mp.nstr(V, 10))
# two-loop running from alpha_s(M_Z) = 0.1180 (VF-QCD-7) to mu = 4.2 GeV, n_f = 5, our convention
nf = 5
b0 = mp.mpf(11) - mp.mpf(2) / 3 * nf
b1 = mp.mpf(102) - mp.mpf(38) / 3 * nf
def minus_beta(s, al):            # s = ln(M_Z^2/mu^2) >= 0 ; d al/ds = -mu^2 d al/d mu^2
    return b0 / (4 * mp.pi) * al**2 + b1 / (4 * mp.pi)**2 * al**3
MZ = mp.mpf('91.1876')
sol = mp.odefun(minus_beta, 0, mp.mpf('0.1180'))
as_mb = sol(mp.log(MZ**2 / mp.mpf('4.2')**2))
print('   alpha_s(4.2 GeV) [2-loop, n_f=5, from 0.1180] = %s' % mp.nstr(as_mb, 6))
ck('alpha_s(4.2 GeV) ~ 0.224 (two-loop running)', abs(as_mb - 0.2245) < 0.003)
Nc = 3; CFn = mp.mpf(4) / 3
fac = 1 + CFn * as_mb / (4 * mp.pi) * V
a1I = C1n + C2n / Nc * fac
a2I = C2n + C1n / Nc * fac
print('   a_{1,I} = %s ;  a_{2,I} = %s  (asymptotic DA, mu = m_b)' % (mp.nstr(a1I, 5), mp.nstr(a2I, 5)))
print('   arg a_{2,I} = %s deg' % mp.nstr(mp.degrees(mp.arg(a2I)), 4))
ck('a_{1,I} ~ 1.045 + 0.014 i, a_{2,I} ~ 0.014 - 0.081 i (illustration; BBNS Table 3 with Gegenbauer moments: 1.054 + 0.026 i, 0.005 - 0.084 i)',
   abs(a1I - (1.045 + 0.014j)) < 0.004 and abs(a2I - (0.014 - 0.081j)) < 0.006)

# ------------------------------------------------------------------------------------------- C
L, M = sp.symbols('Lambda m', positive=True)
F_Bpi = (L / M)**sp.Rational(3, 2); fB = L**sp.Rational(3, 2) * M**sp.Rational(-1, 2); fpi = L; lamB = L
termI = F_Bpi * M**2 * fpi
termII = fB * fpi * fpi * M / lamB
ck('form-factor term ~ hard-spectator term ~ Lambda^{5/2} m^{1/2}', sp.simplify(termI - L**sp.Rational(5, 2) * M**sp.Rational(1, 2)) == 0 and sp.simplify(termII - termI) == 0)
ck('prefactor f_B f_M1/(m_B lambda_B F(0)) = O(1)', sp.simplify(fB * fpi / (M * lamB * F_Bpi)) == 1)
# B -> D pi: spectator term G_F as f_pi f_D f_B (m_B/Lambda)... ~ m Lambda^2 vs leading m^2 Lambda (BBNS 2000)
fD = L**sp.Rational(3, 2) * M**sp.Rational(-1, 2)
spec = fpi * fD * fB * (M / L) * (M / L) * 1        # int Phi_B/xi ~ m/Lambda, int Phi_D/eta ~ m/Lambda (heavy meson)
lead = M**2 * 1 * fpi                                # F^{B->D} ~ 1
ck('B -> D pi: hard-spectator term / leading term = O(Lambda/m)', sp.simplify(spec / lead - L / M) == 0)
# spectator gluon virtuality: l = xi p_B (soft), enters M1 with fraction ybar of p1 (massless); k = l - ybar p1
xi_, yb, mB = sp.symbols('xi ybar m_B', positive=True)
pB4 = sp.Matrix([mB, 0, 0, 0]); p1 = sp.Matrix([mB / 2, 0, 0, -mB / 2])
gm = sp.diag(1, -1, -1, -1); d4 = lambda u, w: (u.T * gm * w)[0]
k = xi_ * pB4 - yb * p1
ck('hard-collinear gluon: k^2 = xi^2 m_B^2 - ybar xi m_B^2 ~ m_b Lambda', sp.simplify(d4(k, k) - (xi_**2 * mB**2 - yb * xi_ * mB**2)) == 0)
p2 = sp.Matrix([mB / 2, 0, 0, mB / 2]); x_ = sp.symbols('x', positive=True)
qprop = x_ * p2 + yb * p1        # quark propagator at the emission vertex (x p2 + ybar p1)
ck('quark propagator at the emission vertex: virtuality x ybar m_B^2 (hard)', sp.simplify(d4(qprop, qprop) - x_ * yb * mB**2) == 0)

# ------------------------------------------------------------------------------------------- D
y = sp.symbols('y', positive=True)
Phi = 6 * y * (1 - y)
ck('<ybar^-1> = <y^-1> = 3 for the asymptotic DA', sp.integrate(Phi / (1 - y), (y, 0, 1)) == 3 and sp.integrate(Phi / y, (y, 0, 1)) == 3)
dlt = sp.symbols('delta', positive=True)
XH = sp.integrate(1 / (1 - y), (y, 0, 1 - dlt))
ck('X_H = int dy/(1-y) Phi_p(y) with Phi_p = 1 diverges logarithmically: ln(1/delta)', sp.simplify(XH - sp.log(1 / dlt)) == 0)

# ------------------------------------------------------------------------------------------- E
# BN rules: int_0^1 dy/y -> X_A, int_0^1 dy ln y / y -> -X_A^2/2 ; similarly for M2 with y -> xbar.
XA, r1, r2 = sp.symbols('X_A r_1 r_2')
xx = sp.symbols('x', positive=True)
PhiX = 6 * xx * (1 - xx); PhiY = 6 * y * (1 - y)
# A_1^i / (pi as) = int dx dy { PhiX PhiY [ 1/(y(1 - x ybar)) + 1/(xbar^2 y) ] + r1 r2 2/(xbar y) }
t1num = mp.quad(lambda X, Y: 36 * X * (1 - X) * (1 - Y) / (1 - X * (1 - Y)), [0, 1], [0, 1])
ck('finite part 36 int int x xbar ybar/(1 - x ybar) = 18(pi^2/3 - 3) (numerical, 1e-20)', abs(t1num - 18 * (mp.pi**2 / 3 - 3)) < 1e-20, mp.nstr(t1num, 15))
t1 = 18 * (sp.pi**2 / 3 - 3)
# second term: int dy PhiY / y = 3 (finite) ; int dx PhiX / xbar^2 = 6 int x/xbar dx -> 6 (X_A - 1)
int_y = sp.integrate(PhiY / y, (y, 0, 1))
int_x = 6 * (XA - 1)               # BN rule: int x/(1-x) dx = int [1/(1-x) - 1] dx -> X_A - 1
t2 = int_y * int_x
t3 = r1 * r2 * 2 * XA * XA
A1i = sp.expand(t1 + t2 + t3)
ck('A_1^i = pi as [18 (X_A - 4 + pi^2/3) + 2 r1 r2 X_A^2]  (VF-BQ-5, BBNS (63))', sp.simplify(A1i - (18 * (XA - 4 + sp.pi**2 / 3) + 2 * r1 * r2 * XA**2)) == 0)
ck('BN normalization: 2 pi as [9(X_A - 4 + pi^2/3) + r1 r2 X_A^2] is the same', sp.simplify(A1i - 2 * (9 * (XA - 4 + sp.pi**2 / 3) + r1 * r2 * XA**2)) == 0)
# A_3^f / (pi as) = int dx dy { r1 PhiX 2(1+xbar)/(xbar^2 y) + r2 PhiY 2(1+y)/(xbar y^2) }
# first: int dx 6x xbar 2(1+xbar)/xbar^2 = 12 int x(2-x)/(1-x) = 12 int [1/(1-x) - (1-x)] -> 12 (X_A - 1/2) ; times int dy/y -> X_A
f1 = 12 * (XA - sp.Rational(1, 2)) * XA
chk1 = sp.simplify(sp.integrate(12 * (1 / (1 - xx) - (1 - xx)) - 6 * xx * 2 * (2 - xx) / (1 - xx), (xx, 0, 1)))
ck('decomposition x(2-x)/(1-x) = 1/(1-x) - (1-x) used for the BN rule', chk1 == 0)
f2 = 12 * (XA - sp.Rational(1, 2)) * XA       # symmetric (y <-> xbar)
chk2 = sp.simplify(sp.integrate(12 * (1 / y - y) - 6 * y * (1 - y) * 2 * (1 + y) / y**2, (y, 0, 1)))
ck('decomposition ybar(1+y)/y = 1/y - y for the second term', chk2 == 0)
A3f = sp.expand(r1 * f1 + r2 * f2)
ck('A_3^f = 6 pi as (r1 + r2)(2 X_A^2 - X_A)  -> 12 pi as r_chi (2X_A^2 - X_A) for r1 = r2 (VF-BQ-5)',
   sp.simplify(A3f - 6 * (r1 + r2) * (2 * XA**2 - XA)) == 0)

# ------------------------------------------------------------------------------------------- F
lnv = mp.log(mp.mpf('5.27966') / mp.mpf('0.5'))
ck('ln(m_B/Lambda_h) = 2.36 for m_B = 5.280 GeV, Lambda_h = 0.5 GeV (the default value "approx 2.4")', abs(lnv - 2.357) < 2e-3, mp.nstr(lnv, 5))

ok = ck.summary()
sys.exit(0 if ok else 1)
