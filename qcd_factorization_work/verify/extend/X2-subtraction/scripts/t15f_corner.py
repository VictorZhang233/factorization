"""X2/T15f: the corner cell II {Xv <= -3, Xk <= -4}: bound rho_r by sum_s |T_s| (and the T's of the other pieces as in T15)
and check exact exponents and strictly negative recession slopes."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp, numpy as np
from tropical import monomials_of, positive_form
from exact_verify import build, solve_exact
from recession import max_slope
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 't15_bubble_certificate.py')).read().split('if __name__')[0]
src = src.replace("os.path.dirname(os.path.abspath(__file__))", repr(os.path.dirname(os.path.abspath(__file__))))
ns = {}; exec(src, ns)
u, v, kap, m2, T = ns['u'], ns['v'], ns['kap'], ns['m2'], ns['T']
cons = [([1, 0], -3), ([0, 1], -4)]
local = [v, kap]
for s_ in ['D', 'e', 't', 'h']:
    n_, d_ = T[s_]
    N = sp.expand(n_.subs(u, 1 - v)); forms = [positive_form(sp.expand(g.subs(u, 1)), local, m2) for g in d_]
    worst = None; slope = None
    for cf, al in monomials_of(N, local, m2):
        rows, rhs, cc, const = build(al, forms, [1, 1], [c for c, _ in cons], [r for _, r in cons], 2)
        out, msg = solve_exact(rows, rhs, cc, const)
        assert out is not None, msg
        worst = out[0] if (worst is None or out[0] > worst) else worst
        sl = max_slope(al, [1, 1], forms, cons)
        slope = sl if (slope is None or sl > slope) else slope
    print(f"T_{s_} on corner: exact exponent lambda^{-2*worst}, max recession slope {slope}")
