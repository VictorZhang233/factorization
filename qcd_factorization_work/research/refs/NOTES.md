# Verified bibliography: QCD factorization monograph — NOTES

Directory: `research/refs/`. Files:

- **`refs.bib`** (203 entries): BibTeX. Readable keys; INSPIRE texkey in the non-standard field `inspire`, erratum DOI in `erratumdoi` (standard styles ignore both).
- **`refs_bibitems.tex`**: the same 203 entries rendered in the house style of `furry_qcd.tex` (`\bibitem{Key}` A.~B.~Author, \emph{Title}, Journal~\textbf{vol} (year) \mbox{pages}, arXiv link). The current preamble uses `thebibliography`, not BibTeX, so this file can be pasted in directly. It is grouped by topic; reorder it by first citation when the chapters are assembled.
- **`NOTES.md`**: this file. It has one line per entry: the key, what the reference contains or is used for in the outline, and where it was verified.

## Verification method (2026-10-09)

1. **INSPIRE-HEP REST API**: one query per entry (journal reference, arXiv ID or record ID). Each query had to return exactly 1 record, and I checked authors, title, journal, volume, first page, year, DOIs, arXiv ID and texkeys against what I expected. The scripts and raw JSON are kept outside the deliverable directory.
2. **Crossref REST API**: every DOI in the INSPIRE records (197 DOIs, including 8 errata) was fetched. The publisher metadata (title, authors, volume, page range, issue date) was compared with INSPIRE field by field.
3. **arXiv API**: all 80 arXiv IDs. I compared titles and authors, and also the journal-ref where one exists.
4. **DOI handle API** (`doi.org/api/handles`): all 197 DOIs printed in `refs.bib` resolve (responseCode 1).
5. **Additional sources where INSPIRE and Crossref were insufficient or disagreed**:
   - CUP Core pages, Crossref book records and Open Library for the books;
   - the JETP archive (jetp.ras.ru) for the Sov. Phys. JETP entries: Sudakov, Landau, Kuraev–Lipatov–Fadin, Dokshitzer;
   - DataCite for the CERN Yellow Report;
   - OpenAlex and Semantic Scholar as tie-breakers for page ranges (Slavnov, Balitsky) and for the CFP 1980 title.

**Policy:**
- Titles are given as published, from the publisher (Crossref) record, with MathML converted to LaTeX.
- Author lists follow INSPIRE's curated names, with two adjustments: forms of the same person are made consistent (e.g. `Ji, Xiangdong`, `Collins, John C.`), and diacritics present in the publisher byline but stripped by INSPIRE are restored (Schäfer, Siódmok, Echevarría).
- Lists with more than 10 authors are given as first author + `others`.
- Page ranges are printed only when the publisher (Crossref) confirms them; otherwise only the first page is given.
- For Soviet journals, the English translation is the main reference and the Russian original goes in brackets.
- Errata are appended as `[Erratum: …]`, and each erratum was itself verified on Crossref.
- **Anything I could not verify was omitted.** The only gap is the page range of Zimmermann's 1970 Brandeis lectures, which is therefore left out.

**Key scheme:** `<Surname1><Surname2><Surname3><Year>[a|b|c]` for up to 3 authors, and `<FirstSurname>EtAl<Year>[a|b]` for 4 or more. The year is the journal (publication) year, not the arXiv year. Example: `AybatSterman2009`, which the task list calls "Aybat–Sterman 2008".

Common names → keys:
- BBNS → `BenekeEtAl1999/2000/2001`; BCDF → `BenekeEtAl2002`
- BFPS → `BauerEtAl2001`; BFPRS → `BauerEtAl2002`
- BBL (NRQCD) → `BodwinBraatenLepage1995`; BBL (Drell–Yan) → `BodwinBrodskyLepage1981`
- CSS → `CollinsSoperSterman1983/1985a/1985b/1988/1989`
- EGMPR → `EllisEtAl1979`; BBDM → `BardeenEtAl1978`; ACOT → `AivazisEtAl1994`
- CJNR → `ChiuEtAl2012a/b`; CTTW → `CataniEtAl1993`
- CTEQ handbook → `StermanEtAl1995`; TMD Handbook → `BoussarieEtAl2023`
- KLF / BL (BFKL) → `KuraevLipatovFadin1977`, `BalitskyLipatov1978`

## Reproduce the verification

The scripts are in `tools/` (Python 3 standard library only; network access needed):
`spec.py` is the candidate list with expected fields; `fetch.py` pulls INSPIRE/Crossref/arXiv; `analyze.py` cross-checks them;
`generate.py` writes the outputs (books, chapters and errata are hand-entered there with their sources); `audit.py` re-checks a finished `refs.bib` against Crossref.
Keep downloads outside the source tree, e.g.

    python3 -I tools/fetch.py    tools/spec.py /tmp/bibdl
    python3 -I tools/analyze.py  tools/spec.py /tmp/bibdl /tmp/analysis.json
    python3 -I tools/generate.py tools/spec.py /tmp/analysis.json /tmp/bibout
    python3 -I tools/audit.py    refs.bib /tmp/bibdl

**Test builds:**
- `refs.bib` + `\nocite{*}` + `unsrt` under XeLaTeX/BibTeX: 203 items, no BibTeX warnings, no LaTeX errors.
- `refs_bibitems.tex` inside the monograph preamble (`common/preamble_fact.tex`, ctexbook/XeLaTeX): no errors, no undefined citations, no missing glyphs, no overfull boxes.

## Corrections and discrepancies found (relative to the task list, INSPIRE, or common citation habits)

1. **Collins, "later edition": there is no second edition.** The 2023 CUP item (DOI 10.1017/9781009401845) is an *Open Access reissue* of the 2011 book. The CUP page says: "First published in 2011, this title has been reissued as an Open Access publication". Crossref gives edition-number 1. It is kept as a separate entry `Collins2023`. I did not compare its pagination with the 2011 printing, so cite `Collins2011` for equation and page numbers.
2. **Qiu–Sterman, Nucl. Phys. B 378 (1992) 52 is about *direct-photon* production, not pion production.** The pion-production paper is Phys. Rev. D 59 (1999) 014004 (hep-ph/9806356, INSPIRE Qiu:1998ia). It is verified but not included.
3. **Sen 1983:** the published title says "*fixed-angle*" on-shell quark scattering amplitudes. INSPIRE has "wide angle".
4. **Di'Lieto–Gendron–Halliday–Sachrajda 1981:** the title is "A counter example to the Bloch–Nordsieck theorem in non-abelian gauge theories", not "…proposal". Doria–Frenkel–Taylor 1980: "Counter-example to non-abelian Bloch–Nordsieck *conjecture*", whereas INSPIRE has "…Theorem".
5. **INSPIRE end-page errors:**
   - Slavnov, Theor. Math. Phys. 10 is pp. 99–104. INSPIRE says 99–107; Crossref, OpenAlex and Semantic Scholar agree on 104.
   - Balitsky, Nucl. Phys. B 463 is pp. 99–157. INSPIRE says 99–160.
6. **INSPIRE's BibTeX export for Bodwin 1985 puts the erratum DOI (10.1103/PhysRevD.34.3932) in the `doi` field.** Do not paste INSPIRE BibTeX blindly. The main DOI is 10.1103/PhysRevD.31.2616.
7. **Landau 1959:** INSPIRE labels Nucl. Phys. 13 (1959) 181 as a "reprint". It is the standard citation; Crossref confirms pp. 181–192. The JETP 10 (1960) 45 version is given as "see also".
8. **CTEQ handbook (Rev. Mod. Phys. 67 (1995) 157–248):**
   - The publisher's author order starts with G. Sterman (17 authors). INSPIRE lists the authors alphabetically from Brock.
   - The published title is "Handbook of perturbative QCD", without the preprint's "Version 1.0".
9. **Publisher titles that differ from INSPIRE / preprint titles**, used here in the published form:
   - Farhi 1977: "Quantum Chromodynamics Test for Jets".
   - Poggio–Quinn–Weinberg 1976: "Smearing method in the quark model".
   - Isgur–Llewellyn Smith 1984: "Asymptotic $Q^2$ for Exclusive Processes in Quantum Chromodynamics". INSPIRE carries the preprint title "Asymptopia…".
   - Rogers–Mulders 2010: "No generalized transverse momentum dependent factorization in the hadroproduction…".
   - Nayak–Qiu–Sterman 2005b and 2006: "nonrelativistic QCD" spelled out.
   - Efremov–Teryaev 1985: "…polarized hadron structure function measurement".
   - Bogoliubov–Parasiuk 1957: German original "Über die Multiplikation der Kausalfunktionen…". The printed author spelling is "Bogoliubow".
   - Curci–Furmanski–Petronzio 1980: "…: The non-singlet case". Here Crossref *truncates* the subtitle; INSPIRE, Semantic Scholar and the literature agree on the full title.
10. **Years differ from naive expectations in some entries:**
    - Aybat–Sterman: Phys. Lett. B 671 (**2009**) 46; the arXiv version is from 2008.
    - Bauer–Fleming–Luke: Phys. Rev. D 63 (**2000**) 014006. Crossref and INSPIRE both give 2000, although the issue is dated January 2001.
    - Collins 1998 erratum: Phys. Rev. D 61 (2000) 019902, published online December 1999.
    - Muta, 3rd ed.: catalogues and INSPIRE give 2010; Crossref's print date is Sept. 2009.
