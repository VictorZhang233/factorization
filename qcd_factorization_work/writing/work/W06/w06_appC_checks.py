r"""
w06_appC_checks.py -- writer W06: checks for App C (appC_dimreg.tex) not covered by the other W06 scripts.

 K1  P^_qq (D dims) = collinear limit of the e+e- real-emission matrix element (VF-EE-5, re-derived in w06_ee_oneloop.py):
     -g sum|M_3|^2 / (-g sum|M_2|^2) -> (8 pi a_s / s_13) C_F [(1+z^2)/(1-z) - eps (1-z)]
 K2  P^_qg = T_F [1 - 2z(1-z)/(1-eps)]: average over D-2 gluon polarisations of the g -> q qbar collinear vertex
 K3  P^_gg = 2 C_A [z/(1-z) + (1-z)/z + z(1-z)]: three-gluon vertex with physical polarisation sums, no eps term
 K4  averaging over 2 instead of D-2 gluon polarisations shifts the MS-bar coefficient by + P_qg (VF-CONV-6 logic)
 S1  e^{-eps gE} Gamma(1-eps) = 1 + pi^2 eps^2/12 + O(eps^3);  Gamma(1-eps) c_Gamma = 1 + O(eps^3)
 S2  one-loop form factor constant: -8 + zeta_2 (binding S_eps) vs -8 (Collins' S_eps)
 F1  form-factor reduction: F^(1) = -i g^2 C_F [ c1 s J(1,1,1) + c2 J(0,1,1) ] (+ scaleless), exact in D; closed form
 T1  master formula int d^Dk/(i pi^{D/2}) (-k^2 + Delta - i0)^{-a} = Gamma(a - D/2)/Gamma(a) Delta^{D/2-a} (numerical)
Run: python3 -I w06_appC_checks.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import itertools
import sympy as sp
import mpmath as mp
from w06_dtrace import trace, contract, dot, D as Dsym

e = sp.Symbol('eps')
Dv = 4 - 2 * e
z = sp.Symbol('z', positive=True)
RES = []


def check(name, cond):
    RES.append((name, bool(cond)))
    print(('PASS  ' if cond else 'FAIL  ') + name)


# ------------------------------------------------------------------------------------------------ K1
y13, y23, y12 = sp.symbols('y13 y23 y12', positive=True)
bracket = (1 - e) * (y13 / y23 + y23 / y13) + 2 * y12 / (y13 * y23) - 2 * e
# -g sum|M3|^2 = 8(1-eps) g^2 C_F N_c e_q^2 * bracket ;  -g sum|M2|^2 = 2(D-2) s N_c e_q^2 = 4(1-eps) s N_c e_q^2
# collinear q(p1) || g(p3): y13 -> 0, y12 -> z, y23 -> 1-z ; ratio * s13 = ratio * s y13 -> 8 pi a_s P^qq/C_F * C_F
ratio_times_s13 = sp.limit(sp.expand(8 * (1 - e) * bracket / (4 * (1 - e)) * y13).subs({y12: z, y23: 1 - z}), y13, 0)   # in units g^2 C_F
Pqq_hat = (1 + z ** 2) / (1 - z) - e * (1 - z)
check('K1  e+e- collinear limit: s13 |M3|^2/|M2|^2 -> 2 g^2 C_F [(1+z^2)/(1-z) - eps(1-z)] = (8 pi a_s) P^_qq', sp.simplify(ratio_times_s13 - 2 * Pqq_hat) == 0)

# ------------------------------------------------------------------------------------------------ K2, K3
# Sudakov kinematics: p1 = z pt + kT - kT^2/(z) n/(2 pt.n), p2 = (1-z) pt - kT - ...; all dot products in units s12 = 2 p1.p2 = 1
s12 = sp.Integer(1)
ptn = sp.Symbol('ptn', positive=True)       # pt.n
dots = {
    dot('p1', 'p1'): 0, dot('p2', 'p2'): 0, dot('n', 'n'): 0, dot('pt', 'pt'): 0,
    dot('p1', 'p2'): s12 / 2,
    dot('n', 'p1'): z * ptn, dot('n', 'p2'): (1 - z) * ptn, dot('n', 'pt'): ptn,
    dot('p1', 'pt'): (1 - z) * s12 / 2, dot('p2', 'pt'): z * s12 / 2,
}


def V(p, mu):
    return sp.Symbol('V_%s_%s' % (p, mu))


def gg(a, b):
    a, b = sorted([a, b])
    return sp.Symbol('g_%s_%s' % (a, b))


def dpol(P, a, b):
    """physical polarisation sum d^{ab}(P, n) = -g^{ab} + (P^a n^b + n^a P^b)/(P.n)"""
    return -gg(a, b) + (V(P, a) * V('n', b) + V('n', a) * V(P, b)) / sp.Symbol('dotn_%s' % P)


# K2: (1/(D-2)) d_{mu nu}(pt) Tr[p1slash g^mu p2slash g^nu]
tr = trace([('p', 'p1'), ('i', 'm'), ('p', 'p2'), ('i', 'n2')])
expr = contract(sp.expand(tr * dpol('pt', 'm', 'n2')))
expr = sp.expand(expr.subs(Dsym, Dv).subs({sp.Symbol('dotn_pt'): ptn}).subs(dots))
Kqg = sp.simplify(expr / (4 * dots[dot('p1', 'p2')]) / (Dv - 2))
check('K2  (1/(D-2)) d_{mu nu}(pt) Tr[p1 g^mu p2 g^nu] = 4 p1.p2 [1 - 2z(1-z)/(1-eps)]  ->  P^_qg = T_F[1 - 2z(1-z)/(1-eps)]',
      sp.simplify(Kqg - (1 - 2 * z * (1 - z) / (1 - e))) == 0)

# K3: three-gluon vertex, momenta incoming (p, mu), (-p1, nu), (-p2, rho), p = p1 + p2


def Vtx(mu, nu, rho):
    # g^{mu nu}(k1-k2)^rho + g^{nu rho}(k2-k3)^mu + g^{rho mu}(k3-k1)^nu with k1 = p1+p2, k2 = -p1, k3 = -p2
    return (gg(mu, nu) * (2 * V('p1', rho) + V('p2', rho)) + gg(nu, rho) * (V('p2', mu) - V('p1', mu))
            + gg(rho, mu) * (-2 * V('p2', nu) - V('p1', nu)))


amp = sp.expand(Vtx('a1', 'b1', 'c1') * Vtx('a2', 'b2', 'c2'))
pols = sp.expand(dpol('pt', 'a1', 'a2') * dpol('p1', 'b1', 'b2') * dpol('p2', 'c1', 'c2'))
# contract term by term (expansion may be large but finite)
tot = 0
for t1 in sp.Add.make_args(amp):
    for t2 in sp.Add.make_args(pols):
        tot += contract(t1 * t2)
tot = sp.expand(tot.subs(Dsym, Dv).subs({sp.Symbol('dotn_pt'): ptn, sp.Symbol('dotn_p1'): z * ptn, sp.Symbol('dotn_p2'): (1 - z) * ptn}).subs(dots))
Kgg = sp.simplify(tot / (Dv - 2))
shape = z / (1 - z) + (1 - z) / z + z * (1 - z)
ratio_gg = sp.simplify(Kgg / shape)
print('      three-gluon collinear factor / [z/(1-z)+(1-z)/z+z(1-z)] =', ratio_gg)
check('K3  three-gluon vertex with physical sums, averaged over D-2: proportional to z/(1-z)+(1-z)/z+z(1-z), no eps and no z in the ratio',
      ratio_gg.free_symbols == set() or (not ratio_gg.has(z) and not ratio_gg.has(e)))
# normalisation: the soft limit z -> 1 of P^_gg must be 2 C_A/(1-z) like the q -> q g kernel's 2 C_F/(1-z):
# with the same normalisation as K2 (divide by 4 p1.p2 = 2 s12): P^_gg/C_A = Kgg/(2 s12) * (1/?) -> check 2/(1-z) coefficient
soft_q = sp.limit((1 - z) * Pqq_hat, z, 1)          # 2 (C_F units)
soft_g = sp.limit((1 - z) * Kgg, z, 1)
print('      soft limits: (1-z) P^_qq/C_F -> %s ;  (1-z) Kgg -> %s' % (soft_q, soft_g))
# soft-gluon universality: (1-z) P^_gg -> 2 C_A exactly as (1-z) P^_qq -> 2 C_F; hence P^_gg/C_A = 2 Kgg/soft_g
Pgg_over_CA = sp.simplify(2 * Kgg / soft_g)
print('      P^_gg/C_A =', sp.factor(Pgg_over_CA))
check('K3b normalisation by the soft limit (1-z)P^_gg -> 2 C_A: P^_gg = 2 C_A [z/(1-z)+(1-z)/z+z(1-z)]',
      sp.simplify(Pgg_over_CA - 2 * shape) == 0 and soft_q == 2)

# ------------------------------------------------------------------------------------------------ K4
A_, B_ = sp.symbols('A B')
bare = -A_ / e + B_            # coefficient of a gluon-initiated partonic cross section with 1/(D-2) average (A ~ P_qg)
bare2 = sp.expand(sp.series((1 - e) * bare, e, 0, 1).removeO())      # average over 2 polarisations = (1-eps) x
check('K4  (1-eps)(-A/eps + B) = -A/eps + (B + A) + O(eps): after MS-bar subtraction of -A/eps the finite part shifts by +A (= +P_qg)',
      sp.simplify(bare2 - (-A_ / e + B_ + A_)) == 0)
# with the D-dim kernel: -(1/eps) P^_qg(z,eps) vs -(1/eps)(1-eps) P^_qg(z,eps): finite parts differ by P_qg(z) = T_F[z^2+(1-z)^2]
Pqg_hat = 1 - 2 * z * (1 - z) / (1 - e)
fin1 = sp.series(-Pqg_hat / e, e, 0, 1).removeO().coeff(e, 0)
fin2 = sp.series(-(1 - e) * Pqg_hat / e, e, 0, 1).removeO().coeff(e, 0)
check('K4b finite parts of -(1/eps)P^_qg with the two averages differ by z^2+(1-z)^2 (T_F units)', sp.simplify(fin2 - fin1 - (z ** 2 + (1 - z) ** 2)) == 0)

# ------------------------------------------------------------------------------------------------ S1, S2
EG = sp.EulerGamma
s_a = sp.series(sp.exp(-e * EG) * sp.gamma(1 - e), e, 0, 3).removeO()
check('S1a e^{-eps gE} Gamma(1-eps) = 1 + pi^2 eps^2/12 + O(eps^3)', sp.simplify(s_a - (1 + sp.pi ** 2 * e ** 2 / 12)) == 0)
cG = sp.gamma(1 + e) * sp.gamma(1 - e) ** 2 / sp.gamma(1 - 2 * e)
s_b = sp.series(sp.gamma(1 - e) * cG, e, 0, 3).removeO()
check('S1b Gamma(1-eps) c_Gamma = 1 + O(eps^3)', sp.simplify(s_b - 1) == 0)
s_c = sp.series(sp.exp(e * EG) * cG, e, 0, 3).removeO()
check('S1c e^{eps gE} c_Gamma = 1 - pi^2 eps^2/12 + O(eps^3)', sp.simplify(s_c - (1 - sp.pi ** 2 * e ** 2 / 12)) == 0)
f = -(2 - e + 2 * e ** 2) / (e ** 2 * (1 - 2 * e))
# binding: g0^2 = 4 pi a_s mu^{2eps} S^{-1}, S = (4pi)^eps e^{-eps gE}: (4pi mu0^2/Q^2)^eps c_Gamma -> (mu^2/Q^2)^eps e^{eps gE} c_Gamma
const_bind = sp.series(sp.exp(e * EG) * cG * f, e, 0, 1).removeO().coeff(e, 0)
const_coll = sp.series(sp.gamma(1 - e) * cG * f, e, 0, 1).removeO().coeff(e, 0)
check('S2  form-factor constant at mu^2 = Q^2: -8 + zeta_2 (binding S_eps), -8 (Collins S_eps)',
      sp.simplify(const_bind - (-8 + sp.pi ** 2 / 6)) == 0 and sp.simplify(const_coll + 8) == 0)

# ------------------------------------------------------------------------------------------------ F1
# Lambda^mu = -i g^2 C_F int d^Dl/(2pi)^D g^a (p1-l) g^mu (-p2-l) g_a / [l^2 (p1-l)^2 (p2+l)^2]
# F1 = Tr[p1 Lambda^mu p2 g_mu]/Tr[p1 g^mu p2 g_mu]; Da = l^2, Db = (p1-l)^2 = Da - 2 l.p1, Dc = (p2+l)^2 = Da + 2 l.p2
def lin_trace(slots_lin):
    choices = []
    for s_ in slots_lin:
        if s_[0] == 'p' and isinstance(s_[1], list):
            choices.append([(c, ('p', nm)) for c, nm in s_[1]])
        else:
            choices.append([(1, s_)])
    tot_ = 0
    for combo in itertools.product(*choices):
        coef = 1
        sl = []
        for c, s_ in combo:
            coef *= c
            sl.append(s_)
        tot_ += coef * trace(sl)
    return sp.expand(tot_)


num = lin_trace([('p', 'p1'), ('i', 'a'), ('p', [(1, 'p1'), (-1, 'l')]), ('i', 'm'), ('p', [(-1, 'p2'), (-1, 'l')]), ('i', 'a'), ('p', 'p2'), ('i', 'm')])
num = sp.expand(contract(num).subs(Dsym, Dv))
den = sp.expand(contract(trace([('p', 'p1'), ('i', 'm'), ('p', 'p2'), ('i', 'm')])).subs(Dsym, Dv))
Da, Db, Dc, s = sp.symbols('Da Db Dc s')
sub = {dot('l', 'l'): Da, dot('l', 'p1'): (Da - Db) / 2, dot('l', 'p2'): (Dc - Da) / 2, dot('p1', 'p1'): 0, dot('p2', 'p2'): 0, dot('p1', 'p2'): s / 2}
numR = sp.expand(num.subs(sub))
denR = sp.expand(den.subs(sub))
# numR is a polynomial in Da, Db, Dc; divide by Da Db Dc: monomials Da^i Db^j Dc^k -> J(1-i, 1-j, 1-k)
P = sp.Poly(numR, Da, Db, Dc)
coef_J = {}
for (i, j, k), c in P.terms():
    key = (1 - i, 1 - j, 1 - k)
    coef_J[key] = sp.simplify(coef_J.get(key, 0) + c / denR)
# scaleless: any J with index <= 0 on Da AND on the other except the (Db, Dc) pair... non-zero ones: J(1,1,1), J(0,1,1), J(-1,1,1)
nonzero = {k_: v for k_, v in coef_J.items() if (k_[1] >= 1 and k_[2] >= 1)}
print('      reduced numerator / Tr[p1 g p2 g]: non-scaleless coefficients ', nonzero)
# J(-1,1,1) = -(s/2) J(0,1,1)
c1 = sp.simplify(nonzero.get((1, 1, 1), 0) / s)
c2 = sp.simplify(nonzero.get((0, 1, 1), 0) - s / 2 * nonzero.get((-1, 1, 1), 0))
print('      F1 = -i g^2 C_F [ c1 s J(1,1,1) + c2 J(0,1,1) ],  c1 =', sp.factor(c1), ',  c2 =', sp.factor(c2))
# J's (Minkowski, s -> -Q2 continued): J111 = -i/(4pi)^{D/2} G(1+e)G(-e)^2/G(1-2e) (-s)^{-1-e};  J011 = i/(4pi)^{D/2} G(1,1) (-s)^{-e}
G11 = sp.gamma(e) * sp.gamma(1 - e) ** 2 / sp.gamma(2 - 2 * e)
J111 = -sp.I * sp.gamma(1 + e) * sp.gamma(-e) ** 2 / sp.gamma(1 - 2 * e)          # times (-s)^{-1-e}/(4pi)^{D/2}
J011 = sp.I * G11                                                               # times (-s)^{-e}/(4pi)^{D/2}
# s J111 = s * (-s)^{-1-e} = -(-s)^{-e}
F1 = -sp.I * c1 * (-J111) - sp.I * c2 * J011          # times g^2 C_F (-s)^{-e}/(4pi)^{D/2}
# compare: F1_ref = -(a_s C_F/4pi)(4pi mu0^2/(-s))^eps c_G f-numerator  =  g^2 C_F/(4pi)^{2-eps} (-s)^{-eps} * [-c_G (2-e+2e^2)/(e^2(1-2e))]
ref = -cG * (2 - e + 2 * e ** 2) / (e ** 2 * (1 - 2 * e))
okF1 = all(abs(sp.N((F1 / ref).subs(e, ev), 30) - 1) < 1e-25 for ev in (sp.Rational(1, 7), sp.Rational(-2, 9), sp.Rational(3, 11)))
check('F1  form factor from the reduction to J(1,1,1), J(0,1,1): F^(1) = -(a_s C_F/4pi)(4pi mu0^2/(-q^2))^eps c_G (2-e+2e^2)/(e^2(1-2e))', okF1)

# ------------------------------------------------------------------------------------------------ T1
mp.mp.dps = 30
okT1 = True
for (a, Dn, Del) in ((2.3, 3.4, 1.7), (3.0, 4.6, 0.6), (1.6, 2.5, 2.2)):
    # Euclidean: int d^Dk_E/pi^{D/2} (k_E^2 + Delta)^{-a} = Gamma(a-D/2)/Gamma(a) Delta^{D/2-a}; radial: Omega_D/(pi^{D/2}) int k^{D-1}
    rad = 2 / mp.gamma(mp.mpf(Dn) / 2) * mp.quad(lambda k: k ** (Dn - 1) / (k ** 2 + Del) ** a, [0, 1, mp.inf])
    cl = mp.gamma(a - mp.mpf(Dn) / 2) / mp.gamma(a) * mp.mpf(Del) ** (mp.mpf(Dn) / 2 - a)
    okT1 &= abs(rad / cl - 1) < 1e-20
check('T1  master formula (Euclidean form, Wick rotation of the Minkowski one) checked numerically in its convergence domain', okT1)
print()
print('SUMMARY: %d/%d checks passed' % (sum(p for _, p in RES), len(RES)))
