"""X2/T4x: exact rational re-verification of all triangle LP certificates of T4 (eps = 0)."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp, numpy as np
from fractions import Fraction
import t4_triangle_certificates as T4
from tropical import monomials_of, positive_form
from exact_verify import build, solve_exact
u, v, kap, m2 = T4.u, T4.v, T4.kap, T4.m2

def exact_cert(label, N, dens, local, frozen, cons):
    Nl = N
    if v in local: Nl = sp.expand(N.subs(u, 1 - v))
    for var, val in frozen.items(): Nl = Nl.subs(var, val)
    Nl = sp.expand(Nl)
    densl = []
    for f in dens:
        g = f
        for var in [u, v]:
            if var not in local: g = g.subs(var, 1)
        densl.append(sp.expand(g))
    n = len(local)
    mons = monomials_of(Nl, local, m2)
    forms = [positive_form(g, local, m2) for g in densl]
    G = [list(c) for c, _ in cons]; h = [r for _, r in cons]
    best = None; dmax = 0; fails = 0
    vals = []
    for c, a in mons:
        rows, rhs, cc, const = build(a, forms, [1]*n, G, h, n)
        out, msg = solve_exact(rows, rhs, cc, const)
        if out is None:
            fails += 1; print(f"   [{label}] monomial {a}: {msg}"); continue
        val, dbound, fl = out
        vals.append((val, dbound, fl))
    phistar = max(v_[0] for v_ in vals)
    d = max(v_[1] for v_ in vals if v_[0] == phistar)
    flmax = max(v_[2] for v_ in vals)
    print(f"[{label}] exact phi* = {phistar} (float {flmax:.6f})  -> lambda^{-2*phistar} L^(<= {d});  monomials {len(mons)}, failures {fails}")
    return phistar, d, fails

if __name__ == "__main__":
    F, Fbig, combo = T4.F, T4.Fbig, T4.combo
    t2 = Fraction(1, 2)
    items = []
    N, D = combo(F, [('G', 1), ('S', -1), ('C1', -1), ('C2', -1), ('H', -1)])
    items += [('r 0<u<1/2', N, D, [u, kap], {}, [([1, 0], 0)]), ('r 1/2<u<1', N, D, [v, kap], {}, [([1, 0], 0)])]
    Nb, Db = combo(Fbig, [('S', -1), ('C1', -1), ('C2', -1), ('H', -1)])
    items += [('r u>1', Nb, Db, [u, kap], {}, [([-1, 0], 0)])]
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
    tot_fail = 0
    for it in items:
        ph, d, f = exact_cert(*it); tot_fail += f
    print("TOTAL exact-dual failures:", tot_fail)
