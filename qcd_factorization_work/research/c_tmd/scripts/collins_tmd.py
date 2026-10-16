# One-loop Collins TMD of a quark in an on-shell massless quark, b-space, D=4-2eps.
# Inputs (derived in DERIVATION.md, checked in real_graphs.py / rapidity_checks.py / ft_check.py):
#   momentum space, kT != 0, after y_B -> -inf at fixed eps and combination with the soft factors
#   f^(1)(x,kT) = c_S/kT^2 { (1-eps)(1-x) + 2x[1/(1-x)]_+ + delta(1-x) ln(zeta/kT^2) },
#   c_S = g^2 mu^{2eps} C_F/(2pi)^{3-2eps};   virtual graphs = 0 (scaleless after the light-like limit)
# unsubtracted TMD and soft factor are also reported separately.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

eps, eta = sp.symbols('epsilon eta')
Lb, lz, Y, yB, yn = sp.symbols('L_b l_zeta Y y_B y_n', real=True)   # L_b=ln(mu^2 b^2/b0^2), l_zeta=ln(zeta/mu^2)
mu, b, zeta, alphas, CF = sp.symbols('mu b zeta alpha_s C_F', positive=True)
gE = sp.EulerGamma
b0 = 2 * sp.exp(-gE)
ORDER = 2   # keep terms through eps^1

def FTpow(e):
    """int d^{2-2eps}k e^{-ik.b} (k^2)^{-1-e}"""
    return sp.pi**(1 - eps) * 2**(-2 * eps - 2 * e) * sp.gamma(-eps - e) / sp.gamma(1 + e) * (b**2)**(e + eps)

# use Gamma(-eps) = -Gamma(1-eps)/eps and psi(-eps) = psi(1-eps) + 1/eps (sympy cannot expand at a pole)
FT_inv_k2 = -sp.pi**(1 - eps) * 2**(-2 * eps) * sp.gamma(1 - eps) / eps * (b**2)**eps
# d/d eta ln FTpow(eta) at eta=0 = -psi(-eps) - psi(1) - 2 ln 2 + ln b^2
dlog = -(sp.polygamma(0, 1 - eps) + 1 / eps) + gE - 2 * sp.log(2) + sp.log(b**2)
FT_lnk2_over_k2 = -FT_inv_k2 * dlog                           # FT[ln(k^2)/k^2] = -d/d eta FTpow
# cross-check of the closed forms against direct differentiation (numerically, eps=-0.3, b=0.7)
_chk = (-sp.diff(FTpow(eta), eta).subs(eta, 0) - FT_lnk2_over_k2).subs({eps: -0.3, b: 0.7})
assert abs(sp.N(_chk)) < 1e-12, _chk
assert abs(sp.N((FTpow(0) - FT_inv_k2).subs({eps: -0.3, b: 0.7}))) < 1e-12
cS = 4 * sp.pi * alphas * mu**(2 * eps) * CF / (2 * sp.pi)**(3 - 2 * eps)

schemes = {
    'binding (CONTEXT.md): S_eps=(4pi)^eps e^{-eps gE}': (4 * sp.pi)**eps * sp.exp(-eps * gE),
    'Collins 2011 Sec.3.3.2: S_eps=(4pi)^eps/Gamma(1-eps)': (4 * sp.pi)**eps / sp.gamma(1 - eps),
}

def laurent(expr, n=ORDER):
    expr = expr.subs({b: b0 * sp.exp(Lb / 2) / mu, zeta: mu**2 * sp.exp(lz)})
    expr = sp.expand_log(sp.expand_power_base(sp.powsimp(sp.expand(expr), force=True), force=True), force=True)
    s = sp.series(expr, eps, 0, n).removeO()
    return sp.expand(sp.simplify(sp.expand(s)))

