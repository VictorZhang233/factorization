# W03-write

(structured result persisted from wf_1b1b7a35-b6e)

## summary

I finished W03's three units, picking up from the drafts the previous session left when it hit the quota limit. Ch3 (ch03_prelim.tex), App A (appA_lightfront.tex) and App I (appI_gamma5.tex) contain every canonical statement, figure and table from the outline. All three compile cleanly (0 errors, nothing overfull above 1 pt, 0 undefined citations) and pass all check_unit_v2.py checks (C1–C8).

**Over budget:** Ch3 is 19 pp against 12 (+58% by page count; LA-8 allows up to +20%) and App A is 4 pp against 3 (+33%); App I is about 2.3 pp against 2. Every page holds outline content: complete proofs of the [R] statements, step-by-step derivations, the 6 worked examples, 3 required figures and the symbol table. The page budget is your call.

**Physics checks:** I re-ran the earlier scripts s1–s7 and the new s8. Two checks in s5 failed because of numerical-integration error (the formulas themselves were fine); after fixing the integration all 134 checks pass. I also re-derived the key signs and factors by hand: the optical theorem, the vacuum polarization, the Wilson-line rules and the ABJ anomaly sign (∂J5 = −n_f(α_s/4π)G·G̃ with ε^{0123}=+1), and the anomaly sign also matches an independent E∥B argument.

**Edits this session:**
- Converted all ASCII quotation marks in the Chinese prose to proper Chinese quotes.
- Made several statements more precise:
  - reversed path ordering, stated as the Wilson line of Collins' convention;
  - the exact two-gluon web term;
  - the condition under which the eikonal approximation fails in the Glauber region;
  - the rapidity-divergence sentence;
  - the reason for the D−2 gluon polarization average, in the DIS and Drell–Yan normalizations;
  - ρ_V and ρ_R are now defined;
  - Q is now defined in the unitarity sketch;
  - the right App C section pointers;
  - App O tags added to the box.
- Added the classical references to the moment-problem remark.
- Moved the fig:soft-eikonal block (unchanged) before Example 1.8; this removes a near-empty page.
- In App I, added a note from Mertig–van Neerven §3 (checked in the arXiv full text). The first moment of their finite renormalization gives −4C_F, the same coefficient as Larin's Z5. That gives the quoted (not yet verified) Z5 value a second check besides my one-loop derivation.
- Re-verified on INSPIRE the 3 new references in the App I .bib-additions file.
- Verified every printed literature location, including Collins 1984 §4.1, §13.2, §13.6 from the Cambridge contents scan and Peskin–Schroeder §7.3.

**Spec problem found:** the caption of fig:prelim-wilson-rules prints "（VF-WL-1）", an internal formula ID. Under LA-10 I copied the block verbatim and did not edit it; the ID should be deleted in figures/figset_A.tex.

## files

1. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/chapters/ch03_prelim.tex
2. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/chapters/appA_lightfront.tex
3. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/chapters/appI_gamma5.tex
4. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/chapters/appI_gamma5.bib-additions
5. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W03/parts/
6. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W03/build.sh
7. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W03/s1_lightfront_boost.py
8. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W03/s2_wilson_lines.py
9. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W03/s3_eikonal_limit.py
10. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W03/s4_dimreg.py
11. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W03/s5_distributions.py
12. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W03/s6_gamma5.py
13. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W03/s7_misc.py
14. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W03/s8_resume_checks.py
15. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W03/logs/
16. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W03/edit2/
17. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/test/W03/test_prelim.pdf
18. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/test/W03/test_appA.pdf
19. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/test/W03/test_appI.pdf
20. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/test/W03/chk_Ch03.txt
21. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/test/W03/chk_AppA.txt
22. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/test/W03/chk_AppI.txt

## pages

