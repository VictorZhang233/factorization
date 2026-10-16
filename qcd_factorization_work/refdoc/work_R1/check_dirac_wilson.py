"""R1 check 2: Dirac light-cone algebra (2.4), support-proof identity, Ward identity (3.15),
eikonal approximation (Fig. 4 caption), Wilson-line first-order Feynman rules (Fig. 4 table vs (2.7)),
and the first-order expansion of U^dagger in the proof of Thm 3.14 (p.25).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp

rng = np.random.default_rng(1)
# Dirac representation
I2 = np.eye(2); Z2 = np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
g0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
gs = [np.block([[Z2, s], [-s, Z2]]) for s in (sx, sy, sz)]
G = [g0] + gs
metric = np.diag([1, -1, -1, -1])
gp = (G[0] + G[3]) / np.sqrt(2); gm = (G[0] - G[3]) / np.sqrt(2)
Pp = 0.5 * gm @ gp; Pm = 0.5 * gp @ gm
ok = lambda A, B: np.allclose(A, B, atol=1e-12)
print("== (2.4) light-cone Dirac algebra ==")
print("(g+)^2=0:", ok(gp @ gp, 0 * gp), " (g-)^2=0:", ok(gm @ gm, 0 * gm), " {g+,g-}=2:", ok(gp @ gm + gm @ gp, 2 * np.eye(4)))
print("P+ projector:", ok(Pp @ Pp, Pp), " P- projector:", ok(Pm @ Pm, Pm), " P++P-=1:", ok(Pp + Pm, np.eye(4)), " P+ hermitian:", ok(Pp, Pp.conj().T))
print("g0 g+ = sqrt2 P+  (support proof):", ok(g0 @ gp, np.sqrt(2) * Pp))

def slash(p):  # p contravariant (p0,p1,p2,p3)
    pl = metric @ p
    return sum(pl[m] * G[m] for m in range(4))

# massless spinor along +z: u satisfies pslash u = 0
E = 3.7; p = np.array([E, 0, 0, E])
w, V = np.linalg.eig(slash(p)); u = V[:, np.argmin(abs(w))]
print("u(p) for p along +z is pure good component (P+ u = u):", ok(Pp @ u, u))
# boost along +z by rapidity y: S = exp(y/2 g0 g3)
y = 0.83
g0g3 = g0 @ G[3]
from scipy.linalg import expm  # may be unavailable
S = expm(0.5 * y * g0g3)
# check S is the spinor boost: S^-1 g^mu S = Lambda^mu_nu g^nu with Lambda boost along +z rapidity y
Lam = np.eye(4); ch, sh = np.cosh(y), np.sinh(y)
Lam[0, 0] = ch; Lam[0, 3] = sh; Lam[3, 0] = sh; Lam[3, 3] = ch
Sinv = np.linalg.inv(S)
print("S = exp(y/2 g0 g3) implements boost along +z:", all(ok(Sinv @ G[m] @ S, sum(Lam[m, n] * G[n] for n in range(4))) for m in range(4)))
# good components scale e^{y/2}, bad e^{-y/2}
psi = rng.normal(size=4) + 1j * rng.normal(size=4)
print("good comps scale e^{+y/2}:", ok(S @ (Pp @ psi), np.exp(y / 2) * (Pp @ psi)), "  bad comps scale e^{-y/2}:", ok(S @ (Pm @ psi), np.exp(-y / 2) * (Pm @ psi)))

print("\n== (3.15) tree Ward identity  i(l+k)/(l+k)^2 (i g kslash t) i l/l^2 = -g t [ i l/l^2 - i(l+k)/(l+k)^2 ] ==")
g = 0.7
for trial in range(3):
    l = rng.normal(size=4); kh = np.array([1.3, 0, 0, 1.3]) * rng.uniform(0.2, 2)   # khat light-like along +z
    sq = lambda v: v @ metric @ v
    lhs = 1j * slash(l + kh) / sq(l + kh) @ (1j * g * slash(kh)) @ (1j * slash(l) / sq(l))
    rhs = -g * (1j * slash(l) / sq(l) - 1j * slash(l + kh) / sq(l + kh))
    print("  trial", trial, ok(lhs, rhs))

print("\n== Fig.4 caption: i(p+k)/((p+k)^2) i g gamma^mu u(p) -> -g p^mu/(p.k) u(p) for soft k ==")
pl = np.array([5.0, 0.3, -0.2, np.sqrt(25 - 0.09 - 0.04)])  # massless
w, V = np.linalg.eig(slash(pl)); up = V[:, np.argmin(abs(w))]
for lam in [1e-2, 1e-3, 1e-4]:
    k = lam * np.array([1.1, 0.4, 0.3, -0.5])
    sq = lambda v: v @ metric @ v
    errs = []
    for mu in range(4):
        exact = 1j * slash(pl + k) / sq(pl + k) @ (1j * g * G[mu]) @ up
        eik = -g * pl[mu] / (pl @ metric @ k) * up
        errs.append(np.linalg.norm(exact - eik) / np.linalg.norm(eik))
    print(f"  lambda={lam:g}: max relative error over mu = {max(errs):.2e}  (should be O(lambda))")

print("\n== Wilson-line first-order Feynman rules (sympy) ==")
lam_, kn, eta = sp.symbols('lambda kn eta', real=True)   # kn = v.k, eta>0 adiabatic regulator
gg = sp.symbols('g', positive=True)
# gluon field mode A(z) ~ e^{-i k.z}: k flows INTO the line at the attachment (absorbed);  k_out = -k
def first_order(sign_exp, lo, hi, damp):
    # coefficient of v.A in  P exp(sign_exp * i g * int_lo^hi dlambda v.A(x+lambda v)),  phase e^{-i lambda kn}
    integrand = sp.exp(-sp.I * lam_ * kn) * damp
    val = sp.integrate(integrand, (lam_, lo, hi), conds='none')
    return sp.simplify(sign_exp * sp.I * gg * val)
res = {}
res["W[x,-inf] = doc W^(-)(x)"] = first_order(+1, -sp.oo, 0, sp.exp(eta * lam_))      # P exp(+ig int_{-inf}^0)
res["W[x,+inf] = doc W^(+)(x)"] = first_order(-1, 0, sp.oo, sp.exp(-eta * lam_))      # P exp(-ig int_0^{inf})
res["W[+inf,x] = doc W^(+)dag(x)"] = first_order(+1, 0, sp.oo, sp.exp(-eta * lam_))   # P exp(+ig int_0^{inf})
res["W[-inf,x] = doc W^(-)dag(x)"] = first_order(-1, -sp.oo, 0, sp.exp(eta * lam_))  # P exp(-ig int_{-inf}^0)
ko = sp.symbols('ko', real=True)  # ko = v.k_out = -kn
for name, val in res.items():
    val_out = sp.simplify(val.subs(kn, -ko))
    # compare with doc rule:  (i g v^mu)(i/(v.k_out +/- i0)) = -g/(v.k_out +/- i eta)
    fut = sp.simplify(val_out - (-gg / (ko + sp.I * eta)))
    pas = sp.simplify(val_out - (-gg / (ko - sp.I * eta)))
    print(f"  {name:32s}: k_in form {sp.simplify(val)} ; k_out form {val_out} ; matches doc future rule: {fut == 0}; doc past rule: {pas == 0}")
# last row of Fig.4: incoming quark absorbing k (k_in) gives -g p^mu/(p.k_in + i0): compare with W[x,-inf] in k_in form
print("  Fig.4 last row (-g/(v.k_in+i0)) equals W[x,-inf] (past-pointing) first-order term:",
      sp.simplify(res["W[x,-inf] = doc W^(-)(x)"] - (-gg / (kn + sp.I * eta))) == 0)

print("\n== p.25: first order of U^dag(y-) psi = -ig int_{-inf}^{y-} dz A(z) psi  ->  g t/(k^+ + i0) ==")
kp, z = sp.symbols('kp z', real=True)
val = sp.simplify(-sp.I * gg * sp.integrate(sp.exp(-sp.I * kp * z + eta * z), (z, -sp.oo, 0), conds='none'))
print("  ", val, " == g/(k^+ + i eta):", sp.simplify(val - gg / (kp + sp.I * eta)) == 0)
print("  first order of W[w,0] = P exp(ig int_0^w dy A): ", sp.simplify(sp.I * gg * sp.integrate(sp.exp(-sp.I * kp * z), (z, 0, sp.Symbol('w', positive=True)))))
