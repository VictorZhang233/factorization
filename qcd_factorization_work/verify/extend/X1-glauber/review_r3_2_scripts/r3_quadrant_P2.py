# Round-3 reviewer 2 -- independent checks of (1) the closed-quadrant lemma of L1(b1),
# (2) P2(b): strict-Glauber weights w_12 = 1/2 + i*delta and p_opp = 1/2 + 2 delta_A delta_B,
# (3) the 97/105 example, computed (a) by the PV/residue formula and (b) by the L1' regulator-pole race.
import sys, os, itertools, math, cmath
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np, sympy as sp
rng = np.random.default_rng(20261011)

def race_weight(order, z):
    # w = prod_m z_{pi(m)} / sum_{l>=m} z_{pi(l)}  (final-group convention; initial group identical form)
    w = 1.0 + 0j
    for m in range(len(order)):
        w *= z[order[m]] / sum(z[order[l]] for l in range(m, len(order)))
    return w

print('--- (1) closed-quadrant lemma ---')
worst = 0.0
for trial in range(20000):
    n = rng.integers(2, 6)
    phi0 = rng.uniform(0, 2*np.pi)
    ang = phi0 + rng.uniform(0, np.pi/2, n)        # all in one closed cone of opening pi/2
    ang[0] = phi0; ang[-1] = phi0 + np.pi/2        # force both edges to be occupied
    z = rng.uniform(0.01, 10, n) * np.exp(1j*ang)
    for order in itertools.permutations(range(n)):
        worst = max(worst, abs(race_weight(order, z)))
print('max |w| over 20000 random closed-quadrant groups (edges occupied):', worst, '-> PASS' if worst <= 1 + 1e-12 else '-> FAIL')
# sharpness: opening slightly larger than pi/2 allows |w| > 1
z = np.array([1.0, 0.3*np.exp(1j*(np.pi/2 + 0.3))])
print('opening pi/2+0.3, z=(1, 0.3 e^{i(pi/2+0.3)}): |w_(0,1)| =', abs(race_weight((0, 1), z)), '(>1: the closed-quadrant condition cannot be relaxed)')
# sum_sigma |w_sigma| <= n! in closed quadrant, and = 1 for same-ray (Glauber) case
z = rng.uniform(0.1, 3, 4)*np.exp(-1j*np.pi/4)
print('same-ray group: sum_w =', sum(race_weight(o, z) for o in itertools.permutations(range(4))), ' sum|w| =', sum(abs(race_weight(o, z)) for o in itertools.permutations(range(4))))

print('--- (2) P2(b): sharp windows, delta formula vs direct 1D principal-value integral ---')
def delta_sharp(K1, K2, K1p, K2p):
    return math.log(min(K2, K1p)/min(K1, K2p))/(2*math.pi)
for (K1, K2, K1p, K2p) in [(1, 3, 4, 0.5), (2, 2, 2, 2), (1, 5, 0.3, 7), (0.2, 0.9, 3, 1.1)]:
    a, b = min(K1, K2p), min(K2, K1p)    # support of chi1(k) chi2(-k) is [-a, b]
    pv = math.log(b/a)                   # PV int_{-a}^{b} dk/k
    print(f'  windows ({K1},{K2};{K1p},{K2p}): delta formula {delta_sharp(K1,K2,K1p,K2p):+.6f}, PV/(2pi) {pv/(2*math.pi):+.6f}')
# identity p_opp = 1/2 + 2 dA dB from factorized strict weights (w12 = 1/2 + i dA, w21 = 1/2 - i dA, same for B)
for dA, dB in [(0.3, -0.7), (0.5, 0.5), (-0.5, 0.5), (1.2, 0.9)]:
    wA12, wA21 = 0.5 + 1j*dA, 0.5 - 1j*dA
    wB12, wB21 = 0.5 + 1j*dB, 0.5 - 1j*dB
    popp_crossed = wA12*wB21 + wA21*wB12      # one convention for which B order is 'opposite'
    print(f'  dA={dA:+.2f} dB={dB:+.2f}: wA12*wB21+wA21*wB12 = {popp_crossed:.6f}  vs 1/2+2dAdB = {0.5+2*dA*dB:.6f}')

print('--- (3) the 97/105 example: chi_e(k) = K1 K2/((K1+ik)(K2-ik)), (K1,K2;K1p,K2p) = (1,3;4,1/2) ---')
k = sp.symbols('k')
def chi(K1, K2, x): return K1*K2/((K1 + sp.I*x)*(K2 - sp.I*x))
K1, K2, K1p, K2p = sp.Integer(1), sp.Integer(3), sp.Integer(4), sp.Rational(1, 2)
f = chi(K1, K2, k)*chi(K1p, K2p, -k)*sp.I/k        # the i0 of i/(k+i0) puts its pole in the LHP
uhp = [p for p in sp.solve(sp.denom(sp.together(f)), k) if sp.im(p) > 0]
val = sp.I*sum(sp.residue(f, k, p) for p in uhp)  # int dk/(2pi) f = i * sum of UHP residues
print('  UHP poles:', uhp, ' w12 (residues) =', sp.nsimplify(sp.simplify(val)))
# (b) L1' regulator-pole race: per line, u(initial pole iK1) = K2/(K1+K2), u(final pole -iK2) = K1/(K1+K2)
def lines(K1, K2): return [('I', sp.I*K1, K2/(K1+K2)), ('F', -sp.I*K2, K1/(K1+K2))]
w12 = 0
for (g1, p1, u1), (g2, p2, u2) in itertools.product(lines(K1, K2), lines(K1p, K2p)):
    if g1 == 'I' and g2 == 'I':   w = p2/(p1 + p2)      # BB order (1,2): K^B_1 = p1, K^B_2 = p1+p2 -> w = p2/(p1+p2)
    elif g1 == 'F' and g2 == 'F': w = p1/(p1 + p2)      # FF order (1,2): K^F_1 = p1+p2, K^F_2 = p2 -> w = p1/(p1+p2)
    elif g1 == 'I' and g2 == 'F': w = 1                 # sector 1V2 has colour order [12]
    else:                         w = 0                 # sector 2V1 has colour order [21]
    w12 += u1*u2*w
print('  w12 (L1prime race) =', sp.nsimplify(sp.simplify(w12)), ' target 97/105 =', sp.Rational(97, 105))
# (c) PV form 1/2 + i delta with delta = (1/2pi) PV int chi1(k) chi2(-k) dk/k
g = sp.lambdify(k, chi(K1, K2, k)*chi(K1p, K2p, -k), 'numpy')
xs = np.linspace(1e-7, 4000, 4_000_001)
pv = np.trapezoid(((g(xs) - g(-xs))/xs), xs)            # PV int_{-X}^{X} = int_0^X [f(x)-f(-x)]/x dx
print('  1/2 + i*PV/(2pi) =', 0.5 + 1j*pv/(2*np.pi), ' (tail beyond 4000 is O(1e-12))')
