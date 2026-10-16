# Round-3 reviewer 2 -- independent test of Lemma L8 (two-insertion jets on the rotated contour, theta = pi/2).
# Jet model (independent implementation): gap functions depend only on the SET of operations already performed
# (scalar-model structure), single-state term with coefficient 1 in every gap  =>  (J), (Sp), (Sp') hold;
# every term carries the common phase i  => (R); all final energies negative => (NF).
import sys, os, itertools, math
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
rng = np.random.default_rng(7)

def make_gap(kind, lam, mu, pmulti):
    # list of (coef, [A_j]) ; kind 'I': factors i/(A+K) ; 'F': factors i/(A-K) ; all A in [-lam,-mu]
    terms = [(1.0 + 0j, [-rng.uniform(mu, lam)])]
    for n in (2, 3):
        if rng.uniform() < pmulti:
            rho = rng.uniform(-1, 1)
            coef = rho * lam**(n - 1) * (1j)**(1 - n)      # keeps the common phase i  (R)
            terms.append((coef, list(-rng.uniform(mu, lam, n))))
    return (kind, terms)

def gap_val(gap, K):
    kind, terms = gap
    out = 0
    for coef, As in terms:
        t = coef
        for A in As:
            t = t * (1j / (A + K) if kind == 'I' else 1j / (A - K))
        out = out + t
    return out

def gap_norms(gap, lam, mu):
    kind, terms = gap
    M = sum(abs(c) * lam**(-(len(As) - 1)) for c, As in terms)
    Mf = sum(abs(c) * mu**(-(len(As) - 1)) for c, As in terms)
    return M, Mf

def make_jet(lam, mu, pmulti):
    G = {S: make_gap('I', lam, mu, pmulti) for S in ('1', '2', '12')}
    G.update({S: make_gap('F', lam, mu, pmulti) for S in ('V', '1V', '2V')})
    allA = [A for g in G.values() for c, As in g[1] for A in As]
    lam_e, mu_e = max(abs(a) for a in allA), min(abs(a) for a in allA)
    secs = {'BB12': ('1', '12'), 'BF12': ('1', '1V'), 'FF12': ('V', '1V'),
            'BB21': ('2', '12'), 'BF21': ('2', '2V'), 'FF21': ('V', '2V')}
    M = max(np.prod([gap_norms(G[s], lam_e, mu_e)[0] for s in v]) for v in secs.values())
    Mf = max(np.prod([gap_norms(G[s], lam_e, mu_e)[1] for s in v]) for v in secs.values())
    return G, lam_e, mu_e, M, Mf

def f_pi(G, k1, k2):
    # rotated contour p_e = -i kappa_e ; gap momenta K = -i y
    p1, p2 = -1j * k1, -1j * k2; P = p1 + p2
    g = lambda S, K: gap_val(G[S], K)
    f12 = g('1', p1) * g('12', P) + g('1', p1) * g('1V', p2) + g('V', P) * g('1V', p2)
    f21 = g('2', p2) * g('12', P) + g('2', p2) * g('2V', p1) + g('V', P) * g('2V', p1)
    return f12, f21

def gfun(G, P):   # g(P) of L8(d) in this model (Jcal = 1)
    return gap_val(G['12'], P) + gap_val(G['V'], P)

def br(y, mu): return np.sqrt(mu**2 + y**2)

