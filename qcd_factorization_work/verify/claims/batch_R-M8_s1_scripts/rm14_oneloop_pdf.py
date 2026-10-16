# R-M14 independent check: one-loop quark-in-quark PDF (operator definition, Feynman gauge, massless quark,
# gluon mass m as IR regulator, DR for UV).  Written independently of research/c_pdf/scripts/s2_oneloop_qq.py.
# Conventions: CONTEXT.md (v.w = v+w- + v-w+ - vT.wT; f = int dw-/(4pi) e^{-i xi P+ w-} <P|psibar g+ W psi|P>).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
import mpmath as mp

ok = True
def check(name, cond, extra=''):
    global ok
    ok &= bool(cond)
    print(('PASS ' if cond else 'FAIL ') + name + ('  ' + extra if extra else ''))

# ---------------------------------------------------------------- 1. Dirac traces with explicit 4x4 matrices (D = 4)
I2 = np.eye(2); Z2 = np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
g0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
gs = [np.block([[Z2, s], [-s, Z2]]) for s in (sx, sy, sz)]
G = [g0] + gs                                   # gamma^mu, metric (+,-,-,-)
eta = np.diag([1, -1, -1, -1.])
def slash(v):                                    # v given with upper (Cartesian) components (v0,v1,v2,v3)
    return sum(eta[m, m] * v[m] * G[m] for m in range(4))
gplus = (g0 + G[3]) / np.sqrt(2)                 # gamma^+ = (g0 + g3)/sqrt2 ; n.v = v^+ for n with n^- = 1
def cart(vp, vm, vT):                            # light-front -> Cartesian
    return np.array([(vp + vm) / np.sqrt(2), vT[0], vT[1], (vp - vm) / np.sqrt(2)])
def dot(a, b):
    return a[0] * b[0] - a[1] * b[1] - a[2] * b[2] - a[3] * b[3]

rng = np.random.default_rng(1)
for trial in range(3):
    pp, xi, m = 1.7, rng.uniform(0.1, 0.9), rng.uniform(0.2, 1.0)
    lT = rng.normal(size=2); LT2 = lT @ lT
    p = cart(pp, 0.0, [0, 0])
    l = cart((1 - xi) * pp, (LT2 + m**2) / (2 * (1 - xi) * pp), lT)     # on-shell massive gluon
    k = p - l
    k2 = dot(k, k)
    # ladder: (1/2) sum_s ubar g^nu kslash g+ kslash g^mu u (-g_{mu nu}) / (k^2)^2 = (1/2) Tr[pslash (-g_mu..)]
    X = sum(eta[n, n] * G[n] @ slash(k) @ gplus @ slash(k) @ G[n] for n in range(4))   # gamma^nu ... gamma_nu
    R1 = 0.5 * np.trace(slash(p) @ (-X)).real / k2**2
    R1_exp = 4 * pp * LT2 * (1 - xi)**2 / (LT2 + xi * m**2)**2          # D=4: 4(1-eps) -> 4
    # interference (gluon on Wilson line on one side): eikonal factor n^mu/(n.l) ; both orderings
    # (1/2) Tr[pslash gamma+ kslash gamma^mu] n_mu/(n.l) /k^2 * (-1 from -g) * 2 (h.c.) -- magnitude and sign
    nslash = gplus
    T = 0.5 * np.trace(slash(p) @ gplus @ slash(k) @ nslash).real
    R2 = -2 * T / ((1 - xi) * pp) / k2
    R2_exp = 8 * xi * pp / (LT2 + xi * m**2)
    check('trace R1 (ladder) = 4 p+ lT^2 (1-xi)^2/(lT^2+xi m^2)^2  [trial %d]' % trial, abs(R1 - R1_exp) < 1e-10 * abs(R1_exp))
    check('trace R2 (Wilson-line interference) = 8 xi p+/(lT^2+xi m^2) [trial %d]' % trial, abs(R2 - R2_exp) < 1e-10 * abs(R2_exp))
    check('k^2 = -(lT^2 + xi m^2)/(1-xi) [trial %d]' % trial, abs(k2 + (LT2 + xi * m**2) / (1 - xi)) < 1e-12)

