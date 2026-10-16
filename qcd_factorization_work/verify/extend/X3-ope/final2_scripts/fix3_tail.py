"""
fix3_tail.py  (X3 final2, Fix 3: Theorem 5.7 step 1)

Checks, for test structure functions F2 dx >= 0 on (0,1] (continuum + elastic point mass), of the
subtracted dispersion relation of Prop. 5.6(d)

    T2(w) = sum_{n<n0} t_n w^{n-1} + 4 w^{n0-1} int x^{n0-2} F2(x) dx / (1 - x^2 w^2),   t_n = 4 M2^(n) (n >= n0),

(the subtraction constants t_n, n < n0, are chosen NOT equal to the moments, to mimic a failure of Grow):

 (a) exact remainder: for every even N' >= n0 and real y,
        T2(iy) - sum_{n<N'} t_n (iy)^{n-1} = 4 (iy)^{N'-1} int x^{N'-2} F2 / (1 + x^2 y^2) dx,
     hence |...| <= t_{N'} |y|^{N'-1} <= t_{n0} |y|^{N'-1}.
 (b) the bound printed in X3-ope_final.md, |tail| <= 2 t_{n0} r^{N-1}, FAILS for odd N (elastic model), while the
     corrected bound t_{n0} r^{N'-1}, N' = least even integer >= N-1 (= N-1 for odd N), holds.
 (c) the whole chain of Theorem 5.7 on a synthetic SA situation: P_N = odd polynomial of degree <= N-3 obtained by
     perturbing the Taylor coefficients; eps_N := sup_{|y|<=r} |T2(iy) - P_N(iy)| (dense grid);
     Markov step:  |t_n' - pi_n'| <= 2 (1+sqrt2)^{N'-3} (eps_N + t_{n0} r^{N'-1}) r^{1-n'}  for all even n' <= N'-2.
 (d) exponent bookkeeping: N >= max(n+3, n0+2) => N' >= n0+2, N'-n >= N-1-n >= 2.
Run: python3 -I fix3_tail.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp

mp.mp.dps = 40
ok_all = True

def make_model(alpha, beta, cont, el):
    """F2 dx = cont * x^alpha (1-x)^beta dx + el * delta(x-1) dx ; returns moment function M(k) = int x^k F2 dx."""
    def M(k):
        return cont * mp.beta(alpha + k + 1, beta + 1) + el
    def integral(k, y):
        # int x^k F2(x)/(1 + x^2 y^2) dx
        f = lambda x: cont * x**(alpha + k) * (1 - x)**beta / (1 + x**2 * y**2)
        return mp.quad(f, [0, 0.5, 1]) + el / (1 + y**2)
    return M, integral

models = {
    "smooth+elastic": (mp.mpf('0.5'), mp.mpf(3), mp.mpf('0.8'), mp.mpf('0.05')),
    "valence-like":   (mp.mpf('0.7'), mp.mpf('3.5'), mp.mpf(2), mp.mpf(0)),
    "elastic only":   (mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf('0.25')),
}

n0 = 4
subtr = {2: mp.mpf('0.37')}   # arbitrary subtraction constant t_2 (not 4 M2^(2))

print("(a) exact remainder identity and bound at w = iy (n0 = %d, t_2 = %s arbitrary)" % (n0, subtr[2]))
for name, (al, be, co, el) in models.items():
    M, integral = make_model(al, be, co, el)
    t = lambda n: subtr[n] if n < n0 else 4 * M(n - 2)
    def T2(y):
        w = mp.mpc(0, y)
        s = sum(subtr[n] * w**(n - 1) for n in subtr)
        return s + 4 * w**(n0 - 1) * integral(n0 - 2, y)
    worst_id = mp.mpf(0); worst_ratio = mp.mpf(0)
    for Np in (4, 6, 8, 10):
        for y in (mp.mpf('0.05'), mp.mpf('0.3'), mp.mpf('0.9'), mp.mpf('2.5')):
            w = mp.mpc(0, y)
            lhs = T2(y) - sum(t(n) * w**(n - 1) for n in range(2, Np, 2))
            rhs = 4 * w**(Np - 1) * integral(Np - 2, y)
            worst_id = max(worst_id, abs(lhs - rhs) / max(abs(rhs), mp.mpf(10)**-30))
            bound = t(n0) * abs(y)**(Np - 1)
            worst_ratio = max(worst_ratio, abs(lhs) / bound)
    ok = worst_id < mp.mpf(10)**-25 and worst_ratio <= 1
    ok_all &= ok
    print("   %-15s max rel. deviation of identity = %.1e ; max |remainder|/(t_n0 |y|^(N'-1)) = %.6f  -> %s"
          % (name, float(worst_id), float(worst_ratio), ok))

print("(b) old bound 2 t_n0 r^(N-1) versus corrected bound t_n0 r^(N'-1), elastic-only model (t_n = 1 for n >= n0)")
M, integral = make_model(*models["elastic only"])
old_fails = False; new_holds = True
for N in (5, 6, 7, 8, 9):
    Np = N - 1 if N % 2 == 1 else N
    for r in (mp.mpf('0.02'), mp.mpf('0.1'), mp.mpf('0.3')):
        w = mp.mpc(0, r)
        tail = abs(4 * w**(Np - 1) * integral(Np - 2, r))     # exact remainder at |y| = r
        oldb = 2 * 1 * r**(N - 1); newb = 1 * r**(Np - 1)
        old_fails |= tail > oldb
        new_holds &= tail <= newb
        print("   N=%d N'=%d r=%.2f : |tail| = %.3e   old 2t r^(N-1) = %.3e (%s)   new t r^(N'-1) = %.3e (%s)"
              % (N, Np, float(r), float(tail), float(oldb), "holds" if tail <= oldb else "FAILS",
                 float(newb), "holds" if tail <= newb else "FAILS"))
ok_all &= old_fails and new_holds
print("   old bound fails for some odd N: %s ; corrected bound holds everywhere: %s" % (old_fails, new_holds))

print("(c) Theorem 5.7 chain (Markov step) on synthetic SA data")
import random
random.seed(7)
M, integral = make_model(*models["smooth+elastic"])
t = lambda n: subtr[n] if n < n0 else 4 * M(n - 2)
def T2(y):
    w = mp.mpc(0, y)
    return sum(subtr[n] * w**(n - 1) for n in subtr) + 4 * w**(n0 - 1) * integral(n0 - 2, y)
chain_ok = True
for N in (7, 8, 9, 10):                    # N >= n0 + 2 = 6 ; odd and even N
    Np = N - 1 if N % 2 == 1 else N
    for r in (mp.mpf('0.05'), mp.mpf('0.15')):
        # P_N: odd, terms pi_m w^{m-1}, m even <= N-2; pi_m = t_m + small perturbation
        pis = {m: t(m) * (1 + mp.mpf(random.uniform(-1, 1)) * mp.mpf('1e-3')) for m in range(2, N - 1, 2)}
        PN = lambda y: sum(pis[m] * mp.mpc(0, y)**(m - 1) for m in pis)
        grid = [r * k / 400 for k in range(-400, 401)]
        epsN = max(abs(T2(y) - PN(y)) for y in grid)
        cD = 2 * (1 + mp.sqrt(2))**(Np - 3)
        for nprime in range(2, Np - 1, 2):
            lhs = abs(t(nprime) - pis.get(nprime, 0))
            rhs = cD * (epsN + t(n0) * r**(Np - 1)) * r**(1 - nprime)
            chain_ok &= lhs <= rhs
        print("   N=%2d N'=%2d r=%.2f eps_N=%.2e : Markov-step bound holds for all even n' <= N'-2: %s"
              % (N, Np, float(r), float(epsN), chain_ok))
ok_all &= chain_ok

print("(d) exponent bookkeeping")
bk = True
for n in range(2, 21, 2):
    for n0_ in range(2, 21, 2):
        for N in range(max(n + 3, n0_ + 2), max(n + 3, n0_ + 2) + 6):
            Np = N - 1 if N % 2 == 1 else N
            bk &= (Np >= n0_ + 2) and (Np - n >= N - 1 - n >= 2) and (Np >= N - 1) and (N - 1 - n0_ >= 1)
print("   N >= max(n+3, n0+2) => N' >= n0+2, N'-n >= N-1-n >= 2, N-1-n0 >= 1 (all even n, n0 <= 20): %s" % bk)
ok_all &= bk
print("RESULT:", "PASS" if ok_all else "FAIL")
