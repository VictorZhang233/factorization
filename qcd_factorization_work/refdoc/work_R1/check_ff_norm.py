"""R1 check 4: normalisation of the collinear fragmentation function (refdoc Def. 2.2, eq. (2.13), p.13):
   d_{h/q}(z) = z^{d-3}/(4 N_c) sum_X int dw^-/(2pi) e^{i k^+ w^-} Tr[ gamma^+ <0|psi(w)|h X><h X|psibar(0)|0> ],
   hadron frame (p_T = 0), k^+ = p^+/z.
Test: 'hadron' = quark, X = one gluon, O(alpha_s), light-cone gauge A^+ = 0 (Wilson line = 1), d = 4.
Expected (number density of quarks with fraction z, integrated over relative transverse momentum):
   d^{(1)}(z) = (alpha_s/2pi) C_F (1+z^2)/(1-z) * int dl_T^2/l_T^2      (z<1)
We compute the coefficient of int dl_T^2/l_T^2 with prefactor z (=z^{d-3} at d=4) and compare;
a prefactor 1/z would give the result times 1/z^2.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

# explicit Dirac matrices (Dirac rep) with sympy
I2 = sp.eye(2); Z2 = sp.zeros(2)
sx = sp.Matrix([[0, 1], [1, 0]]); sy = sp.Matrix([[0, -sp.I], [sp.I, 0]]); sz = sp.Matrix([[1, 0], [0, -1]])
def blk(a, b, c, d):
    M = sp.zeros(4)
    M[:2, :2] = a; M[:2, 2:] = b; M[2:, :2] = c; M[2:, 2:] = d
    return M
g0 = blk(I2, Z2, Z2, -I2)
gi = [blk(Z2, s, -s, Z2) for s in (sx, sy, sz)]
G = [g0] + gi
eta = sp.diag(1, -1, -1, -1)
def slash(v):  # v contravariant (0,1,2,3)
    return sum(((eta[m, m] * v[m]) * G[m] for m in range(4)), sp.zeros(4))
r2 = sp.sqrt(2)
def lc(vp, vm, vx, vy):  # from light-cone (+,-,x,y) to (0,1,2,3)
    return [(vp + vm) / r2, vx, vy, (vp - vm) / r2]
def mdot(a, b):
    return sum(eta[m, m] * a[m] * b[m] for m in range(4))

z, pp, lT = sp.symbols('z p_plus l_T', positive=True)
lp = pp * (1 - z) / z                      # l^+ fixed by delta(k^+ - p^+ - l^+), k^+ = p^+/z
p = lc(pp, 0, 0, 0)                        # hadron (quark) along +z, p_T=0, massless
l = lc(lp, lT**2 / (2 * lp), lT, 0)         # on-shell gluon
k = [p[i] + l[i] for i in range(4)]
k2 = sp.simplify(mdot(k, k))
gplus = (G[0] + G[3]) / r2
nbar = lc(0, 1, 0, 0)                      # nbar.A = A^+  (light-cone gauge vector)
# polarisation sum in A^+=0 gauge: d^{mu nu} = -g^{mu nu} + (l^mu nbar^nu + nbar^mu l^nu)/(nbar.l)
nl = mdot(nbar, l)
N = 0
for mu in range(4):
    for nu in range(4):
        dmunu = -eta[mu, nu] + (l[mu] * nbar[nu] + nbar[mu] * l[nu]) / nl
        if dmunu == 0:
            continue
        # gamma_mu ... gamma_nu with lower indices: gamma_mu = eta_{mu mu} gamma^mu
        N += dmunu * (gplus * slash(k) * (eta[mu, mu] * G[mu]) * slash(p) * (eta[nu, nu] * G[nu]) * slash(k)).trace()
N = sp.simplify(N)
# amplitude <0|psi|q(p) g(l)> = [i kslash/k^2] (i g gamma^mu t^a eps*_mu) u(p)  (overall phase irrelevant);
# |.|^2 summed over spins/colours: g^2 C_F N_c * Tr[gamma^+ kslash gamma^mu pslash gamma^nu kslash] d_{mu nu} / (k^2)^2
# phase space of the gluon: int dl^+ d^2l_T / ((2pi)^3 2 l^+); the w^- integral gives delta(k^+ - p^+ - l^+) -> removes dl^+
gs, Nc, CF = sp.symbols('g N_c C_F', positive=True)
for name, pref in [('z^{d-3} = z (doc, Collins-Soper)', z), ('1/z (blueprint 0.4(8))', 1 / z)]:
    dens = pref / (4 * Nc) * gs**2 * CF * Nc * N / k2**2 / ((2 * sp.pi)**3 * 2 * lp)
    # d^2 l_T = pi d(l_T^2); write as coefficient of d(l_T^2)/l_T^2:
    coeff = sp.simplify(dens * sp.pi * lT**2)
    target = gs**2 / (4 * sp.pi) / (2 * sp.pi) * CF * (1 + z**2) / (1 - z)
    print(f"{name:36s}: coefficient of dl_T^2/l_T^2 = {sp.factor(coeff)} ;  ratio to (alpha_s/2pi) C_F (1+z^2)/(1-z) = {sp.simplify(coeff / target)}")
