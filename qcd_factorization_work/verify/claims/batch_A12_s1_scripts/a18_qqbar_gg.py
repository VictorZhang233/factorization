# Independent numerical check of the spin/colour averaged |M|^2 for q qbar -> g g (massless), metric (+,-,-,-).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
rng = np.random.default_rng(7)
I2 = np.eye(2); Z2 = np.zeros((2, 2))
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex), np.array([[1, 0], [0, -1]], complex)]
g0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
gs = [np.block([[Z2, s], [-s, Z2]]) for s in sig]
gam = [g0] + gs
eta = np.diag([1., -1., -1., -1.])
def sl(p):  # p-slash with upper-index p
    return sum(eta[m, m] * p[m] * gam[m] for m in range(4))
def dot(a, b): return a[0]*b[0] - a[1]*b[1] - a[2]*b[2] - a[3]*b[3]
# Gell-Mann / SU(3) generators t^a = lambda^a / 2
lam = np.zeros((8, 3, 3), complex)
lam[0][0, 1] = lam[0][1, 0] = 1
lam[1][0, 1] = -1j; lam[1][1, 0] = 1j
lam[2][0, 0] = 1; lam[2][1, 1] = -1
lam[3][0, 2] = lam[3][2, 0] = 1
lam[4][0, 2] = -1j; lam[4][2, 0] = 1j
lam[5][1, 2] = lam[5][2, 1] = 1
lam[6][1, 2] = -1j; lam[6][2, 1] = 1j
lam[7] = np.diag([1, 1, -2]) / np.sqrt(3)
t = lam / 2
f = np.zeros((8, 8, 8))
for a in range(8):
    for b in range(8):
        comm = t[a] @ t[b] - t[b] @ t[a]
        for c in range(8):
            f[a, b, c] = np.real(-2j * np.trace(comm @ t[c]))   # [t^a,t^b] = i f^{abc} t^c
# kinematics in the CM frame
E = 1.0
th, ph = 0.7, 0.3
p1 = np.array([E, 0, 0, E]); p2 = np.array([E, 0, 0, -E])
n = np.array([np.sin(th)*np.cos(ph), np.sin(th)*np.sin(ph), np.cos(th)])
k1 = np.concatenate([[E], E*n]); k2 = np.concatenate([[E], -E*n])
s = dot(p1+p2, p1+p2); tt = dot(p1-k1, p1-k1); uu = dot(p1-k2, p1-k2)
def pols(k):
    # two transverse real polarization vectors orthogonal to k (and to time direction)
    kv = k[1:] / np.linalg.norm(k[1:])
    a = np.array([1., 0., 0.]) if abs(kv[0]) < 0.9 else np.array([0., 1., 0.])
    e1 = a - kv * (a @ kv); e1 /= np.linalg.norm(e1)
    e2 = np.cross(kv, e1)
    return [np.concatenate([[0.], e1]), np.concatenate([[0.], e2])]
def V3(ka, kb, kc):  # three-gluon Lorentz structure, all momenta incoming, upper indices (mu,nu,rho) for (a,b,c)
    Vt = np.zeros((4, 4, 4))
    for m in range(4):
        for nn in range(4):
            for r in range(4):
                Vt[m, nn, r] = (eta[m, nn]*(ka-kb)[r] + eta[nn, r]*(kb-kc)[m] + eta[r, m]*(kc-ka)[nn])
    return Vt
def lower(v): return eta @ v
q = p1 + p2
Vs = V3(-k1, -k2, q)   # indices (mu for a, nu for b, rho for c)
def amp_parts(e1, e2):
    # Dirac structures (to be sandwiched between vbar(p2) ... u(p1)), colour structures separate. Common factor g^2 dropped.
    G_t = sl(e2) @ sl(p1 - k1) @ sl(e1) / tt      # colour t^b t^a
    G_u = sl(e1) @ sl(p1 - k2) @ sl(e2) / uu      # colour t^a t^b
    # s-channel: vbar gamma_rho t^c u * (1/s) * f^{abc} V^{mu nu rho} e1_mu e2_nu  (relative sign sigma fixed by gauge invariance)
    J = np.einsum('mnr,m,n->r', Vs, lower(e1), lower(e2))   # upper index rho
    G_s = sl(J) / s                                     # colour i f^{abc} t^c  -> [t^a,t^b]
    return G_t, G_u, G_s
