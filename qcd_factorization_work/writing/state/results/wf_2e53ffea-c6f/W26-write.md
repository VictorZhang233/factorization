# W26-write

(structured result persisted from wf_2e53ffea-c6f)

## summary

I resumed W26 (Ch23 「Yizhuang Liu 的严格因子化研究」) from the draft left by the interrupted session. That draft already contained every canonical statement and 13 verification scripts. I reviewed it completely against LEAD_DECISIONS, WRITER_SPEC_v2, the pack, the claim verdicts and the primary sources (PDFs of nine papers read on rendered pages). Then I fixed what was wrong or unclear, rebuilt it and ran the QA.

The build is clean: 0 errors, no over- or underfull boxes, no undefined citations, BibTeX 0 warnings. check_unit_v2.py passes C1–C4, C6, C7 and C8a. The C5 items are justified as pointers, and the C8b items are the two verified 「据我们所知」 priority statements. The chapter is 32 pp against a 15 pp budget, so it is well over the +20 % (18 pp) limit of LA-8; this is reported as an open item.

Changes made this session:
- **Physics error fixed:** the Sivers sketch had the staple directions paired the wrong way round. The correct pairing is +ẑ = DY = past-pointing and −ẑ = SIDIS = future-pointing.
- **Euclidean HQET normalization:** iṽ·D_E = γ(D_τ − iβD_z); the source prints it without the factor γ.
- **App Q references:** \cref{app:appQ} replaced by 「附录~Q 第~n~条」 (LA-6), which also clears check C3.
- **Internal file removed from the text:** the mention of the LaMET 前沿报告 is gone.
- **Wording:** 「证明」 → 「论证了」 for the [A] threshold theorem; typo 时类 → 类时.
- **Small clarifications:** Γ_cusp^(2) defined; the hyperbolic-angle parametrization and orientation convention stated explicitly; the bent-cusp angle written consistently; the s₀ symbol clash in the decay section removed; the GN quote restored verbatim.
- **Formalism:** missing errtype comments added; verbatim R_PT qualifiers added to the composite [R] items; def:lamet-quasi-tmd added to the \uses of prop:yzliu-sivers.
- **Status table:** split into two floats (internal label tab:yzliu-status-b).

Spec deviations kept because they are correct and verified:
- **θ definition (VF-YZL-4 / notation row 46):** printed with √(v² − i0), because only that form reproduces the two mixed rows of Liu's own Table 1 under his own vector convention.
- **prop:yzliu-lfwf:** printed with +i0 instead of the outline's −i0 (the E02 record, script s07, Liu–Su eq. (4.4)).
- **prop:yzliu-gpd-oneloop:** printed with the forms re-derived from the published kernel. Su et al.'s eq. (7) has the opposite sign of the 1/(2(y−x)) term; this is reported as a candidate erratum and not printed.

Figure issue to fix in the figure sources (I may not edit the blocks under LA-10): all five figure captions print internal VF IDs.

## files

1. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/chapters/ch23_yzliu.tex
2. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/chapters/ch23_yzliu.bib-additions
3. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W26/parts/p00_head.tex
4. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W26/parts/p01_soft.tex
5. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W26/parts/p02_analyticity.tex
6. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W26/parts/p03_rapidity.tex
7. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W26/parts/p04_time.tex
8. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W26/parts/p05_qtmd.tex
9. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W26/parts/p06_exclusive.tex
10. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W26/parts/p07_threshold.tex
11. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W26/parts/p08_renormalon.tex
12. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W26/parts/p09_gpd.tex
13. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W26/parts/p10_models.tex
14. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W26/parts/p11_decay.tex
15. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W26/parts/p12_status.tex
16. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W26/assemble.py
17. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W26/build.sh
18. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W26/scripts/s14_gpd_recheck.py
19. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W26/logs/s14_gpd_recheck.log
20. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W26/logs/s15_source_checks.log
21. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W26/scripts/s01_soft_oneloop.py
22. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W26/scripts/s02_theta_table.py
23. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W26/scripts/s09_gpd_oneloop.py
24. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/test/W26/test_yzliu.tex
25. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/test/W26/test_yzliu.pdf
26. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/test/W26/test_yzliu.log
27. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/test/W26/check_output.txt

