# CSS resummation for Drell-Yan: (i) Fourier identities b -> qT, (ii) O(alpha_s) dictionary between the
# Collins-2011 TMD form  W~ = H(Q;mu) f~_A(x_A,b;Q^2,mu) f~_B(x_B,b;Q^2,mu) |_{mu=Q}
# and the CSS form       W~ = exp{-int_{mu_b^2}^{Q^2} dmu^2/mu^2 [A ln(Q^2/mu^2) + B]} (C(x)f)(x_A;mu_b) (C(x)f)(x_B;mu_b),
# (iii) the qT-space O(alpha_s) asymptotics used by dy_qt_check.py.  Conventions: CONTEXT.md; a = alpha_s C_F/(2pi).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
mp.mp.dps = 25
ok = True

# ---- (i) Bessel moments that make b0 = 2 e^{-gE} the natural constant -----------------------------
#   int_0^inf deta J_1(eta) ln^m(eta/b0) = 1, 0, 0  (m = 0, 1, 2)   [also quoted by Balazs-Yuan 1997, eq. (IntBess)]
#   exact: int_0^inf J_1(eta) eta^s deta = 2^s Gamma(1+s/2)/Gamma(1-s/2)  => d/ds|_0 = ln2 - gE = ln b0, d^2/ds^2|_0 = ln^2 b0
b0 = 2 * mp.e**(-mp.euler)
for m in (0, 1, 2):
    val = mp.quadosc(lambda t: mp.besselj(1, t) * mp.log(t / b0)**m, [0, mp.inf], zeros=lambda n: mp.besseljzero(1, n))
    target = 1 if m == 0 else 0
    print('(i) int J1(eta) ln^%d(eta/b0) = %s   (expected %d)' % (m, mp.nstr(val, 15), target))
    ok &= abs(val - target) < mp.mpf('1e-7')      # oscillatory, conditionally convergent tail: ~1e-8 attainable
s = sp.Symbol('s')
g = 2**s * sp.gamma(1 + s / 2) / sp.gamma(1 - s / 2)
d1, d2 = sp.simplify(sp.diff(g, s).subs(s, 0)), sp.simplify(sp.diff(g, s, 2).subs(s, 0))
print('    analytic: d/ds = %s, d^2/ds^2 = %s  ; ln b0 = %s' % (d1, sp.expand(d2), sp.log(2) - sp.EulerGamma))
ok &= sp.simplify(d1 - (sp.log(2) - sp.EulerGamma)) == 0 and sp.expand(sp.simplify(d2) - (sp.log(2) - sp.EulerGamma)**2) == 0

# ---- Fourier transforms of the b-space logarithms (qT != 0) ---------------------------------------
#   int d^2b/(2pi)^2 e^{i q.b} (Q^2 b^2/b0^2)^eta = -(eta/(pi q^2)) (Q^2/q^2)^eta e^{2 gE eta} Gamma(1+eta)/Gamma(1-eta)  (exact;
#   e^{2gE eta}G(1+eta)/G(1-eta) = 1 - (2 zeta3/3) eta^3 + ..., so FT[L^m] for m <= 3 are free of transcendental constants)
eta, Q2, q2 = sp.symbols('eta Q2 q2', positive=True)
gen = -(eta / (sp.pi * q2)) * (Q2 / q2)**eta * sp.exp(2 * sp.EulerGamma * eta) * sp.gamma(1 + eta) / sp.gamma(1 - eta)
ser = sp.series(gen, eta, 0, 4).removeO()
FT = {m: sp.simplify(sp.factorial(m) * ser.coeff(eta, m)) for m in (1, 2, 3)}
lq = sp.log(Q2 / q2)
print('(i) FT[L]   =', sp.simplify(FT[1]), ';  FT[L^2] =', sp.factor(sp.expand(FT[2])), ';  FT[L^3] =', sp.expand(FT[3]))
ok &= sp.simplify(FT[1] + 1 / (sp.pi * q2)) == 0 and sp.simplify(FT[2] + 2 * lq / (sp.pi * q2)) == 0
# check the generating function against the d=2 Fourier formula pi 2^{2-2a} Gamma(1-a)/Gamma(a) (q^2)^{a-1}, a = -eta
a_ = -eta
formula = sp.pi * 2**(2 - 2 * a_) * sp.gamma(1 - a_) / sp.gamma(a_) * q2**(a_ - 1) / (2 * sp.pi)**2 * (Q2 * sp.exp(2 * sp.EulerGamma) / 4)**eta
print('    generating function == d=2 FT formula:', sp.simplify(sp.gammasimp(formula / gen)) == 1)
ok &= sp.simplify(sp.gammasimp(formula / gen)) == 1

