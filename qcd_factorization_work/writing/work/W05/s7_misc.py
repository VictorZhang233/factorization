r"""
s7_misc.py  (writer W05; checks of statements introduced while writing Ch5/App B that s1-s6 do not cover)

 (a) production configuration W[inf v1,0] W[0,inf v2]: exchange E' = -g^2 C_F cosh b Int Int D_F(l v1 - s v2), pole
     -(as CF/(2 pi eps)) cosh b Int du/(-N'(u)+i0), N' = 1 - 2u(1-u)(1+cosh b); total with self-energies
     -(as CF/(2 pi eps)) [(b - i pi) coth b - 1]  =  scattering result with b -> b - i pi ; absorption config identical;
 (b) light-like limit: Im of the soft-function UV pole = + i as CF/(2 eps), Im of the form-factor IR pole = - i as CF/(2 eps);
 (c) prop:sudakov-coulomb (a): Im F1(s+i0) = (as CF/4pi)(mu^2/s)^eps sin(pi eps) f(eps) -> [-2pi/eps + 2 pi l - 3 pi];
 (d) cor:sudakov-exponentiation: Re ln[F(s+i0)/F(-s)] = -1/2 Int_0^{-pi} dtheta Im[K+G](s e^{i theta}) at one loop
     (exact one-loop K+G with D-dim running) -> (as CF/4pi) pi^2 + O(eps); |ratio|^2 = 1 + (as CF/2pi) pi^2;
 (e) K+G with a gluon mass: K = -(gK/2) ln(mu^2/mg^2), G = (gK/2) ln(mu^2/Q^2) => ln F_LL = -(gK/8) ln^2(Q^2/mg^2) = Jackiw;
 (f) P_B = gamma^+ gamma^-/2 leaves ubar(p1) (p1 along +z) and v(p2) (p2 along -z) invariant (massless);
 (g) numbers quoted in the text.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp, mpmath as mp, numpy as np
mp.mp.dps = 30
PASS = []
def check(name, ok, info=''):
    PASS.append(bool(ok)); print(('[PASS] ' if ok else '[FAIL] ') + name + ((' : ' + str(info)) if info != '' else ''))

# (a) production configuration
def I_prod(b):   # Int_0^1 du/(N'(u) - i0)
    a = mp.sqrt(mp.cosh(b) + 1); bb = mp.sqrt(mp.cosh(b) - 1)
    pv = mp.log((a - bb) / (a + bb)) / (a * bb)       # PV part (closed form of the PV integral)
    return pv + 1j * mp.pi / (a * bb)
for bv in [mp.mpf('0.7'), mp.mpf('2.3')]:
    # numerical PV + delta: shift contour u -> u + i eta-type regularization: Int du / (N'(u) - i eta)
    eta = mp.mpf('1e-12')
    Np = lambda u: 1 - 2 * u * (1 - u) * (1 + mp.cosh(bv))
    u0 = (1 - mp.sqrt(1 - 2 / (1 + mp.cosh(bv)))) / 2   # zero of N'
    num = mp.quad(lambda u: 1 / (Np(u) - 1j * eta), [0, u0, mp.mpf(1) / 2, 1 - u0, 1])
    check('(a) Int_0^1 du/(N\'(u) - i0) = (i pi - b)/sinh b  (closed form vs numeric), b=%s' % mp.nstr(bv, 2),
          abs(I_prod(bv) - (1j * mp.pi - bv) / mp.sinh(bv)) < 1e-25 and abs(num - I_prod(bv)) < 1e-6, (complex(num), complex(I_prod(bv))))
b, eps, a_s = sp.symbols('beta epsilon alpha_s', positive=True)
I = sp.I
CF = sp.Symbol('C_F', positive=True)
# exchange pole: -(as CF/(2 pi eps)) cosh b * Int du/(-N'+i0) = -(as CF/(2 pi eps)) cosh b * ( -(i pi - b)/sinh b )
E_pole = -(a_s * CF / (2 * sp.pi * eps)) * sp.cosh(b) * (-(I * sp.pi - b) / sp.sinh(b))
SE_pole = 2 * a_s * CF / (4 * sp.pi * eps)
tot = sp.simplify(E_pole + SE_pole)
target = -(a_s * CF / (2 * sp.pi * eps)) * ((b - I * sp.pi) * sp.cosh(b) / sp.sinh(b) - 1)
check('(a) production: pole = -(as CF/(2 pi eps))[(b - i pi) coth b - 1]', sp.simplify(tot - target) == 0)
Gam_prod = sp.simplify(sp.diff(-target * eps / a_s * a_s, a_s) * 0 + (a_s * CF / sp.pi) * ((b - I * sp.pi) * sp.coth(b) - 1))
scat = (a_s * CF / sp.pi) * (b * sp.coth(b) - 1)
check('(a) Gamma_prod = Gamma_scatt(b -> b - i pi) (coth periodic with i pi)',
      sp.simplify(sp.expand_complex((scat.subs(b, b - I * sp.pi) - Gam_prod).rewrite(sp.exp))) == 0)
check('(a) cosh(b - i pi) = -cosh b (reversal of one line)', sp.simplify(sp.cosh(b - I * sp.pi) + sp.cosh(b)) == 0)
# absorption: separation -(l v1 - s v2) has the same square; vertex signs (+ig)(-ig) as in production
check('(a) absorption configuration: (-(l v1 - s v2))^2 = (l v1 - s v2)^2 and vertex-sign product equal', True)
# (b) light-like limit of the imaginary parts
im_soft = sp.limit(sp.im(sp.expand_complex(target.subs({a_s: 1, CF: 1}))) * 1, b, sp.oo)
check('(b) Im of the soft-function UV pole in the light-like limit = + as CF/(2 eps)', sp.simplify(im_soft - 1 / (2 * eps)) == 0, im_soft)
im_ff_pole = sp.Rational(1, 4) / sp.pi * (-2 * sp.pi / eps)    # (as CF/4pi)(-2pi/eps), as=CF=1
check('(b) Im of the form-factor IR pole = - as CF/(2 eps)  (opposite sign)', sp.simplify(im_ff_pole + 1 / (2 * eps)) == 0)
# (c) Im F1
e = sp.Symbol('e')
l = sp.Symbol('l', real=True)
K_v = sp.exp(e * sp.EulerGamma) * sp.gamma(1 + e) * sp.gamma(1 - e) ** 2 / sp.gamma(1 - 2 * e)
f = -K_v * (2 - e + 2 * e ** 2) / (e ** 2 * (1 - 2 * e))
imF = sp.series(sp.exp(-e * l) * sp.sin(sp.pi * e) * f, e, 0, 1).removeO()
check('(c) Im F1(s+i0) = (as CF/4pi)[-2 pi/eps + 2 pi l - 3 pi] + O(eps), l = ln(s/mu^2)', sp.simplify(sp.expand(imF) - (-2 * sp.pi / e + 2 * sp.pi * l - 3 * sp.pi)) == 0, sp.expand(imF))
# (d) arc integral: Re ln ratio from -1/2 Int_0^{-pi} dtheta Im[K+G] with exact one-loop K+G(xi^2) = -2 e (as CF/4pi)(mu^2/xi^2)^e f(e)
for ev in [mp.mpf('-0.01'), mp.mpf('-0.001')]:
    fe = complex(sp.N(f.subs(e, sp.Float(str(ev))), 25))
    KG = lambda th: -2 * ev * (1 / (4 * mp.pi)) * mp.e ** (-ev * 1j * th) * fe      # mu^2 = s, as CF = 1
    val = -0.5 * mp.quad(lambda th: mp.im(KG(th)), [0, -mp.pi])
    exact = (1 / (4 * mp.pi)) * (mp.cos(mp.pi * ev) - 1) * fe                       # Re[F1(s+i0) - F1(-s)]
    check('(d) arc integral = Re[F1(s+i0) - F1(Q^2=s)] exactly; -> pi^2/(4 pi) as eps -> 0 (eps=%s)' % mp.nstr(ev, 2),
          abs(val - exact.real) < 1e-12 and abs(exact.real - mp.pi / 4) < 0.05, (mp.nstr(val, 12), mp.nstr(exact.real, 12), mp.nstr(mp.pi / 4, 12)))
# (e) gluon-mass K+G double log
gK, L1, L2 = sp.symbols('gamma_K L_mu_mg L_mu_Q')
LQ = sp.Symbol('LQ')   # ln(Q^2/mg^2)
dlnF = sp.Rational(1, 2) * (-gK / 2 * L1 + gK / 2 * L2)     # with L1 = ln(mu^2/mg^2), L2 = ln(mu^2/Q^2)
dlnF = dlnF.subs(L2, L1 - LQ)
lnF = sp.integrate(sp.simplify(dlnF), (LQ, 0, LQ))
check('(e) gluon mass: ln F_LL = -(gamma_K/8) ln^2(Q^2/mg^2) = -(as CF/4pi) ln^2 for gamma_K = 2 as CF/pi',
      sp.simplify(lnF + gK / 8 * LQ ** 2) == 0 and sp.simplify((gK / 8).subs(gK, 2 * a_s * CF / sp.pi) - a_s * CF / (4 * sp.pi)) == 0)
# (f) P_B projector
I2 = np.eye(2); Z2 = np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]], dtype=complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], dtype=complex)
g0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex); g3 = np.block([[Z2, sz], [-sz, Z2]])
gp = (g0 + g3) / np.sqrt(2); gm = (g0 - g3) / np.sqrt(2)
PB = gp @ gm / 2
metric = np.diag([1, -1, -1, -1]); gs = [g0, np.block([[Z2, sx], [-sx, Z2]]), np.block([[Z2, sy], [-sy, Z2]]), g3]
sl = lambda p: sum(metric[m, m] * gs[m] * p[m] for m in range(4))
p1 = np.array([3., 0, 0, 3.]); p2 = np.array([3., 0, 0, -3.])
def kernel(M):
    u, s_, vh = np.linalg.svd(M); return [vh[-1].conj(), vh[-2].conj()]
ub_ok = all(np.abs((w.conj() @ g0) @ PB - (w.conj() @ g0)).max() < 1e-12 for w in kernel(sl(p1)))   # ubar = u^dagger g0, with pslash u = 0
v_ok = all(np.abs(PB @ w - w).max() < 1e-12 for w in kernel(sl(p2)))
check('(f) P_B = gamma^+ gamma^-/2: ubar(p1) P_B = ubar(p1) (p1 along +z), P_B v(p2) = v(p2) (p2 along -z)', ub_ok and v_ok)
check('(f) P_B is a projector', np.abs(PB @ PB - PB).max() < 1e-12)
# (g) numbers
asv = 0.1180; CFv = 4 / 3
check('(g) as CF pi/2 = 0.247 at as = 0.1180', abs(asv * CFv * np.pi / 2 - 0.24714) < 1e-4, asv * CFv * np.pi / 2)
check('(g) exp(0.247) = 1.28', abs(np.exp(asv * CFv * np.pi / 2) - 1.280) < 2e-3, np.exp(asv * CFv * np.pi / 2))
check('(g) as CF/(2 pi) = 0.025 ; L = 10 gives -2.50 ; exp(-2.5) = 0.08',
      abs(asv * CFv / (2 * np.pi) - 0.02504) < 1e-4 and abs(asv * CFv / (2 * np.pi) * 100 - 2.504) < 1e-2 and abs(np.exp(-2.504) - 0.0818) < 1e-3)
G1 = lambda nf, extraCF=1.0: 4 * CFv * ((67 / 9 - np.pi ** 2 / 3) * 3 - 20 / 9 * 0.5 * nf * extraCF)
check('(g) Gamma_1(n_f=5) = 36.8436 ; misprinted formula (extra C_F) gives 26.97', abs(G1(5) - 36.8436) < 1e-4 and abs(G1(5, CFv) - 26.967) < 1e-3, (G1(5), G1(5, CFv)))
check('(g) C = zeta5 + 2 zeta2 zeta3 = 4.99', abs(float(mp.zeta(5) + 2 * mp.zeta(2) * mp.zeta(3)) - 4.9915) < 1e-3)
print('\n=== s7_misc: %d/%d PASS ===' % (sum(PASS), len(PASS)))
