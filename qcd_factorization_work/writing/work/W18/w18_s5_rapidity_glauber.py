# -*- coding: utf-8 -*-
"""
w18_s5_rapidity_glauber.py -- Ch15 (W18): checks needed for sec:scet-scet2, sec:scet-glauber, sec:scet-rg and the
examples that are not covered by s1-s4.  Own implementation (numpy / sympy / mpmath), conventions of WRITER_SPEC_v2 Sec. 3:
metric (+,-,-,-), D = d - i g A, n = (1,0,0,1), nbar = (1,0,0,-1), nbar.p = sqrt2 p^+.

  A rapidity divergence of soft real emission at fixed k_T; eta-regulated rapidity integral (closed form, 2/eta + O(eta));
  B 2D Fourier transform of the plus distribution (CJNR L_0): FT = -L_b/2;
  C scheme dictionary at one loop: K~ = gamma_nu^S/2 = -F_qqbar = -2 D_EIS, and their mu dependence;
  D Glauber potential from tree-level n-nbar forward scattering: -8 pi alpha_s/q_T^2 [ubar nbarslash/2 T u][ubar nslash/2 T u];
  E Glauber box vs crossed box: k^0 poles (same / opposite half planes) and the |2k^z|^{-eta}-regulated k^z integral;
  F BPS decoupling at O(g): Y from -infinity (+i0) vs Feynman rules of an outgoing quark (-i0, future-pointing line);
  G QCD O(alpha_s) thrust cumulant from the triangle integral (analytic): delta(tau) coefficient pi^2/3 - 1;
  H SCET_II soft emission, spin-summed relative deviation from the eikonal factor (spinor independent measure);
  I W_n: path-ordered integral for m outgoing gluons = product of eikonal factors in each ordering; abelian eikonal identity.
"""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w18_common import *
import sympy as sp
import mpmath as mp

mp.mp.dps = 30
ck = Check('W18 s5: rapidity regulators and dictionary; Glauber potential, box/crossed box; decoupling example; QCD cumulant')

# ---------------------------------------------------------------- A rapidity divergence
# fixed k_T: int dn.k dnbar.k delta(n.k nbar.k - kT^2)/(n.k nbar.k) = (1/kT^2) int dy, y = ln(nbar.k/kT)
kT = 1.7
def fixedkT(Y):
    # integrate over nbar.k from kT e^{-Y} to kT e^{Y}: int dnb/nb * 1/kT^2
    return mp.quad(lambda nb: 1 / nb / kT ** 2, [kT * mp.e ** (-Y), kT * mp.e ** Y])
v1, v2 = fixedkT(5), fixedkT(10)
ck('A1 soft emission at fixed k_T: integral = (1/k_T^2) * (rapidity range 2Y): linear growth, not regulated by DR',
   abs(v1 - 10 / kT ** 2) < 1e-12 and abs(v2 - 20 / kT ** 2) < 1e-12, [float(v1 * kT ** 2), float(v2 * kT ** 2)])
# eta regulator: int dy |2 sinh y|^{-eta} = 2^{-eta} Gamma(eta/2) Gamma(1/2-eta/2)/sqrt(pi)
ok = True; vals = []
for et in (mp.mpf('0.3'), mp.mpf('0.55')):
    num = 2 * mp.quad(lambda y: (2 * mp.sinh(y)) ** (-et), [0, 1, mp.inf])
    cf = 2 ** (-et) * mp.gamma(et / 2) * mp.gamma(mp.mpf(1) / 2 - et / 2) / mp.sqrt(mp.pi)
    vals.append(float(num - cf)); ok &= abs(num - cf) < 1e-10
ck('A2 int dy |2 sinh y|^{-eta} = 2^{-eta} Gamma(eta/2) Gamma(1/2 - eta/2)/sqrt(pi)  (|2k^z| = 2 k_T |sinh y|)', ok, vals)
et = sp.symbols('eta', positive=True)
cfs = 2 ** (-et) * sp.gamma(et / 2) * sp.gamma(sp.Rational(1, 2) - et / 2) / sp.sqrt(sp.pi)
s_ = sp.series(cfs, et, 0, 2).removeO()
ck('A3 expansion: 2/eta + 0 + O(eta)  (both rapidity ends regulated by one pole)',
   sp.simplify(s_.coeff(et, -1) - 2) == 0 and sp.simplify(s_.coeff(et, 0)) == 0, sp.simplify(s_))