# ---- (ii) O(alpha_s) dictionary ------------------------------------------------------------------
L = sp.Symbol('L', real=True)              # L = ln(Q^2/mu_b^2) = ln(Q^2 b^2/b0^2)
A1, B1 = sp.symbols('A1 B1')               # CSS coefficients in units alpha_s/pi
CF, TF = sp.Rational(4, 3), sp.Rational(1, 2)
# TMD form at mu = Q, zeta = Q^2, with each TMD evolved from (mu_b, zeta=mu_b^2) [K~(b;mu_b) = 0 at one loop]:
#   ln f~(Q,Q^2) - ln f~(mu_b,mu_b^2) = ln(Q/mu_b) K~(mu_b) + int_{mu_b}^{Q} dmu/mu [gamma_F(mu;1) - ln(Q/mu) gamma_K]
mu_ = sp.Symbol('m')                        # integration variable t = ln(mu/mu_b) in [0, L/2]
t = sp.Symbol('t')
gF1 = sp.Rational(3, 2) * CF               # gamma_F(1) in units alpha_s/pi
gK1 = 2 * CF                               # gamma_K in units alpha_s/pi
evo_one = sp.integrate(gF1 - (L / 2 - t) * gK1, (t, 0, L / 2))       # fixed coupling at this order
css_exp = -(A1 * L**2 / 2 + B1 * L)                                   # -int dmu^2/mu^2 [A ln(Q^2/mu^2)+B], units alpha_s/pi
sol = sp.solve(sp.Poly(sp.expand(2 * evo_one - css_exp), L).coeffs(), [A1, B1], dict=True)[0]
print('(ii) A^(1) = %s (= gamma_K^(1)/2 = C_F),  B^(1) = %s (= -gamma_F^(1)(1) = -3C_F/2)   [units alpha_s/pi]' % (sol[A1], sol[B1]))
ok &= sol[A1] == CF and sol[B1] == -sp.Rational(3, 2) * CF
# C functions: C^CSS_{qq}(z) = C~_{q/q}(z; mu_b, mu_b^2) + (1/2) H^(1)(Q;mu=Q) delta(1-z);  C^CSS_{qg} = C~_{q/g}(mu_b)
for scheme, Cdelta, H0 in [('binding', -sp.pi**2 / 12, -8 + 7 * sp.pi**2 / 6), ('Collins', 0, -8 + sp.pi**2)]:
    c_delta = sp.simplify(Cdelta + H0 / 2)                         # units a
    print('     [%s] C~ delta-term %s a, H^(1)(L=0) = %s a  =>  C^CSS delta-term = %s a = %s (alpha_s/pi) (SU(3))' % (
        scheme, Cdelta, H0, c_delta, sp.nsimplify(c_delta * CF / 2)))
    ok &= sp.simplify(c_delta - (sp.pi**2 / 2 - 4)) == 0
print('     C^CSS(1)_qq(z) = (alpha_s/pi)[ C_F/2 (1-z) + C_F(pi^2/4 - 2) delta(1-z) ] = (alpha_s/pi)[ (2/3)(1-z) + (pi^2-8)/3 delta(1-z) ]')
print('     C^CSS(1)_qg(z) = (alpha_s/pi) T_F z(1-z) = (alpha_s/pi) z(1-z)/2')
print('     literature: Balazs-Yuan, PRD 56 (1997) 5558, App. "A, B and C functions" (canonical C1=b0, C2=1, citing CSS and Davies-Stirling):')
print('       A^(1)=C_F, B^(1)=-3C_F/2, C^(1)_jk = delta_jk{(2/3)(1-z) + (1/3)delta(1-z)(pi^2-8)}, C^(1)_jG = z(1-z)/2  -> PASS')
ok &= sp.simplify(CF * (sp.pi**2 / 4 - 2) - (sp.pi**2 - 8) / 3) == 0 and sp.simplify(CF / 2 - sp.Rational(2, 3)) == 0

# ---- (iii) qT-space O(alpha_s) asymptotics -----------------------------------------------------------
#   W~(1) = (alpha_s/pi){ -(A1 L^2/2 + B1 L) f f } - (alpha_s/2pi) L [ (P(x)f) f + f (P(x)f) ]  + L-independent (-> delta^2(qT))
#   int d^2b/(2pi)^2 e^{iq.b} W~(1) = (alpha_s/(2 pi^2 qT^2)) { 2[A1 ln(Q^2/qT^2) + B1] f f + (P(x)f) f + f (P(x)f) }
ff, Pf = sp.symbols('ff Pf')               # f_A f_B and [(P(x)f_A) f_B + f_A (P(x)f_B)] (P in the alpha_s/2pi normalisation)
Wt = -(A1 * L**2 / 2 + B1 * L) * ff - sp.Rational(1, 2) * L * Pf      # units alpha_s/pi
Wq = sp.expand(-(A1 / 2) * FT[2] * ff - B1 * FT[1] * ff - sp.Rational(1, 2) * FT[1] * Pf)
target = (1 / (2 * sp.pi * q2)) * (2 * (A1 * lq + B1) * ff + Pf)      # times alpha_s/pi
print('(iii) FT of W~(1) (units alpha_s/pi):', sp.simplify(Wq - target) == 0, '; i.e. dsigma/dQ^2 dy dqT^2 = sigma0 (alpha_s/2pi)(1/qT^2){2[A1 ln + B1] qqbar + P(x)q qbar + q P(x)qbar}')
ok &= sp.simplify(Wq - target) == 0
print('CSS expansion checks:', 'PASS' if ok else 'FAIL')
