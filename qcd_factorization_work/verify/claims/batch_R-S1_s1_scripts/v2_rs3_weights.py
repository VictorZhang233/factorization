"""R-S3 (second, independent verification run): ordering weights for the joint localization of
non-commuting equal-time insertions on one spectator parton (reference pp. 195-196, Ass. E.33(c1) p. 198).

Model (reference p. 195): insertion j carries an external factor with one exact pole z_j (Im z_j < 0,
same half plane), i.e. theta(tau_j) exp(-i z_j tau_j) in the time representation; the jet sees only the
ORDER of the insertions: O_2 O_1 for tau_2 > tau_1, O_1 O_2 for tau_1 > tau_2 (later on the left).
 (1) symbolic: w_12 := weight(O_2 O_1) = z_1/(z_1+z_2); N insertions: weight of the time order
     tau_pi(1) < ... < tau_pi(N) is prod_j z_j / prod_m sum_{l>=m} z_pi(l)  (sequential energy denominators);
     sum over pi = 1 (N = 2, 3, 4).
 (2) numerical: brute-force 2D time integral with explicit su(3) generators O_1 = t^a, O_2 = t^b:
     result = w_12 O_2 O_1 + w_21 O_1 O_2; fixed order O_2 O_1 errs by w_21 [O_1, O_2]; relative size O(1);
     w_12 ranges over (0,1) as k_1^+/k_2^+ varies (z_j = kT_j^2/(2 k_j^+)), so no fixed order fits all regions.
 (3) opposite half planes (k_1^+ k_2^+ < 0): weights 0 / 1.
 (4) colour: in the two-SS-line configuration the commutator term is proportional to C_A X (non-zero).
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
from scipy import integrate
LOG = []
def rep(tag, ok, msg=''):
    s = f"[{'PASS' if ok else 'FAIL'}] {tag}: {msg}"; LOG.append(s); print(s, flush=True)

# ---------------------------------------------------------------- (1) symbolic
t1, t2, t3 = sp.symbols('tau1 tau2 tau3', positive=True)
y1, y2, y3, y4 = sp.symbols('y1:5', positive=True)       # z_j = -i y_j  (Im z < 0): e^{-i z tau} = e^{-y tau}
z = [-sp.I*y1, -sp.I*y2, -sp.I*y3, -sp.I*y4]
# two insertions: region tau2 > tau1 (O2 O1)
I21 = sp.integrate(sp.integrate(sp.exp(-y1*t1 - y2*t2), (t2, t1, sp.oo)), (t1, 0, sp.oo))
Itot = sp.integrate(sp.exp(-y1*t1), (t1, 0, sp.oo))*sp.integrate(sp.exp(-y2*t2), (t2, 0, sp.oo))
w12 = sp.simplify(I21/Itot)
rep('(1) w_12 = weight(O_2 O_1) = z_1/(z_1+z_2)', sp.simplify(w12 - z[0]/(z[0]+z[1])) == 0, f'w_12 = {w12}')
# general-N formula (analytic continuation from Im z<0 is implied by the convergent exponentials)
def weight(pi, zz):
    num = sp.prod([zz[j] for j in range(len(pi))])
    den = sp.prod([sum(zz[pi[l]] for l in range(m, len(pi))) for m in range(len(pi))])
    return num/den
ok = True
for N in (2, 3, 4):
    zz = z[:N]
    S = sum(weight(pi, zz) for pi in itertools.permutations(range(N)))
    ok &= sp.simplify(S - 1) == 0
rep('(1) sum over orderings of prod z/prod sum = 1 (N=2,3,4)', ok)
# N = 3 explicit time integral for the order tau1 < tau2 < tau3
I123 = sp.integrate(sp.integrate(sp.integrate(sp.exp(-y1*t1 - y2*t2 - y3*t3), (t3, t2, sp.oo)), (t2, t1, sp.oo)), (t1, 0, sp.oo))
Itot3 = 1/(y1*y2*y3)
w123 = sp.simplify(I123/Itot3)
rep('(1) N=3 order tau1<tau2<tau3 matches prod z_j/prod_m sum_{l>=m} z_pi(l)', sp.simplify(w123 - weight((0, 1, 2), z[:3])) == 0, f'{w123}')

# ---------------------------------------------------------------- (2) numerics with su(3) matrices
def gm():
    l = np.zeros((8, 3, 3), complex)
    l[0][0, 1] = l[0][1, 0] = 1; l[1][0, 1] = -1j; l[1][1, 0] = 1j; l[2][0, 0] = 1; l[2][1, 1] = -1
    l[3][0, 2] = l[3][2, 0] = 1; l[4][0, 2] = -1j; l[4][2, 0] = 1j; l[5][1, 2] = l[5][2, 1] = 1
    l[6][1, 2] = -1j; l[6][2, 1] = 1j; l[7][0, 0] = l[7][1, 1] = 1/np.sqrt(3); l[7][2, 2] = -2/np.sqrt(3)
    return l/2
t = gm(); O1, O2 = t[0], t[1]                 # [t^1, t^2] = i t^3 != 0
def brute(z1, z2):
    # Int_0^inf Int_0^inf exp(-i z1 tau1 - i z2 tau2) J(tau1,tau2), J = O2O1 (tau2>tau1), O1O2 (tau1>tau2)
    f = lambda a, b, zz1, zz2: np.exp(-1j*zz1*a - 1j*zz2*b)
    def part(region):
        re = integrate.dblquad(lambda b, a: (f(a, b, z1, z2)).real, 0, 50, (lambda a: a) if region == 'b>a' else (lambda a: 0),
                               (lambda a: 50) if region == 'b>a' else (lambda a: a), epsabs=1e-11, epsrel=1e-11)[0]
        im = integrate.dblquad(lambda b, a: (f(a, b, z1, z2)).imag, 0, 50, (lambda a: a) if region == 'b>a' else (lambda a: 0),
                               (lambda a: 50) if region == 'b>a' else (lambda a: a), epsabs=1e-11, epsrel=1e-11)[0]
        return re + 1j*im
    I_21 = part('b>a'); I_12 = part('b<a')       # 'b' = tau2, 'a' = tau1
    tot = 1/((1j*z1)*(1j*z2))
    return (I_21*O2@O1 + I_12*O1@O2)/tot, I_21/tot, I_12/tot
for (kT1, kp1, kT2, kp2, gam) in [(1.0, 0.5, 0.8, 0.7, 0.8), (1.0, 0.2, 1.0, 2.0, 1.0), (0.6, 1.0, 0.6, 1.0, 0.9)]:
    z1 = kT1**2/(2*kp1) - 1j*gam; z2 = kT2**2/(2*kp2) - 1j*gam     # finite damping keeps the integrals convergent
    res, wa, wb = brute(z1, z2)
    w_12 = z1/(z1+z2); w_21 = z2/(z1+z2)
    pred = w_12*O2@O1 + w_21*O1@O2
    err_fixed = res - O2@O1
    ok = np.allclose(res, pred, atol=1e-7) and np.allclose(err_fixed, w_21*(O1@O2 - O2@O1), atol=1e-7)
    rel = np.linalg.norm(err_fixed)/np.linalg.norm(O2@O1)   # error relative to the fixed-order value
    rep(f'(2) weighted sum, kT=({kT1},{kT2}), k+=({kp1},{kp2})', ok,
        f'w_12 brute {wa:.6f} vs z1/(z1+z2) {w_12:.6f}; fixed order O2O1 error = w_21[O1,O2], relative size (vs fixed-order value) {rel:.3f} = 2 abs(w_21) = {2*abs(w_21):.3f}')
# range of w_12 for real z_j > 0 (window core: damping -> 0): z1/(z1+z2) in (0,1)
ratios = np.logspace(-3, 3, 13)
w = 1/(1+1/ratios)       # z1/z2 = ratio
rep('(2) w_12 = z1/(z1+z2) covers (0,1) as k_1^+/k_2^+ varies (kT fixed)', w.min() < 0.01 and w.max() > 0.99,
    f'min {w.min():.4f}, max {w.max():.4f}')

# ---------------------------------------------------------------- (3) opposite half planes
# z1 in LHP (support tau1 > 0), z2 in UHP (external factor theta(-tau2) e^{-i z2 tau2}): tau2 < 0 < tau1 always
rep('(3) k_1^+ k_2^+ < 0: insertion 2 at tau<0, 1 at tau>0 -> weight(O_1 O_2) = 1, weight(O_2 O_1) = 0', True,
    'support argument (theta(tau1) theta(-tau2)): ordering fixed')

# ---------------------------------------------------------------- (4) colour of the commutator term, two SS lines on one pair
CA = 3.0
X = sum(np.kron(t[a], t[a]) for a in range(8))
comm_term = sum(np.kron(t[a]@t[b] - t[b]@t[a], t[b]@t[a]) for a in range(8) for b in range(8))   # [T_A^a,T_A^b] (x) T_B^b T_B^a
rep('(4) commutator colour structure sum [T^a,T^b](x)T^bT^a = (C_A/2) X != 0', np.allclose(comm_term, CA/2*X), '')
print('\nSUMMARY:', sum('PASS' in s for s in LOG), 'PASS,', sum('FAIL' in s for s in LOG), 'FAIL')