## pages

32 pp: chapter body is pp. 1–32 of the test PDF (bibliography pp. 33–37, 37 pp in total). Budget 15 pp; the LA-8 upper limit (+20 %) is 18 pp; exceeded by 14 pp (about 2.1× budget).

## compile_status

xelatex + bibtex + xelatex×2 in writing/test/W26 (driver test_yzliu.tex):
- 0 errors (no "LaTeX Error", "Undefined control sequence" or "Emergency stop").
- 0 overfull boxes and 0 underfull boxes; no "Float too large" warning.
- 0 missing characters.
- 0 undefined citations: the two LA-14 additions, Appelquist:1977es and Brambilla:1999qa, are appended to the test copy of refs_merged_v2.bib.
- 0 multiply defined labels.
- BibTeX: 0 warnings.
- 175 "Reference undefined" warnings, all from 51 distinct external labels of other units (expected in a standalone compile); no Ch23 label is undefined.
- Every page rendered at 110 dpi and inspected.

## checker_output

C1 canonical labels of this unit missing: OK
C1b canonical fig/tab labels of this unit missing: OK
C2 labels defined here but owned by another unit: OK
C3 external refs not canonical: OK
   external refs: asm:intro-bridge, asm:intro-composite, asm:intro-wightman, asm:lamet-aux-renorm, asm:lamet-soft-rapidity, asm:lamet-staple, asm:lamet-uniform, def:excl-gpd, def:intro-tags, def:lamet-quasi-gpd, def:lamet-quasi-tmd, def:lamet-reduced-soft, def:lamet-soft-offlc, def:lattice-quasi, def:power-borel, def:prelim-brst, def:prelim-qcd, def:prelim-wilson, def:sudakov-cusp, def:tmd-soft, fig:tmd-staple, lem:lamet-strip, lem:tmd-glauber, lem:tmd-soft-oneloop, prop:appB-cusp-oneloop, prop:appB-webs, prop:front-rapidity-renorm, prop:lamet-lrr, prop:lamet-oneloop, prop:lamet-tmd-ratios, prop:lamet-truncation, prop:lamet-twoloop, prop:lattice-cs-kernel, prop:lattice-renormalizability, prop:power-renormalon-examples, prop:power-thooft-model, prop:prelim-wilson-rules, prop:thr-dis, prop:tmd-evolution, prop:tmd-regions, rem:lamet-domain, rem:lamet-open, rem:tmd-schemes, sec:lamet-intro, thm:lamet-exp-decay, thm:lamet-hadronic, thm:lamet-quasi-gpd, thm:lamet-quasi-tmd, thm:lattice-lamet, thm:tmd-factorization, thm:tmd-sivers-sign
C4 \uses problems: OK
C5 cref/uses mismatches: cor:yzliu-soft-form-factor: asm:intro-wightman | prop:yzliu-sI-twoloop: thm:yzliu-intrinsic-soft | conj:yzliu-complex-wilson: asm:intro-wightman | prop:yzliu-lfwf: asm:intro-bridge, asm:intro-composite | prop:yzliu-meson-ff: asm:intro-bridge, asm:intro-composite | prop:yzliu-dy-quasi: asm:intro-bridge, asm:intro-composite | prop:yzliu-sivers: asm:intro-bridge, asm:intro-composite | prop:yzliu-ad-algebra: prop:yzliu-sI-twoloop | conj:yzliu-threshold-hadronic: asm:intro-composite, asm:intro-wightman | conj:yzliu-gpd-xi: asm:intro-bridge, asm:intro-composite   [all justified as pointers, see report item 7]
C6 tag/qualifier problems: OK
C7 statements without \uses or "% uses: none": OK
C8a planning markers: OK
C8b phrases to justify: 2 × 「首次」 — the two verified A03 priority statements (Ji:2019sxk; Liu:2023pjb), each introduced by 「据我们所知（INSPIRE 检索，2026 年 10 月）」 as WRITER_SPEC_v2 §6.5 item 3 allows.

