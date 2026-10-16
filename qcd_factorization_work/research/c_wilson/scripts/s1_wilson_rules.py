"""
s1_wilson_rules.py -- item (1): momentum-space Feynman rules of semi-infinite Wilson lines.

W[b,a] = P exp( i g int_a^b dz.A ), points closer to b to the LEFT,  A(x) = int d^4k/(2pi)^4 e^{-ik.x} At(k)
(k flows INTO the line at the attachment point).  n future-pointing.

Claims checked
 (A) exact iterated integrals (sympy, with the adiabatic damping e^{-eps|s|} per field, s = distance from the
     finite end) for m = 1,2,3 attachments on the four semi-infinite lines
        W[0,-inf] (past, along +n),  W[inf,0] (future, along +n),
        W[-inf,0] = W[0,-inf]^dag (along -n),  W[0,inf] = W[inf,0]^dag (along -n);
 (B) the UNIVERSAL RULE: vertex  i g t^a v^mu  (v = dz/ds, the orientation a->b),
     propagator  i/(v.l + i0)  for every segment except the one reaching infinity, l = momentum flowing along
     the orientation (a -> b), l = 0 on the segment touching infinity;  colour matrices in path order (b left);
     equivalently, with n future-pointing and K = sum of momenta flowing in between the segment and infinity:
        past-pointing lines:  i/(n.K + i0),   future-pointing lines:  -i/(n.K - i0);
 (C) numerical check: the path-ordered exponential solved as an ODE in a non-abelian (SU(3)) multi-mode
     background reproduces the momentum-space rule order by order in g (m = 1..4), for all four lines;
     the wrong i0 or the wrong colour order fail;
 (D) hermitian conjugation W[0,-inf]^dag = W[-inf,0] (numerically, real background field);
 (E) gauge covariance W -> U(b) W U^dag(a) of the ordering convention (finite segment, SU(3)).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qcdtools import *
import sympy as sp

R = Report('s1_wilson_rules')

# =====================================================================================================
# (A) + (B): exact sympy iterated integrals
# =====================================================================================================
print('--- (A),(B) exact iterated integrals (sympy) ---')
eps = sp.symbols('epsilon', positive=True)
a = sp.symbols('a1:4', real=True)          # a_j = n.k_j  (k_j flowing into the line)
s = sp.symbols('s1:4', real=True)


def iterated(m, line):
    """
    Exact value of the coefficient of (i g)^m (prod n.At) [colour in path order] for the given line, as a
    function of a_j = n.k_j.  Gluon j is attached at the j-th point counted from the FINITE end (the origin).
    Returns the integral including the sign (dz = +/- n ds) but WITHOUT the factor i^m of (ig)^m.
      'past'   W[0,-inf]:  z = -s n, s in (0,inf), path a=-inf -> b=0 : dz/dlambda = +n
      'future' W[inf,0]:   z = +s n, path 0 -> inf : dz = +n ds
      'pastc'  W[-inf,0]:  z = -s n, path 0 -> -inf: dz = -n ds
      'futc'   W[0,inf]:   z = +s n, path inf -> 0: dz = -n ds
    Gluon j sits at distance s_j from the origin, s_1 < s_2 < ... < s_m; the phase is e^{-i k.z}.
    """
    sign_z = {'past': -1, 'future': +1, 'pastc': -1, 'futc': +1}[line]   # z = sign_z * s n
    sign_dz = {'past': +1, 'future': +1, 'pastc': -1, 'futc': -1}[line]  # orientation v = sign_dz * n
    # exponent coefficients: field j contributes exp(c_j s_j), c_j = -i a_j sign_z - eps  (Re c_j < 0)
    cs = [-sp.I * a[j] * sign_z - eps for j in range(m)]
    # integrate s_m from s_{m-1} to inf, then s_{m-1} from s_{m-2} to inf, ..., s_1 from 0 to inf, using the
    # elementary integral ELEM(c, lo) = int_lo^inf exp(c s) ds  (computed once by sympy, Re c < 0)
    coef = sp.Integer(1)
    cum = sp.Integer(0)                      # accumulated exponent coefficient carried to the next variable
    for j in reversed(range(m)):
        cum = cum + cs[j]
        lo = s[j - 1] if j > 0 else sp.Integer(0)
        val = ELEM.subs({csym: cum, losym: lo}, simultaneous=True)
        # val = coefficient * exp(cum * lo); peel off the exponential (it combines with field j-1)
        coef = coef * sp.simplify(val * sp.exp(-cum * lo))
    return sp.simplify(coef * sign_dz**m)


# the only analytic input: int_lo^inf exp(c s) ds = e^{c lo} int_0^inf e^{c t} dt  for Re c < 0
# (sympy, with c = -x - i y, x > 0; sympy returns a Piecewise whose first branch is valid for x > 0)
_x = sp.symbols('x', positive=True); _y = sp.symbols('y', real=True); _t = sp.symbols('t', positive=True)
csym, losym = sp.symbols('c lo')
_e0 = sp.integrate(sp.exp((-_x - sp.I * _y) * _t), (_t, 0, sp.oo))
_branch, _cond = _e0.args[0]
# (sympy's arg-based branch condition is not symmetric in Im c, so the value is confirmed by quadrature)
import mpmath as mpm
_num_ok = all(abs(mpm.quad(lambda t: mpm.exp(cc * t), [0, mpm.inf]) - (-1 / cc)) < 1e-12
              for cc in [mpm.mpc(-0.7, 1.3), mpm.mpc(-0.7, -1.3), mpm.mpc(-1.1, 0.4)])
R.flag('(A) int_0^inf e^{ct} dt = -1/c for Re c<0 (sympy branch; quadrature for Im c >< 0)',
       sp.simplify(_branch - (-1 / (-_x - sp.I * _y))) == 0 and _num_ok)
ELEM = -sp.exp(csym * losym) / csym      # = e^{c lo} * (-1/c)


def universal(m, line):
    """Universal rule (without the i^m g^m and the n.At factors), gluon j at the j-th point from the origin.
       Includes the sign of v (vertex i g v^mu = +/- i g n^mu) and the eikonal propagators i/(v.l + i c eps)."""
    vsign = {'past': +1, 'future': +1, 'pastc': -1, 'futc': -1}[line]
    # in path order from a to b, are the gluons ordered 1..m (origin = a) or m..1 (origin = b)?
    origin_is_a = line in ('future', 'pastc')         # W[inf,0] and W[-inf,0] start at the origin
    res = sp.Integer(vsign)**m
    if origin_is_a:
        # infinite end = b. Segment BEFORE gluon j (between j-1 and j) carries l = -(k_j+...+k_m) along v;
        # number of gluons between that segment and infinity = m-j+1
        for j in range(1, m + 1):
            l_dot_n = -sum(a[j - 1:m])
            res *= sp.I / (vsign * l_dot_n + sp.I * (m - j + 1) * eps)
    else:
        # infinite end = a; the path runs from infinity to the origin, so in PATH order the gluons are m,...,1.
        # Segment AFTER the path-ordered gluon (i.e. between gluon j and gluon j-1, origin side) carries
        # l = k_m + ... + k_j along v; (m-j+1) gluons between it and infinity.
        for j in range(1, m + 1):
            l_dot_n = sum(a[j - 1:m])
            res *= sp.I / (vsign * l_dot_n + sp.I * (m - j + 1) * eps)
    return sp.simplify(res)


closed = {
    # explicit closed forms quoted in DERIVATION.md (gluon j = j-th attachment from the origin)
    'past': lambda m: sp.prod([sp.I / (sum(a[j - 1:m]) + sp.I * (m - j + 1) * eps) for j in range(1, m + 1)]),
    'future': lambda m: sp.prod([-sp.I / (sum(a[j - 1:m]) - sp.I * (m - j + 1) * eps) for j in range(1, m + 1)]),
    'pastc': lambda m: (-1)**m * sp.prod([sp.I / (sum(a[j - 1:m]) + sp.I * (m - j + 1) * eps) for j in range(1, m + 1)]),
    'futc': lambda m: (-1)**m * sp.prod([-sp.I / (sum(a[j - 1:m]) - sp.I * (m - j + 1) * eps) for j in range(1, m + 1)]),
}

for line in ['past', 'future', 'pastc', 'futc']:
    for m in [1, 2, 3]:
        I_exact = iterated(m, line)
        d1 = sp.simplify(I_exact - universal(m, line))
        d2 = sp.simplify(I_exact - closed[line](m))
        R.flag(f'(A/B) {line:6s} m={m}: iterated integral == universal rule == closed form', d1 == 0 and d2 == 0,
               f'  [{sp.factor(I_exact)}]' if m <= 2 else '')

# NB in 'past' the j-th gluon from the origin is the (m-j+1)-th from -infinity; relabelling k_j -> k_{m-j+1}
# turns the closed form into the familiar  prod_j i/(n.(k_1+...+k_j)+i0) with k_1 nearest -infinity.
m = 2
rel_past = sp.simplify(closed['past'](2).subs({a[0]: sp.Symbol('b2'), a[1]: sp.Symbol('b1')}, simultaneous=True)
                       - sp.I / (sp.Symbol('b1') + sp.I * eps) * sp.I / (sp.Symbol('b1') + sp.Symbol('b2') + 2 * sp.I * eps))
R.flag('(A) past m=2 relabelled: i/(n.k1+i0) * i/(n.(k1+k2)+2i0), k1 nearest -inf', rel_past == 0)

# induction step for general m (past line): if the inner (m-1)-fold integral over the region
# -inf < l_1 < ... < l_{m-1} < l_m equals C_{m-1} exp(-i l_m (K_{m-1} + i(m-1)eps)), then the next one gives
# C_{m-1} * i/(K_m + i m eps) * exp(-i l (K_m + i m eps)).
Kp, am, l_, lm = sp.symbols('K_prev a_m l l_m', real=True)
mm = sp.symbols('m', positive=True, integer=True)
step = sp.integrate(sp.exp(-sp.I * lm * (Kp + sp.I * (mm - 1) * eps)) * sp.exp(-sp.I * lm * am + eps * lm),
                    (lm, -sp.oo, l_), conds='none')
target = sp.I / (Kp + am + sp.I * mm * eps) * sp.exp(-sp.I * l_ * (Kp + am + sp.I * mm * eps))
R.flag('(A) induction step (past line, general m)', sp.simplify(step - target) == 0)

# =====================================================================================================
# (C) numerical path-ordered exponential in a non-abelian background
# =====================================================================================================
print('\n--- (C) ODE solution of dW/ds = i g zdot.A(z(s)) W, SU(3) background ---')
rng = np.random.default_rng(20261009)
Rm = 3                                       # number of Fourier modes
kmodes = [rand_vec(rng, 1.0) for _ in range(Rm)]
epsv = [rand_vec(rng, 1.0, cplx=True) for _ in range(Rm)]
cols = [np.einsum('a,aij->ij', rng.normal(size=8), TA) for _ in range(Rm)]   # T_r = c_r^a t^a (hermitian)
nvec = lc(1.0, 0.0) + 0.0                     # light-like future-pointing n (n.v = v^-)
nvec = nvec + 0.0
EPS = 0.45                                    # adiabatic damping per field
L = 60.0                                      # e^{-EPS L} ~ 2e-12


def ndotA_coeffs(v):
    """coefficients alpha_r = v.eps_r (times T_r) and phases v.k_r for zdot.A along z = s v."""
    return [mdot(v, e) for e in epsv], [mdot(v, k) for k in kmodes]


def solve_line(line, order=4, h=0.004):
    """Solve the perturbative hierarchy W^(m)' = i zdot.A e^{-EPS dist} W^(m-1) with RK4.
       Returns list [W^(0),...,W^(order)] (coefficients of g^m) at the end point b."""
    if line == 'past':      # a=-L n -> b=0, z = t n, t from -L to 0, zdot = n, dist = -t
        t0, t1, zdir, vdir = -L, 0.0, nvec, nvec
        dist = lambda t: -t
        zof = lambda t: t
    elif line == 'future':  # a=0 -> b=L n
        t0, t1, zdir, vdir = 0.0, L, nvec, nvec
        dist = lambda t: t
        zof = lambda t: t
    elif line == 'pastc':   # a=0 -> b=-L n ; parametrize z = -t n, t: 0 -> L, zdot = -n
        t0, t1 = 0.0, L
        dist = lambda t: t
        zof = lambda t: -t
        vdir = -nvec
    elif line == 'futc':    # a=L n -> b=0 ; z = (L - t) n, zdot = -n
        t0, t1 = 0.0, L
        dist = lambda t: L - t
        zof = lambda t: L - t
        vdir = -nvec
    al = [mdot(vdir, e) for e in epsv]            # zdot.eps_r
    ph = [mdot(nvec, k) for k in kmodes]          # n.k_r ; point z = zof(t) n -> phase e^{-i zof(t) n.k}

    def Aof(t):
        M = np.zeros((3, 3), dtype=complex)
        for r in range(Rm):
            M += al[r] * cols[r] * np.exp(-1j * zof(t) * ph[r])
        return 1j * M * np.exp(-EPS * dist(t))

    N = int(round((t1 - t0) / h))
    Ws = [I3.copy()] + [np.zeros((3, 3), dtype=complex) for _ in range(order)]

    def rhs(t, Wl):
        A_ = Aof(t)
        return [np.zeros((3, 3), dtype=complex)] + [A_ @ Wl[mm - 1] for mm in range(1, order + 1)]

    t = t0
    for _ in range(N):
        k1 = rhs(t, Ws)
        k2 = rhs(t + h / 2, [Ws[i] + h / 2 * k1[i] for i in range(order + 1)])
        k3 = rhs(t + h / 2, [Ws[i] + h / 2 * k2[i] for i in range(order + 1)])
        k4 = rhs(t + h, [Ws[i] + h * k3[i] for i in range(order + 1)])
        Ws = [Ws[i] + h / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(order + 1)]
        t += h
    return Ws


def predict(line, m, wrong_i0=False, wrong_order=False):
    """Momentum-space rule for the coefficient of g^m.
       Gluon modes r_1..r_m attached at the 1st..m-th point FROM THE ORIGIN.
       vertex: i (v.eps_r) T_r ; propagators as in closed[...] with a_j = n.k_{r_j}; colour: path order."""
    vsign = {'past': +1, 'future': +1, 'pastc': -1, 'futc': -1}[line]
    past_like = line in ('past', 'pastc')
    tot = np.zeros((3, 3), dtype=complex)
    for rs in itertools.product(range(Rm), repeat=m):
        coef = 1.0 + 0j
        for r in rs:
            coef *= 1j * vsign * mdot(nvec, epsv[r])
        aa = [mdot(nvec, kmodes[r]) for r in rs]
        for j in range(1, m + 1):
            K = sum(aa[j - 1:m])
            c = (m - j + 1) * EPS
            if past_like:
                c = -c if wrong_i0 else c
                coef *= 1j / (K + 1j * c)
            else:
                c = -c if wrong_i0 else c
                coef *= -1j / (K - 1j * c)
        # colour: points closer to b on the left.
        mats = [cols[r] for r in rs]          # mats[j-1] = gluon at j-th point from origin
        if line in ('past', 'futc'):          # b = origin: gluon nearest origin is leftmost
            order_ = mats
        else:                                 # b = infinity: gluon farthest from origin leftmost
            order_ = mats[::-1]
        if wrong_order:
            order_ = order_[::-1]
        M = I3.copy()
        for X in order_:
            M = M @ X
        tot += coef * M
    return tot


for line in ['past', 'future', 'pastc', 'futc']:
    Ws = solve_line(line, order=4)
    for m in [1, 2, 3, 4]:
        pr = predict(line, m)
        R.check(f"(C) {line:6s} order g^{m}: ODE vs momentum-space rule", rel(Ws[m], pr), 1e-6)
    # negative controls
    if True:
        r_i0 = rel(Ws[2], predict(line, 2, wrong_i0=True))
        r_or = rel(Ws[2], predict(line, 2, wrong_order=True))
        R.flag(f'(C) {line:6s} negative controls (wrong i0 / reversed colour order fail)', r_i0 > 1e-3 and r_or > 1e-3,
               f' [rel.diff {r_i0:.2e}, {r_or:.2e}]')

# full path-ordered exponential at finite g vs truncated series
print('\n--- finite-g consistency ---')
gval = 0.15


def solve_full(line, g, h=0.004):
    Ws = solve_line(line, order=6, h=h)
    return sum(g**mm * Ws[mm] for mm in range(7)), Ws


for line in ['past', 'future']:
    Wsum, Ws = solve_full(line, gval)
    W4 = sum(gval**mm * Ws[mm] for mm in range(5))
    # unitarity check is not expected (complex background); check series convergence instead
    R.check(f'(C) {line} series: |W(g) - sum_(m<=4)| ~ g^5', rel(Wsum, W4), 5 * gval**5 * max(1, np.abs(Ws[5]).max()))

# =====================================================================================================
# (D) hermitian conjugation with a REAL background field
# =====================================================================================================
print('\n--- (D) W[0,-inf]^dag = W[-inf,0] for a hermitian background ---')
# make the background hermitian: add the conjugate modes (-k, eps^*), T_r hermitian
kmodes_h = kmodes + [-k for k in kmodes]
epsv_h = epsv + [e.conj() for e in epsv]
cols_h = cols + cols
kmodes, epsv, cols, Rm = kmodes_h, epsv_h, cols_h, 2 * Rm
Wp = solve_line('past', order=4)
Wpc = solve_line('pastc', order=4)
for mm in range(1, 5):
    R.check(f'(D) order g^{mm}: W[-inf,0]^(m) == (W[0,-inf]^(m))^dagger (hermitian field)',
            rel(Wpc[mm], Wp[mm].conj().T), 1e-6)
    # order-by-order unitarity  sum_j W^(j) W^(m-j)dag = 0
    U_m = sum(Wp[j] @ Wp[mm - j].conj().T for j in range(mm + 1))
    R.check(f'(D) order g^{mm}: unitarity sum_j W^(j) W^(m-j)^dag = 0', np.abs(U_m).max() / max(np.abs(Wp[mm]).max(), 1e-12), 1e-6)
# momentum-space statement of (D): with At(k)^dag = At(-k) the m=2 past rule maps onto the pastc rule
k1s, k2s = sp.symbols('kn1 kn2', real=True)
past2 = sp.I / (k1s + sp.I * eps) * sp.I / (k1s + k2s + 2 * sp.I * eps)          # k1 nearest -inf, colour T(k2)T(k1)
conj_rel = sp.conjugate(past2).subs({k1s: -k1s, k2s: -k2s}, simultaneous=True)       # (ig)^2 -> (-ig)^2, k -> -k
# the conjugate has colour T(-k1)^dag ... reversed: T(k1)T(k2) with k1 leftmost = nearest -inf  => pastc rule
pastc2 = sp.I / (k1s + sp.I * eps) * sp.I / (k1s + k2s + 2 * sp.I * eps)
R.flag('(D) momentum space: [past rule]^* with k -> -k == pastc rule (cumulative from -inf, +i0)',
       sp.simplify(conj_rel - pastc2) == 0)

# =====================================================================================================
# (E) gauge covariance of the ordering convention: finite straight segment from a to b
# =====================================================================================================
print('\n--- (E) gauge covariance W -> U(b) W U^dag(a) ---')
gval = 0.7
rng2 = np.random.default_rng(7)
za = rand_vec(rng2, 1.0); zb = rand_vec(rng2, 1.0)
v = zb - za
Ac = [rng2.normal(size=(4, 8)) for _ in range(3)]


def A_field(x):
    """smooth SU(3) background A_mu(x) (lower index) as a list of 4 hermitian 3x3 matrices"""
    out = []
    for mu in range(4):
        c = Ac[0][mu] * np.sin(x @ np.array([0.3, 0.2, -0.1, 0.4])) + Ac[1][mu] * np.cos(x @ np.array([0.1, -0.5, 0.2, 0.3])) + Ac[2][mu] * 0.3
        out.append(np.einsum('a,aij->ij', c, TA))
    return out


thv = rng2.normal(size=(2, 8))


def Ugauge(x):
    th = np.einsum('a,aij->ij', thv[0] * np.sin(x @ np.array([0.2, 0.1, 0.3, -0.2])) + thv[1] * 0.5, TA)
    w, V = np.linalg.eigh(th)
    return V @ np.diag(np.exp(1j * w)) @ V.conj().T


def wilson_segment(Af, ordering='b-left', N=4000, transformed=False):
    """path-ordered exponential along z(s) = za + s v, s in [0,1]; RK4 on dW/ds = i g v^mu A_mu W."""
    h = 1.0 / N
    W = I3.copy()

    def vA(s_):
        x = za + s_ * v
        if not transformed:
            Al = Af(x)
            return sum(v[mu] * Al[mu] for mu in range(4))
        # transformed field contracted with v: U vA U^dag - (i/g) (dU/ds) U^dag
        U = Ugauge(x); Al = Af(x)
        vA0 = sum(v[mu] * Al[mu] for mu in range(4))
        dd = 1e-5
        dU = (Ugauge(za + (s_ + dd) * v) - Ugauge(za + (s_ - dd) * v)) / (2 * dd)
        return U @ vA0 @ U.conj().T - (1j / gval) * dU @ U.conj().T

    for i in range(N):
        s0 = i * h
        if ordering == 'b-left':
            f = lambda s_, W_: 1j * gval * vA(s_) @ W_
        else:
            f = lambda s_, W_: 1j * gval * W_ @ vA(s_)
        k1 = f(s0, W); k2 = f(s0 + h / 2, W + h / 2 * k1); k3 = f(s0 + h / 2, W + h / 2 * k2); k4 = f(s0 + h, W + h * k3)
        W = W + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return W


W0 = wilson_segment(A_field)
W1 = wilson_segment(A_field, transformed=True)
R.check('(E) W\'[b,a] == U(b) W[b,a] U^dag(a) (points closer to b on the left)', rel(W1, Ugauge(zb) @ W0 @ Ugauge(za).conj().T), 1e-6)
W0r = wilson_segment(A_field, ordering='a-left')
W1r = wilson_segment(A_field, ordering='a-left', transformed=True)
R.flag('(E) reversed ordering is NOT covariant (negative control)',
       rel(W1r, Ugauge(zb) @ W0r @ Ugauge(za).conj().T) > 1e-2 and rel(W1r, Ugauge(za) @ W0r @ Ugauge(zb).conj().T) > 1e-2)

R.summary()
