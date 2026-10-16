"""
unitarity_cuts.py  --  Part (1) of research/c_glauber: the sum-over-cuts (unitarity) step of the
CSS/Collins Glauber argument, and what changes for non-abelian (two-gluon) exchange.

U1  Sum over the placements of the final-state cut through a chain of x^+-ordered (light-front) energy
    denominators a_f (amplitude 1/(a+i e), conjugate 1/(a-i e), cut 2 pi delta(a) ~ 2e/(a^2+e^2)).
    Exact finite-epsilon telescoping identity derived here, N=1..7:
        sum_c [prod_{f>c} 1/(a_f - i e)] 2e/(a_c^2+e^2) [prod_{f<c} 1/(a_f + i e)]
            = i prod_f 1/(a_f + i e) - i prod_f 1/(a_f - i e)
    (the opposite overall sign is checked to FAIL, as a guard against sign slips).  Consequence: after the
    integral over the total minus momentum flowing into the final state, the cut sum gives 1 for N=1 and 0
    for N>=2, i.e. final-state interactions cancel by unitarity (the mechanism used by CSS 1985/1988 and in
    Collins 2011 Ch.14; the exact equations there were NOT available to us, so no equation number is quoted).
U2  Aybat-Sterman (2009, arXiv:0811.0246v1) eq.(3)-(4) [text verified]: eikonal identity
    sum_{j=0}^n E_nj(q_1..q_n) = 0 (placements of the cut among the n gluons attached to an incoming Wilson
    line), and their 'causal identity' eq.(10)  sum_{a=0}^n prod_{k<=a} [-(q_1+..+q_k)]^{-1}
    prod_{l>a} [q_l+..+q_n]^{-1} = 0  (spectator attachments to initial vs final states).
U3  One-gluon spectator-spectator exchange (abelian): the two cut graphs (exchange left / right of the cut)
    are separately non-zero and differ point-by-point in the spectators' relative transverse momentum,
    but cancel after integrating over it (Collins-Qiu 2007, arXiv:0705.2141v2, Sec.III B and Fig.5(d,e);
    Rothstein-Stewart 2016, arXiv:1601.04695v3, eqs.(11.12)-(11.13)) [texts verified].
U4  Non-abelian: Glauber phase is a colour matrix U=exp(i chi c), c = T_A.T_B.  Unitarity U^+U=1 => inclusive
    (colour-traced, Delta p_T-integrated) cancellation; a projection on a colour configuration of the
    spectator system (as a rapidity-gap/diffractive condition does) is NOT preserved.
U5  Ladder vs crossed-ladder colour factors: X = L + (C_A/2) c for any pair of representations; the
    abelian eikonal identity 1/(-k+i0)+1/(k+i0) = -2 pi i delta(k).  [Rothstein-Stewart 2016, arXiv:1601.04695v3,
    Secs. 5.2.1, 9.1 (text verified): in the abelian theory box + crossed box combine at integrand level into
    delta(k^+)delta(k^-) and the iterations give the eikonal phase; 'in QCD the box and crossbox have different
    color factors, so this type of manipulation does not suffice'.  With their rapidity regulator every crossed
    Glauber diagram vanishes, the ladders exponentiate to exp(i phi(b)) with phi a Hermitian colour matrix
    (eqs.(9.1),(9.18),(9.19)), and the non-abelian part of the crossed-box topology sits in the soft region.]
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
from scipy import integrate, special

RESULTS = []
def check(name, ok, detail=''):
    RESULTS.append((name, bool(ok)))
    print(('PASS' if ok else 'FAIL') + '  ' + name + ('   [' + detail + ']' if detail else ''))

# ------------------------------------------------------------------------------------------------
print('=== U1: sum over final-state cut placements (telescoping identity) ===')
e = sp.symbols('epsilon', positive=True)
from fractions import Fraction
import random
def cutsum_exact(avals, eps, I):
    """exact evaluation with Gaussian rationals represented as sympy numbers"""
    N = len(avals)
    lhs = 0
    for c in range(N):
        term = 2*eps/(avals[c]**2 + eps**2)
        for f in range(c + 1, N):
            term *= 1/(avals[f] - I*eps)
        for f in range(c):
            term *= 1/(avals[f] + I*eps)
        lhs += term
    pm = 1; pp = 1
    for ai in avals:
        pm *= 1/(ai - I*eps); pp *= 1/(ai + I*eps)
    return sp.nsimplify(lhs), -I*pm + I*pp, I*pm - I*pp
for N in range(1, 8):
    if N <= 3:
        a = sp.symbols('a1:%d' % (N + 1), real=True)
        lhs, rhs_err, rhs_pr = cutsum_exact(list(a), e, sp.I)
        ok_err = sp.cancel(sp.together(lhs - rhs_err)) == 0
        ok_pr = sp.cancel(sp.together(lhs - rhs_pr)) == 0
        how = 'symbolic'
    else:
        random.seed(N)
        ok_err, ok_pr = True, True
        for trial in range(5):
            av = [sp.Rational(random.randint(-97, 97), random.randint(1, 13)) for _ in range(N)]
            ev = sp.Rational(random.randint(1, 50), random.randint(51, 400))
            lhs, rhs_err, rhs_pr = cutsum_exact(av, ev, sp.I)
            ok_err &= sp.simplify(sp.expand(lhs - rhs_err)) == 0
            ok_pr &= sp.simplify(sp.expand(lhs - rhs_pr)) == 0
        how = 'exact rationals, 5 random points'
    check('U1 N=%d (%s): cut-sum identity  = i(prod A - prod B)  holds exactly; opposite sign %s' % (N, how, 'holds (!)' if ok_pr else 'fails'),
          ok_err and not ok_pr)

# consequence: integrate over k_A^-.  a_f = E - d_f with E = P^- - k^- ; each product term has all its
# poles on one side when N>=2 (integrand ~ 1/E^N) -> integral 0; for N=1 the cut gives int dk/(2pi) 2 pi delta = 1.
def cut_sum(E, d, eps):
    N = len(d); af = [E - di for di in d]
    tot = 0j
    for c in range(N):
        t = 2*eps/(af[c]**2 + eps**2)
        for f in range(c + 1, N):
            t /= (af[f] - 1j*eps)
        for f in range(c):
            t /= (af[f] + 1j*eps)
        tot += t
    return tot
for d, label in [([0.3], 'N=1'), ([0.3, -0.5], 'N=2'), ([0.3, -0.5, 1.1], 'N=3'), ([0.2, -0.9, 0.7, 1.6], 'N=4')]:
    eps = 1e-3
    pts = sorted(d)
    def fr(E): return cut_sum(E, d, eps).real
    def fi(E): return cut_sum(E, d, eps).imag
    edges = [-2e3] + sum([[p - 1e-1, p - 1e-2, p - 1e-3, p, p + 1e-3, p + 1e-2, p + 1e-1] for p in pts], []) + [2e3]
    edges = sorted(set(edges))
    val = 0j
    for x0, x1 in zip(edges[:-1], edges[1:]):
        val += integrate.quad(fr, x0, x1, limit=2000)[0] + 1j*integrate.quad(fi, x0, x1, limit=2000)[0]
    val /= 2*np.pi
    target = 1.0 if len(d) == 1 else 0.0
    check('U1-int %s: int dk^-/(2 pi) [sum over cuts of F_T] = %d  (F_T -> 1 after the cut sum)' % (label, target),
          abs(val - target) < 3e-3, 'value=%.5f%+.5fi' % (val.real, val.imag))

# ------------------------------------------------------------------------------------------------
print('\n=== U2: Aybat-Sterman eikonal identity sum_j E_nj = 0 ===')
def eikonal_sum(qv):
    n = len(qv); tot = 0
    for j in range(0, n + 1):
        L = 1
        for k in range(1, j + 1):              # partial sums ending at j: q_k+...+q_j
            L *= 1/sum(qv[k - 1:j])
        R = 1
        for k in range(j + 1, n + 1):          # partial sums starting at j+1: q_{j+1}+...+q_k
            R *= 1/sum(qv[j:k])
        tot += (-1)**(n - j)*R*L
    return tot
for n in range(1, 8):
    if n <= 4:
        q = sp.symbols('q1:%d' % (n + 1), real=True)
        ok = sp.cancel(sp.together(eikonal_sum(list(q)))) == 0
        how = 'symbolic'
    else:
        random.seed(100 + n); ok = True
        for trial in range(20):
            qv = [Fraction(random.choice([-1, 1])*random.randint(1, 60), random.randint(1, 17)) for _ in range(n)]
            try:
                ok &= (eikonal_sum(qv) == 0)
            except ZeroDivisionError:
                pass
        how = 'exact rationals, 20 random points'
    check('U2 n=%d (%s): sum_{j=0}^{n} E_nj = 0 (cut placements among gluons on an incoming Wilson line)' % (n, how), ok)

def causal_sum(qv):
    n = len(qv); tot = 0
    for a in range(0, n + 1):
        L = 1
        for k in range(1, a + 1):
            L *= 1/(-sum(qv[:k]))
        R = 1
        for l in range(a + 1, n + 1):
            R *= 1/sum(qv[l - 1:])
        tot += L*R
    return tot
for n in range(1, 8):
    if n <= 4:
        q = sp.symbols('q1:%d' % (n + 1), real=True)
        ok = sp.cancel(sp.together(causal_sum(list(q)))) == 0
        how = 'symbolic'
    else:
        random.seed(300 + n); ok = True
        for trial in range(20):
            qv = [Fraction(random.choice([-1, 1])*random.randint(1, 60), random.randint(1, 17)) for _ in range(n)]
            try:
                ok &= (causal_sum(qv) == 0)
            except ZeroDivisionError:
                pass
        how = 'exact rationals, 20 random points'
    check('U2b n=%d (%s): Aybat-Sterman causal identity eq.(10) = 0' % (n, how), ok)

# ------------------------------------------------------------------------------------------------
print('\n=== U3: abelian one-gluon spectator-spectator exchange: cut graphs cancel only after the Delta p_T integral ===')
# Model (leading power, c_dy G-i'/Collins-Qiu): M1(Delta) = int d^2k/(2pi)^2 V(k) M0(Delta+k),  V(k) = -i g^2/(k^2+mg^2)
# (g^2 = g_A g_B).  Graph (c): M1 M0^*  ; graph (d): M0 M1^* .  Use a complex, non-symmetric toy M0.
g2, mg = 1.3, 0.6
def M0(D):
    x, y = D
    return np.exp(-0.5*(x - 0.3)**2 - 0.8*(y + 0.1)**2)*(1 + 0.7j*x - 0.4*y + 0.2j*x*y)
# grids: Delta-grid and k-grid with the SAME spacing h, so that the shift Delta -> Delta - k used in the
# unitarity argument is exact on the lattice; M0 is analytic (evaluated at shifted points directly).
h = 0.12
xs = np.arange(-7.2, 7.2 + 1e-9, h)            # Delta grid
ks = np.arange(-6.0, 6.0 + 1e-9, h)            # k grid (V(k) = V(-k) on this symmetric grid)
X, Y = np.meshgrid(xs, xs, indexing='ij')
KX, KY = np.meshgrid(ks, ks, indexing='ij')
Vk = -1j*g2/(KX**2 + KY**2 + mg**2)*h*h/(2*np.pi)**2
M0g = M0((X, Y))
M1g = np.zeros_like(M0g)
for p_ in range(len(ks)):
    for q_ in range(len(ks)):
        M1g += Vk[p_, q_]*M0((X + ks[p_], Y + ks[q_]))
gc = M1g*np.conj(M0g); gd = M0g*np.conj(M1g)
pointwise = np.max(np.abs(gc + gd))
integrated = np.sum(gc + gd)*h*h
scale = np.sum(np.abs(gc))*h*h
check('U3a graphs (c)+(d) do NOT cancel point by point in Delta p_T', pointwise > 1e-2*np.max(np.abs(gc)),
      'max|c+d|/max|c| = %.3f' % (pointwise/np.max(np.abs(gc))))
check('U3b graphs (c)+(d) cancel after integrating over Delta p_T (unitarity / sum over cuts)', abs(integrated) < 1e-10*scale + 1e-14,
      '|int(c+d)|=%.2e, int|c|=%.2e' % (abs(integrated), scale))
# b-space form: chi(b) = -(g^2/2pi) K0(mg b) ; Fourier transform int d^2k/(2pi)^2 e^{ik.b}/(k^2+m^2) = K0(m b)/(2 pi)
import mpmath as mp
mp.mp.dps = 25
for bb in [0.4, 1.5, 3.0]:
    f_ = lambda k: k*mp.besselj(0, k*bb)/(k**2 + mg**2)
    val = mp.quadosc(f_, [0, mp.inf], zeros=lambda n_: mp.besseljzero(0, n_)/bb)/(2*mp.pi)
    exact = mp.besselk(0, mg*bb)/(2*mp.pi)
    check('U3c FT: int d^2k/(2pi)^2 e^{ik.b}/(k^2+m^2) = K0(m b)/(2 pi)  at b=%.1f' % bb,
          abs(val - exact) < 1e-12, 'num=%s exact=%s' % (mp.nstr(val, 12), mp.nstr(exact, 12)))

# ------------------------------------------------------------------------------------------------
print('\n=== U4: non-abelian Glauber phase as a colour matrix ===')
def gellmann(N):
    """generators T^a = lambda^a/2 of SU(N), Tr(T^a T^b)=delta/2"""
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
N = 3
T = gellmann(N)
Tbar = [-t.T for t in T]            # antitriplet generators
I3 = np.eye(N)
def cdot(TA, TB):
    return sum(np.kron(a, b) for a, b in zip(TA, TB))
from scipy.linalg import expm
for name, TB in [('3 x 3', T), ('3 x 3bar', Tbar)]:
    c = cdot(T, TB)
    for chi in [0.37, -1.2]:
        U = expm(1j*chi*c)
        check('U4a [%s] chi=%+.2f: U = exp(i chi T_A.T_B) is unitary' % (name, chi), np.allclose(U.conj().T @ U, np.eye(N*N)))
        rng = np.random.default_rng(7)
        A = rng.normal(size=(N*N, N*N)) + 1j*rng.normal(size=(N*N, N*N)); rho = A @ A.conj().T; rho /= np.trace(rho)
        check('U4b [%s] chi=%+.2f: colour-traced (inclusive) probability unchanged: Tr[U rho U^+] = Tr rho' % (name, chi),
              abs(np.trace(U @ rho @ U.conj().T) - 1) < 1e-12)
    # projection onto the colour-singlet channel of the (3 x 3bar) pair, or the antitriplet channel of (3 x 3)
    if name == '3 x 3bar':
        s = np.zeros(N*N, complex)
        for i in range(N):
            s[i*N + i] = 1/np.sqrt(N)
        Pproj = np.outer(s, s.conj()); lab = 'singlet'
    else:
        # antisymmetric (3bar) projector in 3 x 3
        Sw = np.zeros((N*N, N*N))
        for i in range(N):
            for j in range(N):
                Sw[i*N + j, j*N + i] = 1
        Pproj = 0.5*(np.eye(N*N) - Sw); lab = 'antisymmetric (3bar)'
    # a state that is an eigenstate of the projector is invariant (c commutes with total colour) -> use a mixed state
    psi = np.zeros(N*N, complex); psi[0*N + 1] = 1.0          # |1> x |2>  (not a definite pair representation)
    rho = np.outer(psi, psi.conj())
    chi = 0.8
    U = expm(1j*chi*c)
    p0 = np.real(np.trace(Pproj @ rho)); p1 = np.real(np.trace(Pproj @ U @ rho @ U.conj().T))
    comm = np.linalg.norm(c @ Pproj - Pproj @ c)
    # c = T_A.T_B = (C_tot - C_A - C_B)/2 commutes with projectors on definite total colour: then probabilities ARE preserved.
    check('U4c [%s] T_A.T_B commutes with the projector on definite total colour of the pair (|[c,P]|=%.1e)' % (name, comm), comm < 1e-12)
    check('U4d [%s] hence the %s fraction of the spectator pair is unchanged (%.4f -> %.4f)' % (name, lab, p0, p1), abs(p0 - p1) < 1e-12)
# the non-trivial case: the selected configuration is defined in a basis that does NOT diagonalise c, e.g.
# "colour of spectator A alone" or a correlation with the colour flow to the hard part (3 lines).
# Three-line system: spectator A (3), spectator B (3bar), active parton system (3): Glauber acts on (A,B) only;
# condition: the A-remnant + active-parton system in a colour singlet ("colour-singlet exchange across the gap").
c3 = np.kron(cdot(T, Tbar), I3)
# singlet projector on (A, active) = particles 1 and 3:
s13 = np.zeros((N, N, N), complex)
for i in range(N):
    for j in range(N):
        s13[i, j, i] = (1/np.sqrt(N)) if True else 0
# P13 = sum_j |s>_{13} <s| x 1_2 : build as matrix on 1 x 2 x 3
P13 = np.zeros((N**3, N**3), complex)
for j in range(N):
    v = np.zeros((N, N, N), complex)
    for i in range(N):
        v[i, j, i] = 1/np.sqrt(N)
    v = v.reshape(-1)
    P13 += np.outer(v, v.conj())
# overall colour-singlet initial state of the three lines? use a generic state with definite structure:
rng = np.random.default_rng(11)
psi3 = rng.normal(size=N**3) + 1j*rng.normal(size=N**3); psi3 /= np.linalg.norm(psi3)
rho3 = np.outer(psi3, psi3.conj())
for chi in [0.5, 1.0, 2.0]:
    U3 = expm(1j*chi*c3)
    p0 = np.real(np.trace(P13 @ rho3)); p1 = np.real(np.trace(P13 @ U3 @ rho3 @ U3.conj().T))
    tot0 = np.real(np.trace(rho3)); tot1 = np.real(np.trace(U3 @ rho3 @ U3.conj().T))
    check('U4e chi=%.1f: inclusive (traced) probability preserved (%.6f -> %.6f) but the A-remnant/active-system singlet fraction changes (%.4f -> %.4f): "colour gap survival" != 1'
          % (chi, tot0, tot1, p0, p1), abs(tot1 - tot0) < 1e-12 and abs(p1 - p0) > 1e-3)

# ------------------------------------------------------------------------------------------------
print('\n=== U5: two-gluon exchange: ladder vs crossed ladder colour factors ===')
def adj_gens(N):
    Ts = gellmann(N); n = len(Ts)
    f = np.zeros((n, n, n))
    for a_ in range(n):
        for b_ in range(n):
            comm = Ts[a_] @ Ts[b_] - Ts[b_] @ Ts[a_]
            for c_ in range(n):
                f[a_, b_, c_] = np.real(-2j*np.trace(comm @ Ts[c_]))
    return [(-1j)*f[a_, :, :] for a_ in range(n)], f      # (T^a_adj)_{bc} = -i f^{abc}
for N in [2, 3, 4]:
    TF = gellmann(N); TA, f = adj_gens(N)
    CA = N
    for nm, R1, R2 in [('F x F', TF, TF), ('F x Fbar', TF, [-t.T for t in TF]), ('F x A', TF, TA), ('A x A', TA, TA)]:
        n = len(R1)
        Lcol = sum(np.kron(R1[a_] @ R1[b_], R2[a_] @ R2[b_]) for a_ in range(n) for b_ in range(n))
        Xcol = sum(np.kron(R1[a_] @ R1[b_], R2[b_] @ R2[a_]) for a_ in range(n) for b_ in range(n))
        c = sum(np.kron(R1[a_], R2[a_]) for a_ in range(n))
        ok = np.allclose(Xcol, Lcol + 0.5*CA*c) and np.allclose(Lcol, c @ c)
        check('U5a SU(%d) %s: ladder colour L = c^2 and crossed X = L + (C_A/2) c' % (N, nm), ok)
# abelian eikonal identity for ladder + crossed (line-2 factors) at fixed total k: 1/(-k+i0) + 1/(k+i0) = -2 pi i delta(k)
phi = lambda t: np.exp(-(t + 0.2)**2)*(1.0 + 0.3*t)
eps = 1e-3
val = 0j
for x0, x1 in [(-30, -0.1), (-0.1, -1e-3), (-1e-3, 0), (0, 1e-3), (1e-3, 0.1), (0.1, 30)]:
    fun = lambda t: phi(t)*(1/(-t + 1j*eps) + 1/(t + 1j*eps))
    val += integrate.quad(lambda t: fun(t).real, x0, x1, limit=1000)[0] + 1j*integrate.quad(lambda t: fun(t).imag, x0, x1, limit=1000)[0]
check('U5b ladder+crossed eikonal factors: 1/(-k+i0)+1/(k+i0) = -2 pi i delta(k) (abelian exponentiation)',
      abs(val + 2j*np.pi*phi(0)) < 1e-2, 'num=%s target=%s' % (val, -2j*np.pi*phi(0)))

print('\nSUMMARY: %d/%d PASS' % (sum(ok for _, ok in RESULTS), len(RESULTS)))
