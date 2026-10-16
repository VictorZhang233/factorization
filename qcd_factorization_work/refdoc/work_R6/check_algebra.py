"""R6 checks: algebra of App. D (pp.128-161) of the reference document.
Checks: kinematics of (D.1)-(D.2), Example D.1 identities, (D.26)-(D.27) via per-line operator model,
product formula (Cor. D.13) on the triangle and on the 9-region poset of Fig. 63 with a coordinate-zeroing
model, Moebius/chain expansion, projector algebra (D.15),(D.16), Lemma D.38, expansions of A,B and (D.32).
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np

ok = True
def check(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok = ok and bool(cond)

# ---------------- kinematics (light-cone (+,-,T)) ----------------
P, Pp, m, kp, km, kT2 = sp.symbols('P Pp m kp km kT2', positive=True)
def dot(a, b):  # a=(plus,minus,T2-dot) ; we keep transverse as separate scalar products
    return a[0]*b[1] + a[1]*b[0] - a[2]
# k=(kp,km,kT); p1=(P,-m^2/2P,0); p2=(m^2/2Pp,-Pp,0)
k2 = 2*kp*km - kT2
p1k = P*km + (-m**2/(2*P))*kp
p2k = (m**2/(2*Pp))*km + (-Pp)*kp
p1sq = 2*P*(-m**2/(2*P)); p2sq = 2*(m**2/(2*Pp))*(-Pp)
check("p1^2=-m^2", sp.simplify(p1sq + m**2) == 0)
check("p2^2=-m^2", sp.simplify(p2sq + m**2) == 0)
Dg = -k2
D1 = m**2 + 2*p1k - k2
D2 = m**2 - 2*p2k - k2
check("D1 = -(p1-k)^2", sp.simplify(D1 - (-(p1sq - 2*p1k + k2))) == 0)
check("D2 = -(p2+k)^2", sp.simplify(D2 - (-(p2sq + 2*p2k + k2))) == 0)
# Q^2 = -(p1+p2)^2
p1p2 = P*(-Pp) + (-m**2/(2*P))*(m**2/(2*Pp))
Q2 = -(p1sq + p2sq + 2*p1p2)
Qt2 = 2*P*Pp
check("Q^2 = Qt^2 + 2m^2 + m^4/Qt^2", sp.simplify(Q2 - (Qt2 + 2*m**2 + m**4/Qt2)) == 0)
e1 = m**2 + 2*P*km; h1 = 2*P*km; t1 = 2*P*km - k2
e2 = m**2 + 2*Pp*kp; h2 = 2*Pp*kp; t2 = 2*Pp*kp - k2
check("T_S drops -(m^2/P)k+ - k^2 from D1", sp.simplify(D1 - e1 - (-(m**2/P)*kp - k2)) == 0)
check("e2-D2=(m^2/P')k^- + k^2", sp.simplify(e2 - D2 - ((m**2/Pp)*km + k2)) == 0)
check("T_H: D1(m->0)=t1", sp.simplify(D1.subs(m, 0) - t1) == 0)
check("T_H: D2(m->0)=t2", sp.simplify(D2.subs(m, 0) - t2) == 0)
check("h_i - t_i = k^2 = -Dg", sp.simplify(h1 - t1 - k2) == 0 and sp.simplify(h2 - t2 + Dg) == 0)

# Example D.1(a): C_C2 = (1/(Dg h1))(1/D2-1/e2) = m^2/(2PP') 1/(Dg D2 e2) - 1/(h1 D2 e2)
CC2 = (1/(Dg*h1))*(1/D2 - 1/e2)
CC2_claim = m**2/(2*P*Pp)/(Dg*D2*e2) - 1/(h1*D2*e2)
check("Ex D.1(a) C_C2 identity", sp.simplify(CC2 - CC2_claim) == 0)
# Ex D.1(b): (1-T_C1)T_S Gamma = 1/(Dg e1) (1/e2 - 1/h2), relative size m^2/h2
check("Ex D.1(b) relative factor", sp.simplify((1/e2 - 1/h2)/(1/e2) + m**2/h2) == 0)

# ---------------- per-line operator model for the triangle ----------------
# value of line i under label: '1' exact, 'e','t','h'
vals = {1: {'1': D1, 'e': e1, 't': t1, 'h': h1}, 2: {'1': D2, 'e': e2, 't': t2, 'h': h2}}
def comp(a, b):  # apply a after b (a o b) on a single line label
    if a == '1': return b
    if b == '1': return a
    if a == b: return a
    if 'h' in (a, b): return 'h'
    # remaining: {e,t}
    return 'h'
ops = {'S': ('e', 'e'), 'C1': ('1', 'h'), 'C2': ('h', '1'), 'H': ('t', 't')}
order = {('S', 'C1'), ('S', 'C2'), ('S', 'H'), ('C1', 'H'), ('C2', 'H')}  # (smaller, larger)
def less(a, b): return (a, b) in order
# operators act on formal linear combinations of label pairs: dict {(l1,l2): coeff}
def apply(op, vec):
    out = {}
    for (l1, l2), c in vec.items():
        n = (comp(op[0], l1), comp(op[1], l2))
        out[n] = out.get(n, 0) + c
    return {k: v for k, v in out.items() if v != 0}
def add(a, b, s=1):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + s*v
    return {k: v for k, v in out.items() if v != 0}
def value(vec):
    return sum(c/(Dg*vals[1][l1]*vals[2][l2]) for (l1, l2), c in vec.items())
Gam = {('1', '1'): 1}
regions = ['S', 'C1', 'C2', 'H']
C = {}
for R in regions:  # topological order
    X = dict(Gam)
    for Rp in regions:
        if less(Rp, R):
            X = add(X, C[Rp], -1)
    C[R] = apply(ops[R], X)
claims = {
    'S': 1/(Dg*e1*e2),
    'C1': (1/(Dg*h2))*(1/D1 - 1/e1),
    'C2': (1/(Dg*h1))*(1/D2 - 1/e2),
    'H': Dg/(t1*h1*t2*h2),
}
for R in regions:
    check(f"(D.26) C_{R} recursive = closed form", sp.simplify(value(C[R]) - claims[R]) == 0)
r = dict(Gam)
for R in regions:
    r = add(r, C[R], -1)
Del = lambda D, h: 1/D - 1/h
r_claim = (1/Dg)*(Del(D1, h1)*Del(D2, h2) - Del(e1, h1)*Del(e2, h2) - Del(t1, h1)*Del(t2, h2))
check("(D.27) remainder closed form", sp.simplify(value(r) - r_claim) == 0)
# (Com) and (Abs) on the triangle
def opmul(a, b): return (comp(a[0], b[0]), comp(a[1], b[1]))
com = all(opmul(ops[a], ops[b]) == opmul(ops[b], ops[a]) for a in regions for b in regions)
check("(Com) on triangle", com)
check("(Abs) T_C2 T_S T_C1 = T_C2 T_C1", opmul(ops['C2'], opmul(ops['S'], ops['C1'])) == opmul(ops['C2'], ops['C1']))
check("T_C1 T_S = (e1,h2) != T_S", opmul(ops['C1'], ops['S']) == ('e', 'h'))
# product formula: r = prod (1-T_R) Gamma
prod = dict(Gam)
for R in regions:
    prod = add(prod, apply(ops[R], prod), -1)
check("Cor D.13: r = prod(1-T_R) Gamma (triangle)", sp.simplify(value(prod) - value(r)) == 0)
# remainder at large k ~ m^2/|k|^6: scale all k by s
fr = sp.lambdify((P, Pp, m, kp, km, kT2), r_claim, 'mpmath')
import mpmath as mpm
mpm.mp.dps = 50
vals_s = [abs(fr(mpm.mpf('0.8'), mpm.mpf('1.3'), mpm.mpf('0.3'), mpm.mpf('0.37')*S_, mpm.mpf('0.61')*S_, mpm.mpf('0.29')*S_**2)) for S_ in (mpm.mpf(10)**4, mpm.mpf(10)**5)]
ratio = vals_s[0]/vals_s[1]
vals_m = [abs(fr(mpm.mpf('0.8'), mpm.mpf('1.3'), mm_, mpm.mpf('0.37')*1e5, mpm.mpf('0.61')*1e5, mpm.mpf('0.29')*1e10)) for mm_ in (mpm.mpf('0.3'), mpm.mpf('0.15'))]
print('  scaling ratio (expect 1e6):', mpm.nstr(ratio, 8), '  m-scaling ratio (expect 4):', mpm.nstr(vals_m[0]/vals_m[1], 8))
check("r ~ m^2/|k|^6 at large k (1% tol, finite-S corrections)", abs(ratio/1e6 - 1) < 1e-2 and abs(vals_m[0]/vals_m[1]/4 - 1) < 1e-2)

# ---------------- Fig. 63: two-loop planar vertex, 9 regions ----------------
# lines: k1,k2,o1=p1-k2,i1=p1-k1-k2,o2=p2+k2,i2=p2+k1+k2 ; modes H,A,B,S
lines = ['k1', 'k2', 'o1', 'i1', 'o2', 'i2']
R9 = {
 'HH':  dict(k1='H', k2='H', o1='H', i1='H', o2='H', i2='H'),
 'HC1': dict(k1='H', k2='A', o1='A', i1='H', o2='H', i2='H'),
 'HC2': dict(k1='H', k2='B', o1='H', i1='H', o2='B', i2='H'),
 'C1C1':dict(k1='A', k2='A', o1='A', i1='A', o2='H', i2='H'),
 'C2C2':dict(k1='B', k2='B', o1='H', i1='H', o2='B', i2='B'),
 'HS':  dict(k1='H', k2='S', o1='A', i1='H', o2='B', i2='H'),
 'C1S': dict(k1='A', k2='S', o1='A', i1='A', o2='B', i2='H'),
 'C2S': dict(k1='B', k2='S', o1='A', i1='H', o2='B', i2='B'),
 'SS':  dict(k1='S', k2='S', o1='A', i1='A', o2='B', i2='B'),
}
rank = {'S': 0, 'A': 1, 'B': 1, 'H': 2}
def mle(a, b):  # mode a <= b
    return a == b or a == 'S' or b == 'H'
def mmeet(a, b):
    if mle(a, b): return a
    if mle(b, a): return b
    return 'S'  # A ^ B
def rle(R, Rp): return all(mle(R9[R][j], R9[Rp][j]) for j in lines)
def rmeet(R, Rp):
    d = {j: mmeet(R9[R][j], R9[Rp][j]) for j in lines}
    for name, dd in R9.items():
        if dd == d: return name
    return None
closed = all(rmeet(a, b) is not None for a in R9 for b in R9)
check("Fig.63: 9 leading regions closed under per-line meet (A2)", closed)
# covering relations (Hasse diagram)
names = list(R9)
lt = {(a, b) for a in names for b in names if a != b and rle(a, b)}
cover = sorted((a, b) for (a, b) in lt if not any((a, c) in lt and (c, b) in lt for c in names))
print("  covering relations:", cover)
expected = sorted([('SS','C1S'),('SS','C2S'),('C1S','C1C1'),('C1S','HS'),('C2S','HS'),('C2S','C2C2'),
                   ('C1C1','HC1'),('HS','HC1'),('HS','HC2'),('C2C2','HC2'),('HC1','HH'),('HC2','HH')])
check("Fig.63 Hasse diagram as drawn", cover == expected)
check("meets quoted in Fig.63 caption",
      rmeet('C1C1', 'HS') == 'C1S' and rmeet('HC1', 'HC2') == 'HS' and rmeet('C1C1', 'C2C2') == 'SS')
# beta_R = 3^{h(R)-h*}
def height(R):
    below = [x for x in names if (x, R) in lt]
    return 0 if not below else 1 + max(height(x) for x in below)
hstar = 1 + max(height(R) for R in names if R != 'HH')
beta = {R: sp.Rational(3)**(height(R) - hstar) for R in names if R != 'HH'}
check("beta_R<=1/3 and R'<R=>beta_R>=3beta_R'",
      all(b <= sp.Rational(1, 3) for b in beta.values()) and
      all(beta[b] >= 3*beta[a] for (a, b) in lt if b != 'HH'))
print("  beta (Fig.63):", beta)

# product formula on 9-element poset with a coordinate-zeroing model satisfying (Com),(Abs):
# variables x_{j,c} for line j, component c in {plus,minus,T}; T_R zeroes:
#   line soft -> all comps; A -> minus,T ; B -> plus,T ; H -> none   (toy model)
comps = ['p', 'm', 'T']
zero = {'S': set(comps), 'A': {'m', 'T'}, 'B': {'p', 'T'}, 'H': set()}
X = {(j, c): sp.Symbol(f"x_{j}_{c}") for j in lines for c in comps}
def Top(R):
    return lambda f: f.subs({X[(j, c)]: 0 for j in lines for c in zero[R9[R][j]]}, simultaneous=True)
# generic integrand: random polynomial-like rational function with all variables
import random
random.seed(1)
F = sp.expand(sum(random.randint(1, 5)*sp.Mul(*random.sample(list(X.values()), 3)) for _ in range(40)) + sum(random.randint(1,3)*v for v in X.values()) + 1)
# check (Com) and (Abs) in model
def Tseq(seq, f):
    for R in reversed(seq): f = Top(R)(f)
    return f
abs_ok = True
for a in names:
    for b in names:
        if not rle(a, b) and not rle(b, a):
            mm = rmeet(a, b)
            if sp.expand(Tseq([a, b], F) - Tseq([a, mm, b], F)) != 0: abs_ok = False
check("toy model satisfies (Abs)", abs_ok)
# recursive C_R vs product formula
topo = sorted(names, key=height)
Cr = {}
for R in topo:
    Xr = F - sum((Cr[Rp] for Rp in names if (Rp, R) in lt), sp.Integer(0))
    Cr[R] = Top(R)(Xr)
def prodform(R):
    f = F
    for Rp in topo:
        if (Rp, R) in lt:
            f = f - Top(Rp)(f)
    return Top(R)(f)
pf_ok = all(sp.expand(Cr[R] - prodform(R)) == 0 for R in names)
check("Cor D.13 product formula on Fig.63 poset (toy coordinate-zeroing model)", pf_ok)
rem = F - sum(Cr.values())
f = F
for R in topo: f = f - Top(R)(f)
check("Cor D.13: r = prod(1-T_R)F on Fig.63 poset", sp.expand(rem - f) == 0)
# chain expansion O_P vs product (Moebius argument) on the same model
def chains(P):
    P = list(P); out = [[]]
    for size in range(1, len(P)+1):
        for sub in itertools.combinations(P, size):
            if all(rle(a, b) or rle(b, a) for a in sub for b in sub):
                out.append(sorted(sub, key=height, reverse=True))
    return out
OP = sum(((-1)**len(c))*Tseq(c, F) for c in chains(names))
check("Lemma D.11: r = O_R Gamma (sum over chains)", sp.expand(OP - rem) == 0)
# pairing decomposition (Lemma D.12) for R0 = 'C1C1'
R0 = 'C1C1'
def Oset(P, f):
    return sum(((-1)**len(c))*Tseq(c, f) for c in chains(P))
up = lambda R: [x for x in names if (R, x) in lt]
down = lambda R: [x for x in names if (x, R) in lt]
def Xof(R):
    return Oset(down(R), F)
term1 = Oset(up(R0), Xof(R0) - Top(R0)(Xof(R0)))
inc = [R for R in names if not rle(R, R0) and not rle(R0, R)]
term2 = 0
for R in inc:
    Rw = rmeet(R, R0)
    inner = Top(R)(Xof(Rw) - Top(Rw)(Xof(Rw)))
    term2 += Oset(up(R), inner)
check("Lemma D.12 pairing decomposition (R0=C1C1, all incomparable have meets)",
      sp.expand(rem - (term1 - term2)) == 0)

# ---------------- projectors (D.15), (D.16) ----------------
I2 = np.eye(2); sx = np.array([[0, 1], [1, 0]]); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1])
Z = np.zeros((2, 2))
g0 = np.block([[I2, Z], [Z, -I2]]).astype(complex)
gs = [np.block([[Z, s_], [-s_, Z]]).astype(complex) for s_ in (sx, sy, sz)]
g5 = 1j*g0@gs[0]@gs[1]@gs[2]
gp = (g0 + gs[2])/np.sqrt(2); gm = (g0 - gs[2])/np.sqrt(2)
Pp_ = 0.5*gm@gp; Pm_ = 0.5*gp@gm
check("P+^2=P+, P-^2=P-, P++P-=1", np.allclose(Pp_@Pp_, Pp_) and np.allclose(Pm_@Pm_, Pm_) and np.allclose(Pp_+Pm_, np.eye(4)))
check("bar(P+ psi) = psibar P- : g0 P+^dag g0 = P-", np.allclose(g0@Pp_.conj().T@g0, Pm_))
check("(1/4)Tr[g5 g+ g- g5] = 1", np.isclose(np.trace(g5@gp@gm@g5)/4, 1))
# D.16 projector idempotent on random J
rng = np.random.default_rng(0)
J = rng.normal(size=(4, 4)) + 1j*rng.normal(size=(4, 4))
proj = lambda M: 0.25*(gm@g5)*np.trace(g5@gp@M)
check("(D.16) Dirac projector idempotent", np.allclose(proj(proj(J)), proj(J)))
# P_A = delta - nbar n (mixed indices) in light-cone basis: metric g with (+,-,T)
# use components V^mu with index order (+,-,1,2); g_{+-}=g_{-+}=1, g_{11}=g_{22}=-1
g = np.array([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]], float)
n_up = np.array([1, 0, 0, 0.]); nb_up = np.array([0, 1, 0, 0.])
n_dn = g@n_up; nb_dn = g@nb_up
PA = np.eye(4) - np.outer(nb_up, n_dn)
gT = np.eye(4) - np.outer(n_up, nb_dn) - np.outer(nb_up, n_dn)
check("P_A = g_T + n nbar ; P_A^2 = P_A", np.allclose(PA, gT + np.outer(n_up, nb_dn)) and np.allclose(PA@PA, PA))
H_dn = rng.normal(size=4); J_up = rng.normal(size=4)
lhs = H_dn@PA@J_up
Hup = np.linalg.inv(g)@H_dn
rhs = Hup[1]*J_up[0] - (Hup[2]*J_up[2] + Hup[3]*J_up[3])  # H^- J^+ - H_T.J_T (Euclid)
check("H.P_A.J = H^- J^+ - H_T.J_T", np.isclose(lhs, rhs))
# TMD: n_A(yA)=(1,-e^{-2yA},0), n_B(yB)=(-e^{2yB},1,0)
yA, yB = 1.7, -2.3
nA = np.array([1, -np.exp(-2*yA), 0, 0]); nB = np.array([-np.exp(2*yB), 1, 0, 0])
dotv = lambda a, b: a@g@b
check("n_A.nbar=1, n_A^2=-2e^{-2yA}", np.isclose(dotv(nA, nb_up), 1) and np.isclose(dotv(nA, nA), -2*np.exp(-2*yA)))
check("n_B.n=1", np.isclose(dotv(nB, n_up), 1))
M = gT + np.outer(n_up, g@nB)
check("g_T + n (x) n_B idempotent", np.allclose(M@M, M))
kvec = np.array([0.7, 0.3, 0.2, -0.1])
pi_m_A = dotv(nA, kvec)*nb_up; pi_p_B = dotv(nB, kvec)*n_up
check("pi_-^{(yA)} idempotent", np.allclose(dotv(nA, pi_m_A)*nb_up, pi_m_A))
check("pi_+^{(yB)} pi_-^{(yA)}(k) = -e^{2yB}(n_A.k) n", np.allclose(dotv(nB, pi_m_A)*n_up, -np.exp(2*yB)*dotv(nA, kvec)*n_up))
# product of (g_T + n x n_B) with soft projection (n x n_B) = soft projection
soft = np.outer(n_up, g@nB)
check("(g_T+n x n_B) * soft proj = soft proj", np.allclose(M@soft, soft))

# ---------------- Lemma D.38 ----------------
yA_, yB_, yn, aS, aA, K = sp.symbols('y_A y_B y_n a_S alpha_A K')
S = lambda y1, y2: sp.exp(aS + (y1 - y2)*K)
fAun = sp.exp(aA - yB_*K)
fA = fAun*sp.sqrt(S(yA_, yn)/(S(yA_, yB_)*S(yn, yB_)))
check("Lemma D.38 limit: ln fA = alpha_A - a_S/2 - y_n K",
      sp.simplify(sp.expand_log(sp.log(fA), force=True) - (aA - aS/2 - yn*K)) == 0)
S1, S2, S3 = sp.symbols('S_AB S_An S_nB', positive=True)
fa = sp.sqrt(S2/(S1*S3)); fb = sp.sqrt(S3/(S1*S2))
check("Lemma D.38 identity: fA fB = 1/S(yA,yB) (times unsub)", sp.simplify(fa*fb - 1/S1) == 0)

# ---------------- A, B expansions and (D.32) ----------------
eps = sp.symbols('epsilon')
A = sp.gamma(1+eps)*sp.gamma(1-eps)**2/(eps**2*sp.gamma(1-2*eps))
B = sp.gamma(1+eps)**2*sp.gamma(1-eps)/eps**2
z2 = sp.pi**2/6
serA = sp.series(A*sp.exp(sp.EulerGamma*eps), eps, 0, 1).removeO()
serB = sp.series(B*sp.exp(sp.EulerGamma*eps), eps, 0, 1).removeO()
check("A = e^{-gE eps}(1/eps^2 - zeta2/2 + O(eps))", sp.simplify(serA - (1/eps**2 - z2/2)) == 0)
check("B = e^{-gE eps}(1/eps^2 + 3 zeta2/2 + O(eps))", sp.simplify(serB - (1/eps**2 + 3*z2/2)) == 0)
check("A = -Gamma(eps) J(eps), J = Gamma(-eps)Gamma(1-eps)/Gamma(1-2eps)",
      sp.simplify(sp.gammasimp(A + sp.gamma(eps)*sp.gamma(-eps)*sp.gamma(1-eps)/sp.gamma(1-2*eps))) == 0)
lQ, lm = sp.symbols('ell_Q ell_m')
tot = sp.exp(lQ*eps)*A - 2*sp.exp(lm*eps)*A + sp.exp((2*lm - lQ)*eps)*B
ser = sp.series(tot, eps, 0, 1).removeO()
check("(D.32): poles cancel; finite = (lQ-lm)^2 + 2 zeta2",
      sp.simplify(sp.expand(ser) - ((lQ - lm)**2 + 2*z2)) == 0)

print("\nALL PASS" if ok else "\nSOME FAILED")
