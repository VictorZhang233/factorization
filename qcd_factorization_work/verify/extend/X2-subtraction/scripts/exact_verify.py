"""X2 / exact_verify.py -- exact (rational) re-verification of the tropical LP certificates.
For each numerator monomial a, the lifted LP  max <a+w,X> - a_m - sum_k t_k  s.t.  <b,X> - t_k <= b_m (b in factor k),
G X <= h  is solved in floating point (HiGHS); then a dual vector y >= 0 with A^T y = c is reconstructed EXACTLY:
the support of the floating dual is taken, the square/overdetermined system A_S^T y_S = c is solved in Fractions, and
y_S >= 0 is checked.  Weak duality then gives the exact upper bound  psi_a* <= b^T y - a_m  (a rational number).
Face-dimension bound: every optimal point satisfies the constraints in S with equality, so
dim(argmax) <= (n+K) - rank(A_S)  (rank computed exactly).  This bounds the power of L."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np, sympy as sp
from fractions import Fraction
from scipy.optimize import linprog

def build(a, forms, w, G, h, n):
    K = len(forms)
    rows, rhs = [], []
    for k, fl in enumerate(forms):
        for b in fl:
            row = [Fraction(int(x)) for x in b[:n]] + [Fraction(0)]*K
            row[n + k] = Fraction(-1)
            rows.append(row); rhs.append(Fraction(int(b[n])))
    for gi, hi in zip(G, h):
        rows.append([Fraction(x).limit_denominator(1000) for x in gi] + [Fraction(0)]*K)
        rhs.append(Fraction(hi).limit_denominator(1000))
    c = [Fraction(int(a[i])) + Fraction(w[i]).limit_denominator(1000) for i in range(n)] + [Fraction(-1)]*K
    const = Fraction(-int(a[n]))
    return rows, rhs, c, const

def solve_exact(rows, rhs, c, const, method='highs'):
    out = _solve_exact(rows, rhs, c, const, method)
    if out[0] is None and method == 'highs':
        for m in ['highs-ds', 'highs-ipm']:
            out2 = _solve_exact(rows, rhs, c, const, m)
            if out2[0] is not None:
                return out2
    return out

def _solve_exact(rows, rhs, c, const, method):
    A = np.array([[float(x) for x in r] for r in rows]); b = np.array([float(x) for x in rhs]); cc = np.array([float(x) for x in c])
    res = linprog(-cc, A_ub=A, b_ub=b, bounds=[(None, None)]*len(cc), method=method)
    if res.status == 3:
        return None, 'unbounded'
    if res.status != 0:
        return None, res.message
    yfl = -res.ineqlin.marginals      # duals >= 0 for the max problem
    S = [i for i, y in enumerate(yfl) if y > 1e-9]
    # exact solve A_S^T y = c  (least-squares in exact arithmetic via sympy)
    M = sp.Matrix([[rows[i][j] for i in S] for j in range(len(c))])   # (nvar x |S|)
    rhsv = sp.Matrix(c)
    try:
        sol, params = M.gauss_jordan_solve(rhsv)
    except ValueError:
        return None, 'exact dual system inconsistent'
    if params.shape[0] > 0:
        # degenerate: try setting the free parameters to the rounded floating dual values, then to 0
        free_idx = []
        sub = {}
        for p in params:
            sub[p] = 0
        sol0 = sol.subs(sub)
        if any(v_ < 0 for v_ in sol0):
            # rounded floating values for the free parameters (match by order of appearance)
            fl = [Fraction(float(yfl[S[i]])).limit_denominator(64) for i in range(len(S))]
            sub = {p: sp.Rational(fl[k].numerator, fl[k].denominator) for k, p in enumerate(params)}
            sol0 = sol.subs(sub)
        sol = sol0
    y = [Fraction(int(sp.fraction(sp.nsimplify(v))[0]), int(sp.fraction(sp.nsimplify(v))[1])) for v in sol]
    if any(v < 0 for v in y):
        return None, 'negative exact dual'
    # check A^T y = c exactly
    for j in range(len(c)):
        if sum(rows[S[i]][j]*y[i] for i in range(len(S))) != c[j]:
            return None, 'dual equality fails'
    val = sum(rhs[S[i]]*y[i] for i in range(len(S))) + const
    rank = sp.Matrix([[rows[i][j] for j in range(len(c))] for i in S]).rank() if S else 0
    return (val, len(c) - rank, -res.fun + float(const)), 'ok'
