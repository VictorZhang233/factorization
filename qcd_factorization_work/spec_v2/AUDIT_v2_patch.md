# AUDIT_v2_patch — audit of the verify patch (spec v2.3 → v2.3.1)

**Date.** 2026-10-11.
**Auditor.** spec-v2 auditor (workflow subagent).
**Object.** The verify patch v2.3 of `spec_v2/` (spec patcher, 2026-10-11). The patch was checked against the verification records in `verify/`.
**Result.** spec **v2.3.1**. Every fix was applied by an exact-match script, and every edited file has a CHANGELOG entry. This file replaces the go/no-go table of `AUDIT_v2.md` §6, which now carries a "SUPERSEDED IN PART" banner.

---------------------------------------------------------------------------------------------------

## 0. Verdict

**GO for the writers on spec v2.3.1.**

- All criteria of the task pass (§2), after the fixes of §3.
- The audit found 13 groups of defects in v2.3 (D1–D13). The worst were:
  - six refuted statements still printed;
  - an internal contradiction in the only 「本书新结果」 proposition;
  - two wrong register status sentences;
  - an unverified factual sentence about a cited theorem in a printed status note.
- All defects are fixed. No unit is blocked (§5).

Three lead-author decisions remain open. None blocks the start of any unit, and each can change only a named tag, status sentence or hedge. Until the lead author decides, the spec text binds (§6 items 1–3):

1. **MD1.** `asm:appN-brst-nonlocal` is `\tagC` as a named gap. Confirmation has been outstanding since `AUDIT_v2.md`.
2. **MD19.** Three points need confirmation:
   - the six new assumptions and their tags;
   - the [P] grading of the App O model theorems;
   - the printed novelty marker.
3. **B.3 policy.** X2 Prop B.3 is the fibered–covariant identification of Γ for the triangle. The question is whether the final-review check `verify/extend/X2-subtraction/review_final_scripts/chk_B3.log` counts as its second independent confirmation.
   - If yes, `prop:appN-triangle-cs`(c) becomes unconditional, as in the X2 final report (§11).
   - If no, the other X2 items flagged [new-final] must be hedged the same way (§4 item 7).

---------------------------------------------------------------------------------------------------

## 1. Inputs

- **Task inputs:**
  - `CONTEXT.md`, `REQUIREMENTS.md`, `PROGRESS.md`;
  - the patcher's v2.3 report (16 checks, counts and concerns);
  - spec v2.3: `FINAL_OUTLINE_v2.md`, `WRITER_SPEC_v2.md`, `ASSUMPTIONS.md`, `VERIFIED_FORMULAS_v2.md`, `FIGURES_INDEX_v2.md`, `REFS_NOTES_v2.md`, `refs_merged_v2.bib`, `key_aliases_v2.tsv`;
  - `AUDIT_v2.md` and the three superseded outline drafts.
- **Verification records:**
  - `verify/CLAIM_VERDICTS.md`: 137 claims.
  - Stage records `verify/claims/batch_*_s1.md`, `batch_*_s2.md`.
  - Final reports `verify/extend_reports/X1-glauber_final.md`, `X2-subtraction_final.md`, `X3-ope_final.md`, with their review rounds (`-rev1-*`, `-rev2-*`, `-rev3-*`).
- **Final reviews of X1–X3.** These exist only as script logs. All logs pass, or rerun identical:
  - `verify/extend/X1-glauber/final_review_logs/`;
  - `verify/extend/X2-subtraction/review_final_scripts/*.log`: chk_B3, chk_C4e, chk_C4e3b, chk_misc, chk_coverage, and the archive reruns for the triangle and the bubble;
  - `verify/extend/X3-ope/review_final_scripts/logs/`: fr_ne_rank PASS, rerun_all IDENTICAL.

---------------------------------------------------------------------------------------------------

## 2. Checks

### 2.1 Summary

