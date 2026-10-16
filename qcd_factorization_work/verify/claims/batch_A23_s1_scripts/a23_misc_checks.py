#!/usr/bin/env python3
"""Small algebraic checks used in batch A23 (stage 1).

(1) A24 item 9: Gottfried sum in the quark-parton model with isospin symmetry,
    S_G = int_0^1 dx (F2p - F2n)/x = 1/3 + (2/3) int_0^1 (ubar - dbar) dx,
    so S_G = 1/3 requires int (ubar - dbar) = 0 (flavour-symmetric light sea); NMC 1991: 0.240(16).
(2) A23 item 20: MVV hep-ph/0504242 eq. (4.4), c^(1)_{2,g} = n_f{(2-4x x1)(L1-L0) - 2 + 16 x x1}
    (a_s = alpha_s/4pi, singlet normalisation) equals 2 x 2 x T_F[(x^2+(1-x)^2)ln((1-x)/x) - 1 + 8x(1-x)]
    per flavour, i.e. the 'standard' C_g of the project (q and qbar each, alpha_s/2pi, T_F = 1/2).
(3) A23 item 19: Collins (12.38)/(12.40) prefactor z^{n-3} with n = 4 - 2 eps equals z^{1-2 eps}.
Run: python3 -I a23_misc_checks.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

ok = True
# (1) Gottfried
uv, dv, ub, db, s_ = sp.symbols('u_v d_v ubar dbar s')   # stand for first moments int dx q(x)
# F2/x = sum e_q^2 (q + qbar); proton: u = uv + ub, d = dv + db, s = sbar = s
F2p_over_x = sp.Rational(4, 9)*(uv + 2*ub) + sp.Rational(1, 9)*(dv + 2*db) + sp.Rational(1, 9)*2*s_
# neutron by isospin: u <-> d
F2n_over_x = sp.Rational(4, 9)*(dv + 2*db) + sp.Rational(1, 9)*(uv + 2*ub) + sp.Rational(1, 9)*2*s_
SG = sp.expand((F2p_over_x - F2n_over_x).subs({uv: 2, dv: 1}))
target = sp.Rational(1, 3) + sp.Rational(2, 3)*(ub - db)
print("(1) S_G =", SG, "; equals 1/3 + (2/3)(ubar-dbar):", sp.simplify(SG - target) == 0)
ok &= sp.simplify(SG - target) == 0
print("    NMC 1991: S_G = 0.240 +- 0.016  =>  int(ubar - dbar) =", (0.240 - 1/3)*1.5, "+-", 0.016*1.5)

# (2) MVV normalisation of the one-loop gluon coefficient function
x = sp.symbols('x', positive=True)
L0, L1 = sp.log(x), sp.log(1 - x)
mvv = (2 - 4*x*(1 - x))*(L1 - L0) - 2 + 16*x*(1 - x)        # per n_f, a_s = alpha_s/(4 pi)
TF = sp.Rational(1, 2)
Cg = TF*((x**2 + (1 - x)**2)*(L1 - L0) - 1 + 8*x*(1 - x))   # per flavour per (q or qbar), alpha_s/(2 pi)
conv = 2*(2*Cg)        # q and qbar (x2); alpha_s/2pi = 2 a_s (x2)
print("(2) MVV c(1)_{2,g}/n_f - 4 C_g =", sp.simplify(sp.expand(mvv - conv)))
ok &= sp.simplify(sp.expand(mvv - conv)) == 0

# (3) z^{n-3}
eps, z = sp.symbols('epsilon z', positive=True)
n = 4 - 2*eps
print("(3) z^(n-3) with n=4-2eps:", sp.simplify(z**(n - 3)), "; equals z^(1-2eps):", sp.simplify(z**(n - 3) - z**(1 - 2*eps)) == 0)
ok &= sp.simplify(z**(n - 3) - z**(1 - 2*eps)) == 0
print("RESULT:", "PASS" if ok else "FAIL")
