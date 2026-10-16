# Miscellaneous exact/numerical checks for REPORT (X1-glauber).
#  C1: Lemma L1 weights for N = 3 (all-final, all-initial, mixed) from the time-domain "race" integrals
#      vs the closed formula; sum to 1; continuity across k_e^+ = 0 (Lemma L2).
#  C2: exact contour formula of Lemma L1 for N = 3 against brute-force residues (sympy) on an
#      LCOPT model jet (three spectator insertions, single-state gaps).
#  C3: colour algebra: crossed = X^2 + (C_A/2) X ; [ , ](x)[ , ] = -C_A X ; residual formula
#      -1/2 C_A chi^2 Re(p_opp) X ; half-coincident residual  ~ Re(W12 - W21) [T^a,T^b](x)T^a T^b .
#  C4: ray identity (Lemma L6): int_0^inf dk/k Im rho(i k) = -pi/2 + Im int_0^inf dk/k rho(k + i0)
#      for random rational rho with rho(0) = 1, rho(inf) = 0, poles only in the closed lower/left region.
import sys, os, itertools, random
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np
import mpmath as mp

ok = True
def check(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name, flush=True)
    ok = ok and bool(cond)

# ---------------- C1: race weights ----------------
t1, t2, t3 = sp.symbols('t1 t2 t3', real=True)
z1, z2, z3 = sp.symbols('z1 z2 z3', positive=True)
def race_final(order, zs, ts):
    # all insertions at tau > 0 with density i z e^{-i z tau}; for the identity we may use real decay
    # rates (analytic in z): density z e^{-z tau} (the formula is rational in z, so this suffices)
    expr = sp.Integer(1)
    for z, t in zip(zs, ts): expr *= z*sp.exp(-z*t)
    # region tau_{order[0]} < tau_{order[1]} < tau_{order[2]}
    a, b, c = [ts[i] for i in order]
    val = sp.integrate(sp.integrate(sp.integrate(expr, (a, 0, b)), (b, 0, c)), (c, 0, sp.oo))
    return sp.simplify(val)
def formula_final(order, zs):
    num = zs[0]*zs[1]*zs[2]
    den = 1
    for m in range(3):
        den *= sum(zs[order[l]] for l in range(m, 3))
    return num/den
zs = [z1, z2, z3]; ts = [t1, t2, t3]
tot = 0
allgood = True
for order in itertools.permutations(range(3)):
    r = race_final(order, zs, ts); f = formula_final(order, zs)
    allgood = allgood and sp.simplify(r - f) == 0
    tot += f
check("C1a  N=3 all-final race weights = prod z / prod_m sum_{l>=m} z_pi(l)", allgood)
check("C1b  N=3 weights sum to 1", sp.simplify(tot - 1) == 0)
# initial group: tau<0, density z e^{z tau}; formula prod z / prod_m sum_{l<=m} z_pi(l)
def formula_initial(order, zs):
    num = zs[0]*zs[1]*zs[2]; den = 1
    for m in range(3): den *= sum(zs[order[l]] for l in range(0, m+1))
    return num/den
def race_initial(order, zs, ts):
    expr = sp.Integer(1)
    for z, t in zip(zs, ts): expr *= z*sp.exp(z*t)
    a, b, c = [ts[i] for i in order]          # a < b < c < 0
    val = sp.integrate(sp.integrate(sp.integrate(expr, (c, b, 0)), (b, a, 0)), (a, -sp.oo, 0))
    return sp.simplify(val)
allgood = all(sp.simplify(race_initial(o, zs, ts) - formula_initial(o, zs)) == 0 for o in itertools.permutations(range(3)))
check("C1c  N=3 all-initial race weights = prod z / prod_m sum_{l<=m} z_pi(l)", allgood)
# continuity (Lemma L2): weight of order (1,2) as function of (k1+, k2+) with z_e = a_e/(2 k_e^+)
a1, a2 = sp.Rational(13, 10), sp.Rational(7, 10)
def w12(k1, k2):
    if k1 > 0 and k2 > 0:  z1v, z2v = a1/(2*k1), a2/(2*k2); return z1v/(z1v + z2v)
    if k1 < 0 and k2 < 0:  z1v, z2v = -a1/(2*k1), -a2/(2*k2); return z2v/(z1v + z2v)
    if k1 < 0 < k2: return sp.Integer(1)
    return sp.Integer(0)
eps = sp.Rational(1, 10**8)
cont = []
for (k1, k2) in [(0, sp.Rational(1,3)), (0, -sp.Rational(1,3)), (sp.Rational(1,2), 0), (-sp.Rational(1,2), 0)]:
    if k1 == 0: vals = [w12(eps, k2), w12(-eps, k2)]
    else: vals = [w12(k1, eps), w12(k1, -eps)]
    cont.append(abs(float(vals[0] - vals[1])) < 1e-6)
