import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np, sympy as sp, mpmath as mp

m = 1.0
ER, pR = np.meshgrid(np.linspace(-2, 2, 801), np.linspace(-2, 2, 801), indexing='ij')

def den(eta, xi, lam):
    E = ER + 1j*lam*eta
    p = pR + 1j*lam*xi
    return E - p**2/(2*m)          # i*epsilon added separately (eps >= 0)

def min_abs_with_eps(eta, xi, lam):
    d = den(eta, xi, lam)
    # a zero of d + i eps for some eps>=0 requires Re d = 0 and Im d <= 0.
    # measure: distance of d from the closed negative imaginary half-line {-i t, t>=0}
    dist = np.where(d.imag <= 0, np.abs(d.real), np.abs(d))
    return dist.min()

print("=== E15: anomalous deformations for 1/(E - p^2/2m + i eps)  (Collins App. B.1) ===")
D_first_order = lambda eta, xi: eta - xi*pR/m    # (eta,xi).D with D=(1,-p/m)
cases = {
  "naive (eta,xi)=(1,0)":              (np.ones_like(ER), np.zeros_like(ER)),
  "tangent const (eta,xi)=(0,m)":      (np.zeros_like(ER), m*np.ones_like(ER)),
  "anomalous #1 (|E|+2|p|, m)":        (np.abs(ER)+2*np.abs(pR), m*np.ones_like(ER)),
  "anomalous #2 (p+p^2/2m-E, m)":      (pR + pR**2/(2*m) - ER, m*np.ones_like(ER)),
}
for name, (eta, xi) in cases.items():
    mins = [min_abs_with_eps(eta, xi, lam) for lam in (1e-3, 1e-2, 0.1, 0.5, 1.0)]
    print("%-32s min distance to forbidden set for lam=1e-3..1: %s" % (name, ["%.2e" % v for v in mins]))
# first-order shift on the singular surface E = p^2/2m
pp = np.linspace(-2, 2, 9)
for name, f in [("anomalous #1", lambda p: np.abs(p**2/2)+2*np.abs(p) - p), ("anomalous #2", lambda p: p + p**2/2 - p**2/2 - p)]:
    print(name, "first-order shift (eta,xi).D on E=p^2/2m:", np.round(f(pp), 3))

# exact symbolic statement for #2: Re=0 => Im = lam^3 m/2
E_, p_, lam_, m_ = sp.symbols('E_R p_R lambda m', real=True)
eta2 = p_ + p_**2/(2*m_) - E_; xi2 = m_
d2 = sp.expand((E_ + sp.I*lam_*eta2) - (p_ + sp.I*lam_*xi2)**2/(2*m_))
re2, im2 = sp.re(d2), sp.im(d2)
Esol = sp.solve(sp.Eq(re2, 0), E_)[0]
print("#2: Re d = %s ; on Re d = 0: Im d = %s" % (sp.simplify(re2), sp.simplify(im2.subs(E_, Esol))))
eta1 = sp.Abs(E_) + 2*sp.Abs(p_)
d1 = sp.expand((E_ + sp.I*lam_*eta1) - (p_ + sp.I*lam_*m_)**2/(2*m_))
print("#1: Re d =", sp.simplify(sp.re(d1)), "; Im d =", sp.simplify(sp.im(d1)))

print("\n=== E15: trap without singularity (Collins App. A) ===")
Qs = sp.symbols('Q', positive=True); ms = sp.symbols('m', positive=True); k = sp.symbols('k')
# close contour in lower half plane: only pole k = m - i0 ; integral = -2 pi i Res
res = sp.limit((k-ms)/((k-ms)*k**2*(k+Qs)), k, ms)
I = sp.simplify(ms**2*Qs*(-2*sp.pi*sp.I)*res)
print("I(Q/m) =", I, " -> m->0 limit:", sp.limit(I, ms, 0))
for (mv, Qv) in [(0.1, 1.0), (0.01, 1.0)]:
    e = 1e-4*mv
    f = lambda x: mv**2*Qv/((x-mv+1j*e)*(x-1j*e)**2*(x+Qv-1j*e))
    num = mp.quad(f, [-mp.inf, -Qv-1, -Qv, -Qv/2, -10*mv, -mv, 0, mv, 2*mv, 10*mv, 1, mp.inf], maxdegree=10)
    print("  numeric m=%g Q=%g: %s  vs exact %s" % (mv, Qv, complex(num), complex(-2j*mp.pi/(1+mv/Qv))))
