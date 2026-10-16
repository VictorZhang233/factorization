# One-loop soft factor S~(b_T; y_A, y_B) with non-light-like Wilson lines (Collins 2011 regulator).
# Binding conventions of CONTEXT.md; light-front v.w = v+ w- + v- w+ - vT.wT.
#   time-like  lines: nA = (1,  e^{-2yA}, 0_T),  nB = ( e^{2yB}, 1, 0_T)
#   space-like lines: nA = (1, -e^{-2yA}, 0_T),  nB = (-e^{2yB}, 1, 0_T)   [Collins 2011; Aybat-Rogers 2011 eq.(8)]
# Real gluon (on-shell, l = (lT e^y/sqrt2, lT e^-y/sqrt2, lT)), colour-singlet eikonal current
#   J^mu = g t^a [ nA^mu/(nA.l) - nB^mu/(nB.l) ],   sum_pol -> -g_{mu nu}:
#   -J.J/(g^2 C_F) = 2 nA.nB/((nA.l)(nB.l)) - nA^2/(nA.l)^2 - nB^2/(nB.l)^2
# Phase space: int d^Dl/(2pi)^{D-1} delta+(l^2) = int d^{D-2}lT/(2(2pi)^{D-1}) int dy.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
mp.mp.dps = 30
ok = True

# ---------------------------------------------------------------------------------------
# 1. rapidity integrals:  R(Y) = int dy lT^2 [-J.J/(g^2 C_F)]
def integrands(y, yA, yB, sig):
    s = 1 if sig == 't' else -1
    lT = mp.mpf(1)
    lp, lm = lT * mp.e**y / mp.sqrt(2), lT * mp.e**(-y) / mp.sqrt(2)
    nAp, nAm = 1, s * mp.e**(-2 * yA)
    nBp, nBm = s * mp.e**(2 * yB), 1
    nAl = nAp * lm + nAm * lp
    nBl = nBp * lm + nBm * lp
    nAnB = nAp * nBm + nAm * nBp
    nA2, nB2 = 2 * nAp * nAm, 2 * nBp * nBm
    cross = lT**2 * 2 * nAnB / (nAl * nBl)
    selfA = -lT**2 * nA2 / nAl**2
    selfB = -lT**2 * nB2 / nBl**2
    return cross, selfA, selfB

print('1. rapidity integrals (Y = yA - yB)')
for (yA, yB) in [(mp.mpf('1.3'), mp.mpf('-0.4')), (mp.mpf('4.0'), mp.mpf('1.5')), (mp.mpf('0.2'), mp.mpf('0.05'))]:
    Y = yA - yB
    # time-like: everything finite
    c = mp.quad(lambda y: integrands(y, yA, yB, 't')[0], [-mp.inf, yB, yA, mp.inf])
    sA = mp.quad(lambda y: integrands(y, yA, yB, 't')[1], [-mp.inf, yA, mp.inf])
    sB = mp.quad(lambda y: integrands(y, yA, yB, 't')[2], [-mp.inf, yB, mp.inf])
    print('   time-like  Y=%s : cross=%s (4Y cothY=%s)  selfA=%s selfB=%s (each -2)' % (
        mp.nstr(Y, 4), mp.nstr(c, 15), mp.nstr(4 * Y / mp.tanh(Y), 15), mp.nstr(sA, 12), mp.nstr(sB, 12)))
    ok &= abs(c - 4 * Y / mp.tanh(Y)) < mp.mpf('1e-20') and abs(sA + 2) < mp.mpf('1e-20') and abs(sB + 2) < mp.mpf('1e-20')
    # space-like: cross term has simple poles at y = yA, y = yB -> principal value.
    # exact: cross = -2 coshY/(sinh(y-yA) sinh(y-yB)) = (2 coshY/sinhY)[coth(y-yB) - coth(y-yA)]
    #        PV int_{-L}^{L} coth(y-c) dy = ln(sinh(L-c)/sinh(L+c)) -> -2c   =>  PV int cross = 4 Y coth Y
    f = lambda y: integrands(y, yA, yB, 's')[0]
    ident = max(abs(f(yy) - 2 * mp.cosh(Y) / mp.sinh(Y) * (mp.coth(yy - yB) - mp.coth(yy - yA))) for yy in [yA + mp.mpf('0.31'), yB - mp.mpf('0.7'), (yA + yB) / 2 + mp.mpf('0.013')])
    Lc = mp.mpf(70)
    pvs = []
    for eta in [mp.mpf('1e-3'), mp.mpf('1e-4'), mp.mpf('1e-5')]:
        pv = (mp.quad(f, [-Lc, yB - 3, yB - eta]) + mp.quad(f, [yB + eta, yA - eta]) + mp.quad(f, [yA + eta, yA + 3, Lc]))
        pvs.append(pv)
    print('   space-like Y=%s : identity residual %s ; PV cross (eta=1e-3,1e-4,1e-5) = %s, %s, %s  (4Y cothY=%s)' % (
        mp.nstr(Y, 4), mp.nstr(ident, 3), mp.nstr(pvs[0], 12), mp.nstr(pvs[1], 12), mp.nstr(pvs[2], 12), mp.nstr(4 * Y / mp.tanh(Y), 12)))
    print('      (space-like self-energy terms ~ 1/sinh^2(y-yA): non-integrable at the pole = Wilson-line length divergence;'
          ' they cancel in the TMD combination and are omitted, sigma = 0)')
    # excised integral = PV - 2*eta*(sum of regular parts at the poles) + O(eta^3): Richardson-extrapolate the linear term
    pv = (10 * pvs[2] - pvs[1]) / 9
    print('      Richardson-extrapolated PV = %s   difference to 4Y cothY = %s' % (mp.nstr(pv, 15), mp.nstr(pv - 4 * Y / mp.tanh(Y), 3)))
    ok &= abs(pv - 4 * Y / mp.tanh(Y)) < mp.mpf('1e-8') and ident < mp.mpf('1e-25')

