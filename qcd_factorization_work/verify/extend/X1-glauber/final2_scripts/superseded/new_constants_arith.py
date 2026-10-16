# X1 final2 (Fix 4, Fix 7(a)) -- arithmetic of the explicit constants and elementary inequalities used in the
# revised proofs of T2(a) (constants, hypothesis (v)), T2'(a) (class-X regulator), T2'(b), T3(b), T3(e), P4(a),(b).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
out = []
def log(s=''):
    print(s, flush=True); out.append(s)
ok = True
pi2 = np.pi**2
# ---------------- integrated bounds for S-type functions (L8(g)) ----------------
# theta = pi/2: int_{R<=X}|S| <= 24 Mf l_X^2 ; int_{R>X}|S| <= 2(3200+86) Mf (lam/X)(1+l_X) ;
#   layer cake: int_{R<=X} R|S| <= 4 lam * 24 Mf l^2 + int_{4lam}^X 6572 Mf (lam/r)(1+l_r) dr <= 96 Mf lam l^2 + 6572 Mf lam (1+l) ln(X/4lam)
c_out = 2*(3200 + 86); ok &= (c_out == 6572)
log(f"(1) S-type, theta=pi/2: int_(R>X)|S| <= {c_out} Mf (lam/X)(1+l_X);  int_(R<=X) R|S| <= 96 Mf lam l^2 + {c_out} Mf lam (1+l) ln(X/4lam)")
# theta = pi/4 (constants x8, sqrt2-weighted norms)
c_out4 = 2*8*(3200 + 86); ok &= (c_out4 == 52576)
log(f"    theta=pi/4: int_(R<=X)|S| <= {2*8*12} Mf' l^2; int_(R>X)|S| <= {c_out4} Mf' (lam/X)(1+l); int_(R<=X) R|S| <= {4*2*8*12} Mf' lam l^2 + {c_out4} Mf' lam (1+l) ln(X/4lam)")
# check: ln(X/(4 lam)) <= ln(1 + 4X/mu) for mu <= lam
x = np.logspace(0, 8, 2000)
ok &= np.all(np.log(x/4) <= np.log(1 + 4*x))
# ---------------- T3(b) ----------------
DX_mA = 4*(96 + 6572); DX_rest = 2*6572
DY_mA = 8*(96 + 6572); DY_rest = 2*6572
log(f"(2) T3(b): |Delta X| <= (mf_B r^1/2/(4pi^2)) eps (1+L')^2 [{DX_mA} m_A + {DX_rest}(1+mf_A)];"
    f"  delta_b <= (mf_B r^1/2/(4pi^2)) eps (1+L')^2 [{DY_mA} m_A + {DY_rest}(1+2 mf_A)]")
ok &= (DX_mA == 26672 and DY_mA == 53344 and DX_rest == 13144)
log(f"    |V| <= (mf_B/(8 pi^2)) [24 l_B^2 + {6572//4 + (6572 % 4 > 0)}(1+l_B)]   (6572/4 = {6572/4})")
# ---------------- T3(e) ----------------
a_coef = 2*(4*2*8*12) + 2*c_out4    # (2K/a_min)*768 l^2 + ... : 1536 l^2 + 105152 (1+l) ln + 105152 (1+l)
log(f"(3) T3(e): term (a) <= Mf' (K lam_B/a_min)[{2*768} l_K^2 + {2*c_out4}(1+l_K) ln(X_K/4lam_B) + {2*c_out4}(1+l_K)] <= {2*768 + 2*c_out4} Mf' (K lam_B/a_min)(1+l_K)^2")
ok &= (2*768 + 2*c_out4 == 106688)
log(f"    term (b) <= 32 c_U^2 m_A Mf' [{2*8*12} (lam_A/K) l_K^2 + {2*c_out4} eps r^1/2 (1+L')(1+L)]  ->  {32*192} and {32*2*c_out4}")
ok &= (32*192 == 6144 and 32*2*c_out4 == 3364864)
log(f"    term (c) <= 4 c_U^2 mf_A,pi4 * {c_out4} Mf' * 4 eps r^1/2 (1+L') = {4*c_out4*4} c_U^2 mf_A,pi4 Mf' eps r^1/2 (1+L')")
ok &= (4*c_out4*4 == 841216)
log(f"    C_e1 = {2*768 + 2*c_out4}/(4pi^2) mf' = {(2*768 + 2*c_out4)/(4*pi2):.1f} mf';  C_e2 = 6144/(4pi^2) c_U^2 m_A mf' = {6144/(4*pi2):.2f} c_U^2 m_A mf';"
    f"  C_e3 = c_U^2 r^1/2 mf' ({3364864/(4*pi2):.0f} m_A + {841216/(4*pi2):.0f} mf_A,pi4)")
