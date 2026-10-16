# N17 (stage 2): entanglement test  sum_{X,Y} C(X,Y) = C_F^2 + 4 T_F^2 (N^2-1)/N^2  vs factorized C_F^2.
# METHOD (independent of stage 1): generators built from a RANDOM orthonormal basis of traceless Hermitian
# matrices (Gram-Schmidt in the Hilbert-Schmidt inner product, normalised Tr(t^a t^b) = delta/2), so no
# particular basis is used; amplitudes are explicit numpy tensors with explicit colour-singlet hadrons;
# the antitriplet spectator vertex is derived from the conjugate representation (-t^{aT}); both
# same-side (both gluons in M) and opposite-side (one in M, one in M*) configurations; U(1) control.
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
rng = np.random.default_rng(20261011)
npass = 0; nfail = 0
def check(name, ok, info=""):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(("PASS " if ok else "FAIL ") + name + ("  " + info if info else ""), flush=True)
def generators(N):
    mats = []
    for _ in range(N*N - 1):
        A = rng.normal(size=(N, N)) + 1j*rng.normal(size=(N, N))
        H = (A + A.conj().T)/2; H -= np.trace(H)/N*np.eye(N)
        for B in mats:
            H -= 2*np.trace(B @ H).real*B   # remove projection (Tr(B B) = 1/2)
        nrm = np.sqrt(np.trace(H @ H).real*2)
        mats.append(H/nrm)
    T = np.array(mats)
    G = np.einsum('aij,bji->ab', T, T)
    assert np.allclose(G, 0.5*np.eye(N*N-1)), "normalisation"
    # completeness: sum_a t^a_ij t^a_kl = 1/2 (d_il d_kj - d_ij d_kl / N)
    comp = np.einsum('aij,akl->ijkl', T, T)
    ref = 0.5*(np.einsum('il,kj->ijkl', np.eye(N), np.eye(N)) - np.einsum('ij,kl->ijkl', np.eye(N), np.eye(N))/N)
    assert np.allclose(comp, ref), "completeness"
    return T
# Process: H1 = (quark i1, antitriplet spectator s1) singlet psi = delta/sqrt(N); same for H2.
# Hard part: colour-neutral exchange: quark 1 -> quark 3 (same colour line), quark 2 -> quark 4.
# Final state colours: c3, c4 (quarks), s1, s2 (spectators, antitriplet indices).
# Gluon from spectator j: spectator vertex (antitriplet) = -(t^a)^T acting on the spectator index,
# other end on line X with t^a in fermion-flow order (lines 1,2 incoming; 3,4 outgoing).
def amplitude(T, N, att1=None, att2=None):
    """att1: line (1..4) hit by the gluon from spectator 1 (or None); att2 likewise for spectator 2.
       Returns M[c3, c4, s1, s2] (sum over gluon colours a (from s1) and b (from s2))."""
    I = np.eye(N)
    ngl = T.shape[0]
    psi = I/np.sqrt(N)                       # psi[i, s]
    M = np.zeros((N, N, N, N), dtype=complex)
    alist = range(ngl) if att1 else [None]
    blist = range(ngl) if att2 else [None]
    for a in alist:
        for b in blist:
            # operators acting on colour line A (1 -> 3) and line B (2 -> 4), in fermion-flow order
            L13_in = I.copy(); L13_out = I.copy(); L24_in = I.copy(); L24_out = I.copy()
            S1 = I.copy(); S2 = I.copy()
            if att1:
                S1 = -T[a].T                 # antitriplet vertex on spectator 1: s1' <- s1
                if att1 == 1: L13_in = T[a] @ L13_in
                if att1 == 3: L13_out = T[a] @ L13_out
                if att1 == 2: L24_in = T[a] @ L24_in
                if att1 == 4: L24_out = T[a] @ L24_out
            if att2:
                S2 = -T[b].T
                if att2 == 1: L13_in = T[b] @ L13_in
                if att2 == 3: L13_out = T[b] @ L13_out
                if att2 == 2: L24_in = T[b] @ L24_in
                if att2 == 4: L24_out = T[b] @ L24_out
            # when both gluons hit the same segment the ordering matters only for a single line; here the
            # two gluons never hit the same segment in the classes below except where checked separately.
            A13 = L13_out @ L13_in; A24 = L24_out @ L24_in
            # M[c3,c4,s1',s2'] = sum_{i1,s1,i2,s2} A13[c3,i1] S1[s1',s1] psi[i1,s1] * A24[c4,i2] S2[s2',s2] psi[i2,s2]
            M += np.einsum('ci,ts,is->ct', A13, S1, psi)[:, None, :, None]*np.einsum('di,us,is->du', A24, S2, psi)[None, :, None, :]
    return M
