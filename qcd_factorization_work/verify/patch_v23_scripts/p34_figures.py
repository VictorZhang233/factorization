import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import src
TARGET = 'FIGURES_INDEX_v2.md'
F = lambda n: src.ln(n, 'FIGURES_INDEX_v2.md')

RULE9 = r'''9. **Captions and `verify/` claims (spec v2.1; final in v2.3).** A caption never contains a planning marker (the retired pending-verification marker, 「待文献核查」), a novelty claim (「本书新结果」「首次」) or an erratum statement about a paper; captions state the physics with the published source or the VF ID. The following figures touch claims of `verify/CLAIMS.md` (classes of WRITER_SPEC_v2 §6.5, §6.13) or the proof extensions X1–X3. The verify patch v2.3 has been applied: their owners **must re-check the caption** against the final outcome given in the last column (FINAL_OUTLINE_v2 §0.10, §00.4); generated figures that depend on the changed `\uses` data or master rows are regenerated (§5 note).'''

ROWS = r'''   | figure | claim | final outcome to check (v2.3) |
   |---|---|---|
   | `fig:dy-two-gluon-exchange` | N01 | confirmed but known (`Meggiolaro:1996hf`, `Giordano:2006vv`): no novelty wording anywhere; the caption may cite these sources |
   | `fig:appO-deformation`, `fig:appO-flowchart`, `fig:appO-cutsum`, `fig:appO-lcopt-term`, `fig:method-glauber-direction`, `fig:dy-pole-orientation`, `fig:break-measurement`; optional `fig:appO-windows`, `fig:appO-glauber-flow` | X1 | final App O statements: window-edge terms vanish with side-independent windows (`lem:appO-side-independent-windows`); `asm:appO-mixing` has clause (a′); the model theorems of §O.5 ([P]) and their assumptions `asm:appO-adjacent-swap`, `asm:appO-real-jets`, `asm:appO-collinear-ends` are side boxes of `fig:appO-flowchart`, never premises of `thm:appO-main`; ordering weights continuous with a kink |
   | `fig:method-hasse`, `fig:method-neighbourhoods`, `fig:method-sudakov-plane`, `fig:appN-triangle-regions`, `fig:appN-triangle-remainder` | X2; N12 | final App N statements: (CS1)–(CS3) for the triangle proved in the fibered norm (`prop:appN-triangle-cs`); the remainder is a sharpened explicit result, never "new" (the only novelty marker of the book, `prop:appN-triangle-cs`(a), is printed in the text, never in a caption) |
   | `fig:appM-dependency`, `fig:appM-forest`, `fig:appM-handbag-ab`, `fig:appM-euclid-forward`, `fig:dis-euclid-segment` | X3 | final App M statements: `asm:appM-brst-ope` is (Eε) ((B1) retired); new nodes `lem:appM-ne`, `thm:appM-brst-reduction`, `thm:appM-forward-expansion`, `cor:appM-forward-ope`, `asm:appM-oswi`; `asm:appM-remainder` feeds `thm:appM-scaling`, not `prop:dis-ope-euclid` |
   | `fig:front-gordan` | N02, A08 | N02 confirmed, no novelty claim; `Collins:2020euz` is a preprint |
   | `fig:lamet-hybrid` | E01 | confirmed: the caption gives $\int C_{\rm hyb}=1$ without commenting on the printed form (App Q row Q.8) |
   | `fig:yzliu-leading-region`, `fig:yzliu-soft-hqet` | E02, A03, A04 | E02 confirmed (correct CS exponent); priority words only in the text and only with 「据我们所知」 (A03); A04 corrections applied |
   | `fig:yzliu-complex-lorentz` | E13 | confirmed: the map is $\Lambda(t,z)=(iz,it)$; "edge of the wedge" is not used for the BHW step |
   | `fig:yzliu-threshold` | N06, A26 | confirmed: a check of the published factorization; two-loop agreement as "consistent with" (fitted constants) |
   | `fig:lamet-oneloop` | N05, N09 | N05 confirmed (cite `IzubuchiEtAl2018` App. B); no statement on the convolution domain beyond `prop:lamet-tails` as corrected (N09 refuted as stated) |
   | `fig:lamet-fourier` (optional) | N10 | confirmed, known in substance (also `Monahan:2026skv`): no novelty wording; the mode count cites `SlepianPollak1961`, `LandauWidom1980` |
   | `fig:front-yukawa-pdf` | E35 | confirmed: `CollinsRogersSato2022` model, $f<0$ for $\xi\in(0.264,1)$ at $\mu=0.8$ GeV, positive for all $\xi$ iff $\mu\ge1.699$ GeV; the dispute stays in the text |
   | `fig:jets-sw-cone` | E28 | confirmed as a convention remark: $\epsilon$ is the fraction of the total energy $\sqrt s$ |
   | `fig:excl-endpoint` (optional) | N21 | confirmed; novelty of the closed forms not asserted; cite the soft-region argument to `IsgurLlewellynSmith1984` |'''

