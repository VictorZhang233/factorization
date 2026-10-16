# LEAD_DECISIONS — lead-author decisions for the writing phase (binding; rank 1 in the order of authority)

Date: 2026-10-11. Spec state: v2.3.1 (verify patch + audit, `spec_v2/AUDIT_v2_patch.md`: GO for all units).
These decisions answer the open items of `AUDIT_v2_patch.md` §6 and fix the coordination of the writing phase.
Where a decision changes a spec rule, it overrides `WRITER_SPEC_v2.md` / `FINAL_OUTLINE_v2.md`.

## LA-1 — MD1 confirmed
`asm:appN-brst-nonlocal` is `\tagC` and a **named gap** exactly as in WRITER_SPEC_v2 §4.6 item 6 (premise only of
`thm:appN-structure`; named, never `\uses`d, by `lem:method-ward-multi`, `thm:method-template`, `prop:appF-induction`,
`thm:disall-factorization`, `thm:dy-factorization`). Reason: no all-order argument for the multilocal BRST
classification exists in the literature; Collins 2011 §11.3.2 assumes it.

## LA-2 — MD19 confirmed
1. The six new assumptions and their tags are confirmed: `asm:appM-oswi`, `asm:appN-lce`, `asm:appN-analytic-reg`,
   `asm:appO-collinear-ends` (`\tagA`); `asm:appO-adjacent-swap`, `asm:appO-real-jets` (`\tagP`).
   `asm:appO-collinear-ends` is **not** a premise of `thm:appO-main` or `thm:dy-factorization` (these keep
   `asm:appO-mixing`(c), `\tagA`); it is used only by the statements that list it in the outline.
2. **App O model theorems are [P]** (WRITER_SPEC_v2 §4.3 item 4, row "[R] (model)"): each is printed as a QCD-relevant
   statement whose first sentence names the model (e.g. 「在标量旁观者模型 $M_{\rm glob}$ 中、$O(g^4)$ 阶，……」), followed by a
   **complete `proof` of the model-internal claim** (WRITER_SPEC_v2 §4.10 item 5). Lemmas that are pure mathematics
   about abstract classes carry no tag (「数学」), as the X1 final review requires (L2, L5, L6, L8; `lem:appO-equal-time`,
   `lem:appO-cut-position`, `lem:appO-carrier`).
3. The novelty marker 「本书新结果」 on `prop:appN-triangle-cs`(a) is confirmed (two independent confirmations + literature
   check are recorded), subject to LA-3 not refuting it.
4. `lem:appO-side-independent-windows` (slot X1c) at [R, R_cond] instead of the planned [R, R_PT] is confirmed
   (a weakening is always allowed).

## LA-3 — B.3 policy: obtain a genuine second confirmation
Neither option of `AUDIT_v2_patch.md` §6 item 3 is taken as it stands. A pre-writing confirmation stage re-derives,
independently and by a different method, X2 Prop B.3 (fibered = covariant for Γ of the triangle), Prop C.4(e1),(e3),
`prop:appN-phi36-dis`(c) and `prop:appN-twoloop-remainder`(ii),(iv), after the final-review fixes are applied
(`verify/extend_reports/X2-subtraction_final2.md`).
- Confirmed → printed without premise; B.3 and C.4(e1) are printed as 「本书给出的推导」 of instances of the known
  light-front/LCPT–covariant equivalence for scalar graphs (`LigterinkBakker1995`-type references, Chang–Yan 1973),
  never as new results.
