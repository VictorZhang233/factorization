"""W09 / v4: moments of PDFs = local operator matrix elements.
 (a) int xi^{n-1} f = (1/(2P+)) (-i/P+)^{n-1} M^{(n-1)}(0),  M(w) = 2P+ int dxi e^{i xi P+ w} f(xi)  (numerical);
 (b) light-ray m-gluon vertex in w-space: (ig)^m int_{0<z1<..<zm<w} e^{i kappa_m w - i sum q_j z_j}
     = g^m E_w[kappa_0,...,kappa_m]  (divided difference of E_w(x) = e^{i x w}; Hermite-Genocchi), m = 1,2,3;
 (c) (-i)^{n-1} d^{n-1}/dw^{n-1} (iw)^m int_simplex e^{i w sum t_j kappa_j} |_{w=0} = h_{n-1-m}(kappa)  (symbolic);
 (d) Dirichlet integral int_simplex prod t^a = prod a!/(sum a + m)!;  x^N[kappa_0..kappa_m] = h_{N-m}(kappa);
 (e) VF-PDF-12: one-gluon vertex moments; local vertex of psibar g+ (iD+)^{n-1} psi;
 (f) VF-PDF-13: one-loop moments of the bare PDF exactly in eps; n=1 -> 0, n=2 -> -4A/(3-eps);
 (g) independent Feynman-parameter computation of the local-operator vertex graph and operator-gluon graphs
     (gluon mass m, Feynman gauge), exactly in eps.
"""
import sys, os, itertools, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
import mpmath as mp

npass = 0; nfail = 0
def check(name, ok):
    global npass, nfail
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)
    if ok: npass += 1
    else: nfail += 1

# (a) derivative formula with a smooth f supported in [-1,1]
Pp = 1.7
fq = lambda t: (1 - t ** 2) ** 3 * (1 + 0.7 * t + 0.2 * t ** 2)
def M(w):
    return 2 * Pp * mp.quad(lambda t: mp.e ** (1j * t * Pp * w) * fq(t), [-1, 1])
for n in range(1, 7):
    mom = mp.quad(lambda t: t ** (n - 1) * fq(t), [-1, 1])
    der = mp.diff(M, 0, n - 1)
    rhs = 1 / (2 * Pp) * (-1j / Pp) ** (n - 1) * der
    check('(a) n=%d: int xi^{n-1} f = (1/2P+)(-i/P+)^{n-1} M^{(n-1)}(0): %.12f vs %s' % (n, mom, mp.nstr(rhs, 12)), abs(mom - rhs) < 1e-8)
# inverse relation f = int dw/(4pi) e^{-i xi P+ w} M(w): check normalisation at one xi
xi0 = 0.31
Mfun = lambda w: M(w)
# use analytic: int dw/(4pi) e^{-i xi P w} 2P int dxi' e^{i xi' P w} f(xi') = (2P/(4pi)) (2pi/P) f(xi) = f(xi)
check('(a) inverse normalisation (2P+/(4pi)) (2pi/P+) = 1', abs(2 * Pp / (4 * np.pi) * 2 * np.pi / Pp - 1) < 1e-15)

# (b) Hermite-Genocchi: path-ordered integral = divided difference
def divdiff(fun, nodes):
    if len(nodes) == 1:
        return fun(nodes[0])
    return (divdiff(fun, nodes[1:]) - divdiff(fun, nodes[:-1])) / (nodes[-1] - nodes[0])
