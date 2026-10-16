# AUDIT_v2 — integration and adversarial audit of spec v2

> **SUPERSEDED IN PART (2026-10-11).** The verify patch v2.3 resolved the pending items of this audit; its audit is `AUDIT_v2_patch.md`, whose go/no-go table (§5) replaces §6 below. The merge decisions MD1–MD18 and the defect log of §3–§4 remain valid as records.

**Date:** 2026-10-10. **Author:** spec-v2 integrator and auditor.

**Inputs.** The drafts `OUTLINE_core.md` (5126 lines), `OUTLINE_appMNOPQ.md` (1048), `OUTLINE_frontier.md` (1786) and `ASSUMPTIONS.md` (631). The companion drafts `WRITER_SPEC_v2.md` (v2.1), `FIGURES_INDEX_v2.md` (v2.1), `VERIFIED_FORMULAS_v2.md`, `REFS_NOTES_v2.md`, `refs_merged_v2.bib` (1003 entries) and `key_aliases_v2.tsv`. Also: `CONTEXT.md`, `REQUIREMENTS.md`, spec v1 (`spec/`), `refdoc/REFDOC_ANALYSIS.md` §5, the frontier reports, `research/survey/SURVEY.md`, `research/critic/REVIEW.md`, `verify/CLAIMS.md`, and the stage-1 verification records available at 19:30 (`verify/claims/batch_E01_s1.md`, `batch_E07_s1.md`, `batch_E13_s1.md`, `batch_E19_s1.md`, `batch_E25_s1.md`, `batch_E31_s1.md`).

**Outputs written to `spec_v2/`.**
- `FINAL_OUTLINE_v2.md`: new.
- `AUDIT_v2.md`: this file.
- `checks/check_final_outline_v2.py` and `checks/check_final_outline_v2.log`: new.
- `checks/figures_check.py`: expected counts updated to v2.2 (120 required, 26 optional; PASS).
- `checks/keys_check.py`: now also scans `FINAL_OUTLINE_v2.md` and `ASSUMPTIONS.md` (PASS: 977 and 98 keys, all merged keys).
- Both logs refreshed.
- `WRITER_SPEC_v2.md` → v2.2.
- `ASSUMPTIONS.md` → v2.2.
- `FIGURES_INDEX_v2.md` → v2.2.
- `VERIFIED_FORMULAS_v2.md`: "Used in" lines updated (v2.2).
- A one-line SUPERSEDED banner prepended to each of the three outline drafts. Their content is otherwise unchanged.

`REFS_NOTES_v2.md`, `refs_merged_v2.bib` and `key_aliases_v2.tsv` are unchanged.

---------------------------------------------------------------------------------------------------

## 1. Verdict

**Spec v2 is ready to hand to the writers, with two conditions.**

1. The lead author should confirm merge decision **MD1**: `asm:appN-brst-nonlocal` is tagged [C] and treated as a *named gap* (details in §3). The decision changes only the wording of status paragraphs. No tag changes.
2. Units that depend on the running proof extensions X1/X2/X3 or on App Q are written after the verify patch, or before it under the protocol of WRITER_SPEC_v2 §6.12. §6 lists the units.

**The integrated outline in numbers.**
- 847 canonical statement entries in 39 units. They include 92 worked examples and 41 assumptions.
- 14 reserved [PENDING-VERIFY] slot labels.
- 1325 registry rows.
- 200 master-table rows.
- 236 [PENDING-VERIFY] markers.
- Statement tags (assumptions excluded): (no tag) 301; [A] 146; [R, R_PT] 118; pure mathematics 59; [R, R_cond] 43; [P] 40; [R, R_def] 37; [C] 28; [V] 22; [R, R_OPE] 12.

All fourteen error-level checks of `checks/check_final_outline_v2.py` pass on the files in `spec_v2/` (log: `checks/check_final_outline_v2.log`). Both warning-level checks pass as well: no undefined label is mentioned, and there is no hidden forward dependency. `checks/check_unit_v2.py` reads the new registry correctly; I tested it with a synthetic Ch07 unit, and it detected the owner set and a deliberate forward `\uses`.

---------------------------------------------------------------------------------------------------

