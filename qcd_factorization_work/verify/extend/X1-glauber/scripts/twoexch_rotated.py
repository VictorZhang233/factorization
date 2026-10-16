# Cross-check of twoexch_exact.py by an independent representation: after the exact k^- residues,
# rotate the k^+ contour (both components) by e^{i theta}, theta = pi/2 (complex boost).  Allowed when
# no B final-state denominator can vanish (all B final energies negative) -- see REPORT, Lemma L5.
# On the rotated contour the integrand is smooth; integrate in 2D (polar coordinates per quadrant).
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
mp.mp.dps = 25
I = mp.mpc(0, 1)
from twoexch_exact import jet_params

def FA(k1, k2, pa, a1, a2, col, q1, q2):
    """analytic continuation of the quadrant formula of quadrant (q1,q2) (signs of the real k^+),
       evaluated at complex k1,k2 (the rotated points)."""
    d0, d10, d20, beta, al0, al1, al2 = (pa[k] for k in ('d0','d10','d20','beta','al0','al1','al2'))
    i3 = I**3
    z1 = a1/(2*k1); z2 = a2/(2*k2); r1 = 1/(2*k1); r2 = 1/(2*k2)
    if (q1, q2) == (1, 1):
        J = i3/(d0*(al0 - z1 - z2)*((al1 - z2) if col == '12' else (al2 - z1)))
        return -r1*r2*J
    if (q1, q2) == (-1, -1):
        J = i3/(d0*((d10 + z1) if col == '12' else (d20 + z2))*(z1 + z2 - beta))
        return -r1*r2*J
    if (q1, q2) == (-1, 1):
        if col == '21': return mp.mpc(0)
        return r1*r2*i3/(d0*(d10 + z1)*(al1 - z2))
    if (q1, q2) == (1, -1):
        if col == '12': return mp.mpc(0)
        return r1*r2*i3/(d0*(d20 + z2)*(al2 - z1))

def JB(p1, p2, pb, col):
    d0, beta, al0, al1, al2 = (pb[k] for k in ('d0','beta','al0','al1','al2'))
    den3 = (al1 - p2) if col == '12' else (al2 - p1)
    return I**3/((p1 + p2 - beta)*(al0 - p1 - p2)*den3)

def Irot(pa, pb, a1, a2, cA, cB, theta=mp.pi/2):
    ph = mp.e**(I*theta)
    tot = mp.mpc(0)
    for q1, q2 in itertools.product((1, -1), repeat=2):
        # polar coords in the quadrant: kappa1 = q1 r cos(phi), kappa2 = q2 r sin(phi), phi in (0, pi/2)
        def f(t, phi):
            r = mp.e**t
            x1 = q1*r*mp.cos(phi); x2 = q2*r*mp.sin(phi)
            k1, k2 = ph*x1, ph*x2
            return FA(k1, k2, pa, a1, a2, cA, q1, q2)*JB(-k1, -k2, pb, cB)*r*r   # r dr = r^2 dt
        val = mp.quad(lambda phi: mp.quad(lambda t: f(t, phi), [-40, -10, -6, -4, -2, 0, 2, 4, 10]), [0, mp.pi/8, mp.pi/4, 3*mp.pi/8, mp.pi/2])
        tot += val
    return tot*ph**2/(2*mp.pi)**2

if __name__ == '__main__':
    lam = mp.mpf(sys.argv[1]) if len(sys.argv) > 1 else mp.mpf('0.01')
    sc = lambda v: (lam*mp.mpf(v[0]), lam*mp.mpf(v[1]))
    k1T = sc(('0.8', '0.1')); k2T = sc(('-0.3', '0.9'))
    k1Tm = (-k1T[0], -k1T[1]); k2Tm = (-k2T[0], -k2T[1])
    pa = jet_params(mp.mpf('0.9')*lam, mp.mpf('0.5')*lam, mp.mpf('0.7')*lam, mp.mpf('0.4'), sc(('0.3', '0.2')), k1T, k2T)
    pb = jet_params(mp.mpf('0.8')*lam, mp.mpf('0.6')*lam, mp.mpf('0.5')*lam, mp.mpf('0.55'), sc(('-0.25', '0.4')), k1Tm, k2Tm)
    a1 = k1T[0]**2 + k1T[1]**2; a2 = k2T[0]**2 + k2T[1]**2
    res = {}
    for cA, cB in itertools.product(('12','21'), repeat=2):
        res[(cA, cB)] = Irot(pa, pb, a1, a2, cA, cB)
    N = sum(res.values()); N0 = (I/pa['d0'])*(I/pb['d0'])/(a1*a2)
    print(f"lam={mp.nstr(lam,3)} base set, ROTATED contour: N/N0 = {mp.nstr(N/N0,10)}")
    for k, v in res.items(): print(f"   W{k} = {mp.nstr(v/N, 10)}")
    print(f"   p_opp = {mp.nstr((res[('12','21')]+res[('21','12')])/N, 10)}", flush=True)
