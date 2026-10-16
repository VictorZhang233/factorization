"""
qcdtools.py -- shared numerical toolkit for the c_wilson checks.

Conventions (binding conventions of CONTEXT.md, Peskin-Schroeder signs):
  metric (+,-,-,-);  light-front v^pm = (v^0 pm v^3)/sqrt2,  v.w = v^+w^- + v^-w^+ - v_T.w_T
  D_mu = d_mu - i g A_mu^a t^a
  quark propagator  S(p) = i/(pslash - m) = i(pslash + m)/(p^2 - m^2)
  quark-gluon vertex  i g gamma^mu t^a
  gluon propagator (Feynman gauge)  -i g^{mu nu} delta^{ab}/k^2
  three-gluon vertex (all momenta incoming, (a,mu,k),(b,nu,p),(c,rho,q)):
      g f^{abc} [ g^{mu nu}(k-p)^rho + g^{nu rho}(p-q)^mu + g^{rho mu}(q-k)^nu ]
  ghost propagator  i delta^{ab}/p^2 ;  ghost-gluon vertex  -g f^{abc} p^mu
      (p = outgoing ghost momentum, a = outgoing ghost colour, b = gluon, c = incoming ghost)
  Tr(t^a t^b) = delta^{ab}/2, t^a = lambda^a/2 (Gell-Mann).
All four-vectors are stored with UPPER indices as numpy arrays (v^0, v^1, v^2, v^3).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import itertools

# ---------------------------------------------------------------- metric
METRIC = np.diag([1.0, -1.0, -1.0, -1.0])


def mdot(a, b):
    """Minkowski product a.b for (possibly complex) upper-index vectors."""
    return a[0] * b[0] - a[1] * b[1] - a[2] * b[2] - a[3] * b[3]


def lower(v):
    return METRIC @ v


def lc(plus, minus, t1=0.0, t2=0.0):
    """Cartesian upper-index vector from light-front components (v^+, v^-, v_T)."""
    return np.array([(plus + minus) / np.sqrt(2.0), t1, t2, (plus - minus) / np.sqrt(2.0)])


def lc_comp(v):
    """(v^+, v^-, v^1, v^2) of a Cartesian upper-index vector."""
    return np.array([(v[0] + v[3]) / np.sqrt(2.0), (v[0] - v[3]) / np.sqrt(2.0), v[1], v[2]])


# light-cone basis vectors:  nA.v = v^-  (nA along +z),  nB.v = v^+  (nB along -z)
NA = lc(1.0, 0.0)   # (+,-,T) = (1,0,0): nA.v = v^-
NB = lc(0.0, 1.0)   # (+,-,T) = (0,1,0): nB.v = v^+   (Collins' w_2 = (0,1,0_T))

# ---------------------------------------------------------------- Dirac matrices (Dirac representation)
I2 = np.eye(2, dtype=complex)
SIG = [np.array([[0, 1], [1, 0]], dtype=complex),
       np.array([[0, -1j], [1j, 0]], dtype=complex),
       np.array([[1, 0], [0, -1]], dtype=complex)]
Z2 = np.zeros((2, 2), dtype=complex)
GAM = [np.block([[I2, Z2], [Z2, -I2]])] + [np.block([[Z2, s], [-s, Z2]]) for s in SIG]   # gamma^mu
I4 = np.eye(4, dtype=complex)
GAM5 = 1j * GAM[0] @ GAM[1] @ GAM[2] @ GAM[3]


def slash(p):
    """gamma^mu p_mu for an upper-index (possibly complex) vector p."""
    return p[0] * GAM[0] - p[1] * GAM[1] - p[2] * GAM[2] - p[3] * GAM[3]


def bar(spinor):
    """Dirac adjoint of a column spinor -> row spinor."""
    return spinor.conj() @ GAM[0]


def check_clifford():
    err = 0.0
    for m in range(4):
        for n in range(4):
            err = max(err, np.abs(GAM[m] @ GAM[n] + GAM[n] @ GAM[m] - 2 * METRIC[m, n] * I4).max())
    return err


# ---------------------------------------------------------------- spinors
CHI = [np.array([1, 0], dtype=complex), np.array([0, 1], dtype=complex)]


def u_spinor(p, s, m=0.0):
    """Dirac-representation u(p,s), normalized ubar u = 2m, u^dag u = 2E; requires p on shell."""
    E = p[0]
    sp = sum(p[i + 1] * SIG[i] for i in range(3))
    return np.concatenate([np.sqrt(E + m) * CHI[s], (sp @ CHI[s]) / np.sqrt(E + m)])


def v_spinor(p, s, m=0.0):
    """Dirac-representation v(p,s), normalized vbar v = -2m; requires p on shell."""
    E = p[0]
    sp = sum(p[i + 1] * SIG[i] for i in range(3))
    return np.concatenate([(sp @ CHI[s]) / np.sqrt(E + m), np.sqrt(E + m) * CHI[s]])


# ---------------------------------------------------------------- propagators and vertices (Dirac part)
def S_quark(p, m=0.0):
    """i/(pslash - m) as a 4x4 matrix (computed by inversion: no sign ambiguity)."""
    return 1j * np.linalg.inv(slash(p) - m * I4)


def S_quark_explicit(p, m=0.0):
    return 1j * (slash(p) + m * I4) / (mdot(p, p) - m * m)


# ---------------------------------------------------------------- colour SU(3)
def gell_mann():
    l = np.zeros((8, 3, 3), dtype=complex)
    l[0][0, 1] = l[0][1, 0] = 1
    l[1][0, 1] = -1j; l[1][1, 0] = 1j
    l[2][0, 0] = 1; l[2][1, 1] = -1
    l[3][0, 2] = l[3][2, 0] = 1
    l[4][0, 2] = -1j; l[4][2, 0] = 1j
    l[5][1, 2] = l[5][2, 1] = 1
    l[6][1, 2] = -1j; l[6][2, 1] = 1j
    l[7][0, 0] = l[7][1, 1] = 1 / np.sqrt(3); l[7][2, 2] = -2 / np.sqrt(3)
    return l


TA = gell_mann() / 2.0     # t^a, a = 0..7
I3 = np.eye(3, dtype=complex)
# f^{abc} = -2 i Tr([t^a,t^b] t^c)
FABC = np.zeros((8, 8, 8))
for a in range(8):
    for b in range(8):
        comm = TA[a] @ TA[b] - TA[b] @ TA[a]
        for c in range(8):
            FABC[a, b, c] = np.real(-2j * np.trace(comm @ TA[c]))


def check_colour():
    e1 = max(np.abs(np.trace(TA[a] @ TA[b]) - 0.5 * (a == b)) for a in range(8) for b in range(8))
    e2 = 0.0
    for a in range(8):
        for b in range(8):
            comm = TA[a] @ TA[b] - TA[b] @ TA[a]
            e2 = max(e2, np.abs(comm - 1j * np.einsum('c,cij->ij', FABC[a, b], TA)).max())
    CF = np.einsum('aij,ajk->ik', TA, TA)
    e3 = np.abs(CF - 4.0 / 3.0 * I3).max()
    CA = np.einsum('acd,bcd->ab', FABC, FABC)
    e4 = np.abs(CA - 3.0 * np.eye(8)).max()
    return max(e1, e2, e3, e4)


# ---------------------------------------------------------------- gluon vertices (upper indices)
def V3(a, k, b, p, c, q, g=1.0):
    """Three-gluon vertex tensor V^{mu nu rho} (upper indices) for incoming (a,mu,k),(b,nu,p),(c,rho,q)."""
    f = FABC[a, b, c]
    gi = METRIC  # g^{mu nu} numerically equal to g_{mu nu}
    T = (np.einsum('mn,r->mnr', gi, k - p) + np.einsum('nr,m->mnr', gi, p - q)
         + np.einsum('rm,n->mnr', gi, q - k))
    return g * f * T


def ghost_vertex(a, b, c, p_out, g=1.0):
    """-g f^{abc} p^mu (upper index); a = outgoing ghost colour, b = gluon, c = incoming ghost."""
    return -g * FABC[a, b, c] * p_out


# ---------------------------------------------------------------- random kinematics
def rand_massless(rng, E=None, scale=1.0):
    if E is None:
        E = scale * rng.uniform(0.5, 2.0)
    n = rng.normal(size=3); n /= np.linalg.norm(n)
    return np.concatenate([[E], E * n])


def rand_massive(rng, m, pscale=1.0):
    pv = pscale * rng.normal(size=3)
    return np.concatenate([[np.sqrt(m * m + pv @ pv)], pv])


def rand_vec(rng, scale=1.0, cplx=False):
    v = scale * rng.normal(size=4)
    if cplx:
        v = v + 1j * scale * rng.normal(size=4)
    return v


def phys_pols(k):
    """Two physical (transverse) polarization vectors for an on-shell massless k (eps.k = 0, eps^0 = 0)."""
    kv = np.real(k[1:4]); kn = kv / np.linalg.norm(kv)
    t = np.array([1.0, 0, 0]) if abs(kn[0]) < 0.9 else np.array([0, 1.0, 0])
    e1 = np.cross(kn, t); e1 /= np.linalg.norm(e1)
    e2 = np.cross(kn, e1)
    return [np.concatenate([[0.0], e1]), np.concatenate([[0.0], e2])]


def kbar(k):
    """Conjugate light-like vector (k^0, -vec k)."""
    return np.array([k[0], -k[1], -k[2], -k[3]])


def rel(a, b):
    """max |a-b| / max(|a|,|b|,tiny)."""
    a = np.asarray(a); b = np.asarray(b)
    den = max(np.abs(a).max(), np.abs(b).max(), 1e-300)
    return np.abs(a - b).max() / den


class Report:
    """Collects PASS/FAIL lines."""
    def __init__(self, name):
        self.name = name
        self.rows = []

    def check(self, label, value, tol, note=''):
        ok = bool(value <= tol)
        self.rows.append((label, ok, value, tol, note))
        print(f"[{'PASS' if ok else 'FAIL'}] {label}: {value:.3e} (tol {tol:.0e}) {note}")
        return ok

    def flag(self, label, ok, note=''):
        self.rows.append((label, bool(ok), float('nan'), float('nan'), note))
        print(f"[{'PASS' if ok else 'FAIL'}] {label} {note}")
        return ok

    def summary(self):
        n = len(self.rows); npass = sum(r[1] for r in self.rows)
        print(f"\n=== {self.name}: {npass}/{n} PASS ===")
        return npass, n


if __name__ == '__main__':
    print('Clifford error', check_clifford())
    print('colour algebra error', check_colour())
    rng = np.random.default_rng(1)
    for m in [0.0, 1.3]:
        p = rand_massive(rng, m) if m > 0 else rand_massless(rng)
        su = sum(np.outer(u_spinor(p, s, m), bar(u_spinor(p, s, m))) for s in range(2))
        sv = sum(np.outer(v_spinor(p, s, m), bar(v_spinor(p, s, m))) for s in range(2))
        print('m=', m, 'sum u ubar - (pslash+m):', np.abs(su - slash(p) - m * I4).max(),
              ' sum v vbar - (pslash-m):', np.abs(sv - slash(p) + m * I4).max())
        print('   Dirac eq u:', max(np.abs((slash(p) - m * I4) @ u_spinor(p, s, m)).max() for s in range(2)),
              ' v:', max(np.abs((slash(p) + m * I4) @ v_spinor(p, s, m)).max() for s in range(2)))
