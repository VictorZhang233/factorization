# X1 fix round 2 -- check of the corrected L1(b)/L1'(b) error bound.
# Claims tested:
#  (Q)  closed-quadrant lemma: if all poles of a group lie in one closed quadrant (cone of opening pi/2),
#       then every race weight satisfies |w_pi| <= 1 (each factor |z_pi(m)| / |sum_{l>=m} z_pi(l)| <= 1).
#  (B)  corrected bound: |integral - prod R(0) sum_sigma w_sigma Jcal_sigma| / |prod R(0)|
#          <= N 2^{N+1} (lambda_J/kappa) sum_sigma M_sigma |w_sigma(z)|      (kappa >= 2 lambda_J)
#       for arbitrary complex poles; the old form without sum|w| fails (reviewer 2, chkA case (ii)).
#  (G)  Glauber case (real poles of one sign per group): sum_sigma |w_sigma| = 1, old and new bounds agree.
import sys, os, itertools, random, cmath, math
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
rng = np.random.default_rng(20261011)

def race_weights(z, final=True):
    """race weights for one group; final group: w_pi = prod z / prod_m sum_{l>=m} z_pi(l);
       initial group: w_pi = prod z / prod_m sum_{l<=m} z_pi(l)"""
    n = len(z); out = {}
    for pi in itertools.permutations(range(n)):
        num = np.prod([z[i] for i in pi]); den = 1
        for m in range(n):
            s = sum(z[pi[l]] for l in (range(m, n) if final else range(0, m + 1)))
            den *= s
        out[pi] = num/den
    return out

ok_Q = True; maxQ = 0
for trial in range(20000):
    n = rng.integers(2, 5)
    phi0 = rng.uniform(0, 2*np.pi)
    ang = phi0 + rng.uniform(0, np.pi/2, size=n)          # closed quadrant (cone of opening pi/2)
    rad = np.exp(rng.uniform(-3, 3, size=n))
    z = rad*np.exp(1j*ang)
    for fin in (True, False):
        w = race_weights(list(z), fin)
        m = max(abs(v) for v in w.values())
        maxQ = max(maxQ, m)
        if m > 1 + 1e-12: ok_Q = False
        s = sum(w.values())
        if abs(s - 1) > 1e-9: ok_Q = False
print(f"(Q) closed-quadrant lemma, 20000 random groups (n=2..4, both orientations): max |w_pi| = {maxQ:.6f};  sum w = 1 checked;  PASS={ok_Q}")

# counterexample to |w|<=1 outside a quadrant (opposite real parts), reviewer 2 chkA (ii)
z = [1 - 0.01j, -0.99 - 0.01j]
w = race_weights(z, True)
print(f"(Q') poles {z} (not in a closed quadrant): race weights {[complex(round(v.real,4),round(v.imag,4)) for v in w.values()]}, max|w| = {max(abs(v) for v in w.values()):.3f}")

# (B) N=2, single-state gaps, all sectors compatible with a given F/B assignment; random complex poles
def sector_list(Fset, Bset):
    """sectors: (initial order tuple, final order tuple)"""
    return [(pb, pf) for pb in itertools.permutations(Bset) for pf in itertools.permutations(Fset)]

