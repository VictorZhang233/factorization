import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp, mpmath as mp, numpy as np

print("=== E18 (a) reduce the first line of Collins 0708.4410v1 eq.(10) ===")
x, pp, A, mg2, lT2 = sp.symbols('x p_plus A m_g2 lT2', positive=True)
u = sp.symbols('u')
eps = sp.symbols('epsilon', positive=True)
# l^- integral at l^+=0, u = l^- - k^- : 1/[(-2 x p+ u - A + s i eps)(2(1-x) p+ u - A + s i eps)],  s=+1 (amplitude), s=-1 (conjugate)
def lminus_integral(s):
    u1 = (-A + s*sp.I*eps)/(2*x*pp); u2 = (A - s*sp.I*eps)/(2*(1-x)*pp)
    f = 1/((-2*x*pp)*(u-u1)*(2*(1-x)*pp)*(u-u2))
    # close the contour where u1 lies (upper half plane if s=+1, lower if s=-1)
    res = sp.residue(f, u, u1)
    val = (2*sp.pi*sp.I*res) if s == 1 else (-2*sp.pi*sp.I*res)
    return sp.simplify(sp.limit(val, eps, 0))
J_amp, J_conj = lminus_integral(1), lminus_integral(-1)
print("l^- integral, +i0 on both quark lines (amplitude side):", J_amp)
print("l^- integral, -i0 (complex-conjugate side):           ", J_conj)
# numeric check of the amplitude-side value
xv, pv, Av, ev = 0.3, 2.0, 1.7, 1e-6
num = mp.quad(lambda w: 1/((-2*xv*pv*w - Av + 1j*ev)*(2*(1-xv)*pv*w - Av + 1j*ev)), [-mp.inf, -10, -Av/(2*xv*pv), 0, Av/(2*(1-xv)*pv), 10, mp.inf])
print("  numeric:", complex(num), " vs pi i/(p+ A) =", complex(1j*mp.pi/(pv*Av)))
lam, g1, g2, F = sp.symbols('lambda g1 g2 F')
pref = lam**2*g1**2*g2*(g2+g1)/(2*sp.pi)**12
kminus_jac = 1/(2*(1-x)*pp)          # int dk^- 2 pi delta((p-k)^2-m^2) -> 2 pi/(2(1-x)p+)
per_gluon = lambda J: (2*(1-x)*pp)*(1/(-1))*J   # numerator 2(p+-k+) at l+=0 ; gluon propagator 1/(l^2-mg^2) = -1/(lT^2+mg^2) ; J carries 1/A
for label, J1, J2 in [("literal (+i0 on all four quark lines, as printed)", J_amp, J_amp),
                      ("amplitude x conjugate (+i0 left, -i0 right of the cut)", J_amp, J_conj)]:
    I1 = pref*x*pp*(2*sp.pi)**2*(2*sp.pi)*kminus_jac*per_gluon(J1)*per_gluon(J2)
    I1 = sp.simplify(I1*A**2)   # strip 1/A per gluon -> remaining factor multiplies F^2 = (int d^2l 1/[(l^2+mg^2)((k-l)^2+mq^2)])^2
    N = lam**2*g1**2*g2*(g2+g1)*x*(1-x)/(256*sp.pi**7)
    print("%s: I1 = (%s) * N * F(kT)^2" % (label, sp.simplify(I1/N)))

print("\n=== E18 (b) mass dimensions (lambda has dimension 1 for a cubic scalar coupling) ===")
M = sp.symbols('M', positive=True)
first_line = M**2 * M * M * M**8 * M**2 / M**12 / M**2 / M**2   # lam^2 * xp+ * dk- * d4l d4l * numerators / 6 props / delta(l+)^2 / delta(onshell)
printed_second = M**2 * M**4 * (M**2/(M**2*M**2))**2
corrected_second = M**2 * M**4 * (1/(M**2*M**2))**2
eq11 = M**2 * M**4 / (M**2)**4
print("first line of (10):", first_line, "; printed second line of (10):", printed_second,
      "; corrected:", corrected_second, "; eq.(11):", eq11, " ; a TMD density f(x,kT) has dimension M^-2")

print("\n=== E18 (c) int d^2k (I1+I2) = 0 for the corrected form; printed form diverges ===")
mg, mq = 0.5, 1.0
from scipy import integrate, special
def Fk(k):
    s_ = k*k + mg*mg + mq*mq; Lam = s_*s_ - 4*mg*mg*mq*mq; r = np.sqrt(Lam)
    return np.pi/r*np.log((s_ + r)**2/(4*mg*mg*mq*mq))       # stable form of ln((s+r)/(s-r))
def Bub(q2):   # 2D bubble int d^2l 1/[(l^2+mg^2)((q-l)^2+mq^2)], stable closed form
    s_ = q2 + mg*mg + mq*mq; r = np.sqrt(s_*s_ - 4*mg*mg*mq*mq)
    return np.pi/r*np.log((s_ + r)**2/(4*mg*mg*mq*mq))
def Gk(k):    # G(k) = int d^2l1 Bub((k-l1)^2)/(l1^2+mg^2)  (radial x angular)
    inner = lambda l: integrate.quad(lambda th: Bub(k*k + l*l - 2*k*l*np.cos(th)), 0, np.pi, epsabs=1e-12, epsrel=1e-10)[0]*2
    return integrate.quad(lambda v: (lambda l: l*inner(l)/(l*l+mg*mg))(v/(1-v))/(1-v)**2, 0, 1, limit=200, epsabs=1e-10, epsrel=1e-8)[0]
# check F against direct 2D integral at one point
k0 = 0.7
Fnum = integrate.dblquad(lambda th, l: l/((l*l+mg*mg)*(k0*k0 + l*l - 2*k0*l*np.cos(th) + mq*mq)), 0, np.inf, 0, 2*np.pi, epsabs=1e-12)[0]
print("F(0.7): closed form", Fk(k0), " direct", Fnum)
t = lambda f: integrate.quad(lambda v: f(v/(1-v))/(1-v)**2, 0, 1, limit=400, epsabs=1e-12, epsrel=1e-10)[0]   # k = v/(1-v)
I1int = 2*np.pi*t(lambda k: k*Fk(k)**2)
I2int = 2*np.pi*integrate.quad(lambda v: (lambda k: k*Gk(k)/(k*k+mq*mq))(v/(1-v))/(1-v)**2, 0, 1, limit=100, epsabs=1e-8, epsrel=1e-7)[0]
bval = (2*np.pi)**3*integrate.quad(lambda b: b*special.k0(mg*b)**2*special.k0(mq*b)**2, 0, np.inf, limit=400)[0]
print("int d^2k F^2 = %.9f ; int d^2k G/(k^2+mq^2) = %.9f ; b-space (2pi)^3 int b K0^2 K0^2 = %.9f" % (I1int, I2int, bval))
print("=> int d^2k (I1+I2)/N = %.2e" % (I1int - I2int))
for K in (10, 100, 1000):
    val = 2*np.pi*integrate.quad(lambda k: k*(k*k+mq*mq)**2*Fk(k)**2, 0, K, limit=400)[0]
    print("  printed numerator: int_{k<%d} d^2k (k^2+mq^2)^2 F^2 = %.6g (grows without bound)" % (K, val))
print("  I1(0)+I2(0) in units of N (corrected form):", Fk(0.0)**2 - Gk(0.0)/mq**2)