## 2. What the audit checked, and the results

| criterion of the task | method | result on FINAL_OUTLINE_v2 |
|---|---|---|
| unique labels, correct prefixes, moved v1 labels kept | E1, E2; comparison with the v1 registry | OK. All 397 v1 statement labels are present; the only exceptions to the prefix rule are the 9 moved `prelim` labels (Ch2) and the v1 `lattice` labels (Ch22). One draft violation was fixed: `rem:prelim-bphz-brst` → `rem:qcd-bphz-brst` |
| every `\uses` target exists and is earlier, an appendix statement or an assumption | E3, E4 | OK |
| no forward dependency between chapters | E4 (direct edges) and the new W2 (paths through appendices) | OK. The drafts had none directly but **59 hidden ones through appendices**, all removed (§4.2) |
| no dependency cycle | E5 (Tarjan) | OK. The drafts had **one cycle**, removed (§4.1) |
| grades consistent with grade propagation; qualifier compatibility; [V] never a premise | E6, E7 (WRITER_SPEC_v2 v2.2 §4.6 incl. the R_OPE exception, R_cond content grades, global-only R_cond rule) | OK after the fixes of §4.3 |
| grades consistent with survey, critic and refdoc verdicts; no over-claims; conservative frontier grades | comparison with the v1 tags (no v1 tag strengthened; two weakenings, `prop:pdf-timelike-dglap` and `rem:appJ-nonlocal`); semantic review of every new [R] statement and of all frontier statuses (§4.4) | OK after MD1, MD6, MD7, MD14 and the restriction of `prop:break-jet-veto` |
| every R_cond premise listed and in `\uses` | E7 | OK after fixes (4 statements) |
| status paragraphs for [A]/[P]/[C]/[V]; qualifier for every [R] | E8 | OK after fixes (4 frontier statements) |
| every `asm:` label in `ASSUMPTIONS.md`, same tag, used | E9; identity of the register table in FINAL §08 and ASSUMPTIONS.md §1 (diff) | OK. 41 entries. Tags: 25 `\tagA`, 1 `\tagP`, 14 `\tagC` (6 global), 1 untagged |
| registry = entries (owners, tags) | E10 | OK. The registry is regenerated for all 43 units |
| every figure owned | E11 against FIGURES_INDEX_v2 v2.2 §5 | OK. 120 required and 26 optional figures, one owner each |
| citation keys in `refs_merged_v2.bib` | E12, plus an exhaustive scan of backticked tokens | OK. All 978 citation keys resolve; only alias mentions in WRITER_SPEC are not keys. Cross-checked with the drafter's `checks/keys_check.py`: 977 keys in FINAL_OUTLINE_v2 and 98 in ASSUMPTIONS, all merged keys |
| page budgets ≈ 487 | E13 | Exactly 487 (front 6 + chapters 352 + appendices 129) |
| master-table rows: label exists, tag = entry tag | E14 | OK. All 200 rows |
| WRITER_SPEC_v2 complete and unambiguous for about 30 writers | review; v2.2 edits (§5) | Writer assignment W01–W30 added; every rule that the merge changed is restated; every label it cites exists |
| [PENDING-VERIFY] markers kept | marker count; merged register FINAL §0.10 | Kept (236). The stage-1 notes are recorded there; no pending status was ended |

---------------------------------------------------------------------------------------------------

## 3. Merge decisions (binding unless the lead author overrides; table in FINAL_OUTLINE_v2 §0.8)

The prefix **MD** distinguishes these decisions from the v1 lead-author decisions D1–D7, which the entries still cite (e.g. "decision D3").

**MD1 — the multilocal BRST classification is a named gap [C].**
- **Background.**
  - The core draft had `rem:appJ-nonlocal` tagged [A] and asserting the classification.
  - The appendix draft registered the same claim as `asm:appN-brst-nonlocal` with `\tagA` ("decision flagged") and asked for a `\uses` edge from `lem:method-ward-multi`.
  - The frontier draft stated it as `conj:front-brst-multilocal` [C].
  - So one claim carried two contradictory grades. The literature is unambiguous: Collins 2011 §11.3.2 writes "no proof has been given … I will assume the result is true", and frontier/others §8.3 grades the general case [C].
