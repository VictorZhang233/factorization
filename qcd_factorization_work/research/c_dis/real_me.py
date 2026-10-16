"""
real_me.py -- D-dimensional squared matrix elements for
   (a) gamma*(q) + q(p) -> q(p') + g(k)
   (b) gamma*(q) + g(p) -> q(k1) + qbar(k2)
contracted with the two D-dim projectors  -g_{mu nu}  and  p_mu p_nu.

Variables:  Q^2 = -q^2 (set to 1: every projected quantity used is dimensionless),
            z = Q^2/(2 p.q)   (partonic Bjorken variable),
            y = (1 - cos theta*)/2, theta* = angle between the outgoing gluon (a) / quark (b)
                and the incoming parton p in the gamma*-parton c.m. frame.
            p.k = y p.q  (a)  ;  p.k1 = y p.q  (b).
Dirac traces in D = 4 - 2 eps (Tr 1 = 4).  Polarisation sums: -g_{rho sigma} (exact here,
since the amplitudes contain a single gluon and satisfy k_rho M^rho = 0).
Returned objects (no couplings, colour or averaging factors):
   Tq_g  = (-g_{mu nu}) (-g_{rho sigma}) Tr[ p  Obar^{mu sigma} p'  O^{nu rho} ]
   Tq_pp = ( p_mu p_nu) (-g_{rho sigma}) Tr[ ... ]          (quark channel)
   Tg_g, Tg_pp analogously for the gluon channel with Tr[ k1 O^{nu rho} k2 Obar^{mu sigma} ].
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
import dirac_d as dd

z, y, eps = sp.symbols('z y epsilon')
Dsym = dd.D
I, V = dd.I, dd.V


def quark_channel():
    Q2 = 1
    pq = Q2 / (2 * z)
    dd.set_dots({('p', 'p'): 0, ('k', 'k'): 0, ('q', 'q'): -Q2,
                 ('p', 'q'): pq, ('p', 'k'): y * pq,
                 ('q', 'k'): (-Q2 + (Q2 / z) * (1 - y)) / 2})
    s_hat = Q2 * (1 - z) / z            # (p+q)^2
    t_hat = -(Q2 / z) * y               # (p-k)^2
    P = V(p=1)
    Pp = V(p=1, q=1, k=-1)              # p' = p + q - k
    S = V(p=1, q=1)                     # p + q
    T = V(p=1, k=-1)                    # p - k

    def proj(mu_slot, nu_slot, sign):
        # O^{nu rho}    = g^rho S g^nu / s + g^nu T g^rho / t
        # Obar^{mu sig} = g^mu S g^sig / s + g^sig T g^mu / t
        Ob = [([mu_slot, S, I('r')], 1 / s_hat), ([I('r'), T, mu_slot], 1 / t_hat)]
        O = [([I('r'), S, nu_slot], 1 / s_hat), ([nu_slot, T, I('r')], 1 / t_hat)]
        tot = 0
        for ob, c1 in Ob:
            for o, c2 in O:
                tot += c1 * c2 * dd.tr([P] + ob + [Pp] + o)
        # -g_{rho sigma}: factor -1 ; projector sign given by caller
        return sp.factor(sp.simplify(-sign * tot))

    Tg = proj(I('m'), I('m'), -1)      # (-g_{mu nu}) -> -1 times contraction
    Tpp = proj(P, P, +1)               # p_mu p_nu    -> replace gamma^mu, gamma^nu by p-slash
    return Tg.subs(Dsym, 4 - 2 * eps), Tpp.subs(Dsym, 4 - 2 * eps)


def gluon_channel():
    Q2 = 1
    pq = Q2 / (2 * z)
    # basis p (gluon), q, k1 (quark);  k2 = p + q - k1
    dd.set_dots({('p', 'p'): 0, ('k1', 'k1'): 0, ('q', 'q'): -Q2,
                 ('p', 'q'): pq, ('p', 'k1'): y * pq,
                 ('q', 'k1'): (-Q2 + (Q2 / z) * (1 - y)) / 2})
    K1 = V(k1=1)
    K2 = V(p=1, q=1, k1=-1)
    A = V(k1=1, q=-1)                   # k1 - q  (= p - k2)
    B = V(k1=1, p=-1)                   # k1 - p  (= q - k2)
    A2 = -2 * (y * pq) + 0               # placeholder, recomputed below
    # (k1 - q)^2 = -Q2 - 2 k1.q ;  (k1 - p)^2 = -2 p.k1
    k1q = (-Q2 + (Q2 / z) * (1 - y)) / 2
    a2 = -Q2 - 2 * k1q
    b2 = -2 * y * pq
    P = V(p=1)

    def proj(mu_slot, nu_slot, sign):
        # O^{nu rho}    = g^nu A g^rho / a2 + g^rho B g^nu / b2
        # Obar^{mu sig} = g^sig A g^mu / a2 + g^mu B g^sig / b2
        O = [([nu_slot, A, I('r')], 1 / a2), ([I('r'), B, nu_slot], 1 / b2)]
        Ob = [([I('r'), A, mu_slot], 1 / a2), ([mu_slot, B, I('r')], 1 / b2)]
        tot = 0
        for o, c1 in O:
            for ob, c2 in Ob:
                tot += c1 * c2 * dd.tr([K1] + o + [K2] + ob)
        return sp.factor(sp.simplify(-sign * tot))

    Tg = proj(I('m'), I('m'), -1)
    Tpp = proj(P, P, +1)
    return Tg.subs(Dsym, 4 - 2 * eps), Tpp.subs(Dsym, 4 - 2 * eps)


if __name__ == '__main__':
    Tq_g, Tq_pp = quark_channel()
    print('quark channel  -g.T  =', Tq_g)
    print('quark channel  pp.T  =', Tq_pp)
    Tg_g, Tg_pp = gluon_channel()
    print('gluon channel  -g.T  =', Tg_g)
    print('gluon channel  pp.T  =', Tg_pp)
