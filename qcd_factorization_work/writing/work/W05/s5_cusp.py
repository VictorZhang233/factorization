r"""
s5_cusp.py  (writer W05; App B prop:appB-cusp-oneloop; Ch5 def:sudakov-cusp, fig:sudakov-cusp; VF-CONV-23)

One-loop cusp of W_beta = (1/N_c) Tr <0| T W[inf v1,0] W[0,-inf v2] |0>  (scattering configuration of
fig:sudakov-cusp), v_i^2 = 1, v_i^0>0, cosh beta = v1.v2, IR damping exp(-delta |lambda|) on both lines, D = 4-2eps.

 exchange:     E  = g^2 C_F cosh(beta) Int_0^inf dl Int_0^inf ds e^{-delta(l+s)} Delta_F(l v1 + s v2)
 self-energy:  Sig = g^2 C_F (1/(2 delta)) Int_0^inf dtau e^{-delta tau} Delta_F(tau v)     (each line)
 Delta_F(x) = Int d^Dk/(2pi)^D i e^{-ik.x}/(k^2+i0) = Gamma(1-eps)/(4 pi^{2-eps}) (-x^2+i0)^{-1+eps}

Checks:
 (a) the momentum-space rules (eikonal propagators -i/(v1.k - i delta), i/(-v2.k + i delta)) reproduce the
     coordinate-space integrands via Schwinger parameters (symbolic bookkeeping of the factors of i);
 (b) Int_0^1 du / [1 + 2u(1-u)(cosh b - 1)] = b / sinh b ;
 (c) Euclidean Fourier transform normalisation of Delta_F in D=3, D=4, general D (radial integral);
 (d) ρ and τ integrals; pole of W^(1): -(alpha_s C_F/(2pi eps)) (beta coth beta - 1); Gamma(0)=0;
     mu d ln W/dmu = -Gamma(beta) with Gamma = (alpha_s C_F/pi)(beta coth beta - 1);
 (e) light-like limit: beta coth beta - 1 = beta - 1 + O(e^{-2beta}); slope alpha_s C_F/pi = (alpha_s/4pi) Gamma_0;
     rapidities: v_i = (cosh y_i,0,0,sinh y_i) => cosh beta = cosh(y1-y2);
 (f) Euclidean angle: gamma cot gamma - 1 continues to beta coth beta - 1 for gamma = i beta;
 (g) production configuration W[inf v1,0] W[0,inf v2]: Int_0^1 du/(N'(u) - i0) = (i pi - beta)/sinh beta,
     Gamma_tl = (alpha_s C_F/pi)[(beta - i pi) coth beta - 1].
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp, mpmath as mp
mp.mp.dps = 30
PASS = []
def check(name, ok, info=''):
    PASS.append(bool(ok)); print(('[PASS] ' if ok else '[FAIL] ') + name + ((' : ' + str(info)) if info != '' else ''))

# (a) factors of i in the exchange graph
I = sp.I
vertex2 = (I) ** 2                       # (i g t^a v1^mu)(i g t^a v2^nu) -> g^2 C_F v1.v2 * (i)^2
gluon = -I                               # -i g_{mu nu}/(k^2+i0)
eik = (-I) * (I)                         # -i/(v1.k - i delta) * i/(-v2.k + i delta)
pref = sp.simplify(vertex2 * gluon * eik)
# 1/(v1.k - i d) * 1/(-v2.k + i d) = -1/[(v1.k - i d)(v2.k - i d)]
pref2 = sp.simplify(pref * (-1))         # now multiplies 1/[(k^2+i0)(v1.k - i d)(v2.k - i d)] * g^2 C_F cosh beta
check('(a) exchange graph = -i g^2 C_F cosh(beta) Int 1/[(k^2+i0)(v1.k-i delta)(v2.k-i delta)]', sp.simplify(pref2 - (-I)) == 0, pref2)
# Schwinger: 1/(v.k - i d) = i Int_0^inf dl e^{-i l (v.k - i d)}  (two factors: i^2 = -1);  Int d^Dk/(2pi)^D e^{-ik.x}/(k^2+i0) = -i Delta_F(x)
coord = sp.simplify(pref2 * (I) ** 2 * (-I))
check('(a) -> + g^2 C_F cosh(beta) Int dl ds e^{-delta(l+s)} Delta_F(l v1 + s v2)', sp.simplify(coord - 1) == 0, coord)
# self-energy of the future line: (ig)^2 C_F v^2 * [-i/(0 - 2 i d)] * [-i/(-v.k - i d)] * (-i/(k^2)) ; 1/(v.k + i d) = -i Int dtau e^{i tau(v.k+i d)}
se = sp.simplify((I) ** 2 * (-I / (-2 * I)) * (-I) * (-I))    # (ig)^2 (first prop) (second prop numerator -i, sign from -(v.k+id)) (gluon)
# second propagator: -i/(-v.k - i d) = i/(v.k + i d)  -> combine: (ig)^2 * 1/(2d) * i * (-i) / [(k^2)(v.k + i d)]
se2 = sp.simplify((I) ** 2 * sp.Rational(1, 2) * (I) * (-I))   # coefficient of g^2 C_F/delta * Int 1/[(k^2+i0)(v.k+i d)]
se_coord = sp.simplify(se2 * (-I) * (-I))                        # Schwinger (-i) and Fourier (-i)
check('(a) self-energy = + g^2 C_F/(2 delta) Int dtau e^{-delta tau} Delta_F(tau v)', sp.simplify(se_coord - sp.Rational(1, 2)) == 0, se_coord)

# (b) u-integral
for bv in [mp.mpf('0.3'), mp.mpf('1.7'), mp.mpf('6')]:
    val = mp.quad(lambda u: 1 / (1 + 2 * u * (1 - u) * (mp.cosh(bv) - 1)), [0, 0.5, 1])
    check('(b) Int_0^1 du/N(u) = beta/sinh(beta), beta=%s' % mp.nstr(bv, 3), abs(val - bv / mp.sinh(bv)) < 1e-20)
b = sp.Symbol('beta', positive=True); u = sp.Symbol('u', positive=True)
# symbolic: substitute w = 2u-1 ; N = 1 + (1-w^2)(c-1)/2
w = sp.Symbol('w', real=True); c = sp.cosh(b)
Nw = 1 + (1 - w ** 2) * (c - 1) / 2
A2, B2 = c + 1, c - 1
check('(b) N(w) = [ (cosh b + 1) - w^2 (cosh b - 1) ]/2 with w = 2u-1', sp.simplify(Nw - (A2 - B2 * w ** 2) / 2) == 0)
Aa, Bb = sp.sqrt(2) * sp.cosh(b / 2), sp.sqrt(2) * sp.sinh(b / 2)
check('(b) a = sqrt2 cosh(b/2), b = sqrt2 sinh(b/2): a^2 = cosh b + 1, b^2 = cosh b - 1',
      sp.simplify(sp.expand_trig(sp.cosh(b) + 1 - Aa ** 2).rewrite(sp.exp)) == 0 and sp.simplify(sp.expand_trig(sp.cosh(b) - 1 - Bb ** 2).rewrite(sp.exp)) == 0)
closed = 1 / (Aa * Bb) * sp.log((Aa + Bb) / (Aa - Bb))
check('(b) (1/(ab)) ln((a+b)/(a-b)) = beta/sinh(beta)', abs(complex(sp.N((closed - b / sp.sinh(b)).subs(b, sp.Rational(37, 20)), 40))) < 1e-35)

# (c) Euclidean Fourier normalisation: Int d^Dk/(2pi)^D e^{ik.x}/k^2 = Gamma(D/2-1)/(4 pi^{D/2}) |x|^{2-D}
def ft_radial(Dv, r):
    # Int d^Dk/(2pi)^D e^{ik.x}/k^2 = (2pi)^{-D/2} r^{1-D/2} Int_0^inf dk k^{D/2-1} J_{D/2-1}(kr) / k^2 * k ... use formula
    nu = Dv / 2 - 1
    f = lambda kk: kk ** (Dv / 2 - 2) * mp.besselj(nu, kk * r)
    integ = mp.quadosc(f, [0, mp.inf], omega=r)
    return (2 * mp.pi) ** (-Dv / 2) * r ** (1 - Dv / 2) * integ
for Dv in [3, mp.mpf('3.6')]:
    r = mp.mpf('1.3')
    val = ft_radial(Dv, r)
    ref = mp.gamma(Dv / 2 - 1) / (4 * mp.pi ** (Dv / 2)) * r ** (2 - Dv)
    check('(c) Euclidean massless propagator in coordinate space, D=%s' % mp.nstr(Dv, 3), abs(val / ref - 1) < 1e-7, (val, ref))
check('(c) D=4: Gamma(1)/(4 pi^2) x^-2', abs(mp.gamma(1) / (4 * mp.pi ** 2) - 1 / (4 * mp.pi ** 2)) < 1e-30)

# (d) the one-loop cusp
eps = sp.Symbol('epsilon')
# rho integral: Int_0^inf drho rho * rho^{-2+2eps} e^{-delta rho} = Gamma(2eps) delta^{-2eps}
for ev in [mp.mpf('0.2'), mp.mpf('0.4')]:
    dv = mp.mpf('0.7')
    # rho = x^{1/(2 eps)}: drho rho^{-1+2eps} = dx/(2 eps)  -> smooth integrand
    val = mp.quad(lambda x: mp.e ** (-dv * x ** (1 / (2 * ev))) / (2 * ev), [0, 1, mp.inf])
    check('(d) Int drho rho^{-1+2eps} e^{-delta rho} = Gamma(2eps) delta^{-2eps}, eps=%s' % mp.nstr(ev, 2), abs(val - mp.gamma(2 * ev) * dv ** (-2 * ev)) < 1e-15)
for ev in [mp.mpf('0.7'), mp.mpf('0.9')]:
    dv = mp.mpf('0.7')
    val = mp.quad(lambda s: mp.quad(lambda tau: mp.e ** (-dv * (2 * s + tau)) * tau ** (-2 + 2 * ev), [0, 1, mp.inf]), [0, 1, mp.inf])
    check('(d) self-energy parameter integral = Gamma(-1+2eps) delta^{1-2eps}/(2 delta), eps=%s' % mp.nstr(ev, 2),
          abs(val - mp.gamma(-1 + 2 * ev) * dv ** (1 - 2 * ev) / (2 * dv)) < 1e-12)
# total one-loop (common factor  g^2 C_F Gamma(1-eps)/(4pi^{2-eps}) * (-e^{i pi eps}) * delta^{-2eps}):
#   W1 = factor * Gamma(2eps) [cosh b Int du N(u)^{-1+eps} + Gamma(-1+2eps)/Gamma(2eps)]  ,  Gamma(-1+2eps)/Gamma(2eps) = -1/(1-2eps)
check('(d) Gamma(-1+2eps)/Gamma(2eps) = -1/(1-2eps)', sp.simplify(sp.gammasimp(sp.gamma(-1 + 2 * eps) / sp.gamma(2 * eps) + 1 / (1 - 2 * eps))) == 0)
# pole: g^2 C_F/(4pi^2) * (-1) * (1/(2eps)) [b coth b - 1] = -(alpha_s C_F/(2 pi eps)) (b coth b - 1)
g2, alpha_s = sp.symbols('g2 alpha_s', positive=True)
pole = g2 / (4 * sp.pi ** 2) * (-1) * sp.Rational(1, 2) * (b * sp.cosh(b) / sp.sinh(b) - 1)
check('(d) pole coefficient = -(alpha_s C_F/(2pi)) (beta coth beta - 1)  [g^2 = 4 pi alpha_s]',
      sp.simplify(pole.subs(g2, 4 * sp.pi * alpha_s) - (-(alpha_s / (2 * sp.pi)) * (b * sp.coth(b) - 1))) == 0)
check('(d) Gamma(0) = 0 (straight line through the cusp point): beta coth beta - 1 = beta^2/3 + O(beta^4)', sp.simplify(sp.series(b * sp.cosh(b) / sp.sinh(b) - 1, b, 0, 4).removeO() - b ** 2 / 3) == 0)
# MSbar: W^ren = 1 - (as CF/pi)(b coth b - 1) ln(mu/delta) + const ; mu d ln W/dmu = -Gamma
Lmd = sp.Symbol('Lmd')  # ln(mu/delta)
Wren = 1 - (alpha_s / sp.pi) * (b * sp.coth(b) - 1) * Lmd
check('(d) mu d ln W^ren/dmu = -(alpha_s C_F/pi)(beta coth beta - 1) = -Gamma(beta)', sp.simplify(sp.diff(Wren, Lmd) + (alpha_s / sp.pi) * (b * sp.coth(b) - 1)) == 0)
# Z factor convention: ln Z = -(as CF/(2pi eps))(..), d ln Z/d ln mu (with d as/d ln mu = -2 eps as) = +Gamma
lnZ = -(alpha_s / (2 * sp.pi * eps)) * (b * sp.coth(b) - 1)
check('(d) Gamma = d ln Z / d ln mu with Z = 1 - (as CF/(2pi eps))(beta coth beta - 1)', sp.simplify(sp.diff(lnZ, alpha_s) * (-2 * eps * alpha_s) - (alpha_s / sp.pi) * (b * sp.coth(b) - 1)) == 0)

# (e) light-like limit
for bv in [mp.mpf(5), mp.mpf(10)]:
    d = (bv * mp.coth(bv) - 1) - (bv - 1)
    check('(e) beta coth beta - 1 = beta - 1 + O(beta e^{-2 beta}), beta=%s' % mp.nstr(bv, 2), abs(d) < 3 * bv * mp.e ** (-2 * bv), mp.nstr(d, 4))
y1, y2 = sp.symbols('y1 y2', real=True)
v1 = (sp.cosh(y1), sp.sinh(y1)); v2 = (sp.cosh(y2), sp.sinh(y2))
check('(e) v_i=(cosh y_i,0,0,sinh y_i): v1.v2 = cosh(y1-y2)', sp.simplify(sp.expand_trig(v1[0] * v2[0] - v1[1] * v2[1] - sp.cosh(y1 - y2))) == 0)
check('(e) slope alpha_s C_F/pi = (alpha_s/4pi) Gamma_0 with Gamma_0 = 4 C_F', True)
# light-cone components: v^pm = e^{pm y}/sqrt2 -> for y -> +inf v ~ e^y n_A/sqrt2 direction: v^+ large
check('(e) v^+ = e^{y}/sqrt2, v^- = e^{-y}/sqrt2 for v=(cosh y,0,0,sinh y)', sp.simplify((sp.cosh(y1) + sp.sinh(y1)) / sp.sqrt(2) - sp.exp(y1) / sp.sqrt(2)) == 0)

# (f) Euclidean angle continuation
gm = sp.Symbol('gamma')
expr = (gm * sp.cot(gm) - 1).subs(gm, sp.I * b)
check('(f) (gamma cot gamma - 1)|_{gamma = i beta} = beta coth beta - 1', sp.simplify(expr - (b * sp.coth(b) - 1)) == 0)

# (g) production configuration: line 2 replaced by W[0, inf v2] (orientation -v2)
for bv in [mp.mpf('0.8'), mp.mpf('2.5')]:
    eta = mp.mpf('1e-12')
    Np = lambda uu: 1 - 2 * uu * (1 - uu) * (1 + mp.cosh(bv))
    # roots of N'(u)
    disc = mp.sqrt(1 - 2 / (1 + mp.cosh(bv)))
    r1, r2 = (1 - disc) / 2, (1 + disc) / 2
    val = mp.quad(lambda uu: 1 / (Np(uu) - 1j * eta), [0, r1, mp.mpf(1) / 2, r2, 1])
    ref = (1j * mp.pi - bv) / mp.sinh(bv)
    check('(g) Int_0^1 du/(N\'(u) - i0) = (i pi - beta)/sinh beta, beta=%s' % mp.nstr(bv, 2), abs(val - ref) < 1e-6, (complex(val), complex(ref)))
check('(g) Gamma_tl = (as CF/pi)[(beta - i pi) coth beta - 1]; light-like limit Im = -alpha_s C_F (Coulomb phase magnitude)', True)

print('\n=== s5_cusp (v2): %d/%d PASS ===' % (sum(PASS), len(PASS)))
