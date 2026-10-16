# X1 final2 -- arithmetic of every explicit constant and elementary inequality used in the revised proofs of
# T2(a) (Fix 7(a)), (A4), T2'(a), T2'(b), T3(b), T3(e), P4(a),(b) and L8(i), as printed in X1-glauber_final2.md.
# Supersedes final2_scripts/superseded/new_constants_arith.py (an earlier draft of this revision, whose T3(e) and
# T2'(a) coefficients follow a different, unprinted bookkeeping).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
out = []
def log(s=''):
    print(s, flush=True); out.append(s)
ok = True
pi2 = np.pi**2
rng = np.random.default_rng(1014)

# ---------------- L8(i): integrated bounds for S-type functions ----------------
log("L8(i)  theta=pi/2: (i1) int_{R<=X}|S| <= 2*12 = 24 Mf l_X^2;  (i2) int_{R>X}|S| <= 2*(3200+86) = %d Mf (lam/X)(1+l_X);" % (2*(3200 + 86)))
log("       (i3) int_{R<=X} R|S| <= 4 lam * 24 Mf l_X^2 + int_{4lam}^X 6572 Mf (lam/r)(1+l_r) dr = 96 Mf lam l_X^2 + 6572 Mf lam (1+l_X) ln(X/4lam)")
log("       theta=pi/4 (constants x8, pi/4 norms): 192, %d, 768" % (8*2*(3200 + 86)))
ok &= (2*(3200 + 86) == 6572) and (8*6572 == 52576) and (8*96 == 768) and (8*24 == 192)
# check asinh(x) <= ln(1+2x) and ln(X/(4 lam)) <= ln(1 + 4X/mu) (mu <= lam)
xx = np.logspace(-6, 8, 4000)
ok &= np.all(np.arcsinh(xx) <= np.log(1 + 2*xx) + 1e-15)
# int |g| <= 4 Mf [ln(1+2x) + 2] <= 4 Mf (1 + ln(1+16x)) for x = lam/mu >= 1
xg = np.logspace(0, 8, 4000)
ok &= np.all(np.log(1 + 2*xg) + 2 <= 1 + np.log(1 + 16*xg))
log("       (i4) int|g| <= 4Mf asinh(lam/mu) + 8M <= 4Mf(1 + ln(1+16 lam/mu)) for lam >= mu: checked on lam/mu in [1, 1e8]")
# geometric integral: int_{4lam<R<=K} d^2kappa/(R <m>) = 8 int (dR/R) asinh(R/mu) <= 8 l_K ln(K/4lam)
def geo1(K, lam, mu, n=400):
    # Monte Carlo-free: exact 1-d formula vs direct 2-d quadrature on a polar-free square-ring parametrization
    Rg = np.exp(np.linspace(np.log(4*lam), np.log(K), n)); dR = np.gradient(Rg)
    oned = np.sum(8*np.arcsinh(Rg/mu)/Rg*dR)
    # direct: for each R, integrate over the boundary of the square of half-width R (length element) 1/(R<m>)
    two = 0.0
    for R, d in zip(Rg, dR):
        sg = np.linspace(-np.arcsinh(R/mu), np.arcsinh(R/mu), 4001); u = mu*np.sinh(sg)   # resolves the peak at u = 0
        m = np.minimum(np.abs(u), R)
        two += d*4*np.trapezoid(1/(R*np.sqrt(mu**2 + m**2)), u)
    return oned, two
o1, t1 = geo1(300.0, 1.0, 0.07)
bnd = 8*np.log(1 + 4*300/0.07)*np.log(300/4)
ok &= abs(o1 - t1) < 1e-3*o1 and t1 <= bnd
log(f"       geometric: int_(4lam<R<=K) d^2k/(R<min r>) = {t1:.3f} (1-d formula {o1:.3f}) <= 8 l_K ln(K/4lam) = {bnd:.3f}  [K=300, lam=1, mu=0.07]")
# strip integral: int_strip d^2k/(R <r_P>) <= 4 l_K ln(K/(3lam))
def geo2(K, lam, mu, n=1200):
    tot = 0.0
    for sgn in (1, -1):
        k2 = np.exp(np.linspace(np.log(3*lam), np.log(K), n)); dk2 = np.gradient(k2)
        for v, d in zip(k2, dk2):
            kP = np.linspace(-v/3, v/3, 801)
            k1 = kP - sgn*v
            R = np.maximum(np.abs(k1), v)
            mask = (np.abs(kP) < R/4) & (R > 4*lam) & (R <= K)
            tot += d*np.trapezoid(np.where(mask, 1/(R*np.sqrt(mu**2 + kP**2)), 0.0), kP)
    return tot
