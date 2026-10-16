# X1 review round 3, reviewer 1 -- end-to-end test of T2 (fully coincident SS pair at O(g^4), H_glob model) for
# GENERAL jets of class (J)+(Sp)+(R)+NF (jet A) and (J)+(Sp)+(Sp')+(R)+NF (jet B), i.e. beyond the factorized scalar
# model on which all previous numerics were done.  Independent implementation (own parametrization of the strip).
#
# Rotated contour (L5, theta = pi/2), k^+ = i kappa:
#   h_pi(kappa) = (a1 a2/Jcal_A) F_A^[pi](i kappa),  F_A^[pi] from the quadrant formula L3:
#       F_A^[pi](k^+) = prod_e (-i sgn(k_e^+) r_e) J_A^(sigma(pi,Q))(z_1, z_2),  r_e = 1/(2k_e^+), z_e = a_e/(2k_e^+)
#       => h_pi = (a1 a2/Jcal_A) J_A^(sigma)(-i a1/(2 kappa1), -i a2/(2 kappa2)) / (4|kappa1||kappa2|)
#       sigma: (+,+) -> FF^[pi];  (-,-) -> BB^[pi];  (-,+) -> BF (only [12]);  (+,-) -> BFp (only [21])
#   f_pi(kappa) = J_B^[pi](-i kappa)
#   X(piA,piB) := W(piA,piB) N/N_0 = -(1/Jcal_B) int h_piA f_piB d^2kappa/(2pi)^2,  N/N_0 = sum X,  p_opp = W(12,21)+W(21,12)
# Diagonal quadrants: log-log Gauss-Legendre grid.  Off-diagonal quadrants: (v = |positive kappa|, U = kappa1+kappa2) with
# U = lam_B sinh(s), s in [asinh(-Umax/lam_B), asinh(v/lam_B)]  (uniform resolution of the strip |U| <~ lam_B).
import sys, os, time, copy
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from genjet import Jet, random_general_jet, check_spprime, SECTORS

SIG = {('12', (1, 1)): 'FF', ('21', (1, 1)): 'FFp', ('12', (-1, -1)): 'BB', ('21', (-1, -1)): 'BBp',
       ('12', (-1, 1)): 'BF', ('21', (1, -1)): 'BFp'}


def gl(n, a, b):
    x, w = np.polynomial.legendre.leggauss(n)
    return 0.5*(b - a)*x + 0.5*(b + a), 0.5*(b - a)*w


def scaled(jet, s):
    """copy of jet with all energies multiplied by s and c_t -> c_t s^(+d_t) (keeps M = sum |c_t| lam^-d_t invariant:
    the physical scaling of a jet whose energies are O(lambda^2 Q))"""
    out = Jet(); out.phase = jet.phase
    for sct in SECTORS:
        out.terms[sct] = [(c*s**(len(g1) + len(g2) - 2), [s*A for A in g1], [s*A for A in g2])
                          for (c, g1, g2) in jet.terms[sct]]
    return out


def hfun(jetA, a1, a2, col, q, k1, k2):
    key = (col, q)
    if key not in SIG:
        return np.zeros_like(k1, dtype=complex)
    z1 = -1j*a1/(2*k1); z2 = -1j*a2/(2*k2)
    J = jetA.sector(SIG[key], z1, z2)
    return (a1*a2/jetA.Jcal('BB'))*J/(4*np.abs(k1)*np.abs(k2))


def ffun(jetB, col, k1, k2):
    return jetB.colour(col, -1j*k1, -1j*k2)


