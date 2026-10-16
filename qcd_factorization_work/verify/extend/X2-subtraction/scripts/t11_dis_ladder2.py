"""X2/T11: DIS two-rung ladder (phi^3_6, two loops): remainder r = sum_c (-1)^|c| rho_c, c in {0,1}^3 (REPORT Lemma C.3).
rho_c = (1/pi^4) [1/((1-z1)(1-z2))] v1^-2 v2^-2 H^(c3),
 v1 = z1 (1-c1) m2 + k1^2/(1-z1),  v2 = z2 (1-c2) v1 + |k2 - (1-c2) z2 k1|^2/(1-z2),
 H^(0) = 1/(A + v2 + 2 k2.q),  H^(1) = 1/A,  A = 1 - z1 z2/x.
Norms: (a) full LCPT norm (angles theta12 = angle(k1,k2), theta2q = angle(k2,q_T) in the base),
       (b) theta2q averaged in the fiber, (c) both angles averaged in the fiber; signed integral.
4D transverse measure for a polar angle: dOmega_3 = 4 pi sin^2(th) dth."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np, warnings
from scipy.stats import qmc
warnings.filterwarnings('ignore')
x = 2.0
NG = 24
gn, gw = np.polynomial.legendre.leggauss(NG)
TH = 0.5*np.pi*(gn + 1); THW = 0.5*np.pi*gw*4*np.pi*np.sin(0.5*np.pi*(gn + 1))**2   # weights incl. 4 pi sin^2

def rho_all(z1, z2, k1, k2, c12, c2q, m2):
    """returns rho_r (sum over c with signs) for arrays (broadcastable)."""
    A = 1 - z1*z2/x
    tot = 0.0
    for c1 in (0, 1):
        v1 = z1*(1 - c1)*m2 + k1**2/(1 - z1)
        for c2 in (0, 1):
            if c2 == 0:
                v2 = z2*v1 + (k2**2 + (z2*k1)**2 - 2*z2*k1*k2*c12)/(1 - z2)
            else:
                v2 = k2**2/(1 - z2) + 0*v1
            for c3 in (0, 1):
                H = 1/A if c3 == 1 else 1/(A + v2 + 2*k2*c2q)
                sgn = (-1)**(c1 + c2 + c3)
                tot = tot + sgn*H/(v1**2*v2**2)
    return tot/(np.pi**4*(1 - z1)*(1 - z2))

def run(m2, nlog2=18, lk=(-14.0, 4.0), nrep=4):
    res = {'signed': [], 'full': [], 'avgq': [], 'avg2': []}
    for rep in range(nrep):
        sob = qmc.Sobol(d=4, scramble=True, seed=101 + rep)
        U = sob.random_base2(nlog2)
        # z via z = 1-(1-u)^2 ... use logistic-like map to resolve both ends
        def zmap(u):
            s = -20 + 34*u; sg = 1/(1 + np.exp(-s)); om = 1/(1 + np.exp(s))
            return sg, sg*om*34
        z1, j1 = zmap(U[:, 0]); z2, j2 = zmap(U[:, 1])
        l1 = lk[0] + (lk[1] - lk[0])*U[:, 2]; l2 = lk[0] + (lk[1] - lk[0])*U[:, 3]
        k1 = np.exp(l1); k2 = np.exp(l2)
        jac = j1*j2*(k1**4)*(k2**4)*(lk[1] - lk[0])**2
        # angular quadrature (tensor GL) inside
        Z1 = z1[:, None, None]; Z2 = z2[:, None, None]; K1 = k1[:, None, None]; K2 = k2[:, None, None]
        C12 = np.cos(TH)[None, :, None]; C2Q = np.cos(TH)[None, None, :]
        R = rho_all(Z1, Z2, K1, K2, C12, C2Q, m2)
        R = np.nan_to_num(R, nan=0.0, posinf=0.0, neginf=0.0)
        W2 = THW[None, :, None]*THW[None, None, :]
        full = np.sum(np.abs(R)*W2, axis=(1, 2))
        avgq = np.sum(np.abs(np.sum(R*THW[None, None, :], axis=2))*THW[None, :], axis=1)
        avg2 = np.abs(np.sum(R*W2, axis=(1, 2)))
        signed = np.sum(R*W2, axis=(1, 2))
        for key, arr in [('signed', signed), ('full', full), ('avgq', avgq), ('avg2', avg2)]:
            res[key].append(np.mean(arr*jac))
    return {k: (np.mean(v), np.std(v)/np.sqrt(len(v))) for k, v in res.items()}

if __name__ == "__main__":
    print("DIS two-rung ladder remainder norms (Q=1, x=2); lam = m")
    for m2 in [1e-2, 1e-3, 1e-4, 1e-5, 1e-6]:
        lam = np.sqrt(m2); L = np.log(1/m2)
        out = run(m2)
        s, f, aq, a2 = out['signed'], out['full'], out['avgq'], out['avg2']
        print(f" m2={m2:.0e}: signed={s[0]:+.4e}({s[0]/m2:+.3f} m2)  full={f[0]:.4e} ({f[0]/lam:.4f} lam, {f[0]/(lam*L):.4f} lam L)"
              f"  avg_q={aq[0]:.4e} ({aq[0]/lam:.4f} lam)  avg_both={a2[0]:.4e} ({a2[0]/m2:.3f} m2, {a2[0]/(m2*L*L):.4f} m2 L^2)"
              f"   [rel.err full {f[1]/f[0]:.1e}]")
