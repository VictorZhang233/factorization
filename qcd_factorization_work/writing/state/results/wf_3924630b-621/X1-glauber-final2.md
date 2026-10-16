# X1-glauber-final2

(structured result persisted from wf_3924630b-621)

## summary

I wrote the complete revision 2 of the X1 Glauber report to `verify/extend_reports/X1-glauber_final2.md` (266,688 characters, 2230 lines, SHA-256 4288ce79…). It applies all seven required fixes of the final review and the lead-author decisions LA-2, LA-5, LA-7, LA-12 and LA-14. Every new or changed proof is backed by a script in `final2_scripts/`, and every log in `final2_logs/` ends ALL PASS.

**The `final_report_markdown` field is not the full text.** The report does not fit in one response: my first attempt was cut off after 196,000 characters. The field instead holds everything written or changed in this revision word for word, with each unchanged passage replaced by a marker pointing to its lines in `X1-glauber_final.md`. A new script, `final2_scripts/rebuild_report_from_backup.py`, turns that backup plus `X1-glauber_final.md` back into the report byte for byte (same SHA-256; `final2_logs/rebuild_report_from_backup.log`). The file on disk is the authoritative full report.

**The seven fixes:**
- **Fix 1 (P5):** exchange propagators restored (radiation from line A carries 1/q2², from line B 1/q1²). The line currents alone are not conserved; adding the three-gluon term A3 restores conservation. Positivity of the defect is kept, the comparison with |A_A+A_B|² is stated, and the circular check is replaced by one that includes propagators and A3.
- **Fix 2 (ERR-S1b):** "contradicted" is now qualified as pointwise (on N_A∩N_B, or on N_B with the class-𝔛₁ regulator). Off N_A the end-pole term survives. New status line.
- **Fix 3 (grades):** pure-math lemmas (L2, L5, L6, L8, Lemma V) are untagged; the model theorems T2, T2′, the T3 proposition and P4 are [P], each with a first sentence naming the model and a complete model-internal proof.
- **Fix 4:** explicit hypotheses and constants for T2′(a),(b), T3(b),(e) and P4(a),(b). This includes a complete new proof of T2′(a).
- **Fix 5:** Lemma V is now proved by hand, and c_U ≤ (3+√2)/2 is an analytic bound.
- **Fix 6:** §13 and the register fields of `asm:appO-collinear-ends` are made consistent.
- **Fix 7:** constants and their dependences, the (A4) derivation, the size of hypothesis (v), the LA-5 exponents, Σ|w| = 89.0, the DGOPS step list, and the disclosures.

**Corrections I found myself:**
- L8(h) was false for gaps with several intermediate states. A counterexample is logged; it is corrected with π/4-weighted norms.
- T2′(a) needs a Lipschitz condition on the regulator, so I added a subclass 𝔛₁ to the regulator definition. **This changes `def:appO-regulator-class` and needs the lead author's acceptance.**
- T2′(a) needs neither N_A nor (REAL) for J_A.
- The physical C_AX coefficient is ∝ Re X_w and is bounded without hypothesis (v). The colour-abelian X² part is not covered; I recorded it as OPEN-14.

## fixes_applied

