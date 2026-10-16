# O(alpha_s) thrust distribution (De Rujula-Ellis-Floratos-Gaillard 1978), units C_F alpha_s/(2 pi):
#  A(T) = 2(3T^2-3T+2)/(T(1-T)) ln((2T-1)/(1-T)) - 3(3T-2)(2-T)/(1-T),  2/3 < T < 1, tau = 1-T.
# (i) small-tau singular part must be -(4 ln tau + 3)/tau ;
# (ii) total O(alpha_s) = sigma0*(3/2)*C_F alpha_s/(2pi) [i.e. alpha_s/pi] fixes the delta(tau) coefficient c_delta
#      of the full distribution (with [..]_+ defined on [0,1]); expected pi^2/3 - 1.
import sys,os; sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps=30
def A(tau):
    T=1-tau   # write 1-T as tau and 2T-1 as 1-2tau to avoid cancellation
    return 2*(3*T**2-3*T+2)/(T*tau)*mp.log((1-2*tau)/tau) - 3*(3*T-2)*(2-T)/tau
S=lambda tau: -(4*mp.log(tau)+3)/tau
for t in [mp.mpf('1e-3'),mp.mpf('1e-6'),mp.mpf('1e-9')]:
    print(f"tau={mp.nstr(t,3)}: tau*(A-S) = {mp.nstr(t*(A(t)-S(t)),8)}  (-> 0 means singular part correct)")
tmax=mp.mpf(1)/3
nonsing=mp.quad(lambda t:A(t)-S(t),[0,mp.mpf('1e-8'),mp.mpf('1e-4'),mp.mpf('0.01'),tmax])
plus_part=-4*mp.log(tmax)**2/2 - 3*mp.log(tmax)   # int_0^{1/3} of -4[ln t/t]_+ - 3[1/t]_+
cdelta=mp.mpf(3)/2-nonsing-plus_part
print("c_delta from normalization =",mp.nstr(cdelta,20))
print("pi^2/3 - 1              =",mp.nstr(mp.pi**2/3-1,20))
# cumulant check: Sigma(tau)=1+(CF as/2pi)[-2 ln^2 tau - 3 ln tau + pi^2/3 - 1] + O(tau)
for t in [mp.mpf('1e-2'),mp.mpf('1e-4')]:
    exact=mp.mpf(3)/2 - mp.quad(A,[t,tmax])
    approx=-2*mp.log(t)**2-3*mp.log(t)+mp.pi**2/3-1
    print(f"cumulant tau={mp.nstr(t,2)}: exact {mp.nstr(exact,10)}  singular {mp.nstr(approx,10)}  diff {mp.nstr(exact-approx,4)} (O(tau ln tau))")