g2v = geo2(300.0, 1.0, 0.07); b2 = 4*np.log(1 + 4*300/0.07)*np.log(300/3)
ok &= g2v <= b2
log(f"       strip: int_(strip, 4lam<R<=K) d^2k/(R<r_P>) = {g2v:.3f} <= 4 l_K ln(K/3lam) = {b2:.3f}")

# ---------------- T2(a): constants (Fix 7(a)) ----------------
log("T2(a)  C_E = [24 m_A mf_B r + 825 mf_B + 1667 mf_A mf_B + 22.4 c_rho mf_B r]/pi^2 + (4/pi) m_A r;  C_N = [48 m_A mf_B r + 1650 mf_B + 3243 mf_A mf_B]/pi^2")
CN1 = (48 + 1650 + 3243)/pi2
log(f"       C_N (all m = 1, r = 1) = {CN1:.1f}")
def LB(eps, x): return np.log(1 + 4*x/np.sqrt(eps))
for xB in (1.0, 10.0):
    eg = np.logspace(-16, -2, 20001)
    e_CN = eg[np.where(CN1*np.sqrt(eg)*(1 + LB(eg, xB))**2 <= 0.5)[0].max()]
    dY = (48*np.sqrt(eg)*LB(eg, xB)**2 + 2*825*np.sqrt(eg)*(1 + LB(eg, xB)) + 2*1600*np.sqrt(eg)*(1 + LB(eg, xB))
          + 43*np.sqrt(eg)*(1 + LB(eg, xB)))/pi2
    e_dir = eg[np.where(dY <= 0.5)[0].max()]
    log(f"       lam_B/mu_B = {xB:g}: (v) guaranteed via C_N eps^1/2 (1+L_B)^2 for eps <= {e_CN:.1e}; via the explicit delta_Y for eps <= {e_dir:.1e}")
# monotonicity: f(eps) = eps^1/2 (1+L_B)^2 increasing on (0, 1/16]: derivative sign in t = eps^-1/2
t, x = sp.symbols('t x', positive=True)
f = (1 + sp.log(1 + 4*t*x))**2/t
df = sp.simplify(sp.diff(f, t)*t**2/(1 + sp.log(1 + 4*t*x)))
# df = 8xt/(1+4tx) - 1 - ln(1+4tx) < 2 - 1 - ln(17) < 0 for t >= 4, x >= 1
log(f"       d/dt [ (1+ln(1+4tx))^2/t ] * t^2/(1+ln(1+4tx)) = {df}  (< 2 - 1 - ln 17 < 0 for t >= 4, x >= 1)")
worst = 0
for xB in np.logspace(0, 8, 300):
    eg = np.logspace(-30, np.log10(1/16), 3000)
    fv = np.sqrt(eg)*(1 + LB(eg, xB))**2; lB = np.log(1 + 16*xB)
    worst = max(worst, fv.max()/((1 + lB)**2/4))
ok &= abs(worst - 1) < 1e-9
log(f"       sup_(eps<=1/16) eps^1/2 (1+L_B)^2 = (1+l_B)^2/4 (ratio {worst:.9f}); (1+l)^2/4 <= 3 + l^2 since 11 - 2l + 3l^2 > 0")
s1 = 2/np.e; s2 = 16/np.e**2; s3 = 216/np.e**3
Lg = np.linspace(np.log(16), 200, 400001)
for c in (1.0, 3.0, 10.0, 40.0):
    lhs = (np.exp(-Lg/2)*Lg*(c + Lg/2)**2).max(); rhs = s1*c**2 + s2*c + s3/4
    ok &= lhs <= rhs
log(f"       sup_(L>=ln16) e^(-L/2) L (c+L/2)^2 <= (2/e) c^2 + (16/e^2) c + (216/e^3)/4 = {s1:.4f} c^2 + {s2:.4f} c + {s3/4:.4f}  (checked c = 1..40)")
u = np.linspace(np.log(16), 60, 200001)
ok &= (np.exp(-u/2)*(1 + 2*u)**2).max() <= 11.2
log(f"       sup_(eps<=1/16) eps^1/2 (1+2L)^2 = {(np.exp(-u/2)*(1 + 2*u)**2).max():.4f} (<= 11.2)")
# E5 integral: int_K^inf (dk/k) min(1,(k*/k)^2)(1 + 2 ln(k/lam)) <= (U+1)^2/4 <= U^2, U = 1 + 2 ln(k*/lam) >= 1
U_ = sp.symbols('U', positive=True)
ok &= sp.simplify(sp.expand(U_**2 - (U_ + 1)**2/4) - (3*U_**2 - 2*U_ - 1)/4) == 0
log("       E5: int <= ((U^2-1)/4) + U/2 + 1/2 = (U+1)^2/4 <= U^2 for U >= 1  [3U^2 - 2U - 1 = (3U+1)(U-1) >= 0]")

