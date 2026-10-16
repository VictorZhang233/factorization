# X2-subtraction-rev1-1

(extracted verbatim from the workflow journal; structured output of the agent)

## overall

fixable_issues

## per_result

### [per_result 1]
PROCESS — answer to the relayed question 在正常运行吗: 不完全正常 (not fully). The X2 computations ran and finished: 41 scripts and logs, 17:46–19:54 local, and the agent returned at about 19:58. But verify/extend/X2-subtraction/REPORT.md does NOT exist. The harness refused the subagent's Write ('subagents should return findings as text'), and X1 hit the same refusal. The full report text survives only as the agent's structured result: the journal row with agentId ad47b382e8e1e17ed in ~/.claude/projects/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/subagents/workflows/wf_52f29317-58b/journal.jsonl, containing a summary, 21 results and 10 open items. The workflow nonetheless launched reviewers on the missing file. I reviewed those 21 results and 10 open items, read all scripts and logs, and re-derived the key steps independently (scratch scripts in the session scratchpad, x2rev/c1–c7). For the same policy reason this review is returned only here; review_r1_1.md was NOT written. The orchestrator must write REPORT.md verbatim from results/open and persist this review. Otherwise the fix round ('fix every valid issue in REPORT.md') has no file to fix, and later reviewers will again find nothing.

### [per_result 2]
R1 [X2-Thm2.6, fibered subtraction theorem] — CORRECT as an implication, with OVERSTATEMENTS. Correct: the proof is the triangle inequality on a finite cover plus linearity of the residue map, and identity (D.10) holds fiberwise. (i) 'The 4D contour assumption (A1) disappears' is overstated. (A1)(a) is replaced by an analytic input that must be stated and proved. Every approximated integrand needs the k⁻-residue representation: decay ≤ −2 in each k_i⁻ uniformly, including near k_i⁺ = 0, and no zero-mode/δ(k⁺) contributions. Eikonal factors such as h2 = 2P'k⁺ carry no k⁻ dependence, so the Chang–Yan and Ligterink–Bakker LCPT derivations, which are for full Feynman graphs, do not automatically cover C_R terms. The fibered iterated value of ∫C_R must also equal the DR value used to define the factors; for the triangle this was checked only numerically, by R6. (A1)(b) is still needed for Prop D.16, as R18 itself says. (ii) Caveat (a), that (H3) fails on the real contour, is true but is not an App. D error: Def D.2 and Ass. D.7(A1) explicitly put Ω on a complex deformation. (iii) Caveat (b) is CONFIRMED and is a genuine sharpening. I re-derived ∫_{U_C1∩{k⁺>P}}|ρ_CC2| = ∫_P^∞dx∫_0^{2sx}dκ κ^{−ε}/(Pe2(e2+κ)) ≈ s^{1−ε}P^{−ε}/ε, so the U_R of Def D.5, which are unbounded in their large components, violate ε-uniform (H2). (iv) Caveat (c), first-order vs second-order norms after angular averaging, is stated in Collins 2011 §10.7.3: 'these commonly vanish after an integral over angle. Then the actual error is one power better: p = 2'. It must be attributed, not presented as new. (v) 'The Glauber region never appears' holds only where single-graph fibered densities are integrable (spacelike Sudakov, DIS at x>1); the theorem statement must carry this scope (cf. O7).

### [per_result 3]
R2 [X2-Lem2.8, tropical/LP certificate lemma] — CORRECT. I verified the citation in the arXiv:2008.12310 PDF: Theorem 8.A gives |p| ≤ C p^tr with C = Σ|c_ℓ|, and Theorem 8.B gives the lower bound, trivial for positive coefficients with C = min c_ℓ. The LP plus Hoffman plus recession logic is sound, and the exact dual reconstruction is valid weak duality. The face-dimension bound via complementary slackness needs the exact dual to be OPTIMAL; exact_verify returns the float optimum but never asserts bᵀy = optimum, and it should. ε-uniformity: ψ_a is affine in ε, so the LP value is convex and the endpoints suffice. The X2 run checked ε0 = 1/10 only on the θ=1 cover. I ran the θ=2 cover items at ε0 = 0.1 with the project LP and got worst exponent λ^1.6 = λ^{2−4ε0}, so the claim holds; an exact run should be added. Caveat: the scripts substitute frozen O(1) variables into NUMERATORS before taking |coefficients|. This is harmless in every instance here (numerators are monomials or single-signed, e.g. region III: N = m², −1, 1; sliver: all monomials negative), but the lemma's implementation should bound |p(u)| ≤ Σ|c_j|2^j instead. The report must list, per cell, the comparability of each denominator with its positive form: freezing u or v ∈ [1/2,1] costs at most a factor 2, plus the sign-definite rewriting of factors like −(P²κ+m²x(P−x)).

