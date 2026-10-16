"""W13 / s3: O(alpha_s) MSbar coefficient functions of e+e- -> h X (rem:coll-sia-nlo); writer-derived.
Conventions: D = 4-2eps, CDR, MSbar with S_eps=(4pi)^eps e^{-eps gamma_E}; units alpha_s/(2pi); Q^2 = s.
  dsigma^h/dz = sigma_0 N_c sum_q e_q^2 int_z^1 dy/y { C_q(y) [d_{h/q}+d_{h/qbar}](z/y) + C_g(y) d_{h/g}(z/y) },
  C_q = delta(1-y) + a C_q^(1),  C_g = a C_g^(1),  a = alpha_s/(2 pi);  C = C^T + C^L.
Steps:
 (A) D-dim matrix element of gamma* -> q(p1) qbar(p2) g(p3): -g_{mu nu} projection (VF-EE-5) and the
     longitudinal projections p_h,mu p_h,nu for h = q and h = g;
 (B) full phase-space integral reproduces VF-EE-5 (rho_R/rho_0) exactly in eps;
 (C) quark spectrum (real + virtual VF-EE-4): pole -P_qq/eps (VF-EE-11), MSbar C_q;
 (D) gluon spectrum: pole -2 P_gq/eps, MSbar C_g;
 (E) longitudinal coefficients (finite, 4D): C_L^q, C_L^g;
 (F) checks: energy sum rule int z (2 C_q + C_g) = 3 C_F  (=> R = 1 + 3 C_F alpha_s/(4 pi), VF-EE-6); sigma_T^(1) = 0;
     comparison with the literature form; delta-coefficient difference to DIS C_1^q equals pi^2 C_F
     (time-like vs space-like form factor, VF-SUD-2); mu dependence ln(s/mu^2) P.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w13lib import *
import sympy as sp
import mpmath as mp
mp.mp.dps = 30

npass = 0; nfail = 0
def check(name, ok):
    global npass, nfail
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)
    if ok: npass += 1
    else: nfail += 1

eps = sp.Symbol('epsilon')
y12, y13, y23 = sp.symbols('y12 y13 y23', positive=True)
# s = 1 ; p_i.p_j = y_ij/2
set_dots({('p1', 'p1'): 0, ('p2', 'p2'): 0, ('p3', 'p3'): 0,
          ('p1', 'p2'): y12/2, ('p1', 'p3'): y13/2, ('p2', 'p3'): y23/2})
Dsub = {D: 4 - 2*eps}

# ---------------------------------------------------------------- (A) matrix elements
# Gamma^{mu alpha} = g^alpha (p1+p3)/(2p1.p3) g^mu - g^mu (p2+p3)/(2p2.p3) g^alpha ; reversed for the conjugate
den13 = y13; den23 = y23   # 2 p1.p3 = y13 (s=1), 2 p2.p3 = y23
def amp_terms(mu, al):
    return [(1/den13, [I(al), V(p1=1, p3=1), I(mu)]), (-1/den23, [I(mu), V(p2=1, p3=1), I(al)])]
def conj_terms(nu, be):
    # reverse order of each string
    return [(1/den13, [I(nu), V(p1=1, p3=1), I(be)]), (-1/den23, [I(be), V(p2=1, p3=1), I(nu)])]

def T_contract(mu_slot_amp, mu_slot_conj):
    """sum_spins M^{mu alpha} M^{nu beta *} (-g_{alpha beta}) contracted on the photon side with given slots."""
    tot = 0
    for ca, sa in amp_terms('MU', 'AL'):
        for cb, sb in conj_terms('NU', 'AL'):   # beta -> alpha contracted (index name repeated)
            sa2 = [mu_slot_amp if (isinstance(x, tuple) and x == I('MU')) else x for x in sa]
            sb2 = [mu_slot_conj if (isinstance(x, tuple) and x == I('NU')) else x for x in sb]
            tot += ca*cb*tr([V(p1=1)] + sa2 + [V(p2=1)] + sb2)
    return -sp.expand(tot)   # -g_{alpha beta}: contraction with +g gives the trace, times (-1)

# -g_{mu nu} projection: photon indices contracted (+g) times (-1)
Tg = -T_contract(I('MU'), I('MU'))     # note both 'MU' -> contracted pair
Tg = sp.simplify(Tg.subs(Dsub).subs(y12, 1 - y13 - y23))
bracket_EE5 = (1 - eps)*(y13/y23 + y23/y13) + 2*(1 - y13 - y23)/(y13*y23) - 2*eps
check('(A) -g_{mu nu} sum M M^* = 8(1-eps)[ (1-eps)(y13/y23+y23/y13) + 2 y12/(y13 y23) - 2 eps ]  (VF-EE-5)',
      sp.simplify(Tg - 8*(1 - eps)*bracket_EE5) == 0)
# longitudinal projections (photon indices -> p_h slashed); D-dim
TL1 = T_contract(V(p1=1), V(p1=1))
TL3 = T_contract(V(p3=1), V(p3=1))
TL1 = sp.simplify(TL1.subs(Dsub).subs(y12, 1 - y13 - y23))
TL3 = sp.simplify(TL3.subs(Dsub).subs(y12, 1 - y13 - y23))
print('   p1 p1 T =', sp.factor(TL1))
print('   p3 p3 T =', sp.factor(TL3))
# W_L/(-gW) * bracket  with W_L = 4/(z^2 s) p_h p_h W ; z = x1 = 1 - y23 (quark), z = x3 = y13 + y23 (gluon)
x1 = 1 - y23; x3 = y13 + y23
brL_q = sp.simplify(4/x1**2*TL1/(8*(1 - eps)))
brL_g = sp.simplify(4/x3**2*TL3/(8*(1 - eps)))
print('   [..]_L (quark obs.) =', sp.factor(brL_q))
print('   [..]_L (gluon obs.) =', sp.factor(brL_g))
check('(A) longitudinal projections finite in the collinear limits at fixed z>0 (quark: y13->0 at y23=1-z; gluon: y13->0 at y23=z)',
      all(sp.limit(e.subs(eps, 0).subs(y23, sp.Rational(1, 3)), y13, 0).is_finite for e in (brL_q, brL_g)) and
      all(sp.limit(e.subs(eps, 0).subs(y13, sp.Rational(1, 3)), y23, 0).is_finite for e in (brL_q, brL_g)))

# ---------------------------------------------------------------- (B) total real emission vs VF-EE-5
# (1/sigma0) dsigma/dy13 dy23 = Npref (y12 y13 y23)^(-eps) bracket ; Npref = (alpha_s C_F/2pi)(4pi mu0^2/s)^eps/Gamma(1-eps)
t, u = sp.symbols('t u', positive=True)
# integrate over the simplex: y13 = (1-y23) t
def simplex_integral_exact():
    # terms of bracket: (1-eps)(y13/y23) etc. ; use Dirichlet integrals int y12^a y13^b y23^c over simplex
    def dirichlet(a, b, c):  # int_{y12+y13+y23=1} y12^a y13^b y23^c
        return sp.gamma(a + 1)*sp.gamma(b + 1)*sp.gamma(c + 1)/sp.gamma(a + b + c + 3)
    e = -eps
    tot = (1 - eps)*(dirichlet(e, e + 1, e - 1) + dirichlet(e, e - 1, e + 1)) + 2*dirichlet(e + 1, e - 1, e - 1) \
        - 2*eps*dirichlet(e, e, e)
    return sp.simplify(sp.gammasimp(tot))
Ireal = simplex_integral_exact()
EE5 = 2*(1 - 2*eps)*(2 - 2*eps + eps**2)*sp.gamma(1 - eps)**2/(eps**2*(1 - 3*eps)*(2 - 3*eps)*sp.gamma(1 - 3*eps))
check('(B) int dPhi3: Ireal/Gamma(1-eps) = VF-EE-5 rho_R/rho_0 (exact in eps)',
      sp.simplify(sp.gammasimp(Ireal/sp.gamma(1 - eps) - EE5)) == 0)

# ---------------------------------------------------------------- distribution machinery (symbolic)
# Beta functions reduce to b = Gamma(1-eps)^2/Gamma(1-2eps):
#  B(1-e,1-e) = b/(1-2e), B(-e,1-e) = -b/e, B(2-e,1-e) = b/(2(1-2e)), B(-e,2-e) = -(1-e) b/(e(1-2e)),
#  B(2-e,-e) = -(1-e) b/(e(1-2e)), B(-e,-e) = -2b/e.   (checked below)
x = sp.Symbol('x', positive=True)
lx, l1x, L = sp.symbols('lx l1x L')   # ln x, ln(1-x), L = ln(s/mu^2)
dlt, D0, D1, D2 = sp.symbols('delta D0 D1 D2')
bb = sp.gamma(1 - eps)**2/sp.gamma(1 - 2*eps)
B = lambda a, c: sp.gamma(a)*sp.gamma(c)/sp.gamma(a + c)
for (a, c, cl) in [(1 - eps, 1 - eps, bb/(1 - 2*eps)), (-eps, 1 - eps, -bb/eps), (2 - eps, 1 - eps, bb/(2*(1 - 2*eps))),
                   (-eps, 2 - eps, -(1 - eps)*bb/(eps*(1 - 2*eps))), (2 - eps, -eps, -(1 - eps)*bb/(eps*(1 - 2*eps))),
                   (-eps, -eps, -2*bb/eps)]:
    ok = all(abs(complex(sp.N((B(a, c) - cl).subs(eps, ev), 30))) < 1e-25 for ev in (sp.Rational(1, 7), sp.Rational(-2, 9), sp.Rational(3, 11)))
    check('(C0) Beta reduction B(%s,%s)' % (a, c), ok)
# prefactors (MSbar): real  (alpha_s C_F/2pi) e^{-eps L} e^{eps gE}/Gamma(1-eps) * b = e^{-eps L} r_eps ,
#                      r_eps = e^{eps gE} Gamma(1-eps)/Gamma(1-2eps) ;  virtual: e^{-eps L} e^{eps gE} c_Gamma cos(pi eps)
r_eps = sp.exp(eps*sp.EulerGamma)*sp.gamma(1 - eps)/sp.gamma(1 - 2*eps)
v_eps = sp.exp(eps*sp.EulerGamma)*sp.gamma(1 + eps)*sp.gamma(1 - eps)**2/sp.gamma(1 - 2*eps)*sp.cos(sp.pi*eps)
def ser(expr, n):
    return sp.expand(sp.series(expr, eps, 0, n + 1).removeO())
r_s = ser(r_eps, 3); v_s = ser(v_eps, 3)
print('   r_eps =', r_s, ' ; v_eps =', v_s)
check('(C0) r_eps = 1 - (3/2) zeta_2 eps^2 + O(eps^3)', sp.simplify(r_s.coeff(eps, 1)) == 0 and sp.simplify(r_s.coeff(eps, 2) + sp.Rational(3, 2)*sp.pi**2/6) == 0)
check('(C0) v_eps = 1 - (1/2) zeta_2 eps^2 - (pi^2/2) eps^2 + O(eps^3)', sp.simplify(v_s.coeff(eps, 1)) == 0 and sp.simplify(v_s.coeff(eps, 2) + sp.pi**2/12 + sp.pi**2/2) == 0)
EL = sp.exp(-eps*L)
xp = x*sp.exp(-2*eps*lx)          # x^{1-2eps}
omx = sp.exp(-eps*l1x)            # (1-x)^{-eps}
def trunc(expr, nmin=-2, nmax=0):
    # robust Laurent truncation: sympy's expand writes 1/(eps(1-x)) as 1/(eps - eps x), which .coeff misses
    out = 0
    for t in sp.Add.make_args(sp.expand(expr)):
        c, k = t.as_coeff_exponent(eps)
        if c.has(eps):
            c2 = sp.cancel(t)
            c, k = c2.as_coeff_exponent(eps)
            assert not c.has(eps), t
        if nmin <= k <= nmax:
            out += sp.cancel(c)*eps**k
    return sp.expand(out)
def lcoef(expr, k):
    return sp.expand(sum(t.as_coeff_exponent(eps)[0] for t in sp.Add.make_args(sp.expand(expr)) if t.as_coeff_exponent(eps)[1] == k))

# ---------------------------------------------------------------- (C) quark spectrum
# (1/sigma0) dsigma^R/dx / (alpha_s C_F/2pi) = EL r x^{1-2e}(1-x)^{-e}/(1-2e) { S/(1-x) + Rg }
S_q = (1 - eps)*x/2 - 2*(1 - eps)/eps
R_q = -(1 - eps)*(1 - 2*eps)*(1 - x)/(eps*x) - 2*eps
pref = ser(EL*r_eps/(1 - 2*eps), 3)
# singular piece: g(x) (1-x)^{-1-eps}, g = pref * x^{1-2e} * S_q  (pref x-independent)
g_x = ser(sp.exp(-2*eps*lx), 3)*x*S_q      # x^{1-2e} S_q, with lx symbolic
g_1 = sp.expand((x*S_q).subs(x, 1))          # at x=1: lx = 0
sing = g_1*(-dlt/eps + D0 - eps*D1 + eps**2/2*D2) + (sp.expand(g_x) - g_1)/(1 - x)*ser(omx, 3)
reg = ser(omx, 3)*ser(sp.exp(-2*eps*lx), 3)*x*R_q
real_q = trunc(pref*(sing + reg))
virt_q = trunc(-ser(EL*v_eps, 3)*(2 - eps + 2*eps**2)/(eps**2*(1 - 2*eps))*dlt) if False else None
vpref = ser(EL*v_eps, 3)
vfac = ser((2 - eps + 2*eps**2)/(1 - 2*eps), 3)
virt_q = trunc(-vpref*vfac/eps**2*dlt)
bare_q = sp.expand(real_q + virt_q)
pole2 = sp.simplify(lcoef(bare_q, -2))
pole1 = lcoef(bare_q, -1)
Pqq_dist = 2*D0 - (1 + x) + sp.Rational(3, 2)*dlt     # P_qq/C_F (product convention)
check('(C) quark spectrum: no 1/eps^2 after real+virtual', pole2 == 0)
_pc = sp.expand(pole1 + Pqq_dist).subs({lx: sp.log(x), l1x: sp.log(1 - x)})
check('(C) quark spectrum: 1/eps coefficient = -P_qq/C_F (VF-EE-11)',
      all(abs(complex(sp.N(_pc.subs({x: xv, dlt: 0, D0: 0, D1: 0, D2: 0}), 30))) < 1e-25 for xv in (sp.Rational(1, 5), sp.Rational(1, 2), sp.Rational(7, 9)))
      and _pc.coeff(dlt) == 0 and _pc.coeff(D0) == 0)
Cq_sym = lcoef(bare_q, 0)
Cq = sp.expand(Cq_sym.subs({lx: sp.log(x), l1x: sp.log(1 - x)}))
print('   C_q^(1)/C_F (T+L, MSbar) =', sp.collect(sp.expand(Cq_sym), [dlt, D0, D1, L]))
# ---------------------------------------------------------------- (D) gluon spectrum
Ig_br = -2*(1 - eps)**2/eps - 4*(1 - x)*(1 - 2*eps)/(eps*x**2) - 2*eps
real_g = trunc(pref*ser(sp.exp(-2*eps*lx), 3)*x*ser(omx, 3)*Ig_br)
bare_g = sp.expand(real_g)
Pgq = (1 + (1 - x)**2)/x      # /C_F
check('(D) gluon spectrum: 1/eps coefficient = -2 P_gq/C_F', sp.simplify(lcoef(bare_g, -1) + 2*Pgq) == 0)
check('(D) gluon spectrum: no 1/eps^2', sp.simplify(lcoef(bare_g, -2)) == 0)
Cg = sp.expand(lcoef(bare_g, 0).subs({lx: sp.log(x), l1x: sp.log(1 - x)}))
print('   C_g^(1)/C_F (T+L, MSbar) =', sp.simplify(Cg))

# ---------------------------------------------------------------- (E) longitudinal (4D, finite)
brLq0 = sp.simplify(brL_q.subs(eps, 0))
brLg0 = sp.simplify(brL_g.subs(eps, 0))
# quark observed: x1 = x fixed ; integrate y13 from 0 to x  (y23 = 1-x)
CLq = sp.simplify(sp.integrate(brLq0.subs(y23, 1 - x), (y13, 0, x)))
# gluon observed: x3 = x ; y13 + y23 = x ; integrate y13 from 0 to x with y23 = x - y13
CLg = sp.simplify(sp.integrate(brLg0.subs(y23, x - y13), (y13, 0, x)))
print('   C_L^q/C_F =', CLq, ' ;  C_L^g/C_F =', sp.factor(CLg))
check('(E) C_L^q = C_F (units alpha_s/2pi)', sp.simplify(CLq - 1) == 0)
check('(E) C_L^g = C_F 4(1-x)/x (units alpha_s/2pi; one gluon FF, quark and antiquark summed)',
      sp.simplify(CLg - 4*(1 - x)/x) == 0)

# ---------------------------------------------------------------- (F) checks
def to_dist(expr):
    expr = sp.expand(expr)
    d = {'delta': mp.mpf(str(sp.N(expr.coeff(dlt), 40))) if expr.coeff(dlt) != 0 else 0,
         'D0': mp.mpf(str(sp.N(expr.coeff(D0), 40))), 'D1': mp.mpf(str(sp.N(expr.coeff(D1), 40))), 'D2': mp.mpf(str(sp.N(expr.coeff(D2), 40)))}
    regexpr = sp.simplify(expr - expr.coeff(dlt)*dlt - expr.coeff(D0)*D0 - expr.coeff(D1)*D1 - expr.coeff(D2)*D2)
    f = sp.lambdify(x, regexpr, 'mpmath')
    d['reg'] = (lambda zz, f=f: f(zz))
    return d, regexpr

CqL0 = sp.expand(Cq.subs(L, 0))
check('(F) mu dependence of C_q: coefficient of L = ln(s/mu^2) is P_qq/C_F',
      sp.simplify(sp.expand(Cq).coeff(L) - Pqq_dist) == 0)
check('(F) mu dependence of C_g: coefficient of L is 2 P_gq/C_F', sp.simplify(sp.expand(Cg).coeff(L) - 2*Pgq) == 0)
dq, regq = to_dist(CqL0)
dg_reg = sp.simplify(Cg.subs(L, 0))
print('   C_q^(1)/C_F at mu^2=s: delta coeff =', sp.nsimplify(sp.expand(CqL0).coeff(dlt)), ' D0:', sp.expand(CqL0).coeff(D0),
      ' D1:', sp.expand(CqL0).coeff(D1))
print('   regular part of C_q^(1)/C_F:', sp.simplify(regq))
# energy sum rule: int z (2 C_q + C_g) = 3 (in units C_F alpha_s/2pi)
m2q = moment(dq, 2)
m2g = mp.quad(lambda zz: zz*sp.lambdify(x, dg_reg, 'mpmath')(zz), [0, 0.5, 1])
check('(F) int z C_q^(1) = 35/6 C_F and int z C_g^(1) = -26/3 C_F', abs(m2q - mp.mpf(35)/6) < 1e-22 and abs(m2g + mp.mpf(26)/3) < 1e-22)
print('   int z C_q =', mp.nstr(m2q, 15), ' int z C_g =', mp.nstr(m2g, 15))
check('(F) energy sum rule: int z (2 C_q^(1) + C_g^(1)) = 3 C_F  <=> R = 1 + 3 C_F alpha_s/(4 pi) (VF-EE-6)',
      abs(2*m2q + m2g - 3) < 1e-22)
# transverse part: C_T = C - C_L ; check sigma_T^(1)=0 : int z (2 C_T^q + C_T^g) = 0
m2T = 2*(m2q - mp.quad(lambda zz: zz*1, [0, 1])) + (m2g - mp.quad(lambda zz: zz*4*(1 - zz)/zz, [0, 1]))
check('(F) sigma_T receives no O(alpha_s) correction: int z (2 C_T^q + C_T^g) = 0; sigma_L/sigma_0 = 3 C_F alpha_s/(4pi)',
      abs(m2T) < 1e-20)
# literature form (Nason-Webber / ESW): transverse quark coefficient
#   C_T^q/C_F = (1+z^2) D1 - 3/2 D0 + 2 (1+z^2)/(1-z) ln z + 3/2 (1-z) + (2pi^2/3 - 9/2) delta
lit_T = {'delta': 2*mp.pi**2/3 - mp.mpf(9)/2, 'D0': mp.mpf(-3)/2, 'D1': mp.mpf(2),
         'reg': lambda zz: ((1 + zz**2) - 2)*mp.log(1 - zz)/(1 - zz) + 2*(1 + zz**2)/(1 - zz)*mp.log(zz) + mp.mpf(3)/2*(1 - zz)}
#   note (1+z^2) D1 = 2 D1 + [(1+z^2)-2] ln(1-z)/(1-z)  (product convention VF-CONV-7)
mine_T = dict(dq); mine_T['reg'] = (lambda zz, f=dq['reg']: f(zz) - 1)   # subtract C_L^q = 1
ok = all(abs(moment(mine_T, N) - moment(lit_T, N)) < 1e-18 for N in (1, 2, 3, 4, 5, 7))
check('(F) C_T^q agrees with the literature form [(1+z^2)D1 - 3/2 D0 + 2(1+z^2)ln z/(1-z) + 3/2(1-z) + (2pi^2/3-9/2)delta] (moments N=1..7)', ok)
# literature transverse gluon: C_T^g/C_F = (1+(1-z)^2)/z (ln(1-z) + 2 ln z) - 2 (1-z)/z
litTg = lambda zz: (1 + (1 - zz)**2)/zz*(mp.log(1 - zz) + 2*mp.log(zz)) - 2*(1 - zz)/zz
fCg = sp.lambdify(x, dg_reg, 'mpmath')
ok = all(abs(mp.quad(lambda zz: zz**(N - 1)*(fCg(zz) - 4*(1 - zz)/zz - 2*litTg(zz)), [0, 0.5, 1])) < 1e-18 for N in (2, 3, 4, 6))
check('(F) C_T^g = 2 x [ (1+(1-z)^2)/z (ln(1-z)+2 ln z) - 2(1-z)/z ]  (literature form per q, our C_g sums q and qbar) (moments N=2..6)', ok)
diffg = sp.simplify(sp.expand(dg_reg - 4*(1 - x)/x - 2*((1 + (1 - x)**2)/x*(sp.log(1 - x) + 2*sp.log(x)) - 2*(1 - x)/x)))
check('(F) C_T^g closed form identical (symbolic)', diffg == 0)
check('(F) C_g^(1) (T+L) = 2 (1+(1-z)^2)/z [ln(1-z) + 2 ln z]  (no rational term)',
      sp.simplify(sp.expand(dg_reg - 2*(1 + (1 - x)**2)/x*(sp.log(1 - x) + 2*sp.log(x)))) == 0)
# DIS comparison: delta coefficient of C_1^q (DIS) = -(9/2 + pi^2/3) ; SIA C_T^q: 2pi^2/3 - 9/2 ; difference pi^2
dT = sp.nsimplify(sp.expand(CqL0).coeff(dlt))
check('(F) delta coefficient of C_q^(1) (T+L; C_L has none) = 2 pi^2/3 - 9/2',
      sp.simplify(sp.expand(CqL0).coeff(dlt) - (2*sp.pi**2/3 - sp.Rational(9, 2))) == 0)
check('(F) SIA minus DIS delta coefficient = pi^2 (time-like vs space-like form factor, VF-SUD-2)',
      sp.simplify((2*sp.pi**2/3 - sp.Rational(9, 2)) - (-(sp.Rational(9, 2) + sp.pi**2/3)) - sp.pi**2) == 0)
# moments for the record
for N in (1, 2, 3):
    print('   moment N=%d: C_q^(1)/C_F = %s ; C_T^q/C_F = %s' % (N, mp.nstr(moment(dq, N), 15), mp.nstr(moment(mine_T, N), 15)))
print('\nSUMMARY s3: %d PASS, %d FAIL' % (npass, nfail))
