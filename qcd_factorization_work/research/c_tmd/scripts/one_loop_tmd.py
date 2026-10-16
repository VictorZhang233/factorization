# Assembly of the one-loop TMD of a quark in an on-shell massless quark (Collins 2011 definition),
# with all intermediate objects made explicit.  Conventions: CONTEXT.md (binding) + DERIVATION.md Sec.1.
#
# Inputs proved elsewhere in this directory:
#   real_graphs.py   : real-graph integrands F_a, F_b, F_c (exact, general Wilson-line direction n_B(y_B))
#   soft_factor.py   : one-loop soft factor, rapidity integrals 4(Y coth Y - sigma)
#   virtual_vertex.py: virtual vertex graph ~ (|n_B^2|)^eps -> 0 in the light-like limit taken first
#   ft_check.py      : d-dimensional Fourier transform of (k^2)^(-1-eta)
# Notation: a = alpha_s C_F/(2 pi);  c_S = g^2 mu^{2eps} C_F/(2pi)^{3-2eps};  p(x) = (1+x^2)[1/(1-x)]_+ ;
#   L_b = ln(mu^2 b^2/b0^2), b0 = 2 e^{-gE};  l_z = ln(zeta/mu^2);  delta^2 = e^{2 y_B} kT^2/(2 p+^2).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
ok = True
x, u, d = sp.symbols('x u delta', positive=True)
eps, Lb, lz, eta = sp.symbols('epsilon L_b l_zeta eta')
gE = sp.EulerGamma

# ---------------------------------------------------------------------------------------------
# 1. rapidity-regulated real graphs -> distributions (analytic, sympy)
#   F_b = 2x(1-x)/((1-x)^2 + s delta^2),  F_c = -2 s delta^2 (1-x)/((1-x)^2 + s delta^2)^2   (s=+1 time-like, -1 space-like)
#   claim: F_b -> 2x[1/(1-x)]_+ + delta(1-x) ln(1/delta^2) ;  F_c(time-like) -> -delta(1-x) ;  both up to O(delta)
Ib_t = sp.integrate(2 * (1 - u) * u / (u**2 + d**2), (u, 0, 1))            # int_0^1 F_b dx (u = 1-x), time-like
Ib_s = sp.log(1 - d**2) - sp.log(d**2) - 2 - d * sp.log((1 - d) / (1 + d))  # PV int, space-like (antiderivative in DERIVATION.md)
# verify the space-like PV antiderivative numerically
import mpmath as mp
dv = mp.mpf('0.013')
pvnum = mp.quad(lambda uu: 2 * (1 - uu) * uu / ((uu - dv) * (uu + dv)), [0, dv - mp.mpf('1e-9')]) + \
        mp.quad(lambda uu: 2 * (1 - uu) * uu / ((uu - dv) * (uu + dv)), [dv + mp.mpf('1e-9'), 1])
pv_formula = mp.log(1 - dv**2) - mp.log(dv**2) - 2 - dv * mp.log((1 - dv) / (1 + dv))
print('1. int_0^1 F_b (time-like) =', sp.simplify(Ib_t))
print('   small-delta expansion       =', sp.series(Ib_t, d, 0, 2))
print('   PV int_0^1 F_b (space-like): numeric %s, formula %s (excision 1e-9)' % (mp.nstr(pvnum, 10), mp.nstr(pv_formula, 10)))
ok &= abs(pvnum - pv_formula) < 1e-6
ok &= sp.simplify(sp.series(Ib_t, d, 0, 1).removeO() - (-2 * sp.log(d) - 2)) == 0
Ic_t = sp.integrate(-2 * d**2 * u / (u**2 + d**2)**2, (u, 0, 1))
print('   int_0^1 F_c (time-like) =', sp.simplify(Ic_t), ' -> -1 + O(delta^2): concentrated at 1-x ~ delta  => F_c -> -delta(1-x)')
ok &= sp.limit(Ic_t, d, 0) == -1
# distribution statement: <F_b, h> = <2x[1/(1-x)]_+, h> + h(1)[int F_b - (-2)] since <2x/(1-x)_+,h> = int 2x(h-h(1))/(1-x) - 2h(1)
print('   => F_b -> 2x[1/(1-x)]_+ + delta(1-x) ln(1/delta^2)  (the -2 of int F_b is the plus-prescription remainder)')