## report_markdown

# W26 report — Ch23 `ch23_yzliu.tex` (WRITER_SPEC_v2 §13)

This session resumed the W26 draft left by the interrupted run, which already contained every canonical statement and scripts s01–s13. I re-read the whole draft against the binding files and the primary sources, fixed the problems listed below, rebuilt it and ran the QA.

## 1. File
- **Unit:** `chapters/ch23_yzliu.tex` (157 kB). It is assembled by `writing/work/W26/assemble.py` from `writing/work/W26/parts/p00–p12`, and the figure blocks are inserted verbatim.
- **Bibliography additions:** `chapters/ch23_yzliu.bib-additions`, 2 entries.
- **Page count: 32 pp** (pp. 1–32; the bibliography starts on p. 33). The budget is 15 pp, and the LA-8 limit of +20 % is 18 pp, so the chapter is **over by 14 pp** (see item 14).
- **Compile:**
  - 0 errors, 0 overfull boxes (none of any size), 0 underfull boxes, 0 float warnings.
  - 0 missing characters, 0 undefined citations, 0 multiply defined labels; BibTeX 0 warnings.
  - The 51 distinct undefined references are all external labels.
  - All 32 chapter pages were rendered at 110 dpi and inspected.

## 2. Canonical labels
- **Labels:** every label of the Ch23 registry block is implemented — 51 statements including 3 assumptions, 4 examples and 4 remarks; 13 `sec:` labels; 4 tables; 5 required figures — plus `ch:yzliu`.
- **Optional figures** `fig:yzliu-borel` and `fig:yzliu-single-line` were not drawn; LA-10 says to omit them.
- **check_unit_v2.py:** C1, C1b, C2, C3, C4, C6, C7 and C8a are OK. C5 items are justified in item 7. C8b flags only the two verified 「首次」 priority statements (A03), each with 「据我们所知（INSPIRE 检索，2026 年 10 月）」.
- **C3 fix:** the earlier C3 failure (`app:appQ`) was removed by printing 「附录~Q 第~n~条」 as plain text, as LA-6 prescribes.

## 3. Additional labels
- `tab:yzliu-status-b`: continuation of the status table, which is now split into two floats.
- 37 equation labels `eq:yzliu-*`.
- No auxiliary lemmas and no extra examples.

## 4. External labels referenced (all canonical)
asm:intro-bridge, asm:intro-composite, asm:intro-wightman, asm:lamet-aux-renorm, asm:lamet-soft-rapidity, asm:lamet-staple, asm:lamet-uniform, def:excl-gpd, def:intro-tags, def:lamet-quasi-gpd, def:lamet-quasi-tmd, def:lamet-reduced-soft, def:lamet-soft-offlc, def:lattice-quasi, def:power-borel, def:prelim-brst, def:prelim-qcd, def:prelim-wilson, def:sudakov-cusp, def:tmd-soft, fig:tmd-staple (in the leading-region caption), lem:lamet-strip, lem:tmd-glauber, lem:tmd-soft-oneloop, prop:appB-cusp-oneloop, prop:appB-webs, prop:front-rapidity-renorm (text pointer only), prop:lamet-lrr, prop:lamet-oneloop, prop:lamet-tmd-ratios, prop:lamet-truncation, prop:lamet-twoloop, prop:lattice-cs-kernel, prop:lattice-renormalizability, prop:power-renormalon-examples, prop:power-thooft-model, prop:prelim-wilson-rules, prop:thr-dis, prop:tmd-evolution, prop:tmd-regions, rem:lamet-domain, rem:lamet-open (item 13 cited), rem:tmd-schemes, sec:lamet-intro, thm:lamet-exp-decay, thm:lamet-hadronic, thm:lamet-quasi-gpd, thm:lamet-quasi-tmd (item (b) cited), thm:lattice-lamet, thm:tmd-factorization, thm:tmd-sivers-sign.