def colour_mats(a, b):
    return t[b] @ t[a], t[a] @ t[b], (t[a] @ t[b] - t[b] @ t[a])
def total_M_matrix(e1, e2, sigma):
    G_t, G_u, G_s = amp_parts(e1, e2)
    out = {}
    for a in range(8):
        for b in range(8):
            Ct, Cu, Cs = colour_mats(a, b)
            out[(a, b)] = (G_t, Ct), (G_u, Cu), (G_s, sigma*Cs)
    return out
def spinsum_sq(terms):
    # sum over quark spins and colours of |vbar Gamma u|^2 :  Tr_D[p2s G p1s Gbar] * Tr_c[C C^dag]
    tot = 0.0
    for (Ga, Ca) in terms:
        for (Gb, Cb) in terms:
            Gbbar = g0 @ Gb.conj().T @ g0
            tot += np.trace(sl(p2) @ Ga @ sl(p1) @ Gbbar) * np.trace(Ca @ Cb.conj().T)
    return tot
# 1) Fix sigma by the Ward identity e1 -> k1 (e2 physical)
for sigma in (+1, -1):
    w = 0.0
    for e2 in pols(k2):
        for a in range(8):
            for b in range(8):
                Ct, Cu, Cs = colour_mats(a, b)
                G_t, G_u, G_s = amp_parts(k1, e2)
                Mfull = np.kron(G_t, Ct) + np.kron(G_u, Cu) + sigma*np.kron(G_s, Cs)   # crude: Dirac x colour; test operator norm on on-shell spinor space
                # sandwich with on-shell projectors: vbar ... u -> use p2s M p1s
                X = np.kron(sl(p2), np.eye(3)) @ Mfull @ np.kron(sl(p1), np.eye(3))
                w += np.linalg.norm(X)
    print('sigma = %+d : Ward-identity residual (sum of norms) = %.3e' % (sigma, w))
sig_ok = +1 if True else -1
# choose the sigma with the smaller residual
res = {}
for sigma in (+1, -1):
    w = 0.0
    for e2 in pols(k2):
        for a in range(8):
            for b in range(8):
                Ct, Cu, Cs = colour_mats(a, b)
                G_t, G_u, G_s = amp_parts(k1, e2)
                Mfull = np.kron(G_t, Ct) + np.kron(G_u, Cu) + sigma*np.kron(G_s, Cs)
                X = np.kron(sl(p2), np.eye(3)) @ Mfull @ np.kron(sl(p1), np.eye(3))
                w += np.linalg.norm(X)
    res[sigma] = w
sigma = min(res, key=res.get)
# 2) Sum over physical polarizations and colours
tot = 0.0
for e1 in pols(k1):
    for e2 in pols(k2):
        for a in range(8):
            for b in range(8):
                Ct, Cu, Cs = colour_mats(a, b)
                G_t, G_u, G_s = amp_parts(e1, e2)
                tot += spinsum_sq([(G_t, Ct), (G_u, Cu), (G_s, sigma*Cs)])
avg = np.real(tot) / 4 / 9
formula = 32/27*(tt**2 + uu**2)/(tt*uu) - 8/3*(tt**2 + uu**2)/s**2
print('s, t, u =', s, tt, uu)
print('averaged |M|^2 / g^4 (numerical) = %.12f' % avg)
print('ESW Tab.7.1 / PDG (51.9) formula   = %.12f' % formula)
print('ratio = %.15f' % (avg/formula))
