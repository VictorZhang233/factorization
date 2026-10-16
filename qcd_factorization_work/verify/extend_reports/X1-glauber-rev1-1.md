# X1-glauber-rev1-1

(extracted verbatim from the workflow journal; structured output of the agent)

## overall

fixable_issues

## per_result

### [per_result 1]
RUN STATUS (re the relayed question 在正常运行吗: 在运行，但不完全正常). The workflow is running, but the file I was asked to review does not exist: verify/extend/X1-glauber/REPORT.md was never written. The harness refused the extender's Write of REPORT_part1.md with 'Subagents should return findings as text, not write report files'. The workflow journal shows the same happened for X2 and X3. The orchestrator's extend() neither saves the returned text nor checks that REPORT.md exists, so every round-1 reviewer is pointed at a missing file, and the round-1 fix agents will not be able to write REPORT.md either. I therefore reviewed two things: the extender's returned result (summary, 20 result blocks, 8 open items), recovered from the workflow journal (agent ad274be466e27b0fa), and the refused draft of §0–§3. The 'complete proofs in §§4–8', '§9 numerics', '§10 register' and '§12 novelty' that §0 refers to exist nowhere, so completeness could only be judged on the compressed proofs. For the same reason this review exists only here; I did not write review_r1_1.md, because report .md files are blocked for subagents. Scripts and logs of my independent checks are in verify/extend/X1-glauber/review_r1_1_scripts/ (*.py and logs/).

### [per_result 2]
L1 (joint localization, N insertions): CORRECT. Checked: sector selection; the residues (−i r_f for final insertions, +i r_b for initial ones); the weights w_σ = Πz/ΠK with Σw = 1; and absolute convergence by power counting (number of non-constant factors ≥ dim W + 1). Independent check: the report's quadrant formulas (its FA function) agree to 5.3e-14 relative, at 32 points (4 quadrants × 4 points × 2 colour orders), with my own exact iterated-residue evaluation of the COVARIANT jet function times exact propagators, using distinct finite iη and 40-digit mpmath (check_L3.py). Minor gap: in (b), M_σ = Σ_t|c_t| adds coefficients of terms with different numbers of states per gap, which have different dimensions; the bound should use Σ_t|c_t|λ_J^{Σ_ℓ(n_ℓ^t−1)}. Novelty: the N-order weight already appears in the reference (App. E.4.4, as an example) and in our ERR-S3. The exact sector formula with mixed half-planes and the error bound are new, so calling it 'sharpened' is fair.

### [per_result 3]
L2 (weights as functions of k^+): CORRECT. I re-derived the two-line formulas from L1(c): the weights are continuous with a kink across a single k_e^+ = 0 and discontinuous only at the origin. Physical caveat: the weights encode the external factors at |k^-| ~ |z_e| = a_e/(2|k_e^+|); see the T3 entry.

### [per_result 4]
T1 (commuting insertions to all orders): CORRECT but not new in substance. For commuting insertions 𝒥_σ = 𝒥(0) and Σw = 1, so the result reduces to the reference's line-by-line localization. The reference's Props E.35 and E.31(iii) already cover the abelian and non-coincident cases without E.33(c1). It is an alternative proof. The TMD claim is unverified (see the TMD entry).

### [per_result 5]
P1 (side-independent windows): CORRECT up to a definitional gap. x^A_min ('smallest plus momentum of a J_A line carrying SS momentum') depends on the side assignment whenever the amplitude-side and conjugate-side parts of J_A differ, so the side-independence of ν̂_A claimed in (a) fails as defined. Fix: take the minimum over all J_A lines on both sides that carry SS momentum under some side assignment. In (b), state the routing used (standard flow, each k_m crossing each state once, so that Σ_{l∈S}|K_l| ≤ Σ_m|k_Tm|), and use single-state bounds: |A_D| ≤ max(P^-, Σ_{l∈S}E(l)) and |A'_D| ≤ max(𝓔, Σ_{l∈S}E(l)), not sums over all lines. With these the factor 2 suffices. Window-edge terms disappear, but out-of-window parts still go to K_R (E.44(c)).

### [per_result 6]
L3 (quadrant formulas): CORRECT; independently verified (see the L1 entry).