- **Options.**
  - (a) Keep `\tagA`. This violates the tag criterion ("covered by an all-order argument").
  - (b) Tag it `\tagC` and make it a premise of `lem:method-ward-multi`. Every Feynman-gauge process theorem then drops to [C], contrary to the binding master-table grades and to the survey verdict: DIS factorization is [A] with this gap named.
  - (c) **Adopted.** Tag it `\tagC`; make it a premise only of the precise conditional theorem `thm:appN-structure`, whose content grade becomes [C]. The chapter [A] statements (`lem:method-ward-multi`, `thm:method-template`, `prop:appF-induction`, `thm:disall-factorization`, `thm:dy-factorization`, and every process chapter through `thm:method-template`) *name* it in their 「地位与缺口」 paragraphs as the explicitly assumed step of the standard argument. `def:intro-tags` (Ch1) prints the convention, WRITER_SPEC_v2 §4.6 item 6 makes it a rule, and App P check C-P17 enforces it.
- **Remaining tension.** Under (c) a sharp reader may still read the process theorems as "[A] modulo a [C] step". That is exactly how the outline now describes them, but it should be the lead author's explicit choice. **Confirmation requested.**

**MD2 — the split of (Z2) is kept.**
- `asm:appN-ir-regulator` [C] is a premise only of `thm:disall-renorm-compat`. Its premise sentence was incomplete in the core draft; it now lists (Z1), (Z3)(i), `asm:appN-ir-regulator` and `asm:appN-contour`(b), and the theorem has content grade [C].
- `prop:disall-h5` [A] had `\uses{thm:disall-renorm-compat}`, which would violate grade propagation. It now uses the dimensional-regularization route: `asm:appN-multren`(Z3)(ii) + `prop:disall-factorized-subtraction`.

**MD3 — the technical App M/N/O assumptions stay `\tagA`.**
- This includes the four entries the core draft marked "at risk": `asm:appO-lcopt`, `asm:appN-endpoint`, `asm:appM-forward`, `asm:appN-multren`.
- Each one formalizes a step that the accepted all-order argument covers as a scaling statement (refdoc S8 "B/B′"). This is consistent with the binding [A] grades.

**MD4 — global-only R_cond premises are allowed in the hadron-level part of R_PT/R_OPE statements.**
- Condition: the statement's status line names the same global assumptions.
- This closes the rule gap the core drafter reported (`thm:dis-moments`(b), `prop:lattice-moments`). Written into WRITER_SPEC_v2 §4.6 item 1.

**MD5 — App A–L budgets rebalanced inside the 35 pp:**
- New split: A 3, B 3, C 3, D 4, E 3, F 3, G 3, H 2, I 2, J 3, K 4, L 2.
- This is the core drafter's proposal. Refdoc S50/S53 add lemmas to App K and App J. The v1 split can be restored; no statement may be deleted to fit.

**MD6 — `rem:appJ-nonlocal` weakened** from v1 [A] to an untagged status remark that points to `asm:appN-brst-nonlocal`, `conj:front-brst-multilocal` and `prop:front-brst-bilocal`. This is a weakening, which is allowed.

**MD7 — `prop:front-brst-bilocal` (claim N04) gets planning tag [A].**
- [A] is the source grade.
- The frontier drafter had raised it to [R, R_PT] on the strength of our own, still unverified argument; that argument also carries a circularity risk with `prop:appL-renormalized`.
- The tag is raised to [R, R_PT] only if N04 passes, including the circularity check. This follows "frontier grades conservative".

**MD8 — `thm:power-ope-convergence` keeps [R, R_PT].**
- It is a model statement: its first sentence names massive Euclidean $\varphi^4_4$ at fixed loop order. This is consistent with the massive-model [R, R_PT] theorems of App M.
- The broader `prop:front-ope-scalar` stays [P]: its massless, associativity and curved-space parts are read only at abstract level.

