"""X2 final2 / f2_C4e3_checks.py -- final-review Fix 7 (Prop C.4(e3)) and Fix 9 (Thm B.5 lower bound).

(A) Fix 7(a): the S^{3-2eps} average <h_0>(t) = a^-1 2F1(1/2,1;2-eps;z), a = A + t/(1-xi), z = 4t/a^2, A = 1 - xi/x.
    (A1) 1 - z <= 1 is attained only at t = A(1-xi): z_max = (1-xi)/A, 1 - z_max = xi c_x/A >= xi c_x.
    (A2) the bounds used in the proof:  1 <= F(z) <= K_eps [1 + (1-z)^(1/2-eps)]  and  F(z) - 1 <= z F(z)  (0 <= z < 1),
         F = 2F1(1/2,1;2-eps;.) (Euler representation (1-eps) int_0^1 (1-s)^-eps (1-zs)^-1/2 ds);
         K_eps = (1-eps) max(1/(1-eps) + sqrt2/(1/2-eps), ...) -- checked numerically on a grid in z;
    (A3) F(1) = Gamma(2-eps)Gamma(1/2-eps)/(Gamma(3/2-eps)Gamma(1-eps)) for eps < 1/2 (e.g. 3.49997 at eps = 0.3), and
         F(z) ~ Gamma(2-eps)Gamma(eps-1/2)/Gamma(1/2) (1-z)^(1/2-eps) for 1/2 < eps < 1;
    (A4) the xi-dependence of the two constants of step 1, C_1(xi) = sup_{0<t<=1} |<h_0> - 1/A| (1-xi)/t and
         C_2(xi) = sup_{t>=1} |<h_0>| t/(1-xi): bounded as xi -> 0 for eps < 1/2, ~ xi^(1/2-eps) for eps > 1/2 (x = 2).
(B) Fix 7(b): T(eps) in its square, simplex and closed forms (x = 2, c = 1/2) at eps = -0.6, -0.3 to high precision
    (the r3 log had only 5.6e-11 at eps = -0.3: quadrature-limited, (1-y)^(-1-eps) endpoint).
(C) Fix 9: the lower bound int_{U_S} rho_{C_C1} >= lambda^2/4 on the cover family s = lambda^theta, theta in (0,2]
    (Q~ = 1, P = P' = 1/sqrt2, eps = 0), and the exact kappa-integral used."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import functools
print = functools.partial(print, flush=True)
ALL_OK = True
def report(name, ok):
    global ALL_OK
    ALL_OK &= bool(ok)
    print(f"   [{'PASS' if ok else 'FAIL'}] {name}")

mp.mp.dps = 30
print("(A) Fix 7(a): growth of the constants of step 1 of Prop C.4(e3)")
x = mp.mpf(2); cx = 1 - 1/x
def F(e, z): return mp.hyp2f1(mp.mpf(1)/2, 1, 2 - e, z)
for xi in [mp.mpf('0.1'), mp.mpf('0.01')]:
    A = 1 - xi/x; tstar = A*(1 - xi); a = A + tstar/(1 - xi); zmax = 4*tstar/a**2
    report(f"(A1) xi = {xi}: z(t) maximal at t = A(1-xi), z_max = {mp.nstr(zmax, 12)} = (1-xi)/A = "
           f"{mp.nstr((1 - xi)/A, 12)}, 1 - z_max = {mp.nstr(1 - zmax, 6)} >= xi c_x = {mp.nstr(xi*cx, 6)}",
           abs(zmax - (1 - xi)/A) < mp.mpf('1e-25') and 1 - zmax >= xi*cx)
for e in [mp.mpf('0.3'), mp.mpf('0.45'), mp.mpf('0.55'), mp.mpf('0.6'), mp.mpf('0.9')]:
    zs = [1 - mp.mpf(10)**(-k) for k in range(1, 13)] + [mp.mpf(j)/20 for j in range(20)]
    rat = max(F(e, z)/(1 + (1 - z)**(mp.mpf(1)/2 - e)) for z in zs)
    ineq = all(F(e, z) - 1 <= z*F(e, z) + mp.mpf('1e-25') for z in zs)
    report(f"(A2) eps = {e}: sup_z F(z)/(1 + (1-z)^(1/2-eps)) = {mp.nstr(rat, 8)} (finite); F - 1 <= z F on the grid: {ineq}",
           rat < 10 and ineq)
e = mp.mpf('0.3')
F1 = mp.gamma(2 - e)*mp.gamma(mp.mpf(1)/2 - e)/(mp.gamma(mp.mpf(3)/2 - e)*mp.gamma(1 - e))
d12 = F1 - F(e, 1 - mp.mpf('1e-12')); d24 = F1 - F(e, 1 - mp.mpf('1e-24'))
report(f"(A3) eps = 0.3: F(1) = Gamma(2-e)Gamma(1/2-e)/(Gamma(3/2-e)Gamma(1-e)) = {mp.nstr(F1, 10)} = hyp2f1(.,1) "
       f"{mp.nstr(mp.hyp2f1(0.5, 1, 2 - e, 1), 10)};  F(1) - F(1-1e-12) = {mp.nstr(d12, 5)}, F(1) - F(1-1e-24) = {mp.nstr(d24, 5)}"
       f" (ratio {mp.nstr(d12/d24, 5)} = 10^(12(1/2-eps)) = {mp.nstr(mp.mpf(10)**(12*(0.5 - e)), 5)}: bounded, approach (1-z)^(1/2-eps))",
       abs(F1 - mp.hyp2f1(0.5, 1, 2 - e, 1)) < mp.mpf('1e-20') and abs(d12/d24/mp.mpf(10)**(12*(0.5 - e)) - 1) < mp.mpf('1e-2'))
e = mp.mpf('0.6')
coef = mp.gamma(2 - e)*mp.gamma(e - mp.mpf(1)/2)/mp.gamma(mp.mpf(1)/2)
vals = [(F(e, 1 - mp.mpf(10)**(-k)) + 4*0 )*mp.mpf(10)**(-k*(e - mp.mpf(1)/2)) for k in (8, 16, 24)]
report(f"(A3) eps = 0.6: F(z)(1-z)^(eps-1/2) -> Gamma(2-e)Gamma(e-1/2)/Gamma(1/2) = {mp.nstr(coef, 8)}: "
       f"{[mp.nstr(v, 8) for v in vals]} (unbounded F)", abs(vals[-1]/coef - 1) < mp.mpf('1e-2'))
def consts(e, xi):
    A = 1 - xi/x
    def h0(t):
        a = A + t/(1 - xi); return F(e, 4*t/a**2)/a
    ts1 = [mp.mpf(10)**(-k) for k in range(0, 9)] + [mp.mpf(j)/10 for j in range(1, 10)] + [A*(1 - xi)*(1 + d) for d in (-0.01, 0, 0.01) if A*(1 - xi)*(1 + d) <= 1]
    ts2 = [mp.mpf(10)**k for k in range(0, 7)] + [A*(1 - xi)*(1 + d) for d in (-0.01, 0, 0.01) if A*(1 - xi)*(1 + d) >= 1] + [mp.mpf(j) for j in (2, 3, 5)]
    C1 = max(abs(h0(t) - 1/A)*(1 - xi)/t for t in ts1)
    C2 = max(abs(h0(t))*t/(1 - xi) for t in ts2)
    return C1, C2
for e in [mp.mpf('0.3'), mp.mpf('0.6'), mp.mpf('0.9')]:
    rows = [(xi, *consts(e, xi)) for xi in [mp.mpf('1e-2'), mp.mpf('1e-4'), mp.mpf('1e-6'), mp.mpf('1e-8')]]
    norm = [max(r_[1], r_[2])/(1 + (r_[0]*cx)**(mp.mpf(1)/2 - e)) for r_ in rows]
    raw = [max(r_[1], r_[2]) for r_ in rows]
    grows = e > mp.mpf(1)/2
    report(f"(A4) eps = {e}: C_1(xi) at xi = 1e-2, 1e-4, 1e-6, 1e-8: {[mp.nstr(r_[1], 6) for r_ in rows]}; C_2: "
           f"{[mp.nstr(r_[2], 6) for r_ in rows]};  max(C_1,C_2)/(1 + (xi c_x)^(1/2-eps)) = {[mp.nstr(v_, 4) for v_ in norm]} "
           f"(bounded{'; the constants themselves grow' if grows else '; the constants themselves stay bounded'})",
           max(norm) < 2*norm[0] + 5 and (raw[-1] > 2*raw[0] if grows else raw[-1] < 10))

print("\n(B) Fix 7(b): simplex identity at eps = -0.6, -0.3 (x = 2, c = 1/2), high precision")
mp.mp.dps = 30
c = 1 - 1/x
def T_square(e):
    # int_0^1 ds s^(1-e) int_0^1 dy y (1-y)^(-1-e) (c(1-s) + y s)^(-1-e);  y = 1 - u^p, p = 2/(-e)
    p = 2/(-e)
    inner = lambda s: mp.quad(lambda u_: p*u_**(p - 1)*(1 - u_**p)*u_**(p*(-1 - e))*(c*(1 - s) + (1 - u_**p)*s)**(-1 - e), [0, 0.5, 1])
    return mp.quad(lambda s: s**(1 - e)*inner(s), [0, 0.5, 1])
def T_simplex(e):
    # int_{alpha+beta+gamma=1} beta gamma^(-1-e) (c alpha + beta)^(-1-e);  gamma = u^p, then (alpha, beta) = (1-gamma)(1-w, w)
    p = 2/(-e)
    def g(u_):
        gm = u_**p; jac = p*u_**(p - 1)
        return jac*gm**(-1 - e)*(1 - gm)*mp.quad(lambda w: (1 - gm)*w*((1 - gm)*(c*(1 - w) + w))**(-1 - e), [0, 1])
    return mp.quad(g, [0, 0.5, 1])
def T_closed(e):
    return mp.beta(-e, 2 - e)*((1 - c**(1 - e))/(1 - e) + (c - c**(1 - e))/e)/(1 - c)**2
for ev in ['-0.6', '-0.3']:
    e = mp.mpf(ev)
    ts, tp, tc = T_square(e), T_simplex(e), T_closed(e)
    report(f"eps = {ev}: T(square) = {mp.nstr(ts, 25)}  T(simplex) rel.dev {mp.nstr(abs(tp/ts - 1), 3)}  closed rel.dev "
           f"{mp.nstr(abs(tc/ts - 1), 3)}", abs(tp/ts - 1) < mp.mpf('1e-20') and abs(tc/ts - 1) < mp.mpf('1e-20'))

print("\n(C) Fix 9: int_{U_S} rho_{C_C1} >= lambda^2/4 on s = lambda^theta (Q~ = 1, P = P' = 1/sqrt2, eps = 0)")
mp.mp.dps = 25
P = 1/mp.sqrt(2)
def item_US(m2, s):
    # rho = x m2/(A B), A = x m2 (1-u) + P kappa, B = x m2 + P kappa, x = P u;  int_0^{u s} dkappa exactly:
    #   int_0^K dk x m2/((a1 + P k)(a2 + P k)) = (x m2/(P (a2 - a1))) ln( a2 (a1 + P K)/(a1 (a2 + P K)) ),  a1 < a2
    def inner(u):
        # = (1/(P u)) [ -log(1-u) + log(1 - x m2 u/(a2 + P K)) ]  (a2 - a1 = x m2 u), written without cancellation
        xx = P*u; a2 = xx*m2; K = u*s
        return (-mp.log1p(-u) + mp.log1p(-xx*m2*u/(a2 + P*K)))/(P*u)
    return mp.quad(lambda u: P*inner(u), [0, s/10, s])        # dx = P du
for lam2 in [mp.mpf('1e-4'), mp.mpf('1e-6')]:
    for th in [mp.mpf(1), mp.mpf('1.5'), mp.mpf(2)]:
        s = lam2**(th/2); val = item_US(lam2, s)
        report(f"lambda^2 = {lam2}, theta = {th}: int_(U_S) rho_C_C1 = {mp.nstr(val, 8)} = {mp.nstr(val/lam2, 6)} lambda^2"
               f" >= lambda^2/4;  s/4 = {mp.nstr(s/4, 6)}", val >= lam2/4)
print("\nALL CHECKS PASS" if ALL_OK else "\nSOME CHECK FAILED")