# ---------------------------------------------------------------- B 2D Fourier transform of the plus distribution
def ft_plus(b, mu):
    # int_0^inf dp/p [J0(p b) - theta(mu - p)]
    f1 = mp.quad(lambda p: (mp.besselj(0, p * b) - 1) / p, [0, mu])
    f2 = mp.quadosc(lambda p: mp.besselj(0, p * b) / p, [mu, mp.inf], omega=b)
    return f1 + f2
ok = True; out = []
for b, mu in ((0.7, 1.3), (2.0, 0.45), (0.15, 5.0)):
    lhs = ft_plus(mp.mpf(b), mp.mpf(mu)); rhs = -mp.log(b * mu * mp.e ** mp.euler / 2)
    out.append(float(lhs - rhs)); ok &= abs(lhs - rhs) < 1e-12
ck('B1 int_0^inf dp/p [J0(pb) - theta(mu-p)] = -ln(b mu e^{gamma_E}/2) = -L_b/2,  L_b = ln(b^2 mu^2/b_0^2), b_0 = 2e^{-gamma_E}', ok, out)
ck('B2 hence  int d^2p e^{i p.b} (1/2pi)[1/p^2]_+^{(mu)} = -L_b/2  (angular integral: 2pi J0)', True)

# ---------------------------------------------------------------- C one-loop dictionary
a_s, CF, Lb, mu = sp.symbols('alpha_s C_F L_b mu', positive=True)
Kt = -a_s * CF / sp.pi * Lb                              # Collins-Soper kernel (VF / CONV row 29)
gam_nuS = (4 * a_s * CF / sp.pi) * (-Lb / 2)             # CJNR: nu dS/dnu = (4 a C/pi) L_0 in p space -> b space via B1
F_qq = CF * a_s / sp.pi * Lb                             # Becher-Neubert 2011 eq. (F1loop), L_perp = L_b
D_eis = a_s / (4 * sp.pi) * 2 * CF * Lb                  # EIS 2012: d_1 = 2 C_F L_T, D = sum d_n (a/4pi)^n, L_T = L_b
ck('C1 gamma_nu^S (eta regulator, quark Wilson lines) = -(2 alpha_s C_F/pi) L_b = 2 K~', sp.simplify(gam_nuS - 2 * Kt) == 0, gam_nuS)
ck('C2 collinear anomaly exponent F_qqbar = (alpha_s C_F/pi) L_b = -K~', sp.simplify(F_qq + Kt) == 0)
ck('C3 delta-regulator exponent D = (alpha_s C_F/2pi) L_b = -K~/2  (d ln F~/d ln Q^2 = -D at zeta = Q^2)', sp.simplify(D_eis + Kt / 2) == 0)
Gam = a_s * CF / sp.pi                                   # Gamma_cusp at one loop (Gamma_0 = 4 C_F)
dmu = lambda e: sp.diff(e, Lb) * 2                       # d L_b/d ln mu = 2
ck('C4 dK~/dln mu = -2 Gamma_cusp (= -gamma_K); dF/dln mu = 2 Gamma_cusp; dD/dln mu = Gamma_cusp; d gamma_nu^S/dln mu = -4 Gamma_cusp',
   sp.simplify(dmu(Kt) + 2 * Gam) == 0 and sp.simplify(dmu(F_qq) - 2 * Gam) == 0 and sp.simplify(dmu(D_eis) - Gam) == 0
   and sp.simplify(dmu(gam_nuS) + 4 * Gam) == 0)
# product of two TMDs: d ln(f_A f_B)/d ln Q^2 at zeta_A = zeta_B = Q^2 equals K~ (Collins) = -F (BN) = -2D (EIS)
ck('C5 Q^2 dependence of f~_A f~_B (zeta_A = zeta_B = Q^2): K~ = -F_qqbar = -2D: the three schemes give the same kernel at one loop',
   sp.simplify(Kt - (-F_qq)) == 0 and sp.simplify(Kt - (-2 * D_eis)) == 0)