I checked that the cited items exist in the Ch22 file or the outline: lem:tmd-soft-oneloop(b), thm:lamet-quasi-tmd(b), prop:lamet-oneloop(e), rem:lamet-open (13).

## 5. Tags (all as in the outline; nothing weakened or strengthened)

| Section | Statements and tags |
|---|---|
| §23.2 | lem:yzliu-partial-exp [A]; prop:yzliu-pinch-ultrasoft [A]; asm:yzliu-heavy-pair [C]; thm:yzliu-soft-hqet [A]; ex:yzliu-soft-oneloop (no tag); cor:yzliu-soft-form-factor [R, R_cond], content grade [C] |
| §23.3 | def:yzliu-hyperbolic-angle; asm:yzliu-wightman-pt [A]; thm:yzliu-analyticity [A] |
| §23.4 | prop:yzliu-rapidity-linear [A]; def:yzliu-intrinsic-soft-lc; thm:yzliu-intrinsic-soft [A]; prop:yzliu-sI-twoloop [R, R_PT], two loops; ex:yzliu-sI-rge; asm:yzliu-lightcone-uniform [P]; prop:yzliu-universality-classes [P] |
| §23.5 | def:yzliu-exp-soft; lem:yzliu-matrix-tree and lem:yzliu-final-state (数学, untagged, full proofs); thm:yzliu-time-ordering [A]; prop:yzliu-dy-sidis-exp [P]; conj:yzliu-complex-wilson [C] |
| §23.6 | prop:yzliu-qtmd-powercount [A]; prop:yzliu-hard-kernel [A], items (b) one loop and (c) two loops [R, R_PT]; ex:yzliu-hl-decomposition |
| §23.7 | prop:yzliu-lfwf, prop:yzliu-meson-ff, prop:yzliu-dy-quasi, prop:yzliu-sivers — all [A] |
| §23.8 | def:yzliu-hl-jet; thm:yzliu-jet-continuation [A]; thm:yzliu-threshold [A]; ex:yzliu-threshold-oneloop; prop:yzliu-ad-algebra [A], two-loop item [R, R_PT]; prop:yzliu-threshold-nnlo [P]; rem:yzliu-threshold-domain |
| §23.9 | prop:yzliu-linear-renormalon [P]; conj:yzliu-renormalon-norm [C]; conj:yzliu-threshold-hadronic [C] |
| §23.10 | prop:yzliu-gpd-oneloop [R, R_PT], one loop; conj:yzliu-gpd-xi [C] |
| §23.11 | thm:yzliu-gn-convergence, prop:yzliu-gn-structure, prop:yzliu-on-factorial, prop:yzliu-nlsm, prop:yzliu-2dqcd — all [P], with the model named in the first sentence; rem:yzliu-transforms; rem:yzliu-instantons |
| §23.12 | prop:yzliu-decay-extensions [P] |
| §23.13 | rem:yzliu-relation-css; rem:yzliu-open |

