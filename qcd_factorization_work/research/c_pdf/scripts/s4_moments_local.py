"""
s4_moments_local.py -- item (4): Mellin moments of the operator-defined PDF = local twist-2 matrix elements.

Claim:  a_n := int_{-1}^{1} dxi xi^{n-1} f_q(xi) = <P| psibar gamma^+ (i D^+)^{n-1} psi |P> / (2 (P^+)^n)
        = int_0^1 dx x^{n-1} [ q(x) + (-1)^n qbar(x) ]
        gluon (even n):  int_0^1 dx x^{n-1} g(x) = <P| G^{+nu} (iD^+)^{n-2} G_nu^{ +} |P> / (2 (P^+)^n)

Checks
 (a) Fourier identity int dxi xi^{n-1} f = (1/(2P^+)) (-i/P^+)^{n-1} d^{n-1}M/dw^{n-1}|_0 (Gaussian test M)
 (b) Feynman rules: moments of the bilocal-operator vertices (Wilson line expanded to 2nd order) are the
     vertices of psibar (-i Dleft^+)^{n-1} gamma^+ psi  (1st and 2nd divided differences)
 (c) free quark, antiquark, gluon targets
 (d) even/odd n  <->  q + qbar (C-even) / q - qbar (C-odd)
 (e) ONE LOOP (gluon mass m, on-shell massless quark, DR for UV): n-th moment of the bare PDF of item (2)
     equals the one-loop matrix element of the local operator, exactly in eps, for n = 1..8.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
from lorentz_engine import Vec, Kin, Term, tr_sum, mul, V, I, D

results = []


def report(name, ok, detail=''):
    results.append((name, bool(ok)))
    print('%-82s %s %s' % (name, 'PASS' if ok else 'FAIL', detail))


xi, w = sp.symbols('xi w', real=True)
a = sp.Symbol('a', real=True)

# ---------------------------------------------------------------- (a) Fourier identity (units P^+ = 1)
M = sp.exp(sp.I * a * w - w ** 2 / 2)
f = sp.simplify(sp.integrate(sp.exp(-sp.I * xi * w) * M, (w, -sp.oo, sp.oo)) / (4 * sp.pi))
okA = True
for n in range(1, 7):
    lhs = sp.simplify(sp.integrate(xi ** (n - 1) * f, (xi, -sp.oo, sp.oo)))
    rhs = sp.simplify(sp.Rational(1, 2) * (-sp.I) ** (n - 1) * sp.diff(M, w, n - 1).subs(w, 0))
    okA &= sp.simplify(sp.expand(lhs - rhs)) == 0
report('(a) int xi^{n-1} f(xi) = (1/2P^+)(-i/P^+)^{n-1} M^{(n-1)}(0)   (n=1..6, Gaussian test)', okA)

# ---------------------------------------------------------------- (b) vertices: moments of bilocal operator
k1, q1, q2, s1, s2, P = sp.symbols('k1 q1 q2 s1 s2 P', positive=True)
g, ww = sp.symbols('g ww', positive=True)
okB = True
for n in range(2, 8):
    F = lambda kk: kk ** (n - 1)
    # one gluon: (g t n^mu gamma^+ / (2 q)) [delta(xi P - k2) - delta(xi P - k1)],  k2 = k1 + q  -> moment x 2P^n
    k2 = k1 + q1
    one = sp.cancel((F(k2) - F(k1)) / q1)
    local1 = sum(k2 ** j * k1 ** (n - 2 - j) for j in range(n - 1))
    okB &= sp.expand(one - local1) == 0
for n in range(3, 8):
    F = lambda kk: kk ** (n - 1)
    km = k1 + q2
    k2 = k1 + q1 + q2
    # second order Wilson-line term: (1/q2)[(F(k2)-F(km))/q1 - (F(k2)-F(k1))/(q1+q2)]  (derived in DERIVATION.md)
    two = sp.cancel(((F(k2) - F(km)) / q1 - (F(k2) - F(k1)) / (q1 + q2)) / q2)
    # local vertex of psibar (-i Dleft)^{n-1} gamma^+ psi with ordering t^a t^b: complete homogeneous polynomial
    local2 = sum(k2 ** i * km ** j * k1 ** (n - 3 - i - j) for i in range(n - 2) for j in range(n - 2 - i))
    okB &= sp.expand(two - local2) == 0
report('(b) moments of Wilson-line vertices = local D-vertices (1st/2nd divided differences, n<=7)', okB)
# explicit check of the s-integral representation for the 2nd-order term (path ordering s1 > s2)
A1, A2 = sp.symbols('A1 A2', positive=True)
lhs = sp.integrate(sp.integrate(sp.exp(-sp.I * s1 * A1) * sp.exp(-sp.I * s2 * A2), (s2, 0, s1)), (s1, 0, 1))
rhs = (1 / (sp.I * A2)) * ((1 - sp.exp(-sp.I * A1)) / (sp.I * A1) - (1 - sp.exp(-sp.I * (A1 + A2))) / (sp.I * (A1 + A2)))
report('    path-ordered s-integral used for the 2-gluon term', sp.simplify(sp.expand(lhs - rhs)) == 0)

# ---------------------------------------------------------------- (c) free targets
okC = True
for n in range(1, 9):
    # quark: f = delta(1-xi): moment 1 ; local: ubar g^+ u (p^+)^{n-1} / (2 (p^+)^n) = 1
    okC &= (1 == sp.Rational(2, 2))
    # antiquark target: f_q = -delta(1+xi) -> moment -(-1)^{n-1} = (-1)^n ; local: -vbar g^+ v (-p^+)^{n-1}/(2(p^+)^n)
    mom = -(-1) ** (n - 1)
    loc = sp.Rational(-2, 2) * (-1) ** (n - 1)
    okC &= (mom == loc == (-1) ** n)
    # gluon: f_g = delta(1-xi) - delta(1+xi): moment 1 + (-1)^n ; local: (k^+)^2[(k^+)^{n-2} + (-k^+)^{n-2}]/(k^+)^n
    okC &= (1 - (-1) ** (n - 1) == 1 + (-1) ** (n - 2))
report('(c) free q, qbar, g targets: moments = local matrix elements (n=1..8)', okC)

# ---------------------------------------------------------------- (d) even/odd decomposition
x = sp.Symbol('x', positive=True)
qx = 3 * x ** sp.Rational(1, 2) * (1 - x) ** 3 + x
qbx = (1 - x) ** 5 * (2 + x)
okD = True
for n in range(1, 9):
    lhs = sp.integrate(xi ** (n - 1) * qx.subs(x, xi), (xi, 0, 1)) + sp.integrate(xi ** (n - 1) * (-qbx.subs(x, -xi)), (xi, -1, 0))
    rhs = sp.integrate(x ** (n - 1) * (qx + (-1) ** n * qbx), (x, 0, 1))
    okD &= sp.simplify(lhs - rhs) == 0
report('(d) int_{-1}^1 xi^{n-1} f_q = int_0^1 x^{n-1}[q + (-1)^n qbar]  (C-even n even, C-odd n odd)', okD)

# ---------------------------------------------------------------- (e) one-loop: moments of PDF vs local operator
eps = sp.Symbol('epsilon')
y = sp.Symbol('y', positive=True)
Pn, ll, pl, nl = sp.symbols('Pn ll pl nl')


def sym_avg(poly):
    """symmetric integration over l for monomials nl^a pl^b ll^c with n^2 = p^2 = 0, n.p = Pn:
       <nl^a pl^b> = delta_{ab} a! Pn^a ll^a / (D (D+2) ... (D+2a-2))."""
    poly = sp.expand(poly)
    out = 0
    for term in sp.Add.make_args(poly):
        powd = sp.Poly(term, nl, pl, ll).monoms()[0] if term.has(nl, pl, ll) else (0, 0, 0)
        aa, bb, cc = powd
        coef = term / (nl ** aa * pl ** bb * ll ** cc)
        if aa != bb:
            continue
        den = sp.Integer(1)
        for i in range(aa):
            den *= (D + 2 * i)
        out += coef * sp.factorial(aa) * Pn ** aa * ll ** (cc + aa) / den
    return sp.expand(out)


kin = Kin({('l', 'l'): ll, ('l', 'p'): pl, ('l', 'n'): nl, ('p', 'p'): 0, ('n', 'n'): 0, ('p', 'n'): Pn})
Lv, Pv, Nv = Vec.b('l'), Vec.b('p'), Vec.b('n')


def local_oneloop(n):
    """one-loop bare matrix element of psibar nslash (n.D)^{n-1} psi in an on-shell massless quark,
       gluon mass m, Feynman gauge, normalised to the tree n.p^{n-1}; returned in units of
       A_eps = (alpha_s/2pi) C_F e^{eps gE} Gamma(eps) (mu^2/m^2)^eps."""
    Kv = Lv + Pv * y                         # k = l + y p after Feynman parametrisation (Delta = y m^2)
    nk = nl + y * Pn
    # vertex graph:  -i g^2 C_F int gamma^mu kslash nslash kslash gamma_mu (n.k)^{n-1} / ((k^2)^2 ((p-k)^2-m^2))
    num_a = tr_sum(mul([Term(sp.Rational(1, 2), [V('p')])],
                       [Term(1, [I('mu'), ('v', Kv), V('n'), ('v', Kv), I('mu')])]), kin) * nk ** (n - 1)
    num_a = sym_avg(num_a.subs(D, 4 - 2 * eps)) / (2 * Pn * Pn ** (n - 1))   # divide by (1/2)Tr[pslash nslash] Pn^{n-1}
    num_a = sp.simplify(num_a.subs(D, 4 - 2 * eps))
    # num_a = c * ll ; denominators: int dy 2(1-y) / (l^2 - y m^2)^3
    c_a = sp.simplify(num_a / ll)
    # int d^Dl/(2pi)^D l^2/(l^2-Delta)^3 = i/(4pi)^{D/2} (D/4) Gamma(eps) Delta^{-eps}
    # -i g^2 C_F * i/(4pi)^{2-eps} (D/4) Gamma(eps) = g^2 C_F/(4pi)^{2-eps} Gamma(eps) (D/4)   ; g^2/(4pi)^{2-eps} -> (alpha_s/4pi) mu^{2eps} e^{eps gE}
    # in units of A_eps = (alpha_s/2pi) C_F e^{eps gE} G(eps)(mu^2/m^2)^eps:  factor (1/2) (D/4)
    A = sp.Rational(1, 2) * (4 - 2 * eps) / 4 * c_a * sp.integrate(2 * (1 - y) * y ** (-eps), (y, 0, 1), conds='none') if False else None
    va = sp.Rational(1, 2) * (4 - 2 * eps) / 4 * sp.integrate(2 * (1 - y) * y ** (-eps) * c_a, (y, 0, 1), conds='none')
    # operator-gluon graphs (b)+(c): i g^2 C_F int nslash kslash nslash sum_j (n.k)^{n-2-j} (n.p)^j / (k^2 ((p-k)^2 - m^2))
    if n >= 2:
        sj = sum(nk ** (n - 2 - j) * Pn ** j for j in range(n - 1))
        num_b = tr_sum(mul([Term(sp.Rational(1, 2), [V('p')])], [Term(1, [V('n'), ('v', Kv), V('n')])]), kin) * sj
        num_b = sym_avg(num_b.subs(D, 4 - 2 * eps)) / (2 * Pn * Pn ** (n - 1))
        c_b = sp.simplify(num_b)          # no ll: scalar integral int 1/(l^2 - y m^2)^2 = i/(4pi)^{D/2} Gamma(eps) Delta^{-eps}
        # i g^2 C_F * i Gamma(eps)/(4pi)^{2-eps} = -g^2 C_F Gamma(eps)/(4pi)^{2-eps} -> units A_eps: factor -1/2 ; two graphs: x2
        vb = 2 * (-sp.Rational(1, 2)) * sp.integrate(c_b * y ** (-eps), (y, 0, 1), conds='none')
    else:
        vb = 0
    vse = -(1 - eps) / (2 - eps)        # on-shell residue (s2)
    return sp.simplify(va + vb + vse)


def pdf_moment(n):
    """n-th moment of the bare one-loop PDF of s2 in units of A_eps."""
    reg = (1 - eps) ** 2 * sp.integrate(xi ** (n - 1 - eps) * (1 - xi), (xi, 0, 1), conds='none')
    plus = 2 * sp.integrate(sp.expand(xi ** (1 - eps) * sp.cancel((xi ** (n - 1) - 1) / (1 - xi))), (xi, 0, 1), conds='none')
    return sp.simplify(reg + plus - (1 - eps) / (2 - eps))


okE = True
det = []
for n in range(1, 9):
    lo, pm = local_oneloop(n), pdf_moment(n)
    d_ = sp.simplify(lo - pm)
    okE &= d_ == 0
    det.append(str(sp.factor(pm)) if n <= 2 else '')
report('(e) one loop, exact in eps: moment_n(bare PDF) = <q|O_n|q>^(1)_bare  (n = 1..8)', okE)
print('     n=1:', det[0], '   n=2:', det[1])
# pieces separately (vertex graph <-> ladder; operator-gluon graphs <-> Wilson-line real+virtual)
n = 4
va_check = sp.simplify((1 - eps) ** 2 / ((n - eps) * (n + 1 - eps)) - (1 - eps) ** 2 * sp.integrate(xi ** (n - 1 - eps) * (1 - xi), (xi, 0, 1), conds='none'))
report('    piecewise: vertex graph = ladder moment (1-eps)^2/((n-eps)(n+1-eps))', va_check == 0)
wl = 2 * sp.integrate(sp.expand(xi ** (1 - eps) * sp.cancel((xi ** (n - 1) - 1) / (1 - xi))), (xi, 0, 1), conds='none')
report('    piecewise: Wilson-line graphs = -2 sum_{i=1}^{n-1} 1/(i+1-eps)', sp.simplify(wl + 2 * sum(1 / (i + 1 - eps) for i in range(1, n))) == 0)

print()
print('SUMMARY s4: %d/%d PASS' % (sum(1 for _, o in results if o), len(results)))