Ch3: 19 pp in the standalone build (pp. 1–18 full, p. 19 holds only the tab:prelim-symbols float; bibliography from p. 20). Budget 12 pp, so +58% by page count (+53% by text); LA-8 allows +20%. App A: 4.0 pp, budget 3 (+33%). App I: about 2.3 pp, budget 2 (+12%, within tolerance).

## compile_status

Built with xelatex, bibtex, xelatex, xelatex in writing/test/W03 (drivers test_prelim.tex, test_appA.tex and test_appI.tex, the last two with \appendix; bibliography refs_W03.bib = refs_merged_v2.bib plus appI_gamma5.bib-additions). All three units:
- 0 LaTeX errors or undefined control sequences;
- no overfull box above 1 pt (largest 0.24 pt in Ch3 eq. 1.17 and 0.68 pt in an App A paragraph);
- 0 undefined citations, 0 multiply defined labels, 0 missing characters, 0 BibTeX warnings.
Undefined references are only canonical labels owned by other units, listed in report item 4. Every page was rendered at 110 dpi and inspected: figures, both boxes, the table and all long displays.

## checker_output

check_unit_v2.py, final run:
- Ch03 (ch03_prelim.tex): C1 OK, C1b OK, C2 OK, C3 OK, C4 OK, C5 OK, C6 OK, C7 OK, C8a OK, C8b OK. 57 external references, all canonical: asm:appN-cutsum, asm:intro-wightman, cor:appK-pdf, cor:dis-weak-xspace, def:ir-glauber, def:ir-scalings, def:method-collinear-approx, def:method-soft-approx, def:pdf-quark, def:prelim-feynman-rules, def:prelim-msbar, def:prelim-qcd, def:qcd-dimreg, def:sudakov-cusp, def:tmd-unsub, ex:qcd-qqbar-gg, lem:appA-mellin-table, lem:appB-shuffle, lem:appC-bubble, lem:appK-hausdorff, lem:appO-cut-position, lem:appO-unitarity, lem:method-soft-unitarity, lem:method-ward-multi, prop:appB-rules, prop:appB-webs, prop:appJ-ghost-cuts, prop:appK-continuation, prop:dis-dispersion, prop:disall-nlo, prop:dy-nlo, prop:ee-cutting-exact, prop:ir-power-counting, prop:method-fsi, prop:pdf-lo-kernels, prop:pdf-partonic-dr, prop:qcd-brst-cohomology, prop:qcd-covariance, prop:sudakov-oneloop, prop:thr-oneloop, rem:appK-counterexamples, rem:dis-nonuniform, rem:pdf-ns-plusminus, sec:appA-dirac, sec:appA-lightfront, sec:appA-mellin, sec:appA-plus, sec:appC-msbar, sec:appC-phase-space, sec:qcd-quantization, thm:appK-carlson, thm:appK-even-moments, thm:appK-muntz, thm:coll-g1-moments, thm:dis-bjorken, thm:ee-R-finite, thm:prelim-slavnov-taylor.
- AppA (appA_lightfront.tex): C1–C8b all OK. External references: cor:dis-weak-xspace, def:prelim-mellin, def:prelim-plus, lem:prelim-boost, lem:prelim-mellin, lem:prelim-plus-expansion, rem:appK-counterexamples, sec:prelim-distributions, sec:prelim-lightfront.
- AppI (appI_gamma5.tex): C1–C8b all OK. External references: def:prelim-gamma5, def:prelim-msbar, prop:coll-anomaly-scheme, thm:coll-g1-moments, thm:dis-bjorken, thm:prelim-composite-renorm.

Verification scripts, final run (logs in writing/work/W03/logs/): s1 23/23, s2 40/40, s3 7/7, s4 15/15, s5 22/22, s6 13/13, s7 6/6, s8 8/8, so 134/134 PASS. The two s5 P4 checks had failed through quadrature error (endpoint singularity; truncated tail integral) and pass after the integration was fixed; the formulas were not changed.

## report_markdown

