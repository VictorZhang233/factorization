# N10 (stage 2): independent checks of LaMET Lemma 7.2, Prop 7.3, Prop 7.4.
# Prop 7.4 METHOD (different from stage 1's Nystrom / Bessel-integral matrices): the prolate differential
# operator L_c = -(d/dx)(1-x^2)(d/dx) + c^2 x^2 (which commutes with the band-limiting operator) is
# diagonalized in the normalized Legendre basis (exact pentadiagonal matrix, no quadrature); the eigenvalue of
# F_c f(x) = int_{-1}^1 e^{icxt} f(t) dt on each prolate function is read off from F_c P_k = 2 i^k j_k(cx)
# at x = 0 (even n) or from its derivative at x = 0 (odd n); then lambda_n = (c/2pi)|mu_n|^2.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import mpmath as mp
from numpy.polynomial import legendre as Lg
npass = 0; nfail = 0
def check(name, ok, info=""):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(("PASS " if ok else "FAIL ") + name + ("  " + info if info else ""), flush=True)

# ---------------- Lemma 7.2: strip of analyticity, sharpness (model) ----------------
mp.mp.dps = 20
A, m, P, x0 = mp.mpf(1), mp.mpf('0.5'), mp.mpf(2), mp.mpf('0.3')
w = m/P
grid = [mp.mpf(j) for j in range(0, 3001, 6)]
def q_num(x, k=0):
    f = lambda lam: (1+lam)**k*A*mp.exp(-w*lam)*(mp.exp(1j*(x0-x)*lam) + mp.exp(-1j*(x0-x)*lam))/(2*mp.pi)
    return mp.quad(f, grid)
q_exact = lambda x: (A/mp.pi)*w/(w**2 + (x - x0)**2)
for x in [mp.mpf('0.1'), mp.mpf('0.7') + 0.2j*w, mp.mpf('-0.4') - 0.9j*w]:
    d = abs(q_num(x) - q_exact(x))
    check("Lemma 7.2 model: numerical FT at x=%s equals the Lorentzian continuation" % mp.nstr(x, 4), d < 1e-12, "diff %s" % mp.nstr(d, 3))
vals = [abs(q_exact(x0 + 1j*w*(1 - mp.mpf(10)**(-j)))) for j in (1, 2, 3)]
check("Lemma 7.2 sharp: model has poles at x0 +- i m/P (|q| ~ 1/delta at the edge)", abs(vals[2]/vals[1] - 10) < 0.1, str([mp.nstr(v, 6) for v in vals]))
x = x0 + 1.2j*w
parts = [abs(mp.quad(lambda lam: A*mp.exp(-w*lam)*mp.exp(-1j*(x-x0)*lam), [0, Lam])) for Lam in (20, 40, 80)]
check("Lemma 7.2 sharp: the Fourier integral diverges for |Im x| > m/P", parts[0] < parts[1] < parts[2], str([mp.nstr(p, 5) for p in parts]))

# ---------------- Prop 7.3: truncation bound and the numbers ----------------
hbarc = mp.mpf('0.1973269804')  # GeV fm
for zL, claimed in [(1, '0.079'), (mp.mpf('1.5'), '0.022')]:
    val = mp.exp(-mp.mpf('0.5')*zL/hbarc)
    check("Prop 7.3 numbers: e^{-m z_L}, m=0.5 GeV, z_L=%s fm, claimed %s" % (mp.nstr(zL, 2), claimed), abs(val - mp.mpf(claimed)) < 0.0006, mp.nstr(val, 6))
m_, P_, A_, lamL = mp.mpf('0.5'), mp.mpf('3'), mp.mpf('2'), mp.mpf('8')
bound = A_*P_/(mp.pi*m_)*mp.exp(-m_*lamL/P_)
for x in [0, mp.mpf('0.25'), mp.mpf('0.8')]:
    tail = 2*mp.quad(lambda lam: A_*mp.exp(-m_*lam/P_)*mp.cos(x*lam)/(2*mp.pi), [lamL + j for j in range(0, 400, 4)])
    check("Prop 7.3 bound holds at x=%s" % mp.nstr(x, 3), abs(tail) <= bound*(1 + mp.mpf(10)**-15), "tail %s <= bound %s" % (mp.nstr(abs(tail), 8), mp.nstr(bound, 8)))
tail0 = 2*mp.quad(lambda lam: A_*mp.exp(-m_*lam/P_)/(2*mp.pi), [lamL, mp.inf])
check("Prop 7.3 bound attained (x = 0, positive tail): it is sharp", abs(tail0/bound - 1) < 1e-15)

# ---------------- Prop 7.4: prolate eigenvalues ----------------
def prolate_lambdas(c, K=None):
    if K is None: K = int(1.5*c) + 80
    a = lambda kk: kk/np.sqrt(4.0*kk**2 - 1.0)
    P0 = np.zeros(K); dP0 = np.zeros(K)
    P0[0] = 1.0
    for kk in range(2, K, 2): P0[kk] = -(kk-1)/kk*P0[kk-2]
    for kk in range(1, K, 2): dP0[kk] = kk*P0[kk-1]
    res = []
    for parity in (0, 1):
        ks = np.arange(parity, K, 2).astype(float); n = len(ks)
        M = np.zeros((n, n))
        for i, kk in enumerate(ks):
            M[i, i] = kk*(kk+1) + c**2*(a(kk+1)**2 + (a(kk)**2 if kk > 0 else 0.0))
            if i+1 < n: M[i, i+1] = M[i+1, i] = c**2*a(kk+1)*a(kk+2)
        chi, V = np.linalg.eigh(M)
        nb = np.sqrt(ks + 0.5)
        keep = n - 15   # drop modes affected by the truncation edge (lambda ~ 0 there anyway)
        for j in range(keep):
            beta = V[:, j]
            if parity == 0:
                mu = np.sqrt(2.0)*beta[0]/np.sum(beta*nb*P0[ks.astype(int)])
            else:
                mu = 2.0*c/3.0*np.sqrt(1.5)*beta[0]/np.sum(beta*nb*dP0[ks.astype(int)])
            res.append((chi[j], (c/(2*np.pi))*mu**2))
    res.sort()
    return np.array([l for _, l in res])