def check_B(trials=20000, quadrant=False):
    worst_new = 0; worst_old = 0; viol_old = 0
    for t in range(trials):
        N = int(rng.integers(1, 4))
        lamJ = 1.0
        # poles: assign F (Im<0) or B (Im>0)
        types = rng.integers(0, 2, size=N)          # 1 = final
        z = []
        for e in range(N):
            if quadrant:
                ang = (rng.uniform(-np.pi/2, 0) if types[e] else rng.uniform(np.pi/2, np.pi))
            else:
                ang = (rng.uniform(-np.pi, 0) if types[e] else rng.uniform(0, np.pi))
            z.append(np.exp(rng.uniform(np.log(2.5), np.log(60)))*np.exp(1j*ang))
        Fset = [e for e in range(N) if types[e]]; Bset = [e for e in range(N) if not types[e]]
        r = [complex(rng.normal(), rng.normal()) for e in range(N)]
        tot_err = 0; tot_bound = 0; kappa = np.inf; sumw = 0; lead = 0; exact = 0
        pref = np.prod([(-1j*r[e]) if types[e] else (1j*r[e]) for e in range(N)])
        R0 = np.prod([r[e]/(-z[e]) for e in range(N)])
        secs = sector_list(Fset, Bset)
        data = []
        for (pb, pf) in secs:
            KB = [sum(z[pb[l2]] for l2 in range(l + 1)) for l in range(len(pb))]
            KF = [sum(z[pf[l2]] for l2 in range(l, len(pf))) for l in range(len(pf))]
            kappa = min([kappa] + [abs(k) for k in KB + KF])
            data.append((pb, pf, KB, KF))
        if kappa < 2*lamJ:
            continue
        for (pb, pf, KB, KF) in data:
            # random single-state gap energies |A| <= lamJ (initial A<0 real, final A'<0 real) and coefficient
            Ab = -rng.uniform(0, lamJ, size=len(KB)); Af = -rng.uniform(0, lamJ, size=len(KF))
            c = complex(rng.normal(), rng.normal())
            J = c*np.prod([1j/(Ab[l] + KB[l]) for l in range(len(KB))])*np.prod([1j/(Af[l] - KF[l]) for l in range(len(KF))])
            Jlead = c*np.prod([1/(-1j*k) for k in KB])*np.prod([1/(1j*k) for k in KF])
            wsig = (np.prod([z[e] for e in pf])/np.prod(KF) if KF else 1)*(np.prod([z[e] for e in pb])/np.prod(KB) if KB else 1)
            exact += pref*J; lead += R0*wsig*c
            sumw += abs(wsig)*abs(c)
        err = abs(exact - lead)/abs(R0)
        bound_new = N*2**(N + 1)*(lamJ/kappa)*sumw          # M_sigma = |c| here
        Mmax = sumw / max(1e-300, sum(abs((np.prod([z[e] for e in pf])/np.prod(KF) if KF else 1)*(np.prod([z[e] for e in pb])/np.prod(KB) if KB else 1)) for (pb, pf, KB, KF) in data))
        worst_new = max(worst_new, err/bound_new)
    return worst_new

wn = check_B(20000, quadrant=False)
print(f"(B) corrected bound N 2^(N+1) (lamJ/kappa) sum_sigma M_sigma|w_sigma|, 20000 random sectors, arbitrary complex poles, N<=3: max lhs/bound = {wn:.4f};  PASS={wn <= 1}")
wq = check_B(20000, quadrant=True)
print(f"(B) same, poles of each group in one closed quadrant: max lhs/bound = {wq:.4f};  PASS={wq <= 1}")

# (B') reviewer-2 counterexample: old bound fails, new bound holds
p1, p2 = 1.0 - 0.01j, -0.99 - 0.01j; A1 = A2 = -0.005; lamJ = 0.005
P = p1 + p2; kappa = min(abs(P), abs(p2))
exact = (-1j)*(-1j)*(1j/(A1 - P))*(1j/(A2 - p2)); R0 = (1/(-p1))*(1/(-p2)); w = p1/P
err = abs(exact - R0*w)/abs(R0)
old = 2*2**3*lamJ/kappa; new = old*abs(w)
print(f"(B') chkA case (ii): rel. error = {err:.4f}; old bound = {old:.4f} (holds: {err <= old}); corrected bound (x|w|={abs(w):.2f}) = {new:.3f} (holds: {err <= new})")

# (G) Glauber case: real poles, one sign per group -> sum|w| = 1
mx = 0
for t in range(5000):
    n = int(rng.integers(1, 5)); z = list(np.exp(rng.uniform(-3, 3, size=n)))
    for fin in (True, False):
        w = race_weights([x if fin else -x for x in z], fin)
        mx = max(mx, abs(sum(abs(v) for v in w.values()) - 1))
print(f"(G) real same-sign poles: |sum|w| - 1| <= {mx:.2e};  PASS={mx < 1e-12}")
print("ALL PASS" if (ok_Q and wn <= 1 and wq <= 1 and mx < 1e-12) else "SOME CHECK FAILED")
