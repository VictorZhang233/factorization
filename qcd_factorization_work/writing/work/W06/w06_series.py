r"""
w06_series.py -- exact, fast truncated Laurent expansion in eps (writer W06).

Handles sums/products/integer powers of: Gamma(n + c eps) (n integer, c rational), exp, cos, sin, log of
expressions regular at eps=0, symbols independent of eps, polynomials/rational functions of eps.
Gamma(n + c eps) -> rational(eps) * Gamma(1 + c eps),  ln Gamma(1+x) = -gamma_E x + sum_{k>=2} (-1)^k zeta(k) x^k/k.
Each factor of a product is expanded only to the order needed (leading powers computed first).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp


def _clean(d):
    out = {}
    for k, v in d.items():
        v = sp.expand(v)
        if v != 0:
            out[k] = v
    return out


def _mul(a, b, top):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            k = ka + kb
            if k <= top:
                out[k] = out.get(k, 0) + va * vb
    return _clean(out)


def _add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + v
    return _clean(out)


def _scale(a, c):
    return _clean({k: c * v for k, v in a.items()})


def lead(expr, eps):
    """a lower bound for the leading power (exact for the expressions used here)"""
    if not expr.has(eps):
        return 0
    if expr == eps:
        return 1
    if isinstance(expr, sp.Add):
        try:
            P = sp.Poly(expr, eps)
            return min(m[0] for m in P.monoms())
        except sp.PolynomialError:
            return min(lead(a, eps) for a in expr.args)
    if isinstance(expr, sp.Mul):
        return sum(lead(a, eps) for a in expr.args)
    if isinstance(expr, sp.Pow):
        base, ex = expr.args
        if ex.is_Integer:
            return int(ex) * exact_lead(base, eps)
        return 0
    if isinstance(expr, sp.gamma):
        arg = sp.expand(expr.args[0])
        c = arg.coeff(eps)
        n = sp.expand(arg - c * eps)
        return -1 if (n.is_Integer and n <= 0 and c != 0) else 0
    return 0


def exact_lead(expr, eps):
    if not expr.has(eps):
        return 0
    try:
        P = sp.Poly(sp.expand(expr), eps)
        return min(m[0] for m in P.monoms())
    except sp.PolynomialError:
        pass
    d = ser(expr, eps, lead(expr, eps) + 6)
    return min(d) if d else 0


def _lngamma1p(c, top):
    out = {}
    if c != 0 and top >= 1:
        out[1] = -sp.EulerGamma * c
        for k in range(2, top + 1):
            out[k] = (-1) ** k * sp.zeta(k) * c ** k / k
    return out


def _exp_series(r, top):
    """exp of a series r with r(0) handled by caller (r has only positive powers)"""
    out = {0: sp.Integer(1)}
    term = {0: sp.Integer(1)}
    for j in range(1, top + 1):
        term = _scale(_mul(term, r, top), sp.Rational(1, j))
        if not term:
            break
        out = _add(out, term)
    return out


def _inv(a, top):
    if not a:
        return {}     # requested orders lie below the leading power of 1/a
    m = min(a)
    c0 = a[m]
    r = {k - m: sp.expand(v / c0) for k, v in a.items() if k != m}
    tt = top + m
    out = {0: sp.Integer(1)}
    term = {0: sp.Integer(1)}
    mr = _scale(r, -1)
    for j in range(1, max(tt, 0) + 2):
        term = _mul(term, mr, tt)
        if not term:
            break
        out = _add(out, term)
    return _clean({k - m: v / c0 for k, v in out.items() if k - m <= top})


def ser(expr, eps, top):
    expr = sp.sympify(expr)
    if not expr.has(eps):
        return {0: expr} if (expr != 0 and top >= 0) else {}
    if expr == eps:
        return {1: sp.Integer(1)} if top >= 1 else {}
    if isinstance(expr, sp.Add):
        out = {}
        for t in expr.args:
            out = _add(out, ser(t, eps, top))
        return out
    if isinstance(expr, sp.Mul):
        args = list(expr.args)
        leads = [lead(a, eps) for a in args]
        if sum(leads) > top:
            return {}          # the product starts above the requested order
        out = {0: sp.Integer(1)}
        for i, a in enumerate(args):
            ti = top - sum(l for j, l in enumerate(leads) if j != i)
            # keep enough orders for the factors still to come (their leading powers may be negative)
            out = _mul(out, ser(a, eps, ti), top - sum(leads[i + 1:]))
        return out
    if isinstance(expr, sp.Pow):
        base, ex = expr.args
        if ex.is_Integer:
            n = int(ex)
            m = exact_lead(base, eps)
            if n >= 0:
                b = ser(base, eps, top - (n - 1) * m)
                out = {0: sp.Integer(1)}
                for kk in range(n):
                    out = _mul(out, b, top - (n - 1 - kk) * m)
                return out
            nn = abs(n)
            # 1/base has leading power -m; each factor is needed to order top + (nn-1) m
            b = ser(base, eps, top + 2 * m + (nn - 1) * m)
            inv = _inv(b, top + (nn - 1) * m)
            out = {0: sp.Integer(1)}
            for kk in range(nn):
                out = _mul(out, inv, top + (nn - 1 - kk) * m)
            return out
        return ser(sp.exp(ex * sp.log(base)), eps, top)
    if isinstance(expr, sp.exp):
        a = ser(expr.args[0], eps, top)
        assert not a or min(a) >= 0
        a0 = a.get(0, 0)
        r = {k: v for k, v in a.items() if k > 0}
        return _scale(_exp_series(r, top), sp.exp(a0))
    if isinstance(expr, sp.log):
        arg = expr.args[0]
        a = ser(arg, eps, top)
        assert min(a) == 0
        c0 = a[0]
        r = {k: sp.expand(v / c0) for k, v in a.items() if k > 0}
        out = {0: sp.log(c0)}
        term = {0: sp.Integer(1)}
        for j in range(1, top + 1):
            term = _mul(term, r, top)
            if not term:
                break
            out = _add(out, _scale(term, sp.Rational((-1) ** (j + 1), j)))
        return out
    if isinstance(expr, (sp.cos, sp.sin)):
        a = ser(expr.args[0], eps, top)
        a0 = a.get(0, 0)
        r = {k: v for k, v in a.items() if k > 0}
        csum, ssum = {0: sp.Integer(1)}, {}
        term = {0: sp.Integer(1)}
        for j in range(1, top + 1):
            term = _scale(_mul(term, r, top), sp.Rational(1, j))
            if not term:
                break
            if j % 2 == 0:
                csum = _add(csum, _scale(term, (-1) ** (j // 2)))
            else:
                ssum = _add(ssum, _scale(term, (-1) ** ((j - 1) // 2)))
        if isinstance(expr, sp.cos):
            return _add(_scale(csum, sp.cos(a0)), _scale(ssum, -sp.sin(a0)))
        return _add(_scale(csum, sp.sin(a0)), _scale(ssum, sp.cos(a0)))
    if isinstance(expr, sp.gamma):
        arg = sp.expand(expr.args[0])
        c = arg.coeff(eps)
        n = sp.expand(arg - c * eps)
        if not n.is_Integer:
            raise ValueError('Gamma(%s) not of the form n + c eps' % arg)
        n = int(n)
        x = c * eps
        if n >= 1:
            fac = sp.Integer(1)
            for j in range(1, n):
                fac *= (j + x)
            base = _exp_series(_lngamma1p(c, top), top)
            return _mul(base, ser(sp.expand(fac), eps, top), top)
        fac = sp.Integer(1)
        for j in range(n, 1):
            fac *= (j + x)
        fac = sp.expand(fac)
        m = exact_lead(fac, eps)          # 1 if c != 0 (the factor x), else 0
        base = _exp_series(_lngamma1p(c, top + m), top + m)
        inv = _inv(ser(fac, eps, top + 2 * m), top)
        return _mul(base, inv, top)
    raise ValueError('cannot expand %s' % expr)


def laurent(expr, eps, top):
    d = ser(sp.sympify(expr), eps, top)
    return sp.expand(sum(v * eps ** k for k, v in d.items()))


if __name__ == '__main__':
    import time
    e = sp.Symbol('eps'); L = sp.Symbol('L')
    t0 = time.time()
    cG = sp.gamma(1 + e) * sp.gamma(1 - e) ** 2 / sp.gamma(1 - 2 * e)
    print(laurent(cG, e, 3))
    print(laurent(sp.exp(-e * sp.EulerGamma) * sp.gamma(1 - e), e, 3))
    print(laurent(sp.gamma(e), e, 1))
    f = -(2 - e + 2 * e ** 2) / (e ** 2 * (1 - 2 * e))
    print(laurent(sp.exp(e * sp.EulerGamma) * cG * sp.exp(-e * L) * f, e, 1))
    print(laurent(sp.cos(sp.pi * e) * f, e, 0))
    print(laurent(sp.gamma(-e) ** 2 / sp.gamma(3 - 3 * e), e, 0))
    print('time %.2f s' % (time.time() - t0))