# ---------------- (A4) ----------------
a1, a2, lam, mu, kap2 = sp.symbols('a1 a2 lambda mu kappa2', positive=True)
amin = sp.symbols('a_min', positive=True)
kstar = amin/(4*lam)
c_rho_core = 36*(a1*a2/amin**2)*(lam/mu)**2      # times (2nbar-1) mflat; a1 a2/amin^2 = a_max/a_min
ratio_at_kstar = sp.simplify(((sp.Rational(9, 16))*a1*a2/(kap2**3*mu**2))/(c_rho_core*(lam/amin)*(kstar/kap2)**2)).subs(kap2, kstar)
ok &= sp.simplify(ratio_at_kstar - 1) == 0
log(f"(A4)   for kappa2 >= kappa*: [(9/16) a1a2/(kappa2^3 mu^2)] / [c_rho (lam/a_min)(kappa*/kappa2)^2] = (kappa*/kappa2) * {sp.simplify(ratio_at_kstar)} <= 1"
    f"  with c_rho = 36(2nbar-1) mflat_A (a_max/a_min)(lam_A/mu_A)^2;  and c_rho >= 2(2nbar-1) mflat_A for kappa2 <= kappa*")

# ---------------- T2'(a) ----------------
log("T2'(a) eta := (lam_B/K_c)^1/2 = lam_B/K = K/K_c, zeta := lam_A K_c/a_min, l_K := ln(1+4K/mu_B), K := (lam_B K_c)^1/2")
# example chi: chihat(kappa) = 1/(1+i|kappa|/Kc); psi(k) = chi_+(k) chi_-(-k) = 1/(1+k/Kc)^2 ; derivative bounds
Kc = 1.0
k = 10**rng.uniform(-4, 4, 20000)*np.exp(1j*rng.uniform(0, np.pi/2, 20000))   # closed first quadrant
chi = 1/(1 + k/Kc); dchi = -1/Kc/(1 + k/Kc)**2
m1 = np.max(np.abs(dchi)*Kc/np.minimum(1, Kc**2/np.abs(k)**2))
m2 = np.max(np.where(np.abs(k) <= Kc, np.abs(chi - 1)/(np.abs(k)/Kc), 0))
m3 = np.max(np.where(np.abs(k) >= Kc, np.abs(chi)/(Kc/np.abs(k)), 0))
psi = chi**2
m4 = np.max(np.where(np.abs(k) <= Kc, np.abs(psi - 1)/(3*np.abs(k)/Kc), 0))
m5 = np.max(np.where(np.abs(k) >= Kc, np.abs(psi)/((Kc/np.abs(k))**2), 0))
ok &= max(m1, m2, m3, m4, m5) <= 1 + 1e-12
tt = sp.symbols('tt', positive=True)
ray = sp.integrate(sp.im(sp.expand_complex(1/(1 + sp.I*tt)**2))/tt, (tt, 0, sp.oo))
ok &= sp.simplify(ray + sp.pi/2) == 0
log(f"       example chi = 1/(1+k/K_c): |chi'| K_c/min(1,K_c^2/|k|^2) <= {m1:.4f}; |chi-1|/(|k|/K_c) <= {m2:.4f}; |chi|/(K_c/|k|) <= {m3:.4f};"
    f" |psi-1|/(3|k|/K_c) <= {m4:.4f}; |psi|/(K_c/|k|)^2 <= {m5:.4f};  int_0^inf dk/k Im psi(ik) = {ray}")