# ---------------------------------------------------------------- D Glauber potential (tree level n-nbar forward scattering)
chiA = np.array([0.3 + 0.2j, -0.5, 0.8j, 0.4]); chiB = np.array([0.6, 0.1 - 0.7j, 0.2, -0.3j])
chiC = np.array([-0.2j, 0.9, 0.3, 0.5 + 0.1j]); chiD = np.array([0.4, -0.2, 0.7 - 0.3j, 0.1])
errsD = []
for lam in (1e-1, 1e-2, 1e-3):
    Q = 10.0
    qT = np.array([0.6, -0.35]) * lam * Q
    # Glauber q = (lam^2, lam^2, lam): choose n.q, nbar.q ~ lam^2 Q with on-shell external lines
    nbp = 0.9 * Q; p1T = np.array([0.2, 0.1]) * lam * Q
    p1 = lc_vec(nbp, p1T @ p1T / nbp, p1T)
    p3T = p1T + qT; nbp3 = nbp                   # nbar.q = 0 at this order; n.q fixed by on-shellness
    p3 = lc_vec(nbp3, p3T @ p3T / nbp3, p3T)
    q = p3 - p1
    np2 = 1.1 * Q; p2T = np.array([-0.1, 0.25]) * lam * Q
    p2 = lc_vec(p2T @ p2T / np2, np2, p2T)
    p4 = p2 - q
    u1 = massless_spinor(p1, chiA); u3 = massless_spinor(p3, chiB); u2 = massless_spinor(p2, chiC)
    p4T = np.array([p4[1], p4[2]])
    # p4 is on shell only up to O(lam^4) corrections; use its exact on-shell projection for the spinor
    p4os = lc_vec(p4T @ p4T / (p4[0] - p4[3]), p4[0] - p4[3], p4T)
    u4 = massless_spinor(p4os, chiD)
    # colour stripped amplitudes (colour factor T^A x T^A common): QCD:  [ubar3 g gamma^mu u1][ubar4 g gamma_mu u2] (-i/q^2) (i)^2
    J1 = np.array([bar(u3) @ GAM[m] @ u1 for m in range(4)]); J2 = np.array([bar(u4) @ GAM[m] @ u2 for m in range(4)])
    full = (1j) ** 2 * (J1[0] * J2[0] - J1[1] * J2[1] - J1[2] * J2[2] - J1[3] * J2[3]) * (-1j) / dot(q, q)
    # EFT: Glauber potential  -i (8 pi alpha_s/qT^2)[...] with g^2 = 4 pi alpha_s  -> -i 2 g^2/qT^2 ; here g = 1
    eft = -1j * 2.0 / (qT @ qT) * (bar(u3) @ (NBSL / 2) @ u1) * (bar(u4) @ (NSL / 2) @ u2)
    errsD.append(abs(full - eft) / abs(eft))
ck('D1 tree-level n-nbar forward scattering = -i (8 pi alpha_s/q_T^2)[ubar nbarslash/2 T u][ubar nslash/2 T u] + O(lam): '
   'the Glauber potential is instantaneous in x^+ and x^- (independent of n.q, nbar.q)',
   errsD[2] < 1e-2 and errsD[0] / errsD[2] > 20, ['%.1e' % e for e in errsD])
# spinor identity ubar_n gamma^mu u_n = n^mu ubar_n (nbarslash/2) u_n + O(lam)
p = lc_vec(9.0, (0.03 ** 2 + 0.05 ** 2) / 9.0, [0.03, 0.05]); pp = lc_vec(8.0, (0.04 ** 2 + 0.01 ** 2) / 8.0, [-0.04, 0.01])
ua = massless_spinor(p, chiA); ub = massless_spinor(pp, chiB)
lhs = np.array([bar(ub) @ GAM[m] @ ua for m in range(4)]); rhs = NV * (bar(ub) @ (NBSL / 2) @ ua)
ck('D2 ubar_n gamma^mu u_n = n^mu ubar_n (nbarslash/2) u_n up to O(lam)', np.max(np.abs(lhs - rhs)) / np.max(np.abs(rhs)) < 2e-2,
   '%.1e' % (np.max(np.abs(lhs - rhs)) / np.max(np.abs(rhs))))

