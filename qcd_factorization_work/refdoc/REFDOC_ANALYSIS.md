# REFDOC_ANALYSIS — the reference document `factorization_qcd-2.pdf` and what it means for our monograph

**Status:** synthesis of the eight-segment deep reading, 2026-10-10. This file is an input for the spec synthesizer (FINAL_OUTLINE / WRITER_SPEC / VERIFIED_FORMULAS / FIGURES_INDEX) and for the chapter writers.

**Inputs.**
- Reader notes `refdoc/notes/R1.md` … `R8.md`, all read in full:
  - R1: pp. 1–27; R2: pp. 28–51; R3: pp. 51–71; R4: pp. 72–88 plus the bibliography (pp. 231–238);
  - R5: pp. 88–127 (App. C); R6: pp. 128–161 (App. D); R7: pp. 162–196 (App. E, part 1); R8: pp. 197–230 (App. E, part 2).
- `CONTEXT.md`, `REQUIREMENTS.md`.
- Our plan: `research/critic/REVIEW.md` §3, §4, §5 (TOC v1); `research/architect/BLUEPRINT.md` §0, Ch. 5, Ch. 7, Ch. 10; `spec/FINAL_OUTLINE.md` (§0, all chapter entries, App. A–L, master-table rows, registry); `spec/WRITER_SPEC.md` (complete); `spec/FIGURES_INDEX.md` (rules, existing labels, optional list); `spec/VERIFIED_FORMULAS.md` (VF-CONV-17, status codes); `spec/refs_merged.bib` (key checks).
- The spec files were **re-read at 15:20**, after the spec audit had applied the corrections of §2.4 (see the note at the head of §5).

**Checks made by the synthesizer.** These are in addition to the readers' own checks, which are listed in each note.
1. Reran R1's `work_R1/check_ff_norm.py`. The hadron-frame prefactor $z^{d-3}/(4N_c)$ reproduces $\frac{\alpha_s}{2\pi}C_F\frac{1+z^2}{1-z}\frac{dl_T^2}{l_T^2}$ exactly. Our binding $1/(4N_cz)$ gives $z^{-2}$ times this (§2.4, spec change S9).
2. Reran R3's `work_R3/scripts/eikonal_box_closedform.py`. For two infinite time-like eikonal lines,
   $J_{\rm box}=\frac{2\pi}{ab}(\pi+iY)$ and $J_{\rm cross}=-\frac{2\pi iY}{ab}$, with maximal relative deviation $4.7\times10^{-16}$ at 6 points (§2.1 ERR-S1, S37).
3. Read (E.51) on p. 217 directly with `pdftotext`: equal ordering weights give $A_2=\frac12(-i\chi)^2(X^2+\frac14C_AX)$, i.e. residual $-\frac14C_A\chi^2X$. This resolves the R4 / R3–R7–R8 numerical disagreement (§2.5).
4. New script `refdoc/work_SYN/triangle_remainder.py` (+`.log`, all checks pass). It reproduces R6's value of the one-loop Collins remainder ($-0.0173434339581$). It also shows that the exact remainder is $\int r=-4m^2/Q^4+\frac{m^4}{Q^6}(L^2-15+\frac{\pi^2}3)+O(m^6Q^{-8}L^2)$ — no logarithm at NLP — and verifies the expansion of the exact triangle to $O(t^2)$ (S30, ERR-m25).
5. Checked in `refs_merged.bib` every key proposed in §5 as "already present" (S60).

**Page numbering.** In the entire document the printed page number equals the physical (pdfinfo) page number; the title page is p. 1. All page references below are both.

**Extraction warning.** `pdftotext` detaches superscript minus signs and garbles fractions. For example, it shows a spurious overall "−" in (E.19), while the image is correct. Every formula quoted from the reference must be taken from the page image (R7 E1, R8).

---------------------------------------------------------------------------------------------------

## 0. Executive summary

The reference is a 238-page Chinese text, 「QCD 中的因子化定理：证明、论证与适用边界」, dated 2026-10-10. Its main text (§§1–15, pp. 6–85) is short. About 60 % of the pages are three deep appendices:
- **App. C** (pp. 88–127): the OPE — perturbative proof in massive models, assumptions, and a non-perturbative conditional moment theorem;
- **App. D** (pp. 128–161): the precise form of Collins' subtraction method;
- **App. E** (pp. 162–230): a conditional reconstruction of the Glauber cancellation in colour-singlet inclusive Drell–Yan, built on light-cone-ordered perturbation theory (LCOPT).

Its organizing idea is the one our plan also adopted: every non-trivial result is a **conditional theorem** whose unproven inputs are **numbered assumptions**, with a separate "bridging hypothesis" from partonic perturbation theory to hadrons. The reference executes this idea far more precisely than our current spec in exactly the three places our FINAL_OUTLINE §0.5 names as the weakest links:
1. the OPE and moments;
2. the subtraction theorem;
3. the Glauber region.

**What the reference has that we lack, and must adopt.**
- **App. C.** A rigorous fixed-$n$ moment theorem for hadrons (Thm C.50 + Lemma C.64 + Rem C.65 + Thm C.66). Three points:
  - the Euclidean OPE informs only on the shrinking segment $|\omega|\le\sqrt3M/Q$;
  - moments follow without any sum over spins, from positivity and a $Q$-uniform finite-subtraction dispersion relation proved from Wightman axioms;
  - only the $n=2$ (momentum) sum rule needs a genuine growth assumption.
  It also builds the BPHZ/normal-product machinery behind the perturbative OPE.
- **App. D.**
  - The precise subtraction theorem: conditions at the level of subtraction terms (renamed (CS1)–(CS3) below) and a three-line covering proof.
  - Counterexamples showing that the "naive induction", which is what our BLUEPRINT T7.14 / FINAL_OUTLINE `thm:method-subtraction` proof plan does, fails.
  - The chain expansion, pairing decomposition and product formula.
  - Explicit idempotent approximators with their $i0$, and the complete error table.
  - A fully worked one-loop subtraction with absolutely convergent iterated integrals.
- **App. E.**
  - A rigorous derivation of LCOPT from Feynman integrals.
  - Orientation as a property of LCOPT intermediate states.
  - An exact light-cone largest-time identity with insertions, and a closed-time-path unitarity lemma.
  - An exact equal-light-cone-time localization lemma.
  - Simultaneous two-component contour deformation along $e_G=n_B-n_A$.
  - Quantitative eikonal bounds on the deformed contour.
  - Past-pointing Wilson lines.
  - An honest rigour checklist, plus a precise location of the failures for $pp\to h_1h_2X$, gaps and DFT.

**What the reference gets wrong.** §2 lists 63 de-duplicated items: 4 substantive, 32 moderate, 27 minor. It also lists 8 errors in our own spec (§2.4, OUR-1…OUR-8), which the spec audit has since applied as interim caveats. The most important errors of the reference are these.
1. The non-abelian "residual" $-\frac14C_A\chi^2\mathbf T_A\!\cdot\!\mathbf T_B$, the reference's main justification for an intermediate grade B′ for DY, is an artefact of the strict Glauber truncation. The exact two-gluon eikonal integrals give ${\rm Re}\,p_{\rm opp}=0$: unitarity holds at $O(g^4)$, and the $C_A$ term is the one-loop reggeization phase.
2. Its colour argument for TMD breaking in $pp\to h_1h_2X$ is self-contradictory as written, and the Rogers–Mulders and Nayak–Qiu–Sterman results are misreported.
3. Several over-classifications: the false Euclidean "no-pinch" corollary; super-leading configurations omitted; Thm 3.14 claimed as a theorem; NRQCD decay graded "A*"; gap observables graded "D"; Assumption E.33(c1) internally inconsistent; the Glauber-specific content of the inputs undercounted.

**What we already do better.** See §4. Our plan covers whole areas the reference lacks or treats in a paragraph:
- the Sudakov form factor;
- threshold resummation with formulas;
- jets, NGLs and SLLs;
- small $x$;
- polarized DIS, transversity and Bjorken;
- heavy-quark schemes and nuclear targets;
- photoproduction;
- lattice/LaMET and the frontier;
- explicit one-loop TMD and Glauber computations;
- the explicit Collins–Qiu, Collins 2007 and Rogers–Mulders algebra;
- the CdFR order table and Becher et al. 2025.
It also has correct statements in several places where the reference errs: $P^\pm_{\rm NS}$, Gaunt vs Schwartz–Yan–Zhu, space-like self-energies, and the FSI colour factor $-\mathbf T_a-2\mathbf T_b$.

**Spec changes.** §5 gives 63 numbered changes. The main ones:
- **Four new appendices.**
  - M: OPE — 24 pp.
  - N: precise subtraction — 24 pp.
  - O: LCOPT and the Glauber cancellation — 32 pp.
  - P: formal blueprint and assumption register — 8 pp. This is the generated "App M blueprint" of FINAL_OUTLINE §0.9 item 2, relettered.
- **Tag system.** A fourth `[R]` qualifier $R_{\rm cond}$, for complete proofs from numbered assumptions. A label prefix `asm:` and an assumption register of 25 entries. A grading reconciliation and an error-type taxonomy.
- **Restated statements.** `thm:dis-moments`, `thm:dis-ope`, `thm:method-subtraction`, `prop:method-glauber-deformation` and `thm:dy-factorization` (status layer). These supersede the audit's interim caveats. `def:pdf-ff` (normalization bug) is already fixed.
- **New statements and figures.**
  - 102 new canonical statements: 7 theorems, 25 propositions, 33 lemmas, 4 corollaries, 5 definitions, 6 examples, 22 remarks.
  - 25 numbered assumptions and 12 tables.
  - 22 new figures: 17 required, 5 optional; one existing optional figure is promoted.
  - 7 new master-table rows.
- **New and sharpened results.**
  - One statement is marked 「本书新结果（待文献核查）」: for eikonal spectators, the exact box and crossed box restore unitarity at $O(g^4)$ with no residual (`prop:dy-eikonal-twogluon`, [R, R_PT]). Its ingredients are classical, so a literature check is required before the marker is printed.
  - One sharpened explicit result: the exact Collins remainder of the one-loop off-shell triangle has no logarithm at NLP (`prop:appN-triangle-exact`). This also shows that the reference's Table 5 does not test the remainder.

---------------------------------------------------------------------------------------------------

## 1. Faithful structured synopsis of the reference

### 1.1 Metadata and page map

| part | pages | content |
|---|---|---|
| front | 1–5 | title, abstract (five result classes), TOC |
| §1 | 6–9 | problem (1.1); grades of rigour (Def 1.1); Rem 1.2; five-step skeleton; DIS parton picture; Fig 1 (dependency flowchart by grade), Fig 2 |
| §2 | 10–14 | light-cone conventions ($n\cdot\bar n=1$; refdoc $n$ = our $n_A$, refdoc $\bar n$ = our $n_B$); Lagrangian; Wilson lines (2.6)–(2.7) and the Fig 4 rule table; DIS/DY/$e^+e^-$ kinematics; Def 2.1 (PDFs), Def 2.2 (FF, $z^{d-3}/(4N_c)$, hadron frame); Rem 2.3; Prop 2.4 (support) |
| §3 | 14–27 | Landau (Thm 3.1), Coleman–Norton (Thm 3.2), Cor 3.4; Sudakov regions (Prop 3.5); power counting (Lemmas 3.7, 3.9, 3.10; Cor 3.8; Thm 3.12; Rem 3.13); collinear/soft approximation (3.10)–(3.11); Ward identity → Wilson line (Thm 3.14, "pure gauge" proof); Rem 3.15–3.16; Cor 3.17 |
| §4 | 28–32 | Thm 4.1 ($e^+e^-$ total, four parts (i)–(iv)); Prop 4.2 (cut sums); Rem 4.3; §4.3 limits |
| §5 | 32–39 | Lemma 5.1; OPE (5.2)–(5.6); Ex 5.2; Thm 5.3 (moments, conditional); Prop 5.4 (DGLAP ↔ OPE RG); Lemma 5.5; Thm 5.6 (weak $x$-space); Rem 5.7 |
| §6 | 39–45 | DIS graphical proof: Lemma 6.1, Prop 6.2, subtraction (6.3) with heuristics (P1)(P2), Thm 6.3, Rem 6.4–6.5, Thm 6.6, Rem 6.7–6.8, gluon PDF |
| §7 | 46–51 | one loop: Prop 7.1 (quark-in-quark PDF), Cor 7.2, Lemma 7.3, Prop 7.4 (coefficient functions), DY $q\bar q$ and universality |
| §8 | 51–55 | $e^+e^-\to hX$: Thm 8.1; Lemma 8.2; Cor 8.3; (8.2); Prop 8.4 (soft unitarity); Rem 8.5; Lemma 8.6; Rem 8.7 |
| §9 | 55–62 | DY: Thm 9.1 (grade B′); pole analysis; Lemma 9.2, Prop 9.3 (eikonal spectator model); Lemma 9.5; skeleton (G1)–(G6); §9.5 completeness; Rem 9.6 |
| §10 | 62–68 | TMD: modes (10.1); Ex 10.1; (10.2)–(10.4) = Collins (13.106); Thm 10.3; Prop 10.4 (CS); Cor 10.5 (CSS); (10.9); Thm 10.6 (Sivers via PT) |
| §11 | 68–72 | exclusive: Def 11.1; Thm 11.2 ($F_\pi$); Lemma 11.3 (colour transparency); ERBL (11.6); Thm 11.4 (CFS); DVCS; §11.3 endpoint failures |
| §12 | 72–76 | C/D cases: Conj 12.1 ($pp\to hX$/jets); (12.2) CdFR; Rem 12.2; Thm 12.3 (no TMD factorization in $pp\to h_1h_2X$); diffraction (12.3); NRQCD (12.4)–(12.5), Conj 12.5; DPS; small $x$ |
| §13 | 77–80 | SCET: (13.1); Thm 13.1 (BPS); Rem 13.2–13.3; thrust (13.3)–(13.4); three premises §13.3 |
| §14 | 80–82 | twist expansion (14.1) and TMC; renormalons (14.2)–(14.3); Prop 14.1; Rem 14.2; threshold (14.4); NLP |
| §15 | 83–86 | five lessons; status of the "three key links" (§15.1); **Table 1** (grades of all processes); list of what is not proven |
| App A | 86–87 | proof of Landau (Feynman parameters, $\eta_j=\alpha_j\partial_j\mathcal F$, envelope theorem); Rem A.1 |
| App B | 87–88 | plus distributions, LO and $d$-dimensional splitting functions, sum rules, Mellin table |
| App C | 88–127 | OPE (items C.1–C.70; Figs 54–62; Tables 2–3) |
| App D | 128–161 | precise subtraction (items D.1–D.48; Figs 63–70; Tables 4–6) |
| App E | 162–230 | Glauber cancellation in DY (items E.1–E.57; Figs 71–82; Tables 7–8) |
| refs | 231–238 | [1]–[145]; bibliographically accurate apart from minor title/erratum issues (R4 E15) |

### 1.2 Grading system, bridge hypothesis, the meaning of "proof"

**Definition 1.1 (pp. 6–7) and Table 1 caption (p. 84):**
- **A — non-perturbative structure theorem.** Rests only on Wightman-type properties plus existence of the OPE.
  - Perturbative OPE: Zimmermann (massive); massless QCD cited (Thm C.35).
  - Non-perturbatively: DIS moments for even $n\ge n_0$ under Ass. C.56–C.59 (Thm C.66); $n<n_0$ also needs C.60.
  - Members: $e^+e^-$ total; DIS moments; inclusive quarkonium decay "given NRQCD".
- **A\*** — "as rigorous as the OPE, given NRQCD as the EFT of QCD". Only quarkonium decay.
- **B — all-order perturbative proof "by the CSS standard".** The combinatorics (regions, Ward identities, subtractions) count as complete; general-graph power counting and contour deformation count as arguments.
  - App. D turns these into conditional theorems under Ass. D.7, D.14, D.27, D.37, D.43 (Thm D.46), plus a **bridge hypothesis**: the perturbative IR structure transfers to hadrons, and all $\Lambda$ sensitivity sits in hadronic matrix elements.
  - Members: collinear DIS and $e^+e^-\to hX$; thrust; TMD SIDIS and $e^+e^-\to h_1h_2X$; $F_\pi$ and $\gamma^*\gamma\pi$; DVCS and $\gamma_L^*p\to Mp$; diffractive DIS.
- **B′** — like B, but one step (the DY Glauber cancellation) rests on App. E (Ass. E.18, E.33, E.34, E.44).
  - "Only one graph class is completely proven" (Rem E.52).
  - Members: DY collinear and TMD; double DY ("in the CSS sense only").
- **C** — conjecture *or* partial proof (mixes our [P] and [C]). Members: $pp\to hX$, $pp\to$ jets, NRQCD production, $B\to\pi$, $B\to\pi\pi$.
- **D** — proven broken. Members: TMD $pp\to h_1h_2X$; hadron-collider hard diffraction; gap/non-global $pp$ observables; space-like strict collinear factorization (amplitude level).

**Remark 1.2 (p. 8).** B proofs are perturbative. The remainder of (1.1) is undefined within PT (asymptotic series; IR renormalons cancel against power-correction ambiguities, shown only at large $\beta_0$). The precise content is: "at every order in $\alpha_s$ and at leading power in $\Lambda/Q$ an equality holds". In App. D language: partonic, order by order, remainder $O(\lambda^aL^K)$, $L=\ln(1/\lambda)$, with $a>0$ possibly small (typically $a=\beta_R/3$).

**Five-step skeleton (§1.3, p. 8):**
1. Landau + Coleman–Norton give reduced diagrams $H,J_i,S$.
2. Power counting: one physical parton plus any number of longitudinal ($A^+$) gluons per jet; soft lines on jets by gluons only; nothing soft on $H$.
3. Approximations; overlaps need subtractions.
4. Ward identities give Wilson lines.
5. Unitarity sets $S=1$ (collinear) or combines $S$ into TMDs; Collins subtraction yields (1.1).

For hadron–hadron collisions the Glauber region must be handled before step 3.

### 1.3 Register of the reference's numbered assumptions and conditions

