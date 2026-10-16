# Sivers function at one-gluon exchange in the scalar-diquark spectator model
# (Brodsky-Hwang-Schmidt 2002; Ji-Yuan 2002), binding conventions (D = d - i e A, metric +---).
# Abelian charges: quark e_q (also on the Wilson line), diquark e_s; QCD colour singlet: e_q e_s -> -C_F g^2.
# f(x,kT;S) = 1/(4 (2pi)^3 (1-x) P^+) * sum Mbar gamma^+ M  (cut on the on-shell diquark)
# Tree:   M0 = -g (k+m) U /(k^2-m^2),     k^2-m^2 = -(kT^2+L^2)/(1-x),  L^2 = x lam^2 + (1-x) m^2 - x(1-x) M^2
# 1-loop (gluon between the Wilson line and the diquark, amplitude side), T-odd part from
#   SIDIS: 1/(l^+ - i0) -> +i pi delta(l^+) ;  DY: 1/(l^+ + i0) -> -i pi delta(l^+)
#   M1odd = -2 pi^2 i (1-x) e_q e_s g/(2pi)^4 * s_link * int d^2l (kslash + gamma_T.l + m) U /(l^2((k-l)^2+L^2))
# Trento convention: f = f_1 - f_1T^perp eps^{ij} kT^i ST^j / M,  eps^{12}=+1.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from scipy.integrate import quad, dblquad

# Dirac representation
I2, Z2 = np.eye(2), np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
g0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
gs = [np.block([[Z2, s], [-s, Z2]]) for s in (sx, sy, sz)]
G = [g0] + gs                                   # gamma^mu (upper index)
g5 = 1j * G[0] @ G[1] @ G[2] @ G[3]
gp = (G[0] + G[3]) / np.sqrt(2)                 # gamma^+
eta = np.diag([1, -1, -1, -1])
def slash(v):  # v contravariant (v^0,v^1,v^2,v^3)
    vl = eta @ v
    return sum(G[m] * vl[m] for m in range(4))
def lc_to_cart(vp, vm, vT):
    return np.array([(vp + vm) / np.sqrt(2), vT[0], vT[1], (vp - vm) / np.sqrt(2)])

M, m, lam, gY = 0.94, 0.3, 0.8, 1.0
eqes = -1.0     # attractive (opposite charges), e.g. QCD singlet e_q e_s -> -C_F g^2 (units)
Pp = 5.0

def kin(x, kT):
    L2 = x * lam**2 + (1 - x) * m**2 - x * (1 - x) * M**2
    P = lc_to_cart(Pp, M**2 / (2 * Pp), (0, 0))
    kp = x * Pp
    km = M**2 / (2 * Pp) - (kT[0]**2 + kT[1]**2 + lam**2) / (2 * (1 - x) * Pp)
    k = lc_to_cart(kp, km, kT)
    return L2, P, k

def proj(P, S):   # U Ubar = (Pslash + M)(1 + g5 Sslash)/2
    return (slash(P) + M * np.eye(4)) @ (np.eye(4) + g5 @ slash(S)) / 2

def f1_tree(x, kTv, S):
    L2, P, k = kin(x, kTv)
    kt2 = kTv[0]**2 + kTv[1]**2
    den = -(kt2 + L2) / (1 - x)
    A = (slash(k) + m * np.eye(4))
    tr = np.trace(A @ gp @ A @ proj(P, S)) * gY**2 / den**2
    return (tr / (4 * (2 * np.pi)**3 * (1 - x) * Pp)).real

def lT_integral(kTv, L2):
    """int d^2l l^i/(l^2 ((k-l)^2+L^2)), numerically (polar coords), returns 2-vector"""
    kx, ky = kTv
    def comp(i):
        f = lambda phi, r: (r * np.cos(phi) if i == 0 else r * np.sin(phi)) * r / (r * r * ((kx - r * np.cos(phi))**2 + (ky - r * np.sin(phi))**2 + L2))
        v, _ = dblquad(f, 0, 60, 0, 2 * np.pi, epsabs=1e-11, epsrel=1e-10)
        # large-r tail: angular average of l^i (2 k.l)/l^6 gives 2 pi k^i/r^4 -> int_R^inf r dr 2 pi k^i/r^4 = pi k^i/R^2
        tail = np.pi * (kx if i == 0 else ky) / 60.0**2
        return v + tail
    return np.array([comp(0), comp(1)])

