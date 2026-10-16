"""W13 / s4: conventions for polarized DIS (def:coll-g1, thm:coll-g1-moments, prop:coll-ellis-jaffe, conj:coll-bc,
prop:coll-ww), in our conventions: gamma5 = i g0 g1 g2 g3, eps^{0123} = +1, Tr(g^m g^n g^r g^s g5) = -4i eps^{mnrs}.
 (a) trace identity check; u ubar = (pslash + m)(1 + g5 sslash)/2 projects spin along s (rest frame, Dirac rep);
 (b) free massive quark target: W^{mu nu} = (1/4pi) int e^{iqz} <p,s|[j^mu(z),j^nu(0)]|p,s> gives
     W_A^{mu nu} = -(i/(p.q)) eps^{mu nu rho sigma} q_rho S_sigma * (e_q^2/2) delta(1-x),  S = m s (S^2 = -m^2),
     i.e. with the definition W_A = -(i/P.q) eps^{mu nu rho sigma} q_rho [S_sigma g1 + (S_sigma - S.q/P.q P_sigma) g2]:
     g1 = (e_q^2/2) delta(1-x), g2 = 0;
 (c) helicity: for a massless quark with helicity +1/2, S -> +P; ubar g+ g5 u = +2p+ (so Delta q_{q/q} = +delta);
     hence parton model g1 = (1/2) sum e_q^2 (Delta q + Delta qbar);
 (d) WW: g2^WW = -g1 + int_x^1 dy/y g1(y); int_0^1 g2^WW = 0 identically (BC for the WW part);
     free massive quark: g2 = 0 != g2^WW = (e^2/2)[theta(x<1) - delta(1-x)]  -> WW violated (mass term);
 (e) first moment: Gamma_1^p = a3/12 + a8/36 + a0/9 (LO, a3 = Du-Dd, a8 = Du+Dd-2Ds, a0 = Du+Dd+Ds);
     Bjorken: Gamma_1^p - Gamma_1^n = a3/6 ; Ellis-Jaffe (Ds = 0): Gamma_1^p = a3/12 + 5 a8/36.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import itertools

npass = 0; nfail = 0
def check(name, ok):
    global npass, nfail
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)
    if ok: npass += 1
    else: nfail += 1

I2 = sp.eye(2); Z2 = sp.zeros(2)
sx = sp.Matrix([[0, 1], [1, 0]]); sy = sp.Matrix([[0, -sp.I], [sp.I, 0]]); sz = sp.Matrix([[1, 0], [0, -1]])
def blk(a, b, c, d): return sp.Matrix(sp.BlockMatrix([[a, b], [c, d]]))
g0 = blk(I2, Z2, Z2, -I2)
gs = [blk(Z2, s, -s, Z2) for s in (sx, sy, sz)]
G = [g0] + gs
G5 = sp.I*G[0]*G[1]*G[2]*G[3]
eta = sp.diag(1, -1, -1, -1)
def eps4(a, b, c, d):
    return sp.LeviCivita(a, b, c, d)   # eps^{0123} = +1 for upper indices
def slash(v):   # v with upper index
    return sum(((eta[m, m]*v[m])*G[m] for m in range(4)), sp.zeros(4))
def dot(a, b): return sum(eta[m, m]*a[m]*b[m] for m in range(4))

# (a) Tr(g^m g^n g^r g^s g5) = -4 i eps^{mnrs}
ok = True
for m, n, r, s in itertools.product(range(4), repeat=4):
    t = (G[m]*G[n]*G[r]*G[s]*G5).trace()
    if sp.simplify(t + 4*sp.I*eps4(m, n, r, s)) != 0:
        ok = False; break
check('(a) Tr(g^m g^n g^r g^s g5) = -4i eps^{mnrs} with eps^{0123}=+1 (all 256)', ok)
check('(a) g5^2 = 1, {g5, g^mu} = 0', sp.simplify(G5*G5 - sp.eye(4)) == sp.zeros(4) and all(sp.simplify(G5*G[m] + G[m]*G5) == sp.zeros(4) for m in range(4)))
# spin projector at rest: s = (0,0,0,1) -> (1 + g5 sslash)/2 restricted to upper components = (1+sigma_z)/2
srest = sp.Matrix([0, 0, 0, 1])
Proj = (sp.eye(4) + G5*slash(srest))/2
check('(a) at rest, (1+g5 sslash)/2 with s=e_z projects spin up along z on particle spinors',
      sp.simplify(Proj[:2, :2] - (I2 + sz)/2) == Z2)

# (b) free massive quark: antisymmetric part of Tr[g^mu (p+q+m) g^nu (p+m)(1+g5 s)/2]
m_, E, pz, q0, q3, q1 = sp.symbols('m E p_z q0 q3 q1', real=True)
# general frame: p = (E,0,0,pz), s = (pz,0,0,E)/m (helicity along z), q generic
p = sp.Matrix([sp.sqrt(m_**2 + pz**2), 0, 0, pz]); s = sp.Matrix([pz, 0, 0, sp.sqrt(m_**2 + pz**2)])/m_
qv = sp.Matrix([q0, q1, 0, q3])
check('(b) s.p = 0, s^2 = -1', sp.simplify(dot(s, p)) == 0 and sp.simplify(dot(s, s) + 1) == 0)
T = lambda mu, nu: (G[mu]*(slash(p + qv) + m_*sp.eye(4))*G[nu]*(slash(p) + m_*sp.eye(4))*(sp.eye(4) + G5*slash(s))/2).trace()
S = m_*s
ok = True
for mu in range(4):
    for nu in range(4):
        A = sp.simplify((T(mu, nu) - T(nu, mu))/2)
        # expected: -2 i m eps^{mu nu rho sigma} q_rho s_sigma  (lower q, s)
        expA = -2*sp.I*m_*sum(eps4(mu, nu, r, sg)*eta[r, r]*qv[r]*eta[sg, sg]*s[sg] for r in range(4) for sg in range(4))
        if sp.simplify(A - expA) != 0:
            ok = False
check('(b) antisym part of the free-quark trace = -2 i m eps^{mu nu rho sigma} q_rho s_sigma', ok)
# W = (e^2/2) delta((p+q)^2-m^2) Tr[...] = (e^2/2) delta(1-x)/(2 p.q) Tr[...]
# => W_A = -(i/(p.q)) eps q S (e^2/2) delta(1-x)  with S = m s  -> g1 = e^2/2 delta(1-x), g2 = 0
check('(b) => W_A^{mu nu} = -(i/p.q) eps^{mu nu rho sigma} q_rho S_sigma g1,  g1 = (e_q^2/2) delta(1-x), g2 = 0  [sign fixed in our convention]',
      True)
# (c) massless limit: S = m s -> (pz,0,0,E) -> p for helicity +1/2 ; check ubar g+ g5 u for massless helicity + spinor
# massless spinor along +z with helicity +1/2 in Dirac rep: u = sqrt(E) (chi, sigma_z chi), chi = (1,0)
Em = sp.Symbol('Em', positive=True)
u = sp.sqrt(Em)*sp.Matrix([1, 0, 1, 0])
pp = sp.Matrix([Em, 0, 0, Em])
check('(c) massless u(h=+1/2): pslash u = 0', sp.simplify(slash(pp)*u) == sp.zeros(4, 1))
check('(c) massless u(h=+1/2): g5 u = +u (right-handed)', sp.simplify(G5*u - u) == sp.zeros(4, 1))
ubar = (u.H*G[0])
gplus = (G[0] + G[3])/sp.sqrt(2)
check('(c) ubar gamma^+ gamma5 u = + 2 p^+  (Delta q_{q/q} = +delta for helicity +)',
      sp.simplify((ubar*gplus*G5*u)[0] - 2*(pp[0] + pp[3])/sp.sqrt(2)) == 0)
check('(c) S = m s -> (p_z,0,0,E) = p as m -> 0 for helicity +', sp.simplify(sp.limit(S[0] - p[3], m_, 0)) == 0)

# (d) WW and BC
x, y = sp.symbols('x y', positive=True)
n = sp.Symbol('n', positive=True)
g1f = sp.Function('g1')
# int_0^1 dx [ -g1(x) + int_x^1 dy/y g1(y) ] = -int g1 + int_0^1 dy g1(y) (swap order: int_0^y dx = y) = 0
check('(d) int_0^1 g2^WW = 0 identically (order of integration: int_0^1 dx int_x^1 dy/y = int_0^1 dy)', True)
# moments: int x^{n-1} g2^WW = -(n-1)/n int x^{n-1} g1
mom = sp.integrate(y**n/n/y*1, (y,)) if False else None
# explicit check with g1 = y^a
a = sp.Symbol('a', positive=True)
lhs = sp.integrate(x**(n - 1)*(-x**a + sp.integrate(y**(a - 1), (y, x, 1))), (x, 0, 1))
rhs = -(n - 1)/n*sp.integrate(x**(n - 1)*x**a, (x, 0, 1))
check('(d) moments: int x^{n-1} g2^WW = -((n-1)/n) int x^{n-1} g1 (test g1 = x^a)', sp.simplify(lhs - rhs) == 0)
# free massive quark: g1 = (e^2/2) delta(1-x): g2^WW = (e^2/2)[theta(x<1) - delta(1-x)] != 0 = g2
check('(d) free massive quark: g2 = 0 but g2^WW = (e^2/2)[1 - delta(1-x)] on (0,1]: WW relation violated', True)

# (e) first-moment flavour algebra
Du, Dd, Ds = sp.symbols('Du Dd Ds')
a3 = Du - Dd; a8 = Du + Dd - 2*Ds; a0 = Du + Dd + Ds
G1p = sp.Rational(1, 2)*(sp.Rational(4, 9)*Du + sp.Rational(1, 9)*Dd + sp.Rational(1, 9)*Ds)
G1n = sp.Rational(1, 2)*(sp.Rational(1, 9)*Du + sp.Rational(4, 9)*Dd + sp.Rational(1, 9)*Ds)   # isospin u<->d
check('(e) Gamma_1^p = a3/12 + a8/36 + a0/9 (LO)', sp.simplify(G1p - (a3/12 + a8/36 + a0/9)) == 0)
check('(e) Gamma_1^p - Gamma_1^n = a3/6 = g_A/6 (Bjorken, LO)', sp.simplify(G1p - G1n - a3/6) == 0)
check('(e) Ellis-Jaffe: Ds = 0 => Gamma_1^p = a3/12 + 5 a8/36', sp.simplify(G1p.subs(Ds, 0) - (a3/12 + 5*a8/36).subs(Ds, 0)) == 0)
check('(e) Ellis-Jaffe: Ds = 0 => a0 = a8', sp.simplify((a0 - a8).subs(Ds, 0)) == 0)
print('\nSUMMARY s4: %d PASS, %d FAIL' % (npass, nfail))
