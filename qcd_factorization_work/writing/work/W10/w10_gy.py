"""
W10 / Ch9 sec:method-gy and App F sec:appF-gy -- Grammer-Yennie K/G decompositions (book conventions):
  collinear: g_{mu nu} = K_{mu nu} + G_{mu nu}, K_{mu nu} = k_mu nB_nu/(k.nB - i0)  (mu on H, nu on the A-collinear C)
  soft:      K_s^{mu nu} = k^mu nA^nu/(nA.k +- i0)   (mu on the A jet J, nu on the soft subgraph S)
 (1) algebra (sympy): G k = 0 ; H.G.C = H.(C - C^+ k/k^+) ; J.K_s.S = (J.k) S^-/k^- ;
     J.G_s.S = J^- S^+ - J_T.S_T - (J^- k^+ - J_T.k_T) S^-/k^- ; gluon-PDF identity if H.k = 0
 (2) numerical power counting table (own kinematics, explicit Dirac matrices):
     (a) one-loop DIS vertex integrand, gluon collinear to the target quark: |G term|/|full| for an on-shell massless
         parent (expect lambda^2) and for an off-shell parent with a generic spinor (expect lambda^1)
     (b) soft gluon on an outgoing A-collinear quark: |J.G_s.S|/|J.S| in the soft region (expect lambda) and in the
         Glauber region (expect O(1))
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import sympy as sp
from w10_dirac import *

npass = 0; nfail = 0
def check(name, ok, info=''):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(('[PASS] ' if ok else '[FAIL] ') + name + ((' : ' + str(info)) if info != '' else ''))

# (1) algebra in light-front components (plus, minus, T1, T2)
def dot(a, b): return a[0]*b[1] + a[1]*b[0] - a[2]*b[2] - a[3]*b[3]
kp, km, k1, k2 = sp.symbols('kp km k1 k2')
H = sp.symbols('Hp Hm H1 H2'); C = sp.symbols('Cp Cm C1 C2'); J = sp.symbols('Jp Jm J1 J2'); Sv = sp.symbols('Sp Sm S1 S2')
k = (kp, km, k1, k2); nB = (0, 1, 0, 0); nA = (1, 0, 0, 0)
HKC = dot(H, k)*dot(nB, C)/dot(k, nB)
HGC = dot(H, C) - HKC
check('(1) nB.C = C^+, nA.C = C^-', dot(nB, C) == C[0] and dot(nA, C) == C[1])
check('(1) G_{mu nu} k^nu = 0', sp.simplify(HGC.subs(dict(zip(C, k)))) == 0)
check('(1) H.G.C = H.(C - (C^+/k^+) k)', sp.simplify(HGC - dot(H, tuple(C[i] - C[0]/kp*k[i] for i in range(4)))) == 0)
JKS = dot(J, k)*dot(nA, Sv)/dot(nA, k)
JGS = dot(J, Sv) - JKS
check('(1) J.K_s.S = (J.k) S^-/k^-', sp.simplify(JKS - dot(J, k)*Sv[1]/km) == 0)
check('(1) J.G_s.S = J^- S^+ - J_T.S_T - (J^- k^+ - J_T.k_T) S^-/k^-',
      sp.simplify(JGS - (J[1]*Sv[0] - J[2]*Sv[2] - J[3]*Sv[3] - (J[1]*kp - J[2]*k1 - J[3]*k2)*Sv[1]/km)) == 0)
check('(1) eikonal current J ~ nA (J^- = J_T = 0) is annihilated by G_s', sp.simplify(JGS.subs({J[1]: 0, J[2]: 0, J[3]: 0})) == 0)
Hm_sol = sp.solve(sp.Eq(dot(H, k), 0), H[1])[0]
lhs = dot(H, C).subs(H[1], Hm_sol)
rhs = H[0]*(C[1] - km/kp*C[0]) - H[2]*(C[2] - k1/kp*C[0]) - H[3]*(C[3] - k2/kp*C[0])
check('(1) if H.k = 0: H.C = H^+(C^- - (k^-/k^+)C^+) - H_T.(C_T - (k_T/k^+)C^+)', sp.simplify(lhs - rhs) == 0)

# (2a) one-loop DIS vertex integrand, collinear region
Pp_, Qv = 2.0, 3.0
P = lc(Pp_, 0.0)
q = lc(-Pp_, Qv**2/(2*Pp_))
pp = P + q
check('(2a) p\' = P + q on shell (x = 1)', abs(mdot(pp, pp)) < 1e-12)
epsg = np.array([0.3, 0.8, -0.5, 0.2], dtype=complex)      # photon polarization (generic)
up = u_spinors(pp)[0]; ub = bar(up)
uP = u_spinors(P)[0]
rng = np.random.default_rng(5)
psi = rng.normal(size=4) + 1j*rng.normal(size=4)
def contraction(kvec, parent_mom, parent_spinor):
    Hmu = [ub @ (1j*GAM[mu]) @ S(pp - kvec) @ slash(epsg) for mu in range(4)]        # row vectors
    Cnu = [S(parent_mom - kvec) @ (1j*GAM[nu]) @ parent_spinor for nu in range(4)]    # columns
    HC = sum(ETA[mu, mu]*(Hmu[mu] @ Cnu[mu]) for mu in range(4))
    Hk = sum(ETA[mu, mu]*kvec[mu]*Hmu[mu] for mu in range(4))   # H.k (row)
    Cplus = (Cnu[0] + Cnu[3])/np.sqrt(2)                        # n_B . C = C^+  (upper components -> plus)
    K = (Hk @ Cplus)/plus(kvec)
    return HC, K, HC - K
rows = []
lams = [1e-2, 1e-3, 1e-4]
chi = rng.normal(size=4) + 1j*rng.normal(size=4)
eps_T = np.array([0, 1.0, 0, 0], dtype=complex)
for label, parent, epsg in [('on-shell massless parent, transverse photon', 'on', eps_T),
                            ('on-shell massless parent, generic eps', 'on', np.array([0.3, 0.8, -0.5, 0.2], dtype=complex)),
                            ('off-shell parent, generic spinor, transv.', 'off', eps_T)]:
    vals = []
    for lam in lams:
        kvec = lc(0.3*Pp_, 0.4*lam**2, 0.5*lam, -0.2*lam)
        num = 0.0; den = 0.0
        for upp in u_spinors(pp):
            ub_ = bar(upp)
            if parent == 'on':
                spinors = u_spinors(P); par = P
            else:
                par = lc(Pp_, 0.7*lam**2, 0.3*lam, 0.1*lam)
                spinors = [chi]
            for sp_ in spinors:
                Hmu = [ub_ @ (1j*GAM[mu]) @ S(pp - kvec) @ slash(epsg) for mu in range(4)]
                Cnu = [S(par - kvec) @ (1j*GAM[nu]) @ sp_ for nu in range(4)]
                HC = sum(ETA[mu, mu]*(Hmu[mu] @ Cnu[mu]) for mu in range(4))
                Hk = sum(ETA[mu, mu]*kvec[mu]*Hmu[mu] for mu in range(4))
                Cplus = (Cnu[0] + Cnu[3])/np.sqrt(2)
                K = (Hk @ Cplus)/plus(kvec)
                num += abs(HC - K)**2; den += abs(HC)**2
        vals.append(np.sqrt(num/den))
    slope = np.log(vals[-1]/vals[0])/np.log(lams[-1]/lams[0])
    rows.append((label, vals, slope))
    print('    collinear, %-44s |G|/|full| = %s ; slope %.3f' % (label, ', '.join('%.3e' % v for v in vals), slope))
check('(2a) on-shell massless parent, physical transverse photon: G term ~ lambda^2', abs(rows[0][2] - 2) < 0.02, '%.3f' % rows[0][2])
check('(2a) on-shell massless parent, generic (unphysical) photon polarization: G term ~ lambda^1', abs(rows[1][2] - 1) < 0.02, '%.3f' % rows[1][2])
check('(2a) off-shell parent with a generic spinor: G term ~ lambda^1', abs(rows[2][2] - 1) < 0.02, '%.3f' % rows[2][2])

# (2b) soft attachment to an outgoing A-collinear quark: J^mu = ubar(p) gamma^mu S(p - k) Y (k flows into the line)
Y = rng.normal(size=4) + 1j*rng.normal(size=4)
Ssoft = rng.normal(size=4) + 1j*rng.normal(size=4)      # generic soft current S^nu (upper components)
def soft_ratio(kvec, lam):
    pT = (0.6*lam, 0.3*lam)
    p = lc(1.0, (pT[0]**2 + pT[1]**2)/2.0, *pT)
    upp = u_spinors(p)[0]; ubp = bar(upp)
    Jmu = np.array([ubp @ GAM[mu] @ S(p - kvec) @ Y for mu in range(4)])
    JS = mdot(Jmu, Ssoft)
    Jk = mdot(Jmu, kvec)
    Sminus = minus(Ssoft)
    JGS = JS - Jk*Sminus/minus(kvec)
    return abs(JGS)/abs(JS)
soft_vals = []; glau_vals = []
lams = [1e-3, 1e-4, 1e-5]
for lam in lams:
    soft_vals.append(soft_ratio(lc(0.7*lam, 0.5*lam, 0.4*lam, -0.3*lam), lam))
    glau_vals.append(soft_ratio(lc(0.7*lam**2, -0.5*lam**2, 0.4*lam, -0.3*lam), lam))
ss = np.log(soft_vals[-1]/soft_vals[0])/np.log(lams[-1]/lams[0])
sg = np.log(glau_vals[-1]/glau_vals[0])/np.log(lams[-1]/lams[0])
print('    soft region    k ~ lam(1,1,1):         |J.G_s.S|/|J.S| = %s ; slope %.3f' % (', '.join('%.3e' % v for v in soft_vals), ss))
print('    Glauber region k ~ (lam^2,lam^2,lam):  |J.G_s.S|/|J.S| = %s ; slope %.3f' % (', '.join('%.3e' % v for v in glau_vals), sg))
check('(2b) soft region: G_s term ~ lambda', abs(ss - 1) < 0.05, '%.3f' % ss)
check('(2b) Glauber region: G_s term O(1) (slope ~ 0)', abs(sg) < 0.05 and glau_vals[-1] > 0.05, '%.3f, plateau %.3f' % (sg, glau_vals[-1]))
print('\n=== w10_gy: %d PASS, %d FAIL ===' % (npass, nfail))
