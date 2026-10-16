"""X2 final revision / r3_lptools.py -- r2_lptools.certify_piece with SELF-CONTAINED archiving (reviews r3_1 required
fix 8, r3_2 required fix 7): every piece record now also stores the data from which each LP is built, so that the exact
primal-dual certificates can be re-verified from the archive alone (r3_archive_verify.py, which does not import
r1/r2/r3_lptools):
    'num'          numerator (sympy string; frozen variables appear as symbols),
    'dens'         denominator factors (sympy strings),
    'local'        local variables y_i = exp(L X_i), 'm2' symbol name, 'frozen' {var: [lo, hi]},
    'weights'      measure weights w_i (kappa weight 1 - eps),
    'cons'         cell constraints G X <= h (log coordinates, units of L),
    'num_support'  [[exponents (local..., m2)], coefficient polynomial in the frozen variables (string)],
    'forms'        supports of the denominator factors (exponent tuples over (local..., m2)),
    'comparability' constants of the frozen-variable comparison (one per factor).
The LP for a numerator monomial a is (r2_lptools.build_lp):
    max <a+w, X> - a_m - sum_k t_k   s.t.   <b, X> - t_k <= b_m  (b in forms[k]),   G X <= h,
with variables (X_1..X_n, t_1..t_K); the certified value phi_a gives the bound lambda^{-2 phi*}, phi* = max_a phi_a."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
import r2_lptools as R2

def certify_piece(num, dens, local, m2, cons, w=None, frozen=None, label='', keep=True):
    frozen = frozen or {}
    out = R2.certify_piece(num, dens, local, m2, cons, w=w, frozen=frozen, label=label, keep=keep)
    n = len(local)
    w = w or [1]*n
    fz = list(frozen.keys())
    try:
        sup = R2.support(num, local, m2, fz)
        forms = [R2.positive_form(f, local, m2, fz) for f in dens]
    except Exception as exc:          # zero numerator or failed piece: record what exists
        sup, forms = [], []
    out['lpdata'] = dict(
        num=str(sp.expand(num)), dens=[str(sp.expand(f)) for f in dens], local=[str(z) for z in local], m2=str(m2),
        frozen={str(k): [str(v[0]), str(v[1])] for k, v in frozen.items()}, weights=[str(z) for z in w],
        cons=[[[str(z) for z in g], str(h)] for g, h in cons],
        num_support=[[list(e), str(c)] for e, c in sup], forms=[[list(b) for b in fl] for fl in forms],
        comparability=out.get('comparability', []))
    return out