# ---------------------------------------------------------------- 2. l^- contour integral of the virtual Wilson-line graph
# Check the residue evaluation at finite i*delta against direct numerical integration (poles used as breakpoints),
# then the delta -> 0 limit i pi/(p+(lT^2 + x m^2)) on 0<x<1 and 0 outside.
mp.mp.dps = 30
def lminus_num(lp, pp, LT2, m2, dl):
    a1 = 2 * lp; a2 = -2 * (pp - lp)
    f = lambda lm: 1 / ((a1 * lm - LT2 - m2 + 1j * dl) * (a2 * lm - LT2 + 1j * dl))
    p1 = (LT2 + m2) / a1 if a1 != 0 else 0
    p2 = LT2 / a2 if a2 != 0 else 0
    pts = sorted(set([p1, p2]))
    grid = [-mp.inf] + [pts[0] - 5, pts[0] - 0.1, pts[0] - 0.001, pts[0], pts[0] + 0.001, pts[0] + 0.1]
    grid += [pts[-1] - 0.1, pts[-1] - 0.001, pts[-1], pts[-1] + 0.001, pts[-1] + 0.1, pts[-1] + 5, mp.inf]
    grid = sorted(set(grid), key=lambda v: (v == mp.inf, v))
    grid = [g for g in grid if g == -mp.inf] + sorted([g for g in grid if g not in (-mp.inf, mp.inf)]) + [mp.inf]
    return mp.quad(f, grid, maxdegree=10)
def lminus_res(lp, pp, LT2, m2, dl):
    # exact value for finite dl by residues (both poles from the i*dl prescription)
    a1 = 2 * lp; a2 = -2 * (pp - lp)
    z1 = (LT2 + m2 - 1j * dl) / a1           # zero of first factor
    z2 = (LT2 - 1j * dl) / a2                # zero of second factor
    # close in the upper half plane: pick poles with Im z > 0
    tot = 0
    if mp.im(z1) > 0: tot += 2j * mp.pi / (a1 * (a2 * z1 - LT2 + 1j * dl))
    if mp.im(z2) > 0: tot += 2j * mp.pi / (a2 * (a1 * z2 - LT2 - m2 + 1j * dl))
    return tot
pp, LT2, m2 = mp.mpf('1.3'), mp.mpf('0.7'), mp.mpf('0.4')
for lp in [mp.mpf('0.91'), mp.mpf('0.26'), mp.mpf('-0.4'), mp.mpf('1.6')]:
    dl = mp.mpf('0.05')
    vn, vr = lminus_num(lp, pp, LT2, m2, dl), lminus_res(lp, pp, LT2, m2, dl)
    check('l^- integral: numerical = residue formula at finite i*delta (l+=%s)' % lp, abs(vn - vr) < 1e-8 * max(1, abs(vr)), '%s | %s' % (mp.nstr(vn, 10), mp.nstr(vr, 10)))
    lim = lminus_res(lp, pp, LT2, m2, mp.mpf('1e-25'))
    x = 1 - lp / pp
    exp = mp.pi * 1j / (pp * (LT2 + x * m2)) if 0 < lp < pp else 0
    check('  delta->0 limit = i pi/(p+(lT^2 + x m^2)) theta(0<l+<p+)  (x=%s)' % mp.nstr(x, 4), abs(lim - exp) < 1e-20, mp.nstr(lim, 12))

# ---------------------------------------------------------------- 3. self-energy Sigma_V(0), massive gluon, massless quark
# Sigma(p) = pslash Sigma_V ; Sigma_V(0) = (2-D) g^2 C_F/(4pi)^{D/2} Gamma(eps) int_0^1 dy (1-y) [(1-y) m^2]^{-eps}
eps = sp.symbols('epsilon')
y = sp.symbols('y', positive=True)
Iy = sp.integrate((1 - y) * (1 - y)**(-eps), (y, 0, 1), conds='none')
check('int_0^1 (1-y)^{1-eps} dy = 1/(2-eps)', sp.simplify(Iy - 1 / (2 - eps)) == 0)
# with g^2 = 4 pi alpha_s mu^{2eps} e^{eps gE}/(4pi)^eps:  g^2/(4pi)^{D/2} = (alpha_s/4pi) mu^{2eps} e^{eps gE}
# => Sigma_V(0) = -(1-eps)/(2-eps) * A_eps,  A_eps = (alpha_s C_F/2pi) e^{eps gE} Gamma(eps) (mu^2/m^2)^eps
SigV_over_A = sp.simplify((2 - (4 - 2 * eps)) / 2 * Iy)          # (2-D)*(alpha_s/4pi)/(alpha_s/2pi) = (2-D)/2
check('Sigma_V(0)/A_eps = -(1-eps)/(2-eps)', sp.simplify(SigV_over_A + (1 - eps) / (2 - eps)) == 0)

