# W17 / Ch14 -- s10: algebra of the TMD subtraction structure (sec:tmd-subtraction, lem:tmd-sqrt-identity, rem:tmd-*).
# (a) regulator vectors and projections, idempotency, non-commutation; (b) absorption identities (prop:tmd-zero-bin-soft (a));
# (c) square-root identity and the (T2) limit (CS equation); (d) order-of-limits factor e^{2(y_B - y_k)}; (e) rapidity window
# arithmetic; (f) rapidity of the gluon in the unsubtracted TMD and the cut-off at y ~ y_B; (g) induction (prop:tmd-zero-bin-soft (b))
# as an identity of formal power series; (h) gamma^+ structure: n_B(y_B) . k for the hard-collinear projection.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np
ok = True
def check(name, cond):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name); ok &= bool(cond)
yA, yB, yn, y, kp, km, kT = sp.symbols('y_A y_B y_n y k_p k_m k_T', real=True)
def dot(a, b): return a[0]*b[1] + a[1]*b[0]          # (plus, minus) parts
nA = (1, 0); nB = (0, 1)
nAy = (1, -sp.exp(-2*yA)); nBy = (-sp.exp(2*yB), 1)
check('n_A.n_B = 1, n_A(y_A).n_B = 1, n_B(y_B).n_A = 1 (normalization of the projections)', dot(nA, nB) == 1 and dot(nAy, nB) == 1 and dot(nBy, nA) == 1)
k = (kp, km)
pip = lambda v: tuple(dot(nBy, v)*c for c in nA)      # pi_+^{(y_B)}(v) = (n_B(y_B).v) n_A
pim = lambda v: tuple(dot(nAy, v)*c for c in nB)      # pi_-^{(y_A)}(v) = (n_A(y_A).v) n_B
check('pi_+^{(y_B)} idempotent', all(sp.simplify(a - b) == 0 for a, b in zip(pip(pip(k)), pip(k))))
check('pi_-^{(y_A)} idempotent', all(sp.simplify(a - b) == 0 for a, b in zip(pim(pim(k)), pim(k))))
pp_mm = pip(pim(k))
check('pi_+ pi_-(k) = -e^{2y_B}(n_A(y_A).k) n_A  (non-zero: (Com)(Abs) only up to e^{-2|y|})', sp.simplify(pp_mm[0] + sp.exp(2*yB)*dot(nAy, k)) == 0 and pp_mm[1] == 0)
check('n_B(y_B).k = k^+ - e^{2y_B} k^-', sp.simplify(dot(nBy, k) - (kp - sp.exp(2*yB)*km)) == 0)
check('n_A(y_A).k = k^- - e^{-2y_A} k^+', sp.simplify(dot(nAy, k) - (km - sp.exp(-2*yA)*kp)) == 0)
# (d) relative difference of the hard-collinear projection at fixed x: e^{2 y_B} k^-/k^+ = e^{2(y_B - y_k)}
yk = sp.Rational(1, 2)*sp.log(kp/km)
kpos = {kp: sp.Symbol('kp', positive=True), km: sp.Symbol('km', positive=True)}
check('e^{2y_B} k^-/k^+ = e^{2(y_B - y_k)}', sp.simplify((sp.exp(2*yB)*km/kp - sp.exp(2*(yB - yk))).subs(kpos)) == 0)
# (b) absorption: p_B on shell (mass M, possibly p_B^+ != 0, p_BT != 0)
pBp, pBm, pBT, M = sp.symbols('p_Bp p_Bm p_BT M', positive=True)
# on shell: 2 p+ p- - pT^2 = M^2 ; transverse parts: pi_+(k) has no transverse part
pB = (pBp, pBm)
lhs1 = 2*dot(pB, pip(k)) + dot(pip(k), pip(k))        # (p_B + pi_+(k))^2 - p_B^2  (pi_+(k)^2 = 0, no transverse mixing)
check('(p_B + pi_+(k))^2 - M^2 = 2 p_B^- (n_B(y_B).k)', sp.simplify(lhs1 - 2*pBm*dot(nBy, k)) == 0)
lhs2 = dot(tuple(a + b for a, b in zip(pim(pB), pip(k))), tuple(a + b for a, b in zip(pim(pB), pip(k))))
check('(pi_-(p_B) + pi_+(k))^2 = 2 (n_A(y_A).p_B)(n_B(y_B).k)', sp.simplify(lhs2 - 2*dot(nAy, pB)*dot(nBy, k)) == 0)
check('relative difference: n_A(y_A).p_B/p_B^- - 1 = -e^{-2y_A} p_B^+/p_B^-', sp.simplify(dot(nAy, pB)/pBm - 1 + sp.exp(-2*yA)*pBp/pBm) == 0)
# (c) square-root identity
SA_n, SA_B, Sn_B, fA, fB = sp.symbols('S_An S_AB S_nB fA fB', positive=True)
fAt = fA*sp.sqrt(SA_n/(SA_B*Sn_B)); fBt = fB*sp.sqrt(Sn_B/(SA_B*SA_n))
check('sqrt identity: f_A f_B = f_A^unsub f_B^unsub / S(y_A,y_B), independent of y_n', sp.simplify(fAt*fBt - fA*fB/SA_B) == 0)
# (T2) limit
aS, alA, K, yPA = sp.symbols('a_S alpha_A K y_PA', real=True)
c1, c2, c3, c4 = sp.symbols('c1:5')
lnS = lambda y1, y2, c: aS + (y1 - y2)*K + c*sp.exp(-(y1 - y2))
lnfA = alA - yB*K + c4*sp.exp(yB - yPA)
lnfAt = lnfA + sp.Rational(1, 2)*(lnS(yA, yn, c1) - lnS(yA, yB, c2) - lnS(yn, yB, c3))
lim = sp.limit(sp.limit(lnfAt, yA, sp.oo), yB, -sp.oo)
check('(T2): lim ln f_A = alpha_A - a_S/2 - y_n K', sp.simplify(lim - (alA - aS/2 - yn*K)) == 0)
check('d ln f_A/d y_n = -K, and d/d ln sqrt(zeta_A) = -d/dy_n  =>  CS equation', sp.simplify(sp.diff(lim, yn) + K) == 0)
xA, PAp = sp.symbols('x_A P_Ap', positive=True)
zetaA = 2*(xA*PAp)**2*sp.exp(-2*yn)
check('ln sqrt(zeta_A) = const - y_n', sp.simplify(sp.diff(sp.log(sp.sqrt(zetaA)), yn) + 1) == 0)
# equal slopes are necessary: if f_unsub had slope K' != K the limit would not exist
Kp = sp.Symbol('Kp', real=True)
lnfA2 = alA - yB*Kp
expr = lnfA2 + sp.Rational(1, 2)*(lnS(yA, yn, 0) - lnS(yA, yB, 0) - lnS(yn, yB, 0))
check('with unequal slopes the y_B dependence (K - K\') y_B survives', sp.simplify(sp.diff(expr, yB) - (K - Kp)) == 0)
# (e) rapidity window: soft k with |kT| >= lambda^{1+a}, ||k|| <= 1 (units Q), |k^+ k^-| >= c kT^2 => |y_k| <= (1+a) L + O(1)
for lam_, a_ in [(1e-3, 0.2), (1e-6, 0.1)]:
    L_ = np.log(1/lam_)
    kTmin = lam_**(1 + a_); c_ = 0.5
    # worst case: k^+ = 1, k^- = c kT^2 -> y = 1/2 ln(k+/k-) = 1/2 ln(1/(c kT^2)) = (1+a) L + 1/2 ln(1/c)
    ymax = 0.5*np.log(1/(c_*kTmin**2))
    check('max soft rapidity (1+a)L + O(1): %.4f vs %.4f' % (ymax, (1 + a_)*L_ + 0.5*np.log(1/c_)), abs(ymax - ((1 + a_)*L_ + 0.5*np.log(1/c_))) < 1e-9)
    Y = (1 + 2*a_)*L_ + 0.5*np.log(1/c_)
    err = np.exp(-2*(Y - ymax))
    check('Y >= (1+2a)L + O(1)  =>  e^{-2(Y-|y_k|)} <= lambda^{2a}  (%.3e <= %.3e)' % (err, lam_**(2*a_)), err <= lam_**(2*a_)*(1 + 1e-9))
