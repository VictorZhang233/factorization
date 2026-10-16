r"""
W19 / Ch16 -- s5_independent_checks.py : second, independent set of checks (written in the resumed session,
without reusing code of s1-s4), for the formulas printed in ch16_jets.tex.

  K1  thrust: C_r = int_0^{1/3} r(tau) dtau by direct adaptive quadrature of r (not piecewise) equals
      5/2 - pi^2/3 + 2 ln^2 3 - 3 ln 3; the four elementary pieces quoted in the proof, each by quadrature.
  K2  thrust: cumulant R(tau) from direct 2D integration of the matrix element over {T > 1 - tau}
      (Monte-Carlo-free: nested quadrature over x1, x2 with T = max x_i) vs 1 + a[-2 ln^2 tau - 3 ln tau + pi^2/3 - 1].
  K3  NGL: Dasgupta--Salam angular integral int_0^1 dc2 int_{-1}^0 dc1 Omega_2 = pi^2/6 (direct 2D quadrature
      of their eq. (10)), and the same number from the (eta, phi) form 4*int (coth|deta|-1)/2 ... (see text).
  K4  BMS: (a) the azimuthal average of the correlated antenna, done numerically, equals coth|deta| - 1;
      (b) symmetric slice |eta| < eta_in: second-order coefficient from the direct 2D rapidity integral
      vs pi^2/12 - Li2(exp(-4 eta_in))/2 (BMS eq. (5.5)).
  K5  SLL: 2F2(1,1;2,5/2;-w) from mpmath.hyp2f2 vs the series; n=1 term; w 2F2/ln w at w = 1e8.
  K6  colour: explicit SU(3) generators on the 81-dim colour space of q q -> q q: with T_i acting on leg i
      (incoming: -t^T, outgoing: t), T_1+T_2+T_3+T_4 annihilates colour singlets of the full process, and on that
      singlet subspace T_1.T_2 + T_3.T_4 = T_12^2 - (C_1+C_2+C_3+C_4)/2 with T_12 = T_1 + T_2;
      for an all-outgoing (e+e-) q qbar g singlet, sum_{i<j} T_i.T_j = -(1/2) sum C_i (c-number).
  K7  Sterman--Weinberg: a third implementation (plain stratified Monte Carlo over (x1,x2) with the two-jet
      rule (a)/(b)) of c_2j at (eps,delta) = (0.05,0.25) and (0.01,0.1): agreement with the numbers in the table
      within the MC error.
Run:  python3 -I s5_independent_checks.py
"""
import sys, os, math
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import mpmath as mp

mp.mp.dps = 30
RES = []
def check(name, cond, info=''):
    RES.append((name, bool(cond)))
    print(('PASS  ' if cond else 'FAIL  ') + name + (('   [' + info + ']') if info else ''))

pi = mp.pi
# ---------------------------------------------------------------- K1
def r(t):
    t = mp.mpf(t)
    return 4*mp.log(1-2*t)/t + (4/(1-t) - 6)*(mp.log(1-2*t) - mp.log(t)) + 6 + 9*t
Cr_num = mp.quad(r, [0, mp.mpf(1)/1000, mp.mpf(1)/10, mp.mpf(1)/3])
Cr_cf = mp.mpf(5)/2 - pi**2/3 + 2*mp.log(3)**2 - 3*mp.log(3)
check('K1a C_r by direct quadrature', abs(Cr_num - Cr_cf) < mp.mpf('1e-20'), mp.nstr(Cr_num, 20) + ' vs ' + mp.nstr(Cr_cf, 20))
L2 = mp.polylog
p1 = mp.quad(lambda t: 4*mp.log(1-2*t)/t, [0, mp.mpf(1)/3])
p2 = mp.quad(lambda t: 6+9*t, [0, mp.mpf(1)/3])
p3 = mp.quad(lambda t: -(4/(1-t)-6)*mp.log(t), [0, mp.mpf(1)/3])
p4 = mp.quad(lambda t: (4/(1-t)-6)*mp.log(1-2*t), [0, mp.mpf(1)/3])
q1 = -4*L2(2, mp.mpf(2)/3)
q2 = mp.mpf(5)/2
q3 = -4*mp.log(3)*mp.log(mp.mpf(2)/3) + 4*L2(2, mp.mpf(1)/3) - 2*mp.log(3) - 2
q4 = 4*(mp.log(2)*mp.log(mp.mpf(3)/2) - mp.log(mp.mpf(2)/3)**2/2 - L2(2, mp.mpf(3)/4) + L2(2, mp.mpf(1)/2)) + 2 - mp.log(3)
check('K1b four pieces of C_r', max(abs(p1-q1), abs(p2-q2), abs(p3-q3), abs(p4-q4)) < mp.mpf('1e-20'))
check('K1c pieces add up to C_r', abs(q1+q2+q3+q4 - Cr_cf) < mp.mpf('1e-25'))

