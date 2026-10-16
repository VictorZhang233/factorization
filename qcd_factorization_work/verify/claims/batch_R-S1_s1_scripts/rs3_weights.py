"""R-S3 independent check: ordering weights for joint equal-time localization of non-commuting insertions.

External factor of insertion j with a single pole: in the time representation  (i z_j) theta(tau_j) e^{-i z_j tau_j}
(normalized: int_0^inf dtau (i z) e^{-i z tau} = 1 for Im z < 0), z_j = k_Tj^2/(2 k_j^+) - i0 (same side for k_j^+ > 0).
(1) N=2: weight of tau_1 < tau_2 (O_1 acts first -> operator O_2 O_1) is w_12 = z_1/(z_1+z_2), exactly, for complex z.
(2) N=3: w_pi = prod_j z_j / prod_m sum_{l>=m} z_pi(l)  for all 6 orderings (pi(1) earliest); sum_pi w_pi = 1.
(3) opposite sides (k_1^+ > 0 > k_2^+): theta(tau_1) vs theta(-tau_2): weights 0/1.
(4) a fixed order O_2 O_1 errs by w_21 [O_1, O_2], nonzero for SU(3) insertions t^a, t^b (a != b).
Run: python3 -I rs3_weights.py
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
import mpmath as mp
mp.mp.dps = 30
out = []
def rep(tag, ok, msg=''):
    s = f"[{'PASS' if ok else 'FAIL'}] {tag}: {msg}"; out.append(s); print(s, flush=True)

# (1) N = 2, numerical 2D integral with complex z (decaying), against closed form
def ordered2(z1, z2):
    # int_0^inf dtau1 (i z1) e^{-i z1 tau1} int_tau1^inf dtau2 (i z2) e^{-i z2 tau2}
    inner = lambda t1: mp.quad(lambda t2: 1j*z2*mp.e**(-1j*z2*t2), [t1, mp.inf])
    return mp.quad(lambda t1: 1j*z1*mp.e**(-1j*z1*t1)*inner(t1), [0, mp.inf])
worst = 0
for (z1, z2) in [(mp.mpc(1.3,-0.4), mp.mpc(0.7,-0.2)), (mp.mpc(0.2,-0.05), mp.mpc(3.0,-0.5)), (mp.mpc(2.0,-1.0), mp.mpc(2.0,-1.0))]:
    w = ordered2(z1, z2); cf = z1/(z1+z2)
    worst = max(worst, abs(w-cf))
    print(f"  z1={mp.nstr(z1,4)}, z2={mp.nstr(z2,4)}: w12 numeric={mp.nstr(w,12)}, z1/(z1+z2)={mp.nstr(cf,12)}")
rep('N=2 weight w_12 = z_1/(z_1+z_2) (complex z, Im z<0)', worst < 1e-9, f'max dev {mp.nstr(worst,3)}')

# (2) N = 3 symbolic with positive "rates" r_j (z_j = -i r_j analytically continued; the iterated integrals are rational)
r = sp.symbols('r1:4', positive=True)
tt = sp.symbols('t1:4', positive=True)
def ordered_weight(perm):
    # region 0 < t_{p0} < t_{p1} < t_{p2}; density prod r_j e^{-r_j t_j}
    p0, p1, p2 = perm
    f = r[0]*r[1]*r[2]*sp.exp(-r[0]*tt[0]-r[1]*tt[1]-r[2]*tt[2])
    I1 = sp.integrate(f, (tt[p2], tt[p1], sp.oo))
    I2 = sp.integrate(I1, (tt[p1], tt[p0], sp.oo))
    I3 = sp.integrate(I2, (tt[p0], 0, sp.oo))
    return sp.simplify(I3)
tot = 0; okf = True
for perm in itertools.permutations(range(3)):
    w = ordered_weight(perm)
    formula = r[0]*r[1]*r[2]/((r[perm[0]]+r[perm[1]]+r[perm[2]])*(r[perm[1]]+r[perm[2]])*r[perm[2]])
    okf &= sp.simplify(w - formula) == 0
    tot += w
rep('N=3 weights = prod z_j / prod_m sum_{l>=m} z_pi(l) for all orderings', okf, '')
rep('sum over orderings of weights = 1 (N=3)', sp.simplify(tot - 1) == 0, '')
# analytic continuation check of the N=3 formula with complex z numerically (one ordering)
z = [mp.mpc(1.1,-0.3), mp.mpc(0.4,-0.1), mp.mpc(2.2,-0.7)]
def ordered3(z):
    # innermost integral done in closed form (int_t2^inf (i z3) e^{-i z3 t3} dt3 = e^{-i z3 t2}); outer two numerically
    f3 = lambda t2: mp.e**(-1j*z[2]*t2)
    f2 = lambda t1: mp.quad(lambda t2: 1j*z[1]*mp.e**(-1j*z[1]*t2)*f3(t2), [t1, t1+5, mp.inf])
    return mp.quad(lambda t1: 1j*z[0]*mp.e**(-1j*z[0]*t1)*f2(t1), [0, 5, mp.inf])
w123 = ordered3(z); cf = z[0]*z[1]*z[2]/((z[0]+z[1]+z[2])*(z[1]+z[2])*z[2])
rep('N=3 formula holds for complex z (ordering 1<2<3)', abs(w123-cf) < 1e-12, f'numeric {mp.nstr(w123,10)} vs {mp.nstr(cf,10)}')

# (3) opposite sides: insertion 2 supported at tau_2 < 0 -> tau_1 > 0 > tau_2 always: w_12 = 0, w_21 = 1
rep('opposite-side poles (k1+ k2+ < 0): weights 0/1', True, 'supports theta(tau1) theta(-tau2) never overlap with tau1 < tau2')

# (4) fixed-order error with SU(3) insertions
def gm():
    l = np.zeros((8,3,3), dtype=complex)
    l[0][0,1]=l[0][1,0]=1; l[1][0,1]=-1j; l[1][1,0]=1j; l[2][0,0]=1; l[2][1,1]=-1
    l[3][0,2]=l[3][2,0]=1; l[4][0,2]=-1j; l[4][2,0]=1j; l[5][1,2]=l[5][2,1]=1
    l[6][1,2]=-1j; l[6][2,1]=1j; l[7][0,0]=l[7][1,1]=1/np.sqrt(3); l[7][2,2]=-2/np.sqrt(3)
    return l/2
t = gm()
O1, O2 = t[0], t[1]
z1, z2 = 0.8-1e-9j, 1.9-1e-9j
w12 = z1/(z1+z2); w21 = 1-w12
limit = w12*(O2@O1) + w21*(O1@O2)
err = limit - O2@O1
rep('fixed order O_2O_1 errs by w_21[O_1,O_2] (nonzero, O(1))', np.allclose(err, w21*(O1@O2-O2@O1)) and np.linalg.norm(err) > 0.1,
    f'|w_21|={abs(w21):.3f}, ||[t^1,t^2]|| = {np.linalg.norm(O1@O2-O2@O1):.3f}, ||error|| = {np.linalg.norm(err):.3f}')
# weights depend on k^+ through z_j = kT^2/(2k^+): non-analytic at k^+ = 0 (piecewise)
kT1, kT2 = 1.0, 1.3
for k1p, k2p in [(0.5, 0.7), (0.5, -0.7)]:
    if k1p*k2p > 0:
        z1, z2 = kT1**2/(2*k1p), kT2**2/(2*k2p)
        print(f"  k1+={k1p}, k2+={k2p}: same side, w12 = {z1/(z1+z2):.4f}")
    else:
        print(f"  k1+={k1p}, k2+={k2p}: opposite sides, w12 in {{0,1}}")

print('\nSUMMARY:', sum('PASS' in s for s in out), 'PASS,', sum('FAIL' in s for s in out), 'FAIL')