### [per_result 4]
R3 [X2-Lem2.10/Cor2.11, light-cone positivity] — CORRECT. I checked that cubic graphs have V = 2L+1 vertices for the vertex (2L intermediate states) and V = 2L+2 for DIS (2L+1 states), the same for every ordering. In spacelike/unphysical kinematics every energy denominator is negative. For DIS, Σl_T²/2l⁺ ≥ q_T²/2p⁺ gives p⁻+q⁻−Σ ≤ −(m²+Q²(1−1/x))/2p⁺ < 0. The two-loop numerics in t9 show a single sign. Scope must stay 'UV-finite graphs, spacelike/unphysical kinematics, scalar model'. Novelty is modest: negativity of LCPT denominators below threshold is classical, while its use for (H3^φ) is new.

### [per_result 5]
R4 [X2-Lem2.12, 1D rung-kernel reduction] — CORRECT. Re-derived: l = k−zK, d⁴l = π²|l|²d|l|², |l|² = (1−z)(t−zv), so ∫d⁴kκF = (1−z)∫_{zv}^∞(t−zv)F(t)/t²dt ≤ (1−z)∫F/t.

### [per_result 6]
R5 [X2-Prop3.1, triangle fibered densities] — CORRECT. The densities match the t1 symbolic and numeric checks. I re-derived the normalisation μ^{2ε}∫d^dk/(iπ^{d/2}) = (μ^{2ε}/Γ(1−ε))∫dx dκ κ^{−ε}ρ and the sliver form ρ_CC2 = w/(P[(a−w)P'w+aκ](P'w+κ)). (H3^φ) for 0<ε<1 agrees with App. D Ex. D.47.

### [per_result 7]
R6 [X2-Prop3.2, negative-k⁺ sliver] — CORRECT at ε = 0. Re-derived: ∫dκ ρ_CC2 = ln(a/(a−w))/(PP'w), and ∫_0^a(dw/2)(…) = Li₂(1)/(2PP') = ζ₂/Q̃². Add 'at ε=0' (the κ^{−ε} weight changes this) and note that the statement is fibration/routing dependent. '−2m²/Q̃⁴ of the remainder' is consistent with t2b (−2.000λ²).

### [per_result 8]
R7 [X2-Thm3.3, triangle Collins conditions at the sharp exponent] — CORRECT as a fibered-norm statement, with qualifications. (a) s = λ² is indeed the natural (ultrasoft) scale of the off-shell form factor (∫C_S ∝ (μ²Q̃²/m⁴)^ε). (b) Missing evidence: ε-uniformity on THIS cover. I supplied it: θ=2 at ε0 = 0.1 gives worst λ^1.6. (c) The lower bound is correct: ∫_{U_S}ρ_CC1 ≥ s·min(s,m²)/(4m²) = s/4 for θ ≤ 2; my numerics give A/s → 1 for θ<2 and 1/2 at θ=2. But '(H1)_C1 norm = (θ/2)sL' holds only for θ<2 (0.25, 0.50, 0.75 sL at θ = 0.5, 1, 1.5); at θ=2 it is ≈1.44 sL. (d) At θ=2 the whole interior of the Sudakov diamond (e.g. k~λ) lies in U_H, so the (H1)_H item is the global remainder certificate. The verification is valid, but the cover adds nothing beyond the direct r-bound, and this should be said. (e) The 'correction of App. D Lesson (d)/Def D.5' is a sharpening, not an error correction. The constraints 0<β<1 and β_S<β_C are sufficient-condition choices for Lemma D.25. X2 shows they are unnecessary for the triangle and that they cost powers; 'harmful' is overstated. (f) The L-power is rigorously L^{≤2} from the exact face bound; the float LP gives L^0–L^1.

