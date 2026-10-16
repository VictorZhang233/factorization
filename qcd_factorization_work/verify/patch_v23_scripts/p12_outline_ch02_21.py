import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import src
ln = src.ln
TARGET = 'FINAL_OUTLINE_v2.md'

V9 = r'''**Verification (v2.3).** App N statements and `ex:method-sudakov-subtraction`: slot X2a delivered (`prop:appN-triangle-cs`; claim N12 confirmed; S63-12 resolved — Collins 2011 ch. 10 gives scaling statements, integral-norm bounds only for the triangle), X2b, X2c not delivered (fallback in force: `thm:appN-subtraction` stays [R, R_cond]), X2d open; App O statements: X1 outcomes as in §00.4 (no tag of this chapter changes); `lem:method-gy`: E27 confirmed (Collins 2011 eqs. (11.4)–(11.6) used with the author's errata list); `lem:method-ward-multi`: N04 pointer with the prior art `Braun:2019qtp`.'''
V10 = r'''**Verification (v2.3).** App N statements and `ex:disall-ladder`: slot outcomes of §00.4 (X2a delivered, X2b, X2c not delivered, X2d open); no tag of this chapter changes.'''
V12 = r'''**Verification (v2.3).** X1 (App O route, `tab:dy-status`, orientation lemma, future-vs-past identity, deformation plan): outcomes of §00.4, no tag of this chapter changes; N01 confirmed as a known result (`prop:dy-eikonal-twogluon` printed without marker, citing `Meggiolaro:1996hf`, `Giordano:2006vv`); S63-5 = N01; N25 confirmed (model attribution, novelty not claimed); E31 confirmed (quotation only); A11 items (1), (2), (4), (5) and the RS equation numbers verified (S63-9), item (3) corrected (RS treat the $n$–$\bar n$ production current at one and two loops; no all-order proof).'''
V14 = r'''**Verification (v2.3).** X2: `prop:tmd-zero-bin-soft`(b), `lem:tmd-sqrt-identity`(b) keep their tags; X1: `lem:tmd-glauber` keeps [A] (the App O model results for coincident patterns are [C] for TMD, `rem:appO-literature-comparison`); E17 confirmed (App Q, row Q.2); N20 confirmed (no marker; mechanism attributed); S63-6 confirmed (`Collins:2016hqq`); S63-7: $p=2$ (`Scimemi:2016ffw`, `Moos:2020wvd`); S63-9: Collins 2011 locations verified.'''
V15 = r'''**Verification (v2.3).** E24 confirmed (convention hazard, kept in the statement, not an App Q row); E25 confirmed (App Q, row Q.3); E23 via `def:sudakov-cusp` (App Q, row Q.1).'''
V16 = r'''**Verification (v2.3).** E28 confirmed as a convention remark (no App Q row; the $\ln2\epsilon$ form with total-energy $\epsilon$ is Sterman–Weinberg's own result); E16 confirmed, now by two groups (`Banfi:2025mra`, `Becher:2026kbr`); S63-10 resolved (`Becher:2024kmk`: restoration evidence, "does not amount to a proof").'''
V18 = r'''**Verification (v2.3).** X1: `prop:break-measurement` and the failure locations keep their tags; N16 (our proof of a statement of `Collins2007`), N17 (attachment-sum form of `RogersMulders2010` eq. (34)), N18 (compact form of known channel values) confirmed, all printed as our derivations of known results; E18 confirmed (App Q, row Q.4); E36 wording as in `prop:break-jet-veto`; S63-10 resolved (`Becher:2024kmk`).'''
V19 = r'''**Verification (v2.3).** X2: `prop:excl-soft-cancel` keeps its tag; N21 confirmed (closed forms are our evaluation of the Isgur–Llewellyn Smith fraction function; novelty not asserted); E20, E21 confirmed (App Q, rows Q.5, Q.6); E22 refuted (dropped; nothing printed); E12 confirmed as an author correction (cite `Guo:2023pqw`).'''
V20 = r'''**Verification (v2.3).** E26 confirmed (App Q, row Q.7); N22 refuted (no illustration of our own is printed; the model dependence is stated by `BenekeEtAl2001`, `BenekeNeubert2003`); S63-11: Chay–Kim (`Chay:2003ju`) confirmed.'''
V21 = r'''**Verification (v2.3).** S63-11: `Beneke:1998eq` (the large-$N$ σ-model statement) confirmed; `Feldman:1986ax`, `Gawedzki:1985ez` and `Bostelmann:2005rr` were not re-read (contents hedged in the text); N12 confirmed (pointer in `rem:power-np-status`).'''