def overlap(M1, M2):
    return np.einsum('abcd,abcd->', M1, M2.conj())
for N in [2, 3, 4, 5]:
    T = generators(N)
    CF = (N*N - 1)/(2*N); TF = 0.5
    M0 = amplitude(T, N)
    norm = overlap(M0, M0).real
    check("N=%d tree normalisation sum|M0|^2 = 1" % N, abs(norm - 1) < 1e-12)
    # single attachments (relative to tree): spectator 1 -> X in {3,4,2}; spectator 2 -> Y in {4,3,1}
    C1 = {X: overlap(amplitude(T, N, att1=X), M0)/norm for X in (3, 4, 2)}
    C2 = {Y: overlap(amplitude(T, N, att2=Y), M0)/norm for Y in (4, 3, 1)}
    check("N=%d single gluon: C1(3) = C2(4) = -C_F; C1(4)=C1(2)=C2(3)=C2(1)=0" % N,
          abs(C1[3] + CF) < 1e-12 and abs(C2[4] + CF) < 1e-12 and max(abs(C1[4]), abs(C1[2]), abs(C2[3]), abs(C2[1])) < 1e-12,
          "C1=%s C2=%s" % ({k: round(v.real, 6) for k, v in C1.items()}, {k: round(v.real, 6) for k, v in C2.items()}))
    # two gluons, same side (both in M)
    Cs = {(X, Y): overlap(amplitude(T, N, att1=X, att2=Y), M0)/norm for X in (3, 4, 2) for Y in (4, 3, 1)}
    # two gluons, opposite sides (gluon 1 in M, gluon 2 in M*)
    Co = {(X, Y): overlap(amplitude(T, N, att1=X), amplitude(T, N, att2=Y))/norm for X in (3, 4, 2) for Y in (4, 3, 1)}
    ent = TF**2*(N*N - 1)/N**2
    for lab, C in (("same side", Cs), ("opposite sides", Co)):
        ok = abs(C[(3, 4)] - CF**2) < 1e-12
        ok &= all(abs(C[(X, Y)] - ent) < 1e-12 for X in (4, 2) for Y in (3, 1))
        ok &= all(abs(C[(X, Y)]) < 1e-12 for (X, Y) in [(3, 3), (3, 1), (4, 4), (2, 4)])
        tot = sum(C.values()).real
        fact = (sum(C1.values())*sum(C2.values())).real
        check("N=%d %s: C(3,4)=C_F^2, crossed = T_F^2(N^2-1)/N^2, mixed = 0" % (N, lab), ok)
        check("N=%d %s: sum C = C_F^2 + 4T_F^2(N^2-1)/N^2 = %.6f ; factorized %.6f" % (N, lab, CF**2 + 4*ent, CF**2),
              abs(tot - (CF**2 + 4*ent)) < 1e-12 and abs(fact - CF**2) < 1e-12 and abs(tot/fact - (1 + 4/(N*N - 1))) < 1e-12,
              "total %.12f, ratio %.6f" % (tot, tot/fact))
    if N == 3:
        check("SU(3): 24/9 vs 16/9", abs(sum(Cs.values()).real - 24/9) < 1e-12 and abs(CF**2 - 16/9) < 1e-12)
# U(1) control: charges e1 (hadron-1 quark line 1->3), e2 (line 2->4); spectator charges -e1, -e2 (neutral hadrons)
e1, e2 = 0.7, -1.3
ch = {1: e1, 3: e1, 2: e2, 4: e2}
C1u = {X: (-e1)*ch[X] for X in (3, 4, 2)}; C2u = {Y: (-e2)*ch[Y] for Y in (4, 3, 1)}
Cu = {(X, Y): (-e1)*ch[X]*(-e2)*ch[Y] for X in (3, 4, 2) for Y in (4, 3, 1)}
check("U(1): two-gluon weights are products of single-exchange weights (sum = product)", abs(sum(Cu.values()) - sum(C1u.values())*sum(C2u.values())) < 1e-14)
print("\nTOTAL: %d PASS, %d FAIL" % (npass, nfail))