11. **Ambiguous items in the task list. I chose the following; verified alternatives are noted for the lead author:**
    - "'t Hooft 1971": Nucl. Phys. B 33 (1971) 173 (massless Yang–Mills; Ward identities). Alternative: Nucl. Phys. B 35 (1971) 167, "Renormalizable Lagrangians for massive Yang–Mills fields".
    - "Zimmermann 1973": Ann. Phys. 77 (1973) 570, the short-distance expansion. Companion paper: Ann. Phys. 77 (1973) 536, "Composite operators in the perturbation theory of renormalizable interactions".
    - "Efremov–Radyushkin 1980": Phys. Lett. B 94 (1980) 245. Alternative: Theor. Math. Phys. 42 (1980) 97, "Asymptotical behavior of pion electromagnetic form-factor in QCD".
    - "Radyushkin 1997": Phys. Rev. D 56 (1997) 5524. Earlier letter: Phys. Lett. B 380 (1996) 417, "Scaling limit of deeply virtual Compton scattering".
    - "Ji–Ma–Yuan 2005": Phys. Rev. D 71 (2005) 034005 (SIDIS). Companion: Phys. Lett. B 597 (2004) 299 (spin-dependent DIS and DY).
    - "Beneke–Braun 1995": both 1995 papers are included (large-$\beta_0$; DY renormalons).
    - "Qiu–Sterman 1991/1992": four papers are included (two on power corrections, two on twist-3 single-spin asymmetries).
    - "Libby–Sterman 1978", "Sterman 1978", "Amati–Petronzio–Veneziano 1978", "Shifman–Vainshtein–Zakharov 1979", "Gribov–Lipatov 1972" and "Gross–Wilczek 1973": all parts are included.
    - "Becher et al. SCET lectures" = Lect. Notes Phys. 896 (2015). "Boer et al." = arXiv:1108.1713 (INT report, unpublished). "Gelis et al." = Annu. Rev. Nucl. Part. Sci. 60 (2010) 463. Quarkonium reviews: Brambilla et al. 2011 (Eur. Phys. J. C) and 2005 (CERN Yellow Report). The TMD Handbook (arXiv:2304.03302, no journal publication in INSPIRE) is added.
12. **Preprints with no journal publication** (INSPIRE, 2026-10): Collins 2007 (arXiv:0708.4410, 8 pages), the TMD Handbook, and Boer et al. 2011. They are cited as arXiv/report.
13. **Zimmermann 1970 (Brandeis lectures).** Verified: INSPIRE proceedings record 1375392 (eds. Deser, Grisaru, Pendleton; MIT Press 1970), Open Library, and catalogue contents showing the title in Vol. 1. INSPIRE has no record for the lecture itself. The page range often quoted could not be verified and is omitted.
14. **Soviet-journal end pages are INSPIRE-only.** Only first pages are printed for Gribov–Lipatov, Balitsky–Lipatov, Dokshitzer, Kuraev–Lipatov–Fadin and Sudakov. The Russian originals of Gribov–Lipatov, Balitsky–Lipatov and Slavnov are INSPIRE-only; those of Dokshitzer, KLF and Sudakov are confirmed by the JETP archive.
15. **Count:** 203 entries, slightly above the 120–200 target. If a hard cap of 200 is needed, the first candidates to drop are `Farhi1977`, `HambergVanNeervenMatsuura1991` and `BrandtNeriSato1981`.

## Entries (key — content / use in the outline — verification source)

## Textbooks and monographs (13)

- `Collins2011` — Foundations of Perturbative QCD: standard all-orders treatment of regions, subtractions, Ward identities, collinear and TMD factorization (Ch. 3, 6-8, 10-12). — **Verified:** Crossref 10.1017/CBO9780511975592 (CUP, 2011; ISBNs 9780521855334/9781107645257); CUP Core page (Series Number 32; pp. i-624); INSPIRE 922696; Open Library (xii+624 p.)
- `Collins2023` — Open-Access reissue (2023) of Collins2011 by CUP; not a new edition. — **Verified:** Crossref 10.1017/9781009401845 (online 2023-07-13; print 2023-07-27; edition-number 1); CUP Core page: "First published in 2011, this title has been reissued as an Open Access publication" (CC-BY-NC-ND 4.0, 638 pp.). NOT a second edition; pagination vs 2011 not compared
- `Sterman1993` — An Introduction to Quantum Field Theory: Landau equations, pinch surfaces, power counting, IR safety, factorization (Ch. 3, 7). — **Verified:** Crossref 10.1017/CBO9780511622618 (CUP, 1993-08-26; ISBNs 9780521311328/9780521322584); INSPIRE 375196; Open Library (xvii+572 p.)
- `EllisStirlingWebber1996` — QCD and Collider Physics: one-loop DIS/DY/e+e- calculations, splitting functions, phenomenology (Ch. 4, 5, 8, 10). — **Verified:** Crossref 10.1017/CBO9780511628788 (CUP, 1996-10-24); INSPIRE 328604 (series vol. 8, 435 p.); Open Library (series 8; xiv+435 p.)
- `Muta2010` — Foundations of QCD (3rd ed.): renormalization, RG, OPE and DIS moments in perturbation theory (Ch. 2, 5). — **Verified:** Crossref 10.1142/6766 (edition 3; series WS Lecture Notes in Physics; print date 2009-09); INSPIRE 1330235 (2010, vol. 78); Open Library (3rd ed., 2010, v. 78, xvi+409 p.). Year: catalogues give 2010, Crossref print date Sept 2009
- `Field1989` — Applications of Perturbative QCD: explicit O(alpha_s) calculations for e+e-, DIS, DY in dimensional regularization (Ch. 4, 8, 10). — **Verified:** INSPIRE 287536 (Front. Phys. 77, 366 p.); Open Library ISBN 0201142953 (Addison-Wesley Advanced Book Program, Redwood City, 1989, xviii+366 p., Frontiers in Physics v. 77). No DOI
- `PeskinSchroeder1995` — QFT textbook; source of the binding conventions D_mu = d_mu - i g A_mu^a t^a and Feynman rules; parton model / DGLAP chapters (Ch. 2). — **Verified:** INSPIRE 407703 (Addison-Wesley, Reading 1995; ISBN 9780201503975); Open Library (xxii+842 p.). Later CRC reprint DOI 10.1201/9780429503559 (2018) not cited
- `Weinberg1996` — The Quantum Theory of Fields II: OPE, RG, asymptotic freedom, BRST/Ward identities (Ch. 2, 5). — **Verified:** Crossref 10.1017/CBO9781139644174 (CUP, 1996-08-13; ISBN 9780521550024); INSPIRE 430948 (Vol. 2: Modern applications); Open Library (3 v.)
- `Smirnov2002` — Applied Asymptotic Expansions in Momenta and Masses: asymptotic expansions of Feynman integrals, expansion by regions (Ch. 3). — **Verified:** Crossref 10.1007/3-540-44574-9 (Springer Tracts in Modern Physics; print 2002, online 2001-06-11); INSPIRE 582124 (vol. 177, 262 p.)
- `BecherBroggioFerroglia2015` — Introduction to Soft-Collinear Effective Theory: modes, Lagrangian, decoupling, Sudakov form factor, DY/thrust factorization (Ch. 14). — **Verified:** Crossref 10.1007/978-3-319-14848-9 (Springer, Cham, 2015, Lecture Notes in Physics); INSPIRE 1320996 (Lect. Notes Phys. 896); arXiv:1410.1892
- `KovchegovLevin2012` — Quantum Chromodynamics at High Energy: BFKL, dipole picture, BK/JIMWLK, saturation (Ch. 12). — **Verified:** Crossref 10.1017/CBO9781139022187 (CUP, 2012-08-30); INSPIRE 1217905 (series vol. 33); Open Library (series 33). (A 2022 CUP reissue has DOI 10.1017/9781009291446)
- `Collins1984` — Renormalization: BPHZ, dimensional regularization, RG and OPE (incl. proof sketch of OPE) (Ch. 2, 5, 7). — **Verified:** Crossref 10.1017/CBO9780511622656 (CUP, 1984-11-15; subtitle as given); CUP Core page (series name; OA reissue 2023 DOI 10.1017/9781009401807); INSPIRE 209810. Series number (26 in INSPIRE only) omitted
- `EdenEtAl1966` — The Analytic S-Matrix: Landau singularities, Cutkosky rules, physical-region analyticity (Ch. 3, App. D). — **Verified:** INSPIRE 1517084 (CUP, Cambridge 1966); Open Library (CUP 1966, 295 p.); 1967 reviews in Am. J. Phys./Science (Crossref). No DOI

## Reviews (12)

- `StermanEtAl1995` — CTEQ Handbook of perturbative QCD (RMP version; preprint was 'Version 1.0'): concise reference for factorization, DIS/DY/jets conventions (Ch. 1). — **Verified:** INSPIRE 357192 (CTEQ:1993hwr, Brock:1993sz); Crossref 10.1103/RevModPhys.67.157 (vol 67, p. 157-248, 1995); author order per publisher (Crossref: Sterman, Smith, Collins, Whitmore, Brock, ...; 17 authors); INSPIRE lists alphabetically from Brock; title per publisher (INSPIRE adds "Version 1.0")
- `Diehl2003` — Generalized parton distributions: comprehensive review (definitions, evolution, DVCS, factorization) (Ch. 13). — **Verified:** INSPIRE 624706 (Diehl:2003ny); Crossref 10.1016/j.physrep.2003.08.002 (vol 388, p. 41-277, 2003); arXiv:hep-ph/0307382
- `BelitskyRadyushkin2005` — Unraveling hadron structure with GPDs: review (Ch. 13). — **Verified:** INSPIRE 679716 (Belitsky:2005qn); Crossref 10.1016/j.physrep.2005.06.002 (vol 418, p. 1-387, 2005); arXiv:hep-ph/0504030
- `Beneke1999` — Renormalons: standard review (large-order behaviour, IR renormalons vs power corrections, large-beta0) (Ch. 16). — **Verified:** INSPIRE 473611 (Beneke:1998ui); Crossref 10.1016/S0370-1573(98)00130-6 (vol 317, p. 1-142, 1999); arXiv:hep-ph/9807443
- `BoerEtAl2011` — Gluons and the quark sea at high energies (INT program report / EIC white paper precursor): TMDs, GPDs, saturation (Ch. 11, 12). — **Verified:** INSPIRE 922440 (report nos. SLAC-R-995, INT-PUB-11-034, BNL-96164-2011, JLAB-THY-11-1373; 218 authors; no journal publication); arXiv:1108.1713
- `AngelesMartinezEtAl2015` — TMD parton distribution functions: status and prospects (review) (Ch. 11). — **Verified:** INSPIRE 1383894 (Angeles-Martinez:2015sea); Crossref 10.5506/APhysPolB.46.2501 (vol 46, p. 2501, 2015); arXiv:1507.05267; Crossref gives first page only; page range INSPIRE-only -> first page cited
- `BoussarieEtAl2023` — TMD Handbook: comprehensive review of TMD factorization, evolution, phenomenology, lattice (Ch. 11). — **Verified:** INSPIRE 2650019 (29 authors; no journal publication recorded); arXiv:2304.03302
- `BrambillaEtAl2011` — Heavy quarkonium: progress, puzzles, and opportunities (QWG review) (Ch. 15). — **Verified:** INSPIRE 874793 (Brambilla:2010cs); Crossref 10.1140/epjc/s10052-010-1534-9 (vol 71, p. 1534, 2011); arXiv:1010.5827
- `BrambillaEtAl2005` — Heavy quarkonium physics (QWG CERN Yellow Report): NRQCD/pNRQCD, production and decay (Ch. 15). — **Verified:** DataCite 10.5170/CERN-2005-005 (CERN 2005; 85 creators) -> CDS 872545; INSPIRE 666911 (CERN-2005-005, 487 p.); arXiv:hep-ph/0412158
- `GelisEtAl2010` — The Color Glass Condensate: review of saturation/CGC effective theory (Ch. 12). — **Verified:** INSPIRE 844547 (Gelis:2010nm); Crossref 10.1146/annurev.nucl.010909.083629 (vol 60, p. 463-489, 2010); arXiv:1002.0333
- `CollinsSoper1987` — The theorems of perturbative QCD: review of factorization theorems and their status (Ch. 1, 7). — **Verified:** INSPIRE 245354 (Collins:1987pm); Crossref 10.1146/annurev.ns.37.120187.002123 (vol 37, p. 383-409, 1987)
- `CollinsSoperSterman1989` — Factorization of Hard Processes in QCD: classic review of factorization proofs (DIS, SIA, DY, Glauber cancellation) (Ch. 7-10). — **Verified:** Crossref 10.1142/9789814503266_0001 (pp. 1-91, in "Perturbative QCD", Adv. Ser. Direct. High Energy Phys., 1989-07); INSPIRE 25808 (vol. 5, pp. 1-91) and 286221 (volume: ed. A. H. Mueller, WSP Singapore 1989); arXiv:hep-ph/0409313

