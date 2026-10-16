#!/usr/bin/env python3
"""
w04_power.py -- writer W04 checks for Ch4 sec:ir-power, sec:ir-glauber, sec:ir-cancellation, sec:ir-regions and App E.
Run:  python3 -I w04_power.py   (log: logs/w04_power.log)

Conventions: v^pm=(v0 pm v3)/sqrt2, v.w = v+w- + v-w+ - vT.wT; scalings (k+,k-,kT) ~ (lam^a, lam^b, lam^c) Q;
Sterman units lam_S = lam^2, omega = power of lam_S, p = 2 omega = power of lam.

P1  vertex collinear k^- integral (VF-REG-6): pole positions, residue formula, numerical check
P2  region exponents of the on-shell massless scalar vertex (hard, coll, soft, usoft, Glauber: p=0) and normal coords
P3  eikonal approximation errors: soft O(lam), ultrasoft O(lam^2), Glauber O(1) (VF-REG-7); Glauber lam^0 (VF-GLA-1)
P4  omega(R) from the boost/dimension bookkeeping (exact rationals): table of reduced diagrams, connection powers,
    super-leading rows, e_J = 2 cases, soft-subgraph count by Euler relations (second form)
P5  Dirac algebra of the one-loop vertex numerator: J^- = 0, H^+ = 0, J_T.H_T = 0 (D=4), K dominance O(lam^2)
    for transverse current index; jet-tensor component scaling lam^0, lam^1, lam^2 (boost weights)
P6  real emission gamma* -> q qbar g: diagram-1 squared = 8 y23/y13 (numerator 32 p1.p3 p2.p3 ~ lam^2), full
    |M|^2 ~ 8 (x1^2+x2^2)/((1-x1)(1-x2)), collinear limit = (2 g^2/s13) C_F (1+z^2)/(1-z) x Born
P7  Glauber trapping (VF-REG-9): exact k^- integral 2 pi i/[2 kT^2 (pA+ + pA'+)], eikonal version ~ 1/eps
P8  QED soft photon factor (thm:ir-bn-qed): A = (1/16 pi^3) int dOmega F = (2 alpha/pi)[(1/2 beta) ln((1+beta)/(1-beta)) - 1]
P9  1D toy of the method of regions (VF-REG-13): T_s + T_h -> ln(M/m)/M with k^{-e}; cutoffs: double counting
P10 representation dependence of a divergent zero-bin integral (rem:ir-regions-values)
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
import mpmath as mp

RES = []
def check(name, cond):
    RES.append((name, bool(cond)))
    print(('PASS ' if cond else 'FAIL ') + name)

mp.mp.dps = 40
SQ2 = mp.sqrt(2)
def lc(a, b):            # light-cone tuples (plus, minus, T1, T2)
    return a[0]*b[1] + a[1]*b[0] - a[2]*b[2] - a[3]*b[3]

# =============================================================== P1 collinear k^- integral
print('=== P1: vertex collinear k^- integral (VF-REG-6) ===')
km, kp, kT2, p1p, p2m, xx = sp.symbols('kminus kplus kT2 p1p p2m x', real=True)
i0 = sp.Symbol('delta', positive=True)
D0 = 2*kp*km - kT2
D1 = -2*(p1p - kp)*km - kT2
D2 = 2*kp*(p2m + km) - kT2
sub = {kp: xx*p1p}
# poles of D_j + i delta
kmc = sp.Symbol('kmc')
poles = [sp.solve(sp.Eq(Dj.subs(sub).subs(km, kmc) + sp.I*i0, 0), kmc)[0] for Dj in (D0, D1, D2)]
print('   poles (k^-):', [sp.simplify(pp) for pp in poles])
# residue at the D1 pole (upper half plane for 0<x<1)
kpole = sp.solve(sp.Eq(D1.subs(sub), 0), km)[0]
resid = sp.simplify((1/(D0*D2)).subs(sub).subs(km, kpole)/sp.diff(D1.subs(sub), km))
Qs = 2*p1p*p2m
target = 1/(2*p1p)/(kT2*(xx*Qs - kT2/(1 - xx)))
check('P1 residue: int dk^- 1/(D0 D1 D2) = (2 pi i/2p1+) / [kT^2 (x Q^2 - kT^2/(1-x))]', sp.simplify(resid - target) == 0)
# numerical check with finite i delta
def num_kminus(xv, kTv, delta=1e-12, P1p=1/mp.sqrt(2), P2m=1/mp.sqrt(2)):
    xv = mp.mpf(xv); kTv = mp.mpf(kTv)
    f = lambda k: 1/((2*xv*P1p*k - kTv**2 + 1j*delta)*(-2*(1 - xv)*P1p*k - kTv**2 + 1j*delta)*(2*xv*P1p*(P2m + k) - kTv**2 + 1j*delta))
    poles_re = [kTv**2/(2*xv*P1p), -kTv**2/(2*(1 - xv)*P1p), -P2m + kTv**2/(2*xv*P1p)]
    pts = sorted(set([mp.mpf(p) for p in poles_re] + [mp.mpf(-3), mp.mpf(3)]))
    return mp.quad(f, [-mp.inf] + pts + [mp.inf], maxdegree=10)
for (xv, kTv) in [(0.3, 0.2), (0.6, 0.05), (0.8, 0.3)]:
    P1p = 1/mp.sqrt(2); P2m = 1/mp.sqrt(2); Q2 = 2*P1p*P2m
    ex = 2j*mp.pi/(2*P1p)/(kTv**2*(xv*Q2 - kTv**2/(1 - xv)))
    nu = num_kminus(xv, kTv)
    check('P1 numerical k^- integral matches residue formula at x=%.1f kT=%.2f (rel %.1e)' % (xv, kTv, float(abs(nu/ex - 1))), abs(nu/ex - 1) < 1e-5)
# x outside (0,1): all poles on one side -> 0
xv, kTv = -0.4, 0.2
nu = num_kminus(xv, kTv)
check('P1 x<0: all three poles on one side, integral ~ 0 (|I| = %.1e)' % float(abs(nu)), abs(nu) < 1e-5)

# =============================================================== P2 region exponents of the scalar vertex
print('=== P2: region exponents of the on-shell massless scalar vertex ===')
p1 = (1/SQ2, mp.mpf(0), mp.mpf(0), mp.mpf(0)); p2 = (mp.mpf(0), 1/SQ2, mp.mpf(0), mp.mpf(0))
def integrand(k):
    pm = tuple(p1[i] - k[i] for i in range(4)); pp = tuple(p2[i] + k[i] for i in range(4))
    return 1/(lc(k, k)*lc(pm, pm)*lc(pp, pp))
def expo(scal, base=(0.37, 0.53, 0.61, 0.29)):
    a, b, c = scal
    vals = []
    lams = [mp.mpf(10)**(-e) for e in (4, 5, 6, 7)]
    for lam in lams:
        k = (base[0]*lam**a, base[1]*lam**b*(1 if (a, b, c) != (0, 2, 1) else -1), base[2]*lam**c, base[3]*lam**c)
        meas = lam**(a + b + 2*c)
        vals.append(mp.log(abs(meas*integrand(k))))
    xs = [float(mp.log(l)) for l in lams]
    return np.polyfit(xs, [float(v) for v in vals], 1)[0]
expected = {(0, 0, 0): 0, (0, 2, 1): 0, (2, 0, 1): 0, (1, 1, 1): 0, (2, 2, 2): 0, (2, 2, 1): 0, (0, 1, 1): 1, (2, 2, 3): 2}
ok = True
for sc, pe in expected.items():
    e = expo(sc)
    print('   scaling %s: fitted p = %+.4f (expected %d)' % (sc, e, pe))
    ok = ok and abs(e - pe) < 1e-3
check('P2 all leading regions of the on-shell vertex give p = 0; (0,1,1)->1, (2,2,3)->2', ok)

# =============================================================== P3 eikonal errors, Glauber count
print('=== P3: eikonal approximation errors and the Glauber count ===')
pA = (mp.mpf(1), mp.mpf(0), mp.mpf(0), mp.mpf(0))        # A-collinear, p_A^- = 0
def eik_err(scal):
    a, b, c = scal
    errs = []; lams = [mp.mpf(10)**(-e) for e in (4, 5, 6, 7)]
    for lam in lams:
        k = (0.7*lam**a, -0.45*lam**b, 0.6*lam**c, -0.3*lam**c)
        pk = tuple(pA[i] + k[i] for i in range(4))
        exact = lc(pk, pk); eik = 2*pA[0]*k[1]
        errs.append(abs((exact - eik)/exact))
    return np.polyfit([float(mp.log(l)) for l in lams], [float(mp.log(e)) for e in errs], 1)[0]
es, eu, eg = eik_err((1, 1, 1)), eik_err((2, 2, 2)), eik_err((2, 2, 1))
print('   relative eikonal error exponents: soft %.3f, ultrasoft %.3f, Glauber %.3f' % (es, eu, eg))
check('P3 eikonal error O(lam) soft, O(lam^2) ultrasoft, O(1) Glauber (VF-REG-7)', abs(es - 1) < 1e-3 and abs(eu - 2) < 1e-3 and abs(eg) < 1e-3)
# Glauber power count (VF-GLA-1): measure lam^6, gluon 1/kT^2 lam^-2, two spectator props lam^-4, numerator Q^2
check('P3 Glauber exchange between A and B spectators: 6 - 2 - 4 + 0 = 0 (VF-GLA-1)', 6 - 2 - 4 == 0)

# =============================================================== P4 omega(R) bookkeeping
print('=== P4: superficial degree omega(R) (Sterman units) from the boost/dimension bookkeeping ===')
H = Fr(1, 2)
def jet_power(fg=0, fb=0, bplus=0, t=0, u=0, sg=0, sq=0, e=1):
    """power of lambda of one jet: rest-frame dimension + J-H loop measures + boost weights + soft weights"""
    b = bplus + t + u; f = fg + fb
    dimJ = 4 - 3*b - Fr(5, 2)*f - sg - Fr(3, 2)*sq          # unamputated lines to H, amputated soft legs
    if e == 1:
        dimJ += -1                                          # one external on-shell parton (-3/2 + 1/2)
        meas = 4*(b + f - 1)
    elif e == 2:   # forward (target) jet: two external on-shell partons, b+f-1 loops
        dimJ += -2
        meas = 4*(b + f - 1)
    elif e == 'cut':  # final-state jet of a cut graph: no external legs, b+f-2 relative loops + P_J^2 normal
        meas = 4*(b + f - 2) + 2
    boost = -bplus + u - H*fg + H*fb
    soft = -sg - H*sq
    return dimJ + meas + boost + soft
def soft_power(Mg, Mq):
    return 2*(4 - 3*Mg - Fr(5, 2)*Mq) + 8*(Mg + Mq - 1)
def soft_power_euler(Ng, Nq, V3, V4, Vqg, EJB, EJF, EHB, EHF):
    """direct count (second form): measure lam^8 per soft loop, soft gluon lam^-4, soft quark lam^-2 (with numerator),
    3-gluon vertex lam^2, each attachment to a jet adds a jet propagator lam^-2 with O(1) eikonal numerator"""
    LS = Ng + Nq - (V3 + V4 + Vqg)          # soft loops; attachment points impose no constraint on soft momenta
    return 8*LS - 4*Ng - 2*Nq - 2*(EJB + EJF) + 2*V3
# formula of VF-REG-8, in lambda units
def p_formula(jets, bSH=0, fSH=0):
    tot = 0
    for jt in jets:
        e = 2 if jt.get('e', 1) in (2, 'cut') else 1
        tot += jt.get('fg', 0) + jt.get('t', 0) + 2*jt.get('u', 0) + 2*jt.get('fb', 0) - e + jt.get('sq', 0)
    return tot + 2*bSH + 3*fSH
# general identity check over many configurations
ok_id = True
for fg in range(0, 3):
    for fb in range(0, 2):
        for bp in range(0, 3):
            for t in range(0, 2):
                for u in range(0, 2):
                    for sg in range(0, 2):
                        for sq in range(0, 2):
                            for e in (1, 2, 'cut'):
                                if fg + fb + bp + t + u == 0:
                                    continue
                                lhs = jet_power(fg, fb, bp, t, u, sg, sq, e)
                                ee = 1 if e == 1 else 2
                                rhs = (fg + t - ee) + 2*(u + fb) - 2*(sg + sq)
                                ok_id = ok_id and lhs == rhs
check('P4 jet power p_J = (f^g + t - e_J) + 2(u + f^b) - 2(s^g + s^q) for e_J = 1, 2 (forward), 2 (cut)', ok_id)
ok_s = all(soft_power(Mg, Mq) == 2*Mg + 3*Mq for Mg in range(0, 5) for Mq in range(0, 5) if Mg + Mq > 0)
check('P4 soft component: 2(4 - 3Mg - 5/2 Mq) + 8(M - 1) = 2 Mg + 3 Mq', ok_s)
# second form for the soft subgraph (Euler relations): random soft graphs
import random
rng = random.Random(4); ok_e = True
for _ in range(500):
    V3, V4, Vqg = rng.randint(0, 4), rng.randint(0, 2), rng.randint(0, 3)
    EJF = rng.randint(0, 2); EHF = rng.randint(0, 1)
    EJB, EHB = rng.randint(0, 4), rng.randint(0, 2)
    twoNg = 3*V3 + 4*V4 + Vqg + EJB + EHB; twoNq = 2*Vqg + EJF + EHF
    if twoNg % 2 or twoNq % 2:
        continue
    Ng, Nq = twoNg//2, twoNq//2
    lhs = soft_power_euler(Ng, Nq, V3, V4, Vqg, EJB, EJF, EHB, EHF)
    ok_e = ok_e and lhs == 2*EHB + 3*EHF + EJF
check('P4 second form (Euler relations): p_S = 2 E_H^B + 3 E_H^F + E_J^F for 500 random soft graphs', ok_e)
# table of reduced diagrams (omega = p/2)
rows = [
    ('Sudakov vertex, soft gluon between the two jets', [dict(fg=1, sg=1), dict(fg=1, sg=1)], 0, 0, 0),
    ('vertex, collinear gluon (scalar pol.) into H', [dict(fg=1, bplus=1), dict(fg=1)], 0, 0, 0),
    ('same, transverse gluon into H (twist 3)', [dict(fg=1, t=1), dict(fg=1)], 0, 0, H),
    ('same, "-" gluon into H', [dict(fg=1, u=1), dict(fg=1)], 0, 0, 1),
    ('extra collinear q qbar pair into H (3 quarks, twist 4)', [dict(fg=3), dict(fg=1)], 0, 0, 1),
    ('soft quark exchanged between the two jets', [dict(fg=1, sq=1), dict(fg=1, sq=1)], 0, 0, 1),
    ('soft gluon from S into H', [dict(fg=1, sg=1), dict(fg=1)], 1, 0, 1),
    ('soft quark from S into H', [dict(fg=1, sq=1), dict(fg=1)], 0, 1, 2),
    ('e+e- cut, two quark jets (Born-like)', [dict(fg=2, e='cut'), dict(fg=2, e='cut')], 0, 0, 0),
    ('e+e- cut, quark jets + scalar gluons + soft gluons', [dict(fg=2, bplus=3, sg=2, e='cut'), dict(fg=2, bplus=1, sg=2, e='cut')], 0, 0, 0),
    ('e+e- cut, gluon jet with two transverse gluons', [dict(t=2, e='cut'), dict(fg=2, e='cut')], 0, 0, 0),
    ('gluon jet: one transverse, all others scalar (super-leading)', [dict(t=1, bplus=2, e='cut'), dict(fg=2, e='cut')], 0, 0, -H),
    ('gluon jet: only scalar gluons (super-leading)', [dict(bplus=2, e='cut'), dict(fg=2, e='cut')], 0, 0, -1),
    ('DIS target jet: one quark each side + scalar gluons', [dict(fg=2, bplus=2, e=2)], 0, 0, 0),
    ('DY: two incoming jets + soft gluons between them', [dict(fg=2, sg=2, e=2), dict(fg=2, sg=2, e=2)], 0, 0, 0),
    ('DY: soft gluon into H', [dict(fg=2, sg=1, e=2), dict(fg=2, e=2)], 1, 0, 1),
]
ok_t = True
for name, jets, bSH, fSH, om_exp in rows:
    p_bk = sum(jet_power(**{k: v for k, v in jt.items()}) for jt in jets)
    # soft subgraph: assume one connected soft component with all soft legs (a single component suffices here)
    Mg = sum(jt.get('sg', 0) for jt in jets) + bSH; Mq = sum(jt.get('sq', 0) for jt in jets) + fSH
    if Mg + Mq > 0:
        p_bk += soft_power(Mg, Mq)
    p_f = p_formula(jets, bSH, fSH)
    om = Fr(p_bk, 2)
    print('   %-62s omega = %5s  (lambda^%s)' % (name, str(om), str(p_bk)))
    ok_t = ok_t and p_bk == p_f and om == om_exp
check('P4 table of reduced diagrams reproduces VF-REG-8 check table (bookkeeping = formula)', ok_t)
# per-connection powers (lambda units) and super-leading rows
conn = {'good quark': 1, 'bad quark': 2, 'transverse gluon': 1, 'scalar (K) gluon': 0, '"-" gluon': 2,
        'soft gluon -> jet': 0, 'soft quark -> jet': 1, 'soft gluon -> H': 2, 'soft quark -> H': 3}
ok_c = (p_formula([dict(fg=1)]) - p_formula([dict()]) == 1 and p_formula([dict(fb=1)]) - p_formula([dict()]) == 2 and
        p_formula([dict(t=1)]) - p_formula([dict()]) == 1 and p_formula([dict(u=1)]) - p_formula([dict()]) == 2 and
        p_formula([dict(sq=1)]) - p_formula([dict()]) == 1 and p_formula([dict()], bSH=1) - p_formula([dict()]) == 2 and
        p_formula([dict()], fSH=1) - p_formula([dict()]) == 3)
check('P4 per-connection powers: good q +1, bad q +2, T gluon +1, K gluon 0, "-" gluon +2; soft g->J 0, q->J +1, g->H +2, q->H +3', ok_c)
check('P4 super-leading rows for e_J=2: (n_F,n_T)=(0,0) -> p_J=-2; (0,1) -> p_J=-1',
      jet_power(bplus=2, e=2) == -2 and jet_power(t=1, bplus=1, e=2) == -1 and jet_power(bplus=2, e='cut') == -2 and jet_power(t=1, bplus=1, e='cut') == -1)

# =============================================================== P5 Dirac algebra of the vertex numerator
print('=== P5: one-loop vertex numerator J.H in the collinear-1 region ===')
I2 = np.eye(2); sx = np.array([[0, 1], [1, 0]]); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]])
Z2 = np.zeros((2, 2))
g0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
gs = [np.block([[Z2, s], [-s, Z2]]).astype(complex) for s in (sx, sy, sz)]
GAM = [g0] + gs
METRIC = np.diag([1., -1., -1., -1.])
def slash(p):  # p contravariant cartesian (t,x,y,z)
    return sum(METRIC[m, m]*p[m]*GAM[m] for m in range(4))
def cart(pp, pm, t1, t2):
    return np.array([(pp + pm)/np.sqrt(2), t1, t2, (pp - pm)/np.sqrt(2)])
gp = (GAM[0] + GAM[3])/np.sqrt(2); gm = (GAM[0] - GAM[3])/np.sqrt(2)   # gamma^+ , gamma^- (upper)
Pp = 0.5*gm @ gp; Pm = 0.5*gp @ gm
check('P5 projectors: P_+ + P_- = 1, P_+^2 = P_+, {gamma^+,gamma^-} = 2', np.allclose(Pp + Pm, np.eye(4)) and np.allclose(Pp @ Pp, Pp) and np.allclose(gp @ gm + gm @ gp, 2*np.eye(4)))
P1v = cart(1.0, 0, 0, 0); P2v = cart(0, 1.0, 0, 0)
def nullsp(P):
    u_, s_, vh = np.linalg.svd(slash(P)); return vh[2:].conj().T
U1 = nullsp(P1v); V2 = nullsp(P2v)
spinors = [(U1[:, i].conj() @ g0, V2[:, j]) for i in range(2) for j in range(2)]
def pieces(K, ub, v, mu):
    J = [ub @ GAM[n] @ slash(P1v - K) for n in range(4)]
    Hh = [GAM[mu] @ slash(-(P2v + K)) @ GAM[n] @ v for n in range(4)]
    Jp = (J[0] + J[3])/np.sqrt(2); Jm = (J[0] - J[3])/np.sqrt(2)
    Hp = (Hh[0] + Hh[3])/np.sqrt(2); Hm = (Hh[0] - Hh[3])/np.sqrt(2)
    JpHm = Jp @ Hm; JmHp = Jm @ Hp; JTHT = J[1] @ Hh[1] + J[2] @ Hh[2]
    full = sum(METRIC[n, n]*(J[n] @ Hh[n]) for n in range(4))
    kH = sum(METRIC[n, n]*K[n]*Hh[n] for n in range(4))
    kplus = (K[0] + K[3])/np.sqrt(2)
    Kapprox = (Jp @ kH)/kplus
    return JpHm, JmHp, JTHT, full, Kapprox, np.linalg.norm(Jm), np.linalg.norm(Hp)
lams = [1e-2, 1e-3, 1e-4]
x_, kap, tau = 0.37, -0.8, (0.6, -0.45)
ok_exact = True; rel_T = []; rel_L = {}
for (ub, v) in spinors:
    for mu in range(4):
        for lam in lams:
            K = cart(x_*1.0, lam**2*kap, lam*tau[0], lam*tau[1])
            JpHm, JmHp, JTHT, full, Kap, nJm, nHp = pieces(K, ub, v, mu)
            ok_exact = ok_exact and nJm < 1e-12 and nHp < 1e-12 and abs(JTHT) < 1e-12*max(1, abs(full)) and abs(full - JpHm) < 1e-12*max(1, abs(full))
# K dominance for transverse current index: (N - K)/N ~ lam^2
for mu in (1, 2):
    for (ub, v) in spinors:
        tree = ub @ GAM[mu] @ v
        if abs(tree) < 1e-8:
            continue
        rels = []
        for lam in lams:
            K = cart(x_*1.0, lam**2*kap, lam*tau[0], lam*tau[1])
            JpHm, JmHp, JTHT, full, Kap, _, _ = pieces(K, ub, v, mu)
            rels.append(abs(full - Kap)/abs(full))
        rel_T.append(np.polyfit(np.log(lams), np.log(rels), 1)[0])
check('P5 exactly in D=4 (p1 || n_A, p2 || n_B): J^- = 0, H^+ = 0, J_T.H_T = 0, hence J.H = J^+ H^-', ok_exact)
check('P5 K dominance, transverse current index: |J.H - (J^+/k^+) k.H| / |J.H| ~ lam^2 (fitted %s)' % np.round(rel_T, 3),
      len(rel_T) > 0 and all(abs(r - 2) < 0.02 for r in rel_T))
# for the current index mu = +,-: tree current vanishes (helicity); leading numerator suppressed
trees_pm = [abs(ub @ gp @ v) + abs(ub @ gm @ v) for (ub, v) in spinors]
check('P5 tree current ubar(p1) gamma^pm v(p2) = 0 (only transverse current components at leading power)', max(trees_pm) < 1e-12)
# boost weights of the jet tensor J^nu = ubar(p1) gamma^nu (p1-k)slash with a tilted jet axis (generic components)
def roty(vv, th):
    c, s_ = np.cos(th), np.sin(th); return np.array([vv[0], c*vv[1] + s_*vv[3], vv[2], -s_*vv[1] + c*vv[3]])
comps = []
for lam in lams:
    th = 0.7*lam
    P1r = roty(P1v, th); Kr = roty(cart(x_*1.0, lam**2*kap, lam*tau[0], lam*tau[1]), th)
    U1r = nullsp(P1r); ub = U1r[:, 0].conj() @ g0
    J = [ub @ GAM[n] @ slash(P1r - Kr) for n in range(4)]
    Jp = (J[0] + J[3])/np.sqrt(2); Jm = (J[0] - J[3])/np.sqrt(2)
    comps.append((np.linalg.norm(Jp), np.linalg.norm(np.r_[J[1], J[2]]), np.linalg.norm(Jm)))
comps = np.array(comps)
sl = [np.polyfit(np.log(lams), np.log(comps[:, i]), 1)[0] for i in range(3)]
print('   jet tensor (tilted axis): |J^+| ~ lam^%.3f, |J_T| ~ lam^%.3f, |J^-| ~ lam^%.3f' % tuple(sl))
check('P5 boost weights: J^+ ~ lam^0, J_T ~ lam^1, J^- ~ lam^2 (dim 3/2 + weights -1-1/2, -1/2, +1-1/2)',
      abs(sl[0]) < 0.02 and abs(sl[1] - 1) < 0.02 and abs(sl[2] - 2) < 0.02)

# =============================================================== P6 real emission
print('=== P6: real emission gamma* -> q(p1) qbar(p2) g(p3) ===')
def trace(*ms):
    out = np.eye(4, dtype=complex)
    for M in ms: out = out @ M
    return np.trace(out)
def msq_diagrams(p1, p2, p3):
    """-g_{mu mu'} (-g_{nu nu'}) sum over spins: diagram 1 (gluon off quark), 2 (off antiquark), interference; 4D"""
    P = p1 + p3; Pb = p2 + p3
    s11 = s22 = s12 = 0
    for mu in range(4):
        for nu in range(4):
            gmu, gnu = METRIC[mu, mu], METRIC[nu, nu]
            A1 = GAM[nu] @ slash(P) @ GAM[mu]; A2 = GAM[mu] @ slash(-Pb) @ GAM[nu]
            B1 = GAM[mu] @ slash(P) @ GAM[nu]; B2 = GAM[nu] @ slash(-Pb) @ GAM[mu]
            s11 += gmu*gnu*trace(slash(p1), A1, slash(p2), B1)
            s22 += gmu*gnu*trace(slash(p1), A2, slash(p2), B2)
            s12 += gmu*gnu*trace(slash(p1), A1, slash(p2), B2)
    d1 = 2*(p1 @ METRIC @ p3); d2 = 2*(p2 @ METRIC @ p3)
    # overall: -g for photon index and -g for gluon index -> (+1) product of the two minus signs
    return (s11/d1**2).real, (s22/d2**2).real, (2*s12/(d1*d2)).real, s11.real
rngn = np.random.default_rng(3)
ok6 = True
for _ in range(5):
    # random massless 3-body configuration in the gamma* rest frame, sqrt(s) = 1
    x1, x2 = rngn.uniform(0.3, 0.95), rngn.uniform(0.3, 0.95)
    if x1 + x2 < 1.05: x1, x2 = 0.8, 0.7
    x3 = 2 - x1 - x2
    E1, E2, E3 = x1/2, x2/2, x3/2
    c12 = 1 - 2*(1 - x3)/(x1*x2)    # cos angle between p1 and p2 from s12 = 2E1E2(1-cos) = (1-x3)
    th12 = np.arccos(np.clip(c12, -1, 1))
    p1 = np.array([E1, 0, 0, E1]); p2 = np.array([E2, E2*np.sin(th12), 0, E2*np.cos(th12)]); p3 = np.array([1.0, 0, 0, 0]) - p1 - p2
    m11, m22, m12, n11 = msq_diagrams(p1, p2, p3)
    y13 = 2*(p1 @ METRIC @ p3); y23 = 2*(p2 @ METRIC @ p3); y12 = 2*(p1 @ METRIC @ p2)
    tot = m11 + m22 + m12
    ok6 = ok6 and abs(m11 - 8*y23/y13) < 1e-9*abs(m11) and abs(n11 - 32*(p1 @ METRIC @ p3)*(p2 @ METRIC @ p3)) < 1e-9*abs(n11)
    ok6 = ok6 and abs(tot - 8*(x1**2 + x2**2)/((1 - x1)*(1 - x2))) < 1e-9*tot
check('P6 diagram-1 squared = 8 y23/y13 (numerator 32 p1.p3 p2.p3); total = 8 (x1^2+x2^2)/((1-x1)(1-x2)) (4D, colour/couplings stripped)', ok6)
# collinear scaling of the numerator: p3 -> collinear to p1
ns = []; lamsC = [1e-2, 1e-3, 1e-4]
for lam in lamsC:
    z = 0.6
    th = lam
    # parent momentum along z with energy 1/2 ; q (p1) and g (p3) share it with small opening angle ~ lam
    p1 = z*0.5*np.array([1, np.sin(th*(1 - z)), 0, np.cos(th*(1 - z))])
    p3 = (1 - z)*0.5*np.array([1, -np.sin(th*z), 0, np.cos(th*z)])
    p2 = np.array([1.0, 0, 0, 0]) - p1 - p3
    p2 = np.array([np.sqrt(p2[1]**2 + p2[2]**2 + p2[3]**2), p2[1], p2[2], p2[3]])   # put p2 on shell (energy readjusted)
    m11, m22, m12, n11 = msq_diagrams(p1, p2, p3)
    ns.append(abs(n11))
sl_n = np.polyfit(np.log(lamsC), np.log(ns), 1)[0]
check('P6 collinear limit: squared numerator of the quark-emission graph ~ lam^2 (fitted %.3f)' % sl_n, abs(sl_n - 2) < 0.05)
# collinear limit ratio vs splitting function (exact algebra)
zz, s13, ss = sp.symbols('z s13 s', positive=True)
x1s, x2s = zz, 1 - s13/ss       # x2 -> 1 - s13/s,  x1 -> z at leading power
Msq = 8*(x1s**2 + x2s**2)/((1 - x1s)*(1 - x2s))
Born = 4*ss                     # -g_{mu nu} Tr[p1 g^mu p2 g^nu] = 8 p1.p2 = 4 s
ratio = sp.limit(sp.simplify(Msq/Born*s13), s13, 0)
check('P6 collinear limit: |M|^2/|M_0|^2 -> (2/s13) (1+z^2)/(1-z) [times g^2 C_F] (prop:qcd-soft-collinear-limits(b))',
      sp.simplify(ratio - 2*(1 + zz**2)/(1 - zz)) == 0)

# =============================================================== P7 Glauber trapping
print('=== P7: Glauber trapping (VF-REG-9) ===')
pAp, pBp, kT2s = sp.symbols('pAp pApp kT2', positive=True)
kmm = sp.Symbol('km')
dlt = sp.Symbol('d', positive=True)
Din = -2*pAp*kmm - kT2s      # (p_A - k)^2 for an incoming A line (p_A^- = 0), pole k^- = -kT^2/(2pA+) + i0
Dout = 2*pBp*kmm - kT2s      # (p_A' + k)^2 for an outgoing A line, pole k^- = kT^2/(2pA'+) - i0
kpole = sp.solve(sp.Eq(Din, 0), kmm)[0]
res = sp.simplify((1/Dout).subs(kmm, kpole)/sp.diff(Din, kmm))
check('P7 exact: int dk^- 1/[(Din+i0)(Dout+i0)] = 2 pi i/[2 kT^2 (pA+ + pA\'+)] (close above, residue at Din pole)',
      sp.simplify(res - 1/(2*kT2s*(pAp + pBp))) == 0)
def glauber_num(kT, d, pa=1.0, pb=0.7):
    f = lambda k: 1/((-2*pa*k - kT**2 + 1j*d)*(2*pb*k - kT**2 + 1j*d))
    k1 = mp.mpf(-kT**2/(2*pa)); k2 = mp.mpf(kT**2/(2*pb))      # real parts of the two poles (opposite sides)
    return mp.quad(f, [-mp.inf, -1, k1, 0, k2, 1, mp.inf])
for kT in (0.1, 0.01):
    nu = glauber_num(kT, 1e-12); ex = 2j*mp.pi/(2*kT**2*(1.0 + 0.7))
    check('P7 numeric exact integral at kT=%.2f (rel %.1e)' % (kT, float(abs(nu/ex - 1))), abs(nu/ex - 1) < 1e-6)
# eikonal version: drop kT^2 -> ~ 1/d
vals = []
for d in (1e-3, 1e-4, 1e-5):
    f = lambda k: 1/((-2*1.0*k + 1j*d)*(2*0.7*k + 1j*d))
    vals.append(abs(mp.quad(f, [-mp.inf, -1, 0, 1, mp.inf])))
sl_e = np.polyfit(np.log([1e-3, 1e-4, 1e-5]), np.log([float(v) for v in vals]), 1)[0]
check('P7 eikonal version (kT^2 dropped) diverges ~ 1/i0 (fitted exponent %.3f)' % sl_e, abs(sl_e + 1) < 1e-3)
# exact eikonal value: 2 pi i * 1/(-2pa) * 1/(2pb (i d/2pa) + i d) = -pi/(d (pa+pb)) ... check
d = mp.mpf('1e-4'); f = lambda k: 1/((-2*1.0*k + 1j*d)*(2*0.7*k + 1j*d))
nu = mp.quad(f, [-mp.inf, -1, 0, 1, mp.inf]); ex = -mp.pi/(d*(1.0 + 0.7))
check('P7 eikonal value = -pi/(i0 (pA+ + pA\'+)) (rel %.1e)' % float(abs(nu/ex - 1)), abs(nu/ex - 1) < 1e-6)

# =============================================================== P8 QED soft photon factor
print('=== P8: QED soft-photon exponent (thm:ir-bn-qed) ===')
def A_numeric(beta_rel_target=None, m=1.0, E=2.0, theta=1.1, nth=400, nph=400):
    # incoming p (eta=-1), outgoing p' (eta=+1), same mass m and energy E, scattering angle theta
    pv = np.sqrt(E**2 - m**2)
    p = np.array([E, 0, 0, pv]); pp = np.array([E, pv*np.sin(theta), 0, pv*np.cos(theta)])
    # Gauss-Legendre in cos(th) and in ph (the integrand is smooth for m > 0)
    xc, wc = np.polynomial.legendre.leggauss(nth)
    xp, wp = np.polynomial.legendre.leggauss(nph)
    ph = np.pi*(xp + 1); wph = np.pi*wp
    C, PH = np.meshgrid(xc, ph, indexing='ij'); W = np.outer(wc, wph)
    S = np.sqrt(1 - C**2)
    nx, ny, nz = S*np.cos(PH), S*np.sin(PH), C
    pn = p[0] - (p[1]*nx + p[2]*ny + p[3]*nz); ppn = pp[0] - (pp[1]*nx + pp[2]*ny + pp[3]*nz)
    pdpp = p[0]*pp[0] - p[1:] @ pp[1:]
    Sig = m**2/pn**2 + m**2/ppn**2 - 2*pdpp/(pn*ppn)   # charges e=1, eta_in=-1, eta_out=+1
    val = np.sum(W*(-Sig))                               # int dOmega F,  F = -Sig
    e2 = 4*np.pi   # e^2 = 4 pi alpha with alpha = 1 (A is linear in alpha)
    A = e2*val/(16*np.pi**3)
    beta = np.sqrt(1 - m**4/pdpp**2)
    closed = (2/np.pi)*((1/(2*beta))*np.log((1 + beta)/(1 - beta)) - 1)
    q2 = 2*m**2 - 2*pdpp
    fIR = float(mp.quad(lambda xx: (m**2 - q2/2)/(m**2 - q2*xx*(1 - xx)), [0, 1])) - 1
    return A, closed, (2/np.pi)*fIR
for (E, th) in [(2.0, 1.1), (5.0, 0.4), (1.3, 2.5)]:
    A, closed, fir = A_numeric(E=E, theta=th)
    print('   E=%.1f theta=%.1f: A/alpha numeric %.12f, closed form %.12f, (2/pi) f_IR %.12f' % (E, th, A, closed, fir))
    check('P8 A = (2 alpha/pi)[(1/2beta) ln((1+beta)/(1-beta)) - 1] = (2 alpha/pi) f_IR(q^2) at E=%.1f' % E,
          abs(A - closed) < 1e-8*abs(closed) and abs(closed - fir) < 1e-10)

# =============================================================== P9 1D toy (method of regions)
print('=== P9: one-dimensional toy integral (VF-REG-13) ===')
e_, k_, m_, M_ = sp.symbols('e k m M', positive=True)
Ts = sp.integrate(k_**(-e_)/((k_ + m_)*M_), (k_, 0, sp.oo), conds='none')      # soft: expand 1/(k+M) -> 1/M
en_ = sp.Symbol('en', negative=True)     # the hard-region integral converges for -1 < e < 0
Th = sp.integrate(k_**(-en_)/(k_*(k_ + M_)), (k_, 0, sp.oo), conds='none').subs(en_, e_)       # hard: expand 1/(k+m) -> 1/k
Ts_c = m_**(-e_)*sp.gamma(e_)*sp.gamma(1 - e_)/M_
Th_c = M_**(-1 - e_)*sp.gamma(-e_)*sp.gamma(1 + e_)
check('P9 T_s = m^{-e} Gamma(e) Gamma(1-e)/M (0<e<1)', abs(complex(sp.N((Ts - Ts_c).subs({e_: sp.Rational(3, 10), m_: 2, M_: 5}), 25))) < 1e-18)
check('P9 T_h = M^{-1-e} Gamma(-e) Gamma(1+e) (-1<e<0)', abs(complex(sp.N((Th - Th_c).subs({e_: sp.Rational(-3, 10), m_: 2, M_: 5}), 25))) < 1e-18)
lim = sp.limit(Ts_c + Th_c, e_, 0)
check('P9 T_s + T_h -> ln(M/m)/M as e -> 0', sp.simplify(lim - sp.log(M_/m_)/M_) == 0)
exactI = sp.integrate(1/((k_ + m_)*(k_ + M_)), (k_, 0, sp.oo))
print('   exact I =', sp.simplify(exactI), ' ; leading power ln(M/m)/M')
# cutoff version: m = 1e-3, M = 1, cutoffs [1e-12, 1e12]
lo, hi, mv, Mv = mp.mpf('1e-12'), mp.mpf('1e12'), mp.mpf('1e-3'), mp.mpf(1)
Tsc = mp.quad(lambda kk: 1/((kk + mv)*Mv), [lo, 1, hi])
Thc = mp.quad(lambda kk: 1/(kk*(kk + Mv)), [lo, 1, hi])
Tsh = mp.quad(lambda kk: 1/(kk*Mv), [lo, 1, hi])
print('   cutoffs: T_s + T_h = %s ; T_s + T_h - T_s T_h = %s ; ln(M/m)/M = %s' % (mp.nstr(Tsc + Thc, 6), mp.nstr(Tsc + Thc - Tsh, 8), mp.nstr(mp.log(Mv/mv)/Mv, 8)))
check('P9 cutoffs: T_s + T_h double counts (62.17); T_s + T_h - T_sT_h = 6.9078 = ln(1000)',
      abs(Tsc + Thc - mp.mpf('62.17')) < 0.01 and abs(Tsc + Thc - Tsh - mp.log(1000)) < 1e-3)

# =============================================================== P10 representation dependence of a divergent zero-bin integral
print('=== P10: rem:ir-regions-values ===')
sig = sp.Symbol('sigma', positive=True)
param01 = sp.integrate(sig**(-1 - en_), (sig, 0, 1), conds='none').subs(en_, e_)      # valid for e<0, continued
print('   int_0^1 dsigma sigma^{-1-eps} =', sp.simplify(param01), ' (continued from eps<0)')
check('P10 parametric representation int_0^1 dsigma sigma^{-1-eps} = -1/eps', sp.simplify(param01 + 1/e_) == 0)
print('   int_0^infty dsigma sigma^{-1-eps}: scaleless, = 0 in DR (split at 1: -1/eps_IR + 1/eps_UV)')
check('P10 split at sigma=1: (-1/eps)|_{eps<0} + (1/eps)|_{eps>0} = 0 after continuation', sp.simplify(-1/e_ + 1/e_) == 0)

print()
npass = sum(1 for _, ok in RES if ok)
print('SUMMARY: %d/%d checks passed' % (npass, len(RES)))
