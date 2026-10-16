# X2-subtraction-rev2-1

(extracted verbatim from the workflow journal; structured output of the agent)

## overall

fixable_issues

## per_result

### [per_result 1]
RUN STATUS (answer to the relayed question 在正常运行吗): 不完全正常, not fully normal. The workflow runs and this review completed, but verify/extend/X2-subtraction/REPORT.md still does not exist. Neither do review_r1_*.md or any X1 or X3 report: the harness refuses report files written by subagents. The fix-round report exists only as the structured result in row 96 of journal.jsonl (agent a3b63d44b69bba4fe, X2-subtraction-fix1). I extracted it verbatim to /private/tmp/claude-501/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/scratchpad/x2r2_1b/X2_fix1.md (summary, 28 results, 14 open items) and reviewed that. An earlier rev2-1 attempt (agent a42cd3e182277b640, 02:26) left no result; this is the restarted run. For the same reason review_r2_1.md was NOT written; this StructuredOutput is the review. My check scripts are in .../scratchpad/r2rev1/.

### [per_result 2]
X2-Setup: CORRECT. I checked the conventions and they are consistent with every script: the measure; the normalisation (mu^2eps/Gamma(1-eps)) int dx dkappa kappa^-eps rho; the Qt-Q relation; and rho t = m^2 at Qt = 1.