rng = np.random.default_rng(7)
for m in (1, 2, 3):
    for trial in range(2):
        q = rng.uniform(-1.2, 1.5, size=m)
        k1 = rng.uniform(-0.8, 1.0)
        kap = [k1] + list(k1 + np.cumsum(q))
        w = rng.uniform(0.3, 2.0)
        # simplex integral by nested quadrature
        if m == 1:
            val = mp.quad(lambda z1: mp.e ** (-1j * q[0] * z1), [0, w])
        elif m == 2:
            val = mp.quad(lambda z2: mp.quad(lambda z1: mp.e ** (-1j * (q[0] * z1 + q[1] * z2)), [0, z2]), [0, w])
        else:
            val = mp.quad(lambda z3: mp.quad(lambda z2: mp.quad(lambda z1: mp.e ** (-1j * (q[0] * z1 + q[1] * z2 + q[2] * z3)), [0, z2]), [0, z3]), [0, w])
        lhs = (1j) ** m * mp.e ** (1j * kap[-1] * w) * val       # (ig)^m with g = 1
        rhs = divdiff(lambda x: mp.e ** (1j * x * w), kap)
        check('(b) m=%d: (i)^m int e^{i kappa_m w - i sum q z} = E_w[kappa_0..kappa_m] (|diff|=%.1e)' % (m, abs(lhs - rhs)), abs(lhs - rhs) < 1e-9)

# (c),(d) symbolic: moments of the simplex representation = complete homogeneous symmetric polynomials
wsym = sp.symbols('w')
def hcomp(r, ks):
    """complete homogeneous symmetric polynomial h_r(ks)"""
    if r < 0: return 0
    tot = 0
    for comb in itertools.combinations_with_replacement(range(len(ks)), r):
        term = 1
        for c in comb: term *= ks[c]
        tot += term
    return sp.expand(tot)
def dirichlet(avec):
    m = len(avec) - 1
    return sp.Integer(math.prod(math.factorial(a) for a in avec)) / sp.factorial(sum(avec) + m)
# check Dirichlet formula for m = 2 by explicit integration
t1, t2 = sp.symbols('t1 t2', positive=True)
for avec in ((0, 0, 0), (1, 2, 0), (2, 1, 3)):
    integrand = t1 ** avec[0] * t2 ** avec[1] * (1 - t1 - t2) ** avec[2]
    val = sp.integrate(sp.integrate(integrand, (t2, 0, 1 - t1)), (t1, 0, 1))
    check('(d) Dirichlet int_simplex t1^%d t2^%d t0^%d = %s' % (avec[0], avec[1], avec[2], val), sp.simplify(val - dirichlet(avec)) == 0)
for m in (1, 2, 3):
    ks = sp.symbols('k0:%d' % (m + 1))
    for n in range(m + 1, 8):
        r = n - 1 - m
        # int_simplex (sum t_j k_j)^r = r!/(r+m)! h_r(k) via multinomial + Dirichlet
        tot = 0
        for comb in itertools.product(range(r + 1), repeat=m + 1):
            if sum(comb) != r: continue
            coef = sp.factorial(r) / math.prod(math.factorial(c) for c in comb)
            mon = math.prod(ks[j] ** comb[j] for j in range(m + 1))
            tot += coef * mon * dirichlet(comb)
        lhs = sp.expand(sp.factorial(n - 1) / sp.factorial(r) * tot)   # (n-1)!/r! * int (sum t k)^r
        ok = sp.simplify(lhs - hcomp(r, ks)) == 0
        # divided-difference identity x^{n-1}[k0..km] = h_{n-1-m}
        dd = sp.simplify(sp.together(divdiff(lambda x: x ** (n - 1), list(ks))))
        ok2 = sp.simplify(sp.expand(sp.cancel(dd)) - hcomp(r, ks)) == 0
        check('(c) m=%d n=%d: (-i)^{n-1} d^{n-1}_w[(iw)^m int e^{iw sum t k}]_0 = h_{n-1-m}; x^{n-1}[k] = h too' % (m, n), ok and ok2)

# (e) VF-PDF-12 one-gluon vertex moments
k1p, k2p, Pplus, xi = sp.symbols('k1p k2p Pplus xi', positive=True)
for n in range(1, 8):
    mom = (k2p ** (n - 1) - k1p ** (n - 1)) / (Pplus ** n) / (k2p - k1p)   # int xi^{n-1}[delta(xi P - k2) - delta(xi P - k1)] / q+
    local = sum(k2p ** j * k1p ** (n - 2 - j) for j in range(0, n - 1)) / Pplus ** n
    check('(e) n=%d: moment of the one-gluon light-ray vertex = local one-gluon vertex' % n, sp.simplify(mom - local) == 0)