- **MD14:** prop:yzliu-gpd-oneloop keeps [R, R_PT] because the mandatory re-derivation was done. It is re-derived from the published one-loop kernel of Liu:2019urm, eqs. (40)–(46), whose transcription I checked on the rendered page. Scripts: s09, plus the independent s14.
- **Qualifiers in composite items:** the composite [R] items now carry the verbatim R_PT qualifier sentence, as Ch22 does.
- **Grade propagation:** no conflicts.
  - Every [R, R_PT] statement uses only definitions and [R] statements (def:yzliu-intrinsic-soft-lc, def:sudakov-cusp, prop:appB-cusp-oneloop; def:lamet-quasi-gpd, def:excl-gpd).
  - thm:yzliu-soft-hqet [A] uses asm:lamet-aux-renorm [A]; thm:yzliu-analyticity, thm:yzliu-time-ordering and thm:yzliu-jet-continuation [A] use asm:yzliu-wightman-pt [A].
  - prop:yzliu-universality-classes [P] uses asm:yzliu-lightcone-uniform [P]; cor:yzliu-soft-form-factor has content grade [C] through asm:yzliu-heavy-pair.

## 6. Assumptions
- **Defined (owner):**
  - asm:yzliu-heavy-pair [C], items (HP1)–(HP3).
  - asm:yzliu-wightman-pt [A], items (WP1)(WP2).
  - asm:yzliu-lightcone-uniform [P], item (UL).
  - Each has all fields: statement, 地位, 文献, 被使用于 (copied from the register), 解除途径, and \uses.
- **Used from other units:** asm:lamet-aux-renorm (thm:yzliu-soft-hqet), asm:lamet-staple (prop:yzliu-qtmd-powercount, (ST1)/(ST2) cited) and asm:lamet-soft-rapidity (pointer: prop:yzliu-rapidity-linear is its all-order argument).
- **R_cond premise sentence:** cor:yzliu-soft-form-factor: 「前提：\cref{asm:yzliu-heavy-pair}（及 \cref{thm:yzliu-soft-hqet}）。」, with a full proof.
- **Non-perturbative status lines:**
  - From the outline: cor:yzliu-soft-form-factor (asm:intro-wightman, MA0).
  - Added under §4.4 item 6:
    - prop:yzliu-lfwf, prop:yzliu-meson-ff, prop:yzliu-dy-quasi, prop:yzliu-sivers and conj:yzliu-gpd-xi: asm:intro-bridge, asm:intro-composite (MA0, MA1, MA2).
    - conj:yzliu-complex-wilson: asm:intro-wightman (MA0), plus its extension to Wilson loops.
    - conj:yzliu-threshold-hadronic: asm:intro-wightman, asm:intro-composite (MA0).
  - All other statements carry the partonic, vacuum-correlator or model remark.

## 7. `\uses`
**C5 items, all justified as pointers:**
- **Global non-perturbative assumptions** (asm:intro-*), named only in status lines (§4.4 items 6–7; not proof steps; same practice as Ch22). This covers cor:yzliu-soft-form-factor, conj:yzliu-complex-wilson, prop:yzliu-lfwf, prop:yzliu-meson-ff, prop:yzliu-dy-quasi, prop:yzliu-sivers, conj:yzliu-threshold-hadronic and conj:yzliu-gpd-xi.
- **prop:yzliu-sI-twoloop → thm:yzliu-intrinsic-soft:** the outline calls this "a pointer here". The two-loop proof uses only the explicit two-loop angle-dependent cusp anomalous dimension.
- **prop:yzliu-ad-algebra → prop:yzliu-sI-twoloop:** an independent cross-check (the outline says "independently").

**Other points:**
- **Added to `\uses`:** def:lamet-quasi-tmd in prop:yzliu-sivers. The sketch uses its staple-orientation convention; it is a definition from an earlier chapter, so it has no effect on the grade.
- **Dependency structure:** no forward edges and no cycles (C4 OK). Ch24 is pointed to in running text only.
- **Error types:** `% errtype: E-S` is present on prop:yzliu-pinch-ultrasoft, prop:yzliu-rapidity-linear, prop:yzliu-qtmd-powercount and prop:yzliu-lfwf.

## 8. Formulas
**VF IDs used:** VF-YZL-1…14, 16, 17; VF-LAM-0, 14, 15 (via VF-YZL-5), 16 (reference), 18 (text only); VF-TMD-8.