## Parton model, OPE, asymptotic freedom, evolution (28)

- `Feynman1969` — Very high-energy collisions of hadrons: parton model (Ch. 1). — **Verified:** INSPIRE 55175 (Feynman:1969ej); Crossref 10.1103/PhysRevLett.23.1415 (vol 23, p. 1415-1417, 1969)
- `Bjorken1969` — Asymptotic sum rules at infinite momentum: Bjorken scaling (Ch. 1, 5). — **Verified:** INSPIRE 52694 (Bjorken:1968dy); Crossref 10.1103/PhysRev.179.1547 (vol 179, p. 1547-1553, 1969)
- `BjorkenPaschos1969` — Inelastic electron-proton and gamma-proton scattering and the structure of the nucleon: parton model of DIS (Ch. 1). — **Verified:** INSPIRE 54851 (Bjorken:1969ja); Crossref 10.1103/PhysRev.185.1975 (vol 185, p. 1975-1982, 1969)
- `DrellYan1970` — Massive lepton-pair production in hadron-hadron collisions: Drell-Yan parton model (Ch. 1, 10). — **Verified:** INSPIRE 60911 (Drell:1970wh); Crossref 10.1103/PhysRevLett.25.316 (vol 25, p. 316-320, 1970); erratum Crossref 10.1103/PhysRevLett.25.902.2
- `Wilson1969` — Non-Lagrangian models of current algebra: operator product expansion proposed (Ch. 5). — **Verified:** INSPIRE 54999 (Wilson:1969zs); Crossref 10.1103/PhysRev.179.1499 (vol 179, p. 1499-1512, 1969)
- `Zimmermann1970` — Brandeis lectures: normal products and the all-orders perturbative proof of the short-distance (Wilson) expansion (Ch. 5). — **Verified:** INSPIRE proceedings record 1375392 (eds. Deser, Grisaru, Pendleton; MIT, Cambridge MA 1970); Open Library ISBN 026204031X (M.I.T. Press 1970, 2 v.); web search of catalogue contents (Vol. 1: Zimmermann, "Local Operator Products and Renormalization in Quantum Field Theory"). No INSPIRE record for the lecture itself; PAGE RANGE NOT VERIFIED and therefore omitted
- `Zimmermann1973` — Normal products and the short distance expansion in renormalized perturbation theory: all-orders perturbative proof of Wilson's OPE (Ch. 5). — **Verified:** INSPIRE 74319 (Zimmermann:1972tv); Crossref 10.1016/0003-4916(73)90430-2 (vol 77, p. 570-601, 1973)
- `BrandtPreparata1971` — Operator product expansions near the light cone (Ch. 5). — **Verified:** INSPIRE 60979 (Brandt:1970kg); Crossref 10.1016/0550-3213(71)90265-3 (vol 27, p. 541-567, 1971)
- `Frishman1971` — Operator products at almost light-like distances: light-cone expansion (Ch. 5). — **Verified:** INSPIRE 72094 (Frishman:1971qn); Crossref 10.1016/0003-4916(71)90195-3 (vol 66, p. 373-389, 1971)
- `ChristHasslacherMueller1972` — Light-cone behavior of perturbation theory: light-cone OPE, anomalous dimensions and scaling violation in renormalized PT (Ch. 5). — **Verified:** INSPIRE 75937 (Christ:1972ms); Crossref 10.1103/PhysRevD.6.3543 (vol 6, p. 3543-3562, 1972)
- `GrossWilczek1973a` — Ultraviolet behavior of non-abelian gauge theories: asymptotic freedom (Ch. 2). — **Verified:** INSPIRE 81238 (Gross:1973id); Crossref 10.1103/PhysRevLett.30.1343 (vol 30, p. 1343-1346, 1973)
- `Politzer1973` — Reliable perturbative results for strong interactions?: asymptotic freedom (Ch. 2). — **Verified:** INSPIRE 81351 (Politzer:1973fx); Crossref 10.1103/PhysRevLett.30.1346 (vol 30, p. 1346-1349, 1973)
- `GrossWilczek1973b` — Asymptotically free gauge theories I: anomalous dimensions of twist-2 (non-singlet) operators, DIS moments (Ch. 5). — **Verified:** INSPIRE 81404 (Gross:1973ju); Crossref 10.1103/PhysRevD.8.3633 (vol 8, p. 3633-3652, 1973)
- `GrossWilczek1974` — Asymptotically free gauge theories II: singlet quark/gluon operator mixing (Ch. 5). — **Verified:** INSPIRE 95436 (Gross:1973zrg, Gross:1974cs); Crossref 10.1103/PhysRevD.9.980 (vol 9, p. 980-993, 1974)
- `GeorgiPolitzer1974` — Electroproduction scaling in an asymptotically free theory: moment predictions (Ch. 5). — **Verified:** INSPIRE 2448 (Georgi:1974wnj, Georgi:1951sr); Crossref 10.1103/PhysRevD.9.416 (vol 9, p. 416-420, 1974)
- `GeorgiPolitzer1976` — Freedom at moderate energies: masses in color dynamics -- target-mass corrections (xi scaling) (Ch. 5). — **Verified:** INSPIRE 108855 (Georgi:1976ve); Crossref 10.1103/PhysRevD.14.1829 (vol 14, p. 1829-1848, 1976)
- `Nachtmann1973` — Positivity constraints for anomalous dimensions; introduces the Nachtmann variable / target-mass treatment (Ch. 5). — **Verified:** INSPIRE 85151 (Nachtmann:1973mr); Crossref 10.1016/0550-3213(73)90144-2 (vol 63, p. 237-247, 1973)
- `GribovLipatov1972a` — Deep inelastic ep scattering in perturbation theory: leading-log evolution (precursor of DGLAP) (Ch. 5, 6). — **Verified:** INSPIRE 73449 (Gribov:1972ri); no DOI; Sov. J. Nucl. Phys. and Yad. Fiz. data INSPIRE-only (no DOI); first pages cited
- `GribovLipatov1972b` — e+e- pair annihilation and deep inelastic ep scattering in perturbation theory (Gribov-Lipatov reciprocity) (Ch. 5, 9). — **Verified:** INSPIRE 73450 (Gribov:1972rt); no DOI; Sov. J. Nucl. Phys. and Yad. Fiz. data INSPIRE-only (no DOI); first pages cited
- `AltarelliParisi1977` — Asymptotic freedom in parton language: LO splitting functions and DGLAP equations (Ch. 5, 6). — **Verified:** INSPIRE 119585 (Altarelli:1977zs); Crossref 10.1016/0550-3213(77)90384-4 (vol 126, p. 298-318, 1977)
- `Dokshitzer1977` — Calculation of structure functions for DIS and e+e- annihilation in QCD perturbation theory (DGLAP) (Ch. 5, 6). — **Verified:** INSPIRE 126153 (Dokshitzer:1977sg, Dokshitser:1977cvj); no DOI; JETP archive: JETP 46(4) 641, Oct 1977 [ZhETF 73(4) 1216]; end pages INSPIRE-only -> first page cited; printed spelling "Dokshitser"
- `FloratosRossSachrajda1977` — Two-loop anomalous dimensions of non-singlet Wilson operators (Ch. 5). — **Verified:** INSPIRE 119944 (Floratos:1977au); Crossref 10.1016/0550-3213(77)90020-7 (vol 129, p. 66-88, 1977); erratum Crossref 10.1016/0550-3213(78)90367-X
- `BardeenEtAl1978` — DIS beyond leading order in asymptotically free gauge theories; introduces the MS-bar scheme (Ch. 2, 5, 8). — **Verified:** INSPIRE 130340 (Bardeen:1978yd); Crossref 10.1103/PhysRevD.18.3998 (vol 18, p. 3998-4017, 1978)
- `CurciFurmanskiPetronzio1980` — Evolution of parton densities beyond LO, non-singlet: NLO kernel from operator definition in light-cone gauge (CFP method) (Ch. 6). — **Verified:** INSPIRE 152873 (Curci:1980uw); Crossref 10.1016/0550-3213(80)90003-6 (vol 175, p. 27-92, 1980); title incl. subtitle per INSPIRE + Semantic Scholar (Crossref truncates the subtitle)
- `FurmanskiPetronzio1980` — Singlet parton densities beyond leading order: NLO singlet splitting functions (Ch. 6). — **Verified:** INSPIRE 155291 (Furmanski:1980cm); Crossref 10.1016/0370-2693(80)90636-X (vol 97, p. 437-442, 1980)
- `FurmanskiPetronzio1982` — Lepton-hadron processes beyond leading order in QCD: NLO coefficient functions and evolution (Ch. 8). — **Verified:** INSPIRE 166165 (Furmanski:1981cw); Crossref 10.1007/BF01578280 (vol 11, p. 293-314, 1982)
- `MochVermaserenVogt2004` — Three-loop splitting functions in QCD: non-singlet case (Ch. 5, 6). — **Verified:** INSPIRE 646539 (Moch:2004pa); Crossref 10.1016/j.nuclphysb.2004.03.030 (vol 688, p. 101-134, 2004); arXiv:hep-ph/0403192
- `VogtMochVermaseren2004` — Three-loop splitting functions in QCD: singlet case (Ch. 5, 6). — **Verified:** INSPIRE 648209 (Vogt:2004mw); Crossref 10.1016/j.nuclphysb.2004.04.024 (vol 691, p. 129-181, 2004); arXiv:hep-ph/0404111

