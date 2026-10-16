#!/usr/bin/env python3
"""
Independent check of Theorem 5.7 (X3-ope_final2.md), written without looking at fix3_tail.py.

Method (different from the author's):
 (A) exact remainder identity of step 1 tested at COMPLEX omega anywhere in the cut plane
     (|omega|<1 and |omega|>1 off the cuts), for measures with a non-integrable small-x
     piece (so that low moments do not exist and the subtraction constants t_n, n<n0, are free);
 (B) imaginary-axis bound and its sharpness (ratio -> 1);
 (C) explicit failure of the old bound 2 t_{n0} r^{N-1} for odd N;
 (D) Markov constant of Lemma 5.3 from Chebyshev extremality AND an independent LP;
 (E) exhaustive exponent bookkeeping;
 (F) end-to-end chain (steps 2-4) on synthetic SA data with randomly perturbed P_N.
"""
import sys, os, itertools, random
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import numpy as np
from scipy.optimize import linprog

mp.mp.dps = 40
ok_all = True
def report(name, ok, extra=''):
    global ok_all
    ok_all &= bool(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {extra}")

# ---------------------------------------------------------------- measure
# F_2(x)dx = a_el*delta(1-x) + sum_k b_k delta(x-x_k) + c*x^alpha*(1-x)^beta dx
# alpha = -1.3: moments int x^{n-2} F_2 exist only for n-2+alpha > -1, i.e. n >= 3 -> n0 = 4 (even).
a_el = mp.mpf('0.7')
pts  = [(mp.mpf('0.31'), mp.mpf('0.25')), (mp.mpf('0.77'), mp.mpf('0.4'))]
c_sm, alpha, beta = mp.mpf('0.9'), mp.mpf('-1.3'), mp.mpf('2.5')
n0 = 4
t2_free = mp.mpf('-3.7')     # arbitrary subtraction constant (violates Grow), t_2 has no moment meaning

def moment(n):  # 4*M_2^{(n)} = 4 int x^{n-2} F_2 dx
    s = a_el + sum(b*x**(n-2) for x, b in pts)
    s += c_sm*mp.beta(n-1+alpha, beta+1)
    return 4*s

def integral_tail(m, w):  # 4 w^{m-1} int x^{m-2} F_2/(1-x^2 w^2) dx
    s = a_el/(1-w**2) + sum(b*x**(m-2)/(1-x**2*w**2) for x, b in pts)
    f = lambda x: c_sm*x**(m-2+alpha)*(1-x)**beta/(1-x**2*w**2)
    s += mp.quad(f, [0, mp.mpf('0.5'), 1])
    return 4*w**(m-1)*s

def T2(w):  # Prop 5.6(d) with n0 = 4: T2 = t_2 w + 4 w^3 int x^2 F_2/(1-x^2 w^2)
    return t2_free*w + integral_tail(n0, w)

def t(n):
    if n % 2: return mp.mpf(0)
    return t2_free if n < n0 else moment(n)

# (A) exact remainder identity at complex omega
maxerr = mp.mpf(0)
ws = [mp.mpc('0.3', '0.2'), mp.mpc('-0.55', '0.61'), mp.mpc('0.05', '-0.9'), mp.mpc('1.7', '0.4'),
      mp.mpc('-2.3', '-1.1'), mp.mpc('0', '3.0'), mp.mpc('0.999', '0.01')]
for Np in [4, 6, 8, 10, 12]:
    for w in ws:
        lhs = T2(w) - sum(t(n)*w**(n-1) for n in range(2, Np, 2))
        rhs = integral_tail(Np, w)
        err = abs(lhs-rhs)/max(1, abs(rhs))
        maxerr = max(maxerr, err)
report("(A) exact remainder identity T2 - sum_{n<N'} t_n w^{n-1} = 4 w^{N'-1} int x^{N'-2}F2/(1-x^2w^2) at complex w",
       maxerr < mp.mpf('1e-30'), f"max rel err = {mp.nstr(maxerr, 3)}")

# (B) imaginary-axis bound |tail(iy)| <= t_{N'} |y|^{N'-1} <= t_{n0} |y|^{N'-1}
worst = mp.mpf(0)
for Np in [4, 6, 8, 10]:
    for y in [mp.mpf(v) for v in ['0.001', '0.05', '0.2', '0.5', '1', '3', '10']]:
        w = mp.mpc(0, y)
        tail = abs(T2(w) - sum(t(n)*w**(n-1) for n in range(2, Np, 2)))
        r1 = tail/(t(Np)*y**(Np-1)); r2 = tail/(t(n0)*y**(Np-1))
        worst = max(worst, r1, r2)
        assert t(Np) <= t(n0) + mp.mpf('1e-30')
report("(B) |tail(iy)| <= t_{N'}|y|^{N'-1} <= t_{n0}|y|^{N'-1} (all y, incl. y>1: no condition on r_Q)",
       worst <= 1, f"max ratio = {mp.nstr(worst, 6)}")
# sharpness: purely elastic measure, ratio = 1/(1+y^2) -> 1
y = mp.mpf('1e-4'); Np = 8
tail_el = abs(4*(1j*y)**(Np-1)/(1+y**2)); ratio = tail_el/(4*y**(Np-1))
report("(B') bound is sharp (elastic measure, y->0)", abs(ratio-1) < 1e-7, f"ratio = {mp.nstr(ratio, 10)}")

# (C) old bound 2 t_{n0} r^{N-1} false for odd N: elastic F2 = delta(1-x), t_n = 4 for all even n
fails = []
for N in [5, 7, 9, 11]:
    Np = N-1  # least even >= N-1
    r = mp.mpf('0.2')
    tail = 4*r**(Np-1)/(1+r**2)               # |T2(ir) - sum_{n<N'} 4 (ir)^{n-1}|
    old = 2*4*r**(N-1)
    fails.append((N, tail > old, mp.nstr(tail/old, 5)))
report("(C) old bound 2 t_{n0} r_Q^{N-1} violated for odd N (elastic model, r=0.2)",
       all(f[1] for f in fails), str(fails))

# (D) Markov constant: max over odd real g, deg<=Dg, |g|<=1 on [-1,1], of |g_k| equals |T_m coefficient|,
#     m = largest odd <= Dg.  Check <= (1+sqrt2)^Dg, and LP independent confirmation.
def cheb_coeffs(m):
    c = np.polynomial.chebyshev.cheb2poly([0]*m+[1])
    return c
worst_ratio = 0.0; lp_ok = True; lp_gap = 0.0
for Dg in range(1, 16):
    m = Dg if Dg % 2 else Dg-1
    c = cheb_coeffs(m)
    for k in range(1, m+1, 2):
        val = abs(c[k])
        worst_ratio = max(worst_ratio, val/(1+np.sqrt(2))**Dg)
        if Dg <= 11:
            # LP: maximize g_k s.t. -1 <= g(y_i) <= 1 on grid, g odd of degree <= Dg
            ks = list(range(1, Dg+1, 2))
            ygrid = np.cos(np.linspace(0, np.pi, 4001))
            A = np.array([[yy**kk for kk in ks] for yy in ygrid])
            cvec = np.zeros(len(ks)); cvec[ks.index(k)] = -1.0
            res = linprog(cvec, A_ub=np.vstack([A, -A]), b_ub=np.ones(2*len(ygrid)),
                          bounds=[(None, None)]*len(ks), method='highs')
            lpval = -res.fun
            gap = (lpval - val)/max(1, val)          # LP on a grid is a relaxation: lpval >= val, gap -> 0
            lp_gap = max(lp_gap, abs(gap))
            if not (-1e-9 <= gap <= 2e-5):
                lp_ok = False
                print("   LP mismatch", Dg, k, lpval, val)
report("(D) Lemma 5.3: extremal |h_k| r^k / sup|h| = |t_{m,k}| <= (1+sqrt2)^{Dg} (real coeffs); x2 (or sqrt2) for complex",
       worst_ratio <= 1 and lp_ok, f"max |t_mk|/(1+sqrt2)^Dg = {worst_ratio:.4f}; LP (4001-pt Chebyshev grid) agrees, max rel gap {lp_gap:.1e}: {lp_ok}")

# (E) exponent bookkeeping
bk_ok = True
for n0_ in range(2, 31, 2):
    for n_ in range(2, 31, 2):
        for N in range(max(n_+3, n0_+2), 70):
            Np = N-1 if N % 2 else N
            degPN = N-4 if N % 2 else N-3          # odd P_N: exponents m-1 with m even <= N-2
            degSum = Np-3                          # sum_{n<N', n even} t_n w^{n-1}
            conds = [Np % 2 == 0, Np >= n0_+2, Np >= n_+2, Np >= N-1, max(degPN, degSum) <= Np-3,
                     n_ <= Np-2, n0_ <= Np-2, N-1-n0_ >= 1, min(N-1-n_, Np-n_) == N-1-n_, N-1-n_ >= 2]
            if not all(conds):
                bk_ok = False; print("   bookkeeping fail", n0_, n_, N, conds)
report("(E) bookkeeping: N' even, N'>=n0+2, N'>=n+2, N'>=N-1, deg h<=N'-3, tail never dominates, (M/Q)^{N-1-n}<=(M/Q)^2", bk_ok)

# (F) end-to-end chain (steps 2-4) with synthetic SA data
# T2 exactly from the measure above (Q-independent), r_Q = sqrt3 M/Q.  P_N := sum_{m<=N-2 even} (t_m+delta_m) w^{m-1}
# with random delta_m; eps_N := sup_{I_Q} |T2 - P_N| (so SA(a) holds by construction). Check
# |pi_n - t_n| <= c_N [eps_N r^{1-n} + t_{n0} r^{N'-n}], c_N = 2(1+sqrt2)^{N'-3}, for every even n <= N'-2.
random.seed(7)
chain_ok = True; worst = 0
for N in [6, 7, 8, 9, 10, 11]:
    Np = N-1 if N % 2 else N
    cN = 2*(1+mp.sqrt(2))**(Np-3)
    for rQ in [mp.mpf('0.05'), mp.mpf('0.15'), mp.mpf('0.4')]:
        for trial in range(3):
            delta = {m: mp.mpf(random.uniform(-1, 1))*rQ**(N-1-m)*mp.mpf(10)**random.randint(-3, 0)
                     for m in range(2, N-1, 2)}
            PN = lambda w: sum((t(m)+delta[m])*w**(m-1) for m in range(2, N-1, 2))
            ys = [rQ*mp.mpf(k)/40 for k in range(-40, 41)]
            epsN = max(abs(T2(mp.mpc(0, yy)) - PN(mp.mpc(0, yy))) for yy in ys)
            epsN *= mp.mpf('1.000001')
            for n_ in range(2, Np-1, 2):
                lhs = abs(delta[n_]) if n_ in delta else abs(t(n_))   # pi_n - t_n
                rhs = cN*(epsN*rQ**(1-n_) + t(n0)*rQ**(Np-n_))
                worst = max(worst, lhs/rhs)
                if lhs > rhs: chain_ok = False; print("   chain fail", N, rQ, n_, lhs, rhs)
report("(F) steps 2-4 chain on synthetic SA data (grid sup; N=6..11)", chain_ok, f"max lhs/rhs = {mp.nstr(worst, 4)}")

print("\nOVERALL:", "PASS" if ok_all else "FAIL")