1. Fix 1(a) P5: replaced the 'common factor 1/q_T^2'. A_A^mu = C(vA.vB)vA^mu/((vA.k)q2^2), A_B^mu = -C(vA.vB)vB^mu/((vB.k)q1^2), with q1+q2 = k, vA.q1 = vB.q2 = 0; radiation from A carries 1/q2^2.
2. Fix 1(b) P5: deleted the claimed gauge invariance of |A_A+A_B|^2. k.(A_A+A_B) = C(vA.vB)(1/q2^2-1/q1^2) is not zero. Added the three-gluon term A3 with k.(A_A+A_B+A3) = 0; the line parts alone suffice only when q1^2 = q2^2 (|k_T| << |q_T|).
3. Fix 1(c) P5: positivity 2C+C(vA.vB)^3/((vA.k)(vB.k)q1^2q2^2) > 0 kept. The interference is at least |A_A+A_B|^2_Feyn, with equality for light-like lines; the self-term/interference ratio is given explicitly (about 1/cosh Y).
4. Fix 1(d) P5: the circular check is replaced by final2_scripts/p5_lipatov_check.py (propagators and A3 included). Updated P5 Verification, section 14.4 item 6, section 14.5, section 16 item 44. Grade [A] unchanged.
5. Fix 2 ERR-S1b: every 'contradicted for the uncut-line part' is now pointwise (N_A and N_B unregulated, T2(a); or N_B with the class-X1 k+ regulator, T2'(a)). Off N_A the end-pole term survives (0.2517 for the apole set). The spectator-integrated statement holds only under asm:appO-collinear-ends and where at least one NF condition holds; the rest is OPEN-2. Status is now 'T2(a) (model, pointwise) + [P] (T2'(c))'.
6. Fix 3(a) grades: removed the rule '[R,R_PT] = pure mathematics about defined classes'. L2, L5, L6, L8 and the new Lemma V are marked (数学). [R,R_PT] is kept for L1, L1', L3, L7, P2 and the content of P3.
7. Fix 3(b) grades: one LA-2 convention throughout (section 0.2, section 18, A.2, A.4, headers). T2, T2', the T3 proposition (b),(c),(e) and P4 are [P], each with a Chinese first sentence naming M_glob and a complete model-internal proof. The QCD transfer is an item with content grade [P].
8. Fix 3(c),(d) grades: T3(a),(g) are [R,R_def] in section 0.2. The departure from rev3-2 item 11 is recorded in A.4; the dagger marks are removed because the three register entries are registered (v2.3) and confirmed by LA-2.
9. Fix 4: explicit hypotheses and constants for T2'(a): (iv') 16 lambda_B <= K_c <= a_min/(2 lambda_A), (v') delta^chi_Y <= 1/2, explicit E^chi_tot, delta^chi_Y, C^chi_X, complete proof Steps 0-7. The slip 2R/K_c is corrected to 3R/K_c.
10. Fix 4: T2'(b) now has |Re X_w - Pi| <= E_tot and |Re p_opp - Pi| <= C_T eps^(1/2)(1+L_B)^2(1+L), with the end-pole value Pi defined explicitly.
11. Fix 4: T3(b) has hypotheses eps <= r^(-1/2)/8 and delta_b <= 1/2, with explicit |Delta X|, delta_b, |V|, |E_b|.
12. Fix 4: T3(e) has hypotheses 2 lambda_A <= K <= a_min/(8 lambda_B) and delta_N(K) <= 1/2, with explicit constants and pi/4 norms. The split condition is weakened to a_min/(2K) >= 4 lambda_B.
13. Fix 4: P4(a),(b) have the explicit decomposition W = W_in + W_out + R_P4, the shift dW = -(is/2pi) I_2 + dR with explicit dR, and an explicit eps-threshold.
14. Fix 5: Lemma V proved by hand: |v_K| < 1/2; |v_K| <= s/4 for all x; cubic remainder bound. Closed forms from nine pole pairs, D = S = sw - ip, and A^2 - |N|^2 = G1+...+G5 with each G_i >= 0. Independent checks: vK_hand_proof.py and vK_bounds_proof.py. c_U <= (3+sqrt2)/2 proved analytically and used in every constant.
15. Fix 6(a): the section 13 fully-coincident bullet separates T2'(a) (proved, k+ regulator alone) from T2'(c) (two-sided, numerics [P], one jet pair).
16. Fix 6(b): asm:appO-collinear-ends now has all register fields (地位, 文献, 被使用于, 解除途径) and an explicit note that it is not a premise of thm:appO-main or thm:dy-factorization (grade-propagation rule).
17. Fix 6(c): 'unconditionally' dropped from the T1 bullet.
18. Fix 7(a): C_I polynomial also in ln(a_max/a_min). C_E, C_T, C_I depend on n_A and (lambda_A/mu_A)^2 through c_rho. E_tot replaced by C_E c^2/4 inside constants; monotonicity lemma proved; (A4) derived with smaller c_rho = 36(2n_A-1) m_A^flat r (lambda_A/mu_A)^2. Size of (v) stated (C_N = 500.6; eps <~ 1e-11, or 6e-9 with explicit delta_Y).
19. Fix 7(b): LA-5 refit exponents 0.63/0.70/0.73 and first-decade slopes 0.680-0.717 (t2_numerics_refit.log).
20. Fix 7(c): L1 counterexample sum|w| = 89.0; the quoted 44.7 is max|w|.
21. Fix 7(d): 'DGOPS step 3/6' now refer to DGOPS's own six-step list (arXiv v1 pp. 38-41: step 3 p. 39, step 6 p. 40); logged in lit_checks_final2.log.
22. Fix 7(e): disclosed that final_scripts/t2_constants.py part (2) only re-tabulates logged values. Barcaro et al. INSPIRE record 3181016, texkey Barcaro:2026dsd, logged.
23. LA decisions: LA-2 grades and register entries; LA-5 exponents; LA-7 all locations verified, no 位置待核实; LA-12 CHANGELOG v2.4 entry list in A.4; LA-14 texkey. Novelty wording: instances of known theorems are 本书给出的推导; no novelty marker printed.
24. Author correction 1: L8(h) with the original norms is false for gaps with several intermediate states (explicit counterexample, l8h_modified_norms.log). Corrected with pi/4 norms; the integrated bounds L8(i) added.
25. Author correction 2: T2'(a) needs a Lipschitz regulator. New subclass X1 in D8, which contains the example regulator.
26. Author correction 3: T2'(a) needs neither N_A nor (REAL) for J_A; T2'(b) has a general Pi without (REAL). Numerically confirmed with a non-factorized J_A (t2p_general_regulated.log).
27. Author correction 4: normalization. The C_AX coefficient is -(1/2) C_A chi^2 Re X_w, bounded without hypothesis (v); the colour-abelian X^2 coefficient is new OPEN-14 (D6, T2, T2', section 17).
28. Author corrections 5-6: (A4) smaller constant; monotonicity proved; Lemma V gives |v_K| <= min(1/2, KR/a_min) instead of min(1/2, 8KR/a_min).
29. Backup format: final_report_markdown holds a lossless reconstruction backup (all new or changed text verbatim plus 49 line-range markers into X1-glauber_final.md and 4 one-line substitutions), because the full 266,688 characters exceed the output limit of one response. rebuild_report_from_backup.py reproduces the file byte-for-byte (log ALL PASS).

## items_needing_confirmation

1. P5 (ii),(iii): amplitudes with exchange propagators; k.(A_A+A_B) = C(vA.vB)(1/q2^2-1/q1^2); form, sign and normalization of the three-gluon term A3 (current conservation, gauge independence of |J|^2); eikonal suppression of the colour-symmetric part; positivity of the Feynman-gauge interference; comparison with |A_A+A_B|^2 and the self-term ratio.
2. T2(a): (A4) derivation and new c_rho; monotonicity lemma and explicit C_I; |Re X_w| <= E_tot and its identification (D6) with the C_AX coefficient of the uncut side sum; X^2 coefficient not addressed (OPEN-14).
3. T2'(a), complete new proof: Step 6 (ray identity for the regulator psi alone, no N_A, no (REAL) for J_A); Step 3 (Q1, Q2, two geometric integrals); Step 4 (P5' and the role of class X1); Step 7 (delta^chi_Y, C^chi_X); collected constants.
4. T2'(b): general end-pole value Pi without (REAL) for J_A; error bound with T2 constants; applicability of L6 with axis poles.
5. T3(b): decomposition X_b = 1/2 - V + Delta X; explicit |Delta X|, delta_b, |V|, |E_b|; hypotheses eps <= r^(-1/2)/8 and delta_b <= 1/2.
6. Lemma V: closed forms v_IF, v_II from nine pole pairs; reduction D = S = sw - ip; A^2 - |N|^2 = sum G_i with each G_i >= 0 for p <= s^2/4; cubic remainder bound.
7. T3(e), complete new proof: (2b) global bound |h_reg| <= 4 c_U^2 m^flat_{A,pi/4} for energies of either sign; decomposition (5) with V_K restricted to R <= R_A; bounds (6); constants and delta_N(K); weakened condition a_min/(2K) >= 4 lambda_B.
8. P4(a),(b): W(12,21) = W_in + W_out + R_P4 with W_in depending on J_A only via lambda_A; halving of the T2 bounds for one strip; shift formula, dR and the eps-threshold argument.
9. L8(h),(i): pi/4 norms; every estimate multiplied by at most 2^3; integrated bounds (i1)-(i4), including (i1) for all X > 0.
10. D8 class X1: a change to def:appO-regulator-class that the lead author must accept (CHANGELOG v2.4); membership of the example regulator.
11. L1': closed form of c_U(t) and the analytic bound (3+sqrt2)/2.
12. ERR-S1b (section 12), the T2 relation to the reference, section 13 and section 2.2: reworded statements (Fix 2, Fix 6) and new status lines.
13. Grades (Fix 3; section 0.2, section 18, A.2, A.4): consistency with LA-2 and FINAL_OUTLINE_v2 section 00.4.

## files

1. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend_reports/X1-glauber_final2.md
2. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend_reports/X1-glauber_final.md
3. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/final2_scripts/p5_lipatov_check.py
4. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/final2_scripts/vK_hand_proof.py
5. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/final2_scripts/vK_bounds_proof.py
6. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/final2_scripts/a4_crho_check.py
7. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/final2_scripts/l8h_modified_norms.py
8. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/final2_scripts/final2_constants.py
9. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/final2_scripts/t2_numerics_refit.py
10. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/final2_scripts/t2p_general_regulated.py
11. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/final2_scripts/lit_checks_final2.py
12. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/final2_scripts/rebuild_report_from_backup.py
13. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/final2_scripts/superseded/
14. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/final2_logs/p5_lipatov_check.log
15. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/final2_logs/vK_hand_proof.log
16. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/final2_logs/vK_bounds_proof.log
17. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/final2_logs/a4_crho_check.log
18. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/final2_logs/l8h_modified_norms.log
19. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/final2_logs/final2_constants.log
20. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/final2_logs/t2_numerics_refit.log
21. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/final2_logs/t2p_general_regulated.log
22. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/final2_logs/lit_checks_final2.log
23. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/final2_logs/rebuild_report_from_backup.log

## final_report_markdown

# Backup of X1-glauber_final2.md (lossless reconstruction form)

The complete report is the file `verify/extend_reports/X1-glauber_final2.md` (266,688 characters, 2230 lines, SHA-256 `4288ce79e9998b14d35b9633879c512232bb1227abceaec620cbdcfe0cc141a1`). It is longer than one response can return verbatim (a verbatim attempt was cut off after 196,000 characters). This backup is nevertheless lossless:

* every passage written or changed in revision 2 is given **verbatim** below;
* every passage copied unchanged from `verify/extend_reports/X1-glauber_final.md` appears as a marker line `[[VERBATIM final.md a-b]]`, meaning lines a to b (inclusive) of that file;
* after the markers are expanded, four one-line wording substitutions are applied, each occurring once: P1 novelty "New;" → "Ours (no marker);"; §12 heading "(proposed App Q entry;" → "(App Q entry;"; T2 Contrast "residual $\propto{\rm Re}\,p_{\rm opp}$;" → "residual $\propto{\rm Re}\,X_w$ (${\rm Re}\,p_{\rm opp}$ in the normalization by $N$);"; dictionary "OPEN-13 is new" → "OPEN-13 (final round) and OPEN-14 (revision 2) are new".

`verify/extend/X1-glauber/final2_scripts/rebuild_report_from_backup.py` performs the expansion and the substitutions. Run on this backup and `X1-glauber_final.md`, it reproduces the report byte for byte (identical SHA-256; `final2_logs/rebuild_report_from_backup.log`).
=====BEGIN REPORT BODY=====
# X1 — Glauber cancellation in inclusive Drell–Yan: final report, revision 2 (Appendix O)

**Status of this document.** Last revision of the proof-extension report X1 (topic: spectator–spectator Glauber exchanges in inclusive Drell–Yan, App O of the monograph). It applies every required fix of the independent final review `X1-glauber-finalreview.md` (Fix 1–Fix 7) and the lead-author decisions `writing/LEAD_DECISIONS.md` (LA-2, LA-5, LA-7, LA-12, LA-14). It supersedes `X1-glauber_final.md` (and, through it, `X1-glauber.md`, `-fix1.md`, `-fix2.md`). It is self-contained: every definition, hypothesis and proof needed for transcription is given here, including the proofs that are new or changed in this revision. Near the end, the section *Additional corrections found in this revision* lists the errors found by the author while writing the complete proofs (not flagged by the final review); the report ends with the section *Final-review fixes*, which maps each required fix to the change made, and the section *Items needing independent confirmation*, which lists every new or changed proof. Reviews, scripts and logs are listed in §14 and Appendix A; the scripts and logs of this revision are in `verify/extend/X1-glauber/final2_scripts/` and `final2_logs/`.

**Grade conventions** (WRITER_SPEC_v2 §4.1–§4.3 as fixed by LA-2). Pure mathematics carries **no tag** and is marked (数学) (L2, L5, L6, L8, Lemma V). [R, R_PT] is used for statements about LCOPT jet factors, localized integrals or Feynman integrals with no unproven input (L1, L1′, L3, L7, P2; the content of P3). [R, R_def] is used for colour algebra (L4). [R, R_cond: premises] is used for implications from numbered register entries (T1, P1). **App O model theorems are [P]**: each is a QCD-relevant statement whose first sentence names the model ($\mathbb M_{\rm glob}$, Def. D4), followed by a complete proof of the model-internal claim (T2, T2′, T3's proposition, P4). [A] and [C] keep their meaning (P5; TMD). No novelty marker is printed for any result of this report (FINAL_OUTLINE_v2 §00.4); where a result is an instance of a known theorem, it is described as 「本书给出的推导」 (our derivation), never as new.

---

## 0. Summary

### 0.1 Setting and question

App O (the two-time localization framework, taken over from App E of the reference document `factorization_qcd-2.pdf` and corrected) proves the cancellation of spectator–spectator (SS) Glauber exchanges in inclusive Drell–Yan (DY) for the graph class $\mathcal G_0$, in which the soft subgraph consists of direct soft lines between the two collinear subgraphs $J_A$, $J_B$. For non-commuting localized insertions on one spectator parton (*coincident* connections), the cancellation rests on the complete-set clause `asm:appO-mixing`(c). This report

1. supplies analytic tools for coincident insertions, each an identity or an explicit bound: joint localization with error bounds, multi-pole external factors, rotation of the $k^+$ contour, a ray identity, and bounds for two-insertion jets;
2. proves model theorems, with explicit hypotheses and explicit constants, for the two coincident $O(g^4)$ patterns (fully and half coincident) in the *global two-time model* (Def. D4);
3. repairs the window construction of `prop:appO-ss-cancel` (side-independent windows);
4. states precisely what remains assumed, and where.

### 0.2 Principal results

| result | content (one line) | grade |
|---|---|---|
| L1 | joint localization of $N$ insertions: exact sector formula, error bound with $\sum_\sigma\lvert w_\sigma\rvert$, closed-quadrant lemma | [R, R_PT] |
| L1′ | multi-pole external factors; Lorentzian-regulator pole weights with the analytic bound $c_U\le(3+\sqrt2)/2$ | [R, R_PT] |
| L5, L6, L8 | rotation of the $k^+$ contour; ray identity; explicit bounds for two-insertion jets (the $\pi/4$ version corrected, integrated bounds added) | (数学) |
| P1 | side-independent windows remove the window-edge terms of `prop:appO-ss-cancel` | [R, R_cond: `asm:appO-lcopt`] |
| T2 | in $\mathbb M_{\rm glob}$, pointwise on $\mathcal N_A\cap\mathcal N_B$, $O(g^4)$, fully coincident SS pair, uncut lines: the $C_AX$ coefficient $\propto{\rm Re}\,X_w$ obeys $\lvert{\rm Re}\,X_w\rvert\le C_E\varepsilon^{1/2}(1+L_B)^2$; $\lvert{\rm Re}\,p_{\rm opp}\rvert\le C_T\varepsilon^{1/2}(1+L_B)^2(1+L)$; ${\rm Im}\,p_{\rm opp}=-\frac1\pi\ln\frac1\varepsilon+O(1)$ with explicit bound | [P] (model theorem; complete model-internal proof); QCD transfer content [P]; physical reading [P] |
| T2′ | (a) class-$\mathfrak X_1$ $k^+$ regulator, on $\mathcal N_B$ only, no (REAL) for $J_A$: explicit bound, ${\rm Re}\,X^\chi=O(\eta(1+l_K)^2+\zeta(1+\ln\frac1\zeta)^2)$ with $\eta=(\lambda_B/K_c)^{1/2}$, $\zeta=\lambda_AK_c/a_{\min}$; (b) end-pole value $\Pi$ with explicit error; (c) two-sided regulators | [P] ((a), (b) complete proofs; (c) numerics) |
| P2 | strict window: $p_{\rm opp}=\tfrac12+2\delta_A\delta_B$, set by the regulator shape | [R, R_PT] ((a) is the reference's) |
| T3 | half-coincident pair: residual $2ic_1c_2\,{\rm Im}W_{12}[X_1,X_2]$; ${\rm Re}\,W_{12}=\frac12+O(\varepsilon(1+L')^2)$ explicit; ${\rm Im}W_{12}=O(1)$ unregulated; explicit power bound with an in-window $k^-$ regulator | (a), (g) [R, R_def]; (b), (c), (e) [P] (model theorem, complete proofs); (d), (f), (e′)-numerics [P] |
| L4 | colour: the half-coincident colour factor vanishes for valence remnants and for real colour states | [R, R_def] |
| P4 | per-graph ordering weights are not fixed by window data, within the stated class | [P] ((a), (b) complete proofs; (c) numerics) |
| P5 | the direct-line ladder class is not closed under unitarity at $O(g^6)$ | [A] |
| ERR-S1b | correction to the reference's Rem E.32 / E.33 status / Rem E.49(2): pointwise, uncut lines, model scope | T2(a) (model, pointwise) + [P] (T2′(c)) |

### 0.3 What is not claimed

* The grade of inclusive DY collinear factorization (`thm:dy-factorization`) is unchanged, [A]. The TMD versions of the results are [C] (§11).
* Every statement that an assumption of type `asm:appO-mixing`(c) is "needed" or "not needed" is relative to App O's two-time framework. None is a statement about QCD factorization as such; the graph-by-graph argument of CSS/Collins/DGOPS (§10) has no ordering weights, and no gap in it is identified here.
* The coincident-pattern theorems concern the side sums of **uncut** SS lines (`def:appO-family`). Direct SS gluons that cross the final-state cut (real emission) belong to $\mathcal G_0$ and to `asm:appO-mixing`(c). They are not covered (Remark C, OPEN-13).
* The model theorems are statements about the global two-time model $\mathbb M_{\rm glob}$ (Def. D4). They hold **pointwise**: on $\mathcal N_A\cap\mathcal N_B$ in the unregulated model (T2), or on $\mathcal N_B$ with the in-window class-$\mathfrak X_1$ $k^+$ regulator (T2′(a); mirror statement on $\mathcal N_A$ with a $k^-$ regulator). Off $\mathcal N_A$ the unregulated uncut side sum keeps the non-zero end-pole term of T2′(b) (for the scalar "apole" set ${\rm Re}\,p_{\rm opp}\to0.2517$). The domains exclude an $O(1)$ part of spectator phase space. A spectator-integrated statement is therefore available only under `asm:appO-collinear-ends` (in-window regulators), and only on the part of spectator phase space where at least one NF condition holds; the part where both fail is OPEN-2. The physical reading needs the matching assumption `asm:appO-collinear-ends` (§2).
* T2 and T2′ control the non-abelian $C_AX$ coefficient of the uncut side sum. The colour-abelian $X^2$ coefficient of the side sum with exact model integrals (Def. D6, normalization remark) is not estimated in this report (OPEN-14).

---

[[VERBATIM final.md 43-113]]
For general hadron wave functions they are open. When applied to QCD jets they enter through the register entries `asm:appO-adjacent-swap` and `asm:appO-real-jets` (\tagP; registered in FINAL_OUTLINE_v2 v2.3 §08 and confirmed by LA-2, item 1; §2.2). A round-3 reviewer test shows that (ADJ) cannot simply be dropped from L8: with one final-state energy changed so that (ADJ) fails, the $1/\kappa_2$ strip tails no longer cancel (`review_r3_1_logs/l8_general.log`).
[[VERBATIM final.md 115-138]]
* **Normalization** (added in this revision). The amplitude-side sum of the two-line family member is $\sum_{\pi_A,\pi_B}I(\pi_A,\pi_B)\,{\rm col}(\pi_A,\pi_B)=N_0\big[Y\,X^2+X_w\,\tfrac{C_A}2X\big]$, with
$$Y:=N/N_0,\qquad X_w:=p_{\rm opp}Y=\big[I(12,21)+I(21,12)\big]/N_0 .$$
  With $\chi$ fixed by the localized one-exchange value (so that $N_0$ corresponds to $(-i\chi)^2/2$), $\mathcal M^{(2)}=\frac{(-i\chi)^2}2\big[YX^2+X_w\frac{C_A}2X\big]$. The form displayed above is the case $Y=1$, which the localized limit realizes (`lem:appO-glauber-operator`). For the exact model integrals the $C_AX$ coefficient of the side sum is therefore $-\frac12C_A\chi^2\,{\rm Re}\,X_w$ (the computation of L4(a) with $p_{\rm opp}$ replaced by $X_w$; the configuration with one line on each side carries only $X^2$); in the normalization by $N$ (the displayed form) it reads $-\frac12C_A\chi^2\,{\rm Re}\,p_{\rm opp}$. The two differ by ${\rm Re}(X_w/Y)-{\rm Re}\,X_w$, which contains the cross term $-{\rm Im}\,X_w\,{\rm Im}\,Y/|Y|^2$ of size up to $2|X_w||Y-1|$.
[[VERBATIM final.md 139-146]]
**Definition D8 (regulators).**

* **Class $\mathfrak X$** (scale $K_c>0$). A factor $\prod_e\chi(k_e^+)$ in which $\chi$ is holomorphic in each closed quadrant obtained by rotating a half line counterclockwise by up to $\pi/2$ (the first quadrant for $k^+>0$, the third for $k^+<0$), real on the half lines, and satisfies
  $$|\chi(k)-1|\le|k|/K_c\ \ (|k|\le K_c),\qquad|\chi(k)|\le K_c/|k|\ \ (|k|\ge K_c).$$
  Consequences used below: $|\chi|\le2$ everywhere, and $|\chi(k_1)\chi(k_2)-1|\le|\chi(k_1)-1||\chi(k_2)|+|\chi(k_2)-1|\le3\max(|k_1|,|k_2|)/K_c$ for $|k_1|,|k_2|\le K_c$.
* **Class $\mathfrak X_1\subset\mathfrak X$** (added in this revision). In addition, $|\chi'(k)|\le K_c^{-1}\min\big(1,K_c^2/|k|^2\big)$ in the closed quadrants. (This Lipschitz condition controls the variation of the regulator across the strips in the proof of T2′(a).)
* *Example.* $\chi=1/(1+k/K_c)$ on $k>0$ and $1/(1-k/K_c)$ on $k<0$ lies in $\mathfrak X_1$: in the respective quadrant $|1\pm k/K_c|\ge\max(1,|k|/K_c)$, which gives the three bounds, since $\chi'=\mp K_c^{-1}(1\pm k/K_c)^{-2}$ (`final2_logs/final2_constants.log`). On the rotated contour $k^+=i\kappa$ it reads $\hat\chi(\kappa)=1/(1+i|\kappa|/K_c)$ for both signs of $\kappa$.
* The class is sufficient, not necessary: a Lorentzian $k^+$ regulator also gives ${\rm Re}\,p_{\rm opp}\to0$ numerically (§7, T2′). The relation of $K_c$ to the jet scales is a hypothesis of the theorems that use the class (T2′(a): $16\lambda_B\le K_c\le a_{\min}/(2\lambda_A)$), not part of the definition.
* **Even Lorentzian.** $\chi_K(k):=K^2/(k^2+K^2)$, used on $k^-$ on the $A$ side.
* **Two-sided window** (`asm:appO-collinear-ends`). Use $\chi^+(k^+)$ at a scale $K^+$ with $\lambda_B\ll K^+\ll a/\lambda_A$, and $\chi^-(k^-)$ at a scale $K^-$ with $\lambda_A\ll K^-\ll a/\lambda_B$. Require $K^+K^-\gg a$, so that the near-shell segment $2k^+k^-\sim\mathbf k_T^2$ is retained. The range $a\ll K^+K^-\ll a/\varepsilon$ is non-empty for $\varepsilon\ll1$. (This is the setting of an assumption, stated qualitatively; the proven statements T2′(a) and T3(e) use one regulator each, with explicit conditions.)
[[VERBATIM final.md 154-156]]
## 2. Assumptions

### 2.1 Register entries used

These are entries of `spec_v2/ASSUMPTIONS.md` v2.3 (= FINAL_OUTLINE_v2 §08), with their registered tags.

* `asm:appO-lcopt` [\tagA]: (i) no zero modes or endpoint contributions; minus-component truncation can be dropped; (ii) instantaneous loops. It is the source of (SEC).
* `asm:appO-envelope` [\tagA]: the fibre-integrated envelope; for coincident connections imposed on side-summed families (v2.3 rewording, recalled in §2.3).
* `asm:appO-mixing` [\tagA]: (a′) pre-integration localization with envelope bounds (v2.3 reformulation of the earlier half-plane splitting clause (a), recalled in §2.3); (b) cut compatibility of $S$; (c) the complete-set clause.
* `asm:appO-deformation` [\tagA], items (a)–(d).
* `asm:appO-rewritten-cs` [\tagA].
* The App N inputs listed for `thm:appO-main` (`asm:appN-envelope`, `asm:appN-separation`, `asm:appN-ward-product`).

### 2.2 New register entries (registered in v2.3; confirmed by LA-2)

The owner is App O. The three entries below were proposed in the final report, are registered in FINAL_OUTLINE_v2 v2.3 §08 and `spec_v2/ASSUMPTIONS.md` v2.3 §3.4, and their tags are confirmed by the lead author (LA-2, item 1). The field texts below agree with the register.

**`asm:appO-adjacent-swap` (相邻交换对称性（ADJ）) — \tagP.**

* *Statement:* every leading-power cut-summed LCOPT jet factor $J_X$ ($X=A,B$) of QCD graphs with two amplitude-side insertions on spectator partons satisfies (ADJ) of Def. D3.
* *地位 (status):* [P]: exact in the scalar spectator model; argued, not proved, for spin-summed good-component couplings (Def. D3); no literature argument. It enters only the QCD transfer of the model theorems, which are [P]; it is not a premise of `thm:appO-main` or `thm:dy-factorization`.
* *文献:* — (formulated here).
* *被使用于 (used by):* `prop:appO-twoexch-spectator` (T2(b)), `prop:appO-pergraph-weights` (P4), `prop:appO-halfcoinc-sensitivity` (T3).
* *解除途径 (discharge):* a proof for leading-power cut-summed LCOPT jets (numerator structure of `lem:appO-numerators`); OPEN-12.

**`asm:appO-real-jets` (旁观者喷注函数的实性（REAL）) — \tagP.**

* *Statement:* (REAL) of Def. D3 holds for the leading-power cut-summed LCOPT jet factors of QCD graphs with spectator insertions.
* *地位:* [P]: exact in the scalar model; argued for perturbative spin-summed leading-power LCOPT jets; open for general hadron wave functions. Enters only the QCD transfer of the model theorems.
* *文献:* — (formulated here).
* *被使用于:* `prop:appO-twoexch-spectator`, `prop:appO-pergraph-weights`, `prop:appO-halfcoinc-sensitivity`. (T2′(a) uses (REAL) only for $J_B$; T3(e) uses no (REAL) at all.)
* *解除途径:* a proof for leading-power cut-summed LCOPT jets; OPEN-12.

**`asm:appO-collinear-ends` (共线端点的匹配) — \tagA.**

* *Statement:* the SS windows carry the two-sided analytic rapidity regulators of Def. D8. The complements are the $A$-collinear end ($|k^+|\gtrsim K^+$) and the $B$-collinear end ($|k^-|\gtrsim K^-$), together with the cut contributions located there. They are assigned to the collinear regions, where collinear factorization (Wilson lines and subtraction terms) reproduces them with no leftover Hermitian $C_AX$ term (fully coincident pattern) and no leftover $[X_1,X_2]$ term (half-coincident pattern).
* *地位:* open, [A]. Supporting evidence: P3; `prop:dy-eikonal-twogluon`; T2′(a) (the fully coincident uncut-line part is proved in the model with the class-$\mathfrak X_1$ $k^+$ regulator alone, on $\mathcal N_B$); T2′(c) (two-sided regulators, numerics [P]); T3(e) (the half-coincident uncut-line part is proved in the model with the $k^-$ regulator alone). DGOPS §4 removes soft–collinear overlaps by subtraction terms (their step 6, §10). The SCET argument of Zhou et al. is an EFT form of the statement (§10; we do not accept its key step as a proof). The cut direct-line contributions at the collinear ends are not computed (Remark C, OPEN-13). The entry **relocates, rather than removes,** the content of `asm:appO-mixing`(c) for the coincident $O(g^4)$ patterns.
* *Relation to the main theorems:* it is **not** a premise of `thm:appO-main` or `thm:dy-factorization`, which keep `asm:appO-mixing`(c) with tag \tagA (LA-2, item 1). If it replaced `asm:appO-mixing`(c) and were tagged \tagP, the grade-propagation rule (WRITER_SPEC_v2 §4.6, item 3) would lower `thm:dy-factorization` to [P], contradicting the [A] grade of that theorem. Its tag is \tagA because the subtraction treatment of soft–collinear overlaps is part of the CSS/Collins/DGOPS all-order argument, although not proven in this form.
* *文献:* `Zhou:2017his`, `Liu:2008cc`, `RothsteinStewart2016`, `Collins2011` §14.4.
* *被使用于:* `prop:appO-twoexch-spectator` (physical reading, T2(c)), `prop:appO-twoexch-regulated` (T2′), `prop:appO-halfcoinc-sensitivity` (T3).
* *解除途径:* compute the cut direct-line contributions at the collinear ends, or prove their suppression with the two-sided regulators (Remark C, `rem:appO-cut-ss`, OPEN-13); then prove the matching itself (OPEN-1, OPEN-6).

### 2.3 Rewordings of existing entries (implemented in ASSUMPTIONS.md v2.3)

* **`asm:appO-envelope`.** For coincident connections, the envelope bound is imposed on *side-summed* families. Within the class of P4, the per-graph version cannot hold for coincident pairs (P4). For graph-generated jets the per-graph question is open (OPEN-10).
* **`asm:appO-mixing`(a) → (a′).** Localization is performed *before* the integration over the internal loops of $S$, pointwise outside an exceptional set $E_j$ (L7). Assumed: envelope bounds $C\lambda^aL^K$ (i) for the $S$-loop integral of the absolute localization error, including the factor $\sum_\sigma|w_\sigma(p)|$ when there are several insertions, and (ii) for the unlocalized integrand on $E_j$. These bounds also justify the Fubini interchange.

### 2.4 Local hypotheses, not registered

The precedents are those of ASSUMPTIONS.md §6.

* (SEC) and (EQ): hypotheses of mathematical lemmas, verified in LCOPT, like (ET1)(ET2) of `lem:appO-equal-time`.
* $\mathbb M_{\rm glob}$: a model definition, like the class definition (GC1)–(GC3).
* $\mathcal N_A,\mathcal N_B$: domain definitions for pointwise statements.
* Classes $\mathfrak X$, $\mathfrak X_1$: definitions.
* (ADJ) and (REAL): class conditions of Def. D3. They are hypotheses of the pure-mathematics lemma L8 and of the model-internal claims of T2, T2′, T3 and P4, which concern defined classes. For QCD jets they are the registered entries `asm:appO-adjacent-swap` and `asm:appO-real-jets` (\tagP), which enter only the QCD-transfer items.

[[VERBATIM final.md 209-308]]
  * the round-2 counterexample to the uncorrected bound ($N=2$, $z=(1-0.01i,-0.99-0.01i)$, both poles final): actual relative error 8.86 against the old bound 3.58. The two race weights are $20.4+39.8i$ and $-19.4-39.8i$, so $\sum_\sigma|w_\sigma|=44.72+44.28=89.0$. The factor 44.7 used in the log is $\max_\sigma|w_\sigma|$; it enters the per-sector form (first inequality of (b)), and the corrected per-sector bound 160.0 holds. (`final2_logs/final2_constants.log` recomputes $\sum_\sigma|w_\sigma|=89.0$ and $\max_\sigma|w_\sigma|=44.7$.)
[[VERBATIM final.md 310-311]]
**Novelty.** Known: the race formula, which appears in the reference (App E.4.4, as an example) and in `lem:appO-joint-localization`(a); and $\sum w=1$, which is the eikonal identity (App B) and coincides with the sector-sum ("causal") identity of Aybat–Sterman, eq. (10). The sector rule (a) and its exactness at finite $\eta$ are 本书给出的推导 (residue calculus applied to the LCOPT sector form). The bound (b) with the factor $\sum_\sigma|w_\sigma|$, the closed-quadrant lemma (b1) and (d) are new as stated (elementary). The lemma is printed as a sharpened result without novelty marker (FINAL_OUTLINE_v2 §00.4, N13).
[[VERBATIM final.md 313-348]]
* *Constant.* On the $\pi/4$ contour put $t:=|x_e|=K/|z_e|=2K|\kappa_e|/a_e$ (for a final line $x_e:=iK/z_e=-te^{-i\pi/4}$, for an initial line $x_e=te^{-i\pi/4}$). In terms of $x_e$ the weights are $u_z=x_e^2/(x_e^2-1)$, $u_+=1/(2(1-x_e))$, $u_-=1/(2(1+x_e))$, so
  $$\sum_p|u_e(p)|=c_U(t):=\frac{t^2}{\sqrt{1+t^4}}+\frac1{2\sqrt{1+\sqrt2\,t+t^2}}+\frac1{2\sqrt{1-\sqrt2\,t+t^2}}$$
  for both kinds of line. Its supremum is $c_U:=\sup_tc_U(t)=1.64853$ (numerical maximum at $t=1.154$). **Analytic bound:** $t^2/\sqrt{1+t^4}\le1$, $1+\sqrt2t+t^2\ge1$ and $1-\sqrt2t+t^2=(t-1/\sqrt2)^2+\frac12\ge\frac12$, hence
  $$c_U\le1+\tfrac12+\tfrac1{\sqrt2}=\tfrac{3+\sqrt2}2=2.2071\ \ (\le1+\sqrt2),\qquad c_U^2\le\tfrac{11+6\sqrt2}4=4.8713 .$$
  All proofs below use only the analytic bound; the numerical value 1.64853 is quoted for orientation.
[[VERBATIM final.md 350-351]]
**Verification.**

* The sum rule symbolically (`review_r2_1_scripts/symbolic_checks_r2.py`).
* The $K\to\infty$ limit (`fix_r1_logs/regulator_indep_A.log`).
* $c_U=1.6485$ (`fix_r2_logs/t3e_sensitivity.log`), reproduced as 1.64853 by both round-3 reviewers; the closed form $c_U(t)$, its maximum 1.64853 and the analytic bound $(3+\sqrt2)/2$ in `final2_scripts/vK_bounds_proof.py` → `final2_logs/vK_bounds_proof.log` (direct pole-weight evaluation on both rays: 1.64851).

**Novelty:** 本书给出的推导 (partial fractions and multilinearity applied to L1; elementary).
[[VERBATIM final.md 359-359]]
### Lemma L2 (the weights as functions of $k^+$) — (数学)

*Proposed:* consequence item of `lem:appO-joint-localization`, printed as an item marked 「（数学）」 (pure mathematics: a statement about the explicit rational functions $W_\pi$; LA-2, item 2).
[[VERBATIM final.md 363-382]]
**Novelty.** 本书给出的推导 (a consequence of the eikonal identity L1(c)). It corrects the wording of REFDOC_ANALYSIS ERR-S3, which said that coincident weights are non-analytic "exactly like $\theta(k^+)$": for spectators they are continuous, with a kink.
[[VERBATIM final.md 384-406]]
**Novelty:** 本书给出的推导 (an explicit instance of L1).
[[VERBATIM final.md 408-439]]
**Novelty:** 本书给出的推导 (elementary); its use as a pre-integration replacement of `asm:appO-mixing`(a) is ours.
[[VERBATIM final.md 441-445]]
### Lemma L5 (rotation of the $k^+$ contour) — (数学)
[[VERBATIM final.md 447-496]]
**Novelty:** 本书给出的推导 (a contour rotation of Wick type; the holomorphy domains and the arc estimates for the present integrands are ours).
[[VERBATIM final.md 498-498]]
### Lemma L6 (ray identity) — (数学)
[[VERBATIM final.md 500-522]]
**Novelty:** 本书给出的推导 (an instance of Cauchy's theorem); its role in T2 and T2′ is ours.
[[VERBATIM final.md 524-524]]
### Lemma L8 (two-insertion jets on the rotated contour) — (数学)
[[VERBATIM final.md 526-565]]
**(h) The $\pi/4$ contour** (corrected in this revision). On $p=-e^{i\pi/4}\kappa$ every gap factor obeys $|A-e^{i\pi/4}y|\ge\max(|A|,|y|)/\sqrt2\ge\langle y\rangle/2$. Define the *$\pi/4$ norms*
$$M_{\pi/4,\sigma}:=\sum_t|c_t|\Big(\frac{\sqrt2}{\lambda}\Big)^{d_t},\qquad M^\flat_{\pi/4,\sigma}:=\sum_t|c_t|\Big(\frac{\sqrt2}{\mu}\Big)^{d_t},$$
and $M_{\pi/4}$, $M^\flat_{\pi/4}$ their maxima over $\sigma$. (If every term has $d_t\le2$, then $M_{\pi/4}\le2M$ and $M^\flat_{\pi/4}\le2M^\flat$; in the scalar spectator model $d_t=0$ and the $\pi/4$ norms equal $M$, $M^\flat$.) Then:

* (a) holds with $2/\langle y\rangle$ and $2\lambda/(|y|\langle y\rangle)$;
* (b) holds as $|J^{(\sigma)}|\le4M^\flat_{\pi/4,\sigma}/(\langle y_1\rangle\langle y_2\rangle)$;
* (c)–(g) hold with every constant multiplied by 8 and with $M$, $M^\flat$ replaced by $M_{\pi/4}$, $M^\flat_{\pi/4}$, and with $e^{-2i\theta}$ and $1/(ip_2)$ in place of $-1$ and $1/\kappa_2$.

The final-round statement "(b)–(g) hold with every constant multiplied by 8" with the original norms $M$, $M^\flat$ is false for multi-state gaps: each extra state costs $\sqrt2/\mu$ instead of $1/\mu$ on the $\pi/4$ ray, so the claimed factor 8 can be exceeded once a term has $d_t\ge3$ extra states ($4\cdot2^{3/2}>8$). `final2_logs/l8h_modified_norms.log` exhibits a five-state gap that exceeds the claimed bound by the factor 1.083 (its four-state gap stays below it, at 0.766).

**(i) Integrated bounds for $S$-type functions** (added in this revision; used in T2′(a), T3(b), T3(e)). Let $S$ be $f_{12}+f_{21}$, or any function that obeys (b) sector by sector, (c) off the strip, and (d) in the strip with cancelling $g$-terms. Put $l_X:=\ln(1+4X/\mu)$ and $\ell:=\ln(1+16\lambda/\mu)$. Then

* (i1) $\int_{R\le X}|S|\,d^2\kappa\le24M^\flat l_X^2$ for every $X>0$;
* (i2) $\int_{R>X}|S|\,d^2\kappa\le6572M^\flat(\lambda/X)(1+l_X)$ for $X\ge4\lambda$;
* (i3) $\int_{R\le X}R|S|\,d^2\kappa\le96M^\flat\lambda\,l_X^2+6572M^\flat\lambda(1+l_X)\ln\frac{X}{4\lambda}$ for $X\ge4\lambda$;
* (i4) $\int_{\mathbb R}|g(-iU)|\,dU\le4M^\flat(1+\ell)$, and $\int_{|U|\le X}|U||g(-iU)|\,dU\le4M^\flat\lambda\big(1+2\ln\frac X\lambda\big)$ for $X\ge\lambda$.

On the $\pi/4$ contour, (i1)–(i3) hold with the constants $192$, $52576$, $768$ in place of $24$, $6572$, $96$ and with $M^\flat$ replaced by $M^\flat_{\pi/4}$.
[[VERBATIM final.md 567-638]]
*(h).* On the $\pi/4$ ray, $|A-e^{i\pi/4}y|^2=A^2+y^2-\sqrt2Ay=(|A|-|y|/\sqrt2)^2+y^2/2=(|y|-|A|/\sqrt2)^2+A^2/2$ in the worst case $Ay>0$, so $|A+K|\ge\max(|A|,|y|)/\sqrt2\ge\langle y\rangle/2$ (because $\max(|A|,|y|)\ge\max(\mu,|y|)\ge\langle y\rangle/\sqrt2$).

* A single-state gap factor, and the first state of a multi-state gap, obey $|i/(A+K)|\le2/\langle y\rangle$, twice the bound at $\theta=\pi/2$; the eikonal comparison obeys $|i/(A+K)-i/K|=|A|/(|K||A+K|)\le2\lambda/(|y|\langle y\rangle)$. This is (a).
* Each extra state of a multi-state gap obeys $|1/(A_j+K)|\le\sqrt2/\max(|A_j|,|y|)$, i.e. at most $\sqrt2/\mu$, and at most $\sqrt2\cdot4/R$ where $|y|\ge R/4$; these factors $\sqrt2$ are exactly absorbed by the $\pi/4$ norms. With the first-state factors this gives (b).
* Every estimate in (c)–(g) is a sum of products of at most three such gap-factor bounds (the remaining factors $1/|p_e|$, $1/|P|$ are exact moduli). After absorbing the extra states into the $\pi/4$ norms, each estimate is therefore multiplied by at most $2^3=8$. The cancellations used — the eikonal identities under (EQ), the pairings under (ADJ), and the residue and rotation argument of (e), (f) for $\theta\in[0,\pi/2]$ — are algebraic or contour statements and hold unchanged.

*(i).*

* (i1) is the first bullet of (g), which uses only (b) and therefore holds for every $X>0$: the region $R\le X$ maps into $|y_e|\le2X$, $\int_{|y|\le2X}dy/\langle y\rangle=2\,{\rm asinh}(2X/\mu)\le2l_X$, so each of the three sectors of each colour order contributes at most $4M^\flat l_X^2$; two colour orders give $24M^\flat l_X^2$.
* (i2): off the strip, (g) gives $3200M^\flat(\lambda/X)(1+l_X)$ per colour order; in the strip $S=E_{12}+E_{21}$ because the $g$-terms cancel (d), and (g) gives $86M^\flat(\lambda/X)(1+l_X)$ per order. In total $2(3200+86)=6572$.
* (i3) (layer cake): $\int_{R\le X}R|S|=\int_0^Xdr\int_{r<R\le X}|S|\le4\lambda\int_{R\le X}|S|+\int_{4\lambda}^Xdr\int_{R>r}|S|$. Insert (i1) and (i2) with $l_r\le l_X$.
* (i4): by (e), $\int|g|\le\int_{|U|\le\lambda}2M^\flat\langle U\rangle^{-1}dU+\int_{|U|>\lambda}4M\lambda U^{-2}dU=4M^\flat{\rm asinh}(\lambda/\mu)+8M\le4M^\flat[\ln(1+2\lambda/\mu)+2]$, and $\ln(1+2x)+2\le1+\ln(1+16x)$ for $x=\lambda/\mu\ge1$ because $(1+16x)/(1+2x)\ge17/3>e$. First moment: $\int_{|U|\le\lambda}|U|\,2M^\flat\langle U\rangle^{-1}dU\le4M^\flat\lambda$ and $\int_{\lambda<|U|\le X}|U|\,4M\lambda U^{-2}dU=8M\lambda\ln(X/\lambda)$.
* On the $\pi/4$ contour the same arguments apply with the constants of (h): $8\cdot24=192$, $8\cdot6572=52576$, $8\cdot96=768$. $\square$
[[VERBATIM final.md 640-647]]
* **Final revision.** `final2_scripts/l8h_modified_norms.py` → `final2_logs/l8h_modified_norms.log`, ALL PASS: (1) explicit counterexample to the final-round (h) with the original norms (one $n$-state gap with all energies $-\mu$, at $\kappa_1=-\mu/\sqrt2$): ratio to the claimed bound $0.766,\ 1.083,\ 1.532,\ 3.064$ for $n=4,5,6,8$, while the corrected (b) gives 0.542 for every $n$; (2) the corrected (h) on 400 random (ADJ)-class jets with gaps of up to six states at $\theta=\pi/4$: maximum ratios (b) 0.188, (c) 0.0003, (d) 0.0005, (e) 0.026 (random energies) and (b) 0.762, (c) 0.0062, (d) 0.0121, (e) 0.108 (adversarial energies $A=-\mu$), against 11.8 for (b) with the original norms. The arithmetic of (i) and two geometric integrals used later are checked in `final2_logs/final2_constants.log`.
[[VERBATIM final.md 648-648]]
**Novelty:** new as stated (elementary; no marker).
[[VERBATIM final.md 650-764]]
**Novelty.** The statements are known: `prop:appO-ss-cancel`(iii) and the reference's Props E.35/E.31(iii). The uniform route via L1 is 本书给出的推导. The TMD version is [C] (§11).
[[VERBATIM final.md 766-816]]
## 7. The fully coincident pattern

### Theorem T2 (fully coincident SS pair at $O(g^4)$; model theorem for the uncut side sum) — [P]

*Label:* `prop:appO-twoexch-spectator` (slot X1f, PARTIAL; Appendix A). Grade: [P] as a QCD statement (LA-2, item 2): a model theorem whose first sentence names the model, with a complete proof of the model-internal claim (a).

**First sentence (printed).** 「在全局两时模型 $\mathbb M_{\rm glob}$（`def:appO-glob-model`）中、在 $\mathcal N_A\cap\mathcal N_B$ 上逐点、$O(g^4)$ 阶，对振幅侧两条连接同一个 $A$ 旁观者 $i$ 与同一个 $B$ 旁观者 $j$ 的**未割** SS 线，在下述假设 (i)–(v) 之下，以下结论成立。」 (In $\mathbb M_{\rm glob}$, pointwise on $\mathcal N_A\cap\mathcal N_B$, at $O(g^4)$, for two **uncut** SS lines joining the same $A$-spectator $i$ and the same $B$-spectator $j$ on the amplitude side, the following holds.)

**Hypotheses.**

* (i) The model $\mathbb M_{\rm glob}$ (Def. D4), with exact connecting propagators.
* (ii) $J_A$ satisfies (SEC), (EQ), (REAL). $J_B$ satisfies (SEC), (EQ), (ADJ), (REAL).
* (iii) The configuration lies in $\mathcal N_A\cap\mathcal N_B$.
* (iv) $\varepsilon\le\varepsilon_0:=\min\big(\frac1{16},\frac{a_{\min}^2}{4a_1a_2}\big)$.
* (v) $\delta_Y\le\frac12$, where $\delta_Y:=2\mathcal E_1+2\mathcal E_2+2\mathcal E_3+\mathcal E_4$ is given explicitly in Steps 3–5. Condition (v) is not implied by (iv): the term $2\mathcal E_2$ alone is $\approx167\,m^\flat_B\varepsilon^{1/2}(1+L_B)$. It holds for $\varepsilon$ small enough, given the jet constants. **Size:** with all jet constants equal to 1 and $a_{\max}=a_{\min}$, $C_N=500.6$, so the sufficient condition $C_N\varepsilon^{1/2}(1+L_B)^2\le\frac12$ needs $\varepsilon\lesssim2\times10^{-11}$ for $\lambda_B/\mu_B=1$ and $\varepsilon\lesssim1\times10^{-11}$ for $\lambda_B/\mu_B=10$; evaluating $\delta_Y=2\mathcal E_1+2\mathcal E_2+2\mathcal E_3+\mathcal E_4$ directly relaxes this to $\varepsilon\lesssim6\times10^{-9}$ and $4\times10^{-9}$ (`final2_logs/final2_constants.log`). The numerical tests below run at $\varepsilon=10^{-2}$ to $10^{-5}$, so they probe the statement, not the proven bound.

**Conclusion.**

**(a) (model-internal; complete proof).** With $X_w=p_{\rm opp}N/N_0$ (Def. D6, normalization),
$$|{\rm Re}\,X_w|\le\mathcal E_{\rm tot}\le C_E\,\varepsilon^{1/2}(1+L_B)^2\qquad\text{(this needs only (i)–(iv))},$$
$$|N/N_0-1|\le\delta_Y\le C_N\,\varepsilon^{1/2}(1+L_B)^2,$$
$$|{\rm Re}\,p_{\rm opp}|\le C_T\,\varepsilon^{1/2}(1+L_B)^2(1+L),$$
$$\Big|{\rm Im}\,p_{\rm opp}+\frac1\pi\ln\frac1\varepsilon\Big|\le C_I .$$
The constants $C_E$, $C_N$, $C_T$, $C_I$ are written out in Step 8. They are explicit polynomials in $m_A$, $m^\flat_A$, $m^\flat_B$, $m_B$, $c_\rho$, $r:=a_{\max}/a_{\min}$, $\ell_A$, $\ell_B$ and, for $C_I$, also $\ln(a_{\max}/a_{\min})$ (through $C_{IX}$ and $R_{\rm out}$). Through $c_\rho=36(2\bar n_A-1)m^\flat_A\,r\,(\lambda_A/\mu_A)^2$ (Step 1, (A4)), $C_E$, $C_T$ and $C_I$ also depend on the maximal number $\bar n_A$ of states in a gap of $J_A$ and on $(\lambda_A/\mu_A)^2$. $C_N$ does not depend on $c_\rho$. $C_T$ and $C_I$ depend on $\ln(\lambda_B/\mu_B)$ and $\ln(\lambda_A/\mu_A)$ through $\ell_B$ and $\ell_A$.

*Consequences.*

* The $C_AX$ coefficient of the side sum of the uncut lines is $-\frac12C_A\chi^2\,{\rm Re}\,X_w$ in the normalization by the localized value $N_0$ (Def. D6). It is power suppressed: $|{\rm Re}\,X_w|\le C_E\varepsilon^{1/2}(1+L_B)^2$, without hypothesis (v) and without the factor $(1+L)$. In the normalization by $N$ used in L4(a), the coefficient is $-\frac12C_A\chi^2\,{\rm Re}\,p_{\rm opp}$, power suppressed by the third bound.
* The colour-abelian $X^2$ coefficient of the side sum, which compares $2\,{\rm Re}\,Y$ with the configuration with one line on each side, is not addressed by T2. It cancels identically in the localized limit (L4(a)); its non-localized corrections are OPEN-14.
* The $C_A$ term of $\mathcal M^{(2)}$ equals $(-i\chi X)\big(-C_A\chi\ln(1/\varepsilon)/(4\pi)\big)$ at leading-logarithmic accuracy. This is a real multiple of the anti-Hermitian one-exchange amplitude: the gluon reggeization phase.

**(b) QCD transfer.** For leading-power cut-summed LCOPT jets of QCD graphs, (SEC) and (EQ) hold under `asm:appO-lcopt` (Def. D2; `lem:appO-insertion-values`), and (ADJ), (REAL) are the registered entries `asm:appO-adjacent-swap`, `asm:appO-real-jets` (\tagP; LA-2). Hence (a) holds for these jets as an implication [R, R_cond: `asm:appO-lcopt`, `asm:appO-adjacent-swap`, `asm:appO-real-jets`] whose content grade is [P], set by the two \tagP premises (WRITER_SPEC_v2 §4.6, item 2). This coincides with the [P] grade of the theorem. In the scalar spectator model (§14.1) all of (ii) holds exactly, and (a) holds there with no premise.

**(c) [P] (physical reading).** See below. It is conditional on `asm:appO-collinear-ends` and on OPEN-13.

[[VERBATIM final.md 855-878]]
* **(A4)** On the strip $|\kappa_1+\kappa_2|\le\kappa_2/3$ (with $\kappa_2>0$, so $\kappa_1=-s<0$ and $s\in[\frac23\kappa_2,\frac43\kappa_2]$):
$$|\partial\rho/\partial\kappa_1|\le c_\rho\,(\lambda_A/a_{\min})\min\big(1,(\kappa_*/\kappa_2)^2\big),\qquad\kappa_*:=a_{\min}/(4\lambda_A),\qquad c_\rho:=36(2\bar n_A-1)\,m^\flat_A\,\frac{a_{\max}}{a_{\min}}\Big(\frac{\lambda_A}{\mu_A}\Big)^2,$$
  where $\bar n_A$ is the maximal number of states in a gap of $J_A$. (The final-round value $50(2\bar n_A-1)m^\flat_A(a_{\max}/a_{\min})^2(\lambda_A/\mu_A)^2$ is larger; the derivation below gives the smaller constant.) (A4) holds for real energies of either sign, so it does not use $\mathcal N_A$.

  *Derivation.* At $k^+=(i\kappa_1,i\kappa_2)$ in the quadrant $(-,+)$ the poles are $z_1=ia_1/(2s)$ (initial) and $z_2=-ia_2/(2\kappa_2)$ (final), and the prefactor of L3 is $(+ir_1)(-ir_2)=1/(4s\kappa_2)$. Since $i/(A+ia/(2s))=2s/(a-2isA)$ and $i/(A'+ia/(2\kappa_2))=2\kappa_2/(a-2i\kappa_2A')$,
  $$\rho(\kappa_1,\kappa_2)=\frac{a_1a_2}{\mathcal J_A}\sum_tc_t\,G_t(s)\,H_t(\kappa_2),\qquad G_t(s)=\frac{(2s)^{n_1-1}}{\prod_{j=1}^{n_1}(a_1-2isA_j)},\qquad H_t(\kappa_2)=\frac{(2\kappa_2)^{n_2-1}}{\prod_{j=1}^{n_2}(a_2-2i\kappa_2A'_j)},$$
  with $n_1,n_2$ the numbers of states in the two gaps of term $t$ of sector $1V2$. Further, $\partial\rho/\partial\kappa_1=-\partial\rho/\partial s$ and $\partial_sG_t=G_t\big[(n_1-1)/s+\sum_j2iA_j/(a_1-2isA_j)\big]$. Use $|a-2isA|=(a^2+4s^2A^2)^{1/2}\ge\max(a,2s|A|)$, so that $|2iA_j/(a_1-2isA_j)|\le\min(2\lambda_A/a_1,1/s)$, and $\mu_A\le|A|\le\lambda_A$.
  * *Bound for all $\kappa_2$.* Using $|a_1-2isA_1|\ge a_1$ and $|a_1-2isA_j|\ge2s\mu_A$ for $j\ge2$: $|G_t|\le a_1^{-1}\mu_A^{-(n_1-1)}$. Using two factors $\ge a_1$ and the others $\ge2s\mu_A$: $|G_t|(n_1-1)/s\le2(n_1-1)\mu_A^{-(n_1-2)}a_1^{-2}\le a_1^{-1}\mu_A^{-(n_1-1)}\cdot2(n_1-1)\lambda_A/a_1$. Hence $|\partial_sG_t|\le a_1^{-1}\mu_A^{-(n_1-1)}(2\lambda_A/a_1)(2n_1-1)$. With $|H_t|\le a_2^{-1}\mu_A^{-(n_2-1)}$,
  $$|\partial\rho/\partial\kappa_1|\le2(2\bar n_A-1)\,m^\flat_A\,\lambda_A/a_{\min}.$$
  * *Bound for large $\kappa_2$.* Using $|a_1-2isA_j|\ge2s\mu_A$ for all $j$: $|G_t|\le1/(2s\mu_A^{n_1})$ and $|\partial_sG_t|\le(2n_1-1)/(2s^2\mu_A^{n_1})\le\frac98(2n_1-1)\kappa_2^{-2}\mu_A^{-n_1}$ (from $s\ge\frac23\kappa_2$). Likewise $|H_t|\le1/(2\kappa_2\mu_A^{n_2})$. Hence
  $$|\partial\rho/\partial\kappa_1|\le\tfrac9{16}(2\bar n_A-1)\,m^\flat_A\,\frac{a_1a_2}{\kappa_2^3\mu_A^2}.$$
  * *Combination.* For $\kappa_2\le\kappa_*$ the first bound gives (A4), since $c_\rho\ge2(2\bar n_A-1)m^\flat_A$. For $\kappa_2>\kappa_*$ the ratio of the second bound to $c_\rho(\lambda_A/a_{\min})(\kappa_*/\kappa_2)^2$ equals exactly $\kappa_*/\kappa_2<1$ (insert $\kappa_*^2=a_{\min}^2/(16\lambda_A^2)$ and $a_1a_2=a_{\max}a_{\min}$). (`final2_logs/final2_constants.log` checks the ratio symbolically.)

  *Tests.* `final_review_logs/fr_t2_A4.log` (final review, old $c_\rho$): maximum ratio 0.0396 on 3000 random jets. `final2_scripts/a4_crho_check.py` → `final2_logs/a4_crho_check.log` (new $c_\rho$; 4000 random multi-state mixed-sector jets, up to five states per gap, 30% without NF, $a_{\max}/a_{\min}$ up to $10^4$): maximum ratios 0.999 (first bound), 0.876 (second bound) and 0.091 ((A4) with the new $c_\rho$).
[[VERBATIM final.md 883-938]]
*Step 8 (division by $Y$; the constants).*

* *The $C_AX$ coefficient.* Step 6 already gives $|{\rm Re}\,X|\le\mathcal E_{\rm tot}$; here $X=X_w$ of Def. D6. This uses (i)–(iv) only.
* For $\delta_Y\le\frac12$: $|1/Y|\le2$ and $|p_{\rm opp}-X|=|X||1-Y|/|Y|\le2|X|\delta_Y$. Hence
$$|{\rm Re}\,p_{\rm opp}|\le\mathcal E_{\rm tot}+2(C_{X1}L+C_{X0})\delta_Y,\qquad\Big|{\rm Im}\,p_{\rm opp}+\frac L\pi\Big|\le C_{IX}+2(C_{X1}L+C_{X0})\delta_Y .$$
* *Size of the error terms* with the chosen $K$, writing $r:=a_{\max}/a_{\min}$ (note $a/a_{\min}=r^{1/2}\le r$):
  * $\mathcal E_1,\mathcal E_8\le C\,r\,\varepsilon^{1/2}L_B^2$;
  * $\mathcal E_2,\mathcal E_3,\mathcal E_4,\mathcal E_6,\mathcal E_7\le C\varepsilon^{1/2}(1+L_B)$;
  * $\mathcal E_5\le\frac{2c_\rho}{\pi^2}m^\flat_B\,r\,\varepsilon(1+2L)^2\le\frac{22.4\,c_\rho}{\pi^2}m^\flat_B\,r\,\varepsilon^{1/2}$, using $\varepsilon(1+2L)^2\le11.2\,\varepsilon^{1/2}$ for $\varepsilon\le\frac1{16}$ (the supremum of $\varepsilon^{1/2}(1+2L)^2$ is 11.12).
* Hence $\mathcal E_{\rm tot}\le C_E\varepsilon^{1/2}(1+L_B)^2$ and $\delta_Y\le C_N\varepsilon^{1/2}(1+L_B)^2$, with
$$C_E:=\frac1{\pi^2}\big[24m_Am^\flat_Br+825m^\flat_B+1667m^\flat_Am^\flat_B+22.4\,c_\rho m^\flat_Br\big]+\frac4\pi m_Ar,$$
$$C_N:=\frac1{\pi^2}\big[48m_Am^\flat_Br+1650m^\flat_B+3243m^\flat_Am^\flat_B\big].$$
  $C_E$ depends on $\bar n_A$ and $(\lambda_A/\mu_A)^2$ through $c_\rho$ (Step 1, (A4)).
* *A monotonicity lemma.* Put $c:=1+\ell_B$. For $\varepsilon\le\frac1{16}$,
$$\varepsilon^{1/2}(1+L_B)^2\le\frac{c^2}4\ \Big(\le3+\ell_B^2\Big),\qquad\varepsilon^{1/2}(1+L_B)^2L\le\frac2e\,c^2+\frac{16}{e^2}\,c+\frac{54}{e^3}\le0.736\,c^2+2.166\,c+2.689 .$$
  *Proof.* With $t:=\varepsilon^{-1/2}\ge4$ and $x:=\lambda_B/\mu_B\ge1$, $\varepsilon^{1/2}(1+L_B)^2=(1+\ln(1+4tx))^2/t=:f(t)$, and $t^2f'(t)/(1+\ln(1+4tx))=8tx/(1+4tx)-1-\ln(1+4tx)<2-1-\ln17<0$. So $f$ decreases in $t$, and its maximum over $t\ge4$ is $f(4)=(1+\ln(1+16x))^2/4=c^2/4$. Also $(1+\ell)^2/4\le3+\ell^2$ since $3\ell^2-2\ell+11>0$. For the second bound, $1+L_B\le c+L/2$ (because $1+4\varepsilon^{-1/2}x\le\varepsilon^{-1/2}(1+4x)$), so $\varepsilon^{1/2}(1+L_B)^2L\le e^{-L/2}L(c+L/2)^2=e^{-L/2}(c^2L+cL^2+L^3/4)$, and $\sup_Le^{-L/2}L^k=(2k/e)^k$ gives $2/e$, $16/e^2$, $216/e^3$. (Checked in `final2_logs/final2_constants.log`.) $\square$
* *Final constants* (Fix 7(a): $\mathcal E_{\rm tot}$ is replaced by its bound wherever it occurs inside a constant). Put
$$C_{X0}:=\frac12+C_E\frac{c^2}4+\frac{m^\flat_B}{\pi^2}\big[3\ell_B^2+206(1+\ell_B)\big]+\frac{m^\flat_A}{\pi}\Big(\ell_A+\frac12\Big),\qquad C_{X1}:=\frac{m^\flat_A}{2\pi}+\frac{m^\flat_B(1+\ell_B)}{\pi^2},$$
$$C'_{IX}:=\frac1\pi\ln\frac{8a_{\max}}{a_{\min}}+\frac{m^\flat_B}{\pi^2}\big[3\ell_B^2+208(1+\ell_B)\big]+\frac4{\pi^2}m_B+\frac1\pi\Big[2m_A+m^\flat_A\Big(\ln\frac{a_{\max}}{a_{\min}}+\ell_A+\frac12\Big)\Big]+C_E\frac{c^2}4 ,$$
  so that $|X|\le C_{X1}L+C_{X0}$ and $|{\rm Im}\,X+L/\pi|\le C'_{IX}$ (Step 7, with $|R_{\mathsf S}|$ and $|R_{\rm out}|$ inserted and $\mathcal E_{\rm tot}\le C_Ec^2/4$). Then
$$C_T:=C_E+2C_N(C_{X1}+C_{X0}),\qquad C_I:=C'_{IX}+2C_N\Big[C_{X1}\big(0.736\,c^2+2.166\,c+2.689\big)+C_{X0}\frac{c^2}4\Big].$$
  Indeed $|{\rm Re}\,p_{\rm opp}|\le C_E\varepsilon^{1/2}(1+L_B)^2+2(C_{X1}L+C_{X0})C_N\varepsilon^{1/2}(1+L_B)^2\le C_T\varepsilon^{1/2}(1+L_B)^2(1+L)$, and $|{\rm Im}\,p_{\rm opp}+L/\pi|\le C'_{IX}+2C_N\big[C_{X1}\varepsilon^{1/2}(1+L_B)^2L+C_{X0}\varepsilon^{1/2}(1+L_B)^2\big]\le C_I$ by the monotonicity lemma. The constants are polynomials in the quantities listed in (a); $C_I$ contains $\ln(a_{\max}/a_{\min})$. This proves (a). (b) follows from (a) and the status of the hypotheses (Def. D2, D3; §2.2). $\square$

[[VERBATIM final.md 954-961]]
**Numerics (scalar spectator model, §14; general jets).**

* *Base set* (both jets on $\mathcal N$): ${\rm Re}\,p_{\rm opp}=0.0123,\ 0.00205,\ 0.00035$ at $\lambda=0.01,0.003,0.001$. Methods I and II agree to $10^{-5}$.
  * Independent reviewer values: $0.012347,\ 0.002048,\ 0.000345$, and $0.0000436$ at $\lambda=0.0003$ (round 1); $0.0123468,\ 0.0020501,\ 0.0003476$ (round 3).
  * $N/N_0=0.99843,\ 0.99987,\ 0.99998$.
  * ${\rm Im}\,p_{\rm opp}+\frac1\pi\ln\frac1\varepsilon=+0.036,\ +0.040,\ +0.041$ at $\varepsilon=1.17\times10^{-3},1.05\times10^{-4},1.17\times10^{-5}$: bounded and converging, as stated.
* *Non-factorized jet pairs* (round-3 reviewer, `review_r3_1_logs/t2_general.log`; re-fit in the final review and in `final2_logs/t2_numerics_refit.log`):
  * over two decades ${\rm Re}\,p_{\rm opp}$ decays as $\varepsilon^{0.63}$ (pair 2), $\varepsilon^{0.70}$ (pair 1) and $\varepsilon^{0.73}$ (pair 0); the scalar base set gives $\varepsilon^{0.78}$. $N/N_0\to1$;
  * the first-decade slopes of ${\rm Im}\,p_{\rm opp}$ are 0.680 (pair 2), 0.696 (pair 1) and 0.717 (pair 0) per decade of $\varepsilon$, against the asymptotic $(1/\pi)\ln10=0.733$;
  * ${\rm Im}\,p_{\rm opp}+L/\pi$ at the smallest $\varepsilon$ is $-0.08$, $-0.21$ and $+0.70$ for pairs 0, 1, 2;
  * pair 2 has a $J_A$ that violates (ADJ), consistent with T2 requiring (ADJ) only of $J_B$.
* *Normalization* (`final2_logs/t2_numerics_refit.log`, parts (2), (3)). ${\rm Re}\,p_{\rm opp}={\rm Re}(X_w/Y)$ is dominated by the cross term $-{\rm Im}\,X_w\,{\rm Im}\,Y/|Y|^2$, which is of order $L\,|{\rm Im}\,Y|$. The $C_AX$ coefficient ${\rm Re}\,X_w$ itself is much smaller:
  * base set: ${\rm Re}\,X_w=2.6\times10^{-4},\ 3.0\times10^{-5},\ 0.9\times10^{-6}$ (printed-digit uncertainty at most $0.9\times10^{-6}$) against ${\rm Re}\,p_{\rm opp}=1.2\times10^{-2},\ 2.1\times10^{-3},\ 3.5\times10^{-4}$;
  * pairs 0 and 1: $|{\rm Re}\,X_w|\le1.3\times10^{-4}$ at $\varepsilon\approx9\times10^{-3}$, and below the printed-digit uncertainty ($\approx8\times10^{-6}$) at $\varepsilon\approx9\times10^{-5}$; pair 2: $7.7\times10^{-3},\ 1.4\times10^{-3},\ 2.1\times10^{-4}$.
* *Robustness.* ${\rm Re}\,p_{\rm opp}$ is insensitive to an $A$-side $k^-$ form factor $\Lambda^2/(k^2+\Lambda^2)$: at $\lambda=0.003$ it is $0.00205\to0.00267$ for $\Lambda=\infty\to0.03$, while ${\rm Im}\,p_{\rm opp}$ moves from $-2.875$ to $-2.367$. The vanishing of the real part is robust; the $O(1)$ imaginary constant depends on the scheme.

**Physical reading (scope restricted).**

* *What T2 shows.* Within App O's framework, in $\mathbb M_{\rm glob}$, pointwise on $\mathcal N_A\cap\mathcal N_B$, at $O(g^4)$ and for this pattern: the $C_AX$ part of the side sum of the **uncut** direct lines cancels once the window is combined with the adjacent near-shell region of the same uncut lines. This is the uncut-line part of what `asm:appO-mixing`(c) prescribes.
* *What it does not show.* The cut contributions of the direct lines, which belong to $\mathcal G_0$ and to the "含实发射" clause, are not included (Remark C). In the unregulated model they are not expected to be power suppressed. So T2 does **not** establish that the $\mathcal G_0$-restricted complete-set clause holds.
* *Conditions.* The physical content is conditional on `asm:appO-collinear-ends`. With the in-window class-$\mathfrak X_1$ $k^+$ regulator alone the uncut-line statement is proved on $\mathcal N_B$ (T2′(a)); with two-sided in-window regulators it is numerics [P] for one jet pair (T2′(c)).
* *Relation to the reference.* The reference expects, in three places, that within $\mathcal G_0$ the $O(\chi^2)$ residual should not be expected to vanish (ERR-S1b, §12). T2 contradicts this expectation **for the uncut-line part, pointwise**: on $\mathcal N_A\cap\mathcal N_B$ in the unregulated $\mathbb M_{\rm glob}$ (T2(a)), or on $\mathcal N_B$ with the in-window class-$\mathfrak X_1$ $k^+$ regulator (T2′(a)). Off $\mathcal N_A$ the unregulated uncut side sum keeps the non-zero end-pole term of T2′(b) (e.g. ${\rm Re}\,p_{\rm opp}\to0.2517$ for the apole set). The reference's remark concerns the spectator-integrated statement. That statement holds here only under `asm:appO-collinear-ends` (in-window regulators) and only on the part of spectator phase space where at least one NF condition holds; the rest is OPEN-2. T2 does not refute `asm:appO-mixing`(c), which concerns the complete set.
* *Consistency check.* P3: two-particle unitarity of box plus crossed box for exact on-shell lines.
* *Three-gluon-vertex graphs.* They are not needed for the uncut-line cancellation; their own sum is not computed. If the complete-set clause holds, then the cut direct lines and the three-gluon-vertex graphs must together have zero net Hermitian $C_AX$ part.

[[VERBATIM final.md 984-988]]
**Grades.** [P] as a QCD statement (model theorem): (a) has a complete model-internal proof; (b) is an implication [R, R_cond: `asm:appO-lcopt`, `asm:appO-adjacent-swap`, `asm:appO-real-jets`] with content grade [P]; the physical reading (c) is [P], conditional on `asm:appO-collinear-ends` and OPEN-13.

**Novelty (restricted; no marker).**

* *Prior art.* The physical $O(\alpha_s^2)$ cancellation for this fully coincident SS pattern was shown by explicit two-loop calculations in models with a spectator in each hadron: Lindsay, NPB 231 (1984) 397 (meson + meson, Feynman gauge, all graphs), and Brandt–Frenkel–Taylor, NPB 312 (1989) 589 (eikonal "mesons"). Lindsay–Ross–Sachrajda are not prior art for this pattern: they treat quark + hadron, with no $A$-side spectator. The reggeization reading is textbook (Lipatov; Kuraev–Lipatov–Fadin; Rothstein–Stewart).
* *Ours.* The derivation for general LCOPT jets inside App O's framework with explicit estimates; the ray-identity mechanism; the regulator analysis (T2′). This extends ERR-S1 from eikonal lines to composite LCOPT spectators.

### Proposition T2′ (regulated version; end poles; two-sided regulators) — [P]

*Label:* `prop:appO-twoexch-regulated`. Grade: [P] as a QCD statement (model theorem, LA-2): (a) and (b) have complete model-internal proofs; (c) is numerical. QCD transfer as in T2(b).

**First sentence (printed).** 「在全局两时模型 $\mathbb M_{\rm glob}$ 中、$O(g^4)$ 阶，对振幅侧全重合 SS 对的两条未割线，在下列各项所述的假设之下：……」

The regulated statement (a) is the main physical form for the fully coincident pattern.

**(a) Class-$\mathfrak X_1$ $k^+$ regulator (model-internal; complete proof).**

*Hypotheses.*

* (i) $\mathbb M_{\rm glob}$ with exact connecting propagators and the regulator $\prod_e\chi(k_e^+)$, $\chi\in\mathfrak X_1$ at scale $K_c$ (Def. D8).
* (ii′) $J_A$ satisfies (SEC) and (EQ). $J_B$ satisfies (SEC), (EQ), (ADJ), (REAL). (No (REAL) for $J_A$.)
* (iii′) The configuration lies in $\mathcal N_B$. (No condition on the final energies of $J_A$.)
* (iv′) $16\lambda_B\le K_c\le a_{\min}/(2\lambda_A)$. Put
$$K:=(\lambda_BK_c)^{1/2},\qquad\eta:=(\lambda_B/K_c)^{1/2}=\frac{\lambda_B}K=\frac K{K_c}\le\frac14,\qquad\zeta:=\frac{\lambda_AK_c}{a_{\min}}\le\frac12,\qquad l_K:=\ln\Big(1+\frac{4K}{\mu_B}\Big).$$
* (v′) $\delta^\chi_Y\le\frac12$, with $\delta^\chi_Y$ given below.

*Conclusion.* With $X^\chi:=p^\chi_{\rm opp}N^\chi/N_0$ (the $C_AX$ coefficient in the normalization $N_0$, Def. D6) and $Y^\chi:=N^\chi/N_0$,
$$|{\rm Re}\,X^\chi|\le\mathcal E^\chi_{\rm tot},\qquad|Y^\chi-1|\le\delta^\chi_Y,\qquad|{\rm Re}\,p^\chi_{\rm opp}|\le\mathcal E^\chi_{\rm tot}+2C^\chi_X\,\delta^\chi_Y,$$
where
$$\mathcal E^\chi_{\rm tot}:=\frac1{\pi^2}\Big\{\eta(1+l_K)\big[833m^\flat_B+6668m^\flat_Am^\flat_B\big]+\eta^2(1+l_K)^2\big[5000.5\,m^\flat_B+16m^\flat_Am^\flat_B\big]+48m_Am^\flat_B\,\zeta\eta\,l_K^2+8c_\rho m^\flat_B\,\zeta\eta^2\Big(1+2\ln\frac1{4\zeta\eta^2}\Big)^2\Big\}+\frac1\pi\Big[3\eta+20m_A\zeta+2(1+m^\flat_A)\zeta^2\Big],$$
$$\delta^\chi_Y:=\frac1{\pi^2}\Big\{\eta(1+l_K)\big[1650m^\flat_B+12972m^\flat_Am^\flat_B\big]+5001\,m^\flat_B\,\eta^2(1+l_K)^2+96m_Am^\flat_B\,\zeta\eta\,l_K^2\Big\},$$
$$C^\chi_X:=\frac12+\mathcal E^\chi_{\rm tot}+\frac{m^\flat_B}{\pi^2}\Big[3\ell_B^2+206(1+\ell_B)+2(1+\ell_B)\ln\frac1{3\eta}\Big]+\frac{m^\flat_A}\pi\Big(4\ln\frac1\eta+\frac12\Big),$$
and $c_\rho$ is the constant of (A4) (T2, Step 1). In particular ${\rm Re}\,X^\chi=O\big(\eta(1+l_K)^2+\zeta(1+\ln\frac1\zeta)^2\big)$ and ${\rm Re}\,p^\chi_{\rm opp}=O\big(\eta(1+l_K)^2(1+\ln\frac1\eta)+\zeta(1+\ln\frac1\zeta)^2\big)$, with constants depending on the jet constants (the logarithm of $1/\zeta$ comes from the term $\zeta\eta^2(1+2\ln\frac1{4\zeta\eta^2})^2$, since $\eta^2\ln^2\frac1\eta$ is bounded). This is the final report's rate "$O((\lambda_B/K_c)^{1/2}+K_c\lambda_A/a)$ up to logarithms", now with explicit hypotheses, explicit logarithms and explicit constants.

*Mirror statement.* With a class-$\mathfrak X_1$ regulator on the $A$-side minus components at a scale $K_c^-$ with $16\lambda_A\le K_c^-\le a_{\min}/(2\lambda_B)$, on $\mathcal N_A$, with (ADJ), (REAL) imposed on $J_A$ and (SEC), (EQ) on $J_B$, the same bounds hold with $A\leftrightarrow B$ (same proof, with the $k^-$ contour rotated).

*Proof.*

*Step 0$^\chi$ (rotation, regulator, regions).* L5 holds with class-$\mathfrak X$ regulators: $\chi$ is holomorphic on the swept sets (first quadrant for $x_e>0$, third for $x_e<0$) and bounded by 2, so Steps 1–4 of L5 go through, and $F_A$ is holomorphic there without any condition on $J_A$ (L5, Step 1). At $\theta=\pi/2$,
$$X^\chi=-\frac1{\mathcal J_B}\int(h_{12}f_{21}+h_{21}f_{12})\,\Xi\,\frac{d^2\kappa}{(2\pi)^2},\qquad Y^\chi=-\frac1{\mathcal J_B}\int(h_{12}+h_{21})S_B\,\Xi\,\frac{d^2\kappa}{(2\pi)^2},\qquad\Xi(\kappa):=\hat\chi(\kappa_1)\hat\chi(\kappa_2),$$
with $\hat\chi(\kappa):=\chi(i\kappa)$ continued in the quadrant of the sign of $\kappa$. On the imaginary axis the class bounds give $|\hat\chi-1|\le|\kappa|/K_c$ ($|\kappa|\le K_c$), $|\hat\chi|\le K_c/|\kappa|$ ($|\kappa|\ge K_c$), $|\hat\chi|\le2$ and $|\hat\chi'(\kappa)|\le K_c^{-1}\min(1,K_c^2/\kappa^2)$. Hence $|\Xi|\le4$, $|\Xi-1|\le3R/K_c$ for $R\le K_c$, and $|\Xi|\le1+3\eta\le2$ on $\mathsf S$. Put $\psi(k):=\chi_+(k)\chi_-(-k)$, where $\chi_\pm$ are the two half-line branches. $\psi$ is holomorphic in the closed first quadrant ($-k$ then lies in the closed third quadrant), real on $k>0$, $\psi(0)=1$, $|\psi(k)-1|\le3|k|/K_c$ for $|k|\le K_c$, $|\psi(k)|\le K_c^2/|k|^2$ for $|k|\ge K_c$, and $|\psi|\le4$. On the strip diagonal, $\Xi(-\kappa,\kappa)=\Xi(\kappa,-\kappa)=\psi(i\kappa)$ for $\kappa>0$. The regions $\mathsf S$, $\mathsf T_\pm$, $\mathsf O$ are those of T2 with $K=(\lambda_BK_c)^{1/2}$. By (iv′), $K\ge4\lambda_B$ and $K=\eta K_c\le K_c/4\le a_{\min}/(8\lambda_A)$, so (A1) applies on $\mathsf S$. Also $\lambda_AK/a_{\min}=\zeta\eta$, $\lambda_B/K=\eta$, and $\lambda_A\lambda_B/a_{\min}=\zeta\eta^2$.

*Step 1$^\chi$ ($A$-side).* (A1), (A2), the two bounds of (A3) on the imaginary axis ($|\varrho_{12}(\kappa)-1|\le4m_A\lambda_A\kappa/a_{\min}$ for $\kappa\le a_{\min}/(2\lambda_A)$, and $|\varrho_{12}|\le m^\flat_A$) and (A4) hold for real energies of either sign and use no reality property: on the imaginary axis $|A+K|\ge\max(|A|,|K|)$ for every real $A$. In T2, $\mathcal N_A$ and (REAL) for $J_A$ enter only through the pole-free ray identity for $\varrho_{12}$, $\varrho_{21}$ in Step 6. That step is replaced by Step 6$^\chi$ below.

*Step 2$^\chi$.* L8 and L8(i) apply to $J_B$ ($\mathcal N_B$, (ADJ)), with $\lambda_B$, $\mu_B$, $M^\flat_B$.

*Step 3$^\chi$ (inner square).* By (A1),
$$-\frac1{\mathcal J_B}\int_{\mathsf S}(h_{12}f_{21}+h_{21}f_{12})\Xi=-\frac1{\mathcal J_B}\int_{\mathsf S}\Big[\tfrac12S_B-v\Delta_B\Big]\Xi+P^\chi_1,\qquad|P^\chi_1|\le2\mathcal E_1(K)=\frac{48}{\pi^2}m_Am^\flat_B\,\zeta\eta\,l_K^2,$$
since $|\Xi|\le2$ on $\mathsf S$.

* *The $S_B$ term.* $-\frac1{2\mathcal J_B}\int_{\mathsf S}S_B\Xi=\frac12+T_{\rm tail}+Q_1$ with $|T_{\rm tail}|\le\mathcal E_2=\frac{825}{\pi^2}m^\flat_B\eta(1+l_K)$ (T2, Step 3) and
  $$Q_1:=-\frac1{2\mathcal J_B}\int_{\mathsf S}S_B(\Xi-1)\frac{d^2\kappa}{(2\pi)^2},\qquad|Q_1|\le\frac{3}{8\pi^2K_c|\mathcal J_B|}\int_{R\le K}R|S_B|\le\frac{3}{8\pi^2}m^\flat_B\eta^2\Big[96l_K^2+6572(1+l_K)\ln\frac1{4\eta}\Big]\le\frac{2500.5}{\pi^2}m^\flat_B\eta^2(1+l_K)^2,$$
  by L8(i3) with $X=K$ and $\ln(K/4\lambda_B)=\ln(1/4\eta)\le l_K$.
* *The $v$ term.* $\frac1{\mathcal J_B}\int_{\mathsf S}v\Delta_B\Xi=V_{\mathsf S}+Q_2$, where $V_{\mathsf S}$ is the unregulated term of T2 (purely imaginary by (REAL) of $J_B$, T2 Step 3) and $Q_2:=\frac1{\mathcal J_B}\int_{\mathsf S}v\Delta_B(\Xi-1)\frac{d^2\kappa}{(2\pi)^2}$. Two geometric integrals are used. For fixed $R$, the set $\max(|\kappa_1|,|\kappa_2|)=R$ is the boundary of a square, on which $\min(|\kappa_1|,|\kappa_2|)=|u|$ with $u$ running over $[-R,R]$ on each of the four sides. Hence $\int_{4\lambda<R\le K}d^2\kappa/(R\langle\min(r_1,r_2)\rangle)=\int_{4\lambda}^K\frac{dR}R\,8\,{\rm asinh}\frac R\mu\le8\,l_K\ln\frac K{4\lambda}$. In the strip, $\frac34R\le|\kappa_2|\le R$ and $|\kappa_P|<R/4\le|\kappa_2|/3$, so in the unit-Jacobian variables $(\kappa_P,\kappa_2)$, $\int_{\rm strip,\,4\lambda<R\le K}d^2\kappa/(R\langle r_P\rangle)\le2\int_{3\lambda}^K\frac{d\kappa_2}{\kappa_2}\int_{|\kappa_P|\le\kappa_2/3}\frac{d\kappa_P}{\langle\kappa_P\rangle}\le4\,l_K\ln\frac K{3\lambda}$. (Both checked numerically in `final2_logs/final2_constants.log`.) Split $\mathsf S$ into three parts:
  * $\{R\le4\lambda_B\}$: $|v|\le\frac12$, $|\Xi-1|\le12\lambda_B/K_c=12\eta^2$, and $\int_{R\le4\lambda_B}|\Delta_B|\le24M^\flat_B\ell_B^2$ (L8(g), first bullet, both orders). Contribution at most $\frac{36}{\pi^2}m^\flat_B\eta^2\ell_B^2$.
  * the off-strip part of $\{4\lambda_B<R\le K\}$: $|v|\le\frac12$, $|\Xi-1|\le3R/K_c$, and $|\Delta_B|\le800M^\flat_B\lambda_B/(R^2\langle\min(r_1,r_2)\rangle)$ (L8(c), both orders). Contribution at most $\frac1{4\pi^2}\cdot\frac12\cdot\frac3{K_c}\cdot800m^\flat_B\lambda_B\cdot8l_K\ln\frac K{4\lambda_B}=\frac{2400}{\pi^2}m^\flat_B\eta^2l_K\ln\frac1{4\eta}$.
  * the strip part of $\{4\lambda_B<R\le K\}$: there $v=\pm\frac12$ (quadrants $(-,+)$ and $(+,-)$) and $\Delta_B=2g(-i\kappa_P)/\kappa_2+E_{12}-E_{21}$ (L8(d)), so $v\Delta_B=g(-i\kappa_P)/|\kappa_2|+v(E_{12}-E_{21})$; and $|\Xi-1|\le3R/K_c\le4|\kappa_2|/K_c$. The $g$-part is at most $\frac1{4\pi^2}\cdot\frac4{K_c}\cdot2K\cdot4m^\flat_B(1+\ell_B)=\frac8{\pi^2}m^\flat_B\eta(1+\ell_B)$, by L8(i4) and $|\kappa_2|\le K$. The $E$-part is at most $\frac1{4\pi^2}\cdot\frac12\cdot\frac4{K_c}\cdot2\cdot16m^\flat_B\lambda_B\cdot4l_K\ln\frac K{3\lambda_B}=\frac{64}{\pi^2}m^\flat_B\eta^2l_K\ln\frac1{3\eta}$.

  With $\ell_B\le l_K$ and $\ln\frac1{4\eta}<\ln\frac1{3\eta}\le\ln\frac{4K}{\lambda_B}\le l_K$:
  $$|Q_2|\le\frac{m^\flat_B}{\pi^2}\Big[8\eta(1+l_K)+2500\,\eta^2l_K^2\Big].$$

*Step 4$^\chi$ (strips).* In $\mathsf T_+$, $h_{12}f_{21}\Xi=\rho^\chi[-g(-i\kappa_P)/\kappa_2+E_{21}]$ with $\rho^\chi:=\rho\,\Xi$ and $|\rho^\chi|\le4m^\flat_A$. The $E$-part, over both strips, is at most $4\mathcal E_4$. As in T2, the main part is
$$\frac1{\mathcal J_B}\int_{\mathsf T_+}\rho^\chi g\,\kappa_2^{-1}\frac{d^2\kappa}{(2\pi)^2}=-\frac i{2\pi}\int_K^\infty\frac{d\kappa}\kappa\,\varrho_{12}(\kappa)\psi(i\kappa)+P^\chi_5+P^\chi_6+P^\chi_7,$$
with $|P^\chi_6|\le4\mathcal E_6$ and $|P^\chi_7|\le4\mathcal E_7$ over both strips ($|\rho^\chi(-\kappa_2,\kappa_2)|\le4m^\flat_A$). For the variation across the strip, $\partial_1\rho^\chi=(\partial_1\rho)\Xi+\rho\,\hat\chi'(\kappa_1)\hat\chi(\kappa_2)$. On the strip $|\kappa_1|\ge\frac23\kappa_2$, so $|\hat\chi'(\kappa_1)|\le K_c^{-1}\min\big(1,(3K_c/(2\kappa_2))^2\big)$. With (A4) and L8(i4) (first moment, with $X=\kappa_2/3\ge\lambda_B$), $|P^\chi_5|\le4\mathcal E_5+P'_5$, where
$$P'_5:=\frac{2}{4\pi^2}\cdot2m^\flat_A\cdot\frac{4m^\flat_B\lambda_B}{K_c}\int_K^\infty\frac{d\kappa_2}{\kappa_2}\min\Big(1,\Big(\frac{3K_c}{2\kappa_2}\Big)^2\Big)\Big(1+2\ln\frac{\kappa_2}{3\lambda_B}\Big)\le\frac4{\pi^2}m^\flat_Am^\flat_B\,\eta^2(1+u_c)^2\le\frac{16}{\pi^2}m^\flat_Am^\flat_B\,\eta^2(1+l_K)^2 .$$
Here $u_c:=\ln(K_c/2\lambda_B)=\ln(1/2\eta^2)$. The $\kappa_2$-integral is at most $\frac14[(1+2u_c)^2-1]+(1+u_c)=(1+u_c)^2$, because the head, from $\kappa_2=K$ (where $\ln(K/3\lambda_B)>0$) to $3K_c/2$, gives at most $\frac14[(1+2u_c)^2-1]$, and the tail gives $\int_0^\infty e^{-2v}(1+2u_c+2v)dv=1+u_c$. Finally $1+u_c\le1+2\ln(1/\eta)\le2(1+l_K)$. In $4\mathcal E_5=\frac{8c_\rho}{\pi^2}m^\flat_B\frac{\lambda_A\lambda_B}{a_{\min}}(1+2\ln\frac{\kappa_*}{\lambda_B})^2$ one has $\lambda_A\lambda_B/a_{\min}=\zeta\eta^2$ and $\kappa_*/\lambda_B=1/(4\zeta\eta^2)$; the bound of T2 applies because $\kappa_*\ge K_c/2\ge8\lambda_B$. Adding $\mathsf T_-$ gives the outer contribution
$$p^{\chi,\rm out}_{\rm opp}:=-\frac i{2\pi}\int_K^\infty\frac{d\kappa}\kappa\big[\varrho_{12}(\kappa)+\varrho_{21}(\kappa)\big]\psi(i\kappa).$$

*Step 5$^\chi$ (off-strip).* $|P^\chi_{\mathsf O}|\le4\mathcal E_3$ (T2, Step 5, with $|\Xi|\le4$).

*Step 6$^\chi$ (real part of the outer contribution: the ray identity for the regulator).*
$${\rm Re}\,p^{\chi,\rm out}_{\rm opp}=\frac1{2\pi}\int_K^\infty\frac{d\kappa}\kappa{\rm Im}\big[(\varrho_{12}+\varrho_{21})\psi\big](i\kappa)=\frac1\pi\int_K^\infty\frac{d\kappa}\kappa{\rm Im}\,\psi(i\kappa)+Q_4,\qquad Q_4:=\frac1{2\pi}\int_K^\infty\frac{d\kappa}\kappa{\rm Im}\big[(\varrho_{12}-1+\varrho_{21}-1)\psi\big](i\kappa).$$

* L6 applies to $\psi$ (holomorphic in the closed first quadrant with no poles, real on $k>0$, $\psi(0)=1$, $|\psi-1|\le3|k|/K_c$ for $|k|\le K_c$, $|\psi|\le K_c/|k|$ for $|k|\ge K_c$). So $\int_0^\infty\frac{d\kappa}\kappa{\rm Im}\,\psi(i\kappa)=-\frac\pi2$ **exactly**. Hence $\frac1\pi\int_K^\infty=-\frac12+Q_3$ with $Q_3:=-\frac1\pi\int_0^K\frac{d\kappa}\kappa{\rm Im}\,\psi(i\kappa)$ and $|Q_3|\le\frac1\pi\int_0^K\frac{3}{K_c}d\kappa=\frac3\pi\eta$. (For the example of D8, $\psi(i\kappa)=(1+i\kappa/K_c)^{-2}$ and the integral is $-\pi/2$ symbolically; `final2_logs/final2_constants.log`.)
* Put $\kappa':=a_{\min}/(2\lambda_A)\ge K_c$. Using $|\psi|\le4$ for $\kappa\le K_c$ and $|\psi|\le(K_c/\kappa)^2$ above, $|\varrho-1|\le4m_A\lambda_A\kappa/a_{\min}$ for $\kappa\le\kappa'$ and $|\varrho-1|\le1+m^\flat_A$ always, for each mixed sector
  $$\int_K^\infty\frac{d\kappa}\kappa|\varrho-1||\psi|\le16m_A\zeta+4m_A\zeta+2(1+m^\flat_A)\zeta^2,$$
  so $|Q_4|\le\frac1\pi\big[20m_A\zeta+2(1+m^\flat_A)\zeta^2\big]$.

So ${\rm Re}\,p^{\chi,\rm out}_{\rm opp}=-\frac12+Q_3+Q_4$. Neither $\mathcal N_A$ nor (REAL) for $J_A$ has been used: the $-\frac12$ comes from the regulator, and the $A$-jet enters only through (A1)–(A4) on the imaginary axis.

*Step 7$^\chi$ (collecting; normalization; division).*

* $X^\chi=\frac12+T_{\rm tail}+Q_1+V_{\mathsf S}+Q_2+P^\chi_1+p^{\chi,\rm out}_{\rm opp}+P^\chi_5+P^\chi_6+P^\chi_7+P^\chi_E+P^\chi_{\mathsf O}$, and ${\rm Re}\,V_{\mathsf S}=0$. Hence $|{\rm Re}\,X^\chi|$ is at most the sum of the bounds on $T_{\rm tail}$, $Q_1$, $Q_2$, $P^\chi_1$, $Q_3$, $Q_4$, $P^\chi_5$, $P^\chi_6$, $P^\chi_7$, $P^\chi_E$, $P^\chi_{\mathsf O}$. Collecting terms gives $\mathcal E^\chi_{\rm tot}$. The coefficient of $\eta(1+l_K)$ is $825+8$ (for $m^\flat_B$) and $6400+172+64+32=6668$ (for $m^\flat_Am^\flat_B$; $4\mathcal E_3$, $4\mathcal E_4$, $4\mathcal E_6$, $4\mathcal E_7$ with $1+2l_K\le2(1+l_K)$). The coefficient of $\eta^2(1+l_K)^2$ is $2500.5+2500$ (for $m^\flat_B$; $Q_1$, $Q_2$) and $16$ (for $m^\flat_Am^\flat_B$; $P'_5$). (`final2_logs/final2_constants.log`.)
* *Normalization.* The same steps with $h_{12}+h_{21}$ give $Y^\chi=1+2T_{\rm tail}+2Q_1+(\text{inner }e\text{-terms})+(\text{strip }E\text{-terms})+(\text{off-strip})$. The inner $e$-terms are bounded by $4\mathcal E_1(K)$, using $|e_{12}+e_{21}|\le8m_A\zeta\eta$ on $\mathsf S$ and $|\Xi|\le2$. In the strips $(h_{12}+h_{21})S_B\Xi=\rho^\chi(E_{12}+E_{21})$, because the $g$-terms cancel, which gives $4\mathcal E_4$. Off the strip the bound is $8\mathcal E_3$. In total $|Y^\chi-1|\le4\mathcal E_1+2\mathcal E_2+2\bar Q_1+8\mathcal E_3+4\mathcal E_4=\delta^\chi_Y$, with $\bar Q_1$ the bound on $|Q_1|$.
* *$|X^\chi|$.* $|X^\chi|\le\frac12+\mathcal E^\chi_{\rm tot}+|V_{\mathsf S}|+|p^{\chi,\rm out}_{\rm opp}|$, with $|V_{\mathsf S}|$ bounded as in T2 Step 7 ($K/3\lambda_B=1/3\eta$) and $|p^{\chi,\rm out}_{\rm opp}|\le\frac{m^\flat_A}\pi\int_K^\infty\frac{d\kappa}\kappa|\psi(i\kappa)|\le\frac{m^\flat_A}\pi\big(4\ln\frac1\eta+\frac12\big)$. This is $C^\chi_X$.
* *Division.* For $\delta^\chi_Y\le\frac12$, $|p^\chi_{\rm opp}-X^\chi|\le2|X^\chi|\delta^\chi_Y$, which gives the bound on ${\rm Re}\,p^\chi_{\rm opp}$. $\square$

*Remarks on (a).*

* *Numerical confirmation of the weakened hypotheses* (`final2_scripts/t2p_general_regulated.py` → `final2_logs/t2p_general_regulated.log`). A general (non-factorized) $J_B$ of class (SEC)+(EQ)+(ADJ)+(REAL)+$\mathcal N_B$ was paired with a non-factorized $J_A$ of class (SEC)+(EQ) that violates both $\mathcal N_A$ (three positive final energies in the mixed sectors) and (REAL) (complex phases on the multi-state terms). With the example regulator of D8 at $K_c=(\lambda_Ba_{\min}/\lambda_A)^{1/2}$, at $\eta=0.32,\ 0.18,\ 0.10$: ${\rm Re}\,X^\chi=-1.36\times10^{-2},\ -7.0\times10^{-3},\ -3.0\times10^{-3}$ and ${\rm Re}\,p^\chi_{\rm opp}=0.155,\ 0.107,\ 0.064$ (grid-converged). Both decrease roughly in proportion to $\eta$. Without the regulator the same pair tends to the end-pole value of (b), $\Pi=0.1124$.
* *Scalar model* (class-$\mathfrak X$ example, $K_c=\lambda$, `logs/twoexch_regulated.log`): ${\rm Re}\,p^\chi_{\rm opp}=0.103,\ 0.054,\ 0.028$ at $\lambda=0.01,0.003,0.001$, for the base and the apole sets alike. This is about $\lambda^{1/2}$, consistent with the proven rate ($\lambda_B\propto\lambda^2$, so $\eta\propto\lambda^{1/2}$). The decay of ${\rm Re}\,p^\chi_{\rm opp}$ is carried by the normalization cross term ($1-{\rm Re}\,Y^\chi\propto\lambda$, ${\rm Im}\,Y^\chi\approx-0.10,\ -0.040,\ -0.017$). The $C_AX$ coefficient ${\rm Re}\,X^\chi=-5.1\times10^{-4},\ -1.6\times10^{-4},\ -5.4\times10^{-5}$ decays like $\lambda^{0.97}$ (`final2_logs/t2_numerics_refit.log`, part (3)). So the proven $O(\eta)$ bound on ${\rm Re}\,X^\chi$ is not sharp in this model.
* *Size of (v′).* With all jet constants 1, $\lambda_B=\mu_B$ and the $\zeta$-term dropped, $\delta^\chi_Y=1.7$ at $\eta=10^{-4}$ and $0.21$ at $\eta=10^{-5}$ (`final2_logs/final2_constants.log`). As for T2, the numerics probe the statement, not the proven bound.
* The imaginary constant remains regulator dependent.
* The real part is regulator independent only for regulators that retain the near-shell segment. If an $A$-side $k^-$ regulator at $K^-$ is added, the statement needs $K_cK^-\gg\mathbf k_T^2$; for $K^+K^-\ll\mathbf k_T^2$ the value is set by the regulators (P2; (c)).

**(b) End poles (model-internal; complete proof).**

*Hypotheses.* (i) $\mathbb M_{\rm glob}$ with exact propagators and no regulator; (ii″) $J_A$ satisfies (SEC) and (EQ), $J_B$ satisfies (SEC), (EQ), (ADJ), (REAL); (iii′) $\mathcal N_B$; (iv), (v) of T2. Define the **end-pole value**
$$\Pi:=\frac12+\frac1{2\pi}\int_0^\infty\frac{d\kappa}\kappa\,{\rm Im}\big[\varrho_{12}(\kappa)+\varrho_{21}(\kappa)\big],$$
an absolutely convergent integral on the imaginary axis ($|\varrho-1|\le4m_A\lambda_A\kappa/a_{\min}$ at small $\kappa$, $|\varrho|\le m^\flat_Aa_1a_2/(4\kappa^2\mu_A^2)$ at large $\kappa$).

*Conclusion.*

* (b1) $|{\rm Re}\,X_w-\Pi|\le\mathcal E_{\rm tot}$ and $|{\rm Re}\,p_{\rm opp}-\Pi|\le\mathcal E_{\rm tot}+2(C_{X1}L+C_{X0})\delta_Y\le C_T\varepsilon^{1/2}(1+L_B)^2(1+L)$, with the constants of T2.
* (b2) By L6, $\Pi=\frac1{2\pi}{\rm Im}\int_0^\infty\frac{dk}k(\rho_{12}+\rho_{21})(k+i0)$. (If some poles on the positive axis are multiple, the boundary-value integral is understood as $\lim_{\delta\downarrow0}\int_0^\infty dk\,\rho(k+i\delta)/(k+i\delta)$; the proof of L6 applies verbatim to the region above the line ${\rm Im}\,k=\delta$. The definition of $\Pi$ on the imaginary axis is the primary one, and (b1) does not use L6.) If $J_A$ satisfies (REAL) and the poles of $\rho_{12}$, $\rho_{21}$ on the positive axis are simple, then
$$\Pi=-\frac12\sum_p{\rm Res}_{k_p}(\rho_{12}+\rho_{21})/k_p .$$
  On $\mathcal N_A$ there are no such poles and, with (REAL), $\Pi=0$; this is T2(a).

*Proof.* (b1): the proof of T2(a) uses $\mathcal N_A$ (and (REAL) for $J_A$) only in Step 6. Steps 0–5, 7 and 8 use (A1)–(A4) and the decay bound on the imaginary axis, which need neither. In Step 6,
$${\rm Re}\,p^{\rm out}_{\rm opp}=\frac1{2\pi}\int_K^\infty\frac{d\kappa}\kappa{\rm Im}(\varrho_{12}+\varrho_{21})=\Pi-\frac12-\frac1{2\pi}\int_0^K\frac{d\kappa}\kappa{\rm Im}(\varrho_{12}+\varrho_{21}),$$
and the head is bounded by $\mathcal E_8$ as before. Hence ${\rm Re}\,X=\frac12+{\rm Re}\,p^{\rm out}_{\rm opp}+(\text{the other error terms})=\Pi+O(\mathcal E_{\rm tot})$, with the same bound. Division by $Y$ is as in Step 8. (b2): $\rho_{12}$ is rational with real poles $a_1/(2A_j)<0$ and $a_2/(2A'_j)$, so it is holomorphic in the open first quadrant. Further, $\rho_{12}(0)=1$ by (EQ); $|\rho_{12}(k)-1|\le C|k|$ on $|k|\le a_{\min}/(4\lambda_A)$, where every factor obeys $|2kA-a|\ge a/2$; and $|\rho_{12}(k)|\le C|k|^{-2}$ for $|k|\ge a_{\max}/\mu_A$, where $|2kA-a|\ge|k|\mu_A$. The poles in the closed quadrant lie on the positive axis at $k_p=a_2/(2A'_j)\in[a_{\min}/(2\lambda_A),a_{\max}/(2\mu_A)]$ for the positive final energies $A'_j$ of sector $1V2$. So L6 applies and gives the integral form. With (REAL), $\rho_{12}$ is real on the positive axis away from the poles, and for simple poles ${\rm Im}\int\rho_{12}(k+i0)dk/k=-\pi\sum_p{\rm Res}_{k_p}\rho_{12}/k_p$ (indentation above the poles). The same holds for $\rho_{21}$. $\square$

* *Which energies enter.* Only the final-gap energies of the *mixed* sectors enter: $\alpha_1$ for $1V2$ and $\alpha_2$ for $2V1$. A positive $\alpha_0$, the first final gap of the both-final sector, gives no end-pole term, because that sector does not reach the strip. (The "apole" set has $\alpha_0=0.5625\lambda^2>0$.)
* *Scalar model.* There $\rho_{12}(k)=a_1a_2/((a_1-2d_{10}k)(a_2-2\alpha_1k))$, so ${\rm Res}(\rho_{12})/k_p=-a_1\alpha_1/(a_1\alpha_1+a_2|d_{10}|)$ (verified symbolically by both round-2 reviewers and in `final_review_logs/fr_endpole_L6.log`). Hence $\Pi=+\frac12a_1\alpha_1/(a_1\alpha_1+a_2|d_{10}|)$ if $\alpha_1>0$, and $+\frac12a_2\alpha_2/(a_2\alpha_2+a_1|d_{20}|)$ if $\alpha_2>0$.
* *Location.* The poles sit at $k^+=a/(2\alpha)\sim a/\lambda_A$, the $A$-collinear end.
* *Mirror statement.* Rotating $k^-$ instead of $k^+$, valid on $\mathcal N_A$, gives the analogous end-pole formula for positive final energies of $J_B$. The case where NF fails for both jets is open (OPEN-2).
* *Interpretation.* For **massive** spectators these poles are artefacts of $\mathbb M_{\rm glob}$: exact kinematics forbids an on-shell massive spectator from absorbing an on-shell gluon, since $(s+k)^2=m_s^2$ forces $s\cdot k=0$. For **massless** partons $s\cdot k=0$ is reached for collinear $k$, so the poles are genuine $A$-collinear configurations; `asm:appO-collinear-ends` assigns them to the $A$-collinear region, or (a) removes them.
* *Numerics.*
  * apole set (method II): 0.2626, 0.2536, 0.2520 at $\lambda=0.01,0.003,0.001$, against the prediction 0.2517 (reviewer round 2: 0.25172).
  * alt set (pole in $J_B$; mirror formula; method I): 0.0692, 0.0520, 0.0490 against 0.0483 (reviewer: 0.04834). The altswap set equals alt.
  * general non-factorized pair with $J_A$ violating $\mathcal N_A$ and (REAL) (`final2_logs/t2p_general_regulated.log`): ${\rm Re}\,X_w-\Pi=8.0\times10^{-3},\ 1.8\times10^{-3},\ 3.1\times10^{-4}$ at $\varepsilon=8.8\times10^{-3},\ 8.8\times10^{-4},\ 8.8\times10^{-5}$, with $\Pi=0.1124$ computed from its definition on the imaginary axis; ${\rm Re}\,p_{\rm opp}=0.172,\ 0.127,\ 0.115$.

[[VERBATIM final.md 1032-1047]]
**Novelty.** Ours (no marker): the end-pole formula and its general form $\Pi$, the regulated proof with explicit hypotheses and constants, and the two-sided regulator study, as model statements.
[[VERBATIM final.md 1049-1049]]
### Proposition P2 (the strict window and its regulator-shape dependence) — [R, R_PT]

*Label:* `prop:appO-strict-window-shape`. Qualifier (outline): 「（$R_{\rm PT}$：在 $O(g^4)$ 对所述局域化积分严格。）」 (a statement about explicitly defined localized integrals with regulators, with no unproven input).
[[VERBATIM final.md 1051-1090]]
**Novelty.** (a) is the reference's (Lemma E.48(d); `lem:appO-joint-localization`(c)). The formula (b) and the classification (c) are ours (elementary; no marker).
[[VERBATIM final.md 1092-1092]]
### Proposition P3 (on-shell lines) — content [R, R_PT] at $O(g^4)$; known in substance

*Printed as* the untagged remark `rem:appO-onshell-unitarity` (FINAL_OUTLINE_v2, slot X1f; a remark carries a tag only if the outline gives one, WRITER_SPEC_v2 §4.1). The content is 本书给出的推导 of an instance of Cutkosky's rules.
[[VERBATIM final.md 1094-1104]]
### Proposition P4 (per-graph weights of a fully coincident pair are not fixed by window data) — [P]

*Label:* `prop:appO-pergraph-weights`. Grade: [P] as a QCD statement (model theorem, LA-2): (a), (b) have complete model-internal proofs; (c) is numerical.

**First sentence (printed).** 「在全局两时模型 $\mathbb M_{\rm glob}$ 中、$O(g^4)$ 阶，对全重合 SS 对的未割线与下述喷注函数类，……」

**Definitions.** $D_{\rm win}(J_X):=\{\mathcal J_\sigma\text{ for all sectors};\lambda_X\}$, and $D:=(D_{\rm win}(J_A),D_{\rm win}(J_B),a_e,\mathbf k_{Te})$.

**Class.** The hypotheses of T2(a): $J_A$ satisfies (SEC), (EQ), (REAL) on $\mathcal N_A$; $J_B$ satisfies (SEC), (EQ), (ADJ), (REAL) on $\mathcal N_B$; (iv) and (v) of T2. The class imposes (ADJ) on $J_B$ only; that is all T2 needs. Whether graph-generated QCD jets realize the perturbations used in (b) is OPEN-10. Membership of QCD jets in the class is as in T2(b).

**(a) (model-internal; complete proof).** With $K:=\lambda_B\varepsilon^{-1/2}$ and the error terms $\mathcal E_i$, $\delta_Y$ of T2,
$$W(12,21)=W^{\rm in}_D+W^{\rm out}+R_{P4},\qquad W^{\rm in}_D:=-\frac1{\mathcal J_B}\int_{\mathsf S}w^{[12]}f_{21}\frac{d^2\kappa}{(2\pi)^2},\qquad W^{\rm out}:=-\frac i{2\pi}\int_K^\infty\frac{d\kappa}\kappa\,\varrho_{12}(\kappa),$$
$$|R_{P4}|\le\tfrac12(\mathcal E_1+\mathcal E_3+\mathcal E_4+\mathcal E_5+\mathcal E_6+\mathcal E_7)+2\delta_Y|X_{(12,21)}|,\qquad|X_{(12,21)}|\le\frac3{\pi^2}m^\flat_Bl_K^2+\frac{m^\flat_A}{2\pi}\Big(\frac L2+\ell_A+\frac12\Big)+\tfrac12\textstyle\sum_{i\in\{1,3,4,5,6,7\}}\mathcal E_i .$$
$W^{\rm in}_D$ depends on $J_A$ only through $\lambda_A$ (via $K=\lambda_B\varepsilon^{-1/2}$); otherwise it depends only on $J_B$ and, through the localized weight $w^{[12]}$, on $a_1,a_2$. In particular it depends on $J_A$ only through $D$. So $W(12,21)-W^{\rm out}$ depends on $J_A$ only through $D$, up to $R_{P4}=O\big(\varepsilon^{1/2}(1+L_B)^2(1+L)\big)$.

*Proof.* Put $X_{(12,21)}:=I(12,21)/N_0=-\frac1{\mathcal J_B}\int h_{12}f_{21}$ (L5) and decompose as in Steps 3–5 of T2, for this colour pair alone.

* Inner square: $h_{12}=w^{[12]}+e_{12}$ (A1), so $-\frac1{\mathcal J_B}\int_{\mathsf S}h_{12}f_{21}=W^{\rm in}_D+P^{(12,21)}_1$ with $|P^{(12,21)}_1|\le\frac1{4\pi^2}\cdot4m_A\frac{\lambda_AK}{a_{\min}}\cdot12m^\flat_Bl_K^2=\frac12\mathcal E_1$ (L8(g), one colour order of $J_B$).
* Strip $\mathsf T_+$: $h_{12}f_{21}=\rho[-g/\kappa_2+E_{21}]$ (L8(d)). Its contribution is $W^{\rm out}+P^+_5+P^+_6+P^+_7+P^+_E$, with bounds $\frac12\mathcal E_5$, $\frac12\mathcal E_6$, $\frac12\mathcal E_7$, $\frac12\mathcal E_4$: the bounds of T2 are sums over the two strips, which contribute symmetrically.
* Strip $\mathsf T_-$: it lies in the quadrant $(+,-)$, where $h_{12}=0$ (L3).
* Off the strip: at most $\frac1{4\pi^2}m^\flat_A\cdot3200m^\flat_B(\lambda_B/K)(1+l_K)=\frac12\mathcal E_3$.

So $X_{(12,21)}=W^{\rm in}_D+W^{\rm out}+R'$ with $|R'|\le\frac12(\mathcal E_1+\mathcal E_3+\mathcal E_4+\mathcal E_5+\mathcal E_6+\mathcal E_7)$. With $|Y-1|\le\delta_Y\le\frac12$, $W(12,21)-X_{(12,21)}=X_{(12,21)}(1/Y-1)$ is at most $2\delta_Y|X_{(12,21)}|$; put $R_{P4}:=R'+X_{(12,21)}(1/Y-1)$. Finally $|W^{\rm in}_D|\le\frac1{4\pi^2}\cdot12m^\flat_Bl_K^2$ ($|w^{[12]}|\le1$, L8(g)), and $|W^{\rm out}|\le\frac{m^\flat_A}{2\pi}\big(\ln\frac a{2\mu_AK}+\frac12\big)\le\frac{m^\flat_A}{2\pi}\big(\frac L2+\ell_A+\frac12\big)$ by the decay bound of (A3), as in T2 Step 7. $\square$

**(b) The perturbation (model-internal; complete proof).** Add to the mixed sector $1V2$ of $J_A$ the two-state term
$$s\,c_2\,\frac{i}{A_1+k_1}\,\frac{i}{A_2+k_1}\,\frac{i}{A'-k_2},\qquad c_2=-i\tilde c_2,\quad\tilde c_2/\mathcal J_A\in\mathbb R,\quad A_1,A_2,A'<0,\quad\mu_A\le|A_1|,|A_2|,|A'|\le\lambda_A .$$
Put $\delta m:=|\tilde c_2|/(\lambda_A|\mathcal J_A|)$ (dimensionless).

* *What it preserves.* (SEC), (EQ) and $D$, since no single-state term is added; (REAL), by the phase choice; $\mathcal N_A$ and the jet scales $\lambda_A,\mu_A$. The term has $d_t=1$, so the jet constants change at most to $m_A+|s|\delta m$ and $m^\flat_A+|s|\delta m\,\lambda_A/\mu_A$.
* *What it breaks.* It does **not** preserve (ADJ) for $J_A$: its final gap $i/(A'-k_2)$ is single-state, and (ADJ) for the adjacent pair $(V_H,2)$ would require a partner $s\,c_2[i/(A_1+k_1)][i/(A_2+k_1)][i/(A''+k_1+k_2)]$ in sector $12V$. This is harmless, because the class imposes (ADJ) on $J_B$ only.
* *Effect.* $\varrho_{12}$ changes by $s\rho_2(i\kappa)$, with
$$\rho_2(k)=\frac{a_1a_2}{\mathcal J_A}\,\frac{2k\tilde c_2}{(2kA_1-a_1)(2kA_2-a_1)(2kA'-a_2)} .$$
* *Statement.* With $I_2:=\int_0^\infty\frac{dk}k\rho_2(k)\in\mathbb R$,
$$\delta W(12,21):=W[J_A+s\,\delta J_A]-W[J_A]=-\frac{is}{2\pi}I_2+\delta R,\qquad|\delta R|\le\frac{|s|}\pi\,\delta m\,\frac{\lambda_AK}{a_{\min}}+\bar R_{P4}[J_A+s\,\delta J_A]+\bar R_{P4}[J_A],$$
  where $\bar R_{P4}[\cdot]$ is the bound of (a) evaluated with the constants of the respective jet. $I_2$ has the fixed sign $-{\rm sgn}(\tilde c_2/\mathcal J_A)$ and is **non-zero whenever $\tilde c_2\ne0$**. $I_2$ depends only on the dimensionless ratios $\tilde c_2/(\lambda_A\mathcal J_A)$, $A_i/\lambda_A$, $a_1/a_2$, not on $\varepsilon$, while $\delta R\to0$ as $\varepsilon\to0$ at fixed shape. Hence $\delta W(12,21)\neq0$ for all $\varepsilon$ below the explicit threshold $|sI_2|/(2\pi)>|\delta R|$, and the leading shift is purely imaginary.

*Proof.* The perturbation preserves $\lambda_A$, hence $K$; so by (a) $W^{\rm in}_D$ is unchanged and $W^{\rm out}$ changes by $-\frac{is}{2\pi}\int_K^\infty\frac{d\kappa}\kappa\rho_2(i\kappa)$; the remainders contribute at most $\bar R_{P4}$ for each jet.

* *Rotation.* $\rho_2$ is holomorphic in ${\rm Re}\,k>0$ (its poles $a_1/(2A_1)$, $a_1/(2A_2)$, $a_2/(2A')$ are negative). $\rho_2(k)/k$ is bounded at 0, since $\rho_2(0)=0$, and is $O(|k|^{-3})$ at infinity. Cauchy's theorem on the quarter disc gives $\int_0^\infty\frac{d\kappa}\kappa\rho_2(i\kappa)=\int_0^\infty\frac{dk}k\rho_2(k)=I_2$.
* *Head.* $|2i\kappa A-a|\ge a$ gives $|\rho_2(i\kappa)|\le2\kappa|\tilde c_2|/(a_1|\mathcal J_A|)$. So $\big|\int_0^K\frac{d\kappa}\kappa\rho_2(i\kappa)\big|\le2K|\tilde c_2|/(a_1|\mathcal J_A|)\le2\delta m\,\lambda_AK/a_{\min}$, whence the first term of $\delta R$. (`final2_logs/final2_constants.log`: maximum ratio 1.000 over $2\times10^4$ random points.)
* *Sign and reality.* For $k>0$ each bracket $2kA-a$ is negative, so $\rho_2$ has the fixed sign $-{\rm sgn}(\tilde c_2/\mathcal J_A)$ on $(0,\infty)$ and is real there. Hence $I_2$ is real, and non-zero iff $\tilde c_2\neq0$. $\square$

* *Values.* $\delta W/s=+0.0615i,\ +0.0599i,\ -0.0790i$ for three parameter sets, with closed forms $\int\rho_2dk/k=1-\ln4$, $-0.37619672$ and $\frac{39}{50}\ln6-\frac{13}{10}\ln2$ (round-2 reviewers, sympy and `chkE_P4.py`).
* *With the (ADJ) partner* (if (ADJ) is also wanted for $J_A$). A round-3 reviewer added the partner in $12V$. It changes $\delta W(12,21)$ only at power level: $-7\times10^{-5}i$ at $\lambda=0.01$ and $-1.6\times10^{-5}i$ at $\lambda=0.003$, against $+0.0078i$. The shift formula is confirmed independently ($+0.007838i$ predicted, $+0.00785i$ computed; `review_r3_1_logs/t2_general.log`). This is consistent with (a): the $BB$ sector never reaches the strip, so the partner enters only through $R_{P4}$.

[[VERBATIM final.md 1125-1134]]
**Consequence.**

* Within the class, no **per-graph jet-local rewriting** that replaces each jet by its window data $D$ can satisfy per-graph weak equivalence with an error $C\lambda^aL^K$ for coincident pairs. For the unregulated $\mathbb M_{\rm glob}$ integrand this follows from (b) (proved in the model, for all $\varepsilon$ below the explicit threshold); with $G7$ regulators, from the example in (c) [P].
* For graph-generated (physical LCOPT) jets the statement is open (OPEN-10).
* All these shifts are purely imaginary at leading order in the side sum, so ${\rm Re}\,p_{\rm opp}$ is unaffected (up to $\delta R$). The envelope `asm:appO-envelope` must therefore be imposed on side-summed families for coincident connections (§2.3).

**Novelty.** Ours (no marker); it sharpens ERR-S3.

---

## 8. The half-coincident pattern

### Theorem T3 (half-coincident pair): the unregulated two-time model (remark) and a sensitivity proposition — (b), (c), (e) [P]

*Placement and grades (LA-2).* Items (a), (d), (f)–(j) form the untagged remark `rem:appO-halfcoinc` (the unregulated model); its items (a) and (g) are colour algebra with content [R, R_def] (L4), and (d), (f) are numerical [P]. Items (b), (c), (e) form the proposition `prop:appO-halfcoinc-sensitivity`, graded [P] as a QCD statement (model theorem), with complete model-internal proofs; they are its items (a), (b), (c), and the numerics of (e′) are its item (d). For leading-power LCOPT jets of QCD graphs the transfer is as in T2(b): an implication from `asm:appO-lcopt`, `asm:appO-adjacent-swap`, `asm:appO-real-jets`, with content [P]. The physical reading is at most [P].

**First sentence (printed, proposition).** 「在全局两时模型 $\mathbb M_{\rm glob}$ 中、在 $\mathcal N_B$ 上、$O(g^4)$ 阶，对振幅侧两条未割 SS 线 $i$–$j_1$、$i$–$j_2$（$j_1\ne j_2$ 为 $J_B$ 的旁观者），在下列各项所述的假设之下：……」

**Common hypotheses (H0).** $\mathbb M_{\rm glob}$ with exact connecting propagators; $J_A$ satisfies (SEC) and (EQ); $J_B$ satisfies (SEC), (EQ) and (ADJ); the configuration lies in $\mathcal N_B$; no rapidity regulator unless stated. (REAL) for $J_B$ is added where it is used ((b)). Each item states its smallness conditions explicitly.

*Structure of $J_B$.* The two $B$-insertions sit on different spectators, so $J_B$ carries no colour order. $f_B(\kappa):=J_B(-i\kappa)$, the sum of all six sectors, is an $S$-type function in the sense of L8: its strip terms cancel between the two time orders by (ADJ). It obeys L8(b)–(d), (g), (i) for $S$, and L8(f): $\int f_B\,d^2\kappa/(2\pi)^2=-\mathcal J_B$.

*Notation.* $r:=a_{\max}/a_{\min}$, so that $a/a_{\min}=r^{1/2}$; $L':=\ln\big(1+a/(\lambda_A\mu_B)\big)$ (note $L\le L'$, and $L'\ge\ln(1+1/\varepsilon)$).

**(a) [R, R_def].** $\mathcal R=2ic_1c_2\,{\rm Im}W_{12}\,[X_1,X_2]$ (L4(b), with $c_e$ real).

**(b) (model-internal; complete proof).** *Hypotheses:* (H0); (REAL) for $J_B$; $\varepsilon\le r^{-1/2}/8$ (equivalently $X:=a_{\min}/(2\lambda_A)\ge4\lambda_B$); and $\delta_b\le\frac12$ with $\delta_b$ below. *Conclusion:*
$$W_{12}=\frac12-V+E_b,\qquad V:=\frac1{\mathcal J_B}\int v(\kappa)f_B(\kappa)\frac{d^2\kappa}{(2\pi)^2}\ \text{ purely imaginary},\qquad|V|\le\frac{m^\flat_B}{8\pi^2}\big[24\ell_B^2+1643(1+\ell_B)\big],$$
$$|E_b|\le|\Delta X|+2\delta_b\Big(\frac12+|V|+|\Delta X|\Big),\qquad|\Delta X|\le\frac{m^\flat_B\,r^{1/2}}{4\pi^2}\,\varepsilon(1+L')^2\big[26672\,m_A+13144(1+m^\flat_A)\big],$$
$$\delta_b:=\frac{m^\flat_B\,r^{1/2}}{4\pi^2}\,\varepsilon(1+L')^2\big[53344\,m_A+13144(1+2m^\flat_A)\big].$$
Hence $|{\rm Re}\,W_{12}-\frac12|\le|E_b|=O(\varepsilon(1+L')^2)$ with an explicit constant. ((REAL) for $J_A$ and $\mathcal N_A$ are not needed.)

*Proof.*

* *Numerator and denominator.* By L5 at $\theta=\pi/2$ (on $\mathcal N_B$), $X_b:=I_{12}/N_0=-\frac1{\mathcal J_B}\int h_{12}f_B\frac{d^2\kappa}{(2\pi)^2}$, $Y_b:=N/N_0=-\frac1{\mathcal J_B}\int(h_{12}+h_{21})f_B\frac{d^2\kappa}{(2\pi)^2}$, and $W_{12}=X_b/Y_b$.
* *$A$-side input.* (A1) for $R\le X$: $h_\pi=w^{[\pi]}+e_\pi$ with $|e_\pi|\le4m_A\lambda_AR/a_{\min}$; (A2): $|h_\pi|\le m^\flat_A$ everywhere; $w^{[12]}=\frac12+v$, $w^{[21]}=\frac12-v$, $|w^{[\pi]}|\le1$. Neither uses $\mathcal N_A$ or (REAL).
* *$B$-side input.* L8(f): $-\frac1{\mathcal J_B}\int f_B\frac{d^2\kappa}{(2\pi)^2}=1$. L8(i) with $l_X=\ln(1+2a_{\min}/(\lambda_A\mu_B))$: $\int_{R\le X}R|f_B|\le96M^\flat_B\lambda_Bl_X^2+6572M^\flat_B\lambda_B(1+l_X)\ln\frac X{4\lambda_B}$ and $\int_{R>X}|f_B|\le6572M^\flat_B\frac{\lambda_B}X(1+l_X)$.
* *Decomposition.* $X_b=\frac12-V+\Delta X$ with $\Delta X:=-\frac1{\mathcal J_B}\big[\int_{R\le X}e_{12}f_B+\int_{R>X}(h_{12}-w^{[12]})f_B\big]$ (measure $d^2\kappa/(2\pi)^2$). Since $|h_{12}-w^{[12]}|\le1+m^\flat_A$,
  $$|\Delta X|\le\frac1{4\pi^2|\mathcal J_B|}\Big[4m_A\frac{\lambda_A}{a_{\min}}\int_{R\le X}R|f_B|+(1+m^\flat_A)\int_{R>X}|f_B|\Big].$$
  The $v$-terms cancel in $Y_b$, so $Y_b=1+\Delta Y$ with $|\Delta Y|\le\frac1{4\pi^2|\mathcal J_B|}\big[8m_A\frac{\lambda_A}{a_{\min}}\int_{R\le X}R|f_B|+(1+2m^\flat_A)\int_{R>X}|f_B|\big]$.
* *Arithmetic.* $\lambda_A\lambda_B/a_{\min}=r^{1/2}\varepsilon$, $\lambda_B/X=2r^{1/2}\varepsilon$, $\ln(X/4\lambda_B)=\ln(a_{\min}/(8\lambda_A\lambda_B))\le L\le L'$, $l_X\le\ln2+L'$, and $L'\ge\ln9$ (because $\varepsilon\le\frac18$). Hence $96l_X^2+6572(1+l_X)L\le6668(1+L')^2$ and $1+l_X\le(1+L')^2$ (`final2_logs/final2_constants.log`). This gives the stated bound on $|\Delta X|$ and $|\Delta Y|\le\delta_b$ ($4\cdot6668=26672$, $8\cdot6668=53344$, $2\cdot6572=13144$).
* *Division.* $W_{12}=\frac{\frac12-V+\Delta X}{1+\Delta Y}=\frac12-V+E_b$ with $E_b:=\Delta X-(\frac12-V+\Delta X)\frac{\Delta Y}{1+\Delta Y}$. For $|\Delta Y|\le\delta_b\le\frac12$ this gives the bound on $|E_b|$.
* *$|V|$.* $|v|\le\frac12$, and L8(i1), (i2) with $X=4\lambda_B$ give $\int|f_B|\le24M^\flat_B\ell_B^2+\frac{6572}4M^\flat_B(1+\ell_B)$.
* *Imaginarity.* By (REAL) for $J_B$, $f_B(-\kappa)=e^{2i\varphi}\overline{f_B(\kappa)}$ and $\mathcal J_B\in e^{i\varphi}\mathbb R$. Since $v$ is real and odd, $\int vf_B/\mathcal J_B=-\overline{\int vf_B/\mathcal J_B}$, i.e. $V$ is purely imaginary. So ${\rm Re}\,W_{12}-\frac12={\rm Re}\,E_b$. $\square$

**(c) (model-internal; complete proof).** Under (H0) and $N\neq0$ (for instance under the hypotheses of (b)), ${\rm Im}W_{12}=0$ for configurations symmetric under $1\leftrightarrow2$, i.e. with $a_1=a_2$, $J_A^{[12]}(k_1,k_2)=J_A^{[21]}(k_2,k_1)$ and $J_B(p_1,p_2)=J_B(p_2,p_1)$. Indeed, relabelling the integration variables gives $I_{12}=I_{21}$, and $I_{12}+I_{21}=N\neq0$, so $W_{12}=\frac12$. $\square$

[[VERBATIM final.md 1182-1188]]
**Lemma V (regulated race weights on the $\pi/4$ contour) — (数学).** *Placement:* inside the proof of `prop:appO-halfcoinc-sensitivity` (proved in this revision; Fix 5).

Let the even Lorentzian $\chi_K(k^-)$ act on both lines (L1′, example). On the $\pi/4$ contour put $x_e:=iK/z_e$ ($e=1,2$): $x_e=t_ew$ for an initial line ($\kappa_e<0$) and $x_e=-t_ew$ for a final line ($\kappa_e>0$), with $w:=e^{-i\pi/4}$ and $t_e:=|x_e|=2K|\kappa_e|/a_e$. Let $w_K^{[12]}:=\sum_{(p)}u_1(p_1)u_2(p_2)W^{[12]}(p)$ be the pole sum of L1′ over the nine pole pairs, with $u_z=x^2/(x^2-1)$, $u_+=1/(2(1-x))$, $u_-=1/(2(1+x))$ and the race weights of L1(c). Put $v_K:=w_K^{[12]}-\frac12$ and $s:=t_1+t_2$. Then, in all four sign patterns,

* (a) $|v_K|<\frac12$;
* (b) $|v_K|\le s/4$;
* (c) $|v_K-(x_1-x_2)/4|\le s^3(1+s/4)(\frac32+s/4)/\big(4(1+\sqrt2\,s)\big)$; in particular $v_K=(x_1-x_2)/4+O(s^3)$, with no quadratic term.

The bounds (a) and (b) are sharp: $\sup|v_K|=\frac12$ and $\sup|v_K|/(s/4)=1$.

*Proof.*

* *Closed forms.* A pole $iK/y$ enters the race weight through $y$: $y=x_e$ for the gluon pole, $y=1$ for $+iK$ (initial) and $y=-1$ for $-iK$ (final). The race weight of colour order $[12]$ of a pair $(iK/y_1,iK/y_2)$ is $y_2/(y_1+y_2)$ if both poles are final, $y_1/(y_1+y_2)$ if both are initial, 1 if the pole of line 1 is initial and that of line 2 final, and 0 otherwise. Summing the nine pairs gives, for line 1 initial and line 2 final (pattern IF),
  $$v_{IF}=\frac{2D^2+(x_1-x_2)}{4(1+D)^2},\qquad D:=x_1-x_2-x_1x_2=(1+x_1)(1-x_2)-1,$$
  and for both lines initial (pattern II)
  $$v_{II}=\frac{(x_1-x_2)\big[2S^2+(x_1+x_2)\big]}{4(1+S)^2(x_1+x_2)},\qquad S:=x_1+x_2+x_1x_2 .$$
  The other two patterns follow from $v_{FI}(x)=-v_{IF}(-x)$ and $v_{FF}(x)=-v_{II}(-x)$. These are rational identities (`final2_logs/vK_hand_proof.log`, item (1)).
* *Reduction.* On the rays (IF: $x_1=t_1w$, $x_2=-t_2w$; II: $x_1=t_1w$, $x_2=t_2w$) one has $D=S=sw-ip$ with $p:=t_1t_2\le s^2/4$, using $w^2=-i$. Hence $v_{II}(t_1w,t_2w)=\frac{t_1-t_2}s\,v_{IF}(t_1w,-t_2w)$. The patterns FI and FF map to IF and II under $x\to-x$. It suffices to treat IF.
* *(a).* With $\xi:=x_1-x_2=sw$ ($|\xi|=s$), $|v_{IF}|\le(2|D|^2+s)/(4|1+D|^2)$. Since ${\rm Re}\,D=s/\sqrt2$, $2|1+D|^2-2|D|^2=2+4{\rm Re}\,D=2+2\sqrt2s$, so $2|1+D|^2-(2|D|^2+s)=2+(2\sqrt2-1)s>0$, i.e. $|v_{IF}|<\frac12$.
* *(b).* Write $v_{IF}=\frac{sw}4\,N/P^2$ with $P:=1+D$ and $N:=1+2D^2/(sw)=1+2sw-4ip-2q\bar w$, $q:=p^2/s$. Then
  $$|P|^2=A:=1+\sqrt2s+s^2+\sqrt2sp+p^2,\qquad|N|^2=1+2\sqrt2(s-q)+4s^2+4q^2+8\sqrt2p(s+q)+16p^2,$$
  and expanding gives $A^2-|N|^2=G_1+G_2+G_3+G_4+G_5$ with
  $$G_1=s^4-14p^2,\quad G_2=2\sqrt2(s^3-3sp),\quad G_3=4p^2\Big(s^2-\frac{p^2}{s^2}\Big),\quad G_4=2\sqrt2p^2\Big(s-\frac{4p}s\Big),\quad G_5=2\sqrt2s^3p+4s^2p+2\sqrt2sp^3+p^4+\frac{2\sqrt2p^2}s .$$
  With $p=\tau s^2/4$, $0\le\tau\le1$: $G_1=s^4(8-7\tau^2)/8$, $G_2=\frac{\sqrt2}2s^3(4-3\tau)$, $G_3=\tau^2s^6(16-\tau^2)/64$, $G_4=\frac{\sqrt2}8\tau^2s^5(1-\tau)$. All are $\ge0$, and $G_5\ge0$ termwise. Hence $|N|\le|P|^2$, i.e. $|v_{IF}|\le s/4$, and $|v_{II}|=\frac{|t_1-t_2|}s|v_{IF}|\le s/4$.
* *(c).* The identity $v_{IF}-\xi/4=-D(2x_1x_2+\xi D)/(4(1+D)^2)$ holds. Insert $|D|\le s+p\le s(1+s/4)$, $|2x_1x_2+\xi D|\le2p+s(s+p)\le s^2(\frac32+\frac s4)$ and $|1+D|^2=A\ge1+\sqrt2s$. For II, $v_{II}-\xi_{II}/4=\frac{t_1-t_2}s(v_{IF}-\xi_{IF}/4)$. The cubic bound shows that the quadratic term vanishes; a series expansion confirms this in all four patterns (`final2_logs/vK_hand_proof.log`, item (6)). $\square$

*Checks.* `final2_scripts/vK_hand_proof.py` → `final2_logs/vK_hand_proof.log`, ALL PASS. It checks every algebraic step above symbolically, including the identity $A^2-|N|^2=\sum G_i$ and the factored forms; on $2\times10^5$ random points it finds $\sup|v_K|=0.500000$, $\sup|v_K|/(s/4)=1.000000$, and a remainder ratio $\le0.654$. An independent certificate is in `final2_scripts/vK_bounds_proof.py` → `final2_logs/vK_bounds_proof.log`: $F:=(t_1+t_2)^2(|P|^4-|N|^2)$ is a polynomial with 31 monomials, all with non-negative coefficients. The final review's sampling (`final_review_logs/fr_t3e_vK.log`) found the same suprema; its one-dimensional PV representation agrees with the pole sum to $4\times10^{-8}$.

**(e) Sensitivity (model-internal; complete proof).** Put the even Lorentzian regulator $\chi_K(k^-)=K^2/(k^{-2}+K^2)$ on the $A$-side minus components of both lines.

*Hypotheses.* (H0) (no (REAL) is used); $2\lambda_A\le K\le a_{\min}/(8\lambda_B)$, a range that is non-empty iff $\varepsilon\le r^{-1/2}/16$; and $\delta_N(K)\le\frac12$ with $\delta_N(K)$ below.

*Notation.* $\Lambda_K:=\ln\big(1+2a_{\min}/(K\mu_B)\big)$; $m'_B:=M^\flat_{B,\pi/4}/|\mathcal J_B|$ and $m^\flat_{A,\pi/4}:=M^\flat_{A,\pi/4}/|\mathcal J_A|$ (the $\pi/4$ norms of L8(h)); $c_U\le(3+\sqrt2)/2$ (L1′).

*Conclusion.*
$$\Big|W_{12}(K)-\frac12\Big|\le\frac{53344}{2\pi^2}\,m'_B\,\frac{K\lambda_B}{a_{\min}}(1+\Lambda_K)^2+\frac{6144}{2\pi^2}\,c_U^2m_Am'_B\,\frac{\lambda_A}K\Lambda_K^2+\frac{c_U^2m'_B}{2\pi^2}\,r^{1/2}\varepsilon(1+L')^2\big[3414016\,m_A+841216\,m^\flat_{A,\pi/4}\big],$$
$$\delta_N(K):=\frac{c_U^2m_Am'_B}{2\pi^2}\Big[6144\frac{\lambda_A}K\Lambda_K^2+3414016\,r^{1/2}\varepsilon(1+L')^2\Big]+\frac{210304}{4\pi^2}\big(8c_U^2m^\flat_{A,\pi/4}+1\big)m'_B\,r^{1/2}\varepsilon(1+L') .$$
Numerically the bound reads $2702.4\,m'_B\frac{K\lambda_B}{a_{\min}}(1+\Lambda_K)^2+311.3\,c_U^2m_Am'_B\frac{\lambda_A}K\Lambda_K^2+c_U^2m'_Br^{1/2}\varepsilon(1+L')^2[172956\,m_A+42617\,m^\flat_{A,\pi/4}]$. With $c_U^2\le4.8713$ this is at most $2703\,m'_B\frac{K\lambda_B}{a_{\min}}(1+\Lambda_K)^2+1517\,m_Am'_B\frac{\lambda_A}K\Lambda_K^2+m'_Br^{1/2}\varepsilon(1+L')^2[842600\,m_A+207600\,m^\flat_{A,\pi/4}]$ (`final2_logs/final2_constants.log`). The final report's "$C_e\le10^6m^\flat_B(1+m_A+m^\flat_A)a_{\max}/a_{\min}$" is replaced by these constants; note $r^{1/2}$ instead of $r$, and the $\pi/4$ norms.

*Boost invariance.* Every term is boost invariant. Under $k^+\to e^yk^+$ and $k^-\to e^{-y}k^-$, the combinations $K\lambda_B/a_{\min}$, $\lambda_A/K$ and $a_{\min}/(K\mu_B)$ are invariant, since $K$ is a $k^-$ scale and $\mu_B$ a $k^+$ scale; $\varepsilon$, $L'$, $r$ are invariant (`final_logs/t3f_recompute.log`). The round-2 statement had $\ln(1+K/\mu_B)$ in the second term; that combination is not boost invariant ($\propto e^{-2y}$) and was corrected in the final round.

*Proof.*

* *(1) Rotation.* L5 at $\theta=\pi/4$ with the rational $A$-side regulator. $F_A^{\rm reg}$ is holomorphic on the swept set: $z_e$ never crosses the real $k^-$ axis, the regulator poles $\pm iK$ are fixed, and every gap factor has imaginary part $\ge\eta$. For $\theta<\pi/2$ there is no collision of $z_e$ with $\mp iK$. The $J_B$ factors are holomorphic on the swept set by $\mathcal N_B$. Put $h^{\rm reg}_\pi(\kappa):=\frac{a_1a_2}{\mathcal J_A}F_A^{{\rm reg},[\pi]}(e^{i\pi/4}\kappa)$ and $f^{(\pi/4)}_B(\kappa):=J_B(-e^{i\pi/4}\kappa)$. Then
  $$X(K):=\frac{I_{12}(K)}{N_0}=\frac i{\mathcal J_B}\int h^{\rm reg}_{12}f^{(\pi/4)}_B\frac{d^2\kappa}{(2\pi)^2},\qquad Y(K):=\frac{N(K)}{N_0}=\frac i{\mathcal J_B}\int(h^{\rm reg}_{12}+h^{\rm reg}_{21})f^{(\pi/4)}_B\frac{d^2\kappa}{(2\pi)^2},$$
  and L8(f) on the contour $p=-e^{i\pi/4}\kappa$ gives $\frac i{\mathcal J_B}\int f^{(\pi/4)}_B\frac{d^2\kappa}{(2\pi)^2}=\frac i{\mathcal J_B}(-i\mathcal J_B)=1$.
* *(2) $A$-side on the $\pi/4$ contour.* The final group $\{z_e:\kappa_e>0\}\cup\{-iK\}$ lies in the closed fourth quadrant and the initial group $\{z_e:\kappa_e<0\}\cup\{+iK\}$ in the closed second quadrant (L1′, example).
  * (2a) *Localization.* For $R\le R_A:=a_{\min}/(4\lambda_A)$ (and $K\ge2\lambda_A$), $h^{\rm reg}_\pi=w_K^{[\pi]}+e_K^{[\pi]}$ with $|e_K^{[\pi]}|\le32c_U^2m_A\lambda_A\max(1/K,2R/a_{\min})$. This is L1′(b): the gap momenta are sums of poles of one group, so by the closed-quadrant property $|K_l|\ge\min(|z_e|,K)\ge\min(a_{\min}/(2R),K)\ge2\lambda_A$; also $N2^{N+1}=16$, $\sum_\sigma|w_\sigma|\le2$, and $\sum_{(p)}\prod_e|u_e(p_e)|\le c_U^2$. By L1′(c), $w_K^{[12]}+w_K^{[21]}=1$; so $w_K^{[12]}=\frac12+v_K$ with $v_K$ as in Lemma V.
  * (2b) *Global bound.* Everywhere on the $\pi/4$ contour, $|h^{\rm reg}_\pi|\le4c_U^2m^\flat_{A,\pi/4}$. The gap momentum $K_l$ of an initial gap, and $-K_l$ of a final gap, lie in the closed sector $\frac\pi2\le\arg\le\frac{3\pi}4$. For $w$ in that sector and real $A$, $|A+w|^2\ge A^2-\sqrt2|A||w|+|w|^2\ge\max(A^2,|w|^2)/2$. So every gap factor obeys $|A+K_l|\ge\max(|A|,|K_l|)/\sqrt2$, whatever the sign of $A$, and $|J^{(\sigma)}(p)|\le2M^\flat_{\pi/4,\sigma}/(|K_1||K_2|)$. The prefactor of L1′(a) times $\prod_l|K_l|^{-1}$ equals $\prod_e|\rho_{e,p_e}/p_e|\,|w_\sigma(p)|\le|u_1u_2|/(a_1a_2)$. Summing over the pole pairs and the at most two sectors gives the bound.
* *(3) Regulated weight.* By Lemma V(b), $|v_K|\le\min(\frac12,s/4)$ with $s=|x_1|+|x_2|\le4KR/a_{\min}$, i.e. $|v_K|\le\min(\frac12,KR/a_{\min})$.
* *(4) $B$-side.* L8(h), (i) at $\theta=\pi/4$ with $M':=M^\flat_{B,\pi/4}$: $\int_{R\le X}|f^{(\pi/4)}_B|\le192M'l_X^2$; for $X\ge4\lambda_B$, $\int_{R>X}|f^{(\pi/4)}_B|\le52576M'\frac{\lambda_B}X(1+l_X)$ and $\int_{R\le X}R|f^{(\pi/4)}_B|\le768M'\lambda_Bl_X^2+52576M'\lambda_B(1+l_X)\ln\frac X{4\lambda_B}$.
* *(5) Decomposition.* With $V_K:=\frac1{\mathcal J_B}\int_{R\le R_A}v_Kf^{(\pi/4)}_B\frac{d^2\kappa}{(2\pi)^2}$,
  $$X(K)=\frac12+iV_K+\Delta X_K,\qquad\Delta X_K:=\frac i{\mathcal J_B}\Big[\int_{R\le R_A}e_K^{[12]}f^{(\pi/4)}_B+\int_{R>R_A}\big(h^{\rm reg}_{12}-\tfrac12\big)f^{(\pi/4)}_B\Big],$$
  $$Y(K)=1+\Delta Y_K,\qquad\Delta Y_K:=\frac i{\mathcal J_B}\Big[\int_{R\le R_A}\big(e_K^{[12]}+e_K^{[21]}\big)f^{(\pi/4)}_B+\int_{R>R_A}\big(h^{\rm reg}_{12}+h^{\rm reg}_{21}-1\big)f^{(\pi/4)}_B\Big].$$
  Hence $W_{12}(K)-\frac12=\big(iV_K+\Delta X_K-\frac12\Delta Y_K\big)/(1+\Delta Y_K)$, with
  $$\Delta X_K-\tfrac12\Delta Y_K=\frac i{2\mathcal J_B}\Big[\int_{R\le R_A}\big(e_K^{[12]}-e_K^{[21]}\big)f^{(\pi/4)}_B+\int_{R>R_A}\big(h^{\rm reg}_{12}-h^{\rm reg}_{21}\big)f^{(\pi/4)}_B\Big].$$
* *(6) Bounds.* Put $X_K:=a_{\min}/(2K)$. Then $X_K\ge4\lambda_B$ (since $K\le a_{\min}/(8\lambda_B)$) and $X_K\le R_A$ (since $K\ge2\lambda_A$); also $R_A\ge4\lambda_B$. Further $l_{X_K}=\Lambda_K$, $\ln(X_K/4\lambda_B)\le\Lambda_K$, $l_{R_A}=\ln(1+a_{\min}/(\lambda_A\mu_B))\le L'$, $\ln(R_A/4\lambda_B)\le L\le L'$, $\lambda_A\lambda_B/a_{\min}=r^{1/2}\varepsilon$ and $\lambda_B/R_A=4r^{1/2}\varepsilon$.
  * $|V_K|\le\frac1{4\pi^2|\mathcal J_B|}\big[\frac K{a_{\min}}\int_{R\le X_K}R|f|+\frac12\int_{R>X_K}|f|\big]\le\frac{m'_B}{4\pi^2}\frac{K\lambda_B}{a_{\min}}\big[768\Lambda_K^2+52576(1+\Lambda_K)\Lambda_K+52576(1+\Lambda_K)\big]\le\frac{53344}{4\pi^2}m'_B\frac{K\lambda_B}{a_{\min}}(1+\Lambda_K)^2$.
  * Region $R\le R_A$ of $\Delta X_K-\frac12\Delta Y_K$: $\frac12|e_K^{[12]}-e_K^{[21]}|\le32c_U^2m_A\lambda_A\max(1/K,2R/a_{\min})$. For $R\le X_K$ use $1/K$ and $\int_{R\le X_K}|f|\le192M'\Lambda_K^2$. For $X_K<R\le R_A$ use $2R/a_{\min}$ and the $R$-weighted bound with $X=R_A$. Together this is at most
  $$\text{term}_b:=\frac{c_U^2m_Am'_B}{4\pi^2}\Big[6144\frac{\lambda_A}K\Lambda_K^2+64\cdot53344\,r^{1/2}\varepsilon(1+L')^2\Big],\qquad64\cdot53344=3414016 .$$
  * Region $R>R_A$: $\frac12|h^{\rm reg}_{12}-h^{\rm reg}_{21}|\le4c_U^2m^\flat_{A,\pi/4}$ by (2b), and $\int_{R>R_A}|f|\le52576M'(\lambda_B/R_A)(1+L')=210304M'r^{1/2}\varepsilon(1+L')$. Contribution at most $\frac{4c_U^2m^\flat_{A,\pi/4}}{4\pi^2}210304\,m'_Br^{1/2}\varepsilon(1+L')$.
  * $|\Delta Y_K|\le2\,\text{term}_b+\frac1{4\pi^2}(8c_U^2m^\flat_{A,\pi/4}+1)\,210304\,m'_Br^{1/2}\varepsilon(1+L')=\delta_N(K)$, using $|h^{\rm reg}_{12}+h^{\rm reg}_{21}-1|\le8c_U^2m^\flat_{A,\pi/4}+1$ for $R>R_A$.
* *(7) Conclusion.* For $\delta_N(K)\le\frac12$, $|W_{12}(K)-\frac12|\le2\big(|V_K|+|\Delta X_K-\frac12\Delta Y_K|\big)$. Inserting the bounds of (6) and using $1+L'\le(1+L')^2$ gives the stated inequality. $\square$

[[VERBATIM final.md 1209-1215]]
**(e′) (algebraic part: Lemma V(c); numerics [P]).**

* *Leading term.* By Lemma V(c), $v_K=(x_1-x_2)/4+O(s^3)$, with no quadratic term; i.e. $v_K\approx\frac{iK}4(1/z_1-1/z_2)=\frac{iK}2(k_1^+/a_1-k_2^+/a_2)$ for $|z_e|\gg K$. The final round's numerical statement $|v_K-(x_1-x_2)/4|\le0.044(|x_1|+|x_2|)^2$ for $|x_e|\le\frac14$ is superseded by the proven cubic bound.
[[VERBATIM final.md 1219-1247]]
**Novelty.** The model computation and (e) are ours (to our knowledge new; no marker). The configuration (one $A$-spectator connected to two different $B$-spectators) does not occur in Lindsay 1984 or in Brandt–Frenkel–Taylor 1989 (one spectator per hadron), nor in Lindsay–Ross–Sachrajda (no $A$-spectator).
[[VERBATIM final.md 1249-1251]]
## 9. Beyond $O(g^4)$ uncut coincident pairs

### Proposition P5 (at $O(g^6)$ the direct-line ladder class is not closed under unitarity) — [A]

*Label:* `prop:appO-g6-ladder`.

**Setting.** Two on-shell eikonal (or massive) lines $A$ and $B$. $\mathsf C$ is the class of direct-line ladder graphs at $O(g^6)$: all three gluons join the two lines, with any crossings.

**Definition (unitarity defect).**
$$D_{\mathsf C}:={\rm Disc}_s\Big(\sum_{\Gamma\in\mathsf C}\Gamma\Big)-\int d\Phi_2\,(\mathcal M_{\mathsf C})^\dagger\mathcal M_{\mathsf C}\quad\text{at }O(g^6).$$
It is the part of the class's $s$-channel discontinuity that is not reproduced by two-line intermediate states built from the class's own lower-order amplitudes.

**Statement.**

**(i) The defect is an interference term.** By Cutkosky's rules applied graph by graph, $D_{\mathsf C}$ is the sum of the three-particle cuts of class-$\mathsf C$ graphs. A three-particle cut cuts one rung whose two ends lie on **opposite** sides of the cut: line $A$ on one side, line $B$ on the other. (A cut with no exchange on one side would need an on-shell emission from an on-shell massive or time-like line, which is kinematically forbidden.) Hence
$$D_{\mathsf C}=\int d\Phi_3\,\big[A_A^\dagger A_B+A_B^\dagger A_A\big].$$
Here $A_X$ is the tree $2\to3$ amplitude with one gluon exchanged between the lines and one gluon radiated from line $X$, with emissions before and after the exchange combined; it contains the propagator of the exchanged gluon, see (ii). The self terms $A_A^\dagger A_A$ and $A_B^\dagger A_B$, in which a gluon is emitted and absorbed by the same line, lie outside $\mathsf C$.

**(ii) Kinematics, line parts and the sign in Feynman gauge.** Line $A$ gives up $q_1$ and line $B$ gives up $q_2$, with
$$q_1+q_2=k,\qquad k^2=0,\qquad v_A\cdot q_1=0,\qquad v_B\cdot q_2=0$$
(recoilless eikonal lines; $k$ is the radiated gluon). When the gluon $k$ is radiated from line $A$, the exchanged gluon carries $q_2$, the only momentum transferred to $B$, so $A_A$ contains the exchange propagator $1/q_2^2$. Radiation from line $B$ carries $1/q_1^2$. On each line the two orderings (emission before or after the exchange) combine as follows (Lipatov 1976; Kuraev–Lipatov–Fadin 1977; Del Duca 1995). The colour-antisymmetric ($f^{abc}$) part survives the eikonal limit and gives the line parts of the Lipatov vertex,
$$A_A^\mu=C\,\frac{(v_A\cdot v_B)\,v_A^\mu}{(v_A\cdot k)\,q_2^2},\qquad A_B^\mu=-C\,\frac{(v_A\cdot v_B)\,v_B^\mu}{(v_B\cdot k)\,q_1^2},\qquad C=f^{a_1a_2b}\,T_A^{a_1}T_B^{a_2}$$
(overall $g^3$ and phases dropped; $b$ is the colour of the radiated gluon). The colour-symmetric part is suppressed by $(q_1^2-q_2^2)/(M\,v\cdot k)$ and vanishes in the eikonal limit outside the collinear regions; this is the abelian statement. In Feynman gauge (polarization sum $-g_{\mu\nu}$)
$$2A_A\cdot(-g)\cdot A_B=\frac{2\,C^\dagger C\,(v_A\cdot v_B)^3}{(v_A\cdot k)(v_B\cdot k)\,q_1^2q_2^2}>0,$$
because the exchanges are space-like ($q_1^2,q_2^2<0$) and $v_A\cdot k$, $v_B\cdot k$, $v_A\cdot v_B>0$. This is non-zero in the non-abelian theory. The self terms are $A_X\cdot(-g)\cdot A_X=-C^\dagger C\,(v_A\cdot v_B)^2v_X^2/\big((v_X\cdot k)^2q_{\bar X}^4\big)\le0$, where $q_{\bar X}$ is the exchange momentum in $A_X$; they vanish for light-like lines.

*Comparison with $\int|A_A+A_B|^2$ in Feynman gauge.* The integrand of $D_{\mathsf C}$ is the interference term, so
$$\big[A_A^\dagger A_B+A_B^\dagger A_A\big]_{\rm Feyn}=|A_A+A_B|^2_{\rm Feyn}-(\text{self terms})\ \ge\ |A_A+A_B|^2_{\rm Feyn},$$
with equality for light-like lines. For time-like lines with rapidity separation $Y$ ($v_A\cdot v_B=\cosh Y$),
$$\frac{|\text{self terms}|}{\text{interference}}=\frac1{2\,v_A\cdot v_B}\Big[\frac{(v_B\cdot k)\,q_1^2}{(v_A\cdot k)\,q_2^2}+\frac{(v_A\cdot k)\,q_2^2}{(v_B\cdot k)\,q_1^2}\Big],$$
which is about $1/\cosh Y$ for central emission with $q_1^2\approx q_2^2$. So $D_{\mathsf C}=\int d\Phi_3|A_A+A_B|^2_{\rm Feyn}$ exactly only for light-like lines, and approximately in the Regge limit $Y\to\infty$ for central emission.

**(iii) Gauge dependence.** The line parts alone do not form a conserved current:
$$k\cdot A_A=\frac{C\,(v_A\cdot v_B)}{q_2^2},\qquad k\cdot A_B=-\frac{C\,(v_A\cdot v_B)}{q_1^2},\qquad k\cdot(A_A+A_B)=C\,(v_A\cdot v_B)\Big(\frac1{q_2^2}-\frac1{q_1^2}\Big)\neq0 .$$
Hence neither the class $\mathsf C$, nor $D_{\mathsf C}$, nor $|A_A+A_B|^2$ is gauge invariant. Current conservation requires the three-gluon (central) term of the Lipatov vertex,
$$A_3^\mu=-C\,\frac{(v_A\cdot v_B)(q_1-q_2)^\mu+2(v_A\cdot k)\,v_B^\mu-2(v_B\cdot k)\,v_A^\mu}{q_1^2q_2^2},\qquad k\cdot A_3=-C\,(v_A\cdot v_B)\frac{q_1^2-q_2^2}{q_1^2q_2^2},$$
using $k\cdot(q_1-q_2)=q_1^2-q_2^2$. Thus $k\cdot(A_A+A_B+A_3)=0$ exactly, and $|A_A+A_B+A_3|^2$ is gauge independent. The line parts alone suffice only in the limit $q_1^2=q_2^2$, i.e. for $|k_T|\ll|q_T|$, where the relative violation $|q_1^2-q_2^2|/(|q_1^2|+|q_2^2|)$ is $O(|k_T|/|q_T|)$. For light-like lines $-J\cdot J=4(v_A\cdot v_B)^2/(k_T^2q_{1T}^2q_{2T}^2)$ with $J=A_A+A_B+A_3$, the square of the Lipatov vertex.

**Conclusion.**

* In Feynman gauge with eikonal lines, $D_{\mathsf C}\ne0$ (indeed $>0$ pointwise): the class $\mathsf C$ is not closed under unitarity.
* The gauge-invariant $2\to3$ amplitude needs the three-gluon-vertex term, i.e. the full Lipatov vertex.
* In DY, part of this real emission corresponds to cut direct lines (inside $\mathcal G_0$), and part to soft lines emitted and absorbed by the same spectator (outside $\mathcal G_0$).

**Qualification.** The conclusion concerns the closure of $\mathcal G_0$ under unitarity, i.e. the SS-family bookkeeping. It is not a failure of factorization. It is consistent with Schwartz–Yan–Zhu, PRD 97 (2018) 096017 (pure Glauber ladders cancel for single-scale observables; the leading violation needs the Lipatov vertex), and with Rothstein–Stewart, JHEP 08 (2016) 025.

**Grade.** [A]. This is an argument whose substance is standard (BFKL). The interference identity, its Feynman-gauge sign, the non-conservation of the line current and its restoration by the three-gluon term are checked numerically for eikonal currents.

**Verification.**

* `final2_scripts/p5_lipatov_check.py` → `final2_logs/p5_lipatov_check.log`, ALL PASS. It replaces `final_scripts/p5_interference.py`, whose currents $v_X/(v_X\cdot k)$ had equal normalization (no exchange propagators), which made its gauge-invariance check circular. Kinematics $q_1+q_2=k$, $v_A\cdot q_1=v_B\cdot q_2=0$; rapidity separations $Y=0.5,2,4,8$ and light-like lines; 4000 points each.
  * $k\cdot(A_A+A_B)=C(v_A\cdot v_B)(1/q_2^2-1/q_1^2)$ to $\le3\times10^{-13}$ (relative). The line-part current violation reaches 0.30 ($Y=0.5$) and 1.00 ($Y=8$, light-like). $|A_A+A_B|^2$ differs between Feynman and light-cone gauge by relative amounts up to $8.6\times10^4$.
  * With $A_3$: $|k\cdot J|$ relative to $|k\cdot A_A|+|k\cdot A_B|$ is $\le3\times10^{-13}$, and the gauge difference of $|J|^2$ is $\le2\times10^{-9}$.
  * The Feynman-gauge interference equals $2(v_A\cdot v_B)^3/((v_A\cdot k)(v_B\cdot k)q_1^2q_2^2)$ to $6\times10^{-16}$ and is positive. The self terms are $\le0$, and zero for light-like lines. Interference minus $|A_A+A_B|^2_{\rm Feyn}$ equals minus the self terms, hence is $\ge0$. The ratio $|\text{self}|/\text{interference}$ matches the formula in (ii) to $\le5\times10^{-13}$; for central emission its median is 0.91, 0.36, 0.057, 0.0013, against $1/\cosh Y=0.89,\ 0.27,\ 0.037,\ 0.0007$.
  * The line-part violation falls with $|k_T|/|q_T|$: 0.97, 0.35, 0.10, 0.03, 0.01, 0.001 for $|k_T|/|q_T|=1,0.3,0.1,0.03,0.01,0.001$.
  * Light-like lines: $-J\cdot J=4(v_A\cdot v_B)^2/(k_T^2q_{1T}^2q_{2T}^2)$ to $4\times10^{-11}$.
* The final review's independent implementation (`final_review_scripts/fr_p5_lipatov.py` → `final_review_logs/fr_p5_lipatov.log`: line-part violation up to 99%, $|L_A+L_B|^2$ gauge difference up to $3.9\times10^3$, conservation with the three-gluon term to $3\times10^{-15}$, gauge independence to $10^{-11}$) agrees.
* `review_r3_2_scripts/r3_P5_cut_structure.py`: interference/full $=2.9$–$3.5$ at $Y=0.5$, $1.005$–$1.12$ at $Y=3$, and $1.000001$ at $Y=8$.

**Novelty.** The formulation is ours; the substance is standard (BFKL). Withdrawn (§16): the round-2 identity $D_{\mathsf C}=\int d\Phi_3|A^{\rm lines}|^2$ and its justification (item 31); the final-round claims "common factor $1/\mathbf q_T^2$" and "$|A_A+A_B|^2$ is gauge invariant because $k\cdot(J_A+J_B)=1-1=0$" (item 44).

[[VERBATIM final.md 1293-1333]]

(Items 1–4 below are our summary. DGOPS themselves present the argument as six numbered steps at the beginning of their §4 (arXiv v1, pp. 38–41). The steps are formulated for double DY, and DGOPS state that the refinement applies equally to single DY. Below, "DGOPS step $n$" always refers to that list, not to items 1–4: step 3 (p. 39) contains the routing assumption, and step 6 (p. 40) the removal of failures of the approximations in larger regions by subtraction terms. Verified in `final2_logs/lit_checks_final2.log`.)
[[VERBATIM final.md 1334-1357]]
**Conclusion.**

* No gap is identified in the graph-by-graph argument for the coincident patterns studied here. T3's unregulated residual is not stable under in-window $k^-$ regulators (T3(e)). In the subtraction formalism, the region of large $|k^-|$ belongs to the subtraction term of the region in which the gluon is $B$-collinear: DGOPS's own step 6 (their §4, p. 40) states that failures of the approximations in larger regions are removed by subtraction terms.
* Every statement here that an `asm:appO-mixing`(c)-type assumption is "needed" or "not needed" is relative to App O's two-time framework.
* The graph-by-graph argument has its own stated inputs: the routing assumption of DGOPS's own step 3 (their §4, p. 39), the validity of LCPT (zero modes, instantaneous vertices), and the region/subtraction formalism. App O shares them in other forms (`asm:appO-lcopt`, `asm:appO-mixing`(a′), `asm:appO-deformation`).
[[VERBATIM final.md 1363-1418]]
**Correction.**

1. *Location of the error.* The error lies in the **expectation** that this mechanism is insufficient within $\mathcal G_0$, for the uncut direct lines, and that the three-gluon-vertex graphs are needed. The only reason the reference gives is that the colour structures coincide (Ex. E.38(4)), and a coincidence of colour structures is not an argument for non-cancellation.
2. *Eikonal lines.* For two straight eikonal lines, box and crossed box alone give $\mathcal V^\dagger\mathcal V=1+O(\chi^3)$ (ERR-S1; $p_{\rm opp}=-iY/\pi$; `prop:dy-eikonal-twogluon`).
3. *Composite spectators.* In $\mathbb M_{\rm glob}$, at $O(g^4)$, for the fully coincident SS pattern, the $C_AX$ part of the side sum of the **uncut** direct lines cancels once the window is combined with the near-shell region of the same uncut lines. This holds **pointwise**: on $\mathcal N_A\cap\mathcal N_B$ in the unregulated model (T2(a); a model theorem, [P] as a QCD statement), and on $\mathcal N_B$ with the in-window class-$\mathfrak X_1$ $k^+$ regulator (T2′(a)). At these points the near-shell part of the uncut direct lines therefore supplies the whole $-\frac14C_A\chi^2X$ for this pattern. With in-window two-sided regulators that retain the near-shell segment ($K^+K^-\gg\mathbf k_T^2$), the model has ${\rm Re}\,p_{\rm opp}\to0$ for the uncut lines (T2′(c), numerics [P]). Off $\mathcal N_A$ and without regulator, the uncut side sum keeps the end-pole term $\Pi$ of T2′(b) ($\Pi=0.2517$ for the apole set).
4. *Consistency.* Two-particle unitarity of box plus crossed box for on-shell lines (P3) agrees.
5. *Consequence.* If E.33(c2) holds for the complete set, the remaining contributions must together have zero net Hermitian $C_AX$ part at leading power. These are the **cut** direct lines (real emission, which also belongs to $\mathcal G_0$) and the three-gluon-vertex graphs. Neither group is computed here (OPEN-13; slot X1e).

**What stays.**

* E.33(c2), i.e. `asm:appO-mixing`(c), remains an assumption about the complete set. It is still needed for the $O(g^6)$ ladder class (P5, [A]) and for coincident SA/AS insertions and H-emission endpoints (Remark P6).
* The reference's conclusion "within $\mathcal G_0$ the residual should not be expected to vanish" is contradicted for the uncut-line part **pointwise**: on $\mathcal N_A\cap\mathcal N_B$ in the unregulated $\mathbb M_{\rm glob}$ (T2(a)), or on $\mathcal N_B$ with the in-window class-$\mathfrak X_1$ $k^+$ regulator (T2′(a)). Off $\mathcal N_A$ the unregulated uncut side sum keeps the non-zero end-pole term of T2′(b) (e.g. ${\rm Re}\,p_{\rm opp}\to0.2517$ for the apole set). The spectator-integrated statement, which is what the reference's remark concerns, therefore holds here only under `asm:appO-collinear-ends` (in-window regulators), and only on the part of spectator phase space where at least one NF condition holds ($\mathcal N_B$ with the $k^+$ regulator, $\mathcal N_A$ with the mirror $k^-$ regulator); the rest is OPEN-2.
* Whether the full $\mathcal G_0$ sum at $O(g^4)$, including the cut direct lines, cancels is **open** (OPEN-13). For the complete $\mathcal G_0$ the reference's expectation is neither established nor refuted.
* The strict window-localized expression does not cancel (`lem:appO-joint-localization`(c)); P2 quantifies its regulator dependence.
* Under `asm:appO-collinear-ends`, the content of E.33(c2) for the coincident $O(g^4)$ patterns is relocated to the matching at the collinear ends.
* This is not a refutation of App E.

**Status.** T2(a) (model theorem, pointwise; [P] as a QCD statement) + [P] (T2′(c)); the regulated pointwise statement is T2′(a) (model theorem, [P]). The status "[R, R_cond]" of the final report, which had no premise list, is withdrawn. FINAL_OUTLINE_v2 §00.5 already uses this restricted wording.

[[VERBATIM final.md 1437-1438]]
## 13. Register consequences

All "needed / not needed" statements below are relative to App O's two-time framework (§10).

| register entry | effect of this report |
|---|---|
| `asm:appO-lcopt` | unchanged; it is the premise of (SEC) and of P1 and T1 |
| `asm:appO-envelope` | reworded in v2.3: for coincident connections, imposed on side-summed families (§2.3). The per-graph version is incompatible with P4 within the class; open for graph-generated jets (OPEN-10) |
| `asm:appO-mixing`(a) | replaced by (a′) in v2.3 (L7, §2.3) |
| `asm:appO-mixing`(b) | unchanged |
| `asm:appO-mixing`(c) | see the list below |
| deleted clause (c1) | superseded by L1 together with `asm:appO-envelope` on side-summed families |
| `asm:appO-deformation` | (c) also receives the out-of-window parts of P1's windows and the wee-line endpoint region of P1(c); for (d) see Remark P6 |
| `asm:appO-rewritten-cs` | unchanged |
| new (registered v2.3, confirmed LA-2) | `asm:appO-adjacent-swap` [\tagP], `asm:appO-real-jets` [\tagP], `asm:appO-collinear-ends` [\tagA] (§2.2, with all fields); none of them is a premise of `thm:appO-main` or `thm:dy-factorization` |

**`asm:appO-mixing`(c), pattern by pattern.**

* **Commuting patterns:** not needed (T1, [R, R_cond: `asm:appO-lcopt`]; its integrated form uses `asm:appO-envelope`, exactly as `prop:appO-ss-cancel`(iii) does).
* **Fully coincident SS–SS pairs at $O(g^4)$, uncut lines:** proved in the model with the class-$\mathfrak X_1$ $k^+$ regulator **alone**, pointwise on $\mathcal N_B$ (T2′(a), explicit bound; mirror statement with a $k^-$ regulator on $\mathcal N_A$). This is the in-window form of `asm:appO-collinear-ends` for this pattern. The two-sided version ($K^+K^-\gg\mathbf k_T^2$) is numerics [P] for one jet pair (T2′(c): Lorentzian regulators, jet $A$ localized). Without regulator the cancellation holds pointwise on $\mathcal N_A\cap\mathcal N_B$ (T2(a)); off $\mathcal N_A$ the end-pole term survives (T2′(b)). Configurations where both NF conditions fail are OPEN-2.
* **Half-coincident SS pairs at $O(g^4)$, uncut lines:** proved in the model with the $k^-$ regulator **alone**, with an explicit bound (T3(e)). Adding the class-$\mathfrak X$ $k^+$ factor of the two-sided window is expected to cost $O(a/(K^+K^-))$; this is not proved.
* **Cut direct lines** (real emission) of both coincident patterns at $O(g^4)$: open (Remark C, OPEN-13). In the unregulated model they are not expected to be suppressed. Under the two-sided regulators, power counting suggests suppression; this is to be proved.
* **The fully coincident two-line ladder class from $O(g^6)$ on:** needed, argued [A] (P5). It is expected, not shown, for the other coincident patterns from $O(g^6)$ on.
* **Coincident SA/AS insertions and H-emission endpoints:** needed (Remark P6).

**Proposed status sentence for `asm:appO-mixing`.** "(c) holds for two-gluon exchange between eikonal lines at $O(g^4)$ (`prop:dy-eikonal-twogluon`). For composite spectators in the global two-time model, the uncut-line part of the fully coincident $O(g^4)$ family cancels pointwise on NF, and with an in-window $k^+$ regulator pointwise on $\mathcal N_B$ (`prop:appO-twoexch-spectator`, `prop:appO-twoexch-regulated`, model theorems). Cut direct lines, the half-coincident pattern at the collinear ends, $O(g^6)$ and coincident SA/AS insertions are open."

**Overall.** `thm:dy-factorization` stays [A]. The report upgrades sub-steps only within App O's framework. Its TMD versions are [C].

---

[[VERBATIM final.md 1470-1510]]

* The slope of ${\rm Im}\,p_{\rm opp}$ tends to $-2/\pi$ per unit $\ln(1/\lambda)$ unregulated, and to $-1/\pi$ regulated.
* $N/N_0\to1$ ($0.9998$ at $\lambda=0.003$).
* *Normalization.* In all rows the decay of ${\rm Re}\,p_{\rm opp}$ is dominated by the cross term $-{\rm Im}\,X_w{\rm Im}\,Y/|Y|^2$. The $C_AX$ coefficient ${\rm Re}\,X_w$ is much smaller: $2.6\times10^{-4}\to0.9\times10^{-6}$ for the base row, and $-5.1\times10^{-4},-1.6\times10^{-4},-5.4\times10^{-5}$ for the class-$\mathfrak X$ base row (`final2_logs/t2_numerics_refit.log`).
* *General jets.* A non-factorized pair whose $J_A$ violates both $\mathcal N_A$ and (REAL) tends to its end-pole value $\Pi=0.1124$ without regulator, and to 0 with the class-$\mathfrak X$ regulator (T2′(a), (b); `final2_logs/t2p_general_regulated.log`).
* The half-coincident, colour, two-sided-regulator and P4 numbers are given under T3, L4, T2′(c) and P4.

### 14.4 Log account (honest history)

[[VERBATIM final.md 1518-1522]]
6. `final_scripts/p5_interference.py` (final round) built in equal normalization of the two line currents ($v_X/(v_X\cdot k)$, no exchange propagators). Its "gauge invariance of $|A_A+A_B|^2$" was therefore circular, and the claim it supported was false (Fix 1). It is superseded by `final2_scripts/p5_lipatov_check.py`, which includes the propagators $1/q_2^2$, $1/q_1^2$ and the three-gluon term.
7. `final_scripts/t2_constants.py`, part (2), does **not** recompute anything. It re-tabulates ${\rm Im}\,p_{\rm opp}$ values from logged runs (`logs/twoexch_rotated_fast2.log`, `logs/twoexch_exact2_0.003_base.log`, `review_r3_1_logs/t2_general.log`) and forms ${\rm Im}\,p_{\rm opp}+\frac1\pi\ln\frac1\varepsilon$; the final report did not say so (Fix 7(e)). The same remainders are re-derived from the parsed log in `final2_logs/t2_numerics_refit.log`, part (4).
8. An earlier draft of this revision, written before the session was interrupted, left `new_constants_arith.py/.log`. It used an unprinted bookkeeping for the T2′(a) and T3(e) coefficients, so it has been moved to `final2_scripts/superseded/` (with a README) and is not cited. The printed constants are those of `final2_scripts/final2_constants.py`.
9. While writing the complete proofs of this revision, the author found that L8(h) as stated in the final round is false for multi-state gaps (explicitly from five states in one gap on). It is corrected with the $\pi/4$ norms; `final2_logs/l8h_modified_norms.log` contains the counterexample.

### 14.5 Scripts and logs

All paths are relative to `verify/extend/X1-glauber/`.

**Original run** (`scripts/`, `logs/`):

* two-exchange model: `twoexch_model.py`, `twoexch_exact.py`, `twoexch_rotated_fast(2).py`, `twoexch_regulated.py`, `twoexch_bruteforce.py`, `test_twoexch_parts2.py`;
* half-coincident: `halfcoinc.py`, `halfcoinc_real.py`, `halfcoinc_sym.py`;
* checks: `checks_misc.py`, `checks_C2_C3_C4.py`, `check_halfcoinc_colour.py`, `check_halfcoinc_singlets_v2.py`.

**Fix round 1** (`fix_r1_scripts/` → `fix_r1_logs/`): `regulator_indep.py` (regulator studies A, B), `colour_dy_check.py`, `p4_perturbation.py`.

**Fix round 2** (`fix_r2_scripts/` → `fix_r2_logs/`): `l1_bound_quadrant.py`, `p2_window_shape.py`, `l8_bounds.py`, `p4_regulated_B.py`, `t3e_sensitivity.py`.

**Final round** (`final_scripts/` → `final_logs/`):

* `p2_orientation.py`: exact sector-sum weights by iterated residues; orientation of $\delta_B$.
* `p5_interference.py`: **superseded** (circular gauge-invariance check; §14.4, item 6).
* `t3f_recompute.py`: recomputation of T3(e′),(f), and boost invariance of the T3(e) terms.
* `t2_constants.py`: part (1) checks (A3) and the decay bound of $\varrho$ on 400 random multi-state jets; part (2) re-tabulates logged values (§14.4, item 7).

**Final review** (`final_review_scripts/` → `final_review_logs/`): `fr_p5_lipatov`, `fr_l4_colour`, `fr_t3e_vK`, `fr_t2_A4`, `fr_endpole_L6`, `fr_t2_constants_arith`.

**Final revision 2** (`final2_scripts/` → `final2_logs/`), all ALL PASS:

* `p5_lipatov_check.py`: P5 with the exchange propagators and the three-gluon term (Fix 1(d)).
* `vK_hand_proof.py`: every step of the hand proof of Lemma V (Fix 5).
* `vK_bounds_proof.py`: independent polynomial certificate for Lemma V(b); the closed form of $c_U(t)$, its maximum and the analytic bound $(3+\sqrt2)/2$ (Fix 5).
* `a4_crho_check.py`: (A4) with the derived $c_\rho$ (Fix 7(a)).
* `l8h_modified_norms.py`: counterexample to the final-round L8(h) and test of the corrected L8(h).
* `final2_constants.py`: arithmetic of every new explicit constant (T2(a) Step 8, (A4), T2′(a), T3(b), T3(e), P4, L8(i)); the monotonicity lemma; two geometric integrals; $\sum|w|$ of the L1 counterexample (Fix 4, Fix 7(a), (c)).
* `t2_numerics_refit.py`: LA-5 exponents and slopes, the normalization decomposition, and ${\rm Im}\,p_{\rm opp}+L/\pi$ (Fix 7(b)).
* `t2p_general_regulated.py`: T2′(a), (b) on a general jet pair whose $J_A$ violates $\mathcal N_A$ and (REAL). It imports the round-3 integrator unchanged.
* `lit_checks_final2.py`: the INSPIRE record of Barcaro et al. and DGOPS's own six-step list (Fix 7(d), (e)). It reads the text of the arXiv v1 PDF from a path argument.

**Reviewer checks.**

* Round 1: `review_r1_1_scripts/`, `review_r1_2_scripts/` with `review_r1_2_logs/`.
* Round 2: `review_r2_1_scripts/` with `review_r2_1_logs/`; `review_r2_2_scripts/` (chkA–chkE).
* Round 3: `review_r3_1_scripts/` with `review_r3_1_logs/` (general non-factorized jets for L8 and T2; the P4 partner; T3(e) constants; P2); `review_r3_2_scripts/` (L8, P5 cut structure, T3(e) constants, P2, INSPIRE searches).

The integral form of every result still needs `asm:appO-envelope` on side-summed families.

---

## 15. Novelty ledger

"Ours" means new to our knowledge after the literature checks described below. 「本书给出的推导」 means that the statement is an instance of a known theorem or a standard technique, and only the derivation in the present setting is ours. No novelty marker is printed in the monograph for any result of this report (FINAL_OUTLINE_v2 §00.4; WRITER_SPEC_v2 §6.5; OPEN-8 also remains open).

| result | status | prior work and references |
|---|---|---|
| L1 | partly known | Known: the race formula (reference App E.4.4; `lem:appO-joint-localization`(a)) and $\sum w=1$ (the eikonal identity; Aybat–Sterman 2009, eq. (10)). (a) and its exactness at finite $\eta$: 本书给出的推导 (residue calculus on the LCOPT sector form). (b), (b1), (d): ours as stated (elementary); printed as a sharpened result without marker (N13) |
| L1′ | 本书给出的推导 (elementary) | partial fractions and multilinearity applied to L1 |
| L2 | 本书给出的推导 | a consequence of L1(c); corrects the wording of REFDOC ERR-S3 |
| L3 | 本书给出的推导 | an explicit instance of L1 |
| L4 | (a) known; (b)–(d) ours as statements; (d2) elementary linear algebra | (a): reference Ex. E.38 / `lem:appO-glauber-operator`. Colour-singlet-target mechanism: Lindsay–Ross–Sachrajda 1983. Context: Catani–de Florian–Rodrigo 2012; Forshaw–Seymour–Siodmok 2012; Barcaro–Gao–Gaunt–Pathak 2026 |
| L5 | 本书给出的推导 | a contour rotation of Wick type; holomorphy domains and arc estimates ours |
| L6 | 本书给出的推导 | an instance of Cauchy's theorem; its role in T2, T2′ ours |
| L7 | 本书给出的推导 (elementary) | its use as a replacement of `asm:appO-mixing`(a) is ours |
| L8 | ours as stated (elementary) | — |
| Lemma V | ours as stated (elementary inequalities for explicit rational functions) | — |
| T1 | known statement; the uniform route is 本书给出的推导 | `prop:appO-ss-cancel`(iii); reference Props E.35, E.31(iii) |
| P1 | ours | idea suggested without proof in the reference work notes (R7) |
| T2 | physical cancellation known in models; the general derivation is ours | Lindsay 1984; Brandt–Frenkel–Taylor 1989; reggeization reading: Lipatov 1976, Kuraev–Lipatov–Fadin 1977, Rothstein–Stewart 2016. Ours: general-LCOPT derivation with explicit estimates, ray-identity mechanism, regulator analysis; extends ERR-S1 |
| T2′ | ours | end-pole formula; regulated proof with explicit constants; two-sided regulator study (model statements) |
| P2 | (a) known; (b), (c) ours (elementary) | (a): reference Lemma E.48(d); `lem:appO-joint-localization`(c) |
| P3 | known in substance; 本书给出的推导 | Cutkosky 1960; Veltman 1963; 't Hooft–Veltman; ERR-S1 / `prop:dy-eikonal-twogluon` |
| T3 | ours | the configuration does not occur in Lindsay 1984, Brandt–Frenkel–Taylor 1989 or Lindsay–Ross–Sachrajda |
| P4 | ours | sharpens ERR-S3 |
| P5 | formulation ours; substance standard | BFKL; Lipatov 1976; Kuraev–Lipatov–Fadin 1977; Del Duca 1995; Schwartz–Yan–Zhu 2018; Rothstein–Stewart 2016 |
| Remark P6 | refinement | `asm:appO-deformation`(d), `rem:appO-h-emission` |
| Remark C | observation (power counting only) | — |
| ERR-S1b | erratum item | addendum to ERR-S1 |

**Literature checks.**

* Bibliographic data for every entry of §19 were verified on INSPIRE by reviewers in rounds 1–3 (`review_r3_2_scripts/logs/r3_inspire_refs.log`). Barcaro et al. was re-checked in this revision: INSPIRE record 3181016 (texkey `Barcaro:2026dsd`), "Collinear Factorization Violation and Reggeization", D. Barcaro, A. Gao, J.R. Gaunt, A. Pathak, arXiv:2607.14259, report numbers DESY-26-091 and SLAC-PUB-260713, preprint date 2026-07-15 (`final2_logs/lit_checks_final2.log`).
* Novelty searches by reviewers in rounds 1–3 found no prior statement of T2 for general LCOPT jets, of T3's configuration, of P1, P2(b), P4 or L8 (`review_r3_2_scripts/logs/r3_inspire_novelty*.log`, `r3_inspire_citers.log`). They covered title searches (Glauber with spectator, Glauber with Drell–Yan, spectator interactions, cancellation, factorization) and the Glauber/spectator citers of DGOPS, Aybat–Sterman and Rothstein–Stewart.
* Not accessed: CSS NPB 308 (1988) 833 and Collins 2011 §14.4 (OPEN-8).

---

[[VERBATIM final.md 1591-1643]]

**Withdrawn or corrected in this revision 2 (final review and author):**

44. P5: "the common factor $1/\mathbf q_T^2$" (radiation from $A$ carries $1/q_2^2$, radiation from $B$ carries $1/q_1^2$), and "$|A_A+A_B|^2$ is gauge invariant because $k\cdot(J_A+J_B)=1-1=0$" (false: $k\cdot(A_A+A_B)=C(v_A\cdot v_B)(1/q_2^2-1/q_1^2)$). Also the circular check `final_scripts/p5_interference.py` (Fix 1).
45. ERR-S1b and the T2 relation to the reference: "contradicted for the uncut-line part" without the pointwise qualifier; the status "[R, R_cond]" without a premise list (Fix 2).
46. The self-declared rule "[R, R_PT] = pure mathematics about defined classes"; the grade [R, R_PT] for L2, L5, L6, L8 (now (数学)) and for the model theorems T2(a), T2′(a),(b), T3(b),(c),(e), P4(a),(b) (now [P] with complete model-internal proofs); "content [P]" transfer items with unregistered † premises (Fix 3; LA-2).
47. Informal hypotheses ("$\ll$", "up to logarithms", "$+O$(power)", "$o(1)$", "smallness conditions of the type (iv), (v)") in T2′(a), (b), T3(b), (e), P4(a), (b), and the constant slip $|\chi_1\chi_2-1|\le2R/K_c$ (it is $3R/K_c$) (Fix 4).
48. T3(e), step (3): the inequalities $|v_K|\le(|x_1|+|x_2|)/4$ and $|v_K|\le\frac12$ asserted without proof (now Lemma V, which also shows that the first holds for all $x$); $c_U=1.6485$ used as a proven constant (now the analytic bound $(3+\sqrt2)/2$) (Fix 5).
49. §13: "not needed (T1, unconditionally)"; the fully coincident bullet citing T2′(a) and (c) jointly as if both were proven (Fix 6).
50. L1 verification: "$\sum|w|=44.7$" (it is 89.0; 44.7 is $\max|w_\sigma|$). T2 numerics: "${\rm Re}\,p_{\rm opp}\to0$ roughly as $\varepsilon^{0.7}$ to $\varepsilon^{0.77}$" and "falls by 0.717–0.730 per decade" (now the refit values 0.63, 0.70, 0.73 and first-decade slopes 0.680–0.717; LA-5) (Fix 7(b), (c)).
51. L8(h): "(b)–(g) hold with every constant multiplied by 8" with the original norms $M$, $M^\flat$. This is false for multi-state gaps (possible once $d_t\ge3$; an explicit five-state counterexample is logged); it is corrected with the $\pi/4$ norms (found by the author).
52. T2′(a): the final-round proof did not control the variation of the regulator across the strips. The theorem is now stated for the class $\mathfrak X_1$ (Lipschitz bound), which contains the example of D8 (found by the author).
53. T2, consequences: "the side-sum residual $-\frac12C_A\chi^2({\rm Re}\,p_{\rm opp})X$ of the uncut lines is power suppressed", stated without the normalization caveat. The $C_AX$ coefficient is $\propto{\rm Re}\,X_w$ and bounded without hypothesis (v); the colour-abelian $X^2$ coefficient is OPEN-14 (found by the author).
54. (A4): "$c_\rho\le50(2\bar n_A-1)m^\flat_A(a_{\max}/a_{\min})^2(\lambda_A/\mu_A)^2$", stated without derivation. It is now derived, with the smaller constant $36(2\bar n_A-1)m^\flat_A(a_{\max}/a_{\min})(\lambda_A/\mu_A)^2$ (Fix 7(a)).
[[VERBATIM final.md 1644-1677]]
* **OPEN-12.**
  * Prove (ADJ) and (REAL) for spin-summed leading-power LCOPT jets, which would discharge `asm:appO-adjacent-swap` and `asm:appO-real-jets`.
  * Alternatively, remove (ADJ) from L8 by treating the axis bands with a kink estimate against the continuous weights (L2).
  * Sharpen the constants of L8 (numerically about 6 and 0.4, against the proven 400 and 16), the constants of T2′(a) and T3(e) (crude by several orders of magnitude; the proven $O(\eta)$ bound on ${\rm Re}\,X^\chi$ is not sharp in the scalar model, where ${\rm Re}\,X^\chi\propto\eta^2$), and the power of the logarithm in T2.
* **OPEN-13** (new in the final round). The cut (real-emission) contributions of the direct SS lines for the fully and half-coincident patterns at $O(g^4)$ (Remark C).
  * Compute them, or prove them power suppressed under the two-sided regulators; power counting suggests $O(\lambda_BK^-/a+\lambda_AK^+/a)$.
  * In the unregulated model, determine their net Hermitian $C_AX$ and $[X_1,X_2]$ parts.
  * Together with the three-gluon-vertex graphs (slot X1e), this decides the full $\mathcal G_0$ form of ERR-S1b.
* **OPEN-14** (new in this revision). The colour-abelian $X^2$ coefficient of the uncut side sum in $\mathbb M_{\rm glob}$ with exact model integrals: compare $2\,{\rm Re}\,Y$ with the configuration with one line on each side of the cut (Def. D6, normalization). It cancels identically in the localized limit; T2 and T2′ control only the non-abelian $C_AX$ coefficient.
[[VERBATIM final.md 1686-1688]]
## 18. Results table

| id | grade | status | new / known |
|---|---|---|---|
| D1–D8 | definitions (D8: classes $\mathfrak X\supset\mathfrak X_1$) | — | — |
| L1 | [R, R_PT] | proven | partly known; sharpened result |
| L1′ | [R, R_PT] | proven ($c_U\le(3+\sqrt2)/2$) | 本书给出的推导 |
| L2 | (数学) | proven | 本书给出的推导 |
| L3 | [R, R_PT] | proven | 本书给出的推导 |
| L4 | [R, R_def] | proven | (a) known; (b)–(d) ours |
| L5 | (数学) | proven | 本书给出的推导 |
| L6 | (数学) | proven | 本书给出的推导 |
| L7 | (a),(b) [R, R_PT]; (c) → assumption (a′) | proven; reformulated | 本书给出的推导 |
| L8 | (数学) | proven ((h) corrected, (i) added) | ours (elementary) |
| Lemma V | (数学) | proven | ours (elementary) |
| T1 | [R, R_cond: `asm:appO-lcopt`] (integrated form also `asm:appO-envelope`) | proven | known statement; derivation ours |
| P1 | [R, R_cond: `asm:appO-lcopt`] | proven | ours |
| T2 | [P] (model theorem) | (a) complete model-internal proof; (b) implication [R, R_cond: `asm:appO-lcopt`, `asm:appO-adjacent-swap`, `asm:appO-real-jets`], content [P]; (c) physical reading [P], conditional on `asm:appO-collinear-ends` and OPEN-13 | physical cancellation known in models; derivation ours |
| T2′ | [P] (model theorem) | (a), (b) complete model-internal proofs with explicit hypotheses and constants; (c) numerics | ours |
| P2 | [R, R_PT] | proven | (a) known; (b), (c) ours |
| P3 | content [R, R_PT] at $O(g^4)$; printed as untagged remark | proven | known in substance |
| T3 (remark) | untagged; (a), (g) [R, R_def]; (d), (f) [P] numerics | proven / numerics | ours |
| T3 (proposition: (b), (c), (e)) | [P] (model theorem) | complete model-internal proofs with explicit hypotheses and constants; (e′) numerics | ours |
| P4 | [P] (model theorem) | (a), (b) complete model-internal proofs; (c) numerics | ours |
| P5 | [A] | argued; checks with propagators and three-gluon term | formulation ours |
| Remark P6 | ungraded | argument | refinement |
| Remark C | ungraded | open (OPEN-13) | observation |
| ERR-S1b | T2(a) (model, pointwise) + [P] (T2′(c)); regulated: T2′(a) | proposed, restricted | erratum item |
| TMD | [C] | open | — |
| Inclusive DY collinear factorization | [A] | unchanged | — |

---

[[VERBATIM final.md 1729-1770]]
* D. Barcaro, A. Gao, J.R. Gaunt, A. Pathak, *Collinear Factorization Violation and Reggeization*, arXiv:2607.14259 (2026), DESY-26-091, SLAC-PUB-260713 [INSPIRE texkey `Barcaro:2026dsd`].
[[VERBATIM final.md 1772-1790]]
## Appendix A. Provenance, slot decisions and transcription notes

### A.1 Versions and reviews

**Versions.** `verify/extend_reports/`: `X1-glauber.md` (original), `X1-glauber-fix1.md` (revision after round 1), `X1-glauber-fix2.md` (revision after round 2), `X1-glauber_final.md` (final revision after round 3), and this file, `X1-glauber_final2.md` (revision 2, after the independent final review; the version from which App O is written, LA-12).

**Reviews.** `X1-glauber-rev1-1.md`, `-rev1-2.md`, `-rev2-1.md`, `-rev2-2.md`, `-rev3-1.md`, `-rev3-2.md`; `verify/extend/X1-glauber/review_r2_1.md` and `review_r3_1.md`; the independent final review `X1-glauber-finalreview.md` (verdict: fixable issues; Fix 1–Fix 7, all applied below).
[[VERBATIM final.md 1798-1820]]
The rows F3/item 3 (P5) and F6/items 5, 11 (qualifiers) were revised again in this revision (Fix 1, Fix 3). How the final-review fixes were applied is listed in the section *Final-review fixes* at the end.

### A.2 Slot decisions (App O; FINAL_OUTLINE_v2 §00.4)

* **X1c `lem:appO-side-independent-windows`: PASS.** P1, with the grade [R, R_cond: `asm:appO-lcopt`] instead of the planned [R, R_PT] (LA-2, item 4: a weakening is allowed). The premise is that of `prop:appO-ss-cancel`.
* **X1f `prop:appO-twoexch-spectator`: PARTIAL.**
  * T2 is inserted as a model theorem about the **uncut** side sum, graded [P] as a QCD statement (LA-2, item 2; WRITER_SPEC_v2 §4.3, item 4). Its first sentence names the model and states the restrictions: $\mathbb M_{\rm glob}$, $\mathcal N_A\cap\mathcal N_B$, $O(g^4)$, this pattern, uncut lines. The model-internal claim (a) has a complete proof; hypotheses (iv), (v) are part of the statement.
  * T2′ (`prop:appO-twoexch-regulated`) and P4 (`prop:appO-pergraph-weights`) are [P] in the same way, with complete proofs of (a), (b); their numerical items are [P].
  * The physical reading for $\mathcal G_0$ is [P], conditional on `asm:appO-collinear-ends` and OPEN-13.
* **X1a, X1b, X1d, X1e: not delivered.** The fallbacks stay.
* **T3:** the untagged remark `rem:appO-halfcoinc` in §O.5 and the proposition `prop:appO-halfcoinc-sensitivity` [P] (items (b), (c), (e) with complete proofs). Its physical reading is at most [P].
* **ERR-S1b:** to App Q, in the restricted wording of §12.
* **One convention throughout** (Fix 3(b)): §0.2, §18, A.2 and A.4 all use the LA-2 convention. Pure mathematics is (数学); statements about LCOPT jet factors, localized integrals or Feynman integrals are [R, R_PT]; colour algebra is [R, R_def]; register implications are [R, R_cond]; App O model theorems are [P] with complete model-internal proofs. The planned slot grade "[R, R_PT] (at $O(g^4)$, in $\mathbb M_{\rm glob}$; first sentence states it)" is **not** used.

### A.3 Proposed labels

| result | label |
|---|---|
| D1–D8 | `def:appO-sectors`, `def:appO-jet-class`, `def:appO-structural-conditions`, `def:appO-glob-model`, `def:appO-nf-domain`, `def:appO-ordering-weights`, `def:appO-rotated-notation`, `def:appO-regulator-class` (now with the subclass $\mathfrak X_1$); in FINAL_OUTLINE_v2, (SEC), (EQ), (ADJ), (REAL) are inner names of `def:appO-sectors` |
| L1, L2 | revision of `lem:appO-joint-localization` (L2 as an item marked 「（数学）」) |
| L1′ | `lem:appO-multipole-localization` |
| L3 | `lem:appO-quadrant-residues` |
| L4 | (a) `lem:appO-glauber-operator`; (b)–(d) `lem:appO-halfcoinc-colour` |
| L5 | `lem:appO-kplus-rotation` (数学) |
| L6 | `lem:appO-ray-identity` (数学) |
| L7 | `lem:appO-preintegration-localization` |
| L8 | `lem:appO-two-insertion-bounds` (数学), with (h) corrected and (i) added |
| Lemma V | inside the proof of `prop:appO-halfcoinc-sensitivity` (数学) |
| T1 | remark (alternative proof) in `prop:appO-ss-cancel` |
| P1 | `lem:appO-side-independent-windows` |
| T2, T2′ | `prop:appO-twoexch-spectator`, `prop:appO-twoexch-regulated` |
| P2 | `prop:appO-strict-window-shape` |
| P3 | `rem:appO-onshell-unitarity` |
| T3 | `rem:appO-halfcoinc`, `prop:appO-halfcoinc-sensitivity` |
| P4 | `prop:appO-pergraph-weights` |
| P5 | `prop:appO-g6-ladder` |
| Remark P6 | extension of `rem:appO-h-emission` |
| Remark C | `rem:appO-cut-ss` |

### A.4 Transcription notes

* Print grades as in §18. This is the LA-2 convention and coincides with FINAL_OUTLINE_v2 v2.3 §00.4. For each model theorem, print [P] with the first sentence given here (naming the model), followed by the complete `proof` of the model-internal claim (WRITER_SPEC_v2 §4.10, item 5). Print the QCD transfer as an item "（QCD 喷注）" stating the implication from `asm:appO-lcopt`, `asm:appO-adjacent-swap`, `asm:appO-real-jets` and its content grade [P]. Its premises appear in `\uses`.
* **Departure from rev3-2 item 11** (Fix 3(d)). Item 11 asked for the transfer items as R_cond statements with registered premises. When the final review was written, the premises were unregistered († in the final report), and the transfer items stayed PENDING-VERIFY. Since then the entries `asm:appO-adjacent-swap`, `asm:appO-real-jets` (\tagP) and `asm:appO-collinear-ends` (\tagA) have been registered (FINAL_OUTLINE_v2 v2.3 §08) and confirmed by LA-2. The † marks are therefore removed and no PENDING-VERIFY marker is needed for them. The remaining departure is deliberate: the theorems are printed as [P] model theorems (LA-2) with the transfer as an item, not as stand-alone R_cond statements.
* **Spec entries to update in CHANGELOG v2.4** (LA-12; writers use this report): `def:appO-regulator-class` (subclass $\mathfrak X_1$); `lem:appO-two-insertion-bounds` ((h) with the $\pi/4$ norms; (i)); `lem:appO-multipole-localization` (analytic bound on $c_U$); `prop:appO-twoexch-spectator` (bound on ${\rm Re}\,X_w$; normalization remark; constants of Step 8; (A4) constant); `prop:appO-twoexch-regulated` ((a) for class $\mathfrak X_1$ without $\mathcal N_A$ and without (REAL) for $J_A$, explicit hypotheses and constants; (b) with the general end-pole value $\Pi$ and explicit error); `prop:appO-halfcoinc-sensitivity` (explicit hypotheses and constants; Lemma V; $\pi/4$ norms); `prop:appO-pergraph-weights` (explicit (a), (b)); `prop:appO-g6-ladder` (already consistent with Fix 1 in the outline wording); App Q ERR-S1b (status line).
* No novelty marker is printed (FINAL_OUTLINE_v2 §00.4). Instances of known theorems are introduced as 「本书给出的推导」 (§15).
* Locations (LA-7): every literature location used here was verified (DGOPS steps 3 and 6, §4 pp. 39–40 of arXiv v1; Barcaro et al. INSPIRE record). The disclosures "read in part" (CdFR) and "read §4" (Boer et al.) describe the extent of reading; they are not location markers. Nothing in this report is marked 「位置待核实」.

---

## Additional corrections found in this revision

These were not flagged by the final review. The author found them while writing the complete proofs that Fix 4 and LA-2 require.

1. **L8(h) was false as stated.** With the original norms, "(b)–(g) hold with every constant multiplied by 8" fails for multi-state gaps (it can fail once a term has $d_t\ge3$ extra states; an explicit five-state counterexample is logged): on the $\pi/4$ ray each extra state costs $\sqrt2/\mu$ instead of $1/\mu$. It is corrected with the $\pi/4$ norms $M_{\pi/4}$, $M^\flat_{\pi/4}$; these equal $M$, $M^\flat$ in the scalar model, so all scalar-model statements are unaffected. Evidence: counterexample and test in `final2_logs/l8h_modified_norms.log`. Affected: T3(e) constants (now with $m'_B$, $m^\flat_{A,\pi/4}$).
2. **T2′(a) needed a Lipschitz condition on the regulator.** The final-round proof did not control the variation of $\chi$ across the strips (the term $P_5$), which sup bounds on the closed quadrant do not control at the boundary. D8 now defines the subclass $\mathfrak X_1$ ($|\chi'|\le K_c^{-1}\min(1,K_c^2/|k|^2)$), which contains the example used everywhere. T2′(a) is stated for $\mathfrak X_1$.
3. **T2′(a) needs neither $\mathcal N_A$ nor (REAL) for $J_A$; T2′(b) holds without (REAL) for $J_A$.** The $-\frac12$ is produced by the ray identity applied to the regulator $\psi$ alone, and the end-pole value has the general form $\Pi$. This is a strengthening, supported by the general-jet test `final2_logs/t2p_general_regulated.log`, in which $J_A$ violates both.
4. **Normalization.** The physically relevant $C_AX$ coefficient of the uncut side sum is $-\frac12C_A\chi^2{\rm Re}\,X_w$ with $X_w=p_{\rm opp}N/N_0$. T2's proof bounds it by $\mathcal E_{\rm tot}$ without hypothesis (v) and without the factor $(1+L)$. ${\rm Re}\,p_{\rm opp}$ contains the cross term with ${\rm Im}\,Y$, which dominates the observed decay. The colour-abelian $X^2$ coefficient is not addressed by T2 (OPEN-14). D6, L4(a) (through D6), T2 and T2′ are updated.
5. **(A4)** is derived with a smaller constant, and the monotonicity of $\varepsilon^{1/2}(1+L_B)^2$ is proved (it was used without proof in the final round).
6. **Lemma V** shows that $|v_K|\le s/4$ holds globally and that the remainder of the linear approximation is cubic. As a result $|v_K|\le\min(\frac12,KR/a_{\min})$ replaces $\min(\frac12,8KR/a_{\min})$.

---

## Final-review fixes

Mapping of every required fix of `X1-glauber-finalreview.md` to the change made in this revision.

### Fix 1 — P5

* **(a)** The "common factor $1/\mathbf q_T^2$" is replaced. §9 P5(ii) now gives $A_A^\mu=C(v_A\cdot v_B)v_A^\mu/((v_A\cdot k)q_2^2)$ and $A_B^\mu=-C(v_A\cdot v_B)v_B^\mu/((v_B\cdot k)q_1^2)$ with $q_1+q_2=k$, $v_A\cdot q_1=0$, $v_B\cdot q_2=0$, and explains why radiation from $A$ carries $1/q_2^2$ (the exchanged gluon carries the momentum transferred to $B$).
* **(b)** The claim "$|A_A+A_B|^2$ is gauge invariant because $k\cdot(J_A+J_B)=0$" is deleted. P5(iii) gives $k\cdot(A_A+A_B)=C(v_A\cdot v_B)(1/q_2^2-1/q_1^2)\neq0$; states that current conservation and gauge independence need the three-gluon (central Lipatov) term $A_3$, with $k\cdot(A_A+A_B+A_3)=0$; and that the line parts alone suffice only in the limit $q_1^2=q_2^2$ ($|k_T|\ll|q_T|$).
* **(c)** Positivity is kept in the form $2C^\dagger C(v_A\cdot v_B)^3/((v_A\cdot k)(v_B\cdot k)q_1^2q_2^2)>0$. The comparison with $\int|A_A+A_B|^2$ in Feynman gauge is stated: the integrand of $D_{\mathsf C}$ is at least $|A_A+A_B|^2_{\rm Feyn}$, with equality for light-like lines, and the ratio of self terms to interference is given explicitly ($\approx1/\cosh Y$ for central emission).
* **(d)** The circular check is replaced by `final2_scripts/p5_lipatov_check.py` (propagators and three-gluon term included, as in `final_review_scripts/fr_p5_lipatov.py`). P5 Verification, §14.4 item 6, §14.5 and §16 items 31, 44 are updated. Conclusions and grade [A] are unchanged.

### Fix 2 — ERR-S1b

* "Contradicted for the uncut-line part" is now qualified everywhere it occurs (§12 Correction item 3 and "What stays", T2 "Relation to the reference", §0.2 row, §0.3): pointwise on $\mathcal N_A\cap\mathcal N_B$ in the unregulated $\mathbb M_{\rm glob}$ (T2(a)), or on $\mathcal N_B$ with the in-window class-$\mathfrak X_1$ $k^+$ regulator (T2′(a)). Off $\mathcal N_A$ the unregulated uncut side sum keeps the non-zero end-pole term of T2′(b) (${\rm Re}\,p_{\rm opp}\to0.2517$ for the apole set). The spectator-integrated statement, which the reference's remark concerns, holds only under `asm:appO-collinear-ends` and only where at least one NF condition holds; the rest is OPEN-2.
* The status "[R, R_cond]" (no premise list) is replaced by "T2(a) (model, pointwise) + [P] (T2′(c))", with the regulated statement T2′(a) added (§12, §0.2, §18).

### Fix 3 — Grade system

* **(a)** The self-declared rule "[R, R_PT] = pure mathematics about defined classes" is removed from the opening paragraph. L2, L5, L6, L8 (and the new Lemma V) are marked (数学). [R, R_PT] is kept for L1 (revision of `lem:appO-joint-localization`), L1′, L3, L7, P2 and the content of P3.
* **(b)** One convention is chosen and applied in §0.2, §18, A.2, A.4 and in every theorem header: LA-2 / WRITER_SPEC_v2 §4.3 item 4. T2, T2′, T3's proposition ((b), (c), (e)) and P4 are [P] QCD statements whose first sentence names $\mathbb M_{\rm glob}$ (Chinese first sentences given), each with a complete proof of the model-internal claim. The alternative "[R, R_PT] (at $O(g^4)$, in $\mathbb M_{\rm glob}$)" is explicitly not used (A.2).
* **(c)** §0.2 now gives T3(a) (and (g)) as [R, R_def], as in the body and §18.
* **(d)** The departure from rev3-2 item 11 is recorded in A.4. Because the three entries have since been registered (v2.3) and confirmed by LA-2, the † marks are removed and no PENDING-VERIFY marker is needed for them; the transfer is an item of each [P] theorem (content [P]).

### Fix 4 — Explicit hypotheses and constants

* **T2′(a):** hypotheses (i), (ii′), (iii′), (iv′) $16\lambda_B\le K_c\le a_{\min}/(2\lambda_A)$ (equivalent to the reviewer's $4\lambda_B\le(\lambda_BK_c)^{1/2}\le K_c\le a_{\min}/(2\lambda_A)$), and (v′) $\delta^\chi_Y\le\frac12$, the analogue of (v). Explicit $\mathcal E^\chi_{\rm tot}$, $\delta^\chi_Y$, $C^\chi_X$; complete proof, Steps 0$^\chi$–7$^\chi$. The slip $|\chi_1\chi_2-1|\le2R/K_c$ is corrected to $3R/K_c$ (D8; Step 0$^\chi$).
* **T2′(b):** "$+O$(power)" is replaced by $|{\rm Re}\,X_w-\Pi|\le\mathcal E_{\rm tot}$ and $|{\rm Re}\,p_{\rm opp}-\Pi|\le C_T\varepsilon^{1/2}(1+L_B)^2(1+L)$, under the hypotheses of T2 with $\mathcal N_A$ dropped; $\Pi$ is defined explicitly and equals the residue formula under (REAL).
* **T3(b):** hypotheses (H0), (REAL) for $J_B$, $\varepsilon\le r^{-1/2}/8$, $\delta_b\le\frac12$; explicit $|\Delta X|$, $\delta_b$, $|V|$, $|E_b|$.
* **T3(e):** hypotheses (H0), $2\lambda_A\le K\le a_{\min}/(8\lambda_B)$ (non-empty iff $\varepsilon\le r^{-1/2}/16$), and $|N(K)/N_0-1|\le\delta_N(K)\le\frac12$ with $\delta_N(K)$ explicit; explicit constants. Because Lemma V gives $|v_K|\le s/4$ for all $x$, the split is at $a_{\min}/(2K)$, and the reviewer's suggested condition $a_{\min}/(16K)\ge4\lambda_B$ is weakened to $a_{\min}/(2K)\ge4\lambda_B$.
* **P4(a), (b):** "$O(\lambda_B/K)$", "up to $O(\lambda_AK/a_{\min})$" and "$o(1)$" are replaced by the explicit decomposition $W(12,21)=W^{\rm in}_D+W^{\rm out}+R_{P4}$ with $|R_{P4}|$ explicit, and by $\delta W=-\frac{is}{2\pi}I_2+\delta R$ with $|\delta R|$ explicit and an explicit $\varepsilon$-threshold for $\delta W\neq0$.

### Fix 5 — T3(e) step (3) and $c_U$

* Lemma V (数学) proves $|v_K|<\frac12$ and $|v_K|\le(|x_1|+|x_2|)/4$, the latter for **all** $x$ (stronger than needed). It also proves the cubic remainder bound for $v_K-(x_1-x_2)/4$. The proof is by hand: closed forms from the nine pole pairs, reduction to one sign pattern, and the decomposition $A^2-|N|^2=\sum_{i=1}^5G_i$ with each $G_i\ge0$. Scripts: `vK_hand_proof.py` (every step) and `vK_bounds_proof.py` (independent certificate).
* $c_U$: the analytic bound $c_U\le(3+\sqrt2)/2\le1+\sqrt2$ is proved from the closed form of $c_U(t)$ (L1′ example). All constants of T3(e) use it; 1.64853 is quoted only for orientation.

### Fix 6 — Register and §13 consistency

* **(a)** The fully coincident bullet of §13 now says that the uncut-line statement is proved with the class-$\mathfrak X_1$ $k^+$ regulator alone (T2′(a)), and that the two-sided version is numerics [P] for one jet pair (T2′(c): Lorentzian regulators, jet $A$ localized).
* **(b)** `asm:appO-collinear-ends` has its 地位, 文献, 被使用于 and 解除途径 fields (§2.2), in agreement with the register. §2.2 states that it is not a premise of `thm:appO-main` or `thm:dy-factorization`, which keep `asm:appO-mixing`(c) with \tagA, and that replacing mixing(c) by it with \tagP would lower `thm:dy-factorization` to [P] by grade propagation (WRITER_SPEC_v2 §4.6).
* **(c)** "Unconditionally" is dropped from the T1 bullet. T1 is R_cond, and its integrated form needs `asm:appO-envelope`.

### Fix 7 — Accuracy and disclosure

* **(a)** T2(a) now states that the constants are polynomials also in $\ln(a_{\max}/a_{\min})$ (through $C'_{IX}$ and $R_{\rm out}$), and that $C_E$, $C_T$, $C_I$ depend on $\bar n_A$ and $(\lambda_A/\mu_A)^2$ through $c_\rho$. $\mathcal E_{\rm tot}$ inside $C_{IX}$ (and $C_{X0}$) is replaced by $C_Ec^2/4\le C_E(3+\ell_B^2)$ when forming $C_I$; the supremum in $C_I$ is made explicit (monotonicity lemma, Step 8). The derivation of $c_\rho$ in (A4) is written out (giving the smaller $c_\rho=36(2\bar n_A-1)m^\flat_A\,r\,(\lambda_A/\mu_A)^2$; tests 0.0396 with the old and 0.091 with the new constant). The sentence on the size of (v) is added: with all jet constants 1, $C_N=500.6$ and (v) needs $\varepsilon\lesssim10^{-11}$, or $\varepsilon\lesssim6\times10^{-9}$ using the explicit $\delta_Y$.
* **(b)** T2 numerics: decay exponents 0.63, 0.70, 0.73 and first-decade Im slopes 0.680–0.717 (LA-5; `final2_logs/t2_numerics_refit.log`). The values 0.7–0.77 and 0.717–0.730 are removed.
* **(c)** L1 verification: $\sum_\sigma|w_\sigma|=89.0$; the quoted 44.7 is $\max_\sigma|w_\sigma|$, which enters the per-sector bound 160.
* **(d)** §10: "DGOPS step 3" and "DGOPS step 6" are stated to refer to DGOPS's own six-step list at the beginning of their §4 (arXiv v1, pp. 38–41; step 3 on p. 39, step 6 on p. 40), not to items 1–4 of our summary. Verified and logged in `final2_logs/lit_checks_final2.log`.
* **(e)** §14.4 item 7 discloses that `final_scripts/t2_constants.py` part (2) re-tabulates logged values. The INSPIRE check of Barcaro et al. (record 3181016; DESY-26-091, SLAC-PUB-260713; texkey `Barcaro:2026dsd`, already in `refs_merged_v2.bib`) is stored in `final2_logs/lit_checks_final2.log`.

### Lead-author decisions applied

* **LA-2:** grades (Fix 3); first sentences naming the model; complete model-internal proofs; pure-mathematics lemmas untagged; the three register entries treated as confirmed.
* **LA-5:** only the refit exponents and first-decade slopes are printed.
* **LA-7:** all locations verified; no unverified-location marker remains.
* **LA-12:** A.4 lists the spec entries to update in CHANGELOG v2.4.
* **LA-14:** the only reference whose record was re-checked (Barcaro et al.) is already in the bibliography under its INSPIRE texkey.

---

## Items needing independent confirmation

Every proof that is new or changed in this revision:

1. **P5 (ii), (iii)** (§9): the amplitudes with exchange propagators; the identity $k\cdot(A_A+A_B)=C(v_A\cdot v_B)(1/q_2^2-1/q_1^2)$; the form, sign and normalization of the three-gluon term $A_3$ relative to $A_A$, $A_B$ (current conservation exactly, gauge independence of $|J|^2$); the eikonal suppression of the colour-symmetric part; the positivity of the Feynman-gauge interference; the comparison with $|A_A+A_B|^2_{\rm Feyn}$ and the self-term ratio. Check: `p5_lipatov_check.py`.
2. **T2(a)** (§7): the (A4) derivation and the new $c_\rho$; the monotonicity lemma and the explicit $C_I$; the bound $|{\rm Re}\,X_w|\le\mathcal E_{\rm tot}$ and its identification (D6 normalization) with the $C_AX$ coefficient of the uncut side sum; the statement that the $X^2$ coefficient is not addressed (OPEN-14).
3. **T2′(a)** (§7, complete new proof): Step 6$^\chi$ (the ray identity for the regulator alone; no use of $\mathcal N_A$ or of (REAL) for $J_A$); Step 3$^\chi$ (bounds on $Q_1$, $Q_2$ and the two geometric integrals); Step 4$^\chi$ (the term $P'_5$ and the role of the class $\mathfrak X_1$); Step 7$^\chi$ (normalization $\delta^\chi_Y$ and $C^\chi_X$); the collected constants. Numerical support: `t2p_general_regulated.log`.
4. **T2′(b):** the general end-pole value $\Pi$ (without (REAL) for $J_A$), the error bound with the constants of T2, and the applicability of L6 with axis poles (bounds near 0 and at infinity in the closed quadrant).
5. **T3(b)** (§8): the decomposition $X_b=\frac12-V+\Delta X$, the explicit bounds on $|\Delta X|$, $\delta_b$, $|V|$, $|E_b|$, and the hypotheses $\varepsilon\le r^{-1/2}/8$, $\delta_b\le\frac12$.
6. **Lemma V** (§8): the closed forms of $v_{IF}$, $v_{II}$ from the nine pole pairs; the reduction $D=S=sw-ip$; the identity $A^2-|N|^2=\sum G_i$ and the non-negativity of each $G_i$ for $p\le s^2/4$; the cubic remainder bound.
7. **T3(e)** (§8, complete new proof): (2b), the global bound $|h^{\rm reg}_\pi|\le4c_U^2m^\flat_{A,\pi/4}$ on the $\pi/4$ contour for energies of either sign; the decomposition (5) with $V_K$ restricted to $R\le R_A$; the bounds (6); the constants and $\delta_N(K)$; the weakened condition $a_{\min}/(2K)\ge4\lambda_B$.
8. **P4(a), (b)** (§7): the decomposition $W(12,21)=W^{\rm in}_D+W^{\rm out}+R_{P4}$ with $W^{\rm in}_D$ depending on $J_A$ only through $\lambda_A$; the halving of the T2 error bounds for one strip; the shift formula with $\delta R$ and the $\varepsilon$-threshold argument.
9. **L8(h), (i)** (§4): the $\pi/4$ norms, the argument that every estimate is multiplied by at most $2^3$, and the integrated bounds (i1)–(i4) (including (i1) for all $X>0$).
10. **D8, class $\mathfrak X_1$:** a change of `def:appO-regulator-class` that the lead author must accept (CHANGELOG v2.4); the example's membership.
11. **L1′:** the closed form of $c_U(t)$ and the analytic bound $(3+\sqrt2)/2$.
12. **ERR-S1b** (§12), **T2 relation to the reference**, **§13** and **§2.2**: the reworded statements (Fix 2, Fix 6) and the new status lines.
13. **Grades** (Fix 3; §0.2, §18, A.2, A.4): consistency with LA-2 and FINAL_OUTLINE_v2 §00.4.


