#!/usr/bin/env python3
"""W25 / Ch22 -- s1: one-loop quasi-PDF checks in the book's conventions (writer re-derivation).

Conventions (WRITER_SPEC_v2 Sec.3 rows 4, 40-42): D = d - i g A, quark-gluon vertex i g gamma^mu t^a,
W[b,a] = P exp(i g int_a^b dz.A); a = alpha_s C_F/(2 pi); lambda = P.z = -P^z z; L_z = ln(-z^2 mu^2 e^{2 gE}/4);
ell_p = ln(mu^2/(4 p_z^2)), L_zeta = -ell_p.

A  moments C_n of the coordinate kernel (gamma^0: sigma=0, gamma^z: sigma=1), n = 0..12, vs closed form (VF-LAM-4)
B  RG of the coordinate kernel and consistency with the operator anomalous dimension 3a/2 (VF-LAM-2/4)
C  unphysical region xi > 1, xi < 0 from Feynman rules (ex:lattice-quasi-tree(b)):
   C1 Dirac traces of the vertex and sail numerators (explicit 4x4 gamma matrices)
   C2 Feynman-parameter identity and symmetric integration (vertex numerator -> p0(4/3 l^2 - 8/3 l_z^2))
   C3 3-D Euclidean master integrals 1/(8 pi |l|), 1/(32 pi |l|^3)
   C4 y-integrals -> closed forms (VF-LAM-7), both regions, several xi
   C5 independent route: Fourier transform of the ln(z^2) term of the coordinate kernel
   C6 tadpole: coefficient of ln z^2 of the DR Wilson-line self-energy, and FT[ln zeta^2] = -1/|u|
D  endpoint structure of C^MSbar (prop:lamet-oneloop(e))
E  momentum RGE (prop:lamet-oneloop(f))
F  large-|xi| tails (prop:lamet-tails), sympy series
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np
import mpmath as mp

NP = 0; NF = 0
def check(name, ok, extra=""):
    global NP, NF
    ok = bool(ok)
    print(("PASS " if ok else "FAIL ") + name + ((" : " + str(extra)) if extra != "" else ""))
    if ok: NP += 1
    else: NF += 1

al, xi, y, L = sp.symbols('alpha xi y L', real=True)

# ---------------------------------------------------------------- A: moments
def plus_int(f, g):
    """int_0^1 [f]_+ g = int_0^1 f (g - g(1))"""
    return sp.integrate(sp.simplify(f * (g - g.subs(al, 1))), (al, 0, 1))

B = (1 + al**2) / (1 - al)
def Cn_from_kernel(n, sigma):
    g = al**n
    logc = sp.Rational(3, 2) - plus_int(B, g)                      # coefficient of a L_z
    const = (sp.Rational(3, 2) - plus_int(B, g) - plus_int(4 * sp.log(1 - al) / (1 - al), g)
             + sp.integrate(2 * (1 + sigma) * (1 - al) * g, (al, 0, 1)))
    return sp.nsimplify(sp.simplify(logc)), sp.nsimplify(sp.simplify(const))

def Cn_closed(n, sigma):
    H1 = sum(sp.Rational(1, i) for i in range(1, n + 1))
    H2 = sum(sp.Rational(1, i**2) for i in range(1, n + 1))
    d = 2 + 3 * n + n**2
    logc = sp.Rational(3 + 2 * n, d) + 2 * H1
    const = sp.Rational(5 + 2 * n, d) + 2 * (1 - H1) * H1 - 2 * H2 + (sp.Rational(2, d) if sigma else 0)
    return logc, const

allok = True
for sigma in (0, 1):
    for n in range(0, 13):
        a1, b1 = Cn_from_kernel(n, sigma); a2, b2 = Cn_closed(n, sigma)
        ok = sp.simplify(a1 - a2) == 0 and sp.simplify(b1 - b2) == 0
        allok &= ok
        if n in (0, 1, 2, 12):
            print("   sigma=%d n=%2d : log coeff %s, const %s" % (sigma, n, a2, b2))
check("A moments C_n of the coordinate kernel = closed form, n=0..12, gamma^0 and gamma^z", allok)
check("A C_0 = 1 + a(3/2 L_z + 5/2) (gamma^0), 7/2 (gamma^z)",
      Cn_closed(0, 0) == (sp.Rational(3, 2), sp.Rational(5, 2)) and Cn_closed(0, 1)[1] == sp.Rational(7, 2))
check("A int_0^1 2(1-alpha) = 1  =>  C_ratio has [2(1-alpha)]_+ and no delta term",
      sp.integrate(2 * (1 - al), (al, 0, 1)) == 1)

# ---------------------------------------------------------------- B: RG
# dC/dlnmu^2 = a[3/2 delta - [B]_+] ; DGLAP dI/dlnmu^2 = a [B]_+ (x) I  (P_qq = C_F [B]_+, alpha_s/(2pi) C_F = a)
# => d(C (x) I)/dlnmu^2 = (3/2) a C(x)I + O(a^2): operator AD d ln O/d ln mu^2 = 3 a/2 = 3 alpha_s C_F/(4 pi)
check("B int_0^1 [B]_+ = 0 and [B]_+ = (1+a^2)/(1-a)_+ + 3/2 delta (P_qq normalisation)",
      plus_int(B, sp.Integer(1)) == 0 and sp.simplify(sp.integrate((1 + al**2 - 2) / (1 - al), (al, 0, 1)) + sp.Rational(3, 2)) == 0)
check("B 3a/2 = 3 alpha_s C_F/(4 pi)", sp.simplify(sp.Rational(3, 2) * sp.Symbol('as') * sp.Symbol('CF') / (2 * sp.pi)
                                                   - 3 * sp.Symbol('as') * sp.Symbol('CF') / (4 * sp.pi)) == 0)

# ---------------------------------------------------------------- C1: Dirac traces
g0 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]], dtype=complex)
sx = np.array([[0, 1], [1, 0]]); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]])
def gi(s): return np.block([[np.zeros((2, 2)), s], [-s, np.zeros((2, 2))]]).astype(complex)
G = [g0, gi(sx), gi(sy), gi(sz)]
metric = np.diag([1, -1, -1, -1])
def slash(v): return sum(metric[m, m] * v[m] * G[m] for m in range(4))
def dot(u, v): return u[0] * v[0] - u[1] * v[1] - u[2] * v[2] - u[3] * v[3]
rng = np.random.default_rng(1)
ok1 = ok2 = True
for _ in range(5):
    pz = rng.uniform(0.5, 2); p = np.array([pz, 0, 0, pz])          # massless, along +z
    k = rng.normal(size=4)
    # vertex: (1/2) Tr[ pslash gamma^mu kslash gamma^0 kslash gamma_mu ]
    T = sum(metric[m, m] * np.trace(slash(p) @ G[m] @ slash(k) @ G[0] @ slash(k) @ G[m]) for m in range(4)) / 2
    ok1 &= abs(T - (-8 * k[0] * dot(p, k) + 4 * dot(k, k) * p[0])) < 1e-10
    # sail: (1/2) Tr[ pslash gamma^0 kslash ezslash ],  e_z = (0,0,0,1)
    ez = np.array([0, 0, 0, 1.0])
    T2 = np.trace(slash(p) @ G[0] @ slash(k) @ slash(ez)) / 2
    ok2 &= abs(T2 - (-2 * (p[0] * k[3] + p[3] * k[0]))) < 1e-10
check("C1 vertex numerator (1/2)Tr[p g^mu k g^0 k g_mu] = -8 k^0 (p.k) + 4 k^2 p^0", ok1)
check("C1 sail numerator (1/2)Tr[p g^0 k ez] = -2(p^0 k^z + p^z k^0)", ok2)

# ---------------------------------------------------------------- C2: Feynman parameters, symmetric integration
k0, kz, l0, lz, lp, P0, Pz, yy = sp.symbols('k0 kz l0 lz lperp P0 Pz y', real=True)
# p^2 = 0: y k^2 + (1-y)(p-k)^2 = (k-(1-y)p)^2
kk = sp.Matrix([k0, sp.Symbol('kx'), sp.Symbol('ky'), kz]); pp = sp.Matrix([Pz, 0, 0, Pz])
d4 = lambda u, v: u[0] * v[0] - u[1] * v[1] - u[2] * v[2] - u[3] * v[3]
lhs = yy * d4(kk, kk) + (1 - yy) * d4(pp - kk, pp - kk)
rhs = d4(kk - (1 - yy) * pp, kk - (1 - yy) * pp)
check("C2 y k^2 + (1-y)(p-k)^2 = (k-(1-y)p)^2 for p^2=0", sp.expand(lhs - rhs) == 0)
# numerator in terms of l = k - (1-y)p: -8 k^0 (p.k) + 4 k^2 p^0 -> -8 l^0 (p.l) + 4 p^0 l^2
lvec = sp.Matrix([l0, sp.Symbol('lx'), sp.Symbol('ly'), lz])
kofl = lvec + (1 - yy) * pp
num = -8 * kofl[0] * d4(pp, kofl) + 4 * d4(kofl, kofl) * pp[0]
num_l = -8 * lvec[0] * d4(pp, lvec) + 4 * pp[0] * d4(lvec, lvec)
check("C2 vertex numerator in terms of l: -8 l^0 (p.l) + 4 p^0 l^2", sp.expand(num - num_l) == 0)
# symmetric integration in the 3-D (l^0, l_perp) Minkowski subspace: (l^0)^2 -> (l^2 + l_z^2)/3, l^0 -> 0
l2 = sp.Symbol('l2')   # 4-vector square
num_sym = sp.expand(-8 * pp[0] * (l2 + lz**2) / 3 + 4 * pp[0] * l2)      # p.l = p^0 l^0 - p^z l^z, l^0 l^z term drops
check("C2 symmetric integration gives p^0 (4/3 l^2 - 8/3 l_z^2)",
      sp.simplify(num_sym - pp[0] * (sp.Rational(4, 3) * l2 - sp.Rational(8, 3) * lz**2)) == 0)

# ---------------------------------------------------------------- C3: master integrals
r, ell = sp.symbols('r ell', positive=True)
I2 = sp.integrate(4 * sp.pi * r**2 / (r**2 + ell**2)**2, (r, 0, sp.oo)) / (2 * sp.pi)**3
I3 = sp.integrate(4 * sp.pi * r**2 / (r**2 + ell**2)**3, (r, 0, sp.oo)) / (2 * sp.pi)**3
check("C3 int d^3l_E/(2pi)^3 (l^2+ell^2)^-2 = 1/(8 pi ell)", sp.simplify(I2 - 1 / (8 * sp.pi * ell)) == 0)
check("C3 int d^3l_E/(2pi)^3 (l^2+ell^2)^-3 = 1/(32 pi ell^3)", sp.simplify(I3 - 1 / (32 * sp.pi * ell**3)) == 0)
# Minkowski -> Euclidean: int dl^0 d^2l_perp/(2pi)^3 (l^2)^-n = i (-1)^n int d^3l_E/(2pi)^3 (l_E^2+ell^2)^-n
# vertex bracket: p0[ 4/3 * (i/(8 pi ell)) - 8/3 ell^2 * (-i/(32 pi ell^3)) ] = i p0/(4 pi ell)
br = sp.Rational(4, 3) * sp.I / (8 * sp.pi * ell) - sp.Rational(8, 3) * ell**2 * (-sp.I / (32 * sp.pi * ell**3))
check("C3 vertex 3-D bracket = i/(4 pi |l_z|) (times p^0)", sp.simplify(br - sp.I / (4 * sp.pi * ell)) == 0)

# vertex graph: factor (ig)^2 i i (-i) C_F = -i g^2 C_F; 1/(2 p^z) from the operator vertex; p^z/(2pi) from dk^z delta;
# Feynman parameter 2y ; => q_v = -i g^2 C_F * (1/(2pz)) * (pz/(2 pi)) * int dy 2y * i p0/(4 pi |l_z|), |l_z| = |xi-1+y| pz
g, CF = sp.symbols('g C_F', positive=True)
pref_v = sp.simplify((-sp.I * g**2 * CF) * sp.Rational(1, 2) / (2 * sp.pi) * 2 * sp.I / (4 * sp.pi))   # times int dy y/|xi-1+y| (p0=pz)
a_sym = g**2 * CF / (8 * sp.pi**2)     # = alpha_s C_F/(2pi)
check("C3 vertex prefactor = a (i.e. q_v = a int dy y/|xi-1+y| = a int dy (1-y)/|xi-y|)", sp.simplify(pref_v - a_sym) == 0)
# one sail: factor g (link) * i g (vertex) * i (quark) * (-i) (gluon) = i g^2; link FT gives delta/(2 pz^2 (1-xi));
# numerator -2(p0 k^z + pz k^0) -> -2 pz^2 (xi + 1 - y); 3-D integral i/(8 pi |l_z|); dk^z: pz/(2pi)
pref_s = sp.simplify(sp.I * g**2 * CF / (2 * sp.pi) / 2 * (-2) * sp.I / (8 * sp.pi))   # times int dy (xi+1-y)/|xi-1+y| /(1-xi)
check("C3 one sail prefactor = a/2 ; both sails: (a/(1-xi)) int dy (xi+y)/|xi-y|", sp.simplify(pref_s - a_sym / 2) == 0)

# ---------------------------------------------------------------- C4: y-integrals vs closed forms
def qv(x): return mp.quad(lambda t: (1 - t) / abs(x - t), [0, 1])
def qs(x): return mp.quad(lambda t: (x + t) / abs(x - t), [0, 1]) / (1 - x)
def qt(x): return -1 / abs(1 - x)
def closed(x):
    if x > 1: return (1 + x**2) / (1 - x) * mp.log(x / (x - 1)) + 1
    return -(1 + x**2) / (1 - x) * mp.log(-x / (1 - x)) - 1
mp.mp.dps = 30
ok = True
for x in [1.05, 1.3, 2.0, 5.0, 40.0, -0.01, -0.4, -1.0, -3.0, -25.0]:
    x = mp.mpf(x); s = qv(x) + qs(x) + qt(x)
    ok &= abs(s - closed(x)) < mp.mpf('1e-20')
check("C4 vertex + two sails + tadpole = closed forms (VF-LAM-7) for 10 values of xi outside [0,1]", ok)
# analytic y-integrals (xi>1): int (1-y)/(xi-y) = (1-xi)ln(xi/(xi-1)) + 1 ; int (xi+y)/(xi-y) = 2 xi ln(xi/(xi-1)) - 1
xs = sp.Symbol('xs', positive=True)   # xs > 1
ia = sp.integrate((1 - y) / (xs - y), (y, 0, 1)); ib = sp.integrate((xs + y) / (xs - y), (y, 0, 1))
check("C4 analytic: int_0^1 (1-y)/(xi-y) = (1-xi) ln(xi/(xi-1)) + 1 (xi>1)",
      abs(complex((ia - ((1 - xs) * sp.log(xs / (xs - 1)) + 1)).subs(xs, 2.7))) < 1e-12)
check("C4 analytic: int_0^1 (xi+y)/(xi-y) = 2 xi ln(xi/(xi-1)) - 1 (xi>1)",
      abs(complex((ib - (2 * xs * sp.log(xs / (xs - 1)) - 1)).subs(xs, 2.7))) < 1e-12)

# ---------------------------------------------------------------- C5: independent route via the ln z^2 coefficient
# q~(xi) for xi outside [0,1] = -a int_0^1 dalpha A(alpha)/|xi-alpha|, A = 3/2 delta(1-alpha) - [B]_+
def route2(x):
    x = mp.mpf(x)
    term_delta = mp.mpf(3) / 2 / abs(x - 1)
    term_plus = mp.quad(lambda t: (1 + t**2) / (1 - t) * (1 / abs(x - t) - 1 / abs(x - 1)), [0, 1])
    return -(term_delta - term_plus)
ok = all(abs(route2(x) - closed(mp.mpf(x))) < mp.mpf('1e-18') for x in [1.2, 3.0, 11.0, -0.3, -2.0, -9.0])
check("C5 FT of the ln z^2 term of the coordinate kernel reproduces the unphysical-region quasi-PDF", ok)

# ---------------------------------------------------------------- C6: tadpole
eps = sp.Symbol('epsilon', positive=True)
# DR Wilson-line self-energy (book conventions): -g^2 C_F mu^{2eps} Gamma(1-eps)/(4 pi^{2-eps}) |z|^{2eps} * 1/(2eps(2eps-1))
tad = -g**2 * CF * sp.gamma(1 - eps) / (4 * sp.pi**(2 - eps)) * sp.Symbol('X')**eps / (2 * eps * (2 * eps - 1))   # X = mu^2 z_3^2
ser = sp.series(tad / a_sym, eps, 0, 1).removeO()
coeffX = sp.simplify(sp.diff(ser, sp.Symbol('X')) * sp.Symbol('X'))
check("C6 DR Wilson-line self-energy: coefficient of ln(mu^2 z_3^2) is +a (pole +a/eps)", sp.simplify(coeffX - 1) == 0,
      sp.simplify(ser))
# double integral int_0^1 ds1 int_0^s1 ds2 (s1-s2)^(-2+2eps) = 1/(2eps(2eps-1))
s1, s2 = sp.symbols('s1 s2', positive=True)
dbl = sp.integrate(sp.integrate((s1 - s2)**(-2 + 2 * sp.Rational(3, 1)), (s2, 0, s1)), (s1, 0, 1))   # eps=3 test (convergent)
check("C6 int ds1 ds2 (s1-s2)^(2eps-2) = 1/(2eps(2eps-1)) (checked at eps=3)", sp.simplify(dbl - sp.Rational(1, 6 * 5)) == 0)
# FT[ln zeta^2](u) = -1/|u| for u != 0 : check int dzeta/(2pi) e^{i u zeta} ln(zeta^2) e^{-eta|zeta|} -> -1/|u|
def ft_log(u, eta):
    f = lambda z: mp.cos(u * z) * mp.log(z**2) * mp.exp(-eta * z)
    return 2 * mp.quadosc(f, [0, mp.inf], omega=u) / (2 * mp.pi)
vals = [ft_log(mp.mpf(1.7), mp.mpf(eta)) for eta in ('1e-3', '1e-4')]
check("C6 FT[ln zeta^2](u=1.7) -> -1/|u| (regulator e^{-eta|zeta|}, eta -> 0)", abs(vals[-1] + 1 / mp.mpf(1.7)) < 1e-3,
      [mp.nstr(v, 8) for v in vals])

# ---------------------------------------------------------------- D: endpoint structure
Lz_ = sp.Symbol('L_zeta')   # = -ell_p
xi_ = sp.Symbol('xi', positive=True)
inner = (1 + xi_**2) / (1 - xi_) * (Lz_ + sp.log(xi_ * (1 - xi_))) - xi_ * (1 + xi_) / (1 - xi_)       # 0<xi<1, -ell_p = L_zeta
target_in = 2 / (1 - xi_) * (Lz_ + sp.log(1 - xi_) - 1)
dif = sp.simplify((inner - target_in) * (1 - xi_))
check("D 0<xi<1: C^MS -> 2a/(1-xi) (L_zeta + ln(1-xi) - 1) + O(1) (remainder x (1-xi) -> 0)",
      sp.limit(dif, xi_, 1, '-') == 0)
outer = (1 + xi_**2) / (1 - xi_) * sp.log(xi_ / (xi_ - 1)) + 1 + sp.Rational(3, 2) / xi_ - sp.Rational(3, 2) / xi_
target_out = 2 * sp.log(xi_ - 1) / (xi_ - 1)
dif2 = sp.simplify((outer - target_out) * (xi_ - 1))
check("D xi>1: C^MS -> 2a ln(xi-1)/(xi-1) + O(1)", sp.limit(dif2, xi_, 1, '+') == 0)
# combined form: a(L_zeta-1)[P 1/(1-xi) + P 1/|1-xi|] + a P ln((1-xi)^2)/|1-xi|
for xv, side in ((0.7, 'in'), (1.4, 'out')):
    comb = (sp.Symbol('Lz') - 1) * (1 / (1 - xv) + 1 / abs(1 - xv)) + sp.log((1 - xv)**2) / abs(1 - xv)
    ref = (2 / (1 - xv) * (sp.Symbol('Lz') + sp.log(1 - xv) - 1)) if side == 'in' else 2 * sp.log(xv - 1) / (xv - 1)
    check("D combined endpoint form reproduces the %s-region singular term at xi=%.1f" % (side, xv),
          abs(complex(sp.expand(comb - ref).subs(sp.Symbol('Lz'), 0.37))) < 1e-12)

# ---------------------------------------------------------------- E: momentum RGE
# ell_p = ln(mu^2/(4 y^2 P_z^2)) ; P^z d ell_p/dP^z = -2 ; C^MS depends on ell_p through
# a[(1+xi^2)/(1-xi)]_+ (-ell_p) + a delta (3/2) ell_p  =>  P^z dC/dP^z = 2a{[(1+xi^2)/(1-xi)]_+ - 3/2 delta}
Pzs, mu, ys = sp.symbols('P_z mu y', positive=True)
ellp = sp.log(mu**2 / (4 * ys**2 * Pzs**2))
check("E P^z d ell_p/dP^z = -2", sp.simplify(Pzs * sp.diff(ellp, Pzs) + 2) == 0)
check("E 2a = alpha_s C_F/pi  (so P^z d q~/dP^z = (alpha_s C_F/pi)[[(1+xi^2)/(1-xi)]_+ - 3/2 delta] (x) f)",
      sp.simplify(2 * sp.Symbol('as') * sp.Symbol('CF') / (2 * sp.pi) - sp.Symbol('as') * sp.Symbol('CF') / sp.pi) == 0)

# ---------------------------------------------------------------- F: tails
w = sp.Symbol('w', positive=True)
CMS_out_pos = (1 + xi**2) / (1 - xi) * sp.log(xi / (xi - 1)) + 1           # xi>1 (the 3/(2xi) inside/outside cancel off xi=1)
CMS_out_neg = -(1 + xi**2) / (1 - xi) * sp.log(-xi / (1 - xi)) - 1         # xi<0
CR_out_pos = CMS_out_pos - sp.Rational(3, 2) / (1 - xi)
CR_out_neg = CMS_out_neg + sp.Rational(3, 2) / (1 - xi)
def tail(e, s): return sp.expand(sp.series(sp.simplify(e.subs(xi, s / w)), w, 0, 4).removeO())
t = [tail(CMS_out_pos, 1), tail(CMS_out_neg, -1), tail(CR_out_pos, 1), tail(CR_out_neg, -1)]
print("   tails (w = 1/|xi|):", t)
check("F C^MS -> -3a/(2|xi|) - (17a/6) sgn(xi)/xi^2 + ...",
      t[0].coeff(w, 1) == sp.Rational(-3, 2) and t[1].coeff(w, 1) == sp.Rational(-3, 2)
      and t[0].coeff(w, 2) == sp.Rational(-17, 6) and t[1].coeff(w, 2) == sp.Rational(17, 6))
check("F C^ratio -> -/+ 4a/(3 xi^2) (no 1/|xi| term)",
      t[2].coeff(w, 1) == 0 and t[3].coeff(w, 1) == 0 and t[2].coeff(w, 2) == sp.Rational(-4, 3) and t[3].coeff(w, 2) == sp.Rational(4, 3))
check("F coordinate-space reading: -3/(2|u|) is FT of (3/2) ln zeta^2 delta(1-alpha); ratio tail = int_0^1 alpha [B]_+ = -4/3",
      sp.integrate((al - 1) * B, (al, 0, 1)) == sp.Rational(-4, 3))

print("\nSUMMARY w25_s1_oneloop: %d PASS, %d FAIL" % (NP, NF))