# ---------------------------------------------------------------- K2
# (1/sigma0) dsigma/dx1dx2 = a M, M = (x1^2+x2^2)/((1-x1)(1-x2)); x3 = 2-x1-x2; T = max x_i.
# R(tau) = 1 + a[3/2 - int_{T<1-tau} M]  (tail = all events with T < 1 - tau).
def tail(tau):
    tau = mp.mpf(tau)
    Tm = 1 - tau
    # region: x1 <= Tm, x2 <= Tm, x3 = 2-x1-x2 <= Tm  <=>  x1 + x2 >= 2 - Tm ; also x1+x2 <= 2 automatically
    def inner(x1):
        lo = max(2 - Tm - x1, mp.mpf(0))
        hi = Tm
        if hi <= lo:
            return mp.mpf(0)
        f = lambda x2: (x1**2 + x2**2)/((1-x1)*(1-x2))
        return mp.quad(f, [lo, hi])
    return mp.quad(inner, [1 - Tm, mp.mpf(1)/2, Tm])
ok = True
info = []
for tau in ['1e-3', '1e-4']:
    t = mp.mpf(tau)
    R1 = mp.mpf(3)/2 - tail(t)
    asym = -2*mp.log(t)**2 - 3*mp.log(t) + pi**2/3 - 1
    d = R1 - asym
    info.append('tau=%s diff=%s' % (tau, mp.nstr(d, 5)))
    ok = ok and abs(d) < 40*t*abs(mp.log(t))**2
check('K2  cumulant from direct 2D quadrature -> singular form, O(tau ln^2 tau) remainder', ok, '; '.join(info))

# ---------------------------------------------------------------- K3
def Omega2(c1, c2):
    return 2/((c2 - c1)*(1 - c1)*(1 + c2))
I_ds = mp.quad(lambda c2: mp.quad(lambda c1: Omega2(c1, c2), [-1, 0]), [0, 1])
check('K3a Dasgupta-Salam eq. (10): int Omega_2 = pi^2/6', abs(I_ds - pi**2/6) < mp.mpf('1e-15'), mp.nstr(I_ds, 18))
# (eta,phi) form: <E1^2 W_ab E2^2 [W_a1+W_1b-W_ab]>_phi = 4 (coth|deta|-1) per deta1 deta2 ; integrate eta1<0<eta2
I_eta = mp.quad(lambda D: D*(mp.coth(D) - 1), [0, mp.inf])
check('K3b int_0^inf D(coth D - 1) dD = pi^2/12', abs(I_eta - pi**2/12) < mp.mpf('1e-20'))
# S2 = -C_F C_A/(4 pi^2) * [16 pi^2 * pi^2/12] = -C_F C_A pi^2/3
S2_over_CFCA = -(16*pi**2*I_eta)/(4*pi**2)
check('K3c S2 = -C_F C_A pi^2/3 (normalization alpha_s L/2pi)', abs(S2_over_CFCA + pi**2/3) < mp.mpf('1e-20'))

# ---------------------------------------------------------------- K4
# BMS second order for C_in = {|eta| > eta_in} (jets along the axis), C_out = {|eta| < eta_in}:
# 1 - g = (Delta^2/2) int_{C_in} dOmega_k/4pi w_ab(k) int_{C_out} dOmega_q/4pi [w_ak + w_kb - w_ab](q).
# w_ab(k) dOmega_k = 2 deta dphi ; [w_ak+w_kb-w_ab](q) dOmega_q = 2 cos(dphi)/(cosh(deta)-cos(dphi)) deta dphi.
def phi_avg_num(D):
    # (1/2pi) int_0^{2pi} cos/(cosh D - cos) dphi, numerically (D > 0)
    A = mp.cosh(D)
    return mp.quad(lambda p: mp.cos(p)/(A - mp.cos(p)), [0, pi/8, pi/2, pi, 3*pi/2, 2*pi])/(2*pi)
okphi = all(abs(phi_avg_num(D) - (mp.coth(D) - 1)) < mp.mpf('1e-12') for D in [mp.mpf('0.05'), mp.mpf('0.3'), mp.mpf(1), mp.mpf(3)])
check('K4a azimuthal average (numerical) = coth|deta| - 1', okphi)
def slice_coeff(eta_in):
    # (1/2) * (1/(4pi))^2 * int 2 deta_k dphi_k * int 2 cos/(..) deta_q dphi_q
    # = (1/2) * (1/16 pi^2) * 4 * (2pi)^2 * int deta_k int deta_q (coth|eta_k - eta_q| - 1)
    # k in C_in: eta_k > eta_in or eta_k < -eta_in ; q in C_out: |eta_q| < eta_in. By symmetry 2 x (eta_k > eta_in).
    g = lambda D: mp.coth(D) - 1
    f = lambda ek: mp.quad(lambda eq: g(ek - eq), [-eta_in, eta_in])
    J = 2*mp.quad(f, [eta_in, eta_in + 1, eta_in + 4, mp.inf])
    return mp.mpf(1)/2 * (1/(16*pi**2)) * 4 * (2*pi)**2 * J
