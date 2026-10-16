#!/usr/bin/env python3
"""W24 / Ch21 -- prop:power-next-to-soft: tree-level Low-Burnett-Kroll theorem, numerical verification.

Conventions (book): abelian coupling D = d - i e Q A  ->  scalar vertex  i e Q (p_in + p_out)^mu  (momenta along the
particle flow), fermion vertex i e Q gamma^mu; propagators i/(p^2-m^2), i(pslash+m)/(p^2-m^2); Yukawa/cubic vertex -i g.
All external momenta OUTGOING in the formula, photon (k, eps) outgoing, Q_i = physical charge of external particle i.

Statement checked (amplitude level, through O(k^0)):
  M_{n+1} = - e sum_i Q_i [ (eps*.p_i)/(k.p_i) + eps*_mu k_nu J_i^{mu nu}/(k.p_i) ] M_n + O(k),
  J_i^{mu nu} = p_i^mu d_i^nu - p_i^nu d_i^mu + Sigma_i^{mu nu},
  Sigma = 0 (scalars); outgoing fermion: ubar(p) -> ubar(p) (-(i/2) sigma^{mu nu}); outgoing antifermion: v(p) -> (+(i/2) sigma^{mu nu}) v(p),
  sigma^{mu nu} = (i/2)[gamma^mu, gamma^nu]; derivatives act on the stripped amplitude (any smooth extension off shell /
  off momentum conservation; the result is extension independent).
Cross-section level (Burnett-Kroll):
  sum|M_{n+1}|^2 = -e^2 sum_ij Q_i Q_j (p_i.p_j)/((p_i.k)(p_j.k)) sum|M_n|^2
                   - e^2 sum_ij Q_i Q_j p_{i mu} k_nu L_j^{mu nu} sum|M_n|^2 / ((p_i.k)(p_j.k)) + O(k^0),
  with L_j = p_j^mu d_j^nu - p_j^nu d_j^mu acting on the spin-summed square (including the projectors).
Identity used: [pslash, sigma^{mu nu}] = 2 i (p^mu gamma^nu - p^nu gamma^mu).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np

OK = True
def check(name, cond):
    global OK
    print(("PASS " if cond else "FAIL ") + name)
    OK = OK and bool(cond)

g = np.diag([1.0, -1.0, -1.0, -1.0])
def dot(a, b): return a[0]*b[0] - a[1]*b[1] - a[2]*b[2] - a[3]*b[3]
def lower(a): return g @ a
I2 = np.eye(2); Z2 = np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
gam = [np.block([[I2, Z2], [Z2, -I2]]).astype(complex)] + [np.block([[Z2, s], [-s, Z2]]) for s in (sx, sy, sz)]
def slash(p): return gam[0]*p[0] - gam[1]*p[1] - gam[2]*p[2] - gam[3]*p[3]
def sigma(mu, nu): return 0.5j*(gam[mu] @ gam[nu] - gam[nu] @ gam[mu])
E4 = np.eye(4, dtype=complex)

# ---- identity [pslash, sigma^{mu nu}] = 2i (p^mu gamma^nu - p^nu gamma^mu) ----
rng = np.random.default_rng(3)
p_test = rng.normal(size=4)
okid = all(np.allclose(slash(p_test) @ sigma(m, n) - sigma(m, n) @ slash(p_test),
                       2j*(p_test[m]*gam[n] - p_test[n]*gam[m])) for m in range(4) for n in range(4))
# careful: gamma^nu with upper index = gam[nu]; p^mu upper = p_test[mu]
check("identity [pslash, sigma^{mu nu}] = 2i (p^mu gamma^nu - p^nu gamma^mu)", okid)

def spinor_u(p, m, s):
    E = p[0]; chi = np.array([1, 0], complex) if s == 0 else np.array([0, 1], complex)
    sp_ = p[1]*sx + p[2]*sy + p[3]*sz
    return np.concatenate([np.sqrt(E+m)*chi, (sp_ @ chi)/np.sqrt(E+m)])
def spinor_v(p, m, s):
    E = p[0]; eta = np.array([0, 1], complex) if s == 0 else np.array([-1, 0], complex)
    sp_ = p[1]*sx + p[2]*sy + p[3]*sz
    return np.concatenate([(sp_ @ eta)/np.sqrt(E+m), np.sqrt(E+m)*eta])
def bar(u): return u.conj() @ gam[0]

def boost_from_rest(P):     # Lorentz boost taking (M,0,0,0) to P
    M = np.sqrt(dot(P, P)); gm = P[0]/M; bv = P[1:]/P[0]; b2 = bv @ bv
    L = np.eye(4)
    L[0, 0] = gm; L[0, 1:] = gm*bv; L[1:, 0] = gm*bv
    if b2 > 0: L[1:, 1:] += (gm - 1)*np.outer(bv, bv)/b2
    return L

# kinematics: q1 + q2 -> p1 + p2 + k
Ms, m = 0.7, 0.45
sqs = 5.0
pin = np.sqrt(sqs**2/4 - Ms**2)
q1 = np.array([sqs/2, 0, 0, pin]); q2 = np.array([sqs/2, 0, 0, -pin])
khat = np.array([1.0, np.sin(1.1)*np.cos(0.4), np.sin(1.1)*np.sin(0.4), np.cos(1.1)])
nhat = np.array([np.sin(0.7)*np.cos(2.1), np.sin(0.7)*np.sin(2.1), np.cos(0.7)])
def kinematics(lam):
    k = lam*khat
    P = q1 + q2 - k; M = np.sqrt(dot(P, P)); pm = np.sqrt(M**2/4 - m**2)
    L = boost_from_rest(P)
    p1 = L @ np.concatenate([[M/2], pm*nhat]); p2 = L @ np.concatenate([[M/2], -pm*nhat])
    return p1, p2, k
# a physical polarization orthogonal to k (real, spacelike, eps.k = 0, eps^0 = 0 in this frame)
def polarization(k):
    kv = k[1:]/np.linalg.norm(k[1:]); a = np.array([0.3, -0.8, 0.5]); e = a - (a @ kv)*kv; e /= np.linalg.norm(e)
    return np.concatenate([[0.0], e])

e_c = 0.31; gc = 1.3
def prop_s(l): return 1j/(dot(l, l) - m**2)

# ===================== scalar QED =====================
def Mn_scalar(p1, p2, ext=0):
    # natural extensions: ext=0 uses p2 (l_t = q2-p2, l_u = q1-p2); ext=1 uses p1 (l_t = p1-q1, l_u = p1-q2)
    if ext == 0: lt, lu = q2 - p2, q1 - p2
    else: lt, lu = p1 - q1, p1 - q2
    iM = (-1j*gc)**2*(prop_s(lt) + prop_s(lu))
    return -1j*iM
def Mnp1_scalar_vec(p1, p2, k):
    # returns M^mu (upper index), contract with eps*_mu
    out = np.zeros(4, complex)
    for mu in range(4):
        e = np.zeros(4); e[mu] = 1.0      # e^nu = delta^nu_mu ; the vertex (...)^nu contracted with eps*_nu -> use lowered later
        def V(a, b): return 1j*e_c*(a + b)   # vector (upper index), Q=+1 field
        # (1) emission from outgoing phi+ (p1): line p1+k -> p1
        t1 = V(p1 + k, p1)*prop_s(p1 + k)*(1j*Mn_scalar(p1 + k, p2))
        # (2) emission from outgoing phi- (p2): particle flow in with -p2, out with -p2-k
        t2 = V(-p2, -p2 - k)*prop_s(-p2 - k)*(1j*Mn_scalar(p1, p2 + k))
        # (3),(4) internal: flow -p2 -> (+q2 or +q1) -> la -> photon -> la - k -> -> p1
        t3 = (-1j*gc)**2*prop_s(q2 - p2)*V(q2 - p2, q2 - p2 - k)*prop_s(q2 - p2 - k)
        t4 = (-1j*gc)**2*prop_s(q1 - p2)*V(q1 - p2, q1 - p2 - k)*prop_s(q1 - p2 - k)
        tot = t1 + t2 + t3 + t4
        out[mu] = -1j*tot[mu]
    return out   # vector M^mu (upper)
def low_scalar(p1, p2, k, eps, ext=0, h=1e-6):
    Ms_ = Mn_scalar(p1, p2, ext)
    def grad(fun, p):   # d/dp^nu  (upper-index derivative d^nu = g^{nu rho} d/dp^rho)
        gr = np.zeros(4, complex)
        for r in range(4):
            dp = np.zeros(4); dp[r] = h
            gr[r] = (fun(p + dp) - fun(p - dp))/(2*h)
        return g @ gr          # d^nu = g^{nu rho} d_rho, d_rho = d/dp^rho
    res = 0
    for (Qi, pi, which) in [(+1, p1, 1), (-1, p2, 2)]:
        f = (lambda P: Mn_scalar(P, p2, ext)) if which == 1 else (lambda P: Mn_scalar(p1, P, ext))
        dnu = grad(f, pi)      # d^nu M
        orb = dot(eps, pi)*dot(k, lower(g @ dnu)) if False else None
        # eps*_mu k_nu (p^mu d^nu - p^nu d^mu) M = (eps.p)(k.d M) - (k.p)(eps.d M), with k.d = k_nu d^nu
        kd = dot(k, dnu); ed = dot(eps, dnu)
        res += -e_c*Qi*(dot(eps, pi)/dot(k, pi)*Ms_ + (dot(eps, pi)*kd - dot(k, pi)*ed)/dot(k, pi))
    return res

print("--- scalar QED (internal charged lines) ---")
diffs = []
for lam in [1e-1, 5e-2, 2.5e-2, 1.25e-2]:
    p1, p2, k = kinematics(lam); eps = polarization(k)
    Mv = Mnp1_scalar_vec(p1, p2, k)
    ward = dot(k, Mv)
    exact = dot(eps, Mv)             # eps real -> eps*
    lowp = low_scalar(p1, p2, k, eps, 0)
    lowp1 = low_scalar(p1, p2, k, eps, 1)
    eik = sum(-e_c*Qi*dot(eps, pi)/dot(k, pi) for Qi, pi in [(+1, p1), (-1, p2)])*Mn_scalar(p1, p2, 0)
    diffs.append(abs(exact - lowp))
    print(f"   lam={lam:8.5f}: |k.M|={abs(ward):.2e}  exact={exact:.6e}  Low={lowp:.6e}  |exact-Low|={abs(exact-lowp):.3e}"
          f"  |Low(ext0)-Low(ext1)|={abs(lowp-lowp1):.2e}  |exact-eikonal|={abs(exact-eik):.3e}")
rat = [diffs[i]/diffs[i+1] for i in range(3)]
print("   ratios |Delta(lam)|/|Delta(lam/2)| =", [f"{r:.3f}" for r in rat])
check("scalar: Ward identity k.M_{n+1} = 0", all(True for _ in [0]) and abs(dot(k, Mnp1_scalar_vec(*kinematics(0.05)))) < 1e-10)
check("scalar: exact - Low = O(k) (ratios -> 2)", all(abs(r - 2) < 0.1 for r in rat))
p1, p2, k = kinematics(0.0125); eps = polarization(k)
check("scalar: Low formula independent of the off-shell extension (ext0 vs ext1, diff << O(k^0))",
      abs(low_scalar(p1, p2, k, eps, 0) - low_scalar(p1, p2, k, eps, 1)) < 1e-2*abs(low_scalar(p1, p2, k, eps, 0))*0.0125*10)

# ===================== spinor QED =====================
def S(l): return 1j*(slash(l) + m*E4)/(dot(l, l) - m**2)
def Mtilde(p1, p2, ext=0):
    if ext == 0: lt, lu = q2 - p2, q1 - p2
    else: lt, lu = p1 - q1, p1 - q2
    return -1j*((-1j*gc)**2*(S(lt) + S(lu)))      # stripped amplitude: M_n = ubar(p1) Mtilde v(p2)
def Mnp1_spinor_vec(p1, p2, k, s1, s2):
    ub = bar(spinor_u(p1, m, s1)); v = spinor_v(p2, m, s2)
    out = np.zeros(4, complex)
    for mu in range(4):
        G = 1j*e_c*gam[mu]           # i e Q gamma^mu, Q=+1 field ; upper index mu
        # emission from ubar end (outgoing fermion): ubar G S(p1+k) [hard with p1+k] v
        hard1 = (-1j*gc)**2*(S(q2 - p2) + S(q1 - p2))     # internal momenta with fermion at p1+k: q2-p2, q1-p2
        t1 = ub @ G @ S(p1 + k) @ hard1 @ v
        # emission from v end (outgoing antifermion): ubar [hard with -p2-k] S(-p2-k) G v
        hard2 = (-1j*gc)**2*(S(q2 - p2 - k) + S(q1 - p2 - k))
        t2 = ub @ hard2 @ S(-p2 - k) @ G @ v
        # internal: ubar (-ig) S(la - k) G S(la) (-ig) v,  la = q2 - p2 (t) or q1 - p2 (u)
        t3 = ub @ ((-1j*gc)*S(q2 - p2 - k) @ G @ S(q2 - p2)*(-1j*gc)) @ v
        t4 = ub @ ((-1j*gc)*S(q1 - p2 - k) @ G @ S(q1 - p2)*(-1j*gc)) @ v
        out[mu] = -1j*(t1 + t2 + t3 + t4)
    return out
def low_spinor(p1, p2, k, eps, s1, s2, ext=0, h=1e-6):
    ub = bar(spinor_u(p1, m, s1)); v = spinor_v(p2, m, s2)
    Mt = Mtilde(p1, p2, ext)
    Mn = ub @ Mt @ v
    def dMt(which, nu_idx):   # d/dp^rho of Mtilde, returns list over rho (lower-index derivative d_rho)
        res = []
        for r in range(4):
            dp = np.zeros(4); dp[r] = h
            if which == 1: res.append((Mtilde(p1 + dp, p2, ext) - Mtilde(p1 - dp, p2, ext))/(2*h))
            else: res.append((Mtilde(p1, p2 + dp, ext) - Mtilde(p1, p2 - dp, ext))/(2*h))
        return res
    total = 0
    epsl = lower(eps); kl = lower(k)
    for (Qi, pi, which) in [(+1, p1, 1), (-1, p2, 2)]:
        d_low = dMt(which, None)        # d_rho Mtilde
        # k.d = k^rho d_rho ; eps.d = eps^rho d_rho
        kd = sum(k[r]*d_low[r] for r in range(4)); ed = sum(eps[r]*d_low[r] for r in range(4))
        orb = ub @ ((dot(eps, pi)*kd - dot(k, pi)*ed)) @ v
        # spin: eps*_mu k_nu Sigma^{mu nu}
        SS = sum(epsl[a]*kl[b]*sigma(a, b) for a in range(4) for b in range(4))
        if which == 1: spin = ub @ (-0.5j*SS) @ Mt @ v
        else: spin = ub @ Mt @ (0.5j*SS) @ v
        total += -e_c*Qi*(dot(eps, pi)/dot(k, pi)*Mn + (orb + spin)/dot(k, pi))
    return total

print("--- spinor QED (internal charged lines) ---")
okall = True
for (s1, s2) in [(0, 0), (0, 1), (1, 0), (1, 1)]:
    diffs = []
    for lam in [1e-1, 5e-2, 2.5e-2, 1.25e-2]:
        p1, p2, k = kinematics(lam); eps = polarization(k)
        Mv = Mnp1_spinor_vec(p1, p2, k, s1, s2)
        exact = dot(eps, Mv); lowp = low_spinor(p1, p2, k, eps, s1, s2, 0)
        diffs.append(abs(exact - lowp))
        if lam == 1.25e-2:
            lowp1 = low_spinor(p1, p2, k, eps, s1, s2, 1)
            # without spin term
            print(f"   spins ({s1},{s2}): |k.M|={abs(dot(k, Mv)):.1e} |exact|={abs(exact):.4e} |exact-Low|={abs(exact-lowp):.3e}"
                  f" |Low ext0-ext1|={abs(lowp-lowp1):.2e}")
    rat = [diffs[i]/diffs[i+1] for i in range(3)]
    print(f"      ratios: {[f'{r:.3f}' for r in rat]}")
    okall &= all(abs(r - 2) < 0.15 for r in rat)
check("spinor: exact - Low = O(k) for all four spin configurations (ratios -> 2)", okall)
# spin term necessary: drop it and see an O(1) mismatch
p1, p2, k = kinematics(0.0125); eps = polarization(k)
Mv = Mnp1_spinor_vec(p1, p2, k, 0, 1); exact = dot(eps, Mv)
def low_nospin(p1, p2, k, eps, s1, s2, h=1e-6):
    ub = bar(spinor_u(p1, m, s1)); v = spinor_v(p2, m, s2); Mt = Mtilde(p1, p2, 0); Mn = ub @ Mt @ v
    tot = 0
    for (Qi, pi, which) in [(+1, p1, 1), (-1, p2, 2)]:
        d_low = []
        for r in range(4):
            dp = np.zeros(4); dp[r] = h
            d_low.append((Mtilde(p1 + dp, p2) - Mtilde(p1 - dp, p2))/(2*h) if which == 1 else (Mtilde(p1, p2 + dp) - Mtilde(p1, p2 - dp))/(2*h))
        kd = sum(k[r]*d_low[r] for r in range(4)); ed = sum(eps[r]*d_low[r] for r in range(4))
        tot += -e_c*Qi*(dot(eps, pi)/dot(k, pi)*Mn + (ub @ (dot(eps, pi)*kd - dot(k, pi)*ed) @ v)/dot(k, pi))
    return tot
print("   without the spin term: |exact - Low_nospin| =", f"{abs(exact - low_nospin(p1, p2, k, eps, 0, 1)):.3e}",
      " vs with spin term:", f"{abs(exact - low_spinor(p1, p2, k, eps, 0, 1)):.3e}")
check("spinor: the spin term is necessary (O(k^0) mismatch without it)",
      abs(exact - low_nospin(p1, p2, k, eps, 0, 1)) > 20*abs(exact - low_spinor(p1, p2, k, eps, 0, 1)))

# ===================== Burnett-Kroll (cross section) =====================
def sumsq_n(p1, p2):   # spin-summed |M_n|^2 = Tr[(p1slash+m) Mt (p2slash - m) Mtbar]
    Mt = Mtilde(p1, p2, 0); Mtb = gam[0] @ Mt.conj().T @ gam[0]
    return np.real(np.trace((slash(p1) + m*E4) @ Mt @ (slash(p2) - m*E4) @ Mtb))
def BK(p1, p2, k, h=1e-6):
    base = sumsq_n(p1, p2)
    charges = [(+1, p1, 1), (-1, p2, 2)]
    lead = 0; sub = 0
    for (Qi, pi, _) in charges:
        for (Qj, pj, wj) in charges:
            lead += -e_c**2*Qi*Qj*dot(pi, pj)/(dot(pi, k)*dot(pj, k))*base
            # L_j^{mu nu} = p_j^mu d^nu - p_j^nu d^mu acting on sumsq ; contracted with p_{i mu} k_nu:
            # p_i.p_j (k.d) - (k.p_j)(p_i.d)
            grad_low = []
            for r in range(4):
                dp = np.zeros(4); dp[r] = h
                if wj == 1: grad_low.append((sumsq_n(p1 + dp, p2) - sumsq_n(p1 - dp, p2))/(2*h))
                else: grad_low.append((sumsq_n(p1, p2 + dp) - sumsq_n(p1, p2 - dp))/(2*h))
            kd = sum(k[r]*grad_low[r] for r in range(4)); pid = sum(pi[r]*grad_low[r] for r in range(4))
            sub += -e_c**2*Qi*Qj*(dot(pi, pj)*kd - dot(k, pj)*pid)/(dot(pi, k)*dot(pj, k))
    return lead + sub, lead
print("--- Burnett-Kroll, unpolarized ---")
res = []
for lam in [1e-1, 5e-2, 2.5e-2, 1.25e-2, 6.25e-3]:
    p1, p2, k = kinematics(lam)
    tot = 0
    for s1 in (0, 1):
        for s2 in (0, 1):
            Mv = Mnp1_spinor_vec(p1, p2, k, s1, s2)
            tot += -np.real(dot(Mv, Mv.conj()))      # -g_{mu nu} M^mu M^nu*
    bk, lead = BK(p1, p2, k)
    res.append((lam, tot, bk, lead))
    print(f"   lam={lam:8.5f}: exact={tot:.6e}  BK(2 terms)={bk:.6e}  exact-BK={tot-bk:.4e}  exact-eikonal={tot-lead:.4e}")
d = [abs(r[1] - r[2]) for r in res]; d0 = [abs(r[1] - r[3]) for r in res]
print("   |exact-BK| should stay O(1) while exact ~ 1/lam^2;  |exact-eikonal| should grow ~ 1/lam")
check("Burnett-Kroll: exact - (two-term formula) = O(k^0)", max(d)/min(d) < 3 and res[-1][1]*res[-1][0]**2 > 0)
check("Burnett-Kroll: the O(1/k) term is needed (exact - eikonal grows like 1/k)", d0[-1]/d0[0] > 8)
print("ALL PASS" if OK else "SOME CHECKS FAILED")