def integrate(fun, lamB, tlo, thi, n_d=500, n_v=500, n_s=500):
    # lamB here is the sinh scale of the strip variable U (callers pass mu_B, the smallest B energy)
    """int over R^2 of fun(k1, k2, q) d^2kappa, quadrant by quadrant"""
    tot = 0.0
    t, w = gl(n_d, tlo, thi)
    T1, T2 = np.meshgrid(t, t, indexing='ij'); W = np.outer(w, w)
    for q in ((1, 1), (-1, -1)):
        tot = tot + np.sum(W*np.exp(T1 + T2)*fun(q[0]*np.exp(T1), q[1]*np.exp(T2), q))
    tv, wv = gl(n_v, tlo, thi)
    xs, ws = np.polynomial.legendre.leggauss(n_s)
    Umax = np.exp(thi + 2)
    smin = np.arcsinh(-Umax/lamB)
    V = np.exp(tv)
    smax = np.arcsinh(V/lamB*(1 - 1e-15))
    # s-grid per v: s = smin + (smax - smin) (x+1)/2
    Sg = smin + (smax[:, None] - smin)*(xs[None, :] + 1)/2
    Ws = (smax[:, None] - smin)/2*ws[None, :]
    U = lamB*np.sinh(Sg); dU = lamB*np.cosh(Sg)*Ws
    Vg = V[:, None]*np.ones_like(Sg); Wv = (wv*V)[:, None]
    for q in ((-1, 1), (1, -1)):
        if q == (-1, 1):
            k2 = Vg; k1 = U - Vg
        else:
            k1 = Vg; k2 = U - Vg
        tot = tot + np.sum(Wv*dU*fun(k1, k2, q))
    return tot


def popp(jetA, jetB, a1, a2, tlo, thi, n=500, retall=False):
    lamB, muB = jetB.lam_mu()
    JcB = jetB.Jcal('BB')
    X = {}
    sc = muB
    for cA in ('12', '21'):
        for cB in ('12', '21'):
            fun = lambda k1, k2, q, cA=cA, cB=cB: hfun(jetA, a1, a2, cA, q, k1, k2)*ffun(jetB, cB, k1, k2)
            X[(cA, cB)] = -integrate(fun, sc, tlo, thi, n, n, n)/(2*np.pi)**2/JcB
    N = sum(X.values())
    W = {k: v/N for k, v in X.items()}
    p = W[('12', '21')] + W[('21', '12')]
    return (p, N, W) if retall else (p, N)


def scalar_jet(M, ma, ms, xs, sT, k1T, k2T):
    E = lambda pT, m, pp: (pT[0]**2 + pT[1]**2 + m**2)/(2*pp)
    P = M**2/2
    sub = lambda u, v: (u[0] - v[0], u[1] - v[1])
    s0T = sub(sub(sT, k1T), k2T); s1T = sub(sT, k2T); s2T = sub(sT, k1T)
    aT = (-s0T[0], -s0T[1])
    Ea = E(aT, ma, 1 - xs); Es = E(sT, ms, xs)
    Es0 = E(s0T, ms, xs); Es1 = E(s1T, ms, xs); Es2 = E(s2T, ms, xs)
    d0 = P - Ea - Es0; d10 = P - Ea - Es1; d20 = P - Ea - Es2; beta = Ea + Es - P
    al0 = Es - Es0; al1 = Es - Es1; al2 = Es - Es2
    jet = Jet()
    c = 1j/d0
    e = {'1': d10, '2': d20, '12': -beta, 'V': al0, '1V': al1, '2V': al2}
    jet.add('BB', c, [e['1']], [e['12']]); jet.add('BF', c, [e['1']], [e['1V']]); jet.add('FF', c, [e['V']], [e['1V']])
    jet.add('FFp', c, [e['V']], [e['2V']]); jet.add('BFp', c, [e['2']], [e['2V']]); jet.add('BBp', c, [e['2']], [e['12']])
    return jet, e


