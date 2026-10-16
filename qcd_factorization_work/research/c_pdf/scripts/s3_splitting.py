"""
s3_splitting.py -- item (3): LO splitting functions, sum rules, Mellin moments, anomalous dimensions.

Part A: D-dimensional real-emission kernels from the operator definitions (light-cone gauge A^+ = 0,
        massless on-shell target, one real parton in the final state).  Normalisation:
            f_{i/j}^{real}(xi) = g^2/(2pi)^{D-1} int d^{D-2}l_T  Phat_{ij}(xi; eps) / l_T^2
        so that in D = 4:  f = (alpha_s/2pi) Phat(xi) int dl_T^2/l_T^2.
Part B: delta(1-z) terms from quark-number and momentum conservation.
Part C: Mellin moments gamma_ij(N) = int_0^1 z^{N-1} P_ij(z) dz (symbolic + numeric, non-integer N).
Part D: conversions to other conventions.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
import mpmath as mp
from lorentz_engine import Vec, Kin, Term, tr_sum, contract_sum, mul, V, I, D

results = []


def report(name, ok, detail=''):
    results.append((name, bool(ok)))
    print('%-80s %s %s' % (name, 'PASS' if ok else 'FAIL', detail))


xi, pp, LT2 = sp.symbols('xi p^+ L_T2', positive=True)
eps = sp.Symbol('epsilon')
CF, CA, TF, nf = sp.symbols('C_F C_A T_F n_f', positive=True)
z = sp.Symbol('z', positive=True)

kin = Kin({('p', 'p'): 0, ('n', 'n'): 0, ('p', 'n'): pp, ('p', 'lT'): 0, ('n', 'lT'): 0, ('lT', 'lT'): -LT2})
P, N, LTv = Vec.b('p'), Vec.b('n'), Vec.b('lT')
L = P * (1 - xi) + N * (LT2 / (2 * (1 - xi) * pp)) + LTv      # real massless parton
K = P - L                                                      # parton entering the operator
k2 = sp.simplify(kin.dot(K, K))
nk = kin.dot(N, K)
nl = kin.dot(N, L)
report('kinematics: l^2 = 0, k^2 = -lT^2/(1-xi), n.k = xi p^+', sp.simplify(kin.dot(L, L)) == 0 and
       sp.simplify(k2 + LT2 / (1 - xi)) == 0 and sp.simplify(nk - xi * pp) == 0)


def dLC(a, b, vec, nv):
    """light-cone-gauge numerator d^{ab}(v) = -g^{ab} + (v^a n^b + n^a v^b)/n.v  as Terms."""
    return [Term(-1, [], [(I(a), I(b))]),
            Term(1 / nv, [], [(('v', vec), I(a)), (V('n'), I(b))]),
            Term(1 / nv, [], [(V('n'), I(a)), (('v', vec), I(b))])]


def minus_gT(a, b):
    """-g_T^{ab} = -g^{ab} + (p^a n^b + n^a p^b)/p.n  (sum over physical transverse polarisations)."""
    return [Term(-1, [], [(I(a), I(b))]),
            Term(1 / pp, [], [(V('p'), I(a)), (V('n'), I(b))]),
            Term(1 / pp, [], [(V('n'), I(a)), (V('p'), I(b))])]


def to_eps(e):
    return sp.simplify(sp.factor(e.subs(D, 4 - 2 * eps)))


nslash = [Term(1, [V('n')])]
# ------------------------------------------------------------------ q <- q
amp = [Term(1 / k2, [('v', K), I('mu')])]
cnj = [Term(1 / k2, [I('nu'), ('v', K)])]
S = tr_sum(mul([Term(sp.Rational(1, 2), [V('p')])], cnj, nslash, amp, dLC('mu', 'nu', L, nl)), kin)
Phat_qq = to_eps(S / (4 * (1 - xi) * pp) * LT2)
ref_qq = (1 + xi ** 2) / (1 - xi) - eps * (1 - xi)
report('Phat_qq/C_F = (1+z^2)/(1-z) - eps(1-z)', sp.simplify(Phat_qq - ref_qq) == 0, str(sp.factor(Phat_qq)))

# ------------------------------------------------------------------ g <- q
#   M^j = i g t^a X^{j beta} ubar(l) gamma_beta u(p)/k^2,  X^{mu beta} = (n.k g^{mu alpha} - k^mu n^alpha) d_alpha^beta(k)
X_amp = [Term(nk, [], [(I('j'), I('al'))]), Term(-1, [], [(('v', K), I('j')), (V('n'), I('al'))])]
X_cnj = [Term(nk, [], [(I('jp'), I('alp'))]), Term(-1, [], [(('v', K), I('jp')), (V('n'), I('alp'))])]
dk_amp = dLC('al', 'be', K, nk)
dk_cnj = dLC('alp', 'bep', K, nk)
spin = [Term(sp.Rational(1, 2), [V('lTdummy')])] if False else None
# Dirac: (1/2) Tr[lslash gamma^be pslash gamma^bep]
dirac = [Term(sp.Rational(1, 2), [('v', L), I('be'), V('p'), I('bep')])]
T_gq = tr_sum(mul(dirac, X_amp, dk_amp, X_cnj, dk_cnj, minus_gT('j', 'jp')), kin)
# f = (1/(xi p^+)) * 1/(2(1-xi)p^+) * g^2 C_F * T/(k^2)^2   per g^2/(2pi)^{D-1} d^{D-2}lT
Phat_gq = to_eps(T_gq / (k2 ** 2) / (xi * pp) / (2 * (1 - xi) * pp) * LT2)
ref_gq = (1 + (1 - xi) ** 2) / xi - eps * xi
report('Phat_gq/C_F = (1+(1-z)^2)/z - eps z', sp.simplify(Phat_gq - ref_gq) == 0, str(sp.factor(Phat_gq)))

# ------------------------------------------------------------------ q <- g
#   M = -g t^a kslash gamma^alpha v(l) eps_alpha(p)/k^2 ; sum_s v vbar = lslash ; <eps eps*> = -g_T/(D-2)
dirac_qg = [Term(1, [I('alp'), ('v', K), V('n'), ('v', K), I('al'), ('v', L)])]
T_qg = tr_sum(mul(dirac_qg, minus_gT('al', 'alp')), kin) / (D - 2)
Phat_qg = to_eps(T_qg / (k2 ** 2) / 2 / (2 * (1 - xi) * pp) * LT2)
ref_qg = 1 - 2 * xi * (1 - xi) / (1 - eps)
report('Phat_qg/T_F = 1 - 2z(1-z)/(1-eps)', sp.simplify(Phat_qg - ref_qg) == 0, str(sp.factor(Phat_qg)))

# ------------------------------------------------------------------ g <- g
#   triple-gluon vertex, all momenta incoming: (p,al), (-l,be), (-k,ga)
def V3(a, b, c, q1, q2, q3):
    return [Term(1, [], [(I(a), I(b)), (('v', q1 - q2), I(c))]),
            Term(1, [], [(I(b), I(c)), (('v', q2 - q3), I(a))]),
            Term(1, [], [(I(c), I(a)), (('v', q3 - q1), I(b))])]


Vamp = V3('al', 'be', 'ga', P, -L, -K)
Vcnj = V3('alp', 'bep', 'gap', P, -L, -K)
Xg_amp = [Term(nk, [], [(I('j'), I('de'))]), Term(-1, [], [(('v', K), I('j')), (V('n'), I('de'))])]
Xg_cnj = [Term(nk, [], [(I('jp'), I('dep'))]), Term(-1, [], [(('v', K), I('jp')), (V('n'), I('dep'))])]
prop_amp = dLC('de', 'ga', K, nk)
prop_cnj = dLC('dep', 'gap', K, nk)
T_gg = contract_sum(mul(Vamp, Vcnj, minus_gT('al', 'alp'), dLC('be', 'bep', L, nl), Xg_amp, prop_amp, Xg_cnj, prop_cnj,
                        minus_gT('j', 'jp')), kin) / (D - 2)
Phat_gg = to_eps(T_gg / (k2 ** 2) / (xi * pp) / (2 * (1 - xi) * pp) * LT2)
ref_gg = 2 * (xi / (1 - xi) + (1 - xi) / xi + xi * (1 - xi))
report('Phat_gg/C_A = 2[z/(1-z) + (1-z)/z + z(1-z)]  (no eps dependence)', sp.simplify(Phat_gg - ref_gg) == 0, str(sp.factor(Phat_gg)))
# gauge-invariance test of the cut: replace target polarisation sum by -g (+ ghosts would be needed): skip.

# ------------------------------------------------------------------ Part B: delta terms from sum rules
def plus_moment(f_reg_times_z_pow, f_sing_coef, Nval):
    pass


Pqq_reg = CF * (1 + z ** 2)          # times [1/(1-z)]_+
# int_0^1 dz (1+z^2)/(1-z)_+  =  int (1+z^2-2)/(1-z)
a_qq = -sp.integrate(sp.cancel((1 + z ** 2 - 2) / (1 - z)), (z, 0, 1)) * CF
report('quark number: delta coefficient of P_qq = 3/2 C_F', sp.simplify(a_qq - sp.Rational(3, 2) * CF) == 0, str(a_qq))
P_qg = TF * (z ** 2 + (1 - z) ** 2)
P_gq = CF * (1 + (1 - z) ** 2) / z
# momentum (gluon column): int z [P_gg + 2 n_f P_qg] = 0
reg_gg_moment2 = 2 * CA * (sp.integrate(sp.cancel((z * z - 1) / (1 - z)), (z, 0, 1)) +
                           sp.integrate(z * ((1 - z) / z + z * (1 - z)), (z, 0, 1)))
b_gg = -(reg_gg_moment2 + 2 * nf * sp.integrate(z * P_qg, (z, 0, 1)))
report('momentum: delta coefficient of P_gg = (11 C_A - 4 n_f T_F)/6 = beta_0/2', sp.simplify(b_gg - (11 * CA - 4 * nf * TF) / 6) == 0, str(sp.expand(b_gg)))
# momentum (quark column) is a consistency check: int z [P_qq + P_gq] = 0
mom_q = CF * sp.integrate(sp.cancel((z * (1 + z ** 2) - 2) / (1 - z)), (z, 0, 1)) + sp.Rational(3, 2) * CF + sp.integrate(z * P_gq, (z, 0, 1))
report('momentum (quark column): int z [P_qq + P_gq] = 0  (independent check)', sp.simplify(mom_q) == 0)
# antiquark relations P_qbar qbar = P_qq etc. are charge conjugation; P_{q qbar} = 0 at LO (no graph)

# ------------------------------------------------------------------ Part C: Mellin moments
Nn = sp.Symbol('N', positive=True)


def S1(n):
    return sp.harmonic(n)


def gam_closed(Nv):
    return {
        'qq': CF * (sp.Rational(3, 2) + sp.Rational(1, 1) / (Nv * (Nv + 1)) - 2 * S1(Nv)),
        'qg': TF * (Nv ** 2 + Nv + 2) / (Nv * (Nv + 1) * (Nv + 2)),
        'gq': CF * (Nv ** 2 + Nv + 2) / ((Nv - 1) * Nv * (Nv + 1)),
        'gg': 2 * CA * (sp.Rational(1, 1) / (Nv * (Nv - 1)) + sp.Rational(1, 1) / ((Nv + 1) * (Nv + 2)) - S1(Nv))
              + (11 * CA - 4 * nf * TF) / 6,
    }


def gam_direct(Nv):
    """integrate the distributions against z^{N-1} (integer N)."""
    zN = z ** (Nv - 1)
    qq = CF * sp.integrate(sp.cancel((zN * (1 + z ** 2) - 2) / (1 - z)), (z, 0, 1)) + sp.Rational(3, 2) * CF
    qg = sp.integrate(zN * P_qg, (z, 0, 1))
    gq = sp.integrate(sp.expand(zN * P_gq), (z, 0, 1))
    gg = 2 * CA * (sp.integrate(sp.cancel((zN * z - 1) / (1 - z)), (z, 0, 1)) +
                   sp.integrate(sp.expand(zN * ((1 - z) / z + z * (1 - z))), (z, 0, 1))) + (11 * CA - 4 * nf * TF) / 6
    return {'qq': qq, 'qg': qg, 'gq': gq, 'gg': gg}


okM = True
for Nv in range(2, 13):
    gd, gc = gam_direct(Nv), gam_closed(sp.Integer(Nv))
    for key in gd:
        okM &= sp.simplify(gd[key] - gc[key]) == 0
gd1 = gam_direct(1)
okM &= sp.simplify(gd1['qq'] - gam_closed(sp.Integer(1))['qq']) == 0 and sp.simplify(gd1['qg'] - gam_closed(sp.Integer(1))['qg']) == 0
report('Mellin moments (N=2..12; qq,qg also N=1) equal the closed forms', okM)
g1 = gam_closed(sp.Integer(1))
g2 = gam_closed(sp.Integer(2))
report('gamma_qq(1) = 0 (quark number)', sp.simplify(g1['qq']) == 0)
report('gamma_qq(2)+gamma_gq(2) = 0 and 2 n_f gamma_qg(2) + gamma_gg(2) = 0',
       sp.simplify(g2['qq'] + g2['gq']) == 0 and sp.simplify(2 * nf * g2['qg'] + g2['gg']) == 0)
print('   N=2 matrix [[qq, 2nf qg],[gq, gg]] =', sp.Matrix([[g2['qq'], 2 * nf * g2['qg']], [g2['gq'], g2['gg']]]))

# symbolic N: int_0^1 (z^{N-1}-1)/(1-z) dz = sum_{k>=0} [1/(k+N) - 1/(k+1)] = -(psi(N) + gamma_E)
#   (expand 1/(1-z) = sum z^k; digamma series, DLMF sec. 5.7).  Checked numerically at complex N.
okS = True
mp.mp.dps = 30
for Nc in [mp.mpf('0.6'), mp.mpf('2.3'), mp.mpc('1.7', '2.2'), mp.mpc('4.1', '-0.8')]:
    lhs = mp.quad(lambda t: (t ** (Nc - 1) - 1) / (1 - t), [0, mp.mpf('1e-8'), 0.5, 1])
    ser = mp.nsum(lambda kk: 1 / (kk + Nc) - 1 / (kk + 1), [0, mp.inf])
    okS &= abs(lhs - ser) < 1e-15 and abs(ser + mp.digamma(Nc) + mp.euler) < 1e-20
report('int_0^1 (z^{N-1}-1)/(1-z) dz = -(psi(N)+gamma_E), Re N>0 (numeric, complex N)', okS)

# non-integer N: numerical moments vs closed forms with S_1(N) = psi(N+1) + gamma_E (Carlson continuation)
mp.mp.dps = 30
def S1c(Nv):
    return mp.digamma(Nv + 1) + mp.euler


def num_moments(Nv, CFv=mp.mpf(4) / 3, CAv=mp.mpf(3), TFv=mp.mpf(1) / 2, nfv=5):
    qq = CFv * mp.quad(lambda t: (t ** (Nv - 1) * (1 + t * t) - 2) / (1 - t), [0, mp.mpf('1e-6'), 1]) + 1.5 * CFv
    qg = TFv * mp.quad(lambda t: t ** (Nv - 1) * (t * t + (1 - t) ** 2), [0, mp.mpf('1e-6'), 1])
    gq = CFv * mp.quad(lambda t: t ** (Nv - 1) * (1 + (1 - t) ** 2) / t, [0, mp.mpf('1e-6'), 1])
    gg = 2 * CAv * (mp.quad(lambda t: (t ** Nv - 1) / (1 - t), [0, mp.mpf('1e-6'), 1]) + mp.quad(lambda t: t ** (Nv - 2) * (1 - t) + t ** Nv * (1 - t), [0, mp.mpf('1e-6'), 1])) \
         + (11 * CAv - 4 * nfv * TFv) / 6
    return qq, qg, gq, gg


def cl_moments(Nv, CFv=mp.mpf(4) / 3, CAv=mp.mpf(3), TFv=mp.mpf(1) / 2, nfv=5):
    return (CFv * (1.5 + 1 / (Nv * (Nv + 1)) - 2 * S1c(Nv)),
            TFv * (Nv ** 2 + Nv + 2) / (Nv * (Nv + 1) * (Nv + 2)),
            CFv * (Nv ** 2 + Nv + 2) / ((Nv - 1) * Nv * (Nv + 1)),
            2 * CAv * (1 / (Nv * (Nv - 1)) + 1 / ((Nv + 1) * (Nv + 2)) - S1c(Nv)) + (11 * CAv - 4 * nfv * TFv) / 6)


okNI = True
for Nv in [mp.mpf('1.37'), mp.mpf('2.5'), mp.mpf('3.91'), mp.mpf('7.25')]:
    a, b = num_moments(Nv), cl_moments(Nv)
    okNI &= all(abs(a[i] - b[i]) < mp.mpf('1e-10') * (1 + abs(b[i])) for i in range(4))
report('non-integer N (1.37, 2.5, 3.91, 7.25): moments = closed forms with S_1 = psi(N+1)+gamma_E', okNI)

# ------------------------------------------------------------------ Part D: conventions
# (i) ESW form: gamma_qq = C_F[-1/2 + 1/(N(N+1)) - 2 sum_{k=2}^N 1/k]
okE = all(sp.simplify(gam_closed(sp.Integer(n))['qq'] - CF * (-sp.Rational(1, 2) + sp.Rational(1, n * (n + 1)) - 2 * sum(sp.Rational(1, k) for k in range(2, n + 1)))) == 0 for n in range(1, 15))
report('equivalent form C_F[-1/2 + 1/(N(N+1)) - 2 sum_{k=2}^N 1/k]', okE)
# (ii) MVV: P = sum a_s^{n+1} P^(n), a_s = alpha_s/(4pi), gamma^(n)(N) = - int x^{N-1} P^(n)  => gamma^(0) = -2 gamma
okV = all(sp.simplify(-2 * gam_closed(sp.Integer(n))['qq'] - CF * (4 * S1(n) - 3 - sp.Rational(2, n * (n + 1)))) == 0 for n in range(1, 15))
report('MVV convention: gamma^(0)_ns(N) = -2 gamma_qq(N) = C_F[4S_1 - 3 - 2/(N(N+1))]', okV)
# (iii) operator convention mu dO/dmu = -gamma_O O:  gamma_O = -(alpha_s/pi) gamma_N
#       = (alpha_s/2pi) C_F [1 - 2/(n(n+1)) + 4 sum_{j=2}^n 1/j]   (Gross-Wilczek form)
okG = all(sp.simplify(-2 * gam_closed(sp.Integer(n))['qq'] - CF * (1 - sp.Rational(2, n * (n + 1)) + 4 * sum(sp.Rational(1, j) for j in range(2, n + 1)))) == 0 for n in range(1, 15))
report('GW form: -2 gamma_qq(n) = C_F[1 - 2/(n(n+1)) + 4 sum_{j=2}^n 1/j]', okG)
# eigenvalues of the N=2 singlet matrix (rows i, columns j): 0 and -(4C_F + 2 n_f T_F)/3
Mat = sp.Matrix([[g2['qq'], 2 * nf * g2['qg']], [g2['gq'], g2['gg']]])
ev = Mat.eigenvals()
report('N=2 singlet eigenvalues {0, -(4C_F+2n_fT_F)/3}; asymptotic <x>_q = 3n_f/(16+3n_f) for SU(3)',
       set(sp.simplify(e) for e in ev) == {0, sp.simplify(-(4 * CF + 2 * nf * TF) / 3)})
vec0 = Mat.nullspace()[0]
frac_q = sp.simplify((vec0[0] / (vec0[0] + vec0[1])).subs({CF: sp.Rational(4, 3), TF: sp.Rational(1, 2)}))
report('   asymptotic quark momentum fraction', sp.simplify(frac_q - 3 * nf / (16 + 3 * nf)) == 0, str(frac_q))
# large-N behaviour (cusp): gamma_qq ~ -2 C_F (ln N + gamma_E) + 3/2 C_F ; gamma_gg ~ -2 C_A (ln N + gamma_E) + beta0/2
Nb = mp.mpf(10) ** 6
qq_l = cl_moments(Nb)[0]; gg_l = cl_moments(Nb)[3]
CFv, CAv = mp.mpf(4) / 3, mp.mpf(3)
okL = abs(qq_l - (-2 * CFv * (mp.log(Nb) + mp.euler) + 1.5 * CFv)) < 1e-5 and \
      abs(gg_l - (-2 * CAv * (mp.log(Nb) + mp.euler) + (11 * CAv - 10) / 6)) < 1e-5
report('large-N: gamma_qq -> -2C_F(lnN+gamma_E)+3C_F/2, gamma_gg -> -2C_A(lnN+gamma_E)+beta_0/2', okL)

print()
print('SUMMARY s3: %d/%d PASS' % (sum(1 for _, o in results if o), len(results)))