**Writer-checked items and their scripts** (`writing/work/W26/scripts`, logs in `writing/work/W26/logs`):
- s01: one-loop soft function, S_r and the σ = 0 trap.
- s02: θ table re-derived from the one-loop single-T exchange; closed form and complex Lorentz map.
- s03: γ_HH^(2) and the bent-cusp mismatch 0.190 C_F C_A (VF-YZL-17).
- s04: L_b² coefficient of ln S_I.
- s05: H^(1), H = C⁺C⁻, phases, factor ½.
- s06: γ̃_H^(2), log structure of ln H^(2), c_H, the anomalous-dimension algebra, DGLAP consistency.
- s07: LFWF +i0.
- s08: one-loop threshold check to |λ| = 10⁵, including the phase sign.
- s09 and s14: quasi-GPD structure.
- s10: linear-renormalon residue and N_m = 0.977.
- s11: final-state identity and positivity of P_ee′.
- s12: O(N) factorial asymptotics and the power-counting leading region.
- s13: jet-function poles and the two-loop cusp function B(θ).
- s15 log: primary-source checks on rendered PDF pages for every transcribed (TR/A-status) formula.

**TR/A-status formulas and how they were handled:**
- VF-YZL-4: table re-derived at one loop; closed form corrected (item 13).
- VF-YZL-11: residue re-derived from Liu–Su (2.46).
- VF-YZL-12: checked against Liu:2023pjb.
- VF-YZL-14: numerical asymptotic check.
- VF-YZL-16: checked against APPB (151)–(154).
- Ji:2026vir (5.33): checked on the page.
- Ji:2023pba (6.13)–(6.19): checked on the page.
- Liu:2024omb (4.2)–(4.11): checked on the pages.
- Ji:2019sxk (13): factor γ added.
- Ji:2026vir (5.21)–(5.23) contain dimensional slips, so only their verbal content is printed and the threshold is renamed s_th.

## 9. Verification items
- **「本书新结果」:** none printed (none allowed in Ch23).
- **Registered verdicts applied:**
  - E02: ½ in the CS exponent; App Q row 11; journal version of Ji:2021znw cited as correct.
  - E07(ii): bent-cusp mismatch as our evaluation.
  - E08, E09, E11: rows 12, 13, 15.
  - E10: row 14.
  - E13: BHW; Λ(t,z) = (iz,it) only.
  - N06 and N29: verifications, no novelty claimed.
  - A02: name rule.
  - A03: 「据我们所知」 wording.
  - A04: corrected attribution about Collins:2011ca.
  - A07: both positions on x = ±ξ printed side by side.
- **Candidate errata noticed** (not printed as errata; for a later revision):
  - (i) Liu:2022nnk eq. (123) prints √(v² + i0). With Liu's own convention (incoming v₁, outgoing v₂) the two mixed rows of his Table 1 need √(v² − i0). This is not registered.
  - (ii) Su:2026eta (preprint) eq. (7): the 1/(2(y−x)) term has the opposite sign relative to the published kernel. Under the other reading of the variables, the 1/(4ξ) term disagrees instead. Not registered; s14.
  - (iii) Ji:2021znw journal eqs. (49) and (74): −i0 for ψ⁺. This is inside the verified content of E02 but is not an App Q row. The text notes neutrally that +i0 is the consistent prescription (Liu–Su (4.4)).
  - (iv) Ji:2019sxk eq. (13): missing factor γ (trivial normalization).
  - (v) Ji:2026vir (preprint) eqs. (5.21)–(5.23): dimensional slips.
  - (vi) APPB: the sentence near eq. (145) gives Q² = xx′P·P′, while eq. (152) has √(ζ_z ζ′_z) (minor).