# W03 report — Ch3 `prelim`, App A `appA`, App I `appI` (WRITER_SPEC_v2 §13)

**Context.** The previous session drafted all three units and stopped when it hit the quota limit. This session re-read all the binding inputs (LEAD_DECISIONS, the whole of WRITER_SPEC_v2, PACK W03, FINAL_OUTLINE_v2 §0, CONTEXT, REQUIREMENTS) and checked the drafts against them. There is no SPEC_V24_DELTA file, and FINAL_OUTLINE_v2 is unchanged since 2026-10-11 (v2.3.1).

What this session did:
- Re-ran every verification script and fixed two numerically fragile checks.
- Added a new script, s8 (8 checks).
- Corrected and sharpened the text in about ten places (listed in items 8 and 13).
- Rebuilt the three units, rendered every page and inspected it, and re-ran the unit checker.

## 1. Files, pages, compile status
- `chapters/ch03_prelim.tex` (84 KB). Generated from `writing/work/W03/parts/ch03_p1…p6.tex` by `writing/work/W03/build.sh`.
  - **19 pp**: pp. 1–18 full; p. 19 holds only the float `tab:prelim-symbols`.
  - Budget 12 pp, so +58% by page count (+53% by text). LA-8 allows +20%.
- `chapters/appA_lightfront.tex`: **4.0 pp**, budget 3 (+33%).
- `chapters/appI_gamma5.tex`: **≈2.3 pp**, budget 2 (+12%, within tolerance).
- `chapters/appI_gamma5.bib-additions`: three new references (item 10).
- Compile status (xelatex, bibtex, xelatex ×2):
  - 0 errors;
  - no overfull box above 1 pt (largest 0.24 pt and 0.68 pt);
  - 0 undefined citations, 0 multiply defined labels, 0 missing characters, 0 BibTeX warnings.
- Undefined references are only the canonical labels of other units (item 4).
- Every page was rendered at 110 dpi and inspected: figures, the §6.6 box, the misconception box, the table and all long displays.
- **Justification of the length.**
  - The Ch3 outline puts 25 canonical statements, 6 worked examples, 3 required figures, the symbol table and two boxes into 12 pp.
  - Every [R] statement whose outline plan says "full" has a complete proof. Derivations are printed step by step (LA-15). No padding was found in a dedicated review pass.
  - The overrun matches the other Part I drafts (Ch4 ≈ +65%, Ch5 ≈ +50%, Ch6 ≈ +55%).
  - LA-8 forbids shortening statements, proofs of [R] statements, `\uses` lists, status paragraphs and boxes. The only removable pieces are short side remarks, worth ≈0.2 pp.
  - **The lead author decides.**

## 2. Canonical labels
All implemented, and in the outline's reading order.
- **Ch3** (25 statements, 6 sections, 1 table, 3 figures):
  - Statements: def:prelim-lightfront, lem:prelim-boost, ex:prelim-boost-scaling, def:prelim-wilson, prop:prelim-wilson-covariance, prop:prelim-wilson-rules, lem:prelim-eikonal-identity, ex:prelim-eikonal-two, ex:prelim-wilson-segment, def:prelim-dr-conventions, lem:prelim-scaleless, ex:prelim-scaleless, def:prelim-gamma5, def:prelim-plus, lem:prelim-plus-expansion, ex:prelim-plus, def:prelim-mellin, lem:prelim-mellin, rem:prelim-moment-tools, def:prelim-cut, thm:prelim-cutting-rules, prop:prelim-unitarity, rem:prelim-cutting-dr, prop:prelim-optical, ex:prelim-vacpol.
  - Sections: sec:prelim-lightfront, -wilson, -dimreg, -distributions, -moments, -cuts.
  - Table: tab:prelim-symbols. Figures: fig:prelim-lightcone, fig:prelim-wilson-rules, fig:soft-eikonal.
  - Chapter label: ch:prelim.
