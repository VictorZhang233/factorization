# Independent one-loop massless quark form factor (Feynman gauge, D = 4-2eps) and the
# TMD hard factors H_DY (time-like q^2 = Q^2) and H_SIDIS (space-like q^2 = -Q^2) in two
# MSbar conventions.  Binding conventions of CONTEXT.md (vertex i g gamma^mu t^a).
#
#   Lambda^mu = -i g^2 C_F mu^{2eps} int d^Dl/(2pi)^D
#               gamma^a (p1slash + lslash) gamma^mu (lslash - p2slash) gamma_a / [l^2 (p1+l)^2 (l-p2)^2]
#   (outgoing quark p1, outgoing antiquark p2, q = p1 + p2), F^(1) = Tr[p1 Lambda^mu p2 gamma_mu]/Tr[p1 gamma^mu p2 gamma_mu]
#
# Feynman parameters x (gluon), y (quark p1), z (antiquark p2):  l = l' - y p1 + z p2,  Delta = -y z q^2 - i0.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
from dirac import Dots, trace, contract, D

eps = sp.Symbol('epsilon')
y, z, s12 = sp.symbols('y z s12', positive=True)      # s12 = p1.p2 = q^2/2

# ---- Dirac traces -------------------------------------------------------------------
# slots:  Tr[ p1  e1  A  e2  B  f1  p2  f2 ],  (e1,f1) = gamma^a...gamma_a, (e2,f2) = gamma^mu...gamma_mu
# A = l + p1 = l' + (1-y) p1 + z p2 ,  B = l - p2 = l' - y p1 - (1-z) p2
tab = {('p1', 'p1'): 0, ('p2', 'p2'): 0, ('p1', 'p2'): s12}
dot = Dots(tab)
vecs = ['p1', 'p2']

def tr_pair(a, b):
    """Tr[p1 e1 a e2 b f1 p2 f2] fully contracted (a, b are vector names, or 'e3'/'f3' placeholders)"""
    t = trace(['p1', 'e1', a, 'e2', b, 'f1', 'p2', 'f2'], dot)
    extra = [v for v in (a, b) if v in ('e3', 'f3')]
    t = contract(t, 'e1', 'f1', vecs + ['e2', 'f2'] + extra)
    t = contract(t, 'e2', 'f2', vecs + extra)
    if extra:
        t = contract(t, 'e3', 'f3', vecs)
    rep = {sp.Symbol('dot_p1_p1'): 0, sp.Symbol('dot_p2_p2'): 0, sp.Symbol('dot_p1_p2'): s12}
    return sp.expand(t.subs(rep))

cA = {'p1': 1 - y, 'p2': z}
cB = {'p1': -y, 'p2': -(1 - z)}
T0 = sp.expand(sum(cA[a] * cB[b] * tr_pair(a, b) for a in cA for b in cB))       # l'-independent part
Tll = tr_pair('e3', 'f3')                                                           # l'^r l'^s -> (l'^2/D) g_rs
den = sp.expand(4 * (2 - D) * s12)                                                  # Tr[p1 gamma^mu p2 gamma_mu]
print('T0  =', sp.factor(T0))
print('Tll =', sp.factor(Tll))

# ---- loop integrals ------------------------------------------------------------------
#  int d^Dl/(2pi)^D 1/(l^2-Delta)^3       = -i/(4pi)^{D/2} Gamma(1+eps)/(2 Delta^{1+eps})
#  int d^Dl/(2pi)^D l^2/(l^2-Delta)^3     = +i/(4pi)^{D/2} (D/2) Gamma(eps)/(2 Delta^{eps})
#  => F^(1) = (alpha_s C_F/4pi) (4 pi mu^2)^eps * 2/den * int dy dz [ Tll/D (D/2) G(eps)/(2 Delta^eps) - T0 G(1+eps)/(2 Delta^{1+eps}) ]
#  with Delta = y z (-q^2) = 2 y z (-s12):   write (-q^2)^{-eps} outside, i.e. Delta^{-a} = (yz)^{-a} (-q^2)^{-a}
q2m = sp.Symbol('Qm2', positive=True)        # (-q^2) treated as positive (space-like); continue later