OPS = [
 # ---------------- Ch2: bibliography gaps (task item f)
 ('sub', '「（文献待补：Gribov 1978, Nucl. Phys. B 139, 1）」', '`Gribov:1977wm`', '(Gribov copies; '),
 ('sub', '「（文献待补：J. Zinn-Justin 1975, Lect. Notes Phys. 37）」', '(`Zinn-Justin:1974ggz`)', 'the Zinn-Justin equation 「'),
 ('sub', 'Lee–Zinn-Justin 1972 「（文献待补）」', 'Lee–Zinn-Justin (`Lee:1972fj`, `Lee:1972ocr`, `Lee:1972yfa`)', 'Lee–Zinn-Justin 1972 「（文献待补）」'),
 ('sub', '(Appelquist–Carazzone 「（文献待补：T. Appelquist, J. Carazzone 1975, Phys. Rev. D 11, 2856）」)', '(Appelquist–Carazzone, `Appelquist:1974tg`)', 'Appelquist–Carazzone 「'),
 ('sub', 'Missing from the bib (cite as 「文献待补」 only if needed): Gribov 1978; Lee–Zinn-Justin 1972; Zinn-Justin 1975; Appelquist–Carazzone 1975.',
  'Added in spec v2.3 (INSPIRE-verified): `Gribov:1977wm`, `Lee:1972fj`, `Lee:1972ocr`, `Lee:1972yfa`, `Zinn-Justin:1974ggz`, `Appelquist:1974tg`.',
  'Missing from the bib (cite as 「文献待补」 only if needed)'),
 # ---------------- Ch9
 ('sub', ' [PENDING-VERIFY: X2]', '', '* **引理 `lem:method-i0-compat` —'),
 ('sub', ' [PENDING-VERIFY: X2]', '', '* **引理 `lem:method-local-accuracy` —'),
 ('sub', '(Collins 2011 eqs. (11.4)–(11.6) with the errata [PENDING-VERIFY: E27])',
  '(Collins 2011 eqs. (11.4)–(11.6), used with the author\'s errata list, version of 22 May 2026, §3: upper and lower indices interchanged, $K_{\\mu\\nu}=k_\\mu w_{2\\nu}/(k\\cdot w_2-i0)$ with $k$ flowing into $H$ — the future-pointing (DIS) prescription)',
  'Collins 2011 eqs. (11.4)–(11.6) with the errata [PENDING-VERIFY: E27]'),
 ('sub', 'moment reduction of the bilocal classification problem: Ch24 (pointer) [PENDING-VERIFY: N04]',
  'moment reduction of the bilocal classification problem: Ch24 (pointer; [A]; prior art `Braun:2019qtp` eqs. (2.4), (2.6), (3.1), (3.2))',
  'moment reduction of the bilocal classification problem: Ch24 (pointer) [PENDING-VERIFY: N04]'),
 ('sub', ' [PENDING-VERIFY: X2]', '', '* **例 `ex:method-naive-induction` —'),
 ('sub', ' [PENDING-VERIFY: X2]', '', '* **推论 `cor:method-removing-eps` —'),
 ('sub', '[PENDING-VERIFY: X2, N12]', '(claim N12 verified; complete (CS1)–(CS3) check of this example: `prop:appN-triangle-cs`)', '* **例 `ex:method-sudakov-subtraction` —'),
 ('sub', ' [PENDING-VERIFY: X1]', '', '* **命题 `prop:method-fsi` —'),
 ('sub', ' [PENDING-VERIFY: X1]', '', '* **命题 `prop:method-glauber-deformation` —'),
 ('rep', ln(1901) + '\n', V9 + '\n'),
 # ---------------- Ch10
 ('sub', ' [PENDING-VERIFY: X2]', '', '* **命题 `prop:disall-two-routes` —'),
 ('sub', ' [PENDING-VERIFY: X2]', '', '* **命题 `prop:disall-factorized-subtraction` —'),
 ('sub', ' [PENDING-VERIFY: X2]', '', '* **定理 `thm:disall-renorm-compat` —'),
 ('sub', ' [PENDING-VERIFY: X2]', '', '* **例 `ex:disall-ladder` —'),
 ('rep', ln(2045) + '\n', V10 + '\n'),
 # ---------------- Ch12
 ('sub', ' [PENDING-VERIFY: X1]', '', '* **引理 `lem:dy-poles-orientation` —'),
 ('sub', 'p. 553, [txt]) [PENDING-VERIFY: E31];', 'p. 553, [txt]; quotation only — Collins does not specify the errors, so they are neither listed nor characterized);', 'supersedes Bodwin 1985 and CSS 1985a", p. 553, [txt]) [PENDING-VERIFY: E31]'),
 ('sub', ' [PENDING-VERIFY: X1]', '', '* **例 `ex:dy-future-vs-past` —'),
 ('sub', ' [PENDING-VERIFY: X1]', '', '* **命题 `prop:dy-deformation` —'),
 ('sub', 'our derivation, novelty not claimed [PENDING-VERIFY: N25].',
  'our derivation of known results (`Collins2011` §14.3: eqs. (14.11)–(14.16), §14.3.3, §14.3.4), novelty not claimed (claim N25 confirmed).',
  'our derivation, novelty not claimed [PENDING-VERIFY: N25]'),
 ('sub', ' [PENDING-VERIFY: X1]', '', '* **例 `ex:dy-spectator-lcopt` —'),
 ('sub', '· **「本书新结果（待文献核查）」 candidate** [PENDING-VERIFY: N01, S63-5]', '· our derivation of a known result (`Meggiolaro:1996hf`, `Giordano:2006vv`; claim N01)', '* **命题 `prop:dy-eikonal-twogluon` —'),
 ('sub', 'Not shown: the other $O(g^4)$ graphs (argued to contribute only phases by unitarity of the eikonal system); non-eikonal spectators; all orders.',
  'Including the other $O(g^4)$ eikonal graphs (cited: `Meggiolaro:1996hf` eqs. (3.28)–(3.34), a real multiple of the tree with $F^{(2)}(t)$ real for $t<0$), unitarity holds at $O(g^4)$ for the complete eikonal amplitude. Not shown: non-eikonal spectators (model results in App O: `prop:appO-twoexch-spectator`); all orders.',
  'Not shown: the other $O(g^4)$ graphs (argued to contribute only phases by unitarity of the eikonal system)'),
 ('sub', 'Ingredients are classical (`Cheng:1969eh`, `Korchemskaya:1994qp`, `Korchemsky:1993hr`, `Caron-Huot:2013fea`); the marker is printed only if `verify/` records two independent confirmations and the literature check finds no prior statement of the conclusion (WRITER_SPEC_v2 §6.5); otherwise cite the prior source and present it as 「本书给出的推导」.',
  'The result is in the literature — `Meggiolaro:1996hf` §3, eqs. (3.23)–(3.26), (3.34), (3.36), and graph by graph `Giordano:2006vv` eq. (4.24) —, so it is printed as 「本书给出的推导」 citing these, without novelty marker (claim N01 verified; writer note: do not quote `Meggiolaro:1996hf` eq. (3.35) or `Giordano:2006vv` eqs. (4.15)–(4.21), (4.27)); the high-energy limit is classic (`Cheng:1969eh`, `Korchemskaya:1994qp`, `Korchemsky:1993hr`, `Caron-Huot:2013fea`); `RothsteinStewart2016` §9 (crossed Glauber boxes vanish with their $\eta$ regulator) is consistent.',
  'Ingredients are classical (`Cheng:1969eh`'),
 ('sub', ' [PENDING-VERIFY: N01]', '', '* **注 `rem:dy-common-ordering` —'),
 ('sub', '(`RothsteinStewart2016` eqs. (9.1), (9.18), (9.19), as read by c_glauber [PENDING-VERIFY: S63-9])', '(`RothsteinStewart2016` eqs. (9.1), (9.18), (9.19); locations verified)', 'as read by c_glauber [PENDING-VERIFY: S63-9]'),
 ('sub', '(iii) The genuine open problem is the interplay of Glauber, soft and collinear modes for non-eikonal (composite, interacting) spectators and for active partons (`asm:appO-mixing`(c)).',
  '(iii) The genuine open problem is the interplay of Glauber, soft and collinear modes for non-eikonal (composite, interacting) spectators and for active partons (`asm:appO-mixing`(c)); for composite spectators at $O(g^4)$ the uncut-line side sum cancels in the global two-time model of App O (`prop:appO-twoexch-spectator`, a model theorem, [P] as a QCD statement), while the cut direct lines (`rem:appO-cut-ss`) and $O(g^6)$ (`prop:appO-g6-ladder`) remain open.',
  '(iii) The genuine open problem is the interplay of Glauber, soft and collinear modes'),
 ('sub', '`asm:appO-mixing`(c) (beyond the $O(g^4)$ eikonal case)', '`asm:appO-mixing`(c) (beyond the $O(g^4)$ eikonal case; model evidence for the uncut lines of composite spectators: `prop:appO-twoexch-spectator`)', '- **地位与缺口 (four layers; print).** (1) Survey paragraph, unchanged in substance: 「状态 [A]。CSS (1985, 1988)'),
 ('sub', 'and `Diehl:2015bca` [PENDING-VERIFY: X1, N01, A11].', 'and `Diehl:2015bca` (an LCPT graph-by-graph argument with no ordering weights, `rem:appO-literature-comparison`); `AybatSterman2009` is an outline, not a proof.', 'and `Diehl:2015bca` [PENDING-VERIFY: X1, N01, A11]'),
 ('sub', 'the "plus trap" (VF-DY-12) [PENDING-VERIFY: N25 — attribution only].', 'the "plus trap" (VF-DY-12; attribution only, novelty not claimed).', 'the "plus trap" (VF-DY-12) [PENDING-VERIFY: N25'),
 ('sub', '| literature [PENDING-VERIFY: X1].', '| literature; rows filled from `tab:appO-checklist` (v2.3).', '- `tab:dy-status` (refdoc S34): rows = the App O steps'),
 ('rep', ln(2385) + '\n', V12 + '\n'),
 ('sub', '($O(g^4)$ unitarity, Regge phase; candidate 「本书新结果」)', '($O(g^4)$ unitarity, Regge phase; a known result, `Meggiolaro:1996hf`, printed as our derivation)', '**Purpose.** Verify `thm:method-template` for inclusive DY'),
 # ---------------- Ch14
 ('sub', '(the time-like vs space-like difference $2\\pi^2$ is an illustration, N20 [PENDING-VERIFY: N20])',
  '(the time-like vs space-like difference $2\\pi^2$ is an illustration: our one-loop derivation, claim N20 confirmed; the mechanism is stated qualitatively in `CollinsMetz2004` and Collins 2011 §10.6.4 (pp. 349–350), §10.11.1 (p. 381), Exercise 13.8 (p. 538); not marked new)',
  'is an illustration, N20 [PENDING-VERIFY: N20]'),
 ('sub', ' [PENDING-VERIFY: X2 for (b)]', '', '* **引理 `lem:tmd-sqrt-identity` —'),
 ('sub', 'do not copy Aybat–Rogers eq. (3), which has a spurious factor 2 (VF-TMD-9) [PENDING-VERIFY: E17 — App Q candidate].',
  'do not copy Aybat–Rogers eqs. (3), (4), which have a spurious factor 2 (VF-TMD-9; App Q, row Q.2; the same authors use the factor-free form in `Aybat:2011ge`).',
  'do not copy Aybat–Rogers eq. (3), which has a spurious factor 2'),
 ('sub', ' [PENDING-VERIFY: X2]', '', '* **命题 `prop:tmd-zero-bin-soft` —'),
 ('sub', ' [PENDING-VERIFY: X1]', '', '* **引理 `lem:tmd-glauber` —'),
 ('sub', '`RothsteinStewart2016` (eqs. (11.12)–(11.13), as read by c_glauber).', '`RothsteinStewart2016` (eqs. (11.12)–(11.13); verified).', '- **证明.** Sketch; `CollinsSoperSterman1985a`, Collins 2011 ch. 14, `JiMaYuan2005`'),
 ('sub', '`asm:appO-rewritten-cs` (substantive for TMD: the Wilson-line prescription of localized spectator terms).',
  '`asm:appO-rewritten-cs` (substantive for TMD: the Wilson-line prescription of localized spectator terms); the App O model results for coincident spectator patterns are [C] for TMD (`rem:appO-literature-comparison`(4)).',
  '- **地位与缺口.** [A]: `asm:appO-mixing`, `asm:appO-deformation`, `asm:appO-rewritten-cs` (substantive for TMD'),
 ('sub', '(`Collins:2016hqq`) [PENDING-VERIFY: S63-6];', '(`Collins:2016hqq`; confirmed);', '[PENDING-VERIFY: S63-6]'),
 ('sub', '($p=2$ expected for unpolarized leading-twist TMDs — [PENDING-VERIFY: S63-7])', '($p=2$ for unpolarized leading-twist TMDs: the leading small-$b_T$ power corrections are $O(b_T^2)$, `Scimemi:2016ffw`, `Moos:2020wvd`)', '($p=2$ expected for unpolarized leading-twist TMDs — [PENDING-VERIFY: S63-7])'),
 ('rep', ln(2625) + '\n', V14 + '\n'),
 # ---------------- Ch15
 ('sub', '(correction of BPS 2002\'s wording about the ghost term: c_scet §6 item 15 [PENDING-VERIFY: E25])',
  '(correction of the wording of `BauerPirjolStewart2002` after their eq. (24) about the ghost term: App Q, row Q.3; the field-strength term is collinear and ultrasoft invariant, the gauge-fixing and ghost terms are each only ultrasoft invariant, and only their sum is BRST invariant)',
  'c_scet §6 item 15 [PENDING-VERIFY: E25]'),
 ('sub', '(c_scet §6 item 13) [PENDING-VERIFY: E24].', '(c_scet §6 item 13; equivalently use `Becher:2006qw` eqs. (3), (6)).', '(c_scet §6 item 13) [PENDING-VERIFY: E24]'),
 ('rep', ln(2756) + '\n', V15 + '\n'),
 # ---------------- Ch16
 ('sub', 'is wrong by $4\\ln2|\\ln\\delta|$ [PENDING-VERIFY: E28 — App Q only if a published source with this error is identified];',
  'is wrong by $4\\ln2|\\ln\\delta|$ (a convention remark, not an erratum of `StermanWeinberg1977`: no printed source of the variant was found; numerically at $(\\epsilon,\\delta)=(10^{-6},0.003)$ the exact coefficient $-288.2811$ agrees with the $\\ln2\\epsilon$ form, $-288.2812$, not with the $\\ln\\epsilon$ form, $-304.39$);',
  '[PENDING-VERIFY: E28 — App Q only if a published source'),
 ('sub', 'super-super-leading (coherence-violating) logarithms in one-jettiness: `Banfi:2025mra` (Ch24) [PENDING-VERIFY: E16].',
  'super-super-leading (coherence-violating) logarithms in one-jettiness: `Banfi:2025mra`, confirmed for the $qg\\to qZ$ channel in SCET by `Becher:2026kbr` (Ch24).',
  'super-super-leading (coherence-violating) logarithms in one-jettiness: `Banfi:2025mra` (Ch24) [PENDING-VERIFY: E16]'),
 ('sub', '(three-loop active–active Glauber terms restore consistency below the veto scale) [PENDING-VERIFY: S63-10].',
  '(three-loop active–active Glauber terms restore consistency below the veto scale; by the authors\' own account this "does not amount to a proof").',
  '- **地位与缺口 (three items, refdoc S35).**'),
 ('rep', ln(2841) + '\n', V16 + '\n'),
 # ---------------- Ch18
 ('sub', ' [PENDING-VERIFY: X1]', '', '* **命题 `prop:break-measurement` —'),
 ('sub', 'closed formula as our derivation [PENDING-VERIFY: N18].', 'the closed formula $C_G=1+2\\langle\\mathbf T_a\\cdot\\mathbf T_b\\rangle/C_F$ is our compact derivation of the known channel values (claim N18 confirmed; attachment rule in Wilson-line language: `Buffing:2011mj`; not marked new).', 'closed formula as our derivation [PENDING-VERIFY: N18]'),
 ('sub', '(SU(3): $24/9$ vs $16/9$; c_glauber [C6]; VF-GLA-10) [PENDING-VERIFY: N17];', '(SU(3): $24/9$ vs $16/9$; c_glauber [C6]; VF-GLA-10; the attachment-sum form of `RogersMulders2010` eq. (34), our derivation of a known result);', '[PENDING-VERIFY: N17]'),
 ('sub', 'the Cauchy–Schwarz proof that $I_1(0)+I_2(0)<0$ [PENDING-VERIFY: N16]; the typo in C07 eq. (10) (VF-GLA-8) [PENDING-VERIFY: E18 — App Q candidate].',
  'the Cauchy–Schwarz proof that $I_1(0)+I_2(0)<0$ (「本书给出的证明」 of a statement of `Collins2007`; claim N16 confirmed, no published proof found; not a novelty claim); the misprint in `Collins2007` eq. (10) (VF-GLA-8; App Q, row Q.4).',
  'the Cauchy–Schwarz proof that $I_1(0)+I_2(0)<0$ [PENDING-VERIFY: N16]'),
 ('sub', 'restore consistency with PDF factorization below the veto scale [PENDING-VERIFY: S63-10];', 'restore consistency with PDF factorization below the veto scale (by the authors\' own account not a proof);', '- **地位与缺口.** CdFR predict possible "entangled" logarithms from N$^3$LO'),
 ('sub', 'the Gaunt claim is contested by SYZ — never cite Gaunt without SYZ (S58) [PENDING-VERIFY: E36];',
  '`Gaunt2014` shows that the CSS argument fails at two spectator–spectator Glauber gluons and only suggests a violation; `Schwartz:2018obd` contradict only the pure-Glauber part (their argument does not apply to doubly differential observables, so the $\\Delta p_\\perp$ mechanism of `RothsteinStewart2016` §11.1 and Zeng\'s model lie outside its scope) — never cite Gaunt without SYZ (S58);',
  'the Gaunt claim is contested by SYZ — never cite Gaunt without SYZ (S58) [PENDING-VERIFY: E36]'),
 ('rep', ln(3047) + '\n', V18 + '\n'),
 # ---------------- Ch19
 ('sub', ' [PENDING-VERIFY: X2]', '', '* **命题 `prop:excl-soft-cancel` —'),
 ('sub', 'exact soft fractions VF-EXC-14 [PENDING-VERIFY: N21]);', 'exact soft fractions VF-EXC-14: the closed forms are our evaluation of the Isgur–Llewellyn Smith fraction function, $f(\\varepsilon)=1-R(\\varepsilon)$, $f(1/150)=0.892$ for the asymptotic DA; novelty not asserted, the 1989 ILS papers were not accessible);', 'exact soft fractions VF-EXC-14 [PENDING-VERIFY: N21]'),
 ('sub', 'the correct sign is $-i0$ (c_exclusive §10 item 4) [PENDING-VERIFY: E20 — App Q candidate].', 'the correct sign is $-i0$, as in Ji\'s PRD 55 (1997) 7114 eq. (4) and `Vanderhaeghen:1999xj` eq. (38) (c_exclusive §10 item 4; App Q, row Q.5).', '[PENDING-VERIFY: E20 — App Q candidate]'),
 ('sub', 'do not quote MP\'s "$9/\\tau$" [PENDING-VERIFY: E21];', 'do not quote MP\'s "$9/\\tau$" (their eq. (10) gives $6/\\tau=4g^v(0)/\\tau$ and the ratio $2{:}1$ for every DA; App Q, row Q.6);', 'do not quote MP\'s "$9/\\tau$" [PENDING-VERIFY: E21]'),
 ('sub', 'the earlier sentence on "NLO claims that omit collinear subtractions" is **dropped** from this status paragraph: stage-1 verification shows that the criticised NLO calculation (Hoodbhoy–Lu, unpublished, later retracted by its author) concerns $\\gamma^*_L N\\to V_TN$, not transverse photons (`verify/claims/batch_E19_s1.md` §E22) [PENDING-VERIFY: E22];',
  'the earlier sentence on "NLO claims that omit collinear subtractions" is **dropped** (claim E22 refuted: the omission was acknowledged by its author, who confirmed the vanishing at one loop; nothing is printed about it);',
  'the earlier sentence on "NLO claims that omit collinear subtractions" is **dropped**'),
 ('sub', 'corrected by the authors — cite where used, not an App Q row [PENDING-VERIFY: E12]).', 'corrected by the authors in `Guo:2023pqw` §II — cite where used, not an App Q row).', 'not an App Q row [PENDING-VERIFY: E12]'),
 ('rep', ln(3166) + '\n', V19 + '\n'),
 # ---------------- Ch20
 ('sub', 'and Chay–Kim (`Chay:2003ju`) [PENDING-VERIFY: S63-11],', 'and Chay–Kim (`Chay:2003ju`),', 'and Chay–Kim (`Chay:2003ju`) [PENDING-VERIFY: S63-11]'),
 ('sub', 'the printed "$\\ln(m_M/\\Lambda_h)$" must read $m_B$, c_scet §6 item 17 [PENDING-VERIFY: E26]); annihilation coefficients VF-BQ-5 (prescription dependence of the model illustrated [PENDING-VERIFY: N22]).',
  'the printed "$\\ln(m_M/\\Lambda_h)$" must read $m_B$, c_scet §6 item 17; App Q, row Q.7); annihilation coefficients VF-BQ-5 (the model dependence is stated by `BenekeEtAl2001` and `BenekeNeubert2003` themselves; no illustration of our own is printed).',
  'must read $m_B$, c_scet §6 item 17 [PENDING-VERIFY: E26]'),
 ('rep', ln(3254) + '\n', V20 + '\n'),
 # ---------------- Ch21
 ('sub', '(`Feldman:1986ax`, `Gawedzki:1985ez`) [PENDING-VERIFY: S63-11].', '(`Feldman:1986ax`, `Gawedzki:1985ez`; cited as stated in the literature, contents not re-read in the verification).', '(`Feldman:1986ax`, `Gawedzki:1985ez`) [PENDING-VERIFY: S63-11]'),
 ('sub', '(`prop:appN-triangle-exact`(c) [PENDING-VERIFY: N12]); AQFT OPE (`Bostelmann:2005rr`);', '(`prop:appN-triangle-exact`(c), claim N12 confirmed; `prop:appN-triangle-cs`); AQFT OPE (`Bostelmann:2005rr`, not re-read);', '(`prop:appN-triangle-exact`(c) [PENDING-VERIFY: N12])'),
 ('rep', ln(3370) + '\n', V21 + '\n'),
]