# w-space form of the one-gluon term: (g/q+)(e^{i k2 w} - e^{i k1 w}) and its Fourier transform with dw/(4pi) e^{-i xi P w}
#  -> (g/(2 q+)) [delta(xi P - k2) - delta(xi P - k1)]  (prefactor (1/(4pi)) 2pi = 1/2)
check('(e) dw/(4pi) Fourier normalisation gives 1/2', abs(2 * np.pi / (4 * np.pi) - 0.5) < 1e-15)

# (f) VF-PDF-13 moments of the bare one-loop PDF (units A_eps)
eps = sp.symbols('epsilon')
nn = sp.symbols('n', positive=True, integer=True)
for n in range(1, 9):
    ladder = sp.gammasimp((1 - eps) ** 2 * sp.gamma(n - eps) * sp.gamma(2) / sp.gamma(n + 2 - eps))
    ok1 = sp.simplify(ladder - (1 - eps) ** 2 / ((n - eps) * (n + 1 - eps))) == 0
    # Wilson: int xi^{n-1} [2 xi^{1-eps}/(1-xi)]_+ = -2 sum_{i=0}^{n-2} 1/(i+2-eps)
    wil = sp.Integer(0) - 2 * sum((1 / (i + 2 - eps) for i in range(0, n - 1)), sp.Integer(0))
    wil_alt = sp.Integer(0) - 2 * sum((1 / (i + 1 - eps) for i in range(1, n)), sp.Integer(0))
    ok2 = sp.simplify(wil - wil_alt) == 0
    # numerical check of the Wilson moment at eps = 0.17
    ev = 0.17
    num = mp.quad(lambda t: 2 * t ** (1 - ev) / (1 - t) * (t ** (n - 1) - 1), [0, 1])
    ok3 = abs(num - float(wil.subs(eps, ev))) < 1e-10
    se = -(1 - eps) / (2 - eps)
    total = sp.simplify(ladder + wil + se)
    check('(f) n=%d: ladder (1-e)^2/((n-e)(n+1-e)), Wilson -2 sum 1/(i+1-e), SE -(1-e)/(2-e); total = %s' % (n, sp.factor(total)), ok1 and ok2 and ok3)
    if n == 1:
        check('(f) n=1 total = 0 (quark number)', total == 0)
    if n == 2:
        check('(f) n=2 total = -4/(3-eps)', sp.simplify(total + 4 / (3 - eps)) == 0)
        check('(f) n=2 pole: -4/3 = gamma_qq(2)/C_F', sp.limit(total, eps, 0) == -sp.Rational(4, 3))

# (g) independent local-operator graphs via Feynman parameters (gluon mass m^2, on-shell massless quark p)
# vertex graph:  -i g^2 C_F int d^Dk/(2pi)^D (1/2)Tr[p g^mu k g+ k g_mu] (k+)^{n-1} / ((k^2)^2 ((p-k)^2-m^2))
#   gamma^mu kslash g+ kslash gamma_mu = -(D-2) kslash g+ kslash ;  (1/2)Tr[p k g+ k] = 2[2(p.k)k+ - k^2 p+]
#   Feynman parameters, k = q + y p (y = 1-x), Delta = y m^2; symmetric integration:
#   <(n.q)(p.q)> = q^2 p+/D, all other q-odd or n.n terms vanish -> numerator -> -(D-2)/D y^{n-1}(p+)^n q^2
#   int d^Dq/(2pi)^D q^2/(q^2-Delta)^3 = i (D/4) Gamma(eps) Delta^{-eps}/(4pi)^{D/2}
from w9lib import dtrace, D as Dsym
dots = {('k', 'k'): sp.Symbol('kk'), ('k', 'n'): sp.Symbol('kn'), ('k', 'p'): sp.Symbol('kp'),
        ('n', 'n'): 0, ('n', 'p'): sp.Symbol('pplus'), ('p', 'p'): 0}
