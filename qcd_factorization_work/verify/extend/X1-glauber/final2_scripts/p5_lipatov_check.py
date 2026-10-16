# X1 final2 (Fix 1(d)) -- P5: tree 2->3 amplitude of two straight eikonal lines (velocities v_A, v_B) exchanging one
# gluon and radiating one on-shell gluon k.  Replaces final_scripts/p5_interference.py, whose currents v_X/(v_X.k) had
# equal normalization (no exchange propagators), which made its gauge-invariance check circular.
# Kinematics: line A gives up q1, line B gives up q2, q1 + q2 = k, v_A.q1 = 0, v_B.q2 = 0 (recoilless eikonal lines).
# Colour C = f^{a1 a2 b} T_A^{a1} T_B^{a2} (common to all three terms; overall factor g^3 and phases dropped):
#   A_A^mu =  C (vA.vB) vA^mu /((vA.k) q2^2)                      [gluon k from line A; exchange propagator 1/q2^2]
#   A_B^mu = -C (vA.vB) vB^mu /((vB.k) q1^2)                      [gluon k from line B; exchange propagator 1/q1^2]
#   A_3^mu = -C [(vA.vB)(q1-q2)^mu + 2(vA.k) vB^mu - 2(vB.k) vA^mu]/(q1^2 q2^2)   [three-gluon vertex, both propagators]
# Checks: (1) k.(A_A+A_B) = C (vA.vB)(1/q2^2 - 1/q1^2) (not zero); (2) |A_A+A_B|^2 gauge dependent;
# (3) k.(A_A+A_B+A_3) = 0 and |A_A+A_B+A_3|^2 gauge independent; (4) Feynman-gauge interference
#     2 A_A.(-g).A_B = 2 (vA.vB)^3/((vA.k)(vB.k) q1^2 q2^2) > 0, self terms <= 0, hence D_C-integrand >= |A_A+A_B|^2_F;
# (5) the line parts conserve the current only as q1^2/q2^2 -> 1 (|k_T| << |q_T|);
# (6) light-like lines: -J.J = 4 (vA.vB)^2 / (k_T^2 q1T^2 q2T^2), the square of the Lipatov vertex (C_mu C^mu = -4 q1T^2 q2T^2/k_T^2).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
rng = np.random.default_rng(1729)
out = []
def log(s=''):
    print(s, flush=True); out.append(s)
g = np.diag([1., -1., -1., -1.])
dot = lambda a, b: a @ g @ b
def lc(vp, vm, vt):
    return np.array([(vp + vm)/np.sqrt(2), vt[0], vt[1], (vp - vm)/np.sqrt(2)])
def comps(v):
    return (v[0] + v[3])/np.sqrt(2), (v[0] - v[3])/np.sqrt(2)
def polsum(kind, k, n):
    if kind == 'F':
        return -g
    kl = g @ k; nl = g @ n
    return -g + (np.outer(kl, nl) + np.outer(nl, kl))/dot(n, k)
def solve_q1(vA, vB, k, q1t):
    vAp, vAm = comps(vA); vBp, vBm = comps(vB); kp, km = comps(k)
    # vA.q1 = vA^+ q1^- + vA^- q1^+ (vA_T = 0) = 0 ;  vB.q1 = vB.k
    Amat = np.array([[vAm, vAp], [vBm, vBp]])
    rhs = np.array([0.0, vBp*km + vBm*kp - 0.0])
    q1p, q1m = np.linalg.solve(Amat, rhs)
    return lc(q1p, q1m, q1t)