# ---------------------------------------------------------------- E Glauber box vs crossed box
A_, B_, D1, D2, kz = 3.0, 2.5, 0.7, -0.4, 0.37
delta = mp.mpf('0.05')          # finite +i delta in every propagator; the pole positions are exact for any delta > 0
def box_k0(cross, d=delta):
    # D1 = -A (k0 - kz) - D1 + i d ;  box: D2 = +B (k0 + kz) - D2 + i d ; crossed: D2 = -B (k0 + kz) - D2 + i d
    def f(k0):
        a = -A_ * (k0 - kz) - D1 + 1j * d
        b = (-B_ if cross else B_) * (k0 + kz) - D2 + 1j * d
        return 1 / (a * b)
    pts = [-mp.inf, -20, -2, -1, -0.5, 0, 0.5, 1, 2, 20, mp.inf]
    re_ = mp.quad(lambda k: mp.re(f(k)), pts)
    im_ = mp.quad(lambda k: mp.im(f(k)), pts)
    return complex(re_, im_)
cb = box_k0(True)
bx = box_k0(False)
# analytic box: poles k0 = a (upper), k0 = b (lower):  -(1/AB) 2 pi i/(a - b), a - b = 2kz - D1/A - D2/B + i delta (1/A + 1/B)
amb = 2 * kz - D1 / A_ - D2 / B_ + 1j * float(delta) * (1 / A_ + 1 / B_)
bx_an = -(1 / (A_ * B_)) * 2j * np.pi / amb
ck('E1 crossed box: both k^0 poles in the upper half plane => k^0 integral vanishes (at fixed k^z), for any +i delta',
   abs(cb) < 1e-12, '%.1e' % abs(cb))
ck('E2 box: poles on opposite sides => -(2 pi i/AB)/(2k^z - D1/A - D2/B + i0)', abs(bx - bx_an) / abs(bx_an) < 1e-10,
   '%.1e' % (abs(bx - bx_an) / abs(bx_an)))
# k^z integral with |2k^z|^{-eta}:  x = 2k^z, int dk^z = (1/2) int dx ;
# PV int_{-inf}^{inf} |x|^{-eta}/(x - c) dx = -pi c^{-eta} tan(pi eta/2)  -> 0   (c > 0)
res = []
for etav in (mp.mpf('0.2'), mp.mpf('0.05')):
    c0 = mp.mpf('0.6')
    pv_cf = -mp.pi * c0 ** (-etav) * mp.tan(mp.pi * etav / 2)
    pos = (mp.quad(lambda xx: (xx ** (-etav) - c0 ** (-etav)) / (xx - c0), [0, c0, 2 * c0])
           + mp.quad(lambda xx: xx ** (-etav) / (xx - c0), [2 * c0, 10, mp.inf]))     # PV over x > 0 (odd part around c vanishes)
    neg = -mp.quad(lambda yy: yy ** (-etav) / (yy + c0), [0, 1, 10, mp.inf])          # x = -y < 0
    res.append(float(pos + neg - pv_cf))
ck('E3 PV part of the |2k^z|^{-eta}-regulated k^z integral = -(pi/2) c^{-eta} tan(pi eta/2) -> 0; '
   'the delta-function part gives -i(pi/2) c^{-eta}: the box is a pure (imaginary) phase as eta -> 0',
   max(abs(r) for r in res) < 1e-12, res)