results = {}
for name, Seps in schemes.items():
    norm = (alphas * CF / (2 * sp.pi)) * Seps          # common factor  (alpha_s C_F/2pi) S_eps
    A = laurent(cS * FT_inv_k2 / norm)                  # multiplies [p(x) - eps(1-x)], p(x)=(1+x^2)[1/(1-x)]_+
    Bd = laurent(cS * (sp.log(zeta) * FT_inv_k2 - FT_lnk2_over_k2) / norm)   # delta(1-x) coefficient
    Ae = laurent(cS * FT_inv_k2 / norm * (-eps))        # multiplies (1-x)
    results[name] = (A, Bd, Ae)
    print('=' * 100)
    print(name)
    print('  [1/kT^2]-transform  A(eps)      =', sp.collect(A, eps))
    print('  (1-x) coefficient   -eps*A      =', sp.collect(Ae, eps))
    print('  delta(1-x) coeff.   B(eps)      =', sp.collect(Bd, eps))
    # poles and finite parts (finite part = eps^0 coefficient)
    A_m1, A_0 = A.coeff(eps, -1), A.coeff(eps, 0)
    B_m2, B_m1, B_0 = Bd.coeff(eps, -2), Bd.coeff(eps, -1), Bd.coeff(eps, 0)
    Ae_0 = Ae.coeff(eps, 0)
    print('  poles: p(x)/eps coeff =', A_m1, '; delta: 1/eps^2 coeff =', B_m2, ', 1/eps coeff =', sp.simplify(B_m1))
    # IR poles must be those of the MSbar quark-in-quark PDF:  -(1/eps) [p(x) + 3/2 delta(1-x)]  (units alpha_s C_F/2pi)
    chk_x = sp.simplify(A_m1 - (-1)) == 0
    print('  CHECK x-dependent pole = -p(x)/eps (PDF collinear pole)       :', 'PASS' if chk_x else 'FAIL')
    # UV counterterm (delta(1-x) only):  U = -(total delta-poles) + IR delta-pole(-3/2/eps)
    U_m2 = -B_m2
    U_m1 = sp.simplify(-B_m1 - sp.Rational(3, 2))
    print('  UV counterterm  Z_F Z_2 - 1 = (alpha_s C_F/2pi) S_eps [ %s/eps^2 + (%s)/eps ]' % (U_m2, sp.simplify(U_m1)))
    # gamma_F = d ln Z/d ln mu, with d alpha_s/d ln mu = -2 eps alpha_s + O(alpha_s^2), explicit mu in l_zeta
    a = sp.Symbol('a')     # a = alpha_s C_F/(2 pi)
    lnZ = a * (U_m2 / eps**2 + U_m1 / eps)
    gF = sp.expand(sp.diff(lnZ, a) * (-2 * eps * a) + sp.diff(lnZ, lz) * (-2))
    print('  gamma_F = d lnZ/d ln mu = ', sp.simplify(gF), '  (a = alpha_s C_F/2pi)')
    print('  CHECK gamma_F finite and = (alpha_s C_F/pi)(3/2 - l_zeta)       :',
          'PASS' if sp.simplify(gF - 2 * a * (sp.Rational(3, 2) - lz)) == 0 else 'FAIL')
    # finite (renormalized, IR-subtracted) one-loop pieces => matching coefficient C~(1)
    fin_x = A_0      # times p(x)
    fin_1mx = Ae_0   # times (1-x)
    fin_d = sp.simplify(B_0)
    print('  C~(1)_{q/q} = (alpha_s C_F/2pi){ [%s] p(x) + [%s](1-x) + delta(1-x)[%s] }' % (sp.simplify(fin_x), fin_1mx, sp.expand(fin_d)))
    Kt = sp.expand(2 * sp.diff(fin_d, lz))   # d/d ln sqrt(zeta) = 2 d/d ln zeta
    print('  K~ = dln f/dln sqrt(zeta) = (alpha_s C_F/2pi) *', Kt, ' => K~ = -(alpha_s C_F/pi) L_b :',
          'PASS' if sp.simplify(Kt + 2 * Lb) == 0 else 'FAIL')
    print('  at mu=mu_b (L_b=0), zeta=mu_b^2 (l_zeta=0): delta(1-x) constant =', sp.nsimplify(fin_d.subs({Lb: 0, lz: 0})))
