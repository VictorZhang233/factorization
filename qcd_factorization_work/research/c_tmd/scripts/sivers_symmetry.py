# Ingredients of the T-reversal (PT) proof of f_1T^perp(SIDIS) = - f_1T^perp(DY), checked explicitly.
# Dirac representation, gamma_5 = i g0 g1 g2 g3, metric (+,-,-,-), T_D = i g^1 g^3 (Bjorken-Drell), antiunitary T.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import sympy as sp
ok = True
I2, Z2 = np.eye(2), np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
g = [np.block([[I2, Z2], [Z2, -I2]]).astype(complex)] + [np.block([[Z2, s], [-s, Z2]]) for s in (sx, sy, sz)]
eta = np.diag([1., -1., -1., -1.])
g5 = 1j * g[0] @ g[1] @ g[2] @ g[3]
gl = [eta[m, m] * g[m] for m in range(4)]           # gamma_mu (lower index)
gplus, gminus = (g[0] + g[3]) / np.sqrt(2), (g[0] - g[3]) / np.sqrt(2)

# ---- (1) matrix identities ----------------------------------------------------------------------
TD = 1j * g[1] @ g[3]
c1 = all(np.allclose(TD @ g[m].conj() @ np.linalg.inv(TD), gl[m]) for m in range(4))     # T: gamma^mu* -> gamma_mu
c2 = np.allclose(g[0] @ TD.conj().T @ g[0], TD) and np.allclose(TD @ TD, np.eye(4))
c3 = all(np.allclose(g[0] @ g[m] @ g[0], gl[m]) for m in range(4))                        # P: gamma^mu -> gamma_mu
print('(1) T_D gamma^mu* T_D^-1 = gamma_mu: %s ; g0 T_D^+ g0 = T_D, T_D^2 = 1: %s ; g0 gamma^mu g0 = gamma_mu: %s' % (c1, c2, c3))
ok &= c1 and c2 and c3
# bilinear psibar Gamma psi -> T: psibar (g0 T_D^+ g0) Gamma* T_D psi ;  P: psibar g0 Gamma g0 psi
Tmap = lambda G: g[0] @ TD.conj().T @ g[0] @ G.conj() @ TD
Pmap = lambda G: g[0] @ G @ g[0]
c4 = np.allclose(Tmap(gplus), gminus) and np.allclose(Pmap(gminus), gplus) and np.allclose(Pmap(Tmap(gplus)), gplus)
print('    gamma^+ --T--> gamma^- --P--> gamma^+  (PT keeps gamma^+):', c4)
ok &= c4

# ---- (2) PT on one-particle spinors keeps P and flips S ---------------------------------------------
rng = np.random.default_rng(7)
M = 0.938
def slash(v):
    vl = eta @ v
    return sum(g[m] * vl[m] for m in range(4))
for trial in range(3):
    pvec = rng.normal(size=3) * 2.0
    P = np.array([np.sqrt(M**2 + pvec @ pvec), *pvec])
    s_rest = rng.normal(size=3); s_rest /= np.linalg.norm(s_rest)
    E = P[0]
    S = np.array([pvec @ s_rest / M, *(s_rest + pvec * (pvec @ s_rest) / (M * (E + M)))])   # covariant spin vector
    proj = (slash(P) + M * np.eye(4)) @ (np.eye(4) + g5 @ slash(S)) / 2
    w, v = np.linalg.eig(proj)
    u = v[:, np.argmax(w.real)] * np.sqrt(2 * M)                 # u ubar = proj up to normalisation
    ubar = u.conj() @ g[0]
    up = g[0] @ TD @ u.conj()                                     # PT image of the wave function (same momentum)
    proj_m = (slash(P) + M * np.eye(4)) @ (np.eye(4) - g5 @ slash(S)) / 2
    num = np.outer(up, up.conj() @ g[0])
    lamb = np.trace(num) / np.trace(proj_m)
    c = np.allclose(num, lamb * proj_m, atol=1e-10) and np.allclose(np.outer(u, ubar), (np.trace(np.outer(u, ubar)) / np.trace(proj)) * proj, atol=1e-10)
    print('(2) trial %d: |P| = %.2f, PT[u(P,S)] u-bar ~ (Pslash+M)(1 - g5 Sslash)/2 : %s' % (trial, np.linalg.norm(pvec), c))
    ok &= c

