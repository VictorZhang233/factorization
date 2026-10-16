"""R6 numerical checks of Example D.47 (one-loop off-shell triangle) of the reference document.
(1) k^- residue formula (D.28) [and analogous for C_S, C_H] against direct numerical k^- integration
    with finite i*eta;
(2) full region integrals (D.30),(D.31) at eps=0.3 by numerical (k^+, k_T) integration of the residue result;
(3) J(eps) (D.29);
(4) Table 5: exact d=4 integral vs L^2+pi^2/3, and the exact NLP coefficient; Usyukina-Davydychev closed form.
Conventions as in the reference: denominators carry -i0; measure mu^{2eps} int d^dk/(i pi^{d/2}).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp

mp.mp.dps = 30
ok = True
def check(name, a, b, tol):
    global ok
    good = abs(a - b) <= tol*max(1, abs(b))
    print(("PASS " if good else "FAIL ") + f"{name}: {mp.nstr(a, 15)} vs {mp.nstr(b, 15)}")
    ok = ok and good

P, Pp, m2 = mp.mpf('0.8'), mp.mpf('1.3'), mp.mpf('0.1')
Qt2 = 2*P*Pp

def dens(kp, km, kT2, eta=0):
    k2 = 2*kp*km - kT2
    I = 1j*eta
    Dg = -k2 - I
    D1 = m2 + 2*P*km - (m2/P)*kp - k2 - I
    D2 = m2 - (m2/Pp)*km + 2*Pp*kp - k2 - I
    e1 = m2 + 2*P*km - I; h1 = 2*P*km - I; t1 = 2*P*km - k2 - I
    e2 = m2 + 2*Pp*kp - I; h2 = 2*Pp*kp - I; t2 = 2*Pp*kp - k2 - I
    return Dg, D1, D2, e1, h1, t1, e2, h2, t2

def CR(name, kp, km, kT2, eta=0):
    Dg, D1, D2, e1, h1, t1, e2, h2, t2 = dens(kp, km, kT2, eta)
    if name == 'S':  return 1/(Dg*e1*e2)
    if name == 'C1': return (1/(Dg*h2))*(1/D1 - 1/e1)
    if name == 'C2': return (1/(Dg*h1))*(1/D2 - 1/e2)
    if name == 'H':  return Dg/(t1*h1*t2*h2)

def kminus_numeric(name, kp, kT2, eta=mp.mpf('1e-7')):
    f = lambda km: CR(name, kp, km, kT2, eta)
    # poles near: Dg: kT2/(2kp); e1,h1: ~ -m2/2P, 0; D1: ...; t1, t2 ...
    pts = sorted(set([mp.mpf(0), kT2/(2*kp), -m2/(2*P), (2*Pp*kp + kT2)/(2*kp),
                      -(m2 - (m2/P)*kp + kT2)/(2*(P - kp)), -kT2/(2*(P - kp))]))
    pts = [-mp.inf] + pts + [mp.inf]
    return mp.quad(f, pts, maxdegree=10)/(2*mp.pi)

def kminus_residue(name, kp, kT2):
    # closed forms after residues, as in (D.28) etc. (returned value = int dk^-/(2pi) C_R)
    A = kp*m2*(1 - kp/P) + P*kT2
    B = kp*m2 + P*kT2
    if name == 'C1':
        if 0 < kp < P:  return 0.5j*(1/(2*Pp*kp))*(1/A - 1/B)
        if kp > P:      return 0.5j*(1/(2*Pp*kp))*(-1/B)
        return 0
    if name == 'S':
        if kp > 0: return 0.5j/(B*(m2 + 2*Pp*kp))
        return 0
    if name == 'H':
        if 0 < kp < P:
            k0 = (2*Pp*kp + kT2)/(2*kp)
            Dg = -2*kp*k0 + kT2; h1 = 2*P*k0; t1 = 2*(P - kp)*k0 + kT2; h2 = 2*Pp*kp
            return (1j/(2*kp))*Dg/(t1*h1*h2)
        if kp > P:
            # h1 pole at k^-=0, closing above: +i * Res(1/h1)=1/(2P)
            Dg = kT2; t1 = kT2; t2 = 2*Pp*kp + kT2; h2 = 2*Pp*kp
            return 1j*(1/(2*P))*Dg/(t1*t2*h2)
        return 0

print("--- (1) k^- residues vs numerical k^- integration (eta=1e-7) ---")
for name in ['C1', 'S', 'H']:
    for (kp, kT2) in [(mp.mpf('0.3'), mp.mpf('0.05')), (mp.mpf('1.7'), mp.mpf('0.2')), (mp.mpf('-0.4'), mp.mpf('0.1'))]:
        num = kminus_numeric(name, kp, kT2)
        res = kminus_residue(name, kp, kT2)
        check(f"int dk-/2pi C_{name} at k+={kp}, kT2={kT2}", num, mp.mpc(res), 1e-4)

print("--- (2) region integrals at eps=0.3 (mu=1) ---")
eps = mp.mpf('0.3'); mu2 = mp.mpf(1)
def region_integral(name):
    # int = mu^{2eps} pi^{eps-1} int dk+ d^{2-2eps}kT (2/i) [int dk-/2pi C]
    # d^{2-2eps}kT = pi^{1-eps}/Gamma(1-eps) int dK K^{-eps}
    pref = mu2**eps*mp.pi**(eps - 1)*mp.pi**(1 - eps)/mp.gamma(1 - eps)
    def inner(kp):
        g = lambda K: K**(-eps)*(2/1j*kminus_residue(name, kp, K)).real
        return mp.quad(g, [0, m2, 1, mp.inf])
    return pref*mp.quad(inner, [0, P/4, P/2, P, 2*P, mp.inf])
A = mp.gamma(1+eps)*mp.gamma(1-eps)**2/(eps**2*mp.gamma(1-2*eps))
Bc = mp.gamma(1+eps)**2*mp.gamma(1-eps)/eps**2
val = {n: region_integral(n) for n in ['C1', 'S', 'H']}
check("int C_C1 = -(1/Qt2)(mu2/m2)^eps A", val['C1'], -(1/Qt2)*(mu2/m2)**eps*A, 1e-6)
check("int C_S  = (1/Qt2)(mu2 Qt2/m2^2)^eps B", val['S'], (1/Qt2)*(mu2*Qt2/m2**2)**eps*Bc, 1e-6)
check("int C_H  = (1/Qt2)(mu2/Qt2)^eps A", val['H'], (1/Qt2)*(mu2/Qt2)**eps*A, 1e-6)

print("--- (3) J(eps) ---")
for e in [mp.mpf('0.3'), mp.mpf('0.7')]:
    J1 = mp.quad(lambda v: v**(-1-e)*((1-v)**(-e) - 1), [0, 0.5, 1]) - 1/e
    check(f"J({e})", J1, mp.gamma(-e)*mp.gamma(1-e)/mp.gamma(1-2*e), 1e-12)

print("--- (4) Table 5 ---")
mp.mp.dps = 40
def exact(t):
    f = lambda u: mp.log(u*(1-u)/t)/(u*(1-u) - t)
    u0 = (1 - mp.sqrt(1 - 4*t))/2
    return 2*mp.quad(f, [0, u0/2, u0, (u0+mp.mpf(1)/2)/2, mp.mpf(1)/2])
def UD(t):  # Usyukina-Davydychev Phi^(1)(t,t)
    lam = mp.sqrt(1 - 4*t); rho = 2/(1 - 2*t + lam)
    return (4*mp.polylog(2, -rho*t) + mp.log(rho*t)**2 + mp.pi**2/3)/lam
table = {mp.mpf('1e-1'): '9.107781', mp.mpf('1e-2'): '24.770591', mp.mpf('1e-3'): '51.077533',
         mp.mpf('1e-4'): '88.133782', mp.mpf('1e-6'): '194.158529', mp.mpf('1e-8'): '342.611353',
         mp.mpf('1e-10'): '533.479679'}
for t, s in table.items():
    ex = exact(t); ud = UD(t)
    L = mp.log(1/t); lp = L**2 + mp.pi**2/3
    diff = ex - lp
    nlp = t*(2*L**2 - 4*L - 4 + 2*mp.pi**2/3)
    print(f"  t={mp.nstr(t,3)}: exact={mp.nstr(ex,12)}  UD={mp.nstr(ud,12)}  table={s}  LP={mp.nstr(lp,10)}"
          f"  diff={mp.nstr(diff,4)}  diff/(t L^2)={mp.nstr(diff/(t*L**2),4)}  (diff-NLP)/(t^2 L^2)={mp.nstr((diff-nlp)/(t**2*L**2),4)}")
    check(f"exact vs table t={mp.nstr(t,2)}", ex, mp.mpf(s), 2e-7)
    check(f"exact vs UD closed form t={mp.nstr(t,2)}", ex, ud, mp.mpf('1e-25'))
print("\nALL PASS" if ok else "\nSOME FAILED")
