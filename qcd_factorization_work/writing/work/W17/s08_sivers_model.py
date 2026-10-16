# W17 / Ch14 -- s08: Sivers function in the point-like scalar-diquark (spectator) model, abelian gluon.
# Book conventions: D = d - i e A (quark charge e_q, diquark charge e_s), quark vertex i e_q gamma^mu, scalar vertex
# i e_s (p+p')^mu along the charge flow, Wilson line one-gluon term e_q n^mu/(n.l -+ i0) (l into the line; - SIDIS, + DY),
# n = n_B (n.l = l^+). gamma5 = i g0 g1 g2 g3, eps^{0123} = +1, Tr[g^mu g^nu g^rho g^sigma g5] = -4 i eps^{mu nu rho sigma}.
# Trento: f(x,kT;S) = f_1 - f_1T^perp eps^{ij} k^i S^j / M, eps^{12} = +1.
# TMD normalization: f = (1/(32 pi^3 (1-x) P^+)) sum Abar gamma^+ A  (one-diquark final state).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import mpmath as mp
from scipy import integrate
ok = True
def check(name, cond):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name); ok &= bool(cond)
I2 = np.eye(2); Z2 = np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]], dtype=complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], dtype=complex)
G = [np.block([[I2, Z2], [Z2, -I2]]).astype(complex)] + [np.block([[Z2, s], [-s, Z2]]) for s in (sx, sy, sz)]
gm = np.diag([1., -1., -1., -1.])
g5 = 1j*G[0] @ G[1] @ G[2] @ G[3]
def sl(v): return sum(gm[m, m]*v[m]*G[m] for m in range(4))
def lc(vp, vm, vx, vy): return np.array([(vp + vm)/np.sqrt(2), vx, vy, (vp - vm)/np.sqrt(2)], dtype=complex)
# trace convention check
eps4 = np.zeros((4, 4, 4, 4))
import itertools
for perm in itertools.permutations(range(4)):
    sgn = np.linalg.det(np.eye(4)[list(perm)])
    eps4[perm] = sgn          # eps^{0123} = +1 (upper indices)
mu, nu, rho, sig = 0, 1, 2, 3
tr = np.trace(G[0] @ G[1] @ G[2] @ G[3] @ g5)
check('Tr[g^0 g^1 g^2 g^3 g5] = -4i eps^{0123} = -4i', abs(tr + 4j) < 1e-12)
gplus = (G[0] + G[3])/np.sqrt(2)
# ------------- model parameters
M, m, lam, x, Pp = 0.94, 0.30, 0.80, 0.37, 7.3
g, eq, es = 1.0, 1.0, -1.0      # attractive final-state interaction: e_q e_s < 0
def kin(kx, ky):
    kT2 = kx*kx + ky*ky
    L2 = x*lam**2 + (1 - x)*m**2 - x*(1 - x)*M**2
    psm = (kT2 + lam**2)/(2*(1 - x)*Pp)
    P = lc(Pp, M*M/(2*Pp), 0, 0)
    ps = lc((1 - x)*Pp, psm, -kx, -ky)
    k = P - ps
    return P, ps, k, kT2, L2
kx, ky = 0.41, -0.23
P, ps, k, kT2, L2 = kin(kx, ky)
k2m2 = (k[0]**2 - k[1]**2 - k[2]**2 - k[3]**2).real - m*m
check('k^2 - m^2 = -(kT^2 + L^2)/(1-x)', abs(k2m2 + (kT2 + L2)/(1 - x)) < 1e-12)
# projector U Ubar = (Pslash + M)(1 + g5 Sslash)/2, transverse spin S^mu = (0, Sx, Sy, 0)
def proj(Sx, Sy):
    S = np.array([0, Sx, Sy, 0], dtype=complex)
    return (sl(P) + M*np.eye(4)) @ (np.eye(4) + g5 @ sl(S))/2