def dirichlet(a, b, c):
    """int_{y,z>0, y+z<1} y^a z^b (1-y-z)^c = G(a+1)G(b+1)G(c+1)/G(a+b+c+3)"""
    return sp.gamma(a + 1) * sp.gamma(b + 1) * sp.gamma(c + 1) / sp.gamma(a + b + c + 3)

def integrate_monomials(expr, power):
    """int dy dz expr(y,z) (y z)^power over the simplex (x = 1-y-z integrated out)"""
    expr = sp.Poly(sp.expand(expr), y, z)
    res = 0
    for (i, j), c in expr.terms():
        res += c * dirichlet(i + power, j + power, 0)
    return res

Dsub = 4 - 2 * eps
# Tll term: (Tll/D)(D/2) Gamma(eps)/(2 Delta^eps) = Tll Gamma(eps) /(4 Delta^eps)
I_ll = sp.gamma(eps) / 4 * integrate_monomials(Tll.subs(D, Dsub), -eps) * q2m**(-eps)
I_0 = -sp.gamma(1 + eps) / 2 * integrate_monomials(T0.subs(D, Dsub), -1 - eps) * q2m**(-1 - eps)
# q^2 = 2 s12 -> -q^2 = Qm2 means s12 = -Qm2/2 (space-like)
F1 = (2 / den.subs(D, Dsub)) * (I_ll + I_0)
F1 = F1.subs(s12, -q2m / 2)
# normalise: F1 = (alpha_s C_F/4pi) (4 pi mu^2/(-q^2))^eps * c_Gamma * f(eps)
cG = sp.gamma(1 + eps) * sp.gamma(1 - eps)**2 / sp.gamma(1 - 2 * eps)
f_calc_raw = sp.powsimp(sp.expand(F1 * q2m**eps / cG), force=True)   # contains Gamma functions of eps
f_expected = -(2 - eps + 2 * eps**2) / (eps**2 * (1 - 2 * eps))
# exact identity check: the ratio is a meromorphic function of eps; compare at 6 generic points to 40 digits
ok = True
for ev in [sp.Rational(1, 7), sp.Rational(-2, 9), sp.Rational(3, 11), sp.Rational(-5, 13), sp.Rational(1, 3) + sp.I / 5, sp.Rational(-1, 10) - sp.I / 7]:
    v1 = sp.N(f_calc_raw.subs({eps: ev, q2m: sp.Rational(7, 3)}), 40)
    v2 = sp.N(f_expected.subs(eps, ev), 40)
    good = abs(v1 - v2) < sp.Float('1e-30')
    ok &= bool(good)
    print('   eps=%-14s computed f = %s   expected = %s   %s' % (ev, sp.N(v1, 18), sp.N(v2, 18), 'ok' if good else 'MISMATCH'))
print('CHECK q^2-independence of F1*(-q^2)^eps and exact form f(eps) = -(2-eps+2eps^2)/(eps^2(1-2eps)) :', 'PASS' if ok else 'FAIL')
print('   Laurent: f =', sp.series(f_expected, eps, 0, 1))
f_calc = f_expected     # identical as verified above (used below for the hard factors)

