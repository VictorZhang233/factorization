# N20 (stage-2 verifier): one-loop TMD vertex graph with a non-light-like Wilson line, by two methods that
# differ from the project's (Feynman x + Schwinger lambda with l = l'+xp+-lambda n/2) and from stage 1
# (light-cone residues):
#  (A) the DY-SIDIS DIFFERENCE directly from 1/(n.l+i0) - 1/(n.l-i0) = -2 pi i delta(n.l):
#      time-like n: rest frame of n, delta(l^0) -> Euclidean (D-1)-dim integral with one "on-shell" propagator;
#      space-like n: delta(l_z) -> Minkowski (D-1)-dim bubble.  Closed forms derived by hand (see batch_N18_s2.md §4)
#      and compared with the claimed phases.
#  (B) V_SIDIS (time-like) and V_DY (time-like and space-like) directly, with my own Feynman/Schwinger
#      parametrisation and the rescaling lambda = (x/|a|) u (different substitution from the project's).
#  (C) the 2 pi^2, the light-like limit, and the Fourier transform of the real-graph remainder D(kappa)
#      via the exact representation FT(z) = 4 pi int_0^inf sin(s) arcsinh(s/z)/s^2 ds (derived here).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import sympy as sp
mp.mp.dps = 40
res = []
def check(name, cond, info=''):
    res.append(bool(cond)); print(('PASS ' if cond else 'FAIL ') + name + (('   [' + info + ']') if info else ''))

G = mp.gamma
def B(a, b): return G(a)*G(b)/G(a + b)
ipi = 1j*mp.pi
# normalisation: V = (alpha_s C_F/4pi) * X^eps * c(eps),  X = pi mu^2 |n^2|/(p.n)^2 (common to all four cases)
def c_time(e):        # claimed closed form (project and stage 1)
    return -G(1 - e)*G(1 + 2*e)*(1 - e)/((1 - 2*e)*e**2)

# ---------------- (B) my Feynman/Schwinger derivation ----------------
# V_sigma = 4 g^2 C_F mu^{2eps} Gamma(1+eps)/(4pi)^{2-eps} * K_sigma, with (p.n=1, n^2=2a, p^+=n^-=1):
#   K_SIDIS = -int_0^1dx int_0^inf dlam (1-x-a lam) (2x lam + 2a lam^2 - i0)^{-1-eps}
#   K_DY    = +int_0^1dx int_0^inf dlam (1-x+a lam) (-2x lam + 2a lam^2 - i0)^{-1-eps}
# substitute lam = (x/|a|) u.  Then V = (alpha_s C_F/4pi) (2 pi mu^2 |a|)^eps * 2^{2+eps} Gamma(1+eps) |a|^{-eps} K.
def K_S_time(e):
    return -2**(-1 - e)*(B(-2*e, 2)*B(-e, 1 + 2*e) - B(1 - e, 2*e)/(1 - 2*e))
def K_D_time(e):
    ph = mp.exp(ipi*(1 + e))
    return 2**(-1 - e)*(B(-2*e, 2)*(B(-e, 1 + 2*e) + ph*B(-e, -e)) + (B(-e, 2*e) + ph*B(1 - e, -e))/(1 - 2*e))
def K_S_space(e):
    ph = mp.exp(ipi*(1 + e))
    return -2**(-1 - e)*(B(-2*e, 2)*(B(-e, -e) + ph*B(-e, 1 + 2*e)) + (B(1 - e, -e) + ph*B(-e, 2*e))/(1 - 2*e))
def K_D_space(e):
    ph = mp.exp(ipi*(1 + e))
    return 2**(-1 - e)*ph*(B(-2*e, 2)*B(-e, 1 + 2*e) - B(1 - e, 2*e)/(1 - 2*e))
def c_from_K(K, e):   # V/(alpha_s C_F/4pi)/X^eps
    return 2**(2 + e)*G(1 + e)*K
eps_list = [mp.mpf('0.17'), mp.mpf('-0.23'), mp.mpf('0.41'), mp.mpf('-0.07'), mp.mpf('0.013'), mp.mpf('0.3'), mp.mpf('-0.41')]
for e in eps_list:
    cS = c_from_K(K_S_time(e), e); cD = c_from_K(K_D_time(e), e)
    cSs = c_from_K(K_S_space(e), e); cDs = c_from_K(K_D_space(e), e)
    ct = c_time(e)
    ok = (abs(cS - ct) < 1e-30*abs(ct) and abs(cD - mp.exp(2*ipi*e)*ct) < 1e-30*abs(ct)
          and abs(cSs - mp.exp(-ipi*e)*ct) < 1e-30*abs(ct) and abs(cDs - mp.exp(ipi*e)*ct) < 1e-30*abs(ct))
    check('eps=%s: own Feynman/Schwinger: V_SIDIS^time = V^time (real), V_DY^time = e^{2 pi i eps} V^time, V_SIDIS^space = e^{-i pi eps} V^time, V_DY^space = e^{+i pi eps} V^time'
          % mp.nstr(e, 3), ok, 'c_time=%s' % mp.nstr(ct, 12))
    check('eps=%s: space-like V_SIDIS = conj(V_DY)' % mp.nstr(e, 3), abs(cSs - mp.conj(cDs)) < 1e-30*abs(ct))

