# X3-ope-final2

(structured result persisted from wf_3924630b-621)

## summary

I wrote the revised report to `verify/extend_reports/X3-ope_final2.md` (969 lines, about 114 KB). It is self-contained and applies all six required fixes of the final review. It ends with the sections "Final-review fixes" (§13) and "Items needing independent confirmation" (§14).

**The six fixes**
- **Fix 1 — the zero-momentum insertion statement.** It is now Prop. F.5, outline `prop:appM-zero-momentum-insertion`. I read BM I and II and the action-principle paper (CMP 52: 39, 55, 11) in full. BM's ε is the Feynman iε kept finite, i.e. a damping parameter acting like a mass, with page locations cited.
  - Step 2 writes out why BM II's subtraction C + T(1−C) and plain minimal subtraction give the same η→0 limit. In the massless theory Ω_H = ω_H; the extra IR subtractions scale like positive powers of η and vanish uniformly near D = 4; BM's ε-Lemma then makes their insertions vanish too.
  - General covariant gauges are covered through BM II's propagator form (3.15). Step 3 derives the p²<0 form; I replaced a Gram-matrix argument, which can fail with an indefinite metric.
  - I propose [R, R_PT], but per LA-4 the book prints [A] until step 2 is independently confirmed. The weakest step is 2(iv), which relies on BM's own argument rather than a stated theorem.
  - The "settles Rem. C.37" claim is cut back to the DR existence/IR-finiteness part only.
