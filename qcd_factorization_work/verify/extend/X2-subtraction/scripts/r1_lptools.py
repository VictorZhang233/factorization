"""X2 fix round 1 / r1_lptools.py -- corrected and strengthened certificate tooling (replaces the use of
recession.max_slope and adds exact optimality certificates to exact_verify).

Fixes relative to the round-0 tooling (reviews r1_1 R2, r1_2 Lem 2.8 / F5):
 (1) recession check.  recession.cone_rays returned only boundary directions; for a half-plane cone, e.g.
     cone_rays([([-1,0],0)]) = [(0,1),(0,-1)], the interior direction (1,0) was never tested.  Here the recession cone
     {r : G r <= 0} (2D) is split into its intersections with the four closed quadrants; each piece is a pointed cone
     with at most two extreme rays, computed exactly.  The homogeneous recession function
         psi_inf(r) = <a+w, r> - sum_k max_{b in supp g_k} <b, r>
     is concave and piecewise linear on the segment between the two rays; its maximum is attained at an endpoint or
     at a tie point of two monomials of one factor.  All evaluations are exact (Fractions).
 (2) exact optimality.  exact_verify.solve_exact reconstructs an exact dual-feasible y (weak duality -> exact upper
     bound).  The face-dimension bound via complementary slackness requires y to be OPTIMAL.  Here we additionally
     reconstruct an exact primal feasible point x with c.x = b.y (exact rationals), i.e. an exact primal-dual optimal
     pair; only then is dim(argmax face) <= (n+K) - rank(A_S) asserted.
 (3) frozen variables in numerators.  Variables confined to a fixed interval [lo,hi] (lo>0) are NOT substituted into
     numerators; the numerator support is computed with those variables treated as coefficients
     (|c(u)| <= sum_j |c_j| hi^j on the interval), and denominators are compared with their value at u=1 with the
     explicit constant (max(hi,1)/min(lo,1))^{deg_u} for positive-coefficient factors (checked).
 (4) a general-dimension floating cross-check of the recession condition by LP over orthant cross-sections.
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import sympy as sp
from fractions import Fraction as Fr
from scipy.optimize import linprog

F = lambda x: x if isinstance(x, Fr) else Fr(x).limit_denominator(10**6)

# ----------------------------------------------------------------------------------------------------------------
# polynomial supports
# ----------------------------------------------------------------------------------------------------------------
def support(expr, local, m2, frozen=()):
    """exponent tuples (local..., m2) of expr, with the variables in `frozen` treated as coefficients.
    Returns list of (exps, coeff_poly_in_frozen)."""
    gens = list(local) + [m2]
    P = sp.Poly(sp.expand(expr), *gens)
    out = []
    for mon, c in zip(P.monoms(), P.coeffs()):
        c = sp.expand(c)
        if c != 0:
            out.append((tuple(int(e) for e in mon), c))
    return out

def positive_form(factor, local, m2, frozen=()):
    """support of a denominator factor; requires all coefficients (as polynomial in local, m2 AND frozen) positive."""
    gens = list(local) + [m2] + list(frozen)
    P = sp.Poly(sp.expand(factor), *gens)
    if not all(c > 0 for c in P.coeffs()):
        # allow an overall negative sign
        if all(c < 0 for c in P.coeffs()):
            pass
        else:
            raise ValueError(f"factor {factor} not sign-definite in {gens}")
    Q = sp.Poly(sp.expand(factor), *(list(local) + [m2]))
    return [tuple(int(e) for e in mon) for mon in Q.monoms()]

def comparability(factor, frozen_intervals):
    """for a positive-coefficient factor and frozen variables u in [lo,hi] (lo>0): f(u)/f(u=1) lies in
    [prod min(lo,1)^deg, prod max(hi,1)^deg].  Returns the ratio bound (upper/lower)."""
    const = Fr(1)
    for u, (lo, hi) in frozen_intervals.items():
        d = sp.Poly(sp.expand(factor), u).degree()
        const *= (max(F(hi), Fr(1))/min(F(lo), Fr(1)))**d
    return const

# ----------------------------------------------------------------------------------------------------------------
# exact LP with primal-dual optimality certificate
# ----------------------------------------------------------------------------------------------------------------
def build_lp(a, forms, w, G, h, n):
    """lifted LP:  max <a+w, X> - a_m - sum_k t_k  s.t.  <b,X> - t_k <= b_m (b in factor k),  G X <= h.
    Returns rows (list of Fraction lists), rhs, objective c, constant."""
    K = len(forms)
    rows, rhs = [], []
    for k, fl in enumerate(forms):
        for b in fl:
            row = [Fr(int(x)) for x in b[:n]] + [Fr(0)]*K
            row[n + k] = Fr(-1)
            rows.append(row); rhs.append(Fr(int(b[n])))
    for gi, hi in zip(G, h):
        rows.append([F(x) for x in gi] + [Fr(0)]*K); rhs.append(F(hi))
    c = [Fr(int(a[i])) + F(w[i]) for i in range(n)] + [Fr(-1)]*K
    const = Fr(-int(a[n]))
    return rows, rhs, c, const

def _rat(v):
    v = sp.nsimplify(v)
    num, den = sp.fraction(v)
    return Fr(int(num), int(den))

def exact_lp(rows, rhs, c, const):
    """returns dict(status, value, dim_bound, y, S, x) ; status 'ok' only for an exact primal-dual optimal pair."""
    A = np.array([[float(x) for x in r] for r in rows]); b = np.array([float(x) for x in rhs]); cc = np.array([float(x) for x in c])
    last = None
    for method in ['highs', 'highs-ds', 'highs-ipm']:
        res = linprog(-cc, A_ub=A, b_ub=b, bounds=[(None, None)]*len(cc), method=method)
        if res.status == 3:
            return dict(status='unbounded')
        if res.status != 0:
            last = res.message; continue
        yfl = -res.ineqlin.marginals
        xfl = res.x
        for tol in [1e-9, 1e-7, 1e-11]:
            S = [i for i, y in enumerate(yfl) if y > tol]
            out = _certify(rows, rhs, c, const, S, yfl, xfl)
            if out['status'] == 'ok':
                return out
            last = out['status']
    return dict(status=f'failed: {last}')

def _certify(rows, rhs, c, const, S, yfl, xfl):
    nv = len(c)
    if not S:
        if all(ci == 0 for ci in c):
            return dict(status='ok', value=const, dim_bound=nv, y={}, S=[], x=[Fr(0)]*nv)
        return dict(status='empty support')
    M = sp.Matrix([[rows[i][j] for i in S] for j in range(nv)])
    try:
        sol, params = M.gauss_jordan_solve(sp.Matrix(c))
    except ValueError:
        return dict(status='dual system inconsistent')
    if params.shape[0] > 0:
        cand = []
        fl = [Fr(float(yfl[S[i]])).limit_denominator(4096) for i in range(len(S))]
        cand.append({p: 0 for p in params})
        # free parameters: try matching floating values of the corresponding y-components
        idx = []
        for p in params:
            # parameter names are tau0, tau1,...; map to columns: free columns are those not pivots
            pass
        piv = M.rref()[1]
        free_cols = [j for j in range(len(S)) if j not in piv]
        cand.append({p: sp.Rational(fl[free_cols[k]].numerator, fl[free_cols[k]].denominator) for k, p in enumerate(params)})
        ok = None
        for sub in cand:
            s0 = sol.subs(sub)
            if all(v_ >= 0 for v_ in s0):
                ok = s0; break
        if ok is None:
            return dict(status='negative exact dual')
        sol = ok
    y = [_rat(v) for v in sol]
    if any(v < 0 for v in y):
        return dict(status='negative exact dual')
    for j in range(nv):
        if sum(rows[S[i]][j]*y[i] for i in range(len(S))) != c[j]:
            return dict(status='dual equality fails')
    dual_val = sum(rhs[S[i]]*y[i] for i in range(len(S)))
    # exact primal: tight constraints S, free parameters fixed by rounded floating primal values
    MA = sp.Matrix([[rows[i][j] for j in range(nv)] for i in S])
    try:
        xs, xp = MA.gauss_jordan_solve(sp.Matrix([rhs[i] for i in S]))
    except ValueError:
        return dict(status='primal tight system inconsistent')
    if xp.shape[0] > 0:
        piv = MA.rref()[1]
        free = [j for j in range(nv) if j not in piv]
        sub = {p: sp.Rational(Fr(float(xfl[free[k]])).limit_denominator(4096).numerator,
                              Fr(float(xfl[free[k]])).limit_denominator(4096).denominator) for k, p in enumerate(xp)}
        xs = xs.subs(sub)
    x = [_rat(v) for v in xs]
    # primal feasibility and equal objective (exact)
    for r, bb in zip(rows, rhs):
        if sum(ri*xi for ri, xi in zip(r, x)) > bb:
            return dict(status='primal infeasible')
    prim_val = sum(ci*xi for ci, xi in zip(c, x))
    if prim_val != dual_val:
        return dict(status=f'duality gap {prim_val - dual_val}')
    rank = sp.Matrix([[rows[i][j] for j in range(nv)] for i in S]).rank()
    return dict(status='ok', value=dual_val + const, dim_bound=nv - rank, y={int(S[i]): y[i] for i in range(len(S))},
                S=[int(i) for i in S], x=x)

# ----------------------------------------------------------------------------------------------------------------
# corrected 2D recession check
# ----------------------------------------------------------------------------------------------------------------
def _feasible(r, Gq):
    return all(g[0]*r[0] + g[1]*r[1] <= 0 for g in Gq)

def pointed_pieces_2d(G):
    """split the cone C = {r in R^2 : g.r <= 0 for g in G} into C cap (closed quadrant); return list of
    (r_lo, r_hi) extreme-ray pairs of the (pointed) pieces; r_lo == r_hi for a single ray."""
    G = [(F(g[0]), F(g[1])) for g in G]
    pieces = []
    for s1, s2 in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
        Gq = G + [(Fr(-s1), Fr(0)), (Fr(0), Fr(-s2))]
        cand = []
        for (a, b) in Gq:
            for sg in (1, -1):
                r = (sg*b, -sg*a)
                if (r[0] != 0 or r[1] != 0) and _feasible(r, Gq):
                    cand.append(r)
        if not cand:
            continue
        # angles within the quadrant: use a monotone parametrisation of the quadrant arc
        def ang(r):
            # map direction in quadrant (s1,s2) to t in [0,1]: t = s2*r1... use r normalised by |r|_1
            n1 = abs(r[0]) + abs(r[1])
            return Fr(abs(r[1]), 1)/n1          # 0 along the r1-axis, 1 along the r2-axis (within a quadrant)
        cand.sort(key=ang)
        pieces.append((cand[0], cand[-1]))
    return pieces

def psi_inf(a, w, forms, r):
    n = len(r)
    val = sum((Fr(int(a[i])) + F(w[i]))*r[i] for i in range(n))
    for fl in forms:
        val -= max(sum(Fr(int(b[i]))*r[i] for i in range(n)) for b in fl)
    return val

def max_rec_slope_2d(a, w, forms, G):
    """exact max of psi_inf(r)/|r|_1 over the recession cone of {G X <= h}; None if the cone is {0}."""
    pcs = pointed_pieces_2d(G)
    best = None
    for r1, r2 in pcs:
        ts = {Fr(0), Fr(1)}
        for fl in forms:
            for b1, b2 in itertools.combinations(fl, 2):
                d1 = (int(b1[0]) - int(b2[0]))*r1[0] + (int(b1[1]) - int(b2[1]))*r1[1]
                d2 = (int(b1[0]) - int(b2[0]))*r2[0] + (int(b1[1]) - int(b2[1]))*r2[1]
                if d1 != d2:
                    t = Fr(d1)/(d1 - d2)
                    if 0 <= t <= 1:
                        ts.add(t)
        for t in ts:
            r = ((1 - t)*r1[0] + t*r2[0], (1 - t)*r1[1] + t*r2[1])
            if r == (0, 0):
                continue
            val = psi_inf(a, w, forms, r)/(abs(r[0]) + abs(r[1]))
            best = val if (best is None or val > best) else best
    return best

def max_rec_slope_1d(a, w, forms, G):
    best = None
    for r in (Fr(1), Fr(-1)):
        if all(F(g[0])*r <= 0 for g in G):
            val = (Fr(int(a[0])) + F(w[0]))*r - sum(max(Fr(int(b[0]))*r for b in fl) for fl in forms)
            best = val if (best is None or val > best) else best
    return best

def max_rec_slope_lp(a, w, forms, G, n):
    """floating cross-check in any dimension: max psi_inf(d) over rec cone cap orthant cap {sum s_i d_i = 1}."""
    best = -np.inf
    K = len(forms)
    for signs in itertools.product([1, -1], repeat=n):
        cobj = np.zeros(n + K)
        cobj[:n] = -(np.array([float(a[i]) + float(w[i]) for i in range(n)]))
        cobj[n:] = 1.0
        A_ub = []; b_ub = []
        for k, fl in enumerate(forms):
            for b in fl:
                row = np.zeros(n + K); row[:n] = [float(b[i]) for i in range(n)]; row[n + k] = -1.0
                A_ub.append(row); b_ub.append(0.0)
        for g in G:
            row = np.zeros(n + K); row[:n] = [float(x) for x in g]; A_ub.append(row); b_ub.append(0.0)
        for i in range(n):
            row = np.zeros(n + K); row[i] = -signs[i]; A_ub.append(row); b_ub.append(0.0)
        A_eq = np.zeros((1, n + K)); A_eq[0, :n] = signs
        res = linprog(cobj, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=[1.0],
                      bounds=[(None, None)]*(n + K), method='highs')
        if res.status == 0:
            best = max(best, -res.fun)
        elif res.status == 3:
            return np.inf
    return best

# ----------------------------------------------------------------------------------------------------------------
# full certificate of one rational piece on one cell
# ----------------------------------------------------------------------------------------------------------------
def certify_piece(num, dens, local, m2, cons, w=None, frozen=None, label='', keep=False):
    """num: sympy numerator (frozen variables allowed, treated as coefficients); dens: list of positive-coefficient
    factors (frozen variables are compared with their value 1, constant recorded); cons: list of (g, h) for G X <= h.
    Returns dict with exact phi*, L-power bound, recession max slope, comparability constants, certificates."""
    frozen = frozen or {}
    n = len(local)
    w = w or [1]*n
    fz = list(frozen.keys())
    sup = support(num, local, m2, fz)
    if not sup:
        return dict(label=label, status='zero', phi=None)
    forms = [positive_form(f, local, m2, fz) for f in dens]
    comp = [str(comparability(f, frozen)) for f in dens] if frozen else []
    G = [g for g, _ in cons]; h = [hh for _, hh in cons]
    worst = None; dmax = 0; slope = None; certs = []
    for exps, cpoly in sup:
        rows, rhs, c, const = build_lp(exps, forms, w, G, h, n)
        out = exact_lp(rows, rhs, c, const)
        if out['status'] != 'ok':
            return dict(label=label, status=out['status'], monomial=exps)
        val = out['value']
        if n == 2:
            s = max_rec_slope_2d(exps, w, forms, G)
        elif n == 1:
            s = max_rec_slope_1d(exps, w, forms, G)
        else:
            s = max_rec_slope_lp(exps, w, forms, G, n)
        if s is not None and s >= 0:
            return dict(label=label, status=f'nonnegative recession slope {s}', monomial=exps)
        if s is not None:
            slope = s if (slope is None or s > slope) else slope
        if worst is None or val > worst:
            worst = val; dmax = out['dim_bound']
        elif val == worst:
            dmax = max(dmax, out['dim_bound'])
        if keep:
            certs.append(dict(monomial=list(exps), value=str(val), dim_bound=out['dim_bound'],
                              dual={str(k): str(v) for k, v in out['y'].items()}, primal=[str(v) for v in out['x']]))
    return dict(label=label, status='ok', phi=worst, exponent=-2*worst, Lpow=dmax, slope=slope,
                comparability=comp, nmon=len(sup), certs=certs)

if __name__ == "__main__":
    # unit test of the recession fix (the case reported in review r1_2)
    from recession import cone_rays
    print("old cone_rays for half-plane {r1 >= 0}:", cone_rays([([-1, 0], 0)]))
    print("new pointed pieces                    :", pointed_pieces_2d([[-1, 0]]))
    # psi_inf = <a+w,r> - max(...) example: a=(0,0), w=(1,1), forms: one factor with monomials (1,0),(0,1) and (1,1)
    forms = [[(1, 0, 0), (0, 1, 0)], [(1, 1, 0), (0, 0, 0)]]
    print("example max slope on half-plane r1>=0 :", max_rec_slope_2d((0, 0, 0), [1, 1], forms, [[-1, 0]]),
          " LP cross-check:", round(max_rec_slope_lp((0, 0, 0), [1, 1], forms, [[-1, 0]], 2), 6))