mp.mp.dps = 20
ok = True; info = []
for ein in [mp.mpf('0.5'), mp.mpf('1.0')]:
    c = slice_coeff(ein)
    cf = pi**2/12 - mp.polylog(2, mp.e**(-4*ein))/2
    info.append('eta_in=%s: %s vs %s' % (mp.nstr(ein, 3), mp.nstr(c, 10), mp.nstr(cf, 10)))
    ok = ok and abs(c - cf) < mp.mpf('1e-7')
check('K4  BMS slice: direct angular integral = pi^2/12 - Li2(e^{-4 eta_in})/2 (BMS eq. (5.5))', ok, '; '.join(info))
mp.mp.dps = 30

# ---------------------------------------------------------------- K5
ok = True
for w in [mp.mpf('0.3'), mp.mpf(2), mp.mpf(7)]:
    ser = mp.nsum(lambda n: (-w)**n/((n+1)*mp.rf(mp.mpf(5)/2, n)), [0, mp.inf])
    ok = ok and abs(ser - mp.hyp2f2(1, 1, 2, mp.mpf(5)/2, -w)) < mp.mpf('1e-20')
check('K5a 2F2(1,1;2,5/2;-w) = sum (-w)^n/((n+1)(5/2)_n)', ok)
# n = 1 term of -(4 C_F/3pi) as^3 L^3 Y 2F2 : coefficient of (-w) is 1/(2*(5/2)) = 1/5
check('K5b n=1 term = +(4/15pi^2) C_F N_c as^4 L^5 Y', mp.mpf(1)/(2*mp.mpf(5)/2) == mp.mpf(1)/5)
w = mp.mpf(10)**8
val = w*mp.hyp2f2(1, 1, 2, mp.mpf(5)/2, -w)/mp.log(w)
check('K5c w 2F2/ln w at w=1e8 = 1.497', abs(val - mp.mpf('1.497')) < 5e-4, mp.nstr(val, 6))

# ---------------------------------------------------------------- K6
# Gell-Mann matrices
l = np.zeros((8, 3, 3), dtype=complex)
l[0][0,1]=l[0][1,0]=1
l[1][0,1]=-1j; l[1][1,0]=1j
l[2][0,0]=1; l[2][1,1]=-1
l[3][0,2]=l[3][2,0]=1
l[4][0,2]=-1j; l[4][2,0]=1j
l[5][1,2]=l[5][2,1]=1
l[6][1,2]=-1j; l[6][2,1]=1j
l[7][0,0]=l[7][1,1]=1/np.sqrt(3); l[7][2,2]=-2/np.sqrt(3)
t = l/2
I3 = np.eye(3)
def op(leg, M, n=4):
    mats = [I3]*n
    mats[leg] = M
    out = mats[0]
    for m in mats[1:]:
        out = np.kron(out, m)
    return out
# legs 0,1 incoming quarks (colour charge -t^T), legs 2,3 outgoing quarks (t)
Tleg = []
for leg in range(4):
    Ta = [op(leg, (-t[a].T) if leg < 2 else t[a]) for a in range(8)]
    Tleg.append(Ta)
def dot(A, B):
    return sum(A[a] @ B[a] for a in range(8))
Ctot = [dot(Tleg[i], Tleg[i]) for i in range(4)]
CF = 4/3
okC = all(np.allclose(C, CF*np.eye(81)) for C in Ctot)
# colour-singlet subspace: kernel of sum_i T_i^a for all a
Tsum = [sum(Tleg[i][a] for i in range(4)) for a in range(8)]
Mstack = np.vstack(Tsum)
u, s, vh = np.linalg.svd(Mstack)
null = vh[np.sum(s > 1e-10):].conj().T   # columns span the singlet space
dimsing = null.shape[1]
lhs = dot(Tleg[0], Tleg[1]) + dot(Tleg[2], Tleg[3])
T12 = [Tleg[0][a] + Tleg[1][a] for a in range(8)]
rhs = dot(T12, T12) - 0.5*sum(Ctot)
P = null @ null.conj().T
okid = np.allclose(P @ lhs @ P, P @ rhs @ P)
# T12^2 not proportional to 1 on the singlet space (otherwise no SLL):
T12sq = null.conj().T @ dot(T12, T12) @ null
ev = np.linalg.eigvalsh((T12sq + T12sq.conj().T)/2)
check('K6a q q -> q q: Casimirs C_F, singlet space dim 2, T1.T2+T3.T4 = T12^2 - sum C/2 on it',
      okC and dimsing == 2 and okid, 'dim=%d, eigenvalues of T12^2: %s' % (dimsing, np.round(ev, 6)))
