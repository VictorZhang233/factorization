#!/usr/bin/env python3
"""E20 (stage 2): i0 prescription of the u-channel denominator in Ji's DVCS amplitude.

Method (independent of stage 1, which projected light-cone correlators with traces):
 (A) exact symbolic propagator denominators in Ji's OWN parametrization (hep-ph/9603249v1, eq. (14));
 (B) exact tree-level Compton amplitude on an on-shell massless QUARK target, explicit helicity spinors,
     no Fierz/trace projection, compared at large Q^2 with the corrected LO formula
     T = g_perp sum e^2 int F [1/(x-xi+i0) + 1/(x+xi-i0)] - i eps_perp sum e^2 int Ft [1/(x-xi+i0) - 1/(x+xi-i0)]
     (for the quark target H = Ht = delta(1-x), so the i0 is irrelevant; this tests signs/normalization);
 (C) crossing analyticity: with -i0 the C-even amplitude is the boundary value of ONE analytic function
     A(z) = int_0^1 dx F^(+)(x)/(x - z) at z = xi - i0, hence obeys the dispersion relation on [0,1]
     and Im T^{11} = pi sum e^2 (q + qbar) >= 0;  with Ji's +i0 it is not, and Im T^{11} ~ (q - qbar).
Conventions: metric (+,-,-,-); chiral Dirac matrices; gamma5 = i g0 g1 g2 g3; eps^{0123} = +1 (the
alternative -1 is also tried); T^{mu nu} = i int d^4z e^{i q'.z} <P'|T J^mu(z) J^nu(0)|P>  (mu = outgoing,
nu = incoming photon; identical to Ji's T = i int d^4y e^{-iq.y}<P'|T J^nu(y) J^mu(0)|P> by translation).
Run: python3 -I e20_dvcs_s2.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp

PASS = []
def check(name, ok, info=''):
    PASS.append(bool(ok))
    print(('PASS ' if ok else 'FAIL ') + name + ('  ' + info if info else ''))

# ---------------------------------------------------------------- (A) symbolic denominators
x, xi, Q2, Mb2, eta = sp.symbols('x xi Q2 Mbar2 eta', positive=True)
d1, d2 = sp.symbols('d1 d2', real=True)            # Delta_perp components
# light-cone algebra: p^2 = n^2 = 0, p.n = 1, transverse orthogonal to p, n; vectors as (a_p, a_n, perp)
def dot(a, b):
    return a[0]*b[1] + a[1]*b[0] - (a[2][0]*b[2][0] + a[2][1]*b[2][1])
def add(a, b, s=1):
    return (a[0] + s*b[0], a[1] + s*b[1], (a[2][0] + s*b[2][0], a[2][1] + s*b[2][1]))
q = (-xi, Q2/(2*xi), (0, 0))                         # Ji eq. (14)
Delta = (-xi, xi*Mb2/2, (d1, d2))                    # Delta = -xi(p - Mbar^2/2 n) + Delta_perp
qp = add(q, Delta, -1)                               # q' = q - Delta
k_in = (x + xi/2, 0, (0, 0))                         # collinear active quark leaving the nucleon
k_out = (x - xi/2, 0, (0, 0))                        # returning quark; k_out = k_in + Delta at LO (plus comp.)
ls = add(k_in, q)                                    # s-channel line
lu = add(k_in, qp, -1)                               # u-channel line
ls2 = sp.simplify(dot(ls, ls)); lu2 = sp.expand(dot(lu, lu))
check('(A1) s-channel: (k+q)^2 = (Q^2/xi)(x - xi/2) exactly', sp.simplify(ls2 - Q2/xi*(x - xi/2)) == 0, str(ls2))
lead_u = sp.limit(lu2/Q2, Q2, sp.oo)
check('(A2) u-channel: (k-q\')^2/Q^2 -> -(x + xi/2)/xi at leading power', sp.simplify(lead_u + (x + xi/2)/xi) == 0, str(sp.factor(lead_u)))
# i0: 1/(l^2 + i eta) with eta>0
Ps = sp.simplify((ls2 + sp.I*eta) / (Q2/xi))         # = x - xi/2 + i eta xi/Q2 : +i0 in x
Pu = sp.simplify((-(Q2/xi)*(x + xi/2) + sp.I*eta) / (-(Q2/xi)))   # = x + xi/2 - i eta xi/Q2 : -i0 in x
check('(A3) s-channel denominator is (x - xi/2 + i0)', sp.simplify(sp.im(Ps)) .is_positive, str(sp.simplify(Ps)))
check('(A4) u-channel denominator is -(Q^2/xi)(x + xi/2 - i0)  ->  -i0 in the second bracket term',
      sp.simplify(sp.im(Pu)).is_negative, str(sp.simplify(Pu)))

# ---------------------------------------------------------------- (B) quark-target helicity amplitudes
g0 = np.array([[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]], complex)
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex), np.array([[1, 0], [0, -1]], complex)]
gam = [g0] + [np.block([[np.zeros((2, 2)), s], [-s, np.zeros((2, 2))]]) for s in sig]
g5 = 1j*gam[0] @ gam[1] @ gam[2] @ gam[3]
metric = np.diag([1., -1., -1., -1.])
def slash(v):            # v contravariant
    vl = metric @ v
    return sum(gam[m]*vl[m] for m in range(4))
def lc_eps(s0123):
    import itertools
    e = np.zeros((4, 4, 4, 4))
    for perm in itertools.permutations(range(4)):
        sgn = np.linalg.det(np.eye(4)[list(perm)])
        e[perm] = s0123*round(sgn)
    return e
def spinor(pv, h):       # massless helicity spinor, chiral rep: u = (sqrt(p.sigma) chi, sqrt(p.sigmabar) chi)
    E = pv[0]; nvec = pv[1:]/np.linalg.norm(pv[1:])
    sn = sum(nvec[i]*sig[i] for i in range(3))
    w, V = np.linalg.eigh(sn)
    chi = V[:, np.argmax(w)] if h > 0 else V[:, np.argmin(w)]
    up = np.sqrt(2*E)*chi
    return np.concatenate([np.zeros(2), up]) if h > 0 else np.concatenate([up, np.zeros(2)])
def bar(u):
    return u.conj() @ g0

check('(B0) gamma5 = diag(-1,-1,1,1) in chiral rep; Tr(g0 g1 g2 g3 g5) = -4i',
      np.allclose(g5, np.diag([-1, -1, 1, 1])) and np.isclose(np.trace(gam[0] @ gam[1] @ gam[2] @ gam[3] @ g5), -4j))

Lam = 1/np.sqrt(2)
pJ = Lam*np.array([1, 0, 0, 1.]); nJ = np.array([1, 0, 0, -1.])/(2*Lam)     # Ji: p.n = 1
def amplitude_check(xiJ, t, Q2v, phi, s0123):
    Mb2v = -t/4.0                                     # massless target: Mbar^2 = M^2 - t/4
    dperp = np.sqrt(-t*(1 - xiJ**2/4))
    Dp = np.array([0, dperp*np.cos(phi), dperp*np.sin(phi), 0])
    Pbar = pJ + Mb2v/2*nJ
    Dl = -xiJ*(pJ - Mb2v/2*nJ) + Dp
    P = Pbar - Dl/2; Pp = Pbar + Dl/2
    qv = -xiJ*pJ + Q2v/(2*xiJ)*nJ; qpv = qv - Dl
    mdot = lambda a, b: a @ metric @ b
    assert abs(mdot(P, P)) < 1e-9 and abs(mdot(Pp, Pp)) < 1e-9
    eps = lc_eps(s0123)
    pl = metric @ pJ; nl = metric @ nJ
    epsperp = np.einsum('abcd,c,d->ab', eps, pl, nl)    # eps^{mu nu rho sigma} p_rho n_sigma  (p = nbar along hadron)
    gperp = np.linalg.inv(metric) - np.outer(pJ, nJ) - np.outer(nJ, pJ)
    xim = xiJ/2                                           # modern skewness
    out = {}
    for h in (+1, -1):
        u = spinor(P, h); ub = bar(spinor(Pp, h))
        T = np.zeros((4, 4), complex)
        for mu in range(4):
            for nu in range(4):
                s_ = gam[mu] @ slash(P + qv) @ gam[nu] / mdot(P + qv, P + qv)
                u_ = gam[nu] @ slash(P - qpv) @ gam[mu] / mdot(P - qpv, P - qpv)
                T[mu, nu] = -(ub @ (s_ + u_) @ u)
        F = (ub @ slash(nJ) @ u)/2.0                      # (1/2Pbar^+) ubar gamma^+ u, Pbar^+ = Pbar.n = 1
        Ft = (ub @ slash(nJ) @ g5 @ u)/2.0
        Cv = 1/(1 - xim) + 1/(1 + xim); Ca = 1/(1 - xim) - 1/(1 + xim)
        Tclaim = gperp*F*Cv - 1j*epsperp*Ft*Ca
        # Ji (PRL v1 eq. 15), his notation, x = 1, xi_Ji: -(1/2)(p n + n p - g) Cv' [H ubar nslash u] - (i/2) eps p n Ca' [Ht ubar nslash g5 u]
        CvJ = 1/(1 - xiJ/2) + 1/(1 + xiJ/2); CaJ = 1/(1 - xiJ/2) - 1/(1 + xiJ/2)
        TJi = -0.5*(np.outer(pJ, nJ) + np.outer(nJ, pJ) - np.linalg.inv(metric))*CvJ*(ub @ slash(nJ) @ u) \
              - 0.5j*epsperp*CaJ*(ub @ slash(nJ) @ g5 @ u)
        idx = [1, 2]
        scale = np.max(np.abs(T[np.ix_(idx, idx)]))
        out[h] = (np.max(np.abs((T - Tclaim)[np.ix_(idx, idx)]))/scale,
                  np.max(np.abs((T - TJi)[np.ix_(idx, idx)]))/scale, F, Ft)
    return out

for Q2v in (1e3, 1e5, 1e7):
    o = amplitude_check(0.4, -0.3, Q2v, 0.7, +1)
    print(f'   Q^2={Q2v:.0e}: rel.dev.(claim) h=+: {o[1][0]:.2e}, h=-: {o[-1][0]:.2e};  rel.dev.(Ji form) h=+: {o[1][1]:.2e}, h=-: {o[-1][1]:.2e}')
o7 = amplitude_check(0.4, -0.3, 1e7, 0.7, +1)
o5 = amplitude_check(0.4, -0.3, 1e5, 0.7, +1)
check('(B1) exact quark-target T^{ij} (transverse) -> corrected LO formula, eps^{0123}=+1 (both helicities)',
      max(o7[1][0], o7[-1][0]) < 5e-3 and max(o7[1][0], o7[-1][0]) < max(o5[1][0], o5[-1][0]),
      f'rel. dev. {max(o7[1][0], o7[-1][0]):.1e} at Q^2=1e7 (decreasing ~ t/Q^2)')
check('(B2) Ji PRL eq. (15) structure (away from poles) agrees, with eps^{0123}=+1, gamma5 = i g0g1g2g3',
      max(o7[1][1], o7[-1][1]) < 5e-3)
om = amplitude_check(0.4, -0.3, 1e7, 0.7, -1)
check('(B3) negative control: eps^{0123} = -1 gives a wrong axial term', min(om[1][0], om[-1][0]) > 0.1,
      f'rel. dev. {min(om[1][0], om[-1][0]):.2f}')
check('(B4) quark target: Ft/F = +1 for h=+, -1 for h=- (gamma5 u_R = +u_R)',
      np.isclose(o7[1][3]/o7[1][2], 1) and np.isclose(o7[-1][3]/o7[-1][2], -1))

# ---------------------------------------------------------------- (C) analyticity / positivity
import mpmath as mp
mp.mp.dps = 30
def qf(x):  return x**mp.mpf(-0.5)*(1-x)**3
def qbf(x): return mp.mpf('0.3')*x**mp.mpf(-0.5)*(1-x)**7
def F(x):                                   # GPD-like function in the forward limit: q for x>0, -qbar(-x) for x<0
    return qf(x) if x > 0 else -qbf(-x)
def pv(f, lo, hi, a):
    """PV int_lo^hi f(x)/(x-a) dx for lo < a < hi, by subtraction; f may have integrable endpoint singularities."""
    fa = f(a)
    g = lambda x: (f(x) - fa)/(x - a)
    return mp.quad(g, [lo, a, hi]) + fa*mp.log((hi - a)/(a - lo))
xi0 = mp.mpf('0.2')
# Re A computed DIRECTLY from the original two-term PV integral over [-1,1] (same for both prescriptions):
ReA = (pv(lambda x: F(x), mp.mpf(0), 1, xi0) + mp.quad(lambda x: F(x)/(x - xi0), [-1, 0])
       + mp.quad(lambda x: F(x)/(x + xi0), [0, 1]) + pv(lambda x: F(x), -1, mp.mpf(0), -xi0))
# imaginary parts from Sokhotski-Plemelj:  1/(x-a+i0) -> -i pi delta,  1/(x-a-i0) -> +i pi delta
ImA_corr = lambda t: -mp.pi*(F(t) - F(-t))             # corrected: second term -i0  -> -pi (q + qbar)
ImA_Ji = lambda t: -mp.pi*(F(t) + F(-t))               # Ji PRL v1: second term +i0 -> -pi (q - qbar)
# crossing-symmetric dispersion relation for an amplitude that is the boundary value (xi - i0, i.e. nu + i0)
# of ONE function analytic off the cuts [-1,0] U [0,1]:  Re A(xi) = -(1/pi) PV int_0^1 dx Im A(x) [1/(x-xi) + 1/(x+xi)]
def disp(ImA):
    return -(1/mp.pi)*(pv(ImA, mp.mpf(0), 1, xi0) + mp.quad(lambda t: ImA(t)/(t + xi0), [0, 1]))
dc, dj = disp(ImA_corr), disp(ImA_Ji)
check('(C1) crossing-symmetric dispersion relation holds with -i0 (Re A computed independently on [-1,1])',
      abs(ReA - dc) < 1e-12*abs(ReA), f'Re A = {mp.nstr(ReA, 12)}, dispersion of Im A = {mp.nstr(dc, 12)}')
check('(C2) ... and fails with Ji\'s +i0 when qbar != 0', abs(ReA - dj) > 1e-3*abs(ReA), f'dispersion of Im A_Ji = {mp.nstr(dj, 12)}')
# forward limit: T^{11} = g_perp^{11} A = -A (e_q = 1); must have Im T^{11} = 2 pi F_1 = pi (q + qbar) >= 0
check('(C3) Im T^{11} = pi (q + qbar)(xi) = 2 pi F_1 > 0 with -i0', abs(-ImA_corr(xi0) - mp.pi*(qf(xi0) + qbf(xi0))) < 1e-20)
check('(C4) with +i0: Im T^{11} = pi (q - qbar): antiquarks enter with the wrong sign', abs(-ImA_Ji(xi0) - mp.pi*(qf(xi0) - qbf(xi0))) < 1e-20)
# finite-eta cross-check of the Sokhotski-Plemelj step (direct numerical integration, eta -> 0)
def A_eta(eta, sgn2):
    f = lambda x: F(x)*(1/(x - xi0 + 1j*eta) + 1/(x + xi0 + sgn2*1j*eta))
    return mp.quad(f, [-1, -xi0 - 50*eta, -xi0, -xi0 + 50*eta, 0, xi0 - 50*eta, xi0, xi0 + 50*eta, 1], maxdegree=10)
for eta in (mp.mpf('1e-3'), mp.mpf('1e-4')):
    ac, aj = A_eta(eta, -1), A_eta(eta, +1)
    print(f'   eta={mp.nstr(eta,2)}: Im A(-i0) = {mp.nstr(ac.imag, 8)} (expect {mp.nstr(ImA_corr(xi0), 8)}), '
          f'Im A(+i0) = {mp.nstr(aj.imag, 8)} (expect {mp.nstr(ImA_Ji(xi0), 8)}); Re = {mp.nstr(ac.real, 8)} vs {mp.nstr(ReA, 8)}')
check('(C5) finite-eta integration reproduces both imaginary parts (eta = 1e-4)',
      abs(ac.imag - ImA_corr(xi0)) < 2e-2*abs(ImA_corr(xi0)) and abs(aj.imag - ImA_Ji(xi0)) < 2e-2*abs(ImA_Ji(xi0)))

print(f'\nSUMMARY: {sum(PASS)}/{len(PASS)} PASS')
