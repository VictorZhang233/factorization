"""W12 (Ch10) -- independent re-derivation of the O(alpha_s) DIS coefficient functions.

Steps (all exact in eps = (4-D)/2 where stated):
 A. D-dimensional projected squared matrix elements for gamma* q -> q g and gamma* g -> q qbar
    (own trace engine dtrace.py; polarization sum -g checked against the light-cone sum).
 B. D-dimensional two-body phase space (direct derivation).
 C. y-integrals (Beta functions)  ->  R_2^q, R_L^q, R_2^g, R_L^g exactly in eps; compare with VF-DIS-4/5.
 D. Expansion in distributions (product convention of VF-CONV-7); virtual term from VF-SUD-1;
    pole bookkeeping; MSbar mass factorization  ->  C_2^q, C_2^g, C_L^q, C_L^g (VF-DIS-7).
 E. Mellin moments of the x-space results vs VF-DIS-8 (N = 1..8); whole-bracket-plus form (VF-DIS-9);
    Adler and Bjorken checks (VF-DIS-14); averaging over 2 gluon polarizations (VF-CONV-6).
Run:  python3 -I w12_nlo.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
from dtrace import trace, V, I, D

eps, z, y, Q2 = sp.symbols('epsilon z y Q2', positive=True)
s, t, u = sp.symbols('s t u')   # partonic Mandelstams shat, that, uhat
EG = sp.EulerGamma
z2 = sp.zeta(2)

print('=' * 78)
print('A. Projected squared matrix elements in D = 4 - 2 eps')
# ---------------- quark channel  gamma*(q) + q(p) -> q(pp) + g(k) ----------------
# invariants: p^2=k^2=pp^2=0, q^2=-Q2, s=(p+q)^2, t=(p-k)^2, u=(p-pp)^2=(q-k)^2, s+t+u=-Q2
def dot_q(a, b):
    a, b = sorted((a, b))
    tab = {('p', 'p'): 0, ('k', 'k'): 0, ('pp', 'pp'): 0, ('q', 'q'): -Q2,
           ('p', 'q'): (s + Q2) / 2, ('k', 'p'): -t / 2, ('p', 'pp'): -u / 2,
           ('k', 'q'): -(u + Q2) / 2, ('k', 'pp'): s / 2, ('pp', 'q'): (s + u) / 2,
           ('n', 'n'): 0, ('n', 'p'): sp.Symbol('np'), ('k', 'n'): sp.Symbol('nk'),
           ('n', 'pp'): sp.Symbol('npp'), ('n', 'q'): sp.Symbol('nq')}
    return tab[(a, b)]

# slashed sums are expanded by linearity: A = p + q (s-channel), B = p - k (t-channel)
def string_q(proj):
    """sum over spins and pol (-g_{rho sigma}) of M^mu M^{nu*} contracted with proj.
    proj = 'g'  -> (-g_{mu nu});  proj = 'pp' -> p_mu p_nu."""
    res = sp.Integer(0)
    A = [('p', 1), ('q', 1)]
    B = [('p', 1), ('k', -1)]
    def slot_mu(which):
        if proj == 'g':
            return I('mu') if which == 'mu' else I('mu')
        return V('p')
    # amplitude Gamma^mu = g^rho A g^mu / s + g^mu B g^rho / t
    # conjugate  Gbar^nu = g^nu A g^sigma / s + g^sigma B g^nu / t   (sigma -> rho with -1)
    terms_amp = [([I('rho'), 'A', slot_mu('mu')], 1 / s), ([slot_mu('mu'), 'B', I('rho')], 1 / t)]
    terms_cnj = [([slot_mu('nu'), 'A', I('rho')], 1 / s), ([I('rho'), 'B', slot_mu('nu')], 1 / t)]
    for ga, ca in terms_amp:
        for gc, cc in terms_cnj:
            # expand the momentum sums A, B
            def expand(seq):
                out = [([], 1)]
                for el in seq:
                    if el == 'A' or el == 'B':
                        lst = A if el == 'A' else B
                        out = [(sl + [V(v)], c * w) for sl, c in out for v, w in lst]
                    else:
                        out = [(sl + [el], c) for sl, c in out]
                return out
            for sa, wa in expand(ga):
                for sc, wc in expand(gc):
                    slots = [V('pp')] + sa + [V('p')] + sc
                    tr = trace(slots, dot_q)
                    sign = -1   # pol sum -g_{rho sigma}
                    if proj == 'g':
                        sign *= -1   # projector -g_{mu nu}
                    res += sign * ca * cc * wa * wc * tr
    return sp.simplify(sp.expand(res))

Mg_q = string_q('g')
Mp_q = string_q('pp')
Mg_q_exp = 8 * (1 - eps) * ((1 - eps) * (-t / s - s / t) + 2 * u * Q2 / (s * t) + 2 * eps)
Mp_q_exp = -4 * (1 - eps) * u
sub_u = {u: -Q2 - s - t}
chk1 = sp.simplify((Mg_q - Mg_q_exp).subs(D, 4 - 2 * eps).subs(sub_u))
chk2 = sp.simplify((Mp_q - Mp_q_exp).subs(D, 4 - 2 * eps).subs(sub_u))
print('quark channel  (-g) projection = 8(1-e)[(1-e)(-t/s-s/t)+2uQ2/(st)+2e] :', 'PASS' if chk1 == 0 else chk1)
print('quark channel  (p p) projection = -4(1-e) u                              :', 'PASS' if chk2 == 0 else chk2)

# ---------------- gluon channel  gamma*(q) + g(p) -> q(k1) + qbar(k2) ----------------
# t=(p-k1)^2, u=(p-k2)^2=(k1-q)^2, s=(p+q)^2
def dot_g(a, b):
    a, b = sorted((a, b))
    tab = {('p', 'p'): 0, ('k1', 'k1'): 0, ('k2', 'k2'): 0, ('q', 'q'): -Q2,
           ('p', 'q'): (s + Q2) / 2, ('k1', 'p'): -t / 2, ('k2', 'p'): -u / 2,
           ('k1', 'k2'): s / 2, ('k1', 'q'): -(u + Q2) / 2, ('k2', 'q'): -(t + Q2) / 2,
           ('n', 'n'): 0, ('n', 'p'): sp.Symbol('np'), ('k1', 'n'): sp.Symbol('nk1'),
           ('k2', 'n'): sp.Symbol('nk2'), ('n', 'q'): sp.Symbol('nq')}
    return tab[(a, b)]

def string_g(proj, polsum='g'):
    A = [('k1', 1), ('q', -1)]     # k1 - q, denominator u
    B = [('k1', 1), ('p', -1)]     # k1 - p, denominator t
    res = sp.Integer(0)
    def slot_mu():
        return I('mu') if proj == 'g' else V('p')
    terms_amp = [([slot_mu(), 'A', I('rho')], 1 / u), ([I('rho'), 'B', slot_mu()], 1 / t)]
    terms_cnj = [([I('sig'), 'A', slot_mu()], 1 / u), ([slot_mu(), 'B', I('sig')], 1 / t)]
    def expand(seq):
        out = [([], 1)]
        for el in seq:
            if el in ('A', 'B'):
                lst = A if el == 'A' else B
                out = [(sl + [V(v)], c * w) for sl, c in out for v, w in lst]
            else:
                out = [(sl + [el], c) for sl, c in out]
        return out
    for ga, ca in terms_amp:
        for gc, cc in terms_cnj:
            for sa, wa in expand(ga):
                for sc, wc in expand(gc):
                    base = [V('k1')] + sa + [V('k2')] + sc
                    sgn_proj = -1 if proj == 'g' else 1
                    if polsum == 'g':
                        slots = [(('i', 'rho') if x == ('i', 'sig') else x) for x in base]
                        res += sgn_proj * (-1) * ca * cc * wa * wc * trace(slots, dot_g)
                    else:
                        # light-cone sum: -g + (p n + n p)/(n.p) ; the extra term: replace rho->p, sig->n etc.
                        slots = [(('i', 'rho') if x == ('i', 'sig') else x) for x in base]
                        res += sgn_proj * (-1) * ca * cc * wa * wc * trace(slots, dot_g)
                        for (r1, r2) in (('p', 'n'), ('n', 'p')):
                            sl2 = [(V(r1) if x == ('i', 'rho') else (V(r2) if x == ('i', 'sig') else x)) for x in base]
                            res += sgn_proj * ca * cc * wa * wc * trace(sl2, dot_g) / sp.Symbol('np')
    return sp.simplify(sp.expand(res))

Mg_g = string_g('g')
Mp_g = string_g('pp')
Mg_g_exp = 8 * (1 - eps) * ((1 - eps) * (u / t + t / u) - 2 * s * Q2 / (t * u) - 2 * eps)
Mp_g_exp = 8 * s
chk3 = sp.simplify((Mg_g - Mg_g_exp).subs(D, 4 - 2 * eps).subs({s: -Q2 - t - u}))
chk4 = sp.simplify((Mp_g - Mp_g_exp).subs(D, 4 - 2 * eps).subs({s: -Q2 - t - u}))
print('gluon channel  (-g) projection = 8(1-e)[(1-e)(u/t+t/u)-2sQ2/(tu)-2e]     :', 'PASS' if chk3 == 0 else chk3)
print('gluon channel  (p p) projection = 8 s                                    :', 'PASS' if chk4 == 0 else chk4)
# light-cone polarization sum (gauge-invariance check of the -g replacement)
Mg_g_lc = string_g('g', polsum='lc')
# n is arbitrary light-like; impose momentum conservation n.k2 = n.p + n.q - n.k1
chk5 = sp.simplify((Mg_g_lc - Mg_g).subs({sp.Symbol('nk2'): sp.Symbol('np') + sp.Symbol('nq') - sp.Symbol('nk1')}).subs({s: -Q2 - t - u}))
print('gluon channel: light-cone polarization sum = -g sum                       :', 'PASS' if chk5 == 0 else chk5)

print('=' * 78)
print('B. Two-body phase space in D dims')
# dPhi_2 = |k|^{D-3}/(4 sqrt(s)(2pi)^{D-2}) dOmega_{D-2}, |k| = sqrt(s)/2,
# dOmega_{D-2} = Omega_{D-3} sin^{D-3}theta dtheta = Omega_{D-3} 2^{D-3} [y(1-y)]^{(D-4)/2} dy
sh = sp.Symbol('shat', positive=True)
Dd = 4 - 2 * eps
Omega = lambda n: 2 * sp.pi ** ((n + 1) / sp.Integer(2)) / sp.gamma((n + 1) / sp.Integer(2))   # area of S^n
pref = (sp.sqrt(sh) / 2) ** (Dd - 3) / (4 * sp.sqrt(sh) * (2 * sp.pi) ** (Dd - 2)) * Omega(Dd - 3) * 2 ** (Dd - 3)
target = (4 * sp.pi / sh) ** eps / (8 * sp.pi * sp.gamma(1 - eps))
print('phase space prefactor = (4pi/s)^e/(8 pi Gamma(1-e)) :',
      'PASS' if sp.simplify(sp.gammasimp(pref / target)) == 1 else sp.simplify(pref / target))

print('=' * 78)
print('C. Exact-in-eps partonic structure functions')
# overall:  (1/4pi) * avg colour/spin * g0^2 * dPhi_2 ; g0^2 = 4 pi as mu^{2e} e^{e gE} (4pi)^{-e}
# => (as/2pi) * [colour] * (1/8) (mu^2/s)^e e^{e gE}/Gamma(1-e) * int dy [y(1-y)]^{-e} (...)
# with the quark average 1/2 (spin) and colour C_F (after 1/N_c and Tr t^a t^a), the factor (1/2) is included
# below explicitly; s = Q2 (1-z)/z,  t = -Q2 y / z,  u = -Q2 (1-y)/z.
kin = {s: Q2 * (1 - z) / z, t: -Q2 * y / z, u: -Q2 * (1 - y) / z}
def yint(expr):
    """int_0^1 dy [y(1-y)]^{-e} expr, expr rational in y with poles only at y=0, y=1 (Beta functions)."""
    expr = sp.apart(sp.expand(sp.together(expr)), y)
    total = 0
    for term in sp.Add.make_args(sp.expand(expr)):
        f = sp.factor(term)
        a = 0; b = 0; coeff = sp.Integer(1)
        for fac in sp.Mul.make_args(f):
            base, ex = fac.as_base_exp()
            if base == y:
                a += ex
            elif sp.expand(base - (y - 1)) == 0:
                b += ex; coeff *= (-1) ** ex
            elif sp.expand(base - (1 - y)) == 0:
                b += ex
            elif base.has(y):
                # polynomial in y: expand and recurse
                if fac.is_polynomial(y):
                    rest = sp.Mul(*[g for g in sp.Mul.make_args(f) if g is not fac])
                    total += yint(sp.expand(fac) * rest)
                    a = None
                    break
                raise ValueError('unexpected factor %s in %s' % (fac, term))
            else:
                coeff *= fac
        if a is None:
            continue
        total += coeff * sp.gamma(1 + a - eps) * sp.gamma(1 + b - eps) / sp.gamma(2 + a + b - 2 * eps)
    return sp.simplify(total)

# quark channel, F_2 and F_L projections:  F2/z = 1/(1-e)[(-g)W + (3-2e) 4 z^2/Q2 (pp)W], FL/z = 8 z^2/Q2 (pp) W
avg_q = sp.Rational(1, 2)   # spin 1/2 ; colour gives C_F (factored out)
proj2_q = (Mg_q_exp + (3 - 2 * eps) * 4 * z ** 2 / Q2 * Mp_q_exp) / (1 - eps)
projL_q = 8 * z ** 2 / Q2 * Mp_q_exp
# normalised: Fhat/(z e^2) = (as/2pi) C_F (mu^2/Q2)^e R ;   (mu^2/s)^e = (mu^2/Q2)^e z^e (1-z)^-e
common4 = sp.Rational(1, 4) * sp.exp(eps * EG) / sp.gamma(1 - eps) * z ** eps * (1 - z) ** (-eps)  # (1/4pi)(4pi)(1/8pi)(2pi)
R2q = sp.simplify(common4 * avg_q * yint(proj2_q.subs(kin)))
R2q_vf = sp.exp(eps * EG) * sp.gamma(-eps) / (2 * sp.gamma(2 - 2 * eps)) * z ** eps * (1 - z) ** (-1 - eps) * (2 * (1 + z ** 2) - eps * (7 - 2 * z) + eps ** 2)
RLq = sp.simplify(common4 * avg_q * yint(projL_q.subs(kin)))
RLq_vf = sp.exp(eps * EG) * sp.gamma(2 - eps) / sp.gamma(2 - 2 * eps) * 2 * z * (z / (1 - z)) ** eps
def ratio_ok(expr):
    vals = []
    for zz in (sp.Rational(1, 7), sp.Rational(1, 2), sp.Rational(5, 6)):
        for ee in (sp.Rational(1, 10), sp.Rational(-3, 10), sp.Rational(1, 3)):
            vals.append(abs(sp.N(expr.subs({z: zz, eps: ee}), 30) - 1))
    return max(vals) < 1e-25
r1 = 1 if ratio_ok(R2q / R2q_vf) else R2q / R2q_vf
r2 = 1 if ratio_ok(RLq / RLq_vf) else RLq / RLq_vf
print('R_2^q exact = VF-DIS-4 :', 'PASS' if r1 == 1 else r1)
print('R_L^q exact = VF-DIS-4 :', 'PASS' if r2 == 1 else r2)
# gluon channel: average 1/(2(1-e)) over polarizations, colour T_F
avg_g = 1 / (2 * (1 - eps))
kin_g = {s: Q2 * (1 - z) / z, t: -Q2 * y / z, u: -Q2 * (1 - y) / z}
proj2_g = (Mg_g_exp + (3 - 2 * eps) * 4 * z ** 2 / Q2 * Mp_g_exp) / (1 - eps)
projL_g = 8 * z ** 2 / Q2 * Mp_g_exp
R2g = sp.simplify(common4 * avg_g * yint(proj2_g.subs(kin_g)))
RLg = sp.simplify(common4 * avg_g * yint(projL_g.subs(kin_g)))
R2g_vf = 2 * sp.exp(eps * EG) * sp.gamma(-eps) / sp.gamma(2 - 2 * eps) * (z / (1 - z)) ** eps * (z ** 2 + (1 - z) ** 2 - 3 * eps + 4 * eps ** 2 - 2 * eps ** 3) / (1 - eps) ** 2
RLg_vf = sp.exp(eps * EG) * sp.gamma(1 - eps) / sp.gamma(2 - 2 * eps) * 8 * z * (1 - z) / (1 - eps) * (z / (1 - z)) ** eps
r3 = 1 if ratio_ok(R2g / R2g_vf) else R2g / R2g_vf
r4 = 1 if ratio_ok(RLg / RLg_vf) else RLg / RLg_vf
print('R_2^g exact = VF-DIS-5 :', 'PASS' if r3 == 1 else r3)
print('R_L^g exact = VF-DIS-5 :', 'PASS' if r4 == 1 else r4)

print('=' * 78)
print('D. Expansion in distributions, virtual term, poles, MSbar coefficient functions')
def ser(expr, n=1):
    """Laurent series in eps up to and including eps^(n-1)."""
    return sp.expand(sp.series(expr, eps, 0, n).removeO())

# --- quark channel, F_2 ---
A = sp.exp(eps * EG) * sp.gamma(-eps) / (2 * sp.gamma(2 - 2 * eps))
G = z ** eps * (2 * (1 + z ** 2) - eps * (7 - 2 * z) + eps ** 2)
G1 = G.subs(z, 1)
c_delta = ser(A * (-1 / eps) * G1)
c_D0 = ser(A * G1)
c_D1 = ser(A * (-eps) * G1)
c_D2 = ser(A * eps ** 2 / 2 * G1)
reg_full = A * (G - G1) * (1 - z) ** (-1 - eps)
def laurent_at(expr, zz, n_lo=-1, n_hi=0):
    e2 = expr.subs(z, zz)
    sr = sp.series(e2, eps, 0, n_hi + 1).removeO()
    return [sp.N(sp.expand(sr).coeff(eps, k), 30) for k in range(n_lo, n_hi + 1)]
exp_regfin = -(1 + z) * sp.log(1 - z) - (1 + z ** 2) / (1 - z) * sp.log(z) + 3 + 2 * z
ok_regpole = True; ok_regfin = True
for zz in (sp.Rational(1, 9), sp.Rational(1, 2), sp.Rational(7, 8)):
    cm1, c0 = laurent_at(reg_full, zz)
    ok_regpole &= abs(cm1 - sp.N((1 + z).subs(z, zz), 30)) < 1e-25
    ok_regfin &= abs(c0 - sp.N(exp_regfin.subs(z, zz), 30)) < 1e-25
reg_pole = 1 + z
print('R_2^q:  delta coeff =', sp.simplify(c_delta))
print('        D_0 coeff   =', c_D0, ';  D_1 coeff =', c_D1, ';  D_2 coeff =', c_D2)
exp_delta = 2 / eps ** 2 + sp.Rational(3, 2) / eps + sp.Rational(7, 2) - 3 * z2
ok_delta = sp.simplify(c_delta - exp_delta) == 0
ok_D0 = sp.simplify(c_D0 - (-2 / eps - sp.Rational(3, 2))) == 0
ok_D1 = sp.simplify(c_D1 - 2) == 0
print('R_2^q expansion = VF-DIS-4 (delta, D0, D1, reg pole, reg finite):', ok_delta, ok_D0, ok_D1, ok_regpole, ok_regfin)

# --- virtual: 2 F^(1) delta in units (as/2pi) C_F (mu^2/Q^2)^eps ---
K = sp.exp(eps * EG) * sp.gamma(1 + eps) * sp.gamma(1 - eps) ** 2 / sp.gamma(1 - 2 * eps)
Vv = K * (-(2 - eps + 2 * eps ** 2) / (eps ** 2 * (1 - 2 * eps)))
Vser = sp.simplify(ser(Vv, 2))
print('virtual 2F^(1):', Vser, '  (expect -2/e^2 - 3/e - 8 + zeta2 + O(e))')
print('   check:', sp.simplify(ser(Vv) - (-2 / eps ** 2 - 3 / eps - 8 + z2)) == 0)
# --- sum: poles and finite delta coefficient ---
tot_delta = sp.simplify(c_delta + ser(Vv))
print('real+virtual delta coefficient:', tot_delta, ' -> 1/e^2:', sp.simplify(sp.expand(tot_delta * eps ** 2).subs(eps, 0)),
      ', 1/e:', sp.simplify(sp.expand(tot_delta * eps).coeff(eps, 0)) if False else '', '')
pole1 = sp.expand(tot_delta).coeff(eps, -1)
fin0 = sp.expand(tot_delta).coeff(eps, 0)
print('   1/eps coefficient of delta (real 3/2 + virtual -3) =', pole1, ';  finite delta coefficient =', sp.nsimplify(fin0), '=', sp.simplify(fin0 + sp.Rational(9, 2) + sp.pi ** 2 / 3) == 0 and '-(9/2+pi^2/3)')
# pole of the whole: -2 D0 + 1 + z + (3/2-3) delta  = - P_qq / C_F
# P_qq/C_F = 2 D0 - (1+z) + 3/2 delta  (product convention)
print('   1/eps part = -P_qq/C_F :', sp.simplify(c_D0.coeff(eps, -1) - (-2)) == 0 and sp.simplify(reg_pole - (1 + z)) == 0 and sp.simplify(pole1 + sp.Rational(3, 2)) == 0)

# --- gluon channel ---
R2g_ser = ser(R2g_vf.subs(z, z))
R2g_pole = sp.simplify(sp.expand(R2g_ser).coeff(eps, -1))
R2g_fin = sp.simplify(sp.expand(R2g_ser).coeff(eps, 0))
Pqg = z ** 2 + (1 - z) ** 2
C2g_exp = Pqg * sp.log((1 - z) / z) - 8 * z ** 2 + 8 * z - 1
okg1 = sp.simplify(R2g_pole + 2 * Pqg) == 0
okg2 = all(abs(sp.N((R2g_fin - 2 * C2g_exp).subs(z, zz), 30)) < 1e-25 for zz in (sp.Rational(1, 9), sp.Rational(1, 2), sp.Rational(7, 8)))
print('R_2^g = -(2/e) P_qg/T_F + 2 C_2^g/T_F + O(e):', okg1, okg2)
RLq_ser = sp.simplify(ser(RLq_vf).subs(eps, 0))
RLg_ser = sp.simplify(ser(RLg_vf).subs(eps, 0))
print('R_L^q(e=0) =', RLq_ser, ';  R_L^g(e=0) =', sp.factor(RLg_ser))
# averaging over 2 polarizations: R_2^g -> (1-eps) R_2^g
R2g_2pol = ser(R2g_vf * (1 - eps))
shift = sp.simplify(sp.expand(R2g_2pol).coeff(eps, 0) - R2g_fin)
print('gluon average over 2 polarizations: shift of 2 C_2^g/T_F =', sp.factor(shift), ' (expect 2 P_qg/T_F)')

print('=' * 78)
print('E. Mellin moments vs VF-DIS-8; whole-bracket plus; Adler, Bjorken')
import mpmath as mp
mp.mp.dps = 40
def S(k, n):
    return sum(mp.mpf(1) / mp.mpf(j) ** k for j in range(1, n + 1))
def C2qN_vf(N):
    S1, S2 = S(1, N), S(2, N)
    return S1 ** 2 - S2 + mp.mpf(3) / 2 * S1 - S1 / (N * (N + 1)) + mp.mpf(3) / (2 * N) + mp.mpf(2) / (N + 1) + mp.mpf(1) / N ** 2 - mp.mpf(9) / 2
def C2gN_vf(N):
    S1 = S(1, N)
    return -mp.mpf(N ** 2 + N + 2) / (N * (N + 1) * (N + 2)) * S1 + mp.mpf(1) / N ** 2 - mp.mpf(1) / N + mp.mpf(6) / ((N + 1) * (N + 2))
def mom_C2q(N):
    # C_2^q/C_F = 2 D1 - 3/2 D0 - (1+z) ln(1-z) - (1+z^2)/(1-z) ln z + 3 + 2z - (9/2 + pi^2/3) delta
    f = lambda zz: zz ** (N - 1)
    D0 = mp.quad(lambda zz: (f(zz) - 1) / (1 - zz), [0, 1])
    D1 = mp.quad(lambda zz: (f(zz) - 1) * mp.log(1 - zz) / (1 - zz), [0, 1])
    reg = mp.quad(lambda zz: f(zz) * (-(1 + zz) * mp.log(1 - zz) - (1 + zz ** 2) / (1 - zz) * mp.log(zz) + 3 + 2 * zz), [0, 1])
    return 2 * D1 - mp.mpf(3) / 2 * D0 + reg - (mp.mpf(9) / 2 + mp.pi ** 2 / 3)
def mom_C2q_wb(N):
    # whole-bracket plus form: [ (1+z^2)/(1-z) (ln((1-z)/z) - 3/4) + (9+5z)/4 ]_+
    g = lambda zz: (1 + zz ** 2) / (1 - zz) * (mp.log((1 - zz) / zz) - mp.mpf(3) / 4) + (9 + 5 * zz) / 4
    return mp.quad(lambda zz: g(zz) * (zz ** (N - 1) - 1), [0, 1])
def mom_C2g(N):
    return mp.quad(lambda zz: zz ** (N - 1) * ((zz ** 2 + (1 - zz) ** 2) * mp.log((1 - zz) / zz) - 8 * zz ** 2 + 8 * zz - 1), [0, 1])
worst = 0
rows = []
for N in range(1, 9):
    a, b, c, d = mom_C2q(N), C2qN_vf(N), mom_C2q_wb(N), mom_C2g(N)
    e = C2gN_vf(N)
    worst = max(worst, abs(a - b), abs(c - b), abs(d - e))
    rows.append((N, mp.nstr(b, 12), mp.nstr(e, 12)))
print('max |x-space moments - VF-DIS-8| over N=1..8 (C2q, whole-bracket C2q, C2g):', mp.nstr(worst, 5))
for r in rows:
    print('   N=%d  C2q/CF=%s  C2g/TF=%s' % r)
CLq1 = mp.quad(lambda zz: 2 * zz, [0, 1])
print('Adler: C^q_{2,1} =', mp.nstr(mom_C2q(1), 10), ';  Bjorken: C^q_{1,1} = C^q_{2,1} - C^q_{L,1} =', mp.nstr(mom_C2q(1) - CLq1, 10), '(in units of C_F; expect -1)')

print('=' * 78)
print('F. Intermediate algebra printed in ex:disall-nlo and ex:disall-gluon')
# quark channel: projected integrand (F_2 projection of the Dirac traces) in terms of y, z
integrand_q = sp.simplify(proj2_q.subs(kin))
hand_q = 8 * ((1 - eps) * y ** 2 - 2 * y * (z - eps * (1 - z)) + 1 + z ** 2 - eps * (1 - z) ** 2) / (y * (1 - z)) + 16 * (3 - 2 * eps) * z * (1 - y)
print('quark F_2-projected integrand = 8[(1-e)y^2-2y(z-e(1-z))+1+z^2-e(1-z)^2]/[y(1-z)] + 16(3-2e)z(1-y):',
      sp.simplify(integrand_q - hand_q) == 0)
I0 = sp.gamma(1 - eps) ** 2 / sp.gamma(2 - 2 * eps)
Iq = yint(hand_q)
print('(1-z) * int dy [y(1-y)]^-e (...)/(8 I0) =', sp.simplify(sp.gammasimp((1 - z) * Iq / (8 * I0))),
      ' expect -(1+z^2)/e + (7-2z)/2 - e/2 :', sp.simplify(sp.gammasimp((1 - z) * Iq / (8 * I0)) - (-(1 + z ** 2) / eps + (7 - 2 * z) / 2 - eps / 2)) == 0)
print('Beta-function values: I_1/I_0 =', sp.simplify(sp.gammasimp(yint(y) / I0)), ';  I_{-1}/I_0 =', sp.simplify(sp.gammasimp(yint(1 / y) / I0)))
integrand_L = sp.simplify(projL_q.subs(kin))
print('quark F_L-projected integrand =', sp.factor(integrand_L))
# gluon channel
integrand_g = sp.simplify(proj2_g.subs(kin_g))
Ig = yint(integrand_g)
Pz = z ** 2 + (1 - z) ** 2
expect_g = -16 / eps * I0 * (Pz - 3 * eps + 4 * eps ** 2 - 2 * eps ** 3) / (1 - eps)
print('gluon: int dy [y(1-y)]^-e (F_2 projection) = -(16/e) I0 (P - 3e + 4e^2 - 2e^3)/(1-e) :',
      sp.simplify(sp.gammasimp(Ig / expect_g)) == 1)
print('gluon F_2-projected integrand (y-dependence) =', sp.factor(integrand_g))