### [per_result 3]
X2-Thm2.6 (fibered subtraction theorem): CORRECT as an implication. I re-derived (D.10): (1-T_R0)X_R0 = Gamma - sum over R<=R0 of C_R, so r = (1-T_R0)X_R0 - sum over R not<= R0 of C_R. The triangle inequality on the finite cover gives the norm bound, and the integrated statement needs (CS3^phi)+(ID). Minor inconsistency: the hypothesis 'non-maximal members bounded in every UV direction' is never used in the proof, and the Thm 3.3 cover violates it. U_C2 contains the whole sliver {-m^2/2P' < k+ < 0} x {kappa > 0}; the archived sliver certificates constrain only X_w <= -1 and leave kappa free. This is harmless because the sliver items decay like kappa^-2, but the text must be made consistent.

### [per_result 4]
X2-Lem2.7 (identification): CORRECT as a lemma for integrands built from pure denominators. After a pole is substituted, Re(.) does not depend on eta, so |g_eta| >= |g_0|; which side each pole lies on does not depend on eta; G then dominates. GAP in how the lemma is applied. (a) Hypothesis (I2) FAILS for the composite Collins terms. For C_C1 = T1 + T2, the eta=0 residue pieces are 1/(A h2) and -1/(B h2), each ~1/(x(x m^2 + P kappa)) at the soft end. So the integral of G grows like delta^-eps/eps as the cutoff delta goes to 0. At eps=0.1 it is 462.7, 1644.8, 4614.2 and 12073 for delta = 1e-4, 1e-8, 1e-12, 1e-16. C_C2's two pieces are each ~1/kappa at kappa->0, C_H has four such pieces, and the ladder's C_H = kappa0 h0 - kappa0 hhat has int kappa0 hhat ~ int dt/t, so all fail the same way. (b) If a single integrand with a numerator is used instead (lcpt.py allows e = -1; C_H = Dg/(t1 h1 t2 h2)), then |N_eta| >= |N_0| and the domination step fails. (c) (I1) is verified for no term. So Lemma 2.7 covers at most Gamma and C_S. The following are unproven as written: Thm 6.1's '(AR)+(ID) for all terms at N=1 (exact identification, Lemma 2.7)'; 'by Thm 2.6 and Lemma 2.7' in Thm 3.3 and X2a; and O11's 'checked: the (M2) one-loop graphs' (t6 identifies only Gamma of the ladder). The identification itself is TRUE for the triangle and elementary. Use int_0^oo dkappa kappa^-eps/((kappa+alpha)(kappa+beta)) = Gamma(eps)Gamma(1-eps)(alpha^-eps - beta^-eps)/(beta-alpha). The 0<x<P part of C_C1 then gives (pi/(Qt^2 sin pi eps)) (m^2)^-eps [B(-eps,1-eps) + 1/eps] and the x>P part gives -(pi/(Qt^2 sin pi eps)) (m^2)^-eps/eps, so int C_C1 = Gamma(eps)Gamma(-eps)Gamma(1-eps)(mu^2/m^2)^eps/(Gamma(1-2eps) Qt^2). C_C2 (x>0 part plus the sliver) and C_H (0<x<P plus x>P) work the same way, and C_S splits into two Beta integrals. I verified all four to 36-61 digits at (P,P',m^2,eps) = (0.8,1.3,0.1,0.3), (1/sqrt2,1/sqrt2,0.01,0.2) and (2.1,0.35,1e-3,0.07), in r2rev1/id_check2.py.

### [per_result 5]
X2-Lem2.8 + r1_lptools: CORRECT. The pieces I checked are all sound: strong duality is certified before the face-dimension bound (A_S^T y = c, y >= 0, and an exact primal with c.x = b.y), 2D recession cones are split into quadrants, psi_inf/|r|_1 is maximised at endpoints and tie points, and frozen variables enter as coefficients. Hand check of the archived certificate 'theta=2 (H2)_S C1' at eps=0. The rows are X_u - t1 <= 1, X_k - t1 <= 0, X_u - t2 <= 1, X_k - t2 <= 0, X_u <= -1, -X_u + X_k <= -1. The dual y0 = y2 = y4 = y5 = 1 gives A^T y = (2,1,-1,-1) = c and b.y = 0, so the value is -1 (lambda^2). The primal (-1,-2,-2,-2) is feasible with c.x = 0, rank 4 gives dim 0, and the maximum recession slope is -1/2: all as archived. At eps=1/10 the same LP gives -4/5 (lambda^8/5). The equivalence 'bounded argmax face <=> psi_inf < 0 on rec(U)\0' is correct. All 58 archived entries have status ok.

### [per_result 6]
X2-Lem2.10/Cor2.11 (LCPT positivity): CORRECT. V = 2l+1 and V = 2l+2 follow from the Euler and degree counts. Bound (b): minimising over spectator transverse momenta gives sum l_T^2/2l+ >= Q^2/2p+ (attained at k_T = -(1-xi) q_T for n=1), hence m^2 + Q^2(1-1/x). Rejecting the 1/xi variant was right: it holds only when spectators have zero k_T. Remark: Cor 2.11 has to cite the LCPT-covariant equivalence (Chang-Yan, Ligterink-Bakker) as an input with its hypotheses. Lemma 2.7 alone would be circular here, because for a single-signed density (I2) is exactly int|rho_Gamma| < oo.

### [per_result 7]
X2-Lem2.12: CORRECT, including the d=6-2eps form with c_eps = pi^-eps/Gamma(2-eps).

### [per_result 8]
X2-Prop3.1 (triangle densities): CORRECT. After the analytic kappa-integration the C_R densities reproduce the covariant DR values exactly (see Lem 2.7 above), and the t4 table normalisations (x P) check.

### [per_result 9]
X2-Prop3.2 (sliver): CORRECT. The kappa-integral is ln(a/(a-w))/(PP'w), and the w-integral gives Li2(1)/(2PP') = zeta2/Qt^2. I re-derived the sliver remainder num = -2(m^2(1+c/2P)w + Dg)w from rho_Gamma = 2w/(Dg D1) and rho_CC2 = 2w/(Dg h1).

### [per_result 10]
X2-Thm3.3: CORRECT for the fibered norms. The cells and constraints match the stated cover; the theta=2 and theta=1 logs and the 58 certificates are consistent. The eps0 exponents follow from the soft-cell scaling kappa^-eps ~ lambda^-4eps; for example (H2)_S C1 goes like lambda^(2-4eps), which is lambda^8/5 at eps0. GAP: the integrated corollary |I_Gamma - sum I_CR| <= C(lambda^2 L^2 + lambda^8/5) relies on Lemma 2.7, which does not apply to C_C1, C_C2 and C_H. Replace that step with the closed-form identification. Until then R_PT ('no unproven input') is not met for the integrated part.

### [per_result 11]
X2-Thm3.5/Prop3.6: CORRECT. A symbolic check gives sum of covariant C_R -> Lt^2 + pi^2/3 as eps->0. I re-derived the identity rho t = m^2 and the Q-unit expansion -4m^2/Q^4 + (m^4/Q^6)(L_Q^2 - 15 + pi^2/3).

### [per_result 12]
X2-Thm3.9 (bubble class, hybrid model): CORRECT within the stated model. I verified the single-shell structure. On the sliver (x<0), Dg, D1 and h1 are upper, D2 is lower and the ln Dg cut is upper, so Gamma^(j) and C_C2^(j) are both D2-residues with l_sl = ln[P'(a-w) + a kappa/w] > 0. For x>P, C_S and C_C1 sit on the E1 pole (shell e), C_C2 and C_H on the h1 pole (shell h), Gamma = 0, and the cut is in the lower half plane. I re-derived the rectangle rule and the |delta|, a, b bounds. The v2 eps0 runs give minimum exponent 1.6 for all 270+60 cells, and t15c is correctly disowned. Wording: 'each |T_s| <= lambda^8' on the corner should read int over the corner of |T_s| <= C lambda^8 L^k. The exact exponents (t15f) are lambda^8 for T_D and T_t, lambda^14 for T_e and lambda^16 for T_h.

### [per_result 13]
X2-Prop3.12 (one-loop DIS, M2): CORRECT. The graph list is complete at O(g^2): per channel a ladder, vertex-in, vertex-out and hard self-energy, plus 4 J-phi graphs and the t-channel graph. I re-derived: (1-T_H)R Gamma = S(P)[f(m^2) - f(0)] + [S(P) - S(Phat)][f(0) - f0]; v0 H0 - v H = -z m^2 (v0 + H); H, H0 >= z c_x; g(s) = (c-c0)^2/(pi^2 (a+c)(a+c0)^2); and T_H R = R T_H. The numerics do not depend on the cutoff. Minor, on (v): say that the forward amplitude is taken modulo x-independent terms, since the 1/t graph has no discontinuity in omega.

### [per_result 14]
X2-Thm3.13 (massive photon): CORRECT. I re-derived r = -M^2 g0/(G t1 h1 t2 h2), the vanishing kappa-integral, and the series -lambda^2(L+1) - lambda^4(L/2 + 1/4). The attribution is adequate.

### [per_result 15]
X2-Prop3.14: part (a) is CORRECT (Landau analysis; Gram determinant -16P^2P'^2(1-e^-4Y)^2). Parts (b) and (c) are WRONG as stated, because the singularity list is incomplete. With the stated i0's (h1Y and h2Y both -i0, as in t16 with sgn=-1), rho_CS has THREE real-base poles, not one. (i) x=0, from the h1Y-h2Y pinch in k-: rho ~ c/(x - i0) on both sides, with c = 1/(2PP'(M^2+kappa)(1-e^-4Y)). Numerically x*rho -> 90.9097 at M^2=1e-3, Y=3, kappa=0.01. The report's closed form shows the 1/x but drops its i0. (ii) For x<0, where rho_CS is nonzero (the contour closes downward on h2Y), a pole at -x0' + i0 with x0' = sqrt((M^2+kappa)e^-2Y/2), from G-h2Y. (iii) x0 - i0, from G-h1Y, as reported. At eta=1e-7 the poles sit at +5.9e-8 i (x=0), -2.4e-5 i (x0) and +4.7e-8 i (-x0'). Consequences: 'the only colliding pair is h1Y-G' is false. 'Removed by deforming x into Im x>0' fails globally: a valid contour passes below 0 and -x0' and above x0. It still deforms, so 'no 4D pinch' stands. The remedy 'integrate kappa first; only a weak branch point remains' fails at x=0, because int dkappa kappa^-eps c(kappa) is a nonzero constant and leaves a 1/x pole. The i0 assignment is also not Collins (10.68), which uses the same relative sign of i0 and k+ in both auxiliary denominators. With that choice (h2Y -> +i0) I find no pole at x=0, rho_CS = 0 for x<0, and both remaining poles (x0 and x0') at -i0. The numeric check 63.01377+142.80054i covers only [x0/2, 2x0]. Scripts: r2rev1/sl_check.py and sl_check_collins.py.

### [per_result 16]
X2-Thm4.1/Prop4.2: CORRECT. I verified the reference text of Lemma D.23(iii) ('这一包含关系对逐线下确界总成立') in factorization_qcd-2.pdf, and r1_abs_naive shows exactly the 4 failures.

### [per_result 17]
X2-Thm4.3 (two-loop exact remainder): CORRECT as graded. Part (i): r1_twoloop_exact finds 9 patterns with numeric eps-exponents {0,-1,-1,-2,-2,-2,-3,-3,-4}. In the other 40 the eps-coefficient depends on a free weight with D0 = 0, i.e. there is an m^2-independent rescaling with nonzero eps-weight, so these are scaleless. That step uses the standard DR linearity over analytically continued pieces, which should be stated. Parts (ii) and (iii) have explicit premises. From the UD formula Phi2(t,t) = -(6/lam)[Li4(-1/rho t) - Li4(-rho t)] with inversion, I re-derived the O(m^2) coefficient -(Lt^4/2 + pi^2 Lt^2 + 12 + 7pi^4/30), and the listed values and ratios check. 'NEW' should read 'new worked example': the overlap and zero-bin scalelessness mechanism is Manohar-Stewart PRD 76 (2007) 074002 and Idilbi-Mehen PRD 75 (2007) 114017 (with Jantzen 2011).

### [per_result 18]
X2-Num-2loop: correctly graded [P]. The error statements are now honest (pulls up to 2.4 sigma; the n16 under-coverage is acknowledged).

### [per_result 19]
X2-Lem5.2: CORRECT. The rung pole is upper iff k_(j-1)+ > k_j+, the spine and hard poles are lower, and I re-derived the propagated i0 weight k_(j-1)+/(k_(j-1)+ - k_j+) > 0. The invariant induction (Cauchy-Schwarz with weights z(1-xi) and 1-z) checks.

### [per_result 20]
X2-Lem5.3: CORRECT. (i) d >= z xi c_x. (ii) The S^3 average is 2/(dbar + sqrt(dbar^2 - 4|l|^2)) with dbar >= 1 - z + z xi c_x + |l|^2/(1-z). (iii) The derivative bound uses a^2 - b^2 >= a d_min. (iv) The bound is <= 2.

### [per_result 21]
X2-Prop5.1' (one-rung ladder): parts (a), (b) and (c) are CORRECT. I re-derived every inequality: the region-B bounds with coefficients 4/5 and 4; |k1 - k0| <= 2 delta/(pi^2 (1-z) v0'^3); h1 <= h0; the contributions from |k| <= c_x/4 and |k| > c_x/4; and the cover items 3c lambda(1-z)ln(1/z) and c(1-z)(lambda^2 + 4 sqrt(1-z) lambda). Part (d) has a minor GAP. The coefficient c1(x) = 4 int xi^(1/2)(1-xi)^(3/2)(1-xi/x)^-2 is right (my re-derivation gives (8/3pi)(3pi/2) = 4), but the proof that the angle-even remainder is o(lambda) is not written. Notational clash: in 'kappa^-eps <= 1 + kappa^-eps0', kappa means |k|^2, while the same symbol denotes the rung kernel. For eps > 0 the S^3 averages become S^(3-2eps) averages; say so.

### [per_result 22]
X2-Thm5.1: the downgrade to [P] is appropriate, and gaps g1-g5 are real.

### [per_result 23]
X2-Prop5.4: CORRECT.

### [per_result 24]
X2-Thm6.1: CORRECT as a conditional statement. The status list overstates (AR)+(ID) at N=1 (see Lem 2.7 above). The positioning omits the closest general-graph result: Ma, JHEP 05 (2020) 012 (arXiv:1910.11304). For arbitrary wide-angle massless amplitudes it builds a Collins-type forest formula of approximation operators, proves that 'all the singularities appearing in its subtraction terms cancel pairwise', and derives a factorized form. The report lists it only as a 'polytope and region method'. Also relevant: Erdogan-Sterman PRD 91 (2015) 065033 and Anastasiou-Sterman JHEP 07 (2019) 056. O1 and O10 should say what Ma's forest-formula result already covers (at the pinch-surface level, [A]-type rigour), and that X2's distinct contribution is integral-norm and power-suppression bounds.

### [per_result 25]
X2-Err: (a) is confirmed (I verified the text). (b), (c), (d), (f) and (g) are acceptable as relabelled. The withdrawal in (e) is correct, but the replacement analysis in Prop 3.14 is incomplete.

### [per_result 26]
Attributions. Verified verbatim in the open-access Collins text (scratchpad copy dl_collins/c10.txt): §10.7.3 'these commonly vanish after an integral over angle. Then the actual error is one power better: p = 2'; §10.6.6 'the requirement that the hard factor does not depend on the soft momenta'; the §10.5.6 rapidity divergence; and Theorems 1R, 2R, 3R and 4 in §10.7.5, proved in §10.7.6. I checked the bibliographic data on INSPIRE for Borinsky, Jantzen, Semenova-Smirnov-Smirnov, Gardi-Herzog-Jones-Ma-Schlenk, Ma 2024, Arkani-Hamed-Hillman-Mizera, Collins-Hautmann, Chiu-Jain-Neill-Rothstein PRL 108 151601, Becher-Neubert, Bergere-de Calan-Malbouisson, Curci-Furmanski-Petronzio, Chang-Yan, Ligterink-Bakker and Poldaru 2607.26291 ('Expansion by Regions Derivation from the Mellin Transform'). Missing: Ellis-Georgi-Machacek-Politzer-Ross NPB 152 (1979) 285, the origin of ladder mass-singularity factorization.

### [per_result 27]
Novelty. My INSPIRE searches found no LP or tropical certification of Collins' (CS1)-(CS3) and no fibered integral-norm verification. The searches were: tropical+factorization; tropical+asymptotic expansion; tropical+regions; fulltext 'Collins subtraction' with 'linear programming' or 'Newton polytope'; precise+subtraction+factorization. The narrowed NEW labels therefore stand, except for the Thm 4.3 mechanism and the Ma 2020 positioning.

## required_fixes

### [required_fixes 1]
PROCESS (blocking): the orchestrator or main session must write verify/extend/X2-subtraction/REPORT.md verbatim from row 96 of journal.jsonl (agent a3b63d44b69bba4fe), and persist the round-1 and round-2 reviews from their structured outputs. Later stages must receive these outputs directly, since subagents cannot write report files. review_r2_1.md was not written for this reason.

### [required_fixes 2]
(ID) at N=1: drop the claim that Lemma 2.7 yields (ID) for C_C1, C_C2 and C_H. Insert instead the closed-form identification: the kappa-integral formula, after which the x-integrals reduce to B(-eps,1-eps) + 1/eps, with the 1/eps cancelled by the x>P (or x>0) part. The script is r2rev1/id_check2.py, with agreement to 36-61 digits. Restrict Lemma 2.7 to pure-denominator products (e_j > 0) and note that (I2) generically fails for composite C_R; or prove a version with grouped residues and a dominating function for the group. State (I1) as verified or as assumed. Correct accordingly the 'Hence ... by Thm 2.6 and Lemma 2.7' of Thm 3.3, slot X2a, the status list of Thm 6.1, and O11: the ladder's C_R are not identified, and its C_H also violates (I2).

### [required_fixes 3]
Prop 3.14 (b),(c), SUMMARY item (1) and O8: list all three real-base poles of rho_CS for the stated i0's with their sides: x=0, c/(x - i0), from h1Y-h2Y; -x0' + i0, from G-h2Y, with rho_CS nonzero for x<0; and x0 - i0, from G-h1Y. Restore the i0 of the 1/x factor in the closed form. Delete 'the only colliding pair is h1Y-G'. Replace 'deform into Im x>0' with a contour passing below 0 and -x0' and above x0. Drop or correct the 'integrate kappa first' remedy, since the 1/x pole survives it. Correct the attribution 'as in Collins §10.6.4' for these i0's: Collins (10.68) uses the same relative sign of i0 and k+ in both factors, and with that choice the x=0 pole is absent and both remaining poles lie at -i0.

### [required_fixes 4]
Positioning: cite Ma, JHEP 05 (2020) 012 as forest-formula (Collins-type subtraction) prior art for general graphs in Thm 2.6, Thm 6.1 and O1, not as a polytope reference, and state what X2 adds (integral-norm and power-suppression bounds). Add Erdogan-Sterman PRD 91 (2015) 065033 and Anastasiou-Sterman JHEP 07 (2019) 056. For the Thm 4.3(i) mechanism, cite Manohar-Stewart PRD 76 (2007) 074002 and Idilbi-Mehen PRD 75 (2007) 114017, and relabel the result 'new worked example'. Cite Ellis-Georgi-Machacek-Politzer-Ross NPB 152 (1979) 285 alongside Curci-Furmanski-Petronzio 1980.

### [required_fixes 5]
Thm 2.6: remove the unused hypothesis that non-maximal U_R be UV-bounded and keep it as Remark (b), the reason (CS2) can be uniform in eps. Alternatively, restrict the sliver part of U_C2 to kappa <= s, so that the cover of Thm 3.3 satisfies the stated hypotheses.

### [required_fixes 6]
Prop 5.1'(d): add the short bound showing that the angle-even part of rho_r contributes O(lambda^2 L), so that the leading coefficient c1(x) is proven; otherwise grade (d) as numerically supported. Fix the kappa notation clash in the uniformity sentence, and state that S^(3-2eps) averages replace the S^3 averages for eps > 0.

### [required_fixes 7]
Minor wording: in Thm 3.9, write 'int over the corner of |T_s| <= C lambda^8 L^k' with the exact exponents 8, 14, 8, 16. In Prop 3.12(v), say the forward amplitude is taken modulo x-independent terms. In Cor 2.11, cite the LCPT-covariant equivalence theorem with its hypotheses rather than relying on Lemma 2.7, which would be circular there.
