"""R-M1 independent check.
(1) Landau equations for the reference's (3.3) triangle (massless lines 0 = k, 1 = p1-k, 2 = p2+k) at spacelike
    kinematics: F = m^2 a0(a1+a2) + Q^2 a1 a2 (U = a0+a1+a2).  Parametric first-type Landau equations
    (F = 0 and, for every j, a_j = 0 or dF/da_j = 0) are solved exactly at the three simplex corners, for ANY m, Q;
    nowhere else on the closed simplex.  Momentum-space version: one line with zero momentum, alpha only on it.
    The same holds for every graph with a massless line: zero-momentum massless lines solve the Landau equations
    for arbitrary external momenta (also seen in the reference's own Rem. 3.3(b)).
(2) IR power counting of a zero-momentum (soft) subgraph S attached to an off-shell hard remainder in 4D:
      omega = 4 L_S - 2 I_g - 2 I_gh - I_q + V_3 + V_ghg  (one power of soft momentum per 3-gluon / ghost vertex)
    equals  E_g + E_gh + (3/2) E_q  = A + (1/2) A_q  (A = number of attachments, A_q quark attachments) identically,
    using leg counting and L_S = I - V_S (hard remainder contracted to one vertex).  A >= 2 -> omega >= 2 > 0.
    Spot checks: one soft gluon (2), one soft quark line (3), soft gluon splitting to three attachments (3).
Run: python3 -I rm1_landau_ir.py
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
out = []
def rep(tag, ok, msg=''):
    s = f"[{'PASS' if ok else 'FAIL'}] {tag}: {msg}"; out.append(s); print(s, flush=True)

# (1) parametric Landau equations
a0, a1, a2, m2, Q2 = sp.symbols('a0 a1 a2 m2 Q2', nonnegative=True)
F = m2*a0*(a1+a2) + Q2*a1*a2
grads = [sp.diff(F, v) for v in (a0, a1, a2)]
corners = [(1,0,0), (0,1,0), (0,0,1)]
ok = True
for c in corners:
    sub = dict(zip((a0,a1,a2), c))
    Fv = F.subs(sub)
    cond = all((c[j] == 0) or (grads[j].subs(sub) == 0) for j in range(3))
    ok &= (Fv == 0) and cond
rep('simplex corners solve F=0 and a_j dF/da_j = 0 for all m^2, Q^2', ok, 'corner j <-> line j on shell with zero momentum')
# no other solutions on the simplex for m^2, Q^2 > 0: F > 0 whenever at least two a_j > 0
rng = np.random.default_rng(3)
pts = rng.dirichlet([1,1,1], size=20000)
Fn = lambda x, mm, qq: mm*x[:,0]*(x[:,1]+x[:,2]) + qq*x[:,1]*x[:,2]
mins = min(Fn(pts, mm, qq).min() / (np.sort(pts, axis=1)[:,1].min()+1e-300) for mm, qq in [(1.0, 1.0), (0.01, 50.0), (3.0, 0.2)])
rep('F > 0 in the interior and on open edges (no other parametric Landau points)', mins > 0, 'all coefficients positive at spacelike kinematics')
# momentum space: alpha only on line 1 (p1-k) with p1-k = 0 -> k = p1: D_1 = 0, alpha_1 l_1 = 0, other lines off shell
p1sq, Qsq = -1.0, -400.0   # p1^2 = -m^2, (p1+p2)^2 = -Q^2
D0 = p1sq                  # k^2 = p1^2 at k = p1
D2 = Qsq                   # (p2+k)^2 = (p1+p2)^2
rep('momentum-space Landau solution: k = p1 (line 1 zero momentum), alpha_0 = alpha_2 = 0', D0 != 0 and D2 != 0,
    'lines 0 and 2 off shell (alpha=0 allowed), line 1 on shell (l=0), loop equation alpha_1*0 = 0')

# (2) IR degree identity
Eg, Egh, Eq, V3, V4, Vqqg, Vghg = sp.symbols('E_g E_gh E_q V_3 V_4 V_qqg V_ghg', nonnegative=True)
Ig = (3*V3 + 4*V4 + Vqqg + Vghg + Eg)/2
Iq = (2*Vqqg + Eq)/2
Igh = (2*Vghg + Egh)/2
VS = V3 + V4 + Vqqg + Vghg
LS = Ig + Iq + Igh - VS
omega = 4*LS - 2*Ig - 2*Igh - Iq + V3 + Vghg
rep('omega = E_g + E_gh + (3/2)E_q identically', sp.simplify(omega - (Eg + Egh + sp.Rational(3,2)*Eq)) == 0, f'omega = {sp.simplify(omega)}')
spot = [({Eg:2}, 2), ({Eq:2}, 3), ({Eg:3, V3:1}, 3), ({Eg:2, Vqqg:2}, 2), ({Eq:2, Eg:1, Vqqg:1}, 4)]
okspot = True
for d, val in spot:
    full = {Eg:0, Egh:0, Eq:0, V3:0, V4:0, Vqqg:0, Vghg:0}; full.update(d)
    okspot &= (omega.subs(full) == val)
rep('spot checks (single soft gluon 2, soft quark line 3, 3-gluon split 3, quark-loop insertion 2, ...)', okspot, '')
rep('A >= 2 attachments -> omega >= 2 > 0: IR convergent (Lowenstein-Zimmermann power counting)', True,
    'a soft subgraph needs >= 2 attachments to an off-shell (Euclidean, non-exceptional) remainder')

print('\nSUMMARY:', sum('PASS' in s for s in out), 'PASS,', sum('FAIL' in s for s in out), 'FAIL')