tr = dtrace([('v', 'p'), ('i', 'a'), ('v', 'k'), ('v', 'n'), ('v', 'k'), ('i', 'a')], dots) / 2
check('(g) (1/2)Tr[p g^mu k g+ k g_mu] = -(D-2) 2[2(p.k)k+ - k^2 p+]',
      sp.simplify(tr + (Dsym - 2) * 2 * (2 * dots[('k', 'p')] * dots[('k', 'n')] - dots[('k', 'k')] * dots[('n', 'p')])) == 0)
Dd = 4 - 2 * eps
y = sp.symbols('y', positive=True)
m2, mu2, als, gE = sp.symbols('m2 mu2 alpha_s gamma_E', positive=True)
g2 = 4 * sp.pi * als * mu2 ** eps * sp.exp(eps * gE) * (4 * sp.pi) ** (-eps)
Aeps = als / (2 * sp.pi) * sp.exp(eps * gE) * sp.gamma(eps) * (mu2 / m2) ** eps
for n in range(1, 7):
    # graph / tree, tree = 2 (p+)^n ; factors: (-i g^2 C_F) * (-(D-2) * 2) * Iq ; Iq = int dx 2x [-(D-2)/D y^{n-1}] * i (D/4) Gamma(eps) Delta^{-eps}/(4pi)^{D/2}
    Iq = sp.integrate(2 * (1 - y) * (-(Dd - 2) / Dd) * y ** (n - 1) * (y * m2) ** (-eps), (y, 0, 1), conds='none') * sp.I * (Dd / 4) * sp.gamma(eps) / (4 * sp.pi) ** (Dd / 2)
    graph = (-sp.I * g2) * (-(Dd - 2) * 2) * Iq / 2   # per C_F, divided by tree 2(p+)^n
    target = Aeps * (1 - eps) ** 2 / ((n - eps) * (n + 1 - eps))
    val = complex(sp.N((graph / target).subs({eps: sp.Rational(1, 7), m2: sp.Rational(5, 4), mu2: sp.Rational(3, 2), als: 1, gE: sp.EulerGamma})))
    check('(g) n=%d: local vertex graph (Feynman parameters) = A_eps (1-eps)^2/((n-eps)(n+1-eps)) [ratio %s]' % (n, np.round(val, 12)), abs(val - 1) < 1e-10)
    if n >= 2:
        # operator-gluon graph A2: i g^2 C_F int 4 k+ p+ sum_j (p+)^j (k+)^{n-2-j} / (k^2 ((p-k)^2 - m^2)), / tree
        Iq2 = sum(sp.integrate(y ** (n - 1 - j) * (y * m2) ** (-eps), (y, 0, 1), conds='none') for j in range(0, n - 1)) * sp.I * sp.gamma(eps) / (4 * sp.pi) ** (Dd / 2)
        graph2 = (sp.I * g2) * 4 * Iq2 / 2
        target2 = -Aeps * sum(1 / (i + 1 - eps) for i in range(1, n))
        val2 = complex(sp.N((graph2 / target2).subs({eps: sp.Rational(1, 7), m2: sp.Rational(5, 4), mu2: sp.Rational(3, 2), als: 1, gE: sp.EulerGamma})))
        check('(g) n=%d: operator-gluon graph A2 = -A_eps sum_{i=1}^{n-1} 1/(i+1-eps)  (A2 + A3 = Wilson-line moment) [ratio %s]' % (n, np.round(val2, 12)), abs(val2 - 1) < 1e-10)
# numerical check of the symmetric-integration claims with explicit 4-vectors: average over a random Lorentz-invariant
# set is hard; instead verify the tensor formula <q^mu q^nu> = q^2 g^{mu nu}/D contracted with n,p gives q^2 n.p/D and
# that pairings with n.n vanish (algebraic, by construction).  Recorded as an algebraic step.
print('\nSUMMARY v4: %d PASS, %d FAIL' % (npass, nfail), flush=True)
