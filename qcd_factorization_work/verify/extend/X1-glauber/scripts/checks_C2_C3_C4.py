# C2 (fast, exact linear-form residue algebra), C3 (colour), C4 (ray identity) -- see checks_misc.py header.
import sys, os, itertools, random
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import mpmath as mp
mp.mp.dps = 40
ok = True
def check(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name, flush=True); ok = ok and bool(cond)

# ---- linear-form residue integrator: term = (C, [ (coef vector c (len N), const d) ... ]) means C/prod(c.k + d)
def integrate_var(terms, e):
    out = []
    for (C, forms) in terms:
        dep = [f for f in forms if f[0][e] != 0]
        indep = [f for f in forms if f[0][e] == 0]
        # decay check: need >= 2 factors depending on k_e
        assert len(dep) >= 2
        for j, (cj, dj) in enumerate(dep):
            # pole: k_e = -(dj + sum_{i!=e} cj_i k_i)/cj_e ; with other k real, Im(pole) = -Im(dj)/cj_e
            impole = -mp.im(dj)/cj[e]
            if impole <= 0: continue
            newforms = list(indep)
            for i2, (ci, di) in enumerate(dep):
                if i2 == j: continue
                # substitute k_e -> -(dj + cj.k_rest)/cj_e into ci.k + di
                ratio = ci[e]/cj[e]
                cnew = [ci[m] - ratio*cj[m] for m in range(len(ci))]; cnew[e] = 0
                dnew = di - ratio*dj
                newforms.append((cnew, dnew))
            out.append((C*mp.mpc(0, 1)/cj[e], newforms))     # (2 pi i Res)/(2 pi) = i * C/cj_e * prod others^-1
    return out
def evaluate(terms):
    tot = mp.mpc(0)
    for (C, forms) in terms:
        v = C
        for (c, d) in forms:
            assert all(x == 0 for x in c)
            v /= d
        tot += v
    return tot

N = 3
eta = mp.mpf('1e-12')
Dc = {}; Ac = {}
for r in range(N + 1):
    for s in itertools.combinations(range(N), r):
        fs = frozenset(s)
        Dc[fs] = -mp.mpf(3 + len(fs))/7 - mp.mpf(sum(fs))/11
        Ac[fs] = -mp.mpf(2 + len(fs))/5 + mp.mpf(sum(fs))/13
def sector_forms(order, ninit):
    forms = []; C = mp.mpc(1)
    injected = frozenset()
    for m in range(ninit):
        injected = injected | {order[m]}
        c = [1 if e in injected else 0 for e in range(N)]
        forms.append((c, Dc[injected] + mp.mpc(0, 1)*eta)); C *= mp.mpc(0, 1)
    remaining = frozenset(order[ninit:])
    for m in range(ninit, N):
        c = [-1 if e in remaining else 0 for e in range(N)]
        forms.append((c, Ac[remaining] + mp.mpc(0, 1)*eta)); C *= mp.mpc(0, 1)
        remaining = remaining - {order[m]}
    return C, forms
zv = [mp.mpf(5)/3 - mp.mpc(0, 1)*eta*3, -mp.mpf(7)/4 + mp.mpc(0, 1)*eta*3, mp.mpf(9)/5 - mp.mpc(0, 1)*eta*3]
rv = [mp.mpf(1)/3, -mp.mpf(2)/7, mp.mpf(1)/5]
good = True
for order in itertools.permutations(range(N)):
    terms = []
    for ninit in range(N + 1):
        C, forms = sector_forms(order, ninit)
        forms = forms + [([1 if m == e else 0 for m in range(N)], -zv[e]) for e in range(N)]
        terms.append((C*rv[0]*rv[1]*rv[2], forms))
    for e in range(N): terms = integrate_var(terms, e)
    brute = evaluate(terms)
    init = [e for e in range(N) if mp.im(zv[e]) > 0]
    ninit = len(init)
    if sorted(order.index(e) for e in init) != list(range(ninit)):
        formula = mp.mpc(0)
    else:
        C, forms = sector_forms(order, ninit)
        v = C
        for (c, d) in forms: v /= (sum(c[m]*zv[m] for m in range(N)) + d)
        for e in range(N): v *= (mp.mpc(0, 1) if mp.im(zv[e]) > 0 else -mp.mpc(0, 1))*rv[e]
        formula = v
    good = good and abs(brute - formula) < mp.mpf('1e-25')*max(1, abs(formula))
    print(f"     order {order}: brute = {mp.nstr(brute, 15)}   formula = {mp.nstr(formula, 15)}")
