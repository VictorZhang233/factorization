"""
W10 -- small, independent Dirac/colour toolkit (numpy), conventions of the book:
metric (+,-,-,-); light-front v^pm = (v^0 pm v^3)/sqrt2; gamma^0..3 in the Dirac representation;
quark propagator S(p) = i(pslash + m)/(p^2 - m^2); gluon (Feynman) -i g_{mu nu}/k^2; vertex i g gamma^mu t^a;
three-gluon vertex (all momenta incoming) g f^{abc}[g^{mu nu}(k-p)^rho + g^{nu rho}(p-q)^mu + g^{rho mu}(q-k)^nu];
ghost vertex -g f^{abc} p^mu (p outgoing ghost momentum).
"""
import numpy as np

I2 = np.eye(2, dtype=complex); Z2 = np.zeros((2, 2), dtype=complex)
sig = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]], dtype=complex),
       np.array([[1, 0], [0, -1]], dtype=complex)]
g0 = np.block([[I2, Z2], [Z2, -I2]])
gs = [np.block([[Z2, s], [-s, Z2]]) for s in sig]
GAM = [g0] + gs                      # gamma^mu, upper index
ETA = np.diag([1.0, -1.0, -1.0, -1.0])
ID4 = np.eye(4, dtype=complex)

def lower(v): return ETA @ v
def mdot(a, b): return a[0]*b[0] - a[1]*b[1] - a[2]*b[2] - a[3]*b[3]
def slash(p):                        # gamma^mu p_mu
    pl = lower(np.asarray(p, dtype=complex))
    return sum(GAM[m]*pl[m] for m in range(4))
def lc(plus, minus, t1=0.0, t2=0.0):  # from light-front components to (t,x,y,z)
    return np.array([(plus+minus)/np.sqrt(2), t1, t2, (plus-minus)/np.sqrt(2)], dtype=complex)
def plus(v): return (v[0]+v[3])/np.sqrt(2)
def minus(v): return (v[0]-v[3])/np.sqrt(2)
NA = lc(1.0, 0.0)    # n_A . v = v^-
NB = lc(0.0, 1.0)    # n_B . v = v^+

def S(p, m=0.0):
    p = np.asarray(p, dtype=complex)
    return 1j*(slash(p) + m*ID4)/(mdot(p, p) - m*m)

def u_spinors(p, m=0.0):
    """two independent solutions of (pslash - m) u = 0: u = (pslash + m) chi (exact, also for m = 0)"""
    p = np.asarray(p, dtype=complex)
    M = slash(p) + m*ID4
    out = []
    for chi in (np.array([1, 0, 0, 0], dtype=complex), np.array([0, 1, 0, 0], dtype=complex),
                np.array([0, 0, 1, 0], dtype=complex), np.array([0, 0, 0, 1], dtype=complex)):
        u = M @ chi
        if np.linalg.norm(u) > 1e-8 and (not out or np.linalg.matrix_rank(np.column_stack(out + [u]), tol=1e-8) > len(out)):
            out.append(u)
        if len(out) == 2: break
    return out
def v_spinors(p, m=0.0):
    """two independent solutions of (pslash + m) v = 0: v = (pslash - m) chi"""
    p = np.asarray(p, dtype=complex)
    M = slash(p) - m*ID4
    out = []
    for chi in (np.array([1, 0, 0, 0], dtype=complex), np.array([0, 1, 0, 0], dtype=complex),
                np.array([0, 0, 1, 0], dtype=complex), np.array([0, 0, 0, 1], dtype=complex)):
        v = M @ chi
        if np.linalg.norm(v) > 1e-8 and (not out or np.linalg.matrix_rank(np.column_stack(out + [v]), tol=1e-8) > len(out)):
            out.append(v)
        if len(out) == 2: break
    return out
def bar(s): return s.conj() @ g0

# SU(3)
lam = np.zeros((8, 3, 3), dtype=complex)
lam[0][0, 1] = lam[0][1, 0] = 1
lam[1][0, 1] = -1j; lam[1][1, 0] = 1j
lam[2][0, 0] = 1; lam[2][1, 1] = -1
lam[3][0, 2] = lam[3][2, 0] = 1
lam[4][0, 2] = -1j; lam[4][2, 0] = 1j
lam[5][1, 2] = lam[5][2, 1] = 1
lam[6][1, 2] = -1j; lam[6][2, 1] = 1j
lam[7][0, 0] = lam[7][1, 1] = 1/np.sqrt(3); lam[7][2, 2] = -2/np.sqrt(3)
TA = lam/2
FABC = np.zeros((8, 8, 8))
for a in range(8):
    for b in range(8):
        for c in range(8):
            FABC[a, b, c] = np.real(-2j*np.trace((TA[a] @ TA[b] - TA[b] @ TA[a]) @ TA[c]))

def V3(k, p, q, mu, nu, rho):
    """kinematic part of the three-gluon vertex (colour f^{abc} stripped), all momenta incoming, upper indices"""
    G = np.linalg.inv(ETA)  # g^{mu nu} = diag(1,-1,-1,-1)
    return (G[mu, nu]*(k-p)[rho] + G[nu, rho]*(p-q)[mu] + G[rho, mu]*(q-k)[nu])

def rnd_vec(rng, scale=1.0):
    return rng.normal(size=4)*scale + 0j
