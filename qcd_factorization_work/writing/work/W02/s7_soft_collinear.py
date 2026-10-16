"""W02 / Ch2 check s7 (prop:qcd-soft-collinear-limits, ex:qcd-ee-real-virtual):
 (a) amplitude-level soft factor with the Feynman rules of def:prelim-feynman-rules (D = d - i g A):
     outgoing quark:      ubar(p) (i g eps*.gamma t^a) S(p+k)  ->  -g (p.eps*/p.k) t^a ubar(p)
     outgoing antiquark:  S(-pbar-k) (i g eps*.gamma t^a) v(pbar) ->  +g (pbar.eps*/pbar.k) t^a v(pbar)
                          = -g (pbar.eps*/pbar.k) T_qbar  with T_qbar = -t^{aT} acting on the antiquark index
     outgoing gluon (3-gluon vertex, all momenta incoming):  -> -g (p.eps*/p.k) (F^a)_{bc}, (F^a)_{bc} = -i f^{abc}
     => M_{n+1} = -g sum_i (p_i.eps*/p_i.k) T_i^a M_n   (overall sign fixed by our rules; it flips with g -> -g)
     checked numerically on gamma* -> q qbar g (full tree amplitude vs eikonal limit) and on the gluon vertex.
 (b) |M|^2 limits of the exact (1/sigma0) dsigma/dx1dx2 = (C_F as/2pi)(x1^2+x2^2)/((1-x1)(1-x2)):
     soft:  -> (C_F as/pi) / ((1-x1)(1-x2))  =  sigma0 x g^2 C_F 2p.pbar/((p.k)(pbar.k)) x dPhi3/dPhi2
     collinear (q || g): -> (C_F as/2pi) (1+z^2)/((1-z)(1-x2)),  z = x1/(2-x2)
     D-dim kernel from the VF-EE-5 matrix element: (1+z^2)/(1-z) - eps (1-z)   (VF-PDF-6)
 (c) soft-collinear measure: g^2 C_F 2p.pbar/((p.k)(pbar.k)) d^3k/((2pi)^3 2E) -> (as C_F/pi) dE/E dtheta^2/theta^2.
Run: python3 -I s7_soft_collinear.py
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
npass = nfail = 0
def report(ok, name, detail=''):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(('PASS ' if ok else 'FAIL ') + name + (('   [' + detail + ']') if detail else ''), flush=True)
eta = np.diag([1., -1, -1, -1])
I2 = np.eye(2); Z2 = np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
g0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
gam = [g0] + [np.block([[Z2, s], [-s, Z2]]) for s in (sx, sy, sz)]
def sl(p): return sum(eta[m, m] * p[m] * gam[m] for m in range(4))
def dot(a, b): return a @ eta @ b
lam = np.zeros((8, 3, 3), complex)
lam[0][0, 1] = lam[0][1, 0] = 1; lam[1][0, 1] = -1j; lam[1][1, 0] = 1j; lam[2][0, 0] = 1; lam[2][1, 1] = -1
lam[3][0, 2] = lam[3][2, 0] = 1; lam[4][0, 2] = -1j; lam[4][2, 0] = 1j; lam[5][1, 2] = lam[5][2, 1] = 1
lam[6][1, 2] = -1j; lam[6][2, 1] = 1j; lam[7] = np.diag([1, 1, -2]) / np.sqrt(3)
T = lam / 2
f = np.zeros((8, 8, 8))
for a, b, c in itertools.product(range(8), repeat=3):
    f[a, b, c] = np.real(-2j * np.trace((T[a] @ T[b] - T[b] @ T[a]) @ T[c]))
F = -1j * f   # (F^a)_{bc} = -i f^{abc}
g = 1.0
def S(p): return 1j * sl(p) / dot(p, p)
def massless(E, th, ph): return E * np.array([1, np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)])
# ---------------- (a) quark/antiquark: gamma* -> q qbar + soft g ----------------
p1 = massless(2.0, 0.7, 0.3); p2 = massless(2.0, np.pi - 0.7, 0.3 + np.pi)
nk = np.array([np.sin(1.9) * np.cos(2.4), np.sin(1.9) * np.sin(2.4), np.cos(1.9)])
epsk = np.concatenate([[0], np.cross(nk, [0.2, 0.9, -0.3])]); epsk /= np.sqrt(-dot(epsk, epsk))
up = sl(p1) @ np.array([1, 0.3, -0.2j, 0.5], complex); vp = sl(p2) @ np.array([0.2, 1, 0.4j, -0.3], complex)
ubar = up.conj() @ g0
Gam = gam[1] + 0.4 * gam[2]                          # arbitrary current vertex (colour singlet)
def low(v): return eta @ v
for lamk in [1e-3, 1e-4]:
    k = lamk * np.concatenate([[1], nk])
    for a in [0, 3, 7]:
        epsl = sl(epsk)    # eps*.gamma (real eps)
        # iM_{n+1} = ubar [(i g eps.gamma t^a) S(p1+k) (i Gam) + (i Gam) S(-p2-k) (i g eps.gamma t^a)] v  (colour matrix)
        Mq = np.einsum('i,ij,j->', ubar, (1j * g * epsl) @ S(p1 + k) @ (1j * Gam), vp)
        Mqb = np.einsum('i,ij,j->', ubar, (1j * Gam) @ S(-p2 - k) @ (1j * g * epsl), vp)
        Mn = np.einsum('i,ij,j->', ubar, 1j * Gam, vp)
        # colour: both terms carry (t^a)_{ij}; eikonal prediction (coefficient of t^a_{ij}):
        pred_q = -g * dot(p1, epsk) / dot(p1, k) * Mn
        pred_qb = +g * dot(p2, epsk) / dot(p2, k) * Mn
        okq = abs(Mq / pred_q - 1) < 10 * lamk; okqb = abs(Mqb / pred_qb - 1) < 10 * lamk
    report(okq and okqb, f'(a) eikonal factors at |k| = {lamk:g}: outgoing q -> -g p.eps/p.k t^a ; outgoing qbar -> +g pbar.eps/pbar.k t^a (= -g (pbar.eps/pbar.k) T_qbar, T_qbar = -t^aT)',
           f'ratios {abs(Mq/pred_q):.6f}, {abs(Mqb/pred_qb):.6f}')
# colour conservation for the singlet: (T_q + T_qbar) delta = t^a - t^a = 0
ok = all(np.allclose(np.einsum('ik,kj->ij', T[a], np.eye(3)) + np.einsum('jl,il->ij', -T[a].T, np.eye(3)), 0) for a in range(8))
report(ok, '(a) colour conservation: (T_q + T_qbar) acting on delta_ij gives t^a - t^a = 0')
# ---------------- (a) gluon: soft emission off an outgoing gluon via the 3-gluon vertex ----------------
def V3(k, mu, a, p, nu, b, q, rho, c):
    return g * f[a, b, c] * (eta[mu, nu] * (k - p)[rho] + eta[nu, rho] * (p - q)[mu] + eta[rho, mu] * (q - k)[nu])
pg = massless(2.0, 0.5, 1.2)
epsp = np.concatenate([[0], np.cross(pg[1:] / np.linalg.norm(pg[1:]), [0.4, -0.3, 0.8])]); epsp /= np.sqrt(-dot(epsp, epsp))
rng = np.random.default_rng(3)
Mvec = rng.normal(size=(8, 4)) + 1j * rng.normal(size=(8, 4))      # iM_n^rho (colour c) for an off-shell leg; impose p.M = 0
# project so that p_rho M^rho = 0: subtract component along nbar with p.nbar != 0
nbar = np.array([pg[0], -pg[1], -pg[2], -pg[3]])
for c in range(8):
    Mvec[c] = Mvec[c] - dot(pg, Mvec[c]) / dot(pg, nbar) * nbar
for lamk in [1e-3, 1e-4]:
    k = lamk * np.concatenate([[1], nk])
    okg = True; rat = []
    for a in [0, 2, 5]:
        for b in range(8):
            # iM_{n+1}(b) = sum_c iM_n^rho(c) (-i g_{rho sigma}/(p+k)^2) V^{sigma nu mu}_{c b a}((p+k), -p, -k) eps*_p,nu eps*_k,mu
            val = 0
            for c in range(8):
                if f[c, b, a] == 0: continue
                for rho in range(4):
                    for nu in range(4):
                        for mu in range(4):
                            v = V3(pg + k, rho, c, -pg, nu, b, -k, mu, a)
                            if v == 0: continue
                            val += Mvec[c][rho] * eta[rho, rho] * (-1j / dot(pg + k, pg + k)) * v * low(epsp)[nu] * low(epsk)[mu]
            # prediction: -g (p.eps_k/p.k) (F^a)_{bc} iM_n(c, eps_p)
            Mn_c = np.array([dot(Mvec[c], epsp) for c in range(8)])     # iM_n(c) = iM_n^rho eps*_rho  (with lowered index)
            pred = -g * dot(pg, epsk) / dot(pg, k) * (F[a] @ Mn_c)[b]
            if abs(pred) > 1e-6:
                rat.append(val / pred)
                okg &= abs(val / pred - 1) < 20 * lamk
    report(okg, f'(a) outgoing gluon at |k| = {lamk:g}: -> -g (p.eps/p.k) (F^a)_{{bc}}, (F^a)_{{bc}} = -i f^{{abc}} (same overall sign as for quarks)',
           f'max |ratio-1| = {max(abs(np.array(rat) - 1)):.2e}')
# colour conservation for a two-gluon singlet delta_bc: F^a_{bb'}delta_{b'c} + F^a_{cc'} delta_{bc'} = F^a_bc + F^a_cb = 0
report(all(np.allclose(F[a] + F[a].T, 0) for a in range(8)), '(a) two-gluon singlet: (T_1 + T_2) delta = F^a + F^aT = 0 (F antisymmetric)')
# ---------------- (b) |M|^2 limits of the exact 4D matrix element ----------------
def exact(x1, x2): return (x1**2 + x2**2) / ((1 - x1) * (1 - x2))      # units C_F as/2pi
# soft: x3 -> 0 with fixed v: x1 = 1 - x3 (1-v), x2 = 1 - x3 v
for x3 in [1e-2, 1e-4]:
    v = 0.37
    x1 = 1 - x3 * (1 - v); x2 = 1 - x3 * v
    ratio = exact(x1, x2) / (2 / ((1 - x1) * (1 - x2)))
    report(abs(ratio - 1) < 3 * x3, f'(b) soft limit x3 = {x3:g}: (x1^2+x2^2)/((1-x1)(1-x2)) -> 2/((1-x1)(1-x2)) i.e. (C_F as/pi)/((1-x1)(1-x2))', f'ratio {ratio:.8f}')
# eikonal normalisation: sigma0 g^2 C_F 2p1.p2/((p1.k)(p2.k)) dPhi3/dPhi2 with dPhi3/dPhi2 = s dx1 dx2/(16 pi^2), 2 p_i.k = s(1-x_j)
s_ = 1.0; x1, x2 = 0.999, 0.998
eik = 4 * np.pi * 1.0 * (s_ / 2 * 2) / ((s_ * (1 - x2) / 2) * (s_ * (1 - x1) / 2)) * s_ / (16 * np.pi**2)   # g^2 = 4 pi as with as = 1, C_F = 1
report(np.isclose(eik, 1 / np.pi / ((1 - x1) * (1 - x2))), '(b) eikonal |M|^2 x dPhi3/dPhi2 = (as C_F/pi) dx1 dx2/((1-x1)(1-x2)) (normalisation of the soft limit)')
# collinear: x2 -> 1 (y13 = 1 - x2 -> 0), z = x1/(2 - x2)
for y13 in [1e-3, 1e-5]:
    z = 0.62
    x2 = 1 - y13; x1 = z * (2 - x2)
    ratio = exact(x1, x2) / ((1 + z**2) / ((1 - z) * (1 - x2)))
    report(abs(ratio - 1) < 10 * y13, f'(b) collinear limit y13 = {y13:g}: -> (1+z^2)/((1-z)(1-x2)) [units C_F as/2pi]', f'ratio {ratio:.8f}')
# collinear normalisation: (2 g^2 C_F/s_qg)(1+z^2)/(1-z) x s dx1dx2/(16 pi^2) = (as C_F/2pi)(1+z^2)/((1-z)(1-x2)) dx1 dx2
z = 0.62; x2 = 0.9999; sqg = s_ * (1 - x2)
lhs = 2 * 4 * np.pi / sqg * (1 + z**2) / (1 - z) * s_ / (16 * np.pi**2)
report(np.isclose(lhs, 1 / (2 * np.pi) * (1 + z**2) / ((1 - z) * (1 - x2))), '(b) collinear factor 2 g^2 C_F/s_qg (1+z^2)/(1-z) x dPhi3/dPhi2 reproduces the exact limit')
# D-dimensional kernel from the VF-EE-5 matrix element (bracket times 8(1-eps), Born bracket 8(1-eps)... ratio)
e, y13s, zs = sp.symbols('epsilon y13 z', positive=True)
y23 = 1 - zs; y12 = zs     # collinear limit of y_ij at fixed z
br = (1 - e) * (y13s / y23 + y23 / y13s) + 2 * y12 / (y13s * y23) - 2 * e
lead = sp.limit(sp.simplify(br * y13s), y13s, 0)
report(sp.simplify(lead - ((1 + zs**2) / (1 - zs) - e * (1 - zs))) == 0, '(b) D-dim: y13 x bracket -> (1+z^2)/(1-z) - eps (1-z)  (VF-PDF-6 kernel)', str(sp.factor(lead)))
# ---------------- (c) soft-collinear measure ----------------
Ek, th, Ep, Epb = sp.symbols('E_k theta E_p E_pbar', positive=True)
pk = Ep * Ek * (1 - sp.cos(th)); pbk = Epb * Ek * (1 + sp.cos(th)); ppb = 2 * Ep * Epb
gs, CF = sp.symbols('g C_F', positive=True)
dens = gs**2 * CF * 2 * ppb / (pk * pbk) * Ek / (16 * sp.pi**3) * sp.sin(th) * 2 * sp.pi     # per dE dtheta, azimuth integrated
# express per dE dtheta^2 at small theta: dtheta = dtheta^2/(2 theta)
lim = sp.limit(sp.simplify(dens / (2 * th) * Ek * th**2), th, 0)
report(sp.simplify(lim - gs**2 * CF / (4 * sp.pi**2)) == 0, '(c) small angle: g^2 C_F 2p.pbar/((p.k)(pbar.k)) d^3k/((2pi)^3 2E) -> (as C_F/pi) dE/E dtheta^2/theta^2', str(lim))
print(f'\nSUMMARY: {npass}/{npass + nfail} PASS')
