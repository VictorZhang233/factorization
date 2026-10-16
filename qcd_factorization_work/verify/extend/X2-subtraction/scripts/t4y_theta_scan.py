"""X2/T4y: exact LP certificates of all triangle (H1)/(H2) items for the 2x2 cover U(theta), s = lambda^theta."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction
import t4x_triangle_exact as X
import t4_triangle_certificates as T4
u, v, kap = T4.u, T4.v, T4.kap
F, Fbig, combo = T4.F, T4.Fbig, T4.combo
for theta in [Fraction(3, 2), Fraction(19, 10), Fraction(2)]:
    t2 = theta/2
    print(f"===== theta = {theta}  (s = lambda^{theta})")
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
              ('(H1)_H c', N, D, [u, kap], {}, [([1, 0], -t2), ([1, -1], 0)])]
    worst = None
    for it in items:
        ph, d, f = X.exact_cert(*it)
        worst = ph if (worst is None or ph > worst) else worst
    print(f"  worst item: lambda^{-2*worst}")
