# Round-3 reviewer 2 -- T3(e) ingredients on the theta = pi/4 contour: the per-line regulator-pole weights
# (sum rule, c_U = sup sum_p |u(p)|), and v_K = w_K^[12] - 1/2 (bounds |v_K| <= (|x1|+|x2|)/4 for |x_e| <= 1/4,
# |v_K| <= 1/2, leading term (x1 - x2)/4), computed from the L1' race with gluon pole z_e and regulator poles +-iK.
import sys, os, itertools, math, cmath
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
K = 1.0
def poles(z):
    uz = K**2/(z**2 + K**2); up = z/(2*(z - 1j*K)); um = z/(2*(z + 1j*K))
    return [(z, uz, 'F' if z.imag < 0 else 'I'), (1j*K, up, 'I'), (-1j*K, um, 'F')]
def w12(z1, z2):
    tot = 0
    for (p1, u1, g1), (p2, u2, g2) in itertools.product(poles(z1), poles(z2)):
        if g1 == 'F' and g2 == 'F':   w = p1/(p1 + p2)
        elif g1 == 'I' and g2 == 'I': w = p2/(p1 + p2)
        elif g1 == 'I' and g2 == 'F': w = 1.0
        else:                         w = 0.0
        tot += u1*u2*w
    return tot
def zfrom(kappa, a, theta=np.pi/4):   # z_e = a/(2 k^+), k^+ = e^{i theta} kappa
    return a/(2*cmath.exp(1j*theta)*kappa)
# sum rule and c_U
cu = 0; sr = 0
for kap in np.concatenate([np.geomspace(1e-6, 1e6, 4001), -np.geomspace(1e-6, 1e6, 4001)]):
    z = zfrom(kap, 1.0)
    ps = poles(z)
    sr = max(sr, abs(sum(u for _, u, _ in ps) - 1))
    cu = max(cu, sum(abs(u) for _, u, _ in ps))
print(f'per-line sum rule max|sum u - 1| = {sr:.2e};  c_U = sup sum|u| on the pi/4 rays = {cu:.4f}  (report: 1.65)')
# unregulated limit: K -> 0 relative to |z| large x; check race limits
rng = np.random.default_rng(3)
c_v = 0; c_inf = 0; lead = 0; maxx = 0
for trial in range(200000):
    a1, a2 = rng.uniform(0.2, 5, 2)
    k1, k2 = rng.choice([-1, 1], 2) * 10**rng.uniform(-6, 3, 2)
    z1, z2 = zfrom(k1, a1), zfrom(k2, a2)
    x1, x2 = 1j*K/z1, 1j*K/z2
    v = w12(z1, z2) - 0.5
    c_inf = max(c_inf, abs(v))
    if abs(x1) <= 0.25 and abs(x2) <= 0.25:
        c_v = max(c_v, abs(v)/(abs(x1) + abs(x2)))
        lead = max(lead, abs(v - (x1 - x2)/4)/(abs(x1) + abs(x2))**2)
print(f'sup |v_K| = {c_inf:.4f} (claim <= 1/2);  sup |v_K|/(|x1|+|x2|) for |x_e|<=1/4: {c_v:.4f} (claim <= 1/4);  '
      f'sup |v_K-(x1-x2)/4|/(|x1|+|x2|)^2 = {lead:.4f} (report 0.044)')
# |v_K| <= min(1/2, 8 K R / a_min) check
worst = 0
for trial in range(200000):
    a1, a2 = rng.uniform(0.2, 5, 2); amin = min(a1, a2)
    k1, k2 = rng.choice([-1, 1], 2) * 10**rng.uniform(-6, 3, 2); R = max(abs(k1), abs(k2))
    v = w12(zfrom(k1, a1), zfrom(k2, a2)) - 0.5
    worst = max(worst, abs(v)/min(0.5, 8*K*R/amin))
print(f'max |v_K| / min(1/2, 8KR/a_min) = {worst:.4f}  (claim <= 1)')
# limit checks: |z| >> K -> v_K -> 0 ;  |z| << K -> v_K -> unregulated v (real-contour race of z's)
z1, z2 = zfrom(1e-7, 1.0), zfrom(2e-7, 1.3)
print('strict-Glauber limit (|z|>>K): v_K =', w12(z1, z2) - 0.5)
z1, z2 = zfrom(1e5, 1.0), zfrom(3e5, 1.3)
print('gluon-pole limit (|z|<<K): w_K^[12] =', w12(z1, z2), ' race z1/(z1+z2) =', z1/(z1 + z2))