- Not confirmed → printed as R_cond implications with the premise named ((ID)$_\Gamma$ or the item's own premise).
The outcome is recorded in `FINAL_OUTLINE_v2.md` (CHANGELOG v2.4) before the App N writer starts.

## LA-4 — `prop:appM-zero-momentum-insertion`
The confirmation stage writes out the identification of BM II's $\varepsilon$ with the damping regulator in the
Breitenlohner–Maison framework (X3 final review, fix 1) and checks it independently. Confirmed → the lead author
upgrades the outline tag to [R, R_PT] (recorded in CHANGELOG v2.4); otherwise it stays [A] with the status note.

## LA-5 — X1 exponents
Only the final-review refit values are printed: decay exponents $\varepsilon^{0.63}$, $\varepsilon^{0.70}$,
$\varepsilon^{0.73}$ for the three non-factorized jet pairs, first-decade Im slopes 0.680–0.717 (source:
`verify/extend/X1-glauber/review_r3_1_logs/t2_general.log`, re-fit in the final review). The report values
0.7–0.77 are not printed.

## LA-6 — App Q numbering
App Q rows are numbered in a column 「条目」 as 1, 2, …, 21 (the row order of the spec). Wherever the spec says
"App Q, row Q.$n$", the text prints 「附录~Q 第~$n$~条」 (same $n$). The App Q sections keep their numbers.

## LA-7 — Locations marked 「位置待核实」 and unverified notes
Planning markers are never printed. A writer who meets 「位置待核实」 (or "not re-read"/"not verified") tries to verify
the location in the full text (arXiv/INSPIRE via WebFetch). Verified → print the location. Not verifiable → cite
without a location (and, if the claim itself is unverified, hedge the claim or drop it). Report every case.

## LA-8 — Page budgets
Completeness wins over length. The −15 % lower tolerance stays. Upper tolerance:
- proof appendices App M, App N: up to +30 %; App O: up to 42 pp;
- chapters and other appendices: up to +20 % when needed for complete proofs, full derivations or worked examples.
Report the page count. Never shorten statements, proofs of [R]/R_cond statements, `\uses`, status paragraphs, boxes.

## LA-9 — Coordination override of WRITER_SPEC_v2 §12.1 items 3–4 and §12.3
To remove inter-writer waiting:
- W10 writes Ch9 `sec:method-subtraction` **itself**, from FINAL_OUTLINE_v2 (Ch9 and App N entries) and
  `verify/extend_reports/X2-subtraction_final2.md` (or `_final.md` + its final review if final2 is not yet there).
- W14 writes Ch12 `sec:dy-glauber`, `sec:dy-model`, `sec:dy-theorem` **itself**, from FINAL_OUTLINE_v2 (Ch12 and App O
  entries) and the X1 final reports.
- W07 and W08 do not exchange drafts: the 13 proof-delivery targets are fixed by FINAL_OUTLINE_v2 (Ch7 states and
  points to App M; App M proves).
Consistency between chapter and appendix (Ch7↔App M, Ch9/Ch10↔App N, Ch12/Ch14↔App O) is checked in the cross-unit review.

## LA-10 — Figures
Writers copy each figure block they own **verbatim** from `writing/packs/Wnn/figblocks.tex` (identical to the figure
sources listed in `figures/FIGURES_STATUS.md`; existing figures from `research/tikz*/figures*.tex`). Writers never edit a
figure block; a wrong figure is reported (with the proposed fix). At integration every block is re-synchronized from the
figure sources, so caption fixes made later propagate. Generated figures (`fig:intro-dependency`, `fig:summary-*`,
`fig:appP-dependency*`, `fig:appM-dependency`, `fig:appO-flowchart`, optional `fig:lamet-dependency`) are regenerated
from the final spec by the figure-sync step; their owners copy the current block and the integrator re-syncs.
Optional figures that were not drawn (`fig:pdf-gluon-operator`, `fig:pdf-ff-cut`, `fig:tmd-evolution`, `fig:scet-modes`,
`fig:break-spacelike`, `fig:excl-erbl`, `fig:excl-endpoint`) are simply omitted (no placeholder), unless the writer
draws them to the standard of FIGURES_INDEX_v2 (then: report, block delimiters, own test render).

## LA-11 — `prop:lamet-tails`(iii)
The Ch22 writer re-derives it in full (script kept); the Ch22 reviewer checks it independently (second record).

## LA-12 — Proof appendices use the final2 reports
App M, App N, App O are written from `verify/extend_reports/X3-ope_final2.md`, `X2-subtraction_final2.md`,
`X1-glauber_final2.md` (final reports with the final-review fixes applied and independently confirmed where required),
together with the spec entries as updated in CHANGELOG v2.4.

## LA-13 — Spec files are read-only for writers
Writers and reviewers never edit `spec_v2/`, `research/`, `frontier/`, `refdoc/`, `verify/`, `common/`, `figures/`.
Deviations from the spec are made only where the spec is wrong, are minimal, and are reported (WRITER_SPEC_v2 §13 item 13).

## LA-14 — Missing references
WRITER_SPEC_v2 §9 item 3 is replaced: a writer who needs a reference that is not in `refs_merged_v2.bib` verifies it on
INSPIRE/arXiv/Crossref, writes a complete BibTeX entry (INSPIRE texkey as key, DOI/eprint fields) into
`chapters/<file-stem>.bib-additions`, cites it normally, and lists it in the report. The integrator merges the additions.
Unverifiable references are not cited (the claim is hedged or dropped). 「文献待补」 is never printed.

## LA-15 — Language and quality bar
Chinese prose of monograph quality (as in `/Users/hao-cheng/Desktop/theorem proof/furry_qcd.tex`): every derivation step
written out, every symbol defined at first use, motivation before formalism, a worked example for every main idea, honest
status. Physics correctness is the first priority: every formula that is not copied from VERIFIED_FORMULAS_v2 is
re-derived (python/sympy/numpy scripts kept under `writing/work/<writer>/`), every sign and factor checked.

## LA-16 — Work locations
- Unit files: `chapters/<file>.tex` (the file names of WRITER_SPEC_v2 §1.1).
- Test builds: `writing/test/<writer>/` (writers), `writing/test/<writer>_r<k>/` (reviewers).
- Scripts: `writing/work/<writer>/`, reviewers `writing/work/review/<unit>/`.
- Reports: `writing/reports/<writer>_report.md`, revisions `writing/reports/<writer>_revision<k>.md`; reviews
  `writing/reviews/<writer>_r<k>.md`.
- Nothing is committed to git.