worst = {k: 0.0 for k in ('b', 'c_generic384M', 'c_band9', 'c_400', 'd16', 'e_pt')}
for jet in range(200):
    lam = 1.0; mu = 10**rng.uniform(-3, math.log10(0.6))
    G, lam_e, mu_e, M, Mf = make_jet(lam, mu, pmulti=0.6)
    for trial in range(300):
        R = lam_e * 10**rng.uniform(math.log10(4), 4)
        reg = rng.integers(0, 3)
        if reg == 0:   # generic
            ang = rng.uniform(0, 2*np.pi); k1, k2 = R*np.cos(ang), R*np.sin(ang)
        elif reg == 1:  # axis band r1 < R/4  (r2 = R)
            k2 = R*rng.choice([-1, 1]); k1 = rng.uniform(-R/4, R/4) * 10**rng.uniform(-6, 0)
        else:           # strip r_P < R/4
            k2 = R*rng.choice([-1, 1]) * rng.uniform(0.8, 1.0); kP = rng.uniform(-1, 1) * 10**rng.uniform(-6, 0) * abs(k2)/4.2
            k1 = kP - k2
        f12, f21 = f_pi(G, k1, k2)
        r1, r2, rP = abs(k1), abs(k2), abs(k1 + k2); RR = max(r1, r2)
        # (b) every sector bound |J^(sigma)| <= Mflat/(<y1><y2>)
        p1, p2 = -1j*k1, -1j*k2; P = p1 + p2
        for (Sa, Ka, ya), (Sb, Kb, yb) in [(( '1', p1, k1), ('12', P, k1+k2)), (('1', p1, k1), ('1V', p2, k2)), (('V', P, k1+k2), ('1V', p2, k2)),
                                            (( '2', p2, k2), ('12', P, k1+k2)), (('2', p2, k2), ('2V', p1, k1)), (('V', P, k1+k2), ('2V', p1, k1))]:
            val = abs(gap_val(G[Sa], Ka) * gap_val(G[Sb], Kb))
            worst['b'] = max(worst['b'], val / (Mf / (br(ya, mu_e) * br(yb, mu_e))))
        if RR >= 4*lam_e and rP >= RR/4:
            for f in (f12, f21):
                worst['c_400'] = max(worst['c_400'], abs(f) / (400*Mf*lam_e/(RR**2*br(min(r1, r2), mu_e))))
                if min(r1, r2) >= RR/4:
                    worst['c_generic384M'] = max(worst['c_generic384M'], abs(f) / (384*M*lam_e/RR**3))
                else:
                    worst['c_band9'] = max(worst['c_band9'], abs(f) / (9*Mf*lam_e/(RR**2*br(min(r1, r2), mu_e))))
        if RR >= 4*lam_e and rP < RR/4:
            gg = gfun(G, -1j*(k1 + k2))
            E12 = f12 - gg/k2; E21 = f21 + gg/k2
            bound = 16*Mf*lam_e/(RR**2*br(rP, mu_e))
            worst['d16'] = max(worst['d16'], abs(E12)/bound, abs(E21)/bound)
        U = (k1 + k2)
        gg = abs(gfun(G, -1j*U))
        worst['e_pt'] = max(worst['e_pt'], gg / min(2*Mf/br(U, mu_e), 4*M*lam_e/U**2 if U != 0 else np.inf))
print('L8 pointwise bounds, max(lhs/bound) over 200 jets x 300 points (PASS if <= 1):')
for k, v in worst.items(): print(f'  {k:16s} {v:.4g}', 'PASS' if v <= 1 else 'FAIL')

# (e) integral of g and (f) integral of S, for 5 jets
def int_g(G, mu, lam):
    t = np.linspace(-40, 40, 400001); U = mu*np.sinh(t); dU = mu*np.cosh(t)
    vals = (gap_val(G['12'], -1j*U) + gap_val(G['V'], -1j*U)) * dU
    return np.trapezoid(vals, t) / (2*np.pi)

def int_S(G, mu, lam, smin=None, smax=None, nphi_base=1500, nclus=500):
    # polar coordinates, log-radius; angular grid clustered at the axes and at the anti-diagonals (strip)
    s = np.linspace(math.log(1e-4*mu), math.log(1e7*lam), 1800)
    tot = 0.0
    rows = []
    for si in s:
        R = math.exp(si)
        base = np.linspace(0, 2*np.pi, nphi_base, endpoint=False)
        pts = [base]
        w0 = min(1.0, mu/R)
        for a in (0, np.pi/2, np.pi, 3*np.pi/2, 3*np.pi/4, 7*np.pi/4):
            d = np.geomspace(1e-3*w0, 0.3, nclus)
            pts += [a + d, a - d, np.array([a])]
        phi = np.unique(np.mod(np.concatenate(pts), 2*np.pi))
        phi = np.concatenate([phi, [phi[0] + 2*np.pi]])
        k1, k2 = R*np.cos(phi), R*np.sin(phi)
        f12, f21 = f_pi(G, k1, k2)
        val = np.trapezoid((f12 + f21), phi) * R**2
        rows.append(val)
    return np.trapezoid(np.array(rows), s) / (2*np.pi)**2

print('\nIntegrals (expect int g dU/2pi = -i Jcal = -i ; int S d^2kappa/(2pi)^2 = -Jcal = -1):')
for jet in range(5):
    lam = 1.0; mu = [0.5, 0.2, 0.05, 0.3, 0.1][jet]
    G, lam_e, mu_e, M, Mf = make_jet(lam, mu, pmulti=0.6)
    ig = int_g(G, mu_e, lam_e)
    iS = int_S(G, mu_e, lam_e)
    print(f'  jet {jet}: mu={mu_e:.3g} lam={lam_e:.3g}  int g/(2pi) = {ig:.6f}   int S/(2pi)^2 = {iS:.5f}')
