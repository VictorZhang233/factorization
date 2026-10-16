# Independent check of L4(b)-(d): [X1,X2] = i f T_i T_j1 T_j2; (d1) Wigner-Eckart/singlet formula; (d2) reality; norms.
import sys,os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
rng=np.random.default_rng(12345)
# Gell-Mann
l=np.zeros((8,3,3),complex)
l[0][0,1]=l[0][1,0]=1
l[1][0,1]=-1j; l[1][1,0]=1j
l[2][0,0]=1; l[2][1,1]=-1
l[3][0,2]=l[3][2,0]=1
l[4][0,2]=-1j; l[4][2,0]=1j
l[5][1,2]=l[5][2,1]=1
l[6][1,2]=-1j; l[6][2,1]=1j
l[7]=np.diag([1,1,-2])/np.sqrt(3)
T3=l/2
T3b=-np.conj(T3)          # = -(T^a)^T
# f^{abc}
f=np.zeros((8,8,8))
for a in range(8):
    for b in range(8):
        c_=T3[a]@T3[b]-T3[b]@T3[a]   # = i f^{abc} T^c
        for c in range(8):
            f[a,b,c]=np.real(np.trace(c_@T3[c])*2/1j)
# adjoint on traceless part of 3 x 3bar in a REAL orthonormal basis (matrix units)
I3=np.eye(3)
T33b=np.array([np.kron(T3[a],I3)+np.kron(I3,T3b[a]) for a in range(8)])
sing=np.eye(3).reshape(9)/np.sqrt(3)
M=np.eye(9)-np.outer(sing,sing)
U,s,Vt=np.linalg.svd(M); B=U[:,:8].real          # real basis of traceless subspace
T8=np.array([B.T@T33b[a]@B for a in range(8)])
reps={'3':T3,'3b':T3b,'8':T8}
sgn=np.array([1,-1,1,1,-1,1,-1,1])
for nm,T in reps.items():
    ok=all(np.allclose(np.conj(T[a]),sgn[a]*T[a]) for a in range(8))
    cas=sum(T[a]@T[a] for a in range(8))
    lie=all(np.allclose(T[a]@T[b]-T[b]@T[a],1j*np.einsum('c,cij->ij',f[a,b],T)) for a in range(8) for b in range(8))
    print(f'rep {nm}: Lie algebra {lie}, Casimir {np.real(cas[0,0]):.4f}, (T^a)*=s_a T^a with Gell-Mann signs: {ok}')
print('s_a s_b s_c = -1 when f!=0:', all(sgn[a]*sgn[b]*sgn[c]==-1 for a in range(8) for b in range(8) for c in range(8) if abs(f[a,b,c])>1e-9))
def op(T_list,dims,pos,a):
    mats=[np.eye(d) for d in dims]; mats[pos]=T_list[a]
    out=mats[0]
    for m in mats[1:]: out=np.kron(out,m)
    return out
def gens(labels,pos):
    dims=[reps[x].shape[1] for x in labels]
    return [op(reps[labels[pos]],dims,pos,a) for a in range(8)]
def null_space(mats,tol=1e-9):
    A=np.vstack(mats); u,s,vh=np.linalg.svd(A)
    n=A.shape[1]; r=np.sum(s>tol*max(1,s[0]))
    return vh[r:].conj().T