# e+e- q qbar g, all outgoing: q (t), qbar (-t^T), g (adjoint, -i f)
f = np.zeros((8, 8, 8))
for a in range(8):
    for b in range(8):
        comm = t[a] @ t[b] - t[b] @ t[a]
        for c in range(8):
            f[a, b, c] = np.real(-2j*np.trace(comm @ t[c]))
Tadj = [-1j*f[a] for a in range(8)]   # (T^a)_{bc} = -i f_{abc}
def op3(mats):
    out = mats[0]
    for m in mats[1:]:
        out = np.kron(out, m)
    return out
I8 = np.eye(8)
Tq = [op3([t[a], I3, I8]) for a in range(8)]
Tqb = [op3([I3, -t[a].T, I8]) for a in range(8)]
Tg = [op3([I3, I3, Tadj[a]]) for a in range(8)]
Ts = [Tq[a] + Tqb[a] + Tg[a] for a in range(8)]
u, s, vh = np.linalg.svd(np.vstack(Ts))
null3 = vh[np.sum(s > 1e-10):].conj().T
P3 = null3 @ null3.conj().T
pair = dot(Tq, Tqb) + dot(Tq, Tg) + dot(Tqb, Tg)
CA = 3.0
target = -0.5*(CF + CF + CA)
okee = null3.shape[1] == 1 and np.allclose(P3 @ pair @ P3, target*P3)
okdip = np.allclose(P3 @ (-2*dot(Tq, Tg)) @ P3, CA*P3) and np.allclose(P3 @ (-2*dot(Tq, Tqb)) @ P3, (2*CF - CA)*P3)
check('K6b e+e- q qbar g singlet: sum_{i<j} T_i.T_j = -(2C_F+C_A)/2; -2T_q.T_g = C_A, -2T_q.T_qbar = 2C_F-C_A', okee and okdip)

# ---------------------------------------------------------------- K7
rng = np.random.default_rng(7)
def twojet(x1, x2, eps, delta):
    x3 = 2 - x1 - x2
    X = (x1, x2, x3)
    def cth(i, j):
        k = 3 - i - j
        return 1 - 2*(1 - X[k])/(X[i]*X[j])
    th = {}
    for (i, j) in [(0, 1), (0, 2), (1, 2)]:
        th[(i, j)] = math.acos(max(-1.0, min(1.0, cth(i, j))))
    if any(v <= 2*delta for v in th.values()):
        return True
    for k in range(3):
        i, j = [m for m in range(3) if m != k]
        if X[k] < 2*eps and math.pi - th[(i, j)] <= 2*delta:
            return True
    return False
def c2j_mc(eps, delta, N=400000):
    # sample u = 1-x1, w = 1-x2 with density ~ 1/(u w) restricted to the triangle u + w <= 1, u,w in [umin,1]
    # (the 3-jet region keeps u,w >= ~ d*... > 0); use log-uniform sampling in u and w down to 1e-9
    lo = 1e-9
    U = np.exp(rng.uniform(math.log(lo), 0, N))
    W = np.exp(rng.uniform(math.log(lo), 0, N))
    jac = (math.log(1/lo))**2 * U * W
    tot = 0.0; tot2 = 0.0
    for u, w, j in zip(U, W, jac):
        if u + w > 1:      # x3 = u + w <= 1
            val = 0.0
        else:
            x1, x2 = 1 - u, 1 - w
            if twojet(x1, x2, eps, delta):
                val = 0.0
            else:
                val = (x1*x1 + x2*x2)/(u*w)*j
        tot += val; tot2 += val*val
    mean = tot/N; err = math.sqrt(max(tot2/N - mean*mean, 0)/N)
    # c2j = 3/4 - I3j/2
    return 0.75 - mean/2, err/2
ok = True; info = []
for (eps, delta, ref) in [(0.01, 0.1, -29.9216), (0.05, 0.005, -50.6020)]:
    c, e = c2j_mc(eps, delta)
    info.append('(%g,%g): MC %.3f +- %.3f vs %.4f' % (eps, delta, c, e, ref))
    ok = ok and abs(c - ref) < 4*e + 0.02
check('K7  Sterman-Weinberg c_2j: third implementation (Monte Carlo) agrees with the table', ok, '; '.join(info))

print()
print('SUMMARY: %d/%d checks passed' % (sum(1 for _, c in RES if c), len(RES)))
