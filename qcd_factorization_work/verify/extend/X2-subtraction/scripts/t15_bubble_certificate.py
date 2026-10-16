"""X2/T15: LP certificate for the bubble-chain (log-insertion) class: Gamma^(j) = ln^j(D_g) /(D_g D1 D2).
Four-shell representation (0<u<1; u=x/P, P=P'=1/sqrt2):
   rho^(j) = sum_s l_s^j T_s,  s in {D,e,t,h},  l_s = ln R_s,
   R_D = (u m2 v + kap)/v, R_e = u m2 + kap, R_t = kap/v, R_h = kap,
   T_D = (v/DG - 1/u)/(u m2 v + kap), T_e = m2/(u(m2+u)(u m2+kap)), T_t = 1/(u(uv+kap)),
   T_h = 1/((m2+u)(m2+u+kap)) - 1/(u(u+kap)),   DG = (m2+u)(v(1+m2)+kap)+kap v,  v = 1-u.
Bound on a cell with grouping g (partition of shells, each group G with reference ref(G) in G):
   |rho^(j)| <= sum_G |l_ref|^j |sum_{s in G} T_s| + sum_s j max(|l_s|,|l_ref|)^{j-1} |R_s-R_ref| (1/R_s+1/R_ref) |T_s|.
|l| <= C L (1+|X|) on any cell; so each piece is (polynomial in L,|X|) x (rational function), certified by tropical.py.
We report, for every cell of a polyhedral partition of the normalised log-plane, the best grouping and the resulting
lambda-exponent (must be >= 2 everywhere).  Then int |rho^(j)| <= C_j lambda^2 L^{j+2}."""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp, numpy as np
from tropical import monomials_of, positive_form, lp_max_psi

u, v, kap, m2 = sp.symbols('u v kap m2', positive=True)
DG = (m2 + u)*(v*(1 + m2) + kap) + kap*v
# each T as (numerator, list of positive den factors) with v symbol (v=1-u imposed in numerators)
T = {
 'D': ((v*u - DG), [DG, u, u*m2*v + kap]),            # (v/DG - 1/u)/(u m2 v + kap) = (u v - DG)/(DG u (u m2 v + kap))
 'e': (m2, [u, m2 + u, u*m2 + kap]),
 't': (sp.Integer(1), [u, u*v + kap]),
 'h': (None, None),
}
# T_h = 1/((m2+u)(m2+u+kap)) - 1/(u(u+kap)) = [u(u+kap) - (m2+u)(m2+u+kap)] / (...)
T['h'] = (u*(u + kap) - (m2 + u)*(m2 + u + kap), [m2 + u, m2 + u + kap, u, u + kap])
R = {'D': (u*m2*v + kap, [v]), 'e': (u*m2 + kap, []), 't': (kap, [v]), 'h': (kap, [])}   # R = num/prod(den)

def combine(items):
    """items: list of (sign, (num, dens)). Return (num, dens) of the sum with common denominator (structural)."""
    dens = []
    for _, (n, ds) in items:
        for f in ds:
            if not any(sp.expand(f - g) == 0 for g in dens):
                dens.append(f)
    D = sp.Mul(*dens)
    N = 0
    for s, (n, ds) in items:
        N += s*n*sp.cancel(D/sp.Mul(*ds))
    return sp.expand(N), dens

def Rdiff_times_T(s, r):
    """|R_s - R_r| (1/R_s + 1/R_r) |T_s|  -> two rational functions (num, dens)."""
    (ns, ds_), (nr, dr_) = R[s], R[r]
    diff_num, diff_den = combine([(1, (ns, ds_)), (-1, (nr, dr_))])
    out = []
    for (nn, dd) in [(ns, ds_), (nr, dr_)]:
        # 1/R = prod(dd)/nn
        num = diff_num*sp.Mul(*dd)*T[s][0]
        dens = list(diff_den) + [nn] + list(T[s][1])
        out.append((sp.expand(num), dens))
    return out

def exponent(num, dens, region, cons):
    """max psi for rational function num/prod(dens) on cell; region 'I' (u,kap) with v~1, 'II' (v,kap) with u~1."""
    if region == 'I':
        N = sp.expand(num.subs(v, 1 - u)); loc = [u, kap]
        dl = [sp.expand(f.subs(v, 1)) for f in dens]
    else:
        N = sp.expand(num.subs(u, 1 - v)); loc = [v, kap]
        dl = [sp.expand(f.subs(u, 1)) for f in dens]
    if N == 0:
        return np.inf
    mons = monomials_of(N, loc, m2)
    forms = [positive_form(g, loc, m2) for g in dl]
    G = [np.array(c, float) for c, _ in cons]; h = [float(rr) for _, rr in cons]
    best = -np.inf
    for c, a in mons:
        val, X, res = lp_max_psi(a, forms, [1, 1], G, h, 2)
        best = max(best, val)
    return -2*best      # lambda exponent

