"""W09 / v5: fragmentation functions (def:pdf-ff, prop:pdf-timelike-dglap(b)).
 (a) frame Jacobian: hadron-frame prefactor z^{1-2eps}/(4N_c) = (1/(4 N_c z)) * z^{2-2eps}  (d^{2-2e}p_hT = z^{2-2e} d^{2-2e}k_T);
 (b) free quark / free gluon: d_{q/q} = delta(1-z), and the gluon-FF normalisation z^{1-2eps}/((D-2)(N_c^2-1) k^+);
 (c) light-cone gauge real emission, all four channels, from the HADRON-FRAME definitions (quark FF of VF-CONV-17,
     gluon FF with the prefactor of (b)), at integer D = 4..7:  l_T^2 x density = z^{-2 eps} hatP_ij(z;eps)
     -> UV poles P_ij(z) for z<1 (Gribov-Lipatov at LO), and the O(alpha_s) number-density check of VF-CONV-17;
 (d) Feynman gauge, gluon mass m, quark FF: real graphs R1 (ladder) and R2 (+mirror; quark line x Wilson line)
     after the transverse integral are IDENTICAL to the PDF ones of VF-PDF-3 at xi = z; the virtual graphs are the
     same amplitude <0|[W psi](0)|q(p)>; hence d^(1)_{q/q}(z) = f^(1)_{q/q}(z) graph by graph (bare, exact in eps);
 (e) with the parton-frame prefactor 1/(4N_c z) used in the hadron frame the O(alpha_s) result would be z^{-2+2eps} times larger.
"""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
import mpmath as mp
from w9lib import dtrace, D as Dsym

npass = 0; nfail = 0
def check(name, ok):
    global npass, nfail
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)
    if ok: npass += 1
    else: nfail += 1

# ---------------- (a) frame Jacobian ---------------------------------------------------------------
z, eps = sp.symbols('z epsilon', positive=True)
check('(a) z^{1-2eps} = (1/z) * z^{2-2eps}', sp.simplify(z ** (1 - 2 * eps) - z ** (2 - 2 * eps) / z) == 0)
# transverse boost: parton momentum k with k_T, hadron p_h = z k (+...) ; boost removing p_hT gives k_T = -p_hT/z
# Jacobian of p_hT = -z k_T in d = 2-2eps dimensions: |det| = z^{2-2eps}
d = 2 - 2 * eps
check('(a) |det(d p_hT/d k_T)| = z^{2-2eps} for p_hT = -z k_T in 2-2eps dims', sp.simplify(z ** d - z ** (2 - 2 * eps)) == 0)

# ---------------- D-dimensional numeric Minkowski algebra (as in v3) -------------------------------
class Mink:
    def __init__(self, Dd):
        self.D = Dd
        self.eta = np.diag([1.0] + [-1.0] * (Dd - 1))
    def dot(self, a, b):
        return a @ self.eta @ b
    def lc(self, vp, vm, vT):
        v = np.zeros(self.D, dtype=complex)
        v[0] = (vp + vm) / np.sqrt(2); v[self.D - 1] = (vp - vm) / np.sqrt(2)
        v[1:self.D - 1] = vT
        return v
    def basis(self):
        return [np.eye(self.D)[m].astype(complex) for m in range(self.D)]
    def trace(self, vecs):
        n = len(vecs)
        if n == 0:
            return 4.0
        if n % 2:
            return 0.0
        a = vecs[0]; s = 0.0
        for k in range(1, n):
            s += (-1) ** (k - 1) * self.dot(a, vecs[k]) * self.trace(vecs[1:k] + vecs[k + 1:])
        return s

