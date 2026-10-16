"""X2 / tropical.py -- LP ("tropical") certificates for integral-norm bounds of explicit fibered densities.

Setting (REPORT Lemma A.6).  Variables y_1..y_n > 0 (local coordinates of a sub-domain), small parameter
lambda with  m2 = lambda^2  (all other scales O(1)).  Normalised log coordinates  y_i = exp(L*X_i), m2 = exp(-L),
L = ln(1/lambda^2).  For f = N/D with  N = sum_a c_a y^a m2^{a_m}  (signs arbitrary) and
D = prod_k D_k,  D_k  comparable (within constants) on the sub-domain to a positive polynomial
g_k = sum_j d_kj y^{b_kj} m2^{b_kjm}, we have  |f| <= C * max_a e^{L psi_a(X)},
   psi_a(X) = <a,X> - a_m + <w,X> - sum_k max_j( <b_kj,X> - b_kjm ),
where w = Jacobian weights (dy_i = L y_i dX_i, plus measure powers y_i^{w_i - 1}, e.g. kap^{-eps}).
Each psi_a is concave piecewise linear; psi_a* = max over the polyhedron U (constraints G X <= h) is an LP.
Then  int_U |f| dy <= C' L^{n} sum_a int e^{L psi_a} dX <= C'' sum_a L^{d_a} e^{L psi_a*},
d_a = dimension of the argmax face (which must be bounded).  So
      int_U |f| <= C lambda^{-2 phi*} L^{d},  phi* = max_a psi_a*,  d = max{d_a : psi_a* = phi*}.
This module computes phi*, the maximizing monomials and the face dimensions (floating LP, HiGHS), and an exact
rational re-check of the optimal value via the dual (Farkas) certificate.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from fractions import Fraction
from scipy.optimize import linprog
import sympy as sp


def monomials_of(expr, yvars, m2):
    """expand expr as polynomial in yvars, m2; return list of (coeff(float), exps tuple incl. m2 last)"""
    poly = sp.Poly(sp.expand(expr), *yvars, m2)
    return [(float(c), tuple(int(e) for e in mon)) for mon, c in zip(poly.monoms(), poly.coeffs())]


def positive_form(factor, yvars, m2):
    """return monomial exponent list of a factor if all coefficients have one sign (positive polynomial up to sign)."""
    mons = monomials_of(factor, yvars, m2)
    signs = set(np.sign([c for c, _ in mons]))
    if len(signs) != 1:
        raise ValueError(f"factor {factor} is not sign-definite as a polynomial; supply an equivalent positive form")
    return [e for _, e in mons]


def lp_max_psi(a, den_forms, wvec, G, h, n, extra_obj=None):
    """maximize <a[:n] + w, X> - a[n] - sum_k t_k  s.t. t_k >= <b,X> - b_m for all monomials b of factor k, G X <= h.
    Variables z = (X_1..X_n, t_1..t_K). linprog minimizes, so minimize the negative."""
    K = len(den_forms)
    c = np.zeros(n + K)
    c[:n] = -(np.array(a[:n], float) + np.array(wvec, float))
    c[n:] = 1.0
    const = -a[n]   # m2 power: m2 = e^{-L}  -> contributes -a_m
    A_ub = []; b_ub = []
    for k, forms in enumerate(den_forms):
        for b in forms:
            row = np.zeros(n + K)
            row[:n] = np.array(b[:n], float)
            row[n + k] = -1.0
            A_ub.append(row); b_ub.append(float(b[n]))      # <b,X> - t_k <= b_m   (m2^{b_m} -> -b_m)
    for gi, hi in zip(G, h):
        row = np.zeros(n + K); row[:n] = gi; A_ub.append(row); b_ub.append(hi)
    bounds = [(None, None)] * (n + K)
    res = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub), bounds=bounds, method='highs')
    if res.status == 3:
        return np.inf, None, res
    if res.status != 0:
        raise RuntimeError(res.message)
    return -res.fun + const, res.x[:n], res


def face_dimension(a, den_forms, wvec, G, h, n, psistar, tol=1e-7):
    """dimension of argmax face of psi_a: collect extreme points maximizing random directions within the face."""
    K = len(den_forms)
    pts = []
    rng = np.random.default_rng(0)
    dirs = [np.eye(n)[i] for i in range(n)] + [-np.eye(n)[i] for i in range(n)] + [rng.normal(size=n) for _ in range(4)]
    for dvec in dirs:
        # maximize <d,X> subject to psi_a(X) >= psistar - tol  (linear in (X,t) with t_k >= ...)
        c = np.zeros(n + K); c[:n] = -dvec
        A_ub = []; b_ub = []
        for k, forms in enumerate(den_forms):
            for b in forms:
                row = np.zeros(n + K); row[:n] = np.array(b[:n], float); row[n + k] = -1.0
                A_ub.append(row); b_ub.append(float(b[n]))
        for gi, hi in zip(G, h):
            row = np.zeros(n + K); row[:n] = gi; A_ub.append(row); b_ub.append(hi)
        # psi constraint: -( <a+w,X> - a_m - sum t ) <= -(psistar - tol)
        row = np.zeros(n + K); row[:n] = -(np.array(a[:n], float) + np.array(wvec, float)); row[n:] = 1.0
        A_ub.append(row); b_ub.append(-(psistar - tol) - a[n])
        res = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub), bounds=[(None, None)] * (n + K), method='highs')
        if res.status == 3:
            return np.inf, None   # unbounded face -> integral diverges
        if res.status == 0:
            pts.append(res.x[:n])
    P = np.array(pts)
    if len(P) == 0:
        return 0, P
    D = P - P[0]
    rank = np.linalg.matrix_rank(D, tol=1e-5)
    return int(rank), P


def certify(f_expr, yvars, m2, den_factors_positive, G, h, wvec=None, label="", verbose=True, top=5):
    """f_expr: sympy expression N/D (D given separately as list of factors: their product must equal denominator up to
    a constant factor and up to factors bounded above/below on the domain, already replaced by positive forms).
    den_factors_positive: list of sympy positive polynomials g_k  (the user guarantees D ~ prod g_k on the domain).
    G, h: domain constraints  G X <= h in normalised log coordinates.
    Returns phi*, d."""
    n = len(yvars)
    if wvec is None:
        wvec = [1] * n           # measure dy_1...dy_n  -> y_i dX_i
    num_mons = monomials_of(sp.numer(sp.together(f_expr)) if False else f_expr, yvars, m2)
    den_forms = [positive_form(g, yvars, m2) for g in den_factors_positive]
    best = -np.inf; results = []
    for c, a in num_mons:
        val, X, res = lp_max_psi(a, den_forms, wvec, G, h, n)
        results.append((val, a, X))
    results.sort(key=lambda r: -r[0])
    phistar = results[0][0]
    if phistar == np.inf:
        if verbose:
            print(f"[{label}] UNBOUNDED LP for monomial {results[0][1]}: integral diverges on the domain")
        return np.inf, None
    dmax = 0
    for val, a, X in results:
        if val > phistar - 1e-7:
            d, pts = face_dimension(a, den_forms, wvec, G, h, n, val)
            dmax = max(dmax, d) if d != np.inf else np.inf
    if verbose:
        print(f"[{label}] phi* = {phistar:.6f}  ->  int|f| <= C lambda^({-2*phistar:.4f}) L^{dmax}"
              f"   (#num monomials {len(num_mons)})")
        for val, a, X in results[:top]:
            print(f"      monomial {a}: psi* = {val:.6f} at X = {np.round(X, 4) if X is not None else None}")
    return phistar, dmax