**MD9 — Ch22 owns the quasi-TMD factorization theorem.** This covers `thm:lamet-quasi-tmd`, the off-light-cone and reduced soft functions, the lattice Collins–Soper kernel and TMD ratios. The frontier drafter's departure from the v2.1 default was forced: `prop:lattice-cs-kernel` is a moved v1 label, and the no-forward-edge rule applies. WRITER_SPEC §5.6, §6.11 and §12.2 and the VF "Used in" lines are patched accordingly.

**MD10 — `lem:appO-past-unitarity` deleted.** It duplicated the past-pointing case of Ch9 `lem:method-soft-unitarity`, which states it explicitly. All references are redirected.

**MD11 — `rem:prelim-bphz-brst` → `rem:qcd-bphz-brst`.** It is a new v2 label that carried the Ch3 key but is owned by Ch2; no other unit cites it.

**MD12 — App P.**
- `longtable` is loaded by the integrator in the master driver; the common preamble is untouched and unit writers never use it.
- The per-part graphs (`fig:appP-dependency-b` … `-h`, now registered) show the main theorems, at most 60 nodes each.
- New check C-P17 for named gaps.
- Budget: 10 pp with compaction levels 0–3.
- Master-table row IDs are part numerals.

**MD13 — `asm:front-scet-modes` stays with Ch24**, since no Ch15 statement cites it.

**MD14 — frontier tag questions.**
- `thm:lamet-lcs` stays [A] (not R_OPE).
- `thm:front-collins-pinch` stays [A]: the proof exists only in a preprint (v1 decision D3, A08).
- The fallback for `prop:front-commuting` is [C], not [A]: its premise `asm:front-mor-complete` is [C].
- `prop:yzliu-gpd-oneloop` is [R, R_PT] only with a mandatory re-derivation (the source is a 2026 preprint); otherwise [A].

**MD15 — App M's names for the parts of "the OPE holds" become (OPE1)–(OPE5).** The old names clashed with the inner items (O1)(O2) of `asm:intro-np-ope`.

**MD16 — stage-1 records that appeared after the drafts are used only to correct misleading planning texts:**
- E22: the Ch19 sentence is dropped (refuted as phrased).
- E28 and E32 are removed from the App Q candidates (not errata).
- E32: Ch7 no longer prints the "variant".
- E33: the DHYZ erratum reverses its conclusion; noted in Ch24.
- E20, E21, E23, E25, E26: stage-1 notes added to the App Q table.

All these claims stay [PENDING-VERIFY].

**MD17 — the partial-exponentiation lemma is owned by Ch23** (`lem:yzliu-partial-exp`); App B gets no `sec:appB-partial`.

**MD18 — binding assumption texts are the owners' entries.**
- Ch1 entries for `asm:intro-*`.
- Part VII annex §F1 for the frontier entries.
- App M/N/O entries together with ASSUMPTIONS.md §3.2–§3.4.

ASSUMPTIONS.md v2.2 reproduces these texts verbatim and recomputes every 「被使用于」 field from the final `\uses` data. In passing, the v2.1 register had *different* provisional texts for the two Ch24 entries (for example (SM2) of `asm:front-scet-modes`); the owner's text now governs.

---------------------------------------------------------------------------------------------------

## 4. Defects found in the drafts and fixed

The patch log lists 131 operations: P1–P43 in `FINAL_OUTLINE_v2`, plus the companion-file edits. Each operation is a label-addressed, exact-match edit that fails if its target is absent.

### 4.1 Dependency cycle (1)
- **Cycle:** `lem:method-ward-multi` → `prop:appF-induction` → `asm:appN-ward-product` → `lem:method-ward-multi`.
- **Cause:** the App F induction is the *discharge path* of `asm:appN-ward-product`, not one of its users.
- **Fix:** removed the edge; App F now names the named gap instead (P35).

### 4.2 Hidden forward dependencies (59 chapter statements, 20 root edges; all removed)
The direct-edge rule was satisfied, but 59 chapter statements reached statements of *later* chapters through appendix statements. Examples:
- DIS factorization depended on the Ch19 DA definition.
- Ch4 depended on Ch9 objects.
- Ch9 depended on Ch12 and Ch14 objects.

