"""
W10 / Ch9 sec:method-unitarity -- exact rational check of the cut-position telescoping identity
    sum_{c=1}^N [prod_{f>c} 1/(a_f - i e)] 2e/(a_c^2+e^2) [prod_{f<c} 1/(a_f + i e)]
        = i prod_f 1/(a_f + i e) - i prod_f 1/(a_f - i e)
for N = 1..8, at random rational points (a_1..a_N, e>0), in exact complex-rational arithmetic (sympy Rational, I).
Both sides are rational functions of (a, e); equality at many random points (Schwartz-Zippel) complements the
symbolic N<=5 check of w10_unitarity.py and the telescoping proof printed in the text.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import random
import sympy as sp

random.seed(20261014)
npass = nfail = 0
def check(name, ok):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(('[PASS] ' if ok else '[FAIL] ') + name)

def rnd_rat():
    return sp.Rational(random.randint(-97, 97), random.randint(1, 23))

for N in range(1, 9):
    allok = True
    for trial in range(6):
        a = [rnd_rat() for _ in range(N)]
        e = sp.Rational(random.randint(1, 50), random.randint(1, 37))
        lhs = sp.Integer(0)
        for c in range(N):
            term = 2*e/(a[c]**2 + e**2)
            for f in range(c+1, N):
                term *= 1/(a[f] - sp.I*e)
            for f in range(c):
                term *= 1/(a[f] + sp.I*e)
            lhs += term
        rhs = sp.I*sp.prod([1/(af + sp.I*e) for af in a]) - sp.I*sp.prod([1/(af - sp.I*e) for af in a])
        diff = sp.nsimplify(sp.expand(lhs - rhs))
        allok &= (sp.simplify(diff) == 0)
    check('cut telescoping identity, N=%d, 6 random exact rational points' % N, allok)

print('\n=== w10_cutsum_exact: %d PASS, %d FAIL ===' % (npass, nfail))
