import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp

mp.mp.dps = 30

# Hybrid correction in coordinate (Ioffe-time) space, per unit (3a/2):
#   g(lam) = ln(lam^2/lamS^2) * theta(|lam| - lamS)          (lam = z p^z, lamS = z_S p^z)
# Its FT in u = 1 - xi:  G(u) = int dlam/(2pi) e^{i u lam} g(lam)
# Pairing with a test function phi(u):  <G,phi> = int dlam/(2pi) g(lam) phihat(lam),
#   phihat(lam) = int du e^{i u lam} phi(u).
# Test functions: Gaussians phi(u) = exp(-(u-u0)^2/(2 s^2)) -> phihat = sqrt(2pi) s e^{i u0 lam} e^{-s^2 lam^2/2}

def exact_pairing(lamS, u0, s):
    # (1/2pi) * sqrt(2pi) s * int_{|lam|>lamS} ln(lam^2/lamS^2) cos(u0 lam) e^{-s^2 lam^2/2} dlam
    f = lambda l: 2*mp.log(l/lamS)*mp.cos(u0*l)*mp.exp(-s**2*l**2/2)
    I = mp.quad(f, [lamS, lamS+5, lamS+20, mp.inf])
    return (s/mp.sqrt(2*mp.pi))*2*I

def G(u, lamS):
    # pointwise FT for u != 0 (derived by integration by parts)
    return -1/abs(u) + 2*mp.si(u*lamS)/(mp.pi*u)

def phi(u, u0, s):
    return mp.exp(-(u-u0)**2/(2*s**2))

def plusR_pairing(lamS, u0, s):
    # [G]_+ on R: int du G(u) [phi(u) - phi(0)]
    p0 = phi(0, u0, s)
    f = lambda u: G(u, lamS)*(phi(u, u0, s) - p0)
    # integrate on (-inf,0) and (0,inf); oscillatory tail ~cos(u lamS)/u^2 -> use quadosc for tails
    L = 40
    pts = [mp.mpf(10)**(-12), mp.mpf('0.01'), mp.mpf('0.1'), 1, 3, 10, L]
    I = mp.quad(f, pts) + mp.quad(lambda u: f(-u), pts)
    # tails |u| > L: phi ~ 0 there (Gaussian), so integrand ~ -p0*G(u); integrate G analytically-asymptotically via quadosc
    # G is even; for |u|>L phi is negligible (Gaussian), so the tails give -2 p0 int_L^inf G(u) du
    tail = -2*p0*mp.quadosc(lambda u: G(u, lamS), [L, mp.inf], omega=lamS)
    return I + tail

def printed_pairing(lamS, u0, s):
    # -1/|u|_+ (Ji et al. 2020 definition: lim beta->0 [theta(|u|-beta)/|u| + 2 delta(u) ln beta]) + 2Si(u lamS)/(pi u)
    p0 = phi(0, u0, s)
    # <1/|u|_+, phi> = int_{|u|<1} (phi(u)-phi(0))/|u| du + int_{|u|>1} phi(u)/|u| du
    a = mp.quad(lambda u: (phi(u,u0,s)-p0)/u + (phi(-u,u0,s)-p0)/u, [0, 1])
    b = mp.quad(lambda u: (phi(u,u0,s)+phi(-u,u0,s))/u, [1, 10, 50, mp.inf])
    inv_abs_plus = a + b
    si_term = mp.quad(lambda u: 2*mp.si(u*lamS)/(mp.pi*u)*phi(u,u0,s) if u != 0 else 2*lamS/mp.pi*phi(0,u0,s), [-60, -10, -1, 0, 1, 10, 60])
    return -inv_abs_plus + si_term

print("check int_0^V Si(v)/v dv - (pi/2)(ln V + gamma_E):")
for V in [10, 100, 1000, 10000]:
    val = mp.quad(lambda v: mp.si(v)/v, mp.linspace(0, V, int(V)+1 if V <= 1000 else 2001))
    print(f"  V={V}: {mp.nstr(val - mp.pi/2*(mp.log(V)+mp.euler), 12)}")

print()
print("lamS, u0, s | exact | plus on R | printed | printed-exact | 2 ln(lamS e^gE) phi(0) | ratio")
for lamS in [mp.mpf('0.5'), mp.mpf(1), mp.mpf(2), mp.mpf('3.7')]:
    for (u0, s) in [(mp.mpf(0), mp.mpf('0.7')), (mp.mpf('0.4'), mp.mpf('0.5')), (mp.mpf('-0.8'), mp.mpf('1.3'))]:
        ex = exact_pairing(lamS, u0, s)
        pr = plusR_pairing(lamS, u0, s)
        pp = printed_pairing(lamS, u0, s)
        pred = 2*mp.log(lamS*mp.exp(mp.euler))*phi(0, u0, s)
        print(f"{mp.nstr(lamS,3)}, {mp.nstr(u0,3)}, {mp.nstr(s,3)} | {mp.nstr(ex,14)} | {mp.nstr(pr,14)} | {mp.nstr(pp,14)} | {mp.nstr(pp-ex,14)} | {mp.nstr(pred,14)} | {mp.nstr((pp-ex)/pred,14)}")

# numbers quoted in the claim
for a in [0.06, 0.3*4/3/(2*3.141592653589793)]:
    print("a=%.4f: 3a ln(e^gE) at lamS=1 =" % a, 3*a*float(mp.euler))