# ---------------------------------------------------------------------------------------------
# 2. momentum space, kT != 0:  f_unsub^(1)(x,kT;y_B) = c_S/kT^2 { p(x) - eps(1-x) + delta(1-x)[ln(2 p+^2 e^{-2y_B}/kT^2) - sigma] }
#    soft: (1/2)[S(yA,yn) - S(yA,yB) - S(yn,yB)] = c_S/kT^2 delta(1-x) [2 y_B - 2 y_n + sigma]
yB, yn, pp, kT2, sig = sp.symbols('y_B y_n p_plus kT2 sigma', real=True)
unsub_delta = sp.log(2 * pp**2 * sp.exp(-2 * yB) / kT2) - sig
soft_delta = 2 * yB - 2 * yn + sig
tot = sp.simplify(sp.expand_log(unsub_delta + soft_delta, force=True))
zeta_def = 2 * pp**2 * sp.exp(-2 * yn)                 # zeta = 2 (x p+)^2 e^{-2 y_n} at x = 1  (Collins-Rogers 2013 eq. zeta.A)
print('2. delta(1-x) coefficient of the Collins TMD at kT != 0:', tot, '== ln(zeta/kT^2):',
      sp.simplify(sp.expand_log(tot - sp.log(zeta_def / kT2), force=True)) == 0)
ok &= sp.simplify(sp.expand_log(tot - sp.log(zeta_def / kT2), force=True)) == 0
print('   (y_B and the Wilson-line self-energy constant sigma cancel; y_A cancels inside the soft ratio)')

# ---------------------------------------------------------------------------------------------
# 3. b-space.  FT[(k^2)^(-1-eta)] (d=2-2eps) = pi^{1-eps} 2^{-2eps-2eta} Gamma(-eps-eta)/Gamma(1+eta) (b^2)^{eta+eps}
#   Phi(eta) = c_S FT[(k^2)^(-1-eta)] / (a S_eps):  binding  Phi(0) = A(eps) = -e^{eps L_b} e^{-gE eps} Gamma(1-eps)/eps
#   c_S FT[ln(zeta/k^2)/k^2]/(a S_eps) = A(eps) [ln(zeta b^2/4) + gE - psi(-eps)] = A(eps)[l_z + L_b - 1/eps - psi(1-eps) - gE]
def A_of(scheme):
    base = -sp.exp(eps * Lb) * sp.exp(-gE * eps) * sp.gamma(1 - eps) / eps
    return base if scheme == 'binding' else base * sp.gamma(1 - eps) * sp.exp(-gE * eps)
psi1me = sp.polygamma(0, 1 - eps)
res = {}
for scheme in ('binding', 'Collins'):
    A = A_of(scheme)
    Bd = A * (lz + Lb - 1 / eps - psi1me - gE)
    As = sp.expand(sp.series(A, eps, 0, 2).removeO())
    Bs = sp.expand(sp.series(Bd, eps, 0, 1).removeO())
    # bare Collins TMD: a S_eps { [p - eps(1-x)] A + delta(1-x) B }
    Pp, Om, Dl = sp.symbols('p_x one_minus_x delta_1mx')     # placeholders for p(x), (1-x), delta(1-x)
    fbare = sp.expand(Pp * As - eps * Om * As + Dl * Bs)
    poles = {k: sp.expand(fbare).coeff(eps, k) for k in (-2, -1)}
    fin = sp.expand(fbare).coeff(eps, 0)
    print('3. [%s] A(eps) = %s' % (scheme, sp.collect(As, eps)))
    print('   B(eps) = %s' % sp.collect(Bs, eps))
    print('   bare f~(1)/(a S_eps): 1/eps^2: %s ; 1/eps: %s ; finite: %s' % (poles[-2], sp.collect(poles[-1], [Pp, Dl]), sp.collect(fin, [Pp, Om, Dl])))
    # IR (collinear-PDF) poles: -(1/eps)[p(x) + 3/2 delta(1-x)] (MSbar PDF of a quark in a quark, pure DR)
    UV = sp.expand(poles[-2] / eps**2 + poles[-1] / eps - (-(Pp + sp.Rational(3, 2) * Dl) / eps))
    print('   => UV poles of the bare TMD:', sp.collect(UV, Dl), '   (x-independent, delta(1-x) only)')
    ok &= sp.simplify(UV.coeff(Pp)) == 0
    Zm1 = sp.expand(-UV / Dl)          # Z_F Z_2 - 1 in units a S_eps
    print('   Z_F Z_2 - 1 = a S_eps [%s]' % Zm1)
    # anomalous dimension: d ln Z/d ln mu, d a/d ln mu = -2 eps a + O(a^2), d l_z/d ln mu = -2
    aa = sp.Symbol('a')
    gF = sp.expand(sp.diff(aa * Zm1, aa) * (-2 * eps * aa) + aa * sp.diff(Zm1, lz) * (-2))
    print('   gamma_F = d ln Z/d ln mu =', sp.simplify(gF), '  (a = alpha_s C_F/2pi)')
    ok &= sp.simplify(gF - aa * (3 - 2 * lz)) == 0
    C1 = sp.collect(fin, [Pp, Om, Dl])
    res[scheme] = fin
    Kt = sp.expand(2 * sp.diff(fin, lz))
    print('   C~(1) = a [%s] ;  K~ = d ln f/d ln sqrt(zeta) = a*(%s) = -(alpha_s C_F/pi) L_b: %s' % (C1, Kt, sp.simplify(Kt + 2 * Lb * Dl) == 0))
    ok &= sp.simplify(Kt + 2 * Lb * Dl) == 0

