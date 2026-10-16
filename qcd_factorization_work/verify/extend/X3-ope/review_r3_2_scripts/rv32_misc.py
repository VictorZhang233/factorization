"""rv32_misc.py -- reviewer r3-2: independent algebraic/numerical spot checks of the
fix-round-2 X3 report (journal line 128).

 (a) D1: beta_xi from xi_0 = Z_3 xi_R with one-loop MS-bar Z_3; value at xi=1, SU(3); never 0 for integer n_f
 (b) D1: s raises the D-dim canonical dimension by exactly 1 (d = d4 - eps (n_phi - n_g))
 (c) Thm B step 5: dimension of K_Y for Y = O' d^alpha dS/dphi equals that of the p^alpha coefficient of C^{s phi}_{O'}
     and the exponent formula 3 - d4_Y + eps c_{Y,m}, c = n_phi - n_g - 2 - m
 (d) Thm B step 3: eps'_k * (-1)^{(|phi_k|+1) sum_{l<k}|phi_l|} = eps_k for all parity strings (n <= 6)
 (e) Lemma F.7(a): T2 projector in odd D = 7 with explicit Minkowski vectors (p^2 = 0)
 (f) Lemma F.8: if p^a M_ab = alpha p_b and M_ab p^b = alpha' p_a then d^ab M_ab = -g^ab M_ab + alpha + alpha'
 (g) Cor F.2(b): |nu| <= p0 |q|_E and |Phat|_E^2 = 2 p0^2 - |nu|^2/Q^2 for Euclidean q, light-like p
 (h) Lemma 5.1: rest frame, Euclidean q: Phat^2 = M^2 |qvec|^2/Q^2, omega = 2 i M q4/Q^2
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np

ok_all = True
def report(name, ok):
    global ok_all
    ok_all &= bool(ok)
    print(f"{name}: {'PASS' if ok else 'FAIL'}")

# (a) ------------------------------------------------------------------
al, eps, xi, CA, TF, nf = sp.symbols('alpha epsilon xi C_A T_F n_f')
z = (sp.Rational(13, 6) - xi/2)*CA - sp.Rational(4, 3)*TF*nf
Z3 = 1 + al/(4*sp.pi*eps)*z
beta_al = -2*eps*al                       # leading term suffices at one loop
# 0 = mu d(Z3 xi)/dmu = xi*(dZ3/dal*beta_al + dZ3/dxi*beta_xi) + Z3*beta_xi ; solve to O(al)
bxi = sp.symbols('bxi')
sol = sp.solve(sp.Eq(xi*(sp.diff(Z3, al)*beta_al + sp.diff(Z3, xi)*bxi) + Z3*bxi, 0), bxi)[0]
b1 = sp.simplify(sp.series(sol, al, 0, 2).removeO())
target = al/(2*sp.pi)*xi*z
print("(a) beta_xi (one loop) =", sp.factor(b1))
report("(a) beta_xi = (alpha/2pi) xi [(13/6 - xi/2)C_A - (4/3)T_F n_f]", sp.simplify(b1 - target) == 0)
val = sp.simplify(target.subs({xi: 1, CA: 3, TF: sp.Rational(1, 2)})/(al/(2*sp.pi)))
print("    at xi=1, SU(3): beta_xi/(alpha/2pi) =", val)
report("(a) value 5 - 2 n_f/3 and nonzero for n_f = 0..16", sp.simplify(val - (5 - sp.Rational(2, 3)*nf)) == 0
       and all(val.subs(nf, k) != 0 for k in range(17)))

# (b) ------------------------------------------------------------------
# (d4, n_phi, n_g) of field and of its BRST variation (all terms)
table = {
    'A -> dc':        ((1, 1, 0), [(2, 1, 0)]),
    'A -> g[A,c]':    ((1, 1, 0), [(2, 2, 1)]),
    'psi -> g c psi': ((1.5, 1, 0), [(2.5, 2, 1)]),
    'c -> g c c':     ((1, 1, 0), [(2, 2, 1)]),
    'cbar -> B':      ((1, 1, 0), [(2, 1, 0)]),
}
e = sp.symbols('e')
okb = True
for k, (f, vs) in table.items():
    df = sp.nsimplify(f[0]) - e*(f[1] - f[2])
    for v in vs:
        dv = sp.nsimplify(v[0]) - e*(v[1] - v[2])
        okb &= sp.simplify(dv - df - 1) == 0
report("(b) s raises d(eps) = d4 - eps(n_phi - n_g) by exactly 1 for all generators", okb)

# (c) ------------------------------------------------------------------
dphi, dOp, alph, d4Y, nph, ng, m = sp.symbols('d_phi d_Op alpha_abs d4_Y n_phi n_g m')
Dd = 4 - 2*eps
J = 2 - 2*eps                 # [calJ(q)]
Ztil = (dphi + 1) - Dd        # Fourier transformed Z = s phi at momentum p_Z
dim_Cpa = J + Ztil - dOp - alph
dim_Y = dOp + alph + (Dd - dphi)
dim_K = 3 - 2*eps - dim_Y      # [C_O sO] = [calJ] + 1
report("(c) [K_Y] (Y = O' d^alpha dS/dphi) == dim of p^alpha coeff of C^{s phi}_{O'} = d_phi-1-d_O'-|alpha|",
       sp.simplify(dim_K - dim_Cpa) == 0 and sp.simplify(dim_Cpa - (dphi - 1 - dOp - alph)) == 0)
dimY_gen = d4Y - eps*(nph - ng)
expo = (3 - 2*eps - dimY_gen) - m*eps        # |q| exponent of the g0^m part of K_Y
report("(c) exponent = 3 - d4_Y + eps (n_phi - n_g - 2 - m)", sp.simplify(expo - (3 - d4Y + eps*(nph - ng - 2 - m))) == 0)

# (d) ------------------------------------------------------------------
okd = True
for nlen in range(1, 7):
    for par in itertools.product([0, 1], repeat=nlen):
        for k in range(nlen):
            S = sum(par[:k])
            epsp = (-1)**S
            move = (-1)**((par[k] + 1)*S)
            epsk = (-1)**(par[k]*S)
            okd &= (epsp*move == epsk)
report("(d) eps'_k * (-1)^{(|phi_k|+1) sum_{l<k}|phi_l|} == eps_k (all parity strings, n<=6)", okd)

# (e) ------------------------------------------------------------------
rng = np.random.default_rng(3)
def mink(D):
    g = -np.eye(D); g[0, 0] = 1.0; return g
D = 7
g = mink(D)
dot = lambda x, y: x @ g @ y
n_hat = rng.normal(size=D-1); n_hat /= np.linalg.norm(n_hat)
p = np.r_[1.3, 1.3*n_hat]                         # light-like
q = rng.normal(size=D) + 1j*rng.normal(size=D)     # generic complex q
nu = dot(p, q); q2 = dot(q, q); Q2 = -q2
T1, T2 = 0.37 - 1.1j, -0.8 + 0.45j
ginv = np.linalg.inv(g)
gt = ginv - np.outer(q, q)/q2                      # g~^{mu nu}
Ph = p - (nu/q2)*q
T = -gt*T1 + np.outer(Ph, Ph)*T2/nu                # upper indices
pl = g @ p                                         # lower p
S1 = pl @ T @ pl
S2 = np.sum(g*T)
T2rec = Q2**2*((D - 1)*S1 - (nu**2/Q2)*S2)/((D - 2)*nu**3)
print(f"(e) D=7: |p^2| = {abs(dot(p,p)):.1e}; T2 reconstructed = {T2rec:.12f}; input T2 = {T2:.12f}")
report("(e) Lemma F.7(a) projector reproduces T2 in D=7", abs(T2rec - T2) < 1e-10)

# (f) ------------------------------------------------------------------
D = 6
g = mink(D); ginv = np.linalg.inv(g); dot = lambda x, y: x @ g @ y
n_hat = rng.normal(size=D-1); n_hat /= np.linalg.norm(n_hat)
p = np.r_[0.9, 0.9*n_hat]                          # p^a (upper)
q = rng.normal(size=D) + 0.3j*rng.normal(size=D)
nu = dot(p, q); q2 = dot(q, q)
pl, ql = g @ p, g @ q                              # lower
# lower-index tensors M_ab with p^a M_ab = alpha p_b and M_ab p^b = alpha' p_a:
u = ql/nu                                          # u_a with u_a p^a = 1
Pi = np.eye(D) - np.outer(u, p)                    # Pi_a^c = delta - u_a p^c : p^a Pi_a^c = 0 ; Pi_a^c p_c? -> see below
N = rng.normal(size=(D, D)) + 1j*rng.normal(size=(D, D))
A = Pi @ N @ Pi.T                                  # A_ab = Pi_a^c N_cd Pi_b^d ; p^a A_ab = 0 = A_ab p^b
x = rng.normal(size=D) + 1j*rng.normal(size=D)     # lower vectors
y = rng.normal(size=D) + 1j*rng.normal(size=D)
M = A + np.outer(pl, x) + np.outer(y, pl)          # M_ab
alpha = p @ y                                      # p^a M_ab = (p.y) p_b   (p^a p_a = 0)
alphap = x @ p                                     # M_ab p^b = (x.p) p_a
chk1 = np.abs(p @ M - alpha*pl).max(); chk2 = np.abs(M @ p - alphap*pl).max()
d_up = -ginv + (np.outer(p, q) + np.outer(q, p))/nu - q2*np.outer(p, p)/nu**2   # d^{ab}
lhs = np.sum(d_up*M); rhs = -np.sum(ginv*M) + alpha + alphap
print(f"(f) OS-WI construction residuals {chk1:.1e}, {chk2:.1e}; d^ab M_ab = {lhs:.10f}; -g^ab M_ab + alpha + alpha' = {rhs:.10f}")
report("(f) Lemma F.8 step 3 identity", chk1 < 1e-10 and chk2 < 1e-10 and abs(lhs - rhs) < 1e-9)

# (g) ------------------------------------------------------------------
D = 4; g = mink(4); dot = lambda x, y: x @ g @ y
okg = True; worst = 0
for t in range(2000):
    n_hat = rng.normal(size=3); n_hat /= np.linalg.norm(n_hat)
    p0 = rng.uniform(0.1, 3); p = np.r_[p0, p0*n_hat]
    q4 = rng.normal()*rng.uniform(0.1, 5); qv = rng.normal(size=3)*rng.uniform(0.1, 5)
    q = np.r_[1j*q4, qv]                            # Euclidean q: q^0 = i q4
    qE = np.sqrt(q4**2 + qv @ qv); Q2 = -dot(q, q)
    nu = dot(p, q); Ph = p - (nu/dot(q, q))*q
    okg &= abs(Q2.imag) < 1e-12 and abs(Q2.real - qE**2) < 1e-9*qE**2
    okg &= abs(nu) <= p0*qE*(1 + 1e-12)
    PhE2 = np.sum(np.abs(Ph)**2)
    worst = max(worst, abs(PhE2 - (2*p0**2 - abs(nu)**2/Q2.real))/(2*p0**2))
okg &= worst < 1e-12
print(f"(g) 2000 random points: max rel. dev. of |Phat|_E^2 formula = {worst:.1e}")
report("(g) Cor F.2(b): Q^2 = |q|_E^2, |nu| <= p0|q|_E, |Phat|_E^2 = 2p0^2 - |nu|^2/Q^2 <= 2 p0^2", okg)

# (h) ------------------------------------------------------------------
okh = True
for t in range(500):
    Mm = rng.uniform(0.2, 2); P = np.r_[Mm, 0, 0, 0]
    q4 = rng.normal()*2; qv = rng.normal(size=3)*2; q = np.r_[1j*q4, qv]
    q2 = dot(q, q); Q2 = -q2; nu = dot(P, q)
    Ph = P - (nu/q2)*q
    okh &= abs(dot(Ph, Ph) - Mm**2*(qv @ qv)/Q2) < 1e-10*Mm**2
    okh &= abs(2*nu/Q2 - 2j*Mm*q4/Q2) < 1e-12*(1 + abs(2*nu/Q2))
report("(h) Lemma 5.1: Phat^2 = M^2|qvec|^2/Q^2 and omega = 2iMq4/Q^2", okh)

print("ALL PASS" if ok_all else "SOME CHECK FAILED")
