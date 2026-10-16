"""R6: remainder of Example D.47 directly in d=4.
After the k^- residue integration, int d^4k/(i pi^2) f = int dk^+ int_0^inf dK rho_f(k^+,K), K=k_T^2,
rho_f = (2/i) int dk^-/(2pi) f.  The remainder r = Gamma - sum_R C_R is integrable in d=4, so
int dk^+ dK [rho_Gamma - sum_R rho_R] must equal  I_exact - (1/Qt^2)[ln^2(Qt^2/m^2)+pi^2/3].
Also prints pointwise sizes of the remainder density in the soft / collinear / hard regions.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 20

def setup(P, Pp, m2):
    def dens(kp, km, K):
        k2 = 2*kp*km - K
        Dg = -k2
        D1 = m2 + 2*P*km - (m2/P)*kp - k2
        D2 = m2 - (m2/Pp)*km + 2*Pp*kp - k2
        e1 = m2 + 2*P*km; h1 = 2*P*km; t1 = 2*P*km - k2
        e2 = m2 + 2*Pp*kp; h2 = 2*Pp*kp; t2 = 2*Pp*kp - k2
        return Dg, D1, D2, e1, h1, t1, e2, h2, t2
    a2 = m2/Pp
    def rho_G(kp, K):
        if 0 < kp < P:
            k1 = -(m2*(1 - kp/P) + K)/(2*(P - kp))
            Dg, D1, D2, *_ = dens(kp, k1, K)
            return (1/(P - kp))/(Dg*D2)
        if -m2/(2*Pp) < kp <= 0:
            k2_ = (m2 + 2*Pp*kp + K)/(a2 + 2*kp)
            Dg, D1, D2, *_ = dens(kp, k2_, K)
            return 2/(a2 + 2*kp)/(Dg*D1)
        return mp.mpf(0)
    def rho_S(kp, K):
        if kp > 0: return 1/((kp*m2 + P*K)*(m2 + 2*Pp*kp))
        return mp.mpf(0)
    def rho_C1(kp, K):
        A = kp*m2*(1 - kp/P) + P*K; B = kp*m2 + P*K
        if 0 < kp < P: return (1/(2*Pp*kp))*(1/A - 1/B)
        if kp >= P: return -(1/(2*Pp*kp))/B
        return mp.mpf(0)
    def rho_C2(kp, K):
        if kp > 0: return -(1/P)/((m2 + 2*Pp*kp + K)*(m2 + 2*Pp*kp))
        if -m2/(2*Pp) < kp <= 0:
            k2_ = (m2 + 2*Pp*kp + K)/(a2 + 2*kp)
            Dg, D1, D2, e1, h1, *_ = dens(kp, k2_, K)
            return 2/(a2 + 2*kp)/(Dg*h1)
        return mp.mpf(0)
    def rho_H(kp, K):
        if 0 < kp < P:
            k0 = (2*Pp*kp + K)/(2*kp)
            Dg = -2*kp*k0 + K; h1 = 2*P*k0; t1 = 2*(P - kp)*k0 + K; h2 = 2*Pp*kp
            return (1/kp)*Dg/(t1*h1*h2)
        if kp >= P: return (1/P)/((2*Pp*kp + K)*(2*Pp*kp))
        return mp.mpf(0)
    def rtilde(kp, K):
        return rho_G(kp, K) - rho_S(kp, K) - rho_C1(kp, K) - rho_C2(kp, K) - rho_H(kp, K)
    return rho_G, rtilde

def UD(t):
    lam = mp.sqrt(1 - 4*t); rho = 2/(1 - 2*t + lam)
    return (4*mp.polylog(2, -rho*t) + mp.log(rho*t)**2 + mp.pi**2/3)/lam

for (P, Pp, m2) in [(mp.mpf('0.8'), mp.mpf('1.3'), mp.mpf('0.02')), (mp.mpf(1)/mp.sqrt(2), mp.mpf(1)/mp.sqrt(2), mp.mpf('0.001'))]:
    rho_G, rt = setup(P, Pp, m2)
    Qt2 = 2*P*Pp
    Q2 = Qt2 + 2*m2 + m2**2/Qt2
    t = m2/Q2
    exact = UD(t)/Q2
    regsum = (mp.log(Qt2/m2)**2 + mp.pi**2/3)/Qt2
    # breakpoints
    kpb = [-m2/(2*Pp), 0, m2**2, m2, mp.sqrt(m2), P/2, P, 2*P, 10*P, mp.inf]
    Kb = lambda kp: [0, m2**2, m2, 1, mp.inf]
    inner = lambda kp: mp.quad(lambda K: rt(kp, K), Kb(kp))
    val = mp.quad(inner, kpb)
    innerG = lambda kp: mp.quad(lambda K: rho_G(kp, K), Kb(kp))
    valG = mp.quad(innerG, kpb)
    print(f"P={mp.nstr(P,4)} P'={mp.nstr(Pp,4)} m2={mp.nstr(m2,4)}:")
    print(f"   int rho_Gamma (d=4) = {mp.nstr(valG,12)}   exact I = {mp.nstr(exact,12)}")
    print(f"   int remainder (d=4) = {mp.nstr(val,12)}   I - (D.32) = {mp.nstr(exact - regsum,12)}")
    # pointwise remainder density vs scale (relative to rho_Gamma)
    for lab, kp, K in [("soft  k+~m2, K~m2^2", m2, m2**2), ("coll1 k+~P/2, K~m2", P/2, m2),
                       ("hard  k+~P/2, K~1", P/2, mp.mpf(1)), ("coll2-ish k+~m2, K~m2", m2, m2)]:
        g = rho_G(kp, K); r = rt(kp, K)
        print(f"   {lab}: rho_Gamma={mp.nstr(g,6)}  remainder={mp.nstr(r,6)}  ratio={mp.nstr(r/g,4)}")