# ---------------- (A) the delta-function (difference) method ----------------
# time-like, rest frame of n:  Delta = V_DY - V_SIDIS = 2 pi g^2 C_F mu^{2eps} int d^Dl/(2pi)^D N delta(n.l)/[(l^2+i0)((p-l)^2+i0)]
#   = -i e^{i pi eps} (alpha_s C_F/(2 sqrt(pi))) (4 pi mu^2 n^2/(p.n)^2)^eps Gamma(1/2+eps)(1-eps)/(eps(1-2eps))     [hand derivation]
# in units (alpha_s C_F/4pi) X^eps, X = pi mu^2 n^2/(p.n)^2:   dc_time = -i e^{i pi eps} 2 sqrt(pi) 4^eps Gamma(1/2+eps)(1-eps)/(eps(1-2eps))
def dc_time(e):
    return -1j*mp.exp(ipi*e)*2*mp.sqrt(mp.pi)*4**e*G(mp.mpf(1)/2 + e)*(1 - e)/(e*(1 - 2*e))
def dc_space(e):     # space-like: Minkowski bubble on the hyperplane l_z = 0 (hand derivation): dc_space = e^{-i pi eps} dc_time
    return -1j*2*mp.sqrt(mp.pi)*4**e*G(mp.mpf(1)/2 + e)*(1 - e)/(e*(1 - 2*e))
for e in eps_list:
    ct = c_time(e)
    a1 = abs(dc_time(e) - (mp.exp(2*ipi*e) - 1)*ct) < 1e-30*abs(ct)
    a2 = abs(dc_space(e) - (mp.exp(ipi*e) - mp.exp(-ipi*e))*ct) < 1e-30*abs(ct)
    check('eps=%s: delta-function method: time-like V_DY-V_SIDIS = (e^{2pi i eps}-1)V^time; space-like = 2i sin(pi eps) V^time (purely imaginary)' % mp.nstr(e, 3), a1 and a2)
# analytic identity behind (A): ratio = pi eps/(sin(pi eps) Gamma(1-eps) Gamma(1+eps)) = 1 (duplication + reflection)
es = sp.symbols('epsilon')
ratio = (4**es*sp.gamma(sp.Rational(1, 2) + es)*sp.sqrt(sp.pi)*es)/(sp.sin(sp.pi*es)*sp.gamma(1 - es)*sp.gamma(1 + 2*es))
r2 = sp.simplify(sp.gammasimp(sp.expand_func(ratio.rewrite(sp.gamma))))
num_ok = all(abs(complex(ratio.subs(es, v)) - 1) < 1e-14 for v in (0.1, -0.27, 0.33, 0.049))
check('Gamma identity 4^eps sqrt(pi) Gamma(1/2+eps) eps = sin(pi eps) Gamma(1-eps) Gamma(1+2eps) (symbolic: %s; numeric)' % r2, num_ok)
# sub-step: Euclidean d-dim integral with M^2 = -x^2 - i0:  int d^dk/(k^2 - x^2 - i0)^2 = pi^{d/2} Gamma(2-d/2) (-x^2-i0)^{d/2-2}
# checked numerically at d = 3 - 2eps with eps = 0.2 (convergent for d<4) using radial integration with a finite i0:
for e in (mp.mpf('0.2'), mp.mpf('0.35')):
    d = 3 - 2*e; x = mp.mpf('0.7'); eta = mp.mpf('1e-12')
    Sd = 2*mp.pi**(d/2)/G(d/2)
    f = lambda k: Sd*k**(d - 1)/(k**2 - x**2 - 1j*eta)**2
    # integrate around the pole by deforming k -> k e^{-i theta}?  use contour: k from 0 to inf along the ray arg = -0.3 (no poles crossed: pole at k=x+i0' is above)
    th = mp.mpf('-0.3'); w = mp.exp(1j*th)
    val = mp.quad(lambda r: Sd*(r*w)**(d - 1)*w/((r*w)**2 - x**2)**2, [0, 1, mp.inf])
    target = mp.pi**(d/2)*G(2 - d/2)*mp.exp(-ipi*(d/2 - 2))*x**(d - 4)
    check('(d-1)-dim Euclidean integral with -i0 mass term (eps=%s): contour value = pi^{d/2}Gamma(2-d/2)(-x^2-i0)^{d/2-2}' % mp.nstr(e, 3),
          abs(val - target) < 1e-25*abs(target))

# ---------------- (C) 2 pi^2, light-like limit, Fourier transform of the remainder ----------------
for e in (mp.mpf('1e-6'), mp.mpf('-1e-6'), mp.mpf('1e-9')):
    ct = c_time(e)
    d = (mp.re(mp.exp(2*ipi*e)*ct) - ct)
    check('Re V_DY - V_SIDIS (time-like) -> 2 pi^2 (alpha_s C_F/4pi) at eps=%s' % mp.nstr(e, 3), abs(d - 2*mp.pi**2) < 1e-4, mp.nstr(d, 12))