| # | criterion | method | result |
|---|---|---|---|
| 1 | no `[PENDING-VERIFY]` left | grep over the binding files; checker (reserved entries) | **PASS.** The binding files (the six spec documents and the bib) contain 0 markers and 0 reserved entries. The only occurrence, in `WRITER_SPEC_v2.md`, is the QA rule that forbids the retired comment form. Markers remain only in superseded files, all bannered (D13): OUTLINE_core 138, OUTLINE_frontier 53, OUTLINE_appMNOPQ 26, `AUDIT_v2.md` 5. Withdrawn slot labels occur only in `OUTLINE_appMNOPQ.md` and in two pre-patch figure-generator inputs (§6 item 9). |
| 2 | no refuted claim printed anywhere | every refuted, withdrawn or partly refuted claim traced through all binding files and the VF entries (list in §2.2) | **PASS after D1–D3, D10.** Found in v2.3: six refuted statements printed, wrong refutation reasons in four places, the refdoc "correct version" column binding for two refuted and two superseded items, and one unverified factual sentence. |
| 3 | every 「本书新结果」 satisfies the rule (two confirmations + literature check) | grep for all novelty words (「本书新结果」「首次」「文献中未见」); records | **PASS after D4.** Details in §2.3. |
| 4 | App Q rows confirmed twice; correct credit to prior corrections | each row traced to its stage-1 and stage-2 records; credits checked against the records | **PASS after D6, D11.** 21 rows (16 Q1 + 5 Q2), all confirmed in both stages (§2.4). |
| 5 | App M/N/O statements match the final reports; grades consistent with the final reviews | entry-by-entry comparison with X3, X2, X1 final; slot table §00.4; grades checked against the review rounds and the final-review logs | **PASS** except the accepted deviations of §4. One internal inconsistency fixed (D4); one printed unverified sentence fixed (D10). |
| 6 | grade propagation consistent | checker E1–E14; R_cond premise sentences spot-checked; assumption closures computed with the checker's own parser | **PASS.** The new [P] assumptions `asm:appO-adjacent-swap` and `asm:appO-real-jets`, and `asm:appO-collinear-ends` [A], feed only the App O model propositions: `prop:appO-twoexch-spectator`, `prop:appO-pergraph-weights`, `prop:appO-halfcoinc-sensitivity`, `prop:appO-twoexch-regulated`. The closures of `thm:dy-factorization` and `thm:tmd-factorization` contain none of the six new assumptions. |
| 7 | labels, `\uses`, assumptions and bib keys resolve | checker; `keys_check.py`; `figures_check.py`; the two register tables compared; used-by fields recomputed | **PASS** (counts in §2.5). |
| 8 | checker passes | `python3 -I spec_v2/checks/check_final_outline_v2.py spec_v2` | **PASS.** Exit 0; E1–E14 and W1–W2 OK. Log: `checks/check_final_outline_v2.log`. |
| 9 | the patcher's report | recount | **Confirmed:** 16 checks; 904 entries, 1341 registry rows, 47 register rows, 203 master rows; 16 Q1 + 5 Q2 rows; one novelty marker; six new assumptions; 48 bib additions; 1051 entries. |

### 2.2 Claims traced for criterion 2

| group | claims |
|---|---|
| refuted | E22, E32, N09, N13, N22, R-M15, R-M20 |
| refuted in single items | A04(ii), A06(3) and (4), A11(3) |
| disputed | E34. Its item (iii) was withdrawn by its authors (`Balitsky:2009xg`). |
| withdrawn | E19 |

### 2.3 Novelty markers (criterion 3)

- **The only marker** is on `prop:appN-triangle-cs`(a).
- **Two independent confirmations:**
  - `verify/extend_reports/X2-subtraction-rev2-2.md`, `-rev3-1.md`, `-rev3-2.md`;
  - the archive re-verification of the final review, `verify/extend/X2-subtraction/review_final_scripts/rerun_r3_archive_verify_triangle.log`.
- **Literature check:** X2 final report §12 and the queries of `-rev3-2.md`.
- **Other uses of 首次.** Two verified priority statements about cited works in Ch23 (A03) contain 「首次」. They are attributions, not novelty claims, and are allowed (D12).
- **N02.** The search-date sentence in Ch24 is confirmed by `batch_N01_s1.md` §3 and `batch_E33_s2.md` §7.

### 2.4 App Q confirmations (criterion 4)