claimed = {5: 3, 10: 6, 15: 10, 25: 16}
for c, cnt in claimed.items():
    lam = prolate_lambdas(float(c))
    nhalf = int(np.sum(lam > 0.5))
    near = lam[max(0, nhalf-2):nhalf+2]
    check("Prop 7.4: #{eig > 1/2} = %d for lambda_L = %d" % (cnt, c), nhalf == cnt, "eigs n=%d..%d: %s" % (max(0, nhalf-2), nhalf+1, np.array2string(near, precision=4)))
    check("Prop 7.4: trace = 2 lambda_L/pi = %.4f (lambda_L = %d)" % (2*c/np.pi, c), abs(np.sum(lam) - 2*c/np.pi) < 1e-10, "sum %.13f, smallest kept %.1e" % (np.sum(lam), lam[-1]))
    check("Prop 7.4: 0 < eig <= 1 (to rounding) and decreasing above 1e-10 (lambda_L = %d)" % c, lam.max() < 1 + 1e-12 and np.all(np.diff(lam[lam > 1e-10]) <= 5e-15), "max eig - 1 = %.1e" % (lam.max()-1))
# sanity cross-check with a sinc-kernel Gauss-Legendre Nystrom matrix
c = 10.0
xg, wg = Lg.leggauss(200)
D = xg[:, None] - xg[None, :]
with np.errstate(divide='ignore', invalid='ignore'):
    Kk = np.where(np.abs(D) > 0, np.sin(c*D)/(np.pi*D), c/np.pi)
Kmat = np.sqrt(np.outer(wg, wg))*Kk
ev = np.sort(np.linalg.eigvalsh(Kmat))[::-1][:14]
lam = prolate_lambdas(c)[:14]
check("sanity: prolate-operator eigenvalues = sinc-kernel Nystrom eigenvalues (c=10, n<14)", np.max(np.abs(ev - lam)) < 1e-11, "max diff %.2e" % np.max(np.abs(ev - lam)))
l1 = prolate_lambdas(1.0)[0]; l4 = prolate_lambdas(4.0)[0]
print("   lambda_0(c=1) = %.10f   lambda_0(c=4) = %.10f" % (l1, l4))
check("classical value lambda_0(c=1) = 0.5726 (Slepian-Pollak 1961)", abs(l1 - 0.5726) < 1e-4)
check("classical value lambda_0(c=4) = 0.99589 (Slepian-Pollak 1961)", abs(l4 - 0.99589) < 1e-5)
print("   Landau-Widom: N(alpha) - 2c/pi = (1/pi^2) ln((1-alpha)/alpha) ln c + o(ln c)")
cs = [50, 100, 200, 400, 800]
lams = {c: prolate_lambdas(float(c)) for c in cs}
for alpha in [0.5, 1e-2, 1e-4, 1e-8]:
    Dv = [np.sum(lams[c] > alpha) - 2*c/np.pi for c in cs]
    slope = np.polyfit(np.log(cs), Dv, 1)[0]
    print("     alpha=%-6g N-2c/pi = %s ; slope in ln c %.3f ; LW coefficient %.3f" % (alpha, np.array2string(np.array(Dv), precision=2), slope, np.log((1-alpha)/alpha)/np.pi**2))
# continuous Landau-Widom test: in the plunge region ln(1/lambda_n - 1) is ~ linear in n with slope pi^2/ln(c)
print("   plunge-region slope of ln(1/lambda_n - 1) vs n, times ln(c)/pi^2 (LW predicts -> 1 as c -> inf):")
rat = []; rat4 = []
for c in [25, 50, 100, 200, 400, 800, 1600]:
    lam = prolate_lambdas(float(c))
    n = np.arange(len(lam)); sel = (lam > 1e-6) & (lam < 1 - 1e-6)
    y = np.log(1/lam[sel] - 1); sl = np.polyfit(n[sel], y, 1)[0]
    rat.append(sl*np.log(c)/np.pi**2); rat4.append(sl*np.log(4*np.pi*c)/np.pi**2)
    print("     c=%5d  slope %.4f  slope*ln(c)/pi^2 = %.4f   slope*ln(4 pi c)/pi^2 = %.4f" % (c, sl, rat[-1], sl*np.log(4*np.pi*c)/np.pi**2))
check("Landau-Widom coefficient 1/pi^2: slope*ln(kappa c)/pi^2 brackets 1 for kappa=1 (below, rising) and kappa=4pi (above, falling)",
      all(rat[i] < rat[i+1] < 1 for i in range(len(rat)-1)) and all(1 < rat4[i+1] < rat4[i] for i in range(len(rat4)-1)))
print("\nTOTAL: %d PASS, %d FAIL" % (npass, nfail))
