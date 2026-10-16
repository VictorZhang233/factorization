import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
# (1) Gauge covariance: D = d + i s g A, abelian: psi -> e^{i alpha} psi, A -> A - (s/g) d alpha.
#     Link W = exp(i t g int_0^y dx.A) -> W exp(-i t s (alpha(y)-alpha(0))).
#     psibar(y) W psi(0) invariant  <=>  -alpha(y) - t s (alpha(y)-alpha(0)) + alpha(0) = 0  <=>  t s = -1.
s, t = sp.symbols('s t')
ay, a0 = sp.symbols('alpha_y alpha_0')
phase = -ay - t*s*(ay - a0) + a0
print("invariance condition:", sp.solve(sp.Poly(sp.expand(phase), ay, a0).coeffs(), t))
# light-cone path x=(0^+, eta^-, 0_T): dx.A = d eta^- A^+  ->  IJJSZ exp(-ig int A^+) means t=-1 -> s=+1 (D = d + igA)
# space-like path x = z' e, e=(0,0,0,1): dx.A = dz' A_3 = -dz' A^z -> IJJSZ exp(-ig int A^z) = exp(+ig int dx.A): t=+1 -> s=-1 (D = d - igA)
print("light-cone link exp(-ig int A^+): t=-1 -> s =", sp.solve(-1*s + 1, s))
print("space-like link exp(-ig int A^z): t=+1 -> s =", sp.solve(1*s + 1, s))
# quark-gluon vertex (-i g T^a gamma^mu) <-> L_int = -g psibar A-slash psi <-> D = d + i g A (s=+1)
# (2) the one-loop check of the sail sign is done numerically in e04_sign2.py
