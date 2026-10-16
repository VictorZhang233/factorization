"""
W10 / Ch9 sec:method-regions, sec:method-subtraction -- region poset, meets, neighbourhood exponents, chain expansion,
pairing decomposition, product formula, telescoping identity, covering.

 (1) two-loop planar vertex: the nine leading regions as per-line mode assignments on the six internal lines
     L1=k1, L2=k2, L3=p1-k2, L4=p1-k1-k2, L5=p2+k2, L6=p2+k1+k2 (modes S<A,B<H, A^B=S);
     per-line order, meet closure, the 12 covering relations of fig:method-hasse, the examples of meets printed in the
     caption, heights h(R) and beta_R = 3^{h(R)-h*} (1/81, 1/27, 1/9, 1/3), beta_R >= 3 beta_R' for R' < R != Rmax;
     pinch sets as affine subspaces of (k1,k2) in R^8 (massless limit, p1 ~ nA, p2 ~ nB):
     pi_{R^R'} = pi_R cap pi_R' (lem:method-meets) for all 81 pairs; pi_R' subset pi_R for R' <= R.
 (2) chain expansion (prop:method-chains) and pairing decomposition (lem:method-pairing) for ARBITRARY linear maps
     (random non-commuting matrices) on the nine-element poset -- both are identities without (Com)/(Abs).
 (3) product formula (prop:method-product) for commuting idempotent coordinate zeroings satisfying (Abs),
     including the (CS2) equivalence C_R Gamma = G_{R0}(R) for R incomparable with R0.
 (4) telescoping identity (lem:method-telescoping), symbolic, n <= 5.
 (5) covering (lem:method-covering) on the off-shell triangle with the neighbourhoods of def:method-neighbourhoods.
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp

npass = 0; nfail = 0
def check(name, ok, info=''):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(('[PASS] ' if ok else '[FAIL] ') + name + ((' : ' + str(info)) if info != '' else ''))

# ---------------------------------------------------------------- (1) modes and regions
LE = {('S', 'S'), ('S', 'A'), ('S', 'B'), ('S', 'H'), ('A', 'A'), ('A', 'H'), ('B', 'B'), ('B', 'H'), ('H', 'H')}
def le(x, y): return (x, y) in LE
def meet1(x, y):
    if le(x, y): return x
    if le(y, x): return y
    return 'S'          # A ^ B = S
REG = {  # per-line modes (L1..L6)
    'HH': 'HHHHHH', 'HA': 'HAAHHH', 'HB': 'HBHHBH', 'AA': 'AAAAHH', 'BB': 'BBHHBB',
    'HS': 'HSAHBH', 'AS': 'ASAABH', 'BS': 'BSAHBB', 'SS': 'SSAABB'}
names = list(REG)
def leR(r, s): return all(le(a, b) for a, b in zip(REG[r], REG[s]))
def meetR(r, s):
    m = ''.join(meet1(a, b) for a, b in zip(REG[r], REG[s]))
    for n, v in REG.items():
        if v == m: return n
    return None
closed = all(meetR(r, s) is not None for r in names for s in names)
check('(1) the nine leading regions are closed under per-line meets', closed)
check('(1) caption meets: (C1,C1)^(H,S)=(C1,S), (H,C1)^(H,C2)=(H,S), (C1,C1)^(C2,C2)=(S,S)',
      meetR('AA', 'HS') == 'AS' and meetR('HA', 'HB') == 'HS' and meetR('AA', 'BB') == 'SS')
lt = {(r, s) for r in names for s in names if r != s and leR(r, s)}
cover = {(r, s) for (r, s) in lt if not any((r, t) in lt and (t, s) in lt for t in names)}
expected = {('SS', 'AS'), ('SS', 'BS'), ('AS', 'AA'), ('AS', 'HS'), ('BS', 'BB'), ('BS', 'HS'), ('HS', 'HA'),
            ('HS', 'HB'), ('AA', 'HA'), ('BB', 'HB'), ('HA', 'HH'), ('HB', 'HH')}
check('(1) Hasse diagram: exactly the 12 covering relations of fig:method-hasse', cover == expected, len(cover))
check('(1) the non-obvious relation (C1,C1) < (H,C1) holds', ('AA', 'HA') in lt)
def height(r):
    below = [s for s in names if (s, r) in lt]
    return 0 if not below else 1 + max(height(s) for s in below)
h = {r: height(r) for r in names}
hstar = 1 + max(h[r] for r in names if r != 'HH')
beta = {r: sp.Rational(1, 3**(hstar - h[r])) for r in names if r != 'HH'}
check('(1) heights and beta_R = 3^{h-h*}: SS 1/81, C_iS 1/27, C_iC_i = HS 1/9, HC_i 1/3',
      beta['SS'] == sp.Rational(1, 81) and beta['AS'] == beta['BS'] == sp.Rational(1, 27)
      and beta['AA'] == beta['BB'] == beta['HS'] == sp.Rational(1, 9) and beta['HA'] == beta['HB'] == sp.Rational(1, 3),
      {r: str(beta[r]) for r in beta})
check('(1) beta_R <= 1/3 and beta_R >= 3 beta_R\' for R\' < R != Rmax',
      all(beta[r] <= sp.Rational(1, 3) for r in beta) and all(beta[s] >= 3*beta[r] for (r, s) in lt if s != 'HH'))

# pinch sets as affine subspaces in (k1, k2) in R^8; light-cone components (+,-,x,y); p1 = (1,0,0,0), p2 = (0,1,0,0)
p1 = np.array([1.0, 0, 0, 0]); p2 = np.array([0, 1.0, 0, 0])
LINES = [(np.array([1, 0]), np.zeros(4)), (np.array([0, 1]), np.zeros(4)), (np.array([0, -1]), p1),
         (np.array([-1, -1]), p1), (np.array([0, 1]), p2), (np.array([1, 1]), p2)]   # l = c1 k1 + c2 k2 + const
def constraints(r):
    rows = []; rhs = []
    for (c, const), mode in zip(LINES, REG[r]):
        comps = {'S': [0, 1, 2, 3], 'A': [1, 2, 3], 'B': [0, 2, 3], 'H': []}[mode]
        for comp in comps:
            row = np.zeros(8); row[comp] = c[0]; row[4 + comp] = c[1]
            rows.append(row); rhs.append(-const[comp])
    return (np.array(rows).reshape(-1, 8), np.array(rhs))
def affine(r_list):
    A = np.vstack([constraints(r)[0] for r in r_list if constraints(r)[0].size] or [np.zeros((0, 8))])
    b = np.concatenate([constraints(r)[1] for r in r_list])
    if A.size == 0: return (True, 8, None, None)
    x, res, rank, sv = np.linalg.lstsq(A, b, rcond=None)
    ok = np.linalg.norm(A @ x - b) < 1e-9
    return (ok, 8 - np.linalg.matrix_rank(A), A, b)
good = True; empty_pairs = 0
for r in names:
    for s in names:
        m = meetR(r, s)
        e1, d1, A1, b1 = affine([r, s])     # pi_R cap pi_S
        e2, d2, A2, b2 = affine([m])        # pi_{R^S}
        if e1 != e2: good = False
        if e1 and e2:
            # same affine subspace: same dimension and every solution of one solves the other
            if d1 != d2: good = False
            x = np.linalg.lstsq(A2, b2, rcond=None)[0] if A2 is not None else np.zeros(8)
            if A1 is not None and np.linalg.norm(A1 @ x - b1) > 1e-9: good = False
        if not e1: empty_pairs += 1
check('(1) lem:method-meets: pi_{R^R\'} = pi_R cap pi_R\' for all 81 pairs (affine subspaces)', good,
      'empty intersections: %d' % empty_pairs)
check('(1) R\' <= R  =>  pi_R\' subset pi_R', all(affine([r, s])[1] == affine([r])[1] for (r, s) in lt))
check('(1) every leading pinch set is non-empty', all(affine([r])[0] for r in names))
print('    dims of pinch sets:', {r: affine([r])[1] for r in names})

# ---------------------------------------------------------------- (2) chains and pairing for arbitrary linear maps
rng = np.random.default_rng(7)
n = 6
T = {r: rng.normal(size=(n, n)) / 2 for r in names}
Gam = rng.normal(size=n)
order = sorted(names, key=lambda r: h[r])
C = {}
for r in order:
    acc = Gam.copy()
    for s in names:
        if (s, r) in lt: acc = acc - C[s]
    C[r] = T[r] @ acc
def chains(P):
    """all chains in the subset P (as lists sorted decreasingly = largest first)"""
    out = [[]]
    P = list(P)
    for k in range(1, len(P) + 1):
        for comb in itertools.combinations(P, k):
            if all((a, b) in lt or (b, a) in lt for a, b in itertools.combinations(comb, 2)):
                out.append(sorted(comb, key=lambda r: -h[r]))
    return out
def Tc(c, v):
    w = v.copy()
    for r in reversed(c):        # largest leftmost = acts last
        w = T[r] @ w
    return w
def O(P, v):
    return sum(((-1)**len(c)) * Tc(c, v) for c in chains(P))
ok = True
for r in names:
    s = sum(((-1)**(len(c) - 1)) * Tc(c, Gam) for c in chains(names) if c and c[0] == r)
    ok &= np.allclose(s, C[r])
check('(2) prop:method-chains: C_R Gamma = sum_{chains, max c = R} (-1)^{|c|-1} T_c Gamma (random matrices)', ok)
X = {r: Gam - sum((C[s] for s in names if (s, r) in lt), np.zeros(n)) for r in names}
check('(2) X_R0 = O_{down R0} Gamma for all R0', all(np.allclose(X[r], O([s for s in names if (s, r) in lt], Gam)) for r in names))
rem = Gam - sum(C.values())
check('(2) r = O_{whole poset} Gamma', np.allclose(rem, O(names, Gam)))
# pairing decomposition
okp = True
for R0 in names:
    up = lambda R: [s for s in names if (R, s) in lt]
    inc = [R for R in names if R != R0 and (R, R0) not in lt and (R0, R) not in lt]
    Ip = [R for R in inc if affine([R, R0])[0]]
    Ipp = [R for R in inc if not affine([R, R0])[0]]
    rhs = O(up(R0), (np.eye(n) - T[R0]) @ X[R0])
    for R in Ip:
        Rw = meetR(R, R0)
        rhs = rhs - O(up(R), T[R] @ ((np.eye(n) - T[Rw]) @ X[Rw]))
    for R in Ipp:
        rhs = rhs - O(up(R), T[R] @ Gam)
    okp &= np.allclose(rhs, rem)
check('(2) lem:method-pairing holds for every R0 (arbitrary linear maps, meet-closed poset)', okp)
print('    (here every pair of pinch sets intersects, so I\'\' is empty; the I\'\' branch is exercised in the triangle-free test below)')

# a poset with disjoint pinch sets: two incomparable regions with no common lower bound (I'' non-empty)
# abstract test: regions {a, b, top}, a, b incomparable and minimal, no meet; pairing with R0 = a: I'' = {b}
names2 = ['a', 'b', 'top']; lt2 = {('a', 'top'), ('b', 'top')}
T2 = {r: rng.normal(size=(n, n)) / 2 for r in names2}
C2 = {}
for r in ['a', 'b', 'top']:
    acc = Gam.copy()
    for s in names2:
        if (s, r) in lt2: acc = acc - C2[s]
    C2[r] = T2[r] @ acc
rem2 = Gam - sum(C2.values())
X2a = Gam
rhs2 = (np.eye(n) - T2['top']) @ ((np.eye(n) - T2['a']) @ X2a) - (np.eye(n) - T2['top']) @ (T2['b'] @ Gam)
check('(2) pairing with I\'\' non-empty (two minimal regions without common lower bound)', np.allclose(rhs2, rem2))

# ---------------------------------------------------------------- (3) product formula for coordinate zeroings with (Abs)
# coordinates: (line, component); a region zeroes the small components of each line in its mode
SMALL = {'S': ('p', 'm', 'T'), 'A': ('m', 'T'), 'B': ('p', 'T'), 'H': ()}
coords = [(j, c) for j in range(6) for c in ('p', 'm', 'T')]
sym = {xc: sp.Symbol('x_%d%s' % xc) for xc in coords}
Z = {r: {(j, c) for j, mode in enumerate(REG[r]) for c in SMALL[mode]} for r in names}
check('(3) (Abs) for per-line meets in the zeroing model: Z_{R^R\'} subset Z_R cup Z_R\'',
      all(Z[meetR(r, s)] <= (Z[r] | Z[s]) for r in names for s in names))
xs = [sym[c] for c in coords]
test = sum(sp.Rational(int(rng.integers(1, 9)), int(rng.integers(1, 9))) * sp.prod(rng.choice(xs, 3)) for _ in range(12)) \
       + sum(sp.Rational(int(rng.integers(1, 9)), 7) * xx for xx in xs) + 1
def Tz(r, F): return F.subs({sym[c]: 0 for c in Z[r]}, simultaneous=True)
Cz = {}
for r in order:
    acc = test - sum((Cz[s] for s in names if (s, r) in lt), 0)
    Cz[r] = sp.expand(Tz(r, acc))
okz = True
for r in names:
    F = test
    for s in names:
        if (s, r) in lt: F = sp.expand(F - Tz(s, F))
    okz &= sp.expand(Tz(r, F) - Cz[r]) == 0
check('(3) prop:method-product: C_R Gamma = T_R prod_{R\'<R}(1-T_R\') Gamma', okz)
Fall = test
for s in names: Fall = sp.expand(Fall - Tz(s, Fall))
check('(3) prop:method-product: r = prod_R (1-T_R) Gamma', sp.expand(test - sum(Cz.values()) - Fall) == 0)
okg = True
for R0 in names:
    for R in names:
        if R == R0 or (R, R0) in lt or (R0, R) in lt: continue
        F = test
        for s in set([s for s in names if (s, R) in lt] + [R0]): F = sp.expand(F - Tz(s, F))
        okg &= sp.expand(Tz(R, F) - Cz[R]) == 0
check('(3) (CS2) equivalence: C_R Gamma = G_R0(R) for every R incomparable with R0', okg)
# a model where (Abs) fails: enlarge one zeroing set so that Z_{R^R'} is not contained in Z_R cup Z_R'
Zbad = dict(Z); Zbad['AS'] = Z['AS'] | {(5, 'p'), (5, 'm'), (5, 'T')}
viol = [(r, s) for r in names for s in names if not (Zbad[meetR(r, s)] <= (Zbad[r] | Zbad[s]))]
def Tb(r, F): return F.subs({sym[c]: 0 for c in Zbad[r]}, simultaneous=True)
Cb = {}
for r in order:
    acc = test - sum((Cb[s] for s in names if (s, r) in lt), 0)
    Cb[r] = sp.expand(Tb(r, acc))
diff = []
for r in names:
    F = test
    for s in names:
        if (s, r) in lt: F = sp.expand(F - Tb(s, F))
    if sp.expand(Tb(r, F) - Cb[r]) != 0: diff.append(r)
Fb = test
for s in names: Fb = sp.expand(Fb - Tb(s, Fb))
rdiff = sp.expand(test - sum(Cb.values()) - Fb) != 0
check('(3) control: an (Abs)-violating zeroing set (pairs %s...) breaks the product formula' % viol[:2],
      len(viol) > 0 and (len(diff) > 0 or rdiff), 'C_R differing for %s; r differs: %s' % (diff, rdiff))

# ---------------------------------------------------------------- (4) telescoping identity
okt = True
for nn in range(1, 6):
    f = sp.symbols('f1:%d' % (nn + 1)); g = sp.symbols('g1:%d' % (nn + 1))   # g_i = T f_i
    lhs = sp.prod(f) - sp.prod(g)
    rhs = sum(sp.prod(g[:i]) * (f[i] - g[i]) * sp.prod(f[i + 1:]) for i in range(nn))
    okt &= sp.expand(lhs - rhs) == 0
check('(4) lem:method-telescoping: (1-T) prod f_i = sum_i [prod_{j<i} T f_j](f_i - T f_i)[prod_{j>i} f_j], n<=5', okt)

# ---------------------------------------------------------------- (5) covering for the triangle
lam = 1e-2
bS, bC = 1/9, 1/3
def in_N(region, k):
    kp, km, kT = k
    if region == 'S': return abs(kp) + abs(km) + abs(kT) <= lam**bS
    if region == 'C1': return abs(km) + abs(kT) <= lam**bC      # k || p1 (large plus component)
    if region == 'C2': return abs(kp) + abs(kT) <= lam**bC
    return True
def U(region, k):
    smaller = {'S': [], 'C1': ['S'], 'C2': ['S'], 'H': ['S', 'C1', 'C2']}[region]
    return in_N(region, k) and not any(in_N(s, k) for s in smaller)
pts = np.concatenate([rng.normal(size=(20000, 3)) * sc for sc in (1e-4, 1e-2, 1, 10)])
cov = all(any(U(R, k) for R in ('S', 'C1', 'C2', 'H')) for k in pts)
check('(5) lem:method-covering on the triangle: U_S, U_C1, U_C2, U_H cover k-space (80000 random points)', cov)
print('\n=== w10_poset: %d PASS, %d FAIL ===' % (npass, nfail))
