# -*- coding: utf-8 -*-
"""
s1_scet_algebra.py -- Part (1a): SCET kinematics, spinor projections, the LO collinear quark
Lagrangian (integrating out phi), its one-gluon Feynman rule, and power counting of all modes.

Run:  python3 -I s1_scet_algebra.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

ck = Check('s1_scet_algebra: light-cone algebra, projectors, L_xixi, Feynman rule, power counting')
rng = np.random.default_rng(2024)

n, nb = NVEC, NBVEC
ns, nbs = slash(n), slash(nb)

# ---------------------------------------------------------------------------------- A. kinematics
ck('n^2 = nbar^2 = 0, n.nbar = 2', abs(mdot(n, n)) < 1e-15 and abs(mdot(nb, nb)) < 1e-15 and abs(mdot(n, nb) - 2) < 1e-15)
ok = True; ok2 = True; ok3 = True; ok4 = True
for _ in range(20):
    p = rng.normal(size=4); q = rng.normal(size=4)
    nbp, np_, pp = lc_components(p)
    nbq, nq, qp = lc_components(q)
    # reconstruction
    ok &= close(nbp * n / 2 + np_ * nb / 2 + pp, p)
    # CONTEXT light-front: v^pm = (v0 pm v3)/sqrt2
    pplus, pminus = (p[0] + p[3]) / np.sqrt(2), (p[0] - p[3]) / np.sqrt(2)
    ok2 &= abs(nbp - np.sqrt(2) * pplus) < 1e-12 and abs(np_ - np.sqrt(2) * pminus) < 1e-12
    qplus, qminus = (q[0] + q[3]) / np.sqrt(2), (q[0] - q[3]) / np.sqrt(2)
    lf = pplus * qminus + pminus * qplus - (p[1] * q[1] + p[2] * q[2])
    ok3 &= abs(mdot(p, q) - lf) < 1e-12 and abs(mdot(p, q) - (0.5 * (nbp * nq + np_ * nbq) + mdot(pp, qp))) < 1e-12
    ok4 &= abs(mdot(p, p) - (nbp * np_ + mdot(pp, pp))) < 1e-12 and abs(mdot(pp, pp) + p[1] ** 2 + p[2] ** 2) < 1e-12
ck('p = nbar.p n/2 + n.p nbar/2 + p_perp', ok)
ck('nbar.p = sqrt2 p^+ , n.p = sqrt2 p^-  (CONTEXT light-front)', ok2)
ck('p.q = (nbar.p n.q + n.p nbar.q)/2 + p_perp.q_perp = p^+q^- + p^-q^+ - p_T.q_T', ok3)
ck('p^2 = n.p nbar.p + p_perp^2 ,  p_perp^2 = -p_T^2', ok4)

# ---------------------------------------------------------------------------------- B. projectors
Pn = ns @ nbs / 4
Pnb = nbs @ ns / 4
ck('P_n^2 = P_n, P_nbar^2 = P_nbar', close(Pn @ Pn, Pn) and close(Pnb @ Pnb, Pnb))
ck('P_n + P_nbar = 1, P_n P_nbar = 0', close(Pn + Pnb, ID4) and close(Pn @ Pnb, 0 * ID4))
ck('nslash P_n = 0  (=> nslash xi_n = 0)', close(ns @ Pn, 0 * ID4))
ck('gamma0 P_n^dag gamma0 = P_nbar  (=> xibar = psibar P_nbar)', close(G0 @ Pn.conj().T @ G0, Pnb))
ck('rank P_n = 2 (two independent components of xi_n)', np.linalg.matrix_rank(Pn) == 2)
ok = True
for _ in range(10):
    Dv = rng.normal(size=4)
    nbD, nD, Dp = lc_components(Dv)
    Ds, Dps = slash(Dv), slash(Dp)
    ok &= close(Pnb @ Ds @ Pn, nD * nbs / 2 @ Pn)
    ok &= close(Pn @ Ds @ Pnb, nbD * ns / 2 @ Pnb)
    ok &= close(Pnb @ Ds @ Pnb, Dps @ Pnb)
    ok &= close(Pn @ Ds @ Pn, Dps @ Pn)
ck('P_nbar Dslash P_n = n.D nbarslash/2 ; P_n Dslash P_nbar = nbar.D nslash/2 ; diagonal blocks = Dslash_perp', ok)
# psibar Dslash psi decomposition with random spinors
ok = True
for _ in range(10):
    psi = rng.normal(size=4) + 1j * rng.normal(size=4)
    Dv = rng.normal(size=4)
    nbD, nD, Dp = lc_components(Dv)
    xi, phi = Pn @ psi, Pnb @ psi
    lhs = bar(psi) @ slash(Dv) @ psi
    rhs = (bar(xi) @ (nbs / 2) @ xi * nD + bar(xi) @ slash(Dp) @ phi + bar(phi) @ slash(Dp) @ xi
           + bar(phi) @ (ns / 2) @ phi * nbD)
    ok &= abs(lhs - rhs) < 1e-10
ck('psibar Dslash psi = xibar nbarslash/2 n.D xi + xibar Dslash_perp phi + phibar Dslash_perp xi + phibar nslash/2 nbar.D phi', ok)

# ---------------------------------------------------------------------------------- C. integrating out phi (A = 0)
ok = True; okprop = True; oksol = True
for _ in range(10):
    p = rng.normal(size=4)
    nbp, np_, pp = lc_components(p)
    p2 = mdot(p, p)
    # effective operator on xi-space:  [n.p + pslash_perp (1/nbar.p) pslash_perp] nbarslash/2
    Op = (np_ * ID4 + slash(pp) @ slash(pp) / nbp) @ nbs / 2
    ok &= close(Pnb @ Op @ Pn, (p2 / nbp) * (nbs / 2) @ Pn)
    # propagator: P_n (i pslash/p^2) P_nbar = i nslash/2 nbar.p / p^2  (exact, off-shell)
    okprop &= close(Pn @ (1j * slash(p) / p2) @ Pnb, 1j * ns / 2 * nbp / p2)
for _ in range(10):
    # on-shell massless momentum, check phi = -(1/nbar.p) nbarslash/2 pslash_perp xi for u(p)
    k3 = rng.normal(size=3); p = np.array([np.linalg.norm(k3), *k3])
    nbp, np_, pp = lc_components(p)
    for s in (0, 1):
        u = u_spinor(p, s)
        oksol &= close(Pnb @ u, -(1 / nbp) * (nbs / 2) @ slash(pp) @ Pn @ u)
ck('xi-space operator n.p + pslash_perp pslash_perp/nbar.p = (p^2/nbar.p) on P_n-space', ok)
ck('propagator P_n (i pslash/p^2) P_nbar = i (nslash/2) nbar.p/p^2  (off-shell, exact)', okprop)
ck('on-shell: P_nbar u = -(1/nbar.p)(nbarslash/2) pslash_perp P_n u   (solution for phi)', oksol)

# Jet-function normalization (used in s2): cut definition
#   sum_X (2pi)^D delta(p - p_X) <0|chi_n|X><X|chibar_n|0> = 2pi (nslash/2) nbar.p J(p^2) 1_c  =>  J^(0) = delta(p^2)
# needs sum_s P_n u ubar P_nbar = P_n pslash P_nbar = (nslash/2) nbar.p for on-shell p.
okjet = True
for _ in range(10):
    k3 = rng.normal(size=3); p = np.array([np.linalg.norm(k3), *k3])
    uu = sum(np.outer(u_spinor(p, s), bar(u_spinor(p, s))) for s in (0, 1))
    okjet &= close(uu, slash(p)) and close(Pn @ uu @ Pnb, mdot(nb, p) * ns / 2)
ck('jet normalization: sum_s P_n u ubar P_nbar = (nslash/2) nbar.p  =>  cut definition gives J^(0) = delta(p^2)', okjet)
# Becher-Schwartz 2008 print J = (1/nbar.p)(1/pi) Im[ i int d^4x e^{-ipx} <0|T{chibar_n(x) (nbarslash/2) chi_n(0)}|0> ] = delta + O(as)
# Literal free-field evaluation: <T chibar_a(x) G_ab chi_b(0)> = -Tr[G S(-x)] (fermionic T), S = i (nslash/2) nbar.p/(p^2+i0),
# colour trace N_c.  Result: -2 N_c delta(p^2)  -> an implicit factor -tr/(2N_c) is understood in BS.
trD = np.trace((nbs / 2) @ (ns / 2)).real
xs_, dl_, Nc_ = sp.symbols('x delta N_c', positive=True)
xr_ = sp.Symbol('xr', real=True)
lor = sp.integrate(sp.im(1 / (xr_ + sp.I * dl_)).simplify(), (xr_, -sp.oo, sp.oo))   # int Im 1/(x+i delta) = -pi
coef_BS = sp.nsimplify(trD) * (-Nc_) * sp.I * sp.I                                    # i * ( -N_c Tr[G i nslash/2] )
J0_BS = sp.simplify(coef_BS * lor / sp.pi)                                             # times delta(p^2)
ck('Becher-Schwartz jet-function formula read literally gives J^(0) = -2 N_c delta(p^2) (normalization implicit there)',
   abs(trD - 2) < 1e-12 and sp.simplify(J0_BS + 2 * Nc_) == 0, f'Tr[(nbs/2)(ns/2)] = {trD:.1f}; J0 = {J0_BS} delta(p^2)')

# ---------------------------------------------------------------------------------- D. collinear one-gluon Feynman rule
# V^mu(p',p) = i g t^a [ n^mu + gamma_perp^mu pslash_perp/nbar.p + p'slash_perp gamma_perp^mu/nbar.p'
#                         - p'slash_perp pslash_perp nbar^mu/(nbar.p nbar.p') ] nbarslash/2
# Exact tree-level identity:  P_n S(p') (i g gamma^mu) S(p) P_nbar = S_xi(p') V^mu S_xi(p)
def gperp(mu):
    # gamma_perp^mu = gamma^mu - n^mu nbarslash/2 - nbar^mu nslash/2
    return GAM[mu] - n[mu] * nbs / 2 - nb[mu] * ns / 2

ok = True
for _ in range(10):
    p = rng.normal(size=4) * 2; pp_ = rng.normal(size=4) * 2
    nbp, np_, pperp = lc_components(p)
    nbpp, npp, ppperp = lc_components(pp_)
    S = lambda k: 1j * slash(k) / mdot(k, k)
    Sxi = lambda k: 1j * ns / 2 * lc_components(k)[0] / mdot(k, k)
    for mu in range(4):
        lhs = Pn @ S(pp_) @ (1j * GAM[mu]) @ S(p) @ Pnb
        V = 1j * (n[mu] * ID4 + gperp(mu) @ slash(pperp) / nbp + slash(ppperp) @ gperp(mu) / nbpp
                  - slash(ppperp) @ slash(pperp) * nb[mu] / (nbp * nbpp)) @ nbs / 2
        rhs = Sxi(pp_) @ V @ Sxi(p)
        ok &= close(lhs, rhs, 1e-8)
ck('collinear quark-gluon vertex (BFPS form, g t^a stripped) reproduces QCD 3-point fn exactly', ok)

# ---------------------------------------------------------------------------------- E. power counting
lam = sp.Symbol('lambda', positive=True)
a1, a2, a3, b1, b2, b3, c1, c2 = sp.symbols('a1 a2 a3 b1 b2 b3 c1 c2', positive=True)


def mom(scal, coeffs, perp_dir=(1, 0)):
    """momentum with (nbar.p, n.p, |p_perp|) ~ (lam^s1, lam^s2, lam^s3) times O(1) coefficients.
       returns (nbar.p, n.p, p_perp 2-vector)"""
    s1, s2, s3 = scal
    c_nb, c_n, c_p = coeffs
    return (c_nb * lam ** s1, c_n * lam ** s2, (c_p * lam ** s3 * perp_dir[0], c_p * lam ** s3 * perp_dir[1]))


def sq(p):
    nbp, np_, (px, py) = p
    return sp.expand(nbp * np_ - px ** 2 - py ** 2)


def add(p, q):
    return (p[0] + q[0], p[1] + q[1], (p[2][0] + q[2][0], p[2][1] + q[2][1]))


def lead(expr):
    """leading power of lam in expr (lowest exponent)"""
    expr = sp.expand(expr)
    pw = [sp.degree(t, lam) if t.has(lam) else 0 for t in sp.Add.make_args(expr)]
    # degree for possibly fractional powers
    exps = []
    for t in sp.Add.make_args(expr):
        e = sp.Poly(t.subs(lam, sp.Symbol('L') ** 2), sp.Symbol('L')).monoms() if False else None
        powdict = t.as_powers_dict()
        exps.append(powdict.get(lam, 0))
    return min(exps)


modes = {
    'hard': (0, 0, 0),
    'n-coll': (0, 2, 1),          # (nbar.p, n.p, p_perp) ~ Q(1, lam^2, lam)
    'nbar-coll': (2, 0, 1),
    'usoft': (2, 2, 2),
    'soft(SCET_II)': (1, 1, 1),
    'Glauber n-nbar': (2, 2, 1),
    'Glauber n-soft': (1, 2, 1),   # (nbar.q, n.q, q_perp) ~ (lam, lam^2, lam)
    'Glauber nbar-soft': (2, 1, 1),
    'hard-collinear(n)': (0, 1, sp.Rational(1, 2)),
}
expected_virt = {'hard': 0, 'n-coll': 2, 'nbar-coll': 2, 'usoft': 4, 'soft(SCET_II)': 2,
                 'Glauber n-nbar': 2, 'Glauber n-soft': 2, 'Glauber nbar-soft': 2, 'hard-collinear(n)': 1}
for name, sc in modes.items():
    p = mom(sc, (a1, a2, a3))
    v = lead(sq(p))
    ck(f'virtuality p^2 of {name:18s} ~ lam^{expected_virt[name]}', v == expected_virt[name], f'p^2 ~ lam^{v}')
# Glauber: q^2 dominated by q_perp^2, nbar.q n.q << q_perp^2  (off-shell, instantaneous potential)
for name in ('Glauber n-nbar', 'Glauber n-soft', 'Glauber nbar-soft'):
    s1, s2, s3 = modes[name]
    ck(f'{name}: nbar.q n.q ~ lam^{s1+s2} << q_perp^2 ~ lam^{2*s3}', s1 + s2 > 2 * s3)

# interactions: does mode X absorbing momentum of mode Y stay on its mass shell?
def stays(X, Y):
    p = mom(modes[X], (a1, a2, a3), (1, 0))
    q = mom(modes[Y], (b1, b2, b3), (sp.Rational(3, 5), sp.Rational(4, 5)))
    return lead(sq(add(p, q))), expected_virt[X]

table = [('n-coll', 'usoft', True), ('n-coll', 'soft(SCET_II)', False), ('n-coll', 'nbar-coll', False),
         ('n-coll', 'Glauber n-nbar', True), ('nbar-coll', 'Glauber n-nbar', True),
         ('n-coll', 'Glauber n-soft', True), ('soft(SCET_II)', 'Glauber n-soft', True),
         ('nbar-coll', 'Glauber nbar-soft', True), ('soft(SCET_II)', 'Glauber nbar-soft', True),
         ('usoft', 'n-coll', False)]
for X, Y, expect in table:
    v, v0 = stays(X, Y)
    ok = (v >= v0) == expect
    ck(f'{X} + {Y}: (p+q)^2 ~ lam^{v} vs p^2 ~ lam^{v0}  ->  {"stays on shell" if v >= v0 else "off-shell, integrate out"}', ok)
# n-coll + soft -> hard-collinear virtuality lam^1 (SCET_I intermediate, gives soft Wilson line S_n)
v, _ = stays('n-coll', 'soft(SCET_II)')
ck('n-coll + soft in SCET_II: (p+k)^2 ~ lam Q^2 = hard-collinear virtuality (integrated out -> S_n)', v == 1)

# field scaling from two-point functions: <phi phi> ~ int d^4p (propagator)
# collinear: d^4p ~ lam^4 ; xi propagator nslash nbar.p/p^2 ~ lam^-2  => <xi xibar> ~ lam^2 => xi ~ lam
def fscale(measure, prop):
    return sp.Rational(measure + prop, 2)

ck('xi_n ~ lam            (d^4p ~ lam^4, nbar.p/p^2 ~ lam^-2)', fscale(4, -2) == 1)
# gluon two-point function in covariant gauge: int d^4k (-i/k^2)[g^{mu nu} - (1-xi_g) k^mu k^nu/k^2]
# components (projected with nbar_mu nbar_nu, n_mu n_nu, perp-perp); measure d^4k ~ lam^4 (collinear)
kc = mom(modes['n-coll'], (a1, a2, a3), (1, 0))
k2c = sq(kc)
def comp_scale(gterm, kk):
    # scaling exponent of <A A> component = measure + min(power of g-term/k^2, power of kk/k^4)
    pw = []
    if gterm != 0:
        pw.append(lead(gterm) - lead(k2c))
    pw.append(lead(kk) - 2 * lead(k2c))
    return sp.Rational(4 + min(pw), 2)
s_nb = comp_scale(0, kc[0] ** 2)                 # nbar.nbar = 0
s_n = comp_scale(0, kc[1] ** 2)                  # n.n = 0
s_p = comp_scale(sp.Integer(1), kc[2][0] ** 2)   # g_perp ~ 1
ck('A_n components from covariant-gauge propagator: (nbar.A, n.A, A_perp) ~ (1, lam^2, lam)', (s_nb, s_n, s_p) == (0, 2, 1),
   f'exponents {(s_nb, s_n, s_p)}')
ck('A_us ~ lam^2          (d^4k ~ lam^8, 1/k^2 ~ lam^-4)', fscale(8, -4) == 2)
ck('q_us ~ lam^3          (d^4k ~ lam^8, kslash/k^2 ~ lam^-2)', fscale(8, -2) == 3)
ck('A_s ~ lam  (SCET_II)  (d^4k ~ lam^4, 1/k^2 ~ lam^-2)', fscale(4, -2) == 1)
ck('q_s ~ lam^{3/2} (SCET_II) (d^4k ~ lam^4, kslash/k^2 ~ lam^-1)', fscale(4, -1) == sp.Rational(3, 2))
# Lagrangian terms ~ lam^4 (collinear measure d^4x ~ lam^-4 => action ~ lam^0)
xi_, inD, Dp, invnbD = 1, 2, 1, 0
ck('xibar in.D nbarslash/2 xi ~ lam^4  (in.d, g n.A_n, g n.A_us all ~ lam^2)', xi_ + inD + xi_ == 4)
ck('xibar iDslash_perp (1/in.bar D) iDslash_perp xi ~ lam^4', xi_ + Dp + invnbD + Dp + xi_ == 4)
# usoft field components all ~ lam^2 (A_us ~ k_us); compare with collinear components (1, lam^2, lam)
us = (2, 2, 2); co = (s_nb, s_n, s_p)
ck('usoft-collinear couplings: n.A_us ~ n.A_n ~ lam^2 (LO); nbar.A_us/nbar.A_n ~ lam^2, A_us,perp/A_n,perp ~ lam (subleading)',
   us[1] == co[1] and us[0] - co[0] == 2 and us[2] - co[2] == 1)
# multipole expansion: k_us . x for collinear x ~ (n.x, nbar.x, x_perp) ~ (1, lam^-2, lam^-1)
# k.x = nbar.k n.x/2 + n.k nbar.x/2 + k_perp.x_perp ~ lam^2 + lam^0 + lam^1
kx_us = mom(modes['usoft'], (b1, b2, b3), (sp.Rational(3, 5), sp.Rational(4, 5)))
# collinear position: (n.x, nbar.x, x_perp) ~ (1, lam^-2, lam^-1)  [conjugate to (nbar.p, n.p, p_perp)]
nx, nbx, xperp = c1, c2 * lam ** -2, (a3 * lam ** -1, 0)
t1 = kx_us[0] * nx / 2           # nbar.k n.x/2
t2 = kx_us[1] * nbx / 2          # n.k nbar.x/2
t3 = -(kx_us[2][0] * xperp[0] + kx_us[2][1] * xperp[1])   # k_perp.x_perp
ck('multipole: k_us.x = n.k nbar.x/2 [lam^0] + k_perp.x_perp [lam^1] + nbar.k n.x/2 [lam^2] => A_us(x)=A_us(x_-)+O(lam), x_-^mu = nbar.x n^mu/2',
   (lead(t2), lead(t3), lead(t1)) == (0, 1, 2), f'{(lead(t2), lead(t3), lead(t1))}')
# usoft momentum entering collinear propagator: (p+k)^2 = nbar.p (n.p + n.k) + p_perp^2 + O(lam^3)
p = mom(modes['n-coll'], (a1, a2, a3), (1, 0))
k = mom(modes['usoft'], (b1, b2, b3), (sp.Rational(3, 5), sp.Rational(4, 5)))
full = sq(add(p, k))
lo = sp.expand(p[0] * (p[1] + k[1]) - p[2][0] ** 2 - p[2][1] ** 2)
ck('(p_c + k_us)^2 = nbar.p (n.p + n.k) + p_perp^2 + O(lam^3)  (only n.k_us at LO)', lead(full - lo) == 3,
   f'remainder ~ lam^{lead(full - lo)}')

ok = ck.summary()
sys.exit(0 if ok else 1)
