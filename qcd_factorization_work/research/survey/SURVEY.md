# Rigor-status survey of QCD factorization — with literature verification

Research-phase deliverable for the monograph "QCD 因子化定理：严格证明、全阶论证与适用边界".
Directory: `research/survey/`. Date of the literature check: 2026-10-09.

Companion files (same directory):

| file | content |
|---|---|
| `survey_refs.bib` | 415 BibTeX entries: 412 records downloaded from INSPIRE-HEP after checking them by journal reference or arXiv number, plus 3 manual entries (checked against Crossref or the web; marked as manual in the file). |
| `verified_refs_table.tsv` | label → INSPIRE texkey → journal/arXiv/DOI, for every INSPIRE entry. |
| `inspire_raw/*.json` | raw INSPIRE API responses (abstracts included), one per query label. |
| `master_table_zh.tex`, `test_master_table.tex`, `test_master_table.pdf`, `preamble_fact.tex` (copy of `common/`) | Chinese LaTeX version of the master table: four floats (items 1–6, 7–10, 11–20, 21–30), using `\tagR`…`\tagV` and `\cite{texkey}`. Test-compiled with XeLaTeX + BibTeX (`unsrt`) against `survey_refs.bib`, which also checks that the .bib processes cleanly (no errors; only 4 "empty journal" warnings for arXiv-only entries). |
| `checks/lo_moments_check.py` | sympy check of the LO splitting-function Mellin moments and sum rules quoted in item 2. |

Citations below use INSPIRE texkeys (e.g. `[Collins:2011zzd]`), and every key is in `survey_refs.bib`.

---

## 0. Method, legend, and conventions

### 0.1 How each claim was checked

