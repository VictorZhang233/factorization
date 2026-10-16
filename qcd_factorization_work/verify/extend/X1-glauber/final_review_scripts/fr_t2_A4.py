# Final review of X1 -- T2 Step 1 (A4): on the strip |kappa1+kappa2| <= kappa2/3 (kappa2>0, kappa1=-s<0),
#   rho(kappa1,kappa2) = (a1 a2/Jcal) sum_t c_t (2s)^{n1-1} (2kappa2)^{n2-1} / (prod_j (a1 - 2 i s A_j) prod_j (a2 - 2 i kappa2 A'_j)),
# claim |d rho/d kappa1| <= c_rho (lambda_A/a_min) min(1,(kappa*/kappa2)^2), kappa* = a_min/(4 lambda_A),
#       c_rho <= 50 (2 nbar - 1) mflat_A (a_max/a_min)^2 (lambda_A/mu_A)^2.
# The report gives only a one-line reason; this checks the stated constant on random multi-state NF jets.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
rng = np.random.default_rng(3)
worst = 0.0; worst_info = None
for trial in range(3000):
    lam = 1.0; mu = 10**rng.uniform(-2.5, np.log10(0.7))
    a1, a2 = 10**rng.uniform(-1, 1, size=2)
    nterms = rng.integers(1, 5); terms = []
    for t in range(nterms):
        n1 = 1 if t == 0 else rng.integers(1, 4); n2 = 1 if t == 0 else rng.integers(1, 4)
        A = -rng.uniform(mu, lam, size=n1); Ap = -rng.uniform(mu, lam, size=n2)
        c = (1.0 if t == 0 else rng.normal()*rng.uniform(0.05, 1)*mu**(n1 + n2 - 2))
        terms.append((c, A, Ap))
    J = sum(c for c, A, Ap in terms if len(A) == 1 and len(Ap) == 1)
    nbar = max(max(len(A), len(Ap)) for c, A, Ap in terms)
    mflat = sum(abs(c)*mu**(-(len(A) + len(Ap) - 2)) for c, A, Ap in terms)/abs(J)
    amin, amax = min(a1, a2), max(a1, a2)
    crho = 50*(2*nbar - 1)*mflat*(amax/amin)**2*(lam/mu)**2
    kstar = amin/(4*lam)
    def rho(s, k2):
        tot = 0
        for c, A, Ap in terms:
            v = c*(2*s)**(len(A) - 1)*(2*k2)**(len(Ap) - 1)
            for x in A: v /= (a1 - 2j*s*x)
            for x in Ap: v /= (a2 - 2j*k2*x)
            tot += v
        return tot*a1*a2/J
    for k2 in np.exp(np.linspace(np.log(1e-3*kstar), np.log(1e3*kstar), 60)):
        for s in np.linspace(2*k2/3, 4*k2/3, 7):
            h = 1e-6*s
            d = abs(rho(s + h, k2) - rho(s - h, k2))/(2*h)
            bound = crho*(lam/amin)*min(1, (kstar/k2)**2)
            r = d/bound
            if r > worst:
                worst, worst_info = r, (trial, k2/kstar, mu, nbar)
print(f"(A4) max |d rho/d kappa1| / [c_rho (lambda_A/a_min) min(1,(kappa*/kappa2)^2)] = {worst:.4f} over 3000 random jets "
      f"(<= 1 required); worst at kappa2/kappa* = {worst_info[1]:.3g}, mu/lambda = {worst_info[2]:.3g}, nbar = {worst_info[3]}")