| rows | claims | stage 1 | stage 2 |
|---|---|---|---|
| Q.1, Q.5, Q.6 | E23, E20, E21 | `batch_E19_s1.md` | `batch_E19_s2.md` |
| Q.2, Q.4, Q.16 | E17, E18, E13 | `batch_E13_s1.md` | `batch_E13_s2.md` |
| Q.3 | E25 | `batch_E25_s1.md` | `batch_E19_s2.md` |
| Q.7 | E26 | `batch_E25_s1.md` | `batch_E26_s2.md` |
| Q.8–Q.11 | E01, E03, E04, E02 | `batch_E01_s1.md` | `batch_E01_s2.md` |
| Q.12–Q.15 | E08, E09, E10, E11 | `batch_E07_s1.md` | `batch_E07_s2.md` |
| Q.17 (Q2) | E06 | `batch_E01_s1.md` | `batch_E01_s2.md` |
| Q.18 (Q2) | E12 | `batch_E07_s1.md` | `batch_E07_s2.md` |
| Q.19–Q.21 (Q2) | E27, E29, E30 | `batch_E25_s1.md` | `batch_E26_s2.md` |

Credits, verified:

- **E01:** first corrected in print by `Chou:2022drv`.
- **E02:** noted by the authors only for the RMP (D6).
- **E03:** "not reported" is correct. Liu–Chen 2021 noted a different typo, for x < 0 (`batch_E01_s1.md` §4.3).
- **Q2 rows:** each cites the published correction: `IzubuchiEtAl2018`, `Guo:2023pqw`, Collins' errata list, `GorishniiKataevLarin1991` with `SurguladzeSamuel1991`, and `Collins2002`.
- **Row references:** every "row Q.n" pointer in the binding files names the right claim.

### 2.5 Counts (criterion 7)

- **Checker:** 904 entries (0 reserved), 39 units, 1341 registry rows, 47 register rows, 203 master rows.
- **Keys** (all resolve; 0 unknown):

  | file | keys |
  |---|---|
  | FINAL_OUTLINE_v2 | 1029 |
  | ASSUMPTIONS | 108 |
  | WRITER_SPEC_v2 | 57, of which 3 alias mentions (pre-existing) |
  | VF | 100 |
  | REFS_NOTES_v2 | 755, of which 101 alias mentions |
  | FIGURES_INDEX_v2 | 12 |

- **Figures:** 120 required and 26 optional labels; PASS.
- **Register:** the §08 `### Assumptions` table and `ASSUMPTIONS.md` §1 are identical (47 rows). Every used-by field equals the computed `\uses` (0 mismatches).
- **Bibliography:** 1051 entries. PART 10 has 48 entries; their metadata were spot-checked.

---------------------------------------------------------------------------------------------------

## 3. Defects found and fixed (v2.3 → v2.3.1)

The script part that applies each fix is given in brackets (§7).

**D1. Refuted statements still printed** [a].
- Ch22 `prop:lamet-gluon-singlet`: N09 is refuted. Removed the sentence "only ratio/hybrid schemes converge for Regge-like singlet distributions".
- Ch22 `rem:lamet-open`(9): A06 item (3) is false. The N³LO non-singlet kernel exists (`Cheng:2024wyu`).
- Ch22 quasi-TMD paragraph (C): corrected per A04 item (ii).
- Ch24 `prop:front-nlo-bk`: the α_s²ζ(3) mismatch between NLO BK and NLO BFKL (E34 item (iii)) was printed as a disagreement, but its authors withdrew it (`Balitsky:2009xg`). Removed, together with the "longitudinal cutoffs" attribution.
- Ch24 `prop:front-glauber-bfkl`: corrected per A11 item (3). RS treat the n–n̄ production current at one and two loops; there is no all-order proof.
- VF-DIS-8: removed the "commonly quoted variant" sentence. E32 is refuted: there is no printed source.

**D2. Wrong reasons for refutations** [a].
- E22 in Ch19.
- N13 in §0.10, WRITER_SPEC_v2 §6.5 and VF-REF-12. The ordering-weight formula itself is wrong for k_j⁺ < 0 and for mixed signs, not only its novelty. The race formula holds only when all k_j⁺ > 0.

**D3. WRITER_SPEC_v2 §6.10** [a].
- The section made the "correct version" column of `refdoc/REFDOC_ANALYSIS.md` §2 binding. That column includes:
  - the refuted ERR-M15 and ERR-M20 (R-M15, R-M20);
  - the superseded ERR-S3 and ERR-M26.
- Overrides added. The refdoc file is a read-only input and is unchanged.

**D4. Internal contradiction in the X2a delivery** [a].
- `prop:appN-triangle-cs`(b) asserted the fibered–covariant identification of Γ (X2 Prop B.3, flagged [new-final], one independent confirmation), while (c) treated the same identification as unconfirmed.
- Now (b) identifies only the four Collins terms, and (ID)_Γ appears only as the premise of the implication (c).
- The status sentence of `prop:appN-triangle-exact` printed bookkeeping (「尚待第二次独立确认」). Removed.
- `tab:appN-status`, Ch25 OP-B1, §00.4 and the scope note of `lem:appN-identification` were aligned.
- The record paths of the two confirmations and of the literature check were added to the novelty note.

