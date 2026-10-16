r"""
W19 / Ch16 -- s1b_sw_thrustaxis.py : the constant of the O(alpha_s) cone-jet rate depends on the choice of
the cone axis (and on what is called delta).  Written as  sigma/sigma0 = 1 + (C_F as/4pi)(-16 ln delta ln beta - 12 ln delta + c0),
beta = 2 eps (eps = fraction of the total energy outside the cones), Becher-Neubert-Rothen-Shao (PRL 116
(2016) 192001) state c0 = 10 - 4pi^2/3 for the original Sterman-Weinberg jets (free axis) and
c0 = -2 + 12 ln 2 for cones around the thrust axis.  Independent check with the integrator of s1_sw_jets.py:
  K1  free axis:   c0(num) -> 10 - 4 pi^2/3   (from the s1 predicate);
  K2  thrust axis: c0(num) -> -2 + 12 ln 2    (new predicate: axis along the most energetic parton; as in BNRS
      a particle belongs to a jet iff n.p < delta^2 nbar.p, i.e. cone half-angle 2 arctan(delta) ~ 2 delta,
      so that delta plays the role of half the opening angle of a collinear pair, as in the SW definition).
Run:  python3 -I s1b_sw_thrustaxis.py
"""
import sys, os, math
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, 's1_sw_jets.py')).read()
head = src.split("print('== G: geometry")[0]
numdefs = src.split("print('== N: numerics ==')")[1].split("# reference: research/c_ee")[0]
ns = {}
exec(compile(head + numdefs, 's1defs', 'exec'), ns)

RES = []
def check(name, cond, info=''):
    RES.append((name, bool(cond)))
    print(('PASS  ' if cond else 'FAIL  ') + name + (('   [' + info + ']') if info else ''))

def atoms_thrust(x3, v, eps, dd):
    """atomic predicates for cones of half-angle dd around the thrust axis (= direction of the most energetic
    of the three partons, prop:jets-thrust-lo (c))"""
    x1 = 1 - x3 * (1 - v); x2 = 1 - x3 * v
    x3a = np.full(np.shape(v), x3)
    y12 = 1 - x3a; y13 = x3a * v; y23 = x3a * (1 - v)
    c12 = 1 - 2 * y12 / (x1 * x2); c13 = 1 - 2 * y13 / (x1 * x3a); c23 = 1 - 2 * y23 / (x2 * x3a)
    # BNRS: particle in the right (left) jet iff n.p < delta^2 nbar.p (nbar.p < delta^2 n.p), i.e. its angle to
    # the thrust axis (anti-axis) is below 2 arctan(delta) ~ 2 delta: the cone half-angle is 2 arctan(delta)
    cd = math.cos(2 * math.atan(dd))
    A = {}
    A['M1'] = (x1 >= x2) & (x1 >= x3a); A['M2'] = (x2 > x1) & (x2 >= x3a); A['M3'] = ~(A['M1'] | A['M2'])
    # parton i inside the cone pair around the axis along parton m: theta_im <= d or pi - theta_im <= d
    for (i, m, c) in [(1, 2, c12), (2, 1, c12), (1, 3, c13), (3, 1, c13), (2, 3, c23), (3, 2, c23)]:
        A['in%d_%d' % (i, m)] = (c >= cd) | (c <= -cd)
    A['E1'] = x1 < 2 * eps; A['E2'] = x2 < 2 * eps; A['E3'] = x3a < 2 * eps
    return A

def threejet_thrust(x3, v, eps, dd):
    A = atoms_thrust(x3, v, eps, dd)
    two = np.zeros(np.shape(v), dtype=bool)
    for m, (i, j) in [(1, (2, 3)), (2, (1, 3)), (3, (1, 2))]:
        ii, jj = A['in%d_%d' % (i, m)], A['in%d_%d' % (j, m)]
        ok = (ii & jj) | (ii & A['E%d' % j]) | (jj & A['E%d' % i])
        two |= A['M%d' % m] & ok
    return ~two

def c0_from(eps, delta, I3):
    c2 = 0.75 - I3 / 2
    beta = 2 * eps
    return 4 * c2 + 16 * math.log(delta) * math.log(beta) + 12 * math.log(delta)

pts = [(1e-4, 0.01), (1e-5, 0.01), (1e-6, 0.003)]
c0_free = 10 - 4 * math.pi ** 2 / 3
c0_thr = -2 + 12 * math.log(2)
print('  free-axis (Sterman-Weinberg) cones:')
free = []
for e, dl in pts:
    I3 = ns['I3jet_num'](e, dl)
    free.append(c0_from(e, dl, I3))
    print('    eps=%7.0e delta=%6.3f  I3j=%.8f  c0(num)=%.5f   (10-4pi^2/3 = %.5f)' % (e, dl, I3, free[-1], c0_free))
check('K1  free axis: c0 -> 10 - 4pi^2/3 (|diff| < 5e-3 at the smallest point)', abs(free[-1] - c0_free) < 5e-3)
ns['atoms'] = atoms_thrust
ns['threejet_mask'] = threejet_thrust
print('  thrust-axis cones:')
thr = []
for e, dl in pts:
    I3 = ns['I3jet_num'](e, dl)
    thr.append(c0_from(e, dl, I3))
    print('    eps=%7.0e delta=%6.3f  I3j=%.8f  c0(num)=%.5f   (-2+12 ln2 = %.5f)' % (e, dl, I3, thr[-1], c0_thr))
check('K2  thrust axis: c0 -> -2 + 12 ln 2 (|diff| < 5e-3 at the smallest point)', abs(thr[-1] - c0_thr) < 5e-3)
print()
print('SUMMARY: %d/%d checks passed' % (sum(p for _, p in RES), len(RES)))