# ---- hard factors -----------------------------------------------------------------------
# F^(1) in units alpha_s C_F/(2 pi):  F1/2 = (1/2)(4pi)^eps/S_eps-ratio ... ; (mu^2/(-q^2-i0))^eps
L = sp.Symbol('L', real=True)            # L = ln(Q^2/mu^2)
er = sp.Symbol('epsilon_r', real=True)   # real epsilon for taking real parts
f_calc = f_calc.subs(eps, er); cG = cG.subs(eps, er); eps = er
a = sp.Symbol('a')                       # a = alpha_s C_F/(2 pi)
results = {}
for scheme, normE in [('binding  S_eps=(4pi)^eps e^{-eps gE}', sp.exp(sp.EulerGamma * eps)),
                      ('Collins  S_eps=(4pi)^eps/Gamma(1-eps)', sp.gamma(1 - eps))]:
    for proc, phase in [('DY   (q^2=+Q^2, ln(-q^2-i0)=ln Q^2 - i pi)', sp.exp(sp.I * sp.pi * eps)),
                        ('SIDIS(q^2=-Q^2)', sp.Integer(1))]:
        # Collins bookkeeping: g0^2 = 4 pi alpha_s mu^{2eps}, counterterms S_eps x poles.  Then
        # F^(1) = (alpha_s C_F/4pi)(4 pi mu^2/(-q^2-i0))^eps cG f = a S_eps * [ (4pi)^eps/S_eps * (mu^2/(-q^2-i0))^eps cG f/2 ]
        Fhalf = normE * cG * f_calc * sp.exp(-eps * L) * phase / 2          # units a, times S_eps stripped
        ser = sp.series(Fhalf, eps, 0, 1).removeO()
        ReF = sp.expand(sp.re(sp.expand_complex(sp.expand(ser))))
        twoRe = sp.expand(2 * ReF)
        Zm1 = -1 / eps**2 + (L - sp.Rational(3, 2)) / eps     # TMD counterterm at ln(zeta/mu^2) = L (zeta_A zeta_B = Q^4)
        H1 = sp.expand(twoRe - 2 * Zm1)
        poles = [sp.simplify(H1.coeff(eps, -2)), sp.simplify(H1.coeff(eps, -1))]
        Hfin = sp.nsimplify(sp.simplify(H1.coeff(eps, 0)))
        rg = sp.expand(sp.diff(Hfin, L) * (-2) + 2 * (3 - 2 * L))     # d ln H/d ln mu + gamma_F(zA)+gamma_F(zB) (units a)
        results[(scheme[:7].strip(), proc[:5].strip())] = Hfin
        print('%s | %s : poles %s ; H^(1) = a*[%s] ; RG residual %s' % (scheme, proc, poles, sp.expand(Hfin), rg))
        ok &= poles == [0, 0] and rg == 0

lit = {('binding', 'DY'): -L**2 + 3 * L - 8 + 7 * sp.pi**2 / 6,     # EIS 2012 Sec.7 (standard MSbar), a = alpha_s C_F/2pi
       ('Collins', 'DY'): -L**2 + 3 * L - 8 + sp.pi**2,             # Aybat-Rogers arXiv:1107.3973 (C_F alpha_s/pi)[3L/2-L^2/2-4+pi^2/2]
       ('Collins', 'SIDIS'): -L**2 + 3 * L - 8,                      # Aybat-Rogers arXiv:1107.3973 (C_F alpha_s/pi)[3L/2-L^2/2-4]
       ('binding', 'SIDIS'): -L**2 + 3 * L - 8 + sp.pi**2 / 6}      # implied by scheme shift (no direct source checked)
for k, v in lit.items():
    good = sp.simplify(results[k] - v) == 0
    ok &= good
    print('literature/expected %-18s: %-28s %s' % (str(k), str(v), 'PASS' if good else 'FAIL'))
dDY = sp.simplify(results[('binding', 'DY')] - results[('Collins', 'DY')])
dSI = sp.simplify(results[('binding', 'SIDIS')] - results[('Collins', 'SIDIS')])
print('H(binding)-H(Collins): DY', dDY, ' SIDIS', dSI, ' (both = pi^2/6 = -2 x [Ctilde shift -pi^2/12])')
ratio = sp.simplify((results[('binding', 'DY')] - results[('binding', 'DY')].subs(sp.pi, 0)) /
                    (results[('Collins', 'DY')] - results[('Collins', 'DY')].subs(sp.pi, 0)))
print('ratio of pi^2 terms in H_DY (binding/Collins) =', ratio, '(Collins-Rogers 2013, Sec. "Different versions of MSbar": factor 7/6)')
ok &= dDY == sp.pi**2 / 6 and dSI == sp.pi**2 / 6 and ratio == sp.Rational(7, 6)
print('form factor / hard factor checks:', 'PASS' if ok else 'FAIL')