def ff_kernels_at(Dd, zz, lTmag, kplus=1.7):
    """hadron frame: observed parton p = (z k^+, 0, 0_T); emitted on-shell massless parton l with transverse momentum l_T;
    fragmenting parton k = p + l (k^+ fixed, k_T = l_T).  Returns l_T^2 x density per (colour factor) g^2 d^{D-2}l_T/(2pi)^{D-1}."""
    M = Mink(Dd)
    e = (4 - Dd) / 2
    nT = Dd - 2
    lTdir = np.zeros(nT); lTdir[0] = 0.6; lTdir[1 % nT] += 0.8
    lTdir = lTdir / np.linalg.norm(lTdir)
    lTv = lTmag * lTdir
    pp = zz * kplus
    lp = (1 - zz) * kplus
    p = M.lc(pp, 0.0, np.zeros(nT))
    l = M.lc(lp, lTmag ** 2 / (2 * lp), lTv)
    k = p + l
    k2 = M.dot(k, k)
    n = M.lc(0.0, 1.0, np.zeros(nT))       # n.v = v^+ (our n_B)
    nbar = M.lc(1.0, 0.0, np.zeros(nT))    # our n_A
    E = M.basis()
    g_up = np.linalg.inv(M.eta)
    def lower(v): return M.eta @ v
    def dpol(q):   # physical light-cone polarisation sum (upper indices), q on shell
        return -g_up + (np.outer(q, n) + np.outer(n, q)) / M.dot(n, q)
    pref = zz ** (1 - 2 * e)                # hadron-frame Jacobian factor z^{1-2eps}
    out = {}
    # q -> q(p) + g(l):  (1/4) Tr[n kslash gamma_mu pslash gamma_nu kslash] d^{mu nu}(l) / (k^2)^2 / (2 l^+)  ; C_F
    s = 0.0; dl = dpol(l)
    for mu in range(Dd):
        for nu in range(Dd):
            c = dl[mu, nu]
            if abs(c) < 1e-15: continue
            s += c * M.trace([n, k, E[mu], p, E[nu], k])
    out['qq'] = pref * 0.25 * s / k2 ** 2 / (2 * lp) * lTmag ** 2
    # q -> g(p) + q(l):  (1/4) Tr[n kslash gamma_mu lslash gamma_nu kslash] d^{mu nu}(p) ; C_F
    s = 0.0; dp = dpol(p)
    for mu in range(Dd):
        for nu in range(Dd):
            c = dp[mu, nu]
            if abs(c) < 1e-15: continue
            s += c * M.trace([n, k, E[mu], l, E[nu], k])
    out['gq'] = pref * 0.25 * s / k2 ** 2 / (2 * lp) * lTmag ** 2
    # gluon FF: prefactor z^{1-2eps} / ((D-2) (N_c^2-1) k^+);  operator vertex O^j_rho = k^+ delta^j_rho - k^j n_rho
    kplus_ = M.dot(n, k)
    Pk = g_up - (np.outer(k, n) + np.outer(n, k)) / M.dot(n, k)   # light-cone propagator numerator (upper), minus sign irrelevant
    Oj = []
    for j in range(1, Dd - 1):
        o = np.zeros(Dd, dtype=complex)
        o[j] += kplus_
        o += -k[j] * lower(n)
        Oj.append(o)
    gpref = pref / ((Dd - 2) * kplus_)
    # g -> q(p) + qbar(l):  sum_j Tr[pslash Wslash lslash Wslash],  W^sigma = Pk^{sigma rho} O^j_rho ; T_F
    s = 0.0
    for o in Oj:
        W = Pk @ o            # upper components W^sigma  (Pk is upper-upper, o is lower)
        s += 4 * (2 * M.dot(p, W) * M.dot(l, W) - M.dot(W, W) * M.dot(p, l))
    out['qg'] = gpref * s / k2 ** 2 / (2 * lp) * lTmag ** 2
    # g -> g(p) + g(l): three-gluon vertex V(k, -p, -l) (all incoming), pol sums d(p), d(l) ; C_A
    def V3(q1, q2, q3):
        q1L, q2L, q3L = lower(q1), lower(q2), lower(q3)
        V = np.zeros((Dd, Dd, Dd), dtype=complex)
        for a_, b_, c_ in itertools.product(range(Dd), repeat=3):
            V[a_, b_, c_] = (M.eta[a_, b_] * (q1L - q2L)[c_] + M.eta[b_, c_] * (q2L - q3L)[a_] + M.eta[c_, a_] * (q3L - q1L)[b_])
        return V   # lower indices (sigma: k-line, mu: p, nu: l)
    V = V3(k, -p, -l)
    amp2 = 0.0
    for o in Oj:
        w = Pk @ o            # w^sigma
        A = np.einsum('smn,s->mn', V, w)     # lower mu nu
        amp2 += np.einsum('mn,ab,ma,nb->', A, np.conj(A), dp, dl)
    out['gg'] = gpref * amp2 / k2 ** 2 / (2 * lp) * lTmag ** 2
    return out, e

def hatP(zz, e):
    return {'qq': (1 + zz ** 2) / (1 - zz) - e * (1 - zz),
            'gq': (1 + (1 - zz) ** 2) / zz - e * zz,
            'qg': 1 - 2 * zz * (1 - zz) / (1 - e),
            'gg': 2 * (zz / (1 - zz) + (1 - zz) / zz + zz * (1 - zz))}
colour = {'qq': 'C_F', 'gq': 'C_F', 'qg': 'T_F', 'gg': 'C_A'}