**D5. Wrong internal pointers** [a].
- `lem:appO-glauber-operator`(e) is now `lem:appO-joint-localization`(e).
- N12 is `prop:appN-triangle-exact`(d), not (c). Fixed in §0.10, Ch21 and the WRITER_SPEC_v2 K3 row.

**D6. App Q** [a, e].
- The note of row Q.4 (E18) was numbered "Q.3".
- Versions (arXiv or journal) are now stated for rows Q.3, Q.6, Q.7, Q.10, Q.15 (inclusion rule 4).
- **E02 credit.** PRD 105 (2022) 076014, footnote 1, notes the missing ½ only for its refs. [22] (the RMP, `JiEtAl2021`) and [23] (NPB 955). It does not note it for PLB 811 eq. (22) (`Ji:2019ewn`) or for APPB eqs. (53), (75) (`Liu:2022nnk`) (`batch_E01_s1.md` §3, `batch_E01_s2.md` §3).
- Row Q.11, the credit line, WRITER_SPEC_v2 §6.13 and WRITER_SPEC_v2 §3 row 43 now say so, and name the earlier correct form (`EbertStewartZhao2019`).

**D7. Register status sentences** [b]. Applied to the §08 table, `ASSUMPTIONS.md` §1 and the full entries, and Ch25 OP-A5. Tags unchanged.
- `asm:appM-forward` listed `asm:appM-oswi` as an input of the reduction. Per X3 final, `cor:appM-forward-ope` needs (A3), (Eε) and the Joglekar–Lee triangularity; `asm:appM-oswi` is only an alternative route to the gluon point ω = 0.
- `asm:appN-lce` stated that `lem:appN-identification` proves it. By X2 Cor A.5 the lemma needs (IL1)–(IL3) and cannot replace (LCE).

**D8. Stale items** [a, d, i].
- N02 still marked "pending" in the F5 annex.
- The LPC priority sentence still said "only after verification", although A03 is confirmed (REFS_NOTES_v2 row A03, I.5).
- Part VII sub-items titled "Pending" are renamed "Verification outcome".
- Header revisions:
  - WRITER_SPEC_v2 and VF;
  - REFS_NOTES_v2, which said "current revision v2.1, 1003 entries";
  - FIGURES_INDEX_v2, which said "v2.2" although it had a v2.3 entry;
  - `ASSUMPTIONS.md` and the FINAL_OUTLINE_v2 header ("ASSUMPTIONS revision v2.3").
- Bib count 1003 → 1051 in WRITER_SPEC_v2 §0.
- The §0.8 heading now points to this file for MD19.

**D9. Bookkeeping in master-table cells** [f].
- Nine §09 cells contained claim IDs, slot IDs or 「已证实」: rows II.1, II.8, II.27, II.29, III.4, III.5, III.27, VII.28, VII.46. These cells are transcribed into the printed `tab:summary-master` and `tab:intro-overview`.
- The bookkeeping was removed and the content kept. Rows III.27 and VII.46 now give the source keys instead.

**D10. Unverified or inexact sentences about cited theorems in printed status notes** [h, k].
- **`thm:ee-euclid-ir`.**
  - v2.3 said the Breitenlohner–Maison hypotheses "are spelled out for non-abelian gauge fields with FP ghosts".
  - Per the N24 record (`batch_N18_s2.md` §7.4), BM II do not discuss FP ghosts explicitly, and their existence theorem is distributional.
  - Rewritten with these limits. The pointwise statement is credited to `PoggioQuinn1976`, with `LowensteinZimmermann1975` for BPHZL.
- **`prop:appM-zero-momentum-insertion`.**
  - v2.3 printed as a fact that "the ε of `Breitenlohner:1976te` is the damping regulator of that construction, not the dimension shift of DR".
  - No verification record supports this. X3 final §2 reads BM II Thm 1 as a statement about the dimensionally renormalized amplitude.
  - Replaced by the open point: identifying the limit with the DR MS-bar insertion, in the framework of `Breitenlohner:1975hg`. The claim that the proposition "settles" `rem:appM-exceptional` is now conditional on that identification.
  - The grade stays [A] (§4 item 1).