ok_all = True
rows = []
for case, Y in (('timelike Y=0.5', 0.5), ('timelike Y=2', 2.0), ('timelike Y=4', 4.0), ('timelike Y=8', 8.0), ('lightlike', None)):
    if Y is None:
        vA = np.array([1., 0, 0, 1.]); vB = np.array([1., 0, 0, -1.])
    else:
        vA = lc(np.exp(Y/2)/np.sqrt(2), np.exp(-Y/2)/np.sqrt(2), [0, 0]); vB = lc(np.exp(-Y/2)/np.sqrt(2), np.exp(Y/2)/np.sqrt(2), [0, 0])
    st = dict(id1=0, cons_lines=0, cons_full=0, g_lines=0, g_full=0, id4=0, minint=np.inf, maxself=-np.inf, diff=np.inf, sr=0, cen=[], lip=0)
    yr = (Y/2 if Y is not None else 3.0)
    for _ in range(4000):
        kt = rng.normal(size=2); y = rng.uniform(-yr, yr)
        kT = np.linalg.norm(kt)
        k = lc(kT*np.exp(y)/np.sqrt(2), kT*np.exp(-y)/np.sqrt(2), kt)
        q1t = rng.normal(size=2)*rng.choice([0.3, 1.0, 3.0])
        q1 = solve_q1(vA, vB, k, q1t); q2 = k - q1
        assert abs(dot(vA, q1)) < 1e-9*(1 + abs(q1).max()) and abs(dot(vB, q2)) < 1e-9*(1 + abs(q2).max())
        vv = dot(vA, vB); Q1 = dot(q1, q1); Q2 = dot(q2, q2)
        AA = vv*vA/(dot(vA, k)*Q2); AB = -vv*vB/(dot(vB, k)*Q1)
        A3 = -(vv*(q1 - q2) + 2*dot(vA, k)*vB - 2*dot(vB, k)*vA)/(Q1*Q2)
        L = AA + AB; J = L + A3
        scale = abs(dot(k, AA)) + abs(dot(k, AB))
        st['id1'] = max(st['id1'], abs(dot(k, L) - vv*(1/Q2 - 1/Q1))/scale)
        st['cons_lines'] = max(st['cons_lines'], abs(dot(k, L))/scale)
        st['cons_full'] = max(st['cons_full'], abs(dot(k, J))/scale)
        n = np.array([1.0, *rng.normal(size=3)]); n[1:] /= np.linalg.norm(n[1:])
        PF, PL = polsum('F', k, n), polsum('L', k, n)
        LF, LL = L @ PF @ L, L @ PL @ L
        JF, JL = J @ PF @ J, J @ PL @ J
        st['g_lines'] = max(st['g_lines'], abs(LF - LL)/abs(LF))
        st['g_full'] = max(st['g_full'], abs(JF - JL)/abs(JF))
        inter = 2*(AA @ PF @ AB); pred = 2*vv**3/(dot(vA, k)*dot(vB, k)*Q1*Q2)
        st['id4'] = max(st['id4'], abs(inter - pred)/abs(pred))
        st['minint'] = min(st['minint'], inter)
        selfs = AA @ PF @ AA + AB @ PF @ AB
        st['maxself'] = max(st['maxself'], selfs)
        st['diff'] = min(st['diff'], (inter - LF)/abs(inter))          # = -self/inter >= 0
        if Y is not None:
            pr = ((dot(vB, k)*Q1)/(dot(vA, k)*Q2) + (dot(vA, k)*Q2)/(dot(vB, k)*Q1))/(2*vv)
            st['sr'] = max(st['sr'], abs(-selfs/inter - pr)/pr)
            if abs(y) <= 0.1*Y:
                st['cen'].append(-selfs/inter)
        if Y is None:
            q1T2 = q1t @ q1t; q2T2 = (kt - q1t) @ (kt - q1t)
            st['lip'] = max(st['lip'], abs(JF - 4*vv**2/(kT**2*q1T2*q2T2))/abs(JF))
    okc = (st['id1'] < 1e-10 and st['cons_full'] < 1e-10 and st['g_full'] < 1e-8 and st['id4'] < 1e-10 and st['minint'] > 0
           and st['maxself'] <= 1e-14 and st['g_lines'] > 1e-3 and st['diff'] >= -1e-9 and st['sr'] < 1e-10
           and (Y is not None or st['lip'] < 1e-9))
    ok_all &= okc
    log(f"{case:15s}: k.(A_A+A_B) = (vA.vB)(1/q2^2-1/q1^2) to {st['id1']:.1e}; line-part current violation up to {st['cons_lines']:.3f};"
        f" |A_A+A_B|^2 Feyn vs LC differ up to {st['g_lines']:.2e} (gauge dependent);")
    log(f"{'':15s}  with A_3: |k.J|/scale <= {st['cons_full']:.1e}, |J|^2 gauge difference <= {st['g_full']:.1e};"
        f" Feynman interference = 2(vA.vB)^3/((vA.k)(vB.k)q1^2q2^2) to {st['id4']:.1e}, min value {st['minint']:.2e} > 0;"
        f" max self term {st['maxself']:.2e} (<= 0)")
    extra = f"; light-like -J.J = 4(vA.vB)^2/(kT^2 q1T^2 q2T^2) to {st['lip']:.1e}" if Y is None else ""
    if Y is not None:
        cen = np.array(st['cen'])
        log(f"{'':15s}  interference - |A_A+A_B|^2_Feyn = -self >= 0 (min over points of (inter-|L|^2_F)/inter = {st['diff']:.3e});"
            f" |self|/inter = [..]/(2 vA.vB) to {st['sr']:.1e}; central emission |y|<=Y/10: median |self|/inter = {np.median(cen):.4f},"
            f" 1/cosh Y = {1/np.cosh(Y):.4f}")
    else:
        log(f"{'':15s}  light-like lines: self terms vanish, interference = |A_A+A_B|^2_Feyn exactly (min (inter-|L|^2)/inter = {st['diff']:.1e}){extra}")