# ---------------------------------------------------------------------------------------
# 2. b-space soft factor at one loop
#   S~(1)(b) = g^2 C_F mu^{2eps}/(2(2pi)^{3-2eps}) * R(Y) * FT[1/lT^2],  R = 4(Y cothY - sigma),
#   sigma = 1 (time-like, self-energies included), 0 (space-like, self-energies omitted: they cancel in the TMD)
#   c_S FT[1/k^2] = (alpha_s C_F/2pi) S_eps A(eps),  c_S = g^2 mu^{2eps} C_F/(2pi)^{3-2eps}
#   => S~(1) = (alpha_s C_F/pi) S_eps (Y cothY - sigma) A(eps)
eps, Lb = sp.symbols('epsilon L_b')
gE = sp.EulerGamma
Aeps = {'binding': -sp.exp(eps * Lb) * sp.exp(-gE * eps) * sp.gamma(1 - eps) / eps,      # derived in DERIVATION.md Sec.3.7
        'Collins': -sp.exp(eps * Lb) * sp.exp(-gE * eps) * sp.gamma(1 - eps) / eps * sp.gamma(1 - eps) * sp.exp(-gE * eps)}
# (Collins: g0^2 = g^2 mu^{2eps} Gamma(1-eps)/(4pi)^eps instead of e^{eps gE}/(4pi)^eps -> extra factor e^{-gE eps} Gamma(1-eps))
Ys, sig = sp.symbols('Y sigma', positive=True)
for name, A in Aeps.items():
    Aser = sp.series(A, eps, 0, 2).removeO()
    S1 = sp.expand((Ys * sp.coth(Ys) - sig) * Aser)          # units alpha_s C_F/pi, times S_eps
    print('2. %-8s  A(eps) = %s' % (name, sp.collect(sp.expand(Aser), eps)))
    print('   S~(1)_bare/(alpha_s C_F/pi S_eps) = (Y cothY - sigma) * [%s]' % sp.collect(sp.expand(Aser), eps))
    pole = sp.expand(S1).coeff(eps, -1)
    fin = sp.expand(S1).coeff(eps, 0)
    print('   pole: %s / eps  ;  MSbar-renormalized S~(1) = (alpha_s C_F/pi) * [%s]' % (pole, sp.factor(fin)))
    ok &= sp.simplify(fin + (Ys * sp.coth(Ys) - sig) * Lb) == 0

# ---------------------------------------------------------------------------------------
# 3. Collins-Soper kernel from the soft factor alone (Collins 2011 eq. for K~ via soft factors):
#   K~ = (1/2) d/dy_n ln[ S~(b; y_n, -inf) / S~(b; +inf, y_n) ]   (y_A -> +inf, y_B -> -inf; Y coth Y -> |Y|)
yA, yB, yn = sp.symbols('y_A y_B y_n', real=True)
Sren = lambda Y: -(Y - sig) * Lb          # renormalized one-loop, large |Y|, units alpha_s C_F/pi
Kt = sp.simplify(sp.Rational(1, 2) * sp.diff(Sren(yn - yB) - Sren(yA - yn), yn))
print('3. K~ from soft factor = (alpha_s C_F/pi) * (%s)   [expect -L_b, L_b = ln(mu^2 b^2/b0^2)]' % Kt)
ok &= sp.simplify(Kt + Lb) == 0
gK = sp.diff(-Kt, Lb) * 2          # d K~/d ln mu = -gamma_K ; dL_b/dln mu = 2
print('   gamma_K = -dK~/dln mu = (alpha_s C_F/pi) * %s  => gamma_K = 2 C_F alpha_s/pi' % gK)
ok &= gK == 2

# ---------------------------------------------------------------------------------------
# 4. combination entering the Collins TMD (momentum space, per unit c_S/kT^2):
#   (1/2)[S(yA,yn) - S(yA,yB) - S(yn,yB)],  S(Y) -> 2 (Y cothY - sigma) c_S/kT^2,  large rapidity gaps
comb = sp.expand(sp.Rational(1, 2) * 2 * (((yA - yn) - sig) - ((yA - yB) - sig) - ((yn - yB) - sig)))
print('4. soft combination = (c_S/kT^2) * (%s)   [y_A drops out; -2 y_n + 2 y_B + sigma]' % comb)
ok &= sp.simplify(comb - (-2 * yn + 2 * yB + sig)) == 0
print('soft factor checks:', 'PASS' if ok else 'FAIL')