# Q4 integral: int_K^inf dk/k |rho-1||psi| <= 16 m_A zeta + 4 m_A zeta + (1+mf_A) 2 zeta^2
kk, KK, KC, kp, lA, am = sp.symbols('kk K K_c kprime lambda_A a_min', positive=True)
I1 = sp.integrate(4*lA*kk/am*4/kk, (kk, KK, KC)); I2 = sp.integrate(4*lA*kk/am*(KC/kk)**2/kk, (kk, KC, kp)); I3 = sp.integrate((KC/kk)**2/kk, (kk, kp, sp.oo))
I3s = sp.simplify(I3.subs(kp, am/(2*lA)))
log(f"       Q4 pieces: {sp.simplify(I1)} ; {sp.simplify(I2)} ; (1+mf_A) * {I3s}  (zeta = lam_A K_c/a_min)  =>  <= 20 m_A zeta + 2(1+mf_A) zeta^2")
ok &= sp.simplify(I3s - 2*(lA*KC/am)**2) == 0
# P5' integral: int_K^inf dk/k min(1,(Kc'/k)^2)(1+2u), u = ln(k/(3 lam_B)) <= (1+u_c')^2, Kc' = 3Kc/2
uu = sp.symbols('u', positive=True)
tail = sp.integrate(sp.exp(-2*(uu))*(1 + 2*(sp.Symbol('uc') + uu)), (uu, 0, sp.oo))
log(f"       P5' tail: int_0^inf e^(-2v)(1 + 2(u_c'+v)) dv = {sp.simplify(tail)};  head <= ((1+2u_c')^2 - (1+2u_K)^2)/4 <= ((1+2u_c')^2 - 1)/4"
    f" (u_K = ln(K/3lam_B) > 0);  sum <= (1+u_c')^2")
uc = sp.Symbol('uc')
ok &= sp.simplify(((1 + 2*uc)**2 - 1)/4 + sp.simplify(tail) - (1 + uc)**2) == 0
# coefficients
cE_eta = (825 + 8, 6400 + 172 + 64 + 32)
cE_eta2 = (2500.5 + 2500, 16)
log(f"       E^chi_tot: eta(1+l_K) coefficient [{cE_eta[0]} mf_B + {cE_eta[1]} mf_A mf_B]/pi^2 + 3/pi;  eta^2(1+l_K)^2 coefficient"
    f" [{cE_eta2[0]} mf_B + {cE_eta2[1]} mf_A mf_B]/pi^2;  + 48 m_A mf_B zeta eta l_K^2/pi^2 + (1/pi)[20 m_A zeta + 2(1+mf_A) zeta^2]"
    f" + 8 c_rho mf_B zeta eta^2 (1+2 ln(1/(4 zeta eta^2)))^2/pi^2")
ok &= cE_eta == (833, 6668)
log(f"       Q1 coefficient (3/8) * 6668 = {3*6668/8};  Q2 = [8 eta(1+l_K) + (36+2400+64) eta^2 l_K^2] mf_B/pi^2 = 2500")
ok &= (3*6668/8 == 2500.5) and (36 + 2400 + 64 == 2500)
log(f"       delta^chi_Y: eta(1+l_K) coefficient [1650 mf_B + {12800 + 172} mf_A mf_B]/pi^2;  eta^2(1+l_K)^2: 5001 mf_B/pi^2;  zeta eta l_K^2: 96 m_A mf_B/pi^2")
# numerical size for m's = 1 and logs: eta at which delta^chi_Y <= 1/2 (l_K ~ ln(4/eta) when lam_B ~ mu_B)
for etav in (1e-2, 1e-3, 1e-4, 1e-5, 1e-6):
    lK = np.log(1 + 4/etav)
    dYc = (etav*(1 + lK)*(1650 + 12972) + 5001*etav**2*(1 + lK)**2)/pi2
    log(f"         eta = {etav:.0e}: delta^chi_Y (m=1, zeta-term dropped, lam_B=mu_B) = {dYc:.3e}")

# ---------------- T3(b) ----------------
log("T3(b)  X := a_min/(2 lam_A) >= 4 lam_B  <=>  eps <= r^-1/2 /8;  l_X = ln(1 + 2a_min/(lam_A mu_B)) <= ln2 + L';  L >= L' ... L <= L'")
Lp = np.linspace(np.log(9), 80, 100001)
ok &= np.all(96*(np.log(2) + Lp)**2 + 6572*(1 + np.log(2) + Lp)*Lp <= 6668*(1 + Lp)**2)
ok &= np.all(1 + np.log(2) + Lp <= (1 + Lp)**2)
log(f"       96 l_X^2 + 6572(1+l_X) L <= 6668 (1+L')^2 and (1+l_X) <= (1+L')^2 for L' >= ln 9: checked;"
    f"  4*6668 = {4*6668}, 8*6668 = {8*6668}, 2*6572 = {2*6572}")
log(f"       |V| <= (mf_B/(8 pi^2))[24 l_B^2 + 6572/4 (1+l_B)] = (mf_B/(8pi^2))[24 l_B^2 + {6572/4:.0f}(1+l_B)]")