# (5) line parts conserve the current only when q1^2 = q2^2: violation vs |k_T|/|q_T|
vA = lc(np.exp(2)/np.sqrt(2), np.exp(-2)/np.sqrt(2), [0, 0]); vB = lc(np.exp(-2)/np.sqrt(2), np.exp(2)/np.sqrt(2), [0, 0])
log("(5) line-part current violation |k.(A_A+A_B)|/(|k.A_A|+|k.A_B|) = |q1^2-q2^2|/(|q1^2|+|q2^2|) as |k_T|/|q_T| -> 0 (Y=4):")
viol_prev = None; mono = True
for ratio in (1.0, 0.3, 0.1, 0.03, 0.01, 0.001):
    viols = []
    for _ in range(500):
        phi = rng.uniform(0, 2*np.pi); kt = ratio*np.array([np.cos(phi), np.sin(phi)]); y = rng.uniform(-1, 1)
        kT = np.linalg.norm(kt); k = lc(kT*np.exp(y)/np.sqrt(2), kT*np.exp(-y)/np.sqrt(2), kt)
        psi = rng.uniform(0, 2*np.pi); q1t = np.array([np.cos(psi), np.sin(psi)])
        q1 = solve_q1(vA, vB, k, q1t); q2 = k - q1
        vv = dot(vA, vB); Q1 = dot(q1, q1); Q2 = dot(q2, q2)
        AA = vv*vA/(dot(vA, k)*Q2); AB = -vv*vB/(dot(vB, k)*Q1)
        viols.append(abs(dot(k, AA + AB))/(abs(dot(k, AA)) + abs(dot(k, AB))))
    m = max(viols)
    log(f"    |k_T|/|q_T| = {ratio:g}: max violation {m:.2e}")
    if viol_prev is not None and m > viol_prev:
        mono = False
    viol_prev = m
ok_all &= mono and viol_prev < 1e-2
log("ALL PASS" if ok_all else "SOME CHECK FAILED")
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'final2_logs', 'p5_lipatov_check.log'), 'w') as f:
    f.write('\n'.join(out) + '\n')