check("C2   N=3 exact contour formula (Lemma L1) = exact iterated residues, all 6 colour orders", good)

# ---- C3 colour algebra
def su3():
    l = np.zeros((8, 3, 3), dtype=complex)
    l[0][0,1] = l[0][1,0] = 1; l[1][0,1] = -1j; l[1][1,0] = 1j; l[2][0,0] = 1; l[2][1,1] = -1
    l[3][0,2] = l[3][2,0] = 1; l[4][0,2] = -1j; l[4][2,0] = 1j; l[5][1,2] = l[5][2,1] = 1
    l[6][1,2] = -1j; l[6][2,1] = 1j; l[7][0,0] = l[7][1,1] = 1/np.sqrt(3); l[7][2,2] = -2/np.sqrt(3)
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
    chi = 0.37
    for popp in (0.5, 0.2 - 0.7j, -0.4j):
        M1 = -1j*chi*X; M2 = 0.5*(-1j*chi)**2*(X @ X + popp*1.5*X)
        res = M2 + M2.conj().T + M1.conj().T @ M1
        check(f"C3d  [{name}] residual = -1/2 C_A chi^2 Re(p_opp) X (p_opp={popp})", np.allclose(res, -0.75*chi**2*np.real(popp)*2*X/1.0*0.5*2/1.0*0.5*2) if False else np.allclose(res, -1.5*chi**2*np.real(popp)*X))
I3 = np.eye(3)
def kron3(a, b, c): return np.kron(np.kron(a, b), c)
# Fix round 1: C3e/C3f originally tested the author's FIRST prediction 'residual = 2 c1 c2 (Re W12 - 1/2)[X2,X1]'
# (halfcoinc.py header, 'Thm T5': Re W12 -> 1/2 hence cancellation), which is wrong; the original version and
# its failing log are kept as checks_C2_C3_C4_r0.py / logs/checks_C2_C3_C4_r0.log.  The correct statement
# (REPORT L4(b)) is R = 2 i c1 c2 Im(W12) [X1,X2] with W21 = 1 - W12; it vanishes iff Im W12 = 0.
X1 = sum(kron3(T[a], T[a], I3) for a in range(8)); X2 = sum(kron3(T[a], I3, Tb[a]) for a in range(8))
c1, c2 = 0.31, 0.53
comm12 = X1 @ X2 - X2 @ X1
for W12 in (0.5 - 0.03j, 0.7, 0.5 + 0.2j, 0.2 - 0.1j):
    W21 = 1 - W12
    M2 = (-1j)**2*c1*c2*(W12*(X2 @ X1) + W21*(X1 @ X2))
    M2c = (1j)**2*c1*c2*(np.conj(W12)*(X1 @ X2) + np.conj(W21)*(X2 @ X1))   # conj side: reversed operator order
    M1sq = c1*c2*(X1 @ X2 + X2 @ X1)
    res = M2 + M2c + M1sq
    pred = 2j*c1*c2*np.imag(W12)*comm12
    check(f"C3e  half-coincident residual = 2 i c1 c2 Im(W12) [X1,X2]  (W12={W12})", np.allclose(res, pred))
    check(f"C3f  ... and it vanishes iff Im W12 = 0  (W12={W12})", np.allclose(res, 0) == (abs(np.imag(W12)) < 1e-12))

# ---- C4 ray identity
random.seed(3); allgood = True
for trial in range(8):
    cs = [random.choice([-1, 1])*random.uniform(0.2, 3.0) for _ in range(random.randint(1, 3))]
    rho = lambda kk: mp.fprod([1/(1 + c*kk) for c in cs])
    lhs = mp.quad(lambda kk: mp.im(rho(1j*kk))/kk, [0, 0.1, 1, 10, mp.inf])
    imreal = 0
    for j, c in enumerate(cs):
        if c < 0:
            kp = -1/c
            resid = (1/c)*mp.fprod([1/(1 + cc*kp) for i2, cc in enumerate(cs) if i2 != j])
            imreal += -mp.pi*resid/kp
    rhs = -mp.pi/2 + imreal
    allgood = allgood and abs(lhs - rhs) < 1e-15
    print(f"     trial {trial}: c={['%.3f'%c for c in cs]}  lhs={mp.nstr(lhs,16)}  rhs={mp.nstr(rhs,16)}")
check("C4   ray identity  int dk/k Im rho(ik) = -pi/2 + Im int dk/k rho(k+i0)", allgood)
print("ALL PASS" if ok else "SOME CHECK FAILED")