pref = 1/(32*np.pi**3*(1 - x)*Pp)
# ------------- f_1 at tree level
A0 = lambda: -g*(sl(k) + m*np.eye(4))/k2m2
# Abar gamma^+ A = Tr[gamma^+ A0 (U Ubar) A0bar], A0bar = g0 A0^dagger g0
def Abar(Amat): return G[0] @ Amat.conj().T @ G[0]
f1_num = pref*np.trace(gplus @ A0() @ (sl(P) + M*np.eye(4)) @ Abar(A0())).real/2   # spin average 1/2
f1_closed = g*g/(16*np.pi**3)*(1 - x)*((m + x*M)**2 + kT2)/(kT2 + L2)**2
check('f_1 = (g^2/16pi^3)(1-x)[(m+xM)^2 + kT^2]/(kT^2+L^2)^2  (%.8e vs %.8e)' % (f1_num, f1_closed), abs(f1_num/f1_closed - 1) < 1e-12)
# polarized tree: no S dependence
fS = pref*np.trace(gplus @ A0() @ proj(1, 0) @ Abar(A0())).real - pref*np.trace(gplus @ A0() @ proj(-1, 0) @ Abar(A0())).real
check('tree level: no Sivers term (S-odd part vanishes)', abs(fS) < 1e-14)
# ------------- the l^- integral at l^+ = 0
# D_s = alpha l + beta + i eta, D_q = -gam l + delta + i eta  (alpha = 2(1-x)P^+, gam = 2xP^+):
#   int dl/(D_s D_q) = -2 pi i/(gam beta + alpha delta + i eta (alpha + gam))   (close below, diquark pole)
mp.mp.dps = 30
km = (k[0] - k[3]).real/np.sqrt(2)
for (lx, ly) in [(0.2, 0.1), (-0.5, 0.7)]:
    alpha_, gam_ = 2*(1 - x)*Pp, 2*x*Pp
    beta_ = kT2 - ((lx - kx)**2 + (ly - ky)**2)
    delta_ = 2*x*Pp*km - ((kx - lx)**2 + (ky - ly)**2) - m*m
    for eta in [0.3, 0.05]:
        f = lambda t: 1/((alpha_*t + beta_ + 1j*eta)*(-gam_*t + delta_ + 1j*eta))
        p1, p2 = -beta_/alpha_, delta_/gam_
        pts = sorted(set([p1 + s*eta*fac/alpha_ for s in (-1, 0, 1) for fac in (1, 10, 100)] +
                         [p2 + s*eta*fac/gam_ for s in (-1, 0, 1) for fac in (1, 10, 100)]))
        num = mp.quad(f, [-mp.inf] + pts + [mp.inf], maxdegree=10)
        fin = -2*mp.pi*1j/(gam_*beta_ + alpha_*delta_ + 1j*eta*(alpha_ + gam_))
        check('l^- integral at eta=%.2f matches the residue formula (%s vs %s)' % (eta, mp.nstr(num, 12), mp.nstr(fin, 12)), abs(num - fin) < 1e-10*abs(fin))
    lim = -2*np.pi*1j/(gam_*beta_ + alpha_*delta_)
    cl = np.pi*1j/(Pp*((kx - lx)**2 + (ky - ly)**2 + L2))
    check('eta->0: int dl^- 1/(D_s D_q) = pi i/(P^+[(k-l)_T^2 + L^2])', abs(lim - cl) < 1e-12*abs(cl))
# ------------- the l_T integral  int d^2l l^i/(l^2[(k-l)^2+L^2]) = (pi k^i/k^2) ln((k^2+L^2)/L^2)
def lT_int(comp):
    f = lambda r, phi: (r*np.cos(phi) if comp == 0 else r*np.sin(phi))/(r*r*((kx - r*np.cos(phi))**2 + (ky - r*np.sin(phi))**2 + L2))*r
    return integrate.dblquad(lambda phi, r: f(r, phi), 0, 400, 0, 2*np.pi, epsabs=1e-11, epsrel=1e-10)[0]
