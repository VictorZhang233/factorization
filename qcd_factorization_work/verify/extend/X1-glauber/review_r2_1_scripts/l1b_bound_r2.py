# Round-2 reviewer #1: random test of the corrected L1(b) bound
#   |J^(sigma)(z) - Jcal_sigma prod_l (-i K^B_l)^{-1} prod_l (i K^F_l)^{-1}|
#        <= N 2^{N+1} M_sigma (lambda_J/kappa) prod_l |K_l|^{-1},   M_sigma = sum_t |c_t| lambda_J^{-d_t},
# for random sectors (n initial, m final insertions, N = n + m), random multi-state gap functions
# (n_l factors i/(A + K) or i/(A' - K), |A| <= lambda_J), random complex z with kappa = min |K_l| >= 2 lambda_J.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
rng = np.random.default_rng(7)
worst = 0.0
for trial in range(20000):
    n = rng.integers(0, 3); m = rng.integers(0, 3)
    if n + m == 0:
        continue
    N = n + m
    lJ = 1.0
    # random z: initial group in UHP, final group in LHP (as for a contributing sector), scale >= few lambda_J
    scale = 10**rng.uniform(np.log10(2.0), 3)
    zb = (rng.normal(size=n) + 1j*np.abs(rng.normal(size=n)))*scale
    zf = (rng.normal(size=m) - 1j*np.abs(rng.normal(size=m)))*scale
    KB = np.cumsum(zb) if n else np.array([])
    KF = np.cumsum(zf[::-1])[::-1] if m else np.array([])
    Ks = np.concatenate([KB, KF])
    kappa = np.min(np.abs(Ks))
    if kappa < 2*lJ:
        continue
    nterms = rng.integers(1, 4)
    J = 0; Jcal = 0; M = 0
    for t in range(nterms):
        nl = rng.integers(1, 3, size=N)             # 1 or 2 factors per gap
        dt = int(np.sum(nl - 1))
        c = (rng.normal() + 1j*rng.normal())*lJ**dt
        val = c
        for l in range(N):
            for f in range(nl[l]):
                A = rng.uniform(-lJ, lJ)
                val *= (1j/(A + Ks[l])) if l < n else (1j/(A - Ks[l]))
        J += val
        M += abs(c)*lJ**(-dt)
        if dt == 0:
            Jcal += c
    lead = Jcal*np.prod([1/(-1j*k) for k in KB])*np.prod([1/(1j*k) for k in KF])
    lhs = abs(J - lead)
    bound = N*2**(N + 1)*M*(lJ/kappa)*np.prod(1/np.abs(Ks))
    worst = max(worst, lhs/bound)
print(f"max over 20000 random trials of lhs/bound = {worst:.4f}  ({'PASS' if worst <= 1 else 'FAIL'}: bound must be >= lhs)")
