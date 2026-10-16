# asymmetric window error: is it O(lamJ/min(K1,K2) + max(K1,K2)^2/Lam^2)?  spectator insertion, R single pole
import sys,os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
exec(open('check_e28.py').read().split('print("Lemma E.28(iii)')[0])
Lam=mp.mpf(10)**4
for (K1,K2) in [(20,20),(20,200),(20,2000),(200,2000),(2000,2000),(20,4000)]:
    full,pred,Jm,Jp,terms,z,r=run(mp.mpf(1),Lam,+1,spectator=True)
    win=int_window(terms,mp.mpf(K1),mp.mpf(K2))
    err=abs(win-Jm)/abs(Jm)
    print(K1,K2,'rel err',mp.nstr(err,4),' 1/minK',mp.nstr(1/mp.mpf(min(K1,K2)),4),' maxK^2/Lam^2',mp.nstr(mp.mpf(max(K1,K2))**2/Lam**2,4), ' maxK/Lam', mp.nstr(mp.mpf(max(K1,K2))/Lam,4))
