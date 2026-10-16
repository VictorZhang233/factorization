# R-M25: spectral assumption (W2) of the reference (Ass. C.56, p. 118) and what Lemma C.64 actually uses.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

# (1) Lemma C.64 uses (W2) only through: Fourier support of the commutator in (P +- q)^2 >= M^2  <=>  |omega| >= 1
M, Q2, Pq = sp.symbols('M Q2 Pq', positive=True)
omega = 2*Pq/Q2
s_plus = M**2 + 2*Pq - Q2          # (P+q)^2 with q^2 = -Q2, P^2 = M^2
s_minus = M**2 - 2*Pq - Q2         # (P-q)^2
print('(P+q)^2 - M^2 =', sp.factor(s_plus - M**2), '= Q2*(omega - 1)  ->', sp.simplify(s_plus - M**2 - Q2*(omega - 1)) == 0)
print('(P-q)^2 - M^2 =', sp.factor(s_minus - M**2), '= -Q2*(omega + 1) ->', sp.simplify(s_minus - M**2 + Q2*(omega + 1)) == 0)
print('=> only the lower bound spec subset {p^2 >= M^2} (in the sector reached from |P> by J) is needed; no gap M1 > M is used.')

# (2) physical masses (PDG, MeV): both nucleons lie below the lowest N pi threshold in the baryon-number-1 sector
Mp, Mn = 938.27209, 939.56542
mpi0, mpic = 134.9768, 139.57039
thr = {'p pi0': Mp + mpi0, 'n pi+': Mn + mpic, 'n pi0': Mn + mpi0, 'p pi-': Mp + mpic}
print('M_p = %.3f, M_n = %.3f, M_n - M_p = %.3f MeV' % (Mp, Mn, Mn - Mp))
for k, v in sorted(thr.items(), key=lambda x: x[1]):
    print('  threshold %-6s = %.3f MeV' % (k, v))
print('lowest B=1 continuum threshold = %.3f MeV > M_n = %.3f MeV: both p and n are discrete states below it.' % (min(thr.values()), Mn))
print('=> in the B=1 sector there are two one-particle masses below the continuum; for a NEUTRON target M = M_n is not the lowest')
print('   mass of the B=1 sector (M_p < M_n), so (W2) as stated fails; in the target-flavour sector (N_u,N_d)=(1,2) it holds.')
print('   With QED the massless photon gives N+gamma states with invariant mass from M_N upwards: no isolation in any sector.')

# (3) chiral limit: threshold M + m_pi -> M
mpi = sp.symbols('m_pi', nonnegative=True)
MN = sp.symbols('M_N', positive=True)
print('chiral limit: lim_{m_pi->0} (M_N + m_pi) =', sp.limit(MN + mpi, mpi, 0), ' -> no M1 > M_N with spec in {M_N^2} U {p^2 >= M1^2}.')
# explicit: invariant mass of N + massless pion, N at rest, pion momentum k:  s = M^2 + 2 M k  takes every value >= M^2
k = sp.symbols('k', nonnegative=True)
s = (MN + k)**2 - k**2
print('s(N at rest + massless pion of momentum k) =', sp.expand(s), ' ; range [M_N^2, oo) as k ranges over [0, oo)')
