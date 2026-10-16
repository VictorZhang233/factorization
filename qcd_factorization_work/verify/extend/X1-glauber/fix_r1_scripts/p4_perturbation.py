# X1 fix round 1 -- P4: the per-graph weight W(12,21) depends on jet data outside the Glauber window.
# Mixed sector (1V2) of jet A: single-state term c1 [i/(A+k1)][i/(A'-k2)] (fixes Jcal_sigma = c1) plus a
# two-state initial-gap term c2 [i/(A1+k1)][i/(A2+k1)][i/(A'-k2)] with c2 = -i*ct2 (same overall phase, (R)).
# The perturbation leaves D_win = {Jcal_sigma, lambda_A} unchanged (|A1|,|A2| <= lambda_A) but changes
# rho_12(k) = (a1 a2/Jcal_A) F_A^[12](-k,k) by s*rho2(k), with (derivation in REPORT P4)
#     rho2(k) = (a1 a2/c1) * 2 k ct2 / ((2kA1 - a1)(2kA2 - a1)(2kA' - a2)).
# By T2 Step 4, W(12,21) changes by  dW = -(i s/2pi) * int_0^inf (dkappa/kappa) rho2(i kappa) + o(1).
# Check: Im int = 0 (rho2 real on the axis, rho2(0) = 0: Cauchy), Re int != 0  =>  dW is purely imaginary, O(s).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 30
def rho2(k, a1, a2, A1, A2, Ap, ct2_over_c1):
    return a1*a2*ct2_over_c1*2*k/((2*k*A1 - a1)*(2*k*A2 - a1)*(2*k*Ap - a2))
ok = True
for (a1, a2, A1, A2, Ap, r) in ((1, 1, -1, -2, -1, 1), (0.65, 0.9, -1.6, -0.3, -1.6, 0.7), (1, 2, -0.5, -3, -2, -1.3)):
    f = lambda kap: rho2(1j*kap, a1, a2, A1, A2, Ap, r)/kap
    I = mp.quad(f, [0, 0.01, 0.1, 1, 10, 100, mp.inf])
    realaxis = mp.quad(lambda k: rho2(k, a1, a2, A1, A2, Ap, r)/k, [0, 1, mp.inf])
    print(f"a=({a1},{a2}) A1={A1} A2={A2} A'={Ap} ct2/c1={r}:  int dk/k rho2(ik) = {mp.nstr(I, 12)}   "
          f"(Im part ~ 0: {abs(mp.im(I)) < 1e-20});  dW/s = -(i/2pi)*int = {mp.nstr(-1j*I/(2*mp.pi), 10)};  "
          f"int on real axis = {mp.nstr(realaxis, 12)}")
    ok = ok and abs(mp.im(I)) < 1e-20 and abs(mp.re(I)) > 1e-3
print("PASS: per-graph W(12,21) shifts by a purely imaginary O(1)*s amount with D_win fixed" if ok else "FAIL")
