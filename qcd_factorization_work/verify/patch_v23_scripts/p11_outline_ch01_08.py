import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import src
ln = src.ln
TARGET = 'FINAL_OUTLINE_v2.md'

def strip_hdr(key, marker):
    """remove ' ' + marker from the unique line containing key"""
    return ('sub', ' ' + marker, '', key)

OPS = [
 # ---- Ch1
 ('sub', r'''a full $\lambda^2$ with no logarithm at NLP (`prop:appN-triangle-exact`(c); VF-REF-3) [PENDING-VERIFY: N12].''',
         r'''a full $\lambda^2$ with no logarithm at NLP (`prop:appN-triangle-exact`(d); VF-REF-3; a sharpened explicit result, not marked new), and its fibered integral norm is $O(\lambda^2L^2)$ (`prop:appN-triangle-cs`, App N).''',
         'the exact Collins remainder is $-4m^2/Q^4+O(m^4Q^{-6}L^2)$'),
 ('rep', ln(411) + '\n', r'''**Verification (v2.3).** `rem:intro-sharpness`(b): claim N12 confirmed (two-stage); printed as a sharpened explicit result, never marked new; the ★ rows of `tab:intro-overview` follow Ch25.''' + '\n'),
 # ---- Ch2
 ('sub', r'''`Hollands:2007zg` (pure Yang–Mills, curved spacetime) [PENDING-VERIFY: S63-3 — which parts these cover].''',
         r'''`Hollands:2007zg` (pure Yang–Mills, curved spacetime); scope (S63-3): the Joglekar papers were read at abstract level and Hollands' gauge-invariant closure concerns pure Yang–Mills (not verified in detail) — App M §M.6 states exactly which inputs the OPE route uses.''',
         'literature `Joglekar:1975nu`, `Joglekar:1976eb`, `Joglekar:1976pe` (Joglekar 1977 I+II, QCD currents)'),
 ('sub', r'''`Falcioni:2022fdm`, `Gehrmann:2023ksf` [PENDING-VERIFY: S63-4];''',
         r'''`Falcioni:2022fdm`, `Gehrmann:2023ksf`; precision (S63-4, R-M24): the explicit forward counterexample of `Collins:1994ee` concerns a BRST-exact alien operator, while for EOM operators the forward on-shell massless case is simply not covered by the proof (never claim that it fails);''',
         'literature `Joglekar:1975nu`, `Joglekar:1976eb`, `Joglekar:1976pe` (Joglekar 1977 I+II, QCD currents)'),
 ('sub', r'''a moment reduction of the bilocal PDF case to the local theorem is discussed in Ch24 (pointer) [PENDING-VERIFY: N04].''',
         r'''a moment reduction of the bilocal PDF case to the local theorem (prior art: `Braun:2019qtp` eqs. (2.4), (2.6), (3.1)–(3.2)) is stated in Ch24 (`prop:front-brst-bilocal`, pointer).''',
         'literature `Joglekar:1975nu`, `Joglekar:1976eb`, `Joglekar:1976pe` (Joglekar 1977 I+II, QCD currents)'),
 ('sub', r''' [PENDING-VERIFY: E28 — only if a published source is named as erroneous];''',
         r''' — a convention remark, not an erratum of `StermanWeinberg1977` (verified, E28);''',
         'the variant with $\\ln\\epsilon$ belongs to $\\epsilon$ defined relative to the beam energy)'),
 ('rep', ln(639) + '\n', r'''**Verification (v2.3).** `thm:prelim-composite-renorm` caveats: S63-3 (scope stated), S63-4 (R-M24 precision), N04 (prior art `Braun:2019qtp`); `ex:qcd-sterman-weinberg`: E28 confirmed as a convention remark (no App Q row). VF-QCD-4 general-$\xi_g$ entries (status C) are re-derived by the writer (not a verify item).''' + '\n'),
 # ---- Ch3
 ('sub', r''' (VF-WL-2) [PENDING-VERIFY: N26 — attribution sentence only].''',
         r''' (VF-WL-2); the additive cumulative regulator and the failure of the uniform one are in `Echevarria:2015byo` (eqs. (5)–(6) and text; claim N26 verified, novelty not claimed); the abelian identity itself is classical.''',
         '\\prod_ja_j^{-1}$; exact at finite $\\epsilon$ with the adiabatic regulator'),
 ('rep', ln(788) + '\n', r'''**Verification (v2.3).** `lem:prelim-eikonal-identity`: N26 confirmed; attribution `Echevarria:2015byo` (novelty not claimed).''' + '\n'),
 # ---- Ch4
 ('sub', r'''with a constructive min-norm direction [PENDING-VERIFY: N02].''',
         r'''with a constructive min-norm direction (`Gordan1873`; an elementary identification, printed as a remark in Ch24, not as a new result; N02 verified).''',
         "the geometric part of Collins' 2020 theorem is Gordan's alternative"),
 ('sub', r'''survey item 4; Ch24 discusses it) [PENDING-VERIFY: A08];''',
         r'''survey item 4; Ch24 discusses it; an unrefereed preprint, A08 verified);''',
         'Complete proof only in the preprint `Collins:2020euz`'),
 ('sub', r'''as identified in `Collins:2020euz` [PENDING-VERIFY: E14]; heuristic textbook derivations (E15 — not printed unless verified);''',
         r'''as identified in `Collins:2020euz` §IV and App. D (E14 verified: the tacit equivalence of momentum and parameter pinches fails for massless graphs and linear denominators); heuristic textbook derivations (`EdenEtAl1966` §2.1: "We shall be content with plausibility arguments", p. 48; Collins' objections in `Collins:2020euz` §IV; E15 verified);''',
         'Complete proof only in the preprint `Collins:2020euz`'),
 ('sub', r'''momentum-space version including Wilson lines: Ch24 (pointer) [PENDING-VERIFY: N03].''',
         r'''momentum-space version including Wilson lines: a specialization of `Collins:2020euz` Thm 1 with the Coleman–Norton closure (Ch24, pointer; not new, N03).''',
         'the stronger claim "trapped ⇔ classically realizable"'),
 ('sub', r'''Attributions per A10 [PENDING-VERIFY: A10].''',
         r'''Attributions (A10, verified): rigorous for Euclidean large-momentum and large-mass limits (`Smirnov:1990rz`); a general derivation conditional on commuting expansions and exchangeable summations (`Jantzen2011`); the facet prescription proven at leading order for each essential facet and to all orders when a single facet contributes (`Semenova:2018cwy`); regions and Landau solutions, commutativity for a class of regions (`Gardi:2022khw`); new regions from dissected polytopes from three loops (`Gardi:2024axt`); a hidden three-loop active–active Glauber region missed by an automated finder (`Becher:2024kmk`); the off-shell Sudakov regions example is cited from `BecherBroggioFerroglia2015` §2.2 (massive exchange §2.3, `Jantzen2011` §6), not from `BenekeSmirnov1998`.''',
         'The facet prescription "regions = lower facets of the Newton polytope" fails'),
 ('rep', ln(967) + '\n', r'''**Verification (v2.3).** N02, N03 (remarks, not new; N02 with the literature-search sentence in Ch24), E14, E15 (status paragraphs with Collins' diagnoses), A08 (preprint status), A10 (attributions) — all confirmed; wording applied.''' + '\n'),
 # ---- Ch5
 ('sub', r'''(`ex:method-sudakov-subtraction`, `prop:appN-triangle-exact`) [PENDING-VERIFY: N12];''',
         r'''(`ex:method-sudakov-subtraction`, `prop:appN-triangle-exact`; a sharpened explicit result, not marked new) and their integral-norm verification (`prop:appN-triangle-cs`);''',
         'Forward pointers: the Collins subtraction terms of the same triangle and their exact remainder'),
 ('sub', r'''whether it establishes integral-norm (E-N) bounds or scaling statements (E-S) is open item S63-12 [PENDING-VERIFY: S63-12];''',
         r'''it works at the level of scaling statements and pinch surfaces (E-S), not of integral-norm (E-N) bounds (S63-12, resolved); integral-norm bounds are written out only for the one-loop off-shell triangle (`prop:appN-triangle-cs`, App N);''',
         'the subtraction proof is complete in Collins 2011 ch. 10 for this case'),
 ('sub', r'''(the arXiv source of Becher–Schwartz App. A has a spurious $C_F$, c_scet §6 item 10; VF-SCET-16) [PENDING-VERIFY: E23 — App Q candidate];''',
         r'''(`BecherSchwartz2008` eq. (A.10) — journal and arXiv versions — has a spurious $C_F$ multiplying $T_Fn_f$; erratum E23, App Q row Q.1; $\Gamma_1=36.8436$ for $n_f=5$; VF-SCET-16);''',
         'VF-CONV-23: $\\Gamma_{\\rm cusp}=\\sum_n'),
 ('rep', ln(1083) + '\n', r'''**Verification (v2.3).** `ex:sudakov-offshell` pointer (N12: sharpened, not marked new); `def:sudakov-cusp` (E23: App Q row Q.1); `thm:sudakov-factorization` status sentence (S63-12: scaling statements vs integral norms, resolved as stated).''' + '\n'),
 # ---- Ch6
 ('sub', r'''is open [PENDING-VERIFY: N24];''',
         r'''was carried out in the verification (N24): all interaction terms of massless QCD in covariant gauges, ghost terms included, have IR degree $\ge4$, as `Breitenlohner:1976te` requires;''',
         'the explicit check that the Breitenlohner–Maison hypotheses are spelled out for non-abelian gauge fields'),
 ('sub', r'''Route as our derivation (novelty not claimed) [PENDING-VERIFY: N24].''',
         r'''Route: the corollary of `PoggioQuinn1976` (physical discontinuities are IR finite), written out here (novelty not claimed; N24 verified).''',
         'finiteness at $q^2<0$; Laurent coefficients are polynomials in $L$ vanishing for all real $L$'),
 ('sub', r'''Our derivation (novelty not claimed) [PENDING-VERIFY: N24].''',
         r'''Our derivation (novelty not claimed).''',
         '  - **证明.** Full (reflection formulas). Our derivation'),
 ('sub', r'''(binding decision D3; attribution per A09 [PENDING-VERIFY: A09])''',
         r'''(binding decision D3; attributions as verified, A09; the theory class covered by `Anikin:1978tj` is unverified)''',
         'for QCD with quarks "proved in a gauge theory the same way" (`Collins1984` §12.8) or widely assumed'),
 ('rep', ln(1243) + '\n', r'''**Verification (v2.3).** N24 (the Breitenlohner–Maison hypotheses hold for massless QCD with ghosts in covariant gauges; route attributed to Poggio–Quinn); A09 (OPE status wording as verified); E29 is history only (no App Q row).''' + '\n'),
 # ---- Ch7 headers
 strip_hdr('* **引理 `lem:dis-twist-classification` —', '[PENDING-VERIFY: X3]'),
 strip_hdr('* **引理 `lem:dis-twist-chirality` —', '[PENDING-VERIFY: X3]'),
 strip_hdr('* **命题 `prop:dis-ope-euclid` —', '[PENDING-VERIFY: X3, S63-1]'),
 strip_hdr('* **命题 `prop:dis-ope-gi` —', '[PENDING-VERIFY: X3, S63-3]'),
 strip_hdr('* **命题 `prop:dis-ope-forward` —', '[PENDING-VERIFY: X3, S63-4]'),
 strip_hdr('* **命题 `prop:dis-chiral-suppression` —', '[PENDING-VERIFY: X3]'),
 strip_hdr('* **引理 `lem:dis-euclid-segment` —', '[PENDING-VERIFY: X3]'),
 strip_hdr('* **命题 `prop:dis-dispersion-np` —', '[PENDING-VERIFY: X3]'),
 strip_hdr('* **命题 `prop:dis-low-moments` —', '[PENDING-VERIFY: X3]'),
 strip_hdr('* **引理 `lem:dis-ope-segment` —', '[PENDING-VERIFY: X3]'),
 strip_hdr('* **定理 `thm:dis-fixed-n` —', '[PENDING-VERIFY: X3]'),
 strip_hdr('* **定理 `thm:dis-moments-np` —', '[PENDING-VERIFY: X3]'),
 strip_hdr('* **推论 `cor:dis-weak-xspace` —', '[PENDING-VERIFY: X3]'),
 # ---- prop:dis-ope-euclid body
 ('rep', ln(1325) + '\n' + ln(1326) + '\n' + ln(1327) + '\n' + ln(1328) + '\n',
  r'''  - **陈述.** At each order, for Euclidean non-exceptional $(p,q)$ and in covariant gauges ($\xi$ in a compact set containing 1), the T-product Green function of two currents with elementary external fields admits (A1) $\tilde G^T-\sum_{d_O\le a}\tilde C_O(q;\mu)\tilde G_{[O]}=O(|q|^{D-1-a}\ln^k|q|)$, uniformly in the direction of $q$, in compact non-exceptional $p$ and in $\xi$, in a D-dimensional operator basis that includes gauge-variant, ghost and evanescent operators; (A2) the coefficients are $|q|^{D-d_O}\times$ polynomials in $\ln(q^2/\mu^2)$; (A3) $\tilde C^{\overline{\rm MS}}=\tilde C^{\rm bare}Z^{-1}$ is finite; (A4) the coefficients are **unique blockwise** wherever the four-dimensional tree vertices are independent (condition (NE): the symmetric channel up to dimension 5 and all twist-2 blocks, so all twist-2 coefficients are unique for every $n$; `lem:appM-ne`, `lem:appM-uniqueness`(b)).
  - **证明.** Sketch; location App M §M.5: (A1), (A3) cited graph by graph — `Smirnov:1990rz` (checked: a mixed coordinate/momentum statement in analytic regularization, the DR function form only asserted, ghosts, gauge-variant bases and composite spectators not treated), `Smirnov2002`, `Chetyrkin:1982zq`; IR finiteness `Breitenlohner:1976te` Thm 1; BPHZL convergence `LowensteinZimmermann1975`, `Zimmermann1973`; BPHZL vs DR+$R^*$ —; (A2) by homogeneity; (A4) by `lem:appM-uniqueness`(b).
  - **地位与缺口.** Tag [A] under the binding decision D3 (v1 §0.9 item 4 did not adopt the grade "[R] in PT as a combination of classical results" of the frontier report), **confirmed by the verification** (S63-1): the cited theorem was read in full and its scope falls short of (A1), (A3) as stated (slot X3b not passed); Ch25 open problem OP-A2 stands. The DR route does not use `asm:appM-remainder`; the route "discharge `asm:appM-remainder` by a published theorem plus uniqueness" is circular (S63-2; App M `rem:appM-remainder-reduction`). Error type: E-P per graph (where the cited theorems apply). (本命题只涉及部分子态的 Green 函数。)
  - `\uses{lem:dis-tree-ope, thm:qcd-renormalizability, thm:ee-euclid-ir, lem:appM-uniqueness, lem:appM-ne}`
'''),
 # ---- prop:dis-ope-gi body
 ('rep', ln(1331) + '\n' + ln(1332) + '\n' + ln(1333) + '\n' + ln(1334) + '\n',
  r'''  - **陈述.** (a) For $j^\mu j^\nu$ between physical states only gauge-invariant operators contribute; at twist 2 only $O_q$, $O_g$. (b)（蕴含关系，\tagR，$R_{\rm cond}$）Given `prop:dis-ope-euclid`, (a) follows under `asm:appM-brst-ope`, i.e. the Euclidean expansion with one composite spectator $s\phi$ **including the merged terms** (its item (B2) ≡ (Eε)): then $sX_d\in\mathcal E$ for every coefficient sum $X_d$, hence gauge-invariant ⊕ BRST-exact ⊕ EOM.
  - **证明.** (b) full in App M §M.6 (`thm:appM-brst-reduction`, `lem:appM-lbc-formal`). Literature: `Joglekar:1976eb`, `Joglekar:1976pe` (QCD currents; read at abstract level), `Hollands:2007zg` (pure YM; not verified), `thm:prelim-composite-renorm`.
  - **地位与缺口.** [A] = the status of (Eε) of `asm:appM-brst-ope`; the hope that Joglekar 1977 and Hollands 2008 discharge the earlier (B1)(B2) is not confirmed (S63-3: abstract-level reading; pure Yang–Mills not verified; slot X3d partial); forward on-shell caveat as in `thm:prelim-composite-renorm`.
  - `\uses{prop:dis-ope-euclid, thm:prelim-composite-renorm, lem:dis-twist-classification, asm:appM-brst-ope, thm:appM-local-cohomology, lem:appM-alien-vanish, lem:appM-uniqueness, thm:appM-brst-reduction, lem:appM-lbc-formal}`
'''),
 # ---- prop:dis-ope-forward body
 ('rep', ln(1337) + '\n', ln(1337) + r''' (c) At every order the analytic step is proved per graph (App M `thm:appM-forward-expansion`, [R, R_PT]: each forward on-shell DR Laurent coefficient is holomorphic on the cut $\omega$-plane and equals its naive Taylor series), and (a) holds as `cor:appM-forward-ope`(a) ([A]: the identification with $\overline{\rm MS}$ coefficients goes through (A3) of `prop:dis-ope-euclid` and (Eε) of `asm:appM-brst-ope`).''' + '\n'),
 ('rep', ln(1338) + '\n', r'''  - **证明.** (b) full in App M §M.7; (c) App M §M.7 (`thm:appM-forward-expansion`, `cor:appM-forward-ope`). Check: exact in $\varepsilon$ at $O(\alpha_s)$, $N\le8$ (c_dis `ope_check`, VF-DIS-13).''' + '\n'),
 ('rep', ln(1339) + '\n', r'''  - **地位与缺口.** [A] = the status of `asm:appM-forward`, which `cor:appM-forward-ope` reduces to (A3), (Eε) and the Joglekar–Lee triangularity — reduced, not discharged (S63-4 closed with the R-M24 precision: the forward counterexample of `Collins:1994ee` is for a BRST-exact operator; for EOM operators the forward on-shell case is not covered); never write 「前向在壳部分子矩阵元直接给出 Wilson 系数，无需额外步骤」 (S58).''' + '\n'),
 ('sub', r'''lem:prelim-scaleless, asm:appM-forward, lem:appM-uniqueness}`''', r'''lem:prelim-scaleless, asm:appM-forward, lem:appM-uniqueness, cor:appM-forward-ope}`''', '  - `\\uses{prop:dis-ope-euclid, prop:dis-ope-gi, lem:prelim-scaleless, asm:appM-forward'),
 # ---- thm:dis-ope status
 ('sub', r'''Attribution per A09 [PENDING-VERIFY: A09].''',
         r'''Attributions verified (A09): Zimmermann's proof for scalar theories; `Collins1984` §12.8 asserts the gauge-theory case; `IzubuchiEtAl2018` "widely assumed"; `Hollands:2007zg`: pure Yang–Mills, OPE closing on gauge-invariant operators; `Frob:2016mzv` (preprint): existence for massless renormalizable theories and BRST Ward identities of the coefficients if $H^{1,4}_{E(4)}(s|d)=0$; convergence at finite distance only for $\varphi^4_4$ at fixed loop order; the theory class of `Anikin:1978tj` unverified. The partonic forward sub-statement is reduced, not discharged (App M `cor:appM-forward-ope`).''',
         '**地位与缺口 (verbatim in substance, survey item 1).** Proven to all orders in PT for scalar theories'),
 # ---- prop:dis-ope-rg proof
 ('rep', ln(1361) + '\n' + ln(1362) + '\n',
  r'''  - **证明.** Full, **derived directly from (A3)** of `prop:dis-ope-euclid` (App M §M.6; no uniqueness and no condition (NE) needed): $\hat{\mathcal D}C^{\rm bare}=0$ gives $(\mu\partial_\mu+\beta\partial_\alpha+\beta_\xi\partial_\xi)\tilde C_i=\sum_j\tilde C_j\gamma_{ji}$ in the full D-dimensional basis; the twist-2 gauge-invariant form at $\xi_R=1$ uses `prop:dis-ope-gi` (coefficients outside GI ⊕ aliens vanish), the Joglekar–Lee triangularity with $\partial_\xi\gamma_{GG}=0$ (`prop:appJ-local-operators`) and the $\xi$-independence of the twist-2 coefficients from `prop:dis-ope-forward`; together with `thm:prelim-composite-renorm` and `prop:qcd-rge`. The earlier route "from the exact uniqueness" (refdoc S22, Prop C.46) is superseded.
  - `\uses{prop:dis-ope-euclid, prop:dis-ope-gi, prop:dis-ope-forward, thm:dis-ope, thm:prelim-composite-renorm, prop:appJ-local-operators, prop:qcd-rge, asm:intro-wightman, asm:intro-composite}`
'''),
 # ---- prop:dis-dispersion-np
 ('sub', r'''(d) for every even $n_0>A+2$:''', r'''(d) for every even $n_0>A+1$:''', '  - **陈述.** 前提：\\cref{asm:intro-wightman}。For a hadron target: (a) $T_2$ is analytic'),
 # ---- E32
 ('sub', r'''do **not** print any "commonly quoted variant": stage-1 verification found no printed source of the variant with $\frac2{N+1}+\frac1{N^2}$ (`verify/claims/batch_E31_s1.md` §E32; a single confirmation) — print the correct coefficient with its sources (`BardeenEtAl1978` eq. (3.9), $\overline{\rm MS}$ form) and the Adler check, which `BardeenEtAl1978` already state [PENDING-VERIFY: E32].''',
         r'''print only the correct coefficient with its sources (`BardeenEtAl1978` eqs. (3.9), (4.7), (4.10), $\overline{\rm MS}$ form; `Vermaseren:2005qc` eq. (A.3)) and the Adler check, which `BardeenEtAl1978` already state; no "commonly quoted variant" and no erratum is printed (claim E32 refuted: the variant was not found in print).''',
         'MVV normalization $c^{(1)}_{2,\\rm ns}=2C^q_{2,N}$'),
 ('rep', ln(1470) + '\n', r'''**Verification (v2.3).** All refdoc S19–S22 statements: final forms from the X3 report (App M); `prop:dis-ope-euclid` stays [A] (S63-1, S63-2 resolved); `prop:dis-ope-gi`: (Eε) route (S63-3); `prop:dis-ope-forward`: reduced via `cor:appM-forward-ope` (S63-4); `thm:dis-ope` status wording (A09 verified); `prop:dis-c-oneloop`: E32 refuted, no variant printed.''' + '\n'),
 # ---- Ch8
 ('sub', r'''The debate (CFH vs CRS, CFGH 2024) is reported without a verdict [PENDING-VERIFY: E35];''',
         r'''Verified facts of the debate (E35; a status item, no App Q row): `CollinsRogersSato2022` §VI show that the argument of `CandidoForteHekhorn2020` fails at the step "bare PDFs are positive" (UV contributions positive for $n<4$ turn negative after continuation to $n>4$); in the Yukawa counterexample $f<0$ exactly for $\xi\in(0.264,1)$ at $\mu=0.8$ GeV, and $f>0$ for all $\xi$ iff $\mu\ge1.699$ GeV; `Candido:2023ujx` agree that PDFs turn negative at low, non-perturbative scales and estimate positivity conservatively for $Q^2\gtrsim5$ GeV²; no verdict beyond these facts;''',
         'Circularity warning (C13): LO evolution preserving positivity does not prove positivity of the initial condition.'),
 ('rep', ln(1646) + '\n', r'''**Verification (v2.3).** `conj:pdf-positivity`: debate wording with the verified facts (E35); `def:pdf-ff` Collins location (S63-9: locations of `Collins2011` verified, A13); pointer to the BRST moment reduction (Ch24; N04 prior art `Braun:2019qtp`).''' + '\n'),
]