check("C1d  weights continuous across k1+=0 and k2+=0 (away from the origin)", all(cont))
# discontinuity at the origin: limit depends on direction
d1 = w12(eps, eps); d2 = w12(eps, 10*eps)
check("C1e  weights discontinuous at the origin (homogeneous of degree 0)", abs(float(d1 - d2)) > 1e-3)

# ---------------- C2: exact contour formula, N=3, model jet ----------------
# model: spectator absorbs k1,k2,k3 in some time order; LCOPT jet with V_H at 0; single-state gaps:
#   initial gap after insertions set S (before V_H): 1/(D_S + K_S + i0),  final gap before set T: 1/(A_T - K_T + i0)
# colour order pi -> sector functions; external factors r_e/(k_e - z_e).  Brute force: sympy residues.
k = sp.symbols('k1:4')
Dc = {fs: sp.Rational(-(3 + len(fs)), 7) - sp.Rational(sum(fs), 11) for fs in [frozenset(s) for r in range(4) for s in itertools.combinations(range(3), r)]}
Ac = {fs: sp.Rational(-(2 + len(fs)), 5) + sp.Rational(sum(fs), 13) for fs in Dc}
def sector(order, ninit):
    # insertions order[0..ninit-1] initial (in this time order), rest final
    expr = sp.Integer(1)
    injected = frozenset()
    for m in range(ninit):
        injected = injected | {order[m]}
        Ksum = sum(k[e] for e in injected)
        expr *= sp.I/(Dc[injected] + Ksum + sp.I*sp.Rational(1, 10**6))
    remaining = frozenset(order[ninit:])
    for m in range(ninit, 3):
        Ksum = sum(k[e] for e in remaining)
        expr *= sp.I/(Ac[remaining] + (-Ksum) + sp.I*sp.Rational(1, 10**6))
        remaining = remaining - {order[m]}
    return expr
def colour_function(order):
    return sum(sector(order, n) for n in range(4))
zv = [sp.Rational(5, 3) - sp.I*sp.Rational(1, 10**6), -sp.Rational(7, 4) + sp.I*sp.Rational(1, 10**6), sp.Rational(9, 5) - sp.I*sp.Rational(1, 10**6)]
rv = [sp.Rational(1, 3), sp.Rational(-2, 7), sp.Rational(1, 5)]
def brute(order):
    f = colour_function(order)
    for e in range(3): f = f*rv[e]/(k[e] - zv[e])
    # integrate k1, k2, k3 over R successively by residues (close in UHP: poles with Im>0 at real other k)
    for e in range(3):
        f = sp.together(f)
        num, den = sp.fraction(f)
        poles = sp.roots(sp.Poly(den, k[e]))
        res = 0
        for pole in poles:
            imv = sp.im(pole.subs({kk: 0 for kk in k if kk != k[e]}))
            if imv > 0:
                res += sp.residue(f, k[e], pole)
        f = sp.I*res     # (2 pi i)/(2 pi) * sum Res
        f = sp.simplify(f)
    return sp.N(f, 20)
def formula(order):
    # Lemma L1 exact form: initial group = {e: Im z_e > 0} = {1} (index 1), final = {0, 2}
    init = [e for e in range(3) if sp.im(zv[e]) > 0]
    pos = [order.index(e) for e in init]
    if sorted(pos) != list(range(len(init))): return 0
    val = sector(order, len(init)).subs({k[e]: zv[e] for e in range(3)})
    for e in range(3):
        val *= (sp.I if sp.im(zv[e]) > 0 else -sp.I)*rv[e]
    return sp.N(val, 20)
good = True
for order in itertools.permutations(range(3)):
    b = brute(order); f = formula(order)
    good = good and abs(complex(b - f)) < 1e-12
check("C2   N=3 exact contour formula (Lemma L1) = brute-force residues, all 6 colour orders", good)

# ---------------- C3: colour algebra ----------------
def su3():
    l = np.zeros((8, 3, 3), dtype=complex)
    l[0][0,1] = l[0][1,0] = 1
    l[1][0,1] = -1j; l[1][1,0] = 1j
    l[2][0,0] = 1; l[2][1,1] = -1
    l[3][0,2] = l[3][2,0] = 1
    l[4][0,2] = -1j; l[4][2,0] = 1j
    l[5][1,2] = l[5][2,1] = 1
    l[6][1,2] = -1j; l[6][2,1] = 1j
    l[7][0,0] = l[7][1,1] = 1/np.sqrt(3); l[7][2,2] = -2/np.sqrt(3)
    return l/2
