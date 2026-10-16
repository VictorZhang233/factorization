# X1 final revision -- T3(e'),(f): RECOMPUTATION of the small-K values of Im W12(K) (round-3 note on EX:
# fix_r2_scripts/t3e_sensitivity.py item (iv) only reprinted the round-1 numbers).  Uses the closed-form L1'
# pole weights and the rotated-contour quadrature of fix_r1_scripts/regulator_indep.py (jet A localized,
# even Lorentzian A-side k^- regulator chi_K = K^2/(k^2+K^2) on both lines), at theta = pi/8 and pi/4.
# Also checks the boost behaviour of the terms of the corrected T3(e) bound (F5): under k^+ -> e^y k^+,
# k^- -> e^{-y} k^-, the combinations K lambda_B/a, lambda_A/K, a/(K mu_B) are invariant, K/mu_B is not.
import sys, os, time
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'fix_r1_scripts'))
import numpy as np
import sympy as sp
import regulator_indep as ri

ok_all = True
for variant in ('author', 'Basym'):
    m = ri.halfcoinc_model(variant)
    lamB = abs(m['d0']); a = np.sqrt(m['a1']*m['a2'])
    JB = lambda u1, u2, q: ri.JB_half(-u1, -u2, m)
    print(f"[{variant}] alpha1={m['al1']:.4f} alpha2={m['al2']:.4f} beta={m['beta']:.4f} d0={m['d0']:.4f}  a1={m['a1']:.3f} a2={m['a2']:.3f}")
    den = {th: ri.integrate(JB, th) for th in (np.pi/8, np.pi/4)}
    for Kr in (None, 1.0, 0.1, 0.01, 0.001):
        K = None if Kr is None else Kr*a/lamB
        vals = []
        for th in (np.pi/8, np.pi/4):
            t0 = time.time()
            num = ri.integrate(lambda u1, u2, q: ri.W12(u1, u2, m['a1'], m['a2'], K, q)*JB(u1, u2, q), th)
            vals.append(num/den[th])
        agree = abs(vals[0] - vals[1])
        ok_all &= agree < 1e-6
        lab = "no regulator" if Kr is None else f"K = {Kr:g} a/lambda_B"
        extra = "" if Kr is None else f";  Im W12/(K lambda_B/a) = {vals[1].imag/Kr:+.4f}"
        print(f"    {lab:22s}: W12 = {vals[1]:.8f}  (theta=pi/8 vs pi/4 differ by {agree:.1e}){extra}")

# boost behaviour of the terms in the T3(e) bound
y = sp.symbols('y', real=True)
K, lA, lB, muB, a_ = sp.symbols('K lambda_A lambda_B mu_B a', positive=True)
boost = {K: K*sp.exp(-y), lA: lA*sp.exp(-y), lB: lB*sp.exp(y), muB: muB*sp.exp(y)}
for name, expr in [("K lambda_B/a", K*lB/a_), ("lambda_A/K", lA/K), ("a/(K mu_B)", a_/(K*muB)), ("K/mu_B", K/muB)]:
    ratio = sp.simplify(expr.subs(boost, simultaneous=True)/expr)
    print(f"    boost: {name:14s} -> factor {ratio}")
    if name != "K/mu_B":
        ok_all &= (ratio == 1)
    else:
        ok_all &= (ratio != 1)
print("ALL PASS" if ok_all else "SOME CHECK FAILED")
