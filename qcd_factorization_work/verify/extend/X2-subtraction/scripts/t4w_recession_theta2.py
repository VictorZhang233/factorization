"""X2/T4w: exact recession-slope check (strictly negative required) for all triangle certificates at theta=2, eps=0."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
from fractions import Fraction
from tropical import monomials_of, positive_form
from recession import max_slope
import t4_triangle_certificates as T4
u, v, kap, m2 = T4.u, T4.v, T4.kap, T4.m2
F, Fbig, combo = T4.F, T4.Fbig, T4.combo
t2 = Fraction(1)
def slope(label, N, D, local, frozen, cons):
    Nl = N
    if v in local: Nl = sp.expand(N.subs(u, 1 - v))
    for var, val in frozen.items(): Nl = Nl.subs(var, val)
    Nl = sp.expand(Nl)
    dl = []
    for f in D:
        g = f
        for var in [u, v]:
            if var not in local: g = g.subs(var, 1)
        dl.append(sp.expand(g))
    forms = [positive_form(g, local, m2) for g in dl]
    n = len(local)
    worst = None
    for cf, al in monomials_of(Nl, local, m2):
        if n == 2:
            s = max_slope(al, [1]*n, forms, cons)
        else:   # 1D: rays +-1 allowed by constraints
            s = None
            for r in (1, -1):
                if all(c[0]*r <= 0 for c, _ in cons):
                    val = (int(al[0]) + 1)*r - sum(max(int(b[0])*r for b in fl) for fl in forms)
                    s = val if (s is None or val > s) else s
        if s is not None: worst = s if (worst is None or s > worst) else worst
    print(f"[{label}] max recession slope = {worst}  ({'OK' if (worst is None or worst < 0) else 'FAIL'})")
items = []
N, D = combo(F, [('G', 1), ('S', -1)]); items += [('(H1)_S', N, D, [u, kap], {}, [([1, 0], -t2), ([-1, 1], -t2)])]
for nm in ['C1', 'C2', 'H']:
    N, D = combo(F, [(nm, 1)]); items += [(f'(H2)_S {nm}', N, D, [u, kap], {}, [([1, 0], -t2), ([-1, 1], -t2)])]
N, D = combo(F, [('G', 1), ('S', -1), ('C1', -1)])
items += [('(H1)_C1 I', N, D, [u, kap], {}, [([1, 0], 0), ([-1, 0], t2), ([-1, 1], -t2)]),
          ('(H1)_C1 II', N, D, [v, kap], {}, [([1, 0], 0), ([0, 1], -t2)])]
Nb, Db = combo(Fbig, [('S', -1), ('C1', -1)]); items += [('(H1)_C1 III', Nb, Db, [kap], {u: 1}, [([1], -t2)])]
for nm in ['C2', 'H']:
    N, D = combo(F, [(nm, 1)])
    items += [(f'(H2)_C1 {nm} I', N, D, [u, kap], {}, [([1, 0], 0), ([-1, 0], t2), ([-1, 1], -t2)]),
              (f'(H2)_C1 {nm} II', N, D, [v, kap], {}, [([1, 0], 0), ([0, 1], -t2)])]
    Nb, Db = combo(Fbig, [(nm, 1)]); items += [(f'(H2)_C1 {nm} III', Nb, Db, [kap], {u: 1}, [([1], -t2)])]
N, D = combo(F, [('G', 1), ('S', -1), ('C2', -1)]); items += [('(H1)_C2', N, D, [u, kap], {}, [([1, 0], -t2), ([1, -1], t2), ([-1, 1], 0)])]
for nm in ['C1', 'H']:
    N, D = combo(F, [(nm, 1)]); items += [(f'(H2)_C2 {nm}', N, D, [u, kap], {}, [([1, 0], -t2), ([1, -1], t2), ([-1, 1], 0)])]
N, D = combo(F, [('G', 1), ('S', -1), ('C1', -1), ('C2', -1), ('H', -1)])
items += [('(H1)_H a', N, D, [u, kap], {}, [([1, 0], 0), ([-1, 0], t2), ([1, -1], t2)]),
          ('(H1)_H b', N, D, [v, kap], {}, [([1, 0], 0), ([0, -1], t2)]),
          ('(H1)_H c', N, D, [u, kap], {}, [([1, 0], -t2), ([1, -1], 0)])]
Nb, Db = combo(Fbig, [('S', -1), ('C1', -1), ('C2', -1), ('H', -1)])
items += [('r u>1', Nb, Db, [u, kap], {}, [([-1, 0], 0)])]
for it in items: slope(*it)