# ---------------------------------------------------------------- F BPS decoupling at O(g)
# usoft gluon absorbed (field ~ eps e^{-ik.x}) by Y_n^dagger with Y_n = P exp(ig int_{-inf}^0 ds n.A(x+sn)):
#   Y^dagger -> -ig n.eps T int_{-inf}^0 ds e^{-is n.k + 0 s} = -ig n.eps T * i/(n.k + i0) = + g T n.eps/(n.k + i0)
s_, nk, dl = sp.symbols('s n_k delta', real=True)
I_past = sp.integrate(sp.exp(-sp.I * s_ * nk + dl * s_), (s_, -sp.oo, 0), conds='none')
ck('F1 int_{-inf}^0 ds e^{-i s n.k + delta s} = i/(n.k + i delta): Y_n^dagger (past-pointing) gives +g T n.eps/(n.k + i0)',
   sp.simplify(I_past - sp.I / (nk + sp.I * dl)) == 0, sp.simplify(I_past))
# future-pointing W[x+inf n, x] = P exp(ig int_0^inf ds n.A(x+sn)) for the absorbed gluon:
I_fut = sp.integrate(sp.exp(-sp.I * s_ * nk - dl * s_), (s_, 0, sp.oo), conds='none')
ck('F2 int_0^inf ds e^{-i s n.k - delta s} = -i/(n.k - i delta): W[x+inf n,x] gives + g T n.eps/(n.k - i0) = LO Feynman rules of an outgoing quark',
   sp.simplify(I_fut + sp.I / (nk - sp.I * dl)) == 0, sp.simplify(I_fut))
# difference of the two eikonal factors: 1/(n.k+i0) - 1/(n.k-i0) = -2 pi i delta(n.k): supported at n.k = 0 only
ck('F3 1/(x+i0) - 1/(x-i0) = -2 pi i delta(x): direction matters only at n.k = 0 (virtual graphs; real emission has n.k > 0)', True)
# the O(g) cancellation in (in.d + g n.A)(Y xi0) with Y = 1 - g T n.eps e^{-ik.x}/(n.k)
g_, ne = sp.symbols('g n_eps')
X = sp.symbols('x0')  # placeholder coordinate along n.d direction: in.d e^{-ik.x} = n.k e^{-ik.x}
# act on e^{-ik.x} f: in.d(Y f) = (in.d Y) f + Y in.d f ; in.d Y = -g T n.eps (n.k)/(n.k) e^{-ikx} = -g T n.eps e^{-ikx}
inY = -g_ * ne                                         # coefficient of T e^{-ikx}
ck('F4 O(g): (in.d Y) + g n.A_us = -g T n.eps e^{-ikx} + g T n.eps e^{-ikx} = 0  =>  in.D_us(Y f) = Y in.d f',
   sp.simplify(inY + g_ * ne) == 0)

# ---------------------------------------------------------------- G QCD O(alpha_s) thrust cumulant: triangle integral
# M = (x1^2 + x2^2)/((1-x1)(1-x2)) with y_i = 1 - x_i:  M = 2/(y1 y2) - 2/y1 - 2/y2 + y1/y2 + y2/y1
y1, y2, t = sp.symbols('y1 y2 tau', positive=True)
M = ((1 - y1) ** 2 + (1 - y2) ** 2) / (y1 * y2)
ck('G0 M = 2/(y1y2) - 2/y1 - 2/y2 + y1/y2 + y2/y1', sp.simplify(M - (2 / (y1 * y2) - 2 / y1 - 2 / y2 + y1 / y2 + y2 / y1)) == 0)
# region T < 1 - tau:  y1 > tau, y2 > tau, y1 + y2 < 1 - tau  (x3 = 2 - x1 - x2 < 1 - tau)
Fin = sp.integrate(sp.expand(M), y2)          # elementary antiderivative in y2
def tri_num(expr_in_y2_antider, tv):
    tv = mp.mpf(tv)
    f = sp.lambdify((y1, y2), expr_in_y2_antider, 'mpmath')
    g = lambda u: f(u, 1 - tv - u) - f(u, tv)
    return mp.quad(g, [tv, mp.mpf('0.5') - tv, 1 - 2 * tv])
target = lambda tv: 2 * mp.log(tv) ** 2 + 3 * mp.log(tv) + mp.mpf(5) / 2 - mp.pi ** 2 / 3
diffs = [tri_num(Fin, tv) - target(tv) for tv in ('1e-4', '1e-6', '1e-8')]
ck('G1 int_{T<1-tau} (x1^2+x2^2)/((1-x1)(1-x2)) dx1 dx2 = 2 ln^2 tau + 3 ln tau + 5/2 - pi^2/3 + O(tau ln^2 tau)',
   abs(diffs[2]) < 1e-5 and abs(diffs[1]) < 1e-3 and abs(diffs[0] / diffs[1]) > 20, [mp.nstr(d_, 3) for d_ in diffs])
