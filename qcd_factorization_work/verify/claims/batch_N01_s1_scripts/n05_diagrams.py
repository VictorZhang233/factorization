# Independent first-principles check of the one-loop quasi-PDF diagrams (N05), Gamma = gamma^0,
# Feynman gauge, massless on-shell quark p = (P,0,0,P), xi outside [0,1], d = 4 (vertex, sail),
# tadpole in DR (done analytically in the report).  Conventions: CONTEXT (vertex +i g gamma^mu t^a,
# W = P exp(i g int dz.A)), metric (+,-,-,-).
#   qtilde(x) = (p^z/(2p^0)) int dz/(2pi) e^{i x p^z z} <p| psibar(z) gamma^0 W psi(0) |p>   (tree = delta(1-x))
# Vertex: qv(x) = (1/(2p0)) (-i g^2 C_F) int d^4k/(2pi)^4 Nv delta(x-k^z/p^z) / [(k^2+i0)^2 ((p-k)^2+i0)]
#   Nv = (1/2)Tr[pslash g^mu kslash g^0 kslash g_mu] = -8 (p.k) k^0 + 4 p^0 k^2
# Sail (both): qs(x) = 2 (1/(2p0)) (i g^2 C_F) int d^4k/(2pi)^4 Ns delta(x-y)/[p^z (1-y) (k^2+i0)((p-k)^2+i0)]
#   Ns = (1/2)Tr[pslash g^0 kslash (zhat.gamma)] = -2 (p^0 k^z + p^z k^0)
# k^0 integral done exactly by residues (lower half plane), k_T integral numerically.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
mp.mp.dps = 30

k0, kt2, P, x = sp.symbols('k0 kt2 P x', real=True)
kz = x*P
E = sp.sqrt(kt2 + kz**2)            # k^2 = k0^2 - E^2
Ep = sp.sqrt(kt2 + (P - kz)**2)     # (p-k)^2 = (k0-P)^2 - Ep^2
pk = P*k0 - P*kz                    # p.k with p=(P,0,0,P)
ksq = k0**2 - E**2
Nv = -8*pk*k0 + 4*P*ksq
Ns = -2*(P*kz + P*k0)   # corrected: gamma^3 = slash(e) with e_mu = delta_mu^3

def lower_residues(num, den_factors):
    """sum of residues of num/prod(den) at the poles in the lower half plane:
       k0 = E (from k^2, order = multiplicity) and k0 = P + Ep (from (p-k)^2)."""
    f = num
    for d_ in den_factors:
        f = f / d_
    res = 0
    # pole k0 = E
    m_E = sum(1 for d_ in den_factors if sp.simplify(d_ - ksq) == 0)
    g = sp.simplify(f * (k0 - E)**m_E)
    res += sp.diff(g, k0, m_E - 1).subs(k0, E) / sp.factorial(m_E - 1)
    # pole k0 = P + Ep
    g2 = sp.simplify(f * (k0 - P - Ep))
    res += g2.subs(k0, P + Ep)
    return res

# factor out: k^2 = (k0-E)(k0+E); (p-k)^2 = (k0-P-Ep)(k0-P+Ep)
den_v = [(k0 - E)*(k0 + E), (k0 - E)*(k0 + E), (k0 - P - Ep)*(k0 - P + Ep)]
den_s = [(k0 - E)*(k0 + E), (k0 - P - Ep)*(k0 - P + Ep)]
# rewrite with explicit linear factors so that residues are clean
fv = Nv / ((k0 - E)**2 * (k0 + E)**2 * (k0 - P - Ep) * (k0 - P + Ep))
fs = Ns / ((k0 - E) * (k0 + E) * (k0 - P - Ep) * (k0 - P + Ep))
def res_at(f, pole, order):
    g = sp.cancel(sp.together(f * (k0 - pole)**order))
    return sp.diff(g, k0, order - 1).subs(k0, pole) / sp.factorial(order - 1)
EE, EEp, KZ = sp.symbols('EE EEp KZ', positive=True)
fv2 = fv.subs({E: EE, Ep: EEp}).subs(x*P, KZ)
fs2 = fs.subs({E: EE, Ep: EEp}).subs(x*P, KZ)
Rv = sp.factor(sp.cancel(sp.together(res_at(fv2, EE, 2) + res_at(fv2, P + EEp, 1))))
Rs = sp.factor(sp.cancel(sp.together(res_at(fs2, EE, 1) + res_at(fs2, P + EEp, 1))))
print("simplified LHP residue sums:\n  Rv =", Rv, "\n  Rs =", Rs)
Rv = Rv.subs({EE: E, EEp: Ep, KZ: x*P}); Rs = Rs.subs({EE: E, EEp: Ep, KZ: x*P})
# int dk0 f = -2 pi i * (sum of LHP residues)   (contour closed clockwise; integrand ~ k0^-4, k0^-3)
Iv = sp.lambdify((kt2, P, x), -2*sp.pi*sp.I*Rv, 'mpmath')
Is = sp.lambdify((kt2, P, x), -2*sp.pi*sp.I*Rs, 'mpmath')

def qv_num(xv, Pv=1.0):
    # qv = (1/(2p0)) (-i g^2 C_F) (p^z/(2pi)^4) int d^2kT [int dk0 ...];  int d^2kT = pi int d(kt2)
    # express in units of a = g^2 C_F/(8 pi^2):  g^2 C_F = 8 pi^2 a
    Pv = mp.mpf(Pv); xv = mp.mpf(xv)
    f = lambda t: Iv(t, Pv, xv)
    val = mp.quad(f, [0, 1, 10, 100, mp.inf])
    return (1/(2*Pv)) * (-1j) * 8*mp.pi**2 * Pv / (2*mp.pi)**4 * mp.pi * val

def qs_num(xv, Pv=1.0):
    Pv = mp.mpf(Pv); xv = mp.mpf(xv)
    f = lambda t: Is(t, Pv, xv)
    val = mp.quad(f, [0, 1, 10, 100, mp.inf])
    # 2 * (1/(2p0)) * (i g^2 C_F) * p^z/(2pi)^4 * 1/(p^z (1-x)) * pi*val
    return 2 * (1/(2*Pv)) * 1j * 8*mp.pi**2 * Pv / (2*mp.pi)**4 / (Pv*(1 - xv)) * mp.pi * val

def vert_claim(xv):
    return mp.quad(lambda yy: (1 - yy)/abs(xv - yy), [0, 1])
def sail_claim(xv):
    return mp.quad(lambda yy: (xv + yy)/abs(xv - yy), [0, 1]) / (1 - xv)

worst = 0
for xv in [1.5, 2.0, 3.7, 8.0, -0.4, -1.0, -3.3]:
    v = qv_num(xv); s = qs_num(xv)
    vc = vert_claim(xv); sc = sail_claim(xv)
    dv = abs(v - vc); ds = abs(s - sc)
    worst = max(worst, dv/abs(vc), ds/abs(sc))
    print(f"x={xv:5.2f}: vertex num = {mp.nstr(v,14)}  claim = {mp.nstr(vc,14)} | sail num = {mp.nstr(s,14)}  claim = {mp.nstr(sc,14)}")
# P-independence (boost invariance of the momentum fraction)
print("P-dependence check (x=2.5): vertex", mp.nstr(qv_num(2.5, 1.0), 12), mp.nstr(qv_num(2.5, 3.0), 12),
      " sail", mp.nstr(qs_num(2.5, 1.0), 12), mp.nstr(qs_num(2.5, 3.0), 12))
print("max relative deviation:", mp.nstr(worst, 3))
