r"""
s1_formfactor.py  (writer W05, Ch5 prop:sudakov-oneloop, prop:sudakov-coulomb, prop:sudakov-kg(b),
cor:sudakov-exponentiation; VF-SUD-1, VF-SUD-2, VF-SUD-3, VF-EE-4)

Independent re-derivation, in the conventions of the book (D_mu = d_mu - i g A, vertex i g gamma^mu t^a,
Feynman gauge, CDR, D = 4 - 2 eps, MSbar with S_eps = (4 pi)^eps e^{-eps gamma_E}), of the one-loop massless
on-shell quark form factor exact in eps, step by step as printed in the proof:

 (1) D-dimensional Dirac algebra: gamma^nu a gamma^mu b gamma_nu = -2 b gamma^mu a + (4-D) a gamma^mu b
     (symbolic Clifford-algebra normal ordering in general D);
 (2) spinor sandwiches  ubar(p2) a gamma^mu b u(p1)  for a=(1-x)p1-y p2, b=(1-y)p2-x p1  (numerical, explicit
     Dirac matrices and massless spinors);
 (3) master integrals from the master formula of def:qcd-dimreg;
 (4) Dirichlet integrals over Feynman parameters (symbolic + numerical);
 (5) assembly: F1 = G(eps) * [ -(2-eps+2eps^2)/(eps^2(1-2eps)) ]  with UV part (1-eps)/(eps(1-2eps)) and
     IR part -[2/(eps^2(1-2eps)) + 1/(1-2eps)];
 (6) Laurent expansion vs VF-SUD-1 and vs Moch-Vermaseren-Vogt 2005 eq. (3.5) through eps^4;
 (7) time-like continuation, 2 Re F1, Im F1 (VF-SUD-2, VF-EE-4); pi^2 difference; numerical size at alpha_s=0.118;
 (8) K and G at one loop (VF-SUD-3) and their mu dependence; Collins 1989 eq. (82);
 (9) solution of the K+G equation with the D-dimensional running coupling reproduces F1 exactly in eps.
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np
import mpmath as mp

PASS = []
def check(name, ok, info=''):
    PASS.append(bool(ok))
    print(('[PASS] ' if ok else '[FAIL] ') + name + ((' : ' + str(info)) if info != '' else ''))

eps, D = sp.symbols('epsilon D')
x, y = sp.symbols('x y', positive=True)

# ---------------------------------------------------------------- (1) Clifford algebra in D dimensions
# words of slashed vectors / free index 'mu'; normal ordering by anticommutation {a,b}=2 a.b
VEC = ['a', 'b', 'c', 'mu']
def dot(u, v):
    if u == 'mu' and v == 'mu':
        return D
    return sp.Symbol('(%s.%s)' % tuple(sorted([u, v])))
def normal_order(expr):
    """expr: dict word(tuple)->coeff. Return normal-ordered dict (words sorted by VEC order)."""
    out = {}
    stack = list(expr.items())
    while stack:
        w, c = stack.pop()
        for i in range(len(w) - 1):
            if VEC.index(w[i]) > VEC.index(w[i + 1]):
                # w = ...u v... ,  u v = 2 u.v - v u
                u, v = w[i], w[i + 1]
                w1 = w[:i] + w[i + 2:]
                w2 = w[:i] + (v, u) + w[i + 2:]
                stack.append((w1, 2 * dot(u, v) * c))
                stack.append((w2, -c))
                break
            if w[i] == w[i + 1]:          # u u = u.u
                stack.append((w[:i] + w[i + 2:], dot(w[i], w[i]) * c))
                break
        else:
            out[w] = sp.expand(out.get(w, 0) + c)
    return {k: v for k, v in out.items() if sp.simplify(v) != 0}
def contract(word):
    """gamma^nu word gamma_nu via recursion C(S g^al) = 2 g^al S - C(S) g^al,  C() = D."""
    if len(word) == 0:
        return {(): D}
    S, al = word[:-1], word[-1]
    res = {}
    res[(al,) + S] = 2
    for w, c in contract(S).items():
        res[w + (al,)] = res.get(w + (al,), 0) - c
    return normal_order(res)
lhs = contract(('a', 'mu', 'b'))
rhs = normal_order({('b', 'mu', 'a'): -2, ('a', 'mu', 'b'): 4 - D})
diff = normal_order({**{k: v for k, v in lhs.items()}, **{}})
ok = all(sp.simplify(lhs.get(k, 0) - rhs.get(k, 0)) == 0 for k in set(lhs) | set(rhs))
check('(1) gamma^nu a gamma^mu b gamma_nu = -2 b gamma^mu a + (4-D) a gamma^mu b  (general D)', ok)
lhs2 = contract(('a', 'mu', 'a'))   # used for l gamma^mu l -> l^2/D * gamma^nu gamma^mu gamma_nu = (2-D) l^2/D gamma^mu
check('(1) gamma^nu gamma^mu gamma_nu = (2-D) gamma^mu', sp.simplify(contract(('mu',)).get(('mu',), 0) - (2 - D)) == 0)

# ---------------------------------------------------------------- (2) spinor sandwiches (4D numerics)
g0 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]], dtype=complex)
sig = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]])]
gam = [g0] + [np.block([[np.zeros((2, 2)), s], [-s, np.zeros((2, 2))]]).astype(complex) for s in sig]
metric = np.diag([1., -1., -1., -1.])
def slash(p):
    return sum(metric[m, m] * p[m] * gam[m] for m in range(4))
def u_massless(p, h):
    # basis vector of the two-dimensional kernel of pslash (pslash is nilpotent for p^2=0: use the SVD)
    M = slash(p)
    U, S, Vh = np.linalg.svd(M)
    ker = Vh.conj().T[:, -2:]
    assert np.allclose(M @ ker, 0, atol=1e-12)
    return ker[:, h]
rng = np.random.default_rng(1)
okall = True
for trial in range(5):
    n1 = rng.normal(size=3); n1 /= np.linalg.norm(n1)
    n2 = rng.normal(size=3); n2 /= np.linalg.norm(n2)
    E1, E2 = rng.uniform(1, 3), rng.uniform(1, 3)
    p1 = np.array([E1, *(E1 * n1)]); p2 = np.array([E2, *(E2 * n2)])
    Q2 = 2 * (p1 @ metric @ p2)       # 2 p1.p2 = Q^2 (space-like form factor, q = p2 - p1)
    xx, yy = rng.uniform(0, 0.5, size=2)
    a = (1 - xx) * p1 - yy * p2
    b = (1 - yy) * p2 - xx * p1
    for h1 in range(2):
        for h2 in range(2):
            u1 = u_massless(p1, h1); u2 = u_massless(p2, h2)
            ub2 = u2.conj() @ g0
            for mu in range(4):
                ref = ub2 @ gam[mu] @ u1
                s1 = ub2 @ slash(a) @ gam[mu] @ slash(b) @ u1
                s2 = ub2 @ slash(b) @ gam[mu] @ slash(a) @ u1
                okall &= abs(s1 - (-(1 - xx) * (1 - yy) * Q2 * ref)) < 1e-10 * (1 + abs(Q2 * ref))
                okall &= abs(s2 - (-xx * yy * Q2 * ref)) < 1e-10 * (1 + abs(Q2 * ref))
check('(2) ubar2 a g^mu b u1 = -(1-x)(1-y)Q^2 ubar2 g^mu u1 ;  ubar2 b g^mu a u1 = -x y Q^2 ubar2 g^mu u1', okall)

# ---------------------------------------------------------------- (3) master integrals
# master formula (def:qcd-dimreg): Int d^Dk/(i pi^{D/2}) (-k^2+Delta-i0)^{-n} = Gamma(n-D/2)/Gamma(n) Delta^{D/2-n}
# Hence Int d^Dl/(2pi)^D (l^2-Delta)^{-3} = -i/(4pi)^{D/2} Gamma(1+eps)/2 Delta^{-1-eps}
#       Int d^Dl/(2pi)^D l^2 (l^2-Delta)^{-3} = +i/(4pi)^{D/2} (D/4) Gamma(eps) Delta^{-eps}
Dl = 4 - 2 * eps
Delta = sp.Symbol('Delta', positive=True)
M = lambda n: sp.gamma(n - Dl / 2) / sp.gamma(n) * Delta ** (Dl / 2 - n)   # times i/(4pi)^{D/2}
I3 = (-1) ** 3 * M(3)                       # coefficient of i/(4pi)^{D/2}
I3l2 = (-1) ** 3 * (-1) * (M(2) - Delta * M(3))   # l^2 = -( -l^2+Delta) + Delta
check('(3) Int (l^2-Delta)^-3 = -Gamma(1+eps)/2 Delta^{-1-eps} [x i/(4pi)^{D/2}]',
      sp.simplify(sp.gammasimp(I3 - (-sp.gamma(1 + eps) / 2 * Delta ** (-1 - eps)))) == 0)
check('(3) Int l^2 (l^2-Delta)^-3 = (D/4) Gamma(eps) Delta^{-eps} [x i/(4pi)^{D/2}]',
      sp.simplify(sp.gammasimp(I3l2 - ((Dl / 4) * sp.gamma(eps) * Delta ** (-eps)))) == 0)

# ---------------------------------------------------------------- (4) Dirichlet integrals
def dirichlet(a1, a2, a3):
    return sp.gamma(a1) * sp.gamma(a2) * sp.gamma(a3) / sp.gamma(a1 + a2 + a3)
IA = dirichlet(1 - eps, 1 - eps, 1)                  # Int dF (xy)^{-eps}
IB1 = dirichlet(-eps, -eps, 2)                        # Int dF (xy)^{-1-eps} z
# numerical check at eps=-0.3 (IR-convergent) and eps=+0.3
for ev in [-0.3, 0.2]:
    num_A = mp.quad(lambda X: mp.quad(lambda Y: (X * Y) ** (-ev), [0, 1 - X]), [0, 1])
    okA = abs(num_A - float(IA.subs(eps, ev))) < 1e-8
    check('(4) Dirichlet Int dF (xy)^{-eps}, eps=%g' % ev, okA, (float(num_A), float(IA.subs(eps, ev))))
ev = -0.3
aa = -ev   # integrand x^{aa-1} y^{aa-1} z ; substitute x = u^{1/aa}, y = (1-x) v^{1/aa}
num_B = mp.quad(lambda U: mp.quad(lambda V: (1 / aa) ** 2 * (1 - U ** (1 / aa)) ** aa * (1 - U ** (1 / aa)) * (1 - V ** (1 / aa)), [0, 1]), [0, 1])
check('(4) Dirichlet Int dF (xy)^{-1-eps} z, eps=-0.3', abs(num_B - float(IB1.subs(eps, ev))) < 1e-7,
      (float(num_B), float(IB1.subs(eps, ev))))
# (1-x)(1-y) = z + x y  (z = 1-x-y)
check('(4) (1-x)(1-y) = z + x y', sp.expand((1 - x) * (1 - y) - ((1 - x - y) + x * y)) == 0)

# ---------------------------------------------------------------- (5) assembly
# Lambda^mu = -i g^2 C_F Int d^Dk/(2pi)^D N^mu/[k^2 (p1-k)^2 (p2-k)^2];  (ig)^2 * i * i * (-i) = -i g^2
pref = sp.expand((sp.I) ** 2 * sp.I * sp.I * (-sp.I))
check('(5) (i g)^2 (i)(i)(-i) = -i g^2  [two vertices, two quark propagators, gluon propagator]',
      sp.simplify(pref - (-sp.I)) == 0)
# after Feynman parameters (factor 2 Int dF) and shift: numerator -> [(2-D)^2/D l^2 + (2(1-x)(1-y)-(4-D)xy) Q^2] gamma^mu
# F1 * (4pi)^{D/2}/(g^2 C_F) (Q^2)^{eps} = 2 Int dF { (2-D)^2/D * (D/4)Gamma(eps)(xy)^{-eps}  - [2(1-x)(1-y)-(4-D)xy] Gamma(1+eps)/2 (xy)^{-1-eps} }
# the factor (-i)*(i) from the l^2 integral and (-i)*(-i) from the constant term have been included:
#   -i * ( i (D/4) Gamma(eps) ...) = + (D/4)Gamma(eps)...   ;   -i * (-i Gamma(1+eps)/2 ...) = - Gamma(1+eps)/2 ...
termA = 2 * ((2 - Dl) ** 2 / Dl) * (Dl / 4) * sp.gamma(eps) * IA
termB = -2 * (sp.gamma(1 + eps) / 2) * (2 * (IB1 + IA) - 2 * eps * IA)   # (4-D)=2 eps
Gfac = sp.gamma(1 + eps) * sp.gamma(1 - eps) ** 2 / sp.gamma(1 - 2 * eps)
A_red = sp.simplify(sp.gammasimp(termA / Gfac))
B_red = sp.simplify(sp.gammasimp(termB / Gfac))
check('(5) UV term A = G(eps) (1-eps)/(eps(1-2eps))', sp.simplify(A_red - (1 - eps) / (eps * (1 - 2 * eps))) == 0, A_red)
check('(5) IR term B = -G(eps)[2/(eps^2(1-2eps)) + 1/(1-2eps)]',
      sp.simplify(B_red + (2 / (eps ** 2 * (1 - 2 * eps)) + 1 / (1 - 2 * eps))) == 0, B_red)
total = sp.simplify(A_red + B_red)
check('(5) A+B = -(2-eps+2eps^2)/(eps^2(1-2eps))', sp.simplify(total + (2 - eps + 2 * eps ** 2) / (eps ** 2 * (1 - 2 * eps))) == 0, sp.factor(total))
# MSbar factor: g0^2 = 4 pi alpha_s mu^{2eps} e^{eps gE} (4pi)^{-eps}: g0^2/(4pi)^{D/2} = alpha_s/(4pi) mu^{2eps} e^{eps gE}
asym, mu2, gE = sp.symbols('alpha_s mu2 gamma_E', positive=True)
g02 = 4 * sp.pi * asym * mu2 ** eps * sp.exp(eps * sp.EulerGamma) * (4 * sp.pi) ** (-eps)
check('(5) g0^2/(4pi)^{2-eps} = alpha_s/(4pi) mu^{2eps} e^{eps gamma_E}',
      sp.simplify(g02 / (4 * sp.pi) ** (2 - eps) - asym / (4 * sp.pi) * mu2 ** eps * sp.exp(eps * sp.EulerGamma)) == 0)

# ---------------------------------------------------------------- (6) Laurent expansion
f_exact = sp.exp(eps * sp.EulerGamma) * Gfac * (-(2 - eps + 2 * eps ** 2) / (eps ** 2 * (1 - 2 * eps)))
NORD = 8
def lngam1(xx):   # ln Gamma(1+x) = -gamma x + sum_{k>=2} (-1)^k zeta(k) x^k / k
    return -sp.EulerGamma * xx + sum((-1) ** k * sp.zeta(k) * xx ** k / k for k in range(2, NORD))
lnG = eps * sp.EulerGamma + lngam1(eps) + 2 * lngam1(-eps) - lngam1(-2 * eps)
Gexp = sp.series(sp.exp(sp.expand(lnG)), eps, 0, 7).removeO()
rat = sp.series(-(2 - eps + 2 * eps ** 2) / (eps ** 2 * (1 - 2 * eps)), eps, 0, 5).removeO()
ser = sp.expand(sp.series(sp.expand(Gexp * rat), eps, 0, 5).removeO())
fe_ser = ser
z2, z3, z5 = sp.zeta(2), sp.zeta(3), sp.zeta(5)
vf = -2 / eps ** 2 - 3 / eps - 8 + z2 + eps * (-16 + sp.Rational(3, 2) * z2 + sp.Rational(14, 3) * z3)
low = sum(ser.coeff(eps, k) * eps ** k for k in range(-2, 2))
check('(6) VF-SUD-1 expansion through O(eps)', sp.simplify(sp.expand(low - vf)) == 0)
mvv = (-2 / eps ** 2 - 3 / eps - 8 + z2 + eps * (-16 + sp.Rational(3, 2) * z2 + sp.Rational(14, 3) * z3)
       + eps ** 2 * (-32 + 4 * z2 + 7 * z3 + sp.Rational(47, 20) * z2 ** 2)
       + eps ** 3 * (-64 + 8 * z2 + sp.Rational(56, 3) * z3 + sp.Rational(141, 40) * z2 ** 2 - sp.Rational(7, 3) * z2 * z3 + sp.Rational(62, 5) * z5)
       + eps ** 4 * (-128 + 16 * z2 + sp.Rational(112, 3) * z3 + sp.Rational(47, 5) * z2 ** 2 - sp.Rational(7, 2) * z2 * z3
                     + sp.Rational(93, 5) * z5 + sp.Rational(949, 280) * z2 ** 3 - sp.Rational(49, 9) * z3 ** 2))
dser = sp.expand(ser - mvv)
num = [complex(sp.N(dser.coeff(eps, k), 30)) for k in range(-2, 5)]
check('(6) exact one-loop form factor = MVV 2005 eq. (3.5) through eps^4', max(abs(v) for v in num) < 1e-25, num)

# ---------------------------------------------------------------- (7) time-like continuation
s_, mu = sp.symbols('s mu', positive=True)
ell = sp.Symbol('ell', real=True)   # ell = ln(s/mu^2) or ln(Q^2/mu^2)
# (-q^2 - i0)^{-eps} with q^2 = s>0  ->  s^{-eps} e^{i pi eps}
for ev in [0.1, -0.2, 0.37]:
    val = mp.power(mp.mpc(-1.7, -1e-30), -ev)
    ref = mp.power(1.7, -ev) * mp.e ** (1j * mp.pi * ev)
    check('(7) (-s-i0)^{-eps} = s^{-eps} e^{i pi eps}, eps=%g' % ev, abs(val - ref) < 1e-14)
fe = sp.expand(sum(fe_ser.coeff(eps, k) * eps ** k for k in range(-2, 2)))   # truncated: enough for O(eps^0) results
# 2 Re F1 = (alpha_s C_F/(2pi)) (mu^2/s)^eps cos(pi eps) f(eps);  bracket = (mu^2/s)^eps cos(pi eps) f
br_tl = sp.expand(sp.series(sp.exp(-eps * ell) * sp.cos(sp.pi * eps) * fe, eps, 0, 1).removeO())
vf_tl = -2 / eps ** 2 + (2 * ell - 3) / eps - ell ** 2 + 3 * ell - 8 + z2 + sp.pi ** 2
check('(7) 2Re F1(s+i0) = (a C_F/2pi)[-2/e^2+(2l-3)/e-l^2+3l-8+z2+pi^2]  (VF-EE-4)', sp.simplify(br_tl - vf_tl) == 0)
im_br = sp.expand(sp.series(sp.exp(-eps * ell) * sp.sin(sp.pi * eps) * fe, eps, 0, 1).removeO())
vf_im = -2 * sp.pi / eps + 2 * sp.pi * ell - 3 * sp.pi
check('(7) Im F1(s+i0) = (a C_F/4pi)[-2pi/e + 2pi l - 3pi]  (VF-EE-4)', sp.simplify(im_br - vf_im) == 0)
br_sl = sp.expand(sp.series(sp.exp(-eps * ell) * fe, eps, 0, 1).removeO())
vf_sl = -2 / eps ** 2 + (2 * ell - 3) / eps - ell ** 2 + 3 * ell - 8 + z2
check('(7) space-like F1 = (a C_F/4pi)[-2/e^2+(2l-3)/e-l^2+3l-8+z2] with l=ln(Q^2/mu^2) (VF-EE-4)', sp.simplify(br_sl - vf_sl) == 0)
check('(7) 2ReF1(time-like) - 2F1(space-like) at |q^2|=s:  (a C_F/2pi) pi^2  (VF-SUD-2)', sp.simplify(br_tl - br_sl - sp.pi ** 2) == 0)
d_exact = sp.series((sp.cos(sp.pi * eps) - 1) * fe, eps, 0, 2).removeO()
check('(7) (cos(pi eps)-1) f(eps) = pi^2 + O(eps): IR poles cancel in |F(s)/F(-s)|^2', sp.simplify(d_exact.subs(eps, 0) - sp.pi ** 2) == 0, sp.expand(d_exact))
a_mz = 0.1180
val = a_mz * (4 / 3) * np.pi / 2
check('(7) numerical size alpha_s C_F pi/2 at alpha_s=0.1180', abs(val - 0.24714) < 1e-4, round(val, 5))

# ---------------------------------------------------------------- (8) K and G at one loop
Lmu = sp.Symbol('L', real=True)       # L = ln(mu^2/Q^2)
F1 = sp.exp(eps * Lmu) * fe           # in units alpha_s C_F/(4pi)
dF = -eps * F1                         # d/dln Q^2 of (mu^2/Q^2)^eps
K = 4 / eps                            # units alpha_s C_F/(4pi):  K = (alpha_s C_F/(4pi)) 4/eps
Gfull = sp.simplify(2 * dF - K)
Gser = sp.expand(sp.series(Gfull, eps, 0, 1).removeO())
check('(8) G = (a C_F/2pi)(3 + 2 ln(mu^2/Q^2)) + O(eps)  i.e. (a C_F/4pi)(6+4L)', sp.simplify(Gser - (6 + 4 * Lmu)) == 0, Gser)
# Collins 1989 eq. (82): G = -(a C_F/pi)(ln(Q^2/mu^2) - 3/2)  -> in units a C_F/(4pi): -4(-L - 3/2) = 4L + 6
check('(8) agrees with Collins 1989 eq. (82)', sp.simplify(Gser - (-4 * (-Lmu - sp.Rational(3, 2)))) == 0)
# mu dG/dmu = 2 dG/dL ;  gamma_K = 2 C_F alpha_s/pi = 8 (alpha_s C_F/(4pi))
check('(8) mu dG/dmu = gamma_K = 2 C_F alpha_s/pi', sp.simplify(2 * sp.diff(Gser, Lmu) - 8) == 0)
# mu dK/dmu with mu d alpha_s/dmu = -2 eps alpha_s + O(alpha_s^2):  K ~ alpha_s 4/eps -> -8 alpha_s
check('(8) mu dK/dmu = -gamma_K (D-dim. beta function)', sp.simplify((-2 * eps) * K - (-8)) == 0)
# two-loop gamma_K vs Gamma_1 (VF-CONV-23) and Collins 1989 eq. (82)
CF, CA, TF, nf = sp.symbols('C_F C_A T_F n_f', positive=True)
Gam0 = 4 * CF
Gam1 = 4 * CF * ((sp.Rational(67, 9) - sp.pi ** 2 / 3) * CA - sp.Rational(20, 9) * TF * nf)
gK = 2 * (Gam0 * asym / (4 * sp.pi) + Gam1 * (asym / (4 * sp.pi)) ** 2)
gK_C89 = 2 * CF * asym / sp.pi + ((sp.Rational(67, 18) - sp.pi ** 2 / 6) * CF * CA - sp.Rational(10, 9) * nf * CF * TF) * (asym / sp.pi) ** 2
check('(8) gamma_K = 2 Gamma_cusp through two loops = Collins 1989 eq. (82)', sp.simplify(sp.expand(gK - gK_C89)) == 0)
G1num = float(Gam1.subs({CF: sp.Rational(4, 3), CA: 3, TF: sp.Rational(1, 2), nf: 5}))
check('(8) Gamma_1 = 36.8436 for n_f=5 (VF-CONV-23)', abs(G1num - 36.8436) < 5e-5, G1num)
G1wrong = float((4 * CF * ((sp.Rational(67, 9) - sp.pi ** 2 / 3) * CA - sp.Rational(20, 9) * CF * TF * nf)).subs({CF: sp.Rational(4, 3), CA: 3, TF: sp.Rational(1, 2), nf: 5}))
check('(8) BS (A.10) misprint (extra C_F) would give a different number', abs(G1wrong - G1num) > 1, G1wrong)

# ---------------------------------------------------------------- (9) solution of the K+G equation, exact in eps at one loop
# abar(xi^2) = alpha_s (mu^2/xi^2)^eps (lowest-order D-dim. running); bracket(xi^2) = K + G(1,abar) + 1/2 Int_{xi^2}^{mu^2} dl/l gamma_K(abar)
# with Int_{xi^2}^{mu^2} (dl/l)(mu^2/l)^eps = [(mu^2/xi^2)^eps - 1]/eps.  K = gamma_K/(2 eps) at one loop, so the constant cancels:
# bracket = (mu^2/xi^2)^eps [G1 + gamma_K/(2eps)],  ln F = 1/2 [G1 + gamma_K/(2 eps)] Int_0^{Q^2} dxi/xi (mu^2/xi^2)^eps
#        = 1/2 [G1 + gamma_K/(2eps)] (mu^2/Q^2)^eps / (-eps)   (eps < 0)
G1sym = sp.simplify((2 * (-eps) * f_exact - K))          # G(1,alpha,eps) exact in eps (units alpha C_F/(4pi))
gK1 = 8
check('(9) K = gamma_K/(2 eps) at one loop', sp.simplify(K - gK1 / (2 * eps)) == 0)
lnF_coeff = sp.simplify(sp.Rational(1, 2) * (G1sym + gK1 / (2 * eps)) / (-eps))
diffs = [abs(complex(sp.N((lnF_coeff - f_exact).subs(eps, ev_), 40))) for ev_ in [sp.Rational(-3, 10), sp.Rational(1, 7), sp.Rational(-1, 13)]]
check('(9) solution of the K+G equation reproduces F1 = (mu^2/Q^2)^eps f(eps) exactly in eps', max(diffs) < 1e-30, diffs)
# numerical cross-check of the xi^2 integral at eps=-0.3
ev = -0.3
G1v = complex(sp.N(G1sym.subs(eps, ev)))
Kv = 4 / ev
for qv, mv in [(2.0, 1.0), (7.0, 3.0)]:
    integrand = lambda t: (Kv + G1v * (mv / t) ** ev + 0.5 * gK1 * (((mv / t) ** ev - 1) / ev)) / t
    # substitute t = qv * w^(1/(-ev)) to remove the integrable endpoint singularity t^{-1-ev}
    pw = 1 / (-ev)
    val = 0.5 * mp.quad(lambda w_: integrand(qv * w_ ** pw) * qv * pw * w_ ** (pw - 1), [0, 1])
    tgt = (mv / qv) ** ev * complex(sp.N(f_exact.subs(eps, ev)))
    check('(9) numerical xi^2-integration (eps=-0.3, Q2=%g, mu2=%g)' % (qv, mv), abs(val - tgt) < 1e-10, (complex(val), tgt))

print('\n=== s1_formfactor: %d/%d PASS ===' % (sum(PASS), len(PASS)))