**D11. App Q cross-references** [j].
- "not an App Q row" (E12, Ch19) and "no App Q row" (E29, Ch6) contradicted `tab:appQ-errata-b` rows Q.18 and Q.20.
- They also contradicted WRITER_SPEC_v2 §6.13, VF-EE-10 and REFS_NOTES_v2 §3.5. Corrected.

**D12. QA script and writer rules** [a, d, h].
- `checks/check_unit_v2.py`:
  - C8a also flags the retired comment form `% PENDING-VERIFY:`;
  - C8b shows 「本书新结果」「首次」「文献中未见」 and the printed bookkeeping words 「独立确认」「尚待」, which must be justified.
- WRITER_SPEC_v2:
  - §6.5 item 3: the two verified priority statements of Ch23 about cited works (`Ji:2019sxk`, `Liu:2023pjb`; A03) may contain 「首次」;
  - §6.9: new traps for E34(iii), N09, E22, E32;
  - §6.12: verification bookkeeping is never printed. The exceptions are App Q's 核实 column and the novelty wording of §6.5.

**D13. Superseded files** [c].
- "VOID MARKERS" banners on `OUTLINE_core.md`, `OUTLINE_frontier.md` and `OUTLINE_appMNOPQ.md`. Their markers, planning tags and withdrawn slot labels must never be copied.
- "SUPERSEDED IN PART" banner on `AUDIT_v2.md`. Its §6 is replaced by §5 below.

---------------------------------------------------------------------------------------------------

## 4. Deviations from the final reports (accepted, documented, unchanged)

1. **`prop:appM-zero-momentum-insertion` is [A]; X3 Remark F.5 says [R, R_PT].**
   - The reviewed grade of Remark F.5 was [A], pending O10 (`X3-ope-rev1-1.md`, `-rev2-1.md`, `-rev2-2.md`, `-rev3-1.md`).
   - X3 raised it to [R, R_PT] in its final round (W19) after reading BM II. No independent confirmation followed; the final-review logs do not address it.
   - [A] is therefore consistent with the reviews. The upgrade path is stated in the entry (D10).
2. **X1 exponents.** The spec prints both the report values (ε^0.7–ε^0.77) and the final-review refit (ε^0.63, ε^0.70, ε^0.73), each with its source. Writers must not merge them.
3. **`prop:appO-g6-ladder`.** X1 P5 is graded [A], as in the spec; X1 only proposed a `rem:` label. The registered label stays.
4. **`lem:appM-matroid`** cites Schultka §4, where X3 also cites Feichtner–Sturmfels Prop 2.4 for item (b). It is mathematics either way.
5. **X3 Lemma A.7** appears as the untagged `rem:appM-remainder-reduction` (slot X3a not delivered).
6. **(LCE) and (RA1)(RA2)** are local hypotheses in X2. They are registered as `asm:appN-lce` and `asm:appN-analytic-reg` ([A]) so that the R_cond statements can name them (MD19).
7. **Other [new-final] items.** `prop:appN-phi36-dis`(c) and `prop:appN-twoloop-remainder`(ii),(iv) are printed without a hedge, on the same kind of evidence as B.3: the final report plus one passing final-review check.
   - This is consistent with the X2 final report.
   - It applies a different standard from the one used for B.3 in `prop:appN-triangle-cs`(c). This is the policy decision of §6 item 3.
8. **App Q row numbering.** The row numbers Q.1–Q.21 look like section numbers of App Q. Writers always write "row Q.n" (WRITER_SPEC_v2 §6.13). Cosmetic.

---------------------------------------------------------------------------------------------------

## 5. Go/no-go per unit (replaces `AUDIT_v2.md` §6)

Status meanings:

- **GO:** may be written now from spec v2.3.1; nothing is pending.
- **GO (LA):** may be written now. A named lead-author decision (§6) is pending, which can change only the named tag, status sentence or hedge. The spec text binds until the decision; the writer flags the affected sentences in the unit report.
- **GO-last:** summarizes other units; written at the end.
- **NO-GO:** none.

Start conditions follow WRITER_SPEC_v2 §12.3.

