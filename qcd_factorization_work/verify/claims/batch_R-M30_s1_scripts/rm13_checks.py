"""R-m13 checks (minor corrections m13-m16 of the reference; independent code).

m13 (p. 56, Fig. 34): q(p1) + g(k) -> gamma*(q) + q(p2).  Graph (d): s-channel, graph (e): quark exchanged
     between the gluon vertex and the photon vertex (propagator p2 - k, singular when p2 || k).
     Feynman gauge (gluon pol. sum -g):  t|M_e|^2 -> -8 s,  t 2Re(M_d M_e^*) -> +16 s z(1-z),
     sum -> -8 s [z^2+(1-z)^2]  (z = Q^2/s, t = (k-p2)^2 -> 0).  Axial (light-cone) gauge with gauge vector n
     along p1:  only |M_e|^2 has the 1/t pole.  Couplings, colour and the 1/4 spin average are stripped.
m14 (p. 67): V = PT (antiunitary): V psibar(w) gamma^mu psi(0) V^-1 = + psibar(-w) gamma^mu psi(0) with no
     hermitian conjugation; and the sign of eps_T^{12} implied by the Trento definition
     f = f1 - f1T^perp eps^{mu nu rho sigma} P_mu k_nu S_rho n_sigma /(M P.n)  (eps^{0123}=+1, hadron along +z).
m15 (pp. 68-69): area of the endpoint region xbar*ybar*Q^2 <= Lambda^2 in the unit square.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import itertools

I2 = np.eye(2); Z2 = np.zeros((2, 2))
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
G = [np.block([[Z2, I2], [I2, Z2]]).astype(complex)] + [np.block([[Z2, si], [-si, Z2]]) for si in sig]   # Weyl/chiral rep
eta = np.diag([1., -1., -1., -1.])
def sl(p): return sum(eta[m, m]*p[m]*G[m] for m in range(4))
def dot(a, b): return a @ eta @ b

def kinematics(s, Q2, cth):
    E = np.sqrt(s)/2
    p1 = np.array([E, 0, 0, E]); k = np.array([E, 0, 0, -E])          # quark along +z, gluon along -z
    E2 = (s - Q2)/(2*np.sqrt(s)); sth = np.sqrt(1 - cth**2)
    p2 = np.array([E2, E2*sth, 0, E2*cth]); q = p1 + k - p2
    return p1, k, p2, q

def pieces(p1, k, p2, q, gauge='feynman', n=None):
    """sum over quark spins and photon pol (-g, current conserved) and gluon pols (Feynman: -g;
    axial: d^{ab} = -g^{ab} + (k^a n^b + n^a k^b)/(n.k)).  Returns dd, ee, 2Re(de)."""
    Sd = sl(p1 + k)/dot(p1 + k, p1 + k)
    Se = sl(p2 - k)/dot(p2 - k, p2 - k)
    # gluon polarization tensor with upper indices
    gup = np.diag([1., -1., -1., -1.])
    if gauge == 'feynman':
        dgl = -gup
    else:
        dgl = -gup + (np.outer(k, n) + np.outer(n, k))/dot(n, k)
    gam = G   # gamma^mu with upper index
    res = {'dd': 0.0, 'ee': 0.0, 'de': 0.0}
    g0 = G[0]
    for mu, nu in itertools.product(range(4), range(4)):
        # photon index mu (pol sum -g_{mu mu'}), gluon index a (pol sum d_{a a'}).
        pass
    # amplitude M^{mu a} (mu photon, a gluon), upper indices on gamma's:
    Md = [[gam[mu] @ Sd @ gam[a] for a in range(4)] for mu in range(4)]   # ubar(p2) g^mu S(p1+k) g^a u(p1)
    Me = [[gam[a] @ Se @ gam[mu] for a in range(4)] for mu in range(4)]   # ubar(p2) g^a S(p2-k) g^mu u(p1)
    P2 = sl(p2); P1 = sl(p1)
    def bar(A): return g0 @ A.conj().T @ g0
    for mu, mup, a, ap in itertools.product(range(4), range(4), range(4), range(4)):
        wph = -eta[mu, mup]                     # -g_{mu mu'} (lower indices)
        if wph == 0: continue
        # gluon: contract M^{mu a} M^{* mu' a'} with d_{a a'} (lower indices) = eta d^{..} eta
        dlow = (eta @ dgl @ eta)[a, ap]
        if dlow == 0: continue
        w = wph*dlow
        tdd = np.trace(P2 @ Md[mu][a] @ P1 @ bar(Md[mup][ap]))
        tee = np.trace(P2 @ Me[mu][a] @ P1 @ bar(Me[mup][ap]))
        tde = np.trace(P2 @ Md[mu][a] @ P1 @ bar(Me[mup][ap]))
        res['dd'] += w*tdd; res['ee'] += w*tee; res['de'] += w*2*tde.real
    return {k_: float(np.real(v)) for k_, v in res.items()}

s, Q2 = 10.0, 3.0
z = Q2/s
print(f"m13: s={s}, Q^2={Q2}, z={z}:  predicted Feynman-gauge limits  t|e|^2 -> -8s = {-8*s},  t*2Re(de) -> 16 s z(1-z) = {16*s*z*(1-z):.4f},"
      f"  t*total -> -8 s (z^2+(1-z)^2) = {-8*s*(z**2+(1-z)**2):.4f}")
print("   gauge     cos(th)        t        t|d|^2      t|e|^2     t*2Re(de)    t*total")
for gauge in ('feynman', 'axial'):
    for cth in [-0.9, -0.99, -0.999, -0.9999]:
        p1, k, p2, q = kinematics(s, Q2, cth)
        t = dot(k - p2, k - p2)
        nvec = p1.copy()      # light-cone gauge vector along the incoming quark (n.A = 0, n^2 = 0, n.k != 0)
        r = pieces(p1, k, p2, q, gauge, nvec)
        tot = r['dd'] + r['ee'] + r['de']
        print(f"  {gauge:8s} {cth:9.4f}  {t:10.6f}  {t*r['dd']:10.5f} {t*r['ee']:11.5f} {t*r['de']:11.5f} {t*tot:11.5f}")
# gauge invariance of the total
p1, k, p2, q = kinematics(s, Q2, 0.37)
rF = pieces(p1, k, p2, q, 'feynman'); rA = pieces(p1, k, p2, q, 'axial', p1.copy())
t = dot(k - p2, k - p2); u = dot(p1 - p2, p1 - p2)
print("m13: total Feynman vs axial (cos=0.37):", rF['dd']+rF['ee']+rF['de'], rA['dd']+rA['ee']+rA['de'],
      "; -8(s/t + t/s + 2uQ^2/(st)) =", -8*(s/t + t/s + 2*u*Q2/(s*t)))

# ---------------- m14 ----------------
print()
g0, g1, g2, g3 = G
g5 = 1j*g0@g1@g2@g3
# Peskin-Schroeder: P psi(t,x) P^-1 = g0 psi(t,-x);  T psi(t,x) T^-1 = (-g1 g3) psi(-t,x) (antiunitary, PS eq. 3.139)
# => V = PT: V psi(x) V^-1 = M psi(-x) with M = -g1 g3 g0  (order: T acts on P psi P^-1 -> P T ... )
Mopts = {'(-g1 g3) g0': -g1@g3@g0, 'g0 (-g1 g3)': g0@(-g1@g3)}
for name, M in Mopts.items():
    ok_vec = all(np.allclose(M.conj().T @ g0.conj() @ G[mu].conj() @ M, g0 @ G[mu]) for mu in range(4))
    ok_ax = all(np.allclose(M.conj().T @ g0.conj() @ (G[mu]@g5).conj() @ M, -(g0 @ G[mu] @ g5)) for mu in range(4))
    print(f"m14: M = {name}: psibar g^mu psi -> +psibar(-w) g^mu psi(0) (no h.c.): {ok_vec};  axial gets a minus sign: {ok_ax}")
# eps_T^{12} implied by the Trento definition (hadron along +z, n lightlike along -z, eps^{0123}=+1)
def levi(*idx):
    perm = list(idx)
    if len(set(perm)) < 4: return 0
    sgn = 1
    for i in range(4):
        for j in range(i+1, 4):
            if perm[i] > perm[j]: sgn = -sgn
    return sgn
def eps_contract(P, k, S, n):
    low = lambda v: eta @ v
    Pl, kl, Sl, nl = low(P), low(k), low(S), low(n)
    tot = 0.0
    for a, b, c, d in itertools.product(range(4), repeat=4):
        e = levi(a, b, c, d)
        if e: tot += e*Pl[a]*kl[b]*Sl[c]*nl[d]
    return tot
P = np.array([5.0, 0, 0, 5.0]); nvec = np.array([1.0, 0, 0, -1.0])
kT = np.array([0, 0.3, -0.7, 0]); S = np.array([0, -0.4, 0.9, 0])
lhs = eps_contract(P, kT, S, nvec)/dot(P, nvec)
cross = np.cross(np.array([0, 0, 1.0]), kT[1:]) @ S[1:]
print(f"m14: eps^(mu nu rho sigma) P k S n /(P.n) = {lhs:.6f};  (P^ x k_T).S = {cross:.6f};  eps2D^{{12}}=+1 form k^1 S^2 - k^2 S^1 = {kT[1]*S[2]-kT[2]*S[1]:.6f}")
print("     => with the hadron along +z, the Trento sign corresponds to eps_T^{ij} k^i S^j with eps_T^{12} = +1")
# Trento's eps_perp in their SIDIS frame (q along +z, target at rest): eps_perp^{rs} = eps^{mu nu r s} P_mu q_nu /(P.q sqrt(1+gamma^2))
M_ = 0.94; qv = np.array([2.0, 0, 0, np.sqrt(2.0**2 + 3.0)])     # Q^2 = 3
Pt = np.array([M_, 0, 0, 0])
gam2 = 4*(3.0/(2*dot(Pt, qv)))**2*M_**2/3.0
def eps_perp(r, s_):
    low = lambda v: eta @ v
    Pl, ql = low(Pt), low(qv); tot = 0.0
    for a, b in itertools.product(range(4), repeat=2):
        tot += levi(a, b, r, s_)*Pl[a]*ql[b]
    return tot/(dot(Pt, qv)*np.sqrt(1+gam2))
print(f"m14: Trento eps_perp^(12) in their SIDIS frame (photon along +z) = {eps_perp(1,2):+.6f}  (paper: -1) -- a different object/frame")

# ---------------- m15 ----------------
print()
for r in [1e-2, 1e-3, 1e-4, 1e-6]:     # r = Lambda^2/Q^2
    # area of {(xb, yb) in [0,1]^2 : xb*yb <= r} = r (1 + ln(1/r))
    xs = np.linspace(0, 1, 2000001)
    area = np.trapezoid(np.minimum(1.0, r/np.maximum(xs, 1e-300)), xs)
    print(f"m15: Lambda^2/Q^2 = {r:.0e}: endpoint area = {area:.6e};  r(1+ln(1/r)) = {r*(1+np.log(1/r)):.6e}")
