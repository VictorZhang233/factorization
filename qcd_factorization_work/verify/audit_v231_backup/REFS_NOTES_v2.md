# REFS_NOTES_v2 — companion to `spec_v2/refs_merged_v2.bib`

Drafted 2026-10-10 by the spec-v2 writer-spec/figures/bibliography drafter (current revision **v2.1**, same day: 1003 entries, attribution rules A01–A28, App Q sources E01–E36 — see CHANGELOG). **Writers cite only keys that appear in `refs_merged_v2.bib`**, and attribute to a source **only** what is documented here, in `spec/REFS_NOTES.md` (v1 notes, still binding for the 646 v1 keys), in `research/survey/SURVEY.md` (markers [txt]/[abs]/[bib]) or in the frontier reports (`frontier/lamet/LAMET.md`, `frontier/yzliu/YZLIU.md`, `frontier/others/OTHERS.md`, reading markers *(read)*/[txt], *(abstract)*/[abs], *(title)*, [bib]). If you need a statement from a source that is not documented, mark it `(verify)` in your report instead of writing it as fact. **The reference document `factorization_qcd-2.pdf` is never cited** (WRITER_SPEC_v2 §6.10).

## 0. Provenance, counts, how to use

| part of the bib | origin | entries | verification |
|---|---|---|---|
| 1–4 | spec v1 `spec/refs_merged.bib`, verbatim except the v2.1 format fixes of rule 6 (refs agent, survey, supplement, classical mathematics) | 646 | as v1 (INSPIRE + Crossref + arXiv + Open Library; v1 audit) |
| 5 | `frontier/yzliu/yzliu.bib`, new entries | 57 | INSPIRE; every DOI entry cross-checked against Crossref by the yzliu agent; manual corrections listed in §1.2 |
| 6 | `frontier/lamet/lamet.bib`, new entries | 109 | INSPIRE texkeys, each resolved to exactly that primary record (`frontier/lamet/scripts/build_bib.py`) |
| 7 | `frontier/others/others.bib`, new entries | 145 | INSPIRE verbatim (`Gordan:1873` via Crossref is a duplicate of v1 `Gordan1873`) |
| 8 | spec-v2 additions from INSPIRE-HEP | 41 | one hit per journal-reference query, metadata checked (first author, journal, volume, page, year): `spec_v2/checks/fetch_additions.py` (38 entries) and, in spec v2.1, `spec_v2/checks/fetch_additions_v21.py` (3 small-x helicity papers whose identity was fixed from the INSPIRE reference list of `Borden:2025ehe`); records and JSON in `spec_v2/checks/inspire_additions/`, logs `fetch_additions.log`, `fetch_additions_v21.log` |
| 9 | spec-v2 manual entries (Crossref) | 5 | `Epstein1960`, `Markoff1916` (Crossref DOIs), `Zweig:1964jf` (INSPIRE record re-typed as a CERN report); v2.1: `SlepianPollak1961`, `LandauWidom1980` (Crossref DOIs; classical harmonic analysis, not in INSPIRE) |
| 10 | spec-v2.3 verify-patch additions | 48 | 45 INSPIRE records (one hit per query, `spec_v2/checks/fetch_additions_v23.py`, log `fetch_additions_v23.log`) and 3 Crossref-verified manual entries (`Hormander2003`, `Vladimirov2002`, `NilssonPassare2013`); block built by `checks/add_refs_v23.py`; §5.1 |
| | **total** | **1051** | BibTeX `unsrt` with `\nocite{*}`: exit 0, **0 warnings, 0 errors**; XeLaTeX with `common/preamble_fact.tex`: **0 errors, 0 missing glyphs, 0 overfull boxes** (61 pp.) — `spec_v2/checks/bibtest/SUMMARY.txt` (spec v2.3: 1051 entries; v2.1 with 1003 entries and v2.0 with 998 entries gave the same results on 59 and 58 pp.) |