d_scheme = sp.simplify(res['binding'] - res['Collins'])
print('4. C~(binding) - C~(Collins) =', d_scheme, '  (times a; = -(pi^2/12) a delta(1-x))')
ok &= sp.simplify(d_scheme + sp.pi**2 / 12 * sp.Symbol('delta_1mx')) == 0
print('   at mu = mu_b (L_b=0), zeta = mu_b^2 (l_z=0): Collins C~ = delta + a(1-x) [Aybat-Rogers (A11)];'
      ' binding C~ = delta + a[(1-x) - (pi^2/12) delta(1-x)] [EIS 2012 eq. "coeff" at L_T=0, zeta=Q^2=mu^2]')

# ---------------------------------------------------------------------------------------------
# 5. RG consistency of the small-b OPE: d/dln mu [C~ (x) f] = gamma_F C~ (x) f  at O(alpha_s)
#    with df/dln mu = (alpha_s/pi) P_qq (x) f,  P_qq/C_F = p(x) + 3/2 delta(1-x)
Pp, Dl = sp.symbols('p_x delta_1mx')
C1 = -Lb * Pp + Dl * (-Lb**2 / 2 - Lb * lz)          # L-dependent part of C~(1) (units a)
dC = sp.expand(sp.diff(C1, Lb) * 2 + sp.diff(C1, lz) * (-2))        # d/d ln mu
tot5 = sp.expand(dC + 2 * (Pp + sp.Rational(3, 2) * Dl))           # + (alpha_s/pi) P_qq/(a C_F) = 2 (p + 3/2 delta)
print('5. d(C~ x f)/dln mu (units a, delta-part) =', sp.collect(tot5, [Pp, Dl]), ' ; gamma_F (units a) = 3 - 2 l_z')
ok &= sp.simplify(tot5 - Dl * (3 - 2 * lz)) == 0
# 6. consistency relations among anomalous dimensions
Kt = -2 * Lb                     # units a  (K~ = -(alpha_s C_F/pi) L_b)
gK = -sp.diff(Kt, Lb) * 2        # -dK~/dln mu, units a
gF = 3 - 2 * lz
print('6. gamma_K = %s a = 2 C_F alpha_s/pi ; d gamma_F/d ln sqrt(zeta) = %s a = -gamma_K ; dK~/dln mu = %s a' % (
    gK, sp.diff(gF, lz) * 2, sp.diff(Kt, Lb) * 2))
ok &= gK == 4 and sp.diff(gF, lz) * 2 == -gK
# ---------------------------------------------------------------------------------------------
# 7. the non-uniform remainder of the rapidity-regulator expansion is invisible at fixed b_T in the light-like limit:
#    delta(1-x) part: exact int F_b - limit = D(kappa) = ln(1+kappa^2) + 2 kappa arctan(1/kappa),  kappa = kT/Lambda_B (time-like),
#    its 2D Fourier transform (eps = 0) at b: 2 pi int dkappa/kappa J0(kappa z) D(kappa),  z = Lambda_B b  ->  2 pi^2/z for z >> 1
Dk = lambda k: mp.log(1 + k**2) + 2 * k * mp.atan(1 / k)
for z in (20, 200, 2000):
    val = 2 * mp.pi * mp.quadosc(lambda k: mp.besselj(0, k * z) * Dk(k) / k, [0, mp.inf], omega=z)
    print('7. z = Lambda_B b_T = %5d : FT of remainder = %s ; 2 pi^2/z = %s' % (z, mp.nstr(val, 8), mp.nstr(2 * mp.pi**2 / z, 8)))
    if z == 2000:
        ok &= abs(val * z / (2 * mp.pi**2) - 1) < 2e-2
print('   => vanishes like 1/(Lambda_B b_T): the light-like limit at fixed b_T keeps only the expanded (distribution) form')
print('one-loop TMD assembly checks:', 'PASS' if ok else 'FAIL')
