#!/usr/bin/env python3
"""E19 side check: Collins (2011) eq. (14.30), p. 559 (OA reissue = Nov. 2013 printing).
The integrand of (14.29) is  sum_{c=1}^N [prod_{f>c} 1/(a_f - i0)] 2 pi delta(a_c) [prod_{f<c} 1/(a_f + i0)].
Printed (14.30):     i prod 1/(a_f - i0) - i prod 1/(a_f + i0)
Author's errata (Sec. 3, 'P. 559 ... the sign of each of the terms should be reversed'):
                    -i prod 1/(a_f - i0) + i prod 1/(a_f + i0)
Exact check with finite eps: 2 pi delta_eps(a) = 2 eps/(a^2 + eps^2) = i[1/(a + i eps) - 1/(a - i eps)].
Run: python3 -I e19_collins1430.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
eps = sp.symbols('epsilon', positive=True)
allok = True
for N in range(1, 5):
    a = sp.symbols(f'a1:{N+1}', real=True)
    u = [1/(ai + sp.I*eps) for ai in a]; v = [1/(ai - sp.I*eps) for ai in a]
    delta = [2*eps/(ai**2 + eps**2) for ai in a]
    lhs = sum(sp.Mul(*[v[f] for f in range(c + 1, N)])*delta[c]*sp.Mul(*[u[f] for f in range(c)]) for c in range(N))
    printed = sp.I*sp.Mul(*v) - sp.I*sp.Mul(*u)
    errata = -sp.I*sp.Mul(*v) + sp.I*sp.Mul(*u)
    ok_err = sp.simplify(sp.together(lhs - errata)) == 0
    ok_pr = sp.simplify(sp.together(lhs + printed)) == 0           # printed = - (correct)
    allok &= ok_err and ok_pr
    print(f'N={N}: (14.29) integrand == errata form: {ok_err};  printed (14.30) == -(integrand): {ok_pr}')
print('SUMMARY:', 'PASS (printed (14.30) has the overall sign reversed; the author\'s erratum is correct)' if allok else 'FAIL')