**Merge rules** (`spec_v2/checks/build_refs_v2.py`, reproducible; log `spec_v2/checks/merge_log_v2.tsv`).
1. Order of precedence: v1 > yzliu > lamet > others > spec-v2 INSPIRE additions > manual entries. The first occurrence of a paper is kept with its key; later occurrences become aliases.
2. Duplicates are detected by DOI (normalized), arXiv number (version stripped) or INSPIRE texkey (entry key or the v1 `inspire` field). Result: 186 frontier entries and 2 spec-v2 additions were duplicates (69 lamet, 25 yzliu, 92 others; `Andrasi:1980qw` and `Hamberg:1991qt` were already present); a title-based scan found no further duplicate (two lamet entries share the title "Determination of the Collins–Soper kernel from lattice QCD" but are different papers: `Avkhadiev:2024mgd`, `Schlemmer:2021aij`).
3. All v1 keys are unchanged. New entries keep their INSPIRE texkeys (or the readable manual keys of part 9).
4. arXiv-only `@article` records (no journal) were converted to `@misc` with `howpublished = "arXiv:<number> [<class>]"`, exactly as v1 did (23 entries; they are the preprints of §1.3).
5. Non-ASCII characters were replaced by LaTeX macros (none remained after the yzliu-first ordering: yzliu's `Su:2026eta` uses `\pm\xi`).
6. Field patches (Crossref-verified): `Piguet:1995er` gained series/publisher/address (BibTeX "empty publisher" warning removed). Spec v2.1: `Bartels:1996wc` DOI (INSPIRE exports the non-resolving ADS DOI 10.1007/BF02909194; Crossref: 10.1007/s002880050285); `Blumlein:1996hb` author with umlaut (Bl{\"u}mlein); math titles for `Bartels:1995iu`, `Bartels:1996wc`, `Blumlein:1996hb` ($g_1$, $g_1(x,Q^2)$ instead of INSPIRE's "G(1)", "Q**2"); internal provenance remarks removed from the printed `note` fields of `LatticeParton:2020uhz`, `Markoff1916` and of the two v1 entries `Gardi:2024axt`, `Shifman2000` (see §1.2). Finally, the 29 numeric `month` fields of all parts (INSPIRE exports `month = "7"` for preprints, printed by `unsrt` as "7 2020") are written as BibTeX month macros (`month = jul`, printed "July 2020"). Legacy all-caps INSPIRE titles (11 entries: v1 `Catani:1985xt`, `Frenkel:1983di`, `Kastella:1989ux`, `Ore:1979ry`, `KrasnikovPivovarov1982`, `Gonsalves1983`, `FrenkelTaylor1984`, `BaierFey1979`; additions `Chetyrkin:1982zq`, `Gawedzki:1985ez`, `Nielsen:1980sx`) are replaced by the published titles from Crossref (by DOI); for `Frenkel:1983di` the published title ("Quark-antiquark annihilation is infrared safe at high energy to all orders", NPB 233 (1984) 307) differs in wording from INSPIRE's "Is quark–antiquark annihilation infrared safe at high energy?", and `Catani:1985xt` reads "coherent states". These are the only changes to the v1 text (two notes, eight titles, five month fields); all v1 keys and all other v1 fields are unchanged.
7. `verify/` bibliographies: none existed at build time (spec v2.1 re-check: `verify/` contains only `CLAIMS.md`, whose 215 key-like references all resolve to merged keys; the one reference it marks "to be added", Bartels–Ermolaev–Ryskin, was added). When the verify workflow adds a `.bib`, re-run `python3 -I spec_v2/checks/build_refs_v2.py <WORKDIR>` (it picks up `verify/**/*.bib` automatically, after the frontier files) and re-run the BibTeX test.

**Aliases.** `spec_v2/key_aliases_v2.tsv` (columns `alias`, `merged_key`, `origin`; 1075 rows in spec v2.1) = the 673 v1 rows verbatim + one row per frontier duplicate (frontier key → merged key, with the matching identifiers) + an identity row per new entry (origin = source bibliography) + readable aliases of the spec-v2 additions (e.g. `FaddeevPopov1967` → `Faddeev:1967fc`). `Collins:2011zzd` maps to `Collins2011` first (and to `Collins2023`); always cite `Collins2011` for page and equation numbers. Replace aliases in any reused snippet with the v1 script, changing only the file name:

```python
# python3 -I replace_aliases.py SNIPPET.tex > SNIPPET_fixed.tex
import re, sys
al = {}
for ln in open('spec_v2/key_aliases_v2.tsv', encoding='utf-8'):
    a, k = ln.rstrip('\n').split('\t')[:2]
    if a != 'alias' and a != k:
        al.setdefault(a, k)   # first row wins (Collins:2011zzd -> Collins2011)
t = open(sys.argv[1], encoding='utf-8').read()
def fix(m):
    keys = [al.get(x.strip(), x.strip()) for x in m.group(2).split(',')]
    return m.group(1) + '{' + ','.join(keys) + '}'
print(re.sub(r'(\\(?:no)?cite(?:\[[^\]]*\])?)\{([^}]*)\}', fix, t), end='')
```

Frontier texkeys that map to v1 readable keys (use the readable key): e.g. `Izubuchi:2018srq` → `IzubuchiEtAl2018`, `Ji:2020ect` → `JiEtAl2021` (the LaMET RMP), `Ji:2013dva` → `Ji2013`, `Ma:2017pxb` → `MaQiu2018`, `Radyushkin:2017cyf` → `Radyushkin2017`, `Polyakov:1980ca` → `Polyakov1980`, `Jantzen:2011nz` → `Jantzen2011`, `Korchemsky:1987wg` → `KorchemskyRadyushkin1987`, `Ma:2019hjq` → `Ma2020`, `Libby:1978bx` → `LibbySterman1978b`, `Catani:2011st` → `CataniDeFlorianRodrigo2012`, `Collins:1984kg` → `CollinsSoperSterman1985a`, `Bodwin:1984hc` → `Bodwin1985`, `Nayak:2005rt` → `NayakQiuSterman2005b`; the full list is in §4.6.

**Keys to avoid / replace.** `Radyushkin1996` in `research/c_ee/ee_total.tex` (and `ee_bibitems.tex`) means Radyushkin, JINR Rapid Commun. 78 (1996) 96 (π² terms of $R$), which is **not** in the bib: delete it and cite `KrasnikovPivovarov1982` and `KataevStarshenko1995`. **Trap:** the alias table maps the survey label `Radyushkin1996` to `Radyushkin:1996nd` ("Scaling limit of deeply virtual Compton scattering", PLB 380 (1996) 417) — correct for the survey/exclusive snippets, wrong for the c_ee snippet. Run the alias-replacement script on c_ee material only after removing that citation.

**Errata and translations** are in the `note` field (printed). Non-standard fields `inspire`, `erratumdoi`, `reportNumber`, `archivePrefix`, `primaryClass` are ignored by `unsrt`.

---------------------------------------------------------------------------------------------------

## 1. Binding warnings

### 1.1 Carried over from v1 (unchanged)
- Collins (2011) uses $D_\mu=\partial_\mu+igA_\mu$; flip $g\to-g$ when copying Wilson-line formulas (survey §0.3). His soft factor and TMD fragmentation functions use $e^{+ik_T\cdot b_T}$ (eq. (13.35)); TMD PDFs in his scheme use our convention (survey §0.3; WRITER_SPEC v1 row 30 as made precise by the v1 audit, which supersedes the shorter remark in `spec/REFS_NOTES.md`).
- Qiu–Sterman NPB 378 (1992) 52 (`QiuSterman1992`) is about **direct-photon** SSA; the pion paper is `Qiu:1998ia`.
- BBL use $D^\mu=\partial^\mu+igA^\mu$; their "$M$" in $2{\rm Im}f_n/M^{d_n-4}$ is the heavy-quark pole mass.
- Ji PRL 78 (1997) 610 uses $\xi_{\rm Ji}=2\xi$; VGG 1999 use $\varepsilon_{0123}=+1$ (opposite of ours).
- Becher–Schwartz 2008 App. A (arXiv) prints a spurious $C_F$ in $\Gamma_1$; correct: $\Gamma_1=4C_F[(\frac{67}9-\frac{\pi^2}3)C_A-\frac{20}9T_Fn_f]$.
- MVV normalization: $a_s=\alpha_s/4\pi$, $P^{(0)}_{\rm MVV}=2P$, $\gamma^{(0)}_{\rm MVV}=-2\gamma$; $c^{(1)}_{2,\rm ns}=2C_2^q$, $c^{(1)}_{2,g}=4n_fC_2^g$.
- `SenIndumathiChoudhury2019` is a 2018 arXiv paper on dark matter that reproduces the Grammer–Yennie formulae; cite it only next to `GrammerYennie1973`, as 「as reproduced in」 (its eqs. 7–9).
- Rothstein–Stewart's announced "proof of factorization for Drell–Yan with SCET" does not exist (as of 2026-10); do not cite it. RS 2016 state that the S–S cancellation "taken alone is far from a proof".
- `Collins2023` is the Open-Access reissue of `Collins2011` (not a second edition); quote section numbers from `Collins2011`. Likewise `Collins1984` has a 2023 OA reissue (INSPIRE gives DOI 10.1017/9781009401807 for `Collins:1984xc`); cite `Collins1984`.
- `Collins2007` is an unpublished preprint; `Collins:2020euz` and `Beneke:2026miy` are arXiv preprints (say so).
- `Shifman2000`: booktitle *At the Frontier of Particle Physics* (World Scientific 2001), vol. 3, pp. 1447–1494 (v1 audit correction).

### 1.2 New in v2: corrections made while merging
| key | issue | resolution |
|---|---|---|
| `LatticeParton:2020uhz` | INSPIRE merges PRL 125 (2020) 192001 with PoS LATTICE2021 477 and exports the PoS DOI and a different title (lamet.bib has that version) | the yzliu version is kept: DOI 10.1103/PhysRevLett.125.192001 and the published PRL title (Crossref) |
| `Liu:2023onm` | lamet.bib gives JHEP volume "2024" | yzliu version kept: JHEP **02** (2024) 204 (JHEP convention volume = issue) |
| `Su:2026eta` | lamet.bib title contains a Unicode ξ inside math | yzliu version kept (`\pm\xi`) |
| `Ji:2022ezo` | published title in *Research* 8 (2025) 0695 differs from the arXiv title ("Large-momentum effective theory vs. short-distance operator expansion…") | yzliu version (published title) kept; say "arXiv title differs" if quoting the arXiv version |
| `Collins:2011zzd` | yzliu gives the 2011 DOI, others the 2023 OA DOI | both map to the v1 entries (`Collins2011` resp. `Collins2023`); cite `Collins2011` |
| `Bodwin:1984hc`, `Bodwin:1994jh` | others.bib (INSPIRE) carries the **erratum** DOIs (PRD 34 (1986) 3932; PRD 55 (1997) 5853) | the v1 entries `Bodwin1985`, `BodwinBraatenLepage1995` (original articles) are kept; mention the errata where relevant |
| `Piguet:1995er` | no publisher in INSPIRE | patched: Lecture Notes in Physics Monographs 28, Springer, Berlin, Heidelberg (Crossref) |
| `Zweig:1964jf` | INSPIRE exports an `@inbook` of the 1980 reprint volume (BibTeX would warn) | re-typed as `@techreport` CERN-TH-412 (1964), DOI 10.17181/CERN-TH-412, reprint noted |
| `Gardi:2024axt`, `Shifman2000` (v1 entries) | their printed `note` fields carried internal provenance remarks of the v1 audit ("Added by the spec audit …", "book reference corrected by the spec audit from INSPIRE …") | spec v2.1: removed from the printed notes (Shifman keeps "Talk at the 8th International Symposium on Heavy Flavor Physics (1999)"); provenance recorded here |
| `LatticeParton:2020uhz`, `Markoff1916` | printed `note` fields with internal remarks (INSPIRE merge of PRL 125 (2020) 192001 with PoS LATTICE2021 477; "Crossref also lists J. Grossmann") | spec v2.1: notes removed; Crossref lists J. Grossmann as a second "author" of the German version of Markov's memoir (presumably the translator; not verified) |
| `Bartels:1996wc` | INSPIRE exports DOI 10.1007/BF02909194 (ADS), which does not resolve in Crossref | spec v2.1: DOI 10.1007/s002880050285 (Crossref record of Z. Phys. C 72 (1996) 627) |
| `Blumlein:1996hb`, `Bartels:1995iu`, `Bartels:1996wc` | INSPIRE legacy titles/author string ("Blumlein", "G(1)", "g1 (x, Q**2)") | spec v2.1: Bl{\"u}mlein; titles with $g_1$, $g_1(x,Q^2)$, $x$ (Crossref titles) |
| title variants | `Ji:1998xh`, `Sterman:1986aj`, `Wilson:1969zs`, `Collins:1984kg`, `Libby:1978bx`, `Catani:2011st`, `Becher:2024nqc`, `Nayak:2005rt`, `Nayak:2006fm` differ from the v1 entries only in capitalization/hyphenation of the title, `Zimmermann:1972tv` in the journal abbreviation | v1 entries kept |

### 1.3 New in v2: preprints (arXiv only on 2026-10-10)
Mark 「（预印本）」 at the first citation in a unit and in every status paragraph that relies on them: `Collins:2020euz` (2007.04085), `Collins2007` (0708.4410), `Beneke:2026miy` (2608.25502), `Ji:2026vir` (2601.12189), `Su:2026eta` (2609.20545), `Liu:2021evw` (2102.07248), `Liu:2026npv` (2606.06277), `Liu:2023eve`, `Liu:2023tft`, `Liu:2026rew`, `Ishikawa:2016znu` (1609.02018), `Ji:2025mvk` (2504.09367), `Liu:2018hxv` (1810.05043), `NieMiera:2025mwj` (2510.17758), `Zhang:2023wea` (2304.12481), `Zhang:2026lle` (2605.03234), `Anastasiou:2025cvy`, `Anastasiou:2026kpm`, `Anastasiou:2026jta`, `Frob:2016mzv` (1603.08012), `Guida:2011np` (1103.5692), `Bodwin:2025zzi` (2512.11647), `Gamberg:2022lju` (2211.13209), `Becher:2026zon`, `Becher:2026iim`, `Collins:2018aqt` (1801.03960), and the v1 arXiv-only entries `Collins2007`, `Collins:2020euz`, `Beneke:2026miy`, `Muhlbauer:2020kut`, `SenIndumathiChoudhury2019`. `BoerEtAl2011` (INT report) and `BoussarieEtAl2023` (TMD Handbook) are arXiv documents; `Tyutin1975` is the Lebedev preprint LEBEDEV-75-39 (arXiv 0812.0580).

### 1.4 New in v2: frontier conventions and content warnings
- **$g$ sign.** The LaMET review `JiEtAl2021` (its eq. (44)) and Liu et al. use $D=\partial+igA$ and $W_n=P\exp[-ig\int ds\,n\cdot A]$ (YZLIU §2 translation table); in IJJSZ (`IzubuchiEtAl2018`) the light-cone link $P\exp(-ig\int A^+)$ and the space-like link $P\exp(-ig\int A^z)$ correspond to opposite covariant-derivative conventions, since $A^z=-A_z$ (LAMET §0.3 item 4). Other LaMET papers: check before copying a formula that is odd in $g$. All one-loop kernels are even in $g$ — but state the conversion (WRITER_SPEC_v2 §3 row 4).
- **Ioffe time.** LAMET.md: $\lambda=P\cdot z$; IJJSZ $\zeta=P^zz=-\lambda$; Radyushkin $\nu=-(p\cdot z)=-\lambda$; Ji et al. $\tilde\lambda=zP^z=-\lambda$ (row 40).
- **$L_z$ clash.** Liu et al. and Ji–Liu–Su write $L_z=\ln(\zeta_z/\mu^2)$; LAMET.md §1.1 writes $L_z$ for the coordinate log. The book uses $L_\zeta$ and $L_z$ (row 42).
- **CS exponent.** `Ji:2019ewn` eq. (22), `JiEtAl2021` eqs. (209)–(210), `Liu:2022nnk` eqs. (53), (75), arXiv:2106.05310v1 of `Ji:2021znw` (eqs. (49), (51), (73)) print $e^{K\ln(\zeta_z/\zeta)}$; the correct exponent is $\frac12\tilde K\ln(\zeta_z/\zeta)$ (VF-LAM-15; App Q row Q.11). The journal version of `Ji:2021znw` (PRD 105 (2022) 076014) is correct and notes the omission in its footnote 1 — never list it among the sources with the error.
- **Hybrid kernel.** `Ji:2020brr` (eq. hybridm2) and `JiEtAl2021` print a $\delta$ term that violates $\int C_{\rm hyb}=1$; `Su:2022fiu` (NPB 991 (2023) 116201) has the correct form (VF-LAM-10); the first published correction is `Chou:2022drv` eq. (35) (App Q row Q.8).
- **`Braun:2018brg` eq. (cR)** omits $q(x)\ln(1-x)$; their eqs. (t4-Qparallel), (t4-Qperp) are correct (VF-LAM-13).
- **$\Gamma_S$, $\gamma_C^{(2)}$, $L_b^2$ coefficient**: see VF-YZL-3, VF-YZL-7 (errata of `Liu:2022nnk`, `Ji:2021znw`, `JiEtAl2021`, `Ji:2019ewn`).
- **`Guo:2021ibg`**: gluon-GPD normalization corrected by the authors in `Guo:2023pqw` (factor $\frac12$; $|G|^2$ factor 4) — use the 2023 normalization.
- **`Liu:2022nnk` App. F** says "edge of the wedge" where the Bargmann–Hall–Wightman theorem (`Streater:1989vi`) is meant.
- **Yizhuang Liu**: never print a Chinese name (unverified); do not reproduce career data (the habilitation summary contains personal identifiers).
- **`Collins:2020euz`** (Landau condition): complete proof only for denominators at most quadratic with the sign condition; arXiv v1 only; Collins himself calls the conditions artefacts of the method.
- **OPE status** (`Hollands:2007zg`, `Frob:2016mzv`, `Hollands:2011gf`): pure Yang–Mills / scalar models; no self-contained proof for QCD with quarks; convergence only for $\varphi^4_4$ at fixed loop order (OTHERS §2.7). OTHERS §2.7 grades the all-order perturbative OPE for QCD with quarks "[R] in renormalized PT as a combination of classical results"; spec v1 did **not** adopt this (`spec/FINAL_OUTLINE.md` §0.9 item 4, under decision D3 of its §0.3) and keeps `thm:dis-ope` at [A] — the R_OPE qualifier of WRITER_SPEC_v2 §4 says so. Do not cite these papers as a proof of the OPE for QCD with quarks unless FINAL_OUTLINE_v2 changes the grade.
- **`Schwartz:2018obd` vs `RothsteinStewart2016`** claim (v) and `Gaunt2014`: cite both sides with their exact scope (pure Glauber ladders, single-scale observables).
- **`Banfi:2025mra`** (1-jettiness CVLs): LL coherence-violation approximation; confirmed for the $qg\to q$ channel in SCET with Glauber and new modes by `Becher:2026kbr` (two groups, different methods).
- **`Becher:2024kmk`**: "our analysis does not amount to a proof of PDF factorization" (authors' words, as quoted in OTHERS §4.5; the companion JHEP paper was read at abstract level only).
- **PDG 2024** (`ParticleDataGroup:2024cfk`): the world average $\alpha_s(m_Z^2)=0.1180\pm0.0009$ is eq. (9.25) of review 9 (Quantum Chromodynamics, revised August 2023) — read in the PDF on 2026-10-10.
- **`Andrasi:1980qw`** (NPB 182 (1981) 104, "Soft divergences in perturbative QCD") is the "Andrási et al. 1981" of refdoc S60 and was already in v1; `DiLietoEtAl1981` likewise.
- **The reference document is never cited** (WRITER_SPEC_v2 §6.10); its bibliography is not a source.

### 1.5 New in v2.1: attribution rules from `verify/CLAIMS.md` (A01–A28; verdicts of the verify patch v2.3)

The claims register `verify/CLAIMS.md` (compiled 2026-10-10 by the verification workflow) lists 28 delicate attribution claims. **Verdicts (verify patch v2.3, `verify/CLAIM_VERDICTS.md`):** A01–A03, A05, A07–A10, A12–A28 confirmed — the rules stand, with the precisions written into the rows; A04, A06 and A11 refuted in single items — the rows are corrected; the A20 row follows the correction R-M20. "Abstract level" means that our material documents only the INSPIRE abstract: write 「据其摘要」 or hedge. Keys are merged keys.

| claim | rule for writers | keys |
|---|---|---|
| A01 | NPB 964 (2021) 115311 (hybrid renormalization) is `Ji:2020brr` by X. Ji, Yizhuang Liu, A. Schäfer, W. Wang, Y.-B. Yang, J.-H. Zhang, Y. Zhao (the bib entry is correct). "Ji, Liu, Liu, Zhang, Zhao" is the author list of the RMP `JiEtAl2021`; never copy the author string of LAMET.md §0.3 item 1. `Ji:2019ewn` (PLB 811) is Ji, Yizhuang Liu, Yu-Sheng Liu. | `Ji:2020brr`, `JiEtAl2021`, `Ji:2019ewn` |
| A02 | Never print a Chinese name for Yizhuang Liu (our files contain two conflicting renderings; none is verified) and no career or personal data (WRITER_SPEC_v2 §2 item 3). | — |
| A03 | Priority words only in the printable forms of `verify/CLAIM_VERDICTS.md` A03 (confirmed), each with 「据我们所知（INSPIRE 检索，2026 年 10 月）」 — (A1) `Ji:2019sxk` time-independent soft factor; (A3) `Liu:2022nnk` classification (cusp-angle analyticity: `KorchemskyRadyushkin1987`); (A5) $S_I$ by JLL (precursor $g^S_q$: `EbertStewartZhao2019`); (A6) `Liu:2023pjb`; (B1) `Ji:2019ewn`; (C2) `Ji:2023pba` (earlier: `Gao:2021hxl`); (D1) `Liu:2024omb` (vacuum-correlator precedent `Beneke:1998eq`). In particular `LatticeParton:2020uhz` is never "the first lattice extraction of the Collins–Soper kernel" (`Shanahan:2020zxr` is earlier); "first lattice extraction of $S_I$" only after verification. Earlier Euclidean ("bent") soft functions: `Ji:2014hxa`, `Ebert:2019okf`; earlier time-ordering arguments in other regulators: `Vladimirov:2016dll`, `Vladimirov:2017ksc`. The 2D-model results are model results ([P] as QCD statements). | `Ji:2019sxk`, `Liu:2022nnk`, `Liu:2023pjb`, `Ji:2019ewn`, `Ji:2023pba`, `Liu:2024omb`, `LatticeParton:2020uhz`, `Shanahan:2020zxr`, `Vladimirov:2016dll`, `Vladimirov:2017ksc`, `Ji:2014hxa`, `Ebert:2019okf` |
| A04 | Quote proof-status self-assessments exactly: `Liu:2022nnk` §6 (all proofs "except the ones for the analyticity" follow the usual standards of the TMD literature); `Ji:2019ewn` gives a "sketch". Independent confirmations of quasi-TMD factorization: `Vladimirov:2020ofp` (an SCET$_{\rm II}$ derivation with a one-loop check — A04 corrected), `Ebert:2022fmh` (all orders, large-rapidity scheme), NNLO `delRio:2023pse` and `Ji:2023pba`. The time-ordering theorem is [A] conditional on DR analyticity; $N_m$ beyond large $\beta_0$ is [C]; do not print an exact loop order for the ultrasoft effect mentioned in `Liu:2022nnk`; dividing out staple self-interactions goes back to `Collins:2008ht` and `Ji:2018hvs`. The multiplicative-renormalizability proofs used are not Liu's. **A04 corrections (v2.3):** the APPB §4.4 remark that a detailed explanation beyond one loop "is not presented" concerns `Collins:2011ca` (APPB ref. [47]), not `CollinsSoper1981` (APPB App. D criticises the latter differently: a heuristic IR-safety argument with a loophole for linear divergences); `Ji:2018hvs` has five authors; cite the "open question" quote of `Vladimirov:2017ksc` from the JHEP version (p. 32). | `Liu:2022nnk`, `Ji:2019ewn`, `Vladimirov:2020ofp`, `Ebert:2022fmh`, `delRio:2023pse`, `Ji:2023pba`, `Collins:2008ht`, `Ji:2018hvs`, `Liu:2023onm`, `Liu:2021evw` |
| A05 | LaMET: exponential decay of space-like correlators is `Ji:2026vir` (preprint), building on `Fredenhagen:1984bz`; the matching theorem has two routes, `IzubuchiEtAl2018` (coordinate-space OPE) and `Ma:2014jla`/`MaQiu2018` (collinear factorization) — the RMP `JiEtAl2021` states that the proof is given only for perturbative free-quark states; `Ji:2014gla` asserted order-by-order provability without proof; renormalizability: `Ji:2017oey` (auxiliary field; the space-like extension is asserted), `Green:2017xeu`, `Ishikawa:2017faj` (degree counting, not full BPHZ); check the scope of `Braun:2020ymy` (three loops vs all orders) before quoting it; support: `Radyushkin:1983wh` (recalled — verify before attributing content); the threshold constants $c_a$, $c_H$ of `Ji:2023pba` were fitted; quote the "first" claim of `Avkhadiev:2024mgd` as theirs. | `Ji:2026vir`, `Fredenhagen:1984bz`, `IzubuchiEtAl2018`, `Ma:2014jla`, `MaQiu2018`, `JiEtAl2021`, `Ji:2014gla`, `Ji:2017oey`, `Green:2017xeu`, `Ishikawa:2017faj`, `Braun:2020ymy`, `Radyushkin:1983wh`, `Ji:2023pba`, `Avkhadiev:2024mgd` |
| A06 | Literature-absence statements only in the form 「据我们截至 2026 年 10 月的文献检索，尚未见……」 with the search basis, never as facts; each of the eleven items of CLAIMS A06 (Zimmermann-level OPE for space-like Wilson-line operators; Glauber analysis for quasi-TMDs; N³LO quasi-PDF kernel; refutation of the Rossi–Testa resolution; the announced RS SCET proof for DY; BBNS endpoint refactorization; twist-3 SSA factorization; flow-equation OPE for QCD with quarks; multilocal BRST classification; Gordan's theorem in the Landau literature; DGOPS: Glauber cancellation established only for DY) needs a repeated search at print time. Preprints are marked. **A06 corrections (v2.3):** item 3 is false — the N³LO non-singlet kernel exists (`Cheng:2024wyu`; used by `Ji:2024hit`); item 4 is false as stated — the Rossi–Testa resolution was contested in 2017–2018 with published exchanges on both sides (`Rossi:2018zkn`, `Rossi:2017muf`; replies `Karpie:2018zaz`, `Radyushkin:2018nbf`); the other items hold (item 8 not exhaustively; item 10 partially checked). | `RothsteinStewart2016`, `Diehl:2015bca`, `Collins:2020euz`, `Frob:2016mzv`, `Beneke:2026miy`, `Gamberg:2022lju`, `Bodwin:2025zzi` |
| A07 | GPDs at $x=\pm\xi$: present `Braun:2024snf` and `Su:2026eta` (preprint) side by side: not strictly contradictory (no leading-twist soft term vs a first-power correction), neither paper criticises the other (A07 confirmed); status [C]; mention the kinematic twist-3 discontinuities of `Braun:2023alc`. | `Braun:2024snf`, `Su:2026eta`, `Braun:2023alc`, `CollinsFreund1999` |
| A08 | `Collins:2020euz` and `Muhlbauer:2020kut` are arXiv-only (re-check at print time); grade per FINAL_OUTLINE_v2 (decision D3: Collins' Theorem 1 is not graded [R]†). | `Collins:2020euz`, `Muhlbauer:2020kut` |
| A09 | OPE rigour: Zimmermann (scalar theory); `Hollands:2007zg` (pure Yang–Mills, gauge-invariant operators); `Frob:2016mzv` (preprint; bounds for pure YM only); convergence only in $\varphi^4_4$ at fixed loop order (`Hollands:2011gf`, `Holland:2014pna`); the theory class of `Anikin:1978tj` is unverified; the OTHERS grade "[R] in PT via classical results" is not adopted (§1.4). | `Hollands:2007zg`, `Frob:2016mzv`, `Hollands:2011gf`, `Holland:2014pna`, `Anikin:1978tj`, `IzubuchiEtAl2018` |
| A10 | Method of regions: Euclidean limits rigorous (`Smirnov:1990rz`); `Jantzen2011` conditional; `Semenova:2018cwy` (leading order per facet, all orders for one facet); `Gardi:2022khw`; "regions = lower facets" fails in Minkowski kinematics (`Gardi:2024axt`, abstract level); three-loop Glauber region `Becher:2024kmk` (abstract level). **The off-shell Sudakov regions example is from `BecherBroggioFerroglia2015` §2.2** (massive exchange: `Jantzen2011` §6, BBF §2.3), **not** from `BenekeSmirnov1998`, which introduced the method for the threshold expansion. | `Smirnov:1990rz`, `Jantzen2011`, `Semenova:2018cwy`, `Gardi:2022khw`, `Gardi:2024axt`, `Becher:2024kmk`, `BecherBroggioFerroglia2015`, `BenekeSmirnov1998` |
| A11 | Eikonal Glauber phase: cite `AybatSterman2009` eq. (14) and `RothsteinStewart2016` eqs. (9.1), (9.18)–(9.19), (11.12)–(11.13) — not "Cheng–Wu (verify)"; `Cheng:1969eh` only for the QED history. RS is supporting evidence, not a proof ("far from a proof of factorization, even in the abelian case"); RS §10.1–10.3 do treat the $n$–$\bar n$ production current at one and two loops (Glauber phases explicit in SCET$_{\rm II}$, equal to the soft zero-bin, or carried by ultrasoft graphs in SCET$_{\rm I}$) and expect the same at any order without proof — cite them for $e^+e^-$ only as one- and two-loop evidence (A11 item (3), corrected in v2.3); the BPS field redefinition does not remove Glauber couplings (RS §5.1); `Collins2011` §14.4.5 for "works equally well for the TMD case". | `AybatSterman2009`, `RothsteinStewart2016`, `Cheng:1969eh`, `Collins2011`, `CollinsSoperSterman1988` |
| A12 | Dipole formula: exact through two loops; non-dipole terms from three loops (`Almelid:2015jia`, abstract level) → "beyond two loops: [V]"; `Caron-Huot:2013fea` §4 rules it out from four loops by a Regge argument. | `Almelid:2015jia`, `Caron-Huot:2013fea` |
| A13 | `Collins2011` quotations and page numbers (pp. 110, 407–410, 553, 561–562, 569–571, 580; eqs. (2.2), (13.35), (13.40)) must be checked against the book before printing; quote `Collins2011` (the OA reissue `Collins2023` has not been compared page by page); $g_{\rm Collins}=-g$; his soft factor uses $e^{+ik\cdot b}$. | `Collins2011`, `Collins2023`, `Collins:2012uy` |
| A14 | DY history (BBL 1981/1989, Bodwin 1985 and erratum, Lindsay–Ross–Sachrajda, Brandt–Frenkel–Taylor, DFT 1980/Di'Lieto et al. 1981/Andrási et al. 1981, Frenkel–Gatheral–Taylor, Catani–Ciafaloni–Marchesini, CSS 1989 §10.2 ($m^4/s^2$), Basu–Ramalho–Sterman, Frye et al. 2019, CSS 1986 "conjecture", TMD Handbook §2.11.4): abstract level — report, with 「据其摘要」 where appropriate. | `BodwinBrodskyLepage1981`, `Bodwin:1988fs`, `Bodwin1985`, `Lindsay:1982pu`, `Lindsay:1982gd`, `Brandt:1988xt`, `DoriaFrenkelTaylor1980`, `DiLietoEtAl1981`, `Andrasi:1980qw`, `Frenkel:1983di`, `Catani:1985xt`, `CollinsSoperSterman1989`, `Basu:1984ba`, `Frye:2018xjj`, `Collins:1985gm`, `BoussarieEtAl2023`, `CollinsSoper1981` |
| A15 | DIS/DY attributions are recalled: the DIS-scheme gluon (`DiemozEtAl1988`, cite with "(见)"), the DIS scheme (`AltarelliEllisMartinelli1979`), $F_L$ at $O(\alpha_s)$ (`AltarelliMartinelli1978`), BBDM sum-rule values (via Muta); the $\overline{\rm MS}$ form of the DY $\Delta_{q\bar q}$ must not be attributed to AEM (they used the DIS scheme); the first full $O(\alpha_s^2)$ DY is `HambergVanNeervenMatsuura1991`. | `DiemozEtAl1988`, `AltarelliEllisMartinelli1979`, `AltarelliMartinelli1978`, `BardeenEtAl1978`, `FurmanskiPetronzio1982`, `HambergVanNeervenMatsuura1991` |
| A16 | $R_{e^+e^-}$ finiteness: `PoggioQuinn1976` is physics-level; rigorous versions `LowensteinZimmermann1975`, Lowenstein 1976, `BreitenlohnerMaison1977a` (I–III; the hypotheses of II are met by massless QCD in covariant gauges including ghosts — BM name Yang–Mills with vector-like fermions, ghosts are not discussed explicitly; N24); $r_2$: `ChetyrkinKataevTkachov1979`, `DineSapirstein1979`, `CelmasterGonsalves1980a`. | `PoggioQuinn1976`, `LowensteinZimmermann1975`, `BreitenlohnerMaison1977a`, `ChetyrkinKataevTkachov1979`, `DineSapirstein1979`, `CelmasterGonsalves1980a` |
| A17 | Carlson's theorem: Titchmarsh §5.81 (verified in the book) and Boas Thm 9.2.1 (as cited by Waldschmidt); recalled references of c_pdf (Collins–Soper 1982, Altarelli–Parisi 1977, Curci–Furmanski–Petronzio 1980, Catani–Seymour 1997, Jaffe 1983, Joglekar–Lee 1976, ESW ch. 4) are checked on INSPIRE before content is attributed; MVV normalization: $\gamma^{(0)}_{\rm MVV}=-2\gamma$. | `MochVermaserenVogt2004` |
| A18 | Grammer–Yennie: the original K-photon is symmetric; the one-sided form with $i0$ is Collins' adaptation — cite `GrammerYennie1973` with `SenIndumathiChoudhury2019` as 「as reproduced in」; soft-photon theorem: `Weinberg1965`; Collins section and page numbers used by c_wilson are checked before printing. | `GrammerYennie1973`, `SenIndumathiChoudhury2019`, `Weinberg1965`, `Collins2011` |
| A19 | TMD/Sivers: transverse links `JiYuan2002`, `BelitskyJiYuan2003` (abstract level); the sign reversal is `Collins2002` after `BrodskyHwangSchmidt2002`; universality of T-odd FFs `CollinsMetz2004`, `MeissnerMetz2009`; "the $u$-quark Sivers function is negative" is never printed without a fit citation (e.g. `Bury:2020vhj`). | `JiYuan2002`, `BelitskyJiYuan2003`, `Collins2002`, `BrodskyHwangSchmidt2002`, `CollinsMetz2004`, `MeissnerMetz2009`, `AybatRogers2011` |
| A20 | Glauber/SLL literature: `CataniDeFlorianRodrigo2012` do **not** show a cancellation ($P^{(2)}$ not factorized; "may invalidate the factorization theorem of mass singularities starting at the N³LO" is their statement); FSS: in pure QCD the two-loop effect vanishes and a violation is expected at three loops (one step of that argument is not proven); the sentence of `Guan:2024hlf` that the effects "appear to cancel in pure-QCD cross sections up to NNLO" is a literature summary, not their result; in $\mathcal N=4$ SYM the cancellation is shown by Henn et al. (PRD 112 (2025) 076003); never call a two-loop cancellation statement "wrong" (R-M20); Collins' DDIS proof escapes the $r^-$ pinch by deforming $r^+$; `RogersMulders2010`: double transverse-spin asymmetry (unpolarized non-abelian case only indicated); the first SLL coefficient is quoted from `ForshawKyrieleisSeymour2006` (not recomputed); `Becher:2021zkk`: $2\to1$ from four loops, $2\to0$ from five loops; CDF's "factor $O(10)$" from the 2012 CDF summary; H1 vs ZEUS diffractive photoproduction is an open tension. | `CataniDeFlorianRodrigo2012`, `ForshawSeymourSiodmok2012`, `Guan:2024hlf`, `Collins1998a`, `RogersMulders2010`, `ForshawKyrieleisSeymour2006`, `Becher:2021zkk` |
| A21 | Exclusive: hard pseudoscalar-meson production and the pion pole in $\tilde E$ is `Frankfurt:1999fp` (PRD 60 (1999) 014010), **not** PRL 84 (2000) 2589 (decuplet baryons); NLO kernels (Field–Gupta–Otto–Chang 1981, Dittes–Radyushkin 1981, Braaten–Tse 1987, Melić–Nižić–Passek 1999) are cited, not re-derived; the Lepage–Brodsky normalization is recalled; the soft-overlap $1/Q^4$ scaling is quoted, not derived. | `Frankfurt:1999fp`, `LepageBrodsky1980`, `EfremovRadyushkin1980`, `CollinsFreund1999`, `Ji1997a` |
| A22 | SCET: PRD 66 (2002) 054005 is the BPS power-counting paper; the endpoint-singularity paper is `Bauer:2002aj` (PRD 67 (2003) 071502); the BPS footnote on reparametrization refers to `BauerStewart2001`; charming penguins: report BBNS 2005 vs BPRS 2005 without verdict; BBL sign flips (WRITER_SPEC_v2 §3 row 4); the $B\to D\pi$ statement includes the endpoint-suppression assumption. | `Bauer:2002aj`, `BauerStewart2001`, `BauerPirjolStewart2002`, `Bauer:2004tj`, `BodwinBraatenLepage1995` |
| A23 | A23 confirmed: the theory class of `Anikin:1978tj` is open (never cite it as a QCD proof); `Lowenstein:1974qt` (BPHZL, massless $A^4$, Goldstone and pre-Higgs models) does not cover gauge-fixed QCD; `Frye:2018xjj`: a sum over initial **or** final states suffices; `Gaunt2014`: shown vs suggested (E36); `AybatSterman2009`: an outline, not a proof; the other items as in `verify/CLAIM_VERDICTS.md` A23. | `Anikin:1978tj`, `Lowenstein:1974qt`, `Frye:2018xjj`, `Gaunt2014`, `AybatSterman2009`, `ForshawSeymourSiodmok2012`, `Collins:1985gm`, `Collins1998b`, `DoriaFrenkelTaylor1980`, `DiLietoEtAl1981`, `Mankiewicz:1999tt`, `Braun:2018brg`, `Shifman2000` |
| A24 | Misconception-box attributions: Collins 1993 → Collins 2002 after BHS 2002; T-odd FF universality; transverse links; Lam–Tung violated at $O(\alpha_s^2)$; DFT/Di'Lieto; 't Hooft-model scaling (Callan–Coote–Gross 1976, Einhorn 1976: journal data recalled); Burkardt–Koike $\delta(x)$ terms (recalled); $P^+_{\rm NS}-P^-_{\rm NS}$ at NLO from Curci–Furmanski–Petronzio. Unverified journal data → 「（文献待补）」 rather than a guessed key. | `Collins1993`, `Collins2002`, `BrodskyHwangSchmidt2002`, `JiYuan2002`, `DoriaFrenkelTaylor1980`, `DiLietoEtAl1981`, `CollinsMetz2004`, `MeissnerMetz2009`, `BelitskyJiYuan2003` |
| A25 | Quarkonium/EW/DPS (abstract level): NQS gauge completion necessary at NNLO, all orders in $v$ for octet→singlet ([P]); Bodwin et al. 2020: two-loop universality with stated differences; $\eta_c$ tension: report both sides; EW Bloch–Nordsieck violation `Ciafaloni:2000df` ([V]); non-factorizable EW corrections `Baumgart:2018ntv` ([V] as computed); DPS Glauber cancellation for double DY `Diehl:2015bca`; `Ebert:2021jhy` is conditional on a Glauber assumption; `Gamberg:2022lju` is a preprint. | `NayakQiuSterman2005a`, `NayakQiuSterman2005b`, `NayakQiuSterman2006`, `Bodwin:2019bpf`, `Ciafaloni:2000df`, `Baumgart:2018ntv`, `Diehl:2015bca`, `Ebert:2021jhy`, `Gamberg:2022lju` |
| A26 | Grade conflicts between our materials are settled by FINAL_OUTLINE_v2 (decision D3): perturbative OPE for QCD with quarks [A]; Collins 2020 Theorem 1 not [R]†; multiplicative renormalizability of space-like Wilson-line operators [A] (LAMET), not [R] (YZLIU); two-loop threshold values [P] (a fit cannot certify [R]); `lem:appD-gordan` as the outline grades it. | — |
| A27 | Sivers sign change: "consistent, not decisive" (COMPASS 2017 and 2024, STAR 2016 "if TMD evolution effects are small", `Bury:2020vhj` cannot exclude the same sign, `Echevarria:2020hpy` tension); twist-3 evolution: `Braun:2009mi` vs `Kang:2008ey`, JAM 2020 common-origin analysis `Cammarota:2020qcw`; Collins 1998 (heavy quarks): remainder uniform in $M$ (abstract quote). | `COMPASS:2017jbv`, `COMPASS:2023vqt`, `STAR:2015vmv`, `Bury:2020vhj`, `Echevarria:2020hpy`, `Braun:2009mi`, `Kang:2008ey`, `Kang:2011hk`, `Cammarota:2020qcw`, `Collins1998b` |
| A28 | NLP endpoint factorization (OTHERS §5.5): endpoint divergences are generic and $\overline{\rm MS}$ renormalization of the individual functions is insufficient ([R] by examples); $h\to\gamma\gamma$ ($b$ loop): renormalized theorem [A], resting on SCET assumptions (refactorization conditions proven within SCET); $gg\to h$ via light quarks [A]; threshold DY at NLP: bare $d$-dimensional factorization [P]; LL resummation at NLP [A] at LL only; `Beneke:2026miy` [A]† preprint; `Bodwin:2025zzi` (preprint) scrutinizes ingredients. | `Liu:2019oav`, `Liu:2020wbn`, `Beneke:2019oqx`, `Beneke:2026miy`, `Bodwin:2021cpx`, `Bodwin:2021epw`, `Bodwin:2023asf`, `Bodwin:2025zzi` |

---------------------------------------------------------------------------------------------------

## 2. What each v1 key supports

Unchanged: `spec/REFS_NOTES.md` §1 (refs-agent entries), §2 (survey entries with [txt]/[abs]/[bib]), §3 (supplement) and §4 (classical mathematics) remain binding for the 646 v1 keys. Chapter numbers inside those notes are historical (they refer to older outlines); always locate a citation by the statement label. The v1 per-chapter "Key citation keys" of `spec/FINAL_OUTLINE.md` carry over to the v2 chapter with the same key (chapter number + 1; `lattice` → Ch22; `summary` → Ch25), and to Ch2 `qcd` / Ch3 `prelim` for the two halves of v1 Ch2.

---------------------------------------------------------------------------------------------------

## 3. Citation lists for the new v2 units

Generated by `spec_v2/checks/refs_unit_lists.py` (all keys mapped through the aliases and checked in the bib). The frontier lists contain every key the frontier report cites in the section — not every key must be cited in the book; the frontier reports say what each source supports and at which reading depth (§4).

### 3.1 Ch2 `qcd` (pedagogical QCD; v1 Ch2 keys plus the spec-v2 additions)

**gauge theory, colour, quarks** (6 keys)

`Yang:1954ek`, `Gell-Mann:1964ewy`, `Zweig:1964jf`, `Greenberg:1964pe`, `Han:1965pf`, `Fritzsch:1973pi`

**quantization, ghosts, BRST, unitarity** (9 keys)

`Faddeev:1967fc`, `BecchiRouetStora1975`, `BecchiRouetStora1976`, `Tyutin1975`, `KugoOjima1979`, `tHooft1971`, `Taylor1971`, `Slavnov1972`, `tHooftVeltman1972b`

**regularization, renormalization, RG** (17 keys)

`tHooftVeltman1972`, `tHooft1973`, `BardeenEtAl1978`, `Gell-Mann:1954yli`, `Callan:1970yg`, `Symanzik:1970rt`, `Collins1984`, `Joglekar:1975nu`, `Joglekar:1976eb`, `Joglekar:1976pe`, `Kluberg-Stern:1974iel`, `Henneaux:1993jn`, `DixonTaylor1974`, `Collins:1994ee`, `Hamberg:1991qt`, `Breitenlohner:1975hg`, `Breitenlohner:1976te`

**beta function, asymptotic freedom, alpha_s** (13 keys)

`GrossWilczek1973a`, `Politzer1973`, `Coleman:1973sx`, `Caswell1974`, `Jones1974`, `Tarasov:1980au`, `Larin:1993tp`, `vanRitbergen:1997va`, `Czakon:2004bu`, `Baikov:2016tgj`, `Herzog:2017ohr`, `Nielsen:1980sx`, `ParticleDataGroup:2024cfk`

**IR divergences and IR safety (introductory)** (5 keys)

`BlochNordsieck1937`, `Kinoshita1962`, `LeeNauenberg1964`, `StermanWeinberg1977`, `EllisRossTerrano1981`

**textbooks** (8 keys)

`PeskinSchroeder1995`, `Itzykson:1980rh`, `Weinberg1996`, `Muta2010`, `EllisStirlingWebber1996`, `Sterman1993`, `Collins2011`, `Wilson:1974sk`


### 3.2 Ch22 `lamet` (keys cited in LAMET.md §1–§9; TMD sections go to Ch23)

**LAMET §1. Conventions and the objects** (7 keys)

`IzubuchiEtAl2018`, `Ji2013`, `MaQiu2018`, `Orginos:2017kos`, `Radyushkin:1983wh`, `Radyushkin2017`, `Radyushkin:2018cvn`

**LAMET §2. The LaMET principle: content, formalization, status** (9 keys)

`Braun:2018brg`, `Hatta:2013gta`, `Ji2013`, `Ji:2014gla`, `Ji:2020byp`, `JiEtAl2021`, `Ji:2024oka`, `Liu:2023onm`, `Ma:2014jla`

**LAMET §3. Renormalization of space-like Wilson-line operators** (42 keys)

`Alexandrou:2017huk`, `Bagan:1993zv`, `Beneke:1994sw`, `Bigi:1994em`, `BrandtNeriSato1981`, `Braun:2018brg`, `Braun:2020ymy`, `Briceno:2017cpo`, `Briceno:2018lfj`, `Chen:2016fxx`, `Chen:2017mie`, `Chen:2017mzz`, `Chetyrkin:2003vi`, `Constantinou:2017sej`, `Craigie:1980qs`, `Dorn:1986dt`, `Dotsenko:1979wb`, `Gao:2023lny`, `Green:2017xeu`, `Green:2020xco`, `Holligan:2023rex`, `Ishikawa:2016znu`, `Ishikawa:2017faj`, `IzubuchiEtAl2018`, `Ji:2015jwa`, `Ji:2017oey`, `Ji:2020brr`, `JiEtAl2021`, `LatticeParton:2018gjr`, `LatticePartonLPC:2021gpi`, `Li:2018tpe`, `Monahan:2016bvm`, `Monahan:2017hpu`, `Orginos:2017kos`, `Polyakov1980`, `Radyushkin2017`, `Stefanis:1983ke`, `Stewart:2017tvs`, `Zhang:2018diq`, `Zhang:2023bxs`, `Zhang:2024omt`, `Zhao:2023ptv`

**LAMET §4. The matching (factorization) theorem for quasi-PDFs** (39 keys)

`Alexandrou:2019lfo`, `Balitsky:2019krf`, `Bhattacharya:2020jfj`, `Bhattacharya:2020xlt`, `Braun:2018brg`, `Braun:2020ymy`, `Braun:2021aon`, `Braun:2021gvv`, `Chen:2020arf`, `Chen:2020iqi`, `Chen:2020ody`, `CurciFurmanskiPetronzio1980`, `EllisEtAl1979`, `Gao:2021dbh`, `Good:2025daz`, `Ishikawa:2017faj`, `IzubuchiEtAl2018`, `Ji:2017oey`, `JiEtAl2021`, `Ji:2023pba`, `Ji:2025mvk`, `LatticeParton:2018gjr`, `LatticeParton:2022xsd`, `Li:2020xml`, `Lin:2018pvv`, `Liu:2018hxv`, `Ma:2014jla`, `MaQiu2018`, `NieMiera:2025mwj`, `Radyushkin:2018cvn`, `Stewart:2017tvs`, `Su:2022fiu`, `Wang:2017qyg`, `Wang:2019tgg`, `Wilson1969`, `XiongEtAl2014`, `Yao:2022vtp`, `Zhang:2018ggy`, `Zimmermann1973`

**LAMET §5. Power corrections** (10 keys)

`Alexandrou:2015rja`, `Braun:2018brg`, `Braun:2024snf`, `Chen:2016utp`, `Ji:2020brr`, `Ji:2024oka`, `Liu:2023onm`, `Radyushkin:2017ffo`, `Su:2022fiu`, `Zhang:2023bxs`

**LAMET §6. Threshold factorization and resummation** (10 keys)

`BecherNeubertPecjak2007`, `Chen:2020ody`, `Gao:2021hxl`, `Holligan:2025baj`, `Jain:2008gb`, `Ji:2021znw`, `Ji:2023pba`, `Ji:2024hit`, `Li:2020xml`, `Sterman1987`

**LAMET §7. The Fourier transform: long-distance behaviour, analyticity, and the "inverse problem"** (8 keys)

`Chen:2025cxr`, `Dutrieux:2025jed`, `Fredenhagen:1984bz`, `Gao:2021dbh`, `Ji:2024oka`, `Ji:2026vir`, `Karpie:2019eiq`, `Su:2022fiu`

**Fourier step, classical harmonic analysis (spec v2.1)** (2 keys) — the recoverable-mode count of VF-LAM-17 (LAMET §7.2 names these papers; they are not in INSPIRE): `SlepianPollak1961` (prolate spheroidal functions as eigenfunctions of time–frequency limiting), `LandauWidom1980` (the eigenvalue-counting formula $N(\epsilon)=\frac{2\lambda_L}\pi+\frac1{\pi^2}\ln\frac{1-\epsilon}\epsilon\ln\lambda_L+o(\ln\lambda_L)$ in our variables). Bibliographic level only: the formula was checked numerically by the LaMET agent (`s7`), the papers were not read.

**LAMET §8. LaMET and short-distance factorization (SDF): equivalence, contrast, critiques** (20 keys)

`Braun:2007wv`, `Briceno:2017cpo`, `ChambersEtAl2017`, `DetmoldLin2006`, `IzubuchiEtAl2018`, `Ji:2017rah`, `Ji:2022ezo`, `Joo:2019jct`, `Joo:2020spy`, `Karpie:2018zaz`, `Liu:1993cv`, `Orginos:2017kos`, `Radyushkin2017`, `Radyushkin:2017lvu`, `Radyushkin:2018cvn`, `Radyushkin:2019mye`, `Rossi:2017muf`, `Rossi:2018zkn`, `Zhang:2018ggy`, `Zhang:2026lle`

**LAMET §9. Off-forward and exclusive objects: GPDs, DAs, LFWFs, heavy-meson and baryon LCDAs, $\Delta G$, DPDs** (26 keys)

`Beneke:2023nmj`, `Bhattacharya:2022aob`, `Braun:2023alc`, `Braun:2024snf`, `CollinsFreund1999`, `Deng:2023csv`, `Han:2024fkr`, `Hatta:2013gta`, `Holligan:2023rex`, `Jaarsma:2023woo`, `JiOsborne1998`, `Ji:2013fga`, `Ji:2015qla`, `Ji:2021znw`, `Ji:2025mvk`, `LatticeParton:2022zqc`, `Liu:2018tox`, `Liu:2019urm`, `Ma:2022ggj`, `Radyushkin1997`, `Radyushkin:2019owq`, `Su:2026eta`, `Xiong:2015nua`, `Yao:2022vtp`, `Zhang:2017bzy`, `Zhang:2023wea`


### 3.3 Ch23 `yzliu` (YZLIU.md §3.A–§3.E and LAMET.md §10–§11)

**YZLIU §3.A Euclidean formulation of TMD soft physics** (28 keys)

`Becher:2009kw`, `Bogner:2010kv`, `CollinsSoper1981`, `CollinsMetz2004`, `Collins:2008ht`, `Collins:2011ca`, `Collins2011`, `Ebert:2019okf`, `Echevarria:2015byo`, `FrenkelTaylor1984`, `Gatheral1983`, `Grozin:2015kna`, `Ji:2014hxa`, `Ji:2018hvs`, `Ji:2019ewn`, `Ji:2019sxk`, `JiEtAl2021`, `Ji:2021znw`, `Ji:2023pba`, `KorchemskyRadyushkin1987`, `KugoOjima1979`, `Li:2016axz`, `Liu:2022nnk`, `Liu:2023pjb`, `Moult:2018jzp`, `Streater:1989vi`, `Vladimirov:2016dll`, `Vladimirov:2017ksc`

**YZLIU §3.B Quasi-TMD factorization (LaMET for TMDs)** (21 keys)

`Chen:2020ody`, `Collins2011`, `EbertStewartZhao2019`, `Ebert:2019okf`, `Ebert:2022fmh`, `Ji2013`, `Ji:2014gla`, `Ji:2014hxa`, `Ji:2018hvs`, `Ji:2019ewn`, `Ji:2019sxk`, `JiEtAl2021`, `Ji:2020jeb`, `Ji:2021znw`, `Ji:2023pba`, `LatticeParton:2020uhz`, `LatticePartonLPC:2023pdv`, `Li:2020xml`, `Liu:2022nnk`, `Liu:2023onm`, `Vladimirov:2020ofp`

**YZLIU §3.C Threshold limits and power corrections in LaMET** (11 keys)

`Beneke1999`, `Braun:2018brg`, `Chen:2020ody`, `Jain:2008gb`, `JiEtAl2021`, `Ji:2022ezo`, `Ji:2023pba`, `Ji:2024hit`, `Li:2020xml`, `Liu:2023onm`, `Su:2026eta`

**YZLIU §3.D Exactly solvable laboratories for the twist expansion and the OPE** (8 keys)

`Ji:2018waw`, `Ji:2020bby`, `Kock:2020frx`, `Liu:2021evw`, `Liu:2024omb`, `Liu:2025bqq`, `Liu:2025edu`, `Liu:2026npv`

**YZLIU §3.E Euclidean correlators: renormalization and long-distance asymptotics** (14 keys) — E1–E2 (exponential decay, renormalization) are owned by Ch22

`Dorn:1986dt`, `Dutrieux:2025jed`, `Fredenhagen:1984bz`, `Green:2017xeu`, `Ishikawa:2017faj`, `IzubuchiEtAl2018`, `Ji:2017oey`, `Ji:2020brr`, `JiEtAl2021`, `Ji:2022ezo`, `Ji:2026vir`, `LatticePartonLPC:2021gpi`, `Ma:2014jla`, `MaQiu2018`

**LAMET §10. Transverse-momentum-dependent distributions from LaMET** (43 keys)

`Alexandrou:2023ucc`, `Avkhadiev:2023poz`, `Avkhadiev:2024mgd`, `Bollweg:2024zet`, `BoussarieEtAl2023`, `Constantinou:2019vyb`, `Deng:2022gzi`, `EbertStewartZhao2019`, `Ebert:2019okf`, `Ebert:2019tvc`, `Ebert:2020gxr`, `Ebert:2022fmh`, `Green:2020xco`, `Hagler:2009mb`, `Ji:2014hxa`, `Ji:2018hvs`, `Ji:2019ewn`, `Ji:2019sxk`, `JiEtAl2021`, `Ji:2020jeb`, `Ji:2023pba`, `KorchemskyRadyushkin1987`, `LatticeParton:2020uhz`, `LatticePartonCollaborationLPC:2022myp`, `LatticePartonLPC:2022eev`, `LatticePartonLPC:2023pdv`, `Li:2016axz`, `Liu:2023onm`, `Musch:2010ka`, `Musch:2011er`, `Rodini:2022wic`, `Schlemmer:2021aij`, `Shanahan:2020zxr`, `Shanahan:2021tst`, `Spanoudes:2024kpb`, `Tan:2025ofx`, `Vladimirov:2020ofp`, `Vladimirov:2020umg`, `Yoon:2017qzo`, `Zhang:2022xuw`, `Zhao:2023ptv`, `Zhao:2025oto`, `Zhu:2022bja`

**LAMET §11. Yizhuang Liu's programme: rigorous results, exactly solvable models, and analytic structure** (21 keys)

`Ji:2018waw`, `Ji:2019ewn`, `Ji:2019sxk`, `Ji:2020bby`, `Ji:2020brr`, `JiEtAl2021`, `Ji:2020jeb`, `Ji:2021znw`, `Ji:2023pba`, `Ji:2024hit`, `Ji:2026vir`, `Jia:2018qee`, `Jia:2024atq`, `LatticePartonLPC:2021gpi`, `Liu:2021evw`, `Liu:2023onm`, `Liu:2023pjb`, `Liu:2024omb`, `Liu:2025bqq`, `Liu:2025edu`, `Su:2026eta`

**YZLIU §3.F Exclusive processes (owner Ch19 `excl`)** (34 keys)

`CollinsSoperSterman1985a`, `CollinsSoperSterman1988`, `Collins:2011ca`, `Collins2011`, `Collins:2012uy`, `Collins:2017oxh`, `Collins:2023cuo`, `Ebert:2022fmh`, `Guo:2021ibg`, `Guo:2023pqw`, `Ivanov:2004vd`, `JiMaYuan2005`, `Ji:2019ewn`, `JiEtAl2021`, `Ji:2021znw`, `Ji:2022ezo`, `Ji:2023pba`, `Ji:2026vir`, `KugoOjima1979`, `LatticeParton:2020uhz`, `LatticePartonCollaborationLPC:2022myp`, `LatticePartonLPC:2023pdv`, `Liu:2021evw`, `Liu:2022nnk`, `Liu:2023eve`, `Liu:2023onm`, `Liu:2023pjb`, `Liu:2023tft`, `Liu:2026npv`, `Liu:2026rew`, `Scimemi:2019cmh`, `Streater:1989vi`, `Su:2026eta`, `Vladimirov:2020ofp`


### 3.4 Ch24 `front` (OTHERS.md Appendix A sections; in brackets the v2 units that use the same keys)

**OTHERS §0–1 Landau, IR structure [Ch4, App D]** (30 keys)

`Gordan1873`, `Collins2011`, `Collins:2020euz`, `ColemanNorton1965`, `LibbySterman1978b`, `EdenEtAl1966`, `Ma2020`, `FeigeSchwartz2014`, `Erdogan:2013bga`, `Erdogan:2014gha`, `Erdogan:2017gyf`, `Sterman:2025qsq`, `Anastasiou:2018rib`, `Anastasiou:2020sdt`, `Anastasiou:2022eym`, `Anastasiou:2024xvk`, `Anastasiou:2025cvy`, `Anastasiou:2026kpm`, `Anastasiou:2026jta`, `Mizera:2021icv`, `Fevola:2023kaw`, `Fevola:2023fzn`, `Berghoff:2022mqu`, `Helmer:2024wax`, `Hannesdottir:2022bmo`, `Gong:2008ww`, `Becker:2012nk`, `Becher:2009cu`, `Gardi:2009qi`, `Almelid:2015jia`

**OTHERS §2 OPE [App M, Ch21]** (18 keys)

`Zimmermann1973`, `Collins1984`, `Hollands:2006ag`, `Hollands:2007zg`, `Hollands:2011gf`, `Holland:2014pna`, `Holland:2015tia`, `Holland:2014ifa`, `Frob:2016mzv`, `Frob:2015uqy`, `Efremov:2017sqi`, `Kopper:2009zw`, `Kopper:1999qx`, `Keller:1991cj`, `Keller:1995qn`, `Keller:1990ej`, `Guida:2011np`, `Piguet:1995er`

**OTHERS §3 method of regions [Ch4, Ch15]** (11 keys)

`BenekeSmirnov1998`, `Smirnov:1990rz`, `Smirnov2002`, `Pak:2010pt`, `Jantzen2011`, `Semenova:2018cwy`, `Gardi:2022khw`, `Ma:2023hrt`, `Gardi:2024axt`, `Ananthanarayan:2018tog`, `Heinrich:2021dbf`

**OTHERS §4 Glauber, factorization violation, SLLs [Ch12, Ch16, Ch18]** (32 keys)

`Bodwin1985`, `CollinsSoperSterman1985b`, `CollinsSoperSterman1988`, `Bauer:2010cc`, `RothsteinStewart2016`, `Gaunt2014`, `Zeng:2015iba`, `Schwartz:2018obd`, `Schwartz:2017nmr`, `Mitov:2012gt`, `Catani:2014qha`, `CataniDeFlorianRodrigo2012`, `ForshawSeymourSiodmok2012`, `Dixon:2019lnw`, `Guan:2024hlf`, `ForshawKyrieleisSeymour2006`, `Forshaw:2008cq`, `Angeles-Martinez:2015rna`, `Forshaw:2021fxs`, `Becher:2021zkk`, `Becher:2023mtx`, `Boer:2023jsy`, `Boer:2023ljq`, `Boer:2024hzh`, `Boer:2024xzy`, `Becher:2024nqc`, `Banerjee:2025kkq`, `Becher:2024kmk`, `Becher:2025igg`, `Banfi:2025mra`, `Alioli:2023rxx`, `Stewart:2010tn`

**OTHERS §5 NLP / endpoint factorization [Ch21, Ch20]** (25 keys)

`Liu:2019oav`, `Liu:2020wbn`, `Liu:2022ajh`, `Liu:2017vkm`, `Liu:2018czl`, `Kotsky:1997rq`, `Akhoury:2001mz`, `Penin:2014msa`, `Bodwin:2021cpx`, `Bodwin:2021epw`, `Bodwin:2023asf`, `Bodwin:2025zzi`, `Beneke:2024cpq`, `Beneke:2019oqx`, `Beneke:2018gvs`, `Beneke:2019mua`, `Beneke:2020ibj`, `Beneke:2022obx`, `Beneke:2025ufd`, `Beneke:2026miy`, `Bonocore:2015esa`, `Bonocore:2016awd`, `Bahjat-Abbas:2018hpv`, `Moult:2018jjd`, `Moult:2019mog`

**OTHERS §6 TMD beyond LP [Ch14]** (13 keys)

`Vladimirov:2021hdn`, `Rodini:2022wki`, `Rodini:2023plb`, `Vladimirov:2023aot`, `Piloneta:2025jjb`, `BrisCuerpo:2026pma`, `Ebert:2021jhy`, `Gamberg:2022lju`, `Inglis-Whalen:2021bea`, `Ebert:2018gsn`, `Balitsky:2017flc`, `Balitsky:2017gis`, `Balitsky:2024ozy`

**OTHERS §7 positivity [Ch8]** (3 keys)

`CandidoForteHekhorn2020`, `CollinsRogersSato2022`, `Candido:2023ujx`

**OTHERS §8 BRST [Ch2, Ch8, App J]** (16 keys)

`Joglekar:1975nu`, `Kluberg-Stern:1974iel`, `Kluberg-Stern:1974nmx`, `Kluberg-Stern:1975ebk`, `DixonTaylor1974`, `Henneaux:1993jn`, `Barnich:2000zw`, `Falcioni:2022fdm`, `Gehrmann:2023ksf`, `Hamberg:1991qt`, `Collins:1994ee`, `Collins:2008sg`, `Labastida:1984gy`, `Ji:2017oey`, `Ishikawa:2017faj`, `Green:2017xeu`

**OTHERS §9 small x [Ch17]** (31 keys)

`Balitsky:2007feb`, `Balitsky:2006wa`, `Kovchegov:2006vj`, `Balitsky:2013fea`, `Kovner:2013ona`, `Kovner:2014xia`, `Kovner:2014lca`, `Caron-Huot:2016tzz`, `Lappi:2015fma`, `Beuf:2014uia`, `Iancu:2015vea`, `Caron-Huot:2013fea`, `DelDuca:2013ara`, `DelDuca:2014cya`, `Caron-Huot:2017zfo`, `Dominguez:2011wm`, `Mueller:2012uf`, `Balitsky:2015qba`, `Balitsky:2020jzt`, `Balitsky:2021fer`, `Balitsky:2023hmh`, `Balitsky:2026lop`, `Kovchegov:2015pbl`, `Kovchegov:2016weo`, `Cougoulic:2022gbk`, `Borden:2023ugd`, `Adamiak:2023okq`, `Borden:2024bxa`, `Borden:2025ehe`, `Hatta:2016aoc`, `Hatta:2022bxn`

**small-$x$ helicity, the other side of the disagreement (spec v2.1)** (3 keys): `Bartels:1995iu`, `Bartels:1996wc` (Bartels–Ermolaev–Ryskin, non-singlet and singlet $g_1$ at small $x$; the singlet paper carries the intercept $3.66394\sqrt{\alpha_sN_c/2\pi}$ quoted in OTHERS §9.5), `Blumlein:1996hb` (Blümlein–Vogt, singlet $g_1$ at small $x$). Identity fixed from the reference list of `Borden:2025ehe`; bibliographic level only — the disagreement is reported as Borden–Kovchegov state it (CLAIMS E34(iv); no verdict).

**OTHERS §10 double parton scattering [Ch18]** (13 keys)

`DiehlOstermeierSchafer2012`, `Manohar:2012jr`, `Manohar:2012pe`, `Diehl:2015bca`, `Diehl:2018wfy`, `Vladimirov:2017ksc`, `Diehl:2017kgu`, `Buffing:2017mqm`, `Diehl:2022rxb`, `Diehl:2019rdh`, `Diehl:2022dia`, `Diehl:2020xyg`, `Diehl:2017wew`

**OTHERS §11 jets, NGLs [Ch16]** (16 keys)

`Becher:2015hka`, `Becher:2016mmh`, `Becher:2016omr`, `Caron-Huot:2015bja`, `Banfi:2021owj`, `Banfi:2021xzn`, `Becher:2021urs`, `Becher:2023vrh`, `Becher:2026zon`, `Becher:2026iim`, `Larkoski:2015zka`, `Frye:2016aiz`, `Hoang:2019ceu`, `Kang:2016mcy`, `Dixon:2019uzg`, `Kologlu:2019mfz`

**OTHERS §12 quarkonium [Ch20]** (16 keys)

`BodwinBraatenLepage1995`, `NayakQiuSterman2005a`, `NayakQiuSterman2005b`, `NayakQiuSterman2006`, `Bodwin:2019bpf`, `Kang:2011mg`, `Kang:2014tta`, `Kang:2014pya`, `Fleming:2012wy`, `Ma:2013yla`, `Ma:2014eja`, `Bodwin:2014gia`, `Butenschoen:2014dra`, `Han:2014jya`, `Zhang:2014ybe`, `Ma:2017xno`

**OTHERS §13 QED/EW [Ch11]** (13 keys)

`Manohar:2016nzj`, `Manohar:2017eqh`, `Frixione:2019lga`, `Buonocore:2020nai`, `Bertone:2019hks`, `deFlorian:2015ujt`, `deFlorian:2016gvk`, `Ciafaloni:2000df`, `Bauer:2017isx`, `Bauer:2018arx`, `Fornal:2018znf`, `Manohar:2018kfx`, `Baumgart:2018ntv`


### 3.5 App M, App N, App O (refdoc S46–S48, S60)

**App M (OPE)** (31 keys)

`Zimmermann1969`, `Zimmermann1970`, `Zimmermann1973`, `LowensteinZimmermann1975`, `Lowenstein:1974qt`, `Wilson:1972ee`, `Wilson1969`, `Anikin:1978tj`, `Zavyalov:1990kv`, `Smirnov:1990rz`, `Smirnov2002`, `Chetyrkin:1982zq`, `Joglekar:1975nu`, `Joglekar:1976eb`, `Joglekar:1976pe`, `Hollands:2007zg`, `Hollands:2011gf`, `Frob:2016mzv`, `Collins:1994ee`, `Hamberg:1991qt`, `Falcioni:2022fdm`, `Gehrmann:2023ksf`, `Breitenlohner:1975hg`, `Breitenlohner:1976te`, `Bostelmann:2005rr`, `Streater:1989vi`, `Jost:1965yxu`, `Haag:1958vt`, `Epstein1960`, `Markoff1916`, `Fredenhagen:1984bz`

**App N (subtraction)** (8 keys)

`Collins2011`, `CollinsSoperSterman1989`, `UsyukinaDavydychev1993a`, `Ma2020`, `Jantzen2011`, `Gardi:2024axt`, `Zimmermann1969`, `Breitenlohner:1975hg`

**App O (LCOPT, Glauber)** (21 keys)

`AybatSterman2009`, `Diehl:2015bca`, `RothsteinStewart2016`, `Bodwin1985`, `CollinsSoperSterman1985a`, `Kogut:1969xa`, `Chang:1973qi`, `Ligterink:1994tm`, `Brodsky:1997de`, `Collins:2018aqt`, `Cheng:1969eh`, `Korchemskaya:1994qp`, `Korchemsky:1993hr`, `Caron-Huot:2013fea`, `DoriaFrenkelTaylor1980`, `Andrasi:1980qw`, `DiLietoEtAl1981`, `Basu:1984ba`, `Schwartz:2018obd`, `Gaunt2014`, `Zeng:2015iba`

**App M — keys added by the verify patch v2.3** (14 keys): `Bergere:1977wz`, `Balaban:1985yy`, `Balaban:1989ay`, `Magnen:1992wv`, `Borinsky:2020rqs`, `Schultka:2018nrs`, `Larin:1996wd`, `Arkani-Hamed:2022cqe`, `Henneaux:1995ex`, `Barnich:1999cy`, `Herrlich:1994kh`, `Hormander2003`, `Vladimirov2002`, `NilssonPassare2013`

**App N — keys added by the verify patch v2.3** (6 keys): `Bergere:1977wz`, `Belitsky:2025bez`, `Belitsky:2024yag`, `Jackiw:1980kv`, `Borinsky:2020rqs`, `Arkani-Hamed:2022cqe`

**App O — keys added by the verify patch v2.3** (10 keys): `Meggiolaro:1996hf`, `Giordano:2006vv`, `Lindsay:1983ny`, `Barcaro:2026dsd`, `Zhou:2017his`, `Liu:2008cc`, `Chang:2013pba`, `Li:2022fvk`, `Boer:2017hqr`, `Lindsay:1983dt`

**App Q (errata candidates; sources only) — spec v2.1: keyed to `verify/CLAIMS.md` E01–E36.** Classes (WRITER_SPEC_v2 §6.13): **Q1** = App Q candidate (printed only after two independent confirmations in `verify/`); **Q2** = corrected by the authors or superseded by the same group (cite the corrected version where used; listed in App Q only if the verify patch decides to document author-corrected items); **Q3** = not an App Q item (proof gaps, disputes between groups, convention hazards, errors reported by others: status paragraphs and remarks, with attribution); E19 is withdrawn (never printed); E33 is a rule (always use the corrected versions of papers with published errata).

| claim | class | source as printed (merged key) | correct form / later literature | VF | where in the book | outcome (verify patch v2.3) |
|---|---|---|---|---|---|---|
| E01 | Q1 | `Ji:2020brr`, `JiEtAl2021` (eq. hybridm2) | `Su:2022fiu` | VF-LAM-10 | Ch22 schemes | Q1 confirmed: App Q row Q.8 (first corrected by `Chou:2022drv`) |
| E02 | Q1 | `Ji:2019ewn` (22), `Liu:2022nnk` (53),(75), `JiEtAl2021` (209)–(210), `Ji:2021znw` (49),(51),(73) | `EbertStewartZhao2019`, `Ebert:2022fmh` | VF-LAM-15, VF-YZL-5 | Ch23 | Q1 confirmed: row Q.11 (noted by the authors, PRD 105 fn. 1) |
| E03 | Q1 | `Braun:2018brg` (cR) | their (t4-Qparallel), (t4-Qperp) | VF-LAM-13 | Ch22 power corrections | Q1 confirmed: row Q.9 |
| E04 | Q1 (minor: internal convention inconsistency, no effect at the computed order) | `IzubuchiEtAl2018` | — | VF-LAM-0 | Ch22 (conventions) | Q1 confirmed: row Q.10 |
| E05 | Q3 (incomplete statement: print the proviso) | `Ji:2017oey` | `Constantinou:2017sej`, `Green:2017xeu` | VF-LAM-2 | Ch22 renormalization | Q3 confirmed (status sentence, Ch22) |
| E06 | Q2 (superseded by the same group) | `Ji2013` | `IzubuchiEtAl2018` | VF-LAM-6 | Ch22 (history) | Q2 confirmed: `tab:appQ-errata-b` row Q.17 |
| E07 | Q3 (errors reported by others) | `Alexandrou:2015rja`; `Ji:2014hxa`, `Ebert:2019okf`; `XiongEtAl2014` | `Chen:2016utp`; `Ji:2019sxk`; `Jia:2024atq` | VF-LAM-11 | Ch22, Ch23 | Q3 confirmed (attributed) |
| E08 | Q1 | `Liu:2022nnk` (81), `Ji:2021znw` (72) | `JiEtAl2021`, `Ji:2023pba` (A.6) | VF-YZL-3 | Ch23 | Q1 confirmed: row Q.12 |
| E09 | Q1 | `JiEtAl2021` (205)–(206) | — | VF-YZL-3 | Ch23 | Q1 confirmed: row Q.13 |
| E10 | Q2 (corrected by the authors) | `Ji:2019ewn` (26) | `Ji:2023pba` (A.13) | VF-YZL-7 | Ch23 | Q1 confirmed: row Q.14 (the correct value in `Ji:2023pba` does not note the discrepancy) |
| E11 | Q1 | `Liu:2022nnk` (81), `JiEtAl2021` (208) | — | VF-YZL-3 | Ch23 | Q1 confirmed: row Q.15 |
| E12 | Q2 (corrected by the authors) | `Guo:2021ibg` | `Guo:2023pqw` | VF-YZL-15 | Ch19 | Q2 confirmed: row Q.18 |
| E13 | Q1 (terminology) | `Liu:2022nnk` App. F | `Streater:1989vi`; `Liu:2023pjb` | VF-YZL-12 | Ch23 | Q1 confirmed: row Q.16 |
| E14 | Q3 (proof gap identified by Collins, preprint) | `ColemanNorton1965` | `Collins:2020euz` | VF-FRO-3 | Ch4, App D, Ch24 | Q3 confirmed |
| E15 | Q3 (heuristic textbook derivation) | `EdenEtAl1966` §2.1 | `Collins:2020euz`; `Collins2011` §5.4.3 | VF-FRO-2 | App D, Ch24 | Q3 confirmed |
| E16 | Q3 (single-group result against another group's claim) | `Alioli:2023rxx` | `Banfi:2025mra` | VF-FRO-8 | Ch16, Ch24 | Q3 confirmed, now by two groups (`Becher:2026kbr`) |
| E17 | Q1 | `AybatRogers2011` (3) | their (A10),(A11),(B1) | VF-TMD-9 | Ch14 | Q1 confirmed: row Q.2 (implicitly corrected in `Aybat:2011ge`) |
| E18 | Q1 (unpublished preprint) | `Collins2007` (10) | its (11) | VF-GLA-8 | Ch18 | Q1 confirmed: row Q.4 |
| E19 | withdrawn — never print | — | — | — | — | withdrawn — never printed |
| E20 | Q1 (arXiv v1; check the PRL) | `Ji1997a` (15) | `Vanderhaeghen:1999xj` (38) | VF-EXC-8 | Ch19 | Q1 confirmed: row Q.5 |
| E21 | Q1 (minor internal inconsistency) | `Mankiewicz:1999tt` | their eq. (10) | VF-REF-15 | Ch19 | Q1 confirmed: row Q.6 |
| E22 | Q3 (erratum reported by others) | (the NLO paper criticized in `CollinsDiehl2000`) | `CollinsDiehl2000` | — | Ch19 | refuted: nothing printed |
| E23 | Q1 (arXiv App. A; check the journal version) | `BecherSchwartz2008` | `KorchemskyRadyushkin1987` | VF-CONV-23, VF-SCET-16 | Ch5, Ch15, App B | Q1 confirmed (journal version too): row Q.1 |
| E24 | Q3 (implicit normalization) | `BecherSchwartz2008` | — | VF-SCET-9 | Ch15 | Q3 confirmed |
| E25 | Q1 (minor: imprecise invariance statement) | `BauerPirjolStewart2002` (Lcg) | — | VF-SCET-6 | Ch15 | Q1 confirmed: row Q.3 |
| E26 | Q1 (minor typo) | `BenekeEtAl2001`, `BenekeNeubert2003` | — | VF-BQ-4 | Ch20 | Q1 confirmed: row Q.7 |
| E27 | Q2 (author's errata list) | `Collins2011` Fig. 7.10, eqs. (11.4)–(11.6) | the author's errata | VF-WL-10 | Ch9, App F | Q2 confirmed: row Q.19 |
| E28 | Q1 only if a printed source of the wrong form is identified; else a remark | (secondary literature) | `StermanWeinberg1977` | VF-EE-12 | Ch2, Ch16 | convention remark (Ch2, Ch16); no App Q row |
| E29 | Q2 (corrected by the authors) | GKL 1988 | `GorishniiKataevLarin1991`, `SurguladzeSamuel1991` | VF-EE-10 | Ch6 | Q2 confirmed: row Q.20 |
| E30 | Q2 (corrected by the author) | `Collins1993` | `Collins2002`, `BrodskyHwangSchmidt2002` | — | Ch14 | Q2 confirmed: row Q.21 |
| E31 | Q2 (corrected by the author) | `CollinsSoperSterman1988` | `Collins2011` §14.4 | — | Ch12 | quotation of Collins 2011 only (Ch12); no App Q row |
| E32 | Q3 unless a printed source is identified (then Q1) | (unidentified) | `BardeenEtAl1978` | VF-DIS-8, VF-DIS-14 | Ch7, App G | refuted: nothing printed |
| E33 | rule: use the corrected versions | (list in CLAIMS E33) | the errata | — | all units | rule confirmed (DHYZ erratum reverses its conclusion) |
| E34 | Q3 (disputes, no verdict) | `Liu:2020wbn`, `Rodini:2023plb`, `Balitsky:2007feb`, `Borden:2023ugd`, `Borden:2025ehe` | `Bartels:1996wc`, `Blumlein:1996hb` (other side) | VF-FRO-9, VF-FRO-12, VF-FRO-17 | Ch21, Ch24 | disagreements reported without verdict (item (iii) withdrawn by its authors, `Balitsky:2009xg`) |
| E35 | Q3 (dispute) | `CandidoForteHekhorn2020` | `CollinsRogersSato2022`; `Candido:2023ujx` | VF-FRO-10 | Ch8, Ch24 | Q3 confirmed |
| E36 | Q3 (dispute) | `Gaunt2014`, `RothsteinStewart2016` §11.1 | `Schwartz:2018obd`; `Zeng:2015iba` | — | Ch18, Ch24 | Q3 confirmed (wording: Gaunt shows / suggests; SYZ contradict only the pure-Glauber part) |


---------------------------------------------------------------------------------------------------

## 4. New entries: where they are cited and at which depth

Generated by `spec_v2/checks/refs_notes_tables.py` from the merge log and the frontier reports. Columns: key; authors; publication; title (shortened); the sections of the frontier report that cite the key; the reading depth recorded next to the citation ("read" = the agent located the cited statement in the full text — for YZLIU the depth of its publication map: full / main text / intro–conclusion / partial; "abstract" = INSPIRE abstract only; "—" = no marker found near the citation, treat as bibliographic level and check the report before attributing content); preprint = arXiv only. The depth is extracted heuristically: **always read the report passage** before writing what a paper shows (WRITER_SPEC_v2 §6.11 item 2).


### 4.1 New keys from frontier/yzliu/yzliu.bib (report YZLIU.md) — 57 entries

| key | authors | publication | title | cited in (report §) | depth | preprint |
|---|---|---|---|---|---|---|
| `Becher:2009kw` | Becher–Neubert | Phys. Rev. D 79 (2009) 125004 | Infrared singularities of QCD amplitudes with massive partons | A5 | — |  |
| `Bogner:2010kv` | Bogner–Weinzierl | Int. J. Mod. Phys. A 25 (2010) 2585 | Feynman graph polynomials | A6 | — |  |
| `Chen:2020ody` | Chen–Wang–Zhu | Phys. Rev. Lett. 126 (2021) 072002 | Next-to-Next-to-Leading Order Calculation of Quasiparton Distribution Functions | B2, C2 | read |  |
| `Collins:2008ht` | Collins | PoS LC2008 (2008) 028 | Rapidity divergences and valid definitions of parton densities | A2 | — |  |
| `Collins:2011ca` | Collins | Int. J. Mod. Phys. Conf. Ser. 4 (2011) 85 | New definition of TMD parton densities | 5, A1 | — |  |
| `Collins:2012uy` | Collins–Rogers | Phys. Rev. D 87 (2013) 034018 | Equality of Two Definitions for Transverse Momentum Dependent Parton Distribution Funct... | 5 | — |  |
| `Collins:2023cuo` | Collins–Rogers | Phys. Rev. D 109 (2024) 016006 | Definition of fragmentation functions and the violation of sum rules | 7 | — |  |
| `delRio:2023pse` | del Rio–Vladimirov | Phys. Rev. D 108 (2023) 114009 | Quasitransverse momentum dependent distributions at next-to-next-to-leading order | 5, B1, B2, 4.1 | read |  |
| `Dorn:1986dt` | Dorn | Fortsch. Phys. 34 (1986) 11 | Renormalization of Path Ordered Phase Factors and Related Hadron Operators in Gauge Fie... | E2 | — |  |
| `Dutrieux:2025jed` | Dutrieux et al. | Phys. Rev. D 113 (2026) 074524 | Inverse problem in the large momentum effective theory framework | E1 | — |  |
| `Ebert:2019okf` | Ebert–Stewart–Zhao | JHEP 09 (2019) 037 | Towards Quasi-Transverse Momentum Dependent PDFs Computable on the Lattice | A1, B1 | read |  |
| `Echevarria:2015byo` | Echevarria–Scimemi–Vladimirov | Phys. Rev. D 93 (2016) 054004 | Universal transverse momentum dependent soft function at NNLO | A6 | — |  |
| `Fredenhagen:1984bz` | Fredenhagen | Commun. Math. Phys. 97 (1985) 461 | A Remark on the Cluster Theorem | E1 | — |  |
| `Grozin:2015kna` | Grozin et al. | JHEP 01 (2016) 140 | The three-loop cusp anomalous dimension in QCD and its supersymmetric extensions | A5 | — |  |
| `Guo:2021ibg` | Guo–Ji–Liu | Phys. Rev. D 103 (2021) 096010 | QCD Analysis of Near-Threshold Photon-Proton Production of Heavy Quarkonium | F1, 0.1, 1.3, 4.1 | read (main text) |  |
| `Guo:2023pqw` | Guo et al. | Phys. Rev. D 108 (2023) 034003 | Updated analysis of near-threshold heavy quarkonium production for probe of proton\text... | F1, 0.1, 1.3, 4.1 | read (main text) |  |
| `Ivanov:2004vd` | Ivanov et al. | Eur. Phys. J. C 34 (2004) 297 | Exclusive photoproduction of a heavy vector meson in QCD | F1 | — |  |
| `Jain:2008gb` | Jain–Scimemi–Stewart | Phys. Rev. D 77 (2008) 094008 | Two-loop Jet-Function and Jet-Mass for Top Quarks | C1 | — |  |
| `Ji:2014hxa` | Ji et al. | Phys. Rev. D 91 (2015) 074009 | Soft factor subtraction and transverse momentum dependent parton distributions on the l... | A1, B1 | — |  |
| `Ji:2018hvs` | Ji et al. | Phys. Rev. D 99 (2019) 114006 | Transverse momentum dependent parton quasidistributions | A2, B1 | read |  |
| `Ji:2018waw` | Ji–Liu–Zahed | Phys. Rev. D 99 (2019) 054008 | Quasiparton distribution functions: Two-dimensional scalar and spinor QCD | D4, 0.1, 1.3 | read (main text) |  |
| `Ji:2019ewn` | Ji–Liu–Liu | Phys. Lett. B 811 (2020) 135946 | Transverse-momentum-dependent parton distribution functions from large-momentum effecti... | A1, A5, B1, B2, B5, 0.1 | read (full) |  |
| `Ji:2019sxk` | Ji–Liu–Liu | Nucl. Phys. B 955 (2020) 115054 | TMD soft function from large-momentum effective theory | A1, A4, A5, B4, B5, 0.1 | read (full) |  |
| `Ji:2020bby` | Ji–Liu–Zahed | Phys. Rev. D 103 (2021) 074002 | Mass structure of hadrons and light-front sum rules in the $'t$ Hooft model | D5, 0.1, 1.3 | abstract |  |
| `Ji:2020brr` | Ji et al. | Nucl. Phys. B 964 (2021) 115311 | A Hybrid Renormalization Scheme for Quasi Light-Front Correlations in Large-Momentum Ef... | E2, 0.1, 1.2, 1.3 | read (partial) |  |
| `Ji:2020jeb` | Ji et al. | Phys. Rev. D 103 (2021) 074005 | Single Transverse-Spin Asymmetry and Sivers Function in Large Momentum Effective Theory | B6, 0.1, 1.3 | read (main text) |  |
| `Ji:2021znw` | Ji–Liu | Phys. Rev. D 105 (2022) 076014 | Computing light-front wave functions without light-front quantization: A large-momentum... | A5, B3, 0.1, 1.2, 1.3, 4.1 | read (main text) |  |
| `Ji:2022ezo` | Ji | Research 8 (2025) 0695 | Ab Initio Lattice Quantum Chromodynamics Calculations of Parton Physics in the Proton: ... | 8, C5, E1 | read |  |
| `Ji:2023pba` | Ji–Liu–Su | JHEP 08 (2023) 037 | Threshold resummation for computing large-x parton distribution through large-momentum ... | A5, B1, B2, C1, C2, C3 | read (full) |  |
| `Ji:2024hit` | Ji et al. | JHEP 03 (2025) 045 | Effects of threshold resummation for large-x PDF in large momentum effective theory | C5, 0.1, 1.3 | read (intro/concl.) |  |
| `Ji:2026vir` | Ji–Liu–Su | preprint arXiv:2601.12189 [hep-lat] (2026) | Asymptotic Long-Distance Expansion of Euclidean Correlators in Lattice Parton Applications | 8, E1, 0.1, 1.2, 1.3, 4.1 | read (main text) | yes |
| `Kock:2020frx` | Kock–Liu–Zahed | Phys. Rev. D 102 (2020) 014039 | Pion and kaon parton distributions in the QCD instanton vacuum | D5, 0.1, 1.3 | abstract |  |
| `LatticeParton:2020uhz` | Zhang et al. | Phys. Rev. Lett. 125 (2020) 192001 | Lattice QCD Calculations of Transverse-Momentum-Dependent Soft Function through Large-M... | 5, 8, B4, 0.1, 1.2, 1.3 | read (intro/concl.) |  |
| `LatticePartonCollaborationLPC:2022myp` | He et al. | Phys. Rev. D 109 (2024) 114513 | Unpolarized transverse momentum dependent parton distributions of the nucleon from latt... | 5 | — |  |
| `LatticePartonLPC:2021gpi` | Huo et al. | Nucl. Phys. B 969 (2021) 115443 | Self-renormalization of quasi-light-front correlators on the lattice | E2, 0.1, 1.3 | read |  |
| `LatticePartonLPC:2023pdv` | Chu et al. | JHEP 08 (2023) 172 | Lattice calculation of the intrinsic soft function and the Collins-Soper kernel | 5, B4 | read |  |
| `Li:2016axz` | Li–Neill–Zhu | Nucl. Phys. B 960 (2020) 115193 | An exponential regulator for rapidity divergences | A4, A6 | — |  |
| `Li:2020xml` | Li–Ma–Qiu | Phys. Rev. Lett. 126 (2021) 072001 | Extraction of Next-to-Next-to-Leading-Order Parton Distribution Functions from Lattice ... | B2, C2 | read |  |
| `Liu:2021evw` | Liu–Zahed | preprint arXiv:2102.07248 [hep-ph] (2021) | Small size instanton contributions to the quark quasi-PDF and matching kernel | 8, D5, 0.1, 1.3 | read (intro/concl.) | yes |
| `Liu:2022bru` | Liu–Nowak–Zahed | Phys. Rev. D 108 (2023) 034017 | Mueller\textquoterights dipole wave function in QCD: Emergent Koba-Nielsen-Olesen scali... | 1.3 | — |  |
| `Liu:2022nnk` | Liu | Acta Phys. Polon. B 53 (2022) 4 | Lecture Notes on Transverse-momentum-dependent Parton Distribution Function and Soft Fu... | 7, A1, A2, A3, A4, A5 | read (full) |  |
| `Liu:2023eve` | Liu–Nowak–Zahed | preprint arXiv:2302.01380 [hep-ph] (2023) | Universality of Koba-Nielsen-Olesen scaling in QCD at high energy and entanglement | 8, 1.3 | — | yes |
| `Liu:2023onm` | Liu–Su | JHEP 02 (2024) 204 | Renormalon cancellation and linear power correction to threshold-like asymptotics of sp... | 7, 8, B2, C4, 0.1, 1.3 | read (main text) |  |
| `Liu:2023pjb` | Liu | JHEP 09 (2024) 030 | Revisiting the time-ordering issue of TMD soft factors: causality, coordinate space ana... | 7, 8, A6, 0.1, 1.3, 4.1 | read (full) |  |
| `Liu:2023tft` | Liu | preprint arXiv:2310.15134 [hep-th] (2023) | Analytic asymptotics of the integrable XXX critical spin chains in the small external-f... | 8, 1.3 | — | yes |
| `Liu:2024omb` | Liu | JHEP 09 (2024) 093 | Bjorken and threshold asymptotics of a space-like structure function in the 2D U(N) Gro... | D1, 0.1, 1.3 | read (main text) |  |
| `Liu:2025bqq` | Liu–Mari~no | SciPost Phys. 20 (2026) 156 | Trans-series from condensates in the non-linear sigma model | D3, 0.1, 1.3 | read (intro/concl.) |  |
| `Liu:2025edu` | Liu | JHEP 08 (2025) 014 | Renormalon-like factorial enhancements to power expansion/OPE in a super-renormalizable... | D2, 0.1, 1.3 | read (intro/concl.) |  |
| `Liu:2025qsv` | Liu | JHEP 01 (2026) 064 | Asymptotics of spin-spin correlators weighted by fermion number measurements with low r... | 0.1, 1.3 | read |  |
| `Liu:2026npv` | Liu | preprint arXiv:2606.06277 [hep-th] (2026) | A note on the 2D NLSM free energy | 8, D3, 0.1, 1.3 | abstract | yes |
| `Liu:2026rew` | Liu | preprint arXiv:2604.06011 [math-ph] (2026) | Analyticity, asymptotics and natural boundary for a one-point function of the finite-vo... | 8, 1.3 | — | yes |
| `Moult:2018jzp` | Moult–Zhu | JHEP 08 (2018) 160 | Simplicity from Recoil: The Three-Loop Soft Function and Factorization for the Energy-E... | A6 | read |  |
| `Scimemi:2019cmh` | Scimemi–Vladimirov | JHEP 06 (2020) 137 | Non-perturbative structure of semi-inclusive deep-inelastic and Drell-Yan scattering at... | 5 | — |  |
| `Streater:1989vi` | Streater–Wightman | book Princeton University Press (2000) | PCT, Spin and Statistics, and All That | 8, A3, A6, 4.1 | — |  |
| `Su:2026eta` | Su et al. | preprint arXiv:2609.20545 [hep-lat] (2026) | Computability of GPDs near $x=\pm\xi$ in Lattice QCD | 8, C6, 0.1, 1.3 | read (full) | yes |
| `Vladimirov:2016dll` | Vladimirov | Phys. Rev. Lett. 118 (2017) 062001 | Correspondence between Soft and Rapidity Anomalous Dimensions | A6 | — |  |
| `Vladimirov:2020ofp` | Vladimirov–Schafer | Phys. Rev. D 101 (2020) 074517 | Transverse momentum dependent factorization for lattice observables | 5, B1 | — |  |

### 4.2 New keys from frontier/lamet/lamet.bib (report LAMET.md) — 109 entries

| key | authors | publication | title | cited in (report §) | depth | preprint |
|---|---|---|---|---|---|---|
| `Alexandrou:2015rja` | Alexandrou et al. | Phys. Rev. D 92 (2015) 014502 | Lattice calculation of parton distributions | 5.1 | — |  |
| `Alexandrou:2017huk` | Alexandrou et al. | Nucl. Phys. B 923 (2017) 394 | A complete non-perturbative renormalization prescription for quasi-PDFs | 3.7 | — |  |
| `Alexandrou:2019lfo` | Alexandrou et al. | Phys. Rev. D 99 (2019) 114504 | Systematic uncertainties in parton distribution functions from lattice QCD simulations ... | 4.6 | — |  |
| `Alexandrou:2023ucc` | Alexandrou et al. | Phys. Rev. D 108 (2023) 114503 | Nonperturbative renormalization of asymmetric staple-shaped operators in twisted mass l... | 10.2 | — |  |
| `Avkhadiev:2023poz` | Avkhadiev et al. | Phys. Rev. D 108 (2023) 114505 | Collins-Soper kernel from lattice QCD at the physical pion mass | 10.3 | abstract |  |
| `Avkhadiev:2024mgd` | Avkhadiev et al. | Phys. Rev. Lett. 132 (2024) 231901 | Determination of the Collins-Soper Kernel from Lattice QCD | 10.3 | abstract |  |
| `Bagan:1993zv` | Bagan–Gosdzinsky | Phys. Lett. B 320 (1994) 123 | Renormalizability of the heavy quark effective theory | 3.2 | — |  |
| `Balitsky:2019krf` | Balitsky–Morris–Radyushkin | Phys. Lett. B 808 (2020) 135621 | Gluon Pseudo-Distributions at Short Distances: Forward Case | 4.10 | abstract |  |
| `Beneke:2023nmj` | Beneke et al. | JHEP 09 (2023) 066 | QCD light-cone distribution amplitudes of heavy mesons from boosted HQET | 9.4 | abstract |  |
| `Bhattacharya:2020jfj` | Bhattacharya et al. | Phys. Rev. D 102 (2020) 114025 | The role of zero-mode contributions in the matching for the twist-3 PDFs $e(x)$ and $h_... | 4.9 | — |  |
| `Bhattacharya:2020xlt` | Bhattacharya et al. | Phys. Rev. D 102 (2020) 034005 | One-loop matching for the twist-3 parton distribution $g_T (x)$ | 4.9 | — |  |
| `Bhattacharya:2022aob` | Bhattacharya et al. | Phys. Rev. D 106 (2022) 114512 | Generalized parton distributions from lattice QCD with asymmetric momentum transfer: Un... | 9.1 | abstract |  |
| `Bollweg:2024zet` | Bollweg et al. | Phys. Lett. B 852 (2024) 138617 | Nonperturbative Collins-Soper kernel from chiral quarks with physical masses | 10.3 | abstract |  |
| `Braun:2007wv` | Braun–Muller | Eur. Phys. J. C 55 (2008) 349 | Exclusive processes in position space and the pion distribution amplitude | 8.3 | abstract |  |
| `Braun:2020ymy` | Braun–Chetyrkin–Kniehl | JHEP 07 (2020) 161 | Renormalization of parton quasi-distributions beyond the leading order: spacelike vs. t... | 3.2, 3.3, 3.6, 4.7 | read |  |
| `Braun:2021aon` | Braun–Ji–Vladimirov | JHEP 05 (2021) 086 | QCD factorization for twist-three axial-vector parton quasidistributions | 4.9 | abstract |  |
| `Braun:2021gvv` | Braun–Ji–Vladimirov | JHEP 10 (2021) 087 | QCD factorization for chiral-odd parton quasi- and pseudo-distributions | 4.9 | abstract |  |
| `Braun:2023alc` | Braun | JHEP 10 (2023) 134 | Kinematic twist-three contributions to pseudo- and quasi-GPDs and translation invariance | 13, 9.1 | abstract |  |
| `Braun:2024snf` | Braun–Koller–Schoenleber | Phys. Rev. D 109 (2024) 074510 | Renormalons and power corrections in pseudo- and quasi-GPDs | 13, 5.3, 9.1 | abstract |  |
| `Briceno:2017cpo` | Brice~no–Hansen–Monahan | Phys. Rev. D 96 (2017) 014502 | Role of the Euclidean signature in lattice calculations of quasidistributions and other... | 3.5, 8.4 | abstract |  |
| `Briceno:2018lfj` | Brice~no et al. | Phys. Rev. D 98 (2018) 014511 | Finite-volume effects due to spatially nonlocal operators | 3.5 | abstract |  |
| `Chen:2016fxx` | Chen–Ji–Zhang | Nucl. Phys. B 915 (2017) 1 | Improved quasi parton distribution through Wilson line renormalization | 3.7 | — |  |
| `Chen:2016utp` | Chen et al. | Nucl. Phys. B 911 (2016) 246 | Nucleon Helicity and Transversity Parton Distributions from Lattice QCD | 5.1 | — |  |
| `Chen:2017mie` | Chen et al. | Chin. Phys. C 43 (2019) 103101 | Symmetry properties of nonlocal quark bilinear operators on a Lattice | 3.5 | — |  |
| `Chen:2017mzz` | Chen et al. | Phys. Rev. D 97 (2018) 014505 | Parton distribution function with nonperturbative renormalization from lattice QCD | 3.7 | — |  |
| `Chen:2020arf` | Chen–Wang–Zhu | Phys. Rev. D 102 (2020) 011503 | Quasi parton distribution functions at NNLO: flavor non-diagonal quark contributions | 4.7 | abstract |  |
| `Chen:2020iqi` | Chen–Wang–Zhu | JHEP 10 (2020) 079 | Master integrals for two-loop QCD corrections to quark quasi PDFs | 4.7 | abstract |  |
| `Chen:2025cxr` | Chen et al. | Phys. Rev. D 113 (2026) 014509 | Large-momentum effective theory\textquoterights asymptotic extrapolation vs the inverse... | 7.3 | abstract |  |
| `Chetyrkin:2003vi` | Chetyrkin–Grozin | Nucl. Phys. B 666 (2003) 289 | Three loop anomalous dimension of the heavy light quark current in HQET | 3.2 | — |  |
| `Constantinou:2017sej` | Constantinou–Panagopoulos | Phys. Rev. D 96 (2017) 054506 | Perturbative renormalization of quasi-parton distribution functions | 0.3, 3.5, 3.7 | — |  |
| `Constantinou:2019vyb` | Constantinou–Panagopoulos–Spanoudes | Phys. Rev. D 99 (2019) 074508 | One-loop renormalization of staple-shaped operators in continuum and lattice regulariza... | 10.2 | — |  |
| `Craigie:1980qs` | Craigie–Dorn | Nucl. Phys. B 185 (1981) 204 | On the Renormalization and Short Distance Properties of Hadronic Operators in QCD | 3.1 | — |  |
| `Deng:2022gzi` | Deng–Wang–Zeng | JHEP 09 (2022) 046 | Transverse-momentum-dependent wave functions and soft functions at one-loop in large mo... | 10.4 | — |  |
| `Deng:2023csv` | Deng et al. | JHEP 07 (2023) 191 | Light-cone distribution amplitudes of a light baryon in large-momentum effective theory | 9.2 | abstract |  |
| `Dotsenko:1979wb` | Dotsenko–Vergeles | Nucl. Phys. B 169 (1980) 527 | Renormalizability of Phase Factors in the Nonabelian Gauge Theory | 3.1, 3.2 | — |  |
| `Ebert:2019tvc` | Ebert–Stewart–Zhao | JHEP 03 (2020) 099 | Renormalization and Matching for the Collins-Soper Kernel from Lattice QCD | 10.3 | abstract |  |
| `Ebert:2020gxr` | Ebert et al. | JHEP 09 (2020) 099 | One-loop Matching for Spin-Dependent Quasi-TMDs | 10.5 | abstract |  |
| `Gao:2021dbh` | Gao et al. | Phys. Rev. Lett. 128 (2022) 142003 | Lattice QCD Determination of the Bjorken-x Dependence of Parton Distribution Functions ... | 4.7, 7.3 | abstract |  |
| `Gao:2021hxl` | Gao et al. | Phys. Rev. D 103 (2021) 094504 | Origin and resummation of threshold logarithms in the lattice QCD calculations of PDFs | 6.2 | abstract |  |
| `Gao:2023lny` | Gao–Liu–Zhao | Phys. Rev. D 109 (2024) 094506 | Parton distributions from boosted fields in the Coulomb gauge | 3.7 | — |  |
| `Good:2025daz` | Good–Yao–Lin | Phys. Lett. B 872 (2026) 140067 | First nucleon gluon PDF from large momentum effective theory | 4.10 | — |  |
| `Green:2020xco` | Green–Jansen–Steffens | Phys. Rev. D 101 (2020) 074509 | Improvement, generalization, and scheme conversion of Wilson-line operators on the latt... | 3.5, 10.2 | — |  |
| `Hagler:2009mb` | Hagler et al. | EPL 88 (2009) 61001 | Intrinsic quark transverse momentum in the nucleon from lattice QCD | 10.3 | — |  |
| `Han:2024fkr` | Han et al. | Phys. Rev. D 111 (2025) L111503 | Realistic method to access heavy meson light-cone distribution amplitudes from first-pr... | 9.4 | abstract |  |
| `Hatta:2013gta` | Hatta–Ji–Zhao | Phys. Rev. D 89 (2014) 085030 | Gluon helicity $\Delta G$ from a universality class of operators on a lattice | 2.2, 9.5 | abstract |  |
| `Holligan:2023rex` | Holligan et al. | Nucl. Phys. B 993 (2023) 116282 | Precision control in lattice calculation of x-dependent pion distribution amplitude | 3.4, 9.2 | abstract |  |
| `Holligan:2025baj` | Holligan et al. | JHEP 207 (2025) 241 | Resummation for lattice QCD calculation of generalized parton distributions at nonzero ... | 6.4 | abstract |  |
| `Ishikawa:2016znu` | Ishikawa et al. | preprint arXiv:1609.02018 [hep-lat] (2016) | Practical quasi parton distribution functions | 3.7 | — | yes |
| `Jaarsma:2023woo` | Jaarsma–Rahn–Waalewijn | JHEP 12 (2023) 014 | Towards double parton distributions from first principles using Large Momentum Effectiv... | 9.6 | abstract |  |
| `Ji:2013fga` | Ji–Zhang–Zhao | Phys. Rev. Lett. 111 (2013) 112002 | Physics of the Gluon-Helicity Contribution to Proton Spin | 9.5 | abstract |  |
| `Ji:2015jwa` | Ji–Zhang | Phys. Rev. D 92 (2015) 034006 | Renormalization of quasiparton distribution | 3.2 | — |  |
| `Ji:2015qla` | Ji et al. | Phys. Rev. D 92 (2015) 014039 | One-Loop Matching for Generalized Parton Distributions | 9.1, 9.2 | abstract |  |
| `Ji:2017rah` | Ji–Zhang–Zhao | Nucl. Phys. B 924 (2017) 366 | More On Large-Momentum Effective Theory Approach to Parton Physics | 8.4 | abstract |  |
| `Ji:2020byp` | Ji | AAPPS Bull. 30 (2020) 58 | Why is LaMET an effective field theory for partonic structure? | 2.4 | — |  |
| `Ji:2024oka` | Ji | Nucl. Phys. B 1007 (2024) 116670 | Euclidean effective theory for partons in the spirit of Steven Weinberg | 13, 0.1, 2.4, 5.5, 7.2 | — |  |
| `Ji:2025mvk` | Ji–Yao–Zhang | preprint arXiv:2504.09367 [hep-ph] (2025) | Extracting Meson Distribution Amplitudes from Nonlocal Euclidean Correlations at Next-t... | 4.7, 9.1, 9.2 | abstract | yes |
| `Jia:2018qee` | Jia et al. | Phys. Rev. D 98 (2018) 054011 | Partonic quasidistributions in two-dimensional QCD | 11 | abstract |  |
| `Jia:2024atq` | Jia et al. | Phys. Rev. D 109 (2024) 014042 | Light-cone and quasigeneralized parton distributions in the \textquoterightt Hooft model | 11 | abstract |  |
| `Joo:2019jct` | Joo et al. | JHEP 12 (2019) 081 | Parton Distribution Functions from Ioffe time pseudo-distributions | 8.1 | — |  |
| `Joo:2020spy` | Joo et al. | Phys. Rev. Lett. 125 (2020) 232003 | Parton Distribution Functions from Ioffe Time Pseudodistributions from Lattice Calculat... | 8.1 | — |  |
| `Karpie:2018zaz` | Karpie–Orginos–Zafeiropoulos | JHEP 11 (2018) 178 | Moments of Ioffe time parton distribution functions from non-local matrix elements | 8.1, 8.4 | abstract |  |
| `Karpie:2019eiq` | Karpie et al. | JHEP 04 (2019) 057 | Reconstructing parton distribution functions from Ioffe time data: from Bayesian method... | 7.3 | abstract |  |
| `LatticeParton:2018gjr` | Liu et al. | Phys. Rev. D 101 (2020) 034020 | Unpolarized isovector quark distribution function from lattice QCD: A systematic analys... | 3.7, 4.6 | — |  |
| `LatticeParton:2022xsd` | Yao et al. | Phys. Rev. Lett. 131 (2023) 261901 | Nucleon Transversity Distribution in the Continuum and Physical Mass Limit from Lattice... | 4.9 | title |  |
| `LatticeParton:2022zqc` | Hua et al. | Phys. Rev. Lett. 129 (2022) 132001 | Pion and Kaon Distribution Amplitudes from Lattice QCD | 9.2 | — |  |
| `LatticePartonLPC:2022eev` | Chu et al. | Phys. Rev. D 106 (2022) 034509 | Nonperturbative determination of the Collins-Soper kernel from quasitransverse-momentum... | 10.3 | abstract |  |
| `Li:2018tpe` | Li–Ma–Qiu | Phys. Rev. Lett. 122 (2019) 062002 | Multiplicative Renormalizability of Operators defining Quasiparton Distributions | 3.2, 3.6 | — |  |
| `Lin:2018pvv` | Lin et al. | Phys. Rev. Lett. 121 (2018) 242003 | Proton Isovector Helicity Distribution on the Lattice at Physical Pion Mass | 4.6, 4.9 | abstract |  |
| `Liu:1993cv` | Liu–Dong | Phys. Rev. Lett. 72 (1994) 1790 | Origin of difference between anti-d and anti-u partons in the nucleon | 8.3 | read |  |
| `Liu:2018hxv` | Liu et al. | preprint arXiv:1810.05043 [hep-lat] (2018) | Nucleon Transversity Distribution at the Physical Pion Mass from Lattice QCD | 4.6, 4.9 | abstract | yes |
| `Liu:2018tox` | Liu et al. | Phys. Rev. D 99 (2019) 094036 | Matching the meson quasidistribution amplitude in the RI/MOM scheme | 9.2 | — |  |
| `Liu:2019urm` | Liu et al. | Phys. Rev. D 100 (2019) 034006 | Matching generalized parton quasidistributions in the RI/MOM scheme | 9.1 | abstract |  |
| `Ma:2022ggj` | Ma–Pang–Zhang | JHEP 08 (2022) 130 | QCD factorization of quasi generalized quark distributions | 9.1 | abstract |  |
| `Monahan:2016bvm` | Monahan–Orginos | JHEP 03 (2017) 116 | Quasi parton distributions and the gradient flow | 3.5 | abstract |  |
| `Monahan:2017hpu` | Monahan | Phys. Rev. D 97 (2018) 054507 | Smeared quasidistributions in perturbation theory | 3.5 | abstract |  |
| `Musch:2010ka` | Musch et al. | Phys. Rev. D 83 (2011) 094507 | Exploring quark transverse momentum distributions with lattice QCD | 10.3 | — |  |
| `Musch:2011er` | Musch et al. | Phys. Rev. D 85 (2012) 094510 | Sivers and Boer-Mulders observables from lattice QCD | 10.3 | — |  |
| `NieMiera:2025mwj` | NieMiera et al. | preprint arXiv:2510.17758 [hep-lat] (2025) | First Self-Renormalized Gluon PDF of Nucleon from Large-Momentum Effective Theory in th... | 4.10 | — | yes |
| `Radyushkin:1983wh` | Radyushkin | Phys. Lett. B 131 (1983) 179 | On Spectral Properties of Parton Correlation Functions and Multiparton Wave Functions | 1.3 | — |  |
| `Radyushkin:2017ffo` | Radyushkin | Phys. Lett. B 770 (2017) 514 | Target Mass Effects in Parton Quasi-Distributions | 5.1 | abstract |  |
| `Radyushkin:2017lvu` | Radyushkin | Phys. Lett. B 781 (2018) 433 | Quark pseudodistributions at short distances | 8.1 | — |  |
| `Radyushkin:2019mye` | Radyushkin | Int. J. Mod. Phys. A 35 (2020) 2030002 | Theory and applications of parton pseudodistributions | 8.1 | — |  |
| `Radyushkin:2019owq` | Radyushkin | Phys. Rev. D 100 (2019) 116011 | Generalized parton distributions and pseudodistributions | 9.1, 9.2 | — |  |
| `Rodini:2022wic` | Rodini–Vladimirov | JHEP 09 (2023) 117 | Factorization for quasi-TMD distributions of sub-leading power | 10.5 | abstract |  |
| `Schlemmer:2021aij` | Schlemmer et al. | JHEP 08 (2021) 004 | Determination of the Collins-Soper Kernel from Lattice QCD | 10.3 | — |  |
| `Shanahan:2020zxr` | Shanahan–Wagman–Zhao | Phys. Rev. D 102 (2020) 014511 | Collins-Soper kernel for TMD evolution from lattice QCD | 10.3 | — |  |
| `Shanahan:2021tst` | Shanahan–Wagman–Zhao | Phys. Rev. D 104 (2021) 114502 | Lattice QCD calculation of the Collins-Soper kernel from quasi-TMDPDFs | 10.3 | — |  |
| `Spanoudes:2024kpb` | Spanoudes–Constantinou–Panagopoulos | Phys. Rev. D 109 (2024) 114501 | Renormalization of asymmetric staple-shaped Wilson-line operators in lattice and contin... | 10.2 | — |  |
| `Stefanis:1983ke` | Stefanis | Nuovo Cim. A 83 (1984) 205 | GAUGE INVARIANT QUARK TWO POINT GREEN'S FUNCTION THROUGH CONNECTOR INSERTION TO O (alph... | 3.1 | — |  |
| `Stewart:2017tvs` | Stewart–Zhao | Phys. Rev. D 97 (2018) 054512 | Matching the quasiparton distribution in a momentum subtraction scheme | 3.7, 4.6 | — |  |
| `Su:2022fiu` | Su et al. | Nucl. Phys. B 991 (2023) 116201 | Resumming quark's longitudinal momentum logarithms in LaMET expansion of lattice PDFs | 4.7, 4.8, 5.5, 7.3 | read |  |
| `Tan:2025ofx` | Tan et al. | Phys. Rev. D 113 (2026) 054505 | Lattice QCD determination of the Collins-Soper kernel in the continuum and physical mas... | 10.3 | abstract |  |
| `Vladimirov:2020umg` | Vladimirov | Phys. Rev. Lett. 125 (2020) 192002 | Self-contained definition of the Collins-Soper kernel | 10.1 | abstract |  |
| `Wang:2017qyg` | Wang–Zhao–Zhu | Eur. Phys. J. C 78 (2018) 147 | Gluon quasidistribution function at one loop | 4.6 | — |  |
| `Wang:2019tgg` | Wang et al. | Phys. Rev. D 100 (2019) 074509 | Complete matching for quasidistribution functions in large momentum effective theory | 4.6, 4.10 | abstract |  |
| `Xiong:2015nua` | Xiong–Zhang | Phys. Rev. D 92 (2015) 054037 | One-loop matching for transversity generalized parton distribution | 9.1 | abstract |  |
| `Yao:2022vtp` | Yao–Ji–Zhang | JHEP 11 (2023) 021 | Connecting Euclidean to light-cone correlations: from flavor nonsinglet in forward kine... | 9.1, 4.10 | abstract |  |
| `Yoon:2017qzo` | Yoon et al. | Phys. Rev. D 96 (2017) 094508 | Nucleon Transverse Momentum-dependent Parton Distributions in Lattice QCD: Renormalizat... | 10.3 | — |  |
| `Zhang:2017bzy` | Zhang et al. | Phys. Rev. D 95 (2017) 094514 | Pion Distribution Amplitude from Lattice QCD | 9.2 | — |  |
| `Zhang:2018diq` | Zhang et al. | Phys. Rev. Lett. 122 (2019) 142001 | Accessing Gluon Parton Distributions in Large Momentum Effective Theory | 3.6 | abstract |  |
| `Zhang:2018ggy` | Zhang–Chen–Monahan | Phys. Rev. D 97 (2018) 074508 | Parton distribution functions from reduced Ioffe-time distributions | 4.6, 8.1 | — |  |
| `Zhang:2022xuw` | Zhang et al. | Phys. Rev. Lett. 129 (2022) 082002 | Renormalization of Transverse-Momentum-Dependent Parton Distribution on the Lattice | 10.2 | abstract |  |
| `Zhang:2023bxs` | Zhang et al. | Phys. Lett. B 844 (2023) 138081 | Leading power accuracy in lattice calculations of parton distributions | 13, 3.4, 5.4 | read |  |
| `Zhang:2023wea` | Zhang | preprint arXiv:2304.12481 [hep-ph] (2023) | Double Parton Distributions from Euclidean Lattice | 9.6 | abstract | yes |
| `Zhang:2024omt` | Zhang et al. | Phys. Rev. D 110 (2024) 074505 | Impact of gauge fixing precision on the continuum limit of nonlocal quark-bilinear latt... | 3.5 | title |  |
| `Zhang:2026lle` | Zhang et al. | preprint arXiv:2605.03234 [hep-ph] (2026) | Parton Distribution Functions from Large Momentum Expansion of Current-Current Correlators | 8.3 | read | yes |
| `Zhao:2023ptv` | Zhao | Phys. Rev. Lett. 133 (2024) 241904 | Transverse Momentum Distributions from Lattice QCD without Wilson Lines | 3.7, 10.2 | abstract |  |
| `Zhao:2025oto` | Zhao | Research 9 (2026) 1181 | Improving the Precision of First-Principles Calculation of Parton Physics from Lattice ... | 10.5 | abstract |  |
| `Zhu:2022bja` | Zhu et al. | JHEP 02 (2023) 114 | Gluon transverse-momentum-dependent distributions from large-momentum effective theory | 10.5 | abstract |  |

### 4.3 New keys from frontier/others/others.bib (report OTHERS.md) — 145 entries

| key | authors | publication | title | cited in (report §) | depth | preprint |
|---|---|---|---|---|---|---|
| `Adamiak:2023okq` | Adamiak–Kovchegov–Tawabutr | Phys. Rev. D 108 (2023) 054005 | Helicity evolution at small x: Revised asymptotic results at large Nc and Nf | 9 | abstract |  |
| `Akhoury:2001mz` | Akhoury–Wang–Yakovlev | Phys. Rev. D 64 (2001) 113008 | On the Resummation of large QCD logarithms in Higgs ---\ensuremath> gamma gamma decay | 5 | abstract |  |
| `Alioli:2023rxx` | Alioli et al. | Phys. Rev. D 109 (2024) 094009 | N3LL resummation of one-jettiness for Z-boson plus jet production at hadron colliders | 4 | abstract |  |
| `Anastasiou:2018rib` | Anastasiou–Sterman | JHEP 07 (2019) 056 | Removing infrared divergences from two-loop integrals | 0 | abstract |  |
| `Anastasiou:2020sdt` | Anastasiou et al. | JHEP 04 (2021) 222 | Locally finite two-loop amplitudes for off-shell multi-photon production in electron-po... | 0 | abstract |  |
| `Anastasiou:2022eym` | Anastasiou–Sterman | JHEP 05 (2023) 242 | Locally finite two-loop QCD amplitudes from IR universality for electroweak production | 0 | abstract |  |
| `Anastasiou:2024xvk` | Anastasiou et al. | JHEP 11 (2024) 043 | Locally finite two-loop amplitudes for electroweak production through gluon fusion | 0 | abstract |  |
| `Anastasiou:2025cvy` | Anastasiou et al. | preprint arXiv:2509.07805 [hep-ph] (2025) | General finite two-loop amplitude integrand for photoproduction in quark annihilation | 0 | abstract | yes |
| `Anastasiou:2026jta` | Anastasiou et al. | preprint arXiv:2603.12862 [hep-ph] (2026) | Ward identity preserving local ultraviolet counterterms for photoproduction at two loop... | 0 | abstract | yes |
| `Anastasiou:2026kpm` | Anastasiou et al. | preprint arXiv:2601.22936 [hep-ph] (2026) | Local finiteness for real-virtual corrections to electroweak production in partonic col... | 0 | abstract | yes |
| `Angeles-Martinez:2015rna` | Angeles-Martinez–Forshaw–Seymour | JHEP 12 (2015) 091 | Coulomb gluons and the ordering variable | 4 | abstract |  |
| `Bahjat-Abbas:2018hpv` | Bahjat-Abbas et al. | JHEP 10 (2018) 144 | On next-to-leading power threshold corrections in Drell-Yan production at N$^3$LO | 5 | abstract |  |
| `Balitsky:2006wa` | Balitsky | Phys. Rev. D 75 (2007) 014001 | Quark contribution to the small-x evolution of color dipole | 9 | abstract |  |
| `Balitsky:2013fea` | Balitsky–Chirilli | Phys. Rev. D 88 (2013) 111501 | Rapidity evolution of Wilson lines at the next-to-leading order | 9 | abstract |  |
| `Balitsky:2015qba` | Balitsky–Tarasov | JHEP 10 (2015) 017 | Rapidity evolution of gluon TMD from low to moderate x | 9 | abstract |  |
| `Balitsky:2017flc` | Balitsky–Tarasov | JHEP 07 (2017) 095 | Higher-twist corrections to gluon TMD factorization | 6 | abstract |  |
| `Balitsky:2017gis` | Balitsky–Tarasov | JHEP 05 (2018) 150 | Power corrections to TMD factorization for Z-boson production | 6 | abstract |  |
| `Balitsky:2020jzt` | Balitsky | JHEP 05 (2021) 046 | Gauge-invariant TMD factorization for Drell-Yan hadronic tensor at small x | 9 | abstract |  |
| `Balitsky:2021fer` | Balitsky | JHEP 09 (2021) 022 | Drell-Yan angular lepton distributions at small x from TMD factorization. | 9 | abstract |  |
| `Balitsky:2023hmh` | Balitsky | JHEP 03 (2023) 029 | Rapidity-only TMD factorization at one loop | 9 | abstract |  |
| `Balitsky:2024ozy` | Balitsky | Nucl. Phys. B 1006 (2024) 116658 | $1/Q^2$ power corrections to TMD factorization for Drell-Yan hadronic tensor | 6 | abstract |  |
| `Balitsky:2026lop` | Balitsky | Phys. Lett. B 882 (2026) 141002 | Interpolation between Sudakov and BFKL rapidity evolutions for TMD factorization at sma... | 9 | abstract |  |
| `Banerjee:2025kkq` | Banerjee et al. | JHEP 02 (2026) 092 | Super-leading logarithms in top-quark pair production at hadron colliders | 4 | abstract |  |
| `Banfi:2021owj` | Banfi–Dreyer–Monni | JHEP 10 (2021) 006 | Next-to-leading non-global logarithms in QCD | 11 | abstract |  |
| `Banfi:2021xzn` | Banfi–Dreyer–Monni | JHEP 03 (2022) 135 | Higher-order non-global logarithms from jet calculus | 11 | abstract |  |
| `Barnich:2000zw` | Barnich–Brandt–Henneaux | Phys. Rept. 338 (2000) 439 | Local BRST cohomology in gauge theories | 8 | abstract |  |
| `Bauer:2010cc` | Bauer–Lange–Ovanesyan | JHEP 07 (2011) 077 | On Glauber modes in Soft-Collinear Effective Theory | 4 | abstract |  |
| `Bauer:2017isx` | Bauer–Ferland–Webber | JHEP 08 (2017) 036 | Standard Model Parton Distributions at Very High Energies | 13 | abstract |  |
| `Bauer:2018arx` | Bauer–Webber | JHEP 03 (2019) 013 | Polarization Effects in Standard Model Parton Distributions at Very High Energies | 13 | abstract |  |
| `Baumgart:2018ntv` | Baumgart et al. | Phys. Rev. D 100 (2019) 096008 | Breakdown of the naive parton model in super-weak scale collisions | 13 | abstract |  |
| `Becher:2016omr` | Becher–Pecjak–Shao | JHEP 12 (2016) 018 | Factorization for the light-jet mass and hemisphere soft function | 11 | abstract |  |
| `Becher:2021urs` | Becher–Rauh–Xu | JHEP 08 (2022) 134 | Two-loop anomalous dimension for the resummation of non-global observables | 11 | abstract |  |
| `Becher:2023vrh` | Becher–Schalch–Xu | Phys. Rev. Lett. 132 (2024) 081602 | Resummation of Next-to-Leading Nonglobal Logarithms at the LHC | 11 | abstract |  |
| `Becher:2025igg` | Becher et al. | JHEP 01 (2026) 024 | Low-energy theory of jet processes and PDF factorization | 4 | abstract |  |
| `Becher:2026iim` | Becher et al. | preprint arXiv:2609.35972 [hep-ph] (2026) | Resummation of Next-to-Leading Non-Global Logarithms in Higgs Production | 11 | abstract | yes |
| `Becher:2026zon` | Becher–Haag–Schalch | preprint arXiv:2609.09104 [hep-ph] (2026) | Two-Loop Anomalous Dimension for Non-Global and Clustering Logarithms | 11 | abstract | yes |
| `Becker:2012nk` | Becker–Weinzierl | Phys. Rev. D 86 (2012) 074009 | Direct contour deformation with arbitrary masses in the loop | 0 | abstract |  |
| `Beneke:2019oqx` | Beneke et al. | JHEP 07 (2020) 078 | Threshold factorization of the Drell-Yan process at next-to-leading power | 5 | abstract |  |
| `Beneke:2020ibj` | Beneke et al. | JHEP 10 (2020) 196 | Large-x resummation of off-diagonal deep-inelastic parton scattering from d-dimensional... | 5 | abstract |  |
| `Beneke:2024cpq` | Beneke–Ji–Wang | JHEP 05 (2024) 246 | Renormalization of the next-to-leading-power \ensuremath\gamma\ensuremath\gamma \textri... | 5 | abstract |  |
| `Beneke:2025ufd` | Beneke et al. | JHEP 05 (2025) 067 | Renormalization of the next-to-leading-power soft function for the Drell-Yan off-diagon... | 5 | abstract |  |
| `Berghoff:2022mqu` | Berghoff–Panzer | J. Geom. Phys. 216 (2025) 105539 | Hierarchies in relative Picard-Lefschetz theory | 0 | abstract |  |
| `Bertone:2019hks` | Bertone et al. | JHEP 03 (2020) 135 | The partonic structure of the electron at the next-to-leading logarithmic accuracy in QED | 13 | abstract |  |
| `Beuf:2014uia` | Beuf | Phys. Rev. D 89 (2014) 074039 | Improving the kinematics for low-$x$ QCD evolution equations in coordinate space | 9 | abstract |  |
| `Bodwin:2014gia` | Bodwin et al. | Phys. Rev. Lett. 113 (2014) 022001 | Fragmentation contributions to $J/\psi$ production at the Tevatron and the LHC | 12 | abstract |  |
| `Bodwin:2019bpf` | Bodwin et al. | Phys. Rev. D 101 (2020) 096011 | Covariant calculation of a two-loop test of nonrelativistic QCD factorization | 12 | abstract |  |
| `Bodwin:2021cpx` | Bodwin et al. | Phys. Rev. D 104 (2021) 016010 | Analyticity, renormalization, and evolution of the soft-quark function | 5 | abstract |  |
| `Bodwin:2021epw` | Bodwin et al. | Phys. Rev. D 104 (2021) 116025 | Renormalization of the radiative jet function | 5 | abstract |  |
| `Bodwin:2023asf` | Bodwin et al. | Phys. Rev. D 109 (2024) 056020 | Gauge invariance of radiative jet functions in the position-space formulation of SCET | 5 | abstract |  |
| `Bodwin:2025zzi` | Bodwin et al. | preprint arXiv:2512.11647 [hep-ph] (2025) | Hidden self-energy contributions of collinear functions in SCET | 5 | abstract | yes |
| `Boer:2023jsy` | Boer–Neubert–Stillger | JHEP 10 (2023) 075 | Glauber phases in non-global LHC observables: resummation for quark-initiated processes | 4 | abstract |  |
| `Boer:2023ljq` | Boer et al. | JHEP 02 (2024) 109 | Glauber phases in non-global LHC observables: resummation for gluon-initiated processes | 4 | abstract |  |
| `Boer:2024xzy` | Boer et al. | JHEP 08 (2024) 036 | Resummation of Glauber phases in non-global LHC observables for large N$_c$ | 4 | abstract |  |
| `Bonocore:2015esa` | Bonocore et al. | JHEP 06 (2015) 008 | A factorization approach to next-to-leading-power threshold logarithms | 5 | abstract |  |
| `Bonocore:2016awd` | Bonocore et al. | JHEP 12 (2016) 121 | Non-abelian factorisation for next-to-leading-power threshold logarithms | 5 | abstract |  |
| `Borden:2023ugd` | Borden–Kovchegov | Phys. Rev. D 108 (2023) 014001 | Analytic solution for the revised helicity evolution at small x and large Nc: New resum... | 9 | abstract |  |
| `Borden:2024bxa` | Borden–Kovchegov–Li | JHEP 09 (2024) 037 | Helicity evolution at small x: quark to gluon and gluon to quark transition operators | 9 | abstract |  |
| `Borden:2025ehe` | Borden–Kovchegov | Phys. Rev. D 113 (2026) 034002 | Analytic solution for the helicity evolution equations at small x and large Nc and Nf | 9 | abstract |  |
| `BrisCuerpo:2026pma` | Bris Cuerpo–Arroyo-Castro–Vladimirov | Phys. Rev. D 114 (2026) 034028 | Factorization theorem for quasi-TMD distributions with kinematic power corrections | 6 | abstract |  |
| `Buonocore:2020nai` | Buonocore et al. | JHEP 08 (2020) 019 | Leptons in the proton | 13 | abstract |  |
| `Butenschoen:2014dra` | Butenschoen–He–Kniehl | Phys. Rev. Lett. 114 (2015) 092004 | $\eta_c$ production at the LHC challenges nonrelativistic-QCD factorization | 12 | abstract |  |
| `Caron-Huot:2013fea` | Caron-Huot | JHEP 05 (2015) 093 | When does the gluon reggeize? | 9 | read |  |
| `Caron-Huot:2016tzz` | Caron-Huot–Herranen | JHEP 02 (2018) 058 | High-energy evolution to three loops | 9 | abstract |  |
| `Caron-Huot:2017zfo` | Caron-Huot et al. | JHEP 03 (2018) 098 | Infrared singularities of QCD scattering amplitudes in the Regge limit to all orders | 9 | abstract |  |
| `Catani:2014qha` | Catani–Grazzini–Torre | Nucl. Phys. B 890 (2014) 518 | Transverse-momentum resummation for heavy-quark hadroproduction | 4 | abstract |  |
| `Ciafaloni:2000df` | Ciafaloni–Ciafaloni–Comelli | Phys. Rev. Lett. 84 (2000) 4810 | Bloch-Nordsieck violating electroweak corrections to inclusive TeV scale hard processes | 13 | abstract |  |
| `Cougoulic:2022gbk` | Cougoulic et al. | JHEP 07 (2022) 095 | Quark and gluon helicity evolution at small x: revised and updated | 9 | abstract |  |
| `deFlorian:2015ujt` | de Florian–Sborlini–Rodrigo | Eur. Phys. J. C 76 (2016) 282 | QED corrections to the Altarelli\textendashParisi splitting functions | 13 | abstract |  |
| `deFlorian:2016gvk` | de Florian–Sborlini–Rodrigo | JHEP 10 (2016) 056 | Two-loop QED corrections to the Altarelli-Parisi splitting functions | 13 | abstract |  |
| `DelDuca:2013ara` | Del Duca et al. | Phys. Lett. B 732 (2014) 233 | High-energy QCD amplitudes at two loops and beyond | 9 | abstract |  |
| `DelDuca:2014cya` | Del Duca et al. | JHEP 02 (2015) 029 | Analyzing high-energy factorization beyond next-to-leading logarithmic accuracy | 9 | abstract |  |
| `Diehl:2019rdh` | Diehl et al. | SciPost Phys. 7 (2019) 017 | Two-loop splitting in double parton distributions | 10 | abstract |  |
| `Diehl:2020xyg` | Diehl et al. | Eur. Phys. J. C 80 (2020) 468 | Sum rule improved double parton distributions in position space | 10 | abstract |  |
| `Diehl:2022dia` | Diehl–Nagar–Plossl | JHEP 09 (2023) 100 | Quark mass effects in double parton distributions | 10 | abstract |  |
| `Diehl:2022rxb` | Diehl–Fabry–Vladimirov | JHEP 05 (2023) 067 | Two-loop evolution kernels for colour dependent double parton distributions | 10 | abstract |  |
| `Dixon:2019uzg` | Dixon–Moult–Zhu | Phys. Rev. D 100 (2019) 014009 | Collinear limit of the energy-energy correlator | 11 | abstract |  |
| `Ebert:2018gsn` | Ebert et al. | JHEP 04 (2019) 123 | Subleading power rapidity divergences and power corrections for q$_T$ | 6 | abstract |  |
| `Ebert:2021jhy` | Ebert–Gao–Stewart | JHEP 06 (2022) 007 | Factorization for azimuthal asymmetries in SIDIS at next-to-leading power | 6 | abstract |  |
| `Efremov:2017sqi` | Efremov–Guida–Kopper | J. Math. Phys. 58 (2017) 093503 | Renormalization of SU(2) Yang\textendashMills theory with flow equations | 2 | abstract |  |
| `Erdogan:2013bga` | Erdougan | Phys. Rev. D 89 (2014) 085016 | Coordinate-space singularities of massless gauge theories | 0 | abstract |  |
| `Erdogan:2014gha` | Erdougan–Sterman | Phys. Rev. D 91 (2015) 065033 | Ultraviolet divergences and factorization for coordinate-space amplitudes | 0 | abstract |  |
| `Erdogan:2017gyf` | Erdougan–Sterman | Phys. Rev. D 95 (2017) 116015 | Path description of coordinate-space amplitudes | 0 | abstract |  |
| `Falcioni:2022fdm` | Falcioni–Herzog | JHEP 05 (2022) 177 | Renormalization of gluonic leading-twist operators in covariant gauges | 8 | abstract |  |
| `Fevola:2023fzn` | Fevola–Mizera–Telen | Comput. Phys. Commun. 303 (2024) 109278 | Principal Landau determinants | 0 | abstract |  |
| `Fornal:2018znf` | Fornal–Manohar–Waalewijn | JHEP 05 (2018) 106 | Electroweak Gauge Boson Parton Distribution Functions | 13 | abstract |  |
| `Forshaw:2021fxs` | Forshaw–Holguin | JHEP 12 (2021) 084 | Coulomb gluons will generally destroy coherence | 4 | abstract |  |
| `Frixione:2019lga` | Frixione | JHEP 11 (2019) 158 | Initial conditions for electron and photon structure and fragmentation functions | 13 | read |  |
| `Frob:2016mzv` | Frob–Holland | preprint arXiv:1603.08012 [math-ph] (2016) | All-order existence of and recursion relations for the operator product expansion in Ya... | 2 | read | yes |
| `Frye:2016aiz` | Frye et al. | JHEP 07 (2016) 064 | Factorization for groomed jet substructure beyond the next-to-leading logarithm | 11 | abstract |  |
| `Gamberg:2022lju` | Gamberg et al. | preprint arXiv:2211.13209 [hep-ph] (2022) | Transverse-momentum-dependent factorization at next-to-leading power | 6 | abstract | yes |
| `Gehrmann:2023ksf` | Gehrmann–von Manteuffel–Yang | JHEP 04 (2023) 041 | Renormalization of twist-two operators in covariant gauge to three loops in QCD | 8 | abstract |  |
| `Gong:2008ww` | Gong–Nagy–Soper | Phys. Rev. D 79 (2009) 033005 | Direct numerical integration of one-loop Feynman diagrams for N-photon amplitudes | 0 | abstract |  |
| `Guan:2024hlf` | Guan et al. | JHEP 01 (2025) 090 | Splitting amplitudes at N$^3$LO in QCD | 4 | abstract |  |
| `Guida:2011np` | Guida–Kopper | preprint arXiv:1103.5692 [math-ph] (2011) | All-order uniform momentum bounds for the massless $\phi^4$ theory in four dimensional ... | 2 | abstract | yes |
| `Hamberg:1991qt` | Hamberg–van Neerven | Nucl. Phys. B 379 (1992) 143 | The Correct renormalization of the gluon operator in a covariant gauge | 8 | abstract |  |
| `Han:2014jya` | Han et al. | Phys. Rev. Lett. 114 (2015) 092005 | $\eta_c$ production at LHC and indications on the understanding of $J/\psi$ production | 12 | abstract |  |
| `Hannesdottir:2022bmo` | Hannesdottir–Mizera | book Springer (2023) | What is the i\ensuremath\varepsilon for the S-matrix? | 0 | abstract |  |
| `Hatta:2016aoc` | Hatta et al. | Phys. Rev. D 95 (2017) 114032 | Gluon orbital angular momentum at small-$x$ | 9 | abstract |  |
| `Hatta:2022bxn` | Hatta–Zhou | Phys. Rev. Lett. 129 (2022) 252002 | Small-$x$ evolution of the gluon GPD $E_g$ | 9 | abstract |  |
| `Heinrich:2021dbf` | Heinrich et al. | Comput. Phys. Commun. 273 (2022) 108267 | Expansion by regions with pySecDec | 3 | abstract |  |
| `Helmer:2024wax` | Helmer–Papathanasiou–Tellander | Phys. Rev. D 114 (2026) L011901 | Landau singularities from Whitney stratifications | 0 | abstract |  |
| `Hoang:2019ceu` | Hoang et al. | JHEP 12 (2019) 002 | Nonperturbative Corrections to Soft Drop Jet Mass | 11 | abstract |  |
| `Holland:2014ifa` | Holland–Hollands | Commun. Math. Phys. 336 (2015) 1555 | Recursive construction of operator product expansion coefficients | 2 | abstract |  |
| `Holland:2015tia` | Holland–Hollands | J. Math. Phys. 56 (2015) 122303 | Associativity of the operator product expansion | 2 | abstract |  |
| `Iancu:2015vea` | Iancu et al. | Phys. Lett. B 744 (2015) 293 | Resumming double logarithms in the QCD evolution of color dipoles | 9 | abstract |  |
| `Inglis-Whalen:2021bea` | Inglis-Whalen et al. | Phys. Rev. D 104 (2021) 076018 | Factorization of power corrections in the Drell-Yan process in EFT | 6 | abstract |  |
| `Kang:2014pya` | Kang et al. | Phys. Rev. D 91 (2015) 014030 | Heavy Quarkonium Production at Collider Energies: Partonic Cross Section and Polarization | 12 | abstract |  |
| `Kang:2014tta` | Kang et al. | Phys. Rev. D 90 (2014) 034006 | Heavy Quarkonium Production at Collider Energies: Factorization and Evolution | 12 | abstract |  |
| `Keller:1990ej` | Keller–Kopper–Salmhofer | Helv. Phys. Acta 65 (1992) 32 | Perturbative renormalization and effective Lagrangians in phi**4 in four-dimensions | 2 | — |  |
| `Keller:1991cj` | Keller–Kopper | Phys. Lett. B 273 (1991) 323 | Perturbative renormalization of QED via flow equations | 2 | abstract |  |
| `Keller:1995qn` | Keller–Kopper | Commun. Math. Phys. 176 (1996) 193 | Renormalizability proof for QED based on flow equations | 2 | abstract |  |
| `Kologlu:2019mfz` | Kologlu et al. | JHEP 01 (2021) 128 | The light-ray OPE and conformal colliders | 11 | abstract |  |
| `Kopper:1999qx` | Kopper–Muller | Commun. Math. Phys. 209 (2000) 477 | Renormalization proof for spontaneously broken Yang-Mills theory with flow equations | 2 | abstract |  |
| `Kopper:2009zw` | Kopper–Muller | Rev. Math. Phys. 21 (2009) 781 | Renormalization of Spontaneaously Broken SU(2) Yang-Mills Theory with Flow Equations | 2 | abstract |  |
| `Kotsky:1997rq` | Kotsky–Yakovlev | Phys. Lett. B 418 (1998) 335 | On the resummation of double logarithms in the process Higgs ---\ensuremath> gamma gamma | 5 | abstract |  |
| `Kovchegov:2006vj` | Kovchegov–Weigert | Nucl. Phys. A 784 (2007) 188 | Triumvirate of Running Couplings in Small-x Evolution | 9 | abstract |  |
| `Kovchegov:2015pbl` | Kovchegov–Pitonyak–Sievert | JHEP 01 (2016) 072 | Helicity Evolution at Small-x | 9 | abstract |  |
| `Kovchegov:2016weo` | Kovchegov–Pitonyak–Sievert | Phys. Rev. Lett. 118 (2017) 052001 | Small-$x$ asymptotics of the quark helicity distribution | 9 | abstract |  |
| `Kovner:2013ona` | Kovner–Lublinsky–Mulian | Phys. Rev. D 89 (2014) 061704 | Jalilian-Marian, Iancu, McLerran, Weigert, Leonidov, Kovner evolution at next to leadin... | 9 | abstract |  |
| `Kovner:2014lca` | Kovner–Lublinsky–Mulian | JHEP 08 (2014) 114 | NLO JIMWLK evolution unabridged | 9 | abstract |  |
| `Kovner:2014xia` | Kovner–Lublinsky–Mulian | JHEP 04 (2014) 030 | Conformal symmetry of JIMWLK Evolution at NLO | 9 | abstract |  |
| `Lappi:2015fma` | Lappi–Mantysaari | Phys. Rev. D 91 (2015) 074016 | Direct numerical solution of the coordinate space Balitsky-Kovchegov equation at next t... | 9 | abstract |  |
| `Larkoski:2015zka` | Larkoski–Moult–Neill | JHEP 09 (2015) 143 | Non-Global Logarithms, Factorization, and the Soft Substructure of Jets | 11 | abstract |  |
| `Liu:2017vkm` | Liu–Penin | Phys. Rev. Lett. 119 (2017) 262001 | High-Energy Limit of QCD beyond the Sudakov Approximation | 5 | abstract |  |
| `Liu:2018czl` | Liu–Penin | JHEP 11 (2018) 158 | High-Energy Limit of Mass-Suppressed Amplitudes in Gauge Theories | 5 | abstract |  |
| `Ma:2013yla` | Ma–Qiu–Zhang | Phys. Rev. D 89 (2014) 094029 | Heavy quarkonium fragmentation functions from a heavy quark pair. I. $S$ wave | 12 | abstract |  |
| `Ma:2014eja` | Ma–Qiu–Zhang | Phys. Rev. D 89 (2014) 094030 | Heavy quarkonium fragmentation functions from a heavy quark pair. II. $P$ wave | 12 | abstract |  |
| `Ma:2017xno` | Ma–Chao | Phys. Rev. D 100 (2019) 094007 | New factorization theory for heavy quarkonium production and decay | 12 | abstract |  |
| `Manohar:2018kfx` | Manohar–Waalewijn | JHEP 08 (2018) 137 | Electroweak Logarithms in Inclusive Cross Sections | 13 | abstract |  |
| `Mitov:2012gt` | Mitov–Sterman | Phys. Rev. D 86 (2012) 114038 | Final state interactions in single- and multi-particle inclusive cross sections for had... | 4 | abstract |  |
| `Mizera:2021icv` | Mizera–Telen | JHEP 08 (2022) 200 | Landau discriminants | 0 | abstract |  |
| `Moult:2018jjd` | Moult et al. | JHEP 08 (2018) 013 | First Subleading Power Resummation for Event Shapes | 5 | abstract |  |
| `Moult:2019mog` | Moult–Stewart–Vita | JHEP 11 (2019) 153 | Subleading Power Factorization with Radiative Functions | 5 | abstract |  |
| `Mueller:2012uf` | Mueller–Xiao–Yuan | Phys. Rev. Lett. 110 (2013) 082301 | Sudakov Resummation in Small-$x$ Saturation Formalism | 9 | abstract |  |
| `Penin:2014msa` | Penin | Phys. Lett. B 745 (2015) 69 | High-Energy Limit of Quantum Electrodynamics beyond Sudakov Approximation | 5 | abstract |  |
| `Piguet:1995er` | Piguet–Sorella | book Springer (1995) | Algebraic renormalization: Perturbative renormalization, symmetries and anomalies | 2 | abstract |  |
| `Piloneta:2025jjb` | Piloneta–Vladimirov | JHEP 03 (2026) 049 | Kinematic power corrections for TMD factorization theorem of semi-inclusive deep-inelas... | 6 | abstract |  |
| `Rodini:2022wki` | Rodini–Vladimirov | JHEP 08 (2022) 031 | Definition and evolution of transverse momentum dependent distribution of twist-three | 6 | abstract |  |
| `Rodini:2023plb` | Rodini–Vladimirov | Phys. Rev. D 110 (2024) 034009 | Transverse momentum dependent factorization for SIDIS at next-to-leading power | 6 | abstract |  |
| `Schwartz:2017nmr` | Schwartz–Yan–Zhu | Phys. Rev. D 96 (2017) 056005 | Collinear factorization violation and effective field theory | 4 | abstract |  |
| `Sterman:2025qsq` | Sterman–Erdougan | Eur. Phys. J. ST 235 (2026) 1493 | Coordinate light-cone-ordered perturbation theory | 0 | abstract |  |
| `Stewart:2010tn` | Stewart–Tackmann–Waalewijn | Phys. Rev. Lett. 105 (2010) 092002 | N-Jettiness: An Inclusive Event Shape to Veto Jets | 4 | abstract |  |
| `Vladimirov:2021hdn` | Vladimirov–Moos–Scimemi | JHEP 01 (2022) 110 | Transverse momentum dependent operator expansion at next-to-leading power | 6 | abstract |  |
| `Vladimirov:2023aot` | Vladimirov | JHEP 12 (2023) 008 | Kinematic power corrections in TMD factorization theorem | 6 | abstract |  |
| `Zhang:2014ybe` | Zhang et al. | Phys. Rev. Lett. 114 (2015) 092006 | Impact of $\eta_c$ hadroproduction data on charmonium production and polarization withi... | 12 | abstract |  |

### 4.4 New keys from spec-v2 additions (INSPIRE-HEP) — 41 entries (38 + 3 of spec v2.1)

| key | authors | publication | title | cited in (report §) | depth | preprint |
|---|---|---|---|---|---|---|
| `Baikov:2016tgj` | Baikov–Chetyrkin–Kuhn | Phys. Rev. Lett. 118 (2017) 082002 | Five-Loop Running of the QCD Coupling Constant |  | — |  |
| `Bartels:1995iu` | Bartels–Ermolaev–Ryskin | Z. Phys. C 70 (1996) 273 | Nonsinglet contributions to the structure function $g_1$ at small $x$ | OTHERS §9.5 (via Borden–Kovchegov) | — (v2.1) |  |
| `Bartels:1996wc` | Bartels–Ermolaev–Ryskin | Z. Phys. C 72 (1996) 627 | Flavor singlet contribution to the structure function $g_1$ at small $x$ | OTHERS §9.5 (via Borden–Kovchegov) | — (v2.1) |  |
| `Beneke:1998eq` | Beneke–Braun–Kivel | Phys. Lett. B 443 (1998) 308 | The Operator product expansion, nonperturbative couplings and the Landau pole: Lessons ... |  | — |  |
| `Blumlein:1996hb` | Blümlein–Vogt | Phys. Lett. B 386 (1996) 350 | The singlet contribution to the structure function $g_1(x,Q^2)$ at small $x$ | OTHERS §9.5 (via Borden–Kovchegov) | — (v2.1) |  |
| `Bostelmann:2005rr` | Bostelmann | J. Math. Phys. 46 (2005) 082304 | Operator product expansions as a consequence of phase space properties |  | — |  |
| `Brodsky:1997de` | Brodsky–Pauli–Pinsky | Phys. Rept. 301 (1998) 299 | Quantum chromodynamics and other field theories on the light cone |  | — |  |
| `Callan:1970yg` | Callan | Phys. Rev. D 2 (1970) 1541 | Broken scale invariance in scalar field theory |  | — |  |
| `Chang:1973qi` | Chang–Yan | Phys. Rev. D 7 (1973) 1147 | Quantum field theories in the infinite momentum frame. 2. Scattering matrices of scalar... |  | — |  |
| `Chay:2003ju` | Chay–Kim | Nucl. Phys. B 680 (2004) 302 | Nonleptonic B decays into two light mesons in soft collinear effective theory |  | — |  |
| `Cheng:1969eh` | Cheng–Wu | Phys. Rev. Lett. 22 (1969) 666 | High-energy elastic scattering in quantum electrodynamics |  | — |  |
| `Chetyrkin:1982zq` | Chetyrkin–Tkachov–Gorishnii | Phys. Lett. B 119 (1982) 407 | OPERATOR PRODUCT EXPANSION IN THE MINIMAL SUBTRACTION SCHEME |  | — |  |
| `Collins:2016hqq` | Collins et al. | Phys. Rev. D 94 (2016) 034014 | Relating Transverse Momentum Dependent and Collinear Factorization Theorems in a Genera... |  | — |  |
| `Collins:2018aqt` | Collins | preprint arXiv:1801.03960 [hep-ph] (2018) | The non-triviality of the vacuum in light-front quantization: An elementary treatment |  | — | yes |
| `Czakon:2004bu` | Czakon | Nucl. Phys. B 710 (2005) 485 | The Four-loop QCD beta-function and anomalous dimensions |  | — |  |
| `David:1982qv` | David | Nucl. Phys. B 209 (1982) 433 | Nonperturbative Effects and Infrared Renormalons Within the 1/$N$ Expansion of the O($N... |  | — |  |
| `Faddeev:1967fc` | Faddeev–Popov | Phys. Lett. B 25 (1967) 29 | Feynman Diagrams for the Yang-Mills Field |  | — |  |
| `Feldman:1986ax` | Feldman et al. | Commun. Math. Phys. 103 (1986) 67 | A Renormalizable Field Theory: The Massive Gross-Neveu Model in Two-dimensions |  | — |  |
| `Fritzsch:1973pi` | Fritzsch–Gell-Mann–Leutwyler | Phys. Lett. B 47 (1973) 365 | Advantages of the Color Octet Gluon Picture |  | — |  |
| `Gawedzki:1985ez` | Gawedzki–Kupiainen | Commun. Math. Phys. 102 (1985) 1 | GROSS-NEVEU MODEL THROUGH CONVERGENT PERTURBATION EXPANSIONS |  | — |  |
| `Gell-Mann:1954yli` | Gell-Mann–Low | Phys. Rev. 95 (1954) 1300 | Quantum electrodynamics at small distances |  | — |  |
| `Gell-Mann:1964ewy` | Gell-Mann | Phys. Lett. 8 (1964) 214 | A Schematic Model of Baryons and Mesons |  | — |  |
| `Greenberg:1964pe` | Greenberg | Phys. Rev. Lett. 13 (1964) 598 | Spin and Unitary Spin Independence in a Paraquark Model of Baryons and Mesons |  | — |  |
| `Haag:1958vt` | Haag | Phys. Rev. 112 (1958) 669 | Quantum field theories with composite particles and asymptotic conditions |  | — |  |
| `Han:1965pf` | Han–Nambu | Phys. Rev. 139 (1965) B1006 | Three Triplet Model with Double SU(3) Symmetry |  | — |  |
| `Herzog:2017ohr` | Herzog et al. | JHEP 02 (2017) 090 | The five-loop beta function of Yang-Mills theory with fermions |  | — |  |
| `Itzykson:1980rh` | Itzykson–Zuber | book McGraw-Hill (1980) | Quantum Field Theory |  | — |  |
| `Jost:1965yxu` | Jost | book American Mathematical Society (1965) | The general theory of quantized fields |  | — |  |
| `Kogut:1969xa` | Kogut–Soper | Phys. Rev. D 1 (1970) 2901 | Quantum Electrodynamics in the Infinite Momentum Frame |  | — |  |
| `Korchemskaya:1994qp` | Korchemskaya–Korchemsky | Nucl. Phys. B 437 (1995) 127 | High-energy scattering in QCD and cross singularities of Wilson loops |  | — |  |
| `Korchemsky:1993hr` | Korchemsky | Phys. Lett. B 325 (1994) 459 | On Near forward high-energy scattering in QCD |  | — |  |
| `Larin:1993tp` | Larin–Vermaseren | Phys. Lett. B 303 (1993) 334 | The Three loop QCD Beta function and anomalous dimensions |  | — |  |
| `Ligterink:1994tm` | Ligterink–Bakker | Phys. Rev. D 52 (1995) 5954 | Equivalence of light front and covariant field theory |  | — |  |
| `Nielsen:1980sx` | Nielsen | Am. J. Phys. 49 (1981) 1171 | ASYMPTOTIC FREEDOM AS A SPIN EFFECT |  | — |  |
| `Novikov:1984ac` | Novikov et al. | Phys. Rept. 116 (1984) 103 | Two-Dimensional Sigma Models: Modeling Nonperturbative Effects of Quantum Chromodynamics |  | — |  |
| `ParticleDataGroup:2024cfk` | Navas et al. | Phys. Rev. D 110 (2024) 030001 | Review of particle physics |  | — |  |
| `Symanzik:1970rt` | Symanzik | Commun. Math. Phys. 18 (1970) 227 | Small distance behavior in field theory and power counting |  | — |  |
| `Tarasov:1980au` | Tarasov–Vladimirov–Zharkov | Phys. Lett. B 93 (1980) 429 | The Gell-Mann-Low Function of QCD in the Three Loop Approximation |  | — |  |
| `vanRitbergen:1997va` | van Ritbergen–Vermaseren–Larin | Phys. Lett. B 400 (1997) 379 | The Four loop beta function in quantum chromodynamics |  | — |  |
| `Wilson:1974sk` | Wilson | Phys. Rev. D 10 (1974) 2445 | Confinement of Quarks |  | — |  |
| `Yang:1954ek` | Yang–Mills | Phys. Rev. 96 (1954) 191 | Conservation of Isotopic Spin and Isotopic Gauge Invariance |  | — |  |

### 4.5 New keys from spec-v2 manual entries (Crossref) — 5 entries (3 + 2 of spec v2.1)

| key | authors | publication | title | cited in (report §) | depth | preprint |
|---|---|---|---|---|---|---|
| `Epstein1960` | Epstein | J. Math. Phys. 1 (1960) 524 | Generalization of the ``Edge-of-the-Wedge'' Theorem |  | — |  |
| `Markoff1916` | Markoff | Math. Ann. 77 (1916) 213 | \"Uber Polynome, die in einem gegebenen Intervalle m\"oglichst wenig von Null abweichen |  | — |  |
| `Zweig:1964jf` | Zweig | techreport CERN (1964) | An SU(3) model for strong interaction symmetry and its breaking. Version 2 |  | — |  |
| `SlepianPollak1961` | Slepian–Pollak | Bell Syst. Tech. J. 40 (1961) 43 | Prolate spheroidal wave functions, Fourier analysis and uncertainty -- I | LAMET §7.2 | — (v2.1) |  |
| `LandauWidom1980` | Landau–Widom | J. Math. Anal. Appl. 77 (1980) 469 | Eigenvalue distribution of time and frequency limiting | LAMET §7.2 | — (v2.1) |  |

### 4.6 Frontier keys that are duplicates of an existing entry (use the merged key)

| frontier key | source | merged key | match |
|---|---|---|---|
| `Ji:2020ect` | yzliu | `JiEtAl2021` | arxiv+doi+tk |
| `Ji:2013dva` | yzliu | `Ji2013` | arxiv+doi+tk |
| `Collins:1981uk` | yzliu | `CollinsSoper1981` | doi+tk |
| `Collins:1984kg` | yzliu | `CollinsSoperSterman1985a` | doi+tk |
| `Collins:2004nx` | yzliu | `CollinsMetz2004` | arxiv+doi+tk |
| `Ebert:2018gzl` | yzliu | `EbertStewartZhao2019` | arxiv+doi+tk |
| `Izubuchi:2018srq` | yzliu | `IzubuchiEtAl2018` | arxiv+doi+tk |
| `Ma:2017pxb` | yzliu | `MaQiu2018` | arxiv+doi+tk |
| `Korchemsky:1987wg` | yzliu | `KorchemskyRadyushkin1987` | doi+tk |
| `Frenkel:1984pz` | yzliu | `FrenkelTaylor1984` | doi+tk |
| `Gatheral:1983cz` | yzliu | `Gatheral1983` | doi+tk |
| `Beneke:1998ui` | yzliu | `Beneke1999` | arxiv+doi+tk |
| `Ji:2004wu` | yzliu | `JiMaYuan2005` | arxiv+doi+tk |
| `Collins:1988ig` | yzliu | `CollinsSoperSterman1988` | doi+tk |
| `Collins:2011zzd` | yzliu | `Collins2011` | doi+tk |
| `Kugo:1979gm` | yzliu | `KugoOjima1979` | doi+tk |
| `Becher:2006mr` | lamet | `BecherNeubertPecjak2007` | arxiv+doi+tk |
| `Boussarie:2023izj` | lamet | `BoussarieEtAl2023` | arxiv+tk |
| `Brandt:1981kf` | lamet | `BrandtNeriSato1981` | doi+tk |
| `Chambers:2017dov` | lamet | `ChambersEtAl2017` | arxiv+doi+tk |
| `Collins:1998be` | lamet | `CollinsFreund1999` | arxiv+doi+tk |
| `Curci:1980uw` | lamet | `CurciFurmanskiPetronzio1980` | doi+tk |
| `Detmold:2005gg` | lamet | `DetmoldLin2006` | arxiv+doi+tk |
| `Ebert:2018gzl` | lamet | `EbertStewartZhao2019` | arxiv+doi+tk |
| `Ellis:1978ty` | lamet | `EllisEtAl1979` | doi+tk |
| `Izubuchi:2018srq` | lamet | `IzubuchiEtAl2018` | arxiv+doi+tk |
| `Ji:1998xh` | lamet | `JiOsborne1998` | arxiv+doi+tk |
| `Ji:2013dva` | lamet | `Ji2013` | arxiv+doi+tk |
| `Ji:2020ect` | lamet | `JiEtAl2021` | arxiv+doi+tk |
| `Korchemsky:1987wg` | lamet | `KorchemskyRadyushkin1987` | doi+tk |
| `Ma:2017pxb` | lamet | `MaQiu2018` | arxiv+doi+tk |
| `Polyakov:1980ca` | lamet | `Polyakov1980` | doi+tk |
| `Radyushkin:1997ki` | lamet | `Radyushkin1997` | arxiv+doi+tk |
| `Radyushkin:2017cyf` | lamet | `Radyushkin2017` | arxiv+doi+tk |
| `Sterman:1986aj` | lamet | `Sterman1987` | doi+tk |
| `Wilson:1969zs` | lamet | `Wilson1969` | doi+tk |
| `Xiong:2013bka` | lamet | `XiongEtAl2014` | arxiv+doi+tk |
| `Zimmermann:1972tv` | lamet | `Zimmermann1973` | doi+tk |
| `Gordan:1873` | others | `Gordan1873` | doi |
| `Feige:2014wja` | others | `FeigeSchwartz2014` | arxiv+doi+tk |
| `Eden:1966dnq` | others | `EdenEtAl1966` | tk |
| `Libby:1978bx` | others | `LibbySterman1978b` | doi+tk |
| `Coleman:1965xm` | others | `ColemanNorton1965` | doi+tk |
| `Ma:2019hjq` | others | `Ma2020` | arxiv+doi+tk |
| `Collins:2011zzd` | others | `Collins2023` | doi+tk |
| `Zimmermann:1972tv` | others | `Zimmermann1973` | doi+tk |
| `Beneke:1997zp` | others | `BenekeSmirnov1998` | arxiv+doi+tk |
| `Collins:1984xc` | others | `Collins1984` | tk |
| `Smirnov:2002pj` | others | `Smirnov2002` | tk |
| `Rothstein:2016bsq` | others | `RothsteinStewart2016` | arxiv+doi+tk |
| `Bodwin:1984hc` | others | `Bodwin1985` | tk |
| `Gaunt:2014ska` | others | `Gaunt2014` | arxiv+doi+tk |
| `Catani:2011st` | others | `CataniDeFlorianRodrigo2012` | arxiv+doi+tk |
| `Jantzen:2011nz` | others | `Jantzen2011` | arxiv+doi+tk |
| `Forshaw:2006fk` | others | `ForshawKyrieleisSeymour2006` | arxiv+doi+tk |
| `Forshaw:2012bi` | others | `ForshawSeymourSiodmok2012` | arxiv+doi+tk |
| `Collins:1985ue` | others | `CollinsSoperSterman1985b` | doi+tk |
| `Collins:1988ig` | others | `CollinsSoperSterman1988` | doi+tk |
| `Candido:2020yat` | others | `CandidoForteHekhorn2020` | arxiv+doi+tk |
| `Dixon:1974ss` | others | `DixonTaylor1974` | doi+tk |
| `Collins:2021vke` | others | `CollinsRogersSato2022` | arxiv+doi+tk |
| `Diehl:2011yj` | others | `DiehlOstermeierSchafer2012` | arxiv+doi+tk |
| `Bodwin:1994jh` | others | `BodwinBraatenLepage1995` | arxiv+tk |
| `Nayak:2006fm` | others | `NayakQiuSterman2006` | arxiv+doi+tk |
| `Nayak:2005rw` | others | `NayakQiuSterman2005a` | arxiv+doi+tk |
| `Nayak:2005rt` | others | `NayakQiuSterman2005b` | arxiv+doi+tk |

Frontier keys identical to an existing key (same INSPIRE texkey; nothing to replace): `Almelid:2015jia`, `Ananthanarayan:2018tog`, `Andrasi:1980qw`, `Balitsky:2007feb`, `Banfi:2025mra`, `Becher:2009cu`, `Becher:2015hka`, `Becher:2016mmh`, `Becher:2021zkk`, `Becher:2023mtx`, `Becher:2024kmk`, `Becher:2024nqc`, `Beneke:1994sw`, `Beneke:2018gvs`, `Beneke:2019mua`, `Beneke:2022obx`, `Beneke:2026miy`, `Bigi:1994em`, `Boer:2024hzh`, `Braun:2018brg`, `Buffing:2017mqm`, `Candido:2023ujx`, `Caron-Huot:2015bja`, `Chen:2020ody`, `Collins:1994ee`, `Collins:2008sg`, `Collins:2017oxh`, `Collins:2020euz`, `delRio:2023pse`, `Diehl:2015bca`, `Diehl:2017kgu`, `Diehl:2017wew`, `Diehl:2018wfy`, `Dixon:2019lnw`, `Dominguez:2011wm`, `Dorn:1986dt`, `Dutrieux:2025jed`, `Ebert:2019okf`, `Ebert:2022fmh`, `Fevola:2023kaw`, `Fleming:2012wy`, `Forshaw:2008cq`, `Fredenhagen:1984bz`, `Frob:2015uqy`, `Gardi:2009qi`, `Gardi:2022khw`, `Gardi:2024axt`, `Green:2017xeu`, `Hamberg:1991qt`, `Henneaux:1993jn`, `Holland:2014pna`, `Hollands:2006ag`, `Hollands:2007zg`, `Hollands:2011gf`, `Ishikawa:2017faj`, `Jain:2008gb`, `Ji:2014gla`, `Ji:2014hxa`, `Ji:2017oey`, `Ji:2018hvs`, `Ji:2018waw`, `Ji:2019ewn`, `Ji:2019sxk`, `Ji:2020bby`, `Ji:2020brr`, `Ji:2020jeb`, `Ji:2021znw`, `Ji:2022ezo`, `Ji:2023pba`, `Ji:2024hit`, `Ji:2026vir`, `Joglekar:1975nu`, `Kang:2011mg`, `Kang:2016mcy`, `Kluberg-Stern:1974iel`, `Kluberg-Stern:1974nmx`, `Kluberg-Stern:1975ebk`, `Labastida:1984gy`, `LatticeParton:2020uhz`, `LatticePartonCollaborationLPC:2022myp`, `LatticePartonLPC:2021gpi`, `LatticePartonLPC:2023pdv`, `Li:2016axz`, `Li:2020xml`, `Liu:2019oav`, `Liu:2020wbn`, `Liu:2021evw`, `Liu:2022ajh`, `Liu:2023onm`, `Liu:2023pjb`, `Liu:2024omb`, `Liu:2025bqq`, `Liu:2025edu`, `Ma:2014jla`, `Ma:2023hrt`, `Manohar:2012jr`, `Manohar:2012pe`, `Manohar:2016nzj`, `Manohar:2017eqh`, `Orginos:2017kos`, `Pak:2010pt`, `Radyushkin:2018cvn`, `Rossi:2017muf`, `Rossi:2018zkn`, `Schwartz:2018obd`, `Semenova:2018cwy`, `Smirnov:1990rz`, `Su:2026eta`, `Vladimirov:2017ksc`, `Vladimirov:2020ofp`, `Zeng:2015iba`.

---------------------------------------------------------------------------------------------------

## 5. spec-v2 additions (INSPIRE / Crossref)

Fetched 2026-10-10 by `spec_v2/checks/fetch_additions.py` (one INSPIRE hit per query; the record, the query and the metadata used for the check are in `spec_v2/checks/inspire_additions/`). These are classic or reference works added for Ch2 `qcd`, App M/N/O and the open items of refdoc S60. Their content has **not** been read for this spec: cite them only for their standard attribution (the purpose column) or for content documented elsewhere (frontier reports, refdoc notes); anything more needs `(verify)`. Two queries returned records that were already present (`Andrasi:1980qw` in v1, `Hamberg:1991qt` in others.bib).

| key | readable alias | first author | publication | title | INSPIRE query | purpose |
|---|---|---|---|---|---|---|
| `Andrasi:1980qw` | `AndrasiEtAl1981` | Andrasi, A. | Nucl.Phys.B 182 (1981) 104 | Soft Divergences in Perturbative {QCD} | `j Nucl.Phys.B,182,104` | S60/Ch12: two-loop soft-gluon effects in DY — already in v1 |
| `Baikov:2016tgj` | `BaikovChetyrkinKuhn2017` | Baikov, P.A. | Phys.Rev.Lett. 118 (2017) 082002 | Five-Loop Running of the QCD Coupling Constant | `j Phys.Rev.Lett.,118,082002` | Ch2 qcd: five-loop beta function |
| `Bartels:1995iu` | `BartelsErmolaevRyskin1996a` | Bartels, Jochen | Z.Phys.C 70 (1996) 273 | Nonsinglet contributions to the structure function g1 at small x | `j Z.Phys.C,70,273` | v2.1, Ch24: small-$x$ helicity (CLAIMS E34(iv)); no DOI in INSPIRE or Crossref |
| `Bartels:1996wc` | `BartelsErmolaevRyskin1996b` | Bartels, Jochen | Z.Phys.C 72 (1996) 627 | Flavor singlet contribution to the structure function g1 at small x | `j Z.Phys.C,72,627` | v2.1, Ch24: small-$x$ helicity; intercept quoted in OTHERS §9.5; DOI patched to the Crossref record |
| `Blumlein:1996hb` | `BlumleinVogt1996` | Blümlein, J. | Phys.Lett.B 386 (1996) 350 | The singlet contribution to the structure function g1(x,Q2) at small x | `j Phys.Lett.B,386,350` | v2.1, Ch24: small-$x$ helicity (cited by `Borden:2025ehe`) |
| `Beneke:1998eq` | `BenekeBraunKivel1998` | Beneke, M. | Phys.Lett.B 443 (1998) 308 | The Operator product expansion, nonperturbative couplings and the Landau pole: L | `j Phys.Lett.B,443,308` | S60/Ch21: O(N) sigma model renormalons |
| `Bostelmann:2005rr` | `Bostelmann2005` | Bostelmann, Henning | J.Math.Phys. 46 (2005) 082304 | Operator product expansions as a consequence of phase space properties | `j J.Math.Phys.,46,082304` | S60/App M: OPE from phase-space properties (AQFT) |
| `Brodsky:1997de` | `BrodskyPauliPinsky1998` | Brodsky, Stanley J. | Phys.Rept. 301 (1998) 299 | Quantum chromodynamics and other field theories on the light cone | `j Phys.Rept.,301,299` | S60/App O: light-cone quantization review |
| `Callan:1970yg` | `Callan1970` | Callan, Curtis G., Jr. | Phys.Rev.D 2 (1970) 1541 | Broken scale invariance in scalar field theory | `j Phys.Rev.D,2,1541` | Ch2 qcd: Callan-Symanzik equation |
| `Chang:1973qi` | `ChangYan1973` | Chang, Shau-Jin | Phys.Rev.D 7 (1973) 1147 | Quantum field theories in the infinite momentum frame. 2. Scattering matrices of | `j Phys.Rev.D,7,1147` | S60/App O: Feynman rules at infinite momentum |
| `Chay:2003ju` | `ChayKim2004` | Chay, Junegone | Nucl.Phys.B 680 (2004) 302 | Nonleptonic B decays into two light mesons in soft collinear effective theory | `j Nucl.Phys.B,680,302` | S60/Ch20: B->pi pi in SCET |
| `Cheng:1969eh` | `ChengWu1969` | Cheng, Hung | Phys.Rev.Lett. 22 (1969) 666 | High-energy elastic scattering in quantum electrodynamics | `j Phys.Rev.Lett.,22,666` | S60/App O: eikonal high-energy scattering in QED |
| `Chetyrkin:1982zq` | `ChetyrkinGorishnyTkachov1982` | Chetyrkin, K.G. | Phys.Lett.B 119 (1982) 407 | OPERATOR PRODUCT EXPANSION IN THE MINIMAL SUBTRACTION SCHEME | `j Phys.Lett.B,119,407` | S19/App M: OPE in minimal subtraction |
| `Collins:2018aqt` | `Collins2018LF` | Collins, John | arXiv:1801.03960 | The non-triviality of the vacuum in light-front quantization: An elementary trea | `eprint 1801.03960` | S60/App O: light-front vacuum |
| `Collins:2016hqq` | `CollinsGambergEtAl2016` | Collins, J. | Phys.Rev.D 94 (2016) 034014 | Relating Transverse Momentum Dependent and Collinear Factorization Theorems in a | `j Phys.Rev.D,94,034014` | S60/Ch14: W+Y matching |
| `Czakon:2004bu` | `Czakon2005` | Czakon, M. | Nucl.Phys.B 710 (2005) 485 | The Four-loop QCD beta-function and anomalous dimensions | `j Nucl.Phys.B,710,485` | Ch2 qcd: four-loop beta function (check) |
| `David:1982qv` | `David1982` | David, F. | Nucl.Phys.B 209 (1982) 433 | Nonperturbative Effects and Infrared Renormalons Within the 1/$N$ Expansion of t | `j Nucl.Phys.B,209,433` | S60/Ch21: sigma-model IR renormalons |
| `Faddeev:1967fc` | `FaddeevPopov1967` | Faddeev, L.D. | Phys.Lett.B 25 (1967) 29 | Feynman Diagrams for the Yang-Mills Field | `j Phys.Lett.B,25,29` | Ch2 qcd: gauge fixing, ghosts |
| `Feldman:1986ax` | `FeldmanEtAl1986` | Feldman, J. | Commun.Math.Phys. 103 (1986) 67 | A Renormalizable Field Theory: The Massive {Gross-Neveu} Model in Two-dimensions | `j Commun.Math.Phys.,103,67` | S60/Ch21: massive Gross-Neveu model constructed |
| `Fritzsch:1973pi` | `FritzschGellMannLeutwyler1973` | Fritzsch, H. | Phys.Lett.B 47 (1973) 365 | Advantages of the Color Octet Gluon Picture | `j Phys.Lett.B,47,365` | Ch2 qcd: colour octet gluon picture |
| `Gawedzki:1985ez` | `GawedzkiKupiainen1985` | Gawedzki, K. | Commun.Math.Phys. 102 (1985) 1 | GROSS-NEVEU MODEL THROUGH CONVERGENT PERTURBATION EXPANSIONS | `j Commun.Math.Phys.,102,1` | S60/Ch21: Gross-Neveu model constructed |
| `Gell-Mann:1964ewy` | `GellMann1964` | Gell-Mann, Murray | Phys.Lett. 8 (1964) 214 | A Schematic Model of Baryons and Mesons | `j Phys.Lett.,8,214` | Ch2 qcd: quark model |
| `Gell-Mann:1954yli` | `GellMannLow1954` | Gell-Mann, Murray | Phys.Rev. 95 (1954) 1300 | Quantum electrodynamics at small distances | `j Phys.Rev.,95,1300` | Ch2 qcd: renormalization group |
| `Greenberg:1964pe` | `Greenberg1964` | Greenberg, O.W. | Phys.Rev.Lett. 13 (1964) 598 | Spin and Unitary Spin Independence in a Paraquark Model of Baryons and Mesons | `j Phys.Rev.Lett.,13,598` | Ch2 qcd: parastatistics / colour |
| `Haag:1958vt` | `Haag1958` | Haag, R. | Phys.Rev. 112 (1958) 669 | Quantum field theories with composite particles and asymptotic conditions | `j Phys.Rev.,112,669` | App M: Haag-Ruelle scattering |
| `Hamberg:1991qt` | `HambergVanNeerven1992` | Hamberg, R. | Nucl.Phys.B 379 (1992) 143 | The Correct renormalization of the gluon operator in a covariant gauge | `j Nucl.Phys.B,379,143` | S60/App M: gluon operator renormalization in covariant gauge — already in others.bib |
| `Han:1965pf` | `HanNambu1965` | Han, M.Y. | Phys.Rev. 139 (1965) B1006 | Three Triplet Model with Double SU(3) Symmetry | `j Phys.Rev.,139,B1006` | Ch2 qcd: colour |
| `Herzog:2017ohr` | `HerzogEtAl2017` | Herzog, F. | JHEP 02 (2017) 090 | The five-loop beta function of Yang-Mills theory with fermions | `j JHEP,1702,090` | Ch2 qcd: five-loop beta function, general gauge group |
| `Itzykson:1980rh` | `ItzyksonZuber1980` | Itzykson, C. |  | Quantum Field Theory | `texkey Itzykson:1980rh` | Ch2 qcd: textbook |
| `Jost:1965yxu` | `Jost1965` | Jost, Res | Lectures Appl.Math. 4 (1965) 1 | The general theory of quantized fields | `t general theory of quantized fields and a Jost` | App M: axiomatic QFT textbook |
| `Kogut:1969xa` | `KogutSoper1970` | Kogut, John B. | Phys.Rev.D 1 (1970) 2901 | Quantum Electrodynamics in the Infinite Momentum Frame | `j Phys.Rev.D,1,2901` | S60/App O: light-front QED |
| `Korchemskaya:1994qp` | `KorchemskayaKorchemsky1995` | Korchemskaya, I.A. | Nucl.Phys.B 437 (1995) 127 | High-energy scattering in QCD and cross singularities of Wilson loops | `j Nucl.Phys.B,437,127` | S60/App O: Wilson-loop cross singularities, Regge |
| `Korchemsky:1993hr` | `Korchemsky1994` | Korchemsky, Gregory P. | Phys.Lett.B 325 (1994) 459 | On Near forward high-energy scattering in QCD | `j Phys.Lett.B,325,459` | S60/App O: near-forward high-energy scattering |
| `Larin:1993tp` | `LarinVermaseren1993` | Larin, S.A. | Phys.Lett.B 303 (1993) 334 | The Three loop QCD Beta function and anomalous dimensions | `j Phys.Lett.B,303,334` | Ch2 qcd: three-loop beta function (check) |
| `Ligterink:1994tm` | `LigterinkBakker1995` | Ligterink, N.E. | Phys.Rev.D 52 (1995) 5954 | Equivalence of light front and covariant field theory | `j Phys.Rev.D,52,5954` | S60/App O: equivalence of light-front and covariant PT |
| `Nielsen:1980sx` | `Nielsen1981` | Nielsen, N.K. | Am.J.Phys. 49 (1981) 1171 | ASYMPTOTIC FREEDOM AS A SPIN EFFECT | `j Am.J.Phys.,49,1171` | Ch2 qcd: asymptotic freedom as a spin effect (pedagogical) |
| `Novikov:1984ac` | `NovikovEtAl1984` | Novikov, V.A. | Phys.Rept. 116 (1984) 103 | Two-Dimensional Sigma Models: Modeling Nonperturbative Effects of Quantum Chromo | `j Phys.Rept.,116,103` | S60/Ch21: two-dimensional sigma models |
| `ParticleDataGroup:2024cfk` | `PDG2024` | Navas, S. | Phys.Rev.D 110 (2024) 030001 | Review of particle physics | `j Phys.Rev.D,110,030001` | Ch2 qcd: alpha_s(M_Z) world average |
| `Symanzik:1970rt` | `Symanzik1970` | Symanzik, K. | Commun.Math.Phys. 18 (1970) 227 | Small distance behavior in field theory and power counting | `j Commun.Math.Phys.,18,227` | Ch2 qcd: Callan-Symanzik equation |
| `Tarasov:1980au` | `TarasovVladimirovZharkov1980` | Tarasov, O.V. | Phys.Lett.B 93 (1980) 429 | The Gell-Mann-Low Function of QCD in the Three Loop Approximation | `j Phys.Lett.B,93,429` | Ch2 qcd: three-loop beta function |
| `Wilson:1974sk` | `Wilson1974` | Wilson, Kenneth G. | Phys.Rev.D 10 (1974) 2445 | Confinement of Quarks | `j Phys.Rev.D,10,2445` | Ch2/Ch22: lattice gauge theory |
| `Yang:1954ek` | `YangMills1954` | Yang, Chen-Ning | Phys.Rev. 96 (1954) 191 | Conservation of Isotopic Spin and Isotopic Gauge Invariance | `j Phys.Rev.,96,191` | Ch2 qcd: Yang-Mills gauge theory |
| `vanRitbergen:1997va` | `vanRitbergenVermaserenLarin1997` | van Ritbergen, T. | Phys.Lett.B 400 (1997) 379 | The Four loop beta function in quantum chromodynamics | `j Phys.Lett.B,400,379` | Ch2 qcd: four-loop beta function |
| `Zweig:1964jf` | `Zweig1964` | Zweig, G. | CERN-TH-412 (1964), DOI 10.17181/CERN-TH-412 | An SU(3) model for strong interaction symmetry and its breaking. Version 2 | `texkey Zweig:1964jf` | Ch2 qcd: quark (aces) model (re-typed as @techreport; reprint in Lichtenberg–Rosen, Vol. 1, pp. 22–101) |
| `Epstein1960` | — | Epstein, H. | J. Math. Phys. 1 (1960) 524–531, DOI 10.1063/1.1703688 (Crossref) | Generalization of the "Edge-of-the-Wedge" Theorem | Crossref DOI | App M §M.8: edge-of-the-wedge step of `prop:dis-dispersion-np` |
| `Markoff1916` | — | Markoff, W. | Math. Ann. 77 (1916) 213–258, DOI 10.1007/BF01456902 (Crossref; also lists J. Grossmann) | Über Polynome, die in einem gegebenen Intervalle möglichst wenig von Null abweichen | Crossref DOI | App K `lem:appK-markov` (V. A. Markov coefficient inequality) |
| `SlepianPollak1961` | — | Slepian, D.; Pollak, H. O. | Bell Syst. Tech. J. 40 (1961) 43–63, DOI 10.1002/j.1538-7305.1961.tb03976.x (Crossref) | Prolate spheroidal wave functions, Fourier analysis and uncertainty – I | Crossref DOI | v2.1, Ch22 Fourier step (VF-LAM-17) |
| `LandauWidom1980` | — | Landau, H. J.; Widom, H. | J. Math. Anal. Appl. 77 (1980) 469–481, DOI 10.1016/0022-247X(80)90241-3 (Crossref) | Eigenvalue distribution of time and frequency limiting | Crossref DOI | v2.1, Ch22 Fourier step (VF-LAM-17, eigenvalue count) |

Not found in INSPIRE (cite through textbooks instead): D. Ruelle, Helv. Phys. Acta 35 (1962) 147 (Haag–Ruelle theory: use `Haag:1958vt`, `Jost:1965yxu`, `Streater:1989vi`); V. S. Vladimirov's monographs: the Mir 1979 edition is on neither INSPIRE nor Crossref; the Crossref-verified CRC 2002 monograph `Vladimirov2002` is in the bib since v2.3 (cite it with 「位置待核实」 until the location is checked).

### 5.1 spec-v2.3 additions (verify patch; INSPIRE / Crossref) — 48 entries

Fetched 2026-10-11 by `spec_v2/checks/fetch_additions_v23.py` (one INSPIRE hit per query; records and JSON in `spec_v2/checks/inspire_additions/`, log `fetch_additions_v23.log`) and three Crossref-verified manual entries; PART 10 of `refs_merged_v2.bib`, built by `checks/add_refs_v23.py`. Content depth: as documented in the verification records that cite them (`verify/claims/`, `verify/extend_reports/`); a key whose content was not read there is cited for its standard attribution only. **Not added** (verification failed): Bałaban, CMP 116 (1988) 1 (0 INSPIRE hits; not cited); Vladimirov, Mir 1979 (see above); Feichtner–Sturmfels, Port. Math. 62 (2005) 437 (math/0411260; 0 hits on INSPIRE and Crossref — the citing sentence of `lem:appM-matroid` cites `Schultka:2018nrs` §4 instead). Joglekar 1977 = the existing keys `Joglekar:1976eb`, `Joglekar:1976pe` (INSPIRE re-check).

| key | first author | publication | title | INSPIRE query | purpose | cited in (FINAL_OUTLINE_v2, v2.3) |
|---|---|---|---|---|---|---|
| `Gribov:1977wm` | Gribov, V.N. | Nucl.Phys.B 139 (1978) 1 | Quantization of Nonabelian Gauge Theories | `j Nucl.Phys.B,139,1` | Ch2 qcd: Gribov copies | §0, Ch2 |
| `Lee:1972fj` | Lee, B.W. et al. | Phys.Rev.D 5 (1972) 3121 | Spontaneously Broken Gauge Symmetries Part 1: Preliminaries | `j Phys.Rev.D,5,3121` | Ch2 qcd: renormalizability, Lee-Zinn-Justin I | §0, Ch2 |
| `Lee:1972ocr` | Lee, B.W. et al. | Phys.Rev.D 5 (1972) 3137 | Spontaneously Broken Gauge Symmetries Part 2: Perturbation Theory and Renormalization | `j Phys.Rev.D,5,3137` | Ch2 qcd: renormalizability, Lee-Zinn-Justin II | §0, Ch2 |
| `Lee:1972yfa` | Lee, B.W. et al. | Phys.Rev.D 5 (1972) 3155 | Spontaneously Broken Gauge Symmetries Part 3: Equivalence | `j Phys.Rev.D,5,3155` | Ch2 qcd: renormalizability, Lee-Zinn-Justin III | §0, Ch2 |
| `Zinn-Justin:1974ggz` | Zinn-Justin, Jean | Lect.Notes Phys. 37 (1975) 1 | Renormalization of Gauge Theories | `j Lect.Notes Phys.,37,1` | Ch2 qcd: Zinn-Justin equation | §0, Ch2 |
| `Appelquist:1974tg` | Appelquist, Thomas et al. | Phys.Rev.D 11 (1975) 2856 | Infrared Singularities and Massive Fields | `j Phys.Rev.D,11,2856` | Ch2 qcd: decoupling | §0, Ch2 |
| `Bergere:1977wz` | Bergere, M.C. et al. | Commun.Math.Phys. 62 (1978) 137 | A Theorem on Asymptotic Expansion of Feynman Amplitudes | `j Commun.Math.Phys.,62,137` | App M, App N: asymptotic expansion of Feynman amplitudes | App M, App N |
| `Balaban:1985yy` | Balaban, Tadeusz | Commun.Math.Phys. 109 (1987) 249 | Renormalization Group Approach to Lattice Gauge Fields Theories. 1. Generation of Effective Actions in a Small Fields Approximation and a Coupling Constant Renormalization in Four-dimensions | `j Commun.Math.Phys.,109,249` | App M: UV stability of lattice YM (RG approach I) | App M |
| `Balaban:1989ay` | Balaban, T. | Commun.Math.Phys. 122 (1989) 355 | Large Field Renormalization. 2: Localization, Exponentiation, and Bounds for the R Operation | `j Commun.Math.Phys.,122,355` | App M: UV stability of lattice YM (large field renormalization II) | App M |
| `Magnen:1992wv` | Magnen, Jacques et al. | Commun.Math.Phys. 155 (1993) 325 | Construction of Y M(4) with an infrared cutoff | `j Commun.Math.Phys.,155,325` | App M: YM4 with an infrared cutoff | App M |
| `Schoonderwoerd:1998qj` | Schoonderwoerd, N.C.J. et al. | Phys.Rev.D 57 (1998) 4965 | Equivalence of renormalized covariant and light front perturbation theory. 1. Longitudinal divergences in the Yukawa model | `j Phys.Rev.D,57,4965` | App O / ASSUMPTIONS asm:appO-lcopt: covariant vs light-front PT I | 08 Label |
| `Schoonderwoerd:1998iy` | Schoonderwoerd, N.C.J. et al. | Phys.Rev.D 58 (1998) 025013 | Equivalence of renormalized covariant and light front perturbation theory. 2. Transverse divergences in the Yukawa model | `j Phys.Rev.D,58,025013` | App O / ASSUMPTIONS asm:appO-lcopt: covariant vs light-front PT II | 08 Label |
| `Chou:2022drv` | Chou, Chien-Yu et al. | Phys.Rev.D 106 (2022) 014507 | One-loop hybrid renormalization matching kernels for quasiparton distributions | `j Phys.Rev.D,106,014507` | App Q E01: first published correction of the hybrid kernel | Ch22, F5. Cross, App Q, CHANGELOG |
| `Becher:2026kbr` | Becher, Thomas et al. | Phys.Rev.Lett. 137 (2026) 121902 | Factorization beyond Coherence | `eprint 2603.12383` | Ch18 front: qg->q coherence violation confirmed in SCET | Ch16, Ch24, F5. Cross, Ch25 |
| `Nakanishi:1990qm` | Nakanishi, N. et al. | World Sci.Lect.Notes Phys. 27 (1990) 1 | Covariant operator formalism of gauge theories and quantum gravity | `j World Sci.Lect.Notes Phys.,27` | Ch24 front: Nakanishi-Ojima, World Sci. Lect. Notes Phys. 27 (1990) | Ch24, F5. Cross |
| `Meggiolaro:1996hf` | Meggiolaro, Enrico | Z.Phys.C 76 (1997) 523 | The High-energy quark quark scattering: From Minkowskian to Euclidean theory | `eprint hep-th/9602104` | N01 / App O: eikonal amplitudes at O(g^4) | §0, Ch12, App L, App O, 09 Master |
| `Giordano:2006vv` | Giordano, Matteo et al. | Phys.Rev.D 74 (2006) 016003 | Analyticity and crossing symmetry of the eikonal amplitudes in gauge theories | `eprint hep-ph/0602143` | N01 / App O: eikonal amplitudes, colour structure | §0, Ch12, App L, App O |
| `Cheng:2024wyu` | Cheng, Chen et al. | Phys.Rev.Lett. 134 (2025) 251902 | Lattice-QCD Computable Quark Correlation Functions at Three-Loop Order and Extraction of Splitting Functions | `eprint 2410.05141` | A06: N3LO quasi-PDF matching kernel | §0, Ch22, Ch25 |
| `Radyushkin:2018nbf` | Radyushkin, A.V. | Phys.Lett.B 788 (2019) 380 | Structure of parton quasi-distributions and their moments | `j Phys.Lett.B,788,380` | A06: reply to Rossi-Testa | Ch22 |
| `Lindsay:1983ny` | Lindsay, W.W. | Nucl.Phys.B 231 (1984) 397 | Spectator Interactions in the {Drell-Yan} Process: Meson + Meson $\to$ Lepton Pair + Anything | `j Nucl.Phys.B,231,397` | App O: two-loop spectator calculation | App O |
| `Belitsky:2025bez` | Belitsky, A.V. et al. | Phys.Rev.D 113 (2026) 036022 | Off-shell form factor: Factorization is violated | `eprint 2505.22595` | App N: off-shell form factor, factorization violated | App N |
| `Belitsky:2024yag` | Belitsky, A.V. et al. | JHEP 05 (2025) 237 | Pinching Sudakov | `eprint 2409.05945` | App N: Pinching Sudakov | App N |
| `Jackiw:1980kv` | Jackiw, R. et al. | Phys.Rev.D 23 (1981) 2291 | How Superrenormalizable Interactions Cure their Infrared Divergences | `j Phys.Rev.D,23,2291` | App N: IR of super-renormalizable theories (phi^3_6 regulator remark) | App N |
| `Borinsky:2020rqs` | Borinsky, Michael | Ann.Inst.H.Poincare D Comb.Phys.Interact. 10 (2023) 635 | Tropical Monte Carlo quadrature for Feynman integrals | `eprint 2008.12310` | App M/N: tropical Monte Carlo, Newton polytopes | App M, App N |
| `Schultka:2018nrs` | Schultka, Konrad | arXiv:1806.01086 (preprint) | Toric geometry and regularization of Feynman integrals | `eprint 1806.01086` | App M: Newton polytopes of Feynman integrals | App M |
| `Larin:1996wd` | Larin, S.A. et al. | Nucl.Phys.B 492 (1997) 338 | The Three loop QCD calculation of the moments of deep inelastic structure functions | `j Nucl.Phys.B,492,338` | App M: forward expansion check | App M |
| `Braun:2019qtp` | Braun, V.M. et al. | JHEP 02 (2019) 191 | Two-loop evolution equations for flavor-singlet light-ray operators | `eprint 1901.06172` | N04: light-ray operators as generating functions (prior art) | Ch2, Ch8, Ch9, Ch24, Ch25, App F, App J, 09 Master |
| `Barcaro:2026dsd` | Barcaro, Damiano et al. | arXiv:2607.14259 (preprint) | Collinear Factorization Violation and Reggeization | `eprint 2607.14259` | App O: Glauber literature comparison | App O |
| `Zhou:2017his` | Zhou, Gao-Liang et al. | arXiv:1708.01743 (preprint) | Glauber Gluon Effects in Soft Collinear Factorization | `eprint 1708.01743` | App O: all-order argument literature | App O |
| `Liu:2008cc` | Liu, F. et al. | arXiv:0802.2973 (preprint) | Glauber Gluons in Soft Collinear Effective Theory and Factorization of Drell-Yan Processes | `eprint 0802.2973` | App O: all-order argument literature | App O |
| `Scimemi:2016ffw` | Scimemi, Ignazio et al. | JHEP 03 (2017) 002 | Power corrections and renormalons in Transverse Momentum Distributions | `eprint 1609.06047` | S63-7: small-b power corrections b^2 | §0, Ch14, 09 Master |
| `Moos:2020wvd` | Moos, Valentin et al. | JHEP 12 (2020) 145 | Calculation of transverse momentum dependent distributions beyond the leading power | `eprint 2008.01744` | S63-7: small-b power corrections b^2 | §0, Ch14, 09 Master |
| `Arkani-Hamed:2022cqe` | Arkani-Hamed, Nima et al. | Phys.Rev.D 105 (2022) 125013 | Feynman polytopes and the tropical geometry of UV and IR divergences | `eprint 2202.12296` | App N: tropical geometry of divergences | App M, App N |
| `Henneaux:1995ex` | Henneaux, Marc | Phys.Lett.B 367 (1996) 163 | On the gauge fixed BRST cohomology | `j Phys.Lett.B,367,163` | App M lem:appM-lbc-formal: local BRST cohomology (X3 K6, checked) | App M |
| `Barnich:1999cy` | Barnich, Glenn et al. | Phys.Lett.B 492 (2000) 376 | Cohomological analysis of gauged fixed gauge theories | `j Phys.Lett.B,492,376` | App M lem:appM-lbc-formal: local BRST cohomology (X3 K6, checked) | App M |
| `Herrlich:1994kh` | Herrlich, Stefan et al. | Nucl.Phys.B 455 (1995) 39 | Evanescent operators, scheme dependences and double insertions | `j Nucl.Phys.B,455,39` | App M lem:appM-ne(iii): evanescent operators (X3 K12, abstract) | App M |
| `Chang:2013pba` | Chang, Chun-peng et al. | Phys.Lett.B 726 (2013) 262 | Glauber gluons in pion-induced Drell-Yan processes | `eprint 1305.4694` | App O rem:appO-literature-comparison: dissenting Glauber-phase proposal (X1 sec. 11) | App O |
| `Li:2022fvk` | Li, Hsiang-nan | Phys.Rev.D 106 (2022) 014029 | Glauber gluons in pion-induced Drell-Yan processes revisited | `eprint 2201.10901` | App O rem:appO-literature-comparison: dissenting Glauber-phase proposal (X1 sec. 11) | App O |
| `Boer:2017hqr` | Boer, Daniël et al. | SciPost Phys. 3 (2017) 040 | Colour unwound - disentangling colours for azimuthal asymmetries in Drell-Yan scattering | `eprint 1709.04935` | App O rem:appO-literature-comparison: double Boer-Mulders model check (X1 sec. 11) | App O |
| `Lindsay:1983dt` | Lindsay, W.W. et al. | Nucl.Phys.B 222 (1983) 189 | Factorization and the {Drell-Yan} Process | `j Nucl.Phys.B,222,189` | App O lem:appO-halfcoinc-colour: colour-singlet-target mechanism (Lindsay-Ross-Sachrajda) | App O |
| `Aybat:2011ge` | Aybat, S.Mert et al. | Phys.Rev.D 85 (2012) 034043 | The QCD Evolution of the Sivers Function | `j Phys.Rev.D,85,034043` | App Q E17: the factor-free zeta normalization used by the same authors (claim E17 literature check) | Ch14, App Q |
| `Bhattacharya:2019cme` | Bhattacharya, Shohini et al. | Phys.Rev.D 102 (2020) 054021 | Exploring twist-2 GPDs through quasidistributions in a diquark spectator model | `eprint 1903.05721` | Ch22 prop:lamet-tmc: P^z-independence of the first two gamma^0 moments (claim N07 literature check) | Ch22 |
| `Monahan:2026skv` | Monahan, Christopher et al. | arXiv:2609.40205 (preprint) | Unpolarized quasi- and pseudo-distributions at one loop: gluon correlator decomposition, matching, and the region $\vert x\vert >1$ | `eprint 2609.40205` | Ch22 lem:lamet-strip, prop:lamet-slepian: classical results applied to quasi-PDFs (claim N10 literature check) | Ch22 |
| `Buffing:2011mj` | Buffing, M.G.A. et al. | JHEP 07 (2011) 065 | Gauge links for transverse momentum dependent correlators at tree-level | `eprint 1105.4804` | Ch18 prop:break-colour: attachment rule in Wilson-line form (claim N18 literature check) | Ch18 |
| `Balitsky:2009xg` | Balitsky, Ian et al. | Nucl.Phys.B 822 (2009) 45 | NLO evolution of color dipoles in N=4 SYM | `eprint 0903.5326` | Ch24 prop:front-nlo-bk: the zeta(3) mismatch withdrawn by its authors (claim E34(iii) literature check) | Ch24 |
| `Hormander2003` | Hörmander, L. | Springer, Classics in Mathematics (2003; reprint of the 2nd ed. 1990), DOI 10.1007/978-3-642-61497-2 (Crossref) | The Analysis of Linear Partial Differential Operators I | Crossref DOI | App M §M.8 (`lem:appM-green`), Ch22 (`prop:lamet-support`: Paley–Wiener–Schwartz, Thm. 7.3.1) | Ch22, App M |
| `Vladimirov2002` | Vladimirov, V. S. | CRC Press (2002), DOI 10.1201/9781482288162 (Crossref) | Methods of the Theory of Generalized Functions | Crossref DOI | App M §M.8 (Laplace transforms in tubes); the Mir 1979 edition named in the drafts could not be verified, the location in the 2002 edition is still to be checked (「位置待核实」) | §0, App M |
| `NilssonPassare2013` | Nilsson, L.; Passare, M. | J. Geom. Anal. 23 (2013) 24–46, DOI 10.1007/s12220-011-9235-7 (Crossref) | Mellin Transforms of Multivariate Rational Functions | Crossref DOI | App M §M.7 (novelty check of `thm:appM-forward-expansion`; open problem) | App M |


---------------------------------------------------------------------------------------------------

## 6. CHANGELOG

**2026-10-10 — v2 drafted (spec-v2 writer-spec/figures/bibliography drafter).**
1. `refs_merged_v2.bib` built by `spec_v2/checks/build_refs_v2.py`: v1 (646, verbatim) + yzliu (57 new) + lamet (109 new) + others (145 new) + 38 INSPIRE additions + 3 manual entries = **998** entries; 186 frontier duplicates and 2 duplicate additions mapped as aliases; corrections of §1.2 applied; arXiv-only records converted to `@misc`.
2. `key_aliases_v2.tsv`: 1067 rows (v1 rows verbatim + frontier duplicates + identity rows of new entries + readable aliases of the additions).
3. Tests: BibTeX `unsrt` with `\nocite{*}` 0 errors / 0 warnings; XeLaTeX with the common preamble 0 errors, 0 missing glyphs, 0 overfull boxes (`checks/bibtest/`).
4. Binding warnings extended for the frontier sources (§1.2–§1.4); per-unit citation lists for Ch2, Ch22–Ch24, App M/N/O/Q (§3); per-key depth tables for all new entries (§4); notes on the spec-v2 additions (§5).
5. `verify/` bibliographies: none at build time; the build script merges them automatically when they appear (§0).

**2026-10-10 (later) — spec v2.1 (resumed writer-spec/figures/bibliography drafter).**
1. Bibliography rebuilt with `spec_v2/checks/build_refs_v2.py`: **1003** entries (+3 INSPIRE: `Bartels:1995iu`, `Bartels:1996wc`, `Blumlein:1996hb`, fetched by the new `checks/fetch_additions_v21.py`; +2 Crossref manual entries: `SlepianPollak1961`, `LandauWidom1980`); 1075 alias rows (+5 identity rows, +3 readable aliases). `verify/` has no bibliography; the one reference CLAIMS.md marks "to be added" (Bartels–Ermolaev–Ryskin, E34) is now in the bib, and all 215 key-like references of CLAIMS.md resolve.
2. Printed-note hygiene: internal provenance remarks removed from the `note` fields of `Gardi:2024axt`, `Shifman2000` (v1 text; together with the eight v1 titles and five v1 month fields of item 5, the only changes to v1 text), `LatticeParton:2020uhz` and `Markoff1916`; DOI and typographic patches of the three new INSPIRE entries (§0 rule 6, §1.2).
3. Tests re-run: BibTeX `unsrt` with `\nocite{*}`: 1003 entries, exit 0, 0 warnings, 0 errors; XeLaTeX: 0 errors, 0 missing glyphs, 0 overfull boxes, 59 pp. (`checks/bibtest/`); the merge was re-audited independently (no duplicate keys, no DOI or arXiv collisions, every v1 and frontier key resolves).
4. New §1.5: binding attribution rules keyed to `verify/CLAIMS.md` A01–A28; §3.5 App Q source table keyed to E01–E36 with the classes Q1/Q2/Q3 of WRITER_SPEC_v2 §6.13; new keys added to the citation lists of Ch22 (§3.2) and Ch24 (§3.4) and to §4.4, §4.5, §5.
5. Title and month normalization: 11 legacy all-caps titles replaced by the published titles (Crossref; rule 6); the 29 numeric `month` fields (all arXiv-type records except `Sterman:1995fz`, `Hannesdottir:2022bmo`) are written as BibTeX month macros, so that `unsrt` prints "July 2020" instead of "7 2020" (rule 6); BibTeX/XeLaTeX tests re-run with the same results.

**2026-10-11 — spec v2.3 (spec patcher; verify patch).**
1. Bibliography: PART 10 with **48** verified additions (45 INSPIRE, 3 Crossref) → **1051** entries; `key_aliases_v2.tsv` +48 identity rows. Not added: Bałaban CMP 116 (1988) 1, Vladimirov (Mir 1979), Feichtner–Sturmfels (citing text changed). Test: BibTeX `unsrt` with `\nocite{*}`: 1051 entries, exit 0, 0 warnings, 0 errors; XeLaTeX with the common preamble: 0 errors, 0 missing glyphs, 0 overfull boxes, 61 pp. (`checks/bibtest/SUMMARY.txt`).
2. §1.4: CS-exponent, hybrid-kernel and one-jettiness warnings updated with the verification outcomes; §1.5: verdicts recorded (A04, A06, A11 corrected in single items; A20 wording per R-M20; A03, A07, A16, A17, A23 precisions).
3. §3.5: App M/N/O lists extended by the v2.3 keys; App Q table with the outcome column. §5.1: the v2.3 additions with query, purpose and the units that cite them.