def analyse(Arem,Brem,i,j1,j2,RA_casimir,label,kappa=None):
    labels=list(Arem)+list(Brem); nA=len(Arem)
    dims=[reps[x].shape[1] for x in labels]; D=int(np.prod(dims))
    Ttot=[sum(gens(labels,p)[a] for p in range(len(labels))) for a in range(8)]
    TA=[sum(gens(labels,p)[a] for p in range(nA)) for a in range(8)]
    S=null_space(Ttot)                       # singlets of A-rem x B-rem
    CA=sum(t@t for t in TA)
    # project singlets onto A-rem Casimir eigenspace RA_casimir
    Ms=S.conj().T@CA@S; ev,evec=np.linalg.eigh((Ms+Ms.conj().T)/2)
    sel=np.abs(ev-RA_casimir)<1e-6
    P=S@evec[:,sel]                          # orthonormal basis of DY space
    Ti=gens(labels,i); Tj1=gens(labels,j1); Tj2=gens(labels,j2)
    X1=sum(Ti[a]@Tj1[a] for a in range(8)); X2=sum(Ti[a]@Tj2[a] for a in range(8))
    C=X1@X2-X2@X1
    rhs=1j*sum(f[a,b,c]*Ti[c]@Tj1[a]@Tj2[b] for a in range(8) for b in range(8) for c in range(8) if abs(f[a,b,c])>1e-12)
    print(f'[{label}] dims={D}, #singlets={S.shape[1]}, dim DY space={P.shape[1]}; [X1,X2]==i f T_i T_j1 T_j2: {np.allclose(C,rhs)}')
    print('   X1 real symmetric:',np.allclose(X1,X1.real) and np.allclose(X1,X1.T), '; [X1,X2] real antisymmetric:', np.allclose(C,C.real) and np.allclose(C,-C.T))
    PCP=P.conj().T@C@P
    print(f'   operator norm ||P[X1,X2]P|| = {np.linalg.norm(PCP,2):.4f}')
    # real DY states: need a real basis of the DY space; the space is conjugation invariant -> take Re/Im parts
    R=np.hstack([P.real,P.imag]); u,s,vh=np.linalg.svd(R,full_matrices=False); Preal=u[:,s>1e-8]
    print('   DY space conjugation-invariant (real basis dim == dim):', Preal.shape[1]==P.shape[1])
    mx=0
    for t in range(5):
        v=Preal@rng.normal(size=Preal.shape[1]); v/=np.linalg.norm(v)
        mx=max(mx,abs(v.conj()@C@v))
    print(f'   max |<psi|[X1,X2]|psi>| over random REAL DY states: {mx:.2e}')
    # (d1): <psi|[X1,X2]|psi> = -<psi|(K_i x 1) i f T_j1 T_j2 sum_k T_k|psi>, check with kappa (dim M=1)
    others=[p for p in range(nA,len(labels)) if p not in (j1,j2)]
    if kappa is not None:
        Tk=[sum(gens(labels,p)[a] for p in others) for a in range(8)] if others else [np.zeros((D,D)) for a in range(8)]
        O=1j*sum(f[a,b,c]*Tj1[a]@Tj2[b]@Tk[c] for a in range(8) for b in range(8) for c in range(8) if abs(f[a,b,c])>1e-12)
        mxd=0; vals=[]
        for t in range(5):
            v=P@(rng.normal(size=P.shape[1])+1j*rng.normal(size=P.shape[1])); v/=np.linalg.norm(v)
            lhs=v.conj()@C@v; r=-kappa*(v.conj()@O@v); mxd=max(mxd,abs(lhs-r)); vals.append(lhs)
        print(f'   (d1) with kappa_i={kappa}: max|lhs-rhs| over random complex DY states = {mxd:.2e}; sample lhs = {np.round(vals[:3],4)}')
    else:
        mx=0
        for t in range(5):
            v=P@(rng.normal(size=P.shape[1])+1j*rng.normal(size=P.shape[1])); v/=np.linalg.norm(v)
            mx=max(mx,abs(v.conj()@C@v))
        print(f'   max |<psi|[X1,X2]|psi>| over random COMPLEX DY states: {mx:.2e}')
C3b=4/3
# meson A (a=q, A-rem = qbar), B-rem = qbar qbar g  (j1,j2 = qbar qbar, passive g)
analyse(['3b'],['3b','3b','8'],0,1,2,C3b,'A-rem=qbar; B-rem=qbar qbar g',kappa=1.0)
# diquark A-rem (3x3 -> 3bar), B-rem = qbar qbar g
analyse(['3','3'],['3b','3b','8'],0,2,3,C3b,'A-rem=qq(3bar); B-rem=qbar qbar g',kappa=0.5)
# diquark A-rem, B-rem = qbar q q with j1,j2 = (qbar, q)
analyse(['3','3'],['3b','3','3'],0,2,3,C3b,'A-rem=qq(3bar); B-rem=qbar q q (j1=qbar,j2=q)',kappa=0.5)
# A-rem = q q g projected on 3bar (multiplicity 2), B-rem = {j1,j2} = qbar qbar : should vanish identically
analyse(['3','3','8'],['3b','3b'],0,3,4,C3b,'A-rem=qqg(3bar, mult 2); B-rem=qbar qbar={j1,j2}')
# valence p pbar: A-rem = ud (3bar), B-rem = ubar dbar = {j1,j2}
analyse(['3','3'],['3b','3b'],0,2,3,C3b,'valence p pbar; B-rem={j1,j2}')