- **App A:** app:appA; lem:appA-fierz, def:appA-test-functions, lem:appA-plus-product, lem:appA-weak-convergence, lem:appA-mellin-table; sec:appA-lightfront, -dirac, -plus, -mellin.
- **App I:** app:appI; def:appI-hvbm, prop:appI-larin, rem:appI-anomaly; sec:appI-hvbm, -larin, -anomaly.
- **check_unit_v2.py, all three units:** C1 OK, C1b OK, C2 OK, C3 OK, C4 OK, C5 OK, C6 OK, C7 OK, C8a OK, C8b OK. Nothing needs justifying.

## 3. Additional labels
Equation labels only. No auxiliary lemmas and no extra examples beyond the outline: all 6 Ch3 examples are canonical, so the minimum of 5 is met.
- **Ch3:** eq:prelim-lc-dot, -nAnB, -sudakov, -boost-spinor, -collinear-scaling, -W, -W-ode, -past, -future, -one-gluon, -eikonal, -eikonal-in, -segment, -scaleless, -scaleless-a2, -sigma, -lT-scaleless, -trace-g5, -larin, -plus, -product, -plus-identities, -ck, -plus-expansion, -ex-plus, -mellin-D, -cutting, -qqgg, -optical-vac, -Pi0.
- **App A:** eq:appA-gpm-proj, -fierz, -Dk-bound, -product.
- **App I:** eq:appI-larin-current, -Z5, -anomaly.

## 4. External labels referenced
All canonical (C3 OK).
- **Ch3:** asm:appN-cutsum, asm:intro-wightman, cor:appK-pdf, cor:dis-weak-xspace, def:ir-glauber, def:ir-scalings, def:method-collinear-approx, def:method-soft-approx, def:pdf-quark, def:prelim-feynman-rules, def:prelim-msbar, def:prelim-qcd, def:qcd-dimreg, def:sudakov-cusp, def:tmd-unsub, ex:qcd-qqbar-gg, lem:appA-mellin-table, lem:appB-shuffle, lem:appC-bubble, lem:appK-hausdorff, lem:appO-cut-position, lem:appO-unitarity, lem:method-soft-unitarity, lem:method-ward-multi, prop:appB-rules, prop:appB-webs, prop:appJ-ghost-cuts, prop:appK-continuation, prop:dis-dispersion, prop:disall-nlo, prop:dy-nlo, prop:ee-cutting-exact, prop:ir-power-counting, prop:method-fsi, prop:pdf-lo-kernels, prop:pdf-partonic-dr, prop:qcd-brst-cohomology, prop:qcd-covariance, prop:sudakov-oneloop, prop:thr-oneloop, rem:appK-counterexamples, rem:dis-nonuniform, rem:pdf-ns-plusminus, sec:appA-dirac, sec:appA-lightfront, sec:appA-mellin, sec:appA-plus, sec:appC-msbar, sec:appC-phase-space, sec:qcd-quantization, thm:appK-carlson, thm:appK-even-moments, thm:appK-muntz, thm:coll-g1-moments, thm:dis-bjorken, thm:ee-R-finite, thm:prelim-slavnov-taylor.
- **App A:** cor:dis-weak-xspace, def:prelim-mellin, def:prelim-plus, lem:prelim-boost, lem:prelim-mellin, lem:prelim-plus-expansion, rem:appK-counterexamples, sec:prelim-distributions, sec:prelim-lightfront.
- **App I:** def:prelim-gamma5, def:prelim-msbar, prop:coll-anomaly-scheme, thm:coll-g1-moments, thm:dis-bjorken, thm:prelim-composite-renorm.

## 5. Tags
Every tag is the outline's; nothing was weakened or strengthened.