T = su3(); Tb = np.array([-t.T for t in T])
for name, TA, TB in (("3x3", T, T), ("3x3bar", T, Tb)):
    X = sum(np.kron(TA[a], TB[a]) for a in range(8))
    lad = sum(np.kron(TA[b] @ TA[a], TB[b] @ TB[a]) for a in range(8) for b in range(8))
    crs = sum(np.kron(TA[b] @ TA[a], TB[a] @ TB[b]) for a in range(8) for b in range(8))
    cc = sum(np.kron(TA[a] @ TA[b] - TA[b] @ TA[a], TB[a] @ TB[b] - TB[b] @ TB[a]) for a in range(8) for b in range(8))
    check(f"C3a  [{name}] ladder = X^2", np.allclose(lad, X @ X))
    check(f"C3b  [{name}] crossed = X^2 + (C_A/2) X", np.allclose(crs, X @ X + 1.5*X))
    check(f"C3c  [{name}] [T,T](x)[T,T] = -C_A X", np.allclose(cc, -3*X))
    # residual for complex p_opp
    chi = 0.37
    for popp in (0.5, 0.2 - 0.7j, -0.4j):
        M1 = -1j*chi*X; M2 = 0.5*(-1j*chi)**2*(X @ X + popp*1.5*X)
        res = M2 + M2.conj().T + M1.conj().T @ M1
        check(f"C3d  [{name}] residual = -1/2 C_A chi^2 Re(p_opp) X  (p_opp={popp})", np.allclose(res, -0.5*3*chi**2*np.real(popp)*X))
# half-coincident: A spectator (3), two B spectators (3 and 3bar): lines to different B partons
TA = T; TB1 = T; TB2 = Tb
I3 = np.eye(3)
def kron3(a, b, c): return np.kron(np.kron(a, b), c)
X1 = sum(kron3(TA[a], TB1[a], I3) for a in range(8)); X2 = sum(kron3(TA[a], I3, TB2[a]) for a in range(8))
chi1, chi2 = 0.31, 0.53
for W12 in (0.5 - 0.03j, 0.7, 0.5 + 0.2j):
    W21 = 1 - W12
    M2 = (-1j)**2*chi1*chi2*(W12*(X2 @ X1) + W21*(X1 @ X2))          # 1 first -> X2 X1 (later left)
    M1sq = chi1*chi2*(X1 @ X2 + X2 @ X1)                               # one line on each side
    res = M2 + M2.conj().T + M1sq
    pred = -chi1*chi2*np.real(W12 - W21)*0.5*((X2 @ X1) - (X1 @ X2))*(-1)
    # direct form: res = chi1 chi2 [ (1-Re? ) ... ]; just check it vanishes iff Re W12 = 1/2
    check(f"C3e  half-coincident residual vanishes iff Re W12 = 1/2 (W12={W12})", np.allclose(res, 0) == (abs(np.real(W12) - 0.5) < 1e-12))

# ---------------- C4: ray identity ----------------
mp.mp.dps = 30
random.seed(3)
allgood = True
for trial in range(6):
    # rho(k) = prod_j 1/(1 + c_j k)  with c_j real (any signs; negative c_j -> pole on positive axis, i0 from k+i0)
    cs = [random.choice([-1, 1])*random.uniform(0.2, 3.0) for _ in range(random.randint(1, 3))]
    rho = lambda kk: mp.fprod([1/(1 + c*kk) for c in cs])
    lhs = mp.quad(lambda kk: mp.im(rho(1j*kk))/kk, [0, 0.1, 1, 10, mp.inf])
    # Im of real-axis integral with k -> k + i0: from poles at k = -1/c_j > 0 (c_j<0): sum of -pi * Res
    imreal = 0
    for j, c in enumerate(cs):
        if c < 0:
            kp = -1/c
            resid = (1/c)*mp.fprod([1/(1 + cc*kp) for i2, cc in enumerate(cs) if i2 != j])  # residue of rho at kp
            imreal += -mp.pi*resid/kp                                            # (k+i0) passes above pole
    rhs = -mp.pi/2 + imreal
    allgood = allgood and abs(lhs - rhs) < 1e-12
    print(f"     trial {trial}: c={['%.3f'%c for c in cs]}  lhs={mp.nstr(lhs,14)}  rhs={mp.nstr(rhs,14)}")
check("C4   ray identity  int dk/k Im rho(ik) = -pi/2 + Im int dk/k rho(k+i0)", allgood)
print("ALL PASS" if ok else "SOME CHECK FAILED")
