# X1 final2 -- numerical test of the revised T2'(a) and T2'(b) (fully coincident SS pair, M_glob, O(g^4)).
#
# The revised proof of T2'(a) (class-X_1 k^+ regulator) uses neither N_A nor (REAL) for J_A: the -1/2 of the outer
# strips comes from the ray identity applied to the REGULATOR psi(k) = chi_+(k) chi_-(-k) alone, and the A-jet enters
# only through |rho_12(i kappa) - 1| <= 4 m_A lambda_A kappa/a_min (A3) and |rho| <= mflat_A (A2).
# The revised T2'(b) states, without (REAL) for J_A and without N_A:
#     Re X -> Pi := 1/2 + (1/2pi) int_0^inf (dkappa/kappa) Im[rho_12(i kappa) + rho_21(i kappa)],
# with X := p_opp N/N_0 (and Re p_opp -> Pi as well).  This script tests both claims on a GENERAL (non-factorized)
# jet pair: J_B of class (SEC)+(EQ)+(ADJ)+(REAL)+N_B (reviewer-1 generator), and J_A of class (SEC)+(EQ) only,
# made to violate N_A (positive final energies in the mixed sectors 1V2, 2V1) and (REAL) (complex phases on the
# multi-state terms).  Integrator and jet code: review_r3_1_scripts/{t2_general,genjet}.py (imported, not modified).
# Regulator: chi(k) = 1/(1+k/K_c) (k>0), 1/(1-k/K_c) (k<0); on the rotated contour chihat(kappa) = 1/(1+i|kappa|/K_c).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, '..', 'review_r3_1_scripts'))
import numpy as np
from genjet import random_general_jet, check_spprime, check_R, SECTORS
from t2_general import hfun, ffun, integrate, scaled, gl

out = []
def log(s=''):
    print(s, flush=True); out.append(s)

rng = np.random.default_rng(20261014)
# ---- jet B: (SEC)+(EQ)+(ADJ)+(REAL)+N_B ----
while True:
    jB = random_general_jet(rng, 10**rng.uniform(-1.3, -0.7), n_orbit=2, n_wind=1, n_chain=4, n_iso=2, phase=1j)
    if abs(jB.Jcal('BB')) > 0.3 and check_spprime(jB):
        break
lamB, muB = jB.lam_mu(); JcB = jB.Jcal('BB')
# ---- jet A: start from a general jet, then break N_A and (REAL) while keeping (SEC), (EQ) ----
while True:
    jA0 = random_general_jet(rng, 10**rng.uniform(-1.3, -0.7), n_orbit=2, n_wind=1, n_chain=3, n_iso=2, phase=1j)
    if abs(jA0.Jcal('BB')) > 0.3:
        break
nflip = 0
for s in ('BF', 'BFp'):                         # mixed sectors: final gap = gap 2
    for idx, (c, g1, g2) in enumerate(jA0.terms[s]):
        if len(g2) == 1 and nflip < 3 and rng.uniform() < 0.7:
            jA0.terms[s][idx] = (c, g1, [abs(g2[0])])  # positive final energy (violates N_A)
            nflip += 1
for s in SECTORS:                               # complex phases on multi-state terms (violates (REAL), keeps (EQ))
    jA0.terms[s] = [((c*np.exp(0.9j) if (len(g1) + len(g2) > 2) else c), g1, g2) for (c, g1, g2) in jA0.terms[s]]
Jsec = [jA0.Jcal(s) for s in SECTORS]
eqA = max(abs(x - Jsec[0]) for x in Jsec)/abs(Jsec[0])
posA = sum(1 for s in ('BF', 'BFp') for (c, g1, g2) in jA0.terms[s] for A in g2 if A > 0)
log(f"J_B: (ADJ)={check_spprime(jB)}, (REAL)-violation={check_R(jB):.1e}, lam_B={lamB:.3f}, mu_B={muB:.3f}, "
    f"final energies all negative: {all(A < 0 for s in SECTORS for (c, g1, g2) in jB.terms[s] for A in g1 + g2)}")
log(f"J_A: (EQ) spread of Jcal_sigma over the six sectors = {eqA:.1e};  positive final energies in 1V2/2V1: {posA};  "
    f"(REAL)-violation = {check_R(jA0):.2f};  (ADJ) = {check_spprime(jA0)}")

a1, a2 = 0.9, 1.3; a = np.sqrt(a1*a2); amin = min(a1, a2)

def chihat(k, Kc):
    return 1.0/(1.0 + 1j*np.abs(k)/Kc)

