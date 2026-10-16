#!/usr/bin/env python3
"""
N05 (stage-2 verifier): one-loop quasi-PDF of an on-shell massless quark in the unphysical regions
x>1 and x<0, Gamma = gamma^0, Feynman gauge, CONTEXT conventions
(D = d - i g A,  vertex +i g gamma^mu t^a,  W[z,0] = P exp(i g int_0^1 ds z.A(sz)),
 qtilde(x) = (p^z/p^0) int dz/(4 pi) e^{i x p^z z} <p| psibar(z e_z) gamma^0 W psi(0) |p>, spin/colour averaged).

Methods used here (deliberately different from the stage-1 verifier, who did k^0 by residues and k_T numerically):
  (A) analytic: Feynman parameters + 3-D Euclidean master integrals (own derivation, sympy),
  (B) numerical, NO Feynman parameters: Wick rotation k^0 = i k_4 directly in the loop momentum
      (legitimate only where no pole of (p-k)^2+i0 enters the first quadrant, i.e. x>2 or x<0),
      followed by 2-D quadrature in (k_4, |k_T|) with scipy,
  (C) numerical Feynman-parameter version (3-D quadrature) for 1<x<2 where (B) is not allowed,
  (D) tadpole: DR value vs. transverse/3-D cutoff (linear divergence),
  (E) sums vs. the claimed closed forms, and vs. the eps->0 limit of IJJSZ eq. (1loopquasi).
Run: python3 -I n05_quasi_unphysical.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
from scipy import integrate

PASS = FAIL = 0
def check(name, ok, info=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(("PASS " if ok else "FAIL ") + name + ("   " + info if info else ""))

# ---------------- claimed graph values (in units of a = alpha_s C_F/(2 pi) = g^2 C_F/(8 pi^2)) -------------
def vertex_claim(x):
    return integrate.quad(lambda y: (1 - y) / abs(x - y), 0, 1, limit=200)[0]
def sail_claim(x):
    return integrate.quad(lambda y: (x + y) / abs(x - y), 0, 1, limit=200)[0] / (1 - x)
def tad_claim(x):
    return -1.0 / abs(1 - x)
def sum_claim(x):
    if x > 1:
        return (1 + x**2) / (1 - x) * np.log(x / (x - 1)) + 1
    else:
        return -(1 + x**2) / (1 - x) * np.log(-x / (1 - x)) - 1

# ---------------- (A) analytic Feynman-parameter derivation (sympy) ----------------
# Vertex: N_v = (1/2)Tr[pslash gamma^mu kslash gamma^0 kslash gamma_mu] = -8 (p.k) k^0 + 4 p^0 k^2  (derived by hand,
# re-checked below with explicit Dirac matrices). 1/(k^2)^2 (p-k)^2 = int dy 2y / (l^2)^3, l = k-(1-y)p (p^2=0).
g0 = np.diag([1, 1, -1, -1]).astype(complex)
s = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]])]
gam = [g0] + [np.block([[np.zeros((2, 2)), si], [-si, np.zeros((2, 2))]]).astype(complex) for si in s]
metric = np.diag([1.0, -1.0, -1.0, -1.0])
def slash(v):
    return sum(metric[m, m] * v[m] * gam[m] for m in range(4))
rng = np.random.default_rng(7)
okN = True
for _ in range(20):
    P = rng.normal(); p = np.array([abs(P), 0, 0, P]); k = rng.normal(size=4)
    pk = p @ metric @ k; kk = k @ metric @ k
    Tv = 0.5 * np.trace(slash(p) @ sum(metric[m, m] * gam[m] @ slash(k) @ gam[0] @ slash(k) @ gam[m] for m in range(4)))
    okN &= abs(Tv - (-8 * pk * k[0] + 4 * p[0] * kk)) < 1e-10
    Ts = 0.5 * np.trace(slash(p) @ gam[0] @ slash(k) @ gam[3])        # sail-1 Dirac structure ubar g0 kslash g^3 u
    okN &= abs(Ts - 2 * (p[0] * k[3] + p[3] * k[0])) < 1e-10
    Ts2 = 0.5 * np.trace(slash(p) @ gam[3] @ slash(k) @ gam[0])       # sail-2 Dirac structure ubar g^3 kslash g0 u
    okN &= abs(Ts2 - 2 * (p[0] * k[3] + p[3] * k[0])) < 1e-10
check("traces with explicit Dirac matrices: vertex N_v = -8(p.k)k0+4p0 k^2; both sails 2(p0 kz + pz k0)", okN)

# analytic reduction: symmetric integration over the 3 Euclidean directions after Wick rotation of l^0
lE2, lz2, y, x = sp.symbols('lE2 lz2 y x', positive=True)
# N_v -> p0[-8 (l0)^2 + 4 l^2] with (l0)^2 -> -lE^2/3,  l^2 -> -(lE2+lz2); denominator (l^2)^3 = -(lE2+lz2)^3
# master integrals int d^3l l^{2a}/(l^2+D)^m
def master(n_pow, m, D):
    nE = 3
    return sp.pi**sp.Rational(3, 2) * sp.gamma(sp.Rational(nE, 2) + n_pow) * sp.gamma(m - n_pow - sp.Rational(nE, 2)) / (
        sp.gamma(sp.Rational(nE, 2)) * sp.gamma(m)) * D**(sp.Rational(nE, 2) + n_pow - m)
D = sp.symbols('D', positive=True)
Iv = (sp.Rational(4, 3) * master(1, 3, D) + 4 * D * master(0, 3, D))   # int d^3l [ (4/3)l^2 + 4 D ]/(l^2+D)^3
Iv = sp.simplify(Iv)
check("vertex 3-D master combination = 2 pi^2/sqrt(D)", sp.simplify(Iv - 2 * sp.pi**2 / sp.sqrt(D)) == 0, str(Iv))
Is = sp.simplify(master(0, 2, D))
check("sail 3-D master = pi^2/sqrt(D)", sp.simplify(Is - sp.pi**2 / sp.sqrt(D)) == 0, str(Is))
# prefactors: q_v = (g^2 C_F pz/(2p0)) int dy 2y int d^3l/(2pi)^4 p0 [(4/3)l^2+4lz^2]/L^6 ;  |l_z| = |x-1+y| pz
# => q_v = (g^2 CF/(8 pi^2)) int dy y/|x-1+y|  ; q_s(both) = (g^2CF/(8pi^2)) /(1-x) int dy (x+1-y)/|x-1+y|
pref_v = sp.Rational(1, 2) * 2 * 2 * sp.pi**2 / (2 * sp.pi)**4      # (1/2)*(2y)*(2pi^2) /(2pi)^4, per unit y/|x-1+y|
pref_s = 2 * sp.Rational(1, 2) * 2 * sp.pi**2 / (2 * sp.pi)**4   # 2 sails * (1/2 from pz/(2p0)) * (2 from 2p0pz(x+1-y)/pz) * pi^2/(2pi)^4
a_unit = sp.Rational(1, 8) / sp.pi**2
check("vertex prefactor equals a = g^2 C_F/(8 pi^2)", sp.simplify(pref_v - a_unit) == 0)
check("sail (both) prefactor equals a/(1-x)", sp.simplify(pref_s - a_unit) == 0)

# ---------------- (B) direct Wick rotation in k (x>2 or x<0), 2-D quadrature ----------------
def wick_vertex_sail(xv, pz=1.0):
    p0 = pz; kz = xv * pz
    def D2(k4, kT):
        return (p0 - 1j * k4)**2 - (pz - kz)**2 - kT**2
    def fv(k4, kT):
        kE2 = k4**2 + kT**2 + kz**2
        pk = p0 * (1j * k4) - pz * kz
        Nv = -8 * pk * (1j * k4) + 4 * p0 * (-kE2)
        return (Nv / (kE2**2 * D2(k4, kT))).real * 2 * np.pi * kT
    def fs(k4, kT):
        kE2 = k4**2 + kT**2 + kz**2
        Ns = 2 * (p0 * kz + pz * (1j * k4))
        return (Ns / ((1 - xv) * pz * (-kE2) * D2(k4, kT))).real * 2 * np.pi * kT
    opts = dict(limit=400, epsabs=1e-13, epsrel=1e-11)
    def I2(f):
        inner = lambda kT: integrate.quad(lambda k4: f(k4, kT), -np.inf, np.inf, **opts)[0]
        return integrate.quad(inner, 0, np.inf, **opts)[0]
    # q = (g^2 CF pz/(2p0)) int dk4 d^2kT/(2pi)^4 [...]; in units of a = g^2CF/(8pi^2): factor 8pi^2 pz/(2p0 (2pi)^4)
    unit = 8 * np.pi**2 * pz / (2 * p0 * (2 * np.pi)**4)
    return unit * I2(fv), 2 * unit * I2(fs)

for xv in [2.5, 3.7, 8.0, -0.4, -1.0, -3.3]:
    v, s_ = wick_vertex_sail(xv)
    vc, sc = vertex_claim(xv), sail_claim(xv)
    check(f"(B) Wick-rotated k-space, x={xv}: vertex {v:.10f} vs claim {vc:.10f}; sail {s_:.10f} vs claim {sc:.10f}",
          abs(v - vc) < 1e-7 * max(1, abs(vc)) and abs(s_ - sc) < 1e-7 * max(1, abs(sc)))

# pole bookkeeping that forbids the naive Wick rotation for 0<x<2 (first-quadrant pole of (p-k)^2+i0)
for xv in [1.2, 1.5, 1.9]:
    kT2max = xv * (2 - xv)
    check(f"x={xv}: first-quadrant pole of (p-k)^2+i0 exists for kT^2 < x(2-x) = {kT2max:.3f} (Wick rotation in k not allowed)",
          kT2max > 0)

# ---------------- (C) Feynman-parameter numerics, valid for all x (used for 1<x<2) ----------------
def fp_vertex_sail(xv, pz=1.0):
    p0 = pz
    def vy(yv):
        lz = (xv - 1 + yv) * pz
        f = lambda lE: 4 * np.pi * lE**2 * p0 * ((4 / 3) * lE**2 + 4 * lz**2) / (lE**2 + lz**2)**3
        I = integrate.quad(f, 0, np.inf, limit=400, epsabs=1e-14, epsrel=1e-12)[0]
        return (pz / (2 * p0)) * 2 * yv * I / (2 * np.pi)**4
    def sy(yv):
        lz = (xv - 1 + yv) * pz
        f = lambda lE: 4 * np.pi * lE**2 * 2 * p0 * (xv + 1 - yv) * pz / (lE**2 + lz**2)**2
        I = integrate.quad(f, 0, np.inf, limit=400, epsabs=1e-14, epsrel=1e-12)[0]
        return 2 * (1 / (2 * p0 * (1 - xv) * pz)) * pz * I / (2 * np.pi)**4 * p0 / p0
    unit = 8 * np.pi**2
    V = integrate.quad(vy, 0, 1, limit=200, points=[1 - xv] if 0 < 1 - xv < 1 else None)[0] * unit
    S = integrate.quad(sy, 0, 1, limit=200, points=[1 - xv] if 0 < 1 - xv < 1 else None)[0] * unit
    return V, S

for xv in [1.05, 1.5, 1.9, 2.5, -0.4]:
    v, s_ = fp_vertex_sail(xv)
    vc, sc = vertex_claim(xv), sail_claim(xv)
    check(f"(C) Feynman-parameter numerics, x={xv}: vertex {v:.10f} vs {vc:.10f}; sail {s_:.10f} vs {sc:.10f}",
          abs(v - vc) < 1e-8 * max(1, abs(vc)) and abs(s_ - sc) < 1e-8 * max(1, abs(sc)))

# ---------------- (D) tadpole: DR finite, cutoff linearly divergent ----------------
# qt(x) = (i g^2 CF/((1-x)^2 pz)) int dq0 d^{d-2}qT/(2pi)^d 1/(q^2+i0) |_{q^z=(1-x)pz};
# Wick: int dq0 d^{d-2}qT /(q^2+i0) = -i int d^{d-1}qE/(qE^2+qz^2).  DR (d-1 -> 3): -2 pi^2 |qz|.
e = sp.symbols('e')
dr = sp.limit(sp.pi**((3 - 2 * e) / 2) * sp.gamma(1 - (3 - 2 * e) / 2), e, 0)
check("DR: int d^{3-2eps}q/(q^2+M^2) -> -2 pi^2 M at eps->0", sp.simplify(dr + 2 * sp.pi**2) == 0, f"coefficient {dr}")
def tad_DR(xv, pz=1.0):
    qz = abs(1 - xv) * pz
    val = (1j / ((1 - xv)**2 * pz)) * (-1j) * (-2 * np.pi**2 * qz) / (2 * np.pi)**4
    return (val / (1 / (8 * np.pi**2))).real
def tad_cut(xv, Lam, pz=1.0):
    qz = abs(1 - xv) * pz
    I3 = 4 * np.pi * (Lam - qz * np.arctan(Lam / qz))            # int_{|q|<Lam} d^3q/(q^2+qz^2)
    val = (1j / ((1 - xv)**2 * pz)) * (-1j) * I3 / (2 * np.pi)**4
    return (val / (1 / (8 * np.pi**2))).real
for xv in [1.5, 3.0, -0.7]:
    check(f"tadpole DR x={xv}: {tad_DR(xv):.12f} vs claim {tad_claim(xv):.12f}", abs(tad_DR(xv) - tad_claim(xv)) < 1e-12)
    c1, c2 = tad_cut(xv, 1e3), tad_cut(xv, 1e4)
    lin = (c2 - c1) / 9e3
    check(f"tadpole with 3-D cutoff, x={xv}: grows linearly with Lambda, slope {lin:.6e} = 2/(pi (1-x)^2 pz) = {2/(np.pi*(1-xv)**2):.6e}",
          abs(lin - 2 / (np.pi * (1 - xv)**2)) < 1e-6 * lin)

# ---------------- (E) sums ----------------
for xv in [1.05, 1.5, 2.5, 3.7, 8.0, 30.0, -0.05, -0.4, -1.0, -3.3, -30.0]:
    tot = vertex_claim(xv) + sail_claim(xv) + tad_claim(xv)
    check(f"sum of three graphs = closed form, x={xv}: {tot:.12f} vs {sum_claim(xv):.12f}", abs(tot - sum_claim(xv)) < 1e-9)
# large-|x| tail of the sum: -3/(2|x|)
for xv in [1e3, -1e3]:
    check(f"tail x={xv}: |x| * sum = {abs(xv)*sum_claim(xv):.6f} -> -3/2", abs(abs(xv) * sum_claim(xv) + 1.5) < 5e-3)

# symbolic sums
X = sp.symbols('X', positive=True)          # X = x for x>1 ; X = -x for x<0
Y = sp.symbols('Y', positive=True)
v_gt = sp.integrate((1 - Y) / (X - Y), (Y, 0, 1)); s_gt = sp.integrate((X + Y) / (X - Y), (Y, 0, 1)) / (1 - X)
tot_gt = sp.simplify(v_gt + s_gt - 1 / (X - 1))
cl_gt = (1 + X**2) / (1 - X) * sp.log(X / (X - 1)) + 1
num = [complex((tot_gt - cl_gt).subs(X, t).evalf()) for t in [1.3, 2, 5, 17]]
check("symbolic: x>1 sum minus closed form vanishes", max(abs(c) for c in num) < 1e-12, str(num))
xm = -X
v_lt = sp.integrate((1 - Y) / (Y - xm), (Y, 0, 1)); s_lt = sp.integrate((xm + Y) / (Y - xm), (Y, 0, 1)) / (1 - xm)
tot_lt = v_lt + s_lt - 1 / (1 - xm)
cl_lt = -(1 + xm**2) / (1 - xm) * sp.log(-xm / (1 - xm)) - 1
num = [complex((tot_lt - cl_lt).subs(X, t).evalf()) for t in [0.1, 0.5, 2, 9]]
check("symbolic: x<0 sum minus closed form vanishes", max(abs(c) for c in num) < 1e-12, str(num))

# IJJSZ eq. (1loopquasi), x outside [0,1]: Gamma(eps+1/2) e^{eps gE}/sqrt(pi) (mu/pz)^{2eps} (1-eps)/(eps(1-2eps)) * bracket(eps)
ep = sp.symbols('ep')
def ijjsz_limit(xv):
    xv = sp.nsimplify(xv)
    ax = abs(xv); a1 = abs(1 - xv)
    I3 = (ax**(-1 - 2 * ep) / (xv - 1)) if xv > 1 else (ax**(-1 - 2 * ep) / (xv - 1))
    br = ax**(-1 - 2 * ep) * (1 + xv + xv / 2 * (xv - 1 + 2 * ep)) - a1**(-1 - 2 * ep) * (xv + sp.Rational(1, 2) * (1 - xv)**2) + I3
    pre = sp.gamma(ep + sp.Rational(1, 2)) * sp.exp(ep * sp.EulerGamma) / sp.sqrt(sp.pi) * (1 - ep) / (ep * (1 - 2 * ep))
    return sp.N(sp.limit(pre * br, ep, 0), 15)        # mu = pz
for xv in [1.5, 3.0, -0.5, -2.0]:
    li = ijjsz_limit(xv)
    check(f"IJJSZ (1loopquasi) at eps->0, x={xv}: {float(li):.12f} vs claimed sum {sum_claim(xv):.12f}",
          abs(float(li) - sum_claim(xv)) < 1e-10)

print(f"\nSUMMARY n05: {PASS} PASS, {FAIL} FAIL")
