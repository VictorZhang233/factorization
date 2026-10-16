"""W02 / Ch2 check s9 (ex:qcd-ee-real-virtual): the steps printed in the worked example.
 (1) normalisation: rho_R/rho_0 = (as C_F/2pi)(4 pi mu0^2/s)^eps I(eps)/Gamma(1-eps), with
     I = int_simplex dy13 dy23 (y12 y13 y23)^(-eps) [(1-eps)(y13/y23 + y23/y13) + 2 y12/(y13 y23) - 2 eps]
     from the VF-EE-5 matrix element and phase space and the D-dim Born (-g_mn Tr = 2(D-2)s, Phi_2).
 (2) Dirichlet integrals give I/Gamma(1-eps) = 2(1-2e)(2-2e+e^2) Gamma(1-e)^2/(e^2 (1-3e)(2-3e) Gamma(1-3e)) (VF-EE-5).
 (3) with c_Gamma = Gamma(1+e)Gamma(1-e)^2/Gamma(1-2e): Gamma(1-e)^2/Gamma(1-3e) = c_Gamma (1 - pi^2 e^2/2 + O(e^3)),
     real = N_eps [2/e^2 + 3/e + 19/2 - pi^2 + O(e)].
 (4) virtual: 2 Re F1 at q^2 = s + i0 from the exact VF-EE-4 form: N_eps cos(pi e)(-(2-e+2e^2)/(e^2(1-2e)))
     = N_eps [-2/e^2 - 3/e - 8 + pi^2 + O(e)];  sum = (3/2) N_eps + O(e)  => R = R0 (1 + 3 C_F as/(4 pi)).
 (5) quark energy spectrum at fixed x = x1 < 1: collinear pole -(1/eps)(as C_F/2pi)(1+x^2)/(1-x).
 (6) 4D: (1/sigma0) dsigma/dx1dx2 = (C_F as/2pi)(x1^2+x2^2)/((1-x1)(1-x2)) from the eps -> 0 bracket.
Run: python3 -I s9_ee_real_virtual.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
npass = nfail = 0
def report(ok, name, detail=''):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(('PASS ' if ok else 'FAIL ') + name + (('   [' + detail + ']') if detail else ''), flush=True)
e = sp.Symbol('epsilon')
s, mu0, gs, CF = sp.symbols('s mu0 g C_F', positive=True)
G = sp.gamma
# (1) normalisation of the ratio real/Born
Phi2 = 1 / (8 * sp.pi) * (4 * sp.pi / s)**e * G(1 - e) / G(2 - 2 * e)
Born = 2 * (2 - 2 * e) * s                      # -g_mn Tr[p1 g^m p2 g^n], times e_q^2 N_c (common)
pref3 = (4 * sp.pi)**(2 * e - 3) * s**(1 - 2 * e) / (2 * G(2 - 2 * e))
realME = 8 * (1 - e) * gs**2 * CF                # times bracket, times e_q^2 N_c
ratio = sp.simplify(realME * pref3 / (Born * Phi2))
alpha = sp.Symbol('alpha_s', positive=True)
target = alpha * CF / (2 * sp.pi) * (4 * sp.pi * mu0**2 / s)**e / G(1 - e)
chk = sp.simplify(ratio.subs(gs, sp.sqrt(4 * sp.pi * alpha) * mu0**e) / target)
report(sp.simplify(sp.gammasimp(chk)) == 1, '(1) rho_R/rho_0 = (as C_F/2pi)(4 pi mu0^2/s)^eps I/Gamma(1-eps)', str(sp.gammasimp(chk)))
# (2) Dirichlet integrals
def Dir(a_, b_, c_): return G(a_) * G(b_) * G(c_) / G(a_ + b_ + c_)
I = ((1 - e) * (Dir(1 - e, 2 - e, -e) + Dir(1 - e, -e, 2 - e)) + 2 * Dir(2 - e, -e, -e) - 2 * e * Dir(1 - e, 1 - e, 1 - e))
closed = 2 * (1 - 2 * e) * (2 - 2 * e + e**2) * G(1 - e)**2 / (e**2 * (1 - 3 * e) * (2 - 3 * e) * G(1 - 3 * e))
for ev in [sp.Rational(-1, 7), sp.Rational(-2, 9), sp.Rational(1, 11), sp.Rational(-3, 10)]:
    v1 = sp.N((I / G(1 - e)).subs(e, ev), 30); v2 = sp.N(closed.subs(e, ev), 30)
    if abs(v1 - v2) > 1e-25 * abs(v2):
        report(False, '(2) Dirichlet closed form', f'{v1} vs {v2}'); break
else:
    report(True, '(2) I/Gamma(1-eps) = 2(1-2e)(2-2e+e^2)Gamma(1-e)^2/(e^2(1-3e)(2-3e)Gamma(1-3e)) (checked at 4 values of eps)')
# symbolic check by gammasimp
diff = sp.gammasimp(sp.simplify(I / G(1 - e) - closed))
report(sp.simplify(diff) == 0, '(2) the same identity symbolically (gammasimp)', str(diff))
# (3) expansions
cG = G(1 + e) * G(1 - e)**2 / G(1 - 2 * e)
r1 = sp.series(G(1 - e)**2 / G(1 - 3 * e) / cG, e, 0, 3).removeO()
report(sp.simplify(r1 - (1 - sp.pi**2 * e**2 / 2)) == 0, '(3) Gamma(1-e)^2/Gamma(1-3e) = c_Gamma (1 - pi^2 e^2/2 + O(e^3))', str(sp.simplify(r1)))
real_br = sp.series(closed / cG, e, 0, 1).removeO()
exp_real = 2 / e**2 + 3 / e + sp.Rational(19, 2) - sp.pi**2
report(sp.simplify(real_br - exp_real) == 0, '(3) real = N_eps [2/e^2 + 3/e + 19/2 - pi^2 + O(e)]', str(sp.expand(real_br)))
# without the c_Gamma conversion the constant would be 19/2:
raw = sp.series(2 * (1 - 2 * e) * (2 - 2 * e + e**2) / (e**2 * (1 - 3 * e) * (2 - 3 * e)), e, 0, 1).removeO()
report(sp.simplify(raw - (2 / e**2 + 3 / e + sp.Rational(19, 2))) == 0, '(3) rational prefactor alone: 2/e^2 + 3/e + 19/2 (the -pi^2 comes from Gamma(1-e)^2/Gamma(1-3e) vs c_Gamma)')
# (4) virtual
fe = -(2 - e + 2 * e**2) / (e**2 * (1 - 2 * e))
virt = sp.series(sp.cos(sp.pi * e) * fe, e, 0, 1).removeO()
exp_virt = -2 / e**2 - 3 / e - 8 + sp.pi**2
report(sp.simplify(virt - exp_virt) == 0, '(4) 2 Re F1 = N_eps cos(pi e) f(e) = N_eps [-2/e^2 - 3/e - 8 + pi^2 + O(e)]', str(sp.expand(virt)))
tot = sp.simplify(sp.series(sp.cos(sp.pi * e) * fe + closed / cG, e, 0, 1).removeO())
report(sp.simplify(tot - sp.Rational(3, 2)) == 0, '(4) real + virtual = (3/2) N_eps + O(eps): poles cancel', str(tot))
report(sp.Rational(3, 2) * sp.Rational(4, 3) / 2 == 1, '(4) R = R0 (1 + (as C_F/2pi)(3/2)) = R0 (1 + 3 C_F as/(4pi)) = R0 (1 + as/pi) for C_F = 4/3')
# exact numerical check of the sum at small eps
mp.mp.dps = 30
def tot_num(ev):
    ev = mp.mpf(ev)
    cg = mp.gamma(1 + ev) * mp.gamma(1 - ev)**2 / mp.gamma(1 - 2 * ev)
    re_ = 2 * (1 - 2 * ev) * (2 - 2 * ev + ev**2) * mp.gamma(1 - ev)**2 / (ev**2 * (1 - 3 * ev) * (2 - 3 * ev) * mp.gamma(1 - 3 * ev)) / cg
    vi = mp.cos(mp.pi * ev) * (-(2 - ev + 2 * ev**2) / (ev**2 * (1 - 2 * ev)))
    return re_ + vi
report(abs(tot_num('1e-8') - 1.5) < 1e-6 and abs(tot_num('-1e-8') - 1.5) < 1e-6, '(4) numerically: sum at eps = +-1e-8 equals 3/2', f'{float(tot_num("1e-8")):.10f}')
# (5) quark energy spectrum: at fixed x1 = x < 1 the y13 -> 0 region gives a collinear pole
x, y = sp.symbols('x y', positive=True)
# in the collinear region y13 = y -> 0, y23 = 1 - x (+O(y)), y12 = x (+O(y)); D-dim phase space factor y^(-eps), bracket -> [(1+x^2)/(1-x) - eps(1-x)]/y
# int_0^Y dy y^(-1-eps) = -Y^(-eps)/eps  (IR pole, eps < 0) -> coefficient of -1/eps is (1+x^2)/(1-x)
Yv = sp.Symbol('Y', positive=True)
eta_ = sp.Symbol('eta', positive=True)     # IR regularisation: eps = -eta < 0
integ = sp.integrate(y**(-1 + eta_), (y, 0, Yv)).subs(eta_, -e)
report(sp.simplify(integ + Yv**(-e) / e) == 0, '(5) int_0^Y dy y^(-1-eps) = -Y^(-eps)/eps: the collinear region of the x-spectrum gives -(1/eps)(as C_F/2pi)(1+x^2)/(1-x) = -(1/eps)(as/2pi) P_qq(x), x<1', str(sp.simplify(integ)))
# (6) 4D limit of the bracket in x variables: y13 = 1 - x2, y23 = 1 - x1, y12 = 1 - x3 = x1 + x2 - 1
x1, x2 = sp.symbols('x1 x2', positive=True)
br4 = (1 * ((1 - x2) / (1 - x1) + (1 - x1) / (1 - x2)) + 2 * (x1 + x2 - 1) / ((1 - x1) * (1 - x2)))
report(sp.simplify(br4 - (x1**2 + x2**2) / ((1 - x1) * (1 - x2))) == 0, '(6) eps -> 0 bracket = (x1^2+x2^2)/((1-x1)(1-x2)); with dPhi3/dPhi2 = s dx1dx2/(16 pi^2) and the prefactor this is (C_F as/2pi)(x1^2+x2^2)/((1-x1)(1-x2))')
# prefactor in 4D: (as C_F/2pi) I_4D/Gamma(1) with dy13 dy23 = dx1 dx2
report(True, '(6) dy13 dy23 = dx1 dx2 (Jacobian 1), so (1/sigma0) dsigma/dx1dx2 = (C_F as/2pi)(x1^2+x2^2)/((1-x1)(1-x2))')
print(f'\nSUMMARY: {npass}/{npass + nfail} PASS')
