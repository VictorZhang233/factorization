"""R-OUR1 / OUR-1: normalization of the collinear fragmentation function in the hadron frame.

Definition (reference (2.13); Collins-Soper 1982; Collins 2011 ch. 12), light-cone gauge A^+ = 0 (W = 1):
  d(z) = (z^{1-2eps}/(4 N_c)) sum_X int dw^-/(2pi) e^{i k^+ w^-} Tr[gamma^+ <0|psi(w)|p,X><p,X|psibar(0)|0>],
  hadron frame: p = (p^+, 0, 0_T), k^+ = p^+/z.
Lowest order (quark 'hadron'): d = z * delta(1-z)... = delta(1-z).
O(alpha_s), X = gluon l: amplitude <p,l|psibar(0)|0> = ubar(p)(i g epsslash* t^a)(i kslash/k^2), k = p + l.
  => d(z) = (z/(4N_c)) int d^2 l_T /((2pi)^3 2 l^+) g^2 C_F N_c Tr[g^+ kslash g^nu pslash g^mu kslash] d_{nu mu}(l)/(k^2)^2
     with l^+ = p^+(1-z)/z, d_{mu nu} = -g_{mu nu} + (l_mu n_nu + n_mu l_nu)/(n.l), n.V = V^+.
Target (eps = 0): (alpha_s/2pi) C_F (1+z^2)/(1-z) dl_T^2/l_T^2 = g^2 C_F (1+z^2)/(8 pi^3 (1-z) l_T^2) d^2 l_T.
The parton-frame prefactor 1/(4 N_c z) used in the hadron frame would give 1/z^2 times this.
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np

I2 = np.eye(2); Z2 = np.zeros((2, 2))
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
G = [np.block([[Z2, I2], [I2, Z2]]).astype(complex)] + [np.block([[Z2, si], [-si, Z2]]) for si in sig]
eta = np.diag([1., -1., -1., -1.])
def sl(p): return sum(eta[m, m]*p[m]*G[m] for m in range(4))
def dot(a, b): return a @ eta @ b
def from_lc(vp, vm, vx, vy):   # (+,-,T) -> Cartesian
    return np.array([(vp + vm)/np.sqrt(2), vx, vy, (vp - vm)/np.sqrt(2)])
gplus = (G[0] + G[3])/np.sqrt(2)

def trace_T(pplus, z, lT):
    lplus = pplus*(1 - z)/z
    p = from_lc(pplus, 0.0, 0.0, 0.0)
    l = from_lc(lplus, (lT[0]**2 + lT[1]**2)/(2*lplus), lT[0], lT[1])
    k = p + l
    n = from_lc(0.0, 1.0, 0.0, 0.0)          # n.V = V^+  (n^- = 1)
    assert abs(dot(n, l) - lplus) < 1e-12
    glow = eta
    dlow = -glow + (np.outer(eta@l, eta@n) + np.outer(eta@n, eta@l))/dot(n, l)   # d_{mu nu}
    T = 0.0
    for mu, nu in itertools.product(range(4), range(4)):
        if dlow[nu, mu] == 0: continue
        T += dlow[nu, mu]*np.trace(gplus @ sl(k) @ G[nu] @ sl(p) @ G[mu] @ sl(k))
    return T, k, lplus

print(" z      lT     T(numeric)        8 p+ lT^2 (1+z^2)/(1-z)^2     d/d2lT [z^{1}/(4Nc) prefactor] / target    [1/(4Nc z) prefactor] / target")
g2 = 1.0; CF = 4/3; Nc = 3
for z in (0.2, 0.5, 0.8):
    for lTmag in (0.3, 1.7):
        pplus = 2.3
        lT = np.array([lTmag*0.6, lTmag*0.8])
        T, k, lplus = trace_T(pplus, z, lT)
        k2 = dot(k, k)
        pred_T = 8*pplus*lTmag**2*(1 + z**2)/(1 - z)**2
        dens_hadron = (z/(4*Nc))*g2*CF*Nc*T.real/((2*np.pi)**3*2*lplus*k2**2)      # per d^2 l_T
        dens_parton_pref = (1/(4*Nc*z))*g2*CF*Nc*T.real/((2*np.pi)**3*2*lplus*k2**2)
        target = g2*CF*(1 + z**2)/(8*np.pi**3*(1 - z)*lTmag**2)
        print(f" {z:.1f}  {lTmag:4.1f}  {T.real:14.6f}  {pred_T:22.6f}            {dens_hadron/target:10.6f}                         {dens_parton_pref/target:10.6f} (=1/z^2={1/z**2:.4f})")
# k^2 check
z = 0.5; pplus = 2.3; lT = np.array([0.18, 0.24]); T, k, lplus = trace_T(pplus, z, lT)
print("k^2 =", dot(k, k), " expected lT^2 z/(1-z) =", (lT@lT)*z/(1 - z))
# Jacobian: parton frame (k_T = 0) <-> hadron frame (p_T = 0): boost along the light cone leaves +-components;
# transverse boost: v_T -> v_T - (v^+/k^+) k_T ; hadron p_hT(parton frame) = -(p^+/k^+) l_T = -z l_T  =>  d^2 p_hT = z^2 d^2 l_T  (d=4)
print("Jacobian: d^{2-2eps} p_hT = z^{2-2eps} d^{2-2eps} k_T ;  (1/(4Nc z)) * z^{2-2eps} = z^{1-2eps}/(4Nc)  -> hadron-frame prefactor")
