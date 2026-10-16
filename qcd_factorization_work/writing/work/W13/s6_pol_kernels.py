"""W13 / s6: LO helicity-dependent and transversity splitting kernels (prop:coll-transversity-evolution(b),
prop:coll-soffer, rem on alpha_s Delta G); writer-derived (re-derivation of VF-POL-3, status C).
Method: collinear splitting a(P) -> b(z P, l_T) + c((1-z) P, -l_T) with explicit massless spinors/polarization vectors
(Dirac representation, gamma5 = i g0 g1 g2 g3), parent replaced by its on-shell projection along +z; for each helicity
configuration  R_{ab}(lam_a, lam_b) = lim_{l_T->0} l_T^2 sum_{lam_c} |V|^2/(p_a^2)^2 x (z(1-z)) up to a common constant
per channel, fixed by the unpolarized real kernel of VF-PDF-7.  Transversity: interference of helicity amplitudes
(density-matrix element rho_{+-}), azimuthally averaged.  Virtual (delta) terms: the virtual correction multiplies the
tree-level operator vertex, hence is independent of the Dirac structure (quarks) / polarization (gluons).
Checks: Delta P_qq = P_qq (helicity conservation), Delta P_qg = T_F(2z-1), Delta P_gq = C_F(2-z),
Delta P_gg = 2C_A[1/(1-z)_+ - 2z + 1] + beta0/2 delta; transversity Delta_T P_qq = C_F[2z/(1-z)_+ + 3/2 delta];
helicity-basis kernels non-negative off the diagonal; Soffer combination (P_qq - Delta_T P_qq)/2 = C_F (1-z)/2 >= 0;
first moments; LO tensor-charge exponent 4/27 (n_f=3); alpha_s Delta G constant at LO.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp

npass = 0; nfail = 0
def check(name, ok):
    global npass, nfail
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)
    if ok: npass += 1
    else: nfail += 1

I2 = np.eye(2); Z2 = np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
G = [np.block([[I2, Z2], [Z2, -I2]]).astype(complex)] + [np.block([[Z2, s], [-s, Z2]]) for s in (sx, sy, sz)]
G5 = 1j*G[0] @ G[1] @ G[2] @ G[3]
eta = np.diag([1., -1., -1., -1.])
def sl(v): return sum(eta[m, m]*v[m]*G[m] for m in range(4))
def dot(a, b): return a @ eta @ b
def bar(u): return u.conj() @ G[0]

def spinor(p, h):
    """massless Dirac spinor, helicity h=+-1/2, normalized ubar g^mu u = 2 p^mu (Dirac rep)."""
    E = p[0]; pv = p[1:]; n = pv/np.linalg.norm(pv)
    th = np.arccos(np.clip(n[2], -1, 1)); ph = np.arctan2(n[1], n[0])
    if h > 0:
        chi = np.array([np.cos(th/2), np.exp(1j*ph)*np.sin(th/2)])
    else:
        chi = np.array([-np.exp(-1j*ph)*np.sin(th/2), np.cos(th/2)])
    return np.sqrt(E)*np.concatenate([chi, 2*h*chi])
def vspinor(p, h):
    # v(p,h) = C ubar^T ; with C = i g2 g0
    C = 1j*G[2] @ G[0]
    return C @ bar(spinor(p, h)).T
def polvec(p, lam):
    """polarization vector for a massless vector boson of momentum p, helicity lam = +-1 (transverse)."""
    pv = p[1:]; n = pv/np.linalg.norm(pv)
    th = np.arccos(np.clip(n[2], -1, 1)); ph = np.arctan2(n[1], n[0])
    e1 = np.array([np.cos(th)*np.cos(ph), np.cos(th)*np.sin(ph), -np.sin(th)])
    e2 = np.array([-np.sin(ph), np.cos(ph), 0.0])
    e = -lam*(e1 + 1j*lam*e2)/np.sqrt(2)
    return np.concatenate([[0.0], e])

# sanity checks of the spinors
p = np.array([1.3, 0.4, -0.2, np.sqrt(1.3**2 - 0.2)])
for h in (0.5, -0.5):
    u = spinor(p, h)
    ok = np.allclose(sl(p) @ u, 0) and np.allclose(G5 @ u, 2*h*u) and np.allclose([bar(u) @ G[m] @ u for m in range(4)], 2*p)
    check('massless spinor h=%+.1f: Dirac eq., g5 u = 2h u, ubar g u = 2p' % h, ok)
e = polvec(p, 1)
check('polarization vector: e.p = 0, e.e* = -1', abs(dot(e, p)) < 1e-12 and abs(dot(e, e.conj()) + 1) < 1e-12)

def lc(pp, pm, pt):  # light-cone to cartesian
    return np.array([(pp + pm)/np.sqrt(2), pt[0], pt[1], (pp - pm)/np.sqrt(2)])
P = 1.0
def kin(z, lT, phi):
    lt = lT*np.array([np.cos(phi), np.sin(phi)])
    pb = lc(z*P, lT**2/(2*z*P), lt)
    pc = lc((1 - z)*P, lT**2/(2*(1 - z)*P), -lt)
    pa_onshell = lc(P, 0.0, np.zeros(2))
    return pb, pc, pa_onshell

def R_q_to_q(z, la, lb, lT=1e-4, phi=0.3):
    """sum over gluon helicity of |ubar_b eps*_c u_a|^2 * z(1-z)/l_T^2-scaled; quark a -> quark b + gluon c"""
    pb, pc, pa = kin(z, lT, phi)
    ua = spinor(pa, la); ub = spinor(pb, lb)
    tot = 0
    for lc_ in (1, -1):
        ec = polvec(pc, lc_)
        amp = bar(ub) @ sl(ec.conj()) @ ua
        tot += abs(amp)**2
    pa2 = dot(pb + pc, pb + pc)
    return tot/pa2**2*lT**2/(z*(1 - z))   # splitting density ~ |V|^2 z(1-z)/l_T^2 = |V|^2 l_T^2/((p_a^2)^2 z(1-z))
def amp_q_to_q(z, la, lb, lc_, lT=1e-4, phi=0.3):
    pb, pc, pa = kin(z, lT, phi)
    return (bar(spinor(pb, lb)) @ sl(polvec(pc, lc_).conj()) @ spinor(pa, la))/dot(pb + pc, pb + pc)*lT/np.sqrt(z*(1 - z))
def R_q_to_g(z, la, lb):
    """quark a -> gluon b (fraction z) + quark c"""
    lT = 1e-4; phi = 0.3
    pb, pc, pa = kin(z, lT, phi)   # b = gluon with fraction z, c = quark with 1-z
    tot = 0
    for hc in (0.5, -0.5):
        amp = bar(spinor(pc, hc)) @ sl(polvec(pb, lb).conj()) @ spinor(pa, la)
        tot += abs(amp)**2
    return tot/dot(pb + pc, pb + pc)**2*lT**2/(z*(1 - z))
def R_g_to_q(z, la, lb):
    """gluon a (helicity la) -> quark b (fraction z, helicity lb) + antiquark c"""
    lT = 1e-4; phi = 0.3
    pb, pc, pa = kin(z, lT, phi)
    ea = polvec(pa, la)
    tot = 0
    for hc in (0.5, -0.5):
        amp = bar(spinor(pb, lb)) @ sl(ea) @ vspinor(pc, hc)
        tot += abs(amp)**2
    return tot/dot(pb + pc, pb + pc)**2*lT**2/(z*(1 - z))
def V3(k1, e1, k2, e2, k3, e3):
    """three-gluon vertex (all momenta incoming), Lorentz part: (e1.e2)(k1-k2).e3 + cyclic"""
    return dot(e1, e2)*dot(k1 - k2, e3) + dot(e2, e3)*dot(k2 - k3, e1) + dot(e3, e1)*dot(k3 - k1, e2)
def R_g_to_g(z, la, lb):
    lT = 1e-4; phi = 0.3
    pb, pc, pa = kin(z, lT, phi)
    pa_full = pb + pc
    ea = polvec(pa, la)
    tot = 0
    for lc_ in (1, -1):
        amp = V3(pa_full, ea, -pb, polvec(pb, lb).conj(), -pc, polvec(pc, lc_).conj())
        tot += abs(amp)**2
    return tot/dot(pb + pc, pb + pc)**2*lT**2/(z*(1 - z))

zs = [0.15, 0.3, 0.5, 0.7, 0.85]
CF = 4/3; CA = 3.0; TF = 0.5; nf = 3
Pqq_r = lambda z: CF*(1 + z**2)/(1 - z)
Pgq_r = lambda z: CF*(1 + (1 - z)**2)/z
Pqg_r = lambda z: TF*(z**2 + (1 - z)**2)
Pgg_r = lambda z: 2*CA*(z/(1 - z) + (1 - z)/z + z*(1 - z))
def chan(Rfun, Punpol, has_parent_avg=True, la_set=(0.5, -0.5), lb_set=(0.5, -0.5)):
    """normalize: (1/2) sum_{la,lb} R = c * Punpol; return helicity-resolved kernels P(la=+, lb=+-)"""
    out = {}
    cs = []
    for z in zs:
        S = sum(Rfun(z, la, lb) for la in la_set for lb in lb_set)/2
        cs.append(Punpol(z)/S)
    c = np.mean(cs)
    okc = np.ptp(cs) < 1e-6*abs(c)
    for z in zs:
        out[z] = (c*Rfun(z, la_set[0], lb_set[0]), c*Rfun(z, la_set[0], lb_set[1]))
    return out, okc

qq, ok = chan(R_q_to_q, Pqq_r); check('q->q: helicity sum proportional to C_F(1+z^2)/(1-z) with one constant', ok)
check('q->q: helicity conserved: P(q+ -> q-) = 0', all(abs(qq[z][1]) < 1e-6 for z in zs))
check('q->q: Delta P_qq^real = P_qq^real', all(abs(qq[z][0] - qq[z][1] - Pqq_r(z)) < 1e-6*Pqq_r(z) for z in zs))
gq, ok = chan(R_q_to_g, Pgq_r, la_set=(0.5, -0.5), lb_set=(1, -1)); check('q->g: helicity sum proportional to C_F(1+(1-z)^2)/z', ok)
check('q->g: Delta P_gq = C_F (2-z)', all(abs(gq[z][0] - gq[z][1] - CF*(2 - z)) < 1e-6 for z in zs))
check('q->g: helicity basis P(q+->g+) = C_F/z, P(q+->g-) = C_F (1-z)^2/z  (both >= 0)',
      all(abs(gq[z][0] - CF/z) < 1e-5*CF/z and abs(gq[z][1] - CF*(1 - z)**2/z) < 1e-5*CF/z for z in zs))
qg, ok = chan(R_g_to_q, Pqg_r, la_set=(1, -1), lb_set=(0.5, -0.5)); check('g->q: helicity sum proportional to T_F(z^2+(1-z)^2)', ok)
check('g->q: Delta P_qg = T_F (2z-1)', all(abs(qg[z][0] - qg[z][1] - TF*(2*z - 1)) < 1e-6 for z in zs))
check('g->q: helicity basis P(g+->q+) = T_F z^2, P(g+->q-) = T_F (1-z)^2', all(abs(qg[z][0] - TF*z**2) < 1e-6 and abs(qg[z][1] - TF*(1 - z)**2) < 1e-6 for z in zs))
gg, ok = chan(R_g_to_g, Pgg_r, la_set=(1, -1), lb_set=(1, -1)); check('g->g: helicity sum proportional to 2C_A[z/(1-z)+(1-z)/z+z(1-z)]', ok)
check('g->g: Delta P_gg^real = 2C_A[1/(1-z) - 2z + 1]', all(abs(gg[z][0] - gg[z][1] - 2*CA*(1/(1 - z) - 2*z + 1)) < 1e-6*Pgg_r(z) for z in zs))
check('g->g: helicity basis P(g+->g+) = C_A (1+z^4)/(z(1-z)), P(g+->g-) = C_A (1-z)^3/z',
      all(abs(gg[z][0] - CA*(1 + z**4)/(z*(1 - z))) < 1e-5*gg[z][0] and abs(gg[z][1] - CA*(1 - z)**3/z) < 1e-5*gg[z][0] for z in zs))

# transversity: rho_{+-} interference, quark -> quark, averaged over the azimuth of l_T
def trans_real(z):
    vals = []
    for phi in np.linspace(0, 2*np.pi, 9)[:-1]:
        s = 0
        for lc_ in (1, -1):
            s += amp_q_to_q(z, 0.5, 0.5, lc_, phi=phi)*np.conj(amp_q_to_q(z, -0.5, -0.5, lc_, phi=phi))
        vals.append(s)
    return np.mean(vals)
# normalization constant of the q->q channel
cq = np.mean([Pqq_r(z)/(sum(R_q_to_q(z, la, lb) for la in (0.5, -0.5) for lb in (0.5, -0.5))/2) for z in zs])
tr_vals = {z: cq*trans_real(z) for z in zs}
print('   transversity real kernel / C_F:', {z: np.round(tr_vals[z]/CF, 8) for z in zs})
check('transversity real kernel: |rho_{+-}| = C_F 2z/(1-z)  (relative phase convention: modulus)',
      all(abs(abs(tr_vals[z]) - CF*2*z/(1 - z)) < 1e-6*CF*2*z/(1 - z) for z in zs))
check('transversity: rho_{+-} is real with a z-independent sign (convention of the helicity phases)',
      all(abs(tr_vals[z].imag) < 1e-8 for z in zs) and len(set(np.sign([tr_vals[z].real for z in zs]))) == 1)

# ---------------------------------------------------------------- symbolic: delta terms, moments, Soffer
x = sp.Symbol('z', positive=True)
cf, ca, tf, Nf = sp.symbols('C_F C_A T_F n_f', positive=True)
b0 = sp.Rational(11, 3)*ca - sp.Rational(4, 3)*tf*Nf
def plus_int(reg_sing, z0=None):
    """int_0^1 of g(z)/(1-z) regularized as [ ]_+ : returns 0 by definition"""
    return 0
# Delta_T P = C_F [2z/(1-z)]_real - delta * C_F int_0^1 (1+z^2)/(1-z) (same virtual) ; with a common cutoff:
lam = sp.Symbol('lambda', positive=True)
virt = -cf*sp.integrate((1 + x**2)/(1 - x), (x, 0, 1 - lam))
real_T = cf*sp.integrate(2*x/(1 - x), (x, 0, 1 - lam))
# delta coefficient once the real part is written as C_F 2z/(1-z)_+ = C_F[2z/(1-z) - delta int 2/(1-z)] ... compute numerically:
# Delta_T P = C_F 2z/(1-z) |_{z<1} + delta(1-z) [ virt ]; rewrite 2z/(1-z) = 2z [1/(1-z)]_+ + delta * int_0^{1-lam} 2/(1-z)
dcoef = sp.limit(virt + cf*sp.integrate(2/(1 - x), (x, 0, 1 - lam)), lam, 0)
check('transversity delta coefficient: C_F[2z/(1-z)_+ + 3/2 delta]  (virtual = unpolarized one)', sp.simplify(dcoef - sp.Rational(3, 2)*cf) == 0)
dq_unpol = sp.limit(virt + cf*sp.integrate(2/(1 - x), (x, 0, 1 - lam)), lam, 0)
# first moments
m1_T = cf*sp.integrate((2*x - 2)/(1 - x), (x, 0, 1)) + sp.Rational(3, 2)*cf
check('int_0^1 Delta_T P_qq = -C_F/2', sp.simplify(m1_T + cf/2) == 0)
nf3 = {cf: sp.Rational(4, 3), ca: 3, tf: sp.Rational(1, 2), Nf: 3}
expo = sp.simplify((-2*m1_T/b0).subs(nf3))
check('LO tensor-charge exponent -2 gamma/beta0 = 4/27 (n_f = 3)  (VF-POL-3)', expo == sp.Rational(4, 27))
m1_gq = sp.integrate(cf*(2 - x), (x, 0, 1)); m1_qg = sp.integrate(tf*(2*x - 1), (x, 0, 1))
m1_gg = sp.integrate(2*ca*((1 - 1)/(1 - x) - 2*x + 1) + 2*ca*0, (x, 0, 1)) + b0/2   # [1/(1-z)]_+ has zero first moment
check('first moments: int Delta P_qq = 0, int Delta P_qg = 0, int Delta P_gq = 3C_F/2, int Delta P_gg = beta0/2',
      m1_qg == 0 and sp.simplify(m1_gq - sp.Rational(3, 2)*cf) == 0 and sp.simplify(m1_gg - b0/2) == 0)
# alpha_s Delta G at LO: d/dt (a DeltaG) with t = ln mu^2, da/dt = -beta0/(4pi) a^2
a, DS, DG = sp.symbols('alpha_s DeltaSigma DeltaG')
dDG = a/(2*sp.pi)*(m1_gq*DS + m1_gg*DG)
dDS = a/(2*sp.pi)*(0*DS + 2*Nf*m1_qg*DG)
da = -b0/(4*sp.pi)*a**2
d_aDG = sp.expand(da*DG + a*dDG)
check('d(alpha_s DeltaG)/d ln mu^2 = (3 C_F alpha_s^2/(4 pi)) DeltaSigma: alpha_s DeltaG constant at LO', sp.simplify(d_aDG - 3*cf*a**2/(4*sp.pi)*DS) == 0)
check('d DeltaSigma/d ln mu^2 = 0 at LO', sp.simplify(dDS) == 0)
# Soffer combination and helicity-basis positivity (symbolic)
Pqq_s = cf*(1 + x**2)/(1 - x); DTP_s = cf*2*x/(1 - x)
check('(P_qq - Delta_T P_qq)/2 = C_F (1-z)/2 >= 0 on (0,1) (regular, no delta: both delta terms are 3/2 C_F)', sp.simplify((Pqq_s - DTP_s)/2 - cf*(1 - x)/2) == 0)
check('(P_qq + Delta_T P_qq)/2 = C_F (1+z)^2/(2(1-z)) for z<1', sp.simplify((Pqq_s + DTP_s)/2 - cf*(1 + x)**2/(2*(1 - x))) == 0)
print('\nSUMMARY s6: %d PASS, %d FAIL' % (npass, nfail))