## 10. Citations
- **Keys:** 71, all in `refs_merged_v2.bib`, except two new LA-14 additions verified on INSPIRE: Appelquist:1977es and Brambilla:1999qa, in `chapters/ch23_yzliu.bib-additions`.
- **No** aliases were needed, no 「文献待补」 is printed, and no 「位置待核实」 was encountered.
- **Preprints** marked 「（预印本）」 at first citation and in the status paragraphs that rely on them: Su:2026eta, Ji:2026vir, Liu:2021evw, Liu:2026npv.
- **Quotation and location checks:** quotations and locations were verified on the source PDFs (APPB §§3.2, 3.3, 4.5–4.7, 5, 6, App. E; Liu:2023pjb fn. 5 and §4 item 2; Liu:2024omb §§1, 2.4, 4, 6).
- **Unchecked locations:** Ji:2021znw journal equation numbers (49), (51), (74) and footnote 1 are taken from the E02 verification record; only arXiv v1 was accessible.
- **Ji:2024hit:** introduced as 「据该文摘要与引言」.

## 11. Figures
- **Copied blocks:** the five required blocks were copied verbatim from `writing/packs/W26/figblocks.tex`. They are byte-identical to `figures/figset_D.tex` (2026-10-11 00:25; I checked this). All five were rendered, inspected and are referred to in the text.
- **No new figures** were drawn and there are no placeholders.
- **Issues to fix in `figset_D.tex`:**
  - (a) All five captions print internal identifiers. Proposed fix: delete 「（VF-YZL-2）」 (soft-hqet), 「（VF-YZL-4）」 (theta-strip), 「；VF-YZL-12」 (complex-lorentz), 「VF-YZL-8；」 (leading-region), and 「；VF-LAM-14，VF-YZL-9」 (threshold).
  - (b) fig:yzliu-soft-hqet panel (b) prints iṽ·D_E = D_τ − iβD_z. With ṽ = γ(−i,−β,0), the right side is γ(D_τ − iβD_z). Proposed fix: insert γ or write ∝.
- **Otherwise correct:** the theta-strip labels agree with the corrected table, and the complex-lorentz figure shows (iz,it). The theta-strip block contains a local `\def\Yo` inside its tikzpicture.

## 12. Boxes and tables
- **Boxes:** the chapter box 「本章证明了什么／没有证明什么」 (it additionally lists the [R, R_PT] items of prop:yzliu-hard-kernel(b)(c) and prop:yzliu-ad-algebra); the 「Wightman 预备知识」 box; the misconception box with 7 items (C9, C10, M15, M16, and the three outline items).
- **Tables:** tab:yzliu-conventions, tab:yzliu-theta, tab:yzliu-classes, and tab:yzliu-status plus tab:yzliu-status-b, with columns 标签, 瓶颈, 误差类型 and 发表.
- No correspondence table is required for a frontier chapter.

## 13. Deviations and errors in the spec files
**Deviations from the outline or VF:**
- **(a) def:yzliu-hyperbolic-angle:** printed as cosh θ = (v₁·v₂ − i0)/(√(v₁² − i0)√(v₂² − i0)), instead of the √(v² + i0) of VF-YZL-4, WRITER_SPEC row 46 and F0.3 row 14. Reason: under Liu's own convention (incoming v₁, outgoing v₂; APPB §4.5) and the Feynman propagator, the explicit one-loop integral fixes Im θ for the two mixed rows of his Table 1. The printed form interchanges those two rows. I re-derived this by hand and with script s02. The text states the orientation convention (Y → +∞ means opposite light-cone directions) and gives explicit parametrizations.
- **(b) prop:yzliu-lfwf:** printed with +i0 instead of the outline's −i0. This is in E02's verified content, was checked with s07, and is the form in Liu–Su eq. (4.4).
- **(c) prop:yzliu-gpd-oneloop:** the statement prints the structure re-derived from the published kernel, in both the matching form and the inverse-matching form, instead of the transcription of Su:2026eta eq. (7) (see 9(ii)).
- **(d) thm:yzliu-soft-hqet(b):** printed as iṽ·D_E = γ(D_τ − iβD_z).
- **(e)** def:lamet-quasi-tmd added to the `\uses` of prop:yzliu-sivers.
- **(f)** Seven non-perturbative status lines added (item 6).
- **(g)** The status table is split into two floats (tab:yzliu-status-b).
- **(h)** Length is 32 pp against the 18 pp ceiling (item 14).
- **(i)** In the meson form-factor status paragraph, the mention of the internal frontier report was replaced by the literature reason: Ji:2019sxk defers the details to later work.