log(f"    delta_N <= (mf'/(4pi^2)) [6144 c_U^2 m_A (lam_A/K) l_K^2 + 3364864 c_U^2 m_A eps r^1/2 (1+L')^2 + {4*c_out4}(4 c_U^2 mf_A,pi4 + 1) eps r^1/2 (1+L')]")
cU2 = ((3 + np.sqrt(2))/2)**2
log(f"    c_U^2 <= ((3+sqrt2)/2)^2 = (11 + 6 sqrt2)/4 = {cU2:.4f}  (numerical c_U^2 = {1.64853**2:.4f})")
# ---------------- T2(a): constants, hypothesis (v), sup eps^1/2 (1+L_B)^2 ----------------
CN1 = (48 + 1650 + 3243)/pi2
log(f"(4) T2(a): C_N(all m = 1, r = 1) = (48 + 1650 + 3243)/pi^2 = {CN1:.1f}")
def LB(eps, x): return np.log(1 + 4*x/np.sqrt(eps))
def deltaY_direct(eps, x, r=1.0):   # 2E1 + 2E2 + 2E3 + E4 with all m = 1, K = lam_B eps^-1/2
    L = LB(eps, x)
    return (48*np.sqrt(r)*np.sqrt(eps)*L**2 + 2*825*np.sqrt(eps)*(1 + L) + 2*1600*np.sqrt(eps)*(1 + L) + 43*np.sqrt(eps)*(1 + L))/pi2
for xB in (1.0, 10.0):
    eg = np.logspace(-16, -2, 20001)
    viaCN = CN1*np.sqrt(eg)*(1 + LB(eg, xB))**2
    e_CN = eg[np.where(viaCN <= 0.5)[0].max()]
    e_dir = eg[np.where(deltaY_direct(eg, xB) <= 0.5)[0].max()]
    log(f"    lam_B/mu_B = {xB:g}: hypothesis (v) delta_Y <= 1/2 guaranteed via C_N eps^1/2 (1+L_B)^2 for eps <= {e_CN:.2e};"
        f" via the explicit delta_Y = 2E1+2E2+2E3+E4 for eps <= {e_dir:.2e}")
# sup over eps <= 1/16 of eps^1/2 (1+L_B)^2 equals (1+l_B)^2/4 (attained at eps = 1/16), <= 3 + l_B^2
worst = 0
for xB in np.logspace(0, 8, 400):
    eg = np.logspace(-30, np.log10(1/16), 4000)
    f = np.sqrt(eg)*(1 + LB(eg, xB))**2
    lB = np.log(1 + 16*xB)
    worst = max(worst, f.max()/((1 + lB)**2/4))
    ok &= f.max() <= 3 + lB**2
log(f"    sup_(eps<=1/16) eps^1/2 (1+L_B)^2 / [(1+l_B)^2/4] = {worst:.6f} (= 1: attained at eps = 1/16); (1+l_B)^2/4 <= 3 + l_B^2")
ok &= abs(worst - 1) < 1e-6
u = np.linspace(np.log(16), 60, 200001); f = np.exp(-u/2)*(1 + 2*u)**2
log(f"    sup_(eps<=1/16) eps^1/2 (1+2L)^2 = {f.max():.4f} at L = {u[np.argmax(f)]:.3f} (<= 11.2)")
ok &= f.max() <= 11.2
# ---------------- T2'(a): elementary integrals ----------------
# substitute kappa = K_c y, Lc := ln(K_c/c) >= 0
y, Lc = sp.symbols('y L_c', positive=True)
I3 = sp.simplify(sp.integrate(y**-4*(1 + 2*(sp.log(y) + Lc)), (y, 1, sp.oo)))
I2 = sp.simplify(sp.integrate(y**-3*(1 + 2*(sp.log(y) + Lc)), (y, 1, sp.oo)))
log(f"(5) T2'(a): int_Kc^inf (Kc/k)^3 (1+2ln(k/c)) dk/k = {I3}  [= (1/3)(1+2L_c) + 2/9];"
    f"   int_Kc^inf (Kc/k)^2 (1+2ln(k/c)) dk/k = {I2}  [= (1/2)(1+2L_c) + 1/2],  L_c = ln(K_c/c)")