# series coefficients
x = sp.symbols('x')
ser = sp.series(-2*sp.sin(sp.pi*x)**2*(-sp.gamma(1 - x)*sp.gamma(1 + 2*x)*(1 - x)/((1 - 2*x)*x**2)), x, 0, 2).removeO()
check('series: Re V_DY - V_SIDIS = (alpha_sC_F/4pi)[2pi^2 + 2pi^2(1-gamma_E)eps + O(eps^2)]  (X^eps factor not expanded)',
      sp.simplify(ser - (2*sp.pi**2 + 2*sp.pi**2*(1 - sp.EulerGamma)*x)) == 0, str(sp.simplify(ser)))
ser_im = sp.series(sp.sin(2*sp.pi*x)*(-sp.gamma(1 - x)*sp.gamma(1 + 2*x)*(1 - x)/((1 - 2*x)*x**2)), x, 0, 1).removeO()
check('Im V_DY^time = (alpha_sC_F/4pi)[-2pi/eps + ...]: divergent Coulomb phase', sp.simplify(sp.limit(ser_im*x, x, 0) + 2*sp.pi) == 0, str(sp.simplify(ser_im)))
# light-like limit: |X^eps| -> 0 as |n^2| -> 0 for Re eps > 0
check('light-like limit taken first: |(|n^2|)^eps| -> 0 for Re eps>0 (e.g. eps=0.1, |n^2|=1e-40: %s)' % mp.nstr(mp.mpf('1e-40')**0.1, 3), mp.mpf('1e-40')**0.1 < 1e-3)

# remainder D(kappa) = ln(1+k^2) + 2 k arctan(1/k): exact minus limit of int_0^1 F_b(s=+1)
for dl in (mp.mpf('0.3'), mp.mpf('0.01'), mp.mpf(2)):
    exact = mp.log(1 + dl**-2) + 2*dl*mp.atan(1/dl) - 2
    limit = -2 + mp.log(1/dl**2)
    check('D(delta) = exact - limit of int_0^1 F_b (delta=%s)' % mp.nstr(dl, 3), abs((exact - limit) - (mp.log(1 + dl**2) + 2*dl*mp.atan(1/dl))) < 1e-30)
    # and int_0^1 F_b computed by quadrature
    q = mp.quad(lambda xx: 2*xx*(1 - xx)/((1 - xx)**2 + dl**2), [0, 1])
    check('int_0^1 2x(1-x)/((1-x)^2+delta^2) dx = ln(1+delta^-2)+2 delta arctan(1/delta)-2 (delta=%s)' % mp.nstr(dl, 3), abs(q - exact) < 1e-25)
Dk = lambda k: mp.log(1 + k**2) + 2*k*mp.atan(1/k)
mp.mp.dps = 25
def FT_hankel(z):
    return 2*mp.pi*mp.quadosc(lambda k: mp.besselj(0, k*z)*Dk(k)/k, [0, mp.inf], omega=z)
def FT_rep(z):
    return 4*mp.pi*mp.quadosc(lambda s: mp.sin(s)*mp.asinh(s/z)/s**2, [0, mp.inf], omega=1)
print('   z = Lambda_B b_T :  FT (Hankel)        FT (sin-arcsinh rep.)   2pi^2/z        difference')
for z in (mp.mpf('0.5'), mp.mpf(1), mp.mpf(2), mp.mpf(5), mp.mpf(10), mp.mpf(20)):
    h = FT_hankel(z); r = FT_rep(z); a = 2*mp.pi**2/z
    print('   %5s            %s   %s   %s   %s' % (mp.nstr(z, 3), mp.nstr(h, 14), mp.nstr(r, 14), mp.nstr(a, 14), mp.nstr(h - a, 6)))
    check('FT(z=%s): Hankel transform = exact representation 4pi int sin(s) arcsinh(s/z)/s^2' % mp.nstr(z, 3), abs(h - r) < 1e-10*abs(a))
    if z <= 2:
        check('FT(z=%s) differs from 2pi^2/z by %s: the equality is NOT exact' % (mp.nstr(z, 3), mp.nstr(h - a, 4)), abs(h - a) > 1e-2)
    if z >= 10:
        check('FT(z=%s) = 2pi^2/z up to %s (exponentially small)' % (mp.nstr(z, 3), mp.nstr(h - a, 3)), abs(h - a) < 1e-3*mp.exp(-z/2))
# exponential decay rate of the difference
d5 = FT_rep(mp.mpf(5)) - 2*mp.pi**2/5; d10 = FT_rep(mp.mpf(10)) - 2*mp.pi**2/10
print('   ln|diff(5)/diff(10)|/5 = %s  (rate ~1 => O(e^{-z}) up to powers)' % mp.nstr(mp.log(abs(d5/d10))/5, 6))
print('\nSUMMARY: %d/%d checks passed' % (sum(res), len(res)))