**Errors found in the spec files:**
- the θ i0 prescription in VF-YZL-4, row 46 and F0.3 row 14;
- the −i0 in the outline's prop:yzliu-lfwf;
- the transcribed formula in the outline's prop:yzliu-gpd-oneloop;
- internal VF IDs in the five figure captions (FIGURES sources).

**Physics error found and fixed in the inherited draft:** the Sivers sketch paired the staple directions with the wrong light-like orientations. +ẑ is DY (past-pointing) and −ẑ is SIDIS (future-pointing), consistent with Ch22's def:lamet-quasi-tmd.

## 14. Open items for the lead author
1. **Length:** 32 pp against a 15 pp budget (LA-8 limit 18 pp). The outline's 51 statements, 4 tables, 5 figures and 3 boxes cannot fit at monograph density: floats and boxes alone take about 5.5 pp. The remaining text is already terse, and cutting it would remove proofs, re-derivations or status paragraphs that LA-8 protects. Sibling units are at 1.5–3× their budgets.
2. **Figure captions** in `figures/figset_D.tex`: remove the internal VF IDs and fix the γ in fig:yzliu-soft-hqet(b) (item 11).
3. **Register the new findings** for the next spec or verification patch: the θ-definition correction (VF-YZL-4, row 46, F0.3 row 14) and the candidate errata 9(i)–(ii) (and optionally (iii)) as new claims.
4. **Ji:2021znw:** the journal equation numbers and footnote come from the E02 record; check them against the PRD version.
5. **Re-check at print time:** the 「据我们所知」 priority statements (A03), and the statement that no Glauber analysis of finite-length staples exists as of 2026-10 (A06).

## open_items

1. Page budget: Ch23 is 32 pp against a 15 pp budget (LA-8 limit 18 pp). This needs a lead-author decision; reaching 18 pp would mean cutting proofs, re-derivations or status paragraphs that LA-8 protects.
2. Figure sources (figures/figset_D.tex): all five Ch23 figure captions print internal VF IDs, which should be deleted. Panel (b) of fig:yzliu-soft-hqet prints iṽ·D_E = D_τ − iβD_z without the factor γ that the text now carries. LA-10 does not let writers edit the blocks.
3. Spec correction to register: the hyperbolic-angle definition in VF-YZL-4, WRITER_SPEC row 46 and F0.3 row 14 should use √(v² − i0). Under Liu's own convention, only that form reproduces his Table 1; the chapter prints the corrected form and notes the deviation in a % comment.
4. New candidate errata for verification: Liu:2022nnk eq. (123), i0 in the square roots vs his Table 1; Su:2026eta eq. (7), opposite sign of the 1/(2(y−x)) term relative to the published kernel (preprint). Optionally also the −i0 in Ji:2021znw journal eqs. (49) and (74) (within E02, not an App Q row).
5. Ji:2021znw journal equation numbers (49), (51), (74) and footnote 1 are taken from the E02 verification record, because only arXiv v1 was accessible; check them against PRD 105 (2022) 076014.
6. Re-check at print time: the 「据我们所知（INSPIRE 检索，2026 年 10 月）」 priority statements (A03) and the 「尚未见……有限长订书钉的 Glauber 分析」 absence statement (A06).
7. Integrator: merge chapters/ch23_yzliu.bib-additions (Appelquist:1977es, Brambilla:1999qa) into the master bibliography.