def f_odd(x, kTv, S, link, lint=None):
    s_link = +1 if link == 'SIDIS' else -1
    L2, P, k = kin(x, kTv)
    kt2 = kTv[0]**2 + kTv[1]**2
    den = -(kt2 + L2) / (1 - x)
    if lint is None:
        lint = np.pi * np.array(kTv) / kt2 * np.log(1 + kt2 / L2)     # analytic transverse integral
    gTl = G[1] * lint[0] + G[2] * lint[1]                               # gamma^i l^i  (contravariant comps)
    M0bar = -gY * (slash(k) + m * np.eye(4)) / den                      # acts as Ubar(...) inside the trace
    C1 = -2 * np.pi**2 * 1j * (1 - x) * eqes * gY / (2 * np.pi)**4 * s_link
    amp = M0bar @ gp @ (C1 * gTl)                                       # Mbar0 gamma^+ M1odd (without U)
    val = 2 * np.real(np.trace(amp @ proj(P, S)))
    return val / (4 * (2 * np.pi)**3 * (1 - x) * Pp)

def closed_forms(x, kt2):
    L2 = x * lam**2 + (1 - x) * m**2 - x * (1 - x) * M**2
    f1 = gY**2 / (16 * np.pi**3) * (1 - x) * ((m + x * M)**2 + kt2) / (kt2 + L2)**2
    siv = +gY**2 * eqes / (4 * (2 * np.pi)**4) * M * (m + x * M) * (1 - x) / (kt2 * (kt2 + L2)) * np.log((kt2 + L2) / L2)
    return f1, siv

ok = True
print('transverse integral check  int d^2l l/(l^2((k-l)^2+L^2)) = pi k/k^2 ln(1+k^2/L^2):')
for (x, kTv) in [(0.3, (0.4, 0.1)), (0.6, (0.2, -0.5))]:
    L2 = x * lam**2 + (1 - x) * m**2 - x * (1 - x) * M**2
    num = lT_integral(kTv, L2)
    ana = np.pi * np.array(kTv) / (kTv[0]**2 + kTv[1]**2) * np.log(1 + (kTv[0]**2 + kTv[1]**2) / L2)
    print('   numeric', num, ' analytic', ana)
    ok &= np.allclose(num, ana, rtol=2e-6, atol=1e-8)

print('tree f_1 and Sivers function (Trento) vs closed forms:')
for (x, kTv) in [(0.2, (0.3, 0.0)), (0.5, (0.25, 0.4)), (0.8, (0.6, -0.2))]:
    kt2 = kTv[0]**2 + kTv[1]**2
    Sx = np.array([0, 1.0, 0, 0]); Sy = np.array([0, 0, 1.0, 0])
    f1n = f1_tree(x, kTv, np.zeros(4) + Sx * 0)        # unpolarized part: S->0 in projector  (proj with S=0)
    f1_S = 0.5 * (f1_tree(x, kTv, Sx) + f1_tree(x, kTv, -Sx))
    res = {}
    for link in ('SIDIS', 'DY'):
        # eps^{ij} k^i S^j for S=y: kx ; for S=x: -ky.  f_odd = -f1T eps k S / M
        fy, fx = f_odd(x, kTv, Sy, link), f_odd(x, kTv, Sx, link)
        # solve least squares for f1T from both spin directions
        A = np.array([-kTv[0] / M, kTv[1] / M]); b = np.array([fy, fx])
        res[link] = A @ b / (A @ A)
    f1c, sivc = closed_forms(x, kt2)
    print('  x=%.1f kT=(%.2f,%.2f): f1 num=%.6e closed=%.6e | f1T(SIDIS) num=%.6e closed=%.6e | f1T(DY)=%.6e  ratio DY/SIDIS=%.6f'
          % (x, kTv[0], kTv[1], f1_S, f1c, res['SIDIS'], sivc, res['DY'], res['DY'] / res['SIDIS']))
    ok &= abs(f1_S / f1c - 1) < 1e-10 and abs(res['SIDIS'] / sivc - 1) < 1e-10 and abs(res['DY'] / res['SIDIS'] + 1) < 1e-12
print('sign of f1T^perp(SIDIS) for attractive FSI (e_q e_s<0), Trento convention:', 'positive' if res['SIDIS'] > 0 else 'negative')
print('Spectator-model checks:', 'PASS' if ok else 'FAIL')
