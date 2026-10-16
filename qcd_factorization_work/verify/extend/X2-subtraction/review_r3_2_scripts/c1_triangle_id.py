# Independent re-derivation (reviewer r3_2): triangle (M1) Collins terms and Gamma.
# Fibered side: own residue derivation (reviewer), kappa-integral done by quadrature (no K2 formula) and by K2.
# Covariant side: own Feynman parametrisation of Gamma (standard simplex), closed forms for C_R.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 30

def setup(P, Pp, m2, eps):
    Qt2 = 2*P*Pp
    return dict(P=mp.mpf(P), Pp=mp.mpf(Pp), m2=mp.mpf(m2), eps=mp.mpf(eps), Qt2=mp.mpf(Qt2))

# ---- fibered densities (reviewer's own derivation, normalisation (1/Gamma(1-eps)) int dx dkappa kappa^-eps rho) ----
def rho_Gamma(s, x, k):
    P, Pp, m2, Qt2 = s['P'], s['Pp'], s['m2'], s['Qt2']
    if 0 < x < P:
        u = x/P
        A = P*k + x*m2*(1-u)
        e2 = m2 + 2*Pp*x
        D2 = e2*(1 + m2/Qt2 + k/(Qt2*(1-u))) + k
        return 1/(A*D2)
    a = m2/Pp
    if -a/2 < x < 0:
        w = 2*x + a
        Dg = (a*k + (a-w)*Pp*w)/w
        km = Pp + k/w
        D1 = 2*(P-x)*(m2/(2*P) + km) + k
        return 2/(w*Dg*D1)
    return mp.mpf(0)

def rho_CS(s, x, k):
    P, Pp, m2 = s['P'], s['Pp'], s['m2']
    if x > 0:
        return 1/((x*m2 + P*k)*(m2 + 2*Pp*x))
    return mp.mpf(0)

def rho_CC1(s, x, k):
    P, Pp, m2 = s['P'], s['Pp'], s['m2']
    if x <= 0: return mp.mpf(0)
    u = x/P; h2 = 2*Pp*x
    A = P*k + x*m2*(1-u); B = x*m2 + P*k
    if x < P:
        return 1/(A*h2) - 1/(B*h2)
    return -1/(B*h2)

def rho_CC2(s, x, k):
    P, Pp, m2 = s['P'], s['Pp'], s['m2']
    a = m2/Pp
    if x > 0:
        e2 = m2 + 2*Pp*x
        return -1/(P*e2*(e2 + k))
    if -a/2 < x < 0:
        w = 2*x + a
        return w/(P*((a-w)*Pp*w + a*k)*(Pp*w + k))
    return mp.mpf(0)

def rho_CH(s, x, k):
    P, Pp = s['P'], s['Pp']
    if x <= 0: return mp.mpf(0)
    h2 = 2*Pp*x
    if x < P:
        return -x/(P*(h2 + k)*(h2*(P-x) + P*k))
    return 1/(P*(h2 + k)*h2)

def fib(s, rho, pieces):
    eps = s['eps']
    f = lambda x: mp.quad(lambda k: k**(-eps)*rho(s, x, k), [0, mp.mpf('1e-6'), 1, mp.inf])
    tot = mp.mpf(0)
    for (lo, hi) in pieces:
        tot += mp.quad(f, [lo, hi] if hi != mp.inf else [lo, lo + 1, mp.inf])
    return tot/mp.gamma(1-eps)

# closed forms (report's Prop 3.1')
def closed(s):
    e, m2, Qt2 = s['eps'], s['m2'], s['Qt2']
    G = mp.gamma
    CS = G(e)**2*G(1-e)*(Qt2/m2**2)**e/Qt2
    CC = G(e)*G(-e)*G(1-e)/G(1-2*e)*m2**(-e)/Qt2
    CH = G(1+e)*G(1-e)**2/(e**2*G(1-2*e))*Qt2**(-e)/Qt2
    return CS, CC, CH

def cov_Gamma(s):
    # Gamma(1+eps) * int_simplex Delta^{-1-eps}, Delta = m2*ag*(a1+a2) + a1*a2*Q2
    e, m2, Qt2 = s['eps'], s['m2'], s['Qt2']
    Q2 = (Qt2 + m2)**2/Qt2
    f = lambda a1: mp.quad(lambda a2: (m2*(1-a1-a2)*(a1+a2) + a1*a2*Q2)**(-1-e), [0, (1-a1)/2, 1-a1])
    return mp.gamma(1+e)*mp.quad(f, [0, mp.mpf('0.5'), 1])

if __name__ == '__main__':
    for (P, Pp, m2, eps) in [(0.8, 1.3, 0.1, 0.3), (1/mp.sqrt(2), 1/mp.sqrt(2), 0.01, 0.2)]:
        s = setup(P, Pp, m2, eps)
        a = s['m2']/s['Pp']
        CS, CC, CH = closed(s)
        fCS = fib(s, rho_CS, [(0, s['P']), (s['P'], mp.inf)])
        fC1 = fib(s, rho_CC1, [(0, s['P']), (s['P'], mp.inf)])
        fC2 = fib(s, rho_CC2, [(-a/2, 0), (0, mp.inf)])
        fCH = fib(s, rho_CH, [(0, s['P']), (s['P'], mp.inf)])
        print(f"P={P}, P'={Pp}, m2={m2}, eps={eps}")
        for nm, fv, cv in [('C_S', fCS, CS), ('C_C1', fC1, CC), ('C_C2', fC2, CC), ('C_H', fCH, CH)]:
            print(f"   {nm}: fibered(2D quad) = {mp.nstr(fv, 15)}   closed form = {mp.nstr(cv, 15)}   rel = {mp.nstr(abs(fv/cv-1), 3)}")
        fG = fib(s, rho_Gamma, [(-a/2, 0), (0, s['P'])])
        cG = cov_Gamma(s)
        print(f"   Gamma: fibered(2D quad) = {mp.nstr(fG, 15)}   covariant(simplex) = {mp.nstr(cG, 15)}   rel = {mp.nstr(abs(fG/cG-1), 3)}")
    # sum of Collins terms as eps -> 0 (units Qt=1): compare with L^2 + pi^2/3
    for m2 in [mp.mpf('0.01'), mp.mpf('1e-4')]:
        L = mp.log(1/m2)
        vals = []
        for e in [mp.mpf('1e-6'), mp.mpf('1e-8')]:
            s = setup(1/mp.sqrt(2), 1/mp.sqrt(2), m2, e)
            CS, CC, CH = closed(s)
            vals.append(CS + 2*CC + CH)
        print(f"m2={m2}: sum C_R at eps=1e-6, 1e-8: {mp.nstr(vals[0], 12)}, {mp.nstr(vals[1], 12)};  L^2+pi^2/3 = {mp.nstr(L**2 + mp.pi**2/3, 12)}")
