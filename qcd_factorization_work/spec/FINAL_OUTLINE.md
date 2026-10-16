# FINAL_OUTLINE — 《QCD 因子化定理：严格证明、全阶论证与适用边界》

**Status:** binding chapter-by-chapter specification for the writers (spec synthesizer, 2026-10-10).
**Inputs synthesized:** `CONTEXT.md`; `research/architect/BLUEPRINT.md` (statement plans, §0.4 conventions, supplements S1–S9); `research/critic/REVIEW.md` (TOC v1 §5, over-claims O1–O21, circularities C1–C15, missing topics §4, backbone statements §8, conventions D1–D12); `research/survey/SURVEY.md` (status verdicts, items 1–30, verified quotations); `research/refs/NOTES.md`; derivations `research/c_{dis,pdf,dy,ee,regions,wilson,exclusive,scet,glauber}/DERIVATION.md` (c_glauber: §1–§2 written, §3–§4 pending — logs used); figures `research/tikz1/figures1.tex` (final), `research/tikz2`, `research/tikz3` (being redone — labels only). **Audit update (later on 2026-10-10):** `research/c_tmd/DERIVATION.md` (14:07; 17/17 scripts pass) and c_glauber §3–§4 (13:33) are now written. The TMD, diffraction and space-like entries below and in VERIFIED_FORMULAS were upgraded accordingly (see CHANGELOG at the end). The frontier research notes (`frontier/lamet`, `frontier/yzliu`, `frontier/others`, 14:14–14:21) and the reference-document notes (`refdoc/notes`) were **not** inputs of this outline: see §0.9.
**Companion files (same directory):** `WRITER_SPEC.md` (binding rules, notation table, compile procedure), `FIGURES_INDEX.md`, `VERIFIED_FORMULAS.md` (copy formulas only from there), `refs_merged.bib` + `REFS_NOTES.md` + `key_aliases.tsv`.

---------------------------------------------------------------------------------------------------

## 0. Global decisions (summary; details in WRITER_SPEC.md)

### 0.1 Structure (lead-author decision D1 = critic TOC v1)

22 chapters in 6 parts (`\part{...}`), appendices A–L after `\appendix`. The architect's statement plans are mapped onto this structure; the critic's ordering principles are kept: (i) every tool first appears in its simplest setting (Sudakov form factor before the general method); (ii) the rigorous core ($e^+e^-$, DIS/OPE, operator definitions) precedes the all-order graphical proofs; (iii) SCET precedes jets/NGLs and the breakdown chapter; (iv) each process class has a home.

| Part | `\part` title | Chapters |
|---|---|---|
| I | 基础 (Foundations) | 1 `intro`, 2 `prelim`, 3 `ir`, 4 `sudakov` |
| II | 严格核心：OPE 可及的量 (The rigorous core) | 5 `ee`, 6 `dis`, 7 `pdf` |
| III | 共线因子化的全阶论证 (Collinear factorization to all orders) | 8 `method`, 9 `disall`, 10 `coll`, 11 `dy`, 12 `thr` |
| IV | 超越共线因子化 (Beyond collinear factorization) | 13 `tmd`, 14 `scet`, 15 `jets`, 16 `smallx`, 17 `break` |
| V | 其他硬过程 (Other hard processes) | 18 `excl`, 19 `heavy` |
| VI | 极限与展望 (Limits) | 20 `power`, 21 `lattice`, 22 `summary` |
| 附录 | — | A `appA` … L `appL` |

### 0.2 Page budget (decision D2; A4, 11 pt, `common/preamble_fact.tex`)

Body ≈ 300 pp = front matter 5 + chapters 260 + appendices 35. Reference list (~10 pp) and TOC are not counted.

| # | key | file | 中文标题 | pp | format |
|---|---|---|---|---|---|
| — | front | `front.tex` | 摘要、阅读指南、严格性标签、记号与约定 | 5 | (written by the Ch1 writer) |
| 1 | intro | `ch01_intro.tex` | 引言：部分子图像、因子化的含义与严格性分级 | 12 | full |
| 2 | prelim | `ch02_prelim.tex` | 预备知识 | 14 | full |
| 3 | ir | `ch03_ir.tex` | 费曼积分的红外结构：钳夹、幂次计数与红外安全 | 14 | full |
| 4 | sudakov | `ch04_sudakov.tex` | Sudakov 形状因子与振幅的红外结构 | 12 | full |
| 5 | ee | `ch05_ee.tex` | 严格核心 I：$e^+e^-$ 湮灭总截面 | 12 | full |
| 6 | dis | `ch06_dis.tex` | 严格核心 II：深度非弹散射与算符乘积展开 | 14 | full |
| 7 | pdf | `ch07_pdf.tex` | 严格核心 III：部分子分布与碎裂函数的算符定义 | 14 | full |
| 8 | method | `ch08_method.tex` | 全阶因子化证明的一般方法 | 16 | full |
| 9 | disall | `ch09_disall.tex` | DIS 的全阶动量空间证明、重夸克与核靶 | 12 | full |
| 10 | coll | `ch10_coll.tex` | 其他共线过程：单举湮灭、SIDIS、光生、极化与横度 | 12 | full |
| 11 | dy | `ch11_dy.tex` | Drell–Yan 过程与强子—强子碰撞 | 14 | full |
| 12 | thr | `ch12_thr.tex` | 阈值重求和与重新因子化 | 8 | short |
| 13 | tmd | `ch13_tmd.tex` | 横动量依赖（TMD）因子化 | 14 | full |
| 14 | scet | `ch14_scet.tex` | 有效场论方法：SCET | 12 | full |
| 15 | jets | `ch15_jets.tex` | 喷注、事件形状、非全局对数与超领头对数 | 9 | short |
| 16 | smallx | `ch16_smallx.tex` | 小 $x$ 与高能因子化 | 8 | short |
| 17 | break | `ch17_break.tex` | 因子化的破坏与非标准情形 | 12 | full |
| 18 | excl | `ch18_excl.tex` | 硬遍举过程 | 10 | short |
| 19 | heavy | `ch19_heavy.tex` | 重夸克物理：$B$ 介子衰变与重夸克偶素 | 9 | short |
| 20 | power | `ch20_power.tex` | 幂次修正、次领头幂次、重整化子与非微扰地位 | 12 | full |
| 21 | lattice | `ch21_lattice.tex` | 格点 QCD 与因子化 | 8 | short |
| 22 | summary | `ch22_summary.tex` | 总结：主表与开放问题 | 12 | full |
| A | appA | `appA_lightfront.tex` | 光锥坐标、$\gamma$ 矩阵恒等式、加号分布与 Mellin 变换 | 3 | |
| B | appB | `appB_wilson.tex` | Wilson 线：Feynman 规则与程函恒等式 | 4 | |
| C | appC | `appC_dimreg.tex` | 维数正规化积分与相空间 | 3 | |
| D | appD | `appD_landau.tex` | Landau 方程与 Coleman–Norton 定理的证明 | 4 | |
| E | appE | `appE_powercount.tex` | 幂次计数公式的推导 | 3 | |
| F | appF | `appF_ward.tex` | 图形 Ward 恒等式 | 3 | |
| G | appG | `appG_oneloop.tex` | 单圈与两圈计算细节 | 4 | |
| H | appH | `appH_literature.tex` | 文献导读 | 2 | |
| I | appI | `appI_gamma5.tex` | 维数正规化中的 $\gamma_5$ | 2 | |
| J | appJ | `appJ_brst.tex` | BRST 对称性与割图中的鬼场 | 2 | |
| K | appK | `appK_moments.tex` | 矩问题与解析延拓引理 | 3 | |
| L | appL | `appL_lightray.tex` | 光线算符与定域算符：矩关系的全阶证明 | 2 | |
| | | | **total body** | **300** | |

"short" chapters (D2): every main result in the form **precise statement + status (tag, MA, evidence) + proof idea (`proofsketch`) + one worked example**.

### 0.3 Rigor tags, qualifiers, meta-assumptions (decision D3)

* Tags `\tagR \tagA \tagP \tagC \tagV` in the theorem-environment title: `\begin{theorem}[DIS 矩的因子化 \tagR]`.
* Every `\tagR` statement opens with **one** qualifier, verbatim:
  - **R_PT** — 「（$R_{\mathrm{PT}}$：在重整化微扰论中对红外正规化的部分子态严格。）」 statements about Feynman graphs / partonic Green functions at every order;
  - **R_def** — 「（$R_{\mathrm{def}}$：由算符定义直接推出。）」 algebraic consequences of operator/field definitions and symmetries;
  - **OPE** — 「（以 OPE 为前提：在 QCD 中，含夸克的 OPE 被普遍假定成立，严格证明只对标量理论与纯 Yang–Mills 规范不变算符给出，见\cref{thm:dis-ope}。）」 (short form after first use in a chapter: 「（以 OPE 为前提。）」).
* Pure mathematics (moment problems, Carlson, Gordan, plus-distribution and eikonal identities as identities of rational functions, Mellin algebra) carries **no tag** and is proved completely or cited as a classical theorem.
* Meta-assumptions MA0–MA4 (critic §3.1) are defined once in `def:intro-MA`. Every statement about hadrons ends its hypotheses with 「非微扰地位：MA…（\cref{def:intro-MA}）。」 Every `[A]`, `[P]`, `[C]`, `[V]` statement is followed (inside or right after the environment) by a 「地位与缺口」 paragraph naming the weakest step and the literature location (e.g. "Collins 2011 §14.4.8").
* Where the survey or the critic is more conservative than the blueprint, the conservative tag is used (list in §0.6).

### 0.4 Labels (decision D7)

Chapter keys: `intro prelim ir sudakov ee dis pdf method disall coll dy thr tmd scet jets smallx break excl heavy power lattice summary`; appendices `appA … appL`. Chapter label `ch:<key>`, appendix label `app:<key>` (e.g. `app:appK`), sections `sec:<key>-<name>`, equations `eq:<key>-<name>`, figures `fig:<name>` (existing names from FIGURES_INDEX) or `fig:<key>-<name>` (new), tables `tab:<key>-<name>`. Statements: `def: thm: lem: prop: cor: conj: ex: rem:` + `<key>-<name>`. **The labels listed in this outline are canonical; writers may add internal labels but must not rename canonical ones.**

### 0.5 Critical paths (to be drawn as `fig:intro-dependency`)

* Rigorous core I ($e^+e^-$): `thm:prelim-cutting-rules`, `prop:prelim-optical` → `prop:ee-analytic`, `lem:ee-single-scale`, `thm:ee-euclid-ir` → `thm:ee-R-finite` → `cor:ee-R-alphas`.
* Rigorous core II (DIS): `prop:dis-compton-analytic` → `prop:dis-dispersion`; `lem:dis-tree-ope` + `thm:prelim-composite-renorm` → `thm:dis-ope` [A] → `thm:dis-moments` [R, OPE] → (`thm:pdf-moments-local` ⟵ `thm:pdf-support-pt`, `lem:pdf-wilson-moments`, App K, App L) → `thm:pdf-dglap`, `thm:pdf-dis-xspace` [R, OPE].
* All-order graphical: `thm:ir-landau-momentum` → `prop:ir-coleman-norton` → `prop:ir-pinch-classification` → `prop:ir-power-counting` → `thm:ir-leading-regions`; (`thm:prelim-slavnov-taylor` → `prop:method-ward-one` → `lem:method-ward-multi` → `prop:method-collinear-wilson`, `prop:method-soft-wilson`); (`lem:method-collinear-accuracy`, `lem:method-soft-accuracy` → `thm:method-subtraction`); (`lem:method-soft-unitarity`, `prop:method-fsi`, `prop:method-glauber-deformation`) → **`thm:method-template`** → {`thm:disall-factorization`, `thm:coll-sia`, `thm:coll-sidis`, `thm:dy-factorization`, `thm:tmd-factorization`}. Sudakov form factor (`thm:sudakov-factorization`) is the worked prototype of the same machine.
* The three weakest links that fix the `[A]` tags (cite them in every process chapter's status paragraph): `lem:method-ward-multi` (non-abelian multi-gluon Ward identity with ghosts; Collins 2011 §11.3.2 assumes the BRST classification of non-local operators), `thm:method-subtraction` (general subtraction theorem; complete only for the Sudakov form factor, Collins 2011 ch. 10), `prop:method-glauber-deformation`/`lem:dy-fsi` (Glauber region; Collins 2011 §14.4.8 "Issues remaining").

### 0.6 Tag corrections relative to the blueprint (binding)

| statement (blueprint No.) | blueprint | **final** | reason |
|---|---|---|---|
| OPE in renormalized PT for QCD (T5.9) | [R] | **[A]** (`thm:dis-ope`); [R] for $\varphi^4$ and pure-YM gauge-invariant operators | survey item 1 |
| moment factorization (T5.12), x-space twist-2 DIS (T6.14), twist-4 structure, TMC, Bjorken sum rule | [R] in PT | **[R] with qualifier "以 OPE 为前提"** | D3, survey items 1–2 |
| Landau equations, momentum form | [R] | **[R] for necessity** (Gordan); sufficiency + global deformation **[A]** (`rem:ir-landau-status`) | survey item 4, c_regions §1.9 |
| Coleman–Norton | [R] | algebraic equivalence **[R]**; "trapped ⇔ classical process" **[A]** | c_regions |
| power counting (P3.9) | [R] | superficial degree **[R]**; bound on actual contributions **[A]** | c_regions §2.4 |
| cutting rules in massless DR; $R$ = sum over partonic cuts | [R] | massive/regulated graphs **[R]**; massless DR identification **[A]** (`cor:ee-cuts`) | c_ee §5 |
| PDF support for hadrons (T6.7) | [R] given SPEC | PT **[R]** (`thm:pdf-support-pt`); hadrons **[A]** (`prop:pdf-support-hadron`) | survey item 7 |
| number-density interpretation (P6.5) | [R] | **heuristic remark, no tag** (`rem:pdf-number-density`) | critic O8 |
| Euclidean OPE with condensates (T4.13) | [R] | coefficients **[A]**; non-perturbative OPE **[C]** | survey items 1, 22 |
| PQW smearing (P4.15) | [A] | identity **[R, R_def]**; "$\bar R=\bar R_{\rm PT}+O(\Lambda^4/\Delta^2)$" and local duality **[C]** | critic O3, c_ee |
| $pp\to$ jets/hadrons, heavy-quark pairs (P10.14) | [A] weaker | **[C]** (`conj:dy-coloured-final`) | survey item 9, critic O14 |
| hadron–hadron DY beyond $1/Q^2$ | — | **[V]** (`prop:dy-twist6-failure`) | survey item 8 |
| $B\to\pi\pi$ (P14.12) | [P] | LP formula **[P]** (`prop:heavy-qcdf-lp`); subleading power standard factorization **[V]** (`prop:heavy-qcdf-endpoint`) | survey item 18, critic O19, c_scet |
| renormalons, large-$\beta_0$ (P16.6) | [R] in limit | **[P]** (`prop:power-adler-large-beta0`); IR renormalon ↔ higher twist in general **[C]** | critic O20 |
| transverse-photon meson production (P13.10) | [V]/[C] | **[V]** (`prop:excl-meson-T`) | critic O18, c_exclusive |
| Sivers sign change (T11.14) | [R given defs] | **[R, R_def]** for operator-defined functions; observable sign reversal **[A]** | critic O15, survey item 11 |
| dipole formula as exact all-order statement | — | **[V]** (`prop:sudakov-dipole-violation`) | survey item 30 |
| KLN (T3.13) | [A] | **[A]** (kept; forward-scattering caveat) | survey item 3 |
| method of regions | [P] | Euclidean **[R]** (`thm:ir-regions-euclid`), Minkowskian **[P]** (`prop:ir-regions-minkowski`) | survey item 23 |

### 0.7 How each chapter entry below is organised

For every chapter: **title (中文 / English)**, label, file, page budget; **purpose**; **depends on**; **sections** (with content bullets); **canonical statements** — each with type, canonical label, Chinese title, tag (+ qualifier and MA where applicable), a precise statement in formulas, and a **proof plan** (full / sketch, steps, literature location; "VF-…" refers to an entry of `VERIFIED_FORMULAS.md`); **worked examples**; **figures** (existing labels and new ones, see FIGURES_INDEX); **misconception box** items (critic §7 numbering "M#"); **key citation keys** (all in `refs_merged.bib`). Pure-math lemmas are marked "(数学，无标签)".

### 0.8 Dependency order, composite tags, proofs of [A] deductions (audit rules; binding)

* **Reading order is dependency order.** A proof plan, a `\uses{}` list or a "Depends on" line of chapter $k$ may use only labels of chapters $\le k$ and of the appendices. A label of a later chapter may appear only as a forward pointer (「其一般形式见第~N~章」), never as a proof step and never in `\uses{}`. The audit removed every forward dependency it found (CHANGELOG items 3–9). Chapter 1 and the front matter are overviews and may point forward freely.
* **Composite statements.** Some entries give two tags for parts of one statement (e.g. `prop:sudakov-kg` "[A]; one-loop content [R, R_PT]", `prop:heavy-quarkonium-fragmentation` "[A] … [C]"). The environment title carries the **first** tag listed (the one in the registry); the other part is stated as a separate item with its status in words (WRITER_SPEC §4.11).
* **[A] statements that are deductions.** For `thm:method-template` and for the process theorems deduced from it (`thm:disall-factorization`, `thm:dy-factorization`, `thm:tmd-factorization`) the deduction from the stated hypotheses/propositions is written out in full, but inside a `proofsketch` (WRITER_SPEC §4.7): the [A] comes from the weakest ingredient, which the 「地位与缺口」 paragraph names.
* **[P] statements with a complete restricted proof** (`prop:dy-abelian-model`, `prop:power-adler-large-beta0`, `prop:power-thooft-model`): the restriction (model, limit, order) is part of the first sentence of the statement; the restricted claim gets a full `proof`; the [P] records that the general (QCD) claim is established only in that setting (WRITER_SPEC §4.7).
* **Meta-assumption lines.** The audit added the missing 「非微扰地位」 lines to hadron-level statements (marked "(MA: audit)"). A statement without an MA line is about partonic states, operators or models only.

### 0.9 Open structural items for the lead author (from `REQUIREMENTS.md`; not covered by decisions D1–D8)

These items do not change any statement of Chapters 2–20 or of the appendices; they affect the front matter, Ch1 (overview table), Ch21 and Ch22.

1. **Frontier chapters (REQUIREMENTS.md 3b).** The user requires 「因子化的前沿进展，包含 Yizhuang Liu 的相关严格因子化研究，Xiangdong Ji 的 LaMET 因子化证明，一切都做到详尽严格完整」. The research is complete:
   - `frontier/lamet/LAMET.md` (LaMET principle and grades; renormalization of space-like Wilson-line operators; the matching theorem with explicit hypotheses and three proof architectures: IJJSZ OPE route, Ma–Qiu collinear subtraction, lattice cross sections; one-loop results; power corrections);
   - `frontier/yzliu/YZLIU.md` (73 INSPIRE items; theorem-level results A1–A6, B1–B6, C1–C6, D1–D5, E1–E2; §6.1 proposes an 11-section chapter with draft LaTeX statements);
   - `frontier/others/OTHERS.md` (Collins 2020 Landau theorem; rigorous OPE results; method of regions incl. hidden regions; Glauber EFT and factorization restoration; NLP endpoint factorization; positivity; BRST non-local gap; small $x$; DPS; quarkonium; QED/EW).

   Their bibliographies (`frontier/yzliu/yzliu.bib`, 82 entries; `frontier/others/others.bib`, 238 entries) are **not** merged into `refs_merged.bib` (one entry, `Gardi:2024axt`, was added by the audit). The present outline covers LaMET only inside Ch21 (8 pp, short format) and Yizhuang Liu's work not at all. **Proposal (requires a decision, since it changes D1/D2):** add Part VII 「前沿进展」 with Ch23 `lamet` (LaMET 的因子化定理), Ch24 `yzliu` (刘一壮等：TMD 软函数的欧氏化、时序无关性与准 TMD 因子化), Ch25 `frontier` (其他严格进展), about 12+12+12 pp; reduce Ch21 to lattice basics with forward pointers, or merge it into Ch23; add the corresponding rows to `tab:intro-overview`/`tab:summary-master`; merge the two frontier bib files after deduplication.
2. **Formal blueprint (REQUIREMENTS.md 3d).** 「自动生成的形式化蓝图附录（依赖图与状态表）」 is not yet specified. **Proposal:** App M `appM_blueprint.tex`, generated by the lead author at integration time from the `\uses{}` data and the environment tags (no writer); Ch22 points to it. The `\uses{}` rule of §0.8 makes all cross-chapter edges point backwards, so the generated graph can be drawn in reading order (cycles inside one chapter, if any, are reported by the generator).
3. **Reference document (REQUIREMENTS.md 2).** `refdoc/notes/R1.md`–`R8.md` exist, and `refdoc/REFDOC_ANALYSIS.md` appeared at 15:02 during this audit. That file looks unfinished: its §5.5 stops inside S28 although it refers to items up to S56. The audit adopted only the verified corrections of its §2.4 "errors in our material" that fit the current structure (OUR-1 fragmentation-function prefactor; OUR-2 subtraction conditions; OUR-3 hadronic moment caveat; OUR-4 two-component Glauber deformation; OUR-5 small-$b$ remainder; OUR-6 forward amplitude vs discontinuity; OUR-7 `Shifman2000` booktitle; OUR-8 exceptional forward momenta). Its structural proposals — new appendices M (OPE, 24 pp), N (Collins subtraction, 24 pp), O (Glauber/LCPT, 32 pp), P (blueprint, 8 pp), a fourth $[R]$ qualifier $R_{\rm cond}$, an `asm:` assumption register, an error-type vocabulary and many new Ch1–Ch9 statements — change D1–D3 and the 300-pp budget and need the lead author's decision. The items to adopt (numbered-assumption conditional theorems — already the style of `thm:method-template` (H1)–(H5); its OPE-proof appendix; its precise Collins subtraction; its LCPT treatment of the Glauber cancellation, cf. `Diehl:2015bca` §4 cited in `lem:dy-fsi`) should be checked against the final analysis.
4. **Grades in frontier/others more optimistic than the binding verdicts.** OPE for QCD with quarks "[R] in PT as a combination of classical results" (OTHERS §2.7) and the Collins 2020 Landau theorem "[R]† (preprint)" (§1.7). **Not adopted** (D3: the conservative survey/critic verdicts bind); listed for the lead author.

Until items 1–2 are decided, the front matter, Ch1, Ch21 and Ch22 should not be finalized. All other units can be written now.

---------------------------------------------------------------------------------------------------

# 第一部分 基础 (Part I — Foundations)

---------------------------------------------------------------------------------------------------

## Front matter — `front.tex` (5 pp; written by the Ch1 writer)

* **摘要** (1 p): what the book proves, at which level; the R/A/P/C/V landscape in one paragraph.
* **阅读指南与严格性标签** (1 p): the five tags, the three `[R]` qualifiers, MA0–MA4 in one line each (full definitions in `def:intro-tags`, `def:intro-MA`), reading paths (Part II only = rigorous core; Parts I+III = collinear proofs; Part IV–VI = boundaries).
* **记号与约定** (3 pp): the notation table of `WRITER_SPEC.md` §3, typeset as `tab:front-notation` (longtable not available: split into 3 `table` floats or use `tabularx` blocks inside `\begin{center}`; no new packages).

---------------------------------------------------------------------------------------------------

## Chapter 1 — 引言：部分子图像、因子化的含义与严格性分级 / Introduction: the parton picture, what factorization asserts, and levels of rigour

`\label{ch:intro}` · `ch01_intro.tex` · **12 pp** · full

**Purpose.** (i) Physical picture (time dilation, incoherence, hard–collinear–soft); (ii) precise definition of a factorization statement and of "proof" (asymptotic expansion in $m/Q$ at each fixed order of $\alpha_s$; formal power series; hadrons vs partons — critic O1); (iii) rigour taxonomy: five tags, the two sub-kinds of [R] plus the "以 OPE 为前提" qualifier, meta-assumptions MA0–MA4 (critic §3.1, Chinese draft text in critic §12); (iv) taxonomy of kinds of factorization (critic W6); (v) overview table of all main results with status, kept identical to Ch22's master table; (vi) misconception box; (vii) organisation and critical paths (`fig:intro-dependency`).

**Depends on.** Nothing (forward references only, to canonical labels).

**Sections.**
1. `sec:intro-parton` 部分子模型与物理图像 — Feynman/Bjorken picture; infinite-momentum frame; ratio of time scales $\Delta x^+_{\rm probe}/\Delta x^+_{\rm hadron}\sim m^2/Q^2$; incoherent sum of squares; what each heuristic step becomes later (leading regions ↔ incoherence, light-front operators ↔ frozen ensemble, subtracted partonic cross sections ↔ quasi-free partons). Tree handbag (`ex:intro-handbag`).
2. `sec:intro-statement` 因子化定理的一般形式 — `def:intro-hard-process`, `def:intro-factorization`; one-hadron (DIS), zero-hadron ($e^+e^-$), two-hadron (DY) versions; preview of TMD, threshold, exclusive, NRQCD, SCET-type statements (formula shapes only).
3. `sec:intro-proof` "证明"意味着什么 — two expansions (in $\alpha_s$ and in $m/Q$); "all orders" = every fixed order (formal power series), never convergence; asymptotic nature (renormalons); partonic external states with IR regulators vs hadrons; what is lost in the passage to hadrons (MA1, MA2); C1–C3 circularities to avoid (critic §3.2): PDFs defined by operators first, DGLAP from renormalization before scale independence, no "proof" from the number-density picture.
4. `sec:intro-tags` 严格性分级与元假设 — `def:intro-tags`, `def:intro-MA`; how status lines are printed; example status lines.
5. `sec:intro-kinds` 因子化的种类 — `tab:intro-kinds` with columns 名称 | 尺度 | 低能函数 | 演化变量 | 典型证明技术 | 地位 | 本书章节, rows: collinear (DIS/DY), TMD, threshold, high-energy ($k_T$), exclusive (DA/GPD), heavy-quark (NRQCD/HQE/QCDF), SCET matching, lattice (LaMET/SDF).
6. `sec:intro-overview` 结论总览 — `tab:intro-overview` (68 rows, list in FINAL_OUTLINE §08 "Master-table rows": result | short formula | tag (+qualifier) | MA | chapter/label; may be typeset compactly). Must coincide with `tab:summary-master` (Ch22) in rows and tags.
7. `sec:intro-misconceptions` 常见误解 — `tcolorbox` with 12 items (below), each with the correction and a forward reference.
8. `sec:intro-organisation` 本书结构与阅读路线 — parts; the three tracks (rigorous core / all-order graphical / boundaries); critical paths (§0.5 of this outline); `fig:intro-dependency`.

**Canonical statements.**

* **定义 `def:intro-hard-process` — 硬过程与幂次展开** (no tag). An observable $\sigma(Q;m)$ with hard scale $Q$ and infrared scales $m$ (hadron and parton masses, $\Lambda$, IR regulators) admits a *leading-power expansion* if $\sigma=\sigma_{\rm LP}+r$, $r=O((m/Q)^p)$, $p>0$; define "leading power", "power correction", "twist" (twist = dimension − spin; forward reference `def:dis-twist`). Remark: in massless PT the only infrared scales are regulators; $\Lambda$ enters through $\alpha_s(\mu)$.

* **定义 `def:intro-factorization` — 共线因子化陈述** (no tag). Blueprint Definition 0 verbatim in substance:
  $$\sigma(Q;m)=\sum_{i,j}\int_{x_a}^1\frac{d\xi_a}{\xi_a}\int_{x_b}^1\frac{d\xi_b}{\xi_b}\,H_{ij}\Big(\frac{x_a}{\xi_a},\frac{x_b}{\xi_b},\frac{Q}{\mu},\alpha_s(\mu)\Big)f_{i/A}(\xi_a;\mu)f_{j/B}(\xi_b;\mu)+r(Q;m),$$
  with (a) $f$ = matrix elements of specified gauge-invariant renormalized operators (`def:pdf-quark`, `def:pdf-gluon`); (b) $H_{ij}$ independent of the external states and of the IR regularization, computable order by order; (c) $r=O((m/Q)^p)$, understood order by order in $\alpha_s$ for partonic states (PT) and as an asymptotic statement for hadrons under MA1–MA2 (and MA4). One-hadron version: $F_2/x=\sum_iC_{2,i}\otimes f_i+r$; zero-hadron version: $e^+e^-$ total cross section (no PDFs; IR finiteness).

* **定义 `def:intro-tags` — 严格性标签** (no tag). The five tags of CONTEXT.md verbatim; the rule "a tag refers to the statement exactly as formulated"; the three qualifiers of `[R]` (R_PT, R_def, 以 OPE 为前提) with their meaning (critic O2, §12; D3). Add: "凡涉及强子的陈述，最多只能达到'$R_{\rm PT}$ + 元假设'的地位" (critic §12).

* **定义 `def:intro-MA` — 元假设 MA0–MA4** (no tag). Text of critic §12 (Chinese, ready): MA0 存在性 (QCD exists as a 4D QFT; hadron states; matrix elements of renormalized light-ray operators exist at least as distributions; the existence of 4D Yang–Mills is a Clay problem); MA1 区域完备性; MA2 幂次计数的传递; MA3 解析性与高能行为; MA4 渐近性. Each item ≤ 3 lines; then one sentence: "本书每个涉及强子的定理在前提中列出它用到的元假设。"

* **注 `rem:intro-incoherence` — 部分子模型的非相干性论证（启发式）** (no tag; blueprint H1.5). Time-dilation estimate; incoherence; explicitly marked heuristic; list of later precise counterparts.

* **例 `ex:intro-handbag` — 树图手提包与 Callan–Gross 关系.** With $W^{\mu\nu}$ normalized as in VF-CONV-13: leading-twist projection of the quark correlator $\Phi\to\frac14\gamma^-{\rm Tr}[\gamma^+\Phi]$ (Fierz, VF-EXC-13 for the general decomposition), on-shell condition $\delta((\xi P+q)^2)$ fixes $\xi=x$, giving $F_2=\sum_qe_q^2x(q+\bar q)$, $F_1=\frac12\sum_qe_q^2(q+\bar q)$, $F_L=0$. Proof: full (1 p). Check: free quark $F_2=e_q^2\delta(1-x)$ (VF-DIS-1). Remark that $F_L=0$ is a parton-model/LO statement ($F_L=O(\alpha_s)$, `prop:disall-nlo`; M26).

**Tables.** `tab:intro-kinds`; `tab:intro-overview`. The latter and Ch22's `tab:summary-master` use the same row list, in §08 "Master-table rows" of this outline.

**Misconception box (12 items; forward refs).** M28 ([R] ≠ proven for real-world QCD) → `def:intro-tags`; M1 (factorization proven for all processes) → `tab:intro-overview`, Ch17; M2 (MS-bar PDFs are probabilities) → `conj:pdf-positivity`; M3 (factorization = OPE) → Ch6/Ch11; M4 (moments ⇒ uniform x-space error) → `rem:dis-nonuniform`; M7 (Glauber always cancels) → Ch11, Ch17; M8 (KLN explains hadron-collider finiteness) → `prop:ir-bn-failure`; M9 (IR safety ⇒ factorization) → Ch15; M10 (power corrections always $\Lambda^2/Q^2$) → Ch20; M15 (soft factor always 1) → `lem:method-soft-unitarity`, Ch13; M18 (SCET independent of regions) → `rem:scet-assumptions`; M24 (DR partonic PDF is "nothing") → `prop:pdf-partonic-dr`.

**Figures.** existing: `fig:parton-model`, `fig:handbag`, `fig:factorization-schematic` (all `research/tikz1/figures1.tex`); new: `fig:intro-dependency` (dependency graph of the main results coloured by tag).

**Key citation keys.** `Feynman1969`, `Bjorken1969`, `BjorkenPaschos1969`, `DrellYan1970`, `CollinsSoperSterman1989`, `CollinsSoper1987`, `Collins2011`, `Sterman1993`, `StermanEtAl1995`, `CollinsSoper1982a`, `CandidoForteHekhorn2020`, `CollinsRogersSato2022`, `DoriaFrenkelTaylor1980`, `DiLietoEtAl1981`, `CollinsQiu2007`, `RogersMulders2010`, `CataniDeFlorianRodrigo2012`, `Beneke1999`, `Hollands:2011gf`, `tHooft1974`, `IzubuchiEtAl2018`.

---------------------------------------------------------------------------------------------------

## Chapter 2 — 预备知识 / Preliminaries

`\label{ch:prelim}` · `ch02_prelim.tex` · **14 pp** · full (long proofs in App A, B, I, J, K)

**Purpose.** Collect every tool used later, with conventions fixed once (WRITER_SPEC §3): QCD and Feynman rules; BRST and Slavnov–Taylor identities (needed for non-abelian Ward identities, Ch8, App F/J); light-front coordinates and boosts (power counting, Ch3, App E); Wilson lines and their momentum-space rules (Ch4, 7, 8, 11, 13; App B); DR, MS-bar, RG, the $\gamma_5$ scheme (App I) and renormalization of gauge-invariant composite operators (Joglekar–Lee; Ch6, 7, App L); distributions on $[0,1]$ and Mellin transforms (App A, K); cut diagrams, cutting rules, optical theorem for current correlators.

**Depends on.** none.

**Sections.**
1. `sec:prelim-qcd` QCD、规范固定与 Feynman 规则 — Lagrangian, gauge transformations, Feynman-rule table (`fig:prelim-feynman-rules`), light-cone gauge mentioned only as heuristic (Collins 2011 §12.6: proofs in Feynman gauge).
2. `sec:prelim-brst` BRST 对称性与 Slavnov–Taylor 恒等式 — definitions, nilpotency, ST identity in the form used for factorization; physical unitarity (ghost cuts); proofs in App J.
3. `sec:prelim-lightfront` 光锥坐标、Sudakov 分解与 Lorentz 推动 — $n_A,n_B$; boost scaling of components and of good/bad spinor components.
4. `sec:prelim-wilson` Wilson 线 — definition, ODE, covariance, composition/retracing, adjoint lines; momentum-space rules (universal rule); eikonal identity; external partons ↔ semi-infinite lines; light-like lines have cusp/rapidity divergences (forward refs Ch4, Ch13).
5. `sec:prelim-renorm` 维数正规化、重整化与重整化群 — MS-bar ($S_\varepsilon$ convention and the Collins-convention warning), $\beta$ function, RG improvement, $\gamma_5$ (HVBM + Larin), composite operators (Joglekar–Lee).
6. `sec:prelim-distributions` $[0,1]$ 上的分布与 Mellin 变换 — plus distributions (whole-function and product conventions, $\mathcal D_k$), expansion lemma, Mellin transform, convolution theorem, harmonic sums.
7. `sec:prelim-cuts` 割图、幺正性与光学定理 — cut diagrams; cutting rules; $R=12\pi\,{\rm Im}\,\Pi$; $W^{\mu\nu}=\frac1{2\pi}{\rm Im}\,T^{\mu\nu}$.

**Canonical statements.**

* **定义 `def:prelim-qcd` — QCD 拉氏量与规范变换** (no tag). VF-CONV-2: $\mathcal L=-\frac14G^a_{\mu\nu}G^{a\mu\nu}+\sum_q\bar\psi_q(i\slashed D-m_q)\psi_q-\frac1{2\xi}(\partial\cdot A^a)^2+\bar c^a(-\partial^\mu D^{ac}_\mu)c^c$, $D_\mu=\partial_\mu-igA^a_\mu t^a$, $(D_\mu X)^a=\partial_\mu X^a+gf^{abc}A^b_\mu X^c$; $\psi\to U\psi$, $A_\mu\to UA_\mu U^{-1}-\frac ig(\partial_\mu U)U^{-1}$.
* **定义 `def:prelim-feynman-rules` — Feynman 规则** (no tag; table + `fig:prelim-feynman-rules`). VF-CONV-3 (quark, gluon in covariant gauge, ghost propagators; $ig\gamma^\mu t^a$; three-gluon $gf^{abc}[g^{\mu\nu}(k-p)^\rho+g^{\nu\rho}(p-q)^\mu+g^{\rho\mu}(q-k)^\nu]$, all momenta incoming; ghost vertex $-gf^{abc}p^\mu$, $p$ the outgoing-ghost momentum; four-gluon). State that these coincide with Peskin–Schroeder ch. 16 and were checked by c_pdf (plane waves) and c_wilson (Ward identities fail with the opposite sign; $q\bar q\to gg$ cross section).
* **定义 `def:prelim-brst` — BRST 变换** (no tag). $sA^a_\mu=D^{ab}_\mu c^b$, $s\psi=igc^at^a\psi$, $sc^a=-\frac g2f^{abc}c^bc^c$, $s\bar c^a=B^a$, $sB^a=0$ (signs to be re-derived by the writer against PS §16.4; c_wilson §5.6 warns).
* **引理 `lem:prelim-brst-nilpotent` — $s^2=0$ 与拉氏量的 BRST 不变性** [R, R_def]. $s^2=0$ on all fields; $s\mathcal L$ = total derivative. Proof: full in App J (Jacobi identity), 0.5 p.
* **定理 `thm:prelim-slavnov-taylor` — Slavnov–Taylor 恒等式（因子化所用形式）** [R, R_PT]. In renormalized PT with DR (BRST preserved; no $\gamma_5$ in the vector sector) and LSZ-amputated on-shell physical external particles $\Phi$ at non-exceptional momenta: $\langle0|T\,\partial\cdot A^{a_1}(x_1)\cdots\partial\cdot A^{a_N}(x_N)\,\Phi|0\rangle=0$ ($N\ge1$, $\Phi\ne1$), and the one-longitudinal-gluon identity with ghost terms (c_wilson §5.6, VF-WL-9). Proof: sketch (BRST-invariant vacuum, $\partial\cdot A^a=-\xi s\bar c^a$, $s\Phi$ has no single-particle pole); App J. Literature: `tHooft1971`, `Taylor1971`, `Slavnov1972`, `BecchiRouetStora1975`, `BecchiRouetStora1976`, `Tyutin1975`, `KugoOjima1979`. Status remark: the *identity* is [R]; its use to convert arbitrarily many non-abelian K-gluons into Wilson lines is [A] (`lem:method-ward-multi`).
* **命题 `prop:prelim-unitarity` — 物理幺正性与鬼场割线** [R, R_PT]. The sum over all cuts of Feynman-gauge graphs including ghost cuts equals the sum over physical (transverse-gluon, quark) final states; one-loop example $q\bar q\to gg$: $\sum_{\rm phys}|\mathcal A|^2=\sum_{-g,-g}|\mathcal A|^2-2\sum|\mathcal A_{\rm gh}|^2$, cross section $\frac1{36}\sum_{\rm phys}|\mathcal A|^2=g^4[\frac{32}{27}\frac{t^2+u^2}{tu}-\frac83\frac{t^2+u^2}{s^2}]$ (VF-WL-9). Proof: sketch (Kugo–Ojima quartets; 't Hooft–Veltman combinatorics), example full. Literature: `KugoOjima1979`, `tHooftVeltman1972b`, `CombridgeKripfganzRanft1977`.
* **定义 `def:prelim-lightfront` — 光锥坐标与 Sudakov 分解** (no tag). VF-CONV-1; $n_A=(1^+,0^-,\mathbf 0_T)$ with $n_A\cdot v=v^-$, $n_B=(0^+,1^-,\mathbf 0_T)$ with $n_B\cdot v=v^+$ ($n_B$ = Collins' $w_2$); $k=\alpha p_A+\beta p_B+k_T$.
* **引理 `lem:prelim-boost` — 推动下的标度** [R, R_def]. Boost along $z$ with rapidity $\eta$: $v^\pm\to e^{\pm\eta}v^\pm$, $v_T\to v_T$; good/bad spinor components $P_\pm\psi$, $P_+=\frac12\gamma^-\gamma^+$, $P_-=\frac12\gamma^+\gamma^-$, scale as $e^{\pm\eta/2}$. Proof: full (generator $\gamma^0\gamma^3$).
* **定义 `def:prelim-wilson` — Wilson 线** (no tag). VF-CONV-9: $W[b,a]=P\exp(ig\int_a^bdz^\mu A^a_\mu t^a)$, later points left; semi-infinite lines $W[\infty n,y]$, $W[y,-\infty n]$, … ($n$ future pointing); adjoint line $W^{(A)}_{ab}[b,a]=2{\rm Tr}[t^aW[b,a]t^bW[a,b]]$; Fourier convention $A(x)=\int\frac{d^4k}{(2\pi)^4}e^{-ik\cdot x}\tilde A(k)$ ($k$ flows *into* the line); adiabatic regulator.
* **命题 `prop:prelim-wilson-covariance` — Wilson 线的规范协变性** [R, R_def]. $\frac{d}{ds}W(s)=ig\,\dot z\cdot A(z(s))W(s)$; $W[b,a]\to U(b)W[b,a]U^\dagger(a)$ (the reversed ordering is not covariant); $W[c,b]W[b,a]=W[c,a]$, $W[b,a]W[a,b]=1$. Proof: full (ODE uniqueness), App B; numerical SU(2)/SU(3) checks cited as remark (c_pdf s1, c_wilson s1(E)).
* **命题 `prop:prelim-wilson-rules` — 半无限直 Wilson 线的动量空间 Feynman 规则** [R, R_def]. VF-WL-1 (c_wilson §2.5 universal rule): vertex $igt^av^\mu$, eikonal propagator $i/(v\cdot\ell+i0)$ with $\ell$ along the orientation, colour in path order, $\ell=0$ on the segment reaching infinity; equivalently past-pointing $W[0,-\infty n]$: $\prod_j\frac{i}{n\cdot(k_1+\dots+k_j)+i0}$, future-pointing $W[\infty n,0]$: $\prod_j\frac{-i}{n\cdot(k_j+\dots+k_m)-i0}$; conjugate lines: complex conjugates (vertex $-igt^an^\mu$). Proof: full in App B (iterated integrals + induction). Figure `fig:prelim-wilson-rules`.
* **引理 `lem:prelim-eikonal-identity` — 程函恒等式** (数学，无标签). $\sum_{\pi\in S_m}\prod_{j=1}^m[a_{\pi(1)}+\dots+a_{\pi(j)}]^{-1}=\prod_ja_j^{-1}$; exact at finite $\epsilon$ with the adiabatic regulator ($j$-th denominator carries $+ij\epsilon$), not with a uniform $+i\epsilon$ (VF-WL-2). Proof: full (two proofs: simplex decomposition; induction), App B; shuffle identity and the non-abelian (web) decomposition in App B.
* **定义 `def:prelim-msbar` — $\overline{\rm MS}$ 方案** (no tag). VF-CONV-4: $g_0^2=4\pi\alpha_s(\mu)\mu^{2\varepsilon}e^{\varepsilon\gamma_E}(4\pi)^{-\varepsilon}Z_g^2$, i.e. $S_\varepsilon=(4\pi)^\varepsilon e^{-\varepsilon\gamma_E}$; warning: Collins 2011 uses $(4\pi)^\varepsilon/\Gamma(1-\varepsilon)$, which differs at $O(\varepsilon^2)$ and changes constants multiplying double poles (TMD hard factors: `rem:tmd-scheme-constants`).
* **命题 `prop:prelim-beta` — $\beta$ 函数** [R, R_PT]. VF-CONV-5: $\mu^2\frac{d\alpha_s}{d\mu^2}=-\frac{\beta_0}{4\pi}\alpha_s^2-\frac{\beta_1}{(4\pi)^2}\alpha_s^3+\dots$, $\beta_0=\frac{11}3C_A-\frac43T_Fn_f$, $\beta_1=\frac{34}3C_A^2-4C_FT_Fn_f-\frac{20}3C_AT_Fn_f$; one-loop solution. Proof: sketch ($\beta_0$ from $\delta Z_3$ and vertex counterterms — VF-PDF-14 gives $\delta Z_3$ and $\delta Z_2$); literature `GrossWilczek1973a`, `Politzer1973`, `Caswell1974`, `Jones1974`.
* **命题 `prop:prelim-rg` — 重整化群改进** [R, R_PT]. For a dimensionless RG-invariant $D(Q^2/\mu^2,\alpha_s(\mu))$: $D=D(1,\alpha_s(Q))$; at each order the coefficient of $\alpha_s^n(\mu)$ is a polynomial in $\ln(Q^2/\mu^2)$ fixed by lower orders and $\beta_i$. Proof: full (characteristics).
* **定义 `def:prelim-gamma5` — $\gamma_5$ 与 $\varepsilon$ 张量** (no tag). VF-CONV-10: $\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3$, $\varepsilon^{0123}=+1$, ${\rm Tr}(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma\gamma_5)=-4i\varepsilon^{\mu\nu\rho\sigma}$; in DR: HVBM with Larin's finite renormalization of the axial currents (App I). Warn: VGG use $\varepsilon_{0123}=+1$.
* **定理 `thm:prelim-composite-renorm` — 规范不变复合算符的重整化（Joglekar–Lee）** [R, R_PT]. Gauge-invariant local operators mix under renormalization only with gauge-invariant operators of the same dimension and quantum numbers, BRST-exact operators and equation-of-motion operators; the latter two classes have vanishing matrix elements between physical states. Hence physical matrix elements of twist-2 operators renormalize within $\{O_q,O_g\}$. Proof: sketch; literature `Joglekar:1975nu`, `Joglekar:1976eb`, `Joglekar:1976pe`, `Kluberg-Stern:1974iel`, `Kluberg-Stern:1975ebk`, `Henneaux:1993jn`, `DixonTaylor1974`; remark on `Collins:1994ee` (Hamberg–van Neerven puzzle) and on the non-local (light-ray) case, where the classification is *assumed* in Collins 2011 §11.3.2 (survey item 6).
* **定义 `def:prelim-plus` — 加号分布** (no tag). VF-CONV-7: $\int_0^1[g]_+h=\int_0^1g\,(h-h(1))$; $\mathcal D_k(z)=[\ln^k(1-z)/(1-z)]_+$; **product convention** $g(z)\mathcal D_k\equiv g(1)\mathcal D_k+\frac{g(z)-g(1)}{1-z}\ln^k(1-z)$; identities $C_F[\frac{1+z^2}{1-z}]_+=C_F[\frac{1+z^2}{(1-z)_+}+\frac32\delta(1-z)]$, $[\frac{2z}{1-z}]_+=\frac{2z}{(1-z)_+}+2\delta(1-z)$, $[\frac z{1-z}]_+=z[\frac1{1-z}]_++\delta(1-z)$; $(1+z^2)\mathcal D_1$ and $[(1+z^2)\ln(1-z)/(1-z)]_+$ differ by $\frac74\delta(1-z)$ (VF-DY-12). Plus distributions at $\tau\to0$ (thrust) and SCET star distributions are introduced in Ch14 with their own notation.
* **引理 `lem:prelim-plus-expansion` — $(1-z)^{-1-a\varepsilon}$ 的分布展开** (数学，无标签). On $[0,1]$, test functions continuous at 1, for $a\varepsilon<0$: $(1-z)^{-1-a\varepsilon}=-\frac{1}{a\varepsilon}\delta(1-z)+\sum_{k\ge0}\frac{(-a\varepsilon)^k}{k!}\mathcal D_k(z)$. Proof: full (App A). Used with $a=1$ (DIS), $a=2$ (DY, soft functions).
* **定义 `def:prelim-mellin` — Mellin 变换与卷积** (no tag). $\tilde f(N)=\int_0^1z^{N-1}f(z)dz$; $(f\otimes g)(x)=\int_x^1\frac{d\xi}\xi f(\xi)g(x/\xi)$; harmonic sums $S_k(N)$, $S_1(N)=\psi(N+1)+\gamma_E$, $S_2(N)=\zeta_2-\psi'(N+1)$; $\bar N=Ne^{\gamma_E}$.
* **引理 `lem:prelim-mellin` — Mellin 卷积定理与加号分布的矩** (数学，无标签). $\widetilde{f\otimes g}=\tilde f\tilde g$ (for distributions supported in $[0,1]$ with existing moments); $\int_0^1z^{N-1}\mathcal D_0=-S_1(N-1)$, $\int_0^1z^{N-1}\mathcal D_1=\frac12[S_1^2(N-1)+S_2(N-1)]$ (VF-CONV-8); large-$N$: $-\ln\bar N$, $\frac12(\ln^2\bar N+\zeta_2)$. Proof: full (App A).
* **定义 `def:prelim-cut` — 割图** (no tag). Cut propagators $2\pi\delta^+(p^2-m^2)(\slashed p+m)$; right of the cut: complex-conjugate rules (incl. Wilson-line rules of `prop:prelim-wilson-rules`).
* **定理 `thm:prelim-cutting-rules` — 切割规则** [R, R_PT]. For Feynman graphs with positive masses on all internal lines (or otherwise regulated so that all integrals converge), the largest-time equation gives $2\,{\rm Im}\,G=\sum_{\rm cuts}G_{\rm cut}$ in the physical region. Proof: sketch of the largest-time equation (`Veltman1963`, `tHooftVeltman1974`), `Cutkosky1960`. **注 `rem:prelim-cutting-dr`** [A]: extension to massless graphs in DR with ghosts (identity of meromorphic functions of $\varepsilon$); verified exactly in $\varepsilon$ at $O(g^2)$ for the current correlator (VF-EE-8); no single source writes the general massless DR version in full (c_ee §5).
* **命题 `prop:prelim-optical` — 流关联函数的光学定理** [R, R_def]. With VF-CONV-12/13/14: $\sum_X(2\pi)^4\delta^4(q-p_X)\langle0|j^\mu|X\rangle\langle X|j^\nu|0\rangle=2\,{\rm Im}\,\Pi^{\mu\nu}(q)$ ($q^0>0$), hence $R(s)=12\pi\,{\rm Im}\,\Pi(s+i0)$; $W^{\mu\nu}=\frac1{2\pi}{\rm Im}\,T^{\mu\nu}$ for $q^0>0$, $x<1$. 非微扰地位：对强子态需 MA0（态的完备性与谱条件）. Proof: full (insert states; ${\rm Im}[-1/(\Delta+i0)]=\pi\delta(\Delta)$). Check: free quark loop ${\rm Im}\,\Pi=N_ce_q^2/(12\pi)$ (VF-EE-3).

**Worked examples.**
* `ex:prelim-vacpol` — one-loop massless correlator in DR: $\Pi_0=N_ce_q^2\frac{2(D-2)}{D-1}\frac{G(1,1)}{(4\pi)^{D/2}}(-q^2-i0)^{-\varepsilon}$, $\overline{\rm MS}$: $\frac{N_ce_q^2}{12\pi^2}(\frac53-L)$, $L=\ln(-q^2/\mu^2)$; ${\rm Im}$ from $L\to\ln s-i\pi$ and from the two-particle cut agree exactly in $\varepsilon$ (VF-EE-3). Sign: $\Pi_{\rm PS}=-e^2\Pi$.
* `ex:prelim-eikonal-two` — eikonal identity for $m=2$; eikonal limit of an incoming quark propagator $S(p+k)ig\gamma^\mu t^au(p)\simeq-gt^a\frac{p^\mu}{p\cdot k+i0}u(p)$ (VF-WL-5).
* `ex:prelim-plus` — $\int_0^1dz(1-z)^{-1-2\varepsilon}z^{-\varepsilon}h(z)$ (the structure of every one-loop real emission).

**Figures.** existing (tikz2): `fig:soft-eikonal` (owned here since the audit: it shows external partons ↔ future/past-pointing semi-infinite Wilson lines, the content of `sec:prelim-wilson` and `ex:prelim-eikonal-two`; Ch8 refers back; its caption mentions the Glauber region — add a pointer to `def:ir-glauber`); new: `fig:prelim-feynman-rules`, `fig:prelim-wilson-rules` (adapt `research/c_wilson/tex/c_wilson_rules.tex`, `fig:cw-rules`); optional new `fig:prelim-lightcone`.

**Misconception box.** M24 (DR scaleless integrals) is in Ch7; here: "维数正规化消除红外发散" → it regulates them (`prop:pdf-partonic-dr`).

**Key citation keys.** `PeskinSchroeder1995`, `Muta2010`, `Collins1984`, `Weinberg1996`, `tHooftVeltman1972`, `tHooftVeltman1972b`, `tHooftVeltman1974`, `tHooft1973`, `BardeenEtAl1978`, `Cutkosky1960`, `Veltman1963`, `tHooft1971`, `Taylor1971`, `Slavnov1972`, `BecchiRouetStora1975`, `BecchiRouetStora1976`, `Tyutin1975`, `KugoOjima1979`, `GrossWilczek1973a`, `Politzer1973`, `Caswell1974`, `Jones1974`, `BreitenlohnerMaison1977a`, `Larin:1993tq`, `Joglekar:1975nu`, `Joglekar:1976eb`, `Kluberg-Stern:1974iel`, `Henneaux:1993jn`, `DixonTaylor1974`, `Collins:1994ee`, `Polyakov1980`, `BrandtNeriSato1981`, `KorchemskyRadyushkin1987`, `CombridgeKripfganzRanft1977`.

---------------------------------------------------------------------------------------------------

## Chapter 3 — 费曼积分的红外结构：钳夹、幂次计数与红外安全 / Infrared structure of Feynman integrals: pinches, power counting, IR safety

`\label{ch:ir}` · `ch03_ir.tex` · **14 pp** · full (proofs in App D, E)

**Purpose.** Geometric and analytic foundation of all graphical proofs: (i) where long-distance sensitivity can arise (Landau conditions in two forms — singularities in external invariants vs trapped points of the loop-momentum contour; critic O12); pinch vs endpoint; (ii) Coleman–Norton picture; (iii) pinch surfaces of massless QCD ↔ reduced diagrams; (iv) power counting with normal variables (units!) and leading regions; the Glauber region and its trapping criterion; (v) KLN, Bloch–Nordsieck (and its non-abelian failure), IR safety; (vi) method of regions with its precise status (Euclidean [R], Minkowskian [P]; critic C5: it is a cross-check, not the source of the region analysis).

**Depends on.** Ch2 (Feynman rules, `lem:prelim-boost`, `def:prelim-cut`, `thm:prelim-slavnov-taylor` for the cancellation of super-leading terms).

**Sections.**
1. `sec:ir-landau` Landau 方程：参数形式与动量形式 — $\alpha$-representation; theorem L1 (c_regions §1.2); envelope lemma; momentum-space criterion via Gordan; caveat (massless self-energy: momentum pinch without parameter pinch — Collins 2020 App. D1); endpoint vs pinch (`fig:landau-pinch`).
2. `sec:ir-coleman-norton` Coleman–Norton 图像 (`fig:coleman-norton`).
3. `sec:ir-pinch` 无质量 QCD 中的钳夹面与约化图 — massless vertex and box examples (`fig:vertex-regions`); reduced diagrams for $e^+e^-$, DIS, DY (`fig:reduced-ee`, `fig:reduced-dis`, `fig:reduced-dy`, all owned here since the audit; Ch9 and Ch11 refer back).
4. `sec:ir-power` 幂次计数 — normal variables, region table (`fig:momentum-regions`), the two units ($\lambda$ vs $\lambda_S=\lambda^2$), superficial degree formula, leading regions theorem, Feynman-gauge K-polarization dominance.
5. `sec:ir-glauber` Glauber 区 — definition, why eikonal fails, trapping criterion with explicit one-loop integrals (full analysis in Ch8, Ch11).
6. `sec:ir-cancellation` KLN、Bloch–Nordsieck 与红外安全.
7. `sec:ir-regions` 区域方法及其地位 — prescription, 1D toy with zero-bin, status, forward reference to the Sudakov examples of Ch4.

**Canonical statements.**

* **定义 `def:ir-landau-setup` — Feynman 参数表示与 Symanzik 多项式** (no tag). VF-REG-1: $I(p)=\int\prod\frac{d^Dk_l}{i\pi^{D/2}}\prod_j(-D_j-i0)^{-\nu_j}=\frac{\Gamma(\nu-LD/2)}{\prod\Gamma(\nu_j)}\int d\alpha\,\delta(1-\sum_{\sigma}\alpha)\prod\alpha_j^{\nu_j-1}\,\mathcal U^{\nu-(L+1)D/2}(\mathcal F-i0)^{LD/2-\nu}$; $\mathcal D(\alpha,k)=\sum_j\alpha_j(m_j^2-q_j^2)$, $\mathcal U=\det A$, $\mathcal F=\mathcal U\mathcal D(\alpha,k_c)$; homogeneity degrees $L$, $L+1$.
* **引理 `lem:ir-envelope` — 包络恒等式** (数学，无标签). For $\mathcal U\ne0$: $\partial_j(\mathcal F/\mathcal U)=-D_j(k_c)$; $\{\mathcal F=0,\alpha_j\partial_j\mathcal F=0\ \forall j\}\iff$ momentum-space Landau equations with $k=k_c(\alpha)$. Proof: full (App D). Caveat (must be printed): algebraic equivalence of the *equations*, not of the *pinches* (Collins 2020 App. D1; massless self-energy, VF-REG-4 remark).
* **定理 `thm:ir-landau-alpha` — Landau 条件（参数形式）：解析性与红外有限性判据** [R, R_PT]. (c_regions L1.) If the parametric integral is UV-convergent (or DR-continued) and there is no $\alpha$ in the closed simplex with $\mathcal F(\alpha,p_0)=0$ and $\alpha_j\partial_j\mathcal F(\alpha,p_0)=0$ for all $j$, then $I$ is finite at $p_0$ and extends holomorphically to a complex neighbourhood of $p_0$. Proof: full in App D — deformation $z_j=\alpha_j[1-i\tau\eta(\partial_j\mathcal F-\sum_k\alpha_k\partial_k\mathcal F)]$ preserving the constraint and the faces, ${\rm Im}\,\mathcal F(z)=-\tau\eta V+O(\eta^3)$, $V=\sum_j\alpha_j(\partial_j\mathcal F)^2-c^2\ge0$ (VF-REG-2), compactness, dominated convergence. Numerical illustration (c_regions L6).
* **定理 `thm:ir-landau-momentum` — 动量空间的钳夹必要条件** [R, R_PT]. (c_regions L3; blueprint S1.) For real $k_0$ with on-shell set $S$ and $u_j=\partial D_j/\partial k(k_0)$: if no $\alpha\in\mathbb R^S_{\ge0}\setminus\{0\}$ satisfies $\sum_{j\in S}\alpha_ju_j=0$, there is a local deformation $k\to k+i\eta\chi(k)v$ with ${\rm Im}\,D_j>0$ for $j\in S$ and $D_j\ne0$ for $j\notin S$; i.e. a trapped point satisfies the momentum-space Landau equations with $\alpha_j\ge0$. Proof: full — Gordan's alternative (`lem:appD-gordan`, App D) + exact formula $D_j(k+i\eta\chi v)=D_j(k)-\eta^2\chi^2(v'_j)^2+2i\eta\chi q_j\cdot v'_j$.
* **注 `rem:ir-landau-status`** [A]. Sufficiency (Landau ⇒ trapped) and the gluing of local deformations into a global one: complete proof only in the preprint `Collins:2020euz` (no journal record as of 2026-10; survey item 4); Collins 2011 §5.4.3 (p. 110): textbook proofs incomplete; `EdenEtAl1966` p. 48 "plausibility arguments"; `Muhlbauer:2020kut`, `Pham:2011SingInt` for the topological theory. Also: second-type singularities ($\mathcal U=0$) excluded.
* **定义 `def:ir-pinch-surface` — 钳夹面、内禀坐标与法坐标** (no tag).
* **命题 `prop:ir-coleman-norton` — Coleman–Norton 定理（代数形式）** [R, R_PT]. A real solution with $\alpha_j\ge0$ ⇔ a classical space-time process: $\Delta x_j=\alpha_jq_j$ on on-shell lines; loop equations ⇔ consistent vertex positions; massless lines move at light speed; zero-momentum lines connect arbitrary points. Proof: full (0.5 p). Remark: the stronger claim "trapped ⇔ classically realizable" needs the converse of `thm:ir-landau-momentum` and is [A] (`ColemanNorton1965`, gaps in the proof but not in the result: `Collins:2020euz`). Figure `fig:coleman-norton`.
* **命题 `prop:ir-pinch-classification` — 钳夹面与约化图** [A]. In massless QCD every pinch surface of a cut graph for $e^+e^-\to$ hadrons corresponds to a reduced diagram: one hard vertex, jets of collinear on-shell lines along light-like directions, a soft subgraph of zero-momentum lines; for DIS, SIA, DY add incoming target jets. Proof: sketch via `prop:ir-coleman-norton`. Literature: `Sterman1978a`, `Sterman1978b`, `LibbySterman1978a`, `Sterman1993`, Collins 2011 ch. 5.
* **定义 `def:ir-scalings` — 区域标度** (no tag). Table VF-REG-7 in $(k^+,k^-,k_T)$ with $\lambda=m/Q$: hard $Q(1,1,1)$; $A$-collinear $Q(1,\lambda^2,\lambda)$; $B$-collinear $Q(\lambda^2,1,\lambda)$; soft $Q(\lambda,\lambda,\lambda)$; ultrasoft $Q(\lambda^2,\lambda^2,\lambda^2)$; Glauber $|k^+k^-|\ll k_T^2$, typically $Q(\lambda^2,\lambda^2,\lambda)$; eikonal errors $O(\lambda)$, $O(\lambda^2)$, $O(1)$ for soft, ultrasoft, Glauber (c_regions P3). **Units:** Sterman's $\omega$ is the power of $\lambda_S=\lambda^2$; the power of $\lambda$ is $2\omega$. Libby–Sterman's "soft" = ultrasoft here; TMD factorization (Ch13) uses the soft scaling.
* **命题 `prop:ir-power-counting` — 超表观红外发散度** [R, R_PT]. For a reduced diagram $R$ in Feynman gauge (Sterman units; c_regions P2, boxed, VF-REG-8):
  $$\omega(R)=\sum_J\tfrac12\big(f^g_J+t_J+2u_J+2f^b_J-e_J\big)+\tfrac12\sum_Js^q_J+b_{S\to H}+\tfrac32f_{S\to H},$$
  $f^g_J$ ($f^b_J$) quark lines to $H$ through good (bad) components, $t_J$ transverse and $u_J$ "−" polarized gluons to $H$ (scalar-polarized $A^+$-type gluons not counted), $e_J=1$ (amplitude with one external parton) or $2$ (forward/target jet, or final-state jet of a cut graph), $s^q_J$ soft quarks attached to $J$, $b_{S\to H}$, $f_{S\to H}$ soft lines attached to $H$. The contribution of the homogeneous integral scales as $\lambda_S^{\omega}$ up to logarithms. Proof: full (App E: boost + dimension argument; blueprint S2 with the bad-component term added). Checks table (c_regions P7): Sudakov soft and collinear 0; transverse gluon into $H$ $\frac12$; "−" gluon 1; extra $q\bar q$ pair into $H$ 1; soft quark exchange 1; soft gluon into $H$ 1; soft quark into $H$ 2; gluon jet with only scalar gluons $-\frac12$ (super-leading). Remark: superficial degree only; nested sub-regions → `thm:ir-leading-regions` [A].
* **定理 `thm:ir-leading-regions` — 领头区域** [A]. In Feynman gauge for $e^+e^-\to$ hadrons, DIS, SIA, DY: $\omega=0$ regions are exactly those with (i) each jet attached to $H$ (and $H^*$) by one physical parton on each side (good quark component or transverse gluon) plus any number of scalar-polarized collinear gluons; (ii) soft subgraph attached only to jets and only by gluons; (iii) nothing soft attached to $H$; for DY additionally Glauber subregions of spectator–spectator exchanges. Super-leading configurations cancel by Ward identities and colour neutrality. Proof: sketch. Literature: `Sterman1978a`, `LibbySterman1978a`, `LibbySterman1978b`, Collins 2011 §5.8–5.11 (§5.9.2 leading-region rules; eqs. (5.75)–(5.79)), `CollinsSoperSterman1989` §8.7 (quotation verified by c_regions), `Sterman:1995fz` §§2.3–2.4 (eqs. (60)–(65); eq. (63) presupposes connected $S$, use eq. (64)). Gaps: nested regions (no Minkowskian analogue of Weinberg's theorem); in Feynman gauge extra disconnected hard scatterings cancel only after a sum over graphs (`Labastida:1984gy`; Collins 2011 §14.4.8).
* **例 `ex:ir-vertex` — 单圈无质量顶点** (VF-REG-4, REG-6). $\mathcal F=-Q^2\alpha_1\alpha_2$; Landau set: edges $\{\alpha_2=0\}$ ($k=xp_1$), $\{\alpha_1=0\}$, soft corner, soft-quark corners; no hard pinch for $Q^2\ne0$; Cayley-matrix check; Coleman–Norton pictures; collinear $k^-$ integral $\int dk^-[D_0D_1D_2]^{-1}=\frac{2\pi i}{2p_1^+}\frac{1}{k_T^2(xQ^2-k_T^2/(1-x))}$; logarithmic $k_T$ scaling; normal-coordinate exponent $p=4-2-2=0$. Figure `fig:vertex-regions`.
* **例 `ex:ir-k-dominance` — Feynman 规范下共线区域的标量极化主导** (VF-REG-8 remark; c_regions P5): $J\cdot H=(J^+/k^+)(k\cdot H)+O(\lambda^2)$ for the one-loop vertex; $J_T\cdot H_T=0$ in $D=4$ for back-to-back light-like quarks.
* **定义 `def:ir-glauber` — Glauber 区** (no tag). $|k^+k^-|\ll k_T^2$; $(p_A+k)^2\simeq2p_A^+k^--2p_{A,T}\cdot k_T-k_T^2$ — the $k_T^2$ is not negligible, eikonal approximation fails (error $O(1)$, VF-WL-11); couples as $A^-$ to $A$-lines and $A^+$ to $B$-lines with $1/k_T^2$ ("Coulomb").
* **命题 `prop:ir-glauber-trapping` — 单圈 Glauber 区的钳夹判据** [R, R_PT]. (c_regions §2.6, VF-REG-9.) For the one-loop vertex each light-cone integral sees one pole in the Glauber region: not trapped, contour can be moved to $|k^\pm|\sim k_T$; with an incoming and an outgoing $A$-collinear line carrying $k$ the poles $k^-=-k_T^2/(2p_A^+)+i0$, $k^-=k_T^2/(2p_{A'}^+)-i0$ pinch at $|k^-|\sim k_T^2/p^+$; the exact integral is finite, $2\pi i/[2k_T^2(p_A^++p_{A'}^+)]$, while the eikonal version diverges. Proof: full (residues). Forward: Ch8 `prop:method-glauber-deformation`, Ch11.
* **定理 `thm:ir-bn-qed` — QED 中的 Bloch–Nordsieck 定理** [R, R_PT]. For QED with massive charged fermions, soft-photon divergences cancel in cross sections inclusive over photons below an energy resolution; exponentiation (YFS). Proof: sketch; `BlochNordsieck1937`, `YennieFrautschiSuura1961`, `Weinberg1965`.
* **定理 `thm:ir-kln` — KLN 定理** [A]. Transition probabilities summed over degenerate initial *and* final states are IR finite at every order; caveat: a one-sided sum suffices but generically requires forward-scattering and disconnected contributions (`Frye:2018xjj`). Initial-state collinear singularities of hadron collisions are factorized into PDFs, not cancelled (M8). Proof: sketch; `Kinoshita1962`, `LeeNauenberg1964`, `Sterman:1976jh`.
* **命题 `prop:ir-bn-failure` — 有色初态时非阿贝尔 Bloch–Nordsieck 抵消的失效** [V]. Two massive coloured initial quarks, colour averaged: non-leading IR divergences from two soft gluons do not cancel at two loops (`DoriaFrenkelTaylor1980`; confirmed by `DiLietoEtAl1981`, `Andrasi:1980qw`); the non-cancelling terms are power suppressed at high energy (`Frenkel:1983di` to $O(g^4)$; "higher twist" `Catani:1985xt`); CSS 1989 §10.2: relative order $m^4/s^2$ in DY. Proof: sketch (structure: Coulomb/Glauber phase with colour matrices). Survey item 3.
* **定义 `def:ir-safe` — 红外安全可观测量** (no tag). Weights continuous under soft emission and collinear splitting; Sterman–Weinberg cones as example (Ch15).
* **定理 `thm:ir-safe-finite` — 红外安全可观测量的有限性** [A]. IR-safe $e^+e^-$ observables are finite order by order in massless PT. Proof: sketch; `Sterman1978a`, `Sterman1978b`, `Sterman:1979uw`, `StermanWeinberg1977`, `Ore:1979ry`. (The total cross section is proved separately and at [R] in Ch5.)
* **定义 `def:ir-regions` — 区域方法** (no tag). Beneke–Smirnov prescription: choose regions, Taylor expand, integrate over the full domain in DR (with analytic regulators where needed), drop scaleless integrals, sum; Jantzen's four conditions (domains cover, expansions commute, all integrals regularized, absolute convergence) (c_regions §3.3).
* **定理 `thm:ir-regions-euclid` — 欧氏极限的渐近展开** [R, R_PT]. For large Euclidean external momenta / large masses, expansion by regions coincides with the (proven) expansion by subgraphs. Proof: cite `Smirnov:1990rz`, `Smirnov2002`, `Gorishnii1989` (and Chetyrkin 1988, not in bib: do not cite).
* **命题 `prop:ir-regions-minkowski` — Minkowski 极限下区域方法的地位** [P]. No general proof for threshold, Sudakov, Regge, on-shell expansions; partial results: `Jantzen2011` (partition of the domain, conditions; massive Sudakov), `Pak:2010pt` (Newton polytope), `Jantzen:2012mw`, `Semenova:2018cwy` (leading order of each facet; full expansion when one facet contributes; multi-facet case reduced to an unproven commutativity), `Gardi:2022khw` (on-shell expansion; commuting expansions for two-jet soft subgraphs), `Ma:2023hrt`. Even the off-shell Sudakov example (four facets) is not covered by a complete proof (verified exactly at one loop, `ex:sudakov-offshell`, Ch4 — pointer). **Audit addition:** the facet prescription "regions = lower facets of the Newton polytope" fails as a general statement in Minkowski kinematics: three-loop non-planar $2\to2$ counterexamples with hidden regions (`Gardi:2024axt`; frontier/others §3.5). Print this as a sentence of the status paragraph: the prescription is [V] in general, the method with a correctly completed set of regions remains unproven ([P]/[C]), and SCET mode lists inherit this caveat.
* **例 `ex:ir-regions-toy` — 一维玩具积分与零区减除** (VF-REG-13). $I=\int_0^\infty dk/[(k+m)(k+M)]$; with $k^{-e}$: $T_s+T_h\to\ln(M/m)/M$, $T_sT_h=0$; with cutoffs the overlap must be subtracted (zero-bin).

**Worked examples.** `ex:ir-vertex`, `ex:ir-k-dominance`, `ex:ir-regions-toy`; plus `ex:ir-real-emission` — $e^+e^-\to q\bar qg$ with the gluon collinear to the quark: squared numerator $\sim\lambda^2$, propagators $\lambda^{-4}$, phase space $\lambda^2$ ⇒ logarithmic (c_regions P4); $\sum|M|^2\propto8(x_1^2+x_2^2)/((1-x_1)(1-x_2))$ (VF-EE-5).

**Figures.** existing (tikz2): `fig:landau-pinch`, `fig:vertex-regions`, `fig:coleman-norton`, `fig:reduced-ee`, `fig:reduced-dis`, `fig:reduced-dy`, `fig:momentum-regions` (the caption of `fig:momentum-regions` writes $n$, $\bar n$ for our $n_A$, $n_B$: say so in the text, FIGURES_INDEX §1 notes); optional new `fig:ir-landau-simplex` (adapt `research/c_regions/landau.tex`, `fig:landau-simplex`).

**Misconception box.** M8, M19 (method of regions is a theorem), M20 (Landau equations give the singularities), M9 (IR safety ⇒ factorization, first statement).

**Key citation keys.** `Landau1959`, `ColemanNorton1965`, `EdenEtAl1966`, `Pham:2011SingInt`, `Collins:2020euz`, `Muhlbauer:2020kut`, `Fevola:2023kaw`, `Gordan1873`, `Nakanishi:1959jzx`, `Cutkosky1960`, `Sterman1978a`, `Sterman1978b`, `LibbySterman1978a`, `LibbySterman1978b`, `CollinsSterman1981`, `Sterman:1995fz`, `Sterman1993`, `Collins2011`, `CollinsSoperSterman1989`, `Labastida:1984gy`, `Weinberg1960`, `Hahn:1968HZ`, `Kinoshita1962`, `LeeNauenberg1964`, `Frye:2018xjj`, `Sterman:1976jh`, `BlochNordsieck1937`, `YennieFrautschiSuura1961`, `Weinberg1965`, `DoriaFrenkelTaylor1980`, `DiLietoEtAl1981`, `Andrasi:1980qw`, `Frenkel:1983di`, `Catani:1985xt`, `StermanWeinberg1977`, `Sterman:1979uw`, `Ore:1979ry`, `BenekeSmirnov1998`, `Smirnov:1990rz`, `Smirnov2002`, `Smirnov2012`, `Gorishnii1989`, `Jantzen2011`, `Pak:2010pt`, `Jantzen:2012mw`, `Semenova:2018cwy`, `Gardi:2022khw`, `Ma:2023hrt`, `Ananthanarayan:2018tog`, `LeePomeransky2013`.

---------------------------------------------------------------------------------------------------

## Chapter 4 — Sudakov 形状因子与振幅的红外结构 / The Sudakov form factor and the infrared structure of amplitudes

`\label{ch:sudakov}` · `ch04_sudakov.tex` · **12 pp** · full

**Purpose.** (Critic's new chapter.) The simplest all-order factorization theorem, with every tool of the general method in its simplest setting and no PDFs: one-loop form factor exact in $\varepsilon$; regions (off-shell; massive exchange needs analytic regulators); factorization $F=H\cdot J\cdot J/S$ with Wilson-line definitions; Ward identities → Wilson lines; $K+G$ evolution; cusp anomalous dimension; exponentiation (incl. webs); IR poles of multi-leg amplitudes (dipole formula and its three-loop failure); Coulomb phases; strict collinear factorization of amplitudes (timelike) and a preview of the spacelike violation.

**Depends on.** Ch2 (Wilson lines, MS-bar), Ch3 (regions, power counting).

**Sections.**
1. `sec:sudakov-oneloop` 一圈形状因子 — exact in $\varepsilon$; UV/IR bookkeeping; timelike continuation; $\pi^2$ enhancement.
2. `sec:sudakov-regions` 区域分析 — on-shell massless (= hard region), off-shell (four regions), massive exchange (analytic regulator; collinear anomaly analogue); LL coefficients (`fig:sudakov-ff`).
3. `sec:sudakov-factorization` 全阶因子化 $F=H\cdot J\cdot J/S$ — reduced diagrams, Ward identities, Wilson-line definitions of jet and soft functions; subtraction at one loop (`ex:method-sudakov-subtraction` is in Ch8; here the structure) (`fig:sudakov-hjjs`).
4. `sec:sudakov-evolution` $K+G$ 演化、cusp 反常维度与指数化 (`fig:sudakov-cusp`).
5. `sec:sudakov-multileg` 多腿振幅的红外极点 — $\mathbf Z$ factorization; dipole formula; three-loop non-dipole terms; webs (`fig:sudakov-dipole`).
6. `sec:sudakov-collinear` 振幅的共线因子化与 Coulomb 相位 — timelike strict collinear factorization (Feige–Schwartz); Coulomb phases; spacelike preview (full in Ch17).

**Canonical statements.**

* **定义 `def:sudakov-ff` — 夸克形状因子** (no tag). $\bar u(p_2)\Gamma^\mu u(p_1)$ for massless on-shell quarks: $\Gamma^\mu=F(q^2)\gamma^\mu$ (chirality); spacelike $Q^2=-q^2>0$; timelike $q^2=s+i0$.
* **命题 `prop:sudakov-oneloop` — 一圈形状因子（精确到 $\varepsilon$ 的所有阶）** [R, R_PT]. VF-SUD-1:
  $$F=1+\frac{\alpha_s}{4\pi}C_F\Big(\frac{\mu^2}{Q^2}\Big)^\varepsilon\frac{e^{\varepsilon\gamma_E}\Gamma(1+\varepsilon)\Gamma^2(1-\varepsilon)}{\Gamma(1-2\varepsilon)}\Big[-\frac{2-\varepsilon+2\varepsilon^2}{\varepsilon^2(1-2\varepsilon)}\Big]=1+\frac{\alpha_s}{4\pi}C_F\Big(\frac{\mu^2}{Q^2}\Big)^\varepsilon\Big[-\frac2{\varepsilon^2}-\frac3\varepsilon-8+\zeta_2+\varepsilon\big(-16+\tfrac32\zeta_2+\tfrac{14}3\zeta_3\big)+O(\varepsilon^2)\Big];$$
  all poles infrared ($Z_1=Z_2$; scaleless external self-energies); timelike: $(\mu^2/Q^2)^\varepsilon\to(\mu^2/s)^\varepsilon e^{i\pi\varepsilon}$, $2{\rm Re}F^{(1)}=\frac{\alpha_sC_F}{2\pi}(\frac{\mu^2}{s})^\varepsilon\cos(\pi\varepsilon)f(\varepsilon)$, timelike exceeds spacelike by $\frac{\alpha_sC_F}{2\pi}\pi^2$ (VF-SUD-2). Proof: full (Feynman parameters; 1 p) — App G for details; checks: c_dis, c_ee, c_dy (MVV 2005 through $\varepsilon^4$), c_scet.
* **例 `ex:sudakov-onshell-hard` — 在壳无质量形状因子 = 硬区** (VF-REG-10/c_regions §3.7). With $\mathcal F=Q^2\alpha_1\alpha_2$ the integral is its hard region; IR poles = UV poles of scaleless low-energy regions ($1/\varepsilon_{\rm UV}-1/\varepsilon_{\rm IR}=0$).
* **例 `ex:sudakov-offshell` — 离壳 Sudakov 三角形的区域展开** (VF-REG-10; `fig:sudakov-ff`). Regions (each $\times1/Q^2$): $H=(\frac{\mu^2}{Q^2})^\varepsilon e^{\varepsilon\gamma_E}\frac{\Gamma(1+\varepsilon)\Gamma^2(-\varepsilon)}{\Gamma(1-2\varepsilon)}$, $C_{1,2}=-(\frac{\mu^2}{P^2})^\varepsilon e^{\varepsilon\gamma_E}\frac{\Gamma(1+\varepsilon)\Gamma^2(-\varepsilon)}{\Gamma(1-2\varepsilon)}$, $S=-(\frac{\mu^2Q^2}{P^4})^\varepsilon e^{\varepsilon\gamma_E}\Gamma(1+\varepsilon)\Gamma(\varepsilon)\Gamma(-\varepsilon)$, soft and Glauber zero; sum $=\frac1{Q^2}[\ln^2\frac{Q^2}{P^2}+\frac{\pi^2}3]+O(\varepsilon)$; poles cancel ($1-2+1$); NLP/NNLP agree with the exact Usyukina–Davydychev result. Literature: `BecherBroggioFerroglia2015` §2.2 (eqs. (2.39)–(2.44)) — the method is `BenekeSmirnov1998`; this example is BBF's (c_regions correction to blueprint E3.19). Normalization note: $q^2C_0=Q^2I$ (VF-REG-14).
* **例 `ex:sudakov-massive` — 有质量交换：需要解析正规化** (VF-REG-11). Pure DR leaves $\int dx/x$ unregulated (rapidity divergence); with analytic regulators $H+C_1+C_2=\frac1{Q^2}[\frac12\ln^2\frac{Q^2}{M^2}+\frac{\pi^2}3]$ (`Jantzen2011` eqs. (6.26)–(6.30); `BecherBroggioFerroglia2015` eqs. (2.50)–(2.52)); the large logarithm reappears through the cancellation of $1/\delta$ poles — analogue of the collinear anomaly (`BecherNeubert2011`). Contrast: on-shell *massive legs* with a massless gluon are DR-regulated (VF-REG-12; this corrects critic O11).
* **例 `ex:sudakov-ll` — 双对数系数** (VF-SUD-4). $\delta F_{\rm LL}=-\frac{\alpha}{2\pi}\ln\frac{Q^2}{P_1^2}\ln\frac{Q^2}{P_2^2}$ (off-shell), $-\frac{\alpha}{4\pi}\ln^2\frac{Q^2}{M^2}$ (massive photon) — Sudakov's and Jackiw's coefficients as quoted in `Collins:1989bt`; QCD: $\alpha\to C_F\alpha_s$.
* **定理 `thm:sudakov-factorization` — Sudakov 形状因子的全阶因子化** [A]. At leading power the (IR-regulated) form factor factorizes as $F=H(Q^2/\mu^2)\,J_1\,J_2/S$ (or in Collins' form with rapidity variables), $J_i$ = matrix elements of a quark field and a Wilson line along the opposite direction, $S$ = vacuum expectation of two Wilson lines (cusp). Proof: sketch using only Ch2–Ch3 and the literature (audit: no forward dependency) — (1) leading regions (`thm:ir-leading-regions`, `prop:ir-power-counting`); (2) collinear and soft approximations in their simplest form (one hard vertex, two back-to-back jets); (3) Ward identities → Wilson lines: abelian case shown explicitly here from the elementary identities (VF-WL-6) and the eikonal identity (`lem:prelim-eikonal-identity`, `prop:prelim-wilson-rules`); the non-abelian all-order step is cited from Collins 2011 §10.8 (with `thm:prelim-slavnov-taylor`); (4) subtractions: the one-loop region structure (`ex:sudakov-offshell`, zero-bin overlaps scaleless in DR); all orders cited from Collins 2011 §10.3 (p. 321) and §10.8 (p. 359), where this case is treated completely. Forward pointers only (not in `\uses{}`): the general lemmas `lem:method-ward-abelian`, `lem:method-ward-multi`, `thm:method-subtraction` and the example `ex:method-sudakov-subtraction` (Ch8). `\uses{thm:ir-leading-regions,prop:ir-power-counting,lem:prelim-eikonal-identity,prop:prelim-wilson-rules,thm:prelim-slavnov-taylor,prop:sudakov-oneloop}`. Literature: `Mueller:1979ih`, `Collins:1980ih`, `Sen:1981sd`, `Sen1983`, `Collins:1989bt`, `Magnea:1990zb`, `Korchemsky1989`, `Akhoury1979`. 地位与缺口: general non-abelian Ward-identity step outlined; the subtraction proof is complete in Collins' book for this case.
* **命题 `prop:sudakov-kg` — $K+G$ 演化方程** [A]; one-loop content [R, R_PT] (VF-SUD-3). $\frac{\partial\ln F}{\partial\ln Q^2}=\frac12[K(\varepsilon,\alpha_s(\mu))+G(Q^2/\mu^2,\alpha_s(\mu),\varepsilon)]$, $K$ a pure counterterm series, $G$ finite as $\varepsilon\to0$, $\mu\frac{dK}{d\mu}=-\gamma_K=-\mu\frac{dG}{d\mu}$; one loop: $K=\frac{\alpha_sC_F}{4\pi}\frac4\varepsilon$, $G=\frac{\alpha_sC_F}{2\pi}(3+2\ln\frac{\mu^2}{Q^2})$, $\gamma_K=\frac{2C_F\alpha_s}\pi$ (critic c7, pole and log terms). Proof: sketch of the all-order derivation from `thm:sudakov-factorization` + RG; one-loop check full.
* **推论 `cor:sudakov-exponentiation` — 指数化与解析延拓** [A]. $F$ exponentiates; the double logarithms are governed by $\gamma_K$; $|F(q^2)/F(-q^2)|^2$ is finite and computable (`Magnea:1990zb`); one-loop: $\pi^2$ term (VF-SUD-2).
* **定义 `def:sudakov-cusp` — cusp 反常维度** (no tag). VF-CONV-23: $\Gamma_{\rm cusp}=\sum_n(\frac{\alpha_s}{4\pi})^{n+1}\Gamma_n$, $\Gamma_0=4C_F$, $\Gamma_1=4C_F[(\frac{67}9-\frac{\pi^2}3)C_A-\frac{20}9T_Fn_f]$ (note the misprint in Becher–Schwartz App. A, c_scet §6.10); Collins' $\gamma_K=2\Gamma_{\rm cusp}$. One-loop cusp of two timelike Wilson lines with cusp angle $\beta$: $\Gamma(\beta)=\frac{\alpha_sC_F}\pi(\beta\coth\beta-1)$ (VF-CONV-23, verified by the audit: c_tmd R4 soft-factor pole plus a structural check; the $-1$ is the line self-energy, $\Gamma(0)=0$). Literature `Polyakov1980`, `BrandtNeriSato1981`, `KorchemskyRadyushkin1987`, `Korchemsky1989`.
* **命题 `prop:sudakov-webs` — 非阿贝尔指数化（webs）** [A]; $O(g^2)$ statement [R, R_def]. $W^{(2)}-\frac12(W^{(1)})^2=\frac14\sum_{r,s}[T_s,T_r](E(r,s)-E(s,r))$ exactly at finite $\epsilon$ (VF-WL-3): $\ln W$ starts at $O(g^2)$ with commutators only; all-order web exponentiation `Gatheral1983`, `FrenkelTaylor1984`.
* **定理 `thm:sudakov-ir-poles` — 无质量多腿振幅红外极点的因子化** [A]. $|\mathcal M(\{p\},\varepsilon)\rangle=\mathbf Z(\{p\},\mu,\varepsilon)|\mathcal M_{\rm fin}(\{p\},\mu)\rangle$ with $\mathbf Z$ from a colour-space anomalous dimension; through two loops $\mathbf\Gamma=\sum_{(i,j)}\frac{\mathbf T_i\cdot\mathbf T_j}{2}\gamma_{\rm cusp}\ln\frac{\mu^2}{-s_{ij}}+\sum_i\gamma^i$ — normalization fixed by VF-SUD-5: $(i,j)$ runs over ordered pairs $i\ne j$, $s_{ij}=2\sigma_{ij}p_i\cdot p_j+i0$, $\gamma_{\rm cusp}$ Casimir-stripped; checked by the audit against VF-SCET-8 (the two-parton case reproduces $d\ln C_V/d\ln\mu$); cite `Becher:2009cu` eq. (2). Literature `Catani:1998bh` (two-loop poles), `Sterman:2002qn`, `Becher:2009cu`, `Becher:2009qa`, `Gardi:2009qi`, `DixonMagneaSterman2008`. Status: explicit to the orders computed [R]; all-order factorization of poles [A] (survey item 30).
* **命题 `prop:sudakov-dipole-violation` — 偶极子公式作为全阶精确公式的失效** [V]. At three loops non-dipole corrections appear: a constant for three coloured partons, conformal-cross-ratio dependence for $\ge4$ (`Almelid:2015jia`); the term preserves strict timelike collinear factorization. Proof: cite; structure explained.
* **命题 `prop:sudakov-coulomb` — Coulomb 相位** [R, R_PT] (one loop). The imaginary parts $i\pi\,\mathbf T_i\cdot\mathbf T_j$ arise for pairs both incoming or both outgoing and differ between timelike and spacelike invariants; at one loop: ${\rm Im}F^{(1)}(s+i0)=\frac{\alpha_sC_F}{4\pi}[-\frac{2\pi}\varepsilon+2\pi\ell-3\pi]$, cancelling in $|F|^2$ (VF-EE-4). Proof: full (one loop).
* **命题 `prop:sudakov-amplitude-factorization` — 振幅的硬—软—共线因子化（出射或阈值运动学）** [A]. Feige–Schwartz all-order hard–soft–collinear factorization of amplitudes; excludes initial-state partons collinear to final-state ones (`FeigeSchwartz2014` §2, §7; `Feige:2013zla`). Consistent with the spacelike violation (Ch17).
* **注 `rem:sudakov-spacelike`** [V] (preview of `prop:break-spacelike`).

**Worked examples.** `ex:sudakov-onshell-hard`, `ex:sudakov-offshell`, `ex:sudakov-massive`, `ex:sudakov-ll`; one-loop $K,G$ extraction (part of `prop:sudakov-kg`).

**Figures.** existing: `fig:sudakov-ff` (tikz2); new: `fig:sudakov-hjjs`, `fig:sudakov-cusp`, `fig:sudakov-dipole`.

**Misconception box.** M16 (rapidity divergences are artefacts — first mention, here for the massive Sudakov form factor), M21 preview.

**Key citation keys.** `Sudakov1956`, `Mueller:1979ih`, `Collins:1980ih`, `Sen:1981sd`, `Sen1983`, `Akhoury1979`, `Magnea:1990zb`, `Collins:1989bt`, `Korchemsky1989`, `KorchemskyRadyushkin1987`, `Polyakov1980`, `BrandtNeriSato1981`, `Gatheral1983`, `FrenkelTaylor1984`, `Catani:1998bh`, `Sterman:2002qn`, `Becher:2009cu`, `Becher:2009qa`, `Gardi:2009qi`, `Almelid:2015jia`, `DixonMagneaSterman2008`, `FeigeSchwartz2014`, `Feige:2013zla`, `CataniDeFlorianRodrigo2012`, `Gonsalves1983`, `MochVermaserenVogt2005`, `BecherBroggioFerroglia2015`, `BenekeSmirnov1998`, `Jantzen2011`, `UsyukinaDavydychev1993a`, `BecherNeubert2011`, `BecherBell2012`, `Collins2011`, `Dixon:2019lnw`.

---------------------------------------------------------------------------------------------------

# 第二部分 严格核心：OPE 可及的量 (Part II — The rigorous core)

---------------------------------------------------------------------------------------------------

## Chapter 5 — 严格核心 I：$e^+e^-$ 湮灭总截面 / Rigorous core I: the $e^+e^-$ total cross section

`\label{ch:ee}` · `ch05_ee.tex` · **12 pp** · full

**Purpose.** Prove, inside renormalized PT, that $R(s)\equiv12\pi\,{\rm Im}\,\Pi(s+i0)$ is IR finite at every order and compute it to $O(\alpha_s)$ in two independent ways (cut diagrams; Euclidean two-loop correlator); show analyticity, unitarity and RG in their cleanest setting; state honestly the status of condensates and of duality. Proof route (critic O3, c_ee §5): Euclidean IR finiteness + polynomial structure in $\ln(-q^2/\mu^2)$ + trivial analytic continuation.

**Depends on.** Ch2 (`prop:prelim-optical`, `thm:prelim-cutting-rules`, `rem:prelim-cutting-dr`, `prop:prelim-rg`, `def:prelim-msbar`, `prop:prelim-unitarity`), Ch3 (KLN, for remarks).

**Logical flow chart (print at the start of §5.4).** `prop:ee-analytic` + `lem:ee-single-scale` + `thm:ee-euclid-ir` + UV renormalization ⇒ $\Pi_R(s+i0)$ finite; + `prop:ee-adler-rg` ⇒ polynomial structure (`thm:ee-R-finite`); + cutting rules ⇒ equality with the sum over partonic final states (`cor:ee-cuts`, [A]); explicit $O(\alpha_s)$: `prop:ee-oneloop`, `prop:ee-twoloop`, `prop:ee-cutting-exact`.

**Sections.**
1. `sec:ee-R` $R$ 比与流关联函数 — normalizations VF-CONV-12, VF-EE-1.
2. `sec:ee-analytic` 解析性、谱表示与 Adler 函数.
3. `sec:ee-euclid` 欧氏红外有限性与重整化群 — the IR-degree count $d=A+\frac12A_q\ge2$.
4. `sec:ee-theorem` 主定理：$R(s)$ 的红外有限性.
5. `sec:ee-oneloop` $O(\alpha_s)$：实—虚相消与两圈关联函数 — real/virtual in one normalization; two-loop Euclidean route; exact cutting identity; KLN for the total rate vs the non-IR-safe quark spectrum.
6. `sec:ee-higher` 高阶：$\pi^2$ 项与已知系数 — contour formula; $r_n$ vs $d_n$; literature values.
7. `sec:ee-ope` 欧氏 OPE 与凝聚.
8. `sec:ee-duality` 类时区：抹平与对偶.

**Canonical statements.**

* **定义 `def:ee-R` — $R$ 比** (no tag). $R(s)=\sigma(e^+e^-\to{\rm hadrons})/\sigma(e^+e^-\to\mu^+\mu^-)$, one-photon exchange, lowest order in $\alpha$, $\sigma_{\mu\mu}=4\pi\alpha^2/(3s)$; $R_0=N_c\sum_qe_q^2$ (VF-EE-1).
* **命题 `prop:ee-R-ImPi` — $R=12\pi\,{\rm Im}\,\Pi$** [R, R_def]. With $\Pi^{\mu\nu}=i\int d^4x\,e^{iq\cdot x}\langle0|Tj^\mu(x)j^\nu(0)|0\rangle=(q^\mu q^\nu-q^2g^{\mu\nu})\Pi(q^2)$: $\sigma=\frac{16\pi^2\alpha^2}{s}{\rm Im}\,\Pi(s+i0)$, $R=12\pi\,{\rm Im}\,\Pi(s+i0)$ (lepton tensor contraction $L_{\mu\nu}(q^\mu q^\nu-q^2g^{\mu\nu})=s^2$). 非微扰地位：MA0. Proof: full (VF-CONV-12).
* **命题 `prop:ee-analytic` — 解析性与正定性** [R, R_def]. $\Pi(q^2)$ is analytic in $\mathbb C\setminus[s_0,\infty)$, ${\rm Im}\,\Pi(s+i0)\ge0$, once-subtracted dispersion relation $\Pi(q^2)-\Pi(-\mu^2)=\frac{q^2+\mu^2}\pi\int_{s_0}^\infty ds\frac{{\rm Im}\Pi(s)}{(s-q^2-i0)(s+\mu^2)}$; $s_0=4m_\pi^2$ (hadrons) or $0$ (massless PT). 非微扰地位：对强子需 MA0（Källén–Lehmann 表示、正定谱密度、多项式有界）. Proof: full given the spectral representation (half page); PT version from `lem:ee-single-scale`.
* **引理 `lem:ee-single-scale` — 无质量传播子型图的单标度结构** [R, R_PT]. Every bare $(n+1)$-loop contribution to $\Pi$ in massless QCD with DR equals $c_n(\varepsilon)(\mu_0^2)^{n\varepsilon}(-q^2-i0)^{-(n+1)\varepsilon}$ with $c_n$ meromorphic (VF-EE-15). Proof: full ($\alpha$-representation: $\mathcal F=-q^2\mathcal U_2$, $\mathcal U_2\ge0$; dimension count; blueprint S4).
* **定义 `def:ee-adler` / 命题 `prop:ee-adler-dispersion` — Adler 函数** [R, R_def]. $D(Q^2)\equiv-12\pi^2Q^2\frac{d\Pi(-Q^2)}{dQ^2}=Q^2\int_0^\infty ds\frac{R(s)}{(s+Q^2)^2}$; $D$ is free of the additive renormalization of $\Pi$. Check: $R$ const ⇒ $D=R$ (VF-EE-14).
* **定理 `thm:ee-euclid-ir` — 欧氏红外有限性** [R, R_PT]. In a renormalizable theory with massless fields and no super-renormalizable couplings, renormalized Green functions at non-exceptional Euclidean momenta are finite at every order (MS-bar or BPHZL subtractions). Proof: sketch with the IR-degree computation printed in full (blueprint S3: for a soft subset $S$ attached $A$ times to non-soft lines, $A_q$ of them quark ends, $d=A+\frac12A_q\ge2$; VF-EE-13, architect derivation — writer re-derives); convergence theorem cited: `PoggioQuinn1976` (general physics-level proof; "any physical discontinuity of Green's functions is also infrared finite"), `LowensteinZimmermann1975`, `Lowenstein:1975ps`, `Breitenlohner:1975hg`, `Breitenlohner:1976te`, `BreitenlohnerMaison1977a`, `Frob:2015uqy` (pure YM). 地位注：the explicit check that the Breitenlohner–Maison hypotheses are spelled out for non-abelian gauge fields with FP ghosts in covariant gauges is **(to verify)** (c_ee §5); the gauge-invariant current correlator is gauge independent.
* **命题 `prop:ee-adler-rg` — Adler 函数的重整化群** [R, R_PT]. $(\mu^2\partial_{\mu^2}+\beta(\alpha_s)\partial_{\alpha_s})D=0$, $D(Q^2)=R_0\,d(a(Q^2))$; $\mu^2d\Pi/d\mu^2$ is $q$-independent (contact term); at order $a^n$, $\Pi_{\overline{\rm MS}}$ is a polynomial in $L=\ln(-q^2/\mu^2)$ of degree $\max(1,n)$ (VF-EE-9). Proof: full.
* **定理 `thm:ee-R-finite` — $R(s)$ 在微扰论每一阶的红外有限性** [R, R_PT]. (c_ee Theorem 5.1.) Let $R^{(n)}$ be the coefficient of $a^n$ of $12\pi\,{\rm Im}\,\Pi_{\overline{\rm MS}}(s+i0)$ computed with $D$-dimensional loops and analytic continuation of the bare expressions at fixed $\varepsilon$. Then (i) $\lim_{\varepsilon\to0}R^{(n)}$ exists; (ii) for $n\ge1$ it is a polynomial of degree $\le n-1$ in $\ln(s/\mu^2)$; (iii) it equals the analytic continuation $L\to\ln(s/\mu^2)-i\pi$ of the Euclidean renormalized correlator. Proof: full (steps (a)–(c) of c_ee §5: finiteness at $q^2<0$; Laurent coefficients are polynomials in $L$ vanishing for all real $L$ hence identically; continuation commutes with $\varepsilon\to0$).
* **推论 `cor:ee-cuts` — 与部分子末态求和的等同；KLN** [A]. $R^{(n)}$ equals the sum over all cuts (all partonic final states with physical polarizations, including $\overline{\rm MS}$ counterterm insertions) of the $D$-dimensional cross section; each cut separately has poles up to $\varepsilon^{-2n}$; for $e^+e^-$ only final-state degeneracies are needed. Proof: `thm:prelim-cutting-rules`, `rem:prelim-cutting-dr`, `prop:prelim-unitarity`; exact-in-$\varepsilon$ check at $O(g^2)$ (`prop:ee-cutting-exact`). 地位：no single source writes the massless, IR-regulated $D$-dimensional cutting rules with ghosts in complete rigour (c_ee §5).
* **命题 `prop:ee-oneloop` — $O(\alpha_s)$ 的实辐射与虚修正** [R, R_PT]. In the common normalization $N_\varepsilon=\frac{\alpha_sC_F}{2\pi}(\frac{4\pi\mu_0^2}{s})^\varepsilon c_\Gamma$: virtual $\rho_V/\rho_0=N_\varepsilon[-\frac2{\varepsilon^2}-\frac3\varepsilon-8+\pi^2+O(\varepsilon)]$ (from $2{\rm Re}F$, exact form VF-EE-4), real $\rho_R/\rho_0=\frac{\alpha_sC_F}{2\pi}(\frac{4\pi\mu_0^2}s)^\varepsilon\frac{2(1-2\varepsilon)(2-2\varepsilon+\varepsilon^2)\Gamma(1-\varepsilon)^2}{\varepsilon^2(1-3\varepsilon)(2-3\varepsilon)\Gamma(1-3\varepsilon)}=N_\varepsilon[\frac2{\varepsilon^2}+\frac3\varepsilon+\frac{19}2-\pi^2+O(\varepsilon)]$ (VF-EE-5); sum $\frac32N_\varepsilon\Rightarrow R=R_0(1+\frac{3C_F}4\frac{\alpha_s}\pi)$ (VF-EE-6). Warning to print: separate real/virtual constants depend on the common normalization (the two $\Gamma$-prefactors differ by $1-\frac{\pi^2}2\varepsilon^2$), only the sum does not. Proof: full (App G: matrix element (3.4), three-body phase space (3.5), Dirichlet integrals).
* **命题 `prop:ee-twoloop` — 欧氏两圈关联函数** [R, R_PT]. Exact bare result $\Pi^{(1)}_{\rm bare}=N_ce_q^2C_F\frac{g_0^2(Q^2)^{-2\varepsilon}}{(4\pi)^D}[r_1G(1,1)^2+r_2G(1,1)G(1+\varepsilon,1)]$ with $r_1,r_2$ of VF-EE-7; Ward identity $q_\mu q_\nu\Pi^{\mu\nu}=0$; $\Pi_{\overline{\rm MS}}=\frac{N_ce_q^2}{12\pi^2}[\frac53-L+\frac{\alpha_s}\pi\frac{3C_F}4(\frac{55}{12}-4\zeta_3-L)]$; $D=N_ce_q^2(1+\frac{3C_F}4\frac{\alpha_s}\pi)$. Proof: sketch in text, details App G (IBP triangle rule, $\hat I(1,1,1,1,1)=6\zeta_3$).
* **命题 `prop:ee-cutting-exact` — $O(g^2)$ 处精确到 $\varepsilon$ 的切割恒等式** [R, R_PT]. $2(D-1)s\,{\rm Im}\,\Pi^{(1)}_{\rm bare}(s+i0)=\rho_V+\rho_R$, term by term ($r_1G_{11}^2\leftrightarrow\rho_V$, $r_2G_{11}G_{1+\varepsilon,1}\leftrightarrow\rho_R$) (VF-EE-8). Proof: full (reflection formulas).
* **推论 `cor:ee-R-alphas` — $R(s)$ 的微扰展开** [R, R_PT] (for the $O(\alpha_s)$ coefficient and the structural relations). $R=R_0[1+\frac34C_Fa+r_2a^2+r_3a^3+\dots]$, $a=\alpha_s(s)/\pi$ ($\overline{\rm MS}$, $\mu^2=s$, photon exchange, massless quarks); SU(3): $r_2=\frac{365}{24}-11\zeta_3-n_f(\frac{11}{12}-\frac23\zeta_3)=1.9857-0.1153n_f$ (VF-EE-10, verified); general group $r_2=-\frac3{32}C_F^2+C_FC_A(\frac{123}{32}-\frac{11}4\zeta_3)-C_FT_Fn_f(\frac{11}8-\zeta_3)$ **(literature form; reduces to the verified SU(3) value; cite `ChetyrkinKataevTkachov1979`, `DineSapirstein1979`, `CelmasterGonsalves1980a`)**; structural relations $r_1=d_1$, $r_2=d_2$, $r_3=d_3-\frac{\pi^2}3b_0^2d_1$, $r_4=d_4-\pi^2(b_0^2d_2+\frac56b_0b_1d_1)$ with $b_0=\beta_0/4$, $b_1=\beta_1/16$ (VF-EE-9, verified); the singlet $(\sum e_q)^2$ term starts at $a^3$ (Furry's theorem; link to the previous monograph). Higher literature values ($r_3$, $O(a^4)$: `GorishniiKataevLarin1991`, `SurguladzeSamuel1991`, `BaikovChetyrkinKuhn2008`) quoted only as "(literature)".
* **命题 `prop:ee-contour` — 围道公式** [R, R_def]. $R(s)=\frac1{2\pi}\int_{-\pi}^{\pi}d\theta\,D(se^{i\theta})$ (c_ee §6; VF-EE-9). Proof: full.
* **定理 `thm:ee-ope` — 流关联函数的欧氏 OPE** [A]. $\Pi(-Q^2)=C_{\mathbb 1}(Q^2)+\sum_qC_{m\bar qq}\frac{\langle m_q\bar qq\rangle}{Q^4}+C_G\frac{\langle\frac{\alpha_s}\pi G^2\rangle}{Q^4}+O(Q^{-6})$ in renormalized PT for Green functions; no $1/Q^2$ term for massless quarks (no dimension-2 gauge-invariant operator). Coefficients: `ShifmanVainshteinZakharov1979a`, `ShifmanVainshteinZakharov1979b` (normalization to be converted to VF-CONV-12 — to verify). Proof: sketch, self-contained (audit: no forward dependency) — (1) Weinberg's theorem and Zimmermann's identity with improved remainder for the Euclidean two-point function of the gauge-invariant current; (2) Lorentz covariance and dimension counting (no gauge-invariant operator of dimension 2); (3) BRST-exact and EOM operators have vanishing vacuum expectation values (`thm:prelim-composite-renorm`). 地位与缺口: proven to all orders in PT for scalar theories (`Zimmermann1973`; convergence at each order `Hollands:2011gf`) and for gauge-invariant operators in pure Yang–Mills (`Hollands:2007zg`); for QCD with quarks "proved in a gauge theory the same way" (`Collins1984` §12.8) or widely assumed (`IzubuchiEtAl2018` Sec. II) — hence [A]. The full status discussion is repeated with `thm:dis-ope` (Ch6), which refers back to this proof.
* **猜想 `conj:ee-np-ope` — 非微扰 OPE 与凝聚** [C]. The OPE holds between hadronic/vacuum states with the same coefficients, condensates being non-perturbative parameters; $\langle G^2\rangle$ is ambiguous at the level of the leading IR renormalon (`prop:power-adler-large-beta0`); `Novikov:1984rf`, `David:1983gz`, `David:1985xj`.
* **命题 `prop:ee-smearing` — Poggio–Quinn–Weinberg 抹平恒等式** [R, R_def]. $\bar R(s,\Delta)\equiv\frac\Delta\pi\int_0^\infty ds'\frac{R(s')}{(s'-s)^2+\Delta^2}=\frac{12\pi}{2i}[\Pi(s+i\Delta)-\Pi(s-i\Delta)]$. 非微扰地位：MA0. Proof: full (from `prop:ee-analytic`).
* **猜想 `conj:ee-duality` — 夸克—强子对偶** [C]. (a) $\bar R=\bar R_{\rm PT}+O(\Lambda^4/\Delta^2)$ for $\Delta\sim s$ rests on the non-perturbative OPE in the complex plane; (b) local (pointwise) duality is not controlled by the OPE (oscillating terms invisible in the $1/Q^2$ expansion). `PoggioQuinnWeinberg1976`, `Shifman2000`. (M27.)

**Worked examples.**
* `ex:ee-twoloop-route` — the Euclidean two-loop route reproduces $1+\alpha_s/\pi$ (strongest pedagogical demonstration of `thm:ee-R-finite`).
* `ex:ee-pi2` — the $\pi^2$ term $-\frac{\pi^2}3b_0^2d_1$ at $O(a^3)$ from the contour formula; numerical size ($\frac{\pi^2}3b_0^2=16.66,14.28,12.09$ for $n_f=3,4,5$) dominates the known $r_3$.
* `ex:ee-quark-spectrum` — KLN at work and its limits (c_ee §7, VF-EE-11): exclusive pieces $\pm2/\varepsilon^2$; the quark energy spectrum keeps $-\frac1\varepsilon\frac{\alpha_s}{2\pi}P_{qq}(x)$ (moments $0,\frac43,\frac{25}{12},\frac{157}{60}$ times $C_F$) — absorbed into FFs (Ch10).

**Figures.** existing: `fig:ee-oneloop` (tikz2); new: `fig:ee-pi-plane` (complex $q^2$ plane: cut $[0,\infty)$, Euclidean point, circle $|z|=s$ traversed counter-clockwise from $s+i0$ to $s-i0$, smearing points $s\pm i\Delta$).

**Misconception box.** M27 (perturbative $R(s)$ valid pointwise); "the $O(\alpha_s^2)$ singlet term" (vanishes by Furry's theorem).

**Key citation keys.** `AppelquistGeorgi1973`, `Zee1973`, `Adler1974`, `PoggioQuinn1976`, `PoggioQuinnWeinberg1976`, `LowensteinZimmermann1975`, `Lowenstein:1975ps`, `LowensteinSpeer1976`, `Breitenlohner:1975hg`, `Breitenlohner:1976te`, `BreitenlohnerMaison1977a`, `Symanzik1973`, `KinoshitaUkawa1976`, `Frob:2015uqy`, `Sterman:1976jh`, `Sterman1978a`, `Sterman1978b`, `ChetyrkinKataevTkachov1979`, `DineSapirstein1979`, `CelmasterGonsalves1980a`, `CelmasterGonsalves1980b`, `GorishniiKataevLarin1991`, `SurguladzeSamuel1991`, `BaikovChetyrkinKuhn2008`, `ChetyrkinKuhnKwiatkowski1996`, `KrasnikovPivovarov1982`, `KataevStarshenko1995`, `ChetyrkinTkachov1981`, `Tkachov1981`, `Gonsalves1983`, `MochVermaserenVogt2005`, `ShifmanVainshteinZakharov1979a`, `ShifmanVainshteinZakharov1979b`, `Novikov:1984rf`, `David:1983gz`, `David:1985xj`, `Shifman2000`, `EllisStirlingWebber1996`, `Kinoshita1962`, `LeeNauenberg1964`, `Frye:2018xjj`, `Hollands:2011gf`, `Holland:2014pna`.

---------------------------------------------------------------------------------------------------

## Chapter 6 — 严格核心 II：深度非弹散射与算符乘积展开 / Rigorous core II: DIS and the operator product expansion

`\label{ch:dis}` · `ch06_dis.tex` · **14 pp** · full (uniqueness proofs in App K)

**Purpose.** Moment factorization of DIS structure functions, rebuilt per critic O4–O7: (1) analyticity and crossing of the forward Compton amplitude; (2) the dispersion relation identifies the Taylor coefficients at $\omega=0$ (unphysical, Euclidean-like region) with moments; (3) the **Euclidean** short-distance OPE (status [A] for QCD with quarks) gives these coefficients; (4) RG; (5) moments ⇒ x-space only in the sense of distributions; pointwise remainder not controlled (counterexample); light-cone OPE as the x-space structure behind it ([A]); higher twist and target mass; polarized moments (Bjorken sum rule). The x-space theorem with operator-defined PDFs is completed in Ch7 (`thm:pdf-dis-xspace`).

**Depends on.** Ch2 (`prop:prelim-optical`, `thm:prelim-composite-renorm`, `prop:prelim-rg`, Mellin), Ch5 (methodological model).

**Proof architecture (flow chart at chapter start).** `prop:dis-compton-analytic` → `prop:dis-dispersion` ⟵ `thm:dis-ope` + `lem:dis-tree-ope` → `thm:dis-moments` → `prop:dis-ope-rg` → `cor:dis-scaling`; App K lemmas → Ch7.

**Sections.**
1. `sec:dis-kinematics` 运动学、强子张量与结构函数 (`fig:dis-kinematics`).
2. `sec:dis-compton` 前向 Compton 振幅：解析性、交叉与色散关系 (`fig:forward-compton`, `fig:omega-plane`).
3. `sec:dis-ope` 扭度与欧氏算符乘积展开 (`fig:ope-schematic`) — tree level; the OPE theorem and its status; gauge-theory subtleties (BRST-exact and EOM operators; trace subtractions).
4. `sec:dis-moments` 主定理：结构函数矩的因子化.
5. `sec:dis-rg` 重整化群与标度破坏.
6. `sec:dis-wilson` Wilson 系数的单圈计算 — two derivations (cut diagrams + moments; hard-region forward amplitude) (`fig:dis-oneloop`).
7. `sec:dis-xspace` 从矩到 $x$ 空间：唯一性与非一致性 — App K results stated; the $\sin(Q^2x)$ counterexample; light-cone OPE.
8. `sec:dis-higher-twist` 高扭度与靶质量修正 (`fig:higher-twist`).
9. `sec:dis-polarized` 极化 DIS 的矩：Bjorken 求和规则.

**Canonical statements.**

* **定义 `def:dis-kinematics` — DIS 运动学与强子张量** (no tag). VF-CONV-13: $Q^2=-q^2$, $x=Q^2/(2P\cdot q)$, $y=P\cdot q/P\cdot\ell$, $\omega=1/x$; $W^{\mu\nu}=\frac1{4\pi}\int d^4z\,e^{iq\cdot z}\langle P|[j^\mu(z),j^\nu(0)]|P\rangle$ (spin averaged) $=(-g^{\mu\nu}+\frac{q^\mu q^\nu}{q^2})F_1+\tilde P^\mu\tilde P^\nu\frac{F_2}{P\cdot q}$; **$F_L=(1+4M^2x^2/Q^2)F_2-2xF_1$** (reduces to $F_2-2xF_1$ at $M\to0$; critic D1, c_dis §2); cross section $\frac{d^2\sigma}{dx\,dQ^2}=\frac{4\pi\alpha^2}{xQ^4}[xy^2F_1+(1-y-\frac{x^2y^2M^2}{Q^2})F_2]$ **(writer re-derives from the lepton tensor; PDG form not re-checked)**, $M\to0$: $\frac{2\pi\alpha^2}{xQ^4}[(1+(1-y)^2)F_2-y^2F_L]$.
* **命题 `prop:dis-W-structure` — 强子张量的一般结构** [R, R_def]. (i) $q_\mu W^{\mu\nu}=0$; (ii) the decomposition is the most general symmetric one for an unpolarized target (P, T, hermiticity); (iii) $F_1\ge0$, $F_L\ge0$ (positivity of $\epsilon^*_\mu W^{\mu\nu}\epsilon_\nu$; $2x\,\epsilon_L\epsilon_LW=F_L$, $\epsilon_T\epsilon_TW=F_1$; VF-CONV-13); (iv) $W^{\mu\nu}=0$ for $x>1$, elastic contribution at $x=1$. 非微扰地位：MA0. Proof: full.
* **定义 `def:dis-compton` — 前向 Compton 振幅** (no tag). VF-CONV-14: $T^{\mu\nu}=i\int d^4z\,e^{iq\cdot z}\langle P|Tj^\mu(z)j^\nu(0)|P\rangle$, invariant amplitudes $T_{1,2}(\omega,Q^2)$ with the same tensors.
* **命题 `prop:dis-compton-analytic` — 解析性与交叉** [R, R_PT]. At fixed $Q^2>0$, $T_{1,2}$ are analytic in the $\omega$-plane cut along real $|\omega|\ge1$; $T_1(-\omega)=T_1(\omega)$, $T_2(-\omega)=-T_2(\omega)$; ${\rm Im}\,T_i(\omega+i0)=2\pi F_i$ for $\omega\ge1$. 非微扰地位：对强子靶需 MA0（解析性由因果性与谱条件给出）与 MA3（$|\omega|\to\infty$ 时的增长界，最低阶矩所需；Regge 行为）. Proof: crossing and ${\rm Im}\,T=2\pi W$ full; analyticity — PT: $\alpha$-representation at fixed $q^2<0$; hadrons: cite the retarded-commutator/Jost–Lehmann–Dyson literature (not in bib — state as MA0 content).
* **命题 `prop:dis-dispersion` — 色散关系：Taylor 系数 = 矩** [R, R_PT]. For $|\omega|<1$: $T_2=\sum_{n=2,4,\dots}4\omega^{n-1}M^{(2)}_n$, $T_1-T_1(0)=\sum_{n=2,4,\dots}4\omega^nM^{(1)}_n$, $M^{(2)}_n=\int_0^1dx\,x^{n-2}F_2$, $M^{(1)}_n=\int_0^1dx\,x^{n-1}F_1$ (elastic peak included). Proof: full (contour deformation, `fig:omega-plane`; left cut by crossing; drop the circle at infinity under MA3). **Mandatory check:** free quark $F_2=e_q^2\delta(1-x)$ ⇒ $T_2=4e_q^2\omega/(1-\omega^2)$ (VF-CONV-14; blueprint S5).
* **定义 `def:dis-twist` — 扭度与扭度 2 算符** (no tag). VF-CONV-15: $O_q^{\mu_1\cdots\mu_n}=\mathcal S\bar\psi\gamma^{\mu_1}iD^{\mu_2}\cdots iD^{\mu_n}\psi-$traces, $O_g^{\mu_1\cdots\mu_n}=\mathcal S G^{\mu_1\alpha}iD^{\mu_2}\cdots iD^{\mu_{n-1}}G_\alpha{}^{\mu_n}-$traces (sign fixed by $\langle g|O_g^{+\cdots+}|g\rangle=2(k^+)^n$, i.e. $O_g^{+\cdots+}=\sum_jG^{+j}(iD^+)^{n-2}G^{+j}$); $\langle P|O_i^{\mu_1\cdots\mu_n}|P\rangle=2A_i^{(n)}(P^{\mu_1}\cdots P^{\mu_n}-{\rm traces})$; one-gluon vertex of $O_q$ (VF-PDF-12).
* **引理 `lem:dis-tree-ope` — 树图 OPE** [R, R_PT]. At tree level between quark states $T^{\mu\nu}$ equals the OPE with $C^{(n)}_{1,q}=C^{(n)}_{2,q}=e_q^2$ for even $n$; odd $n$ cancel between $s$- and $u$-channel graphs (crossing). Proof: full (expand $\frac{1}{(p\pm q)^2}=\frac{-1}{Q^2(1\mp\omega)}$; blueprint S5).
* **定理 `thm:dis-ope` — 重整化微扰论中的欧氏 OPE** [A]. For Green functions of $T\,j^\mu j^\nu$ with IR-regulated (e.g. off-shell Euclidean) partonic external momenta, as $Q^2\to\infty$ (Euclidean $q$, or for each fixed Taylor coefficient in $\omega$):
  $$T^{\mu\nu}=\sum_{n=2,4,\dots}\sum_i\Big[\Big(-g^{\mu\nu}+\frac{q^\mu q^\nu}{q^2}\Big)\frac{2^nq_{\mu_1}\cdots q_{\mu_n}}{(Q^2)^n}C^{(n)}_{1,i}+\Big(g^\mu{}_{\mu_1}-\frac{q^\mu q_{\mu_1}}{q^2}\Big)\Big(g^\nu{}_{\mu_2}-\frac{q^\nu q_{\mu_2}}{q^2}\Big)\frac{2^nq_{\mu_3}\cdots q_{\mu_n}}{(Q^2)^{n-1}}C^{(n)}_{2,i}\Big]O_i^{\mu_1\cdots\mu_n}+R,$$
  $C$ independent of external states and IR regulators, $R$ = twist $\ge4$ contributions, $O(Q^{-2})\times$logs for each fixed $n$; BRST-exact and EOM operators drop out of physical matrix elements (`thm:prelim-composite-renorm`). Forward on-shell partonic matrix elements are at **exceptional** momenta ($P_{\rm in}=P_{\rm out}$) and are not covered by the non-exceptional Euclidean theorem; their use to extract Wilson coefficients (`prop:dis-wilson-partons`) is an additional step, verified exactly in $\varepsilon$ at $O(\alpha_s)$ (VF-DIS-13) — say so (audit, after REFDOC_ANALYSIS §2.4 OUR-8). With $\langle P|O_i|P\rangle$ normalized as above: $T_1\ni2\omega^nC^{(n)}_{1,i}A^{(n)}_i$, $T_2\ni4\omega^{n-1}C^{(n)}_{2,i}A^{(n)}_i$ (normalization derived by the architect from `lem:dis-tree-ope` + `prop:dis-dispersion`; one-loop moments confirmed by c_dis `ope_check`, VF-DIS-13). Proof: sketch with steps (Weinberg's theorem; Zimmermann identity with improved remainder; Lorentz covariance; on-shell partonic matrix elements in DR) — the steps of `thm:ee-ope` (Ch5), now with quark and gluon external states and operators of every spin. **Status paragraph (verbatim in substance, survey item 1):** proven to all orders in PT for scalar theories (`Zimmermann1973`, `Zimmermann:1972te`, `Zimmermann1970`; convergence at each order in $\varphi^4$: `Hollands:2011gf`, `Holland:2014pna`) and for gauge-invariant operators in pure Yang–Mills (`Hollands:2007zg`; IR control `Frob:2015uqy`); for QCD with quarks "proved in a gauge theory the same way" (`Collins1984` §12.8) or "widely assumed" (`IzubuchiEtAl2018` Sec. II); gauge-theory ingredients `Joglekar:1976eb`, `Joglekar:1976pe`. Not valid beyond PT without MA0, MA4.
* **命题 `prop:dis-wilson-partons` — 由部分子结构函数提取 Wilson 系数** [R, 以 OPE 为前提]. $\int_0^1dz\,z^{n-2}\hat F_2^{(j)}=\sum_iC^{(n)}_{2,i}\langle j|O^{(n)}_i|j\rangle$ with partonic matrix elements $=\delta_{ij}$ plus pure $\overline{\rm MS}$ counterterms (all loop corrections to $\langle j|O_i|j\rangle$ are scaleless in DR for massless on-shell partons; the PDF analogue is `prop:pdf-partonic-dr`, Ch7 — pointer only). One-loop check exact in $\varepsilon$ (VF-DIS-13). Proof: full at one loop.
* **命题 `prop:dis-ope-rg` — Wilson 系数与约化矩阵元的重整化群** [R, 以 OPE 为前提]. In the convention VF-CONV-16: $\frac{dA^{(n)}_i}{d\ln\mu^2}=\sum_j\Gamma_{ij}(n,\alpha_s)A^{(n)}_j$, $\Gamma_{ij}=\frac{\alpha_s}{2\pi}\gamma_{ij}(n)+O(\alpha_s^2)$, $\gamma_{ij}(n)=\int_0^1z^{n-1}P_{ij}$; $\frac{dC^{(n)}_{a,j}}{d\ln\mu^2}=-\sum_iC^{(n)}_{a,i}\Gamma_{ij}$. Dictionary to MVV and to Gross–Wilczek must be printed (VF-PDF-10). Proof: full. 非微扰地位：MA0（强子矩阵元 $A^{(n)}$） (MA: audit).
* **定理 `thm:dis-moments` — DIS 结构函数矩的因子化** [R, 以 OPE 为前提]. For even $n\ge2$, as $Q^2\to\infty$ at fixed $n$:
  $$\int_0^1dx\,x^{n-2}F_2(x,Q^2)=\sum_iC^{(n)}_{2,i}\Big(\frac{Q^2}{\mu^2},\alpha_s(\mu)\Big)A^{(n)}_i(\mu)+O\Big(\frac1{Q^2}\Big),\qquad 2\int_0^1dx\,x^{n-1}F_1=\sum_iC^{(n)}_{1,i}A^{(n)}_i+O\Big(\frac1{Q^2}\Big),$$
  $i\in\{q,\bar q,g\}$, $A^{(n)}_q=\int_0^1x^{n-1}(q+\bar q)$ for even $n$ (after Ch7: `thm:pdf-moments-local`). The $O(1/Q^2)$ (twist 4, target mass) is not uniform in $n$ (resonances dominate for $n\gtrsim Q^2/M^2$). 非微扰地位：MA0、MA3、MA4（并需非微扰 OPE）. Proof: full given `thm:dis-ope` for partonic targets (insert, contract, compare the Taylor coefficients at $\omega=0$ with `prop:dis-dispersion`, for each fixed $n$; no convergence of the OPE in $\omega$ and no interchange of limits). **Caveat for hadrons (audit, after REFDOC_ANALYSIS §2.4 OUR-3):** with $q$ Euclidean in the hadron rest frame, $\omega=2iMq^4/Q^2$ lies on a segment of the imaginary axis of length $O(M/Q)$, so reading off Taylor coefficients from the OPE on that segment amplifies the $O(1/Q^2)$ errors; the hadron-level statement needs, besides the non-perturbative OPE, positivity of $F_2$ and the analyticity and polynomial bounds of MA0, with MA3 needed only for the lowest moments. Write the hadronic step as a sketch and say so in the 「地位与缺口」 paragraph; a complete conditional proof is proposed in REFDOC_ANALYSIS S20–S22 (lead-author decision, §0.9).
* **推论 `cor:dis-scaling` — 标度破坏** [R, 以 OPE 为前提]. Non-singlet LO: $M_n^{\rm NS}(Q^2)=M_n^{\rm NS}(Q_0^2)[\alpha_s(Q^2)/\alpha_s(Q_0^2)]^{-2\gamma_{qq}(n)/\beta_0}$; $n=2$ singlet: eigenvalues $0$ and $-\frac{4C_F+2n_fT_F}3$ of the $\gamma$-matrix; asymptotic quark momentum fraction $\frac{3n_f}{16+3n_f}$ (SU(3)) (VF-PDF-9). 非微扰地位：MA0、MA3、MA4 (MA: audit).
* **命题 `prop:dis-c-oneloop` — 单圈 Wilson 系数** [R, R_PT]. $C^{(n)}_{2,q}=e_q^2[1+\frac{\alpha_s}{2\pi}(C^q_{2,N}+\gamma_{qq}(N)\ln\frac{Q^2}{\mu^2})]_{N=n}$, gluon $C^{(n)}_{2,g}=\sum_qe_q^2\frac{\alpha_s}{2\pi}2(C^g_{2,N}+\gamma_{qg}(N)\ln\frac{Q^2}{\mu^2})$, $C_L$ similarly, with VF-DIS-8 closed forms and the table $N=1..8$ (c_dis §11). Checks: $C^q_{2,1}=0$ (Adler), $C^q_{1,1}=-C_F$ (Bjorken $\nu$ sum rule) (VF-DIS-14); MVV normalization $c^{(1)}_{2,\rm ns}=2C^q_{2,N}$ (a commonly quoted variant with $\frac2{N+1}+\frac1{N^2}$ fails the Adler check — critic c2). Proof: two derivations, both self-contained here (audit: no forward dependency): (i) cut diagrams in $D$ dimensions (calculation in App G `sec:appG-dis`; VF-DIS-3…7; `fig:dis-oneloop`) followed by Mellin moments, giving the closed forms for all $N$ (VF-DIS-8); (ii) hard-region forward Compton amplitude exactly in $\varepsilon$, $N\le8$ (VF-DIS-13). The $x$-space coefficient functions and their derivation are presented in Ch9 (`prop:disall-nlo`), which refers back.
* **注 `rem:dis-uniqueness` — 偶数矩决定 C 偶组合（数学）**. (VF-PDF-15.) Statement of `thm:appK-even-moments` and `cor:appK-pdf`: even moments ($N\ge N_1$) determine $q+\bar q$ and $g$ a.e. (for $x^{N_1-1}(\cdot)\in L^1$); odd moments determine $q-\bar q$; fails for distributions supported at $x=0$ ($\delta'$: all even moments vanish); continuation in $N$ unique under polynomial bounds (`prop:appK-continuation`); Carlson's sharp form; $P^+_{\rm NS}\ne P^-_{\rm NS}$ from NLO (`rem:pdf-ns-plusminus`). (M5, M6.)
* **注 `rem:dis-nonuniform` — 矩的 $O(1/Q^2)$ 不蕴含逐点 $O(1/Q^2)$**. $R_Q(x)=\sin(Q^2x)$ has $|Q^2\int x^nR_Q|\le c_n$ for all $n$ but $\sup|R_Q|=1$ (VF-MISC-3, critic c5). Consequence: the pointwise x-space statement is the [A] theorem `thm:disall-factorization` (critic O7; C4; M4).
* **命题 `prop:dis-light-cone` — 光锥展开** [A]. Near $z^2=0$ the current product expands in towers of fixed twist, each containing all spins $n$; leading tower twist 2. Literature `BrandtPreparata1971`, `Frishman1971`, `Frishman:1970fx`, `ChristHasslacherMueller1972`, `Anikin:1978tj` (arbitrary order of PT; theory class not checked — survey), `Zavyalov:1990kv`, light-ray operators `Balitsky:1987bk`, `MullerEtAl1994`. Explain why moments need only the short-distance theorem while fixed-$x$ statements are light-cone statements.
* **命题 `prop:dis-twist4` — 扭度 4 修正的算符结构** [R, 以 OPE 为前提]. $1/Q^2$ corrections to each moment from twist-4 operators (quark–gluon–quark, four-quark), their anomalous dimensions and mixing with EOM operators; matrix elements non-perturbative. Proof: sketch; `EllisFurmanskiPetronzio1982`, `EllisFurmanskiPetronzio1983`, `Jaffe:1982pm`, `Jaffe1983`, `Qiu:1988dn` (survey item 21: [R] in moment space modulo item 1). 非微扰地位：MA0、MA3、MA4 (MA: audit).
* **命题 `prop:dis-tmc` — 靶质量修正** [R, 以 OPE 为前提]. The trace terms of twist-2 matrix elements give target-mass corrections to the moments (Nachtmann moments; Georgi–Politzer); x-space representation with $\xi_N=2x/(1+\sqrt{1+4M^2x^2/Q^2})$; the "threshold problem" ($F_2^{\rm TMC}\ne0$ at $x>1$) shows the non-uniformity of the $M^2/Q^2$ expansion near $x\to1$ (prescription-dependent in x-space). Proof: sketch; `GeorgiPolitzer1976`, `Nachtmann1973`. 非微扰地位：MA0、MA3、MA4 (MA: audit).
* **定理 `thm:dis-bjorken` — Bjorken 求和规则** [R, 以 OPE 为前提]. $\int_0^1dx\,[g_1^p-g_1^n](x,Q^2)=\frac{g_A}6\big[1-a-(\frac{55}{12}-\frac{n_f}3)a^2+O(a^3)\big]+O(\Lambda^2/Q^2)$, $a=\alpha_s(Q^2)/\pi$, SU(3), $\overline{\rm MS}$ with the HVBM–Larin $\gamma_5$ scheme (non-singlet: scheme independent after Larin's finite renormalization); inputs: isospin, $g_A$ from $\beta$ decay. 非微扰地位：MA0、MA3、MA4. Proof: OPE with odd-$n$ axial operators; $a^2$ coefficient verified via the Crewther relation (VF-POL-1/2, critic c4); literature `Bjorken1966`, `Kodaira1980`, `LarinVermaseren1991`, `Larin:1993tq`.
* **注 `rem:dis-crewther` — Crewther 关系** (one formula, verified at $O(a^2)$): $C_{\rm Bjp}D_{\rm NS}=1+\beta_0(\frac78-\zeta_3)a^2+\dots$, $K_1=C_F(-\frac{21}8+3\zeta_3)$ (VF-POL-2).

**Worked examples.**
* `ex:dis-free-quark` — $T_2=4e_q^2\omega/(1-\omega^2)$ and ${\rm Im}\,T_2(\omega+i0)=2\pi e_q^2\delta(1-x)$ (sign check ${\rm Im}\frac{-1}{Q^2(\omega-1)+i0}=\pi\delta(\cdot)$).
* `ex:dis-n2` — $n=2$: energy–momentum tensor, $\sum_iA^{(2)}_i=1$ RG invariant, eigenvalue $0$.
* `ex:dis-oneloop-ope` — the hard-region forward Compton amplitude reproduces the moments of the cut calculation exactly in $\varepsilon$ ($N\le8$); renormalized Wilson coefficients and the residues $-\gamma_{qq}(N)$, $-\gamma_{qg}(N)$ (c_dis §11).
* `ex:dis-tmc-n2` — $O(M^2/Q^2)$ correction to the second moment from the trace terms (writer derives).

**Figures.** existing (tikz1): `fig:dis-kinematics`, `fig:forward-compton`, `fig:omega-plane`, `fig:ope-schematic`, `fig:dis-oneloop` (owned here since the audit; Ch9 refers back); existing (tikz3): `fig:higher-twist` (owned here since the audit; Ch20 refers back).

**Misconception box.** M3 (factorization is just the OPE), M4, M5, M6 (first statement), "Adler sum rule receives QCD corrections" (it does not: $C^q_{2,1}=0$ to all orders by current conservation; `Adler1966`), "Bloom–Gilman duality is a theorem" ([C], `BloomGilman1970`).

**Key citation keys.** `Bjorken1969`, `Wilson1969`, `Zimmermann1973`, `Zimmermann:1972te`, `Zimmermann1970`, `Wilson:1972ee`, `BrandtPreparata1971`, `Frishman1971`, `Frishman:1970fx`, `ChristHasslacherMueller1972`, `Anikin:1978tj`, `Zavyalov:1990kv`, `Balitsky:1987bk`, `MullerEtAl1994`, `Joglekar:1976eb`, `Joglekar:1976pe`, `Collins1984`, `Hollands:2007zg`, `Hollands:2011gf`, `Holland:2014pna`, `Frob:2015uqy`, `IzubuchiEtAl2018`, `Callan:1973pu`, `GrossWilczek1973b`, `GrossWilczek1974`, `GeorgiPolitzer1974`, `GeorgiPolitzer1976`, `Nachtmann1973`, `BardeenEtAl1978`, `FloratosRossSachrajda1977`, `Vermaseren:2005qc`, `Moch:2004xu`, `AltarelliMartinelli1978`, `Muta2010`, `PeskinSchroeder1995`, `EllisFurmanskiPetronzio1982`, `EllisFurmanskiPetronzio1983`, `Jaffe:1982pm`, `Jaffe1983`, `Qiu:1988dn`, `Bjorken1966`, `Kodaira1980`, `LarinVermaseren1991`, `Larin:1993tq`, `Adler1966`, `BloomGilman1970`.

---------------------------------------------------------------------------------------------------

## Chapter 7 — 严格核心 III：部分子分布与碎裂函数的算符定义 / Rigorous core III: operator definitions of PDFs and FFs

`\label{ch:pdf}` · `ch07_pdf.tex` · **14 pp** · full (all-order moment proof in App L)

**Purpose.** Define PDFs/FFs as gauge-invariant renormalized matrix elements (C1: before any factorization theorem); prove their basic properties (gauge invariance, free-field values, support, moments = local twist-2 matrix elements, DGLAP from operator renormalization, sum rules); compute the one-loop kernel directly from the operator definition; complete the x-space DIS theorem for the twist-2 part; discuss interpretation (number density, heuristic) and positivity ([C]); FFs and timelike evolution; polarized (helicity, transversity) definitions.

**Depends on.** Ch2 (Wilson lines, `thm:prelim-composite-renorm`, Mellin), Ch6 (`thm:dis-moments`, App K lemmas).

**Sections.**
1. `sec:pdf-definitions` 定义：夸克、反夸克与胶子分布 (`fig:pdf-operator`).
2. `sec:pdf-properties` 规范不变性、自由场值与支撑.
3. `sec:pdf-interpretation` 数密度诠释及其局限（启发式）.
4. `sec:pdf-moments` 矩与定域算符.
5. `sec:pdf-dglap` 重整化与 DGLAP 方程 (`fig:dglap-ladder`, `fig:splitting-vertices`).
6. `sec:pdf-oneloop` 单圈计算：由算符定义得到 $P_{qq}$ (`fig:pdf-oneloop`).
7. `sec:pdf-dis` $x$ 空间的 DIS 定理（扭度 2 部分）.
8. `sec:pdf-sumrules` 求和规则、方案与正定性.
9. `sec:pdf-ff` 碎裂函数、类时演化与极化分布的定义.

**Canonical statements.**

* **定义 `def:pdf-quark` — 夸克分布** (no tag). CONTEXT verbatim: $f_{q/H}(\xi;\mu)=\int\frac{dw^-}{4\pi}e^{-i\xi P^+w^-}\langle P|\bar\psi(w)\gamma^+W[w,0]\psi(0)|P\rangle_c$, $w=(0^+,w^-,\mathbf 0_T)$; connected; summed over the operator's colour index, averaged over target colour and spin; $\overline{\rm MS}$ renormalized; renormalization convention $f_{\rm ren}=Z\otimes f_{\rm bare}$ (VF-PDF-4).
* **定义 `def:pdf-antiquark` — 反夸克分布** (no tag). $f_{\bar q}(\xi)=-f_q(-\xi)$; equivalent to the definition with $\psi^c=C\bar\psi^{\mathsf T}$ and $W^*$ (c_pdf §2.2; VF-PDF-1); $q(x)=f_q(x)$, $\bar q(x)=-f_q(-x)$ for $x>0$.
* **定义 `def:pdf-gluon` — 胶子分布** (no tag). VF-PDF-2: $f_{g/H}(\xi)=\sum_j\int\frac{dw^-}{2\pi\xi P^+}e^{-i\xi P^+w^-}\langle P|G^{+j}_a(w)W^{(A)}_{ab}[w,0]G^{+j}_b(0)|P\rangle_c$ ($D-2$ transverse $j$); $f_g(-\xi)=-f_g(\xi)$; partonic gluon targets averaged over $D-2=2(1-\varepsilon)$ polarizations — part of the $\overline{\rm MS}$ convention (averaging over 2 shifts $C_2^g\to C_2^g+P_{qg}$, $\Delta_{qg}\to\Delta_{qg}+P_{qg}$; VF-CONV-6).
* **命题 `prop:pdf-invariance` — 规范不变性、推动不变性与自由场值** [R, R_def]. Gauge invariance (`prop:prelim-wilson-covariance`); dependence on $\xi$ only (boosts along $z$); $f^{(0)}_{q/q}=\delta(1-\xi)$, $f^{(0)}_{q/\bar q}=-\delta(1+\xi)$, $f^{(0)}_{g/g}=\delta(1-\xi)-\delta(1+\xi)$; $\langle k|T^{++}_g|k\rangle=2(k^+)^2$ fixes the gluon normalization (momentum sum rule). Proof: full (c_pdf s1, 21/21). 非微扰地位：MA0（强子态） (MA: audit).
* **定理 `thm:pdf-support-pt` — 支撑（微扰论）** [R, R_PT]. In PT, graph by graph, $f_{q/j}(\xi)=0$ for $|\xi|>1$ (and $f_g$ likewise) for partonic targets; support survives $\overline{\rm MS}$ renormalization since $Z(\xi/\zeta)$ vanishes for $\xi>\zeta$. Proof: sketch — light-front-ordered PT (Collins 2011 §6.9.3, p. 191: "the proofs are non-perturbative" refers to the spectral version) or the $\alpha$-representation of cut graphs (`Diehl:1998sm`); `Jaffe1983` (twist-4 multiparton support).
* **命题 `prop:pdf-support-hadron` — 支撑（强子态）** [A]. For hadron states, inserting complete states between $\bar\psi(w)W$ and $W\psi(0)$ (light-like separation: ordinary product = time-ordered, Jaffe) gives $p_X^+=(1-\xi)P^+\ge0\Rightarrow\xi\le1$; the antiquark term gives $\xi\ge-1$. 非微扰地位：MA0. Status [A] (survey item 7: spectral argument non-perturbative but rests on existence assumptions). Remark: the point $\xi=0$ is delicate (twist-3 $\delta(x)$ terms, `Burkardt–Koike` not in bib — mention without citation or omit).
* **注 `rem:pdf-number-density` — 数密度诠释（启发式）** (no tag; critic O8). Bare, UV-cutoff densities in $A^+=0$ gauge: $f=\|a|P\rangle\|^2\ge0$ (Collins 2011 §6.7, §6.9.1); caveats: UV divergence of the $k_T$ integral (renormalization destroys the interpretation), spurious $1/k^+$ singularities, zero modes, transverse links at light-cone infinity (`JiYuan2002`, `BelitskyJiYuan2003`). Not a statement about $\overline{\rm MS}$ PDFs (C3; M2, M11).
* **定义 `def:pdf-lightray` — 光线算符** (no tag). $O(w^-)=\bar\psi(w)\gamma^+W[w,0]\psi(0)$; $M(w^-)=\langle P|O(w^-)|P\rangle=2P^+\int d\xi\,e^{i\xi P^+w^-}f(\xi)$.
* **引理 `lem:pdf-wilson-moments` — Wilson 线顶点的矩 = 定域算符顶点** [R, R_def]. The $n$-th moment of the $m$-gluon vertex of $O(w^-)$ equals the $m$-gluon vertex of $\bar\psi\gamma^+(iD^+)^{n-1}\psi$ (divided differences; one gluon: $\frac{gt^an^\mu\gamma^+}{2(P^+)^n}\sum_{j=0}^{n-2}(k_2^+)^j(k_1^+)^{n-2-j}$, VF-PDF-12). Proof: full for $m=1,2$ (c_pdf s4(b): $n\le7$), induction for general $m$ (App L).
* **定理 `thm:pdf-moments-local` — PDF 的矩 = 扭度 2 定域算符矩阵元** [R, R_PT]. For $\overline{\rm MS}$-renormalized quantities, $\int_{-1}^1d\xi\,\xi^{n-1}f_q(\xi;\mu)=\frac{\langle P|[\bar\psi\gamma^+(iD^+)^{n-1}\psi]_\mu|P\rangle}{2(P^+)^n}=A^{(n)}_q(\mu)=\int_0^1x^{n-1}[q+(-1)^n\bar q]$ ($n\ge1$), $\int_0^1x^{n-1}g=\frac{\langle P|O_g^{(n)}|P\rangle}{2(P^+)^n}$ ($n$ even) (VF-PDF-11). 非微扰地位：对强子态需 MA0. Proof: full in App L — (1) bare identity (moments as derivatives at $w^-=0$, $\partial_{w^-}[\bar\psi W]=[\bar\psi\overleftarrow D^+]W$, total derivatives vanish in forward matrix elements; blueprint S6); (2) renormalization: $Z_f(N)=Z_O(N)$ by uniqueness of minimal subtraction, local operators by `thm:prelim-composite-renorm`; (3) all-order convolution structure: construct $Z_{ij}(x)$ from partonic targets, show finiteness for any state because pole parts are compactly supported distributions with all moments zero (Fourier–Laplace transform entire; gluon via the even distribution $\xi f_g$). One-loop check exact in $\varepsilon$ (VF-PDF-13). Remark: left- and right-acting derivatives agree only in forward matrix elements (GPDs, Ch18).
* **定理 `thm:pdf-dglap` — 由算符重整化得到 DGLAP 方程** [R, R_PT]. $\frac{\partial f_i(x;\mu)}{\partial\ln\mu^2}=\sum_j(\mathcal P_{ij}\otimes f_j)(x)$, $\mathcal P_{ij}=\frac{\alpha_s}{2\pi}P_{ij}+O(\alpha_s^2)$ (CONTEXT normalization; $P_{ij}$ always denotes the LO kernel), with $\mathcal P=-\alpha_s\partial Z^{(1)}/\partial\alpha_s$ for $Z=\mathbb 1+\sum_kZ^{(k)}/\varepsilon^k$ (one loop: $Z^{(1)}=-\frac{\alpha_s}{2\pi}P$, VF-PDF-4) (using $\mu^2d\alpha_s/d\mu^2=-\varepsilon\alpha_s+\beta(\alpha_s)$; higher poles cancel by consistency conditions). Proof: full. Logical order (C2): this precedes and is independent of any factorization theorem. 非微扰地位：MA0（强子态；部分子态无需） (MA: audit).
* **命题 `prop:pdf-lo-kernels` — 领头阶分裂函数** [R, R_PT]. VF-PDF-7: $P_{qq}=C_F[\frac{1+z^2}{1-z}]_+$, $P_{qg}=T_F[z^2+(1-z)^2]$, $P_{gq}=C_F\frac{1+(1-z)^2}z$, $P_{gg}=2C_A[\frac z{(1-z)_+}+\frac{1-z}z+z(1-z)]+\frac{\beta_0}2\delta(1-z)$ ($z/(1-z)_+$ means $z[1/(1-z)]_+$); $D$-dimensional kernels (VF-PDF-6); number and momentum sum rules; singlet matrix with $2n_fP_{qg}$; Mellin moments $\gamma_{ij}(N)$ (VF-PDF-8); $N=2$ matrix and eigenvalues (VF-PDF-9); convention dictionary (VF-PDF-10). Proof: full (real-emission kernels from the operator definitions in $A^+=0$, $\delta$-terms from virtual graphs or conservation laws — identical).
* **命题 `prop:pdf-pqq-operator` — Feynman 规范下由算符定义计算 $P_{qq}$** [R, R_PT]. With a gluon mass $m$ as IR regulator and DR for UV: real part $f_R=A_\varepsilon[(1-\varepsilon)^2(1-\xi)\xi^{-\varepsilon}+\frac{2\xi^{1-\varepsilon}}{1-\xi}]$, $A_\varepsilon=\frac{\alpha_s}{2\pi}C_Fe^{\varepsilon\gamma_E}\Gamma(\varepsilon)(\frac{\mu^2}{m^2})^\varepsilon$; Wilson-line real + virtual combine into $A_\varepsilon[2\xi^{1-\varepsilon}/(1-\xi)]_+$ (endpoint cancels only in the combination); self-energy $-A_\varepsilon\frac{1-\varepsilon}{2-\varepsilon}\delta(1-\xi)$; quark number exactly conserved in $\varepsilon$; UV poles graph by graph (units $\frac{\alpha_s}{2\pi}\frac{C_F}\varepsilon$): ladder $(1-\xi)$, Wilson $[\frac{2\xi}{1-\xi}]_+$, self-energy $-\frac12\delta$, sum $P_{qq}/C_F$; renormalized $f^{(1)}_{q/q}=\frac{\alpha_s}{2\pi}\{P_{qq}\ln\frac{\mu^2}{m^2}+C_F[-(1-\xi)(2+\ln\xi)-[\frac{2\xi\ln\xi}{1-\xi}]_++\frac14\delta(1-\xi)]\}$ (regulator dependent); light-cone-gauge ladder alone gives the same $D$-dimensional kernel (VF-PDF-3). Proof: full (App G); `fig:pdf-oneloop`.
* **命题 `prop:pdf-partonic-dr` — 纯维数正规化中的部分子分布** [R, R_PT]. For massless on-shell partons, bare PDFs are $\delta_{ij}\delta(1-\xi)$ to all orders (scaleless; $\int d^{2-2\varepsilon}l_T/l_T^2\propto\frac1{\varepsilon_{\rm UV}}-\frac1{\varepsilon_{\rm IR}}=0$); $\overline{\rm MS}$: $f_{i/j}=\delta_{ij}\delta(1-\xi)-\frac{\alpha_s}{2\pi}\frac1\varepsilon P_{ij}(\xi)+O(\alpha_s^2)$, the surviving pole being infrared (VF-PDF-5; C14, M24). Proof: full.
* **命题 `prop:pdf-local-anomalous` — 定域算符的单圈反常维度（含混合）** [R, R_PT]. UV poles of $\langle j|O_i|j\rangle$ give $\Gamma_{qq}=\gamma_{qq}$, $\Gamma_{q_kg}=2\gamma_{qg}$, $\Gamma_{gq}=\gamma_{gq}$, $\Gamma_{gg}=\gamma_{gg}$; per-graph Feynman-gauge and covariant-gauge values (only the sum including $\delta Z_{2,3}$ is gauge independent); $N=2$: $T^{++}$ not renormalized (VF-PDF-14). Proof: full for the quark sector (hand derivations A1, A2, B, C1 of c_pdf §6.3), gluon sector table.
* **定理 `thm:pdf-dis-xspace` — DIS 的 $x$ 空间因子化（扭度 2 部分）** [R, 以 OPE 为前提]. Define $F_2^{\rm tw2}$ as the unique distribution (`cor:appK-pdf`) whose even moments are $\sum_iC^{(n)}_{2,i}A^{(n)}_i$. Then $F_2^{\rm tw2}/x=\sum_iC_{2,i}\otimes f_i$ with $C_{2,i}$ the unique distributions with moments $C^{(n)}_{2,i}$; at $O(\alpha_s)$: $\frac{F_2^{\rm tw2}}x=\sum_qe_q^2\{(q+\bar q)+\frac{\alpha_s}{2\pi}[(C_2^q+LP_{qq})\otimes(q+\bar q)+2(C_2^g+LP_{qg})\otimes g]\}$, $L=\ln(Q^2/\mu^2)$, $C_L^q=2C_Fz$, $C_L^g=4T_Fz(1-z)$ (VF-DIS-7). $F_2-F_2^{\rm tw2}$ has moments $O(1/Q^2)$ for each fixed $n$; its pointwise size is not controlled (`rem:dis-nonuniform`). 非微扰地位：MA0、MA3、MA4. Proof: full (`thm:dis-moments` + `thm:pdf-moments-local` + `lem:prelim-mellin` + App K; constructively $C_{2,i}$ = $\overline{\rm MS}$-subtracted partonic structure functions, `prop:pdf-partonic-dr`).
* **命题 `prop:pdf-sum-rules` — 求和规则** [R, R_PT]. $\int_0^1(q-\bar q)=N_q$ ($\gamma_{qq}(1)=0$; conserved current); $\sum_i\int_0^1xf_i(x;\mu)=1$ exactly in $\overline{\rm MS}$ (finiteness of $T^{++}$, eigenvalue 0). 非微扰地位：对强子 MA0. Proof: full.
* **注 `rem:pdf-ns-plusminus` — 解析延拓与 $P^\pm_{\rm NS}$**. C-even (even $N$) and C-odd (odd $N$) continuations are different functions; unique under polynomial bounds (`prop:appK-continuation`); $P^+_{\rm NS}-P^-_{\rm NS}$ starts at NLO (colour factor $C_F(C_F-\frac{C_A}2)$ — standard, `CurciFurmanskiPetronzio1980`; not re-derived). (M6.)
* **注 `rem:pdf-schemes` — 方案变换**. $f'=Z\otimes f$, $C'=C\otimes Z^{-1}$; DIS scheme (VF-DIS-11); the gluon-average convention is part of the scheme.
* **猜想 `conj:pdf-positivity` — $\overline{\rm MS}$ PDF 的正定性** [C]. For $\mu$ above some scale $\mu_0$, $\overline{\rm MS}$ quark and gluon PDFs are non-negative. Evidence for: `CandidoForteHekhorn2020` (NLO positive in the perturbative regime), `Candido:2023ujx` (positivity inherited above $Q^2\gtrsim5$ GeV², "very conservative semi-quantitative estimate"); against a general theorem: `CollinsRogersSato2022` (bare PDFs need not be positive in DR; negative at low scales in a model). No verdict. Circularity warning (C13): LO evolution preserving positivity does not prove positivity of the initial condition. **Audit addition (print it):** the stronger statement "$\overline{\rm MS}$ PDFs are non-negative at every scale" is **false** — explicit one-loop counterexample in a Yukawa model, negative at low $\mu$ and positive at large $\mu$ (`CollinsRogersSato2022` eqs. (55)–(56); script-verified in frontier/others §7, Prop. 7.1); $\overline{\rm MS}$ heavy-quark PDFs are negative just below their matching threshold. The conjecture is therefore only about $\mu\ge\mu_0$, with $\mu_0$ non-perturbative.
* **定义 `def:pdf-ff` — 碎裂函数** (no tag). VF-CONV-17 (corrected by the audit): in the hadron frame $\mathbf p_{h,T}=0$, $w=(0^+,w^-,\mathbf 0_T)$, $d_{h/q}(z)=\frac{z^{1-2\varepsilon}}{4N_c}\sum_X\int\frac{dw^-}{2\pi}e^{ik^+w^-}{\rm Tr}_c{\rm Tr}_D[\gamma^+\langle0|W[\infty n_B,w]\psi(w)|hX\rangle\langle hX|\bar\psi(0)W[0,\infty n_B]|0\rangle]$, future-pointing lines; parton frame: $\frac1{4N_cz}$ with an explicit $\int d^{2-2\varepsilon}\mathbf p_{h,T}$ ($d^{2-2\varepsilon}p_{hT}=z^{2-2\varepsilon}d^{2-2\varepsilon}k_T$). Free quark $d_{q/q}=\delta(1-z)$. **Print the $O(\alpha_s)$ check** that the free-quark check cannot provide: $A^+=0$ gauge, $h=q$, $X=g$: $d^{(1)}_{q/q}=\frac{\alpha_s}{2\pi}C_F\frac{1+z^2}{1-z}\int\frac{dl_T^2}{l_T^2}$ ($z<1$); the first version's $\frac1{4N_cz}$ in the hadron frame would give $z^{-2}$ times this (REFDOC_ANALYSIS §2.4 OUR-1, S9). The Collins 2011 location (ch. 12) is to be verified.
* **命题 `prop:pdf-timelike-dglap` — 类时 DGLAP 演化** [R, R_PT]. $\frac{\partial d_{h/i}}{\partial\ln\mu^2}=\sum_jP^T_{ji}\otimes d_{h/j}$ (transposed index structure); $P^{T(0)}=P^{(0)}$ (Gribov–Lipatov), different at NLO (`CurciFurmanskiPetronzio1980`); momentum sum rule formal. Proof: sketch. (M23.) 非微扰地位：MA0（强子态） (MA: audit).
* **定义 `def:pdf-polarized` — 螺旋度与横度分布** (no tag). $\Delta q$ with $\gamma^+\gamma_5$, transversity $h_1$ with $i\sigma^{j+}\gamma_5$ (or $\gamma^+\gamma^j\gamma_5$), $\Delta g$; spin vectors; $\gamma_5$ scheme (`def:prelim-gamma5`). Processes and evolution: Ch10.

**Worked examples.** `ex:pdf-free-field` (c_pdf §2); `ex:pdf-oneloop` (= `prop:pdf-pqq-operator` in full); `ex:pdf-moments-exact` (one-loop moments exactly in $\varepsilon$: ladder ↔ vertex $A_\varepsilon\frac{(1-\varepsilon)^2}{(n-\varepsilon)(n+1-\varepsilon)}$, Wilson ↔ operator-gluon $-2A_\varepsilon\sum_{i=1}^{n-1}\frac1{i+1-\varepsilon}$, self-energy $-A_\varepsilon\frac{1-\varepsilon}{2-\varepsilon}$; $n=1$: 0; $n=2$: $-\frac{4A_\varepsilon}{3-\varepsilon}$); `ex:pdf-quark-in-gluon` (one-loop $f_{q/g}$: kernel $\hat P_{qg}=T_F[1-\frac{2z(1-z)}{1-\varepsilon}]$; effect of the polarization average).

**Figures.** existing (tikz1): `fig:pdf-operator`, `fig:pdf-oneloop`, `fig:dglap-ladder`, `fig:splitting-vertices`; optional new: `fig:pdf-gluon-operator`, `fig:pdf-ff-cut`.

**Misconception box.** M2, M6, M11, M23, M24, "PDFs are defined by DIS" (C1).

**Key citation keys.** `CollinsSoper1982a`, `Soper:1976jc`, `Soper:1979fq`, `Jaffe1983`, `Diehl:1998sm`, `Collins2011`, `Collins2003`, `CurciFurmanskiPetronzio1980`, `FurmanskiPetronzio1980`, `AltarelliParisi1977`, `GribovLipatov1972a`, `GribovLipatov1972b`, `Dokshitzer1977`, `Lipatov:1974qm`, `CataniSeymour1997`, `GrossWilczek1974`, `GeorgiPolitzer1974`, `Joglekar:1975nu`, `Collins:1994ee`, `MochVermaserenVogt2004`, `VogtMochVermaseren2004`, `CandidoForteHekhorn2020`, `CollinsRogersSato2022`, `Candido:2023ujx`, `AltarelliForteRidolfi1998`, `DiemozEtAl1988`, `Larin:1993tq`, `MertigVanNeerven1996`, `Vogelsang1996`, `RalstonSoper1979`, `JaffeJi1991`, `JaffeJi1992`, `JiYuan2002`, `BelitskyJiYuan2003`, `Hausdorff1923`, `Carlson1914`, `Titchmarsh1939`.

---------------------------------------------------------------------------------------------------

# 第三部分 共线因子化的全阶论证 (Part III — Collinear factorization to all orders)

---------------------------------------------------------------------------------------------------

## Chapter 8 — 全阶因子化证明的一般方法 / The general method of all-order factorization proofs

`\label{ch:method}` · `ch08_method.tex` · **16 pp** · full (proof details in App E, F)

**Purpose.** One reusable proof machine, stated as a template theorem with explicit hypotheses (H1)–(H5), so that Ch9–Ch13 only verify hypotheses and Ch17 can name the hypothesis that fails. Steps: regions → approximations (collinear, soft; with the correct $i0$) → Grammer–Yennie decomposition and power suppression → Ward identities → Wilson lines → subtractions → unitarity (final-state interactions, soft factor) → Glauber region → factorized form; scale and scheme dependence. Critic C7: the order "approximate → Ward identity → Wilson line" must be respected; C8: inclusivity in the spectator final state is a theorem per observable, not a slogan; O10: the subtraction formalism is [A], not BPHZ-level.

**Depends on.** Ch2 (`thm:prelim-slavnov-taylor`, `prop:prelim-wilson-rules`, `lem:prelim-eikonal-identity`), Ch3 (`thm:ir-landau-momentum`, `prop:ir-power-counting`, `thm:ir-leading-regions`, `def:ir-glauber`, `prop:ir-glauber-trapping`), Ch4 (prototype), Ch7 (operator definitions that the subtraction terms must reproduce).

**Sections.**
1. `sec:method-strategy` 证明策略 — the six steps; `fig:method-flowchart`.
2. `sec:method-regions` 区域的偏序与近似子 — poset of regions; collinear and soft approximators; accuracy lemmas (`fig:method-nesting`).
3. `sec:method-gy` Grammer–Yennie 分解 — original (QED) form; collinear (Collins 2011 eqs. (11.4)–(11.6), corrected in the errata); soft; power suppression; the gluon-PDF exception (`fig:method-kg`).
4. `sec:method-ward` Ward 恒等式与 Wilson 线 — elementary, abelian, non-abelian one gluon, tree-level two-gluon with ghosts, multi-gluon (outline), collinear and soft Wilson lines (`fig:ward-identity`; `fig:soft-eikonal`, owned by Ch2).
5. `sec:method-subtraction` 减除形式体系 — definition, theorem, chains (forest analogue), one-loop Sudakov example with zero-bin.
6. `sec:method-unitarity` 幺正性：末态相互作用与软因子.
7. `sec:method-glauber` Glauber 区与围道变形 (`fig:glauber-contour`).
8. `sec:method-template` 模板定理；因子化标度与方案.

**Canonical statements.**

* **定义 `def:method-regions` — 区域的偏序** (no tag). For a (cut) graph $\Gamma$: regions $R$ = leading pinch surfaces $\pi_R$ with decomposition $(H_R,\{J_{i,R}\},S_R)$; $R'<R$ iff $\pi_{R'}\subsetneq\pi_R$ (soft minimal, hard maximal). One-loop vertex: $\pi_S\subset\pi_A$, $\pi_S\subset\pi_B$.
* **定义 `def:method-collinear-approx` — 共线近似子** (no tag). At the interface of an $A$-collinear subgraph with $H$ ($\hat k=(k^+,0,\mathbf 0_T)$): quark line $H(k)\Phi(k)\to H(\hat k)\frac14\gamma^-{\rm Tr}[\gamma^+\Phi(k)]$ (forward amplitude; check $\Phi=\slashed p\to p^+\gamma^-$); gluon line $H_\mu(k)g^{\mu\nu}J_\nu(k)\to H_\mu(\hat k)\frac{\hat k^\mu n_B^\nu}{n_B\cdot k\mp i0}J_\nu(k)+[-H_j(\hat k)J^j(k)]$, with $-i0$ for attachments to final-state lines (DIS; future-pointing Wilson line) and $+i0$ for initial-state lines (DY; past-pointing) (c_wilson §6.2, s6; VF-WL-10).
* **定义 `def:method-soft-approx` — 软近似子** (no tag). Soft gluon between $S$ (index $\mu$) and $J_A$ (index $\nu$): $S^\mu g_{\mu\nu}J_A^\nu\to S^\mu\frac{n_{A\mu}k_\nu}{n_A\cdot k\pm i0}J_A^\nu$ ($+i0$ incoming $A$ line, $-i0$ outgoing); the $n_A$ end produces a Wilson line along $n_A$ in the soft factor (VF-WL-11).
* **引理 `lem:method-collinear-accuracy` — 共线近似的精度** [A]. Near $\pi_R$, away from smaller regions, $T_R\Gamma=\Gamma[1+O(\lambda)]$. Proof: sketch (expand $H$ in $k^-,k_T$; bad components and non-K polarizations suppressed by the boost factors of `prop:ir-power-counting`). Numerical nuance (c_wilson §6.2): G-term $O(\lambda^2)$ for an on-shell massless parent, $O(\lambda)$ generically. Literature: Collins 2011 ch. 10 (Sudakov), §11.3.
* **引理 `lem:method-soft-accuracy` — 软近似的精度** [A]. Same for the soft approximator, valid only where $|k^+k^-|\gtrsim k_T^2$ (outside the Glauber region), in particular after contour deformation. Proof: sketch; remainder formula VF-WL-11 ($O(\lambda|k_T|/|k^-|)$; $O(1)$ in the Glauber region).
* **引理 `lem:method-gy` — Grammer–Yennie 分解** (数学恒等式，无标签). Collinear: $g_{\mu\nu}=K_{\mu\nu}+G_{\mu\nu}$, $K_{\mu\nu}=\frac{k_\mu w_{2\nu}}{k\cdot w_2-i0}$, $w_2=n_B$; $G_{\mu\nu}k^\nu=0$; $H\cdot G\cdot C=H\cdot(C-\frac{C^+}{k^+}k)$; soft: $K_s^{\mu\nu}=\frac{k^\mu n_A^\nu}{n_A\cdot k\pm i0}$; original QED form $b_k k_\mu k_\nu$ (`GrammerYennie1973`, as reproduced in `SenIndumathiChoudhury2019` eqs. (7)–(9)) (VF-WL-10/11). Proof: full.
* **命题 `prop:method-gy-suppression` — G 部分的幂次压低** [A]. Each collinear G-gluon beyond the minimal parton content costs $\ge\lambda$; K-gluons cost nothing; exception: a single transversely polarized gluon as the active parton ($k\cdot H=0$, G term leading, combines into $G^{+j}$ via $k^+A^j-k^jA^+$); soft G-gluons $O(\lambda)$ outside the Glauber region. Proof: sketch + numerics (c_wilson s5).
* **引理 `lem:method-ward-elementary` — 基本 Ward 恒等式** [R, R_PT]. VF-WL-6: (W1) $S(p+k)(ig\slashed kt^a)S(p)=gt^a[S(p+k)-S(p)]$; (W2) on-shell ends; (W3) $q_{1\mu}V^{\mu\nu\rho}_{abc}=gf^{abc}[(q_3^2g^{\nu\rho}-q_3^\nu q_3^\rho)-(q_2^2g^{\nu\rho}-q_2^\nu q_2^\rho)]$; (W4) ghost vertex not a pure difference; (W5) eikonal Ward identity $\frac{n\cdot k}{(n\cdot\ell+i0)(n\cdot(\ell+k)+i0)}=\frac1{n\cdot\ell+i0}-\frac1{n\cdot(\ell+k)+i0}$. Proof: full.
* **引理 `lem:method-ward-abelian` — 阿贝尔 Ward 恒等式** [R, R_PT]. On a fermion line with on-shell ends, the sum over all insertions of a scalar-polarized gluon gives $g\sum_r[\text{line with gluon }r\text{ carrying }q_r+k\text{ and colour }[T_K,T_r]]$, hence 0 in the abelian case (VF-WL-6, c_wilson §5.2). With one end at the hard vertex, $\sum_{\rm insertions}\prod_ik_{i\mu_i}H^{\mu_1\cdots\mu_m}=(\pm g)^mH_0$ (shifted kinematics); the eikonal factors appear only after the K projectors, giving the abelian Wilson line via the eikonal identity (c_wilson correction to blueprint L7.8). Proof: full.
* **命题 `prop:method-ward-one` — 单个纵向胶子的非阿贝尔 Ward 恒等式** [R, R_PT]. $k_\mu\mathcal M^\mu_a=0$ at every order when all other external partons are on shell and physically polarized. Proof: full from `thm:prelim-slavnov-taylor`.
* **命题 `prop:method-ward-tree` — 树图层次的非阿贝尔恒等式与 PDF Wilson 线的种子** [R, R_PT]. (c_wilson §5.3–5.5, VF-WL-7/8/9.) (a) $\gamma^*\to q\bar qg$: $k_\mu\mathcal A^{\mu\nu}=0$ on shell; with the antiquark leg off shell the hard part gives $-gt^aH_0$; (b) DIS: $k_\mu H^\mu_a=gt^aH_0$, and with the K projector $H_\mu\frac{k^\mu n_B^\alpha}{n_B\cdot k-i0}=W^{(1)}[\infty n_B,0]H_0$; two collinear K-gluons give exactly $(n_B\cdot k_1)(n_B\cdot k_2)W^{(2)}_{ab}[\infty n_B,0]H_0$ (path ordering from the commutator term; no ghost or three-gluon graph at this order); (c) $q\bar q\to g^*g^*$: $k_{1\mu}\mathcal A^{\mu\nu}_{ab}=\frac{g^2f^{abc}}{Q^2}(k_2^2g^{\nu\sigma}-k_2^\nu k_2^\sigma)J_{c\sigma}$; ghost term for unphysical polarizations. Proof: full (App F).
* **引理 `lem:method-ward-multi` — 多个 K 胶子的 Ward 恒等式与 Wilson 线** [A]. For $n$ K-gluons attached in all ways to $H$ whose other external lines are on-shell physical partons, the sum equals $H_0$ times the Feynman rules of a Wilson line along $n_B$ (future/past according to final/initial-state attachments); ghost contributions cancel or are absorbed into Wilson-line operators. Conditions must be stated (c_wilson §8.5). Proof: sketch — App F gives $n=1$ (`prop:method-ward-one`) and $n=2$ (tree, `prop:method-ward-tree`) in full and the inductive step in outline. Literature: Collins 2011 §11.9 (p. 416, Fig. 11.6) and §11.3.2 (pp. 407–410: the BRST classification for non-local operators is **assumed**: "no proof has been given… I will assume the result is true"; survey item 6); `CollinsSoper1982a`; `Labastida:1984gy`; `Collins:2008sg` (non-zero leading remainder of the naive K-gluon identity, needed for the gluon PDF); amplitude-level alternative `FeigeSchwartz2014`. Status: abelian [R]; $n\le2$ at tree level [R]; general non-abelian combinatorics with ghosts [A].
* **命题 `prop:method-collinear-wilson` — 共线 Wilson 线与 PDF** [A]. Summing the collinear approximation over all attachments of $A$-collinear K-gluons gives $H_0(\hat k)\otimes\Phi^W(k)$; integrating over $k^-,k_T$ at fixed $k^+=\xi P^+$ yields the bare PDF of `def:pdf-quark`/`def:pdf-gluon` with the straight light-like segment, since $W[w,\infty n_B]W[\infty n_B,0]=W[w,0]=W[w,-\infty n_B]W[-\infty n_B,0]$ for $w_T=0$ (composition and retracing, `prop:prelim-wilson-covariance`; restated for DY in Ch11 as `prop:dy-universality` — pointer). Proof: sketch.
* **命题 `prop:method-soft-wilson` — 软 Wilson 线** [A]. Soft gluons attached to $J_A$, after `def:method-soft-approx` and the Ward identity, decouple from $J_A$ and attach to a Wilson line along $n_A$ in $S=\langle0|\prod_iW_{n_i}|0\rangle$ (time orderings as appropriate). Proof: sketch.
* **定义 `def:method-subtraction` — 减除项** (no tag). $C_R\Gamma\equiv T_R(\Gamma-\sum_{R'<R}C_{R'}\Gamma)$, starting from minimal regions; $T_R$ = product of the approximators with integrations extended to the full ranges.
* **定理 `thm:method-subtraction` — 减除定理** [A]. $\Gamma=\sum_RC_R\Gamma+O(\lambda^p)$. Proof: sketch, steps: (1) accuracy near $\pi_R$; (2) key compatibility property for $R'<R$; (3) covering of the integration domain; (4) UV divergences of extended integrations = those of the operator definitions; (5) induction. **Caveat (audit, after REFDOC_ANALYSIS §2.4 OUR-2, S25):** steps (2) and (5) must not be stated termwise — individual chain terms $T_R\Gamma$ need not even be absolutely integrable (one-loop off-shell triangle: $T_{C_1}\Gamma$ is not in $L^1$ for any $\varepsilon$), and the suppression holds only for the grouped expressions $C_R\Gamma$. State the conditions explicitly: (CS1) accuracy $(1-T_{R_0})X_{R_0}$ suppressed near $\pi_{R_0}$ with $X_{R_0}=\Gamma-\sum_{R<R_0}C_R\Gamma$; (CS2) $C_R\Gamma$ suppressed near $\pi_{R_0}$ for $R\not\le R_0$; (CS3) integrability of $\Gamma$ and all $C_R\Gamma$; the theorem is the implication (CS1)–(CS3) ⇒ $\Gamma=\sum_RC_R\Gamma+O(\lambda^p)$, and the [A] concerns the verification of (CS1)–(CS3). 地位与缺口: the Sudakov form factor is treated completely in Collins 2011 ch. 10 (§10.3, §10.8); general processes [A]; CSS 1989 §10.1: "there is as yet in the literature no complete and systematic subtraction procedure in QCD… even in the case of deeply inelastic scattering" (survey item 6, quotation [txt]); no Minkowskian analogue of Weinberg's theorem (critic O10).
* **命题 `prop:method-chains` — 减除的链展开（森林公式类比）** (algebraic identity, no tag). $C_R\Gamma=\sum_{\text{chains }R_1<\dots<R_k<R}(-1)^kT_RT_{R_k}\cdots T_{R_1}\Gamma$; forests ↔ chains of nested pinch surfaces; IR forest formula for wide-angle amplitudes `Ma2020`. Proof: full (induction).
* **引理 `lem:method-soft-unitarity` — 软因子的幺正性** [R, R_def]. For an observable that does not constrain soft momenta, the soft factor summed over cuts with all Wilson lines at the same point is $\langle0|(W_{n_A}W_{n_B})^\dagger(0)(W_{n_A}W_{n_B})(0)|0\rangle=1$; in DR every graph beyond tree level is scaleless. Proof: full. Contrast: TMD soft factor $S(b_T)\ne1$ (Ch13). Logical order (critic O13): valid only after the Glauber region has been dealt with.
* **命题 `prop:method-fsi` — 末态相互作用的幺正性相消** [A]. Final-state interactions not constrained by the observable cancel in the sum over cuts (unitarity identity, VF-GLA-5): either the final-state jet is not pinched in the forward amplitude (DIS: part of $H$), or the interactions cancel by unitarity (DY spectators). Proof: sketch (Cutkosky + deformation); `LibbySterman1978a`, `CollinsSoperSterman1988`, Collins 2011 §14.4.
* **命题 `prop:method-glauber-oneloop` — 两条程函线之间的单胶子交换** [R, R_PT]. With $n_A\cdot k=k^-$, $n_B\cdot k=k^+$: for past–past lines the $k^-$ integral of $\frac{1}{(k^-+i0)(-k^++i0)(2k^+k^--k_T^2+i0)}$ vanishes for $k^+>0$ and equals $-2\pi i/(k_T^2k^+)$ for $k^+<0$; the difference of past and future $A$ lines is $\frac1{k^-+i0}-\frac1{k^--i0}=-2\pi i\delta(k^-)$ — the Glauber (Coulomb) phase, $\propto\int d^2k_T/k_T^2$ (VF-WL-12; c_wilson s6). Proof: full.
* **命题 `prop:method-glauber-deformation` — Glauber 区的围道变形判据** [A]. At fixed $k^+,k_T$: if all $k^-$ poles from $A$-collinear lines coupling to the soft gluon lie on one side, the contour can be deformed to $|k^-|\sim|k_T|$ where `lem:method-soft-accuracy` applies at the $A$ end; to leave the Glauber region altogether both light-cone components must be deformed simultaneously ($k^-$ away from the $A$-collinear poles, $k^+$ away from the $B$-collinear poles): a one-component deformation leaves $|k^+k^-|\ll k_T^2$, and the soft line's own pole limits it to $|\Delta k^\mp|\sim k_T^2/|k^\pm|$ (audit, after REFDOC_ANALYSIS §2.4 OUR-4); poles lie on one side when the relevant lines are all initial-state or all final-state; obstruction ("Glauber pinch") when both occur, as for spectator–spectator interactions (pole half-plane rule, VF-GLA-4); for inclusive observables the final-state poles are removed first by unitarity (`prop:method-fsi`; the CSS mechanism realized for DY in Ch11). Proof: sketch (blueprint S7; `prop:ir-glauber-trapping`; `fig:glauber-contour`).
* **定理 `thm:method-template` — 因子化模板定理** [A]. For an observable with collinear directions $n_A,n_B,\dots$ assume: **(H1)** its leading regions are those of `thm:ir-leading-regions` (plus Glauber regions); **(H2)** at the $H$–$J$ interfaces the collinear approximation holds and K-gluons decouple into Wilson lines (`lem:method-ward-multi`, `prop:method-collinear-wilson`); **(H3)** after contour deformation out of the Glauber region, or explicit cancellation of Glauber contributions, the soft approximation holds and soft gluons decouple (`prop:method-soft-wilson`); **(H4)** final-state interactions not constrained by the observable cancel by unitarity and the soft factor is 1 (collinear factorization) or a well-defined vacuum matrix element of Wilson lines (TMD); **(H5)** the subtraction terms coincide with the renormalized matrix elements of the operators defining the PDFs/FFs/TMDs. Then $\sigma=\sum_{ij}H_{ij}\otimes f_{i/A}\otimes f_{j/B}[\otimes S]+O(\lambda^p)$, with $H_{ij}$ computable with partonic external states (`prop:pdf-partonic-dr`). Proof: `proofsketch` (WRITER_SPEC §4.7) in which the deduction from (H1)–(H5) is written out completely; it uses `thm:method-subtraction` ([A]) to sum the subtraction terms, so the [A] reflects both that theorem and the status of the hypotheses (§0.8). 非微扰地位：MA1、MA2、MA4. The tag refers to the hypotheses; each process chapter verifies them with its own status line.
* **命题 `prop:method-scale-scheme` — 因子化标度与方案** [R, R_def]. $\mu_F$-independence of $\sigma$ + DGLAP (`thm:pdf-dglap`) ⇒ $\partial H/\partial\ln\mu_F^2=-H\otimes P$ (convolution form); scheme change $f'=Z\otimes f$, $H'=H\otimes Z^{-1}$; $\mu_R$ dependence via $\beta$. Proof: full. Logical order (C2): DGLAP first, scale independence as corollary. (M25: scale variation is a convention, not a theorem.)

**Worked examples.**
* `ex:method-dis-oneloop` — one-loop DIS on a quark in subtraction language: $C_A\Gamma^{(1)}=f^{(1)}_{q/q}\otimes{\rm Born}=-\frac{\alpha_s}{2\pi}\frac1\varepsilon P_{qq}$ (pure DR), $C_H\Gamma^{(1)}=\frac{\alpha_s}{2\pi}C_2^q$: the coefficient function *is* the subtracted graph (VF-DIS-6).
* `ex:method-sudakov-subtraction` — one-loop Sudakov form factor: $C_S\Gamma=T_S\Gamma$, $C_A\Gamma=T_A(\Gamma-T_S\Gamma)$ (zero-bin), $C_B$, $C_H\Gamma=T_H(\Gamma-\dots)$; in DR all pairwise overlaps are scaleless (c_regions §3.3, A7) so no explicit zero-bin terms survive; with cutoffs they are needed (`ex:ir-regions-toy`).
* `ex:method-ward-tree` — $q\bar q\to g^*g^*$ with both gluons longitudinal; ghost term; physical-polarization sum $=-g$ sums minus ghosts; cross-check with the $q\bar q\to gg$ cross section (VF-WL-9).
* `ex:method-glauber-oneloop` — = `prop:method-glauber-oneloop` with pole figure.

**Figures.** existing (tikz2): `fig:ward-identity`, `fig:glauber-contour` (owned); `fig:soft-eikonal` (owned by Ch2; refer back); new: `fig:method-flowchart`, `fig:method-kg` (adapt `research/c_wilson/tex/c_wilson_gy.tex`, `fig:cw-kg`), `fig:method-nesting`.

**Misconception box.** M15 (soft factor always 1), M24 (UV/IR bookkeeping), M25 (scale variation = error), C7 (Ward identities before approximations).

**Key citation keys.** `Collins2011`, `CollinsSoper1982a`, `CollinsSoperSterman1985b`, `CollinsSoperSterman1988`, `CollinsSoperSterman1989`, `Bodwin1985`, `GrammerYennie1973`, `SenIndumathiChoudhury2019`, `Labastida:1984gy`, `Collins:2008sg`, `FeigeSchwartz2014`, `Ma2020`, `ErdoganSterman2015`, `BogoliubovParasiuk1957`, `Hepp1966`, `Zimmermann1969`, `LibbySterman1978a`, `tHooft1971`, `Taylor1971`, `Slavnov1972`, `BecchiRouetStora1976`, `KugoOjima1979`, `Weinberg1965`, `CombridgeKripfganzRanft1977`, `AybatSterman2009`, `Collins2003`.

---------------------------------------------------------------------------------------------------

## Chapter 9 — DIS 的全阶动量空间证明、重夸克与核靶 / DIS to all orders in momentum space; heavy quarks; nuclear targets

`\label{ch:disall}` · `ch09_disall.tex` · **12 pp** · full

**Purpose.** First application of `thm:method-template` (one hadron, no soft factor at leading power, final-state interactions summed by unitarity); comparison with the [R, OPE] results of Ch6–Ch7 made precise (critic O7/D12: twist-2 parts agree in the sense of distributions; the pointwise x-space remainder is the content of the [A] theorem); explicit $O(\alpha_s)$ coefficient functions in $\overline{\rm MS}$ with full derivation; scale independence; DIS scheme; Collins' acknowledged gaps; heavy-quark masses (Collins 1998 theorem; schemes); nuclear targets.

**Depends on.** Ch3, Ch6–Ch8.

**Sections.**
1. `sec:disall-regions` Breit 系与领头区域 (`fig:reduced-dis`, owned by Ch3; `fig:disall-seed`).
2. `sec:disall-fsi` 末态相互作用与幺正性.
3. `sec:disall-theorem` 模板假设的验证与主定理.
4. `sec:disall-consistency` 与 OPE 结果的一致性.
5. `sec:disall-nlo` $O(\alpha_s)$ 系数函数的推导 (`fig:dis-oneloop`, owned by Ch6).
6. `sec:disall-scale` 标度无关性与 DIS 方案.
7. `sec:disall-heavy` 重夸克质量与变味方案.
8. `sec:disall-nuclear` 核靶.

**Canonical statements.**

* **定义 `def:disall-breit` — Breit 系与投影算符** (no tag). $P=(P^+,M^2/2P^+,\mathbf 0_T)$, $q=(-xP^+,Q^2/(2xP^+),\mathbf 0_T)$; $D$-dimensional projectors $\frac{F_L}x=\frac{8x^2}{Q^2}P_\mu P_\nu W^{\mu\nu}$, $\frac{F_2}x=\frac1{1-\varepsilon}[-g_{\mu\nu}+(3-2\varepsilon)\frac{4x^2}{Q^2}P_\mu P_\nu]W^{\mu\nu}$; massive-target version (VF-DIS-2).
* **命题 `prop:disall-regions` — DIS 的领头区域** [A]. Leading regions of $T^{\mu\nu}$: target-collinear subgraph + hard subgraph joined by two partons plus any number of $A^+$-polarized gluons; no soft subgraph, no final-state collinear subgraph after the sum over cuts. Proof: sketch (`thm:ir-leading-regions`, `lem:disall-fsi`; soft lines into $H$ cost $\lambda^2$). Literature: `LibbySterman1978a`, CSS 1989 §8.7.
* **引理 `lem:disall-fsi` — 末态喷注的非钳夹性** [A]. Sum over cuts = discontinuity of $T^{\mu\nu}$; lines carrying the large $q^-$ are not pinched in the forward amplitude ($k^-$ contour deformable by $O(Q^2/P^+)$), so the current jet and soft lines attached to it are part of $H$. Proof: sketch (`prop:method-fsi`).
* **命题 `prop:disall-h2` — (H2) 的验证** [A]. Collinear approximation + `lem:method-ward-multi` + `prop:method-collinear-wilson` give the PDFs of Ch7 with the straight Wilson line (future-pointing in the amplitude). Proof: sketch; seed `prop:method-ward-tree`(b).
* **命题 `prop:disall-h3h4` — (H3)(H4) 平凡成立** [A]. No soft factor at leading power; no Glauber problem (one hadron, final state summed).
* **命题 `prop:disall-h5` — (H5) 的验证** [A]. Subtraction terms $=f_{i/j}\otimes C$ with renormalized partonic PDFs; hence $C_{2,i}=\hat F_2^{(j)}\otimes(f^{\rm partonic})^{-1}$, at one loop in pure DR $C=\hat F^{(1)}+\frac1\varepsilon P\otimes\hat F^{(0)}$.
* **定理 `thm:disall-factorization` — DIS 共线因子化（动量空间，$x$ 空间逐点）** [A]. For fixed $0<x<1$ with $W^2\gg\Lambda^2$, as $Q\to\infty$:
  $$\frac{F_2(x,Q^2)}x=\sum_i\int_x^1\frac{d\xi}\xi C_{2,i}\Big(\frac x\xi,\frac{Q^2}{\mu^2},\alpha_s(\mu)\Big)f_i(\xi;\mu)+R(x,Q),$$
  similarly $F_L$, with $R=O(\Lambda^2/Q^2)$ with an $x$-dependent coefficient, non-uniform as $x\to1$ (heuristic parameter $\Lambda^2/(Q^2(1-x))$) and $x\to0$. 非微扰地位：MA1、MA2、MA4. Proof: `proofsketch` in which the deduction from `prop:disall-regions`–`prop:disall-h5` and `thm:method-template` is written out completely (WRITER_SPEC §4.7; §0.8). Point to print (audit, after REFDOC_ANALYSIS §2.4 OUR-6, S27): bounds on the forward amplitude $T^{\mu\nu}$ for real $|\omega|<1$ do not by themselves control its discontinuity. Moments follow by Cauchy estimates if the subtraction bounds hold uniformly on a complex disc $|\omega|\le\rho<1$; the fixed-$x$ statement needs the analysis of the cut graphs (sum over cuts, `lem:disall-fsi`), and uniformity fails as $x\to1$. 地位与缺口 (print): Collins 2011 §11.3.2 (pp. 407–410) — BRST classification of non-local operators assumed; naive K-gluon identity has a non-zero leading remainder (`Collins:2008sg`); complete proof in a non-gauge theory: Collins 2011 §8.9; CSS 1989 §10.1 quotation; early physical-gauge arguments `EllisEtAl1979`, `Ellis:1978sf`, `AmatiPetronzioVeneziano1978a`, `AmatiPetronzioVeneziano1978b`, `Mueller1978`, `CurciFurmanskiPetronzio1980`; physical gauges obstruct Glauber deformations (Collins 2011 §12.6) — proofs in Feynman gauge.
* **推论 `cor:disall-consistency` — 与 OPE 系数的一致性** [R, 以 OPE 为前提]. The momentum-space coefficient functions coincide with the OPE ones: at $O(\alpha_s)$ by explicit calculation exactly in $\varepsilon$ ($N\le8$; VF-DIS-13); at all orders by uniqueness (`cor:appK-pdf`), since both satisfy the same moment relations. The twist-2 parts of `thm:disall-factorization` and `thm:pdf-dis-xspace` agree as distributions; the pointwise remainder is controlled only by the [A] theorem (critic O7, D12).
* **命题 `prop:disall-nlo` — $O(\alpha_s)$ 的 $\overline{\rm MS}$ 系数函数** [R, R_PT]. (c_dis, VF-DIS-1…12.) With $\frac{F_2}x=\sum_qe_q^2\{(q+\bar q)+\frac{\alpha_s}{2\pi}[C_2^q\otimes(q+\bar q)+2C_2^g\otimes g]\}$, $\frac{F_L}x=\sum_qe_q^2\frac{\alpha_s}{2\pi}[C_L^q\otimes(q+\bar q)+2C_L^g\otimes g]$, at $\mu=Q$:
  $C_2^q=C_F[2\mathcal D_1-\frac32\mathcal D_0-(1+z)\ln(1-z)-\frac{1+z^2}{1-z}\ln z+3+2z-(\frac92+\frac{\pi^2}3)\delta(1-z)]$, $C_2^g=T_F[(z^2+(1-z)^2)\ln\frac{1-z}z-8z^2+8z-1]$, $C_L^q=2C_Fz$, $C_L^g=4T_Fz(1-z)$; general $\mu$: $+\ln(Q^2/\mu^2)P_{qi}$; the factor 2 counts quark and antiquark; gluon polarization average $1/(D-2)$. Proof: full — Born exact in $D$; virtual form factor (`prop:sudakov-oneloop`); real emission exact in $\varepsilon$ ($R_2^q$, $R_L^q$, $R_2^g$, $R_L^g$); plus-distribution expansion; pole structure ($1/\varepsilon^2$: $2-2$; $1/\varepsilon$: $-P_{qq}/C_F$ incl. $\frac32\delta$ from the virtual graph; $\delta$ coefficient $\frac72-3\zeta_2-8+\zeta_2=-(\frac92+\frac{\pi^2}3)$); mass factorization with `prop:pdf-partonic-dr`. Literature cross-checks (c_dis §12): `Vermaseren:2005qc` ($c^{(1)}_{2,\rm ns}=2C_2^q$, $c^{(1)}_{2,g}=4n_fC_2^g$), `Moch:2004xu`, `AltarelliMartinelli1978`, `BardeenEtAl1978` (via the citations), `FurmanskiPetronzio1982`.
* **命题 `prop:disall-scale` — 标度无关性** [R, R_PT]. $\partial(F_2/x)/\partial\ln\mu_F^2=O(\alpha_s^2)$; $\partial F_2/\partial\ln\mu_R^2=-\frac{\beta_0}2a^2\sum e_q^2[C_2^q\otimes(q+\bar q)+2C_2^g\otimes g]$, $a=\alpha_s/2\pi$; $F_L$ $\mu$-independent at $O(a)$ (VF-DIS-10). Proof: full (Mellin space).
* **命题 `prop:disall-dis-scheme` — DIS 方案** [R, R_def]. $q_i^{\rm DIS}=q_i+a[C_2^q\otimes q_i+C_2^g\otimes g]$, $g^{\rm DIS}=g-a[C_2^q\otimes\Sigma+2n_fC_2^g\otimes g]$ (gluon fixed by the momentum sum rule; attribution `DiemozEtAl1988` recalled by c_dis — cite with "(see)"); $C_{2}^{\rm DIS}=\ln(Q^2/\mu^2)P$; $P^{(1),\rm DIS}_{\rm NS}=P^{(1),\overline{\rm MS}}_{\rm NS}-\frac{\beta_0}2C_2^q$; $C_L$ scheme independent at $O(\alpha_s)$ (VF-DIS-11). Proof: full.
* **定理 `thm:disall-heavy` — 含重夸克质量的因子化（Collins 1998）** [A]. Keeping heavy-quark masses in the hard part, with heavy-quark PDFs in the CWZ/ACOT framework, $F=\sum_if_i\otimes\hat C_i(m_h/Q,Q/\mu)$ with power-suppressed corrections "uniformly suppressed by a power of $\Lambda/Q$, independently of… $M$" (`Collins1998b` abstract, survey item 27). Proof: sketch. Schemes FFNS, ZM-VFNS, GM-VFNS (ACOT, S-ACOT, TR, BMSN, FONLL) are equivalent prescriptions to the order computed (`CollinsWilczekZee1978`, `AivazisEtAl1994`, `Aivazis:1993kh`, `Kramer:2000hn`, `Thorne:1997ga`, `Buza:1996wv`, `Forte:2010ta`). Caveat for hadron–hadron (Collins 2011 §14.6, pp. 569–570: massive incoming partons — "a bad idea"). 非微扰地位：MA1、MA2 (MA: audit).
* **命题 `prop:disall-nuclear` — 核靶上的 DIS** [A]. Leading power: as DIS on a hadron (nuclear PDFs); nuclear-enhanced twist-4 terms $\propto A^{1/3}\Lambda^2/Q^2$ [P] (`QiuSterman1991a`, `Luo:1993ui`, `Luo:1994np`); BBL: factorization requires energy ≫ a scale growing with the target length (`Bodwin:1988fs`, abstract); leading-twist shadowing via DDIS factorization (`Frankfurt:2011cs`); saturation regime at small $x$ [C] (Ch16). Global nPDF fits assume leading-twist factorization (`Eskola:2021nhw`, `Kovarik:2015cma`, `AbdulKhalek:2022fyi`). 非微扰地位：MA1、MA2 (MA: audit).

**Worked examples.**
* `ex:disall-nlo` — the full derivation of `prop:disall-nlo` (main worked calculation of the chapter, ~3 pp; c_dis `dis_oneloop.tex` is a ready Chinese draft — adapt, relabel `fig:dis1l-diagrams` → use `fig:dis-oneloop`).
* `ex:disall-gluon` — photon–gluon fusion: $\hat F_2^g/(ze_q^2)=\frac{\alpha_s}{2\pi}(\frac{\mu^2}{Q^2})^\varepsilon[-\frac2\varepsilon P_{qg}+2C_2^g]$, poles from both collinear configurations; average-over-2 shift.
* `ex:disall-heavy-lo` — LO $\gamma^*g\to Q\bar Q$ with full mass dependence and its $m\to0$ limit $\ln(Q^2/m^2)P_{qg}$ = ACOT subtraction **(formula to be derived by the writer; not verified by an agent)**.

**Figures.** referred back to: `fig:reduced-dis` (Ch3), `fig:dis-oneloop` (Ch6); new, required since the audit: `fig:disall-seed` (adapt `fig:cw-dis-seed`), `fig:disall-heavy`.

**Misconception box.** M4, M25, M26 (Callan–Gross is LO only: $C_L^q=2C_Fz$).

**Key citation keys.** `LibbySterman1978a`, `Collins2011`, `CollinsSoperSterman1989`, `Collins:2008sg`, `EllisEtAl1979`, `Ellis:1978sf`, `AmatiPetronzioVeneziano1978a`, `AmatiPetronzioVeneziano1978b`, `Mueller1978`, `Mueller:1981sg`, `CurciFurmanskiPetronzio1980`, `BardeenEtAl1978`, `AltarelliMartinelli1978`, `FurmanskiPetronzio1982`, `Vermaseren:2005qc`, `Moch:2004xu`, `DiemozEtAl1988`, `CollinsWilczekZee1978`, `AivazisEtAl1994`, `Aivazis:1993kh`, `Collins1998b`, `Kramer:2000hn`, `Thorne:1997ga`, `Buza:1996wv`, `Forte:2010ta`, `QiuSterman1991a`, `Luo:1993ui`, `Luo:1994np`, `Bodwin:1988fs`, `BodwinBrodskyLepage1981`, `Frankfurt:2011cs`, `Eskola:2021nhw`, `Kovarik:2015cma`, `AbdulKhalek:2022fyi`, `EllisStirlingWebber1996`.

---------------------------------------------------------------------------------------------------

## Chapter 10 — 其他共线过程：单举湮灭、SIDIS、光生、极化与横度 / Other collinear processes: SIA, SIDIS, photoproduction, polarized processes, transversity

`\label{ch:coll}` · `ch10_coll.tex` · **12 pp** · full

**Purpose.** Give each remaining collinear process class a home (critic §4 items 3, 4, 8, 11): one observed hadron in $e^+e^-$ (FFs), collinear SIDIS (PDF ⊗ FF), photoproduction and photon structure (direct [A], resolved [C], diffractive resolved [V]), longitudinally polarized DIS and the axial anomaly (scheme dependence of $\Delta\Sigma$/$\Delta G$), transversity. Each statement is a verification of `thm:method-template` or an OPE statement.

**Depends on.** Ch6–Ch9.

**Sections.**
1. `sec:coll-sia` $e^+e^-\to hX$ 与碎裂函数 (`fig:coll-sia`).
2. `sec:coll-sidis` 共线半单举 DIS (`fig:coll-sidis`).
3. `sec:coll-photo` 光生过程与光子结构 (`fig:coll-photoproduction`).
4. `sec:coll-polarized` 纵向极化：$g_1$、轴反常与方案依赖.
5. `sec:coll-transversity` 横向极化与横度分布.

**Canonical statements.**

* **定义 `def:coll-sia` — 单举湮灭的运动学** (no tag). $z=2p_h\cdot q/q^2$; $\frac{d\sigma}{dz\,d\cos\theta}=\frac38(1+\cos^2\theta)\frac{d\sigma_T}{dz}+\frac34\sin^2\theta\frac{d\sigma_L}{dz}$, so that $\frac{d\sigma}{dz}=\frac{d\sigma_T}{dz}+\frac{d\sigma_L}{dz}$ (VF-MISC-5; angular weights checked by the audit; cf. `NasonWebber1994`).
* **命题 `prop:coll-sia-regions` — SIA 的领头区域** [A]. Hard vertex, jet containing $h$, other jets, soft subgraph; Glauber regions not pinched (all collinear lines outgoing); soft gluons and unobserved jets cancel by unitarity; soft factor 1.
* **定理 `thm:coll-sia` — $e^+e^-\to hX$ 的因子化** [A]. $\frac{d\sigma^h}{dz}=\sum_i\int_z^1\frac{dy}y\hat\sigma_i(y,\frac{Q^2}{\mu^2},\alpha_s(\mu))d_{h/i}(\frac zy;\mu)+$ power corrections; $\sigma_L$ receives $1/Q$ corrections (`BenekeBraunMagnea1997`); the power in general [C]. 非微扰地位：MA1、MA2. Proof: deduction from `thm:method-template`; `CollinsSoper1982a`, `Mueller1978` (cut vertices), Collins 2011 §12.5–12.8.
* **注 `rem:coll-sia-nlo` — 系数函数与检验**. $O(\alpha_s)$ $\overline{\rm MS}$ coefficient functions **(literature: `AltarelliEtAl1979`, `BaierFey1979`, `RijkenVanNeerven1996`, `RijkenVanNeerven1997`, `NasonWebber1994`; to verify — not computed by an agent)**; energy sum rule $\sum_h\int dz\,z\,\frac{d\sigma^h}{dz}=2\sigma_{\rm tot}$ returns `cor:ee-R-alphas`; analytic continuation from DIS (`CurciFurmanskiPetronzio1980`) with $\pi^2$ terms from $(-q^2)^{-\varepsilon}$; the collinear pole of the quark spectrum (`ex:ee-quark-spectrum`) is absorbed into $d_{h/q}$.
* **定理 `thm:coll-sidis` — 共线 SIDIS 的因子化** [A]. For $P_{hT}$ integrated (or $P_{hT}\sim Q$): $d\sigma=\sum_{ij}f_{i/H}\otimes d\hat\sigma_{ij}\otimes d_{h/j}+\dots$; matching to TMD factorization (W + Y) in Ch13. Proof: deduction; Collins 2011 §12.14, `Graudenz1994` (NLO), `Meng:1995yn`, `Nadolsky:1999kb`. 非微扰地位：MA1、MA2 (MA: audit).
* **定理 `thm:coll-direct-photo` — 直接光生与光子结构函数** [A]. Direct photoproduction behaves like DIS (one hadron); the proof "would appear to apply also to direct photo-production" (`Collins1998a` conclusions, [txt]). 非微扰地位：MA1、MA2 (MA: audit).
* **命题 `prop:coll-photon-sf` — 光子结构函数的点状部分** [R, 以 OPE 为前提]. At large $Q^2$ the point-like part of $F_2^\gamma$ is computable (inhomogeneous evolution; `Witten:1977ju`, NLO `Bardeen:1978hg`); the hadronic component is non-perturbative. 非微扰地位：MA0、MA3、MA4 (MA: audit).
* **猜想 `conj:coll-resolved-photo` — 分辨光生** [C]. Resolved photoproduction is effectively hadron–hadron with coloured final states; the separation direct/resolved is ambiguous beyond LO (`Collins1998a`, `Klasen:2002xb`).
* **命题 `prop:coll-diffractive-photo` — 衍射光生中的因子化破坏** [V]. The statement is about **resolved** diffractive photoproduction, which is hadron–hadron-like (survey item 28; c_glauber §3.6): standard factorization with the DDIS diffractive PDFs fails (H1: dijet photoproduction must be scaled by ≈0.5, "first clear observation of QCD hard scattering factorisation breaking at HERA", `H1:2007jtx`; ZEUS `ZEUS:2007uvk`; `Klasen:2008ah`: global suppression 0.42–0.71, or resolved-only suppression by about 3). Experimental, not a perturbative counterexample. **Direct** diffractive photoproduction is covered in principle by Collins' DDIS proof (`thm:break-ddis`, Ch17 — pointer); H1's suppression also of the direct component is an unresolved tension (ZEUS differs) — say so, without a tag of its own.
* **命题 `prop:coll-luxqed` — 质子的光子分布** [A]. Determined model-independently as an integral over proton structure functions (`Manohar:2016nzj`, `Manohar:2017eqh`). 非微扰地位：MA0、MA4 (MA: audit).
* **定义 `def:coll-g1` — 极化结构函数** (no tag). Antisymmetric part of $W^{\mu\nu}$ with $g_1,g_2$; $\varepsilon^{0123}=+1$ (VF-CONV-10); spin four-vector conventions.
* **定理 `thm:coll-g1-moments` — $g_1$ 的奇数矩** [R, 以 OPE 为前提]. Odd moments of $g_1$ are given by the OPE with axial twist-2 operators; first moment: non-singlet → Bjorken (`thm:dis-bjorken`); singlet: $\Delta\Sigma$ and $\Delta G$ mix through the axial anomaly; the split is scheme dependent (`AltarelliRoss1988`, `CarlitzCollinsMueller1988`, `Kodaira1980`, `Larin:1993tq`). 非微扰地位：MA0、MA3、MA4 (MA: audit).
* **命题 `prop:coll-anomaly-scheme` — 一阶矩的方案依赖** [R, R_PT]. The first moment of the $\gamma^*g$ box contribution to $g_1$ differs between HVBM and anticommuting-$\gamma_5$ treatments, i.e. between schemes for $\Delta\Sigma$ (critic §6 example) **(the explicit numbers must be derived by the writer; not verified by an agent)**. Proof: full one-loop computation (App I).
* **命题 `prop:coll-ellis-jaffe` — Ellis–Jaffe 求和规则作为预言** [V]. It assumes $\Delta s=0$ (and negligible gluon contribution); violated by data (EMC "spin crisis": `EMC1988`). `EllisJaffe1974`.
* **猜想 `conj:coll-bc` — Burkhardt–Cottingham 求和规则** [C]. $\int_0^1g_2\,dx=0$; assumes no $J=0$ fixed pole or $\delta(x)$ term; holds at $O(\alpha_s)$ in PT (`BurkhardtCottingham1970`).
* **命题 `prop:coll-ww` — Wandzura–Wilczek 关系的一般失效** [V]. $g_2=g_2^{\rm WW}$ fails in general because of genuine twist-3 $\bar qGq$ terms (`WandzuraWilczek1977`; critic B24).
* *(Audit: polarized Drell–Yan and $A_{LL}$ in hadron collisions moved to Ch11 as `thm:dy-polarized` and `conj:dy-polarized-jets`, because both rest on Ch11 results.)*
* **定义 `def:coll-transversity` — 横度分布** (no tag). $h_1$ chiral-odd; absent from inclusive DIS at leading twist; accessible via SIDIS Collins effect (TMD, Ch13), dihadron FFs (collinear), transversely polarized DY.
* **命题 `prop:coll-transversity-evolution` — 横度的演化** [R, R_def] for "no gluon mixing" (helicity-flip by two units has no gluon counterpart for a spin-½ target, any order); LO kernel $\Delta_TP_{qq}=C_F[\frac{2z}{(1-z)_+}+\frac32\delta(1-z)]$ (VF-POL-3, status C: standard, `ArtruMekhfi1990`; internal consistency checked by the audit — the writer re-derives it or hedges 「（待核实）」). 非微扰地位：MA0（强子态） (MA: audit).
* **命题 `prop:coll-soffer` — Soffer 不等式** [R, R_PT] at LO, in the following restricted form (audit): if $|h_1|\le\frac12(f_1+g_1)$ holds at a scale $\mu_0$ for LO-evolved densities, LO evolution preserves it for $\mu>\mu_0$ (`Soffer1995`; critic B24). Remark (print): the inequality itself follows only from the positive density-matrix (number-density) interpretation, a heuristic (`rem:pdf-number-density`); for $\overline{\rm MS}$ densities it is not a theorem and is scheme dependent beyond LO — the same caveats as `conj:pdf-positivity` (C13; frontier/others §7: do not state Soffer-type bounds as theorems).
* **注 `rem:coll-christ-lee`** — inclusive DIS transverse single-target-spin asymmetry vanishes at one-photon exchange by T invariance (`ChristLee1966`).

**Worked example.** `ex:coll-sia-lo` — LO $e^+e^-\to hX$: $\frac{d\sigma^h}{dz}=\frac{4\pi\alpha^2}{3s}N_c\sum_qe_q^2[d_{h/q}(z)+d_{h/\bar q}(z)]$ (VF-MISC-5); check $\sum_h\int dz\,z\frac{d\sigma^h}{dz}=2\sigma_{\rm tot}$ at LO from the momentum sum rule; angular distribution $1+\cos^2\theta$.

**Figures.** new: `fig:coll-sia`, `fig:coll-sidis`, `fig:coll-photoproduction`; optional `fig:coll-transversity`.

**Misconception box.** "Inclusive DIS has transverse SSAs from FSI" (Christ–Lee); M23 (timelike = spacelike kernels); "diffractive PDFs are universal" (only DDIS; Ch17).

**Key citation keys.** `CollinsSoper1982a`, `Mueller1978`, `AltarelliEtAl1979`, `BaierFey1979`, `RijkenVanNeerven1996`, `RijkenVanNeerven1997`, `NasonWebber1994`, `BenekeBraunMagnea1997`, `CurciFurmanskiPetronzio1980`, `GribovLipatov1972b`, `Graudenz1994`, `Meng:1995yn`, `Nadolsky:1999kb`, `Collins2011`, `Witten:1977ju`, `Bardeen:1978hg`, `Klasen:2002xb`, `Collins1998a`, `H1:2007jtx`, `ZEUS:2007uvk`, `Klasen:2008ah`, `Manohar:2016nzj`, `Manohar:2017eqh`, `Bjorken1966`, `EllisJaffe1974`, `EMC1988`, `Kodaira1980`, `AltarelliRoss1988`, `CarlitzCollinsMueller1988`, `LarinVermaseren1991`, `Larin:1993tq`, `BurkhardtCottingham1970`, `WandzuraWilczek1977`, `RalstonSoper1979`, `JaffeJi1991`, `JaffeJi1992`, `Soffer1995`, `ArtruMekhfi1990`, `MertigVanNeerven1996`, `Vogelsang1996`, `AltarelliForteRidolfi1998`, `ChristLee1966`, `MeleNason1991`, `CacciariGrecoNason1998`.

---------------------------------------------------------------------------------------------------

## Chapter 11 — Drell–Yan 过程与强子—强子碰撞 / Drell–Yan and hadron–hadron collisions

`\label{ch:dy}` · `ch11_dy.tex` · **14 pp** · full

**Purpose.** Verify `thm:method-template` for inclusive DY, where (H3) — the Glauber region — is genuinely new; give the CSS/Bodwin/Collins argument in structured form with an honest status paragraph (Collins 2011 §14.4.8 "Issues remaining"); an explicit abelian model in which the spectator Glauber phase cancels by unitarity; the one-loop $\overline{\rm MS}$ coefficient functions (verified against the literature); other colour-singlet processes [A]; coloured final states [C]; higher twist.

**Depends on.** Ch3, Ch7, Ch8 (esp. `def:ir-glauber`, `prop:method-glauber-deformation`, `lem:method-soft-unitarity`, `prop:method-glauber-oneloop`), Ch9.

**Sections.**
1. `sec:dy-born` 运动学与 Born 截面.
2. `sec:dy-regions` 领头区域：初态与末态相互作用 (`fig:reduced-dy`, owned by Ch3; `fig:glauber-exchange`).
3. `sec:dy-glauber` Glauber 问题及其在单举 DY 中的解决.
4. `sec:dy-model` 阿贝尔模型：旁观者 Glauber 相位的显式相消 (`fig:dy-abelian-model`, required since the audit).
5. `sec:dy-theorem` 主定理与其地位.
6. `sec:dy-nlo` $O(\alpha_s)$ 系数函数 (`fig:dy-oneloop`).
7. `sec:dy-other` 其他强子—强子过程.
8. `sec:dy-twist` 高扭度：$1/Q^2$ 处的广义因子化及其在更高幂次的失效.

**Canonical statements.**

* **定义 `def:dy-kin` — DY 运动学** (no tag). $A(P_A)+B(P_B)\to\gamma^*(q)+X$, $\tau=Q^2/s$, $y=\frac12\ln(q^+/q^-)$, $x_{A,B}=\sqrt\tau e^{\pm y}$; normalization through the master formula $\hat s\frac{d\hat\sigma}{dQ^2}=\frac{2\alpha^2}{3Q^2}\int d\Phi_{\gamma^*X}\langle-g_{\mu\nu}H^\mu H^{\nu*}\rangle$, lepton tensor $\int d\Phi_2L_{\mu\nu}=\frac1{6\pi}(q_\mu q_\nu-q^2g_{\mu\nu})$ (VF-DY-2).
* **命题 `prop:dy-born` — Born 截面** [R, R_PT]. $\frac{d\sigma}{dQ^2dy}=\frac{4\pi\alpha^2}{3N_cQ^2s}\sum_qe_q^2[q(x_A)\bar q(x_B)+\bar q(x_A)q(x_B)]$; $\hat\sigma(q\bar q\to\ell^+\ell^-)=\frac{4\pi\alpha^2e_q^2}{3N_c\hat s}$; Jacobian 1; Drell–Yan scaling (VF-DY-1). Proof: full.
* **命题 `prop:dy-regions` — DY 的领头区域** [A]. $H$ (one per side of the cut), $J_A$, $J_B$ (incl. spectators), soft subgraph connecting $J_A$, $J_B$, plus Glauber exchanges, in particular between spectators; initial- vs final-state interactions. Proof: sketch (`thm:ir-leading-regions`).
* **命题 `prop:dy-glauber-pinch` — 单个割图中的 Glauber 钳夹** [R, R_PT] (one-loop explicit). For an exchange between an incoming active parton and an outgoing spectator of the same hadron (or between spectators) the $k^-$ poles lie on both sides; the contour is trapped at $|k^-|\sim k_T^2/p^+$ (`prop:ir-glauber-trapping`; c_dy G-iii: lifting the contour changes the value). Proof: full.
* **引理 `lem:dy-fsi` — 旁观者末态相互作用的幺正性相消** [A]. After summing over all final-state cuts of the spectator systems (inclusive in $X$), interactions after the hard scattering cancel: the sum over cuts of final-state interactions equals the uncut subgraph with the interactions removed. Proof: sketch; `CollinsSoperSterman1985b`, `CollinsSoperSterman1988`, `Bodwin1985` (+ erratum), Collins 2011 §14.4 (follows CSS 1988 "with some important improvements and with correction of errors… supersedes Bodwin 1985 and CSS 1985a", p. 553, [txt]); LCPT version `Diehl:2015bca` §4.
* **命题 `prop:dy-deformation` — 移除末态极点后的围道变形** [A]. The remaining $k^-$ poles of $A$-collinear lines coupling to a soft gluon are initial-state and lie on one side: deform out of the Glauber region (Collins 2011 §14.4.1 steps: region decomposition, sum over cuts, deformation "away from initial-state singularities" with final-state ones crossed but cancelled after the sum over cuts, Grammer–Yennie approximant with **past-pointing** Wilson lines, Ward identities). Proof: sketch; `AybatSterman2009` (phases with initial-state partons).
* **引理 `lem:dy-soft` — 软因子为 1** [A]. The soft gluons decouple into past-pointing Wilson lines; for the $q_T$-integrated cross section T invariance (Collins 2011 §13.17) equates past- and future-pointing soft factors and unitarity gives 1 (`lem:method-soft-unitarity`; Collins 2011 §14.4.6). Bodwin–Brodsky–Lepage phases "do not break factorization; rather they get moved into the parton densities" (§14.4.7, [txt]).
* **命题 `prop:dy-universality` — DY 与 DIS 的共线 PDF 是同一对象** [R, R_def]. For $w=(0^+,w^-,\mathbf 0_T)$: $W[w,-\infty n_B]W[-\infty n_B,0]=W[w,0]=W[w,\infty n_B]W[\infty n_B,0]$ (composition and retracing). Proof: full. (Contrast: TMD staples do not collapse, Ch13.)
* **定理 `thm:dy-factorization` — 单举 DY 的共线因子化** [A].
  $$\frac{d\sigma}{dQ^2dy}=\sum_{ij}\int_{x_A}^1\frac{d\xi_A}{\xi_A}\int_{x_B}^1\frac{d\xi_B}{\xi_B}f_{i/A}(\xi_A;\mu)f_{j/B}(\xi_B;\mu)\,\mathcal H_{ij}\Big(\frac{x_A}{\xi_A},\frac{x_B}{\xi_B},\frac Q\mu,\alpha_s(\mu)\Big)+O\Big(\Big(\frac\Lambda Q\Big)^p\Big),$$
  $p$ not fixed by the proof ([C]; expected 2, renormalon analyses `BenekeBraun1995b`); 非微扰地位：MA1、MA2、MA4. Proof: `proofsketch` in which the deduction from `prop:dy-regions`–`prop:dy-universality` and `thm:method-template` is written out completely (WRITER_SPEC §4.7; §0.8). **Status paragraph (print in substance):** 「状态 [A]。CSS (1985, 1988) 与 Bodwin (1985) 给出了全阶论证的关键步骤（Glauber 区的围道变形、末态相互作用的幺正性相消、软因子为 1）；Collins (2011) §14.4 在 CSS 1988 基础上改进并纠正了若干错误。§14.4.8 'Issues remaining' 列出：(i) 证明依赖微扰论的动量分类，非微扰的'分级快度' Glauber 交换（多周边、类 Regge）未被覆盖；(ii) Feynman 规范下领头区域不完备（额外的不连通硬散射，须对图求和后相消，Labastida–Sterman 1985）；(iii) '现有真正的证明显然是令人生畏的'。Rothstein–Stewart (2016) 的 Glauber 算符框架复现了旁观者相位的相消，但'单独来看远不是因子化的证明'，其宣布的完整 SCET 证明截至 2026 年 10 月尚未发表。没有已知的领头幂次反例；NNLO（及更高阶）计算与实验一致。」 (survey item 8.)
* **命题 `prop:dy-abelian-model` — 阿贝尔模型中旁观者 Glauber 相位的相消** [P]. (c_dy §7, VF-DY-13.) In an abelian theory with massive vector boson and eikonal spectators: (G-i) spectator–spectator exchanges sum to $e^{i\chi(b)}$, $\chi(b)=-\frac{g_Ag_B}{2\pi}K_0(m|b|)$ (real); (G-ii) the phase cancels in any cross section inclusive in the spectators' relative transverse momentum, order by order ($O(g^{2n})$: $\sum_j\frac{(i\chi)^j}{j!}\frac{(-i\chi)^{n-j}}{(n-j)!}=0$) and to all orders ($|e^{i\chi}|^2=1$), including $q_T$ spectra at leading power; (G-iii) the spectator–spectator Glauber region is trapped; (G-iv) the active–spectator exchange is not trapped in $k^+$ and belongs to the $A$-collinear subgraph with a past-pointing Wilson line. Not shown: non-abelian case, all-order region analysis, power corrections, measured hadrons. Proof: full `proof` of the model statement (residues, eikonal identity, Parseval); the [P] records that the QCD claim is established only in this model (§0.8).
* **命题 `prop:dy-nlo` — $O(\alpha_s)$ 的 $\overline{\rm MS}$ 系数函数** [R, R_PT]. (c_dy, VF-DY-8.) $\frac{d\sigma}{dQ^2}=\frac{\sigma_0}s\sum_qe_q^2\int dx_1dx_2dz\,\delta(x_1x_2z-\tau)\{[q\bar q+\bar qq]\Delta_{q\bar q}(z)+[g(q+\bar q)+(q+\bar q)g]\Delta_{qg}(z)\}$, $\sigma_0=\frac{4\pi\alpha^2}{3N_cQ^2}$,
  $\Delta_{q\bar q}=\delta(1-z)+\frac{\alpha_s}{2\pi}\{C_F[4(1+z^2)\mathcal D_1-2\frac{1+z^2}{1-z}\ln z+(\frac{2\pi^2}3-8)\delta(1-z)]+2P_{qq}\ln\frac{Q^2}{\mu_F^2}\}$, $\Delta_{qg}=\frac{\alpha_s}{2\pi}\{T_F[(z^2+(1-z)^2)\ln\frac{(1-z)^2}z+\frac12+3z-\frac72z^2]+P_{qg}\ln\frac{Q^2}{\mu_F^2}\}$ (product convention for $(1+z^2)\mathcal D_1$; whole-term plus would change the $\delta$ coefficient by $7C_F$); no $\mu_R$ dependence at this order. Proof: full — matrix elements, $D$-dimensional phase space, real exact in $\varepsilon$, timelike form factor, Laurent table, origin of $\frac{2\pi^2}3=-\frac{\pi^2}2+\frac{\pi^2}6+\pi^2$, mass factorization (two PDFs ⇒ $2P_{qq}$; $qg$ channel subtraction $f_{\bar q/g}\otimes\hat\sigma_{q\bar q}$). Literature: agreement with `Duhr:2020sdp` (ancillary files) incl. $\mu_F$ terms; threshold constant `Moch:2005ky`; form factor `MochVermaserenVogt2005`; first NLO: `AltarelliEllisMartinelli1979` (DIS scheme — attribution of the $\overline{\rm MS}$ form must be phrased carefully), `KubarAndrePaige1979`; NNLO `HambergVanNeervenMatsuura1991`.
* **命题 `prop:dy-scale` — $\mu_F$ 无关性** [R, R_PT]. $d\sigma/d\ln\mu_F^2=O(\alpha_s^2)$ (Mellin exact; $x$-space numerics $10^{-13}$) (VF-DY-11).
* **注 `rem:dy-dis-scheme`** — DIS-scheme DY: $\Delta^{\rm DIS}_{q\bar q}=C_F[(1+\frac{4\pi^2}3)\delta(1-z)+2(1+z^2)\mathcal D_1+3\mathcal D_0-6-4z]$, $\Delta^{\rm DIS}_{qg}=T_F[(z^2+(1-z)^2)\ln(1-z)+\frac32-5z+\frac92z^2]$; $\Delta^{\overline{\rm MS}}_{q\bar q}-2C_2^q=\Delta^{\rm DIS}_{q\bar q}$, $\Delta^{\overline{\rm MS}}_{qg}-C_2^g=\Delta^{\rm DIS}_{qg}$ verified to $10^{-30}$ (critic c2; VF-DY-10): universality of PDFs between DIS and DY at one loop.
* **定理 `thm:dy-colour-singlet` — 色单态末态** [A]. $W$, $Z$, Higgs (gluon fusion via the heavy-top effective vertex or full theory), dibosons: the proof of `thm:dy-factorization` applies unchanged. Literature for the hard functions: `AltarelliEllisMartinelli1979`, `Dawson1991`, `DjouadiSpiraZerwas1991`, `HarlanderKilgore2002`, `AnastasiouEtAl2015`. 非微扰地位：MA1、MA2 (MA: audit).
* **定理 `thm:dy-polarized` — 极化 Drell–Yan** [A]. (Moved from Ch10 by the audit; formerly “thm:coll-polarized-dy”（已废弃）.) Longitudinally and transversely polarized DY factorize as unpolarized DY (`thm:dy-factorization`), with helicity and transversity PDFs (`def:pdf-polarized`); transverse: `RalstonSoper1979`, `JaffeJi1991`. 非微扰地位：MA1、MA2、MA4 (MA: audit). Proof: sketch (the proof of `thm:dy-factorization` with spin projectors).
* **猜想 `conj:dy-coloured-final` — 强子对撞中有色末态的共线因子化** [C]. Single-inclusive hadrons and jets at large $p_T$ and heavy-quark pairs: the factorized form is universally used but unproven. Evidence/obstructions: Collins 2011 §14.7 ("relative lack of detailed proofs… One notable exception is Nayak, Qiu, and Sterman (2005)"); `Diehl:2015bca` §5 (absence of Glauber effects not proven for coloured final states); `Collins:1985gm` (heavy quarks: "an analysis at all orders… is needed to reliably establish this conjecture"); `AybatSterman2009` (outline); `CataniDeFlorianRodrigo2012` §8 (possible N3LO issue); NLO heavy quarks `NasonDawsonEllis1988`; jets `Kang:2016mcy` (semi-inclusive jet function). Survey item 9; critic O14.
* **猜想 `conj:dy-polarized-jets` — 极化强子对撞中的 $A_{LL}$（喷注、$\pi^0$）** [C]. (Moved from Ch10 by the audit; formerly “conj:coll-all-jets”（已废弃）.) Inherits `conj:dy-coloured-final`.
* **定理 `thm:dy-higher-twist` — $1/Q^2$ 处的广义因子化** [A]. Leading power corrections are twist 4 and factorize in a generalized form (`QiuSterman1991a`, `QiuSterman1991b`); nuclear double scattering (`Kastella:1989ux`). 非微扰地位：MA1、MA2 (MA: audit).
* **命题 `prop:dy-twist6-failure` — 更高幂次的因子化失效** [V]. Factorization holds at $m^2/s$ but fails at $m^4/s^2$ in a scalar-quark model (`Basu:1984ba`); CSS 1989 §10.2: two-loop non-cancellation at $m^4/s^2$ in DY; BBL 1995 §VI: "Beyond that order, factorization is known to fail" (survey items 8, 21).

**Worked examples.** `ex:dy-nlo` (full derivation; c_dy `dy_oneloop.tex` is a ready Chinese draft — adapt; its `fig:dy1l-diagrams` → use `fig:dy-oneloop`); `ex:dy-threshold` (VF-DY-14; large-$N$: $\Delta_{q\bar q,N}=1+aC_F[4\ln^2\bar N+8\zeta_2-8]+O(\ln N/N)$, $a=\alpha_s/2\pi$; leads to Ch12); `ex:dy-glauber-model` (= `prop:dy-abelian-model` with FFT illustration).

**Figures.** existing (tikz2): `fig:dy-oneloop`, `fig:glauber-exchange` (owned); `fig:reduced-dy` (owned by Ch3; refer back); new, required since the audit: `fig:dy-abelian-model` (adapt `research/c_dy/dy_oneloop.tex`, `fig:dy1l-glauber`).

**Misconception box.** M7 (Glauber cancels in every inclusive cross section), M25, "the soft factor is 1 for $q_T$-differential DY" (no: Ch13).

**Key citation keys.** `DrellYan1970`, `AltarelliEllisMartinelli1979`, `KubarAndrePaige1979`, `HambergVanNeervenMatsuura1991`, `Duhr:2020sdp`, `Moch:2005ky`, `MochVermaserenVogt2005`, `BodwinBrodskyLepage1981`, `Bodwin:1988fs`, `CollinsSoperSterman1983`, `Collins:1981tt`, `Collins:1983ju`, `Bodwin1985`, `CollinsSoperSterman1985b`, `CollinsSoperSterman1988`, `CollinsSoperSterman1989`, `Lindsay:1982pu`, `Lindsay:1982gd`, `Brandt:1988xt`, `Collins2011`, `Diehl:2015bca`, `AybatSterman2009`, `RothsteinStewart2016`, `Labastida:1984gy`, `Landshoff:1971zu`, `Henyey:1974zs`, `Cardy:1974vq`, `DeTar:1974vx`, `Collins:1985gm`, `NayakQiuSterman2005b`, `CataniDeFlorianRodrigo2012`, `Kang:2016mcy`, `NasonDawsonEllis1988`, `QiuSterman1991a`, `QiuSterman1991b`, `Kastella:1989ux`, `Basu:1984ba`, `BodwinBraatenLepage1995`, `Dawson1991`, `DjouadiSpiraZerwas1991`, `HarlanderKilgore2002`, `AnastasiouEtAl2015`, `BenekeBraun1995b`.

---------------------------------------------------------------------------------------------------

## Chapter 12 — 阈值重求和与重新因子化 / Threshold resummation and refactorization

`\label{ch:thr}` · `ch12_thr.tex` · **8 pp** · short format

**Purpose.** As $z=Q^2/\hat s\to1$ the hard coefficient itself refactorizes into hard × soft (× jet for DIS); Mellin-space exponentiation; the one-loop check against `prop:dy-nlo`; prescriptions (Landau pole); SCET momentum-space version; NLP status.

**Depends on.** Ch4 (cusp), Ch9, Ch11.

**Sections.** 1. `sec:thr-limit` 阈值极限与 Mellin 空间; 2. `sec:thr-refactorization` 重新因子化定理 (`fig:thr-kinematics`); 3. `sec:thr-check` 单圈检验; 4. `sec:thr-prescriptions` Landau 极点与处方 (`fig:thr-mellin`); 5. `sec:thr-nlp` 次领头幂次.

**Canonical statements.**

* **定义 `def:thr-limit` — 部分子阈值与强子阈值** (no tag). Partonic threshold $z\to1$ ↔ $N\to\infty$; hadronic threshold $\tau\to1$; distinction (steep PDFs make partonic threshold logs relevant away from hadronic threshold — heuristic remark).
* **定理 `thm:thr-refactorization` — DY 阈值重新因子化与指数化** [A]. At leading power in $(1-z)$: $\Delta_{q\bar q}=H(Q,\mu)\,Q\,S_{\rm DY}(Q(1-z),\mu)$ (distributions $\delta$, $\mathcal D_k$); in Mellin space, up to $N$-independent terms and $O(1/N)$:
  $$\ln\Delta_N=\int_0^1dz\,\frac{z^{N-1}-1}{1-z}\Big[2\int_{\mu_F^2}^{(1-z)^2Q^2}\frac{dq^2}{q^2}A(\alpha_s(q^2))+D(\alpha_s((1-z)^2Q^2))\Big],\qquad A=\frac{C_F\alpha_s}\pi+O(\alpha_s^2),\ D=O(\alpha_s^2)$$
  (VF-THR-1; normalization of $A^{(1)}$ verified against the one-loop $8C_F\mathcal D_1$, critic c6). Proof: sketch (eikonal soft function with Wilson lines; RG). Literature `Sterman1987`, `CataniTrentadue1989`, `Catani:1990rp`, `Korchemsky:1992xv`, `Contopanagos:1996nh`, `Kidonakis:1997gm`; SCET `Becher:2006nr`, `Becher:2007ty`. Survey item 25.
* **命题 `prop:thr-oneloop` — 单圈检验** [R, R_PT]. With $\langle\mathcal D_0,z^{N-1}\rangle=-S_1(N-1)\to-\ln\bar N$, $\langle\mathcal D_1,z^{N-1}\rangle=\frac12[S_1^2+S_2](N-1)\to\frac12(\ln^2\bar N+\zeta_2)$: the exponent at $O(\alpha_s)$ reproduces the $\ln^2\bar N$ and $\ln\bar N$ terms of $\Delta_{q\bar q,N}=1+\frac{\alpha_s}{2\pi}C_F[4\ln^2\bar N+8\zeta_2-8]$ (at $\mu_F=Q$); the constant agrees with `Moch:2005ky` ($g_{01}^{\rm DY}=C_F(-16+16\zeta_2+8\gamma_E^2)$ in their normalization; c_dy §6.2) (VF-THR-2/3). Proof: full.
* **注 `rem:thr-prescriptions`** — the $q^2$ integral hits the Landau pole; prescriptions (minimal prescription `CataniEtAl1996`) are prescriptions, not theorems; partonic vs hadronic threshold.
* **命题 `prop:thr-dis` — DIS 的大 $x$ 重新因子化** [A]. $C_2^q\to H\cdot J\otimes S$ as $x\to1$ (`Sterman1987`, `BecherNeubertPecjak2007`).
* **命题 `prop:thr-nlp` — 次领头幂次的阈值对数** [P]. LL resummation at NLP for DY (`Beneke:2018gvs`) and Higgs (`Beneke:2019mua`); endpoint factorization case by case (`Beneke:2022obx`, NLP DIS `Beneke:2026miy`, preprint).

**Worked example.** `ex:thr-dy` — expand the exponent to $O(\alpha_s)$ and compare with the Mellin transform of `prop:dy-nlo` (= `prop:thr-oneloop` with all steps; ~1.5 pp).

**Figures.** new: `fig:thr-kinematics`, `fig:thr-mellin`.

**Key citation keys.** `Sterman1987`, `CataniTrentadue1989`, `Catani:1990rp`, `Korchemsky:1992xv`, `Contopanagos:1996nh`, `Kidonakis:1997gm`, `CataniEtAl1996`, `Becher:2006nr`, `BecherNeubertPecjak2007`, `Becher:2007ty`, `Moch:2005ky`, `Beneke:2018gvs`, `Beneke:2019mua`, `Beneke:2022obx`, `Beneke:2026miy`, `Liu:2019oav`.

---------------------------------------------------------------------------------------------------

# 第四部分 超越共线因子化 (Part IV — Beyond collinear factorization)

---------------------------------------------------------------------------------------------------

## Chapter 13 — 横动量依赖（TMD）因子化 / TMD factorization

`\label{ch:tmd}` · `ch13_tmd.tex` · **14 pp** · full

**Purpose.** At small $q_T$ the soft factor no longer cancels. The collinear subgraphs keep their transverse momenta, light-like Wilson lines produce rapidity divergences, and whether a Wilson line points to the future or the past becomes physical. The chapter gives:
- the definitions: staple-shaped Wilson lines, the soft factor, and Collins' combination;
- the factorization theorem and its status;
- Collins–Soper (CS) and renormalization-group (RG) evolution, with one-loop checks;
- the small-$b$ OPE and the CSS solution;
- process dependence: the Sivers sign as an operator identity versus the observable sign reversal, and the universality of the Collins function;
- matching to twist-3 collinear factorization, and the warning that $\int d^2k_T f\neq f$.

C9 and C10 apply throughout. Universality is derived from the operator definitions, never assumed. Only the properly combined objects are regulator independent.

**Depends on.**
- Ch4: `prop:sudakov-kg` ($K+G$, cusp).
- Ch7: `def:pdf-quark`.
- Ch8: `thm:method-template` with (H4) soft factor $\ne1$; `prop:method-glauber-oneloop`.
- Ch11: `lem:dy-fsi`, `prop:dy-abelian-model`, `prop:dy-universality` (by contrast).

**Source status (audit update).** `research/c_tmd/DERIVATION.md` now exists (14:07; 17/17 scripts pass; results R1–R12 cross-checked against Aybat–Rogers 2011, EIS 2012, Collins–Rogers 2013, Balázs–Yuan 1997 and Bacchetta–Conti–Radici 2008). All c_tmd numbers used below are verified (VF-TMD-1…10); the "(to verify)" marks of the first version were removed where c_tmd settles them. Chinese drafts in the monograph style: `research/c_tmd/tex/tmd_{definitions,oneloop,evolution,sivers}.tex` (adapt per WRITER_SPEC §11.1). Follow c_tmd §8 (corrections to the blueprint).

**Sections.**
1. `sec:tmd-kinematics` 小横动量：运动学与 Sudakov 对数.
2. `sec:tmd-regions` 领头区域：软区（非超软）、快度与 Glauber 区.
3. `sec:tmd-definitions` 定义：订书钉形 Wilson 线、软因子与 Collins 定义 (`fig:tmd-staple`, `fig:tmd-soft-factor`).
4. `sec:tmd-theorem` 因子化定理 (`fig:tmd-dy`).
5. `sec:tmd-evolution` Collins–Soper 方程与重整化群演化 (optional `fig:tmd-evolution`).
6. `sec:tmd-small-b` 小 $b$ 展开与 CSS 解.
7. `sec:tmd-universality` 过程依赖：Sivers 符号与 Collins 函数 (`fig:sidis-dy-links`).
8. `sec:tmd-twist3` 与扭度 3 共线因子化的匹配；$k_T$ 积分.

**Canonical statements.**

* **定义 `def:tmd-kin` — 小 $q_T$ 区域** (no tag).
  - Processes: DY $A+B\to\gamma^*(q)+X$ with $q_T\ll Q$; SIDIS with $P_{hT}/z\ll Q$; $e^+e^-\to h_1h_2X$ (nearly back to back).
  - At $O(\alpha_s)$ the cross section behaves like $\frac{\alpha_s}{q_T^2}[c_1\ln\frac{Q^2}{q_T^2}+c_0]$. In CSS normalization (expansion parameter $\alpha_s/\pi$, $C_1=b_0$, $C_2=1$): $A^{(1)}=C_F$, $B^{(1)}=-\frac32C_F$.
  - Check: the $O(\alpha_s)$ CSS expansion reproduces the exact small-$q_T$ asymptotics of the fixed-order $q\bar q$ and $qg$ channels (ratio $\to1$ as $q_T/Q\to0$). With $B^{(1)}=0$ the ratio at $q_T/Q=10^{-3}$ would be $0.896$.
  - Source: c_tmd [R11] (VF-TMD-7, VF-TMD-10; verified).
* **命题 `prop:tmd-regions` — 小 $q_T$ 的领头区域** [A]. The leading regions are:
  - $H$;
  - $J_A$ and $J_B$, with $k_T\sim q_T$;
  - a **soft** subgraph with all components of $k$ of order $q_T$. This is not the ultrasoft scaling of `def:ir-scalings`. Soft and collinear regions are separated only in rapidity, which is the origin of rapidity divergences when the Wilson lines are light-like;
  - Glauber exchanges.

  *Proof:* sketch (`prop:ir-power-counting` with the soft scaling; `thm:ir-leading-regions`). Literature: Collins 2011 ch. 10 and ch. 13 (section numbers **(verify)**); `CollinsSoper1981`.
* **定义 `def:tmd-unsub` — 未减除的 TMD 关联函数** (no tag). The Fourier convention is CONTEXT's, $\tilde f(x,b_T)=\int d^{2-2\varepsilon}k_T\,e^{-ik_T\cdot b_T}f(x,k_T)$. Correspondingly
  $\tilde f^{\rm unsub}(x,b_T)=\int\frac{dw^-}{4\pi}e^{-ixP^+w^-}\langle P|\bar\psi(w)\gamma^+\,\mathcal W_{\rm staple}[w,0]\,\psi(0)|P\rangle_c$ with $w=(0^+,w^-,b_T)$.
  - This follows from $f(x,k_T)=\int\frac{dw^-d^2w_T}{16\pi^3}e^{-ixP^+w^-+ik_T\cdot w_T}\langle\cdots\rangle$. The sign chain agrees with c_tmd §2.1 (Aybat–Rogers 2011 eqs. (11), (27)): verified (VF-CONV-11).
  - The staple runs from $w$ to $w\pm\infty n$, then along a transverse link at infinity (`BelitskyJiYuan2003`; needed in non-covariant gauges), then back to $0$.
  - The staple is future pointing for SIDIS and past pointing for DY.
  - A light-like $n$ gives rapidity divergences. Collins uses a non-light-like, **space-like** $n(y_B)$ with $y_B\to-\infty$ taken at the end (VF-TMD-9: with time-like past-pointing lines the PT argument of `thm:tmd-sivers-sign` fails at finite rapidity).
  - Tree-level normalization check: $\tilde f^{\rm unsub}(x,b_T\to0)=f(x)$.
  - The writer transcribes Collins 2011's definition (equation number **(verify)**) into the binding conventions. Collins uses $D_\mu=\partial_\mu+igA_\mu$ ($g\to-g$). His eq. (13.35) uses $e^{+ik_T\cdot b_T}$ for the soft factor and the TMD FFs (survey §0.3), while the Collins-scheme TMD-PDF definition of Aybat–Rogers 2011 eq. (27) agrees with our convention: check the sign at each transcription (VF-CONV-11).
* **定义 `def:tmd-soft` — 软因子** (no tag).
  $\tilde S(b_T;y_A,y_B)=\frac1{N_c}\langle0|{\rm Tr}\,\mathcal W(b_T/2;\infty,n(y_B))^\dagger\cdots\mathcal W(-b_T/2;\infty,n(y_A))|0\rangle$, with non-light-like Wilson lines of rapidities $y_A,y_B$. The operator ordering and staple geometry follow Collins 2011 **(verify equation number)**. DY and SIDIS soft factors are equal by T invariance (`lem:dy-soft`).
* **定义 `def:tmd-collins` — Collins 的 TMD 定义** (no tag).
  $$\tilde f(x,b_T;\mu,\zeta)=\lim_{y_B\to-\infty}\tilde f^{\rm unsub}(x,b_T;y_P-y_B)\sqrt{\frac{\tilde S(b_T;+\infty,y_n)}{\tilde S(b_T;+\infty,y_B)\,\tilde S(b_T;y_n,y_B)}}\times Z_{\rm UV},\qquad \zeta=M^2x^2e^{2(y_P-y_n)}.$$
  - Rapidity divergences cancel between the unsubtracted correlator and the soft factors.
  - Only the combination is regulator independent (C10).
  - In the cross section $\zeta_A\zeta_B=Q^4$ (binding, D4). Normalization $\zeta=M^2x^2e^{2(y_P-y_n)}=2(xP^+)^2e^{-2y_n}$; do not copy Aybat–Rogers eq. (3), which has a spurious factor 2 (VF-TMD-9).
  - **Order of limits** (print it): light-like limit $y_B\to-\infty$ first at fixed $\varepsilon$, then $\overline{\rm MS}$ renormalization, then $\varepsilon\to0$ (VF-TMD-9). One loop: $Z_{\rm UV}=Z_FZ_2=1+aS_\varepsilon[-\frac1{\varepsilon^2}+\frac{l_\zeta-3/2}\varepsilon]$, $a=\frac{\alpha_sC_F}{2\pi}$ (VF-TMD-4).
* **注 `rem:tmd-schemes` — 其他方案**. The other schemes are:
  - Ji–Ma–Yuan (`JiMaYuan2005`, `Ji:2004xq`, `Ji:2005nu`);
  - the $\delta$ regulator (`EchevarriaIdilbiScimemi2012`, `Echevarria:2012js`);
  - the rapidity RG (`ChiuEtAl2012a`, `ChiuEtAl2012b`);
  - the collinear anomaly (`BecherNeubert2011`).

  Relations between them: `Collins:2017oxh`. Their equivalence is [A], shown explicitly at low orders. The rapidity anomalous dimension is known to four loops (`Duhr:2022yyp`, `Moult:2022xzt`; quoted as literature).

  $\delta$-regulator check (c_tmd `delta_regulator.log`): the soft rapidity integral gives $\ln\frac{l_T^2}{2\delta^+\delta^-}$, and the combination gives $\ln(\zeta/k_T^2)$ with $\zeta=2(p^+)^2\delta^-/\delta^+$ (c_tmd [R9], verified; equals Collins–Rogers 2013 eq. (zetaA)).
* **注 `rem:tmd-scheme-constants` — 方案常数（$S_\varepsilon$ 约定）** (c_tmd [R8], [R10]; verified, VF-TMD-3/5). Units are $\frac{\alpha_sC_F}{2\pi}$.
  - **Small-$b$ coefficient.** At $\mu=\mu_b$, $\zeta=\mu_b^2$, the $\delta(1-x)$ constant of $\tilde C_{q/q}$ is $-\frac{\pi^2}{12}$ with the binding $S_\varepsilon=(4\pi)^\varepsilon e^{-\varepsilon\gamma_E}$. It is $0$ with Collins' $S_\varepsilon=(4\pi)^\varepsilon/\Gamma(1-\varepsilon)$ (Collins 2011 §3.3.2, as quoted by Collins–Rogers 2013).
  - **Hard factor.** The constant is $-8+\frac{7\pi^2}6$ (binding) versus $-8+\pi^2$ (Collins).
  - **Cancellation.** $\mathcal H^{\rm bind}-\mathcal H^{\rm Coll}=\frac{\pi^2}6$ and $2[\tilde C^{\rm bind}-\tilde C^{\rm Coll}]=-\frac{\pi^2}6$, so the cross section is unchanged.
  - **CSS coefficient.** $C^{(1)}_{qq}=\frac{\alpha_s}\pi[\frac{C_F}2(1-z)+C_F(\frac{\pi^2}4-2)\delta(1-z)]$ is the same in both conventions.

  **Writer rule:** use the binding $S_\varepsilon$ everywhere. When quoting Collins' constants, convert them and say so.
* **命题 `prop:tmd-h1h5` — 小 $q_T$ DY 对模板假设的验证** [A]. Each hypothesis of `thm:method-template` holds in the following form:
  - (H2): collinear subgraphs at fixed $k^+$ **and** $k_T$;
  - (H3): Glauber cancellation (`lem:tmd-glauber`);
  - (H4): the soft factor is $\tilde S(b_T)$, not $1$;
  - (H5): the subtractions, including the soft–collinear overlaps (the soft factors in `def:tmd-collins`), reproduce the operator definitions.

  *Proof:* sketch.
* **引理 `lem:tmd-glauber` — TMD DY、SIDIS、$e^+e^-$ 中的 Glauber 相消** [A].
  - **DY.** The spectator–spectator phase cancels after the integration over the spectators' *relative* transverse momentum $\Delta$ at fixed $q_T$. In the abelian model this is exact: $\int d^2\Delta\,2{\rm Re}[\mathcal M^{(1)}\mathcal M^{(0)*}]=0$, with the phase $e^{i\chi(b)}$, $\chi=-\frac{e_Ae_B}{2\pi}K_0(m_gb)$ (`research/c_glauber/DERIVATION.md` §1.5 Steps 3–4, checks [SS1b–e, SS3a–e]; VF-GLA-2/3).
  - **SIDIS.** There is one incoming hadron, so only final-state poles occur.
  - **$e^+e^-$.** All collinear lines are outgoing.

  Contrast: $h_1h_2\to H_1H_2X$ (`thm:break-tmd`). *Proof:* sketch; `CollinsSoperSterman1985a`, Collins 2011 ch. 14, `JiMaYuan2005`, `RothsteinStewart2016` (eqs. (11.12)–(11.13), as read by c_glauber).
* **引理 `lem:tmd-soft-oneloop` — 单圈软因子** [R, R_PT].
  - **Large rapidity separation.** $\tilde S(b_T;y_A,y_B)=1+\tilde K(b_T;\mu)(y_A-y_B)+O(\alpha_s^2)+O((y_A-y_B)^0\alpha_s)$, with $\tilde K=-\frac{\alpha_sC_F}\pi\ln\frac{\mu^2b_T^2}{b_0^2}$ (VF-TMD-1, verified).
  - **Exact one-loop rapidity dependence.** It is $\propto(Y\coth Y-\sigma)$, $Y=y_A-y_B$, with $\sigma=1$ for time-like lines (self-energies included) and $\sigma=0$ for space-like lines; the time-like and the space-like (principal-value) rapidity integrals both give $4(Y\coth Y-\sigma)$ (c_tmd [R4], verified; VF-TMD-8). For $\sigma=1$ the pole is two cusps with the anomalous dimension of `def:sudakov-cusp`. Space-like Wilson-line self-energies are non-integrable (length divergences) and cancel in the TMD combination.
  - **Higher orders.** Non-abelian exponentiation (webs): `Gatheral1983`, `FrenkelTaylor1984`.

  *Proof:* full at one loop (App G).
* **定理 `thm:tmd-factorization` — Drell–Yan 的 TMD 因子化** [A].
  $$\frac{d\sigma}{dQ^2\,dy\,d^2q_T}=\frac{\sigma_0}{s}\sum_qe_q^2\,\mathcal H(Q;\mu)\int\!\frac{d^2b_T}{(2\pi)^2}e^{iq_T\cdot b_T}\tilde f_{q/A}(x_A,b_T;\mu,\zeta_A)\tilde f_{\bar q/B}(x_B,b_T;\mu,\zeta_B)+(q\leftrightarrow\bar q)+Y(q_T,Q)+O\Big(\Big(\frac{m}{Q}\Big)^p\Big),$$
  - Here $\zeta_A\zeta_B=Q^4$ and $\sigma_0=\frac{4\pi\alpha^2}{3N_cQ^2}$ is the DY normalization of WRITER_SPEC row 33 (audit: the first version used the same symbol for $\sigma_0/s$; c_tmd §5.1 also writes $\sigma_0$ for our $\sigma_0/s$), so that $\int d^2q_T$ at tree level returns `prop:dy-born` (VF-DY-1).
  - $Y$ is the large-$q_T$ matching term.
  - The Fourier form follows from $\delta^2(q_T-k_{AT}-k_{BT})=\int\frac{d^2b}{(2\pi)^2}e^{i(q_T-k_{AT}-k_{BT})\cdot b}$ and CONTEXT's sign.
  - Analogues: SIDIS (future-pointing TMD PDF ⊗ TMD FF) and $e^+e^-\to h_1h_2X$ (two TMD FFs).
  - 非微扰地位：MA1、MA2、MA4.

  *Proof:* `proofsketch` in which the deduction from `prop:tmd-regions`–`lem:tmd-soft-oneloop` and `thm:method-template` is written out completely (WRITER_SPEC §4.7; §0.8).

  **地位与缺口:**
  - Literature: `CollinsSoper1981`, `CollinsSoperSterman1985a`, `JiMaYuan2005`, `Ji:2004xq`; Collins 2011 ch. 13–14 (the survey cites §14.4.5, §14.5).
  - DY inherits the Glauber argument of Ch11 (`thm:dy-factorization`).
  - The SCET derivations drop the Glauber Lagrangian after arguments (survey item 10).
  - The equivalence of rapidity schemes is shown order by order only (`Collins:2017oxh`).
* **命题 `prop:tmd-evolution` — Collins–Soper 方程与重整化群方程** [A].
  $$\frac{\partial\ln\tilde f}{\partial\ln\sqrt\zeta}=\tilde K(b_T;\mu),\qquad\frac{d\tilde K}{d\ln\mu}=-\gamma_K(\alpha_s),\qquad\frac{d\ln\tilde f}{d\ln\mu}=\gamma_q(\alpha_s;1)-\tfrac12\gamma_K(\alpha_s)\ln\frac{\zeta}{\mu^2}.$$
  These follow from `def:tmd-collins` together with the multiplicative renormalizability of the combined TMD operator, which is argued, not proven (Collins 2011 ch. 13). M17: $\tilde K$ is perturbative only for $b_T\ll1/\Lambda$. *Proof:* sketch.
* **命题 `prop:tmd-evolution-oneloop` — 单圈演化系数与硬因子的 RG 相容性** [R, R_PT].
  - $\tilde K=-\frac{\alpha_sC_F}\pi\ln\frac{\mu^2b_T^2}{b_0^2}$ and $\gamma_K=\frac{2\alpha_sC_F}\pi$ (VF-TMD-1/2, verified, critic c7).
  - $\gamma_q(\alpha_s;1)=\frac32\frac{\alpha_sC_F}\pi$ (c_tmd [R7]: $\gamma_F=\frac{\alpha_sC_F}\pi(\frac32-l_\zeta)$, $l_\zeta=\ln\frac\zeta{\mu^2}$; VF-TMD-4, verified).
  - $\mathcal H=1+\frac{\alpha_sC_F}{2\pi}[-L^2+3L-8+\frac{7\pi^2}6]$, $L=\ln\frac{Q^2}{\mu^2}$ (VF-TMD-3 = VF-SCET-8, verified). It obeys $\frac{d\ln\mathcal H}{d\ln\mu}=\frac{\alpha_sC_F}\pi(2L-3)$, which cancels $2\gamma_q-\frac12\gamma_K\ln\frac{\zeta_A\zeta_B}{\mu^4}=\frac{\alpha_sC_F}\pi(3-2L)$.

  *Proof:* full at one loop (`ex:tmd-oneloop`).
* **命题 `prop:tmd-css` — CSS 解与非微扰输入** [A] (solution formula).
  - The solution is evaluated with $\mu_b=b_0/b_*$, $b_*=b_T/\sqrt{1+b_T^2/b_{\max}^2}$, and the non-perturbative functions $g_K(b_T)$, $g_{j/H}(x,b_T)$ (`CollinsSoperSterman1985a`; Collins 2011 ch. 13).
  - Historical antecedents: `ParisiPetronzio1979`, `DokshitzerDiakonovTroian1978`.
  - Honest remark: the large-$b_T$ region is non-perturbative. It is fitted, or computed on the lattice for $\tilde K$ (`prop:lattice-cs-kernel`). The choice of prescription is a model ingredient (M17).
* **命题 `prop:tmd-small-b` — 小 $b$ 展开** [A].
  $\tilde f_{q/H}(x,b_T;\mu,\zeta)=\sum_j\int_x^1\frac{d\xi}\xi\tilde C_{q/j}(\frac x\xi,b_T;\mu,\zeta)f_{j/H}(\xi;\mu)+O((mb_T)^p)$, $p>0$ (c_tmd §8 item 6; $p=2$ is expected for unpolarized leading-twist TMDs — (verify), REFDOC_ANALYSIS OUR-5). 非微扰地位：MA0、MA4 (MA: audit).

  One-loop coefficients at $\mu=\mu_b$, $\zeta=\mu_b^2$, with the binding $S_\varepsilon$ (c_tmd [R8]; verified; VF-TMD-5/6; the full $\mu$, $\zeta$ dependence is in VF-TMD-5):
  - $\tilde C_{q/q}=\delta(1-x)+\frac{\alpha_sC_F}{2\pi}\big[(1-x)-\frac{\pi^2}{12}\delta(1-x)\big]$;
  - $\tilde C_{q/g}=\frac{\alpha_sT_F}{2\pi}2x(1-x)$. Its pole $-\frac1\varepsilon P_{qg}/T_F$ is IR and matches the PDF.

  In Collins' $S_\varepsilon$ convention the $\pi^2$ term is absent; that value equals `AybatRogers2011` (A11), and the binding value equals EIS 2012 (VF-TMD-5).
* **定理 `thm:tmd-sivers-sign` — Sivers 函数的符号反转（算符层面）** [R, R_def]. 非微扰地位：MA0（强子矩阵元的存在） (MA: audit). For the operator-defined Sivers function (Trento convention, `BacchettaEtAl2004`), with space-like or light-like Wilson lines (VF-TMD-9):
  $$f_{1T}^{\perp q}(x,k_T)\big|_{\rm SIDIS}=-f_{1T}^{\perp q}(x,k_T)\big|_{\rm DY}.$$
  *Proof:* full. Parity and time reversal (antiunitary) map the future-pointing staple to the past-pointing one. The Sivers structure $\epsilon_T^{ij}k_T^iS_T^j$ is T-odd.

  One-gluon illustration: $\frac1{k^++i0}-\frac1{k^+-i0}=-2\pi i\delta(k^+)$ (VF-WL-12). Spectator-model check (c_tmd [R12], verified; VF-TMD-8; equals Bacchetta–Conti–Radici 2008): ratio DY/SIDIS $=-1$, and $f_{1T}^\perp|_{\rm SIDIS}<0$ for an attractive final-state interaction in the Trento convention.

  Literature: `Collins2002` (correcting the T-invariance argument of `Collins1993`), `BrodskyHwangSchmidt2002`, `JiYuan2002`, `BelitskyJiYuan2003`, Collins 2011 §13.17. Status per critic O15: (a) here [R, R_def]; (b) `cor:tmd-sivers-observable`.
* **推论 `cor:tmd-sivers-observable` — 可观测不对称的符号反转** [A]. 非微扰地位：MA1、MA2 (MA: audit).
  - It requires `thm:tmd-factorization` for both processes.
  - Experiment is consistent but not decisive: `COMPASS:2017jbv`, `COMPASS:2023vqt`, `STAR:2015vmv`, `STAR:2023jwh`. `Bury:2020vhj` fits "cannot exclude the same sign".
  - SIDIS data: `HERMES:2009lmz`, `HERMES:2020ifk`. Global analysis: `Echevarria:2020hpy`.
* **命题 `prop:tmd-collins-universality` — T-奇碎裂函数的普适性** [A]. The Collins function (`Collins1993`) is the same in SIDIS and $e^+e^-$; there is no sign change (`CollinsMetz2004`, `MeissnerMetz2009`). (M13) 非微扰地位：MA1、MA2 (MA: audit).
* **定义 `def:tmd-etqs` — Qiu–Sterman (ETQS) 关联函数** (no tag). (Moved here from Ch20 by the audit, formerly “def:power-etqs”（已废弃）, because `prop:tmd-twist3-matching` uses it.) $T_F(x_1,x_2)$ is a quark–gluon–quark light-cone correlator with $\epsilon^{S_T\sigma n_An_B}$ structure. Its gluonic-pole value is $T_F(x,x)$ (`EfremovTeryaev1985`, `Efremov:1981sh`, `QiuSterman1991c`). Ch20 uses it for twist-3 factorization.
* **命题 `prop:tmd-twist3-matching` — 与扭度 3 共线因子化的匹配** [P].
  - For $\Lambda\ll q_T\ll Q$ the TMD and twist-3 (ETQS) descriptions of single-spin asymmetries agree at one loop (`Ji:2006ub`).
  - The first $k_T$-moment of the Sivers function is related to the Qiu–Sterman function $T_F(x,x)$ (gluonic pole) by a convention-dependent factor (`Boer:2003cm`; **(verify)**).
  - Evolution of $T_F$: the dispute between `Braun:2009mi` and `Kang:2008ey` is resolved.
  - NLO SSA in DY: `Vogelsang:2009pj`.
  - The process-dependence "sign mismatch": `Kang:2011hk`, addressed by `Cammarota:2020qcw`.
* **注 `rem:tmd-kt-integral` — $\int d^2k_T\,f\ne f$** (M14). Beyond tree level the $k_T$ integral of the renormalized TMD diverges in the UV (the tail is $\sim\alpha_s/k_T^2$). The relation to $f(x;\mu)$ holds only with a cutoff, up to scheme-dependent terms and power corrections (`EbertMichelStewartSun2022`).

**Worked examples.**
* `ex:tmd-oneloop` — one loop throughout:
  - the unsubtracted TMD with Collins' non-light-like regulator;
  - the soft factor;
  - the combination of `def:tmd-collins`;
  - extraction of $\tilde K$, $\gamma_K$, $\gamma_q$ and $\tilde C_{q/q}$, including the $S_\varepsilon$ remark.

  Follow `research/c_tmd/DERIVATION.md` §3 (R1–R8) and its draft `tex/tmd_oneloop.tex`; all numbers are verified (VF-TMD-1…9).
* `ex:tmd-qt-asymptotics` — expand `thm:tmd-factorization` to $O(\alpha_s)$ and recover the fixed-order small-$q_T$ terms ($A^{(1)}$, $B^{(1)}$, $C^{(1)}_{qq}$).
* `ex:tmd-sivers-model` — the scalar-diquark (BHS) Sivers function with future- and past-pointing lines.

**Figures.**
- Existing (tikz3, being redone): `fig:tmd-staple`, `fig:tmd-soft-factor`, `fig:tmd-dy`, `fig:sidis-dy-links`.
- Optional new: `fig:tmd-evolution`.

**Misconception box.** M12, M13, M14, M15, M16, M17; C9, C10.

**Key citation keys.** `CollinsSoper1981`, `CollinsSoper1982b`, `CollinsSoperSterman1985a`, `ParisiPetronzio1979`, `DokshitzerDiakonovTroian1978`, `Collins2011`, `JiMaYuan2005`, `Ji:2004xq`, `Ji:2005nu`, `JiYuan2002`, `BelitskyJiYuan2003`, `Collins:1999dz`, `AybatRogers2011`, `EchevarriaIdilbiScimemi2012`, `Echevarria:2012js`, `ChiuEtAl2012a`, `ChiuEtAl2012b`, `BecherNeubert2011`, `Collins:2017oxh`, `Vladimirov:2017ksc`, `Duhr:2022yyp`, `Moult:2022xzt`, `Gatheral1983`, `FrenkelTaylor1984`, `Collins2002`, `Collins1993`, `BrodskyHwangSchmidt2002`, `Sivers1990`, `Sivers:1990fh`, `BoerMulders1998`, `Boer:2003cm`, `CollinsMetz2004`, `MeissnerMetz2009`, `BacchettaEtAl2004`, `HERMES:2009lmz`, `HERMES:2020ifk`, `COMPASS:2017jbv`, `COMPASS:2023vqt`, `STAR:2015vmv`, `STAR:2023jwh`, `Bury:2020vhj`, `Echevarria:2020hpy`, `Ji:2006ub`, `QiuSterman1991c`, `EfremovTeryaev1985`, `Kang:2008ey`, `Braun:2009mi`, `Vogelsang:2009pj`, `Kang:2011hk`, `Cammarota:2020qcw`, `EbertMichelStewartSun2022`, `BoussarieEtAl2023`, `AngelesMartinezEtAl2015`, `RothsteinStewart2016`, `Meng:1995yn`, `Nadolsky:1999kb`.

---------------------------------------------------------------------------------------------------

## Chapter 14 — 有效场论方法：SCET / Effective-field-theory methods: soft-collinear effective theory

`\label{ch:scet}` · `ch14_scet.tex` · **12 pp** · full

**Purpose.** Reformulate factorization as an effective field theory (EFT). The chapter covers:
- modes and power counting;
- the leading collinear Lagrangian and the collinear Wilson line;
- gauge symmetry and the BPS ultrasoft decoupling theorem, with all of its conditions;
- SCET$_{\rm I}$ versus SCET$_{\rm II}$, zero-bin subtractions, rapidity divergences and regulators;
- Glauber operators;
- matching;
- thrust factorization $H\,J\otimes J\otimes S$, with one-loop factors, RG consistency and LL resummation.

Honest status (C6, M18): mode completeness *is* the region analysis of Ch3, and Glauber modes must be shown to cancel or to be absent.

**Conventions (this chapter only).**
- $n=(1,0,0,1)$, $\bar n=(1,0,0,-1)$.
- Scalings are written for $(\bar n\!\cdot\!p,\ n\!\cdot\!p,\ p_\perp)$. Rothstein–Stewart and the blueprint use the swapped order, so convert every quotation.
- Star distributions as in `def:prelim-plus` (jet: reference $\mu^2$; soft: reference $\mu$). Thrust plus distributions subtract at $\tau=0$.
- Laplace transforms follow Becher–Schwartz (c_scet §1).

**Depends on.** Ch4, Ch8 (regions, subtractions), Ch13 (rapidity divergences).

**Sections.**
1. `sec:scet-modes` 模式与幂次计数.
2. `sec:scet-lagrangian` 领头阶共线拉氏量与共线 Wilson 线 (`fig:scet-wilson`).
3. `sec:scet-decoupling` 规范对称性与超软退耦.
4. `sec:scet-scet2` SCET$_{\rm II}$、零箱减除与快度发散.
5. `sec:scet-glauber` Glauber 算符.
6. `sec:scet-thrust` 推力分布的因子化 (`fig:dijet-factorization`).
7. `sec:scet-rg` 重整化群一致性与重求和.
8. `sec:scet-status` SCET 证明的前提与地位.

**Canonical statements.**

* **定义 `def:scet-modes` — 模式** (no tag). In $(\bar n\!\cdot\!p,n\!\cdot\!p,p_\perp)/Q$ (VF-SCET-1; Rothstein–Stewart Table 1 after swapping the first two entries):

  | mode | scaling |
  |---|---|
  | hard | $(1,1,1)$ |
  | $n$-collinear | $(1,\lambda^2,\lambda)$ |
  | $\bar n$-collinear | $(\lambda^2,1,\lambda)$ |
  | ultrasoft | $(\lambda^2,\lambda^2,\lambda^2)$ |
  | soft | $(\lambda,\lambda,\lambda)$ |
  | hard-collinear | $(1,\lambda,\lambda^{1/2})$ |
  | Glauber $n\bar n$ | $(\lambda^2,\lambda^2,\lambda)$ |
  | Glauber $ns$ | $(\lambda,\lambda^2,\lambda)$ |
  | Glauber $\bar ns$ | $(\lambda^2,\lambda,\lambda)$ |
* **命题 `prop:scet-scalings` — 场的标度** [R, R_def]. $\xi_n\sim\lambda$; $(\bar n\!\cdot\!A_n,n\!\cdot\!A_n,A_{n\perp})\sim(1,\lambda^2,\lambda)$; $A_{us}\sim\lambda^2$; $q_{us}\sim\lambda^3$; $A_s\sim\lambda$; $q_s\sim\lambda^{3/2}$. These follow from the two-point functions (VF-SCET-2; `BauerEtAl2001`; power counting `Bauer:2002uv`).
* **命题 `prop:scet-lagrangian` — 领头阶共线夸克拉氏量** [R, R_PT].
  $$\mathcal L^{(0)}_{\xi\xi}=\bar\xi_n\Big[in\!\cdot\!D+i\slashed D_{\perp c}\frac1{i\bar n\!\cdot\!D_c}i\slashed D_{\perp c}\Big]\frac{\bar{\slashed n}}2\xi_n,\qquad in\!\cdot\!D=in\!\cdot\!\partial+gn\!\cdot\!A_n+gn\!\cdot\!A_{us}(x_-).$$
  - Derivation: integrate out $\phi=P_{\bar n}\psi$ at tree level. This is an exact identity; then power counting.
  - Feynman rules: the collinear vertex, the ultrasoft vertex $igt^an^\mu\frac{\bar{\slashed n}}2$, and the propagator $i\frac{\slashed n}2\frac{\bar n\cdot p}{p^2+i0}$ (VF-SCET-3/4; `BauerEtAl2001`, `BauerPirjolStewart2002`).

  *Proof:* full (c_scet `s1`).
* **命题 `prop:scet-wilson` — 共线 Wilson 线** [R, R_PT].
  - Definition: $W_n(x)=W[x,x-\infty\bar n]=P\exp(ig\int_{-\infty}^0ds\,\bar n\!\cdot\!A_n(x+s\bar n))=\sum_{\rm perms}\exp[-\frac g{\bar{\mathcal P}}\bar n\!\cdot\!A_n]$.
  - One-gluon rule: $-g\bar n^\mu t^a/(\bar n\cdot k+i0)$.
  - Origin: it arises from integrating out off-shell modes at tree level. One gluon was checked numerically; all orders follow by the induction of `BauerEtAl2001`.
  - No sign change of $g$ is needed relative to BFPS/BPS, who use $D=\partial-igA$ (c_scet §6 item 6; VF-SCET-5).
* **命题 `prop:scet-gauge` — 共线与超软规范对称性** [R, R_def].
  - The field-strength term is invariant under both collinear and ultrasoft transformations.
  - The gauge-fixing and ghost terms are ultrasoft covariant and BRST invariant.
  - Correction of BPS 2002's wording about the ghost term: c_scet §6 item 15.
* **定理 `thm:scet-decoupling` — 超软退耦（BPS 场重定义）** [R, R_def].
  - **Key identity:** $in\!\cdot\!D_{us}Y_n=Y_n\,in\!\cdot\!\partial$, where $Y_n(x)=W[x,x-\infty n]$ is built from the multipole-expanded $n\!\cdot\!A_{us}(x_-)$ (VF-SCET-6).
  - **Statement:** the redefinitions $\xi_n=Y_n\xi_n^{(0)}$, $A_n=Y_nA_n^{(0)}Y_n^\dagger$, $c_n=Y_nc_n^{(0)}Y_n^\dagger$ remove $n\!\cdot\!A_{us}$ from $\mathcal L^{(0)}_{\xi\xi}+\mathcal L^{(0)}_{cg}$.
  - **Conditions** (c_scet §6 item 5):
    1. the collinear ghosts are redefined;
    2. the collinear gauge fixing is covariant under ultrasoft transformations;
    3. the Jacobian is unity;
    4. the statement holds at leading power only;
    5. $Y_n$ is built from multipole-expanded fields.
  - **Status:** as an identity of the LO SCET Lagrangian, [R, R_def]. As a statement about QCD it inherits mode completeness, which is [A] (`rem:scet-assumptions`).

  *Proof:* full (c_scet §2.4; `BauerPirjolStewart2002`).
* **注 `rem:scet-y-direction` — $Y_n$ 的方向与 $i0$**.
  - For outgoing collinear quarks the QCD eikonal rules give the future-pointing line.
  - This is immaterial for the Lagrangian identity and for one-loop thrust (`Chay:2004zn`, `Kang:2015moa`).
  - Rule (`RothsteinStewart2016`): ultrasoft directions are physical.
  - Ultrasoft decoupling does **not** remove Glauber interactions (c_scet §6 item 14).
* **定义 `def:scet-zero-bin` — 零箱减除** (no tag). The zero-bin subtraction (`ManoharStewart2007`) is the EFT counterpart of `def:method-subtraction`. It is equivalent to soft subtractions (`IdilbiMehen2007`). Double counting is avoided only if it is carried out consistently (C6).
* **命题 `prop:scet-scet2` — SCET$_{\rm II}$ 与软 Wilson 线** [R, R_PT].
  - Collinear $(1,\lambda^2,\lambda)$ and soft $(\lambda,\lambda,\lambda)$ modes have the same virtuality.
  - A soft gluon attached to a collinear line produces hard-collinear virtuality $\lambda Q^2$. Integrating it out yields $S_n=P\exp(ig\int_{-\infty}^0ds\,n\!\cdot\!A_s(x+sn))$. Numerical check: relative error $0.77,0.077,0.0077$ for $\lambda=10^{-1,-2,-3}$.
  - Integrals are separated only in rapidity, so rapidity regulators are required (`Hill:2002vw`, `BauerEtAl2002`).
* **命题 `prop:scet-rapidity-rg` — 快度发散的处理与等价性** [A]. The rapidity RG (`ChiuEtAl2012a`, `ChiuEtAl2012b`), the collinear anomaly (`BecherNeubert2011`) and Collins' non-light-like lines (Ch13) give equivalent TMD factorization (`Collins:2017oxh`, explicit at low orders). In the EIS/δ-regulator normalization $\partial\ln\tilde f/\partial\ln Q^2=-D$ at $\zeta=Q^2$ with $D=-\tilde K/2$ (c_tmd §3.8; verified). The normalization of the rapidity-RG anomalous dimension $\gamma_\nu$ of `ChiuEtAl2012a` relative to $\tilde K$ is to be transcribed by the writer **(verify)**.
* **命题 `prop:scet-glauber-operators` — Glauber 算符** [A] (`RothsteinStewart2016`).
  - There are Glauber operators coupling the $n$, $\bar n$ and soft sectors, and Glauber exchange "can induce corrections which invalidate factorization".
  - Glauber subtractions make soft and collinear Wilson-line directions irrelevant.
  - The spectator–spectator phase cancels once $\Delta p_\perp$ is integrated.
  - Active–active Glauber equals the Glauber zero-bin of the soft graph (RS §10.1, as read by c_glauber).
  - The announced complete SCET proof of DY had not been found as of 2026-10 (survey item 8).
* **命题 `prop:scet-hard-matching` — 硬匹配系数** [R, R_PT]. With $a=\frac{C_F\alpha_s}{4\pi}$:
  - $C_V=1+a[-L^2+3L-8+\zeta_2]$, $L=\ln\frac{-q^2-i0}{\mu^2}$;
  - $H=|C_V|^2=1+a[-2L_Q^2+6L_Q-16+\frac{7\pi^2}3]$ (VF-SCET-7/8; agrees with `BecherSchwartz2008` App. B).

  *Proof:* full (exact-in-$\varepsilon$ form factor, `prop:sudakov-oneloop`).
* **定理 `thm:scet-thrust` — 推力分布的因子化** [A]. 非微扰地位：MA1、MA2 (MA: audit).
  $$\frac1{\sigma_0}\frac{d\sigma}{d\tau}=H(Q^2,\mu)\int dp_L^2\,dp_R^2\,dk\;J(p_L^2,\mu)J(p_R^2,\mu)S_T(k,\mu)\,\delta\Big(\tau-\frac{p_L^2+p_R^2}{Q^2}-\frac kQ\Big)+O(\tau^0)$$
  The jet function is defined by the explicitly normalized cut (c_scet `tex/c_scet_thrust.tex`, eq. thrust-Jdef). Becher–Schwartz' literal formula carries an implicit $-\frac1{2N_c}{\rm tr}$ (c_scet §6 item 13).

  **地位:** [A] to all orders within SCET with modes hard, two collinear, and ultrasoft. For $e^+e^-$ there is no Glauber pinch because all collinear lines are outgoing (`prop:method-glauber-deformation`). Cite RS 2016 only for the general mechanism (c_scet §6 item 14). Literature: `BecherSchwartz2008`, `Schwartz:2007ib`, `Fleming:2007qr`, `Fleming:2007xt`, `Bauer:2008dt`, `Lee:2006nr`.
* **命题 `prop:scet-thrust-oneloop` — 单圈因子与 RG 一致性** [R, R_PT].
  - Jet function: $J=\delta(p^2)+a\{(7-\pi^2)\delta(p^2)-3[\frac1{p^2}]_*+4[\frac{\ln(p^2/\mu^2)}{p^2}]_*\}$.
  - Soft function: $S_T=\delta(k)+a\{\frac{\pi^2}3\delta(k)-16[\frac{\ln(k/\mu)}k]_*\}$ (VF-SCET-9/10).
  - Consistency: the cusp terms cancel identically ($2L_Q-4L_J+4L_S=0$), and $\gamma^S=\gamma^H-2\gamma^J$. This is the correct form of the blueprint's "$\gamma_H+2\gamma_J+\gamma_S=0$" (c_scet §6 item 1).
  - Two loops: $\gamma^S_1=C_FC_A(\frac{808}{27}-\frac{11\pi^2}9-28\zeta_3)+C_FT_Fn_f(-\frac{224}{27}+\frac{4\pi^2}9)$ (VF-SCET-11).
  - Reproduces QCD: $\frac1{\sigma_0}\frac{d\sigma}{d\tau}=\delta(\tau)+\frac{C_F\alpha_s}{2\pi}\{(\frac{\pi^2}3-1)\delta(\tau)-3[\frac1\tau]_+-4[\frac{\ln\tau}\tau]_+\}$ (VF-SCET-12; also critic c3).
* **命题 `prop:scet-ll` — 领头对数指数** [A] (audit: was [R, R_PT], an over-claim; as the LL solution of the RG equations of `thm:scet-thrust` the statement is an algebraic consequence, [R, R_def] — state this as item (b), WRITER_SPEC §4.11; as a statement about the QCD thrust distribution it inherits [A]).
  $\ln\tilde t_{\rm LL}=\ell g_1(\lambda)$, with $g_1=-\frac{C_F}{\pi b\lambda}[(1-2\lambda)\ln(1-2\lambda)-2(1-\lambda)\ln(1-\lambda)]$, $\lambda=b\alpha_s(Q)\ell$, $b=\beta_0/(4\pi)$, $\ell=\ln(\nu e^{\gamma_E})$ (VF-SCET-14). This matches CTTW (`CataniEtAl1993`).
* **注 `rem:scet-assumptions` — SCET 证明的前提** (C6, M18).
  1. Mode completeness: the chosen modes reproduce the IR of QCD. This *is* the region analysis of Ch3 (`thm:ir-leading-regions`).
  2. Zero-bin consistency.
  3. Glauber modes are absent or cancel.
  4. Leading power.

  Survey item 17: Collins 2011 §15.9 could not "penetrate the SCET literature". Collins' graphical approach and the SCET approach are complementary; neither supersedes the other's hypotheses.

**Worked examples.**
* `ex:scet-wn-tree` — tree-level matching of an off-shell collinear gluon attached to a $\bar n$ quark, producing the first term of $W_n$.
* `ex:scet-decoupling-tree` — tree-level demonstration that the BPS redefinition removes $n\cdot A_{us}$ from $\mathcal L^{(0)}$.
* `ex:scet-thrust-oneloop` — $H$, $J$, $S_T$ at one loop combine in Laplace space into the QCD singular terms. The $\delta(\tau)$ coefficient $\frac{\pi^2}3-1$ is also obtained from the total-rate sum rule ($2.289868133697$ vs. $2.289868133696$).

**Figures.**
- Existing (tikz2): `fig:scet-wilson`, `fig:dijet-factorization`.
- Optional new: `fig:scet-modes` (modes in the $(\ln\bar n\cdot p,\ln n\cdot p)$ plane, with the hyperbolae of constant virtuality and the Glauber points).

**Misconception box.** M18, M19 (Minkowski regions), C6.

**Key citation keys.** `BauerFlemingLuke2000`, `BauerEtAl2001`, `BauerStewart2001`, `BauerPirjolStewart2001`, `BauerPirjolStewart2002`, `BauerEtAl2002`, `Bauer:2002uv`, `BenekeEtAl2002`, `Beneke:2002ni`, `Hill:2002vw`, `ManoharStewart2007`, `IdilbiMehen2007`, `Lee:2006nr`, `BecherSchwartz2008`, `Schwartz:2007ib`, `Bauer:2008dt`, `Fleming:2007qr`, `Fleming:2007xt`, `Bauer:2003di`, `Chay:2004zn`, `Kang:2015moa`, `ChiuEtAl2012a`, `ChiuEtAl2012b`, `BecherNeubert2011`, `Collins:2017oxh`, `RothsteinStewart2016`, `Feige:2013zla`, `FeigeSchwartz2014`, `KorchemskyRadyushkin1987`, `CataniEtAl1993`, `DeRujula:1978vmq`, `BecherBroggioFerroglia2015`, `Collins2011`.

---------------------------------------------------------------------------------------------------

## Chapter 15 — 喷注、事件形状、非全局对数与超领头对数 / Jets, event shapes, non-global and super-leading logarithms

`\label{ch:jets}` · `ch15_jets.tex` · **9 pp** · short format (precise statement + status + proof idea + one worked example)

**Purpose.** Give IR-safe jet observables a home. The chapter covers:
- what IR safety gives and does not give (M9, M10);
- the classic Sterman–Weinberg (SW) calculation and the LO thrust distribution;
- the status of hadronization corrections;
- non-global logarithms: existence, BMS, EFT factorization;
- super-leading logarithms, as computed and resummed results.

The factorization-violation side of super-leading logarithms belongs to Ch17.

**Depends on.** Ch3 (`def:ir-safe`, `thm:ir-safe-finite`), Ch5, Ch14.

**Sections.** `sec:jets-irsafe` 红外安全的喷注与事件形状 (`fig:jets-sw-cone`); `sec:jets-hadronization` 强子化修正; `sec:jets-ngl` 非全局对数 (`fig:jets-ngl`); `sec:jets-sll` 超领头对数 (`fig:jets-gap`).

**Canonical statements.**

* **定义 `def:jets-algorithms` — 红外安全的喷注定义与事件形状** (no tag). The following are IR safe in the sense of `def:ir-safe`:
  - the SW cone (half-angle $\delta$; energy fraction $\epsilon$ of the **total** energy $\sqrt s$);
  - thrust $T$, $\tau=1-T$;
  - sequential recombination: $k_T$ (`CataniEtAl1993kt`, `EllisSoper1993`) and anti-$k_T$ (`CacciariSalamSoyez2008`);
  - SISCone (`SalamSoyez2007`).

  Seed-based cones are not IR safe at higher orders (`SalamSoyez2007`).
* **命题 `prop:jets-sw` — Sterman–Weinberg 两喷注截面** [R, R_PT].
  $$\sigma_{2j}=\sigma_0\Big\{1-\frac{C_F\alpha_s}\pi\Big[4\ln\delta\ln2\epsilon+3\ln\delta+\frac{\pi^2}3-\frac52\Big]\Big\},\qquad\epsilon<\delta\ll1.$$
  - If $\epsilon$ is a fraction of the *beam* energy, the log is $\ln\epsilon$.
  - The variant "$4\ln\delta\ln\epsilon$" with $\epsilon$ a fraction of the total energy is wrong by $4\ln2|\ln\delta|$.
  - The formula fails for $\epsilon\gg\delta$.

  Source: c_ee §8, 6/6 checks; VF-EE-12. *Proof:* full (worked example).
* **推论 `cor:jets-ir-finite` — 红外安全喷注截面的有限性** [A]. This is `thm:ir-safe-finite` applied to jet algorithms (`StermanWeinberg1977`, `Sterman1978a`, `Sterman1978b`, `Sterman:1979uw`). It covers final-state singularities only. With incoming hadrons it needs collinear factorization (M8, M9).
* **命题 `prop:jets-thrust-lo` — 领头阶推力分布** [R, R_PT].
  - Distribution: $\frac{C_F\alpha_s}{2\pi}\big[\frac{2(3T^2-3T+2)}{T(1-T)}\ln\frac{2T-1}{1-T}-\frac{3(3T-2)(2-T)}{1-T}\big]$ (VF-SCET-13; `DeRujula:1978vmq`).
  - Singular terms and cumulant: $1+\frac{C_F\alpha_s}{2\pi}[-2\ln^2\tau-3\ln\tau+\frac{\pi^2}3-1]+O(\tau\ln\tau)$ (critic c3, 20 digits; VF-SCET-12).
  - Exact identity $\frac{M_L^2+M_R^2}{Q^2}=\tau-\frac{\tau^2}2+\frac{(M_R^2-M_L^2)^2}{2Q^4}$ for massless particles (VF-SCET-15).
* **猜想 `conj:jets-hadronization` — 强子化修正的普适性** [C].
  - The leading hadronization correction to event shapes is a shift $\propto\Lambda/Q$ with a universal coefficient (dispersive model `DokshitzerWebber1995`; renormalon motivation: Ch20).
  - For $Q\tau\sim\Lambda$ the soft function becomes a non-perturbative shape function (`Korchemsky:1994is`, `Korchemsky:1999kt`, `Bauer:2003di`, `Lee:2006nr`, `Bauer:2008dt`). Universality is [C] (critic B18). M10: event shapes have $O(\Lambda/Q)$ corrections.
* **命题 `prop:jets-ngl` — 非全局对数的存在** [R, R_PT]. For an energy-flow veto in a patch (Dasgupta–Salam hemisphere case) the leading NGL appears at $O(\alpha_s^2)$ with colour factor $C_FC_A$ and a $\pi^2$ coefficient (`DasguptaSalam2001`, `Dasgupta:2002bw`; normalization **(verify)**). The exact fixed-order coefficients are known.
* **定理 `thm:jets-bms` — BMS 方程** [A] (leading log, large $N_c$). The BMS equation is `Banfi:2002hw`. Finite-$N_c$ evolution: `Weigert:2003mm`, `Hatta:2013iba`. Relation to BFKL/BK: `Caron-Huot:2015bja`.
* **命题 `prop:jets-ngl-beyond` — 超出领头对数与有限 $N_c$** [P]. Partial and numerical results only.
* **定理 `thm:jets-ngl-factorization` — 喷注过程的有效场论因子化** [A]. Multi-Wilson-line soft functions and their RG (`Becher:2015hka`, `Becher:2016mmh`).
* **命题 `prop:jets-sll` — 超领头对数** [P].
  - In hadron-collider gap-between-jets cross sections, Coulomb (Glauber) phases do not cancel. They generate terms $\alpha_s^nL^{2n-3}$, starting at $\alpha_s^4L^5$ relative to Born (`ForshawKyrieleisSeymour2006` eqs. (3.22), (3.24); `Forshaw:2008cq`). Verified via c_glauber §4.5 (VF-GLA-13): first term $-\sigma_0(\frac{2\alpha_s}\pi)^4\ln^5\frac Q{Q_0}\pi^2Y\frac{3N^2-4}{480}$ for quark–quark scattering with one gluon outside the gap; all-order tower $\alpha_s^{n+3}L^{2n+3}$ (`Becher:2021zkk`).
  - Resummation: `Becher:2021zkk`, `Becher:2023mtx`, `Boer:2024hzh`, `Becher:2024nqc`.
  - Super-super-leading logarithms in one-jettiness: `Banfi:2025mra`.
  - Their factorization-violating side: `prop:break-fss`, `prop:break-mass-singularity` (Ch17).

**Worked example.** `ex:jets-sw` — the SW cross section at $O(\alpha_s)$ (c_ee §8):
- the three-body phase space and the cone and energy cuts;
- the virtual correction;
- the $\ln2\epsilon$ subtlety, with a numerical table.

**Figures.** New: `fig:jets-sw-cone`, `fig:jets-ngl`, `fig:jets-gap`.

**Misconception box.** M8, M9, M10.

**Key citation keys.** `StermanWeinberg1977`, `Sterman1978a`, `Sterman1978b`, `Sterman:1979uw`, `Farhi1977`, `DeRujula:1978vmq`, `CataniEtAl1993`, `CataniEtAl1993kt`, `EllisSoper1993`, `CacciariSalamSoyez2008`, `SalamSoyez2007`, `DokshitzerWebber1995`, `Korchemsky:1994is`, `Korchemsky:1999kt`, `Bauer:2003di`, `Lee:2006nr`, `Bauer:2008dt`, `DasguptaSalam2001`, `Dasgupta:2002bw`, `Banfi:2002hw`, `Weigert:2003mm`, `Hatta:2013iba`, `Caron-Huot:2015bja`, `Becher:2015hka`, `Becher:2016mmh`, `ForshawKyrieleisSeymour2006`, `Forshaw:2008cq`, `Becher:2021zkk`, `Becher:2023mtx`, `Boer:2024hzh`, `Becher:2024nqc`, `Banfi:2025mra`, `EllisStirlingWebber1996`.

---------------------------------------------------------------------------------------------------

## Chapter 16 — 小 $x$ 与高能因子化 / Small $x$ and high-energy factorization

`\label{ch:smallx}` · `ch16_smallx.tex` · **8 pp** · short format

**Purpose.** State precisely what is established in the Regge limit:
- BFKL at LL and NLL, as statements about the high-energy limit of perturbation theory;
- $k_T$ (high-energy) factorization, at LL in $\ln(1/x)$ for specific processes;
- BK/JIMWLK, at LL plus NLO BK in the dipole/shock-wave framework;
- saturation, which is [C].

Collinear factorization becomes non-uniform as $x\to0$.

**Depends on.** Ch4 (Wilson lines and cusp), Ch7 (DGLAP), Ch13 (Wilson-line correlators).

**Sections.** `sec:smallx-regge` Regge 极限与 $\ln(1/x)$; `sec:smallx-bfkl` BFKL (`fig:bfkl-ladder`); `sec:smallx-kt` $k_T$ 因子化; `sec:smallx-dipole` 偶极子、BK 与 JIMWLK (`fig:smallx-dipole`); `sec:smallx-status` 地位与图谱 (`fig:smallx-map`).

**Canonical statements.**

* **定义 `def:smallx-regge` — 高能极限** (no tag).
  - The limit: $s\gg|t|$, or $x\to0$ at fixed $Q^2$.
  - Leading logarithms: $(\alpha_s\ln\frac1x)^n$.
  - The unintegrated gluon distribution $\mathcal F(x,k_T)$ and the dipole amplitude $N(x,r)$, each in a stated normalization.
* **定理 `thm:smallx-bfkl` — BFKL 方程** [A] (within LL/NLL).
  - The BFKL equation resums $(\alpha_s\ln\frac1x)^n$: LL (`Fadin:1975cb`, `Kuraev:1976ge`, `KuraevLipatovFadin1977`, `BalitskyLipatov1978`); NLL (`Fadin:1998py`, `Ciafaloni:1998gs`).
  - The LL intercept is $\omega_{\mathbb P}=4\ln2\,\frac{N_c\alpha_s}\pi=\bar\alpha_s\chi(\frac12)$ (VF-MISC-4; verified).
  - The NLL corrections are large, which motivates collinear-improved schemes (remark).
* **命题 `prop:smallx-kt` — $k_T$（高能）因子化** [P].
  - $\sigma=\int d^2k_T\,\hat\sigma(x,k_T)\mathcal F(x,k_T)$ for heavy quarks and DIS at LL in $\ln(1/x)$ (`CataniCiafaloniHautmann1991`, `Catani:1990xk`, `CollinsEllis1991`, `Levin:1991ry`; beyond LL: `Catani:1994sq`).
  - It is not a theorem with controlled power corrections.
  - Unintegrated gluon distributions are process dependent (`Dominguez:2011wm`).
* **定理 `thm:smallx-bk` — BK 方程与 JIMWLK** [A] (LL, in the dipole/shock-wave framework).
  - LL BK: $\partial_YN_{01}=\frac{\bar\alpha_s}{2\pi}\int d^2x_2\frac{x_{01}^2}{x_{02}^2x_{12}^2}[N_{02}+N_{12}-N_{01}-N_{02}N_{12}]$, $\bar\alpha_s=N_c\alpha_s/\pi$ (VF-MISC-4: the linear part has eigenvalue $\bar\alpha_s\chi(\gamma)$ on $(x_{01}^2)^\gamma$ — checked numerically by the audit — so this normalization is consistent with $\omega_{\mathbb P}$; `Balitsky1996`, `Kovchegov1999`).
  - JIMWLK: `Jalilian-Marian:1997qno`, `Jalilian-Marian:1997jhx`, `Iancu:2000hn`, `Ferreiro:2001qy`.
  - NLO BK: `Balitsky:2007feb`.
  - The linearized BK equation is LL BFKL.
* **猜想 `conj:smallx-saturation` — 饱和与色玻璃凝聚** [C]. At small $x$, gluon densities saturate, and the CGC is the effective theory of QCD in that regime (`GribovLevinRyskin1983`, `Mueller:1985wy`, `McLerran:1993ni`, `GelisEtAl2010`, `KovchegovLevin2012`). Matching to collinear factorization is not proven.
* **注 `rem:smallx-nonuniform` — 共线因子化在小 $x$ 的非一致性**.
  - Coefficient functions and splitting functions contain $\alpha_s^n\ln^{n-1}(1/x)$, so both the $\alpha_s$ expansion and the power expansion are non-uniform as $x\to0$ (`Milana:1986tq`).
  - Small-$x$ resummation of anomalous dimensions: `Catani:1994sq`.
  - Nuclear targets: `prop:disall-nuclear`.

**Worked example.** `ex:smallx-dla` — the double-leading-log overlap of DGLAP and BFKL:
- $\frac{\alpha_s}{2\pi}\gamma_{gg}(N)\simeq\frac{\bar\alpha_s}{N-1}$ ($\gamma_{gg}$ normalized as in VF-PDF-8; audit fixed the notation), the collinear limit of the BFKL kernel;
- $xg\sim\exp\sqrt{4\bar\alpha_s\ln\frac1x\ln\frac{Q^2}{Q_0^2}}$ at fixed coupling (VF-MISC-4; the writer derives it from `prop:pdf-lo-kernels` by a saddle point).

**Figures.**
- Existing (tikz3, being redone): `fig:bfkl-ladder`.
- New: `fig:smallx-dipole`, `fig:smallx-map`.

**Key citation keys.** `Fadin:1975cb`, `Kuraev:1976ge`, `KuraevLipatovFadin1977`, `BalitskyLipatov1978`, `Fadin:1998py`, `Ciafaloni:1998gs`, `CataniCiafaloniHautmann1991`, `Catani:1990xk`, `CollinsEllis1991`, `Levin:1991ry`, `Catani:1994sq`, `Balitsky1996`, `Kovchegov1999`, `Jalilian-Marian:1997qno`, `Jalilian-Marian:1997jhx`, `Iancu:2000hn`, `Ferreiro:2001qy`, `Balitsky:2007feb`, `GribovLevinRyskin1983`, `Mueller:1985wy`, `McLerran:1993ni`, `Dominguez:2011wm`, `Milana:1986tq`, `GelisEtAl2010`, `KovchegovLevin2012`, `BoerEtAl2011`.

---------------------------------------------------------------------------------------------------

## Chapter 17 — 因子化的破坏与非标准情形 / Breakdown of factorization and non-standard cases

`\label{ch:break}` · `ch17_break.tex` · **12 pp** · full

**Purpose.** For each case, say *which hypothesis of `thm:method-template` fails*, and give the evidence: an explicit counterexample, experiment, or a partial proof. This is where most [V], [C] and [P] tags live, so it must be as careful as the rigorous chapters.

A [V] means one of three things:
- an explicit perturbative counterexample in a model or in QCD;
- an explicit calculation;
- experiment.

Which one is said every time (critic O17).

**Depends on.** Ch8 (`thm:method-template`, `prop:method-glauber-deformation`), Ch11 (`lem:dy-fsi`, `prop:dy-abelian-model`), Ch13 (TMD definitions), Ch14 (Glauber operators), Ch15 (SLLs).

**Source.** `research/c_glauber/DERIVATION.md` §1–§4 (audit update: §3 diffraction and §4 space-like collinear limit and super-leading logarithms are written, file of 13:33; no check failed, c_glauber §5). Follow c_glauber §6 (corrections to the blueprint). Chinese snippets in the monograph style: `research/c_glauber/tex/c_glauber_snippets.tex`.

**Opening table `tab:break-cases`.**

| case | failing hypothesis | status | evidence |
|---|---|---|---|
| TMD-sensitive $h_1h_2\to H_1H_2X$ | (H3)/(H4): colour entanglement | [V] | model counterexamples (CQ 2007; C07; RM 2010) |
| strict collinear factorization of amplitudes (space-like) | (H2) at amplitude level | [V] | explicit one-loop calculation (CdFR 2012) |
| mass-singularity factorization beyond NNLO | (H3) | [C] | CdFR; Becher et al. 2025 |
| gap-between-jets / non-global hadron-collider observables | (H3) | [V]/[P] | FSS 2012; SLLs (Ch15) |
| MPI-sensitive observables ($E_T$, beam thrust with vetoes) | (H3): spectator Glauber | [V] | Zeng 2015 (explicit); Gaunt 2014 |
| hadron–hadron hard diffraction | (H3)/(H4): gap survival | [V] | experiment (CDF) |
| diffractive DIS | none | [A] | Collins 1998 |
| double DY | (H3) holds | [A] | Diehl et al. 2016 |
| DPS with coloured final states | (H3) | [C] | — |

**Sections.**
1. `sec:break-overview` 组织：哪一条假设失效.
2. `sec:break-tmd` 强子—强子碰撞中 TMD 因子化的破坏 (`fig:violation-cq`).
3. `sec:break-spacelike` 类空共线极限、Coulomb 相位与 PDF 因子化.
4. `sec:break-mpi` 对多重相互作用敏感的观测量.
5. `sec:break-diffraction` 衍射 (`fig:diffraction`).
6. `sec:break-dps` 双部分子散射 (`fig:dps`).
7. `sec:break-summary` 小结.

**Canonical statements.**

* **定义 `def:break-generalized-tmd` — 标准与广义 TMD 因子化** (no tag). Following RM eqs. (2)–(3):
  - **Standard:** process-independent TMDs, up to the known T-reversal sign rule.
  - **Generalized:** single-hadron correlators with process- and colour-routing-dependent Wilson-line structures, e.g. BBMP (A11a):
    $$U^{[tt^*]}_{qq}=\frac1{N^2-1}\Big[(N^2+1)\frac{{\rm Tr}U^{[\square]}}NU^{[+]}-2U^{[\square]}U^{[+]}\Big].$$
    It contains "no matrix element of the form $\langle H_1H_2|\cdots|H_1H_2\rangle$".

  References: `Bomhof:2004aw`, `Bomhof:2006dp`, `BacchettaBomhofMuldersPijlman2005`.
* **命题 `prop:break-colour` — 单个额外胶子的色因子（胶子极强度）** [R, R_PT].
  - The pole parts of the eikonal attachments sum to $P=-\mathbf T_a-2\mathbf T_b$, so that
    $$C_G=1+\frac{2\langle\mathbf T_a\cdot\mathbf T_b\rangle}{C_F}.$$
  - Checks: SIDIS $+1$; DY $-1$.
  - Channel table, exact in $N$:
    - $qq'\to qq'$ ($tt^*$): $\frac{N^2-5}{N^2-1}=\frac12$;
    - $tu^*$: $-\frac{N^2+3}{N^2-1}=-\frac32$;
    - $q\bar q'\to q\bar q'$ ($tt^*$): $-\frac{N^2-3}{N^2-1}=-\frac34$;
    - $q\bar q\to q'\bar q'$ ($ss^*$): $\frac{N^2+1}{N^2-1}=\frac54$.
  - Graph by graph (QVY Table I): $C_I/C_u=-\frac2{N^2-1}$, $C_{F1}/C_u=-\frac1{N^2-1}$, $C_{F2}/C_u=\frac{N^2-2}{N^2-1}$.
  - Source: c_glauber §2.3, [C1–C5]; VF-GLA-6. Literature: `BacchettaBomhofMuldersPijlman2005` (Table I; eqs. (B5)–(B6)), `QiuVogelsangYuan2007` (eqs. (25)–(28)). *Proof:* full (colour algebra).
* **定理 `thm:break-tmd` — 强子—强子末态强子的 TMD 因子化不成立** [V].
  - **Standard TMD factorization fails** for TMD-sensitive observables in $h_1h_2\to H_1H_2X$:
    - `CollinsQiu2007`: SSA, abelian model, one extra gluon. The T-odd coefficient is $g_1+2g_2$, not $g_1$, so no Wilson line of hadron 1 can represent it.
    - `Collins2007`: unpolarized, abelian, two extra gluons. The anomaly is $4\pi^2g_2(g_2+g_1)\delta(l_1^+)\delta(l_2^+)$ (VF-GLA-7).
  - **Generalized TMD factorization fails** in a non-abelian theory (`RogersMulders2010`, double transverse-spin asymmetry). The entanglement test gives $\sum_{X,Y}C(X,Y)=C_F^2+\frac{4T_F^2(N^2-1)}{N^2}\ne C_F^2$ (SU(3): $24/9$ vs $16/9$; c_glauber [C6]; VF-GLA-10). In the abelian case "actual = product" identically.
  - **Survives** at the orders examined: collinear factorization ($\int d^2k_T(I_1+I_2)=0$).
  - **Not affected:** SIDIS, DY, $e^+e^-\to h_1h_2X$.
  - Further: `Rogers:2013zha` (extra spin asymmetries); `Vogelsang:2007jk` (abelian two-gluon results consistent with the gauge-link structure).

  *Proof:* sketch reproducing the eikonal algebra (`ex:break-c07`). Honest remark: the counterexamples are model calculations of a general method ("if methods fail in the model, they will also fail in QCD", C07). Their phenomenological size is not established. The CQ mechanism could first give uncancelled divergences in partonic cross sections at N$^3$LO.
* **命题 `prop:break-spacelike` — 类空共线极限中严格共线因子化的失效** [V] (amplitude level; critic O16).
  - CdFR 2012 (`CataniDeFlorianRodrigo2012`): for an incoming and an outgoing parton becoming collinear, the one-loop splitting amplitude depends on the colours of the non-collinear partons through $\mathbf T_2\cdot\mathbf T_3$ terms with $i\pi$ (their eq. (68)).
  - For $n\ge5$ (four coloured partons in the reduced $2\to2$ amplitude), $\mathbf T_2\cdot\mathbf T_3$ is not proportional to $1$. For three partons it is.
  - The one-loop breaking term is anti-Hermitian and cancels in $2{\rm Re}\langle M_0|M_1\rangle$ (c_glauber §4.1–4.2, checks S3–S7; VF-GLA-12; order of first violation per level: c_glauber §4.3 table).
  - **The DY collinear theorem stays [A].** M21: this does not show that PDF factorization fails.
* **命题 `prop:break-mass-singularity` — 超出 NNLO 的质量奇异性因子化** [C]. CdFR predict possible "entangled" logarithms from N$^3$LO (e.g. small-$Q_T$ dihadron/dijet). `Becher:2024kmk`: three-loop active–active Glauber terms restore consistency with PDF factorization below the veto scale. No general statement is proven.
* **命题 `prop:break-fss` — Coulomb 相位与软交换不对易导致的共线因子化破坏** [V].
  - `ForshawSeymourSiodmok2012`: the breakdown in gap-between-jets-type cross sections is driven by the non-commutation of Coulomb/Glauber exchanges with other soft exchanges.
  - Colour pattern (c_glauber §4.2, checks S5a–g; VF-GLA-9, VF-GLA-12, VF-GLA-13):
    - the tripole $\langle M|f_{abc}\mathbf T_i^a\mathbf T_j^b\mathbf T_k^c|M\rangle=0$ for real colour vectors (pure-QCD tree);
    - $\langle M|[A,D]|M\rangle=0$, i.e. no two-loop Coulomb × eikonal term;
    - $\langle M|[D,[D,A]]|M\rangle\ne0$ at three loops, which is the SLL structure.
  - Connection: `prop:jets-sll`.
* **命题 `prop:break-jet-veto` — 对多重部分子相互作用敏感的观测量** [V].
  - `Zeng:2015iba`: explicit counterexample. A leading-power longitudinal spin asymmetry of beam thrust arises from spectator Glauber exchange (QCD with scalar quarks).
  - `Gaunt2014`: for hadronic $E_T$ / transverse thrust, the CSS cancellation breaks down "at the level of two Glauber gluons exchanged between the spectators".
  - `Schwartz:2018obd`: pure Glauber ladders cancel for single-scale observables, so the leading violation needs at least one soft gluon (Lipatov vertex).
  - Which graphs violate first is not settled (c_glauber §1.6 item 3).
* **定义 `def:break-diffraction` — 衍射 DIS 与衍射部分子分布** (no tag).
  - Kinematics: $x_{\mathbb P}$, $\beta$, $t$.
  - $f^D_{i/p}(\beta,x_{\mathbb P},t;\mu)$ is the PDF operator with a detected final-state proton (`Berera:1995fj`).
  - Fracture functions: `Trentadue:1993ka`.
* **定理 `thm:break-ddis` — 衍射 DIS 的因子化** [A]. $d\sigma(\gamma^*p\to p'X)=\sum_i\hat\sigma_i\otimes f^D_{i/p}$ (`Collins1998a`).
  - 非微扰地位：MA1、MA2 (MA: audit).
  - *Proof:* sketch (Collins 1998 §III; c_glauber §3.2, checks D1a–c; VF-GLA-11). The detected proton belongs to the target subgraph A, whose final state is **constrained**, so the sum over the cuts of A is not available (unlike inclusive DIS). A soft gluon attached to A has its $r^-$ contour trapped (A contains initial- and final-state lines). The proof escapes by deforming $r^+$: near the soft region only final-state current-jet poles constrain $r^+$, A-collinear poles sit at $|r^+|\sim Q$, and the virtual photon has no spectators. Ward identities then factor the soft gluons, and the soft factor cancels in a region unaffected by the diffractive requirement. **Audit correction** (c_glauber §6 item 6): "one incoming hadron, hence no Glauber problem; final-state interactions summed" is **not** the argument and must not be written.
  - Fits: `H1:2006zyl`.
* **命题 `prop:break-hh-diffraction` — 强子—强子硬衍射中的因子化破坏** [V] (experimental; not a perturbative counterexample).
  - HERA diffractive PDFs overestimate Tevatron diffractive dijets by $O(10)$: `AffolderEtAl2000`, `CDF:1997gvd` ($W$), `CDF:2012nhl` (Run II recap); see also `CMS:2012odd`.
  - Mechanism: spectator interactions fill the gap ("gap survival", `Bjorken:1992er`). Unitarity protects only traces, not colour projections. In the dipole toy, singlet→octet leakage is quadratic in the phase difference, with coefficient $C_F/(2N)=\frac29$ (c_glauber §3.3–3.4, checks D2a–f).
  - Original proposal: `IngelmanSchlein1985`. Tests: `Alvero:1998ta`. Photoproduction analogue: `prop:coll-diffractive-photo`.
* **定义 `def:break-dpdf` — 双部分子分布与双 Drell–Yan** (no tag). $F_{ij}(x_1,x_2,y)$, with colour, spin and flavour correlations (`DiehlOstermeierSchafer2012`, `Manohar:2012jr`).
* **定理 `thm:break-double-dy` — 双 Drell–Yan 的因子化** [A]. 非微扰地位：MA1、MA2 (MA: audit).
  - Glauber cancellation to all orders, collinear and TMD: `Diehl:2015bca`.
  - Soft-gluon factorization: `Diehl:2018wfy`.
  - Double counting with single scattering solved: `Diehl:2017kgu`.
  - Sum rules: `Diehl:2018kgr`.
  - Open issues (`Diehl:2017wew`): evolution, positivity.
* **猜想 `conj:break-dps-coloured` — 有色末态的双部分子散射** [C].
* **猜想 `conj:break-pocket` — "口袋公式" $\sigma_{\rm DPS}=\sigma_A\sigma_B/\sigma_{\rm eff}$** [C]. This holds only if correlations and the $1\to2$ splitting are neglected. It is a model assumption, not a consequence of `thm:break-double-dy` (`Diehl:2017wew`, `Gaunt:2009re`, `Blok:2011bu`).

**Worked examples.**
* `ex:break-colour` — the C_G table from projectors, the abelian limit, and the entanglement test.
* `ex:break-c07` — Collins 2007's two-gluon anomaly (abelian scalar model), from c_glauber §2.4:
  - $I_1=\mathcal NF^2$ and $I_2=-\mathcal NG/(k_T^2+m_q^2)$, with closed forms;
  - b-space by Parseval, giving $\int d^2k_T(I_1+I_2)=0$;
  - the Cauchy–Schwarz proof that $I_1(0)+I_2(0)<0$;
  - the typo in C07 eq. (10) (VF-GLA-8).
* `ex:break-spacelike` — the colour structure of CdFR's one-loop space-like splitting (structure only).

**Figures.**
- Existing (tikz3, being redone): `fig:violation-cq`, `fig:diffraction`, `fig:dps`.
- Optional new: `fig:break-spacelike`.

**Misconception box.** M7, M21; "diffractive PDFs are universal" (only for DDIS); C8.

**Key citation keys.** `CollinsQiu2007`, `Collins2007`, `RogersMulders2010`, `Rogers:2013zha`, `Vogelsang:2007jk`, `Bomhof:2004aw`, `Bomhof:2006dp`, `BacchettaBomhofMuldersPijlman2005`, `QiuVogelsangYuan2007`, `AybatSterman2009`, `RothsteinStewart2016`, `CataniDeFlorianRodrigo2012`, `ForshawSeymourSiodmok2012`, `ForshawKyrieleisSeymour2006`, `Becher:2021zkk`, `Becher:2024kmk`, `Gaunt2014`, `Zeng:2015iba`, `Schwartz:2018obd`, `Collins1998a`, `Berera:1994xh`, `Berera:1995fj`, `Trentadue:1993ka`, `IngelmanSchlein1985`, `AffolderEtAl2000`, `CDF:1997gvd`, `CDF:2012nhl`, `CMS:2012odd`, `H1:2006zyl`, `H1:2007jtx`, `ZEUS:2007uvk`, `Bjorken:1992er`, `Alvero:1998ta`, `Collins:1992cv`, `Landshoff:1971zu`, `DiehlOstermeierSchafer2012`, `Diehl:2015bca`, `Diehl:2017kgu`, `Diehl:2018wfy`, `Diehl:2018kgr`, `Diehl:2017wew`, `Manohar:2012jr`, `Manohar:2012pe`, `Blok:2011bu`, `Gaunt:2009re`, `Buffing:2017mqm`, `DoriaFrenkelTaylor1980`, `Frenkel:1983di`, `Brandt:1988xt`.

---------------------------------------------------------------------------------------------------

# 第五部分 其他硬过程 (Part V — Other hard processes)

---------------------------------------------------------------------------------------------------

## Chapter 18 — 硬遍举过程 / Hard exclusive processes

`\label{ch:excl}` · `ch18_excl.tex` · **10 pp** · short format

**Purpose.** Amplitude-level factorization with distribution amplitudes (DAs) and generalized parton distributions (GPDs). The chapter covers:
- definitions, ERBL evolution, polynomiality;
- the pion electromagnetic and transition form factors;
- DVCS and longitudinal-photon meson production, which are [A];
- the endpoint problem and soft overlap, which are [P];
- the failure of standard collinear factorization for transverse photons, which is [V] (critic O18).

**Conventions (this chapter).**
- Use $n_A=(1^+,0^-,0_T)$ and $n_B=(0^+,1^-,0_T)$, **not** $\bar n,n$ ($\bar n,n$ are reserved for Ch14). c_exclusive's $\bar n$ is our $n_A$, and its $n$ is our $n_B$.
- $g_\perp^{\mu\nu}=g^{\mu\nu}-n_A^\mu n_B^\nu-n_B^\mu n_A^\nu$ and $\epsilon_\perp^{\mu\nu}=\epsilon^{\mu\nu\rho\sigma}n_{A\rho}n_{B\sigma}$, so $\epsilon_\perp^{12}=+1$, with $\epsilon^{0123}=+1$ and $\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3$ (VF-CONV-10). VGG 1999 use $\varepsilon_{0123}=+1$.
- $f_\pi\approx130$ MeV ($F_\pi=f_\pi/\sqrt2\approx92$ MeV).
- Ji's $\xi_{\rm Ji}=2\xi$.

**Depends on.** Ch3 (endpoint regions), Ch7 (operator definitions, light-ray operators), Ch8 (collinear Wilson lines).

**Sections.** `sec:excl-da` 分布振幅与 ERBL 演化; `sec:excl-ff` 介子形状因子 (`fig:pion-ff`); `sec:excl-endpoint` 端点区域与软重叠; `sec:excl-gpd` 广义部分子分布 (`fig:dvcs-handbag`); `sec:excl-dvcs` DVCS 与介子产生 (`fig:meson-production`).

**Canonical statements.**

* **定义 `def:excl-da` — 介子分布振幅** (no tag).
  $\langle0|\bar d(z)\gamma^+\gamma_5W[z,-z]u(-z)|\pi^+(p)\rangle=if_\pi p^+\int_0^1dx\,e^{i(2x-1)p^+z^-}\phi_\pi(x)$, with $z=(0^+,z^-,0_T)$ and $x$ the $u$-quark momentum fraction. Properties:
  - $\int\phi_\pi=1$;
  - moments are local twist-2 axial operators;
  - Gegenbauer expansion $\phi_\pi=6x\bar x\sum_na_nC_n^{3/2}(2x-1)$.

  Source: VF-EXC-1, VF-EXC-2; `Braun:2003rp`, eq. (140) after translation.
* **命题 `prop:excl-erbl` — 单圈 ERBL 演化** [R, R_PT]. 非微扰地位：MA0（强子 DA） (MA: audit).
  - Equation: $\mu^2\partial_{\mu^2}\phi=\frac{\alpha_s}{2\pi}V_0\otimes\phi$.
  - Kernel: $V_0(x,y)=C_F[\frac xy(1+\frac1{y-x})\theta(y-x)+\frac{\bar x}{\bar y}(1+\frac1{x-y})\theta(x-y)]_+$.
  - The Gegenbauer polynomials are eigenfunctions, with a proof for all $n$.
  - Anomalous dimensions: $\gamma_n=2C_F[1-\frac2{(n+1)(n+2)}+4\sum_{j=2}^{n+1}\frac1j]$, so $a_n\propto\alpha_s^{\gamma_n/(2\beta_0)}$; $\gamma_0=0$, $\gamma_2=\frac{25}3C_F$.
  - The eigenvalues equal the DGLAP non-singlet moments at $N=n+1$.
  - Asymptotic DA: $6x\bar x$.

  Source: VF-EXC-3/4/5. NLO ERBL is [R] at fixed order in the literature (`Braun:2003rp` §5), not redone here. *Proof:* full (c_exclusive §3).
* **定理 `thm:excl-pion-ff` — 介子电磁形状因子的因子化** [A]. At leading power:
  $F_\pi(Q^2)=\int dx\,dy\,\phi_\pi^*(y,\mu)T_H(x,y,Q,\mu)\phi_\pi(x,\mu)+O(\Lambda^2/Q^2)$.
  - Literature: `Lepage:1979zb`, `LepageBrodsky1980`, `EfremovRadyushkin1980`, `Efremov:1978rn`, `Duncan:1979ny`, `Duncan:1979hi`, `Chernyak:1977as`, `ChernyakZhitnitsky1984`, `Farrar:1979aw`.
  - 非微扰地位：MA1、MA2.

  **地位与缺口:** at accessible $Q^2$, endpoint and soft-overlap contributions may dominate (`prop:excl-endpoint`).
* **命题 `prop:excl-pion-lo` — 领头阶硬核** [R, R_PT].
  - Hard kernel: $T_H=\frac{2\pi C_F\alpha_sf_\pi^2}{N_cQ^2}\big[\frac{e_u}{\bar x\bar y}+\frac{e_{\bar d}}{xy}\big]$.
  - For a general DA: $Q^2F_\pi=\frac{2\pi C_F}{N_c}\alpha_sf_\pi^2[e_u|\int\frac\phi{\bar x}|^2+e_{\bar d}|\int\frac\phi x|^2]$.
  - Asymptotic limit: $Q^2F_\pi\to8\pi\alpha_sf_\pi^2$.
  - There are exactly four $O(\alpha_s)$ graphs in Feynman gauge. Only the pairs A+B and C+D are gauge invariant (c_exclusive §10 item 3).

  Source: VF-EXC-6. *Proof:* full (worked example).
* **定理 `thm:excl-transition` — $\gamma^*\gamma\to\pi^0$ 形状因子** [A].
  - Formula: $Q^2F_{\gamma^*\gamma\pi}=\frac{\sqrt2f_\pi}3\int_0^1dx\frac{\phi_\pi(x)}x+O(\alpha_s)\to\sqrt2f_\pi$ (VF-EXC-7; BaBar normalization).
  - Higher orders: NNLO in `Gao:2021iqq`.
  - Data: `CELLO:1990klc`, `CLEO:1997fho`, `BaBar:2009rrj`, `Belle:2012wwz`.
* **命题 `prop:excl-endpoint` — 端点区域与软重叠** [P].
  - The soft (Feynman) mechanism competes numerically at accessible $Q^2$ (`IsgurLlewellynSmith1984`, `Isgur:1988iw`). Its formal power counting is $1/Q^4$, quoted as a remark with citation (c_exclusive §10 item 6).
  - The Sudakov/$k_T$ resummation scheme (`LiSterman1992`) is model dependent.
  - Endpoint behaviour: `fig:excl-endpoint` (optional; adapt c_exclusive `fig:cex-endpoint`).
* **定义 `def:excl-gpd` — 广义部分子分布** (no tag).
  - Ji's $H,E,\tilde H,\tilde E$, in the light-front normalization of `Diehl2003`.
  - Kinematics $\xi$, $t$.
  - Forward limits: $H(x,0,0)=q(x)$, $\tilde H(x,0,0)=\Delta q(x)$.

  References: `Ji1997a`, `Ji1997b`, `Radyushkin:1996nd`, `Radyushkin1997`, `Diehl2003`, `BelitskyRadyushkin2005`.
* **命题 `prop:excl-polynomiality` — 多项式性与 Ji 求和规则** [R, R_def]. 非微扰地位：MA0 (MA: audit).
  - $\int dx\,H=F_1(t)$.
  - $\int dx\,xH=A(t)+4\xi^2C(t)$.
  - $\int dx\,x(H+E)=A+B$, hence $J^q=\frac12[A^q(0)+B^q(0)]$.
  - The D-term: `Polyakov:1999gs`.

  Source: VF-EXC-12. *Proof:* full (Lorentz covariance of local matrix elements).
* **定理 `thm:excl-dvcs` — DVCS 的因子化** [A]. 非微扰地位：MA1、MA2 (MA: audit).
  - Literature: `CollinsFreund1999`, `JiOsborne1998`.
  - Per Collins–Freund, the issues are the collinear region (Ward identities → Wilson line) and the endpoint/breakpoint regions $x=\pm\xi$. Do **not** say that "soft gluons cancel by Ward identities" (c_exclusive §10 item 11).
* **命题 `prop:excl-dvcs-lo` — DVCS 领头阶系数函数** [R, R_PT].
  $$T^{\mu\nu}=g_\perp^{\mu\nu}\sum_qe_q^2\!\int\!dx\,F^q\Big[\frac1{x-\xi+i0}+\frac1{x+\xi-i0}\Big]-i\epsilon_\perp^{\mu\nu}\sum_qe_q^2\!\int\!dx\,\tilde F^q\Big[\frac1{x-\xi+i0}-\frac1{x+\xi-i0}\Big]$$
  The overall sign is tied to the definition of $T^{\mu\nu}$ in `def:dis-compton`. DIS limit check: ${\rm Im}\,T^{11}=2\pi F_1$.

  Source: VF-EXC-8/9/10. Ji's arXiv v1 prints the second denominator as "$x+\xi/2+i\epsilon$"; the correct sign is $-i0$ (c_exclusive §10 item 4).
* **定理 `thm:excl-meson-L` — 纵向光子介子产生的因子化** [A]. 非微扰地位：MA1、MA2 (MA: audit).
  - Literature: `CollinsFrankfurtStrikman1997`.
  - Leading order, for the pseudoscalar case: $\varepsilon_L\cdot A_\pi=-i\frac{C_F}{N_c}\frac{4\pi\alpha_sf_\pi}Q\int dz\,\phi_\pi(z)\int dx\big[\frac{e_a}{\bar z(x-\xi+i0)}+\frac{e_b}{z(x+\xi-i0)}\big]\tilde F^{ba}$ (VF-EXC-11; agrees with VGG eqs. (48), (59)).
  - Further references: `Vanderhaeghen:1999xj`, `Mankiewicz:1997uy`, `Frankfurt:1999fp` (the pion pole of $\tilde E$; **not** PRL 84 (2000) 2589, which is about decuplet baryons).
* **命题 `prop:excl-meson-T` — 横向光子：标准共线因子化失效** [V].
  - The leading-twist $\gamma_T^*\to V_T$ amplitude vanishes to all orders. This is chirality and helicity conservation, with status [A] (`Diehl:1998pd`, `CollinsDiehl2000`).
  - At twist 3, in the Wandzura–Wilczek approximation, the integrals diverge **logarithmically** at the endpoints, because $g_\perp^{(v)}(0)=\frac12\int du\,\phi_\parallel(u)/u\ne0$. Endpoint suppression of $\phi_\parallel$ therefore does not help. In addition the GPD convolutions have double poles $(\xi\mp x-i0)^{-2}$ (`Mankiewicz:1999tt`; c_exclusive §10 item 10).
  - Do not quote MP's "$9/\tau$".
  - Phenomenological models: `Goloskokov:2005sd`.
* **注 `rem:excl-hadron-scattering` — 宽角强子散射**. Constituent counting (`BrodskyFarrar1973`), the Landshoff pinch (`Landshoff:1974ew`), and its Sudakov suppression (`Botts:1989kf`) are all [P].

**Worked example.** `ex:excl-pion-ff-lo` — the four graphs, the Fierz projectors (`App A`), the hard kernel, and the asymptotic limit $8\pi\alpha_sf_\pi^2$ (c_exclusive §4; `tex/c_exclusive_formfactors.tex` is a ready draft).

**Figures.**
- Existing (tikz3, being redone): `fig:pion-ff`, `fig:dvcs-handbag`, `fig:meson-production`.
- Optional new: `fig:excl-erbl` (adapt `fig:cex-erbl-graphs`), `fig:excl-endpoint` (adapt `fig:cex-endpoint`).

**Key citation keys.** `Lepage:1979zb`, `LepageBrodsky1980`, `EfremovRadyushkin1980`, `Efremov:1978rn`, `Duncan:1979ny`, `Duncan:1979hi`, `Chernyak:1977as`, `ChernyakZhitnitsky1984`, `Farrar:1979aw`, `Brodsky:1980ny`, `Brodsky:1981rp`, `Braun:2003rp`, `IsgurLlewellynSmith1984`, `Isgur:1988iw`, `LiSterman1992`, `BrodskyFarrar1973`, `Landshoff:1974ew`, `Botts:1989kf`, `CELLO:1990klc`, `CLEO:1997fho`, `BaBar:2009rrj`, `Belle:2012wwz`, `Gao:2021iqq`, `Ji1997a`, `Ji1997b`, `Ji:1998pc`, `Radyushkin:1996nd`, `Radyushkin1997`, `Diehl2003`, `BelitskyRadyushkin2005`, `Goeke:2001tz`, `Belitsky:2001ns`, `Polyakov:1999gs`, `CollinsFreund1999`, `JiOsborne1998`, `CollinsFrankfurtStrikman1997`, `Vanderhaeghen:1999xj`, `Mankiewicz:1997uy`, `Frankfurt:1999fp`, `Diehl:1998pd`, `CollinsDiehl2000`, `Mankiewicz:1999tt`, `Goloskokov:2005sd`, `Diehl:1998sm`.

---------------------------------------------------------------------------------------------------

## Chapter 19 — 重夸克物理：$B$ 介子衰变与重夸克偶素 / Heavy-quark physics: $B$ decays and quarkonium

`\label{ch:heavy}` · `ch19_heavy.tex` · **9 pp** · short format

**Purpose.** Factorization with a heavy-quark scale. The chapter covers:
- exclusive $B\to D\pi$, which is [A];
- QCD factorization (QCDF) for charmless $B\to M_1M_2$: leading power [P], power corrections [V], the $X_A,X_H$ models;
- inclusive $B$ decays: the OPE in $1/m_b$ and the shape-function region;
- quarkonium: NRQCD decays [A], production [C].

**Depends on.** Ch14 (SCET, BPS decoupling), Ch18 (DAs), Ch6 (OPE).

**Sections.** `sec:heavy-bdpi` $B\to D\pi$ (`fig:heavy-bdpi`); `sec:heavy-qcdf` 无粲 $B$ 衰变的 QCD 因子化 (`fig:heavy-qcdf`); `sec:heavy-inclusive` 单举 $B$ 衰变; `sec:heavy-nrqcd` 重夸克偶素：NRQCD (`fig:nrqcd`).

**Canonical statements.**

* **定理 `thm:heavy-bdpi` — $B\to D\pi$ 的全阶因子化** [A]. At leading power and all orders in $\alpha_s$:
  $\langle D\pi|O|B\rangle=N\,F^{B\to D}(0)\int_0^1dx\,T(x,\mu)\phi_\pi(x,\mu)$, with $N=\frac i2m_BE_\pi f_\pi$ for $O_{\bf0}=[\bar c\gamma^\mu P_Lb][\bar d\gamma_\mu P_Lu]$, $P_L=\frac12(1-\gamma_5)$ ($O_{\bf8}$ with $T^a\otimes T^a$; VF-BQ-6, audit), for $\bar B^0\to D^+\pi^-$ and $B^-\to D^0\pi^-$.
  - BPS write $F^{B\to D}(0)$, not $F(m_\pi^2)$; the difference is power suppressed.
  - The endpoint-suppression **assumption** is part of the statement (c_scet §6 item 7).
  - Literature: `BauerPirjolStewart2001`; the two-loop IR demonstration `BenekeEtAl2000` (which "does not accomplish an all-order 'proof'"); NNLO kernel `Huber:2016xod`; colour transparency `Bjorken:1988kk`, `Dugan:1990de`, `Politzer:1991au`.
  - 非微扰地位：MA1、MA2.
* **命题 `prop:heavy-qcdf-lp` — 无粲两体衰变的领头幂次 QCD 因子化** [P]. 非微扰地位：MA1、MA2 (MA: audit). The formula (BBNS) is
  $\langle M_1M_2|Q_i|\bar B\rangle=F^{B\to M_1}(0)\int dx\,T^{\rm I}_i(x)\phi_{M_2}(x)+\int d\xi\,dx\,dy\,T^{\rm II}_i(\xi,x,y)\phi_B(\xi)\phi_{M_1}(y)\phi_{M_2}(x)$.
  - One-loop vertex term: $V_M=12\ln\frac{m_b}\mu-18+\int_0^1g\,\Phi_M$. The coefficient 12 is forced by $\mu$-independence. $\int g\Phi_M=-\frac12-3i\pi+(\frac{11}2-3i\pi)\alpha_1^M-\frac{21}{20}\alpha_2^M$ (VF-BQ-1/2).
  - IR finiteness is established explicitly through NNLO for $T^{\rm I}$ (`Bell:2007tv`, `Bell:2009nk`, `Beneke:2009ek`; penguins `Bell:2015koa`, `Bell:2020qus`) and at one loop for $T^{\rm II}$ (`Beneke:2005vv`, `Beneke:2006mk`, `Kivel:2006xc`, `Pilipp:2007mg`; jet function `Beneke:2005gs`).
  - SCET derivation: `Bauer:2004tj` (BPRS), with `Beneke:2003pa` and `Hill:2002vw`.

  **地位与缺口:**
  - Tag [P] (survey item 18, more conservative than critic O19's [A]).
  - The open BBNS–BPRS dispute on charming penguins is reported without a verdict (`Beneke:2004bn` vs `Bauer:2005wb`).
* **命题 `prop:heavy-qcdf-endpoint` — 幂次修正中的端点发散** [V].
  - The annihilation and twist-3 spectator terms are divergent convolutions at $O(\alpha_s)$: $X_A=\int_0^1\frac{dy}y$, $X_H=\int_0^1\frac{dy}{1-y}\Phi_p(y)$.
  - The model $X=(1+\varrho e^{i\varphi})\ln\frac{m_B}{\Lambda_h}$, $\varrho\le1$, $\Lambda_h=0.5$ GeV is a **model** (VF-BQ-3/4; `BenekeNeubert2003`). Typo: "$\ln(m_M/\Lambda_h)$" must read $m_B$ (c_scet §6 item 17).
  - Annihilation coefficients in the $X_A$ model: VF-BQ-5.
  - Refactorization of these endpoint divergences is [C]. There are case-by-case successes elsewhere (`Liu:2019oav`, `Liu:2020wbn`, `Liu:2022ajh`, `Hurth:2023paz`) and attempts for annihilation (`Lu:2022kos`).
  - Colour-suppressed $B\to D^0M^0$: `Mantry:2003uz`.
* **定理 `thm:heavy-inclusive-b` — 单举 $B$ 衰变的重夸克展开** [A]. 非微扰地位：MA0、MA4 (MA: audit).
  - OPE in $1/m_b$ for total and inclusive semileptonic rates, with no $1/m_b$ term (`ChayGeorgiGrinstein1990`, `BigiUraltsevVainshtein1992`, `ManoharWise1994`, `BigiEtAl1994`).
  - In the endpoint/shape-function region: factorization into hard × jet × shape function (`Neubert1994a`, `Neubert1994b`, `KorchemskySterman1994`, `BauerFlemingLuke2000`, `Bauer:2003pi`, `Lange:2003ff`, `Becher:2006qw`).
  - Local quark–hadron duality is assumed ([C], `conj:ee-duality`).
  - Pole-mass renormalon: `Bigi:1994em`, `Beneke:1994sw`.
* **定义 `def:heavy-nrqcd` — NRQCD 及其幂次计数** (no tag).
  - Velocity rules: $\psi\sim(mv)^{3/2}$, $D\sim mv$, $D_t\sim mv^2$, $gE\sim m^2v^3$, $gB\sim m^2v^4$ (VF-NRQ-1; `CaswellLepage1986`, `BodwinBraatenLepage1995` §II).
  - BBL use $D=\partial+igA$, so the signs of the $c_{2,3,4}$ bilinears flip under CONTEXT's convention (c_scet §6 item 9).
* **定理 `thm:heavy-nrqcd-decay` — 衰变的 NRQCD 因子化** [A]. $\Gamma=\sum_n\frac{2{\rm Im}f_n}{m_Q^{d_n-4}}\langle H|O_n|H\rangle$, where $m_Q$ is the heavy-quark pole mass (BBL §II.F–G; P-wave consistency `Bodwin:1992ye`). 非微扰地位：MA1、MA2 (MA: audit).
* **命题 `prop:heavy-nrqcd-matching` — 匹配系数** [R, R_PT].
  - $\Gamma(^3S_1\to e^+e^-)=\frac{N_ce_Q^2\alpha^2|R(0)|^2}{3m_Q^2}$.
  - $\Gamma(^1S_0\to\gamma\gamma)=\frac{4N_ce_Q^4\alpha^2|R(0)|^2}{M^2}$, with $M=2m_Q$.
  - One loop: $c_v=1-2C_F\frac{\alpha_s}\pi$, so $\Gamma(V\to e^+e^-)\propto1-\frac{16\alpha_s}{3\pi}$ (VF-NRQ-2/3/4; `VanRoyen:1967nq`, `Barbieri:1975ki`, `Celmaster:1978yz`, `Barbieri:1979be`).

  *Proof:* full at one loop (`ex:heavy-cv`).
* **猜想 `conj:heavy-nrqcd-production` — 产生的 NRQCD 因子化** [C].
  - Formula: $\sigma=\sum_nF_n\langle O_n^H\rangle/m_Q^{d_n-4}$ (BBL §VI.A).
  - At NNLO, IR poles appear that conventional octet operators do not match. Gauge-completed operators with Wilson lines restore factorization at that order, which is [P] (`NayakQiuSterman2005a`, `NayakQiuSterman2005b`, `NayakQiuSterman2006`).
  - Possible further non-local operators at higher orders.
  - Universality and polarization tensions: `Butenschoen:2010rq`, `Butenschoen:2011yh`, `Butenschoen:2012px`, `Chao:2012iv`, `BrambillaEtAl2011`, `Lansberg:2019adr`.
* **命题 `prop:heavy-quarkonium-fragmentation` — 大 $p_T$ 重夸克偶素产生** [A] for the perturbative-QCD part, [C] for the NRQCD step. Leading-power plus NLP factorization in $m_Q^2/p_T^2$ (`Kang:2011mg`, `Fleming:2012wy`). 非微扰地位：MA1、MA2 (MA: audit).

**Worked example.** `ex:heavy-cv` — the one-loop $c_v$ at threshold in DR:
- vertex $a(\frac3\varepsilon-4+3\ln\frac{\mu^2}{m^2})$;
- $\delta Z_2^{\rm OS}=-a(\frac3\varepsilon+4+3\ln\frac{\mu^2}{m^2})$;
- the Coulomb singularity is separated and matched by the NRQCD potential.

c_scet `s3` is the source; check against BBL App. A.

**Figures.** existing (tikz3, being redone): `fig:nrqcd`; new: `fig:heavy-bdpi`, `fig:heavy-qcdf`.

**Key citation keys.** `BenekeEtAl1999`, `BenekeEtAl2000`, `BenekeEtAl2001`, `BenekeNeubert2003`, `BauerPirjolStewart2001`, `Bauer:2004tj`, `Beneke:2004bn`, `Bauer:2005wb`, `Beneke:2003pa`, `Hill:2002vw`, `Beneke:2005gs`, `Beneke:2005vv`, `Beneke:2006mk`, `Kivel:2006xc`, `Pilipp:2007mg`, `Bell:2007tv`, `Bell:2009nk`, `Beneke:2009ek`, `Bell:2015koa`, `Bell:2020qus`, `Huber:2016xod`, `Mantry:2003uz`, `Bjorken:1988kk`, `Dugan:1990de`, `Politzer:1991au`, `Bauer:2002aj`, `Lange:2003ff`, `Grozin:1996pq`, `Liu:2019oav`, `Liu:2020wbn`, `Liu:2022ajh`, `Hurth:2023paz`, `Lu:2022kos`, `Bell:2024bxg`, `ChayGeorgiGrinstein1990`, `BigiUraltsevVainshtein1992`, `ManoharWise1994`, `BigiEtAl1994`, `Neubert1994a`, `Neubert1994b`, `KorchemskySterman1994`, `BauerFlemingLuke2000`, `Bauer:2003pi`, `Becher:2006qw`, `Bigi:1994em`, `Beneke:1994sw`, `CaswellLepage1986`, `BodwinBraatenLepage1995`, `Bodwin:1992ye`, `Lepage:1992tx`, `VanRoyen:1967nq`, `Barbieri:1975ki`, `Barbieri:1975am`, `Celmaster:1978yz`, `Barbieri:1979be`, `Harris:1957zza`, `NayakQiuSterman2005a`, `NayakQiuSterman2005b`, `NayakQiuSterman2006`, `Butenschoen:2010rq`, `Butenschoen:2011yh`, `Butenschoen:2012px`, `Chao:2012iv`, `Kang:2011mg`, `Fleming:2012wy`, `BrambillaEtAl2005`, `BrambillaEtAl2011`, `Lansberg:2019adr`.

---------------------------------------------------------------------------------------------------

# 第六部分 极限与展望 (Part VI — Limits)

---------------------------------------------------------------------------------------------------

## Chapter 20 — 幂次修正、次领头幂次、重整化子与非微扰地位 / Power corrections, next-to-leading power, renormalons, non-perturbative status

`\label{ch:power}` · `ch20_power.tex` · **12 pp** · full

**Purpose.** State what is known beyond leading power and beyond perturbation theory:
- twist 4 in DIS, in $x$-space;
- twist 3 and single-spin asymmetries;
- next-to-leading-power (NLP) factorization and endpoint divergences (M22);
- renormalons: large-$\beta_0$ results are [P], and the general correspondence with higher twist is [C] (critic O20);
- the honest non-perturbative status of every theorem, with the only genuinely non-perturbative "laboratories" (critic O21): convergence of the OPE in perturbative $\varphi^4$, the 't Hooft model, and lattice evidence (Ch21).

**Depends on.** Ch5 (OPE, condensates), Ch6 (twist, `prop:dis-twist4`), Ch11 (`thm:dy-higher-twist`), Ch12 (NLP threshold), Ch13 (Sivers), Ch14 (SCET at subleading power).

**Sections.**
1. `sec:power-twist4` DIS 的扭度 4：从矩到 $x$ 空间 (`fig:higher-twist`, owned by Ch6).
2. `sec:power-twist3` 扭度 3 与单自旋不对称 (`fig:twist3-ssa`).
3. `sec:power-nlp` 次领头幂次：次软定理与端点发散.
4. `sec:power-renormalons` 重整化子 (`fig:renormalon-chain`, `fig:power-borel-plane`).
5. `sec:power-np` 非微扰地位与可解模型.

**Canonical statements.**

* **命题 `prop:power-dis-twist4-x` — DIS 扭度 4 修正的 $x$ 空间形式** [A]. $F_2(x,Q^2)=F_2^{\rm tw2}+\frac1{Q^2}\sum_i\int dx_1dx_2\,H_i(x_1,x_2,x)\,T^{(4)}_i(x_1,x_2)+\dots$, with quark–gluon correlators $T^{(4)}$. 非微扰地位：MA1、MA2、MA4 (MA: audit).
  - Moment space: [R, 以 OPE 为前提] (`prop:dis-twist4`).
  - $x$ space: [A] (`EllisFurmanskiPetronzio1982`, `EllisFurmanskiPetronzio1983`, `Jaffe:1982pm`, `Qiu:1988dn`).
  - Twist-4 contributions mix with the leading twist through renormalon ambiguities (`conj:power-renormalon-ht`).
  - Nuclear enhancement: `prop:disall-nuclear`.
* *(Audit: the ETQS correlator is now defined in Ch13 as `def:tmd-etqs` — formerly “def:power-etqs”（已废弃） — because `prop:tmd-twist3-matching` needs it there; this chapter refers back.)*
* **命题 `prop:power-twist3-sidis` — SIDIS 型过程中的扭度 3 共线因子化** [P].
  - Single-spin asymmetries at $P_{hT}\sim Q$ factorize at twist 3; explicit at one loop and NLO in specific processes (`Ji:2006ub`, `Vogelsang:2009pj`).
  - The evolution of $T_F(x,x)$ is settled (`Braun:2009mi` vs `Kang:2008ey`).
  - Relation to the Sivers function: $gT_F(x,x)=\mp\int d^2k_T\frac{k_T^2}Mf^{\perp q}_{1T}(x,k_T)|_{\rm SIDIS}$, as in `prop:tmd-twist3-matching` (Ch13; $T_F$ defined in `def:tmd-etqs`). Sign and normalization are convention dependent (`Boer:2003cm`; **(verify)**).
* **猜想 `conj:power-twist3-pp` — 强子—强子碰撞中单举强子单自旋不对称的扭度 3 因子化** [C]. Covers $p^\uparrow p\to hX$ (`QiuSterman1991c`, `Qiu:1998ia`) and direct photons (`QiuSterman1992`). It inherits `conj:dy-coloured-final`: no all-order argument exists even at leading twist for coloured final states. On the "sign mismatch": `Kang:2011hk`, `Cammarota:2020qcw`.
* **命题 `prop:power-next-to-soft` — 次软定理** [R, R_PT].
  - Tree level: the Low–Burnett–Kroll theorem. The amplitude for emitting a soft photon through order $k^0$ is fixed by the non-radiative amplitude and its derivatives (`Low1958`, `BurnettKroll1968`).
  - Extension to collinear regions: `DelDuca1990`. Loop-level validity in QCD is [A].
  - This is the starting point of NLP threshold factorization (Ch12).
* **命题 `prop:power-nlp-endpoint` — 次领头幂次因子化与端点发散** [P].
  - At NLP the naive convolutions diverge at the endpoints (M22).
  - Refactorizations exist case by case:
    - LL DY/Higgs threshold at NLP (`Beneke:2018gvs`, `Beneke:2019mua`);
    - $h\to\gamma\gamma$ through a $b$-quark loop (`Liu:2019oav`, `Liu:2020wbn`);
    - $gg\to h$ (`Liu:2022ajh`);
    - $B\to X_s\gamma$ (`Hurth:2023paz`);
    - DIS at large $x$ (`Beneke:2022obx`; NLP DIS preprint `Beneke:2026miy`).
  - No general theorem exists. $B\to M_1M_2$: `prop:heavy-qcdf-endpoint` ([V]).
* **定义 `def:power-borel` — Borel 变换与重整化子** (no tag).
  - For $R=\sum_nr_n\alpha_s^{n+1}$: $B[R](t)=\sum_nr_nt^n/n!$ and $R=\int_0^\infty dt\,e^{-t/\alpha_s}B[R](t)$.
  - With $u=\beta_0t/(4\pi)$ (binding $\beta_0$), $e^{-t/\alpha_s(\mu)}=(\Lambda^2/\mu^2)^u$ at one loop. So a pole at $u=u_0>0$ produces an ambiguity $\propto(\Lambda^2/Q^2)^{u_0}$.
  - IR renormalons sit at $u>0$, UV renormalons at $u<0$.
  - Large-order behaviour: $r_n\sim n!\,(\beta_0/4\pi u_0)^n n^\gamma$.
* **命题 `prop:power-adler-large-beta0` — 大 $\beta_0$ 极限下的 Adler 函数** [P] (critic O20).
  - In the large-$\beta_0$ (bubble-chain) approximation, $B[D](u)$ has IR renormalon poles at $u=2,3,\dots$ and **none at $u=1$**, consistent with the absence of a dimension-2 gauge-invariant operator. The $u=2$ pole matches $\langle\frac{\alpha_s}\pi G^2\rangle$.
  - UV renormalon poles sit at $u=-1,-2,\dots$.
  - The closed form, including the $\overline{\rm MS}$ scheme constant $e^{5u/3}$, is to be transcribed from `Beneke1999` §5 (also `Beneke1993`, `Broadhurst1993`, `BenekeBraun1995a`) **(to verify)**.

  *Proof:* full `proof` in the large-$\beta_0$ limit (`ex:power-renormalon-chain`); the [P] records that only this limit is established (§0.8). Mueller's analysis: `Mueller1985`.
* **命题 `prop:power-renormalon-examples` — 若干过程中的重整化子与幂次修正** [P]. All in the large-$\beta_0$ approximation:
  - DIS: $1/Q^2$ (`DasguptaWebber1996`).
  - Inclusive DY: no $1/Q$ (`BenekeBraun1995b`).
  - $e^+e^-$ longitudinal cross section: $1/Q$ (`BenekeBraunMagnea1997`).
  - Event shapes: $1/Q$ (`Korchemsky:1994is`, `DokshitzerWebber1995`).
  - Pole mass: $u=\frac12$, which is why short-distance masses are preferred (`Bigi:1994em`, `Beneke:1994sw`).
  - Quasi-PDFs: `Braun:2018brg`.
  - Lattice high-order evidence: `Bali:2014fea`.
* **猜想 `conj:power-renormalon-ht` — 红外重整化子与高扭度的一般对应** [C]. In general, IR-renormalon ambiguities of leading-twist coefficient functions cancel against UV ambiguities of higher-twist matrix elements, one to one (`Mueller1985`, `David:1983gz`, `David:1985xj`, `Novikov:1984rf`, `tHooft1979`). There is no non-perturbative definition of the OPE in QCD (survey item 22).
* **注 `rem:power-np-status` — 非微扰地位**.
  - Every factorization theorem of this book is a statement in perturbation theory, or about perturbation theory plus MA0–MA4 (`def:intro-MA`).
  - QCD has not been constructed as a 4D QFT (M28).
  - Given MA0, the following are non-perturbative: analyticity, positivity of spectral functions, support (`prop:pdf-support-hadron`), and sum rules.
  - The cleanest non-perturbative link is the lattice evaluation of local twist-2 matrix elements (Ch21).
* **定理 `thm:power-ope-convergence` — 微扰 $\varphi^4_4$ 中 OPE 的收敛性** [R, R_PT]. In massive Euclidean $\varphi^4$ theory in four dimensions, at each order of perturbation theory, the OPE of a product of composite fields converges at finite separation, not only asymptotically (`Hollands:2011gf`, `Holland:2014pna`; the curved-space framework is `Hollands:2006ag`). It is a model statement; for QCD see `thm:dis-ope`.
* **命题 `prop:power-thooft-model` — 't Hooft 模型** [P] (exact, but only in 2D QCD at large $N_c$). Bjorken scaling holds and the structure functions are computable exactly from the meson wave functions (`tHooft1974`, `CallanCooteGross1976`, `Einhorn1976`). It is the only setting in which "parton distributions of a bound state" are computed non-perturbatively from first principles.

**Worked examples.**
* `ex:power-sgp` — the soft-gluon-pole mechanism at lowest order. The phase comes from $\frac1{k^+\pm i0}$ (VF-WL-12), and its sign is linked to the Sivers sign.
* `ex:power-renormalon-chain` — one gluon with $n$ fermion bubbles. Its Borel transform shows the structure of `prop:power-adler-large-beta0` (no $u=1$ pole).

**Figures.**
- Existing (tikz3, being redone): `fig:renormalon-chain`, `fig:twist3-ssa` (owned); `fig:higher-twist` (owned by Ch6 since the audit; refer back).
- New: `fig:power-borel-plane`.

**Misconception box.** M10, M22, M28; C11.

**Key citation keys.** `EllisFurmanskiPetronzio1982`, `EllisFurmanskiPetronzio1983`, `Jaffe:1982pm`, `Jaffe1983`, `Qiu:1988dn`, `QiuSterman1991a`, `QiuSterman1991b`, `EfremovTeryaev1985`, `Efremov:1981sh`, `QiuSterman1991c`, `QiuSterman1992`, `Qiu:1998ia`, `Ji:2006ub`, `Vogelsang:2009pj`, `Braun:2009mi`, `Kang:2008ey`, `Kang:2011hk`, `Cammarota:2020qcw`, `Boer:2003cm`, `Low1958`, `BurnettKroll1968`, `DelDuca1990`, `Beneke:2018gvs`, `Beneke:2019mua`, `Beneke:2022obx`, `Beneke:2026miy`, `Liu:2019oav`, `Liu:2020wbn`, `Liu:2022ajh`, `Hurth:2023paz`, `tHooft1979`, `Mueller1985`, `David:1983gz`, `David:1985xj`, `Novikov:1984rf`, `Beneke1993`, `Broadhurst1993`, `Beneke1999`, `BenekeBraun1995a`, `BenekeBraun1995b`, `BenekeBraunMagnea1997`, `DasguptaWebber1996`, `DokshitzerWebber1995`, `Korchemsky:1994is`, `Bigi:1994em`, `Beneke:1994sw`, `Bali:2014fea`, `Braun:2018brg`, `Hollands:2011gf`, `Holland:2014pna`, `Hollands:2006ag`, `tHooft1974`, `CallanCooteGross1976`, `Einhorn1976`, `Shifman2000`.

---------------------------------------------------------------------------------------------------

## Chapter 21 — 格点 QCD 与因子化 / Lattice QCD and factorization

`\label{ch:lattice}` · `ch21_lattice.tex` · **8 pp** · short format

**Scope note (audit).** REQUIREMENTS.md 3b asks for Ji's LaMET factorization proofs (and Yizhuang Liu's work) in 「详尽严格完整」 form; this 8-pp short chapter cannot hold them. See §0.9 item 1: the lead author must decide whether LaMET moves to a full frontier chapter before this chapter is written.

**Purpose.** Lattice QCD supplies non-perturbative matrix elements. It does **not** test the factorization of hadronic cross sections (C12). The chapter covers:
- moments of local twist-2 operators and the lattice Compton amplitude;
- quasi-PDFs, pseudo-PDFs and lattice cross sections, which rest on their own factorization theorems ([A]; Euclidean OPE);
- renormalization of Wilson-line operators;
- the lattice Collins–Soper kernel;
- the critiques.

**Depends on.** Ch6 (`prop:dis-dispersion`, `thm:dis-ope`), Ch7 (`thm:pdf-moments-local`), Ch13 (`prop:tmd-evolution`).

**Sections.** `sec:lattice-moments` 矩与格点 Compton 振幅; `sec:lattice-quasi` 准分布、赝分布与格点截面 (`fig:quasi-pdf`); `sec:lattice-matching` 匹配定理 (`fig:lattice-matching`); `sec:lattice-tmd` 格点 TMD 与 Collins–Soper 核; `sec:lattice-status` 批评与地位.

**Canonical statements.**

* **命题 `prop:lattice-moments` — 格点可计算的矩** [R, 以 OPE 为前提].
  - (a) By `thm:pdf-moments-local`, the PDF moments are forward matrix elements of local twist-2 operators, i.e. Euclidean-accessible quantities ($R_{\rm def}$ content).
  - (b) The Euclidean forward Compton amplitude $T^{\mu\nu}(\omega,Q^2)$ at $|\omega|<1$ can be computed on the lattice. Its Taylor coefficients equal the structure-function moments (`prop:dis-dispersion`). Their OPE decomposition gives $C^{(n)}A^{(n)}$ (`DetmoldLin2006`, `ChambersEtAl2017`).
  - 非微扰地位：MA0、MA4.
  - Lattice renormalization and the continuum limit are numerical [P].
* **定义 `def:lattice-quasi` — 准分布、赝分布与格点截面** (no tag).
  - Quasi-PDF: $\tilde q(x,P^z)=\int\frac{dz}{4\pi}e^{ixP^zz}\langle P|\bar\psi(z)\Gamma W[z,0]\psi(0)|P\rangle$, with spacelike $z=(0,0,0,z)$ and $\Gamma=\gamma^t$ or $\gamma^z$. The normalization and sign are to be fixed by the writer so that $\tilde q\to q$ at tree level (`Ji2013`, `Ji:2014gla`).
  - Pseudo-ITD $\mathcal M(\nu,z^2)$ (`Radyushkin2017`, `Radyushkin:2018cvn`, `Orginos:2017kos`).
  - Lattice cross sections (`MaQiu2018`, `Ma:2014jla`).
* **命题 `prop:lattice-renormalizability` — Wilson 线夸克双线性算符的乘法可重整性** [A]. The operator has a linear divergence $\propto|z|/a$ from the Wilson-line self-energy and is multiplicatively renormalizable to all orders (`Ishikawa:2017faj`, `Ji:2017oey`, `Green:2017xeu`).
* **定理 `thm:lattice-lamet` — LaMET/短距离因子化** [A].
  $$\tilde q(x,P^z;\mu)=\int\frac{dy}{|y|}C\Big(\frac xy,\frac\mu{|y|P^z}\Big)q(y;\mu)+(\text{power corrections}).$$
  - 非微扰地位：MA0、MA4 (MA: audit).
  - Sources: `IzubuchiEtAl2018` (through the OPE of the spacelike bilocal operator), `Ma:2014jla`, `MaQiu2018`.
  - The one-loop kernel is in `XiongEtAl2014` (**formula to verify**; not computed by an agent).
  - Power corrections: their $x$-dependence is not part of the [A] statement. The renormalon analysis gives $\Lambda^2/(x^2(1-x)P_z^2)$ (`Braun:2018brg`; survey item 24); the older estimate $O(\Lambda^2/(x^2P_z^2),\Lambda^2/((1-x)^2P_z^2))$ of the LaMET reviews (`JiEtAl2021`) differs at large $x$. Quote both with their sources (audit: the first version printed the two forms inconsistently).
  - Status [A]: it relies on the spacelike OPE in QCD (`thm:dis-ope`, [A]).
  - Reviews: `JiEtAl2021`, `Constantinou:2020hdm`.
* **命题 `prop:lattice-cs-kernel` — 格点 Collins–Soper 核** [A]. 非微扰地位：MA0、MA4 (MA: audit). Ratios of quasi-TMDs at different $P^z$ determine $\tilde K(b_T;\mu)$ non-perturbatively (`EbertStewartZhao2019`). Lattice–continuum TMD factorization: `Ebert:2022fmh`.
* **注 `rem:lattice-critiques` — 批评与回应**.
  - Rossi–Testa (`Rossi:2017muf`, `Rossi:2018zkn`) question the interchange of the continuum limit and the light-cone limit. The responses are in `IzubuchiEtAl2018` and `JiEtAl2021`.
  - C12: lattice results supply matrix elements; they are not tests of cross-section factorization.

**Worked example.** `ex:lattice-quasi-tree` — the quasi-PDF of a free quark at tree level, and the one-loop support property. The quasi-PDF has support for all real $x$, which shows why matching is a convolution over $y\in\mathbb R$. Structure only; cite `XiongEtAl2014`.

**Figures.** existing (tikz3, being redone): `fig:quasi-pdf`; new: `fig:lattice-matching`.

**Key citation keys.** `DetmoldLin2006`, `ChambersEtAl2017`, `Ji2013`, `Ji:2014gla`, `Radyushkin2017`, `Radyushkin:2018cvn`, `Orginos:2017kos`, `MaQiu2018`, `Ma:2014jla`, `Ishikawa:2017faj`, `Ji:2017oey`, `Green:2017xeu`, `IzubuchiEtAl2018`, `XiongEtAl2014`, `Braun:2018brg`, `JiEtAl2021`, `Constantinou:2020hdm`, `EbertStewartZhao2019`, `Ebert:2022fmh`, `Rossi:2017muf`, `Rossi:2018zkn`.

---------------------------------------------------------------------------------------------------

## Chapter 22 — 总结：主表与开放问题 / Summary: master table and open problems

`\label{ch:summary}` · `ch22_summary.tex` · **12 pp** · no new statements

**Purpose.** Close the book with three things:
1. **The master table** `tab:summary-master`. Its rows are **identical** in content and tags to `tab:intro-overview`; the row list is in §08 of this outline. It adds two columns: "瓶颈假设" (which hypothesis of `thm:method-template`, or which MA, is the bottleneck) and "升级路径" (what would upgrade the tag).
2. Lessons, in about 2 pp.
3. Open problems. Each is one paragraph naming the precise canonical statement it would settle.

**Sections.**
1. `sec:summary-master` 主表 (`tab:summary-master`, 4–5 pp, split into several `table` floats with 「（续）」 captions — `longtable` is not loaded, WRITER_SPEC §7.7; `fig:summary-status-map`). If the lead author adopts §0.9 items 1–2, add the frontier rows and a pointer to the generated App M.
2. `sec:summary-hypotheses` 假设与瓶颈 (`fig:summary-hypotheses`). For each [A] theorem, which of (H1)–(H5) and MA0–MA4 it uses.
3. `sec:summary-lessons` 经验与教训. Topics:
   - rigour is local, and the tag belongs to a statement, not to a process;
   - moment-space vs $x$-space;
   - inclusivity in the spectator final state;
   - soft factors and rapidity;
   - EFT and graphical proofs are complementary.
4. `sec:summary-open` 开放问题. Fourteen problems:
   1. A complete, published all-order proof of inclusive DY including Glauber subtractions. It would upgrade `thm:dy-factorization` and `thm:tmd-factorization`.
   2. The non-abelian multi-gluon Ward identity with ghosts and the BRST classification of non-local operators (`lem:method-ward-multi`; Collins 2011 §11.3.2).
   3. A Minkowskian subtraction theorem, i.e. an analogue of Weinberg's theorem (`thm:method-subtraction`); also Landau sufficiency and global deformations (`rem:ir-landau-status`; `Collins:2020euz` is a preprint).
   4. A proof of the OPE for QCD with quarks (`thm:dis-ope`).
   5. The non-perturbative status: MA0–MA4, and the construction of QCD (`rem:power-np-status`).
   6. Collinear factorization for $pp\to$ jets, hadrons and heavy quarks (`conj:dy-coloured-final`).
   7. Positivity of $\overline{\rm MS}$ PDFs (`conj:pdf-positivity`).
   8. NRQCD production (`conj:heavy-nrqcd-production`).
   9. NLP factorization and endpoint refactorization (`prop:power-nlp-endpoint`, `prop:heavy-qcdf-endpoint`).
   10. Small $x$: unify collinear, TMD and high-energy factorization; saturation (`prop:smallx-kt`, `conj:smallx-saturation`).
   11. Space-like collinear violation, SLLs, and mass-singularity factorization beyond NNLO (`prop:break-mass-singularity`, `prop:jets-sll`).
   12. DPS beyond double DY; MPI-sensitive observables (`conj:break-dps-coloured`, `prop:break-jet-veto`).
   13. Power corrections and renormalon-free schemes in LaMET (`thm:lattice-lamet`).
   14. The IR-renormalon/higher-twist correspondence and the universality of hadronization (`conj:power-renormalon-ht`, `conj:jets-hadronization`).

**Figures.** New: `fig:summary-status-map` (a grid of process classes × levels {PT-rigorous, all-order argued, partial, conjecture, violated}); `fig:summary-hypotheses` (the dependency of the main [A] theorems on (H1)–(H5) and MA0–MA4).

**Rules.** No new results. Every row cites its canonical label. The tags must match the chapter statements exactly; a script check is listed in WRITER_SPEC §9.

---------------------------------------------------------------------------------------------------

# 附录 (Appendices A–L, 35 pp)

---------------------------------------------------------------------------------------------------

General rules for the appendices:
- Each appendix is a `\chapter` after `\appendix` in the master file, with `\label{app:<key>}`.
- Statements use the same environments and tags as the main text.
- Pure mathematics carries no tag.
- The appendices hold the complete proofs that the chapters announce as "完整论证见附录 X". A proof promised in a chapter must actually appear here; the list is in WRITER_SPEC §6.

## Appendix A — 光锥坐标、Dirac 代数、加号分布与 Mellin 变换 / Light-front coordinates, Dirac algebra, plus distributions, Mellin transforms

`\label{app:appA}` · `appA_lightfront.tex` · **3 pp**

**Sections and statements.**
1. `sec:appA-lightfront` — light-front components, $d^4k=dk^+dk^-d^2k_T$, the boost proof of `lem:prelim-boost`, and $n_A,n_B$ versus the SCET $n,\bar n$ dictionary ($\bar n\cdot p=\sqrt2p^+$).
2. `sec:appA-dirac` — the $\gamma^\pm$ algebra and projectors $P_+=\frac12\gamma^-\gamma^+$, $P_-=\frac12\gamma^+\gamma^-$.
   * **引理 `lem:appA-fierz` — 共线 Fierz 分解** (数学，无标签). For any $4\times4$ matrix $M$:
     $$P_+MP_-=\tfrac14\big[{\rm Tr}(\gamma^+M)\gamma^-+{\rm Tr}(\gamma^+\gamma_5M)\gamma_5\gamma^-+\textstyle\sum_{j=1,2}{\rm Tr}(\gamma^+\gamma^jM)\gamma^-\gamma^j\big].$$
     Source: c_exclusive §1; VF-EXC-13. It is the leading-twist projector for PDFs, DAs and GPDs.
3. `sec:appA-plus` — distributions.
   - $[\cdot]_+$ at $z=1$; $\mathcal D_k(z)=[\ln^k(1-z)/(1-z)]_+$.
   - **Product convention:** $g(z)\mathcal D_k$ means $\int(gh-g(1)h(1))\frac{\ln^k(1-z)}{1-z}$. Example: in DY, the whole-term plus of $(1+z^2)\mathcal D_1$ would shift the $\delta$ coefficient by $7C_F$ (c_dy).
   - Expansion: $(1-z)^{-1-\varepsilon}=-\frac{\delta(1-z)}\varepsilon+\sum_k\frac{(-\varepsilon)^k}{k!}\mathcal D_k$ (proof of `lem:prelim-plus-expansion`).
   - Star distributions (SCET) and plus distributions at $\tau=0$ (event shapes).
   * **引理 `lem:appA-plus-product` — 乘积约定下的恒等式** (数学，无标签). $g(z)\mathcal D_k=g(1)\mathcal D_k+\frac{g(z)-g(1)}{1-z}\ln^k(1-z)$; the second term is a regular function.
4. `sec:appA-mellin` — Mellin transforms.
   * **引理 `lem:appA-mellin-table` — Mellin 变换表** (数学，无标签).
     - $\langle\mathcal D_0,z^{N-1}\rangle=-S_1(N-1)$ and $\langle\mathcal D_1,z^{N-1}\rangle=\frac12[S_1^2+S_2](N-1)$.
     - Large $N$: $-\ln\bar N$ and $\frac12(\ln^2\bar N+\zeta_2)$, with $\ln\bar N=\ln N+\gamma_E$ (VF-THR-2).
     - Moments of $P_{ij}$ (VF-PDF-8) and of $C_2^q$, $C_2^g$ (VF-DIS-8).
     - Continuation $S_1(N)\mapsto\psi(N+1)+\gamma_E$ (`prop:appK-continuation`).

**Sources.** c_exclusive §1; c_dy §§3, 6; c_scet §1; c_dis; critic c6.

---------------------------------------------------------------------------------------------------

## Appendix B — Wilson 线：Feynman 规则、程函恒等式与尖点 / Wilson lines: Feynman rules, eikonal identities, cusp

`\label{app:appB}` · `appB_wilson.tex` · **4 pp**

**Sections and statements.**
1. `sec:appB-definition` — the binding definition $W[b,a]=P\exp(ig\int_a^bdz\cdot A)$, with later points to the left and $W\to U(b)WU^\dagger(a)$. Properties: composition, retracing, unitarity, adjoint lines.
   **Convention warning:** Collins 2011 uses $g\to-g$ relative to us (D4).
2. `sec:appB-rules`
   * **命题 `prop:appB-rules` — Wilson 线的 Feynman 规则** [R, R_def].
     - With $A(x)=\int\!đ^4k\,e^{-ik\cdot x}\tilde A(k)$: $W[\infty n,0]\ni g t^an^\mu\tilde A_\mu(k)/(n\cdot k-i0)$ and $W[-\infty n,0]\ni gt^an^\mu\tilde A_\mu(k)/(n\cdot k+i0)$.
     - Future minus past: $2\pi i\,gt^an^\mu\delta(n\cdot k)$.
     - Multi-gluon rule: nested denominators $\prod_j[n\cdot(k_1+\dots+k_j)\mp i0]^{-1}$ with the colour ordering.

     Source: VF-WL-1/2/3; c_wilson universal rule; c_glauber §0.2. *Proof:* full.
3. `sec:appB-eikonal`
   * **引理 `lem:appB-shuffle` — 程函恒等式（洗牌积）** (数学，无标签). $\sum_{\sigma\in S_m}\prod_{j=1}^m\frac1{n\cdot(k_{\sigma1}+\dots+k_{\sigma j})+i0}=\prod_{j=1}^m\frac1{n\cdot k_j+i0}$. This proves `lem:prelim-eikonal-identity` (VF-WL-4).
   * Ward identity of a semi-infinite Wilson line (VF-WL-13), used in App F.
   * **命题 `prop:appB-webs` — 非阿贝尔指数化** [A]. Wilson-loop correlators exponentiate in terms of webs with modified colour factors (`Gatheral1983`, `FrenkelTaylor1984`). It is [R, R_def] at $O(g^2)$ (`prop:sudakov-webs`).
4. `sec:appB-cusp`
   * **命题 `prop:appB-cusp-oneloop` — 单圈尖点反常维度** [R, R_PT]. For two time-like lines with Minkowskian cusp angle $\beta$ ($\cosh\beta=v_1\cdot v_2$): $\Gamma_{\rm cusp}(\beta)=\frac{\alpha_sC_F}\pi(\beta\coth\beta-1)+O(\alpha_s^2)$. Its light-like limit is linear in $\beta$ and gives the cusp $\Gamma_{\rm cusp}=\frac{\alpha_sC_F}\pi\times$(rapidity).
     - Verified (VF-CONV-23): c_tmd R4 (the UV pole of the one-loop soft factor is two cusps with this anomalous dimension) and the audit's structural check; literature `Polyakov1980`, `BrandtNeriSato1981`, `KorchemskyRadyushkin1987`.
     - The $-1$ is the Wilson-line self-energy ($\Gamma(0)=0$ for a straight line).
     - Two loops: $\Gamma_1=4C_F[(\frac{67}9-\frac{\pi^2}3)C_A-\frac{20}9T_Fn_f]$ in BS normalization. The Becher–Schwartz arXiv source has a typo (c_scet §6 item 10; VF-SCET-16).

**Sources.** c_wilson §§2–4; c_glauber §0.2; c_scet §6; critic D-items.

---------------------------------------------------------------------------------------------------

## Appendix C — 维数正规化积分与相空间 / Dimensional-regularization integrals and phase space

`\label{app:appC}` · `appC_dimreg.tex` · **3 pp**

**Sections and statements.**
1. `sec:appC-msbar` — $\overline{\rm MS}$ with the binding $S_\varepsilon=(4\pi)^\varepsilon e^{-\varepsilon\gamma_E}$, and the comparison with Collins' $(4\pi)^\varepsilon/\Gamma(1-\varepsilon)$.
   * **注 `rem:appC-Seps` — $S_\varepsilon$ 约定的影响**. $e^{-\varepsilon\gamma_E}\Gamma(1-\varepsilon)=1+\frac{\pi^2}{12}\varepsilon^2+O(\varepsilon^3)$. This changes finite constants wherever $1/\varepsilon^2$ poles are subtracted (TMD $\tilde C$ and $\mathcal H$; `rem:tmd-scheme-constants`), but never physical cross sections. Derived by the spec synthesizer; consistent with c_tmd.
2. `sec:appC-integrals`
   * **引理 `lem:appC-bubble` — 单圈两点函数** (数学，无标签).
     - $\int\frac{d^Dk}{i\pi^{D/2}}\frac1{(-k^2)^a(-(k-q)^2)^b}=(-q^2)^{D/2-a-b}G(a,b)$, with $G(a,b)=\frac{\Gamma(a+b-D/2)\Gamma(D/2-a)\Gamma(D/2-b)}{\Gamma(a)\Gamma(b)\Gamma(D-a-b)}$.
     - $c_\Gamma=\frac{\Gamma(1+\varepsilon)\Gamma^2(1-\varepsilon)}{\Gamma(1-2\varepsilon)}$.
     - Standard; used by c_ee for $r_1G(1,1)^2+r_2G(1,1)G(1+\varepsilon,1)$.
   * **引理 `lem:appC-ibp` — 分部积分（三角规则）** (数学，无标签). The triangle rule. Two-loop propagator integral $\hat I(1,1,1,1,1)=6\zeta_3$ (VF-EE-7 context).
3. `sec:appC-phase-space`
   * **引理 `lem:appC-phase-space` — $D$ 维相空间** (数学，无标签).
     - Two-body: $\int d\Phi_2=\frac1{8\pi}\big(\frac{4\pi}s\big)^\varepsilon\frac{\Gamma(1-\varepsilon)}{\Gamma(2-2\varepsilon)}$ (audit: equals VF-DY-4 integrated over $v$ in the massless limit).
     - Three-body for $e^+e^-$ (Dirichlet form).
     - DIS/DY $2\to2$ phase spaces exact in $\varepsilon$ (c_dis, c_dy).
4. `sec:appC-formfactor` — the massless quark form factor exact in $\varepsilon$, $F^{(1)}_{\rm bare}=\frac{\alpha_sC_F}{4\pi}(\frac{4\pi\mu_0^2}{Q^2})^\varepsilon c_\Gamma[-\frac{2-\varepsilon+2\varepsilon^2}{\varepsilon^2(1-2\varepsilon)}]$ (VF-SUD-1; c_dis = c_scet row 7), and its timelike continuation.

**Sources.** c_ee §§3–4; c_dis; c_dy; c_scet row 7.

---------------------------------------------------------------------------------------------------

## Appendix D — Landau 方程与 Coleman–Norton 定理 / Landau equations and the Coleman–Norton theorem

`\label{app:appD}` · `appD_landau.tex` · **4 pp**

**Sections and statements.**
1. `sec:appD-gordan`
   * **引理 `lem:appD-gordan` — Gordan 择一定理** (数学，无标签). For $u_1,\dots,u_m\in\mathbb R^d$ exactly one of the following holds:
     - (i) there is $\alpha\in\mathbb R^m_{\ge0}\setminus\{0\}$ with $\sum_j\alpha_ju_j=0$;
     - (ii) there is $v\in\mathbb R^d$ with $v\cdot u_j>0$ for all $j$.

     Reference: `Gordan1873`. *Proof:* full (separating hyperplane).
2. `sec:appD-momentum` — proof of `thm:ir-landau-momentum`. The local deformation $k\to k+i\epsilon v$ shows that a non-pinched point admits a deformation (c_regions L3; blueprint S1).
3. `sec:appD-alpha` — the $\alpha$-representation. `lem:ir-envelope` and the proof of `thm:ir-landau-alpha` (c_regions L1–L2).
4. `sec:appD-cn` — derivation of `prop:ir-coleman-norton`: $\alpha_jk_j=\Delta x_j$, interpreted as a classical process.
5. `sec:appD-caveats` — what is *not* proved.
   - Sufficiency and the global existence of the deformation (`rem:ir-landau-status`). Collins 2011 §5.4.3: "no published complete proof".
   - Preprints claiming complete proofs: `Collins:2020euz`, `Muhlbauer:2020kut`.
   - Literature: `Landau1959`, `Nakanishi:1959jzx`, `ColemanNorton1965`, `EdenEtAl1966`, `Pham:2011SingInt`, `Fevola:2023kaw`, `Sterman1993`.

**Sources.** c_regions §1 (VF-REG-1…6); blueprint S1.

---------------------------------------------------------------------------------------------------

## Appendix E — 幂次计数公式的推导 / Derivation of the power-counting formula

`\label{app:appE}` · `appE_powercount.tex` · **3 pp**

**Sections and statements.**
1. `sec:appE-units` — Sterman units: $\lambda$ for collinear lines, $\lambda_S=\lambda^2$ for soft lines. The scaling of measures, propagators and numerators, including the boost factors of good and bad components.
2. `sec:appE-formula`
   * **命题 `prop:appE-degree` — 约化图的超表观红外发散度** [R, R_PT]. The derivation of the formula in `prop:ir-power-counting` (VF-REG-8) by dimension counting plus boost counting (blueprint S2; c_regions P2).
   * **注 `rem:appE-actual-bound` — 从超表观度到实际界** [A]. Bounding actual contributions needs nested-region control (c_regions §2.4). This is why `thm:ir-leading-regions` is [A].
3. `sec:appE-examples` — reduced diagrams for $e^+e^-$, DIS and DY, with explicit degrees (c_regions `fig:pc-ee`, `fig:pc-dis`, `fig:pc-dy`). The Glauber region is $\lambda^0$ (c_glauber §1.1 [P5]; VF-GLA-1).

**Sources.** c_regions §2 (VF-REG-7…12); c_glauber §1.1.

---------------------------------------------------------------------------------------------------

## Appendix F — 图形 Ward 恒等式 / Graphical Ward identities

`\label{app:appF}` · `appF_ward.tex` · **3 pp**

**Sections and statements.**
1. `sec:appF-one` — proof of `prop:method-ward-one` from `thm:prelim-slavnov-taylor` (external physical partons on shell).
2. `sec:appF-two`
   * **命题 `prop:appF-two-gluon` — 两个纵向胶子：树图层次的完整证明** [R, R_PT]. In DIS kinematics, two collinear K-gluons give exactly $(n_B\cdot k_1)(n_B\cdot k_2)W^{(2)}_{ab}[\infty n_B,0]H_0$. The path ordering comes from the commutator term, and no ghost or three-gluon graph contributes at this order. For $q\bar q\to g^*g^*$ with unphysical polarizations, the ghost term is explicit (VF-WL-8/9; c_wilson §5.4–5.5).
3. `sec:appF-induction`
   * **命题 `prop:appF-induction` — 多胶子情形的归纳论证** [A]. This is the outline of the inductive step of `lem:method-ward-multi`. The conditions are: on-shell physical external partons, approximated (not exact) collinear momenta, and ghost terms cancelling or being absorbed. Collins 2011 §11.9 and §11.3.2 assume the BRST classification of non-local operators. `Collins:2008sg`: remainder of the naive identity.
4. `sec:appF-gy` — details of Grammer–Yennie: collinear and soft forms, errata to Collins 2011 eqs. (11.4)–(11.6) (as flagged by c_wilson), and the numerical suppression table (VF-WL-10/11).

**Sources.** c_wilson §§5–7; `GrammerYennie1973`; `SenIndumathiChoudhury2019` (only next to `GrammerYennie1973`).

---------------------------------------------------------------------------------------------------

## Appendix G — 单圈与两圈计算细节 / Details of one- and two-loop calculations

`\label{app:appG}` · `appG_oneloop.tex` · **4 pp** · calculations only (no new canonical statements)

1. `sec:appG-ee` — $e^+e^-$: real and virtual in one normalization; the warning about the separate constants; the two-loop $\Pi$ via IBP (c_ee §§3–4; VF-EE-4…8).
2. `sec:appG-dis` — DIS real emission exact in $\varepsilon$ ($R_2^q$, $R_L^q$, $R_2^g$, $R_L^g$) and the Laurent table (c_dis; VF-DIS-3…6).
3. `sec:appG-dy` — DY real emission exact in $\varepsilon$, the origin of $\frac{2\pi^2}3$, and mass factorization (c_dy; VF-DY-3…9).
4. `sec:appG-pdf` — the one-loop quark PDF with a gluon mass, graph by graph, and the local-operator anomalous dimensions (c_pdf §§3, 6; VF-PDF-3, VF-PDF-14).
5. `sec:appG-tmd` — the one-loop soft factor and unsubtracted TMD with Collins' regulator (c_tmd DERIVATION §3, R1–R9; verified; draft `research/c_tmd/tex/tmd_oneloop.tex`).

---------------------------------------------------------------------------------------------------

## Appendix H — 文献导读 / Annotated bibliography

`\label{app:appH}` · `appH_literature.tex` · **2 pp**

Organized by topic, one or two sentences per item, using the warnings of `REFS_NOTES.md`:
- **Textbooks:** `Collins2011` (for section numbers use the 2011 edition; `Collins2023` is the Open Access reissue), `Sterman1993`, `EllisStirlingWebber1996`, `Field1989`, `Muta2010`, `Collins1984`, `PeskinSchroeder1995`, `Weinberg1996`, `BecherBroggioFerroglia2015`, `KovchegovLevin2012`.
- **Reviews:** `CollinsSoperSterman1989`, `CollinsSoper1987`, `Sterman:1995fz`, `StermanEtAl1995`, `Beneke1999`, `Diehl2003`, `BelitskyRadyushkin2005`, `BoussarieEtAl2023`, `AngelesMartinezEtAl2015`, `BrambillaEtAl2011`, `JiEtAl2021`, `Constantinou:2020hdm`, `Diehl:2017wew`, `GelisEtAl2010`.
- **Historical:** `Feynman1969`, `BjorkenPaschos1969`, `Bjorken1969`, `DrellYan1970`.

---------------------------------------------------------------------------------------------------

## Appendix I — 维数正规化中的 $\gamma_5$ / $\gamma_5$ in dimensional regularization

`\label{app:appI}` · `appI_gamma5.tex` · **2 pp**

**Sections and statements.**
* **定义 `def:appI-hvbm` — HVBM 方案** (no tag).
  - $\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3$, with $\epsilon^{0123}=+1$ and ${\rm Tr}(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma\gamma_5)=-4i\epsilon^{\mu\nu\rho\sigma}$ (VF-CONV-10; checked on all 256 index sets by c_exclusive).
  - Split $\gamma^\mu=\bar\gamma^\mu+\hat\gamma^\mu$: $\gamma_5$ anticommutes with $\bar\gamma^\mu$ and commutes with $\hat\gamma^\mu$ (`tHooftVeltman1972`, `BreitenlohnerMaison1977a`).
* **命题 `prop:appI-larin` — Larin 方案与非单态轴矢流的有限重整化** [R, R_PT].
  - The axial current is written with $\gamma^\mu\gamma_5\to-\frac i6\epsilon^{\mu\nu\rho\sigma}\gamma_\nu\gamma_\rho\gamma_\sigma$ in the binding convention $\epsilon^{0123}=+1$ (VF-CONV-24). **Audit correction:** the first version printed $+\frac i6$; the literature form $\gamma_\mu\gamma_5=\frac i6\epsilon_{\mu\nu\rho\sigma}\gamma^\nu\gamma^\rho\gamma^\sigma$ assumes $\epsilon_{0123}=+1$.
  - A finite renormalization $Z_5^{\rm ns}=1-4C_F\frac{\alpha_s}{4\pi}+O(\alpha_s^2)$ restores the anticommuting Ward identity (`Larin:1993tq`, `LarinVermaseren1991`; **coefficient to verify**).
  - Non-singlet results (Bjorken) are then scheme independent.
  - Singlet: the axial anomaly makes the split $\Delta\Sigma/\Delta G$ scheme dependent (`prop:coll-anomaly-scheme`).
* **注 `rem:appI-anomaly` — 轴矢反常**. The ABJ anomaly for the singlet current, in the binding normalization **(writer derives; normalization to verify)**. Consequence: the first moment of the $\gamma^*g$ box differs between HVBM and anticommuting-$\gamma_5$ treatments (`AltarelliRoss1988`, `CarlitzCollinsMueller1988`).

**Sources.** c_exclusive §1; critic c4 (Bjorken, Crewther); `MertigVanNeerven1996`, `Vogelsang1996` for the polarized NLO kernels.

---------------------------------------------------------------------------------------------------

## Appendix J — BRST 对称性与割图中的鬼场 / BRST symmetry and ghosts in cut diagrams

`\label{app:appJ}` · `appJ_brst.tex` · **2 pp**

**Sections and statements.**
1. `sec:appJ-brst` — BRST transformations in the binding conventions, nilpotency (`lem:prelim-brst-nilpotent`), and the Kugo–Ojima quartet mechanism (`KugoOjima1979`, `BecchiRouetStora1975`, `BecchiRouetStora1976`, `Tyutin1975`).
2. `sec:appJ-cuts`
   * **命题 `prop:appJ-ghost-cuts` — 割图中的鬼场贡献** [R, R_PT]. Summing cut gluon lines with $-g_{\mu\nu}$ and subtracting the ghost cuts equals the physical-polarization sum. Tree-level check: $q\bar q\to gg$ (VF-WL-9). This completes `thm:prelim-cutting-rules` for gauge theories.
3. `sec:appJ-operators`
   * **命题 `prop:appJ-local-operators` — 规范不变定域算符的重整化与混合** [R, R_PT]. Gauge-invariant local operators mix only with gauge-invariant operators, BRST-exact operators and equation-of-motion (EOM) operators. The latter two have vanishing physical matrix elements (`Joglekar:1975nu`, `Joglekar:1976eb`, `Joglekar:1976pe`, `Kluberg-Stern:1974iel`, `Kluberg-Stern:1974nmx`, `Kluberg-Stern:1975ebk`, `Henneaux:1993jn`, `Collins:1994ee`).
   * **注 `rem:appJ-nonlocal` — 非定域算符** [A]. The analogous classification for the non-local operators of factorization proofs is assumed (Collins 2011 §11.3.2, pp. 407–410).

---------------------------------------------------------------------------------------------------

## Appendix K — 矩问题与解析延拓引理 / Moment problems and continuation lemmas

`\label{app:appK}` · `appK_moments.tex` · **3 pp**. All pure mathematics, no tags; complete proofs (c_pdf §7, s6 15/15 PASS).

* **引理 `lem:appK-hausdorff` — Hausdorff 唯一性** (数学). A finite signed Borel measure on $[0,1]$ with all moments zero vanishes. If $h\in L^1$ has all moments zero, then $h=0$ a.e. Proof: Weierstrass plus the uniqueness part of Riesz representation (`Hausdorff1921a`, `Hausdorff1921b`, `Hausdorff1923`).
* **定理 `thm:appK-even-moments` — 偶数矩决定函数** (数学). If $x^{2k_0}g\in L^1(0,1)$ and $\int_0^1x^{2k}g=0$ for all $k\ge k_0$, then $g=0$ a.e. Proof: substitute $t=x^2$, then apply `lem:appK-hausdorff`. Müntz–Szász is not needed.
* **推论 `cor:appK-pdf` — PDF 的唯一性** (数学). Even moments $N\ge N_1$ determine $q+\bar q$ and $g$; odd moments determine $q-\bar q$. Even moments alone do not determine $q$ and $\bar q$ separately (explicit pair, c_pdf s6(h)).
* **命题 `prop:appK-kernels` — 领头阶核由偶数矩唯一确定** (数学). For $P=r(x)+a[\frac1{1-x}]_++b\delta(1-x)$ with $|r|\le C/x$: if all even moments vanish, then $a=b=0$ and $r=0$ a.e.
* **定理 `thm:appK-carlson` — Carlson 定理** (数学，经典，引用). Statement as in c_pdf Thm 7.6, with sharpness from $\sin\pi z$. For even integers the bound is $<\pi/2$ (`Carlson1914`, `Titchmarsh1939` §5.81, `Boas1954` Thm 9.2.1).
* **命题 `prop:appK-continuation` — 多项式有界条件下延拓的唯一性** (数学). If $F$ is holomorphic for ${\rm Re}\,z>\sigma_0$ with $|F|\le C(1+|z|)^m$, and vanishes on an arithmetic progression, then $F\equiv0$. Full proof via the Cayley map and Jensen's formula (`Rudin1987`). Corollary: Mellin transforms of PDFs and kernels continue uniquely from even $N$. Adding $c\sin(\pi N/2)$ is excluded by the growth bound. The even and odd continuations differ beyond LO.
* **定理 `thm:appK-muntz` — Müntz–Szász** (数学，经典，引用; `Muntz1914`, `Szasz1916`). It is included with the $L^2$ distance formula, for reference.
* **注 `rem:appK-counterexamples` — 反例与稳定性**.
  - $\delta'(x)$: all even moments vanish, but it is not a function.
  - $\sin(Q^2x)$: $Q^2$ times every moment stays bounded, yet $\sup|R|=1$ (VF-MISC-3).
  - Uniqueness is not stability: the Hilbert-matrix condition number grows like $e^{3.5K}$ (c_pdf s6(c); VF-MISC-2).

---------------------------------------------------------------------------------------------------

## Appendix L — 光线算符与定域算符：矩关系的全阶证明 / Light-ray and local operators: all-order proof of the moment relation

`\label{app:appL}` · `appL_lightray.tex` · **2 pp**. This is the complete proof of `thm:pdf-moments-local`.

* **引理 `lem:appL-divided-differences` — 均差恒等式** (数学). The $n$-th moment of the $m$-gluon vertex of the light-ray operator equals the $m$-gluon vertex of $\bar\psi\gamma^+(iD^+)^{n-1}\psi$. One gluon: $\frac{gt^an^\mu\gamma^+}{2(P^+)^n}\sum_{j=0}^{n-2}(k_2^+)^j(k_1^+)^{n-2-j}$ (VF-PDF-12). c_pdf verified $m=1,2$ for $n\le7$; general $m$ follows by induction on divided differences.
* **命题 `prop:appL-bare` — 裸算符恒等式** [R, R_def].
  - Moments are derivatives at $w^-=0$, using $\partial_{w^-}[\bar\psi W]=[\bar\psi\overleftarrow D^+]W$.
  - Total derivatives vanish in forward matrix elements.
  - The gluon case uses the even distribution $\xi f_g$.

  Source: blueprint S6, with signs fixed.
* **命题 `prop:appL-renormalized` — 重整化后的矩关系** [R, R_PT].
  - $Z_f(N)=Z_O(N)$, by the uniqueness of minimal subtraction and `thm:prelim-composite-renorm`.
  - Construct $Z_{ij}(x)$ from partonic targets.
  - Finiteness holds for any state, because the pole parts are compactly supported distributions with all moments zero (their Fourier–Laplace transform is entire).
  - One-loop check exact in $\varepsilon$ (VF-PDF-13).
  - Remark: left- and right-acting derivatives agree only in forward matrix elements, which is why GPDs differ (Ch18).

---------------------------------------------------------------------------------------------------

# 08 Registry: master-table rows, canonical labels, counts

---------------------------------------------------------------------------------------------------

This section is generated from the chapter entries above (`check_outline.py`, `master_rows.py` in the spec synthesizer's scratch area). When it was generated:
- every label referenced anywhere in this outline was defined in it;
- every citation key used here was present in `refs_merged.bib`;
- every master-table row matched the tag of its canonical statement.

Writers use the registry to check:
- their own canonical labels (§9 of WRITER_SPEC);
- that every external label they reference exists.

### Master-table rows (`tab:intro-overview` = `tab:summary-master`)

Ch1 typesets columns 1–5; Ch22 adds "瓶颈假设" and "升级路径". The tag shown must equal the tag of the canonical statement; `master_rows.py` checks this against the registry.

| # | 结论 | 公式/要点 | 标签 | MA | 规范标签 | 瓶颈假设（Ch22） | 升级路径（Ch22） |
|---|---|---|---|---|---|---|---|
| 1 | 欧氏 Green 函数的红外有限性 | 非例外欧氏动量 | [R, R_PT] | — | `thm:ee-euclid-ir` | BM 假设对含鬼场的非阿贝尔理论的逐条核对 | — |
| 2 | $R(s)$ 每阶红外有限 | $R=R_0(1+\frac34C_Fa+r_2a^2+\dots)$ | [R, R_PT] | MA0（强子） | `thm:ee-R-finite` | —（微扰论中已严格） | 构造 QCD |
| 3 | $R$ 与部分子割图之和等同 | 无质量 DR 割图规则 | [A] | — | `cor:ee-cuts` | 无质量 DR 中含鬼场的割图规则 | 完整的 DR 割图证明 |
| 4 | $R(s)$ 的 $O(\alpha_s^2)$ 系数（SU(3)） | $r_2=1.9857-0.1153n_f$ | [R, R_PT] | — | `cor:ee-R-alphas` | — | — |
| 5 | KLN 定理 | 简并态求和 | [A] | — | `thm:ir-kln` | 初态求和需前向散射项 | — |
| 6 | 红外安全截面的有限性 |  | [A] | — | `thm:ir-safe-finite` | 全阶区域分析 | — |
| 7 | 有色初态的 Bloch–Nordsieck 相消 | 幂次压低的未相消项 | [V] | — | `prop:ir-bn-failure` | — | — |
| 8 | Landau 方程（必要性） | Gordan 择一 | [R, R_PT] | — | `thm:ir-landau-momentum` | 充分性与整体形变 | Collins 2020 预印本的发表与核查 |
| 9 | 超表观红外幂次计数 | $\omega(R)$ 公式 | [R, R_PT] | — | `prop:ir-power-counting` | — | — |
| 10 | 领头区域的完备性 |  | [A] | MA1 | `thm:ir-leading-regions` | 实际界与嵌套区域 | 全阶界 |
| 11 | 区域方法（欧氏） | 大动量/大质量展开 | [R, R_PT] | — | `thm:ir-regions-euclid` | — | — |
| 12 | 区域方法（闵氏） | 阈值、在壳、Glauber | [P] | — | `prop:ir-regions-minkowski` | 一般证明缺失 | 闵氏版本的证明 |
| 13 | Sudakov 形状因子的因子化 | $H\,J\,J\,S$；$K+G$ | [A] | — | `thm:sudakov-factorization` | 一般减除定理（仅此例完整） | — |
| 14 | 多腿振幅的红外极点（偶极子公式至两圈） |  | [A] | — | `thm:sudakov-ir-poles` |  | — |
| 15 | 偶极子公式作为全阶精确陈述 | 三圈非偶极子项 | [V] | — | `prop:sudakov-dipole-violation` | — | — |
| 16 | QCD（含夸克）的欧氏 OPE |  | [A] | — | `thm:dis-ope` | 含夸克规范理论的全阶证明 | Zimmermann/Hollands 型证明推广到 QCD |
| 17 | DIS 结构函数矩的因子化 | $\int x^{n-2}F_2=\sum C^{(n)}A^{(n)}$ | [R, 以 OPE 为前提] | MA0、MA3、MA4 | `thm:dis-moments` | `thm:dis-ope`；非微扰 OPE | 非微扰 OPE |
| 18 | Bjorken 求和规则 | $\frac{g_A}6[1-a-(\frac{55}{12}-\frac{n_f}3)a^2]$ | [R, 以 OPE 为前提] | MA0、MA3、MA4 | `thm:dis-bjorken` | 同上 | 同上 |
| 19 | DGLAP 来自算符重整化 | $\partial f/\partial\ln\mu^2=P\otimes f$ | [R, R_PT] | MA0（强子） | `thm:pdf-dglap` | — | — |
| 20 | PDF 的矩 = 定域算符矩阵元 |  | [R, R_PT] | MA0 | `thm:pdf-moments-local` | — | — |
| 21 | PDF 支撑（微扰论） | $|\xi|\le1$ | [R, R_PT] | — | `thm:pdf-support-pt` | — | — |
| 22 | PDF 支撑（强子） | 谱论证 | [A] | MA0 | `prop:pdf-support-hadron` | 存在性假设 | 非微扰构造 |
| 23 | 数与动量求和规则 |  | [R, R_PT] | MA0 | `prop:pdf-sum-rules` | — | — |
| 24 | $\overline{\rm MS}$ PDF 的正定性 |  | [C] | — | `conj:pdf-positivity` | 无一般证明；文献有争议 | 证明或反例 |
| 25 | $x$ 空间 DIS（扭度 2 部分） | $F_2^{\rm tw2}/x=\sum C_i\otimes f_i$ | [R, 以 OPE 为前提] | MA0、MA3、MA4 | `thm:pdf-dis-xspace` | 逐点余项不受控 | `thm:disall-factorization` 升级 |
| 26 | 因子化模板定理 | (H1)–(H5) ⇒ 因子化形式 | [A] | MA1、MA2、MA4 | `thm:method-template` | `lem:method-ward-multi`, `thm:method-subtraction`, Glauber | 三处弱环的完整证明 |
| 27 | DIS 共线因子化（$x$ 空间逐点） |  | [A] | MA1、MA2、MA4 | `thm:disall-factorization` | BRST 分类（非定域算符）；减除 | 同上 |
| 28 | 含重夸克质量的 DIS | Collins 1998 | [A] | MA1、MA2 | `thm:disall-heavy` | 同上 | 同上 |
| 29 | $e^+e^-\to hX$（碎裂函数） |  | [A] | MA1、MA2 | `thm:coll-sia` | 同上 | 同上 |
| 30 | 共线 SIDIS |  | [A] | MA1、MA2 | `thm:coll-sidis` | 同上 | 同上 |
| 31 | $g_1$ 奇数矩 |  | [R, 以 OPE 为前提] | MA0、MA3、MA4 | `thm:coll-g1-moments` | 单态：轴反常与方案依赖 | — |
| 32 | 单举 Drell–Yan 共线因子化 |  | [A] | MA1、MA2、MA4 | `thm:dy-factorization` | Glauber 区（Collins §14.4.8） | 含 Glauber 减除的完整证明 |
| 33 | 色单态末态（$W,Z,H$） |  | [A] | MA1、MA2 | `thm:dy-colour-singlet` | 同上 | 同上 |
| 34 | $pp\to$ 喷注/强子/重夸克对 |  | [C] | — | `conj:dy-coloured-final` | 有色末态的 Glauber 相消 | 与 DY 同等细节的证明 |
| 35 | DY 超出 $1/Q^2$ | $m^4/s^2$ 处失效 | [V] | — | `prop:dy-twist6-failure` | — | — |
| 36 | 阈值重新因子化（领头幂次） | Mellin 指数化 | [A] | — | `thm:thr-refactorization` | 同 DY | — |
| 37 | 次领头幂次阈值对数 | LL | [P] | — | `prop:thr-nlp` | 端点发散 | 一般 NLP 因子化 |
| 38 | TMD 因子化（DY、SIDIS、$e^+e^-$） | $\zeta_A\zeta_B=Q^4$ | [A] | MA1、MA2、MA4 | `thm:tmd-factorization` | Glauber；快度方案等价性 | 全阶方案等价性 |
| 39 | Sivers 符号反转（算符） | $f_{1T}^\perp|_{\rm SIDIS}=-f_{1T}^\perp|_{\rm DY}$ | [R, R_def] | MA0 | `thm:tmd-sivers-sign` | — | — |
| 40 | Sivers 符号反转（可观测） |  | [A] | MA1、MA2 | `cor:tmd-sivers-observable` | 依赖 TMD 因子化 | 实验判定 |
| 41 | 超软退耦（BPS） | SCET 拉氏量恒等式 | [R, R_def] | — | `thm:scet-decoupling` | 作为 QCD 陈述需模式完备 | — |
| 42 | 推力分布 $H\,J\otimes J\otimes S$ |  | [A] | MA1、MA2 | `thm:scet-thrust` | 模式完备性 | — |
| 43 | 非全局对数（LL，大 $N_c$） | BMS | [A] | — | `thm:jets-bms` | 有限 $N_c$ | — |
| 44 | 超领头对数 | $\alpha_s^nL^{2n-3}$ | [P] | — | `prop:jets-sll` | Glauber 相位 | — |
| 45 | BFKL（LL/NLL） |  | [A] | — | `thm:smallx-bfkl` | 对数近似 | — |
| 46 | $k_T$ 因子化 |  | [P] | — | `prop:smallx-kt` | 幂次修正不受控；过程依赖 | — |
| 47 | 饱和/色玻璃凝聚 |  | [C] | — | `conj:smallx-saturation` | 与共线因子化的匹配 | — |
| 48 | $h_1h_2\to H_1H_2X$ 的 TMD 因子化 | 色纠缠 | [V] | — | `thm:break-tmd` | — | — |
| 49 | 类空严格共线因子化（振幅） | CdFR | [V] | — | `prop:break-spacelike` | — | — |
| 50 | 衍射 DIS | 衍射 PDF | [A] | MA1、MA2 | `thm:break-ddis` | 同 DIS | — |
| 51 | 强子—强子硬衍射 | 间隙存活 | [V] | — | `prop:break-hh-diffraction` | — | — |
| 52 | 双 Drell–Yan |  | [A] | MA1、MA2 | `thm:break-double-dy` | 演化、正定性 | — |
| 53 | 介子形状因子（领头幂次） | $Q^2F_\pi\to8\pi\alpha_sf_\pi^2$ | [A] | MA1、MA2 | `thm:excl-pion-ff` | 端点区域 | — |
| 54 | DVCS |  | [A] | MA1、MA2 | `thm:excl-dvcs` | 同上 | — |
| 55 | 纵向光子介子产生 |  | [A] | MA1、MA2 | `thm:excl-meson-L` | 同上 | — |
| 56 | 横向光子介子产生（标准共线形式） | 端点对数发散 | [V] | — | `prop:excl-meson-T` | — | — |
| 57 | $B\to D\pi$ |  | [A] | MA1、MA2 | `thm:heavy-bdpi` | 端点压低假设 | — |
| 58 | $B\to\pi\pi$（领头幂次） | BBNS | [P] | — | `prop:heavy-qcdf-lp` | 全阶证明缺失；粲企鹅争议 | 全阶证明 |
| 59 | $B\to\pi\pi$ 幂次修正 | $X_A,X_H$ | [V] | — | `prop:heavy-qcdf-endpoint` | 端点发散 | 端点再因子化 |
| 60 | 单举 $B$ 衰变（重夸克展开） |  | [A] | MA0、MA4 | `thm:heavy-inclusive-b` | 局域对偶 | — |
| 61 | NRQCD 衰变 |  | [A] | MA1、MA2 | `thm:heavy-nrqcd-decay` |  | — |
| 62 | NRQCD 产生 |  | [C] | — | `conj:heavy-nrqcd-production` | NNLO 以上的规范完备化 | 全阶证明或反例 |
| 63 | SIDIS 型扭度 3 单自旋不对称 |  | [P] | — | `prop:power-twist3-sidis` | 全阶论证缺失 | — |
| 64 | 大 $\beta_0$ 重整化子 | 无 $u=1$ 极点 | [P] | — | `prop:power-adler-large-beta0` | 近似 | — |
| 65 | 红外重整化子 ↔ 高扭度（一般） |  | [C] | — | `conj:power-renormalon-ht` | 无非微扰 OPE 定义 | — |
| 66 | 夸克—强子对偶 |  | [C] | — | `conj:ee-duality` | 非微扰 OPE | — |
| 67 | LaMET 匹配 |  | [A] | MA0、MA4 | `thm:lattice-lamet` | 类空 OPE | — |
| 68 | $\varphi^4_4$ 中 OPE 的逐阶收敛 |  | [R, R_PT] | — | `thm:power-ope-convergence` | — | — |

## 08 Label registry (generated by `check_outline.py`; canonical labels with tags)

Counts: "statements" = def/thm/lem/prop/cor/conj/rem; "examples" = ex. Tag column as given in the entry.

| unit | statements | of which thm/prop/lem/cor/conj | examples |
|---|---|---|---|
| front | 0 | 0 | 0 |
| Ch01 | 5 | 0 | 1 |
| Ch02 | 25 | 14 | 3 |
| Ch03 | 21 | 14 | 5 |
| Ch04 | 12 | 9 | 4 |
| Ch05 | 19 | 17 | 3 |
| Ch06 | 20 | 14 | 4 |
| Ch07 | 23 | 14 | 4 |
| Ch08 | 23 | 19 | 3 |
| Ch09 | 13 | 12 | 3 |
| Ch10 | 20 | 15 | 1 |
| Ch11 | 19 | 17 | 3 |
| Ch12 | 6 | 4 | 1 |
| Ch13 | 21 | 13 | 3 |
| Ch14 | 16 | 12 | 3 |
| Ch15 | 10 | 9 | 1 |
| Ch16 | 6 | 4 | 1 |
| Ch17 | 14 | 11 | 3 |
| Ch18 | 13 | 10 | 1 |
| Ch19 | 9 | 8 | 1 |
| Ch20 | 12 | 10 | 2 |
| Ch21 | 6 | 4 | 1 |
| Ch22 | 0 | 0 | 0 |
| AppA | 3 | 3 | 0 |
| AppB | 4 | 4 | 0 |
| AppC | 4 | 3 | 0 |
| AppD | 1 | 1 | 0 |
| AppE | 2 | 1 | 0 |
| AppF | 2 | 2 | 0 |
| AppG | 0 | 0 | 0 |
| AppH | 0 | 0 | 0 |
| AppI | 3 | 1 | 0 |
| AppJ | 3 | 2 | 0 |
| AppK | 8 | 7 | 0 |
| AppL | 3 | 3 | 0 |
| **total** | **346** | **257** | **51** |

### Ch01

| label | type | tag | title |
|---|---|---|---|
| `def:intro-hard-process` | def | (no tag) | 定义  — 硬过程与幂次展开 |
| `def:intro-factorization` | def | (no tag) | 定义  — 共线因子化陈述 |
| `def:intro-tags` | def | (no tag) | 定义  — 严格性标签 |
| `def:intro-MA` | def | (no tag) | 定义  — 元假设 MA0–MA4 |
| `rem:intro-incoherence` | rem | — | 注  — 部分子模型的非相干性论证（启发式） |

Examples: `ex:intro-handbag`

### Ch02

| label | type | tag | title |
|---|---|---|---|
| `def:prelim-qcd` | def | (no tag) | 定义  — QCD 拉氏量与规范变换 |
| `def:prelim-feynman-rules` | def | — | 定义  — Feynman 规则 |
| `def:prelim-brst` | def | (no tag) | 定义  — BRST 变换 |
| `lem:prelim-brst-nilpotent` | lem | [R, R_def] | 引理  — $s^2=0$ 与拉氏量的 BRST 不变性 |
| `thm:prelim-slavnov-taylor` | thm | [R, R_PT] | 定理  — Slavnov–Taylor 恒等式（因子化所用形式） |
| `prop:prelim-unitarity` | prop | [R, R_PT] | 命题  — 物理幺正性与鬼场割线 |
| `def:prelim-lightfront` | def | (no tag) | 定义  — 光锥坐标与 Sudakov 分解 |
| `lem:prelim-boost` | lem | [R, R_def] | 引理  — 推动下的标度 |
| `def:prelim-wilson` | def | (no tag) | 定义  — Wilson 线 |
| `prop:prelim-wilson-covariance` | prop | [R, R_def] | 命题  — Wilson 线的规范协变性 |
| `prop:prelim-wilson-rules` | prop | [R, R_def] | 命题  — 半无限直 Wilson 线的动量空间 Feynman 规则 |
| `lem:prelim-eikonal-identity` | lem | (数学，无标签) | 引理  — 程函恒等式 |
| `def:prelim-msbar` | def | (no tag) | 定义  — $\overline{\rm MS}$ 方案 |
| `prop:prelim-beta` | prop | [R, R_PT] | 命题  — $\beta$ 函数 |
| `prop:prelim-rg` | prop | [R, R_PT] | 命题  — 重整化群改进 |
| `def:prelim-gamma5` | def | (no tag) | 定义  — $\gamma_5$ 与 $\varepsilon$ 张量 |
| `thm:prelim-composite-renorm` | thm | [R, R_PT] | 定理  — 规范不变复合算符的重整化（Joglekar–Lee） |
| `def:prelim-plus` | def | (no tag) | 定义  — 加号分布 |
| `lem:prelim-plus-expansion` | lem | (数学，无标签) | 引理  — $(1-z)^{-1-a\varepsilon}$ 的分布展开 |
| `def:prelim-mellin` | def | (no tag) | 定义  — Mellin 变换与卷积 |
| `lem:prelim-mellin` | lem | (数学，无标签) | 引理  — Mellin 卷积定理与加号分布的矩 |
| `def:prelim-cut` | def | (no tag) | 定义  — 割图 |
| `thm:prelim-cutting-rules` | thm | [R, R_PT] | 定理  — 切割规则 |
| `rem:prelim-cutting-dr` | rem | [A] | 注 |
| `prop:prelim-optical` | prop | [R, R_def] | 命题  — 流关联函数的光学定理 |

Examples: `ex:prelim-vacpol`, `ex:prelim-eikonal-two`, `ex:prelim-plus`

### Ch03

| label | type | tag | title |
|---|---|---|---|
| `def:ir-landau-setup` | def | (no tag) | 定义  — Feynman 参数表示与 Symanzik 多项式 |
| `lem:ir-envelope` | lem | (数学，无标签) | 引理  — 包络恒等式 |
| `thm:ir-landau-alpha` | thm | [R, R_PT] | 定理  — Landau 条件（参数形式）：解析性与红外有限性判据 |
| `thm:ir-landau-momentum` | thm | [R, R_PT] | 定理  — 动量空间的钳夹必要条件 |
| `rem:ir-landau-status` | rem | [A] | 注 |
| `def:ir-pinch-surface` | def | (no tag) | 定义  — 钳夹面、内禀坐标与法坐标 |
| `prop:ir-coleman-norton` | prop | [R, R_PT] | 命题  — Coleman–Norton 定理（代数形式） |
| `prop:ir-pinch-classification` | prop | [A] | 命题  — 钳夹面与约化图 |
| `def:ir-scalings` | def | (no tag) | 定义  — 区域标度 |
| `prop:ir-power-counting` | prop | [R, R_PT] | 命题  — 超表观红外发散度 |
| `thm:ir-leading-regions` | thm | [A] | 定理  — 领头区域 |
| `def:ir-glauber` | def | (no tag) | 定义  — Glauber 区 |
| `prop:ir-glauber-trapping` | prop | [R, R_PT] | 命题  — 单圈 Glauber 区的钳夹判据 |
| `thm:ir-bn-qed` | thm | [R, R_PT] | 定理  — QED 中的 Bloch–Nordsieck 定理 |
| `thm:ir-kln` | thm | [A] | 定理  — KLN 定理 |
| `prop:ir-bn-failure` | prop | [V] | 命题  — 有色初态时非阿贝尔 Bloch–Nordsieck 抵消的失效 |
| `def:ir-safe` | def | (no tag) | 定义  — 红外安全可观测量 |
| `thm:ir-safe-finite` | thm | [A] | 定理  — 红外安全可观测量的有限性 |
| `def:ir-regions` | def | (no tag) | 定义  — 区域方法 |
| `thm:ir-regions-euclid` | thm | [R, R_PT] | 定理  — 欧氏极限的渐近展开 |
| `prop:ir-regions-minkowski` | prop | [P] | 命题  — Minkowski 极限下区域方法的地位 |

Examples: `ex:ir-vertex`, `ex:ir-k-dominance`, `ex:sudakov-offshell`, `ex:ir-regions-toy`, `ex:ir-real-emission`

### Ch04

| label | type | tag | title |
|---|---|---|---|
| `def:sudakov-ff` | def | (no tag) | 定义  — 夸克形状因子 |
| `prop:sudakov-oneloop` | prop | [R, R_PT] | 命题  — 一圈形状因子（精确到 $\varepsilon$ 的所有阶） |
| `thm:sudakov-factorization` | thm | [A] | 定理  — Sudakov 形状因子的全阶因子化 |
| `prop:sudakov-kg` | prop | [A] | 命题  — $K+G$ 演化方程 |
| `cor:sudakov-exponentiation` | cor | [A] | 推论  — 指数化与解析延拓 |
| `def:sudakov-cusp` | def | (no tag) | 定义  — cusp 反常维度 |
| `prop:sudakov-webs` | prop | [A] | 命题  — 非阿贝尔指数化（webs） |
| `thm:sudakov-ir-poles` | thm | [A] | 定理  — 无质量多腿振幅红外极点的因子化 |
| `prop:sudakov-dipole-violation` | prop | [V] | 命题  — 偶极子公式作为全阶精确公式的失效 |
| `prop:sudakov-coulomb` | prop | [R, R_PT] | 命题  — Coulomb 相位 |
| `prop:sudakov-amplitude-factorization` | prop | [A] | 命题  — 振幅的硬—软—共线因子化（出射或阈值运动学） |
| `rem:sudakov-spacelike` | rem | [V] | 注 |

Examples: `ex:method-sudakov-subtraction`, `ex:sudakov-onshell-hard`, `ex:sudakov-massive`, `ex:sudakov-ll`

### Ch05

| label | type | tag | title |
|---|---|---|---|
| `def:ee-R` | def | (no tag) | 定义  — $R$ 比 |
| `prop:ee-R-ImPi` | prop | [R, R_def] | 命题  — $R=12\pi\,{\rm Im}\,\Pi$ |
| `prop:ee-analytic` | prop | [R, R_def] | 命题  — 解析性与正定性 |
| `lem:ee-single-scale` | lem | [R, R_PT] | 引理  — 无质量传播子型图的单标度结构 |
| `def:ee-adler` | def | (no tag) | 定义  / 命题  — Adler 函数 |
| `prop:ee-adler-dispersion` | prop | [R, R_def] | 定义  / 命题  — Adler 函数 |
| `thm:ee-euclid-ir` | thm | [R, R_PT] | 定理  — 欧氏红外有限性 |
| `prop:ee-adler-rg` | prop | [R, R_PT] | 命题  — Adler 函数的重整化群 |
| `thm:ee-R-finite` | thm | [R, R_PT] | 定理  — $R(s)$ 在微扰论每一阶的红外有限性 |
| `cor:ee-cuts` | cor | [A] | 推论  — 与部分子末态求和的等同；KLN |
| `prop:ee-oneloop` | prop | [R, R_PT] | 命题  — $O(\alpha_s)$ 的实辐射与虚修正 |
| `prop:ee-twoloop` | prop | [R, R_PT] | 命题  — 欧氏两圈关联函数 |
| `prop:ee-cutting-exact` | prop | [R, R_PT] | 命题  — $O(g^2)$ 处精确到 $\varepsilon$ 的切割恒等式 |
| `cor:ee-R-alphas` | cor | [R, R_PT] | 推论  — $R(s)$ 的微扰展开 |
| `prop:ee-contour` | prop | [R, R_def] | 命题  — 围道公式 |
| `thm:ee-ope` | thm | [A] | 定理  — 流关联函数的欧氏 OPE |
| `conj:ee-np-ope` | conj | [C] | 猜想  — 非微扰 OPE 与凝聚 |
| `prop:ee-smearing` | prop | [R, R_def] | 命题  — Poggio–Quinn–Weinberg 抹平恒等式 |
| `conj:ee-duality` | conj | [C] | 猜想  — 夸克—强子对偶 |

Examples: `ex:ee-twoloop-route`, `ex:ee-pi2`, `ex:ee-quark-spectrum`

### Ch06

| label | type | tag | title |
|---|---|---|---|
| `def:dis-kinematics` | def | (no tag) | 定义  — DIS 运动学与强子张量 |
| `prop:dis-W-structure` | prop | [R, R_def] | 命题  — 强子张量的一般结构 |
| `def:dis-compton` | def | (no tag) | 定义  — 前向 Compton 振幅 |
| `prop:dis-compton-analytic` | prop | [R, R_PT] | 命题  — 解析性与交叉 |
| `prop:dis-dispersion` | prop | [R, R_PT] | 命题  — 色散关系：Taylor 系数 = 矩 |
| `def:dis-twist` | def | (no tag) | 定义  — 扭度与扭度 2 算符 |
| `lem:dis-tree-ope` | lem | [R, R_PT] | 引理  — 树图 OPE |
| `thm:dis-ope` | thm | [A] | 定理  — 重整化微扰论中的欧氏 OPE |
| `prop:dis-wilson-partons` | prop | [R, 以 OPE 为前提] | 命题  — 由部分子结构函数提取 Wilson 系数 |
| `prop:dis-ope-rg` | prop | [R, 以 OPE 为前提] | 命题  — Wilson 系数与约化矩阵元的重整化群 |
| `thm:dis-moments` | thm | [R, 以 OPE 为前提] | 定理  — DIS 结构函数矩的因子化 |
| `cor:dis-scaling` | cor | [R, 以 OPE 为前提] | 推论  — 标度破坏 |
| `prop:dis-c-oneloop` | prop | [R, R_PT] | 命题  — 单圈 Wilson 系数 |
| `rem:dis-uniqueness` | rem | — | 注  — 偶数矩决定 C 偶组合（数学） |
| `rem:dis-nonuniform` | rem | — | 注  — 矩的 $O(1/Q^2)$ 不蕴含逐点 $O(1/Q^2)$ |
| `prop:dis-light-cone` | prop | [A] | 命题  — 光锥展开 |
| `prop:dis-twist4` | prop | [R, 以 OPE 为前提] | 命题  — 扭度 4 修正的算符结构 |
| `prop:dis-tmc` | prop | [R, 以 OPE 为前提] | 命题  — 靶质量修正 |
| `thm:dis-bjorken` | thm | [R, 以 OPE 为前提] | 定理  — Bjorken 求和规则 |
| `rem:dis-crewther` | rem | — | 注  — Crewther 关系 |

Examples: `ex:dis-free-quark`, `ex:dis-n2`, `ex:dis-oneloop-ope`, `ex:dis-tmc-n2`

### Ch07

| label | type | tag | title |
|---|---|---|---|
| `def:pdf-quark` | def | (no tag) | 定义  — 夸克分布 |
| `def:pdf-antiquark` | def | (no tag) | 定义  — 反夸克分布 |
| `def:pdf-gluon` | def | (no tag) | 定义  — 胶子分布 |
| `prop:pdf-invariance` | prop | [R, R_def] | 命题  — 规范不变性、推动不变性与自由场值 |
| `thm:pdf-support-pt` | thm | [R, R_PT] | 定理  — 支撑（微扰论） |
| `prop:pdf-support-hadron` | prop | [A] | 命题  — 支撑（强子态） |
| `rem:pdf-number-density` | rem | — | 注  — 数密度诠释（启发式） |
| `def:pdf-lightray` | def | (no tag) | 定义  — 光线算符 |
| `lem:pdf-wilson-moments` | lem | [R, R_def] | 引理  — Wilson 线顶点的矩 = 定域算符顶点 |
| `thm:pdf-moments-local` | thm | [R, R_PT] | 定理  — PDF 的矩 = 扭度 2 定域算符矩阵元 |
| `thm:pdf-dglap` | thm | [R, R_PT] | 定理  — 由算符重整化得到 DGLAP 方程 |
| `prop:pdf-lo-kernels` | prop | [R, R_PT] | 命题  — 领头阶分裂函数 |
| `prop:pdf-pqq-operator` | prop | [R, R_PT] | 命题  — Feynman 规范下由算符定义计算 $P_{qq}$ |
| `prop:pdf-partonic-dr` | prop | [R, R_PT] | 命题  — 纯维数正规化中的部分子分布 |
| `prop:pdf-local-anomalous` | prop | [R, R_PT] | 命题  — 定域算符的单圈反常维度（含混合） |
| `thm:pdf-dis-xspace` | thm | [R, 以 OPE 为前提] | 定理  — DIS 的 $x$ 空间因子化（扭度 2 部分） |
| `prop:pdf-sum-rules` | prop | [R, R_PT] | 命题  — 求和规则 |
| `rem:pdf-ns-plusminus` | rem | — | 注  — 解析延拓与 $P^\pm_{\rm NS}$ |
| `rem:pdf-schemes` | rem | — | 注  — 方案变换 |
| `conj:pdf-positivity` | conj | [C] | 猜想  — $\overline{\rm MS}$ PDF 的正定性 |
| `def:pdf-ff` | def | (no tag) | 定义  — 碎裂函数 |
| `prop:pdf-timelike-dglap` | prop | [R, R_PT] | 命题  — 类时 DGLAP 演化 |
| `def:pdf-polarized` | def | (no tag) | 定义  — 螺旋度与横度分布 |

Examples: `ex:pdf-free-field`, `ex:pdf-oneloop`, `ex:pdf-moments-exact`, `ex:pdf-quark-in-gluon`

### Ch08

| label | type | tag | title |
|---|---|---|---|
| `def:method-regions` | def | (no tag) | 定义  — 区域的偏序 |
| `def:method-collinear-approx` | def | (no tag) | 定义  — 共线近似子 |
| `def:method-soft-approx` | def | (no tag) | 定义  — 软近似子 |
| `lem:method-collinear-accuracy` | lem | [A] | 引理  — 共线近似的精度 |
| `lem:method-soft-accuracy` | lem | [A] | 引理  — 软近似的精度 |
| `lem:method-gy` | lem | (数学恒等式，无标签) | 引理  — Grammer–Yennie 分解 |
| `prop:method-gy-suppression` | prop | [A] | 命题  — G 部分的幂次压低 |
| `lem:method-ward-elementary` | lem | [R, R_PT] | 引理  — 基本 Ward 恒等式 |
| `lem:method-ward-abelian` | lem | [R, R_PT] | 引理  — 阿贝尔 Ward 恒等式 |
| `prop:method-ward-one` | prop | [R, R_PT] | 命题  — 单个纵向胶子的非阿贝尔 Ward 恒等式 |
| `prop:method-ward-tree` | prop | [R, R_PT] | 命题  — 树图层次的非阿贝尔恒等式与 PDF Wilson 线的种子 |
| `lem:method-ward-multi` | lem | [A] | 引理  — 多个 K 胶子的 Ward 恒等式与 Wilson 线 |
| `prop:method-collinear-wilson` | prop | [A] | 命题  — 共线 Wilson 线与 PDF |
| `prop:method-soft-wilson` | prop | [A] | 命题  — 软 Wilson 线 |
| `def:method-subtraction` | def | (no tag) | 定义  — 减除项 |
| `thm:method-subtraction` | thm | [A] | 定理  — 减除定理 |
| `prop:method-chains` | prop | — | 命题  — 减除的链展开（森林公式类比） |
| `lem:method-soft-unitarity` | lem | [R, R_def] | 引理  — 软因子的幺正性 |
| `prop:method-fsi` | prop | [A] | 命题  — 末态相互作用的幺正性相消 |
| `prop:method-glauber-oneloop` | prop | [R, R_PT] | 命题  — 两条程函线之间的单胶子交换 |
| `prop:method-glauber-deformation` | prop | [A] | 命题  — Glauber 区的围道变形判据 |
| `thm:method-template` | thm | [A] | 定理  — 因子化模板定理 |
| `prop:method-scale-scheme` | prop | [R, R_def] | 命题  — 因子化标度与方案 |

Examples: `ex:method-dis-oneloop`, `ex:method-ward-tree`, `ex:method-glauber-oneloop`

### Ch09

| label | type | tag | title |
|---|---|---|---|
| `def:disall-breit` | def | (no tag) | 定义  — Breit 系与投影算符 |
| `prop:disall-regions` | prop | [A] | 命题  — DIS 的领头区域 |
| `lem:disall-fsi` | lem | [A] | 引理  — 末态喷注的非钳夹性 |
| `prop:disall-h2` | prop | [A] | 命题  — (H2) 的验证 |
| `prop:disall-h3h4` | prop | [A] | 命题  — (H3)(H4) 平凡成立 |
| `prop:disall-h5` | prop | [A] | 命题  — (H5) 的验证 |
| `thm:disall-factorization` | thm | [A] | 定理  — DIS 共线因子化（动量空间，$x$ 空间逐点） |
| `cor:disall-consistency` | cor | [R, 以 OPE 为前提] | 推论  — 与 OPE 系数的一致性 |
| `prop:disall-nlo` | prop | [R, R_PT] | 命题  — $O(\alpha_s)$ 的 $\overline{\rm MS}$ 系数函数 |
| `prop:disall-scale` | prop | [R, R_PT] | 命题  — 标度无关性 |
| `prop:disall-dis-scheme` | prop | [R, R_def] | 命题  — DIS 方案 |
| `thm:disall-heavy` | thm | [A] | 定理  — 含重夸克质量的因子化（Collins 1998） |
| `prop:disall-nuclear` | prop | [A] | 命题  — 核靶上的 DIS |

Examples: `ex:disall-nlo`, `ex:disall-gluon`, `ex:disall-heavy-lo`

### Ch10

| label | type | tag | title |
|---|---|---|---|
| `def:coll-sia` | def | (no tag) | 定义  — 单举湮灭的运动学 |
| `prop:coll-sia-regions` | prop | [A] | 命题  — SIA 的领头区域 |
| `thm:coll-sia` | thm | [A] | 定理  — $e^+e^-\to hX$ 的因子化 |
| `rem:coll-sia-nlo` | rem | — | 注  — 系数函数与检验 |
| `thm:coll-sidis` | thm | [A] | 定理  — 共线 SIDIS 的因子化 |
| `thm:coll-direct-photo` | thm | [A] | 定理  — 直接光生与光子结构函数 |
| `prop:coll-photon-sf` | prop | [R, 以 OPE 为前提] | 命题  — 光子结构函数的点状部分 |
| `conj:coll-resolved-photo` | conj | [C] | 猜想  — 分辨光生 |
| `prop:coll-diffractive-photo` | prop | [V] | 命题  — 衍射光生中的因子化破坏 |
| `prop:coll-luxqed` | prop | [A] | 命题  — 质子的光子分布 |
| `def:coll-g1` | def | (no tag) | 定义  — 极化结构函数 |
| `thm:coll-g1-moments` | thm | [R, 以 OPE 为前提] | 定理  — $g_1$ 的奇数矩 |
| `prop:coll-anomaly-scheme` | prop | [R, R_PT] | 命题  — 一阶矩的方案依赖 |
| `prop:coll-ellis-jaffe` | prop | [V] | 命题  — Ellis–Jaffe 求和规则作为预言 |
| `conj:coll-bc` | conj | [C] | 猜想  — Burkhardt–Cottingham 求和规则 |
| `prop:coll-ww` | prop | [V] | 命题  — Wandzura–Wilczek 关系的一般失效 |
| `def:coll-transversity` | def | (no tag) | 定义  — 横度分布 |
| `prop:coll-transversity-evolution` | prop | [R, R_def] | 命题  — 横度的演化 |
| `prop:coll-soffer` | prop | [R, R_PT] | 命题  — Soffer 不等式 |
| `rem:coll-christ-lee` | rem | — | 注 |

Examples: `ex:coll-sia-lo`

### Ch11

| label | type | tag | title |
|---|---|---|---|
| `def:dy-kin` | def | (no tag) | 定义  — DY 运动学 |
| `prop:dy-born` | prop | [R, R_PT] | 命题  — Born 截面 |
| `prop:dy-regions` | prop | [A] | 命题  — DY 的领头区域 |
| `prop:dy-glauber-pinch` | prop | [R, R_PT] | 命题  — 单个割图中的 Glauber 钳夹 |
| `lem:dy-fsi` | lem | [A] | 引理  — 旁观者末态相互作用的幺正性相消 |
| `prop:dy-deformation` | prop | [A] | 命题  — 移除末态极点后的围道变形 |
| `lem:dy-soft` | lem | [A] | 引理  — 软因子为 1 |
| `prop:dy-universality` | prop | [R, R_def] | 命题  — DY 与 DIS 的共线 PDF 是同一对象 |
| `thm:dy-factorization` | thm | [A] | 定理  — 单举 DY 的共线因子化 |
| `prop:dy-abelian-model` | prop | [P] | 命题  — 阿贝尔模型中旁观者 Glauber 相位的相消 |
| `prop:dy-nlo` | prop | [R, R_PT] | 命题  — $O(\alpha_s)$ 的 $\overline{\rm MS}$ 系数函数 |
| `prop:dy-scale` | prop | [R, R_PT] | 命题  — $\mu_F$ 无关性 |
| `rem:dy-dis-scheme` | rem | — | 注 |
| `thm:dy-colour-singlet` | thm | [A] | 定理  — 色单态末态 |
| `thm:dy-polarized` | thm | [A] | 定理  — 极化 Drell–Yan |
| `conj:dy-coloured-final` | conj | [C] | 猜想  — 强子对撞中有色末态的共线因子化 |
| `conj:dy-polarized-jets` | conj | [C] | 猜想  — 极化强子对撞中的 $A_{LL}$（喷注、$\pi^0$） |
| `thm:dy-higher-twist` | thm | [A] | 定理  — $1/Q^2$ 处的广义因子化 |
| `prop:dy-twist6-failure` | prop | [V] | 命题  — 更高幂次的因子化失效 |

Examples: `ex:dy-nlo`, `ex:dy-threshold`, `ex:dy-glauber-model`

### Ch12

| label | type | tag | title |
|---|---|---|---|
| `def:thr-limit` | def | (no tag) | 定义  — 部分子阈值与强子阈值 |
| `thm:thr-refactorization` | thm | [A] | 定理  — DY 阈值重新因子化与指数化 |
| `prop:thr-oneloop` | prop | [R, R_PT] | 命题  — 单圈检验 |
| `rem:thr-prescriptions` | rem | — | 注 |
| `prop:thr-dis` | prop | [A] | 命题  — DIS 的大 $x$ 重新因子化 |
| `prop:thr-nlp` | prop | [P] | 命题  — 次领头幂次的阈值对数 |

Examples: `ex:thr-dy`

### Ch13

| label | type | tag | title |
|---|---|---|---|
| `def:tmd-kin` | def | (no tag) | 定义  — 小 $q_T$ 区域 |
| `prop:tmd-regions` | prop | [A] | 命题  — 小 $q_T$ 的领头区域 |
| `def:tmd-unsub` | def | (no tag) | 定义  — 未减除的 TMD 关联函数 |
| `def:tmd-soft` | def | (no tag) | 定义  — 软因子 |
| `def:tmd-collins` | def | (no tag) | 定义  — Collins 的 TMD 定义 |
| `rem:tmd-schemes` | rem | — | 注  — 其他方案 |
| `rem:tmd-scheme-constants` | rem | — | 注  — 方案常数（$S_\varepsilon$ 约定） |
| `prop:tmd-h1h5` | prop | [A] | 命题  — 小 $q_T$ DY 对模板假设的验证 |
| `lem:tmd-glauber` | lem | [A] | 引理  — TMD DY、SIDIS、$e^+e^-$ 中的 Glauber 相消 |
| `lem:tmd-soft-oneloop` | lem | [R, R_PT] | 引理  — 单圈软因子 |
| `thm:tmd-factorization` | thm | [A] | 定理  — Drell–Yan 的 TMD 因子化 |
| `prop:tmd-evolution` | prop | [A] | 命题  — Collins–Soper 方程与重整化群方程 |
| `prop:tmd-evolution-oneloop` | prop | [R, R_PT] | 命题  — 单圈演化系数与硬因子的 RG 相容性 |
| `prop:tmd-css` | prop | [A] | 命题  — CSS 解与非微扰输入 |
| `prop:tmd-small-b` | prop | [A] | 命题  — 小 $b$ 展开 |
| `thm:tmd-sivers-sign` | thm | [R, R_def] | 定理  — Sivers 函数的符号反转（算符层面） |
| `cor:tmd-sivers-observable` | cor | [A] | 推论  — 可观测不对称的符号反转 |
| `prop:tmd-collins-universality` | prop | [A] | 命题  — T-奇碎裂函数的普适性 |
| `def:tmd-etqs` | def | (no tag) | 定义  — Qiu–Sterman (ETQS) 关联函数 |
| `prop:tmd-twist3-matching` | prop | [P] | 命题  — 与扭度 3 共线因子化的匹配 |
| `rem:tmd-kt-integral` | rem | — | 注  — $\int d^2k_T\,f\ne f$ |

Examples: `ex:tmd-oneloop`, `ex:tmd-qt-asymptotics`, `ex:tmd-sivers-model`

### Ch14

| label | type | tag | title |
|---|---|---|---|
| `def:scet-modes` | def | (no tag) | 定义  — 模式 |
| `prop:scet-scalings` | prop | [R, R_def] | 命题  — 场的标度 |
| `prop:scet-lagrangian` | prop | [R, R_PT] | 命题  — 领头阶共线夸克拉氏量 |
| `prop:scet-wilson` | prop | [R, R_PT] | 命题  — 共线 Wilson 线 |
| `prop:scet-gauge` | prop | [R, R_def] | 命题  — 共线与超软规范对称性 |
| `thm:scet-decoupling` | thm | [R, R_def] | 定理  — 超软退耦（BPS 场重定义） |
| `rem:scet-y-direction` | rem | — | 注  — $Y_n$ 的方向与 $i0$ |
| `def:scet-zero-bin` | def | (no tag) | 定义  — 零箱减除 |
| `prop:scet-scet2` | prop | [R, R_PT] | 命题  — SCET$_{\rm II}$ 与软 Wilson 线 |
| `prop:scet-rapidity-rg` | prop | [A] | 命题  — 快度发散的处理与等价性 |
| `prop:scet-glauber-operators` | prop | [A] | 命题  — Glauber 算符 |
| `prop:scet-hard-matching` | prop | [R, R_PT] | 命题  — 硬匹配系数 |
| `thm:scet-thrust` | thm | [A] | 定理  — 推力分布的因子化 |
| `prop:scet-thrust-oneloop` | prop | [R, R_PT] | 命题  — 单圈因子与 RG 一致性 |
| `prop:scet-ll` | prop | [A] | 命题  — 领头对数指数 |
| `rem:scet-assumptions` | rem | — | 注  — SCET 证明的前提 |

Examples: `ex:scet-wn-tree`, `ex:scet-decoupling-tree`, `ex:scet-thrust-oneloop`

### Ch15

| label | type | tag | title |
|---|---|---|---|
| `def:jets-algorithms` | def | (no tag) | 定义  — 红外安全的喷注定义与事件形状 |
| `prop:jets-sw` | prop | [R, R_PT] | 命题  — Sterman–Weinberg 两喷注截面 |
| `cor:jets-ir-finite` | cor | [A] | 推论  — 红外安全喷注截面的有限性 |
| `prop:jets-thrust-lo` | prop | [R, R_PT] | 命题  — 领头阶推力分布 |
| `conj:jets-hadronization` | conj | [C] | 猜想  — 强子化修正的普适性 |
| `prop:jets-ngl` | prop | [R, R_PT] | 命题  — 非全局对数的存在 |
| `thm:jets-bms` | thm | [A] | 定理  — BMS 方程 |
| `prop:jets-ngl-beyond` | prop | [P] | 命题  — 超出领头对数与有限 $N_c$ |
| `thm:jets-ngl-factorization` | thm | [A] | 定理  — 喷注过程的有效场论因子化 |
| `prop:jets-sll` | prop | [P] | 命题  — 超领头对数 |

Examples: `ex:jets-sw`

### Ch16

| label | type | tag | title |
|---|---|---|---|
| `def:smallx-regge` | def | (no tag) | 定义  — 高能极限 |
| `thm:smallx-bfkl` | thm | [A] | 定理  — BFKL 方程 |
| `prop:smallx-kt` | prop | [P] | 命题  — $k_T$（高能）因子化 |
| `thm:smallx-bk` | thm | [A] | 定理  — BK 方程与 JIMWLK |
| `conj:smallx-saturation` | conj | [C] | 猜想  — 饱和与色玻璃凝聚 |
| `rem:smallx-nonuniform` | rem | — | 注  — 共线因子化在小 $x$ 的非一致性 |

Examples: `ex:smallx-dla`

### Ch17

| label | type | tag | title |
|---|---|---|---|
| `def:break-generalized-tmd` | def | (no tag) | 定义  — 标准与广义 TMD 因子化 |
| `prop:break-colour` | prop | [R, R_PT] | 命题  — 单个额外胶子的色因子（胶子极强度） |
| `thm:break-tmd` | thm | [V] | 定理  — 强子—强子末态强子的 TMD 因子化不成立 |
| `prop:break-spacelike` | prop | [V] | 命题  — 类空共线极限中严格共线因子化的失效 |
| `prop:break-mass-singularity` | prop | [C] | 命题  — 超出 NNLO 的质量奇异性因子化 |
| `prop:break-fss` | prop | [V] | 命题  — Coulomb 相位与软交换不对易导致的共线因子化破坏 |
| `prop:break-jet-veto` | prop | [V] | 命题  — 对多重部分子相互作用敏感的观测量 |
| `def:break-diffraction` | def | (no tag) | 定义  — 衍射 DIS 与衍射部分子分布 |
| `thm:break-ddis` | thm | [A] | 定理  — 衍射 DIS 的因子化 |
| `prop:break-hh-diffraction` | prop | [V] | 命题  — 强子—强子硬衍射中的因子化破坏 |
| `def:break-dpdf` | def | (no tag) | 定义  — 双部分子分布与双 Drell–Yan |
| `thm:break-double-dy` | thm | [A] | 定理  — 双 Drell–Yan 的因子化 |
| `conj:break-dps-coloured` | conj | [C] | 猜想  — 有色末态的双部分子散射 |
| `conj:break-pocket` | conj | [C] | 猜想  — "口袋公式" $\sigma_{\rm DPS}=\sigma_A\sigma_B/\sigma_{\rm eff}$ |

Examples: `ex:break-c07`, `ex:break-colour`, `ex:break-spacelike`

### Ch18

| label | type | tag | title |
|---|---|---|---|
| `def:excl-da` | def | (no tag) | 定义  — 介子分布振幅 |
| `prop:excl-erbl` | prop | [R, R_PT] | 命题  — 单圈 ERBL 演化 |
| `thm:excl-pion-ff` | thm | [A] | 定理  — 介子电磁形状因子的因子化 |
| `prop:excl-pion-lo` | prop | [R, R_PT] | 命题  — 领头阶硬核 |
| `thm:excl-transition` | thm | [A] | 定理  — $\gamma^*\gamma\to\pi^0$ 形状因子 |
| `prop:excl-endpoint` | prop | [P] | 命题  — 端点区域与软重叠 |
| `def:excl-gpd` | def | (no tag) | 定义  — 广义部分子分布 |
| `prop:excl-polynomiality` | prop | [R, R_def] | 命题  — 多项式性与 Ji 求和规则 |
| `thm:excl-dvcs` | thm | [A] | 定理  — DVCS 的因子化 |
| `prop:excl-dvcs-lo` | prop | [R, R_PT] | 命题  — DVCS 领头阶系数函数 |
| `thm:excl-meson-L` | thm | [A] | 定理  — 纵向光子介子产生的因子化 |
| `prop:excl-meson-T` | prop | [V] | 命题  — 横向光子：标准共线因子化失效 |
| `rem:excl-hadron-scattering` | rem | — | 注  — 宽角强子散射 |

Examples: `ex:excl-pion-ff-lo`

### Ch19

| label | type | tag | title |
|---|---|---|---|
| `thm:heavy-bdpi` | thm | [A] | 定理  — $B\to D\pi$ 的全阶因子化 |
| `prop:heavy-qcdf-lp` | prop | [P] | 命题  — 无粲两体衰变的领头幂次 QCD 因子化 |
| `prop:heavy-qcdf-endpoint` | prop | [V] | 命题  — 幂次修正中的端点发散 |
| `thm:heavy-inclusive-b` | thm | [A] | 定理  — 单举 $B$ 衰变的重夸克展开 |
| `def:heavy-nrqcd` | def | (no tag) | 定义  — NRQCD 及其幂次计数 |
| `thm:heavy-nrqcd-decay` | thm | [A] | 定理  — 衰变的 NRQCD 因子化 |
| `prop:heavy-nrqcd-matching` | prop | [R, R_PT] | 命题  — 匹配系数 |
| `conj:heavy-nrqcd-production` | conj | [C] | 猜想  — 产生的 NRQCD 因子化 |
| `prop:heavy-quarkonium-fragmentation` | prop | [A] | 命题  — 大 $p_T$ 重夸克偶素产生 |

Examples: `ex:heavy-cv`

### Ch20

| label | type | tag | title |
|---|---|---|---|
| `prop:power-dis-twist4-x` | prop | [A] | 命题  — DIS 扭度 4 修正的 $x$ 空间形式 |
| `prop:power-twist3-sidis` | prop | [P] | 命题  — SIDIS 型过程中的扭度 3 共线因子化 |
| `conj:power-twist3-pp` | conj | [C] | 猜想  — 强子—强子碰撞中单举强子单自旋不对称的扭度 3 因子化 |
| `prop:power-next-to-soft` | prop | [R, R_PT] | 命题  — 次软定理 |
| `prop:power-nlp-endpoint` | prop | [P] | 命题  — 次领头幂次因子化与端点发散 |
| `def:power-borel` | def | (no tag) | 定义  — Borel 变换与重整化子 |
| `prop:power-adler-large-beta0` | prop | [P] | 命题  — 大 $\beta_0$ 极限下的 Adler 函数 |
| `prop:power-renormalon-examples` | prop | [P] | 命题  — 若干过程中的重整化子与幂次修正 |
| `conj:power-renormalon-ht` | conj | [C] | 猜想  — 红外重整化子与高扭度的一般对应 |
| `rem:power-np-status` | rem | — | 注  — 非微扰地位 |
| `thm:power-ope-convergence` | thm | [R, R_PT] | 定理  — 微扰 $\varphi^4_4$ 中 OPE 的收敛性 |
| `prop:power-thooft-model` | prop | [P] | 命题  — 't Hooft 模型 |

Examples: `ex:power-renormalon-chain`, `ex:power-sgp`

### Ch21

| label | type | tag | title |
|---|---|---|---|
| `prop:lattice-moments` | prop | [R, 以 OPE 为前提] | 命题  — 格点可计算的矩 |
| `def:lattice-quasi` | def | (no tag) | 定义  — 准分布、赝分布与格点截面 |
| `prop:lattice-renormalizability` | prop | [A] | 命题  — Wilson 线夸克双线性算符的乘法可重整性 |
| `thm:lattice-lamet` | thm | [A] | 定理  — LaMET/短距离因子化 |
| `prop:lattice-cs-kernel` | prop | [A] | 命题  — 格点 Collins–Soper 核 |
| `rem:lattice-critiques` | rem | — | 注  — 批评与回应 |

Examples: `ex:lattice-quasi-tree`

### AppA

| label | type | tag | title |
|---|---|---|---|
| `lem:appA-fierz` | lem | (数学，无标签) | 引理  — 共线 Fierz 分解 |
| `lem:appA-plus-product` | lem | (数学，无标签) | 引理  — 乘积约定下的恒等式 |
| `lem:appA-mellin-table` | lem | (数学，无标签) | 引理  — Mellin 变换表 |

### AppB

| label | type | tag | title |
|---|---|---|---|
| `prop:appB-rules` | prop | [R, R_def] | 命题  — Wilson 线的 Feynman 规则 |
| `lem:appB-shuffle` | lem | (数学，无标签) | 引理  — 程函恒等式（洗牌积） |
| `prop:appB-webs` | prop | [A] | 命题  — 非阿贝尔指数化 |
| `prop:appB-cusp-oneloop` | prop | [R, R_PT] | 命题  — 单圈尖点反常维度 |

### AppC

| label | type | tag | title |
|---|---|---|---|
| `rem:appC-Seps` | rem | — | 注  — $S_\varepsilon$ 约定的影响 |
| `lem:appC-bubble` | lem | (数学，无标签) | 引理  — 单圈两点函数 |
| `lem:appC-ibp` | lem | (数学，无标签) | 引理  — 分部积分（三角规则） |
| `lem:appC-phase-space` | lem | (数学，无标签) | 引理  — $D$ 维相空间 |

### AppD

| label | type | tag | title |
|---|---|---|---|
| `lem:appD-gordan` | lem | (数学，无标签) | 引理  — Gordan 择一定理 |

### AppE

| label | type | tag | title |
|---|---|---|---|
| `prop:appE-degree` | prop | [R, R_PT] | 命题  — 约化图的超表观红外发散度 |
| `rem:appE-actual-bound` | rem | [A] | 注  — 从超表观度到实际界 |

### AppF

| label | type | tag | title |
|---|---|---|---|
| `prop:appF-two-gluon` | prop | [R, R_PT] | 命题  — 两个纵向胶子：树图层次的完整证明 |
| `prop:appF-induction` | prop | [A] | 命题  — 多胶子情形的归纳论证 |

### AppI

| label | type | tag | title |
|---|---|---|---|
| `def:appI-hvbm` | def | (no tag) | 定义  — HVBM 方案 |
| `prop:appI-larin` | prop | [R, R_PT] | 命题  — Larin 方案与非单态轴矢流的有限重整化 |
| `rem:appI-anomaly` | rem | — | 注  — 轴矢反常 |

### AppJ

| label | type | tag | title |
|---|---|---|---|
| `prop:appJ-ghost-cuts` | prop | [R, R_PT] | 命题  — 割图中的鬼场贡献 |
| `prop:appJ-local-operators` | prop | [R, R_PT] | 命题  — 规范不变定域算符的重整化与混合 |
| `rem:appJ-nonlocal` | rem | [A] | 注  — 非定域算符 |

### AppK

| label | type | tag | title |
|---|---|---|---|
| `lem:appK-hausdorff` | lem | (数学) | 引理  — Hausdorff 唯一性 |
| `thm:appK-even-moments` | thm | (数学) | 定理  — 偶数矩决定函数 |
| `cor:appK-pdf` | cor | (数学) | 推论  — PDF 的唯一性 |
| `prop:appK-kernels` | prop | (数学) | 命题  — 领头阶核由偶数矩唯一确定 |
| `thm:appK-carlson` | thm | (数学，经典，引用) | 定理  — Carlson 定理 |
| `prop:appK-continuation` | prop | (数学) | 命题  — 多项式有界条件下延拓的唯一性 |
| `thm:appK-muntz` | thm | (数学，经典，引用; `Muntz1914`, `Szasz1916`) | 定理  — Müntz–Szász |
| `rem:appK-counterexamples` | rem | — | 注  — 反例与稳定性 |

### AppL

| label | type | tag | title |
|---|---|---|---|
| `lem:appL-divided-differences` | lem | (数学) | 引理  — 均差恒等式 |
| `prop:appL-bare` | prop | [R, R_def] | 命题  — 裸算符恒等式 |
| `prop:appL-renormalized` | prop | [R, R_PT] | 命题  — 重整化后的矩关系 |


### Figures per chapter

See `FIGURES_INDEX.md` §4. In total: 44 existing figures (tikz1 12 final; tikz2 16 and tikz3 16 being redone), 29 new required figures and 10 new optional figures (audit: `fig:disall-seed`, `fig:disall-heavy`, `fig:dy-abelian-model` promoted to required; ownership of `fig:reduced-dis`, `fig:reduced-dy` → Ch3, `fig:dis-oneloop`, `fig:higher-twist` → Ch6, `fig:soft-eikonal` → Ch2).

### Verified formulas

Every `VF-…` identifier cited in this outline is defined in `VERIFIED_FORMULAS.md`. The groups are CONV 1–24, EE 1–15, SUD 1–5, REG 1–14, WL 1–13, DIS 1–14, PDF 1–15, DY 1–14, THR 1–3, TMD 1–10, SCET 1–16, NRQ 1–4, BQ 1–6, EXC 1–13, POL 1–3, GLA 1–13 and MISC 1–5 (audit additions: CONV-24, SUD-5, TMD-9/10, BQ-6, POL-3, GLA-13, MISC-4/5). Entries with status **T** must be re-derived or hedged (WRITER_SPEC §6.4).

---------------------------------------------------------------------------------------------------

## CHANGELOG

**2026-10-10 — spec audit (auditor agent).** Inputs re-read: all spec files; CONTEXT.md; REQUIREMENTS.md; the critic (O1–O21, D1–D12), survey (items 1–30) and the c_* derivations, including the new `research/c_tmd/DERIVATION.md` and c_glauber §3–§4; the frontier status tables. Independent checks (scripts in the auditor's scratchpad `audit/`): labels unique and prefix-correct (346 statements); every referenced label, VF ID, bib key and figure label exists; registry tags = entry tags = master-table tags; page budget 5 + 260 + 35 = 300; bibliography 646 entries, BibTeX 0 warnings/0 errors with `\nocite{*}`. Changes:
1. **Sources.** Header and Ch13/Ch17 source paragraphs updated: c_tmd DERIVATION (17/17 scripts pass) and c_glauber §3–§4 now exist; all c_tmd-dependent "(to verify)" marks resolved (VF-TMD-1…10), Ch17 "§3/§4 pending" marks removed.
2. **New §0.8** (dependency order; composite tags; [A] deductions in `proofsketch`; [P] restricted proofs; MA lines) and **§0.9** (open items from REQUIREMENTS.md: frontier chapters on Ji's LaMET proofs and Yizhuang Liu's work, formal-blueprint appendix, refdoc integration; optimistic frontier grades not adopted). Front matter, Ch1, Ch21, Ch22 put on hold pending the lead author's decision.
3. **Forward dependency removed — Ch4:** `thm:sudakov-factorization` proof plan no longer uses Ch8 lemmas; it uses Ch2–Ch3, the elementary identities and Collins 2011 §10.3/§10.8 (complete for this case); Ch8 results are pointers only; explicit `\uses{}` list.
4. **Ch5:** `thm:ee-ope` gets a self-contained proof sketch and its own status paragraph (it previously referred to the later `thm:dis-ope`); `thm:dis-ope` refers back.
5. **Ch6:** `prop:dis-c-oneloop` no longer depends on Ch9 (`prop:disall-nlo`): primary derivation via App G + Mellin moments, cross-check by the hard-region forward amplitude; `prop:dis-wilson-partons` no longer cites Ch7 as a proof step.
6. **Ch8:** `prop:method-collinear-wilson` cites `prop:prelim-wilson-covariance` instead of the later `prop:dy-universality`; `prop:method-glauber-deformation` cites `prop:method-fsi`.
7. **Ch10 → Ch11:** polarized DY and $A_{LL}$ (which rest on Ch11) moved and relabelled `thm:dy-polarized`, `conj:dy-polarized-jets` (old labels retired).
8. **Ch20 → Ch13:** the ETQS correlator definition moved to Ch13 as `def:tmd-etqs` (old label retired), because `prop:tmd-twist3-matching` (Ch13) uses it; Ch20 refers back.
9. **Figures (first-use ownership):** `fig:reduced-dis`, `fig:reduced-dy` → Ch3; `fig:dis-oneloop`, `fig:higher-twist` → Ch6; `fig:soft-eikonal` → Ch2; `fig:disall-seed`, `fig:disall-heavy`, `fig:dy-abelian-model` made required. Caption-notation ($n,\bar n$) warning added.
10. **Tag/proof consistency:** `thm:method-template`, `thm:disall-factorization`, `thm:dy-factorization`, `thm:tmd-factorization` ([A]) now specify a `proofsketch` with the deduction written out (they said "Proof: full", contradicting WRITER_SPEC §4.7); `prop:dy-abelian-model`, `prop:power-adler-large-beta0` ([P]) clarified.
11. **Over-claims corrected:** `prop:scet-ll` [R, R_PT] → [A] (with the [R, R_def] RG-solution content as item (b)); `prop:coll-soffer` restricted to "preserved by LO evolution", with the caveat that the bound is not a theorem for $\overline{\rm MS}$ densities; `prop:coll-diffractive-photo` restricted to resolved photoproduction (survey item 28, c_glauber §3.6); `thm:break-ddis` proof plan rewritten (the old text gave the argument c_glauber §6 item 6 explicitly corrects); `conj:pdf-positivity` sharpened (all-scale positivity is false, Collins–Rogers–Sato model); `prop:ir-regions-minkowski` gains the hidden-region counterexample (`Gardi:2024axt`).
12. **Formula fixes:** App I Larin replacement sign in the binding $\epsilon$ convention ($-\frac i6$, VF-CONV-24; numerically verified); `thm:tmd-factorization` uses $\sigma_0/s$ (the symbol $\sigma_0$ had two meanings); `thm:lattice-lamet` power-correction forms made consistent and the matching argument written $\mu/(|y|P^z)$; `prop:tmd-small-b` error term $O((mb_T)^p)$; `ex:coll-sia-lo` normalization made explicit (VF-MISC-5); `thm:heavy-bdpi` operator normalization stated (VF-BQ-6); `ex:smallx-dla` normalization of $\gamma_{gg}$ fixed.
13. **Verified items that were "(to verify)":** one-loop cusp $\Gamma(\beta)$ (Ch4, App B; VF-CONV-23), dipole-formula normalization (VF-SUD-5), BFKL intercept and BK normalization (VF-MISC-4), SLL order and coefficient (VF-GLA-13), SIA angular normalization, two-body phase space (App C), TMD scheme constants, ζ normalization, order of limits and space-like regulator lines (Ch13, VF-TMD-9).
14. **Meta-assumption lines** added to 36 hadron-level statements (including the moved `thm:dy-polarized`) that lacked them (marked "(MA: audit)"); master-table rows 19, 39, 67 updated accordingly.
15. Ch22: `longtable` replaced by split `table` floats (it is not loaded); Ch21 scope note; Ch14 `prop:scet-rapidity-rg` normalization partly fixed ($D=-\tilde K/2$).
16. Registry: moved labels and counts updated (Ch10 20, Ch11 19, Ch13 21, Ch20 12 statements; total unchanged at 346); `prop:scet-ll` tag updated; VF groups list updated.
17. **Corrections taken from `refdoc/REFDOC_ANALYSIS.md` §2.4 (written 15:02, during the audit), each re-checked by the audit:** `def:pdf-ff` prefactor $z^{1-2\varepsilon}/(4N_c)$ in the hadron frame (OUR-1; frame-change Jacobian); `thm:method-subtraction` caveat and conditions (CS1)–(CS3) (OUR-2); hadronic caveat in the proof plan of `thm:dis-moments` (OUR-3; rest-frame Euclidean segment $|\omega|=O(M/Q)$ checked); two-component Glauber deformation in `prop:method-glauber-deformation` (OUR-4); `prop:tmd-small-b` remainder note (OUR-5); forward amplitude vs discontinuity in `thm:disall-factorization` (OUR-6); exceptional forward momenta in `thm:dis-ope` (OUR-8); `Shifman2000` booktitle (OUR-7, INSPIRE-checked). §0.9 item 3 updated; the file's structural proposals are left to the lead author.

