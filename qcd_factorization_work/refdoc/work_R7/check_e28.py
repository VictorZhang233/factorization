"""Checks of Lemma E.28 (eqs. E.28, E.29) and Note E.29(2) of the reference document.
Model (LCOPT form, Lemma E.22):
  J_in(k) = c1/(k+A1+i e) + c2/((k+A1+i e)(k+A2+i e))         [initial-state denominators, analytic in UHP]
  J_fi(k) = d1/(A3-k+i e) + d2/((A3-k+i e)(A4-k+i e))         [final-state denominators, analytic in LHP]
  J_- = -i c1,  J_+ = -i d1  (from J_in ~ iJ_-/k, J_fi ~ -iJ_+/k);  spectator insertion: c1 = d1.
External factor: R(k) = r/(k - z), single pole (direct Glauber line: z = kT^2/(2k^+) -/+ i0).
All integrals done exactly by partial fractions (simple poles)."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 40
I = mp.mpc(0, 1)

def pf_terms(c1, c2, d1, d2, A1, A2, A3, A4, eps, r, z):
    """Return list of (residue, pole) for J(k) R(k) = sum res/(k - pole)."""
    terms = []
    p1, p2 = -A1 - I * eps, -A2 - I * eps          # J_in poles (LHP)
    p3, p4 = A3 + I * eps, A4 + I * eps            # J_fi poles (UHP)
    # J_in R = c1 r /((k-p1)(k-z)) + c2 r/((k-p1)(k-p2)(k-z))
    def add(coef, poles):
        for i, pi in enumerate(poles):
            res = coef
            for j, pj in enumerate(poles):
                if j != i: res /= (pi - pj)
            terms.append((res, pi))
    add(c1 * r, [p1, z]); add(c2 * r, [p1, p2, z])
    # J_fi = d1/(A3-k+ie) = -d1/(k-p3);  d2/((A3-k)(A4-k)) = d2/((k-p3)(k-p4))
    add(-d1 * r, [p3, z]); add(d2 * r, [p3, p4, z])
    return terms

def int_full(terms):
    # int_R dk/2pi sum res/(k-p): for 1/k^2 decay, = i * sum_{Im p>0} res
    s = sum(res for res, p in terms)
    assert abs(s) < mp.mpf('1e-25'), s
    return I * sum(res for res, p in terms if mp.im(p) > 0)

def int_window(terms, K1, K2):
    return sum(res * (mp.log(K2 - p) - mp.log(-K1 - p)) for res, p in terms) / (2 * mp.pi)

def run(lamJ, Lam, kplus_sign, spectator=True, show=True):
    A1, A2, A3, A4 = 0.6 * lamJ, -0.9 * lamJ, 0.8 * lamJ, -0.5 * lamJ
    c1 = mp.mpc(0.7, 0.3); c2 = mp.mpc(-0.4, 0.2) * lamJ
    d1 = c1 if spectator else mp.mpc(-0.2, 0.5); d2 = mp.mpc(0.3, -0.6) * lamJ
    eps = mp.mpf('1e-30')
    z = 2 * Lam * (1 if kplus_sign > 0 else -1) - I * eps * kplus_sign   # k+>0: pole in LHP (R_down)
    r = -z   # normalise R(0) = 1
    Jm, Jp = -I * c1, -I * d1
    terms = pf_terms(c1, c2, d1, d2, A1, A2, A3, A4, eps, r, z)
    full = int_full(terms)
    R0 = r / (0 - z)
    c = R0 / R0 if mp.im(z) < 0 else 0      # R is a single pole: R_down(0)/R(0) = 1 or 0
    pred = R0 * (Jm + c * (Jp - Jm))
    return full, pred, Jm, Jp, terms, z, r

print("Lemma E.28(iii): full real axis, single-pole R; error should scale like lambda_J/Lambda")
for spect in [True, False]:
    for sgn in [+1, -1]:
        errs = []
        for Lam in [mp.mpf(10), mp.mpf(100), mp.mpf(1000)]:
            full, pred, Jm, Jp, terms, z, r = run(mp.mpf(1), Lam, sgn, spectator=spect)
            errs.append(abs(full - pred))
        ratios = [errs[i] / errs[i + 1] for i in range(2)]
        ok = all(abs(x - 10) < 0.5 for x in ratios)
        print(f"  {'spectator' if spect else 'active   '} k+ {'>' if sgn>0 else '<'} 0: |err| at Lam=10,100,1000: {[mp.nstr(e,4) for e in errs]}  ratio {[mp.nstr(x,4) for x in ratios]} {'PASS (1/Lambda)' if ok else 'CHECK'}")
        if not spect:
            print(f"      active line: J_+ != J_- ; c = theta(k+) = {1 if sgn>0 else 0}; result depends on c as claimed")

print("\nLemma E.28(ii): window [-K,K], 2 lamJ <= K <= Lam/2 :  R(0)(J_+ + J_-)/2 + iKR'(0)(J_- - J_+)/pi + O(lamJ/K + K^2/Lam^2)")
for spect in [True, False]:
    lamJ, Lam = mp.mpf(1), mp.mpf(10)**4
    for K in [mp.mpf(30), mp.mpf(100), mp.mpf(300)]:
        full, pred, Jm, Jp, terms, z, r = run(lamJ, Lam, +1, spectator=spect)
        win = int_window(terms, K, K)
        R0 = r / (0 - z); R1 = -r / (0 - z) ** 2
        predw = R0 * (Jp + Jm) / 2 + I * K * R1 / mp.pi * (Jm - Jp)
        err = abs(win - predw)
        bound = abs(Jm) * (lamJ / K + K**2 / Lam**2)
        print(f"  {'spectator' if spect else 'active   '} K={mp.nstr(K,4)}: window={mp.nstr(win,8)}  pred={mp.nstr(predw,8)}  |err|={mp.nstr(err,3)}  (lamJ/K+K^2/Lam^2)*|J|={mp.nstr(bound,3)}")
print("  asymmetric window [-K1,K2], spectator: result R(0)J(0) independent of shape:")
for (K1, K2) in [(100, 100), (100, 400), (400, 100), (50, 2000)]:
    full, pred, Jm, Jp, terms, z, r = run(mp.mpf(1), mp.mpf(10)**5, +1, spectator=True)
    win = int_window(terms, mp.mpf(K1), mp.mpf(K2))
    print(f"    K1={K1}, K2={K2}: window={mp.nstr(win,10)}  R(0)J(0)={mp.nstr(Jm,10)}  rel.diff={mp.nstr(abs(win-Jm)/abs(Jm),3)}")

print("\nNote E.29(2): Glauber line R ~ 1/(2k+k - kT^2 + i0), Lambda = kT^2/(4|k+|), window K = delta kT^2/|k+| = 4 delta Lambda")
for delta in [mp.mpf('0.125'), mp.mpf('0.05'), mp.mpf('0.01')]:
    for sgn in [+1, -1]:
        lamJ, Lam = mp.mpf(1), mp.mpf(10)**6
        full, pred, Jm, Jp, terms, z, r = run(lamJ, Lam, sgn, spectator=False)
        K = 4 * delta * Lam
        win = int_window(terms, K, K)
        # extract effective c from window result: win = R0[J_- + c (J_+ - J_-)]
        R0 = r / (0 - z)
        c_eff = (win / R0 - Jm) / (Jp - Jm)
        c_full = (full / R0 - Jm) / (Jp - Jm)
        c_pred = mp.mpf(1)/2 - 2 * I * delta * sgn / mp.pi
        print(f"  delta={mp.nstr(delta,3)}, sgn(k+)={sgn:+d}: c(window)={mp.nstr(c_eff,6)}  pred 1/2-2i delta sgn/pi={mp.nstr(c_pred,6)}  |  c(full axis)={mp.nstr(c_full,6)} (pred theta(k+)={1 if sgn>0 else 0})")
