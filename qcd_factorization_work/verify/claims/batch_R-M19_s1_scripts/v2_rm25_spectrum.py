# R-M25 (independent check, verifier s1 v2)
# Reference Ass. C.56 (W2): baryon-number-1 spectrum in {p^2 = M^2} U {p^2 >= M1^2}, M1 > M, M = lowest mass (nucleon), isolated.
# Lemma C.64 uses (W2) only via: FT of <P|[J(z),J(0)]|P> vanishes unless (P +- q)^2 >= M^2  <=>  |omega| >= 1.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

M, Q2, Pq, mpi, k = sp.symbols('M Q2 Pq m_pi k', positive=True)
omega = 2 * Pq / Q2
sp_plus = M**2 + 2 * Pq - Q2      # (P+q)^2 with P^2 = M^2, q^2 = -Q2
sp_minus = M**2 - 2 * Pq - Q2     # (P-q)^2
print('(P+q)^2 - M^2 - Q2*(omega-1) =', sp.simplify(sp_plus - M**2 - Q2 * (omega - 1)))
print('(P-q)^2 - M^2 + Q2*(omega+1) =', sp.simplify(sp_minus - M**2 + Q2 * (omega + 1)))
print('=> support of Disc T: omega >= 1 (s-channel, incl. elastic point omega = 1) and omega <= -1 (u-channel):')
print('   only the LOWER BOUND spec subset {p^2 >= M^2} in the sector reached by J|P> is used; no gap M1 > M enters.')

# chiral limit: N at rest + pion of momentum k:  s(k) = (sqrt(M^2+k^2) + sqrt(m_pi^2+k^2))^2 - 0
s = (sp.sqrt(M**2 + k**2) + sp.sqrt(mpi**2 + k**2))**2
print('threshold s(k=0) =', sp.simplify(s.subs(k, 0)), ' ; chiral limit m_pi -> 0: s(k) =', sp.simplify(s.subs(mpi, 0)),
      '-> s(0) =', sp.simplify(s.subs(mpi, 0).subs(k, 0)), ' (continuum starts AT M^2: no isolation)')

# physical masses (PDG 2024, MeV)
Mp, Mn, mpi0, mpic = 938.27209, 939.56542, 134.9768, 139.57039
thr = sorted([('p pi0', Mp + mpi0), ('n pi0', Mn + mpi0), ('p pi-', Mp + mpic), ('n pi+', Mn + mpic)], key=lambda x: x[1])
print('M_p = %.5f, M_n = %.5f, M_n - M_p = %.5f MeV' % (Mp, Mn, Mn - Mp))
for nm, v in thr:
    print('   N pi threshold %-6s : %.4f MeV' % (nm, v))
print('=> both p and n lie below the lowest B=1 continuum threshold (%.2f MeV): with isospin breaking the B=1 sector has TWO'
      % thr[0][1])
print('   discrete masses; (W2) with M = target mass fails for a neutron target (M_p < M_n is in the B=1 spectrum).')
print('   In the sector with the target flavour numbers (J conserves each quark flavour) the lower bound p^2 >= M_target^2 holds.')
print('   With dynamical QED: massless photon -> N gamma states with s from M_N^2 upward: no isolation in any sector.')
