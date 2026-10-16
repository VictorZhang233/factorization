"""
check_real_me_numeric.py -- independent numerical check of the D-dimensional real-emission squared
matrix elements of real_me.py, using EXPLICIT Clifford algebras in D = 4, 6, 8, 10 (matrices of size
2^(D/2), traces rescaled to Tr 1 = 4), explicit momenta in the gamma*-parton c.m. frame and an explicit
sum over the D-2 PHYSICAL polarisation vectors of the gluon (instead of -g_{rho sigma}).

The symbolic results are polynomials in eps of low degree (two index contractions), so agreement at four
integer dimensions D = 4,6,8,10 (eps = 0,-1,-2,-3) checks the full eps dependence; it also verifies that
replacing the physical polarisation sum by -g_{rho sigma} is legitimate (current conservation / Ward
identity, checked explicitly as well: the amplitude contracted with the gluon momentum vanishes).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import sympy as sp
import real_me
from test_dirac import clifford

zs, ys, es = real_me.z, real_me.y, real_me.eps
Tq_g, Tq_pp = real_me.quark_channel()
Tg_g, Tg_pp = real_me.gluon_channel()
f_q_g = sp.lambdify((zs, ys, es), Tq_g)
f_q_pp = sp.lambdify((zs, ys, es), Tq_pp)
f_g_g = sp.lambdify((zs, ys, es), Tg_g)
f_g_pp = sp.lambdify((zs, ys, es), Tg_pp)


def kinematics(Dim, z, y):
    """Q^2 = 1.  c.m. frame of p+q; axis Dim-1 is the collision axis, axis 1 the emission plane."""
    s = (1 - z) / z
    rs = np.sqrt(s)
    pq = 1 / (2 * z)
    E = pq / rs
    p = np.zeros(Dim); p[0] = E; p[-1] = E
    q = np.zeros(Dim); q[0] = rs - E; q[-1] = -E
    c = 1 - 2 * y
    sn = np.sqrt(1 - c * c)
    k = np.zeros(Dim); k[0] = rs / 2; k[1] = rs / 2 * sn; k[-1] = rs / 2 * c
    return p, q, k, c, sn


def run(Dim, z, y):
    gam, eta = clifford(Dim)
    n = gam[0].shape[0]
    sl = lambda v: sum(eta[a, a] * v[a] * gam[a] for a in range(Dim))
    dot = lambda a, b: a @ eta @ b
    tr = lambda m: np.trace(m).real * 4.0 / n
    p, q, k, c, sn = kinematics(Dim, z, y)
    out = {}
    # ---------------- quark channel: gamma*(q) q(p) -> q(p') g(k)
    pp_ = p + q - k
    S, T = p + q, p - k
    s_, t_ = dot(S, S), dot(T, T)
    # physical polarisations of the outgoing gluon: orthogonal to k, zero time component
    pols = []
    e1 = np.zeros(Dim); e1[1] = c; e1[-1] = -sn
    pols.append(e1)
    for j in range(2, Dim - 1):
        e = np.zeros(Dim); e[j] = 1.0
        pols.append(e)
    assert len(pols) == Dim - 2
    for e in pols:
        assert abs(dot(e, k)) < 1e-12 and abs(dot(e, e) + 1) < 1e-12

    def A_q(nu_mat, eps_mat):      # u-bar(p') A u(p):  e S g^nu /s + g^nu T e /t
        return eps_mat @ sl(S) @ nu_mat / s_ + nu_mat @ sl(T) @ eps_mat / t_

    def Abar_q(mu_mat, eps_mat):   # reversed order
        return mu_mat @ sl(S) @ eps_mat / s_ + eps_mat @ sl(T) @ mu_mat / t_

    gmat = lambda a: gam[a]
    Tg = 0.0
    Tpp = 0.0
    for e in pols:
        E_ = sl(e)
        for mu in range(Dim):
            Tg += -eta[mu, mu] * tr(sl(p) @ Abar_q(gmat(mu), E_) @ sl(pp_) @ A_q(gmat(mu), E_))
        Tpp += tr(sl(p) @ Abar_q(sl(p), E_) @ sl(pp_) @ A_q(sl(p), E_))
    out['q_g'] = (Tg, f_q_g(z, y, (4 - Dim) / 2))
    out['q_pp'] = (Tpp, f_q_pp(z, y, (4 - Dim) / 2))
    # Ward identity: replace the gluon polarisation by its momentum -> amplitude vanishes between spinors;
    # test with the trace  Tr[p' A(k) p X]  for random X  (p-slash u(p) = 0 etc. are built in via traces)
    w = max(abs(np.trace(sl(pp_) @ A_q(gmat(mu), sl(k)) @ sl(p) @ gmat(nu2))) for mu in range(Dim)
            for nu2 in range(Dim))
    out['ward_q'] = w
    # ---------------- gluon channel: gamma*(q) g(p) -> q(k1) qbar(k2)
    k1 = k.copy()
    k2 = p + q - k1
    Av, Bv = k1 - q, k1 - p
    a2, b2 = dot(Av, Av), dot(Bv, Bv)
    polsg = []
    for j in range(1, Dim - 1):     # transverse to the collision axis: physical polarisations of p
        e = np.zeros(Dim); e[j] = 1.0
        polsg.append(e)

    def A_g(nu_mat, eps_mat):      # u-bar(k1) A v(k2):  g^nu A e /a2 + e B g^nu /b2
        return nu_mat @ sl(Av) @ eps_mat / a2 + eps_mat @ sl(Bv) @ nu_mat / b2

    def Abar_g(mu_mat, eps_mat):
        return eps_mat @ sl(Av) @ mu_mat / a2 + mu_mat @ sl(Bv) @ eps_mat / b2

    Tg = 0.0
    Tpp = 0.0
    for e in polsg:
        E_ = sl(e)
        for mu in range(Dim):
            Tg += -eta[mu, mu] * tr(sl(k1) @ A_g(gmat(mu), E_) @ sl(k2) @ Abar_g(gmat(mu), E_))
        Tpp += tr(sl(k1) @ A_g(sl(p), E_) @ sl(k2) @ Abar_g(sl(p), E_))
    out['g_g'] = (Tg, f_g_g(z, y, (4 - Dim) / 2))
    out['g_pp'] = (Tpp, f_g_pp(z, y, (4 - Dim) / 2))
    w = max(abs(np.trace(sl(k1) @ A_g(gmat(mu), sl(p)) @ sl(k2) @ gmat(nu2))) for mu in range(Dim)
            for nu2 in range(Dim))
    out['ward_g'] = w
    return out


if __name__ == '__main__':
    allok = True
    for Dim in (4, 6, 8, 10):
        for (z, y) in ((0.3, 0.27), (0.71, 0.83), (0.05, 0.5)):
            o = run(Dim, z, y)
            line = f'D={Dim:2d} z={z:4.2f} y={y:4.2f}:'
            for key in ('q_g', 'q_pp', 'g_g', 'g_pp'):
                num, sym = o[key]
                good = abs(num - sym) < 1e-8 * (1 + abs(sym))
                allok &= good
                line += f'  {key}: {num: .6e} vs {sym: .6e} {"ok" if good else "FAIL"}'
            wok = o['ward_q'] < 1e-8 and o['ward_g'] < 1e-8
            allok &= wok
            print(line + f'   Ward: {"ok" if wok else "FAIL"}')
    print('REAL ME NUMERIC CHECK:', 'ALL PASS' if allok else 'FAILURES')