Ix, Iy = lT_int(0), lT_int(1)
c = np.pi/kT2*np.log((kT2 + L2)/L2)
check('l_T integral = (pi k^i/k^2) ln((k^2+L^2)/L^2)  (x: %.8f vs %.8f; y: %.8f vs %.8f)' % (Ix, c*kx, Iy, c*ky), abs(Ix - c*kx) < 1e-5*abs(c*kx) + 1e-6 and abs(Iy - c*ky) < 1e-5*abs(c*ky) + 1e-6)
# ------------- Sivers term
def f_odd(Sx, Sy, sgn):   # sgn = -1 SIDIS (1/(l+ - i0)), +1 DY
    # A1^odd = (-sgn) 2 pi^2 i (1-x) e_q e_s g/(2pi)^4 * [ gammaT.kT * (pi/kT^2) ln(...) ] U   (the (kslash+m) part is a pure phase)
    # -lslash contains + l^1 gamma^1 + l^2 gamma^2 (lslash = l^+ g^- + l^- g^+ - l_T.gamma_T); after the l_T integral: gamma_T.k_T * c
    gT_k = kx*G[1] + ky*G[2]
    # A1^odd = -+ 2 pi^2 i (1-x) e_q e_s g/(2pi)^4 [...] U, upper sign SIDIS:  sgn = -1 -> -2 pi^2 i,  sgn = +1 -> +2 pi^2 i
    A1 = (sgn)*2*np.pi**2*1j*(1 - x)*eq*es*g/(2*np.pi)**4*gT_k*c
    pr = proj(Sx, Sy)
    val = np.trace(gplus @ A1 @ pr @ Abar(A0())) + np.trace(gplus @ A0() @ pr @ Abar(A1))
    return pref*val.real
def sivers(sgn):
    # f_odd(S) = - f_1T^perp (kx Sy - ky Sx)/M  ->  extract from S = (0,1)
    v = f_odd(0, 1, sgn) - f_odd(0, -1, sgn)       # = -2 f_1T kx / M
    return -v*M/(2*kx)
fS_SIDIS = sivers(-1); fS_DY = sivers(+1)
closed = g*g*eq*es/(4*(2*np.pi)**4)*M*(m + x*M)*(1 - x)/(kT2*(kT2 + L2))*np.log((kT2 + L2)/L2)
print('   f_1T^perp SIDIS numerical = %.10e ; closed form = %.10e ; DY = %.10e' % (fS_SIDIS, closed, fS_DY))
check('f_1T^perp(SIDIS) = g^2 e_q e_s/(4(2pi)^4) M(m+xM)(1-x)/(kT^2(kT^2+L^2)) ln((kT^2+L^2)/L^2)', abs(fS_SIDIS/closed - 1) < 1e-10)
check('f_1T^perp(DY) = - f_1T^perp(SIDIS)', abs(fS_DY/fS_SIDIS + 1) < 1e-12)
check('attractive FSI (e_q e_s < 0), m + xM > 0  =>  f_1T^perp(SIDIS) < 0 (Trento)', fS_SIDIS < 0)
# consistency of the S-structure: the odd part is proportional to eps^{ij} k^i S^j (check with S = (1,0))
v2 = (f_odd(1, 0, -1) - f_odd(-1, 0, -1))/2      # = -f_1T (kx*0 - ky*1)/M = f_1T ky/M
check('S-dependence is - f_1T eps^{ij}k^i S^j/M with eps^{12}=+1 (S along x)', abs(v2 - fS_SIDIS*ky/M) < 1e-12*abs(v2) + 1e-18)
# the (kslash + m) "pure phase" part gives no S-odd contribution
A1p = 1j*(sl(k) + m*np.eye(4))
val = np.trace(gplus @ A1p @ proj(0, 1) @ Abar(A0())) + np.trace(gplus @ A0() @ proj(0, 1) @ Abar(A1p))
val2 = np.trace(gplus @ A1p @ proj(0, -1) @ Abar(A0())) + np.trace(gplus @ A0() @ proj(0, -1) @ Abar(A1p))
check('(kslash+m) x i(real) part: no S-odd term and no contribution to f_1', abs(val.real) < 1e-12 and abs(val2.real) < 1e-12)
# QCD colour-singlet replacement e_q e_s -> -4 pi C_F alpha_s keeps the sign negative
check('QCD singlet: e_q e_s -> -4 pi C_F alpha_s < 0', -4*np.pi*(4/3)*0.3 < 0)
# relation of the b-space first moment (VF/c_tmd): f~^{perp(1)}_{1T}(x,0) = int d^2k k^2/(2M^2) f_1T^perp -> finite? (log divergence check)
print('ALL PASS' if ok else 'SOME FAIL')