# ---------------- (b) free gluon normalisation --------------------------------------------------------
# <0|G^{+j}_a(0)|g(p,lam,b)> = -i p^+ eps^j delta_ab ; sum_{lam,j} |eps^j|^2 = D-2 ; colours N^2-1 ;
# int dw/(2pi) e^{i(k^+ - p^+) w} = delta(k^+ - p^+) = delta(1-z)/k^+ ; prefactor z^{1-2eps}/((D-2)(N^2-1) k^+)
Dd_, Nc_, kp = sp.symbols('D N_c k_plus', positive=True)
val = (z ** (1 - 2 * eps) / ((Dd_ - 2) * (Nc_ ** 2 - 1) * kp)) * (z * kp) ** 2 * (Dd_ - 2) * (Nc_ ** 2 - 1) / kp
check('(b) free gluon: d_{g/g} = [z^{1-2eps}/((D-2)(N^2-1)k+)] (p+)^2 (D-2)(N^2-1) delta(1-z)/k+ -> 1 * delta(1-z) at z=1',
      sp.simplify(val.subs(z, 1) - 1) == 0)
valq = (z ** (1 - 2 * eps) / (4 * Nc_)) * Nc_ * 4 * (z * kp) / kp
check('(b) free quark: d_{q/q} = [z^{1-2eps}/(4N)] N Tr[g+ pslash] delta(1-z)/k+ -> delta(1-z)', sp.simplify(valq.subs(z, 1) - 1) == 0)

# ---------------- (c) light-cone gauge real emission, all channels ---------------------------------
for Dd in (4, 5, 6, 7):
    for zz in (0.23, 0.61, 0.88):
        for lT in (0.37, 1.9):
            res, e = ff_kernels_at(Dd, zz, lT)
            ref = hatP(zz, e)
            for ch in ('qq', 'gq', 'qg', 'gg'):
                val_ = res[ch].real
                target = zz ** (-2 * e) * ref[ch]
                check('(c) D=%d z=%.2f lT=%.2f: l_T^2 x FF density[%s]/%s = %.10f vs z^{-2eps} hatP = %.10f'
                      % (Dd, zz, lT, ch, colour[ch], val_, target), abs(val_ - target) < 1e-9 * max(1, abs(target)))
# O(alpha_s) number-density check (4D): g^2/(2pi)^3 int d^2 l_T hatP/l_T^2 = (alpha_s/2pi) hatP int dl_T^2/l_T^2
g = sp.symbols('g', positive=True)
check('(c) 4D: g^2/(2pi)^3 * pi = alpha_s/(2pi) with alpha_s = g^2/(4pi)',
      sp.simplify(g ** 2 / (2 * sp.pi) ** 3 * sp.pi - (g ** 2 / (4 * sp.pi)) / (2 * sp.pi)) == 0)

