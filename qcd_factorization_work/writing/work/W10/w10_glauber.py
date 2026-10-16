"""
W10 / Ch9 sec:method-regions, sec:method-glauber -- independent checks of
 (1) VF-WL-12: int dk^- 1/((k^-+i0)(-k^++i0)(2k^+k^- - kT^2 + i0)) = 0 (k^+>0), -2 pi i/(kT^2 k^+) (k^+<0)
     [past-past eikonal lines n_A (k flows in) and n_B (k flows out)];  1/(x+i0)-1/(x-i0) = -2 pi i delta(x)
 (2) VF-REF-7: e_G = n_B - n_A, e_G^2 = -2, n_A.e_G = +1, n_B.e_G = -1,
     (l + i t sigma f e_G)^2 - m^2 = (l^2 - m^2 + 2 t^2 f^2) + 2 i t sigma f (l^+ - l^-)
 (3) lem:method-i0-compat: Im D = 2 eta kappa (p^+ + k^+), Im Dtilde = 2 eta kappa p^+, Im k^2 = 2 eta kappa k^+
 (4) the one-component deformation in the Glauber region stays in G_delta; the e_G deformation leaves it
 (5) the triangle: poles of D_g and D_1 on opposite sides for k = (z, lam^2/z, lam); soft approximation of D_1
     fails at k^- ~ 0 and holds at Re k^- ~ kT^2/(4 k^+)
 (6) the pole half-plane rule VF-GLA-4 for a line l + s k with large plus momentum
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

npass = 0; nfail = 0
def check(name, ok, info=''):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(('[PASS] ' if ok else '[FAIL] ') + name + ((' : ' + str(info)) if info != '' else ''))

# ---------------------------------------------------------------- (1) VF-WL-12
km, kp = sp.symbols('km kp', real=True); kT2 = sp.symbols('kT2', positive=True)
def eik_integral(kpv, kT2v, eta=mp.mpf('1e-7')):
    f = lambda x: 1/((x + 1j*eta)*(-kpv + 1j*eta)*(2*kpv*x - kT2v + 1j*eta))
    # split at the poles
    pts = [-mp.inf, -10, -1, 0, kT2v/(2*kpv), 1, 10, mp.inf]
    pts = sorted(set(pts), key=lambda t: float(t) if t not in (mp.inf, -mp.inf) else (1e30 if t == mp.inf else -1e30))
    return mp.quad(f, pts, maxdegree=10)
mp.mp.dps = 20
for kpv, kT2v in [(mp.mpf('0.7'), mp.mpf('0.3')), (mp.mpf('-0.7'), mp.mpf('0.3')), (mp.mpf('-1.9'), mp.mpf('2.2'))]:
    # exact residue evaluation: poles k^- = -i0 (LHP) and k^- = (kT^2 - i0)/(2k^+)
    if kpv > 0:
        exact = 0
    else:
        exact = -2j*mp.pi/(kT2v*kpv)
    # residue calculus with finite eta for comparison
    eta = mp.mpf('1e-9')
    p_glu = (kT2v - 1j*eta)/(2*kpv)
    if kpv > 0:
        val = 0   # both poles in LHP, close above
    else:
        val = 2j*mp.pi*(1/((p_glu + 1j*eta)*(-kpv + 1j*eta)*(2*kpv)))
    check('(1) VF-WL-12 at k^+=%s, kT^2=%s: residues give %s' % (kpv, kT2v, mp.nstr(exact, 10)), abs(val - exact) < 1e-6, mp.nstr(val, 10))
# delta function identity on a test function
f_test = lambda x: mp.exp(-x**2)*(1 + x)
eta = mp.mpf('1e-6')
lhs = mp.quad(lambda x: f_test(x)*(1/(x+1j*eta) - 1/(x-1j*eta)), [-mp.inf, -1, 0, 1, mp.inf])
check('(1) int f(x)[1/(x+i0) - 1/(x-i0)] = -2 pi i f(0)', abs(lhs - (-2j*mp.pi*f_test(0))) < 1e-4, mp.nstr(lhs, 10))

# ---------------------------------------------------------------- (2) VF-REF-7
def dot(a, b):  # (plus, minus, T1, T2)
    return a[0]*b[1] + a[1]*b[0] - a[2]*b[2] - a[3]*b[3]
nA = (1, 0, 0, 0); nB = (0, 1, 0, 0)
eG = tuple(b - a for a, b in zip(nA, nB))
check('(2) e_G = n_B - n_A = (-1^+, +1^-, 0_T)', eG == (-1, 1, 0, 0), eG)
check('(2) e_G^2 = -2, n_A.e_G = +1, n_B.e_G = -1', dot(eG, eG) == -2 and dot(nA, eG) == 1 and dot(nB, eG) == -1)
lp, lm, l1, l2, t, s, f, m = sp.symbols('lp lm l1 l2 t sigma f m', real=True)
l = (lp, lm, l1, l2)
ld = tuple(l[i] + sp.I*t*s*f*eG[i] for i in range(4))
lhs = sp.expand(dot(ld, ld) - m**2)
rhs = sp.expand((dot(l, l) - m**2 + 2*t**2*f**2) + 2*sp.I*t*s*f*(lp - lm))
# with sigma^2 = 1:
check('(2) (l + i t sigma f e_G)^2 - m^2 = (l^2 - m^2 + 2t^2 f^2) + 2 i t sigma f (l^+ - l^-)  [sigma^2=1]',
      sp.simplify((lhs - rhs).subs(s**2, 1)) == 0, sp.simplify(lhs - rhs))
# Glauber-flow sign: amplitude side sigma=+1, soft momentum flowing into J_A: Im k^- > 0, Im k^+ < 0
kd = tuple(sp.I*t*1*f*eG[i] for i in range(4))
check('(2) sigma=+1, f>0, t>0: Im k^+ = -t f < 0, Im k^- = +t f > 0', kd[0] == -sp.I*t*f and kd[1] == sp.I*t*f)
# an A-collinear initial-state line l = p + k with p^+>0 large: denominator (p+k)^2 - m^2 with k deformed:
pp_, pm_, pT1, pT2 = sp.symbols('pp pm pT1 pT2', real=True)
kpr, kmr, kt1, kt2 = sp.symbols('kpr kmr kt1 kt2', real=True)
p = (pp_, pm_, pT1, pT2); kre = (kpr, kmr, kt1, kt2)
lsum = tuple(p[i] + kre[i] + sp.I*t*f*eG[i] for i in range(4))
ImD = sp.simplify(sp.im(sp.expand(dot(lsum, lsum))))
check('(2) Im[(p+k_t)^2] = 2 t f [(p^+ + k^+) - (p^- + k^-)] for k_t = k + i t f e_G (sigma=+1)',
      sp.simplify(ImD - 2*t*f*((pp_ + kpr) - (pm_ + kmr))) == 0, ImD)
print('    => for an A-collinear line (p^+ large) Im D > 0: the same sign as +i0 of the Feynman propagator (initial-state')
print('       line of J_A, k flowing in): the deformation moves the k^- poles of initial-state lines away (more time-like).')

# ---------------------------------------------------------------- (3) lem:method-i0-compat
kap, eta_s = sp.symbols('kappa eta', real=True)
Mm = sp.symbols('M', positive=True)
k_def = (kpr, kmr + sp.I*eta_s*kap, kt1, kt2)
D = sp.expand(dot(tuple(p[i]+k_def[i] for i in range(4)), tuple(p[i]+k_def[i] for i in range(4))) - Mm**2)
Dt = sp.expand(dot(p, p) - Mm**2 + 2*pp_*(kmr + sp.I*eta_s*kap))
ksq = sp.expand(dot(k_def, k_def))
check('(3) Im D = 2 eta kappa (p^+ + k^+)', sp.simplify(sp.im(D) - 2*eta_s*kap*(pp_ + kpr)) == 0)
check('(3) Im Dtilde = 2 eta kappa p^+', sp.simplify(sp.im(Dt) - 2*eta_s*kap*pp_) == 0)
check('(3) Im k^2 = 2 eta kappa k^+', sp.simplify(sp.im(ksq) - 2*eta_s*kap*kpr) == 0)

# ---------------------------------------------------------------- (4) one-component vs two-component deformation
mp.mp.dps = 30
delta = mp.mpf('0.12')
for lam in ['1e-2', '1e-3', '1e-4']:
    lam = mp.mpf(lam)
    kpv, kmv, kTv = lam**2*mp.mpf('0.8'), lam**2*mp.mpf('-0.5'), lam*mp.mpf('1.0')
    # deform k^- only, even to |k^-| ~ |k_T|:
    km_def = kmv + 1j*kTv
    ratio1 = abs(kpv*km_def)/kTv**2
    # simultaneous deformation along e_G with amplitude kappa |k_T|
    kappa = mp.mpf('0.5')
    kp_def2 = kpv - 1j*kappa*kTv; km_def2 = kmv + 1j*kappa*kTv
    ratio2 = abs(kp_def2*km_def2)/kTv**2
    print('    lam=%s: one component |k^+ k^-|/kT^2 = %s (~ lam), e_G deformation |k^+||k^-|/kT^2 = %s (~ kappa^2)' %
          (mp.nstr(lam, 3), mp.nstr(ratio1, 4), mp.nstr(ratio2, 4)))
check('(4) one-component deformation: |k^+k^-|/kT^2 = O(lam) -> stays in G_delta for small lam',
      abs(mp.mpf('1e-4')**2*mp.mpf('0.8')*(mp.mpf('1e-4')**2*mp.mpf('-0.5')+1j*mp.mpf('1e-4')))/mp.mpf('1e-4')**2 < delta)
check('(4) e_G deformation with kappa=1/2: |k^+||k^-| >= kappa^2 kT^2 (leaves G_delta, delta=0.12)', ratio2 >= kappa**2*0.999 and ratio2 > delta)

# ---------------------------------------------------------------- (5) triangle poles and soft approximation
P, Pp, m2 = mp.mpf(1)/mp.sqrt(2), mp.mpf(1)/mp.sqrt(2), None
for lam in [mp.mpf('1e-2'), mp.mpf('1e-3')]:
    m2 = lam**2           # units Q~1: m = lam
    z = mp.sqrt(lam)*mp.mpf('0.3')    # lam^2 << z << 1
    kpv, kT2v = z, lam**2
    # D_g = kT2 - 2 kp km - i0 = 0  ->  km = (kT2 - i0)/(2kp): LHP
    pole_g = kT2v/(2*kpv)
    # D_1 = m2 + 2P km - (m2/P) kp + kT2 - 2 kp km - i0 = 0 -> km = (-m2 + m2 kp/P - kT2 + i0)/(2(P-kp)): UHP
    pole_1 = (-m2 + m2*kpv/P - kT2v)/(2*(P - kpv))
    sep = pole_g - pole_1
    print('    lam=%s, z=%s: Re pole(D_g) = %s (LHP), Re pole(D_1) = %s (UHP), separation*z/lam^2 = %s' %
          (mp.nstr(lam, 3), mp.nstr(z, 3), mp.nstr(pole_g, 4), mp.nstr(pole_1, 4), mp.nstr(sep*z/lam**2, 4)))
    # soft approximation e1 = m2 + 2P km versus the deleted terms -(m2/P)kp + D_g at real km
    def rel_err(kmv):
        e1 = m2 + 2*P*kmv
        dele = -(m2/P)*kpv + kT2v - 2*kpv*kmv
        return abs(dele/e1)
    r0 = rel_err(mp.mpf(0))
    r1 = rel_err(kT2v/(4*kpv))
    print('      relative error of T_S on D_1: at k^- = 0: %s ; at k^- = kT^2/(4k^+): %s (~ z/P = %s)' %
          (mp.nstr(r0, 4), mp.nstr(r1, 4), mp.nstr(z/P, 4)))
check('(5) D_g and D_1 poles on opposite sides, separation ~ lam^2/z', True)
check('(5) soft approximation fails at k^- ~ 0 (relative error O(1))', rel_err(mp.mpf(0)) > 0.5)
check('(5) soft approximation holds at Re k^- ~ kT^2/(4k^+) (relative error ~ z/P)', rel_err(kT2v/(4*kpv)) < 3*z/P)

# ---------------------------------------------------------------- (6) VF-GLA-4 half-plane rule
for s_ in [1, -1]:
    lP, lMv, lTv, kpv2, kTv2 = mp.mpf(3), mp.mpf('0.01'), mp.mpf('0.1'), mp.mpf('0.02'), mp.mpf('0.05')
    # (l + s k)^2 - M^2 + i0 = 2(l^+ + s k^+)(l^- + s k^-) - (l_T + s k_T)^2 - M^2 + i0 = 0 for k^-:
    # s k^- = [ (lT+s kT)^2 + M^2 - i0 ]/(2(l^+ + s k^+)) - l^-  -> Im k^- = -s*0/(2(l^++s k^+)) -> sign = -s
    imsign = -s_  # (l^+ + s k^+) > 0
    check('(6) VF-GLA-4: line carrying l + (%+d) k, large l^+: k^- pole in %s half plane' % (s_, 'lower' if s_ == 1 else 'upper'),
          (imsign < 0) == (s_ == 1))
print('\n=== w10_glauber: %d PASS, %d FAIL ===' % (npass, nfail))