Root causes and fixes:
- **Ch4/Ch5 statements listing App N assumptions formulated with Ch9 objects.** These are `thm:ir-leading-regions`, `prop:ir-super-leading` and `thm:sudakov-factorization`. The App N assumptions are now named as pointers only, and the master-table bottleneck cells I.15, I.16 and I.25 were adjusted (P32–P34).
- **App N approximator definitions citing the Ch14/Ch19 definitions as context.** `def:appN-tmd-approx` cited `def:tmd-collins`, and `def:appN-excl-approx` cited `def:excl-da`. Both are now pointers; `asm:appN-endpoint` now uses `def:excl-da` itself (P36).
- **App O citing Ch12 material.**
  - `def:dy-kin` and `ex:dy-future-vs-past` are now pointers (P37).
  - The precise orientation lemma is now the App O lemma `lem:appO-orientation`. Ch12 `lem:dy-poles-orientation` is its chapter statement and cites it (P39).

A new rule in WRITER_SPEC_v2 §4.5 item 5 forbids hidden forward dependencies, and checker W2 enforces it.

### 4.3 Grade propagation and the R_cond rules
- `thm:disall-renorm-compat`: premise sentence completed; content grade [C] (MD2).
- `prop:disall-h5`: re-routed (MD2).
- `prop:excl-soft-cancel`: `asm:appN-ward-product` added. Its step (i) uses (WI1); the appendix draft had flagged this.
- `prop:disall-two-routes`: (GA1), (GA3) and (GA4) added, as the App N target requires.
- `cor:dis-weak-xspace`: premise labels added to `\uses`.
- 21 chapter statements received the appendix lemmas of the App M/N/O proof-delivery tables in their `\uses` (P7).

### 4.4 Over-claims, conservative frontier grades, contradictions between units
- **Contradictory grades for one claim:** `rem:appJ-nonlocal` [A] vs `conj:front-brst-multilocal` [C] vs `asm:appN-brst-nonlocal` [A]. Resolved by MD1 and MD6.
- **`prop:break-jet-veto` [V].** Its statement mixed the model counterexample (Zeng), Gaunt's *argument* and the SYZ cancellation. It is now restricted to the [V] content: the counterexample to *generalized* factorization. The rest stays in words, with status [C], pointing to Ch24 (frontier §F5 item 7; verify stage-1 E36 wording).
- **`prop:jets-ngl-beyond` [P] vs `prop:front-ngl` [A].** Scoped so that the two do not overlap: finite $N_c$ and fixed order on one side, large-$N_c$ NLL on the other.
- **`prop:front-brst-bilocal`:** MD7.
- **`prop:front-commuting`:** fallback corrected to [C].
- **`prop:yzliu-gpd-oneloop`:** re-derivation now mandatory (MD14).
- **Semantic review of every new tagged statement of v2** (core, App M/N/O and frontier; listing in the scratch notes). No other over-claim was found:
  - The [R, R_PT] statements of Ch2 are textbook perturbative results with literature proofs.
  - App M/N/O [R] statements are proofs in this book or implications (R_cond).
  - Frontier fixed-order [R, R_PT] statements are either derived in this book or computed independently by two groups.
  - Frontier [A] statements read only at abstract level are hedged with 「据该文摘要」 (WRITER_SPEC_v2 §6.11 item 2); see §5, item 4.

### 4.5 Missing or thin status paragraphs
`prop:lamet-ad-spacelike`, `conj:yzliu-renormalon-norm`, `conj:yzliu-threshold-hadronic` and `prop:front-regge` now have a 「地位与缺口」 paragraph with weakest step, literature and upgrade path (P21).

### 4.6 Ch25 and the master table
- **Provisional labels.** The core draft used 13 provisional frontier labels that do not exist, such as `thm:lamet-hadronic-matching`, `prop:front-gordan` and `prop:yzliu-gn-convergence`. Block VII was rebuilt from frontier §F3 and the v1 `lattice` rows.
- **Completeness rule** (Ch25: every theorem, conjecture, [V] and [P] statement, and the App M/N/O main theorems). Added rows:
  - II.28 `thm:appM-ope-identity`.
  - II.29 `thm:appM-scaling`.
  - III.38 `thm:appN-structure`.
  - 16 frontier rows for every remaining frontier `thm:`, `conj:` and [V] statement.