## Renormalization, gauge-theory identities, unitarity, Wilson lines (15)

- `BogoliubovParasiuk1957` — Ueber die Multiplikation der Kausalfunktionen in der Quantentheorie der Felder: R-operation (BPHZ) (Ch. 7). — **Verified:** INSPIRE 9188 (Bogoliubov:1957gp); Crossref 10.1007/BF02392399 (vol 97, p. 227-266, 1957); German original title per publisher; printed author spelling "Bogoliubow"; INSPIRE gives English translation of title
- `Hepp1966` — Proof of the Bogoliubov-Parasiuk theorem on renormalization (BPHZ) (Ch. 7). — **Verified:** INSPIRE 50060 (Hepp:1966eg); Crossref 10.1007/BF01773358 (vol 2, p. 301-326, 1966)
- `Zimmermann1969` — Convergence of Bogoliubov's method of renormalization in momentum space: forest formula (BPHZ) (Ch. 7). — **Verified:** INSPIRE 55117 (Zimmermann:1969jj); Crossref 10.1007/BF01645676 (vol 15, p. 208-234, 1969)
- `Weinberg1960` — High-energy behavior in quantum field theory: Weinberg's power-counting theorem (Ch. 3, App. E). — **Verified:** INSPIRE 9382 (Weinberg:1959nj); Crossref 10.1103/PhysRev.118.838 (vol 118, p. 838-849, 1960)
- `LowensteinZimmermann1975` — Power-counting theorem for Feynman integrals with massless propagators (IR + UV) (Ch. 3). — **Verified:** INSPIRE 98803 (Lowenstein:1975rg); Crossref 10.1007/BF01609059 (vol 44, p. 73-86, 1975)
- `Cutkosky1960` — Singularities and discontinuities of Feynman amplitudes: cutting rules (Ch. 2). — **Verified:** INSPIRE 9133 (Cutkosky:1960sp); Crossref 10.1063/1.1703676 (vol 1, p. 429-433, 1960)
- `Veltman1963` — Unitarity and causality in a renormalizable field theory with unstable particles: largest-time equation, cutting rules (Ch. 2). — **Verified:** INSPIRE 3888 (Veltman:1963th); Crossref 10.1016/S0031-8914(63)80277-3 (vol 29, p. 186-207, 1963)
- `tHooft1971` — Renormalization of massless Yang-Mills fields: gauge-theory Ward identities (Ch. 2, 7). — **Verified:** INSPIRE 68080 (tHooft:1971akt, 'tHooft:1971fh); Crossref 10.1016/0550-3213(71)90395-6 (vol 33, p. 173-199, 1971)
- `Taylor1971` — Ward identities and charge renormalization of the Yang-Mills field (Slavnov-Taylor identities) (Ch. 7). — **Verified:** INSPIRE 68079 (Taylor:1971ff); Crossref 10.1016/0550-3213(71)90297-5 (vol 33, p. 436-444, 1971)
- `Slavnov1972` — Ward identities in gauge theories (Slavnov-Taylor identities) (Ch. 7). — **Verified:** INSPIRE 74885 (Slavnov:1972fg); Crossref 10.1007/BF01090719; English pages 99-104 per Crossref/OpenAlex/Semantic Scholar (INSPIRE says 99-107: wrong); Russian original TMF 10, 153 per INSPIRE only
- `tHooftVeltman1972` — Regularization and renormalization of gauge fields: dimensional regularization (Ch. 2). — **Verified:** INSPIRE 74886 (tHooft:1972tcz, 'tHooft:1972fi); Crossref 10.1016/0550-3213(72)90279-9 (vol 44, p. 189-213, 1972)
- `GrammerYennie1973` — Improved treatment of IR divergences in QED: K/G decomposition (basis of the collinear/soft approximations) (Ch. 7). — **Verified:** INSPIRE 83664 (Grammer:1973db); Crossref 10.1103/PhysRevD.8.4332 (vol 8, p. 4332-4344, 1973)
- `Polyakov1980` — Gauge fields as rings of glue: Wilson-loop renormalization, cusp divergences (Ch. 2, App. B). — **Verified:** INSPIRE 157352 (Polyakov:1980ca); Crossref 10.1016/0550-3213(80)90507-6 (vol 164, p. 171-188, 1980)
- `BrandtNeriSato1981` — Renormalization of loop functions for all loops (Wilson loops) (Ch. 2, App. B). — **Verified:** INSPIRE 164992 (Brandt:1981kf); Crossref 10.1103/PhysRevD.24.879 (vol 24, p. 879-902, 1981)
- `KorchemskyRadyushkin1987` — Renormalization of Wilson loops beyond leading order: two-loop cusp anomalous dimension (Ch. 2, 11). — **Verified:** INSPIRE 246684 (Korchemsky:1987wg); Crossref 10.1016/0550-3213(87)90277-X (vol 283, p. 342-364, 1987)

## Infrared structure, Landau equations, power counting, regions (17)

- `BlochNordsieck1937` — Note on the radiation field of the electron: cancellation of soft-photon IR divergences (Ch. 3). — **Verified:** INSPIRE 23337 (Bloch:1937pw); Crossref 10.1103/PhysRev.52.54 (vol 52, p. 54-59, 1937)
- `Sudakov1956` — Vertex parts at very high energies in QED: Sudakov double logarithms (Ch. 3, 11). — **Verified:** INSPIRE 9137 (Sudakov:1954sw); no DOI; JETP archive: JETP 3(1) 65, Jul 1956 [ZhETF 30(1) 87]; first page cited
- `Landau1959` — On analytic properties of vertex parts in QFT: Landau equations (Ch. 3, App. D). — **Verified:** INSPIRE 4561 (Landau:1959fi); Crossref 10.1016/0029-5582(59)90154-3; INSPIRE mislabels Nucl. Phys. 13 as "reprint"; Crossref confirms Nucl. Phys. 13 (1959) 181-192; JETP archive confirms JETP 10(1) 45 (Jan 1960) version
- `Kinoshita1962` — Mass singularities of Feynman amplitudes (KLN theorem) (Ch. 3). — **Verified:** INSPIRE 2272 (Kinoshita:1962ur); Crossref 10.1063/1.1724268 (vol 3, p. 650-677, 1962)
- `LeeNauenberg1964` — Degenerate systems and mass singularities (KLN theorem) (Ch. 3). — **Verified:** INSPIRE 23504 (Lee:1964is); Crossref 10.1103/PhysRev.133.B1549 (vol 133, p. B1549-B1562, 1964)
- `ColemanNorton1965` — Singularities in the physical region: Coleman-Norton theorem (pinch <-> classical propagation) (Ch. 3, App. D). — **Verified:** INSPIRE 48874 (Coleman:1965xm); Crossref 10.1007/BF02750472 (vol 38, p. 438-442, 1965)
- `PoggioQuinn1976` — IR behavior of zero-mass Green's functions: IR finiteness of off-shell Green functions (Ch. 3). — **Verified:** INSPIRE 3250 (Poggio:1976qr); Crossref 10.1103/PhysRevD.14.578 (vol 14, p. 578-582, 1976)
- `StermanWeinberg1977` — Jets from quantum chromodynamics: IR-safe (cone) jet cross sections (Ch. 3, 9). — **Verified:** INSPIRE 120612 (Sterman:1977wj); Crossref 10.1103/PhysRevLett.39.1436 (vol 39, p. 1436-1439, 1977)
- `Farhi1977` — Quantum chromodynamics test for jets: thrust as an IR-safe event shape (Ch. 9). — **Verified:** INSPIRE 120966 (Farhi:1977sg); Crossref 10.1103/PhysRevLett.39.1587 (vol 39, p. 1587-1588, 1977); publisher title "Quantum Chromodynamics Test for Jets" (INSPIRE: "A QCD Test for Jets")
- `Sterman1978a` — Mass divergences in annihilation processes I: origin and nature of divergences (pinch surfaces, power counting) (Ch. 3, 4). — **Verified:** INSPIRE 6170 (Sterman:1978bi); Crossref 10.1103/PhysRevD.17.2773 (vol 17, p. 2773-2788, 1978)
- `Sterman1978b` — Mass divergences in annihilation processes II: cancellation of divergences in cut vacuum-polarization diagrams (Ch. 3, 4). — **Verified:** INSPIRE 6171 (Sterman:1978bj); Crossref 10.1103/PhysRevD.17.2789 (vol 17, p. 2789-2799, 1978)
- `LibbySterman1978a` — Jet and lepton-pair production in high-energy lepton-hadron and hadron-hadron scattering: leading regions, power counting (Ch. 3). — **Verified:** INSPIRE 130908 (Libby:1978qf); Crossref 10.1103/PhysRevD.18.3252 (vol 18, p. 3252-3268, 1978)
- `LibbySterman1978b` — Mass divergences in two-particle inelastic scattering (Ch. 3). — **Verified:** INSPIRE 131121 (Libby:1978bx); Crossref 10.1103/PhysRevD.18.4737 (vol 18, p. 4737-4745, 1978)
- `CollinsSterman1981` — Soft partons in QCD: soft-region power counting (Ch. 3, 7). — **Verified:** INSPIRE 10172 (Collins:1981ta); Crossref 10.1016/0550-3213(81)90370-9 (vol 185, p. 172-188, 1981)
- `Sen1983` — Asymptotic behavior of fixed-angle on-shell quark scattering amplitudes in non-abelian gauge theories: jet/soft/hard factorization of amplitudes (Ch. 3, 7). — **Verified:** INSPIRE 181894 (Sen:1982bt); Crossref 10.1103/PhysRevD.28.860 (vol 28, p. 860-875, 1983); publisher title says "fixed-angle" (INSPIRE: "wide angle")
- `BenekeSmirnov1998` — Asymptotic expansion of Feynman integrals near threshold: method of regions (Ch. 3). — **Verified:** INSPIRE 451284 (Beneke:1997zp); Crossref 10.1016/S0550-3213(98)00138-2 (vol 522, p. 321-344, 1998); arXiv:hep-ph/9711391
- `Jantzen2011` — Foundation and generalization of the expansion by regions (Ch. 3). — **Verified:** INSPIRE 945404 (Jantzen:2011nz); Crossref 10.1007/JHEP12(2011)076 (vol 2011, p. 76, 2011); arXiv:1111.2589

## e+e- annihilation, duality, event shapes, cut vertices (7)

- `AppelquistGeorgi1973` — e+e- annihilation in gauge theories of strong interactions: O(alpha_s) correction to R (Ch. 4). — **Verified:** INSPIRE 83798 (Appelquist:1973uz); Crossref 10.1103/PhysRevD.8.4000 (vol 8, p. 4000-4002, 1973)
- `Zee1973` — Electron-positron annihilation in stagnant field theories: O(alpha_s) correction to R (Ch. 4). — **Verified:** INSPIRE 83666 (Zee:1973sr); Crossref 10.1103/PhysRevD.8.4038 (vol 8, p. 4038-4041, 1973)
- `PoggioQuinnWeinberg1976` — Smearing method in the quark model: smeared R ratio, quark-hadron duality (Ch. 4). — **Verified:** INSPIRE 100347 (Poggio:1975af); Crossref 10.1103/PhysRevD.13.1958 (vol 13, p. 1958-1968, 1976); publisher title "Smearing method in the quark model" (INSPIRE: "Smearing the Quark Model")
- `ShifmanVainshteinZakharov1979a` — QCD and resonance physics: theoretical foundations (OPE with condensates, sum rules) (Ch. 4, 16). — **Verified:** INSPIRE 130694 (Shifman:1978bx); Crossref 10.1016/0550-3213(79)90022-1 (vol 147, p. 385-447, 1979)
- `ShifmanVainshteinZakharov1979b` — QCD and resonance physics: applications (Ch. 4). — **Verified:** INSPIRE 130695 (Shifman:1978by); Crossref 10.1016/0550-3213(79)90023-3 (vol 147, p. 448-518, 1979)
- `CataniEtAl1993` — Resummation of large logarithms in e+e- event-shape distributions (CTTW) (Ch. 9). — **Verified:** INSPIRE 344540 (Catani:1992ua); Crossref 10.1016/0550-3213(93)90271-P (vol 407, p. 3-42, 1993)
- `Mueller1978` — Cut vertices and their renormalization: generalization of the Wilson expansion (SIA, fragmentation) (Ch. 9). — **Verified:** INSPIRE 6841 (Mueller:1978xu); Crossref 10.1103/PhysRevD.18.3705 (vol 18, p. 3705-3727, 1978)

## Collinear factorization proofs (DIS, DY), PDFs (17)

- `AmatiPetronzioVeneziano1978a` — Relating hard QCD processes through universality of mass singularities (Ch. 7). — **Verified:** INSPIRE 129640 (Amati:1978wx); Crossref 10.1016/0550-3213(78)90313-9 (vol 140, p. 54-72, 1978)
- `AmatiPetronzioVeneziano1978b` — Relating hard QCD processes through universality of mass singularities II (Ch. 7). — **Verified:** INSPIRE 131122 (Amati:1978by); Crossref 10.1016/0550-3213(78)90430-3 (vol 146, p. 29-49, 1978)
- `EllisEtAl1979` — Perturbation theory and the parton model in QCD: factorization of collinear singularities in axial gauge (EGMPR) (Ch. 7). — **Verified:** INSPIRE 7143 (Ellis:1978ty); Crossref 10.1016/0550-3213(79)90105-6 (vol 152, p. 285-329, 1979)
- `AltarelliEllisMartinelli1979` — Large perturbative corrections to the Drell-Yan process in QCD: NLO DY, DIS scheme (Ch. 10). — **Verified:** INSPIRE 140456 (Altarelli:1979ub); Crossref 10.1016/0550-3213(79)90116-0 (vol 157, p. 461-497, 1979)
- `BodwinBrodskyLepage1981` — Initial-state interactions and the Drell-Yan process: potential Glauber factorization breaking (Ch. 10). — **Verified:** INSPIRE 167748 (Bodwin:1981fv); Crossref 10.1103/PhysRevLett.47.1799 (vol 47, p. 1799-1803, 1981)
- `CollinsSoper1982a` — Parton distribution and decay functions: gauge-invariant operator definitions of PDFs and FFs (Ch. 6). — **Verified:** INSPIRE 166064 (Collins:1981uw); Crossref 10.1016/0550-3213(82)90021-9 (vol 194, p. 445-492, 1982)
- `CollinsSoperSterman1983` — Factorization for one-loop corrections in the Drell-Yan process (Glauber cancellation at one loop) (Ch. 10). — **Verified:** INSPIRE 12758 (Collins:1982wa); Crossref 10.1016/0550-3213(83)90062-7 (vol 223, p. 381-421, 1983)
- `Bodwin1985` — Factorization of the Drell-Yan cross section in perturbation theory: Glauber region, contour deformation (Ch. 10). — **Verified:** INSPIRE 207541 (Bodwin:1984hc); Crossref 10.1103/PhysRevD.31.2616 (vol 31, p. 2616-2642, 1985); erratum Crossref 10.1103/PhysRevD.34.3932; NB: INSPIRE BibTeX export puts the ERRATUM DOI in the doi field; main DOI 10.1103/PhysRevD.31.2616 used here
- `CollinsSoperSterman1985b` — Factorization for short-distance hadron-hadron scattering: DY proof (Ch. 10). — **Verified:** INSPIRE 212922 (Collins:1985ue); Crossref 10.1016/0550-3213(85)90565-6 (vol 261, p. 104-142, 1985)
- `CollinsSoperSterman1988` — Soft gluons and factorization: completion of the DY factorization argument (Ch. 10). — **Verified:** INSPIRE 23557 (Collins:1988ig); Crossref 10.1016/0550-3213(88)90130-7 (vol 308, p. 833-856, 1988)
- `DoriaFrenkelTaylor1980` — Counter-example to non-abelian Bloch-Nordsieck conjecture (Ch. 10). — **Verified:** INSPIRE 8825 (Doria:1980ak); Crossref 10.1016/0550-3213(80)90278-3 (vol 168, p. 93-110, 1980); publisher title "...conjecture" (INSPIRE: "...Theorem")
- `DiLietoEtAl1981` — A counter-example to the Bloch-Nordsieck theorem in non-abelian gauge theories (Ch. 10). — **Verified:** INSPIRE 154636 (DiLieto:1980nkq, Di'Lieto:1980dt); Crossref 10.1016/0550-3213(81)90554-X (vol 183, p. 223-250, 1981)
- `HambergVanNeervenMatsuura1991` — Complete O(alpha_s^2) correction to the Drell-Yan K-factor (Ch. 10). — **Verified:** INSPIRE 300492 (Hamberg:1990np); Crossref 10.1016/0550-3213(91)90064-5 (vol 359, p. 343-405, 1991); erratum Crossref 10.1016/S0550-3213(02)00814-3; INSPIRE title has typo "alpha-s"; publisher title used
- `Collins2003` — What exactly is a parton density?: operator definitions, gauge links (Ch. 6, 11). — **Verified:** INSPIRE 616924 (Collins:2003fm); no DOI; arXiv:hep-ph/0304122; journal data INSPIRE + arXiv journal-ref (no DOI); first page cited
- `AltarelliForteRidolfi1998` — On positivity of parton distributions (Ch. 6). — **Verified:** INSPIRE 471691 (Altarelli:1998gn); Crossref 10.1016/S0550-3213(98)00661-0 (vol 534, p. 277-296, 1998); arXiv:hep-ph/9806345
- `CandidoForteHekhorn2020` — Can MS-bar parton distributions be negative? (Ch. 6). — **Verified:** INSPIRE 1801135 (Candido:2020yat); Crossref 10.1007/JHEP11(2020)129 (vol 2020, p. 129, 2020); arXiv:2006.07377
- `CollinsRogersSato2022` — Positivity and renormalization of parton densities (Ch. 6). — **Verified:** INSPIRE 1958816 (Collins:2021vke); Crossref 10.1103/PhysRevD.105.076010 (vol 105, p. 076010, 2022); arXiv:2111.01170

## Heavy quarks in factorization (3)

- `CollinsWilczekZee1978` — Low-energy manifestations of heavy particles: decoupling (CWZ) subtraction scheme (Ch. 8). — **Verified:** INSPIRE 6481 (Collins:1978wz); Crossref 10.1103/PhysRevD.18.242 (vol 18, p. 242-247, 1978)
- `AivazisEtAl1994` — Leptoproduction of heavy quarks II: ACOT variable-flavour-number scheme (Ch. 8). — **Verified:** INSPIRE 361377 (Aivazis:1993pi); Crossref 10.1103/PhysRevD.50.3102 (vol 50, p. 3102-3118, 1994); arXiv:hep-ph/9312319
- `Collins1998b` — Hard-scattering factorization with heavy quarks: a general treatment (Ch. 8). — **Verified:** INSPIRE 471389 (Collins:1998rz); Crossref 10.1103/PhysRevD.58.094002 (vol 58, p. 094002, 1998); arXiv:hep-ph/9806259

## TMD factorization (17)

- `DokshitzerDiakonovTroian1978` — On the transverse momentum distribution of massive lepton pairs (DDT double-log resummation) (Ch. 11). — **Verified:** INSPIRE 136764 (Dokshitzer:1978yd); Crossref 10.1016/0370-2693(78)90240-X (vol 79, p. 269-272, 1978); names as in INSPIRE; printed byline: D. I. D'yakonov, S. I. Troyan
- `ParisiPetronzio1979` — Small transverse momentum distributions in hard processes: b-space resummation (Ch. 11). — **Verified:** INSPIRE 140188 (Parisi:1979se); Crossref 10.1016/0550-3213(79)90040-3 (vol 154, p. 427-440, 1979)
- `CollinsSoper1981` — Back-to-back jets in QCD: TMD factorization for e+e- -> h1 h2 X, Collins-Soper evolution (Ch. 11). — **Verified:** INSPIRE 164211 (Collins:1981uk); Crossref 10.1016/0550-3213(81)90339-4 (vol 193, p. 381-443, 1981); erratum Crossref 10.1016/0550-3213(83)90235-3
- `CollinsSoper1982b` — Back-to-back jets: Fourier transform from b to k_T (Ch. 11). — **Verified:** INSPIRE 11171 (Collins:1981va); Crossref 10.1016/0550-3213(82)90453-9 (vol 197, p. 446-476, 1982)
- `CollinsSoperSterman1985a` — Transverse-momentum distribution in Drell-Yan pair and W, Z production: CSS formalism (Ch. 11). — **Verified:** INSPIRE 203059 (Collins:1984kg); Crossref 10.1016/0550-3213(85)90479-1 (vol 250, p. 199-224, 1985)
- `Sivers1990` — Single-spin production asymmetries from hard scattering of point-like constituents: Sivers function (Ch. 11). — **Verified:** INSPIRE 277567 (Sivers:1989cc); Crossref 10.1103/PhysRevD.41.83 (vol 41, p. 83-90, 1990)
- `Collins1993` — Fragmentation of transversely polarized quarks probed in transverse-momentum distributions: Collins function (Ch. 11). — **Verified:** INSPIRE 337381 (Collins:1992kk); Crossref 10.1016/0550-3213(93)90262-N (vol 396, p. 161-182, 1993); arXiv:hep-ph/9208213
- `BrodskyHwangSchmidt2002` — Final-state interactions and single-spin asymmetries in SIDIS (Ch. 11). — **Verified:** INSPIRE 582417 (Brodsky:2002cx); Crossref 10.1016/S0370-2693(02)01320-5 (vol 530, p. 99-107, 2002); arXiv:hep-ph/0201296
- `Collins2002` — Leading-twist single transverse-spin asymmetries: DY vs DIS -- Sivers sign reversal from T-reversal of Wilson lines (Ch. 11). — **Verified:** INSPIRE 584849 (Collins:2002kn); Crossref 10.1016/S0370-2693(02)01819-1 (vol 536, p. 43-48, 2002); arXiv:hep-ph/0204004
- `JiYuan2002` — Parton distributions in light-cone gauge: where are the final-state interactions? (transverse gauge link) (Ch. 11). — **Verified:** INSPIRE 587988 (Ji:2002aa); Crossref 10.1016/S0370-2693(02)02384-5 (vol 543, p. 66-72, 2002); arXiv:hep-ph/0206057
- `BelitskyJiYuan2003` — Final-state interactions and gauge-invariant parton distributions: transverse links at light-cone infinity (Ch. 11). — **Verified:** INSPIRE 591923 (Belitsky:2002sm); Crossref 10.1016/S0550-3213(03)00121-4 (vol 656, p. 165-198, 2003); arXiv:hep-ph/0208038
- `JiMaYuan2005` — QCD factorization for SIDIS at low transverse momentum (Ch. 11). — **Verified:** INSPIRE 648873 (Ji:2004wu); Crossref 10.1103/PhysRevD.71.034005 (vol 71, p. 034005, 2005); arXiv:hep-ph/0404183
- `CollinsMetz2004` — Universality of soft and collinear factors in hard-scattering factorization (Ch. 11). — **Verified:** INSPIRE 657122 (Collins:2004nx); Crossref 10.1103/PhysRevLett.93.252001 (vol 93, p. 252001, 2004); arXiv:hep-ph/0408249
- `BecherNeubert2011` — Drell-Yan production at small q_T, transverse parton distributions and the collinear anomaly (Ch. 11, 14). — **Verified:** INSPIRE 862424 (Becher:2010tm); Crossref 10.1140/epjc/s10052-011-1665-7 (vol 71, p. 1665, 2011); arXiv:1007.4005
- `EchevarriaIdilbiScimemi2012` — Factorization theorem for DY at low q_T and TMDs on the light-cone (delta regulator) (Ch. 11, 14). — **Verified:** INSPIRE 946813 (Echevarria:2011epo, GarciaEchevarria:2011rb); Crossref 10.1007/JHEP07(2012)002 (vol 2012, p. 2, 2012); arXiv:1111.4996; author diacritics per publisher byline (Echevarría)
- `ChiuEtAl2012a` — Rapidity renormalization group (PRL) (Ch. 11, 14). — **Verified:** INSPIRE 894935 (Chiu:2011qc); Crossref 10.1103/PhysRevLett.108.151601 (vol 108, p. 151601, 2012); arXiv:1104.0881
- `ChiuEtAl2012b` — A formalism for the systematic treatment of rapidity logarithms in QFT (rapidity RG, eta regulator) (Ch. 11, 14). — **Verified:** INSPIRE 1087437 (Chiu:2012ir); Crossref 10.1007/JHEP05(2012)084 (vol 2012, p. 84, 2012); arXiv:1202.0814

## Factorization breaking and non-rigorous cases (14)

- `CollinsQiu2007` — k_T factorization is violated in production of high-p_T particles in hadron-hadron collisions (Ch. 12) [V]. — **Verified:** INSPIRE 750627 (Collins:2007nk); Crossref 10.1103/PhysRevD.75.114014 (vol 75, p. 114014, 2007); arXiv:0705.2141
- `Collins2007` — 2-soft-gluon exchange and factorization breaking (Ch. 12). — **Verified:** INSPIRE 759565 (no journal publication); arXiv:0708.4410 (comment: 8 pages; no journal-ref)
- `AybatSterman2009` — Soft-gluon cancellation, phases and factorization with initial-state partons (Ch. 10, 12). — **Verified:** INSPIRE 801376 (Aybat:2008ct); Crossref 10.1016/j.physletb.2008.11.050 (vol 671, p. 46-50, 2009); arXiv:0811.0246; arXiv 2008, journal 2009
- `RogersMulders2010` — No generalized TMD factorization in the hadroproduction of high-p_T hadrons (Ch. 12) [V]. — **Verified:** INSPIRE 843028 (Rogers:2010dm); Crossref 10.1103/PhysRevD.81.094006 (vol 81, p. 094006, 2010); arXiv:1001.2977; publisher title differs from arXiv/INSPIRE wording; publisher version used
- `ForshawKyrieleisSeymour2006` — Super-leading logarithms in non-global observables in QCD (Ch. 12). — **Verified:** INSPIRE 714255 (Forshaw:2006fk); Crossref 10.1088/1126-6708/2006/08/059 (vol 2006, p. 059-059, 2006); arXiv:hep-ph/0604094
- `DasguptaSalam2001` — Resummation of non-global QCD observables: non-global logarithms (Ch. 9, 12). — **Verified:** INSPIRE 555905 (Dasgupta:2001sh); Crossref 10.1016/S0370-2693(01)00725-0 (vol 512, p. 323-330, 2001); arXiv:hep-ph/0104277
- `CataniDeFlorianRodrigo2012` — Space-like (vs time-like) collinear limits in QCD: strict collinear factorization violated (Ch. 12). — **Verified:** INSPIRE 1082019 (Catani:2011st); Crossref 10.1007/JHEP07(2012)026 (vol 2012, p. 26, 2012); arXiv:1112.4405
- `ForshawSeymourSiodmok2012` — On the breaking of collinear factorization in QCD (Ch. 12). — **Verified:** INSPIRE 1120161 (Forshaw:2012bi); Crossref 10.1007/JHEP11(2012)066 (vol 2012, p. 66, 2012); arXiv:1206.6363; author diacritics per publisher byline (Siódmok)
- `RothsteinStewart2016` — An EFT for forward scattering and factorization violation: Glauber operators in SCET (Ch. 12, 14). — **Verified:** INSPIRE 1415957 (Rothstein:2016bsq); Crossref 10.1007/JHEP08(2016)025 (vol 2016, p. 25, 2016); arXiv:1601.04695
- `IngelmanSchlein1985` — Jet structure in high-mass diffractive scattering: pomeron parton densities (Ch. 12). — **Verified:** INSPIRE 207624 (Ingelman:1984ns); Crossref 10.1016/0370-2693(85)91181-5 (vol 152, p. 256-260, 1985)
- `Collins1998a` — Proof of factorization for diffractive hard scattering (diffractive DIS) (Ch. 12). — **Verified:** INSPIRE 449041 (Collins:1997sr); Crossref 10.1103/PhysRevD.57.3051 (vol 57, p. 3051-3056, 1998); arXiv:hep-ph/9709499; erratum Crossref 10.1103/PhysRevD.61.019902; erratum PRD 61 019902: Crossref online 1999, volume year 2000 (INSPIRE 2000)
- `AffolderEtAl2000` — CDF: diffractive dijets with a leading antiproton at sqrt(s)=1800 GeV -- breakdown of diffractive factorization in hadron-hadron (Ch. 12) [V]. — **Verified:** INSPIRE 525012 (CDF:2000rua, Affolder:2000vb); Crossref 10.1103/PhysRevLett.84.5043 (vol 84, p. 5043-5048, 2000)
- `DiehlOstermeierSchafer2012` — Elements of a theory for multiparton interactions in QCD (Ch. 12). — **Verified:** INSPIRE 944460 (Diehl:2011yj); Crossref 10.1007/JHEP03(2012)089 (vol 2012, p. 89, 2012); arXiv:1111.0910; erratum Crossref 10.1007/JHEP03(2016)001; author diacritics per publisher byline (Schäfer)
- `Gaunt2014` — Glauber gluons and multiple parton interactions (Ch. 12). — **Verified:** INSPIRE 1295494 (Gaunt:2014ska); Crossref 10.1007/JHEP07(2014)110 (vol 2014, p. 110, 2014); arXiv:1405.2080

## Small-x, BFKL, saturation (7)

- `KuraevLipatovFadin1977` — The Pomeranchuk singularity in non-abelian gauge theories (BFKL) (Ch. 12). — **Verified:** INSPIRE 123995 (Kuraev:1977fs); no DOI; JETP archive: JETP 45(2) 199, Feb 1977 [ZhETF 72(2) 377]; first page cited
- `BalitskyLipatov1978` — The Pomeranchuk singularity in QCD (BFKL) (Ch. 12). — **Verified:** INSPIRE 137229 (Balitsky:1978ic); no DOI; Sov. J. Nucl. Phys. and Yad. Fiz. data INSPIRE-only (no DOI); first pages cited
- `GribovLevinRyskin1983` — Semihard processes in QCD: gluon recombination, saturation (GLR) (Ch. 12). — **Verified:** INSPIRE 200601 (Gribov:1983ivg, Gribov:1984tu); Crossref 10.1016/0370-1573(83)90022-4 (vol 100, p. 1-150, 1983)
- `CataniCiafaloniHautmann1991` — High-energy factorization and small-x heavy-flavour production (k_T factorization) (Ch. 12). — **Verified:** INSPIRE 302969 (Catani:1990eg); Crossref 10.1016/0550-3213(91)90055-3 (vol 366, p. 135-188, 1991)
- `CollinsEllis1991` — Heavy-quark production in very high energy hadron collisions (k_T factorization) (Ch. 12). — **Verified:** INSPIRE 313886 (Collins:1991ty); Crossref 10.1016/0550-3213(91)90288-9 (vol 360, p. 3-30, 1991)
- `Balitsky1996` — Operator expansion for high-energy scattering: Balitsky hierarchy (Ch. 12). — **Verified:** INSPIRE 399690 (Balitsky:1995ub); Crossref 10.1016/0550-3213(95)00638-9; arXiv:hep-ph/9509348; pages 99-157 per Crossref/OpenAlex/Semantic Scholar (INSPIRE says 99-160: wrong)
- `Kovchegov1999` — Small-x F2 of a nucleus including multiple pomeron exchanges: BK equation (Ch. 12). — **Verified:** INSPIRE 493965 (Kovchegov:1999yj); Crossref 10.1103/PhysRevD.60.034008 (vol 60, p. 034008, 1999); arXiv:hep-ph/9901281

## Hard exclusive processes, DAs, GPDs (13)

- `BrodskyFarrar1973` — Scaling laws at large transverse momentum: constituent counting rules (Ch. 13). — **Verified:** INSPIRE 81095 (Brodsky:1973kr); Crossref 10.1103/PhysRevLett.31.1153 (vol 31, p. 1153-1156, 1973)
- `LepageBrodsky1980` — Exclusive processes in perturbative QCD: light-cone DAs, ERBL evolution, pion form factor (Ch. 13). — **Verified:** INSPIRE 153236 (Lepage:1980fj); Crossref 10.1103/PhysRevD.22.2157 (vol 22, p. 2157-2198, 1980)
- `EfremovRadyushkin1980` — Factorization and asymptotic behavior of the pion form factor in QCD (Ch. 13). — **Verified:** INSPIRE 145717 (Efremov:1979qk); Crossref 10.1016/0370-2693(80)90869-2 (vol 94, p. 245-250, 1980)
- `ChernyakZhitnitsky1984` — Asymptotic behavior of exclusive processes in QCD (review; CZ distribution amplitudes) (Ch. 13). — **Verified:** INSPIRE 194579 (Chernyak:1983ej); Crossref 10.1016/0370-1573(84)90126-1 (vol 112, p. 173-318, 1984)
- `IsgurLlewellynSmith1984` — Asymptotic Q^2 for exclusive processes in QCD: endpoint (soft) contributions critique (Ch. 13). — **Verified:** INSPIRE 14464 (Isgur:1984jm); Crossref 10.1103/PhysRevLett.52.1080 (vol 52, p. 1080-1083, 1984); publisher title "Asymptotic Q^2 for ..." (INSPIRE carries preprint title "Asymptopia in high q**2 ...")
- `LiSterman1992` — The perturbative pion form factor with Sudakov suppression (Ch. 13). — **Verified:** INSPIRE 333159 (Li:1992nu); Crossref 10.1016/0550-3213(92)90643-P (vol 381, p. 129-140, 1992)
- `MullerEtAl1994` — Wave functions, evolution equations and evolution kernels from light-ray operators of QCD (origin of GPDs) (Ch. 13). — **Verified:** INSPIRE 465908 (Muller:1994ses, Mueller:1998fv); Crossref 10.1002/prop.2190420202 (vol 42, p. 101-141, 1994); arXiv:hep-ph/9812448
- `Ji1997a` — Gauge-invariant decomposition of nucleon spin: GPDs and DVCS (Ch. 13). — **Verified:** INSPIRE 416559 (Ji:1996ek); Crossref 10.1103/PhysRevLett.78.610 (vol 78, p. 610-613, 1997); arXiv:hep-ph/9603249
- `Ji1997b` — Deeply virtual Compton scattering (Ch. 13). — **Verified:** INSPIRE 423438 (Ji:1996nm); Crossref 10.1103/PhysRevD.55.7114 (vol 55, p. 7114-7125, 1997); arXiv:hep-ph/9609381
- `Radyushkin1997` — Non-forward parton distributions (Ch. 13). — **Verified:** INSPIRE 441746 (Radyushkin:1997ki); Crossref 10.1103/PhysRevD.56.5524 (vol 56, p. 5524-5557, 1997); arXiv:hep-ph/9704207
- `CollinsFrankfurtStrikman1997` — Factorization for hard exclusive electroproduction of mesons in QCD (longitudinal photons) (Ch. 13). — **Verified:** INSPIRE 426483 (Collins:1996fb); Crossref 10.1103/PhysRevD.56.2982 (vol 56, p. 2982-3006, 1997); arXiv:hep-ph/9611433
- `JiOsborne1998` — One-loop corrections and all-order factorization in DVCS (Ch. 13). — **Verified:** INSPIRE 466154 (Ji:1998xh); Crossref 10.1103/PhysRevD.58.094018 (vol 58, p. 094018, 1998); arXiv:hep-ph/9801260
- `CollinsFreund1999` — Proof of factorization for deeply virtual Compton scattering in QCD (Ch. 13). — **Verified:** INSPIRE 466174 (Collins:1998be); Crossref 10.1103/PhysRevD.59.074009 (vol 59, p. 074009, 1999); arXiv:hep-ph/9801262

## Soft-collinear effective theory (12)

- `BauerFlemingLuke2000` — Summing Sudakov logarithms in B -> X_s gamma in effective field theory: first SCET paper (Ch. 14). — **Verified:** INSPIRE 527930 (Bauer:2000ew); Crossref 10.1103/PhysRevD.63.014006 (vol 63, p. 014006, 2000); arXiv:hep-ph/0005275; year 2000 (Crossref issued 2000; issue dated Jan 2001)
- `BauerEtAl2001` — An EFT for collinear and soft gluons: heavy-to-light decays -- SCET Lagrangian, collinear Wilson lines (Ch. 14). — **Verified:** INSPIRE 537516 (Bauer:2000yr); Crossref 10.1103/PhysRevD.63.114020 (vol 63, p. 114020, 2001); arXiv:hep-ph/0011336
- `BauerStewart2001` — Invariant operators in collinear effective theory (Ch. 14). — **Verified:** INSPIRE 559421 (Bauer:2001ct); Crossref 10.1016/S0370-2693(01)00902-9 (vol 516, p. 134-142, 2001); arXiv:hep-ph/0107001
- `BauerPirjolStewart2001` — A proof of factorization for B -> D pi (Ch. 14). — **Verified:** INSPIRE 559422 (Bauer:2001cu); Crossref 10.1103/PhysRevLett.87.201806 (vol 87, p. 201806, 2001); arXiv:hep-ph/0107002
- `BauerPirjolStewart2002` — Soft-collinear factorization in EFT: ultrasoft decoupling field redefinition (Ch. 14). — **Verified:** INSPIRE 562452 (Bauer:2001yt); Crossref 10.1103/PhysRevD.65.054022 (vol 65, p. 054022, 2002); arXiv:hep-ph/0109045
- `BauerEtAl2002` — Hard scattering factorization from effective field theory: DIS, DY, e+e- in SCET (Ch. 14). — **Verified:** INSPIRE 582803 (Bauer:2002nz); Crossref 10.1103/PhysRevD.66.014017 (vol 66, p. 014017, 2002); arXiv:hep-ph/0202088
- `BenekeEtAl2002` — SCET and heavy-to-light currents beyond leading power (position-space SCET) (Ch. 14). — **Verified:** INSPIRE 588622 (Beneke:2002ph); Crossref 10.1016/S0550-3213(02)00687-9 (vol 643, p. 431-476, 2002); arXiv:hep-ph/0206152
- `ManoharStewart2007` — The zero-bin and mode factorization in QFT (Ch. 14). — **Verified:** INSPIRE 715628 (Manohar:2006nz); Crossref 10.1103/PhysRevD.76.074002 (vol 76, p. 074002, 2007); arXiv:hep-ph/0605001
- `IdilbiMehen2007` — On the equivalence of soft and zero-bin subtractions (Ch. 14). — **Verified:** INSPIRE 743755 (Idilbi:2007ff); Crossref 10.1103/PhysRevD.75.114017 (vol 75, p. 114017, 2007); arXiv:hep-ph/0702022
- `BecherNeubertPecjak2007` — Factorization and momentum-space resummation in DIS (x -> 1) (Ch. 14). — **Verified:** INSPIRE 722046 (Becher:2006mr); Crossref 10.1088/1126-6708/2007/01/076 (vol 2007, p. 076-076, 2007); arXiv:hep-ph/0607228
- `BecherSchwartz2008` — A precise determination of alpha_s from LEP thrust data using EFT: thrust factorization H J J S (Ch. 9, 14). — **Verified:** INSPIRE 780596 (Becher:2008cf); Crossref 10.1088/1126-6708/2008/07/034 (vol 2008, p. 034-034, 2008); arXiv:0803.0342
- `FeigeSchwartz2014` — Hard-soft-collinear factorization to all orders (amplitude level) (Ch. 7, 14). — **Verified:** INSPIRE 1287360 (Feige:2014wja); Crossref 10.1103/PhysRevD.90.105020 (vol 90, p. 105020, 2014); arXiv:1403.6472

## B-meson decays (QCD factorization) (4)

- `BenekeEtAl1999` — QCD factorization for B -> pi pi: strong phases and CP violation in the heavy-quark limit (BBNS) (Ch. 14). — **Verified:** INSPIRE 499707 (Beneke:1999br); Crossref 10.1103/PhysRevLett.83.1914 (vol 83, p. 1914-1917, 1999); arXiv:hep-ph/9905312
- `BenekeEtAl2000` — QCD factorization for exclusive non-leptonic B decays: general arguments and heavy-light final states (Ch. 14). — **Verified:** INSPIRE 528680 (Beneke:2000ry); Crossref 10.1016/S0550-3213(00)00559-9 (vol 591, p. 313-418, 2000); arXiv:hep-ph/0006124
- `BenekeEtAl2001` — QCD factorization in B -> pi K, pi pi decays and extraction of Wolfenstein parameters (Ch. 14). — **Verified:** INSPIRE 555353 (Beneke:2001ev); Crossref 10.1016/S0550-3213(01)00251-6 (vol 606, p. 245-321, 2001); arXiv:hep-ph/0104110
- `BenekeNeubert2003` — QCD factorization for B -> PP and B -> PV decays; endpoint-divergence parametrization (Ch. 14). — **Verified:** INSPIRE 624954 (Beneke:2003zv); Crossref 10.1016/j.nuclphysb.2003.09.026 (vol 675, p. 333-415, 2003); arXiv:hep-ph/0308039

## Heavy quarkonium (5)

- `CaswellLepage1986` — Effective Lagrangians for bound-state problems in QED, QCD and other field theories: NRQED/NRQCD (Ch. 15). — **Verified:** INSPIRE 213093 (Caswell:1985ui); Crossref 10.1016/0370-2693(86)91297-9 (vol 167, p. 437-442, 1986)
- `BodwinBraatenLepage1995` — Rigorous QCD analysis of inclusive annihilation and production of heavy quarkonium: NRQCD factorization (BBL) (Ch. 15). — **Verified:** INSPIRE 374999 (Bodwin:1994jh); Crossref 10.1103/PhysRevD.51.1125 (vol 51, p. 1125-1171, 1995); arXiv:hep-ph/9407339; erratum Crossref 10.1103/PhysRevD.55.5853
- `NayakQiuSterman2005a` — Fragmentation, factorization and infrared poles in heavy-quarkonium production (Ch. 15). — **Verified:** INSPIRE 675608 (Nayak:2005rw); Crossref 10.1016/j.physletb.2005.03.031 (vol 613, p. 45-51, 2005); arXiv:hep-ph/0501235
- `NayakQiuSterman2005b` — Fragmentation, NRQCD and NNLO factorization analysis in heavy-quarkonium production: gauge-completed operators (Ch. 15). — **Verified:** INSPIRE 691365 (Nayak:2005rt); Crossref 10.1103/PhysRevD.72.114012 (vol 72, p. 114012, 2005); arXiv:hep-ph/0509021
- `NayakQiuSterman2006` — NRQCD factorization and velocity-dependence of NNLO poles in heavy-quarkonium production (Ch. 15). — **Verified:** INSPIRE 723335 (Nayak:2006fm); Crossref 10.1103/PhysRevD.74.074007 (vol 74, p. 074007, 2006); arXiv:hep-ph/0608066

## Power corrections, higher twist, renormalons, threshold resummation (14)

- `tHooft1979` — Can we make sense out of QCD?: origin of renormalons (Erice 1977 lectures) (Ch. 16). — **Verified:** Crossref 10.1007/978-1-4684-0991-8_17 (pp. 943-982 in 'The Whys of Subnuclear Physics', ed. Zichichi, Springer US, Boston MA, 1979); INSPIRE 5753 (Subnucl. Ser. 15 (1979) 943; Erice 1977)
- `EllisFurmanskiPetronzio1982` — Power corrections to the parton model in QCD: higher-twist factorization (Ch. 16). — **Verified:** INSPIRE 176841 (Ellis:1982wd); Crossref 10.1016/0550-3213(82)90132-8 (vol 207, p. 1-14, 1982)
- `EllisFurmanskiPetronzio1983` — Unravelling higher twists (Ch. 16). — **Verified:** INSPIRE 178625 (Ellis:1982cd); Crossref 10.1016/0550-3213(83)90597-7 (vol 212, p. 29-98, 1983)
- `Jaffe1983` — Parton distribution functions for twist four (Ch. 16). — **Verified:** INSPIRE 190275 (Jaffe:1983hp); Crossref 10.1016/0550-3213(83)90361-9 (vol 229, p. 205-230, 1983)
- `EfremovTeryaev1985` — QCD asymmetry and polarized hadron structure function measurement: twist-3 quark-gluon correlators (ETQS) (Ch. 16). — **Verified:** INSPIRE 207564 (Efremov:1984ip); Crossref 10.1016/0370-2693(85)90999-2 (vol 150, p. 383-386, 1985)
- `Mueller1985` — On the structure of infrared renormalons in physical processes at high energies (Ch. 16). — **Verified:** INSPIRE 15601 (Mueller:1984vh); Crossref 10.1016/0550-3213(85)90485-7 (vol 250, p. 327-350, 1985)
- `QiuSterman1991a` — Power corrections in hadronic scattering I: leading 1/Q^2 corrections to the DY cross section (Ch. 16). — **Verified:** INSPIRE 28106 (Qiu:1990xxa); Crossref 10.1016/0550-3213(91)90503-P (vol 353, p. 105-136, 1991)
- `QiuSterman1991b` — Power corrections in hadronic scattering II: factorization (Ch. 16). — **Verified:** INSPIRE 28107 (Qiu:1990xy); Crossref 10.1016/0550-3213(91)90504-Q (vol 353, p. 137-164, 1991)
- `QiuSterman1991c` — Single transverse-spin asymmetries: twist-3 (ETQS) mechanism (Ch. 16). — **Verified:** INSPIRE 30360 (Qiu:1991pp); Crossref 10.1103/PhysRevLett.67.2264 (vol 67, p. 2264-2267, 1991)
- `QiuSterman1992` — Single transverse-spin asymmetries in direct-photon production: detailed twist-3 (ETQS) calculation (Ch. 16). [NB: not the pion-production paper.] — **Verified:** INSPIRE 31047 (Qiu:1991wg); Crossref 10.1016/0550-3213(92)90003-T (vol 378, p. 52-78, 1992); content is direct-photon production (not pion production)
- `BenekeBraun1995a` — Naive non-abelianization and resummation of fermion bubble chains (large-beta0) (Ch. 16). — **Verified:** INSPIRE 379565 (Beneke:1994qe); Crossref 10.1016/0370-2693(95)00184-M (vol 348, p. 513-520, 1995); arXiv:hep-ph/9411229
- `BenekeBraun1995b` — Power corrections and renormalons in Drell-Yan production (Ch. 16). — **Verified:** INSPIRE 396739 (Beneke:1995pq); Crossref 10.1016/0550-3213(95)00439-Y (vol 454, p. 253-290, 1995); arXiv:hep-ph/9506452
- `Sterman1987` — Summation of large corrections to short-distance hadronic cross sections: threshold resummation (Ch. 10). — **Verified:** INSPIRE 230126 (Sterman:1986aj); Crossref 10.1016/0550-3213(87)90258-6 (vol 281, p. 310-364, 1987)
- `CataniTrentadue1989` — Resummation of the QCD perturbative series for hard processes: threshold resummation (Ch. 10). — **Verified:** INSPIRE 25461 (Catani:1989ne); Crossref 10.1016/0550-3213(89)90273-3 (vol 327, p. 323-352, 1989)

## Lattice approaches to parton physics (5)

- `Ji2013` — Parton physics on a Euclidean lattice: quasi-PDFs / LaMET (Ch. 16). — **Verified:** INSPIRE 1232221 (Ji:2013dva); Crossref 10.1103/PhysRevLett.110.262002 (vol 110, p. 262002, 2013); arXiv:1305.1539
- `Radyushkin2017` — Quasi-PDFs, momentum distributions and pseudo-PDFs (Ch. 16). — **Verified:** INSPIRE 1598042 (Radyushkin:2017cyf, Radyushkin:2017ryp); Crossref 10.1103/PhysRevD.96.034025 (vol 96, p. 034025, 2017); arXiv:1705.01488
- `MaQiu2018` — Exploring partonic structure of hadrons using ab initio lattice QCD calculations: lattice cross sections (Ch. 16). — **Verified:** INSPIRE 1622746 (Ma:2017pxb); Crossref 10.1103/PhysRevLett.120.022003 (vol 120, p. 022003, 2018); arXiv:1709.03018
- `IzubuchiEtAl2018` — Factorization theorem relating Euclidean and light-cone parton distributions (Ch. 16). — **Verified:** INSPIRE 1647571 (Izubuchi:2018srq); Crossref 10.1103/PhysRevD.98.056004 (vol 98, p. 056004, 2018); arXiv:1801.03917
- `JiEtAl2021` — Large-momentum effective theory: review (Ch. 16). — **Verified:** INSPIRE 1790338 (Ji:2020ect); Crossref 10.1103/RevModPhys.93.035005 (vol 93, p. 035005, 2021); arXiv:2004.03543