def run(jA, Kc, n):
    """X(piA,piB) := I(piA,piB)/N_0 = -(1/Jcal_B) int h_piA f_piB Xi d^2kappa/(2pi)^2  (Xi = 1 if Kc is None)"""
    lamA, muA = jA.lam_mu()
    reg = (lambda k1, k2: 1.0) if Kc is None else (lambda k1, k2: chihat(k1, Kc)*chihat(k2, Kc))
    X = {}
    for cA in ('12', '21'):
        for cB in ('12', '21'):
            fun = lambda k1, k2, q, cA=cA, cB=cB: hfun(jA, a1, a2, cA, q, k1, k2)*ffun(jB, cB, k1, k2)*reg(k1, k2)
            X[(cA, cB)] = -integrate(fun, muB, np.log(muB) - 14, np.log(a/lamA) + 12, n, n, n)/(2*np.pi)**2/JcB
    Y = sum(X.values()); Xo = X[('12', '21')] + X[('21', '12')]
    return Xo, Y, Xo/Y

def Pi_value(jA):
    """Pi := 1/2 + (1/2pi) int_0^inf dkappa/kappa Im[rho_12(i kappa) + rho_21(i kappa)]  (imaginary axis only)"""
    lamA, muA = jA.lam_mu()
    t, w = gl(6000, np.log(muA*1e-6) + np.log(a/lamA) - 30, np.log(a/lamA) + 30)
    kap = np.exp(t)
    r12 = hfun(jA, a1, a2, '12', (-1, 1), -kap, kap)
    r21 = hfun(jA, a1, a2, '21', (1, -1), kap, -kap)
    return 0.5 + np.sum(w*(r12 + r21).imag)/(2*np.pi), abs(r12[0] - 1) + abs(r21[0] - 1)

ok = True
rows = []
for sA in (1e-2, 1e-3, 1e-4):
    jA = scaled(jA0, sA)
    lamA, muA = jA.lam_mu(); eps = lamA*lamB/a
    Pi, small = Pi_value(jA)
    Kc = np.sqrt(lamB*amin/lamA)                   # geometric mean: eta^2 = lam_B/K_c, zeta = lam_A K_c/a_min
    eta = np.sqrt(lamB/Kc); zeta = lamA*Kc/amin
    n = 1200 if sA > 1e-4 else 1600
    Xu, Yu, pu = run(jA, None, n)
    Xr, Yr, pr = run(jA, Kc, n)
    rows.append((eps, Pi, Xu, Yu, pu, Xr, Yr, pr, eta, zeta))
    log(f"eps={eps:.2e}  (lam_A={lamA:.2e}, mu_A={muA:.2e});  Pi = {Pi:+.6f}  (rho(0)-1 check {small:.1e})")
    log(f"    unregulated : Re X = {Xu.real:+.6f}  Re p_opp = {pu.real:+.6f}  Im p_opp = {pu.imag:+.4f}  |Y-1| = {abs(Yu - 1):.2e}"
        f"   Re X - Pi = {Xu.real - Pi:+.2e}")
    log(f"    class-X K_c={Kc:.3e} (eta={eta:.3f}, zeta={zeta:.2e}): Re X^chi = {Xr.real:+.3e}  Re p^chi_opp = {pr.real:+.3e}"
        f"  Im p^chi_opp = {pr.imag:+.4f}  |Y^chi-1| = {abs(Yr - 1):.2e}")
# convergence of the smallest-eps regulated point with a finer grid
jA = scaled(jA0, 1e-4); lamA, muA = jA.lam_mu(); Kc = np.sqrt(lamB*amin/lamA)
Xr2, Yr2, pr2 = run(jA, Kc, 2000)
log(f"grid check (eps={rows[-1][0]:.2e}, n=2000): Re X^chi = {Xr2.real:+.3e}, Re p^chi_opp = {pr2.real:+.3e} "
    f"(n=1600: {rows[-1][5].real:+.3e}, {rows[-1][7].real:+.3e})")
# assessments
dPi = [abs(r[2].real - r[1]) for r in rows]
reXr = [abs(r[5].real) for r in rows]; repr_ = [abs(r[7].real) for r in rows]
log(f"|Re X - Pi| (unregulated) = {', '.join(f'{d:.2e}' for d in dPi)}  (decreasing: {dPi[0] > dPi[1] > dPi[2]});  "
    f"Pi stays O(1): {', '.join(f'{r[1]:+.4f}' for r in rows)}")
log(f"|Re X^chi| = {', '.join(f'{v:.2e}' for v in reXr)};  |Re p^chi_opp| = {', '.join(f'{v:.2e}' for v in repr_)}  "
    f"(decreasing: {reXr[0] > reXr[1] > reXr[2] and repr_[0] > repr_[1] > repr_[2]})")
ok &= dPi[0] > dPi[1] > dPi[2] and reXr[0] > reXr[1] > reXr[2] and repr_[0] > repr_[1] > repr_[2]
ok &= abs(rows[-1][1]) > 10*max(dPi[-1], reXr[-1])      # the end-pole value is not small, the regulated one is
ok &= abs(Xr2.real - rows[-1][5].real) < 0.1*abs(rows[-1][5].real) + 1e-6
log("ALL PASS" if ok else "SOME CHECK FAILED")
with open(os.path.join(here, '..', 'final2_logs', 't2p_general_regulated.log'), 'w') as f:
    f.write('\n'.join(out) + '\n')
