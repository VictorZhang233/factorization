"""
W07 / Ch7 -- s1_kinematics.py
Writer-derived checks for sec:dis-kinematics (def:dis-kinematics, prop:dis-W-structure):
 (1) DIS cross section from the lepton tensor (massive target), and its M->0 form;
 (2) positivity projections eps_T eps_T W = F_1, 2x eps_L eps_L W = F_L with F_L=(1+4M^2x^2/Q^2)F_2-2xF_1;
 (3) both-sided current conservation excludes the antisymmetric structure P^mu q^nu - q^mu P^nu;
 (4) support: (P+q)^2 = M^2 + Q^2 (1-x)/x ;  (P-q)^2 < M^2 in the physical region (u-channel term of the commutator absent).
Conventions: metric (+,-,-,-); W^{mu nu} = (-g+qq/q^2) F1 + Pt Pt F2/(P.q), Pt = P - (P.q/q^2) q  (VF-CONV-13).
Run: python3 -I s1_kinematics.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

ok_all = True
def check(name, expr):
    global ok_all
    e = sp.simplify(expr)
    ok = (e == 0)
    ok_all &= ok
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"   residual = {e}"))

g = sp.diag(1, -1, -1, -1)
def dot(a, b):
    return sum(g[i, i] * a[i] * b[i] for i in range(4))

# ---------------------------------------------------------------- (1) cross section, target rest frame
print("(1) cross section from the lepton tensor (target rest frame, massless leptons)")
M, E, Ep, th = sp.symbols('M E Eprime theta', positive=True)
F1, F2 = sp.symbols('F1 F2')
P = sp.Matrix([M, 0, 0, 0])
l = sp.Matrix([E, 0, 0, E])
lp = sp.Matrix([Ep, Ep * sp.sin(th), 0, Ep * sp.cos(th)])
q = l - lp
q2 = sp.simplify(dot(q, q))
Q2 = -q2
Pq = dot(P, q)
x = Q2 / (2 * Pq)
y = Pq / dot(P, l)
Pt = P - (Pq / q2) * q
def W(mu, nu):
    return (-g[mu, nu] + q[mu] * q[nu] / q2 * 1) * F1 + Pt[mu] * Pt[nu] * F2 / Pq
# lowered-index helper
def low(v):
    return sp.Matrix([g[i, i] * v[i] for i in range(4)])
lL, lpL = low(l), low(lp)
# L_{mu nu} = 2 (l_mu l'_nu + l'_mu l_nu - g_{mu nu} l.l')   (spin averaged, massless)
def L(mu, nu):
    return 2 * (lL[mu] * lpL[nu] + lpL[mu] * lL[nu] - g[mu, nu] * dot(l, lp))
LW = sp.simplify(sum(L(m, n) * W(m, n) for m in range(4) for n in range(4)))
# d sigma/dx dQ^2 = (pi alpha^2 / (2 M^2 E^2 Q^2 x^2)) L_{mu nu} W^{mu nu}   (derivation in the chapter)
alpha = sp.symbols('alpha', positive=True)
dsig = sp.pi * alpha**2 / (2 * M**2 * E**2 * Q2 * x**2) * LW
target = 4 * sp.pi * alpha**2 / (x * Q2**2) * (x * y**2 * F1 + (1 - y - x**2 * y**2 * M**2 / Q2) * F2)
check("d^2sigma/dx dQ^2 = 4 pi a^2/(x Q^4) [x y^2 F1 + (1-y-x^2y^2M^2/Q^2) F2]", dsig - target)
# Jacobian d^3l'/(2E') = pi Q^2/(4 M E x^2) dQ^2 dx  (azimuthal integral done)
Q2s, nus, cth = sp.symbols('Q2s nus cth', positive=True)
J = sp.Matrix([[sp.diff(2 * E * Ep * (1 - cth), Ep), sp.diff(2 * E * Ep * (1 - cth), cth)],
               [sp.diff(E - Ep, Ep), sp.diff(E - Ep, cth)]]).det()
check("|d(Q^2,nu)/d(E',cos th)| = 2 E E'", sp.Abs(J) - 2 * E * Ep)
# massless limit with F_L = F2 - 2x F1
FL = sp.symbols('FL')
xs, ys, Qs = sp.symbols('x y Q2', positive=True)
lhs = 4 * sp.pi * alpha**2 / (xs * Qs**2) * (xs * ys**2 * (F2 - FL) / (2 * xs) + (1 - ys) * F2)
rhs = 2 * sp.pi * alpha**2 / (xs * Qs**2) * ((1 + (1 - ys)**2) * F2 - ys**2 * FL)
check("M->0: = 2 pi a^2/(x Q^4)[(1+(1-y)^2) F2 - y^2 F_L]", lhs - rhs)

# ---------------------------------------------------------------- (2) positivity projections
print("(2) photon polarization projections (massive target, general frame)")
Mm, Qq, xx = sp.symbols('M Q x', positive=True)
# choose frame: P at rest, q along z: q = (nu, 0,0, sqrt(nu^2+Q^2)), nu = Q^2/(2 M x)
nu = Qq**2 / (2 * Mm * xx)
Pv = sp.Matrix([Mm, 0, 0, 0])
qv = sp.Matrix([nu, 0, 0, sp.sqrt(nu**2 + Qq**2)])
qq2 = sp.simplify(dot(qv, qv))
Pqv = dot(Pv, qv)
Ptv = Pv - (Pqv / qq2) * qv
def Wv(mu, nu_):
    return (-g[mu, nu_] + qv[mu] * qv[nu_] / qq2) * F1 + Ptv[mu] * Ptv[nu_] * F2 / Pqv
epsT = sp.Matrix([0, 1, 0, 0])
Pt2 = sp.simplify(dot(Ptv, Ptv))
epsL = Ptv / sp.sqrt(Pt2)
def contract(a, b):
    aL, bL = low(a), low(b)
    return sp.simplify(sum(aL[m] * Wv(m, n) * bL[n] for m in range(4) for n in range(4)))
check("eps_T . q = eps_T . P = 0", dot(epsT, qv) + dot(epsT, Pv))
check("eps_L . q = 0, eps_L^2 = +1", sp.simplify(dot(epsL, qv)) + sp.simplify(dot(epsL, epsL) - 1))
check("eps_T eps_T W = F1", contract(epsT, epsT) - F1)
FLm = (1 + 4 * Mm**2 * xx**2 / Qq**2) * F2 - 2 * xx * F1
check("2x eps_L eps_L W = F_L = (1+4M^2x^2/Q^2) F2 - 2x F1", 2 * xx * contract(epsL, epsL) - FLm)
check("Pt^2 = M^2 + (P.q)^2/Q^2", Pt2 - (Mm**2 + Pqv**2 / Qq**2))
# F2 >= 0 follows: rho^2 F2 = F_L + 2x F1
print("   (F_1>=0, F_L>=0 => rho^2 F_2 = F_L + 2x F_1 >= 0 => F_2 >= 0)")

# ---------------------------------------------------------------- (3) conservation excludes the antisymmetric structure
print("(3) general rank-2 tensor from g, P, q with both-sided conservation")
A_, B_, C_, D_, Ea = sp.symbols('A B C D E_a')
# generic numeric-free check with symbolic invariants: write W = A g + B PP + C qq + D(Pq+qP) + E(Pq-qP)
Pq_s, q2_s, M2_s = sp.symbols('Pq q2 M2')
# coefficients of P^nu and q^nu in q_mu W^{mu nu} and W^{mu nu} q_nu:
left = {'P': B_ * Pq_s + D_ * q2_s - Ea * q2_s, 'q': A_ + C_ * q2_s + D_ * Pq_s + Ea * Pq_s}
right = {'P': B_ * Pq_s + D_ * q2_s + Ea * q2_s, 'q': A_ + C_ * q2_s + D_ * Pq_s - Ea * Pq_s}
sol = sp.solve([left['P'], left['q'], right['P'], right['q']], [A_, C_, D_, Ea], dict=True)
print("   solution:", sol)
check("E (antisymmetric (P q - q P) coefficient) = 0", sol[0][Ea])
# remaining two structures reproduce the F1,F2 decomposition: A = -F1 + ..., check rank
print("   remaining free parameters: B and (A,C,D) fixed => two invariant amplitudes (F1, F2)")

# ---------------------------------------------------------------- (4) support
print("(4) support of W")
xS, QS, MS = sp.symbols('x Q M', positive=True)
Pq_ = QS**2 / (2 * xS)
check("(P+q)^2 = M^2 + Q^2 (1-x)/x", MS**2 + 2 * Pq_ - QS**2 - (MS**2 + QS**2 * (1 - xS) / xS))
check("(P-q)^2 = M^2 - Q^2 (1+x)/x  (< M^2 for x>0)", MS**2 - 2 * Pq_ - QS**2 - (MS**2 - QS**2 * (1 + xS) / xS))

print("ALL PASS" if ok_all else "SOME CHECKS FAILED")
