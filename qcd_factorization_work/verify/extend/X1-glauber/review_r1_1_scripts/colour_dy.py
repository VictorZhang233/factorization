# Independent check of L4(d)/T3 colour claim, with DY-type remnant colour states.
# In DY at lowest order the remnant colour state is |psi> = singlet of (A-remnant in irrep conj. to the active
# parton of A) x (B-remnant in irrep conj. to active parton of B), produced by delta_{c c'} at the hard vertex.
# Claim to test (reviewer): <psi| i f^{abc} T_i^c T_j1^a T_j2^b |psi> = 0 unless the hadron containing j1,j2 has
# at least one further (passive) remnant parton.  Report's L4(d) quotes the MAX over the full 4-parton singlet
# space, which ignores the DY structure.
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
rng = np.random.default_rng(1)
def su3():
    l = np.zeros((8, 3, 3), dtype=complex)
    l[0][0,1] = l[0][1,0] = 1; l[1][0,1] = -1j; l[1][1,0] = 1j; l[2][0,0] = 1; l[2][1,1] = -1
    l[3][0,2] = l[3][2,0] = 1; l[4][0,2] = -1j; l[4][2,0] = 1j; l[5][1,2] = l[5][2,1] = 1
    l[6][1,2] = -1j; l[6][2,1] = 1j; l[7][0,0] = l[7][1,1] = 1/np.sqrt(3); l[7][2,2] = -2/np.sqrt(3)
    return l/2
F = su3(); Fb = np.array([-t.T for t in F])
fabc = np.zeros((8,8,8))
for a in range(8):
    for b in range(8):
        cm = F[a]@F[b]-F[b]@F[a]
        for c in range(8): fabc[a,b,c] = np.real(-2j*np.trace(cm@F[c]))
Adj = np.array([-1j*fabc[a] for a in range(8)])
R = {'3': F, '3b': Fb, '8': Adj}
def embed(mats, pos, dims):
    out=[]
    for a in range(8):
        M = np.array([[1.0+0j]])
        for p,d in enumerate(dims):
            M = np.kron(M, mats[a] if p==pos else np.eye(d))
        out.append(M)
    return out
def gens(labels):
    dims=[R[l].shape[1] for l in labels]
    return dims, [embed(R[l], p, dims) for p,l in enumerate(labels)]
def irrep_states(labels, target):
    """random state of the multi-parton system 'labels' lying in irrep 'target' (as a 3x... map): returns
    isometry V: C^{dim target} -> H with  sum_p T_p^a V = V T_target^a  (intertwiner), random in multiplicity space."""
    dims, Ts = gens(labels); D = int(np.prod(dims)); Tt = R[target]; d = Tt.shape[1]
    # solve linear equations for V (D x d): sum_p T_p^a V - V T_t^a = 0 for all a
    rows=[]
    for a in range(8):
        Ta = sum(Ts[p][a] for p in range(len(labels)))
        rows.append(np.kron(Ta, np.eye(d)) - np.kron(np.eye(D), Tt[a].T))
    M = np.vstack(rows)
    u,s,vh = np.linalg.svd(M)
    sv = np.concatenate([s, np.zeros(vh.shape[0]-len(s))])
    null = vh[sv < 1e-8*max(1.0, sv.max())].conj()
    if null.shape[0]==0: return None
    coeff = rng.normal(size=null.shape[0]) + 1j*rng.normal(size=null.shape[0])
    v = coeff@null
    V = v.reshape(D, d)
    # normalise so that V^dag V = c*1
    n = np.trace(V.conj().T@V).real/d
    return V/np.sqrt(n)
def dy_state(Alabels, Arep, Blabels, Brep):
    """|psi> = sum_m V_A|m>_(Arep) (x) V_B|m>_(Brep) contracted into a singlet; Arep and Brep conjugate."""
    VA = irrep_states(Alabels, Arep); VB = irrep_states(Blabels, Brep)
    if VA is None or VB is None: return None
    d = VA.shape[1]
    # singlet of Arep x Brep: for 3b x 3 use delta; for 8x8 use delta too (real adjoint)
    psi = sum(np.kron(VA[:, m], VB[:, m]) for m in range(d))
    # verify singlet
    labels = Alabels + Blabels
    dims, Ts = gens(labels)
    for a in range(8):
        Ta = sum(Ts[p][a] for p in range(len(labels)))
        assert np.linalg.norm(Ta@psi) < 1e-8*np.linalg.norm(psi), 'not singlet'
    return psi/np.linalg.norm(psi), labels
def residual_colour(psi, labels, i, j1, j2):
    dims, Ts = gens(labels)
    O = sum(fabc[a,b,c]*Ts[i][c]@Ts[j1][a]@Ts[j2][b] for a in range(8) for b in range(8) for c in range(8) if abs(fabc[a,b,c])>1e-12)
    return np.vdot(psi, 1j*O@psi)
cases = [
 # (A-remnant partons, A-remnant irrep, B-remnant partons, B-remnant irrep, description); i = 0 (first A parton)
 (['3b'], '3b', ['3b','3b'], '3', 'meson A (active q) ; antibaryon B (active qbar), B-rem = 2 partons'),
 (['3','3'], '3b', ['3b','3b'], '3', 'proton A (active q, diquark) ; antiproton B (active qbar, anti-diquark): valence p pbar'),
 (['3','3','8'], '3b', ['3b','3b'], '3', 'A-rem = qqg ; B-rem = 2 antiquarks'),
 (['3b'], '3b', ['3b','3b','8'], '3', 'A-rem = 1 ; B-rem = qbar qbar g (passive gluon in B)'),
 (['3','3'], '3b', ['3b','3b','8'], '3', 'A-rem = diquark ; B-rem = qbar qbar g'),
 (['3','3'], '3b', ['3b','3','3'], '3', 'A-rem = diquark ; B-rem = qbar q q (B = proton whose active parton is a sea antiquark)'),
]
for (Al, Ar, Bl, Br, desc) in cases:
    vals=[]
    for trial in range(4):
        out = dy_state(Al, Ar, Bl, Br)
        if out is None: vals.append(None); break
        psi, labels = out
        nA = len(Al)
        vals.append(residual_colour(psi, labels, 0, nA, nA+1))
    print(f"{desc}\n   A-rem={Al}->{Ar}, B-rem={Bl}->{Br}: <psi|i f T_i T_j1 T_j2|psi> over random DY states = "
          + ", ".join('None' if v is None else f"{v.real:+.3e}{v.imag:+.1e}i" for v in vals))