# (f) gluon rapidity in the unsubtracted TMD: l^+ = (1-x)p^+, l^- = kT^2/(2(1-x)p^+): y_l = ln(sqrt2 (1-x) p^+/kT)
x, pp = sp.symbols('x p_p', positive=True)
lp = (1 - x)*pp; lm = kT**2/(2*(1 - x)*pp)
yl = sp.Rational(1, 2)*sp.log(lp/lm)
check('y_l = ln(sqrt2 (1-x) p^+/k_T)', sp.simplify(sp.expand_log((yl - sp.log(sp.sqrt(2)*(1 - x)*pp/kT)).subs(kT, sp.Symbol('kTp', positive=True)), force=True)) == 0)
# (1-x)^2 = delta^2 = e^{2 y_B} kT^2/(2 p+^2)  <=>  y_l = y_B
d2 = sp.exp(2*yB)*kT**2/(2*pp**2)
sol = sp.solve(sp.Eq((1 - x)**2, d2), x)
yl_at = [sp.simplify(sp.expand_log(yl.subs(x, s_).subs(kT, sp.Symbol('kTp', positive=True)), force=True)) for s_ in sol]
check('the regulator denominator (1-x)^2 + s delta^2 switches at y_l = y_B: %s' % yl_at, any(sp.simplify(v - yB) == 0 for v in yl_at))
# (g) induction of prop:tmd-zero-bin-soft (b): if f_A^unsub = X_A S (formal power series), the subtracted A contributions satisfy
#   X^(N) = f^(N) - sum_{K=1}^N X^(N-K) S^(K); check it reproduces the coefficients of f/S up to order 6 for random series
rng = np.random.default_rng(11)
for trial in range(3):
    f = [1.0] + list(rng.normal(size=6)); S = [1.0] + list(rng.normal(size=6))
    X = [1.0]
    for N in range(1, 7):
        X.append(f[N] - sum(X[N - K]*S[K] for K in range(1, N + 1)))
    # direct division of power series
    g = sp.Symbol('g')
    fs = sum(f[i]*g**i for i in range(7)); Ss = sum(S[i]*g**i for i in range(7))
    q = sp.series(fs/Ss, g, 0, 7).removeO()
    check('induction X^(N) = f^(N) - sum X^(N-K) S^(K) gives f/S (trial %d)' % trial, all(abs(float(q.coeff(g, i)) - X[i]) < 1e-9 for i in range(7)))
    # and X_A X_B S = f_A f_B / S
    fB_ = [1.0] + list(rng.normal(size=6))
    XB = [1.0]
    for N in range(1, 7):
        XB.append(fB_[N] - sum(XB[N - K]*S[K] for K in range(1, N + 1)))
    fBs = sum(fB_[i]*g**i for i in range(7))
    lhs = sp.series(sum(X[i]*g**i for i in range(7))*sum(XB[i]*g**i for i in range(7))*Ss, g, 0, 7).removeO()
    rhs = sp.series(fs*fBs/Ss, g, 0, 7).removeO()
    check('X_A X_B S = f_A^unsub f_B^unsub / S as formal power series (trial %d)' % trial, all(abs(float(lhs.coeff(g, i) - rhs.coeff(g, i))) < 1e-8 for i in range(7)))
print('ALL PASS' if ok else 'SOME FAIL')