| unit | writer | status | conditions / notes |
|---|---|---|---|
| front, Ch1 `intro` | W01 | GO-last | after all chapters. ★ rows from §09 (v2.3.1 cells carry no claim IDs). 47-entry register table. Regenerate `fig:intro-dependency` from v2.3.1 (FIGURES_INDEX_v2 CHANGELOG v2.3 item 3 and v2.3.1 item 2). The register tags follow MD1 and MD19. |
| Ch2 `qcd` | W02 | GO | first wave. E28 is a convention remark: Sterman–Weinberg's own ln 2ε form is correct; no App Q row. |
| Ch3 `prelim` | W03 | GO | first wave. N26: attribution `Echevarria:2015byo`; novelty not claimed. |
| Ch4 `ir` | W04 | GO | after Ch2, Ch3. N02 and N03 remarks without novelty marker. E14 and E15 status paragraphs with Collins' diagnoses. |
| Ch5 `sudakov` | W05 | GO | after Ch3, Ch4. E23 is row Q.1. N12 is a pointer to a sharpened result, never marked new. |
| Ch6 `ee` | W06 | GO | after Ch2, Ch3. `thm:ee-euclid-ir` status note as rewritten (D10). E29: one history sentence, plus row Q.20 in App Q (D11). |
| Ch7 `dis` | W07 | GO | after Ch2, Ch3, Ch6. App M route final (X3). `prop:dis-c-oneloop` prints no variant (E32 refuted). 13 proof-delivery targets with W08. |
| Ch8 `pdf` | W09 | GO | after Ch7. `conj:pdf-positivity` uses the verified debate facts (E35). |
| Ch9 `method` | W10 | GO (LA: MD1) | after Ch4, Ch5, Ch8 and the App N statements. Integrates W11's draft of `sec:method-subtraction`. Slots: X2a delivered; X2b and X2c not delivered (fallback `thm:appN-subtraction` [R, R_cond]); X2d open. Named gap in `lem:method-ward-multi` / `thm:method-template`. |
| Ch10 `disall` | W12 | GO | after Ch9 and App N. Slot outcomes of §00.4; no tag changes. |
| Ch11 `coll` | W13 | GO | after Ch9, Ch10. |
| Ch12 `dy` | W14 | GO | after Ch9 and the App O statements; integrates W15's drafts. `prop:dy-eikonal-twogluon` carries no marker: N01 is a known result (`Meggiolaro:1996hf`, `Giordano:2006vv`). A11 item (3) corrected. The App O model theorems are referred to as [P] (MD19). |
| Ch13 `thr` | W16 | GO | after Ch12. |
| Ch14 `tmd` | W17 | GO | after Ch9, Ch12, App N, App O. E17 is row Q.2. `lem:tmd-glauber` stays [A]. |
| Ch15 `scet` | W18 | GO | after Ch5, Ch9. E24 is a convention hazard kept in the statement; E25 is row Q.3. |
| Ch16 `jets` | W19 | GO | after Ch15. E28 convention remark. E16 is now confirmed by two groups (`Banfi:2025mra`, `Becher:2026kbr`). |
| Ch17 `smallx` | W20 | GO | after Ch9. |
| Ch18 `break` | W21 | GO | after Ch12, Ch14. N16–N18 are our derivations of known results. E18 is row Q.4. E36 wording. |
| Ch19 `excl` | W22 | GO | after Ch9 and App N. E20 and E21 are rows Q.5 and Q.6. E22 is refuted: nothing printed (reason corrected, D2). E12 is row Q.18 (D11). |
| Ch20 `heavy` | W23 | GO | after Ch15. E26 is row Q.7. N22 is refuted: no illustration of our own. |
| Ch21 `power` | W24 | GO | after Ch7, Ch9. The N12 pointer goes to `prop:appN-triangle-exact`(d) (D5). |
| Ch22 `lamet` | W25 | GO | after Ch8, Ch14, Ch21. D1 fixes applied (N09, A06(3), A04(ii)). Re-derive `prop:lamet-tails`(iii), which rests on one verification record (§6 item 7). |
| Ch23 `yzliu` | W26 | GO | after Ch14, Ch22. E02 credit for the RMP only (D6). The two verified priority statements may contain 「首次」 (D12). `prop:yzliu-gpd-oneloop` must be re-derived (MD14). |
| Ch24 `front` | W27 | GO | after Ch4, Ch9, Ch12, Ch18, Ch21. E34 item (iii) and A11 item (3) corrected (D1). N02 remark with the search-date sentence. `prop:front-brst-bilocal` stays [A] (N04, prior art `Braun:2019qtp`). |
| Ch25 `summary` | W28 | GO-last | after everything else. Rows from §09 (203; v2.3.1 cells). OP-A5 and OP-B1 as corrected (D4, D7). |
| App A, C, E, I, L | W03, W06, W04, W03, W09 | GO | App L: the N04 circularity check of `prop:appL-renormalized` remains with the writer. |
| App B | W05 | GO | with Ch5. |
| App D | W04 | GO | A08 (preprint status of `Collins:2020euz`). `lem:appD-gordan` is classical; no marker. |
| App F | W10 | GO (LA: MD1) | named gap in `prop:appF-induction`. |
| App G, App H | W29 | GO | after the drafts of Ch6–Ch14. |
| App J | W02 | GO | `lem:appJ-cut-hermiticity`: N14 is unresolved. The tag covers (a) and (b); the hedge of (c) is printed; never marked new. |
| App K | W09 | GO | with Ch8. |
| App M | W08 | GO (LA: MD19) | from the outline (Ch7 statements). X3 final statements. `asm:appM-oswi` is [A]. `prop:appM-zero-momentum-insertion` is [A], with the status note of D10. No novelty marker on `thm:appM-forward-expansion`: its novelty check is open. |
| App N | W11 | GO (LA: B.3, MD19, MD1) | starts first (critical path). `prop:appN-triangle-cs`: (a) is the only 「本书新结果」, worded as in WRITER_SPEC_v2 §6.5; (b) covers the four Collins terms only; (c) is an implication with premise (ID)_Γ. Reproduce the X2 [new-final] derivations (B.3, C.4e, …) in full: the final reviews exist only as logs. `asm:appN-lce` and `asm:appN-analytic-reg` are [A]. |
| App O | W15 | GO (LA: MD19) | after App N §N.3–§N.5 are frozen. Model theorems [P], with `asm:appO-adjacent-swap` and `asm:appO-real-jets` [P] and `asm:appO-collinear-ends` [A]. Ordering weights as corrected in `lem:appO-joint-localization` (N13). The 32 pp budget is tight: 77 entries; §0.1 item 4 cuts §O.11 first. |
| App P | W28 + integrator | GO-last | generated at integration from FINAL_OUTLINE_v2 v2.3.1. Rebuild the generator inputs (D13; §6 item 9). |
| App Q | W30 | GO | `verify/` is complete; final rows: 16 Q1 + 5 Q2, each confirmed twice (§2.4). Credits as in the tables: E01 `Chou:2022drv`; E02 the authors, for the RMP only. Versions stated. |

