import sys,os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps=25
sets=[((1,1),-1,-2,-1,1.0,(-0.38629436112, 0.06148065706)),
      ((0.65,0.9),-1.6,-0.3,-1.6,0.7,(-0.376196716824,0.05987356706)),
      ((1,2),-0.5,-3,-2,-1.3,(0.49648105127,-0.07901741346))]
for (a,A1,A2,Ap,r,claim) in sets:
    a1,a2=a
    rho2=lambda k: a1*a2*2*k*r/((2*k*A1-a1)*(2*k*A2-a1)*(2*k*Ap-a2))
    Ireal=mp.quad(lambda k: rho2(k)/k,[0,1,10,mp.inf])
    Iim=mp.quad(lambda x: rho2(1j*x)/x,[0,1,10,mp.inf])
    dW=-1j/(2*mp.pi)*Iim
    print(f"a={a} A1={A1} A2={A2} A'={Ap} ct2/c1={r}: int_real={mp.nstr(Ireal,12)} int_imag-axis={mp.nstr(Iim,12)} dW/s={mp.nstr(dW,10)}  report: int={claim[0]}, dW/s={claim[1]}i")