* **Bibliography.** Each reference was queried on INSPIRE-HEP by journal reference (e.g. `j Phys.Rev.D,31,2616`) or arXiv number. Title, authors, journal, volume, page, year and errata were compared with the citation, then the BibTeX was downloaded by record id. Three items not in INSPIRE (Hahn–Zimmermann 1968, Pham 2011, Zimmermann's 1970 Brandeis lectures) were checked against Crossref or the web.
* **Content.** Each content claim carries one of these markers:
  * **[txt §…]**: read in the full text, with the location given. Full texts read: Collins, *Foundations of perturbative QCD* (Open Access PDF from Cambridge Core); Collins, *Renormalization* (Open Access PDF); and the arXiv versions of BBL 1995, the CSS 1989 review, Collins 1998 (diffraction), Rothstein–Stewart 2016, the TMD Handbook 2023, Diehl–Gaunt 2018, IJJSZ 2018, BBNS 2000, CdFR 2012, CFGH 2023, Aybat–Sterman 2009, DGOPS 2016, Collins 2020 (Landau), CDF Run II 2012, BVZ 2019, Bury–Prokudin–Vladimirov 2021, STAR 2016 and Feige–Schwartz 2014.
  * **[abs]**: checked against the INSPIRE abstract.
  * **[bib]**: only the bibliographic record was checked; the content statement comes from general knowledge.
* Anything I could not verify is marked **UNVERIFIED**.

### 0.2 Rigor tags (binding definitions from CONTEXT.md)

| tag | macro | meaning |
|---|---|---|
| **[R]** | `\tagR` 严格 | complete mathematical proof at every order of renormalized perturbation theory (PT) |
| **[A]** | `\tagA` 全阶论证 | standard all-order PT argument accepted in the literature; some steps exist only as sketches |
| **[P]** | `\tagP` 部分 | proven or verified only at fixed order, in a model, or for a subclass |
| **[C]** | `\tagC` 猜想 | widely used but unproven, or the known proof has a gap |
| **[V]** | `\tagV` 破坏 | known to fail (explicit counterexample or proof) |

Read strictly, the [R] definition fits very few QCD statements. I give a single tag per item, but where the item contains sub-statements of different status I list the sub-tags in the notes.

### 0.3 Convention hazards for transcription (verified)

1. **Sign of g.** Collins (2011) uses $D_\mu=\partial_\mu+ig\,t^\alpha A^\alpha_\mu$ ([txt eq. (2.2)] of [Collins:2011zzd]), so his Wilson lines are $P\exp(-ig\int n\cdot A)$ (e.g. his eq. (13.40)). The project uses $D_\mu=\partial_\mu-igA_\mu$ with $W=P\exp(+ig\int dz\cdot A)$. When transcribing eikonal Feynman rules or Wilson-line formulas from Collins, flip $g\to-g$. Physical results are unchanged.
2. **Sign of the TMD Fourier transform.** Collins defines $\tilde S(b_T)=\int d^{2-2\epsilon}k_T\,e^{+ik_T\cdot b_T}S(k_T)$ and likewise for TMD fragmentation functions ([txt eq. (13.35)]; he notes the normalization also differs from Collins–Soper 1982). The project uses $e^{-ik_T\cdot b_T}$. Azimuthally symmetric functions are unaffected, but b-space T-odd functions (Sivers, Boer–Mulders) and the inverse transform $e^{\mp iq_T\cdot b_T}$ in the factorization formula change sign. Fix one convention before transcribing.
3. **Plus distributions in $P_{gg}$.** In $P_{gg}$, "$z/(1-z)_+$" means $z\,[1/(1-z)]_+$. Since $[z/(1-z)]_+=z[1/(1-z)]_+ +\delta(1-z)$, misreading it shifts the $\delta(1-z)$ coefficient by $2C_A$ and violates the momentum sum rule (checked in `checks/lo_moments_check.py`).

---

## 1. Master table

**Legend:** PT = perturbation theory; LP = leading power; NLP = next-to-leading power. In the "Level" column, "all orders" means all orders in α_s at leading power unless stated otherwise.

| # | Topic | What is established | By whom / where (verified) | Level | Tag | Main gap / counterexample |
|---|---|---|---|---|---|---|
| 1 | Wilson OPE; light-cone OPE | Short-distance OPE of Green functions (asymptotic; convergent at each loop order in φ⁴). The OPE closes on gauge-invariant operators in pure Yang–Mills. Light-cone expansion of current products. | Zimmermann 1970/1973 (scalar); Hollands–Kopper 2012; Holland–Hollands–Kopper 2016; Hollands 2008 (YM); Joglekar–Lee 1976, Joglekar 1977; Collins 1984 ch. 10, §12.8; Brandt–Preparata 1971, Frishman 1971, CHM 1972, Anikin–Zav'yalov 1978 | all orders in PT | **[A]** (sub: [R] for φ⁴ and pure YM; [C] beyond PT) | For QCD with quarks the proof is asserted "the same way" (Collins 1984 §12.8); IJJSZ 2018: "proven for scalar field theory… widely assumed" for QCD. Not valid beyond PT (renormalons). |
| 2 | DIS moments; DGLAP | $M_N(Q^2)=\sum_i C_{N,i}A_{N,i}+O(\Lambda^2/Q^2)$; RG evolution; DGLAP for operator-defined $\overline{\rm MS}$ PDFs; anomalous dimensions $\gamma_N=\int z^{N-1}P(z)$. Explicit kernels to 3 loops. | Gross–Wilczek 1973–74; Georgi–Politzer 1974; Gribov–Lipatov 1972; Altarelli–Parisi 1977; Dokshitzer 1977; Collins–Soper 1982; Moch–Vermaseren–Vogt 2004 | all orders in PT (structure); kernels to fixed order | **[R]** (moments: [R] modulo item 1; kernels [R] at each computed order) | Moment-wise $O(1/Q^2)$ bounds do not give uniform-in-$x$ control. Parton-language derivations (AP, LLA) are heuristic. |
| 3 | IR finiteness | $R_{e^+e^-}$ finite order by order; Euclidean Green functions at non-exceptional momenta are IR finite in massless renormalizable theories; IR-safe jet cross sections finite. | Poggio–Quinn 1976; Lowenstein–Zimmermann 1975; Lowenstein 1976; Breitenlohner–Maison 1977; Fröb–Holland–Hollands 2016 (YM); Sterman 1976, 1978, 1979; KLN 1962/64 | all orders in PT | **[R]** total σ and Euclidean; **[A]** jets | Bloch–Nordsieck **[V]** with coloured initial states (Doria–Frenkel–Taylor 1980; Di'Lieto et al. 1981): uncancelled terms are power-suppressed. KLN needs initial-state sums plus forward scattering (Frye et al. 2019). |
| 4 | Landau equations; Coleman–Norton | Necessary (and, for physical-region pinches, sufficient) conditions for pinch singularities; classical-process interpretation. | Landau 1959; Coleman–Norton 1965; ELOP 1966; Pham 2011; Collins 2020 (arXiv); Mühlbauer 2020 (arXiv) | per graph, all orders | **[A]** | Collins 2011 §5.4.3: no published complete proof; textbook proofs incomplete. Collins 2020 gives a complete proof, but it is a preprint (no journal record found on INSPIRE). |
| 5 | Power counting; leading regions | Power law $Q^p(\lambda/Q)^{\alpha(R)}(\lambda_S/Q)^{\beta(R)}\cdots$; catalogue of leading regions; Glauber pinch criteria. | Sterman 1978; Libby–Sterman 1978a,b; Collins 2011 ch. 5 (eqs. 5.75–5.79, §5.9); Gardi et al. 2022 | all orders | **[A]** | Leading regions incomplete in Feynman gauge: extra disconnected hard scatterings, cancelled after a sum over graphs (Labastida–Sterman 1985; Collins §14.4.8). Overlapping regions need subtractions (§5.10). |
| 6 | DIS collinear factorization (graph methods) | $F=\sum_i C_i\otimes f_i+O((\Lambda/Q)^a)$ in $x$-space with gauge-invariant PDFs. | EGMPR 1978/79; APV 1978; Libby–Sterman 1978; Mueller 1978 (cut vertices); CFP 1980; CSS 1989; Collins 2011 §8.9 (non-gauge: complete), ch. 10–11 (QCD); Collins 1998 (masses) | all orders, LP | **[A]** | Collins §11.3.2: the BRST classification of non-local operators "no proof has been given… I will assume the result is true". Naive K-gluon Ward identity has a non-zero leading remainder (Collins–Rogers 2008). |
| 7 | Operator PDFs/FFs; support; positivity | Gauge-invariant definitions; renormalization; support $\lvert\xi\rvert\le1$, $f_{q}(-\xi)=-f_{\bar q}(\xi)$; number-density interpretation (bare). | Collins–Soper 1982; Jaffe 1983; Diehl–Gousset 1998 (GPDs); Collins 2011 §6.3, §6.7, §6.9, §7.5–7.6 | definitions; PT; non-perturbative spectral arguments | **[R]** definitions, renormalization, support (PT); **[C]** $\overline{\rm MS}$ positivity | Positivity disputed: Candido–Forte–Hekhorn 2020 (positive) vs Collins–Rogers–Sato 2022 (proof fails; negative at low scales) vs Candido–Forte–Giani–Hekhorn 2024 (positive above a scale, roughly $Q^2\gtrsim5$ GeV², semi-quantitative). |
| 8 | Drell–Yan collinear factorization; Glauber cancellation | Inclusive DY at LP: $d\sigma=\sum f\otimes f\otimes\hat\sigma$; spectator Glauber exchanges cancel after the sum over cuts and contour deformation. | Bodwin 1985 (+ erratum 1986); CSS 1985, 1988; LRS 1982–83 (2-loop); Brandt–Frenkel–Taylor 1989; Collins 2011 §14.3–14.4; DGOPS 2016; Aybat–Sterman 2009 | all orders, LP | **[A]** | Collins §14.4.8 "Issues remaining". Rothstein–Stewart 2016: a full SCET proof "will be given elsewhere" (not found as of 2026-10). Fails for jet-veto, beam-thrust or $E_T$ observables (Gaunt 2014; Zeng 2015). Factorization holds at $1/Q^2$ but fails at $m^4/s^2$ (BRS 1984; CSS 1989 §10.2). |
| 9 | Single-inclusive hadron/jet and heavy-quark production in hadron collisions | Collinear factorization with fragmentation functions or jet functions is assumed in phenomenology. | Arguments: CSS 1989; Nayak–Qiu–Sterman 2005; Aybat–Sterman 2009 | argued | **[C]** | Collins §14.7: "relative lack of detailed proofs". DGOPS 2016: Glauber cancellation not proven for coloured final states. CSS 1986: heavy-quark case is a "conjecture". CdFR 2012: possible N3LO issue. |
| 10 | TMD factorization (DY, SIDIS, $e^+e^-$) | b-space factorization with soft-factor-subtracted TMDs; Collins–Soper and RG evolution; small-$b$ OPE onto collinear PDFs. | Collins–Soper 1981; CSS 1985; JMY 2004–05; Collins 2011 ch. 13, §14.4.5, §14.5; Becher–Neubert 2011; EIS 2012; CJNR 2012; Collins–Rogers 2017; TMD Handbook 2023 | all orders, LP in $q_T/Q$ | **[A]** | DY relies on the Glauber argument (item 8). The SCET derivations drop the Glauber Lagrangian after arguments. Equivalence of rapidity schemes was shown order by order (Collins–Rogers 2017). |
| 11 | Sivers sign change | $f_{1T}^{\perp}\vert_{\rm DY}=-f_{1T}^{\perp}\vert_{\rm SIDIS}$ | Collins 2002 (correcting Collins 1993); BHS 2002; Ji–Yuan 2002; BJY 2003; Collins 2011 §13.17 | exact consequence of T, P and the operator definitions | **[R]** given TMD factorization | Experiment: consistent (COMPASS 2017, 2024; STAR 2016) but not decisive. Bury–Prokudin–Vladimirov 2021 fits "cannot exclude the same sign". |
| 12 | TMD factorization breaking in $h_1h_2\to h_3h_4X$ | Standard and generalized TMD factorization fail. | Collins–Qiu 2007; Collins 2007 (2-gluon, unpublished preprint); Rogers–Mulders 2010; Vogelsang–Yuan 2007 | explicit counterexamples in models | **[V]** | Counterexamples use simplified or spectator models with abelian or non-abelian gluons. |
| 13 | Space-like collinear factorization; SLLs; Glauber EFT | Strict collinear factorization fails for space-like limits beyond tree level; super-leading logarithms exist; Glauber operator EFT. | CdFR 2012; FSS 2012; FKS 2006, 2008; Becher–Neubert–Shao 2021; BNSS 2023; Becher et al. 2025; Banfi–Forshaw–Holguin 2026; Rothstein–Stewart 2016 | explicit 1–3 loop results; LL resummations | **[V]** (strict collinear factorization); **[C]** (mass-singularity factorization beyond NNLO) | Becher et al. 2025: 3-loop active–active Glauber terms restore consistency with PDF factorization below the veto scale. |
| 14 | Diffractive factorization | DDIS (and target-fragmentation-conditioned DIS) factorizes; hadron–hadron hard diffraction does not. | Collins 1998; Berera–Soper 1994–96; Trentadue–Veneziano 1994; CDF 1997, 2000 (Run II recap 2012); ACTW 1999; H1 2007; ZEUS 2008 | all orders (DDIS) | **[A]** DDIS; **[V]** pp̄ (and resolved photoproduction) | CDF: diffractive structure function suppressed by $O(10)$ versus HERA DPDFs. H1 photoproduction: factor ≈0.5. |
| 15 | Double parton scattering | Double DY: Glauber cancellation to all orders (collinear and TMD); double counting solved; soft-gluon decoupling; dPDF sum rules. | Diehl–Ostermeier–Schäfer 2012; DGOPS 2016; DGS 2017; Diehl–Nagar 2019; Diehl–Plößl–Schäfer 2019; Manohar–Waalewijn 2012; BDFS 2012 | all orders, colourless final states | **[A]** double DY; **[C]** coloured final states | Diehl–Gaunt 2018 open issues: S-matrix evolution and positivity. MPI-sensitive observables violate standard factorization (Gaunt 2014). |
| 16 | Hard exclusive processes | Pion form factor at LP; DVCS; longitudinal-photon meson production; endpoint failure for transverse photons. | LB 1979/80; ER 1980; DM 1980; CZ 1977/84; CFS 1997; Ji 1997; Radyushkin 1996/97; Ji–Osborne 1998; Collins–Freund 1999; Mankiewicz–Piller 2000; Li–Sterman 1992 | all orders, LP | **[A]** ($F_\pi$, DVCS, $\gamma^*_L$ mesons); **[V]** $\gamma^*_T$ | Endpoint and soft-overlap dominance at accessible $Q^2$ (Isgur–Llewellyn Smith 1984/89). The Sudakov/$k_T$ approach is a model. |
| 17 | SCET factorization proofs | Operator-level soft–collinear decoupling; B→Dπ to all orders; DIS/DY/DVCS rederived; dijet/thrust $H\,J\otimes J\otimes S$; zero-bin. | BFL 2000; BFPS 2001; BS 2001; BPS 2001, 2002; BFPRS 2002; BCDF 2002; Beneke–Feldmann 2003; Manohar–Stewart 2007; Becher–Schwartz 2008; BFLS 2008; Feige–Schwartz 2014 | all orders, LP | **[A]** | Assumes completeness of modes and absence or cancellation of Glauber modes. Collins 2011 §15.9 could not "penetrate the SCET literature". |
| 18 | QCD factorization for charmless B decays (BBNS) | LP factorization at $O(\alpha_s)$, with explicit 2-loop (NNLO) amplitudes; B→Dπ heavy–light proven at 2 loops. | BBNS 1999–2001; Beneke–Neubert 2003; Beneke–Jäger 2006–07; Bell 2008/09; BHL 2010; BBHL 2015/2020; BPRS 2004 | fixed order (1–2 loops), LP | **[P]** | BBNS 2000: "does not accomplish an all-order 'proof'". Power corrections (annihilation, twist-3 spectator) are endpoint divergent. No endpoint refactorization for B→ππ found. |
| 19 | NRQCD factorization | Decays: $\Gamma=\sum_n 2\,{\rm Im}f_n\langle O_n\rangle/M^{d_n-4}$. Production: $\sigma=\sum_n F_n\langle O_n^H\rangle/M^{d_n-4}$. | BBL 1995 (+ erratum 1997); NQS 2005a,b, 2006 | decays: all orders in α_s at each order in v; production: NNLO checks | **[A]** decays; **[C]** production (**[P]**: NNLO with gauge-completed operators) | Octet production operators need Wilson lines. Possible extra non-local operators at higher orders (NQS 2005). Universality and polarization tensions (Butenschoen–Kniehl 2011–12). |
| 20 | Small-$x$: $k_T$ factorization, BFKL, BK/JIMWLK | High-energy factorization at LL in $\ln1/x$; BFKL at LL and NLL; BK/JIMWLK at LL (+NLO BK). | CCH 1990/91; Collins–Ellis 1991; LRSS 1991; KLF 1975–77; BL 1978; Fadin–Lipatov 1998; Ciafaloni–Camici 1998; Balitsky 1996; Kovchegov 1999; JIMWLK 1997–2002; Balitsky–Chirilli 2008 | leading-log approximations | **[P]** ($k_T$ factorization); **[A]** within LL/NLL; **[C]** saturation | Unintegrated gluon distributions are process dependent (Dominguez–Marquet–Xiao–Yuan 2011). Not a theorem with controlled power corrections. |
| 21 | Higher twist and twist-3 | DIS twist-4 via OPE; twist-4 DY at $1/Q^2$ (generalized factorization); twist-3 SSAs (ETQS). | EFP 1982/83; Jaffe–Soldate 1982; Jaffe 1983; Qiu 1990; Qiu–Sterman 1991a,b, 1991, 1992, 1999; Efremov–Teryaev 1982/85; Vogelsang–Yuan 2009; BMP 2009 | DIS: all orders (OPE); twist-3: one loop | DIS **[R]** (moments, modulo item 1); hadronic $1/Q^2$ **[A]**; twist-3 **[P]**; beyond $1/Q^2$ in hadron–hadron **[V]** | Renormalon mixing with leading twist. Twist-3 evolution once disputed (BMP 2009 versus Kang–Qiu 2009). Sivers "sign mismatch" (2011) addressed by JAM 2020. |
| 22 | Renormalons | IR renormalons correspond to power corrections; factorial divergence. | 't Hooft 1977; David 1984/86; Mueller 1985; NSVZ 1985; Beneke 1999; Beneke–Braun 1994; BSUV 1994; Bali–Bauer–Pineda 2014 | large-β₀ exact; general: argued | **[A]** (large-β₀ statements [R] in that approximation); **[C]** non-perturbative OPE | No non-perturbative definition of the OPE in QCD. |
| 23 | Method of regions | Euclidean asymptotic expansions (large momenta and masses) rigorous; threshold, on-shell and Glauber expansions in Minkowski space conjectured, proven in special cases. | Smirnov 1990, 2002; Beneke–Smirnov 1998; Jantzen 2011; Pak–Smirnov 2011; JSS 2012; SSS 2019; Gardi et al. 2022 | general | **[R]** Euclidean; **[P]** Minkowski | SSS 2019: "make a conjecture… prove this conjecture in some partial cases". |
| 24 | LaMET and pseudo-PDF factorization | Matching of quasi-PDFs and pseudo-ITDs to light-cone PDFs; multiplicative renormalizability of Wilson-line quark bilinears to all orders. | Ji 2013/2014; IJJSZ 2018; Radyushkin 2017/18; Ma–Qiu 2014/2018; Ishikawa–Ma–Qiu–Yoshida 2017; Ji–Zhang–Zhao 2018 | all orders in PT (via OPE) | **[A]** | Relies on the space-like OPE in QCD (item 1). Power corrections scale as $\Lambda^2/(x^2(1-x)P_z^2)$ (BVZ 2019). Rossi–Testa 2017/18 criticism. |
| 25 | Threshold resummation; refactorization | LP threshold factorization $\hat\sigma\to H\cdot S(\cdots)\otimes J$ and exponentiation in Mellin space; NLP at LL. | Sterman 1987; Catani–Trentadue 1989/91; Korchemsky–Marchesini 1993; CLS 1997; Kidonakis–Sterman 1997; Becher–Neubert(–Pecjak/Xu) 2006–08; Beneke et al. 2019–22 | all orders, LP; NLP LL | **[A]** LP; **[P]** NLP | NLP endpoint divergences, resolved case by case. |
| 26 | Non-global logarithms | NGLs from $O(\alpha_s^2)$; BMS equation (large $N_c$); finite-$N_c$ evolution; EFT factorization. | Dasgupta–Salam 2001/02; BMS 2002; Weigert 2004; Hatta–Ueda 2013; Caron-Huot 2018; BNRS 2016 | fixed order: exact; resummation: LL | **[R]** existence (explicit); **[A]** LL large-$N_c$; **[P]** beyond | At hadron colliders, Glauber phases give SLLs (item 13). |
| 27 | Heavy-quark schemes in DIS | Factorization with heavy-quark masses kept: remainder uniformly $O(\Lambda/Q)$; schemes ACOT, S-ACOT, TR, BMSN, FONLL. | CWZ 1978; AOT/ACOT 1994; Collins 1998; Krämer–Olness–Soper 2000; Thorne–Roberts 1998; BMSN 1998; FLNR 2010 | all orders (Collins 1998) | **[A]** | The schemes are prescriptions that are equivalent to the order computed. |
| 28 | Photoproduction; resolved photons | $F_2^\gamma$ (point-like part) from the OPE; direct photoproduction behaves like DIS; resolved photoproduction behaves like hadron–hadron; photon PDF of the proton from structure functions. | Witten 1977; Bardeen–Buras 1979; Klasen 2002; Collins 1998; H1 2007; Klasen–Kramer 2008; LUXqed 2016/17 | various | **[A]** direct; **[C]** resolved; **[V]** diffractive resolved | Separating direct from resolved contributions is ambiguous beyond LO (Collins 1998 conclusions). |
| 29 | Nuclear PDFs; factorization in nuclei | eA DIS as DIS; pA DY as DY with nuclear-enhanced $A^{1/3}/Q^2$ twist-4 terms; nPDF fits assume leading-twist factorization. | Qiu–Sterman 1991; Luo–Qiu–Sterman 1994; Guo 1998; BBL 1981/89; FGS 2012; EPPS21; nCTEQ15; nNNPDF3.0 | inherits items 2, 6, 8 | **[A]** (eA: as DIS; pA: as DY) | BBL: factorization requires energy ≫ a scale growing with target length. Saturation at small $x$ in large nuclei. |
| 30 | Other essentials | $e^+e^-\to hX$ (FFs); Sudakov form factor; IR structure of amplitudes (dipole formula exact to 2 loops, corrected at 3 loops); amplitude-level factorization; colour-singlet production in hadron collisions. | Collins–Soper 1982; Mueller 1978; Collins 2011 ch. 10, 12; Mueller 1979; Collins 1980; Sen 1981; Magnea–Sterman 1990; Catani 1998; Becher–Neubert 2009; Gardi–Magnea 2009; Almelid–Duhr–Gardi 2016; Feige–Schwartz 2014 | all orders | **[A]** | The dipole formula as an exact all-order statement fails at 3 loops [V]: non-dipole terms from 3 coloured legs (constant), kinematic from ≥4. Feige–Schwartz exclude initial–final collinear configurations. |

---

## 2. Detailed notes, item by item

Notation follows CONTEXT.md: metric $(+,-,-,-)$, light-front $v^\pm=(v^0\pm v^3)/\sqrt2$, $D_\mu=\partial_\mu-igA_\mu$, $\overline{\rm MS}$, $D=4-2\epsilon$, and DGLAP $\partial f/\partial\ln\mu^2=(\alpha_s/2\pi)P\otimes f$.

### Item 1 — Wilson OPE and light-cone OPE in renormalized PT

**Statements.** (a) *Short-distance OPE.* For local operators $A,B$ and "spectator" fields $X$ at fixed separation,
$$\langle A(x)B(0)X\rangle=\sum_{n:\,d_n\le\Delta}C_n(x;\mu)\,\langle O_n(0;\mu)X\rangle+R_\Delta(x),\qquad C_n\sim|x|^{d_n-d_A-d_B}\times(\text{logs}),$$
for operators of (canonical) dimension $d_n\le\Delta$. The remainder obeys $R_\Delta=O(|x|^{\Delta'-d_A-d_B}\times\text{powers of }\ln|x|)$ as $x\to0$, where $\Delta'>\Delta$ is the lowest dimension among the omitted operators. In momentum space this becomes the large-Euclidean-$q$ expansion. (b) *Light-cone OPE.* For $x^2\to0$, an infinite tower of operators of fixed twist contributes at the same power. For DIS the relevant tower is twist 2, $O^{\mu_1\cdots\mu_N}_{q}=\bar\psi\gamma^{\{\mu_1}iD^{\mu_2}\cdots iD^{\mu_N\}}\psi-{\rm traces}$ (and the gluon analogue).

**What is proven, by whom, where.**
* Wilson proposed the OPE [Wilson:1969zs]. Zimmermann proved it in renormalized PT (BPHZ, normal products) for a *scalar* field theory: "Normal products are defined in perturbation theory for renormalizable interactions of a scalar field… Wilson's asymptotic short distance expansion is verified… for a product of two field operators" [Zimmermann:1972tv] [abs]; see also [Zimmermann:1972te] and the 1970 Brandeis lectures [Zimmermann:1970Brandeis] (bibliographic details partly UNVERIFIED, see the manual BibTeX note). Wilson–Zimmermann give an axiomatic framework [Wilson:1972ee].
* Convergence: in Euclidean massive φ⁴₄ the OPE is not only asymptotic but converges at finite distances at every finite loop order [Hollands:2011gf] [abs]. The same holds for massless φ⁴₄ [Holland:2014pna] [abs]. Curved-space version: [Hollands:2006ag] [abs].
* Gauge theories:
  * The renormalization of gauge-invariant local operators to all orders is established: they mix only with BRST-exact and equation-of-motion (EOM) operators [Joglekar:1975nu] [abs], [Kluberg-Stern:1974iel, Kluberg-Stern:1975ebk] [abs]. A simplified proof via antifield cohomology is [Henneaux:1993jn] [abs]. An apparent contradiction found by Hamberg and van Neerven is explained by subtle IR singularities of gluonic matrix elements taken on shell at zero momentum transfer [Collins:1994ee] [abs].
  * Joglekar treats the OPE of two gauge-invariant currents in non-abelian theories and shows that the gauge-variant operators which can appear have vanishing or unisolable physical matrix elements [Joglekar:1976eb, Joglekar:1976pe] [abs].
  * Collins' *Renormalization*: ch. 10 proves the OPE for connected Green functions in φ⁴ at leading power (§10.3) and states "Our proof generalizes" (§10.4). §12.8 says "This expansion is proved in a gauge theory the same way as in any other theory", then restricts to BRST-invariant operators, i.e. gauge-invariant plus classes A and B [txt §10.4, §12.8 of Collins:1984xc]. The book was reissued Open Access in 2023, DOI 10.1017/9781009401807.
  * Rigorous results for **pure Yang–Mills**: perturbative construction in curved spacetime, where "the operator product expansion closes on the space of gauge invariant operators" [Hollands:2007zg] [abs]. All-order bounds for correlators of gauge-invariant composite operators in Euclidean YM, including IR control [Frob:2015uqy] [abs].
  * IJJSZ (2018) summarize: "For such operators the OPE has been proven for scalar field theory to all orders in perturbation theory, and is widely assumed to hold for any renormalizable quantum field theory including QCD" [txt Sec. II of Izubuchi:2018srq].
* Light-cone expansion:
  * Formulated by Brandt–Preparata [Brandt:1970kg] and Frishman [Frishman:1970fx, Frishman:1971qn] [bib].
  * Christ–Hasslacher–Mueller derived, order by order in PT, RG-type equations for $W_1,\nu W_2$ (Symanzik's technique) and computed leading logarithms in fermion–pseudoscalar and fermion–vector theories [Christ:1972ms] [abs].
  * Anikin–Zav'yalov derived "short-distance and light-cone expansions for T-ordered products of currents… in the framework of the arbitrary order of the perturbation theory" [Anikin:1978tj] [abs]. Which class of theories is covered was not checked (UNVERIFIED). Monograph: [Zavyalov:1990kv] [bib].
  * Non-local light-ray operator formalism: [Balitsky:1987bk], [Muller:1994ses] [bib].
* Related: the only asymptotically free theories are non-abelian gauge theories [Coleman:1973sx]; Bjorken scaling in QFT [Callan:1973pu] [bib].
* Beyond PT: OPE with condensates [Shifman:1978bx]; model studies "Can it fail?" [Novikov:1984rf] [abs]; renormalon ambiguities of composite operators [David:1983gz, David:1985xj] [abs].

**Level.** All orders in PT.

**Sketched or disputed steps.** For QCD with massless quarks, no proof written out at Zimmermann's level was found. The standard sources assert that the scalar proof carries over (Collins 1984 §12.8) or "widely assume" it (IJJSZ). The IR issues of massless fields are handled by BPHZL [Lowenstein:1975rg, Lowenstein:1975ps] or dimensional renormalization [Breitenlohner:1975hg, Breitenlohner:1976te]. The Euclidean OPE gives asymptotics at large $-q^2$ with other momenta fixed. Its use for DIS proceeds via the forward Compton amplitude in the unphysical region and dispersion relations (item 2).

**Counterexamples.** None in PT. Beyond PT the OPE is not established; IR renormalons make the split into coefficients and condensates ambiguous (item 22).

**Tag.** **[A]** for QCD; **[R]** for φ⁴ and for gauge-invariant operators in pure YM; **[C]** non-perturbatively.
*Recommendation:* OUTLINE Ch5 calls moment factorization "[R in PT]". Either qualify it with a footnote ("rigorous given the OPE, which is rigorously proven for scalar theories and pure YM; for QCD with quarks it is the standard extension") or tag it [A] (see the discrepancies list).

### Item 2 — DIS moments and DGLAP (GW, GP, GL, AP, Dokshitzer)

**Statements.**
* Forward Compton amplitude: $T^{\mu\nu}=i\int d^4z\,e^{iq\cdot z}\langle P|T J^\mu(z)J^\nu(0)|P\rangle$, analytic in $\omega=1/x$ with cuts on $|\omega|\ge1$.
* The OPE applies for $|\omega|<1$; a dispersion relation identifies its Taylor coefficients with moments. For electromagnetic neutral-current $F_2$ only even $N$ appear (crossing):
$$M_N(Q^2)\equiv\int_0^1dx\,x^{N-2}F_2(x,Q^2)=\sum_{i=q,\bar q,g}C^{(2)}_{N,i}\!\Big(\frac{Q^2}{\mu^2},\alpha_s(\mu)\Big)A_{N,i}(\mu)+O\!\Big(\frac{\Lambda^2}{Q^2}\Big),\quad N=2,4,\dots$$
* With the CONTEXT definition of $f_q$, the reduced twist-2 matrix elements are PDF moments:
$$\int_{-1}^{1}d\xi\,\xi^{N-1}f_q(\xi)=\frac{\langle P|\bar\psi(0)\gamma^+(iD^+)^{N-1}\psi(0)|P\rangle}{2(P^+)^N}=\int_0^1d\xi\,\xi^{N-1}\big[q(\xi)+(-1)^N\bar q(\xi)\big].$$
  I checked the normalization for a free quark target ($f=\delta(1-\xi)$) and the sign relation using $f_{\bar q}(\xi)=-f_q(-\xi)$.
* RG: $\partial A_{N,i}/\partial\ln\mu^2=\frac{\alpha_s}{2\pi}\sum_j\gamma_{ij}(N)A_{N,j}$ with $\gamma_{ij}(N)=\int_0^1dz\,z^{N-1}P_{ij}(z)$, equivalent to x-space DGLAP.
* LO kernels in the CONTEXT normalization, checked with sympy (`checks/lo_moments_check.py`):
$$P_{qq}=C_F\Big[\tfrac{1+z^2}{1-z}\Big]_+,\quad P_{qg}=T_F[z^2+(1-z)^2],\quad P_{gq}=C_F\tfrac{1+(1-z)^2}{z},$$
$$P_{gg}=2C_A\Big[\tfrac{z}{(1-z)_+}+\tfrac{1-z}{z}+z(1-z)\Big]+\delta(1-z)\tfrac{11C_A-4n_fT_F}{6}.$$
* Moments: $\gamma_{qq}(N)=C_F[\tfrac32+\tfrac1{N(N+1)}-2S_1(N)]$, so $\gamma_{qq}(1)=0$ (quark number). $\gamma_{gg}(N)=2C_A[\tfrac1{N(N-1)}+\tfrac1{(N+1)(N+2)}-S_1(N)]+\tfrac{\beta_0}{2}$. Momentum sum rules: $\gamma_{qq}(2)+\gamma_{gq}(2)=0$ and $\gamma_{gg}(2)+2n_f\gamma_{qg}(2)=0$ (verified).

**Who, where.**
* Anomalous dimensions of twist-2 operators and moment predictions: [Gross:1973id, Gross:1973ju, Gross:1973zrg], [Georgi:1974wnj], with [Politzer:1973fx] [bib].
* Parton-language and leading-log derivations: Gribov–Lipatov in QED and pseudoscalar theories [Gribov:1972ri, Gribov:1972rt], [Lipatov:1974qm]; Altarelli–Parisi [Altarelli:1977zs]; Dokshitzer [Dokshitzer:1977sg] [bib].
* Two-loop kernels: [Floratos:1977au] (+ erratum), [Curci:1980uw], [Furmanski:1980cm]. Three-loop: [Moch:2004pa, Vogt:2004mw] [bib].
* x-space DGLAP from the renormalization of the operator-defined PDF: [Collins:1981uw] ("renormalization, light-cone expansions and sum rules" [abs]); Collins 2011 §8.3–8.5, §11.4 [txt TOC].

**Level.** The structure holds at all orders in PT. Kernels are known exactly to three loops.

**Sketched steps and caveats.**
1. The moment statement inherits the OPE caveat of item 1.
2. *From moments to $x$-space.* $F_2(x)$ has support in $[0,1]$, and the even moments determine it. Müntz–Szász gives density of $\{x^{2k}\}$ in $C[0,1]$, since $\sum 1/(2k)=\infty$. Because perturbative structure functions are distributions ($\delta(1-x)$, plus distributions), uniqueness should be stated for compactly supported distributions or measures. However, moment-wise remainders $O(\Lambda^2/Q^2)$ with $N$-dependent constants give convergence only in the weak (smeared) sense. They do **not** give a pointwise-in-$x$ remainder, and in particular nothing uniform near $x\to1$. Pointwise statements come from the graph-based proof (item 6).
3. The DGLAP equation for $\overline{\rm MS}$ PDFs is rigorous given the renormalization of local twist-2 operators (Joglekar–Lee class; item 1), the support property (item 7), and the Mellin-moment/local-operator identity. The parton-model derivations (AP 1977, LLA) are heuristic but agree.

**Tag.** **[R]** (moment factorization: [R] modulo item 1; kernels: [R] at each computed order).

### Item 3 — IR finiteness of $e^+e^-$ and jet cross sections; Euclidean Green functions

**Statements.**
* (a) Total cross section: $\Pi^{\mu\nu}(q)=i\int d^4x\,e^{iqx}\langle0|Tj^\mu(x)j^\nu(0)|0\rangle=(q^\mu q^\nu-q^2g^{\mu\nu})\Pi(q^2)$ and $R(s)=12\pi\,{\rm Im}\,\Pi(s+i0)$. For massless quarks and photon exchange, $R=N_c\sum_qe_q^2[1+\alpha_s/\pi+O(\alpha_s^2)]$. As a normalization check, the free-quark $\Pi=-\frac{N_c\sum e_q^2}{12\pi^2}\ln(-q^2/\mu^2)+\dots$ gives $R=N_c\sum e_q^2$.
* (b) IR-safe weighted or jet cross sections are finite as masses go to 0, order by order.
* (c) Euclidean Green functions at non-exceptional momenta are IR finite in massless renormalizable theories.

**Who, where.**
* (c) Poggio–Quinn: "a simple proof that all Green's functions for nonexceptional Euclidean momenta in any renormalizable (but not superrenormalizable) field theory containing zero-mass particles are infrared finite… any physical discontinuity of Green's functions is also infrared finite" [Poggio:1976qr] [abs].
  * Rigorous BPHZL framework: IR power-counting theorem [Lowenstein:1975rg] and convergence theorems for zero-mass propagators [Lowenstein:1975ps] [abs]; [Lowenstein:1974qt].
  * Dimensional renormalization: existence of Green functions to all orders for massless theories without super-renormalizable couplings [Breitenlohner:1975hg, Breitenlohner:1976te] [abs].
  * Pure YM with full UV and IR control: [Frob:2015uqy] [abs]. UV power counting: [Weinberg:1959nj], [Hahn:1968HZ].
* (a) Optical theorem plus (c). Order by order, $\Pi$ is a polynomial in $\ln(-q^2/\mu^2)$ (RG plus dimensional analysis in the massless theory), so its continuation to $s>0$ is finite. Textbook account: Collins 2011 §4.1 [txt TOC]; smearing and duality: Poggio–Quinn–Weinberg [Poggio:1975af] [abs].
* (b) Sterman 1978 I, II: "loop momentum configurations which can give rise to mass divergences are of a severely limited form and have a direct interpretation in terms of physically realizable processes… cross sections smeared over a small region of phase space are at worst logarithmically divergent". In II, mass divergences cancel for ensembles of jet-like states, "extended to… non-Abelian gauge theories" [Sterman:1978bi, Sterman:1978bj] [abs]. Kinoshita's theorem in Yang–Mills [Sterman:1976jh]; jet cross sections finite "to all orders in perturbation theory" [Sterman:1979uw] [abs]; Sterman–Weinberg jets [Sterman:1977wj]; operator approach to weighted cross sections [Ore:1979ry].
* KLN: [Kinoshita:1962ur], [Lee:1964is]. Bloch–Nordsieck: [Bloch:1937pw].

**Counterexamples and limitations.**
* *Non-abelian Bloch–Nordsieck fails* for coloured initial states. Doria–Frenkel–Taylor: "two quarks (with non-zero mass, colour averaged) in the initial state, in which non-leading infrared divergences coming from two soft gluons do not cancel" [Doria:1980ak] [abs]. Confirmed by [DiLieto:1980nkq], which agrees on the non-cancellation but disagrees on intermediate results [abs], and by [Andrasi:1980qw] [abs].
* The non-cancelling terms are power-suppressed. The Bloch–Nordsieck cross section is finite "except for terms which are power-suppressed at high energies" to $O(g^4)$, with an argued all-order extension [Frenkel:1983di] [abs]. The terms are "in general of higher twist type" [Catani:1985xt] [abs].
* The CSS review (§10.2) states that at two loops non-cancelling divergences appear at relative order $m^4/s^2$ in DY [txt §10.2 of Collins:1989gx].
* *KLN* needs sums over degenerate initial *and* final states. Frye et al. show that a one-sided sum suffices but generically requires forward scattering and disconnected diagrams [Frye:2018xjj] [abs].

**Tag.** **[R]** for (a) and (c); **[A]** for (b) (all-order argument with Landau equations plus power counting plus unitarity; widely accepted; not at BPHZ-level rigor). The Bloch–Nordsieck statement with coloured initial states is **[V]** (power-suppressed).

### Item 4 — Landau equations and Coleman–Norton

**Statements.**
* Landau conditions for a pinch singular surface of a graph with internal lines $k_j$ (masses $m_j$): there exist $\alpha_j\ge0$, not all zero, with
$$\alpha_j\,(k_j^2-m_j^2)=0\ \ \forall j,\qquad \sum_{j\in L}\epsilon_{Lj}\,\alpha_j\,k_j^\mu=0\ \ \forall\ \text{loops }L.$$
* Coleman–Norton: with $\Delta x_j^\mu\equiv\alpha_jk_j^\mu$, physical-region solutions describe classical on-shell particles propagating forward in time between vertices, with closed spacetime loops.

**Who, where.** [Landau:1959fi], [Nakanishi:1959jzx], discontinuities [Cutkosky:1960sp], [Coleman:1965xm], the ELOP book [Eden:1966dnq], Pham (homology, Picard–Lefschetz) [Pham:2011SingInt], Sterman's textbook [Sterman:1993hfp] [bib].

**Status of the proofs.**
* Collins 2011 §5.4.3: a search for a published proof that "the Landau equations are both necessary and sufficient for a PSS" would be "rewarded by not finding a published explicit and complete proof. Textbook treatments, when examined closely, are incomplete". ELOP p. 48 is quoted: "A proper proof needs the use of topology; … We shall be content with plausibility arguments" [txt p. 110 of Collins:2011zzd]. Exercise 5.3 (***) asks for such a proof.
* Collins (2020), arXiv:2007.04085: "in existing treatments there are significant gaps… implicit assumptions… false in important cases like the massless Feynman graphs ubiquitous in QCD applications". It gives "a new proof that the Landau condition is both necessary and sufficient for physical-region pinches", including the modified graphs used in QCD, without Feynman parameters [Collins:2020euz] [abs]. It notes that a property "universally assumed in textbook proofs… is in fact false" (App. B1), and on Coleman–Norton: "it is not the result that breaks down, but the proof" [txt].
* Mühlbauer (2020), arXiv:2011.10368: momentum-space Landau equations via isotopy, including second-type singularities [Muhlbauer:2020kut] [abs]. Algebraic-geometry approach: [Fevola:2023kaw] [bib].
* INSPIRE lists no journal publication for Collins 2020 or Mühlbauer 2020 (checked 2026-10-09).

**Tag.** **[A]**. For standard massive graphs the classic arguments reach the correct conclusion (Collins 2020 says of Coleman–Norton that "it is not the result that breaks down, but the proof"). The topological theory of singularities of integrals (Pham) underlies the necessity statement. A gap-free proof of necessity and sufficiency covering the massless and modified graphs used in QCD exists only in a preprint (Collins 2020). The Coleman–Norton interpretation is a reformulation of the Landau conditions; its status follows theirs.

### Item 5 — Power counting and leading regions (Sterman 1978; Libby–Sterman 1978)

**Statement.** For a pinch singular surface (PSS) $R$ with collinear scaling parameter $\lambda$ and soft scale $\lambda_S=\lambda^2/Q$ (Collins 2011 eqs. (5.75)–(5.79), [txt pp. 140–141]):
$$Q^p\Big(\frac{\lambda}{Q}\Big)^{\alpha(R)}\Big(\frac{\lambda_S}{Q}\Big)^{\beta(R)}\Big(\frac mQ\Big)^{{\rm s.r.}(H)}\Big(\frac m\lambda\Big)^{{\rm s.r.}(C)}\Big(\frac m{\lambda_S}\Big)^{{\rm s.r.}(S)},\qquad p=4-\#(\text{ext. lines}),$$
$$\alpha(R)=\#(CH)-\#(\text{scalar-pol. glue }CH)-\#(\text{ext. lines}),\qquad \beta(R)=\#(0\text{ or }1,SH)+\tfrac32\#(\tfrac12,SH)+\tfrac12\#(0\text{ or }\tfrac12,SC),$$
with hard-subgraph dimension $d_H=4-\tfrac32N_F-N_B$. Here "s.r." are dimensions of super-renormalizable couplings; they vanish in QCD.
Leading-region rules (§5.9.2): (1) soft subgraphs attach only to collinear subgraphs and only by gluons; (2) collinear subgraphs attach to the hard part with the minimal number of lines; (3) plus any number of scalar-polarized collinear gluons.

**Who, where.** [Sterman:1978bi] (power counting for cut vacuum polarization graphs) [abs]; [Libby:1978qf] (to all orders, moments factorize in leptoproduction; extension to hadron–hadron where IR divergences cancel; massless QED) [abs]; [Libby:1978bx] [abs]; Collins 2011 ch. 5 (§5.6 Glauber pinches, §5.8–5.11) [txt]; review [Collins:1989gx]; TASI notes [Sterman:1995fz] [bib]. Modern systematics: regions as Landau solutions and facets of the Newton polytope for the on-shell expansion [Gardi:2022khw] [abs]; graph-theoretic identification for wide-angle scattering [Ma:2023hrt] [bib].

**Sketched steps.**
* Nested and overlapping regions need subtractions (Collins §5.10, ch. 10).
* In Feynman gauge, individual graphs can be "super-leading". Leading regions are incomplete: "There can be regions with extra disconnected hard-scattering subgraphs… Such extra hard scatterings cancel after a sum over graphs for the hard scattering (Labastida and Sterman, 1985)" [txt §14.4.8]. See also [Labastida:1984gy] [abs].
* The Glauber region is handled separately (§5.6, §5.11; items 8 and 13).

**Tag.** **[A]**.

### Item 6 — DIS collinear factorization by graph methods

**Statement.**
$$F_{1,2,L}(x,Q^2)=\sum_{i}\int_x^1\frac{d\xi}{\xi}\,C_i\!\Big(\frac x\xi,\frac{Q}{\mu},\alpha_s(\mu)\Big)f_{i/H}(\xi,\mu)+O\big((\Lambda/Q)^a\big),$$
with gauge-invariant operator-defined PDFs (item 7). For leading twist in DIS, $a=2$ in practice (twist 4).

**Who, where.**
* Early all-order arguments in physical (axial or light-cone) gauges:
  * EGMPR: "mass-singularities of inclusive cross sections in QCD factor to all orders"; the NPB paper claims proof "for all leading and non-leading logs" [Ellis:1978sf, Ellis:1978ty] [abs].
  * Amati–Petronzio–Veneziano: "at all orders the factorization of mass singularities for every hard QCD process" [Amati:1978wx, Amati:1978by] [abs].
  * Libby–Sterman [Libby:1978qf]; Mueller's cut vertices, with a Callan–Symanzik equation "valid to all orders… in both gauge and nongauge theories" [Mueller:1978xu] [abs], [Mueller:1981sg]; light-cone gauge 2PI kernels [Curci:1980uw]; [Collins:1981ta].
* CSS review (1989): "Factorization proofs in nonabelian gauge theories have reached a certain level of sophistication… there is as yet in the literature no complete and systematic subtraction procedure in QCD… even in the case of deeply inelastic scattering" [txt §10.1 of Collins:1989gx].
* Collins 2011:
  * "complete proof in a non-gauge theory in Sec. 8.9" (ladder method) [txt ch. 11 intro].
  * Subtraction formalism in ch. 10; QCD in §11.3.
  * Gauge choice: physical gauges have unphysical singularities that obstruct contour deformations out of the Glauber region; "to the best of my knowledge [the required demonstration] has not been done… for fully general and reliable proofs one should use Feynman gauge" [txt §12.6].
* Heavy-quark masses: "A detailed proof of hard scattering factorization is given with the inclusion of heavy quark masses… power-suppressed corrections… uniformly suppressed by a power of Λ/Q, independently of… M" [Collins:1998rz] [abs].

**Explicitly acknowledged gaps (Collins 2011 §11.3.2, pp. 407–410)** [txt]:
1. "In much of the original work on proving factorization the issues related to extracting K gluons from the hard scattering were glossed over." Labastida–Sterman proved that one gets zero when all or all but one external lines are K gluons, but only in the strictly collinear limit. Collins–Rogers (2008) found a non-zero leading remainder, which is needed for the correct gauge-invariant gluon PDF [Collins:2008sg] [abs].
2. Collins therefore uses a BRST argument. BRST-invariant operators are gauge invariant, BRST-exact (class A) or EOM-vanishing (class B), a theorem proven for local operators (Joglekar–Lee 1976; Joglekar 1977a,b; Nakanishi–Ojima). Quote: "Unfortunately, the published proofs… apply as written to local operators… as far as I know, no proof has been given [for non-local operators]. For the purposes of the discussion, I will assume the result is true, and leave the proof (or refutation) to future research."

**Relation to item 2.** For moments, only local operators enter, so the moment-space statement avoids gap 2. The $x$-space theorem with pointwise remainder needs the graph proof.

**Tag.** **[A]** ($x$-space, graph-based); moment space as in item 2.

### Item 7 — Operator definitions of PDFs and FFs; support; positivity

**Definitions.** $f_{q/H}(\xi;\mu)=\int\frac{dw^-}{4\pi}e^{-i\xi P^+w^-}\langle P|\bar\psi(w)\gamma^+W[w,0]\psi(0)|P\rangle$ (CONTEXT), and similarly for gluons and FFs [Collins:1981uw]. Earlier steps: [Soper:1976jc, Soper:1979fq] [bib]. Collins 2011 §6.3 (operators), §7.5–7.6 (Wilson lines and Feynman rules), §12.4 (FFs) [txt TOC].

**Support and crossing.**
* Collins 2011 §6.9.3 [txt p. 191]: intermediate states have $P^+-k^+\ge0$, so $f=0$ for $\xi>1$ (integrated and unintegrated alike). (Anti)commuting the fields at light-like separation gives $f_{j/h}(\xi)=-f_{\bar j/h}(-\xi)$ (and $f(\xi,k_T)=-f_{\bar j}(-\xi,-k_T)$), so $f=0$ for $\xi<-1$. Collins notes "The proofs are non-perturbative".
* Jaffe 1983: twist-4 multiparton distributions have $0\le k^+/p^+\le1$ for all quanta, given on-shell intermediate states and no semi-disconnected graphs [Jaffe:1983hp] [abs].
* GPDs: [Diehl:1998sm] [bib].

**Number density and positivity.**
* For bare (light-front, cutoff) densities, $f=\|a|P\rangle\|^2\ge0$ (Collins 2011 §6.7, §6.9.1). But "this particular result will not hold exactly in renormalizable theories, because of the need for renormalization" [txt §6.9.1]. TMD FFs: "Failure of positivity" at large $k_T$ [txt §13.14.3].
* $\overline{\rm MS}$ debate:
  * Candido–Forte–Hekhorn: "NLO $\overline{\rm MS}$ PDFs are actually positive in the perturbative regime", via a positive-coefficient scheme and the NLO scheme change [Candido:2020yat] [abs].
  * Collins–Rogers–Sato: the primary failure is the assumption that bare PDFs are always positive. With DR used for both UV ($n<4$) and collinear ($n>4$) divergences, "Divergent UV contributions… can and often do become negative after analytic continuation". They illustrate in a model QFT and contrast "track A" and "track B" [Collins:2021vke] [abs].
  * Candido–Forte–Giani–Hekhorn (2024): they agree that PDFs "turn negative at a low enough scale" and argue that positivity is inherited in the perturbative domain. Their estimate is $Q^2\gtrsim5$ GeV², "a very conservative semi-quantitative estimate". NNPDF4.0 imposes positivity at $Q^2=5$ GeV² [txt §3–4 of Candido:2023ujx].
  * Polarized bounds: [Altarelli:1998gn].

**Tag.** **[R]** for definitions, gauge invariance, renormalization (PT), and support (graph by graph; non-perturbatively via spectral arguments, [A]). **[C]** for $\overline{\rm MS}$ positivity. The number-density interpretation holds only for bare or regularized densities.

### Item 8 — Drell–Yan factorization and Glauber cancellation

**Statement.** $\frac{d\sigma}{dQ^2dy}=\sum_{ij}\int d\xi_ad\xi_b\,f_{i/A}(\xi_a,\mu)f_{j/B}(\xi_b,\mu)\,\frac{d\hat\sigma_{ij}}{dQ^2dy}+O(\Lambda^2/Q^2)$ (Collins 2011 eq. (14.1)). Leading power corrections are twist 4 [Qiu:1990xxa, Qiu:1990xy].

**History (verified).**
* BBL 1981: "initial-state interactions violate the usual QCD factorization predictions… in leading twist" [Bodwin:1981fv] [abs]. BBL 1989: such interactions "can invalidate the parton-model (factorized) form… unless the beam energy is greater than a scale that grows with the length of the target", and they increase $\langle q_T^2\rangle$ in proportion to target length [Bodwin:1988fs] [abs].
* CSS steps: new form of factorization [Collins:1981tt]; one loop [Collins:1982wa]; outline of all-order arguments [Collins:1983ju] [abs].
* Bodwin 1985: one- and two-loop examples, then "this factorization program can be implemented to all orders"; DY structure functions "simply related to those that occur in deep-inelastic lepton scattering" [Bodwin:1984hc] [abs]. Erratum: PRD 34 (1986) 3932 (content not examined).
* CSS 1985 [Collins:1985ue] [abs] and CSS 1988 "Soft gluons and factorization" [Collins:1988ig] [abs].
* Two-loop checks: the sum of non-factorizing spectator terms is zero [Lindsay:1982pu, Lindsay:1982gd]. Two-loop eikonal "meson" model: cancellation verified [Brandt:1988xt] [abs].
* Collins 2011 §14.4: "I will follow the proof given by Collins, Soper, and Sterman (1988), but with some important improvements and with correction of errors. That reference supersedes earlier work (Bodwin, 1985; Collins, Soper, and Sterman, 1985a)" [txt p. 553]. The steps (§14.4.1): region decomposition, then sum over cuts, then deformation "away from initial-state singularities" (with final-state singularities crossed but cancelled after the sum over cuts), then a Grammer–Yennie approximant with *past-pointing* Wilson lines, then Ward identities. For the $q_T$-integrated cross section, T invariance (§13.17) equates past- and future-pointing soft factors, after which unitarity cancels the soft factor [txt §14.4.6].
* Bodwin–Brodsky–Lepage phases: "while the phases exist and give a contribution to the cross section, their effects do not break factorization; rather they get moved into the parton densities" [txt §14.4.7].
* Aybat–Sterman: outline of soft cancellation with incoming partons and Wilson lines and with final-state jets or heavy particles [Aybat:2008ct] [abs, txt].
* DGOPS 2016: "To the best of our knowledge, the cancellation of Glauber gluon exchange in single hard scattering has also been established only for Drell-Yan production". They "revisit and clarify some issues" for single DY. Their §3.5 notes difficulties generalizing the one-gluon method to all orders "already for single Drell-Yan production". The all-order proof uses light-cone perturbation theory following CSS 1988 and Collins [txt §1, §3.5, §4 of Diehl:2015bca].

**Remaining issues (verified).**
* Collins §14.4.8 "Issues remaining" [txt p. 561–562]:
  1. Proof relies on the PT momentum categories. A non-perturbative "graduated rapidity" Glauber exchange (multiperipheral, Regge-like) is not covered.
  2. Leading regions are incomplete in Feynman gauge (extra disconnected hard scatterings; Labastida–Sterman 1985).
  3. "The current versions of genuine proofs are evidently formidable."
* SCET: Rothstein–Stewart give the Glauber Lagrangian. The spectator–spectator phase cancels after the unrestricted $\Delta p_\perp$ integral, but "taken alone it is far from a proof of factorization, even in the abelian case". Further, "A complete proof of factorization in SCET entails proving that the Glauber Lagrangian does not contribute… will be given elsewhere" [txt §11.1 of Rothstein:2016bsq]. The TMD Handbook cites "Rothstein and Stewart, A Proof of Factorization for Drell-Yan with SCET, to appear" [txt ref. [230] of Boussarie:2023izj]. An INSPIRE search (2026-10-09) found no such paper.
* Higher twist: Qiu–Sterman establish generalized factorization at $1/Q^2$ [abs]. In a scalar-quark model, factorization "holds at order $m^2/s$, but fails at order $m^4/s^2$" [Basu:1984ba] [abs]. CSS 1989 §10.2 [txt]: two-loop non-cancellation at $m^4/s^2$ in DY. BBL 1995 restate: "one can prove only that a factored form holds through next-to-leading order in… $1/Q^2$… Beyond that order, factorization is known to fail", citing Qiu–Sterman and Doria et al. [txt §VI of Bodwin:1994jh].
* Less inclusive observables:
  * Hadronic $E_T$: "the classic CSS argument… breaks down at the level of two Glauber gluons", so MPI-sensitive observables (beam thrust, transverse thrust) lack standard factorization [Gaunt:2014ska] [abs].
  * Jet vetoes / beam thrust: "a direct counter-example in QCD with scalar quarks, contradicting any form of factorization in which the two collinear sectors are decoupled" (non-zero leading-power spin asymmetry from spectator Glauber exchange) [Zeng:2015iba] [abs].
  * Partial rebuttal: for *pure* Glauber ladders, factorization-violating effects cancel for any single-scale observable; violation needs at least one soft gluon (Lipatov vertex) [Schwartz:2018obd] [abs].

**Tag.** **[A]** for inclusive DY (and $W/Z/H$) at leading power. **[V]** beyond $1/Q^2$ (twist 6). **[V]** (counterexample) or **[C]** for jet-vetoed and MPI-sensitive observables.

### Item 9 — Single-inclusive hadron and jet production at large $p_T$ in hadron collisions

**Statement used in phenomenology.** $E_h\,d\sigma/d^3p_h=\sum\int f\otimes f\otimes d\hat\sigma\otimes D_{h/k}+\dots$ (or with jet functions).

**Status (verified quotes).**
* Collins 2011 §14.7: "there is a relative lack of detailed proofs of factorization in these cases… One notable exception is Nayak, Qiu, and Sterman (2005)" (= PRD 72 114012) [txt p. 570–571]. Also: "Our proof of factorization for the Drell-Yan process depended quite essentially on the cross section being completely inclusive in the hadronic part of the final state."
* [Nayak:2005rt]: "including a review of arguments for the factorization of high-$p_T$ particles into fragmentation functions for hadronic initial states" [abs].
* DGOPS 2016 (§5): for single-scattering processes with colour in the final state, "to the best of our knowledge the absence of Glauber gluon effects has not yet been proven" [txt].
* Rothstein–Stewart 2016: derivations exist "for single inclusive hadron production [CSS 1989 review; NQS 2005]… These results are often used to motivate using factorization to make predictions in other hadron-hadron scattering observables without complete proofs" [txt §1].
* CdFR 2012: violation of strict collinear factorization "may invalidate the factorization theorem of mass singularities starting at the N3LO" for inclusive high-$p_T$ jet or hadron production unless cancelled by other subprocesses. "An explicit quantitative proof of such a cancellation would represent a highly non-trivial check" [txt §8 of Catani:2011st].
* Heavy quarks: CSS 1986 argue from low-order graphs that the standard formula applies but "emphasize that an analysis at all orders of perturbation theory is needed to reliably establish this conjecture" [Collins:1985gm] [abs].
* Outline of soft and Glauber cancellation with final-state jets: [Aybat:2008ct].

**Tag.** **[C]** (borderline [A] if one accepts the NQS/Aybat–Sterman outlines). The TMD version is **[V]** (item 12).

### Item 10 — TMD factorization for DY, SIDIS, $e^+e^-$

**Statement** (DY, unpolarized; CONTEXT Fourier convention $\tilde f(b)=\int d^{2}k\,e^{-ik\cdot b}f(k)$):
$$\frac{d\sigma}{dQ^2dy\,d^2q_T}=\sigma_0\sum_je_j^2\,H(Q,\mu)\int\!\frac{d^2b_T}{(2\pi)^2}e^{iq_T\cdot b_T}\,\tilde f_{j/A}(x_A,b_T;\mu,\zeta_A)\,\tilde f_{\bar j/B}(x_B,b_T;\mu,\zeta_B)+Y+O\big((q_T/Q)^a,(\Lambda/Q)^a\big),\quad \zeta_A\zeta_B=Q^4.$$
I checked that $\int\frac{d^2b}{(2\pi)^2}e^{iq\cdot b}\tilde f_A\tilde f_B=\int d^2k_Ad^2k_B\,\delta^2(q-k_A-k_B)f_Af_B$.
Evolution (Collins): $\partial\ln\tilde f/\partial\ln\sqrt\zeta=\tilde K(b_T;\mu)$ and $d\tilde K/d\ln\mu=-\gamma_K(\alpha_s)$. At one loop
$$\tilde K=-\frac{\alpha_sC_F}{\pi}\big[\ln(\mu^2b_T^2)-\ln4+2\gamma_E\big]=-\frac{\alpha_sC_F}{\pi}\ln\frac{\mu^2b_T^2}{b_0^2},\qquad \gamma_K=\frac{2C_F\alpha_s}{\pi}+O(\alpha_s^2),$$
from [txt eqs. (13.55)–(13.56) of Collins:2011zzd] (with $g^2/(4\pi^2)=\alpha_s/\pi$). Here $b_0=2e^{-\gamma_E}$.

**Who, where.**
* $e^+e^-\to h_1h_2X$: Collins–Soper 1981 [Collins:1981uk] (+ erratum NPB 213 (1983) 545), [Collins:1981va]. The TMD Handbook: "The first process where TMD factorization was proven is back-to-back hadron production in $e^+e^-$" [txt §2.11.4].
* DY $q_T$ and the CSS formula: [Collins:1984kg] [abs].
* SIDIS: Meng–Olness–Soper (energy-integrated) [Meng:1995yn]; Nadolsky–Stump–Yuan [Nadolsky:1999kb]; Ji–Ma–Yuan: "verify the factorization to one-loop order… and argue that it is valid to all orders", with gauge links slightly off the light cone [Ji:2004wu] [abs], plus [Ji:2004xq] (spin) and [Ji:2005nu] (gluon TMDs). Collins 2011 §13.15.2 states that these treatments "ignored important quark polarization effects", provided in JMY 2004 [txt].
* Collins 2011 ch. 13: final definitions (§13.7), with Wilson-line self-interactions cancelling in the final definitions (§13.7.2) [txt].
* Drell–Yan TMD: "the treatment of the Glauber region was originally formulated (CSS 1988) only in the context of… integrated parton densities… In fact, the argument works equally well for the TMD case" [txt §14.4.5].
* Definitional issues: light-like Wilson lines and rapidity divergences [Collins:2003fm, Collins:1999dz].
* SCET approaches:
  * Collinear anomaly; the product of TMDs is defined [Becher:2010tm] [abs].
  * On-the-light-cone Wilson lines with soft subtraction, "validated to first order in $\alpha_s$" [Echevarria:2011epo] [abs], [Echevarria:2012js].
  * Rapidity RG [Chiu:2011qc, Chiu:2012ir] [abs].
* Relation among formalisms and equality of non-perturbative functions: [Collins:2017oxh] [abs]. Review: [Boussarie:2023izj], whose ch. 3 says CSS methods give "foundational and complete results for factorization proofs" and that $\mathcal L_G^{(0)}$ "can be dropped" in SCET after the stated arguments [txt §3.1, §3.5].
* Higher-order checks: four-loop rapidity anomalous dimension [Duhr:2022yyp, Moult:2022xzt] [bib]. Renormalization theorem for rapidity divergences of (multi-parton) soft factors [Vladimirov:2017ksc] [abs].

**Tag.** **[A]** ($e^+e^-$ and SIDIS: Glauber avoidable by contour deformation; DY: via the CSS 1988 argument as extended by Collins).

### Item 11 — Sivers sign change and experimental status

**Statement.** $f_{1T}^{\perp q}(x,k_T)\big|_{\rm DY}=-f_{1T}^{\perp q}(x,k_T)\big|_{\rm SIDIS}$ (likewise the Boer–Mulders function $h_1^\perp$).

**Who, where.**
* Collins 2002: "An earlier proof that the Sivers asymmetry vanishes because of time-reversal invariance is invalidated by the path-ordered exponential… Instead, the time-reversal argument shows that the Sivers asymmetry is reversed in sign in hadron-induced hard processes" [Collins:2002kn] [abs]. The earlier claim is [Collins:1992kk] [bib].
* Model mechanism: [Brodsky:2002cx, Brodsky:2002rv] [abs]. Light-cone gauge with transverse links at infinity: [Ji:2002aa], [Belitsky:2002sm] [abs]. Universality of T-odd effects: [Boer:2003cm]. Original Sivers function: [Sivers:1989cc, Sivers:1990fh].
* Collins 2011 §13.17.1 (Sivers), §13.17.2 (Boer–Mulders), §13.17.5 (soft factors and $K$); in the DY proof, §14.4.1 items 8–10 [txt].

**Experimental status (verified).**
* SIDIS observation: [HERMES:2009lmz]; full HERMES analysis [HERMES:2020ifk].
* COMPASS 2017: "the observed sign of the Sivers asymmetry is found to be consistent with" the sign change [COMPASS:2017jbv] [abs]. COMPASS final 2015+2018 data (PRL 133 (2024) 071902): "consistent with the fundamental QCD prediction of a sign change" [COMPASS:2023vqt] [abs].
* STAR $W^\pm/Z$ (2011 data): χ²/ndf = 7.4/6 with the sign change versus 19.6/6 without (KQ model, no TMD evolution). "favor… a change of sign… if TMD evolution effects are small" [txt of STAR:2015vmv]. STAR $Z^0$ (2017 data): [STAR:2023jwh] [abs]. A STAR $W^\pm$ $A_N$ paper from the 2017 data was not found (only preliminary results; web check).
* Fits:
  * BPV 2021: a fit without the sign change "has χ²/N_pt = 1.0 and cannot exclude the same sign of Sivers functions in DY and SIDIS"; the sea-quark Sivers sign is central [txt of Bury:2020vhj].
  * Echevarria–Kang–Terry find tension when describing the RHIC W/Z data [Echevarria:2020hpy] [abs].

**Tag.** **[R]** given TMD factorization and the operator definitions (it follows from T and P invariance). Experimentally consistent but not established at high significance as of the literature checked.

### Item 12 — TMD factorization breaking

**Who, where.**
* Collins–Qiu 2007: explicit counterexample for the single-spin asymmetry in back-to-back hadron production in a simplified model. It "implies that standard arguments for factorization fail not just for the single-spin asymmetry but for the unpolarized cross section" [Collins:2007nk] [abs].
* Collins 2007 (arXiv:0708.4410; no journal record on INSPIRE): extension to two-gluon exchange. "by explicit calculation, standard $k_T$-factorization fails for the unpolarized cross-section" [Collins:2007jp] [abs].
* Rogers–Mulders 2010: generalized TMD factorization (process-dependent Wilson lines per hadron) is impossible in a non-abelian theory, shown by direct counterexample (double spin asymmetry, spectator model) [Rogers:2010dm] [abs].
* Vogelsang–Yuan: the dijet imbalance "obeys at best a non-standard or 'generalized'" TMD factorization [Vogelsang:2007jk] [abs].
* Process-dependent gauge links: [Bomhof:2004aw, Bomhof:2006dp]. Extra asymmetries from the breaking: [Rogers:2013zha] [abs].
* Collins 2011 §14.7: "these TMD factorization properties appear to fail (Collins and Qiu, 2007; Rogers and Mulders, 2010)" [txt].

**Tag.** **[V]** (counterexamples are model or low-order calculations, which suffice to disprove a general theorem).

### Item 13 — Space-like collinear factorization violation, super-leading logarithms, the Glauber operator

* **CdFR 2012.** "strict (process-independent) factorization is not valid at one-loop and higher-loop orders in the case of the collinear limit in space-like regions". They introduce generalized factorization, with dependence on non-collinear momenta and colour. Consequences for squared amplitudes start at NNLO (logs) and at N3LO (mass singularities) [Catani:2011st] [abs, txt].
* **FSS 2012.** For non-inclusive observables, "factorization is violated at the three-loop level… identical to… super-leading logarithms… driven by the non-commutation of Coulomb/Glauber gluon exchanges with other soft exchanges" [Forshaw:2012bi] [abs].
* **SLLs.**
  * Discovery in gaps-between-jets: [Forshaw:2006fk, Forshaw:2008cq] [abs].
  * Double logs start at four loops at hadron colliders; all-order structure and resummation [Becher:2021zkk] [abs]. Factorization theorem plus resummation [Becher:2023mtx] [abs]. RG-improved resummation [Boer:2024hzh] [abs]. pp → 2 jets [Becher:2024nqc] [abs].
  * "Factorization restoration through Glauber gluons": three-loop active–active Glauber contributions render gap-between-jets "consistent with PDF factorization below the gap veto scale" [Becher:2024kmk] [abs].
  * One-jettiness has "super-super-leading" logs from $\alpha_s^4\ln^6(1/\tau_1)$, "consistent with the factorization of universal parton distribution functions at scale $\tau_1Q$" [Banfi:2025mra] [abs].
* **Glauber EFT.** Operator basis for leading-power Glauber exchange in SCET; BFKL as rapidity RG; criteria for eikonalization and factorization violation [Rothstein:2016bsq] [abs, txt]. Related: [Schwartz:2018obd], [Dixon:2019lnw] [bib].
* **Consistency with all-order amplitude factorization.** The all-order hard–soft–collinear factorization of Feige–Schwartz [Feige:2014wja] explicitly excludes initial-state particles collinear to final-state particles [txt]. It is therefore not in conflict with the space-like violation found by CdFR. Almelid–Duhr–Gardi find that the three-loop non-dipole term preserves strict collinear factorization in the (time-like) two-particle collinear limit [Almelid:2015jia] [abs].

**Tag.** **[V]** for strict collinear factorization (space-like). **[C]** for the factorization of mass singularities in inclusive hadron-collider observables beyond NNLO (expected to hold; the explicit check is open). **[R]** for the existence of SLLs at fixed order (explicit calculation). **[A]** for LL resummation within its approximations.

### Item 14 — Diffractive factorization

* **DDIS: [A].** Collins 1998: "A proof is given that hard-scattering factorization is valid for deep-inelastic processes which are diffractive or which have some other condition imposed on the final state in the target fragmentation region" [Collins:1997sr] [abs] (erratum PRD 61 (2000) 019902). The conclusions add [txt]:
  * "Given the results… on the Drell-Yan process, we must not expect the theorem to be applicable to hadron-hadron collisions… It is only when one of the initiating particles is a lepton that the proof of factorization is valid."
  * "The proof would appear to apply also to direct photo-production… However, the proof does not apply to resolved photoproduction processes, since these are in effect hadron-hadron processes."
  * Fracture functions (Trentadue–Veneziano) are covered for DIS but fail in hadron–hadron collisions.
* Related: [Berera:1994xh, Berera:1995fj], [Trentadue:1993ka], [Ingelman:1984ns], [Bjorken:1992er] [bib].
* **Hadron–hadron: [V].**
  * Pre-QCD theory: factorization-breaking terms in diffractive and non-diffractive DY that cancel in the inclusive sum [Landshoff:1971zu], [Henyey:1974zs], [Cardy:1974vq], [DeTar:1974vx]; coherent pomeron [Collins:1992cv] [bib].
  * Experiment: diffractive W [CDF:1997gvd]; diffractive dijets [CDF:2000rua]. CDF Run II recalls the Run I result as "a breakdown of QCD factorization, expressed as a suppression by a factor of O(10) of the diffractive structure function… relative to that derived from… DDIS at HERA" [txt §I of CDF:2012nhl].
  * Fits: "predictions for the Tevatron cross sections are substantially higher than data" [Alvero:1998ta] [abs].
  * LHC: gap survival estimated [CMS:2012odd] [abs].
* **Diffractive photoproduction at HERA.**
  * H1: in DIS the dijets are "well described, supporting the validity of QCD factorisation". In photoproduction the prediction "has to be multiplied by a factor of approximately 0.5 for both direct and resolved", the "first clear observation of QCD hard scattering factorisation breaking at HERA" [H1:2007jtx] [abs]. DPDFs: [H1:2006zyl].
  * ZEUS: [ZEUS:2007uvk] [abs].
  * Review: global suppression 0.42 (H1) and 0.71 (ZEUS) if direct and resolved are suppressed equally; or a factor ≈3 suppression of resolved only [Klasen:2008ah] [abs].

### Item 15 — Double parton scattering factorization

**Statement** (collinear, colourless final states): $\sigma_{\rm DPS}=\frac1C\sum\int d^2y\,F_{a_1a_2}(x_1,x_2,y)F_{b_1b_2}(\bar x_1,\bar x_2,y)\,\hat\sigma_{a_1b_1}\hat\sigma_{a_2b_2}$, with $C=2$ for identical final states and $1$ otherwise. Colour, spin and flavour interference terms are also present [Diehl:2011yj].

**Who, where.**
* Elements of a theory: power counting, colour and spin structure, Sudakov logs [Diehl:2011yj] [abs].
* $\delta^{(2)}(z_\perp)$ singularity and mixing with single PDFs [Manohar:2012jr, Manohar:2012pe] [abs]. dDGLAP and "1v2" contributions [Blok:2011bu]. dPDF sum rules [Gaunt:2009re], proven to all orders [Diehl:2018kgr] [abs].
* DGOPS 2016: Glauber cancellation "at all orders for double Drell-Yan production… both for the integrated cross section and for the cross section differential in the transverse boson momenta" [Diehl:2015bca] [abs].
* DGS 2017: double counting between SPS and DPS solved; dPDFs as operator matrix elements [Diehl:2017kgu] [abs].
* Diehl–Nagar 2019: soft-gluon decoupling via non-abelian Ward identities, generalizing CSS [Diehl:2018wfy] [abs]. TMD DPS [Buffing:2017mqm].
* Open issues per Diehl–Gaunt 2018 [txt §8 of Diehl:2017wew]:
  1. no all-order proof of the non-abelian Ward identities for DPS (subsequently addressed by Diehl–Nagar 2019);
  2. no general proof of the evolution equation of the soft matrix S (an all-order proof was "put forward" by Vladimirov [Vladimirov:2017ksc], but its applicability to their regulator was unclear);
  3. no general proof that S is positive semidefinite.
* MPI-sensitive observables: [Gaunt:2014ska].

**Tag.** **[A]** for double DY (colourless), at the level of single DY. **[C]** for DPS with coloured final states.

### Item 16 — Hard exclusive processes

* **Pion form factor.**
  * LO: $Q^2F_\pi(Q^2)=\frac{8\pi}{9}\alpha_s f_\pi^2\big|\int_0^1dx\,\phi_\pi(x)/x\big|^2[1+O(\alpha_s)]$, with $\int\phi_\pi=1$ and $f_\pi\simeq130$ MeV. The asymptotic DA $\phi=6x(1-x)$ gives $Q^2F_\pi\to8\pi\alpha_sf_\pi^2$, equivalently $16\pi\alpha_s f_\pi^2$ for $f_\pi\simeq93$ MeV. (Normalization of this LO formula: [bib]; I checked internal consistency.)
  * All-order factorization arguments: [Lepage:1979zb, Lepage:1980fj], [Efremov:1979qk, Efremov:1978rn], [Duncan:1979ny, Duncan:1979hi], [Chernyak:1977as, Chernyak:1983ej] [bib].
  * Criticism (endpoint and soft dominance at accessible $Q^2$): [Isgur:1984jm, Isgur:1988iw]. Sudakov-suppression framework: [Li:1992nu]. Wide-angle elastic scattering: [Landshoff:1974ew], [Botts:1989kf] [bib].
  * NNLO for the $\gamma^*\gamma\to\pi^0$ form factor: [Gao:2021iqq] [bib]. NLO and NNLO results for the EM pion form factor were not checked here (UNVERIFIED).
* **DVCS.**
  * [Ji:1996ek, Ji:1996nm], [Radyushkin:1996nd, Radyushkin:1997ki] [bib].
  * One loop: IR divergences "can be factorized entirely into off-forward parton distributions… We argue that this property persists to all orders" [Ji:1998xh] [abs].
  * Collins–Freund: "factorization holds for the DVCS amplitude in QCD, up to power suppressed terms, to all orders… the virtuality of the produced photon does not influence the general theorem" [Collins:1998be] [abs]. Collins 2011 §11.8 [txt TOC]. Reviews: [Diehl:2003ny], [Belitsky:2005qn].
* **Meson production.** CFS 1997: "We formulate and prove a QCD factorization theorem for hard exclusive electroproduction of mesons… valid for the leading power in Q and all logarithms" (longitudinal photon) [Collins:1996fb] [abs].
* **Transverse photons.** "QCD factorization cannot be applied as shown explicitly in a leading order calculation", with infrared-singular (endpoint) contributions [Mankiewicz:1999tt] [abs]. Phenomenology with $k_T$ modelling: [Goloskokov:2005sd]. SCET rederivations (π–γ form factor, DVCS): [Bauer:2002nz].
* **Tag.** **[A]** for $F_\pi$, the transition form factor, DVCS and $\gamma^*_L$ meson production. **[V]** for collinear factorization of $\gamma^*_T\to V_T$. **[C]/[P]** for the Sudakov/$k_T$ resummation scheme.

### Item 17 — SCET factorization proofs

* Founding papers:
  * [Bauer:2000ew] ($B\to X_s\gamma$ Sudakov logs); [Bauer:2000yr] (collinear and soft gluons; heavy-to-light); invariant operators [Bauer:2001ct].
  * "A proof of factorization for B → Dπ… to all orders in $\alpha_s$, up to corrections suppressed by factors of $1/m_b$, $1/m_c$, and $1/E_\pi$" [Bauer:2001cu] [abs].
  * Soft–collinear factorization at operator level [Bauer:2001yt] [abs].
  * Hard-scattering factorization (DIS, DY, DVCS, form factors), "proofs do not depend on the choice of a particular gauge" [Bauer:2002nz] [abs].
  * Position-space and multipole-expanded SCET, subleading currents [Beneke:2002ph, Beneke:2002ni] [bib].
* Zero-bin: [Manohar:2006nz]; relation to eikonal/soft subtractions [Lee:2006nr, Idilbi:2007ff] [bib].
* Event shapes: [Schwartz:2007ib], [Becher:2008cf], [Bauer:2008dt] ($e^+e^-$ event shapes with hadronic final states), [Fleming:2007qr, Fleming:2007xt] [bib].
* Amplitude-level hard–soft–collinear factorization "to all orders": [Feige:2013zla, Feige:2014wja] [bib]. Textbook: [Becher:2014oda].
* Assumptions: completeness of modes (method of regions, item 23), zero-bin subtractions, and absence or cancellation of Glauber contributions (Rothstein–Stewart 2016; TMD Handbook §3.5).
* Collins 2011 §15.9: "I have not been able to penetrate the SCET literature to properly understand its rationale" [txt p. 580].
* **Tag.** **[A]** ($e^+e^-$ dijet/thrust; B → Dπ at LP; DIS rederivation). Hadron-collider SCET theorems inherit the Glauber caveat.

### Item 18 — QCD factorization for charmless B decays (BBNS)

**Statement** (BBNS 2000 eq. (4) [txt]): up to $O(\Lambda/m_b)$,
$$\langle M_1M_2|O_i|\bar B\rangle=\sum_jF_j^{B\to M_1}(m_2^2)\int_0^1du\,T^I_{ij}(u)\Phi_{M_2}(u)+(M_1\leftrightarrow M_2)+\int d\xi\,du\,dv\,T_i^{II}(\xi,u,v)\Phi_B(\xi)\Phi_{M_1}(v)\Phi_{M_2}(u)$$
for two light mesons. For heavy $M_1$ and light $M_2$, only the first term remains.

**Who, where.**
* [Beneke:1999br]. [Beneke:2000ry]: general arguments, a two-loop proof for heavy–light, and "Some of the arguments… have straightforward extensions to all orders, but the following does not accomplish an all-order 'proof'"; "a considerable amount of conceptual work remains… proving the validity of the factorization formula to all orders… the two-loop proof for heavy-light final states… must be extended to… two light mesons" [txt §5, §8].
* [Beneke:2001ev] (πK, ππ; power-correction estimates with endpoint parameters); [Beneke:2003zv].
* NNLO: spectator scattering [Beneke:2005vv, Beneke:2006mk]; vertex corrections [Bell:2007tv, Bell:2009nk, Beneke:2009ek]; penguins [Bell:2015koa, Bell:2020qus]; heavy–heavy [Huber:2016xod] [bib].
* SCET: LP factorization theorem for B → M₁M₂ valid "even if $\alpha_s(E_M\Lambda)$ is not perturbative", with possible long-distance charming penguins at LO [Bauer:2004tj] [abs].
* Endpoint (NLP) refactorization exists for other processes: [Liu:2019oav, Liu:2020wbn] (h → γγ via b loop), [Liu:2022ajh] (gg → h), [Beneke:2022obx] (off-diagonal "gluon" thrust), [Beneke:2019mua], [Hurth:2023paz] ($\bar B\to X_s\gamma$, "prove a factorisation theorem… to all orders"), [Bell:2024bxg] (soft-overlap $B_c\to\eta_c$), [Beneke:2026miy] (NLP DIS, preprint). A novel leading-power contribution to pure weak-annihilation B decays is identified in [Lu:2022kos] [abs].
* INSPIRE searches (2026-10-09) found **no** completed endpoint refactorization of the BBNS power corrections (annihilation, twist-3 spectator) for B → ππ, πK.

**Tag.** **[P]**: leading power checked at one and two loops for charmless modes, not proven to all orders; power corrections not factorizable in the naive form (endpoint divergences). B → Dπ is **[A]** (item 17).

### Item 19 — NRQCD factorization

**Statements** (BBL [txt eqs. (2.14), (6.4)]):
$$\Gamma(H\to{\rm LH})=\sum_n\frac{2\,{\rm Im}f_n(\Lambda)}{M^{d_n-4}}\langle H|O_n(\Lambda)|H\rangle,\qquad \sigma(H)=\sum_n\frac{F_n(\Lambda)}{M^{d_n-4}}\langle0|O_n^H(\Lambda)|0\rangle.$$

**Who, where.**
* BBL 1995 (+ erratum PRD 55 (1997) 5853) [Bodwin:1994jh]. Their own assessment [txt §V–VI]:
  * The production arguments "are less rigorous than those that we have given for the factorization of the quarkonium annihilation rate… [whose] level of rigor is comparable to… deep-inelastic lepton-hadron scattering, which can be formulated in terms of the operator-product expansion". Production rigor is "comparable to… the Drell-Yan process".
  * For hadron collisions: "we will merely assume that the Glauber divergences cancel".
* NQS:
  * Uncancelled NNLO IR poles not matched by conventional NRQCD matrix elements. Octet production operators need Wilson lines; with them factorization is restored at NNLO. "infrared poles at yet higher orders may require… additional nonlocal operators" [Nayak:2005rw] [abs].
  * Fragmentation and gauge-completed matrix elements [Nayak:2005rt] [abs].
  * Consistency with NRQCD factorization to all orders in $v$ at NNLO [Nayak:2006fm] [abs].
* Phenomenology and tensions: [Butenschoen:2010rq, Butenschoen:2011yh, Butenschoen:2012px], [Chao:2012iv], fragmentation-based improvements [Kang:2011mg, Fleming:2012wy]; reviews [Brambilla:2010cs, Lansberg:2019adr] [bib].

**Tag.** **[A]** for inclusive annihilation decays (all orders in $\alpha_s$ to the order in $v$ considered). **[C]** for production in general, with **[P]** NNLO checks using gauge-completed operators.

### Item 20 — Small $x$: $k_T$ factorization, BFKL, BK/JIMWLK

* **High-energy ($k_T$) factorization.** [Catani:1990xk, Catani:1990eg], [Collins:1991ty], [Levin:1991ry]; DIS beyond LO [Catani:1994sq] [bib].
* **BFKL.** [Fadin:1975cb, Kuraev:1976ge, Kuraev:1977fs, Balitsky:1978ic]; NLL [Fadin:1998py, Ciafaloni:1998gs] [bib].
* **Non-linear evolution.** BK [Balitsky:1995ub, Kovchegov:1999yj]; JIMWLK [Jalilian-Marian:1997qno, Jalilian-Marian:1997jhx, Iancu:2000hn, Ferreiro:2001qy]; NLO BK [Balitsky:2007feb]; saturation and recombination [Gribov:1983ivg, Mueller:1985wy, McLerran:1993ni] [bib].
* Process dependence of unintegrated gluon distributions in the dense regime: [Dominguez:2011wm] [abs]. Factorization at low $x$ "shown to be preserved in the cases considered" [Milana:1986tq] [abs].
* CSS 1989: "factorization has been shown to hold explicitly in leading logarithms in x… factorization theorems need a more extensive examination in this region" [txt §10.3]. Collins 2011 §15.3.
* **Tag.** **[P]** ($k_T$ factorization: LL in $\ln1/x$, not a power-controlled theorem). **[A]** for BFKL/BK/JIMWLK as derivations within LL/NLL approximations (BK at large $N_c$). **[C]** for saturation-based factorization.

### Item 21 — Higher twist and twist 3

* **DIS twist 4.**
  * OPE-based (moments): as item 2.
  * $x$-space: transverse-basis methods [Ellis:1982wd, Ellis:1982cd] [abs]; canonical operators [Jaffe:1982pm]; multiparton distributions [Jaffe:1983hp] [abs]; [Qiu:1988dn] [abs].
* **Hadron–hadron at $1/Q^2$.** Generalized factorization [Qiu:1990xxa, Qiu:1990xy] [abs]; nuclear double scattering [Kastella:1989ux]. Fails beyond (item 8).
* **Twist 3 and single-spin asymmetries.**
  * [Efremov:1981sh, Efremov:1984ip]; Qiu–Sterman direct-photon SSA via a twist-3 quark–gluon correlation [Qiu:1991pp, Qiu:1991wg] [abs]; pions [Qiu:1998ia] [bib].
  * Twist-3 and TMD descriptions "describe the same physics in the kinematic region where they overlap" [Ji:2006ub] [abs].
  * NLO for the DY weighted SSA [Vogelsang:2009pj] [abs].
  * Evolution: [Braun:2009mi] "do not agree with the recent calculations" of [Kang:2008ey] [abs].
  * Sivers–$T_F$ "sign mismatch" [Kang:2011hk] [abs]; common-origin global analysis [Cammarota:2020qcw] [abs].
* No all-order proof of twist-3 collinear factorization for SSAs was found; existing checks are at one loop in specific processes.
* **Tag.** DIS twist 4 **[R]** (moment space, modulo item 1). Hadronic $1/Q^2$ **[A]**. Twist-3 SSA factorization **[P]** (and **[C]** for $pp\to\pi X$, coloured final state). Beyond $1/Q^2$ in hadron–hadron **[V]**.

### Item 22 — Renormalons

* 't Hooft's Erice lectures [tHooft:1977xjm]. Ambiguity of composite operators and the status of the OPE [David:1983gz, David:1985xj] [abs].
* Mueller 1985 on IR renormalons in IR-safe processes: "In the limit of zero current quark masses all non-perturbative corrections are found to vanish as $1/Q^4$ for certain infrared safe quantities" [Mueller:1984vh] [abs].
* NSVZ: an unambiguous OPE procedure via the normalization point μ in models [Novikov:1984rf] [abs].
* Review: [Beneke:1998ui]. Pole-mass renormalon: [Beneke:1994sw, Bigi:1994em] [bib].
* Numerical confirmation from the plaquette to $O(\alpha^{35})$: [Bali:2014fea] [bib]. Renormalon-based power corrections for quasi-PDFs: [Braun:2018brg] [abs].
* **Tag.** **[A]** (structure argued generally; exact in the large-β₀ approximation). **[C]** for a non-perturbative OPE.

### Item 23 — Method of regions

* Euclidean large-momentum and large-mass expansions are rigorous: [Smirnov:1990rz] [bib], [Smirnov:2002pj].
* Threshold expansion: [Beneke:1997zp] [abs]; [Smirnov:1998vk], [Smirnov:1999bza].
* Jantzen 2011: "a general proof for its correctness has still been missing. This paper shows how the expansion by regions manages to reproduce the exact result… clarifies the conditions on the choice and completeness of the considered regions… additional overlap contributions… may be needed depending on the choice of the regularization scheme" [Jantzen:2011nz] [abs].
* Geometric approach [Pak:2010pt]; potential and Glauber regions found automatically [Jantzen:2012mw] [abs]. SSS 2019: "make a conjecture that [the prescriptions] hold even in a much more general case. We prove this conjecture in some partial cases" [Semenova:2018cwy] [abs].
* On-shell expansion: regions ↔ Landau solutions ↔ Newton-polytope facets; commuting expansions proven for certain regions [Gardi:2022khw] [abs]. [Ananthanarayan:2018tog].
* **Tag.** **[R]** Euclidean; **[P]** Minkowski on-shell, threshold and Glauber expansions (proven in partial cases; widely conjectured). Collins 2011 ch. 10 replaces it with an explicit subtraction formalism.

### Item 24 — LaMET and pseudo-PDF factorization

**Statements** [txt eqs. (6), (12) of Izubuchi:2018srq]:
$$\tilde q(x,P^z,\mu_R)=\int_{-1}^1\frac{dy}{|y|}\,C\Big(\frac xy,\frac{\mu_R}{\mu},\frac{\mu}{|y|P^z}\Big)q(y,\mu)+O\Big(\frac{M^2}{P_z^2},\frac{\Lambda^2}{P_z^2}\Big),\qquad \mathcal P(x,z^2\mu_R^2)=\int\frac{dy}{|y|}\,\mathcal C\Big(\frac xy,\frac{\mu_R^2}{\mu^2},z^2\mu_R^2\Big)q(y,\mu)+O(z^2\Lambda^2,z^2M^2).$$

**Who, where.**
* [Ji:2013dva, Ji:2014gla] [bib]. IJJSZ: derivation from the OPE; quasi-PDFs and pseudo-PDFs obey equivalent factorization; the matching depends on the partonic momentum $|y|P^z$. The OPE is "proven for scalar field theory… widely assumed" for QCD [Izubuchi:2018srq] [abs, txt].
* Pseudo-PDFs and Ioffe-time distributions [Radyushkin:2017cyf, Radyushkin:2018cvn], [Orginos:2017kos].
* "Good lattice cross sections": the quasi-PDF factorizes "to all orders in perturbation theory if it can be multiplicatively renormalized" [Ma:2014jla, Ma:2017pxb] [abs].
* Multiplicative renormalizability to all orders, including power divergences [Ishikawa:2017faj] [abs] and via an auxiliary heavy-quark field [Ji:2017oey] [abs]; non-perturbative lattice renormalization [Green:2017xeu].
* Renormalon analysis: power corrections behave as $\Lambda^2/(p^2x^2(1-x))$ [txt eq. (69) of Braun:2018brg].
* Critiques: power-divergent mixing on the lattice [Rossi:2017muf]; an "obstruction to a direct Euclidean calculation" [Rossi:2018zkn] [abs].
* Reviews: [Ji:2020ect], [Constantinou:2020hdm].

**Tag.** **[A]** for the perturbative matching (OPE plus all-order renormalizability). Practical lattice implementation: **[C]/[P]** (inverse problem, power corrections near endpoints).

### Item 25 — Threshold resummation and refactorization

**Statement** (DY, $z=Q^2/\hat s\to1$; standard Mellin form):
$$\ln\Delta_N=\int_0^1dz\,\frac{z^{N-1}-1}{1-z}\Big[2\int_{\mu^2}^{(1-z)^2Q^2}\frac{dq^2}{q^2}A(\alpha_s(q^2))+D(\alpha_s((1-z)^2Q^2))\Big],\qquad A=\frac{C_F\alpha_s}{\pi}+\dots$$
(Form [bib]: Sterman 1987, Catani–Trentadue 1989. Check normalization conventions before transcribing.)

**Who, where.** [Sterman:1986aj], [Catani:1989ne, Catani:1990rp], [Korchemsky:1992xv], [Contopanagos:1996nh], [Kidonakis:1997gm]; SCET momentum-space resummation [Becher:2006nr, Becher:2006mr, Becher:2007ty] [bib]. NLP: LL threshold resummation of DY [Beneke:2018gvs] and Higgs [Beneke:2019mua]; endpoint factorization [Beneke:2022obx]; NLP DIS [Beneke:2026miy] (preprint) [abs].

**Tag.** **[A]** (LP refactorization); **[P]** (NLP beyond LL; endpoint issues are being resolved case by case).

### Item 26 — Non-global logarithms

* Discovery (single logs from $O(\alpha_s^2)$ for observables sensitive to restricted regions) and resummation at large $N_c$: [Dasgupta:2001sh, Dasgupta:2002bw] [bib].
* BMS equation [Banfi:2002hw]; finite $N_c$ [Weigert:2003mm, Hatta:2013iba]; link to BFKL [Caron-Huot:2015bja]; EFT factorization [Becher:2015hka, Becher:2016mmh] [bib].
* **Tag.** **[R]** for existence at fixed order (explicit); **[A]** for LL large-$N_c$ resummation; **[P]** beyond. Hadron collider: item 13.

### Item 27 — Heavy-quark schemes in DIS

* CWZ decoupling subtraction [Collins:1978wz]. AOT/ACOT [Aivazis:1993kh, Aivazis:1993pi] [abs]. Collins 1998: general proof with masses, remainder uniform in $M/Q$ [Collins:1998rz] [abs]. S-ACOT [Kramer:2000hn]; TR [Thorne:1997ga]; BMSN [Buza:1996wv]; FONLL [Forte:2010ta] [bib]. Collins 2011 §3.10–3.11, §11.7, §15.7 [txt TOC].
* Caveat for *hadron–hadron* collisions (not DIS): Collins 2011 §14.6 discusses calculations with massive incoming partons and massless gluons. It notes that factorization guarantees only the cancellation of IR divergences at leading power in $Q$, and that terms like $\frac{m^2}{Q^2}\times\frac1\epsilon$ can survive (cf. Catani–Ciafaloni–Marchesini 1986 [Catani:1985xt]). It concludes that preserving heavy-quark masses in the hard scattering "including the case of incoming quarks… is a bad idea" [txt pp. 569–570]. This does not contradict Collins 1998 (DIS, one hadron), but it matters when transferring ACOT-type schemes to hadron–hadron collisions.
* **Tag.** **[A]** for the theorem. The schemes are equivalent prescriptions to the order computed.

### Item 28 — Photoproduction and resolved photons

* Photon structure function, point-like part: [Witten:1977ju], NLO [Bardeen:1978hg] [bib]. OPE-based (photon target, PT): status as item 2, with a non-perturbative hadronic component.
* Direct versus resolved: review [Klasen:2002xb]. Collins 1998 conclusions [txt] (item 14): proof "would appear to apply" to direct photoproduction, not to resolved. HERA diffractive photoproduction breaks factorization [H1:2007jtx, ZEUS:2007uvk, Klasen:2008ah].
* Photon PDF of the proton from structure functions (LUXqed): determined "in a model-independent manner… as an integral over proton structure functions" [Manohar:2016nzj] [abs], [Manohar:2017eqh].
* **Tag.** **[A]** for direct photoproduction and $F_2^\gamma$; **[C]** for resolved (hadron–hadron-like, coloured final states); **[V]** for diffractive resolved.

### Item 29 — Nuclear PDFs and factorization in nuclei

* eA DIS is DIS on a hadron (items 2 and 6). pA → DY inherits item 8.
* Nuclear-enhanced twist 4, $\propto A^{1/3}/Q^2$: [Qiu:1990xxa, Qiu:1990xy], [Luo:1993ui, Luo:1994np], [Guo:1997it] (DY $q_T$ nuclear dependence) [bib]; double scattering [Kastella:1989ux].
* BBL 1981/1989: energy must exceed a scale growing with target length [abs].
* Leading-twist shadowing via Gribov theory and DDIS factorization [Frankfurt:2011cs] [bib]. Global nPDF fits assuming leading-twist factorization: [Eskola:2021nhw, Kovarik:2015cma, AbdulKhalek:2022fyi] [bib].
* **Tag.** **[A]** (inherits). Saturation-dominated small-$x$ regime in large nuclei **[C]**.

### Item 30 — Other essentials

1. **$e^+e^-\to hX$ and SIDIS with collinear FFs.** [Collins:1981uw]; cut vertices [Mueller:1978xu]; Collins 2011 §12.5–12.8 (gauge choice, sum over cuts, proof), §12.14 (SIDIS) [txt TOC]. **[A]**.
2. **Sudakov form factor.** All-order exponentiation [Mueller:1979ih, Collins:1980ih, Sen:1981sd, Magnea:1990zb], review [Collins:1989bt]; Collins 2011 ch. 10 (subtraction method) [bib]. **[A]**.
3. **IR singularities of massless multi-leg amplitudes.** Two-loop pole structure [Catani:1998bh] [abs]; [Sterman:2002qn]. Becher–Neubert proposed "an exact formula… valid at any number of loops", based on the conjecture that the soft anomalous-dimension matrix contains only one non-trivial colour structure, the dipole form [Becher:2009cu] [abs]; see also [Becher:2009qa], [Gardi:2009qi]. Almelid–Duhr–Gardi computed the complete three-loop correction to the dipole formula. "nondipole corrections appear already for three colored partons, where the correction is a constant"; kinematic dependence enters through conformal cross ratios for four or more coloured partons; and the term preserves strict (time-like) collinear factorization [Almelid:2015jia] [abs]. Tags: factorization of IR poles **[A]**; the dipole formula as an exact all-order statement **[V]** (fails at three loops).
4. **Amplitude-level hard–soft–collinear factorization.** Feige–Schwartz "prove it to all orders in perturbation theory" [Feige:2014wja] [abs]. Their formulation explicitly excludes configurations in which initial-state particles are collinear to final-state particles. With initial-state collinear particles, "unitarity-based arguments should still hold, even if they have not yet been rigorously proven"; general hadron–hadron scattering is not covered (threshold kinematics excepted) [txt §2, §7 of Feige:2014wja]. This is consistent with the space-like violation found by CdFR 2012 (item 13). **[A]** (outgoing or threshold kinematics).
5. **Colour-singlet production in hadron collisions** (W, Z, H, diboson): inherits DY, **[A]**.
6. **γ5 and polarized DIS scheme issues**: [Larin:1993tq] [bib].
7. **Fully unintegrated parton correlation functions**: [Collins:2007ph] [bib].

---

## 3. Cross-cutting findings for the monograph

### 3.1 Recommended corrections to OUTLINE v0 (also listed in the structured output)

1. **Ch5 "moment factorization [R in PT]".** The Euclidean OPE is rigorously proven for scalar theories (Zimmermann) and for gauge-invariant operators in pure YM (Hollands 2008). For QCD with quarks it is the standard extension (Collins 1984 §12.8: "proved… the same way"; IJJSZ 2018: "widely assumed"). Either footnote the [R] or use [A].
   The x-space corollary needs care. Moments determine distributions on $[0,1]$ (with only even moments, use Müntz–Szász or Carlson-type uniqueness for distributions), but moment-wise remainders give only weak convergence, not uniform-in-$x$ power corrections.
2. **Ch3 / App. D "Landau equations… proof in Feynman-parameter space".** Collins 2011 §5.4.3 and Collins 2020 (arXiv:2007.04085) show that the textbook and Feynman-parameter proofs are incomplete and use assumptions that are false for massless graphs. App. D should follow Collins 2020's momentum-space proof of necessity and sufficiency for physical-region pinches, citing it as a preprint (no journal record on INSPIRE as of 2026-10-09).
3. **Ch8 DIS [A].** State Collins' explicit gap (§11.3.2): the BRST classification for non-local operators is assumed. Cite Collins–Rogers 2008 for the K-gluon remainder.
4. **Ch10 Drell–Yan.** Base the Glauber cancellation on Collins 2011 §14.3–14.4 (CSS 1988 "with important improvements and correction of errors"; CSS 1988 supersedes Bodwin 1985 and CSS 1985) and DGOPS 2016 §4 (LCPT all-order proof, with clarifications). Quote §14.4.8 "Issues remaining" in the honest-gaps discussion.
5. **Ch10 "other hadron–hadron processes".** High-$p_T$ hadrons and jets and heavy-quark production should be tagged **[C]**, not [A] (Collins §14.7; DGOPS 2016; CSS 1986 "conjecture"; CdFR 2012 N3LO issue). Colour-singlet production (W, Z, H) stays [A].
6. **Ch12.** Add the following as [V] or disputed items: Gaunt 2014 and Zeng 2015 (jet-veto, beam-thrust and $E_T$ observables); Schwartz–Yan–Zhu 2018 (partial rebuttal); FSS 2012 (three-loop violation for non-inclusive observables). Add the SLL developments (Becher–Neubert–Shao 2021, BNSS 2023, "Factorization restoration through Glauber gluons" PRL 2025, Banfi–Forshaw–Holguin PRL 2026).
7. **Ch11 Sivers.** "[R] given factorization" is correct. Experimental status: consistent (COMPASS 2017, 2024; STAR 2016 favours it if evolution effects are small) but not decisive (BPV 2021 cannot exclude the same sign; EKT 2021 tension with W/Z data).
8. **Ch16 LaMET/pseudo-PDF.** Use [A] for the perturbative matching, and mention the $x$-dependence of the power corrections, $\Lambda^2/(P_z^2x^2(1-x))$ (BVZ 2019), and the Rossi–Testa critique.
9. **Collins' book "and any later edition".** There is no revised edition. The 2023 version is an Open Access *reissue* ("First published 2011, Reissued as OA 2023"; DOI 10.1017/9781009401845; ISBN 978-1-009-40183-8 hb, 978-1-009-40182-1 pb). The same holds for *Renormalization* (DOI 10.1017/9781009401807). Note that INSPIRE now attaches the OA DOI to the 2011 record.
10. **Overview table (Ch1, Ch17).** Under the binding [R] definition, only a handful of statements qualify: IR finiteness of $R_{e^+e^-}$ and of Euclidean Green functions; the OPE for φ⁴ and pure YM; DGLAP from operator renormalization; support properties in PT; the Sivers sign change *given* the definitions; the Euclidean method of regions. Almost every factorization theorem proper is [A] or weaker.

### 3.2 Transcription hazards (see §0.3)
These are the sign of $g$ in Collins, the sign of the Fourier exponent in Collins' TMD formulas, and the plus-prescription in $P_{gg}$.

### 3.3 Open problems (for Ch17)
1. A complete proof of the Glauber cancellation for coloured final states (single-inclusive hadrons and jets).
2. The BRST classification for non-local light-ray operators (Collins §11.3.2).
3. An SCET factorization proof including $\mathcal L_G$ (announced by Rothstein–Stewart, not yet published).
4. Mass-singularity factorization at N3LO in the presence of space-like collinear violation (CdFR 2012).
5. A published, refereed proof of the Landau criterion for massless graphs (Collins 2020 is a preprint).
6. Positivity of $\overline{\rm MS}$ PDFs.
7. Endpoint factorization for B → ππ power corrections.
8. NRQCD production factorization beyond NNLO.
9. A general proof of the method of regions in Minkowski kinematics.
10. A non-perturbative status for the OPE and factorization.

---

## 4. Bibliography

All keys used above are in `survey_refs.bib` (415 entries; INSPIRE BibTeX plus three manual entries). Per-item key lists follow; the full label→key table with journal/arXiv/DOI is `verified_refs_table.tsv`.

* **Item 1.** Wilson:1969zs, Zimmermann:1972te, Zimmermann:1972tv, Zimmermann:1970Brandeis, Wilson:1972ee, Brandt:1970kg, Frishman:1970fx, Frishman:1971qn, Christ:1972ms, Anikin:1978tj, Zavyalov:1990kv, Callan:1973pu, Coleman:1973sx, Joglekar:1975nu, Joglekar:1976eb, Joglekar:1976pe, Kluberg-Stern:1974iel, Kluberg-Stern:1974nmx, Kluberg-Stern:1975ebk, Henneaux:1993jn, Collins:1994ee, Collins:1984xc, Hollands:2011gf, Holland:2014pna, Hollands:2006ag, Hollands:2007zg, Frob:2015uqy, Novikov:1984rf, Shifman:1978bx, David:1983gz, David:1985xj, Balitsky:1987bk, Muller:1994ses, Izubuchi:2018srq
* **Item 2.** Gross:1973id, Politzer:1973fx, Gross:1973ju, Gross:1973zrg, Georgi:1974wnj, Gribov:1972ri, Gribov:1972rt, Lipatov:1974qm, Altarelli:1977zs, Dokshitzer:1977sg, Floratos:1977au, Curci:1980uw, Furmanski:1980cm, Moch:2004pa, Vogt:2004mw, Collins:1981uw
* **Item 3.** Bloch:1937pw, Kinoshita:1962ur, Lee:1964is, Sterman:1976jh, Sterman:1978bi, Sterman:1978bj, Sterman:1977wj, Sterman:1979uw, Ore:1979ry, Poggio:1976qr, Poggio:1975af, Lowenstein:1975rg, Lowenstein:1975ps, Lowenstein:1974qt, Breitenlohner:1975hg, Breitenlohner:1976te, Weinberg:1959nj, Hahn:1968HZ, Doria:1980ak, DiLieto:1980nkq, Andrasi:1980qw, Frenkel:1983di, Catani:1985xt, Frye:2018xjj, Collins:1987pm
* **Item 4.** Landau:1959fi, Nakanishi:1959jzx, Cutkosky:1960sp, Coleman:1965xm, Eden:1966dnq, Pham:2011SingInt, Collins:2020euz, Muhlbauer:2020kut, Fevola:2023kaw, Sterman:1993hfp
* **Item 5.** Libby:1978qf, Libby:1978bx, Labastida:1984gy, Gardi:2022khw, Ma:2023hrt, Sterman:1995fz, Collins:1989gx, Collins:2011zzd
* **Item 6.** Ellis:1978sf, Ellis:1978ty, Amati:1978wx, Amati:1978by, Mueller:1978xu, Mueller:1981sg, Collins:1981ta, Collins:2008sg, Collins:1998rz
* **Item 7.** Soper:1976jc, Soper:1979fq, Jaffe:1983hp, Diehl:1998sm, Candido:2020yat, Collins:2021vke, Candido:2023ujx, Altarelli:1998gn, Collins:2003fm
* **Item 8.** Bodwin:1984hc, Collins:1985ue, Collins:1988ig, Collins:1981tt, Collins:1982wa, Collins:1983ju, Bodwin:1981fv, Bodwin:1988fs, Lindsay:1982pu, Lindsay:1982gd, Brandt:1988xt, Aybat:2008ct, Diehl:2015bca, Rothstein:2016bsq, Boussarie:2023izj, Qiu:1990xxa, Qiu:1990xy, Basu:1984ba, Gaunt:2014ska, Zeng:2015iba, Schwartz:2018obd, Bodwin:1994jh
* **Item 9.** Nayak:2005rt, Nayak:2005rw, Catani:2011st, Collins:1985gm, Kang:2016mcy
* **Item 10.** Collins:1981uk, Collins:1981va, Collins:1984kg, Meng:1995yn, Nadolsky:1999kb, Ji:2004wu, Ji:2004xq, Ji:2005nu, Becher:2010tm, Echevarria:2011epo, Echevarria:2012js, Chiu:2011qc, Chiu:2012ir, Collins:2017oxh, Collins:1999dz, Duhr:2022yyp, Moult:2022xzt, Vladimirov:2017ksc
* **Item 11.** Collins:2002kn, Collins:1992kk, Brodsky:2002cx, Brodsky:2002rv, Ji:2002aa, Belitsky:2002sm, Boer:2003cm, Sivers:1989cc, Sivers:1990fh, HERMES:2009lmz, HERMES:2020ifk, COMPASS:2017jbv, COMPASS:2023vqt, STAR:2015vmv, STAR:2023jwh, Bury:2020vhj, Echevarria:2020hpy
* **Item 12.** Collins:2007nk, Collins:2007jp, Rogers:2010dm, Bomhof:2004aw, Bomhof:2006dp, Vogelsang:2007jk, Rogers:2013zha
* **Item 13.** Forshaw:2012bi, Forshaw:2006fk, Forshaw:2008cq, Becher:2021zkk, Becher:2023mtx, Boer:2024hzh, Becher:2024nqc, Becher:2024kmk, Banfi:2025mra, Dixon:2019lnw
* **Item 14.** Collins:1997sr, Berera:1994xh, Berera:1995fj, Trentadue:1993ka, Ingelman:1984ns, Landshoff:1971zu, Henyey:1974zs, Cardy:1974vq, DeTar:1974vx, Collins:1992cv, CDF:1997gvd, CDF:2000rua, CDF:2012nhl, Alvero:1998ta, H1:2006zyl, H1:2007jtx, ZEUS:2007uvk, Klasen:2008ah, CMS:2012odd, Bjorken:1992er
* **Item 15.** Diehl:2011yj, Diehl:2017kgu, Diehl:2018wfy, Buffing:2017mqm, Manohar:2012jr, Manohar:2012pe, Blok:2011bu, Gaunt:2009re, Diehl:2018kgr, Diehl:2017wew
* **Item 16.** Lepage:1979zb, Lepage:1980fj, Efremov:1979qk, Efremov:1978rn, Duncan:1979ny, Duncan:1979hi, Chernyak:1977as, Chernyak:1983ej, Collins:1996fb, Ji:1996ek, Ji:1996nm, Radyushkin:1996nd, Radyushkin:1997ki, Ji:1998xh, Collins:1998be, Mankiewicz:1999tt, Goloskokov:2005sd, Li:1992nu, Botts:1989kf, Isgur:1984jm, Isgur:1988iw, Landshoff:1974ew, Diehl:2003ny, Belitsky:2005qn, Gao:2021iqq
* **Item 17.** Bauer:2000ew, Bauer:2000yr, Bauer:2001ct, Bauer:2001cu, Bauer:2001yt, Bauer:2002nz, Beneke:2002ph, Beneke:2002ni, Manohar:2006nz, Lee:2006nr, Idilbi:2007ff, Bauer:2008dt, Becher:2008cf, Schwartz:2007ib, Fleming:2007qr, Fleming:2007xt, Feige:2013zla, Feige:2014wja, Becher:2014oda
* **Item 18.** Beneke:1999br, Beneke:2000ry, Beneke:2001ev, Beneke:2003zv, Bauer:2004tj, Beneke:2005vv, Beneke:2006mk, Bell:2007tv, Bell:2009nk, Beneke:2009ek, Bell:2015koa, Bell:2020qus, Huber:2016xod, Liu:2019oav, Liu:2020wbn, Liu:2022ajh, Beneke:2019mua, Beneke:2022obx, Hurth:2023paz, Lu:2022kos, Bell:2024bxg, Beneke:2026miy
* **Item 19.** Nayak:2006fm, Butenschoen:2010rq, Butenschoen:2011yh, Butenschoen:2012px, Chao:2012iv, Kang:2011mg, Fleming:2012wy, Brambilla:2010cs, Lansberg:2019adr
* **Item 20.** Catani:1990xk, Catani:1990eg, Collins:1991ty, Levin:1991ry, Catani:1994sq, Fadin:1975cb, Kuraev:1976ge, Kuraev:1977fs, Balitsky:1978ic, Fadin:1998py, Ciafaloni:1998gs, Balitsky:1995ub, Kovchegov:1999yj, Jalilian-Marian:1997qno, Jalilian-Marian:1997jhx, Iancu:2000hn, Ferreiro:2001qy, Balitsky:2007feb, Gribov:1983ivg, Mueller:1985wy, McLerran:1993ni, Dominguez:2011wm, Milana:1986tq
* **Item 21.** Ellis:1982wd, Ellis:1982cd, Jaffe:1982pm, Qiu:1988dn, Kastella:1989ux, Efremov:1981sh, Efremov:1984ip, Qiu:1991pp, Qiu:1991wg, Qiu:1998ia, Ji:2006ub, Vogelsang:2009pj, Braun:2009mi, Kang:2008ey, Kang:2011hk, Cammarota:2020qcw
* **Item 22.** tHooft:1977xjm, Mueller:1984vh, Beneke:1998ui, Beneke:1994sw, Bigi:1994em, Bali:2014fea, Braun:2018brg
* **Item 23.** Beneke:1997zp, Smirnov:1998vk, Smirnov:1999bza, Smirnov:1990rz, Smirnov:2002pj, Pak:2010pt, Jantzen:2011nz, Jantzen:2012mw, Semenova:2018cwy, Ananthanarayan:2018tog
* **Item 24.** Ji:2013dva, Ji:2014gla, Radyushkin:2017cyf, Orginos:2017kos, Radyushkin:2018cvn, Ma:2014jla, Ma:2017pxb, Ishikawa:2017faj, Ji:2017oey, Green:2017xeu, Rossi:2017muf, Rossi:2018zkn, Ji:2020ect, Constantinou:2020hdm
* **Item 25.** Sterman:1986aj, Catani:1989ne, Catani:1990rp, Korchemsky:1992xv, Contopanagos:1996nh, Kidonakis:1997gm, Becher:2006nr, Becher:2006mr, Becher:2007ty, Beneke:2018gvs
* **Item 26.** Dasgupta:2001sh, Dasgupta:2002bw, Banfi:2002hw, Weigert:2003mm, Hatta:2013iba, Caron-Huot:2015bja, Becher:2015hka, Becher:2016mmh
* **Item 27.** Collins:1978wz, Aivazis:1993kh, Aivazis:1993pi, Kramer:2000hn, Thorne:1997ga, Buza:1996wv, Forte:2010ta
* **Item 28.** Witten:1977ju, Bardeen:1978hg, Klasen:2002xb, Manohar:2016nzj, Manohar:2017eqh
* **Item 29.** Luo:1993ui, Luo:1994np, Guo:1997it, Frankfurt:2011cs, Eskola:2021nhw, Kovarik:2015cma, AbdulKhalek:2022fyi
* **Item 30.** Mueller:1979ih, Collins:1980ih, Sen:1981sd, Magnea:1990zb, Collins:1989bt, Catani:1998bh, Sterman:2002qn, Becher:2009cu, Becher:2009qa, Gardi:2009qi, Almelid:2015jia, Larin:1993tq, Collins:2007ph