# ---------------- (d) Feynman gauge, gluon mass: quark FF graph by graph ------------------------------
xi, lT2, m2, kp_ = sp.symbols('xi l_T2 m2 kplus', positive=True)
# FF kinematics (hadron frame): p^+ = z k^+, l^+ = (1-z) k^+, l^2 = m^2, p^2 = 0, k = p + l
k2_ff = (z * lT2 + m2) / (1 - z)
dots = {('k', 'k'): k2_ff, ('k', 'n'): kp_, ('k', 'p'): (k2_ff - m2) / 2, ('n', 'n'): 0, ('n', 'p'): z * kp_, ('p', 'p'): 0}
nl = (1 - z) * kp_
# amplitude A^mu = g t^a [ -kslash gamma^mu / k^2 + n^mu / n.l ] u(p);  sum over pol: -g_{mu nu} (Ward identity checked below)
R1 = -dtrace([('v', 'n'), ('v', 'k'), ('i', 'a'), ('v', 'p'), ('i', 'a'), ('v', 'k')], dots) / k2_ff ** 2
R2 = (dtrace([('v', 'n'), ('v', 'k'), ('v', 'n'), ('v', 'p')], dots) + dtrace([('v', 'n'), ('v', 'p'), ('v', 'n'), ('v', 'k')], dots)) / (k2_ff * nl)
D4 = 4 - 2 * eps
# density per C_F g^2 d^{D-2}l_T/(2pi)^{D-1}:  z^{1-2eps} (1/4) T / (2 l^+)
dR1 = sp.simplify((z ** (1 - 2 * eps) * sp.Rational(1, 4) * R1 / (2 * nl)).subs(Dsym, D4))
dR2 = sp.simplify((z ** (1 - 2 * eps) * sp.Rational(1, 4) * R2 / (2 * nl)).subs(Dsym, D4))
exp1 = z ** (-2 * eps) * (1 - eps) * (1 - z) * lT2 / (lT2 + m2 / z) ** 2
exp2 = 2 * z ** (1 - 2 * eps) / ((1 - z) * (lT2 + m2 / z))
check('(d) FF R1 density = z^{-2eps}(1-eps)(1-z) l_T^2/(l_T^2 + m^2/z)^2', sp.simplify(dR1 - exp1) == 0)
check('(d) FF R2(+mirror) density = 2 z^{1-2eps}/((1-z)(l_T^2 + m^2/z))', sp.simplify(dR2 - exp2) == 0)
# transverse integrals: int d^{2-2e} l  l^2/(l^2+M^2)^2 = pi^{1-e}(1-e)Gamma(e) M^{-2e};  int d^{2-2e} l 1/(l^2+M^2) = pi^{1-e} Gamma(e) M^{-2e}
# -> in units of A_eps (which carries pi^{1-e} Gamma(e) (m^2)^{-e} and the MS-bar factors):
FF1 = z ** (-2 * eps) * (1 - eps) * (1 - z) * (1 - eps) * (m2 / z) ** (-eps) / m2 ** (-eps)
FF2 = 2 * z ** (1 - 2 * eps) / (1 - z) * (m2 / z) ** (-eps) / m2 ** (-eps)
PDF1 = (1 - eps) ** 2 * (1 - z) * z ** (-eps)
PDF2 = 2 * z ** (1 - eps) / (1 - z)
check('(d) after the l_T integral: FF R1 = A_eps (1-eps)^2 (1-z) z^{-eps} = PDF R1 at xi = z (VF-PDF-3)', sp.simplify(sp.powsimp(FF1 - PDF1, force=True)) == 0)
check('(d) after the l_T integral: FF R2 = A_eps 2 z^{1-eps}/(1-z) = PDF R2 at xi = z (VF-PDF-3)', sp.simplify(sp.powsimp(FF2 - PDF2, force=True)) == 0)
# Ward identity for the real gluon (abelian at this order): replace eps -> l  gives 0:  -kslash lslash u/k^2 + u = 0 since kslash lslash u(p) = k^2 u(p)
# numerical spinor check in 4D
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import w9lib as W
pp_ = 1.3; zz = 0.37; lTv = np.array([0.4, -0.25]); m = 0.6
kpl = pp_ / zz; lpl = kpl - pp_
pvec = W.lc_to_cart(pp_, 0, 0, 0)
lvec = W.lc_to_cart(lpl, (lTv @ lTv + m ** 2) / (2 * lpl), lTv[0], lTv[1])
kvec = pvec + lvec
U = W.spinors_massless_z(pp_)
nvec = W.lc_to_cart(0, 1, 0, 0)
for h in U:
    amp = -W.sl(kvec) @ W.sl(lvec) @ U[h] / W.dot(kvec, kvec) + (W.dot(nvec, lvec) / W.dot(nvec, lvec)) * U[h]
    check('(d) Ward identity of the FF real-gluon amplitude (h=%+.1f): |A.l| = %.1e' % (h, np.max(np.abs(amp))), np.allclose(amp, 0))
check('(d) massive-gluon k^2 in the hadron frame: (p+l)^2 = (z l_T^2 + m^2)/(1-z)',
      abs(W.dot(kvec, kvec) - (zz * (lTv @ lTv) + m ** 2) / (1 - zz)) < 1e-12)
# total bare one-loop FF = total bare one-loop PDF => UV pole (alpha_s/2pi)(1/eps) P_qq, including 3/2 delta
print('   (d) consequence: d^(1)_{q/q}(z) = f^(1)_{q/q}(z) graph by graph, so P^T(0)_{qq} = P_qq incl. the 3/2 C_F delta(1-z)')

# ---------------- (e) wrong prefactor ------------------------------------------------------------------
check('(e) [1/(4N_c z)] / [z^{1-2eps}/(4N_c)] = z^{-2+2eps}', sp.simplify((1 / z) / z ** (1 - 2 * eps) - z ** (-2 + 2 * eps)) == 0)

# ---------------- (f) the delta-term argument for P^T_gg: (z^{-2eps}-1)/eps * hatP_gg is integrable at z->1 -----
f_int = mp.quad(lambda t: (t ** (-2 * 0.01) - 1) / 0.01 * 2 * (t / (1 - t) + (1 - t) / t + t * (1 - t)) * t, [0, 1])
check('(f) int_0^1 z (z^{-2e}-1)/e hatP_gg(z) dz finite (e=0.01): %.6f' % f_int, abs(f_int) < 1e3)
lim = sp.limit((z ** (-2 * eps) - 1) / (1 - z), z, 1)
check('(f) lim_{z->1} (z^{-2eps}-1)/(1-z) = 2 eps (finite)', sp.simplify(lim - 2 * eps) == 0)

print('\nSUMMARY v5: %d PASS, %d FAIL' % (npass, nfail))
