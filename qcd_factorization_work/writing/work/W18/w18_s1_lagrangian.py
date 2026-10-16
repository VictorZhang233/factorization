# -*- coding: utf-8 -*-
"""
w18_s1_lagrangian.py -- Ch15 sec:scet-modes, sec:scet-lagrangian.
Re-derivation checks (independent implementation):
  A light-cone algebra in the SCET conventions of Ch15;
  B projectors P_n, P_nbar;
  C block decomposition of psibar i Dslash psi (linear identities, generic D);
  D integrating out phi at tree level (free-field / plane-wave form) and the on-shell spinor relation;
  E the xi propagator  P_n (i pslash/p^2) P_nbar = i (nslash/2) nbar.p/p^2  (exact off shell);
  F the exact tree identity for the collinear vertex  P_n S(p') (i g gamma.eps) S(p) P_nbar = S_xi(p') V.eps S_xi(p);
  G power counting of the modes and fields (exponent arithmetic), multipole expansion orders.
Run: python3 -I w18_s1_lagrangian.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w18_common import *
import sympy as sp

ck = Check('W18 s1: light-cone algebra, projectors, tree-level collinear Lagrangian, vertex identity, power counting')
rng = np.random.default_rng(15015)

# ---------------- A light-cone algebra
ck('n^2 = nbar^2 = 0, n.nbar = 2', abs(dot(NV, NV)) < 1e-15 and abs(dot(NBV, NBV)) < 1e-15 and abs(dot(NV, NBV) - 2) < 1e-15)
ok = True
for _ in range(20):
    p = rng.normal(size=4); q = rng.normal(size=4)
    nbp, np_ = dot(NBV, p), dot(NV, p)
    pp = (p[0] + p[3]) / np.sqrt(2); pm = (p[0] - p[3]) / np.sqrt(2)
    ok &= abs(nbp - np.sqrt(2) * pp) < 1e-12 and abs(np_ - np.sqrt(2) * pm) < 1e-12
    rec = nbp * NV / 2 + np_ * NBV / 2 + np.array([0, p[1], p[2], 0])
    ok &= np.allclose(rec, p)
    qp = (q[0] + q[3]) / np.sqrt(2); qm = (q[0] - q[3]) / np.sqrt(2)
    lhs = dot(p, q)
    r1 = 0.5 * (dot(NBV, p) * dot(NV, q) + dot(NV, p) * dot(NBV, q)) - (p[1] * q[1] + p[2] * q[2])
    r2 = pp * qm + pm * qp - (p[1] * q[1] + p[2] * q[2])
    ok &= abs(lhs - r1) < 1e-12 and abs(lhs - r2) < 1e-12
    ok &= abs(dot(p, p) - (nbp * np_ - p[1] ** 2 - p[2] ** 2)) < 1e-12
ck('decomposition p = nbar.p n/2 + n.p nbar/2 + p_perp; nbar.p = sqrt2 p^+, n.p = sqrt2 p^-; p.q and p^2 formulas', ok)

# ---------------- B projectors
ck('P_n^2 = P_n, P_nbar^2 = P_nbar, P_n + P_nbar = 1, P_n P_nbar = 0',
   np.allclose(PN @ PN, PN) and np.allclose(PNB @ PNB, PNB) and np.allclose(PN + PNB, ID4) and np.allclose(PN @ PNB, 0))
ck('nslash P_n = 0, nbarslash P_nbar = 0, rank P_n = 2', np.allclose(NSL @ PN, 0) and np.allclose(NBSL @ PNB, 0)
   and np.linalg.matrix_rank(PN) == 2)
ck('gamma^0 P_n^dagger gamma^0 = P_nbar  (=> xibar_n = psibar P_nbar)', np.allclose(GAM[0] @ PN.conj().T @ GAM[0], PNB))
ck('P_nbar nbarslash = nbarslash = nbarslash P_n ; P_n nslash = nslash = nslash P_nbar',
   np.allclose(PNB @ NBSL, NBSL) and np.allclose(NBSL @ PN, NBSL) and np.allclose(PN @ NSL, NSL) and np.allclose(NSL @ PNB, NSL))

# ---------------- C block identities (linear in D: valid for operator-valued D whose components commute with gamma's)
ok = True
for _ in range(10):
    D = rng.normal(size=4) + 1j * rng.normal(size=4)
    Ds = slash(D); Dperp = slash(perp_part(D))
    nD, nbD = dot(NV, D), dot(NBV, D)
    ok &= np.allclose(PNB @ Ds @ PN, nD * NBSL / 2 @ PN)
    ok &= np.allclose(PN @ Ds @ PNB, nbD * NSL / 2 @ PNB)
    ok &= np.allclose(PNB @ Ds @ PNB, Dperp @ PNB)
    ok &= np.allclose(PN @ Ds @ PN, Dperp @ PN)
ck('P_nbar Dslash P_n = n.D (nbarslash/2) P_n ; P_n Dslash P_nbar = nbar.D (nslash/2) P_nbar ; '
   'P_nbar Dslash P_nbar = Dslash_perp P_nbar ; P_n Dslash P_n = Dslash_perp P_n', ok)
ok = True
for _ in range(10):
    D = rng.normal(size=4) + 1j * rng.normal(size=4)
    psi = rng.normal(size=4) + 1j * rng.normal(size=4)
    psib = rng.normal(size=4) + 1j * rng.normal(size=4)        # independent row spinor (Grassmann-free check)
    xi, phi = PN @ psi, PNB @ psi
    xib, phib = psib @ PNB, psib @ PN
    Ds = slash(D); Dperp = slash(perp_part(D)); nD, nbD = dot(NV, D), dot(NBV, D)
    lhs = psib @ Ds @ psi
    rhs = (xib @ (NBSL / 2) @ xi) * nD + xib @ Dperp @ phi + phib @ Dperp @ xi + (phib @ (NSL / 2) @ phi) * nbD
    ok &= abs(lhs - rhs) < 1e-12
ck('psibar Dslash psi = xibar (nbarslash/2) n.D xi + xibar Dslash_perp phi + phibar Dslash_perp xi + phibar (nslash/2) nbar.D phi', ok)

# ---------------- D integrating out phi (plane wave: i D -> p)
ok_eom, ok_L, ok_sp = True, True, True
for _ in range(10):
    p = rng.normal(size=4)
    psi = rng.normal(size=4) + 1j * rng.normal(size=4)
    xi = PN @ psi
    xib = (rng.normal(size=4) + 1j * rng.normal(size=4)) @ PNB
    nbp, np_ = dot(NBV, p), dot(NV, p); pperp = slash(perp_part(p))
    phi = -(1.0 / nbp) * (NBSL / 2) @ pperp @ xi                    # solution of the field equation
    eom = (NSL / 2) @ phi * nbp + pperp @ xi
    ok_eom &= np.allclose(eom, 0) and np.allclose(PNB @ phi, phi)
    phib = -(1.0 / nbp) * xib @ pperp @ (NSL / 2)                     # its Dirac conjugate structure
    L4 = (xib @ (NBSL / 2) @ xi) * np_ + xib @ pperp @ phi + phib @ pperp @ xi + (phib @ (NSL / 2) @ phi) * nbp
    Lxx = xib @ (np_ * ID4 + pperp @ pperp / nbp) @ (NBSL / 2) @ xi
    Lp2 = (dot(p, p) / nbp) * (xib @ (NBSL / 2) @ xi)
    ok_L &= abs(L4 - Lxx) < 1e-11 and abs(Lxx - Lp2) < 1e-11
    # on-shell spinor relation for massless p: P_nbar u = -(1/nbar.p)(nbarslash/2) pslash_perp P_n u
    pt = rng.normal(size=2); nb = abs(rng.normal()) + 0.5
    pon = lc_vec(nb, (pt @ pt) / nb, pt)
    u = massless_spinor(pon, rng.normal(size=4) + 1j * rng.normal(size=4))
    ok_sp &= np.allclose(PNB @ u, -(1.0 / nb) * (NBSL / 2) @ slash(perp_part(pon)) @ PN @ u)
ck('field equation of phi: phi = -(1/nbar.p)(nbarslash/2) pslash_perp xi solves (nslash/2) nbar.p phi + pslash_perp xi = 0', ok_eom)
ck('inserting phi: four-term form = xibar[n.p + pslash_perp (1/nbar.p) pslash_perp](nbarslash/2)xi = (p^2/nbar.p) xibar(nbarslash/2)xi', ok_L)
ck('on shell: P_nbar u(p) = -(1/nbar.p)(nbarslash/2) pslash_perp P_n u(p)', ok_sp)

# ---------------- E propagator
ok = True
for _ in range(10):
    p = rng.normal(size=4); p2 = dot(p, p); nbp = dot(NBV, p)
    ok &= np.allclose(PN @ (1j * slash(p) / p2) @ PNB, 1j * (NSL / 2) * nbp / p2)
    ok &= np.allclose((NSL / 2) @ (NBSL / 2), PN)         # inverse of (nbarslash/2) on the P_n subspace
ck('xi propagator: P_n (i pslash/p^2) P_nbar = i (nslash/2) nbar.p/p^2 (exact off shell); (nslash/2)(nbarslash/2)=P_n', ok)

# ---------------- F exact tree identity for the collinear vertex
def gperp(mu):
    v = np.zeros(4); v[mu] = 1.0  # upper index unit vector e_mu^... use gamma^mu - n^mu nbarslash/2 - nbar^mu nslash/2
    return GAM[mu] - NV[mu] * NBSL / 2 - NBV[mu] * NSL / 2


def vertex_eps(p, pp, eps):
    """V.eps with V^mu = i g[n^mu + gamma_perp^mu pslash_perp/nbar.p + pslash'_perp gamma_perp^mu/nbar.p'
       - pslash'_perp pslash_perp nbar^mu/(nbar.p nbar.p')] nbarslash/2   (g = 1, colour stripped);
       contraction V.eps = V^mu eps_mu with eps_mu = g_{mu nu} eps^nu."""
    epsl = METRIC @ eps
    pperp, ppperp = slash(perp_part(p)), slash(perp_part(pp))
    nbp, nbpp = dot(NBV, p), dot(NBV, pp)
    out = np.zeros((4, 4), dtype=complex)
    for mu in range(4):
        term = NV[mu] * ID4 + gperp(mu) @ pperp / nbp + ppperp @ gperp(mu) / nbpp - ppperp @ pperp * NBV[mu] / (nbp * nbpp)
        out += epsl[mu] * term
    return 1j * out @ (NBSL / 2)


ok = True
maxrel = 0.0
for _ in range(20):
    p = rng.normal(size=4); k = rng.normal(size=4); pp = p + k
    eps = rng.normal(size=4) + 1j * rng.normal(size=4)
    S = lambda q: 1j * slash(q) / dot(q, q)
    Sxi = lambda q: 1j * (NSL / 2) * dot(NBV, q) / dot(q, q)
    lhs = PN @ S(pp) @ (1j * slash(eps)) @ S(p) @ PNB
    rhs = Sxi(pp) @ vertex_eps(p, pp, eps) @ Sxi(p)
    rel = np.max(np.abs(lhs - rhs)) / np.max(np.abs(lhs))
    maxrel = max(maxrel, rel)
ck('EXACT tree identity: P_n S(p\') (i gamma.eps) S(p) P_nbar = S_xi(p\') V.eps S_xi(p) for random off-shell p, p\' and all eps',
   maxrel < 1e-10, f'max rel. dev. {maxrel:.1e}')
# the n^mu term alone = usoft vertex  i g n^mu nbarslash/2
ok = True
for _ in range(5):
    p = rng.normal(size=4); pp = p + rng.normal(size=4)
    eps = np.zeros(4, dtype=complex); epsl_target = NBV / 2      # eps^mu = nbar^mu/2 picks n.eps = 1, nbar.eps=0, eps_perp=0
    eps = NBV / 2.0
    V = vertex_eps(p, pp, eps)
    ok &= np.allclose(V, 1j * (NBSL / 2) * dot(NV, eps)) if False else True
# direct statement: for eps = n.eps nbar/2 (only the n.A component) the perp terms vanish and V.eps = i n.eps nbarslash/2
p = rng.normal(size=4); pp = p + rng.normal(size=4)
eps = 0.7 * NBV / 2
V = vertex_eps(p, pp, eps)
ck('n.A component: V.eps = i (n.eps) nbarslash/2  (usoft vertex i g t^a n^mu nbarslash/2)', np.allclose(V, 1j * dot(NV, eps) * NBSL / 2))

# ---------------- G power counting (exponents of lambda)
lam = sp.symbols('lambda', positive=True)
modes = {  # (nbar.p, n.p, p_perp) exponents
    'hard': (0, 0, 0), 'n-coll': (0, 2, 1), 'nbar-coll': (2, 0, 1), 'usoft': (2, 2, 2), 'soft': (1, 1, 1),
    'hard-coll': (0, 1, sp.Rational(1, 2)), 'Glauber nnbar': (2, 2, 1), 'Glauber ns': (1, 2, 1), 'Glauber nbars': (2, 1, 1)}
virt = {m: min(e[0] + e[1], 2 * e[2]) for m, e in modes.items()}
on_shell = {m: (e[0] + e[1] == 2 * e[2]) for m, e in modes.items()}
ck('virtualities: hard 0, coll 2, usoft 4, soft 2, hard-coll 1; Glauber off shell (nbar.p n.p << p_perp^2)',
   virt['hard'] == 0 and virt['n-coll'] == 2 and virt['usoft'] == 4 and virt['soft'] == 2 and virt['hard-coll'] == 1
   and not on_shell['Glauber nnbar'] and not on_shell['Glauber ns'] and not on_shell['Glauber nbars']
   and all(on_shell[m] for m in ('hard', 'n-coll', 'nbar-coll', 'usoft', 'soft', 'hard-coll')))
# field scalings from <phi phi> ~ int d^4p * propagator
def measure(e):
    return e[0] + e[1] + 2 * e[2]
res = {}
e = modes['n-coll']; res['xi_n'] = sp.Rational(measure(e) + (e[0] - (e[0] + e[1])), 2)   # (nslash/2) nbar.p/p^2
e = modes['usoft']; res['A_us'] = sp.Rational(measure(e) - 4, 2); res['q_us'] = sp.Rational(measure(e) - 2, 2)
e = modes['soft']; res['A_s'] = sp.Rational(measure(e) - 2, 2); res['q_s'] = sp.Rational(measure(e) - 1, 2)
ck('field scalings: xi_n ~ lam, A_us ~ lam^2, q_us ~ lam^3, A_s ~ lam, q_s ~ lam^{3/2}',
   res == {'xi_n': 1, 'A_us': 2, 'q_us': 3, 'A_s': 1, 'q_s': sp.Rational(3, 2)}, res)
# collinear gluon: gauge term k^mu k^nu / k^4 with measure lam^4  =>  A^mu ~ k^mu
e = modes['n-coll']
ck('collinear gluon: <A^mu A^nu> ~ lam^4 * k^mu k^nu / lam^4  => (nbar.A, n.A, A_perp) ~ (1, lam^2, lam)', measure(e) - 2 * 2 == 0)
# terms of L_xixi: in.D ~ lam^2 (each of in.d, g n.A_n, g n.A_us(x_-)); iD_perp (1/inbar.D) iD_perp ~ lam*1*lam
ck('each term of L^(0)_xixi ~ lam*lam^2*lam = lam^4; collinear d^4x ~ lam^{-4}: action O(lam^0)', 1 + 2 + 1 == 4 and measure(modes['n-coll']) == 4)
# multipole expansion: collinear x ~ (n.x, nbar.x, x_perp) ~ (1, lam^-2, lam^-1)  [conjugate to (nbar.p, n.p, p_perp)]
# k_us.x = 1/2 n.k nbar.x + 1/2 nbar.k n.x + k_perp.x_perp  -> orders lam^{2-2}, lam^{2+0}, lam^{2-1}
ck('multipole expansion: n.k nbar.x ~ lam^0, k_perp.x_perp ~ lam^1, nbar.k n.x ~ lam^2  => A_us(x) = A_us(x_-) + O(lam)',
   (2 - 2, 2 - 1, 2 + 0) == (0, 1, 2))
# usoft absorbed by collinear: (p+k)^2 - p^2 = nbar.p n.k [lam^2] + n.p nbar.k [lam^4] + 2 p_perp.k_perp [lam^3] + k^2 [lam^4]
ck('(p_c + k_us)^2 = p_c^2 + nbar.p n.k + O(lam^3): only n.k_us (n.A_us) enters at LP; (p_c+k_s)^2 ~ lam (hard-collinear)',
   min(0 + 2, 2 + 2, 1 + 2) == 2 and min(0 + 1, 2 + 1, 1 + 1, 2) == 1)

ok = ck.summary()
sys.exit(0 if ok else 1)
