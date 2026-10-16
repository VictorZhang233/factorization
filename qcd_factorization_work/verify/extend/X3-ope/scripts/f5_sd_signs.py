"""f5_sd_signs.py -- X3 fix round 2: check of the Grassmann signs in the
Schwinger-Dyson identity (DR-SD) used in Theorem B.

Claim tested (Euclidean weight e^{-S}; the Minkowski weight e^{iS} only adds
an overall factor i):

    < Y * dS/dphi(y) * phi_1 ... phi_n >
        = sum_{k : phi_k = phi(y)} eps_k < Y * phi_1 .. (omit k) .. phi_n >,

    eps_k = (-1)^{|phi| * (|phi_1| + ... + |phi_{k-1}|)}          (no |Y|!)

for any monomial Y that does not contain phi(y) (so that the delta(0) term,
which vanishes in DR, is absent here as well).  dS/dphi is the LEFT
derivative.  The first version of the report had the factor
(-1)^{|phi||Y|} in eps_k (review r2-2, item 5); the script shows that this
factor is wrong whenever |phi| = |Y| = 1 and right otherwise.

Model: 0-dimensional 'lattice' with sites x = 0,1,2 and four Grassmann
fields psi_x, psibar_x, c_x, cbar_x (all odd), action
    S = sum psibar_x M_xy psi_y + sum cbar_x K_xy c_y
        + lam * sum_x psibar_x psi_x cbar_x c_x .
Berezin integrals are exact polynomial algebra (no convergence issues).
Coefficients are exact rationals (sympy).
"""
import sys, os, itertools, random
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
from sympy import Rational, simplify

random.seed(20261011)

# ---------------- Grassmann algebra -------------------------------------
# element: dict {tuple(sorted generator indices): coefficient}

def gmul_mono(a, b):
    """product of two sorted monomials a,b (tuples); return (sign, mono) or (0,None)"""
    if set(a) & set(b):
        return 0, None
    arr = list(a) + list(b)
    # sign of the permutation sorting arr (bubble count of inversions)
    inv = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inv += 1
    return (-1) ** inv, tuple(sorted(arr))

def gmul(A, B):
    C = {}
    for ma, ca in A.items():
        for mb, cb in B.items():
            s, m = gmul_mono(ma, mb)
            if s == 0:
                continue
            C[m] = C.get(m, 0) + s * ca * cb
    return {m: c for m, c in C.items() if c != 0}

def gadd(A, B, fac=1):
    C = dict(A)
    for m, c in B.items():
        C[m] = C.get(m, 0) + fac * c
    return {m: c for m, c in C.items() if c != 0}

def gen(i):
    return {(i,): Rational(1)}

ONE = {(): Rational(1)}

def dleft(A, i):
    """left derivative d/d theta_i"""
    C = {}
    for m, c in A.items():
        if i in m:
            pos = m.index(i)
            mm = m[:pos] + m[pos + 1:]
            C[mm] = C.get(mm, 0) + (-1) ** pos * c
    return {m: c for m, c in C.items() if c != 0}

def gexp_neg(S, nmax):
    """exp(-S) for an even element S without constant term"""
    E = dict(ONE)
    term = dict(ONE)
    for k in range(1, nmax + 1):
        term = gmul(term, S)
        term = {m: -c / k for m, c in term.items()}
        if not term:
            break
        E = gadd(E, term)
    return E

# ---------------- model ---------------------------------------------------
NS = 3
fields = ['psi', 'psibar', 'c', 'cbar']
idx = {}
n = 0
for f in fields:
    for x in range(NS):
        idx[(f, x)] = n
        n += 1
NG = n
TOP = tuple(range(NG))

def rnd():
    return Rational(random.randint(-5, 5), random.randint(1, 4))

M = [[rnd() + (3 if i == j else 0) for j in range(NS)] for i in range(NS)]
K = [[rnd() + (2 if i == j else 0) for j in range(NS)] for i in range(NS)]
lam = Rational(2, 3)

S = {}
for x in range(NS):
    for y in range(NS):
        S = gadd(S, gmul(gen(idx[('psibar', x)]), gen(idx[('psi', y)])), M[x][y])
        S = gadd(S, gmul(gen(idx[('cbar', x)]), gen(idx[('c', y)])), K[x][y])
for x in range(NS):
    t = gmul(gmul(gen(idx[('psibar', x)]), gen(idx[('psi', x)])),
             gmul(gen(idx[('cbar', x)]), gen(idx[('c', x)])))
    S = gadd(S, t, lam)
W = gexp_neg(S, NG)

def berezin(A):
    return A.get(TOP, 0)

Z = berezin(W)
assert Z != 0

def vev(A):
    return simplify(berezin(gmul(A, W)) / Z)

def prod(lst):
    P = dict(ONE)
    for g in lst:
        P = gmul(P, g)
    return P

# ---------------- tests ---------------------------------------------------
all_gens = list(idx.keys())
ntest = 0
nok_new = 0
nok_old = 0
nY_odd_and_phi_odd = 0
old_fail_cases = 0
for trial in range(400):
    phi = random.choice(all_gens)            # phi(y)
    iphi = idx[phi]
    others = [g for g in all_gens if g != phi]
    # Y: random monomial (0..3 generators) not containing phi(y)
    ylen = random.randint(0, 3)
    Ylist = random.sample(others, ylen)
    # Phi string: contains phi(y) once or twice? (only once possible: theta^2=0)
    # put phi(y) at random position k among n insertions; others distinct, not in Y
    rest = [g for g in others if g not in Ylist]
    nPhi = random.randint(1, 4)
    Phil = random.sample(rest, nPhi - 1)
    kpos = random.randint(0, nPhi - 1)
    Phil.insert(kpos, phi)
    Y = prod([gen(idx[g]) for g in Ylist])
    Phi = prod([gen(idx[g]) for g in Phil])
    dS = dleft(S, iphi)
    lhs = vev(gmul(gmul(Y, dS), Phi))
    # right-hand side: only k = kpos contributes (phi(y) appears once)
    par_before = kpos  # all fields odd: number of odd fields before position k
    eps_new = (-1) ** (1 * par_before)
    eps_old = (-1) ** (1 * (ylen + par_before))
    Phik = prod([gen(idx[g]) for j, g in enumerate(Phil) if j != kpos])
    rhs0 = vev(gmul(Y, Phik))
    ntest += 1
    ok_new = simplify(lhs - eps_new * rhs0) == 0
    ok_old = simplify(lhs - eps_old * rhs0) == 0
    nok_new += ok_new
    nok_old += ok_old
    if ylen % 2 == 1:
        nY_odd_and_phi_odd += 1
        if (not ok_old) and rhs0 != 0:
            old_fail_cases += 1

print("f5_sd_signs: Grassmann toy check of DR-SD signs")
print("tests:", ntest)
print("eps_k = (-1)^{|phi| sum_{l<k}|phi_l|}        : passed", nok_new, "of", ntest)
print("eps_k with extra (-1)^{|phi||Y|} (rev1 form) : passed", nok_old, "of", ntest)
print("cases with |Y| odd:", nY_odd_and_phi_odd, "; of these the rev1 sign fails (non-zero rhs):", old_fail_cases)
assert nok_new == ntest
print("RESULT: corrected sign rule confirmed; the |Y| factor of rev1 is wrong for odd Y and odd phi.")