if __name__ == '__main__':
    out = []
    def log(s):
        print(s, flush=True); out.append(s)
    logpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'review_r3_1_logs', 't2_general.log')
    mode = sys.argv[1] if len(sys.argv) > 1 else 'all'

    # ---------------- (0) validation on the scalar base set (twoexch_model.py run(): lambda = 1 shapes) -------------
    from genjet import check_R
    k1T = (0.8, 0.1); k2T = (-0.3, 0.9)
    a1 = k1T[0]**2 + k1T[1]**2; a2 = k2T[0]**2 + k2T[1]**2
    jA0, eA = scalar_jet(0.9, 0.5, 0.7, 0.4, (0.3, 0.2), k1T, k2T)
    jB, eB = scalar_jet(0.8, 0.6, 0.5, 0.55, (-0.25, 0.4), (-k1T[0], -k1T[1]), (-k2T[0], -k2T[1]))
    lamB, muB = jB.lam_mu()
    NV = 1600
    if mode in ('all', 'val'):
        log(f"(0) scalar base set: jet A energies {eA};  jet B energies {eB};  a1={a1:.3f} a2={a2:.3f}")
        log(f"    NF_A: {all(eA[k] < 0 for k in ('V','1V','2V'))};  NF_B: {all(eB[k] < 0 for k in ('V','1V','2V'))}")
        for n in (800, 1600):
            v = -integrate(lambda k1, k2, q: ffun(jB, '12', k1, k2) + ffun(jB, '21', k1, k2), muB, np.log(muB) - 14, 18.0, n, n, n)/(2*np.pi)**2/jB.Jcal('BB')
            log(f"    integrator check n={n}: -(1/Jcal_B) int S_B d^2k/(2pi)^2 = {v:.8f}")
        ref = {0.01: 0.0123471, 0.003: 0.0020476, 0.001: 0.0003448}
        for lam in (0.01, 0.003, 0.001):
            jA = scaled(jA0, lam**2)
            lamA, muA = jA.lam_mu(); eps = lamA*lamB/np.sqrt(a1*a2)
            for n in (1200, 1600):
                p, N = popp(jA, jB, a1, a2, np.log(muB) - 14, np.log(np.sqrt(a1*a2)/lamA) + 12, n)
                log(f"    lambda={lam} (eps={eps:.3e}), n={n}: p_opp = {p.real:.7f}{p.imag:+.6f}i ;  N/N0 = {N.real:.7f}{N.imag:+.7f}i"
                    f"   [reference Re p_opp = {ref[lam]}]")

    # ---------------- (1) general (non-factorized) jets ----------------
    if mode in ('all', 'gen'):
        rng = np.random.default_rng(777)
        for jt in range(3):
            while True:
                jBg = random_general_jet(rng, 10**rng.uniform(-1.3, -0.7), n_orbit=2, n_wind=1, n_chain=4, n_iso=2, phase=1j)
                if abs(jBg.Jcal('BB')) > 0.3 and check_spprime(jBg):
                    break
            while True:
                jAg = random_general_jet(rng, 10**rng.uniform(-1.3, -0.7), n_orbit=2, n_wind=1, n_chain=3, n_iso=2, phase=1j)
                if abs(jAg.Jcal('BB')) > 0.3:
                    break
            if jt == 2:   # J_A violating (Sp') (T2 requires only (Sp) of J_A)
                c, g1, g2 = jAg.terms['FF'][0]
                jAg.terms['FF'][0] = (c, [0.6*g1[0]], g2)
            lamBg, muBg = jBg.lam_mu()
            log(f"(1) general pair {jt}: J_B (Sp')={check_spprime(jBg)}, (R)-violation={check_R(jBg):.1e}, lam_B={lamBg:.3f}, mu_B={muBg:.3f}, "
                f"terms/sector={[len(jBg.terms[x]) for x in SECTORS]};  J_A (Sp')={check_spprime(jAg)}, (R)-violation={check_R(jAg):.1e}, "
                f"terms/sector={[len(jAg.terms[x]) for x in SECTORS]}")
            ag1, ag2 = 0.9, 1.3
            for sA in (1e-2, 1e-3, 1e-4):
                jA = scaled(jAg, sA)
                lamA, muA = jA.lam_mu(); eps = lamA*lamBg/np.sqrt(ag1*ag2)
                for n in ((1200, 1600) if sA == 1e-4 else (1200,)):
                    p, N = popp(jA, jBg, ag1, ag2, np.log(muBg) - 14, np.log(np.sqrt(ag1*ag2)/lamA) + 12, n)
                    log(f"    eps={eps:.2e} n={n}: Re p_opp = {p.real:+.7f}   Im p_opp = {p.imag:+.5f}   N/N0 = {N.real:.6f}{N.imag:+.6f}i"
                        f"   [Re p_opp/eps^0.5 = {p.real/np.sqrt(eps):+.4f}]")

    # ---------------- (2) P4(b): (Sp') status of the perturbation and effect of its (Sp')-partner ----------------
    if mode in ('all', 'p4'):
        lamA0, muA0 = jA0.lam_mu(); Jc = jA0.Jcal('BB')
        A1, A2, Ap, App = -0.7*lamA0, -0.45*lamA0, -0.55*lamA0, -0.8*lamA0
        r = 1.0
        c2 = -1j*r*Jc*lamA0        # c_2 = -i ct_2, ct_2/c_1 = r lam_A real; (R) holds
        sP = 0.05
        def perturbed(partner):
            j = scaled(jA0, 1.0)
            j.add('BF', sP*c2, [A1, A2], [Ap])
            if partner:
                j.add('BB', sP*c2, [A1, A2], [App])
            return j
        jP = perturbed(False); jPP = perturbed(True)
        log(f"(2) P4(b): perturbation s c_2 [i/(A1+k1)][i/(A2+k1)][i/(A'-k2)] in sector 1V2 (BF) of the scalar jet A:"
            f" (Sp') of J_A without partner = {check_spprime(jP)}, with the BB partner = {check_spprime(jPP)};"
            f" (R)-violation {check_R(jP):.1e}, {check_R(jPP):.1e}")
        # prediction: delta W(12,21) = -(i s/2pi) int_0^inf dk/k rho2(k), rho2 = (a1 a2/c1) 2k ct2 / [(2kA1-a1)(2kA2-a1)(2kA'-a2)]
        ct2 = 1j*c2
        rho2 = lambda k: (a1*a2/Jc)*2*k*ct2/((2*k*A1 - a1)*(2*k*A2 - a1)*(2*k*Ap - a2))
        t, w = gl(4000, -30, 30); kk = np.exp(t)
        I2 = np.sum(w*rho2(kk))
        pred = -1j*sP/(2*np.pi)*I2
        log(f"    rho2 sign on (0,inf): {np.sign(rho2(kk).real).min()} .. {np.sign(rho2(kk).real).max()}, Im/Re max {np.max(np.abs(rho2(kk).imag)):.1e};"
            f"  prediction delta W(12,21) = {pred:.6f}")
        for lam in (0.01, 0.003):
            res = {}
            for lab, j in (('base', jA0), ('P4', jP), ('P4+partner', jPP)):
                jA = scaled(j, lam**2); lamA, muA = jA.lam_mu()
                p, N, W = popp(jA, jB, a1, a2, np.log(muB) - 14, np.log(np.sqrt(a1*a2)/lamA) + 12, 1200, retall=True)
                res[lab] = (p, N, W)
            dW = res['P4'][2][('12', '21')] - res['base'][2][('12', '21')]
            dWp = res['P4+partner'][2][('12', '21')] - res['base'][2][('12', '21')]
            dp = res['P4'][0] - res['base'][0]; dpp = res['P4+partner'][0] - res['base'][0]
            log(f"    lambda={lam}: delta W(12,21) [no partner] = {dW:.6f};  [with BB partner] = {dWp:.6f};  "
                f"difference = {dWp - dW:.2e};  delta p_opp = {dp:.2e} / {dpp:.2e}")
    with open(logpath, 'a') as fh:
        fh.write("\n".join(out) + "\n")
