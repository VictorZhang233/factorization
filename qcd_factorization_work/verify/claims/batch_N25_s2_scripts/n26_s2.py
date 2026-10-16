#!/usr/bin/env python3
"""N26 (stage-2 verifier): eikonal identity at finite regulator.
 sum_{perms} prod_j i/(a_{p1}+...+a_{pj} + i eta_j) =?= prod_j i/(a_j + i eps)
Methods (different from project s2 and from stage 1, which used numerical ordered multiple integrals):
 (1) exact symbolic identities for m = 2..4 (adiabatic, future-pointing, general additive per-gluon dampings)
 (2) necessity: arbitrary subset-dependent shifts eta(S); exactness <=> eta additive (m=2 symbolic, m=3 symbolic)
 (3) the uniform prescription = ordered integral damped only at the farthest attachment (exact sympy integrals)
 (4) distributional limit: EXACT closed form of the pairing of the m=2 uniform-eps defect with a Lorentzian test
     function (residues), = pi^2 eps/((1+eps)^2 (2+eps)) -> 0, cross-checked by 2D quadrature
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

NP = 0; NF = 0
def check(name, ok, info=''):
    global NP, NF
    if ok: NP += 1
    else: NF += 1
    print(('[PASS] ' if ok else '[FAIL] ') + name + ('   ' + info if info else ''))

I = sp.I
eps = sp.symbols('epsilon', positive=True)
def lhs(avars, shift):
    """sum over orderings; shift(perm, j) = regulator of the j-th cumulative denominator (j=1..m, from the infinite end)"""
    m = len(avars); tot = 0
    for p in itertools.permutations(range(m)):
        term = 1
        for j in range(1, m + 1):
            term *= I / (sum(avars[p[i]] for i in range(j)) + I * shift(p, j))
        tot += term
    return tot

for m in (2, 3):
    a = sp.symbols('a1:%d' % (m + 1), real=True)
    rhs = sp.prod([I / (aj + I * eps) for aj in a])
    adi = lhs(a, lambda p, j: j * eps)
    check('(1a) m=%d past-pointing, adiabatic e^{-eps|t|} (j-th denominator +i j eps): identity exact at finite eps' % m,
          sp.cancel(sp.together(adi - rhs)) == 0)
    uni = lhs(a, lambda p, j: eps)
    dU = sp.cancel(sp.together(uni - rhs))
    check('(1b) m=%d uniform +i eps on every denominator: identity NOT exact (defect != 0)' % m, dU != 0)
    # defect is O(eps) at generic real a
    pt = {a[k]: sp.Rational(k + 2, 3) * (-1)**k for k in range(m)}
    dnum = [complex(dU.subs(pt).subs(eps, e)) for e in (sp.Rational(1, 10**3), sp.Rational(1, 10**4))]
    check('(1c) m=%d uniform defect is O(eps) at a generic point (ratio of defects for eps=1e-3,1e-4 ~ 10)' % m,
          abs(abs(dnum[0] / dnum[1]) - 10) < 0.1, 'ratio %.4f' % abs(dnum[0] / dnum[1]))
    # future-pointing: -i/(n.(k_j+...+k_m) - i (m-j+1) eps), product of -i/(a - i eps)
    fut_rhs = sp.prod([-I / (aj - I * eps) for aj in a])
    fut = 0
    for p in itertools.permutations(range(m)):
        term = 1
        for j in range(1, m + 1):
            term *= -I / (sum(a[p[i]] for i in range(j - 1, m)) - I * (m - j + 1) * eps)
        fut += term
    check('(1d) m=%d future-pointing, adiabatic: identity exact at finite eps' % m, sp.cancel(sp.together(fut - fut_rhs)) == 0)
    # unequal per-gluon dampings eps_j (still additive): exact as well -> "only adiabatic" means "only additive"
    ej = sp.symbols('e1:%d' % (m + 1), positive=True)
    gen = lhs(a, lambda p, j: sum(ej[p[i]] for i in range(j)))
    gen_rhs = sp.prod([I / (a[k] + I * ej[k]) for k in range(m)])
    check('(1e) m=%d unequal per-gluon dampings e^{-eps_k|t|} (cumulative sums): identity also exact' % m,
          sp.cancel(sp.together(gen - gen_rhs)) == 0)

# m = 4, 5: exact Gaussian-rational arithmetic at random points (adiabatic exact; uniform not; unequal additive exact)
import random
random.seed(11)
for m in (4, 5):
    okA = okU = okG = True
    for trial in range(3):
        av = [sp.Rational(random.randint(-40, 40), random.randint(1, 9)) for _ in range(m)]
        ev = sp.Rational(random.randint(1, 30), 97)
        evs = [sp.Rational(random.randint(1, 30), 89) for _ in range(m)]
        rhsv = sp.prod([I / (x + I * ev) for x in av])
        okA &= sp.nsimplify(sp.expand(lhs(av, lambda p, j: j * ev) - rhsv)) == 0
        okU &= sp.nsimplify(sp.expand(lhs(av, lambda p, j: ev) - rhsv)) != 0
        okG &= sp.nsimplify(sp.expand(lhs(av, lambda p, j: sum(evs[p[i]] for i in range(j))) - sp.prod([I / (av[k] + I * evs[k]) for k in range(m)]))) == 0
    check('(1g) m=%d exact rationals (3 points): adiabatic exact, uniform not exact, unequal additive exact' % m, okA and okU and okG)

# (1f) explicit m=2 uniform defect
a1, a2 = sp.symbols('a1 a2', real=True)
d2 = sp.simplify(lhs((a1, a2), lambda p, j: eps) - I / (a1 + I * eps) * I / (a2 + I * eps))
check('(1f) m=2 uniform defect = -i eps/[(a1+i eps)(a2+i eps)(a1+a2+i eps)] (with the factors i)',
      sp.simplify(d2 - (-I * eps / ((a1 + I * eps) * (a2 + I * eps) * (a1 + a2 + I * eps)))) == 0, str(sp.factor(d2)))

# ---------------------------------------------------------------- (2) necessity
h1, h2, h12 = sp.symbols('eta1 eta2 eta12', positive=True)
def shift2(p, j):
    if j == 2: return h12
    return h1 if p[0] == 0 else h2
D = sp.factor(sp.together(lhs((a1, a2), shift2) - I / (a1 + I * h1) * I / (a2 + I * h2)))
num = sp.numer(D)
check('(2a) m=2, arbitrary shifts eta1, eta2, eta12: defect proportional to (eta1+eta2-eta12) => exact for all real a iff additive',
      sp.simplify(num.subs(h12, h1 + h2)) == 0 and sp.simplify(num.subs(h12, h1 + h2 + sp.Rational(1, 7))) != 0, 'defect = %s' % D)
a3 = sp.symbols('a3', real=True)
hh = {frozenset([0]): sp.Symbol('n1', positive=True), frozenset([1]): sp.Symbol('n2', positive=True), frozenset([2]): sp.Symbol('n3', positive=True)}
def shift3(p, j, triple):
    S = frozenset(p[:j])
    if len(S) == 1: return hh[S]
    if len(S) == 2: return sum(hh[frozenset([k])] for k in S)
    return triple
n1, n2, n3 = hh[frozenset([0])], hh[frozenset([1])], hh[frozenset([2])]
r3 = I / (a1 + I * n1) * I / (a2 + I * n2) * I / (a3 + I * n3)
ok_add = sp.simplify(sp.together(lhs((a1, a2, a3), lambda p, j: shift3(p, j, n1 + n2 + n3)) - r3)) == 0
bad = sp.simplify(sp.together(lhs((a1, a2, a3), lambda p, j: shift3(p, j, n1 + n2 + n3 + sp.Rational(1, 5))) - r3))
check('(2b) m=3: additive shifts exact; a non-additive triple shift breaks the identity', ok_add and bad != 0)

# ---------------------------------------------------------------- (3) uniform prescription as an ordered integral
# ordering lambda1 < lambda2 < 0 (gluon 1 farther from the endpoint), field factors e^{-i lambda_j a_j};
# int_{-inf}^{u} e^{c lambda} d lambda = e^{c u}/c for Re c > 0 (done by hand: the dampings make every c have Re c > 0)
A1, A2 = sp.symbols('A1 A2', real=True)
e_ = sp.symbols('e', positive=True)
def ordered(d1, d2):
    """damping e^{d1 lambda1 + d2 lambda2}: int_{-inf}^0 dl2 int_{-inf}^{l2} dl1 e^{(d1 - i A1) l1 + (d2 - i A2) l2}"""
    c1 = d1 - I * A1; c2 = d2 - I * A2
    return (1 / c1) * (1 / (c1 + c2))      # inner gives e^{c1 l2}/c1, outer int_{-inf}^0 e^{(c1+c2) l2} = 1/(c1+c2)
check('(3a) damping e^{eps lambda} on EACH field (adiabatic), ordered: = i/(A1+i eps) * i/(A1+A2+2i eps)',
      sp.simplify(ordered(e_, e_) - I / (A1 + I * e_) * I / (A1 + A2 + 2 * I * e_)) == 0)
check('(3b) damping only at the farthest attachment e^{eps lambda_min}: = i/(A1+i eps) * i/(A1+A2+i eps), the uniform prescription (not a product of single-field factors)',
      sp.simplify(ordered(e_, 0) - I / (A1 + I * e_) * I / (A1 + A2 + I * e_)) == 0)
# numerical spot check of (3a) by direct 2D quadrature over the simplex
A1v, A2v, ev = mp.mpf('0.7'), mp.mpf('-1.9'), mp.mpf('0.4')
num = mp.quad(lambda l2: mp.quad(lambda l1: mp.exp((ev - 1j * A1v) * l1 + (ev - 1j * A2v) * l2), [-mp.inf, l2]), [-mp.inf, 0])
check('(3c) direct 2D quadrature over the simplex confirms (3a)', abs(num - complex(ordered(e_, e_).subs({A1: 0.7, A2: -1.9, e_: 0.4}))) < 1e-12)

# ---------------------------------------------------------------- (4) distributional limit of the uniform defect
# pairing with phi(a1,a2) = 1/((1+a1^2)(1+a2^2)): close both contours in the UHP; the defect's poles are all in the LHP
Dfun = lambda x, y, e: -1j * e / ((x + 1j * e) * (y + 1j * e) * (x + y + 1j * e))
exact = lambda e: mp.pi**2 * e / ((1 + e)**2 * (2 + e))
for e in [mp.mpf('0.2'), mp.mpf('0.05')]:
    # 2D quadrature on contours shifted to Im a1 = Im a2 = 1/2 (no singularity is crossed: the defect's poles are at
    # Im a1, Im a2, Im(a1+a2) = -eps, the test function's at a = +-i), where the integrand is smooth
    sh = 0.5j
    fsh = lambda x, y: Dfun(x + sh, y + sh, e) / ((1 + (x + sh)**2) * (1 + (y + sh)**2))
    gq = lambda u, v: fsh(mp.tan(u), mp.tan(v)) / (mp.cos(u)**2 * mp.cos(v)**2)          # x = tan u, y = tan v
    pts = [-mp.pi / 2, -mp.pi / 4, 0, mp.pi / 4, mp.pi / 2]
    with mp.workdps(20):
        num2 = mp.quad(lambda u: mp.quad(lambda v: gq(u, v), pts), pts)
    check('(4a) <uniform defect, Lorentzian> = pi^2 eps/((1+eps)^2(2+eps)) (residues) vs 2D quadrature, eps=%s' % e,
          abs(num2 - exact(e)) < 1e-8, 'quad=%s exact=%s' % (mp.nstr(num2, 10), mp.nstr(exact(e), 10)))
check('(4b) hence the uniform-eps identity holds only distributionally: pairing ~ (pi^2/2) eps -> 0, nonzero at any finite eps',
      all(exact(mp.mpf(10)**(-k)) > 0 for k in range(1, 8)) and abs(exact(mp.mpf('1e-8')) / mp.mpf('1e-8') - mp.pi**2 / 2) < 1e-6)

print('\nSUMMARY n26_s2: %d PASS, %d FAIL' % (NP, NF))
