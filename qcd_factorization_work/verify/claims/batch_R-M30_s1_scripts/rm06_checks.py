"""R-m06 checks (minor corrections m6, m8, m11 of the reference).

m6 (p. 34, Ex. 5.2): tree handbag numerator.  Which piece of (kslash + qslash) feeds the T_2 tensor
   structure (P^mu P^nu) and which feeds T_1 (g^{mu nu}) / gauge terms (q^mu ...)?
   Spin-averaged quark target, k = xi P, massless:  N^{mu nu} = (1/2) Tr[kslash gamma^mu (kslash+qslash) gamma^nu].
m8 (p. 49, Rem 7.5): Mellin moments of [ln^k(1-z)/(1-z)]_+ behave like (-1)^{k+1} ln^{k+1}(N)/(k+1) + ...,
   so alpha_s^n [ln^{2n-1}(1-z)/(1-z)]_+  <->  alpha_s^n ln^{2n} N; plain ln^{2n-1}(1-z) gives only ln^{2n-1}N / N.
m11 (p. 29): RG for the Adler function: a_n has degree n-1 for n >= 1 (a_0 constant); the n-th coefficient of
   Pi(-Q^2) has degree max(1, n) in L.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
import mpmath as mp

# ---------------- m6 ----------------
I2 = np.eye(2); Z2 = np.zeros((2, 2))
s = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
g = [np.block([[Z2, I2], [I2, Z2]]).astype(complex)] + [np.block([[Z2, si], [-si, Z2]]) for si in s]
eta = np.diag([1, -1, -1, -1.0])
def sl(p): return sum(eta[m, m]*p[m]*g[m] for m in range(4))
def dot(a, b): return a @ eta @ b
rng = np.random.default_rng(11)
P = np.array([1.3, 0.2, -0.1, 1.2]); P = P.copy(); P[0] = np.sqrt(P[1]**2+P[2]**2+P[3]**2)  # lightlike
xi = 0.4; k = xi*P
q = np.array([0.3, 0.7, -0.4, -1.1])   # generic spacelike q
Q2 = -dot(q, q); assert Q2 > 0
Pq = dot(P, q)
def Nmunu(vec):
    M = np.zeros((4, 4), complex)
    for mu in range(4):
        for nu in range(4):
            M[mu, nu] = 0.5*np.trace(sl(k) @ g[mu] @ sl(vec) @ g[nu])
    return M.real
Nk = Nmunu(k)          # piece from kslash in the propagator numerator
Nq = Nmunu(q)          # piece from qslash
# contravariant tensors: N^{mu nu} computed with gamma^mu (upper) -> compare with tensors built from upper vectors
gup = np.diag([1, -1, -1, -1.0])
# Decompose a symmetric tensor X^{mu nu} on the basis {g^{mu nu}, P^mu P^nu, (P^mu q^nu + q^mu P^nu), q^mu q^nu}
basis = [gup, np.outer(P, P), np.outer(P, q)+np.outer(q, P), np.outer(q, q)]
def decompose(X):
    A = np.array([b.flatten() for b in basis]).T
    coef, res, *_ = np.linalg.lstsq(A, X.flatten(), rcond=None)
    return coef, np.linalg.norm(A@coef - X.flatten())
ck, rk = decompose(Nk); cq, rq = decompose(Nq)
print("m6: (1/2)Tr[kslash g^mu kslash g^nu] = c_g g + c_PP PP + c_Pq (Pq+qP) + c_qq qq :", np.round(ck, 6), " resid", f"{rk:.1e}")
print("    expected 2 k^mu k^nu (k^2=0):  c_PP = 2 xi^2 =", 2*xi**2)
print("m6: (1/2)Tr[kslash g^mu qslash g^nu] = ", np.round(cq, 6), " resid", f"{rq:.1e}")
print("    expected k^mu q^nu + q^mu k^nu - g^{mu nu} k.q :  c_g = -xi P.q =", -xi*Pq, ", c_Pq = xi =", xi, ", c_PP = 0")
print("    => the T_2 (P^mu P^nu) structure comes ONLY from kslash; qslash feeds g^{mu nu} (T_1) and the q^mu (gauge) terms.")
# the gamma-index of the twist-2 operator: gamma^mu kslash gamma^nu = k^mu gamma^nu + k^nu gamma^mu - g^{mu nu} kslash - i eps gamma gamma5
lhs = [[g[mu] @ sl(k) @ g[nu] for nu in range(4)] for mu in range(4)]
ok = True
kup = k
g5 = 1j*g[0]@g[1]@g[2]@g[3]
for mu in range(4):
    for nu in range(4):
        sym = kup[mu]*g[nu] + kup[nu]*g[mu] - gup[mu, nu]*sl(k)
        anti = 0.5*(lhs[mu][nu] - lhs[nu][mu])
        symm = 0.5*(lhs[mu][nu] + lhs[nu][mu])
        ok &= np.allclose(symm, sym)
print("m6: symmetric part of gamma^mu kslash gamma^nu = k^mu gamma^nu + k^nu gamma^mu - g^{mu nu} kslash :", ok)

# ---------------- m8 ----------------
print()
mp.mp.dps = 30
def mellin_plus(kpow, N):
    # int_0^1 dz (z^{N-1}-1) ln^k(1-z)/(1-z)
    f = lambda z: (z**(N-1) - 1)*mp.log(1-z)**kpow/(1-z)
    return mp.quad(f, [0, 0.5, 0.9, 0.99, 0.999, 1])
def mellin_plain(kpow, N):
    f = lambda z: z**(N-1)*mp.log(1-z)**kpow
    return mp.quad(f, [0, 0.5, 0.9, 0.99, 0.999, 1])
for kpow in (1, 3):
    print(f"m8: k={kpow}:  N, M[(ln^k(1-z)/(1-z))_+](N), leading (-1)^(k+1) ln^(k+1)(N e^gE)/(k+1), ratio ;  plain ln^k(1-z) moment, ln^k(N)/N")
    for N in (10, 100, 1000, 10000):
        m = mellin_plus(kpow, N)
        lead = (-1)**(kpow+1)*mp.log(N*mp.e**mp.euler)**(kpow+1)/(kpow+1)
        mpl = mellin_plain(kpow, N)
        print(f"     N={N:6d}  {mp.nstr(m,10):>16}  {mp.nstr(lead,10):>16}  ratio={mp.nstr(m/lead,6)}   plain={mp.nstr(mpl,8):>14}  (-1)^k ln^k N/N={mp.nstr((-1)**kpow*mp.log(N)**kpow/N,8)}")
# exact large-N expansion check for k=1 with sympy: int (z^{N-1}-1) ln(1-z)/(1-z) = (1/2)[S1(N-1)^2 + S2(N-1)]  (harmonic sums)
N = 50
exact = 0.5*(sum(1/mp.mpf(j) for j in range(1, N))**2 + sum(1/mp.mpf(j)**2 for j in range(1, N)))
print("m8: k=1 exact harmonic-sum form at N=50:", mp.nstr(exact, 15), " numeric:", mp.nstr(mellin_plus(1, 50), 15))
print("    => alpha_s^n [ln^{2n-1}(1-z)/(1-z)]_+  <->  alpha_s^n ln^{2n} N ; plain ln^{2n-1}(1-z) is 1/N suppressed")

# ---------------- m11 ----------------
print()
L, a = sp.symbols('L a')
b0, b1 = sp.symbols('b0 b1')
# D = sum_n a_n(L) a^n with a = alpha_s(mu); RG: (mu d/dmu + beta(a) d/da) D = 0, L = ln(Q^2/mu^2) => mu d/dmu = -2 d/dL
# beta(a) = mu d a/d mu = -2 (b0 a^2 + b1 a^3 + ...)
nmax = 5
c = [sp.Symbol(f'c{n}') for n in range(nmax+1)]
an = [c[0]]   # a_0 constant
beta = -2*(b0*a**2 + b1*a**3)
D = sum(an[i]*a**i for i in range(len(an)))
for n in range(1, nmax+1):
    # determine a_n from d a_n/dL : coefficient of a^n in  -2 dD/dL + beta dD/da = 0
    an_try = sp.Function('A')(L)
    Dn = D + an_try*a**n
    eq = sp.expand(-2*sp.diff(Dn, L) + beta*sp.diff(Dn, a))
    coeff = eq.coeff(a, n)
    sol = sp.dsolve(sp.Eq(coeff, 0), an_try)
    an_n = sol.rhs.subs(sp.Symbol('C1'), c[n])
    an.append(sp.expand(an_n))
    D = D + an_n*a**n
for n, x in enumerate(an):
    print(f"m11: a_{n}(L) degree in L = {sp.degree(x, L) if x.has(L) else 0}")
# Pi: D = -12 pi^2 dPi/dL  =>  Pi_n = -(1/12pi^2) int a_n dL + const
for n, x in enumerate(an):
    Pin = -sp.integrate(x, L)/(12*sp.pi**2)
    print(f"m11: Pi_{n}(L) degree in L = {sp.degree(sp.expand(Pin), L)}   (max(1,n) = {max(1,n)})")