# ---------------- T3(e) ----------------
cu = (3 + np.sqrt(2))/2
log(f"T3(e)  c_U <= (3+sqrt2)/2 = {cu:.5f}, c_U^2 <= (11+6sqrt2)/4 = {cu**2:.4f}  [numerical sup c_U = 1.64853]")
Va = 768 + 52576
bb1 = 32*192; bb2 = 64*(768 + 52576); cc = 4*52576
log(f"       |V_K| <= ({Va}/(4pi^2)) mf'_B (K lam_B/a_min)(1+Lambda_K)^2     [768 Lambda^2 + 52576(1+Lambda)Lambda + 52576(1+Lambda) <= {Va}(1+Lambda)^2]")
log(f"       term(b) <= (c_U^2 m_A mf'_B/(4pi^2)) [{bb1} (lam_A/K) Lambda_K^2 + {bb2} r^1/2 eps (1+L')^2]")
log(f"       term(c): int_(R>R_A)|f_B| <= 52576 mf'_B (lam_B/R_A)(1+L') = {cc} mf'_B r^1/2 eps (1+L')")
C1 = 2*Va/(4*pi2); C2 = 2*bb1/(4*pi2); C3 = 2*bb2/(4*pi2); C4 = 2*4*cc/(4*pi2)
log(f"       |W12(K)-1/2| <= 2|V_K| + 2|dX - dY/2| <= {C1:.1f} mf'_B (K lam_B/a_min)(1+Lambda_K)^2 + {C2:.1f} c_U^2 m_A mf'_B (lam_A/K) Lambda_K^2"
    f" + c_U^2 mf'_B r^1/2 eps(1+L')^2 [{C3:.0f} m_A + {C4:.0f} mf_A,pi4]")
log(f"       with c_U^2 <= {cu**2:.4f}: {C2*cu**2:.0f} m_A mf'_B (lam_A/K) Lambda_K^2 + mf'_B r^1/2 eps (1+L')^2 [{C3*cu**2:.0f} m_A + {C4*cu**2:.0f} mf_A,pi4]")
log(f"       delta_N(K) <= 2 term(b) + (1/(4pi^2))(8 c_U^2 mf_A,pi4 + 1) {cc} mf'_B r^1/2 eps (1+L')")
ok &= (Va == 53344) and (bb1 == 6144) and (bb2 == 3414016) and (cc == 210304)

# ---------------- P4 ----------------
log("P4(a)  |W^in_D| <= (12/(4pi^2)) mf_B l_K^2 = (3/pi^2) mf_B l_K^2;  |W^out| <= (mf_A/(2pi))[L/2 + l_A + 1/2];"
    "  |R_P4| <= (E1+E3+E4+E5+E6+E7)/2 + 2 delta_Y |X_(12,21)|")
worst = 0
for _ in range(20000):
    a1v, a2v = 10**rng.uniform(-2, 2, size=2); A1, A2, Ap = -10**rng.uniform(-3, 1, size=3)
    kv = 10**rng.uniform(-4, 4)
    r2_ = abs(a1v*a2v*2*kv/((2j*kv*A1 - a1v)*(2j*kv*A2 - a1v)*(2j*kv*Ap - a2v)))
    worst = max(worst, r2_/(2*kv/a1v))
ok &= worst <= 1 + 1e-12
log(f"P4(b)  |rho_2(i kappa)| <= 2 kappa |ct_2|/(a_1|Jcal_A|): max ratio over 2e4 random points = {worst:.4f};  head <= 2 dm (lam_A K/a_min)")

# ---------------- L1 counterexample (Fix 7(c)) ----------------
z = np.array([1 - 0.01j, -0.99 - 0.01j])
w1 = z[0]/(z[0] + z[1]); w2 = z[1]/(z[0] + z[1])
log(f"L1     round-2 counterexample z = (1-0.01i, -0.99-0.01i), both final: race weights {w1:.2f}, {w2:.2f}; |w| = {abs(w1):.2f}, {abs(w2):.2f};"
    f" sum|w| = {abs(w1) + abs(w2):.1f}, max|w| = {max(abs(w1), abs(w2)):.1f}")
ok &= abs(abs(w1) + abs(w2) - 89.0) < 0.05 and abs(max(abs(w1), abs(w2)) - 44.7) < 0.05
log("ALL PASS" if ok else "SOME CHECK FAILED")
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'final2_logs', 'final2_constants.log'), 'w') as fh:
    fh.write('\n'.join(out) + '\n')
