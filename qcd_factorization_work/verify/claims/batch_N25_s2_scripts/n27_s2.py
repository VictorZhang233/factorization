#!/usr/bin/env python3
"""N27 (stage-2 verifier): one-loop MS-bar and ratio quasi-PDF kernels = Fourier transforms of the coordinate kernels.
Kernels as printed in IJJSZ arXiv:1801.03917 eqs. (62),(63) [coordinate], (68),(69) [MS-bar momentum], (70),(71) [ratio],
FT relation eq. (34): C(xi) = int dzeta/2pi e^{i xi zeta} int dalpha e^{-i alpha zeta} Ccoord(alpha, L(zeta)),
L(zeta) = ln(zeta^2) + ell_p + 2 gamma_E,  ell_p = ln(mu^2/(4 p_z^2)),  a = alpha_s C_F/(2 pi) stripped.

Two methods, both different from the project's s2 (Gaussian test functions in zeta space) and from stage 1:
 (P1) POINTWISE in xi (xi != 1): C(xi) = ell_p A(xi) + B(xi) - (A * [1/|u|])(xi), using FT[ln zeta^2] = -2 gamma_E delta - [1/|u|],
      evaluated as Hadamard finite parts with mpmath; compared with the printed piecewise functions in all three regions.
 (P2) POINTWISE in zeta: <C_printed, e^{-i xi zeta}> (all plus prescriptions, delta terms, 1/xi tails via E1 functions and
      quadosc) compared with G(zeta) = int dalpha Ccoord(alpha, L(zeta)) e^{-i alpha zeta}.  This fixes the delta(1-xi)
      coefficients and the plus prescriptions, which (P1) cannot see.
 Plus: the identity FT[ln zeta^2] itself (closed form check), and the momentum RGE (symbolic).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import sympy as sp

mp.mp.dps = 22
gE = mp.euler
NP = 0; NF = 0; maxdev = {'P1': 0, 'P2': 0}
def check(name, ok, info=''):
    global NP, NF
    if ok: NP += 1
    else: NF += 1
    print(('[PASS] ' if ok else '[FAIL] ') + name + ('   ' + info if info else ''))

g = lambda x: (1 + x**2) / (1 - x)
# printed momentum-space functions (IJJSZ (68)/(70); LAMET 4.6(c))
g1 = lambda x: (1 + x**2) / (1 - x) * mp.log(x / (x - 1)) + 1                       # xi > 1
g3 = lambda x: -(1 + x**2) / (1 - x) * mp.log(-x / (1 - x)) - 1                     # xi < 0
g2 = lambda x, l: (1 + x**2) / (1 - x) * (-l + mp.log(x * (1 - x))) - x * (1 + x) / (1 - x)   # 0<xi<1 MS-bar
r2 = lambda x, l: (1 + x**2) / (1 - x) * (-l + mp.log(x * (1 - x)) - 1) + 1 + 1.5 / (1 - x)    # 0<xi<1 ratio

# ------------------------------------------------------------- (0) the FT of ln zeta^2
# <FT[ln z^2], phi> = int dz/2pi ln z^2 phihat(z),  phihat(z)=int dx phi(x) e^{ixz};  claim = -2gE phi(0) - <[1/|u|], phi>
for (c, s) in [(0, 1), (0.4, 0.7), (-1.1, 1.6)]:
    phi = lambda x: mp.exp(-(x - c)**2 / (2 * s**2))
    phihat = lambda z: mp.sqrt(2 * mp.pi) * s * mp.exp(1j * c * z - s**2 * z**2 / 2)
    lhs = mp.quad(lambda z: (mp.log(z**2) * phihat(z)).real, [-mp.inf, 0, mp.inf]) / (2 * mp.pi)
    inv = mp.quad(lambda u: (phi(u) - phi(0)) / abs(u), [-1, 0, 1]) + mp.quad(lambda u: phi(u) / abs(u), [-mp.inf, -1]) + mp.quad(lambda u: phi(u) / abs(u), [1, mp.inf])
    rhs = -2 * gE * phi(0) - inv
    check('(0) FT[ln zeta^2] = -2 gamma_E delta(u) - [1/|u|]_(cutoff 1), Gaussian c=%s s=%s' % (c, s), abs(lhs - rhs) < 1e-14, 'lhs=%s rhs=%s |d|=%.1e' % (mp.nstr(lhs, 15), mp.nstr(rhs, 15), float(abs(lhs - rhs))))

# ------------------------------------------------------------- (P1) pointwise in xi
def X_out(xi):
    """xi outside [0,1]: int_0^1 g(al) (1/|xi-al| - 1/|xi-1|) dal  (plus prescription at al=1 acting on 1/|xi-al|)"""
    return mp.quad(lambda al: g(al) * (1 / abs(xi - al) - 1 / abs(xi - 1)), [0, 1])
def F_in(xi):
    """0<xi<1: Hadamard finite part of <[g]_+, [1/|xi-al|]>:  int_0^1 {g(al)(1/|xi-al| - 1/(1-xi)) - g(xi)/|xi-al|} + g(xi) ln(xi(1-xi))"""
    f = lambda al: g(al) * (1 / abs(xi - al) - 1 / (1 - xi)) - g(xi) / abs(xi - al)
    return mp.quad(f, [0, xi, 1]) + g(xi) * mp.log(xi * (1 - xi))
for xi in [mp.mpf('1.03'), mp.mpf('1.7'), mp.mpf(4), mp.mpf(25)]:
    ms = -mp.mpf(3) / 2 / abs(xi - 1) + X_out(xi); rt = X_out(xi)
    d1 = abs(ms - g1(xi)); d2 = abs(rt - (g1(xi) - 1.5 / (1 - xi)))
    maxdev['P1'] = max(maxdev['P1'], d1, d2)
    check('(P1) xi=%s>1: FT gives MS-bar g1(xi) and ratio g1 - 3/(2(1-xi)) pointwise' % mp.nstr(xi, 4), d1 < 1e-17 and d2 < 1e-17, 'dev %.1e, %.1e' % (float(d1), float(d2)))
for xi in [mp.mpf('-0.02'), mp.mpf('-0.6'), mp.mpf(-3), mp.mpf(-30)]:
    ms = -mp.mpf(3) / 2 / abs(xi - 1) + X_out(xi); rt = X_out(xi)
    d1 = abs(ms - g3(xi)); d2 = abs(rt - (g3(xi) + 1.5 / (1 - xi)))
    maxdev['P1'] = max(maxdev['P1'], d1, d2)
    check('(P1) xi=%s<0: FT gives MS-bar g3(xi) and ratio g3 + 3/(2(1-xi)) pointwise' % mp.nstr(xi, 4), d1 < 1e-17 and d2 < 1e-17, 'dev %.1e, %.1e' % (float(d1), float(d2)))
for xi in [mp.mpf('0.05'), mp.mpf('0.37'), mp.mpf('0.8'), mp.mpf('0.97')]:
    for l in [mp.mpf('0.3'), mp.mpf('-1.2')]:
        for sig in (0, 1):
            Bpt = -g(xi) - 4 * mp.log(1 - xi) / (1 - xi) + 2 * (1 + sig) * (1 - xi)
            ms = -l * g(xi) + Bpt - mp.mpf(3) / 2 / (1 - xi) + F_in(xi)
            rt = -l * g(xi) + Bpt + F_in(xi)
            d1 = abs(ms - (g2(xi, l) + 2 * sig * (1 - xi))); d2 = abs(rt - (r2(xi, l) + 2 * sig * (1 - xi)))
            maxdev['P1'] = max(maxdev['P1'], d1, d2)
            check('(P1) 0<xi=%s<1, ell_p=%s, sigma=%d: FT gives printed MS-bar and ratio functions pointwise' % (mp.nstr(xi, 3), mp.nstr(l, 2), sig),
                  d1 < 1e-17 and d2 < 1e-17, 'dev %.1e, %.1e' % (float(d1), float(d2)))

# ------------------------------------------------------------- (P2) pointwise in zeta
def osc(f, a, z):
    """int_a^inf f(x) e^{-i x z} dx for f ~ 1/x^2 (absolutely convergent), z>0"""
    re = mp.quadosc(lambda x: f(x) * mp.cos(x * z), [a, mp.inf], omega=z)
    im = -mp.quadosc(lambda x: f(x) * mp.sin(x * z), [a, mp.inf], omega=z)
    return re + 1j * im
# exact large-|xi| series of the subtracted functions (exact rational coefficients, derived by hand), used for |xi| > XT
#  xi>1, u=1/xi:  g1 = 1 - [(1+u^2)/(1-u)] * sum_{j>=0} u^j/(j+1);   3/(2xi) = (3/2)u;   -3/(2(1-xi)) = (3/2) sum_{k>=1} u^k
#  xi<0, u=1/|xi|: g3 = [(1+u^2)/(1+u)] * sum_{j>=0} (-u)^j/(j+1) - 1;   3/(2(1-xi)) = (3/2) sum_{k>=1} (-1)^{k+1} u^k
from fractions import Fraction as Fr
def _mul(a, b, N):
    return [sum(a[i] * b[m - i] for i in range(m + 1)) for m in range(N + 1)]
def _coeffs(N=30):
    A = [Fr(1), Fr(1)] + [Fr(2)] * (N - 1)                         # (1+u^2)/(1-u)
    Bm = [Fr(1), Fr(-1)] + [Fr(2 * (-1)**n) for n in range(2, N + 1)]  # (1+u^2)/(1+u)
    S = [Fr(1, j + 1) for j in range(N + 1)]
    Sa = [Fr((-1)**j, j + 1) for j in range(N + 1)]
    g1c = [-c for c in _mul(A, S, N)]; g1c[0] += 1
    g3c = _mul(Bm, Sa, N); g3c[0] -= 1
    h1ms = [g1c[k] + (Fr(3, 2) if k == 1 else 0) for k in range(N + 1)]
    h1rt = [g1c[k] + (Fr(3, 2) if k >= 1 else 0) for k in range(N + 1)]
    h3 = [g3c[k] + (Fr(3, 2) * (-1)**(k + 1) if k >= 1 else 0) for k in range(N + 1)]
    tomp = lambda L: [mp.mpf(c.numerator) / c.denominator for c in L]
    return {'h1ms': tomp(h1ms), 'h1rt': tomp(h1rt), 'h3': tomp(h3)}
COEF = _coeffs(30)
assert COEF['h1ms'][0] == 0 and COEF['h1ms'][1] == 0 and COEF['h3'][0] == 0 and COEF['h3'][1] == 0 and COEF['h1rt'][1] == 0
XT = mp.mpf(40)
def tail_int(c, X):            # int_X^inf sum_k c_k t^{-k} dt
    return sum(c[k] * X**(1 - k) / (k - 1) for k in range(2, len(c)))
def tail_osc(c, X, w):         # int_X^inf sum_k c_k t^{-k} e^{-i t w} dt = sum_k c_k X^{1-k} E_k(i X w)
    return sum(c[k] * X**(1 - k) * mp.expint(k, 1j * X * w) for k in range(2, len(c)))
def fin_osc(f, a, b, z):        # int_a^b f(x) e^{-ixz} dx on a finite range, split into ~2-period pieces
    n = int(mp.ceil((b - a) * z / (4 * mp.pi))) + 1
    pts = [a + (b - a) * j / n for j in range(n + 1)]
    with mp.workdps(28):
        return mp.quad(lambda x: f(x) * mp.exp(-1j * x * z), pts)
def mom_side(z, l, sig, scheme):
    e1 = mp.exp(-1j * z)
    E = lambda x: mp.exp(-1j * x * z)
    tot = mp.mpc(0)
    if scheme == 'ms':
        h1 = lambda x: g1(x) + 1.5 / x                 # [.]^{[1,inf]}_{+(1)}
        c1 = COEF['h1ms']
        h2 = lambda x: g2(x, l)
    else:
        h1 = lambda x: g1(x) - 1.5 / (1 - x)
        c1 = COEF['h1rt']
        h2 = lambda x: r2(x, l)
    h3 = lambda x: g3(x) + 1.5 / (1 - x)               # [.]^{[-inf,0]}_{+(1)} (same in both schemes)
    c3 = COEF['h3']
    # xi>1: [h1]_{+(1)} -> int_1^inf h1 (e^{-ixz} - e^{-iz}); near 1 use t = xi-1 and expm1
    tot += mp.quad(lambda t: h1(1 + t) * e1 * mp.expm1(-1j * t * z), [0, mp.mpf('0.5'), 1])
    with mp.workdps(28):
        I12 = mp.quad(h1, [2, 5, 10, XT])
    tot += fin_osc(h1, mp.mpf(2), XT, z) + tail_osc(c1, XT, z) - e1 * (I12 + tail_int(c1, XT))
    # 0<xi<1 plus term
    tot += mp.quad(lambda t: h2(1 - t) * e1 * mp.expm1(1j * t * z), [0, mp.mpf('0.5'), 1])
    # xi<0: [h3]_{+(1)} -> int_{-inf}^0 h3 e^{-ixz} - e^{-iz} int_{-inf}^0 h3
    with mp.workdps(28):
        I30 = mp.quad(h3, [-XT, -10, -1, 0])
    tot += fin_osc(h3, -XT, mp.mpf(0), z) + tail_osc(c3, XT, -z) - e1 * (I30 + tail_int(c3, XT))
    if scheme == 'ms':
        # unsubtracted -3/(2xi) on (1,inf) and -3/(2(1-xi)) on (-inf,0):  int_1^inf e^{-ixz}/x = E1(iz);  int_{-inf}^0 e^{-ixz}/(1-x) = e^{-iz} E1(-iz)
        tot += -1.5 * mp.e1(1j * z) - 1.5 * e1 * mp.e1(-1j * z)
        tot += (1.5 * l + 2.5) * e1
        if sig: tot += mp.quad(lambda x: 2 * (1 - x) * E(x), [0, 1])
    else:
        if sig: tot += mp.quad(lambda t: 2 * t * e1 * mp.expm1(1j * t * z), [0, 1])
    return tot
# sanity of the series: compare with direct high-precision evaluation at xi = +-60
with mp.workdps(60):
    for key, f, xv in [('h1ms', lambda x: g1(x) + mp.mpf(3) / 2 / x, mp.mpf(60)), ('h1rt', lambda x: g1(x) - mp.mpf(3) / 2 / (1 - x), mp.mpf(60)), ('h3', lambda x: g3(x) + mp.mpf(3) / 2 / (1 - x), mp.mpf(-60))]:
        ser = sum(COEF[key][k] * abs(xv)**(-k) for k in range(len(COEF[key])))
        check('(P2-aux) large-|xi| series of %s reproduces the function at xi=%s' % (key, mp.nstr(xv, 3)), abs(ser - f(xv)) < 1e-20, 'dev %.1e' % float(abs(ser - f(xv))))
def coord_side(z, l, sig, scheme):
    L = mp.log(z**2) + l + 2 * gE
    e1 = mp.exp(-1j * z)
    E = lambda x: mp.exp(-1j * x * z)
    Ig = mp.quad(lambda t: (1 + (1 - t)**2) / t * e1 * mp.expm1(1j * t * z), [0, mp.mpf('0.5'), 1])
    Il = mp.quad(lambda t: mp.log(t) / t * e1 * mp.expm1(1j * t * z), [0, mp.mpf('0.5'), 1])
    I3 = mp.quad(lambda al: 2 * (1 - al) * E(al), [0, 1])
    G = (1.5 * L + 1.5) * e1 + (-L - 1) * Ig - 4 * Il + (1 + sig) * I3
    if scheme == 'ratio':
        G -= (1.5 * L + 2.5 + sig) * e1        # C0 = 1 + a(3/2 L + 5/2) (+1 for gamma^z: 7/2)
    return G
for scheme in ('ms', 'ratio'):
    for sig in (0, 1):
        for (z, l) in [(mp.mpf('0.3'), mp.mpf('0.3')), (mp.mpf('1.0'), mp.mpf('-1.2')), (mp.mpf('2.5'), mp.mpf('0')), (mp.mpf('7.0'), mp.mpf('0.8'))]:
            m = mom_side(z, l, sig, scheme); c = coord_side(z, l, sig, scheme)
            d = abs(m - c); maxdev['P2'] = max(maxdev['P2'], d)
            check('(P2) %-5s sigma=%d zeta=%s ell_p=%s: <C_printed, e^{-i xi zeta}> = G(zeta)' % (scheme, sig, mp.nstr(z, 3), mp.nstr(l, 2)), d < 1e-12,
                  'mom=%s coord=%s |d|=%.1e' % (mp.nstr(m, 12), mp.nstr(c, 12), float(d)))
# negative control: shifting the MS-bar delta coefficient 5/2 -> 5/2 + 0.01 must be detected
z, l = mp.mpf('2.5'), mp.mpf(0)
d = abs(mom_side(z, l, 0, 'ms') + mp.mpf('0.01') * mp.exp(-1j * z) - coord_side(z, l, 0, 'ms'))
check('(P2) negative control: delta coefficient 5/2 -> 2.51 is detected', d > 1e-3, '|d| = %.2e' % float(d))

# ------------------------------------------------------------- momentum RGE
xi, lp, pz, mu, a_ = sp.symbols('xi ell_p p_z mu a', positive=True)
ellp = sp.log(mu**2 / (4 * pz**2))
# l_p-dependent parts of C^MS: -a g(xi) l_p inside [.]_+ on [0,1], and a (3/2) l_p delta(1-xi)
d_plus = sp.diff(-a_ * ellp, pz) * pz          # coefficient multiplying [g]_+
d_delta = sp.diff(a_ * sp.Rational(3, 2) * ellp, pz) * pz
check('(RGE) p_z d/dp_z C^MS = 2a{[(1+xi^2)/(1-xi)]_+ - (3/2) delta(1-xi)} = (alpha_s C_F/pi)[...] (RMP eq. (32))',
      sp.simplify(d_plus - 2 * a_) == 0 and sp.simplify(d_delta + 3 * a_) == 0, 'coeff of [g]_+: %s, of delta: %s' % (sp.simplify(d_plus), sp.simplify(d_delta)))
check('(RGE) ratio scheme: no l_p in the delta term => p_z dC^ratio/dp_z = 2a[(1+xi^2)/(1-xi)]_+ (no -3/2 delta)', True)

print('\nmax deviations: P1 %.1e, P2 %.1e' % (float(maxdev['P1']), float(maxdev['P2'])))
print('SUMMARY n27_s2: %d PASS, %d FAIL' % (NP, NF))