### [per_result 7]
L4 (colour bookkeeping): (a) CORRECT (reference result; C3 checks). (b) CORRECT: I re-derived R = 2i c1c2 Im W12 [X1,X2] from the CTP colour ordering, assuming W12 + W21 = 1. (c) CORRECT. (d) WRONG as a statement about Drell–Yan. In DY the remnant colour state is a singlet of A-rem (in the irrep conjugate to A's active parton) times B-rem. Wigner–Eckart on the A side, the singlet condition and the identity f^{abc}T^a_{j1}T^b_{j2}(T^c_{j1}+T^c_{j2}) = 0 give ⟨ψ|[X1,X2]|ψ⟩ = −κ_i⟨ψ| i f^{abc}T^a_{j1}T^b_{j2} Σ_{k∈B-rem∖{j1,j2}}T^c_k|ψ⟩. This vanishes whenever the hadron containing j1 and j2 has no further remnant parton, however many spectators A has. Numerically (colour_dy.py, random DY states): ≤3e-17 when B-rem = {j1,j2}, for A-rem of 1, 2 (valence p p̄) or 3 partons; of order 0.1–0.3 when B-rem has 3 partons. The quoted 0.38 and 0.71 are maxima over four-parton singlets that cannot occur as DY remnants. The statement 'does not vanish when one hadron has ≥2 spectators and there are ≥4 in total' is false; valence p p̄ is a counterexample.

### [per_result 8]
L5 (complex rotation of the k^+ contour): CORRECT. The proof applies Stokes to the 3-chain swept in each quadrant; the 2-form vanishes on u_e = 0; the arcs vanish by the strip estimate; and NF_B is exactly what keeps J_B's final factors off the swept set. One slip: 'for t ∈ (0, π] no factor vanishes' is false at t = π, where A_D − e^{iπ}X = 0 at X = −A_D > 0. Only θ ≤ π/2 is used, so this is harmless. Independently confirmed: θ = π/2 and θ = π/4 give the same p_opp to 1e-8 at λ = 1 and to 1e-6 at λ = 0.01 and 0.001.

### [per_result 9]
L6 (ray identity): CORRECT (Cauchy's theorem on the quadrant). Independently verified for 8 random rational ρ, including poles on the positive axis, with |difference| < 2e-17 (check_L6.py). The identity is elementary; only its use as the T2 mechanism is new.

### [per_result 10]
T2 (fully coincident SS pair at O(g^4)): CORRECT AS A THEOREM ABOUT THE MODEL INTEGRAL, but with a HIDDEN HYPOTHESIS and OVERSTATED NOVELTY. I reproduced the numbers with my own quadrature (popp_indep2.py): Re p_opp = 0.012347, 0.002048, 0.000345 and 0.0000436 at λ = 0.01, 0.003, 0.001 and 0.0003 (report: 0.0123, 0.00205, 0.00035). The Im slope between λ = 0.001 and 0.0003 is −0.6366 = −2/π, and N/N0 → 1. (i) Hidden hypothesis: the integrand is taken to be J_A(k^-)ΠR_e(k)J_B(k^+) on all of R^4, i.e. Lemma E.19(a),(b) applied globally. Without a regulator, the −1/4 per rapidity end comes from |k^+| ~ a/λ_A = O(Q), where E.19(a) fails at relative O(1). The report itself uses exactly this argument to discard the end poles in T2'(b). The physical statement is therefore T2' (a smooth regulator inside the Glauber window) together with G7. (ii) Robustness, in favour of T2: Re p_opp is insensitive to O(1) changes of the A-side integrand at k^- ~ z. With a form factor Λ²/(k²+Λ²) at λ = 0.003, Re p_opp = 0.00205, 0.00204, 0.00203, 0.00203, 0.00212 and 0.00267 for Λ = ∞, 10, 1, 0.3, 0.1 and 0.03, while Im p_opp moves from −2.875 to −2.367. Re p_opp also → 0 for a Lorentzian k^+ regulator that is outside class 𝔛: 0.0453, 0.0177 and 0.0072 at λ = 0.01, 0.003 and 0.001. Class 𝔛 itself reproduces the report's 0.1029, 0.0542 and 0.0278. So the vanishing of the real part is robust; the O(1) imaginary constant c depends on the scheme. (iii) Novelty: the physical O(α_s²) cancellation for the fully coincident pattern was already shown by explicit two-loop calculations, by Lindsay, NPB 231 (1984) 397 (meson+meson, Feynman gauge, all graphs), and by Brandt–Frenkel–Taylor, NPB 312 (1989) 589 (eikonal mesons). The reggeization reading is textbook. What is new is the derivation for general LCOPT jets inside App. E's framework, the ray-identity mechanism and the regulator analysis. The claim 'refutes the reference / E.33(c2) not needed for this pattern' is too strong.

### [per_result 11]
T2' (analytic regulator and end-pole terms): CORRECT for the model. The regulated values are reproduced (class 𝔛, K_c = λ: 0.1029, 0.0542, 0.0278), and the end-pole formula is confirmed (apole set: 0.26257 at λ = 0.01 and 0.25204 at λ = 0.001, against 0.2517 predicted). Class 𝔛 is sufficient but not necessary, since a Lorentzian regulator also gives Re p_opp → 0. NF_X fails generically for QCD jets, and also for the model's alt set (α_2 = 0.518λ² > 0), so the regulated version is the relevant one. The symmetric version (O2) remains open.

### [per_result 12]
P2 (strict window): CORRECT; this is the reference's result (R8 K5). My Lorentzian test supports the diagnosis that the ½ comes from sharp, non-analytic truncation, but the diagnosis is an interpretation, not part of an [R] statement.

### [per_result 13]
P3 (on-shell lines unitary at O(g^4)): CORRECT and known (Cutkosky; for on-shell lines the crossed box has no s-channel cut). Note that the same argument applied to three on-shell lines (i; j1; j2) gives W12 + W21* = 1, from M + M† + M†M = 0 with only the physical three-particle cut; the Y graph drops out because it has no s-channel cut. That means the half-coincident residual vanishes for exact on-shell lines, the opposite of T3's model result (see the T3 entry).

### [per_result 14]
T3 (half-coincident pair): parts (a), (b) and (c) are CORRECT as statements about the model. Part (d): the model numbers are CORRECT. I reproduced W12 = 0.49788−0.03663i, 0.49980−0.03161i, 0.49999−0.03069i and 0.49999912−0.03058i at λ = 0.03, 0.01, 0.003 and 0.001, and −0.00003i in the symmetric configuration. But the PHYSICAL CONCLUSION is UNSUPPORTED, and part (e) is WRONG (see L4(d)). Reasons: (1) At leading power, Im W12 is entirely the A-side race weight integrated against J_B: the localized-limit value 0.5 − 0.030559i equals the λ → 0 limit. By L1(a), these weights are values of the external factors at k_e^- = z_e = a_e/(2k_e^+) ≈ 0.1 (units P^± = 1) for the dominant |k^+| ~ λ_B. There the connecting gluon is B-collinear (k^- is comparable to the B spectators' minus fractions, 0.3–0.35), and E.19(b) fails at O(1). (2) Sensitivity: a smooth A-side k^- form factor Λ²/(k²+Λ²) changes Im W12 from −0.03056 to −0.02418 (Λ = 0.3), −0.01634 (Λ = 0.1) and −0.00782 (Λ = 0.03), with Re W12 = ½ unchanged. (3) Scheme dependence: with a k^- rapidity regulator inside the Glauber window (Λ_- = λ, so that λ_A ≪ Λ_- ≪ z), Im W12 = −0.0065, −0.0019 and −0.00065 at λ = 0.01, 0.003 and 0.001, i.e. power suppressed. In the same scheme the fully coincident Re p_opp → 0 as well (0.028, 0.010, 0.0039). In the strict window W12 = ½. So with smooth regulators on both ends, both coincident O(g^4) patterns cancel inside the window, and T3's residual sits in the B-collinear complement. That is a matching question of G7 type at the k^- end. (4) Exact unitarity forbids the residual for on-shell lines (see the P3 entry). Hence the following are not established: the [V] grade; 'an E.33(c2)-type compensation … genuinely needed already at O(g^4)'; the three-gluon-colour compensation claim; and REG's G5(i).

### [per_result 15]
P4 (per-graph weak equivalence fails): CORRECT for the model; it is in fact the report's own evidence that per-graph weights are fixed at the collinear ends. As an [R] statement, 'data local to the window' needs a precise definition, for example {𝒥_σ, a_e, k_T, λ_{A,B}}, because the base and apole sets differ in A's energies (d0, d10, the α's).

### [per_result 16]
P5 (O(g^6)): acceptable at grade [A]. The 'line part' of the Lipatov vertex is textbook and should be cited. The conclusion concerns whether 𝒢₀ is closed under unitarity, not a failure of factorization.

### [per_result 17]
L7 (E.33(a) on the far-off-shell set): CORRECT at fixed S-loop momenta (an elementary estimate of the affine zero). The reduction of E.33(a) has gaps: (1) L1 is proved only for single-pole external factors, but L7's factors have several poles, so the multi-pole generalization (a sum over pole choices) must be stated. (2) E.33(a) concerns R_j after S's loops are integrated; R_j then has cuts, and the half-plane decomposition R_↓ + R_↑ with bounds is required. (3) Interchanging the k_j^- fibre integration with the S-loop integration is not justified near the exceptional set. L7 should be presented as a pre-integration lemma.

### [per_result 18]
P6 (obstruction for coincident SA/AS insertions and H-emission endpoints): a plausible analysis, but OVERGRADED. No precise theorem is stated; 'a half-line deformation does not cure it' is an argument. It should be graded [A] or presented as a remark. It also inherits the end-dependence of the weights (see the T3 entry).

### [per_result 19]
REG (assumption register): needs revision. G5(i) (half-coincident patterns from O(g^4)) is not established (see T3). 'Not needed for fully coincident pairs' must be made conditional on G7 and on a smooth, non-sharp rapidity regulator. G7 must be two-sided: the k^+ end for the B-side weights and the end poles, and the k^- end for the A-side weights. With in-window regulators on both ends, the model shows no in-window O(g^4) coincident residual for either pattern.

### [per_result 20]
EX and verification logs: the numerics are CORRECT. My independent third quadrature reproduces methods I and II; at λ = 1 it gives 0.3740971311−0.2694186095i against the report's 0.374097135−0.269418606i. The log reporting, however, is INACCURATE. checks_C2_C3_C4.log ends with 'SOME CHECK FAILED' (C3e and C3f), and check_halfcoinc_singlets.log crashed with a LAPACK error before the (8,8,8,8) and (3̄,8,8,3) cases, yet the summary says all checks pass. The failing C3e/C3f formula is called 'deliberately mis-specified', but the header of halfcoinc.py shows it was the extender's original, wrong prediction ('Thm T5': Re W12 → ½, hence cancellation). The failure of the naive polar grid is documented correctly.

### [per_result 21]
TMD version: NOT TREATED, which is a gap relative to the task. It is only asserted (O7: the results 'carry over verbatim'). Before any TMD statement is graded, at least the following must be checked: how the SS rapidity regulator χ(k^+) and G7 interact with the TMD rapidity regulator and CS evolution; the soft-scale windows of E.19(e); and the staple direction.

### [per_result 22]
Novelty and literature: the report says its search was limited, and directly relevant work is missing. Missing: Lindsay, NPB 231 (1984) 397 (meson+meson at two loops); Lindsay–Ross–Sachrajda, NPB 222 (1983) 189 (quark + meson or baryon, colour-singlet requirement); Brandt, ZPC 45 (1989) 287; Nelson, NPB 223 (1983) 366; Bodwin–Brodsky–Lepage, PRL 47 (1981) 1799 (the original claim of non-cancellation); and Sterman–Erdoğan, coordinate-space LCOPT (arXiv:2502.14230, EPJ ST 235 (2026) 1493). The descriptions of LRS PLB 117 (1982) 105 and NPB 214 (1983) 61 (one side has no spectators) and of BFT NPB 312 (1989) 589 (eikonal mesons with one spectator each) are correct. Liu–Ma arXiv:0802.2973 exists (an unpublished SCET argument). I found no paper stating T3's model result or the LCOPT ray-identity proof of T2, so both are new as statements about the framework.

## required_fixes

### [required_fixes 1]
PROCESS (orchestrator): REPORT.md must be written by the parent session, because subagents are not allowed to write report .md files. Steps: (1) write verify/extend/X1-glauber/REPORT.md from the extender's returned result (workflow journal, agent ad274be466e27b0fa); (2) write the full sections that do not exist anywhere (§§4–12: complete proofs, numerics, register, novelty); (3) save the round-1 reviews from the structured outputs; (4) add a check in extend() that REPORT.md exists, saving the returned text if it does not. X2 and X3 need the same treatment.

### [required_fixes 2]
State as an explicit, numbered hypothesis of T2, T2', T3 and P4, and of the physical reading of L2 and P6, that the integrand is J_A(k^-)ΠR_e(k)J_B(k^+) on all of R^4 (E.19(a),(b) applied globally). Add the remark that the ordering weights of L1(c) are generated where the connecting gluon is near shell (k_e^- = z_e). That is k^- ~ a/|k^+| = O(Q) for |k^+| ~ λ_B, where the gluon is B-collinear and E.19(b) is invalid; symmetrically, the B-side weights are generated where the gluon is A-collinear and E.19(a) is invalid. Grade every physical conclusion accordingly.

### [required_fixes 3]
T3: withdraw the [V] grade, the claim that an E.33(c2)-type compensation with three-gluon colour is 'genuinely needed already at O(g^4)', and the matching statements in the executive summary and REG. Restate T3 as a model result: in App. E's framework (global E.19 jets, exact propagators, no k^- regulator) the half-coincident family leaves 2ic1c2 Im W12 [X1,X2] with Im W12 = O(1). Say also that Im W12 is generated at the B-collinear end (k^- ~ z); that it depends on the regulator (power suppressed with an in-window k^- regulator: −0.0065, −0.0019, −0.00065 at λ = 0.01, 0.003, 0.001; zero in the strict window); that the unitarity argument of P3 forbids it for exact on-shell lines; and that its fate in QCD is an open, two-sided-G7 matching question. Keep (a), (b) and (c) as [R] statements about the model.

### [required_fixes 4]
L4(d) and T3(e): replace the colour condition with the correct DY statement. The residual's colour factor is −κ_i⟨ψ| i f^{abc}T^a_{j1}T^b_{j2}Σ_{k∈B-rem∖{j1,j2}}T^c_k|ψ⟩, which vanishes unless the hadron containing j1 and j2 has at least one further remnant parton; for example it is zero for valence p p̄ → DY. Include the proof (Wigner–Eckart, the singlet condition, and f^{abc}T^a_{j1}T^b_{j2}(T^c_{j1}+T^c_{j2}) = 0). Delete the 0.38 and 0.71 'maximal singlet-space' numbers or label them as non-DY states, and fix and re-run the singlet check that crashed.

### [required_fixes 5]
T2 and T2': cite Lindsay NPB 231 (1984) 397 and Brandt–Frenkel–Taylor NPB 312 (1989) 589 (and LRS NPB 222 (1983) 189) as earlier two-loop demonstrations of the cancellation. Restrict 'new' to the general-LCOPT-jet derivation inside App. E, the ray-identity mechanism and the regulator analysis. Replace 'refutes the reference … E.33(c2) not needed for this pattern at O(g^4)' with: 'within App. E's framework Re p_opp → 0 inside the window for smooth rapidity regulators; the strict-window ½ is an artefact of sharp truncation; the full statement requires G7'. State that Re p_opp → 0 is robust (it survives A-side k^- form factors and a Lorentzian k^+ regulator), that the O(1) imaginary constant c depends on the scheme, and that class 𝔛 is sufficient but not necessary.

### [required_fixes 6]
REG: delete G5(i). Make G7 two-sided (both rapidity ends), and make the 'not needed' statements conditional on G7 and on smooth regulators. Record that with in-window regulators on both ends the model has no in-window O(g^4) coincident residual for either pattern.

### [required_fixes 7]
L1(b): fix the dimensionally inhomogeneous constant M_σ by normalizing the coefficients of multi-state gaps with powers of λ_J.

### [required_fixes 8]
L5: replace 't ∈ (0, π]' with 't ∈ (0, π)', since the initial factors vanish at t = π.

### [required_fixes 9]
P1: define x^A_min independently of the side assignment, as the minimum over all J_A lines on both sides that can carry SS momentum. State the transverse routing that is used, and use the single-state bounds |A_D| ≤ max(P^-, Σ_{l∈S}E(l)) and |A'_D| ≤ max(𝓔, Σ_{l∈S}E(l)).

### [required_fixes 10]
L7: state and prove the multi-pole generalization of L1 that L7 relies on. Distinguish the pre-integration statement from E.33(a), which concerns R_j after the S-loop integration (with cuts and the R_↓ + R_↑ decomposition). Either justify interchanging the k_j^- fibre integration with the S-loop integration or drop that step.

### [required_fixes 11]
P6: downgrade from [R] to [A], or formulate a precise theorem. P4: give a precise definition of 'data local to the window'.

### [required_fixes 12]
Verification logs: re-run or remove the obsolete C3e/C3f checks so that checks_C2_C3_C4.log passes. Replace 'deliberately mis-specified' with an accurate account: the original prediction (Re W12 → ½, hence cancellation) was wrong and was later corrected. Report the crash of the singlet check instead of claiming that all checks pass.

### [required_fixes 13]
TMD: either carry out the TMD transcription (the interplay of the SS rapidity regulator with the TMD rapidity regulator and CS evolution, the windows of E.19(e), the staple direction), or remove 'and its TMD version' from the claimed results, or grade it [C].

### [required_fixes 14]
Literature: add Lindsay 1984, LRS NPB 222 (1983), Brandt ZPC 45 (1989), Nelson NPB 223 (1983), Bodwin–Brodsky–Lepage PRL 47 (1981) and Sterman–Erdoğan arXiv:2502.14230. Re-check the novelty markers after reading CSS 1988, Collins 2011 §14.4 and DGOPS 2016 §4 (open item O8).

### [required_fixes 15]
NF hypotheses: state that NF_X fails generically for QCD jets, and also for the model's alt set, so the unregulated T2 is a special case. Make T2' (with its mirror; the symmetric version O2 is open) the main statement.
