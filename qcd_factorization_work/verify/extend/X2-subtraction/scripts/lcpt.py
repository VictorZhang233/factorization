"""X2 / lcpt.py -- vectorized iterated-residue engine ("light-cone ordered" fibered densities).

An integrand is a product of factors  F_j = (a_j + sum_i b_ji * km_i - i*eta*w_j)^(-e_j),  e_j in {+1 (propagator), -1 (numerator)},
linear in the minus components km_1..km_Lp of the loop momenta.  The coefficients a_j, b_ji are numpy arrays over a batch of
base points (k_i^+, k_iT).  The iterated integral  int dkm_1 ... dkm_Lp  prod F_j  is evaluated exactly by residues,
closing each contour in the upper half plane, with the infinitesimal imaginary parts tracked linearly:
substituting the pole of factor f (variable i) into factor g:  a_g -> a_g - b_gi a_f/b_fi,  b_g -> b_g - b_gi b_f/b_fi,
w_g -> w_g - (b_gi/b_fi) w_f.  A pole of factor f in variable i lies in the upper half plane iff  w_f / b_fi > 0.
Only simple poles are supported (a factor appearing twice must be split, e.g. by a tiny regulator).
Decay at infinity (net degree <= -2 in each variable at each stage) is checked and a ValueError raised if violated.
Returns  I = int prod_i dkm_i  prod_j F_j   (no 1/(2 pi) or i factors removed:  I = (2 pi i)^{#} * sum of residues).
"""
import numpy as np

class Factor:
    __slots__ = ('a', 'b', 'w', 'e')
    def __init__(self, a, b, w, e=1):
        self.a = a; self.b = list(b); self.w = w; self.e = e
    def copy(self):
        return Factor(self.a, list(self.b), self.w, self.e)

def _is_zero(x):
    return np.all(np.asarray(x) == 0)

def iterated_residue(factors, nvar, order=None, tol=0.0):
    """factors: list of Factor with arrays a (shape (N,)), b list of nvar arrays/scalars, w scalar (generic positive).
    Returns complex array (N,)."""
    if order is None:
        order = list(range(nvar))
    return _integrate(factors, order)

def _integrate(factors, order):
    if not order:
        out = 1.0
        for f in factors:
            out = out * (f.a.astype(complex) if hasattr(f.a, 'astype') else complex(f.a))**(-f.e)
        return out
    i = order[0]
    rest = order[1:]
    # degree in variable i: count factors with b_i not identically zero (weighted by -e)
    deg = 0
    for f in factors:
        if not _is_zero(f.b[i]):
            deg -= f.e
    if deg > -2:
        raise ValueError(f"insufficient decay in variable {i}: degree {deg}")
    # classify poles per point; close on the side with fewer poles (exact zero if one side is empty)
    cand = []
    for fi, f in enumerate(factors):
        if f.e != 1 or _is_zero(f.b[i]):
            continue
        bfi = np.asarray(f.b[i], float)
        with np.errstate(divide='ignore', invalid='ignore'):
            safe_b = np.where(bfi == 0, 1.0, bfi)
            up = ((np.asarray(f.w) / safe_b) > 0) & (bfi != 0)
            lo = ((np.asarray(f.w) / safe_b) < 0) & (bfi != 0)
        cand.append((fi, f, bfi, safe_b, up, lo))
    nup = sum(c[4].astype(int) for c in cand) if cand else 0
    nlo = sum(c[5].astype(int) for c in cand) if cand else 0
    use_up = (nup <= nlo)
    nonzero = (np.asarray(nup) > 0) & (np.asarray(nlo) > 0)
    total = 0.0
    for (fi, f, bfi, safe_b, up, lo) in cand:
        sel_up = up & use_up & nonzero
        sel_lo = lo & (~use_up) & nonzero
        if not (np.any(sel_up) or np.any(sel_lo)):
            continue
        newf = []
        for gj, g in enumerate(factors):
            if gj == fi:
                continue
            ratio = np.asarray(g.b[i], float) / safe_b if not _is_zero(g.b[i]) else 0.0
            a2 = g.a - ratio * f.a
            b2 = [ (g.b[k] - ratio * f.b[k]) if k != i else 0.0 for k in range(len(g.b)) ]
            w2 = g.w - ratio * f.w
            newf.append(Factor(a2, b2, w2, g.e))
        sub = _integrate(newf, rest)
        contrib = 2j*np.pi * sub / safe_b
        total = total + np.where(sel_up, contrib, 0.0) - np.where(sel_lo, contrib, 0.0)
    return total