| Label | Tag | Proof given |
|---|---|---|
| lem:prelim-boost | [R, R_def] | full; details in App A |
| prop:prelim-wilson-covariance | [R, R_def] | full: ODE uniqueness, gauge law, composition and retracing |
| prop:prelim-wilson-rules | [R, R_def] | key steps (iterated integrals, induction); full proof in App B (prop:appB-rules) |
| thm:prelim-cutting-rules | [R, R_PT] | proof sketch of the largest-time equation, as the outline plans; Veltman 1963, 't Hooft–Veltman 1974, Cutkosky 1960, P&S §7.3 cited; "（本定理只涉及 Feynman 图。）" |
| prop:prelim-unitarity | [R, R_PT] | proof sketch: polarization sum, Slavnov–Taylor tree identity, BRST quartets; App J prop:appJ-ghost-cuts, Kugo–Ojima, 't Hooft–Veltman, CKR; partonic remark |
| rem:prelim-cutting-dr | [A] | — |
| prop:prelim-optical | [R, R_def] | full |

- **rem:prelim-cutting-dr:** the 「地位与缺口」 paragraph gives the O(g²) check exact in ε (VF-EE-8) with ρ_V, ρ_R defined. It names:
  - the weakest step: the per-graph largest-time equation and its analytic continuation for massless IR-divergent graphs with ghosts;
  - asm:appN-cutsum as a pointer only;
  - the error type E-S (`% errtype: E-S`);
  - the upgrade path.
- **prop:prelim-optical:** carries the non-perturbative status line 「非微扰地位：\cref{asm:intro-wightman}（MA0…）」.
- **Untagged (pure mathematics):** lem:prelim-eikonal-identity (two full proofs plus the explicit counterexample for a uniform +iε), lem:prelim-scaleless (full), lem:prelim-plus-expansion (sketch; full in App A), lem:prelim-mellin (proof here and in App A), and all four App A lemmas (full proofs).
- **Definitions and examples:** untagged. rem:prelim-moment-tools and rem:appI-anomaly are untagged remarks.
- **prop:appI-larin:** [R, R_PT]. The proof cites the literature, re-derives the sign of the replacement in our convention, and re-derives the one-loop Z5 coefficient. Partonic and operator remark included.
- Every R-qualifier sentence is verbatim (C6 OK). No grade-propagation conflicts.

## 6. Assumptions
- None defined (none is owned by these units).
- **asm:intro-wightman:** used by prop:prelim-optical, in `\uses` and in the non-perturbative status line. It is the only hadron-level statement in the three units.
- **asm:appN-cutsum:** named as a pointer in the status paragraph of rem:prelim-cutting-dr, outside the environment and not in `\uses`.
- No R_cond statements, so no premise sentences.

## 7. `\uses`
- C5 OK. Every `\cref` to a later chapter or to an appendix outside a `\uses` list sits in running text (forward pointers, as §4.5 item 4 allows).
- **One addition to the outline lists:** prop:prelim-wilson-covariance also lists def:prelim-qcd, because its proof uses the gauge transformation defined there.
- **No forward edges and no cycles.**
- **No hidden forward dependency:** lem:appA-mellin-table depends only on Ch3 definitions, and the App B/C/J/K labels used by Ch3 passed the outline-level check (W2).

## 8. Formulas
**VF IDs used:**
- Ch3: VF-CONV-1, -4, -6, -7, -8, -9, -10, -12, -13, -14, -24; VF-WL-1, -2, -3, -5, -9; VF-EE-3, -8; VF-PDF-5; VF-DY-12; VF-MISC-1, -2, -3.
- App A: VF-CONV-8, -20; VF-DIS-7, -8; VF-DY-12; VF-EXC-13; VF-PDF-7, -8; VF-THR-2.
- App I: VF-CONV-10, -24; VF-POL-1.

**Writer-derived formulas** (scripts in `writing/work/W03/`, logs in `logs/`; 134/134 PASS):