pieces = [(1 / (y1 * y2), lambda tv: mp.log(tv) ** 2 - mp.pi ** 2 / 6), (1 / y2, lambda tv: -mp.log(tv) - 1),
          (y1 / y2, lambda tv: -mp.log(tv) / 2 - mp.mpf(3) / 4)]
chk = []
for e, tg in pieces:
    Fe = sp.integrate(e, y2)
    chk.append(tri_num(Fe, '1e-8') - tg(mp.mpf('1e-8')))
ck('G2 pieces: int 1/(y1y2) = ln^2 tau - pi^2/6, int 1/y2 = -ln tau - 1, int y1/y2 = -ln(tau)/2 - 3/4  (+ O(tau ln^2 tau))',
   max(abs(c) for c in chk) < 1e-5, [mp.nstr(c, 3) for c in chk])
tl = sp.symbols('ell')
ck('G3 combination 2 I_a - 4 I_b + 2 I_c = 2 ln^2 tau + 3 ln tau + 5/2 - pi^2/3',
   sp.simplify(2 * (tl ** 2 - sp.pi ** 2 / 6) - 4 * (-tl - 1) + 2 * (-tl / 2 - sp.Rational(3, 4)) - (2 * tl ** 2 + 3 * tl + sp.Rational(5, 2) - sp.pi ** 2 / 3)) == 0)
Rc = sp.Rational(3, 2) - (2 * tl ** 2 + 3 * tl + sp.Rational(5, 2) - sp.pi ** 2 / 3)
ck('G4 cumulant R = 1 + (C_F alpha_s/2pi)[-2 ln^2 tau - 3 ln tau + pi^2/3 - 1]; differentiating: -3[1/tau]_+ - 4[ln tau/tau]_+ + (pi^2/3-1) delta(tau)',
   sp.simplify(Rc - (-2 * tl ** 2 - 3 * tl + sp.pi ** 2 / 3 - 1)) == 0)
cdel = mp.pi ** 2 / 3 - 1
ck('G5 delta(tau) coefficient pi^2/3 - 1 = %s' % mp.nstr(cdel, 20), True)

# ---------------------------------------------------------------- H SCET_II soft emission (spin-summed measure)
def scet2_ratio(lam, kdir, eps_):
    Q = 10.0
    nbp = 0.8 * Q; pt = np.array([0.5, -0.3]) * lam * Q
    p = lc_vec(nbp, pt @ pt / nbp, pt)
    ks = np.array(kdir) * lam * Q
    # matrices acting to the right on the current: exact  pslash-projected:  ubar(p) [i eps-slash][i (p+k)-slash/(p+k)^2]
    Ex = (1j * slash(eps_)) @ (1j * slash(p + ks) / dot(p + ks, p + ks))
    Ek = (-dot(NV, eps_) / dot(NV, ks)) * ID4
    Dm = Ex - Ek
    # sum_s (ubar_s X)(ubar_s X)^dagger = Tr[X X^dagger gamma0 pslash]  (Euclidean norm of the row vector, spin summed)
    num = np.trace(Dm @ Dm.conj().T @ GAM[0] @ slash(p)).real
    den = np.trace(Ek @ Ek.conj().T @ GAM[0] @ slash(p)).real
    return np.sqrt(abs(num / den))
e_c = np.array([0.2, 0.5 + 0.3j, -0.1, 0.4])
rH = [scet2_ratio(l, [1.0, 0.3, -0.6, 0.2], e_c) for l in (1e-1, 1e-2, 1e-3)]
ck('H1 SCET_II: spin-summed relative deviation of exact single soft emission from -n.eps/n.k scales like lam',
   rH[0] / rH[1] > 8 and rH[1] / rH[2] > 9.5 and rH[2] < 1e-2, ['%.3f' % r for r in rH])
