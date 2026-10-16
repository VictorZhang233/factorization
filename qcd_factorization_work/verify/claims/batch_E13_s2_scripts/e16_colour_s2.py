#!/usr/bin/env python3
"""E16 stage-2: BFH colour factors A_q, A_g by matrix-free colour algebra, SU(N), N=2..6.

Conventions (all-outgoing): outgoing quark index c: T^x psi = t^x psi (on c);
incoming quark index (lower) : T^x psi = - psi t^x (on that index);
gluon index g: (T^x psi)_g = (F^x)_{g g'} psi_{g'}, (F^x)_{gg'} = -i f^{x g g'}.
Born:  a=quark : M_{c a b} = (t^b)_{c a}   (q_a g_b -> q_c)
       a=gluon : M_{c b a} = (t^a)_{c b}   (g_a q_b -> q_c)
psi = T_a^d M (gluon d emitted from incoming parton a).
Computes  R_a = <psi| (1/3)[S,[S,T_ad^2]] |psi> / <M|M>,  S = (T_a+T_b)^2,
T_ad^2 = sum_{i<j, (ij) != (ad)} T_i.T_j, and the shortcut
R_a = -(1/3) <S psi|(C_a - U)|S psi>/<M|M>, U = (T_a+T_d)^2 (uses U psi = C_a psi).
BFH: A_q/(f f sigma) = (8/3) N^2 T_R^4 = N^2/6 ; A_g/(f f sigma) = -(32/3) N^2 T_R^4 = -2N^2/3.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from fractions import Fraction

def sun_generators(N):
    gens = []
    for i in range(N):
        for j in range(i + 1, N):
            m = np.zeros((N, N), complex); m[i, j] = m[j, i] = 0.5; gens.append(m)
            m = np.zeros((N, N), complex); m[i, j] = -0.5j; m[j, i] = 0.5j; gens.append(m)
    for k in range(1, N):
        m = np.zeros((N, N), complex)
        for i in range(k): m[i, i] = 1
        m[k, k] = -k
        m *= 1/np.sqrt(2*k*(k + 1)); gens.append(m)
    t = np.array(gens)
    # f^{abc} = -2 i Tr([t^a,t^b] t^c)
    comm = np.einsum('aij,bjk->abik', t, t) - np.einsum('bij,ajk->abik', t, t)
    f = (-2j*np.einsum('abij,cji->abc', comm, t)).real
    return t, f

def run(N, which):
    t, f = sun_generators(N)
    A = N*N - 1
    F = -1j*f                                  # (F^x)_{g g'} = -i f^{x g g'}
    assert np.allclose(np.einsum('aij,bji->ab', t, t), 0.5*np.eye(A))
    CF, CA = (N*N - 1)/(2*N), N
    # index layout of 4-parton tensors: (c, a, b, d) ; meaning of a, b depends on 'which'
    if which == 'q':   # a = incoming quark (lower fundamental), b = incoming gluon, c = outgoing quark
        M = np.einsum('bca->cab', t)                         # M[c,a,b] = t^b_{ca}
        kinds = {'c': 'qout', 'a': 'qin', 'b': 'g'}
        Ca = CF
    else:              # a = incoming gluon, b = incoming quark (lower), c = outgoing quark; layout (c, b, a)
        M = np.einsum('acb->cba', t)                         # M[c,b,a] = t^a_{cb}
        kinds = {'c': 'qout', 'b': 'qin', 'a': 'g'}
        Ca = CA
    order3 = ['c', 'a', 'b'] if which == 'q' else ['c', 'b', 'a']
    order4 = order3 + ['d']
    kinds4 = dict(kinds); kinds4['d'] = 'g'

    def act(leg, x, psi, order, kinds_):
        ax = order.index(leg)
        k = kinds_[leg]
        if k == 'qout':
            mat = t[x]
        elif k == 'qin':
            mat = -t[x].T
        else:
            mat = F[x]
        return np.moveaxis(np.tensordot(mat, psi, axes=([1], [ax])), 0, ax)

    # colour conservation on Born
    for x in range(A):
        tot = sum(act(l, x, M, order3, kinds) for l in order3)
        assert np.allclose(tot, 0), 'Born not colour singlet'
    # emission psi[...,d] = (T_a^d M)
    psi = np.stack([act('a', x, M, order3, kinds) for x in range(A)], axis=-1)
    for x in range(A):
        tot = sum(act(l, x, psi, order4, kinds4) for l in order4)
        assert np.allclose(tot, 0), '4-parton state not colour singlet'
    nM = np.vdot(M, M).real
    assert np.isclose(np.vdot(psi, psi).real, Ca*nM)

    def dot(l1, l2, v):
        return sum(act(l1, x, act(l2, x, v, order4, kinds4), order4, kinds4) for x in range(A))
    def S(v):
        return dot('a', 'a', v) + dot('b', 'b', v) + 2*dot('a', 'b', v)
    def U(v):
        return dot('a', 'a', v) + dot('d', 'd', v) + 2*dot('a', 'd', v)
    pairs = [('a', 'b'), ('a', 'c'), ('b', 'c'), ('b', 'd'), ('c', 'd')]   # all i<j except (a,d)
    def Tad2(v):
        return sum(dot(i, j, v) for i, j in pairs)
    assert np.allclose(U(psi), Ca*psi), 'U psi != C_a psi'
    Sp = S(psi); SSp = S(Sp)
    # <psi|[S,[S,V]]|psi> = <psi|SSV - 2SVS + VSS|psi>
    V = Tad2
    val = np.vdot(SSp, V(psi)) - 2*np.vdot(Sp, V(Sp)) + np.vdot(psi, V(SSp))
    R_direct = (val/3/nM)
    R_short = (-(1/3)*np.vdot(Sp, Ca*Sp - U(Sp))/nM)
    return R_direct, R_short

print(' N   R_q(direct)        R_q(shortcut)     N^2/6       R_g(direct)        R_g(shortcut)    -2N^2/3')
allok = True
for N in [2, 3, 4, 5, 6]:
    rq, rqs = run(N, 'q'); rg, rgs = run(N, 'g')
    print(f'{N:2d}  {rq.real:+.10f}{rq.imag:+.1e}j  {rqs.real:+.10f}  {N*N/6:+.6f}   {rg.real:+.10f}{rg.imag:+.1e}j  {rgs.real:+.10f}  {-2*N*N/3:+.6f}')
    allok &= abs(rq - N*N/6) < 1e-9 and abs(rg + 2*N*N/3) < 1e-9 and abs(rqs - rq) < 1e-9 and abs(rgs - rg) < 1e-9
print('PASS' if allok else 'FAIL', 'A_q = (8/3) N^2 T_R^4 sigma, A_g = -(32/3) N^2 T_R^4 sigma for N = 2..6 (two independent evaluations)')