# ---- (3) b-space form of the Sivers term with the CONTEXT.md Fourier convention -------------------
#   f(x,k,S) = f_1 - f_1T^perp eps^{ij} k^i S^j/M  (Trento),  f~(x,b) = int d^2k e^{-i k.b} f(x,k)
#   => f~(x,b,S) = f~_1(x,b) + i M eps^{ij} b^i S^j f~_1T^{perp(1)}(x,b),  f~^{(1)} = -(2/M^2) d f~_1T^perp/d(b^2),
#      f~^{(1)}(x,0) = int d^2k k^2/(2M^2) f_1T^perp = f_1T^{perp(1)}(x)
kx, ky, bx, by, w, Mm, Nn = sp.symbols('k_x k_y b_x b_y w M N', positive=True)
gk = Nn * sp.exp(-(kx**2 + ky**2) / w)                          # Gaussian test f_1T^perp(k^2)
# the Gaussian factorizes: do the two 1D integrals separately (fast, exact)
def ft1(fx, kv, bv):
    return sp.simplify(sp.integrate(sp.exp(-sp.I * kv * bv) * fx, (kv, -sp.oo, sp.oo), conds='none'))
Gx = ft1(sp.exp(-kx**2 / w), kx, bx); Gy = ft1(sp.exp(-ky**2 / w), ky, by); Gkx = ft1(kx * sp.exp(-kx**2 / w), kx, bx)
gt = sp.simplify(Nn * Gx * Gy)                                  # f~_1T^perp(b^2)
lhs_x = sp.simplify(Nn * Gkx * Gy)                              # FT of k^x g(k^2)
b2 = sp.Symbol('b2', positive=True)
gt_b2 = sp.simplify(gt.subs(by, sp.sqrt(b2 - bx**2)))
dg = sp.diff(gt_b2, b2).subs(b2, bx**2 + by**2)
rhs_x = sp.simplify(2 * sp.I * bx * dg)
c5 = sp.simplify(lhs_x - rhs_x) == 0
f1 = sp.simplify((-2 / Mm**2) * dg).subs({bx: 0, by: 0})
mom = sp.simplify(sp.pi * sp.integrate(sp.Symbol('r')**3 / Mm**2 * Nn * sp.exp(-sp.Symbol('r')**2 / w), (sp.Symbol('r'), 0, sp.oo)))   # int d^2k k^2/(2M^2) g, polar
c6 = sp.simplify(f1 - mom) == 0
print('(3) FT[k^i g(k^2)] = 2 i b^i dg~/d(b^2): %s ;  f~^{(1)}(x,b=0) = f_1T^{perp(1)}(x): %s' % (c5, c6))
ok &= c5 and c6
# sign bookkeeping: -f_1T eps^{ij} S^j FT[k^i g]/M = -(eps^{ij} b^i S^j/M) 2i dg~/db^2 = + i M eps^{ij} b^i S^j [-(2/M^2) dg~/db^2]
print('    => f~(x,b,S) = f~_1 + i M eps^{ij} b^i S^j f~_1T^{perp(1)}(x,b)   (eps^{12} = +1, hadron along +z)')

# ---- (4) spectator model vs Bacchetta-Conti-Radici 2008 (point-like scalar diquark) ------------------
#   ours (sivers_spectator.py): f_1T^perp(SIDIS) = + g^2 e_q e_s/(4(2pi)^4) M(m+xM)(1-x)/(kT^2(kT^2+L^2)) ln((kT^2+L^2)/L^2)
#   BCR eq.(SivBM2-s-pl):       f_1T^perp       = - g_s^2 e_c^2/(4(2pi)^4) M(m+xM)(1-x)/(pT^2(L^2+pT^2))  log((L^2+pT^2)/L^2)
#   BCR rules: eikonal vertex -i e_c n^rho with propagator i/(-l^+ + i eps); diquark vertex +i e_c (2P-2p+l)^rho
#   ours:      eikonal (i e_q n)(-i/(l^+ - i0)),                          diquark vertex +i e_s (p_in+p_out)
#   => e_q = -e_c, e_s = e_c, i.e. e_q e_s = -e_c^2 (attractive); QCD: e_c^2 -> 4 pi C_F alpha_s (BCR)
import sivers_spectator as ss                      # prints its own checks
x_, kt2 = 0.37, 0.21
L2 = x_ * ss.lam**2 + (1 - x_) * ss.m**2 - x_ * (1 - x_) * ss.M**2
ours = ss.closed_forms(x_, kt2)[1]
ec2 = -ss.eqes
bcr = -ss.gY**2 * ec2 / (4 * (2 * np.pi)**4) * ss.M * (ss.m + x_ * ss.M) * (1 - x_) / (kt2 * (L2 + kt2)) * np.log((L2 + kt2) / L2)
print('(4) spectator model, x=%.2f kT^2=%.2f: ours f_1T(SIDIS) = %.6e ; BCR point-like with e_c^2 = -e_q e_s = %.1f: %.6e  -> %s' % (
    x_, kt2, ours, ec2, bcr, 'PASS' if np.isclose(ours, bcr, rtol=1e-12) else 'FAIL'))
ok &= np.isclose(ours, bcr, rtol=1e-12)
print('sivers symmetry checks:', 'PASS' if ok else 'FAIL')