S12_OLD = '`asm:appM-remainder`, `asm:appM-brst-ope`, `asm:appM-forward` (orange dashed boxes, top row); statements `prop:dis-dispersion-np`'
S12_NEW = '`asm:appM-remainder`, `asm:appM-brst-ope` ((Eε)), `asm:appM-forward`, `asm:appM-oswi` (orange dashed boxes, top row); statements `prop:dis-dispersion-np`'
S12_ADD_OLD = '`prop:dis-ope-forward`, `thm:dis-moments` (tag-coloured boxes, middle and bottom rows); edges from the `\\uses` lists; R_cond edges dashed.'
S12_ADD_NEW = '`prop:dis-ope-forward`, `thm:dis-moments` (tag-coloured boxes, middle and bottom rows), and (v2.3) the App M statements `lem:appM-ne`, `thm:appM-brst-reduction`, `thm:appM-forward-expansion`, `cor:appM-forward-ope`, `thm:appM-scaling`; edges from the `\\uses` lists (in v2.3 `asm:appM-remainder` feeds `thm:appM-scaling` only); R_cond edges dashed.'

S14_OLD = 'as dashed orange boxes attached to the steps that use them; the lemmas proved without assumptions as green tags.'
S14_NEW = 'as dashed orange boxes attached to the steps that use them; the lemmas proved without assumptions as green tags (v2.3: `lem:appO-side-independent-windows` at (O-3), [R, R_cond]); (v2.3) a separate box "§O.5 model theorems ([P])" with the side boxes `asm:appO-adjacent-swap`, `asm:appO-real-jets` (\\tagP) and `asm:appO-collinear-ends` (\\tagA), connected to (O-3) by a dotted line only (evidence, not a premise of `thm:appO-main`).'

OPS = [
 ('rep', F(27) + '\n', RULE9 + '\n'),
 ('range', '   | figure | claim | what to check after the patch |\n', '\n**Counts (v2).**', ROWS + '\n', False),
 ('sub', '*(Pending: CLAIMS N01 — no novelty wording in the caption; rule 9.)*', '*(v2.3: claim N01 confirmed but known — no novelty wording; the caption may cite `Meggiolaro:1996hf`, `Giordano:2006vv`; rule 9.)*', '*(Pending: CLAIMS N01'),
 ('sub', S12_OLD, S12_NEW, '- **Draw:** nodes: `asm:intro-wightman`, `asm:intro-composite`, `asm:intro-np-ope`'),
 ('sub', S12_ADD_OLD, S12_ADD_NEW, '- **Draw:** nodes: `asm:intro-wightman`, `asm:intro-composite`, `asm:intro-np-ope`'),
 ('sub', S14_OLD, S14_NEW, '- **Draw:** eight boxes (O-1) regions, domain and windows;'),
 ('sub', '*(Pending: X1 — the owner re-checks the caption against the final App O statements; rule 9.)*', '*(v2.3: X1 applied — the statements cited in the caption are unchanged; the owner re-checks the caption against the final App O statements, rule 9.)*', '*(Pending: X1 — the owner re-checks'),
 ('rep', '4. Counts: 120 required, 26 optional (§0 table, §5). Every chapter still owns ≥ 2 required figures, every big appendix ≥ 1. No caption draft was changed.',
  '4. Counts: 120 required, 26 optional (§0 table, §5). Every chapter still owns ≥ 2 required figures, every big appendix ≥ 1. No caption draft was changed.' + r'''

**2026-10-11 — v2.3 (spec patcher; verify patch).**
1. Rule 9 final: the table now gives the outcome of every claim and slot (N01, N02, N05, N06, N09, N10, N12, N21, E01, E02, E13, E28, E35, A03, A04, A08, A26; X1–X3); `fig:break-measurement`, `fig:appM-handbag-ab` and the optional App O figures added to the re-check list.
2. S12 `fig:appM-dependency`: nodes `asm:appM-oswi`, `lem:appM-ne`, `thm:appM-brst-reduction`, `thm:appM-forward-expansion`, `cor:appM-forward-ope`, `thm:appM-scaling`; S14 `fig:appO-flowchart`: model-theorem box with side boxes (not premises of `thm:appO-main`); the pending notes of two caption drafts replaced by outcomes. No caption text and no count changed.
3. Generated figures to regenerate from the v2.3 outline (changed `\uses` data, register and master rows): `fig:intro-dependency`, `fig:summary-status-map`, `fig:summary-hypotheses`, `fig:appP-dependency` and `fig:appP-dependency-b` … `-h`, `fig:appM-dependency`, `fig:appO-flowchart`, optional `fig:lamet-dependency`.'''),
]
