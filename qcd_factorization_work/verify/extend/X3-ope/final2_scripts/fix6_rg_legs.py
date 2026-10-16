"""
fix6_rg_legs.py  (X3 final2, Fix 6(a): Theorem A (A5) step 3 with renormalized elementary legs)

Symbolic check of
    sum_j gamma_ij G_[O_j];Phi = - Dhat G_[O_i];Phi + (sum_{phi in Phi} gamma_phi) G_[O_i];Phi,
where
    G_[O_i];Phi = prod_{phi in Phi} Z_phi^{1/2} sum_j Z_ij G^bare_{O_j;Phi}   (amputation with renormalized propagators),
    gamma = -(Dhat Z) Z^{-1},   gamma_phi = (1/2) Dhat ln Z_phi,   Dhat G^bare = 0  (total mu-derivative at fixed bare
    parameters; here Dhat = d/d ln mu acting on the explicit mu-dependence of Z, Z_phi).
Generic 3x3 mixing matrix Z(t), two legs with Z_1(t), Z_2(t), t = ln mu; G^bare constant.
Also checks the amputation factor: G_R^amp = prod Z_phi^{+1/2} Z G^bare,amp, from
    G_R^nonamp = prod Z_phi^{-1/2} Z G^bare,nonamp  and  Delta_R = Z_phi^{-1} Delta_0.
Run: python3 -I fix6_rg_legs.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

t = sp.symbols('t')
n = 3
Z = sp.Matrix(n, n, lambda i, j: sp.Function('Z%d%d' % (i, j))(t))
z1, z2 = sp.Function('z1')(t), sp.Function('z2')(t)
Gb = sp.Matrix(n, 1, lambda i, j: sp.Symbol('Gb%d' % i))          # bare amputated Green functions (mu-independent)

GR = sp.sqrt(z1 * z2) * Z * Gb                                      # renormalized amputated Green functions
gamma = -(Z.diff(t)) * Z.inv()                                      # operator anomalous-dimension matrix
g1 = sp.Rational(1, 2) * sp.diff(sp.log(z1), t)
g2 = sp.Rational(1, 2) * sp.diff(sp.log(z2), t)

lhs = gamma * GR
rhs = -GR.diff(t) + (g1 + g2) * GR
res = sp.simplify(lhs - rhs)
ok1 = all(sp.simplify(e) == 0 for e in res)
print("(1) sum_j gamma_ij G_j = -Dhat G_i + (gamma_phi1 + gamma_phi2) G_i  (generic 3x3 Z, two legs):", ok1)

# (2) amputation factor
D01, D02 = sp.symbols('Delta01 Delta02')                            # bare full propagators of the two legs
Gb_non = Gb * D01 * D02                                             # bare non-amputated = bare amputated x propagators
GR_non = Z * Gb_non / sp.sqrt(z1 * z2)                               # phi_0 = z^{1/2} phi_R  =>  <..phi_R..> = z^{-1/2} <..phi_0..>
DR1, DR2 = D01 / z1, D02 / z2                                       # renormalized propagators
GR_amp = GR_non / (DR1 * DR2)
ok2 = all(sp.simplify(e) == 0 for e in (GR_amp - GR))
print("(2) amputation with renormalized propagators gives prod Z_phi^{+1/2} Z G^bare,amp:", ok2)
print("RESULT:", "PASS" if (ok1 and ok2) else "FAIL")
