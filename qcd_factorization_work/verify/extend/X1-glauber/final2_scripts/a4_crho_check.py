# X1 final2 (Fix 7(a)) -- (A4) of T2: on the strip |kappa1+kappa2| <= kappa2/3 (kappa2 > 0, kappa1 = -s < 0),
#   rho(kappa1,kappa2) = (a1 a2/Jcal) sum_t c_t (2s)^{n1-1} (2kappa2)^{n2-1} / (prod_j (a1 - 2 i s A_j) prod_j (a2 - 2 i kappa2 A'_j)).
# Written-out derivation (report, T2 Step 1 (A4)) gives, for every point of the strip,
#   |d rho/d kappa1| <= 2(2nbar-1) mflat_A lambda_A/a_min                                  (all kappa2)
#   |d rho/d kappa1| <= (9/16)(2nbar-1) mflat_A a1 a2 /(kappa2^3 mu_A^2)                   (all kappa2)
# hence |d rho/d kappa1| <= c_rho (lambda_A/a_min) min(1, (kappa*/kappa2)^2), kappa* = a_min/(4 lambda_A),
#   c_rho := 36 (2nbar-1) mflat_A (a_max/a_min) (lambda_A/mu_A)^2.
# The energies need NOT be negative (A4 holds on the imaginary axis for any real energies with |A| >= mu_A).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
rng = np.random.default_rng(2718)
out = []
def log(s=''):
    print(s, flush=True); out.append(s)
w_main = 0.0; w_small = 0.0; w_large = 0.0; info = None
for trial in range(4000):
    lam = 1.0; mu = 10**rng.uniform(-3, np.log10(0.8))
    a1, a2 = 10**rng.uniform(-2, 2, size=2)
    nterms = int(rng.integers(1, 6)); terms = []
    sgnfree = rng.uniform() < 0.3          # 30% of the jets with energies of both signs (no NF)
    for t in range(nterms):
        n1 = 1 if t == 0 else int(rng.integers(1, 6)); n2 = 1 if t == 0 else int(rng.integers(1, 6))
        A = rng.uniform(mu, lam, size=n1)*(rng.choice([-1, 1], size=n1) if sgnfree else -1)
        Ap = rng.uniform(mu, lam, size=n2)*(rng.choice([-1, 1], size=n2) if sgnfree else -1)
        if rng.uniform() < 0.3:            # adversarial: all extra energies at the scale mu
            A[1:] = -mu; Ap[1:] = -mu
        c = (1.0 if t == 0 else rng.normal()*rng.uniform(0.05, 1)*mu**(n1 + n2 - 2))
        terms.append((c, A, Ap))
    J = sum(c for c, A, Ap in terms if len(A) == 1 and len(Ap) == 1)
    nbar = max(max(len(A), len(Ap)) for c, A, Ap in terms)
    mflat = sum(abs(c)*mu**(-(len(A) + len(Ap) - 2)) for c, A, Ap in terms)/abs(J)
    amin, amax = min(a1, a2), max(a1, a2)
    crho = 36*(2*nbar - 1)*mflat*(amax/amin)*(lam/mu)**2
    kstar = amin/(4*lam)
    def drho(s, k2):
        # analytic derivative with respect to s (= -kappa1)
        tot = 0
        for c, A, Ap in terms:
            G = (2*s)**(len(A) - 1)/np.prod(a1 - 2j*s*A)
            dlogG = (len(A) - 1)/s + np.sum(2j*A/(a1 - 2j*s*A))
            H = (2*k2)**(len(Ap) - 1)/np.prod(a2 - 2j*k2*Ap)
            tot += c*G*dlogG*H
        return tot*a1*a2/J
    for k2 in np.exp(np.linspace(np.log(1e-4*kstar), np.log(1e4*kstar), 70)):
        for s in np.linspace(2*k2/3, 4*k2/3, 9):
            d = abs(drho(s, k2))
            b_small = 2*(2*nbar - 1)*mflat*lam/amin
            b_large = (9/16)*(2*nbar - 1)*mflat*a1*a2/(k2**3*mu**2)
            bound = crho*(lam/amin)*min(1, (kstar/k2)**2)
            w_small = max(w_small, d/b_small); w_large = max(w_large, d/b_large)
            r = d/bound
            if r > w_main:
                w_main, info = r, (k2/kstar, mu, nbar, amax/amin, sgnfree)
ok = w_main <= 1 and w_small <= 1 and w_large <= 1
log(f"(A4) 4000 random multi-state mixed-sector jets (up to 5 states per gap; 30% without NF; a_max/a_min up to 1e4):")
log(f"     max |d rho/d kappa1| / [2(2nbar-1) mflat lambda/a_min] = {w_small:.4f}   (<= 1)")
log(f"     max |d rho/d kappa1| / [(9/16)(2nbar-1) mflat a1 a2/(kappa2^3 mu^2)] = {w_large:.4f}   (<= 1)")
log(f"     max |d rho/d kappa1| / [c_rho (lambda/a_min) min(1,(kappa*/kappa2)^2)], c_rho = 36(2nbar-1) mflat (a_max/a_min)(lambda/mu)^2"
    f" = {w_main:.4f} (<= 1); worst at kappa2/kappa* = {info[0]:.3g}, mu/lambda = {info[1]:.3g}, nbar = {info[2]}, a_max/a_min = {info[3]:.3g}")
log("ALL PASS" if ok else "SOME CHECK FAILED")
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'final2_logs', 'a4_crho_check.log'), 'w') as f:
    f.write('\n'.join(out) + '\n')