# ---------------------------------------------------------------- 4. prefactor of the real graphs
# g^2 C_F/(2pi)^{3-2eps} * int d^{2-2eps} lT [ (1-eps)(1-xi) lT^2/(lT^2+M^2)^2 + 2xi/((1-xi)(lT^2+M^2)) ],  M^2 = xi m^2
# int d^d l (l^2)^a/(l^2+M^2)^b = pi^{d/2} G(a+d/2) G(b-a-d/2)/(G(d/2) G(b)) M^{2(a+d/2-b)}
d = 2 - 2 * eps
I_10 = sp.gamma(d / 2) * sp.gamma(1 - d / 2) / (sp.gamma(d / 2) * sp.gamma(1))        # a=0,b=1, times pi^{d/2} M^{-2eps}
I_21 = sp.gamma(1 + d / 2) * sp.gamma(2 - 1 - d / 2) / (sp.gamma(d / 2) * sp.gamma(2))  # a=1,b=2
check('int d^{2-2eps}l/(l^2+M^2) = pi^{1-eps} Gamma(eps) M^{-2eps}', sp.simplify(I_10 - sp.gamma(eps)) == 0)
check('int d^{2-2eps}l l^2/(l^2+M^2)^2 = pi^{1-eps}(1-eps) Gamma(eps) M^{-2eps}', sp.simplify(sp.gammasimp(I_21 - (1 - eps) * sp.gamma(eps))) == 0)
# numeric check of the master formula at eps = 0.3
M2v, ev = mp.mpf('0.6'), mp.mpf('0.3')
num = 2 * mp.pi**(1 - ev) / mp.gamma(1 - ev) * mp.quad(lambda t: (lambda L: L**(-ev) * L / (L + M2v)**2 * L)(mp.e**t), [-mp.inf, -20, -5, 0, 5, 20, 80, mp.inf]) / 2   # angular: d^{d}l = pi^{d/2}/G(d/2) (l^2)^{d/2-1} dl^2
ana = mp.pi**(1 - ev) * (1 - ev) * mp.gamma(ev) * M2v**(-ev)
check('master formula numerically (eps=0.3)', abs(num - ana) < 1e-15, '%s vs %s' % (mp.nstr(num, 12), mp.nstr(ana, 12)))
# coupling/phase-space normalisation: 4 pi alpha_s mu^{2eps} e^{eps gE}(4pi)^{-eps} * pi^{1-eps}/(2pi)^{3-2eps} = (alpha_s/2pi) mu^{2eps} e^{eps gE}
norm = sp.simplify(4 * sp.pi * (4 * sp.pi)**(-eps) * sp.pi**(1 - eps) / (2 * sp.pi)**(3 - 2 * eps) * 2 * sp.pi)
check('coupling x phase-space normalisation = alpha_s/(2pi)', sp.simplify(sp.powsimp(sp.expand_power_base(norm, force=True), force=True)) == 1, str(norm))

# ---------------------------------------------------------------- 5. assemble, expand in eps, MSbar, quark number
# bare: A_eps { (1-eps)^2 (1-xi) xi^{-eps} + [2 xi^{1-eps}/(1-xi)]_+ - (1-eps)/(2-eps) delta(1-xi) }
# A_eps = a C_F [1/eps + Lm + O(eps)],  a = alpha_s/2pi, Lm = ln(mu^2/m^2)
xi_, Lm = sp.symbols('xi L_m', positive=True)
Aser = 1 / eps + Lm            # O(eps) terms of A only multiply O(eps) of the brackets -> irrelevant at O(eps^0)? (bracket is O(1)) -> need A to O(eps): A = 1/eps + Lm + eps*c ; c * bracket(eps=0) = c * [P/C_F] contributes c*P: absorbed? check below
c = sp.symbols('c')            # keep the O(eps) term of A explicitly
Aser = 1 / eps + Lm + c * eps
reg = (1 - eps)**2 * (1 - xi_) * xi_**(-eps)                   # regular part (ladder)
plus_num = 2 * xi_**(1 - eps)                                  # numerator of [ ./(1-xi)]_+
dcoef = -(1 - eps) / (2 - eps)
ser = lambda e: sp.series(e, eps, 0, 2).removeO()
reg_s = sp.expand(ser(Aser * reg))
plus_s = sp.expand(ser(Aser * plus_num))
d_s = sp.expand(ser(Aser * dcoef))
print('ladder part      :', sp.collect(reg_s, eps))
print('Wilson part (num):', sp.collect(plus_s, eps))
print('delta coefficient:', sp.collect(d_s, eps))
# finite parts (eps^0):
reg0 = sp.simplify(reg_s.coeff(eps, 0)); plus0 = sp.simplify(plus_s.coeff(eps, 0)); d0 = sp.simplify(d_s.coeff(eps, 0))
check('ladder eps^0 = (1-xi)(Lm - 2 - ln xi)', sp.simplify(reg0 - (1 - xi_) * (Lm - 2 - sp.log(xi_))) == 0)
check('Wilson eps^0 numerator = 2xi Lm - 2 xi ln xi', sp.simplify(plus0 - (2 * xi_ * Lm - 2 * xi_ * sp.log(xi_))) == 0)
check('delta eps^0 = -(1/2) Lm + 1/4', sp.simplify(d0 - (-Lm / 2 + sp.Rational(1, 4))) == 0)
# poles: (1-xi) + [2xi/(1-xi)]_+ - 1/2 delta  = [(1+xi^2)/(1-xi)]_+
check('pole of ladder = (1-xi), of Wilson = 2xi/(1-xi) (plus), of delta = -1/2',
      sp.simplify(reg_s.coeff(eps, -1) - (1 - xi_)) == 0 and sp.simplify(plus_s.coeff(eps, -1) - 2 * xi_) == 0 and sp.simplify(d_s.coeff(eps, -1) + sp.Rational(1, 2)) == 0)