SHELLS = ['D', 'e', 't', 'h']
# Universal decomposition (REPORT Lemma B.11, "rectangle rule" for the shell logarithms):
#   l_e = l_h + a, l_t = l_h + b, l_D = l_h + a + b + delta,
#   a = ln(1 + u m2/kap) in [0, min(u m2/kap, C L)],  b = ln(1/v) in [0, min(u/v, C L)],
#   |delta| <= u^2 m2/(u m2 v + kap).
#   rho^(j) = sum_n C(j,n) l_h^{j-n} [ a^n (T_D+T_e) + b^n (T_D+T_t) + ((a+b+delta)^n - a^n - b^n) T_D ].
# Pieces (any j; L-powers aside):  P0 = rho_r;  P1 = w_a |T_D+T_e|;  P2 = w_b |T_D+T_t|;  P3 = d |T_D|;  P4 = w_a w_b |T_D|,
# with w_a in {u m2/kap, 1(x L)}, w_b in {u/v, 1(x L)}, d = u^2 m2/(u m2 v + kap).
def weighted(G, wnum, wden):
    numG, densG = combine([(1, T[s]) for s in G])
    return sp.expand(wnum*numG), list(wden) + list(densG)

cache = {}
def piece_exponents(region, cons, key):
    if key in cache: return cache[key]
    numr, densr = combine([(1, T[s]) for s in SHELLS])
    out = {'P0': exponent(numr, densr, region, cons)}
    def best(G, choices):
        vals = []
        for (wn, wd) in choices:
            n_, d_ = weighted(G, wn, wd); vals.append(exponent(n_, d_, region, cons))
        return max(vals)
    wa = [(u*m2, [kap]), (sp.Integer(1), [])]
    wb = [(u, [v]), (sp.Integer(1), [])]
    out['P1'] = best(['D', 'e'], wa)
    out['P2'] = best(['D', 't'], wb)
    out['P3'] = best(['D'], [(u**2*m2, [u*m2*v + kap])])
    out['P4'] = best(['D'], [(an*bn, ad + bd) for (an, ad) in wa for (bn, bd) in wb])
    out['min'] = min(out.values())
    cache[key] = out
    return out

if __name__ == "__main__":
    # cells in adapted coordinates (X1, Y), Y = Xk - X1  (region I: X1 = Xu; region II: X1 = Xv, there y ~ kap)
    x1_edges = [-np.inf, -3, -2, -1.5, -1.25, -1, -0.75, -0.5, -0.25, 0]
    y_edges = [-np.inf, -4, -3, -2, -1.5, -1.25, -1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 1, 2, np.inf]
    worst_cell = np.inf; report = []
    for region in ['I', 'II']:
        for (a, b) in zip(x1_edges[:-1], x1_edges[1:]):
            for (c, d) in zip(y_edges[:-1], y_edges[1:]):
                cons = []
                if np.isfinite(b): cons.append(([1, 0], b))
                if np.isfinite(a): cons.append(([-1, 0], -a))
                if region == 'I':
                    if np.isfinite(d): cons.append(([-1, 1], d))
                    if np.isfinite(c): cons.append(([1, -1], -c))
                else:   # region II: u ~ 1, use Y = Xk directly
                    if np.isfinite(d): cons.append(([0, 1], d))
                    if np.isfinite(c): cons.append(([0, -1], -c))
                ex = piece_exponents(region, cons, (region, a, b, c, d))
                bestname = min(ex, key=lambda k: ex[k]); bestval = ex['min']
                report.append((region, a, b, c, d, bestname, bestval))
                worst_cell = min(worst_cell, bestval)
                if bestval < 2 - 1e-9:
                    print(f"  cell {region} X1 in [{a},{b}] Y in [{c},{d}]: best {bestname} -> lambda^{bestval:.3f}  ** below 2 **  {ex}", flush=True)
    print(f"cells: {len(report)}; minimal certified lambda-exponent over all cells = {worst_cell:.4f}")
    from collections import Counter
    print("grouping usage:", Counter(r[5] for r in report))
    import json
    json.dump([list(map(lambda z: (None if (isinstance(z, float) and not np.isfinite(z)) else z), r)) for r in report],
              open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bubble_cells.json'), 'w'))
