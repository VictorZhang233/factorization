"""
W10 / Ch9 sec:method-ward and App F -- independent numerical checks (own toolkit w10_dirac.py) of
 (W1)-(W5) [VF-WL-6], the abelian / non-abelian fermion-line identity, gamma* -> q qbar g with eps -> k [VF-WL-7],
 the DIS seed of the PDF Wilson line with one and two K gluons [VF-WL-8], the non-abelian tree identity
 q qbar -> g* g*, its ghost term and the ghost-subtracted polarization sum + CKR cross section [VF-WL-9].
 Coupling g = 1 unless stated; amplitudes = sum of Feynman diagrams (= i M).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from w10_dirac import *

npass = 0; nfail = 0
def check(name, val, tol=1e-10):
    global npass, nfail
    ok = val < tol
    npass += ok; nfail += (not ok)
    print(('[PASS] ' if ok else '[FAIL] ') + '%s : %.3e' % (name, val))
def rel(a, b):
    a = np.asarray(a); b = np.asarray(b)
    return np.max(np.abs(a - b))/max(np.max(np.abs(b)), 1e-300)

rng = np.random.default_rng(20261014)
g = 1.0
for m in [0.0, 0.7]:
    p = rnd_vec(rng); k = rnd_vec(rng)
    lhs = S(p+k, m) @ (1j*g*slash(k)) @ S(p, m)
    rhs = g*(S(p+k, m) - S(p, m))
    check('(W1) S(p+k) i g kslash S(p) = g[S(p+k)-S(p)], m=%.1f' % m, rel(lhs, rhs))
    # on-shell ends
    def onshell(mass):
        pv = rng.normal(size=3); E = np.sqrt(pv @ pv + mass**2)
        return np.array([E, *pv], dtype=complex)
    pp = onshell(m); kk = rnd_vec(rng)
    for u in u_spinors(pp, m):
        check('(W2) ubar(p\') i g kslash S(p\'-k) = g ubar(p\'), m=%.1f' % m, rel(bar(u) @ (1j*g*slash(kk)) @ S(pp-kk, m), g*bar(u)))
        check('(W2) S(p+k) i g kslash u(p) = -g u(p), m=%.1f' % m, rel(S(pp+kk, m) @ (1j*g*slash(kk)) @ u, -g*u))
    for v in v_spinors(pp, m):
        check('(W2) vbar(p) i g kslash S(-p-k) = +g vbar(p), m=%.1f' % m, rel(bar(v) @ (1j*g*slash(kk)) @ S(-pp-kk, m), g*bar(v)))
        check('(W2) S(-p+k) i g kslash v(p) = -g v(p), m=%.1f' % m, rel(S(-pp+kk, m) @ (1j*g*slash(kk)) @ v, -g*v))

# (W3) three-gluon vertex, kinematic part
q1 = rnd_vec(rng); q2 = rnd_vec(rng); q3 = -q1 - q2
G = np.diag([1.0, -1, -1, -1])
mx = 0
for nu in range(4):
    for rho in range(4):
        lhs = sum(lower(q1)[mu]*V3(q1, q2, q3, mu, nu, rho) for mu in range(4))
        rhs = (mdot(q3, q3)*G[nu, rho] - q3[nu]*q3[rho]) - (mdot(q2, q2)*G[nu, rho] - q2[nu]*q2[rho])
        mx = max(mx, abs(lhs - rhs))
check('(W3) q1_mu V^{mu nu rho}(q1,q2,q3) = (q3^2 g - q3 q3) - (q2^2 g - q2 q2)  [x g f^{abc}]', mx)
# (W4) ghost vertex: k.p' = (p'^2 - p^2 + k^2)/2, p' = p + k
pg = rnd_vec(rng); kg = rnd_vec(rng); ppg = pg + kg
check('(W4) k_mu(-g f p\'^mu) = -(g/2) f (p\'^2 - p^2 + k^2)', abs(mdot(kg, ppg) - 0.5*(mdot(ppg, ppg) - mdot(pg, pg) + mdot(kg, kg))))
# (W5) eikonal identity with the same +i0 (exact algebra; check at finite eps)
n = rnd_vec(rng); l = rnd_vec(rng); ke = rnd_vec(rng); e = 1e-3
lhs = mdot(n, ke)/((mdot(n, l)+1j*e)*(mdot(n, l+ke)+1j*e))
rhs = 1/(mdot(n, l)+1j*e) - 1/(mdot(n, l+ke)+1j*e)
check('(W5) eikonal Ward identity (same i0 on both)', abs(lhs-rhs)/abs(rhs))

# fermion line with on-shell ends, n = 2 gluons + one scalar-polarized gluon, non-abelian (random colour matrices)
for m in [0.0, 0.5]:
    def onshell(mass):
        pv = rng.normal(size=3); E = np.sqrt(pv @ pv + mass**2)
        return np.array([E, *pv], dtype=complex)
    p = onshell(m); pp = onshell(m); k = rnd_vec(rng); qa = rnd_vec(rng); qb = pp - p - qa - k
    e1 = rnd_vec(rng); e2 = rnd_vec(rng)
    T1, T2, TK = [rng.normal(size=(3, 3)) + 1j*rng.normal(size=(3, 3)) for _ in range(3)]
    V1 = 1j*g*slash(e1); V2 = 1j*g*slash(e2); VK = 1j*g*slash(k)
    for u in u_spinors(p, m)[:1]:
        for up in u_spinors(pp, m)[:1]:
            ub = bar(up)
            # insertions: K first, between, last (matrices ordered against the fermion arrow)
            ins0 = (ub @ V2 @ S(p+k+qa, m) @ V1 @ S(p+k, m) @ VK @ u, T2 @ T1 @ TK)
            ins1 = (ub @ V2 @ S(p+qa+k, m) @ VK @ S(p+qa, m) @ V1 @ u, T2 @ TK @ T1)
            ins2 = (ub @ VK @ S(pp-k, m) @ V2 @ S(p+qa, m) @ V1 @ u, TK @ T2 @ T1)
            lhs = sum(a*c for a, c in [ins0, ins1, ins2])
            Z1 = ub @ V2 @ S(p+qa+k, m) @ V1 @ u
            Z2 = ub @ V2 @ S(p+qa, m) @ V1 @ u
            rhs = g*(Z1*(T2 @ (TK @ T1 - T1 @ TK)) + Z2*((TK @ T2 - T2 @ TK) @ T1))
            check('fermion line: sum of K insertions = g sum_r Z_r [T_K,T_r] (n=2, m=%.1f)' % m, rel(lhs, rhs))
            lhs_ab = ins0[0] + ins1[0] + ins2[0]
            check('fermion line: abelian sum of K insertions = 0 (n=2, m=%.1f)' % m, abs(lhs_ab)/abs(ins0[0]))

# gamma* -> q(p1) qbar(p2) g(k): eps -> k
def onshell(mass, scale=1.0):
    pv = rng.normal(size=3)*scale; E = np.sqrt(pv @ pv + mass**2)
    return np.array([E, *pv], dtype=complex)
for m in [0.0, 0.4]:
    p1 = onshell(m); p2 = onshell(m); k = onshell(0.0)
    for u1 in u_spinors(p1, m)[:1]:
        for v2 in v_spinors(p2, m)[:1]:
            mx = 0
            for nu in range(4):
                A = bar(u1) @ (1j*g*slash(k) @ S(p1+k, m) @ GAM[nu] + GAM[nu] @ S(-p2-k, m) @ (1j*g*slash(k))) @ v2
                mx = max(mx, abs(A))
            check('(VF-WL-7) gamma*->q qbar g: k_mu A^{mu nu} = 0 on shell (m=%.1f)' % m, mx)
    # antiquark leg off shell: graph (1) alone gives -g t^a ubar gamma^nu X
    X = rng.normal(size=4) + 1j*rng.normal(size=4)
    for u1 in u_spinors(p1, m)[:1]:
        mx = 0
        for nu in range(4):
            A1 = bar(u1) @ (1j*g*slash(k)) @ S(p1+k, m) @ GAM[nu] @ X
            mx = max(mx, abs(A1 - (-g)*(bar(u1) @ GAM[nu] @ X)))
        check('(VF-WL-7) off-shell antiquark leg: graph (1) gives exactly -g ubar(p1) gamma^nu X (m=%.1f)' % m, mx)

# DIS seed: H^mu_a = ubar(p') i g gamma^mu t^a S(p'-k) Gamma
Gam = rng.normal(size=4) + 1j*rng.normal(size=4)      # open index (Gamma times the off-shell leg)
for m in [0.0, 0.5]:
    pp = onshell(m); k = rnd_vec(rng)
    for up in u_spinors(pp, m)[:1]:
        ub = bar(up)
        kH = sum(lower(k)[mu]*(ub @ (1j*g*GAM[mu]) @ S(pp-k, m) @ Gam) for mu in range(4))
        check('(VF-WL-8) k_mu H^mu = g ubar(p\') Gamma = g H_0 (colour t^a) (m=%.1f)' % m, abs(kH - g*(ub @ Gam))/abs(ub @ Gam))
        # two K gluons: exact identity
        k1 = rnd_vec(rng); k2 = rnd_vec(rng); K = k1 + k2
        Ta, Tb = TA[2], TA[4]
        H12 = np.zeros((3, 3), dtype=complex)
        # ordering 1: gluon a (k1) next to ubar: ubar i g k1slash t^a S(p'-k1) i g k2slash t^b S(p'-K) Gamma
        o1 = ub @ (1j*g*slash(k1)) @ S(pp-k1, m) @ (1j*g*slash(k2)) @ S(pp-K, m) @ Gam
        o2 = ub @ (1j*g*slash(k2)) @ S(pp-k2, m) @ (1j*g*slash(k1)) @ S(pp-K, m) @ Gam
        lhs = o1*(Ta @ Tb) + o2*(Tb @ Ta)
        rhs = g**2*(Tb @ Ta)*(ub @ Gam) + 1j*g**2*(Ta @ Tb - Tb @ Ta)*(ub @ slash(k2) @ S(pp-K, m) @ Gam)
        check('(VF-WL-8) two K gluons, exact: = g^2 t^b t^a H0 + i g^2 [t^a,t^b] ubar k2slash S(p\'-K) Gamma (m=%.1f)' % m, rel(lhs, rhs))
    # collinear limit: k_i -> (k_i^+, 0, 0_T), p' such that the identity is exact
    if m == 0.0:
        for up in u_spinors(pp, m)[:1]:
            ub = bar(up)
            k1h = lc(0.7, 0.0); k2h = lc(1.9, 0.0); Kh = k1h + k2h
            o1 = ub @ (1j*g*slash(k1h)) @ S(pp-k1h, m) @ (1j*g*slash(k2h)) @ S(pp-Kh, m) @ Gam
            o2 = ub @ (1j*g*slash(k2h)) @ S(pp-k2h, m) @ (1j*g*slash(k1h)) @ S(pp-Kh, m) @ Gam
            lhs = o1*(Ta @ Tb) + o2*(Tb @ Ta)
            n1, n2, nK = plus(k1h), plus(k2h), plus(Kh)
            W2 = g**2*((Tb @ Ta)/(nK*n2) + (Ta @ Tb)/(nK*n1))
            rhs = n1*n2*W2*(ub @ Gam)
            check('(VF-WL-8) collinear K gluons: = (nB.k1)(nB.k2) W^(2)_ab[infty nB,0] H0', rel(lhs, rhs))

# q(p1) qbar(p2) -> g*(k1,a,mu) g*(k2,b,nu): k1_mu A^{mu nu}_ab = (g^2 f^{abc}/Q^2)(k2^2 g^{nu sigma} - k2^nu k2^sigma) J_{c sigma}
def amp_qqgg(p1, p2, k1, k2, u1, v2, a, b, m=0.0):
    """A^{mu nu}_{ab} (4x4 array over mu, nu, upper indices) times colour: returns array [mu,nu,i,j] colour matrix"""
    Q = p1 + p2
    out = np.zeros((4, 4, 3, 3), dtype=complex)
    Ginv = np.diag([1.0, -1, -1, -1])
    for mu in range(4):
        for nu in range(4):
            t = bar(v2) @ (1j*g*GAM[nu]) @ S(p1-k1, m) @ (1j*g*GAM[mu]) @ u1
            uu = bar(v2) @ (1j*g*GAM[mu]) @ S(p1-k2, m) @ (1j*g*GAM[nu]) @ u1
            col = t*(TA[b] @ TA[a]) + uu*(TA[a] @ TA[b])
            # s-channel: vbar i g gamma_sigma t^c u  (-i g^{sigma rho}/Q^2)  g f^{c a b} V_{rho}^{mu nu}(Q,-k1,-k2)
            s_amp = np.zeros((3, 3), dtype=complex)
            for c in range(8):
                if abs(FABC[c, a, b]) < 1e-14: continue
                tot = 0
                for rho in range(4):
                    Jr = bar(v2) @ (1j*g*GAM[rho]) @ u1       # upper index rho
                    # contract J^rho (upper) with -i g_{rho rho'} /Q^2 V^{rho' mu nu}: lower rho
                    tot += Jr*Ginv[rho, rho]*(-1j/mdot(Q, Q))*g*V3(Q, -k1, -k2, rho, mu, nu)
                s_amp += FABC[c, a, b]*tot*TA[c]
            out[mu, nu] = col + s_amp
    return out
m = 0.0
p1 = onshell(0.0); p2 = onshell(0.0); Q = p1 + p2
# off-shell gluons: k1 random, k2 = Q - k1
k1 = rnd_vec(rng); k2 = Q - k1
u1 = u_spinors(p1)[0]; v2 = v_spinors(p2)[0]
mx = 0; mx0 = 0
for a in range(8):
    for b in range(8):
        A = amp_qqgg(p1, p2, k1, k2, u1, v2, a, b)
        for nu in range(4):
            lhs = sum(lower(k1)[mu]*A[mu, nu] for mu in range(4))
            rhs = np.zeros((3, 3), dtype=complex)
            for c in range(8):
                if abs(FABC[a, b, c]) < 1e-14: continue
                Jlow = np.array([bar(v2) @ GAM[s] @ u1 for s in range(4)])  # J^sigma (colour stripped) upper
                proj = mdot(k2, k2)*Jlow[nu] - k2[nu]*mdot(k2, Jlow)
                rhs += g**2*FABC[a, b, c]/mdot(Q, Q)*proj*TA[c]
            mx = max(mx, np.max(np.abs(lhs - rhs))); mx0 = max(mx0, np.max(np.abs(lhs)))
check('(VF-WL-9) q qbar -> g*g*: k1_mu A^{mu nu}_ab = (g^2 f^{abc}/Q^2)(k2^2 g^{nu s} - k2^nu k2^s) J_{c s}', mx/max(mx0, 1e-300))
# both longitudinal, off shell: k1_mu k2_nu A^{mu nu} = 0
mx = 0
for a in range(8):
    for b in range(8):
        A = amp_qqgg(p1, p2, k1, k2, u1, v2, a, b)
        val = sum(lower(k1)[mu]*lower(k2)[nu]*A[mu, nu] for mu in range(4) for nu in range(4))
        mx = max(mx, np.max(np.abs(val)))
check('(VF-WL-9) k1_mu k2_nu A^{mu nu} = 0 (off shell)', mx)

# on-shell gluons: physical polarization sums vs -g sums minus ghosts; CKR
def pols(kvec):
    """two transverse polarization vectors for on-shell massless k (real, orthonormal, eps.k = 0, eps^0 = 0)"""
    kv = np.real(kvec[1:]); kh = kv/np.linalg.norm(kv)
    a = np.array([1.0, 0, 0]) if abs(kh[0]) < 0.9 else np.array([0, 1.0, 0])
    e1 = np.cross(kh, a); e1 /= np.linalg.norm(e1); e2 = np.cross(kh, e1)
    return [np.array([0, *e1], dtype=complex), np.array([0, *e2], dtype=complex)]
# kinematics in the CM frame: p1, p2 along z, k1, k2 at angle theta
E = 1.3; th = 0.83
p1 = np.array([E, 0, 0, E], dtype=complex); p2 = np.array([E, 0, 0, -E], dtype=complex)
k1 = np.array([E, E*np.sin(th), 0, E*np.cos(th)], dtype=complex); k2 = p1 + p2 - k1
s_ = mdot(p1+p2, p1+p2).real; t_ = mdot(p1-k1, p1-k1).real; u_ = mdot(p1-k2, p1-k2).real
sum_phys = 0; sum_gg = 0; sum_gh = 0
Gmetric = np.diag([1.0, -1, -1, -1])
for u1 in u_spinors(p1):
    for v2 in v_spinors(p2):
        # normalize spinors: ubar gamma^0 u = 2E  -> u^dagger u = 2E
        u1n = u1*np.sqrt(2*E/np.real(u1.conj() @ u1)); v2n = v2*np.sqrt(2*E/np.real(v2.conj() @ v2))
        for a in range(8):
            for b in range(8):
                A = amp_qqgg(p1, p2, k1, k2, u1n, v2n, a, b)
                # physical
                for e1v in pols(k1):
                    for e2v in pols(k2):
                        Mc = sum(lower(e1v.conj())[mu]*lower(e2v.conj())[nu]*A[mu, nu] for mu in range(4) for nu in range(4))
                        sum_phys += np.sum(np.abs(Mc)**2)
                # -g sums: sum_{mu nu} A^{mu nu} A*^{mu' nu'} g_{mu mu'} g_{nu nu'}
                for mu in range(4):
                    for nu in range(4):
                        sum_gg += Gmetric[mu, mu]*Gmetric[nu, nu]*np.sum(np.abs(A[mu, nu])**2)
                # ghost amplitude A_gh = (g^2/Q^2) f^{abd} k1.J_d
                Agh = np.zeros((3, 3), dtype=complex)
                for d in range(8):
                    if abs(FABC[a, b, d]) < 1e-14: continue
                    J = np.array([bar(v2n) @ GAM[s] @ u1n for s in range(4)])
                    Agh += g**2/s_*FABC[a, b, d]*mdot(k1, J)*TA[d]
                sum_gh += np.sum(np.abs(Agh)**2)
check('(VF-WL-9) sum_phys |A|^2 = sum_{-g,-g}|A|^2 - 2 sum |A_gh|^2', abs(sum_phys - (sum_gg - 2*sum_gh))/sum_phys)
ckr = g**4*(32/27*(t_**2+u_**2)/(t_*u_) - 8/3*(t_**2+u_**2)/s_**2)
check('(VF-WL-9) (1/36) sum_phys |A|^2 = g^4[(32/27)(t^2+u^2)/(tu) - (8/3)(t^2+u^2)/s^2] (CKR)', abs(sum_phys/36 - ckr)/ckr)
print('    s,t,u = %.4f %.4f %.4f ; (1/36) sum_phys = %.10f ; CKR = %.10f ; 2 sum|A_gh|^2/sum_{-g-g} = %.4f' %
      (s_, t_, u_, sum_phys/36, ckr, 2*sum_gh/sum_gg))
print('\n=== w10_ward: %d PASS, %d FAIL ===' % (npass, nfail))
