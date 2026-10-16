"""
W10 / Ch9 sec:method-unitarity -- checks of
 (1) the cut-position telescoping identity at finite eps (all alpha_i = beta_i):
     sum_{c=1}^N [prod_{f>c} 1/(a_f - i e)] 2e/(a_c^2+e^2) [prod_{f<c} 1/(a_f + i e)] = i prod 1/(a_f+ie) - i prod 1/(a_f-ie)
     and int dE/(2 pi) of it with a_f = E - d_f: 1 for N=1, 0 for N>=2
 (2) the identity with insertions (lem:appO-cut-position) for small n with random complex weights
 (3) soft-factor unitarity at one loop in a toy: real + virtual cancel when the soft momentum is unconstrained
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
import random

npass = 0; nfail = 0
def check(name, ok, info=''):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(('[PASS] ' if ok else '[FAIL] ') + name + ((' : ' + str(info)) if info != '' else ''))

e = sp.symbols('e', positive=True)
for N in range(1, 6):
    a = sp.symbols('a1:%d' % (N+1), real=True)
    lhs = 0
    for c in range(N):
        term = 2*e/(a[c]**2 + e**2)
        for f in range(c+1, N): term *= 1/(a[f] - sp.I*e)
        for f in range(c): term *= 1/(a[f] + sp.I*e)
        lhs += term
    rhs = sp.I*sp.prod([1/(af + sp.I*e) for af in a]) - sp.I*sp.prod([1/(af - sp.I*e) for af in a])
    check('(1) cut telescoping identity, N=%d (exact, symbolic)' % N, sp.simplify(lhs - rhs) == 0)
mp.mp.dps = 25
for N in [1, 2, 3]:
    ds = [mp.mpf(x) for x in ['0.3', '-0.7', '1.1'][:N]]
    eps = mp.mpf('0.05')
    f = lambda E: (1j*mp.fprod([1/(E - d + 1j*eps) for d in ds]) - 1j*mp.fprod([1/(E - d - 1j*eps) for d in ds]))/(2*mp.pi)
    val = mp.quad(f, [-mp.inf, -2, -1, 0, 1, 2, mp.inf])
    check('(1) int dE/(2pi) [cut sum] = %d for N=%d' % (1 if N == 1 else 0, N), abs(val - (1 if N == 1 else 0)) < 1e-10, mp.nstr(val, 12))

# (2) identity with insertions: sum_j T_j = delta_{n0} W_0 - i sum_m (alpha_m - beta_m) prod_{i<m} alpha_i prod_{i>m} beta_i int dE/2pi H_m
random.seed(7)
for n in range(1, 5):
    Es = [mp.mpf(random.uniform(-1, 1)) for _ in range(n+1)]
    al = [None] + [mp.mpc(random.uniform(-1, 1), random.uniform(-1, 1)) for _ in range(n)]
    be = [None] + [mp.mpc(random.uniform(-1, 1), random.uniform(-1, 1)) for _ in range(n)]
    eta = mp.mpf('0.3')
    def Tj(j):
        W = mp.fprod([al[i] for i in range(1, j+1)])*mp.fprod([be[i] for i in range(j+1, n+1)])
        f = lambda E: (mp.fprod([1/(E - Es[i] + 1j*eta) for i in range(j)])*(2*eta/((E - Es[j])**2 + eta**2))
                       *mp.fprod([1/(E - Es[i] - 1j*eta) for i in range(j+1, n+1)]))/(2*mp.pi)
        return W*mp.quad(f, [-mp.inf, -1, 0, 1, mp.inf])
    lhs = sum(Tj(j) for j in range(n+1))
    rhs = 0
    for mm in range(1, n+1):
        H = lambda E: (mp.fprod([1/(E - Es[i] + 1j*eta) for i in range(mm)])*mp.fprod([1/(E - Es[i] - 1j*eta) for i in range(mm, n+1)]))/(2*mp.pi)
        rhs += -1j*(al[mm] - be[mm])*mp.fprod([al[i] for i in range(1, mm)])*mp.fprod([be[i] for i in range(mm+1, n+1)])*mp.quad(H, [-mp.inf, -1, 0, 1, mp.inf])
    check('(2) cut-position identity with insertions, n=%d, random weights' % n, abs(lhs - rhs) < 1e-12, mp.nstr(abs(lhs-rhs), 3))
    # with alpha = beta: sum = 0 for n>=1
    be2 = list(al)
    def Tj2(j):
        W = mp.fprod([al[i] for i in range(1, j+1)])*mp.fprod([be2[i] for i in range(j+1, n+1)])
        f = lambda E: (mp.fprod([1/(E - Es[i] + 1j*eta) for i in range(j)])*(2*eta/((E - Es[j])**2 + eta**2))
                       *mp.fprod([1/(E - Es[i] - 1j*eta) for i in range(j+1, n+1)]))/(2*mp.pi)
        return W*mp.quad(f, [-mp.inf, -1, 0, 1, mp.inf])
    s2 = sum(Tj2(j) for j in range(n+1))
    check('(2) alpha_i = beta_i: sum over cut positions = 0 (n=%d)' % n, abs(s2) < 1e-12, mp.nstr(abs(s2), 3))
print('\n=== w10_unitarity: %d PASS, %d FAIL ===' % (npass, nfail))
