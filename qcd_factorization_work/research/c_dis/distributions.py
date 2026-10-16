"""
distributions.py -- canonical representation of distributions on z in [0,1] of the form

     dist = delta * delta(1-z) + sum_k plus[k] * [ ln^k(1-z)/(1-z) ]_+ + reg(z)

with constant coefficients delta, plus[k] (independent of z) and a locally integrable regular
function reg(z).  (Any smooth-function multiple A(z)[g]_+ is brought to this canonical form via
A(z)[g]_+ = A(1)[g]_+ + (A(z)-A(1)) g(z).)   Plus prescription (binding convention):
     int_0^1 dz [g]_+ h(z) = int_0^1 dz g(z) [h(z) - h(1)].
Also: Laurent expansion in eps of  (1-z)^(-1-eps) * G(z,eps)  with G regular at z = 1.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

z, eps = sp.symbols('z epsilon')
L1 = sp.log(1 - z)


def clean(e):
    """exact simplification incl. polygamma at half-integers:
       psi(1/2) = -gE - 2 ln 2,  psi^(m)(1/2) = (-1)^(m+1) m! (2^(m+1)-1) zeta(m+1)  (m>=1),
       psi^(m)(x+1) = psi^(m)(x) + (-1)^m m!/x^(m+1)."""
    e = sp.sympify(e)

    def pg(m, x):
        m = int(m)
        n = x - sp.Rational(1, 2)
        if m == 0:
            val = -sp.EulerGamma - 2 * sp.log(2)
        else:
            val = (-1) ** (m + 1) * sp.factorial(m) * (2 ** (m + 1) - 1) * sp.zeta(m + 1)
        xx = sp.Rational(1, 2)
        for _ in range(int(n)):
            val += (-1) ** m * sp.factorial(m) / xx ** (m + 1)
            xx += 1
        return val
    e = e.replace(lambda t: isinstance(t, sp.polygamma) and t.args[1].is_Rational and
                  t.args[1].q == 2 and t.args[1] > 0,
                  lambda t: pg(t.args[0], t.args[1]))
    return sp.simplify(sp.expand_func(e))


class Dist:
    def __init__(self, delta=0, plus=None, reg=0):
        self.delta = sp.sympify(delta)
        self.plus = {k: sp.sympify(v) for k, v in (plus or {}).items()}
        self.reg = sp.sympify(reg)

    def __add__(self, o):
        pl = dict(self.plus)
        for k, v in o.plus.items():
            pl[k] = pl.get(k, 0) + v
        return Dist(self.delta + o.delta, pl, self.reg + o.reg)

    def __sub__(self, o):
        return self + o.scale(-1)

    def scale(self, c):
        return Dist(c * self.delta, {k: c * v for k, v in self.plus.items()}, c * self.reg)

    def simplify(self):
        cl = clean
        pl = {k: cl(v) for k, v in self.plus.items()}
        pl = {k: v for k, v in pl.items() if v != 0}
        return Dist(cl(self.delta), pl, cl(self.reg))

    def is_zero(self, numeric_check=True):
        d = self.simplify()
        ok = d.delta == 0 and all(v == 0 for v in d.plus.values())
        r = sp.simplify(sp.expand_log(d.reg, force=True))
        if r != 0 and numeric_check:
            # robust numerical test of the regular part at a few points
            subs = {sym: sp.Rational(7, 3) + i for i, sym in enumerate(sorted(d.reg.free_symbols - {z}, key=str))}
            mp.mp.dps = 50
            f = sp.lambdify(z, d.reg.subs(subs), 'mpmath')
            vals = [abs(f(mp.mpf(t))) for t in ('0.013', '0.137', '0.5', '0.731', '0.977')]
            r = 0 if max(vals) < mp.mpf('1e-35') else r
        return ok and r == 0

    def mellin(self, N, prec=40):
        """int_0^1 dz z^(N-1) dist(z), numerically with mpmath (N may be complex/real)."""
        mp.mp.dps = prec
        res = mp.mpf(0)
        res += mp.mpf(sp.N(self.delta, prec)) if self.delta != 0 else 0
        for k, c in self.plus.items():
            ck = mp.mpf(sp.N(c, prec))
            res += ck * mp.quad(lambda t: (t ** (N - 1) - 1) * mp.log(1 - t) ** k / (1 - t), [0, 0.5, 1])
        if self.reg != 0:
            f = sp.lambdify(z, self.reg, 'mpmath')
            res += mp.quad(lambda t: t ** (N - 1) * f(t), [0, 0.5, 1])
        return res

    def latex(self):
        parts = []
        for k in sorted(self.plus):
            g = r'\frac{1}{1-z}' if k == 0 else (r'\frac{\ln(1-z)}{1-z}' if k == 1 else
                                                   r'\frac{\ln^{%d}(1-z)}{1-z}' % k)
            parts.append('(' + sp.latex(self.plus[k]) + r')\left[' + g + r'\right]_+')
        if self.reg != 0:
            parts.append('(' + sp.latex(self.reg) + ')')
        if self.delta != 0:
            parts.append('(' + sp.latex(self.delta) + r')\,\delta(1-z)')
        return ' + '.join(parts) if parts else '0'

    def __repr__(self):
        return f'Dist(delta={self.delta}, plus={self.plus}, reg={self.reg})'


def expand_singular(G, order_max=0, kmax=3):
    """
    Laurent-expand  (1-z)^(-1-eps) * G(z,eps)  (G regular at z=1, at most poles in eps)
    as a distribution, returning {n: Dist} for eps^n, n <= order_max.
    Uses (1-z)^(-1-eps) = -(1/eps) delta(1-z) + sum_k (-eps)^k/k! [ln^k(1-z)/(1-z)]_+ .
    """
    G1 = sp.simplify(G.subs(z, 1))
    lowest = -3
    ser1 = sp.series(G1, eps, 0, order_max + 3).removeO()
    serz = sp.series(G, eps, 0, order_max + 2).removeO()
    out = {n: Dist() for n in range(lowest, order_max + 1)}
    # delta term: -G(1,eps)/eps
    dl = sp.expand(-ser1 / eps)
    for n in range(lowest, order_max + 1):
        out[n].delta += dl.coeff(eps, n)
    # plus terms
    for k in range(0, kmax + 1):
        pref = (-eps) ** k / sp.factorial(k)
        A1 = sp.expand(pref * ser1)
        Az = sp.expand(pref * serz)
        for n in range(lowest, order_max + 1):
            c1 = A1.coeff(eps, n)
            cz = Az.coeff(eps, n)
            if c1 != 0:
                out[n].plus[k] = out[n].plus.get(k, 0) + c1
            if cz != 0 or c1 != 0:
                out[n].reg += (cz - c1) * L1 ** k / (1 - z)
    return out


def expand_regular(F, order_max=0):
    """Laurent expansion of a regular (integrable) function F(z,eps)."""
    ser = sp.series(F, eps, 0, order_max + 1).removeO()
    ser = sp.expand(ser)
    return {n: Dist(reg=ser.coeff(eps, n)) for n in range(-3, order_max + 1)}