- **Broken table rows.** Pipes inside math broke two F3 rows (and two rows of the frontier conventions table); fixed with `\vert` (P38).
- **The rows now live in §09 of FINAL_OUTLINE_v2.** The task asked for "registry and master-table rows" at the end; Ch25 keeps the rules and points to §09.
- **Ch25 text** updated: open-problem labels, OP-A6, OP-A7, OP-A8, OP-B3 and OP-F3/F5/F6, and the incidence matrix (named gap, (Z2), frontier entries).

### 4.7 Registry, labels and format
- **Registry.** The frontier registry lacked its 15 worked examples and registered 7 optional figures as rows (`check_unit_v2.py` C1b would have demanded them). The final registry is generated from the entries for all 43 units, with optional figures and tables listed as notes.
- **Merge markers.** 63 markers ([SYNC-APP], [SYNC-ASM], [SYNC-FRONTIER]) were removed after checking that every flagged label exists with the stated owner and tag.
- **Stale references.** References to the draft files and to the removed frontier sections §F2/§F3 now point into FINAL_OUTLINE_v2.
- **Inner-name clash** (O1): fixed by MD15. `thm:dis-moments-np` now cites 「\cref{asm:intro-np-ope}(O1)」.
- **Users of the global assumptions.** The 「被使用于」 fields of the six `asm:intro-*` entries are regenerated from the final `\uses` data.

---------------------------------------------------------------------------------------------------

## 5. Remaining concerns (ranked) — for the lead author

1. **MD1 needs confirmation** (§3). If the lead author prefers option (b), only one change is needed: add `asm:appN-brst-nonlocal` to the `\uses` of `lem:method-ward-multi`. Every downstream [A] process theorem then becomes [C], and Ch1, Ch25 and the boxes must be re-tagged. The checker flags all affected statements automatically (E6).
2. **Pending verification.**
   - Slots X1a–X1f, X2a–X2d and X3a–X3e. Their scripts and logs exist in `verify/extend/`, but no reports yet.
   - The K1 candidates for 「本书新结果」: N01–N04 and N07–N10.
   - All App Q items. The candidate table has stage-1 notes; stage 2 is pending for every item.
   - N13 (`lem:appO-joint-localization`(b)) is a new proof not found in the literature. If it cannot be written out, it falls back to $N=2$ (see the App O entry).
   - None of these change grades before the patch. The units affected are listed in §6.
3. **Our own new results carry [R] planning tags as implications or explicit computations:**
   - N01 `prop:dy-eikonal-twogluon` [R, R_PT].
   - N03 `cor:front-coleman-norton` [R, R_cond].
   - N07 `prop:lamet-tmc` [R, R_cond].
   - N09 `prop:lamet-tails` [R, R_PT].
   - N08 and N10, which are pure mathematics.

   They are correct only if the verification confirms them. Unlike N04 (MD7), none of them raises the grade of a published result, so the planning tags were kept. If verification fails, the statements must be revised, not just retagged.
4. **Frontier [A] statements read only at abstract level.** These are `prop:lamet-euclid-minkowski`, `prop:front-heavy-fsi`, `prop:front-ggh`, `prop:front-tmd-nlp-operator`, `prop:front-rapidity-renorm`, `prop:front-ngl`(b), `prop:front-jet-substructure`(c), `prop:front-lepton-pdf` and `prop:front-ew-pdf`. They are hedged with 「据该文摘要」, and the writer may not add details. A literature check in the verify patch may downgrade them.
5. **Page pressure.**
   - App P realistically needs 11–13 pp at compaction level 1. Levels 2–3, or +2 pp, are needed.
   - Ch1's overview table `tab:intro-overview` has **96 ★ rows**, roughly 2.5 pp of the 14 pp of Ch1. The lead author may reduce the ★ set; Ch25 keeps all 200 rows.
   - The App A–L rebalance (MD5) needs approval.