# the O(eps) constant c of A_eps does not enter: it multiplies the eps^{-1}... no: c*eps * (1/eps-free bracket at eps=0) -> c * P/C_F at eps^1? check
check('O(eps) term of A_eps does not affect the eps^0 coefficient', all(sp.diff(t, c) == 0 for t in [reg0, plus0, d0]))
# test-function check of the renormalised finite part against the claimed closed form, and quark number
mp.mp.dps = 25
def finite_pairing(h):
    # <f_fin, h> in units a*C_F, Lm = 0 part, using the eps^0 pieces above with Lm=0
    lad = mp.quad(lambda x: (1 - x) * (-2 - mp.log(x)) * h(x), [0, 1])
    wil = mp.quad(lambda x: (-2 * x * mp.log(x)) / (1 - x) * (h(x) - h(1)), [0, 1])
    return lad + wil + mp.mpf(1) / 4 * h(1)
claimed = lambda h: (mp.quad(lambda x: -(1 - x) * (2 + mp.log(x)) * h(x), [0, 1])
                     - mp.quad(lambda x: 2 * x * mp.log(x) / (1 - x) * (h(x) - h(1)), [0, 1]) + h(1) / 4)
for h in [lambda x: 1, lambda x: x, lambda x: x**3, lambda x: mp.exp(-x)]:
    check('finite part pairs like  -(1-xi)(2+ln xi) - [2 xi ln xi/(1-xi)]_+ + delta/4', abs(finite_pairing(h) - claimed(h)) < 1e-20)
check('quark number of the renormalised finite part: <f_fin, 1> = 0', abs(finite_pairing(lambda x: 1)) < 1e-20, mp.nstr(finite_pairing(lambda x: 1), 5))
# the Lm coefficient pairs like P_qq: (1-xi) + [2xi/(1-xi)]_+ - 1/2 delta, quark number zero
lm_pair = lambda h: (mp.quad(lambda x: (1 - x) * h(x), [0, 1]) + mp.quad(lambda x: 2 * x / (1 - x) * (h(x) - h(1)), [0, 1]) - h(1) / 2)
P_pair = lambda h: mp.quad(lambda x: (1 + x**2) / (1 - x) * (h(x) - h(1)), [0, 1])   # [(1+x^2)/(1-x)]_+ = (1+x^2)/(1-x)_+ + 3/2 delta
for h in [lambda x: 1, lambda x: x, lambda x: x**2 + 3 * x**5]:
    check('ln(mu^2/m^2) coefficient = P_qq/C_F = [(1+xi^2)/(1-xi)]_+', abs(lm_pair(h) - P_pair(h)) < 1e-20)
# endpoint: the Wilson-line real graph alone is not integrable at xi -> 1 for any eps (and any m): xi^{1-eps}/(1-xi)
print('Wilson-line real graph integrand at xi -> 1 behaves like 2/(1-xi) for every eps and m: not regulated by DR or by m;')
print('it is cancelled only by the virtual Wilson-line graph, forming [2 xi^{1-eps}/(1-xi)]_+  (cf. section 2 above).')
print('SUMMARY rm14:', 'ALL PASS' if ok else 'SOME FAIL')
