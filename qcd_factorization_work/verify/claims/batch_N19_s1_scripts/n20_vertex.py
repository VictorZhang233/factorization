"""
n20_vertex.py -- independent verification of claim N20 (stage-1 verifier).

One-loop vertex graph of the unsubtracted TMD of an on-shell massless quark p=(p^+,0,0_T), Feynman gauge,
Wilson line n=(n^+,n^-,0_T) attached to psi(0):
   V = i g^2 C_F mu^{2eps} \int d^Dl/(2pi)^D  N(l) / [(n.l -/+ i0)(l^2+i0)((p-l)^2+i0)],
   (n.l - i0): SIDIS (future-pointing),  (n.l + i0): DY (past-pointing),  N = Tr[pslash g^+ (pslash-lslash) nslash]/Tr[pslash g^+].
METHOD (different from the project's Feynman/Schwinger-parameter route): light-cone variables,
l^- integral by residues (exact), then l_T (DR, t = l_T^2) and x = l^+/p^+ integrals in closed form, region by region,
each region continued analytically in eps.  i0 bookkeeping: when a single pole z_* is picked, every other denominator is
written c*(z_* - z_other) and inherits the sign of Im z_* (all other poles lie in the opposite half plane).
Units: p^+ = 1, n^- = 1, n^+ = a  (a>0 time-like, a<0 space-like); n^2 = 2a, p.n = 1.

Also checked: (i) numerator N = 2 n^-(p^+ - l^+) in D dims (own trace),
(ii) numerical checks of the l^- residues and of the complex-c t-integral formulas at finite i0,
(iii) the remainder Fourier transform 2 pi int dk/k J0(k z) [ln(1+k^2) + 2k arctan(1/k)] vs 2 pi^2/z.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
mp.mp.dps = 40
RES = []
def check(name, ok, info=''):
    RES.append(bool(ok)); print(('PASS ' if ok else 'FAIL ') + name + (('   [' + info + ']') if info else ''))

# ---------------------------------------------------------------- (i) numerator, own D-dim trace of 4 gammas
pp, npl, nmi, lp, lm, lT2 = sp.symbols('pp npl nmi lp lm lT2')
def dot(u, v):   # light-cone dot product, vectors as (plus, minus, Tsq-handled) ; transverse parts: only l has one
    (u1, u2, uT), (v1, v2, vT) = u, v
    return u1*v2 + u2*v1 - (uT*vT)
# represent transverse parts by symbols: only l has l_T; dot(l,l) needs -lT2; dot(l,other) has no T part
P = (pp, 0, 0); Vv = (0, 1, 0); Nn = (npl, nmi, 0); L = (lp, lm, 0)   # (T parts handled separately)
def d(u, v):
    val = dot(u, v)
    return val
def tr4(a, b, c, e):  # Tr[a b c e]/4 = (a.b)(c.e) - (a.c)(b.e) + (a.e)(b.c)
    return d(a, b)*d(c, e) - d(a, c)*d(b, e) + d(a, e)*d(b, c)
PL = (pp - lp, -lm, 0)   # p - l (its transverse part only enters via dot with l_T-free vectors -> irrelevant here)
num = tr4(P, Vv, PL, Nn); den = d(P, Vv)
Nexpr = sp.simplify(2*num/(2*den))
check('N(l) = Tr[pslash g^+ (pslash-lslash) nslash]/Tr[pslash g^+] = 2 n^- (p^+ - l^+)', sp.simplify(Nexpr - 2*nmi*(pp - lp)) == 0, str(sp.factor(Nexpr)))

# ---------------------------------------------------------------- (ii) region-by-region closed forms (my derivation)
B = lambda u, v: mp.gamma(u)*mp.gamma(v)/mp.gamma(u + v)
def K_case(case, e, absa=mp.mpf(1)):
    """K = int dx int_0^inf dt t^{-eps} R(x,t),  int dl^- F = 2 pi i R.  Closed forms, region by region."""
    e = mp.mpf(e) if not isinstance(e, mp.mpc) else e
    C = 2**(-1 - e)*(mp.pi/mp.sin(mp.pi*e))*absa**e
    ph = mp.e**(1j*mp.pi*e)
    if case == 'SIDIS_time':     # (0,1): -Res_G ; (1,inf): Res_E
        r01 = -B(-2*e, 2)
        r1i = B(2*e - 1, 2) - B(2*e - 1, 2 - e)
        return C*(r01 + r1i)
    if case == 'DY_time':        # (-inf,0): -Res_E ; (0,1): Res_Q with (2x(1-x) - a t + i0)
        rm0 = B(-e, 2*e - 1)
        r01 = mp.e**(1j*mp.pi*(1 + e))*B(-e, 2 - e)
        return C*(rm0 + r01)
    if case == 'SIDIS_space':    # (-inf,0): -Res_E with two t-poles (+i0) ; (0,1): Res_Q (no pole)
        rm0 = ph*B(-e, 2*e - 1)
        r01 = -B(-e, 2 - e)
        return C*(rm0 + r01)
    if case == 'DY_space':       # (0,1): -Res_G with (2x^2 - b t + i0) ; (1,inf): Res_E with two t-poles (+i0)
        r01 = mp.e**(1j*mp.pi*(1 + e))*B(-2*e, 2)
        r1i = ph*(B(2*e - 1, 2) - B(2*e - 1, 2 - e))
        return C*(r01 + r1i)
def V_mine(case, e):
    """V / [(alpha_s C_F/4pi) (2 pi |a| mu^2)^eps]   (mu=1, |a|=1):  V = -(alpha_s C_F/4pi) 4 (4 pi mu^2)^eps K/Gamma(1-eps)"""
    e = mp.mpf(e)
    K = K_case(case, e)
    return -4*(4*mp.pi)**e*K/mp.gamma(1 - e)/(2*mp.pi)**e
def V_proj_time_sidis(e):   # project's closed form, c_tmd DERIVATION 3.4 (same normalisation)
    e = mp.mpf(e)
    return -mp.gamma(1 - e)*mp.gamma(1 + 2*e)*(1 - e)/((1 - 2*e)*e**2)
for e in ['0.17', '-0.23', '0.41', '-0.07', '0.013']:
    vs = V_mine('SIDIS_time', e); vp = V_proj_time_sidis(e)
    vd = V_mine('DY_time', e); vss = V_mine('SIDIS_space', e); vds = V_mine('DY_space', e)
    E = mp.mpf(e)
    ok1 = abs(vs - vp) < mp.mpf(10)**-30*abs(vp)
    ok2 = abs(vd - mp.e**(2j*mp.pi*E)*vs) < mp.mpf(10)**-30*abs(vs)
    ok3 = abs(vss - mp.e**(-1j*mp.pi*E)*vs) < mp.mpf(10)**-30*abs(vs) and abs(vds - mp.e**(1j*mp.pi*E)*vs) < mp.mpf(10)**-30*abs(vs)
    ok4 = abs(vss - mp.conj(vds)) < mp.mpf(10)**-30*abs(vs)
    check('eps=%s: V_SIDIS^time (light-cone residues) = project closed form -G(1-e)G(1+2e)(1-e)/((1-2e)e^2)' % e, ok1,
          'mine %s  proj %s' % (mp.nstr(vs, 15), mp.nstr(vp, 15)))
    check('eps=%s: V_DY^time = e^{2 i pi eps} V_SIDIS^time ; V_SIDIS^space = e^{-i pi eps} V^time, V_DY^space = e^{+i pi eps} V^time' % e, ok2 and ok3)
    check('eps=%s: space-like lines: V_SIDIS = (V_DY)^*  exactly' % e, ok4, 'SIDIS %s  DY %s' % (mp.nstr(vss, 12), mp.nstr(vds, 12)))
    diff = mp.re(vd) - vs
    exact = 2*mp.sin(mp.pi*E)**2*(-vs)
    check('eps=%s: Re V_DY^time - V_SIDIS^time = 2 sin^2(pi eps) |V^time| (units alpha_s C_F/4pi x common power)' % e,
          abs(diff - exact) < mp.mpf(10)**-28*abs(exact), 'value %s' % mp.nstr(diff, 15))
# exact identities used: S = -P  and  B(-e,2-e) = 2cos(pi e) B(-e,2e-1)
es = sp.Symbol('e')
Bs = lambda u, v: sp.gamma(u)*sp.gamma(v)/sp.gamma(u + v)
S_ = -Bs(-2*es, 2) + Bs(2*es - 1, 2) - Bs(2*es - 1, 2 - es); P_ = Bs(-es, 2*es - 1)
for ev in [sp.Rational(1, 7), sp.Rational(-2, 9), sp.Rational(3, 11)]:
    check('identity S = -P exact at eps=%s' % ev, sp.N((S_ + P_).subs(es, ev), 40) == 0 or abs(sp.N((S_ + P_).subs(es, ev), 40)) < 1e-35)
    check('identity B(-e,2-e) = 2 cos(pi e) B(-e,2e-1) at eps=%s' % ev,
          abs(sp.N((Bs(-es, 2 - es) - 2*sp.cos(sp.pi*es)*P_).subs(es, ev), 40)) < 1e-35)
ser = sp.series(2*sp.sin(sp.pi*es)**2*sp.gamma(1 - es)*sp.gamma(1 + 2*es)*(1 - es)/((1 - 2*es)*es**2), es, 0, 2).removeO()
check('eps->0: Re V_DY^time - V_SIDIS^time -> (alpha_s C_F/4pi) * 2 pi^2', sp.simplify(ser.subs(es, 0) - 2*sp.pi**2) == 0, 'series: %s' % sp.nsimplify(sp.expand(ser)))
# Coulomb phase of the DY time-like vertex: Im V_DY = sin(2 pi eps) V^time -> -(2 pi/eps + ...)
serI = sp.series(sp.sin(2*sp.pi*es)*(-sp.gamma(1 - es)*sp.gamma(1 + 2*es)*(1 - es)/((1 - 2*es)*es**2)), es, 0, 1).removeO()
print('      Im V_DY^time /(alpha_s C_F/4pi) =', sp.simplify(serI))

# ---------------------------------------------------------------- (ii-b) numeric checks of residues and i0 bookkeeping
# (1) l^- integral at finite i0 vs 2 pi i R(x,t), DY time-like, 0<x<1 (where the t-pole sits)  and SIDIS space-like x<0
def F(z, x, t, a, sE, d):
    E = a*z + x - 1j*sE*d       # sE=+1: SIDIS (n.l - i0); sE=-1: DY (n.l + i0)
    G = 2*x*z - t + 1j*d
    Q = -2*(1 - x)*z - t + 1j*d
    return (1 - x)/(E*G*Q)
def lminus_int(x, t, a, sE, d):
    poles = [(-x)/a, t/(2*x) if x != 0 else 0, t/(2*(x - 1))]
    pts = sorted(set([p for p in poles])); grid = [-mp.inf]
    for p_ in pts:
        grid += [p_ - 1, p_ - 1e-3, p_, p_ + 1e-3, p_ + 1]
    grid = sorted(set(grid[1:])); grid = [-mp.inf] + grid + [mp.inf]
    return mp.quad(lambda z: F(z, x, t, a, sE, d), grid, maxdegree=10)
d = mp.mpf('1e-9')
x, t, a = mp.mpf('0.3'), mp.mpf('0.25'), mp.mpf('0.7')
num = lminus_int(x, t, a, -1, d)
R = (1 - x)**2/(t*(2*x*(1 - x) - a*t))     # away from the t-pole (2x(1-x)=0.42 vs a t = 0.175): no i0 needed
check('l^- residue, DY time-like, 0<x<1: int dl^- F = 2 pi i (1-x)^2/(t(2x(1-x)-a t))', abs(num - 2j*mp.pi*R) < 1e-6*abs(R), '%s vs %s' % (mp.nstr(num, 10), mp.nstr(2j*mp.pi*R, 10)))
x = mp.mpf('-0.4'); a = mp.mpf('-0.6'); b = -a
num = lminus_int(x, t, a, +1, d)
u = -x
R = (1 + u)*b/((2*u**2 - b*t)*(2*u*(1 + u) - b*t))
check('l^- residue, SIDIS space-like, x<0: int dl^- F = 2 pi i (1+u) b/((2u^2-bt)(2u(1+u)-bt))', abs(num - 2j*mp.pi*R) < 1e-6*abs(R), '%s vs %s' % (mp.nstr(num, 10), mp.nstr(2j*mp.pi*R, 10)))
# (2) sign of i0 at the t-pole: put t near the pole and compare finite-d numerics with  R evaluated with +i*eta
x = mp.mpf('0.3'); a = mp.mpf('0.7'); tpole = 2*x*(1 - x)/a
for dt in [mp.mpf('1e-4'), mp.mpf('-1e-4')]:
    t = tpole + dt; dd = mp.mpf('1e-6')
    num = lminus_int(x, t, a, -1, dd)
    # exact finite-d residue at z_Q: the other denominators evaluated at z_Q with the finite d's
    zQ = (t - 1j*dd)/(2*(x - 1))
    resQ = (1 - x)/((-2*(1 - x))*(a*zQ + x + 1j*dd)*(2*x*zQ - t + 1j*dd))
    check('finite-i0 l^- integral near the t-pole (DY time-like, dt=%s) = 2 pi i Res_{z_Q} with Im E(z_Q) > 0' % mp.nstr(dt, 2),
          abs(num - 2j*mp.pi*resQ) < 1e-5*abs(resQ) and mp.im(a*zQ + x + 1j*dd) > 0, 'Im E(z_Q)=%s' % mp.nstr(mp.im(a*zQ + x + 1j*dd), 3))
# (3) complex-c t-integral formula used for the poles on the t contour
e = mp.mpf('-0.3'); c = mp.mpf(2)
f1 = mp.quad(lambda tt: tt**(-1 - e)/(c - tt + 1j*mp.mpf('1e-12')), [0, 1, c - 1e-3, c, c + 1e-3, 3, mp.inf])
# int_0^inf t^{-1-e}/(c - t + i0) dt = -int t^{-1-e}/(t - c - i0) = -(-(-c-i0)^{-1-e} pi/sin(pi e))  with (-c-i0) = c e^{-i pi}
f1_an = c**(-1 - e)*mp.e**(1j*mp.pi*(1 + e))*mp.pi/mp.sin(mp.pi*e)   # (c e^{-i pi})^{-1-e} written with the branch explicit
check('t-integral with a pole on the contour: int t^{-1-e}/(c - t + i0) = c^{-1-e} e^{i pi(1+e)} pi/sin(pi e)', abs(f1 - f1_an) < 1e-6*abs(f1_an),
      '%s vs %s' % (mp.nstr(f1, 10), mp.nstr(f1_an, 10)))

# ---------------------------------------------------------------- (iii) remainder Fourier transform
def Dk(k): return mp.log(1 + k**2) + 2*k*mp.atan(1/k)
check('D(kappa) = exact - limit of int_0^1 F_b(s=+1): ln(1+d^-2)+2d atan(1/d)-2 - (-2 + ln d^-2) = D(d)',
      all(abs((mp.log(1 + dd**-2) + 2*dd*mp.atan(1/dd) - 2) - (-2 + mp.log(dd**-2)) - Dk(dd)) < 1e-30 for dd in [mp.mpf('0.1'), mp.mpf('0.7'), mp.mpf(3)]))
for z in [1, 2, 5, 20, 200]:
    z = mp.mpf(z)
    val = 2*mp.pi*mp.quadosc(lambda k: Dk(k)/k*mp.besselj(0, k*z), [0, mp.inf], zeros=lambda n: mp.besseljzero(0, n)/z)
    print('      FT[D/k^2](z=%s) = %s ; 2 pi^2/z = %s ; difference = %s' % (mp.nstr(z, 4), mp.nstr(val, 14), mp.nstr(2*mp.pi**2/z, 14), mp.nstr(val - 2*mp.pi**2/z, 5)))
    if z >= 20:
        check('FT of the remainder = 2 pi^2/(Lambda_B b_T) at Lambda_B b_T = %s (difference exponentially small)' % mp.nstr(z, 4),
              abs(val - 2*mp.pi**2/z) < 1e-7)
print('\nSUMMARY n20: %d/%d PASS' % (sum(RES), len(RES)))