| Formula | Check |
|---|---|
| Boost rules, spinor boost S(η), projectors, ψ̄γ⁺ψ = √2\|P₊ψ\|², SCET dictionary, collinear Fierz identity | s1 |
| Wilson-line rules at finite adiabatic ε (m ≤ 3, all four orientations) and future − past = 2πi δ | s2 R1–R3 |
| Eikonal identity: exact and symbolic; defect of a uniform +iε, −iε/[(a₁+iε)(a₂+iε)(a₁+a₂+iε)], whose pairing with the test function is π²ε/((1+ε)²(2+ε)) | s2 E1–E3 |
| Exact two-gluon web term ½[T₂,T₁](E(1,2) − E(2,1)) | s2 E4 = VF-WL-3 |
| Finite light-like segment W⁽¹⁾[w,0] = g t^a Ã⁺(1 − e^{−ik⁺w⁻})/k⁺: sign in our convention, both limits, decomposition via ±∞ | s2 S1 |
| SU(2)/SU(3) covariance; reversed ordering not covariant; variation formula | s2 C1–C2 |
| Reversed ordering transforms as U(a)…U†(b) in Collins' convention | s8 R1 |
| Eikonal limits with O(λ) errors | s3 |
| Scaleless-integral ε_UV/ε_IR bookkeeping | s4 D1, D3 |
| Massless one-loop Σ_V(p²) exact in ε and its expansion (Feynman-parameter derivation) | s7 Q1 |
| Vacuum polarization (D−dimensional traces, MS-bar constant 5/3; cut = continuation exactly in ε; Φ₂) | s4 D5–D8, s7 Q3 |
| c_k[g] identities and the 7/4 value | s5 P1–P3, A3 |
| Expansion lemma, its radius of convergence, and ⟨𝒟_k,(1−z)^η⟩ = (−1)^k k!/η^{k+1} | s5 P4 |
| B(N−ε,−2ε) to O(ε) | s5 P5, A4 |
| Mellin table; P_ij and C₂ moments (N = 1…8); convolution theorem | s5 M1–M7 |
| Large-N numbers at N = 100 | s7 Q2 |
| Weak-convergence counterexample (sin Q²x, limit 2/π) | s5 A1–A2 |
| Hilbert-matrix condition numbers | s7 H1 |
| γ₅ traces (256 index sets); Larin replacement sign; D-dimensional Clifford identities and the inconsistency of an anticommuting γ₅; HVBM | s6 G1–G6 |
| One-loop Larin Z5 (X_L − X_V = 4ε) | s6 G7 |
| Heavy-quark low-energy theorem normalization; ABJ anomaly sign and normalization in our convention (c = −1) | s6 G8 |
| ABJ sign cross-checked by the E∥B Landau-level argument (εFF = −8 E·B for ε^{0123}=+1) | s8 R2 |
| DIS/DY normalization of the polarization-average shift | s8 R3 |
| DGLAP consistency of the pure-DR partonic PDF | s8 R4 |

**Quoted (T-status) formulas.** VF-POL-1 (Z5^ns coefficient) is writer-verified twice:
- by the one-loop UV-pole computation printed in the proof of prop:appI-larin (s6 G7);
- by the first moment of the finite renormalization z_qq = −8C_F(1−x) in Mertig–van Neerven §3, which gives −4C_F (s8 R5; checked in the arXiv full text). This is printed as a sentence in App I.

I suggest the spec status of VF-POL-1 be changed from T to V.

## 9. Verification items
- **No 「本书新结果」:** none is due in these units.
- **N26:** lem:prelim-eikonal-identity carries the attribution to Echevarria–Scimemi–Vladimirov, eqs. (5)–(6) and the following text. The abelian identity is called classical and no novelty is claimed.
- **Errata:** no candidate errata were found in the literature.
- **Problem in the spec files:** see item 11.

