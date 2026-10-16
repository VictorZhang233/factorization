"""W09 helper library: explicit 4x4 Dirac algebra (numpy), light-front helpers, and a small
D-dimensional symbolic trace routine (sympy) for traces of slashed vectors with contracted
Lorentz indices handled through the D-dimensional contraction identities.

Conventions (WRITER_SPEC_v2 Sec. 3): metric (+,-,-,-); v^pm = (v^0 pm v^3)/sqrt2;
v.w = v^+ w^- + v^- w^+ - v_T.w_T;  gamma_5 = i g0 g1 g2 g3;  epsilon^{0123} = +1.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import itertools

I2 = np.eye(2, dtype=complex)
Z2 = np.zeros((2, 2), dtype=complex)
SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex),
       np.array([[1, 0], [0, -1]], complex)]
# Dirac representation
G0 = np.block([[I2, Z2], [Z2, -I2]])
GI = [np.block([[Z2, s], [-s, Z2]]) for s in SIG]
G = [G0] + GI                      # gamma^mu, upper index
ETA = np.diag([1.0, -1.0, -1.0, -1.0])
G5 = 1j * G[0] @ G[1] @ G[2] @ G[3]
GPLUS = (G[0] + G[3]) / np.sqrt(2)  # gamma^+
GMINUS = (G[0] - G[3]) / np.sqrt(2)  # gamma^-
ONE4 = np.eye(4, dtype=complex)


def lc_to_cart(vp, vm, vx, vy):
    """(v^+, v^-, v_x, v_y) -> (v^0, v^1, v^2, v^3)."""
    return np.array([(vp + vm) / np.sqrt(2), vx, vy, (vp - vm) / np.sqrt(2)], dtype=complex)


def plus(v):
    return (v[0] + v[3]) / np.sqrt(2)


def minus(v):
    return (v[0] - v[3]) / np.sqrt(2)


def dot(a, b):
    return a[0] * b[0] - a[1] * b[1] - a[2] * b[2] - a[3] * b[3]


def lower(v):
    return ETA @ v


def sl(p):
    """slashed p = gamma^mu p_mu."""
    pl = lower(p)
    return sum(G[m] * pl[m] for m in range(4))


def eps4(mu, nu, rho, sig):
    """Levi-Civita with upper indices, epsilon^{0123} = +1."""
    perm = [mu, nu, rho, sig]
    if len(set(perm)) < 4:
        return 0
    # parity of permutation
    p = list(perm); s = 1
    for i in range(4):
        while p[i] != i:
            j = p[i]; p[i], p[j] = p[j], p[i]; s = -s
    return s


def spinors_massless_z(pplus):
    """Helicity spinors u(p,h) for a massless momentum along +z (p^- = 0, p_T = 0),
    normalised to ubar gamma^mu u = 2 p^mu.  Returns dict h -> u, h = +1/2, -1/2."""
    E = pplus / np.sqrt(2)   # p^0 = p^3 = E
    out = {}
    for h, chi in ((+0.5, np.array([1, 0], complex)), (-0.5, np.array([0, 1], complex))):
        # Dirac rep: u = sqrt(E) (chi, 2h chi) for massless along z (sigma_z chi = 2h chi)
        out[h] = np.sqrt(E) * np.concatenate([chi, 2 * h * chi])
    return out


def vspinors_massless_z(pplus):
    """v(p,h) = C ubar^T convention-free construction: v(p,h) with vbar gamma^mu v = 2 p^mu."""
    E = pplus / np.sqrt(2)
    out = {}
    for h, eta in ((+0.5, np.array([0, 1], complex)), (-0.5, np.array([1, 0], complex))):
        # v for massless along z: v = sqrt(E) (sigma.p_hat eta', eta') style; use v = gamma5 u-type
        out[h] = np.sqrt(E) * np.concatenate([-2 * h * eta, eta])
    return out


def bar(u):
    return u.conj() @ G0


# ----------------------------------------------------------------------------------------
# D-dimensional symbolic traces.  We represent a product of gamma matrices as a list whose
# entries are either ('v', name) for a slashed vector or ('i', label) for gamma^mu with a
# Lorentz index label; repeated labels are contracted (D-dimensional metric).
# The trace of 2n gamma matrices is computed recursively:
#   Tr(a1 a2 ... a2n) = sum_{k=2}^{2n} (-1)^k g(a1,ak) Tr(a2 .. ^ak .. a2n),  Tr(1) = 4.
# g(v,w) = v.w (symbol), g(v, mu) = v^mu (index object), g(mu,nu) = metric.
# After expansion, contracted index pairs are eliminated: g^mu_mu = D, v^mu w_mu = v.w,
# g^{mu nu} v_nu = v^mu.
import sympy as sp

D = sp.Symbol('D')


class Term:
    """coefficient * product of 'factors'; factors are tuples ('dot', a, b) with a<=b names,
    ('vec', name, idx), ('met', idx1, idx2)."""
    pass


def _g(a, b):
    """metric contraction of two slots a, b -> factor tuple."""
    ta, tb = a[0], b[0]
    if ta == 'v' and tb == 'v':
        x, y = sorted([a[1], b[1]])
        return ('dot', x, y)
    if ta == 'v' and tb == 'i':
        return ('vec', a[1], b[1])
    if ta == 'i' and tb == 'v':
        return ('vec', b[1], a[1])
    x, y = sorted([a[1], b[1]])
    return ('met', x, y)


def _trace_raw(slots):
    """returns list of (coef, [factors])"""
    n = len(slots)
    if n == 0:
        return [(4, [])]
    if n % 2 == 1:
        return []
    out = []
    a1 = slots[0]
    for k in range(1, n):
        sign = (-1) ** (k - 1)
        rest = slots[1:k] + slots[k + 1:]
        f = _g(a1, slots[k])
        for c, fs in _trace_raw(rest):
            out.append((sign * c, [f] + fs))
    return out


def _contract(factors):
    """Contract repeated indices among factors; returns (coef, remaining factors) or None."""
    fs = list(factors)
    coef = sp.Integer(1)
    changed = True
    while changed:
        changed = False
        # find an index appearing twice
        idx_count = {}
        for f in fs:
            if f[0] == 'vec':
                idx_count.setdefault(f[2], []).append(f)
            elif f[0] == 'met':
                idx_count.setdefault(f[1], []).append(f)
                idx_count.setdefault(f[2], []).append(f)
        for idx, lst in idx_count.items():
            # metric with itself g^mu_mu
            for f in lst:
                if f[0] == 'met' and f[1] == f[2] == idx:
                    fs.remove(f); coef *= D; changed = True; break
            if changed:
                break
            if len(lst) == 2:
                f1, f2 = lst
                fs.remove(f1); fs.remove(f2)
                # combine
                def other(f):
                    if f[0] == 'vec':
                        return ('v', f[1])
                    return ('i', f[2] if f[1] == idx else f[1])
                o1, o2 = other(f1), other(f2)
                fs.append(_g(o1, o2))
                changed = True
                break
    return coef, fs


def dtrace(slots, dots):
    """D-dim trace of slots (list of ('v',name) / ('i',label)); all index labels must be
    contracted in pairs.  dots: dict (a,b)->sympy expr for a.b (a<=b sorted)."""
    res = sp.Integer(0)
    for c, fs in _trace_raw(slots):
        cc, rem = _contract(fs)
        val = sp.Integer(c) * cc
        for f in rem:
            if f[0] != 'dot':
                raise ValueError('uncontracted index: %s' % (f,))
            key = (f[1], f[2])
            val *= dots[key]
        res += val
    return sp.expand(res)


def check_dtrace_selftest():
    """self tests: gamma^mu pslash gamma_mu = -(D-2) pslash etc. via traces."""
    p, q, r, s = sp.symbols('p q r s')
    dots = {}
    names = ['p', 'q', 'r', 's']
    syms = {}
    for i, a in enumerate(names):
        for b in names[i:]:
            dots[(a, b)] = sp.Symbol('%s%s' % (a, b))
    # Tr(gamma^mu p gamma_mu q) = -(D-2) Tr(p q) = -(D-2) 4 p.q
    t = dtrace([('i', 'm'), ('v', 'p'), ('i', 'm'), ('v', 'q')], dots)
    ok1 = sp.simplify(t + (D - 2) * 4 * dots[('p', 'q')]) == 0
    # Tr(gamma^mu p q gamma_mu r s) = 4 p.q Tr(r s) - (4-D) Tr(p q r s)
    t2 = dtrace([('i', 'm'), ('v', 'p'), ('v', 'q'), ('i', 'm'), ('v', 'r'), ('v', 's')], dots)
    trpqrs = 4 * (dots[('p', 'q')] * dots[('r', 's')] - dots[('p', 'r')] * dots[('q', 's')] + dots[('p', 's')] * dots[('q', 'r')])
    ok2 = sp.simplify(t2 - (4 * dots[('p', 'q')] * 4 * dots[('r', 's')] - (4 - D) * trpqrs)) == 0
    return ok1 and ok2


if __name__ == '__main__':
    print('dtrace self-test:', check_dtrace_selftest())
    # Clifford check
    ok = all(np.allclose(G[m] @ G[n] + G[n] @ G[m], 2 * ETA[m, n] * ONE4) for m in range(4) for n in range(4))
    print('Clifford:', ok)
    print('Tr(g^0g^1g^2g^3g5) = -4i eps^{0123}:', np.isclose(np.trace(G[0] @ G[1] @ G[2] @ G[3] @ G5), -4j))