---------------------------------------------------------------------------------------------------

## 6. Open items for the lead author

1. **MD1.** Confirm `asm:appN-brst-nonlocal` as `\tagC`, a named gap. This affects the status sentences of Ch9, App F, App N and `thm:appN-structure`.
2. **MD19.** Confirm:
   - the six new assumptions and their tags;
   - the [P] grading of the App O model theorems;
   - the printed novelty marker on `prop:appN-triangle-cs`(a);
   - X1c (`lem:appO-side-independent-windows`) at [R, R_cond] instead of the planned [R, R_PT].
3. **B.3 policy.** Choose one:
   - (i) Accept `chk_B3.log` as the second independent confirmation of X2 Prop B.3. Then print (c) unconditionally, using the X2 §11 sentence.
   - (ii) Hedge every X2 item flagged [new-final] in the same way: `prop:appN-phi36-dis`(c) and `prop:appN-twoloop-remainder`(ii),(iv).
4. **`prop:appM-zero-momentum-insertion`.** It can go up to [R, R_PT] only after two steps: the identification of D10 is written out (BM II in the framework of `Breitenlohner:1975hg`, which X3 did not read), and it is independently confirmed.
5. **Final reviews of X1–X3.** They exist only as script logs. It is recommended to persist them as review documents, so that the "two confirmations" of the [new-final] items can be cited.
6. **X1 exponents.** Two sets are printed, each with its source (§4 item 2). Decide whether the book keeps both.
7. **`prop:lamet-tails`(iii).** The N09 correction rests on one verification record (`batch_N07_s1.md` §4.3). The Ch22 writer re-derives it; a second record would be better.
8. **N14** is unresolved; `lem:appJ-cut-hermiticity` stays hedged.
9. **Figures.**
   - The pre-patch generator inputs `figures/test_fa/uses.json` and `figures/test_ff/scripts/outline.json` contain withdrawn slot labels. Rebuild them from FINAL_OUTLINE_v2 v2.3.1.
   - Then regenerate: `fig:intro-dependency`, `fig:summary-status-map`, `fig:summary-hypotheses`, the App P graphs, `fig:appM-dependency`, `fig:appO-flowchart`, and the optional `fig:lamet-dependency`.
   - Captions must be re-checked by FIGURES_INDEX_v2 rule 9. No caption in `figures/figset_*.tex` contains a planning marker or a slot label; `fig:lamet-hybrid` does not use the refuted N09 domain statement.