## 10. Citations
**Keys used:**
- Ch3: BrandtNeriSato1981, BreitenlohnerMaison1977a, Carlson1914, Collins1984, Collins2011, CombridgeKripfganzRanft1977, Cutkosky1960, Echevarria:2015byo, FrenkelTaylor1984, Gatheral1983, Hausdorff1923, KorchemskyRadyushkin1987, KugoOjima1979, Larin:1993tq, Muntz1914, PeskinSchroeder1995, Polyakov1980, Szasz1916, Titchmarsh1939, Vanderhaeghen:1999xj, Veltman1963, tHooftVeltman1972, tHooftVeltman1972b, tHooftVeltman1974.
- App I: Adler:1969gk, AltarelliRoss1988, Bell:1969ts, BreitenlohnerMaison1977a, CarlitzCollinsMueller1988, Collins1984, Larin:1993tq, LarinVermaseren1991, MertigVanNeerven1996, Shifman:1978zn, Vogelsang1996, tHooftVeltman1972.
- App A: none (classical mathematics proved in full).

**New references:** Adler:1969gk, Bell:1969ts, Shifman:1978zn are in `appI_gamma5.bib-additions`, with BibTeX taken from INSPIRE and re-checked this session.

**Locations verified (LA-7):**

| Citation | How verified |
|---|---|
| Collins1984 §4.1 "Definition and axioms"; §13.2 "Definition of γ₅"; §13.6 "Non-singlet axial current has no anomaly" | contents pages of the Cambridge 2023 OA reissue (facsimile; ch. 13 on pp. 331–353, as in the 1984 listing) |
| PeskinSchroeder1995 §7.3 (optical theorem and cutting rules) | confirmed by web search |
| Titchmarsh1939 §5.81 | location confirmed in REFS_NOTES |
| Echevarria:2015byo eqs. (5)–(6) | literature check of claim N26 in CLAIM_VERDICTS |
| MertigVanNeerven1996 §3 | arXiv full text |

**Other:**
- No aliases needed; nothing marked 「文献待补」; no preprints cited.
- Abstract-level keys are used only for what their abstracts state: Vogelsang "confirms the results of MvN"; AltarelliRoss, CarlitzCollinsMueller as the outline prescribes.
- The classical moment-problem sources (Hausdorff, Carlson with Titchmarsh §5.81, Müntz, Szász) were added to rem:prelim-moment-tools, following the pack's key list.

## 11. Figures
- All three blocks are copied verbatim (LA-10), identical to `writing/packs/W03/figblocks.tex` and to the current sources:
  - fig:prelim-lightcone and fig:prelim-wilson-rules from `figures/figset_A.tex` (2026-10-10 23:24);
  - fig:soft-eikonal from `research/tikz2/figures2.tex` (2026-10-10 13:00).
- All three are referred to in the text and were inspected at 110 dpi.
- **fig:soft-eikonal:**
  - The text adds the conversion sentence (its n is the quark direction, not n_A or n_B) and a pointer to def:ir-glauber.
  - The unchanged block now sits just before ex:prelim-eikonal-two, so that it floats onto a text page instead of a near-empty float page (saves ≈0.45 pp).
- **Figure issue to fix at the source:** the caption of fig:prelim-wilson-rules prints 「统一规则（VF-WL-1）」, an internal formula ID. Proposed fix: delete 「（VF-WL-1）」 in figures/figset_A.tex.
- No new figures and no placeholders.

## 12. Boxes and tables
- §6.6 box present after the opening paragraphs; App O tags were added to the 「没有证明」 line.
- Misconception box at the end of sec:prelim-cuts:
  - the M24 preview, ε_UV vs ε_IR in scaleless integrals;
  - 「单个割图是幺正的」, with pointers to prop:method-fsi and lem:appO-unitarity.
- 「本章小结」, 「这些工具在后文的用途」 and `tab:prelim-symbols` (caption 「本章记号速查」) are present.
- No correspondence table or status table is required for these units.