ok &= sp.simplify(I3 - (sp.Rational(1, 3)*(1 + 2*Lc) + sp.Rational(2, 9))) == 0
ok &= sp.simplify(I2 - (sp.Rational(1, 2)*(1 + 2*Lc) + sp.Rational(1, 2))) == 0
t = sp.symbols('t', positive=True)
psi_int = sp.integrate(sp.im(1/(1 + sp.I*t)**2).simplify()/t, (t, 0, sp.oo))
log(f"    example chi = 1/(1+k/K_c) (k>0), 1/(1-k/K_c) (k<0): psi(i kappa) = 1/(1+i kappa/K_c)^2,"
    f" int_0^inf (dkappa/kappa) Im psi = {sp.simplify(psi_int)}  (= -pi/2, ray identity without poles)")
ok &= sp.simplify(psi_int + sp.pi/2) == 0
# Q1 coefficient, Q2 coefficients
log(f"    Q_1 <= (3/(8pi^2)) mf_B (lam_B/K_c) 6668 (1+l_K)^2 = ({3*6668/8}/pi^2) mf_B eta^2 (1+l_K)^2;   Q_2 <= (mf_B/(4pi^2))[(144+9600+192) eta^2 l_K^2 + 32 eta (2+l_K)]"
    f" = (mf_B/(4pi^2))[{144 + 9600 + 192} eta^2 l_K^2 + 32 eta (2+l_K)]")
ok &= (144 + 9600 + 192 == 9936)
# sup of eta (1+Lambda)^2 with eta = exp(-Lambda/2), Lambda >= ln 16
Lam = np.linspace(np.log(16), 80, 400001); eta = np.exp(-Lam/2)
s1 = (eta*(1 + Lam)**2).max(); s2 = (eta*Lam**2).max()
log(f"    sup_(eta<=1/4) eta (1+Lambda_c)^2 = {s1:.4f};  sup eta Lambda_c^2 = {s2:.4f}   (Lambda_c = 2 ln(1/eta))")
ok &= s1 <= 3.6
# delta_Y^chi and E^chi_tot leading coefficients (eta (1+l_K) terms), for the record
a1 = 825 + 8*2 ; a1b = 6400 + 172 + 16 + 64
log(f"    E^chi_tot: eta(1+l_K) coefficient <= [(825+16) mf_B + ({a1b}) mf_A mf_B]/pi^2 + 3/pi;"
    f"  delta_Y^chi: eta(1+l_K) coefficient <= [1650 mf_B + {12800 + 172} mf_A mf_B]/pi^2")
ok &= (a1b == 6652)
# ---------------- P4 ----------------
log("(6) P4(a): |X^in_D| <= (12/(4pi^2)) mf_B l_K^2 = (3/pi^2) mf_B l_K^2;  |W^out| <= (mf_A/(2pi))[L/2 + l_A + 1/2];"
    "  |R_P4| <= (E1+E3+E4+E5+E6+E7)/2 + 2 delta_Y |X_(12,21)|")
log("    P4(b): |int_0^K rho_2(i kappa) dkappa/kappa| <= 2 K |ct_2|/(a_1 |Jcal_A|) <= 2 dm (lam_A K/a_min),  dm = |ct_2|/(lam_A |Jcal_A|)")
# numerical check of |rho2(i kappa)| <= 2 kappa |ct2|/(a1 |J|) on random parameters
rng = np.random.default_rng(99); worst = 0
for _ in range(20000):
    a1_, a2_ = 10**rng.uniform(-2, 2, size=2); A1, A2, Ap = -10**rng.uniform(-3, 1, size=3)
    kap = 10**rng.uniform(-4, 4)
    r2 = abs(a1_*a2_*2*kap/((2j*kap*A1 - a1_)*(2j*kap*A2 - a1_)*(2j*kap*Ap - a2_)))
    worst = max(worst, r2/(2*kap/a1_))
log(f"    max |rho_2(i kappa)| / (2 kappa |ct_2|/(a_1|Jcal_A|)) over 2e4 random points = {worst:.4f} (<= 1)")
ok &= worst <= 1 + 1e-12
log("ALL PASS" if ok else "SOME CHECK FAILED")
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'final2_logs', 'new_constants_arith.log'), 'w') as f:
    f.write('\n'.join(out) + '\n')
