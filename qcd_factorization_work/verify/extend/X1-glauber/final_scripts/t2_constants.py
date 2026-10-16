# X1 final revision -- T2 (round-3 fix F4): ingredients of the explicit constants C_X, C_I and numerical status of
# "Im p_opp = -(1/pi) ln(1/eps) + O(1)".
# (1) Random multi-state mixed-sector jets (sector 1V2) with real coefficients and NF:  on the imaginary axis k = i kappa,
#       rho_12(k) = (a1 a2/Jcal) sum_t c_t (2ik)^{n1+n2-2} / (prod_j (2k A_j - a1) prod_j (2k A'_j - a2)),
#     check  (A3)  |rho(i kappa) - 1| <= 4 m_A lambda kappa / a_min      for kappa <= a_min/(2 lambda)
#            (D)   |rho(i kappa)| <= mflat_A min(1, a1 a2/(4 kappa^2 mu^2))   for all kappa
#     with m_A = sum|c_t| lambda^{-d_t}/|Jcal|, mflat_A = sum|c_t| mu^{-d_t}/|Jcal|.
# (2) The O(1) remainder Im p_opp + (1/pi) ln(1/eps) for the scalar base set and three non-factorized jet pairs,
#     from the logged runs (logs/twoexch_rotated_fast2.log; review_r3_1_logs/t2_general.log, which prints eps).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
rng = np.random.default_rng(7)
ok_all = True
worstA3 = 0.0; worstD = 0.0
for trial in range(400):
    lam = 1.0; mu = 10**rng.uniform(-3, np.log10(0.6))
    a1, a2 = rng.uniform(0.2, 2.0, size=2)
    nterms = rng.integers(1, 6)
    terms = []
    # one or more single-single terms (they define Jcal), plus multi-state terms
    for t in range(nterms):
        n1 = 1 if t == 0 else rng.integers(1, 4); n2 = 1 if t == 0 else rng.integers(1, 4)
        A = -rng.uniform(mu, lam, size=n1); Ap = -rng.uniform(mu, lam, size=n2)     # NF: all energies negative
        c = rng.normal()*(1.0 if t == 0 else rng.uniform(0.01, 1.0)*mu**(n1 + n2 - 2))
        terms.append((c, A, Ap))
    Jcal = sum(c for (c, A, Ap) in terms if len(A) == 1 and len(Ap) == 1)
    if abs(Jcal) < 1e-3:
        continue
    mA = sum(abs(c)*lam**(-(len(A) + len(Ap) - 2)) for (c, A, Ap) in terms)/abs(Jcal)
    mfA = sum(abs(c)*mu**(-(len(A) + len(Ap) - 2)) for (c, A, Ap) in terms)/abs(Jcal)
    amin = min(a1, a2)
    kap = np.exp(np.linspace(np.log(1e-4), np.log(1e6), 3000))
    k = 1j*kap
    rho = np.zeros_like(k)
    for (c, A, Ap) in terms:
        val = c*(2j*k)**(len(A) + len(Ap) - 2)
        for x in A: val = val/(2*k*x - a1)
        for x in Ap: val = val/(2*k*x - a2)
        rho = rho + val
    rho = rho*a1*a2/Jcal
    sel = kap <= amin/(2*lam)
    worstA3 = max(worstA3, np.max(np.abs(rho[sel] - 1)/(4*mA*lam*kap[sel]/amin)))
    worstD = max(worstD, np.max(np.abs(rho)/(mfA*np.minimum(1, a1*a2/(4*kap**2*mu**2)))))
okA = worstA3 <= 1 + 1e-12 and worstD <= 1 + 1e-12
ok_all &= okA
print(f"(1) 400 random multi-state mixed-sector jets: max |rho-1|/(4 m_A lambda kappa/a_min) = {worstA3:.3f} (<= 1);"
      f"  max |rho|/(mflat_A min(1, a1a2/(4kappa^2mu^2))) = {worstD:.3f} (<= 1);  ok={okA}")

print("(2) O(1) remainder of Im p_opp:")
rows = [("scalar base set", [(1.167e-3, -2.113440), (1.051e-4, -2.875446), (1.167e-5, -3.574342)]),
        ("general pair 0", [(8.92e-3, -1.60248), (8.92e-4, -2.31899), (8.92e-5, -3.04947)]),
        ("general pair 1", [(9.07e-3, -1.75033), (9.07e-4, -2.44598), (9.07e-5, -3.17300)]),
        ("general pair 2", [(8.87e-3, -0.86576), (8.87e-4, -1.54609), (8.87e-5, -2.27111)])]
for name, pts in rows:
    rem = [im + np.log(1/eps)/np.pi for (eps, im) in pts]
    spread = max(rem) - min(rem)
    print(f"    {name:16s}: Im p_opp + (1/pi)ln(1/eps) = " + ", ".join(f"{r:+.4f}" for r in rem) +
          f"   (eps = " + ", ".join(f"{e:.2e}" for e, _ in pts) + f");  spread {spread:.3f}")
    ok_all &= spread < 0.1
print("ALL PASS" if ok_all else "SOME CHECK FAILED")
