"""X2 fix round 1 / r1_triangle_covariant.py -- identification of the FIBERED values of the triangle's Collins terms with
the COVARIANT dimensionally regulated values (review r1_1 R1(i), r1_2 F6).

Covariant values (Feynman/Schwinger parameters, d = 4 - 2 eps, measure mu^{2eps} int d^dk/(i pi^{d/2}), propagators
1/(-l^2 - i0); n1.k = P k^-, n2.k = P' k^+, 2 n1.n2 = Qt^2 = 2PP'):
  C_S  = 1/((-k^2)(m2 + 2 n1.k)(m2 + 2 n2.k)):  1/(ABC) = int dl1 dl2 2/(A + l1 B + l2 C)^3,  Delta = l1 l2 Qt^2 + (l1+l2) m2
         => int C_S = Gamma(eps)^2 Gamma(1-eps) (mu^2 Qt^2/m2^2)^eps / Qt^2                         (0 < eps < 1, convergent)
  C_C1 = T1 + T2, T1 = 1/((-k^2)(-(p1-k)^2)(2 n2.k)), T2 = -1/((-k^2)(m2 + 2 n1.k)(2 n2.k)) (scaleless, 0 in DR);
         Delta(T1) = x(1-x) m2 + x l Qt^2  => int T1 = Gamma(1+eps) Gamma(-eps) Gamma(1-eps)/(eps Gamma(1-2eps)) (mu^2/m2)^eps / Qt^2
         (the x- and l-integrals converge in disjoint eps-domains: analytic continuation, standard DR convention);
  C_C2 = same with P <-> P' (the closed form depends on Qt only);
  C_H  = Dg/(t1 h1 t2 h2) = massless on-shell triangle + scaleless terms
         => int C_H = Gamma(1+eps) Gamma(1-eps)^2/(eps^2 Gamma(1-2eps)) (mu^2/Qt^2)^eps / Qt^2.
Fibered values: (mu^{2eps}/Gamma(1-eps)) int dk+ dkap kap^{-eps} rho_{C_R}, densities of X2-Prop3.1 (general P, P')."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 20

def covariant(P, Pp, m2, eps, mu2=1):
    Qt2 = 2*P*Pp; G = mp.gamma
    return {'C_S': G(eps)**2*G(1 - eps)*(mu2*Qt2/m2**2)**eps/Qt2,
            'C_C1': G(1 + eps)*G(-eps)*G(1 - eps)/(eps*G(1 - 2*eps))*(mu2/m2)**eps/Qt2,
            'C_C2': G(1 + eps)*G(-eps)*G(1 - eps)/(eps*G(1 - 2*eps))*(mu2/m2)**eps/Qt2,
            'C_H': G(1 + eps)*G(1 - eps)**2/(eps**2*G(1 - 2*eps))*(mu2/Qt2)**eps/Qt2}

def densities(P, Pp, m2):
    Qt2 = 2*P*Pp; a = m2/Pp
    def rS(x, k):
        return 1/((x*m2 + P*k)*(m2 + 2*Pp*x)) if x > 0 else 0
    def rC1(x, k):
        if 0 < x < P:
            u = x/P; A = x*m2*(1 - u) + P*k; B = x*m2 + P*k
            return x*m2/(Qt2*A*B)
        if x >= P:
            return -1/((2*Pp*x)*(x*m2 + P*k))
        return 0
    def rC2(x, k):
        if x > 0:
            e2 = m2 + 2*Pp*x; return -1/(P*e2*(e2 + k))
        if -a/2 < x <= 0:
            w = 2*x + a; return w/(P*((a - w)*Pp*w + a*k)*(Pp*w + k))
        return 0
    def rH(x, k):
        h2 = 2*Pp*x
        if 0 < x < P:
            return -x/(P*(h2 + k)*(h2*(P - x) + P*k))
        if x >= P:
            return 1/(P*(h2 + k)*h2)
        return 0
    return {'C_S': rS, 'C_C1': rC1, 'C_C2': rC2, 'C_H': rH}

def fibered(rho, P, Pp, m2, eps, mu2=1):
    a = m2/Pp
    fk = lambda x: mp.quad(lambda lk: rho(x, mp.e**lk)*mp.e**(lk*(1 - eps)), [-60, mp.log(m2), 0, 10, 60])
    pts_pos = [mp.mpf(0), m2*1e-6, m2*1e-3, m2, mp.mpf(P)/10, P, 2*P, 10*P, 1e3*P, mp.inf]
    I = mp.quad(fk, pts_pos)
    I += mp.quad(fk, [-a/2, -a/4, 0])
    return I*mu2**eps/mp.gamma(1 - eps)

if __name__ == "__main__":
    for (P, Pp, m2, eps) in [(mp.mpf('0.8'), mp.mpf('1.3'), mp.mpf('0.1'), mp.mpf('0.3')),
                             (1/mp.sqrt(2), 1/mp.sqrt(2), mp.mpf('0.01'), mp.mpf('0.2'))]:
        print(f"P={mp.nstr(P,4)}, P'={mp.nstr(Pp,4)}, m2={mp.nstr(m2,3)}, eps={mp.nstr(eps,2)}:")
        cov = covariant(P, Pp, m2, eps); dens = densities(P, Pp, m2)
        for nm in ['C_S', 'C_C1', 'C_C2', 'C_H']:
            fb = fibered(dens[nm], P, Pp, m2, eps)
            print(f"   {nm:5s}: fibered {mp.nstr(fb, 12):>18}   covariant {mp.nstr(cov[nm], 12):>18}   rel.diff {mp.nstr(abs(fb/cov[nm] - 1), 2)}")
