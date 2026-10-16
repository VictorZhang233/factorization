# E12 stage-2 check: normalization of the near-threshold J/psi amplitude in Guo-Ji-Liu (2021) / Guo-Ji-Liu-Yang (2023).
# (a) spin sum by Dirac traces (numpy, random kinematics), (b) Gordon reduction of the C term,
# (c) algebraic identity between the trace result and the printed form of |G|^2,
# (d) high-energy normalization test against the classic LO formula (Ryskin 1993; RRML Z.Phys.C76 (1997) 231):
#     dsigma/dt|_{t=0} = Gamma_ee M^3 pi^3/(48 alpha) * (alpha_s/Qbar^4)^2 [x g(x)]^2,  Qbar^2 = M^2/4,
#     using GJL (13),(14),(17): G = (1/2xi) int dx A(x,xi) F_g, Im A = pi[delta(x-xi)+delta(x+xi)],
#     dsigma/dt = alpha e_Q^2/(4 (W^2-M_N^2)^2) (16 pi alpha_s)^2/(3 M_V^3) |psi(0)|^2 |G|^2,
#     Gamma_ee = 16 pi alpha^2 e_Q^2 |psi(0)|^2 / M_V^2 (Van Royen-Weisskopf, N_c = 3).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp

rng = np.random.default_rng(12345)
I2 = np.eye(2); Z2 = np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
g0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
gs = [np.block([[Z2, s], [-s, Z2]]) for s in (sx, sy, sz)]
gam = [g0] + gs                                # gamma^mu, mu = 0..3
metric = np.diag([1., -1., -1., -1.])
def slash(p):  # p^mu contravariant
    return sum(metric[m, m]*p[m]*gam[m] for m in range(4))
gplus = (gam[0] + gam[3])/np.sqrt(2)          # gamma^+ = (gamma^0 + gamma^3)/sqrt2
def plus(v): return (v[0] + v[3])/np.sqrt(2)
def sigma(mu, nu): return 0.5j*(gam[mu] @ gam[nu] - gam[nu] @ gam[mu])
def sigma_plus_nu_Delta(D):  # sigma^{+ nu} Delta_nu
    Dlow = metric @ D
    s = np.zeros((4, 4), complex)
    for nu in range(4):
        s += (sigma(0, nu) + sigma(3, nu))/np.sqrt(2)*Dlow[nu]
    return s
def bar(G): return g0 @ G.conj().T @ g0

maxdev = 0.0; maxdev2 = 0.0
for trial in range(20):
    M = 0.938
    # random on-shell momenta
    p = rng.normal(size=3)*2; pp = rng.normal(size=3)*2
    P = np.array([np.sqrt(M**2 + p @ p), *p]); Pp = np.array([np.sqrt(M**2 + pp @ pp), *pp])
    Pbar = (P + Pp)/2; D = Pp - P
    xi = -plus(D)/(2*plus(Pbar)); t = D @ metric @ D
    H, E = rng.normal(), rng.normal()
    Gam = H*gplus + E*1j*sigma_plus_nu_Delta(D)/(2*M)
    tr = np.trace((slash(Pp) + M*np.eye(4)) @ Gam @ (slash(P) + M*np.eye(4)) @ bar(Gam)).real
    formula = 4*plus(Pbar)**2*((1 - xi**2)*H**2 - 2*xi**2*H*E - (xi**2 + t/(4*M**2))*E**2)
    maxdev = max(maxdev, abs(0.5*tr/formula - 1))
    # (b) Gordon: u'bar [A g+ P+ + B P+ i sigma Delta/2M + C (Delta+)^2/M] u = P+ u'bar[(A+4xi^2 C) g+ + (B-4xi^2 C) i sigma Delta/2M] u
    A_, B_, C_ = rng.normal(size=3)
    lhs = A_*gplus*plus(Pbar) + B_*plus(Pbar)*1j*sigma_plus_nu_Delta(D)/(2*M) + C_*plus(D)**2/M*np.eye(4)
    rhs = plus(Pbar)*((A_ + 4*xi**2*C_)*gplus + (B_ - 4*xi**2*C_)*1j*sigma_plus_nu_Delta(D)/(2*M))
    # compare sandwiched between on-shell projectors: (P'slash+M) X (Pslash+M)
    X = (slash(Pp) + M*np.eye(4)) @ (lhs - rhs) @ (slash(P) + M*np.eye(4))
    maxdev2 = max(maxdev2, np.abs(X).max()/np.abs((slash(Pp) + M*np.eye(4)) @ lhs @ (slash(P) + M*np.eye(4))).max())
print('(a) spin sum: max |(1/2)Tr / [4 P+^2((1-xi^2)H^2 - 2xi^2 HE - (xi^2+t/4M^2)E^2)] - 1| =', maxdev)
print('(b) Gordon reduction H2 = A + 4 xi^2 C, E2 = B - 4 xi^2 C: max relative residual =', maxdev2)

# (c) identity
H2, E2, x_, t_, M_ = sp.symbols('H_2 E_2 xi t M')
trace_form = (1 - x_**2)*H2**2 - 2*x_**2*H2*E2 - (x_**2 + t_/(4*M_**2))*E2**2
printed = (1 - t_/(4*M_**2))*E2**2 - 2*E2*(H2 + E2) + (1 - x_**2)*(H2 + E2)**2
print('(c) trace form - printed brace =', sp.expand(trace_form - printed))
print('    => with G = <T^{++}>/(xi^2 P+^2) (no 1/2): (1/2)sum|G|^2 = (4/xi^4){...} [2023 eq.(5)]; with the 2021 1/2: (1/xi^4){...} [2021 eq.(26)]')

# (d) high-energy normalization test
al, eQ, aS, psi2, Mv, W, xg = sp.symbols('alpha e_Q alpha_s psi2 M_V W xg', positive=True)
for label, norm in [('corrected (2023) F_g', 1), ('2021 F_g with Tr (1/2)', sp.Rational(1, 2))]:
    x_B = Mv**2/W**2; xi_ = x_B/2
    # Im G = (pi/xi) F_g(xi,xi,0); F_g = (1/2P+) H_g ubar g+ u, spin-averaged |ubar g+ u|^2 -> 4 P+^2 (xi->0); H_g(xi,xi) ~ norm * x g(x)
    G2 = (sp.pi/xi_)**2*(norm*xg)**2          # (1/4P+^2) * 4P+^2 cancels
    dsdt = al*eQ**2/(4*W**4)*(16*sp.pi*aS)**2/(3*Mv**3)*psi2*G2
    Gee = 16*sp.pi*al**2*eQ**2*psi2/Mv**2
    Qb2 = Mv**2/4
    ryskin = Gee*Mv**3*sp.pi**3/(48*al)*(aS/Qb2**2)**2*xg**2
    print('(d)', label, ': [GJL (13),(14),(17)] / [Ryskin LO] =', sp.simplify(dsdt/ryskin))
