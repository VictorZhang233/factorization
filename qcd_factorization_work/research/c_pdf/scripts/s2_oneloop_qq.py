"""
s2_oneloop_qq.py -- item (2): one-loop quark-in-quark PDF from the operator definition, Feynman gauge.

Target: on-shell massless quark p = (p^+, 0, 0_T).  IR regulator: gluon mass m (UV: DR, D = 4 - 2 eps).
Graphs (cut-diagram language, Wilson line W[w,0] = W[w,inf n] W[inf n,0], n^mu = delta^mu_-, n.v = v^+):
  R1  real gluon, attached to the quark line on both sides of the cut           (ladder)
  R2  real gluon, quark line on one side, Wilson line on the other  (+ h.c.)     (interference)
  R3  real gluon, Wilson line on both sides  ~ n^2 = 0
  V1  virtual gluon between the Wilson line and the incoming quark (+ h.c.)
  V2  quark self-energy on the external legs (LSZ residue)
  V3  Wilson-line self-energy ~ n^2 = 0
Amplitude for one real gluon (colour a, momentum l, polarisation eps*):
  <l| W[inf,0] psi(0) |p>  = -g t^a eps*_mu [ kslash gamma^mu / k^2 + n^mu/(n.l) ] u(p),   k = p - l
Normalisation: f(xi) = sum_X (1/2) delta(xi P^+ - (P-p_X)^+) <P|[psibar W](0)|X> gamma^+ <X|[W psi](0)|P>
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
import mpmath as mp
from lorentz_engine import Vec, Kin, Term, trace, tr_sum, mul, V, I, D, contract

results = []


def report(name, ok, detail=''):
    results.append((name, bool(ok)))
    print('%-78s %s %s' % (name, 'PASS' if ok else 'FAIL', detail))


xi, pp, LT2, m, eps = sp.symbols('xi p^+ L_T2 m epsilon', positive=True)
x = sp.Symbol('x', positive=True)

# ---------------------------------------------------------------- kinematics
kin = Kin({('p', 'p'): 0, ('n', 'n'): 0, ('p', 'n'): pp, ('p', 'lT'): 0, ('n', 'lT'): 0, ('lT', 'lT'): -LT2})
P, N, LT = Vec.b('p'), Vec.b('n'), Vec.b('lT')
lminus = (LT2 + m ** 2) / (2 * (1 - xi) * pp)
L = P * (1 - xi) + N * lminus + LT          # real gluon, l^2 = m^2
K = P - L                                   # parton entering the operator
dot = kin.dot
report('l^2 = m^2 (on-shell massive gluon)', sp.simplify(dot(L, L) - m ** 2) == 0)
k2 = sp.simplify(dot(K, K))
report('k^2 = -(L_T^2 + xi m^2)/(1-xi)', sp.simplify(k2 + (LT2 + xi * m ** 2) / (1 - xi)) == 0)
report('n.k = xi p^+,  n.l = (1-xi) p^+', sp.simplify(dot(N, K) - xi * pp) == 0 and sp.simplify(dot(N, L) - (1 - xi) * pp) == 0)
nl = dot(N, L)

# amplitude pieces Gamma^mu (acting on u(p)) and conjugate Gammabar^nu (ubar(p) ... )
def Gam(lab, kk=K, k2_=k2, nl_=nl):
    return [Term(1 / k2_, [('v', kk), I(lab)]), Term(1 / nl_, [], [(V('n'), I(lab))])]


def Gambar(lab, kk=K, k2_=k2, nl_=nl):
    return [Term(1 / k2_, [I(lab), ('v', kk)]), Term(1 / nl_, [], [(V('n'), I(lab))])]


pslash = [Term(sp.Rational(1, 2), [V('p')])]   # (1/2) sum_s u ubar = pslash/2
nslash = [Term(1, [V('n')])]                     # operator vertex gamma^+ = nslash

# Ward identity: l_mu Gamma^mu u(p) = 0  ->  Tr[pslash/2 Gbar^nu nslash (l.Gamma)] = 0
lGam = [Term(1 / k2, [('v', K), ('v', L)]), Term(dot(N, L) / nl, [])]
# contract the conjugate index with l as well (full l.l term of a massive polarisation sum)
lGambar = [Term(1 / k2, [('v', L), ('v', K)]), Term(dot(N, L) / nl, [])]
ward = sp.simplify(tr_sum(mul(pslash, lGambar, nslash, lGam), kin))
report('Ward identity: l_mu l_nu M^mu Mbar^nu = 0 (eikonal term cancels longitudinal part)', ward == 0)
# stronger: (kslash lslash/k^2 + 1) pslash = 0 as a matrix, tested against a basis of Dirac structures
kin2 = Kin({('p', 'p'): 0, ('n', 'n'): 0, ('p', 'n'): pp, ('p', 'lT'): 0, ('n', 'lT'): 0, ('lT', 'lT'): -LT2,
            ('a', 'a'): sp.Symbol('aa'), ('a', 'p'): sp.Symbol('ap'), ('a', 'n'): sp.Symbol('an'), ('a', 'lT'): sp.Symbol('al'),
            ('b', 'b'): sp.Symbol('bb'), ('b', 'p'): sp.Symbol('bp'), ('b', 'n'): sp.Symbol('bn'), ('b', 'lT'): sp.Symbol('bl'),
            ('a', 'b'): sp.Symbol('ab')})
okw = True
for Y in ([], [V('a')], [V('a'), V('b')]):
    expr = tr_sum(mul(lGam, [Term(1, [V('p')])], [Term(1, list(Y))]), kin2)
    okw &= sp.simplify(expr) == 0
report('Ward identity as a matrix: (kslash lslash/k^2 + 1) pslash = 0', okw)

# ---------------------------------------------------------------- R1+R2(+R3): Feynman gauge, -g sum
S_F = sp.simplify(-tr_sum(mul(pslash, Gambar('a'), nslash, Gam('a')), kin))      # -g_{mu nu}
epsD = sp.Symbol('epsilon')
S_F_eps = sp.simplify(S_F.subs(D, 4 - 2 * epsD))
S_hand = pp * (4 * (1 - epsD) * LT2 * (1 - xi) ** 2 / (LT2 + xi * m ** 2) ** 2 + 8 * xi / (LT2 + xi * m ** 2))
report('Feynman-gauge |M|^2 / (g^2 C_F) = p^+[4(1-eps)L(1-xi)^2/(L+xi m^2)^2 + 8xi/(L+xi m^2)]',
       sp.simplify(S_F_eps - S_hand) == 0)
# individual pieces
S_R1 = sp.simplify(-tr_sum(mul(pslash, [Gambar('a')[0]], nslash, [Gam('a')[0]]), kin).subs(D, 4 - 2 * epsD))
S_R2 = sp.simplify(-tr_sum(mul(pslash, [Gambar('a')[0]], nslash, [Gam('a')[1]]), kin)
                   - tr_sum(mul(pslash, [Gambar('a')[1]], nslash, [Gam('a')[0]]), kin))
S_R3 = sp.simplify(-tr_sum(mul(pslash, [Gambar('a')[1]], nslash, [Gam('a')[1]]), kin))
report('R3 (Wilson-Wilson) = 0 since n^2 = 0', S_R3 == 0)
report('R2 (interference, both orderings) = 8 xi p^+/(lT^2 + xi m^2) = -8 xi p^+/((1-xi) k^2)',
       sp.simplify(S_R2 - 8 * xi * pp / (LT2 + xi * m ** 2)) == 0 and sp.simplify(S_R2 + 8 * xi * pp / ((1 - xi) * k2)) == 0,
       'S_R2=%s' % sp.simplify(S_R2))
report('R1 (ladder) = 4(1-eps) p^+ lT^2 (1-xi)^2/(lT^2+xi m^2)^2',
       sp.simplify(S_R1 - 4 * (1 - epsD) * pp * LT2 * (1 - xi) ** 2 / (LT2 + xi * m ** 2) ** 2) == 0)
# massive vector polarisation sum  -g + l l/m^2  gives the same
S_P = sp.simplify(S_F + tr_sum(mul(pslash, lGambar, nslash, lGam), kin) / m ** 2)
report('massive polarisation sum (-g + l l/m^2) = Feynman -g result', sp.simplify(S_P - S_F) == 0)

# phase space: f_R = (1/2) int d^{D-2}l_T /((2pi)^{D-1} 2 (1-xi) p^+) * g^2 C_F * S
F_int = sp.simplify(S_F_eps / (4 * (1 - xi) * pp))           # integrand of (g^2 C_F/(2pi)^{D-1}) int d^{D-2}l_T
F_hand = (1 - epsD) * (1 - xi) * LT2 / (LT2 + xi * m ** 2) ** 2 + 2 * xi / ((1 - xi) * (LT2 + xi * m ** 2))
report('f_R integrand = (1-eps)(1-xi)L/(L+xi m^2)^2 + 2xi/((1-xi)(L+xi m^2))', sp.simplify(F_int - F_hand) == 0)

# ---------------------------------------------------------------- massless limit: D-dim kernel; light-cone gauge
F0 = sp.simplify(F_int.subs(m, 0) * LT2)
Phat_qq = (1 + xi ** 2) / (1 - xi) - epsD * (1 - xi)
report('massless Feynman gauge: L_T^2 x integrand = (1+xi^2)/(1-xi) - eps(1-xi)', sp.simplify(F0 - Phat_qq) == 0)
# light-cone gauge (A^+ = 0): only R1 with d^{mu nu}(l) = -g + (l^mu n^nu + n^mu l^nu)/n.l, massless gluon
kin0 = kin
L0 = P * (1 - xi) + N * (LT2 / (2 * (1 - xi) * pp)) + LT
K0 = P - L0
k20 = sp.simplify(dot(K0, K0))
nl0 = dot(N, L0)
amp = [Term(1 / k20, [('v', K0), I('mu')])]
cnj = [Term(1 / k20, [I('nu'), ('v', K0)])]
dmunu = [Term(-1, [], [(I('mu'), I('nu'))]),
         Term(1 / nl0, [], [(('v', L0), I('mu')), (V('n'), I('nu'))]),
         Term(1 / nl0, [], [(V('n'), I('mu')), (('v', L0), I('nu'))])]
S_LC = sp.simplify(tr_sum(mul(pslash, cnj, nslash, amp, dmunu), kin0).subs(D, 4 - 2 * epsD))
F_LC = sp.simplify(S_LC / (4 * (1 - xi) * pp) * LT2)
report('light-cone gauge ladder alone gives the same D-dim kernel', sp.simplify(F_LC - Phat_qq) == 0)

# ---------------------------------------------------------------- transverse integrals
def Tint(a, b, M2, d):
    """int d^d l (l^2)^a/(l^2+M^2)^b  (Euclidean)."""
    return sp.pi ** (d / 2) * sp.gamma(a + d / 2) * sp.gamma(b - a - d / 2) / (sp.gamma(d / 2) * sp.gamma(b)) * M2 ** (a + d / 2 - b)


# numeric check of the master formula at non-integer d
okT = True
for (a, b, d_, M2_) in [(0, 1, 1.4, 0.7), (1, 2, 1.3, 2.0), (0, 2, 2.6, 1.1), (-sp.Rational(1, 2), 1, 2.2, 0.5)]:
    exact = complex(Tint(sp.nsimplify(a), b, M2_, d_).evalf())
    radial = 2 * mp.pi ** (d_ / 2) / mp.gamma(d_ / 2) * mp.quad(lambda r: r ** (d_ - 1) * r ** (2 * float(a)) / (r ** 2 + M2_) ** b, [0, 1, mp.inf])
    okT &= abs(exact - complex(radial)) < 1e-10 * abs(exact)
report('master formula int d^d l (l^2)^a/(l^2+M^2)^b checked numerically (non-integer d)', okT)

d = 2 - 2 * epsD
M2 = xi * m ** 2
I_R = sp.simplify((1 - epsD) * (1 - xi) * Tint(1, 2, M2, d) + 2 * xi / (1 - xi) * Tint(0, 1, M2, d))
pref = sp.Symbol('C')   # C = g^2 C_F/(2pi)^{D-1}
# coupling: g0^2 = 4 pi alpha_s mu^{2eps} e^{eps gamma_E} (4pi)^{-eps}   (MSbar, S_eps = (4pi)^eps e^{-eps gamma_E})
als, mu, CF = sp.symbols('alpha_s mu C_F', positive=True)
g02 = 4 * sp.pi * als * mu ** (2 * epsD) * sp.exp(epsD * sp.EulerGamma) * (4 * sp.pi) ** (-epsD)
pref_val = g02 * CF / (2 * sp.pi) ** (3 - 2 * epsD)
check_pref = sp.simplify(sp.powsimp(sp.expand_power_base(pref_val * sp.pi ** (1 - epsD) / (als / (2 * sp.pi) * CF * mu ** (2 * epsD) * sp.exp(epsD * sp.EulerGamma)), force=True), force=True))
report('g0^2/(2pi)^{3-2eps} * pi^{1-eps} = (alpha_s/2pi) mu^{2eps} e^{eps gamma_E}', sp.simplify(check_pref - 1) == 0, str(check_pref))
A_eps = als / (2 * sp.pi) * CF * sp.exp(epsD * sp.EulerGamma) * sp.gamma(epsD) * (mu ** 2 / m ** 2) ** epsD
fR_closed = A_eps * (xi ** (-epsD) * (1 - epsD) ** 2 * (1 - xi) + 2 * xi ** (1 - epsD) / (1 - xi))
fR_from_int = als / (2 * sp.pi) * CF * mu ** (2 * epsD) * sp.exp(epsD * sp.EulerGamma) / sp.pi ** (1 - epsD) * I_R
report('f_R = A_eps [xi^{-eps}(1-eps)^2(1-xi) + 2 xi^{1-eps}/(1-xi)],  A_eps=(as/2pi)C_F e^{eps gE} G(eps)(mu^2/m^2)^eps',
       sp.simplify(sp.powsimp(sp.expand_power_base((fR_from_int / fR_closed), force=True), force=True) - 1) == 0)

# ---------------------------------------------------------------- V1: virtual Wilson-line vertex
# Dirac factor ubar g^+ (pslash - lslash) g^+ u / ubar g^+ u = 2 (p-l)^+
Lv = Vec.b('lv')
kinv = Kin({('p', 'p'): 0, ('n', 'n'): 0, ('p', 'n'): pp, ('p', 'lv'): sp.Symbol('pl'), ('n', 'lv'): sp.Symbol('lplus'),
            ('lv', 'lv'): sp.Symbol('ll')})
num = tr_sum(mul(pslash, nslash, [Term(1, [('v', P - Lv)])], nslash), kinv)
den = tr_sum(mul(pslash, nslash), kinv)
report('Dirac factor of V1: ubar g^+ (p-l)slash g^+ u = 2(p^+ - l^+) ubar g^+ u', sp.simplify(num / den - 2 * (pp - sp.Symbol('lplus'))) == 0)

# l^- contour integral:  int dl^- 1/[(2 l^+ l^- - lT^2 - m^2 + i0)(-2(p^+-l^+) l^- - lT^2 + i0)]
#   = pi i /(p^+ (lT^2 + x m^2)) for l^+ = (1-x) p^+, 0<x<1, and 0 otherwise.
def lminus_int(xx, lt2, mm2, ppv=1.3, eta=1e-7):
    lp = (1 - xx) * ppv
    f = lambda lm: 1 / ((2 * lp * lm - lt2 - mm2 + 1j * eta) * (-2 * (ppv - lp) * lm - lt2 + 1j * eta))
    # integrate along a contour slightly deformed? use direct real-axis quad with breakpoints at the poles
    poles = sorted([(lt2 + mm2) / (2 * lp) if lp != 0 else 0.0, -lt2 / (2 * (ppv - lp)) if ppv != lp else 0.0])
    return mp.quad(f, [-mp.inf, poles[0] - 1, poles[0], poles[0] + 1e-3, poles[1], poles[1] + 1, mp.inf], maxdegree=10)


mp.mp.dps = 20
okC = True
details = []
for (xx, lt2, mm2) in [(0.3, 0.8, 0.5), (0.75, 2.0, 0.3), (0.5, 0.1, 1.0)]:
    num_val = complex(lminus_int(xx, lt2, mm2, eta=1e-9))
    ex = complex(mp.pi * 1j / (1.3 * (lt2 + xx * mm2)))
    details.append('%.2e' % (abs(num_val - ex) / abs(ex)))
    okC &= abs(num_val - ex) < 1e-4 * abs(ex)
for (xx, lt2, mm2) in [(1.4, 0.8, 0.5), (-0.3, 1.0, 0.4)]:   # l^+ < 0 or l^+ > p^+ : both poles on one side
    num_val = complex(lminus_int(xx, lt2, mm2, eta=1e-9))
    details.append('%.1e' % abs(num_val))
    okC &= abs(num_val) < 1e-5
report('l^- contour integral = pi i/(p^+(lT^2+x m^2)) on 0<x<1, zero outside (numerical)', okC, ','.join(details))
# assemble V1: delta_V = -i g^2 C_F int d^Dl/(2pi)^D 2(p^+-l^+)/[(-l^+ + i0)(l^2-m^2)((p-l)^2)]
#            = -(g^2 C_F)/(2 (2pi)^{D-1}) int_0^1 dx int d^{D-2}lT 2x/((1-x)(lT^2+x m^2))
lp_ = (1 - x) * pp
deltaV_integrand = (-sp.I) * (2 * (pp - lp_)) / (-lp_) * (sp.pi * sp.I / (pp * (LT2 + x * m ** 2))) * pp / (2 * sp.pi) ** 4   # (dl^+ = p^+ dx), per d^{D-2}lT
deltaV_integrand = sp.simplify(deltaV_integrand * (2 * sp.pi) ** 4)   # strip (2pi)^D -> compare structure with (2pi)^{D-1}
target = -sp.Rational(1, 2) * 2 * x / ((1 - x) * (LT2 + x * m ** 2)) * 2 * sp.pi   # -(1/2)/(2pi)^{D-1} => *2pi relative to (2pi)^D
report('V1 integrand: delta_V = -(g^2C_F/(2(2pi)^{D-1})) int dx d^{D-2}lT 2x/((1-x)(lT^2+x m^2))',
       sp.simplify(deltaV_integrand - target) == 0)
# 2 Re delta_V (V1 + h.c.) = - (same x-integrand as the real interference R2 at xi -> x):
R2_part = 2 * xi / ((1 - xi) * (LT2 + xi * m ** 2))
V1_part = 2 * (-sp.Rational(1, 2)) * 2 * x / ((1 - x) * (LT2 + x * m ** 2))
report('R2(xi) and 2Re V1 combine into a plus distribution [2xi/((1-xi)(lT^2+xi m^2))]_+',
       sp.simplify(R2_part.subs(xi, x) + V1_part) == 0)

# ---------------------------------------------------------------- V2: self-energy, on-shell residue
# -i Sigma = (ig)^2 C_F int gamma^mu i(pslash-lslash) gamma_mu (-i)/(((p-l)^2)(l^2-m^2))
# Dirac: gamma^mu a gamma_mu = (2-D) a  (engine)
kinS = Kin({('a', 'a'): sp.Symbol('aa'), ('a', 'b'): sp.Symbol('ab'), ('b', 'b'): sp.Symbol('bb')})
lhs = trace([I('m'), V('a'), I('m'), V('b')], [], kinS)
report('gamma^mu aslash gamma_mu = (2-D) aslash', sp.simplify(lhs - (2 - D) * 4 * sp.Symbol('ab')) == 0)
y = sp.Symbol('y', positive=True)
# Sigma = pslash Sigma_V,  Sigma_V(p^2) = (2-D) g^2 C_F/(4pi)^{D/2} Gamma(eps) int_0^1 dy (1-y) [(1-y)(m^2 - y p^2)]^{-eps}
SigmaV0 = (2 - (4 - 2 * epsD)) * g02 * CF / (4 * sp.pi) ** (2 - epsD) * sp.gamma(epsD) * sp.integrate((1 - y) ** (1 - epsD), (y, 0, 1), conds='none') * (m ** 2) ** (-epsD)
SigmaV0_closed = -A_eps * (1 - epsD) / (2 - epsD)
report('on-shell residue: dZ_2 = Sigma_V(0) = -A_eps (1-eps)/(2-eps)',
       sp.simplify(sp.powsimp(sp.expand_power_base(SigmaV0 / SigmaV0_closed, force=True), force=True) - 1) == 0)
pole_Z2 = sp.limit(epsD * SigmaV0_closed, epsD, 0)
report('UV pole of Z_2 (Feynman gauge) = -(alpha_s/4pi) C_F / eps', sp.simplify(pole_Z2 + als * CF / (4 * sp.pi)) == 0)

# ---------------------------------------------------------------- assembly as distributions (test functions)
# <f_bare^(1), h> = A_eps { int_0^1 [xi^{-eps}(1-eps)^2(1-xi) h + 2 xi^{1-eps}/(1-xi) (h - h(1))] - (1-eps)/(2-eps) h(1) }
def pair_bare(hfun, order=1):
    """Laurent expansion in eps of <f_bare^(1), h> / ((alpha_s/2pi) C_F)."""
    h1 = hfun.subs(xi, 1)
    reg = sp.integrate(sp.series(xi ** (-epsD) * (1 - epsD) ** 2 * (1 - xi) * hfun, epsD, 0, order + 1).removeO(), (xi, 0, 1))
    plus = sp.integrate(sp.series(2 * xi ** (1 - epsD) * sp.cancel((hfun - h1) / (1 - xi)), epsD, 0, order + 1).removeO(), (xi, 0, 1))
    tot = reg + plus - (1 - epsD) / (2 - epsD) * h1
    pre = sp.exp(epsD * sp.EulerGamma) * sp.gamma(epsD) * (mu ** 2 / m ** 2) ** epsD
    return sp.series(pre * tot, epsD, 0, order).removeO()


def pair_Pqq(hfun):
    """<P_qq, h>/C_F with P_qq = C_F[(1+z^2)/(1-z)_+ + 3/2 delta(1-z)]."""
    h1 = hfun.subs(xi, 1)
    return sp.integrate(sp.cancel(((1 + xi ** 2) * hfun - 2 * h1) / (1 - xi)), (xi, 0, 1)) + sp.Rational(3, 2) * h1


Lmu = sp.log(mu ** 2 / m ** 2)
okUV = True
for hfun in [sp.Integer(1), xi, xi ** 2, xi ** 5, (1 - xi) ** 3, xi ** 3 * (1 + xi)]:
    ser = sp.expand(pair_bare(hfun))
    pole = ser.coeff(epsD, -1)
    okUV &= sp.simplify(pole - pair_Pqq(hfun)) == 0
report('UV pole of bare f^(1): (alpha_s/2pi)(1/eps) P_qq, P_qq = C_F[(1+z^2)/(1-z)]_+  (6 test fns)', okUV)
# exact-in-eps quark number: <f_bare^(1), 1> = 0
reg1 = sp.integrate(xi ** (-epsD) * (1 - epsD) ** 2 * (1 - xi), (xi, 0, 1), conds='none')
report('exact quark number of bare f^(1): int_0^1 f^(1) = 0 for all eps', sp.simplify(reg1 - (1 - epsD) / (2 - epsD)) == 0)

# renormalised (MSbar):  f_ren = Z (x) f_bare, Z = delta - (alpha_s/2pi)(1/eps) P_qq
def pair_ren_finite(hfun):
    ser = sp.expand(pair_bare(hfun))
    return sp.simplify(ser.coeff(epsD, 0))   # pole removed by the counterterm


def pair_ren_formula(hfun):
    """claimed finite result /( (alpha_s/2pi) C_F ):
       P_qq/C_F ln(mu^2/m^2) - (1-xi)(2+ln xi) - [2 xi ln xi/(1-xi)]_+ + (1/4) delta(1-xi)"""
    h1 = hfun.subs(xi, 1)
    t1 = pair_Pqq(hfun) * Lmu
    t2 = sp.integrate(-(1 - xi) * (2 + sp.log(xi)) * hfun, (xi, 0, 1))
    t3 = -sp.integrate(2 * xi * sp.log(xi) / (1 - xi) * (hfun - h1), (xi, 0, 1))
    return t1 + t2 + t3 + sp.Rational(1, 4) * h1


okF = True
for hfun in [sp.Integer(1), xi, xi ** 2, xi ** 4 + 2 * xi]:
    okF &= sp.simplify(pair_ren_finite(hfun) - pair_ren_formula(hfun)) == 0
report('MSbar finite part: P ln(mu^2/m^2) + C_F[-(1-xi)(2+ln xi) - [2xi ln xi/(1-xi)]_+ + delta/4]', okF)
report('quark number of renormalised f: int_0^1 f_ren^(1) = 0', sp.simplify(pair_ren_finite(sp.Integer(1))) == 0)

# ---------------------------------------------------------------- pure DR: scaleless, UV/IR split
M2s = sp.Symbol('M2', positive=True)
# int d^d l [1/l^2 - 1/(l^2+M^2)] = M^2 int d^d l 1/(l^2 (l^2+M^2))  (IR divergent, UV convergent; needs eps<0)
IR_piece = sp.simplify(M2s * Tint(-1, 1, M2s, d))
UV_piece = Tint(0, 1, M2s, d)
report('pure DR: int d^{2-2eps} lT/lT^2 = pi^{1-eps}G(1+eps)M^{-2eps}(1/eps_UV - 1/eps_IR) = 0',
       sp.simplify(sp.gammasimp(IR_piece + UV_piece)) == 0,
       'IR=%s' % sp.simplify(sp.gammasimp(IR_piece)))

# ---------------------------------------------------------------- off-shell target (cross-check of the UV pole)
Lam2 = sp.Symbol('Lambda2', positive=True)
Pm = P + N * (-Lam2 / (2 * pp))                       # p^2 = -Lambda^2, p_T = 0
L1 = P * (1 - xi) + N * (LT2 / (2 * (1 - xi) * pp)) + LT   # massless real gluon
K1 = Pm - L1
k21 = sp.simplify(dot(K1, K1))
pslash_off = [Term(sp.Rational(1, 2), [('v', Pm)])]
S_off = sp.simplify(-tr_sum(mul(pslash_off, Gambar('a', K1, k21, dot(N, L1)), nslash, Gam('a', K1, k21, dot(N, L1))), kin).subs(D, 4))
F_off = sp.simplify(S_off / (4 * (1 - xi) * pp))
lim = sp.limit(F_off * LT2, LT2, sp.oo)
report('off-shell target: lim_{lT->oo} lT^2 x integrand = (1+xi^2)/(1-xi) (same UV pole)', sp.simplify(lim - Phat_qq.subs(epsD, 0)) == 0)

print()
print('SUMMARY s2: %d/%d PASS' % (sum(1 for _, o in results if o), len(results)))
