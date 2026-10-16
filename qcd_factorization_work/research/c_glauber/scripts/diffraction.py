"""
diffraction.py  --  Part (3) of research/c_glauber: why Collins' proof of factorization for diffractive DIS
(Collins, PRD 57 (1998) 3051 [Erratum PRD 61 (2000) 019902], arXiv:hep-ph/9709499v2, Sec. III; text verified)
works, and why the same argument fails for hadron-hadron diffraction.

D1  Pole structure of a soft/Glauber gluon r attached to the target subgraph A (which contains BOTH initial-state
    lines -- incoming proton, active parton -- and final-state lines -- the detected p' / target-fragmentation
    system, which is NOT summed over because of the diffractive requirement):
      * r^- is trapped by A (poles on both sides, |r^-| ~ m^2/Q)  [so the inclusive-DIS argument, which sums over
        the cuts of A, is unavailable];
      * DDIS: the only r^+ poles near the Glauber region come from final-state current-jet lines (one side);
        A-collinear lines put their r^+ poles at |r^+| ~ Q  =>  r^+ can be deformed out of the Glauber region
        (Collins 1998 Sec. III D, Fig. 6);
      * hadron-hadron diffraction (second hadron B with its own spectators): B-collinear lines put r^+ poles near
        the origin on BOTH sides (initial-state active parton of B, final-state B remnant)  =>  pinch in r^- AND r^+
        (spectator-spectator Glauber pinch); the CSS way out (sum over all cuts of the spectator interactions) is
        blocked by the requirement on the A-fragmentation final state.
D2  Unitarity vs selection.  A Glauber exchange acts on the spectator systems as a unitary operator U(b).
      * inclusive (sum over all final states of the remnants): sum_f |<f|U|i>|^2 = 1 (cancellation);
      * diffractive selection (projector P on 'remnant intact / colour-singlet across the gap'):
        <i|U^+ P U|i> < <i|P|i>  ('gap survival' < 1).
    Toy: the diffracted hadron as a two-constituent colour-singlet dipole of size r at impact parameter b w.r.t. a
    B spectator; abelian: phases e^{i e chi(|b+r/2|)} e^{-i e chi(|b-r/2|)}; non-abelian: colour rotation
    exp(i chi_1 T_q.T_B + i chi_2 T_qbar.T_B) leaking singlet -> octet.  Survival -> 1 as r -> 0 (colour
    transparency), inclusive probability = 1 exactly.  [Bjorken, PRD 47 (1993) 101 introduced the 'survival
    probability of the rapidity gap' (abstract verified); the toy here is ours and is only an illustration.]
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from scipy import special, integrate
from scipy.linalg import expm

RESULTS = []
def check(name, ok, detail=''):
    RESULTS.append((name, bool(ok)))
    print(('PASS' if ok else 'FAIL') + '  ' + name + ('   [' + detail + ']' if detail else ''))

def vec(p, m, pT):
    pT = np.asarray(pT, float)
    return np.array([p, (m**2 + pT @ pT)/(2*p), pT[0], pT[1]])
def pole_kminus(l, s, k, M, eps=1e-9):
    lp = l[0] + s*k[0]; lT = l[2:] + s*k[2:]
    return (lT @ lT + M**2 - 2*lp*l[1] - 1j*eps)/(2*lp*s)
def pole_kplus(l, s, k, M, eps=1e-9):
    lm = l[1] + s*k[1]; lT = l[2:] + s*k[2:]
    return (lT @ lT + M**2 - 2*lm*l[0] - 1j*eps)/(2*lm*s)
half = lambda z: 'UHP' if z.imag > 0 else 'LHP'

# ------------------------------------------------------------------------------------------------
print('=== D1: pole structure, diffractive DIS vs hadron-hadron diffraction ===')
Q = 100.0; lam = 0.05; m = lam*Q
PA = vec(Q, m, [0, 0])
pprime = vec(0.9*Q, m, [0.6*m, -0.3*m])            # detected diffracted proton p' (x_P = 0.1), final state
la = PA - pprime                                    # 'pomeron' momentum entering the hard part (A-collinear)
r = np.array([0.3*m**2/Q, -0.5*m**2/Q, 0.7*m, 0.4*m])   # Glauber-scaled gluon momentum
# route: r flows from the other side (Y) into the A subgraph at p', back along A lines to H.
#   p' internal segment carries p' - r (s=-1); the A line into H carries la + r (s=+1).
A_lines_minus = [half(pole_kminus(pprime, -1, r, m)), half(pole_kminus(la, +1, r, m))]
check('D1a r^- is trapped by the target subgraph (detected p\' = final state, pomeron/active line = initial state)',
      len(set(A_lines_minus)) == 2, 'r^- poles %s' % A_lines_minus)
# r^+ poles of the A-collinear lines: far away (|r^+| ~ Q)
A_plus = [pole_kplus(pprime, -1, r, m), pole_kplus(la, +1, r, m)]
check('D1b A-collinear lines put their r^+ poles at |r^+| ~ Q (not in the Glauber region r^+ ~ m^2/Q)',
      min(abs(z.real) for z in A_plus) > 0.1*Q, 'Re r^+ = %s' % ['%.3g' % z.real for z in A_plus])
# DDIS: the other end of r is on a current-jet line (large minus momentum, final state): from H along the jet to Y.
pc = np.array([0.0, 0.6*Q, 0.5*m, -0.2*m]); pc[0] = (m**2 + pc[2]**2 + pc[3]**2)/(2*pc[1])
pc2 = np.array([0.0, 0.4*Q, -0.3*m, 0.6*m]); pc2[0] = (m**2 + pc2[2]**2 + pc2[3]**2)/(2*pc2[1])
J = pc + pc2                                         # jet parent (internal, final-state), splits into pc + pc2
DDIS_plus = [half(pole_kplus(J, +1, r, m)), half(pole_kplus(pc, +1, r, m))]
near = [abs(pole_kplus(J, +1, r, m).real), abs(pole_kplus(pc, +1, r, m).real)]
check('D1c DDIS: near the Glauber region r^+ meets only final-state (current-jet) poles, all on one side -> deformable',
      len(set(DDIS_plus)) == 1 and max(near) < 10*m**2/Q, 'jet r^+ poles %s at |Re| = %s (m^2/Q=%.2f)' % (DDIS_plus, ['%.3g' % x for x in near], m**2/Q))
# hadron-hadron diffraction: the other end of r on a B-spectator (final state) with the B active parton (initial state)
PB = np.array([m**2/(2*Q), Q, 0, 0])
pBp_T = np.array([-0.3*m, 0.5*m]); pBp = np.array([(m**2 + pBp_T @ pBp_T)/(2*0.55*Q), 0.55*Q, *pBp_T])
lb = PB - pBp
hh_plus = [half(pole_kplus(pBp, +1, r, m)), half(pole_kplus(lb, -1, r, m))]
nearB = [abs(pole_kplus(pBp, +1, r, m).real), abs(pole_kplus(lb, -1, r, m).real)]
check('D1d hadron-hadron diffraction: B spectator (final) and B active parton (initial) put r^+ poles on BOTH sides near the origin -> r^+ trapped too',
      len(set(hh_plus)) == 2 and max(nearB) < 10*m**2/Q, 'B r^+ poles %s at |Re| = %s' % (hh_plus, ['%.3g' % x for x in nearB]))
check('D1e => hadron-hadron diffraction: Glauber pinch in BOTH r^- and r^+ (no contour escape); DDIS: pinch in r^- only (escape via r^+)',
      len(set(A_lines_minus)) == 2 and len(set(hh_plus)) == 2 and len(set(DDIS_plus)) == 1)

# ------------------------------------------------------------------------------------------------
print('\n=== D2: unitarity vs diffractive selection (dipole toy) ===')
mg = 0.5; eAB = 1.2
chi = lambda b: -eAB*special.k0(mg*np.maximum(b, 1e-12))/(2*np.pi)
# abelian dipole: internal wavefunction psi(r_vec) Gaussian; after the exchange the internal state is multiplied
# by exp(i[chi(|b+r/2|) - chi(|b-r/2|)]) (constituent charges +e, -e); survival = |<psi|e^{i dphi}|psi>|^2.
def abelian_survival(bvec, R):
    # integrate over internal r_vec with |psi|^2 = exp(-r^2/R^2)/(pi R^2)
    def integrand(rr, th):
        rv = rr*np.array([np.cos(th), np.sin(th)])
        dphi = chi(np.linalg.norm(bvec + rv/2)) - chi(np.linalg.norm(bvec - rv/2))
        w = np.exp(-rr**2/R**2)/(np.pi*R**2)*rr
        return w*np.cos(dphi), w*np.sin(dphi)
    re = integrate.dblquad(lambda rr, th: integrand(rr, th)[0], 0, 2*np.pi, 0, 6*R, epsabs=1e-10)[0]
    im = integrate.dblquad(lambda rr, th: integrand(rr, th)[1], 0, 2*np.pi, 0, 6*R, epsabs=1e-10)[0]
    return re**2 + im**2
bvec = np.array([1.1, 0.0])
S_vals = {R: abelian_survival(bvec, R) for R in [0.05, 0.3, 1.0]}
check('D2a abelian dipole: probability to stay in the original internal state < 1 and -> 1 as the dipole size -> 0',
      S_vals[1.0] < S_vals[0.3] < S_vals[0.05] <= 1.0 and S_vals[0.05] > 0.999,
      'S(R=0.05,0.3,1.0) = %s' % ['%.5f' % v for v in S_vals.values()])
# inclusive = survival + break-up: expand e^{i dphi} psi in a complete orthonormal basis of internal states
# (2D Hermite functions with the width of psi) and sum |<n|e^{i dphi} psi>|^2 over n -> 1 (completeness / unitarity)
R = 1.0; ngrid = 161; xs = np.linspace(-6*R, 6*R, ngrid); dx = xs[1] - xs[0]
Xg, Yg = np.meshgrid(xs, xs, indexing='ij')
psi = np.exp(-(Xg**2 + Yg**2)/(2*R**2))/np.sqrt(np.pi*R**2)
dphi = chi(np.sqrt((bvec[0] + Xg/2)**2 + (bvec[1] + Yg/2)**2)) - chi(np.sqrt((bvec[0] - Xg/2)**2 + (bvec[1] - Yg/2)**2))
phi_out = np.exp(1j*dphi)*psi
from numpy.polynomial.hermite import hermval
from math import factorial
def h1(n, x):
    c = np.zeros(n + 1); c[n] = 1
    return hermval(x/R, c)*np.exp(-x**2/(2*R**2))/np.sqrt(2**n*factorial(n)*np.sqrt(np.pi)*R)
H = [h1(n, xs) for n in range(70)]
Hm = np.array(H)                                   # (n, x)
amps = Hm @ phi_out @ Hm.T * dx*dx                 # <n_x n_y | phi_out>
probs = np.abs(amps)**2
surv = probs[0, 0]
totals = [probs[:n, :n].sum() for n in (20, 40, 70)]
gridnorm = np.sum(np.abs(phi_out)**2)*dx*dx
check('D2b abelian dipole: survival (n=0) + break-up (n>0) over a complete internal basis -> 1 (unitarity); survival < 1',
      abs(gridnorm - 1) < 1e-10 and totals[0] < totals[1] < totals[2] and abs(1 - totals[2]) < 1e-4 and surv < 1 - 1e-4 and abs(surv - S_vals[1.0]) < 1e-4,
      'survival = %.6f (dblquad %.6f); partial sums n<20,40,70: %s; grid norm %.12f (deficit = basis truncation near the log singularities of chi)'
      % (surv, S_vals[1.0], ['%.8f' % t for t in totals], gridnorm))
# non-abelian: colour space (q: 3, qbar: 3bar, B spectator: 3); U = exp(i chi1 T_q.T_B + i chi2 T_qbar.T_B)
def gellmann(N):
    Ts = []
    for i in range(N):
        for j in range(i + 1, N):
            M = np.zeros((N, N), complex); M[i, j] = M[j, i] = 0.5; Ts.append(M)
            M = np.zeros((N, N), complex); M[i, j] = -0.5j; M[j, i] = 0.5j; Ts.append(M)
    for k in range(1, N):
        M = np.zeros((N, N), complex)
        for i in range(k):
            M[i, i] = 1.0
        M[k, k] = -k
        M *= 1.0/np.sqrt(2*k*(k + 1)); Ts.append(M)
    return Ts
T = gellmann(3); Tb = [-t.T for t in T]; I3 = np.eye(3)
cqB = sum(np.kron(np.kron(T[a], I3), T[a]) for a in range(8))
cqbB = sum(np.kron(np.kron(I3, Tb[a]), T[a]) for a in range(8))
# A-dipole singlet x B colour (density matrix: B unpolarized in colour)
sing = np.zeros((3, 3), complex)
for i in range(3):
    sing[i, i] = 1/np.sqrt(3)
Psing = np.kron(np.outer(sing.reshape(-1), sing.reshape(-1).conj()), I3)        # projector: A-dipole singlet, any B
rho0 = np.kron(np.outer(sing.reshape(-1), sing.reshape(-1).conj()), I3/3)
res = []
for (c1, c2) in [(0.4, 0.4), (0.4, 0.3), (0.4, 0.0), (1.5, -0.5)]:
    U = expm(1j*(c1*cqB + c2*cqbB))
    rho = U @ rho0 @ U.conj().T
    res.append((c1, c2, np.real(np.trace(rho)), np.real(np.trace(Psing @ rho))))
check('D2c non-abelian dipole: inclusive colour-summed probability = 1 for every exchange (unitarity)',
      all(abs(t - 1) < 1e-12 for _, _, t, _ in res))
check('D2d colour-singlet survival = 1 when both constituents see the same phase (zero size: T_q+T_qbar annihilates the singlet), < 1 otherwise',
      abs(res[0][3] - 1) < 1e-12 and all(p < 1 - 1e-6 for _, _, _, p in res[1:]),
      'P_singlet = %s' % ['%.5f' % p for _, _, _, p in res])
# leading behaviour for small phase difference d = chi1-chi2 at a common phase chi0: 1 - P ~ c d^2
for chi0 in [0.0, 0.4]:
    d_list = [0.02, 0.04, 0.08]
    leak = []
    for dd in d_list:
        U = expm(1j*((chi0 + dd)*cqB + chi0*cqbB))
        leak.append(1 - np.real(np.trace(Psing @ U @ rho0 @ U.conj().T)))
    ratios = [leak[i + 1]/leak[i] for i in range(2)]
    check('D2e chi0=%.1f: singlet -> octet leakage is quadratic in the phase difference (first non-trivial order = two-gluon/cut level)' % chi0,
          all(abs(rr - 4) < 0.05 for rr in ratios), 'leak = %s, ratios = %s' % (['%.3e' % x for x in leak], ['%.3f' % x for x in ratios]))
    if chi0 == 0.0:
        # exact second-order coefficient for U = exp(i d T_q.T_B), B unpolarized fundamental, A-dipole singlet:
        # 1 - P = d^2 [ <(T_q.T_B)^2> - <T_q.T_B P T_q.T_B> ] = d^2 C_F/(2N)   (since <s|T_q^a|s> = 0)
        N = 3; CF = (N*N - 1)/(2*N)
        check('D2f chi0=0: leakage coefficient = C_F/(2N) = (N^2-1)/(4N^2) = 2/9 for SU(3) (one constituent rotated)',
              abs(leak[0]/d_list[0]**2 - CF/(2*N)) < 0.01*CF/(2*N), 'coef num = %.5f, C_F/(2N) = %.5f' % (leak[0]/d_list[0]**2, CF/(2*N)))
print('\nSUMMARY: %d/%d PASS' % (sum(ok for _, ok in RESULTS), len(RESULTS)))