## 13. Deviations and errors found in the spec files
**Deviations:**
- Page budget (item 1).
- lem:prelim-plus-expansion assumes Hölder continuity at z = 1, not just "continuous at 1" as the outline words it. Mere continuity is insufficient: App A gives the counterexample 1/ln(e/(1−z)), and the hypothesis matches def:appA-test-functions.
- prop:appI-larin re-derives the one-loop Z5 coefficient, although the outline says "cite, do not claim a re-derivation". WRITER_SPEC §6.4.1 prefers a writer re-derivation for T-status formulas. The literature proof is still cited.
- def:prelim-dr-conventions (c) points to sec:appC-phase-space and sec:appC-msbar (section pointers) instead of `\cref`ing rem:appC-Seps inside the definition.
- prop:prelim-wilson-covariance has the extra `\uses` entry def:prelim-qcd.
- Chapter numbers in parentheses, 「（第~N~章）」, are written as text, following §4.5.4.
- The table sets `\renewcommand{\arraystretch}` inside its float, a local setting.
- fig:soft-eikonal block position (item 11).

**Clarity and precision edits this session:**
- ASCII quotation marks converted to proper Chinese quotes.
- Reversed path ordering stated exactly as Collins' P exp(−ig∫A) along the reversed path.
- Exact two-gluon web formula, with T_j and E(j) defined.
- Validity condition of the eikonal approximation in the Glauber region.
- Rapidity-divergence sentence.
- DIS (2C₂^g, two poles) and DY (one pole) normalizations of the polarization-average shift.
- 「本节末」 corrected to \cref{sec:prelim-cuts}.
- Soft and collinear pole bookkeeping in ex:prelim-plus.
- ρ_V and ρ_R defined.
- Q = k₁ + k₂ defined.
- Mertig–van Neerven note in App I.

**Error in the spec files:** the figure caption (item 11). Nothing else.

## 14. Open items for the lead author
See the open_items field.

## open_items

1. Page budget: Ch3 is 19 pp against 12 (+58%), App A 4 pp against 3 (+33%), App I about 2.3 pp against 2. Only ≈0.2 pp could be cut without shortening the statements, [R] proofs, \uses lists, status paragraphs or boxes that LA-8 protects. Please decide whether to accept the length or cap it (for example by dropping side remarks in sec:prelim-wilson).
2. Figure caption fix at the source: in figures/figset_A.tex, delete 「（VF-WL-1）」 from the caption of fig:prelim-wilson-rules (an internal formula ID printed in the book). Writers may not edit figure blocks under LA-10.
3. Integrator: merge chapters/appI_gamma5.bib-additions (Adler:1969gk, Bell:1969ts, Shifman:1978zn; INSPIRE BibTeX, re-checked 2026-10-14) into the master bibliography.
4. Spec bookkeeping: the Z5^ns coefficient in VF-POL-1 is checked twice (one-loop UV-pole computation, s6 G7; first moment of Mertig–van Neerven's z_qq = −8C_F(1−x) is −4C_F, s8 R5). Its status could move from T to V. prop:appI-larin prints the re-derivation although the outline said 'cite only'.
5. Cross-unit consistency, for the reviewers. Ch2 (W02) must define sec:qcd-quantization, def:qcd-dimreg, prop:qcd-covariance, prop:qcd-brst-cohomology and ex:qcd-qqbar-gg as Ch3 uses them. App B (W05) must deliver lem:appB-shuffle, prop:appB-rules and prop:appB-webs ([A]). App C (W06) must deliver lem:appC-bubble, sec:appC-msbar and sec:appC-phase-space. App K (W09) must deliver the moment-problem results as summarized in rem:prelim-moment-tools.
6. The ABJ anomaly sign in our conventions, ∂J5 = −n_f(α_s/8π)ε^{μνρσ}G^a_{μν}G^a_{ρσ} with ε^{0123}=+1, is fixed in App I and checked two independent ways (s6 G8 Pauli–Villars triangle; s8 R2 E∥B argument). Ch11 prop:coll-anomaly-scheme (W13) should use the same sign.