6. **Missing bibliography entries, cited as 「文献待补」.**
   - Gribov 1978; Lee–Zinn-Justin 1972; Zinn-Justin 1975; Appelquist–Carazzone 1975.
   - Vladimirov's monograph; Hörmander; Bergère–de Calan–Malbouisson; Bałaban; Magnen–Rivasseau–Sénéor; Schoonderwoerd–Bakker.
   - Chou–Chen, PRD 106 (2022) 014507 (E01); Becher–Hager–Neubert–Schwienbacher, arXiv:2603.12383 = PRL 137 (2026) 121902 (E16); Joglekar 1977; Nakanishi–Ojima 1990.

   They should be added, with verified metadata, by the bibliography step of the verify patch.
7. **REFS_NOTES_v2 §1.4** must be updated after the patch: E02 (the journal version of `Ji:2021znw` is correct) and E16 (the "single group" sentence). I left it unchanged because both items are still pending.
8. **Candidate new VF entries,** to be added only after second confirmations:
   - the two-loop mismatch $\Gamma^{(2)}(\pi/2)-\gamma^{(2)}_{HH}$;
   - Collins' trapped-but-regular one-dimensional integral;
   - the exact $O(\alpha_s)$ difference of `rem:lamet-early-form`.
9. **Master-table bottleneck cells** in some rows are prose ("全阶区域分析", "SCET 前提"), and three rows name assumptions as pointers. App P's C-P14 is a warning and will list them; I accepted this.
10. **Prose-level physics.** The audit is structural and grade-level: labels, dependencies, grades, ownership, budgets, citations and figures. Physics content was reviewed semantically only where a grade or contradiction was at stake (§4.4). The drafts' physics rests on the refdoc analysis, the frontier reports and the verification workflow; the planned physics-review rounds (REQUIREMENTS 3a) remain necessary.
11. **Wording of the global assumptions.** For the global assumptions, the owner's (Ch1) wording now governs. The register's alternative v2.1 wording (for example, the coefficient bound inside `asm:intro-np-ope`) is dropped. The bound appears as a hypothesis of `lem:dis-ope-segment`, so nothing is lost, but the Ch1 and App M writers must keep the two consistent.

---------------------------------------------------------------------------------------------------

## 6. Go/no-go per unit

Status meanings:
- **GO**: may be written now. The pending items are attributions or erratum wordings, handled by `% PENDING-VERIFY` comments.
- **GO-last**: summarizes other units; write at the end.
- **COND**: statements frozen. The parts tied to X1/X2/X3 are written after the verify patch, or before it with the planning tag and comments (WRITER_SPEC_v2 §6.12).
- **NO-GO**: blocked until `verify/` completes.

