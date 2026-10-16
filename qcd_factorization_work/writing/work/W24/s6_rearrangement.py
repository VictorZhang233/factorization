#!/usr/bin/env python3
"""W24 / Ch21 -- prop:power-rearrangement (OPE basis rearrangement) and the endpoint toy of sec:power-nlp.

(A) Rearrangement: operators O_i of dimension d_i (finite tower d_i <= N), coefficients Ct_i(q).
    O'_i = O_i + sum_{d_j<d_i} kappa_ij Lambda^{d_i-d_j} O_j  (triangular, unipotent)  ==>
    Ct'_j = Ct_j - sum_{d_i>d_j} Ct'_i kappa_ij Lambda^{d_i-d_j}   (solved top-down), and
    sum_i Ct'_i <O'_i> = sum_i Ct_i <O_i> exactly (identical remainder).
    Growth: |Ct'_j| <= K' |q|^{2-d_j} ln^k |q| for |q| >= Lambda.
(B) Rearranging only twist >= 4 changes twist-2 coefficients by terms ~ Lambda^2/Q^2 = e^{-4pi/(beta0 alpha(Q))}
    (one loop) = o(alpha^K) for all K.
(C) Endpoint toy: A(rho) = int_rho^1 dz/z ln(z/rho) = (1/2) ln^2(1/rho); the integrand expanded at fixed z
    (rho -> 0 first) is (1/z)(ln z + ln(1/rho)), whose integral over [0,1] diverges at z -> 0 (endpoint divergence);
    with an analytic regulator z^eta: int_0^1 dz z^{-1+eta}(ln z + L) = -1/eta^2 + L/eta (poles that must cancel
    against a separate 'soft' term), and int_0^rho dz z^{-1+eta}(...) supplies them.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import random

OK = True
def check(name, cond):
    global OK
    print(("PASS " if cond else "FAIL ") + name)
    OK = OK and bool(cond)

# ---- (A) exact rational test, dimensions 0,2,4,6,8 (two operators of dimension 4) ----
random.seed(7)
q, Lam = sp.symbols('q Lambda', positive=True)
dims = [0, 2, 4, 4, 6, 8]
nO = len(dims)
c = [sp.Rational(random.randint(1, 9), random.randint(1, 9)) for _ in range(nO)]
Ct = [c[i]*q**(2 - dims[i]) for i in range(nO)]
O = [sp.Symbol(f'o{i}') for i in range(nO)]                 # vacuum/hadronic matrix elements <O_i>
kappa = {}
for i in range(nO):
    for j in range(nO):
        if dims[j] < dims[i]:
            kappa[(i, j)] = sp.Rational(random.randint(-5, 5), random.randint(1, 4))
Op = [O[i] + sum(kappa[(i, j)]*Lam**(dims[i]-dims[j])*O[j] for j in range(nO) if dims[j] < dims[i]) for i in range(nO)]
# solve top-down
order = sorted(range(nO), key=lambda i: -dims[i])
Ctp = [None]*nO
for j in order:
    Ctp[j] = Ct[j] - sum(Ctp[i]*kappa[(i, j)]*Lam**(dims[i]-dims[j]) for i in range(nO) if dims[i] > dims[j])
lhs = sp.expand(sum(Ctp[i]*Op[i] for i in range(nO)))
rhs = sp.expand(sum(Ct[i]*O[i] for i in range(nO)))
check("(A) sum_i Ct'_i <O'_i> = sum_i Ct_i <O_i> exactly (top-down solution)", sp.simplify(lhs - rhs) == 0)
# top level unchanged; growth: Ct'_j q^{d_j-2} = c_j + O(Lambda/q)
check("(A) highest-dimension coefficients unchanged", all(sp.simplify(Ctp[i] - Ct[i]) == 0 for i in range(nO) if dims[i] == max(dims)))
okg = True
for j in range(nO):
    lead = sp.limit(sp.expand(Ctp[j]*q**(dims[j]-2)), q, sp.oo)
    okg &= sp.simplify(lead - c[j]) == 0
check("(A) growth bound: Ct'_j q^{d_j-2} -> c_j as q -> oo (corrections O(Lambda/q)^{2})", okg)
# relative change of the dimension-0 (unit-operator) and dimension-2 coefficients is O(Lambda^2/q^2):
for j in range(nO):
    rel = sp.simplify((Ctp[j] - Ct[j])/Ct[j])
    print(f"   d={dims[j]}: relative change of coefficient = {sp.factor(rel)}")

# ---- (B) Lambda^2/Q^2 in terms of alpha(Q) at one loop and o(alpha^K) ----
al, b0 = sp.symbols('alpha beta0', positive=True)
expr = sp.exp(-4*sp.pi/(b0*al))
check("(B) Lambda^2/Q^2 = exp(-4 pi/(beta0 alpha(Q))) is o(alpha^K): limit of ratio = 0 for K=1,10",
      all(sp.limit(expr/al**K, al, 0, '+') == 0 for K in [1, 10]))

# ---- (C) endpoint toy ----
z, rho, eta = sp.symbols('z rho eta', positive=True)
A = sp.integrate(sp.log(z/rho)/z, (z, rho, 1))
check("(C1) int_rho^1 dz/z ln(z/rho) = (1/2) ln^2 rho", sp.simplify(A - sp.log(rho)**2/2) == 0)
L = sp.symbols('L', positive=True)  # L = ln(1/rho)
reg_hc = sp.integrate(z**(-1+eta)*(sp.log(z) + L), (z, 0, 1), conds='none')
print("   regulated 'collinear' term int_0^1 z^{-1+eta}(ln z + L) =", sp.simplify(reg_hc))
check("(C2) analytic regulator: = -1/eta^2 + L/eta (pure poles, from the endpoint z -> 0)", sp.simplify(reg_hc - (-1/eta**2 + L/eta)) == 0)
# 'soft' term: the region z < rho, where the true integrand vanishes; with the regulator the expanded integrand integrated
# over [0, rho] (to be subtracted) gives the compensating poles:
reg_soft = sp.integrate(z**(-1+eta)*(sp.log(z) + L), (z, 0, sp.exp(-L)), conds='none')
tot = sp.simplify(sp.series(reg_hc - reg_soft, eta, 0, 1).removeO())
print("   difference (collinear minus endpoint region) as eta -> 0:", tot)
check("(C3) poles cancel between the two terms and the finite part is L^2/2", sp.simplify(tot - L**2/2) == 0)
print("ALL PASS" if OK else "SOME CHECKS FAILED")
