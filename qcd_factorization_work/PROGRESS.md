# Progress log — QCD factorization monograph (for continuity across sessions / quota resets)

## Done
- Phase 1 research (`research/`): architect BLUEPRINT.md, critic REVIEW.md, survey SURVEY.md, refs (refs.bib, NOTES.md),
  computations c_pdf, c_dis, c_dy, c_ee, c_regions, c_wilson, c_tmd, c_glauber, c_exclusive, c_scet (DERIVATION.md each),
  TikZ sets tikz1 (12 figs), tikz2 (16), tikz3 (16) — figures files `research/tikz*/figures*.tex`.
- Spec v1 (`spec/`): FINAL_OUTLINE.md (22 ch + App A–L, 346 statements), WRITER_SPEC.md, FIGURES_INDEX.md,
  VERIFIED_FORMULAS.md (178), refs_merged.bib (646), REFS_NOTES.md, key_aliases.tsv; audited (GO Ch2–20, App A–L).
- Reference document deep reading (`refdoc/`): notes R1–R8.md (all 238 pp), REFDOC_ANALYSIS.md (63 errors in the
  reference, 8 in our spec, spec changes S1–S63, proposed App M/N/O/P).
- Frontier research (`frontier/`): lamet/LAMET.md (+lamet.bib), yzliu/YZLIU.md (+yzliu.bib), others/OTHERS.md (+others.bib).
- Common files (`common/`): preamble_fact.tex (ctexbook; theorem/assumption/conjecture envs; rigor tags; \uses;
  TikZ styles incl. enlarged Wilson arrows), fd_styles.tex, fd_styles_ext.tex.

## Done (2026-10-10, evening)
- Spec v2 (`spec_v2/`): FINAL_OUTLINE_v2.md (8031 lines; 847 statements in 39 units; 41 assumptions; 200 master rows;
  236 [PENDING-VERIFY]), WRITER_SPEC_v2.md (v2.2), ASSUMPTIONS.md, FIGURES_INDEX_v2.md (113 required + 25 optional),
  VERIFIED_FORMULAS_v2.md, refs_merged_v2.bib (1003), AUDIT_v2.md. Lead decisions: accept MD1 (asm:appN-brst-nonlocal
  = [C] named gap), MD2–MD18, App P ≈ 12 pp, MD5 rebalance; reduce Ch1 starred overview rows to the main results.

## Done (2026-10-11)
- Figures (`figures/`): figset_A–F (132 labels; 113/120 required, 7 App P graphs generated at integration), FIGURES_STATUS.md, FIGCHECK.md.
- Verification (`verify/`): CLAIM_VERDICTS.md (137 claims; errata 33 confirmed/2 refuted/1 disputed; new results 25/3/1 unresolved;
  refdoc corrections 42/2; attributions 25/3). Extensions X1–X3: 3 review rounds + final repair + final review
  (`verify/extend_reports/X*_final.md`, `X*-finalreview.md`, all rounds persisted).
- Spec v2.3.1 (verify patch + audit, `spec_v2/AUDIT_v2_patch.md`: GO for all units). Only 「本书新结果」: prop:appN-triangle-cs(a).
- Lead decisions `writing/LEAD_DECISIONS.md` (LA-1…LA-16). Writer context packs `writing/packs/Wnn/` (tools/build_packs.py).

## Running (2026-10-14) — writing phase, script factorization-writing (args.group)
- 2026-10-11 runs failed at once (weekly limit of the previous account; nothing written). Relaunched 2026-10-14 with
  failure guards (a failed stage stops its chain; resume re-runs only failed stages):
- group A run wf_1b1b7a35-b6e (task wyx5f2k01): W02 W03 W04 W05 W06 W09 W13 W16 W22 W30
- group B run wf_3924630b-621 (task w2j2a421q): pre-writing (X1–X3 final2 + independent confirm2 + spec v2.4 sync
  + figure sync), then W10 W07 W14 W12 W17 W21 (reviews gated on the sync), W11 W15 W08 (start after the sync)
- group C run wf_2e53ffea-c6f (task wkul57h1j): W25 W27 W26 W24 W18 W23 W19 W20
- group R run wf_e30388b7-c05 (task wu749v5mo): W02 W07 W27 re-run (interrupted 14:05 EDT by an un-retried rate-limit error;
  the re-run continues from their partial drafts/scripts in writing/work/Wnn/). In A/B/C these three chains stopped at 'write'.
- 2026-10-14 evening — proof completion (REQUIREMENTS 6):
  - deep research X4 (non-abelian multiple Glauber insertions, collinear + TMD DY): run wf_6971bc3e-f8c (task wn70exalx),
    script factorization-deep-research (args.topics) → verify/research/X4-nonabelian-glauber/
  - proof completion: inventory proofs/INVENTORY.{json,md} (320 items: 185 [A], 48 [P], 45 [C], 23 [V], 19 [R]-sketch;
    tools/proof_inventory.py); triage + prove + 2 verifiers + repair: runs wf_7c986a86-ad7 (T1–T5, task w1uiqtj13) and
    wf_f2b311b2-bad (T6–T10, task wro2n4ik6), script factorization-proof-completion (args.groups) → proofs/
- integration-tooling agent (background): writing/tools/{blueprint_gen,figsync,bibmerge,make_master,check_book}.py, build/build.sh
- per unit: write → review 1 → revise 1 → review 2 → revise 2 (if issues). Output in chapters/, tests writing/test/.
- Resume after interruption: Workflow({scriptPath: <session>/workflows/scripts/factorization-writing-wf_55541c51-5f2.js,
  args: {group}, resumeFromRunId: <run>}).

## PAUSED (2026-10-14 ≈22:00 EDT, user request) — see writing/state/RESUME.md
- All 7 workflow runs and the tooling agent were stopped deliberately; nothing lost. Done before the pause: W03, W06, W10,
  W12, W14, W26 writers; X1/X3 final2. In flight (resume with the RESUMPTION NOTE): all other writers, X2 final2,
  X1/X3 confirm2, X4 survey, triage T1–T10. Scripts patched for resume (args.resume/done/skip); exact args in
  writing/state/args_*.json; state in writing/state/RUN_STATE_20261014.json; persisted results in writing/state/results/.

- Draft PDF for the user (2026-10-14 22:12): snapshot build/snapshot_draft_20261014 → build/draft_20261014/ (462 pp,
  0 LaTeX errors, 0 undefined citations, 215 expected undefined refs to unwritten units, App P 35 pp at level 3) copied to
  ../qcd_factorization_draft_20261014.pdf. Rebuild a draft any time: copy chapters/ to a snapshot dir, then
  bash build/build.sh --chapters <snapshot> --builddir <dir>  (≈4 min; chapters/ is never modified).

## Next
1. Group D: W29 (App G/H), W28 (Ch25 + App P intro), W01 (front + Ch1) — after A/B/C drafts exist.
2. Integration → `build/`: master driver, figure re-sync, generated App P (from \uses), merged bib (+ .bib-additions), compile.
3. Global review rounds (cross-unit consistency, conventions, grades, physics by part) + fixes; final visual check.
4. Deliver `qcd_factorization.tex/.pdf` to the project root.
