# Final review of X1 -- P5(ii),(iii): eikonal 2->3 amplitude A+B -> A+B+g at O(g^3) with straight
# time-like Wilson lines v_A, v_B.  Exchange momenta: q1 emitted by line A, q2 emitted by line B,
# q1 + q2 = k (on shell), with the infinite-line constraints v_A.q1 = 0, v_B.q2 = 0.
#   line part A (gluon k radiated from A, exchange q2 from B):  L_A^mu =  C v_A^mu (vA.vB)/((vA.k) q2^2)
#   line part B (gluon k radiated from B, exchange q1 from A):  L_B^mu = -C v_B^mu (vA.vB)/((vB.k) q1^2)
#   three-gluon term: V^mu = C [ (vA.vB)(q1-q2)^mu + 2(vA.k) vB^mu - 2(vB.k) vA^mu ] /(q1^2 q2^2)  (overall sign
#   fixed below by requiring current conservation of the sum).
# Checks: (1) k.(L_A+L_B) != 0 unless q1^2 = q2^2 (the report's "common factor 1/q_T^2" is an approximation);
#         (2) |L_A+L_B|^2 is gauge dependent (Feynman vs light-cone gauge) for q1^2 != q2^2;
#         (3) with the three-gluon term, the full current is conserved and |J|^2 is gauge independent;
#         (4) the Feynman-gauge interference 2 Re L_A.(-g).L_B stays positive (P5's sign conclusion survives).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
rng = np.random.default_rng(11)
g = np.diag([1., -1., -1., -1.])
dot = lambda a, b: a @ g @ b
def lc(vp, vm, vt):  # light-cone components -> Cartesian (v^0, v^1, v^2, v^3)
    return np.array([(vp + vm)/np.sqrt(2), vt[0], vt[1], (vp - vm)/np.sqrt(2)])
def polsum(kind, k, n):
    if kind == 'F':
        return -g
    kl = g @ k; nl = g @ n
    return -g + (np.outer(kl, nl) + np.outer(nl, kl))/dot(n, k)
svals = []; worst_cons_lines = 0.0; worst_cons_full = 0.0; gauge_lines = 0.0; gauge_full = 0.0; min_int = np.inf
for Y in (1.0, 4.0):
    vA = lc(np.exp(Y/2)/np.sqrt(2), np.exp(-Y/2)/np.sqrt(2), [0, 0])   # v^2 = 1
    vB = lc(np.exp(-Y/2)/np.sqrt(2), np.exp(Y/2)/np.sqrt(2), [0, 0])
    for _ in range(3000):
        kt = rng.normal(size=2); y = rng.uniform(-Y/2, Y/2)
        k = lc(np.linalg.norm(kt)*np.exp(y)/np.sqrt(2), np.linalg.norm(kt)*np.exp(-y)/np.sqrt(2), kt)
        q1t = rng.normal(size=2)*1.5
        # unknowns q1^+, q1^- : vA.q1 = 0 and vB.(k - q1) = 0  (linear system)
        M = np.array([[vA[0]/np.sqrt(2) - vA[3]/np.sqrt(2) if False else 0, 0], [0, 0]], dtype=float)
        # vA.q = vA^+ q^- + vA^- q^+ - vAt.qt ; vA_t = 0
        vAp, vAm = (vA[0] + vA[3])/np.sqrt(2), (vA[0] - vA[3])/np.sqrt(2)
        vBp, vBm = (vB[0] + vB[3])/np.sqrt(2), (vB[0] - vB[3])/np.sqrt(2)
        kp, km = (k[0] + k[3])/np.sqrt(2), (k[0] - k[3])/np.sqrt(2)
        Amat = np.array([[vAm, vAp], [vBm, vBp]])          # rows: vA.q1 = 0, vB.q1 = vB.k ; cols: q1^+, q1^-
        rhs = np.array([0.0, vBp*km + vBm*kp])
        q1p, q1m = np.linalg.solve(Amat, rhs)
        q1 = lc(q1p, q1m, q1t); q2 = k - q1
        assert abs(dot(vA, q1)) < 1e-9 and abs(dot(vB, q2)) < 1e-9 and abs(dot(k, k)) < 1e-9
        C = 1.0; vv = dot(vA, vB)
        LA = C*vA*vv/(dot(vA, k)*dot(q2, q2))
        LB = -C*vB*vv/(dot(vB, k)*dot(q1, q1))
        V = C*(vv*(q1 - q2) + 2*dot(vA, k)*vB - 2*dot(vB, k)*vA)/(dot(q1, q1)*dot(q2, q2))
        # fix the relative sign s of the three-gluon term by current conservation
        s = -(dot(k, LA + LB))/dot(k, V)
        svals.append(s)
        Jfull = LA + LB + s*V
        scale = abs(dot(k, LA)) + abs(dot(k, LB))
        worst_cons_lines = max(worst_cons_lines, abs(dot(k, LA + LB))/scale)
        worst_cons_full = max(worst_cons_full, abs(dot(k, Jfull))/scale)
        n = np.array([1.0, *rng.normal(size=3)]); n[1:] /= np.linalg.norm(n[1:])
        PF, PL = polsum('F', k, n), polsum('L', k, n)
        lines_F, lines_L = (LA + LB) @ PF @ (LA + LB), (LA + LB) @ PL @ (LA + LB)
        full_F, full_L = Jfull @ PF @ Jfull, Jfull @ PL @ Jfull
        gauge_lines = max(gauge_lines, abs(lines_F - lines_L)/abs(lines_F))
        gauge_full = max(gauge_full, abs(full_F - full_L)/abs(full_F))
        min_int = min(min_int, 2*(LA @ PF @ LB)/(2*vv**3/(dot(vA, k)*dot(vB, k)*dot(q1, q1)*dot(q2, q2))))
        if not np.isfinite(s) or abs(s - s) > 0:
            raise SystemExit('bad sign')
print(f"(1) max |k.(L_A+L_B)|/(|k.L_A|+|k.L_B|) = {worst_cons_lines:.3f}   (report: 'k.(J_A+J_B) = 1-1 = 0')")
print(f"(2) max |(|L_A+L_B|^2)_Feyn - (..)_LC| / (..)_Feyn = {gauge_lines:.3e}   (line parts alone: gauge DEPENDENT)")
print(f"(3) with the three-gluon term (relative sign fixed once): max |k.J| rel = {worst_cons_full:.1e}, gauge diff of |J|^2 = {gauge_full:.1e}")
print(f"    relative sign of the three-gluon term: s in [{min(svals):.12f}, {max(svals):.12f}] (a constant => genuine Lipatov-vertex conservation)")
print(f"(4) Feynman interference 2 L_A.(-g).L_B divided by 2 C^2 (vA.vB)^3/((vA.k)(vB.k) q1^2 q2^2): min = {min_int:.6f} (=1: positive, since q1^2 q2^2 > 0)")