rH2 = [scet2_ratio(l, [0.7, -0.2, 0.5, -0.1], np.array([0.1, -0.4j, 0.6, 0.3])) for l in (1e-1, 1e-2, 1e-3)]
ck('H2 second kinematic point: also O(lam)', rH2[1] / rH2[2] > 9.5, ['%.3f' % r for r in rH2])
# virtuality of the intermediate line
lam = 1e-2; Q = 10.0
pp = lc_vec(0.8 * Q, 0.0, [0.0, 0.0]); ksft = np.array([1.0, 0.3, -0.6, 0.2]) * lam * Q
ck('H3 (p+k_s)^2 ~ lam Q^2 (hard-collinear), (p+k_s)^2/(nbar.p n.k) = 1 + O(lam)',
   abs(dot(pp + ksft, pp + ksft) / (dot(NBV, pp) * dot(NV, ksft)) - 1) < 3e-2,
   '%.4f' % (dot(pp + ksft, pp + ksft) / (dot(NBV, pp) * dot(NV, ksft))))

# ---------------------------------------------------------------- I W_n: ordered integrals and eikonal identity
k1, k2, k3 = sp.symbols('k1 k2 k3', positive=True)   # nbar.k_j of outgoing gluons
d = sp.symbols('d', positive=True)
sv, bb = sp.symbols('s b')
# elementary step: int_{-inf}^{s} e^{b s'} ds' = e^{b s}/b  for Re b > 0
br_ = sp.symbols('b_r', positive=True); bi_ = sp.symbols('b_i', real=True)
step = sp.integrate(sp.exp((br_ + sp.I * bi_) * sv), (sv, -sp.oo, 0), conds='none')
ck('I0 int_{-inf}^0 e^{b s} ds = 1/b (Re b > 0): each nested ordered integral is elementary',
   sp.simplify(step - 1 / (br_ + sp.I * bi_)) == 0, sp.simplify(step))
# recursion: F_1(s) = e^{a1 s}/a1, F_{j}(s) = e^{(a1+..+aj)s}/prod_{i<=j}(a1+..+ai); at s = 0 with a_j = i k_j + d (outgoing gluons)
a = [sp.I * k1 + d, sp.I * k2 + d, sp.I * k3 + d]
F0 = 1
cum = 0
for aj in a:
    cum = cum + aj
    F0 = F0 / cum
val = sp.simplify((sp.I) ** 3 * F0.subs(d, 0))
target3 = 1 / (k1 * (k1 + k2) * (k1 + k2 + k3))
ck('I1 (ig)^3 x ordered integral = g^3/[nbar.k1 nbar.(k1+k2) nbar.(k1+k2+k3)]: the m-gluon term of W_n in one ordering',
   sp.simplify(val - target3) == 0, val)
# numerical cross-check of the nested integral (with damping d) by direct quadrature for m = 2
kk1, kk2, dd = mp.mpf('0.7'), mp.mpf('1.3'), mp.mpf('0.4')
num2 = mp.quad(lambda s2: mp.quad(lambda s1: mp.e ** ((1j * kk1 + dd) * s1), [-mp.inf, s2]) * mp.e ** ((1j * kk2 + dd) * s2), [-mp.inf, 0])
an2 = 1 / ((1j * kk1 + dd) * (1j * kk1 + 1j * kk2 + 2 * dd))
ck('I1b direct quadrature of the m = 2 nested integral agrees with the recursion', abs(num2 - an2) < 1e-15, mp.nstr(abs(num2 - an2), 3))
# abelian eikonal identity: sum over the 3! orderings of the eikonal products = prod 1/k_i
tot = 0
for perm in itertools.permutations([k1, k2, k3]):
    a1, b1, c1 = perm
    tot += 1 / (a1 * (a1 + b1) * (a1 + b1 + c1))
ck('I2 eikonal identity: sum_perms prod_j 1/nbar.K_j = prod_i 1/nbar.k_i (abelian limit of W_n = exponential)',
   sp.simplify(tot - 1 / (k1 * k2 * k3)) == 0)

ok = ck.summary()
sys.exit(0 if ok else 1)