| label | page | content (one line) | status claimed by the reference |
|---|---|---|---|
| C.24 | 99–100 | momentum-space remainder estimate for the frozen-$q$ bilocal normal product: $\vert h\vert \le K\vert q\vert ^{D-1-a}\ln^k\vert q\vert $ uniformly in direction, compact $p$, for all $\partial_p$, $p\cdot$, $m\partial_m$ images | input ("no verbatim proof in the literature") |
| (B1)(B2) of Prop C.44 | 110–111 | BRST-symmetric renormalized insertions with classical coefficients and Ward identities; remainder of Thm C.35 also with $s\phi$ insertions | conditions ("not found verbatim") |
| forward remainder (Rem C.37, Prop C.54(a)) | 107, 116 | OPE remainder for forward on-shell massless partonic matrix elements (exceptional momenta) | assumption |
| C.56 (W1)–(W4) | 118 | Wightman QCD with GI composites, conserved $J$, parity; spectrum condition in the $B=1$ sector with isolated nucleon mass; tempered forward matrix elements; covariant retarded extension | assumption ((W2) incorrect as stated, R5 E3) |
| C.57 | 118–119 | GI operator families graded by dimension; twist-2 = $O_q,O_g$; RG with triangular mixing; asymptotic $\beta,\gamma$; PDF light-ray operators exist with moments $A_i^{(n)}$ | assumption |
| C.58 | 119 | non-perturbative OPE (O1) for vacuum and all hadrons, uniform with derivative bounds; covariant coefficients; chiral suppression of odd-twist coefficients | assumption |
| C.59 | 119 | precise asymptotic freedom: $\tilde C_i(q;\vert q\vert )=\vert q\vert ^{2-d_i}[\sum_kc_{i,k}(\hat q)\alpha_s(\vert q\vert )^k+O(\alpha_s^{K+1})]$ with $\overline{\rm MS}$ coefficients | assumption |
| C.60 | 119 | $\lim_{y\to\infty}T_2(iy)/(iy)=0$ | assumption (only for $n<n_0$) |
| (H1)–(H3) (Def D.9) | 134 | Collins conditions: accuracy of $T_{R_0}$ on $X_{R_0}$; suppression of subtraction terms of non-smaller regions on $U_{R_0}$; integrability of $\Gamma$ and every $C_R\Gamma$ | conditions of Thm D.10 |
| D.7 (A1)–(A4) | 133–134 | (A1) contour (homotopy crosses no singularity; meromorphy in $\epsilon$); (A2) meet-closure; (A3) power-counting envelopes $\Phi_{R_0}$ with $\int\Phi\le CL^K$ (pointwise boost bound (iii)); (A4) separation: Łojasiewicz-type $\vert l^2-M^2\vert \ge ct_R^2$, $\vert l^+\vert \ge ct_R$ on changed jet lines, no-Glauber $\vert k^+k^-\vert \ge c\vert \mathbf k_T\vert ^2$ and $\vert \tilde D\vert \ge c(\vert p^+\vert \vert k^-\vert +v_A(p))$ | assumption ((A2) is a choice) |
| D.14 | 137 | (H1)–(H3) hold for every integrand of the process | assumption (= Collins' power-counting claim) |
| D.17 | 138 | a linear rule for values of single (divergent) chain terms with (D1) compatibility and (D2) scaleless = 0 | convention/assumption |
| D.27 | 144–145 | cut-summed representation (LCPT): common domain and integrand (X1); approximators act (X2); event-shape density (X3) | assumption |
| D.31 | 146–147 | DY Glauber cancellation: (G-a) weak equivalence to a one-sided form; (G-b) one-sidedness; (G-c) contour clauses and compatibility | partly proven in App. E |
| D.34 (T1)–(T4) | 147–148 | TMD: $k_T$ tails; asymptotic linearity of $\ln\tilde S$ and $\ln\tilde f^{\rm unsub}$ with equal slope $\tilde K$; $b$-space multiplicative renormalization; $y_B\to-\infty$ under the integral | assumption |
| D.37 (W1)(W2) | 149 | product structure of Ward identities on approximated integrands; regrouping of subtractions | assumption |
| D.39 (E1)–(E3) | 150–151 | exclusive endpoint conditions on partonic subgraphs; hard kernel at most $1/x$; endpoint region suppressed | assumption |
| D.41 (U1)(U2) | 152 | integrand-level BPHZ(L) renormalization; $T_R$ commutes with $t_\gamma$ up to finite local terms | assumption ((U2) proven in two cases; (U1) imprecise, R6 E6) |
| D.43 (Z1)–(Z3) | 152–153 | multiplicative renormalization in moment space; a Ward-identity-preserving IR regulator for partonic targets; DR-IR targets give the same $\hat{\mathsf H}^{\rm bare}$ | assumption ((Z2) a genuine input) |
| E.18 | 181 | LCOPT applicability: (i) zero modes/endpoints absent at LP; (ii) instantaneous-loop values; (iii) Hermiticity of cut rules | assumption ((iii) provable, R7 E7) |
| E.33 | 198 | Glauber–soft mixing: (a) smoothness of external factors; (b) cut compatibility of $S$; (c1) fixed localization order for non-commuting insertions; (c2) cancellation in the complete graph set | assumption ((c1) inconsistent, R8 E1) |
| E.34 | 200 | power-counting envelope for fibre integrals | assumption |
| E.44 | 210–211 | (a) deformation target for general configurations; (b) compatibility with the set algebra $\mathfrak B$; (c) (H1)(H2) on the soft-angle region; (d) H-emission endpoints | assumption ((b)(c) needed even for abelian $\mathcal G_0$) |

### 1.4 Main text: theorems, statements and proof architecture

**§2 conventions and definitions.**
- (2.1)–(2.4): $v^\pm=(v^0\pm v^3)/\sqrt2$; $n=(1,0,0_T)$, $\bar n=(0,1,0_T)$, $n\cdot\bar n=1$; boosts; $\mathcal P_+=\frac12\gamma^-\gamma^+$; good components scale as $e^{y/2}$.
- (2.6): $W_{\mathcal C}[x,y]=\mathcal P\exp(ig\int_{y\to x}dz\cdot A)$, identical to CONTEXT.
- (2.7): $W^{(\pm)}_v(x)=\mathcal P\exp(-ig\int_0^{\pm\infty}d\lambda\,v\cdot A(x+\lambda v))=W[x,\pm\infty v]$.
- Fig 4: rules "vertex $igv^\mu t^a$, propagator $i/(v\cdot k\pm i0)$, ± future/past" — ambiguous, see ERR-M4.
- (2.8)–(2.10): $W^{\mu\nu}$, $T^{\mu\nu}$, ${\rm Im}\,T=2\pi W$, LO DY (all verified).
- **Def 2.1** (unrenormalized PDFs): quark identical to CONTEXT; gluon with $F^{+j}$ and an adjoint line.
- **Def 2.2** (FF): $d_{h/q}(z)=\frac{z^{d-3}}{4N_c}\sum_X\int\frac{dw^-}{2\pi}e^{ik^+w^-}{\rm Tr}[\gamma^+\langle0|W^{(+)\dagger}_{\bar n}\psi(w)|hX\rangle\langle hX|\bar\psi W^{(+)}_{\bar n}(0)|0\rangle]$, hadron frame. **Correct** (verified at $O(\alpha_s)$).
- **Prop 2.4** (support): $|\xi|\le1$; $f_q(\xi)=-f_{\bar q}(-\xi)$ for $\xi<0$. Proof: light-cone gauge state sum with $P_X^+\ge0$; antiquark part via the anticommutator; Jaffe's pole argument as an alternative. Formal (ERR-m4).

**§3 IR structure.**
- **Thm 3.1** (Landau): necessary conditions $\alpha_jD_j=0$, $\sum_{j\in a}\alpha_j\varepsilon_{aj}l_j=0$, proof in App A. It conflates the parameter-space and momentum-space theorems (ERR-M3).
- **Thm 3.2** (Coleman–Norton): one-to-one with classical processes.
- **Cor 3.4**: "no pinch in the Euclidean region" — false (ERR-M1).
- **Prop 3.5**: four Sudakov regions with $1/\epsilon^2$ coefficients $(1,-1,-1,1)$, fixed by $\mu$-independence. The double log is $(a-b)^2=\ln^2(Q^2/m^2)$; the constant $\pi^2/3$ is omitted.
- **(3.7)** mode table: hard, collinear, soft$=\lambda^2$ (our ultrasoft), Glauber $(\lambda^2,\lambda^2,\lambda)$. **Fig 10** shows the modes in exponent space.
- **Lemma 3.7**: $p_J=n_F+n_T+2n_--c_J$, by boost + dimension.
- **Cor 3.8**: leading connections — omits super-leading cases (ERR-S4).
- **Lemma 3.9**: $p_S=2E_H^B+3E_H^F+E_J^F$.
- **Lemma 3.10**: Glauber is $\lambda^0$.
- **Thm 3.12**: leading regions for DIS ($|x|>1$), $e^+e^-\to hX$, DY.
- **Rem 3.13**: power counting gives scaling statements, not bounds; the integral version is Ass. D.7.
- **(3.10)–(3.11)**: collinear K-projection $H_\mu(\hat k)\frac{\hat k^\mu\bar n_\nu}{\bar n\cdot k}J^\nu$ (no $i0$); soft $\frac{n^\mu k_\nu}{n\cdot k\pm i0}$.
- **Thm 3.14** (decoupling of longitudinal gluons). "Pure-gauge" proof:
  1. $\mathcal A_{\rm eff}=n^\mu\mathcal A(y^-)$ has $F_{\mu\nu}=0$, so $\mathcal A_{\rm eff}=-\frac ig(\partial U)U^\dagger$;
  2. background-gauge covariance gives $\psi\to U^\dagger\psi$, with Slavnov–Taylor identities cited for the non-abelian identity;
  3. expansion gives eikonal factors.
  Complete only for abelian/tree-level $H$ (ERR-M6).
- **Rem 3.15**: base point irrelevant for collinear PDFs, since $W[w,\pm\infty]W[\pm\infty,0]=W[w,0]$; relevant for TMDs.
- **(3.15)/Fig 16**: telescoping Ward identity.
- **Cor 3.17**: soft Wilson lines; (3.16) is schematic (ERR-M7).

**§4 Thm 4.1, $e^+e^-$ total cross section, with four logically separate parts.**
- (i) Wightman-level analyticity, ${\rm Im}\,\Pi\ge0$, once-subtracted dispersion relation at a Euclidean point iff $\int\rho/s^2<\infty$ (⟺ finite Adler function).
- (ii) IR finite at every order; polynomial in $\ln(s/\mu^2)$; $R=N_c\sum e_q^2[1+a+(1.9857-0.1153n_f)a^2]$. Proof: no Euclidean pinch + Lowenstein–Zimmermann IR power counting, RG (degree $n-1$), continuation $L\to\ln(s/\mu^2)-i\pi$.
- (iii) OPE power corrections, no $1/Q^2$ term (conditional on C.56–C.59).
- (iv) PQW smearing identity $\bar R(s,\Delta)=12\pi\,{\rm Im}\,\Pi(s+i\Delta)$. Exact; computability requires the OPE at complex $q^2$.

Prop 4.2 (cut-sum IR finiteness): a sketch via unitarity/Disc of the forward $J\otimes S$ function, Fig 19.

**§5 DIS via the OPE.**
- **Lemma 5.1**: cut-plane analyticity of $T_{1,2}(\omega)$, crossing ($T_1$ even, $T_2$ odd), Disc $=4\pi iF_i$.
- (5.2)–(5.6): OPE tensor structure and twist-2 operators; $T_2=4\sum\omega^{n-1}CA$, stated to be formal.
- **Ex 5.2**: tree OPE $T_2=4e_q^2\omega/(1-\omega^2)$.
- **Thm 5.3**: for even $n\ge n_0$ ($Q$-independent), $M_2^{(n)}=\sum_iC^{(n)}_{2,i}A^{(n)}_i+O(\Lambda^2/Q^2)$ under C.56–C.59; all even $n\ge2$ with C.60. (5.8) identifies light-ray moments with local operators by integration by parts.
- **Prop 5.4**: DGLAP ⟺ OPE RG with a single kernel — wrong beyond LO (ERR-M10).
- **Lemma 5.5**: even-moment uniqueness via $y=x^2$ (correct for $L^1$).
- **Thm 5.6**: weak $x$-space factorization under condition (Φ).
- **Rem 5.7**: the coefficient of $1/Q^2$ grows like $n$; heuristically $O(1/(Q^2(1-x)))$; failure at $W^2\sim\Lambda^2$.

**§6 DIS graphical.**
- **Lemma 6.1** (Clifford projection $\frac14{\rm Tr}[H\gamma^-]{\rm Tr}[\gamma^+J]$).
- **Prop 6.2** ($\int\frac{d\xi}{\xi}\hat H(\xi P)f(\xi)$; normalization chain verified; colour projection missing).
- Subtraction (6.3) $C_R\Gamma=T_R(\Gamma-\sum_{R'<R}C_{R'}\Gamma)$ with heuristics:
  - (P1) accuracy for the combination;
  - (P2) suppression of whole subtraction terms.
- **Thm 6.3**: under the contour condition + (H1)–(H3), $\Gamma=\sum C_R\Gamma+O(\lambda^aL^K)$. Proof: $r=(1-T_{R_0})X_{R_0}-\sum_{R\not\le R_0}C_R\Gamma$ on covering sets $U_{R_0}$.
- **Rem 6.4**: naive termwise induction fails.
- **Thm 6.6** (DIS collinear factorization, conditional on D.7, D.14, D.27, D.41, D.43 + bridge), in four steps:
  1. unphysical region $|\omega|<1$;
  2. $\overline{\rm MS}$;
  3. partonic inversion (6.6);
  4. continuation.
  Key warning: real-segment bounds do not continue to the discontinuity. Two routes: Cauchy estimates for moments, or direct cut-graph analysis.
- Rem 6.7: the current jet merges into $H$; the endpoint $\xi\to x$ gives the plus distributions.
- §6.4: gluon PDF from $k^+A^j-k^jA^+$.
- Rem 6.8: light-cone gauge pitfalls.

**§7 one loop.**
- **Prop 7.1**: real part $\frac{\alpha_sC_F}{2\pi}[\frac{1+\xi^2}{1-\xi}-\epsilon(1-\xi)]\frac{(4\pi\mu^2)^\epsilon}{\Gamma(1-\epsilon)}\int\frac{dk_T^2}{k_T^{2+2\epsilon}}$: ladder $(1-\epsilon)(1-\xi)$, Wilson graphs $2\xi/(1-\xi)$; the virtual part is fixed by a sum rule (not computed). Result: $Z_{qq}=\delta+\frac{a_s}{\hat\epsilon}P^{(0)}_{qq}$.
- **Cor 7.2**: DGLAP from operator renormalization.
- **Lemma 7.3**: initial-state collinear limit with $\hat P_{qq}(z,\epsilon)$.
- **Prop 7.4**: $c_q$, $C_{2,g}$ (finite parts quoted, verified against c_dis).
- (7.8): DY $q\bar q$ coefficient $c_q^{\rm DY}$; the pole is the sum of two PDF poles (one-loop universality, "not a proof").

**§8 $e^+e^-\to hX$.**
- **Thm 8.1** (conditional on D.7, D.14, D.27, D.37, D.41 and a D.43-type assumption for FFs, since FF moments are not local operators).
- **Lemma 8.2**: final-state jet lines have their $k^+$ poles on one side.
- **Cor 8.3**: a single soft momentum can be deformed so that $|k^+k^-|\gtrsim k_T^2$, but only with $\kappa\sim k_T^2/|k^-|$ because of the soft line's own pole.
- (8.2) soft factor with future lines.
- **Prop 8.4**: $\int S=\langle0|\mathcal U^\dagger\mathcal U|0\rangle=1$ via $d\mathcal U/dt=igB\mathcal U$; DR scalelessness.
- Rem 8.5: when $S\neq1$.
- **Lemma 8.6**: unobserved-jet sum rule, by three arguments (light-cone Källén–Lehmann, DR boost scalelessness, deformation).
- Rem 8.7: FF universality (Collins–Metz).

**§9 DY (B′).**
- **Thm 9.1** with skeleton (G1)–(G6):
  - (G1) LCPT;
  - (G2) cut sum of FSI;
  - (G3) deformation — needs both $k^\pm$, since one component leaves $|k^+k^-|\sim\lambda^3$;
  - (G4) eikonal + Ward → past lines;
  - (G5) soft unitarity (past);
  - (G6) $W[w,-\infty]W[-\infty,0]=W[w^-,0]$.
- Pole analysis: spectator pole in the UHP, active pole in the LHP.
- **Lemma 9.2** (eikonal phase $\mathcal V=\mathcal P\exp(i\chi T_A\otimes T_B)$; abelian proven).
- **Prop 9.3** (spectator FSI cancel after $\int d^2s_T$; non-abelian $N\ge2$ claimed not to cancel within the model — wrong, ERR-S1).
- **Lemma 9.5**: initial-state poles on one side; eikonal $1/(\bar n\cdot k-i0)$ → past-pointing.
- §9.5: complete only for $\mathcal G_0$ (Rem E.52). NNLO/N³LO test only collinear-pole universality (no hadron spectators); DFT is outside the premises.

**§10 TMD.**
- (10.1) modes $(1,\lambda^2,\lambda),(\lambda^2,1,\lambda),(\lambda,\lambda,\lambda)$.
- **Ex 10.1**: rapidity divergence $f^{(1)}\supset\frac{\alpha_sC_F}{\pi^2}\frac{\xi}{(1-\xi)\mathbf k_T^2}$ (verified).
- **Def 10.2** = Collins (13.106); $\zeta_A\zeta_B=Q^4$.
- **Thm 10.3** (B for SIDIS and $e^+e^-\to h_1h_2X$, B′ for DY). Its proof's subtraction formula is degenerate as printed (ERR-M15); the W+Y uniformity claim is unqualified (ERR-M16).
- **Prop 10.4** (CS equations from boost invariance + asymptotic linearity $\ln\tilde S=a+(y_1-y_2)c$ + integrability; one-loop $\tilde K$, $\gamma_K$).
- **Cor 10.5** (CSS solution).
- **Thm 10.6**: Sivers sign reversal from PT invariance (valid for any $\theta$, since the $\theta$ term is C-even + CPT); full matrix-element proof; $f_1^{[+]}=f_1^{[-]}$.

**§11 exclusive.**
- Def 11.1 (pion DA, $f_\pi\simeq130.4$ MeV).
- **Thm 11.2** ($F_\pi=\int\phi^*T_H\phi$, $T_H=\frac{16\pi C_F\alpha_s}{Q^2}\frac{f_\pi^2}{8N_c}\frac1{\bar x\bar y}$, $Q^2F_\pi\to8\pi\alpha_sf_\pi^2\approx0.15$ GeV², conditional on the endpoint condition; remainder missing a log, ERR-m15).
- **Lemma 11.3**: $W_n(b_1)W_n^\dagger(b_2)=1+O(b\Lambda)$ on singlets.
- ERBL (11.6) with the 50/81 exponent.
- **Thm 11.4** (CFS, $\gamma_L^*$; the transverse-photon mechanism is mischaracterized, ERR-M17).
- DVCS (Ji, Radyushkin, Collins–Freund).
- §11.3: endpoint failures — twist-3 $F_\pi$, $B\to\pi$ soft overlap, BBNS, Landshoff with Sudakov suppression, Liu–Neubert refactorization.

**§12 C/D.**
- **Conj 12.1**: $pp\to hX$/jets.
- (12.2): CdFR $i\pi\mathbf T_{\rm coll}\cdot\mathbf T_j/\epsilon$ ($\mathbf T_{\rm coll}$ undefined).
- Rem 12.2: SLLs.
- **Thm 12.3**: no TMD factorization in $pp\to h_1h_2X$ (colour argument wrong; CQ/RM misdescribed, ERR-S2, ERR-M18).
- Diffractive DIS (12.3) B vs hadron-collider diffraction D.
- NRQCD: decay A\* (over-claim), production Conj 12.5 (nonstandard statement; NQS misreported).
- DPS B′ (CSS sense); small $x$ ≈ C.

**§13 SCET.**
- **Thm 13.1** (BPS decoupling, correct algebraic proof).
- Rem 13.2 (Jacobian 1; direction of $Y_n$ — imprecise).
- Thrust (13.3)–(13.4).
- §13.3: "SCET proofs are not more rigorous than Collins'". Its three premises:
  - mode completeness ↔ leading regions;
  - zero-bin ↔ subtraction;
  - Glauber ↔ Glauber cancellation.

**§14.**
- (14.1) twist-4 + TMC coefficient $\frac{n(n-1)}{n+2}\frac{M^2}{Q^2}a_{n+2}$ (verified).
- (14.2)–(14.3): large-order behaviour and renormalon ambiguity $(\Lambda^2/Q^2)^p$.
- **Prop 14.1** (renormalon ↔ twist-4 at large $\beta_0$; only an argument).
- Rem 14.2 (thrust shift $2\Omega_1/Q$; DY $1/Q^2$).
- (14.4): threshold refactorization as a nested factorization whose rigour is bounded by the outer one.
- NLP: LBK, endpoint rearrangement.

**§15 Table 1** (p. 84):

| process | grade | key step / failure |
|---|---|---|
| $e^+e^-$ total; DIS moments | A | analyticity, unitarity, OPE |
| DIS ($x$); $e^+e^-\to hX$; thrust; SIDIS and $e^+e^-\to h_1h_2X$ (TMD); $\pi$ FF, $\gamma^*\gamma\pi$; DVCS, $\gamma_L^*p\to Mp$; DDIS | B | — |
| DY collinear and TMD; double DY | B′ | Glauber |
| quarkonium decay | A\* | — |
| $B\to\pi$, $B\to\pi\pi$; $pp\to hX$/jets; NRQCD production | C | — |
| $pp\to h_1h_2X$ (TMD); hard diffraction; gap observables | D | — |

The list of what is not proven (p. 86) ends with the bridging assumption.

### 1.5 Appendices A and B (pp. 86–88)

**App A** proves Thm 3.1 at the level of Eden–Landshoff–Olive–Polkinghorne (ELOP). The steps:
1. Feynman parameters: $I\propto\int\delta(1-\sum\alpha)\,\mathcal U^{N-(L+1)d/2}/[\mathcal F-i0\,\mathcal U]^{N-Ld/2}$, with the stationary point (A.1) $\sum_j\alpha_j\varepsilon_{aj}l_j(k_0)=0$.
2. Deformation $\alpha_j\to\alpha_j-i\epsilon\eta_j$ with $\eta_j=\alpha_j\partial_j\mathcal F$, so that ${\rm Im}\,\mathcal F=-\epsilon\sum\alpha_j(\partial_j\mathcal F)^2$. It fails iff $\alpha_j=0$ or $\partial_j\mathcal F=0$ for each $j$ (A.2).
3. Envelope theorem $\partial_j(-\mathcal F/\mathcal U)=D_j(k_0)$; homogeneity; projective contour.

Rem A.1 lists two honest caveats: $\mathcal U=0$ (second-type singularities), and the gluing of local deformations into a global one (Pham). It omits Coleman–Norton.

**App B**:
- (B.1): test-function class for $[\,]_+$ (bounded, Lipschitz at 1).
- (B.2): $(1-z)^{-1-\epsilon}=-\frac1\epsilon\delta+[\frac1{1-z}]_+-\epsilon[\frac{\ln(1-z)}{1-z}]_++\dots$
- (B.3)–(B.6): LO kernels and sum rules.
- (B.7): $d$-dimensional $\hat P_{ij}$ (gluon average over $d-2$).
- (B.8): Mellin table.

All verified (R4, R5).

### 1.6 Appendix C (pp. 88–127): the OPE — perturbative proof, non-perturbative assumptions, conditional theorems

**Aim (pp. 88–89, Fig 54 dependency diagram: proved / cited / assumed).** Split "the OPE has been proven" into checkable statements; prove what can be proven; make the rest numbered assumptions; prove Thm 5.3 under them.

**§C.1 — the statement needed by §5.**
- **Def C.1** has five parts:
  - (O1): $T^{\mu\nu}=\sum_{d_j\le N}\tilde C_j^{\mu\nu}(q;\mu)\langle P|O_j|P\rangle+O(|q|^{1-N}\ln^k|q|)$, Euclidean and direction-uniform;
  - (O2): gauge-invariant operators only;
  - (O3): $t_n=4\sum C^{(n)}_{2,i}A^{(n)}_i+O(Q^{-2}\ln^k)$;
  - (O4): RG;
  - (O5): $t_n=4\int_{[0,1]}x^{n-2}F_2$ for even $n\ge n_0$, $F_2dx$ a positive measure.
- **Rem C.2**: a moment needs one Taylor coefficient $t_n$, not the all-spin sum. The OPE informs only on $|\omega|\le\sqrt3M/Q$.
- **Rem C.3**: partonic structure functions are not positive measures, so the positivity argument is non-perturbative only.

**§C.2–C.4 — BPHZ machinery.** Massive Euclidean scalar/Yukawa models.
- **Defs C.4–C.7**: graphs, $\omega(\gamma)=4L+\sum(2d_\ell-4)+\sum\delta_v$, forests, $R_\Gamma$, Bogoliubov recursion.
- **Thm C.8** (Zimmermann convergence, cited): vertex-additive oversubtraction degrees $\delta(\gamma)=\omega(\gamma)+\sum_{v\in\gamma}c_v$.
- **Rem C.9**: a counterexample showing that $\delta\ge\omega$ alone is insufficient.
- **Def C.10**: normal products $N_a[O]$.
- **Lemma C.11**: contraction and bridges.
- **Lemma C.12** (chain expansion): one combinatorial identity (C.11) generating both
  - **Thm C.13** (Zimmermann identity $N_a[O]=N_{a'}[O]+\sum u_{O'}N_{a'}[O']$), and
  - the OPE identity.
- **Cor C.14** ($N_a[O]=\sum z_{OO'}N[O']$).
- **Ex C.15** (Callan–Symanzik).
- **Thm C.17** (Weinberg, cited).
- **Cor C.18** ($\alpha(L)\le\max\omega$).

**§C.5 — OPE at every order (massive model).**
- AB parts (Def C.19).
- Two subtractions (Def C.21):
  - the T-product ($q$ external);
  - the **frozen-$q$ bilocal normal product** $N_a[A(x)B(0)]$, with Taylor subtraction in $p$ only.
- **Lemma C.22**: chain decomposition; every term absolutely integrable.
- **Lemma C.23**: contact terms.
- **Ass C.24**: momentum-space remainder.
- **Thm C.25**, in four parts:
  - (i) unconditional exact OPE identity $\tilde G^T=\sum_{d_O\le a}\tilde C_O(q)\tilde G_{N[O]}+\tilde N_a$ with absolutely convergent hard coefficients;
  - (ii)–(iv), given C.24: derivative bounds; uniqueness; scaling $|\tilde C_O|\le K|q|^{D-d_O}\ln^k$ of *reduced* coefficients (false for unreduced ones, Ex C.27).
- **Ex C.26**: the tree OPE is the Taylor expansion of $\varphi(x)$.
- **Rem C.28**: heuristic origin of the exponent.
- **Lemma C.29**: $q$-derivative bounds from homogeneity, $O(4)$ and the Lagrange identity.
- **Lemma C.30**: order-by-order uniqueness.
- **Lemma C.32 / Cor C.33**: dyadic momentum → coordinate remainder.
- **Rem C.34**: unidentified polynomial terms.

**§C.6 — massless QCD.**
- BPHZL vs DR+$R^*$.
- **Thm C.35** (cited): massless QCD OPE at Euclidean non-exceptional momenta, with a basis including gauge-variant and ghost operators; coefficients $|q|^{D-d_O}\times$ polynomial in $\ln$.
- **Lemma C.36**: exact uniqueness from the log-polynomial structure.
- **Rem C.37**: forward on-shell kinematics are *exceptional* — no all-order remainder proof.
- BRST (C.26)–(C.28).
- **Lemma C.39** (local BRST cohomology, cited).
- **Thm C.40** (Joglekar–Lee, cited + sketch).
- **Lemma C.41**: aliens vanish between physical states, "including forward" — over-claim, ERR-M24.
- **Lemma C.42** (twist-2 GI classification by collinear twist $t=d-h$; table $\psi_+:1$, $\psi_-:2$, $D^+:0$, $D^j:1$, $D^-:2$, $F^{+j}:1$, $F^{+-},F^{ij}:2$, $F^{-j}:3$).
- **Lemma C.43**: twist parity = chirality, for symmetric traceless operators.
- **Prop C.44**: (O2) in PT under (B1)(B2).
- **Prop C.46**: coefficient RG *derived* from uniqueness.

**§C.7 — from the local OPE to moments.**
- (C.31): Euclidean $q$ with $|\mathbf q|\ge Q/2$ gives $\omega\in\mathcal I_Q=\{iy:|y|\le\sqrt3M/Q\}$.
- **Lemma C.47**: the OPE on the segment gives an odd polynomial $\mathcal P_N$ with $\sup_{\mathcal I_Q}|T_2-\mathcal P_N|\le K(M/Q)^{N-2}\ln^k$ and $\pi_n=4\sum CA+O(\frac{M^2+mM}{Q^2}\ln^k)$.
- **Rem C.48**: chiral suppression; odd twist vanishes in massless PT by $\gamma$-parity; non-perturbatively an input.
- **Lemma C.49**: Markov coefficient inequality.
- **Thm C.50** (fixed-$n$ Taylor coefficients). Given:
  - Lemma C.47 for all $N$;
  - $T_2$ analytic and odd in $|\omega|<1$;
  - $F_2dx\ge0$;
  - a $Q$-independent $n_0$ with $t_n=4\int x^{n-2}F_2$ for $n\ge n_0$.

  Then $t_n=4\sum CA+O(\frac{M^2+mM}{Q^2}\ln^kQ)$ for **every** even $n\ge2$. The proof uses three ingredients:
  - the positivity tail $0\le t_{n'}\le t_{n_0}$;
  - Markov on $\mathcal I_Q$;
  - a bootstrap bound on $t_{n_0}$.

  No spin sum is needed.
- **Lemma C.51 / Cor C.52**: weak $x$-space convergence under (Φ); a pointwise $O(1/Q^2)$ is impossible.
- **Rem C.53**: existence of $\Phi_Q$ is a Hausdorff problem.
- **Prop C.54**: fixed-order all-spin sum for on-shell partons in DR, under the forward remainder assumption.
- **Rem C.55**: amplitude form.

**§C.8 — non-perturbative layer.**
- Obstacles: no 4D YM construction; composite fields; non-summability.
- **Ass C.56–C.60** (table §1.3).
- **Rem C.61** (Bostelmann; instantons $(\Lambda/Q)^{11-2n_f/3}$), **Rem C.62** (vacuum OPE: no $1/Q^2$).
- **Lemma C.63**: entire $f$ with $|f|\le C(1+|z|)^A|{\rm Im}\,z|^{-B}$ is a polynomial (Jensen).
- **Lemma C.64** (finite-subtraction dispersion relation from C.56), in four parts:
  - (a) cut-plane analyticity, oddness;
  - (b) $|T_2|\le C_Q(1+|\omega|)^A|{\rm Im}\,\omega|^{-B}$ with **$Q$-independent** $A,B$;
  - (c) ${\rm Disc}\,T_2=4\pi i\nu_Q$, $\nu_Q\ge0$;
  - (d) $T_2=\sum_{n<n_0}t_n\omega^{n-1}+4\omega^{n_0-1}\int x^{n_0-2}F_2/(1-x^2\omega^2)$ for even $n_0>A+2$.

  Proof: forward-tube holomorphy with Vladimirov bounds; invariant theory at $\hat P=0$; edge of the wedge; positivity by $Q^2$-smearing; almost-analytic extension + Green's formula; Lemma C.63.
- **Rem C.65**: low sum rules ($2\le n<n_0$, incl. the momentum sum rule) hold **iff** $T_2(iy)=o(y)$; Regge behaviour is neither equivalent nor sufficient.
- **Thm C.66** (non-perturbative moment theorem):
  - (i) RG-defined coefficients satisfy the OPE at every $\mu$, with asymptotically free $C(1,\alpha_s(Q))$;
  - (ii) $M_2^{(n)}=\sum CA+O(\Lambda_h^2Q^{-2}\ln^kQ)$ for even $n\ge n_0$ under C.56–C.59; for all even $n\ge2$ with C.60;
  - (iii) weak $x$-space under (Φ).
- **Rem C.67**: the practical (SVZ) cutoff OPE is routing-dependent and gauge-breaking.
- **Prop C.68**: rearrangement freedom $O_i'=O_i+\sum\kappa_{ij}\Lambda^{d_i-d_j}O_j$. Twist-2 coefficients are meaningful only up to $O(\Lambda^2/Q^2)$ unless normalized non-perturbatively; asymptotic expansions are unchanged.
- **Rem C.69**: renormalon absorption has two conjectural ingredients.
- Supporting results: Hollands–Kopper, Fröb–Holland–Hollands, Mack, PRER, Bostelmann, Hollands–Wald, Gross–Neveu.

**§C.9.** Rem C.70; status Tables 2 (PT) and 3 (moments, non-perturbative), with "theorem / cited / input / assumption / conjecture" per claim.

### 1.7 Appendix D (pp. 128–161): the precise form of Collins' subtraction method

**§D.1 — why naive induction fails** (Ex D.1, off-shell triangle (3.3), $p_1=(P,-m^2/2P,0)$, $p_2=(m^2/2P',-P',0)$; approximants $T_S,T_{C_1},T_{C_2},T_H$ on $(D_1,D_2)$, (D.2)):
- (a) $T_{C_2}\Gamma$ is not suppressed in $C_1$, not even integrable (massless collinear pinch); only $C_{C_2}\Gamma=T_{C_2}(\Gamma-T_S\Gamma)$ is.
- (b) $T_{C_1}$ must be accurate on the subtraction term $T_S\Gamma$.
- (c) Single chain terms such as $T_{C_1}\Gamma$ are not absolutely integrable for **any** $\epsilon$ (rapidity end needs $\epsilon<0$, UV end needs $\epsilon>0$).

Lessons: accuracy on $X_{R_0}$; suppression of whole subtraction terms; integrability only of grouped expressions; $\lambda$-dependent neighbourhoods; contour; UV.

**§D.2 — setup.**
- **Def D.2**: power suppression $F\in\mathfrak S(A)$ iff $\int_A|F|d\mu\le C\lambda^aL^K$ uniformly in $\lambda$ and $\epsilon$. It is an integral norm for two reasons: measurement thin layers, and the non-pointwise $\overline{\rm MS}$ counterterm cancellation.
- **Def D.3**: regions = per-line mode assignments ($S<A,B<H$); pinch sets $\pi_R$ are affine subspaces; per-line order and meet.
- **Lemma D.4**: $\pi_{R\wedge R'}=\pi_R\cap\pi_{R'}$.
- **Fig 63**: Hasse diagram of the 9 leading regions of the two-loop planar vertex (meet-closed; $(C_1,C_1)<(H,C_1)$).
- **Def D.5**: neighbourhoods $N_R=\{\sigma_{R(j)}(l_j)\le\lambda^{\beta_R}\}$, $U_R=N_R\setminus\cup_{R'<R}N_{R'}$, $\beta_R=3^{h(R)-h_*}$.
- **Lemma D.6**: covering.
- **Ass D.7**: (A1)–(A4).
- **Note D.8**: status of each.

**§D.3 — the precise subtraction theorem.**
- **Def D.9**: (H1)–(H3).
- **Thm D.10**: (A1)(a)+(H3)+(H1),(H2) for all $R_0$ ⇒ $\int_\Omega|\Gamma-\sum_RC_R\Gamma|\le C\lambda^aL^K$ uniformly. Proof: pointwise $r=(1-T_{R_0})X_{R_0}-\sum_{R\not\le R_0}C_R\Gamma$ on $U_{R_0}$, plus finite covering.
- **Lemma D.11**: chain expansion $C_R\Gamma=\sum_{\max c=R}(-1)^{|c|-1}T_c\Gamma$, $r=\mathcal O_{\mathcal R}\Gamma$.
- **Lemma D.12**: pairing decomposition via meets.
- **Cor D.13** (product formula): under (Com) and (Abs), $r=\prod_{\mathcal R}(1-T_R)\Gamma$ and (H1)(H2) ⟺ grouped power counting (D.14). Proof: Möbius/meet-irreducibles.
- **Ass D.14**: (H1)–(H3) for general graphs.
- **Rem D.15**: forest analogy — chains ↔ nested families only; overlaps handled via meets.
- **Prop D.16**: meromorphic + bounded ⇒ no pole at $\epsilon=0$.
- **Ass D.17**: values of chain terms.

**§D.4 — explicit approximators.**
- **Def D.18** (hard–collinear): $k\to\pi_+(k)=(\bar n\cdot k)n$; $\mathcal P_\pm$; $\mathcal P_A=g_T+n\otimes\bar n$ ($H_\mu J^\mu\to H^-J^+-\mathbf H_T\cdot\mathbf J_T$). No new denominators; the collinear-PDF Wilson-line prescription is irrelevant.
- **Def D.19** (soft): $k\to\pi_-(k)$ inside $J_A$; projection $n^\mu\bar n_\nu$; the $i0$ is inherited from $\tilde D=p^2-M^2+2p^+k^-+i0$.
- **Lemma D.20** (i0 compatibility and deformation amplitude), two parts:
  - (a) ${\rm Im}D,{\rm Im}\tilde D\ge0$ under $k^-\to k^-+i\eta\kappa$;
  - (b) the soft line's own pole limits $\kappa\sim k_T^2/|k^+|$, **not** $|k_T|$; opposite orientations give a Glauber pinch.
- **Def D.21** (TMD, rapidity-regularized $n_A(y_A)$, $n_B(y_B)$): order-of-limits subtlety $e^{2(y_B-y_k)}$.
- **Def D.22** (exclusive DA projector $\frac14\gamma^-\gamma_5{\rm Tr}[\gamma_5\gamma^+\cdot]\otimes\delta/N_c$).
- **Lemma D.23** (algebra): idempotence and (Com) for adapted routing. (Abs) fails exactly by the transverse coupling of a direction-flipping line; there is an edge case, ERR-m25.
- **Rem D.24**: no adapted routing in general.

**§D.5 — error terms.**
- **Lemma D.25 / Table 4**: rows 1–9 (hard–collinear line, masses, quark and gluon projections, soft line, soft polarization, TMD rapidity, exclusive, event-shape measurement). Pointwise relative vs envelope vs integral bounds; $\delta\le C\lambda^{\beta_R/3}$; soft row $(s_R/t_R)^{1/2}$ from (A4)(iii).
- **Telescoping (D.18)**.
- **Lemma D.26**: $(1-T_{R_0})\Gamma\in\mathfrak S(U_{R_0})$, i.e. (H1) for minimal $R_0$. Term-by-term stability fails.

**§D.6 — process propositions (each conditional on listed assumptions):**
- **Prop D.28** (DIS), three parts:
  - (a) unphysical forward amplitude — only A and H modes, $T=\sum C_RT+O$;
  - (b) moments need complex-$\omega$ uniformity; the Cauchy estimate gives $O(\rho^{-N}\lambda^aL^K)$;
  - (c) $x$ space at fixed $x<1$ under D.27; threshold breaks uniformity.
- **Prop D.29** ($e^+e^-\to hX$).
- **Prop D.30** (thrust; zero-bin scaleless by $k^+\to ak^+$, $k_T\to\sqrt ak_T$ ⇒ $a^{-\epsilon}$).
- **Ass D.31 / Prop D.32** (DY: Glauber input + disjoint-block proof of (D.19)).
- **Note D.33**.
- **Ass D.34**.
- **Prop D.35** (TMD window $c_0L\le Y\le c_1L$, $c_0>1+2a$, $|y_k|\le(1+a)L$).
- **Prop D.36** (zero-bin = soft factor), two parts:
  - (a) one-loop absorption $T_RT_{R'}=T_{R'}$ up to $e^{-2Y}p_B^+/p_B^-$;
  - (b) all orders under D.37: $\sum C_R\Gamma=[\mathsf H\tilde f_A^{\rm unsub}\tilde f_B^{\rm unsub}/\tilde S]^{[N]}$.
- **Lemma D.38**: the square root is an exact identity; CS equation from (T2).
- **Ass D.39 / Prop D.40** (exclusive): integrand-level colour-singlet soft cancellation — "dipole cancellation = smallness of the approximation error"; failure for twist-3 and transverse photons.

**§D.7 — UV and renormalization.**
- **Ass D.41**.
- **Prop D.42**: in DIS, $\sum C_R\Gamma=\hat{\mathsf H}_R\otimes\mathsf J_R^{\rm bare}$.
- **Ass D.43**: (Z2) is a genuine input — no on-shell gluon IR regulator preserving the Ward identities is known.
- **Thm D.44** (moment-space compatibility): $C=\hat{\mathsf H}^{\rm bare}Z$ is finite and target independent; recursion (D.25) $C^{[n]}=\lim_{\lambda\to0}[T^{[n]}-\sum_{m<n}C^{[m]}f^{{\rm ren}[n-m]}]$.

**§D.8–D.9 — assembly and examples.**
- **Thm D.46**: factorization structures for (a) DIS, $e^+e^-\to hX$; (b) thrust; (c) DY; (d) TMD; (e) exclusive.
- **Ex D.47** (complete one-loop triangle):
  - closed forms (D.26) and remainder (D.27);
  - $k^-$-residue forms (D.28);
  - absolutely convergent iterated integrals for $0<\epsilon<1$, with values (D.30)–(D.31);
  - $\sum=\frac1{\tilde Q^2}[\ln^2\frac{\tilde Q^2}{m^2}+\frac{\pi^2}3]$ (D.32);
  - zero-bin $=(\ldots)(\frac1{\epsilon_{\rm UV}}-\frac1{\epsilon_{\rm IR}})$ (D.33);
  - Table 5 numerics (the numbers are right; the table compares $I$ with the LP formula in $Q^2$, so it does not test the remainder — ERR-m25);
  - Figs 69 (Sudakov plane) and 70.
- **Ex D.48** (two-loop ladder): $r=\Delta\mathsf H_0\Delta K_2\Delta K_1$; $C_1\to\hat{\mathsf H}^{[1]}$; $C_H\to$ two-loop coefficient; grouping is necessary.

**§D.10.** Table 6: item-by-item status.

### 1.8 Appendix E (pp. 162–230): Glauber cancellation in inclusive DY

**Scope.** All orders of non-abelian PT. External hadrons are *colour-singlet perturbative models* (point-like splitting vertices); coloured external states are excluded (DFT). Collinear DY, and TMD DY measuring only the pair $q_T$.

**Architecture** (Fig 71):
1. LCOPT with one light-cone time per jet ($x^+$ for $J_A$, $x^-$ for $J_B$);
2. cut sums via a light-cone largest-time identity and a closed-time-path form;
3. equal-time localization inside scale-adapted windows (weak equivalence only);
4. spectator–spectator exchange as a Hermitian $\tau=0$ insertion;
5. simultaneous deformation;
6. eikonal approximation + Ward identities → past-pointing Wilson lines;
7. soft factor 1;
8. interface with App D.

**Error taxonomy** (E.1.3, Note E.20): scaling statement / pointwise bound / fibre-integrated bound / integral-norm bound. $F_\Gamma$ carries pinched $i0$ distributions and is not $L^1$, hence only *weak equivalence* (E.6).

**E.2 definitions and main theorems.**
- **Def E.1**: leading-region data; active vs spectator lines; class $\mathcal G_0$ (soft subgraph = direct $J_A$–$J_B$ lines).
- **Def E.2**: initial/final are properties of **LCOPT intermediate states**, not of lines.
- **Def E.3**: standard flow — soft momenta exit through $V_H$; initial denominators carry $+k_j^-$, final ones $-k_j^-$; the cut $\delta$ is soft-free.
- **Def E.4**: $G_\delta=\{|k^+k^-|\le\delta k_T^2\}$; intra- and inter-term pinches. Deforming one component does not leave $G_\delta$.
- **Def E.5**: localizable endpoints; windows $\Theta_j=\vartheta(4\nu_A\mu_j/(\lambda^{a_G}k_{Tj}^2))$ depending only on $k_T$ and jet plus/transverse components; soft-angle region $K_R$.
- **Def E.6**: measurement-compatible cut sum $F_\Gamma$; weak equivalence $\doteq_R$.
- **Def E.7**: deformation target (a)–(c), plus (d) compatibility with $\mathfrak B$.
- **Thm E.8** (main, collinear), conditional on E.18, E.33, E.34, E.44(a), plus D.7(A3), (A4)(ii):
  - (i) $F_\Gamma\doteq_R\tilde F_{\Gamma,R}=\mathfrak r_RF_\Gamma$ for all chain terms;
  - (ii) one-sidedness in windows;
  - (iii) deformation target; eikonal; past-pointing $W^{(-)}$; soft factor 1; DIS PDFs;
  - (iv) SS cancellation for non-coincident connections on window cores.
- **Thm E.9**: TMD version, with past-pointing staples and $\tilde S(b_T)$.
- **Cor E.10**: interface — (G-a), (G-b), (G-c) of D.31; (E.8) = (D.19) under E.44(b)(c).
- **Notes E.11–E.13**: clause-by-clause map and a correction table for (G1)–(G6).

**E.3 LCOPT.**
- **Lemma E.15** [rigorous]: LCOPT from Feynman integrals at finite $\eta_0$. For graphs without self-loops and with reduced numerators, $I_J(q^-)=2\pi\delta(\sum q^-)\prod\frac{N_l}{2l^+}\sum_{\pi\in{\rm Ord}(J)}\prod_i\frac{i}{D_i^\pi}$ (E.13). The proof: absolute convergence by Weinberg/Hahn–Zimmermann ($\dim W\le|L_W|-1$), Fubini, sector decomposition, distributional limit.
- **Lemma E.16**: instantaneous terms and contact vertices; instantaneous loops are independent of external minus energies.
- **Note E.17**: contact vertices at $V_H$ are suppressed ($\gamma^+\gamma^+=0$).
- **Ass E.18**.
- **Lemma E.19**: Glauber power counting (scaling).
- **Lemma E.21**: $V_H$ at $\tau=0$ on both sides; $\mathcal E$ unweighted; (E.17).
- **Lemma E.22**: pole positions; sign coherence of initial denominators.
- **Ex E.23**: spectator model in LCOPT, (E.19)–(E.20): two orderings = product of Feynman propagators; after $k^-$ the exchange is an equal-time $k_T$ transfer; single orderings are regularization dependent.

**E.4 cut sums.**
- **Lemma E.24** (exact algebraic cut-position identity, light-cone largest-time equation): $\sum_j\mathcal T_j=\delta_{n0}W_0-i\sum_m(\alpha_m-\beta_m)\prod_{i<m}\alpha_i\prod_{i>m}\beta_i\int H_m$. At most two insertion terms survive.
- **Lemma E.26**: closed-time-path representation (E.25); FSI internal to $J_A$ vanish; largest-time pairing.
- **Note E.27**: why one time per jet — in a single $x^+$ ordering, $H$'s B end spreads over the Glauber range. Measurement compatibility means the identity stands between cut states.
- **Lemma E.28** (equal-time insertion): $\mathcal J_+-\mathcal J_-\leftrightarrow[O(0),V_H(0)]$; window form (E.28); full axis (E.29) with $c=R_\downarrow(0)/R(0)$.
- **Note E.29**: $c=\theta(k^+)$ on the full axis vs $\frac12+O(\delta)$ in the window; only active-line insertions care; spectators see $J(k)=O(\lambda_J/k^2)$ (the LCOPT form of Cor 3.17).
- SS localization (E.30)–(E.31): relative error $\frac{\nu_A\nu_B}{k_T^2}(1+\ln\frac{k_T^2}{\nu_A\nu_B})$; the log is genuine.
- (E.32): $V_G=\int\rho_A\chi\rho_B$, Hermitian, amplitude $-iV_G$.
- Non-commuting insertions: ordering weights $\prod z_j/\prod_m\sum_{l\ge m}z_{\pi(l)}$, correlated between the jets.
- **Def E.30**: spectator-exchange families, coincident connections.
- **Prop E.31**:
  - (i)–(iii) cancellation for non-coincident connections on window cores ($\prod_l(-iG_lX_l+iG_lX_l)=0$);
  - (iv) coincident non-abelian: residual $-\frac12C_A\chi^2({\rm Re}\,p_{\rm opp})X$.
- **Rem E.32**: self-correction of §9.

**E.4.5–E.4.6 one-sidedness and examples.**
- **Ass E.33**.
- Rewriting $\mathfrak r_R=\prod_u[\Theta_u\mathfrak l_u+(1-\Theta_u)]$ with the entire carrier $\phi(x)=2\sqrt\pi e^{-x^2}$ (E.34).
- **H-emission endpoints**: $c_j=\theta(k_j^+)$ is non-analytic, so the endpoints are excluded and go to E.44(d).
- **Ass E.34**.
- **Prop E.35**: one-sidedness after the cut sum (E.35), weak.
- **Rem E.36**: why only weak; SA/AS construction; subtraction terms of rewritten forms defined by $\mathfrak r_RC_{R'}F$.
- **Ex E.37**: single exchange, $\mathcal J_+=\mathcal J_-=i/D_1$, $-i\chi\mathbf T_A\cdot\mathbf T_B$; AS contact term.
- **Ex E.38**: two exchanges. Ladder $X^2$, crossed $X^2+\frac12C_AX$, $M^{(2)}=\frac{(-i\chi)^2}2[X^2+p_{\rm opp}\frac12C_AX]$, residual (E.36) $-\frac12C_A\chi^2({\rm Re}\,p_{\rm opp})X$. Common ordering ($p_{\rm opp}=0$, the RS regulator) gives 0; the strict window ($p_{\rm opp}=\frac12$) gives $-\frac14C_A\chi^2X$.

**E.5 deformation and Wilson lines.**
- (F1)–(F3).
- Switch $\psi$ (E.38); **Glauber direction** $e_G=\bar n-n$ (ours: $n_B-n_A$), $e_G^2=-2$ (E.39).
- **Def E.39**: direct-line deformation (E.40) and Glauber flows (E.41).
- **Rem E.40**: $(l+it\sigma fe_G)^2-m^2=(l^2-m^2+2t^2f^2)+2it\sigma f(l^+-l^-)$ (E.42); a two-component deformation only makes denominators more timelike.
- **Lemma E.41**: no singularity crossed; subtraction-term eikonal denominators must be **past-pointing**.
- **Def E.42 / Prop E.43**: graded configurations; routing (E.44)–(E.45); target for $\mathcal G_0$ with $c=\min(\kappa^2,\delta/2)$.
- **Ass E.44**.
- **Prop E.45**: eikonal bounds on the deformed contour, (E.46) and the Grammer–Yennie ratio (E.47).
- **Prop E.46**: Ward → past-pointing $W^{(-)}$. In a single cut graph the attachment sum is the **future** line; past arises only after rewriting. The matching check is relegated to (H1)(H2).
- **Prop E.47**: $T[\mathcal U^{(-)}]=U_I(0,-\infty)$ is unitary.
- **Lemma E.48** (ordering structure), four parts:
  - (a) Hermitian $V_G$;
  - (b) abelian exponentiation;
  - (c) common ordering gives unitarity;
  - (d) independent cutoffs give non-unitarity (E.51).
- **Rem E.49**: self-correction of (9.2).
- **Prop E.50**: TMD.

**E.6 assembly.**
- Proof of Thm E.8 in steps (S1)–(S8), with the three error types.
- Thm E.9 via (E.52) $U^\dagger e^{ib\cdot\hat P_T}U=e^{ib\cdot\hat P_T}$.
- **Rem E.51**: compatible with measurement ⟺ the measurement operator commutes with $U$ and with the $\tau=0$ insertions.
- **Rem E.52 + Tables 7–8**: rigour checklist.
- **Rem E.53** (DFT outside the premises; (E.53) $(p_A-k)^2-m^2=-2p_A^+(k^-+\frac{m^2}{2(p_A^+)^2}k^+)+k^2$).
- **Rem E.54** ($pp\to h_1h_2X$ fails at (S3)).
- **Rem E.55** (gaps: $\Pi_{\rm gap}$ non-commuting, (E.54)).
- **Rem E.56** (RS dictionary).
- **Rem E.57** (double DY).

### 1.9 Inventory of explicit calculations in the reference (all re-verified unless marked)

| calculation | pages | verdict |
|---|---|---|
| light-cone algebra, boosts, $\mathcal P_\pm$, Breit frame, DY LO and Jacobian, FF $O(\alpha_s)$ normalization | 10–13 | correct (R1) |
| Sudakov regions $(1,-1,-1,1)$, $\ln^2+\pi^2/3$ | 15–17 | correct; constant omitted (R1, R6) |
| power-counting exponents (3.8), (3.9), Glauber $\lambda^0$, Fig 10 geometry | 18–21 | correct; super-leading cases missing |
| telescoping (3.15), $W^{(1)}[w^-,0]=gt^a(1-e^{-ik^+w^-})/k^+$ | 26 | correct |
| $R$ to $O(a^2)$; one-loop real/virtual constants | 29–31 | correct (normalization-dependent split) |
| tree OPE $T_2=4e_q^2\omega/(1-\omega^2)$; $\int z^{n-1}P_{qq}$ | 34–37 | correct |
| one-loop PDF traces; $c_q$, $C_{2,g}$; $c_q^{\rm DY}$ | 46–51 | correct (finite parts quoted) |
| cutting identity; $-i/(4s^\pm)$; Fig 36 sums | 52–58 | correct (strict-window colour residual is an artefact, ERR-S1) |
| Def 10.2 = Collins (13.106); $\zeta_A\zeta_B=Q^4$; CS algebra; one-loop $\tilde K,\gamma_K$; (10.8) | 63–66 | correct |
| Sivers ratio $-1$ (PT); $T_H$, $0.15$ GeV²; ERBL 50/81; GPD kinematics | 66–71 | correct |
| TMC coefficient $\frac{n(n-1)}{n+2}$; bubble-chain $n!/p^{n+1}$; $E_s=\frac12\sqrt{\hat s}(1-z)$ | 80–82 | correct |
| Landau envelope identity; App B sum rules, (B.2), (B.8) | 86–88 | correct |
| App C: chain-expansion signs, Zimmermann identity, Ex C.15, Ex C.26, Ex C.27 (sharpened), Lemma C.29 Lagrange identity, C.47 projector, C.63 Jensen, C.64 geometry, C.65 identity, (C.39) | 91–125 | correct (R5) |
| App D: (D.1)–(D.33), Fig 63 Hasse diagram, Lemmas D.11–D.13 on the 9-region poset, projectors, Lemma D.38, $J(\epsilon)$ to 25 digits, Table 5 | 128–160 | correct, 50/50 checks (R6); Table 5's reading as a remainder test is not (ERR-m25; synthesizer) |
| App E: (E.13) on 8 graphs to $10^{-30}$; (E.24) to $10^{-39}$; (E.19)/(E.20); (E.28)/(E.29); ordering weights; colour residues; (E.31) log; (E.36), (E.51); (E.42); Prop E.43, E.45 bounds; single-cut-graph eikonal identity | 162–230 | correct (R7, R8) |

---------------------------------------------------------------------------------------------------

## 2. Errors and over-claims (consolidated, de-duplicated, verified)

**Severity.**
- **S**: a physics or logic error that changes a stated result or its grade.
- **M**: a wrong or over-strong statement, a wrong attribution, or a missing hypothesis that a careful reader would be misled by.
- **m**: minor (wording, notation, sharpness).

"Readers" names the notes where the item is documented with evidence. ✓ marks items independently re-verified (by a script or by hand, by the reader and, where marked "syn.", by the synthesizer).

**Rule for our writers.** None of these errors may be copied. Where our text treats the same topic, the "correct version" column is binding unless a VERIFIED_FORMULAS entry says otherwise.

### 2.1 Substantive (S)

| ID | page(s) | what is wrong | correct version | readers |
|---|---|---|---|---|
| ERR-S1 | 57–58 (Prop 9.3, Fig 36 caption), 61 (§9.5), 85 (§15.1); App E Prop E.31(iv), Ex E.38, Lemma E.48(d), Rem E.49 | Claim: non-abelian $N\ge2$ spectator–spectator Glauber exchanges "do not cancel within these graphs", leaving the residual $-\frac14C_A\chi^2\mathbf T_A\!\cdot\!\mathbf T_B$; the common ordering is a "regularization convention"; Ass. E.33(c) "including real emission" is needed. This is the reference's main justification for grading DY B′ rather than B. | The colour algebra is right for independent symmetric cutoffs ($p_{\rm opp}=\frac12$). But evaluating **the same** box and crossed box exactly for two infinite time-like eikonal lines (rapidity difference $Y$, exact gluon propagators) at fixed transverse momenta ($a=k_T^2+m^2$, $b=(K-k)_T^2+m^2$) gives $J_{\rm box}=\frac{2\pi}{ab}(\pi+iY)$ and $J_{\rm cross}=-\frac{2\pi iY}{ab}$. Hence $p_{\rm opp}=-iY/\pi$, ${\rm Re}\,p_{\rm opp}=0$, and, with $X\equiv\mathbf T_A\!\cdot\!\mathbf T_B$ and the colour factors $c_{\rm box}=X^2$, $c_{\rm cross}=X^2+\frac{C_A}2X$ (same ordering convention as the reference's (E.51)), $J_{\rm box}c_{\rm box}+J_{\rm cross}c_{\rm cross}=\frac{2\pi}{ab}[\pi X^2-iY\frac{C_A}2X]$: the common-ordering term plus a Hermitian×$i$ one-loop **reggeization phase**. So the two-gluon exchange graphs alone give $\mathcal V^\dagger\mathcal V=1+O(\chi^3)$, with no real emission (for straight infinite time-like lines the one-gluon emission amplitude $\propto\delta(v\cdot k)$ vanishes on shell, so real cuts first enter at $O(g^6)$); the other $O(g^4)$ graphs (one-loop correction of the single exchange, three-gluon graphs) can contribute only phases by unitarity of the eikonal system (argued, not computed). The residual is an artefact of the strict instantaneous truncation, which discards the principal-value parts near $2k^+k^-=k_T^2$. The genuine open problem is the all-order interplay of Glauber, soft and collinear modes for **non-eikonal** (composite, interacting) spectators and for active partons. The reference's own Rem E.49 and Rem E.56 concede that the RS regulator gives the common ordering. | R3 E1 ✓ (`eikonal_box*.py`, $<5\times10^{-16}$; syn. reran ✓), R4 E12, R7 §10.1, R8 Ex E.38 |
| ERR-S2 | 74 (argument for Thm 12.3) | Colour bookkeeping: with a uniform eikonal numerator and $\mathbf T_a+\mathbf T_b=\mathbf T_c+\mathbf T_d$, the combination $\eta_b\mathbf T_b+\eta_c\mathbf T_c+\eta_d\mathbf T_d$ is claimed irreducible "because $\eta_b\neq\eta_{c,d}$". With these conventions it reduces to $-\eta_b\mathbf T_a$. The same bookkeeping would predict **no** Sivers sign flip, and it contradicts Collins–Qiu's explicit factor $i\pi(g_1+2g_2)$. | With all-outgoing charges ($\sum_j\mathbf T_j=0$; initial lines $1/(n\cdot k+i0)$, final lines $1/(n\cdot k-i0)$ for $k$ into the line), the Glauber part is $\propto\mathbf T_b-\mathbf T_c-\mathbf T_d=\mathbf T_a+2\mathbf T_b$, which is irreducible. Equivalently, in the "in = out" convention the $\delta$ parts of initial and final eikonal factors carry the **same** sign. SIDIS gives $+\mathbf T_a$ and DY gives $-\mathbf T_a$ (sign flip ✓). Our `prop:break-colour` ($P=-\mathbf T_a-2\mathbf T_b$) is already correct. | R4 E1 ✓ (`checks_R4.py`) |
| ERR-S3 | 198 (Ass E.33(c1)); consequences in Prop E.35, Thm E.8(i)(ii) | (c1) asserts a **fixed** localization order for non-commuting equal-time insertions on one spectator parton, for which per-graph weak equivalence holds. The reference's own analysis (pp. 195–196) shows that the equal-time limit is a **weighted** sum $w_{12}O_2O_1+w_{21}O_1O_2$, with $w_{12}=z_1/(z_1+z_2)$, $z_j=k_{Tj}^2/(2k_j^+)$, for same-side poles, and $0/1$ for $k_1^+k_2^+<0$. A fixed order errs by $w_{21}[O_1,O_2]=O(1)$, so (c1) is generically false per graph. | Replace (c1) by a **lemma**: multi-insertion localization with ordering weights $w_\pi$ fixed by the external factors (N insertions with single poles: $\prod_jz_j/\prod_m\sum_{l\ge m}z_{\pi(l)}$). Keep only the complete-set statement (c2) as an assumption. Note the new obstruction: the weights are piecewise in $k_j^+$, non-analytic at $k_j^+=0$ exactly like $c_j=\theta(k_j^+)$ for H-emission endpoints. Coincident SA/AS insertions therefore need the same treatment as E.44(d). | R8 E1 ✓ (`check_weights.py` K12), R7 C5 ✓ |
| ERR-S4 | 19 (Cor 3.8), 22 (Thm 3.12 "$p(R)\ge0$") | Super-leading configurations are omitted: by (3.8) with $c_J=2$, $(n_F,n_T)=(0,0)$ has $p_J=-2$ and $(0,1)$ has $p_J=-1$. "All other combinations are suppressed by $\ge\lambda$" is false. $(0,0)$ is dismissed in one line; $(0,1)$ is never mentioned. | State the super-leading configurations and their cancellation in gauge-invariant sums (Ward identity + colour neutrality, CSS 1989 §8.6) [A]. Their $O(\lambda)$ and $O(\lambda^2)$ remainders are leading and build $F^{+j}=\partial^+A^j-\partial^jA^++\dots$. For a gluon as the only active parton, $k\cdot H=0$ and the G term $\propto k^+A^j-k^jA^+$ is leading. "$n_T$ transverse gluons" is not a gauge-invariant bookkeeping in the gluon channel. | R1 E4 ✓ |

### 2.2 Moderate (M)

| ID | page(s) | what is wrong | correct version | readers |
|---|---|---|---|---|
| ERR-M1 | 15 (Cor 3.4) | "No pinch in the Euclidean region". Zero-momentum massless lines solve the Landau equations for any external kinematics (e.g. the three simplex corners of (3.3)). | In the Euclidean non-exceptional region the only Landau solutions are sets of zero-momentum massless lines. These are IR convergent by power counting (Lowenstein–Zimmermann; our `thm:ee-euclid-ir` IR degree $d=A+\frac12A_q\ge2$). With massive lines $\mathcal F>0$ and there is no solution. | R1 E1 ✓ |
| ERR-M2 | 16–17 (Prop 3.5) | (3.3) is called "Euclidean kinematics", but $p_i^2=-m^2$ with $(p_1+p_2)^2=-Q^2$, $Q\gg m$ is not realizable with Euclidean vectors. The proof assumes the regions expansion (unproven in this multi-facet Minkowskian case), single-scale Laurent forms, and existence of the $C_1$ integral (which has no common convergence strip). The constant $\pi^2/3$ is omitted. | Compute the four regions explicitly; tag [P] (verified at one loop); give $Q^2I=\ln^2(Q^2/m^2)+\pi^2/3+t(2L^2-4L-4+2\pi^2/3)+\dots$ ($t=m^2/Q^2$, $L=\ln(Q^2/m^2)$; exact closed form $\Phi^{(1)}(t,t)$, Usyukina–Davydychev). Also: the "hard point" is the absence of a pinch, not a Landau solution (ERR-m1). | R1 E2, E3 ✓; R6 E3 ✓ |
| ERR-M3 | 14–15 (Thm 3.1, §3.1) | The parameter-space theorem (singularities in external $p$) is conflated with the momentum-space trapping criterion used for reduced diagrams; parameter pinches ≠ momentum pinches for massless graphs (Collins 2020 App D1). "Endpoints do not occur" ignores second-type singularities and endpoint singularities after partial integrations (needed in §11). | Two theorems with two proofs (α-space analyticity; Gordan-type momentum criterion). Our `thm:ir-landau-alpha`, `thm:ir-landau-momentum`, `rem:ir-landau-status` already do this. | R1 E10 |
| ERR-M4 | 11 (Fig 4) | Wilson-line rules "vertex $igv^\mu t^a$, propagator $i/(v\cdot k\pm i0)$, ± future/past": no momentum routing, $W$ vs $W^\dagger$ not distinguished, and inconsistent with (2.7) and with the table's own last row. | Universal rule (our VF-WL-1): vertex $igt^av^\mu$ (orientation $+v$), propagator $i/(v\cdot\ell+i0)$ with $\ell$ along the orientation; past $W[0,-\infty n]$: $\prod\frac{i}{n\cdot(k_1+\dots+k_j)+i0}$, future $W[\infty n,0]$: $\prod\frac{-i}{n\cdot(k_j+\dots+k_m)-i0}$. | R1 E5 ✓ |
| ERR-M5 | 23 (3.10), 25 (step 3 of Thm 3.14) | The collinear K-projection has no $i0$; the pure-gauge argument is blind to it and cannot fix the Wilson-line direction (it produces "past" only because $U$ was based at $-\infty$). | DIS: $K_{\mu\nu}=k_\mu w_{2\nu}/(k\cdot w_2-i0)$ (future; Collins 2011 eq. (11.6) with errata); DY: $+i0$ (past). The direction is fixed by the $i0$ of the replaced propagators and, for DY, by the contour (App E Lemma E.41(e)). | R1 E6 |
| ERR-M6 | 23–25 (Thm 3.14) | Stated as a theorem for general $H$. Proven only for $H$ built of quark lines with colour-singlet vertices (tree level); the non-abelian background-field identification is cited; "one Wilson line" for two quark lines; gluon-initiated $H$ not covered. | Abelian/tree identity [R]; all-order non-abelian [A] (our `lem:method-ward-multi`). Keep the pure-gauge argument as a structural heuristic whose step 2 is the BRST content. | R1 E11 |
| ERR-M7 | 26 ((3.16), Cor 3.17) | The soft factor contains a literal "⋯": positions, ordering, cut and future/past all unspecified. "Identical proof" to Thm 3.14, but the base point of soft lines is physical. | Precise operator definitions (8.2)/(E.48), with the $i0$ inherited from the replaced jet propagators; future for $e^+e^-$/DIS final states, past for DY. | R1 E8 |
| ERR-M8 | 1 (abstract), 7, 84 | Hard exclusive meson electroproduction is listed without "longitudinal photon". | CFS covers $\sigma_L$ only; $\gamma_T^*$ has endpoint divergences (our `thm:excl-meson-L` [A], `prop:excl-meson-T` [V]). | R1 E13 |
| ERR-M9 | 7 (Def 1.1), 75, 84 (Table 1) | Inclusive quarkonium decay graded A/A\* ("as rigorous as the OPE"). | The decay rate is Minkowskian at a fixed physical point: no Euclidean continuation is available, so a non-perturbative statement needs local duality (not an App C assumption). Perturbatively it is [A] (BBL; also the NRQCD cutoff dependence of $f_n$ and $\langle\mathcal O_n\rangle$). Our `thm:heavy-nrqcd-decay` [A] is right. | R1 E14, R4 E6 |
| ERR-M10 | 36–37 (Prop 5.4) | "DGLAP ⟺ OPE RG" with a single kernel $P_{qq}$ for all $n$ (even and odd). Beyond LO, $P^\pm_{\rm NS}=P^V_{qq}\pm P^V_{q\bar q}$ differ: $\int_0^1P^{V(1)}_{q\bar q}=0.71931\,C_F(C_F-\frac{C_A}2)\neq0$. | Even-$n$ RG ⟺ DGLAP for the C-even set $(q+\bar q,g)$; odd-$n$ ⟺ DGLAP for $q-\bar q$ with $P^-$; separate Carlson continuations. Our `rem:pdf-ns-plusminus` is right. | R2 E1 ✓ (`check_Pplusminus.py`) |
| ERR-M11 | 41 (Fig 24; regions used in Thm 6.3/6.6) | The two-rung ladder is said to have "two leading regions"; the maximal (all-hard) region $R_0$, which carries the two-loop coefficient, is missing. Without it (6.4) is false. | Three regions $R_2<R_1<R_H$ (as App D Ex D.48 does). | R2 E2 |
| ERR-M12 | 39 (§6 intro), 6–7 (Def 1.1) | "§6 fully executes the five steps"; "the combinatorics are complete". The regrouping of $\sum_{\Gamma,R}C_R\Gamma$ into $\hat T\otimes f$ (subtractions act only on hard parts; colour projection) takes three sentences. | The combinatorial regrouping is itself an input (App D Ass. D.37 (W1)(W2); D.42 for DIS). State it as such. | R2 rigour (a) |
| ERR-M13 | 29 (Thm 4.1(ii)) | Proves finiteness of $12\pi\,{\rm Im}\,\Pi$, but never shows that the DR sum over partonic cuts (ghosts, counterterms, $D$-dim cutting rules) equals it; the interchange of $\epsilon\to0$ with continuation is glossed. | Our `thm:ee-R-finite` [R, R_PT] (Laurent coefficients polynomial in $L$, vanishing for real $L$, hence identically) + `cor:ee-cuts` [A]. | R2 rigour (b) |
| ERR-M14 | 47 (Prop 7.1) | The one-loop PDF "check": the virtual $\delta$ term is fixed by a sum rule; the $\xi\to1$ (rapidity) divergences of the Wilson-line real and virtual graphs and their cancellation in $[2\xi/(1-\xi)]_+$ are not shown; the self-energy $-\frac12\delta$ is not shown. | Our `prop:pdf-pqq-operator` (gluon mass; every graph; gauge independence) and VF-PDF-3/13/14. | R2 rigour (c) |
| ERR-M15 | 64 (proof of Thm 10.3, step (iv)) | Printed: $\tilde f^{\rm unsub}_A\tilde f^{\rm unsub}_B\tilde S(+\infty,-\infty)/[\tilde S(+\infty,-\infty)\tilde S(+\infty,-\infty)]=\tilde f_A\tilde f_B$. With identical arguments the left side is $\tilde f^{\rm unsub}_A\tilde f^{\rm unsub}_B/\tilde S$, which is rapidity divergent. | $\tilde f^{\rm unsub}_A(y_{P_A}-y_B)\tilde f^{\rm unsub}_B(y_A-y_{P_B})\tilde S(y_A,y_B)/[\tilde S(+\infty,y_B)\tilde S(y_A,-\infty)]$, with limits taken after combining; inserting $y_n$ and using linearity of $\ln\tilde S$ gives (10.4). | R3 E2 ✓ (200-dpi zoom) |
| ERR-M16 | 64 (Thm 10.3 box) | "With the Y term the error is **uniformly** $O((\Lambda/Q)^a)$", stated without qualification. | The standard W+Y needs modified cutoffs near $q_T\sim Q$ and $q_T\sim\Lambda$ (Collins–Gamberg–Prokudin–Rogers–Sato–Wang 2016, **verify**). The reference itself excludes Y from its conditional theorem. | R3 E7 |
| ERR-M17 | 71 (proof of Thm 11.4) | The transverse-photon failure is described as "$\int dz\,\phi(z)/z^2$-type". | In the WW approximation the twist-3 integrals diverge logarithmically because $g_\perp^{(v)}(0)=\frac12\int du\,\phi_\parallel(u)/u\neq0$; there are also double poles $(\xi\mp x-i0)^{-2}$ in the GPD convolution (Mankiewicz–Piller 2000). The leading-twist $\gamma_T^*\to V_T$ amplitude vanishes to all orders by chirality/helicity (Diehl–Gousset–Pire 1999; Collins–Diehl 2000). | R3 E3 |
| ERR-M18 | 74 (description of RM, CQ) | CQ's model is abelian (called non-abelian). RM's counterexample is a double-Sivers asymmetry with a colour-singlet hard exchange and colour factor ${\rm Tr}[t^at^b]{\rm Tr}[t^bt^a]=T_F^2(N_c^2-1)$, against the prediction 0 from colour-traced Wilson loops — not a "difference ∝ $[t^a,t^b]$". Collins 2007 (unpolarized, two gluons) is not cited. | As corrected; our `thm:break-tmd` (entanglement test $C_F^2+\frac{4T_F^2(N^2-1)}{N^2}$, C07 anomaly) is already right. | R4 E2 ✓ (papers read) |
| ERR-M19 | 76 (NQS) | "These Wilson lines do not change the numerical result at NNLO". | NQS find uncancelled NNLO poles $\propto\alpha_s^2v^2/\epsilon$, generated exactly by the gauge-completed octet operators. The Wilson lines are **necessary** at NNLO (relative order $v^2$); beyond NNLO new non-local operators may be needed. | R4 E3 ✓ |
| ERR-M20 | 73 (Rem 12.2) | "For one- and two-loop cross sections the phase terms cancel after the colour sum". | One loop: yes (anti-Hermitian). Two loops: CdFR find a Hermitian operator in $P^{(2)}$ for $\ge5$ partons. FSS: its expectation value vanishes on pure-QCD trees (one step unproven) but not with QCD+EW phases. Pure-QCD non-inclusive violation starts at three loops; mass singularities possibly from N³LO; GHMMS 2025: cancels up to NNLO in pure QCD. | R4 E4 |
| ERR-M21 | 72 (§11.3(c)), 84 | "BBNS holds at $O(\alpha_s)$ and LP"; $B\to\pi$ and $B\to\pi\pi$ lumped as C. | BBNS argued LP to all orders (two-loop IR analysis); SCET LP derivations exist (Chay–Kim 2004; BPRS 2004, charming-penguin caveat). The heavy-to-light form factor = soft overlap + hard spectator is a theorem-level LP statement (BPS 2003; Beneke–Feldmann 2004); only the further factorization of $\xi_\pi$ fails. | R4 E5 |
| ERR-M22 | 76 (Conj 12.5) | "For $p_T\gg m_Q$ **or** $\sqrt s\gg m_Q$, at leading velocity power" is not BBL's conjecture; the large-$p_T$ two-step structure is omitted. | BBL: all inclusive production with $m_Q$ hard, order by order in $v$. At $p_T\gg m_Q$: QCD factorization into single-parton (LP) and double-parton (NLP) fragmentation (Kang–Qiu–Sterman 2012; KMQS 2014; FLMR 2012), then NRQCD for the FFs. Our `prop:heavy-quarkonium-fragmentation` already has this. | R4 E7 |
| ERR-M23 | 73, 84 | Gap/non-global $pp$ observables graded D ("standard collinear factorization fails"). | Strict collinear factorization of amplitudes [V]; SLLs exist at fixed order and are resummed; PDF factorization of gap cross sections is open, with evidence for restoration (Becher–Hager–Jaskiewicz–Neubert–Schwienbacher, PRL 134 (2025) 061901) → [C]. | R4 E8 ✓ (INSPIRE) |
| ERR-M24 | 108–109 (Lemma C.41(a)), 127 (Table 2) | EOM (alien) operators vanish between on-shell partonic states "including forward", with an imprecise reason. | Valid for non-zero momentum transfer or IR-regulated legs. Forward on-shell massless gluon matrix elements have known IR subtleties (Hamberg–van Neerven 1992 puzzle, Collins–Scalise 1994 = the reference's own [108]; modern alien counterterms: Falcioni–Herzog 2022, Gehrmann–von Manteuffel–Yang 2023, **verify**). Grade "proved off-forward/IR-regulated". | R5 E2 |
| ERR-M25 | 118 (Ass C.56 (W2)) | "Baryon-number-1 spectrum ⊂ $\{p^2=M^2\}\cup\{p^2\ge M_1^2\}$, $M_1>M$, nucleon isolated": false in the chiral limit (massless pions: $N\pi$ continuum starts at $M$, used elsewhere in App C) and for $m_u\neq m_d$/QED ($p$ and $n$ both below threshold). | State the spectral condition in the superselection sector of the target's conserved flavour numbers (where the intermediate states of $\langle P\vert JJ\vert P\rangle$ live). Lemma C.64 needs only ${\rm spec}\subset\{p^2\ge M^2\}$ there; isolation is needed only for Haag–Ruelle. Massive light quarks must be stated and reconciled with massless $\overline{\rm MS}$ coefficients. | R5 E3 |
| ERR-M26 | 88, 93, 103, 110–111, 127 | "No verbatim proof in the literature" of the momentum-space remainder (hence Ass C.24) and of the gauge-variant-basis statement (hence (B1)(B2)), without checking Anikin–Zav'yalov 1978 (its own [116]), Zav'yalov 1990 (uncited), Joglekar 1977 I+II and Hollands 2008 (both absent). By uniqueness (Thm C.25(iii)) any proven momentum-space OPE with that remainder would discharge C.24. | Check and cite. C.24 may become "cited theorem via uniqueness"; (B1)(B2) may be partly discharged (pure YM: Hollands 2008). The refs agent must verify the scope. | R5 E4, E5 |
| ERR-M27 | 143 (Table 4 row 6 proof), 63 (Fig 39 caption) | Self-energy terms of space-like regulator lines $n_A(y_A)$ are called "a finite term indispensable in the rapidity-regularization scheme". | They are **non-integrable**: $n_A\cdot k\propto\sinh(y_k-y_A)$ vanishes inside the real-gluon phase space, giving a $1/\sinh^2$ double pole (length divergence). Any self-energy constant cancels identically in Collins' combination (D.22). They must be excluded or defined by a convention consistently in $\tilde f^{\rm unsub}$ and $\tilde S$. Our c_tmd and `lem:tmd-soft-oneloop` are already right. | R6 E1 ✓ (c_tmd R4) |
| ERR-M28 | 152 (Ass D.41 (U1)) | "The passage to $\overline{\rm MS}$ is a finite renormalization (finite redefinitions of couplings and fields)". | In non-abelian theories BPHZ(L) Taylor subtractions break Slavnov–Taylor identities. Equivalence with DR+$\overline{\rm MS}$ needs extra finite **non-invariant** counterterms (algebraic renormalization; Breitenlohner–Maison 1977). Graphical Ward identities then hold exactly only for DR graphs; the compatibility of (U1) with (W1)/(Z2) is not addressed. | R6 E6 |
| ERR-M29 | 223 (Rem E.52(1)), 225 (Table 8 caption), 226 | "App D inputs are unrelated to the Glauber region, equally needed for DIS and $e^+e^-\to hX$"; Glauber-specific gaps are only E.33(c), E.44(a)–(d), E.33(a)(b). | (H1)(H2) **for rewritten and family-summed forms** carry Glauber-specific content: localized spectator terms vs external-endpoint distributions at $n\cdot K_i=0$ (Prop E.46 step 2), and the allocation of SA/AS endpoints between regions (E.46(c)). E.34 is DY-specific as well. Count them as Glauber-specific open inputs. | R8 E2 |
| ERR-M30 | 229 (Rem E.55) | Gaunt 2014 is cited as showing that the CSS argument fails at two Glauber gluons between spectators for hadronic $E_T$, without the rebuttal in the reference's own [137]. | Contested: Schwartz–Yan–Zhu 2018 show that pure Glauber ladders cancel for single-scale observables (incl. $E_T$, beam thrust), so the leading violation needs at least one soft gluon (Lipatov vertex), i.e. Glauber–soft mixing. MPI-sensitive observables remain non-factorizing (Zeng 2015 explicit counterexample). Our `prop:break-jet-veto` is already right. | R8 E3 ✓ (abstract) |
| ERR-M31 | 228 (Rem E.54(b)) | "$2l\cdot k\ni2l^+k^-$, $l^+\sim Q$, so $J_1$ depends on $k^-$ at scale $\lambda^2$" ignores $-2l_T\cdot k_T\sim Q\lambda$ for a central jet. | The relevant pinch region is Glauber relative to the pair $(n_A,w_1)$: $k\cdot n_A\sim k\cdot w_1\sim\lambda^2$, with $k_T$ nearly orthogonal to $w_{1T}$. There $J_1$ depends on $k^-$ at scale $\lambda^2$ (the conclusion survives). | R8 E8 |
| ERR-M32 | 162–230 (whole App E; bibliography) | The method — hybrid LCPT ($x^+$ for one jet, $x^-$ for the other), pinch replaced by a mismatch of deformation directions, FSI phases cancelled by unitarity — is that of **Aybat–Sterman, PLB 671 (2009) 46**, which is not cited anywhere. Diehl–Gaunt–Ostermeier–Plößl–Schäfer 2016 (LCPT for single and double DY) is not compared. | Credit Aybat–Sterman 2009 and DGOPS 2016 as precedents (our c_glauber §1.5–1.6 verified the former). | R7 E10, R8 G7 |

### 2.3 Minor (m)

| ID | page(s) | issue → correction | readers |
|---|---|---|---|
| ERR-m1 | 16–17 | The "hard point ($\alpha_k=0$, all lines off shell)" is listed as a Landau solution, but it is the absence of a pinch; the soft-quark corners $k=p_1,-p_2$ are omitted. | R1 E2 |
| ERR-m2 | 25 (Rem 3.15) | $U(+\infty)$ is a field-dependent operator, not a "constant colour matrix / global gauge transformation"; the conclusion holds via $W[w,\infty]W[\infty,0]=W[w,0]$. | R1 E7 |
| ERR-m3 | 23 | "K part of Grammer–Yennie [15]": the original GY K-photon is the symmetric $b_kk_\mu k_\nu$; the one-sided form with $i0$ is Collins' adaptation. | R1 E9 |
| ERR-m4 | 13–14 (Prop 2.4) | Positivity of the "unrenormalized" PDF is formal (UV divergent); the light-cone-gauge proof inherits the $1/k^+$ ambiguity it raises itself; the anticommutator $\propto\delta(w^-)\delta^2(0)$ is a divergent constant; support of the renormalized PDF is not addressed. Use the gauge-invariant state sum and the support of $Z$. | R1 E12 |
| ERR-m5 | 6, 12 | (1.1) has an absolute remainder and schematic $\hat\sigma(\xi_A,\xi_B)$; $\nu=P\cdot q$ clashes with the Lorentz index; grade C mixes [P] and [C]. | R1 E15 |
| ERR-m6 | 34 (Ex 5.2) | "$\slashed q$ combines with the vertex $\gamma$'s into $\gamma^{\mu_1}$": for the $T_2$ structure the operator $\gamma^{\mu_1}$ is a vertex $\gamma$ and $\slashed k$ supplies the derivative; $\slashed q$ feeds $T_1$ and the gauge terms. | R2 E3 |
| ERR-m7 | 32 (§4.3) | Duality-violation example "$e^{-c\sqrt s/\Lambda}\sin(\dots)$" is non-standard (instanton models: power-damped oscillations; resonance models: $e^{-\delta-\gamma s}\sin(\alpha+\beta s)$). | R2 E4 |
| ERR-m8 | 49 (Rem 7.5) | "$\alpha_s^n\ln^{2n-1}(1-z)$" → $\alpha_s^n[\ln^{2n-1}(1-z)/(1-z)]_+$ ⟷ $\alpha_s^n\ln^{2n}N$. | R2 E5 |
| ERR-m9 | 49 vs 12 | $\tau=Q^2/\hat s$ (partonic) vs $\tau=Q^2/s$ (hadronic). | R2 E6 |
| ERR-m10 | 39–40 (Lemma 6.1, Prop 6.2) | The colour projection ${\rm Tr}_c[HJ]\simeq\frac1{N_c}{\rm Tr}_cH\,{\rm Tr}_cJ$ is missing. | R2 E7 |
| ERR-m11 | 29 | "$a_n$ has degree $n-1$" holds for $n\ge1$; the degree of $\Pi$ is $\max(1,n)$. | R2 E8 |
| ERR-m12 | 49 (Prop 7.4) | Finite parts of $c_q$, $C_{2,g}$ are quoted, not derived; the gluon-average convention $1/(D-2)$, the DIS scheme and $F_L$ are not mentioned. | R2 (d) |
| ERR-m13 | 56 (Fig 34 caption) | "The square of (e) diverges…" is gauge dependent: in Feynman gauge $2{\rm Re}(M_dM_e^*)$ also has the $1/t$ pole ($t\vert M_e\vert ^2\to-80$, $t\,2{\rm Re}\to+33.6$, sum $\propto P_{qg}$); only in an axial gauge does it come from $\vert (e)\vert ^2$ alone. | R3 E4 ✓ |
| ERR-m14 | 67 (Thm 10.6 proof) | "Vector bilinear → $+\bar\psi\gamma^\mu\psi(-x)$ (after Hermitian conjugation)": no conjugation is needed; the colour bookkeeping ($t^a\to t^{a*}$ reverses path ordering) is hidden; the sign of $\epsilon_T^{12}$ is unstated (Trento: $+1$). | R3 E5 ✓ |
| ERR-m15 | 68 vs 69 | (11.2) remainder $O(\Lambda^2/Q^4)$ should be $O(\frac{\Lambda^2}{Q^4}\ln\frac{Q^2}{\Lambda^2})$ by the reference's own endpoint-area estimate. | R3 E6 ✓ |
| ERR-m16 | 53–71 | Collected precision issues: (9.3) omits $(2\pi)^2$ and conflates total and relative momenta; $\chi(b)$ as written is IR divergent; the Coulomb-phase analogy (Rem 9.4) is imprecise; Rem 9.6 "no Glauber region in DIS" holds only for unphysical $\omega$; (10.3) soft factor undefined; $\sigma_0$, $x_{A,B}$ undefined in §10 and antiquark terms missing; small-$b$ remainder $O(b_T\Lambda)$ should be $O((b_Tm)^2)$ for unpolarized TMDs; Lemma 8.6 endpoints unspecified; Fig 46 omits $-1<x<-\xi$; $f_\pi$ is an older PDG value. | R3 E8 |
| ERR-m17 | 73 ((12.2)) | $\mathbf T_{\rm coll}$ undefined: it must be $\mathbf T_2$, the charge of the collinear parton with negative momentum fraction; genuine colour correlations need $\ge4$ coloured partons. | R4 E9 ✓ |
| ERR-m18 | 77–78 (Rem 13.2) | "The correct prescription cannot be seen at the Lagrangian level" is imprecise: the LO SCET rules already give the future-pointing line for outgoing collinear quarks; the direction is fixed by matching external states. The $\lambda^2Q$ mode is ultrasoft, not "soft". | R4 E10 |
| ERR-m19 | 81 (Prop 14.1) | Labelled 命题 but only an argument is given (the text says so). The proven case is the large-$N$ O($N$) σ-model (David; NSVZ; Beneke–Braun–Kivel 1998). | R4 E11 |
| ERR-m20 | 83 | "Twist parity = chirality" is unqualified; it holds for symmetric traceless operators only (false for transversity). | R4 E13 |
| ERR-m21 | 72 ((12.1)) | $\hat\sigma_{ab\to c}$ must be the invariant $E_cd\hat\sigma/d^3p_c$ ($1/z^2$ = Jacobian). | R4 E14 |
| ERR-m22 | 231–238 | Bibliography: minor title/erratum issues ([27], [34], [53], [54], [56], [59], [60], [139]); content misattributions of [53] and [60] (= ERR-M18, M19); missing key references (Collins 2007, Aybat–Sterman 2009, Mitov–Sterman 2012, Becher et al. 2025, KQS 2012, NQS PLB 2005, BBNS 2000, Nachtmann 1973, …). | R4 E15 |
| ERR-m23 | 101–102 (Ex C.27) | "$=O(q^{-4}\ln q^2)$" is not sharp: the combination is $-\kappa\pi^2/(2q^4)+O(m^2q^{-6}\ln q)$, with no log and an $m$-independent leading term (4D harmonicity). | R5 E1 ✓ |
| ERR-m24 | 91–123 | Fig 55 has cubic vertices (outside the stated model); Cor C.18 needs $\omega$ for disconnected $\gamma$; "the only external input is Thm C.8" omits routing compatibility for frozen $q$; the 1D slice edge-of-the-wedge step in Lemma C.64 needs the $Q^2$-smearing sentence; $\Vert \gamma\Vert \le C\alpha$ for mass-mixing entries needs rescaling (Thm C.66). | R5 E6–E10 |
| ERR-m25 | 141–158 | Lemma D.20 is misinvoked for DIS (Prop D.28(a)); Table 5's fit "$2\lambda^2L^2-3.9\lambda^2L$" should be the exact NLP of $I$, $t(2L^2-4L-4+\frac{2\pi^2}3)$; moreover Table 5 compares $I$ with $L^2+\frac{\pi^2}3$ written in $Q^2$, not with (D.32), which is written in $\tilde Q^2=2PP'$, so it does not test the Collins remainder at all: the remainder is $I-$(D.32)$=-4m^2/Q^4+O(m^4Q^{-6}L^2)$, with no logarithm at NLP (synthesizer check, S30); the $C_S$ $k^+$ integral is a Beta function, not $J(\epsilon)$; Lemma D.23(iii) "always true" has an uncovered edge case from the soft-line convention (plausible); typography ("假设假设"). | R6 E2–E5, E7 ✓ |
| ERR-m26 | 162–195 | Lemma E.28(iii) proof gap — fixable by closing in the LHP: $\int ER_\downarrow=-i\sum r_iE(z_i)$, $\vert E(z_i)\vert \le2M\lambda_J/\vert z_i\vert ^2$. The window-shape claim needs $K_{1,2}\le\Lambda/2$, and the error is $O(\lambda_J/\min K)$. The vertex sign "$-igJ^{+a}$" should be $+ig$ with the reference's own $D_\mu$. (E.30) is stated as relative but should be absolute. $\delta$ is reused. E.18(iii) is provable. "Strongest form that can hold" is rhetorical. $\Theta(-k_T)=\Theta(k_T)$ needed. | R7 E2–E9 ✓ |
| ERR-m27 | 198–223 | Rem E.49(2) sign wording (the compensating term is $+\frac14C_A\chi^2X$); $\sigma$ missing in ${\rm Im}(n\cdot K)=t\sigma\sum f_a$; Def E.39 "$k^-$ does not move at $\Theta'<1$" is inaccurate; $w_{12}$ depends on $k_{T1}^2/k_{T2}^2$ too; the boundary-layer estimate in Prop E.35 may fail for endpoints set by other $N_{R'}$ (plausible); Rem E.52(1) "complete" Wilson-line structure should read "up to (H1)(H2)" for TMD. | R8 E4–E7, E9, E10 ✓ |

**Count:** 4 S + 32 M + 27 m = 63 items.

### 2.4 Errors in OUR material found by the readers (must be fixed in the spec)

| ID | our location | problem | fix |
|---|---|---|---|
| OUR-1 | WRITER_SPEC §3 row 20; VF-CONV-17; FINAL_OUTLINE `def:pdf-ff`; BLUEPRINT §0.4(8) | FF prefactor $\frac{1}{4N_cz}$ "in the frame with $\mathbf p_{h,T}=0$" gives $z^{-2}\times$ the correct $O(\alpha_s)$ number density. The free-quark check $\delta(1-z)$ cannot detect this. | Hadron frame ($\mathbf p_{h,T}=0$, $w=(0^+,w^-,\mathbf 0_T)$): prefactor $\frac{z^{1-2\varepsilon}}{4N_c}$ ($=z^{d-3}/(4N_c)$; Collins–Soper 1982; Collins 2011 ch. 12). Parton frame: $\frac{1}{4N_cz}$ together with an explicit $\int d^{2-2\varepsilon}p_{hT}$. Spec change S9. (R1 check 4; syn. reran ✓) |
| OUR-2 | BLUEPRINT T7.14 step (2)+(5); FINAL_OUTLINE `thm:method-subtraction` proof plan | "Key compatibility property… induction" is the naive termwise argument that Ex D.1/Ex D.48 refute (single chain terms are not even $L^1$; suppression holds only for grouped expressions). | Restate as the precise conditional theorem (S29–S31). |
| OUR-3 | FINAL_OUTLINE `prop:dis-dispersion` ("drop the circle at infinity under MA3"), `thm:dis-moments` proof "insert, contract, compare" | For hadrons the Euclidean OPE informs only on $\vert \omega\vert \le\sqrt3M/Q$; "insert and compare coefficients" uses (5.6) as a convergent series. Analyticity and $Q$-uniform polynomial bounds follow from MA0 (Lemma C.64); only $n<n_0$ needs growth. | Thm C.50/Lemma C.64/Rem C.65/Thm C.66 route (S20–S22). |
| OUR-4 | FINAL_OUTLINE `prop:method-glauber-deformation` (also BLUEPRINT P7.19, L7.5) | "The $k^-$ contour can be deformed … to $\vert k^-\vert \sim\vert k_T\vert $": with a single deformed component the soft line's own pole limits the amplitude to $\kappa\sim k_T^2/\vert k^\pm\vert $ (Lemma D.20(b)); leaving $G_\delta$ with amplitude $\kappa\vert k_T\vert $ needs the simultaneous two-component deformation along $e_G$ (E.42). Deforming one component leaves $\vert k^+k^-\vert \sim\lambda^3$. | S32. |
| OUR-5 | FINAL_OUTLINE `prop:tmd-small-b` | Remainder "$+O(b_Tm)$" (copied from the reference). | $O((b_Tm)^p)$, $p=2$ for unpolarized leading-twist TMDs (twist 4), **verify**. |
| OUR-6 | BLUEPRINT L8.2/C8.7; FINAL_OUTLINE `lem:disall-fsi`, `thm:disall-factorization` | The distinction "remainder bounds on a real $\omega$-segment do not continue to the discontinuity" is absent. | Two routes (S27). |
| OUR-7 | `spec/refs_merged.bib` `Shifman2000` | Booktitle given as "8th International Symposium on Heavy Flavor Physics". | INSPIRE: *At the Frontier of Particle Physics* (World Scientific 2001), vol. 3, pp. 1447–1494. |
| OUR-8 | FINAL_OUTLINE `thm:dis-moments` / `thm:dis-ope` "(Euclidean $q$, or for each fixed Taylor coefficient in $\omega$)" | The forward on-shell partonic statement is at exceptional momenta and is not covered by the Euclidean theorem. | Sub-statements with separate tags (S19). |

### 2.5 Reader disagreements and how they were resolved

1. **Size of the strict-window residual.** R4 E12 says "$-\frac14C_A\chi^2$ only if the crossed graph carries the whole abelian weight, $-\frac18$ for an equal split". R3, R7 (C5) and R8 (C3–C6) agree on the parametrization residual $=-\frac12C_A\chi^2({\rm Re}\,p_{\rm opp})X$. The equal split $p_{\rm opp}=\frac12$ gives $-\frac14C_A\chi^2X$. The synthesizer read (E.51) on p. 217: $A_2=\frac12(-i\chi)^2(X^2+\frac14C_AX)$ with all four ordering pairs weighted $\frac14$, so the residual is $-\frac14C_A\chi^2X$. **R4's "$-\frac18$" is a slip.** The exact eikonal value $p_{\rm opp}=-iY/\pi$ gives 0.
2. **Off-shell Sudakov NLP sign.** R1 quotes "$t(2L^2+4L-4+2\pi^2/3)$ of c_regions R3"; R6 gives $t(2L^2-4L-4+2\pi^2/3)$ with $L=\ln(Q^2/m^2)$. With $L=\ln(Q^2/m^2)$, Table 5 at $t=10^{-10}$ (difference $9.71\times10^{-8}$) is reproduced only by the "$-4L$" form ($970.86\times10^{-10}$; the "$+4L$" form gives $1.155\times10^{-7}$). The difference is the sign convention of $L$ in c_regions ($L\to-L$). **Binding form:** $t(2L^2-4L-4+\frac{2\pi^2}3)$, $L=\ln(Q^2/m^2)$.
3. **Page offsets.** The task notes expected printed = physical − 1 for some segments. All eight readers found printed = physical throughout.
4. **Fig 39 caption** ("self-energies (c)(d) must be kept for space-like lines", R3 p. 63) and ERR-M27 (R6) concern the same wrong claim; it is counted once (ERR-M27).

---------------------------------------------------------------------------------------------------

## 3. What to adopt (incorporate or surpass)

**Level-of-detail codes.**
- **FP**: full proof in our text;
- **SK**: statement + numbered proof sketch with literature location;
- **ST**: precise statement + status paragraph;
- **RM**: remark;
- **EX**: worked example;
- **TAB / FIG**: table or figure.

Chapter numbers are those of FINAL_OUTLINE (= TOC v1). App M, N, O, P are the **new** appendices proposed in §5 (S1–S4).

**General rule.** Nothing from the reference is copied. Every adopted construction is re-derived by our writer, checked (script or hand) and presented in our conventions. Error corrections from §2 are applied, and primary literature is cited. The reference itself is not a citable source (S62).

### 3.a The conditional-theorem framework

| # | item (reference) | our target | level | how we surpass it |
|---|---|---|---|---|
| F1 | Every B/B′ result is a **conditional theorem** under numbered assumptions (Def 1.1; App D/E assumptions) | Ch1 `def:intro-tags` + new qualifier $R_{\rm cond}$ (S5); every [A] statement is split into an $R_{\rm cond}$ implication plus named assumptions | ST | Uniform across the whole book (the reference does this only in App C/D/E). Each assumption carries a label `asm:`, a status, a literature line, "used by", and an upgrade route (register, S6). Dependencies are machine-checked through `\uses{}` (App P). |
| F2 | Explicit **bridging hypothesis** from partonic PT to hadrons (Def 1.1) | `asm:intro-bridge` = MA1 + MA2 (+MA4); `def:intro-MA` keeps MA0–MA4 as umbrellas | ST | The reference's bridge is one informal sentence. We split it into region completeness, power-counting transfer and asymptoticity, and print it in every hadron statement (the existing "非微扰地位" line). |
| F3 | Precise meaning of "every order, leading power": partonic, IR-regulated, order by order, remainder $O(\lambda^aL^K)$ in an integral norm, uniform in $\epsilon$; not summable (Rem 1.2, Def D.2, §14 intro) | Ch1 `sec:intro-proof`; Ch8 `def:method-power-suppressed` | ST | Add the sharpness lesson: per-order exponents from the general method can be far from the true power ($a=\beta_R/3$, e.g. $1/243$ for the two-loop $(S,S)$ region), while explicit examples give the true $O(\lambda^2L^2)$ (Ex D.47 with the exact NLP). |
| F4 | **Error-type taxonomy**: scaling statement / pointwise bound / fibre-integrated bound / integral-norm bound / weak equivalence (E.1.3, Note E.20, Rem E.36(1)); "power counting is a scaling statement, not a bound" (Rem 3.13) | Ch1 `def:intro-error-types` (S7); used in all status tables and in App P | ST | The reference introduces it late (App E). We make it a book-wide vocabulary and require each step of each [A]/[P] proof to name its error type. |
| F5 | **Status tables** with columns step / result / status / literature (Tables 2, 3, 6, 7, 8; Table 1 with "key step / failure mechanism" and NP-factor columns) | Chapter status boxes (Ch6, Ch8, Ch9, Ch11, Ch13); `tab:summary-master` adds "瓶颈假设 / 升级路径"; App P `tab:appP-status` | TAB | Correct the reference's bookkeeping errors (ERR-M29). Add the error-type column and the assumption labels. |
| F6 | **"What is and is not proved"** opening lists and **self-correction remarks** (App C intro; Rem E.32, E.49; Note E.13 correspondence table "sketch in text ↔ precise version in appendix, with corrections") | Every core chapter opens with a 「本章证明了什么 / 没有证明什么」 box; every [A] chapter whose precise version lives in App M/N/O ends with a correspondence table (`tab:<key>-correspondence`) | TAB/RM | Uniform format; links are canonical labels, not prose. |
| F7 | Distinction between process grades and **statement** grades; "a model counterexample excludes a general proof, it does not compute real cross sections" (Thm 12.3 framing) | Ch1 misconception box; Ch17 opening | RM | Already our M28 idea; add the [V] evidence-type rule (model counterexample / explicit calculation / experiment). |
| F8 | "Dependency flowchart coloured by grade" (Fig 1, Fig 54, Fig 71) | `fig:intro-dependency` (existing, now with an $R_{\rm cond}$ colour); new `fig:appM-dependency`, `fig:appO-flowchart`; App P auto-generated graph | FIG | Generated from `\uses{}` rather than drawn by hand, so it cannot drift from the text. |

### 3.b Appendix C — the OPE

| # | item | our target | level | improvement |
|---|---|---|---|---|
| C1 | Euclidean segment (C.31): the Euclidean OPE informs only on $\omega\in\mathcal I_Q=\{iy:\vert y\vert \le\sqrt3M/Q\}$ (Rem C.2) | Ch6 `lem:dis-euclid-segment` | FP | — |
| C2 | Lemma C.47 (OPE on the segment → odd polynomial with controlled coefficients) + Lemma C.49 (Markov coefficient inequality) | Ch6 `lem:dis-ope-segment` [R, R_cond]; App K `lem:appK-markov` (math) | FP | State the chiral-suppression input as a named assumption part, and give the projector formula for $T_2$ explicitly. |
| C3 | **Thm C.50**: fixed-$n$ Taylor coefficients from the local OPE + analyticity + positivity + $Q$-uniform finite-subtraction dispersion relation; no spin sum | Ch6 `thm:dis-fixed-n` [R, R_cond] | FP | This is the precise version of what our `thm:dis-moments` currently assumes silently ("insert, contract, compare"). It fixes OUR-3. |
| C4 | **Lemma C.64** (dispersion relation from Wightman axioms, $Q$-independent exponents, positivity of Disc, $n_0>A+2$) + **Lemma C.63** (entire functions of controlled growth) | Ch6 `prop:dis-dispersion-np` [R, R_cond: `asm:intro-wightman`]; full proof in App M §M.8; `lem:appK-entire` (math) | FP | Correct (W2) (ERR-M25); add the slice edge-of-the-wedge sentence (ERR-m24). This replaces BLUEPRINT P5.4's "growth bound (verify Jost–Lehmann–Dyson)". |
| C5 | **Rem C.65**: low sum rules incl. the momentum sum rule ⟺ $T_2(iy)=o(y)$; Regge neither equivalent nor sufficient; fixed poles invisible in $F_2$ | Ch6 `prop:dis-low-moments` [R, R_def]; refine MA3 into `asm:intro-growth` | FP | Gives MA3 a precise, testable content and links it to the Burkhardt–Cottingham-type fixed-pole question (`conj:coll-bc`). |
| C6 | **Thm C.66** (non-perturbative moment theorem) under C.56–C.59 (+C.60 for $n<n_0$); RG-defined coefficients asymptotically free | Ch6 `thm:dis-moments-np` [R, R_cond]; assumptions `asm:intro-wightman`, `asm:intro-composite`, `asm:intro-np-ope`, `asm:intro-af-coeff`, `asm:intro-growth` | FP (App M), statement in Ch6 | Fix the mass-mixing norm (ERR-m24). State explicitly what is new relative to the PT theorem: $t_n$ for all even $n$ from the OPE, and the moment identification for $n<n_0$ only under growth. |
| C7 | Cor C.52 + Rem C.53: weak $x$-space convergence under (Φ); a pointwise $O(1/Q^2)$ is impossible from the OPE; Hausdorff-problem caveat | Ch6 `cor:dis-weak-xspace` [R, R_cond]; complements `rem:dis-nonuniform` ($\sin(Q^2x)$) | FP | Combine with our stronger moment lemmas (distributions, $\delta'$, Carlson; App K). |
| C8 | Perturbative machinery: Lemma C.11, **chain expansion Lemma C.12** (one identity giving both the Zimmermann identities and the OPE identity), Thm C.13, Cor C.14, Ex C.15, frozen-$q$ bilocal normal product (Def C.21), Lemma C.22 (absolute integrability), Lemma C.23 (contact terms), Thm C.25(i) | App M §M.2–M.3 | FP for (i); Thm C.8 and Weinberg cited | Add the explicit routing lemma for frozen $q$ (ERR-m24) and the disconnected-$\omega$ extension (Cor C.18). |
| C9 | Ass C.24 (remainder) + Lemma C.29 (derivative bounds from homogeneity, $O(4)$, Lagrange identity) + Lemma C.30 (order-by-order uniqueness) + Thm C.25(ii)–(iv) (scaling of *reduced* coefficients from uniqueness) + Lemma C.32 / Cor C.33 (coordinate-space remainder) | App M §M.4 with `asm:appM-remainder` | FP given the assumption | **Surpass:** attempt to discharge C.24 via Anikin–Zav'yalov 1978 / Zav'yalov 1990 plus uniqueness (ERR-M26). If successful, `asm:appM-remainder` becomes a cited theorem. The refs agent verifies the scope. |
| C10 | Rem C.9 counterexample ($\delta\ge\omega$ is insufficient; degrees must be vertex additive) | App M §M.2 RM; Ch2 renormalization remark | RM | — |
| C11 | Ex C.26 (tree OPE = Taylor expansion of $\varphi(x)$), Ex C.27 (unreduced coefficients violate scaling) | App M EX | EX | Use the sharpened $-\kappa\pi^2/(2q^4)$, with no log (ERR-m23). |
| C12 | Thm C.35 (massless QCD, Euclidean non-exceptional; BPHZL vs DR+$R^*$; cited) + Lemma C.36 (exact uniqueness from the log-polynomial structure) + **Rem C.37** (forward on-shell = exceptional) | Ch6: split `thm:dis-ope` into `prop:dis-ope-euclid`, `prop:dis-ope-gi`, `prop:dis-ope-forward` (S19); App M §M.5 | ST/FP | Precise re-tagging: the graph-by-graph Euclidean expansion [A] under the binding decision D3 (FINAL_OUTLINE §0.9 item 4), with upgrade path [R, R_PT] if the refs agent confirms the cited scope for QCD with quarks and ghosts; the gauge-invariant reduction [A]; the forward on-shell step [A] with our exact-in-$\varepsilon$ $O(\alpha_s)$ check (c_dis). |
| C13 | BRST (C.26)–(C.28), Lemma C.39 (local cohomology $H(s)$ not $H(s\vert d)$), Thm C.40 (Joglekar–Lee sketch), Lemma C.41 (aliens vanish) | Ch2 `thm:prelim-composite-renorm`; App J; App M §M.6 | SK | Add the forward on-shell caveat (Hamberg–van Neerven, Collins–Scalise; ERR-M24) and Joglekar 1977, Hollands 2008 (ERR-M26). |
| C14 | Lemma C.42 (twist-2 GI classification by collinear twist $t=d-h$, with table), Lemma C.43 (twist parity = chirality, symmetric traceless), Rem C.48 (odd-twist coefficients vanish in massless PT by $\gamma$-parity, DR-safe; non-perturbatively an input) | Ch6 `lem:dis-twist-classification` [R, R_def], `lem:dis-twist-chirality` [R, R_def], `prop:dis-chiral-suppression` [R, R_PT]; Ch7 (good/bad components) | FP | Add the mixed-symmetry caveat (transversity is twist 2 and chiral odd; ERR-m20). |
| C15 | Prop C.44 ((O2) in PT under (B1)(B2)) | Ch6 `prop:dis-ope-gi` [A] / App M with `asm:appM-brst-ope` | SK | — |
| C16 | Prop C.46 (coefficient RG *derived* from uniqueness) | Ch6 `prop:dis-ope-rg` proof route | FP | — |
| C17 | Prop C.54 (fixed-order all-spin sum: scaleless matrix elements force twist 2; Taylor-coefficient contradiction argument) + Rem C.55 (amplitude form with the odd quark extension and gluon factor 2) | Ch6 `prop:dis-ope-forward` (with `asm:appM-forward`); Ch9 | SK + EX | c_dis gives the exact one-loop instance ($N\le8$). |
| C18 | Prop C.68 (rearrangement freedom of the OPE basis), Rem C.67 (practical OPE routing-dependent and gauge-breaking), Rem C.69 (renormalon absorption: two conjectural ingredients) | Ch20 `prop:power-rearrangement` [R, R_def], `rem:power-practical-ope` | FP/RM | Add the O($N$) σ-model as the proven case of renormalon–higher-twist cancellation (ERR-m19). |
| C19 | Rem C.61, C.62 (Bostelmann; instantons $(\Lambda/Q)^{b}$; vacuum OPE has no $1/Q^2$), supporting results list | Ch5 `thm:ee-ope`, `conj:ee-np-ope`; Ch20 `rem:power-np-status` | RM | Add the 't Hooft model (already in our plan) and the Gross–Neveu Borel summability. |
| C20 | Fig 54 (dependency), Fig 57 (handbag as AB part vs reduced graph), Fig 61 ($\omega$-plane with $\mathcal I_Q$), Fig 62 (scale line), Tables 2–3 | `fig:appM-dependency`, `fig:appM-handbag-ab`, `fig:dis-euclid-segment`, status tables | FIG/TAB | — |

### 3.c Appendix D — the precise Collins subtraction method

| # | item | our target | level | improvement |
|---|---|---|---|---|
| D1 | **Ex D.1**: three counterexamples to naive induction (incomparable approximant non-integrable; accuracy needed on subtraction terms; single chain terms never $L^1$) | Ch8 `ex:method-naive-induction` [R, R_PT] | EX (full) | Fixes OUR-2; becomes the motivation of `sec:method-subtraction`. |
| D2 | Def D.2 (integral-norm power suppression uniform in $\epsilon$; the two reasons) | Ch8 `def:method-power-suppressed` | ST | — |
| D3 | Def D.3 + Lemma D.4 (regions = per-line mode assignments; pinch sets affine; per-line meet = intersection) | Ch8 `def:method-regions` (revised), `lem:method-meets` (math) | FP | — |
| D4 | Fig 63 (Hasse diagram of the 9 leading regions of the two-loop vertex; meet-closed) | `fig:method-hasse` (owner Ch8 by first use; Ch4 pointer only) | FIG | — |
| D5 | Def D.5 + Lemma D.6 + Fig 64 ($\lambda$-dependent neighbourhoods $N_R$, $U_R$, $\beta_R=3^{h(R)-h_*}$; covering) | Ch8 `def:method-neighbourhoods`, `lem:method-covering` (math); `fig:method-neighbourhoods` | FP | — |
| D6 | Ass D.7 (A1)–(A4) + Note D.8 (status of each; the corrected no-Glauber condition $\vert k^+k^-\vert \gtrsim k_T^2$ replacing "$\kappa\sim\vert k_T\vert $"; Łojasiewicz exponent 2; endpoint assignments) | App N §N.2: `asm:appN-contour`, `asm:appN-envelope`, `asm:appN-separation` ((A2) becomes a definition: meet-closure) | ST | Renamed (GA1)–(GA4) to avoid clashing with our [A] tag (S8). |
| D7 | Def D.9 (H1)–(H3) + **Thm D.10** (three-line covering proof) | Ch8 `def:method-collins-conditions` ((CS1)–(CS3)); `thm:method-subtraction` split into `thm:appN-subtraction` [R, R_cond] and the [A] content `asm:appN-collins` | FP | Fixes OUR-2. Separates the trivial covering argument from the hard estimates. |
| D8 | Lemma D.11 (chain expansion), **Lemma D.12** (pairing decomposition via meets), **Cor D.13** (product formula $\prod(1-T_R)$ under (Com)(Abs); Möbius/meet-irreducible proof; (CS1)(CS2) ⟺ grouped power counting) | Ch8 `prop:method-chains` (exists) + `lem:method-pairing` (math) + `prop:method-product` (math); App N proofs | FP | Our `prop:method-chains` is upgraded; the correct forest analogy (Rem D.15) is added. |
| D9 | Prop D.16 (meromorphic + uniformly bounded ⇒ no pole; reused in Thm D.44(a)) | Ch8 `lem:method-no-pole` (math) | FP | — |
| D10 | Ass D.17 (values of divergent chain terms are representation dependent; (D1) non-trivial; checked in the triangle) | Ch3 `rem:ir-regions-values`; App N `asm:appN-values` | RM/ST | Ties the method of regions (`prop:ir-regions-minkowski` [P]) to Collins subtraction honestly. |
| D11 | Defs D.18, D.19, D.21, D.22: explicit idempotent approximators ($\mathcal P_\pm$, $\mathcal P_A=g_T+n_A\otimes n_B$, soft $n_A^\mu n_{B\nu}$, DA projector, rapidity-regularized $n_A(y_A),n_B(y_B)$); no new denominators; $i0$ inherited | Ch8 `def:method-collinear-approx`, `def:method-soft-approx` (revised to the idempotent-projector form); Ch13, Ch18 | ST | Converted to our $n_A,n_B$ notation; consistent with VF-WL-10/11. |
| D12 | **Lemma D.20** + Fig 65: $i0$ compatibility; the soft line's own pole limits $\kappa\sim k_T^2/\vert k^+\vert $; opposite orientations give a Glauber pinch | Ch8 `lem:method-i0-compat` [R, R_PT]; fixes OUR-4 | FP | Merged with App E's two-component deformation (D↔E link). |
| D13 | Lemma D.23 (algebra of approximators: idempotence, (Com); (Abs) fails exactly by the transverse coupling of a direction-flipping line) + Rem D.24 | Ch8 `rem:method-abs-failure`; App N | RM | Add the uncovered edge case (ERR-m25) to the assumption. |
| D14 | Lemma D.25 + **Table 4** (complete error table) + telescoping (D.18) + Lemma D.26 | Ch8 `tab:method-errors` (full page) + `lem:method-local-accuracy` [R, R_cond] | TAB/FP | Converted to our notation; a column for the error type is added. |
| D15 | Ass D.27 (cut-summed LCPT representation (X1)–(X3)); why single cut graphs and gluon masses fail | Ch8 `sec:method-unitarity`; `asm:appN-cutsum`; partly *provided* by App O's LCOPT lemmas | ST | Our App O supplies (X1) explicitly via Lemma E.15/E.21 for DY-type graphs. This is a genuine strengthening: the reference keeps D.27 as an assumption even where App E builds the representation. |
| D16 | Prop D.28 (DIS: unphysical region has only A/H modes; moments via complex-$\omega$ uniformity and the Cauchy estimate; $x$ space via cut graphs; threshold non-uniformity) | Ch9 `prop:disall-two-routes` [R, R_cond] | FP | Fixes OUR-6; links Ch9 to Ch6 precisely. |
| D17 | Prop D.30 (thrust zero-bin scaleless by $a^{-\epsilon}$ scaling) | Ch14 `thm:scet-thrust` proof; Ch15 | SK | — |
| D18 | Ass D.31, Prop D.32, Note D.33 (DY = cut-summed Glauber cancellation + combinatorics as in $e^+e^-$; disjoint-block proof) | Ch11 status; App N §N.5 `prop:appN-dy`; interface `cor:appO-interface` | FP given assumptions | — |
| D19 | Ass D.34, Prop D.35 (TMD rapidity window $c_0L\le Y\le c_1L$, $\vert y_k\vert \le(1+a)L$), **Prop D.36** (zero-bin = soft factor; one-loop absorption), **Lemma D.38** (square root is an exact identity; CS from asymptotic linearity) | Ch13 `prop:tmd-zero-bin-soft`, `lem:tmd-sqrt-identity` [R, R_def], `rem:tmd-rapidity-window`; `asm:appN-tmd` | FP/ST | Add the one-loop verification of (T2) from c_tmd ($Y\coth Y$, equal slopes, cancellation of $y_B$ and $\sigma$) and correct the self-energy claim (ERR-M27). |
| D20 | Def D.21 subtlety: the rapidity-regularized collinear factor at fixed $x$ differs from the light-front matrix element by $e^{2(y_B-y_k)}$, not small near $y_B$ | Ch13 `rem:tmd-order-of-limits` | RM | Complements c_tmd caveat 4. |
| D21 | Ass D.39, **Prop D.40** (exclusive: integrand-level colour-singlet soft cancellation; "dipole cancellation = smallness of the approximation error"; endpoint conditions on partonic subgraphs; failure for twist 3 and transverse photons) | Ch18 `prop:excl-soft-cancel` [R, R_cond], `asm:appN-endpoint` | FP/ST | Correct the transverse-photon mechanism (ERR-M17) and the log in the remainder (ERR-m15). |
| D22 | Ass D.41 (U2) partial proof (Taylor subtraction commutes with linear substitution); Prop D.42 (DIS subtraction terms factorize exactly); Ass D.43 discussion (why (Z2) is a genuine input) | Ch9 `prop:disall-factorized-subtraction` [R, R_cond]; App N `asm:appN-uv`, `asm:appN-multren` | FP/ST | Fix (U1) (ERR-M28); state the DR route with on-shell partonic targets (scaleless PDFs) as our working scheme, with the (Z3)-type identification as an assumption. |
| D23 | **Thm D.44** + recursion (D.25) for coefficients | Ch9 `thm:disall-renorm-compat` [R, R_cond] | FP | — |
| D24 | **Ex D.47** (complete one-loop off-shell triangle: closed forms; $k^-$ residues; absolutely convergent iterated integrals for $0<\epsilon<1$; (D.32); zero-bin as $1/\epsilon_{\rm UV}-1/\epsilon_{\rm IR}$; Fig 69) | Ch8 `ex:method-sudakov-subtraction` (enlarged) + App N `prop:appN-triangle-exact` [R, R_PT] | EX + FP | **Surpass:** state the exact remainder. With $\tilde Q^2=2PP'$ and $Q^2=(\tilde Q^2+m^2)^2/\tilde Q^2$: $r=I-$(D.32)$=-\frac{4m^2}{Q^4}+\frac{m^4}{Q^6}(L^2-15+\frac{\pi^2}3)+O(\frac{m^6}{Q^8}L^2)$, a full $\lambda^2$ with no logarithm at NLP (synthesizer, `work_SYN/triangle_remainder.py`; R6's $d=4$ remainder density integrates to the same value to 12 digits). Replace the Table 5 fit (ERR-m25). (S30) |
| D25 | **Ex D.48** (two-loop ladder: $r=\Delta\mathsf H_0\Delta K_2\Delta K_1$; $C_1\to\hat{\mathsf H}^{[1]}$; $C_H\to$ two-loop coefficient; grouping necessary) + Fig 70(b) | Ch9 `ex:disall-ladder` + `fig:disall-ladder-regions` | EX | Three regions, including the hard one (fixes ERR-M11). |
| D26 | Table 6 (status of every App D item) | App N `tab:appN-status`; App P | TAB | — |

### 3.d Appendix E — the Glauber cancellation in DY

| # | item | our target | level | improvement |
|---|---|---|---|---|
| E1 | Architecture with exact interface (Thm E.8/E.9, Cor E.10, Notes E.11–E.13, Fig 71) | Ch11 `sec:dy-theorem` status layer; App O `thm:appO-main` [R, R_cond], `cor:appO-interface` | ST + FP | Fix the bookkeeping (ERR-M29), credit Aybat–Sterman and DGOPS (ERR-M32), and attach error types to every step. |
| E2 | **Lemma E.15** (LCOPT from Feynman integrals at finite $\eta_0$: absolute convergence via Weinberg/Hahn–Zimmermann, $\dim W\le\vert L_W\vert-1$, Fubini, sector decomposition) | App O §O.2 `lem:appO-lcopt` [R, R_PT] | FP | Add the numerical check on 8 graphs (R7 C1) as an exercise/illustration; light-front literature (Kogut–Soper, BPP; refs agent: Chang–Yan, Ligterink–Bakker). |
| E3 | Lemma E.16 (instantaneous terms; instantaneous loops independent of external minus energies) + Note E.17 | App O `lem:appO-numerators` [R, R_PT] | FP | — |
| E4 | Ass E.18: (i)(ii) assumptions; **(iii) provable** | App O `asm:appO-lcopt` ((i)(ii) only); App J `lem:appJ-cut-hermiticity` [R, R_def] discharges (iii) | ST + FP | **Surpass:** prove (iii) (R7 E7). |
| E5 | Def E.2/E.3 (orientation = property of LCOPT intermediate states; standard flow: initial $+k^-$, final $-k^-$; cut $\delta$ soft-free) + **Lemma E.22** | Ch11 `lem:dy-poles-orientation` [R, R_PT]; App O §O.3 | FP | Replaces the line-by-line pole tables (c_glauber §1.2, kept as an example). Generalizes Lemmas 8.2 and 9.5. |
| E6 | Def E.4 (Glauber pinch incl. inter-term pinches; why inter-term pinches obstruct Ward identities; one-component deformation does not leave $G_\delta$) | Ch3 `def:ir-glauber` remark; Ch8 `rem:method-two-component`; Ch11 | RM | New misconception M31 (S57). |
| E7 | Lemma E.19 (Glauber power counting, scaling) + Lemma E.21 ($V_H$ at $\tau=0$ on both sides; $\mathcal E$ unweighted) | App O `lem:appO-glauber-pc` (scaling), `lem:appO-hard-locality` [R, R_cond] | FP | — |
| E8 | **Ex E.23 / Ex E.37** (spectator model in LCOPT: two orderings = two covariant propagators; $k^-$ integral = equal-time $k_T$ transfer; single orderings regularization-dependent, the sum not) + Fig 76 | Ch11 `ex:dy-spectator-lcopt`; combined with `prop:dy-abelian-model` | EX | Combine with our explicit IR-regulated kernel $\chi(b)=-\frac{e_Ae_B}{2\pi}K_0(m_gb)$ and the $\Delta$-integrated cancellation (c_glauber §1.5, c_dy §7). |
| E9 | **Lemma E.24** (exact light-cone cut-position identity with insertions; at most two insertion terms) + Note E.25 (largest-time interpretation) + **Lemma E.26** (closed-time-path form; FSI internal to $J_A$ vanish) | Ch8 `prop:method-fsi` (precise version); App O `lem:appO-cut-position` (math), `lem:appO-unitarity` [R, R_cond] | FP | Our c_glauber has only the all-internal case. Also reused in Ch9 (DIS FSI), Ch10 (SIA), Ch11. |
| E10 | Note E.27(1): why one light-cone time per jet; "measurement compatible" = identity operator between cut states | Ch11 `rem:dy-one-time-per-jet`; Ch17 | RM | Credit Aybat–Sterman 2009. |
| E11 | **Lemma E.28** + Note E.29 (equal-time localization; contact term $c[O(0),V_H(0)]$, $c=R_\downarrow(0)/R(0)$; $c=\theta(k^+)$ vs $\frac12+O(\delta)$; spectators decouple from eikonal-region gluons) | App O `lem:appO-equal-time` (math) | FP | Use the corrected proof of (iii) and the window-shape statement (ERR-m26). |
| E12 | (E.30)–(E.32): SS localization error with genuine log; Hermitian $V_G$ | App O `prop:appO-ss-localize` [R, R_cond] | FP | Use the vertex sign $+ig$ (ERR-m26) and state the bound as absolute. |
| E13 | Non-commuting insertions: ordering weights $\prod z_j/\prod_m\sum_{l\ge m}z_{\pi(l)}$, correlated between jets | App O `lem:appO-joint-localization` [R, R_PT] for single-pole external factors | FP | **Surpass:** this replaces the inconsistent E.33(c1) (ERR-S3) by a lemma. The general case is folded into `asm:appO-mixing`(a). |
| E14 | Def E.30, **Prop E.31** (family cancellation for non-coincident connections on window cores; $\prod_l(-iG_lX_l+iG_lX_l)=0$) | App O `prop:appO-ss-cancel` [R, R_cond] | FP | **Surpass:** side-independent window construction (suggested by R7: build $\Theta$ from $P_A^-$, cut-line energies and core lines only) to remove window-edge terms — to be checked by the App O writer; if it fails, keep the edge terms in `asm:appO-deformation`(c). |
| E15 | Ex E.38 + Lemma E.48 + Rem E.49 (the $p_{\rm opp}$ parametrization; residual $-\frac12C_A\chi^2{\rm Re}\,p_{\rm opp}X$; common ordering ↔ RS regulator) | Ch11 `prop:dy-eikonal-twogluon` (new result, S37) + App O `lem:appO-glauber-operator` [R, R_def] | FP | **Surpass:** the exact eikonal computation gives $p_{\rm opp}=-iY/\pi$, hence ${\rm Re}\,p_{\rm opp}=0$ and a reggeization phase (ERR-S1). |
| E16 | Ass E.33 (a)(b)(c2), Ass E.34 | App O `asm:appO-mixing` ((a)(b)(c2); (c1) replaced), `asm:appO-envelope` | ST | Status lines updated with the exact $O(g^4)$ eikonal result. |
| E17 | Rewriting $\mathfrak r_R$ with the entire carrier $\phi(x)=2\sqrt\pi e^{-x^2}$ (E.34); Prop E.35 (one-sidedness, weak); Rem E.36 (why only weak; SA/AS construction; subtraction terms of rewritten forms) | App O §O.6 | FP | Check the boundary-layer step against our neighbourhood definition (ERR-m27). |
| E18 | **H-emission endpoint obstruction** ($c_j=\theta(k_j^+)$ non-analytic) | App O `asm:appO-deformation`(d); Ch22 open problem | ST | Unified with the coincident SA/AS obstruction (ERR-S3 consequence). |
| E19 | **Glauber direction** $e_G=n_B-n_A$, (E.42), Rem E.40, Fig 78 | Ch8 `rem:method-two-component`; App O §O.7; `fig:method-glauber-direction` | FP/FIG | Fixes OUR-4. |
| E20 | **Lemma E.41** (no singularity crossed; subtraction-term eikonal denominators must be past-pointing) | App O `lem:appO-no-crossing` [R, R_PT] | FP | Also used in Ch13 for the staple direction. |
| E21 | Def E.42 + **Prop E.43** (graded configurations; routing; convex gluing; constants $\kappa^2<1/(2KN_C^2)$, $c=\min(\kappa^2,\delta/2)$) | App O `prop:appO-target` [R, R_PT] | FP | — |
| E22 | Ass E.44 (a)–(d) | App O `asm:appO-deformation` | ST | (b)(c) are needed even for abelian $\mathcal G_0$ — must be said in Ch11's status paragraph. |
| E23 | **Prop E.45** (quantitative eikonal bounds on the deformed contour; Grammer–Yennie ratio (E.47); $O(1)$ failure on the real contour) | Ch8 `lem:method-soft-accuracy` upgraded in the Glauber core; App O `prop:appO-eikonal` [R, R_PT] | FP | — |
| E24 | Prop E.46 + the **single-cut-graph identity** $iQ_a/(k^-+i0)+iQ_s[\frac1{k^-+i0}-\frac1{k^--i0}]=iQ_a/(k^--i0)$ ($Q_s=-Q_a$: a single cut graph gives the *future* line; past only after rewriting) | Ch11 `ex:dy-future-vs-past` [R, R_def]; App O `prop:appO-past-wilson` [A] | EX/SK | Pedagogical highlight; also in Ch4 (Coulomb phases) and Ch13 (process dependence). New misconception M33. |
| E25 | Prop E.47 ($T[\mathcal U^{(-)}]=U_I(0,-\infty)$ unitary; role of $v^0>0$) | Ch8 `lem:method-soft-unitarity` (past version); App O | FP | Pair it with the c_tmd caveat that for *time-like* non-light-like past lines path order is anti-time order. |
| E26 | Prop E.50 + **(E.52)** $\sum_X\vert X\rangle e^{ib\cdot P_{XT}}\langle X\vert=e^{ib\cdot\hat P_T}$, commuting with light-cone evolution; Rem E.51 (compatible with measurement ⟺ the measurement operator commutes with $U$ and the $\tau=0$ insertions) | Ch13 `lem:tmd-glauber`; Ch17 `prop:break-measurement` [R, $R_{\rm cond}$] | FP | Becomes the unifying criterion of Ch17 (contrast $\Pi_h$, $\Pi_{\rm gap}$). |
| E27 | Proof (S1)–(S8) with three error types; Rem E.52 + Tables 7–8 | App O §O.9–O.10 `tab:appO-checklist`; Ch11 `tab:dy-status` | TAB | Corrected (ERR-M29, m27). |
| E28 | Rem E.53 (DFT outside the premises; location via $\delta_Ak^+$ in (E.53)) | Ch3 `prop:ir-bn-failure` status; Ch11 `rem:dy-dft-premises` | RM | Add FGT 1984, Andrási 1981, Di'Lieto 1981, Catani–Ciafaloni–Marchesini 1986, and BRS 1984 / CSS 1989 §10.2 (power corrections themselves non-factorizable at $m^4/s^2$). |
| E29 | Rem E.54 ($pp\to h_1h_2X$ fails at the one-sided-rewriting step; the gap of Conj 12.1 is located there), Rem E.55 (gaps: (E.54), survival), Rem E.56 (RS dictionary), Rem E.57 (double DY) | Ch17 (`thm:break-tmd`, `prop:break-hh-diffraction`, `thm:break-double-dy` status); Ch14 `rem:scet-glauber-dictionary`; Ch11 `conj:dy-coloured-final` status | RM | Corrected argument for Rem E.54(b) (ERR-M31); Gaunt vs SYZ (ERR-M30). |

### 3.e Main-text items, explicit calculations, figures and examples

| # | item (page) | our target | level | improvement |
|---|---|---|---|---|
| T1 | Fig 3 (two-panel light-cone geometry: hyperbola; logarithmic plane, boosts = translations) | `fig:prelim-lightcone` (Ch2; upgrade from optional to required) | FIG | — |
| T2 | Fig 10 (modes in exponent space $(a,b,c)$: H, C$_A$, C$_B$, usoft on the plane $c=\frac{a+b}2$, TMD-soft at the centre, Glauber below) | Ch3 `fig:ir-mode-exponents` | FIG | Label "usoft" vs "soft" per our D3.8. |
| T3 | Fig 12 (power of $\lambda$ per connection type) | Ch3 `tab:ir-connection-powers` | TAB | Add the super-leading rows $(0,0)$, $(0,1)$ (ERR-S4). |
| T4 | Remark 3.3 (scaling-limit treatment of soft lines in Coleman–Norton) and Fig 8(c) (DY initial/final soft gluons; active vs spectator poles on opposite sides) | Ch3 `prop:ir-coleman-norton` remark; Ch11 motivation | RM | — |
| T5 | Prop 3.5 consistency argument ($\mu$-independence + pole cancellation fix $(c_h,c_1,c_2,c_s)=(1,-1,-1,1)$; double log $(a-b)^2$) | Ch4 `rem:sudakov-consistency` | RM | Complements our explicit region integrals; the constant $\pi^2/3$ is added. |
| T6 | Fig 9 right (regions as corners of the $(\ln k^+,\ln k^-)$ plane) and Fig 69 | `fig:momentum-regions` (exists) + `fig:method-sudakov-plane` (Ch8) | FIG | — |
| T7 | Lemma 3.7 boost + dimension proof with Fig 11 | App E `prop:appE-degree` (exists); add Fig 11 as `fig:appE-boost` (optional) | FIG | — |
| T8 | Thm 3.14 "pure gauge" argument ($F_{\mu\nu}[\mathcal A_{\rm eff}]=0\Rightarrow\mathcal A_{\rm eff}=-\frac ig(\partial U)U^\dagger$, $\psi\to U^\dagger\psi$) | Ch8 `rem:method-pure-gauge` (heuristic; step 2 = BRST content [A]); Ch14 cross-reference with collinear gauge invariance | RM | Corrected status (ERR-M6) and $i0$ (ERR-M5). |
| T9 | (3.15) + Fig 16 (telescoping with $B_0..B_3$; sign matched to $W^{(1)}[w^-,0]=gt^a(1-e^{-ik^+w^-})/k^+$) | App F `sec:appF-one` example | EX | — |
| T10 | Thm 4.1's four-part status layout (i) Wightman analyticity with the exact one-subtraction condition $\int\rho/s^2<\infty$ ⟺ finite Adler function; (ii) PT; (iii) OPE-conditional; (iv) smearing identity with computability as a separate assumption | Ch5 `prop:ee-analytic` (add the exact condition), `rem:ee-status-layout` | ST | Our c_ee route (Laurent polynomial argument) is stronger for (ii). |
| T11 | Fig 18 (classes of $O(\alpha_s^2)$ cuts; "poles up to $1/\epsilon^4$ per class") and Fig 19 (sum over cuts = Disc of the forward $J\otimes S$; contour movable at $O(Q)$) | Ch5 `fig:ee-cutsum-disc` (new) | FIG | Add the Furry remark (singlet $(\sum e_q)^2$ from $O(\alpha_s^3)$). |
| T12 | Fig 21 (graphical OPE: twist ↔ extra partons, $\lambda$ per transverse gluon, $\lambda^2$ per quark pair) | Ch6 `fig:dis-twist-graphical` (optional) | FIG | — |
| T13 | Fig 22 (LL DGLAP: strongly ordered ladders, simplex volume $L^n/n!$) | `fig:dglap-ladder` (exists) caption enriched | FIG | — |
| T14 | Lemma 6.1/Prop 6.2 Clifford projection and normalization chain ($\int d^4k\to P^+\int d\xi$; $\int\frac{dk^-d^2k_T}{(2\pi)^4}{\rm Tr}[\gamma^+J]=2f$; $\frac12\xi P^+\gamma^-$ = spin-averaged projector) | Ch8 `def:method-collinear-approx`; Ch9 `prop:disall-h2` | FP | Add the colour projection (ERR-m10). |
| T15 | Figs 24–25 (recursion on the two-rung ladder) | Ch9 `fig:disall-ladder-regions` | FIG | With the hard region (ERR-M11). |
| T16 | Remark 6.7 + Fig 27 ($(\xi P+q)^2=Q^2(\xi-x)/x$; current jet merges into $H$; endpoint $\xi\to x$ → plus distributions and threshold) | Ch9 `lem:disall-fsi`; Ch12 motivation | RM | — |
| T17 | §6.4 + Rem 6.8 (gluon PDF from $k^+A^j-k^jA^+$; light-cone-gauge pitfalls ↔ Wilson-line direction) | Ch7 `def:pdf-gluon` remark; Ch8 `prop:method-gy-suppression` | RM | — |
| T18 | Prop 7.1/Cor 7.2 graph-by-graph traces; Figs 29–31 ("coefficient function = cut graph minus its collinear approximation": ISR² ↔ ladder; ISR–FSR interference ↔ Wilson-line graphs) | Ch9 `fig:method-coeff-minus-coll` (new) + `ex:method-dis-oneloop` | FIG/EX | Our c_pdf/c_dis computations are complete (virtuals, gauge independence, all kernels). |
| T19 | Lemma 8.2, Cor 8.3, Prop 8.4 (two-level proof), Lemma 8.6 (three arguments), Rem 8.5 (when $S\neq1$) | Ch10 `lem:coll-final-poles` [R, R_PT], `lem:coll-unobserved-jet` [A], Ch8 `lem:method-soft-unitarity` | FP/SK | Add an observable ⇔ soft-function table (R3 gap 10) in Ch10/Ch15. |
| T20 | Thm 8.1's explicit hypothesis: FF multiplicative renormalization is an independent input (FF moments are not local operators) | Ch7 `rem:pdf-ff-multren`; Ch10 `thm:coll-sia` status | RM | — |
| T21 | Example 10.1 (rapidity divergence from the unintegrated Wilson-line graphs, $\frac{\alpha_sC_F}{\pi^2}\frac{\xi}{(1-\xi)k_T^2}$, read as double counting with the other hadron) | Ch13 `ex:tmd-oneloop` (add this reading as its first step) | EX | Coefficient verified in c_tmd. |
| T22 | Prop 10.4 compact CS derivation ($\frac12[\ln\tilde S(+\infty,y_n)-\ln\tilde S(+\infty,y_B)-\ln\tilde S(y_n,y_B)]=\frac12[-a-2(y_n-y_B)c]$) | Ch13 `prop:tmd-evolution` proof sketch | SK | Ties to `lem:tmd-sqrt-identity`. |
| T23 | Thm 10.6 via **PT** (exact for any $\theta$: the $\theta$ term is C-even + CPT) with the full matrix-element proof; $f_1^{[+]}=f_1^{[-]}$; Fig 41 ($\mp i\pi\delta(k^+)$ mechanism) | Ch13 `thm:tmd-sivers-sign` proof | FP | Corrected details (ERR-m14). |
| T24 | Lemma 11.3 + Fig 45 (colour transparency $W_n(b_1)W_n^\dagger(b_2)=1+O(b\Lambda)$); Fig 44 (hard vs Feynman mechanism; endpoint area $c(1-\ln c)$) | Ch18 | EX/FIG | Combine with our exact $R_{\rm as}(c)$ curves (c_exclusive). |
| T25 | §13 intro/§13.3 ("SCET proofs are not more rigorous than Collins'"; three premises mapped to Collins' three difficulties) | Ch14 `rem:scet-assumptions` (opening and closing) | RM | Add the RS dictionary (E29) and the corrected $i0$/direction statement (ERR-m18). |
| T26 | (14.1) TMC coefficient $\frac{n(n-1)}{n+2}\frac{M^2}{Q^2}a_{n+2}$ (verified) | Ch6 `prop:dis-tmc` / `ex:dis-tmc-n2` | EX | — |
| T27 | Fig 52 (bubble chain; Borel plane with $\mathcal C_\pm$) | `fig:renormalon-chain` (exists) + `fig:power-borel-plane` (exists in plan) | FIG | — |
| T28 | §14.3 (threshold resummation as a nested factorization bounded by the outer one; the threshold region analysis is an extra input) | Ch12 `thm:thr-refactorization` status paragraph | ST | Our plan has the formulas the reference lacks. |
| T29 | App A (Feynman-parameter Landau proof with $\eta_j=\alpha_j\partial_j\mathcal F$, envelope theorem, homogeneity; caveats) | App D `sec:appD-alpha` (alternative proof) | FP | Our constraint-preserving deformation is kept as the main proof. |
| T30 | App B (precise test-function class; (B.2); $d$-dim kernels with the averaging convention; (B.8)) | App A `sec:appA-plus` (test functions) and App C `sec:appC-msbar` ($d$-dim kernels, averaging conventions) | FP | — |

---------------------------------------------------------------------------------------------------

## 4. What we already do better, and what the reference lacks

### 4.1 Whole topics in our 22-chapter plan that are absent from the reference or reduced to a paragraph

| topic | reference | our plan |
|---|---|---|
| Sudakov form factor to all orders: $HJJ/S$, $K+G$, cusp, webs, multi-leg IR poles (dipole formula and its three-loop failure), Coulomb phases, timelike strict collinear factorization | one-loop region example only (Prop 3.5) | Ch4 (12 pp): `thm:sudakov-factorization`, `prop:sudakov-kg`, `prop:sudakov-webs`, `thm:sudakov-ir-poles`, `prop:sudakov-dipole-violation`, `prop:sudakov-coulomb`, `prop:sudakov-amplitude-factorization` |
| Threshold resummation with formulas: Mellin exponent; $A^{(1)}$ check of $8C_F\mathcal D_1$; large-$N$ dictionary; prescriptions | (14.4) + a figure, no formulas | Ch12: `thm:thr-refactorization`, `prop:thr-oneloop` (verified), `rem:thr-prescriptions`, `prop:thr-nlp` |
| Jets, event shapes, NGLs (BMS), SLLs, IR safety of algorithms, hadronization $1/Q$ | thrust (13.3)–(13.4) and Rem 14.2 only | Ch15 |
| Small $x$: BFKL, BK/JIMWLK, $k_T$ factorization status, saturation, Kovchegov–Tuchin, DMXY | one paragraph (§12.6) | Ch16 |
| Polarized DIS ($g_1$, Bjorken with the verified $a^2$ coefficient, axial anomaly and the scheme dependence of $\Delta\Sigma$, BC, WW), transversity (evolution, Soffer), polarized DY | absent (only $g_2$ mentioned in Fig 21) | Ch6 `thm:dis-bjorken`, `rem:dis-crewther`; Ch10 §§4–5; App I |
| Heavy-quark schemes (CWZ, ACOT/S-ACOT/FONLL/TR; the Collins 1998 uniform theorem) and nuclear targets | absent | Ch9 `thm:disall-heavy`, `prop:disall-nuclear` |
| Photoproduction and photon structure; LUXqed; diffractive photoproduction breaking | absent (DDIS only) | Ch10 |
| Collinear SIDIS, SIA kinematics and coefficient functions, energy sum rule, $1/Q$ in $\sigma_L$ | SIA only structurally (Thm 8.1) | Ch10 |
| Inclusive $B$ decays (HQE), $B\to D\pi$ to all orders, heavy-quarkonium fragmentation at large $p_T$ | absent | Ch19 `thm:heavy-inclusive-b`, `thm:heavy-bdpi`, `prop:heavy-quarkonium-fragmentation` |
| Lattice QCD and factorization (moments, LaMET/pseudo-PDFs, renormalizability of Wilson-line bilinears, lattice CS kernel) | "lattice comparisons are evidence" (one line in App C) | Ch21; plus the frontier chapters (REQUIREMENTS 3b: Ji's LaMET proofs, Yizhuang Liu's rigorous factorization) |
| Twist-3 SSAs (ETQS), matching to TMD Sivers | absent | Ch13 `def:tmd-etqs`, `prop:tmd-twist3-matching`, Ch20 `prop:power-twist3-sidis`, `conj:power-twist3-pp` |
| 't Hooft model; OPE convergence in $\varphi^4_4$ | only cited in "supporting results" | Ch20 `prop:power-thooft-model`, `thm:power-ope-convergence` |
| KLN, Bloch–Nordsieck (QED, YFS) and its non-abelian failure, IR safety | KLN only in §4.2; DFT only in Rem E.53 | Ch3 `thm:ir-kln`, `thm:ir-bn-qed`, `prop:ir-bn-failure`, `thm:ir-safe-finite` |
| $\gamma_5$ in DR (HVBM + Larin), BRST and ghosts in cut diagrams, physical unitarity | BRST only in App C.6 | Ch2, App I, App J |
| Misconception box (28 items), master table (68 rows), reading paths | flowchart only | Ch1, Ch22 |

### 4.2 Shared topics where our plan is already more correct or more complete

1. **$P^+_{\rm NS}\neq P^-_{\rm NS}$, Carlson, $\delta'$ counterexample, $\sin(Q^2x)$ counterexample, stability of the moment problem** (App K; `rem:pdf-ns-plusminus`, `rem:dis-nonuniform`). The reference errs on the first (ERR-M10) and lacks the others.
2. **Explicit one-loop PDF with all graphs** (gluon mass, virtuals, self-energy, gauge-parameter independence) and **all four LO kernels from operator renormalization** (`prop:pdf-pqq-operator`, `prop:pdf-local-anomalous`). The reference fixes the virtual term by a sum rule (ERR-M14).
3. **DIS one-loop finite parts derived** (pole structure; $-\frac2{\epsilon^2}-\frac3\epsilon-8+\zeta_2$; $\delta$ coefficient; gluon average $1/(D-2)$; $F_L$; DIS scheme; $\mu_F$, $\mu_R$ independence) vs quoted (ERR-m12). **DY $qg$ channel and DIS-scheme cross-check** to $10^{-30}$ vs $q\bar q$ only.
4. **$e^+e^-$**: two independent $O(\alpha_s)$ routes (cut diagrams; Euclidean two-loop with $\frac{55}{12}-4\zeta_3$), the exact cutting identity at $O(g^2)$, the contour formula and $\pi^2$ terms, the general-group $r_2$, Furry. The reference has one route and quoted constants.
5. **Landau theory in two forms, with the Gordan proof, the envelope caveat, and the status of sufficiency** (`thm:ir-landau-alpha`, `thm:ir-landau-momentum`, `rem:ir-landau-status`) vs one conflated form and a false corollary (ERR-M1, M3).
6. **Method of regions status** (Euclidean [R], Minkowskian [P] with Jantzen, Pak–Smirnov, Semenova–Smirnov–Smirnov, Gardi et al.; the massive-exchange example needing analytic regulators) vs an unstated premise (ERR-M2).
7. **Wilson-line Feynman rules** with Fourier convention, orientation, $\pm i0$, $W$ vs $W^\dagger$ and cut rules (VF-WL-1, `prop:prelim-wilson-rules`) vs ambiguous Fig 4 (ERR-M4). **Grammer–Yennie with the correct $i0$ and the gluon-active-parton exception** (`lem:method-gy`, `prop:method-gy-suppression`). **Explicit tree-level non-abelian Ward identities with ghosts** (`prop:method-ward-tree`, App F).
8. **Super-leading configurations** handled (`prop:ir-power-counting` table, `thm:ir-leading-regions`) vs omitted (ERR-S4).
9. **TMD**: space-like self-energies handled correctly (`lem:tmd-soft-oneloop`) vs ERR-M27; explicit one-loop TMD/soft/hard computations, $Y\coth Y$, $S_\varepsilon$-convention constants, other rapidity schemes, transverse links, the $\int d^2k_T f\neq f$ warning.
10. **Glauber**: explicit IR-regulated kernel $\chi=-\frac{e_Ae_B}{2\pi}K_0(m_gb)$; pointwise non-cancellation (~30 %) vs exact cancellation after $\int d^2\Delta$; the four-pole table; Aybat–Sterman, LRS, BFT, RS, SYZ, DGOPS (c_glauber §§1.5–1.7). The reference regulates by windows only and misses these sources (ERR-M30, M32).
11. **Breakdown chapter**: correct CQ/C07/RM algebra (`prop:break-colour` with $P=-\mathbf T_a-2\mathbf T_b$; entanglement test; C07 anomaly); CdFR with definitions and order table; Becher et al. 2025 restoration; Gaunt vs SYZ; Zeng 2015 (`prop:break-jet-veto`). The reference errs on several of these (ERR-S2, M18, M20, M23, M30).
12. **NRQCD**: decay [A] (not "A*"), production [C], the two-step large-$p_T$ structure, NQS correctly stated (ERR-M9, M19, M22).
13. **Exclusive**: $T_H$ derivation, $\gamma^*\gamma\to\pi^0$ ($Q^2F\to\sqrt2f_\pi$), exact endpoint fractions, Isgur–Llewellyn Smith numerics, JLab comparison, GPD definitions/polynomiality/Ji sum rule, DVCS coefficient functions with $i0$, correct transverse-photon mechanism (ERR-M17).
14. **Conventions table** (WRITER_SPEC §3), notation dictionaries (Collins $g\to-g$, $S_\varepsilon$, MVV, BBL signs), VERIFIED_FORMULAS with status, and a bibliography of 646 checked entries (`refs_merged.bib`).

### 4.3 What our plan currently lacks and the reference has (summary; details §3, changes §5)

1. The non-perturbative conditional moment theorem (Thm C.50, Lemma C.64, Rem C.65, Thm C.66), and the precise split of MA0/MA3 into proven consequences vs genuine assumptions.
2. The perturbative OPE machinery (chain expansion, frozen-$q$ normal products, uniqueness, scaling of reduced coefficients, coordinate-space remainder).
3. The precise subtraction theorem: counterexamples, conditions on grouped expressions, pairing decomposition, product formula, error table, $\lambda$-dependent neighbourhoods, a complete one-loop example and the two-loop ladder.
4. The LCOPT/Glauber machinery: rigorous LCOPT, orientation of intermediate states, the cut-position identity with insertions, closed-time-path unitarity, equal-time localization, windows/carrier, two-component deformation, quantitative eikonal bounds, past-pointing lines from the contour, the single-cut-graph "future line" identity, and the operational definition of measurement compatibility.
5. The register of numbered assumptions, the error-type vocabulary and the status checklists.

---------------------------------------------------------------------------------------------------

## 5. Concrete spec changes (to FINAL_OUTLINE, WRITER_SPEC, VERIFIED_FORMULAS, FIGURES_INDEX)

**Notation.** Changes are numbered S1–S63, without parentheses; the parenthesized (S1)–(S8) always mean the proof steps of the reference's Thm E.8. Each change gives the target file and section, then the exact change. Tags follow WRITER_SPEC §4. New labels follow FINAL_OUTLINE §0.4 plus the new prefix `asm:` (S12). "本书新结果" marks results not in the literature; they need re-derivation and a script check before the chapter is accepted (S59).

**State of the spec (re-read at 15:20).** While this file was being written, the spec audit applied the corrections of §2.4 as interim caveats (FINAL_OUTLINE CHANGELOG 17; WRITER_SPEC CHANGELOG 7; VERIFIED_FORMULAS CHANGELOG 7): OUR-1 (FF normalization), OUR-2 (caveat and (CS1)–(CS3) in `thm:method-subtraction`), OUR-3 (hadronic caveat in `thm:dis-moments`), OUR-4 (two-component deformation sentence), OUR-5 (`prop:tmd-small-b`), OUR-6 (forward amplitude vs discontinuity in `thm:disall-factorization`), OUR-7 (`Shifman2000`), OUR-8 (exceptional momenta in `thm:dis-ope`). The audit left the structural proposals to the lead author (FINAL_OUTLINE §0.9 item 3). Accordingly:
- S9 is fully applied;
- S19–S22, S27, S29 and S32 **supersede** the interim caveats with the complete restructuring (new statements, App M/N/O);
- everything else below is new.

### 5.1 Structure and budgets

**S1 — New Appendix M** (FINAL_OUTLINE §0.1, §0.2, appendix list; WRITER_SPEC §1.1).
- Key `appM`, file `appM_ope.tex`, title 「重整化微扰论中的算符乘积展开：BPHZ、正规乘积、唯一性与非微扰条件定理」, **24 pp**.
- Owns the full proofs announced in Ch6 (`thm:dis-fixed-n`, `prop:dis-dispersion-np`, `thm:dis-moments-np`) and the perturbative OPE machinery.
- Contents and labels: S46.

**S2 — New Appendix N.**
- Key `appN`, `appN_subtraction.tex`, 「Collins 减除法的精确形式：条件、组合恒等式、误差表与显式例子」, **24 pp**.
- Owns the precise subtraction theorem behind `thm:method-subtraction` and the process-by-process conditions.
- Contents: S47.

**S3 — New Appendix O.**
- Key `appO`, `appO_glauber.tex`, 「光锥序微扰论与单举 Drell–Yan 中 Glauber 区相消的条件证明」, **32 pp**.
- Owns the LCOPT derivation, the cut-sum unitarity lemmas, equal-time localization, the simultaneous deformation, eikonal bounds, past-pointing Wilson lines, the main conditional theorem and the rigour checklist.
- Contents: S48.

**S4 — New Appendix P.**
- Key `appP`, `appP_blueprint.tex`, 「形式化蓝图：编号假设登记表、依赖图与状态表」, **8 pp**.
- The register table, dependency graph and status table are generated by script from `\uses{}` and the `asm:` environments.
- This is the blueprint appendix of FINAL_OUTLINE §0.9 item 2, proposed there as 「App M `appM_blueprint.tex`」 and generated by the lead author at integration time (no writer). Because the content appendices M–O are inserted before it, it becomes App P: update §0.9 item 2 and the Ch22 sentence 「a pointer to the generated App M」 accordingly.
- Required by REQUIREMENTS 3d. Labels: S49.

Page budgets for all units are in **S10**.

### 5.2 Tag system, grading reconciliation, assumption register

**S5 — Fourth `[R]` qualifier $R_{\rm cond}$** (WRITER_SPEC §4.4; FINAL_OUTLINE §0.3; Ch1 `def:intro-tags`; front matter 「阅读指南」: "the three `[R]` qualifiers" becomes four).
- Verbatim text: 「（$R_{\mathrm{cond}}$：在所列编号假设之下证明完整；结论的地位不高于其中最弱的假设。）」
- The next sentence must be 「前提：\cref{asm:…}、\cref{asm:…}（及 \cref{…}）。」
- **Use** for complete proofs whose hypotheses are numbered assumptions or tagged statements, both perturbative (Thm D.10-type) and non-perturbative (Thm C.66-type).
- **Grade-propagation rule** (print in Ch1 and App P): a process-level statement built from an $R_{\rm cond}$ implication carries the weakest grade among the assumptions it uses. For example, `thm:dy-factorization` stays [A] because `asm:appN-collins` and `asm:appO-mixing` are [A]-level.
- Tag check (WRITER_SPEC §9.7) accepts four qualifiers.
- `thm:method-template` and the process theorems keep [A] with a written-out `proofsketch` (FINAL_OUTLINE §0.8); their deduction now runs through `thm:appN-subtraction` [R, $R_{\rm cond}$] (S29).

**S6 — The assumption register** (new; Ch1 `tab:intro-assumptions`, App P `tab:appP-register`).
- Every numbered assumption of the book is an `assumption` environment with an `asm:` label (S12), owned by exactly one unit; the key in the label is the owner.
- The register `tab:appP-register` (S49) is generated from these environments; Ch1 prints the short version `tab:intro-assumptions` (S13).
- MA0–MA4 remain as umbrella names; the dictionary is at the end of §5.3.

**S7 — Error-type vocabulary** (Ch1 new `def:intro-error-types`, no tag).
- 误差类型:
  - **E-S** 标度陈述 (scaling statement);
  - **E-P** 逐点界;
  - **E-F** 纤维积分界 (bound after integrating one variable, pointwise in the rest);
  - **E-N** 积分范数界 ($\int_A|F|\le C\lambda^aL^K$ uniformly in $\varepsilon$);
  - **E-W** 弱等价 (equality of integrals over sets of a fixed algebra, with all subtraction-term weights).
- Every status table (`tab:dy-status`, `tab:appN-status`, `tab:appO-checklist`, `tab:appP-status`) has a column 「误差类型」.
- Every proof step of an [A] sketch that relies on power counting says which type it establishes.

**S8 — Grading reconciliation and naming** (Ch1 `rem:intro-grade-dictionary`, no tag; App P). Print the dictionary without citing the reference document.

| external grade (literature practice) | our representation |
|---|---|
| non-perturbative structure theorem conditional on QFT axioms + OPE ("A") | PT part: [R, R_PT] or [R, 以 OPE 为前提]; non-perturbative part: [R, $R_{\rm cond}$] listing `asm:intro-*` |
| "as rigorous as the OPE given an EFT" ("A\*") | [A] (quarkonium decay; non-perturbatively needs local duality [C]) |
| all-order argument "by the CSS standard" ("B") | [A] for the process; the implication from the register is [R, $R_{\rm cond}$] (App N); the bridge is `asm:intro-bridge` |
| "B with a delicate step" ("B′") | [A] + mandatory 「地位与缺口」 naming the `asm:appO-*` items (no extra tag) |
| conjecture *or* partial proof ("C") | split per statement: [P] (finite order / subclass) or [C] |
| proven broken ("D") | [V] + evidence type (model counterexample / explicit calculation / experiment) |

**Naming to avoid clashes with our (H1)–(H5), [A] and MA labels:**
- Collins subtraction conditions are **(CS1) accuracy**, **(CS2) suppression of non-smaller regions**, **(CS3) integrability**;
- geometric–analytic inputs are **(GA1) contour**, **(GA2) meet closure** (a definition, not an assumption), **(GA3) envelope**, **(GA4) separation**;
- the CSS/Bodwin Glauber skeleton steps are **(CSS-1)…(CSS-6)**;
- the App O proof steps are **(O-1)…(O-8)**;
- the Glauber interface clauses are **(Gla-a), (Gla-b), (Gla-c)**.

### 5.3 The assumption register (labels, owners, content, status)

**S6 continued — the register entries** (each an `assumption` environment; owner chapter/appendix in the label).

| label | owner | content | status line (地位) | refines / replaces |
|---|---|---|---|---|
| `asm:intro-wightman` | Ch1 (commentary in App M §M.8) | (W1) Wightman QCD with gauge-invariant composites, conserved hermitian $j^\mu$, parity; (W2) spectral condition $p^2\ge M^2$ in the superselection sector of the target's conserved flavour numbers, with an isolated one-particle mass for Haag–Ruelle states; massive light quarks; (W3) tempered forward matrix elements; (W4) a covariant retarded extension with $q_\mu\tilde R^{\mu\nu}=0$ (polynomial ambiguity affects finitely many low $t_n$) | open (4D QCD not constructed) | MA0 (part); corrects ERR-M25 |
| `asm:intro-composite` | Ch1 | gauge-invariant operator families graded by dimension; twist-2 = $O_q,O_g$; RG with triangular mixing; $\beta,\gamma$ asymptotic to PT; PDF light-ray operators exist between hadrons with moments $A_i^{(n)}$ | open | MA0 (part), MA4 (part) |
| `asm:intro-np-ope` | Ch1 | the OPE (direction-uniform, with derivative bounds, covariant coefficients) holds between the vacuum and hadron states; odd-twist (chiral-odd) coefficients are suppressed by a light mass | open, widely assumed; vacuum part = `conj:ee-np-ope` [C] | the old NP-OPE |
| `asm:intro-af-coeff` | Ch1 | at $\mu=\vert q\vert $ the coefficients are asymptotic to their $\overline{\rm MS}$ series | open; compatible with renormalons and instantons ($e^{-2\pi/\alpha_s}=(\Lambda/Q)^{\beta_0}$) | MA4 (part) |
| `asm:intro-growth` | Ch1 | $\lim_{y\to\infty}T_2(iy,Q^2)/(iy)=0$ | open; equivalent to the low-moment sum rules incl. the momentum sum rule (`prop:dis-low-moments`); holds at computed fixed orders | MA3 (the genuine part; analyticity is now a theorem under `asm:intro-wightman`) |
| `asm:intro-bridge` | Ch1 | region completeness and power-counting transfer to hadronic states: all $\Lambda$-sensitivity sits in the hadronic matrix elements of the same operators; remainder $O((\Lambda/Q)^p)$ as an asymptotic statement | open | MA1 + MA2 (+MA4) |
| `asm:appM-remainder` | App M | momentum-space remainder estimate for the frozen-$q$ bilocal normal product ($\vert h\vert \le K\vert q\vert ^{D-1-a}\ln^k\vert q\vert $, uniform in direction, all $\partial_p$, $p\cdot$, $m\partial_m$ images) | open as stated; **possibly dischargeable** via Anikin–Zav'yalov 1978 / Zav'yalov 1990 + uniqueness (refs agent to verify) | — |
| `asm:appM-brst-ope` | App M | (B1) BRST-symmetric renormalized insertions with classical coefficients and Ward identities; (B2) the Euclidean remainder also with $s\phi$ insertions | open as stated; partly dischargeable (Joglekar 1977 I+II; Hollands 2008 for pure YM; refs agent) | — |
| `asm:appM-forward` | App M | the OPE remainder for forward on-shell massless partonic matrix elements (exceptional momenta) | open; verified exactly in $\varepsilon$ at $O(\alpha_s)$ for $N\le8$ (c_dis `ope_check.py`) | — |
| `asm:appN-contour` | App N | (GA1) a contour $\Omega$ homotopic to real space crossing no singularity of $\Gamma$ or any $C_R\Gamma$; each $\int_\Omega C_R\Gamma$ meromorphic near $\varepsilon=0$ | open in general; holds when all poles are one-sided (`lem:method-i0-compat`) | — |
| `asm:appN-envelope` | App N | (GA3) power-counting envelopes $\Phi_{R_0}$ on $U_{R_0}$ with $\int\Phi_{R_0}\le CL^K$ dominating every partially approximated integrand; uniform integrability at $\Vert k\Vert \ge1$; pointwise boost bound for projections | open (never written in integral form at all orders) | — |
| `asm:appN-separation` | App N | (GA4) Łojasiewicz-type virtuality bound on $H_R$ lines ($\ge ct_R^2$); $\vert l^+\vert \ge ct_R$ on changed jet lines (endpoint assignments in $\mathcal R$); for soft momenta $\vert k^+k^-\vert \ge c\mathbf k_T^2$ and $\vert \tilde D\vert \ge c(\vert p^+\vert \vert k^-\vert +v_A(p))$ | open in general; verified in the one-loop triangle | — |
| `asm:appN-collins` | App N | (CS1)–(CS3) hold for every integrand (graph or common-routing family) of the process, including multi-direction processes and non-adapted routing | [A]-level: Collins 2011 ch. 10 asserts it (complete for the Sudakov form factor at the level of rigour of that chapter). For the one-loop off-shell triangle the identities, the values and the exact remainder are known (`prop:appN-triangle-exact`), but uniform integral bounds on a deformed four-dimensional contour have not been written even there (R6) | the old "subtraction gap" |
| `asm:appN-values` | App N | a linear rule assigning values to divergent chain terms, compatible with the absolutely convergent subtraction terms; scaleless = 0 | convention; verified in the one-loop triangle | — |
| `asm:appN-cutsum` | App N | cut-summed representation (LCPT common domain and integrand; approximators act on it; event-shape density condition) | open in general; **(X1) provided by App O** for DY-type graphs (`lem:appO-lcopt`, `lem:appO-hard-locality`) under `asm:appO-lcopt` | — |
| `asm:appN-ward-product` | App N | Ward identities apply to integrands already modified by other approximators and give the product structure hard ⊗ collinear ⊗ soft; regrouping of subtractions by order | [A] (= content of `lem:method-ward-multi` + combinatorics); abelian and $n\le2$ tree-level [R] | — |
| `asm:appN-uv` | App N | UV renormalization compatible with the approximators: DR+$\overline{\rm MS}$ at integrand level via $R^*$, or BPHZ(L) **plus the finite non-invariant counterterms restoring the Slavnov–Taylor identities**; $T_R$ commutes with the subtractions up to finite local terms | partly proven (linear substitutions; Euclidean points); corrects ERR-M28 | — |
| `asm:appN-multren` | App N | (Z1) moment-space multiplicative renormalization of collinear factors (theorem for local twist-2 operators on shell; independent input for FFs); (Z2) an IR regulator for partonic targets preserving the Ward identities; (Z3) DR-IR on-shell targets give the same $\hat{\mathsf H}^{\rm bare}$ | (Z1) partly theorem; (Z2) genuine input (no on-shell gluon regulator known); (Z3) assumption | — |
| `asm:appN-tmd` | App N | (T1) $k_T$ tails; (T2) asymptotic linearity of $\ln\tilde S$ and $\ln\tilde f^{\rm unsub}$ with equal slope; (T3) $b$-space multiplicative renormalization; (T4) $y_B\to-\infty$ under the integral | one loop verified (c_tmd: $Y\coth Y$, equal slopes, $\sigma$ cancels); all orders [A] | — |
| `asm:appN-endpoint` | App N | (E1)–(E3): endpoint integrability of meson-jet subgraphs; hard kernel at most $1/x$; endpoint region suppressed | true for finite Gegenbauer truncations; assumption for non-perturbative DAs | — |
| `asm:appO-lcopt` | App O | (i) no zero modes or endpoint contributions at $l^+=0$ at leading power; truncation of minus components can be dropped; (ii) instantaneous-loop values exist reproducing the covariant minus integrals | open; [P] in the light-front literature | E.18(i)(ii); (iii) proven in App J (S53) |
| `asm:appO-envelope` | App O | integrable envelope for all fibre-integration errors of the equal-time rewriting, uniform in $\varepsilon$ and in the $i0$ regulator | open | — |
| `asm:appO-mixing` | App O | (a) external factors of localizable endpoints split into half-plane-analytic parts with Lemma-E.28-type bounds (general soft subgraphs); (b) cut compatibility of the soft subgraph; (c) for coincident connections, the complete graph set at the given order (with adjacent near-shell soft regions and real emission) gives $\mathcal W'^\dagger\mathcal W=1+O(\lambda^a)$ weakly | (a)(b) automatic for $\mathcal G_0$; (c) **holds for the two-gluon exchange graphs of eikonal spectators at $O(g^4)$** (`prop:dy-eikonal-twogluon`); open beyond (non-eikonal spectators, higher orders, coincident SA/AS insertions) | E.33 with (c1) replaced by `lem:appO-joint-localization` |
| `asm:appO-deformation` | App O | (a) deformation targets for general configurations (Glauber flows; localized legs; single-leg-type components); (b) compatibility of the deformation with the region set algebra; (c) (CS1)(CS2) on the soft-angle region and for the window-edge terms; (d) H-emission endpoints **and coincident SA/AS insertions** (non-analytic ordering weights) | (a) proved for $\mathcal G_0$ and graded configurations (`prop:appO-target`); (b)(c)(d) open, **needed even for abelian $\mathcal G_0$** | E.44 + ERR-S3 consequence |
| `asm:appO-rewritten-cs` | App O | (CS1)(CS2) for rewritten and family-summed forms, incl. matching of localized spectator terms with the external-endpoint distributions at $n\cdot K_i=0$ (Wilson-line prescription) and the allocation of SA/AS endpoints between regions | open; Glauber-specific (ERR-M29); harmless for collinear PDFs (direction irrelevant), substantive for TMD | split off from D.14 |

Total: **25 assumptions** (6 global, 3 OPE, 11 subtraction, 5 Glauber). `def:intro-MA` keeps MA0–MA4 as umbrella names with this dictionary:
- MA0 ⊃ `asm:intro-wightman`, `asm:intro-composite`;
- MA1 + MA2 = `asm:intro-bridge`;
- MA3 = analyticity (now `prop:dis-dispersion-np` under MA0) + `asm:intro-growth`;
- MA4 ⊃ `asm:intro-af-coeff`.

### 5.4 Binding conventions

**S9 — Fragmentation-function normalization (binding fix).** **[Applied by the spec audit, 15:09–15:10:** WRITER_SPEC row 20 (CHANGELOG 7), VF-CONV-17 (status A, CHANGELOG 7), `def:pdf-ff` with the printed $O(\alpha_s)$ check (FINAL_OUTLINE CHANGELOG 17). Remaining action: none, except the BLUEPRINT §0.4(8) note, which is superseded and need not be edited.**]** The applied form, for reference:
$$d_{h/q}(z)=\frac{z^{1-2\varepsilon}}{4N_c}\sum_X\int\frac{dw^-}{2\pi}e^{ik^+w^-}{\rm Tr}_c{\rm Tr}_D\Big[\gamma^+\langle0|W[\infty n_B,w]\psi(w)|hX\rangle\langle hX|\bar\psi(0)W[0,\infty n_B]|0\rangle\Big],\quad w=(0^+,w^-,\mathbf 0_T),\ k^+=p_h^+/z,$$
- Frame: the **hadron frame** $\mathbf p_{h,T}=0$; future-pointing lines.
- Equivalent **parton-frame** form: prefactor $\frac1{4N_cz}$ together with an explicit $\int d^{2-2\varepsilon}\mathbf p_{h,T}$ (since $d^{2-2\varepsilon}p_{hT}=z^{2-2\varepsilon}d^{2-2\varepsilon}k_T$).
- The $O(\alpha_s)$ check, printed inside `def:pdf-ff` (no separate example label): at $O(\alpha_s)$ in $A^+=0$ gauge with $h=q$, $X=g$, $d^{(1)}_{q/q}=\frac{\alpha_s}{2\pi}C_F\frac{1+z^2}{1-z}\int\frac{dl_T^2}{l_T^2}$. The prefactor $\frac1{4N_cz}$ in the hadron frame would give $z^{-2}$ times this. The free-quark check cannot distinguish the two.
- VF-CONV-17 status **A** (R1 `check_ff_norm.py`, rerun by the synthesizer; frame-change Jacobian re-derived by the audit).

**S10 — Page budgets** (FINAL_OUTLINE §0.2; WRITER_SPEC §10).

| unit | old | new |
|---|---|---|
| Ch1 | 12 | 13 |
| Ch3 | 14 | 15 |
| Ch6 | 14 | 17 |
| Ch8 | 16 | 19 |
| Ch9 | 12 | 13 |
| Ch11 | 14 | 17 |
| Ch13 | 14 | 15 |
| Ch22 | 12 | 14 |
| App D | 4 | 6 |
| App E | 3 | 5 |
| App F | 3 | 5 |
| App J | 2 | 4 |
| App K | 3 | 4 |
| App M | — | 24 |
| App N | — | 24 |
| App O | — | 32 |
| App P | — | 8 |

- Totals: chapters 260 → 275; appendices 35 → 132; body ≈ 412 pp.
- Tolerance unchanged (−15 %/+10 %).
- If the lead author must cap the size, cut first the optional figures and App O §O.11 (neighbouring problems, which duplicate Ch17). Never cut statements or status lines.

**S11 — New convention row** (WRITER_SPEC §3, row 38). Glauber direction:
- $e_G\equiv n_B-n_A$, $(e_G^+,e_G^-,\mathbf e_{G,T})=(-1,+1,\mathbf 0)$, $e_G^2=-2$, $n_A\cdot e_G=+1$, $n_B\cdot e_G=-1$;
- $(l+it\sigma fe_G)^2-m^2=(l^2-m^2+2t^2f^2)+2it\sigma f(l^+-l^-)$ (VF-REF-7).
- Also state: an amplitude-side ($\sigma=+1$) soft momentum flowing into $J_A$ is deformed with ${\rm Im}\,k^->0$, ${\rm Im}\,k^+<0$.

**S12 — Label prefix and environment for assumptions** (WRITER_SPEC §4.1, §5.1, §9.6; `check_outline.py`).
- Add `asm:<key>-<name>` to the statement label scheme; the environment `assumption` already exists in `preamble_fact.tex` (`\crefname{assumption}{假设}`).
- Body fields, in order: statement; 「地位：」; 「文献：」; 「被使用于：」 (filled from the registry); 「解除途径：」.
- Add `asm` to the regex of the label-check script, i.e. `(def|thm|lem|prop|cor|conj|rem|ex|asm|sec|fig|tab)`, and to the outline registry generator.

### 5.5 Chapter-by-chapter changes (new canonical statements with labels and tags)

**S13 — Ch1** (`ch:intro`, +1 p).
1. Update `def:intro-tags` (fourth qualifier, grade-propagation rule).
2. New `def:intro-error-types` (S7).
3. New `rem:intro-grade-dictionary` (S8).
4. Update `def:intro-MA` with the register dictionary (S6/§5.3).
5. New assumption environments `asm:intro-wightman`, `asm:intro-composite`, `asm:intro-np-ope`, `asm:intro-af-coeff`, `asm:intro-growth`, `asm:intro-bridge` (complete statements in Ch1, 4–8 lines each; App M §M.8 adds the technical commentary — which axiom is used where — and never a second statement).
6. New table `tab:intro-assumptions` (25 rows: label, one-line content, status, used by).
7. `sec:intro-proof`: add the sharpness remark — per-order exponents of the general method can be far from the true power, while explicit examples give the true power (F3).

**S14 — Ch2** (`ch:prelim`).
1. `thm:prelim-cutting-rules`: add a forward pointer to the light-cone largest-time identity with insertions (`lem:appO-cut-position`).
2. `thm:prelim-composite-renorm`: add the forward on-shell caveat (Hamberg–van Neerven 1992 / `Collins:1994ee`) and cite Joglekar 1977 I+II and Hollands 2008. Keys (checked by the synthesizer in `refs_merged.bib`): `Joglekar:1976eb` (Ann. Phys. 108, 1977), `Joglekar:1976pe` (Ann. Phys. 109, 1977), `Joglekar:1975nu`, `Hollands:2007zg` (Rev. Math. Phys. 20, 2008). Hamberg–van Neerven 1992 is not in the bibliography (S60).
3. New `rem:prelim-bphz-brst` (no tag): BPHZ(L) Taylor subtractions break the Slavnov–Taylor identities, and equivalence with DR+$\overline{\rm MS}$ needs finite non-invariant counterterms (`Breitenlohner:1975hg`, `Breitenlohner:1976te`). Graphical Ward identities are therefore used with DR graphs (ERR-M28).
4. `thm:prelim-composite-renorm` or the BPHZ remark: degrees of the subtraction must be vertex-additive; a counterexample shows that $\delta\ge\omega$ alone is not enough (reference Rem C.9, re-derived; details in App M §M.2).

**S15 — Ch3** (`ch:ir`, +1 p).
1. New `rem:ir-euclid-corners` (no tag; misconception **M29**). In Euclidean non-exceptional kinematics, zero-momentum massless lines always solve the Landau equations (e.g. the simplex corners of the off-shell triangle); finiteness follows from IR power counting (`thm:ee-euclid-ir`). "No Landau solution in the Euclidean region" is false.
2. New `prop:ir-super-leading` [A]. With $\lambda$ units and a target jet ($c_J=2$): $(n_F,n_T)=(0,0)$ gives $p_J=-2$ and $(0,1)$ gives $p_J=-1$. In gauge-invariant sums these cancel (Ward identity + colour neutrality; `CollinsSoperSterman1989` §8.6). Their $O(\lambda)$, $O(\lambda^2)$ remainders are leading and combine into $G^{+j}$ via $k^+A^j-k^jA^+$. Proof: sketch; cross-reference `prop:method-gy-suppression`.
3. New `tab:ir-connection-powers`: power of $\lambda$ per connection — good quark +1, bad quark +2, transverse gluon +1, scalar (K) gluon 0, "−" gluon +2; soft gluon→jet 0, soft quark→jet +1, soft gluon→$H$ +2, soft quark→$H$ +3; super-leading rows. State the unit: powers of $\lambda$, $k_T\sim\lambda Q$.
4. New figure `fig:ir-mode-exponents` (S56).
5. New `rem:ir-scaling-vs-bound` (no tag): `prop:ir-power-counting` and `thm:ir-leading-regions` are scaling statements (E-S); their integral version is `asm:appN-envelope`, `asm:appN-separation`.
6. New `rem:ir-regions-values` (no tag): values of divergent region integrals depend on the representation (e.g. the zero-bin $\int_0^\infty d\sigma/\sigma^{1+\varepsilon}$ vs a parametric $\int_0^1$); Collins subtraction terms are absolutely convergent iterated integrals. Link `asm:appN-values`, `prop:ir-regions-minkowski`.
7. `prop:ir-coleman-norton`: add the scaling-limit treatment of soft lines (the reference's Rem 3.3). In Ch11 `sec:dy-regions`, use `fig:glauber-exchange` to show initial- and final-state soft gluons with the active and spectator poles on opposite sides.

**S16 — Ch4** (`ch:sudakov`).
1. New `rem:sudakov-consistency` (no tag): single-scale structure + $\mu$-independence + pole cancellation fix the $1/\varepsilon^2$ coefficients $(1,-1,-1,1)$ and the double log $\frac12[a^2-2b^2+(2b-a)^2]=(a-b)^2$, with $a=\ln\frac{\mu^2}{Q^2}$, $b=\ln\frac{\mu^2}{m^2}$.
2. In `ex:sudakov-offshell`: quote the exact result $Q^2I=\Phi^{(1)}(t,t)=[4{\rm Li}_2(-\rho t)+\ln^2(\rho t)+\frac{\pi^2}3]/\sqrt{1-4t}$, $\rho=\frac2{1-2t+\sqrt{1-4t}}$, with expansion $L^2+\frac{\pi^2}3+t(2L^2-4L-4+\frac{2\pi^2}3)+t^2(6L^2-14L-11+2\pi^2)+O(t^3L^2)$, $L=\ln\frac{Q^2}{m^2}$, $t=\frac{m^2}{Q^2}$ (VF-REF-2).
3. Forward reference to `ex:method-sudakov-subtraction` and `prop:appN-triangle-exact`.
4. Pointer only (first-use ownership, FIGURES_INDEX CHANGELOG 1): `fig:method-hasse` (Ch8) shows the nine two-loop regions.

**S17 — Ch5** (`ch:ee`).
1. `prop:ee-analytic`: add the exact condition — one subtraction suffices iff $\int^\infty ds\,{\rm Im}\,\Pi(s)/s^2<\infty$ ⟺ the Adler function is finite at one Euclidean point (proof: $\rho\ge0$ and $(s+Q^2)^{-2}\ge(2s)^{-2}$ for $s\ge Q^2$); the subtraction point is Euclidean because $\Pi(0)$ is IR divergent for massless quarks.
2. New `rem:ee-status-layout` (no tag): the four logically separate levels (axiomatic analyticity / PT / OPE-conditional / smearing identity vs its computability).
3. New `rem:ee-complex-ope` (no tag): App M's OPE assumptions are Euclidean; using the OPE at complex $q^2$ (smearing at $s+i\Delta$) is an extra assumption (feeds `conj:ee-duality`).
4. New figure `fig:ee-cutsum-disc` (S56).
5. `thm:ee-ope` / `conj:ee-np-ope`: the vacuum OPE of the Adler function has no $1/Q^2$ term (no gauge-invariant dimension-2 operator); condensate terms are conditional on `asm:intro-np-ope` (reference Rem C.62).

**S18 — Ch6 overview** (`ch:dis`, +3 pp). The chapter now has two proof routes: (I) partonic PT (forward amplitude); (II) hadronic, non-perturbative conditional. Print a flow chart: `prop:dis-compton-analytic` (PT) / `prop:dis-dispersion-np` (hadrons) → `lem:dis-euclid-segment` → `lem:dis-ope-segment` → `thm:dis-fixed-n` → `thm:dis-moments` / `thm:dis-moments-np`. Misconception **M34** (S57).

**S19 — Ch6: split `thm:dis-ope`** (keep the label `thm:dis-ope` [A] as umbrella).
- New `prop:dis-ope-euclid` — 欧氏非例外动量下 Green 函数的逐图渐近展开 [A]. At each order, for Euclidean non-exceptional $(p,q)$, the T-product Green function admits $\tilde G^T-\sum_{d_O\le a}\tilde C_O(q;\mu)\tilde G_{[O]}=O(|q|^{D-1-a}\ln^k|q|)$ in a basis including gauge-variant and ghost operators. The coefficients are $|q|^{D-d_O}\times$ polynomials in $\ln(q^2/\mu^2)$, and are **unique** (log-polynomial argument).
  - Cite the graph-by-graph DR asymptotic-expansion theorems and BPHZL convergence (refs agent to fix keys and scope: Smirnov 1990/1991/2002; Chetyrkin–Gorishny–Tkachov; Lowenstein–Zimmermann).
  - **Tag [A]** under the binding decision D3: FINAL_OUTLINE §0.9 item 4 did not adopt the grade "[R] in PT as a combination of classical results" of `frontier/others` §2.7, and Ch22 open problem 4 is the OPE for QCD with quarks. Upgrade path: [R, R_PT] if the refs agent confirms that the cited theorems jointly cover QCD with quarks, ghosts and gauge-variant operators; then Ch22 open problem 4 must be reworded as well.
- New `prop:dis-ope-gi` — 物理矩阵元只需规范不变算符 [A]. For $j^\mu j^\nu$ between physical states only gauge-invariant operators contribute at twist 2 ($O_q,O_g$). Implication: [R, $R_{\rm cond}$] under `asm:appM-brst-ope` (Prop C.44 route). Literature: Joglekar 1977 (QCD currents), Hollands 2008 (pure YM), `thm:prelim-composite-renorm`.
- New `prop:dis-ope-forward` — 前向在壳部分子矩阵元 [A]. For on-shell massless partons in DR, at fixed order: $T_2^{(j)}=4\sum_{n\,{\rm even}}\omega^{n-1}\sum_iC^{(n)}_{2,i}A^{(n)}_{i/j}$ uniformly on $|\omega|\le r<1$. Implication [R, $R_{\rm cond}$] under `asm:appM-forward` (scaleless matrix elements force twist 2; Taylor-coefficient contradiction argument). Check: exact in $\varepsilon$ at $O(\alpha_s)$, $N\le8$ (c_dis). Remark: amplitude form $\sum_q\int_{-1}^1\hat H_q(\xi\omega)f_q+\int_0^1\hat H_gf_g$ (no $d\xi/\xi$; odd extension; gluon factor 2).
- `thm:dis-ope` text: "the three statements above"; its [A] tag refers to all three sub-statements (the first one by D3).

**S20 — Ch6: fixed-$n$ moments from the local OPE.**
- New `lem:dis-euclid-segment` — 欧氏点在 $\omega$ 平面上的位置 [R, R_def]. In the rest frame, Euclidean $q=(iq^4,\mathbf q)$ with $|\mathbf q|\ge Q/2$ gives $\omega=2iMq^4/Q^2\in\mathcal I_Q\equiv\{iy:|y|\le\sqrt3M/Q\}$, and every point of $\mathcal I_Q$ is attained. Proof: full.
- New `lem:dis-ope-segment` — OPE 在线段上的多项式逼近 [R, $R_{\rm cond}$: `asm:intro-np-ope`]. If (O1) holds to level $N$ with covariant coefficients $|\tilde C_j|\le K|q|^{2-d_j}\ln^k$, twist $\ge2$, chiral suppression for odd twist, and twist-2 only from $O_q,O_g$, then there is an odd polynomial $\mathcal P_N(\omega)=\sum_{n\le N-2}\pi_n\omega^{n-1}$ with $\sup_{\mathcal I_Q}|T_2-\mathcal P_N|\le K_N(M/Q)^{N-2}\ln^kQ$ and $\pi_n=4\sum_iC^{(n)}_{2,i}A^{(n)}_i+O(\frac{M^2+mM}{Q^2}\ln^kQ)$. Proof: full in App M (projector $T_2=\frac{3\nu}{2(\hat P^2)^2}[\hat P_\mu\hat P_\nu-\frac{\hat P^2}3g_{\mu\nu}]T^{\mu\nu}$; `lem:appK-markov`).
- New `thm:dis-fixed-n` — 由定域 OPE 得到固定 $n$ 的 Taylor 系数 [R, $R_{\rm cond}$].
  - Assume `lem:dis-ope-segment` for every even $N$; $T_2$ analytic and odd in $|\omega|<1$; $F_2\,dx\ge0$ (incl. the elastic point); a $Q$-independent even $n_0$ with $t_n=4\int x^{n-2}F_2$ for even $n\ge n_0$.
  - Then for **every** even $n\ge2$: $t_n(Q^2)=4\sum_iC^{(n)}_{2,i}A^{(n)}_i+O(\frac{M^2+mM}{Q^2}\ln^kQ)$.
  - No sum over spins and no interchange of limits is used.
  - Proof: full in App M (positivity tail; Markov; bootstrap of $t_{n_0}$).
  - Status: positivity makes it inherently non-perturbative; the PT analogue is `prop:dis-ope-forward`.

**S21 — Ch6: dispersion relation and low moments.**
- New `prop:dis-dispersion-np` — 由 Wightman 公理得到的有限减除色散关系 [R, $R_{\rm cond}$: `asm:intro-wightman`].
  - (a) $T_2$ is analytic in $\mathbb C\setminus((-\infty,-1]\cup[1,\infty))$, odd, real-analytic.
  - (b) $|T_2(\omega)|\le C_Q(1+|\omega|)^A|{\rm Im}\,\omega|^{-B}$ with $A,B$ independent of $Q$.
  - (c) ${\rm Disc}\,T_2=4\pi iF_2(1/\omega)d\omega\ge0$.
  - (d) For every even $n_0>A+2$: $T_2(\omega)=\sum_{n<n_0}t_n\omega^{n-1}+4\omega^{n_0-1}\int_0^1dx\,\frac{x^{n_0-2}F_2(x)}{1-x^2\omega^2}$.
  - Proof: full in App M §M.8 (forward tube, Vladimirov bound, edge of the wedge with $Q^2$-smearing, positivity, almost-analytic extension + Green's formula, `lem:appK-entire`).
  - Replaces the hadronic part of `prop:dis-compton-analytic` and the phrase "drop the circle at infinity under MA3" in `prop:dis-dispersion`.
- New `prop:dis-low-moments` — 低阶矩与增长条件的等价 [R, R_def].
  - If (d) holds for some $n_0\ge4$, then $t_n=4\int_0^1x^{n-2}F_2$ for all even $2\le n<n_0$ **iff** $\lim_{y\to\infty}T_2(iy)/(iy)=0$, i.e. $\int F_2<\infty$ and no real "fixed-pole" term $c\,\omega$.
  - Regge behaviour of $F_2$ is neither necessary nor sufficient.
  - Hence the momentum sum rule needs `asm:intro-growth`.
  - Proof: full (descending induction).
- `prop:dis-dispersion` stays [R, R_PT] for partonic targets (α-representation), with the remark "for hadrons see `prop:dis-dispersion-np`".

**S22 — Ch6: non-perturbative moment theorem; revised `thm:dis-moments`; twist lemmas.**
- New `thm:dis-moments-np` — DIS 矩因子化的非微扰条件定理 [R, $R_{\rm cond}$: `asm:intro-wightman`, `asm:intro-composite`, `asm:intro-np-ope`, `asm:intro-af-coeff`].
  - (i) The coefficients defined at $\mu$ by the exact operator RG from $\mu_0$ satisfy (O1) at every $\mu$ and the RG equation. $C^{(n)}_{2,i}(\frac{Q^2}{\mu^2},\alpha_s(\mu))=\sum_jC^{(n)}_{2,j}(1,\alpha_s(Q))[\mathcal P\exp(-\int_\mu^Q\frac{d\mu'}{\mu'}\gamma^{(n)})]_{ji}$, with $C(1,\alpha_s(Q))$ asymptotic to the $\overline{\rm MS}$ series.
  - (ii) For even $n\ge n_0$: $\int_0^1x^{n-2}F_2=\sum_iC^{(n)}_{2,i}A^{(n)}_i+O(\frac{\Lambda_h^2}{Q^2}\ln^kQ)$; with `asm:intro-growth`, for all even $n\ge2$.
  - (iii) Under (Φ), `cor:dis-weak-xspace`.
  - Proof: full in App M (norm bound on $U^{\pm1}$ from asymptotic freedom with mass-mixing rescaling; verification of the hypotheses of `thm:dis-fixed-n`).
- New `cor:dis-weak-xspace` — $x$ 空间的弱收敛 [R, $R_{\rm cond}$]. If finite signed measures $\Phi_Q$ have the twist-2 moments, then $\int x^{n_0-2}\phi\,d(F_2dx-\Phi_Q)=O(\frac{M^2+mM}{Q^2}\ln^k)$ for polynomials $\phi$ in $x^2$, and $\to0$ for all continuous $\phi$ under uniform mass bounds. A pointwise $O(1/Q^2)$ is impossible. Existence of $\Phi_Q$ is a Hausdorff problem.
- **Revise `thm:dis-moments`** (tag unchanged [R, 以 OPE 为前提]).
  - Statement: "for even $n\ge n_0$; all even $n\ge2$ under `asm:intro-growth`".
  - MA line replaced by the asm list.
  - Proof plan: partonic part from `prop:dis-ope-forward`; hadronic part from `thm:dis-fixed-n` + `prop:dis-dispersion-np` + `thm:dis-moments-np`.
  - Remove "insert, contract, compare" as the hadronic proof.
- New `lem:dis-twist-classification` — 扭度 2 规范不变算符的分类 [R, R_def]. Collinear twist $t=d-h$ table ($\psi_+,\bar\psi_+$: 1; $\psi_-$: 2; $D^+$: 0; $D^j$: 1; $D^-$: 2; $F^{+j}$: 1; $F^{+-},F^{ij}$: 2; $F^{-j}$: 3). Twist-2 symmetric traceless gauge-invariant operators with non-zero spin-averaged forward matrix elements are spanned (mod total derivatives and EOM) by $O_q^{(n)}$ per flavour and $O_g^{(n)}$ ($n$ even). Proof: full.
- New `lem:dis-twist-chirality` — 扭度奇偶性与手征 [R, R_def]. For bosonic ghost-free polynomials in the symmetric traceless rank-$j$ representation, $(-1)^{d-j}=\chi$. Caveat (print): false for mixed symmetry (transversity is twist 2 and chiral odd).
- New `prop:dis-chiral-suppression` — 奇扭度系数的手征压低 [R, R_PT]. In massless PT every chiral-odd coefficient vanishes at every order ($\gamma$-parity of open quark lines; DR-safe, no $\gamma_5$). Non-perturbatively it is part of `asm:intro-np-ope` (χSB, $U(1)_A$, instantons $e^{-2\pi/\alpha_s}$).
- `prop:dis-ope-rg`: proof route "derived from the exact uniqueness of `prop:dis-ope-euclid`" (Prop C.46).
- New figure `fig:dis-euclid-segment` (S56).

**S23 — Ch7** (`ch:pdf`).
1. `def:pdf-ff`: [applied] (S9).
2. New `rem:pdf-ff-multren` (no tag): moments of FFs are not local-operator matrix elements, so the multiplicative renormalizability of FFs is an independent input (`asm:appN-multren`(Z1)); timelike DGLAP `prop:pdf-timelike-dglap` is [R, R_PT] graph by graph, but the all-order operator statement is [A].
3. `prop:pdf-support-hadron`: add the antiquark part (anticommutator at light-like separation; divergent disconnected constant removed) and new `rem:pdf-support-jaffe` (the $k^-$-pole argument as a second proof).
4. New `rem:pdf-gauge-residual` (no tag): residual gauge freedom of $A^+=0$ and the $1/k^+$ prescription as boundary conditions. The finite light-like segment is prescription independent; TMD staples are not. $U(+\infty)$ is a field-dependent operator, not a global gauge transformation.
5. `def:pdf-gluon`: remark that the gluon density arises from $k^+A^j-k^jA^+$ (the G term of `prop:method-gy-suppression`), and that the light-cone-gauge pitfalls correspond to the choice of Wilson-line direction.

**S24 — Ch8: regions, neighbourhoods, power suppression** (`ch:method`, part of +3 pp).
- New `def:method-power-suppressed` — 积分范数意义下的幂次压低. $F\in\mathfrak S(A)$ iff $\int_A|F|d\mu\le C\lambda^aL^K$ uniformly in $\lambda\in(0,\lambda_0]$, $\varepsilon\in(0,\varepsilon_0]$. Reasons: measurement thin layers; non-pointwise $\overline{\rm MS}$ cancellations. $\Gamma$ is a single integrand with UV subdivergences removed at integrand level.
- Revise `def:method-regions`: regions are **per-line mode assignments** ($S<A,B<H$; $A\wedge B=S$); pinch sets $\pi_R$ are affine subspaces; per-line order and meet. New `lem:method-meets` (数学): $\pi_{R\wedge R'}=\pi_R\cap\pi_{R'}$; if $\pi_R\cap\pi_{R'}=\emptyset$ there is no common lower bound.
- New `def:method-neighbourhoods` — $\lambda$ 依赖的邻域. $N_R=\{\sigma_{R(j)}(l_j)\le\lambda^{\beta_R}\ \forall R(j)\ne H\}$ with $\sigma_A=|l^-|+|l_T|$, $\sigma_B=|l^+|+|l_T|$, $\sigma_S=\|l\|$; $U_R=N_R\setminus\cup_{R'<R}N_{R'}$; $\beta_R=3^{h(R)-h_*}$. New `lem:method-covering` (数学): $\cup_RU_R=\Omega$.
- New figure `fig:method-neighbourhoods` (S56).

**S25 — Ch8: why naive induction fails; Collins conditions.**
- New `ex:method-naive-induction` [R, R_PT], off-shell one-loop triangle, $p_1=(P,-\frac{m^2}{2P},0)$, $p_2=(\frac{m^2}{2P'},-P',0)$:
  - (a) $T_{C_2}\Gamma=\frac1{D_gh_1D_2}$ has an unregulated collinear pinch in $C_1$, while $C_{C_2}\Gamma=T_{C_2}(\Gamma-T_S\Gamma)=\frac{m^2}{2PP'}\frac1{D_gD_2e_2}-\frac1{h_1D_2e_2}$ is suppressed;
  - (b) $C_S\Gamma$ is leading in $C_1$, so $T_{C_1}$ must be accurate on $T_S\Gamma$: $(1-T_{C_1})T_S\Gamma=\frac1{D_ge_1}(\frac1{e_2}-\frac1{h_2})$;
  - (c) $T_{C_1}\Gamma$ is not absolutely integrable for any $\varepsilon$ (rapidity end needs $\varepsilon<0$, UV end needs $\varepsilon>0$).
  - Misconception **M35** (S57).
- New `def:method-collins-conditions` — 减除条件 (CS1)–(CS3). With $X_{R_0}=\Gamma-\sum_{R<R_0}C_R\Gamma$:
  - (CS1)$_{R_0}$: $(1-T_{R_0})X_{R_0}\in\mathfrak S(U_{R_0})$;
  - (CS2)$_{R_0}$: $C_R\Gamma\in\mathfrak S(U_{R_0})$ for all $R\not\le R_0$;
  - (CS3): $\Gamma$ and all $C_R\Gamma$ are in $L^1(\Omega)$, uniformly in $\varepsilon$ for $\Gamma$.

**S26 — Ch8: explicit approximators, $i0$, error table.**
- Revise `def:method-collinear-approx` and `def:method-soft-approx` to the **idempotent-projector form**:
  - $k\to\pi_+(k)=(n_B\cdot k)n_A$ in $H$; $\mathcal P_+=\frac12\gamma^-\gamma^+$ (out-flowing $\mathcal P_-$);
  - gluon projector $\mathcal P_A{}^\mu{}_\nu=g_T{}^\mu{}_\nu+n_A^\mu n_{B\nu}$, so that $H_\mu J^\mu\to H^-J^+-\mathbf H_T\cdot\mathbf J_T$;
  - soft $k\to\pi_-(k)=(n_A\cdot k)n_B$ inside $J_A$, projection $n_A^\mu n_{B\nu}$;
  - **no new denominators**: the soft-approximated $\tilde D=p^2-M^2+2p^+k^-+i0$ inherits its $i0$, and the Wilson-line $1/(k^-\pm i0)$ arise only after the Ward identity.
  - Keep the existing explicit $i0$ forms (future for DIS, past for DY) as consequences.
- New `lem:method-i0-compat` — 软近似分母的 $i0$ 相容性与变形幅度 [R, R_PT]. If a soft momentum flows through $J_A$ lines $l=p+k$ with common sign $\eta$ of $p^+$, then under $k^-\to k^-+i\eta\kappa$: ${\rm Im}D=2\eta\kappa(p^++k^+)\ge0$ and ${\rm Im}\tilde D=2\eta\kappa p^+\ge0$. The soft line's own propagator limits the amplitude to $\kappa\sim k_T^2/|k^+|$, giving only $|k^+k^-|\gtrsim k_T^2$. Opposite orientations give a Glauber pinch. Proof: full.
- New `tab:method-errors` (full page): Table 4 rows 1–9 in our notation, with columns approximation / deleted / kept / size on $U_R$ / bound type (relative E-P, envelope, E-N) / input used.
- New `lem:method-telescoping` (数学): $(1-T)\prod f_i=\sum_i[\prod_{j<i}Tf_j](f_i-Tf_i)[\prod_{j>i}f_j]$.
- New `lem:method-local-accuracy` [R, $R_{\rm cond}$: `asm:appN-envelope`, `asm:appN-separation`]: $(1-T_{R_0})\Gamma\in\mathfrak S(U_{R_0})$; hence (CS1) holds for minimal $R_0$. Remark: term-by-term stability of chain terms is false (Ex D.47, D.48 types).
- New `rem:method-abs-failure` (no tag): (Abs) fails exactly by the transverse coupling of a direction-flipping line (leading for a physical gluon connection), plus the soft-line-convention edge case. Hence the general product formula is part of `asm:appN-collins`.

**S27 — Ch9: from the unphysical forward amplitude to moments and to $x$ space** (`ch:disall`, part of +1 p).
- New `prop:disall-two-routes` — 从非物理区前向振幅到矩与 $x$ 空间的两条途径 [R, $R_{\rm cond}$].
  - (a) For $|\omega|<1$ the leading regions of $T^{\mu\nu}$ contain only target-collinear and hard modes.
  - (b) If the subtraction bounds hold uniformly on the complex disc $|\omega|\le\rho<1$, then every moment of $W^{\mu\nu}$ factorizes with remainder $O(\rho^{-N}\lambda^aL^K)$ (Cauchy estimate).
  - (c) Real-segment bounds alone do **not** control the discontinuity. The $x$-space statement at fixed $x<1$ requires the cut-graph analysis under `asm:appN-cutsum`. Uniformity fails as $x\to1$ (threshold region).
  - Proof: full for (b) and the counter-remark.
- Revise `lem:disall-fsi` / `thm:disall-factorization` proofs accordingly.

**S28 — Ch9: factorized subtraction terms, renormalization, the two-loop ladder.**
- New `prop:disall-factorized-subtraction` [R, $R_{\rm cond}$]. In DIS, $R'<R$ ⇒ $J_{R'}\supset J_R$, so $T_{R'}$ never alters $J_R$'s internal factors and $\sum_{\rm graphs}C_R\Gamma=\hat{\mathsf H}_R\otimes\mathsf J_R^{\rm bare}$ (with (Com)(Abs) for adapted routing).
- New `thm:disall-renorm-compat` — 减除与 $\overline{\rm MS}$ 重整化的相容性（矩空间） [R, $R_{\rm cond}$: `asm:appN-multren`].
  - (a) $C_i\equiv\sum_k\hat{\mathsf H}_k^{\rm bare}Z_{ki}$ is finite at $\varepsilon=0$.
  - (b) It is target and regulator independent, and equals the DR partonic matching under (Z3).
  - (c) $C^{[n]}=\lim_{\lambda\to0}[T^{[n]}_{(j)}-\sum_{m<n}C^{[m]}f^{{\rm ren}[n-m]}_{\cdot/j}]$.
  - Proof: full (meromorphic + bounded ⇒ no pole, `lem:method-no-pole`).
- New `ex:disall-ladder` (two-rung ladder; **three** regions $R_2<R_1<R_H$): $r=\Delta\mathsf H_0\Delta K_2\Delta K_1$; $C_2\Gamma$, $C_1\Gamma$, $C_H\Gamma$ explicit; $C_1\to\hat{\mathsf H}^{[1]}$, $C_H\to$ two-loop coefficient with $\hat{\mathsf H}^{[1]}\otimes f^{[1]}$ and $\mathsf H^{[0]}\otimes f^{[2]}$ subtractions; the single chain term $T_H(1-T_2)\Gamma$ is not $L^1$ on $U_{R_2}$, so the grouping is necessary. Figure `fig:disall-ladder-regions`.
- `prop:disall-h2`: add the colour projection ${\rm Tr}_c[HJ]\simeq\frac1{N_c}{\rm Tr}_cH\,{\rm Tr}_cJ$ (colour-singlet target).
- `lem:disall-fsi`: add $(\xi P+q)^2=Q^2(\xi-x)/x$: as $\xi\to x$ the current jet merges into $H$. This endpoint produces the plus distributions and the threshold region (pointer to Ch12).
- `thm:disall-factorization` 「地位与缺口」 lists `asm:appN-collins`, `asm:appN-envelope`, `asm:appN-separation`, `asm:appN-cutsum`, `asm:appN-ward-product`, `asm:appN-uv`, `asm:appN-multren`, `asm:intro-bridge`.
- New figure `fig:method-coeff-minus-coll` (S56).

**S29 — Ch8: the precise subtraction theorem** (`sec:method-subtraction`; fixes OUR-2).
- `thm:method-subtraction` keeps its label and its [A] tag. **New statement.** For every leading-power integrand $\Gamma$ of the process (a single graph, or a family of graphs with a common routing), $\Gamma=\sum_{R\in\mathcal R}C_R\Gamma+r$ with $r\in\mathfrak S(\Omega)$ (`def:method-power-suppressed`). Hence $\int\Gamma=\sum_R\int C_R\Gamma+O(\lambda^aL^K)$, and each $\int C_R\Gamma$ converges absolutely.
- **New proof plan**, replacing steps (1)–(5):
  1. `thm:appN-subtraction` (the deduction);
  2. (CS1) for minimal regions from `lem:method-local-accuracy`;
  3. under (Com)(Abs) the remaining (CS1)(CS2) reduce to grouped power counting (`prop:method-product`);
  4. the grouped estimates are `asm:appN-collins`;
  5. removing $\varepsilon$ (`cor:method-removing-eps`) and the UV structure (`asm:appN-uv`).

  Delete "(2) key compatibility property" and "(5) induction". Misconception M35.
- **Status line.** "The deduction is [R, $R_{\rm cond}$]; the [A] is that of `asm:appN-collins`." Keep the CSS 1989 §10.1 quotation and the critic O10 remark.
- **New `thm:appN-subtraction` — 减除定理（条件形式）** [R, $R_{\rm cond}$: `asm:appN-contour`(a); (CS1)–(CS3) for the given $\Gamma$]. Owner: App N; Ch8 quotes it.
  - Statement: if (CS1)$_{R_0}$ and (CS2)$_{R_0}$ hold for every $R_0\in\mathcal R$ and (CS3) holds, then $\int_\Omega|\Gamma-\sum_RC_R\Gamma|\,d\mu\le C\lambda^aL^K$ for all $\lambda\le\lambda_0$, $\varepsilon\le\varepsilon_0$.
  - Each $\int C_R\Gamma$ equals the real-space integral in which every denominator keeps its own $i0$.
  - Proof: full and deliberately elementary. On $U_{R_0}$, pointwise $r=(1-T_{R_0})X_{R_0}-\sum_{R\not\le R_0}C_R\Gamma$; then `lem:method-covering`, then (CS3).
- **Revise `prop:method-chains`** (algebraic identity, no tag).
  - Add $X_{R_0}=\mathcal O_{\downarrow R_0}\Gamma$ and $r=\mathcal O_{\mathcal R}\Gamma$, where $\mathcal O_{\mathcal P}\equiv\sum_{\text{chains }c\subset\mathcal P}(-1)^{|c|}T_c$ ($T_c$ with the largest element leftmost). For a totally ordered $\mathcal P$: $\mathcal O_{\mathcal P}=(1-T_{P_n})\cdots(1-T_{P_1})$.
  - Correct the forest analogy. Chains correspond only to nested families. Incomparable regions never appear in one chain, even when their pinch sets intersect; they interact only through meets. As in BPHZ, rigorous estimates exist only for grouped expressions, never for single chain terms.
- **New `lem:method-pairing` — 配对分解** (数学，无标签).
  - Setting: $\mathcal R$ meet-closed; fix $R_0$; $\mathcal I'$ ($\mathcal I''$) = the regions incomparable with $R_0$ whose pinch sets meet (do not meet) $\pi_{R_0}$; $R_\wedge=R\wedge R_0$.
  - Pointwise: $r=\mathcal O_{\uparrow R_0}[(1-T_{R_0})X_{R_0}]-\sum_{R\in\mathcal I'}\mathcal O_{\uparrow R}T_R[(1-T_{R_\wedge})X_{R_\wedge}]-\sum_{R\in\mathcal I''}\mathcal O_{\uparrow R}T_R\Gamma$.
  - Remark to print: expanding the alternating sums $\mathcal O_{\uparrow R}$ regenerates non-integrable terms (`ex:disall-ladder`). The decomposition says which combinations must be estimated; it does not reduce the problem to single approximation errors.
- **New `prop:method-product` — 乘积公式** (数学，无标签).
  - Hypotheses: all pairwise pinch sets intersect; $\mathcal R$ is meet-closed; each $T_R$ is idempotent; (Com) $T_RT_{R'}=T_{R'}T_R$; (Abs) $T_RT_{R'}=T_RT_{R\wedge R'}T_{R'}$ for incomparable $R,R'$.
  - Conclusion: $C_R\Gamma=T_R\prod_{R'<R}(1-T_{R'})\Gamma$, $X_{R_0}=\prod_{R<R_0}(1-T_R)\Gamma$, $r=\prod_R(1-T_R)\Gamma$.
  - Equivalences: (CS1)$_{R_0}$ ⟺ $\prod_{R\le R_0}(1-T_R)\Gamma\in\mathfrak S(U_{R_0})$; (CS2)$_{R_0}$ ⟺ $T_R\prod_{R'\in\downarrow R\cup\{R_0\}}(1-T_{R'})\Gamma\in\mathfrak S(U_{R_0})$ for $R\not\le R_0$.
  - Proof: Möbius function of the meet-semilattice (meet-irreducible elements).
  - Remark: (Com)(Abs) hold exactly for momentum substitutions with adapted routing (scalar triangle). (Abs) can fail for polarization projections (`rem:method-abs-failure`).
- **New `lem:method-no-pole`** (数学，无标签): a function meromorphic near $\varepsilon=0$ and bounded on $(0,\varepsilon_0]$ has no pole at $0$.
- **New `cor:method-removing-eps` — 去掉维数正规化** [R, $R_{\rm cond}$: `thm:appN-subtraction`, `asm:appN-contour`(b)].
  - If $\int\Gamma$ is analytic near $\varepsilon=0$, then $F(\varepsilon)=\sum_R\int C_R\Gamma$ has no pole at $\varepsilon=0$, and $|\int\Gamma-F|_{\varepsilon=0}\le C\lambda^aL^K$.
  - Meaning: the UV poles of single subtraction terms cancel in the sum, as in (b) of `prop:appN-triangle-exact`.

**S30 — Ch8: the complete one-loop example** (source: Ex D.47, R6, synthesizer).
- **Enlarge `ex:method-sudakov-subtraction`** (+1.5 pp) to the **off-shell** one-loop triangle in light-cone variables. Keep the present DR on-shell paragraph as its last part. Content:
  - the kinematics of `ex:method-naive-induction`;
  - $k^-$ residues;
  - the four regions $S,C_1,C_2,H$ with $\beta_S=\frac19$, $\beta_C=\frac13$;
  - the pointwise closed forms of the $C_R\Gamma$;
  - which grouped expression supplies the small factor on each $U_R$;
  - why the soft approximation holds only on a contour that crosses the real axis near the gluon pole, ${\rm Re}\,k^-\sim k_T^2/(4k^+)$, and fails at $k^-\approx0$ (the simplest instance of "the approximation holds only on the deformed contour");
  - the values, the pole cancellation, (D.32) and the exact remainder;
  - the zero-bin as $\frac1{\varepsilon_{\rm UV}}-\frac1{\varepsilon_{\rm IR}}$ and its representation dependence (`rem:ir-regions-values`);
  - figure `fig:method-sudakov-plane`.
- **New `prop:appN-triangle-exact` — 单圈离壳三角图：Collins 减除的完整计算与精确余项** [R, R_PT]. Owner App N; Ch4 and Ch8 cite it.
  - **Setting.** Scalar triangle with massless internal lines; $p_1=(P,-\frac{m^2}{2P},\mathbf 0_T)$, $p_2=(\frac{m^2}{2P'},-P',\mathbf 0_T)$; $\tilde Q^2=2PP'$, $Q^2=-(p_1+p_2)^2=(\tilde Q^2+m^2)^2/\tilde Q^2$; regions $\{S,C_1,C_2,H\}$; normalization of VF-REF-3.
  - **(a) Subtraction terms.** After the $k^-$ residues, every $C_R\Gamma$ is an absolutely convergent iterated integral for $0<\varepsilon<1$, with
    - $\int C_H\Gamma=\tilde Q^{-2}(\mu^2/\tilde Q^2)^\varepsilon\mathcal A$;
    - $\int C_{C_1}\Gamma=\int C_{C_2}\Gamma=-\tilde Q^{-2}(\mu^2/m^2)^\varepsilon\mathcal A$;
    - $\int C_S\Gamma=\tilde Q^{-2}(\mu^2\tilde Q^2/m^4)^\varepsilon\mathcal B$;
    - $\mathcal A=\frac{\Gamma(1+\varepsilon)\Gamma(1-\varepsilon)^2}{\varepsilon^2\Gamma(1-2\varepsilon)}$, $\mathcal B=\frac{\Gamma(1+\varepsilon)^2\Gamma(1-\varepsilon)}{\varepsilon^2}$.
  - **(b) Sum.** The poles cancel ($1-2+1=0$ at $\varepsilon^{-2}$), and $\sum_R\int C_R\Gamma|_{\varepsilon\to0}=\tilde Q^{-2}[\ln^2(\tilde Q^2/m^2)+\frac{\pi^2}3]$.
  - **(c) Exact remainder.** With $I=\Phi^{(1)}(t,t)/Q^2$, $t=m^2/Q^2$, $L=\ln(Q^2/m^2)$: $\int r=-\frac{4m^2}{Q^4}+\frac{m^4}{Q^6}\big(L^2-15+\frac{\pi^2}3\big)+O\big(\frac{m^6}{Q^8}L^2\big)$. This is a full power $\lambda^2$ with **no logarithm at NLP**: the logarithms of the NLP of $I$, $t(2L^2-4L-4+\frac{2\pi^2}3)$, are reproduced by the subtraction terms through the exact kinematics $\tilde Q^2\ne Q^2$. By contrast, the general argument guarantees only relative errors $O(\lambda^{1/9})$ on $U_S$ here.
  - **(d) Values.** In the light-cone representation the zero-bin $T_{C_1}T_S\Gamma$ is $\propto\frac1{\varepsilon_{\rm UV}}-\frac1{\varepsilon_{\rm IR}}$ and is set to zero (`asm:appN-values`), while a parametric soft expansion over $[0,1]$ would give $-1/\varepsilon$.
  - **Proof:** full (App N), from the closed forms and `UsyukinaDavydychev1993a`.
  - **Checks:** R6 (`work_R6/check_remainder_d4.py`: the $d=4$ remainder density integrates to $-0.0173434339581$ at $m^2=0.02$, $P=0.8$, $P'=1.3$, 12 digits; values (a) at $\varepsilon=0.3$ to 9–10 digits). Synthesizer: `refdoc/work_SYN/triangle_remainder.py` (+`.log`), which reproduces R6's number and verifies the expansions of (c) and of $I$ to $O(t^3L^2)$.
  - **Status sentence to print.** The identities, the values and the remainder are exact. The uniform integral bounds of `thm:appN-subtraction` on a deformed four-dimensional contour have not been written even for this example. The example therefore illustrates `asm:appN-collins`; it does not verify it in integral form.

**S31 — Ch8: accuracy lemmas, the unitarity section, template hypotheses, pure gauge.**
- `lem:method-collinear-accuracy`, `lem:method-soft-accuracy` (keep [A]):
  - add "scaling statements (E-S); their integral form is `lem:method-local-accuracy`";
  - add to the soft lemma "valid on the contour of `lem:method-i0-compat`, and in the Glauber core only on the App O contour".
- `prop:method-fsi` [A]: new proof plan.
  - The light-cone cut-position identity with insertions (`lem:appO-cut-position`, 数学) and the closed-time-path form (`lem:appO-unitarity` [R, $R_{\rm cond}$: `asm:appO-lcopt`]), in which FSI internal to one jet vanish exactly.
  - For DIS-type final states, the current jet is part of $H$ in the unphysical region (`prop:disall-two-routes`).
  - State the precise setting `asm:appN-cutsum`, and why single cut graphs and gluon masses do not provide it.
- **New `tab:method-hypotheses` — 模板假设 (H1)–(H5) 与编号假设的对应.** Columns: hypothesis | precise form (labels) | status | verified per process in.

  | hypothesis | precise form (labels) |
  |---|---|
  | (H1) | `thm:ir-leading-regions` (scaling) + `asm:appN-envelope`, `asm:appN-separation` |
  | (H2) | `lem:method-ward-multi` + `asm:appN-ward-product` |
  | (H3) | revised `prop:method-glauber-deformation`; for DY-type processes `asm:appO-mixing`, `asm:appO-deformation`, `asm:appO-rewritten-cs` |
  | (H4) | `lem:method-soft-unitarity`, `prop:method-fsi`, `asm:appN-cutsum`, `asm:appO-lcopt` |
  | (H5) | `asm:appN-collins`, `asm:appN-values`, `asm:appN-uv`, `asm:appN-multren` (+ `asm:appN-tmd` for TMD) |

- **New `rem:method-pure-gauge`** (no tag).
  - The pure-gauge argument ($F[\mathcal A_{\rm eff}]=0\Rightarrow\mathcal A_{\rm eff}=-\frac ig(\partial U)U^\dagger$, $\psi\to U^\dagger\psi$) is a structural heuristic. Its step 2 is the BRST content of `lem:method-ward-multi` [A].
  - It cannot fix the Wilson-line direction: the $i0$ of `def:method-collinear-approx` does.
  - $U(+\infty)$ is a field-dependent operator, not a global gauge transformation (ERR-m2, ERR-M5, ERR-M6).

**S32 — Ch8: corrected Glauber deformation** (fixes OUR-4).
- **Revise `prop:method-glauber-deformation`** (keep [A]). Replace "the contour can be deformed to $|k^-|\sim|k_T|$" by three items.
  - **(a)** If all $k^-$ poles of the $J_A$ lines carrying the soft momentum $k$ lie in one half-plane, $k^-$ can be deformed. The soft line's own pole limits the amplitude to $\kappa\sim k_T^2/|k^+|$ (`lem:method-i0-compat`).
  - **(b)** In the Glauber region ($k^\pm\sim\lambda^2$, $k_T\sim\lambda$), deforming one component, even to $\sim|k_T|$, leaves $|k^+k^-|\sim\lambda^3\ll k_T^2$. The momentum stays in $G_\delta=\{|k^+k^-|\le\delta k_T^2\}$, and the soft approximation becomes valid only for the other jet.
  - **(c)** Leaving $G_\delta$ requires a **simultaneous** deformation of $k^+$ and $k^-$ along $e_G=n_B-n_A$, with coherent signs and amplitude $\sim|k_T|$. It only makes denominators more time-like (VF-REF-7). It is possible after the attachments to one jet have been rewritten by equal-light-cone-time localization. For colour-singlet inclusive DY this is carried out in App O (`prop:appO-target`, `thm:appO-main` [R, $R_{\rm cond}$]); in general it is part of (H3).
  - The obstruction (poles on both sides) and the unitarity pre-step (`prop:method-fsi`) are kept as they are.
- **New `rem:method-two-component`** (no tag): the geometry of (b)–(c) with the new figure `fig:method-glauber-direction` (owner Ch8 by first use; App O §O.7 refers back). Misconception M31.

**S33 — Ch10** (`ch:coll`).
- **New `lem:coll-final-poles` — 全部为末态的共线子图的极点在同一半平面** [R, R_PT].
  - Statement: take a jet subgraph all of whose external collinear lines are final-state ($e^+e^-\to hX$; the current jet of SIDIS), in its light-cone-ordered representation. Every energy denominator that depends on the minus component of a soft momentum $k$ entering the jet has its $k^-$ pole in the same half-plane, fixed by the direction of $k$.
  - Proof: full (energy denominators of an outgoing jet in light-cone-ordered form; the reference's Lemma 8.2, re-derived).
  - Ch11's `lem:dy-poles-orientation` generalizes it (forward pointer only).
- **New `lem:coll-unobserved-jet` — 未观测喷注与软辐射的幺正性相消** [A]. The jets not containing $h$, and the soft radiation, cancel in the sum over their final states: the cut sum equals the discontinuity of the forward jet function, and the contour can be moved at $O(Q)$. Proof: sketch (three arguments of the reference's Lemma 8.6; Collins 2011 §12.8).
- `thm:coll-sia`: add to the status the independent input `rem:pdf-ff-multren` (= `asm:appN-multren`(Z1)), and cite `lem:coll-final-poles`, `lem:coll-unobserved-jet` in the deduction.

**S34 — Ch11: the status layer and the LCOPT statements** (`ch:dy`, +3 pp together with S37).
- **`thm:dy-factorization`** keeps [A]. Its 「地位与缺口」 gets four layers.
  1. The survey paragraph, unchanged.
  2. 「精确形式」: `thm:appO-main` [R, $R_{\rm cond}$] → `cor:appO-interface` → `prop:appN-dy` [R, $R_{\rm cond}$] → the factorized form.
  3. The open inputs by label: `asm:appO-lcopt`, `asm:appO-envelope`, `asm:appO-mixing`(c) (beyond the $O(g^4)$ eikonal case), `asm:appO-deformation`(b)(c)(d) (**needed even for abelian graphs**), `asm:appO-rewritten-cs`, the generic `asm:appN-*`, and `asm:intro-bridge`.
  4. 「没有已知的领头幂次反例；文献中 strict-window 的非幺正残差是截断假象（\cref{prop:dy-eikonal-twogluon}）。」 Credit `AybatSterman2009` (hybrid light-cone ordering, pinch replaced by a mismatch of deformation directions) and `Diehl:2015bca`.
- **New `tab:dy-status` — DY 证明的逐步状态表.** Rows: the App O steps (O-1)…(O-8). Columns: step | statement (label) | status | error type (S7) | assumptions | literature.
- **New `lem:dy-poles-orientation` — 光锥序中间态的取向与 $k^-$ 极点** [R, R_PT], in the finite-$\eta_0$ LCOPT representation of `lem:appO-lcopt`.
  - (a) Orientation is a property of LCOPT intermediate states, not of lines. In the standard flow (initial lines carry $+k^-$, final lines $-k^-$), the intermediate states of $J_A$ before the hard vertex give energy denominators with one sign of $i0$, those after it the opposite sign. Cut $\delta$-functions are free of soft light-cone components.
  - (b) Hence the $k^-$ poles of the lines coupling to a soft $k$ lie on one side iff all the intermediate states it traverses have one orientation.
  - It generalizes `lem:coll-final-poles` and `prop:dy-glauber-pinch` (the reference's Defs E.2–E.3, Lemma E.22). Proof: full (App O).
- **New `ex:dy-spectator-lcopt` — 旁观者模型的光锥序表示.**
  - The two orderings equal the two covariant propagators. The $k^-$ integral is an equal-light-cone-time transfer of $k_T$.
  - Single orderings depend on the regulator; their sum does not.
  - It is combined with the kernel $\chi(b)=-\frac{e_Ae_B}{2\pi}K_0(m_gb)$ of `prop:dy-abelian-model`.
- **New `ex:dy-future-vs-past` — 单个割图给出未来指向的 Wilson 线** [R, R_def].
  - The identity $\frac{iQ_a}{k^-+i0}+iQ_s\big[\frac1{k^-+i0}-\frac1{k^--i0}\big]=\frac{iQ_a}{k^--i0}$ with $Q_s=-Q_a$: a single cut graph gives the **future**-pointing line.
  - The past-pointing line appears only after the one-sided rewriting (`prop:appO-past-wilson` [A]).
  - Misconception M33.
- **New `rem:dy-one-time-per-jet`** (no tag). One light-cone time per jet ($x^+$ for $J_A$, $x^-$ for $J_B$), the hybrid ordering of Aybat–Sterman 2009. "Compatible with the measurement" means: the identity operator between cut states.
- **New `rem:dy-nnlo-not-glauber`** (no tag; misconception M30). Fixed-order partonic cross sections contain no hadron spectators. Their finiteness after mass factorization (NNLO, N3LO) tests the active-parton Glauber contributions to that order. It does not test spectator–spectator exchanges, which are the content of `prop:dy-abelian-model` and App O. It is evidence, not proof.
- **New `rem:dy-dft-premises`** (no tag).
  - The Doria–Frenkel–Taylor non-cancellation (two loops, non-abelian, massive coloured initial partons, fixed colour) lies outside the premises of `thm:appO-main` (massless active partons, colour-singlet hadrons).
  - The term $\frac{m^2}{2(p_A^+)^2}k^+$ in the $A$-line denominator ties $k^+$ to $k^-$ (VF-REF-8).
  - The DFT terms are power suppressed ($m^2/s$) and vanish after averaging over the colours of the incoming partons (colour-singlet hadrons). For hadronic DY, factorization fails at $m^4/s^2$ (`Basu:1984ba`, CSS 1989 §10.2; `prop:dy-twist6-failure`).
  - Literature: `DoriaFrenkelTaylor1980`, `Frenkel:1983di`, `Catani:1985xt`; Andrási et al. 1981 and Di'Lieto et al. 1981 (S60).
- **Revise `prop:dy-deformation`** (keep [A]). The proof plan becomes the App O chain:
  1. cut-summed unitarity (`lem:appO-unitarity`);
  2. equal-light-cone-time localization (`lem:appO-equal-time`, `lem:appO-joint-localization`);
  3. one-sided rewriting with the carrier (App O §O.6);
  4. simultaneous deformation along $e_G$ (`prop:appO-target`);
  5. eikonal bounds (`prop:appO-eikonal`);
  6. past-pointing Wilson lines (`prop:appO-past-wilson`).
- **`lem:dy-fsi`** (keep [A]): its precise form is `lem:appO-unitarity` [R, $R_{\rm cond}$]. The [A] now concerns the premises (leading regions, LCOPT).
- **Misconception box:** add M30, M32, M33.

**S35 — Ch12, Ch15, Ch16.**
- **Ch12.** In `thm:thr-refactorization`, add to the 「地位」 paragraph:
  - threshold factorization is nested inside the collinear one, and its remainder is controlled by the outer one only at leading power in $(1-z)$;
  - region completeness as $z\to1$ is an extra input;
  - pointer to `prop:disall-two-routes`(c) (non-uniformity as $x\to1$).
- **Ch15.** Check that the status lines of `prop:jets-sll` and of Ch17's `prop:break-mass-singularity` separate three things:
  - (i) amplitude-level violation of strict collinear factorization [V];
  - (ii) SLLs at fixed order and resummed;
  - (iii) PDF factorization of gap cross sections [C], with restoration evidence `Becher:2024kmk` (ERR-M23).

  Optional table `tab:jets-soft-functions`: observable ↔ soft function (Wilson-line content, measurement, $q_T$/thrust/jet veto).
- **Ch16.** No change: the reference has one paragraph (§12.6).

**S36 — Ch13** (`ch:tmd`).
- **New `prop:tmd-zero-bin-soft` — 零箱减除即软因子** [R, $R_{\rm cond}$: `asm:appN-ward-product`, `asm:appN-tmd`].
  - (a) One loop, unconditional (stated in words, WRITER_SPEC §4.11): $T_RT_{R'}=T_{R'}$ when the $B$ lines carry only the on-shell external momentum and the soft momenta. This is exact for $p_B^+=0$, and holds to relative $O(e^{-2Y}p_B^+/p_B^-)$ otherwise. Hence $C_A\Gamma=T_A\Gamma-T_S\Gamma$, which after the Ward identity equals $\mathsf H^{(0)}[\tilde f_A^{{\rm unsub}(1)}(y_B)-\tilde S^{(1)}(y_A,y_B)]$.
  - (b) All orders: $\sum_{\rm graphs}\sum_R\int C_R\Gamma=\big[\mathsf H\,\tilde f_A^{\rm unsub}(y_B)\tilde f_B^{\rm unsub}(y_A)/\tilde S(y_A,y_B)\big]^{[N]}$ as formal power series.
  - Proof: full for (a); (b) by induction (App N). One-loop check: c_tmd.
- **New `lem:tmd-sqrt-identity` — 平方根构造是恒等式** [R, R_def].
  - With $\tilde f_A\equiv\tilde f_A^{\rm unsub}(y_B)\sqrt{\tilde S(y_A,y_n)/[\tilde S(y_A,y_B)\tilde S(y_n,y_B)]}$ and $\tilde f_B$ alike, $\tilde f_A\tilde f_B=\tilde f_A^{\rm unsub}\tilde f_B^{\rm unsub}/\tilde S(y_A,y_B)$ exactly, independent of $y_n$.
  - Second item, stated in words, [R, $R_{\rm cond}$: `asm:appN-tmd`(T2)]: the limits exist and $\partial\ln\tilde f_A/\partial y_n=-\tilde K$, which is the CS equation.
  - "$\tilde S$ depends only on $y_1-y_2$" is exact (boost invariance). Asymptotic linearity is dynamical.
- **New `rem:tmd-rapidity-window`** (no tag).
  - The subtraction theorem holds for rapidity cutoffs $c_0L\le Y\le c_1L$, with constants polynomial in $Y$.
  - $Y\to\infty$ is taken only after summing regions and organizing by `prop:tmd-zero-bin-soft` and `lem:tmd-sqrt-identity`.
  - Integral norms take absolute values, so the oscillation $e^{i\mathbf b_T\cdot\mathbf k_T}$ does not help.
- **New `rem:tmd-order-of-limits`** (no tag). At fixed $x$, the rapidity-regularized collinear factor differs from the light-front matrix element by $e^{2(y_B-y_k)}$, which is not small near $y_B$. Taking $y_B\to-\infty$ under the integral is (T4).
- **`lem:tmd-glauber`** (DY item): its precise form is `prop:appO-tmd` [R, $R_{\rm cond}$]. Measurement operator $e^{i\mathbf b\cdot\hat{\mathbf P}_T}$: $\sum_X|X\rangle e^{i\mathbf b\cdot\mathbf P_{XT}}\langle X|=e^{i\mathbf b\cdot\hat{\mathbf P}_T}$ commutes with light-cone evolution and with the $\tau=0$ insertions.
- **`prop:tmd-small-b`:** [applied by the audit] the remainder is $O((mb_T)^p)$, with "$p=2$ expected for unpolarized leading-twist TMDs (verify)" (OUR-5).
- **`prop:tmd-h1h5`:** cite `prop:tmd-zero-bin-soft` and `lem:tmd-sqrt-identity` for (H5), and `lem:tmd-glauber` + App O for (H3).
- **`thm:tmd-factorization` status:** the $W+Y$ matching is not uniform near $q_T\sim Q$ and $q_T\sim\Lambda$ without modified cutoffs (Collins–Gamberg–Prokudin–Rogers–Sato–Wang 2016, **verify**; ERR-M16).
- **`thm:tmd-sivers-sign` proof:** the PT route (the $\theta$ term is C-even, plus CPT).
  - No Hermitian conjugation is needed.
  - $t^a\to t^{a*}$ reverses the path ordering.
  - $\epsilon_T^{12}=+1$ (Trento) (ERR-m14).
- **`ex:tmd-oneloop`:** first step, the rapidity divergence of the unintegrated Wilson-line graphs, $\frac{\alpha_sC_F}{\pi^2}\frac{\xi}{(1-\xi)k_T^2}$, read as double counting with the other hadron.
- Optional figure `fig:tmd-rapidity-bars` (S56).
- `prop:tmd-evolution` proof sketch: the compact CS derivation $\frac12[\ln\tilde S(+\infty,y_n)-\ln\tilde S(+\infty,y_B)-\ln\tilde S(y_n,y_B)]$ with asymptotic linearity, via `lem:tmd-sqrt-identity`.

**S37 — The new result, owned by Ch11** (`sec:dy-model`; proof in App O §O.8).
- **New `prop:dy-eikonal-twogluon` — 两条程函线之间的双胶子交换：$O(g^4)$ 幺正性与 Regge 相位** [R, R_PT].
  - **Setting.** Two infinite time-like Wilson lines (rapidity difference $Y>0$, colour generators $\mathbf T_A,\mathbf T_B$) exchange two gluons of mass $m$ (IR regulator), with exact propagators ($k^+k^-$ kept), at fixed transverse momenta; $a=\mathbf k_T^2+m^2$, $b=(\mathbf K-\mathbf k)_T^2+m^2$.
  - **(a) Longitudinal integrals.** $J_{\rm box}=\frac{2\pi}{ab}(\pi+iY)$, $J_{\rm cross}=-\frac{2\pi iY}{ab}$. With $X=\mathbf T_A\cdot\mathbf T_B$, $c_{\rm box}=X^2$, $c_{\rm cross}=X^2+\frac{C_A}2X$: $J_{\rm box}c_{\rm box}+J_{\rm cross}c_{\rm cross}=\frac{2\pi}{ab}[\pi X^2-iY\frac{C_A}2X]$.
  - **(b) Interpretation.** After the transverse integrals the first term is the exponentiation term $\frac12(-i\chi)^2X^2$ (normalization VF-REF-9). The second is $i\times$real$\times$Hermitian: the one-loop reggeization phase $\propto C_AY$.
  - **(c) Consequence.** In the parametrization of `lem:appO-glauber-operator`, $p_{\rm opp}=-iY/\pi$, so ${\rm Re}\,p_{\rm opp}=0$ and the strict-window residual $-\frac12C_A\chi^2({\rm Re}\,p_{\rm opp})X$ vanishes. The two-gluon exchange graphs give $\mathcal V^\dagger\mathcal V=1+O(\chi^3)$ with no real emission (real cuts start at $O(g^6)$ for straight lines).
  - **Not shown:** the other $O(g^4)$ graphs (they can contribute only phases, by unitarity of the eikonal system — argued); non-eikonal spectators; all orders.
  - **Proof:** full (App O; residues in $k^+$ and $k^-$). Checks: R3 `work_R3/scripts/eikonal_box*.py` ($<5\times10^{-16}$ at 10 points; residues checked against brute-force $i\varepsilon$ quadrature); the synthesizer reran the closed-form script.
  - **Marking:** 「本书新结果（待文献核查）」 (S59). The ingredients are classical: the high-energy limit of the eikonal box and crossed box, $\ln(-s)$ vs $\ln s$ (Cheng–Wu 1969; Korchemskaya–Korchemsky 1994–95; Caron-Huot 2013 — none of them in `refs_merged.bib`, S60). The refs agent must check whether the conclusion — the strict-truncation residual is an artefact — is already in print before the label is used.
- **New `rem:dy-common-ordering` — 共同时序是物理结果** (no tag).
  - (i) The exact graphs put the whole $s$-channel weight into the uncrossed graph. The RS regulator agrees: crossed Glauber boxes vanish, and the ladders exponentiate to a Hermitian colour phase (`RothsteinStewart2016` eqs. (9.1), (9.18), (9.19)).
  - (ii) For eikonal spectators to all orders, unitarity follows from the unitarity of $T\exp\{ig\int dt[v_A\cdot A(v_At)\mathbf T_A+v_B\cdot A(v_Bt+\mathbf b)\mathbf T_B]\}$, at the same formal level as `lem:method-soft-unitarity`.
  - (iii) The genuine open problem is the interplay of Glauber, soft and collinear modes for non-eikonal (composite, interacting) spectators and for active partons (`asm:appO-mixing`(c)).
- Ch11 misconception **M32** (S57): "the non-abelian two-Glauber exchange leaves a non-unitary residual".

**S38 — Ch14** (`ch:scet`).
- `rem:scet-assumptions`: open and close the chapter with the map of the three SCET premises onto the three difficulties of the graphical method.

  | SCET premise | graphical difficulty |
  |---|---|
  | mode completeness | region completeness and power counting (`asm:intro-bridge`, `asm:appN-envelope`) |
  | zero-bin consistency | subtraction combinatorics (`asm:appN-collins`) |
  | Glauber Lagrangian and rapidity regulator | `asm:appO-*` |

  "SCET proofs are not more rigorous than Collins'; they are complementary."
- `rem:scet-y-direction` (existing): correct it (ERR-m18).
  - The LO SCET rules already give future-pointing $Y$ lines for outgoing collinear quarks (`Chay:2004zn`); the direction is fixed by matching the external states.
  - The $\lambda^2Q$ mode is ultrasoft.
- **New `rem:scet-glauber-dictionary` — Glauber SCET 与光锥序证明的对照** (no tag).
  - RS Glauber operators ↔ the window/carrier construction.
  - The RS rapidity regulator $|2k^z|^{-\eta}$ ↔ the common ordering (`rem:dy-common-ordering`); crossed Glauber boxes vanish.
  - RS: "taken on its own this is far from a proof of factorization".
- `def:scet-zero-bin`: add that zero-bin integrals for thrust are scaleless by $a^{-\varepsilon}$ scaling (the reference's Prop D.30, re-derived). `thm:scet-thrust` cites it.

**S39 — Ch17** (`ch:break`).
- **New `prop:break-measurement` — 测量相容性判据** [R, $R_{\rm cond}$: `asm:appO-lcopt`].
  - Statement: if the measurement operator $\Pi$ on cut states commutes with the light-cone evolution $U$ of App O and with the $\tau=0$ insertions, the cut-sum unitarity lemmas (`lem:appO-unitarity`) hold with $\Pi$ inserted.
  - Examples: $\Pi=1$ (inclusive); $\Pi=e^{i\mathbf b\cdot\hat{\mathbf P}_T}$ (TMD DY).
  - Proof: full (an operator identity).
  - A following remark (no tag) locates the failures:
    - $\Pi_h$ (identified hadrons in $pp\to h_1h_2X$) and $\Pi_{\rm gap}$ do not commute;
    - for $pp\to h_1h_2X$ the argument breaks at the one-sided rewriting step (O-3), with the Glauber region taken relative to $(n_A,w_1)$ (ERR-M31).
  - Use it as the organizing criterion of `sec:break-overview`.
- `tab:break-cases`: refine the gap row as in S35 (ERR-M23).
- `thm:break-tmd` [V]: add the location of the failure in the App O framework (not a new proof of violation).
- `conj:dy-coloured-final` (Ch11) and `tab:break-cases`: note that the App O argument fails for coloured final states at step (O-3).
- `prop:break-colour`: add the warning that an "in = out" bookkeeping with a uniform eikonal numerator gives no Sivers flip (ERR-S2), as an exercise.
- `thm:break-double-dy` [A]: add the App O remark (same structure; `Diehl:2015bca`).

**S40 — Ch18** (`ch:excl`).
- **New `prop:excl-soft-cancel` — 色单态介子的软胶子在被积函数层次相消** [R, $R_{\rm cond}$: `asm:appN-endpoint`, `asm:appN-collins`].
  - Statement: for the pion form factor and the meson side of $\gamma_L^*$ meson production, soft gluons attached to the colour-singlet meson jets cancel at the integrand level. The cancellation is the smallness of the soft-approximation error for a small colour dipole.
  - The endpoint conditions (E1)–(E3) are the hypotheses. The argument fails for twist 3 and for transverse photons, where they are violated.
  - Proof: full given the assumptions (App N §N.6).
- `thm:excl-pion-ff`: remainder $O(\frac{\Lambda^2}{Q^4}\ln\frac{Q^2}{\Lambda^2})$ (ERR-m15). Gegenbauer remark: the endpoint conditions hold for every finite truncation.
- `prop:excl-meson-T` [V]: the correct mechanism (ERR-M17).
  - The WW twist-3 integrals diverge logarithmically because $g_\perp^{(v)}(0)\ne0$.
  - There are double poles $(\xi\mp x-i0)^{-2}$.
  - The leading-twist $\gamma_T^*\to V_T$ amplitude vanishes by chirality (`Diehl:1998pd`, `CollinsDiehl2000`, `Mankiewicz:1999tt`).
- `thm:excl-meson-L` status: list `asm:appN-endpoint`, `asm:appN-collins`, `asm:intro-bridge`.
- `prop:excl-endpoint` [P]: add the colour-transparency statement (the Wilson-line pair of a small dipole is $1+O(b\Lambda)$) and the endpoint-area estimate $c(1-\ln c)$. Combine them with our exact $R_{\rm as}(c)$ curves (c_exclusive).

**S41 — Ch19** (`ch:heavy`).
- **New `prop:heavy-btopi-ff` — 重到轻形状因子：软重叠与硬旁观者** [A].
  - Statement: at leading power in $\Lambda/m_b$ and large recoil, $F^{B\to\pi}=C(E)\,\xi_\pi(E)+\int T\,\phi_B\,\phi_\pi$ (soft overlap + hard spectator), to all orders in $\alpha_s$.
  - Literature: `Bauer:2002aj`, `Beneke:2003pa`. The further factorization of $\xi_\pi$ fails (endpoint divergences, `prop:heavy-qcdf-endpoint`).
- `prop:heavy-qcdf-lp` keeps [P] (D3). Add the SCET LP derivations to its literature: `Bauer:2004tj` (with the charming-penguin caveat) and Chay–Kim 2004 (S60) (ERR-M21).
- `thm:heavy-nrqcd-decay` [A]: add "non-perturbatively the decay rate needs local duality, since it is Minkowskian at a fixed point and not covered by the OPE assumptions" (ERR-M9).
- `conj:heavy-nrqcd-production`: the NQS statement exactly — the gauge completion is necessary at NNLO, relative order $v^2$ (ERR-M19).

**S42 — Ch20** (`ch:power`).
- **New `prop:power-rearrangement` — OPE 基的重排自由** [R, R_def].
  - Statement: given the OPE with growth bounds, $O'_i=O_i+\sum_{d_j<d_i}\kappa_{ij}\Lambda^{d_i-d_j}O_j$ gives a valid OPE with $\tilde C'_j=\tilde C_j-\sum_{d_i>d_j}\tilde C'_i\kappa_{ij}\Lambda^{d_i-d_j}$ (top-down) and the same remainder.
  - (a) Twist-2 coefficients are meaningful only to relative $O(\frac{\Lambda^2}{Q^2}\ln^kQ)$, unless the basis is fixed non-perturbatively.
  - (b) Rearranging only twist $\ge4$ changes twist-2 coefficients by $o(\alpha_s^K)$, so `thm:dis-moments-np` is unaffected.
  - Proof: full.
- **New `rem:power-practical-ope`** (no tag).
  - The practical OPE "$|k|>\mu_F$" is routing-dependent and gauge-breaking; it needs a gauge-invariant smooth cutoff, which is not available.
  - Renormalon absorption into twist 4 has exactly two conjectural ingredients: Borel continuation along $\mathbb R_+$ near the singularities, and factorization of the renormalon residue with RG-matched $\alpha_s$ dependence. Both are verified at large $\beta_0$; the general case is the Mueller/David conjecture `conj:power-renormalon-ht`.
- `prop:power-renormalon-examples` [P]: add the proven case, the large-$N$ O($N$) σ-model (David; Novikov–Shifman–Vainshtein–Zakharov; Beneke–Braun–Kivel 1998, S60), and the Borel summability of the Gross–Neveu model (Feldman–Magnen–Rivasseau–Sénéor, S60) (ERR-m19).
- `rem:power-np-status`: add the per-order meaning of power suppression (F3). "Asymptotic, not summable; exponents from the general method can be far from sharp" (`prop:appN-triangle-exact`(c)).

**S43 — Ch21** (`ch:lattice`). `prop:lattice-moments` [R, 以 OPE 为前提]: add that the lattice moments test `thm:dis-moments-np`, including the $n<n_0$ caveat (`asm:intro-growth`), and that the twist-2 basis is normalized non-perturbatively on the lattice (`prop:power-rearrangement`(a)).

**S44 — Ch22** (`ch:summary`; +2 pp).
- `tab:summary-master`: the "瓶颈假设" column names `asm:` labels instead of prose.
- **New `tab:summary-assumptions`**: an incidence matrix (process theorems × register entries).
- Open problems:
  - No. 1 (DY): reword as "discharge `asm:appO-mixing`(c), `asm:appO-deformation`(b)–(d), `asm:appO-rewritten-cs`".
  - No. 3: add "integral-norm form of (CS1)–(CS3) on a deformed contour, even for the Sudakov form factor and the one-loop triangle".
  - No. 4: keep the wording (D3); add "possibly dischargeable parts: `asm:appM-remainder` (Anikin–Zav'yalov), `asm:appM-brst-ope` (Joglekar, Hollands)".
  - New No. 15: H-emission endpoints and coincident SA/AS insertions (non-analytic ordering weights).
  - New No. 16: the growth condition `asm:intro-growth` (fixed poles, the momentum sum rule).
  - New No. 17: forward on-shell OPE (`asm:appM-forward`).
- `sec:summary-lessons`: add the lesson that rigour statements are about grouped expressions, never single terms (`ex:method-naive-induction`).

**S45 — Cross-cutting chapter format** (WRITER_SPEC §6; all core chapters: Ch3, Ch5–Ch9, Ch11, Ch13).
1. Open with a box 「本章证明了什么／没有证明什么」 (5–8 lines, labels only).
2. Every chapter whose precise version lives in App M/N/O ends with a correspondence table `tab:<key>-correspondence`: chapter statement | precise version (App label) | what differs (assumptions, error type).
3. Every 「地位与缺口」 paragraph names the `asm:` labels it depends on, not only (H1)–(H5) and MA.
4. Every [A]/[P] proof sketch step that rests on power counting names its error type (S7).

### 5.6 The new appendices: contents, labels, tags

General rules (in addition to FINAL_OUTLINE's appendix rules):
- App M, N, O hold the complete proofs of the statements that Ch6, Ch8/Ch9/Ch13/Ch18 and Ch11/Ch13/Ch17 announce. These statements keep their chapter labels; the appendix section begins with 「\cref{…} 的证明」.
- Statements first stated in an appendix carry `appM-`/`appN-`/`appO-` keys.
- Every appendix opens with what is proved and what is assumed (S45 item 1) and closes with a status table with error types.

**S46 — App M** (`app:appM`, `appM_ope.tex`, 24 pp; source: reference App C, R5, our c_dis).

| § | label · title | content and labels | pp |
|---|---|---|---|
| M.1 | `sec:appM-overview` 概览 | what is proved and assumed; `fig:appM-dependency` (moment theorems ← assumptions) | 1.5 |
| M.2 | `sec:appM-bphz` BPHZ 与正规乘积 | forest formula, Zimmermann convergence, vertex-additive degrees and the counterexample of a non-additive choice (cited theorems with exact statements: `Zimmermann1969`, `LowensteinZimmermann1975`, `Lowenstein:1974qt`) | 2.5 |
| M.3 | `sec:appM-chain` 链展开与 OPE 恒等式 | `lem:appM-chain-expansion` (数学: one identity gives the Zimmermann identities and the OPE identity); `def:appM-normal-product` (frozen-$q$ bilocal normal product); `lem:appM-integrability` (absolute integrability); `lem:appM-contact` (contact terms); `thm:appM-ope-identity` [R, R_PT] (the OPE identity at the level of normal products, massive models, with routing compatibility for frozen $q$ and disconnected $\omega$); `ex:appM-tree` (tree OPE = Taylor expansion); `fig:appM-handbag-ab` | 4 |
| M.4 | `sec:appM-remainder` 余项、唯一性与标度 | `asm:appM-remainder`; `lem:appM-derivative-bounds` (数学: homogeneity, $O(4)$, Lagrange identity); `lem:appM-uniqueness` [R, R_PT] (order-by-order uniqueness; exact uniqueness from the log-polynomial structure); `thm:appM-scaling` [R, $R_{\rm cond}$: `asm:appM-remainder`] (scaling of the *reduced* coefficients from uniqueness); `cor:appM-coordinate` [R, $R_{\rm cond}$] (coordinate-space remainder); `ex:appM-unreduced` (unreduced coefficients violate scaling; the sharpened value $-\kappa\pi^2/(2q^4)$, VF-REF-14) | 3.5 |
| M.5 | `sec:appM-massless` 无质量 QCD | proof location of `prop:dis-ope-euclid` [A] (cited Euclidean theorems; BPHZL vs DR+$R^*$); forward on-shell momenta are exceptional; `asm:appM-forward` | 1.5 |
| M.6 | `sec:appM-brst` BRST、规范不变算符与扭度 | local cohomology $H(s)$ vs $H(s\vert d)$; Joglekar–Lee (sketch; `Joglekar:1975nu`, `Joglekar:1976eb`, `Joglekar:1976pe`, `Hollands:2007zg`); aliens vanish off-forward or IR-regulated (forward on-shell caveat: Hamberg–van Neerven, `Collins:1994ee`); `asm:appM-brst-ope`; proofs of `prop:dis-ope-gi`, `lem:dis-twist-classification`, `lem:dis-twist-chirality`, `prop:dis-chiral-suppression`, `prop:dis-ope-rg` (from uniqueness) | 3.5 |
| M.7 | `sec:appM-forward` 固定阶的全自旋求和 | proof of `prop:dis-ope-forward` (scaleless matrix elements force twist 2; Taylor-coefficient contradiction argument; amplitude form with the odd quark extension and gluon factor 2; check against c_dis, $N\le8$) | 1.5 |
| M.8 | `sec:appM-np` 非微扰层 | commentary on `asm:intro-wightman`…`asm:intro-growth` (which axiom is used where; corrected (W2)); proofs of `prop:dis-dispersion-np` (forward tube, Vladimirov bound, edge of the wedge with $Q^2$-smearing, positivity, almost-analytic extension; `lem:appK-entire`), `lem:dis-ope-segment` (`lem:appK-markov`), `thm:dis-fixed-n`, `prop:dis-low-moments`, `thm:dis-moments-np` (mass-mixing rescaling), `cor:dis-weak-xspace` | 5 |
| M.9 | `sec:appM-status` 状态 | `tab:appM-status` (step, status, error type, assumptions); remarks: AQFT OPE (Bostelmann), instantons $(\Lambda/Q)^b$, no $1/Q^2$ in the vacuum OPE | 1 |


**S47 — App N** (`app:appN`, `appN_subtraction.tex`, 24 pp; source: reference App D, R6).

| § | label · title | content and labels | pp |
|---|---|---|---|
| N.1 | `sec:appN-setting` 设定 | integrands, routing, measure, $\Omega$, $\varepsilon$-uniformity; proofs of `lem:method-meets`, `lem:method-covering`; the nine-region poset (`fig:method-hasse`, owner Ch8) | 2.5 |
| N.2 | `sec:appN-inputs` 几何–解析输入 | (GA1)–(GA4): `asm:appN-contour`, meet closure as a definition, `asm:appN-envelope`, `asm:appN-separation`, with the status of each (corrected no-Glauber condition $\vert k^+k^-\vert \gtrsim k_T^2$; Łojasiewicz exponent 2; endpoint assignments) | 2.5 |
| N.3 | `sec:appN-theorem` 定理与组合恒等式 | `thm:appN-subtraction` + proof; proofs of `prop:method-chains`, `lem:method-pairing`, `prop:method-product` (Möbius), `cor:method-removing-eps`; the correct forest analogy; `asm:appN-values` | 3.5 |
| N.4 | `sec:appN-approximators` 近似子与误差 | idempotent projectors; proof of `lem:method-i0-compat`; (Com)(Abs) and the failure of (Abs) (`rem:method-abs-failure`, with the edge case); proofs of the rows of `tab:method-errors` (owner Ch8), `lem:method-telescoping`, `lem:method-local-accuracy` | 3.5 |
| N.5 | `sec:appN-processes` 过程 | `asm:appN-cutsum` ((X1) supplied by App O for DY-type graphs); DIS: proofs of `prop:disall-two-routes`, `prop:disall-factorized-subtraction`, `thm:disall-renorm-compat`; `asm:appN-uv`, `asm:appN-multren`; thrust zero-bin scaleless; DY: `prop:appN-dy` [R, $R_{\rm cond}$: `cor:appO-interface`, `asm:appN-collins`, `asm:appN-cutsum`] (DY collinear factorization = cut-summed Glauber cancellation + the $e^+e^-$-type combinatorics, disjoint blocks); TMD: `asm:appN-tmd`, `asm:appN-ward-product`, proof of `prop:tmd-zero-bin-soft`(b), the rapidity window | 5 |
| N.6 | `sec:appN-exclusive` 遍举 | `asm:appN-endpoint`; proof of `prop:excl-soft-cancel` | 1.5 |
| N.7 | `sec:appN-examples` 例子 | `prop:appN-triangle-exact` + proof; the details of `ex:method-naive-induction` and `ex:disall-ladder` | 4 |
| N.8 | `sec:appN-status` 状态 | `tab:appN-status` (every item: status, error type, assumption labels) | 1.5 |

**S48 — App O** (`app:appO`, `appO_glauber.tex`, 32 pp; source: reference App E, R7, R8, our c_glauber).

| § | label · title | content and labels | pp |
|---|---|---|---|
| O.1 | `sec:appO-overview` 架构 | `fig:appO-flowchart`; the steps (O-1) regions, domain and windows; (O-2) leading-power form in LCOPT; (O-3) cut sum and one-sided rewriting (unitarity, localization, carrier); (O-4) consistency of the subtraction (chain) terms with the rewriting; (O-5) deformation target; (O-6) eikonal approximation and past-pointing Wilson lines; (O-7) soft factor $=1$ and collinear factors; (O-8) interface with App N (these are the reference's (S1)–(S8)); what is proved; precedents `AybatSterman2009`, `Diehl:2015bca`; the reference's Ass. E.33(c1) is replaced by a lemma | 2 |
| O.2 | `sec:appO-lcopt` 光锥序微扰论 | `lem:appO-lcopt` [R, R_PT] (LCOPT from Feynman integrals at finite $\eta_0$: absolute convergence, $\dim W\le\vert L_W\vert-1$, Fubini, sector decomposition); `lem:appO-numerators` [R, R_PT] (instantaneous terms; instantaneous loops independent of external minus energies); `asm:appO-lcopt`; `fig:appO-lcopt-term` | 4 |
| O.3 | `sec:appO-orientation` 取向与幂次计数 | proof of `lem:dy-poles-orientation`; inter-term pinches; `lem:appO-glauber-pc` [R, R_PT] (Glauber power counting; scaling statement); `lem:appO-hard-locality` [R, $R_{\rm cond}$: `asm:appO-lcopt`] ($V_H$ at $\tau=0$ on both sides; the unweighted variable $\mathcal E$) | 3 |
| O.4 | `sec:appO-unitarity` 割图求和的幺正性 | `lem:appO-cut-position` (数学: exact light-cone cut-position identity with insertions, at most two insertion terms); `lem:appO-unitarity` [R, $R_{\rm cond}$: `asm:appO-lcopt`] (closed-time-path form; FSI internal to one jet vanish); `fig:appO-cutsum` | 3 |
| O.5 | `sec:appO-localization` 等光锥时刻局域化 | `lem:appO-equal-time` (数学: contact term $c[O(0),V_H(0)]$, $c=R_\downarrow(0)/R(0)$; proof of (iii) by closing in the lower half-plane); `prop:appO-ss-localize` [R, $R_{\rm cond}$] (SS localization error with its logarithm; Hermitian $V_G$; vertex $+ig$); `lem:appO-joint-localization` [R, R_PT] (ordering weights, VF-REF-12, single-pole external factors); `prop:appO-ss-cancel` [R, $R_{\rm cond}$] (family cancellation for non-coincident connections on window cores); `lem:appO-glauber-operator` [R, R_def] (the $p_{\rm opp}$ parametrization, VF-REF-10); `asm:appO-mixing` | 5 |
| O.6 | `sec:appO-rewriting` 单侧改写 | windows and the entire carrier $\phi(x)=2\sqrt\pi e^{-x^2}$; `prop:appO-one-sided` [R, $R_{\rm cond}$: `asm:appO-envelope`] (one-sidedness in weak equivalence, E-W); `asm:appO-envelope`; why only weak; SA/AS construction; the H-emission endpoint obstruction | 3.5 |
| O.7 | `sec:appO-deformation` 同时形变 | $e_G$ (VF-REF-7; `fig:method-glauber-direction`, owner Ch8); `lem:appO-no-crossing` [R, R_PT]; `prop:appO-target` [R, R_PT] (graded configurations; constants $\kappa^2<1/(2KN_C^2)$, $c=\min(\kappa^2,\delta/2)$); `asm:appO-deformation`; `prop:appO-eikonal` [R, R_PT] (eikonal bounds on the deformed contour; Grammer–Yennie ratio; $O(1)$ failure on the real contour); optional `fig:appO-glauber-flow` | 4.5 |
| O.8 | `sec:appO-wilson` Wilson 线 | `prop:appO-past-wilson` [A] (Ward identity on the rewritten forms gives past-pointing lines; contrast `ex:dy-future-vs-past`); past-line unitarity ($T[\mathcal U^{(-)}]=U_I(0,-\infty)$, role of $v^0>0$; pointer to `lem:method-soft-unitarity`); proof of `prop:dy-eikonal-twogluon` (`fig:dy-two-gluon-exchange`, owner Ch11) | 2.5 |
| O.9 | `sec:appO-main` 主定理 | `thm:appO-main` [R, $R_{\rm cond}$] (below); `cor:appO-interface` [R, $R_{\rm cond}$] (the clauses (Gla-a), (Gla-b), (Gla-c) used by `prop:appN-dy`); `prop:appO-tmd` [R, $R_{\rm cond}$] (with $e^{i\mathbf b\cdot\hat{\mathbf P}_T}$ inserted) | 2 |
| O.10 | `sec:appO-checklist` 严格性清单 | `tab:appO-checklist`: step, statement, status, error type, assumptions, Glauber-specific (yes/no) — with the corrected bookkeeping (ERR-M29) | 1.5 |
| O.11 | `sec:appO-neighbours` 相邻问题 | $pp\to h_1h_2X$ (fails at (O-3); corrected argument, ERR-M31); gaps; DFT (`rem:dy-dft-premises`); double DY; the RS dictionary (`rem:scet-glauber-dictionary`). Cut first if pages are short. | 1 |

**`thm:appO-main` — 单举色单态 DY 中 Glauber 区相消的条件定理** [R, $R_{\rm cond}$: `asm:appO-lcopt`, `asm:appO-envelope`, `asm:appO-mixing`, `asm:appO-deformation`, `asm:appO-rewritten-cs`]. (It supplies (X1) of `asm:appN-cutsum` for these graphs; (X2)(X3) enter only in `prop:appN-dy`.)
- **Setting.** Colour-singlet inclusive DY with massless active partons, at fixed order in perturbation theory, summed over all cuts and all graphs of the order.
- **Statement.** The cut-summed integrand is weakly equivalent (E-W) on the algebra of the regions to an integrand in which:
  - spectator Glauber exchanges are absent;
  - every soft attachment to $J_A$ ($J_B$) is replaced by a past-pointing Wilson line along $n_B$ ($n_A$);
  - the subtraction terms have the same structure.

  The error is $O(\lambda^aL^K)$.
- **Proof:** steps (O-1)…(O-8) with their error types (S7).
- **Remark to print:** the hypotheses (b)–(d) of `asm:appO-deformation` are needed even for abelian graphs.

**S49 — App P** (`app:appP`, `appP_blueprint.tex`, 8 pp; generated by the lead author, no writer).
- **`tab:appP-register`:** the 25 assumptions; columns label | owner | content (one line) | status | used by (from `\uses{}`) | upgrade path.
- **`fig:appP-dependency`:** the dependency graph of the canonical statements, coloured by tag, $R_{\rm cond}$ statements with dashed edges to their `asm:` premises.
- **`tab:appP-status`:** every canonical statement; columns label | tag | qualifier | premises | error type of the weakest step.
- **Generator checks:**
  - no forward edges (FINAL_OUTLINE §0.8);
  - every `asm:` label is used at least once;
  - grade propagation: no process statement carries a tag stronger than its weakest premise (S5);
  - every $R_{\rm cond}$ statement lists its premises in its first sentence.

### 5.7 Changes to the existing appendices

**S50 — App K** (+1 p).
- **New `lem:appK-entire`** (数学). Entire functions of controlled growth: the reference's Lemma C.63, used in the proof of `prop:dis-dispersion-np`.
- **New `lem:appK-markov`** (数学). V. A. Markov's coefficient inequality: for a real polynomial $p$ of degree $\le N$, $|p^{(k)}(0)|/k!\le c_{N,k}\,h^{-k}\max_{|x|\le h}|p(x)|$, where $c_{N,k}$ is the corresponding coefficient bound attained by the Chebyshev polynomial $T_N$. Used in `lem:dis-ope-segment` and `thm:dis-fixed-n`.
- `rem:appK-counterexamples`: add the Hausdorff-problem caveat of `cor:dis-weak-xspace`.

**S51 — App A and App C** (no budget change).
- App A `sec:appA-plus`: the precise test-function class (the reference's App B), and the weak-convergence statement used in `cor:dis-weak-xspace`.
- App C `sec:appC-msbar`: the $d$-dimensional splitting kernels with the averaging conventions (gluon $1/(D-2)$, quark $\frac12$).

**S52 — App D, E, F** (+2, +2, +2 pp; S10).
- **App D `sec:appD-alpha`:**
  - the Feynman-parameter proof of the Landau conditions ($\eta_j=\alpha_j\partial_j\mathcal F$, envelope theorem, homogeneity) with its caveats, as an alternative to our constraint-preserving deformation;
  - the details of `rem:ir-euclid-corners` ($\mathcal F=m^2\alpha_0(\alpha_1+\alpha_2)+Q^2\alpha_1\alpha_2$ and its corners, VF-REF-17);
  - the parameter-space vs momentum-space distinction (`Collins:2020euz` App D1).
- **App E:**
  - the boost-and-dimension proof of `prop:appE-degree` (optional `fig:appE-boost`);
  - `rem:appE-actual-bound` links to `asm:appN-envelope` (scaling vs integral bound).
- **App F:**
  - `sec:appF-one`: the telescoping example with $W^{(1)}[w^-,0]=gt^a(1-e^{-ik^+w^-})/k^+$ (signs re-derived in our conventions);
  - `sec:appF-gy`: the Grammer–Yennie decomposition with its $i0$ (DIS $K_{\mu\nu}=k_\mu w_{2\nu}/(k\cdot w_2-i0)$; the one-sided form is Collins' adaptation of the symmetric original, ERR-m3);
  - the abelian/tree status of the pure-gauge argument (`rem:method-pure-gauge`).

**S53 — App J** (+2 pp).
- **New `lem:appJ-cut-hermiticity` — 割图规则的厄米性** [R, R_def].
  - With Hermitian ghost fields (e.g. Kugo–Ojima's $c,\bar c$ with $\mathcal L_{\rm FP}=-i\partial^\mu\bar c^aD_\mu^{ab}c^b$; the convention must match `prop:appJ-ghost-cuts`, **verify**), the vertex factors on the two sides of the cut are complex conjugates, including the three-gluon and ghost vertices.
  - The LCOPT on-shell numerators are the same polynomials on both sides of the forward graph.
  - Hence the cut rules are Hermitian. This discharges the reference's Ass. E.18(iii), so `asm:appO-lcopt` keeps only (i)(ii).
- `sec:appJ-cuts`: state the setting of `asm:appN-cutsum` (why single cut graphs and gluon masses do not give a cut-summed representation with common domain).

### 5.8 VERIFIED_FORMULAS, master table, registry

**S54 — VERIFIED_FORMULAS: new group VF-REF.** The status codes are those of VERIFIED_FORMULAS: V = script-checked by an agent; A = re-derived, not script-checked; T = to verify.

| ID | formula (binding conventions) | status · source | used in |
|---|---|---|---|
| VF-REF-1 | rest frame, Euclidean $q$, $\vert\mathbf q\vert\ge Q/2$: $\omega=2iMq^4/Q^2\in\{iy:\vert y\vert\le\sqrt3M/Q\}$, $\hat P^2=M^2\mathbf q^2/Q^2$; projector $T_2=\frac{3\nu}{2(\hat P^2)^2}[\hat P_\mu\hat P_\nu-\frac{\hat P^2}3g_{\mu\nu}]T^{\mu\nu}$, $\hat P=P-\frac{P\cdot q}{q^2}q$ | A · R5; re-derived by the synthesizer (both parts) | `lem:dis-euclid-segment`, `lem:dis-ope-segment` |
| VF-REF-2 | $Q^2I=\Phi^{(1)}(t,t)=\frac{4{\rm Li}_2(-\rho t)+\ln^2(\rho t)+\pi^2/3}{\sqrt{1-4t}}$, $\rho=\frac2{1-2t+\sqrt{1-4t}}$; $=L^2+\frac{\pi^2}3+t(2L^2-4L-4+\frac{2\pi^2}3)+t^2(6L^2-14L-11+2\pi^2)+O(t^3L^2)$ | V · R6; `work_SYN/triangle_remainder.py` ($<10^{-49}$ vs the 1D integral; expansion residuals $O(t^3L^2)$) | `ex:sudakov-offshell`, `prop:appN-triangle-exact` |
| VF-REF-3 | the subtraction terms (a), the sum (b) and the remainder (c) of `prop:appN-triangle-exact` | V · R6 (`check_remainder_d4.py`, `check_algebra.py`); synthesizer | `ex:method-sudakov-subtraction`, `prop:appN-triangle-exact` |
| VF-REF-4 | finite-subtraction dispersion relation (d) of `prop:dis-dispersion-np`; low moments ⟺ $T_2(iy)=o(y)$ | A · R5 | Ch6, App M |
| VF-REF-5 | $\int_0^1P^{V(1)}_{q\bar q}=0.71931\,C_F(C_F-\frac{C_A}2)$ | V · R2 `check_Pplusminus.py` | `rem:pdf-ns-plusminus` |
| VF-REF-6 | TMC: $\frac{n(n-1)}{n+2}\frac{M^2}{Q^2}a_{n+2}$ | V · R4 | `ex:dis-tmc-n2` |
| VF-REF-7 | $e_G=n_B-n_A$; $(l+it\sigma fe_G)^2-m^2=(l^2-m^2+2t^2f^2)+2it\sigma f(l^+-l^-)$ | V · R7, R8 | `prop:method-glauber-deformation`, App O |
| VF-REF-8 | $(p_A-k)^2-m^2=-2p_A^+\big(k^-+\frac{m^2}{2(p_A^+)^2}k^+\big)+k^2$ for $p_A=(p_A^+,\frac{m^2}{2p_A^+},\mathbf 0_T)$ | A · elementary | `rem:dy-dft-premises` |
| VF-REF-9 | $J_{\rm box}=\frac{2\pi}{ab}(\pi+iY)$, $J_{\rm cross}=-\frac{2\pi iY}{ab}$; $c_{\rm box}=X^2$, $c_{\rm cross}=X^2+\frac{C_A}2X$; the sum $\frac{2\pi}{ab}[\pi X^2-iY\frac{C_A}2X]$; $p_{\rm opp}=-iY/\pi$ | V · R3 `eikonal_box*.py`; synthesizer rerun | `prop:dy-eikonal-twogluon` |
| VF-REF-10 | $\mathcal V^\dagger\mathcal V-1=-\frac12C_A\chi^2({\rm Re}\,p_{\rm opp})X+O(\chi^3)$; equal weights ((E.51)): $A_2=\frac12(-i\chi)^2(X^2+\frac14C_AX)$, residual $-\frac14C_A\chi^2X$ | V · R3, R7, R8; (E.51) read on the page image | `lem:appO-glauber-operator` |
| VF-REF-11 | $\frac{iQ_a}{k^-+i0}+iQ_s\big[\frac1{k^-+i0}-\frac1{k^--i0}\big]=\frac{iQ_a}{k^--i0}$ for $Q_s=-Q_a$ | V · R8 | `ex:dy-future-vs-past` |
| VF-REF-12 | $w_{12}=\frac{z_1}{z_1+z_2}$, $z_j=\frac{k_{Tj}^2}{2k_j^+}$ (same-side poles; $0$ or $1$ for $k_1^+k_2^+<0$); $N$ insertions: $\prod_jz_j/\prod_m\sum_{l\ge m}z_{\pi(l)}$ | V · R8 `check_weights.py` | `lem:appO-joint-localization` |
| VF-REF-13 | the square-root identity of `lem:tmd-sqrt-identity` | V · R6 (symbolic) | Ch13 |
| VF-REF-14 | unreduced coefficient example: $-\frac{\kappa\pi^2}{2q^4}+O(m^2q^{-6}\ln q)$ | V · R5 | `ex:appM-unreduced` |
| VF-REF-15 | WW: $g_\perp^{(v)}(0)=\frac12\int_0^1du\,\phi_\parallel(u)/u\ne0$ | T · R3 (literature: `Mankiewicz:1999tt`) | `prop:excl-meson-T` |
| VF-REF-16 | all-outgoing charges: Glauber factor $\propto\mathbf T_b-\mathbf T_c-\mathbf T_d=\mathbf T_a+2\mathbf T_b$; Collins–Qiu $i\pi(g_1+2g_2)$ | V · R4 `checks_R4.py`; cross-check with the VF entry behind `prop:break-colour` | Ch17 |
| VF-REF-17 | off-shell triangle: $\mathcal F=m^2\alpha_0(\alpha_1+\alpha_2)+Q^2\alpha_1\alpha_2$; Landau solutions only at the simplex corners (zero-momentum massless lines) | A · R1 | `rem:ir-euclid-corners` |
| VF-REF-18 | $C_{C_2}\Gamma=\frac{m^2}{2PP'}\frac1{D_gD_2e_2}-\frac1{h_1D_2e_2}$; $(1-T_{C_1})T_S\Gamma=\frac1{D_ge_1}(\frac1{e_2}-\frac1{h_2})$ (denominators as in App N §N.7) | V · R6 `check_algebra.py` | `ex:method-naive-induction` |
| VF-REF-19 | $n_A(y_A)\cdot k=-\sqrt2\,\vert\mathbf k_T\vert e^{-y_A}\sinh(y_k-y_A)$ for on-shell $k$: the space-like line self-energy is non-integrable ($1/\sinh^2$) | V · R6, c_tmd R4; re-derived by the synthesizer | `lem:tmd-soft-oneloop` |

**S55 — Master table and registry** (FINAL_OUTLINE §08; `master_rows.py`, `check_outline.py`).
- **New rows 69–75** (columns as in §08):

  | # | 结论 | 公式/要点 | 标签 | MA | 规范标签 | 瓶颈假设（Ch22） | 升级路径（Ch22） |
  |---|---|---|---|---|---|---|---|
  | 69 | 由定域 OPE 得到固定 $n$ 的矩（强子） | 无自旋求和；正性＋有限减除色散关系 | [R, $R_{\rm cond}$] | MA0 | `thm:dis-fixed-n` | `asm:intro-np-ope` | 非微扰 OPE |
  | 70 | DIS 矩因子化的非微扰条件定理 | $n\ge n_0$；全部偶数 $n$ 需增长条件 | [R, $R_{\rm cond}$] | MA0、MA3、MA4 | `thm:dis-moments-np` | `asm:intro-np-ope`、`asm:intro-growth` | 构造 QCD；非微扰 OPE |
  | 71 | 减除定理（条件形式） | (CS1)–(CS3) ⇒ 余项积分范数压低 | [R, $R_{\rm cond}$] | — | `thm:appN-subtraction` | `asm:appN-collins` | 变形围道上的一致积分界 |
  | 72 | 单圈离壳三角图的完整减除 | $\int r=-4m^2/Q^4+O(m^4Q^{-6}L^2)$ | [R, R_PT] | — | `prop:appN-triangle-exact` | — | — |
  | 73 | 单举 DY 中 Glauber 区相消（条件定理） | LCOPT；等光锥时刻局域化；沿 $e_G$ 同时形变 | [R, $R_{\rm cond}$] | — | `thm:appO-main` | `asm:appO-mixing`(c)、`asm:appO-deformation`(b)–(d)、`asm:appO-rewritten-cs` | 解除上述假设 |
  | 74 | 程函线间双胶子交换的 $O(g^4)$ 幺正性 | $p_{\rm opp}=-iY/\pi$；Regge 相位 | [R, R_PT] | — | `prop:dy-eikonal-twogluon` | — | 非程函旁观者与全阶 |
  | 75 | 重到轻形状因子：软重叠＋硬旁观者 | $F=C\,\xi_\pi+T\otimes\phi_B\otimes\phi_\pi$ | [A] | MA1、MA2 | `prop:heavy-btopi-ff` | SCET 全阶论证；$\xi_\pi$ 的端点发散 | — |

- **Changed rows.**
  - Row 16 (`thm:dis-ope`): 瓶颈 → `prop:dis-ope-euclid`（D3）、`asm:appM-brst-ope`、`asm:appM-forward`.
  - Row 17 (`thm:dis-moments`): 结论 adds 「$n\ge n_0$；全部偶数 $n$ 需 `asm:intro-growth`」; 瓶颈 → `asm:intro-np-ope`、`asm:intro-growth`.
  - Every row whose 瓶颈 column cites `thm:method-subtraction`, `prop:method-glauber-deformation` or `lem:dy-fsi`: name the `asm:` labels instead.
- `tab:intro-overview` (Ch1) follows; 68 → 75 rows.
- **Registry.**
  - Regenerate after the statements of S13–S53 are entered.
  - Extend the label regex with `asm` (S12).
  - Add a section "Assumptions" (25 entries) to the registry.
  - The registry should report the new count of statements (346 + the new ones of §5) and of examples.

### 5.9 Figures

**S56 — FIGURES_INDEX: new figures** (owners by first use, FIGURES_INDEX CHANGELOG 1). The reference's figure numbers are given only for orientation: redraw, never copy (S62).
- Counts: required 29 → 47 (17 new + `fig:prelim-lightcone` promoted); optional 10 → 14 (5 new, 1 promoted away).

| label | owner (section) | draw | caption draft | ref. fig. |
|---|---|---|---|---|
| `fig:prelim-lightcone` (promoted to required) | Ch2 | two panels: the $(z,t)$ plane with light-cone axes and a boosted hadron band; the $(\ln v^+,\ln v^-)$ plane, where boosts are translations | 「光锥坐标：洛伦兹推动在对数光锥平面上是平移。」 | 3 |
| `fig:ir-mode-exponents` | Ch3 (`sec:ir-power`) | exponent space $(a,b,c)$ of $(k^+,k^-,k_T)\sim(\lambda^a,\lambda^b,\lambda^c)$: H, C$_A$, C$_B$, ultrasoft on the plane $c=\frac{a+b}2$, TMD-soft at the centre, Glauber below the plane | 「模式在指数空间中的位置；Glauber 模式位于在壳平面之下。」 | 10 |
| `fig:ee-cutsum-disc` | Ch5 | left: classes of $O(\alpha_s^2)$ cuts of the two-loop self-energy, poles up to $1/\varepsilon^4$ per class; right: the sum over cuts = discontinuity of the forward function, contour movable at distance $O(Q)$ | 「对割图求和等于前向函数的不连续性；围道可在 $O(Q)$ 处移动。」 | 18–19 |
| `fig:dis-euclid-segment` | Ch6 | $\omega$ plane with the cuts $(-\infty,-1]$, $[1,\infty)$, the unit disc, and the short segment $\mathcal I_Q=\{iy:\vert y\vert\le\sqrt3M/Q\}$; inset: scale line $M/Q$ | 「欧氏 OPE 只在长度 $O(M/Q)$ 的虚轴线段上提供信息；固定 $n$ 的矩需要正性与色散关系。」 | 61–62 |
| `fig:method-hasse` | Ch8 (`sec:method-regions`) | Hasse diagram of the nine leading regions of the two-loop vertex, meet-closed | 「两圈顶点九个领头区域的 Hasse 图（对逐线交封闭）。」 | 63 |
| `fig:method-neighbourhoods` | Ch8 | nested $\lambda$-dependent neighbourhoods $N_R$, $U_R=N_R\setminus\cup_{R'<R}N_{R'}$, exponents $\beta_R$ | 「依赖于 $\lambda$ 的邻域与覆盖。」 | 64 |
| `fig:method-sudakov-plane` | Ch8 | $(\ln k^+,\ln k^-)$ plane: regions as corners, soft–collinear overlap, the on-shell line $k_T^2=2k^+k^-$ | 「Sudakov 平面中的区域与软–共线重叠。」 | 9, 69 |
| `fig:method-coeff-minus-coll` | Ch8 (`ex:method-dis-oneloop`) | one-loop DIS: coefficient function = cut graph minus its collinear approximation (ISR² ↔ ladder; ISR–FSR interference ↔ Wilson-line graphs) | 「系数函数 = 割图减去其共线近似。」 | 29–31 |
| `fig:disall-ladder-regions` | Ch9 | two-rung ladder with the three regions $R_2<R_1<R_H$ and the grouped remainder $r=\Delta\mathsf H_0\Delta K_2\Delta K_1$ | 「两级梯形图的三个区域与分组余项。」 | 24–25, 70(b) |
| `fig:dy-pole-orientation` | Ch11 | a cut DY graph in hybrid light-cone ordering ($x^+$ for $J_A$, $x^-$ for $J_B$); intermediate states before and after $V_H$ with the sign of their $i0$ | 「光锥序中间态的取向决定 $k^-$ 极点所在的半平面。」 | 72–74 (R7) |
| `fig:dy-two-gluon-exchange` | Ch11 | box and crossed box between two eikonal lines; the values of $J_{\rm box}$, $J_{\rm cross}$; ordering weights | 「双胶子交换：全部 $s$ 道权重在非交叉图中，交叉图只贡献 Regge 相位。」 | 77 (corrected) |
| `fig:method-glauber-direction` | Ch8 (`sec:method-glauber`) | three panels: one-component deformation (stays in $G_\delta$); the soft line's own pole; the simultaneous deformation along $e_G$ | 「离开 Glauber 区需要沿 $e_G=n_B-n_A$ 同时形变两个光锥分量。」 | 78 |
| `fig:appM-dependency` | App M | moment theorems ← assumptions, coloured by status | 「DIS 矩定理对编号假设的依赖。」 | 54 |
| `fig:appM-handbag-ab` | App M | the handbag as an AB part vs as a reduced graph | 「手提袋图：AB 部分与约化图。」 | 57 |
| `fig:appO-flowchart` | App O | steps (O-1)…(O-8) with assumptions as dashed boxes | 「Glauber 相消条件证明的结构。」 | 71 |
| `fig:appO-lcopt-term` | App O | one LCOPT term: energy denominators, instantaneous lines, $V_H$ at $\tau=0$ | 「一个光锥序项。」 | 74 (R7) |
| `fig:appO-cutsum` | App O | the cut-position identity with insertions; closed-time-path picture | 「割线位置恒等式与闭时路形式。」 | 75 (R7) |
| `fig:appP-dependency` | App P | generated dependency graph | (generated) | — |
| `fig:dis-twist-graphical` (optional) | Ch6 | twist ↔ extra partons ($\lambda$ per transverse gluon, $\lambda^2$ per quark pair) | 「扭度与额外部分子。」 | 21 |
| `fig:appE-boost` (optional) | App E | the boost-and-dimension argument | 「推动与量纲给出幂次。」 | 11 |
| `fig:tmd-rapidity-bars` (optional) | Ch13 | rapidity coverage $y_B<y_{P_B}<y_n<y_{P_A}<y_A$ of $\tilde f^{\rm unsub}$, $\tilde S$ and the split at $y_n$ | 「快度覆盖与平方根构造。」 | 67 |
| `fig:appO-glauber-flow` (optional) | App O | Glauber flows and graded configurations | 「分级构型。」 | — |
| `fig:break-measurement` (optional) | Ch17 | measurement operators that commute ($1$, $e^{i\mathbf b\cdot\hat{\mathbf P}_T}$) or not ($\Pi_h$, $\Pi_{\rm gap}$) with the light-cone evolution | 「测量相容性判据。」 | — |

### 5.10 WRITER_SPEC rules

**S57 — Honesty checklist: new misconceptions M29–M35** (WRITER_SPEC §6.6). REVIEW.md is frozen, so the texts are given here; copy them into WRITER_SPEC §6.6 as a footnote table.

| M# | misconception (中文) | correct statement | chapter |
|---|---|---|---|
| M29 | 「欧氏区没有钳夹，所以欧氏 Green 函数红外有限」 | zero-momentum massless lines always solve the Landau equations; finiteness follows from IR power counting | Ch3 (`rem:ir-euclid-corners`) |
| M30 | 「NNLO/N3LO 的 DY 与数据一致，说明 Glauber 相消已被检验」 | partonic fixed-order results contain no hadron spectators; they test active-parton contributions only | Ch11 (`rem:dy-nnlo-not-glauber`) |
| M31 | 「把 $k^-$ 围道推到 $\vert k^-\vert\sim\vert k_T\vert$ 就离开了 Glauber 区」 | a one-component deformation stays in $G_\delta$; both components must move along $e_G$ | Ch8 (`rem:method-two-component`), Ch11 |
| M32 | 「非阿贝尔双 Glauber 交换留下非幺正残差」 | an artefact of the strict truncation; the exact graphs give ${\rm Re}\,p_{\rm opp}=0$ | Ch11 (`prop:dy-eikonal-twogluon`) |
| M33 | 「单个割图中的软 Wilson 线已经是过去指向的」 | a single cut graph gives the future-pointing line; past-pointing only after the one-sided rewriting | Ch11, Ch13 (`ex:dy-future-vs-past`) |
| M34 | 「欧氏 OPE 代入、收缩、比较系数即得强子结构函数的矩」 | the OPE informs only on a segment of length $O(M/Q)$; positivity and a dispersion relation are needed; $n<n_0$ needs growth | Ch6 (`thm:dis-fixed-n`) |
| M35 | 「减除定理可以逐项归纳证明」 | single chain terms need not be integrable; only grouped expressions are suppressed | Ch8 (`ex:method-naive-induction`) |

Add them to the allocation table (rows 3, 6, 8, 11, 13). The Ch1 misconception box may include M32 and M35.

**S58 — Over-claims to avoid** (WRITER_SPEC §6.7; append).
- 「欧氏区无 Landau 奇点」 (M29; ERR-M1).
- 「非阿贝尔双 Glauber 残差是 DY 因子化的开放障碍」 (M32; ERR-S1).
- 「纯规范论证证明了非阿贝尔 Wilson 线结构」 (ERR-M6). It is a heuristic whose step 2 is the [A] Ward identity.
- 「NRQCD 衰变因子化与 OPE 同样严格」 (ERR-M9).
- 「间隙截面的因子化已被证明破坏」. Amplitude-level violation is [V]; PDF factorization of gap cross sections is [C], with restoration evidence (ERR-M23).
- 「NQS 的规范完备 Wilson 线在 NNLO 不改变结果」 (ERR-M19).
- 「Gaunt (2014) 证明了强子 $E_T$ 的因子化破坏」 without Schwartz–Yan–Zhu (ERR-M30).
- 「DGLAP 与 OPE 重整化群在所有阶以单一核等价」 (ERR-M10).
- 「横向光子失效源于 $\int\phi/z^2$ 型发散」 (ERR-M17).
- 「BBNS 只在 $O(\alpha_s)$ 成立」. This understates; the LP formula is [P] with all-order arguments (ERR-M21).
- 「前向在壳部分子矩阵元直接给出 Wilson 系数，无需额外步骤」 (ERR-M24, OUR-8).
- 「Glauber 相消的方法是 Collins (2011) 首创的光锥序处理」. Credit Aybat–Sterman 2009 (ERR-M32).

**S59 — 「本书新结果」** (WRITER_SPEC §6.5, amended). Replace "No new results" by the following.
- 「不得加入大纲以外的定理（证明所需的辅助引理除外，标 `lem:<key>-…` 并报告）。」
- 「大纲中标注『本书新结果（待文献核查）』的陈述可以印出，但须满足以下条件。」
  1. A full derivation in the text.
  2. A script check stored under `research/` or `refdoc/work_*` and cited in the final report.
  3. A literature check by the refs agent. If a prior source is found, cite it and drop the marker.
- Current list: `prop:dy-eikonal-twogluon`.
- Sharpened explicit results, not marked new: `prop:appN-triangle-exact`(c), `lem:appO-joint-localization` (the reference's own analysis made a lemma), `lem:appJ-cut-hermiticity` (standard).

**S60 — Bibliography additions** (refs agent; verify every detail; none of these keys exists in `refs_merged.bib` at 15:20).
- **Regge / eikonal (S37):**
  - Cheng–Wu 1969 (high-energy elastic scattering in QED);
  - Korchemskaya–Korchemsky, Nucl. Phys. B 437 (1995) 127, and Korchemsky, Phys. Lett. B 325 (1994) 459;
  - Caron-Huot, "When does the gluon reggeize?", arXiv:1309.6521.
- **OPE (App M):**
  - Hamberg–van Neerven, Nucl. Phys. B 379 (1992) 143;
  - Falcioni–Herzog 2022 and Gehrmann–von Manteuffel–Yang 2023 (gauge-variant operators in covariant gauge);
  - Bostelmann 2005 (AQFT OPE).
- **LCOPT (App O):**
  - Kogut–Soper 1970;
  - Chang–Yan 1973;
  - Ligterink–Bakker 1995;
  - Brodsky–Pauli–Pinsky, Phys. Rep. 301 (1998) 299;
  - Collins arXiv:1801.03960 (LF vacuum).
- **DFT:** Andrási et al. 1981; Di'Lieto et al. 1981.
- **TMD:** Collins–Gamberg–Prokudin–Rogers–Sato–Wang, Phys. Rev. D 94 (2016) 034014.
- **Heavy:** Chay–Kim 2004 ($B\to\pi\pi$ in SCET).
- **Power:**
  - Beneke–Braun–Kivel 1998 (O($N$) σ-model);
  - David 1982–86 and Novikov–Shifman–Vainshtein–Zakharov 1984 (σ-model);
  - Feldman–Magnen–Rivasseau–Sénéor 1986 (Gross–Neveu).
- **Already present (checked by the synthesizer):**
  - OPE and renormalization: `Joglekar:1975nu`, `Joglekar:1976eb`, `Joglekar:1976pe`, `Hollands:2007zg`, `Anikin:1978tj`, `Zavyalov:1990kv`, `Collins:1994ee`, `Breitenlohner:1975hg`, `Breitenlohner:1976te`, `Smirnov:1990rz`, `Smirnov2002`, `LowensteinZimmermann1975`;
  - exclusive: `Mankiewicz:1999tt`, `Diehl:1998pd`, `CollinsDiehl2000`;
  - heavy quarks and SCET: `Bauer:2002aj`, `Beneke:2003pa`, `Bauer:2004tj`, `BenekeEtAl2000`, `Chay:2004zn`, `Kang:2011mg`, `Fleming:2012wy`;
  - Glauber and breakdown: `AybatSterman2009`, `Diehl:2015bca`, `RothsteinStewart2016`, `Gaunt2014`, `Schwartz:2018obd`, `Zeng:2015iba`, `Becher:2024kmk`, `DoriaFrenkelTaylor1980`, `Frenkel:1983di`, `Catani:1985xt`, `Basu:1984ba`;
  - integrals: `UsyukinaDavydychev1993a`.

### 5.11 Process

**S61 — Writer order and critical path.**
1. The lead author decides on S1–S8 (structure, tags, register). Then the new statements of S13–S53 are entered into FINAL_OUTLINE, and the registry is regenerated (S55).
2. **App N first.** Ch8, Ch9, Ch13 and Ch18 cite its labels. Recommended: the App N writer also writes `sec:method-subtraction` of Ch8.
3. **App O after the App N labels of §N.3–§N.5 are frozen.** Recommended: the same writer writes Ch11 `sec:dy-glauber`, `sec:dy-model` and `sec:dy-theorem`.
4. **App M is independent.** Recommended: the Ch6 writer, or a dedicated writer with the Ch6 statements frozen first.
5. Ch1 and Ch22 last (they also wait for FINAL_OUTLINE §0.9 items 1–2). App P is generated at integration.
6. **Critical path:** FINAL_OUTLINE update → App N → App O → Ch11/Ch13/Ch17 → Ch22 → App P.
7. If Part VII (frontier) is adopted, its assumptions enter the same register (e.g. `asm:lamet-*`), and App P becomes App S or later. The appendix letters M–O are unaffected.

**S62 — The reference document** (WRITER_SPEC §8 and §11).
- `factorization_qcd-2.pdf` is an unpublished text of unknown authorship. It is **not cited, not quoted, and its figures are not copied**.
- Every adopted construction is re-derived in our conventions and attributed to the primary literature (Collins 2011; Collins–Soper–Sterman; Aybat–Sterman; Zimmermann; Joglekar–Lee; …) or presented as our own derivation.
- Formulas taken from the reader notes must be checked against the page images (`refdoc/work_R*/p130-*.png` and the like), not against `pdftotext` output, which detaches minus signs.
- The reference's numbering (Thm C.50, Ass. E.33, …) never appears in our text.

**S63 — Open verification items** (refs agent or verify agent; each blocks only the sentence it supports).
1. Scope of the cited graph-by-graph Euclidean expansion theorems for QCD with quarks, ghosts and gauge-variant operators (`prop:dis-ope-euclid` upgrade path).
2. Anikin–Zav'yalov 1978 and Zav'yalov 1990: can `asm:appM-remainder` be discharged via uniqueness?
3. Joglekar 1977 I+II and Hollands 2008: which parts of `asm:appM-brst-ope` they cover.
4. Hamberg–van Neerven 1992, Falcioni–Herzog 2022, Gehrmann–von Manteuffel–Yang 2023: the forward on-shell alien-operator issue.
5. Literature check of `prop:dy-eikonal-twogluon` (S37, S59).
6. CGPRSW 2016: the $W+Y$ uniformity statement (Ch13).
7. $p=2$ in `prop:tmd-small-b`.
8. The ghost-conjugation convention of `lem:appJ-cut-hermiticity` against `prop:appJ-ghost-cuts`.
9. Equation numbers quoted from RS 2016 ((9.1), (9.18), (9.19), via c_glauber) and Collins 2011 ((11.6) with errata; ch. 12 for the FF).
10. Becher et al. 2025 (`Becher:2024kmk`): the exact form of the restoration evidence.
11. Beneke–Braun–Kivel 1998, Feldman–Magnen–Rivasseau–Sénéor 1986, Bostelmann 2005, Chay–Kim 2004: keys and contents.
12. Collins 2011 ch. 10: whether the Sudakov form-factor treatment establishes integral-norm bounds or scaling statements only. This affects the wording of `thm:method-subtraction`'s status and of open problem 3.
