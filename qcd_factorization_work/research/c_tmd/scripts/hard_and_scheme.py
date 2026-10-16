# DY hard factor, RG consistency with the TMD anomalous dimension, and MSbar-convention dependence.
# Input (derived independently in form_factor.py of this directory, Feynman parameters, exact in eps;
#        it also agrees with research/c_ee/ee_nlo.py, check B0):
#   F(s+i0) = 1 + (alpha_s C_F/4pi) (4pi mu^2)^eps (-s-i0)^-eps c_Gamma f(eps),
#   c_Gamma = G(1+e)G(1-e)^2/G(1-2e),  f(eps) = -(2 - eps + 2 eps^2)/(eps^2 (1-2 eps))
# TMD counterterm (collins_tmd.py): Z_F Z_2 - 1 = (alpha_s C_F/2pi) S_eps [-1/eps^2 + (l_zeta - 3/2)/eps]
# Factorization at O(alpha_s):  H^(1) = 2 Re F^(1) - 2 (Z-1)|_{zeta_A=zeta_B=Q^2}  (pure DR)
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

eps, L, Lb, lz = sp.symbols('epsilon L L_b l_zeta', real=True)   # L = ln(Q^2/mu^2)
gE = sp.EulerGamma
cG = sp.gamma(1 + eps) * sp.gamma(1 - eps)**2 / sp.gamma(1 - 2 * eps)
f = -(2 - eps + 2 * eps**2) / (eps**2 * (1 - 2 * eps))
ok = True
res = {}
for name, NormE in [('binding', sp.exp(gE * eps)), ('Collins', sp.gamma(1 - eps))]:
    # (4pi)^eps / S_eps = NormE ;  (mu^2/(-s-i0))^eps = exp(-eps L) exp(i pi eps)
    F1 = NormE * cG * sp.exp(-eps * L) * sp.exp(sp.I * sp.pi * eps) * f / 2   # in units alpha_s C_F/(2pi)
    ser = sp.series(F1, eps, 0, 1).removeO()
    ReF = sp.expand(sp.simplify(sp.re(sp.expand(ser.rewrite(sp.cos)))))
    ReF = sp.expand(sp.simplify(sp.expand_complex(ser)).as_real_imag()[0])
    twoRe = sp.expand(2 * ReF)
    Zm1 = -1 / eps**2 + (L - sp.Rational(3, 2)) / eps            # at l_zeta = ln(Q^2/mu^2) = L
    H1 = sp.expand(twoRe - 2 * Zm1)
    poles = [sp.simplify(H1.coeff(eps, -2)), sp.simplify(H1.coeff(eps, -1))]
    Hfin = sp.simplify(H1.coeff(eps, 0))
    res[name] = Hfin
    print('%-8s  H^(1) poles (must vanish): %s   H^(1) = (alpha_s C_F/2pi)[%s]' % (name, poles, sp.expand(Hfin)))
    ok &= poles == [0, 0]
    # RG: d ln H/d ln mu = (alpha_s C_F/2pi) dH1/dL * (-2) ; TMDs: gamma_F(A)+gamma_F(B) = (alpha_s C_F/pi)(3 - 2L)
    rg = sp.expand(sp.diff(Hfin, L) * (-2) + 2 * (3 - 2 * L))
    print('          RG: dlnH/dlnmu + gamma_F(zeta_A) + gamma_F(zeta_B), zeta_A zeta_B = Q^4  ->', rg)
    ok &= rg == 0
# convention dependence: H_bind - H_Collins and C~_bind - C~_Collins (collins_tmd.py: -pi^2/12 delta(1-x))
dH = sp.simplify(res['binding'] - res['Collins'])
print('H(binding) - H(Collins) =', dH, ' ; 2*[C~(binding)-C~(Collins)] =', -sp.pi**2 / 6, ' -> sum:', sp.simplify(dH - sp.pi**2 / 6))
ok &= sp.simplify(dH - sp.pi**2 / 6) == 0
# CSS coefficient with the hard factor absorbed symmetrically: C^CSS = C~(mu_b, mu_b^2) + H^(1)(L=0)/2
for name, cdelta in [('binding', -sp.pi**2 / 12), ('Collins', 0)]:
    c = sp.simplify(cdelta + res[name].subs(L, 0) / 2)
    print('%-8s  C_CSS^(1) delta(1-z) coefficient (units alpha_s C_F/2pi): %s' % (name, c))
    ok &= sp.simplify(c - (sp.pi**2 / 2 - 4)) == 0
print('=> C_qq^CSS(1) = (alpha_s/pi)[ C_F/2 (1-z) + C_F (pi^2/4 - 2) delta(1-z) ]; SU(3): (2/3)(1-z) + (pi^2-8)/3 delta(1-z)')
print('hard factor / scheme checks:', 'PASS' if ok else 'FAIL')