| unit | writer | status | conditions / notes |
|---|---|---|---|
| front, Ch1 `intro` | W01 | GO-last | after all chapters; ★ rows from §09; 41-entry register table; `def:intro-tags` prints named gaps (MD1) and the global-only R_cond rule (MD4) |
| Ch2 `qcd` | W02 | GO | first wave; E28 sentence (convention remark only), S63-3/4 caveats as comments; VF-QCD-4 general-gauge constants re-derived by the writer |
| Ch3 `prelim` | W03 | GO | first wave |
| Ch4 `ir` | W04 | GO | after Ch2–Ch3; `thm:ir-leading-regions` and `prop:ir-super-leading` name the App N assumptions as pointers only (hidden-forward fix) |
| Ch5 `sudakov` | W05 | GO | `thm:sudakov-factorization` names `asm:appN-collins` as a pointer (S63-12 pending) |
| Ch6 `ee` | W06 | GO | — |
| Ch7 `dis` | W07 | COND (X3) | PT route GO; the App M route (13 statements, premise lists) after X3; E32 sentence as in the entry |
| Ch8 `pdf` | W09 | GO | `prop:pdf-timelike-dglap` [A] (v1 [R] weakened) |
| Ch9 `method` | W10 | COND (X1, X2) | `sec:method-subtraction` with W11's draft after X2; Glauber deformation after X1; named gap in `lem:method-ward-multi`/`thm:method-template` (MD1, confirmation pending) |
| Ch10 `disall` | W12 | COND (X2) | `thm:disall-renorm-compat` content [C]; `prop:disall-h5` re-routed (MD2) |
| Ch11 `coll` | W13 | GO | — |
| Ch12 `dy` | W14 | COND (X1, N01) | DY Glauber sections with W15's drafts after X1; `prop:dy-eikonal-twogluon` without novelty wording until N01 passes |
| Ch13 `thr` | W16 | GO | — |
| Ch14 `tmd` | W17 | COND (X1, X2) | `lem:tmd-glauber`, `prop:tmd-zero-bin-soft`(b) after the patch; E17 silently correct |
| Ch15 `scet` | W18 | GO | E24/E25 as comments |
| Ch16 `jets` | W19 | GO | `prop:jets-ngl-beyond` scoped; E28 convention remark |
| Ch17 `smallx` | W20 | GO | — |
| Ch18 `break` | W21 | COND (X1) | `prop:break-measurement` after X1; `prop:break-jet-veto` restricted (E36 wording) |
| Ch19 `excl` | W22 | COND (X2) | `prop:excl-soft-cancel` premises completed; E22 sentence dropped |
| Ch20 `heavy` | W23 | GO | E26 as a comment |
| Ch21 `power` | W24 | GO | `thm:power-ope-convergence` stays [R, R_PT] (MD8) |
| Ch22 `lamet` | W25 | GO | owns the quasi-TMD theorem and the lattice CS kernel (MD9); K1 items N07–N10 without novelty wording; E01/E02/E03 printed in correct form silently |
| Ch23 `yzliu` | W26 | GO | `prop:yzliu-gpd-oneloop` needs a re-derivation (MD14); A03 novelty wordings pending |
| Ch24 `front` | W27 | GO | `prop:front-brst-bilocal` planning [A] (MD7); `prop:front-commuting` fallback [C]; N02/N03 without novelty wording |
| Ch25 `summary` | W28 | GO-last | after the verify patch; rows from §09 (200) |
| App A, C, E, I, L | W03, W06, W04, W03, W09 | GO | App L: `prop:appL-renormalized` must not presuppose the non-local classification (N04 circularity check) |
| App B | W05 | GO | E23 (Becher–Schwartz $\Gamma_1$) as a comment |
| App D | W04 | GO | A08 (Collins 2020 preprint), N02 pointer |
| App F | W10 | GO | `prop:appF-induction` names the named gap (cycle removed) |
| App G, App H | W29 | GO | after drafts of Ch6–Ch14 (App G details) |
| App J | W02 | GO | `rem:appJ-nonlocal` untagged (MD6); `lem:appJ-cut-hermiticity` (S63-8, X1) with a comment |
| App K | W09 | GO | `lem:appK-entire`, `lem:appK-markov` used by App M (X3 does not change them) |
| App M | W08 | COND (X3) | §M.1–§M.4, §M.6, §M.8 now; slots X3a–X3e after the patch |
| App N | W11 | COND (X2) | start first (critical path); slots X2a–X2d after the patch; `thm:appN-structure` content [C] (MD1) |
| App O | W15 | COND (X1) | owns `lem:appO-orientation`; `lem:appO-past-unitarity` removed (MD10); slots X1a–X1f and N13 after the patch |
| App P | W28 + integrator | GO-last | generated at integration (`blueprint_gen.py` per §P.7, plus C-P17); introduction written last; `longtable` in the master driver |
| App Q | W30 | **NO-GO** | until `verify/` completes (two independent confirmations per item) |

---------------------------------------------------------------------------------------------------

## 7. Reproducibility

- **Checker.** `python3 -I spec_v2/checks/check_final_outline_v2.py spec_v2` runs the checks E1–E14, W1 and W2 on FINAL_OUTLINE_v2 against FIGURES_INDEX_v2, `refs_merged_v2.bib` and the register table. It uses the Python standard library only. Exit code 0 means pass. Log: `checks/check_final_outline_v2.log`.
- **Patches to come.** The verify patch and later edits should be applied to `FINAL_OUTLINE_v2.md` directly, followed by a re-run of the checker.
- **Assembly.** It was scripted: label-addressed patches over the drafts plus generated registry and master rows. The scripts are in the integrator's scratch area and are not needed for future work, because the drafts are superseded.
- **Unit check.** `checks/check_unit_v2.py` reads §08 of FINAL_OUTLINE_v2 unchanged (tested).