### [per_result 9]
R8 [X2-Thm3.5/Prop3.6, norm vs integral] — CORRECT. An independent integrator reproduces the norm to all printed digits: 35.83841, 54.52888, 72.98858·m² at λ² = 10⁻⁴, 10⁻⁶, 10⁻⁸. Extending to 91.41525·m² at 10⁻¹⁰ gives ∫|ρ_r| = λ²(4L̃ − c) with c → 0.688. The NNLP formula checks numerically: m² = 10⁻⁴ gives −3.99109·10⁻⁴. My exact NLP from UD is ∫r = −4λ² + O(λ⁴L̃²). The Table 5 remark is correct: it tests the LP of the exact integral in Q, not the Collins remainder in Q̃.

### [per_result 10]
R9 [X2-Thm3.9, bubble-chain class] — LARGELY CORRECT, with GAPS. I verified the four-shell representation, i.e. that the k⁻ contour closes away from the ln D_g cut in every x-range. For 0<x<P it closes upward on the line-1 shell; for x>P only the e and h shells contribute; on the sliver it closes downward on the D2 pole, with the cut in the upper half plane. The rectangle-rule algebra (δ = ln((κ+um²v)/(κ+um²)), |δ| ≤ u²m²/(um²v+κ)) and every log-difference weight W(a,b) of t17 are also correct. Gaps: (a) the sliver is NOT certified for j ≥ 1 (t15, t15b and t17y omit it; only t5 numerics), and it is needed for the remainder and for (H1)_C2 on U_C2. (b) The U_C1 part III items (1<u<2) are missing for j ≥ 1 in t17/t17y. They are easy, since only the e and h shells contribute and they are m²-suppressed. (c) '(H3) as for the triangle' needs a stated hybrid scheme (d-dimensional outer loop with a fixed 4D ln^j insertion); the true d=4−2ε renormalized chain is not ln^j. (d) C_j grows FACTORIALLY. On the u>1 part alone, norm/(m² j!) → ≈2.0 for j = 8, 10, 12 at m² = 10⁻², while norm/(m²L^{j+2}) grows, so C_j ≳ 2 j!/L0^{j+2} from the UV tail ∫ln^jκ/κ². No statement about the summed chain is possible (renormalon); say so. (e) Lemma 3.7 needs a written argument that no region with bubble lines in a different mode is leading (the massless bubble's only singularity is at k²=0) and that Ass. D.41 is used for the renormalized insertion.

### [per_result 11]
R10 [X2-Prop3.12, all one-loop DIS graphs in φ³₆] — PART (i) CORRECT, PART (ii) WRONG as stated. (i) For the ladder I derived the leading full-norm coefficient analytically: 4∫₀¹dξ(1−ξ)^{3/2}ξ^{1/2}/(1−ξ/x)² = 1.26298 at x=2, using ⟨|cosθ|⟩_{S³} = 4/3π and ∫₀^∞(2y+1)y^{−1/2}(1+y)^{−2}dy = 3π/2. This matches the numerics converging to 1.2633. (ii) In φ³₆ the one-loop vertex corrections (3 propagators, degree 6−6 = 0) and the hard-line self-energy (degree 2) are UV DIVERGENT. So '(H3) trivial' is false (Γ ∉ L¹ uniformly in ε). For the self-energy, (1−T_H)Γ is itself divergent: the mass term gives AΛ²[1/(s−m²)² − 1/s²] ∝ m²Λ², and the wave-function term gives Σ(s−m²) − Σ(s) ≈ −m²Σ'(s), which is log divergent. Integrand-level BPHZ renormalization is required (Ass. D.41; unproblematic in scalar φ³₆), together with a proof that T_H commutes with it; then (H1)_H must be redone. The model's current vertex and the full list of one-loop graphs must also be stated.

### [per_result 12]
R11 [X2-Thm3.13, massive photon with light-like approximators] — CORRECT. Re-derived: the κ-integral of the 0<u<1 bracket vanishes identically, and ∫r = −M²∫₁^∞du ln(u/M²)/(u(u−M²)) = −λ²(L+1) − λ⁴(L/2+1/4) + …, consistent with expanding Jantzen's closed form. Per the data the norm is ≈ λ²(3.0L − 0.85), i.e. O(λ²L). The (H3) failure from rapidity divergence of light-like Wilson lines is KNOWN (Collins 2011 §10.5.4 and §10.6.4; Collins–Hautmann hep-ph/9908467). Only the explicit remainder formula is new. The Jantzen offset of 1.68·10⁻⁴, constant in M², is a κ-cutoff tail and harmless.

### [per_result 13]
R12 [X2-Prop3.14, time-like vs space-like regulators] — TIME-LIKE PART CORRECT [P]; SPACE-LIKE PART WRONG. The time-like part is consistent with Collins §10.6.4: time-like vectors may be used if universality is given up. For the space-like part, the collision of the eikonal and gluon poles in the k⁻ plane at 2e^{−2Y}(k⁺)² = M²+κ is NOT a pinch of the 4D integral. Landau equations: −2α_G k + α₁n₁ = 0 forces k ∝ n₁, hence k² ∝ n₁² < 0, contradicting G=0 (k² = M² > 0). Adding n₂ forces (α₁,α₂) into the kernel of the non-degenerate Gram matrix, so k=0 and G = M² ≠ 0. There is no Landau singularity. The fibered density has a simple pole with definite i0 at x₀ = √((M²+κ)/2e), just below the real k⁺ axis. It is integrable as a distribution and is removed by deforming k⁺ upward; the upper/lower classification of the k⁻ poles is stable under that deformation. What fails is absolute integrability on the REAL fibered base, a limitation of the real-base (H3^φ), not (H3) in App. D's sense. Collins 2011 §10.6.4 uses exactly such space-like n₁,n₂, with the same i0 as X2's t16 (pole of −n₁·k+i0 above the axis, gluon pole below), so the claim would wrongly impugn the textbook virtual soft factor. 'Extends erratum E1' is also wrong: E1 is about real emission, where cut lines cannot be deformed. Drop the grade '[R] (pinch analysis)'.

### [per_result 14]
R13 [X2-Thm4.1/Prop4.2, two-loop algebra and the (Abs) counterexample] — CORRECT, independently confirmed. I re-derived by hand the zeroing sets of the literal App. D convention: HS a2 {k2−,k2T,M}, HS b2 {k2+,k2T,M}, C1S b2 {k1−,k1T,k2+,k2T,M}, C2S a2 {k1+,k1T,k2−,k2T,M}. Rechecking (Abs) on all 9 incomparable pairs gives exactly 4 failures: (C1C1,HS) and (C1C1,C2S) on a2 [k2+], and (C2C2,HS) and (C2C2,C1S) on b2 [k2−]. With soft-first there are 0. Wording: 'soft-first is necessary' should read 'soft-first is sufficient; the literal convention fails'. Cite R6 E5, a different edge case of the same Lemma D.23(iii).

### [per_result 15]
R14 [X2-Num-2loop] — NUMERICS CONSISTENT, STATED ASYMPTOTICS WRONG. Each zeroing pattern is exactly homogeneous under its region scaling (e.g. T_{C1S}Γ ∝ (m²)^{−3ε}), so Σ_R∫C_R is exactly the LP polynomial in L̃ = ln(Q̃²/m²). Hence ∫r = Φ^(2)(t,t)/Q⁴ − [L̃⁴/4 + π²L̃²/2 + 7π⁴/60]. This predicts −7.0507, −4.5967, −2.5705, −1.2817 at m² = 0.04, 0.01, 0.0025, 6.25·10⁻⁴. The X2 QMC values are −7.036±0.22, −4.593±0.08, −2.386±0.24, −1.319±0.084, all within 1σ, which confirms the 50-pattern implementation. But the series is ∫r = −λ²(L̃⁴/2 + π²L̃² + 12 + 7π⁴/30) + O(λ⁴L̃⁴): ∫r/(m²L̃³) runs −5.29, −4.71, −4.78, −5.11, −5.72, −7.64, −9.75 down to m² = 10⁻⁸. So '∫r ~ −4.7m²L³' is a pre-asymptotic fit (in the fitted window m²L⁴ is nearly flat). Because the averaged norm ≥ |∫r|, 'averaged norm ~ m²L^{2.6–3}' is also asymptotically wrong: it is ≥ ½λ²L̃⁴(1+o(1)). The QMC error bars are unreliable: the n16 and n18 runs differ by up to 4σ at m² = 6.25·10⁻⁴ (−1.78±0.11 vs −1.32±0.08), and n16 ∫Γ is off by 2.5σ. 'Full norm ~31λL' is plausible as [P] (cf. Collins §10.7.3).

### [per_result 16]
R15 [X2-Lem5.2, DIS ladder representation] — CORRECT as far as checked. The invariant v ≥ ξm² + |K|²/(1−ξ) propagates by Cauchy–Schwarz: |l+zK|²/(1−zξ) ≤ |l|²/(1−z) + z|K|²/(1−ξ), with weights (1−z) and z(1−ξ) summing to 1−zξ. The product/difference structure is correct because the approximators act on distinct factors. The pole-side induction for ordered k⁺ should be written out in the report.

### [per_result 17]
R16 [X2-Thm5.1, DIS ladders of every length n] — GAP: graded [R] but only OUTLINED. (P1), (P2) and the case split (A) |k|² ≥ 64v / (B), with constants 3 and 19, must be written in full and checked. Lemma 5.3 is supported only by random sampling (t19), but it is provable in a few lines, and I checked the steps. With the invariant, d ≥ A+v'−2|k| ≥ 1 − zξ/x + |k|²/(1−zξ) − 2|k| ≥ zξ(1−1/x). Then ⟨1/d⟩_{S³} = 2/(d̄+√(d̄²−4|l|²)) ≤ 2/d̄, with d̄ ≥ 1−z+zξ(1−1/x) after minimizing zv + 2zK·q under v ≥ |K|²/(1−ξ). ε-uniformity of the items, which Thm 2.6 needs together with (H3) at ε>0, is not shown; all bounds are at ε=0. Until the complete proof exists the grade should be [P] (n=1 analytic, confirmed by my 1.26298λ; n=2 numerical) or [R]-pending.

### [per_result 18]
R17 [X2-Prop5.4, two-element chains] — CORRECT (C_A = H(πk)J, C_H = T_H[(H−H(πk))J] = ΔH·J̃, r = ΔH·ΔJ).

### [per_result 19]
R18 [X2-Thm6.1, all-orders conditional theorem] — CORRECT as a conditional statement (Thm 2.6 summed over graphs). The status table needs edits. 'Admissibility of all Collins terms (decay per graph)' is listed as VERIFIED at all orders, but no general proof is given: zeroing can reduce the number of k⁻-dependent factors per loop, and eikonal factors raise k⁺=0 zero-mode questions. Prove it, or list it as checked only for N ≤ 2 patterns. The bubble class 'at all N' must carry the factorial C_j and the hybrid regularization (R9). Goal (ii), 'all two-loop graphs', is not met: the crossed two-loop vertex and the subdivergent graphs are absent (O3).

### [per_result 20]
R19 [X2-Err, corrections to App. D] — (a) CONFIRMED (see R13). (b) A sharpening, not an error correction; rephrase as in R7(e). (c) Not an App. D error, since App. D uses a deformed Ω; rephrase as a remark. (d) CONFIRMED and valuable: non-maximal U_R must be UV-bounded, and I re-derived the s/ε scaling. (e) WRONG (see R12). (f) CONFIRMED: norm ≈ 4λ²L, and the sliver ζ₂ statement holds at ε=0. (g) Correct.

### [per_result 21]
R20 [X2-Err-own, retraction] — CORRECT, and consistent with my independent re-analysis of t18. B(θ) = ∫_{U_C1}|ρ_G−ρ_S−ρ_C1| ≈ (θ/2)sL for θ<2, never λ²L/s, so the t18 docstring's 'exponent 1 is optimal' is false. Make sure that docstring is never quoted.

### [per_result 22]
R21 [X2-Est, explicit error estimates] — The one-loop entries are CORRECT. The bubble entries must add 'C_j grows ~j!'. The DIS-ladder entries must carry the R16 grade. The two-loop entries 'signed ~ −4.7m²L³' and 'averaged ~ m²L^{2.6–3}' are WRONG asymptotically; replace them with the exact NLP formula −λ²(L̃⁴/2+π²L̃²+12+7π⁴/30) and the lower bound ½λ²L̃⁴ on the averaged norm.

### [per_result 23]
SUMMARY-level claims and OPEN items. Summary (1) see R1; (5) '[R] ladders, all n' see R16; (6) '[R] all one-loop DIS graphs' see R10; (7) 'space-like regulators pinch' see R12; (8) '∫r ~ −4.7m²L³' see R14. O1–O7, O9 and O10 are reasonable. O8 must be rewritten: the third option is a complex deformation of the base k⁺, and there is no pinch. Missing from the open list: zero-mode-free LCPT for approximated integrands; BPHZ for the φ³₆ vertex and self-energy graphs; factorial growth of C_j. All results are scalar-model statements (φ³₄-type vertex, φ³₆ DIS) and must not be presented as QCD results (O2). NOVELTY: I found no prior LP/tropical certification of Collins' conditions in INSPIRE or web searches, but the methods are standard and must be cited: Borinsky AIHPD 10 (2023) 635 [2008.12310]; Jantzen JHEP 12 (2011) 076 [1111.2589]; Semenova–Smirnov–Smirnov EPJC 79 (2019) 136 [1809.04325]; Gardi–Herzog–Jones–Ma–Schlenk JHEP 07 (2023) 197 [2211.14845]; Ma JHEP 09 (2024) 197 [2312.14012]; Ma JHEP 05 (2020) 012 [1910.11304]; Arkani-Hamed–Hillman–Mizera PRD 105 (2022) 125013 [2202.12296]. Already known: the angle-averaging exponent (Collins 2011 §10.7.3); massive-gluon rapidity divergences and non-lightlike lines (Collins §10.5–10.6; hep-ph/9908467); the inductive structure (Collins Theorems 1R–4, §10.7.5–10.7.6).

## required_fixes

### [required_fixes 1]
Persist the deliverables. Write verify/extend/X2-subtraction/REPORT.md verbatim from the X2 agent's structured result (journal row agentId ad47b382e8e1e17ed: summary + 21 results + 10 open), and persist this review. Change the workflow so that reviewers and fixers receive the structured outputs directly, because subagents are not allowed to write report/review .md files. X1 has the same problem.

### [required_fixes 2]
Withdraw the space-like 'genuine pinch' claim (R12, R19(e), summary item 7) and rewrite O8. Correct statement: the real-base fibered density has a non-absolutely-integrable simple pole at 2e^{−2Y}(k⁺)² = M²+κ. There is no Landau pinch, since k ∝ n₁ is incompatible with k² = M² > 0 for space-like n₁. The pole is removable by a complex deformation of k⁺. Space-like vectors, as in Collins §10.6.4, remain admissible for virtual graphs, and 'extends E1' must be deleted.

### [required_fixes 3]
Replace the two-loop asymptotics (R14, R21, summary item 8). Use ∫r = Φ^(2)(t,t)/Q⁴ − (L̃⁴/4 + π²L̃²/2 + 7π⁴/60) = −λ²(L̃⁴/2 + π²L̃² + 12 + 7π⁴/30) + O(λ⁴L̃⁴), with the homogeneity argument that Σ_R∫C_R is exactly the LP polynomial in L̃. State that the azimuth-averaged norm is ≥ ½λ²L̃⁴(1+o(1)). Quote QMC errors from more independent randomizations (n16 and n18 disagree by up to 4σ).

### [required_fixes 4]
R10(ii): the φ³₆ one-loop vertex corrections (UV degree 0) and the hard-line self-energy (degree 2) are UV divergent. Remove '(H3) trivial'. Introduce integrand-level BPHZ renormalization (Ass. D.41), prove that T_H commutes with it, and redo (H1)_H; for the self-energy, (1−T_H)Γ is divergent without mass and wave-function counterterms. List the model's current vertex and all one-loop graphs explicitly.

### [required_fixes 5]
R16 (Thm 5.1, ladders of all n): write the complete proof of (P1), (P2) and the case split (A)/(B) with all constants, and address ε-uniformity of the items. Insert the analytic proof of Lemma 5.3 in place of the sampling in t19: d ≥ zξ(1−1/x) by completing the square with the invariant, and ⟨1/d⟩ ≤ 2/d̄ with d̄ ≥ 1−z+zξ(1−1/x). Until then, grade it [P]/[R]-pending (n=1 analytic, n=2 numerical) and fix summary item 5.

### [required_fixes 6]
R1/Thm 2.6: replace '(A1) disappears' by an explicit analytic lemma with hypotheses. It must cover the existence of the k⁻-residue representation for every approximated term (decay ≥ 2 uniformly, no zero modes at k_i⁺ = 0 for eikonal factors) and the identification of the fibered value of ∫C_R with the DR value that defines the factors. Keep (A1)(b) for Prop D.16, and state the scope: only processes whose single-graph fibered densities are integrable, i.e. no Glauber-pinched processes.

### [required_fixes 7]
Fix the attributions. The angle-averaging p=1 → p=2 phenomenon is Collins 2011 §10.7.3. Massive-gluon rapidity divergences and non-lightlike Wilson lines are Collins 2011 §10.5–10.6 and Collins–Hautmann hep-ph/9908467. The inductive structure is Collins Theorems 1R–4 (§10.7.5–10.7.6). The tropical approximation is Borinsky arXiv:2008.12310, Thms 8.A/8.B. Cite the Newton-polytope literature (Jantzen 2011; Semenova–Smirnov–Smirnov 2019; Gardi–Herzog–Jones–Ma–Schlenk 2023; Ma 2024; Ma 2020; Arkani-Hamed–Hillman–Mizera 2022).

### [required_fixes 8]
Bubble class (R9). Add exact certificates for the sliver (−m²/2P' < k⁺ < 0) and for the U_C1 part III (1<u<2) items for j ≥ 1. State the hybrid regularization used for (H3) (d-dimensional outer loop with a fixed 4D ln^j insertion). State that C_j grows factorially (≈2m²j! from the UV tail, so no resummed statement is possible). Write out the argument for Lemma 3.7: no region with bubble lines in a different mode is leading, and the renormalized insertion is treated via Ass. D.41.

### [required_fixes 9]
Thm 3.3 and R19(b),(c): rephrase the 'corrections' of Def D.5 / Lesson (d) as sharpenings. The reference's λ^β, β<1 constraints are sufficient but not necessary, and natural-scale covers give sharp exponents. Note that at θ=2 the U_H set contains the interior of the diamond, so (H1)_H coincides with the global r-certificate. Restrict '(θ/2)sL' to θ<2 (≈1.44sL at θ=2). Reclassify R19(c) as a remark, not an App. D error.

### [required_fixes 10]
Strengthen the certificate evidence for Thm 3.3. Add the exact ε0 = 1/10 run on the θ=2 cover (my float run gives a worst exponent of λ^1.6 = λ^{2−4ε0}). Assert dual optimality (bᵀy equals the LP optimum) in exact_verify before using the face-dimension bound. Bound frozen variables in numerators through |coefficients| rather than substitution. List the per-cell comparability constants in the report, and archive the exact certificates (cells, dual vectors) for reproducibility.

### [required_fixes 11]
Prop 4.2: change 'soft-first is necessary' to 'soft-first is sufficient; the literal App. D convention fails in exactly the 4 listed cases' (independently confirmed), and cite R6 E5.

### [required_fixes 12]
Thm 6.1 status table: move 'admissibility of all Collins terms at all orders' to unproven, or supply a proof. Add the crossed two-loop vertex and the subdivergent two-loop graphs as unverified, since goal (ii) ('all two-loop graphs') is not met. Label every result as a scalar-model statement and make no QCD claim (O2).

### [required_fixes 13]
Prop 3.2: add 'at ε = 0' and note that the ζ₂/Q̃² sliver statement depends on the fibration and the momentum routing.
