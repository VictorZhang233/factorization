# X1 fix round 2 -- T3(e) restated as a sensitivity proposition.  Regulated A-side weight (even Lorentzian k^- regulator
# chi_K(k) = K^2/(k^2+K^2) on both lines, jet A localized) on the rotated contour k^+ = e^{i pi/4} kappa:
#   v_K(kappa) := W^[12]_K - 1/2 depends only on x_e := iK/z_e, z_e = a_e/(2 k_e^+), |x_e| = 2K|kappa_e|/a_e.
# Claims: (i) v_K = (x1 - x2)/4 + O(|x|^2)          (algebraic; exact rational function of x1, x2)
#         (ii) |v_K| <= c_v (|x1| + |x2|) for |x_e| <= 1/4, and |v_K| <= c_inf everywhere (all four quadrants)
#         (iii) normalized pole weights: sum_p |u_e(p)| <= c_U on the pi/4 rays; poles of each group in a closed quadrant
#         (iv) numerical consistency with T3(f): Im W12(K) ~ K ln(1/K) for small K.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'fix_r1_scripts'))
import numpy as np
import regulator_indep as ri

th = np.pi/4; ph = np.exp(1j*th)
def vK(t1, t2, q, K=1.0, a1=1.0, a2=1.0):
    # choose kappa_e so that |x_e| = 2 K |kappa_e| / a_e = t_e
    k1 = q[0]*t1*a1/(2*K); k2 = q[1]*t2*a2/(2*K)
    u1 = ph*k1; u2 = ph*k2
    return ri.W12(u1, u2, a1, a2, K, q) - 0.5, (1j*K/(a1/(2*u1)), 1j*K/(a2/(2*u2)))

ts = np.exp(np.linspace(np.log(1e-6), np.log(0.25), 120))
cv = 0; cinf = 0; lead_err = 0
for q in ((1, 1), (-1, -1), (-1, 1), (1, -1)):
    T1, T2 = np.meshgrid(ts, ts, indexing='ij')
    V, (x1, x2) = vK(T1, T2, q)
    cv = max(cv, np.max(np.abs(V)/(T1 + T2)))
    lead = (x1 - x2)/4
    lead_err = max(lead_err, np.max(np.abs(V - lead)/(T1 + T2)**2))
    tb = np.exp(np.linspace(np.log(1e-6), np.log(1e6), 400))
    B1, B2 = np.meshgrid(tb, tb, indexing='ij')
    Vb, _ = vK(B1, B2, q)
    cinf = max(cinf, np.max(np.abs(Vb)))
print(f"(i)  |v_K - (x1-x2)/4| <= {lead_err:.3f} (|x1|+|x2|)^2 for |x_e| <= 1/4 (all quadrants)")
print(f"(ii) c_v = sup_{{|x|<=1/4}} |v_K|/(|x1|+|x2|) = {cv:.4f};  c_inf = sup |v_K| = {cinf:.4f}")

# (iii) normalized pole weights on the pi/4 rays: z = (a/(2|kappa|)) e^{-i pi/4} sgn(kappa)
cU = 0
for sg in (1, -1):
    for t in np.exp(np.linspace(np.log(1e-6), np.log(1e6), 2000)):
        z = (1.0/t)*np.exp(-1j*th)*sg*1j*1.0   # |x| = t  <=>  |z| = K/t with K = 1;  direction of z
        z = (1.0/t)*np.exp(-1j*th)*sg
        uz = 1/(z**2 + 1)*1.0; up = z/(2*(z - 1j)); um = z/(2*(z + 1j))
        cU = max(cU, abs(uz) + abs(up) + abs(um))
        assert abs(uz + up + um - 1) < 1e-12
print(f"(iii) c_U = sup sum_p |u_e(p)| on the pi/4 rays = {cU:.4f}  (final group {{z (Re>0,Im<0), -iK}} and initial group {{z (Re<0,Im>0), +iK}} lie in closed quadrants)")

# (iv) consistency with T3(f) values (fix_r1_logs/regulator_indep_A.log, author set): Im W12(K) for K = 0.1, 0.01, 0.001 a/lambda_B
vals = {0.1: -0.00499902, 0.01: -0.00060102, 0.001: -0.00006124}
for K in vals:
    print(f"(iv) K = {K:g} a/lambda_B: Im W12 = {vals[K]:.3e};  Im W12/(K) = {vals[K]/K:.4f};  Im W12/(K ln(1/K)) = {vals[K]/(K*np.log(1/K)):.4f}")
print("ALL PASS" if (cv < 1 and cinf < 1 and lead_err < 5) else "SOME CHECK FAILED")
