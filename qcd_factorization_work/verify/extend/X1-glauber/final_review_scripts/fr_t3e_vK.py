# Final review of X1 -- T3(e) step (3): the regulated localized weight v_K = w_K^[12] - 1/2 on the theta-contour.
# Pole sum (L1'): line e has poles z_e (final iff Im z_e<0), -iK (final), +iK (initial) with weights
#   u_z = K^2/(z^2+K^2), u_+ = z/(2(z-iK)) [pole +iK], u_- = z/(2(z+iK)) [pole -iK];
# race weights for colour order [12]: both final p1/(p1+p2); both initial p2/(p1+p2); (1 init,2 fin) 1; (1 fin,2 init) 0.
# Cross-check with the 1-D representation from the three-sector identity:
#   w^[12] = 1/2 + (i/2pi) PV int rho1(k) rho2(-k) dk/k,  rho_e(k) = z_e K^2/((z_e - k)(k^2+K^2)).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from scipy import integrate
rng = np.random.default_rng(5)
def wK(z1, z2, K):
    poles = lambda z: [(z, K**2/(z**2 + K**2)), (1j*K, z/(2*(z - 1j*K))), (-1j*K, z/(2*(z + 1j*K)))]
    tot = 0
    for p1, u1 in poles(z1):
        for p2, u2 in poles(z2):
            f1, f2 = p1.imag < 0, p2.imag < 0
            if f1 and f2: W = p1/(p1 + p2)
            elif (not f1) and (not f2): W = p2/(p1 + p2)
            elif (not f1) and f2: W = 1.0
            else: W = 0.0
            tot += u1*u2*W
    return tot
def wK_1d(z1, z2, K):
    rho = lambda z, k: z*K**2/((z - k)*(k**2 + K**2))
    g = lambda k: (rho(z1, k)*rho(z2, -k) - rho(z1, -k)*rho(z2, k))/(2*k)   # odd part / k (PV)
    re = integrate.quad(lambda k: g(k).real, 0, np.inf, limit=400)[0]*2
    im = integrate.quad(lambda k: g(k).imag, 0, np.inf, limit=400)[0]*2
    return 0.5 + 1j*(re + 1j*im)/(2*np.pi)
th = np.pi/4; K = 1.0
sup_v = 0; sup_ratio = 0; sup_rem = 0; worst_1d = 0; sup_ratio_any = 0
for n in range(200000):
    t = 10**rng.uniform(-4, 4, size=2); sg = rng.choice([-1, 1], size=2)
    # contour variable x_e = sg*|x_e|; z_e = a_e/(2 e^{i th} x_e); x^K_e = iK/z_e has modulus t_e
    z = 1j*K/(sg*t*np.exp(1j*(th + np.pi/2)))
    xK = 1j*K/z
    v = wK(z[0], z[1], K) - 0.5
    sup_v = max(sup_v, abs(v))
    if max(t) <= 0.25:
        sup_ratio = max(sup_ratio, abs(v)/(t[0] + t[1]))
        sup_rem = max(sup_rem, abs(v - (xK[0] - xK[1])/4)/(t[0] + t[1])**2)
    sup_ratio_any = max(sup_ratio_any, abs(v)/min(0.5, 2*max(t)))
    if n < 300:
        worst_1d = max(worst_1d, abs(wK_1d(z[0], z[1], K) - (v + 0.5)))
print(f"theta=pi/4: sup|v_K| = {sup_v:.6f}  (proof uses <= 1/2)")
print(f"            sup |v_K|/(|x1|+|x2|) over |x_e|<=1/4 = {sup_ratio:.6f}  (proof uses <= 1/4)")
print(f"            sup |v_K - (x1-x2)/4|/(|x1|+|x2|)^2 over |x_e|<=1/4 = {sup_rem:.4f}  (report 0.044)")
print(f"            sup |v_K| / min(1/2, 2 max|x_e|) = {sup_ratio_any:.4f}  (consistent with |v_K| <= min(1/2, 8KR/a_min))")
print(f"            pole-sum vs 1-D PV representation: max diff over 300 points = {worst_1d:.1e}")
# crude provable bound: |w| <= sum|u1||u2| (each race weight has modulus <= 1 in closed quadrants)
cU = 0
for s in np.exp(np.linspace(np.log(1e-4), np.log(1e4), 200001)):
    z = s*np.exp(-1j*th)
    cU = max(cU, abs(K**2/(z**2 + K**2)) + abs(z/(2*(z - 1j*K))) + abs(z/(2*(z + 1j*K))))
print(f"            c_U on the pi/4 ray = {cU:.5f}; crude analytic bound 1+sqrt2 = {1+np.sqrt(2):.4f}; provable |v_K| <= c_U^2 + 1/2 = {cU**2+0.5:.3f}")