10. **`refdoc/REFDOC_ANALYSIS.md` §2** still lists the refuted and superseded "correct versions". It is read-only for writers; the overrides are in WRITER_SPEC_v2 §6.10.
11. **App Q row numbering** collides with the section numbering (§4 item 8). Optionally rename the rows.
12. **Unverified locations.** The remaining location hedges are 9 occurrences of 「位置待核实」 and the "not re-read" / "not verified" notes. They must be resolved or kept as hedges at print time; WRITER_SPEC_v2 §10 item 10 tracks them.
13. **App O page budget** (§5).
14. **Optional, Ch22.** If the x < 0 form of `Braun:2018brg` eq. (61) is mentioned, Liu–Chen, PRD 104 (2021) 094501, footnote 1, should be credited. It is not in the bib.
15. **Git.** Nothing was committed.

---------------------------------------------------------------------------------------------------

## 7. Reproducibility

- **Backup.** The v2.3 state of the 11 edited files is in `verify/audit_v231_backup/`:
  - `FINAL_OUTLINE_v2.md`, `WRITER_SPEC_v2.md`, `VERIFIED_FORMULAS_v2.md`, `REFS_NOTES_v2.md`, `ASSUMPTIONS.md`, `FIGURES_INDEX_v2.md`;
  - `AUDIT_v2.md`, `OUTLINE_core.md`, `OUTLINE_appMNOPQ.md`, `OUTLINE_frontier.md`;
  - `check_unit_v2.py`.
- **Scripts.** All are in `verify/audit_v231_scripts/`. Every script is an exact-match edit and aborts unless each target matches exactly once.

  | part | script | edits | content |
  |---|---|---|---|
  | a | `apply_audit_v231.py` | 42 edits + 4 CHANGELOG entries | D1–D5, D6 (Q.4 and versions), D8, D12 (§6.5, §6.9, §6.10, §6.12) |
  | b | `apply_audit_v231b.py` | 9 | D7 |
  | c | `apply_audit_v231c.py` | 4 banners | D13 |
  | d | `apply_audit_v231d.py` | 8 | headers, bib count, `check_unit_v2.py` C8 |
  | e | `apply_audit_v231e.py` | 4 | E02 credit |
  | f | `apply_audit_v231f.py` | 9 | §09 cells |
  | g | `apply_audit_v231g.py` | 2 | CHANGELOG items |
  | h | `apply_audit_v231h.py` | 7 | `thm:ee-euclid-ir`; 「首次」 rule |
  | i | `apply_audit_v231i.py` | 11 + 1 entry | version references |
  | j | `apply_audit_v231j.py` | 4 | E12 and E29 cross-references |
  | k | `apply_audit_v231k.py` | 3 | `prop:appM-zero-momentum-insertion` |

- **Driver.** `apply_all_v231.py TARGETDIR` copies the backup and runs parts a–k in order. Its output is byte-identical to `spec_v2/` for all 10 spec files and `checks/check_unit_v2.py` (verified after part k).
- **Checks** (run from the work directory; logs refreshed in `spec_v2/checks/`):

```
python3 -I spec_v2/checks/check_final_outline_v2.py spec_v2   # exit 0; E1–E14, W1–W2 OK
python3 -I spec_v2/checks/keys_check.py "$PWD"                # RESULT: PASS (no unknown keys)
python3 -I spec_v2/checks/figures_check.py "$PWD"             # RESULT: PASS
python3 -I spec_v2/checks/check_unit_v2.py UNIT.tex UNITID    # writers (C8a/C8b updated)
```

- **Unchanged:** `refs_merged_v2.bib`, `key_aliases_v2.tsv`, all `verify/` records, `refdoc/`. The only additions under `verify/` are the two new directories `verify/audit_v231_backup/` and `verify/audit_v231_scripts/`. Nothing was committed.