- **Fix 2 — Theorem F status.** SSS 2019 §7 Prop. 6 is now named as the closest prior result. Its positivity hypothesis fails here: some coefficients are 1 − ω. Theorem F adds four things: sign-indefinite terms, convergence for complex |ω| < 1, holomorphy on the cut plane, and the DR identification. Jantzen 2011 is characterised from §3 (p. 17, no general convergence proof) and §7 (the Glauber/Regge limit). O12 is extended, the note that the reviewers' INSPIRE searches missed the expansion-by-regions literature is added, and 本书新结果 stays withheld.
- **Fix 3 — Theorem 5.7.** Step 1 now uses the exact dispersion remainder, giving the bound t_{n0} r_Q^{N'−1}. The old bound 2t_{n0} r_Q^{N−1} is shown to be false for odd N. The conclusion is unchanged, and the constants are now explicit.
- **Fix 4 — Lemma NE(ii).** The Dirac rank is r' ≤ 4, the minimal demand is n+6−r', and the supply is n+1 or n+4. The argument no longer needs chirality.
- **Fix 5.** The Feichtner–Sturmfels copy is added, and copies of every other newly checked text, so §2's claim that all checked texts are in `literature/` is now true.
- **Fix 6 (optional clarity).** All three parts are applied: the renormalized-leg term in (A5), the double induction in Lemma A.3, and the Cor. F.2 wording.

**Regrading and wording**
- Pure-mathematics lemmas (NE, B.1, F.1, F.6, 5.3–5.5) and E4 are now untagged 数学, and Examples F.3–F.4 are untagged, per LA-2. Remark B.1 is renamed Lemma B.1.
- Novelty wording follows the K4 class (「本书给出的推导／证明」). LA-5 does not apply, and there are no model theorems for LA-2's [P] rule.
- Hollands 2008 §4.1.3 was located and read (LA-7), which resolves the old "not verified" marker.

**Checks**
- New scripts: `fix1_homogeneity.py` and `fix6_rg_legs.py`. From the interrupted run: `fix1_bm_illustration.py`, `fix3_tail.py` and `fix4_ne_demand.py`. All pass.
- A full rerun of 16 scripts (the 9 author scripts, the reviewer's 3, and 4 final2 scripts) was byte-identical. `fix6_rg_legs` was added after that run and rerun separately, also identical.

## final_report_markdown

The complete report is the file /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend_reports/X3-ope_final2.md (969 lines, 114017 bytes, sha256 prefix ff031f66bf4cf5fe). This field gives a section-by-section digest; the file is the authoritative full text.

# X3 (final2): OPE in massless QCD; DIS and e⁺e⁻ moments at hadron level (Appendix M)

The report supersedes X3-ope.md, X3-ope-fix1.md, X3-ope-fix2.md and X3-ope_final.md. It applies:
- the six required fixes of X3-ope-finalreview.md;
- LEAD_DECISIONS LA-2 (pure-mathematics lemmas untagged), LA-4 and LA-7;
- the K4 novelty wording 「本书给出的推导／证明」.

LA-5 and LA-2's model-theorem rule have no instance here.

Notation: η is BM's damping parameter (BM write ε) and D is BM's n.

Grades:
- [R, R_PT], [R, R_def], [R, R_cond: X], [A], [C];
- 数学 (no tag) for pure mathematics;
- examples untagged.

Markers: 本书给出的严格证明 only for Theorem F; 本书新结果 withheld.

## 0. Summary
1. Theorem I [A], with parts A1–A5 and B.
2. Theorem F [R, R_PT] per graph, the analytic step of the method of projectors. Closest prior result: SSS 2019 §7 Prop. 6.
3. Prop. F.5: zero-momentum insertions exist in DR at every order. Proposed [R, R_PT]; printed [A] until the LA-4 confirmation. It settles only the DR existence part of reference Rem. C.37.
4. Theorem M [R, R_cond: W, SA (+RG, Grow, Meas)].
5. E1–E6.

Slot outcomes: X3a not delivered; X3b not passed; X3c not delivered; X3d partial (pure YM: Hollands §4.1.3 read, transfer to DR+MS-bar not made); X3e PASS per graph.

## 1. Setup and assumption register
- D1–D11 unchanged.
- In the register, LBC now points to Lemma B.1.
- Earlier names: Lemma B.1 = Remark B.1; Prop. F.5 = Remark F.5.

## 2. Literature ledger
Copies of all checked texts are in literature/. This revision added BM I, the BM action-principle paper, FS, SSS 2019, Jantzen, Nilsson–Passare, BFP and Hollands.

K1: BM I, BM II and the action-principle paper, all read in full.
- BM I (CMP 52, 39): ε-Lemma p. 42; Prop. 1 p. 45; §II.3 pp. 45–47; §III pp. 48–49 (definition of the renormalized amplitude as the ε→0 limit); Thm 1 p. 49, whose proof states that ε acts like a mass term and that ε-proportional counterterms vanish.
- BM II (CMP 52, 55): §1 pp. 55–56; S = C + T(1−C) p. 61; Prop. 1, eq. (3.13); eq. (3.14) p. 62; propagators (3.15)–(3.17); Ω_H = ω_H + 2s_H p. 69; Lemma 3 pp. 67–68; Thm 1 p. 72.
- Action-principle paper (CMP 52, 11): the factor exp[−iΣα_ℓ(m_ℓ² − iε)] on pp. 13/30/36; t_G√ε p. 35; Thm 1 p. 22.
- What BM's ε is: the damping parameter. Covariant-gauge QCD qualifies, including Δ_B = 2 and the double-pole gluon term.

K5: Hollands RMP 20 (2008) 1033, §4.1.3, pp. 75–76 of arXiv v4, located and read.

K8: FS Props 2.3, 2.4, 2.6; BFP Def. 2.1, Thms 2.2, 2.4; Nilsson–Passare Def. 1, Thms 1–2. Bibliography note on FS.

Forward-expansion literature: SSS 2019 (§§2–4 and §7 checked) and Jantzen (§3 p. 17 and §7 checked; regions hard, collinear, Glauber, collinear-plane).

## 3. Part I
- Lemma A.3: proof rewritten as an induction over (order, number of legs). This is Fix 6(b).
- Def. A.2: unchanged.
- Lemma NE (outline `lem:appM-ne`), 数学, part (ii):
  - (β): r' ≤ 4, because μ, ν and at most one q̂ fill the indices outside the symmetric set. Chirality is stated but not used.
  - (γ): generator types (G), (M_r), (G5). The demand is n+10+r'−2r−2(Z_up+Z_low+Z_D), with minimum n+6−r'; (G5) needs at least n+3. The supply is at most n+4 (b = 0) or n+1 (b = 1).
  - Checks: fix4_ne_demand, fr_ne_rank, fr_ne_rank_allr.
- Theorem A: (A5) step 3 now includes renormalized legs, Σ_j γ_ij G_j = −D̂G_i + (Σγ_φ)G_i, checked symbolically by fix6_rg_legs. This is Fix 6(a).
- Cor. A.5, Rem. A.6, Lemma A.7, Theorem B, Theorem I: unchanged.
- Lemma B.1 (outline `lem:appM-lbc-formal`), 数学: 本书给出的推导.

## 4. Part II
- F.0 [R, R_PT].
- F.1 and F.6 are 数学. F.1(a) now notes that the polynomial is completely non-vanishing.
- Theorem F: the status paragraph is rewritten.
  - SSS 2019 §7 Prop. 6 is the closest prior result. The base facet is the only essential facet, but SSS's positivity hypothesis fails because some coefficients are 1 − ω.
  - Theorem F adds (i)–(iv): sign-indefinite terms, convergence for complex |ω| < 1, cut-plane holomorphy, and the DR identification.
  - Jantzen §3 and §7 are characterised; the searches caveat is added.
- F.7: unchanged.
- Cor. F.2 step 4: wording fixed (Fix 6c).
- F.8 and F.3: unchanged.
- Examples F.3–F.4: untagged.
- Prop. F.5:
  - Grade and weakest step 2(iv).
  - Setting, BM definition, claims (a)–(c).
  - Step 1: hypotheses of BM II Thm 1.
  - Step 2: (i) decomposition, (ii) Ω_H = ω_H, (iii) homogeneity lemma, (iv) the insertions vanish.
  - Step 3: little-group decomposition and distributional scaling.
  - "What it settles": restricted as Fix 1(c) requires.

## 5. Part III
- Lemmas 5.3–5.5 are 数学, with App K labels.
- Prop 5.6: 本书给出的证明 of reference C.64.
- Theorem 5.7: steps 1–4 rewritten with N', the exact remainder t_{n0} r_Q^{N'−1}, c_N = 2(1+√2)^{N'−3} and Q_1. The conclusion is unchanged; check fix3_tail.
- Prop 5.8, Thm 5.9, Thm M: unchanged.

## 6. Part IV
E1–E6; E4 is untagged, as an illustration for conj:ee-duality(b).

## 7. Verification scripts
A full rerun of 16 scripts was byte-identical, plus fix6_rg_legs rerun separately. The table lists the five final2 scripts.

## 8–12
- §8 novelty ledger in K4 wording.
- §9 W1–W27 (new: W21–W27).
- §10 C.37 statement and spec patch.
- §11 O10 and O12 updated.
- §12 round-3 dispositions.

## 13. Final-review fixes
A table mapping Fix 1(a), 1(b), 1(c), 2, 3, 4, 5, 6(a), 6(b), 6(c) and LEAD_DECISIONS to the change made.

## 14. Items needing independent confirmation
Nine items:
1. the whole of Prop. F.5;
2. Theorem 5.7;
3. Lemma NE(ii)(β)–(γ);
4. (A5) step 3;
5. the Lemma A.3 proof;
6. Cor. F.2 step 4;
7. the Theorem F status paragraph and F.1(a);
8. the changed literature-ledger entries;
9. the regrading.

## fixes_applied

1. Fix 1(a): K1 now states that BM's ε is the damping parameter (Feynman iε kept finite; it 'acts like a mass term'), not the dimensional regulator. Locations: action-principle paper §II.1 pp. 13/30/36 and p. 35; BM I p. 49; BM II §1 and (3.17). BM notation is fixed in the conventions (η = BM's ε, D = BM's n). Prop. F.5 states analyticity at D = 4 and the η→0 limit in S'(R^4).
2. Fix 1(b): BM I read in full (Thm 1, Prop. 1, §II.3, §III) and the identification written out in Prop. F.5 step 2: (i) BM II Prop. 1 with S1 = C, S2 = T(1−C); (ii) Ω_H = ω_H; (iii) homogeneity lemma, coefficients vanishing uniformly near D = 4 with D = 4 form η^{(Ω−j)/2}P(ln(μ²/η)); (iv) the insertions vanish by BM's ε-Lemma (BM I §III). General ξ covered through BM II (3.15); p²<0 form via the little group. Proposed [R, R_PT], printed [A] until the LA-4 confirmation; weakest step 2(iv) named. Scripts fix1_bm_illustration and fix1_homogeneity.
3. Fix 1(c): 'settles reference Rem. C.37' replaced by the restricted statement: in DR, only the existence/IR-finiteness part for off-shell forward two-point insertions. The forward remainder stays asm:appM-forward (Cor. F.2 [A]) and the BPHZL version is not addressed. Changed in Prop. F.5, §0, §10, W24 and O10.
4. Fix 2: Theorem F status paragraph names SSS 2019 §7 Prop. 6 as the closest prior result and the mechanism of Lemma F.1. It shows why SSS's positivity hypothesis fails (1 − ω coefficients; the base facet is the only essential facet) and lists Theorem F's additions (i)–(iv). Jantzen §3 (p. 17, no general convergence proof) and §7 (Glauber/Regge limit) are characterised. Added the note that the reviewer INSPIRE searches did not cover the expansion-by-regions literature; SSS §7 and Nilsson–Passare added to O12; §2 list updated; 本书新结果 withheld.
5. Fix 3: Theorem 5.7 step 1 replaced by the exact dispersion remainder 4|y|^{N'−1}∫x^{N'−2}F2/(1+x²y²) ≤ t_{n0} r_Q^{N'−1}, with N' the least even integer ≥ N−1. Steps 2–4 rewritten with explicit constants (c_N = 2(1+√2)^{N'−3}, Q_1, exponent bookkeeping). The old bound is recorded as false for odd N (W21); conclusion unchanged; script fix3_tail.
6. Fix 4: Lemma NE(ii)(β): r' ≤ 4 (μ, ν and one q̂ besides the first-row index); chirality (r' odd) stated but not used. (γ): generator types (G), (M_r), (G5); demand formula with minimum n+6−r'; (G5) needs at least n+3; supply n+4 (b=0) or n+1 (b=1). The conclusion is independent of chirality. Checks: fix4_ne_demand and the reviewer's fr_ne_rank and fr_ne_rank_allr, rerun identical.
7. Fix 5: Feichtner–Sturmfels copy added (literature/feichtner_sturmfels_math0411260.txt); Props 2.3, 2.4, 2.6 verified and cited. Copies of all other newly checked texts added (BM I, BM action principle, SSS 2019, Jantzen, Nilsson–Passare, BFP, Hollands 2008), so §2's claim is true.
8. Fix 6(a): (A5) step 3 now includes renormalized legs, Σ_j γ_ij G_j = −D̂G_i + (Σγ_φ)G_i, with the derivation; symbolic check fix6_rg_legs.
9. Fix 6(b): Lemma A.3 proof rewritten as a lexicographic induction over (order, number of legs), with the reason it is needed.
10. Fix 6(c): Cor. F.2 step 4 reworded: GI forward trees are built from p alone; alien trees contracted with d_ab may contain q but vanish.
11. LEAD_DECISIONS LA-2: pure-mathematics lemmas (NE, B.1 formerly Remark B.1, F.1, F.6, 5.3, 5.4, 5.5) and E4 untagged (数学); Examples F.3–F.4 untagged; outline labels attached. LA-4: Prop. F.5 printed [A] pending confirmation. LA-7: Hollands §4.1.3 located and read; K5 marker resolved.
12. Novelty wording per WRITER_SPEC_v2 §6.5 K4: 'new argument', 'new detail', 'new conditional form' and 'under a minimal hypothesis' replaced by 本书给出的推导／证明 or 'no novelty claim' (W25–W27); only Theorem F carries 本书给出的严格证明.

## items_needing_confirmation

1. Prop. F.5 (whole proof; this LA-4 confirmation decides [A] → [R, R_PT]). Step 1: hypothesis check of BM II Thm 1 (field IR degrees incl. Δ_B = 2, general covariant-gauge propagator as form (3.15), insertion vertex internal with IR degree n+2, external vertices). Step 2(i)–(ii): BM II Prop. 1 decomposition and Ω_H = ω_H. Step 2(iii): homogeneity lemma (pure-power structure of c_j, analyticity on |D−4| ≤ r < 1/(2h_G), bound K_j η^{1/4}, form η^{(Ω−j)/2}P_j(ln(μ²/η)) at D = 4). Step 2(iv): BM's ε-Lemma applied to reduced graphs carrying the vertex parts η^k P_j; this is the cited and weakest step (BM I §III, BM II Lemma 3). Step 3: little-group decomposition on {p²<0} ≅ (0,∞)×H and the distributional scaling argument. Also the quoted BM page locations.
2. Theorem 5.7 steps 1–4: exact dispersion remainder, choice of N', Markov constant c_N = 2(1+√2)^{N'−3}, bootstrap with Q_1, exponent bookkeeping (N' ≥ n0+2, N' ≥ n+2, N' ≥ N−1).
3. Lemma NE(ii)(β)–(γ): the r' ≤ 4 argument; the demand formula and its minimum n+6−r'; the (G5) count with Z + Z_D ≤ 1; the supply n+2−3b (+2 for B^-_n); the split of the relation by Dirac rank.
4. Theorem A (A5) step 3: the renormalized-leg identity with Σ_φ γ_φ and the Z_φ^{1/2} amputation factor (checked symbolically by fix6_rg_legs).
5. Lemma A.3: the rewritten proof by induction over (order, number of legs).
6. Corollary F.2 step 4: reworded only; check that the argument is unchanged.
7. Theorem F status paragraph: the literature comparison (SSS 2019 §7 Prop. 6 and its hypotheses, the base-facet-only argument, failure of positivity for 1−ω, additions (i)–(iv), Jantzen §3 p. 17 and §7). Also the new sentence in Lemma F.1(a) that the polynomial is completely non-vanishing (BFP Thm 2.2, Nilsson–Passare Thm 1).
8. Changed literature-ledger entries: K1 (BM I, BM II and the action-principle paper, with page locations), K5 (Hollands §4.1.3, pp. 75–76 of arXiv v4), K8 (FS Props 2.3/2.4/2.6; BFP Def. 2.1, Thms 2.2/2.4; Nilsson–Passare Def. 1, Thms 1–2), forward-expansion list (SSS, Jantzen).
9. Regrading: pure-mathematics lemmas, E4 and the examples untagged; consistency with the FINAL_OUTLINE_v2 labels (lem:appM-ne, lem:appM-lbc-formal, lem:appM-newton, lem:appM-matroid, lem:appM-curved-approach, lem:appM-green, lem:appK-markov, lem:appK-entire; prop:appM-zero-momentum-insertion [A] pending LA-4).

## files

1. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend_reports/X3-ope_final2.md
2. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/final2_scripts/fix1_bm_illustration.py
3. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/final2_scripts/fix1_homogeneity.py
4. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/final2_scripts/fix3_tail.py
5. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/final2_scripts/fix4_ne_demand.py
6. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/final2_scripts/fix6_rg_legs.py
7. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/final2_scripts/rerun_all.sh
8. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/final2_logs/fix1_bm_illustration.log
9. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/final2_logs/fix1_homogeneity.log
10. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/final2_logs/fix3_tail.log
11. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/final2_logs/fix4_ne_demand.log
12. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/final2_logs/fix6_rg_legs.log
13. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/final2_logs/rerun_all.log
14. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/final2_logs/rerun/
15. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/literature/breitenlohner_maison_CMP52_39_1977_I.txt
16. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/literature/breitenlohner_maison_CMP52_55_1977_II.txt
17. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/literature/breitenlohner_maison_CMP52_11_1977_action_principle.txt
18. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/literature/feichtner_sturmfels_math0411260.txt
19. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/literature/semenova_smirnov_smirnov_1809.04325.txt
20. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/literature/jantzen_1111.2589.txt
21. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/literature/nilsson_passare_1010.5060.txt
22. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/literature/berkesch_forsgard_passare_1103.6273.txt
23. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/literature/hollands_RMP20_2008_0705.3340v4.txt

