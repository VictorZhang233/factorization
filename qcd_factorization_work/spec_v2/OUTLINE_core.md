> **SUPERSEDED (2026-10-10).** This draft was merged by the spec-v2 integrator into `FINAL_OUTLINE_v2.md`, with the fixes and merge decisions listed there (§0.8) and in `AUDIT_v2.md`. Writers must use `FINAL_OUTLINE_v2.md` (and `checks/check_unit_v2.py` reads only its registry); this file is kept unchanged below as the drafter's record.
>
> **VOID MARKERS (2026-10-11, audit v2.3.1).** The `[PENDING-VERIFY]` markers, planning tags, reserved slot labels and candidate texts below were resolved by the verify patch v2.3 in `FINAL_OUTLINE_v2.md` (§0.10, §00.4, §10); the undelivered slot labels are withdrawn and must not be used. Nothing in this file may be copied into a unit.

# OUTLINE_core — spec v2 core outline: Ch1–Ch21, Ch25 and Appendices A–L
## 《QCD 因子化定理：严格证明、全阶论证与适用边界》

**Status.** Draft of the spec-v2 **core drafter** (2026-10-10). This file is one of the four drafts that the spec-v2 synthesizer merges into `spec_v2/FINAL_OUTLINE_v2.md`: `OUTLINE_core.md` (this file: front matter, Ch1–Ch21, Ch25, App A–L), `OUTLINE_appMNOPQ.md` (App M–Q), `OUTLINE_frontier.md` (Ch22–Ch24), `ASSUMPTIONS.md` (the register of numbered assumptions). It supersedes `spec/FINAL_OUTLINE.md` (v1) for every unit it covers.

**Inputs read for this draft.** `CONTEXT.md`; `REQUIREMENTS.md` (items 1–5); `spec/FINAL_OUTLINE.md` (v1, all 2641 lines, incl. registry and CHANGELOG); `spec/WRITER_SPEC.md`; `refdoc/REFDOC_ANALYSIS.md` (§0, §1.2–1.3, §2 incl. §2.4–2.5, §3, §4, **§5 S1–S63 in full**); `frontier/lamet/LAMET.md` (§12 status board, §13 open problems, §14 new results), `frontier/yzliu/YZLIU.md` (§6–§7), `frontier/others/OTHERS.md` (§7, §14); `research/critic/REVIEW.md` (§3.1, §7); `verify/CLAIMS.md` (index and the entries cited below; the verification itself is still running); the spec-v2 companion drafts that already exist (re-read in their revision **v2.1** before assembly): `spec_v2/WRITER_SPEC_v2.md`, `spec_v2/VERIFIED_FORMULAS_v2.md` (groups CONV…MISC, **QCD**, REF, LAM, YZL, FRO), `spec_v2/FIGURES_INDEX_v2.md`, `spec_v2/REFS_NOTES_v2.md`, `spec_v2/refs_merged_v2.bib` (1003 entries in v2.1; every citation key of this file resolves), `spec_v2/checks/check_unit_v2.py`; the Furry monograph `furry_qcd.tex` (§2 "约定、QCD 拉氏量与带标号的微扰展开", as the model for the pedagogical Ch2).

**Companion files (binding, same directory).** `WRITER_SPEC_v2.md` (rules: §3 conventions, §4 tags/qualifiers/assumptions/`\uses`, §5 labels and definition ownership, §6 content obligations, §7 readability of Part I, §10 QA), `VERIFIED_FORMULAS_v2.md` (copy formulas only from there; "VF-…" below), `FIGURES_INDEX_v2.md` (figure owners and drawing specs), `refs_merged_v2.bib` + `REFS_NOTES_v2.md` + `key_aliases_v2.tsv` (citations).

**Planning markers used in this file (never printed in the book).**
- **[PENDING-VERIFY: id]** — the final wording, the tag, a novelty claim or an erratum depends on the running verification workflow (`verify/`). `id` is a claim id of `verify/CLAIMS.md` (E01…E36 errata, N01…N29 new results, A01…A28 attributions), one of the proof extensions **X1** (Glauber, App O), **X2** (subtraction, App N), **X3** (OPE, App M), or an open verification item **S63-k** of refdoc §5.11. A later spec patch finalizes these places (WRITER_SPEC_v2 §6.12). Until then writers follow WRITER_SPEC_v2 §6.12 (tag not stronger than given here; no marker and no novelty claim printed).
- **[SYNC-APP]** — label owned by App M/N/O/P/Q (`OUTLINE_appMNOPQ.md`); the label is the one proposed in refdoc §5.6 (S46–S49) and must be checked against that draft at the merge.
- **[SYNC-ASM]** — content, tag or owner of a register entry (`asm:`) to be checked against `ASSUMPTIONS.md`.
- **[SYNC-FRONTIER]** — label or row owned by Ch22–Ch24 (`OUTLINE_frontier.md`); provisional here.

---------------------------------------------------------------------------------------------------

## 0. Global decisions for the core units

### 0.1 Binding v2 structure (lead-author decision; chapter keys are label prefixes)

Labels of existing statements are **not renamed** when a statement changes chapter (WRITER_SPEC_v2 §5.3). Units covered by this file are in **bold**.

| part | # | key | file | 中文标题（`\chapter{}` 标题） | pp | format |
|---|---|---|---|---|---|---|
| — | **front** | — | `front.tex` | 摘要、阅读指南、严格性标签、记号与约定 | **6** | front (Ch1 writer) |
| I 基础 | **1** | `intro` | `ch01_intro.tex` | 引言：部分子图像、因子化的含义与严格性分级 | **14** | full |
| I | **2** | `qcd` | `ch02_qcd.tex` | QCD 基础——从规范不变性到渐近自由 | **18** | **pedagogical (new)** |
| I | **3** | `prelim` | `ch03_prelim.tex` | 因子化的数学与场论工具 | **12** | full |
| I | **4** | `ir` | `ch04_ir.tex` | 费曼积分的红外结构：钳夹、幂次计数与红外安全 | **15** | full |
| I | **5** | `sudakov` | `ch05_sudakov.tex` | Sudakov 形状因子与振幅的红外结构 | **14** | full |
| II 严格核心 | **6** | `ee` | `ch06_ee.tex` | 严格核心 I：$e^+e^-$ 湮灭总截面 | **14** | full |
| II | **7** | `dis` | `ch07_dis.tex` | 严格核心 II：深度非弹散射与算符乘积展开 | **18** | full |
| II | **8** | `pdf` | `ch08_pdf.tex` | 严格核心 III：部分子分布与碎裂函数的算符定义 | **15** | full |
| III 共线因子化 | **9** | `method` | `ch09_method.tex` | 全阶因子化证明的一般方法 | **20** | full |
| III | **10** | `disall` | `ch10_disall.tex` | DIS 的全阶动量空间证明、重夸克与核靶 | **13** | full |
| III | **11** | `coll` | `ch11_coll.tex` | 其他共线过程：单举湮灭、SIDIS、光生、极化与横度 | **13** | full |
| III | **12** | `dy` | `ch12_dy.tex` | Drell–Yan 过程与强子—强子碰撞 | **18** | full |
| III | **13** | `thr` | `ch13_thr.tex` | 阈值重求和与重新因子化 | **9** | short |
| IV 共线之外 | **14** | `tmd` | `ch14_tmd.tex` | 横动量依赖（TMD）因子化 | **16** | full |
| IV | **15** | `scet` | `ch15_scet.tex` | 有效场论方法：SCET | **13** | full |
| IV | **16** | `jets` | `ch16_jets.tex` | 喷注、事件形状、非全局对数与超领头对数 | **10** | short |
| IV | **17** | `smallx` | `ch17_smallx.tex` | 小 $x$ 与高能因子化 | **9** | short |
| IV | **18** | `break` | `ch18_break.tex` | 因子化的破坏与非标准情形 | **14** | full |
| V 其他硬过程 | **19** | `excl` | `ch19_excl.tex` | 硬遍举过程 | **11** | short |
| V | **20** | `heavy` | `ch20_heavy.tex` | 重夸克物理：$B$ 介子衰变与重夸克偶素 | **10** | short |
| VI 极限 | **21** | `power` | `ch21_power.tex` | 幂次修正、次领头幂次、重整化子与非微扰地位 | **13** | full |
| VII 前沿进展 | 22 | `lamet` | `ch22_lamet.tex` | LaMET 与格点因子化：季向东等人的因子化证明 | 18 | frontier (`OUTLINE_frontier.md`; absorbs v1 Ch21 `lattice`, labels kept) |
| VII | 23 | `yzliu` | `ch23_yzliu.tex` | Yizhuang Liu 的严格因子化研究 | 15 | frontier |
| VII | 24 | `front` | `ch24_front.tex` | 其他前沿严格结果 | 18 | frontier |
| (after VII) | **25** | `summary` | `ch25_summary.tex` | 总结：主表、依赖图与开放问题 | **12** | full |
| 附录 | **A–L** | `appA`…`appL` | v1 file names | v1 titles | **35** | tools |
| 附录 | M, N, O, P, Q | `appM`…`appQ` | `appM_ope.tex`, `appN_subtraction.tex`, `appO_glauber.tex`, `appP_blueprint.tex`, `appQ_errata.tex` | OPE：微扰证明、无质量 QCD、非微扰条件定理 / Collins 减除法的精确形式 / 光锥排序微扰论与 Drell–Yan 的 Glauber 相消 / 形式化蓝图：假设登记表、依赖图与状态表 / 经核实的文献勘误 | 24+24+32+10+4 | `OUTLINE_appMNOPQ.md` |

Totals (lead author): front 6 + chapters 352 + appendices 129 ≈ **487 pp**. Core units of this file: front 6 + chapters (Ch1–Ch21, Ch25) 301 + App A–L 35 = **342 pp**.

**What moves where (v1 → v2).** v1 Ch2 `prelim` is split: its QCD-basics half (QCD Lagrangian, Feynman rules, BRST, Slavnov–Taylor, $\overline{\rm MS}$, $\beta$, RG, composite-operator renormalization) moves, **with unchanged labels**, into the new pedagogical Ch2 `qcd`; its tool half (light front, Wilson lines, distributions/Mellin, cut diagrams, unitarity, $\gamma_5$) stays in Ch3 `prelim`. v1 Ch3–Ch20 become Ch4–Ch21 (same keys). v1 Ch21 `lattice` moves to Ch22 `lamet` (frontier outline). v1 Ch22 `summary` becomes Ch25. Part VI is now Ch21 only; Part VII (Ch22–Ch24) is new.

### 0.2 Page budgets and the appendix rebalancing proposal

Chapter budgets: as in the table. Tolerance −15 %/+10 % (WRITER_SPEC_v2 §11). Never cut statements, `\uses` lists, status lines or the boxes of WRITER_SPEC_v2 §6.6; cut first optional figures and examples beyond the minimum counts of WRITER_SPEC_v2 §7.

**App A–L (35 pp, lead-author decision).** refdoc S50–S53 add material to App A, C, D, E, F, J, K (refdoc S10 asked for +9 pp). It must fit into 35 pp (WRITER_SPEC_v2 §1.1 note 3). **Proposal for the lead author (no statement is deleted):** A 3, B 3 (−1: the eikonal-identity proofs are compressed because Ch3 states the rules with the universal rule), C 3, D 4, E 3, F 3, G 3 (−1: App G keeps the derivations not printed in the chapters; the Ch10/Ch12 worked examples are printed in full in the chapters), H 2, I 2, J 3 (+1: `lem:appJ-cut-hermiticity`), K 4 (+1: `lem:appK-entire`, `lem:appK-markov`), L 2 = **35**. The App D alternative proof (refdoc S52) is given as a 1-page remark with its caveats, not as a second full proof; App E and App F additions are ≤ 0.5 pp each. If the lead author keeps the v1 split (3,4,3,4,3,3,4,2,2,2,3,2), the App J/K additions must be compressed to fit, and the writer reports it.

### 0.3 Tag system v2 (binding; full rules in WRITER_SPEC_v2 §4)

1. **Five tags** `\tagR \tagA \tagP \tagC \tagV` with the CONTEXT.md meanings, attached to the statement **exactly as formulated**.
2. **Four `[R]` qualifiers**, exactly one per `[R]`, printed verbatim as the first sentence (WRITER_SPEC_v2 §4.3): **R_PT**, **R_def**, **R_OPE** (replaces v1's 「以 OPE 为前提」; every v1 statement with that qualifier is relabelled R_OPE in this file), **R_cond** (complete proof from explicitly numbered assumptions; the premise sentence 「前提：\cref{asm:…}…。」 follows immediately). In this file the qualifier is written inside the tag bracket: `[R, R_PT]`, `[R, R_def]`, `[R, R_OPE]`, `[R, R_cond]`.
3. **Grade propagation** (refdoc S5; WRITER_SPEC_v2 §4.6). Order $[R]>[A]>[P]>[C]$; $[V]$ outside the order. A statement is never stronger than its weakest premise (definitions, pure mathematics and the six global non-perturbative assumptions `asm:intro-*` excepted). An R_cond implication has a **content grade** = the weakest of its premises; a statement that uses it inherits that content grade (technical premises only). **R_OPE** (WRITER_SPEC_v2 v2.1 §4.6 item 1): the OPE premises `thm:dis-ope`, `prop:dis-ope-euclid`, `prop:dis-ope-gi`, `prop:dis-ope-forward` are not counted for an R_OPE statement; its content grade is [A] for its users; an R_cond statement that uses an R_OPE statement lists `thm:dis-ope` in its premise sentence (this file avoids such uses: `thm:dis-moments-np` uses the operator RG directly, not `prop:dis-ope-rg`). **Global-only R_cond premises:** an R_cond statement whose premises are only global `asm:intro-*` entries (e.g. `prop:dis-dispersion-np`, `thm:dis-fixed-n`, `thm:dis-moments-np`) has content grade [R] and may be used by R_OPE statements about hadrons, whose status line names the same global assumptions (`thm:dis-moments`(b)); the qualifier table of WRITER_SPEC_v2 §4.6 item 1 does not mention this case — reported to the synthesizer.
4. **Rule TA — how technical assumptions enter the propagation (= WRITER_SPEC_v2 v2.1 §4.4 item 2 and §4.6 item 3; the tags themselves are the register's, [SYNC-ASM]).** The technical assumptions of the register (`asm:appM-*`, `asm:appN-*`, `asm:appO-*`) are precise **integral-norm (E-N)** formulations of steps for which the standard literature (Collins 2011, CSS 1985–89, Aybat–Sterman 2009) gives all-order **arguments** at the level of scaling statements (E-S). Their propagation tag is therefore **`\tagA`** ("[A]-level": argued to all orders, E-N form open), not `\tagC`, unless the step has no all-order argument at all; conventions (`asm:appN-values`) carry no tag. This is exactly why the process theorems that depend on them are **[A]** and not [R] (binding grades of v1/refdoc S5), and why discharging them would upgrade those theorems. If `ASSUMPTIONS.md` tags any of these entries `\tagC`, the merge must either (a) change the entry to `\tagA` with the sentence 「全阶论证（标度陈述）见…；积分范数形式未证」, or (b) remove it from the `\uses` lists of the [A] process theorems and keep it only in the R_cond chain and the 「地位与缺口」 paragraph (the [A] grade then rests on the chapter-level argument). This draft writes the `\uses` lists under assumption (a). **Entries at risk** (their refdoc §5.3 status sentence could be read as `\tagP` or `\tagC`): `asm:appO-lcopt` ("[P] in the light-front literature"; used by `thm:dy-factorization`, `prop:method-fsi`, `prop:break-measurement`), `asm:appN-endpoint` ("true for finite Gegenbauer truncations"; used by `thm:excl-pion-ff`, `thm:excl-meson-L`), `asm:appM-forward` ("verified at $O(\alpha_s)$"; used through `prop:dis-ope-forward` by `thm:dis-ope`), `asm:appN-multren`(Z2) ("genuine input"; used by `thm:method-template`, `thm:disall-factorization`, `thm:coll-sia`, `prop:pdf-timelike-dglap`). Under Rule TA they are `\tagA` (the CSS/Collins and Lepage–Brodsky/Collins–Frankfurt–Strikman arguments cover these steps at the scaling level); the table `### Assumptions` of §08 lists the proposed tag of every register entry.
5. **Non-perturbative status line** (replaces v1's MA line; WRITER_SPEC_v2 §4.4 item 6): every statement about hadrons ends its hypotheses with 「非微扰地位：\cref{asm:…}、…（MA…）。」. The umbrella names are kept with the dictionary MA0 ⊃ `asm:intro-wightman`, `asm:intro-composite`; MA1+MA2(+MA4 asymptoticity) = `asm:intro-bridge`; MA3 = analyticity (now `prop:dis-dispersion-np` under MA0) + `asm:intro-growth`; MA4 ⊃ `asm:intro-af-coeff`; non-perturbative OPE = `asm:intro-np-ope`. The v1 lines are converted as follows (applied throughout this file):

   | v1 line | v2 line |
   |---|---|
   | MA0 (hadron states; matrix elements of local or light-ray operators) | `asm:intro-wightman`, `asm:intro-composite`（MA0） |
   | MA0 (analyticity, spectral condition only) | `asm:intro-wightman`（MA0） |
   | MA1, MA2 | `asm:intro-bridge`（MA1、MA2） |
   | MA1, MA2, MA4 | `asm:intro-bridge`（MA1、MA2、MA4） |
   | MA0, MA3, MA4 (OPE-based hadronic moments) | `asm:intro-wightman`, `asm:intro-composite`, `asm:intro-np-ope`, `asm:intro-af-coeff`（MA0、MA4）; plus `asm:intro-growth`（MA3） only for the moments $n<n_0$ |
   | MA0, MA4 | `asm:intro-wightman`, `asm:intro-composite`, `asm:intro-af-coeff`（MA0、MA4） or, for factorization-type statements, `asm:intro-bridge` |

   A statement about partonic states, operators or models only says 「（本命题只涉及部分子态。）」 (or 「…算符恒等式…」, 「…模型…」).
6. **Error types** E-S / E-P / E-F / E-N / E-W (refdoc S7; `def:intro-error-types`). Every step of an [A] or [P] proof sketch that rests on power counting names its type; every status table has a column 「误差类型」.
7. **Grade dictionary** (refdoc S8; `rem:intro-grade-dictionary`), printed without citing or naming the reference document (refdoc S62).
8. **Pure mathematics** carries no tag (`(数学，无标签)`); definitions carry no tag; a remark carries a tag only if given here.
9. **Composite statements**: the environment title carries the first (registry) tag; the other part is an item with its status in words (WRITER_SPEC_v2 §4.3 rule 3).

### 0.4 Labels

- Scheme (WRITER_SPEC_v2 §5.1): `ch:<key>`, `app:<key>`, `sec:<key>-<name>`, `def|asm|thm|lem|prop|cor|conj|rem|ex:<key>-<name>`, `tab:<key>-<name>`, `fig:<name>` (existing) / `fig:<key>-<name>` (new), `eq:<key>-<name>` (unit-internal).
- **Owner = the unit under which the label is listed in the registry of this file (§08), not its prefix.** Moved v1 labels keep their key: the nine QCD-basics labels with prefix `prelim` (`def:prelim-qcd`, `def:prelim-feynman-rules`, `def:prelim-brst`, `lem:prelim-brst-nilpotent`, `thm:prelim-slavnov-taylor`, `def:prelim-msbar`, `prop:prelim-beta`, `prop:prelim-rg`, `thm:prelim-composite-renorm`) and the section labels `sec:prelim-qcd`, `sec:prelim-brst`, `sec:prelim-renorm` are owned by **Ch2 `qcd`**; all other `prelim` labels by **Ch3 `prelim`**; the `lattice` labels by Ch22 (frontier outline); the `summary` labels by **Ch25**.
- **New labels:** Ch2 uses the key `qcd`; Ch3 keeps `prelim`; every other core chapter keeps its v1 key.
- **Labels proposed in refdoc §5 are adopted verbatim** (e.g. `rem:prelim-bphz-brst` — owner Ch2 although its key is `prelim` —, `prop:ir-super-leading`, `lem:dis-euclid-segment`, `thm:dis-fixed-n`, `def:method-collins-conditions`, `prop:dy-eikonal-twogluon`, …), because the App M/N/O drafts cite them.
- **Assumptions** `asm:<owner-key>-<name>`; the six `asm:intro-*` are owned and stated by Ch1; the others by App M/N/O ([SYNC-ASM]).
- The labels in this file are **canonical**: writers may add internal labels with their own key, never rename or reuse canonical ones.

### 0.5 Formalism: `\uses` lists (Lean-blueprint style; WRITER_SPEC_v2 §4.5)

1. Every `definition`, `assumption`, `lemma`, `proposition`, `theorem`, `corollary`, `conjecture`, every tagged `remark` and every `example` that relies on other statements carries exactly one `\uses{…}` as the last line of its body (the macro of `common/preamble_fact.tex` prints 「依赖：…」); a statement that depends on nothing has the comment `% uses: none`. In this file the list is given in each entry as a line beginning with `\uses{…}`, or as the comment line `% uses: none`.
2. A `\uses` list contains **every** statement label that the statement or its proof uses as a step: definitions of the objects in the statement, assumptions, lemmas/propositions/theorems invoked (including appendix lemmas when the proof is in an appendix), examples/remarks used as steps. Pointers (「比较…」「其推广见…」) are not dependencies and are written in running text only.
3. **Order.** A chapter statement uses only (a) statements of earlier chapters, (b) earlier statements of the same chapter, (c) statements of the appendices (App A–Q), (d) assumptions owned by Ch1 or by an appendix. **Chapter statements are listed in this file in their reading order**, which is the order in which writers must print them; `\uses` never points to a later statement of the same chapter. Ch1 and Ch25 may point forward in text, but their own statements obey the rule. Appendix statements may use any chapter statement (no cycles: App P's generator reports them).
4. **R_cond statements** list in `\uses` every assumption and every non-[R] statement of their premise sentence.
5. **Appendix proofs.** A chapter statement whose proof is in an appendix lists the appendix lemmas the proof uses; the appendix section begins with 「\cref{…} 的证明」 and does not restate the chapter statement.
6. **Only statement labels** in `\uses` (prefixes `def thm lem prop cor conj rem ex asm`), never `sec: eq: fig: tab: ch: app:`.

### 0.6 Format of the chapter entries (machine-parsable; checked by the drafter's script)

Each chapter entry has: title (中文 / English), `\label{ch:…}`, file, budget, format, part; **Purpose**; **Depends on**; **Box** (the content of 「本章证明了什么／没有证明什么」, WRITER_SPEC_v2 §6.6, for Ch2–Ch21); **Sections** (canonical `sec:` labels, in order); **Canonical statements** in reading order; **Worked examples** (minimum counts of WRITER_SPEC_v2 §7 for Part I); **Tables**; **Figures** (owners per FIGURES_INDEX_v2); **Misconception box** (allocation of WRITER_SPEC_v2 §6.8); **Key citation keys** (all in `refs_merged_v2.bib`); **Pending** (the [PENDING-VERIFY] items of the unit).

Each canonical statement is one bullet whose first line is

`* **<类型> \`<label>\` — <中文标题>** [<tag>] · <origin>`

with 类型 ∈ {定义, 假设, 定理, 引理, 命题, 推论, 猜想, 注, 例}; `[<tag>]` ∈ {`[R, R_PT]`, `[R, R_def]`, `[R, R_OPE]`, `[R, R_cond]`, `[A]`, `[P]`, `[C]`, `[V]`} or `(no tag)` / `(数学，无标签)`; origin = `v1` (carried over from v1, possibly with changes), `v1→rev.` (restated), `refdoc S#` (new from REFDOC_ANALYSIS), `new` (new in this draft). Sub-items: **陈述** (precise, in formulas, binding conventions), **非微扰地位** (hadron statements), **`\uses{…}`**, **证明** (full/sketch; steps; literature locations; VF IDs), **地位与缺口** (for [A]/[P]/[C]/[V], WRITER_SPEC_v2 §4.9), **Pending** where relevant.

### 0.7 Critical paths (to be drawn as `fig:intro-dependency`; the full graph is generated in App P)

- **QCD foundations (Ch2).** `def:prelim-qcd` → `thm:qcd-gauge-invariance`; `def:qcd-fp` + `def:prelim-brst` → `lem:prelim-brst-nilpotent` → `lem:qcd-st-regularized` → `thm:qcd-renormalizability` → {`prop:qcd-st-relations`, `thm:prelim-slavnov-taylor`, `prop:qcd-xi-independence`, `thm:prelim-composite-renorm`} → `prop:prelim-beta` → `prop:qcd-rge` → `prop:prelim-rg`, `thm:qcd-asymptotic-freedom`.
- **Rigorous core I ($e^+e^-$).** `thm:prelim-cutting-rules`, `prop:prelim-optical` → `prop:ee-analytic`, `lem:ee-single-scale`, `thm:ee-euclid-ir` → `thm:ee-R-finite` → `cor:ee-R-alphas`.
- **Rigorous core II (DIS).** PT route: `prop:dis-compton-analytic` → `prop:dis-dispersion`; `lem:dis-tree-ope` + `thm:prelim-composite-renorm` → `prop:dis-ope-euclid`, `prop:dis-ope-gi`, `prop:dis-ope-forward` (= `thm:dis-ope` [A]) → `thm:dis-moments` [R, R_OPE]. Hadronic route (App M): `prop:dis-dispersion-np` + `lem:dis-euclid-segment` + `lem:dis-ope-segment` → `thm:dis-fixed-n` → `thm:dis-moments-np` [R, R_cond] → `cor:dis-weak-xspace`. Then `thm:pdf-moments-local` (App K, App L) → `thm:pdf-dglap`, `thm:pdf-dis-xspace` [R, R_OPE].
- **All-order graphical (Ch4, Ch9; App N, O).** `thm:ir-landau-momentum` → `prop:ir-coleman-norton` → `prop:ir-pinch-classification` → `prop:ir-power-counting` → `thm:ir-leading-regions` (+ `prop:ir-super-leading`); (`thm:prelim-slavnov-taylor` → `prop:method-ward-one` → `lem:method-ward-multi` → `prop:method-collinear-wilson`, `prop:method-soft-wilson`); (`def:method-collins-conditions` → `thm:appN-subtraction` [R, R_cond] → `thm:method-subtraction` [A], bottleneck `asm:appN-collins`); (`lem:method-soft-unitarity`, `prop:method-fsi` ⟸ `lem:appO-unitarity`, `prop:method-glauber-deformation` ⟸ `thm:appO-main`) → **`thm:method-template`** → {`thm:disall-factorization`, `thm:coll-sia`, `thm:coll-sidis`, `thm:dy-factorization`, `thm:tmd-factorization`}.
- **The weakest links that fix the [A] tags** (cite them in every process chapter's status paragraph, by `asm:` label): (i) the non-abelian multi-gluon Ward identity with ghosts and the BRST classification of non-local operators — `lem:method-ward-multi`, `asm:appN-ward-product` (Collins 2011 §11.3.2 assumes it); (ii) the integral-norm subtraction estimates — `asm:appN-collins` (with `asm:appN-envelope`, `asm:appN-separation`, `asm:appN-contour`); (iii) the Glauber region — `asm:appO-mixing`(c), `asm:appO-deformation`(b)–(d), `asm:appO-rewritten-cs` (Collins 2011 §14.4.8 "Issues remaining"); (iv) the bridge to hadrons — `asm:intro-bridge`.

### 0.8 Status changes relative to v1 (binding; all tags not listed are unchanged)

| statement | v1 | v2 | reason |
|---|---|---|---|
| all statements with qualifier 「以 OPE 为前提」 (`prop:dis-wilson-partons`, `prop:dis-ope-rg`, `thm:dis-moments`, `cor:dis-scaling`, `prop:dis-twist4`, `prop:dis-tmc`, `thm:dis-bjorken`, `thm:pdf-dis-xspace`, `cor:disall-consistency`, `prop:coll-photon-sf`, `thm:coll-g1-moments`; Ch22: `prop:lattice-moments`) | [R, 以 OPE 为前提] | [R, R_OPE] | new qualifier name (lead author); the hadronic versions name `asm:intro-np-ope` in their status line |
| `thm:dis-ope` | [A], one statement | [A], umbrella for `prop:dis-ope-euclid` [A], `prop:dis-ope-gi` [A], `prop:dis-ope-forward` [A] | refdoc S19 (fixes OUR-8) |
| `thm:dis-moments` | proof "insert, contract, compare" | partonic part via `prop:dis-ope-forward`; hadronic part via `thm:dis-fixed-n`, `prop:dis-dispersion-np`, `thm:dis-moments-np`; "even $n\ge n_0$; all even $n\ge2$ under `asm:intro-growth`" | refdoc S22 (fixes OUR-3) |
| `prop:dis-compton-analytic`, `prop:dis-dispersion` | hadronic part under MA0/MA3 | partonic targets only; hadrons: `prop:dis-dispersion-np` [R, R_cond] | refdoc S21 |
| `thm:method-subtraction` | statement with steps (1)–(5) | new statement in integral norm; deduction [R, R_cond] = `thm:appN-subtraction`; the [A] is that of `asm:appN-collins` | refdoc S29 (fixes OUR-2) |
| `def:method-regions`, `def:method-collinear-approx`, `def:method-soft-approx`, `prop:method-chains` | v1 forms | per-line mode assignments; idempotent projectors; corrected forest analogy | refdoc S24, S26, S29 |
| `prop:method-glauber-deformation` | one-component deformation | items (a)–(c), simultaneous deformation along $e_G$ | refdoc S32 (fixes OUR-4) |
| `prop:method-fsi`, `lem:dy-fsi`, `prop:dy-deformation`, `lem:tmd-glauber` | sketches | same tags; precise forms in App O (`lem:appO-unitarity`, `thm:appO-main`, `prop:appO-tmd`) [PENDING-VERIFY: X1] | refdoc S31, S34, S36 |
| `thm:dy-factorization` | [A] with survey paragraph | [A] with four-layer status (precise chain, open inputs by label) | refdoc S34 |
| `prop:scet-ll` | [A] (audit) | [A] | unchanged |
| `prop:pdf-timelike-dglap` | [R, R_PT] | [A] (composite: one-loop content $P^{T(0)}=P^{(0)}$ [R, R_PT]) | all-order time-like evolution needs the multiplicative renormalizability of FFs, `asm:appN-multren`(Z1) (refdoc S23); weakened, not strengthened |
| `prop:method-scale-scheme`, `prop:disall-dis-scheme` | [R, R_def] | [R, R_PT] | grade kept; qualifier corrected because the proofs use R_PT statements (WRITER_SPEC_v2 §4.6 item 1) |
| `ex:dy-future-vs-past`, `prop:dy-eikonal-twogluon`, `lem:tmd-glauber` | — | same tags | `\uses` lists cleaned: `prop:method-glauber-oneloop` (R_PT) and `prop:dy-abelian-model` ([P]) are pointers there, not premises |
| new statements | — | 35 in Ch2 (incl. 10 examples), and the refdoc S13–S45 statements in Ch1, Ch3–Ch21 (listed per chapter); App A `def:appA-test-functions`, `lem:appA-weak-convergence`; App C `rem:appC-d-kernels`; App D `rem:appD-parameter-proof`; App F `ex:appF-telescoping`; App J `lem:appJ-cut-hermiticity`; App K `lem:appK-entire`, `lem:appK-markov` | REQUIREMENTS 3e; refdoc §5, S50–S53 |

No v1 tag is strengthened. No v1 canonical statement is deleted (the v1 statement `def:ee-adler` / `prop:ee-adler-dispersion` pair stays as two labels).

### 0.9 [PENDING-VERIFY] register of the core units

| item | where | depends on | what the patch decides |
|---|---|---|---|
| App M route of the DIS moments | Ch7: `prop:dis-ope-euclid` (upgrade path), `prop:dis-ope-gi`, `prop:dis-ope-forward`, `lem:dis-ope-segment`, `thm:dis-fixed-n`, `prop:dis-dispersion-np`, `prop:dis-low-moments`, `thm:dis-moments-np`, `cor:dis-weak-xspace`, `lem:dis-twist-classification`, `lem:dis-twist-chirality`, `prop:dis-chiral-suppression`, proof route of `prop:dis-ope-rg`; App K `lem:appK-entire`, `lem:appK-markov` | X3; S63-1, S63-2, S63-3, S63-4 | final statements, premise lists, whether `asm:appM-remainder` becomes a cited theorem (then `prop:dis-ope-euclid` may become [R, R_PT] and Ch25 open problem OP-A2 is reworded) |
| App N route of the subtraction theorem | Ch9: `thm:method-subtraction` (precise form), `def:method-collins-conditions`, `lem:method-local-accuracy`, `lem:method-pairing`, `prop:method-product`, `cor:method-removing-eps`, `lem:method-i0-compat`, `ex:method-naive-induction`, `ex:method-sudakov-subtraction`, `tab:method-errors`; Ch10: `prop:disall-two-routes`, `prop:disall-factorized-subtraction`, `thm:disall-renorm-compat`, `ex:disall-ladder`; Ch14: `prop:tmd-zero-bin-soft`(b), `lem:tmd-sqrt-identity` item (b); Ch19: `prop:excl-soft-cancel` | X2; N12; S63-12 | final statements; status wording (integral norm vs scaling) |
| App O route of the Glauber cancellation | Ch9: `prop:method-fsi`, `prop:method-glauber-deformation`(c), `rem:method-two-component`; Ch12: `thm:dy-factorization` layer 2–3, `tab:dy-status`, `lem:dy-poles-orientation`, `prop:dy-deformation`, `lem:dy-fsi`, `ex:dy-spectator-lcopt`, `ex:dy-future-vs-past`; Ch14: `lem:tmd-glauber` (precise form); Ch18: `prop:break-measurement`, failure location in `thm:break-tmd`; App J `lem:appJ-cut-hermiticity` | X1; N13; S63-8 | final statements; premise lists of `thm:appO-main` |
| 「本书新结果」 candidate | Ch12 `prop:dy-eikonal-twogluon`, `rem:dy-common-ordering` | N01; S63-5 | marker printed or dropped; citation of a prior source |
| sharpened results (not marked new) | Ch5/Ch9 pointers to `prop:appN-triangle-exact`(c) | N12 | wording "no logarithm at NLP" |
| verified computations (novelty never claimed) | Ch3 `lem:prelim-eikonal-identity` (adiabatic regulator); Ch6 `thm:ee-R-finite` route; Ch12 `prop:dy-abelian-model`, `rem:dy-dis-scheme` (plus trap); Ch14 `lem:tmd-soft-oneloop` (time-like vs space-like lines); Ch18 `prop:break-colour`, `thm:break-tmd`, `ex:break-c07`; Ch19 `prop:excl-endpoint`; Ch20 `prop:heavy-qcdf-endpoint`; App K | N26, N24, N25, N20, N16–N19, N21, N22, N23 | only the attribution sentence ("derived here" vs a literature source) |
| literature errata (App Q candidates) mentioned in core chapters | Ch5/Ch15/App B (Becher–Schwartz $\Gamma_1$, E23); Ch14 (Aybat–Rogers $\zeta$, E17); Ch15 (BS jet-function normalization E24; BPS ghost wording E25); Ch16 (Sterman–Weinberg $\ln2\epsilon$, E28; one-jettiness, E16); Ch18 (Collins 2007 eq. (10), E18); Ch19 (Ji 1997 eq. (15) $i\epsilon$, E20; Mankiewicz–Piller "9/τ", E21; NLO $\gamma_T^*$, E22; Guo–Ji–Liu ½, E12); Ch20 (BBNS "$m_M$", E26); Ch4 (Coleman–Norton proof gap E14, Landau-analysis errors E15); Ch7 ("commonly quoted" $C^{q}_{2,N}$ variant, E32); Ch9/App F (Collins 2011 errata, E27) | E12, E14–E18, E20–E28, E32 | printed as an App Q row or only silently corrected (with a `%` comment) |
| attributions | Ch12 (CSS 1988 errors corrected in Collins 2011, E31; Aybat–Sterman credit, A11); Ch4/Ch24 pointers (Collins 2020 preprint status, A08); Ch7 (OPE status, A09); Ch4 (regions, A10); Ch18 (Gaunt vs SYZ, E36); Ch8 (positivity, E35) | E31, E35, E36, A08–A11 | wording of the status paragraphs |
| open verification items | Ch14 (W+Y uniformity, S63-6; $p=2$ in `prop:tmd-small-b`, S63-7); Ch18 (`Becher:2024kmk` restoration evidence, S63-10); Ch20/Ch21 (Chay–Kim, BBK, FMRS, Bostelmann contents, S63-11); Ch9/Ch12/Ch15 (equation numbers of RS 2016 and Collins 2011, S63-9) | S63-6, 7, 9, 10, 11 | sentences supported by these sources |
| appendix items (App A–L) | App B `lem:appB-shuffle` (adiabatic regulator, N26), `prop:appB-cusp-oneloop` (Becher–Schwartz $\Gamma_1$, E23), `sec:appB-definition` ($g$-sign convention, E27); App D `sec:appD-caveats` (Collins 2020 preprint status, A08; Gordan identification, N02); App F `sec:appF-gy` (symmetric GY original, A18; Collins 2011 errata, E27), `ex:appF-telescoping` (N19); App J `lem:appJ-cut-hermiticity` (S63-8, X1; N14, class K3), `rem:appJ-nonlocal` (page numbers, A18; moment reduction, N04); App K (classical proofs, N23; `lem:appK-entire`, `lem:appK-markov` with the App M route, X3) | N02, N04, N14, N19, N23, N26, A08, A18, E23, E27, S63-8, X1, X3 | attribution sentences; App Q rows (E23 only, class Q1); final form of `lem:appJ-cut-hermiticity` |

### 0.10 External labels used by the core units (owned by other drafts)

- **App M** [SYNC-APP]: `def:appM-normal-product`, `lem:appM-chain-expansion`, `lem:appM-integrability`, `lem:appM-contact`, `thm:appM-ope-identity`, `ex:appM-tree`, `lem:appM-derivative-bounds`, `lem:appM-uniqueness`, `thm:appM-scaling`, `cor:appM-coordinate`, `ex:appM-unreduced`.
- **App N** [SYNC-APP]: `thm:appN-subtraction`, `prop:appN-triangle-exact`, `prop:appN-dy`.
- **App O** [SYNC-APP]: `lem:appO-lcopt`, `lem:appO-numerators`, `lem:appO-glauber-pc`, `lem:appO-hard-locality`, `lem:appO-cut-position`, `lem:appO-unitarity`, `lem:appO-equal-time`, `prop:appO-ss-localize`, `lem:appO-joint-localization`, `prop:appO-ss-cancel`, `lem:appO-glauber-operator`, `prop:appO-one-sided`, `lem:appO-no-crossing`, `prop:appO-target`, `prop:appO-eikonal`, `prop:appO-past-wilson`, `thm:appO-main`, `cor:appO-interface`, `prop:appO-tmd`.
- **Register entries owned by App M/N/O** [SYNC-ASM]: `asm:appM-remainder`, `asm:appM-brst-ope`, `asm:appM-forward`; `asm:appN-contour`, `asm:appN-envelope`, `asm:appN-separation`, `asm:appN-collins`, `asm:appN-values`, `asm:appN-cutsum`, `asm:appN-ward-product`, `asm:appN-uv`, `asm:appN-multren`, `asm:appN-tmd`, `asm:appN-endpoint`; `asm:appO-lcopt`, `asm:appO-envelope`, `asm:appO-mixing`, `asm:appO-deformation`, `asm:appO-rewritten-cs` (contents as in refdoc §5.3).
- **Ch22** (moved v1 labels, pointers only from Ch7, Ch8, Ch14, Ch21; dependencies only from Ch25): `def:lattice-quasi`, `prop:lattice-moments`, `prop:lattice-renormalizability`, `thm:lattice-lamet`, `prop:lattice-cs-kernel`, `rem:lattice-critiques`, `ex:lattice-quasi-tree`, `fig:quasi-pdf`, `fig:lattice-matching`.
- **Ch22–Ch24 new labels** [SYNC-FRONTIER]: used only in Ch25 (master-table block VII and open problems) and as chapter pointers (`\cref{ch:lamet}`, `\cref{ch:yzliu}`, `\cref{ch:front}`) elsewhere.

### 0.11 Where the refdoc changes S1–S63 are applied

| refdoc | content | applied in |
|---|---|---|
| S1–S4 | App M, N, O, P | `OUTLINE_appMNOPQ.md`; chapter statements that announce their proofs (Ch7, Ch9, Ch10, Ch12, Ch14, Ch18, Ch19) |
| S5–S8 | R_cond, register, error types, grade dictionary | §0.3; Ch1 `def:intro-tags`, `def:intro-error-types`, `rem:intro-grade-dictionary`, `def:intro-MA`, `asm:intro-*`, `tab:intro-assumptions` |
| S9 | FF normalization | Ch8 `def:pdf-ff` (applied in v1 audit; kept) |
| S10 | page budgets | superseded by the lead-author v2 budgets (§0.1, §0.2) |
| S11 | Glauber direction $e_G$ | WRITER_SPEC_v2 §3 row 38; Ch9 `prop:method-glauber-deformation`, `rem:method-two-component` |
| S12 | `asm:` labels | §0.4 |
| S13 | Ch1 | Ch1 |
| S14 | v1 Ch2 | Ch2 (`thm:prelim-composite-renorm`, `rem:prelim-bphz-brst`), Ch3 (`thm:prelim-cutting-rules` pointer) |
| S15–S17 | v1 Ch3–Ch5 | Ch4, Ch5, Ch6 |
| S18–S22 | v1 Ch6 | Ch7 |
| S23 | v1 Ch7 | Ch8 |
| S24–S26, S29–S32 | v1 Ch8 | Ch9 |
| S27–S28 | v1 Ch9 | Ch10 |
| S33 | v1 Ch10 | Ch11 |
| S34, S37 | v1 Ch11 | Ch12 |
| S35 | v1 Ch12, Ch15, Ch16 | Ch13, Ch16 (Ch17 unchanged) |
| S36 | v1 Ch13 | Ch14 |
| S38 | v1 Ch14 | Ch15 |
| S39 | v1 Ch17 | Ch18 |
| S40 | v1 Ch18 | Ch19 |
| S41 | v1 Ch19 | Ch20 |
| S42 | v1 Ch20 | Ch21 |
| S43 | v1 Ch21 | Ch22 (frontier outline) |
| S44 | v1 Ch22 | Ch25 |
| S45 | chapter format | boxes and correspondence tables in Ch2–Ch21 (WRITER_SPEC_v2 §6.6–6.7) |
| S46–S49 | App M–P contents | `OUTLINE_appMNOPQ.md` |
| S50–S53 | App K; A, C; D, E, F; J | App A, C, D, E, F, J, K (this file) |
| S54 | VF-REF | `VERIFIED_FORMULAS_v2.md`; cited per statement |
| S55 | master-table rows 69–75 | Ch25 `tab:summary-master` |
| S56 | figures | FIGURES_INDEX_v2 §3; cited per chapter |
| S57–S58 | misconceptions M29–M35, over-claims | WRITER_SPEC_v2 §6.8–6.9; misconception boxes per chapter |
| S59 | 「本书新结果」 | §0.9; Ch12 `prop:dy-eikonal-twogluon` |
| S60 | bibliography additions | `refs_merged_v2.bib` (all S60 keys now present except Gribov 1978, Lee–Zinn-Justin 1972, Zinn-Justin 1975, Appelquist–Carazzone 1975 — cited as 「文献待补」 where needed) |
| S61 | writer order | WRITER_SPEC_v2 §12.1 |
| S62 | reference document not citable | everywhere |
| S63 | open verification items | §0.9 |

### 0.12 Cross-links from the core units to the frontier chapters (pointers only)

Ch4 → Ch24 (Collins 2020 physical-region pinch criterion, Gordan's alternative, momentum-space Coleman–Norton, hidden regions); Ch5 → Ch23 (heavy–light Sudakov form factor, off-light-cone soft functions); Ch7 → Ch22 (lattice moments, quasi-PDF matching as a Euclidean OPE statement), Ch24 (rigorous OPE results: Hollands, Holland–Hollands–Kopper, Fröb–Holland); Ch8 → Ch22 (quasi-/pseudo-PDFs), Ch24 (positivity debate, BRST moment reduction); Ch9 → Ch24 (IR forest formula, Glauber EFT); Ch12, Ch18 → Ch24 (Glauber EFT, SYZ, factorization restoration, SLL resummation); Ch13 → Ch23 (threshold factorization of the quasi-PDF kernel); Ch14 → Ch22 (lattice CS kernel), Ch23 (quasi-TMD factorization, Euclidean soft functions, time-ordering theorem); Ch16, Ch17, Ch20 → Ch24 (NGL factorization, NLO BK and small-$x$ helicity, quarkonium updates); Ch21 → Ch22 (linear renormalon, LRR), Ch23 (Gross–Neveu and O($N$) models), Ch24 (NLP endpoint factorization, NLP TMD). These are forward pointers in running text, never `\uses`.

---------------------------------------------------------------------------------------------------

# 第一部分 基础 (Part I — Foundations)

---------------------------------------------------------------------------------------------------

## Front matter — `front.tex` (6 pp; written by the Ch1 writer)

- **摘要** (1 p): what the book proves and at which level, in the tag vocabulary (five tags, four `[R]` qualifiers); the landscape in one paragraph (rigorous core: $e^+e^-$, DIS moments, operator definitions; all-order arguments: DIS $x$ space, SIA, SIDIS, DY, TMD, thrust, DDIS, exclusive LP; partial/conjectural/violated cases; frontier: LaMET and quasi-TMD factorization, Euclidean formulations of soft functions, other rigorous progress); the formal blueprint (App P) and the verified errata (App Q) in one sentence each.
- **阅读指南与严格性标签** (1.5 pp): the five tags; the four qualifiers (verbatim strings of WRITER_SPEC_v2 §4.3); the register of numbered assumptions in one paragraph (six global `asm:intro-*`, technical `asm:appM/N/O-*`, frontier `asm:lamet/yzliu/front-*`); the error types in one line; the grade-propagation rule in two lines; how to read a `\uses` line (「依赖：…」) and the dependency graph of App P; reading paths through the seven parts: (i) rigorous core only: Ch2–Ch3, Ch6–Ch8 (+App M); (ii) collinear proofs: Part I + Ch9–Ch13 (+App N, O); (iii) boundaries: Ch14–Ch21; (iv) frontier: Ch22–Ch24; (v) summary: Ch25 + App P.
- **记号与约定** (3.5 pp): the notation table of WRITER_SPEC_v2 §3 (rows 1–48), typeset as `tab:front-notation` (split into `table` floats `tab:front-notation`, `tab:front-notation-b`, `tab:front-notation-c`, … with 「（续）」 captions; `longtable` is not loaded). Key clash: `front.tex` owns only the labels `tab:front-notation*`; every other `…:front-…` label belongs to Ch24 (WRITER_SPEC_v2 §1.1 note 2).

---------------------------------------------------------------------------------------------------

## Chapter 1 — 引言：部分子图像、因子化的含义与严格性分级 / Introduction: the parton picture, what factorization asserts, and levels of rigour

`\label{ch:intro}` · `ch01_intro.tex` · **14 pp** · full · Part I

**Purpose.** (i) Physical picture (time dilation, incoherence, hard–collinear–soft). (ii) Precise definition of a factorization statement and of "proof": asymptotic expansion in $m/Q$ at each fixed order of $\alpha_s$ (formal power series), remainder in integral norm (E-N) for partonic states, asymptotic statement for hadrons under numbered assumptions (critic O1; refdoc F3). (iii) The rigour system of the book: five tags, four `[R]` qualifiers, the register of numbered assumptions (six global ones stated here), error types, grade propagation (with Rule TA), the grade dictionary; the Lean-blueprint `\uses` formalism and App P. (iv) Kinds of factorization (critic W6), now including LaMET/short-distance factorization and quasi-TMD factorization. (v) Overview table of the main results (★ rows of Ch25's master table). (vi) Misconception box (14 items). (vii) Organisation: seven parts, App A–Q, reading paths, critical paths (`fig:intro-dependency`).

**Depends on.** Nothing (forward references only, to canonical labels). Its own definitions and assumptions obey §0.5 item 3: their `\uses` contain only earlier Ch1 labels; objects defined later are described inline with forward pointers.

**Box.** Not required (WRITER_SPEC_v2 §6.6); the first paragraph says what the book proves and at which level.

**Sections.**
1. `sec:intro-parton` 部分子模型与物理图像 — Feynman/Bjorken picture; infinite-momentum frame; ratio of time scales $\Delta x^+_{\rm probe}/\Delta x^+_{\rm hadron}\sim m^2/Q^2$; incoherent sum of squares; what each heuristic step becomes later (leading regions ↔ incoherence, light-front operators ↔ frozen ensemble, subtracted partonic cross sections ↔ quasi-free partons); `ex:intro-handbag`.
2. `sec:intro-statement` 因子化定理的一般形式 — `def:intro-hard-process`, `def:intro-factorization`; zero-, one-, two-hadron versions; preview of TMD, threshold, exclusive, NRQCD, SCET, LaMET statements (formula shapes only).
3. `sec:intro-proof` "证明"意味着什么 — two expansions; "all orders" = every fixed order (formal power series), never convergence; integral-norm remainder $O(\lambda^aL^K)$ uniformly in $\varepsilon$ (`def:intro-error-types`); asymptotic nature (renormalons); partonic external states with IR regulators vs hadrons; what is lost in the passage to hadrons (`asm:intro-bridge`); circularities to avoid (critic C1–C3: PDFs defined by operators first; DGLAP from renormalization before scale independence; no "proof" from the number-density picture); `rem:intro-sharpness`.
4. `sec:intro-tags` 严格性分级、编号假设与依赖关系 — `def:intro-tags`, `def:intro-error-types`, `rem:intro-grade-dictionary`, the six assumptions `asm:intro-*`, `def:intro-MA`, `tab:intro-assumptions`; how status lines and `\uses` lines are printed (example status line; example dependency line); App P.
5. `sec:intro-kinds` 因子化的种类 — `tab:intro-kinds`.
6. `sec:intro-overview` 结论总览 — `tab:intro-overview`.
7. `sec:intro-misconceptions` 常见误解 — `tcolorbox` with 14 items.
8. `sec:intro-organisation` 本书结构与阅读路线 — the seven parts and the appendices A–Q; the three tracks (rigorous core / all-order graphical / boundaries) plus frontier; critical paths (§0.7 of this outline); `fig:intro-dependency`.

**Canonical statements** (in reading order).

* **定义 `def:intro-hard-process` — 硬过程与幂次展开** (no tag) · v1
  - **陈述.** An observable $\sigma(Q;m)$ with hard scale $Q$ and infrared scales $m$ (hadron and parton masses, $\Lambda$, IR regulators) admits a *leading-power expansion* if $\sigma=\sigma_{\rm LP}+r$, $r=O((m/Q)^p)$, $p>0$; define "leading power", "power correction", "twist" (twist = dimension − spin; forward pointer `def:dis-twist`). Remark: in massless PT the only infrared scales are regulators; $\Lambda$ enters through $\alpha_s(\mu)$ (forward pointer `def:qcd-lambda`).
  - `% uses: none`

* **定义 `def:intro-factorization` — 共线因子化陈述** (no tag) · v1
  - **陈述.** $$\sigma(Q;m)=\sum_{i,j}\int_{x_a}^1\frac{d\xi_a}{\xi_a}\int_{x_b}^1\frac{d\xi_b}{\xi_b}\,H_{ij}\Big(\frac{x_a}{\xi_a},\frac{x_b}{\xi_b},\frac{Q}{\mu},\alpha_s(\mu)\Big)f_{i/A}(\xi_a;\mu)f_{j/B}(\xi_b;\mu)+r(Q;m),$$ with (a) $f$ = matrix elements of specified gauge-invariant renormalized operators (forward pointers `def:pdf-quark`, `def:pdf-gluon`); (b) $H_{ij}$ independent of the external states and of the IR regularization, computable order by order; (c) $r=O((m/Q)^p)$, understood order by order in $\alpha_s$ for partonic states (in integral norm, E-N) and as an asymptotic statement for hadrons under `asm:intro-bridge`. One-hadron version $F_2/x=\sum_iC_{2,i}\otimes f_i+r$; zero-hadron version: $e^+e^-$ total cross section (no PDFs; IR finiteness).
  - `\uses{def:intro-hard-process}`

* **注 `rem:intro-incoherence` — 部分子模型的非相干性论证（启发式）** (no tag) · v1
  - Time-dilation estimate; incoherence; explicitly heuristic; list of the later precise counterparts (`thm:ir-leading-regions`, `def:pdf-quark`, `thm:method-template`, as pointers).

* **例 `ex:intro-handbag` — 树图手提包与 Callan–Gross 关系** (no tag) · v1
  - With $W^{\mu\nu}$ normalized as in VF-CONV-13: leading-twist projection $\Phi\to\frac14\gamma^-{\rm Tr}[\gamma^+\Phi]$ (Fierz, VF-EXC-13), on-shell condition $\delta((\xi P+q)^2)$ fixes $\xi=x$: $F_2=\sum_qe_q^2x(q+\bar q)$, $F_1=\frac12\sum_qe_q^2(q+\bar q)$, $F_L=0$. Full (1 p). Check: free quark $F_2=e_q^2\delta(1-x)$ (VF-DIS-1). Remark: $F_L=0$ is a parton-model/LO statement ($F_L=O(\alpha_s)$, pointer `prop:disall-nlo`; M26).
  - `\uses{def:intro-factorization}`

* **注 `rem:intro-sharpness` — "每一阶、领头幂次"的精确含义与幂次的锐利性** (no tag) · new (refdoc S13.7, F3)
  - (a) The precise content of a perturbative factorization theorem: for IR-regulated partonic states, order by order in $\alpha_s$, the remainder after subtraction is bounded in integral norm, $\int|r|\le C\lambda^aL^K$, $L=\ln(1/\lambda)$, uniformly in $\varepsilon$ (E-N; pointer `def:method-power-suppressed`); nothing is claimed about summability. (b) Sharpness: the exponents $a$ delivered by the general method (e.g. $a=\beta_R/3$ on neighbourhoods of nested regions) can be far below the true power, while explicit examples give the true one; example (pointer only): for the one-loop off-shell triangle the general argument guarantees only relative errors $O(\lambda^{1/9})$ on the soft neighbourhood, while the exact Collins remainder is $-4m^2/Q^4+O(m^4Q^{-6}L^2)$, a full $\lambda^2$ with no logarithm at NLP (`prop:appN-triangle-exact`(c); VF-REF-3) [PENDING-VERIFY: N12]. (c) For hadrons the power $p$ of `def:intro-factorization`(c) is not fixed by the perturbative proofs (`asm:intro-bridge`).
  - `\uses{def:intro-factorization}`

* **定义 `def:intro-tags` — 严格性标签、限定语与等级传递** (no tag) · v1→rev. (refdoc S5, S13.1)
  - **陈述.** (1) The five tags of CONTEXT.md verbatim, with the rule "a tag refers to the statement exactly as formulated". (2) The four `[R]` qualifiers R_PT, R_def, R_OPE, R_cond with their verbatim sentences (WRITER_SPEC_v2 §4.3) and meaning; R_cond is always followed by the premise sentence 「前提：…」. (3) 「凡涉及强子的陈述，最多只能达到'有严格的微扰论内容 + 编号假设'的地位」: the tag of a hadron statement is its perturbative status; its non-perturbative status is the line 「非微扰地位：…」. (4) **Grade propagation** (order $[R]>[A]>[P]>[C]$, $[V]$ outside): a statement is never stronger than its weakest `\uses` premise (definitions, pure mathematics and the global assumptions excepted); R_cond implications are [R] as implications and carry a content grade equal to their weakest premise; process statements built from R_cond implications carry the weakest grade of the technical assumptions they use (example: `thm:dy-factorization` stays [A] because `asm:appN-collins`, `asm:appO-mixing` are [A]-level). (5) **Technical vs global assumptions** (Rule TA, §0.3 item 4 of this outline): technical assumptions are tagged by the status of their content as an all-order argument (\tagA when argued to all orders at the level of scaling statements, even if their integral-norm form is open); the six global non-perturbative assumptions `asm:intro-*` do not lower perturbative tags. (6) Composite statements: the first tag in the title, the other part as an item with its status in words. (7) Every [A]/[P]/[C]/[V] statement is followed by 「地位与缺口」; every statement carries a `\uses` line; App P is generated from these lines.
  - `% uses: none`

* **定义 `def:intro-error-types` — 误差类型** (no tag) · refdoc S7
  - **陈述.** E-S 标度陈述 (scaling statement; power counting of a region, no bound); E-P 逐点界 (pointwise bound on an integrand); E-F 纤维积分界 (bound after integrating one variable, pointwise in the rest); E-N 积分范数界 ($\int_A|F|d\mu\le C\lambda^aL^K$ uniformly in $\lambda\in(0,\lambda_0]$, $\varepsilon\in(0,\varepsilon_0]$); E-W 弱等价 (equality of integrals over the sets of a fixed algebra, with all subtraction-term weights). Rule: every status table has a column 「误差类型」, and every power-counting step of an [A]/[P] sketch names its type (「（此步只给出 E-S 型陈述）」). Remark: "power counting is a scaling statement, not a bound" — the gap between E-S and E-N is exactly the content of `asm:appN-envelope`, `asm:appN-separation` (pointers).
  - `\uses{def:intro-tags}`

* **注 `rem:intro-grade-dictionary` — 与文献中另一种分级的对照** (no tag) · refdoc S8
  - Introduced as 「文献中常见的另一种分级（按非微扰结构定理、CSS 标准的全阶证明等划分）」, **without citing or naming the reference document** (refdoc S62). Table: "A" (non-perturbative structure theorem conditional on QFT axioms + OPE) ↔ PT part [R, R_PT] or [R, R_OPE], non-perturbative part [R, R_cond] listing `asm:intro-*`; "A\*" ↔ [A] (quarkonium decay; non-perturbatively local duality [C]); "B" (all-order argument by the CSS standard) ↔ [A] for the process, implication [R, R_cond] (App N), bridge `asm:intro-bridge`; "B′" ↔ [A] + mandatory 「地位与缺口」 naming `asm:appO-*`; "C" ↔ split into [P] or [C]; "D" ↔ [V] + evidence type.
  - `\uses{def:intro-tags}`

* **假设 `asm:intro-wightman` — QCD 的 Wightman 结构** [C] · refdoc S6/S13 (corrected (W2), ERR-M25)
  - **陈述.** (W1) QCD with $n_f$ quark flavours of positive masses exists as a Wightman theory: a Hilbert space with positive metric, a strongly continuous unitary representation of the Poincaré group, a unique invariant vacuum $|0\rangle$, and local gauge-invariant composite fields — in particular the conserved hermitian electromagnetic current $j^\mu$ and the operators of `asm:intro-composite` — as operator-valued tempered distributions satisfying locality; parity is a symmetry. (W2) Spectral condition: the joint spectrum of $P^\mu$ lies in the closed forward cone; **in the superselection sector of the target's conserved flavour quantum numbers** the spectrum lies in $\{p^2\ge M^2,p^0>0\}$, $M$ the target mass, and for Haag–Ruelle one-particle states $M$ is an isolated eigenvalue of the mass operator in that sector (isolation is used only for the existence of the asymptotic target state). (W3) The connected forward matrix elements $\langle P|j^\mu(x)j^\nu(0)|P\rangle$ are tempered distributions in $x$. (W4) A covariant retarded extension $\tilde R^{\mu\nu}(q)$ of the commutator exists with $q_\mu\tilde R^{\mu\nu}=0$; its polynomial (contact-term) ambiguity affects only finitely many low Taylor coefficients $t_n$ of the forward amplitude. Massive light quarks are part of the assumption; the reconciliation with massless $\overline{\rm MS}$ coefficients is part of `asm:intro-af-coeff`.
  - **地位：** open — 4D QCD has not been constructed (the existence of 4D Yang–Mills with a mass gap is a Clay Millennium problem); widely assumed; (W2) as stated here corrects the spectral condition "nucleon isolated below the $N\pi$ continuum", which is false in the chiral limit and for $m_u\ne m_d$ (ERR-M25). **文献：** `Streater:1989vi`, `Jost:1965yxu`, `Haag:1958vt`; technical commentary (which axiom is used where) in App M §M.8 [SYNC-APP]. **被使用于：** `prop:ee-R-ImPi`, `prop:ee-analytic`, `prop:ee-smearing`, `prop:dis-W-structure`, `prop:dis-dispersion-np`, `thm:dis-moments-np`, `prop:pdf-support-hadron` and every hadron-level status line with MA0 [SYNC-ASM]. **解除途径：** construction of QCD (constructive field theory); in the meantime: lattice QCD as non-perturbative evidence (not proof).
  - `% uses: none`

* **假设 `asm:intro-composite` — 规范不变复合算符与光线算符的存在与重整化群** [C] · refdoc S6/S13
  - **陈述.** (C1) Gauge-invariant local composite operators exist as Wightman fields (in the sense of `asm:intro-wightman`) and are organized in finite families graded by mass dimension; after renormalization they obey RG equations with triangular mixing (an operator mixes only with operators of equal or lower dimension), with $\beta$ and anomalous-dimension matrices asymptotic to their perturbative series. (C2) The spin-$n$ twist-2 sector with non-zero spin-averaged forward matrix elements is spanned by the quark operators $O_q^{(n)}$ (one per flavour) and the gluon operator $O_g^{(n)}$ (even $n$) of the perturbative classification (forward pointers: `def:dis-twist`, `lem:dis-twist-classification`). (C3) The PDF light-ray operators (Wilson-line bilocals of `def:pdf-lightray`, forward pointer) exist between hadron states as tempered distributions in $w^-$, and their moments are the reduced matrix elements $A_i^{(n)}$ of the local twist-2 operators.
  - **地位：** open (presupposes `asm:intro-wightman`); in PT, (C1)–(C3) are theorems (`thm:prelim-composite-renorm`, `thm:pdf-moments-local`). **文献：** `Joglekar:1976eb`, `Joglekar:1976pe`, `Hollands:2007zg` (PT/pure YM). **被使用于：** `prop:pdf-support-hadron`, `thm:dis-moments-np`, `thm:pdf-moments-local` (hadron version), `thm:pdf-dglap` (hadron version) [SYNC-ASM]. **解除途径：** as for `asm:intro-wightman`.
  - `\uses{asm:intro-wightman}`

* **假设 `asm:intro-np-ope` — 非微扰算符乘积展开** [C] · refdoc S6/S13
  - **陈述.** (O1) For the T-product of two currents, the Euclidean OPE holds between the vacuum and between the hadron states of `asm:intro-wightman`, to every finite level $N$ in the operator dimension: $\tilde T^{\mu\nu}(q)-\sum_{d_j\le N}\tilde C^{\mu\nu}_j(q;\mu)\langle O_j\rangle=O(|q|^{2-N-\delta}\ln^k|q|)$, with remainder bounds uniform in the direction of $q$ and with bounds on all $q$-derivatives; the coefficients are Lorentz covariant. (O2) Odd-twist (chiral-odd) coefficients are suppressed by a light-quark mass ($\propto m_q/|q|$).
  - **地位：** open, widely assumed; its vacuum part is `conj:ee-np-ope` [C] (forward pointer); compatible with renormalons and instantons only as an asymptotic statement (`asm:intro-af-coeff`). **文献：** `Wilson1969`, `ShifmanVainshteinZakharov1979a`, `Novikov:1984rf`; AQFT approach `Bostelmann:2005rr`. **被使用于：** `lem:dis-ope-segment`, `thm:dis-fixed-n`, `thm:dis-moments-np`, the hadron versions of all R_OPE statements [SYNC-ASM]. **解除途径：** a non-perturbative definition of the OPE in QCD (Ch25 open problem OP-A3).
  - `\uses{asm:intro-wightman, asm:intro-composite}`

* **假设 `asm:intro-af-coeff` — 系数的渐近自由行为** [C] · refdoc S6/S13
  - **陈述.** At $\mu=|q|$ the OPE coefficients of `asm:intro-np-ope` are asymptotic to their $\overline{\rm MS}$ perturbative series: for every $K$, $\tilde C_i(q;|q|)=|q|^{2-d_i}\big[\sum_{k\le K}c_{i,k}(\hat q)\,\alpha_s(|q|)^k+O(\alpha_s(|q|)^{K+1})\big]$, with $c_{i,k}$ the perturbative coefficients (forward pointers `prop:dis-ope-euclid`, `prop:dis-c-oneloop`); light-quark-mass corrections are included as higher-dimension terms.
  - **地位：** open; compatible with IR renormalons and with instanton effects $e^{-2\pi/\alpha_s}=(\Lambda/Q)^{\beta_0}$ (both beyond every power of $\alpha_s$). **文献：** `Mueller1985`, `Beneke1999`. **被使用于：** `thm:dis-moments-np` [SYNC-ASM]. **解除途径：** as for `asm:intro-np-ope`.
  - `\uses{asm:intro-np-ope}`

* **假设 `asm:intro-growth` — 前向振幅的增长条件** [C] · refdoc S6/S13
  - **陈述.** For each fixed $Q^2$, the invariant forward Compton amplitude of a hadron target satisfies $\lim_{y\to\infty}T_2(iy,Q^2)/(iy)=0$ (normalization of `def:dis-compton`, forward pointer).
  - **地位：** open; holds at every computed fixed order in PT; it is **equivalent** to the validity of the low-moment sum rules (in particular the momentum sum rule) for the hadronic structure function and to the absence of a real fixed-pole term $c\,\omega$ (forward pointer `prop:dis-low-moments`); Regge behaviour of $F_2$ is neither necessary nor sufficient. **文献：** fixed poles: `conj:coll-bc` context (`BurkhardtCottingham1970`). **被使用于：** `prop:dis-low-moments`, `thm:dis-moments-np`, `thm:dis-moments` (moments $n<n_0$) [SYNC-ASM]. **解除途径：** a bound on the high-energy behaviour of the forward amplitude from first principles (Ch25 open problem OP-A4).
  - `\uses{asm:intro-wightman}`

* **假设 `asm:intro-bridge` — 从部分子微扰论到强子的桥接假设** [C] · refdoc S6/S13 (= MA1 + MA2, + MA4 asymptoticity)
  - **陈述.** (Br1) *Region completeness:* the leading-power regions found in PT for IR-regulated partonic states are the only leading-power regions in QCD with hadron states; confinement modifies only the IR-sensitive factors and creates no new leading region. (Br2) *Power-counting transfer:* all $\Lambda$-sensitivity of a hadronic cross section covered by a factorization theorem sits in the hadronic matrix elements of the same operators (PDFs, FFs, TMDs, DAs, soft factors) that appear in the partonic theorem. (Br3) *Asymptoticity:* the remainder is $O((\Lambda/Q)^p)$ for some $p>0$ as an asymptotic statement; perturbative series are asymptotic and renormalon ambiguities are of the order of power corrections, so "exact up to power corrections" has meaning only once the power-correction term is defined.
  - **地位：** open; supported by phenomenology, lattice consistency and renormalon analyses; the value of $p$ is not fixed by the perturbative proofs except for OPE-accessible quantities. **文献：** `CollinsSoperSterman1989`, `Collins2011` (ch. 14 discussion), `Beneke1999`. **被使用于：** every hadron-level factorization theorem of Ch5–Ch21 (non-perturbative status line) [SYNC-ASM]. **解除途径：** non-perturbative control of QCD (Ch25 open problem OP-A1).
  - `\uses{def:intro-factorization}`

* **定义 `def:intro-MA` — 元假设 MA0–MA4（总称）与编号假设的对应** (no tag) · v1→rev. (refdoc S6)
  - **陈述.** MA0 存在性 (⊃ `asm:intro-wightman`, `asm:intro-composite`); MA1 区域完备性 + MA2 幂次计数的传递 (= `asm:intro-bridge` (Br1)(Br2)); MA3 解析性与高能行为 (= analyticity, now a theorem under MA0: `prop:dis-dispersion-np`, + the genuine growth assumption `asm:intro-growth`); MA4 渐近性 (⊃ `asm:intro-af-coeff`, `asm:intro-bridge` (Br3)). Each umbrella in ≤ 3 lines, then: 「本书每个涉及强子的陈述在前提之后列出它用到的编号假设（括号中注明 MA 总称）。」 Text of critic §12 (Chinese, ready) adapted.
  - `\uses{asm:intro-wightman, asm:intro-composite, asm:intro-np-ope, asm:intro-af-coeff, asm:intro-growth, asm:intro-bridge}`

**Tables.**
- `tab:intro-kinds` — columns 名称 | 尺度 | 低能函数 | 演化变量 | 典型证明技术 | 地位 | 本书章节; rows: collinear (DIS/DY), TMD, threshold, high-energy ($k_T$), exclusive (DA/GPD), heavy-quark (NRQCD/HQE/QCDF), SCET matching, **LaMET / short-distance factorization (quasi-/pseudo-PDF)**, **quasi-TMD (Euclidean soft functions)**.
- `tab:intro-assumptions` — the short register (refdoc S13.6): label | one-line content | status tag | used by; the 25 entries of refdoc §5.3 plus the frontier entries `asm:lamet-*`, `asm:yzliu-*`, `asm:front-*` [SYNC-ASM][SYNC-FRONTIER]. Generated from the assumption environments (the long version is `tab:appP-register`).
- `tab:intro-overview` — the rows of `tab:summary-master` marked ★ (§25 of this outline), columns 结论 | 公式/要点 | 标签 | 非微扰地位 | 规范标签. Tags must coincide with Ch25 and with the statements (script check, WRITER_SPEC_v2 §10).

**Misconception box (14 items; each with the correction and a forward reference).** M28 ([R] ≠ proven for real-world QCD) → `def:intro-tags`; M1 (factorization proven for all processes) → `tab:intro-overview`, Ch18; M2 (MS-bar PDFs are probabilities) → `conj:pdf-positivity`; M3 (factorization = OPE) → Ch7, Ch12; M4 (moments ⇒ uniform $x$-space error) → `rem:dis-nonuniform`, `cor:dis-weak-xspace`; M7 (Glauber always cancels) → Ch12, Ch18 (`prop:break-measurement`); M8 (KLN explains hadron-collider finiteness) → `prop:ir-bn-failure`; M9 (IR safety ⇒ factorization) → Ch16; M10 (power corrections always $\Lambda^2/Q^2$) → Ch21; M15 (soft factor always 1) → `lem:method-soft-unitarity`, Ch14; M18 (SCET independent of regions) → `rem:scet-assumptions`; M24 (DR partonic PDF is "nothing") → `prop:pdf-partonic-dr`; **M32** (the non-abelian two-Glauber exchange leaves a non-unitary residual) → `prop:dy-eikonal-twogluon`; **M35** (the subtraction theorem can be proved term by term by induction) → `ex:method-naive-induction`.

**Figures.** Existing (tikz1): `fig:parton-model`, `fig:handbag`, `fig:factorization-schematic` (its caption points to `fig:pdf-operator`, Ch8 — pointer only). New: `fig:intro-dependency` (FIGURES_INDEX_v2 §2 item 1, updated for v2: columns tools (Ch2–Ch3) / IR (Ch4–Ch5) / rigorous core (Ch6–Ch8) / machine (Ch9 + App N, O) / processes (Ch10–Ch15) / boundaries (Ch18) / frontier (Ch22–Ch24); assumption nodes; R_cond nodes dashed).

**Key citation keys.** `Feynman1969`, `Bjorken1969`, `BjorkenPaschos1969`, `DrellYan1970`, `CollinsSoperSterman1989`, `CollinsSoper1987`, `Collins2011`, `Sterman1993`, `StermanEtAl1995`, `CollinsSoper1982a`, `CandidoForteHekhorn2020`, `CollinsRogersSato2022`, `DoriaFrenkelTaylor1980`, `DiLietoEtAl1981`, `CollinsQiu2007`, `RogersMulders2010`, `CataniDeFlorianRodrigo2012`, `Beneke1999`, `Hollands:2011gf`, `tHooft1974`, `IzubuchiEtAl2018`, `Ji2013`, `JiEtAl2021`, `Ji:2019ewn`, `Liu:2022nnk`, `Streater:1989vi`, `Jost:1965yxu`, `Haag:1958vt`, `Bostelmann:2005rr`, `Mueller1985`, `Novikov:1984rf`, `ShifmanVainshteinZakharov1979a`, `Wilson1969`, `BurkhardtCottingham1970`, `Collins:2020euz`.

**Pending.** `rem:intro-sharpness`(b) [PENDING-VERIFY: N12]; `tab:intro-assumptions` frontier rows [SYNC-ASM][SYNC-FRONTIER]; the ★ rows of `tab:intro-overview` follow Ch25 after the verify patch.

---------------------------------------------------------------------------------------------------

## Chapter 2 — QCD 基础——从规范不变性到渐近自由 / QCD basics: from gauge invariance to asymptotic freedom

`\label{ch:qcd}` · `ch02_qcd.tex` · **18 pp** · **pedagogical** (WRITER_SPEC_v2 §7: ≈40 % motivation and explanation, 35 % definitions, statements and proofs, 25 % worked examples) · Part I · **new chapter** (REQUIREMENTS 3e)

**Purpose.** Start the book, like the Furry monograph (`furry_qcd.tex` §2), from the basics and move gradually to the deep material: (i) why QCD is an SU(3) gauge theory; (ii) the gauge principle from QED to SU($N$), the Lagrangian and its gauge invariance; (iii) quantization by gauge fixing and Faddeev–Popov ghosts, Feynman rules derived (not postulated) with every sign checked; (iv) BRST symmetry, nilpotency, the physical state space; (v) UV divergences, dimensional regularization, renormalization, renormalizability, Slavnov–Taylor identities, gauge-parameter independence, $\overline{\rm MS}$, composite operators; (vi) the one-loop renormalization constants and $\beta_0$ computed in four Slavnov–Taylor-equivalent ways; (vii) the renormalization group, the running coupling with numbers, asymptotic freedom; (viii) infrared divergences and IR safety at an introductory level, as the bridge to Part I's later chapters. Every basic fact gets a canonical statement with an **honest grade**: algebraic facts [R, R_def]; perturbative facts [R, R_PT] (with "proof sketch + source of the complete proof" where the complete proof is long, WRITER_SPEC_v2 §4.10); formal path-integral manipulations are remarks without tag; non-perturbative existence is `asm:intro-wightman` [C]. The rigour vocabulary (tags, `\uses`) is used from the start; the first section explains it in plain words with a pointer back to `def:intro-tags`.

**Depends on.** Ch1 (`def:intro-tags`, `asm:intro-wightman` as pointers for the status of non-perturbative existence). Moved v1 labels (§0.4): `def:prelim-qcd`, `def:prelim-feynman-rules`, `def:prelim-brst`, `lem:prelim-brst-nilpotent`, `thm:prelim-slavnov-taylor`, `def:prelim-msbar`, `prop:prelim-beta`, `prop:prelim-rg`, `thm:prelim-composite-renorm`; section labels `sec:prelim-qcd`, `sec:prelim-brst`, `sec:prelim-renorm`. VF: VF-QCD-1…9, VF-CONV-2/3/4/5, VF-PDF-14, VF-WL-5, VF-WL-9, VF-EE-4/5/6/11/12. Inter-unit ownership (WRITER_SPEC_v2 §12.2): Ch2 owns the QCD Lagrangian, gauge invariance, Faddeev–Popov, BRST, Feynman rules, renormalization, $\overline{\rm MS}$, RG, running coupling, asymptotic freedom, and the *introductory* IR material; Ch3 owns the DR technical conventions (ε_UV/ε_IR, scaleless integrals, CDR traces); Ch4 owns `def:ir-safe`, KLN, Bloch–Nordsieck; Ch6 owns the complete $e^+e^-$ computation; App J holds the BRST proofs.

**Box (「本章给出完整推导的／本章只陈述、留待后文或文献的」).**
- 本章给出完整推导的：`thm:qcd-gauge-invariance`（[R, R_def]）；`prop:qcd-covariance`（[R, R_def]）；`lem:prelim-brst-nilpotent`（[R, R_def]，细节见附录 J）；`prop:qcd-brst-cohomology`（[R, R_def]）；`prop:qcd-superficial-degree`（[R, R_def]）；单圈 $Z$ 因子与 $\beta_0$（`ex:qcd-gluon-self-energy`、`ex:qcd-quark-self-energy-vertex`、`ex:qcd-beta0-four-ways`，`prop:prelim-beta` 的 $\beta_0$ 部分 [R, R_PT]）；`prop:qcd-rge`（[R, R_PT]，以可重整性为前提的完整推导）；`prop:prelim-rg`（[R, R_PT]）；`thm:qcd-asymptotic-freedom`（[R, R_PT]）；`prop:qcd-soft-collinear-limits`（[R, R_PT]，树图）。
- 本章只陈述、留待后文或文献的：`thm:qcd-renormalizability`、`lem:qcd-st-regularized`、`prop:qcd-st-relations`（全阶部分）、`thm:prelim-slavnov-taylor`、`prop:qcd-xi-independence`、`thm:prelim-composite-renorm`（[R, R_PT]，证明概要 + 完整证明的文献）；$\beta_1,\beta_2$（文献值）；红外定理（第~4~章：`thm:ir-bn-qed`、`thm:ir-kln`、`prop:ir-bn-failure`、`thm:ir-safe-finite`）；QCD 的非微扰存在性（`asm:intro-wightman`，[C]）；Gribov 复本、禁闭（不在本书范围）。

**Sections** (reading order; the three moved labels are canonical).
1. `sec:qcd-why` 为什么是 SU(3) 规范理论 (≈1.5 pp) — quark model (`Gell-Mann:1964ewy`, `Zweig:1964jf`); colour from statistics ($\Delta^{++}$, `Greenberg:1964pe`, `Han:1965pf`) and from $R=N_c\sum e_q^2$ (forward pointer `cor:ee-R-alphas`); Bjorken scaling and the need for a theory that is weak at short distances (forward pointer Ch7; `Coleman:1973sx`: only non-abelian gauge theories are asymptotically free); colour octet gluons (`Fritzsch:1973pi`); what is and is not proven about QCD (perturbation theory vs `asm:intro-wightman`); how to read the tags in this chapter (plain words + pointer `def:intro-tags`).
2. `sec:qcd-gauge` 规范原理：从 QED 到 SU($N$) (≈2.5 pp) — local phase invariance in QED and the covariant derivative; non-abelian generalization (`Yang:1954ek`); Lie algebra, representations, Casimirs, Fierz identity; covariant derivative and field strength; infinitesimal transformations; Bianchi identity.
3. `sec:prelim-qcd` QCD 拉氏量及其规范不变性 (≈1.5 pp) — the Lagrangian; gauge invariance and uniqueness of the renormalizable Lagrangian; $\theta$ term.
4. `sec:qcd-quantization` 量子化：规范固定、Faddeev–Popov 鬼场与 Feynman 规则 (≈2.5 pp) — why the gluon propagator needs gauge fixing; the Faddeev–Popov construction (formal) and the gauge-fixed Lagrangian; Feynman rules derived from it (as in the Furry monograph: vertex = $i\times$ coefficient, all field assignments summed); light-cone gauge mentioned only as a heuristic (proofs in Feynman gauge, Collins 2011 §12.6); the tree-level $q\bar q\to gg$ example showing why ghosts are needed.
5. `sec:qcd-regularization` 紫外发散与维数正规化 (≈1 p) — superficial degree of divergence; DR definition (technical conventions in Ch3).
6. `sec:prelim-brst` BRST 对称性与物理态 (≈2 pp) — BRST transformations, nilpotency, BRST-exactness of the gauge-fixing sector, the free asymptotic state space and the quartet mechanism, Slavnov–Taylor identities of the regularized theory.
7. `sec:prelim-renorm` 重整化：可重整性、Slavnov–Taylor 恒等式与 $\overline{\rm MS}$ (≈2.5 pp) — renormalization constants, $\overline{\rm MS}$, renormalizability, Slavnov–Taylor relations among $Z$'s, the renormalized ST identity in the form used for factorization, gauge-parameter independence, composite operators, BPHZ vs DR.
8. `sec:qcd-renorm` 单圈重整化：真空极化、$Z$ 因子与 $\beta_0$ (≈2 pp) — the one-loop gluon self-energy (`fig:qcd-vacuum-polarization`), quark self-energy and vertex, $\beta_0$ four ways, the $\beta$ function.
9. `sec:qcd-running` 重整化群方程与跑动耦合 (≈1.5 pp) — RGE; RG improvement; $\Lambda_{\overline{\rm MS}}$; numbers (`fig:qcd-running-coupling`); decoupling.
10. `sec:qcd-af` 渐近自由 (≈1 p) — theorem; screening vs antiscreening (`fig:qcd-antiscreening`); what AF does and does not imply.
11. `sec:qcd-ir` 红外发散与红外安全（入门） (≈1.5 pp) — soft and collinear limits at tree level; IR divergences of exclusive quantities; real–virtual cancellation; IR safety (informal); Sterman–Weinberg; preview of the IR theorems of Ch4 (`fig:qcd-ir-safety`).
12. `sec:qcd-summary` 本章小结、记号速查与后文用途 (≈0.5 p) — 「本章小结」; `tab:qcd-symbols` 记号速查; 「这些工具在后文的用途」 (WRITER_SPEC_v2 §7 items 2, 7).

**Canonical statements** (in reading order).

* **定义 `def:qcd-gauge-group` — 规范群 SU($N$) 及其表示** (no tag) · new
  - **陈述.** Gauge group SU($N$), $N\ge2$ (physical $N=3$). Fundamental generators $t^a$ ($a=1,\dots,N^2-1$): hermitian, traceless, $[t^a,t^b]=if^{abc}t^c$, ${\rm Tr}(t^at^b)=T_F\delta^{ab}$, $T_F=\frac12$; $d^{abc}=2{\rm Tr}(\{t^a,t^b\}t^c)$; adjoint generators $(F^a)_{bc}=-if^{abc}$; Casimirs $t^at^a=C_F\mathbb 1$, $C_F=\frac{N^2-1}{2N}$, $f^{acd}f^{bcd}=C_A\delta^{ab}$, $C_A=N$; SU(3): $t^a=\lambda^a/2$, $C_F=\frac43$, $C_A=3$; $n_f$ quark flavours in the fundamental representation (VF-QCD-1; WRITER_SPEC_v2 §3 rows 4, 47).
  - `% uses: none`

* **引理 `lem:qcd-colour-identities` — 色代数恒等式** (数学，无标签) · new
  - **陈述.** (i) Fierz: $t^a_{ij}t^a_{kl}=\frac12(\delta_{il}\delta_{kj}-\frac1N\delta_{ij}\delta_{kl})$; (ii) $t^at^a=C_F\mathbb 1$, $f^{acd}f^{bcd}=C_A\delta^{ab}$; (iii) $t^bt^at^b=(C_F-\frac{C_A}2)t^a=-\frac1{2N}t^a$; (iv) ${\rm Tr}(t^at^bt^c)=\frac14(d^{abc}+if^{abc})$; (v) Jacobi $f^{abe}f^{ecd}+f^{bce}f^{ead}+f^{cae}f^{ebd}=0$, equivalently $[F^a,F^b]=if^{abc}F^c$; (vi) $if^{abc}t^bt^c=-\frac{C_A}2t^a$.
  - **证明.** Full: (i) completeness of $\{\mathbb 1/\sqrt{2N},t^a\}$ in the space of $N\times N$ matrices; (ii)–(iv), (vi) from (i) and the commutator; (v) from the associativity of the matrix product. Explicit SU(2)/SU(3) checks: VF-QCD-1 (v2-check Q1a–f).
  - `\uses{def:qcd-gauge-group}`

* **例 `ex:qcd-colour-algebra` — 单圈图的色因子与双线记号** (no tag) · new
  - Colour factors of the one-loop graphs used later: quark self-energy $C_F$; quark loop in the gluon self-energy $T_Fn_f\delta^{ab}$; gluon and ghost loops $C_A\delta^{ab}$; quark–gluon vertex correction with the gluon between the quark legs $(C_F-\frac{C_A}2)t^a$ and with the three-gluon vertex $\frac{C_A}2t^a$; double-line ('t Hooft) notation and the $1/N$ term of the Fierz identity (optional `fig:qcd-colour-flow`). All from VF-QCD-1.
  - `\uses{lem:qcd-colour-identities}`

* **命题 `prop:qcd-covariance` — 协变导数与场强的规范协变性** [R, R_def] · new
  - **陈述.** With $D_\mu=\partial_\mu-igA_\mu$, $A_\mu=A^a_\mu t^a$ and $G_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu-ig[A_\mu,A_\nu]$: (a) under $\psi\to U\psi$, $A_\mu\to UA_\mu U^{-1}-\frac ig(\partial_\mu U)U^{-1}$ ($U(x)\in$ SU($N$) smooth): $D_\mu\psi\to UD_\mu\psi$ and $G_{\mu\nu}\to UG_{\mu\nu}U^{-1}$; (b) $[D_\mu,D_\nu]=-igG_{\mu\nu}$ and $G^a_{\mu\nu}=\partial_\mu A^a_\nu-\partial_\nu A^a_\mu+gf^{abc}A^b_\mu A^c_\nu$; (c) for $U=1+i\theta^at^a$: $\delta\psi=i\theta^at^a\psi$, $\delta A^a_\mu=\frac1g(D_\mu\theta)^a$ with the adjoint covariant derivative $(D_\mu X)^a=\partial_\mu X^a+gf^{abc}A^b_\mu X^c$; (d) Bianchi identity $[D_\lambda,G_{\mu\nu}]+[D_\mu,G_{\nu\lambda}]+[D_\nu,G_{\lambda\mu}]=0$.
  - **证明.** Full (one page; the matrix identity $U\partial_\mu U^{-1}=-(\partial_\mu U)U^{-1}$; (d) from the Jacobi identity of commutators). Checks: VF-QCD-2 (v2-check Q1g, Q2). (本命题是算符恒等式，不涉及强子态。)
  - `\uses{def:qcd-gauge-group, lem:qcd-colour-identities}`

* **定义 `def:prelim-qcd` — QCD 拉氏量与规范变换** (no tag) · v1 (moved to Ch2; label unchanged)
  - **陈述.** VF-CONV-2: $\mathcal L=-\frac14G^a_{\mu\nu}G^{a\mu\nu}+\sum_q\bar\psi_q(i\slashed D-m_q)\psi_q-\frac1{2\xi_g}(\partial\cdot A^a)^2+\bar c^a(-\partial^\mu D^{ac}_\mu)c^c$, $D_\mu=\partial_\mu-igA^a_\mu t^a$, $(D_\mu X)^a=\partial_\mu X^a+gf^{abc}A^b_\mu X^c$; $\psi\to U\psi$, $A_\mu\to UA_\mu U^{-1}-\frac ig(\partial_\mu U)U^{-1}$. The first two terms form the classical Lagrangian $\mathcal L_{\rm cl}$; the last two (gauge fixing, ghosts) are explained in `sec:qcd-quantization` (forward pointer `def:qcd-fp`, which restates them with their origin). Conventions: WRITER_SPEC_v2 §3 row 4 (Collins, BBL and the LaMET/Liu papers use $g\to-g$).
  - `\uses{def:qcd-gauge-group}`

* **定理 `thm:qcd-gauge-invariance` — 经典 QCD 拉氏量的规范不变性与唯一性** [R, R_def] · new
  - **陈述.** (a) $\mathcal L_{\rm cl}=-\frac14G^aG^a+\sum_q\bar\psi_q(i\slashed D-m_q)\psi_q$ is invariant under all local SU($N$) gauge transformations of `def:prelim-qcd` (finite $U(x)$, not only infinitesimal). The term $G^a_{\mu\nu}\tilde G^{a\mu\nu}$ ($\tilde G^{a\mu\nu}=\frac12\epsilon^{\mu\nu\rho\sigma}G^a_{\rho\sigma}$) is gauge invariant and a total derivative, $G\tilde G=\partial_\mu J^\mu_{\rm CS}$. (b) Every Lorentz-invariant, gauge-invariant local polynomial in $A^a_\mu$, $\psi_q$, $\bar\psi_q$ and their derivatives with mass dimension $\le4$ (no other fields) is a linear combination of $G^a_{\mu\nu}G^{a\mu\nu}$, $G^a_{\mu\nu}\tilde G^{a\mu\nu}$, $\bar\psi_qi\slashed D\psi_{q'}$, $\bar\psi_q\gamma_5i\slashed D\psi_{q'}$, $\bar\psi_q\psi_{q'}$, $\bar\psi_qi\gamma_5\psi_{q'}$ (flavour matrices; the operator $1$ excluded). After flavour rotations the kinetic terms are canonical and the mass matrix is diagonal with real non-negative entries, up to the interplay of its overall phase with $\theta$ (axial anomaly; not used in this book).
  - **证明.** (a) Full (from `prop:qcd-covariance`; the trace cyclicity for $G^aG^a=2{\rm Tr}G_{\mu\nu}G^{\mu\nu}$; Chern–Simons current as in the Furry monograph). (b) Sketch: gauge invariance forces $A$ to appear only through $D_\mu$ and $G_{\mu\nu}$ (Lorentz-covariant gauge-covariant building blocks); enumerate monomials of dimension $\le4$; total-derivative relations among them; cite `Weinberg1996` ch. 15（节号待核实） and `PeskinSchroeder1995` ch. 15. (本定理是关于场的代数陈述。)
  - `\uses{def:prelim-qcd, prop:qcd-covariance}`

* **注 `rem:qcd-theta` — $\theta$ 项** (no tag) · new
  - $\mathcal L_\theta=\frac{\theta g^2}{32\pi^2}G\tilde G$ is a total derivative, hence contributes to no order of perturbation theory (vertices proportional to the total momentum); it violates P and T, preserves C; the strong CP problem and instantons are outside the scope (instanton effects $\propto e^{-8\pi^2/g^2}$ appear again in `asm:intro-af-coeff`). Source: `furry_qcd.tex` (θ-term paragraph) re-derived; `PeskinSchroeder1995` §19.

* **注 `rem:qcd-fp-derivation` — Faddeev–Popov 构造（形式推导）** (no tag) · new
  - The quadratic form of $A$ in $\mathcal L_{\rm cl}$, $-k^2g^{\mu\nu}+k^\mu k^\nu$, has the zero mode $k^\mu$ (gauge orbits), so no propagator exists without gauge fixing. Formal derivation: insert $1=\Delta_{\rm FP}[A]\int\mathcal DU\,\delta(F(A^U)-\omega)$, average over $\omega$ with a Gaussian weight, $\Delta_{\rm FP}=\det(\delta F(A^U)/\delta\theta)$, exponentiate with Grassmann ghosts. **Formal**: the path integral is not defined; within perturbation theory the result is taken as the *definition* `def:qcd-fp`, whose consistency is then established by BRST (`thm:qcd-renormalizability`, `prop:qcd-xi-independence`). Non-perturbatively the gauge-fixing surface meets orbits more than once (Gribov copies; 「（文献待补：Gribov 1978, Nucl. Phys. B 139, 1）」), irrelevant at every order of PT (optional `fig:qcd-gauge-orbit`). Sources: `Faddeev:1967fc`; `PeskinSchroeder1995` §16.2; `Weinberg1996` ch. 15（节号待核实）.

* **定义 `def:qcd-fp` — 协变规范、Faddeev–Popov 鬼场与微扰 QCD** (no tag) · new
  - **陈述.** (a) Covariant gauge fixing with parameter $\xi_g$ (Feynman $\xi_g=1$; Landau $\xi_g\to0$ as a limit): $\mathcal L_{\rm gf}=-\frac1{2\xi_g}(\partial^\mu A^a_\mu)^2$, equivalently $\mathcal L_{\rm gf}=B^a\partial^\mu A^a_\mu+\frac{\xi_g}2B^aB^a$ with the auxiliary Nakanishi–Lautrup field $B^a$ (eliminating $B^a=-\partial\cdot A^a/\xi_g$ returns the first form). (b) Ghost Lagrangian $\mathcal L_{\rm FP}=\bar c^a(-\partial^\mu D^{ac}_\mu)c^c$, equal to $(\partial^\mu\bar c^a)(D_\mu c)^a$ up to a total derivative; $c^a,\bar c^a$ independent Grassmann-odd scalars in the adjoint representation (VF-QCD-3). (c) **Perturbative QCD** is the formal power series in $g$ of the Green functions generated by $\mathcal L=\mathcal L_{\rm cl}+\mathcal L_{\rm gf}+\mathcal L_{\rm FP}$ (= `def:prelim-qcd`), regularized and renormalized as in `sec:prelim-renorm`; light-cone and other axial gauges are used in this book only for heuristics (`rem:pdf-number-density`, forward pointer).
  - `\uses{def:prelim-qcd}`

* **例 `ex:qcd-fp-lowest-order` — 由拉氏量导出传播子、鬼场顶点与闭合鬼圈因子** (no tag) · new
  - (a) The gluon quadratic form $-k^2g^{\mu\nu}+(1-\xi_g^{-1})k^\mu k^\nu$ and its inverse times $i$: $\frac{-i}{k^2+i0}[g^{\mu\nu}-(1-\xi_g)\frac{k^\mu k^\nu}{k^2}]$; (b) ghost propagator $\frac{i\delta^{ab}}{p^2+i0}$ and the ghost–gluon vertex $-gf^{abc}p^\mu$ ($p$ = momentum of the outgoing ghost) obtained exactly as in the Furry monograph (derivative acting on $\bar c$, $\partial^\mu\to+ip^\mu$); (c) the factor $-1$ for each closed ghost loop (Grassmann). VF-CONV-3, VF-QCD-3.
  - `\uses{def:qcd-fp}`

* **定义 `def:prelim-feynman-rules` — Feynman 规则** (no tag) · v1 (moved; label unchanged)
  - **陈述.** VF-CONV-3 (table + `fig:prelim-feynman-rules`): quark, gluon (covariant gauge), ghost propagators; $ig\gamma^\mu t^a$; three-gluon $gf^{abc}[g^{\mu\nu}(k-p)^\rho+g^{\nu\rho}(p-q)^\mu+g^{\rho\mu}(q-k)^\nu]$, all momenta incoming; ghost vertex $-gf^{abc}p^\mu$, $p$ the outgoing-ghost momentum; four-gluon vertex as in Peskin–Schroeder ch. 16. Derivation: vertex = $i\times$ coefficient of the monomial, summed over all assignments of external legs ($3!$, $4!$ for the gluon self-couplings), $\partial_\mu\to-ip_\mu$ on incoming plane waves. Checked by c_pdf (plane waves) and c_wilson (Ward identities fail with the opposite sign; $q\bar q\to gg$ cross section).
  - `\uses{def:prelim-qcd, def:qcd-fp}`

* **例 `ex:qcd-qqbar-gg` — 树图 $q\bar q\to gg$：为什么需要鬼场** (no tag) · new (content of v1 `prop:prelim-unitarity`'s example, moved here)
  - $s$-, $t$-, $u$-channel graphs; $k_{1\mu}\mathcal M^{\mu\nu}_{ab}\ne0$ when the other gluon is not physically polarized (non-abelian term $\propto f^{abc}$); $\sum_{\rm phys}|\mathcal M|^2=\sum_{-g,-g}|\mathcal M|^2-2\sum|\mathcal M_{\rm gh}|^2$; spin- and colour-averaged $\frac1{36}\sum_{\rm phys}|\mathcal M|^2=g^4[\frac{32}{27}\frac{t^2+u^2}{tu}-\frac83\frac{t^2+u^2}{s^2}]$ (VF-WL-9; `CombridgeKripfganzRanft1977`). The general reason is the quartet mechanism (`prop:qcd-brst-cohomology`) and physical unitarity of cut diagrams (`prop:prelim-unitarity`, Ch3) — pointers.
  - `\uses{def:prelim-feynman-rules}`

* **定义 `def:qcd-dimreg` — 维数正规化** (no tag) · new
  - **陈述.** Loop integrals in $D=4-2\varepsilon$ dimensions, defined by analytic continuation in $D$ (master formula $\int\frac{d^Dk}{i\pi^{D/2}}\frac1{(-k^2+\Delta-i0)^a}=\frac{\Gamma(a-D/2)}{\Gamma(a)}\Delta^{D/2-a}$; App C); conventional DR (CDR: $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}$, $g^\mu{}_\mu=D$, ${\rm Tr}\,\mathbb 1=4$); the bare coupling has mass dimension $\varepsilon$: $g_0=\mu_0^\varepsilon\hat g_0$ (WRITER_SPEC_v2 §3 row 6). DR preserves gauge and BRST invariance in vector-like theories (no $\gamma_5$); $\gamma_5$ (HVBM + Larin) in `def:prelim-gamma5` and App I (forward pointers). The technical conventions ($\varepsilon_{\rm UV}$ vs $\varepsilon_{\rm IR}$, scaleless integrals, polarization averages) are owned by Ch3 (`def:prelim-dr-conventions`, forward pointer).
  - `% uses: none`

* **命题 `prop:qcd-superficial-degree` — 紫外超表观发散度** [R, R_def] · new
  - **陈述.** For a 1PI graph of QCD in $D=4$ with $E_A$ external gluons, $E_c$ external ghost lines and $E_\psi$ external quark lines, $\omega=4-E_A-E_c-\frac32E_\psi$, independent of the number of loops. Hence the superficially divergent 1PI functions are the gluon, ghost and quark two-point functions and the three-gluon, four-gluon, ghost–gluon and quark–gluon vertices ($\omega=2,2,1,1,0,1,0$), the derivative coupling of the ghost lowering the actual degree of the ghost two-point and ghost–gluon functions by one unit per external ghost momentum.
  - **证明.** Full (count $\omega=4L-2I_A-2I_c-I_\psi+V_3+V_{c}$ with the topological relations; one paragraph). (本命题是关于 Feynman 图的组合陈述。)
  - `\uses{def:prelim-feynman-rules}`

* **定义 `def:prelim-brst` — BRST 变换** (no tag) · v1 (moved; label unchanged)
  - **陈述.** $sA^a_\mu=D^{ab}_\mu c^b$, $s\psi=igc^at^a\psi$, $sc^a=-\frac g2f^{abc}c^bc^c$, $s\bar c^a=B^a$, $sB^a=0$ ($s$ a Grassmann-odd derivation acting from the left). Signs re-derived by the writer against `PeskinSchroeder1995` §16.4 in our convention $D=\partial-igA$ (c_wilson §5.6 warns).
  - `\uses{def:qcd-fp}`

* **引理 `lem:prelim-brst-nilpotent` — $s^2=0$ 与拉氏量的 BRST 不变性** [R, R_def] · v1 (moved; extended)
  - **陈述.** (a) $s^2=0$ on $A$, $\psi$, $c$, $\bar c$, $B$; (b) $s\mathcal L_{\rm cl}=0$ (a gauge transformation with parameter $\propto c$); (c) $\mathcal L_{\rm gf}+\mathcal L_{\rm FP}=s\Psi$ with the gauge fermion $\Psi=\bar c^a(\partial\cdot A^a+\frac{\xi_g}2B^a)$ (using $s(\bar cX)=(s\bar c)X-\bar c\,(sX)$), hence $s\mathcal L=0$ up to a total derivative.
  - **证明.** Full; the Jacobi identity for $s^2c=0$ and $s^2A=0$; details in App J (`sec:appJ-brst`).
  - `\uses{def:prelim-brst, def:prelim-qcd, def:qcd-fp, lem:qcd-colour-identities, prop:qcd-covariance}`

* **命题 `prop:qcd-brst-cohomology` — 自由渐近 Fock 空间上的 BRST 上同调（Kugo–Ojima 四重态）** [R, R_def] · new
  - **陈述.** For the free ($g=0$) theory in covariant gauge, let $Q$ be the BRST charge on the indefinite-metric Fock space of gluons (four polarizations), ghosts, antighosts, $B$ and quarks. Then (a) $Q^2=0$; (b) at ghost number zero, $\ker Q/{\rm im}\,Q$ is isomorphic to the Fock space of quarks and transversely polarized gluons; (c) the inner product is positive semi-definite on $\ker Q$ and vanishes on ${\rm im}\,Q$, so $\ker Q/{\rm im}\,Q$ is a positive-metric Hilbert space; (d) the unphysical modes (for each light-like $k$: the scalar/longitudinal gluon combinations, $c$, $\bar c$, $B$) form BRST quartets, which contribute zero norm.
  - **证明.** Full for a single momentum mode (`ex:qcd-brst-quartet`), then by tensor products (Künneth); `KugoOjima1979` (§3 and §4, 位置待核实). Remark (print): in the interacting theory the same structure for the asymptotic states, together with the Slavnov–Taylor identities, gives the unitarity of the physical S-matrix order by order — the cut-diagram form of this statement is `prop:prelim-unitarity` (Ch3, pointer). (本命题是关于自由场 Fock 空间的代数陈述。)
  - `\uses{def:prelim-brst, def:qcd-fp, lem:prelim-brst-nilpotent}`

* **例 `ex:qcd-brst-quartet` — 单一动量模式的四重态** (no tag) · new
  - For light-like $k$ with the light-like partner $\bar k$ ($k\cdot\bar k\ne0$): the gluon modes along $k$ and $\bar k$, the ghost, antighost and $B$ modes; $Q$ maps the $\bar k$-polarized gluon to the ghost (up to normalization) and the antighost to $B$; Gram matrix of the quartet; zero norm of every state containing quartet modes in $\ker Q$. Ties back to `ex:qcd-qqbar-gg` ($-g_{\mu\nu}$ sum minus ghosts = transverse sum).
  - `\uses{prop:qcd-brst-cohomology, ex:qcd-qqbar-gg}`

* **引理 `lem:qcd-st-regularized` — 维数正规化理论的 Slavnov–Taylor 恒等式** [R, R_PT] · new
  - **陈述.** In dimensionally regularized perturbative QCD (vector-like; no $\gamma_5$), at every order in $g$ and as identities of meromorphic functions of $\varepsilon$: for every product $X$ of elementary fields, $\langle0|T\,(sX)|0\rangle=0$ (Slavnov–Taylor identities); equivalently the generating functional of 1PI functions with BRST sources satisfies the Zinn-Justin (master) equation. In particular the gluon self-energy is transverse, and the vertex functions obey the relations that imply `prop:qcd-st-relations`.
  - **证明.** Sketch: BRST invariance of $\mathcal L$ (`lem:prelim-brst-nilpotent`) and of the DR "measure" (the identities are algebraic identities of the integrands in $D$ dimensions); Schwinger–Dyson/source argument. Sources: `Taylor1971`, `Slavnov1972`, `BecchiRouetStora1976`, `KugoOjima1979`, `Collins1984` ch. 12（位置待核实）; the Zinn-Justin equation 「（文献待补：J. Zinn-Justin 1975, Lect. Notes Phys. 37）」. (本引理只涉及正规化的 Green 函数。)
  - `\uses{def:qcd-dimreg, lem:prelim-brst-nilpotent, def:prelim-feynman-rules}`

* **定义 `def:qcd-renormalization` — 重整化常数与抵消项** (no tag) · new
  - **陈述.** Bare and renormalized quantities: $\psi_0=Z_2^{1/2}\psi$, $A_0=Z_3^{1/2}A$, $c_0=\tilde Z_3^{1/2}c$, $m_0=Z_mm$, $\xi_{g,0}=Z_3\xi_g$; the vertex constants $Z_{1F}$ (quark–gluon), $\tilde Z_1$ (ghost–gluon), $Z_1$ (three-gluon), $Z_4$ (four-gluon) are defined as the independent multiplicative renormalizations of the four vertices; the coupling constant renormalization $Z_g$ is **defined** by the quark–gluon vertex, $g_0=\mu^\varepsilon Z_gg\times(\text{scheme factor of `def:prelim-msbar`})$, $Z_g\equiv Z_{1F}/(Z_2Z_3^{1/2})$; counterterm Lagrangian $\delta\mathcal L=\mathcal L(\text{bare})-\mathcal L(\text{renormalized})$; $Z=1+\delta Z$, $\delta Z=\sum_{k\ge1}(\frac{\alpha_s}{4\pi})^k\sum_jz_{kj}\varepsilon^{-j}$ in minimal schemes.
  - `\uses{def:prelim-qcd, def:qcd-fp, def:qcd-dimreg}`

* **定义 `def:prelim-msbar` — $\overline{\rm MS}$ 方案** (no tag) · v1 (moved; label unchanged)
  - **陈述.** VF-CONV-4: $g_0^2=4\pi\alpha_s(\mu)\mu^{2\varepsilon}e^{\varepsilon\gamma_E}(4\pi)^{-\varepsilon}Z_g^2$, i.e. $S_\varepsilon=(4\pi)^\varepsilon e^{-\varepsilon\gamma_E}$; the $Z$'s contain only poles in $\varepsilon$. **Warning (print):** Collins 2011 uses $(4\pi)^\varepsilon/\Gamma(1-\varepsilon)$, which differs at $O(\varepsilon^2)$ and changes constants multiplying double poles (TMD hard factors: `rem:tmd-scheme-constants`, forward pointer; App C `rem:appC-Seps`).
  - `\uses{def:qcd-renormalization}`

* **定理 `thm:qcd-renormalizability` — QCD 的可重整性** [R, R_PT] · new
  - **陈述.** In DR with minimal subtraction ($\overline{\rm MS}$), massless or massive quarks, there exist renormalization constants $Z_2,Z_3,\tilde Z_3,Z_m,Z_g$ and the vertex constants of `def:qcd-renormalization` — formal power series in $\alpha_s(\mu)$ whose coefficients are polynomials in $1/\varepsilon$ without constant terms — such that all renormalized Green functions of the elementary fields at non-exceptional momenta, and all S-matrix elements between physical states, have finite limits as $\varepsilon\to0$ at every order; the counterterms have the form of the original Lagrangian (multiplicative renormalization, with $\xi_{g,0}=Z_3\xi_g$), and the renormalized theory is BRST invariant with the renormalized BRST transformations.
  - **证明.** Sketch with the four steps: (1) `prop:qcd-superficial-degree` limits the possible local divergences; (2) the Slavnov–Taylor identities of the regularized theory (`lem:qcd-st-regularized`) restrict the counterterms at each order to BRST-invariant local functionals of dimension $\le4$, which by the local BRST cohomology are the gauge-invariant ones of `thm:qcd-gauge-invariance`(b) plus BRST-exact terms (field and gauge-parameter renormalizations); (3) DR preserves the identities order by order; (4) induction on the loop order with the forest formula (`Zimmermann1969`; in DR `tHooftVeltman1972`, `Collins1984` ch. 5–6, 位置待核实). Complete proofs: `tHooft1971`, `tHooftVeltman1972`, `BecchiRouetStora1976` (algebraic renormalization), `Kluberg-Stern:1974nmx`, `Kluberg-Stern:1975ebk` (background field); Lee–Zinn-Justin 1972 「（文献待补）」. Status sentence (print): "the theorem has a complete proof in the literature; this book gives the structure of the proof" (WRITER_SPEC_v2 §4.10, §9.7). (本定理只涉及部分子态的 Green 函数与 S 矩阵元。)
  - `\uses{prop:qcd-superficial-degree, def:qcd-renormalization, def:prelim-msbar, lem:qcd-st-regularized, thm:qcd-gauge-invariance}`

* **命题 `prop:qcd-st-relations` — 重整化常数间的 Slavnov–Taylor 关系** [R, R_PT] · new
  - **陈述.** To all orders in $\overline{\rm MS}$: $Z_g=\frac{Z_{1F}}{Z_2Z_3^{1/2}}=\frac{\tilde Z_1}{\tilde Z_3Z_3^{1/2}}=\frac{Z_1}{Z_3^{3/2}}=\frac{Z_4^{1/2}}{Z_3}$. One loop (units $\frac{\alpha_s}{4\pi\varepsilon}$, general $\xi_g$; VF-QCD-4): $\delta Z_2=-C_F\xi_g$, $\delta Z_3=(\frac{13}6-\frac{\xi_g}2)C_A-\frac43T_Fn_f$, $\delta Z_{1F}=-(\xi_gC_F+\frac{3+\xi_g}4C_A)$, $\delta\tilde Z_3=\frac{3-\xi_g}4C_A$, $\delta\tilde Z_1=-\frac{\xi_g}2C_A$, $\delta Z_1=(\frac{17}{12}-\frac{3\xi_g}4)C_A-\frac43T_Fn_f$, $\delta Z_4=(\frac23-\xi_g)C_A-\frac43T_Fn_f$, so that all four routes give $\delta Z_g=-\frac{\beta_0}2$, $\beta_0=\frac{11}3C_A-\frac43T_Fn_f$, independent of $\xi_g$.
  - **证明.** All orders: sketch from `lem:qcd-st-regularized` and minimal subtraction (`Taylor1971`, `Slavnov1972`). One loop: the general-$\xi_g$ constants are quoted with their literature sources (`PeskinSchroeder1995` ch. 16, `Muta2010`) and verified explicitly in the worked examples `ex:qcd-gluon-self-energy`, `ex:qcd-quark-self-energy-vertex`, `ex:qcd-beta0-four-ways` that follow (pointers: verifications, not steps of the proof). **Formula status:** $\delta Z_2$, $\delta Z_3$ VL; the other five C (general-$\xi_g$ values recalled; the four ST identities, their $\xi_g$ independence and the Feynman-gauge $\delta Z_{1F}$ verified, v2-check Q3); the writer re-derives at least the Feynman-gauge quark–gluon vertex and reports it. (本命题只涉及部分子态。)
  - `\uses{thm:qcd-renormalizability, lem:qcd-st-regularized, def:qcd-renormalization}`

* **定理 `thm:prelim-slavnov-taylor` — Slavnov–Taylor 恒等式（因子化所用形式）** [R, R_PT] · v1 (moved; hypotheses made explicit)
  - **陈述.** In $\overline{\rm MS}$-renormalized perturbative QCD with DR (BRST preserved; no $\gamma_5$ in the vector sector) and for LSZ-amputated on-shell physical external particles $\Phi$ at non-exceptional momenta: $\langle0|T\,\partial\cdot A^{a_1}(x_1)\cdots\partial\cdot A^{a_N}(x_N)\,\Phi|0\rangle=0$ ($N\ge1$, $\Phi\ne1$); and the one-longitudinal-gluon identity with ghost terms (c_wilson §5.6, VF-WL-9).
  - **证明.** Sketch (BRST-invariant vacuum; $\partial\cdot A^a=-\xi_gs\bar c^a$ on shell of $B$; $s\Phi$ has no single-particle pole); App J. Literature: `tHooft1971`, `Taylor1971`, `Slavnov1972`, `BecchiRouetStora1975`, `BecchiRouetStora1976`, `Tyutin1975`, `KugoOjima1979`. Status remark (print): the *identity* is [R]; its use to convert arbitrarily many non-abelian K-gluons into Wilson lines is [A] (`lem:method-ward-multi`, Ch9, pointer). (本定理只涉及部分子态。)
  - `\uses{lem:qcd-st-regularized, thm:qcd-renormalizability, def:prelim-brst}`

* **命题 `prop:qcd-xi-independence` — 物理量的规范参数无关性** [R, R_PT] · new
  - **陈述.** At every order of $\overline{\rm MS}$-renormalized PT, (a) S-matrix elements between physical states (quarks and transverse gluons, `prop:qcd-brst-cohomology`), and (b) Green functions of gauge-invariant composite operators (at non-exceptional momenta) are independent of the gauge parameter $\xi_g$; (c) consequently the $\overline{\rm MS}$ $\beta$ function and the anomalous dimensions of gauge-invariant operators are $\xi_g$ independent.
  - **证明.** Sketch: $\partial\mathcal L/\partial\xi_g=s(\frac12\bar c^aB^a)$ is BRST exact; insert it in a physical amplitude and use `thm:prelim-slavnov-taylor` and the quartet structure; (c) from (a)–(b) applied to a physical quantity that determines $\beta$ (e.g. the Adler function, forward pointer) — or directly from the ST relations. Sources: `KugoOjima1979`, `BecchiRouetStora1976`, `Collins1984`（位置待核实）. (本命题只涉及部分子态与算符。)
  - `\uses{thm:prelim-slavnov-taylor, thm:qcd-renormalizability, lem:prelim-brst-nilpotent, prop:qcd-brst-cohomology}`

* **定理 `thm:prelim-composite-renorm` — 规范不变复合算符的重整化（Joglekar–Lee）** [R, R_PT] · v1 (moved; refdoc S14.2 applied)
  - **陈述.** Gauge-invariant local operators mix under renormalization only with gauge-invariant operators of the same dimension and quantum numbers, BRST-exact operators and equation-of-motion (EOM) operators; the latter two classes have vanishing matrix elements between physical states **at non-zero momentum transfer or with IR-regulated external legs**. Hence physical matrix elements of twist-2 operators renormalize within $\{O_q,O_g\}$.
  - **证明.** Sketch; literature `Joglekar:1975nu`, `Joglekar:1976eb`, `Joglekar:1976pe` (Joglekar 1977 I+II, QCD currents), `Kluberg-Stern:1974iel`, `Kluberg-Stern:1975ebk`, `Henneaux:1993jn`, `DixonTaylor1974`, `Hollands:2007zg` (pure Yang–Mills, curved spacetime) [PENDING-VERIFY: S63-3 — which parts these cover]. **Caveats to print:** (i) forward on-shell massless gluon matrix elements have IR subtleties with the alien operators: the Hamberg–van Neerven puzzle (`Hamberg:1991qt`) and `Collins:1994ee`; modern treatments of alien counterterms in covariant gauges `Falcioni:2022fdm`, `Gehrmann:2023ksf` [PENDING-VERIFY: S63-4]; (ii) the non-local (light-ray) case is **assumed** in Collins 2011 §11.3.2 (survey item 6); a moment reduction of the bilocal PDF case to the local theorem is discussed in Ch24 (pointer) [PENDING-VERIFY: N04]. App J `prop:appJ-local-operators` gives the statement in BRST language; App M §M.6 uses it.
  - `\uses{thm:qcd-renormalizability, lem:qcd-st-regularized, thm:qcd-gauge-invariance}`

* **注 `rem:prelim-bphz-brst` — BPHZ 减除与 Slavnov–Taylor 恒等式；减除度的顶点可加性** (no tag) · refdoc S14.3–S14.4 (label as proposed by refdoc; owner Ch2)
  - (a) BPHZ(L) Taylor subtractions at zero momentum break the Slavnov–Taylor identities of non-abelian gauge theories; the equivalence with DR+$\overline{\rm MS}$ requires additional **finite non-invariant counterterms** (algebraic renormalization; `Breitenlohner:1975hg`, `Breitenlohner:1976te`); the passage from BPHZ to $\overline{\rm MS}$ is therefore *not* a finite renormalization of couplings and fields alone (corrects a statement found in the literature-style presentations; ERR-M28). Consequence used throughout: graphical Ward identities (Ch9) are applied to DR graphs. (b) In the forest formula the subtraction degrees must be vertex additive; the condition $\delta\ge\omega$ alone is not sufficient (counterexample in App M §M.2 [SYNC-APP]).

* **例 `ex:qcd-gluon-self-energy` — 单圈胶子自能与 $Z_3$** (no tag) · new
  - Feynman gauge, external momentum $k$: quark loop ($T_Fn_f$), gluon loop (symmetry factor $\frac12$), ghost loop (closed-loop $-1$), four-gluon tadpole (scaleless, zero in DR); each of the gluon and ghost loops alone is not transverse, the sum is $\propto(k^2g^{\mu\nu}-k^\mu k^\nu)$ (`lem:qcd-st-regularized`); UV pole $\delta Z_3=\frac{\alpha_s}{4\pi\varepsilon}[\frac53C_A-\frac43T_Fn_f]$ (general $\xi_g$: $(\frac{13}6-\frac{\xi_g}2)C_A-\frac43T_Fn_f$). VF-PDF-14, VF-QCD-4; `fig:qcd-vacuum-polarization`.
  - `\uses{def:prelim-feynman-rules, def:qcd-renormalization, def:prelim-msbar, lem:qcd-colour-identities, lem:qcd-st-regularized}`

* **例 `ex:qcd-quark-self-energy-vertex` — 夸克自能与夸克—胶子顶点** (no tag) · new
  - $\delta Z_2=-C_F\xi_g\frac{\alpha_s}{4\pi\varepsilon}$; the quark–gluon vertex: the abelian-like graph with colour $(C_F-\frac{C_A}2)$ and the non-abelian graph with colour $\frac{C_A}2$ (`ex:qcd-colour-algebra`); Feynman gauge $\delta Z_{1F}=-(C_F+C_A)\frac{\alpha_s}{4\pi\varepsilon}$ (re-derived by the writer, reported; general $\xi_g$ value VF-QCD-4, status C).
  - `\uses{def:prelim-feynman-rules, def:qcd-renormalization, ex:qcd-colour-algebra}`

* **例 `ex:qcd-beta0-four-ways` — 用四种 Slavnov–Taylor 等价途径计算 $\beta_0$** (no tag) · new
  - Each route of `prop:qcd-st-relations` with the one-loop values: quark–gluon $\delta Z_{1F}-\delta Z_2-\frac12\delta Z_3$; ghost $\delta\tilde Z_1-\delta\tilde Z_3-\frac12\delta Z_3$; three-gluon $\delta Z_1-\frac32\delta Z_3$; four-gluon $\frac12\delta Z_4-\delta Z_3$ — all equal to $-\frac{11}6C_A+\frac23T_Fn_f=-\frac{\beta_0}2$, the $\xi_g$ dependence cancelling in each (v2-check Q3). Pedagogical point: the gauge-dependent pieces of the individual $Z$'s and the gauge-independent $Z_g$.
  - `\uses{prop:qcd-st-relations, ex:qcd-gluon-self-energy, ex:qcd-quark-self-energy-vertex}`

* **命题 `prop:prelim-beta` — $\beta$ 函数** [R, R_PT] · v1 (moved; VF-QCD-5 added)
  - **陈述.** VF-CONV-5, VF-QCD-5: $\mu^2\frac{d\alpha_s}{d\mu^2}=\beta(\alpha_s)=-\frac{\beta_0}{4\pi}\alpha_s^2-\frac{\beta_1}{(4\pi)^2}\alpha_s^3-\frac{\beta_2}{(4\pi)^3}\alpha_s^4-\dots$ (in $D$ dimensions $\mu^2\frac{d\alpha_s}{d\mu^2}=-\varepsilon\alpha_s+\beta(\alpha_s)$), $\beta_0=\frac{11}3C_A-\frac43T_Fn_f$, $\beta_1=\frac{34}3C_A^2-4C_FT_Fn_f-\frac{20}3C_AT_Fn_f$, $\beta_2$ as in VF-QCD-5; SU(3): $\beta_0=11-\frac23n_f$, $\beta_1=102-\frac{38}3n_f$, $\beta_2=\frac{2857}2-\frac{5033}{18}n_f+\frac{325}{54}n_f^2$.
  - **证明.** $\beta_0$: full — from $Z_g$ (`prop:qcd-st-relations`, `ex:qcd-beta0-four-ways`) and $\mu$-independence of $g_0$ in $\overline{\rm MS}$. $\beta_1$, $\beta_2$: cited (`Caswell1974`, `Jones1974`; `Tarasov:1980au`, `Larin:1993tp`), status C for the group forms (reduction to SU(3) verified, v2-check Q4b–c); four and five loops only as literature (`vanRitbergen:1997va`, `Czakon:2004bu`, `Baikov:2016tgj`, `Herzog:2017ohr`); original $\beta_0$: `GrossWilczek1973a`, `Politzer1973`. (本命题只涉及微扰论。)
  - `\uses{prop:qcd-st-relations, def:prelim-msbar, ex:qcd-beta0-four-ways}`

* **命题 `prop:qcd-rge` — 重整化群方程** [R, R_PT] · new
  - **陈述.** Let $G_R(p_i;\mu,\alpha_s,m,\xi_g)$ be a renormalized Green function of elementary fields ($n_A$ gluons, $n_\psi$ quarks, $n_c$ ghosts). Then $\big[\mu^2\frac{\partial}{\partial\mu^2}+\beta(\alpha_s)\frac{\partial}{\partial\alpha_s}+\gamma_m(\alpha_s)m\frac{\partial}{\partial m}+\delta_\xi(\alpha_s,\xi_g)\frac{\partial}{\partial\xi_g}-\frac{n_A}2\gamma_3-\frac{n_\psi}2\gamma_2-\frac{n_c}2\tilde\gamma_3\big]G_R=0$, with $\gamma_i=\mu^2\frac{d\ln Z_i}{d\mu^2}$, all finite at $\varepsilon\to0$ and, in $\overline{\rm MS}$, functions of $\alpha_s$ (and $\xi_g$) only; for gauge-invariant dimensionless observables and S-matrix elements the field terms drop and $\delta_\xi$ does not contribute (`prop:qcd-xi-independence`).
  - **证明.** Full given `thm:qcd-renormalizability`: bare functions do not depend on $\mu$; minimal subtraction implies that $\beta$ and the $\gamma$'s have no poles ('t Hooft's consistency conditions, `tHooft1973`). Literature: `Gell-Mann:1954yli`, `Callan:1970yg`, `Symanzik:1970rt`, `tHooft1973`, `Collins1984`. (本命题只涉及部分子态。)
  - `\uses{thm:qcd-renormalizability, def:prelim-msbar, prop:prelim-beta, prop:qcd-xi-independence}`

* **命题 `prop:prelim-rg` — 重整化群改进** [R, R_PT] · v1 (moved)
  - **陈述.** For a dimensionless RG-invariant $D(Q^2/\mu^2,\alpha_s(\mu))$: $D=D(1,\alpha_s(Q))$; at each order the coefficient of $\alpha_s^n(\mu)$ is a polynomial in $\ln(Q^2/\mu^2)$ fixed by lower orders and the $\beta_i$ (VF-QCD-9; example $d_2(\mu)=d_2+b_0d_1\ln\frac{\mu^2}{Q^2}$ in the normalization of VF-EE-9).
  - **证明.** Full (characteristics).
  - `\uses{prop:qcd-rge, prop:prelim-beta}`

* **定义 `def:qcd-lambda` — $\Lambda_{\overline{\rm MS}}$ 与跑动耦合** (no tag) · new
  - **陈述.** One loop: $\alpha_s(Q^2)=\frac{\alpha_s(\mu^2)}{1+\frac{\beta_0}{4\pi}\alpha_s(\mu^2)\ln(Q^2/\mu^2)}=\frac{4\pi}{\beta_0\ln(Q^2/\Lambda^2)}$; two loops: the exact separable solution and the truncated form $\alpha_s(Q^2)=\frac{4\pi}{\beta_0L}[1-\frac{\beta_1}{\beta_0^2}\frac{\ln L}{L}]$, $L=\ln(Q^2/\Lambda^2)$, which **defines** $\Lambda^{(n_f)}_{\overline{\rm MS}}$ at this order (VF-QCD-6); $n_f$ = number of quarks lighter than the scale; the matching of $\alpha_s^{(n_f)}$ across heavy-quark thresholds starts at $O(\alpha_s^2)$ when the matching scale equals the heavy-quark $\overline{\rm MS}$ mass (literature; not used in this book).
  - `\uses{prop:prelim-beta}`

* **注 `rem:qcd-decoupling` — 重夸克退耦与有效味数** (no tag) · new
  - $\overline{\rm MS}$ is mass independent, so heavy quarks do not decouple automatically; decoupling is implemented by matching effective theories with $n_f$ and $n_f-1$ flavours (Appelquist–Carazzone 「（文献待补：T. Appelquist, J. Carazzone 1975, Phys. Rev. D 11, 2856）」); the corresponding statement for PDFs and coefficient functions is the variable-flavour-number scheme (forward pointer `thm:disall-heavy`).

* **例 `ex:qcd-running-numbers` — 从 $\alpha_s(M_Z)$ 出发的数值跑动** (no tag) · new
  - PDG 2024 $\alpha_s(M_Z^2)=0.1180\pm0.0009$ (`ParticleDataGroup:2024cfk`, eq. (9.25)); $n_f=5$, $\beta_0=\frac{23}3$, $\beta_1=\frac{116}3$; the table of VF-QCD-7 (one loop, exact two loop, truncated two loop with $\Lambda^{(5)}=0.2262$ GeV; e.g. $\alpha_s(10\,{\rm GeV})=0.1731/0.1779/0.1783$); slope of $1/\alpha_s$ in $\ln Q$: $\beta_0/(2\pi)=1.2202$; `fig:qcd-running-coupling` (tested starter code in FIGURES_INDEX_v2 §4.1 N2). Only these experimental numbers may be printed (WRITER_SPEC_v2 §2 item 9).
  - `\uses{def:qcd-lambda, prop:prelim-rg}`

* **定理 `thm:qcd-asymptotic-freedom` — 渐近自由** [R, R_PT] · new
  - **陈述.** (a) The one-loop coefficient $\beta_0=\frac{11}3C_A-\frac43T_Fn_f$ of SU($N$) gauge theory with $n_f$ Dirac quarks in the fundamental representation is independent of the gauge parameter; $\beta_0$ and $\beta_1$ are the same in all mass-independent schemes related by $\alpha_s'=\alpha_s+c_1\alpha_s^2+\dots$. (b) $\beta_0>0\iff n_f<\frac{11C_A}{4T_F}$ (SU(3): $n_f\le16$; $\beta_1>0$ for $n_f\le8$, $<0$ for $9\le n_f\le16$; VF-QCD-8). (c) For $\beta_0>0$ and every truncation $\beta^{[K]}$ of the perturbative $\beta$ function with $K\ge1$ terms, the solution of $\mu^2d\alpha_s/d\mu^2=\beta^{[K]}(\alpha_s)$ with a sufficiently small initial value $\alpha_s(\mu_0)>0$ exists for all $\mu>\mu_0$, decreases monotonically to $0$, and $\alpha_s(\mu)=\frac{4\pi}{\beta_0\ell}-\frac{4\pi\beta_1}{\beta_0^3}\frac{\ln\ell}{\ell^2}+O(\frac{\ln^2\ell}{\ell^3})$, $\ell=\ln(\mu^2/\Lambda^2)$ (for $K\ge2$; the one-loop form for $K=1$). In words: the perturbative renormalization-group flow has an ultraviolet-stable fixed point at $\alpha_s=0$.
  - **证明.** (a) $\xi_g$ independence from `prop:qcd-xi-independence`(c); scheme independence of $\beta_0,\beta_1$ by substituting $\alpha_s'(\alpha_s)$ into the RGE (full, three lines). (b) Arithmetic (v2-check Q4d–e). (c) Elementary ODE analysis (separation of variables; full). Literature: `GrossWilczek1973a`, `Politzer1973`; `Coleman:1973sx` (no asymptotic freedom without non-abelian gauge fields, at one loop); `Caswell1974`, `Jones1974`. Status remark (print): AF is a statement about the perturbative RG flow; that QCD exists non-perturbatively with this ultraviolet behaviour is part of `asm:intro-wightman` ([C]); lattice simulations (`Wilson:1974sk`) are evidence, not proof. (本定理只涉及微扰论。)
  - `\uses{prop:prelim-beta, prop:qcd-rge, prop:qcd-xi-independence}`

* **注 `rem:qcd-antiscreening` — 屏蔽与反屏蔽的直观图像** (no tag) · new
  - Screening by virtual quark pairs ($-\frac43T_Fn_f$) vs antiscreening by the coloured gluon cloud ($+\frac{11}3C_A$); the "paramagnetic spin" interpretation of the gluon contribution (`Nielsen:1980sx`); explicitly heuristic, the gauge-independent derivation is `prop:prelim-beta`; `fig:qcd-antiscreening`.

* **注 `rem:qcd-af-meaning` — 渐近自由意味着什么、不意味着什么** (no tag) · new
  - AF makes hard coefficients computable **only if** the long-distance part has been separated — the content of the factorization theorems of this book; AF does not imply confinement; the perturbative series are asymptotic (renormalons, forward pointer `def:power-borel`); the hadron-level use of PT always goes through `asm:intro-bridge`; the coupling at hadronic scales is not small (VF-QCD-7: $\alpha_s(5\,{\rm GeV})\approx0.21$).

* **命题 `prop:qcd-soft-collinear-limits` — 树图层次的软极限与共线极限** [R, R_PT] · new
  - **陈述.** (Tree level, massless partons, $D=4$ unless stated.) (a) *Soft limit:* if a gluon $(k,a,\varepsilon)$ is added to a tree amplitude $\mathcal M_n$ with external massless partons $i$ of momenta $p_i$ (all outgoing) and colour operators $\mathbf T_i$, then for $k\to0$ uniformly, $\mathcal M_{n+1}=g\sum_i\frac{p_i\cdot\varepsilon^*}{p_i\cdot k}\mathbf T^a_i\mathcal M_n+O(k^0)$ (overall sign fixed by our Feynman rules, VF-WL-5); summing over polarizations (allowed with $-g_{\mu\nu}$ by colour conservation $\sum_i\mathbf T_i=0$), $\sum|\mathcal M_{n+1}|^2\to-g^2\sum_{i\ne j}\frac{p_i\cdot p_j}{(p_i\cdot k)(p_j\cdot k)}\langle\mathcal M_n|\mathbf T_i\cdot\mathbf T_j|\mathcal M_n\rangle$; for a colour-singlet $q\bar q$ pair this is $g^2C_F\frac{2p\cdot\bar p}{(p\cdot k)(\bar p\cdot k)}|\mathcal M_n|^2$. (b) *Collinear limit:* if an outgoing quark of momentum $P$ is replaced by a quark $zP+\dots$ and a gluon $(1-z)P+\dots$ with relative transverse momentum $k_T\to0$, then $\sum|\mathcal M_{n+1}|^2\to\frac{2g^2}{s_{qg}}C_F\frac{1+z^2}{1-z}\sum|\mathcal M_n|^2$ (spin summed; in $D$ dimensions the kernel $\frac{1+z^2}{1-z}-\varepsilon(1-z)$, VF-PDF-6). (c) Both factors behave as $\frac{dE_k}{E_k}\frac{d\theta^2}{\theta^2}$ near the singular configurations: exclusive partonic cross sections are IR divergent.
  - **证明.** Full (eikonal approximation of the propagator next to the emission vertex; Sudakov parametrization for (b)). Checks (writer-derived, report): both limits of the exact $\gamma^*\to q\bar qg$ matrix element $\propto\frac{x_1^2+x_2^2}{(1-x_1)(1-x_2)}$ (VF-EE-5), and the real part of $P_{qq}$ (VF-PDF-7). Literature: `AltarelliParisi1977`, `CataniSeymour1997`, `Weinberg1965`. (本命题只涉及部分子振幅。)
  - `\uses{def:prelim-feynman-rules, lem:qcd-colour-identities}`

* **定义 `def:qcd-ir-safety-informal` — 红外安全（非形式）** (no tag) · new
  - **陈述.** An observable is *infrared safe* if its value is unchanged when a parton of zero energy is added to the final state or a massless parton is replaced by two exactly collinear massless partons with the same total momentum. The precise definition (weights continuous in the energy-flow topology) is `def:ir-safe` (Ch4, forward pointer).
  - `% uses: none`

* **例 `ex:qcd-ee-real-virtual` — $e^+e^-\to q\bar q(g)$：实辐射与虚修正的相消** (no tag) · new
  - In one normalization: virtual $N_\varepsilon[-\frac2{\varepsilon^2}-\frac3\varepsilon-8+\pi^2]$ (from $2{\rm Re}F$, VF-EE-4), real $N_\varepsilon[\frac2{\varepsilon^2}+\frac3\varepsilon+\frac{19}2-\pi^2]$ (VF-EE-5); sum $\frac32N_\varepsilon$, $R=R_0(1+\frac{3C_F}4\frac{\alpha_s}\pi)$ (VF-EE-6); the quark energy spectrum keeps a collinear pole (VF-EE-11) — not IR safe; absorbed into fragmentation functions (forward pointer). Full derivation in Ch6 (`prop:ee-oneloop`, pointer); here the structure and the pole cancellation are shown, with `fig:qcd-ir-safety`.
  - `\uses{prop:qcd-soft-collinear-limits, def:qcd-ir-safety-informal, def:qcd-dimreg}`

* **例 `ex:qcd-sterman-weinberg` — 第一个红外安全的排他量：Sterman–Weinberg 两喷注截面** (no tag) · new
  - $\sigma_{2j}=\sigma_0\{1-\frac{C_F\alpha_s}\pi[4\ln\delta\ln2\epsilon+3\ln\delta+\frac{\pi^2}3-\frac52]\}$ for $\epsilon<\delta\ll1$ with $\epsilon$ a fraction of the **total** energy (VF-EE-12; the variant with $\ln\epsilon$ belongs to $\epsilon$ defined relative to the beam energy) [PENDING-VERIFY: E28 — only if a published source is named as erroneous]; derivation in Ch16 (`prop:jets-sw`, pointer); here: why the double logarithm appears and why the result is finite.
  - `\uses{ex:qcd-ee-real-virtual, def:qcd-ir-safety-informal}`

* **注 `rem:qcd-ir-theorems-preview` — 红外定理预览** (no tag) · new
  - In words with tags and forward pointers: Bloch–Nordsieck in QED (`thm:ir-bn-qed`, [R]); KLN (`thm:ir-kln`, [A]); the non-abelian failure of Bloch–Nordsieck with coloured initial states (`prop:ir-bn-failure`, [V], power suppressed); finiteness of IR-safe observables (`thm:ir-safe-finite`, [A]); initial-state collinear singularities are not cancelled but factorized into PDFs (Part II–III). 「这些定理的精确陈述与证明见第~4~章。」

**Worked examples (≥ 8 required; 10 here).** `ex:qcd-colour-algebra`, `ex:qcd-fp-lowest-order`, `ex:qcd-qqbar-gg`, `ex:qcd-brst-quartet`, `ex:qcd-gluon-self-energy`, `ex:qcd-quark-self-energy-vertex`, `ex:qcd-beta0-four-ways`, `ex:qcd-running-numbers`, `ex:qcd-ee-real-virtual`, `ex:qcd-sterman-weinberg`.

**Tables.** `tab:qcd-symbols` 记号速查 (symbols introduced in Ch2: $t^a,f^{abc},d^{abc},C_F,C_A,T_F,n_f$; $D_\mu$, $G_{\mu\nu}$, $\tilde G$; $\xi_g$, $c,\bar c,B$, $s$, $Q$; $D,\varepsilon,\mu_0,\mu,S_\varepsilon$; $Z_2,Z_3,\tilde Z_3,Z_{1F},\tilde Z_1,Z_1,Z_4,Z_g,Z_m$; $\beta(\alpha_s),\beta_n,\gamma_i,\Lambda^{(n_f)}$), each with the place of definition.

**Figures.** Required (FIGURES_INDEX_v2): `fig:prelim-feynman-rules` (§2 item 2), `fig:qcd-vacuum-polarization` (§4.1 N1, in `sec:qcd-renorm`), `fig:qcd-running-coupling` (N2, `sec:qcd-running`; tested starter code), `fig:qcd-antiscreening` (N3, `sec:qcd-af`), `fig:qcd-ir-safety` (N4, `sec:qcd-ir`). Optional: `fig:qcd-gauge-orbit` (`sec:qcd-quantization`), `fig:qcd-colour-flow` (`sec:qcd-gauge`). `fig:ee-oneloop` (Ch6) and `fig:soft-eikonal` (Ch3) only as forward pointers.

**Misconception box (WRITER_SPEC_v2 §6.8).** 「维数正规化消除红外发散」 → it regulates them; scaleless integrals are $\frac1{\varepsilon_{\rm UV}}-\frac1{\varepsilon_{\rm IR}}$ (pointers `def:prelim-dr-conventions`, `prop:pdf-partonic-dr`); M28 preview (QCD is not constructed as a mathematical QFT, so [R] means perturbatively rigorous; `asm:intro-wightman`); 「鬼场是非物理的，可以忽略」 → needed for unitarity of cut sums in covariant gauges (`ex:qcd-qqbar-gg`); 「渐近自由证明了微扰论对强子过程适用」 → only after factorization (`rem:qcd-af-meaning`); critic C14 preview (UV vs IR poles).

**Key citation keys (REFS_NOTES_v2 §3.1).** `Yang:1954ek`, `Gell-Mann:1964ewy`, `Zweig:1964jf`, `Greenberg:1964pe`, `Han:1965pf`, `Fritzsch:1973pi`; `Faddeev:1967fc`, `BecchiRouetStora1975`, `BecchiRouetStora1976`, `Tyutin1975`, `KugoOjima1979`, `tHooft1971`, `Taylor1971`, `Slavnov1972`, `tHooftVeltman1972b`; `tHooftVeltman1972`, `tHooft1973`, `BardeenEtAl1978`, `Gell-Mann:1954yli`, `Callan:1970yg`, `Symanzik:1970rt`, `Collins1984`, `Joglekar:1975nu`, `Joglekar:1976eb`, `Joglekar:1976pe`, `Kluberg-Stern:1974iel`, `Kluberg-Stern:1974nmx`, `Kluberg-Stern:1975ebk`, `Henneaux:1993jn`, `DixonTaylor1974`, `Collins:1994ee`, `Hamberg:1991qt`, `Falcioni:2022fdm`, `Gehrmann:2023ksf`, `Hollands:2007zg`, `Breitenlohner:1975hg`, `Breitenlohner:1976te`, `Zimmermann1969`; `GrossWilczek1973a`, `Politzer1973`, `Coleman:1973sx`, `Caswell1974`, `Jones1974`, `Tarasov:1980au`, `Larin:1993tp`, `vanRitbergen:1997va`, `Czakon:2004bu`, `Baikov:2016tgj`, `Herzog:2017ohr`, `Nielsen:1980sx`, `ParticleDataGroup:2024cfk`; `BlochNordsieck1937`, `Kinoshita1962`, `LeeNauenberg1964`, `StermanWeinberg1977`, `EllisRossTerrano1981`, `AltarelliParisi1977`, `CataniSeymour1997`, `Weinberg1965`, `CombridgeKripfganzRanft1977`; textbooks `PeskinSchroeder1995`, `Itzykson:1980rh`, `Weinberg1996`, `Muta2010`, `EllisStirlingWebber1996`, `Sterman1993`, `Collins2011`, `Wilson:1974sk`. Missing from the bib (cite as 「文献待补」 only if needed): Gribov 1978; Lee–Zinn-Justin 1972; Zinn-Justin 1975; Appelquist–Carazzone 1975.

**Pending.** `thm:prelim-composite-renorm` caveats [PENDING-VERIFY: S63-3, S63-4, N04]; `ex:qcd-sterman-weinberg` sentence on the $\ln\epsilon$ variant [PENDING-VERIFY: E28]. VF-QCD-4 general-$\xi_g$ entries (status C) are re-derived by the writer (not a verify item).

---------------------------------------------------------------------------------------------------

## Chapter 3 — 因子化的数学与场论工具 / Mathematical and field-theoretic tools of factorization

`\label{ch:prelim}` · `ch03_prelim.tex` · **12 pp** · full (long proofs in App A, B, C, I, J, K) · Part I

**Purpose.** Collect every tool used later, with conventions fixed once (WRITER_SPEC_v2 §3), starting each section from the question it answers (WRITER_SPEC_v2 §7): light-front coordinates and boosts (power counting, Ch4, App E); Wilson lines and their momentum-space rules (Ch5, Ch8, Ch9, Ch12, Ch14; App B); the technical conventions of dimensional regularization ($\varepsilon_{\rm UV}$ vs $\varepsilon_{\rm IR}$, scaleless integrals, polarization averages) and $\gamma_5$ (App I); distributions on $[0,1]$, plus distributions, Mellin transforms; the moment problems, Carlson's and Müntz's theorems (App K) as the mathematics behind "moments determine $x$ space only as distributions"; cut diagrams, cutting rules, physical unitarity, the optical theorem for current correlators. The QCD-basics half of v1 Ch2 is now Ch2.

**Depends on.** Ch2 (`def:prelim-qcd`, `def:prelim-feynman-rules`, `prop:qcd-covariance`, `prop:qcd-brst-cohomology`, `thm:prelim-slavnov-taylor`, `def:qcd-dimreg`, `def:prelim-msbar`, `ex:qcd-qqbar-gg`); App A, B, I, J, K.

**Box.**
- 证明了：`lem:prelim-boost`（[R, R_def]）；`prop:prelim-wilson-covariance`、`prop:prelim-wilson-rules`（[R, R_def]，证明见附录 B）；`lem:prelim-eikonal-identity`、`lem:prelim-scaleless`、`lem:prelim-plus-expansion`、`lem:prelim-mellin`（数学）；`thm:prelim-cutting-rules`（[R, R_PT]，有质量或已正规化的图）；`prop:prelim-unitarity`（[R, R_PT]）；`prop:prelim-optical`（[R, R_def]，强子态需 `asm:intro-wightman`）。
- 给出全阶论证：`rem:prelim-cutting-dr`（[A]：无质量维数正规化中含鬼场的割图规则）。
- 没有证明：带插入的光锥割线位置恒等式与闭时路幺正性（附录 O，`lem:appO-cut-position`、`lem:appO-unitarity`）；单个割图不满足幺正性（只有对割线求和才行）。

**Sections.**
1. `sec:prelim-lightfront` 光锥坐标、Sudakov 分解与 Lorentz 推动 — $n_A,n_B$; boost scaling of momentum components and of good/bad spinor components; `fig:prelim-lightcone`.
2. `sec:prelim-wilson` Wilson 线 — definition, ODE, covariance, composition/retracing, adjoint lines; momentum-space rules (universal rule); finite light-like segments; eikonal identity; external partons ↔ semi-infinite lines (`fig:soft-eikonal`); light-like lines have cusp/rapidity divergences (forward pointers Ch5, Ch14).
3. `sec:prelim-dimreg` 维数正规化的技术约定与 $\gamma_5$ — $\varepsilon_{\rm UV}/\varepsilon_{\rm IR}$ bookkeeping; scaleless integrals; CDR traces and averages; $S_\varepsilon$ (pointer `def:prelim-msbar`, App C); $\gamma_5$ (HVBM + Larin, App I).
4. `sec:prelim-distributions` $[0,1]$ 上的分布与 Mellin 变换 — plus distributions (whole-function and product conventions, $\mathcal D_k$), expansion lemma, Mellin transform, convolution theorem, harmonic sums.
5. `sec:prelim-moments` 矩问题、Carlson 定理与 Müntz–Szász 定理 — the results of App K stated and explained (what moments determine, and what they do not).
6. `sec:prelim-cuts` 割图、切割规则、幺正性与光学定理 — cut diagrams; cutting rules; physical unitarity with ghosts; $R=12\pi{\rm Im}\Pi$; $W^{\mu\nu}=\frac1{2\pi}{\rm Im}T^{\mu\nu}$; the one-loop correlator example.

**Canonical statements** (in reading order).

* **定义 `def:prelim-lightfront` — 光锥坐标与 Sudakov 分解** (no tag) · v1
  - **陈述.** VF-CONV-1; $n_A=(1^+,0^-,\mathbf 0_T)$ with $n_A\cdot v=v^-$, $n_B=(0^+,1^-,\mathbf 0_T)$ with $n_B\cdot v=v^+$ ($n_B$ = Collins' $w_2$); $k=\alpha p_A+\beta p_B+k_T$; rapidity $y=\frac12\ln(k^+/k^-)$; dictionary to the SCET $n,\bar n$ (Ch15) in App A.
  - `% uses: none`

* **引理 `lem:prelim-boost` — 推动下的标度** [R, R_def] · v1
  - **陈述.** Boost along $z$ with rapidity $\eta$: $v^\pm\to e^{\pm\eta}v^\pm$, $v_T\to v_T$; good/bad spinor components $P_\pm\psi$, $P_+=\frac12\gamma^-\gamma^+$, $P_-=\frac12\gamma^+\gamma^-$, scale as $e^{\pm\eta/2}$.
  - **证明.** Full (generator $\gamma^0\gamma^3$; App A).
  - `\uses{def:prelim-lightfront}`

* **例 `ex:prelim-boost-scaling` — 共线动量与好/坏分量的标度** (no tag) · new
  - A collinear momentum $Q(1,\lambda^2,\lambda)$ as the boost of a rest-frame momentum with $e^\eta\sim1/\lambda$; the good components dominate ($\propto\lambda^{-1/2}$ relative); why the gluon field of a fast hadron is dominated by $A^+$ (preview of K-gluons, `def:ir-scalings` and `prop:ir-power-counting`, pointers).
  - `\uses{lem:prelim-boost}`

* **定义 `def:prelim-wilson` — Wilson 线** (no tag) · v1
  - **陈述.** VF-CONV-9: $W[b,a]=P\exp(ig\int_a^bdz^\mu A^a_\mu t^a)$, later points left; semi-infinite lines $W[\infty n,y]$, $W[y,-\infty n]$, … ($n$ future pointing); adjoint line $W^{(A)}_{ab}[b,a]=2{\rm Tr}[t^aW[b,a]t^bW[a,b]]$; Fourier convention $A(x)=\int\frac{d^4k}{(2\pi)^4}e^{-ik\cdot x}\tilde A(k)$ ($k$ flows *into* the line); adiabatic regulator.
  - `\uses{def:prelim-qcd, def:prelim-lightfront}`

* **命题 `prop:prelim-wilson-covariance` — Wilson 线的规范协变性** [R, R_def] · v1
  - **陈述.** $\frac{d}{ds}W(s)=ig\,\dot z\cdot A(z(s))W(s)$; $W[b,a]\to U(b)W[b,a]U^\dagger(a)$ (the reversed ordering is not covariant); $W[c,b]W[b,a]=W[c,a]$, $W[b,a]W[a,b]=1$.
  - **证明.** Full (ODE uniqueness), App B; numerical SU(2)/SU(3) checks as a remark (c_pdf s1, c_wilson s1(E)).
  - `\uses{def:prelim-wilson, prop:qcd-covariance}`

* **命题 `prop:prelim-wilson-rules` — 半无限直 Wilson 线的动量空间 Feynman 规则** [R, R_def] · v1
  - **陈述.** VF-WL-1 (universal rule): vertex $igt^av^\mu$, eikonal propagator $i/(v\cdot\ell+i0)$ with $\ell$ along the orientation, colour in path order, $\ell=0$ on the segment reaching infinity; past-pointing $W[0,-\infty n]$: $\prod_j\frac{i}{n\cdot(k_1+\dots+k_j)+i0}$; future-pointing $W[\infty n,0]$: $\prod_j\frac{-i}{n\cdot(k_j+\dots+k_m)-i0}$; conjugate lines: complex conjugates (vertex $-igt^an^\mu$); future minus past at the same point: $2\pi i\,gt^an^\mu\delta(n\cdot k)$.
  - **证明.** Full in App B (iterated integrals + induction; `prop:appB-rules`). `fig:prelim-wilson-rules`.
  - `\uses{def:prelim-wilson, def:prelim-feynman-rules, prop:appB-rules}`

* **引理 `lem:prelim-eikonal-identity` — 程函恒等式** (数学，无标签) · v1
  - **陈述.** $\sum_{\pi\in S_m}\prod_{j=1}^m[a_{\pi(1)}+\dots+a_{\pi(j)}]^{-1}=\prod_ja_j^{-1}$; exact at finite $\epsilon$ with the adiabatic regulator (the $j$-th denominator carries $+ij\epsilon$), **not** with a uniform $+i\epsilon$ (VF-WL-2) [PENDING-VERIFY: N26 — attribution sentence only].
  - **证明.** Full (two proofs: simplex decomposition; induction), App B (`lem:appB-shuffle`); non-abelian (web) decomposition in App B.
  - `\uses{lem:appB-shuffle}`

* **例 `ex:prelim-eikonal-two` — $m=2$ 的程函恒等式与入射夸克传播子的程函极限** (no tag) · v1
  - Eikonal identity for $m=2$; eikonal limit $S(p+k)ig\gamma^\mu t^au(p)\simeq-gt^a\frac{p^\mu}{p\cdot k+i0}u(p)$ (VF-WL-5); link to `fig:soft-eikonal`.
  - `\uses{lem:prelim-eikonal-identity, prop:prelim-wilson-rules}`

* **例 `ex:prelim-wilson-segment` — 有限类光线段的单胶子项** (no tag) · new
  - For $w=(0^+,w^-,\mathbf 0_T)$ and the segment along $n_B$: $W^{(1)}[w,0]=gt^a\int\frac{d^4k}{(2\pi)^4}\tilde A^{a+}(k)\frac{1-e^{-ik^+w^-}}{k^+}$ (writer re-derives the sign in our convention; refdoc S52 uses this form in App F); the pole at $k^+=0$ is removable; the limits $w^-\to\pm\infty$ with the adiabatic factor reproduce the semi-infinite rules of `prop:prelim-wilson-rules`; this is the one-gluon term of the PDF Wilson line (forward pointer `def:pdf-quark`).
  - `\uses{def:prelim-wilson, prop:prelim-wilson-rules}`

* **定义 `def:prelim-dr-conventions` — 维数正规化的技术约定** (no tag) · new
  - **陈述.** (a) The origin of every pole is stated: $\varepsilon_{\rm UV}$ (from large momenta, removed by renormalization) vs $\varepsilon_{\rm IR}$ (from soft/collinear regions, cancelling or factorized); in DR both are the same $\varepsilon$, and the labelling is a bookkeeping device (critic C14). (b) Averages over initial states: quark spin $\frac12$, colour $\frac1{N_c}$; gluon polarizations $\frac1{D-2}=\frac1{2(1-\varepsilon)}$, colour $\frac1{N_c^2-1}$ — the gluon average is part of the $\overline{\rm MS}$ convention for partonic coefficient functions (VF-CONV-6). (c) CDR traces (`def:qcd-dimreg`); $D$-dimensional phase space and the $S_\varepsilon$ conventions: App C (`rem:appC-Seps`).
  - `\uses{def:qcd-dimreg, def:prelim-msbar}`

* **引理 `lem:prelim-scaleless` — 无标度积分为零** (数学，无标签) · new
  - **陈述.** In DR, $\int d^Dk\,(-k^2-i0)^{-a}=0$ for every $a$; more generally every integral without a scale vanishes. For $a=2$, $D=4-2\varepsilon$: splitting at $|k|=\Lambda$ (Euclidean) gives $\propto(\frac1{\varepsilon_{\rm UV}}-\frac1{\varepsilon_{\rm IR}})$, each part continued from its own convergence region.
  - **证明.** Full (analytic continuation; App C).
  - `\uses{def:qcd-dimreg}`

* **例 `ex:prelim-scaleless` — 无标度积分的紫外/红外记账** (no tag) · new
  - (i) The on-shell massless quark self-energy is scaleless: $Z_2^{\rm OS}=1$ in DR, so external legs carry no corrections (used in `prop:sudakov-oneloop`); (ii) the quark-in-quark PDF integral $\int\frac{d^{2-2\varepsilon}l_T}{l_T^2}=0$, read as $\frac1{\varepsilon_{\rm UV}}-\frac1{\varepsilon_{\rm IR}}$, so that the $\overline{\rm MS}$ counterterm turns into an IR pole (forward pointer `prop:pdf-partonic-dr`; misconception M24).
  - `\uses{lem:prelim-scaleless, def:prelim-dr-conventions}`

* **定义 `def:prelim-gamma5` — $\gamma_5$ 与 $\varepsilon$ 张量** (no tag) · v1
  - **陈述.** VF-CONV-10: $\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3$, $\varepsilon^{0123}=+1$, ${\rm Tr}(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma\gamma_5)=-4i\varepsilon^{\mu\nu\rho\sigma}$; in DR: HVBM with Larin's finite renormalization of the axial currents (App I; replacement $\gamma^\mu\gamma_5=-\frac i6\epsilon^{\mu\nu\rho\sigma}\gamma_\nu\gamma_\rho\gamma_\sigma$ in our convention, VF-CONV-24). Warning: VGG use $\varepsilon_{0123}=+1$.
  - `\uses{def:qcd-dimreg}`

* **定义 `def:prelim-plus` — 加号分布** (no tag) · v1
  - **陈述.** VF-CONV-7: $\int_0^1[g]_+h=\int_0^1g\,(h-h(1))$; $\mathcal D_k(z)=[\ln^k(1-z)/(1-z)]_+$; **product convention** $g(z)\mathcal D_k\equiv g(1)\mathcal D_k+\frac{g(z)-g(1)}{1-z}\ln^k(1-z)$; identities $C_F[\frac{1+z^2}{1-z}]_+=C_F[\frac{1+z^2}{(1-z)_+}+\frac32\delta(1-z)]$, $[\frac{2z}{1-z}]_+=\frac{2z}{(1-z)_+}+2\delta(1-z)$, $[\frac z{1-z}]_+=z[\frac1{1-z}]_++\delta(1-z)$; $(1+z^2)\mathcal D_1$ and $[(1+z^2)\ln(1-z)/(1-z)]_+$ differ by $\frac74\delta(1-z)$ (VF-DY-12). Test-function class: App A (refdoc S51). Star distributions and $\tau$-space plus distributions (event shapes) are introduced in Ch15 with their own notation (WRITER_SPEC_v2 §3 row 22).
  - `% uses: none`

* **引理 `lem:prelim-plus-expansion` — $(1-z)^{-1-a\varepsilon}$ 的分布展开** (数学，无标签) · v1
  - **陈述.** On $[0,1]$, test functions continuous at 1, for $a\varepsilon<0$: $(1-z)^{-1-a\varepsilon}=-\frac{1}{a\varepsilon}\delta(1-z)+\sum_{k\ge0}\frac{(-a\varepsilon)^k}{k!}\mathcal D_k(z)$. Used with $a=1$ (DIS), $a=2$ (DY, soft functions).
  - **证明.** Full (App A).
  - `\uses{def:prelim-plus}`

* **例 `ex:prelim-plus` — 单圈实辐射的典型积分** (no tag) · v1
  - $\int_0^1dz(1-z)^{-1-2\varepsilon}z^{-\varepsilon}h(z)$ expanded with `lem:prelim-plus-expansion` (the structure of every one-loop real emission).
  - `\uses{lem:prelim-plus-expansion}`

* **定义 `def:prelim-mellin` — Mellin 变换与卷积** (no tag) · v1
  - **陈述.** $\tilde f(N)=\int_0^1z^{N-1}f(z)dz$; $(f\otimes g)(x)=\int_x^1\frac{d\xi}\xi f(\xi)g(x/\xi)$; harmonic sums $S_k(N)$, $S_1(N)=\psi(N+1)+\gamma_E$, $S_2(N)=\zeta_2-\psi'(N+1)$; $\bar N=Ne^{\gamma_E}$.
  - `\uses{def:prelim-plus}`

* **引理 `lem:prelim-mellin` — Mellin 卷积定理与加号分布的矩** (数学，无标签) · v1
  - **陈述.** $\widetilde{f\otimes g}=\tilde f\tilde g$ (distributions supported in $[0,1]$ with existing moments); $\int_0^1z^{N-1}\mathcal D_0=-S_1(N-1)$, $\int_0^1z^{N-1}\mathcal D_1=\frac12[S_1^2(N-1)+S_2(N-1)]$ (VF-CONV-8); large $N$: $-\ln\bar N$, $\frac12(\ln^2\bar N+\zeta_2)$.
  - **证明.** Full (App A, `lem:appA-mellin-table`).
  - `\uses{def:prelim-mellin, def:prelim-plus, lem:appA-mellin-table}`

* **注 `rem:prelim-moment-tools` — 矩问题工具箱** (no tag) · new
  - States, with the proofs in App K, the facts used later: Hausdorff uniqueness (`lem:appK-hausdorff`); even moments determine a function (`thm:appK-even-moments`) and the C-even PDF combinations (`cor:appK-pdf`); Carlson's theorem (`thm:appK-carlson`) and unique continuation under polynomial bounds (`prop:appK-continuation`); Müntz–Szász (`thm:appK-muntz`); counterexamples and instability (`rem:appK-counterexamples`: $\delta'$; $\sin(Q^2x)$; Hilbert-matrix condition number $\sim e^{3.5K}$). Message: moments determine $x$-space objects as distributions; neither pointwise bounds nor stable inversion follow (preview of `rem:dis-nonuniform`, `cor:dis-weak-xspace`).
  - `\uses{lem:appK-hausdorff, thm:appK-even-moments, cor:appK-pdf, thm:appK-carlson, prop:appK-continuation, thm:appK-muntz, rem:appK-counterexamples}`

* **定义 `def:prelim-cut` — 割图** (no tag) · v1
  - **陈述.** Cut propagators $2\pi\delta^+(p^2-m^2)(\slashed p+m)$; right of the cut: complex-conjugate rules (including the Wilson-line rules of `prop:prelim-wilson-rules`).
  - `\uses{def:prelim-feynman-rules, prop:prelim-wilson-rules}`

* **定理 `thm:prelim-cutting-rules` — 切割规则** [R, R_PT] · v1 (+ refdoc S14.1)
  - **陈述.** For Feynman graphs with positive masses on all internal lines (or otherwise regulated so that all integrals converge), the largest-time equation gives $2\,{\rm Im}\,G=\sum_{\rm cuts}G_{\rm cut}$ in the physical region.
  - **证明.** Sketch of the largest-time equation (`Veltman1963`, `tHooftVeltman1974`), `Cutkosky1960`. Forward pointer (refdoc S14.1): the light-cone version with insertions and its closed-time-path form (`lem:appO-cut-position`, `lem:appO-unitarity`, App O). (本定理只涉及 Feynman 图。)
  - `\uses{def:prelim-cut, def:prelim-feynman-rules}`

* **命题 `prop:prelim-unitarity` — 物理幺正性与鬼场割线** [R, R_PT] · v1
  - **陈述.** The sum over all cuts of Feynman-gauge graphs including ghost cuts equals the sum over physical (transverse-gluon, quark) final states; tree-level example $q\bar q\to gg$ (`ex:qcd-qqbar-gg`, VF-WL-9).
  - **证明.** Sketch (quartet structure `prop:qcd-brst-cohomology` + `thm:prelim-slavnov-taylor`; 't Hooft–Veltman combinatorics); App J `prop:appJ-ghost-cuts`. Literature: `KugoOjima1979`, `tHooftVeltman1972b`, `CombridgeKripfganzRanft1977`. (本命题只涉及部分子态。)
  - `\uses{def:prelim-cut, thm:prelim-cutting-rules, prop:qcd-brst-cohomology, thm:prelim-slavnov-taylor, prop:appJ-ghost-cuts, ex:qcd-qqbar-gg}`

* **注 `rem:prelim-cutting-dr` — 无质量维数正规化中的割图规则** [A] · v1
  - **陈述.** Extension of `thm:prelim-cutting-rules` and `prop:prelim-unitarity` to massless graphs in DR with ghosts, as identities of meromorphic functions of $\varepsilon$.
  - **地位与缺口.** Verified exactly in $\varepsilon$ at $O(g^2)$ for the current correlator (VF-EE-8; forward pointer `prop:ee-cutting-exact`); no single source writes the general massless DR version in full (c_ee §5); the cut-summed light-cone representation used in App O (`asm:appN-cutsum`) is the precise form needed for factorization (pointer). Error type: the identity is exact where it is proved; the general statement is an E-S-level argument.
  - `\uses{thm:prelim-cutting-rules, prop:prelim-unitarity, def:qcd-dimreg}`

* **命题 `prop:prelim-optical` — 流关联函数的光学定理** [R, R_def] · v1
  - **陈述.** With VF-CONV-12/13/14: $\sum_X(2\pi)^4\delta^4(q-p_X)\langle0|j^\mu|X\rangle\langle X|j^\nu|0\rangle=2\,{\rm Im}\,\Pi^{\mu\nu}(q)$ ($q^0>0$), hence $R(s)=12\pi\,{\rm Im}\,\Pi(s+i0)$; $W^{\mu\nu}=\frac1{2\pi}{\rm Im}\,T^{\mu\nu}$ for $q^0>0$, $x<1$.
  - **非微扰地位.** 对强子态：\cref{asm:intro-wightman}（MA0：态的完备性与谱条件）。
  - **证明.** Full (insert states; ${\rm Im}[-1/(\Delta+i0)]=\pi\delta(\Delta)$). Check: free quark loop ${\rm Im}\,\Pi=N_ce_q^2/(12\pi)$ (VF-EE-3).
  - `\uses{def:prelim-cut, asm:intro-wightman}`

* **例 `ex:prelim-vacpol` — 维数正规化中的单圈无质量流关联函数** (no tag) · v1 (moved to the end of `sec:prelim-cuts`)
  - $\Pi_0=N_ce_q^2\frac{2(D-2)}{D-1}\frac{G(1,1)}{(4\pi)^{D/2}}(-q^2-i0)^{-\varepsilon}$; $\overline{\rm MS}$: $\frac{N_ce_q^2}{12\pi^2}(\frac53-L)$, $L=\ln(-q^2/\mu^2)$; ${\rm Im}$ from $L\to\ln s-i\pi$ and from the two-particle cut agree exactly in $\varepsilon$ (VF-EE-3). Sign: $\Pi_{\rm PS}=-e^2\Pi$.
  - `\uses{def:prelim-dr-conventions, def:prelim-msbar, thm:prelim-cutting-rules, prop:prelim-optical, lem:appC-bubble}`

**Worked examples (≥ 5).** `ex:prelim-boost-scaling`, `ex:prelim-eikonal-two`, `ex:prelim-wilson-segment`, `ex:prelim-scaleless`, `ex:prelim-plus`, `ex:prelim-vacpol`.

**Tables.** `tab:prelim-symbols` 记号速查 (WRITER_SPEC_v2 §7 item 2).

**Figures.** Existing (tikz2): `fig:soft-eikonal` (owner Ch3 in v2; its caption's $n$ is the direction of the quark momentum — say so; caption mentions the Glauber region: add a pointer to `def:ir-glauber`); new: `fig:prelim-wilson-rules` (adapt `research/c_wilson/tex/c_wilson_rules.tex`, `fig:cw-rules`), `fig:prelim-lightcone` (required, refdoc S56).

**Misconception box.** M24 preview (scaleless integrals: $\frac1{\varepsilon_{\rm UV}}-\frac1{\varepsilon_{\rm IR}}$); 「单个割图是幺正的」 → only the sum over cuts (pointers `prop:method-fsi`, `lem:appO-unitarity`).

**Key citation keys.** `PeskinSchroeder1995`, `Muta2010`, `Collins1984`, `Collins2011`, `Cutkosky1960`, `Veltman1963`, `tHooftVeltman1974`, `tHooftVeltman1972`, `tHooftVeltman1972b`, `KugoOjima1979`, `CombridgeKripfganzRanft1977`, `BreitenlohnerMaison1977a`, `Larin:1993tq`, `Polyakov1980`, `BrandtNeriSato1981`, `KorchemskyRadyushkin1987`, `Hausdorff1923`, `Carlson1914`, `Titchmarsh1939`, `Muntz1914`, `Szasz1916`.

**Pending.** `lem:prelim-eikonal-identity` [PENDING-VERIFY: N26] (attribution sentence only).

---------------------------------------------------------------------------------------------------

## Chapter 4 — 费曼积分的红外结构：钳夹、幂次计数与红外安全 / Infrared structure of Feynman integrals: pinches, power counting, IR safety

`\label{ch:ir}` · `ch04_ir.tex` · **15 pp** · full (proofs in App D, E) · Part I

**Purpose.** Geometric and analytic foundation of all graphical proofs: (i) where long-distance sensitivity can arise — Landau conditions in two forms (singularities in external invariants vs trapped points of the loop-momentum contour; critic O12), pinch vs endpoint, and the correct Euclidean statement (zero-momentum lines always solve the Landau equations; finiteness comes from power counting, M29); (ii) the Coleman–Norton picture, including the scaling-limit treatment of soft lines; (iii) pinch surfaces of massless QCD ↔ reduced diagrams; (iv) power counting with normal variables (units!), the per-connection table, super-leading configurations and their cancellation, leading regions; the Glauber region and its trapping criterion; power counting is a scaling statement (E-S), its integral form is an assumption of App N; (v) KLN, Bloch–Nordsieck (and its non-abelian failure), IR safety; (vi) the method of regions with its precise status (Euclidean [R], Minkowskian [P], hidden regions), and the representation dependence of the values of divergent region integrals.

**Depends on.** Ch2 (`def:prelim-feynman-rules`, `thm:prelim-slavnov-taylor`, `def:qcd-dimreg`, `prop:qcd-soft-collinear-limits`, `def:qcd-ir-safety-informal`), Ch3 (`lem:prelim-boost`, `def:prelim-lightfront`, `def:prelim-cut`, `prop:prelim-unitarity`); App D, E.

**Box.**
- 证明了：`thm:ir-landau-alpha`、`thm:ir-landau-momentum`（[R, R_PT]，必要性；附录 D）；`prop:ir-coleman-norton`（[R, R_PT]，代数形式）；`prop:ir-power-counting`（[R, R_PT]，超表观度，E-S；附录 E）；`prop:ir-glauber-trapping`（[R, R_PT]，单圈）；`thm:ir-bn-qed`（[R, R_PT]）；`thm:ir-regions-euclid`（[R, R_PT]）。
- 给出全阶论证：`prop:ir-pinch-classification`、`prop:ir-super-leading`、`thm:ir-leading-regions`、`thm:ir-kln`、`thm:ir-safe-finite`（[A]；瓶颈：嵌套区域与积分形式的幂次计数 `asm:appN-envelope`、`asm:appN-separation`）。
- 没有证明：Landau 条件的充分性与整体围道形变（`rem:ir-landau-status`；第~24~章的预印本结果）；闵氏区域方法（`prop:ir-regions-minkowski`，[P]；“区域 = Newton 多面体下表面”在三圈有反例）；非阿贝尔 Bloch–Nordsieck 抵消（`prop:ir-bn-failure`，[V]）。

**Sections.**
1. `sec:ir-landau` Landau 方程：参数形式与动量形式 — $\alpha$-representation; analyticity criterion; envelope lemma; momentum-space criterion via Gordan; caveat (massless self-energy: momentum pinch without parameter pinch — Collins 2020 App. D1); endpoint vs pinch (`fig:landau-pinch`); the Euclidean region (`rem:ir-euclid-corners`, M29).
2. `sec:ir-coleman-norton` Coleman–Norton 图像 (`fig:coleman-norton`) — including the scaling-limit treatment of soft lines (refdoc S15.7).
3. `sec:ir-pinch` 无质量 QCD 中的钳夹面与约化图 — massless vertex and box examples (`fig:vertex-regions`); reduced diagrams for $e^+e^-$, DIS, DY (`fig:reduced-ee`, `fig:reduced-dis`, `fig:reduced-dy`, owned here; Ch10 and Ch12 refer back).
4. `sec:ir-power` 幂次计数 — normal variables; region table (`fig:momentum-regions`; caption writes $n,\bar n$ for our $n_A,n_B$ — say so); mode exponents (`fig:ir-mode-exponents`); the two units ($\lambda$ vs $\lambda_S=\lambda^2$); per-connection powers (`tab:ir-connection-powers`); superficial degree formula; super-leading configurations; leading regions; Feynman-gauge K-polarization dominance; scaling vs bound.
5. `sec:ir-glauber` Glauber 区 — definition, why eikonal fails, trapping criterion with explicit one-loop integrals (full analysis in Ch9, Ch12, App O).
6. `sec:ir-cancellation` KLN、Bloch–Nordsieck 与红外安全.
7. `sec:ir-regions` 区域方法及其地位 — prescription, 1D toy with zero-bin, value of divergent region integrals, status (Euclidean / Minkowskian / hidden regions), forward pointer to the Sudakov examples of Ch5 and to Ch24.

**Canonical statements** (in reading order).

* **定义 `def:ir-landau-setup` — Feynman 参数表示与 Symanzik 多项式** (no tag) · v1
  - **陈述.** VF-REG-1: $I(p)=\int\prod\frac{d^Dk_l}{i\pi^{D/2}}\prod_j(-D_j-i0)^{-\nu_j}=\frac{\Gamma(\nu-LD/2)}{\prod\Gamma(\nu_j)}\int d\alpha\,\delta(1-\sum_\sigma\alpha)\prod\alpha_j^{\nu_j-1}\,\mathcal U^{\nu-(L+1)D/2}(\mathcal F-i0)^{LD/2-\nu}$; $\mathcal D(\alpha,k)=\sum_j\alpha_j(m_j^2-q_j^2)$, $\mathcal U=\det A$, $\mathcal F=\mathcal U\mathcal D(\alpha,k_c)$; homogeneity degrees $L$, $L+1$.
  - `\uses{def:prelim-feynman-rules, def:qcd-dimreg}`

* **引理 `lem:ir-envelope` — 包络恒等式** (数学，无标签) · v1
  - **陈述.** For $\mathcal U\ne0$: $\partial_j(\mathcal F/\mathcal U)=-D_j(k_c)$; $\{\mathcal F=0,\alpha_j\partial_j\mathcal F=0\ \forall j\}\iff$ momentum-space Landau equations with $k=k_c(\alpha)$. Caveat (must be printed): algebraic equivalence of the *equations*, not of the *pinches* (Collins 2020 App. D1; massless self-energy, VF-REG-4 remark).
  - **证明.** Full (App D).
  - `\uses{def:ir-landau-setup}`

* **定理 `thm:ir-landau-alpha` — Landau 条件（参数形式）：解析性与红外有限性判据** [R, R_PT] · v1
  - **陈述.** (c_regions L1.) If the parametric integral is UV convergent (or DR continued) and there is no $\alpha$ in the closed simplex with $\mathcal F(\alpha,p_0)=0$ and $\alpha_j\partial_j\mathcal F(\alpha,p_0)=0$ for all $j$, then $I$ is finite at $p_0$ and extends holomorphically to a complex neighbourhood of $p_0$.
  - **证明.** Full in App D — deformation $z_j=\alpha_j[1-i\tau\eta(\partial_j\mathcal F-\sum_k\alpha_k\partial_k\mathcal F)]$ preserving the constraint and the faces, ${\rm Im}\,\mathcal F(z)=-\tau\eta V+O(\eta^3)$, $V=\sum_j\alpha_j(\partial_j\mathcal F)^2-c^2\ge0$ (VF-REG-2), compactness, dominated convergence; alternative proof via $\eta_j=\alpha_j\partial_j\mathcal F$ and homogeneity, with its caveats, as a remark in App D (refdoc S52). Numerical illustration (c_regions L6). (本定理只涉及 Feynman 积分。)
  - `\uses{def:ir-landau-setup, lem:ir-envelope}`

* **定理 `thm:ir-landau-momentum` — 动量空间的钳夹必要条件** [R, R_PT] · v1
  - **陈述.** (c_regions L3.) For real $k_0$ with on-shell set $S$ and $u_j=\partial D_j/\partial k(k_0)$: if no $\alpha\in\mathbb R^S_{\ge0}\setminus\{0\}$ satisfies $\sum_{j\in S}\alpha_ju_j=0$, there is a local deformation $k\to k+i\eta\chi(k)v$ with ${\rm Im}\,D_j>0$ for $j\in S$ and $D_j\ne0$ for $j\notin S$; i.e. a trapped point satisfies the momentum-space Landau equations with $\alpha_j\ge0$.
  - **证明.** Full — Gordan's alternative (`lem:appD-gordan`) + the exact formula $D_j(k+i\eta\chi v)=D_j(k)-\eta^2\chi^2(v'_j)^2+2i\eta\chi q_j\cdot v'_j$. Remark (pointer, Ch24): the geometric part of Collins' 2020 theorem is Gordan's alternative, with a constructive min-norm direction [PENDING-VERIFY: N02]. (本定理只涉及 Feynman 积分。)
  - `\uses{def:ir-landau-setup, lem:appD-gordan}`

* **注 `rem:ir-landau-status` — Landau 条件的充分性与整体形变** [A] · v1
  - **陈述.** Sufficiency (Landau ⇒ trapped) and the gluing of local deformations into a global one; second-type singularities ($\mathcal U=0$) excluded.
  - **地位与缺口.** Complete proof only in the preprint `Collins:2020euz` (arXiv only as of 2026-10; a sign condition and quadratic denominators are assumed there; survey item 4; Ch24 discusses it) [PENDING-VERIFY: A08]; Collins 2011 §5.4.3 (p. 110): textbook proofs incomplete; `EdenEtAl1966` p. 48 "plausibility arguments"; the proof gap of `ColemanNorton1965` (momentum vs parameter pinch) as identified in `Collins:2020euz` [PENDING-VERIFY: E14]; heuristic textbook derivations (E15 — not printed unless verified); `Muhlbauer:2020kut`, `Pham:2011SingInt` for the topological theory.
  - `\uses{thm:ir-landau-momentum, thm:ir-landau-alpha}`

* **注 `rem:ir-euclid-corners` — 欧氏区的 Landau 解与红外有限性** (no tag) · refdoc S15.1 (misconception M29)
  - In Euclidean non-exceptional kinematics, sets of zero-momentum massless lines always solve the Landau equations (for the off-shell triangle: $\mathcal F=m^2\alpha_0(\alpha_1+\alpha_2)+Q^2\alpha_1\alpha_2$ vanishes only at the simplex corners, VF-REF-17); finiteness follows from IR power counting (forward pointer `thm:ee-euclid-ir`, IR degree $d=A+\frac12A_q\ge2$); with massive lines $\mathcal F>0$ and there is no solution. The statement 「欧氏区没有 Landau 解」 is false.
  - `\uses{def:ir-landau-setup, thm:ir-landau-alpha}`

* **例 `ex:ir-euclid-triangle` — 离壳三角图的 Symanzik 多项式** (no tag) · new
  - Compute $\mathcal U$, $\mathcal F$ for the scalar triangle with two off-shell legs $p_i^2=-m^2$ and $(p_1+p_2)^2=-Q^2$; locate the Landau solutions at the corners; show by direct power counting that the corner regions are integrable (VF-REF-17); App D `sec:appD-alpha` gives the details.
  - `\uses{rem:ir-euclid-corners}`

* **定义 `def:ir-pinch-surface` — 钳夹面、内禀坐标与法坐标** (no tag) · v1
  - `\uses{thm:ir-landau-momentum}`

* **命题 `prop:ir-coleman-norton` — Coleman–Norton 定理（代数形式）** [R, R_PT] · v1 (+ refdoc S15.7)
  - **陈述.** A real solution with $\alpha_j\ge0$ ⇔ a classical space-time process: $\Delta x_j=\alpha_jq_j$ on on-shell lines; loop equations ⇔ consistent vertex positions; massless lines move at light speed; zero-momentum lines connect arbitrary points. Scaling-limit treatment of soft lines (refdoc S15.7): a soft line is the limit $\lambda\to0$ of lines of momentum $\lambda q$, whose $\alpha$ scale as $1/\lambda$ so that $\Delta x$ stays finite; the picture for DY initial- and final-state soft gluons (active and spectator poles on opposite sides) is drawn in Ch12 with `fig:glauber-exchange` (pointer).
  - **证明.** Full (0.5 p; App D `sec:appD-cn`). Remark: the stronger claim "trapped ⇔ classically realizable" needs the converse of `thm:ir-landau-momentum` and is [A] (`ColemanNorton1965`; gaps in the proof but not in the result: `Collins:2020euz`); momentum-space version including Wilson lines: Ch24 (pointer) [PENDING-VERIFY: N03]. `fig:coleman-norton`. (本命题只涉及 Feynman 积分。)
  - `\uses{thm:ir-landau-momentum, def:ir-pinch-surface}`

* **命题 `prop:ir-pinch-classification` — 钳夹面与约化图** [A] · v1
  - **陈述.** In massless QCD every pinch surface of a cut graph for $e^+e^-\to$ hadrons corresponds to a reduced diagram: one hard vertex, jets of collinear on-shell lines along light-like directions, a soft subgraph of zero-momentum lines; for DIS, SIA, DY add incoming target jets.
  - **证明.** Sketch via `prop:ir-coleman-norton`. Literature: `Sterman1978a`, `Sterman1978b`, `LibbySterman1978a`, `Sterman1993`, Collins 2011 ch. 5.
  - **地位与缺口.** The classification uses the converse of the Landau criterion (sufficiency, `rem:ir-landau-status`) and the completeness of the enumeration of pinch surfaces for general graphs; both are arguments (E-S), not proofs.
  - `\uses{prop:ir-coleman-norton, def:ir-pinch-surface}`

* **定义 `def:ir-scalings` — 区域标度** (no tag) · v1
  - **陈述.** VF-REG-7 in $(k^+,k^-,k_T)$ with $\lambda=m/Q$: hard $Q(1,1,1)$; $A$-collinear $Q(1,\lambda^2,\lambda)$; $B$-collinear $Q(\lambda^2,1,\lambda)$; soft $Q(\lambda,\lambda,\lambda)$; ultrasoft $Q(\lambda^2,\lambda^2,\lambda^2)$; Glauber $|k^+k^-|\ll k_T^2$, typically $Q(\lambda^2,\lambda^2,\lambda)$; eikonal errors $O(\lambda)$, $O(\lambda^2)$, $O(1)$ for soft, ultrasoft, Glauber (c_regions P3). **Units:** Sterman's $\omega$ is the power of $\lambda_S=\lambda^2$; the power of $\lambda$ is $2\omega$. Libby–Sterman's "soft" = ultrasoft here; TMD factorization (Ch14) uses the soft scaling. `fig:ir-mode-exponents` shows the modes in exponent space (Glauber below the on-shell plane).
  - `\uses{def:prelim-lightfront}`

* **命题 `prop:ir-power-counting` — 超表观红外发散度** [R, R_PT] · v1
  - **陈述.** For a reduced diagram $R$ in Feynman gauge (Sterman units; c_regions P2, VF-REG-8): $$\omega(R)=\sum_J\tfrac12\big(f^g_J+t_J+2u_J+2f^b_J-e_J\big)+\tfrac12\sum_Js^q_J+b_{S\to H}+\tfrac32f_{S\to H},$$ $f^g_J$ ($f^b_J$) quark lines to $H$ through good (bad) components, $t_J$ transverse and $u_J$ "−" polarized gluons to $H$ (scalar-polarized $A^+$-type gluons not counted), $e_J=1$ (amplitude with one external parton) or $2$ (forward/target jet, or final-state jet of a cut graph), $s^q_J$ soft quarks attached to $J$, $b_{S\to H}$, $f_{S\to H}$ soft lines attached to $H$. The homogeneous integral scales as $\lambda_S^\omega$ up to logarithms. Per-connection powers in $\lambda$ units: `tab:ir-connection-powers`.
  - **证明.** Full (App E: boost + dimension argument; `prop:appE-degree`). Checks table (c_regions P7). Remark (refdoc S15.5): this is a scaling statement (E-S); superficial degree only; nested sub-regions → `thm:ir-leading-regions` [A]. (本命题只涉及 Feynman 积分。)
  - `\uses{def:ir-scalings, lem:prelim-boost, def:prelim-feynman-rules, prop:appE-degree}`

* **命题 `prop:ir-super-leading` — 超领头构型及其相消** [A] · refdoc S15.2 (corrects ERR-S4 of the literature-style presentations)
  - **陈述.** In $\lambda$ units, for a jet $J$ with $e_J=2$ (target jet or final-state jet of a cut graph), the configurations with no good-quark and no transverse-gluon connection, $(n_F,n_T)=(0,0)$ (only scalar-polarized gluons), have $p_J=-2$, and those with $(n_F,n_T)=(0,1)$ have $p_J=-1$: they are super-leading. In gauge-invariant sums over graphs these contributions cancel (Ward identity + colour neutrality; `CollinsSoperSterman1989` §8.6); their $O(\lambda)$ and $O(\lambda^2)$ remainders are leading and combine into the field strength $G^{+j}$ through $k^+A^j-k^jA^+$. For a gluon as the only active parton, $k\cdot H=0$ and the G term $\propto k^+A^j-k^jA^+$ is leading. "$n_T$ transverse gluons" is not a gauge-invariant bookkeeping in the gluon channel.
  - **证明.** Sketch (power counting with `tab:ir-connection-powers`; Ward identities `thm:prelim-slavnov-taylor`); cross-reference to the Grammer–Yennie exception `prop:method-gy-suppression` (Ch9, pointer).
  - **地位与缺口.** The cancellation is shown in the literature for the relevant sums of graphs (E-S level); a general all-order integral-norm statement is part of `asm:appN-envelope` and `asm:appN-ward-product`.
  - `\uses{prop:ir-power-counting, thm:prelim-slavnov-taylor, asm:appN-envelope, asm:appN-ward-product}`

* **注 `rem:ir-scaling-vs-bound` — 标度陈述与积分界** (no tag) · refdoc S15.5
  - `prop:ir-power-counting` and `thm:ir-leading-regions` are scaling statements (E-S); the integral-norm versions needed for a proof are `asm:appN-envelope` (power-counting envelopes) and `asm:appN-separation` (virtuality bounds) of App N.
  - `\uses{prop:ir-power-counting}`

* **定理 `thm:ir-leading-regions` — 领头区域** [A] · v1
  - **陈述.** In Feynman gauge for $e^+e^-\to$ hadrons, DIS, SIA, DY: $\omega=0$ regions are exactly those with (i) each jet attached to $H$ (and $H^*$) by one physical parton on each side (good quark component or transverse gluon) plus any number of scalar-polarized collinear gluons; (ii) soft subgraph attached only to jets and only by gluons; (iii) nothing soft attached to $H$; for DY additionally Glauber subregions of spectator–spectator exchanges. Super-leading configurations cancel (`prop:ir-super-leading`).
  - **证明.** Sketch. Literature: `Sterman1978a`, `LibbySterman1978a`, `LibbySterman1978b`, Collins 2011 §5.8–5.11 (§5.9.2 leading-region rules; eqs. (5.75)–(5.79)), `CollinsSoperSterman1989` §8.7, `Sterman:1995fz` §§2.3–2.4 (eqs. (60)–(65); eq. (63) presupposes connected $S$, use eq. (64)).
  - **地位与缺口.** Nested regions (no Minkowskian analogue of Weinberg's theorem); in Feynman gauge extra disconnected hard scatterings cancel only after a sum over graphs (`Labastida:1984gy`; Collins 2011 §14.4.8); the statement is E-S; the integral form is `asm:appN-envelope`, `asm:appN-separation`. (本定理只涉及部分子态；其强子版本即 \cref{asm:intro-bridge}(Br1)。)
  - `\uses{prop:ir-pinch-classification, prop:ir-power-counting, prop:ir-super-leading, thm:prelim-slavnov-taylor, asm:appN-envelope, asm:appN-separation}`

* **例 `ex:ir-vertex` — 单圈无质量顶点** (no tag) · v1
  - (VF-REG-4, REG-6.) $\mathcal F=-Q^2\alpha_1\alpha_2$; Landau set: edges $\{\alpha_2=0\}$ ($k=xp_1$), $\{\alpha_1=0\}$, soft corner, soft-quark corners; no hard pinch for $Q^2\ne0$ (the "hard point" is the absence of a pinch); Cayley-matrix check; Coleman–Norton pictures; collinear $k^-$ integral $\int dk^-[D_0D_1D_2]^{-1}=\frac{2\pi i}{2p_1^+}\frac{1}{k_T^2(xQ^2-k_T^2/(1-x))}$; logarithmic $k_T$ scaling; normal-coordinate exponent $p=4-2-2=0$. `fig:vertex-regions`.
  - `\uses{thm:ir-landau-alpha, prop:ir-coleman-norton, prop:ir-power-counting}`

* **例 `ex:ir-k-dominance` — Feynman 规范下共线区域的标量极化主导** (no tag) · v1
  - $J\cdot H=(J^+/k^+)(k\cdot H)+O(\lambda^2)$ for the one-loop vertex; $J_T\cdot H_T=0$ in $D=4$ for back-to-back light-like quarks (VF-REG-8 remark; c_regions P5).
  - `\uses{prop:ir-power-counting}`

* **例 `ex:ir-real-emission` — $e^+e^-\to q\bar qg$ 的共线区** (no tag) · v1
  - Gluon collinear to the quark: squared numerator $\sim\lambda^2$, propagators $\lambda^{-4}$, phase space $\lambda^2$ ⇒ logarithmic (c_regions P4); $\sum|M|^2\propto8(x_1^2+x_2^2)/((1-x_1)(1-x_2))$ (VF-EE-5); compare the tree-level limits of `prop:qcd-soft-collinear-limits`.
  - `\uses{prop:ir-power-counting, prop:qcd-soft-collinear-limits}`

* **定义 `def:ir-glauber` — Glauber 区** (no tag) · v1
  - **陈述.** $|k^+k^-|\ll k_T^2$; $(p_A+k)^2\simeq2p_A^+k^--2p_{A,T}\cdot k_T-k_T^2$ — the $k_T^2$ is not negligible, the eikonal approximation fails (error $O(1)$, VF-WL-11); couples as $A^-$ to $A$-lines and $A^+$ to $B$-lines with $1/k_T^2$ ("Coulomb"). Remark (refdoc E6): a Glauber pinch can also arise between terms of the light-cone-ordered representation (inter-term pinches), which obstruct the Ward identities; a deformation of a single light-cone component does not leave the region $G_\delta=\{|k^+k^-|\le\delta k_T^2\}$ (forward pointers `rem:method-two-component`, App O).
  - `\uses{def:ir-scalings}`

* **命题 `prop:ir-glauber-trapping` — 单圈 Glauber 区的钳夹判据** [R, R_PT] · v1
  - **陈述.** (c_regions §2.6, VF-REG-9.) For the one-loop vertex each light-cone integral sees one pole in the Glauber region: not trapped, contour can be moved to $|k^\pm|\sim k_T$; with an incoming and an outgoing $A$-collinear line carrying $k$ the poles $k^-=-k_T^2/(2p_A^+)+i0$, $k^-=k_T^2/(2p_{A'}^+)-i0$ pinch at $|k^-|\sim k_T^2/p^+$; the exact integral is finite, $2\pi i/[2k_T^2(p_A^++p_{A'}^+)]$, while the eikonal version diverges.
  - **证明.** Full (residues). Forward pointers: `prop:method-glauber-deformation` (Ch9), Ch12. (本命题只涉及 Feynman 积分。)
  - `\uses{def:ir-glauber, thm:ir-landau-momentum}`

* **定理 `thm:ir-bn-qed` — QED 中的 Bloch–Nordsieck 定理** [R, R_PT] · v1
  - **陈述.** For QED with massive charged fermions, soft-photon divergences cancel in cross sections inclusive over photons below an energy resolution; exponentiation (YFS).
  - **证明.** Sketch; `BlochNordsieck1937`, `YennieFrautschiSuura1961`, `Weinberg1965`. (本定理只涉及微扰 QED。)
  - `% uses: none`

* **定理 `thm:ir-kln` — KLN 定理** [A] · v1
  - **陈述.** Transition probabilities summed over degenerate initial *and* final states are IR finite at every order.
  - **证明.** Sketch; `Kinoshita1962`, `LeeNauenberg1964`, `Sterman:1976jh`.
  - **地位与缺口.** A one-sided sum suffices but generically requires forward-scattering and disconnected contributions (`Frye:2018xjj`); initial-state collinear singularities of hadron collisions are factorized into PDFs, not cancelled (M8); the general proof is an all-order argument.
  - `\uses{prop:prelim-unitarity, thm:ir-bn-qed}`

* **命题 `prop:ir-bn-failure` — 有色初态时非阿贝尔 Bloch–Nordsieck 抵消的失效** [V] · v1
  - **陈述.** Two massive coloured initial quarks, colour averaged: non-leading IR divergences from two soft gluons do not cancel at two loops; the non-cancelling terms are power suppressed at high energy.
  - **证明.** Sketch (structure: Coulomb/Glauber phase with colour matrices).
  - **地位与缺口.** Evidence: explicit two-loop calculation (`DoriaFrenkelTaylor1980`; confirmed by `DiLietoEtAl1981`, `Andrasi:1980qw`); power suppression (`Frenkel:1983di` to $O(g^4)$; "higher twist" `Catani:1985xt`); CSS 1989 §10.2: relative order $m^4/s^2$ in DY. The premises differ from those of the DY theorem (massive coloured initial partons at fixed colour vs massless partons in colour-singlet hadrons): forward pointer `rem:dy-dft-premises`. Survey item 3.
  - `\uses{thm:ir-bn-qed, def:prelim-feynman-rules}`

* **定义 `def:ir-safe` — 红外安全可观测量** (no tag) · v1
  - **陈述.** Weights continuous under soft emission and collinear splitting (precise version of `def:qcd-ir-safety-informal`); Sterman–Weinberg cones as an example (Ch16).
  - `\uses{def:qcd-ir-safety-informal}`

* **定理 `thm:ir-safe-finite` — 红外安全可观测量的有限性** [A] · v1
  - **陈述.** IR-safe $e^+e^-$ observables are finite order by order in massless PT.
  - **证明.** Sketch; `Sterman1978a`, `Sterman1978b`, `Sterman:1979uw`, `StermanWeinberg1977`, `Ore:1979ry`. (The total cross section is proved separately and at [R] in Ch6.)
  - **地位与缺口.** Rests on the leading-region analysis (`thm:ir-leading-regions`, [A]) and on the cancellation of final-state singularities in the sum over cuts (E-S level).
  - `\uses{def:ir-safe, thm:ir-leading-regions, prop:prelim-unitarity}`

* **定义 `def:ir-regions` — 区域方法** (no tag) · v1
  - **陈述.** Beneke–Smirnov prescription: choose regions, Taylor expand, integrate over the full domain in DR (with analytic regulators where needed), drop scaleless integrals, sum; Jantzen's four conditions (domains cover, expansions commute, all integrals regularized, absolute convergence) (c_regions §3.3).
  - `\uses{def:qcd-dimreg, lem:prelim-scaleless}`

* **定理 `thm:ir-regions-euclid` — 欧氏极限的渐近展开** [R, R_PT] · v1
  - **陈述.** For large Euclidean external momenta / large masses, expansion by regions coincides with the (proven) expansion by subgraphs.
  - **证明.** Cite `Smirnov:1990rz`, `Smirnov2002`, `Gorishnii1989`. (本定理只涉及 Feynman 积分。)
  - `\uses{def:ir-regions}`

* **命题 `prop:ir-regions-minkowski` — Minkowski 极限下区域方法的地位** [P] · v1
  - **陈述.** No general proof for threshold, Sudakov, Regge, on-shell expansions; partial results: `Jantzen2011` (partition of the domain, conditions; massive Sudakov), `Pak:2010pt` (Newton polytope), `Jantzen:2012mw`, `Semenova:2018cwy`, `Gardi:2022khw`, `Ma:2023hrt`. Even the off-shell Sudakov example (four facets) is not covered by a complete proof (verified exactly at one loop, `ex:sudakov-offshell`, pointer).
  - **地位与缺口.** The facet prescription "regions = lower facets of the Newton polytope" fails as a general statement in Minkowski kinematics: three-loop non-planar $2\to2$ counterexamples with hidden regions (`Gardi:2024axt`; Ch24) — the prescription is [V] in general, the method with a correctly completed set of regions remains unproven ([P]/[C]); SCET mode lists inherit this caveat. Attributions per A10 [PENDING-VERIFY: A10].
  - `\uses{def:ir-regions, thm:ir-regions-euclid}`

* **注 `rem:ir-regions-values` — 发散区域积分的值依赖于表示** (no tag) · refdoc S15.6
  - The values of divergent region integrals depend on the representation (e.g. the zero-bin $\int_0^\infty d\sigma/\sigma^{1+\varepsilon}$ in light-cone variables vs a parametric $\int_0^1$, which gives $-1/\varepsilon$); Collins subtraction terms are absolutely convergent iterated integrals; link to `asm:appN-values` and `prop:ir-regions-minkowski`.
  - `\uses{def:ir-regions}`

* **例 `ex:ir-regions-toy` — 一维玩具积分与零区减除** (no tag) · v1
  - (VF-REG-13.) $I=\int_0^\infty dk/[(k+m)(k+M)]$; with $k^{-e}$: $T_s+T_h\to\ln(M/m)/M$, $T_sT_h=0$; with cutoffs the overlap must be subtracted (zero-bin).
  - `\uses{def:ir-regions, rem:ir-regions-values}`

**Worked examples (≥ 5).** `ex:ir-euclid-triangle`, `ex:ir-vertex`, `ex:ir-k-dominance`, `ex:ir-real-emission`, `ex:ir-regions-toy`.

**Tables.** `tab:ir-connection-powers` (refdoc S15.3): power of $\lambda$ per connection — good quark +1, bad quark +2, transverse gluon +1, scalar (K) gluon 0, "−" gluon +2; soft gluon→jet 0, soft quark→jet +1, soft gluon→$H$ +2, soft quark→$H$ +3; super-leading rows $(n_F,n_T)=(0,0)$: $p_J=-2$, $(0,1)$: $p_J=-1$ for $e_J=2$; unit: powers of $\lambda$, $k_T\sim\lambda Q$.

**Figures.** Existing (tikz2): `fig:landau-pinch`, `fig:vertex-regions`, `fig:coleman-norton`, `fig:reduced-ee`, `fig:reduced-dis`, `fig:reduced-dy`, `fig:momentum-regions`; new (required, refdoc S56): `fig:ir-mode-exponents`; optional: `fig:ir-landau-simplex` (adapt `research/c_regions/landau.tex`).

**Misconception box.** M8, M9 (first statement), M19, M20, **M29**; critic C5, C15; O11, O12.

**Key citation keys.** `Landau1959`, `ColemanNorton1965`, `EdenEtAl1966`, `Pham:2011SingInt`, `Collins:2020euz`, `Muhlbauer:2020kut`, `Fevola:2023kaw`, `Gordan1873`, `Nakanishi:1959jzx`, `Cutkosky1960`, `Sterman1978a`, `Sterman1978b`, `LibbySterman1978a`, `LibbySterman1978b`, `CollinsSterman1981`, `Sterman:1995fz`, `Sterman1993`, `Collins2011`, `CollinsSoperSterman1989`, `Labastida:1984gy`, `Weinberg1960`, `Hahn:1968HZ`, `Kinoshita1962`, `LeeNauenberg1964`, `Frye:2018xjj`, `Sterman:1976jh`, `BlochNordsieck1937`, `YennieFrautschiSuura1961`, `Weinberg1965`, `DoriaFrenkelTaylor1980`, `DiLietoEtAl1981`, `Andrasi:1980qw`, `Frenkel:1983di`, `Catani:1985xt`, `StermanWeinberg1977`, `Sterman:1979uw`, `Ore:1979ry`, `BenekeSmirnov1998`, `Smirnov:1990rz`, `Smirnov2002`, `Smirnov2012`, `Gorishnii1989`, `Jantzen2011`, `Pak:2010pt`, `Jantzen:2012mw`, `Semenova:2018cwy`, `Gardi:2022khw`, `Gardi:2024axt`, `Ma:2023hrt`, `Ananthanarayan:2018tog`, `LeePomeransky2013`.

**Pending.** [PENDING-VERIFY: N02, N03, E14, E15, A08, A10] (wording of the pointers to Ch24 and of the status remarks).

---------------------------------------------------------------------------------------------------

## Chapter 5 — Sudakov 形状因子与振幅的红外结构 / The Sudakov form factor and the infrared structure of amplitudes

`\label{ch:sudakov}` · `ch05_sudakov.tex` · **14 pp** · full · Part I

**Purpose.** The simplest all-order factorization theorem, with every tool of the general method in its simplest setting and no PDFs: one-loop form factor exact in $\varepsilon$; regions (off-shell, with the exact closed form; massive exchange needs analytic regulators); the consistency argument fixing the region coefficients; factorization $F=H\cdot J\cdot J/S$ with Wilson-line definitions; Ward identities → Wilson lines; $K+G$ evolution; cusp anomalous dimension; exponentiation (incl. webs); IR poles of multi-leg amplitudes (dipole formula and its three-loop failure); Coulomb phases; strict collinear factorization of amplitudes (timelike) and a preview of the spacelike violation.

**Depends on.** Ch2 (`def:prelim-feynman-rules`, `def:prelim-msbar`, `thm:prelim-slavnov-taylor`, `prop:qcd-rge`), Ch3 (Wilson lines, `lem:prelim-scaleless`), Ch4 (regions, power counting, leading regions).

**Box.**
- 证明了：`prop:sudakov-oneloop`（[R, R_PT]，精确到 $\varepsilon$ 的所有阶）；`prop:sudakov-coulomb`（[R, R_PT]，单圈）；`prop:sudakov-kg` 与 `prop:sudakov-webs` 的单圈/$O(g^2)$ 内容（[R]）。
- 给出全阶论证：`thm:sudakov-factorization`（[A]；减除在 Collins 2011 第 10 章中对此例完整）、`prop:sudakov-kg`、`cor:sudakov-exponentiation`、`prop:sudakov-webs`、`thm:sudakov-ir-poles`、`prop:sudakov-amplitude-factorization`（[A]）。
- 没有证明：偶极子公式作为全阶公式（`prop:sudakov-dipole-violation`，[V]）；类空严格共线因子化（`rem:sudakov-spacelike`，[V]，见第~18~章）。

**Sections.**
1. `sec:sudakov-oneloop` 一圈形状因子 — exact in $\varepsilon$; UV/IR bookkeeping; timelike continuation; $\pi^2$ enhancement.
2. `sec:sudakov-regions` 区域分析 — on-shell massless (= hard region), off-shell (four regions, exact closed form, consistency argument), massive exchange (analytic regulator; collinear-anomaly analogue); LL coefficients (`fig:sudakov-ff`; its caption's $n,\bar n$ are our $n_A,n_B$ — say so).
3. `sec:sudakov-factorization` 全阶因子化 $F=H\cdot J\cdot J/S$ — reduced diagrams, Ward identities, Wilson-line definitions of jet and soft functions; one-loop subtraction structure (forward pointer `ex:method-sudakov-subtraction`, `prop:appN-triangle-exact`) (`fig:sudakov-hjjs`).
4. `sec:sudakov-evolution` $K+G$ 演化、cusp 反常维度与指数化 (`fig:sudakov-cusp`).
5. `sec:sudakov-multileg` 多腿振幅的红外极点 — $\mathbf Z$ factorization; dipole formula; three-loop non-dipole terms; webs (`fig:sudakov-dipole`).
6. `sec:sudakov-collinear` 振幅的共线因子化与 Coulomb 相位 — timelike strict collinear factorization (Feige–Schwartz); Coulomb phases; spacelike preview (full in Ch18). Pointer to Ch23 (heavy–light Sudakov form factor; off-light-cone soft functions as HQET form factors).

**Canonical statements** (in reading order).

* **定义 `def:sudakov-ff` — 夸克形状因子** (no tag) · v1
  - **陈述.** $\bar u(p_2)\Gamma^\mu u(p_1)$ for massless on-shell quarks: $\Gamma^\mu=F(q^2)\gamma^\mu$ (chirality); spacelike $Q^2=-q^2>0$; timelike $q^2=s+i0$.
  - `\uses{def:prelim-feynman-rules}`

* **命题 `prop:sudakov-oneloop` — 一圈形状因子（精确到 $\varepsilon$ 的所有阶）** [R, R_PT] · v1
  - **陈述.** VF-SUD-1: $$F=1+\frac{\alpha_s}{4\pi}C_F\Big(\frac{\mu^2}{Q^2}\Big)^\varepsilon\frac{e^{\varepsilon\gamma_E}\Gamma(1+\varepsilon)\Gamma^2(1-\varepsilon)}{\Gamma(1-2\varepsilon)}\Big[-\frac{2-\varepsilon+2\varepsilon^2}{\varepsilon^2(1-2\varepsilon)}\Big]=1+\frac{\alpha_s}{4\pi}C_F\Big(\frac{\mu^2}{Q^2}\Big)^\varepsilon\Big[-\frac2{\varepsilon^2}-\frac3\varepsilon-8+\zeta_2+\varepsilon\big(-16+\tfrac32\zeta_2+\tfrac{14}3\zeta_3\big)+O(\varepsilon^2)\Big];$$ all poles infrared ($Z_1=Z_2$; scaleless external self-energies, `ex:prelim-scaleless`); timelike: $(\mu^2/Q^2)^\varepsilon\to(\mu^2/s)^\varepsilon e^{i\pi\varepsilon}$, $2{\rm Re}F^{(1)}=\frac{\alpha_sC_F}{2\pi}(\frac{\mu^2}{s})^\varepsilon\cos(\pi\varepsilon)f(\varepsilon)$, timelike exceeds spacelike by $\frac{\alpha_sC_F}{2\pi}\pi^2$ (VF-SUD-2).
  - **证明.** Full (Feynman parameters; 1 p) — App G and App C (`sec:appC-formfactor`); checks: c_dis, c_ee, c_dy (MVV 2005 through $\varepsilon^4$), c_scet. (本命题只涉及部分子态。)
  - `\uses{def:sudakov-ff, def:qcd-dimreg, def:prelim-dr-conventions, lem:prelim-scaleless, ex:prelim-scaleless}`

* **例 `ex:sudakov-onshell-hard` — 在壳无质量形状因子 = 硬区** (no tag) · v1
  - (VF-REG-10/c_regions §3.7.) With $\mathcal F=Q^2\alpha_1\alpha_2$ the integral is its hard region; IR poles = UV poles of scaleless low-energy regions ($1/\varepsilon_{\rm UV}-1/\varepsilon_{\rm IR}=0$).
  - `\uses{prop:sudakov-oneloop, def:ir-regions}`

* **例 `ex:sudakov-offshell` — 离壳 Sudakov 三角形的区域展开** (no tag) · v1 (+ refdoc S16.2)
  - (VF-REG-10; `fig:sudakov-ff`.) Regions (each $\times1/Q^2$): $H=(\frac{\mu^2}{Q^2})^\varepsilon e^{\varepsilon\gamma_E}\frac{\Gamma(1+\varepsilon)\Gamma^2(-\varepsilon)}{\Gamma(1-2\varepsilon)}$, $C_{1,2}=-(\frac{\mu^2}{P^2})^\varepsilon e^{\varepsilon\gamma_E}\frac{\Gamma(1+\varepsilon)\Gamma^2(-\varepsilon)}{\Gamma(1-2\varepsilon)}$, $S=-(\frac{\mu^2Q^2}{P^4})^\varepsilon e^{\varepsilon\gamma_E}\Gamma(1+\varepsilon)\Gamma(\varepsilon)\Gamma(-\varepsilon)$, soft and Glauber zero; sum $=\frac1{Q^2}[\ln^2\frac{Q^2}{P^2}+\frac{\pi^2}3]+O(\varepsilon)$; poles cancel ($1-2+1$). **Exact result (refdoc S16.2; VF-REF-2):** $Q^2I=\Phi^{(1)}(t,t)=[4{\rm Li}_2(-\rho t)+\ln^2(\rho t)+\frac{\pi^2}3]/\sqrt{1-4t}$, $\rho=\frac2{1-2t+\sqrt{1-4t}}$, with expansion $L^2+\frac{\pi^2}3+t(2L^2-4L-4+\frac{2\pi^2}3)+t^2(6L^2-14L-11+2\pi^2)+O(t^3L^2)$, $L=\ln\frac{Q^2}{m^2}$, $t=\frac{m^2}{Q^2}$ (binding sign convention, refdoc §2.5 item 2). Literature: `BecherBroggioFerroglia2015` §2.2 (eqs. (2.39)–(2.44)), method `BenekeSmirnov1998`, closed form `UsyukinaDavydychev1993a`. Normalization note: $q^2C_0=Q^2I$ (VF-REG-14). Forward pointers: the Collins subtraction terms of the same triangle and their exact remainder (`ex:method-sudakov-subtraction`, `prop:appN-triangle-exact`) [PENDING-VERIFY: N12]; `fig:method-hasse` (Ch9) shows the nine two-loop regions (pointer only).
  - `\uses{def:ir-regions, prop:ir-regions-minkowski}`

* **例 `ex:sudakov-massive` — 有质量交换：需要解析正规化** (no tag) · v1
  - (VF-REG-11.) Pure DR leaves $\int dx/x$ unregulated (rapidity divergence); with analytic regulators $H+C_1+C_2=\frac1{Q^2}[\frac12\ln^2\frac{Q^2}{M^2}+\frac{\pi^2}3]$ (`Jantzen2011` eqs. (6.26)–(6.30); `BecherBroggioFerroglia2015` eqs. (2.50)–(2.52)); the large logarithm reappears through the cancellation of $1/\delta$ poles — analogue of the collinear anomaly (`BecherNeubert2011`). Contrast: on-shell *massive legs* with a massless gluon are DR-regulated (VF-REG-12; corrects critic O11).
  - `\uses{def:ir-regions}`

* **例 `ex:sudakov-ll` — 双对数系数** (no tag) · v1
  - (VF-SUD-4.) $\delta F_{\rm LL}=-\frac{\alpha}{2\pi}\ln\frac{Q^2}{P_1^2}\ln\frac{Q^2}{P_2^2}$ (off-shell), $-\frac{\alpha}{4\pi}\ln^2\frac{Q^2}{M^2}$ (massive photon) — Sudakov's and Jackiw's coefficients as quoted in `Collins:1989bt`; QCD: $\alpha\to C_F\alpha_s$.
  - `\uses{ex:sudakov-offshell, ex:sudakov-massive}`

* **注 `rem:sudakov-consistency` — 一致性论证：单标度结构、$\mu$ 无关性与极点相消** (no tag) · refdoc S16.1 (T5)
  - Single-scale structure of each region + $\mu$-independence + pole cancellation fix the $1/\varepsilon^2$ coefficients $(c_h,c_1,c_2,c_s)=(1,-1,-1,1)$ and the double logarithm $\frac12[a^2-2b^2+(2b-a)^2]=(a-b)^2$, $a=\ln\frac{\mu^2}{Q^2}$, $b=\ln\frac{\mu^2}{m^2}$; the constant $\frac{\pi^2}3$ is not fixed by this argument (it comes from the explicit integrals); the argument presupposes the region expansion (unproven in this Minkowskian multi-facet case, `prop:ir-regions-minkowski`).
  - `\uses{ex:sudakov-offshell}`

* **定理 `thm:sudakov-factorization` — Sudakov 形状因子的全阶因子化** [A] · v1
  - **陈述.** At leading power the (IR-regulated) form factor factorizes as $F=H(Q^2/\mu^2)\,J_1\,J_2/S$ (or in Collins' form with rapidity variables), $J_i$ = matrix elements of a quark field and a Wilson line along the opposite direction, $S$ = vacuum expectation of two Wilson lines (cusp).
  - **证明.** Sketch using only Ch2–Ch4 and the literature (no forward dependency): (1) leading regions (`thm:ir-leading-regions`, `prop:ir-power-counting`); (2) collinear and soft approximations in their simplest form (one hard vertex, two back-to-back jets); (3) Ward identities → Wilson lines: abelian case shown explicitly from the elementary identities (VF-WL-6) and the eikonal identity (`lem:prelim-eikonal-identity`, `prop:prelim-wilson-rules`); the non-abelian all-order step is cited from Collins 2011 §10.8 (with `thm:prelim-slavnov-taylor`); (4) subtractions: the one-loop region structure (`ex:sudakov-offshell`, zero-bin overlaps scaleless in DR); all orders cited from Collins 2011 §10.3 (p. 321) and §10.8 (p. 359). Forward pointers only: `lem:method-ward-abelian`, `lem:method-ward-multi`, `thm:method-subtraction`, `ex:method-sudakov-subtraction` (Ch9). Literature: `Mueller:1979ih`, `Collins:1980ih`, `Sen:1981sd`, `Sen1983`, `Collins:1989bt`, `Magnea:1990zb`, `Korchemsky1989`, `Akhoury1979`.
  - **地位与缺口.** General non-abelian Ward-identity step outlined; the subtraction proof is complete in Collins 2011 ch. 10 for this case at the level of rigour of that chapter — whether it establishes integral-norm (E-N) bounds or scaling statements (E-S) is open item S63-12 [PENDING-VERIFY: S63-12]; the bottleneck of the [A] grade is therefore `asm:appN-collins` (precise conditional form: `thm:appN-subtraction`, App N). (本定理只涉及部分子态。)
  - `\uses{thm:ir-leading-regions, prop:ir-power-counting, lem:prelim-eikonal-identity, prop:prelim-wilson-rules, def:prelim-wilson, thm:prelim-slavnov-taylor, prop:sudakov-oneloop, ex:sudakov-offshell, asm:appN-collins}`

* **定义 `def:sudakov-cusp` — cusp 反常维度** (no tag) · v1
  - **陈述.** VF-CONV-23: $\Gamma_{\rm cusp}=\sum_n(\frac{\alpha_s}{4\pi})^{n+1}\Gamma_n$, $\Gamma_0=4C_F$, $\Gamma_1=4C_F[(\frac{67}9-\frac{\pi^2}3)C_A-\frac{20}9T_Fn_f]$ (the arXiv source of Becher–Schwartz App. A has a spurious $C_F$, c_scet §6 item 10; VF-SCET-16) [PENDING-VERIFY: E23 — App Q candidate]; Collins' $\gamma_K=2\Gamma_{\rm cusp}$. One-loop cusp of two timelike Wilson lines with cusp angle $\beta$: $\Gamma(\beta)=\frac{\alpha_sC_F}\pi(\beta\coth\beta-1)$ (VF-CONV-23; the $-1$ is the line self-energy, $\Gamma(0)=0$; App B `prop:appB-cusp-oneloop`). Literature `Polyakov1980`, `BrandtNeriSato1981`, `KorchemskyRadyushkin1987`, `Korchemsky1989`. Large-angle constant $\gamma_{HH}$ (WRITER_SPEC_v2 §3 row 44) is introduced in Ch23 (pointer).
  - `\uses{def:prelim-wilson}`

* **命题 `prop:sudakov-kg` — $K+G$ 演化方程** [A] · v1 (composite)
  - **陈述.** (a) $\frac{\partial\ln F}{\partial\ln Q^2}=\frac12[K(\varepsilon,\alpha_s(\mu))+G(Q^2/\mu^2,\alpha_s(\mu),\varepsilon)]$, $K$ a pure counterterm series, $G$ finite as $\varepsilon\to0$, $\mu\frac{dK}{d\mu}=-\gamma_K=-\mu\frac{dG}{d\mu}$. (b)（单圈内容，\tagR，$R_{\rm PT}$）$K=\frac{\alpha_sC_F}{4\pi}\frac4\varepsilon$, $G=\frac{\alpha_sC_F}{2\pi}(3+2\ln\frac{\mu^2}{Q^2})$, $\gamma_K=\frac{2C_F\alpha_s}\pi$ (VF-SUD-3; critic c7).
  - **证明.** Sketch of the all-order derivation from `thm:sudakov-factorization` + RG; one-loop check full.
  - **地位与缺口.** Inherits `thm:sudakov-factorization` ([A]).
  - `\uses{thm:sudakov-factorization, def:sudakov-cusp, prop:qcd-rge, prop:sudakov-oneloop}`

* **推论 `cor:sudakov-exponentiation` — 指数化与解析延拓** [A] · v1
  - **陈述.** $F$ exponentiates; the double logarithms are governed by $\gamma_K$; $|F(q^2)/F(-q^2)|^2$ is finite and computable (`Magnea:1990zb`); one-loop: $\pi^2$ term (VF-SUD-2).
  - **地位与缺口.** Inherits `prop:sudakov-kg`.
  - `\uses{prop:sudakov-kg}`

* **命题 `prop:sudakov-webs` — 非阿贝尔指数化（webs）** [A] · v1 (composite)
  - **陈述.** (a) All-order web exponentiation of Wilson-line correlators (`Gatheral1983`, `FrenkelTaylor1984`; App B `prop:appB-webs`). (b)（$O(g^2)$ 内容，\tagR，$R_{\rm def}$）$W^{(2)}-\frac12(W^{(1)})^2=\frac14\sum_{r,s}[T_s,T_r](E(r,s)-E(s,r))$ exactly at finite $\epsilon$ (VF-WL-3): $\ln W$ starts at $O(g^2)$ with commutators only.
  - **地位与缺口.** The all-order combinatorics is a standard argument; (b) is exact.
  - `\uses{def:prelim-wilson, prop:prelim-wilson-rules, lem:prelim-eikonal-identity, prop:appB-webs}`

* **定理 `thm:sudakov-ir-poles` — 无质量多腿振幅红外极点的因子化** [A] · v1
  - **陈述.** $|\mathcal M(\{p\},\varepsilon)\rangle=\mathbf Z(\{p\},\mu,\varepsilon)|\mathcal M_{\rm fin}(\{p\},\mu)\rangle$ with $\mathbf Z$ from a colour-space anomalous dimension; through two loops $\mathbf\Gamma=\sum_{(i,j)}\frac{\mathbf T_i\cdot\mathbf T_j}{2}\gamma_{\rm cusp}\ln\frac{\mu^2}{-s_{ij}}+\sum_i\gamma^i$ — normalization VF-SUD-5: $(i,j)$ ordered pairs $i\ne j$, $s_{ij}=2\sigma_{ij}p_i\cdot p_j+i0$, $\gamma_{\rm cusp}$ Casimir-stripped; the two-parton case reproduces $d\ln C_V/d\ln\mu$ (VF-SCET-8); cite `Becher:2009cu` eq. (2). Literature `Catani:1998bh`, `Sterman:2002qn`, `Becher:2009cu`, `Becher:2009qa`, `Gardi:2009qi`, `DixonMagneaSterman2008`.
  - **地位与缺口.** Explicit to the orders computed [R]; all-order factorization of poles [A] (survey item 30); the form of $\mathbf\Gamma$ beyond two loops is not the dipole form (`prop:sudakov-dipole-violation`). (本定理只涉及部分子振幅。)
  - `\uses{thm:sudakov-factorization, def:sudakov-cusp, prop:sudakov-webs}`

* **命题 `prop:sudakov-dipole-violation` — 偶极子公式作为全阶精确公式的失效** [V] · v1
  - **陈述.** At three loops non-dipole corrections appear: a constant for three coloured partons, conformal-cross-ratio dependence for $\ge4$ (`Almelid:2015jia`); the term preserves strict timelike collinear factorization.
  - **证明.** Cite; structure explained.
  - **地位与缺口.** Evidence: explicit three-loop calculation; attribution per A12.
  - `\uses{thm:sudakov-ir-poles}`

* **命题 `prop:sudakov-coulomb` — Coulomb 相位** [R, R_PT] · v1
  - **陈述.** (One loop.) The imaginary parts $i\pi\,\mathbf T_i\cdot\mathbf T_j$ arise for pairs both incoming or both outgoing and differ between timelike and spacelike invariants; at one loop ${\rm Im}F^{(1)}(s+i0)=\frac{\alpha_sC_F}{4\pi}[-\frac{2\pi}\varepsilon+2\pi\ell-3\pi]$, cancelling in $|F|^2$ (VF-EE-4).
  - **证明.** Full (one loop).
  - `\uses{prop:sudakov-oneloop}`

* **命题 `prop:sudakov-amplitude-factorization` — 振幅的硬—软—共线因子化（出射或阈值运动学）** [A] · v1
  - **陈述.** Feige–Schwartz all-order hard–soft–collinear factorization of amplitudes; excludes initial-state partons collinear to final-state ones (`FeigeSchwartz2014` §2, §7; `Feige:2013zla`). Consistent with the spacelike violation (Ch18).
  - **地位与缺口.** All-order argument at the amplitude level; IR forest formula for wide-angle amplitudes `Ma2020` (Ch24, pointer).
  - `\uses{thm:sudakov-factorization, thm:ir-leading-regions}`

* **注 `rem:sudakov-spacelike` — 类空共线极限预览** [V] · v1
  - Preview of `prop:break-spacelike`: for an incoming and an outgoing parton becoming collinear, the one-loop splitting amplitude depends on the colours of the non-collinear partons (CdFR 2012).
  - **地位与缺口.** Evidence: explicit one-loop calculation (`CataniDeFlorianRodrigo2012`); does not by itself show that PDF factorization fails (M21).
  - `\uses{prop:sudakov-amplitude-factorization}`

**Worked examples (≥ 4).** `ex:sudakov-onshell-hard`, `ex:sudakov-offshell`, `ex:sudakov-massive`, `ex:sudakov-ll`; one-loop $K,G$ extraction (part of `prop:sudakov-kg`).

**Figures.** Existing: `fig:sudakov-ff` (tikz2); new: `fig:sudakov-hjjs`, `fig:sudakov-cusp`, `fig:sudakov-dipole`.

**Misconception box.** M16 (rapidity divergences are artefacts — first mention, for the massive Sudakov form factor), M21 preview; critic O11 (massive exchange needs analytic regulators).

**Key citation keys.** `Sudakov1956`, `Mueller:1979ih`, `Collins:1980ih`, `Sen:1981sd`, `Sen1983`, `Akhoury1979`, `Magnea:1990zb`, `Collins:1989bt`, `Korchemsky1989`, `KorchemskyRadyushkin1987`, `Polyakov1980`, `BrandtNeriSato1981`, `Gatheral1983`, `FrenkelTaylor1984`, `Catani:1998bh`, `Sterman:2002qn`, `Becher:2009cu`, `Becher:2009qa`, `Gardi:2009qi`, `Almelid:2015jia`, `DixonMagneaSterman2008`, `FeigeSchwartz2014`, `Feige:2013zla`, `CataniDeFlorianRodrigo2012`, `Gonsalves1983`, `MochVermaserenVogt2005`, `BecherBroggioFerroglia2015`, `BenekeSmirnov1998`, `Jantzen2011`, `UsyukinaDavydychev1993a`, `BecherNeubert2011`, `BecherBell2012`, `Collins2011`, `Dixon:2019lnw`, `Ma2020`.

**Pending.** `ex:sudakov-offshell` pointer sentence [PENDING-VERIFY: N12]; `def:sudakov-cusp` (BS misprint, App Q candidate) [PENDING-VERIFY: E23]; `thm:sudakov-factorization` status sentence [PENDING-VERIFY: S63-12].

---------------------------------------------------------------------------------------------------

# 第二部分 严格核心 (Part II — The rigorous core)

---------------------------------------------------------------------------------------------------

## Chapter 6 — 严格核心 I：$e^+e^-$ 湮灭总截面 / Rigorous core I: the $e^+e^-$ total cross section

`\label{ch:ee}` · `ch06_ee.tex` · **14 pp** · full · Part II

**Purpose.** Prove, inside renormalized PT, that $R(s)\equiv12\pi\,{\rm Im}\,\Pi(s+i0)$ is IR finite at every order and compute it to $O(\alpha_s)$ in two independent ways (cut diagrams; Euclidean two-loop correlator); show analyticity, unitarity and RG in their cleanest setting, with the four logically separate levels (axiomatic analyticity / perturbation theory / OPE-conditional statements / the smearing identity vs its computability) kept apart; state honestly the status of condensates and of duality. Proof route (critic O3, c_ee §5): Euclidean IR finiteness + polynomial structure in $\ln(-q^2/\mu^2)$ + trivial analytic continuation.

**Depends on.** Ch2 (`prop:prelim-rg`, `prop:qcd-rge`, `def:prelim-msbar`, `thm:qcd-renormalizability`, `thm:prelim-composite-renorm`), Ch3 (`prop:prelim-optical`, `thm:prelim-cutting-rules`, `rem:prelim-cutting-dr`, `prop:prelim-unitarity`), Ch4 (`def:ir-landau-setup`; KLN for remarks), Ch5 (`prop:sudakov-oneloop`).

**Logical flow chart (print at the start of `sec:ee-theorem`).** `prop:ee-analytic` + `lem:ee-single-scale` + `thm:ee-euclid-ir` + UV renormalization ⇒ $\Pi_R(s+i0)$ finite; + `prop:ee-adler-rg` ⇒ polynomial structure (`thm:ee-R-finite`); explicit $O(\alpha_s)$: `prop:ee-oneloop`, `prop:ee-twoloop`, `prop:ee-cutting-exact`; + cutting rules ⇒ equality with the sum over partonic final states (`cor:ee-cuts`, [A]).

**Box.**
- 证明了：`thm:ee-R-finite`、`thm:ee-euclid-ir`、`lem:ee-single-scale`、`prop:ee-adler-rg`、`prop:ee-oneloop`、`prop:ee-twoloop`、`prop:ee-cutting-exact`、`cor:ee-R-alphas`（[R, R_PT]）；`prop:ee-R-ImPi`、`prop:ee-analytic`、`prop:ee-adler-dispersion`、`prop:ee-contour`、`prop:ee-smearing`（[R, R_def]；强子态需 `asm:intro-wightman`）。
- 给出全阶论证：`cor:ee-cuts`（[A]：无质量维数正规化割图规则）；`thm:ee-ope`（[A]：含夸克 QCD 的 OPE）。
- 没有证明：非微扰 OPE 与凝聚（`conj:ee-np-ope`，[C]；`asm:intro-np-ope`）；夸克—强子对偶（`conj:ee-duality`，[C]）；在复 $q^2$ 处使用 OPE（`rem:ee-complex-ope`）。

**Sections.**
1. `sec:ee-R` $R$ 比与流关联函数 — normalizations VF-CONV-12, VF-EE-1.
2. `sec:ee-analytic` 解析性、谱表示与 Adler 函数 — incl. the exact one-subtraction condition.
3. `sec:ee-euclid` 欧氏红外有限性与重整化群 — the IR-degree count $d=A+\frac12A_q\ge2$.
4. `sec:ee-theorem` 主定理：$R(s)$ 的红外有限性.
5. `sec:ee-oneloop` $O(\alpha_s)$：实—虚相消与两圈关联函数 — real/virtual in one normalization; Euclidean two-loop route; exact cutting identity; KLN for the total rate vs the non-IR-safe quark spectrum; identification with partonic cuts.
6. `sec:ee-higher` 高阶：$\pi^2$ 项与已知系数 — contour formula; $r_n$ vs $d_n$; literature values; `fig:ee-pi-plane`, `fig:ee-cutsum-disc`; the four-level status layout.
7. `sec:ee-ope` 欧氏 OPE 与凝聚.
8. `sec:ee-duality` 类时区：抹平与对偶.

**Canonical statements** (in reading order).

* **定义 `def:ee-R` — $R$ 比** (no tag) · v1
  - **陈述.** $R(s)=\sigma(e^+e^-\to{\rm hadrons})/\sigma(e^+e^-\to\mu^+\mu^-)$, one-photon exchange, lowest order in $\alpha$, $\sigma_{\mu\mu}=4\pi\alpha^2/(3s)$; $R_0=N_c\sum_qe_q^2$ (VF-EE-1).
  - `% uses: none`

* **命题 `prop:ee-R-ImPi` — $R=12\pi\,{\rm Im}\,\Pi$** [R, R_def] · v1
  - **陈述.** With $\Pi^{\mu\nu}=i\int d^4x\,e^{iq\cdot x}\langle0|Tj^\mu(x)j^\nu(0)|0\rangle=(q^\mu q^\nu-q^2g^{\mu\nu})\Pi(q^2)$: $\sigma=\frac{16\pi^2\alpha^2}{s}{\rm Im}\,\Pi(s+i0)$, $R=12\pi\,{\rm Im}\,\Pi(s+i0)$ (lepton tensor contraction $L_{\mu\nu}(q^\mu q^\nu-q^2g^{\mu\nu})=s^2$).
  - **非微扰地位.** \cref{asm:intro-wightman}（MA0）。
  - **证明.** Full (VF-CONV-12; `prop:prelim-optical`).
  - `\uses{def:ee-R, prop:prelim-optical, asm:intro-wightman}`

* **引理 `lem:ee-single-scale` — 无质量传播子型图的单标度结构** [R, R_PT] · v1
  - **陈述.** Every bare $(n+1)$-loop contribution to $\Pi$ in massless QCD with DR equals $c_n(\varepsilon)(\mu_0^2)^{n\varepsilon}(-q^2-i0)^{-(n+1)\varepsilon}$ with $c_n$ meromorphic (VF-EE-15); in particular each order is analytic in $q^2\in\mathbb C\setminus[0,\infty)$.
  - **证明.** Full ($\alpha$-representation: $\mathcal F=-q^2\mathcal U_2$, $\mathcal U_2\ge0$; dimension count; blueprint S4). (本引理只涉及 Feynman 图。)
  - `\uses{def:ir-landau-setup, def:qcd-dimreg}`

* **命题 `prop:ee-analytic` — 解析性与正定性** [R, R_def] · v1 (+ refdoc S17.1)
  - **陈述.** (a) $\Pi(q^2)$ is analytic in $\mathbb C\setminus[s_0,\infty)$, ${\rm Im}\,\Pi(s+i0)\ge0$; $s_0=4m_\pi^2$ (hadrons) or $0$ (massless PT, cf. `lem:ee-single-scale`). (b) **Exact subtraction condition (refdoc S17.1):** one subtraction suffices, $\Pi(q^2)-\Pi(-\mu^2)=\frac{q^2+\mu^2}\pi\int_{s_0}^\infty ds\frac{{\rm Im}\Pi(s)}{(s-q^2-i0)(s+\mu^2)}$, **iff** $\int^\infty ds\,{\rm Im}\,\Pi(s)/s^2<\infty$ ⟺ the Adler function is finite at one Euclidean point; the subtraction point is Euclidean because $\Pi(0)$ is IR divergent for massless quarks.
  - **非微扰地位.** \cref{asm:intro-wightman}（MA0：Källén–Lehmann 表示、正定谱密度、多项式有界）。
  - **证明.** Full given the spectral representation (half page; for (b): $\rho\ge0$ and $(s+Q^2)^{-2}\ge(2s)^{-2}$ for $s\ge Q^2$).
  - `\uses{prop:ee-R-ImPi, asm:intro-wightman}`

* **定义 `def:ee-adler` — Adler 函数** (no tag) · v1
  - **陈述.** $D(Q^2)\equiv-12\pi^2Q^2\frac{d\Pi(-Q^2)}{dQ^2}$; free of the additive renormalization of $\Pi$.
  - `\uses{def:ee-R}`

* **命题 `prop:ee-adler-dispersion` — Adler 函数的色散表示** [R, R_def] · v1
  - **陈述.** $D(Q^2)=Q^2\int_0^\infty ds\frac{R(s)}{(s+Q^2)^2}$. Check: $R$ const ⇒ $D=R$ (VF-EE-14).
  - **证明.** Full (from `prop:ee-analytic`).
  - `\uses{def:ee-adler, prop:ee-analytic}`

* **定理 `thm:ee-euclid-ir` — 欧氏红外有限性** [R, R_PT] · v1
  - **陈述.** In a renormalizable theory with massless fields and no super-renormalizable couplings, renormalized Green functions at non-exceptional Euclidean momenta are finite at every order (MS-bar or BPHZL subtractions).
  - **证明.** Sketch with the IR-degree computation printed in full (blueprint S3: for a soft subset $S$ attached $A$ times to non-soft lines, $A_q$ of them quark ends, $d=A+\frac12A_q\ge2$; VF-EE-13; the zero-momentum Landau solutions of `rem:ir-euclid-corners` are integrable by this count); convergence theorem cited: `PoggioQuinn1976`, `LowensteinZimmermann1975`, `Lowenstein:1975ps`, `Breitenlohner:1975hg`, `Breitenlohner:1976te`, `BreitenlohnerMaison1977a`, `Frob:2015uqy` (pure YM). 地位注: the explicit check that the Breitenlohner–Maison hypotheses are spelled out for non-abelian gauge fields with FP ghosts in covariant gauges is open [PENDING-VERIFY: N24]; the gauge-invariant current correlator is gauge independent (`prop:qcd-xi-independence`). (本定理只涉及部分子态的 Green 函数。)
  - `\uses{thm:qcd-renormalizability, def:prelim-msbar, def:qcd-dimreg, prop:qcd-xi-independence}`

* **命题 `prop:ee-adler-rg` — Adler 函数的重整化群** [R, R_PT] · v1
  - **陈述.** $(\mu^2\partial_{\mu^2}+\beta(\alpha_s)\partial_{\alpha_s})D=0$, $D(Q^2)=R_0\,d(a(Q^2))$; $\mu^2d\Pi/d\mu^2$ is $q$-independent (contact term); at order $a^n$, $\Pi_{\overline{\rm MS}}$ is a polynomial in $L=\ln(-q^2/\mu^2)$ of degree $\max(1,n)$ (VF-EE-9).
  - **证明.** Full.
  - `\uses{def:ee-adler, prop:prelim-rg, prop:qcd-rge}`

* **定理 `thm:ee-R-finite` — $R(s)$ 在微扰论每一阶的红外有限性** [R, R_PT] · v1
  - **陈述.** (c_ee Theorem 5.1.) Let $R^{(n)}$ be the coefficient of $a^n$ of $12\pi\,{\rm Im}\,\Pi_{\overline{\rm MS}}(s+i0)$ computed with $D$-dimensional loops and analytic continuation of the bare expressions at fixed $\varepsilon$. Then (i) $\lim_{\varepsilon\to0}R^{(n)}$ exists; (ii) for $n\ge1$ it is a polynomial of degree $\le n-1$ in $\ln(s/\mu^2)$; (iii) it equals the analytic continuation $L\to\ln(s/\mu^2)-i\pi$ of the Euclidean renormalized correlator.
  - **非微扰地位.** 强子层次的 $R(s)$ 需 \cref{asm:intro-wightman}（MA0）与 \cref{asm:intro-bridge}；逐点意义见 `conj:ee-duality`。
  - **证明.** Full (steps (a)–(c) of c_ee §5: finiteness at $q^2<0$; Laurent coefficients are polynomials in $L$ vanishing for all real $L$ hence identically; continuation commutes with $\varepsilon\to0$). Route as our derivation (novelty not claimed) [PENDING-VERIFY: N24].
  - `\uses{prop:ee-R-ImPi, lem:ee-single-scale, thm:ee-euclid-ir, prop:ee-adler-rg}`

* **命题 `prop:ee-oneloop` — $O(\alpha_s)$ 的实辐射与虚修正** [R, R_PT] · v1
  - **陈述.** In the common normalization $N_\varepsilon=\frac{\alpha_sC_F}{2\pi}(\frac{4\pi\mu_0^2}{s})^\varepsilon c_\Gamma$: virtual $\rho_V/\rho_0=N_\varepsilon[-\frac2{\varepsilon^2}-\frac3\varepsilon-8+\pi^2+O(\varepsilon)]$ (from $2{\rm Re}F$, VF-EE-4), real $\rho_R/\rho_0=\frac{\alpha_sC_F}{2\pi}(\frac{4\pi\mu_0^2}s)^\varepsilon\frac{2(1-2\varepsilon)(2-2\varepsilon+\varepsilon^2)\Gamma(1-\varepsilon)^2}{\varepsilon^2(1-3\varepsilon)(2-3\varepsilon)\Gamma(1-3\varepsilon)}=N_\varepsilon[\frac2{\varepsilon^2}+\frac3\varepsilon+\frac{19}2-\pi^2+O(\varepsilon)]$ (VF-EE-5); sum $\frac32N_\varepsilon\Rightarrow R=R_0(1+\frac{3C_F}4\frac{\alpha_s}\pi)$ (VF-EE-6). Warning to print: separate real/virtual constants depend on the common normalization (the two $\Gamma$-prefactors differ by $1-\frac{\pi^2}2\varepsilon^2$), only the sum does not.
  - **证明.** Full (App G: matrix element, three-body phase space, Dirichlet integrals; `lem:appC-phase-space`).
  - `\uses{def:ee-R, prop:sudakov-oneloop, def:prelim-dr-conventions, lem:appC-phase-space}`

* **例 `ex:ee-quark-spectrum` — KLN 的作用与局限** (no tag) · v1
  - (c_ee §7, VF-EE-11.) Exclusive pieces $\pm2/\varepsilon^2$; the quark energy spectrum keeps $-\frac1\varepsilon\frac{\alpha_s}{2\pi}P_{qq}(x)$ (moments $0,\frac43,\frac{25}{12},\frac{157}{60}$ times $C_F$) — absorbed into FFs (Ch11, pointer).
  - `\uses{prop:ee-oneloop, thm:ir-kln}`

* **命题 `prop:ee-twoloop` — 欧氏两圈关联函数** [R, R_PT] · v1
  - **陈述.** Exact bare result $\Pi^{(1)}_{\rm bare}=N_ce_q^2C_F\frac{g_0^2(Q^2)^{-2\varepsilon}}{(4\pi)^D}[r_1G(1,1)^2+r_2G(1,1)G(1+\varepsilon,1)]$ with $r_1,r_2$ of VF-EE-7; Ward identity $q_\mu q_\nu\Pi^{\mu\nu}=0$; $\Pi_{\overline{\rm MS}}=\frac{N_ce_q^2}{12\pi^2}[\frac53-L+\frac{\alpha_s}\pi\frac{3C_F}4(\frac{55}{12}-4\zeta_3-L)]$; $D=N_ce_q^2(1+\frac{3C_F}4\frac{\alpha_s}\pi)$.
  - **证明.** Sketch in text, details App G (IBP triangle rule `lem:appC-ibp`, $\hat I(1,1,1,1,1)=6\zeta_3$; `lem:appC-bubble`).
  - `\uses{def:prelim-msbar, lem:appC-bubble, lem:appC-ibp}`

* **例 `ex:ee-twoloop-route` — 欧氏两圈路线** (no tag) · v1
  - The Euclidean two-loop route reproduces $1+\alpha_s/\pi$ (strongest pedagogical demonstration of `thm:ee-R-finite`).
  - `\uses{prop:ee-twoloop, thm:ee-R-finite}`

* **命题 `prop:ee-cutting-exact` — $O(g^2)$ 处精确到 $\varepsilon$ 的切割恒等式** [R, R_PT] · v1
  - **陈述.** $2(D-1)s\,{\rm Im}\,\Pi^{(1)}_{\rm bare}(s+i0)=\rho_V+\rho_R$, term by term ($r_1G_{11}^2\leftrightarrow\rho_V$, $r_2G_{11}G_{1+\varepsilon,1}\leftrightarrow\rho_R$) (VF-EE-8).
  - **证明.** Full (reflection formulas). Our derivation (novelty not claimed) [PENDING-VERIFY: N24].
  - `\uses{prop:ee-oneloop, prop:ee-twoloop}`

* **推论 `cor:ee-cuts` — 与部分子末态求和的等同；KLN** [A] · v1
  - **陈述.** $R^{(n)}$ equals the sum over all cuts (all partonic final states with physical polarizations, including $\overline{\rm MS}$ counterterm insertions) of the $D$-dimensional cross section; each cut separately has poles up to $\varepsilon^{-2n}$; for $e^+e^-$ only final-state degeneracies are needed (`fig:ee-cutsum-disc`).
  - **证明.** `thm:prelim-cutting-rules`, `rem:prelim-cutting-dr`, `prop:prelim-unitarity`; exact-in-$\varepsilon$ check at $O(g^2)$ (`prop:ee-cutting-exact`).
  - **地位与缺口.** No single source writes the massless, IR-regulated $D$-dimensional cutting rules with ghosts in complete rigour (c_ee §5); this is `rem:prelim-cutting-dr` ([A]).
  - `\uses{thm:ee-R-finite, thm:prelim-cutting-rules, rem:prelim-cutting-dr, prop:prelim-unitarity, prop:ee-cutting-exact}`

* **命题 `prop:ee-contour` — 围道公式** [R, R_def] · v1
  - **陈述.** $R(s)=\frac1{2\pi}\int_{-\pi}^{\pi}d\theta\,D(se^{i\theta})$ (c_ee §6; VF-EE-9); `fig:ee-pi-plane`.
  - **证明.** Full.
  - `\uses{prop:ee-adler-dispersion, prop:ee-analytic}`

* **推论 `cor:ee-R-alphas` — $R(s)$ 的微扰展开** [R, R_PT] · v1
  - **陈述.** (For the $O(\alpha_s)$ coefficient and the structural relations.) $R=R_0[1+\frac34C_Fa+r_2a^2+r_3a^3+\dots]$, $a=\alpha_s(s)/\pi$ ($\overline{\rm MS}$, $\mu^2=s$, photon exchange, massless quarks); SU(3): $r_2=\frac{365}{24}-11\zeta_3-n_f(\frac{11}{12}-\frac23\zeta_3)=1.9857-0.1153n_f$ (VF-EE-10); general group $r_2=-\frac3{32}C_F^2+C_FC_A(\frac{123}{32}-\frac{11}4\zeta_3)-C_FT_Fn_f(\frac{11}8-\zeta_3)$ (literature form, reduces to the verified SU(3) value; `ChetyrkinKataevTkachov1979`, `DineSapirstein1979`, `CelmasterGonsalves1980a`); structural relations $r_1=d_1$, $r_2=d_2$, $r_3=d_3-\frac{\pi^2}3b_0^2d_1$, $r_4=d_4-\pi^2(b_0^2d_2+\frac56b_0b_1d_1)$, $b_0=\beta_0/4$, $b_1=\beta_1/16$ (VF-EE-9); the singlet $(\sum e_q)^2$ term starts at $a^3$ (Furry's theorem; link to the previous monograph). Higher values ($r_3$: `GorishniiKataevLarin1991` — the earlier GKL value was corrected (history only, E29) —, `SurguladzeSamuel1991`, $O(a^4)$ `BaikovChetyrkinKuhn2008`) quoted only as "(literature)".
  - **证明.** Full for the $O(\alpha_s)$ coefficient and the structural relations; $r_2$ cited.
  - `\uses{thm:ee-R-finite, prop:ee-oneloop, prop:ee-twoloop, prop:ee-adler-rg, prop:ee-contour}`

* **例 `ex:ee-pi2` — $O(a^3)$ 的 $\pi^2$ 项** (no tag) · v1
  - $-\frac{\pi^2}3b_0^2d_1$ from the contour formula; numerical size ($\frac{\pi^2}3b_0^2=16.66,14.28,12.09$ for $n_f=3,4,5$) dominates the known $r_3$.
  - `\uses{prop:ee-contour, cor:ee-R-alphas}`

* **注 `rem:ee-status-layout` — 四个逻辑层次** (no tag) · refdoc S17.2 (T10)
  - (i) Wightman analyticity with the exact one-subtraction condition (`prop:ee-analytic`, under `asm:intro-wightman`); (ii) perturbation theory (`thm:ee-R-finite`, [R, R_PT]); (iii) OPE-conditional statements (`thm:ee-ope` [A], condensates `conj:ee-np-ope` [C]); (iv) the smearing identity (`prop:ee-smearing`, [R, R_def]) vs its computability (`conj:ee-duality`, [C]). These levels must never be merged in the text.

* **定理 `thm:ee-ope` — 流关联函数的欧氏 OPE** [A] · v1 (+ refdoc S17.5)
  - **陈述.** $\Pi(-Q^2)=C_{\mathbb 1}(Q^2)+\sum_qC_{m\bar qq}\frac{\langle m_q\bar qq\rangle}{Q^4}+C_G\frac{\langle\frac{\alpha_s}\pi G^2\rangle}{Q^4}+O(Q^{-6})$ in renormalized PT for Green functions; no $1/Q^2$ term for massless quarks (no gauge-invariant dimension-2 operator). Coefficients: `ShifmanVainshteinZakharov1979a`, `ShifmanVainshteinZakharov1979b` (normalization converted to VF-CONV-12 by the writer).
  - **证明.** Sketch, self-contained: (1) Weinberg's theorem and Zimmermann's identity with improved remainder for the Euclidean two-point function of the gauge-invariant current; (2) Lorentz covariance and dimension counting; (3) BRST-exact and EOM operators have vanishing vacuum expectation values (`thm:prelim-composite-renorm`).
  - **地位与缺口.** Proven to all orders in PT for scalar theories (`Zimmermann1973`; convergence at each order `Hollands:2011gf`) and for gauge-invariant operators in pure Yang–Mills (`Hollands:2007zg`); for QCD with quarks "proved in a gauge theory the same way" (`Collins1984` §12.8) or widely assumed (`IzubuchiEtAl2018` Sec. II) — hence [A] (binding decision D3; attribution per A09 [PENDING-VERIFY: A09]); the vacuum OPE of the Adler function has no $1/Q^2$ term; the condensate terms are conditional on `asm:intro-np-ope` (refdoc S17.5). The full status discussion is repeated with `thm:dis-ope` (Ch7), which refers back; the rigorous OPE results of the literature are collected in Ch24 (pointer). (本定理只涉及部分子态的 Green 函数。)
  - `\uses{thm:prelim-composite-renorm, thm:ee-euclid-ir, def:ee-adler}`

* **猜想 `conj:ee-np-ope` — 非微扰 OPE 与凝聚** [C] · v1
  - **陈述.** The OPE holds between vacuum states with the same coefficients, condensates being non-perturbative parameters (this is the vacuum part of `asm:intro-np-ope`); $\langle G^2\rangle$ is ambiguous at the level of the leading IR renormalon (pointer `prop:power-adler-large-beta0`).
  - **地位与缺口.** No non-perturbative definition of the OPE in QCD; AQFT results (`Bostelmann:2005rr`) need phase-space properties not established for QCD; `Novikov:1984rf`, `David:1983gz`, `David:1985xj`.
  - `\uses{thm:ee-ope}`

* **注 `rem:ee-complex-ope` — 复 $q^2$ 处的 OPE 是额外假设** (no tag) · refdoc S17.3
  - The OPE assumptions of App M and `asm:intro-np-ope` are Euclidean; using the OPE at complex $q^2$ (e.g. the smearing points $s\pm i\Delta$) is an extra assumption, which feeds `conj:ee-duality`.

* **命题 `prop:ee-smearing` — Poggio–Quinn–Weinberg 抹平恒等式** [R, R_def] · v1
  - **陈述.** $\bar R(s,\Delta)\equiv\frac\Delta\pi\int_0^\infty ds'\frac{R(s')}{(s'-s)^2+\Delta^2}=\frac{12\pi}{2i}[\Pi(s+i\Delta)-\Pi(s-i\Delta)]$.
  - **非微扰地位.** \cref{asm:intro-wightman}（MA0）。
  - **证明.** Full (from `prop:ee-analytic`).
  - `\uses{prop:ee-analytic, asm:intro-wightman}`

* **猜想 `conj:ee-duality` — 夸克—强子对偶** [C] · v1
  - **陈述.** (a) $\bar R=\bar R_{\rm PT}+O(\Lambda^4/\Delta^2)$ for $\Delta\sim s$ rests on the non-perturbative OPE in the complex plane (`rem:ee-complex-ope`); (b) local (pointwise) duality is not controlled by the OPE (oscillating terms invisible in the $1/Q^2$ expansion). `PoggioQuinnWeinberg1976`, `Shifman2000`. (M27.)
  - **地位与缺口.** Both parts are conjectures; models of duality violation (instanton models: power-damped oscillations; resonance models) are illustrations only.
  - `\uses{prop:ee-smearing, conj:ee-np-ope}`

**Worked examples.** `ex:ee-quark-spectrum`, `ex:ee-twoloop-route`, `ex:ee-pi2`.

**Figures.** Existing: `fig:ee-oneloop` (tikz2); new: `fig:ee-pi-plane`, `fig:ee-cutsum-disc` (required, refdoc S56; with the Furry remark).

**Misconception box.** M27 (perturbative $R(s)$ valid pointwise); "the $O(\alpha_s^2)$ singlet term" (vanishes by Furry's theorem); critic O3, O21 (part).

**Key citation keys.** `AppelquistGeorgi1973`, `Zee1973`, `Adler1974`, `PoggioQuinn1976`, `PoggioQuinnWeinberg1976`, `LowensteinZimmermann1975`, `Lowenstein:1975ps`, `LowensteinSpeer1976`, `Breitenlohner:1975hg`, `Breitenlohner:1976te`, `BreitenlohnerMaison1977a`, `Symanzik1973`, `KinoshitaUkawa1976`, `Frob:2015uqy`, `Sterman:1976jh`, `Sterman1978a`, `Sterman1978b`, `ChetyrkinKataevTkachov1979`, `DineSapirstein1979`, `CelmasterGonsalves1980a`, `CelmasterGonsalves1980b`, `GorishniiKataevLarin1991`, `SurguladzeSamuel1991`, `BaikovChetyrkinKuhn2008`, `ChetyrkinKuhnKwiatkowski1996`, `KrasnikovPivovarov1982`, `KataevStarshenko1995`, `ChetyrkinTkachov1981`, `Tkachov1981`, `Gonsalves1983`, `MochVermaserenVogt2005`, `ShifmanVainshteinZakharov1979a`, `ShifmanVainshteinZakharov1979b`, `Novikov:1984rf`, `David:1983gz`, `David:1985xj`, `Shifman2000`, `Bostelmann:2005rr`, `EllisStirlingWebber1996`, `Kinoshita1962`, `LeeNauenberg1964`, `Frye:2018xjj`, `Hollands:2011gf`, `Hollands:2007zg`, `Holland:2014pna`, `Collins1984`, `IzubuchiEtAl2018`.

**Pending.** [PENDING-VERIFY: N24] (BM hypotheses for non-abelian theories with ghosts; route attribution); [PENDING-VERIFY: A09] (OPE status wording); E29 is history only (no App Q row).

---------------------------------------------------------------------------------------------------

## Chapter 7 — 严格核心 II：深度非弹散射与算符乘积展开 / Rigorous core II: DIS and the operator product expansion

`\label{ch:dis}` · `ch07_dis.tex` · **18 pp** · full (complete proofs of the non-perturbative layer and of the OPE machinery in App M; uniqueness lemmas in App K) · Part II

**Purpose.** Moment factorization of DIS structure functions, along **two proof routes** (refdoc S18): (I) partonic PT — analyticity and crossing of the forward Compton amplitude, the dispersion relation identifying the Taylor coefficients at $\omega=0$ with moments, the Euclidean OPE split into its three sub-statements (Euclidean graph-by-graph expansion, reduction to gauge-invariant operators, forward on-shell partonic matrix elements) with separate tags, RG; (II) hadrons, non-perturbative and conditional — the Euclidean OPE informs only on a segment of length $O(M/Q)$ of the imaginary $\omega$ axis, so fixed-$n$ moments need positivity and a $Q$-uniform finite-subtraction dispersion relation proved from the Wightman axioms; only the lowest moments (incl. the momentum sum rule) need a genuine growth assumption. Then: moments ⇒ $x$ space only in the sense of distributions (weak convergence; pointwise remainder not controlled; counterexample); light-cone OPE as the $x$-space structure ([A]); twist classification and chirality; higher twist and target mass; polarized moments (Bjorken sum rule). The $x$-space theorem with operator-defined PDFs is completed in Ch8 (`thm:pdf-dis-xspace`).

**Depends on.** Ch2 (`thm:prelim-composite-renorm`, `prop:prelim-rg`, `prop:qcd-rge`, `thm:qcd-renormalizability`, `prop:prelim-beta`), Ch3 (`prop:prelim-optical`, Mellin, `lem:prelim-boost`, `lem:prelim-scaleless`, `def:prelim-gamma5`), Ch4 (`def:ir-landau-setup`), Ch5 (`prop:sudakov-oneloop`), Ch6 (methodological model; `thm:ee-euclid-ir`); App M [SYNC-APP], App K, App I.

**Proof architecture (flow chart at chapter start; refdoc S18).** PT route: `prop:dis-compton-analytic` → `prop:dis-dispersion` ⟵ `lem:dis-tree-ope`, `prop:dis-ope-euclid` → `prop:dis-ope-gi` → `prop:dis-ope-forward` (= `thm:dis-ope`) → `thm:dis-moments`(a) → `prop:dis-ope-rg` → `cor:dis-scaling`. Hadronic route: `prop:dis-dispersion-np` → `lem:dis-euclid-segment` → `lem:dis-ope-segment` → `thm:dis-fixed-n` → `thm:dis-moments-np` → `thm:dis-moments`(b), `cor:dis-weak-xspace`. Misconception **M34**.

**Box.**
- 证明了：`prop:dis-W-structure`、`lem:dis-euclid-segment`、`lem:dis-twist-classification`、`lem:dis-twist-chirality`、`prop:dis-low-moments`（[R, R_def]）；`prop:dis-compton-analytic`、`prop:dis-dispersion`、`lem:dis-tree-ope`、`prop:dis-chiral-suppression`、`prop:dis-c-oneloop`（[R, R_PT]）；`thm:dis-moments`、`prop:dis-wilson-partons`、`prop:dis-ope-rg`、`cor:dis-scaling`、`prop:dis-twist4`、`prop:dis-tmc`、`thm:dis-bjorken`（[R, R_OPE]）；`prop:dis-dispersion-np`（[R, R_cond]，前提 `asm:intro-wightman`）、`lem:dis-ope-segment`（前提 `asm:intro-np-ope`）、`thm:dis-fixed-n`、`thm:dis-moments-np`、`cor:dis-weak-xspace`（[R, R_cond]，前提 `asm:intro-*`）。
- 给出全阶论证：`thm:dis-ope` 及其三个子陈述 `prop:dis-ope-euclid`、`prop:dis-ope-gi`、`prop:dis-ope-forward`（[A]；瓶颈 `asm:appM-brst-ope`、`asm:appM-forward`）；`prop:dis-light-cone`（[A]）。
- 没有证明：含夸克 QCD 的 OPE 的严格证明；非微扰 OPE（`asm:intro-np-ope`）；低阶矩（含动量求和规则）所需的增长条件（`asm:intro-growth`）；$x$ 空间逐点的 $O(1/Q^2)$（`rem:dis-nonuniform`）。

**Sections.**
1. `sec:dis-kinematics` 运动学、强子张量与结构函数 (`fig:dis-kinematics`).
2. `sec:dis-compton` 前向 Compton 振幅：解析性、交叉与色散关系（部分子靶） (`fig:forward-compton`, `fig:omega-plane`).
3. `sec:dis-ope` 扭度、规范不变算符与欧氏算符乘积展开 (`fig:ope-schematic`; optional `fig:dis-twist-graphical`) — twist classification and chirality; tree level; the three OPE sub-statements and the umbrella; chiral suppression; extraction of Wilson coefficients; RG.
4. `sec:dis-np` 强子靶：Wightman 色散关系、欧氏线段与固定 $n$ 的矩 (`fig:dis-euclid-segment`) — **new section** (refdoc S20–S22).
5. `sec:dis-moments` 主定理：结构函数矩的因子化 — the two routes combined (`thm:dis-moments`).
6. `sec:dis-rg` 重整化群与标度破坏 (v1 section label kept) — `cor:dis-scaling`, `ex:dis-n2`; the RG of coefficients (`prop:dis-ope-rg`) is stated in `sec:dis-ope`.
7. `sec:dis-wilson` Wilson 系数的单圈计算 — two derivations (cut diagrams + moments; hard-region forward amplitude) (`fig:dis-oneloop`).
8. `sec:dis-xspace` 从矩到 $x$ 空间：唯一性、弱收敛与非一致性 — App K results; the $\sin(Q^2x)$ counterexample; light-cone OPE.
9. `sec:dis-higher-twist` 高扭度与靶质量修正 (`fig:higher-twist`).
10. `sec:dis-polarized` 极化 DIS 的矩：Bjorken 求和规则.
11. Closing: `tab:dis-correspondence` (chapter statement | precise version in App M | what differs: assumptions, error type) (refdoc S45.2).

**Canonical statements** (in reading order).

* **定义 `def:dis-kinematics` — DIS 运动学与强子张量** (no tag) · v1
  - **陈述.** VF-CONV-13: $Q^2=-q^2$, $x=Q^2/(2P\cdot q)$, $y=P\cdot q/P\cdot\ell$, $\omega=1/x$; $W^{\mu\nu}=\frac1{4\pi}\int d^4z\,e^{iq\cdot z}\langle P|[j^\mu(z),j^\nu(0)]|P\rangle$ (spin averaged) $=(-g^{\mu\nu}+\frac{q^\mu q^\nu}{q^2})F_1+\tilde P^\mu\tilde P^\nu\frac{F_2}{P\cdot q}$; $F_L=(1+4M^2x^2/Q^2)F_2-2xF_1$ (reduces to $F_2-2xF_1$ at $M\to0$; critic D1); cross section $\frac{d^2\sigma}{dx\,dQ^2}=\frac{4\pi\alpha^2}{xQ^4}[xy^2F_1+(1-y-\frac{x^2y^2M^2}{Q^2})F_2]$ (writer re-derives from the lepton tensor), $M\to0$: $\frac{2\pi\alpha^2}{xQ^4}[(1+(1-y)^2)F_2-y^2F_L]$.
  - `% uses: none`

* **命题 `prop:dis-W-structure` — 强子张量的一般结构** [R, R_def] · v1
  - **陈述.** (i) $q_\mu W^{\mu\nu}=0$; (ii) the decomposition is the most general symmetric one for an unpolarized target (P, T, hermiticity); (iii) $F_1\ge0$, $F_L\ge0$ (positivity of $\epsilon^*_\mu W^{\mu\nu}\epsilon_\nu$; $2x\,\epsilon_L\epsilon_LW=F_L$, $\epsilon_T\epsilon_TW=F_1$); (iv) $W^{\mu\nu}=0$ for $x>1$, elastic contribution at $x=1$.
  - **非微扰地位.** \cref{asm:intro-wightman}（MA0）。
  - **证明.** Full.
  - `\uses{def:dis-kinematics, asm:intro-wightman}`

* **定义 `def:dis-compton` — 前向 Compton 振幅** (no tag) · v1
  - **陈述.** VF-CONV-14: $T^{\mu\nu}=i\int d^4z\,e^{iq\cdot z}\langle P|Tj^\mu(z)j^\nu(0)|P\rangle$, invariant amplitudes $T_{1,2}(\omega,Q^2)$ with the same tensors; Taylor coefficients $t_n$ of $T_2$ at $\omega=0$.
  - `\uses{def:dis-kinematics}`

* **命题 `prop:dis-compton-analytic` — 解析性与交叉（部分子靶）** [R, R_PT] · v1→rev. (refdoc S21: hadronic part moved to `prop:dis-dispersion-np`)
  - **陈述.** For IR-regulated partonic targets at every order of PT, at fixed $Q^2>0$, $T_{1,2}$ are analytic in the $\omega$-plane cut along real $|\omega|\ge1$; $T_1(-\omega)=T_1(\omega)$, $T_2(-\omega)=-T_2(\omega)$; ${\rm Im}\,T_i(\omega+i0)=2\pi F_i$ for $\omega\ge1$. For hadron targets see `prop:dis-dispersion-np` (later in this chapter; pointer).
  - **证明.** Crossing and ${\rm Im}\,T=2\pi W$ full; analyticity from the $\alpha$-representation at fixed $q^2<0$. (本命题只涉及部分子态。)
  - `\uses{def:dis-compton, def:ir-landau-setup, prop:prelim-optical}`

* **命题 `prop:dis-dispersion` — 色散关系：Taylor 系数 = 矩（部分子靶）** [R, R_PT] · v1→rev.
  - **陈述.** For partonic targets, for $|\omega|<1$: $T_2=\sum_{n=2,4,\dots}4\omega^{n-1}M^{(2)}_n$, $T_1-T_1(0)=\sum_{n=2,4,\dots}4\omega^nM^{(1)}_n$, $M^{(2)}_n=\int_0^1dx\,x^{n-2}F_2$, $M^{(1)}_n=\int_0^1dx\,x^{n-1}F_1$ (elastic peak included).
  - **证明.** Full (contour deformation, `fig:omega-plane`; left cut by crossing; the circle at infinity is controlled order by order in PT by the polynomial growth of the partonic amplitude). **Mandatory check:** free quark $F_2=e_q^2\delta(1-x)$ ⇒ $T_2=4e_q^2\omega/(1-\omega^2)$ (VF-CONV-14). For hadrons: `prop:dis-dispersion-np`, `prop:dis-low-moments` (pointers). (本命题只涉及部分子态。)
  - `\uses{prop:dis-compton-analytic, def:dis-compton}`

* **例 `ex:dis-free-quark` — 自由夸克的前向振幅** (no tag) · v1
  - $T_2=4e_q^2\omega/(1-\omega^2)$ and ${\rm Im}\,T_2(\omega+i0)=2\pi e_q^2\delta(1-x)$ (sign check ${\rm Im}\frac{-1}{Q^2(\omega-1)+i0}=\pi\delta(\cdot)$).
  - `\uses{prop:dis-dispersion}`

* **定义 `def:dis-twist` — 扭度与扭度 2 算符** (no tag) · v1
  - **陈述.** VF-CONV-15: $O_q^{\mu_1\cdots\mu_n}=\mathcal S\bar\psi\gamma^{\mu_1}iD^{\mu_2}\cdots iD^{\mu_n}\psi-$traces, $O_g^{\mu_1\cdots\mu_n}=\mathcal S G^{\mu_1\alpha}iD^{\mu_2}\cdots iD^{\mu_{n-1}}G_\alpha{}^{\mu_n}-$traces (sign fixed by $\langle g|O_g^{+\cdots+}|g\rangle=2(k^+)^n$, i.e. $O_g^{+\cdots+}=\sum_jG^{+j}(iD^+)^{n-2}G^{+j}$); $\langle P|O_i^{\mu_1\cdots\mu_n}|P\rangle=2A_i^{(n)}(P^{\mu_1}\cdots P^{\mu_n}-{\rm traces})$; one-gluon vertex of $O_q$ (VF-PDF-12); collinear twist $t=d-h$ of field components.
  - `\uses{def:prelim-qcd}`

* **引理 `lem:dis-twist-classification` — 扭度 2 规范不变算符的分类** [R, R_def] · refdoc S22 [PENDING-VERIFY: X3]
  - **陈述.** Collinear twist $t=d-h$ of the building blocks: $\psi_+,\bar\psi_+$: 1; $\psi_-$: 2; $D^+$: 0; $D^j$: 1; $D^-$: 2; $F^{+j}$: 1; $F^{+-},F^{ij}$: 2; $F^{-j}$: 3. Twist-2 symmetric traceless gauge-invariant operators with non-zero spin-averaged forward matrix elements are spanned, modulo total derivatives and EOM operators, by $O_q^{(n)}$ (one per flavour) and $O_g^{(n)}$ ($n$ even).
  - **证明.** Full (App M §M.6 [SYNC-APP]; boost weights from `lem:prelim-boost`). (本引理是算符的代数陈述。)
  - `\uses{def:dis-twist, lem:prelim-boost}`

* **引理 `lem:dis-twist-chirality` — 扭度奇偶性与手征** [R, R_def] · refdoc S22 [PENDING-VERIFY: X3]
  - **陈述.** For bosonic, ghost-free gauge-invariant polynomials in the symmetric traceless rank-$j$ representation, $(-1)^{d-j}=\chi$ (chirality). **Caveat (print):** false for mixed symmetry — transversity is twist 2 and chiral odd.
  - **证明.** Full (App M §M.6).
  - `\uses{def:dis-twist}`

* **引理 `lem:dis-tree-ope` — 树图 OPE** [R, R_PT] · v1
  - **陈述.** At tree level between quark states $T^{\mu\nu}$ equals the OPE with $C^{(n)}_{1,q}=C^{(n)}_{2,q}=e_q^2$ for even $n$; odd $n$ cancel between $s$- and $u$-channel graphs (crossing).
  - **证明.** Full (expand $\frac{1}{(p\pm q)^2}=\frac{-1}{Q^2(1\mp\omega)}$; blueprint S5).
  - `\uses{def:dis-twist, def:prelim-feynman-rules, def:dis-compton}`

* **命题 `prop:dis-ope-euclid` — 欧氏非例外动量下 Green 函数的逐图渐近展开** [A] · refdoc S19 [PENDING-VERIFY: X3, S63-1]
  - **陈述.** At each order, for Euclidean non-exceptional $(p,q)$, the T-product Green function of two currents with elementary external fields admits $\tilde G^T-\sum_{d_O\le a}\tilde C_O(q;\mu)\tilde G_{[O]}=O(|q|^{D-1-a}\ln^k|q|)$ in an operator basis that includes gauge-variant and ghost operators; the coefficients are $|q|^{D-d_O}\times$ polynomials in $\ln(q^2/\mu^2)$ and are **unique** (log-polynomial argument, `lem:appM-uniqueness`).
  - **证明.** Sketch; location App M §M.5 (cited graph-by-graph DR asymptotic-expansion theorems and BPHZL convergence: `Smirnov:1990rz`, `Smirnov2002`, `Chetyrkin:1982zq`, `LowensteinZimmermann1975`, `Zimmermann1973`; BPHZL vs DR+$R^*$).
  - **地位与缺口.** Tag [A] under the binding decision D3 (v1 §0.9 item 4 did not adopt the grade "[R] in PT as a combination of classical results" of the frontier report); upgrade path: [R, R_PT] if the verification confirms that the cited theorems jointly cover QCD with quarks, ghosts and gauge-variant operators (S63-1); then Ch25 open problem OP-A2 is reworded. Related open input of App M: `asm:appM-remainder` (momentum-space remainder estimate for the frozen-$q$ bilocal normal product; possibly dischargeable via `Anikin:1978tj`, `Zavyalov:1990kv` and uniqueness, S63-2). Error type: E-P per graph (where the cited theorems apply). (本命题只涉及部分子态的 Green 函数。)
  - `\uses{lem:dis-tree-ope, thm:qcd-renormalizability, thm:ee-euclid-ir, lem:appM-uniqueness, asm:appM-remainder}`

* **命题 `prop:dis-ope-gi` — 物理矩阵元只需规范不变算符** [A] · refdoc S19 [PENDING-VERIFY: X3, S63-3] (composite)
  - **陈述.** (a) For $j^\mu j^\nu$ between physical states only gauge-invariant operators contribute; at twist 2 only $O_q$, $O_g$. (b)（蕴含关系，\tagR，$R_{\rm cond}$）Given `prop:dis-ope-euclid`, (a) follows under `asm:appM-brst-ope` (BRST-symmetric renormalized insertions with classical coefficients and Ward identities; the Euclidean remainder also with $s\phi$ insertions).
  - **证明.** (b) full in App M §M.6 [SYNC-APP]. Literature: `Joglekar:1976eb`, `Joglekar:1976pe` (QCD currents), `Hollands:2007zg` (pure YM), `thm:prelim-composite-renorm`.
  - **地位与缺口.** [A] = the status of `asm:appM-brst-ope` (partly dischargeable by Joglekar 1977, Hollands 2008, S63-3); forward on-shell caveat as in `thm:prelim-composite-renorm`.
  - `\uses{prop:dis-ope-euclid, thm:prelim-composite-renorm, lem:dis-twist-classification, asm:appM-brst-ope}`

* **命题 `prop:dis-ope-forward` — 前向在壳部分子矩阵元** [A] · refdoc S19 [PENDING-VERIFY: X3, S63-4] (composite; fixes OUR-8)
  - **陈述.** (a) For on-shell massless partons in DR, at fixed order: $T_2^{(j)}=4\sum_{n\,{\rm even}}\omega^{n-1}\sum_iC^{(n)}_{2,i}A^{(n)}_{i/j}$ uniformly on $|\omega|\le r<1$, with $A^{(n)}_{i/j}$ the partonic matrix elements ($\delta_{ij}$ plus pure $\overline{\rm MS}$ counterterms). (b)（蕴含关系，\tagR，$R_{\rm cond}$）(a) follows from `prop:dis-ope-euclid`, `prop:dis-ope-gi` under `asm:appM-forward` (the OPE remainder for forward on-shell massless partonic matrix elements, which are at exceptional momenta): scaleless matrix elements force twist 2 (`lem:prelim-scaleless`); Taylor-coefficient contradiction argument. Remark: amplitude form $\sum_q\int_{-1}^1\hat H_q(\xi\omega)f_q+\int_0^1\hat H_gf_g$ (no $d\xi/\xi$; odd extension; gluon factor 2).
  - **证明.** (b) full in App M §M.7 [SYNC-APP]. Check: exact in $\varepsilon$ at $O(\alpha_s)$, $N\le8$ (c_dis `ope_check`, VF-DIS-13).
  - **地位与缺口.** [A] = the status of `asm:appM-forward`; never write 「前向在壳部分子矩阵元直接给出 Wilson 系数，无需额外步骤」 (S58).
  - `\uses{prop:dis-ope-euclid, prop:dis-ope-gi, lem:prelim-scaleless, asm:appM-forward}`

* **定理 `thm:dis-ope` — 重整化微扰论中的欧氏 OPE** [A] · v1→rev. (umbrella; refdoc S19)
  - **陈述.** "The three statements `prop:dis-ope-euclid`, `prop:dis-ope-gi`, `prop:dis-ope-forward`", i.e. for Green functions of $Tj^\mu j^\nu$ with IR-regulated partonic external momenta, as $Q^2\to\infty$ (Euclidean $q$, or for each fixed Taylor coefficient in $\omega$ for forward partonic matrix elements): $$T^{\mu\nu}=\sum_{n=2,4,\dots}\sum_i\Big[\Big(-g^{\mu\nu}+\frac{q^\mu q^\nu}{q^2}\Big)\frac{2^nq_{\mu_1}\cdots q_{\mu_n}}{(Q^2)^n}C^{(n)}_{1,i}+\Big(g^\mu{}_{\mu_1}-\frac{q^\mu q_{\mu_1}}{q^2}\Big)\Big(g^\nu{}_{\mu_2}-\frac{q^\nu q_{\mu_2}}{q^2}\Big)\frac{2^nq_{\mu_3}\cdots q_{\mu_n}}{(Q^2)^{n-1}}C^{(n)}_{2,i}\Big]O_i^{\mu_1\cdots\mu_n}+R,$$ $C$ independent of external states and IR regulators, $R$ = twist $\ge4$ contributions, $O(Q^{-2})\times$logs for each fixed $n$. With $\langle P|O_i|P\rangle$ normalized as in `def:dis-twist`: $T_1\ni2\omega^nC^{(n)}_{1,i}A^{(n)}_i$, $T_2\ni4\omega^{n-1}C^{(n)}_{2,i}A^{(n)}_i$ (VF-DIS-13).
  - **证明.** By the three propositions (the steps of `thm:ee-ope`, now with quark and gluon external states and operators of every spin).
  - **地位与缺口 (verbatim in substance, survey item 1).** Proven to all orders in PT for scalar theories (`Zimmermann1973`, `Zimmermann:1972te`, `Zimmermann1970`; convergence at each order in $\varphi^4$: `Hollands:2011gf`, `Holland:2014pna`) and for gauge-invariant operators in pure Yang–Mills (`Hollands:2007zg`; IR control `Frob:2015uqy`); for QCD with quarks "proved in a gauge theory the same way" (`Collins1984` §12.8) or "widely assumed" (`IzubuchiEtAl2018` Sec. II); gauge-theory ingredients `Joglekar:1976eb`, `Joglekar:1976pe`. The [A] refers to all three sub-statements (the first by D3, the others by `asm:appM-brst-ope`, `asm:appM-forward`). Not valid beyond PT without `asm:intro-np-ope`, `asm:intro-af-coeff`. Attribution per A09 [PENDING-VERIFY: A09].
  - `\uses{prop:dis-ope-euclid, prop:dis-ope-gi, prop:dis-ope-forward}`

* **命题 `prop:dis-chiral-suppression` — 奇扭度系数的手征压低** [R, R_PT] · refdoc S22 [PENDING-VERIFY: X3]
  - **陈述.** In massless PT, every graph contributing to a chiral-odd structure of the T-product of two vector currents between quark states vanishes at every order (even number of $\gamma$ matrices on each open quark line; DR-safe, no $\gamma_5$); hence all chiral-odd (odd-twist, by `lem:dis-twist-chirality`) OPE coefficients vanish in massless PT. Non-perturbatively, the suppression of odd-twist coefficients is part of `asm:intro-np-ope`(O2) (chiral symmetry breaking, $U(1)_A$, instantons $e^{-2\pi/\alpha_s}$).
  - **证明.** Full ($\gamma$-parity of open quark lines; App M §M.6). (本命题只涉及部分子态。)
  - `\uses{lem:dis-twist-chirality, def:prelim-feynman-rules}`

* **命题 `prop:dis-wilson-partons` — 由部分子结构函数提取 Wilson 系数** [R, R_OPE] · v1
  - **陈述.** $\int_0^1dz\,z^{n-2}\hat F_2^{(j)}=\sum_iC^{(n)}_{2,i}\langle j|O^{(n)}_i|j\rangle$ with partonic matrix elements $=\delta_{ij}$ plus pure $\overline{\rm MS}$ counterterms (all loop corrections to $\langle j|O_i|j\rangle$ are scaleless in DR for massless on-shell partons; the PDF analogue is `prop:pdf-partonic-dr`, Ch8 — pointer). One-loop check exact in $\varepsilon$ (VF-DIS-13).
  - **证明.** Full at one loop; all orders from `prop:dis-ope-forward` and `prop:dis-dispersion`. (本命题只涉及部分子态。)
  - `\uses{thm:dis-ope, prop:dis-ope-forward, lem:prelim-scaleless, prop:dis-dispersion}`

* **命题 `prop:dis-ope-rg` — Wilson 系数与约化矩阵元的重整化群** [R, R_OPE] · v1 (proof route refdoc S22)
  - **陈述.** In the convention VF-CONV-16: $\frac{dA^{(n)}_i}{d\ln\mu^2}=\sum_j\Gamma_{ij}(n,\alpha_s)A^{(n)}_j$, $\Gamma_{ij}=\frac{\alpha_s}{2\pi}\gamma_{ij}(n)+O(\alpha_s^2)$, $\gamma_{ij}(n)=\int_0^1z^{n-1}P_{ij}$; $\frac{dC^{(n)}_{a,j}}{d\ln\mu^2}=-\sum_iC^{(n)}_{a,i}\Gamma_{ij}$. Dictionary to MVV and to Gross–Wilczek printed (VF-PDF-10).
  - **非微扰地位.** 强子矩阵元 $A^{(n)}$：\cref{asm:intro-wightman}、\cref{asm:intro-composite}（MA0）。
  - **证明.** Full, **derived from the exact uniqueness of the coefficients** (`prop:dis-ope-euclid`, `lem:appM-uniqueness`; refdoc S22, Prop C.46 route) together with `thm:prelim-composite-renorm` and `prop:qcd-rge`.
  - `\uses{prop:dis-ope-euclid, thm:dis-ope, lem:appM-uniqueness, thm:prelim-composite-renorm, prop:qcd-rge, asm:intro-wightman, asm:intro-composite}`

* **引理 `lem:dis-euclid-segment` — 欧氏点在 $\omega$ 平面上的位置** [R, R_def] · refdoc S20 [PENDING-VERIFY: X3]
  - **陈述.** In the rest frame of the target, Euclidean $q=(iq^4,\mathbf q)$ with $|\mathbf q|\ge Q/2$ gives $\omega=2iMq^4/Q^2\in\mathcal I_Q\equiv\{iy:|y|\le\sqrt3M/Q\}$, and every point of $\mathcal I_Q$ is attained; $\hat P^2=M^2\mathbf q^2/Q^2$; projector $T_2=\frac{3\nu}{2(\hat P^2)^2}[\hat P_\mu\hat P_\nu-\frac{\hat P^2}3g_{\mu\nu}]T^{\mu\nu}$, $\hat P=P-\frac{P\cdot q}{q^2}q$ (VF-REF-1). `fig:dis-euclid-segment`.
  - **证明.** Full (elementary kinematics).
  - `\uses{def:dis-compton}`

* **命题 `prop:dis-dispersion-np` — 由 Wightman 公理得到的有限减除色散关系** [R, R_cond] · refdoc S21 [PENDING-VERIFY: X3]
  - **陈述.** 前提：\cref{asm:intro-wightman}。For a hadron target: (a) $T_2$ is analytic in $\mathbb C\setminus((-\infty,-1]\cup[1,\infty))$, odd, real-analytic; (b) $|T_2(\omega)|\le C_Q(1+|\omega|)^A|{\rm Im}\,\omega|^{-B}$ with $A,B$ independent of $Q$; (c) ${\rm Disc}\,T_2=4\pi iF_2(1/\omega)d\omega\ge0$; (d) for every even $n_0>A+2$: $T_2(\omega)=\sum_{n<n_0}t_n\omega^{n-1}+4\omega^{n_0-1}\int_0^1dx\,\frac{x^{n_0-2}F_2(x)}{1-x^2\omega^2}$ (VF-REF-4).
  - **证明.** Full in App M §M.8 [SYNC-APP]: forward tube, Vladimirov bound (`Streater:1989vi`), edge of the wedge with $Q^2$-smearing (`Epstein1960`), positivity (`prop:dis-W-structure`), almost-analytic extension + Green's formula, `lem:appK-entire`. Replaces the hadronic part of v1's `prop:dis-compton-analytic` and the phrase "drop the circle at infinity under MA3".
  - `\uses{def:dis-compton, prop:dis-W-structure, lem:appK-entire, asm:intro-wightman}`

* **命题 `prop:dis-low-moments` — 低阶矩与增长条件的等价** [R, R_def] · refdoc S21 [PENDING-VERIFY: X3]
  - **陈述.** Suppose the representation (d) of `prop:dis-dispersion-np` holds for some even $n_0\ge4$. Then $t_n=4\int_0^1x^{n-2}F_2$ for all even $2\le n<n_0$ **iff** $\lim_{y\to\infty}T_2(iy)/(iy)=0$, i.e. iff $\int F_2<\infty$ and there is no real "fixed-pole" term $c\,\omega$. Regge behaviour of $F_2$ is neither necessary nor sufficient. Hence the momentum sum rule needs `asm:intro-growth`.
  - **证明.** Full (descending induction).
  - `\uses{def:dis-compton}`

* **引理 `lem:dis-ope-segment` — OPE 在线段上的多项式逼近** [R, R_cond] · refdoc S20 [PENDING-VERIFY: X3]
  - **陈述.** 前提：\cref{asm:intro-np-ope}。If (O1) of `asm:intro-np-ope` holds to level $N$ with covariant coefficients $|\tilde C_j|\le K|q|^{2-d_j}\ln^k|q|$, twist $\ge2$, chiral suppression for odd twist (O2), and twist 2 only from $O_q,O_g$ (`lem:dis-twist-classification`), then there is an odd polynomial $\mathcal P_N(\omega)=\sum_{n\le N-2}\pi_n\omega^{n-1}$ with $\sup_{\mathcal I_Q}|T_2-\mathcal P_N|\le K_N(M/Q)^{N-2}\ln^kQ$ and $\pi_n=4\sum_iC^{(n)}_{2,i}A^{(n)}_i+O(\frac{M^2+mM}{Q^2}\ln^kQ)$.
  - **证明.** Full in App M §M.8 (projector of `lem:dis-euclid-segment`; `lem:appK-markov`).
  - `\uses{lem:dis-euclid-segment, lem:dis-twist-classification, lem:appK-markov, asm:intro-np-ope}`

* **定理 `thm:dis-fixed-n` — 由定域 OPE 得到固定 $n$ 的 Taylor 系数** [R, R_cond] · refdoc S20 [PENDING-VERIFY: X3]
  - **陈述.** 前提：\cref{asm:intro-np-ope}、\cref{asm:intro-wightman}（经由 \cref{lem:dis-ope-segment}、\cref{prop:dis-dispersion-np}）。Assume `lem:dis-ope-segment` for every even $N$; $T_2$ analytic and odd in $|\omega|<1$; $F_2\,dx\ge0$ (including the elastic point); a $Q$-independent even $n_0$ with $t_n=4\int x^{n-2}F_2$ for even $n\ge n_0$. Then for **every** even $n\ge2$: $t_n(Q^2)=4\sum_iC^{(n)}_{2,i}A^{(n)}_i+O(\frac{M^2+mM}{Q^2}\ln^kQ)$. No sum over spins and no interchange of limits is used.
  - **证明.** Full in App M §M.8 (positivity tail; Markov's inequality; bootstrap of $t_{n_0}$). Status: positivity makes it inherently non-perturbative; the PT analogue is `prop:dis-ope-forward`. Misconception M34: 「欧氏 OPE 代入、收缩、比较系数即得强子结构函数的矩」 is false.
  - `\uses{lem:dis-ope-segment, prop:dis-dispersion-np, prop:dis-W-structure, lem:appK-markov, asm:intro-np-ope, asm:intro-wightman}`

* **定理 `thm:dis-moments-np` — DIS 矩因子化的非微扰条件定理** [R, R_cond] · refdoc S22 [PENDING-VERIFY: X3]
  - **陈述.** 前提：\cref{asm:intro-wightman}、\cref{asm:intro-composite}、\cref{asm:intro-np-ope}、\cref{asm:intro-af-coeff}（对 $n<n_0$ 另需 \cref{asm:intro-growth}）。(i) The coefficients defined at $\mu$ by the exact operator RG from $\mu_0$ satisfy (O1) at every $\mu$ and the RG equation; $C^{(n)}_{2,i}(\frac{Q^2}{\mu^2},\alpha_s(\mu))=\sum_jC^{(n)}_{2,j}(1,\alpha_s(Q))[\mathcal P\exp(-\int_\mu^Q\frac{d\mu'}{\mu'}\gamma^{(n)})]_{ji}$, with $C(1,\alpha_s(Q))$ asymptotic to the $\overline{\rm MS}$ series. (ii) For even $n\ge n_0$: $\int_0^1x^{n-2}F_2=\sum_iC^{(n)}_{2,i}A^{(n)}_i+O(\frac{\Lambda_h^2}{Q^2}\ln^kQ)$; with `asm:intro-growth`, for all even $n\ge2$. (iii) Under the hypothesis (Φ) of `cor:dis-weak-xspace`, weak $x$-space convergence.
  - **证明.** Full in App M §M.8 (norm bound on the evolution operators from asymptotic freedom with the mass-mixing rescaling, using the operator RG of `thm:prelim-composite-renorm` and `prop:qcd-rge` directly — not the R_OPE statement `prop:dis-ope-rg`, which would add `thm:dis-ope` to the premises (WRITER_SPEC_v2 v2.1 §4.6 item 1); verification of the hypotheses of `thm:dis-fixed-n`; `prop:dis-low-moments` for $n<n_0$).
  - `\uses{thm:dis-fixed-n, prop:dis-dispersion-np, prop:dis-low-moments, thm:prelim-composite-renorm, prop:qcd-rge, thm:qcd-asymptotic-freedom, asm:intro-wightman, asm:intro-composite, asm:intro-np-ope, asm:intro-af-coeff, asm:intro-growth}`

* **推论 `cor:dis-weak-xspace` — $x$ 空间的弱收敛** [R, R_cond] · refdoc S22 [PENDING-VERIFY: X3]
  - **陈述.** 前提：\cref{asm:intro-wightman}、\cref{asm:intro-composite}、\cref{asm:intro-np-ope}、\cref{asm:intro-af-coeff}（经由 \cref{thm:dis-moments-np}）。If finite signed measures $\Phi_Q$ on $[0,1]$ have the twist-2 moments (hypothesis (Φ)), then $\int x^{n_0-2}\phi\,d(F_2dx-\Phi_Q)=O(\frac{M^2+mM}{Q^2}\ln^kQ)$ for polynomials $\phi$ in $x^2$, and $\to0$ for all continuous $\phi$ under uniform mass bounds. A pointwise $O(1/Q^2)$ is impossible from the OPE (`rem:dis-nonuniform`, pointer); the existence of $\Phi_Q$ is a Hausdorff moment problem (App K, `rem:appK-counterexamples`).
  - **证明.** Full (App M §M.8; Weierstrass approximation; App A test-function class).
  - `\uses{thm:dis-moments-np, lem:appA-weak-convergence, lem:appK-hausdorff}`

* **定理 `thm:dis-moments` — DIS 结构函数矩的因子化** [R, R_OPE] · v1→rev. (refdoc S22; fixes OUR-3)
  - **陈述.** (a) For IR-regulated partonic targets, every even $n\ge2$, as $Q^2\to\infty$ at fixed $n$: $$\int_0^1dx\,x^{n-2}F_2(x,Q^2)=\sum_iC^{(n)}_{2,i}\Big(\frac{Q^2}{\mu^2},\alpha_s(\mu)\Big)A^{(n)}_i(\mu)+O\Big(\frac1{Q^2}\Big),\qquad 2\int_0^1dx\,x^{n-1}F_1=\sum_iC^{(n)}_{1,i}A^{(n)}_i+O\Big(\frac1{Q^2}\Big),$$ $i\in\{q,\bar q,g\}$, $A^{(n)}_q=\int_0^1x^{n-1}(q+\bar q)$ for even $n$ (after Ch8: `thm:pdf-moments-local`). (b) For hadrons: the same for even $n\ge n_0$; for all even $n\ge2$ under `asm:intro-growth`. The $O(1/Q^2)$ (twist 4, target mass) is not uniform in $n$ (resonances dominate for $n\gtrsim Q^2/M^2$).
  - **非微扰地位.** \cref{asm:intro-wightman}、\cref{asm:intro-composite}、\cref{asm:intro-np-ope}、\cref{asm:intro-af-coeff}（MA0、MA4）；$n<n_0$ 另需 \cref{asm:intro-growth}（MA3）。
  - **证明.** (a) full given `prop:dis-ope-forward` and `prop:dis-dispersion` (compare Taylor coefficients at $\omega=0$ for each fixed $n$; no convergence of the OPE in $\omega$ and no interchange of limits). (b) `thm:dis-fixed-n` + `prop:dis-dispersion-np` + `thm:dis-moments-np`. "Insert, contract, compare" is **not** a proof for hadrons (M34). Pointer: lattice tests of the moments (Ch22, `prop:lattice-moments`).
  - `\uses{def:dis-kinematics, prop:dis-dispersion, prop:dis-ope-forward, thm:dis-ope, thm:dis-fixed-n, prop:dis-dispersion-np, thm:dis-moments-np, asm:intro-wightman, asm:intro-composite, asm:intro-np-ope, asm:intro-af-coeff, asm:intro-growth}`

* **推论 `cor:dis-scaling` — 标度破坏** [R, R_OPE] · v1
  - **陈述.** Non-singlet LO: $M_n^{\rm NS}(Q^2)=M_n^{\rm NS}(Q_0^2)[\alpha_s(Q^2)/\alpha_s(Q_0^2)]^{-2\gamma_{qq}(n)/\beta_0}$; $n=2$ singlet: eigenvalues $0$ and $-\frac{4C_F+2n_fT_F}3$ of the $\gamma$-matrix; asymptotic quark momentum fraction $\frac{3n_f}{16+3n_f}$ (SU(3)) (VF-PDF-9).
  - **非微扰地位.** \cref{asm:intro-wightman}、\cref{asm:intro-composite}、\cref{asm:intro-np-ope}、\cref{asm:intro-af-coeff}；$n=2$ 的强子陈述另需 \cref{asm:intro-growth}。
  - `\uses{thm:dis-moments, prop:dis-ope-rg, prop:prelim-beta}`

* **例 `ex:dis-n2` — $n=2$：能动张量** (no tag) · v1
  - Energy–momentum tensor, $\sum_iA^{(2)}_i=1$ RG invariant, eigenvalue $0$; for hadrons the momentum sum rule is exactly the growth condition (`prop:dis-low-moments`).
  - `\uses{thm:dis-moments, prop:dis-ope-rg, prop:dis-low-moments}`

* **命题 `prop:dis-c-oneloop` — 单圈 Wilson 系数** [R, R_PT] · v1
  - **陈述.** (At one loop.) $C^{(n)}_{2,q}=e_q^2[1+\frac{\alpha_s}{2\pi}(C^q_{2,N}+\gamma_{qq}(N)\ln\frac{Q^2}{\mu^2})]_{N=n}$, gluon $C^{(n)}_{2,g}=\sum_qe_q^2\frac{\alpha_s}{2\pi}2(C^g_{2,N}+\gamma_{qg}(N)\ln\frac{Q^2}{\mu^2})$, $C_L$ similarly, with VF-DIS-8 closed forms and the table $N=1..8$. Checks: $C^q_{2,1}=0$ (Adler), $C^q_{1,1}=-C_F$ (Bjorken $\nu$ sum rule) (VF-DIS-14); MVV normalization $c^{(1)}_{2,\rm ns}=2C^q_{2,N}$; a variant with $\frac2{N+1}+\frac1{N^2}$ fails the Adler check (critic c2) — print it as a warning without attributing it to a source unless the verification finds one [PENDING-VERIFY: E32].
  - **证明.** Two self-contained derivations: (i) cut diagrams in $D$ dimensions (App G `sec:appG-dis`; VF-DIS-3…7; `fig:dis-oneloop`) followed by Mellin moments, giving the closed forms for all $N$ (VF-DIS-8); (ii) hard-region forward Compton amplitude exactly in $\varepsilon$, $N\le8$ (VF-DIS-13). The $x$-space coefficient functions are presented in Ch10 (`prop:disall-nlo`), which refers back. (本命题只涉及部分子态。)
  - `\uses{lem:dis-tree-ope, prop:sudakov-oneloop, lem:prelim-plus-expansion, lem:prelim-mellin, prop:dis-dispersion}`

* **例 `ex:dis-oneloop-ope` — 单圈 OPE 检验** (no tag) · v1
  - The hard-region forward Compton amplitude reproduces the moments of the cut calculation exactly in $\varepsilon$ ($N\le8$); renormalized Wilson coefficients and the residues $-\gamma_{qq}(N)$, $-\gamma_{qg}(N)$ (c_dis §11) — the explicit one-loop instance of `prop:dis-ope-forward`.
  - `\uses{prop:dis-c-oneloop, prop:dis-ope-forward}`

* **注 `rem:dis-uniqueness` — 偶数矩决定 C 偶组合（数学）** (no tag) · v1
  - (VF-PDF-15.) Statement of `thm:appK-even-moments` and `cor:appK-pdf`: even moments ($N\ge N_1$) determine $q+\bar q$ and $g$ a.e. (for $x^{N_1-1}(\cdot)\in L^1$); odd moments determine $q-\bar q$; fails for distributions supported at $x=0$ ($\delta'$: all even moments vanish); continuation in $N$ unique under polynomial bounds (`prop:appK-continuation`); Carlson's sharp form; $P^+_{\rm NS}\ne P^-_{\rm NS}$ from NLO (`rem:pdf-ns-plusminus`, pointer). (M5, M6.)
  - `\uses{thm:appK-even-moments, cor:appK-pdf, prop:appK-continuation, thm:appK-carlson}`

* **注 `rem:dis-nonuniform` — 矩的 $O(1/Q^2)$ 不蕴含逐点 $O(1/Q^2)$** (no tag) · v1
  - $R_Q(x)=\sin(Q^2x)$ has $|Q^2\int x^nR_Q|\le c_n$ for all $n$ but $\sup|R_Q|=1$ (VF-MISC-3, critic c5). Consequence: the pointwise $x$-space statement is the [A] theorem `thm:disall-factorization` (pointer; critic O7; C4; M4); the best the OPE gives is the weak convergence of `cor:dis-weak-xspace`.

* **命题 `prop:dis-light-cone` — 光锥展开** [A] · v1
  - **陈述.** Near $z^2=0$ the current product expands in towers of fixed twist, each containing all spins $n$; leading tower twist 2.
  - **地位与缺口.** Literature `BrandtPreparata1971`, `Frishman1971`, `Frishman:1970fx`, `ChristHasslacherMueller1972`, `Anikin:1978tj` (arbitrary order of PT; theory class not checked), `Zavyalov:1990kv`, light-ray operators `Balitsky:1987bk`, `MullerEtAl1994`. Explain why moments need only the short-distance theorem while fixed-$x$ statements are light-cone statements.
  - `\uses{prop:dis-ope-euclid, def:dis-twist}`

* **命题 `prop:dis-twist4` — 扭度 4 修正的算符结构** [R, R_OPE] · v1
  - **陈述.** $1/Q^2$ corrections to each moment from twist-4 operators (quark–gluon–quark, four-quark), their anomalous dimensions and mixing with EOM operators; matrix elements non-perturbative.
  - **非微扰地位.** \cref{asm:intro-wightman}、\cref{asm:intro-composite}、\cref{asm:intro-np-ope}、\cref{asm:intro-af-coeff}（MA0、MA4）。
  - **证明.** Sketch; `EllisFurmanskiPetronzio1982`, `EllisFurmanskiPetronzio1983`, `Jaffe:1982pm`, `Jaffe1983`, `Qiu:1988dn` (survey item 21: [R] in moment space modulo item 1). The twist-2 coefficients are meaningful only to relative $O(\Lambda^2/Q^2)$ unless the basis is fixed non-perturbatively (forward pointer `prop:power-rearrangement`).
  - `\uses{thm:dis-ope, thm:prelim-composite-renorm, def:dis-twist, asm:intro-wightman, asm:intro-composite, asm:intro-np-ope, asm:intro-af-coeff}`

* **命题 `prop:dis-tmc` — 靶质量修正** [R, R_OPE] · v1
  - **陈述.** The trace terms of twist-2 matrix elements give target-mass corrections to the moments (Nachtmann moments; Georgi–Politzer); x-space representation with $\xi_N=2x/(1+\sqrt{1+4M^2x^2/Q^2})$; the "threshold problem" ($F_2^{\rm TMC}\ne0$ at $x>1$) shows the non-uniformity of the $M^2/Q^2$ expansion near $x\to1$ (prescription dependent in $x$ space).
  - **非微扰地位.** as `thm:dis-moments`.
  - **证明.** Sketch; `GeorgiPolitzer1976`, `Nachtmann1973`.
  - `\uses{thm:dis-moments, def:dis-twist, asm:intro-wightman, asm:intro-composite, asm:intro-np-ope, asm:intro-af-coeff}`

* **例 `ex:dis-tmc-n2` — 第二阶矩的靶质量修正** (no tag) · v1 (+ VF-REF-6)
  - $O(M^2/Q^2)$ correction from the trace terms; general coefficient $\frac{n(n-1)}{n+2}\frac{M^2}{Q^2}a_{n+2}$ (VF-REF-6, verified).
  - `\uses{prop:dis-tmc}`

* **定理 `thm:dis-bjorken` — Bjorken 求和规则** [R, R_OPE] · v1
  - **陈述.** $\int_0^1dx\,[g_1^p-g_1^n](x,Q^2)=\frac{g_A}6\big[1-a-(\frac{55}{12}-\frac{n_f}3)a^2+O(a^3)\big]+O(\Lambda^2/Q^2)$, $a=\alpha_s(Q^2)/\pi$, SU(3), $\overline{\rm MS}$ with the HVBM–Larin $\gamma_5$ scheme (non-singlet: scheme independent after Larin's finite renormalization); inputs: isospin, $g_A$ from $\beta$ decay.
  - **非微扰地位.** \cref{asm:intro-wightman}、\cref{asm:intro-composite}、\cref{asm:intro-np-ope}、\cref{asm:intro-af-coeff}；第一阶矩另需 \cref{asm:intro-growth}（极化振幅的相应增长条件）。
  - **证明.** OPE with odd-$n$ axial operators; $a^2$ coefficient verified via the Crewther relation (VF-POL-1/2, critic c4); literature `Bjorken1966`, `Kodaira1980`, `LarinVermaseren1991`, `Larin:1993tq`.
  - `\uses{thm:dis-ope, def:prelim-gamma5, prop:appI-larin, asm:intro-wightman, asm:intro-composite, asm:intro-np-ope, asm:intro-af-coeff, asm:intro-growth}`

* **注 `rem:dis-crewther` — Crewther 关系** (no tag) · v1
  - One formula, verified at $O(a^2)$: $C_{\rm Bjp}D_{\rm NS}=1+\beta_0(\frac78-\zeta_3)a^2+\dots$, $K_1=C_F(-\frac{21}8+3\zeta_3)$ (VF-POL-2).

**Worked examples.** `ex:dis-free-quark`, `ex:dis-n2`, `ex:dis-oneloop-ope`, `ex:dis-tmc-n2`.

**Tables.** `tab:dis-correspondence` — rows: `prop:dis-ope-euclid` ↔ App M §M.5 (cited theorems; S63-1); `prop:dis-ope-gi` ↔ App M §M.6 (`asm:appM-brst-ope`); `prop:dis-ope-forward` ↔ App M §M.7 (`asm:appM-forward`); `prop:dis-dispersion-np`, `lem:dis-ope-segment`, `thm:dis-fixed-n`, `prop:dis-low-moments`, `thm:dis-moments-np`, `cor:dis-weak-xspace` ↔ App M §M.8 (`asm:intro-*`); columns: chapter statement | precise version | what differs (assumptions; error type E-P/E-N) [SYNC-APP].

**Figures.** Existing (tikz1): `fig:dis-kinematics`, `fig:forward-compton`, `fig:omega-plane`, `fig:ope-schematic`, `fig:dis-oneloop` (owner; Ch10 refers back); existing (tikz3): `fig:higher-twist` (owner; Ch21 refers back); new (required, refdoc S56): `fig:dis-euclid-segment`; optional: `fig:dis-twist-graphical`.

**Misconception box.** M3, M4, M5, M6 (first statement), **M34**; "Adler sum rule receives QCD corrections" (it does not: $C^q_{2,1}=0$ to all orders by current conservation, `Adler1966`; for hadrons it is a low-moment statement needing `asm:intro-growth`); "Bloom–Gilman duality is a theorem" ([C], `BloomGilman1970`); critic C4, C15; O4, O5, O6, O7.

**Key citation keys.** `Bjorken1969`, `Wilson1969`, `Zimmermann1973`, `Zimmermann:1972te`, `Zimmermann1970`, `Wilson:1972ee`, `BrandtPreparata1971`, `Frishman1971`, `Frishman:1970fx`, `ChristHasslacherMueller1972`, `Anikin:1978tj`, `Zavyalov:1990kv`, `Balitsky:1987bk`, `MullerEtAl1994`, `Joglekar:1976eb`, `Joglekar:1976pe`, `Collins1984`, `Hollands:2007zg`, `Hollands:2011gf`, `Holland:2014pna`, `Frob:2015uqy`, `IzubuchiEtAl2018`, `Smirnov:1990rz`, `Smirnov2002`, `Chetyrkin:1982zq`, `LowensteinZimmermann1975`, `Streater:1989vi`, `Epstein1960`, `Markoff1916`, `Callan:1973pu`, `GrossWilczek1973b`, `GrossWilczek1974`, `GeorgiPolitzer1974`, `GeorgiPolitzer1976`, `Nachtmann1973`, `BardeenEtAl1978`, `FloratosRossSachrajda1977`, `Vermaseren:2005qc`, `Moch:2004xu`, `AltarelliMartinelli1978`, `Muta2010`, `PeskinSchroeder1995`, `EllisFurmanskiPetronzio1982`, `EllisFurmanskiPetronzio1983`, `Jaffe:1982pm`, `Jaffe1983`, `Qiu:1988dn`, `Bjorken1966`, `Kodaira1980`, `LarinVermaseren1991`, `Larin:1993tq`, `Adler1966`, `BloomGilman1970`.

**Pending.** All refdoc S19–S22 statements [PENDING-VERIFY: X3]; `prop:dis-ope-euclid` upgrade path [S63-1, S63-2]; `prop:dis-ope-gi` [S63-3]; `prop:dis-ope-forward` [S63-4]; `thm:dis-ope` status wording [A09]; `prop:dis-c-oneloop` warning [E32].

---------------------------------------------------------------------------------------------------

## Chapter 8 — 严格核心 III：部分子分布与碎裂函数的算符定义 / Rigorous core III: operator definitions of PDFs and FFs

`\label{ch:pdf}` · `ch08_pdf.tex` · **15 pp** · full (all-order moment proof in App L) · Part II

**Purpose.** Define PDFs/FFs as gauge-invariant renormalized matrix elements (critic C1: before any factorization theorem); prove their basic properties (gauge invariance, free-field values, support, moments = local twist-2 matrix elements, DGLAP from operator renormalization, sum rules); compute the one-loop kernel directly from the operator definition; complete the $x$-space DIS theorem for the twist-2 part; discuss interpretation (number density, heuristic), the residual gauge freedom of light-cone gauge, positivity ([C]; all-scale positivity is false); FFs and timelike evolution, with the independent input that FF moments are not local operators; polarized (helicity, transversity) definitions.

**Depends on.** Ch2 (`thm:prelim-composite-renorm`, `prop:qcd-rge`, `prop:prelim-beta`, `def:prelim-msbar`, `def:prelim-feynman-rules`), Ch3 (Wilson lines, Mellin, `lem:prelim-scaleless`, `lem:prelim-boost`, `def:prelim-gamma5`), Ch4 (`def:ir-landau-setup`), Ch7 (`thm:dis-moments`, `def:dis-twist`, App K lemmas); App L.

**Box.**
- 证明了：`prop:pdf-invariance`、`lem:pdf-wilson-moments`（[R, R_def]）；`thm:pdf-support-pt`、`thm:pdf-moments-local`、`thm:pdf-dglap`、`prop:pdf-lo-kernels`、`prop:pdf-pqq-operator`、`prop:pdf-partonic-dr`、`prop:pdf-local-anomalous`、`prop:pdf-sum-rules`（[R, R_PT]；强子版本需 `asm:intro-composite`）；`thm:pdf-dis-xspace`（[R, R_OPE]）；`prop:pdf-timelike-dglap` 的单圈内容（[R, R_PT]）。
- 给出全阶论证：`prop:pdf-support-hadron`（[A]）；`prop:pdf-timelike-dglap`（[A]：碎裂函数的乘法可重整性是独立输入，`asm:appN-multren`(Z1)）。
- 没有证明：$\overline{\rm MS}$ PDF 在某一非微扰标度以上的正定性（`conj:pdf-positivity`，[C]；在所有标度上非负是错的）；数密度诠释（启发式，`rem:pdf-number-density`）；非定域算符的 BRST 分类（第~24~章讨论其矩约化）。

**Sections.**
1. `sec:pdf-definitions` 定义：夸克、反夸克与胶子分布 (`fig:pdf-operator`; optional `fig:pdf-gluon-operator`).
2. `sec:pdf-properties` 规范不变性、自由场值与支撑.
3. `sec:pdf-interpretation` 数密度诠释及其局限（启发式）；光锥规范的剩余规范自由.
4. `sec:pdf-moments` 矩与定域算符.
5. `sec:pdf-dglap` 重整化与 DGLAP 方程 (`fig:dglap-ladder`, `fig:splitting-vertices`).
6. `sec:pdf-oneloop` 单圈计算：由算符定义得到 $P_{qq}$ (`fig:pdf-oneloop`).
7. `sec:pdf-dis` $x$ 空间的 DIS 定理（扭度 2 部分）.
8. `sec:pdf-sumrules` 求和规则、方案与正定性.
9. `sec:pdf-ff` 碎裂函数、类时演化与极化分布的定义 (optional `fig:pdf-ff-cut`).

**Canonical statements** (in reading order).

* **定义 `def:pdf-quark` — 夸克分布** (no tag) · v1
  - **陈述.** CONTEXT verbatim: $f_{q/H}(\xi;\mu)=\int\frac{dw^-}{4\pi}e^{-i\xi P^+w^-}\langle P|\bar\psi(w)\gamma^+W[w,0]\psi(0)|P\rangle_c$, $w=(0^+,w^-,\mathbf 0_T)$; connected; summed over the operator's colour index, averaged over target colour and spin; $\overline{\rm MS}$ renormalized; renormalization convention $f_{\rm ren}=Z\otimes f_{\rm bare}$ (VF-PDF-4).
  - `\uses{def:prelim-wilson, def:prelim-lightfront, def:prelim-msbar}`

* **定义 `def:pdf-antiquark` — 反夸克分布** (no tag) · v1
  - **陈述.** $f_{\bar q}(\xi)=-f_q(-\xi)$; equivalent to the definition with $\psi^c=C\bar\psi^{\mathsf T}$ and $W^*$ (c_pdf §2.2; VF-PDF-1); $q(x)=f_q(x)$, $\bar q(x)=-f_q(-x)$ for $x>0$.
  - `\uses{def:pdf-quark}`

* **定义 `def:pdf-gluon` — 胶子分布** (no tag) · v1 (+ refdoc S23.5)
  - **陈述.** VF-PDF-2: $f_{g/H}(\xi)=\sum_j\int\frac{dw^-}{2\pi\xi P^+}e^{-i\xi P^+w^-}\langle P|G^{+j}_a(w)W^{(A)}_{ab}[w,0]G^{+j}_b(0)|P\rangle_c$ ($D-2$ transverse $j$); $f_g(-\xi)=-f_g(\xi)$; partonic gluon targets averaged over $D-2=2(1-\varepsilon)$ polarizations — part of the $\overline{\rm MS}$ convention (averaging over 2 shifts $C_2^g\to C_2^g+P_{qg}$, $\Delta_{qg}\to\Delta_{qg}+P_{qg}$; VF-CONV-6). Remark (refdoc S23.5): the gluon density arises from the combination $k^+A^j-k^jA^+$ (the G term of the Grammer–Yennie decomposition that is leading for a gluon as the active parton; pointers `prop:ir-super-leading`, `prop:method-gy-suppression`); the pitfalls of light-cone gauge correspond to the choice of Wilson-line direction (`rem:pdf-gauge-residual`).
  - `\uses{def:prelim-wilson, def:pdf-quark}`

* **命题 `prop:pdf-invariance` — 规范不变性、推动不变性与自由场值** [R, R_def] · v1
  - **陈述.** Gauge invariance (`prop:prelim-wilson-covariance`); dependence on $\xi$ only (boosts along $z$); $f^{(0)}_{q/q}=\delta(1-\xi)$, $f^{(0)}_{q/\bar q}=-\delta(1+\xi)$, $f^{(0)}_{g/g}=\delta(1-\xi)-\delta(1+\xi)$; $\langle k|T^{++}_g|k\rangle=2(k^+)^2$ fixes the gluon normalization (momentum sum rule).
  - **非微扰地位.** 强子态：\cref{asm:intro-wightman}、\cref{asm:intro-composite}（MA0）。
  - **证明.** Full (c_pdf s1, 21/21).
  - `\uses{def:pdf-quark, def:pdf-antiquark, def:pdf-gluon, prop:prelim-wilson-covariance, lem:prelim-boost, asm:intro-wightman, asm:intro-composite}`

* **例 `ex:pdf-free-field` — 自由场值** (no tag) · v1
  - The free-field values of `prop:pdf-invariance` computed with plane waves (c_pdf §2), including the sign of the antiquark and the gluon normalization.
  - `\uses{prop:pdf-invariance}`

* **定理 `thm:pdf-support-pt` — 支撑（微扰论）** [R, R_PT] · v1
  - **陈述.** In PT, graph by graph, $f_{q/j}(\xi)=0$ for $|\xi|>1$ (and $f_g$ likewise) for partonic targets; support survives $\overline{\rm MS}$ renormalization since $Z(\xi/\zeta)$ vanishes for $\xi>\zeta$.
  - **证明.** Sketch — light-front-ordered PT (Collins 2011 §6.9.3, p. 191) or the $\alpha$-representation of cut graphs (`Diehl:1998sm`); `Jaffe1983` (twist-4 multiparton support). (本定理只涉及部分子态。)
  - `\uses{def:pdf-quark, def:pdf-gluon, def:ir-landau-setup}`

* **命题 `prop:pdf-support-hadron` — 支撑（强子态）** [A] · v1 (+ refdoc S23.3)
  - **陈述.** For hadron states, (a) inserting complete states between $\bar\psi(w)W$ and $W\psi(0)$ (light-like separation: ordinary product = time-ordered product, Jaffe) gives $p_X^+=(1-\xi)P^+\ge0\Rightarrow\xi\le1$; (b) the antiquark part, from the anticommutator at light-like separation with the divergent disconnected constant removed, gives $\xi\ge-1$.
  - **非微扰地位.** \cref{asm:intro-wightman}、\cref{asm:intro-composite}（MA0）。
  - **地位与缺口.** Survey item 7: the spectral argument is non-perturbative, but it treats the renormalized light-ray operator as an operator between which complete sets of states can be inserted — the interchange of the state sum with renormalization is the step that keeps the tag at [A]; the point $\xi=0$ is delicate (twist-3 $\delta(x)$ terms; mention without citation). A second argument: `rem:pdf-support-jaffe`.
  - `\uses{def:pdf-quark, def:pdf-antiquark, thm:pdf-support-pt, asm:intro-wightman, asm:intro-composite}`

* **注 `rem:pdf-support-jaffe` — 支撑的第二种论证：$k^-$ 极点** (no tag) · refdoc S23.3
  - Jaffe's argument: in the cut-graph representation, for $\xi>1$ (or $\xi<-1$) all $k^-$ poles of the parton–target amplitude lie on one side of the real axis, so the $k^-$ integral vanishes (`Jaffe1983`); in PT this is equivalent to `thm:pdf-support-pt`.
  - `\uses{thm:pdf-support-pt}`

* **注 `rem:pdf-number-density` — 数密度诠释（启发式）** (no tag) · v1
  - Bare, UV-cutoff densities in $A^+=0$ gauge: $f=\|a|P\rangle\|^2\ge0$ (Collins 2011 §6.7, §6.9.1); caveats: UV divergence of the $k_T$ integral (renormalization destroys the interpretation), spurious $1/k^+$ singularities, zero modes, transverse links at light-cone infinity (`JiYuan2002`, `BelitskyJiYuan2003`). Not a statement about $\overline{\rm MS}$ PDFs (C3; M2, M11).

* **注 `rem:pdf-gauge-residual` — 光锥规范的剩余规范自由与 $1/k^+$ 处方** (no tag) · refdoc S23.4
  - The residual gauge freedom of $A^+=0$ and the prescription of $1/k^+$ act as boundary conditions at $w^-=\pm\infty$; the finite light-like segment of the collinear PDF is prescription independent (composition and retracing), TMD staples are not (pointer Ch14); $U(+\infty)$ is a field-dependent operator, not a global gauge transformation (the conclusion of the usual argument holds via $W[w,\infty]W[\infty,0]=W[w,0]$).

* **定义 `def:pdf-lightray` — 光线算符** (no tag) · v1
  - **陈述.** $O(w^-)=\bar\psi(w)\gamma^+W[w,0]\psi(0)$; $M(w^-)=\langle P|O(w^-)|P\rangle=2P^+\int d\xi\,e^{i\xi P^+w^-}f(\xi)$ (Ioffe-time representation; pointer to the space-like analogue in Ch22).
  - `\uses{def:pdf-quark}`

* **引理 `lem:pdf-wilson-moments` — Wilson 线顶点的矩 = 定域算符顶点** [R, R_def] · v1
  - **陈述.** The $n$-th moment of the $m$-gluon vertex of $O(w^-)$ equals the $m$-gluon vertex of $\bar\psi\gamma^+(iD^+)^{n-1}\psi$ (divided differences; one gluon: $\frac{gt^an^\mu\gamma^+}{2(P^+)^n}\sum_{j=0}^{n-2}(k_2^+)^j(k_1^+)^{n-2-j}$, VF-PDF-12).
  - **证明.** Full for $m=1,2$ (c_pdf s4(b): $n\le7$), induction for general $m$ (App L, `lem:appL-divided-differences`).
  - `\uses{def:pdf-lightray, prop:prelim-wilson-rules, lem:appL-divided-differences}`

* **定理 `thm:pdf-moments-local` — PDF 的矩 = 扭度 2 定域算符矩阵元** [R, R_PT] · v1
  - **陈述.** For $\overline{\rm MS}$-renormalized quantities, $\int_{-1}^1d\xi\,\xi^{n-1}f_q(\xi;\mu)=\frac{\langle P|[\bar\psi\gamma^+(iD^+)^{n-1}\psi]_\mu|P\rangle}{2(P^+)^n}=A^{(n)}_q(\mu)=\int_0^1x^{n-1}[q+(-1)^n\bar q]$ ($n\ge1$), $\int_0^1x^{n-1}g=\frac{\langle P|O_g^{(n)}|P\rangle}{2(P^+)^n}$ ($n$ even) (VF-PDF-11).
  - **非微扰地位.** 对强子态：\cref{asm:intro-wightman}、\cref{asm:intro-composite}(C3)（MA0）。
  - **证明.** Full in App L — (1) bare identity (moments as derivatives at $w^-=0$, $\partial_{w^-}[\bar\psi W]=[\bar\psi\overleftarrow D^+]W$, total derivatives vanish in forward matrix elements; `prop:appL-bare`); (2) renormalization: $Z_f(N)=Z_O(N)$ by uniqueness of minimal subtraction, local operators by `thm:prelim-composite-renorm`; (3) all-order convolution structure: $Z_{ij}(x)$ from partonic targets; finiteness for any state because pole parts are compactly supported distributions with all moments zero (Fourier–Laplace transform entire; gluon via the even distribution $\xi f_g$) (`prop:appL-renormalized`). One-loop check exact in $\varepsilon$ (VF-PDF-13). Remark: left- and right-acting derivatives agree only in forward matrix elements (GPDs, Ch19).
  - `\uses{lem:pdf-wilson-moments, thm:prelim-composite-renorm, def:dis-twist, prop:appL-bare, prop:appL-renormalized, asm:intro-wightman, asm:intro-composite}`

* **定理 `thm:pdf-dglap` — 由算符重整化得到 DGLAP 方程** [R, R_PT] · v1
  - **陈述.** $\frac{\partial f_i(x;\mu)}{\partial\ln\mu^2}=\sum_j(\mathcal P_{ij}\otimes f_j)(x)$, $\mathcal P_{ij}=\frac{\alpha_s}{2\pi}P_{ij}+O(\alpha_s^2)$ (CONTEXT normalization; $P_{ij}$ always the LO kernel), with $\mathcal P=-\alpha_s\partial Z^{(1)}/\partial\alpha_s$ for $Z=\mathbb 1+\sum_kZ^{(k)}/\varepsilon^k$ (one loop: $Z^{(1)}=-\frac{\alpha_s}{2\pi}P$, VF-PDF-4) (using $\mu^2d\alpha_s/d\mu^2=-\varepsilon\alpha_s+\beta(\alpha_s)$; higher poles cancel by consistency conditions).
  - **非微扰地位.** 强子态：\cref{asm:intro-composite}（MA0；部分子态无需）。
  - **证明.** Full. Logical order (C2): this precedes and is independent of any factorization theorem.
  - `\uses{def:pdf-quark, def:pdf-gluon, thm:pdf-moments-local, prop:qcd-rge, prop:prelim-beta, asm:intro-composite}`

* **命题 `prop:pdf-lo-kernels` — 领头阶分裂函数** [R, R_PT] · v1
  - **陈述.** VF-PDF-7: $P_{qq}=C_F[\frac{1+z^2}{1-z}]_+$, $P_{qg}=T_F[z^2+(1-z)^2]$, $P_{gq}=C_F\frac{1+(1-z)^2}z$, $P_{gg}=2C_A[\frac z{(1-z)_+}+\frac{1-z}z+z(1-z)]+\frac{\beta_0}2\delta(1-z)$; $D$-dimensional kernels (VF-PDF-6); number and momentum sum rules; singlet matrix with $2n_fP_{qg}$; Mellin moments $\gamma_{ij}(N)$ (VF-PDF-8); $N=2$ matrix and eigenvalues (VF-PDF-9); convention dictionary (VF-PDF-10).
  - **证明.** Full (real-emission kernels from the operator definitions in $A^+=0$, $\delta$-terms from virtual graphs or conservation laws — identical).
  - `\uses{thm:pdf-dglap, def:pdf-quark, def:pdf-gluon}`

* **命题 `prop:pdf-pqq-operator` — Feynman 规范下由算符定义计算 $P_{qq}$** [R, R_PT] · v1
  - **陈述.** (One loop.) With a gluon mass $m$ as IR regulator and DR for UV: real part $f_R=A_\varepsilon[(1-\varepsilon)^2(1-\xi)\xi^{-\varepsilon}+\frac{2\xi^{1-\varepsilon}}{1-\xi}]$, $A_\varepsilon=\frac{\alpha_s}{2\pi}C_Fe^{\varepsilon\gamma_E}\Gamma(\varepsilon)(\frac{\mu^2}{m^2})^\varepsilon$; Wilson-line real + virtual combine into $A_\varepsilon[2\xi^{1-\varepsilon}/(1-\xi)]_+$ (endpoint cancels only in the combination); self-energy $-A_\varepsilon\frac{1-\varepsilon}{2-\varepsilon}\delta(1-\xi)$; quark number exactly conserved in $\varepsilon$; UV poles graph by graph (units $\frac{\alpha_s}{2\pi}\frac{C_F}\varepsilon$): ladder $(1-\xi)$, Wilson $[\frac{2\xi}{1-\xi}]_+$, self-energy $-\frac12\delta$, sum $P_{qq}/C_F$; renormalized $f^{(1)}_{q/q}=\frac{\alpha_s}{2\pi}\{P_{qq}\ln\frac{\mu^2}{m^2}+C_F[-(1-\xi)(2+\ln\xi)-[\frac{2\xi\ln\xi}{1-\xi}]_++\frac14\delta(1-\xi)]\}$ (regulator dependent); light-cone-gauge ladder alone gives the same $D$-dimensional kernel (VF-PDF-3).
  - **证明.** Full (App G `sec:appG-pdf`); `fig:pdf-oneloop`.
  - `\uses{def:pdf-quark, def:prelim-feynman-rules, prop:prelim-wilson-rules, def:prelim-msbar}`

* **例 `ex:pdf-oneloop` — 单圈夸克 PDF（逐图）** (no tag) · v1
  - = `prop:pdf-pqq-operator` in full, graph by graph, with `fig:pdf-oneloop`.
  - `\uses{prop:pdf-pqq-operator}`

* **命题 `prop:pdf-partonic-dr` — 纯维数正规化中的部分子分布** [R, R_PT] · v1
  - **陈述.** For massless on-shell partons, bare PDFs are $\delta_{ij}\delta(1-\xi)$ to all orders (scaleless; $\int d^{2-2\varepsilon}l_T/l_T^2\propto\frac1{\varepsilon_{\rm UV}}-\frac1{\varepsilon_{\rm IR}}=0$); $\overline{\rm MS}$: $f_{i/j}=\delta_{ij}\delta(1-\xi)-\frac{\alpha_s}{2\pi}\frac1\varepsilon P_{ij}(\xi)+O(\alpha_s^2)$, the surviving pole being infrared (VF-PDF-5; C14, M24).
  - **证明.** Full.
  - `\uses{def:pdf-quark, lem:prelim-scaleless, ex:prelim-scaleless, prop:pdf-lo-kernels}`

* **命题 `prop:pdf-local-anomalous` — 定域算符的单圈反常维度（含混合）** [R, R_PT] · v1
  - **陈述.** UV poles of $\langle j|O_i|j\rangle$ give $\Gamma_{qq}=\gamma_{qq}$, $\Gamma_{q_kg}=2\gamma_{qg}$, $\Gamma_{gq}=\gamma_{gq}$, $\Gamma_{gg}=\gamma_{gg}$; per-graph Feynman-gauge and covariant-gauge values (only the sum including $\delta Z_{2,3}$ is gauge independent); $N=2$: $T^{++}$ not renormalized (VF-PDF-14).
  - **证明.** Full for the quark sector (c_pdf §6.3), gluon sector table.
  - `\uses{def:dis-twist, thm:prelim-composite-renorm, prop:pdf-lo-kernels}`

* **例 `ex:pdf-moments-exact` — 精确到 $\varepsilon$ 的单圈矩** (no tag) · v1
  - Ladder ↔ vertex $A_\varepsilon\frac{(1-\varepsilon)^2}{(n-\varepsilon)(n+1-\varepsilon)}$, Wilson ↔ operator-gluon $-2A_\varepsilon\sum_{i=1}^{n-1}\frac1{i+1-\varepsilon}$, self-energy $-A_\varepsilon\frac{1-\varepsilon}{2-\varepsilon}$; $n=1$: 0; $n=2$: $-\frac{4A_\varepsilon}{3-\varepsilon}$ (VF-PDF-13).
  - `\uses{thm:pdf-moments-local, prop:pdf-pqq-operator}`

* **例 `ex:pdf-quark-in-gluon` — 胶子中的夸克** (no tag) · v1
  - One-loop $f_{q/g}$: kernel $\hat P_{qg}=T_F[1-\frac{2z(1-z)}{1-\varepsilon}]$; effect of the polarization average.
  - `\uses{def:pdf-gluon, prop:pdf-lo-kernels}`

* **定理 `thm:pdf-dis-xspace` — DIS 的 $x$ 空间因子化（扭度 2 部分）** [R, R_OPE] · v1
  - **陈述.** Define $F_2^{\rm tw2}$ as the unique distribution (`cor:appK-pdf`) whose even moments are $\sum_iC^{(n)}_{2,i}A^{(n)}_i$. Then $F_2^{\rm tw2}/x=\sum_iC_{2,i}\otimes f_i$ with $C_{2,i}$ the unique distributions with moments $C^{(n)}_{2,i}$; at $O(\alpha_s)$: $\frac{F_2^{\rm tw2}}x=\sum_qe_q^2\{(q+\bar q)+\frac{\alpha_s}{2\pi}[(C_2^q+LP_{qq})\otimes(q+\bar q)+2(C_2^g+LP_{qg})\otimes g]\}$, $L=\ln(Q^2/\mu^2)$, $C_L^q=2C_Fz$, $C_L^g=4T_Fz(1-z)$ (VF-DIS-7). $F_2-F_2^{\rm tw2}$ has moments $O(1/Q^2)$ for each fixed $n$ ($n\ge n_0$ for hadrons, all $n$ under `asm:intro-growth`); its pointwise size is not controlled (`rem:dis-nonuniform`); weakly it tends to zero (`cor:dis-weak-xspace`).
  - **非微扰地位.** \cref{asm:intro-wightman}、\cref{asm:intro-composite}、\cref{asm:intro-np-ope}、\cref{asm:intro-af-coeff}、\cref{asm:intro-growth}（MA0、MA3、MA4）。
  - **证明.** Full (`thm:dis-moments` + `thm:pdf-moments-local` + `lem:prelim-mellin` + App K; constructively $C_{2,i}$ = $\overline{\rm MS}$-subtracted partonic structure functions, `prop:pdf-partonic-dr`).
  - `\uses{thm:dis-moments, thm:pdf-moments-local, lem:prelim-mellin, cor:appK-pdf, prop:pdf-partonic-dr, asm:intro-wightman, asm:intro-composite, asm:intro-np-ope, asm:intro-af-coeff, asm:intro-growth}`

* **命题 `prop:pdf-sum-rules` — 求和规则** [R, R_PT] · v1
  - **陈述.** $\int_0^1(q-\bar q)=N_q$ ($\gamma_{qq}(1)=0$; conserved current); $\sum_i\int_0^1xf_i(x;\mu)=1$ exactly in $\overline{\rm MS}$ (finiteness of $T^{++}$, eigenvalue 0).
  - **非微扰地位.** 对强子：\cref{asm:intro-wightman}、\cref{asm:intro-composite}（MA0）；对强子结构函数的动量求和规则另需 \cref{asm:intro-growth}（`prop:dis-low-moments`）。
  - **证明.** Full.
  - `\uses{thm:pdf-moments-local, prop:pdf-lo-kernels, thm:pdf-dglap, asm:intro-wightman, asm:intro-composite}`

* **注 `rem:pdf-ns-plusminus` — 解析延拓与 $P^\pm_{\rm NS}$** (no tag) · v1 (+ VF-REF-5)
  - C-even (even $N$) and C-odd (odd $N$) continuations are different functions; unique under polynomial bounds (`prop:appK-continuation`); $P^+_{\rm NS}-P^-_{\rm NS}$ starts at NLO (colour factor $C_F(C_F-\frac{C_A}2)$, `CurciFurmanskiPetronzio1980`); $\int_0^1P^{V(1)}_{q\bar q}=0.71931\,C_F(C_F-\frac{C_A}2)\ne0$ (VF-REF-5). Never write 「DGLAP 与 OPE 重整化群在所有阶以单一核等价」 (S58). (M6.)

* **注 `rem:pdf-schemes` — 方案变换** (no tag) · v1
  - $f'=Z\otimes f$, $C'=C\otimes Z^{-1}$; DIS scheme (VF-DIS-11); the gluon-average convention is part of the scheme.

* **猜想 `conj:pdf-positivity` — $\overline{\rm MS}$ PDF 的正定性** [C] · v1 (+ frontier)
  - **陈述.** For $\mu$ above some scale $\mu_0$, $\overline{\rm MS}$ quark and gluon PDFs of hadrons are non-negative.
  - **地位与缺口.** Evidence for: `CandidoForteHekhorn2020` (NLO positive in the perturbative regime), `Candido:2023ujx` (positivity inherited above $Q^2\gtrsim5$ GeV², a conservative semi-quantitative estimate). Against a general theorem: `CollinsRogersSato2022` (bare PDFs need not be positive in DR; negative at low scales in a model). **The stronger statement "$\overline{\rm MS}$ PDFs are non-negative at every scale" is false**: explicit one-loop counterexample in a Yukawa model, negative at low $\mu$ and positive at large $\mu$ (`CollinsRogersSato2022` eqs. (55)–(56); exact negative region at $\mu=0.8$ GeV for the parameter set of VF-FRO-10: $\xi>0.264$ up to $\xi=1$); $\overline{\rm MS}$ heavy-quark PDFs are negative just below their matching threshold. Circularity warning (C13): LO evolution preserving positivity does not prove positivity of the initial condition. The debate (CFH vs CRS, CFGH 2024) is reported without a verdict [PENDING-VERIFY: E35]; Ch24 gives the details (pointer). The conjecture is therefore only about $\mu\ge\mu_0$, with $\mu_0$ non-perturbative.
  - `\uses{def:pdf-quark, def:pdf-gluon}`

* **定义 `def:pdf-ff` — 碎裂函数** (no tag) · v1 (refdoc S9 applied)
  - **陈述.** VF-CONV-17: in the hadron frame $\mathbf p_{h,T}=0$, $w=(0^+,w^-,\mathbf 0_T)$, $d_{h/q}(z)=\frac{z^{1-2\varepsilon}}{4N_c}\sum_X\int\frac{dw^-}{2\pi}e^{ik^+w^-}{\rm Tr}_c{\rm Tr}_D[\gamma^+\langle0|W[\infty n_B,w]\psi(w)|hX\rangle\langle hX|\bar\psi(0)W[0,\infty n_B]|0\rangle]$, future-pointing lines; parton frame: $\frac1{4N_cz}$ with an explicit $\int d^{2-2\varepsilon}\mathbf p_{h,T}$ ($d^{2-2\varepsilon}p_{hT}=z^{2-2\varepsilon}d^{2-2\varepsilon}k_T$). Free quark $d_{q/q}=\delta(1-z)$. **Print the $O(\alpha_s)$ check** that the free-quark check cannot provide: $A^+=0$ gauge, $h=q$, $X=g$: $d^{(1)}_{q/q}=\frac{\alpha_s}{2\pi}C_F\frac{1+z^2}{1-z}\int\frac{dl_T^2}{l_T^2}$ ($z<1$); the prefactor $\frac1{4N_cz}$ in the hadron frame would give $z^{-2}$ times this. The Collins 2011 location (ch. 12) is to be verified (S63-9).
  - `\uses{def:prelim-wilson, def:prelim-lightfront}`

* **注 `rem:pdf-ff-multren` — 碎裂函数的乘法可重整性是独立输入** (no tag) · refdoc S23.2 (T20)
  - The moments of FFs are not matrix elements of local operators (the state sum $\sum_X|hX\rangle\langle hX|$ sits between the fields), so the moment argument of `thm:pdf-moments-local` does not apply; the multiplicative renormalizability of FFs (in moment space) is an independent input, `asm:appN-multren`(Z1); hence timelike DGLAP is [R, R_PT] at the orders computed but [A] as an all-order operator statement (`prop:pdf-timelike-dglap`). The FF momentum sum rule is formal (see also `Collins:2023cuo`; content to be checked before attributing details).
  - `\uses{def:pdf-ff, thm:pdf-moments-local}`

* **命题 `prop:pdf-timelike-dglap` — 类时 DGLAP 演化** [A] · v1→rev. (tag weakened from [R, R_PT], refdoc S23.2) (composite)
  - **陈述.** (a) $\frac{\partial d_{h/i}}{\partial\ln\mu^2}=\sum_jP^T_{ji}\otimes d_{h/j}$ (transposed index structure) to all orders, given the multiplicative renormalizability of FFs (`asm:appN-multren`(Z1)); $P^{T}$ differs from $P$ beyond LO (`CurciFurmanskiPetronzio1980`); momentum sum rule formal. (b)（单圈内容，\tagR，$R_{\rm PT}$）The UV poles of the one-loop partonic FFs give $P^{T(0)}=P^{(0)}$ (Gribov–Lipatov relation).
  - **非微扰地位.** 强子态：\cref{asm:intro-wightman}、\cref{asm:intro-composite}（MA0）。
  - **证明.** Sketch for (a); full for (b).
  - **地位与缺口.** The all-order statement rests on `asm:appN-multren`(Z1) ([A]-level; refdoc S23.2); (M23: timelike = spacelike kernels only at LO).
  - `\uses{def:pdf-ff, rem:pdf-ff-multren, prop:pdf-lo-kernels, asm:appN-multren, asm:intro-wightman, asm:intro-composite}`

* **定义 `def:pdf-polarized` — 螺旋度与横度分布** (no tag) · v1
  - **陈述.** $\Delta q$ with $\gamma^+\gamma_5$, transversity $h_1$ with $i\sigma^{j+}\gamma_5$ (or $\gamma^+\gamma^j\gamma_5$), $\Delta g$; spin vectors; $\gamma_5$ scheme (`def:prelim-gamma5`). Processes and evolution: Ch11.
  - `\uses{def:pdf-quark, def:prelim-gamma5}`

**Worked examples.** `ex:pdf-free-field`, `ex:pdf-oneloop`, `ex:pdf-moments-exact`, `ex:pdf-quark-in-gluon`.

**Figures.** Existing (tikz1): `fig:pdf-operator` (caption: $n$ is our $n_B$ — say so), `fig:pdf-oneloop`, `fig:dglap-ladder` (caption enriched: strongly ordered ladders, simplex volume $L^n/n!$, refdoc T13), `fig:splitting-vertices`; optional new: `fig:pdf-gluon-operator`, `fig:pdf-ff-cut`.

**Misconception box.** M2, M6, M11, M23, M24, "PDFs are defined by DIS" (C1); critic C1, C2, C3, C13, C14; O6, O8, O9.

**Key citation keys.** `CollinsSoper1982a`, `Soper:1976jc`, `Soper:1979fq`, `Jaffe1983`, `Diehl:1998sm`, `Collins2011`, `Collins2003`, `CurciFurmanskiPetronzio1980`, `FurmanskiPetronzio1980`, `AltarelliParisi1977`, `GribovLipatov1972a`, `GribovLipatov1972b`, `Dokshitzer1977`, `Lipatov:1974qm`, `CataniSeymour1997`, `GrossWilczek1974`, `GeorgiPolitzer1974`, `Joglekar:1975nu`, `Collins:1994ee`, `MochVermaserenVogt2004`, `VogtMochVermaseren2004`, `CandidoForteHekhorn2020`, `CollinsRogersSato2022`, `Candido:2023ujx`, `Collins:2023cuo`, `AltarelliForteRidolfi1998`, `DiemozEtAl1988`, `Larin:1993tq`, `MertigVanNeerven1996`, `Vogelsang1996`, `RalstonSoper1979`, `JaffeJi1991`, `JaffeJi1992`, `JiYuan2002`, `BelitskyJiYuan2003`, `Hausdorff1923`, `Carlson1914`, `Titchmarsh1939`.

**Pending.** `conj:pdf-positivity` debate wording [PENDING-VERIFY: E35]; `def:pdf-ff` Collins location [S63-9]; pointer to the BRST moment reduction (Ch24) [N04].

---------------------------------------------------------------------------------------------------

# 第三部分 共线因子化 (Part III — Collinear factorization)

---------------------------------------------------------------------------------------------------

## Chapter 9 — 全阶因子化证明的一般方法 / The general method of all-order factorization proofs

`\label{ch:method}` · `ch09_method.tex` · **20 pp** · full (precise forms and proofs in App N, App O; App E, F for power counting and Ward identities) · Part III

**Purpose.** One reusable proof machine, stated as a template theorem with explicit hypotheses (H1)–(H5), so that Ch10–Ch14 only verify hypotheses and Ch18 can name the hypothesis that fails — **now with the precise conditional forms behind each step** (refdoc S24–S32): regions as per-line mode assignments with meets; $\lambda$-dependent neighbourhoods and power suppression in integral norm (E-N); idempotent approximators with their $i0$; the error table; why the naive termwise induction fails and the Collins conditions (CS1)–(CS3) on grouped expressions; the precise subtraction theorem (deduction [R, R_cond] in App N, content [A] = `asm:appN-collins`); combinatorics (chains, pairing, product formula); a complete one-loop example; unitarity (cut-position identity, closed-time-path form); the Glauber region with the corrected two-component deformation along $e_G$; the template theorem and the table linking (H1)–(H5) to the numbered assumptions. Critic C7: the order "approximate → Ward identity → Wilson line" is respected; C8: inclusivity in the spectator final state is a theorem per observable; O10: the subtraction formalism is [A], not BPHZ-level.

**Depends on.** Ch2 (`thm:prelim-slavnov-taylor`), Ch3 (`prop:prelim-wilson-rules`, `prop:prelim-wilson-covariance`, `lem:prelim-eikonal-identity`, `def:prelim-lightfront`, `lem:prelim-boost`, `thm:prelim-cutting-rules`), Ch4 (`thm:ir-landau-momentum`, `prop:ir-power-counting`, `prop:ir-super-leading`, `thm:ir-leading-regions`, `def:ir-glauber`, `prop:ir-glauber-trapping`, `def:ir-pinch-surface`, `def:ir-scalings`), Ch5 (prototype; `ex:sudakov-offshell`), Ch8 (operator definitions that the subtraction terms must reproduce; `prop:pdf-partonic-dr`, `thm:pdf-dglap`); App E, F, N, O [SYNC-APP].

**Box.**
- 证明了：`lem:method-ward-elementary`、`lem:method-ward-abelian`、`prop:method-ward-one`、`prop:method-ward-tree`、`lem:method-i0-compat`、`prop:method-glauber-oneloop`、`ex:method-naive-induction`（[R, R_PT]）；`lem:method-soft-unitarity`（[R, R_def]）；`prop:method-scale-scheme`（[R, R_PT]）；数学引理 `lem:method-meets`、`lem:method-covering`、`lem:method-telescoping`、`lem:method-gy`、`prop:method-chains`、`lem:method-pairing`、`prop:method-product`、`lem:method-no-pole`；条件定理 `lem:method-local-accuracy`（前提 `asm:appN-envelope`、`asm:appN-separation`）、`cor:method-removing-eps`（前提 `asm:appN-contour`）、`thm:appN-subtraction`（附录 N）。
- 给出全阶论证：`lem:method-collinear-accuracy`、`lem:method-soft-accuracy`、`prop:method-gy-suppression`、`lem:method-ward-multi`（瓶颈 `asm:appN-ward-product`）、`prop:method-collinear-wilson`、`prop:method-soft-wilson`、`thm:method-subtraction`（瓶颈 `asm:appN-collins`）、`prop:method-fsi`（`asm:appN-cutsum`、`asm:appO-lcopt`）、`prop:method-glauber-deformation`（`asm:appO-deformation`）、`thm:method-template`（[A]）。
- 没有证明：积分范数意义下的全阶幂次计数（`asm:appN-envelope`、`asm:appN-separation`）；含鬼场的非阿贝尔多胶子 Ward 恒等式与非定域算符的 BRST 分类；Glauber 区的一般情形（`asm:appO-*`）；单个链项的可积性（一般不成立，`ex:method-naive-induction`）。

**Sections.**
1. `sec:method-strategy` 证明策略 — the six steps; `fig:method-flowchart` (updated for v2: side annotations to (H1)–(H5) and the `asm:` labels).
2. `sec:method-regions` 区域、邻域与幂次压低 — regions as per-line mode assignments, meets (`fig:method-hasse`: nine two-loop regions; `fig:method-nesting`); power suppression in integral norm; $\lambda$-dependent neighbourhoods and covering (`fig:method-neighbourhoods`); idempotent approximators; the $i0$ compatibility; accuracy lemmas; `tab:method-errors`; local accuracy; failure of (Abs).
3. `sec:method-gy` Grammer–Yennie 分解 — original (QED) form; collinear (Collins 2011 eqs. (11.4)–(11.6), corrected in the errata); soft; power suppression; the gluon-PDF exception (`fig:method-kg`).
4. `sec:method-ward` Ward 恒等式与 Wilson 线 — elementary, abelian, non-abelian one gluon, tree-level two-gluon with ghosts, multi-gluon (outline), collinear and soft Wilson lines (`fig:ward-identity`; `fig:soft-eikonal` owned by Ch3); the pure-gauge heuristic.
5. `sec:method-subtraction` 减除形式体系 — definition; why naive induction fails; the Collins conditions; chains, pairing, product formula; removing $\varepsilon$; the theorem; the complete one-loop example (`fig:method-sudakov-plane`); one-loop DIS in subtraction language (`fig:method-coeff-minus-coll`).
6. `sec:method-unitarity` 幺正性：末态相互作用与软因子.
7. `sec:method-glauber` Glauber 区与围道变形 (`fig:glauber-contour`, `fig:method-glauber-direction`).
8. `sec:method-template` 模板定理；因子化标度与方案 — `tab:method-hypotheses`; closing `tab:method-correspondence`.

**Canonical statements** (in reading order).

* **定义 `def:method-regions` — 区域：逐线模式指派与偏序** (no tag) · v1→rev. (refdoc S24)
  - **陈述.** For a (cut) graph $\Gamma$ and a fixed momentum routing, a region $R$ is a **per-line mode assignment** $R(j)\in\{H,A,B,S\}$ (with the partial order $S<A$, $S<B$, $A,B<H$ and $A\wedge B=S$) that corresponds to a leading pinch surface $\pi_R$ with decomposition $(H_R,\{J_{i,R}\},S_R)$; pinch sets $\pi_R$ are affine subspaces of loop-momentum space; $R'\le R$ iff $R'(j)\le R(j)$ for every line; the meet $R\wedge R'$ is taken line by line. One-loop vertex: $\pi_S\subset\pi_A$, $\pi_S\subset\pi_B$. The leading regions are those of `thm:ir-leading-regions`; the set $\mathcal R$ of regions used is chosen meet-closed (meet closure is a definition, (GA2) of App N, not an assumption).
  - `\uses{def:ir-pinch-surface, def:ir-scalings, thm:ir-leading-regions}`

* **引理 `lem:method-meets` — 逐线交与钳夹集的交** (数学，无标签) · refdoc S24
  - **陈述.** $\pi_{R\wedge R'}=\pi_R\cap\pi_{R'}$; if $\pi_R\cap\pi_{R'}=\emptyset$ there is no common lower bound.
  - **证明.** Full (App N §N.1 [SYNC-APP]).
  - `\uses{def:method-regions}`

* **定义 `def:method-power-suppressed` — 积分范数意义下的幂次压低** (no tag) · refdoc S24
  - **陈述.** For a measurable set $A$ of loop momenta, $F\in\mathfrak S(A)$ iff $\int_A|F|\,d\mu\le C\lambda^aL^K$ for some $a>0$, $K$, uniformly in $\lambda\in(0,\lambda_0]$, $\varepsilon\in(0,\varepsilon_0]$ ($L=\ln(1/\lambda)$; error type E-N of `def:intro-error-types`). Reasons for the integral norm: thin layers of measurement functions; $\overline{\rm MS}$ cancellations that are not pointwise. $\Gamma$ is a single integrand with UV subdivergences removed at integrand level.
  - `\uses{def:intro-error-types}`

* **定义 `def:method-neighbourhoods` — 依赖于 $\lambda$ 的邻域** (no tag) · refdoc S24
  - **陈述.** $N_R=\{\sigma_{R(j)}(l_j)\le\lambda^{\beta_R}\ \forall j:R(j)\ne H\}$ with $\sigma_A=|l^-|+|l_T|$, $\sigma_B=|l^+|+|l_T|$, $\sigma_S=\|l\|$ (in units of $Q$); $U_R=N_R\setminus\bigcup_{R'<R}N_{R'}$; exponents $\beta_R=3^{h(R)-h_*}$ ($h$ = height in the poset). `fig:method-neighbourhoods`.
  - `\uses{def:method-regions}`

* **引理 `lem:method-covering` — 邻域覆盖** (数学，无标签) · refdoc S24
  - **陈述.** $\bigcup_{R\in\mathcal R}U_R=\Omega$ (the integration domain), with $U_H$ the complement of all smaller neighbourhoods.
  - **证明.** Full (App N §N.1).
  - `\uses{def:method-neighbourhoods}`

* **定义 `def:method-collinear-approx` — 共线近似子（幂等投影形式）** (no tag) · v1→rev. (refdoc S26)
  - **陈述.** At the interface of an $A$-collinear subgraph with $H$: momentum projection $k\to\pi_+(k)=(n_B\cdot k)n_A=(k^+,0,\mathbf 0_T)$ in $H$; Dirac projection $\mathcal P_+=\frac12\gamma^-\gamma^+$ (out-flowing quarks: $\mathcal P_-$), i.e. $H(k)\Phi(k)\to H(\hat k)\frac14\gamma^-{\rm Tr}[\gamma^+\Phi(k)]$ (check $\Phi=\slashed p\to p^+\gamma^-$); gluon projector $\mathcal P_A{}^\mu{}_\nu=g_T{}^\mu{}_\nu+n_A^\mu n_{B\nu}$, so that $H_\mu J^\mu\to H^-J^+-\mathbf H_T\cdot\mathbf J_T$; the projectors are idempotent; **no new denominators** are introduced: the Wilson-line denominators $\frac1{n_B\cdot k\mp i0}$ appear only after the Ward identity, with $-i0$ for attachments to final-state lines (DIS; future-pointing line) and $+i0$ for initial-state lines (DY; past-pointing line, after the one-sided rewriting of App O) (c_wilson §6.2, s6; VF-WL-10). Spin/colour projections: ${\rm Tr}_c[HJ]\simeq\frac1{N_c}{\rm Tr}_cH\,{\rm Tr}_cJ$ for colour-singlet targets.
  - `\uses{def:method-regions, def:prelim-lightfront, lem:prelim-boost}`

* **定义 `def:method-soft-approx` — 软近似子（幂等投影形式）** (no tag) · v1→rev. (refdoc S26)
  - **陈述.** Soft momentum $k$ entering $J_A$: $k\to\pi_-(k)=(n_A\cdot k)n_B$ inside $J_A$ (keeps $k^-$), projection $n_A^\mu n_{B\nu}$ on the soft gluon; the soft-approximated $J_A$ denominators $\tilde D=p^2-M^2+2p^+k^-+i0$ inherit their $i0$; after the Ward identity the soft gluons attach to a Wilson line along $n_A$ with $\frac1{n_A\cdot k\pm i0}$ ($+i0$ incoming $A$ line, $-i0$ outgoing) (VF-WL-11). The explicit $i0$ forms of v1 are consequences.
  - `\uses{def:method-regions, def:prelim-lightfront}`

* **引理 `lem:method-i0-compat` — 软近似分母的 $i0$ 相容性与变形幅度** [R, R_PT] · refdoc S26 [PENDING-VERIFY: X2]
  - **陈述.** If a soft momentum flows through $J_A$ lines $l=p+k$ whose $p^+$ all have the same sign $\eta$, then under $k^-\to k^-+i\eta\kappa$: ${\rm Im}D=2\eta\kappa(p^++k^+)\ge0$ and ${\rm Im}\tilde D=2\eta\kappa p^+\ge0$, so neither the exact nor the soft-approximated denominators are crossed. The soft line's own propagator limits the amplitude to $\kappa\sim k_T^2/|k^+|$, which gives only $|k^+k^-|\gtrsim k_T^2$ (not $|k^-|\sim|k_T|$). Opposite orientations give a Glauber pinch.
  - **证明.** Full (App N §N.4). (本引理只涉及 Feynman 积分。)
  - `\uses{def:method-soft-approx, def:ir-glauber}`

* **引理 `lem:method-telescoping` — 乘积的伸缩恒等式** (数学，无标签) · refdoc S26
  - **陈述.** $(1-T)\prod_{i=1}^nf_i=\sum_i[\prod_{j<i}Tf_j](f_i-Tf_i)[\prod_{j>i}f_j]$ for an approximator $T$ acting factor by factor.
  - **证明.** Full (one line).
  - `% uses: none`

* **引理 `lem:method-collinear-accuracy` — 共线近似的精度** [A] · v1 (+ refdoc S31)
  - **陈述.** Near $\pi_R$, away from smaller regions, $T_R\Gamma=\Gamma[1+O(\lambda)]$.
  - **证明.** Sketch (expand $H$ in $k^-,k_T$; bad components and non-K polarizations suppressed by the boost factors of `prop:ir-power-counting`). Numerical nuance (c_wilson §6.2): G-term $O(\lambda^2)$ for an on-shell massless parent, $O(\lambda)$ generically. Literature: Collins 2011 ch. 10 (Sudakov), §11.3.
  - **地位与缺口.** A scaling statement (E-S); its integral form is `lem:method-local-accuracy` (under `asm:appN-envelope`, `asm:appN-separation`).
  - `\uses{def:method-collinear-approx, prop:ir-power-counting}`

* **引理 `lem:method-soft-accuracy` — 软近似的精度** [A] · v1 (+ refdoc S31)
  - **陈述.** Same for the soft approximator, valid only where $|k^+k^-|\gtrsim k_T^2$ (outside the Glauber region): on the contour of `lem:method-i0-compat`, and in the Glauber core only on the App O contour (`prop:appO-eikonal`, pointer).
  - **证明.** Sketch; remainder formula VF-WL-11 ($O(\lambda|k_T|/|k^-|)$; $O(1)$ in the Glauber region).
  - **地位与缺口.** E-S; integral form under `asm:appN-envelope`, `asm:appN-separation`; quantitative bounds on the deformed contour in App O.
  - `\uses{def:method-soft-approx, lem:method-i0-compat, prop:ir-power-counting}`

* **引理 `lem:method-local-accuracy` — 局部精度（积分范数）** [R, R_cond] · refdoc S26 [PENDING-VERIFY: X2]
  - **陈述.** 前提：\cref{asm:appN-envelope}、\cref{asm:appN-separation}。For every region $R_0$: $(1-T_{R_0})\Gamma\in\mathfrak S(U_{R_0})$; hence (CS1) holds for minimal $R_0$ (`def:method-collins-conditions`, later in this chapter: the statement is self-contained). Remark (print): term-by-term stability of chain terms is false (the two counterexamples of `ex:method-naive-induction`).
  - **证明.** Full in App N §N.4 (the rows of `tab:method-errors`; `lem:method-telescoping`).
  - `\uses{def:method-power-suppressed, def:method-neighbourhoods, lem:method-telescoping, def:method-collinear-approx, def:method-soft-approx, asm:appN-envelope, asm:appN-separation}`

* **注 `rem:method-abs-failure` — 吸收性质 (Abs) 何时失效** (no tag) · refdoc S26
  - The absorption property (Abs) $T_RT_{R'}=T_RT_{R\wedge R'}T_{R'}$ of approximators fails exactly by the transverse coupling of a direction-flipping line (leading for a physical gluon connection), plus an edge case of the soft-line convention; hence the general product formula (`prop:method-product`) is part of `asm:appN-collins`, not a theorem.

* **引理 `lem:method-gy` — Grammer–Yennie 分解** (数学，无标签) · v1 (+ refdoc ERR-m3 wording)
  - **陈述.** Collinear: $g_{\mu\nu}=K_{\mu\nu}+G_{\mu\nu}$, $K_{\mu\nu}=\frac{k_\mu w_{2\nu}}{k\cdot w_2-i0}$, $w_2=n_B$; $G_{\mu\nu}k^\nu=0$; $H\cdot G\cdot C=H\cdot(C-\frac{C^+}{k^+}k)$; soft: $K_s^{\mu\nu}=\frac{k^\mu n_A^\nu}{n_A\cdot k\pm i0}$. The original QED form is the symmetric $b_kk_\mu k_\nu$ (`GrammerYennie1973`, as reproduced in `SenIndumathiChoudhury2019` eqs. (7)–(9)); the one-sided form with its $i0$ is Collins' adaptation (Collins 2011 eqs. (11.4)–(11.6) with the errata [PENDING-VERIFY: E27]) (VF-WL-10/11).
  - **证明.** Full.
  - `\uses{def:method-collinear-approx, def:method-soft-approx}`

* **命题 `prop:method-gy-suppression` — G 部分的幂次压低** [A] · v1
  - **陈述.** Each collinear G-gluon beyond the minimal parton content costs $\ge\lambda$; K-gluons cost nothing; exception: a single transversely polarized gluon as the active parton ($k\cdot H=0$, G term leading, combines into $G^{+j}$ via $k^+A^j-k^jA^+$; `prop:ir-super-leading`); soft G-gluons $O(\lambda)$ outside the Glauber region.
  - **证明.** Sketch + numerics (c_wilson s5).
  - **地位与缺口.** E-S statements; integral form under `asm:appN-envelope`.
  - `\uses{lem:method-gy, prop:ir-power-counting, prop:ir-super-leading}`

* **引理 `lem:method-ward-elementary` — 基本 Ward 恒等式** [R, R_PT] · v1
  - **陈述.** VF-WL-6: (W1) $S(p+k)(ig\slashed kt^a)S(p)=gt^a[S(p+k)-S(p)]$; (W2) on-shell ends; (W3) $q_{1\mu}V^{\mu\nu\rho}_{abc}=gf^{abc}[(q_3^2g^{\nu\rho}-q_3^\nu q_3^\rho)-(q_2^2g^{\nu\rho}-q_2^\nu q_2^\rho)]$; (W4) ghost vertex not a pure difference; (W5) eikonal Ward identity $\frac{n\cdot k}{(n\cdot\ell+i0)(n\cdot(\ell+k)+i0)}=\frac1{n\cdot\ell+i0}-\frac1{n\cdot(\ell+k)+i0}$.
  - **证明.** Full.
  - `\uses{def:prelim-feynman-rules, prop:prelim-wilson-rules}`

* **引理 `lem:method-ward-abelian` — 阿贝尔 Ward 恒等式** [R, R_PT] · v1
  - **陈述.** On a fermion line with on-shell ends, the sum over all insertions of a scalar-polarized gluon gives $g\sum_r[\text{line with gluon }r\text{ carrying }q_r+k\text{ and colour }[T_K,T_r]]$, hence 0 in the abelian case (VF-WL-6, c_wilson §5.2). With one end at the hard vertex, $\sum_{\rm insertions}\prod_ik_{i\mu_i}H^{\mu_1\cdots\mu_m}=(\pm g)^mH_0$ (shifted kinematics); the eikonal factors appear only after the K projectors, giving the abelian Wilson line via the eikonal identity.
  - **证明.** Full.
  - `\uses{lem:method-ward-elementary, lem:prelim-eikonal-identity}`

* **命题 `prop:method-ward-one` — 单个纵向胶子的非阿贝尔 Ward 恒等式** [R, R_PT] · v1
  - **陈述.** $k_\mu\mathcal M^\mu_a=0$ at every order when all other external partons are on shell and physically polarized.
  - **证明.** Full from `thm:prelim-slavnov-taylor` (App F `sec:appF-one`).
  - `\uses{thm:prelim-slavnov-taylor}`

* **命题 `prop:method-ward-tree` — 树图层次的非阿贝尔恒等式与 PDF Wilson 线的种子** [R, R_PT] · v1
  - **陈述.** (c_wilson §5.3–5.5, VF-WL-7/8/9.) (a) $\gamma^*\to q\bar qg$: $k_\mu\mathcal A^{\mu\nu}=0$ on shell; with the antiquark leg off shell the hard part gives $-gt^aH_0$; (b) DIS: $k_\mu H^\mu_a=gt^aH_0$, and with the K projector $H_\mu\frac{k^\mu n_B^\alpha}{n_B\cdot k-i0}=W^{(1)}[\infty n_B,0]H_0$; two collinear K-gluons give exactly $(n_B\cdot k_1)(n_B\cdot k_2)W^{(2)}_{ab}[\infty n_B,0]H_0$ (path ordering from the commutator term; no ghost or three-gluon graph at this order); (c) $q\bar q\to g^*g^*$: $k_{1\mu}\mathcal A^{\mu\nu}_{ab}=\frac{g^2f^{abc}}{Q^2}(k_2^2g^{\nu\sigma}-k_2^\nu k_2^\sigma)J_{c\sigma}$; ghost term for unphysical polarizations.
  - **证明.** Full (App F, `prop:appF-two-gluon`).
  - `\uses{lem:method-ward-elementary, prop:method-ward-one, prop:appF-two-gluon}`

* **例 `ex:method-ward-tree` — $q\bar q\to g^*g^*$ 的两个纵向胶子** (no tag) · v1
  - Ghost term; physical-polarization sum $=-g$ sums minus ghosts; cross-check with the $q\bar q\to gg$ cross section (VF-WL-9; `ex:qcd-qqbar-gg`).
  - `\uses{prop:method-ward-tree, ex:qcd-qqbar-gg}`

* **引理 `lem:method-ward-multi` — 多个 K 胶子的 Ward 恒等式与 Wilson 线** [A] · v1
  - **陈述.** For $n$ K-gluons attached in all ways to $H$ whose other external lines are on-shell physical partons, the sum equals $H_0$ times the Feynman rules of a Wilson line along $n_B$ (future/past according to final/initial-state attachments); ghost contributions cancel or are absorbed into Wilson-line operators. Conditions stated (c_wilson §8.5).
  - **证明.** Sketch — App F gives $n=1$ (`prop:method-ward-one`) and $n=2$ (tree, `prop:method-ward-tree`) in full and the inductive step in outline (`prop:appF-induction`).
  - **地位与缺口.** Collins 2011 §11.9 (p. 416, Fig. 11.6) and §11.3.2 (pp. 407–410: the BRST classification for non-local operators is **assumed**: "no proof has been given… I will assume the result is true"; survey item 6); `CollinsSoper1982a`; `Labastida:1984gy`; `Collins:2008sg` (non-zero leading remainder of the naive K-gluon identity, needed for the gluon PDF); amplitude-level alternative `FeigeSchwartz2014`; moment reduction of the bilocal classification problem: Ch24 (pointer) [PENDING-VERIFY: N04]. Status: abelian [R]; $n\le2$ at tree level [R]; general non-abelian combinatorics with ghosts [A]; the precise form needed in App N is `asm:appN-ward-product`.
  - `\uses{prop:method-ward-one, prop:method-ward-tree, prop:appF-induction}`

* **命题 `prop:method-collinear-wilson` — 共线 Wilson 线与 PDF** [A] · v1
  - **陈述.** Summing the collinear approximation over all attachments of $A$-collinear K-gluons gives $H_0(\hat k)\otimes\Phi^W(k)$; integrating over $k^-,k_T$ at fixed $k^+=\xi P^+$ yields the bare PDF of `def:pdf-quark`/`def:pdf-gluon` with the straight light-like segment, since $W[w,\infty n_B]W[\infty n_B,0]=W[w,0]=W[w,-\infty n_B]W[-\infty n_B,0]$ for $w_T=0$ (composition and retracing, `prop:prelim-wilson-covariance`; restated for DY as `prop:dy-universality`, pointer).
  - **证明.** Sketch.
  - **地位与缺口.** Inherits `lem:method-ward-multi` (`asm:appN-ward-product`).
  - `\uses{lem:method-ward-multi, def:method-collinear-approx, prop:prelim-wilson-covariance, def:pdf-quark, def:pdf-gluon}`

* **命题 `prop:method-soft-wilson` — 软 Wilson 线** [A] · v1
  - **陈述.** Soft gluons attached to $J_A$, after `def:method-soft-approx` and the Ward identity, decouple from $J_A$ and attach to a Wilson line along $n_A$ in $S=\langle0|\prod_iW_{n_i}|0\rangle$ (time orderings as appropriate).
  - **证明.** Sketch.
  - **地位与缺口.** Inherits `lem:method-ward-multi` and `lem:method-soft-accuracy` (valid outside the Glauber region).
  - `\uses{lem:method-ward-multi, def:method-soft-approx, lem:method-soft-accuracy}`

* **注 `rem:method-pure-gauge` — 纯规范论证的地位** (no tag) · refdoc S31 (T8)
  - The pure-gauge argument ($F[\mathcal A_{\rm eff}]=0\Rightarrow\mathcal A_{\rm eff}=-\frac ig(\partial U)U^\dagger$, $\psi\to U^\dagger\psi$) is a structural heuristic; its step 2 is the BRST content of `lem:method-ward-multi` [A]; it cannot fix the Wilson-line direction — the $i0$ of `def:method-collinear-approx` does; $U(+\infty)$ is a field-dependent operator, not a global gauge transformation. Never write 「纯规范论证证明了非阿贝尔 Wilson 线结构」 (S58). Cross-reference: collinear gauge invariance in SCET (Ch15).

* **定义 `def:method-subtraction` — 减除项** (no tag) · v1
  - **陈述.** $C_R\Gamma\equiv T_R(\Gamma-\sum_{R'<R}C_{R'}\Gamma)$, starting from minimal regions; $T_R$ = product of the approximators with integrations extended to the full ranges; $X_{R_0}\equiv\Gamma-\sum_{R<R_0}C_R\Gamma$.
  - `\uses{def:method-regions, def:method-collinear-approx, def:method-soft-approx}`

* **例 `ex:method-naive-induction` — 朴素归纳为何失败：离壳单圈三角图** [R, R_PT] · refdoc S25 [PENDING-VERIFY: X2] (misconception M35)
  - **陈述.** (One loop.) For the off-shell scalar triangle with $p_1=(P,-\frac{m^2}{2P},\mathbf 0_T)$, $p_2=(\frac{m^2}{2P'},-P',\mathbf 0_T)$ and regions $\{S,C_1,C_2,H\}$: (a) $T_{C_2}\Gamma=\frac1{D_gh_1D_2}$ has an unregulated collinear pinch in $C_1$, while $C_{C_2}\Gamma=T_{C_2}(\Gamma-T_S\Gamma)=\frac{m^2}{2PP'}\frac1{D_gD_2e_2}-\frac1{h_1D_2e_2}$ is suppressed there; (b) $C_S\Gamma$ is leading in $C_1$, so $T_{C_1}$ must be accurate on $T_S\Gamma$: $(1-T_{C_1})T_S\Gamma=\frac1{D_ge_1}(\frac1{e_2}-\frac1{h_2})$; (c) $T_{C_1}\Gamma$ is not absolutely integrable for any $\varepsilon$ (the rapidity end needs $\varepsilon<0$, the UV end $\varepsilon>0$). Hence statements about single chain terms are false in general; only grouped expressions $C_R\Gamma$ are suppressed (denominators as in App N §N.7; VF-REF-18).
  - **证明.** Full (closed forms; App N §N.7).
  - `\uses{def:method-subtraction, def:method-power-suppressed}`

* **定义 `def:method-collins-conditions` — 减除条件 (CS1)–(CS3)** (no tag) · refdoc S25
  - **陈述.** With $X_{R_0}=\Gamma-\sum_{R<R_0}C_R\Gamma$: (CS1)$_{R_0}$ $(1-T_{R_0})X_{R_0}\in\mathfrak S(U_{R_0})$ (accuracy); (CS2)$_{R_0}$ $C_R\Gamma\in\mathfrak S(U_{R_0})$ for all $R\not\le R_0$ (suppression of non-smaller regions); (CS3) $\Gamma$ and all $C_R\Gamma$ are in $L^1(\Omega)$, uniformly in $\varepsilon$ for $\Gamma$ (integrability). Names chosen to avoid clashes with (H1)–(H5), [A] and MA (refdoc S8).
  - `\uses{def:method-subtraction, def:method-power-suppressed, def:method-neighbourhoods}`

* **命题 `prop:method-chains` — 减除的链展开** (数学，无标签) · v1→rev. (refdoc S29)
  - **陈述.** $C_R\Gamma=\sum_{\text{chains }R_1<\dots<R_k<R}(-1)^kT_RT_{R_k}\cdots T_{R_1}\Gamma$; $X_{R_0}=\mathcal O_{\downarrow R_0}\Gamma$ and the remainder $r\equiv\Gamma-\sum_RC_R\Gamma=\mathcal O_{\mathcal R}\Gamma$, where $\mathcal O_{\mathcal P}\equiv\sum_{\text{chains }c\subset\mathcal P}(-1)^{|c|}T_c$ ($T_c$ with the largest element leftmost); for a totally ordered $\mathcal P$: $\mathcal O_{\mathcal P}=(1-T_{P_n})\cdots(1-T_{P_1})$. **Corrected forest analogy:** chains correspond only to nested families; incomparable regions never appear in one chain, even when their pinch sets intersect; they interact only through meets; as in BPHZ, rigorous estimates exist only for grouped expressions, never for single chain terms. IR forest formula for wide-angle amplitudes: `Ma2020` (pointer).
  - **证明.** Full (induction; App N §N.3).
  - `\uses{def:method-subtraction}`

* **引理 `lem:method-pairing` — 配对分解** (数学，无标签) · refdoc S29
  - **陈述.** Let $\mathcal R$ be meet-closed; fix $R_0$; let $\mathcal I'$ ($\mathcal I''$) be the regions incomparable with $R_0$ whose pinch sets meet (do not meet) $\pi_{R_0}$; $R_\wedge=R\wedge R_0$. Pointwise: $r=\mathcal O_{\uparrow R_0}[(1-T_{R_0})X_{R_0}]-\sum_{R\in\mathcal I'}\mathcal O_{\uparrow R}T_R[(1-T_{R_\wedge})X_{R_\wedge}]-\sum_{R\in\mathcal I''}\mathcal O_{\uparrow R}T_R\Gamma$. Remark (print): expanding the alternating sums $\mathcal O_{\uparrow R}$ regenerates non-integrable terms (`ex:disall-ladder`, Ch10, pointer); the decomposition says which combinations must be estimated, it does not reduce the problem to single approximation errors.
  - **证明.** Full (App N §N.3).
  - `\uses{prop:method-chains, lem:method-meets}`

* **命题 `prop:method-product` — 乘积公式** (数学，无标签) · refdoc S29
  - **陈述.** Hypotheses: all pairwise pinch sets intersect; $\mathcal R$ meet-closed; each $T_R$ idempotent; (Com) $T_RT_{R'}=T_{R'}T_R$; (Abs) $T_RT_{R'}=T_RT_{R\wedge R'}T_{R'}$ for incomparable $R,R'$. Conclusion: $C_R\Gamma=T_R\prod_{R'<R}(1-T_{R'})\Gamma$, $X_{R_0}=\prod_{R<R_0}(1-T_R)\Gamma$, $r=\prod_R(1-T_R)\Gamma$; equivalences: (CS1)$_{R_0}$ ⟺ $\prod_{R\le R_0}(1-T_R)\Gamma\in\mathfrak S(U_{R_0})$; (CS2)$_{R_0}$ ⟺ $T_R\prod_{R'\in\downarrow R\cup\{R_0\}}(1-T_{R'})\Gamma\in\mathfrak S(U_{R_0})$ for $R\not\le R_0$. Remark: (Com)(Abs) hold exactly for momentum substitutions with adapted routing (scalar triangle); (Abs) can fail for polarization projections (`rem:method-abs-failure`).
  - **证明.** Möbius function of the meet-semilattice (meet-irreducible elements); App N §N.3.
  - `\uses{prop:method-chains, lem:method-meets, lem:method-pairing, def:method-collins-conditions}`

* **引理 `lem:method-no-pole` — 有界的亚纯函数无极点** (数学，无标签) · refdoc S29
  - **陈述.** A function meromorphic near $\varepsilon=0$ and bounded on $(0,\varepsilon_0]$ has no pole at $0$.
  - **证明.** Full (one line).
  - `% uses: none`

* **推论 `cor:method-removing-eps` — 去掉维数正规化** [R, R_cond] · refdoc S29 [PENDING-VERIFY: X2]
  - **陈述.** 前提：\cref{asm:appN-contour}(b)（及 \cref{thm:appN-subtraction} 的前提）。If $\int\Gamma$ is analytic near $\varepsilon=0$ and the hypotheses of `thm:appN-subtraction` hold, then $F(\varepsilon)=\sum_R\int C_R\Gamma$ has no pole at $\varepsilon=0$ and $|\int\Gamma-F|_{\varepsilon=0}\le C\lambda^aL^K$. Meaning: the UV poles of single subtraction terms cancel in the sum (as in (b) of `prop:appN-triangle-exact`).
  - **证明.** Full (`lem:method-no-pole` applied to $F$; App N §N.3).
  - `\uses{thm:appN-subtraction, lem:method-no-pole, asm:appN-contour}`

* **定理 `thm:method-subtraction` — 减除定理** [A] · v1→rev. (refdoc S29; fixes OUR-2)
  - **陈述.** For every leading-power integrand $\Gamma$ of the process (a single graph, or a family of graphs with a common routing), $\Gamma=\sum_{R\in\mathcal R}C_R\Gamma+r$ with $r\in\mathfrak S(\Omega)$; hence $\int\Gamma=\sum_R\int C_R\Gamma+O(\lambda^aL^K)$, and each $\int C_R\Gamma$ converges absolutely.
  - **证明.** `proofsketch`, new plan (replacing v1 steps (1)–(5); "key compatibility property" and "induction" are deleted): (1) the deduction is `thm:appN-subtraction` [R, R_cond] (premises (CS1)–(CS3) for the given $\Gamma$ and `asm:appN-contour`(a)); (2) (CS1) for minimal regions from `lem:method-local-accuracy`; (3) under (Com)(Abs) the remaining (CS1)(CS2) reduce to grouped power counting (`prop:method-product`); (4) the grouped estimates for all integrands are `asm:appN-collins`; (5) removing $\varepsilon$ (`cor:method-removing-eps`) and the UV structure (`asm:appN-uv`).
  - **地位与缺口.** "The deduction is [R, R_cond]; the [A] is that of `asm:appN-collins`." Collins 2011 ch. 10 (§10.3, §10.8) treats the Sudakov form factor completely at the level of rigour of that chapter (integral-norm vs scaling: S63-12); general processes [A]; CSS 1989 §10.1: "there is as yet in the literature no complete and systematic subtraction procedure in QCD… even in the case of deeply inelastic scattering" (survey item 6); no Minkowskian analogue of Weinberg's theorem (critic O10). Never write 「减除定理可以逐项归纳证明」 (M35). Error type: E-N is what is claimed; what exists in the literature is E-S.
  - `\uses{def:method-subtraction, def:method-collins-conditions, def:method-power-suppressed, thm:appN-subtraction, lem:method-local-accuracy, prop:method-product, cor:method-removing-eps, asm:appN-collins, asm:appN-uv, asm:appN-contour}`

* **例 `ex:method-sudakov-subtraction` — 完整的单圈例子：离壳三角图的 Collins 减除** (no tag) · v1→enlarged (refdoc S30) [PENDING-VERIFY: X2, N12]
  - In light-cone variables (the kinematics of `ex:method-naive-induction`): $k^-$ residues; the four regions $S,C_1,C_2,H$ with $\beta_S=\frac19$, $\beta_C=\frac13$; the pointwise closed forms of the $C_R\Gamma$; which grouped expression supplies the small factor on each $U_R$; why the soft approximation holds only on a contour that crosses the real axis near the gluon pole, ${\rm Re}\,k^-\sim k_T^2/(4k^+)$, and fails at $k^-\approx0$ (the simplest instance of "the approximation holds only on the deformed contour"); the values, the pole cancellation ($1-2+1$), the sum $\tilde Q^{-2}[\ln^2(\tilde Q^2/m^2)+\frac{\pi^2}3]$ and the exact remainder $-4m^2/Q^4+O(m^4Q^{-6}L^2)$ (no logarithm at NLP; `prop:appN-triangle-exact`, VF-REF-3); the zero-bin as $\frac1{\varepsilon_{\rm UV}}-\frac1{\varepsilon_{\rm IR}}$ and its representation dependence (`rem:ir-regions-values`); `fig:method-sudakov-plane`. Last part (kept from v1): the on-shell DR version, where all pairwise overlaps are scaleless (c_regions §3.3) so no explicit zero-bin terms survive; with cutoffs they are needed (`ex:ir-regions-toy`). Status sentence (print): identities, values and remainder are exact; the uniform integral bounds of `thm:appN-subtraction` on a deformed four-dimensional contour have not been written even here — the example illustrates `asm:appN-collins`, it does not verify it in integral form.
  - `\uses{thm:method-subtraction, ex:method-naive-induction, prop:appN-triangle-exact, ex:sudakov-offshell, rem:ir-regions-values}`

* **例 `ex:method-dis-oneloop` — 减除语言中的单圈 DIS** (no tag) · v1 (+ refdoc T18)
  - One-loop DIS on a quark: $C_A\Gamma^{(1)}=f^{(1)}_{q/q}\otimes{\rm Born}=-\frac{\alpha_s}{2\pi}\frac1\varepsilon P_{qq}$ (pure DR), $C_H\Gamma^{(1)}=\frac{\alpha_s}{2\pi}C_2^q$: the coefficient function *is* the subtracted graph (VF-DIS-6); "coefficient function = cut graph minus its collinear approximation" — ISR² ↔ ladder, ISR–FSR interference ↔ Wilson-line graphs (`fig:method-coeff-minus-coll`).
  - `\uses{def:method-subtraction, prop:pdf-partonic-dr, prop:pdf-pqq-operator}`

* **引理 `lem:method-soft-unitarity` — 软因子的幺正性** [R, R_def] · v1 (+ refdoc E25)
  - **陈述.** For an observable that does not constrain soft momenta, the soft factor summed over cuts with all Wilson lines at the same point is $\langle0|(W_{n_A}W_{n_B})^\dagger(0)(W_{n_A}W_{n_B})(0)|0\rangle=1$; in DR every graph beyond tree level is scaleless. For past-pointing lines the time-ordered product is the interaction-picture evolution operator $T[\mathcal U^{(-)}]=U_I(0,-\infty)$, unitary (role of $v^0>0$; for *time-like non-light-like* past lines path order is anti-time order — c_tmd caveat).
  - **证明.** Full. Contrast: TMD soft factor $\tilde S(b_T)\ne1$ (Ch14). Logical order (critic O13): used only after the Glauber region has been dealt with.
  - `\uses{def:prelim-wilson, prop:prelim-wilson-covariance}`

* **命题 `prop:method-fsi` — 末态相互作用的幺正性相消** [A] · v1→rev. (refdoc S31) [PENDING-VERIFY: X1]
  - **陈述.** Final-state interactions not constrained by the observable cancel in the sum over cuts: either the final-state jet is not pinched in the forward amplitude (DIS: part of $H$ in the unphysical region, forward pointer `prop:disall-two-routes`), or the interactions cancel by unitarity (DY spectators).
  - **证明.** New plan: the light-cone cut-position identity with insertions (`lem:appO-cut-position`, 数学) and its closed-time-path form (`lem:appO-unitarity` [R, R_cond: `asm:appO-lcopt`]), in which final-state interactions internal to one jet vanish exactly; the precise setting is `asm:appN-cutsum` (a cut-summed representation with common domain and integrand); single cut graphs and gluon masses do not provide it. Literature: `LibbySterman1978a`, `CollinsSoperSterman1988`, Collins 2011 §14.4, `AybatSterman2009`.
  - **地位与缺口.** [A] = `asm:appN-cutsum`, `asm:appO-lcopt`; "a single cut graph is unitary" is false (Ch3 misconception).
  - `\uses{lem:method-soft-unitarity, thm:prelim-cutting-rules, lem:appO-cut-position, lem:appO-unitarity, asm:appN-cutsum, asm:appO-lcopt}`

* **命题 `prop:method-glauber-oneloop` — 两条程函线之间的单胶子交换** [R, R_PT] · v1
  - **陈述.** With $n_A\cdot k=k^-$, $n_B\cdot k=k^+$: for past–past lines the $k^-$ integral of $\frac{1}{(k^-+i0)(-k^++i0)(2k^+k^--k_T^2+i0)}$ vanishes for $k^+>0$ and equals $-2\pi i/(k_T^2k^+)$ for $k^+<0$; the difference of past and future $A$ lines is $\frac1{k^-+i0}-\frac1{k^--i0}=-2\pi i\delta(k^-)$ — the Glauber (Coulomb) phase, $\propto\int d^2k_T/k_T^2$ (VF-WL-12; c_wilson s6).
  - **证明.** Full.
  - `\uses{prop:prelim-wilson-rules, def:ir-glauber}`

* **例 `ex:method-glauber-oneloop` — 单胶子交换的极点图** (no tag) · v1
  - = `prop:method-glauber-oneloop` with the pole figure (`fig:glauber-contour`).
  - `\uses{prop:method-glauber-oneloop}`

* **命题 `prop:method-glauber-deformation` — Glauber 区的围道变形判据** [A] · v1→rev. (refdoc S32; fixes OUR-4) [PENDING-VERIFY: X1]
  - **陈述.** (a) If all $k^-$ poles of the $J_A$ lines carrying the soft momentum $k$ lie in one half-plane, $k^-$ can be deformed; the soft line's own pole limits the amplitude to $\kappa\sim k_T^2/|k^+|$ (`lem:method-i0-compat`). (b) In the Glauber region ($k^\pm\sim\lambda^2$, $k_T\sim\lambda$), deforming one component, even to $\sim|k_T|$, leaves $|k^+k^-|\sim\lambda^3\ll k_T^2$: the momentum stays in $G_\delta=\{|k^+k^-|\le\delta k_T^2\}$ and the soft approximation becomes valid only for the other jet. (c) Leaving $G_\delta$ requires a **simultaneous** deformation of $k^+$ and $k^-$ along $e_G=n_B-n_A$, with coherent signs and amplitude $\sim|k_T|$; it only makes denominators more time-like, $(l+it\sigma fe_G)^2-m^2=(l^2-m^2+2t^2f^2)+2it\sigma f(l^+-l^-)$ (VF-REF-7; WRITER_SPEC_v2 §3 row 38); it is possible after the attachments to one jet have been rewritten by equal-light-cone-time localization; for colour-singlet inclusive DY this is carried out in App O (`prop:appO-target`, `thm:appO-main` [R, R_cond]); in general it is part of (H3). The obstruction (poles on both sides — the Glauber pinch, as for spectator–spectator interactions; pole half-plane rule VF-GLA-4) and the unitarity pre-step (`prop:method-fsi`) are kept.
  - **证明.** Sketch (blueprint S7; `prop:ir-glauber-trapping`; `fig:glauber-contour`, whose caption must be supplemented at the first reference by 「离开 Glauber 区须沿 $e_G$ 同时形变两个分量（\cref{fig:method-glauber-direction}）」, M31).
  - **地位与缺口.** [A]; precise form under `asm:appO-deformation`, `asm:appO-mixing`, `asm:appO-envelope`, `asm:appO-rewritten-cs` (App O); Collins 2011 §14.4.8 "Issues remaining".
  - `\uses{lem:method-i0-compat, prop:ir-glauber-trapping, prop:method-fsi, def:ir-glauber, prop:appO-target, thm:appO-main, asm:appO-deformation, asm:appO-mixing, asm:appO-envelope, asm:appO-rewritten-cs}`

* **注 `rem:method-two-component` — 一个分量的形变为何不够** (no tag) · refdoc S32 (misconception M31)
  - The geometry of (b)–(c) of `prop:method-glauber-deformation` with `fig:method-glauber-direction` (three panels: one-component deformation stays in $G_\delta$; the soft line's own pole; the simultaneous deformation along $e_G$); amplitude-side ($\sigma=+1$) soft momentum flowing into $J_A$ is deformed with ${\rm Im}\,k^->0$, ${\rm Im}\,k^+<0$. Never write 「把 $k^-$ 围道推到 $|k^-|\sim|k_T|$ 就离开了 Glauber 区」 (M31).

* **定理 `thm:method-template` — 因子化模板定理** [A] · v1 (+ refdoc S5, S31)
  - **陈述.** For an observable with collinear directions $n_A,n_B,\dots$ assume: **(H1)** its leading regions are those of `thm:ir-leading-regions` (plus Glauber regions), with the integral-norm power counting of `asm:appN-envelope`, `asm:appN-separation`; **(H2)** at the $H$–$J$ interfaces the collinear approximation holds and K-gluons decouple into Wilson lines (`lem:method-ward-multi`, `prop:method-collinear-wilson`; precise form `asm:appN-ward-product`); **(H3)** after contour deformation out of the Glauber region, or explicit cancellation of Glauber contributions, the soft approximation holds and soft gluons decouple (`prop:method-glauber-deformation`, `prop:method-soft-wilson`; for DY-type processes `asm:appO-mixing`, `asm:appO-deformation`, `asm:appO-rewritten-cs`); **(H4)** final-state interactions not constrained by the observable cancel by unitarity and the soft factor is 1 (collinear factorization) or a well-defined vacuum matrix element of Wilson lines (TMD) (`lem:method-soft-unitarity`, `prop:method-fsi`, `asm:appN-cutsum`, `asm:appO-lcopt`); **(H5)** the subtraction terms coincide with the renormalized matrix elements of the operators defining the PDFs/FFs/TMDs (`thm:method-subtraction`, `asm:appN-collins`, `asm:appN-values`, `asm:appN-uv`, `asm:appN-multren`; + `asm:appN-tmd` for TMD). Then $\sigma=\sum_{ij}H_{ij}\otimes f_{i/A}\otimes f_{j/B}[\otimes S]+O(\lambda^p)$, with $H_{ij}$ computable with partonic external states (`prop:pdf-partonic-dr`).
  - **非微扰地位.** \cref{asm:intro-bridge}（MA1、MA2、MA4）。
  - **证明.** `proofsketch` in which the deduction from (H1)–(H5) is written out completely (WRITER_SPEC_v2 §4.10 item 4); its precise conditional form runs through `thm:appN-subtraction` [R, R_cond] (refdoc S5).
  - **地位与缺口.** [A] reflects both `thm:method-subtraction` and the status of the hypotheses; each process chapter verifies (H1)–(H5) with its own status line; the correspondence (H$i$) ↔ `asm:` labels is `tab:method-hypotheses`.
  - `\uses{thm:ir-leading-regions, lem:method-ward-multi, prop:method-collinear-wilson, prop:method-soft-wilson, prop:method-glauber-deformation, lem:method-soft-unitarity, prop:method-fsi, thm:method-subtraction, prop:pdf-partonic-dr, asm:intro-bridge, asm:appN-envelope, asm:appN-separation, asm:appN-ward-product, asm:appN-cutsum, asm:appN-collins, asm:appN-values, asm:appN-uv, asm:appN-multren}`

* **命题 `prop:method-scale-scheme` — 因子化标度与方案** [R, R_PT] · v1 (qualifier R_def → R_PT, because it uses `thm:pdf-dglap`; grade unchanged)
  - **陈述.** $\mu_F$-independence of $\sigma$ + DGLAP (`thm:pdf-dglap`) ⇒ $\partial H/\partial\ln\mu_F^2=-H\otimes P$ (convolution form); scheme change $f'=Z\otimes f$, $H'=H\otimes Z^{-1}$; $\mu_R$ dependence via $\beta$. Equivalently, for the hard coefficients defined as $\overline{\rm MS}$-subtracted partonic cross sections the statement follows from DGLAP for partonic PDFs and the $\mu$-independence of the bare partonic cross section.
  - **证明.** Full. Logical order (C2): DGLAP first, scale independence as corollary. (M25: scale variation is a convention, not a theorem.) (本命题只涉及部分子态的系数函数。)
  - `\uses{def:intro-factorization, thm:pdf-dglap, prop:prelim-beta, rem:pdf-schemes}`

**Worked examples.** `ex:method-ward-tree`, `ex:method-naive-induction`, `ex:method-sudakov-subtraction`, `ex:method-dis-oneloop`, `ex:method-glauber-oneloop`.

**Tables.**
- `tab:method-errors` (full page; refdoc S26): rows 1–9 of the error table of the approximators (collinear momentum projection; Dirac projection; gluon projection; soft momentum projection; soft polarization projection; rapidity-regularized directions; …) in our notation, with columns approximation | deleted | kept | size on $U_R$ | bound type (relative E-P, envelope, E-N) | input used [SYNC-APP: proofs App N §N.4].
- `tab:method-hypotheses` (refdoc S31): hypothesis | precise form (labels) | status | verified per process in — (H1) `thm:ir-leading-regions` (scaling) + `asm:appN-envelope`, `asm:appN-separation`; (H2) `lem:method-ward-multi` + `asm:appN-ward-product`; (H3) revised `prop:method-glauber-deformation`; for DY-type processes `asm:appO-mixing`, `asm:appO-deformation`, `asm:appO-rewritten-cs`; (H4) `lem:method-soft-unitarity`, `prop:method-fsi`, `asm:appN-cutsum`, `asm:appO-lcopt`; (H5) `asm:appN-collins`, `asm:appN-values`, `asm:appN-uv`, `asm:appN-multren` (+ `asm:appN-tmd` for TMD). Last column: Ch10 (`prop:disall-h2`, `prop:disall-h3h4`, `prop:disall-h5`), Ch11 (`thm:coll-sia`), Ch12 (`thm:dy-factorization`), Ch14 (`prop:tmd-h1h5`).
- `tab:method-correspondence` (refdoc S45.2): chapter statement | precise version (App N/O label) | what differs (assumptions, error type) — `thm:method-subtraction` ↔ `thm:appN-subtraction`; `lem:method-collinear-accuracy`, `lem:method-soft-accuracy` ↔ `lem:method-local-accuracy`, App N §N.4; `prop:method-fsi` ↔ `lem:appO-unitarity`; `prop:method-glauber-deformation` ↔ `prop:appO-target`, `thm:appO-main`; `thm:method-template` ↔ `thm:appN-subtraction` + register [SYNC-APP].

**Figures.** Existing (tikz2): `fig:ward-identity`, `fig:glauber-contour` (owned); `fig:soft-eikonal` (owned by Ch3; refer back); `fig:momentum-regions` (Ch4; refer back). New (v1, required): `fig:method-flowchart` (updated for v2), `fig:method-kg` (adapt `research/c_wilson/tex/c_wilson_gy.tex`), `fig:method-nesting`. New (refdoc S56, required): `fig:method-hasse`, `fig:method-neighbourhoods`, `fig:method-sudakov-plane`, `fig:method-coeff-minus-coll`, `fig:method-glauber-direction`.

**Misconception box.** M15 (soft factor always 1), M24 (UV/IR bookkeeping), M25 (scale variation = error), **M31**, **M35**; critic C2, C7 (Ward identities before approximations), C14; O10, O13.

**Key citation keys.** `Collins2011`, `CollinsSoper1982a`, `CollinsSoperSterman1985b`, `CollinsSoperSterman1988`, `CollinsSoperSterman1989`, `Bodwin1985`, `GrammerYennie1973`, `SenIndumathiChoudhury2019`, `Labastida:1984gy`, `Collins:2008sg`, `FeigeSchwartz2014`, `Ma2020`, `ErdoganSterman2015`, `BogoliubovParasiuk1957`, `Hepp1966`, `Zimmermann1969`, `LibbySterman1978a`, `tHooft1971`, `Taylor1971`, `Slavnov1972`, `BecchiRouetStora1976`, `KugoOjima1979`, `Weinberg1965`, `CombridgeKripfganzRanft1977`, `AybatSterman2009`, `Diehl:2015bca`, `Collins2003`, `UsyukinaDavydychev1993a`, `Jantzen2011`.

**Pending.** App N statements and the example [PENDING-VERIFY: X2, N12, S63-12]; App O statements [PENDING-VERIFY: X1]; Collins errata in `lem:method-gy` [E27]; N04 pointer in `lem:method-ward-multi`.

---------------------------------------------------------------------------------------------------

## Chapter 10 — DIS 的全阶动量空间证明、重夸克与核靶 / DIS to all orders in momentum space; heavy quarks; nuclear targets

`\label{ch:disall}` · `ch10_disall.tex` · **13 pp** · full (precise forms in App N) · Part III

**Purpose.** First application of `thm:method-template` (one hadron, no soft factor at leading power, final-state interactions summed by unitarity); **the two routes from the unphysical forward amplitude** to moments (Cauchy estimates on a complex disc) and to $x$ space (cut graphs; non-uniform as $x\to1$) (refdoc S27); the factorized structure of the DIS subtraction terms, their compatibility with $\overline{\rm MS}$ renormalization and the recursion for the coefficients (refdoc S28); the two-rung ladder with its three regions; comparison with the [R, R_OPE] results of Ch7–Ch8 (critic O7/D12: twist-2 parts agree in the sense of distributions; the pointwise $x$-space remainder is the content of the [A] theorem); explicit $O(\alpha_s)$ coefficient functions in $\overline{\rm MS}$; scale independence; DIS scheme; Collins' acknowledged gaps; heavy-quark masses (Collins 1998 theorem; schemes); nuclear targets.

**Depends on.** Ch4, Ch7–Ch9; App N [SYNC-APP].

**Box.**
- 证明了：`prop:disall-nlo`、`prop:disall-scale`、`prop:disall-dis-scheme`（[R, R_PT]）；`cor:disall-consistency`（[R, R_OPE]）；`prop:disall-two-routes`、`prop:disall-factorized-subtraction`、`thm:disall-renorm-compat`（[R, R_cond]；前提 `asm:appN-collins`、`asm:appN-cutsum`、`asm:appN-ward-product`、`asm:appN-uv`、`asm:appN-multren`）。
- 给出全阶论证：`thm:disall-factorization`（[A]；瓶颈 `asm:appN-collins`、`asm:appN-ward-product`、`asm:appN-cutsum`）、`prop:disall-regions`、`lem:disall-fsi`、`prop:disall-h2`、`prop:disall-h3h4`、`prop:disall-h5`、`thm:disall-heavy`、`prop:disall-nuclear`（[A]）。
- 没有证明：$x\to1$ 处的一致性（阈值区）；非定域算符的 BRST 分类（`lem:method-ward-multi`）；积分范数形式的减除估计（`asm:appN-collins`）。

**Sections.**
1. `sec:disall-regions` Breit 系与领头区域；两条途径 (`fig:reduced-dis`, owned by Ch4; `fig:disall-seed`).
2. `sec:disall-fsi` 末态相互作用与幺正性.
3. `sec:disall-subtraction` 减除项的因子化结构、重整化相容性与两级梯形图 (`fig:disall-ladder-regions`) — **new section** (refdoc S28).
4. `sec:disall-theorem` 模板假设的验证与主定理.
5. `sec:disall-consistency` 与 OPE 结果的一致性.
6. `sec:disall-nlo` $O(\alpha_s)$ 系数函数的推导 (`fig:dis-oneloop`, owned by Ch7).
7. `sec:disall-scale` 标度无关性与 DIS 方案.
8. `sec:disall-heavy` 重夸克质量与变味方案 (`fig:disall-heavy`).
9. `sec:disall-nuclear` 核靶.
10. Closing: `tab:disall-correspondence` (chapter statement | App N version | difference).

**Canonical statements** (in reading order).

* **定义 `def:disall-breit` — Breit 系与投影算符** (no tag) · v1
  - **陈述.** $P=(P^+,M^2/2P^+,\mathbf 0_T)$, $q=(-xP^+,Q^2/(2xP^+),\mathbf 0_T)$; $D$-dimensional projectors $\frac{F_L}x=\frac{8x^2}{Q^2}P_\mu P_\nu W^{\mu\nu}$, $\frac{F_2}x=\frac1{1-\varepsilon}[-g_{\mu\nu}+(3-2\varepsilon)\frac{4x^2}{Q^2}P_\mu P_\nu]W^{\mu\nu}$; massive-target version (VF-DIS-2).
  - `\uses{def:dis-kinematics}`

* **命题 `prop:disall-two-routes` — 从非物理区前向振幅到矩与 $x$ 空间的两条途径** [R, R_cond] · refdoc S27 [PENDING-VERIFY: X2] (fixes OUR-6)
  - **陈述.** 前提：\cref{asm:appN-collins}（在复圆盘 $|\omega|\le\rho<1$ 上一致）、\cref{asm:appN-cutsum}（用于 (c)）。(a) For $|\omega|<1$ the leading regions of $T^{\mu\nu}$ contain only target-collinear and hard modes (the current jet is off shell by $O(Q^2)$ in the unphysical region). (b) If the integral-norm subtraction bounds (CS1)–(CS3) of `def:method-collins-conditions` (the content of `asm:appN-collins`) hold uniformly for $\omega$ in the complex disc $|\omega|\le\rho<1$, then every moment of $W^{\mu\nu}$ factorizes with remainder $O(\rho^{-N}\lambda^aL^K)$ (Cauchy estimate). (c) Bounds on a real $\omega$-segment alone do **not** control the discontinuity; the $x$-space statement at fixed $x<1$ requires the cut-graph analysis under `asm:appN-cutsum`; uniformity fails as $x\to1$ (threshold region; pointer Ch13).
  - **证明.** Full for (b) and the counter-remark of (c) (App N §N.5 [SYNC-APP]).
  - `\uses{def:disall-breit, def:dis-compton, def:method-collins-conditions, asm:appN-collins, asm:appN-cutsum}`

* **引理 `lem:disall-fsi` — 末态喷注的非钳夹性** [A] · v1 (+ refdoc S27, S28)
  - **陈述.** Sum over cuts = discontinuity of $T^{\mu\nu}$; lines carrying the large $q^-$ are not pinched in the forward amplitude ($k^-$ contour deformable by $O(Q^2/P^+)$), so the current jet and soft lines attached to it are part of $H$. With $(\xi P+q)^2=Q^2(\xi-x)/x$: as $\xi\to x$ the current jet merges into $H$; this endpoint produces the plus distributions and the threshold region (refdoc T16; pointer Ch13).
  - **证明.** Sketch (`prop:method-fsi`; `prop:disall-two-routes`(a)).
  - **地位与缺口.** [A]: E-S argument; the cut-graph version needed at fixed $x$ rests on `asm:appN-cutsum`.
  - `\uses{prop:method-fsi, def:disall-breit, prop:disall-two-routes}`

* **命题 `prop:disall-regions` — DIS 的领头区域** [A] · v1
  - **陈述.** Leading regions of $T^{\mu\nu}$: target-collinear subgraph + hard subgraph joined by two partons plus any number of $A^+$-polarized gluons; no soft subgraph, no final-state collinear subgraph after the sum over cuts.
  - **证明.** Sketch (`thm:ir-leading-regions`, `lem:disall-fsi`; soft lines into $H$ cost $\lambda^2$). Literature: `LibbySterman1978a`, CSS 1989 §8.7.
  - **地位与缺口.** E-S; integral form `asm:appN-envelope`, `asm:appN-separation`.
  - `\uses{thm:ir-leading-regions, lem:disall-fsi}`

* **命题 `prop:disall-factorized-subtraction` — DIS 减除项的因子化结构** [R, R_cond] · refdoc S28 [PENDING-VERIFY: X2]
  - **陈述.** 前提：\cref{asm:appN-ward-product}、\cref{asm:appN-uv}（及 \cref{prop:disall-regions}）。In DIS, $R'<R$ implies $J_{R'}\supset J_R$, so $T_{R'}$ never alters the internal factors of $J_R$, and with (Com)(Abs) for adapted routing (`prop:method-product`) $\sum_{\rm graphs}C_R\Gamma=\hat{\mathsf H}_R\otimes\mathsf J_R^{\rm bare}$, where $\mathsf J_R^{\rm bare}$ is the bare partonic PDF of `def:pdf-quark`/`def:pdf-gluon` and the colour projection ${\rm Tr}_c[HJ]\simeq\frac1{N_c}{\rm Tr}_cH\,{\rm Tr}_cJ$ is used.
  - **证明.** Full (App N §N.5).
  - `\uses{prop:method-product, def:method-subtraction, prop:disall-regions, def:pdf-quark, def:pdf-gluon, asm:appN-ward-product, asm:appN-uv}`

* **命题 `prop:disall-h2` — (H2) 的验证** [A] · v1 (+ refdoc S28)
  - **陈述.** Collinear approximation + `lem:method-ward-multi` + `prop:method-collinear-wilson` give the PDFs of Ch8 with the straight Wilson line (future-pointing in the amplitude); colour projection ${\rm Tr}_c[HJ]\simeq\frac1{N_c}{\rm Tr}_cH\,{\rm Tr}_cJ$ (colour-singlet target); normalization chain $\int d^4k\to P^+\int d\xi$, $\int\frac{dk^-d^2k_T}{(2\pi)^4}{\rm Tr}[\gamma^+J]=2f$ (refdoc T14).
  - **证明.** Sketch; seed `prop:method-ward-tree`(b) (`fig:disall-seed`).
  - **地位与缺口.** `asm:appN-ward-product` (non-abelian multi-gluon Ward identity with ghosts).
  - `\uses{def:method-collinear-approx, lem:method-ward-multi, prop:method-collinear-wilson, prop:method-ward-tree, prop:disall-regions}`

* **命题 `prop:disall-h3h4` — (H3)(H4) 平凡成立** [A] · v1
  - **陈述.** No soft factor at leading power; no Glauber problem (one hadron, final state summed; the forward amplitude in the unphysical region has no final-state jet).
  - **地位与缺口.** E-S argument (`lem:disall-fsi`, `prop:disall-regions`).
  - `\uses{prop:disall-regions, lem:disall-fsi, lem:method-soft-unitarity}`

* **定理 `thm:disall-renorm-compat` — 减除与 $\overline{\rm MS}$ 重整化的相容性（矩空间）** [R, R_cond] · refdoc S28 [PENDING-VERIFY: X2]
  - **陈述.** 前提：\cref{asm:appN-multren}（及 \cref{prop:disall-factorized-subtraction} 的前提）。(a) $C_i\equiv\sum_k\hat{\mathsf H}_k^{\rm bare}Z_{ki}$ is finite at $\varepsilon=0$; (b) it is target and regulator independent, and equals the DR partonic matching under (Z3); (c) recursion $C^{[n]}=\lim_{\lambda\to0}[T^{[n]}_{(j)}-\sum_{m<n}C^{[m]}f^{{\rm ren}[n-m]}_{\cdot/j}]$.
  - **证明.** Full (meromorphic + bounded ⇒ no pole, `lem:method-no-pole`; App N §N.5).
  - `\uses{prop:disall-factorized-subtraction, lem:method-no-pole, prop:pdf-partonic-dr, def:prelim-msbar, asm:appN-multren}`

* **命题 `prop:disall-h5` — (H5) 的验证** [A] · v1
  - **陈述.** Subtraction terms $=f_{i/j}\otimes C$ with renormalized partonic PDFs; hence $C_{2,i}=\hat F_2^{(j)}\otimes(f^{\rm partonic})^{-1}$, at one loop in pure DR $C=\hat F^{(1)}+\frac1\varepsilon P\otimes\hat F^{(0)}$.
  - **地位与缺口.** `asm:appN-collins`, `asm:appN-multren` (precise form `thm:disall-renorm-compat`).
  - `\uses{thm:disall-renorm-compat, prop:pdf-partonic-dr, thm:method-subtraction}`

* **例 `ex:disall-ladder` — 两级梯形图：三个区域与分组余项** (no tag) · refdoc S28 [PENDING-VERIFY: X2]
  - Two-rung ladder with **three** regions $R_2<R_1<R_H$ (the all-hard region carries the two-loop coefficient — corrects the "two regions" count of literature-style presentations); $r=\Delta\mathsf H_0\Delta K_2\Delta K_1$; $C_2\Gamma$, $C_1\Gamma$, $C_H\Gamma$ explicit; $C_1\to\hat{\mathsf H}^{[1]}$; $C_H\to$ two-loop coefficient with the $\hat{\mathsf H}^{[1]}\otimes f^{[1]}$ and $\mathsf H^{[0]}\otimes f^{[2]}$ subtractions; the single chain term $T_H(1-T_2)\Gamma$ is not $L^1$ on $U_{R_2}$, so the grouping is necessary. `fig:disall-ladder-regions`; details App N §N.7.
  - `\uses{thm:method-subtraction, prop:method-chains, def:method-collins-conditions, thm:disall-renorm-compat}`

* **定理 `thm:disall-factorization` — DIS 共线因子化（动量空间，$x$ 空间逐点）** [A] · v1 (+ refdoc S27, S28)
  - **陈述.** For fixed $0<x<1$ with $W^2\gg\Lambda^2$, as $Q\to\infty$: $$\frac{F_2(x,Q^2)}x=\sum_i\int_x^1\frac{d\xi}\xi C_{2,i}\Big(\frac x\xi,\frac{Q^2}{\mu^2},\alpha_s(\mu)\Big)f_i(\xi;\mu)+R(x,Q),$$ similarly $F_L$, with $R=O(\Lambda^2/Q^2)$ with an $x$-dependent coefficient, non-uniform as $x\to1$ (heuristic parameter $\Lambda^2/(Q^2(1-x))$) and $x\to0$.
  - **非微扰地位.** \cref{asm:intro-bridge}（MA1、MA2、MA4）。
  - **证明.** `proofsketch` in which the deduction from `prop:disall-regions`–`prop:disall-h5` and `thm:method-template` is written out completely (WRITER_SPEC_v2 §4.10). Point to print: bounds on $T^{\mu\nu}$ for real $|\omega|<1$ do not by themselves control its discontinuity; moments follow by Cauchy estimates under uniform complex-disc bounds; the fixed-$x$ statement needs the analysis of the cut graphs, and uniformity fails as $x\to1$ (`prop:disall-two-routes`).
  - **地位与缺口 (print).** Bottlenecks by label: `asm:appN-collins`, `asm:appN-envelope`, `asm:appN-separation`, `asm:appN-cutsum`, `asm:appN-ward-product`, `asm:appN-uv`, `asm:appN-multren`, `asm:intro-bridge`. Collins 2011 §11.3.2 (pp. 407–410) — BRST classification of non-local operators assumed; naive K-gluon identity has a non-zero leading remainder (`Collins:2008sg`); complete proof in a non-gauge theory: Collins 2011 §8.9; CSS 1989 §10.1 quotation; early physical-gauge arguments `EllisEtAl1979`, `Ellis:1978sf`, `AmatiPetronzioVeneziano1978a`, `AmatiPetronzioVeneziano1978b`, `Mueller1978`, `CurciFurmanskiPetronzio1980`; physical gauges obstruct Glauber deformations (Collins 2011 §12.6) — proofs in Feynman gauge.
  - `\uses{thm:method-template, prop:disall-regions, lem:disall-fsi, prop:disall-h2, prop:disall-h3h4, prop:disall-h5, prop:disall-two-routes, def:pdf-quark, def:pdf-gluon, asm:intro-bridge, asm:appN-collins, asm:appN-envelope, asm:appN-separation, asm:appN-cutsum, asm:appN-ward-product, asm:appN-uv, asm:appN-multren}`

* **推论 `cor:disall-consistency` — 与 OPE 系数的一致性** [R, R_OPE] · v1
  - **陈述.** The coefficient functions defined as $\overline{\rm MS}$-subtracted partonic structure functions (the construction of `prop:pdf-partonic-dr`) have moments equal to the OPE coefficients: at $O(\alpha_s)$ by explicit calculation exactly in $\varepsilon$ ($N\le8$; VF-DIS-13); at all orders by uniqueness (`cor:appK-pdf`), since both satisfy the same moment relations (`prop:dis-wilson-partons`). The twist-2 parts of `thm:disall-factorization` and `thm:pdf-dis-xspace` therefore agree as distributions; the pointwise remainder is controlled only by the [A] theorem (critic O7, D12).
  - **证明.** Full.
  - `\uses{thm:pdf-dis-xspace, prop:dis-wilson-partons, cor:appK-pdf, prop:pdf-partonic-dr}`

* **命题 `prop:disall-nlo` — $O(\alpha_s)$ 的 $\overline{\rm MS}$ 系数函数** [R, R_PT] · v1
  - **陈述.** (At one loop; c_dis, VF-DIS-1…12.) With $\frac{F_2}x=\sum_qe_q^2\{(q+\bar q)+\frac{\alpha_s}{2\pi}[C_2^q\otimes(q+\bar q)+2C_2^g\otimes g]\}$, $\frac{F_L}x=\sum_qe_q^2\frac{\alpha_s}{2\pi}[C_L^q\otimes(q+\bar q)+2C_L^g\otimes g]$, at $\mu=Q$: $C_2^q=C_F[2\mathcal D_1-\frac32\mathcal D_0-(1+z)\ln(1-z)-\frac{1+z^2}{1-z}\ln z+3+2z-(\frac92+\frac{\pi^2}3)\delta(1-z)]$, $C_2^g=T_F[(z^2+(1-z)^2)\ln\frac{1-z}z-8z^2+8z-1]$, $C_L^q=2C_Fz$, $C_L^g=4T_Fz(1-z)$; general $\mu$: $+\ln(Q^2/\mu^2)P_{qi}$; the factor 2 counts quark and antiquark; gluon polarization average $1/(D-2)$.
  - **证明.** Full — Born exact in $D$; virtual form factor (`prop:sudakov-oneloop`); real emission exact in $\varepsilon$; plus-distribution expansion; pole structure ($1/\varepsilon^2$: $2-2$; $1/\varepsilon$: $-P_{qq}/C_F$ incl. $\frac32\delta$ from the virtual graph; $\delta$ coefficient $\frac72-3\zeta_2-8+\zeta_2=-(\frac92+\frac{\pi^2}3)$); mass factorization with `prop:pdf-partonic-dr`. Literature cross-checks: `Vermaseren:2005qc`, `Moch:2004xu`, `AltarelliMartinelli1978`, `BardeenEtAl1978`, `FurmanskiPetronzio1982`. (本命题只涉及部分子态。)
  - `\uses{def:disall-breit, prop:sudakov-oneloop, lem:prelim-plus-expansion, prop:pdf-partonic-dr, lem:appC-phase-space, prop:dis-c-oneloop}`

* **例 `ex:disall-nlo` — $O(\alpha_s)$ 系数函数的完整推导** (no tag) · v1
  - The full derivation of `prop:disall-nlo` (main worked calculation of the chapter, ≈3 pp; c_dis `dis_oneloop.tex` is a ready Chinese draft — adapt, relabel `fig:dis1l-diagrams` → `fig:dis-oneloop`).
  - `\uses{prop:disall-nlo}`

* **例 `ex:disall-gluon` — 光子—胶子融合** (no tag) · v1
  - $\hat F_2^g/(ze_q^2)=\frac{\alpha_s}{2\pi}(\frac{\mu^2}{Q^2})^\varepsilon[-\frac2\varepsilon P_{qg}+2C_2^g]$, poles from both collinear configurations; average-over-2 shift (VF-CONV-6).
  - `\uses{prop:disall-nlo}`

* **命题 `prop:disall-scale` — 标度无关性** [R, R_PT] · v1
  - **陈述.** $\partial(F_2/x)/\partial\ln\mu_F^2=O(\alpha_s^2)$; $\partial F_2/\partial\ln\mu_R^2=-\frac{\beta_0}2a^2\sum e_q^2[C_2^q\otimes(q+\bar q)+2C_2^g\otimes g]$, $a=\alpha_s/2\pi$; $F_L$ $\mu$-independent at $O(a)$ (VF-DIS-10).
  - **证明.** Full (Mellin space).
  - `\uses{prop:disall-nlo, thm:pdf-dglap, prop:prelim-beta}`

* **命题 `prop:disall-dis-scheme` — DIS 方案** [R, R_PT] · v1 (qualifier R_def → R_PT: it uses the $\overline{\rm MS}$ coefficient functions of `prop:disall-nlo`; grade unchanged)
  - **陈述.** $q_i^{\rm DIS}=q_i+a[C_2^q\otimes q_i+C_2^g\otimes g]$, $g^{\rm DIS}=g-a[C_2^q\otimes\Sigma+2n_fC_2^g\otimes g]$ (gluon fixed by the momentum sum rule; attribution `DiemozEtAl1988` "(see)"); $C_{2}^{\rm DIS}=\ln(Q^2/\mu^2)P$; $P^{(1),\rm DIS}_{\rm NS}=P^{(1),\overline{\rm MS}}_{\rm NS}-\frac{\beta_0}2C_2^q$; $C_L$ scheme independent at $O(\alpha_s)$ (VF-DIS-11).
  - **证明.** Full.
  - `\uses{prop:disall-nlo, rem:pdf-schemes}`

* **定理 `thm:disall-heavy` — 含重夸克质量的因子化（Collins 1998）** [A] · v1
  - **陈述.** Keeping heavy-quark masses in the hard part, with heavy-quark PDFs in the CWZ/ACOT framework, $F=\sum_if_i\otimes\hat C_i(m_h/Q,Q/\mu)$ with power-suppressed corrections "uniformly suppressed by a power of $\Lambda/Q$, independently of… $M$" (`Collins1998b` abstract, survey item 27).
  - **非微扰地位.** \cref{asm:intro-bridge}（MA1、MA2）。
  - **证明.** Sketch. Schemes FFNS, ZM-VFNS, GM-VFNS (ACOT, S-ACOT, TR, BMSN, FONLL) are equivalent prescriptions to the order computed (`CollinsWilczekZee1978`, `AivazisEtAl1994`, `Aivazis:1993kh`, `Kramer:2000hn`, `Thorne:1997ga`, `Buza:1996wv`, `Forte:2010ta`); decoupling (`rem:qcd-decoupling`).
  - **地位与缺口.** Inherits `thm:disall-factorization`; caveat for hadron–hadron (Collins 2011 §14.6, pp. 569–570: massive incoming partons — "a bad idea").
  - `\uses{thm:disall-factorization, rem:qcd-decoupling, asm:intro-bridge}`

* **例 `ex:disall-heavy-lo` — 领头阶 $\gamma^*g\to Q\bar Q$** (no tag) · v1
  - LO $\gamma^*g\to Q\bar Q$ with full mass dependence and its $m\to0$ limit $\ln(Q^2/m^2)P_{qg}$ = ACOT subtraction (formula derived by the writer; not verified by an agent; `fig:disall-heavy`).
  - `\uses{thm:disall-heavy}`

* **命题 `prop:disall-nuclear` — 核靶上的 DIS** [A] · v1
  - **陈述.** Leading power: as DIS on a hadron (nuclear PDFs); nuclear-enhanced twist-4 terms $\propto A^{1/3}\Lambda^2/Q^2$ [P] (`QiuSterman1991a`, `Luo:1993ui`, `Luo:1994np`); BBL: factorization requires energy ≫ a scale growing with the target length (`Bodwin:1988fs`, abstract); leading-twist shadowing via DDIS factorization (`Frankfurt:2011cs`); saturation regime at small $x$ [C] (Ch17).
  - **非微扰地位.** \cref{asm:intro-bridge}（MA1、MA2）。
  - **地位与缺口.** Global nPDF fits assume leading-twist factorization (`Eskola:2021nhw`, `Kovarik:2015cma`, `AbdulKhalek:2022fyi`); the nuclear-size dependence of the power corrections is not controlled.
  - `\uses{thm:disall-factorization, asm:intro-bridge}`

**Worked examples.** `ex:disall-ladder`, `ex:disall-nlo`, `ex:disall-gluon`, `ex:disall-heavy-lo`.

**Tables.** `tab:disall-correspondence`: `prop:disall-two-routes`, `prop:disall-factorized-subtraction`, `thm:disall-renorm-compat`, `ex:disall-ladder` ↔ App N §N.5, §N.7 (assumptions; error types) [SYNC-APP].

**Figures.** Referred back to: `fig:reduced-dis` (Ch4), `fig:dis-oneloop` (Ch7); new (required): `fig:disall-seed` (adapt `fig:cw-dis-seed`), `fig:disall-heavy`, `fig:disall-ladder-regions` (refdoc S56).

**Misconception box.** M4, M25, M26 (Callan–Gross is LO only: $C_L^q=2C_Fz$); critic O7.

**Key citation keys.** `LibbySterman1978a`, `Collins2011`, `CollinsSoperSterman1989`, `Collins:2008sg`, `EllisEtAl1979`, `Ellis:1978sf`, `AmatiPetronzioVeneziano1978a`, `AmatiPetronzioVeneziano1978b`, `Mueller1978`, `Mueller:1981sg`, `CurciFurmanskiPetronzio1980`, `BardeenEtAl1978`, `AltarelliMartinelli1978`, `FurmanskiPetronzio1982`, `Vermaseren:2005qc`, `Moch:2004xu`, `DiemozEtAl1988`, `CollinsWilczekZee1978`, `AivazisEtAl1994`, `Aivazis:1993kh`, `Collins1998b`, `Kramer:2000hn`, `Thorne:1997ga`, `Buza:1996wv`, `Forte:2010ta`, `QiuSterman1991a`, `Luo:1993ui`, `Luo:1994np`, `Bodwin:1988fs`, `BodwinBrodskyLepage1981`, `Frankfurt:2011cs`, `Eskola:2021nhw`, `Kovarik:2015cma`, `AbdulKhalek:2022fyi`, `EllisStirlingWebber1996`.

**Pending.** App N statements and `ex:disall-ladder` [PENDING-VERIFY: X2].

---------------------------------------------------------------------------------------------------

## Chapter 11 — 其他共线过程：单举湮灭、SIDIS、光生、极化与横度 / Other collinear processes: SIA, SIDIS, photoproduction, polarized processes, transversity

`\label{ch:coll}` · `ch11_coll.tex` · **13 pp** · full · Part III

**Purpose.** Give each remaining collinear process class a home (critic §4 items 3, 4, 8, 11): one observed hadron in $e^+e^-$ (FFs) — with the light-cone-ordered pole lemma for all-final-state jets and the unitarity cancellation of unobserved jets (refdoc S33); collinear SIDIS (PDF ⊗ FF); photoproduction and photon structure (direct [A], resolved [C], diffractive resolved [V]); the photon PDF; longitudinally polarized DIS and the axial anomaly (scheme dependence of $\Delta\Sigma$/$\Delta G$); transversity. Each statement is a verification of `thm:method-template` or an OPE statement.

**Depends on.** Ch7–Ch10; App O (`lem:appO-lcopt`), App I.

**Box.**
- 证明了：`lem:coll-final-poles`（[R, R_PT]）；`prop:coll-anomaly-scheme`、`prop:coll-soffer`（[R, R_PT]，后者为 LO 演化的保持性）；`prop:coll-transversity-evolution`（[R, R_def]）；`thm:coll-g1-moments`、`prop:coll-photon-sf`（[R, R_OPE]）。
- 给出全阶论证：`lem:coll-unobserved-jet`、`prop:coll-sia-regions`、`thm:coll-sia`（另需 FF 乘法可重整性 `asm:appN-multren`(Z1)）、`thm:coll-sidis`、`thm:coll-direct-photo`、`prop:coll-luxqed`（[A]）。
- 没有证明：分辨光生（`conj:coll-resolved-photo`，[C]）；Burkhardt–Cottingham（`conj:coll-bc`，[C]）；衍射光生的标准因子化（`prop:coll-diffractive-photo`，[V]，实验）；Ellis–Jaffe、Wandzura–Wilczek（[V]）。

**Sections.**
1. `sec:coll-sia` $e^+e^-\to hX$ 与碎裂函数 (`fig:coll-sia`).
2. `sec:coll-sidis` 共线半单举 DIS (`fig:coll-sidis`).
3. `sec:coll-photo` 光生过程、光子结构与光子分布 (`fig:coll-photoproduction`).
4. `sec:coll-polarized` 纵向极化：$g_1$、轴反常与方案依赖.
5. `sec:coll-transversity` 横向极化与横度分布 (optional `fig:coll-transversity`).

**Canonical statements** (in reading order).

* **定义 `def:coll-sia` — 单举湮灭的运动学** (no tag) · v1
  - **陈述.** $z=2p_h\cdot q/q^2$; $\frac{d\sigma}{dz\,d\cos\theta}=\frac38(1+\cos^2\theta)\frac{d\sigma_T}{dz}+\frac34\sin^2\theta\frac{d\sigma_L}{dz}$, so that $\frac{d\sigma}{dz}=\frac{d\sigma_T}{dz}+\frac{d\sigma_L}{dz}$ (VF-MISC-5; cf. `NasonWebber1994`).
  - `\uses{def:pdf-ff}`

* **引理 `lem:coll-final-poles` — 全部为末态的共线子图的极点在同一半平面** [R, R_PT] · refdoc S33
  - **陈述.** Take a jet subgraph all of whose external collinear lines are final-state ($e^+e^-\to hX$; the current jet of SIDIS), in its light-cone-ordered representation (`lem:appO-lcopt`). Every energy denominator that depends on the minus component of a soft momentum $k$ entering the jet has its $k^-$ pole in the same half-plane, fixed by the direction of $k$.
  - **证明.** Full (energy denominators of an outgoing jet in light-cone-ordered form). Generalized by `lem:dy-poles-orientation` (Ch12, pointer). (本引理只涉及 Feynman 积分。)
  - `\uses{lem:appO-lcopt, def:coll-sia}`

* **引理 `lem:coll-unobserved-jet` — 未观测喷注与软辐射的幺正性相消** [A] · refdoc S33
  - **陈述.** The jets not containing $h$, and the soft radiation, cancel in the sum over their final states: the cut sum equals the discontinuity of the forward jet function, and the contour can be moved at distance $O(Q)$.
  - **证明.** Sketch (three arguments: unitarity of the cut sum, analyticity of the forward jet function, absence of pinches at $O(Q)$; Collins 2011 §12.8; `prop:method-fsi`).
  - **地位与缺口.** `asm:appN-cutsum` (cut-summed representation); E-S level.
  - `\uses{prop:method-fsi, prop:prelim-unitarity}`

* **命题 `prop:coll-sia-regions` — SIA 的领头区域** [A] · v1
  - **陈述.** Hard vertex, jet containing $h$, other jets, soft subgraph; Glauber regions not pinched (all collinear lines outgoing, `lem:coll-final-poles`); soft gluons and unobserved jets cancel by unitarity (`lem:coll-unobserved-jet`); soft factor 1.
  - **地位与缺口.** E-S; `asm:appN-envelope`, `asm:appN-cutsum`.
  - `\uses{thm:ir-leading-regions, lem:coll-final-poles, lem:coll-unobserved-jet}`

* **定理 `thm:coll-sia` — $e^+e^-\to hX$ 的因子化** [A] · v1 (+ refdoc S33)
  - **陈述.** $\frac{d\sigma^h}{dz}=\sum_i\int_z^1\frac{dy}y\hat\sigma_i(y,\frac{Q^2}{\mu^2},\alpha_s(\mu))d_{h/i}(\frac zy;\mu)+$ power corrections; $\sigma_L$ receives $1/Q$ corrections (`BenekeBraunMagnea1997`); the power in general [C].
  - **非微扰地位.** \cref{asm:intro-bridge}（MA1、MA2）。
  - **证明.** Deduction from `thm:method-template` with `lem:coll-final-poles`, `lem:coll-unobserved-jet`; `CollinsSoper1982a`, `Mueller1978` (cut vertices), Collins 2011 §12.5–12.8.
  - **地位与缺口.** Besides the generic `asm:appN-*` (`tab:method-hypotheses`), the independent input of the multiplicative renormalizability of FFs (`rem:pdf-ff-multren` = `asm:appN-multren`(Z1)).
  - `\uses{thm:method-template, prop:coll-sia-regions, lem:coll-final-poles, lem:coll-unobserved-jet, def:pdf-ff, rem:pdf-ff-multren, asm:appN-multren, asm:intro-bridge}`

* **注 `rem:coll-sia-nlo` — 系数函数与检验** (no tag) · v1
  - $O(\alpha_s)$ $\overline{\rm MS}$ coefficient functions (literature: `AltarelliEtAl1979`, `BaierFey1979`, `RijkenVanNeerven1996`, `RijkenVanNeerven1997`, `NasonWebber1994`; to verify — not computed by an agent); energy sum rule $\sum_h\int dz\,z\,\frac{d\sigma^h}{dz}=2\sigma_{\rm tot}$ returns `cor:ee-R-alphas`; analytic continuation from DIS (`CurciFurmanskiPetronzio1980`) with $\pi^2$ terms from $(-q^2)^{-\varepsilon}$; the collinear pole of the quark spectrum (`ex:ee-quark-spectrum`) is absorbed into $d_{h/q}$.

* **例 `ex:coll-sia-lo` — 领头阶 $e^+e^-\to hX$** (no tag) · v1
  - $\frac{d\sigma^h}{dz}=\frac{4\pi\alpha^2}{3s}N_c\sum_qe_q^2[d_{h/q}(z)+d_{h/\bar q}(z)]$ (VF-MISC-5); check $\sum_h\int dz\,z\frac{d\sigma^h}{dz}=2\sigma_{\rm tot}$ at LO from the momentum sum rule; angular distribution $1+\cos^2\theta$.
  - `\uses{thm:coll-sia, def:coll-sia}`

* **定理 `thm:coll-sidis` — 共线 SIDIS 的因子化** [A] · v1
  - **陈述.** For $P_{hT}$ integrated (or $P_{hT}\sim Q$): $d\sigma=\sum_{ij}f_{i/H}\otimes d\hat\sigma_{ij}\otimes d_{h/j}+\dots$; matching to TMD factorization (W + Y) in Ch14 (pointer).
  - **非微扰地位.** \cref{asm:intro-bridge}（MA1、MA2）。
  - **证明.** Deduction (one incoming hadron: final-state poles only, `lem:coll-final-poles` for the current jet); Collins 2011 §12.14, `Graudenz1994` (NLO), `Meng:1995yn`, `Nadolsky:1999kb`.
  - **地位与缺口.** As `thm:disall-factorization` and `thm:coll-sia`.
  - `\uses{thm:method-template, thm:disall-factorization, thm:coll-sia, lem:coll-final-poles, asm:intro-bridge}`

* **定理 `thm:coll-direct-photo` — 直接光生与光子结构函数** [A] · v1
  - **陈述.** Direct photoproduction behaves like DIS (one hadron); the proof "would appear to apply also to direct photo-production" (`Collins1998a` conclusions, [txt]).
  - **非微扰地位.** \cref{asm:intro-bridge}（MA1、MA2）。
  - **地位与缺口.** Inherits `thm:disall-factorization`; the separation direct/resolved is ambiguous beyond LO.
  - `\uses{thm:disall-factorization, asm:intro-bridge}`

* **命题 `prop:coll-photon-sf` — 光子结构函数的点状部分** [R, R_OPE] · v1
  - **陈述.** At large $Q^2$ the point-like part of $F_2^\gamma$ is computable (inhomogeneous evolution; `Witten:1977ju`, NLO `Bardeen:1978hg`); the hadronic component is non-perturbative.
  - **非微扰地位.** \cref{asm:intro-wightman}、\cref{asm:intro-composite}、\cref{asm:intro-np-ope}、\cref{asm:intro-af-coeff}（MA0、MA4）。
  - `\uses{thm:dis-ope, prop:dis-ope-rg, asm:intro-wightman, asm:intro-composite, asm:intro-np-ope, asm:intro-af-coeff}`

* **猜想 `conj:coll-resolved-photo` — 分辨光生** [C] · v1
  - **陈述.** Resolved photoproduction factorizes with photon PDFs like a hadron–hadron process with coloured final states.
  - **地位与缺口.** Effectively hadron–hadron with coloured final states (inherits `conj:dy-coloured-final`, Ch12, pointer); the separation direct/resolved is ambiguous beyond LO (`Collins1998a`, `Klasen:2002xb`).
  - `\uses{thm:coll-direct-photo}`

* **命题 `prop:coll-diffractive-photo` — 衍射光生中的因子化破坏** [V] · v1
  - **陈述.** **Resolved** diffractive photoproduction is hadron–hadron-like (survey item 28; c_glauber §3.6): standard factorization with the DDIS diffractive PDFs fails.
  - **地位与缺口.** Evidence: experiment, not a perturbative counterexample — H1: dijet photoproduction must be scaled by ≈0.5, "first clear observation of QCD hard scattering factorisation breaking at HERA" (`H1:2007jtx`); ZEUS (`ZEUS:2007uvk`); `Klasen:2008ah`: global suppression 0.42–0.71, or resolved-only suppression by about 3. **Direct** diffractive photoproduction is covered in principle by Collins' DDIS proof (`thm:break-ddis`, Ch18 — pointer); H1's suppression also of the direct component is an unresolved tension (ZEUS differs) — say so, without a tag of its own.
  - `\uses{conj:coll-resolved-photo}`

* **命题 `prop:coll-luxqed` — 质子的光子分布** [A] · v1
  - **陈述.** The photon PDF of the proton is determined model-independently as an integral over proton structure functions (`Manohar:2016nzj`, `Manohar:2017eqh`); point-like limit reproduces `Frixione:2019lga` eq. (4.189) (VF-FRO-11).
  - **非微扰地位.** \cref{asm:intro-wightman}、\cref{asm:intro-composite}（MA0、MA4）。
  - **地位与缺口.** Derivation at $O(\alpha)$ in QED with the operator definition of the photon PDF; QCD corrections to the matching at higher orders cited; further QED/EW factorization topics in Ch24 (pointer).
  - `\uses{def:pdf-gluon, def:dis-kinematics, asm:intro-wightman, asm:intro-composite}`

* **定义 `def:coll-g1` — 极化结构函数** (no tag) · v1
  - **陈述.** Antisymmetric part of $W^{\mu\nu}$ with $g_1,g_2$; $\varepsilon^{0123}=+1$ (VF-CONV-10); spin four-vector conventions.
  - `\uses{def:dis-kinematics, def:prelim-gamma5}`

* **定理 `thm:coll-g1-moments` — $g_1$ 的奇数矩** [R, R_OPE] · v1
  - **陈述.** Odd moments of $g_1$ are given by the OPE with axial twist-2 operators; first moment: non-singlet → Bjorken (`thm:dis-bjorken`); singlet: $\Delta\Sigma$ and $\Delta G$ mix through the axial anomaly; the split is scheme dependent (`AltarelliRoss1988`, `CarlitzCollinsMueller1988`, `Kodaira1980`, `Larin:1993tq`).
  - **非微扰地位.** \cref{asm:intro-wightman}、\cref{asm:intro-composite}、\cref{asm:intro-np-ope}、\cref{asm:intro-af-coeff}；第一阶矩另需 \cref{asm:intro-growth} 的极化类比（MA3）。
  - `\uses{thm:dis-ope, def:coll-g1, thm:dis-bjorken, prop:appI-larin, asm:intro-wightman, asm:intro-composite, asm:intro-np-ope, asm:intro-af-coeff}`

* **命题 `prop:coll-anomaly-scheme` — 一阶矩的方案依赖** [R, R_PT] · v1
  - **陈述.** (One loop.) The first moment of the $\gamma^*g$ box contribution to $g_1$ differs between HVBM and anticommuting-$\gamma_5$ treatments, i.e. between schemes for $\Delta\Sigma$ (critic §6 example) — explicit numbers derived by the writer (not verified by an agent).
  - **证明.** Full one-loop computation (App I).
  - `\uses{def:appI-hvbm, prop:appI-larin, def:coll-g1}`

* **命题 `prop:coll-ellis-jaffe` — Ellis–Jaffe 求和规则作为预言** [V] · v1
  - **陈述.** The Ellis–Jaffe sum rule assumes $\Delta s=0$ (and negligible gluon contribution).
  - **地位与缺口.** Evidence: experiment (EMC "spin crisis": `EMC1988`); `EllisJaffe1974`.
  - `\uses{thm:coll-g1-moments}`

* **猜想 `conj:coll-bc` — Burkhardt–Cottingham 求和规则** [C] · v1
  - **陈述.** $\int_0^1g_2\,dx=0$.
  - **地位与缺口.** Assumes no $J=0$ fixed pole or $\delta(x)$ term (compare the growth condition `asm:intro-growth` and `prop:dis-low-moments`); holds at $O(\alpha_s)$ in PT (`BurkhardtCottingham1970`).
  - `\uses{def:coll-g1}`

* **命题 `prop:coll-ww` — Wandzura–Wilczek 关系的一般失效** [V] · v1
  - **陈述.** $g_2=g_2^{\rm WW}$ fails in general because of genuine twist-3 $\bar qGq$ terms (`WandzuraWilczek1977`; critic B24).
  - **地位与缺口.** Evidence: explicit operator analysis (non-vanishing twist-3 matrix elements); not a statement about the size.
  - `\uses{def:coll-g1}`

* **定义 `def:coll-transversity` — 横度分布** (no tag) · v1
  - **陈述.** $h_1$ chiral-odd; absent from inclusive DIS at leading twist; accessible via SIDIS Collins effect (TMD, Ch14), dihadron FFs (collinear), transversely polarized DY (Ch12).
  - `\uses{def:pdf-polarized}`

* **命题 `prop:coll-transversity-evolution` — 横度的演化** [R, R_def] · v1 (composite)
  - **陈述.** (a) No gluon mixing for transversity at any order (helicity flip by two units has no gluon counterpart for a spin-½ target). (b)（领头阶核，状态以文字说明）$\Delta_TP_{qq}=C_F[\frac{2z}{(1-z)_+}+\frac32\delta(1-z)]$ (VF-POL-3, status C: standard, `ArtruMekhfi1990`; the writer re-derives it or hedges 「（待核实）」).
  - **非微扰地位.** 强子态：\cref{asm:intro-wightman}、\cref{asm:intro-composite}（MA0）。
  - `\uses{def:coll-transversity, def:pdf-polarized, asm:intro-wightman, asm:intro-composite}`

* **命题 `prop:coll-soffer` — Soffer 不等式（LO 演化的保持性）** [R, R_PT] · v1
  - **陈述.** (At LO.) If $|h_1|\le\frac12(f_1+g_1)$ holds at a scale $\mu_0$ for LO-evolved densities, LO evolution preserves it for $\mu>\mu_0$ (`Soffer1995`; critic B24). Remark (print): the inequality itself follows only from the positive density-matrix (number-density) interpretation, a heuristic (`rem:pdf-number-density`); for $\overline{\rm MS}$ densities it is not a theorem and is scheme dependent beyond LO — the same caveats as `conj:pdf-positivity` (C13; do not state Soffer-type bounds as theorems).
  - **证明.** Full (LO kernels).
  - `\uses{prop:coll-transversity-evolution, prop:pdf-lo-kernels}`

* **注 `rem:coll-christ-lee` — 单举 DIS 中无单靶自旋横向不对称** (no tag) · v1
  - Inclusive DIS transverse single-target-spin asymmetry vanishes at one-photon exchange by T invariance (`ChristLee1966`).

*(Polarized Drell–Yan and $A_{LL}$ in hadron collisions are in Ch12 as `thm:dy-polarized`, `conj:dy-polarized-jets`.)*

**Worked example.** `ex:coll-sia-lo`.

**Tables.** No separate soft-function table in this chapter; the observable ↔ soft-function table is `tab:jets-soft-functions` (Ch16, optional; refdoc T19, S35).

**Figures.** New (required): `fig:coll-sia`, `fig:coll-sidis`, `fig:coll-photoproduction`; optional `fig:coll-transversity`.

**Misconception box.** "Inclusive DIS has transverse SSAs from FSI" (Christ–Lee); M23 (timelike = spacelike kernels); "diffractive PDFs are universal" (only DDIS; Ch18).

**Key citation keys.** `CollinsSoper1982a`, `Mueller1978`, `AltarelliEtAl1979`, `BaierFey1979`, `RijkenVanNeerven1996`, `RijkenVanNeerven1997`, `NasonWebber1994`, `BenekeBraunMagnea1997`, `CurciFurmanskiPetronzio1980`, `GribovLipatov1972b`, `Graudenz1994`, `Meng:1995yn`, `Nadolsky:1999kb`, `Collins2011`, `Witten:1977ju`, `Bardeen:1978hg`, `Klasen:2002xb`, `Collins1998a`, `H1:2007jtx`, `ZEUS:2007uvk`, `Klasen:2008ah`, `Manohar:2016nzj`, `Manohar:2017eqh`, `Frixione:2019lga`, `Bjorken1966`, `EllisJaffe1974`, `EMC1988`, `Kodaira1980`, `AltarelliRoss1988`, `CarlitzCollinsMueller1988`, `LarinVermaseren1991`, `Larin:1993tq`, `BurkhardtCottingham1970`, `WandzuraWilczek1977`, `RalstonSoper1979`, `JaffeJi1991`, `JaffeJi1992`, `Soffer1995`, `ArtruMekhfi1990`, `MertigVanNeerven1996`, `Vogelsang1996`, `AltarelliForteRidolfi1998`, `ChristLee1966`, `MeleNason1991`, `CacciariGrecoNason1998`.

**Pending.** None specific (generic `asm:` status per [SYNC-ASM]).

---------------------------------------------------------------------------------------------------

## Chapter 12 — Drell–Yan 过程与强子—强子碰撞 / Drell–Yan and hadron–hadron collisions

`\label{ch:dy}` · `ch12_dy.tex` · **18 pp** · full (precise forms in App O and App N) · Part III

**Purpose.** Verify `thm:method-template` for inclusive DY, where (H3) — the Glauber region — is genuinely new; give the CSS/Bodwin/Collins argument in structured form with an honest four-layer status (survey paragraph; the precise conditional chain App O → App N; the open inputs by label; the absence of counterexamples); orientation of light-cone-ordered intermediate states and the location of the $k^-$ poles; why a single cut graph gives a future-pointing Wilson line and the past-pointing line appears only after the one-sided rewriting; an explicit abelian model in which the spectator Glauber phase cancels by unitarity, and its light-cone-ordered form; the exact two-gluon exchange between eikonal lines ($O(g^4)$ unitarity, Regge phase; candidate 「本书新结果」); what NNLO/N3LO agreement does and does not test; the Doria–Frenkel–Taylor premises; the one-loop $\overline{\rm MS}$ coefficient functions; other colour-singlet processes [A]; coloured final states [C]; higher twist.

**Depends on.** Ch4 (`def:ir-glauber`, `prop:ir-glauber-trapping`, `thm:ir-leading-regions`), Ch8 (`def:pdf-quark`, `def:pdf-gluon`, `thm:pdf-dglap`, `prop:pdf-partonic-dr`), Ch9 (`prop:method-glauber-deformation`, `lem:method-soft-unitarity`, `prop:method-glauber-oneloop`, `prop:method-fsi`, `thm:method-template`), Ch10, Ch11 (`lem:coll-final-poles`); App O, App N [SYNC-APP].

**Box.**
- 证明了：`prop:dy-born`、`prop:dy-glauber-pinch`、`lem:dy-poles-orientation`、`prop:dy-eikonal-twogluon`、`prop:dy-nlo`、`prop:dy-scale`（[R, R_PT]）；`prop:dy-universality`、`ex:dy-future-vs-past`（[R, R_def]）；`thm:appO-main`、`prop:appN-dy`（[R, R_cond]，附录 O、N）；`prop:dy-abelian-model`（[P]：阿贝尔程函模型中的完整证明）。
- 给出全阶论证：`prop:dy-regions`、`lem:dy-fsi`、`prop:dy-deformation`、`lem:dy-soft`、`thm:dy-factorization`、`thm:dy-colour-singlet`、`thm:dy-polarized`、`thm:dy-higher-twist`（[A]；瓶颈 `asm:appO-mixing`(c)、`asm:appO-deformation`(b)–(d)、`asm:appO-rewritten-cs`）。
- 没有证明：非程函（复合、相互作用）旁观者与活动部分子的 Glauber–软–共线混合（`asm:appO-mixing`(c)）；有色末态（`conj:dy-coloured-final`，[C]）；$1/Q^2$ 以外的幂次（`prop:dy-twist6-failure`，[V]）。

**Sections.**
1. `sec:dy-born` 运动学与 Born 截面.
2. `sec:dy-regions` 领头区域：初态与末态相互作用 (`fig:reduced-dy`, owned by Ch4; `fig:glauber-exchange` — use it to show initial- and final-state soft gluons with the active and spectator poles on opposite sides, refdoc S15.7; caption supplement on the two-component deformation, M31).
3. `sec:dy-orientation` 光锥序中间态的取向与 $k^-$ 极点 (`fig:dy-pole-orientation`) — **new section** (refdoc S34).
4. `sec:dy-glauber` Glauber 问题及其在单举 DY 中的解决 — unitarity, one-sided rewriting, future vs past lines, the App O chain, soft factor 1.
5. `sec:dy-model` 阿贝尔模型、光锥序表示与程函线间的双胶子交换 (`fig:dy-abelian-model`, `fig:dy-two-gluon-exchange`).
6. `sec:dy-theorem` 主定理与其地位 — `tab:dy-status`; what NNLO tests; DFT premises.
7. `sec:dy-nlo` $O(\alpha_s)$ 系数函数 (`fig:dy-oneloop`).
8. `sec:dy-other` 其他强子—强子过程.
9. `sec:dy-twist` 高扭度：$1/Q^2$ 处的广义因子化及其在更高幂次的失效.
10. Closing: `tab:dy-correspondence` (chapter statement | App O / App N version | difference).

**Canonical statements** (in reading order).

* **定义 `def:dy-kin` — DY 运动学** (no tag) · v1
  - **陈述.** $A(P_A)+B(P_B)\to\gamma^*(q)+X$, $\tau=Q^2/s$, $y=\frac12\ln(q^+/q^-)$, $x_{A,B}=\sqrt\tau e^{\pm y}$; normalization through the master formula $\hat s\frac{d\hat\sigma}{dQ^2}=\frac{2\alpha^2}{3Q^2}\int d\Phi_{\gamma^*X}\langle-g_{\mu\nu}H^\mu H^{\nu*}\rangle$, lepton tensor $\int d\Phi_2L_{\mu\nu}=\frac1{6\pi}(q_\mu q_\nu-q^2g_{\mu\nu})$ (VF-DY-2).
  - `\uses{def:prelim-lightfront}`

* **命题 `prop:dy-born` — Born 截面** [R, R_PT] · v1
  - **陈述.** (Lowest order.) $\frac{d\sigma}{dQ^2dy}=\frac{4\pi\alpha^2}{3N_cQ^2s}\sum_qe_q^2[q(x_A)\bar q(x_B)+\bar q(x_A)q(x_B)]$; $\hat\sigma(q\bar q\to\ell^+\ell^-)=\frac{4\pi\alpha^2e_q^2}{3N_c\hat s}$; Jacobian 1; Drell–Yan scaling (VF-DY-1).
  - **证明.** Full.
  - `\uses{def:dy-kin, def:pdf-quark}`

* **命题 `prop:dy-regions` — DY 的领头区域** [A] · v1
  - **陈述.** $H$ (one per side of the cut), $J_A$, $J_B$ (incl. spectators), soft subgraph connecting $J_A$, $J_B$, plus Glauber exchanges, in particular between spectators; initial- vs final-state interactions.
  - **证明.** Sketch (`thm:ir-leading-regions`).
  - **地位与缺口.** E-S; Feynman-gauge incompleteness (extra disconnected hard scatterings, `Labastida:1984gy`); `asm:appN-envelope`, `asm:appN-separation`.
  - `\uses{thm:ir-leading-regions, def:dy-kin}`

* **命题 `prop:dy-glauber-pinch` — 单个割图中的 Glauber 钳夹** [R, R_PT] · v1
  - **陈述.** (One loop, explicit.) For an exchange between an incoming active parton and an outgoing spectator of the same hadron (or between spectators) the $k^-$ poles lie on both sides; the contour is trapped at $|k^-|\sim k_T^2/p^+$ (`prop:ir-glauber-trapping`; c_dy G-iii: lifting the contour changes the value).
  - **证明.** Full.
  - `\uses{prop:ir-glauber-trapping, def:ir-glauber}`

* **引理 `lem:dy-poles-orientation` — 光锥序中间态的取向与 $k^-$ 极点** [R, R_PT] · refdoc S34 [PENDING-VERIFY: X1]
  - **陈述.** In the finite-$\eta_0$ light-cone-ordered representation of `lem:appO-lcopt`: (a) orientation is a property of light-cone-ordered intermediate states, not of lines; in the standard flow (initial lines carry $+k^-$, final lines $-k^-$) the intermediate states of $J_A$ before the hard vertex give energy denominators with one sign of $i0$, those after it the opposite sign; cut $\delta$-functions are free of soft light-cone components. (b) Hence the $k^-$ poles of the lines coupling to a soft $k$ lie on one side iff all the intermediate states it traverses have one orientation. Generalizes `lem:coll-final-poles` and `prop:dy-glauber-pinch`; replaces the line-by-line pole tables (c_glauber §1.2, kept as an example).
  - **证明.** Full (App O §O.3). `fig:dy-pole-orientation`. (本引理只涉及 Feynman 积分。)
  - `\uses{lem:appO-lcopt, lem:coll-final-poles, prop:dy-glauber-pinch}`

* **注 `rem:dy-one-time-per-jet` — 每个喷注一个光锥时间** (no tag) · refdoc S34 (E10)
  - One light-cone time per jet ($x^+$ for $J_A$, $x^-$ for $J_B$): the hybrid ordering of Aybat–Sterman 2009 (`AybatSterman2009`); "compatible with the measurement" means that the measurement acts as the identity operator between cut states (precise criterion: `prop:break-measurement`, Ch18, pointer).

* **引理 `lem:dy-fsi` — 旁观者末态相互作用的幺正性相消** [A] · v1 (+ refdoc S34)
  - **陈述.** After summing over all final-state cuts of the spectator systems (inclusive in $X$), interactions after the hard scattering cancel: the sum over cuts of final-state interactions equals the uncut subgraph with the interactions removed.
  - **证明.** Sketch; precise form `lem:appO-unitarity` [R, R_cond: `asm:appO-lcopt`]; `CollinsSoperSterman1985b`, `CollinsSoperSterman1988`, `Bodwin1985` (+ erratum), Collins 2011 §14.4 (follows CSS 1988 "with some important improvements and with correction of errors… supersedes Bodwin 1985 and CSS 1985a", p. 553, [txt]) [PENDING-VERIFY: E31]; LCPT version `Diehl:2015bca` §4.
  - **地位与缺口.** The [A] concerns the premises (leading regions, LCOPT applicability `asm:appO-lcopt`).
  - `\uses{prop:method-fsi, lem:appO-unitarity, asm:appO-lcopt}`

* **例 `ex:dy-future-vs-past` — 单个割图给出未来指向的 Wilson 线** [R, R_def] · refdoc S34 [PENDING-VERIFY: X1] (misconception M33)
  - **陈述.** For an active parton (charge $Q_a$) and a spectator (charge $Q_s=-Q_a$, colour neutrality) of hadron $A$ coupling to a soft gluon: $\frac{iQ_a}{k^-+i0}+iQ_s\big[\frac1{k^-+i0}-\frac1{k^--i0}\big]=\frac{iQ_a}{k^--i0}$ (VF-REF-11): a single cut graph gives the **future**-pointing line; the past-pointing line appears only after the one-sided rewriting (`prop:appO-past-wilson` [A]).
  - **证明.** Full (one line; the Glauber phase of `prop:method-glauber-oneloop`).
  - `\uses{prop:prelim-wilson-rules}`

* **命题 `prop:dy-deformation` — 移除末态极点后的围道变形** [A] · v1→rev. (refdoc S34) [PENDING-VERIFY: X1]
  - **陈述.** After the cut sum, the remaining $k^-$ poles of $A$-collinear lines coupling to a soft gluon can be brought to one side, and the soft momentum can be deformed out of the Glauber region along $e_G$; the Grammer–Yennie approximant then holds with **past-pointing** Wilson lines.
  - **证明.** Sketch; the App O chain: (1) cut-summed unitarity (`lem:appO-unitarity`); (2) equal-light-cone-time localization (`lem:appO-equal-time`, `lem:appO-joint-localization`); (3) one-sided rewriting with the entire carrier (App O §O.6, `prop:appO-one-sided`); (4) simultaneous deformation along $e_G$ (`prop:appO-target`); (5) eikonal bounds (`prop:appO-eikonal`); (6) past-pointing Wilson lines (`prop:appO-past-wilson`). Collins 2011 §14.4.1 steps (region decomposition, sum over cuts, deformation "away from initial-state singularities" with final-state ones crossed but cancelled after the sum over cuts, Grammer–Yennie with past-pointing lines, Ward identities); `AybatSterman2009` (phases with initial-state partons; credit for the hybrid ordering).
  - **地位与缺口.** [A]: `asm:appO-mixing`, `asm:appO-deformation` (b)–(d) needed even for abelian graphs, `asm:appO-envelope`, `asm:appO-rewritten-cs`; Collins 2011 §14.4.8.
  - `\uses{prop:method-glauber-deformation, lem:dy-fsi, lem:dy-poles-orientation, lem:appO-unitarity, lem:appO-equal-time, lem:appO-joint-localization, prop:appO-one-sided, prop:appO-target, prop:appO-eikonal, prop:appO-past-wilson, asm:appO-mixing, asm:appO-deformation, asm:appO-envelope, asm:appO-rewritten-cs}`

* **引理 `lem:dy-soft` — 软因子为 1** [A] · v1
  - **陈述.** The soft gluons decouple into past-pointing Wilson lines; for the $q_T$-integrated cross section T invariance (Collins 2011 §13.17) equates past- and future-pointing soft factors and unitarity gives 1 (`lem:method-soft-unitarity`; Collins 2011 §14.4.6). Bodwin–Brodsky–Lepage phases "do not break factorization; rather they get moved into the parton densities" (§14.4.7, [txt]).
  - **地位与缺口.** Inherits `prop:dy-deformation`.
  - `\uses{prop:dy-deformation, lem:method-soft-unitarity, prop:appO-past-wilson}`

* **命题 `prop:dy-universality` — DY 与 DIS 的共线 PDF 是同一对象** [R, R_def] · v1
  - **陈述.** For $w=(0^+,w^-,\mathbf 0_T)$: $W[w,-\infty n_B]W[-\infty n_B,0]=W[w,0]=W[w,\infty n_B]W[\infty n_B,0]$ (composition and retracing). (Contrast: TMD staples do not collapse, Ch14.)
  - **证明.** Full.
  - `\uses{prop:prelim-wilson-covariance, def:pdf-quark}`

* **命题 `prop:dy-abelian-model` — 阿贝尔模型中旁观者 Glauber 相位的相消** [P] · v1
  - **陈述.** In an abelian theory with massive vector boson and eikonal spectators (c_dy §7, VF-DY-13): (G-i) spectator–spectator exchanges sum to $e^{i\chi(b)}$, $\chi(b)=-\frac{g_Ag_B}{2\pi}K_0(m|b|)$ (real); (G-ii) the phase cancels in any cross section inclusive in the spectators' relative transverse momentum, order by order ($O(g^{2n})$: $\sum_j\frac{(i\chi)^j}{j!}\frac{(-i\chi)^{n-j}}{(n-j)!}=0$) and to all orders ($|e^{i\chi}|^2=1$), including $q_T$ spectra at leading power; (G-iii) the spectator–spectator Glauber region is trapped; (G-iv) the active–spectator exchange is not trapped in $k^+$ and belongs to the $A$-collinear subgraph with a past-pointing Wilson line. Not shown: non-abelian case, all-order region analysis, power corrections, measured hadrons.
  - **证明.** Full `proof` of the model statement (residues, eikonal identity, Parseval); our derivation, novelty not claimed [PENDING-VERIFY: N25].
  - **地位与缺口.** [P]: the QCD claim is established only in this model (WRITER_SPEC_v2 §4.10 item 5).
  - `\uses{prop:method-glauber-oneloop, lem:prelim-eikonal-identity}`

* **例 `ex:dy-spectator-lcopt` — 旁观者模型的光锥序表示** (no tag) · refdoc S34 (E8) [PENDING-VERIFY: X1]
  - The two orderings equal the two covariant propagators; the $k^-$ integral is an equal-light-cone-time transfer of $k_T$; single orderings depend on the regulator, their sum does not; combined with the kernel $\chi(b)=-\frac{e_Ae_B}{2\pi}K_0(m_gb)$ of `prop:dy-abelian-model` and the $\Delta$-integrated cancellation (c_glauber §1.5, c_dy §7).
  - `\uses{lem:appO-lcopt, lem:dy-poles-orientation, prop:dy-abelian-model}`

* **例 `ex:dy-glauber-model` — 阿贝尔 Glauber 模型的数值演示** (no tag) · v1
  - `prop:dy-abelian-model` with the FFT illustration: pointwise non-cancellation (~30 %) vs exact cancellation after $\int d^2\Delta$ (c_glauber §1.5).
  - `\uses{prop:dy-abelian-model}`

* **命题 `prop:dy-eikonal-twogluon` — 两条程函线之间的双胶子交换：$O(g^4)$ 幺正性与 Regge 相位** [R, R_PT] · refdoc S37 · **「本书新结果（待文献核查）」 candidate** [PENDING-VERIFY: N01, S63-5] (misconception M32)
  - **陈述.** (At $O(g^4)$.) Two infinite time-like Wilson lines (rapidity difference $Y>0$, colour generators $\mathbf T_A,\mathbf T_B$) exchange two gluons of mass $m$ (IR regulator) with exact propagators ($k^+k^-$ kept), at fixed transverse momenta; $a=\mathbf k_T^2+m^2$, $b=(\mathbf K-\mathbf k)_T^2+m^2$. (a) Longitudinal integrals: $J_{\rm box}=\frac{2\pi}{ab}(\pi+iY)$, $J_{\rm cross}=-\frac{2\pi iY}{ab}$; with $X=\mathbf T_A\cdot\mathbf T_B$, $c_{\rm box}=X^2$, $c_{\rm cross}=X^2+\frac{C_A}2X$: $J_{\rm box}c_{\rm box}+J_{\rm cross}c_{\rm cross}=\frac{2\pi}{ab}[\pi X^2-iY\frac{C_A}2X]$. (b) After the transverse integrals the first term is the exponentiation term $\frac12(-i\chi)^2X^2$ (VF-REF-9); the second is $i\times$real$\times$Hermitian: the one-loop reggeization phase $\propto C_AY$. (c) In the parametrization of `lem:appO-glauber-operator`, $p_{\rm opp}=-iY/\pi$, so ${\rm Re}\,p_{\rm opp}=0$ and the strict-window residual $-\frac12C_A\chi^2({\rm Re}\,p_{\rm opp})X$ vanishes; the two-gluon exchange graphs give $\mathcal V^\dagger\mathcal V=1+O(\chi^3)$ with no real emission (real cuts start at $O(g^6)$ for straight lines, since one-gluon emission from straight infinite lines is $\propto\delta(v\cdot k)$). Not shown: the other $O(g^4)$ graphs (argued to contribute only phases by unitarity of the eikonal system); non-eikonal spectators; all orders.
  - **证明.** Full (App O §O.8; residues in $k^+$ and $k^-$). Checks: R3 `work_R3/scripts/eikonal_box*.py` ($<5\times10^{-16}$ at 10 points; residues checked against brute-force $i\varepsilon$ quadrature), rerun by the synthesizer; `fig:dy-two-gluon-exchange`. Ingredients are classical (`Cheng:1969eh`, `Korchemskaya:1994qp`, `Korchemsky:1993hr`, `Caron-Huot:2013fea`); the marker is printed only if `verify/` records two independent confirmations and the literature check finds no prior statement of the conclusion (WRITER_SPEC_v2 §6.5); otherwise cite the prior source and present it as 「本书给出的推导」. (本命题只涉及程函线模型。)
  - `\uses{prop:prelim-wilson-rules, lem:qcd-colour-identities, lem:appO-glauber-operator}`

* **注 `rem:dy-common-ordering` — 共同时序是物理结果** (no tag) · refdoc S37 [PENDING-VERIFY: N01]
  - (i) The exact graphs put the whole $s$-channel weight into the uncrossed graph; the RS regulator agrees: crossed Glauber boxes vanish, and the ladders exponentiate to a Hermitian colour phase (`RothsteinStewart2016` eqs. (9.1), (9.18), (9.19), as read by c_glauber [PENDING-VERIFY: S63-9]). (ii) For eikonal spectators to all orders, unitarity follows from the unitarity of $T\exp\{ig\int dt[v_A\cdot A(v_At)\mathbf T_A+v_B\cdot A(v_Bt+\mathbf b)\mathbf T_B]\}$, at the same formal level as `lem:method-soft-unitarity`. (iii) The genuine open problem is the interplay of Glauber, soft and collinear modes for non-eikonal (composite, interacting) spectators and for active partons (`asm:appO-mixing`(c)). Never write 「非阿贝尔双 Glauber 残差是 DY 因子化的开放障碍」 (S58, M32).

* **定理 `thm:dy-factorization` — 单举 DY 的共线因子化** [A] · v1 (+ refdoc S34)
  - **陈述.** $$\frac{d\sigma}{dQ^2dy}=\sum_{ij}\int_{x_A}^1\frac{d\xi_A}{\xi_A}\int_{x_B}^1\frac{d\xi_B}{\xi_B}f_{i/A}(\xi_A;\mu)f_{j/B}(\xi_B;\mu)\,\mathcal H_{ij}\Big(\frac{x_A}{\xi_A},\frac{x_B}{\xi_B},\frac Q\mu,\alpha_s(\mu)\Big)+O\Big(\Big(\frac\Lambda Q\Big)^p\Big),$$ $p$ not fixed by the proof ([C]; expected 2, renormalon analyses `BenekeBraun1995b`).
  - **非微扰地位.** \cref{asm:intro-bridge}（MA1、MA2、MA4）。
  - **证明.** `proofsketch` in which the deduction from `prop:dy-regions`–`prop:dy-universality` and `thm:method-template` is written out completely (WRITER_SPEC_v2 §4.10).
  - **地位与缺口 (four layers; print).** (1) Survey paragraph, unchanged in substance: 「状态 [A]。CSS (1985, 1988) 与 Bodwin (1985) 给出了全阶论证的关键步骤（Glauber 区的围道变形、末态相互作用的幺正性相消、软因子为 1）；Collins (2011) §14.4 在 CSS 1988 基础上改进并纠正了若干错误。§14.4.8 'Issues remaining' 列出：(i) 证明依赖微扰论的动量分类，非微扰的'分级快度' Glauber 交换（多周边、类 Regge）未被覆盖；(ii) Feynman 规范下领头区域不完备（额外的不连通硬散射，须对图求和后相消，Labastida–Sterman 1985）；(iii) '现有真正的证明显然是令人生畏的'。Rothstein–Stewart (2016) 的 Glauber 算符框架复现了旁观者相位的相消，但'单独来看远不是因子化的证明'，其宣布的完整 SCET 证明截至 2026 年 10 月尚未发表。」 (2) 「精确形式」: `thm:appO-main` [R, R_cond] → `cor:appO-interface` → `prop:appN-dy` [R, R_cond] → the factorized form. (3) Open inputs by label: `asm:appO-lcopt`, `asm:appO-envelope`, `asm:appO-mixing`(c) (beyond the $O(g^4)$ eikonal case), `asm:appO-deformation`(b)(c)(d) (**needed even for abelian graphs**), `asm:appO-rewritten-cs`, the generic `asm:appN-*`, and `asm:intro-bridge`. (4) 「没有已知的领头幂次反例；文献中 strict-window 的非幺正残差是截断假象（\cref{prop:dy-eikonal-twogluon}）。」 Credit `AybatSterman2009` (hybrid light-cone ordering, pinch replaced by a mismatch of deformation directions) and `Diehl:2015bca` [PENDING-VERIFY: X1, N01, A11]. Error types per step: `tab:dy-status`.
  - `\uses{thm:method-template, prop:dy-regions, lem:dy-fsi, prop:dy-deformation, lem:dy-soft, prop:dy-universality, thm:appO-main, cor:appO-interface, prop:appN-dy, def:pdf-quark, def:pdf-gluon, asm:intro-bridge, asm:appO-lcopt, asm:appO-envelope, asm:appO-mixing, asm:appO-deformation, asm:appO-rewritten-cs, asm:appN-collins, asm:appN-cutsum}`

* **注 `rem:dy-nnlo-not-glauber` — 固定阶部分子截面不检验旁观者 Glauber 相消** (no tag) · refdoc S34 (misconception M30)
  - Fixed-order partonic cross sections contain no hadron spectators; their finiteness after mass factorization (NNLO, N3LO) tests the active-parton Glauber contributions to that order, not spectator–spectator exchanges (which are the content of `prop:dy-abelian-model` and App O); it is evidence, not proof.

* **注 `rem:dy-dft-premises` — Doria–Frenkel–Taylor 非相消的前提** (no tag) · refdoc S34 (E28)
  - The Doria–Frenkel–Taylor non-cancellation (two loops, non-abelian, massive coloured initial partons, fixed colour) lies outside the premises of `thm:appO-main` (massless active partons, colour-singlet hadrons); the term $\frac{m^2}{2(p_A^+)^2}k^+$ in the $A$-line denominator ties $k^+$ to $k^-$ (VF-REF-8); the DFT terms are power suppressed ($m^2/s$) and vanish after averaging over the colours of the incoming partons (colour-singlet hadrons); for hadronic DY, factorization fails at $m^4/s^2$ (`Basu:1984ba`, CSS 1989 §10.2; `prop:dy-twist6-failure`, pointer). Literature: `DoriaFrenkelTaylor1980`, `Frenkel:1983di`, `Catani:1985xt`, `Andrasi:1980qw`, `DiLietoEtAl1981`; compare `prop:ir-bn-failure`.

* **命题 `prop:dy-nlo` — $O(\alpha_s)$ 的 $\overline{\rm MS}$ 系数函数** [R, R_PT] · v1
  - **陈述.** (At one loop; c_dy, VF-DY-8.) $\frac{d\sigma}{dQ^2}=\frac{\sigma_0}s\sum_qe_q^2\int dx_1dx_2dz\,\delta(x_1x_2z-\tau)\{[q\bar q+\bar qq]\Delta_{q\bar q}(z)+[g(q+\bar q)+(q+\bar q)g]\Delta_{qg}(z)\}$, $\sigma_0=\frac{4\pi\alpha^2}{3N_cQ^2}$, $\Delta_{q\bar q}=\delta(1-z)+\frac{\alpha_s}{2\pi}\{C_F[4(1+z^2)\mathcal D_1-2\frac{1+z^2}{1-z}\ln z+(\frac{2\pi^2}3-8)\delta(1-z)]+2P_{qq}\ln\frac{Q^2}{\mu_F^2}\}$, $\Delta_{qg}=\frac{\alpha_s}{2\pi}\{T_F[(z^2+(1-z)^2)\ln\frac{(1-z)^2}z+\frac12+3z-\frac72z^2]+P_{qg}\ln\frac{Q^2}{\mu_F^2}\}$ (product convention for $(1+z^2)\mathcal D_1$; whole-term plus would change the $\delta$ coefficient by $7C_F$); no $\mu_R$ dependence at this order.
  - **证明.** Full — matrix elements, $D$-dimensional phase space, real exact in $\varepsilon$, timelike form factor, Laurent table, origin of $\frac{2\pi^2}3=-\frac{\pi^2}2+\frac{\pi^2}6+\pi^2$, mass factorization (two PDFs ⇒ $2P_{qq}$; $qg$ channel subtraction $f_{\bar q/g}\otimes\hat\sigma_{q\bar q}$). Literature: agreement with `Duhr:2020sdp` (ancillary files) incl. $\mu_F$ terms; threshold constant `Moch:2005ky`; form factor `MochVermaserenVogt2005`; first NLO: `AltarelliEllisMartinelli1979` (DIS scheme — attribution of the $\overline{\rm MS}$ form phrased carefully), `KubarAndrePaige1979`; NNLO `HambergVanNeervenMatsuura1991`. (本命题只涉及部分子态。)
  - `\uses{def:dy-kin, prop:sudakov-oneloop, lem:prelim-plus-expansion, prop:pdf-partonic-dr, lem:appC-phase-space}`

* **例 `ex:dy-nlo` — $O(\alpha_s)$ 系数函数的完整推导** (no tag) · v1
  - Full derivation; c_dy `dy_oneloop.tex` is a ready Chinese draft — adapt; its `fig:dy1l-diagrams` → use `fig:dy-oneloop`.
  - `\uses{prop:dy-nlo}`

* **命题 `prop:dy-scale` — $\mu_F$ 无关性** [R, R_PT] · v1
  - **陈述.** $d\sigma/d\ln\mu_F^2=O(\alpha_s^2)$ (Mellin exact; $x$-space numerics $10^{-13}$) (VF-DY-11).
  - **证明.** Full.
  - `\uses{prop:dy-nlo, thm:pdf-dglap}`

* **注 `rem:dy-dis-scheme` — DIS 方案中的 DY 与 PDF 的普适性** (no tag) · v1
  - DIS-scheme DY: $\Delta^{\rm DIS}_{q\bar q}=C_F[(1+\frac{4\pi^2}3)\delta(1-z)+2(1+z^2)\mathcal D_1+3\mathcal D_0-6-4z]$, $\Delta^{\rm DIS}_{qg}=T_F[(z^2+(1-z)^2)\ln(1-z)+\frac32-5z+\frac92z^2]$; $\Delta^{\overline{\rm MS}}_{q\bar q}-2C_2^q=\Delta^{\rm DIS}_{q\bar q}$, $\Delta^{\overline{\rm MS}}_{qg}-C_2^g=\Delta^{\rm DIS}_{qg}$ verified to $10^{-30}$ (critic c2; VF-DY-10): universality of PDFs between DIS and DY at one loop; the "plus trap" (VF-DY-12) [PENDING-VERIFY: N25 — attribution only].

* **例 `ex:dy-threshold` — 大 $N$ 极限** (no tag) · v1
  - VF-DY-14; large $N$: $\Delta_{q\bar q,N}=1+aC_F[4\ln^2\bar N+8\zeta_2-8]+O(\ln N/N)$, $a=\alpha_s/2\pi$; leads to Ch13.
  - `\uses{prop:dy-nlo, lem:prelim-mellin}`

* **定理 `thm:dy-colour-singlet` — 色单态末态** [A] · v1
  - **陈述.** $W$, $Z$, Higgs (gluon fusion via the heavy-top effective vertex or full theory), dibosons: the proof of `thm:dy-factorization` applies unchanged. Literature for the hard functions: `AltarelliEllisMartinelli1979`, `Dawson1991`, `DjouadiSpiraZerwas1991`, `HarlanderKilgore2002`, `AnastasiouEtAl2015`.
  - **非微扰地位.** \cref{asm:intro-bridge}（MA1、MA2）。
  - **地位与缺口.** As `thm:dy-factorization`.
  - `\uses{thm:dy-factorization, asm:intro-bridge}`

* **定理 `thm:dy-polarized` — 极化 Drell–Yan** [A] · v1
  - **陈述.** Longitudinally and transversely polarized DY factorize as unpolarized DY (`thm:dy-factorization`), with helicity and transversity PDFs (`def:pdf-polarized`); transverse: `RalstonSoper1979`, `JaffeJi1991`.
  - **非微扰地位.** \cref{asm:intro-bridge}（MA1、MA2、MA4）。
  - **证明.** Sketch (the proof of `thm:dy-factorization` with spin projectors).
  - **地位与缺口.** As `thm:dy-factorization`.
  - `\uses{thm:dy-factorization, def:pdf-polarized, asm:intro-bridge}`

* **猜想 `conj:dy-coloured-final` — 强子对撞中有色末态的共线因子化** [C] · v1 (+ refdoc S39)
  - **陈述.** Single-inclusive hadrons and jets at large $p_T$ and heavy-quark pairs in hadron–hadron collisions factorize in the standard collinear form.
  - **地位与缺口.** Universally used but unproven. Evidence/obstructions: Collins 2011 §14.7 ("relative lack of detailed proofs… One notable exception is Nayak, Qiu, and Sterman (2005)"); `Diehl:2015bca` §5 (absence of Glauber effects not proven for coloured final states); `Collins:1985gm` (heavy quarks: "an analysis at all orders… is needed to reliably establish this conjecture"); `AybatSterman2009` (outline); `CataniDeFlorianRodrigo2012` §8 (possible N3LO issue); NLO heavy quarks `NasonDawsonEllis1988`; jets `Kang:2016mcy`. In the App O framework the argument fails at the one-sided-rewriting step (O-3) for coloured final states (refdoc S39; `prop:break-measurement`, pointer). Survey item 9; critic O14.
  - `\uses{thm:dy-factorization}`

* **猜想 `conj:dy-polarized-jets` — 极化强子对撞中的 $A_{LL}$（喷注、$\pi^0$）** [C] · v1
  - **陈述.** Longitudinal double-spin asymmetries for jets and $\pi^0$ factorize with helicity PDFs.
  - **地位与缺口.** Inherits `conj:dy-coloured-final`.
  - `\uses{conj:dy-coloured-final, thm:dy-polarized}`

* **定理 `thm:dy-higher-twist` — $1/Q^2$ 处的广义因子化** [A] · v1
  - **陈述.** Leading power corrections are twist 4 and factorize in a generalized form (`QiuSterman1991a`, `QiuSterman1991b`); nuclear double scattering (`Kastella:1989ux`).
  - **非微扰地位.** \cref{asm:intro-bridge}（MA1、MA2）。
  - **地位与缺口.** All-order argument at twist 4; the Glauber analysis at subleading power is not carried out in App O.
  - `\uses{thm:dy-factorization, asm:intro-bridge}`

* **命题 `prop:dy-twist6-failure` — 更高幂次的因子化失效** [V] · v1
  - **陈述.** Factorization holds at $m^2/s$ but fails at $m^4/s^2$.
  - **地位与缺口.** Evidence: explicit perturbative counterexample in a scalar-quark model (`Basu:1984ba`); CSS 1989 §10.2: two-loop non-cancellation at $m^4/s^2$ in DY; BBL 1995 §VI: "Beyond that order, factorization is known to fail" (survey items 8, 21).
  - `\uses{thm:dy-higher-twist}`

**Worked examples.** `ex:dy-future-vs-past`, `ex:dy-spectator-lcopt`, `ex:dy-glauber-model`, `ex:dy-nlo`, `ex:dy-threshold`.

**Tables.**
- `tab:dy-status` (refdoc S34): rows = the App O steps (O-1) regions, domain and windows; (O-2) leading-power form in LCOPT; (O-3) cut sum and one-sided rewriting; (O-4) consistency of the subtraction terms with the rewriting; (O-5) deformation target; (O-6) eikonal approximation and past-pointing Wilson lines; (O-7) soft factor $=1$ and collinear factors; (O-8) interface with App N; columns: step | statement (label) | status | error type | assumptions | literature [SYNC-APP] [PENDING-VERIFY: X1].
- `tab:dy-correspondence` (refdoc S45.2): `lem:dy-fsi` ↔ `lem:appO-unitarity`; `prop:dy-deformation` ↔ `prop:appO-target`, `prop:appO-eikonal`, `prop:appO-past-wilson`; `lem:dy-poles-orientation` ↔ App O §O.3; `prop:dy-eikonal-twogluon` ↔ App O §O.8; `thm:dy-factorization` ↔ `thm:appO-main`, `cor:appO-interface`, `prop:appN-dy`.

**Figures.** Existing (tikz2): `fig:dy-oneloop`, `fig:glauber-exchange` (owned); `fig:reduced-dy` (owned by Ch4; refer back); new (required): `fig:dy-abelian-model` (adapt `research/c_dy/dy_oneloop.tex`, `fig:dy1l-glauber`), `fig:dy-pole-orientation`, `fig:dy-two-gluon-exchange` (refdoc S56).

**Misconception box.** M7 (Glauber cancels in every inclusive cross section), M25, **M30, M31, M32, M33**; "the soft factor is 1 for $q_T$-differential DY" (no: Ch14); critic C8, C11; O13, O14.

**Key citation keys.** `DrellYan1970`, `AltarelliEllisMartinelli1979`, `KubarAndrePaige1979`, `HambergVanNeervenMatsuura1991`, `Duhr:2020sdp`, `Moch:2005ky`, `MochVermaserenVogt2005`, `BodwinBrodskyLepage1981`, `Bodwin:1988fs`, `CollinsSoperSterman1983`, `Collins:1981tt`, `Collins:1983ju`, `Bodwin1985`, `CollinsSoperSterman1985b`, `CollinsSoperSterman1988`, `CollinsSoperSterman1989`, `Lindsay:1982pu`, `Lindsay:1982gd`, `Brandt:1988xt`, `Collins2011`, `Diehl:2015bca`, `AybatSterman2009`, `RothsteinStewart2016`, `Labastida:1984gy`, `Landshoff:1971zu`, `Henyey:1974zs`, `Cardy:1974vq`, `DeTar:1974vx`, `Collins:1985gm`, `NayakQiuSterman2005b`, `CataniDeFlorianRodrigo2012`, `Kang:2016mcy`, `NasonDawsonEllis1988`, `QiuSterman1991a`, `QiuSterman1991b`, `Kastella:1989ux`, `Basu:1984ba`, `BodwinBraatenLepage1995`, `Dawson1991`, `DjouadiSpiraZerwas1991`, `HarlanderKilgore2002`, `AnastasiouEtAl2015`, `BenekeBraun1995b`, `DoriaFrenkelTaylor1980`, `Frenkel:1983di`, `Catani:1985xt`, `Andrasi:1980qw`, `DiLietoEtAl1981`, `Cheng:1969eh`, `Korchemskaya:1994qp`, `Korchemsky:1993hr`, `Caron-Huot:2013fea`.

**Pending.** [PENDING-VERIFY: X1] (App O route, `tab:dy-status`, orientation lemma, future-vs-past identity, deformation plan); [N01, S63-5] (`prop:dy-eikonal-twogluon` marker); [N25] (model attribution); [E31, A11, S63-9] (attributions and RS equation numbers).

---------------------------------------------------------------------------------------------------

## Chapter 13 — 阈值重求和与重新因子化 / Threshold resummation and refactorization

`\label{ch:thr}` · `ch13_thr.tex` · **9 pp** · short format · Part III

**Purpose.** As $z=Q^2/\hat s\to1$ the hard coefficient itself refactorizes into hard × soft (× jet for DIS); Mellin-space exponentiation; the one-loop check against `prop:dy-nlo`; prescriptions (Landau pole); SCET momentum-space version; NLP status. Threshold factorization is nested inside the collinear one and its remainder is controlled by the outer one only at leading power in $(1-z)$ (refdoc S35). Pointer: the threshold factorization of the quasi-PDF matching kernel (Ch23).

**Depends on.** Ch5 (cusp), Ch10, Ch12; App A (Mellin table).

**Box.**
- 证明了：`prop:thr-oneloop`（[R, R_PT]，单圈检验）。
- 给出全阶论证：`thm:thr-refactorization`、`prop:thr-dis`（[A]）。
- 没有证明：次领头幂次的一般阈值因子化（`prop:thr-nlp`，[P]）；Landau 极点处方（处方不是定理，`rem:thr-prescriptions`）。

**Sections.** 1. `sec:thr-limit` 阈值极限与 Mellin 空间; 2. `sec:thr-refactorization` 重新因子化定理 (`fig:thr-kinematics`); 3. `sec:thr-check` 单圈检验; 4. `sec:thr-prescriptions` Landau 极点与处方 (`fig:thr-mellin`); 5. `sec:thr-nlp` 次领头幂次.

**Canonical statements** (in reading order).

* **定义 `def:thr-limit` — 部分子阈值与强子阈值** (no tag) · v1
  - **陈述.** Partonic threshold $z\to1$ ↔ $N\to\infty$; hadronic threshold $\tau\to1$ ($\tau=Q^2/s$ hadronic vs $z=Q^2/\hat s$ partonic — never mix); distinction (steep PDFs make partonic threshold logs relevant away from hadronic threshold — heuristic remark).
  - `\uses{def:dy-kin, def:prelim-mellin}`

* **定理 `thm:thr-refactorization` — DY 阈值重新因子化与指数化** [A] · v1 (+ refdoc S35)
  - **陈述.** At leading power in $(1-z)$: $\Delta_{q\bar q}=H(Q,\mu)\,Q\,S_{\rm DY}(Q(1-z),\mu)$ (distributions $\delta$, $\mathcal D_k$); in Mellin space, up to $N$-independent terms and $O(1/N)$: $$\ln\Delta_N=\int_0^1dz\,\frac{z^{N-1}-1}{1-z}\Big[2\int_{\mu_F^2}^{(1-z)^2Q^2}\frac{dq^2}{q^2}A(\alpha_s(q^2))+D(\alpha_s((1-z)^2Q^2))\Big],\qquad A=\frac{C_F\alpha_s}\pi+O(\alpha_s^2),\ D=O(\alpha_s^2)$$ (VF-THR-1; normalization of $A^{(1)}$ verified against the one-loop $8C_F\mathcal D_1$, critic c6). The towers are $\alpha_s^n[\ln^{2n-1}(1-z)/(1-z)]_+\leftrightarrow\alpha_s^n\ln^{2n}N$.
  - **证明.** Sketch (eikonal soft function with past-pointing Wilson lines; RG). Literature `Sterman1987`, `CataniTrentadue1989`, `Catani:1990rp`, `Korchemsky:1992xv`, `Contopanagos:1996nh`, `Kidonakis:1997gm`; SCET `Becher:2006nr`, `Becher:2007ty`. Survey item 25.
  - **地位与缺口.** (refdoc S35) Threshold factorization is nested inside `thm:dy-factorization`; its remainder is controlled by the outer theorem only at leading power in $(1-z)$; region completeness as $z\to1$ is an extra input; non-uniformity as $x\to1$ (pointer `prop:disall-two-routes`(c)). Inherits `thm:dy-factorization` ([A]).
  - `\uses{thm:dy-factorization, def:sudakov-cusp, prop:qcd-rge, def:thr-limit}`

* **命题 `prop:thr-oneloop` — 单圈检验** [R, R_PT] · v1
  - **陈述.** (One loop.) With $\langle\mathcal D_0,z^{N-1}\rangle=-S_1(N-1)\to-\ln\bar N$, $\langle\mathcal D_1,z^{N-1}\rangle=\frac12[S_1^2+S_2](N-1)\to\frac12(\ln^2\bar N+\zeta_2)$: the $O(\alpha_s)$ expansion of the exponent formula (as an explicit expression, VF-THR-1) reproduces the $\ln^2\bar N$ and $\ln\bar N$ terms of $\Delta_{q\bar q,N}=1+\frac{\alpha_s}{2\pi}C_F[4\ln^2\bar N+8\zeta_2-8]$ (at $\mu_F=Q$); the constant agrees with `Moch:2005ky` ($g_{01}^{\rm DY}=C_F(-16+16\zeta_2+8\gamma_E^2)$ in their normalization; c_dy §6.2) (VF-THR-2/3).
  - **证明.** Full.
  - `\uses{prop:dy-nlo, lem:prelim-mellin, lem:appA-mellin-table, def:thr-limit}`

* **注 `rem:thr-prescriptions` — Landau 极点与处方** (no tag) · v1
  - The $q^2$ integral hits the Landau pole; prescriptions (minimal prescription `CataniEtAl1996`) are prescriptions, not theorems; partonic vs hadronic threshold.

* **命题 `prop:thr-dis` — DIS 的大 $x$ 重新因子化** [A] · v1
  - **陈述.** $C_2^q\to H\cdot J\otimes S$ as $x\to1$ (`Sterman1987`, `BecherNeubertPecjak2007`).
  - **地位与缺口.** Nested inside `thm:disall-factorization`; non-uniformity of the outer remainder as $x\to1$ (`prop:disall-two-routes`(c)).
  - `\uses{thm:disall-factorization, def:thr-limit}`

* **命题 `prop:thr-nlp` — 次领头幂次的阈值对数** [P] · v1
  - **陈述.** LL resummation at NLP for DY (`Beneke:2018gvs`) and Higgs (`Beneke:2019mua`); endpoint factorization case by case (`Beneke:2022obx`, NLP DIS `Beneke:2026miy`, preprint).
  - **地位与缺口.** Established at LL and for specific processes; no general NLP threshold factorization theorem; endpoint divergences (pointer `prop:power-nlp-endpoint`, Ch21; Ch24 for the frontier status).
  - `\uses{thm:thr-refactorization}`

* **例 `ex:thr-dy` — 指数的 $O(\alpha_s)$ 展开与 `prop:dy-nlo` 的 Mellin 变换** (no tag) · v1
  - = `prop:thr-oneloop` with all steps (≈1.5 pp).
  - `\uses{prop:thr-oneloop}`

**Worked example.** `ex:thr-dy`.

**Figures.** New (required): `fig:thr-kinematics`, `fig:thr-mellin`.

**Misconception box.** 「处方是定理」 (prescriptions are not theorems).

**Key citation keys.** `Sterman1987`, `CataniTrentadue1989`, `Catani:1990rp`, `Korchemsky:1992xv`, `Contopanagos:1996nh`, `Kidonakis:1997gm`, `CataniEtAl1996`, `Becher:2006nr`, `BecherNeubertPecjak2007`, `Becher:2007ty`, `Moch:2005ky`, `Beneke:2018gvs`, `Beneke:2019mua`, `Beneke:2022obx`, `Beneke:2026miy`, `Liu:2019oav`.

**Pending.** None specific.

---------------------------------------------------------------------------------------------------

# 第四部分 共线之外 (Part IV — Beyond collinear factorization)

---------------------------------------------------------------------------------------------------

## Chapter 14 — 横动量依赖（TMD）因子化 / TMD factorization

`\label{ch:tmd}` · `ch14_tmd.tex` · **16 pp** · full (precise forms in App N, App O) · Part IV

**Purpose.** At small $q_T$ the soft factor no longer cancels; the collinear subgraphs keep their transverse momenta; light-like Wilson lines produce rapidity divergences; whether a Wilson line points to the future or the past becomes physical. The chapter gives: the definitions (staple-shaped Wilson lines, soft factor, Collins' combination) with the **exact square-root identity** and the order of limits; the statement "zero-bin = soft factor" (refdoc S36); the factorization theorem and its status (W+Y caveat); Collins–Soper (CS) and RG evolution with one-loop checks; the small-$b$ OPE and the CSS solution; process dependence (the Sivers sign as an operator identity via the PT route vs the observable sign reversal; universality of the Collins function); matching to twist-3 collinear factorization; $\int d^2k_T f\ne f$. Universality is derived from the operator definitions, never assumed (C9); only the properly combined objects are regulator independent (C10). Pointers: lattice CS kernel (Ch22), quasi-TMD factorization and Euclidean soft functions (Ch23).

**Depends on.** Ch5 (`prop:sudakov-kg`, `def:sudakov-cusp`, `prop:sudakov-oneloop`), Ch8 (`def:pdf-quark`, `thm:pdf-dglap`), Ch9 (`thm:method-template` with (H4) soft factor $\ne1$, `prop:method-glauber-oneloop`, `def:method-subtraction`), Ch12 (`lem:dy-fsi`, `prop:dy-abelian-model`, `thm:dy-factorization`; `prop:dy-universality` by contrast); App N, App O [SYNC-APP].

**Source status.** `research/c_tmd/DERIVATION.md` (17/17 scripts pass; results R1–R12 cross-checked against Aybat–Rogers 2011, EIS 2012, Collins–Rogers 2013, Balázs–Yuan 1997, Bacchetta–Conti–Radici 2008); all c_tmd numbers are verified (VF-TMD-1…10). Chinese drafts `research/c_tmd/tex/tmd_{definitions,oneloop,evolution,sivers}.tex`.

**Box.**
- 证明了：`lem:tmd-soft-oneloop`、`prop:tmd-evolution-oneloop`（[R, R_PT]，单圈）；`lem:tmd-sqrt-identity`、`thm:tmd-sivers-sign`（[R, R_def]）；`prop:tmd-zero-bin-soft`（[R, R_cond]，前提 `asm:appN-ward-product`、`asm:appN-tmd`；(a) 单圈无条件）。
- 给出全阶论证：`prop:tmd-regions`、`lem:tmd-glauber`、`prop:tmd-h1h5`、`thm:tmd-factorization`、`prop:tmd-evolution`、`prop:tmd-css`、`prop:tmd-small-b`、`cor:tmd-sivers-observable`、`prop:tmd-collins-universality`（[A]；瓶颈 `asm:appN-tmd`、`asm:appO-rewritten-cs`、`asm:appO-mixing`）。
- 没有证明：快度方案的全阶等价（只逐阶验证）；大 $b_T$ 区（非微扰）；$W+Y$ 在 $q_T\sim Q$ 与 $q_T\sim\Lambda$ 处的一致性（需修正的截断）；与扭度 3 的全阶匹配（`prop:tmd-twist3-matching`，[P]）。

**Sections.**
1. `sec:tmd-kinematics` 小横动量：运动学与 Sudakov 对数.
2. `sec:tmd-regions` 领头区域：软区（非超软）、快度与 Glauber 区.
3. `sec:tmd-definitions` 定义：订书钉形 Wilson 线、软因子、平方根恒等式与 Collins 定义 (`fig:tmd-staple`, `fig:tmd-soft-factor`; optional `fig:tmd-rapidity-bars`).
4. `sec:tmd-subtraction` 零箱减除即软因子；快度窗口 — **new section** (refdoc S36).
5. `sec:tmd-theorem` 因子化定理 (`fig:tmd-dy`).
6. `sec:tmd-evolution` Collins–Soper 方程与重整化群演化 (optional `fig:tmd-evolution`).
7. `sec:tmd-small-b` 小 $b$ 展开与 CSS 解.
8. `sec:tmd-universality` 过程依赖：Sivers 符号与 Collins 函数 (`fig:sidis-dy-links`; at the first reference add that in a single cut graph the line is future-pointing and the past-pointing form appears only after the cut sum and one-sided rewriting, `ex:dy-future-vs-past`, M33).
9. `sec:tmd-twist3` 与扭度 3 共线因子化的匹配；$k_T$ 积分.
10. Closing: `tab:tmd-correspondence` (chapter statement | App N / App O version | difference).

**Canonical statements** (in reading order).

* **定义 `def:tmd-kin` — 小 $q_T$ 区域** (no tag) · v1
  - **陈述.** Processes: DY $A+B\to\gamma^*(q)+X$ with $q_T\ll Q$; SIDIS with $P_{hT}/z\ll Q$; $e^+e^-\to h_1h_2X$ (nearly back to back). At $O(\alpha_s)$ the cross section behaves like $\frac{\alpha_s}{q_T^2}[c_1\ln\frac{Q^2}{q_T^2}+c_0]$. In CSS normalization (expansion parameter $\alpha_s/\pi$, $C_1=b_0$, $C_2=1$): $A^{(1)}=C_F$, $B^{(1)}=-\frac32C_F$. Check: the $O(\alpha_s)$ CSS expansion reproduces the exact small-$q_T$ asymptotics of the fixed-order $q\bar q$ and $qg$ channels (ratio $\to1$ as $q_T/Q\to0$; with $B^{(1)}=0$ the ratio at $q_T/Q=10^{-3}$ would be $0.896$) (c_tmd [R11]; VF-TMD-7, VF-TMD-10).
  - `\uses{def:dy-kin}`

* **命题 `prop:tmd-regions` — 小 $q_T$ 的领头区域** [A] · v1
  - **陈述.** The leading regions are: $H$; $J_A$ and $J_B$ with $k_T\sim q_T$; a **soft** subgraph with all components of $k$ of order $q_T$ (not the ultrasoft scaling of `def:ir-scalings`; soft and collinear regions are separated only in rapidity, the origin of rapidity divergences when the Wilson lines are light-like); Glauber exchanges.
  - **证明.** Sketch (`prop:ir-power-counting` with the soft scaling; `thm:ir-leading-regions`). Literature: Collins 2011 ch. 10 and ch. 13 (section numbers to be verified, S63-9); `CollinsSoper1981`.
  - **地位与缺口.** E-S; `asm:appN-envelope`, `asm:appN-separation`.
  - `\uses{thm:ir-leading-regions, prop:ir-power-counting, def:tmd-kin}`

* **定义 `def:tmd-unsub` — 未减除的 TMD 关联函数** (no tag) · v1
  - **陈述.** The Fourier convention is CONTEXT's, $\tilde f(x,b_T)=\int d^{2-2\varepsilon}k_T\,e^{-ik_T\cdot b_T}f(x,k_T)$; $\tilde f^{\rm unsub}(x,b_T)=\int\frac{dw^-}{4\pi}e^{-ixP^+w^-}\langle P|\bar\psi(w)\gamma^+\,\mathcal W_{\rm staple}[w,0]\,\psi(0)|P\rangle_c$ with $w=(0^+,w^-,b_T)$ (follows from $f(x,k_T)=\int\frac{dw^-d^2w_T}{16\pi^3}e^{-ixP^+w^-+ik_T\cdot w_T}\langle\cdots\rangle$; sign chain agrees with c_tmd §2.1 and Aybat–Rogers 2011 eqs. (11), (27); VF-CONV-11). The staple runs from $w$ to $w\pm\infty n$, then along a transverse link at infinity (`BelitskyJiYuan2003`; needed in non-covariant gauges), then back to $0$; future pointing for SIDIS, past pointing for DY. A light-like $n$ gives rapidity divergences; Collins uses a non-light-like, **space-like** $n(y_B)$ with $y_B\to-\infty$ taken at the end (VF-TMD-9: with time-like past-pointing lines the PT argument of `thm:tmd-sivers-sign` fails at finite rapidity). Tree level: $\tilde f^{\rm unsub}(x,b_T\to0)=f(x)$. Transcription of Collins 2011's definition into the binding conventions (Collins uses $g\to-g$; his eq. (13.35) uses $e^{+ik_T\cdot b_T}$ for the soft factor and the TMD FFs): check the sign at each transcription (VF-CONV-11).
  - `\uses{def:prelim-wilson, def:pdf-quark}`

* **定义 `def:tmd-soft` — 软因子** (no tag) · v1
  - **陈述.** $\tilde S(b_T;y_A,y_B)=\frac1{N_c}\langle0|{\rm Tr}\,\mathcal W(b_T/2;\infty,n(y_B))^\dagger\cdots\mathcal W(-b_T/2;\infty,n(y_A))|0\rangle$, with non-light-like Wilson lines of rapidities $y_A,y_B$ (operator ordering and staple geometry as in Collins 2011, equation number to be verified, S63-9); $\tilde S$ depends only on $y_A-y_B$ (boost invariance, exact). DY and SIDIS soft factors are equal by T invariance (`lem:dy-soft`).
  - `\uses{def:prelim-wilson}`

* **引理 `lem:tmd-soft-oneloop` — 单圈软因子** [R, R_PT] · v1 (+ VF-REF-19)
  - **陈述.** (One loop.) (a) Large rapidity separation: $\tilde S(b_T;y_A,y_B)=1+\tilde K(b_T;\mu)(y_A-y_B)+O(\alpha_s^2)+O((y_A-y_B)^0\alpha_s)$, $\tilde K=-\frac{\alpha_sC_F}\pi\ln\frac{\mu^2b_T^2}{b_0^2}$ (VF-TMD-1). (b) Exact one-loop rapidity dependence $\propto(Y\coth Y-\sigma)$, $Y=y_A-y_B$, with $\sigma=1$ for time-like lines (self-energies included) and $\sigma=0$ for space-like lines; the time-like and the space-like (principal-value) rapidity integrals both give $4(Y\coth Y-\sigma)$ (c_tmd [R4]; VF-TMD-8); for $\sigma=1$ the pole is two cusps with the anomalous dimension of `def:sudakov-cusp`. (c) Space-like Wilson-line self-energies are non-integrable: $n_A(y_A)\cdot k=-\sqrt2|\mathbf k_T|e^{-y_A}\sinh(y_k-y_A)$ vanishes inside the real-gluon phase space, giving a $1/\sinh^2$ double pole (length divergence) (VF-REF-19); any self-energy constant cancels identically in the TMD combination, so self-energies must be excluded or defined by one convention in $\tilde f^{\rm unsub}$ and $\tilde S$ (the time-like vs space-like difference $2\pi^2$ is an illustration, N20 [PENDING-VERIFY: N20]). (d) Higher orders: non-abelian exponentiation (webs), `Gatheral1983`, `FrenkelTaylor1984`.
  - **证明.** Full at one loop (App G `sec:appG-tmd`).
  - `\uses{def:tmd-soft, prop:prelim-wilson-rules, def:sudakov-cusp}`

* **引理 `lem:tmd-sqrt-identity` — 平方根构造是恒等式** [R, R_def] · refdoc S36 (composite) [PENDING-VERIFY: X2 for (b)]
  - **陈述.** (a) With $\tilde f_A\equiv\tilde f_A^{\rm unsub}(y_B)\sqrt{\tilde S(y_A,y_n)/[\tilde S(y_A,y_B)\tilde S(y_n,y_B)]}$ and $\tilde f_B$ alike, $\tilde f_A\tilde f_B=\tilde f_A^{\rm unsub}\tilde f_B^{\rm unsub}/\tilde S(y_A,y_B)$ exactly, independent of $y_n$ (VF-REF-13). (b)（蕴含关系，\tagR，$R_{\rm cond}$，前提 `asm:appN-tmd`(T2)）The limits $y_A\to+\infty$, $y_B\to-\infty$ exist and $\partial\ln\tilde f_A/\partial y_n=-\tilde K$, which is the CS equation; "$\tilde S$ depends only on $y_1-y_2$" is exact (boost invariance), asymptotic linearity of $\ln\tilde S$ and $\ln\tilde f^{\rm unsub}$ with equal slope is dynamical.
  - **证明.** (a) Full (algebra); (b) full given (T2) (App N §N.5).
  - `\uses{def:tmd-unsub, def:tmd-soft}`

* **定义 `def:tmd-collins` — Collins 的 TMD 定义** (no tag) · v1
  - **陈述.** $$\tilde f(x,b_T;\mu,\zeta)=\lim_{y_B\to-\infty}\tilde f^{\rm unsub}(x,b_T;y_P-y_B)\sqrt{\frac{\tilde S(b_T;+\infty,y_n)}{\tilde S(b_T;+\infty,y_B)\,\tilde S(b_T;y_n,y_B)}}\times Z_{\rm UV},\qquad \zeta=M^2x^2e^{2(y_P-y_n)}.$$ Rapidity divergences cancel between the unsubtracted correlator and the soft factors (`lem:tmd-sqrt-identity`); only the combination is regulator independent (C10). In the cross section $\zeta_A\zeta_B=Q^4$ (binding). Normalization $\zeta=M^2x^2e^{2(y_P-y_n)}=2(xP^+)^2e^{-2y_n}$; do not copy Aybat–Rogers eq. (3), which has a spurious factor 2 (VF-TMD-9) [PENDING-VERIFY: E17 — App Q candidate]. **Order of limits** (print): light-like limit $y_B\to-\infty$ first at fixed $\varepsilon$, then $\overline{\rm MS}$ renormalization, then $\varepsilon\to0$ (VF-TMD-9). One loop: $Z_{\rm UV}=Z_FZ_2=1+aS_\varepsilon[-\frac1{\varepsilon^2}+\frac{l_\zeta-3/2}\varepsilon]$, $a=\frac{\alpha_sC_F}{2\pi}$ (VF-TMD-4).
  - `\uses{def:tmd-unsub, def:tmd-soft, lem:tmd-sqrt-identity}`

* **注 `rem:tmd-schemes` — 其他方案** (no tag) · v1
  - Ji–Ma–Yuan (`JiMaYuan2005`, `Ji:2004xq`, `Ji:2005nu`); the $\delta$ regulator (`EchevarriaIdilbiScimemi2012`, `Echevarria:2012js`); the rapidity RG (`ChiuEtAl2012a`, `ChiuEtAl2012b`); the collinear anomaly (`BecherNeubert2011`). Relations: `Collins:2017oxh`; their equivalence is [A], shown explicitly at low orders; the rapidity anomalous dimension is known to four loops (`Duhr:2022yyp`, `Moult:2022xzt`; literature). $\delta$-regulator check (c_tmd [R9]): the combination gives $\ln(\zeta/k_T^2)$ with $\zeta=2(p^+)^2\delta^-/\delta^+$ (= Collins–Rogers 2013 eq. (zetaA)). Euclidean (off-light-cone) realizations of the soft factor: Ch23 (pointer).

* **注 `rem:tmd-scheme-constants` — 方案常数（$S_\varepsilon$ 约定）** (no tag) · v1
  - (c_tmd [R8], [R10]; VF-TMD-3/5; units $\frac{\alpha_sC_F}{2\pi}$.) Small-$b$ coefficient at $\mu=\mu_b$, $\zeta=\mu_b^2$: the $\delta(1-x)$ constant of $\tilde C_{q/q}$ is $-\frac{\pi^2}{12}$ with the binding $S_\varepsilon$, $0$ with Collins' $S_\varepsilon$; hard factor $-8+\frac{7\pi^2}6$ (binding) vs $-8+\pi^2$ (Collins); $\mathcal H^{\rm bind}-\mathcal H^{\rm Coll}=\frac{\pi^2}6$ and $2[\tilde C^{\rm bind}-\tilde C^{\rm Coll}]=-\frac{\pi^2}6$, so the cross section is unchanged; the CSS coefficient $C^{(1)}_{qq}=\frac{\alpha_s}\pi[\frac{C_F}2(1-z)+C_F(\frac{\pi^2}4-2)\delta(1-z)]$ is the same in both. **Writer rule:** use the binding $S_\varepsilon$; when quoting Collins' constants, convert and say so.

* **注 `rem:tmd-order-of-limits` — 极限次序** (no tag) · refdoc S36 (D20)
  - At fixed $x$, the rapidity-regularized collinear factor differs from the light-front matrix element by $e^{2(y_B-y_k)}$, which is not small near $y_B$; taking $y_B\to-\infty$ under the integral is `asm:appN-tmd`(T4).

* **命题 `prop:tmd-zero-bin-soft` — 零箱减除即软因子** [R, R_cond] · refdoc S36 [PENDING-VERIFY: X2] (composite)
  - **陈述.** 前提：\cref{asm:appN-ward-product}、\cref{asm:appN-tmd}。(a) (One loop, unconditional; stated in words, 「（单圈，\tagR，$R_{\rm PT}$）」) $T_RT_{R'}=T_{R'}$ when the $B$ lines carry only the on-shell external momentum and the soft momenta — exact for $p_B^+=0$, relative $O(e^{-2Y}p_B^+/p_B^-)$ otherwise; hence $C_A\Gamma=T_A\Gamma-T_S\Gamma$, which after the Ward identity equals $\mathsf H^{(0)}[\tilde f_A^{{\rm unsub}(1)}(y_B)-\tilde S^{(1)}(y_A,y_B)]$. (b) All orders: $\sum_{\rm graphs}\sum_R\int C_R\Gamma=\big[\mathsf H\,\tilde f_A^{\rm unsub}(y_B)\tilde f_B^{\rm unsub}(y_A)/\tilde S(y_A,y_B)\big]^{[N]}$ as formal power series.
  - **证明.** Full for (a); (b) by induction (App N §N.5). One-loop check: c_tmd.
  - `\uses{def:tmd-collins, def:method-subtraction, lem:tmd-soft-oneloop, asm:appN-ward-product, asm:appN-tmd}`

* **注 `rem:tmd-rapidity-window` — 快度窗口** (no tag) · refdoc S36
  - The subtraction theorem holds for rapidity cutoffs $c_0L\le Y\le c_1L$, with constants polynomial in $Y$; $Y\to\infty$ is taken only after summing regions and organizing by `prop:tmd-zero-bin-soft` and `lem:tmd-sqrt-identity`; integral norms take absolute values, so the oscillation $e^{i\mathbf b_T\cdot\mathbf k_T}$ does not help.

* **引理 `lem:tmd-glauber` — TMD DY、SIDIS、$e^+e^-$ 中的 Glauber 相消** [A] · v1 (+ refdoc S36) [PENDING-VERIFY: X1]
  - **陈述.** **DY.** The spectator–spectator phase cancels after the integration over the spectators' *relative* transverse momentum $\Delta$ at fixed $q_T$; in the abelian model this is exact: $\int d^2\Delta\,2{\rm Re}[\mathcal M^{(1)}\mathcal M^{(0)*}]=0$, with the phase $e^{i\chi(b)}$, $\chi=-\frac{e_Ae_B}{2\pi}K_0(m_gb)$ (c_glauber §1.5 Steps 3–4; VF-GLA-2/3); precise form `prop:appO-tmd` [R, R_cond] with the measurement operator $e^{i\mathbf b\cdot\hat{\mathbf P}_T}$, $\sum_X|X\rangle e^{i\mathbf b\cdot\mathbf P_{XT}}\langle X|=e^{i\mathbf b\cdot\hat{\mathbf P}_T}$, which commutes with light-cone evolution and with the $\tau=0$ insertions. **SIDIS.** One incoming hadron: only final-state poles. **$e^+e^-$.** All collinear lines outgoing. Contrast: $h_1h_2\to H_1H_2X$ (`thm:break-tmd`, Ch18).
  - **证明.** Sketch; `CollinsSoperSterman1985a`, Collins 2011 ch. 14, `JiMaYuan2005`, `RothsteinStewart2016` (eqs. (11.12)–(11.13), as read by c_glauber).
  - **地位与缺口.** [A]: `asm:appO-mixing`, `asm:appO-deformation`, `asm:appO-rewritten-cs` (substantive for TMD: the Wilson-line prescription of localized spectator terms).
  - `\uses{lem:dy-fsi, prop:appO-tmd, asm:appO-mixing, asm:appO-deformation, asm:appO-rewritten-cs}`

* **命题 `prop:tmd-h1h5` — 小 $q_T$ DY 对模板假设的验证** [A] · v1 (+ refdoc S36)
  - **陈述.** Each hypothesis of `thm:method-template` holds in the following form: (H2) collinear subgraphs at fixed $k^+$ **and** $k_T$; (H3) Glauber cancellation (`lem:tmd-glauber` + App O); (H4) the soft factor is $\tilde S(b_T)$, not 1; (H5) the subtractions, including the soft–collinear overlaps, reproduce the operator definitions (`prop:tmd-zero-bin-soft`, `lem:tmd-sqrt-identity`).
  - **证明.** Sketch.
  - **地位与缺口.** `asm:appN-tmd`, `asm:appN-ward-product`, `asm:appO-*`.
  - `\uses{thm:method-template, prop:tmd-regions, lem:tmd-glauber, prop:tmd-zero-bin-soft, lem:tmd-sqrt-identity}`

* **定理 `thm:tmd-factorization` — Drell–Yan 的 TMD 因子化** [A] · v1 (+ refdoc S36)
  - **陈述.** $$\frac{d\sigma}{dQ^2\,dy\,d^2q_T}=\frac{\sigma_0}{s}\sum_qe_q^2\,\mathcal H(Q;\mu)\int\!\frac{d^2b_T}{(2\pi)^2}e^{iq_T\cdot b_T}\tilde f_{q/A}(x_A,b_T;\mu,\zeta_A)\tilde f_{\bar q/B}(x_B,b_T;\mu,\zeta_B)+(q\leftrightarrow\bar q)+Y(q_T,Q)+O\Big(\Big(\frac{m}{Q}\Big)^p\Big),$$ with $\zeta_A\zeta_B=Q^4$ and $\sigma_0=\frac{4\pi\alpha^2}{3N_cQ^2}$ (WRITER_SPEC_v2 §3 row 33), so that $\int d^2q_T$ at tree level returns `prop:dy-born` (VF-DY-1); $Y$ is the large-$q_T$ matching term; the Fourier form follows from $\delta^2(q_T-k_{AT}-k_{BT})=\int\frac{d^2b}{(2\pi)^2}e^{i(q_T-k_{AT}-k_{BT})\cdot b}$. Analogues: SIDIS (future-pointing TMD PDF ⊗ TMD FF) and $e^+e^-\to h_1h_2X$ (two TMD FFs).
  - **非微扰地位.** \cref{asm:intro-bridge}（MA1、MA2、MA4）。
  - **证明.** `proofsketch` in which the deduction from `prop:tmd-regions`–`prop:tmd-h1h5` and `thm:method-template` is written out completely (WRITER_SPEC_v2 §4.10).
  - **地位与缺口.** Literature: `CollinsSoper1981`, `CollinsSoperSterman1985a`, `JiMaYuan2005`, `Ji:2004xq`; Collins 2011 ch. 13–14 (§14.4.5, §14.5). DY inherits the Glauber argument of Ch12; the SCET derivations drop the Glauber Lagrangian after arguments (survey item 10); the equivalence of rapidity schemes is shown order by order only (`Collins:2017oxh`); the $W+Y$ matching is not uniform near $q_T\sim Q$ and $q_T\sim\Lambda$ without modified cutoffs (`Collins:2016hqq`) [PENDING-VERIFY: S63-6]; bottlenecks by label: `asm:appN-tmd`, `asm:appN-collins`, `asm:appO-rewritten-cs`, `asm:appO-mixing`, `asm:intro-bridge`; quasi-TMD factorization (Ch23) uses this theorem as an [A] input.
  - `\uses{prop:tmd-h1h5, prop:tmd-regions, lem:tmd-soft-oneloop, lem:tmd-glauber, def:tmd-collins, thm:method-template, thm:dy-factorization, asm:intro-bridge, asm:appN-tmd, asm:appN-collins, asm:appO-rewritten-cs, asm:appO-mixing}`

* **命题 `prop:tmd-evolution` — Collins–Soper 方程与重整化群方程** [A] · v1 (+ refdoc S36)
  - **陈述.** $$\frac{\partial\ln\tilde f}{\partial\ln\sqrt\zeta}=\tilde K(b_T;\mu),\qquad\frac{d\tilde K}{d\ln\mu}=-\gamma_K(\alpha_s),\qquad\frac{d\ln\tilde f}{d\ln\mu}=\gamma_q(\alpha_s;1)-\tfrac12\gamma_K(\alpha_s)\ln\frac{\zeta}{\mu^2}.$$
  - **证明.** Sketch; compact CS derivation $\frac12[\ln\tilde S(+\infty,y_n)-\ln\tilde S(+\infty,y_B)-\ln\tilde S(y_n,y_B)]$ with asymptotic linearity, via `lem:tmd-sqrt-identity` (refdoc T22).
  - **地位与缺口.** Rests on the multiplicative renormalizability of the combined TMD operator in $b$ space (`asm:appN-tmd`(T3)), argued, not proven (Collins 2011 ch. 13); M17: $\tilde K$ is perturbative only for $b_T\ll1/\Lambda$ (lattice determinations: `prop:lattice-cs-kernel`, Ch22, pointer).
  - `\uses{def:tmd-collins, lem:tmd-sqrt-identity, asm:appN-tmd}`

* **命题 `prop:tmd-evolution-oneloop` — 单圈演化系数与硬因子的 RG 相容性** [R, R_PT] · v1
  - **陈述.** (One loop.) $\tilde K=-\frac{\alpha_sC_F}\pi\ln\frac{\mu^2b_T^2}{b_0^2}$ and $\gamma_K=\frac{2\alpha_sC_F}\pi$ (VF-TMD-1/2); $\gamma_q(\alpha_s;1)=\frac32\frac{\alpha_sC_F}\pi$ (c_tmd [R7]: $\gamma_F=\frac{\alpha_sC_F}\pi(\frac32-l_\zeta)$; VF-TMD-4); $\mathcal H=1+\frac{\alpha_sC_F}{2\pi}[-L^2+3L-8+\frac{7\pi^2}6]$, $L=\ln\frac{Q^2}{\mu^2}$ (VF-TMD-3 = VF-SCET-8), obeying $\frac{d\ln\mathcal H}{d\ln\mu}=\frac{\alpha_sC_F}\pi(2L-3)$, which cancels $2\gamma_q-\frac12\gamma_K\ln\frac{\zeta_A\zeta_B}{\mu^4}=\frac{\alpha_sC_F}\pi(3-2L)$.
  - **证明.** Full at one loop (`ex:tmd-oneloop`, which follows as the worked computation; App G).
  - `\uses{lem:tmd-soft-oneloop, def:tmd-collins, prop:sudakov-oneloop}`

* **命题 `prop:tmd-small-b` — 小 $b$ 展开** [A] · v1
  - **陈述.** $\tilde f_{q/H}(x,b_T;\mu,\zeta)=\sum_j\int_x^1\frac{d\xi}\xi\tilde C_{q/j}(\frac x\xi,b_T;\mu,\zeta)f_{j/H}(\xi;\mu)+O((mb_T)^p)$, $p>0$ ($p=2$ expected for unpolarized leading-twist TMDs — [PENDING-VERIFY: S63-7]). One-loop coefficients at $\mu=\mu_b$, $\zeta=\mu_b^2$ with the binding $S_\varepsilon$ (c_tmd [R8]; VF-TMD-5/6): $\tilde C_{q/q}=\delta(1-x)+\frac{\alpha_sC_F}{2\pi}\big[(1-x)-\frac{\pi^2}{12}\delta(1-x)\big]$; $\tilde C_{q/g}=\frac{\alpha_sT_F}{2\pi}2x(1-x)$ (its pole $-\frac1\varepsilon P_{qg}/T_F$ is IR and matches the PDF); in Collins' $S_\varepsilon$ the $\pi^2$ term is absent (equals `AybatRogers2011` (A11)); the binding value equals EIS 2012.
  - **非微扰地位.** \cref{asm:intro-composite}、\cref{asm:intro-bridge}（MA0、MA4）。
  - **地位与缺口.** An OPE-type statement for light-cone bilocal operators with transverse separation; all-order argument (Collins 2011 ch. 13); the remainder power is not proven in general.
  - `\uses{def:tmd-collins, thm:pdf-dglap, asm:intro-composite, asm:intro-bridge}`

* **命题 `prop:tmd-css` — CSS 解与非微扰输入** [A] · v1
  - **陈述.** (Solution formula.) The solution is evaluated with $\mu_b=b_0/b_*$, $b_*=b_T/\sqrt{1+b_T^2/b_{\max}^2}$, and the non-perturbative functions $g_K(b_T)$, $g_{j/H}(x,b_T)$ (`CollinsSoperSterman1985a`; Collins 2011 ch. 13); antecedents `ParisiPetronzio1979`, `DokshitzerDiakonovTroian1978`.
  - **地位与缺口.** The large-$b_T$ region is non-perturbative; it is fitted, or computed on the lattice for $\tilde K$ (`prop:lattice-cs-kernel`, Ch22, pointer); the choice of prescription is a model ingredient (M17).
  - `\uses{prop:tmd-evolution, prop:tmd-small-b}`

* **定理 `thm:tmd-sivers-sign` — Sivers 函数的符号反转（算符层面）** [R, R_def] · v1 (proof route refdoc S36)
  - **陈述.** For the operator-defined Sivers function (Trento convention, `BacchettaEtAl2004`), with space-like or light-like Wilson lines (VF-TMD-9): $$f_{1T}^{\perp q}(x,k_T)\big|_{\rm SIDIS}=-f_{1T}^{\perp q}(x,k_T)\big|_{\rm DY};$$ the unpolarized TMD obeys $f_1^{[+]}=f_1^{[-]}$.
  - **非微扰地位.** \cref{asm:intro-wightman}、\cref{asm:intro-composite}（MA0：强子矩阵元的存在）。
  - **证明.** Full, **via PT** (exact for any $\theta$: the $\theta$ term is C-even, plus CPT; refdoc T23): no Hermitian conjugation is needed; $t^a\to t^{a*}$ reverses the path ordering; $\epsilon_T^{12}=+1$ (Trento). PT maps the future-pointing staple to the past-pointing one; the Sivers structure $\epsilon_T^{ij}k_T^iS_T^j$ is T-odd. One-gluon illustration: $\frac1{k^++i0}-\frac1{k^+-i0}=-2\pi i\delta(k^+)$ (VF-WL-12). Spectator-model check (c_tmd [R12]; VF-TMD-8; = Bacchetta–Conti–Radici 2008): ratio DY/SIDIS $=-1$, $f_{1T}^\perp|_{\rm SIDIS}<0$ for an attractive final-state interaction. Literature: `Collins2002` (correcting the T-invariance argument of `Collins1993`, history only), `BrodskyHwangSchmidt2002`, `JiYuan2002`, `BelitskyJiYuan2003`, Collins 2011 §13.17.
  - `\uses{def:tmd-unsub, def:tmd-collins, asm:intro-wightman, asm:intro-composite}`

* **推论 `cor:tmd-sivers-observable` — 可观测不对称的符号反转** [A] · v1
  - **陈述.** The single-spin asymmetries measured in SIDIS and DY have opposite signs at leading power.
  - **非微扰地位.** \cref{asm:intro-bridge}（MA1、MA2）。
  - **地位与缺口.** Requires `thm:tmd-factorization` for both processes; experiment consistent but not decisive (`COMPASS:2017jbv`, `COMPASS:2023vqt`, `STAR:2015vmv`, `STAR:2023jwh`; `Bury:2020vhj` fits "cannot exclude the same sign"); SIDIS data `HERMES:2009lmz`, `HERMES:2020ifk`; global analysis `Echevarria:2020hpy`.
  - `\uses{thm:tmd-sivers-sign, thm:tmd-factorization, asm:intro-bridge}`

* **命题 `prop:tmd-collins-universality` — T-奇碎裂函数的普适性** [A] · v1
  - **陈述.** The Collins function (`Collins1993`) is the same in SIDIS and $e^+e^-$; there is no sign change (`CollinsMetz2004`, `MeissnerMetz2009`). (M13)
  - **非微扰地位.** \cref{asm:intro-bridge}（MA1、MA2）。
  - **地位与缺口.** Inherits `thm:tmd-factorization`.
  - `\uses{thm:tmd-factorization, asm:intro-bridge}`

* **定义 `def:tmd-etqs` — Qiu–Sterman (ETQS) 关联函数** (no tag) · v1
  - **陈述.** $T_F(x_1,x_2)$ is a quark–gluon–quark light-cone correlator with $\epsilon^{S_T\sigma n_An_B}$ structure; its gluonic-pole value is $T_F(x,x)$ (`EfremovTeryaev1985`, `Efremov:1981sh`, `QiuSterman1991c`). Ch21 uses it for twist-3 factorization.
  - `\uses{def:pdf-quark}`

* **命题 `prop:tmd-twist3-matching` — 与扭度 3 共线因子化的匹配** [P] · v1
  - **陈述.** For $\Lambda\ll q_T\ll Q$ the TMD and twist-3 (ETQS) descriptions of single-spin asymmetries agree at one loop (`Ji:2006ub`); the first $k_T$-moment of the Sivers function is related to $T_F(x,x)$ by a convention-dependent factor (`Boer:2003cm`; verify); evolution of $T_F$: the dispute between `Braun:2009mi` and `Kang:2008ey` is resolved; NLO SSA in DY: `Vogelsang:2009pj`; the "sign mismatch": `Kang:2011hk`, addressed by `Cammarota:2020qcw`.
  - **地位与缺口.** Established at one loop / NLO in specific processes; no all-order matching theorem.
  - `\uses{def:tmd-etqs, thm:tmd-factorization}`

* **注 `rem:tmd-kt-integral` — $\int d^2k_T\,f\ne f$** (no tag) · v1
  - Beyond tree level the $k_T$ integral of the renormalized TMD diverges in the UV (tail $\sim\alpha_s/k_T^2$); the relation to $f(x;\mu)$ holds only with a cutoff, up to scheme-dependent terms and power corrections (`EbertMichelStewartSun2022`). (M14)

* **例 `ex:tmd-oneloop` — 单圈全过程** (no tag) · v1 (+ refdoc S36, T21)
  - First step (refdoc T21): the rapidity divergence of the unintegrated Wilson-line graphs, $\frac{\alpha_sC_F}{\pi^2}\frac{\xi}{(1-\xi)k_T^2}$, read as double counting with the other hadron; then the unsubtracted TMD with Collins' non-light-like regulator; the soft factor; the combination of `def:tmd-collins`; extraction of $\tilde K$, $\gamma_K$, $\gamma_q$ and $\tilde C_{q/q}$, including the $S_\varepsilon$ remark. Follow `research/c_tmd/DERIVATION.md` §3 (R1–R8) and `tex/tmd_oneloop.tex` (VF-TMD-1…9).
  - `\uses{lem:tmd-soft-oneloop, def:tmd-collins, prop:tmd-evolution-oneloop, prop:tmd-small-b}`

* **例 `ex:tmd-qt-asymptotics` — 小 $q_T$ 渐近式的重现** (no tag) · v1
  - Expand `thm:tmd-factorization` to $O(\alpha_s)$ and recover the fixed-order small-$q_T$ terms ($A^{(1)}$, $B^{(1)}$, $C^{(1)}_{qq}$) (VF-TMD-7, VF-TMD-10).
  - `\uses{thm:tmd-factorization, prop:tmd-evolution-oneloop, def:tmd-kin}`

* **例 `ex:tmd-sivers-model` — 标量双夸克模型中的 Sivers 函数** (no tag) · v1
  - The scalar-diquark (BHS) Sivers function with future- and past-pointing lines (VF-TMD-8).
  - `\uses{thm:tmd-sivers-sign}`

**Worked examples.** `ex:tmd-oneloop`, `ex:tmd-qt-asymptotics`, `ex:tmd-sivers-model`.

**Tables.** `tab:tmd-correspondence`: `prop:tmd-zero-bin-soft`, `lem:tmd-sqrt-identity` ↔ App N §N.5 (`asm:appN-tmd`); `lem:tmd-glauber` ↔ `prop:appO-tmd` (`asm:appO-*`) [SYNC-APP].

**Figures.** Existing (tikz3, final): `fig:tmd-staple` (caption: light-like staples; $n$ is our $n_B$ — say so; space-like staples of the quasi-TMD are in Ch22–Ch23), `fig:tmd-soft-factor`, `fig:tmd-dy`, `fig:sidis-dy-links` (M33 sentence at first reference). Optional new: `fig:tmd-evolution`, `fig:tmd-rapidity-bars` (refdoc S56).

**Misconception box.** M12, M13, M14, M15, M16, M17, **M33**; critic C8, C9, C10; O15.

**Key citation keys.** `CollinsSoper1981`, `CollinsSoper1982b`, `CollinsSoperSterman1985a`, `ParisiPetronzio1979`, `DokshitzerDiakonovTroian1978`, `Collins2011`, `JiMaYuan2005`, `Ji:2004xq`, `Ji:2005nu`, `JiYuan2002`, `BelitskyJiYuan2003`, `Collins:1999dz`, `AybatRogers2011`, `EchevarriaIdilbiScimemi2012`, `Echevarria:2012js`, `ChiuEtAl2012a`, `ChiuEtAl2012b`, `BecherNeubert2011`, `Collins:2017oxh`, `Collins:2016hqq`, `Vladimirov:2017ksc`, `Duhr:2022yyp`, `Moult:2022xzt`, `Gatheral1983`, `FrenkelTaylor1984`, `Collins2002`, `Collins1993`, `BrodskyHwangSchmidt2002`, `Sivers1990`, `Sivers:1990fh`, `BoerMulders1998`, `Boer:2003cm`, `CollinsMetz2004`, `MeissnerMetz2009`, `BacchettaEtAl2004`, `HERMES:2009lmz`, `HERMES:2020ifk`, `COMPASS:2017jbv`, `COMPASS:2023vqt`, `STAR:2015vmv`, `STAR:2023jwh`, `Bury:2020vhj`, `Echevarria:2020hpy`, `Ji:2006ub`, `QiuSterman1991c`, `EfremovTeryaev1985`, `Kang:2008ey`, `Braun:2009mi`, `Vogelsang:2009pj`, `Kang:2011hk`, `Cammarota:2020qcw`, `EbertMichelStewartSun2022`, `BoussarieEtAl2023`, `AngelesMartinezEtAl2015`, `RothsteinStewart2016`, `Meng:1995yn`, `Nadolsky:1999kb`.

**Pending.** [PENDING-VERIFY: X2] (`prop:tmd-zero-bin-soft`(b), `lem:tmd-sqrt-identity`(b)); [X1] (`lem:tmd-glauber` precise form); [E17] (Aybat–Rogers $\zeta$); [N20]; [S63-6] (W+Y); [S63-7] ($p=2$); [S63-9] (Collins equation numbers).

---------------------------------------------------------------------------------------------------

## Chapter 15 — 有效场论方法：SCET / Effective-field-theory methods: soft-collinear effective theory

`\label{ch:scet}` · `ch15_scet.tex` · **13 pp** · full · Part IV

**Purpose.** Reformulate factorization as an effective field theory: modes and power counting; the leading collinear Lagrangian and the collinear Wilson line; gauge symmetry and the BPS ultrasoft decoupling theorem with all of its conditions; SCET$_{\rm I}$ vs SCET$_{\rm II}$, zero-bin subtractions, rapidity divergences and regulators; Glauber operators and their dictionary to the light-cone-ordered proof (refdoc S38); matching; thrust factorization $H\,J\otimes J\otimes S$ with one-loop factors, RG consistency and LL resummation. Honest status (C6, M18): mode completeness *is* the region analysis of Ch4, and Glauber modes must be shown to cancel or to be absent; "SCET proofs are not more rigorous than Collins'; they are complementary" — the chapter opens and closes with the map of the three SCET premises onto the three difficulties of the graphical method.

**Conventions (this chapter only).** $n=(1,0,0,1)$, $\bar n=(1,0,0,-1)$; scalings for $(\bar n\!\cdot\!p,\ n\!\cdot\!p,\ p_\perp)$ (Rothstein–Stewart and the blueprint use the swapped order — convert every quotation); star distributions as in WRITER_SPEC_v2 §3 row 22 (thrust plus distributions subtract at $\tau=0$); Laplace transforms follow Becher–Schwartz (row 24).

**Depends on.** Ch4 (`def:ir-scalings`, `thm:ir-leading-regions`), Ch5 (`prop:sudakov-oneloop`), Ch9 (regions, subtractions, `prop:method-glauber-deformation`), Ch14 (rapidity divergences, `prop:tmd-evolution`).

**Box.**
- 证明了：`prop:scet-scalings`、`prop:scet-gauge`、`thm:scet-decoupling`（[R, R_def]，作为 LO SCET 拉氏量的恒等式）；`prop:scet-lagrangian`、`prop:scet-wilson`、`prop:scet-scet2`、`prop:scet-hard-matching`、`prop:scet-thrust-oneloop`（[R, R_PT]）。
- 给出全阶论证：`prop:scet-rapidity-rg`、`prop:scet-glauber-operators`、`thm:scet-thrust`、`prop:scet-ll`（[A]；作为 QCD 陈述继承模式完备性 `asm:intro-bridge`、`asm:appN-envelope`）。
- 没有证明：模式完备性本身（即第~4~章的区域分析）；强子对撞中的 Glauber 相消（RS：远不是因子化的证明）；宣布的完整 SCET DY 证明（截至 2026 年 10 月未发表）。

**Sections.**
1. `sec:scet-modes` 模式与幂次计数 (optional `fig:scet-modes`) — opening paragraph: `rem:scet-assumptions` map (forward within chapter as text).
2. `sec:scet-lagrangian` 领头阶共线拉氏量与共线 Wilson 线 (`fig:scet-wilson`).
3. `sec:scet-decoupling` 规范对称性与超软退耦.
4. `sec:scet-scet2` SCET$_{\rm II}$、零箱减除与快度发散.
5. `sec:scet-glauber` Glauber 算符及其与光锥序证明的对照.
6. `sec:scet-thrust` 推力分布的因子化 (`fig:dijet-factorization`).
7. `sec:scet-rg` 重整化群一致性与重求和.
8. `sec:scet-status` SCET 证明的前提与地位.

**Canonical statements** (in reading order).

* **定义 `def:scet-modes` — 模式** (no tag) · v1
  - **陈述.** In $(\bar n\!\cdot\!p,n\!\cdot\!p,p_\perp)/Q$ (VF-SCET-1; Rothstein–Stewart Table 1 after swapping the first two entries): hard $(1,1,1)$; $n$-collinear $(1,\lambda^2,\lambda)$; $\bar n$-collinear $(\lambda^2,1,\lambda)$; ultrasoft $(\lambda^2,\lambda^2,\lambda^2)$; soft $(\lambda,\lambda,\lambda)$; hard-collinear $(1,\lambda,\lambda^{1/2})$; Glauber $n\bar n$ $(\lambda^2,\lambda^2,\lambda)$; Glauber $ns$ $(\lambda,\lambda^2,\lambda)$; Glauber $\bar ns$ $(\lambda^2,\lambda,\lambda)$.
  - `\uses{def:ir-scalings}`

* **命题 `prop:scet-scalings` — 场的标度** [R, R_def] · v1
  - **陈述.** $\xi_n\sim\lambda$; $(\bar n\!\cdot\!A_n,n\!\cdot\!A_n,A_{n\perp})\sim(1,\lambda^2,\lambda)$; $A_{us}\sim\lambda^2$; $q_{us}\sim\lambda^3$; $A_s\sim\lambda$; $q_s\sim\lambda^{3/2}$ — from the two-point functions (VF-SCET-2; `BauerEtAl2001`; `Bauer:2002uv`).
  - **证明.** Full.
  - `\uses{def:scet-modes, def:prelim-feynman-rules}`

* **命题 `prop:scet-lagrangian` — 领头阶共线夸克拉氏量** [R, R_PT] · v1
  - **陈述.** (Tree-level matching.) $\mathcal L^{(0)}_{\xi\xi}=\bar\xi_n\big[in\!\cdot\!D+i\slashed D_{\perp c}\frac1{i\bar n\!\cdot\!D_c}i\slashed D_{\perp c}\big]\frac{\bar{\slashed n}}2\xi_n$, $in\!\cdot\!D=in\!\cdot\!\partial+gn\!\cdot\!A_n+gn\!\cdot\!A_{us}(x_-)$; Feynman rules: collinear vertex, ultrasoft vertex $igt^an^\mu\frac{\bar{\slashed n}}2$, propagator $i\frac{\slashed n}2\frac{\bar n\cdot p}{p^2+i0}$ (VF-SCET-3/4; `BauerEtAl2001`, `BauerPirjolStewart2002`).
  - **证明.** Full (integrate out $\phi=P_{\bar n}\psi$ at tree level — an exact identity — then power counting; c_scet `s1`).
  - `\uses{prop:scet-scalings, def:prelim-qcd}`

* **命题 `prop:scet-wilson` — 共线 Wilson 线** [R, R_PT] · v1
  - **陈述.** $W_n(x)=W[x,x-\infty\bar n]=P\exp(ig\int_{-\infty}^0ds\,\bar n\!\cdot\!A_n(x+s\bar n))=\sum_{\rm perms}\exp[-\frac g{\bar{\mathcal P}}\bar n\!\cdot\!A_n]$; one-gluon rule $-g\bar n^\mu t^a/(\bar n\cdot k+i0)$; arises from integrating out off-shell modes at tree level (one gluon checked numerically; all orders by the induction of `BauerEtAl2001`); no sign change of $g$ is needed relative to BFPS/BPS (VF-SCET-5).
  - **证明.** Full at tree level.
  - `\uses{prop:scet-lagrangian, def:prelim-wilson}`

* **例 `ex:scet-wn-tree` — $W_n$ 的树图匹配** (no tag) · v1
  - Tree-level matching of an off-shell collinear gluon attached to a $\bar n$ quark, producing the first term of $W_n$.
  - `\uses{prop:scet-wilson}`

* **命题 `prop:scet-gauge` — 共线与超软规范对称性** [R, R_def] · v1
  - **陈述.** The field-strength term is invariant under collinear and ultrasoft transformations; the gauge-fixing and ghost terms are ultrasoft covariant and BRST invariant (correction of BPS 2002's wording about the ghost term: c_scet §6 item 15 [PENDING-VERIFY: E25]).
  - **证明.** Full (as statements about the LO SCET Lagrangian written in `prop:scet-lagrangian`, taken as an expression).
  - `\uses{def:scet-modes, prop:qcd-covariance, lem:prelim-brst-nilpotent}`

* **定理 `thm:scet-decoupling` — 超软退耦（BPS 场重定义）** [R, R_def] · v1
  - **陈述.** Key identity: $in\!\cdot\!D_{us}Y_n=Y_n\,in\!\cdot\!\partial$, where $Y_n(x)=W[x,x-\infty n]$ is built from the multipole-expanded $n\!\cdot\!A_{us}(x_-)$ (VF-SCET-6). The redefinitions $\xi_n=Y_n\xi_n^{(0)}$, $A_n=Y_nA_n^{(0)}Y_n^\dagger$, $c_n=Y_nc_n^{(0)}Y_n^\dagger$ remove $n\!\cdot\!A_{us}$ from $\mathcal L^{(0)}_{\xi\xi}+\mathcal L^{(0)}_{cg}$. Conditions (c_scet §6 item 5): (1) the collinear ghosts are redefined; (2) the collinear gauge fixing is covariant under ultrasoft transformations; (3) the Jacobian is unity; (4) leading power only; (5) $Y_n$ is built from multipole-expanded fields.
  - **证明.** Full (c_scet §2.4; `BauerPirjolStewart2002`).
  - **Status (print).** As an identity of the LO SCET Lagrangian, [R, R_def]; as a statement about QCD it inherits mode completeness, which is [A] (`rem:scet-assumptions`).
  - `\uses{prop:scet-gauge, prop:prelim-wilson-covariance}`

* **例 `ex:scet-decoupling-tree` — BPS 场重定义的树图演示** (no tag) · v1
  - Tree-level demonstration that the redefinition removes $n\cdot A_{us}$ from $\mathcal L^{(0)}$.
  - `\uses{thm:scet-decoupling}`

* **注 `rem:scet-y-direction` — $Y_n$ 的方向与 $i0$** (no tag) · v1→corrected (refdoc S38, ERR-m18)
  - The LO SCET Feynman rules already give future-pointing $Y$ lines for outgoing collinear quarks (`Chay:2004zn`); the direction is fixed by matching the external states; it is immaterial for the Lagrangian identity and for one-loop thrust (`Kang:2015moa`); rule (`RothsteinStewart2016`): ultrasoft directions are physical; the $\lambda^2Q$ mode is ultrasoft; ultrasoft decoupling does **not** remove Glauber interactions (c_scet §6 item 14).

* **定义 `def:scet-zero-bin` — 零箱减除** (no tag) · v1 (+ refdoc S38, D17)
  - **陈述.** The zero-bin subtraction (`ManoharStewart2007`) is the EFT counterpart of `def:method-subtraction`; equivalent to soft subtractions (`IdilbiMehen2007`); double counting is avoided only if it is carried out consistently (C6). For thrust, the zero-bin integrals are scaleless by $a^{-\varepsilon}$ scaling (re-derived), which `thm:scet-thrust` uses.
  - `\uses{def:method-subtraction, lem:prelim-scaleless}`

* **命题 `prop:scet-scet2` — SCET$_{\rm II}$ 与软 Wilson 线** [R, R_PT] · v1
  - **陈述.** Collinear $(1,\lambda^2,\lambda)$ and soft $(\lambda,\lambda,\lambda)$ modes have the same virtuality; a soft gluon attached to a collinear line produces hard-collinear virtuality $\lambda Q^2$; integrating it out yields $S_n=P\exp(ig\int_{-\infty}^0ds\,n\!\cdot\!A_s(x+sn))$ (numerical check: relative error $0.77,0.077,0.0077$ for $\lambda=10^{-1,-2,-3}$); integrals are separated only in rapidity, so rapidity regulators are required (`Hill:2002vw`, `BauerEtAl2002`).
  - **证明.** Full at tree level.
  - `\uses{def:scet-modes, prop:scet-wilson}`

* **命题 `prop:scet-rapidity-rg` — 快度发散的处理与等价性** [A] · v1
  - **陈述.** The rapidity RG (`ChiuEtAl2012a`, `ChiuEtAl2012b`), the collinear anomaly (`BecherNeubert2011`) and Collins' non-light-like lines (Ch14) give equivalent TMD factorization (`Collins:2017oxh`, explicit at low orders); in the EIS/δ-regulator normalization $\partial\ln\tilde f/\partial\ln Q^2=-D$ at $\zeta=Q^2$ with $D=-\tilde K/2$ (c_tmd §3.8); the normalization of $\gamma_\nu$ of `ChiuEtAl2012a` relative to $\tilde K$ is transcribed by the writer (verify).
  - **地位与缺口.** Equivalence shown order by order only.
  - `\uses{prop:scet-scet2, def:tmd-collins, prop:tmd-evolution}`

* **命题 `prop:scet-glauber-operators` — Glauber 算符** [A] · v1
  - **陈述.** (`RothsteinStewart2016`.) There are Glauber operators coupling the $n$, $\bar n$ and soft sectors, and Glauber exchange "can induce corrections which invalidate factorization"; Glauber subtractions make soft and collinear Wilson-line directions irrelevant; the spectator–spectator phase cancels once $\Delta p_\perp$ is integrated; active–active Glauber equals the Glauber zero-bin of the soft graph (RS §10.1, as read by c_glauber).
  - **地位与缺口.** The construction is [A]; the announced complete SCET proof of DY had not been found as of 2026-10 (survey item 8); Glauber EFT status and the SYZ result for single-scale observables: Ch18, Ch24 (pointers).
  - `\uses{def:scet-modes, prop:scet-scet2}`

* **注 `rem:scet-glauber-dictionary` — Glauber SCET 与光锥序证明的对照** (no tag) · refdoc S38 (E29)
  - RS Glauber operators ↔ the window/carrier construction of App O; the RS rapidity regulator $|2k^z|^{-\eta}$ ↔ the common ordering (`rem:dy-common-ordering`); crossed Glauber boxes vanish; RS: "taken on its own this is far from a proof of factorization".

* **命题 `prop:scet-hard-matching` — 硬匹配系数** [R, R_PT] · v1
  - **陈述.** (One loop.) With $a=\frac{C_F\alpha_s}{4\pi}$: $C_V=1+a[-L^2+3L-8+\zeta_2]$, $L=\ln\frac{-q^2-i0}{\mu^2}$; $H=|C_V|^2=1+a[-2L_Q^2+6L_Q-16+\frac{7\pi^2}3]$ (VF-SCET-7/8; agrees with `BecherSchwartz2008` App. B).
  - **证明.** Full (exact-in-$\varepsilon$ form factor, `prop:sudakov-oneloop`).
  - `\uses{prop:sudakov-oneloop}`

* **定理 `thm:scet-thrust` — 推力分布的因子化** [A] · v1 (+ refdoc S38)
  - **陈述.** $$\frac1{\sigma_0}\frac{d\sigma}{d\tau}=H(Q^2,\mu)\int dp_L^2\,dp_R^2\,dk\;J(p_L^2,\mu)J(p_R^2,\mu)S_T(k,\mu)\,\delta\Big(\tau-\frac{p_L^2+p_R^2}{Q^2}-\frac kQ\Big)+O(\tau^0),$$ $\tau=1-T$; the jet function is defined by the explicitly normalized cut (c_scet `tex/c_scet_thrust.tex`, eq. thrust-Jdef); Becher–Schwartz' literal formula carries an implicit $-\frac1{2N_c}{\rm tr}$ (c_scet §6 item 13) [PENDING-VERIFY: E24].
  - **非微扰地位.** \cref{asm:intro-bridge}（MA1、MA2）。
  - **证明.** Sketch (decoupling; zero-bin scaleless; matching).
  - **地位与缺口.** [A] to all orders within SCET with modes hard, two collinear, and ultrasoft; for $e^+e^-$ there is no Glauber pinch because all collinear lines are outgoing (`prop:method-glauber-deformation`, `lem:coll-final-poles`); cite RS 2016 only for the general mechanism (c_scet §6 item 14); mode completeness = `asm:intro-bridge`(Br1) + `asm:appN-envelope`. Literature: `BecherSchwartz2008`, `Schwartz:2007ib`, `Fleming:2007qr`, `Fleming:2007xt`, `Bauer:2008dt`, `Lee:2006nr`.
  - `\uses{thm:scet-decoupling, prop:scet-hard-matching, def:scet-zero-bin, prop:method-glauber-deformation, thm:ir-leading-regions, asm:intro-bridge}`

* **命题 `prop:scet-thrust-oneloop` — 单圈因子与 RG 一致性** [R, R_PT] · v1
  - **陈述.** (One loop, $a=\frac{C_F\alpha_s}{4\pi}$.) Jet function $J=\delta(p^2)+a\{(7-\pi^2)\delta(p^2)-3[\frac1{p^2}]_*+4[\frac{\ln(p^2/\mu^2)}{p^2}]_*\}$; soft function $S_T=\delta(k)+a\{\frac{\pi^2}3\delta(k)-16[\frac{\ln(k/\mu)}k]_*\}$ (VF-SCET-9/10); consistency: the cusp terms cancel identically ($2L_Q-4L_J+4L_S=0$), and $\gamma^S=\gamma^H-2\gamma^J$ (the correct form of the blueprint's "$\gamma_H+2\gamma_J+\gamma_S=0$"); two loops: $\gamma^S_1=C_FC_A(\frac{808}{27}-\frac{11\pi^2}9-28\zeta_3)+C_FT_Fn_f(-\frac{224}{27}+\frac{4\pi^2}9)$ (VF-SCET-11); reproduces QCD: $\frac1{\sigma_0}\frac{d\sigma}{d\tau}=\delta(\tau)+\frac{C_F\alpha_s}{2\pi}\{(\frac{\pi^2}3-1)\delta(\tau)-3[\frac1\tau]_+-4[\frac{\ln\tau}\tau]_+\}$ (VF-SCET-12; critic c3).
  - **证明.** Full at one loop.
  - `\uses{prop:scet-hard-matching, def:prelim-plus}`

* **例 `ex:scet-thrust-oneloop` — 单圈 $H$、$J$、$S_T$ 合成 QCD 奇异项** (no tag) · v1
  - $H$, $J$, $S_T$ at one loop combine in Laplace space into the QCD singular terms; the $\delta(\tau)$ coefficient $\frac{\pi^2}3-1$ also from the total-rate sum rule ($2.289868133697$ vs $2.289868133696$).
  - `\uses{prop:scet-thrust-oneloop}`

* **命题 `prop:scet-ll` — 领头对数指数** [A] · v1 (composite)
  - **陈述.** (a) For the QCD thrust distribution: $\ln\tilde t_{\rm LL}=\ell g_1(\lambda)$, $g_1=-\frac{C_F}{\pi b\lambda}[(1-2\lambda)\ln(1-2\lambda)-2(1-\lambda)\ln(1-\lambda)]$, $\lambda=b\alpha_s(Q)\ell$, $b=\beta_0/(4\pi)$, $\ell=\ln(\nu e^{\gamma_E})$ (VF-SCET-14); matches CTTW (`CataniEtAl1993`). (b)（作为 `thm:scet-thrust` 的 RG 方程的 LL 解，\tagR，$R_{\rm def}$）the formula is an algebraic consequence of the RG equations.
  - **地位与缺口.** As a statement about QCD it inherits `thm:scet-thrust` ([A]); never write 「推力的领头对数重求和在微扰论中已严格证明」.
  - `\uses{thm:scet-thrust, prop:scet-thrust-oneloop, prop:prelim-beta}`

* **注 `rem:scet-assumptions` — SCET 证明的前提** (no tag) · v1 (+ refdoc S38; opening and closing of the chapter)
  - (1) Mode completeness: the chosen modes reproduce the IR of QCD — this *is* the region analysis of Ch4 (`thm:ir-leading-regions`); (2) zero-bin consistency; (3) Glauber modes absent or cancelling; (4) leading power. Map onto the graphical method: mode completeness ↔ region completeness and power counting (`asm:intro-bridge`, `asm:appN-envelope`); zero-bin consistency ↔ subtraction combinatorics (`asm:appN-collins`); Glauber Lagrangian and rapidity regulator ↔ `asm:appO-*`. Survey item 17: Collins 2011 §15.9 could not "penetrate the SCET literature"; "SCET proofs are not more rigorous than Collins'; they are complementary" (C6, M18).

**Worked examples.** `ex:scet-wn-tree`, `ex:scet-decoupling-tree`, `ex:scet-thrust-oneloop`.

**Figures.** Existing (tikz2): `fig:scet-wilson`, `fig:dijet-factorization`; optional new: `fig:scet-modes`.

**Misconception box.** M18, M19 (Minkowski regions; hidden regions); C6.

**Key citation keys.** `BauerFlemingLuke2000`, `BauerEtAl2001`, `BauerStewart2001`, `BauerPirjolStewart2001`, `BauerPirjolStewart2002`, `BauerEtAl2002`, `Bauer:2002uv`, `BenekeEtAl2002`, `Beneke:2002ni`, `Hill:2002vw`, `ManoharStewart2007`, `IdilbiMehen2007`, `Lee:2006nr`, `BecherSchwartz2008`, `Schwartz:2007ib`, `Bauer:2008dt`, `Fleming:2007qr`, `Fleming:2007xt`, `Bauer:2003di`, `Chay:2004zn`, `Kang:2015moa`, `ChiuEtAl2012a`, `ChiuEtAl2012b`, `BecherNeubert2011`, `Collins:2017oxh`, `RothsteinStewart2016`, `Feige:2013zla`, `FeigeSchwartz2014`, `KorchemskyRadyushkin1987`, `CataniEtAl1993`, `DeRujula:1978vmq`, `BecherBroggioFerroglia2015`, `Collins2011`.

**Pending.** [PENDING-VERIFY: E24, E25] (BS normalization, BPS ghost wording); E23 via `def:sudakov-cusp`.

---------------------------------------------------------------------------------------------------

## Chapter 16 — 喷注、事件形状、非全局对数与超领头对数 / Jets, event shapes, non-global and super-leading logarithms

`\label{ch:jets}` · `ch16_jets.tex` · **10 pp** · short format (precise statement + status + proof idea + one worked example) · Part IV

**Purpose.** Give IR-safe jet observables a home: what IR safety gives and does not give (M9, M10); the classic Sterman–Weinberg calculation and the LO thrust distribution; the status of hadronization corrections; non-global logarithms (existence, BMS, EFT factorization); super-leading logarithms as computed and resummed results, with the three-way separation of their status (refdoc S35): (i) amplitude-level violation of strict collinear factorization [V], (ii) SLLs at fixed order and resummed, (iii) PDF factorization of gap cross sections [C] with restoration evidence. The factorization-violation side belongs to Ch18; coherence-violating logarithms in one-jettiness and other frontier items are in Ch24 (pointers).

**Depends on.** Ch4 (`def:ir-safe`, `thm:ir-safe-finite`), Ch5 (`prop:sudakov-coulomb`, `thm:sudakov-ir-poles`), Ch6 (`prop:ee-oneloop`), Ch15 (`thm:scet-thrust`).

**Box.**
- 证明了：`prop:jets-sw`、`prop:jets-thrust-lo`、`prop:jets-ngl`（[R, R_PT]，固定阶）。
- 给出全阶论证：`cor:jets-ir-finite`、`thm:jets-bms`（LL，大 $N_c$）、`thm:jets-ngl-factorization`（[A]）。
- 没有证明：强子化修正的普适性（`conj:jets-hadronization`，[C]）；超出 LL 与有限 $N_c$ 的 NGL（`prop:jets-ngl-beyond`，[P]）；超领头对数的全阶结构与间隙截面的 PDF 因子化（`prop:jets-sll`，[P]；PDF 因子化 [C]）。

**Sections.** `sec:jets-irsafe` 红外安全的喷注与事件形状 (`fig:jets-sw-cone`); `sec:jets-hadronization` 强子化修正; `sec:jets-ngl` 非全局对数 (`fig:jets-ngl`); `sec:jets-sll` 超领头对数 (`fig:jets-gap`).

**Canonical statements** (in reading order).

* **定义 `def:jets-algorithms` — 红外安全的喷注定义与事件形状** (no tag) · v1
  - **陈述.** IR safe in the sense of `def:ir-safe`: the SW cone (half-angle $\delta$; energy fraction $\epsilon$ of the **total** energy $\sqrt s$); thrust $T$, $\tau=1-T$; sequential recombination: $k_T$ (`CataniEtAl1993kt`, `EllisSoper1993`) and anti-$k_T$ (`CacciariSalamSoyez2008`); SISCone (`SalamSoyez2007`). Seed-based cones are not IR safe at higher orders (`SalamSoyez2007`).
  - `\uses{def:ir-safe}`

* **命题 `prop:jets-sw` — Sterman–Weinberg 两喷注截面** [R, R_PT] · v1
  - **陈述.** (At $O(\alpha_s)$.) $$\sigma_{2j}=\sigma_0\Big\{1-\frac{C_F\alpha_s}\pi\Big[4\ln\delta\ln2\epsilon+3\ln\delta+\frac{\pi^2}3-\frac52\Big]\Big\},\qquad\epsilon<\delta\ll1;$$ if $\epsilon$ is a fraction of the *beam* energy, the log is $\ln\epsilon$; the variant "$4\ln\delta\ln\epsilon$" with $\epsilon$ a fraction of the total energy is wrong by $4\ln2|\ln\delta|$ [PENDING-VERIFY: E28 — App Q only if a published source with this error is identified]; the formula fails for $\epsilon\gg\delta$ (c_ee §8, 6/6 checks; VF-EE-12).
  - **证明.** Full (worked example).
  - `\uses{def:jets-algorithms, prop:ee-oneloop, prop:qcd-soft-collinear-limits}`

* **例 `ex:jets-sw` — $O(\alpha_s)$ 的 Sterman–Weinberg 截面** (no tag) · v1
  - The three-body phase space and the cone and energy cuts; the virtual correction; the $\ln2\epsilon$ subtlety, with a numerical table (c_ee §8).
  - `\uses{prop:jets-sw}`

* **推论 `cor:jets-ir-finite` — 红外安全喷注截面的有限性** [A] · v1
  - **陈述.** IR-safe jet cross sections in $e^+e^-$ are finite order by order (`thm:ir-safe-finite` applied to jet algorithms; `StermanWeinberg1977`, `Sterman1978a`, `Sterman1978b`, `Sterman:1979uw`).
  - **地位与缺口.** Covers final-state singularities only; with incoming hadrons it needs collinear factorization (M8, M9).
  - `\uses{thm:ir-safe-finite, def:jets-algorithms}`

* **命题 `prop:jets-thrust-lo` — 领头阶推力分布** [R, R_PT] · v1
  - **陈述.** (At $O(\alpha_s)$.) Distribution $\frac{C_F\alpha_s}{2\pi}\big[\frac{2(3T^2-3T+2)}{T(1-T)}\ln\frac{2T-1}{1-T}-\frac{3(3T-2)(2-T)}{1-T}\big]$ (VF-SCET-13; `DeRujula:1978vmq`); singular terms and cumulant $1+\frac{C_F\alpha_s}{2\pi}[-2\ln^2\tau-3\ln\tau+\frac{\pi^2}3-1]+O(\tau\ln\tau)$ (critic c3; VF-SCET-12); exact identity $\frac{M_L^2+M_R^2}{Q^2}=\tau-\frac{\tau^2}2+\frac{(M_R^2-M_L^2)^2}{2Q^4}$ for massless particles (VF-SCET-15).
  - **证明.** Full.
  - `\uses{def:jets-algorithms}`

* **猜想 `conj:jets-hadronization` — 强子化修正的普适性** [C] · v1
  - **陈述.** The leading hadronization correction to event shapes is a shift $\propto\Lambda/Q$ with a universal coefficient (dispersive model `DokshitzerWebber1995`; renormalon motivation: Ch21).
  - **地位与缺口.** For $Q\tau\sim\Lambda$ the soft function becomes a non-perturbative shape function (`Korchemsky:1994is`, `Korchemsky:1999kt`, `Bauer:2003di`, `Lee:2006nr`, `Bauer:2008dt`); universality is [C] (critic B18); M10: event shapes have $O(\Lambda/Q)$ corrections.
  - `\uses{thm:scet-thrust}`

* **命题 `prop:jets-ngl` — 非全局对数的存在** [R, R_PT] · v1
  - **陈述.** (At $O(\alpha_s^2)$.) For an energy-flow veto in a patch (Dasgupta–Salam hemisphere case) the leading NGL appears at $O(\alpha_s^2)$ with colour factor $C_FC_A$ and a $\pi^2$ coefficient (`DasguptaSalam2001`, `Dasgupta:2002bw`; normalization to be checked by the writer); the exact fixed-order coefficients are known.
  - **证明.** Sketch (strongly ordered two-gluon emission).
  - `\uses{def:jets-algorithms}`

* **定理 `thm:jets-bms` — BMS 方程** [A] · v1
  - **陈述.** (Leading log, large $N_c$.) The BMS equation (`Banfi:2002hw`) resums the NGLs; finite-$N_c$ evolution: `Weigert:2003mm`, `Hatta:2013iba`; relation to BFKL/BK: `Caron-Huot:2015bja`.
  - **地位与缺口.** LL and large $N_c$ only.
  - `\uses{prop:jets-ngl}`

* **命题 `prop:jets-ngl-beyond` — 超出领头对数与有限 $N_c$** [P] · v1
  - **陈述.** Beyond LL and at finite $N_c$, NGL resummation exists only in partial and numerical forms.
  - **地位与缺口.** Partial and numerical results only (NLL NGL resummation: Ch24, pointer).
  - `\uses{thm:jets-bms}`

* **定理 `thm:jets-ngl-factorization` — 喷注过程的有效场论因子化** [A] · v1
  - **陈述.** Multi-Wilson-line soft functions and their RG factorize non-global $e^+e^-$ observables (`Becher:2015hka`, `Becher:2016mmh`; VF-FRO-14).
  - **非微扰地位.** \cref{asm:intro-bridge}（MA1、MA2）。
  - **地位与缺口.** All-order EFT argument within SCET (inherits `thm:scet-thrust`'s premises).
  - `\uses{thm:scet-thrust, prop:jets-ngl, asm:intro-bridge}`

* **命题 `prop:jets-sll` — 超领头对数** [P] · v1 (+ refdoc S35)
  - **陈述.** In hadron-collider gap-between-jets cross sections, Coulomb (Glauber) phases do not cancel; they generate terms $\alpha_s^nL^{2n-3}$, starting at $\alpha_s^4L^5$ relative to Born (`ForshawKyrieleisSeymour2006` eqs. (3.22), (3.24); `Forshaw:2008cq`); first term $-\sigma_0(\frac{2\alpha_s}\pi)^4\ln^5\frac Q{Q_0}\pi^2Y\frac{3N^2-4}{480}$ for quark–quark scattering with one gluon outside the gap (VF-GLA-13); all-order tower $\alpha_s^{n+3}L^{2n+3}$ and its resummation (`Becher:2021zkk`, `Becher:2023mtx`, `Boer:2024hzh`, `Becher:2024nqc`; VF-FRO-7); super-super-leading (coherence-violating) logarithms in one-jettiness: `Banfi:2025mra` (Ch24) [PENDING-VERIFY: E16].
  - **地位与缺口 (three items, refdoc S35).** (i) Amplitude-level violation of strict collinear factorization: [V] (`prop:break-spacelike`, Ch18); (ii) SLLs at fixed order and resummed: [P] as stated here; (iii) PDF factorization of gap cross sections: [C], with restoration evidence `Becher:2024kmk` (three-loop active–active Glauber terms restore consistency below the veto scale) [PENDING-VERIFY: S63-10]. Never write 「间隙截面的因子化已被证明破坏」 (S58).
  - `\uses{prop:sudakov-coulomb, thm:sudakov-ir-poles}`

**Worked example.** `ex:jets-sw`.

**Tables.** Optional `tab:jets-soft-functions` (refdoc S35, T19): observable ↔ soft function (Wilson-line content, measurement): total rate ($S=1$), $q_T$ (`def:tmd-soft`), thrust ($S_T$), jet veto, hemisphere mass, gaps (multi-Wilson-line).

**Figures.** New (required): `fig:jets-sw-cone`, `fig:jets-ngl`, `fig:jets-gap` (caption's restoration pointer → `prop:jets-sll`).

**Misconception box.** M8, M9, M10.

**Key citation keys.** `StermanWeinberg1977`, `Sterman1978a`, `Sterman1978b`, `Sterman:1979uw`, `Farhi1977`, `DeRujula:1978vmq`, `CataniEtAl1993`, `CataniEtAl1993kt`, `EllisSoper1993`, `CacciariSalamSoyez2008`, `SalamSoyez2007`, `DokshitzerWebber1995`, `Korchemsky:1994is`, `Korchemsky:1999kt`, `Bauer:2003di`, `Lee:2006nr`, `Bauer:2008dt`, `DasguptaSalam2001`, `Dasgupta:2002bw`, `Banfi:2002hw`, `Weigert:2003mm`, `Hatta:2013iba`, `Caron-Huot:2015bja`, `Becher:2015hka`, `Becher:2016mmh`, `ForshawKyrieleisSeymour2006`, `Forshaw:2008cq`, `Becher:2021zkk`, `Becher:2023mtx`, `Boer:2024hzh`, `Becher:2024nqc`, `Becher:2024kmk`, `Banfi:2025mra`, `EllisStirlingWebber1996`.

**Pending.** [PENDING-VERIFY: E28, E16, S63-10].

---------------------------------------------------------------------------------------------------

## Chapter 17 — 小 $x$ 与高能因子化 / Small $x$ and high-energy factorization

`\label{ch:smallx}` · `ch17_smallx.tex` · **9 pp** · short format · Part IV

**Purpose.** State precisely what is established in the Regge limit: BFKL at LL and NLL as statements about the high-energy limit of perturbation theory; $k_T$ (high-energy) factorization at LL in $\ln(1/x)$ for specific processes; BK/JIMWLK at LL plus NLO BK in the dipole/shock-wave framework (results within the eikonal (Regge) expansion at fixed logarithmic accuracy, not leading-power theorems of QCD); saturation [C]. Collinear factorization becomes non-uniform as $x\to0$. Frontier items (NLO BK issues, Regge factorization beyond NLL [V], small-$x$ helicity discrepancy) are in Ch24 (pointers).

**Depends on.** Ch3 (Wilson lines), Ch5 (cusp), Ch7 (`def:dis-kinematics`), Ch8 (DGLAP, `prop:pdf-lo-kernels`), Ch14 (Wilson-line correlators).

**Box.**
- 证明了：（无新的 [R] 陈述；`ex:smallx-dla` 为固定耦合下的鞍点计算）。
- 给出全阶论证：`thm:smallx-bfkl`（LL/NLL）、`thm:smallx-bk`（LL，偶极子框架）（[A]）。
- 没有证明：$k_T$ 因子化的幂次修正控制（`prop:smallx-kt`，[P]）；饱和（`conj:smallx-saturation`，[C]）；与共线因子化的匹配。

**Sections.** `sec:smallx-regge` Regge 极限与 $\ln(1/x)$; `sec:smallx-bfkl` BFKL (`fig:bfkl-ladder`); `sec:smallx-kt` $k_T$ 因子化; `sec:smallx-dipole` 偶极子、BK 与 JIMWLK (`fig:smallx-dipole`); `sec:smallx-status` 地位与图谱 (`fig:smallx-map`).

**Canonical statements** (in reading order).

* **定义 `def:smallx-regge` — 高能极限** (no tag) · v1
  - **陈述.** The limit $s\gg|t|$, or $x\to0$ at fixed $Q^2$; leading logarithms $(\alpha_s\ln\frac1x)^n$; the unintegrated gluon distribution $\mathcal F(x,k_T)$ and the dipole amplitude $N(x,r)$, each in a stated normalization.
  - `\uses{def:prelim-wilson, def:dis-kinematics}`

* **定理 `thm:smallx-bfkl` — BFKL 方程** [A] · v1
  - **陈述.** (Within LL/NLL.) The BFKL equation resums $(\alpha_s\ln\frac1x)^n$: LL (`Fadin:1975cb`, `Kuraev:1976ge`, `KuraevLipatovFadin1977`, `BalitskyLipatov1978`); NLL (`Fadin:1998py`, `Ciafaloni:1998gs`); LL intercept $\omega_{\mathbb P}=4\ln2\,\frac{N_c\alpha_s}\pi=\bar\alpha_s\chi(\frac12)$ (VF-MISC-4).
  - **地位与缺口.** A statement about the high-energy limit of perturbation theory at fixed logarithmic accuracy; the NLL corrections are large, which motivates collinear-improved schemes; Regge-pole factorization of amplitudes fails beyond NLL (Ch24, pointer).
  - `\uses{def:smallx-regge}`

* **命题 `prop:smallx-kt` — $k_T$（高能）因子化** [P] · v1
  - **陈述.** $\sigma=\int d^2k_T\,\hat\sigma(x,k_T)\mathcal F(x,k_T)$ for heavy quarks and DIS at LL in $\ln(1/x)$ (`CataniCiafaloniHautmann1991`, `Catani:1990xk`, `CollinsEllis1991`, `Levin:1991ry`; beyond LL: `Catani:1994sq`).
  - **地位与缺口.** Not a theorem with controlled power corrections; unintegrated gluon distributions are process dependent (`Dominguez:2011wm`).
  - `\uses{thm:smallx-bfkl}`

* **定理 `thm:smallx-bk` — BK 方程与 JIMWLK** [A] · v1
  - **陈述.** (LL, dipole/shock-wave framework.) LL BK: $\partial_YN_{01}=\frac{\bar\alpha_s}{2\pi}\int d^2x_2\frac{x_{01}^2}{x_{02}^2x_{12}^2}[N_{02}+N_{12}-N_{01}-N_{02}N_{12}]$, $\bar\alpha_s=N_c\alpha_s/\pi$ (VF-MISC-4, VF-FRO-12: the linear part has eigenvalue $\bar\alpha_s\chi(\gamma)$ on $(x_{01}^2)^\gamma$; `Balitsky1996`, `Kovchegov1999`); JIMWLK: `Jalilian-Marian:1997qno`, `Jalilian-Marian:1997jhx`, `Iancu:2000hn`, `Ferreiro:2001qy`; NLO BK: `Balitsky:2007feb`; the linearized BK equation is LL BFKL.
  - **地位与缺口.** Results within the eikonal (Regge) expansion at fixed logarithmic accuracy; never write 「BK/JIMWLK 是 QCD 的领头幂次定理」 (WRITER_SPEC_v2 §6.9); NLO issues: Ch24.
  - `\uses{def:smallx-regge, thm:smallx-bfkl}`

* **猜想 `conj:smallx-saturation` — 饱和与色玻璃凝聚** [C] · v1
  - **陈述.** At small $x$, gluon densities saturate, and the CGC is the effective theory of QCD in that regime (`GribovLevinRyskin1983`, `Mueller:1985wy`, `McLerran:1993ni`, `GelisEtAl2010`, `KovchegovLevin2012`).
  - **地位与缺口.** Matching to collinear factorization is not proven.
  - `\uses{thm:smallx-bk}`

* **注 `rem:smallx-nonuniform` — 共线因子化在小 $x$ 的非一致性** (no tag) · v1
  - Coefficient functions and splitting functions contain $\alpha_s^n\ln^{n-1}(1/x)$, so both the $\alpha_s$ expansion and the power expansion are non-uniform as $x\to0$ (`Milana:1986tq`); small-$x$ resummation of anomalous dimensions: `Catani:1994sq`; nuclear targets: `prop:disall-nuclear`.

* **例 `ex:smallx-dla` — DGLAP 与 BFKL 的双领头对数重叠** (no tag) · v1
  - $\frac{\alpha_s}{2\pi}\gamma_{gg}(N)\simeq\frac{\bar\alpha_s}{N-1}$ ($\gamma_{gg}$ normalized as in VF-PDF-8), the collinear limit of the BFKL kernel; $xg\sim\exp\sqrt{4\bar\alpha_s\ln\frac1x\ln\frac{Q^2}{Q_0^2}}$ at fixed coupling (VF-MISC-4; the writer derives it from `prop:pdf-lo-kernels` by a saddle point).
  - `\uses{prop:pdf-lo-kernels, thm:smallx-bfkl}`

**Worked example.** `ex:smallx-dla`.

**Figures.** Existing (tikz3, final): `fig:bfkl-ladder`; new (required): `fig:smallx-dipole`, `fig:smallx-map`.

**Misconception box.** Non-uniformity of collinear factorization at small $x$; 「BK/JIMWLK 是领头幂次定理」.

**Key citation keys.** `Fadin:1975cb`, `Kuraev:1976ge`, `KuraevLipatovFadin1977`, `BalitskyLipatov1978`, `Fadin:1998py`, `Ciafaloni:1998gs`, `CataniCiafaloniHautmann1991`, `Catani:1990xk`, `CollinsEllis1991`, `Levin:1991ry`, `Catani:1994sq`, `Balitsky1996`, `Kovchegov1999`, `Jalilian-Marian:1997qno`, `Jalilian-Marian:1997jhx`, `Iancu:2000hn`, `Ferreiro:2001qy`, `Balitsky:2007feb`, `GribovLevinRyskin1983`, `Mueller:1985wy`, `McLerran:1993ni`, `Dominguez:2011wm`, `Milana:1986tq`, `GelisEtAl2010`, `KovchegovLevin2012`, `BoerEtAl2011`.

**Pending.** None specific (frontier disagreements E34 are reported in Ch24).

---------------------------------------------------------------------------------------------------

## Chapter 18 — 因子化的破坏与非标准情形 / Breakdown of factorization and non-standard cases

`\label{ch:break}` · `ch18_break.tex` · **14 pp** · full · Part IV

**Purpose.** For each case, say *which hypothesis of `thm:method-template` fails* and give the evidence (explicit counterexample, explicit calculation, partial proof, or experiment — said every time, critic O17). This is where most [V], [C] and [P] tags live, so it must be as careful as the rigorous chapters. **Organizing criterion (refdoc S39):** the measurement-compatibility criterion `prop:break-measurement` — the cut-sum unitarity lemmas hold with a measurement operator inserted iff it commutes with the light-cone evolution and the $\tau=0$ insertions; $1$ and $e^{i\mathbf b\cdot\hat{\mathbf P}_T}$ do, the identified-hadron and gap projectors do not, and for $pp\to h_1h_2X$ the argument breaks at the one-sided-rewriting step (O-3).

**Depends on.** Ch5 (`prop:sudakov-amplitude-factorization`), Ch9 (`thm:method-template`, `prop:method-glauber-deformation`), Ch12 (`lem:dy-fsi`, `prop:dy-abelian-model`, `thm:dy-factorization`), Ch14 (TMD definitions), Ch15 (Glauber operators), Ch16 (SLLs); App O [SYNC-APP].

**Source.** `research/c_glauber/DERIVATION.md` §1–§4 (no check failed, c_glauber §5); corrections c_glauber §6; Chinese snippets `research/c_glauber/tex/c_glauber_snippets.tex`.

**Box.**
- 证明了：`prop:break-colour`（[R, R_PT]）；`prop:break-measurement`（[R, R_cond]，前提 `asm:appO-lcopt`）。
- 给出全阶论证：`thm:break-ddis`、`thm:break-double-dy`（[A]）。
- 破坏（附证据类型）：`thm:break-tmd`（模型反例）、`prop:break-spacelike`（显式单圈计算，振幅层次）、`prop:break-fss`、`prop:break-jet-veto`（显式反例）、`prop:break-hh-diffraction`（实验）（[V]）。
- 没有证明：超出 NNLO 的质量奇异性因子化（`prop:break-mass-singularity`，[C]）；有色末态的 DPS 与“口袋公式”（[C]）。

**Opening table `tab:break-cases`** (refined, refdoc S35/S39).

| case | failing hypothesis | status | evidence |
|---|---|---|---|
| TMD-sensitive $h_1h_2\to H_1H_2X$ | (H3)/(H4): colour entanglement; App O step (O-3) | [V] | model counterexamples (CQ 2007; C07; RM 2010) |
| strict collinear factorization of amplitudes (space-like) | (H2) at amplitude level | [V] | explicit one-loop calculation (CdFR 2012) |
| mass-singularity factorization beyond NNLO | (H3) | [C] | CdFR; Becher et al. 2025 (restoration evidence) |
| gap-between-jets / non-global hadron-collider observables | (H3); measurement does not commute | amplitude [V]; SLLs [P]; PDF factorization [C] | FSS 2012; SLLs (Ch16); `Becher:2024kmk` |
| MPI-sensitive observables ($E_T$, beam thrust with vetoes) | (H3): spectator Glauber + soft | [V] | Zeng 2015 (explicit); Gaunt 2014 vs SYZ 2018 |
| hadron–hadron hard diffraction | (H3)/(H4): gap survival | [V] | experiment (CDF) |
| diffractive DIS | none | [A] | Collins 1998 |
| double DY | (H3) holds | [A] | Diehl et al. 2016 |
| DPS with coloured final states | (H3) | [C] | — |

**Sections.**
1. `sec:break-overview` 组织：哪一条假设失效；测量相容性判据 (optional `fig:break-measurement`).
2. `sec:break-tmd` 强子—强子碰撞中 TMD 因子化的破坏 (`fig:violation-cq`).
3. `sec:break-spacelike` 类空共线极限、Coulomb 相位与 PDF 因子化 (optional `fig:break-spacelike`).
4. `sec:break-mpi` 对多重相互作用敏感的观测量.
5. `sec:break-diffraction` 衍射 (`fig:diffraction`).
6. `sec:break-dps` 双部分子散射 (`fig:dps`).
7. `sec:break-summary` 小结; closing `tab:break-correspondence` (chapter statement | App O location of the failure | evidence type).

**Canonical statements** (in reading order).

* **定义 `def:break-generalized-tmd` — 标准与广义 TMD 因子化** (no tag) · v1
  - **陈述.** Following RM eqs. (2)–(3): **standard**: process-independent TMDs, up to the known T-reversal sign rule; **generalized**: single-hadron correlators with process- and colour-routing-dependent Wilson-line structures, e.g. BBMP (A11a): $U^{[tt^*]}_{qq}=\frac1{N^2-1}\big[(N^2+1)\frac{{\rm Tr}U^{[\square]}}NU^{[+]}-2U^{[\square]}U^{[+]}\big]$; it contains "no matrix element of the form $\langle H_1H_2|\cdots|H_1H_2\rangle$". References: `Bomhof:2004aw`, `Bomhof:2006dp`, `BacchettaBomhofMuldersPijlman2005`.
  - `\uses{def:tmd-unsub}`

* **命题 `prop:break-measurement` — 测量相容性判据** [R, R_cond] · refdoc S39 [PENDING-VERIFY: X1]
  - **陈述.** 前提：\cref{asm:appO-lcopt}（及 \cref{lem:appO-unitarity}）。If the measurement operator $\Pi$ on cut states commutes with the light-cone evolution $U$ of App O and with the $\tau=0$ insertions, the cut-sum unitarity lemmas (`lem:appO-unitarity`) hold with $\Pi$ inserted. Examples: $\Pi=1$ (inclusive); $\Pi=e^{i\mathbf b\cdot\hat{\mathbf P}_T}$ (TMD DY).
  - **证明.** Full (an operator identity).
  - `\uses{lem:appO-unitarity, asm:appO-lcopt}`

* **注 `rem:break-measurement-failures` — 失效的位置** (no tag) · refdoc S39
  - $\Pi_h$ (identified hadrons in $pp\to h_1h_2X$) and $\Pi_{\rm gap}$ do not commute with $U$; for $pp\to h_1h_2X$ the argument breaks at the one-sided-rewriting step (O-3), with the Glauber region taken relative to the pair $(n_A,w_1)$ ($k\cdot n_A\sim k\cdot w_1\sim\lambda^2$, $k_T$ nearly orthogonal to $w_{1T}$; there $J_1$ depends on $k^-$ at scale $\lambda^2$) (refdoc E29, corrected argument). Used as the organizing criterion of `sec:break-overview`; this locates failures, it is not a new proof of violation.
  - `\uses{prop:break-measurement}`

* **命题 `prop:break-colour` — 单个额外胶子的色因子（胶子极强度）** [R, R_PT] · v1 (+ refdoc S39)
  - **陈述.** The pole parts of the eikonal attachments sum to $P=-\mathbf T_a-2\mathbf T_b$ (all-outgoing charges equivalently $\mathbf T_a+2\mathbf T_b$, VF-REF-16), so that $C_G=1+\frac{2\langle\mathbf T_a\cdot\mathbf T_b\rangle}{C_F}$; checks: SIDIS $+1$, DY $-1$; channel table, exact in $N$: $qq'\to qq'$ ($tt^*$) $\frac{N^2-5}{N^2-1}=\frac12$; $tu^*$ $-\frac{N^2+3}{N^2-1}=-\frac32$; $q\bar q'\to q\bar q'$ ($tt^*$) $-\frac{N^2-3}{N^2-1}=-\frac34$; $q\bar q\to q'\bar q'$ ($ss^*$) $\frac{N^2+1}{N^2-1}=\frac54$; graph by graph (QVY Table I): $C_I/C_u=-\frac2{N^2-1}$, $C_{F1}/C_u=-\frac1{N^2-1}$, $C_{F2}/C_u=\frac{N^2-2}{N^2-1}$ (c_glauber §2.3, [C1–C5]; VF-GLA-6). Warning (refdoc S39, ERR-S2): an "in = out" bookkeeping with a uniform eikonal numerator gives no Sivers flip — exercise.
  - **证明.** Full (colour algebra). Literature: `BacchettaBomhofMuldersPijlman2005` (Table I; eqs. (B5)–(B6)), `QiuVogelsangYuan2007` (eqs. (25)–(28)); closed formula as our derivation [PENDING-VERIFY: N18].
  - `\uses{prop:prelim-wilson-rules, lem:qcd-colour-identities}`

* **例 `ex:break-colour` — 由投影算符得到 $C_G$ 表；阿贝尔极限；纠缠检验** (no tag) · v1
  - `\uses{prop:break-colour}`

* **定理 `thm:break-tmd` — 强子—强子末态强子的 TMD 因子化不成立** [V] · v1 (+ refdoc S39)
  - **陈述.** **Standard TMD factorization fails** for TMD-sensitive observables in $h_1h_2\to H_1H_2X$: `CollinsQiu2007` (SSA, abelian model, one extra gluon: the T-odd coefficient is $g_1+2g_2$, not $g_1$, so no Wilson line of hadron 1 can represent it); `Collins2007` (unpolarized, abelian, two extra gluons; anomaly $4\pi^2g_2(g_2+g_1)\delta(l_1^+)\delta(l_2^+)$, VF-GLA-7). **Generalized TMD factorization fails** in a non-abelian theory (`RogersMulders2010`, double transverse-spin asymmetry): entanglement test $\sum_{X,Y}C(X,Y)=C_F^2+\frac{4T_F^2(N^2-1)}{N^2}\ne C_F^2$ (SU(3): $24/9$ vs $16/9$; c_glauber [C6]; VF-GLA-10) [PENDING-VERIFY: N17]; in the abelian case "actual = product" identically. **Survives** at the orders examined: collinear factorization ($\int d^2k_T(I_1+I_2)=0$). **Not affected:** SIDIS, DY, $e^+e^-\to h_1h_2X$. Further: `Rogers:2013zha`, `Vogelsang:2007jk`. Location in the App O framework: step (O-3) (`rem:break-measurement-failures`).
  - **证明.** Sketch reproducing the eikonal algebra (`ex:break-c07`).
  - **地位与缺口.** Evidence: model calculations of a general method ("if methods fail in the model, they will also fail in QCD", C07); phenomenological size not established; the CQ mechanism could first give uncancelled divergences in partonic cross sections at N$^3$LO.
  - `\uses{prop:break-colour, def:break-generalized-tmd, rem:break-measurement-failures}`

* **例 `ex:break-c07` — Collins 2007 的双胶子反常（阿贝尔标量模型）** (no tag) · v1
  - From c_glauber §2.4: $I_1=\mathcal NF^2$ and $I_2=-\mathcal NG/(k_T^2+m_q^2)$, with closed forms; $b$ space by Parseval, giving $\int d^2k_T(I_1+I_2)=0$; the Cauchy–Schwarz proof that $I_1(0)+I_2(0)<0$ [PENDING-VERIFY: N16]; the typo in C07 eq. (10) (VF-GLA-8) [PENDING-VERIFY: E18 — App Q candidate].
  - `\uses{thm:break-tmd}`

* **命题 `prop:break-spacelike` — 类空共线极限中严格共线因子化的失效** [V] · v1
  - **陈述.** (Amplitude level; critic O16.) For an incoming and an outgoing parton becoming collinear, the one-loop splitting amplitude depends on the colours of the non-collinear partons through $\mathbf T_2\cdot\mathbf T_3$ terms with $i\pi$ (`CataniDeFlorianRodrigo2012` eq. (68)); for $n\ge5$ (four coloured partons in the reduced $2\to2$ amplitude) $\mathbf T_2\cdot\mathbf T_3$ is not proportional to $1$; for three partons it is; the one-loop breaking term is anti-Hermitian and cancels in $2{\rm Re}\langle M_0|M_1\rangle$ (c_glauber §4.1–4.2; VF-GLA-12; order of first violation per level: c_glauber §4.3 table).
  - **地位与缺口.** Evidence: explicit one-loop calculation. **The DY collinear theorem stays [A]** (M21: this does not show that PDF factorization fails).
  - `\uses{prop:sudakov-amplitude-factorization}`

* **例 `ex:break-spacelike` — CdFR 单圈类空劈裂的色结构** (no tag) · v1
  - Structure only.
  - `\uses{prop:break-spacelike}`

* **命题 `prop:break-mass-singularity` — 超出 NNLO 的质量奇异性因子化** [C] · v1
  - **陈述.** Mass singularities of hadron-collider cross sections factorize into PDFs beyond NNLO.
  - **地位与缺口.** CdFR predict possible "entangled" logarithms from N$^3$LO (e.g. small-$Q_T$ dihadron/dijet); `Becher:2024kmk`: three-loop active–active Glauber terms restore consistency with PDF factorization below the veto scale [PENDING-VERIFY: S63-10]; no general statement is proven; status separation as in `prop:jets-sll`; the amplitude-level violation `prop:break-spacelike` ([V]) motivates the question but is not a premise.
  - `\uses{def:pdf-quark, def:pdf-gluon}`

* **命题 `prop:break-fss` — Coulomb 相位与软交换不对易导致的共线因子化破坏** [V] · v1
  - **陈述.** `ForshawSeymourSiodmok2012`: the breakdown in gap-between-jets-type cross sections is driven by the non-commutation of Coulomb/Glauber exchanges with other soft exchanges; colour pattern (c_glauber §4.2; VF-GLA-9, VF-GLA-12, VF-GLA-13): the tripole $\langle M|f_{abc}\mathbf T_i^a\mathbf T_j^b\mathbf T_k^c|M\rangle=0$ for real colour vectors (pure-QCD tree); $\langle M|[A,D]|M\rangle=0$ (no two-loop Coulomb × eikonal term); $\langle M|[D,[D,A]]|M\rangle\ne0$ at three loops (the SLL structure).
  - **地位与缺口.** Evidence: explicit calculation (amplitude/strict-factorization level, three loops); connection `prop:jets-sll`; PDF factorization of the cross sections themselves: [C].
  - `\uses{prop:break-spacelike, prop:jets-sll}`

* **命题 `prop:break-jet-veto` — 对多重部分子相互作用敏感的观测量** [V] · v1
  - **陈述.** `Zeng:2015iba`: explicit counterexample — a leading-power longitudinal spin asymmetry of beam thrust arises from spectator Glauber exchange (QCD with scalar quarks); `Gaunt2014`: for hadronic $E_T$ / transverse thrust, the CSS cancellation breaks down "at the level of two Glauber gluons exchanged between the spectators"; `Schwartz:2018obd`: pure Glauber ladders cancel for single-scale observables, so the leading violation needs at least one soft gluon (Lipatov vertex), i.e. Glauber–soft mixing.
  - **地位与缺口.** Evidence: explicit model counterexample (Zeng); the Gaunt claim is contested by SYZ — never cite Gaunt without SYZ (S58) [PENDING-VERIFY: E36]; which graphs violate first is not settled (c_glauber §1.6 item 3); in the measurement criterion these observables do not commute with the light-cone evolution.
  - `\uses{prop:break-measurement}`

* **定义 `def:break-diffraction` — 衍射 DIS 与衍射部分子分布** (no tag) · v1
  - **陈述.** Kinematics $x_{\mathbb P}$, $\beta$, $t$; $f^D_{i/p}(\beta,x_{\mathbb P},t;\mu)$ is the PDF operator with a detected final-state proton (`Berera:1995fj`); fracture functions `Trentadue:1993ka`.
  - `\uses{def:pdf-quark}`

* **定理 `thm:break-ddis` — 衍射 DIS 的因子化** [A] · v1
  - **陈述.** $d\sigma(\gamma^*p\to p'X)=\sum_i\hat\sigma_i\otimes f^D_{i/p}$ (`Collins1998a`).
  - **非微扰地位.** \cref{asm:intro-bridge}（MA1、MA2）。
  - **证明.** Sketch (Collins 1998 §III; c_glauber §3.2, checks D1a–c; VF-GLA-11). The detected proton belongs to the target subgraph A, whose final state is **constrained**, so the sum over the cuts of A is not available (unlike inclusive DIS); a soft gluon attached to A has its $r^-$ contour trapped (A contains initial- and final-state lines); the proof escapes by deforming $r^+$: near the soft region only final-state current-jet poles constrain $r^+$, A-collinear poles sit at $|r^+|\sim Q$, and the virtual photon has no spectators; Ward identities then factor the soft gluons, and the soft factor cancels in a region unaffected by the diffractive requirement. **Do not write** "one incoming hadron, hence no Glauber problem; final-state interactions summed" (c_glauber §6 item 6).
  - **地位与缺口.** As DIS (`thm:disall-factorization`), plus the $r^+$ deformation argument; fits `H1:2006zyl`.
  - `\uses{def:break-diffraction, thm:method-template, prop:method-glauber-deformation, thm:disall-factorization, asm:intro-bridge}`

* **命题 `prop:break-hh-diffraction` — 强子—强子硬衍射中的因子化破坏** [V] · v1
  - **陈述.** HERA diffractive PDFs overestimate Tevatron diffractive dijets by $O(10)$ (`AffolderEtAl2000`, `CDF:1997gvd` ($W$), `CDF:2012nhl`; see also `CMS:2012odd`); mechanism: spectator interactions fill the gap ("gap survival", `Bjorken:1992er`); unitarity protects only traces, not colour projections; in the dipole toy, singlet→octet leakage is quadratic in the phase difference, with coefficient $C_F/(2N)=\frac29$ (c_glauber §3.3–3.4, checks D2a–f); original proposal `IngelmanSchlein1985`; tests `Alvero:1998ta`; photoproduction analogue `prop:coll-diffractive-photo`.
  - **地位与缺口.** Evidence: experiment (not a perturbative counterexample); the gap projector does not commute with the light-cone evolution (`prop:break-measurement`).
  - `\uses{thm:break-ddis}`

* **定义 `def:break-dpdf` — 双部分子分布与双 Drell–Yan** (no tag) · v1
  - **陈述.** $F_{ij}(x_1,x_2,y)$, with colour, spin and flavour correlations (`DiehlOstermeierSchafer2012`, `Manohar:2012jr`).
  - `\uses{def:pdf-quark}`

* **定理 `thm:break-double-dy` — 双 Drell–Yan 的因子化** [A] · v1 (+ refdoc S39)
  - **陈述.** Double DY factorizes into DPDs and partonic cross sections: Glauber cancellation to all orders, collinear and TMD (`Diehl:2015bca`); soft-gluon factorization (`Diehl:2018wfy`); double counting with single scattering solved (`Diehl:2017kgu`; VF-FRO-13); sum rules (`Diehl:2018kgr`).
  - **非微扰地位.** \cref{asm:intro-bridge}（MA1、MA2）。
  - **地位与缺口.** Open issues (`Diehl:2017wew`): evolution, positivity; the App O structure applies in the same form (refdoc S39; `Diehl:2015bca`).
  - `\uses{def:break-dpdf, thm:dy-factorization, asm:intro-bridge}`

* **猜想 `conj:break-dps-coloured` — 有色末态的双部分子散射** [C] · v1
  - **陈述.** DPS with coloured final states factorizes like double DY.
  - **地位与缺口.** No all-order argument (as `conj:dy-coloured-final`).
  - `\uses{thm:break-double-dy}`

* **猜想 `conj:break-pocket` — "口袋公式" $\sigma_{\rm DPS}=\sigma_A\sigma_B/\sigma_{\rm eff}$** [C] · v1
  - **陈述.** $\sigma_{\rm DPS}=\sigma_A\sigma_B/\sigma_{\rm eff}$ with a process-independent $\sigma_{\rm eff}$.
  - **地位与缺口.** Holds only if correlations and the $1\to2$ splitting are neglected; a model assumption, not a consequence of `thm:break-double-dy` (`Diehl:2017wew`, `Gaunt:2009re`, `Blok:2011bu`).
  - `\uses{def:break-dpdf}`

**Worked examples.** `ex:break-colour`, `ex:break-c07`, `ex:break-spacelike`.

**Tables.** `tab:break-cases` (above); `tab:break-correspondence` (refdoc S45.2): `thm:break-tmd`, `prop:break-jet-veto`, `prop:break-hh-diffraction` ↔ location of the failure in App O (step (O-3); measurement non-commuting) [SYNC-APP].

**Figures.** Existing (tikz3, final): `fig:violation-cq`, `fig:diffraction`, `fig:dps`; optional new: `fig:break-spacelike`, `fig:break-measurement`.

**Misconception box.** M7, M21; "diffractive PDFs are universal" (only for DDIS); critic C8; O16, O17.

**Key citation keys.** `CollinsQiu2007`, `Collins2007`, `RogersMulders2010`, `Rogers:2013zha`, `Vogelsang:2007jk`, `Bomhof:2004aw`, `Bomhof:2006dp`, `BacchettaBomhofMuldersPijlman2005`, `QiuVogelsangYuan2007`, `AybatSterman2009`, `RothsteinStewart2016`, `CataniDeFlorianRodrigo2012`, `ForshawSeymourSiodmok2012`, `ForshawKyrieleisSeymour2006`, `Becher:2021zkk`, `Becher:2024kmk`, `Gaunt2014`, `Zeng:2015iba`, `Schwartz:2018obd`, `Collins1998a`, `Berera:1994xh`, `Berera:1995fj`, `Trentadue:1993ka`, `IngelmanSchlein1985`, `AffolderEtAl2000`, `CDF:1997gvd`, `CDF:2012nhl`, `CMS:2012odd`, `H1:2006zyl`, `H1:2007jtx`, `ZEUS:2007uvk`, `Bjorken:1992er`, `Alvero:1998ta`, `Collins:1992cv`, `Landshoff:1971zu`, `DiehlOstermeierSchafer2012`, `Diehl:2015bca`, `Diehl:2017kgu`, `Diehl:2018wfy`, `Diehl:2018kgr`, `Diehl:2017wew`, `Manohar:2012jr`, `Manohar:2012pe`, `Blok:2011bu`, `Gaunt:2009re`, `Buffing:2017mqm`, `DoriaFrenkelTaylor1980`, `Frenkel:1983di`, `Brandt:1988xt`.

**Pending.** [PENDING-VERIFY: X1] (`prop:break-measurement`, failure locations); [N16, N17, N18] (attribution of the derived formulas); [E18] (C07 typo); [E36] (Gaunt vs SYZ wording); [S63-10] (`Becher:2024kmk`).

---------------------------------------------------------------------------------------------------

# 第五部分 其他硬过程 (Part V — Other hard processes)

---------------------------------------------------------------------------------------------------

## Chapter 19 — 硬遍举过程 / Hard exclusive processes

`\label{ch:excl}` · `ch19_excl.tex` · **11 pp** · short format · Part V

**Purpose.** Amplitude-level factorization with distribution amplitudes (DAs) and generalized parton distributions (GPDs): definitions, ERBL evolution, polynomiality; the integrand-level cancellation of soft gluons for colour-singlet meson jets under endpoint conditions (refdoc S40); the pion electromagnetic and transition form factors; DVCS and longitudinal-photon meson production [A]; the endpoint problem and soft overlap [P]; the failure of standard collinear factorization for transverse photons [V] with the correct mechanism (critic O18); near-threshold heavy-quarkonium photoproduction as a new factorization regime [P] (WRITER_SPEC_v2 §12.2).

**Conventions (this chapter).** $n_A=(1^+,0^-,0_T)$, $n_B=(0^+,1^-,0_T)$, **not** $\bar n,n$ (reserved for Ch15); c_exclusive's $\bar n$ is our $n_A$, its $n$ is our $n_B$; $g_\perp^{\mu\nu}=g^{\mu\nu}-n_A^\mu n_B^\nu-n_B^\mu n_A^\nu$, $\epsilon_\perp^{\mu\nu}=\epsilon^{\mu\nu\rho\sigma}n_{A\rho}n_{B\sigma}$, $\epsilon_\perp^{12}=+1$ (VF-CONV-10; VGG use $\varepsilon_{0123}=+1$); $f_\pi\approx130$ MeV ($F_\pi=f_\pi/\sqrt2$); Ji's $\xi_{\rm Ji}=2\xi$.

**Depends on.** Ch4 (endpoint regions), Ch7 (`def:dis-compton`), Ch8 (operator definitions, light-ray operators), Ch9 (collinear Wilson lines, `thm:method-template`); App N §N.6 [SYNC-APP].

**Box.**
- 证明了：`prop:excl-erbl`、`prop:excl-pion-lo`、`prop:excl-dvcs-lo`（[R, R_PT]）；`prop:excl-polynomiality`（[R, R_def]）；`prop:excl-soft-cancel`（[R, R_cond]，前提 `asm:appN-endpoint`、`asm:appN-collins`）。
- 给出全阶论证：`thm:excl-pion-ff`、`thm:excl-transition`、`thm:excl-dvcs`、`thm:excl-meson-L`（[A]）。
- 没有证明：端点区与软重叠的大小（`prop:excl-endpoint`，[P]）；横向光子的标准共线因子化（`prop:excl-meson-T`，[V]）；近阈重夸克偶素光生超出 LO（`prop:excl-near-threshold`，[P]）。

**Sections.** `sec:excl-da` 分布振幅与 ERBL 演化 (optional `fig:excl-erbl`); `sec:excl-soft` 色单态介子：软胶子在被积函数层次的相消 (**new**, refdoc S40); `sec:excl-ff` 介子形状因子 (`fig:pion-ff`); `sec:excl-endpoint` 端点区域与软重叠 (optional `fig:excl-endpoint`); `sec:excl-gpd` 广义部分子分布 (`fig:dvcs-handbag`); `sec:excl-dvcs` DVCS 与介子产生 (`fig:meson-production`); `sec:excl-threshold` 近阈重夸克偶素光生 (**new**); closing `tab:excl-correspondence`.

**Canonical statements** (in reading order).

* **定义 `def:excl-da` — 介子分布振幅** (no tag) · v1
  - **陈述.** $\langle0|\bar d(z)\gamma^+\gamma_5W[z,-z]u(-z)|\pi^+(p)\rangle=if_\pi p^+\int_0^1dx\,e^{i(2x-1)p^+z^-}\phi_\pi(x)$, $z=(0^+,z^-,0_T)$, $x$ the $u$-quark momentum fraction; $\int\phi_\pi=1$; moments are local twist-2 axial operators; Gegenbauer expansion $\phi_\pi=6x\bar x\sum_na_nC_n^{3/2}(2x-1)$ (VF-EXC-1, VF-EXC-2; `Braun:2003rp` eq. (140) after translation).
  - `\uses{def:prelim-wilson, def:prelim-gamma5}`

* **命题 `prop:excl-erbl` — 单圈 ERBL 演化** [R, R_PT] · v1
  - **陈述.** (One loop.) $\mu^2\partial_{\mu^2}\phi=\frac{\alpha_s}{2\pi}V_0\otimes\phi$, $V_0(x,y)=C_F[\frac xy(1+\frac1{y-x})\theta(y-x)+\frac{\bar x}{\bar y}(1+\frac1{x-y})\theta(x-y)]_+$; Gegenbauer polynomials are eigenfunctions (proof for all $n$); $\gamma_n=2C_F[1-\frac2{(n+1)(n+2)}+4\sum_{j=2}^{n+1}\frac1j]$, so $a_n\propto\alpha_s^{\gamma_n/(2\beta_0)}$; $\gamma_0=0$, $\gamma_2=\frac{25}3C_F$; eigenvalues = DGLAP non-singlet moments at $N=n+1$; asymptotic DA $6x\bar x$ (VF-EXC-3/4/5). NLO ERBL is [R] at fixed order in the literature (`Braun:2003rp` §5), not redone here.
  - **非微扰地位.** 强子 DA：\cref{asm:intro-wightman}、\cref{asm:intro-composite}（MA0）。
  - **证明.** Full (c_exclusive §3).
  - `\uses{def:excl-da, prop:pdf-lo-kernels, asm:intro-wightman, asm:intro-composite}`

* **命题 `prop:excl-soft-cancel` — 色单态介子的软胶子在被积函数层次相消** [R, R_cond] · refdoc S40 [PENDING-VERIFY: X2]
  - **陈述.** 前提：\cref{asm:appN-endpoint}、\cref{asm:appN-collins}。For the pion form factor and the meson side of $\gamma_L^*$ meson production, soft gluons attached to the colour-singlet meson jets cancel at the integrand level; the cancellation is the smallness of the soft-approximation error for a small colour dipole (colour transparency: the Wilson-line pair of a dipole of size $b$ is $1+O(b\Lambda)$). The endpoint conditions (E1)–(E3) of `asm:appN-endpoint` are the hypotheses; the argument fails for twist 3 and for transverse photons, where they are violated.
  - **证明.** Full given the assumptions (App N §N.6).
  - `\uses{def:excl-da, def:method-soft-approx, asm:appN-endpoint, asm:appN-collins}`

* **定理 `thm:excl-pion-ff` — 介子电磁形状因子的因子化** [A] · v1 (+ refdoc S40)
  - **陈述.** At leading power: $F_\pi(Q^2)=\int dx\,dy\,\phi_\pi^*(y,\mu)T_H(x,y,Q,\mu)\phi_\pi(x,\mu)+O(\frac{\Lambda^2}{Q^4}\ln\frac{Q^2}{\Lambda^2})$ (remainder with the logarithm from the endpoint-area estimate, ERR-m15 correction); Gegenbauer remark: the endpoint conditions hold for every finite truncation.
  - **非微扰地位.** \cref{asm:intro-bridge}（MA1、MA2）。
  - **地位与缺口.** Literature: `Lepage:1979zb`, `LepageBrodsky1980`, `EfremovRadyushkin1980`, `Efremov:1978rn`, `Duncan:1979ny`, `Duncan:1979hi`, `Chernyak:1977as`, `ChernyakZhitnitsky1984`, `Farrar:1979aw`. Bottlenecks `asm:appN-endpoint`, `asm:appN-collins`, `asm:intro-bridge`; at accessible $Q^2$, endpoint and soft-overlap contributions may dominate (`prop:excl-endpoint`).
  - `\uses{def:excl-da, prop:excl-soft-cancel, thm:method-template, asm:appN-endpoint, asm:intro-bridge}`

* **命题 `prop:excl-pion-lo` — 领头阶硬核** [R, R_PT] · v1
  - **陈述.** (Tree level.) $T_H=\frac{2\pi C_F\alpha_sf_\pi^2}{N_cQ^2}\big[\frac{e_u}{\bar x\bar y}+\frac{e_{\bar d}}{xy}\big]$; for a general DA $Q^2F_\pi=\frac{2\pi C_F}{N_c}\alpha_sf_\pi^2[e_u|\int\frac\phi{\bar x}|^2+e_{\bar d}|\int\frac\phi x|^2]$; asymptotic limit $Q^2F_\pi\to8\pi\alpha_sf_\pi^2$; exactly four $O(\alpha_s)$ graphs in Feynman gauge; only the pairs A+B and C+D are gauge invariant (c_exclusive §10 item 3) (VF-EXC-6).
  - **证明.** Full (worked example).
  - `\uses{def:excl-da, def:prelim-feynman-rules, lem:appA-fierz}`

* **例 `ex:excl-pion-ff-lo` — 领头阶 $\pi$ 形状因子** (no tag) · v1
  - The four graphs, the Fierz projectors (App A `lem:appA-fierz`), the hard kernel, and the asymptotic limit $8\pi\alpha_sf_\pi^2$ (c_exclusive §4; `tex/c_exclusive_formfactors.tex` is a ready draft).
  - `\uses{prop:excl-pion-lo}`

* **定理 `thm:excl-transition` — $\gamma^*\gamma\to\pi^0$ 形状因子** [A] · v1
  - **陈述.** $Q^2F_{\gamma^*\gamma\pi}=\frac{\sqrt2f_\pi}3\int_0^1dx\frac{\phi_\pi(x)}x+O(\alpha_s)\to\sqrt2f_\pi$ (VF-EXC-7; BaBar normalization); NNLO `Gao:2021iqq`; data `CELLO:1990klc`, `CLEO:1997fho`, `BaBar:2009rrj`, `Belle:2012wwz`.
  - **非微扰地位.** \cref{asm:intro-bridge}（MA1、MA2）。
  - **地位与缺口.** All-order argument (one meson; no soft-overlap issue at leading power); power corrections not controlled.
  - `\uses{def:excl-da, thm:method-template, asm:intro-bridge}`

* **命题 `prop:excl-endpoint` — 端点区域与软重叠** [P] · v1 (+ refdoc S40)
  - **陈述.** The soft (Feynman) mechanism competes numerically at accessible $Q^2$ (`IsgurLlewellynSmith1984`, `Isgur:1988iw`; exact soft fractions VF-EXC-14 [PENDING-VERIFY: N21]); its formal power counting is $1/Q^4$; the Sudakov/$k_T$ resummation scheme (`LiSterman1992`) is model dependent; colour transparency (the Wilson-line pair of a small dipole is $1+O(b\Lambda)$) and the endpoint-area estimate $c(1-\ln c)$, combined with the exact $R_{\rm as}(c)$ curves (c_exclusive) (refdoc S40, T24).
  - **地位与缺口.** Established in models and at fixed order; no QCD bound on the soft overlap.
  - `\uses{thm:excl-pion-ff}`

* **定义 `def:excl-gpd` — 广义部分子分布** (no tag) · v1
  - **陈述.** Ji's $H,E,\tilde H,\tilde E$ in the light-front normalization of `Diehl2003`; kinematics $\xi$, $t$; forward limits $H(x,0,0)=q(x)$, $\tilde H(x,0,0)=\Delta q(x)$. References `Ji1997a`, `Ji1997b`, `Radyushkin:1996nd`, `Radyushkin1997`, `Diehl2003`, `BelitskyRadyushkin2005`.
  - `\uses{def:pdf-quark, def:pdf-lightray}`

* **命题 `prop:excl-polynomiality` — 多项式性与 Ji 求和规则** [R, R_def] · v1
  - **陈述.** $\int dx\,H=F_1(t)$; $\int dx\,xH=A(t)+4\xi^2C(t)$; $\int dx\,x(H+E)=A+B$, hence $J^q=\frac12[A^q(0)+B^q(0)]$; D-term `Polyakov:1999gs` (VF-EXC-12).
  - **非微扰地位.** \cref{asm:intro-wightman}、\cref{asm:intro-composite}（MA0）。
  - **证明.** Full (Lorentz covariance of local matrix elements).
  - `\uses{def:excl-gpd, asm:intro-wightman, asm:intro-composite}`

* **定理 `thm:excl-dvcs` — DVCS 的因子化** [A] · v1
  - **陈述.** DVCS amplitudes factorize at leading power into GPDs and perturbative coefficient functions (`CollinsFreund1999`, `JiOsborne1998`).
  - **非微扰地位.** \cref{asm:intro-bridge}（MA1、MA2）。
  - **地位与缺口.** Per Collins–Freund, the issues are the collinear region (Ward identities → Wilson line) and the endpoint/breakpoint regions $x=\pm\xi$; do **not** say that "soft gluons cancel by Ward identities" (c_exclusive §10 item 11); GPDs at $x=\pm\xi$ are a frontier question (Ch22, pointer).
  - `\uses{def:excl-gpd, thm:method-template, asm:intro-bridge}`

* **命题 `prop:excl-dvcs-lo` — DVCS 领头阶系数函数** [R, R_PT] · v1
  - **陈述.** (Tree level.) $$T^{\mu\nu}=g_\perp^{\mu\nu}\sum_qe_q^2\!\int\!dx\,F^q\Big[\frac1{x-\xi+i0}+\frac1{x+\xi-i0}\Big]-i\epsilon_\perp^{\mu\nu}\sum_qe_q^2\!\int\!dx\,\tilde F^q\Big[\frac1{x-\xi+i0}-\frac1{x+\xi-i0}\Big];$$ the overall sign is tied to the definition of $T^{\mu\nu}$ in `def:dis-compton`; DIS-limit check ${\rm Im}\,T^{11}=2\pi F_1$ (VF-EXC-8/9/10). Ji's arXiv v1 prints the second denominator as "$x+\xi/2+i\epsilon$"; the correct sign is $-i0$ (c_exclusive §10 item 4) [PENDING-VERIFY: E20 — App Q candidate].
  - **证明.** Full.
  - `\uses{def:excl-gpd, def:dis-compton, def:prelim-feynman-rules}`

* **定理 `thm:excl-meson-L` — 纵向光子介子产生的因子化** [A] · v1 (+ refdoc S40)
  - **陈述.** (`CollinsFrankfurtStrikman1997`.) Leading order, pseudoscalar case: $\varepsilon_L\cdot A_\pi=-i\frac{C_F}{N_c}\frac{4\pi\alpha_sf_\pi}Q\int dz\,\phi_\pi(z)\int dx\big[\frac{e_a}{\bar z(x-\xi+i0)}+\frac{e_b}{z(x+\xi-i0)}\big]\tilde F^{ba}$ (VF-EXC-11; agrees with VGG eqs. (48), (59)); further `Vanderhaeghen:1999xj`, `Mankiewicz:1997uy`, `Frankfurt:1999fp` (the pion pole of $\tilde E$; **not** PRL 84 (2000) 2589).
  - **非微扰地位.** \cref{asm:intro-bridge}（MA1、MA2）。
  - **地位与缺口.** Bottlenecks `asm:appN-endpoint`, `asm:appN-collins`, `asm:intro-bridge` (refdoc S40).
  - `\uses{def:excl-da, def:excl-gpd, prop:excl-soft-cancel, thm:method-template, asm:appN-endpoint, asm:appN-collins, asm:intro-bridge}`

* **命题 `prop:excl-meson-T` — 横向光子：标准共线因子化失效** [V] · v1 (+ refdoc S40, ERR-M17)
  - **陈述.** (a) The leading-twist $\gamma_T^*\to V_T$ amplitude vanishes to all orders by chirality and helicity conservation ([A]; `Diehl:1998pd`, `CollinsDiehl2000`). (b) At twist 3, in the Wandzura–Wilczek approximation, the integrals diverge **logarithmically** at the endpoints, because $g_\perp^{(v)}(0)=\frac12\int du\,\phi_\parallel(u)/u\ne0$ (VF-REF-15, status T); endpoint suppression of $\phi_\parallel$ does not help; the GPD convolutions also have double poles $(\xi\mp x-i0)^{-2}$ (`Mankiewicz:1999tt`).
  - **地位与缺口.** Evidence: explicit calculation (twist-3 WW); do not quote MP's "$9/\tau$" [PENDING-VERIFY: E21]; never write 「横向光子失效源于 $\int\phi/z^2$ 型发散」 (S58); NLO claims that omit collinear subtractions [PENDING-VERIFY: E22]; phenomenological models `Goloskokov:2005sd`.
  - `\uses{thm:excl-meson-L}`

* **注 `rem:excl-hadron-scattering` — 宽角强子散射** (no tag) · v1
  - Constituent counting (`BrodskyFarrar1973`), the Landshoff pinch (`Landshoff:1974ew`), and its Sudakov suppression (`Botts:1989kf`) are all [P].

* **命题 `prop:excl-near-threshold` — 近阈重夸克偶素光生（重夸克极限）** [P] · new (WRITER_SPEC_v2 §12.2; frontier YZLIU §3.F1)
  - **陈述.** (LO in $\alpha_s(M_V)$, NRQCD at LO, $M_V\to\infty$.) Near threshold ($\xi=1+O(M_N/M_V)$, $-t\sim M_NM_V$): $\mathcal M=\frac{8\sqrt2\pi\alpha_s(M_V)}{M_V^2}\phi^*(0)\,G(t,\xi)\,(\varepsilon_V^*\cdot\varepsilon)$, $G=\frac1{2\xi}\int_{-1}^1dx\,A(x,\xi)F_g(x,\xi,t)$, $A=\frac1{x+\xi-i0}-\frac1{x-\xi+i0}$; at $\xi\to1$ the spin-2 (gluonic gravitational form factor) moments dominate; cross section and $|G|^2$ as in VF-YZL-15 (corrected normalization of `Guo:2023pqw`; the 2021 definition of `Guo:2021ibg` had a spurious factor $\frac12$ in the gluon GPD, corrected by the authors — cite where used, not an App Q row [PENDING-VERIFY: E12]).
  - **地位与缺口.** [P]: LO two-gluon exchange; the persistence of all-order GPD factorization of the high-energy region (`Ivanov:2004vd`) at threshold is argued, not proven; the spin-2 truncation requires large $|t|$ and $\xi$.
  - **Remark.** $\phi(0)$ is the non-relativistic wave function at the origin in the normalization of VF-YZL-15; NRQCD itself is introduced in Ch20 (`def:heavy-nrqcd`, forward pointer, not a dependency: only the LO normalization constant enters).
  - `\uses{def:excl-gpd}`

**Worked example.** `ex:excl-pion-ff-lo`.

**Tables.** `tab:excl-correspondence` (refdoc S45.2): `prop:excl-soft-cancel`, `thm:excl-pion-ff`, `thm:excl-meson-L` ↔ App N §N.6 (`asm:appN-endpoint`) [SYNC-APP].

**Figures.** Existing (tikz3, final): `fig:pion-ff`, `fig:dvcs-handbag`, `fig:meson-production`; optional new: `fig:excl-erbl`, `fig:excl-endpoint`.

**Misconception box.** Critic O18 (transverse photons); "soft gluons cancel by Ward identities in DVCS" (no: Collins–Freund).

**Key citation keys.** `Lepage:1979zb`, `LepageBrodsky1980`, `EfremovRadyushkin1980`, `Efremov:1978rn`, `Duncan:1979ny`, `Duncan:1979hi`, `Chernyak:1977as`, `ChernyakZhitnitsky1984`, `Farrar:1979aw`, `Brodsky:1980ny`, `Brodsky:1981rp`, `Braun:2003rp`, `IsgurLlewellynSmith1984`, `Isgur:1988iw`, `LiSterman1992`, `BrodskyFarrar1973`, `Landshoff:1974ew`, `Botts:1989kf`, `CELLO:1990klc`, `CLEO:1997fho`, `BaBar:2009rrj`, `Belle:2012wwz`, `Gao:2021iqq`, `Ji1997a`, `Ji1997b`, `Ji:1998pc`, `Radyushkin:1996nd`, `Radyushkin1997`, `Diehl2003`, `BelitskyRadyushkin2005`, `Goeke:2001tz`, `Belitsky:2001ns`, `Polyakov:1999gs`, `CollinsFreund1999`, `JiOsborne1998`, `CollinsFrankfurtStrikman1997`, `Vanderhaeghen:1999xj`, `Mankiewicz:1997uy`, `Frankfurt:1999fp`, `Diehl:1998pd`, `CollinsDiehl2000`, `Mankiewicz:1999tt`, `Goloskokov:2005sd`, `Diehl:1998sm`, `Guo:2021ibg`, `Guo:2023pqw`, `Ivanov:2004vd`.

**Pending.** [PENDING-VERIFY: X2] (`prop:excl-soft-cancel`); [N21]; [E20, E21, E22, E12].

---------------------------------------------------------------------------------------------------

## Chapter 20 — 重夸克物理：$B$ 介子衰变与重夸克偶素 / Heavy-quark physics: $B$ decays and quarkonium

`\label{ch:heavy}` · `ch20_heavy.tex` · **10 pp** · short format · Part V

**Purpose.** Factorization with a heavy-quark scale: exclusive $B\to D\pi$ [A]; the heavy-to-light form factor at large recoil (soft overlap + hard spectator) [A] (refdoc S41); QCD factorization (QCDF) for charmless $B\to M_1M_2$ — leading power [P] with all-order arguments, power corrections [V], the $X_A,X_H$ models; inclusive $B$ decays: the OPE in $1/m_b$ and the shape-function region; quarkonium: NRQCD decays [A] (non-perturbatively local duality is needed), production [C] (NQS: gauge completion necessary at NNLO), large-$p_T$ two-step factorization. Quarkonium and NLP endpoint updates: Ch24 (pointer).

**Depends on.** Ch7 (OPE), Ch15 (SCET, BPS decoupling), Ch19 (DAs); Ch6 (`conj:ee-duality`).

**Box.**
- 证明了：`prop:heavy-nrqcd-matching`（[R, R_PT]，单圈）。
- 给出全阶论证：`thm:heavy-bdpi`、`prop:heavy-btopi-ff`、`thm:heavy-inclusive-b`、`thm:heavy-nrqcd-decay`、`prop:heavy-quarkonium-fragmentation`（[A]）。
- 部分/猜想/破坏：`prop:heavy-qcdf-lp`（[P]）、`conj:heavy-nrqcd-production`（[C]）、`prop:heavy-qcdf-endpoint`（[V]）。

**Sections.** `sec:heavy-bdpi` $B\to D\pi$ (`fig:heavy-bdpi`); `sec:heavy-qcdf` 重到轻形状因子与无粲 $B$ 衰变的 QCD 因子化 (`fig:heavy-qcdf`); `sec:heavy-inclusive` 单举 $B$ 衰变; `sec:heavy-nrqcd` 重夸克偶素：NRQCD (`fig:nrqcd`).

**Canonical statements** (in reading order).

* **定理 `thm:heavy-bdpi` — $B\to D\pi$ 的全阶因子化** [A] · v1
  - **陈述.** At leading power and all orders in $\alpha_s$: $\langle D\pi|O|B\rangle=N\,F^{B\to D}(0)\int_0^1dx\,T(x,\mu)\phi_\pi(x,\mu)$, with $N=\frac i2m_BE_\pi f_\pi$ for $O_{\bf0}=[\bar c\gamma^\mu P_Lb][\bar d\gamma_\mu P_Lu]$, $P_L=\frac12(1-\gamma_5)$ ($O_{\bf8}$ with $T^a\otimes T^a$; VF-BQ-6), for $\bar B^0\to D^+\pi^-$ and $B^-\to D^0\pi^-$; BPS write $F^{B\to D}(0)$, not $F(m_\pi^2)$ (difference power suppressed); the endpoint-suppression **assumption** is part of the statement (c_scet §6 item 7).
  - **非微扰地位.** \cref{asm:intro-bridge}（MA1、MA2）。
  - **地位与缺口.** Literature: `BauerPirjolStewart2001`; two-loop IR demonstration `BenekeEtAl2000` (which "does not accomplish an all-order 'proof'"); NNLO kernel `Huber:2016xod`; colour transparency `Bjorken:1988kk`, `Dugan:1990de`, `Politzer:1991au`; SCET premises (`rem:scet-assumptions`).
  - `\uses{def:excl-da, thm:scet-decoupling, asm:intro-bridge}`

* **命题 `prop:heavy-btopi-ff` — 重到轻形状因子：软重叠与硬旁观者** [A] · refdoc S41 (corrects ERR-M21 of literature-style presentations)
  - **陈述.** At leading power in $\Lambda/m_b$ and large recoil, $F^{B\to\pi}=C(E)\,\xi_\pi(E)+\int T\,\phi_B\,\phi_\pi$ (soft overlap + hard spectator), to all orders in $\alpha_s$ (`Bauer:2002aj`, `Beneke:2003pa`).
  - **非微扰地位.** \cref{asm:intro-bridge}（MA1、MA2）。
  - **地位与缺口.** All-order SCET argument; the further factorization of $\xi_\pi$ fails (endpoint divergences, `prop:heavy-qcdf-endpoint`).
  - `\uses{def:excl-da, thm:scet-decoupling, asm:intro-bridge}`

* **命题 `prop:heavy-qcdf-lp` — 无粲两体衰变的领头幂次 QCD 因子化** [P] · v1 (+ refdoc S41)
  - **陈述.** (BBNS) $\langle M_1M_2|Q_i|\bar B\rangle=F^{B\to M_1}(0)\int dx\,T^{\rm I}_i(x)\phi_{M_2}(x)+\int d\xi\,dx\,dy\,T^{\rm II}_i(\xi,x,y)\phi_B(\xi)\phi_{M_1}(y)\phi_{M_2}(x)$; one-loop vertex term $V_M=12\ln\frac{m_b}\mu-18+\int_0^1g\,\Phi_M$ (the 12 forced by $\mu$-independence; $\int g\Phi_M=-\frac12-3i\pi+(\frac{11}2-3i\pi)\alpha_1^M-\frac{21}{20}\alpha_2^M$; VF-BQ-1/2); IR finiteness established explicitly through NNLO for $T^{\rm I}$ (`Bell:2007tv`, `Bell:2009nk`, `Beneke:2009ek`; penguins `Bell:2015koa`, `Bell:2020qus`) and at one loop for $T^{\rm II}$ (`Beneke:2005vv`, `Beneke:2006mk`, `Kivel:2006xc`, `Pilipp:2007mg`; jet function `Beneke:2005gs`).
  - **非微扰地位.** \cref{asm:intro-bridge}（MA1、MA2）。
  - **地位与缺口.** Tag [P] (survey item 18, more conservative than critic O19's [A]); SCET LP derivations: `Bauer:2004tj` (BPRS, with the charming-penguin caveat) and Chay–Kim (`Chay:2003ju`) [PENDING-VERIFY: S63-11], with `Beneke:2003pa`, `Hill:2002vw`; the open BBNS–BPRS dispute on charming penguins is reported without a verdict (`Beneke:2004bn` vs `Bauer:2005wb`); never write 「BBNS 只在 $O(\alpha_s)$ 成立」 (S58).
  - `\uses{prop:heavy-btopi-ff, def:excl-da, asm:intro-bridge}`

* **命题 `prop:heavy-qcdf-endpoint` — 幂次修正中的端点发散** [V] · v1
  - **陈述.** The annihilation and twist-3 spectator terms are divergent convolutions at $O(\alpha_s)$: $X_A=\int_0^1\frac{dy}y$, $X_H=\int_0^1\frac{dy}{1-y}\Phi_p(y)$; the model $X=(1+\varrho e^{i\varphi})\ln\frac{m_B}{\Lambda_h}$, $\varrho\le1$, $\Lambda_h=0.5$ GeV is a **model** (VF-BQ-3/4; `BenekeNeubert2003`; the printed "$\ln(m_M/\Lambda_h)$" must read $m_B$, c_scet §6 item 17 [PENDING-VERIFY: E26]); annihilation coefficients VF-BQ-5 (prescription dependence of the model illustrated [PENDING-VERIFY: N22]).
  - **地位与缺口.** Evidence: explicit calculation (divergent convolutions); refactorization of these endpoint divergences is [C] (case-by-case successes elsewhere: `Liu:2019oav`, `Liu:2020wbn`, `Liu:2022ajh`, `Hurth:2023paz`; attempts for annihilation `Lu:2022kos`); colour-suppressed $B\to D^0M^0$: `Mantry:2003uz`.
  - `\uses{prop:heavy-qcdf-lp}`

* **定理 `thm:heavy-inclusive-b` — 单举 $B$ 衰变的重夸克展开** [A] · v1
  - **陈述.** OPE in $1/m_b$ for total and inclusive semileptonic rates, as an asymptotic expansion of the rates smeared over the hadronic energy release, with no $1/m_b$ term (`ChayGeorgiGrinstein1990`, `BigiUraltsevVainshtein1992`, `ManoharWise1994`, `BigiEtAl1994`); in the endpoint/shape-function region: factorization into hard × jet × shape function (`Neubert1994a`, `Neubert1994b`, `KorchemskySterman1994`, `BauerFlemingLuke2000`, `Bauer:2003pi`, `Lange:2003ff`, `Becher:2006qw`).
  - **非微扰地位.** \cref{asm:intro-wightman}、\cref{asm:intro-composite}、\cref{asm:intro-af-coeff}（MA0、MA4）；端点（形状函数）区的因子化另需 \cref{asm:intro-bridge}（MA1、MA2）。
  - **地位与缺口.** All-order status that of the OPE (`thm:dis-ope`, [A]) and, in the shape-function region, of the SCET factorization (premises `rem:scet-assumptions`). Applying the expansion to the physical rate at fixed kinematics needs local quark–hadron duality ([C], `conj:ee-duality`), which is not a premise of the statement as formulated (pointer); pole-mass renormalon: `Bigi:1994em`, `Beneke:1994sw`.
  - `\uses{thm:dis-ope, thm:scet-decoupling, asm:intro-wightman, asm:intro-composite, asm:intro-af-coeff, asm:intro-bridge}`

* **定义 `def:heavy-nrqcd` — NRQCD 及其幂次计数** (no tag) · v1
  - **陈述.** Velocity rules: $\psi\sim(mv)^{3/2}$, $D\sim mv$, $D_t\sim mv^2$, $gE\sim m^2v^3$, $gB\sim m^2v^4$ (VF-NRQ-1; `CaswellLepage1986`, `BodwinBraatenLepage1995` §II); BBL use $D=\partial+igA$, so the signs of the $c_{2,3,4}$ bilinears flip under our convention (c_scet §6 item 9).
  - `\uses{def:prelim-qcd}`

* **定理 `thm:heavy-nrqcd-decay` — 衰变的 NRQCD 因子化** [A] · v1 (+ refdoc S41)
  - **陈述.** $\Gamma=\sum_n\frac{2{\rm Im}f_n}{m_Q^{d_n-4}}\langle H|O_n|H\rangle$, $m_Q$ the heavy-quark pole mass (BBL §II.F–G; P-wave consistency `Bodwin:1992ye`).
  - **非微扰地位.** \cref{asm:intro-bridge}（MA1、MA2）；非微扰地还需局域对偶（`conj:ee-duality`）。
  - **地位与缺口.** Perturbatively [A] (BBL; NRQCD cutoff dependence of $f_n$ and $\langle O_n\rangle$); non-perturbatively the decay rate needs local duality, since it is Minkowskian at a fixed point and not covered by the OPE assumptions (refdoc S41, ERR-M9); never write 「NRQCD 衰变因子化与 OPE 同样严格」 (S58).
  - `\uses{def:heavy-nrqcd, asm:intro-bridge}`

* **命题 `prop:heavy-nrqcd-matching` — 匹配系数** [R, R_PT] · v1
  - **陈述.** (One loop.) $\Gamma(^3S_1\to e^+e^-)=\frac{N_ce_Q^2\alpha^2|R(0)|^2}{3m_Q^2}$; $\Gamma(^1S_0\to\gamma\gamma)=\frac{4N_ce_Q^4\alpha^2|R(0)|^2}{M^2}$, $M=2m_Q$; $c_v=1-2C_F\frac{\alpha_s}\pi$, so $\Gamma(V\to e^+e^-)\propto1-\frac{16\alpha_s}{3\pi}$ (VF-NRQ-2/3/4; `VanRoyen:1967nq`, `Barbieri:1975ki`, `Celmaster:1978yz`, `Barbieri:1979be`).
  - **证明.** Full at one loop (`ex:heavy-cv`, which follows; App G).
  - `\uses{def:heavy-nrqcd, def:prelim-msbar}`

* **例 `ex:heavy-cv` — 阈值处的单圈 $c_v$** (no tag) · v1
  - Vertex $a(\frac3\varepsilon-4+3\ln\frac{\mu^2}{m^2})$; $\delta Z_2^{\rm OS}=-a(\frac3\varepsilon+4+3\ln\frac{\mu^2}{m^2})$; the Coulomb singularity is separated and matched by the NRQCD potential (c_scet `s3`; check against BBL App. A).
  - `\uses{prop:heavy-nrqcd-matching}`

* **猜想 `conj:heavy-nrqcd-production` — 产生的 NRQCD 因子化** [C] · v1 (+ refdoc S41)
  - **陈述.** $\sigma=\sum_nF_n\langle O_n^H\rangle/m_Q^{d_n-4}$ (BBL §VI.A), for all inclusive production with $m_Q$ hard, order by order in $v$.
  - **地位与缺口.** At NNLO, IR poles appear that conventional octet operators do not match: NQS find uncancelled NNLO poles $\propto\alpha_s^2v^2/\varepsilon$, generated exactly by the gauge-completed octet operators — the Wilson lines are **necessary** at NNLO (relative order $v^2$) ([P]: `NayakQiuSterman2005a`, `NayakQiuSterman2005b`, `NayakQiuSterman2006`); beyond NNLO new non-local operators may be needed; universality and polarization tensions (`Butenschoen:2010rq`, `Butenschoen:2011yh`, `Butenschoen:2012px`, `Chao:2012iv`, `BrambillaEtAl2011`, `Lansberg:2019adr`); updates: Ch24 (pointer). Never write 「NQS 的规范完备 Wilson 线在 NNLO 不改变结果」 (S58).
  - `\uses{def:heavy-nrqcd}`

* **命题 `prop:heavy-quarkonium-fragmentation` — 大 $p_T$ 重夸克偶素产生** [A] · v1
  - **陈述.** Leading-power plus NLP factorization in $m_Q^2/p_T^2$ of large-$p_T$ quarkonium production into single-parton and double-parton fragmentation functions (`Kang:2011mg`, `Fleming:2012wy`), for the perturbative-QCD part; the fragmentation functions are left unexpanded.
  - **非微扰地位.** \cref{asm:intro-bridge}（MA1、MA2）。
  - **地位与缺口.** All-order argument at the level of the cited papers; for hadron colliders it inherits the coloured-final-state issue (`conj:dy-coloured-final`, pointer); the further NRQCD factorization of the fragmentation functions is [C] (as `conj:heavy-nrqcd-production`, pointer) and is not part of this statement.
  - `\uses{def:pdf-ff, asm:intro-bridge}`

**Worked example.** `ex:heavy-cv`.

**Figures.** Existing (tikz3, final): `fig:nrqcd`; new (required): `fig:heavy-bdpi`, `fig:heavy-qcdf`.

**Misconception box.** Critic O19 (QCDF status); 「BBNS 只在 $O(\alpha_s)$ 成立」; 「NRQCD 产生的因子化已证明」.

**Key citation keys.** `BenekeEtAl1999`, `BenekeEtAl2000`, `BenekeEtAl2001`, `BenekeNeubert2003`, `BauerPirjolStewart2001`, `Bauer:2004tj`, `Chay:2003ju`, `Beneke:2004bn`, `Bauer:2005wb`, `Beneke:2003pa`, `Hill:2002vw`, `Beneke:2005gs`, `Beneke:2005vv`, `Beneke:2006mk`, `Kivel:2006xc`, `Pilipp:2007mg`, `Bell:2007tv`, `Bell:2009nk`, `Beneke:2009ek`, `Bell:2015koa`, `Bell:2020qus`, `Huber:2016xod`, `Mantry:2003uz`, `Bjorken:1988kk`, `Dugan:1990de`, `Politzer:1991au`, `Bauer:2002aj`, `Lange:2003ff`, `Grozin:1996pq`, `Liu:2019oav`, `Liu:2020wbn`, `Liu:2022ajh`, `Hurth:2023paz`, `Lu:2022kos`, `Bell:2024bxg`, `ChayGeorgiGrinstein1990`, `BigiUraltsevVainshtein1992`, `ManoharWise1994`, `BigiEtAl1994`, `Neubert1994a`, `Neubert1994b`, `KorchemskySterman1994`, `BauerFlemingLuke2000`, `Bauer:2003pi`, `Becher:2006qw`, `Bigi:1994em`, `Beneke:1994sw`, `CaswellLepage1986`, `BodwinBraatenLepage1995`, `Bodwin:1992ye`, `Lepage:1992tx`, `VanRoyen:1967nq`, `Barbieri:1975ki`, `Barbieri:1975am`, `Celmaster:1978yz`, `Barbieri:1979be`, `Harris:1957zza`, `NayakQiuSterman2005a`, `NayakQiuSterman2005b`, `NayakQiuSterman2006`, `Butenschoen:2010rq`, `Butenschoen:2011yh`, `Butenschoen:2012px`, `Chao:2012iv`, `Kang:2011mg`, `Fleming:2012wy`, `BrambillaEtAl2005`, `BrambillaEtAl2011`, `Lansberg:2019adr`.

**Pending.** [PENDING-VERIFY: E26, N22, S63-11].

---------------------------------------------------------------------------------------------------

# 第六部分 极限 (Part VI — Limits)

---------------------------------------------------------------------------------------------------

## Chapter 21 — 幂次修正、次领头幂次、重整化子与非微扰地位 / Power corrections, next-to-leading power, renormalons, non-perturbative status

`\label{ch:power}` · `ch21_power.tex` · **13 pp** · full · Part VI

**Purpose.** State what is known beyond leading power and beyond perturbation theory: twist 4 in DIS in $x$ space; twist 3 and single-spin asymmetries; next-to-leading-power (NLP) factorization and endpoint divergences (M22); the rearrangement freedom of the OPE basis and the meaning of "twist-2 coefficients" beyond relative $O(\Lambda^2/Q^2)$ (refdoc S42); renormalons — large-$\beta_0$ results [P], proven cases (large-$N$ O($N$) σ-model; Borel summability of the Gross–Neveu model), the general correspondence with higher twist [C] (critic O20); the honest non-perturbative status of every theorem, with the genuinely non-perturbative "laboratories" (critic O21): convergence of the OPE in perturbative $\varphi^4$, the 't Hooft model, lattice evidence (Ch22). Frontier pointers: linear renormalon and LRR (Ch22), Gross–Neveu and O($N$) models (Ch23), NLP endpoint factorization and NLP TMD (Ch24).

**Depends on.** Ch6 (OPE, condensates), Ch7 (twist, `prop:dis-twist4`, `thm:dis-ope`, `thm:dis-moments-np`), Ch12 (`thm:dy-higher-twist`), Ch13 (NLP threshold), Ch14 (Sivers, `def:tmd-etqs`), Ch15 (SCET at subleading power).

**Box.**
- 证明了：`prop:power-next-to-soft`（[R, R_PT]，树图）；`prop:power-rearrangement`（[R, R_def]）；`thm:power-ope-convergence`（[R, R_PT]，$\varphi^4_4$）；`prop:power-adler-large-beta0`、`prop:power-thooft-model`（[P]：在大 $\beta_0$ 极限／二维大 $N_c$ 中完整证明）。
- 给出全阶论证：`prop:power-dis-twist4-x`（[A]，$x$ 空间）。
- 没有证明：一般的次领头幂次因子化（`prop:power-nlp-endpoint`，[P]）；强子—强子单自旋不对称的扭度 3 因子化（`conj:power-twist3-pp`，[C]）；红外重整化子与高扭度的一般对应（`conj:power-renormalon-ht`，[C]）；QCD 的构造（`rem:power-np-status`）。

**Sections.**
1. `sec:power-twist4` DIS 的扭度 4：从矩到 $x$ 空间 (`fig:higher-twist`, owned by Ch7).
2. `sec:power-twist3` 扭度 3 与单自旋不对称 (`fig:twist3-ssa`).
3. `sec:power-nlp` 次领头幂次：次软定理与端点发散.
4. `sec:power-ope-basis` OPE 基的重排与"实用 OPE" — **new section** (refdoc S42).
5. `sec:power-renormalons` 重整化子 (`fig:renormalon-chain`, `fig:power-borel-plane`).
6. `sec:power-np` 非微扰地位与可解模型.

**Canonical statements** (in reading order).

* **命题 `prop:power-dis-twist4-x` — DIS 扭度 4 修正的 $x$ 空间形式** [A] · v1
  - **陈述.** $F_2(x,Q^2)=F_2^{\rm tw2}+\frac1{Q^2}\sum_i\int dx_1dx_2\,H_i(x_1,x_2,x)\,T^{(4)}_i(x_1,x_2)+\dots$, with quark–gluon correlators $T^{(4)}$; moment space: [R, R_OPE] (`prop:dis-twist4`); $x$ space: [A] (`EllisFurmanskiPetronzio1982`, `EllisFurmanskiPetronzio1983`, `Jaffe:1982pm`, `Qiu:1988dn`); nuclear enhancement: `prop:disall-nuclear`.
  - **非微扰地位.** \cref{asm:intro-bridge}（MA1、MA2、MA4）。
  - **地位与缺口.** Twist-4 contributions mix with the leading twist through renormalon ambiguities (`conj:power-renormalon-ht`, later in this chapter); the twist-2 basis is meaningful only up to the rearrangement of `prop:power-rearrangement`.
  - `\uses{prop:dis-twist4, thm:disall-factorization, asm:intro-bridge}`

* **命题 `prop:power-twist3-sidis` — SIDIS 型过程中的扭度 3 共线因子化** [P] · v1
  - **陈述.** Single-spin asymmetries at $P_{hT}\sim Q$ factorize at twist 3; explicit at one loop and NLO in specific processes (`Ji:2006ub`, `Vogelsang:2009pj`); the evolution of $T_F(x,x)$ is settled (`Braun:2009mi` vs `Kang:2008ey`); relation to the Sivers function $gT_F(x,x)=\mp\int d^2k_T\frac{k_T^2}Mf^{\perp q}_{1T}(x,k_T)|_{\rm SIDIS}$ as in `prop:tmd-twist3-matching` ($T_F$ defined in `def:tmd-etqs`; sign and normalization convention dependent, `Boer:2003cm`; verify).
  - **地位与缺口.** Fixed-order and process-specific evidence; no all-order twist-3 argument.
  - `\uses{def:tmd-etqs, prop:tmd-twist3-matching}`

* **猜想 `conj:power-twist3-pp` — 强子—强子碰撞中单举强子单自旋不对称的扭度 3 因子化** [C] · v1
  - **陈述.** $p^\uparrow p\to hX$ (`QiuSterman1991c`, `Qiu:1998ia`) and direct photons (`QiuSterman1992`) factorize at twist 3.
  - **地位与缺口.** Inherits `conj:dy-coloured-final`: no all-order argument exists even at leading twist for coloured final states; the "sign mismatch": `Kang:2011hk`, `Cammarota:2020qcw`.
  - `\uses{prop:power-twist3-sidis, conj:dy-coloured-final}`

* **例 `ex:power-sgp` — 最低阶的软胶子极点机制** (no tag) · v1
  - The phase comes from $\frac1{k^+\pm i0}$ (VF-WL-12), and its sign is linked to the Sivers sign (`thm:tmd-sivers-sign`).
  - `\uses{prop:power-twist3-sidis, thm:tmd-sivers-sign}`

* **命题 `prop:power-next-to-soft` — 次软定理** [R, R_PT] · v1
  - **陈述.** (Tree level.) The Low–Burnett–Kroll theorem: the amplitude for emitting a soft photon through order $k^0$ is fixed by the non-radiative amplitude and its derivatives (`Low1958`, `BurnettKroll1968`); extension to collinear regions `DelDuca1990`.
  - **证明.** Full at tree level.
  - **Remark.** Loop-level validity in QCD is [A]; starting point of NLP threshold factorization (Ch13).
  - `\uses{prop:qcd-soft-collinear-limits}`

* **命题 `prop:power-nlp-endpoint` — 次领头幂次因子化与端点发散** [P] · v1
  - **陈述.** At NLP the naive convolutions diverge at the endpoints (M22); refactorizations exist case by case: LL DY/Higgs threshold at NLP (`Beneke:2018gvs`, `Beneke:2019mua`); $h\to\gamma\gamma$ through a $b$-quark loop (`Liu:2019oav`, `Liu:2020wbn`; VF-FRO-9); $gg\to h$ (`Liu:2022ajh`); $B\to X_s\gamma$ (`Hurth:2023paz`); DIS at large $x$ (`Beneke:2022obx`; NLP DIS preprint `Beneke:2026miy`).
  - **地位与缺口.** No general theorem; $B\to M_1M_2$: `prop:heavy-qcdf-endpoint` ([V]); NLP TMD and the reported disagreements (E34): Ch24 (pointer).
  - `\uses{prop:power-next-to-soft, prop:thr-nlp}`

* **命题 `prop:power-rearrangement` — OPE 基的重排自由** [R, R_def] · refdoc S42
  - **陈述.** Given the OPE with growth bounds, $O'_i=O_i+\sum_{d_j<d_i}\kappa_{ij}\Lambda^{d_i-d_j}O_j$ gives a valid OPE with $\tilde C'_j=\tilde C_j-\sum_{d_i>d_j}\tilde C'_i\kappa_{ij}\Lambda^{d_i-d_j}$ (top-down) and the same remainder. (a) Twist-2 coefficients are meaningful only to relative $O(\frac{\Lambda^2}{Q^2}\ln^kQ)$, unless the basis is fixed non-perturbatively (e.g. by lattice normalization, Ch22). (b) Rearranging only twist $\ge4$ changes twist-2 coefficients by $o(\alpha_s^K)$, so `thm:dis-moments-np` is unaffected.
  - **证明.** Full (linear algebra of the expansion). (本命题是关于展开的代数陈述。)
  - `\uses{def:dis-twist}`

* **注 `rem:power-practical-ope` — "实用 OPE" 与重整化子吸收的两个猜想性成分** (no tag) · refdoc S42 (C18)
  - The practical OPE "$|k|>\mu_F$" is routing dependent and gauge breaking; it needs a gauge-invariant smooth cutoff, which is not available; renormalon absorption into twist 4 has exactly two conjectural ingredients: Borel continuation along $\mathbb R_+$ near the singularities, and factorization of the renormalon residue with RG-matched $\alpha_s$ dependence; both are verified at large $\beta_0$; the general case is the Mueller/David conjecture `conj:power-renormalon-ht` (forward within the chapter).

* **定义 `def:power-borel` — Borel 变换与重整化子** (no tag) · v1
  - **陈述.** For $R=\sum_nr_n\alpha_s^{n+1}$: $B[R](t)=\sum_nr_nt^n/n!$ and $R=\int_0^\infty dt\,e^{-t/\alpha_s}B[R](t)$; with $u=\beta_0t/(4\pi)$ (binding $\beta_0$; Liu–Su use $u=\beta_0t/2$ with their $\beta_0$, WRITER_SPEC_v2 §3 row 45), $e^{-t/\alpha_s(\mu)}=(\Lambda^2/\mu^2)^u$ at one loop, so a pole at $u=u_0>0$ produces an ambiguity $\propto(\Lambda^2/Q^2)^{u_0}$; IR renormalons at $u>0$, UV at $u<0$; large-order behaviour $r_n\sim n!\,(\beta_0/4\pi u_0)^nn^\gamma$.
  - `\uses{prop:prelim-beta, def:qcd-lambda}`

* **命题 `prop:power-adler-large-beta0` — 大 $\beta_0$ 极限下的 Adler 函数** [P] · v1
  - **陈述.** (In the large-$\beta_0$ (bubble-chain) approximation.) $B[D](u)$ has IR renormalon poles at $u=2,3,\dots$ and **none at $u=1$**, consistent with the absence of a dimension-2 gauge-invariant operator; the $u=2$ pole matches $\langle\frac{\alpha_s}\pi G^2\rangle$; UV renormalon poles at $u=-1,-2,\dots$; the closed form including the $\overline{\rm MS}$ scheme constant $e^{5u/3}$ is transcribed from `Beneke1999` §5 (also `Beneke1993`, `Broadhurst1993`, `BenekeBraun1995a`) (to verify).
  - **证明.** Full `proof` in the large-$\beta_0$ limit (`ex:power-renormalon-chain`, which follows as the explicit computation); Mueller's analysis `Mueller1985`.
  - **地位与缺口.** [P]: only this limit is established (WRITER_SPEC_v2 §4.10 item 5).
  - `\uses{def:power-borel, def:ee-adler, thm:ee-ope}`

* **例 `ex:power-renormalon-chain` — 带 $n$ 个费米子泡的单胶子** (no tag) · v1
  - Its Borel transform shows the structure of `prop:power-adler-large-beta0` (no $u=1$ pole).
  - `\uses{prop:power-adler-large-beta0}`

* **命题 `prop:power-renormalon-examples` — 若干过程中的重整化子与幂次修正** [P] · v1 (+ refdoc S42)
  - **陈述.** In the large-$\beta_0$ approximation: DIS $1/Q^2$ (`DasguptaWebber1996`); inclusive DY no $1/Q$ (`BenekeBraun1995b`); $e^+e^-$ longitudinal cross section $1/Q$ (`BenekeBraunMagnea1997`); event shapes $1/Q$ (`Korchemsky:1994is`, `DokshitzerWebber1995`); pole mass $u=\frac12$ (`Bigi:1994em`, `Beneke:1994sw`); quasi-PDFs (`Braun:2018brg`); lattice high-order evidence (`Bali:2014fea`). **Proven cases (refdoc S42, ERR-m19):** the large-$N$ O($N$) σ-model, where the IR renormalon–condensate cancellation is established (`David:1982qv`, `Novikov:1984ac`, `Beneke:1998eq`); Borel summability and construction of the massive Gross–Neveu model in two dimensions (`Feldman:1986ax`, `Gawedzki:1985ez`) [PENDING-VERIFY: S63-11].
  - **地位与缺口.** [P]: large-$\beta_0$ and model statements only.
  - `\uses{def:power-borel, prop:power-adler-large-beta0}`

* **猜想 `conj:power-renormalon-ht` — 红外重整化子与高扭度的一般对应** [C] · v1
  - **陈述.** In general, IR-renormalon ambiguities of leading-twist coefficient functions cancel against UV ambiguities of higher-twist matrix elements, one to one (`Mueller1985`, `David:1983gz`, `David:1985xj`, `Novikov:1984rf`, `tHooft1979`).
  - **地位与缺口.** There is no non-perturbative definition of the OPE in QCD (survey item 22; `asm:intro-np-ope`); verified at large $\beta_0$ and in the O($N$) σ-model at large $N$.
  - `\uses{prop:power-renormalon-examples, rem:power-practical-ope}`

* **注 `rem:power-np-status` — 非微扰地位** (no tag) · v1 (+ refdoc S42)
  - Every factorization theorem of this book is a statement in perturbation theory, or about perturbation theory plus the numbered assumptions `asm:intro-*` (`def:intro-MA`); QCD has not been constructed as a 4D QFT (M28); given `asm:intro-wightman`, the following are non-perturbative theorems: analyticity and positivity of spectral functions, the finite-subtraction dispersion relation (`prop:dis-dispersion-np`), support (`prop:pdf-support-hadron`, [A]), sum rules; the cleanest non-perturbative link is the lattice evaluation of local twist-2 matrix elements (Ch22). Per-order meaning of power suppression (refdoc F3): asymptotic, not summable; exponents from the general method can be far from sharp (`prop:appN-triangle-exact`(c) [PENDING-VERIFY: N12]); AQFT OPE (`Bostelmann:2005rr`); instantons give $(\Lambda/Q)^b$ terms.

* **定理 `thm:power-ope-convergence` — 微扰 $\varphi^4_4$ 中 OPE 的收敛性** [R, R_PT] · v1
  - **陈述.** In massive Euclidean $\varphi^4$ theory in four dimensions, at each order of perturbation theory, the OPE of a product of composite fields converges at finite separation, not only asymptotically (`Hollands:2011gf`, `Holland:2014pna`; curved-space framework `Hollands:2006ag`; VF-FRO-4). A model statement; for QCD see `thm:dis-ope`; further rigorous OPE results (pure Yang–Mills, CFT light-ray OPE): Ch24.
  - **证明.** Cited (complete proof in the literature). (本定理只涉及 $\varphi^4_4$ 模型的微扰论。)
  - `% uses: none`

* **命题 `prop:power-thooft-model` — 't Hooft 模型** [P] · v1
  - **陈述.** (Exact, but only in 2D QCD at large $N_c$.) Bjorken scaling holds and the structure functions are computable exactly from the meson wave functions (`tHooft1974`, `CallanCooteGross1976`, `Einhorn1976`); the only setting in which "parton distributions of a bound state" are computed non-perturbatively from first principles; quasi-PDFs in this model: Ch23 (pointer).
  - **证明.** Full for the model statement.
  - **地位与缺口.** [P] as a statement about QCD (model in $D=2$, $N_c\to\infty$).
  - `% uses: none`

**Worked examples.** `ex:power-sgp`, `ex:power-renormalon-chain`.

**Figures.** Existing (tikz3, final): `fig:renormalon-chain`, `fig:twist3-ssa` (owned); `fig:higher-twist` (owned by Ch7; refer back); new (required): `fig:power-borel-plane`.

**Misconception box.** M10, M22, M28; critic C11; O20, O21.

**Key citation keys.** `EllisFurmanskiPetronzio1982`, `EllisFurmanskiPetronzio1983`, `Jaffe:1982pm`, `Jaffe1983`, `Qiu:1988dn`, `QiuSterman1991a`, `QiuSterman1991b`, `EfremovTeryaev1985`, `Efremov:1981sh`, `QiuSterman1991c`, `QiuSterman1992`, `Qiu:1998ia`, `Ji:2006ub`, `Vogelsang:2009pj`, `Braun:2009mi`, `Kang:2008ey`, `Kang:2011hk`, `Cammarota:2020qcw`, `Boer:2003cm`, `Low1958`, `BurnettKroll1968`, `DelDuca1990`, `Beneke:2018gvs`, `Beneke:2019mua`, `Beneke:2022obx`, `Beneke:2026miy`, `Liu:2019oav`, `Liu:2020wbn`, `Liu:2022ajh`, `Hurth:2023paz`, `tHooft1979`, `Mueller1985`, `David:1983gz`, `David:1985xj`, `David:1982qv`, `Novikov:1984rf`, `Novikov:1984ac`, `Beneke:1998eq`, `Feldman:1986ax`, `Gawedzki:1985ez`, `Beneke1993`, `Broadhurst1993`, `Beneke1999`, `BenekeBraun1995a`, `BenekeBraun1995b`, `BenekeBraunMagnea1997`, `DasguptaWebber1996`, `DokshitzerWebber1995`, `Korchemsky:1994is`, `Bigi:1994em`, `Beneke:1994sw`, `Bali:2014fea`, `Braun:2018brg`, `Hollands:2011gf`, `Holland:2014pna`, `Hollands:2006ag`, `tHooft1974`, `CallanCooteGross1976`, `Einhorn1976`, `Shifman2000`, `Bostelmann:2005rr`.

**Pending.** [PENDING-VERIFY: S63-11] (renormalon proven cases: keys and contents); [N12] pointer in `rem:power-np-status`.

---------------------------------------------------------------------------------------------------

# 第七部分 前沿进展 (Part VII — Frontier progress) — Ch22 `lamet`, Ch23 `yzliu`, Ch24 `front`: see `OUTLINE_frontier.md`

---------------------------------------------------------------------------------------------------

## Chapter 25 — 总结：主表、依赖图与开放问题 / Summary: master table, dependency graph and open problems

`\label{ch:summary}` · `ch25_summary.tex` · **12 pp** · full · after Part VII · **no new canonical statements**

**Purpose.** Close the book with: (1) **the master table** `tab:summary-master` — every theorem of the book (all `thm:` labels with a tag; App M/N/O main theorems; the frontier main results), every conjecture, every [V] and [P] statement, every R_cond statement of the chapters and the key propositions of the v1/refdoc master rows — with grade, non-perturbative status, bottleneck assumptions (`asm:` labels, refdoc S44) and upgrade path; (2) the **assumption incidence matrix** `tab:summary-assumptions` (process theorems × register entries); (3) an **overview of the dependency graph** (chapter-level DAG, critical paths, statistics; the full graph is generated in App P); (4) lessons (≈2 pp); (5) the **open problems**, merging v1 Ch22's list, refdoc S44 and the open problems of the frontier reports, each naming the precise canonical statements and `asm:` labels it would settle. Ch25 is an overview: it may cite every chapter; it introduces no new results; App Q (verified errata) is referred to, not repeated.

**Depends on.** All chapters and appendices (pointers only; no `\uses`, since the chapter has no statements).

**Sections.**
1. `sec:summary-master` 主表 (`tab:summary-master`, ≈5 pp, split into several `table` floats with 「（续）」 captions — `longtable` is not loaded; `fig:summary-status-map`).
2. `sec:summary-hypotheses` 假设与瓶颈 (`tab:summary-assumptions`; `fig:summary-hypotheses`).
3. `sec:summary-dependency` 依赖图概览 — **new section**: the chapter-level DAG (optional `fig:summary-chapter-dag`, FIGURES_INDEX_v2 §4.8), the critical paths of §0.7, statistics generated from App P (number of canonical statements per tag and qualifier; number of `asm:` entries and how often each is used; the longest dependency chain; the statements with the most dependants), how to read App P (`tab:appP-status`, `fig:appP-dependency`).
4. `sec:summary-lessons` 经验与教训.
5. `sec:summary-open` 开放问题.

**Rules.**
- Every row cites its canonical label; tags must match the chapter statements exactly (script check, WRITER_SPEC_v2 §10); `tab:intro-overview` (Ch1) consists of the rows marked ★, with identical tags.
- The column 瓶颈假设 names `asm:` labels (refdoc S44), not prose; "—" for statements without technical bottleneck.
- The incidence matrix and the bottleneck column are generated from the `\uses` data (App P) and must agree with them; the version printed here is the target.
- Frontier rows (block VII) carry labels of `OUTLINE_frontier.md`; the provisional labels below are marked [SYNC-FRONTIER] and are replaced at the merge; their tags follow the frontier reports mapped by WRITER_SPEC_v2 §4.3 item 4.
- After the verify patch: rows marked [PENDING-VERIFY] are finalized (tags not stronger than here).
- Tagged preview remarks are represented by their main statement and get no row of their own (`rem:sudakov-spacelike` → row IV.24, `prop:break-spacelike`).

### `tab:summary-master` — row list (columns: # | 结论 | 公式/要点 | 标签 | 非微扰地位 | 规范标签 | 瓶颈假设 | 升级路径 | ★)

Abbreviations in the 非微扰地位 column: W = `asm:intro-wightman`, Co = `asm:intro-composite`, NO = `asm:intro-np-ope`, AF = `asm:intro-af-coeff`, Gr = `asm:intro-growth`, Br = `asm:intro-bridge`; "部分子" = statement about partonic states / operators / models only.

**Block I — Part I (Ch2–Ch5): foundations** (rows I.n; row numbers use the part numerals so that they never collide with the claim IDs E01–E36, N01–N29, A01–A28 of `verify/CLAIMS.md`).

| # | 结论 | 公式/要点 | 标签 | 非微扰 | 规范标签 | 瓶颈假设 | 升级路径 | ★ |
|---|---|---|---|---|---|---|---|---|
| I.1 | 经典拉氏量的规范不变性与唯一性 | 维数 $\le4$ 的规范不变多项式 | [R, R_def] | 部分子 | `thm:qcd-gauge-invariance` | — | — | ★ |
| I.2 | QCD 的可重整性（DR + $\overline{\rm MS}$） | 乘法重整化，ST 关系 | [R, R_PT] | 部分子 | `thm:qcd-renormalizability` | —（文献中完整） | — | ★ |
| I.3 | Slavnov–Taylor 恒等式（因子化所用形式） | $\langle T\,\partial A\cdots\Phi\rangle=0$ | [R, R_PT] | 部分子 | `thm:prelim-slavnov-taylor` | — | — | ★ |
| I.4 | 物理量的规范参数无关性 | BRST 正合的 $\partial_\xi\mathcal L$ | [R, R_PT] | 部分子 | `prop:qcd-xi-independence` | — | — | |
| I.5 | 规范不变复合算符的重整化 | 只与规范不变、BRST 正合、EOM 算符混合 | [R, R_PT] | 部分子 | `thm:prelim-composite-renorm` | 前向在壳胶子的外来算符 | 非定域情形的分类 | ★ |
| I.6 | $\beta$ 函数 | $\beta_0=\frac{11}3C_A-\frac43T_Fn_f$ | [R, R_PT] | 部分子 | `prop:prelim-beta` | — | — | |
| I.7 | 渐近自由 | $\alpha_s(\mu)\simeq\frac{4\pi}{\beta_0\ln(\mu^2/\Lambda^2)}$，$n_f\le16$ | [R, R_PT] | W（非微扰存在） | `thm:qcd-asymptotic-freedom` | — | 构造 QCD | ★ |
| I.8 | 切割规则（有质量/正规化图） | $2{\rm Im}G=\sum G_{\rm cut}$ | [R, R_PT] | 部分子 | `thm:prelim-cutting-rules` | — | — | |
| I.9 | 物理幺正性与鬼场割线 | $\sum_{\rm phys}=\sum_{-g}-$鬼场 | [R, R_PT] | 部分子 | `prop:prelim-unitarity` | — | — | |
| I.10 | Landau 条件（参数形式） | 无 Landau 点 ⇒ 解析 | [R, R_PT] | 部分子 | `thm:ir-landau-alpha` | — | — | |
| I.11 | Landau 方程（动量空间，必要性） | Gordan 择一 | [R, R_PT] | 部分子 | `thm:ir-landau-momentum` | 充分性与整体形变（`rem:ir-landau-status`） | Collins 2020 预印本的发表与核查 | ★ |
| I.12 | Coleman–Norton（代数形式） | 经典时空过程 | [R, R_PT] | 部分子 | `prop:ir-coleman-norton` | — | — | |
| I.13 | 钳夹面与约化图 | 硬—喷注—软 | [A] | 部分子 | `prop:ir-pinch-classification` | Landau 充分性 | 完整的钳夹面分类 | |
| I.14 | 超表观红外幂次计数 | $\omega(R)$ 公式（E-S） | [R, R_PT] | 部分子 | `prop:ir-power-counting` | — | — | ★ |
| I.15 | 超领头构型的相消 | $p_J=-2,-1$ 的组合相消 | [A] | 部分子 | `prop:ir-super-leading` | `asm:appN-envelope`、`asm:appN-ward-product` | 积分形式 | |
| I.16 | 领头区域 | 一个物理部分子 + 标量胶子；软只连喷注 | [A] | Br（强子版本） | `thm:ir-leading-regions` | `asm:appN-envelope`、`asm:appN-separation` | 嵌套区域的积分界 | ★ |
| I.17 | 单圈 Glauber 钳夹判据 | 初末态极点两侧 ⇒ 钳夹 | [R, R_PT] | 部分子 | `prop:ir-glauber-trapping` | — | — | |
| I.18 | QED Bloch–Nordsieck | 软光子相消、YFS | [R, R_PT] | 部分子 | `thm:ir-bn-qed` | — | — | |
| I.19 | KLN 定理 | 简并态求和 | [A] | 部分子 | `thm:ir-kln` | 初态求和需前向散射项 | — | ★ |
| I.20 | 有色初态 Bloch–Nordsieck 相消失效 | 幂次压低的未相消项 | [V] | — | `prop:ir-bn-failure` | 证据：显式两圈计算 | — | ★ |
| I.21 | 红外安全截面的有限性 | 逐阶有限 | [A] | 部分子 | `thm:ir-safe-finite` | 全阶区域分析 | — | ★ |
| I.22 | 区域方法（欧氏） | 大动量/大质量展开 | [R, R_PT] | 部分子 | `thm:ir-regions-euclid` | — | — | ★ |
| I.23 | 区域方法（闵氏） | 阈值、在壳；隐藏区域 | [P] | 部分子 | `prop:ir-regions-minkowski` | 一般证明缺失；Newton 多面体处方在三圈失效 | 闵氏证明 + 隐藏区域算法 | ★ |
| I.24 | 单圈形状因子（精确到 $\varepsilon$） | $-\frac2{\varepsilon^2}-\frac3\varepsilon-8+\zeta_2$ | [R, R_PT] | 部分子 | `prop:sudakov-oneloop` | — | — | |
| I.25 | Sudakov 形状因子的因子化 | $H\,J\,J/S$；$K+G$ | [A] | 部分子 | `thm:sudakov-factorization` | `asm:appN-collins`（此例在 Collins 2011 第 10 章中完整） | 积分范数估计 | ★ |
| I.26 | 多腿振幅红外极点（偶极子公式至两圈） | $\mathbf Z$ 因子化 | [A] | 部分子 | `thm:sudakov-ir-poles` | — | 全阶极点结构 | ★ |
| I.27 | 偶极子公式作为全阶精确陈述 | 三圈非偶极子项 | [V] | — | `prop:sudakov-dipole-violation` | 证据：显式三圈计算 | — | ★ |

**Block II — Part II (Ch6–Ch8): the rigorous core.**

| # | 结论 | 公式/要点 | 标签 | 非微扰 | 规范标签 | 瓶颈假设 | 升级路径 | ★ |
|---|---|---|---|---|---|---|---|---|
| II.1 | 欧氏 Green 函数的红外有限性 | 非例外欧氏动量；$d=A+\frac12A_q\ge2$ | [R, R_PT] | 部分子 | `thm:ee-euclid-ir` | BM 假设对含鬼场非阿贝尔理论的逐条核对 [PENDING-VERIFY: N24] | — | ★ |
| II.2 | $R(s)$ 每阶红外有限 | Laurent 系数为 $L$ 的多项式 | [R, R_PT] | W、Br（强子） | `thm:ee-R-finite` | — | 构造 QCD | ★ |
| II.3 | $R$ 与部分子割图之和等同 | 无质量 DR 割图规则 | [A] | 部分子 | `cor:ee-cuts` | 无质量 DR 中含鬼场的割图规则 | 完整的 DR 割图证明 | ★ |
| II.4 | $R(s)$ 的微扰展开 | $r_2=1.9857-0.1153n_f$ | [R, R_PT] | 部分子 | `cor:ee-R-alphas` | — | — | ★ |
| II.5 | 流关联函数的欧氏 OPE | 无 $1/Q^2$ 项 | [A] | 部分子 | `thm:ee-ope` | 含夸克规范理论的全阶证明 | 见 II.8 | |
| II.6 | 非微扰 OPE 与凝聚 | 真空凝聚 | [C] | — | `conj:ee-np-ope` | 无非微扰 OPE 定义 | — | |
| II.7 | 夸克—强子对偶 | 抹平与局域对偶 | [C] | — | `conj:ee-duality` | 复平面上的非微扰 OPE | — | ★ |
| II.8 | QCD（含夸克）的欧氏 OPE（总括） | 三个子陈述 | [A] | 部分子 | `thm:dis-ope` | `prop:dis-ope-euclid`（IV.3）、`asm:appM-brst-ope`、`asm:appM-forward` | 引用定理覆盖范围的核实（S63-1） | ★ |
| II.9 | 逐图欧氏渐近展开 | 唯一系数（对数多项式） | [A] | 部分子 | `prop:dis-ope-euclid` | IV.3；`asm:appM-remainder` | [R, R_PT] [PENDING-VERIFY: S63-1] | |
| II.10 | 物理矩阵元只需规范不变算符 | 扭度 2：$O_q,O_g$ | [A] | 部分子 | `prop:dis-ope-gi` | `asm:appM-brst-ope` | Joglekar、Hollands 覆盖部分 | |
| II.11 | 前向在壳部分子矩阵元 | 例外动量 | [A] | 部分子 | `prop:dis-ope-forward` | `asm:appM-forward` | 外来算符问题的解决 | |
| II.12 | Wightman 色散关系（有限减除） | $Q$ 无关指数；Disc $\ge0$ | [R, R_cond] | W | `prop:dis-dispersion-np` | — | 构造 QCD | |
| II.13 | OPE 在欧氏线段上的多项式逼近 | $\mathcal I_Q=\{iy:\vert y\vert\le\sqrt3M/Q\}$ | [R, R_cond] | NO | `lem:dis-ope-segment` | — | 非微扰 OPE | |
| II.14 | 由定域 OPE 得到固定 $n$ 的矩（强子） | 无自旋求和；正性 + 色散关系 | [R, R_cond] | W、NO | `thm:dis-fixed-n` | `asm:intro-np-ope` | 非微扰 OPE | ★ |
| II.15 | DIS 矩因子化的非微扰条件定理 | $n\ge n_0$；全部偶数 $n$ 需增长条件 | [R, R_cond] | W、Co、NO、AF（+Gr） | `thm:dis-moments-np` | `asm:intro-np-ope`、`asm:intro-growth` | 构造 QCD；非微扰 OPE | ★ |
| II.16 | $x$ 空间的弱收敛 | 逐点 $O(1/Q^2)$ 不可能 | [R, R_cond] | W、Co、NO、AF | `cor:dis-weak-xspace` | — | — | |
| II.17 | DIS 结构函数矩的因子化 | $\int x^{n-2}F_2=\sum C^{(n)}A^{(n)}$；$n\ge n_0$（全部偶数 $n$ 需 Gr） | [R, R_OPE] | W、Co、NO、AF、Gr | `thm:dis-moments` | `thm:dis-ope`；`asm:intro-np-ope`、`asm:intro-growth` | 非微扰 OPE | ★ |
| II.18 | Bjorken 求和规则 | $\frac{g_A}6[1-a-(\frac{55}{12}-\frac{n_f}3)a^2]$ | [R, R_OPE] | W、Co、NO、AF、Gr | `thm:dis-bjorken` | 同 II.17 | 同 II.17 | ★ |
| II.19 | 光锥展开 | 固定扭度塔 | [A] | 部分子 | `prop:dis-light-cone` | 理论类别未核查 | — | |
| II.20 | PDF 支撑（微扰论） | $\vert\xi\vert\le1$ | [R, R_PT] | 部分子 | `thm:pdf-support-pt` | — | — | ★ |
| II.21 | PDF 支撑（强子） | 谱论证 | [A] | W、Co | `prop:pdf-support-hadron` | 态求和与重整化的交换 | 非微扰构造 | ★ |
| II.22 | PDF 的矩 = 定域算符矩阵元 | $\int\xi^{n-1}f=A^{(n)}$ | [R, R_PT] | W、Co | `thm:pdf-moments-local` | — | — | ★ |
| II.23 | DGLAP 来自算符重整化 | $\partial f/\partial\ln\mu^2=P\otimes f$ | [R, R_PT] | Co（强子） | `thm:pdf-dglap` | — | — | ★ |
| II.24 | 数与动量求和规则 | $\sum\int xf=1$ | [R, R_PT] | W、Co（强子结构函数另需 Gr） | `prop:pdf-sum-rules` | — | — | ★ |
| II.25 | $x$ 空间 DIS（扭度 2 部分） | $F_2^{\rm tw2}/x=\sum C_i\otimes f_i$ | [R, R_OPE] | W、Co、NO、AF、Gr | `thm:pdf-dis-xspace` | 逐点余项不受控 | `thm:disall-factorization` 升级 | ★ |
| II.26 | 类时 DGLAP（全阶） | $P^T$；单圈 $P^{T(0)}=P^{(0)}$ [R] | [A] | W、Co | `prop:pdf-timelike-dglap` | `asm:appN-multren`(Z1) | FF 乘法可重整性的证明 | |
| II.27 | $\overline{\rm MS}$ PDF 的正定性（$\mu\ge\mu_0$） | 所有标度上非负是错的（Yukawa 反例） | [C] | — | `conj:pdf-positivity` | 无一般证明；文献有争议 [PENDING-VERIFY: E35] | 证明或反例；$\mu_0$ 的非微扰确定 | ★ |

**Block III — Part III (Ch9–Ch13): collinear factorization; App N, O.**

| # | 结论 | 公式/要点 | 标签 | 非微扰 | 规范标签 | 瓶颈假设 | 升级路径 | ★ |
|---|---|---|---|---|---|---|---|---|
| III.1 | 局部精度（积分范数） | $(1-T_{R_0})\Gamma\in\mathfrak S(U_{R_0})$ | [R, R_cond] | 部分子 | `lem:method-local-accuracy` | `asm:appN-envelope`、`asm:appN-separation` | 积分形式的幂次计数 | |
| III.2 | 去掉维数正规化 | 单个减除项的极点在和中相消 | [R, R_cond] | 部分子 | `cor:method-removing-eps` | `asm:appN-contour` | — | |
| III.3 | 减除定理（条件形式） | (CS1)–(CS3) ⇒ 余项积分范数压低 | [R, R_cond] | 部分子 | `thm:appN-subtraction` [SYNC-APP] | `asm:appN-collins` | 变形围道上的一致积分界 | ★ |
| III.4 | 单圈离壳三角图的完整减除 | $\int r=-4m^2/Q^4+O(m^4Q^{-6}L^2)$ | [R, R_PT] | 部分子 | `prop:appN-triangle-exact` [SYNC-APP] | — [PENDING-VERIFY: N12] | — | ★ |
| III.5 | 减除定理 | $\Gamma=\sum_RC_R\Gamma+O(\lambda^aL^K)$ | [A] | 部分子 | `thm:method-subtraction` | `asm:appN-collins`、`asm:appN-uv`、`asm:appN-contour` | 解除 `asm:appN-collins`（S63-12） | ★ |
| III.6 | 多个 K 胶子的 Ward 恒等式 | 非阿贝尔、含鬼场 | [A] | 部分子 | `lem:method-ward-multi` | `asm:appN-ward-product`；非定域算符 BRST 分类 | 分类的证明（第~24~章矩约化） | ★ |
| III.7 | 末态相互作用的幺正性相消 | 闭时路形式 | [A] | 部分子 | `prop:method-fsi` | `asm:appN-cutsum`、`asm:appO-lcopt` | — | |
| III.8 | Glauber 区的围道变形 | 沿 $e_G$ 同时形变 | [A] | 部分子 | `prop:method-glauber-deformation` | `asm:appO-deformation`、`asm:appO-mixing`、`asm:appO-envelope`、`asm:appO-rewritten-cs` | 见 III.25 | ★ |
| III.9 | 因子化模板定理 | (H1)–(H5) ⇒ 因子化形式 | [A] | Br | `thm:method-template` | `asm:appN-envelope`、`asm:appN-separation`、`asm:appN-ward-product`、`asm:appN-cutsum`、`asm:appN-collins`、`asm:appN-uv`、`asm:appN-multren`；经 III.7、III.8：`asm:appO-lcopt`、`asm:appO-deformation`（`asm:appN-values` 为约定；全表见 `tab:method-hypotheses`） | 解除上述假设 | ★ |
| III.10 | 两条途径：矩与 $x$ 空间 | 复圆盘一致界 ⇒ 矩；$x\to1$ 非一致 | [R, R_cond] | 部分子 | `prop:disall-two-routes` | `asm:appN-collins`、`asm:appN-cutsum` | — | |
| III.11 | DIS 减除项的因子化结构 | $\sum C_R\Gamma=\hat{\mathsf H}_R\otimes\mathsf J_R^{\rm bare}$ | [R, R_cond] | 部分子 | `prop:disall-factorized-subtraction` | `asm:appN-ward-product`、`asm:appN-uv` | — | |
| III.12 | 减除与 $\overline{\rm MS}$ 重整化的相容性 | 系数有限、与靶无关 | [R, R_cond] | 部分子 | `thm:disall-renorm-compat` | `asm:appN-multren` | (Z2) 正规子 | |
| III.13 | DIS 共线因子化（$x$ 空间逐点） | $F_2/x=\sum C\otimes f+O(\Lambda^2/Q^2)$ | [A] | Br | `thm:disall-factorization` | `asm:appN-collins`、`asm:appN-ward-product`、`asm:appN-cutsum`、`asm:appN-envelope`、`asm:appN-separation`、`asm:appN-uv`、`asm:appN-multren` | 解除上述假设 | ★ |
| III.14 | 一致性：动量空间与 OPE 系数 | 作为分布一致 | [R, R_OPE] | 部分子 | `cor:disall-consistency` | — | — | |
| III.15 | 含重夸克质量的 DIS | Collins 1998 | [A] | Br | `thm:disall-heavy` | 同 III.13 | 同 III.13 | ★ |
| III.16 | $e^+e^-\to hX$（碎裂函数） | $d\sigma=\hat\sigma\otimes d$ | [A] | Br | `thm:coll-sia` | 同 III.13 + `asm:appN-multren`(Z1) | 同上 | ★ |
| III.17 | 共线 SIDIS | PDF ⊗ 硬 ⊗ FF | [A] | Br | `thm:coll-sidis` | 同 III.16 | 同上 | ★ |
| III.18 | 直接光生 | 类 DIS | [A] | Br | `thm:coll-direct-photo` | 同 III.13 | — | |
| III.19 | 分辨光生 | 有色末态 | [C] | — | `conj:coll-resolved-photo` | 同 III.31 | — | |
| III.20 | 衍射（分辨）光生的因子化破坏 | 抑制因子 0.42–0.71 | [V] | — | `prop:coll-diffractive-photo` | 证据：实验 | — | |
| III.21 | $g_1$ 奇数矩 | 轴反常、方案依赖 | [R, R_OPE] | W、Co、NO、AF（+Gr） | `thm:coll-g1-moments` | 单态：轴反常与方案依赖 | — | ★ |
| III.22 | Ellis–Jaffe 求和规则 | 假定 $\Delta s=0$ | [V] | — | `prop:coll-ellis-jaffe` | 证据：实验（EMC） | — | |
| III.23 | Burkhardt–Cottingham 求和规则 | 固定极点 | [C] | — | `conj:coll-bc` | 极化结构函数的固定极点问题（增长条件的极化类比，非依赖） | — | |
| III.24 | Wandzura–Wilczek 关系 | 真扭度 3 项 | [V] | — | `prop:coll-ww` | 证据：算符分析 | — | |
| III.25 | 单举 Drell–Yan 中 Glauber 区相消（条件定理） | LCOPT；等光锥时刻局域化；沿 $e_G$ 同时形变 | [R, R_cond] | 部分子 | `thm:appO-main` [SYNC-APP] | `asm:appO-mixing`(c)、`asm:appO-deformation`(b)–(d)、`asm:appO-rewritten-cs` | 解除上述假设 [PENDING-VERIFY: X1] | ★ |
| III.26 | 单举 Drell–Yan 共线因子化 | $\sigma=f\otimes f\otimes\mathcal H+O((\Lambda/Q)^p)$ | [A] | Br | `thm:dy-factorization` | `asm:appO-mixing`(c)、`asm:appO-deformation`(b)–(d)、`asm:appO-rewritten-cs`、`asm:appO-lcopt`、`asm:appO-envelope`；`asm:appN-collins`、`asm:appN-cutsum`（其余 `asm:appN-*` 经 III.9） | 含 Glauber 减除的完整证明 | ★ |
| III.27 | 程函线间双胶子交换的 $O(g^4)$ 幺正性 | $p_{\rm opp}=-iY/\pi$；Regge 相位 | [R, R_PT] | 部分子 | `prop:dy-eikonal-twogluon` | — [PENDING-VERIFY: N01] | 非程函旁观者与全阶 | ★ |
| III.28 | 阿贝尔模型中旁观者 Glauber 相位的相消 | $\vert e^{i\chi}\vert^2=1$ | [P] | 部分子（模型） | `prop:dy-abelian-model` | 非阿贝尔、全阶 | — | |
| III.29 | 色单态末态（$W,Z,H$） | 同 DY | [A] | Br | `thm:dy-colour-singlet` | 同 III.26 | 同 III.26 | ★ |
| III.30 | 极化 Drell–Yan | 螺旋度与横度 PDF | [A] | Br | `thm:dy-polarized` | 同 III.26 | 同 III.26 | |
| III.31 | $pp\to$ 喷注/强子/重夸克对 | 有色末态 | [C] | — | `conj:dy-coloured-final` | 有色末态的 Glauber 相消（App O 在 (O-3) 失效） | 与 DY 同等细节的证明 | ★ |
| III.32 | 极化强子对撞的 $A_{LL}$ | 继承 III.31 | [C] | — | `conj:dy-polarized-jets` | 同 III.31 | — | |
| III.33 | $1/Q^2$ 处的广义因子化 | 扭度 4 | [A] | Br | `thm:dy-higher-twist` | 次领头幂次的 Glauber 分析 | — | |
| III.34 | DY 超出 $1/Q^2$ | $m^4/s^2$ 处失效 | [V] | — | `prop:dy-twist6-failure` | 证据：标量夸克模型显式反例 | — | ★ |
| III.35 | 阈值重新因子化（领头幂次） | Mellin 指数化 | [A] | Br | `thm:thr-refactorization` | 同 III.26；$z\to1$ 的区域完备性 | — | ★ |
| III.36 | DIS 大 $x$ 重新因子化 | $H\cdot J\otimes S$ | [A] | Br | `prop:thr-dis` | 同 III.13 | — | |
| III.37 | 次领头幂次阈值对数 | LL | [P] | — | `prop:thr-nlp` | 端点发散 | 一般 NLP 因子化 | ★ |

**Block IV — Part IV (Ch14–Ch18): beyond collinear.**

| # | 结论 | 公式/要点 | 标签 | 非微扰 | 规范标签 | 瓶颈假设 | 升级路径 | ★ |
|---|---|---|---|---|---|---|---|---|
| IV.1 | 零箱减除即软因子 | $\sum C_R\Gamma=\mathsf H\tilde f^{\rm unsub}\tilde f^{\rm unsub}/\tilde S$ | [R, R_cond] | 部分子 | `prop:tmd-zero-bin-soft` | `asm:appN-ward-product`、`asm:appN-tmd` | — | |
| IV.2 | 平方根构造是恒等式 | 与 $y_n$ 无关 | [R, R_def] | 部分子 | `lem:tmd-sqrt-identity` | — | — | |
| IV.3 | TMD 因子化（DY、SIDIS、$e^+e^-$） | $\zeta_A\zeta_B=Q^4$ | [A] | Br | `thm:tmd-factorization` | `asm:appN-tmd`、`asm:appN-collins`、`asm:appO-rewritten-cs`、`asm:appO-mixing` | 全阶方案等价性；Glauber | ★ |
| IV.4 | Collins–Soper 与 RG 方程 | $\partial\ln\tilde f/\partial\ln\sqrt\zeta=\tilde K$ | [A] | 部分子 | `prop:tmd-evolution` | `asm:appN-tmd`(T3) | — | |
| IV.5 | 小 $b$ 展开 | $\tilde f=\tilde C\otimes f+O((mb_T)^p)$ | [A] | Co、Br | `prop:tmd-small-b` | $p=2$ [PENDING-VERIFY: S63-7] | — | |
| IV.6 | Sivers 符号反转（算符） | $f_{1T}^\perp\vert_{\rm SIDIS}=-f_{1T}^\perp\vert_{\rm DY}$ | [R, R_def] | W、Co | `thm:tmd-sivers-sign` | — | — | ★ |
| IV.7 | Sivers 符号反转（可观测） | | [A] | Br | `cor:tmd-sivers-observable` | 依赖 IV.3 | 实验判定 | ★ |
| IV.8 | Collins 函数的普适性 | 无符号变化 | [A] | Br | `prop:tmd-collins-universality` | 依赖 IV.3 | — | |
| IV.9 | 与扭度 3 的匹配 | 单圈一致 | [P] | — | `prop:tmd-twist3-matching` | 全阶匹配 | — | |
| IV.10 | 超软退耦（BPS） | SCET 拉氏量恒等式 | [R, R_def] | 部分子 | `thm:scet-decoupling` | 作为 QCD 陈述需模式完备 | — | ★ |
| IV.11 | 推力分布 $H\,J\otimes J\otimes S$ | | [A] | Br | `thm:scet-thrust` | 模式完备性（`asm:intro-bridge`、`asm:appN-envelope`） | — | ★ |
| IV.12 | 领头对数指数 | $\ell g_1(\lambda)$ | [A] | Br | `prop:scet-ll` | 继承 IV.11 | — | |
| IV.13 | 非全局对数（LL，大 $N_c$） | BMS | [A] | — | `thm:jets-bms` | 有限 $N_c$ | — | ★ |
| IV.14 | 非全局对数：超出 LL 与有限 $N_c$ | 部分与数值结果 | [P] | — | `prop:jets-ngl-beyond` | 只有部分/数值重求和 | NLL 重求和的完整处理（第~24~章） | |
| IV.15 | 喷注过程的 EFT 因子化 | 多 Wilson 线软函数 | [A] | Br | `thm:jets-ngl-factorization` | 继承 IV.11 | — | |
| IV.16 | 超领头对数 | $\alpha_s^nL^{2n-3}$ | [P] | — | `prop:jets-sll` | Glauber 相位；PDF 因子化 [C] | — | ★ |
| IV.17 | 强子化修正的普适性 | $\Lambda/Q$ 平移 | [C] | — | `conj:jets-hadronization` | 形状函数 | — | |
| IV.18 | BFKL（LL/NLL） | $\omega_{\mathbb P}=4\ln2\,\bar\alpha_s$ | [A] | — | `thm:smallx-bfkl` | 对数近似 | — | ★ |
| IV.19 | $k_T$ 因子化 | | [P] | — | `prop:smallx-kt` | 幂次修正不受控；过程依赖 | — | ★ |
| IV.20 | BK 与 JIMWLK（LL） | 偶极子框架 | [A] | — | `thm:smallx-bk` | 程函展开中的固定对数精度 | — | |
| IV.21 | 饱和/色玻璃凝聚 | | [C] | — | `conj:smallx-saturation` | 与共线因子化的匹配 | — | ★ |
| IV.22 | 测量相容性判据 | $[\Pi,U]=0$ ⇒ 割线求和幺正性 | [R, R_cond] | 部分子 | `prop:break-measurement` | `asm:appO-lcopt` | — | ★ |
| IV.23 | $h_1h_2\to H_1H_2X$ 的 TMD 因子化 | 色纠缠 | [V] | — | `thm:break-tmd` | 证据：模型反例 | — | ★ |
| IV.24 | 类空严格共线因子化（振幅） | CdFR | [V] | — | `prop:break-spacelike` | 证据：显式单圈计算 | — | ★ |
| IV.25 | 超出 NNLO 的质量奇异性因子化 | 恢复的证据 | [C] | — | `prop:break-mass-singularity` | [PENDING-VERIFY: S63-10] | — | |
| IV.26 | Coulomb 相位与软交换不对易 | 三圈 $[D,[D,A]]$ | [V] | — | `prop:break-fss` | 证据：显式计算 | — | |
| IV.27 | 对 MPI 敏感的观测量 | Zeng 反例；Gaunt vs SYZ | [V] | — | `prop:break-jet-veto` | 证据：显式模型反例 | — | |
| IV.28 | 衍射 DIS | 衍射 PDF | [A] | Br | `thm:break-ddis` | 同 III.13 + $r^+$ 形变 | — | ★ |
| IV.29 | 强子—强子硬衍射 | 间隙存活 | [V] | — | `prop:break-hh-diffraction` | 证据：实验 | — | ★ |
| IV.30 | 双 Drell–Yan | | [A] | Br | `thm:break-double-dy` | 演化、正定性；同 III.26 | — | ★ |
| IV.31 | 有色末态 DPS | | [C] | — | `conj:break-dps-coloured` | 同 III.31 | — | |
| IV.32 | 口袋公式 | $\sigma_A\sigma_B/\sigma_{\rm eff}$ | [C] | — | `conj:break-pocket` | 关联被忽略 | — | |

**Block V — Parts V–VI (Ch19–Ch21).**

| # | 结论 | 公式/要点 | 标签 | 非微扰 | 规范标签 | 瓶颈假设 | 升级路径 | ★ |
|---|---|---|---|---|---|---|---|---|
| V.1 | 色单态介子软胶子的被积函数相消 | 小色偶极子 | [R, R_cond] | 部分子 | `prop:excl-soft-cancel` | `asm:appN-endpoint`、`asm:appN-collins` | — | |
| V.2 | 介子形状因子（领头幂次） | $Q^2F_\pi\to8\pi\alpha_sf_\pi^2$ | [A] | Br | `thm:excl-pion-ff` | `asm:appN-endpoint`；端点区域 | — | ★ |
| V.3 | $\gamma^*\gamma\to\pi^0$ | $Q^2F\to\sqrt2f_\pi$ | [A] | Br | `thm:excl-transition` | — | — | |
| V.4 | 端点区域与软重叠 | Feynman 机制 | [P] | — | `prop:excl-endpoint` | 无 QCD 界 | — | |
| V.5 | DVCS | | [A] | Br | `thm:excl-dvcs` | $x=\pm\xi$ 区域 | — | ★ |
| V.6 | 纵向光子介子产生 | | [A] | Br | `thm:excl-meson-L` | `asm:appN-endpoint`、`asm:appN-collins` | — | ★ |
| V.7 | 横向光子介子产生（标准共线形式） | 扭度 3 端点对数发散 | [V] | — | `prop:excl-meson-T` | 证据：显式计算 | — | ★ |
| V.8 | 近阈重夸克偶素光生 | 自旋 2 引力形状因子 | [P] | — | `prop:excl-near-threshold` | LO；阈值处 GPD 因子化 | — | |
| V.9 | $B\to D\pi$ | | [A] | Br | `thm:heavy-bdpi` | 端点压低假设；SCET 前提 | — | ★ |
| V.10 | 重到轻形状因子：软重叠 + 硬旁观者 | $F=C\,\xi_\pi+T\otimes\phi_B\otimes\phi_\pi$ | [A] | Br | `prop:heavy-btopi-ff` | SCET 全阶论证；$\xi_\pi$ 的端点发散 | — | ★ |
| V.11 | $B\to\pi\pi$（领头幂次） | BBNS | [P] | Br | `prop:heavy-qcdf-lp` | 全阶证明缺失；粲企鹅争议 | 全阶证明 | ★ |
| V.12 | $B\to\pi\pi$ 幂次修正 | $X_A,X_H$ | [V] | — | `prop:heavy-qcdf-endpoint` | 证据：发散卷积 | 端点再因子化 | ★ |
| V.13 | 单举 $B$ 衰变（重夸克展开） | 无 $1/m_b$ 项 | [A] | W、Co、AF | `thm:heavy-inclusive-b` | 局域对偶（`conj:ee-duality`） | — | ★ |
| V.14 | NRQCD 衰变 | | [A] | Br（+局域对偶） | `thm:heavy-nrqcd-decay` | 局域对偶 | — | ★ |
| V.15 | NRQCD 产生 | | [C] | — | `conj:heavy-nrqcd-production` | NNLO 以上的规范完备化 | 全阶证明或反例 | ★ |
| V.16 | 大 $p_T$ 重夸克偶素 | LP + NLP 碎裂 | [A] | Br | `prop:heavy-quarkonium-fragmentation` | 强子对撞的有色末态；NRQCD 步骤 [C]（不属于该陈述） | — | |
| V.17 | DIS 扭度 4（$x$ 空间） | | [A] | Br | `prop:power-dis-twist4-x` | 重整化子混合 | — | |
| V.18 | SIDIS 型扭度 3 单自旋不对称 | | [P] | — | `prop:power-twist3-sidis` | 全阶论证缺失 | — | ★ |
| V.19 | 强子—强子单自旋不对称的扭度 3 因子化 | | [C] | — | `conj:power-twist3-pp` | 同 III.31 | — | |
| V.20 | 次领头幂次因子化与端点发散 | 逐个过程 | [P] | — | `prop:power-nlp-endpoint` | 无一般定理 | 一般 NLP 定理 | |
| V.21 | OPE 基的重排自由 | 扭度 2 系数的意义 | [R, R_def] | 部分子 | `prop:power-rearrangement` | — | — | |
| V.22 | 大 $\beta_0$ 重整化子 | 无 $u=1$ 极点 | [P] | — | `prop:power-adler-large-beta0` | 近似 | — | ★ |
| V.23 | 若干过程的重整化子；已证明的模型情形 | O($N$) σ 模型；Gross–Neveu | [P] | — | `prop:power-renormalon-examples` | [PENDING-VERIFY: S63-11] | — | |
| V.24 | 红外重整化子 ↔ 高扭度（一般） | | [C] | — | `conj:power-renormalon-ht` | 无非微扰 OPE 定义 | — | ★ |
| V.25 | $\varphi^4_4$ 中 OPE 的逐阶收敛 | | [R, R_PT] | 部分子（模型） | `thm:power-ope-convergence` | — | — | ★ |
| V.26 | 't Hooft 模型 | 二维大 $N_c$ 精确 | [P] | 部分子（模型） | `prop:power-thooft-model` | 模型 | — | |

**Block VII — Part VII (Ch22–Ch24): frontier main results** [SYNC-FRONTIER] (labels and tags from `OUTLINE_frontier.md`; the v1 `lattice` labels are fixed; provisional labels are given for the others with the grade of the frontier reports mapped by WRITER_SPEC_v2 §4.3 item 4).

| # | 结论 | 标签 | 规范标签 | 瓶颈 | ★ |
|---|---|---|---|---|---|
| VII.1 | 格点可计算的矩 | [R, R_OPE] | `prop:lattice-moments` | `asm:intro-growth`（$n<n_0$）；基的非微扰归一化 | ★ |
| VII.2 | Wilson 线夸克双线性算符的乘法可重整性 | [A] | `prop:lattice-renormalizability` | 静态源 + QCD 的可重整性写出（开放问题 OP-F1） | |
| VII.3 | LaMET/短距离因子化：部分子匹配（全阶） | [A] | `thm:lattice-lamet` | 类空 OPE（`thm:dis-ope` 型） | ★ |
| VII.4 | 格点 Collins–Soper 核 | [A] | `prop:lattice-cs-kernel` | 准 TMD 因子化 | ★ |
| VII.5 | LaMET 原理（非微扰） | [C] | provisional `conj:lamet-principle` | 非微扰 | ★ |
| VII.6 | 强子层次的准 PDF 匹配（含幂次修正形式） | [C]（蕴含关系 [R, R_cond]） | provisional `thm:lamet-hadronic-matching` | Ioffe 时间一致性、长距离控制（`asm:lamet-*`） | |
| VII.7 | 类空关联函数的指数衰减（公理化标量理论） | [R, R_cond]（QCD [A]/[C]） | provisional `thm:lamet-exp-decay` | 质量间隙（含静态色源） | |
| VII.8 | 准 TMD 因子化（CS 指数含 $\frac12$） | [A] | provisional `thm:yzliu-quasi-tmd` | (T3)、极限次序、有限长订书钉的 Glauber 分析 [PENDING-VERIFY: E02] | ★ |
| VII.9 | 时序无关性：DY 型软因子 = 类空形状因子 | [A] | provisional `thm:yzliu-time-ordering` | DR 关联函数的微扰 Wightman 结构 | ★ |
| VII.10 | 离光锥软函数 = 快速色源对的 HQET 形状因子 | [A] | provisional `thm:yzliu-soft-hqet` | — | |
| VII.11 | 准 PDF 匹配核的阈值因子化 | [A]（单/两圈 [R, R_PT]） | provisional `thm:yzliu-threshold` | — | |
| VII.12 | 二维 Gross–Neveu：扭度展开的绝对收敛 | [P]（模型内严格） | provisional `prop:yzliu-gn-convergence` | 模型 | |
| VII.13 | 物理区钳夹判据（Collins 2020，预印本） | [A]（证明仅见于预印本） | provisional `thm:front-collins-landau` | 发表与符号条件 [PENDING-VERIFY: A08] | ★ |
| VII.14 | Gordan 择一与动量空间 Coleman–Norton | [R, R_def]／（N02、N03） | provisional `prop:front-gordan` | [PENDING-VERIFY: N02, N03] | |
| VII.15 | 区域 = Newton 多面体下表面（闵氏） | [V]（三圈非平面反例） | provisional `prop:front-hidden-regions` | — | |
| VII.16 | Glauber EFT；纯 Glauber 梯形对单标度观测量相消 | [A] | provisional `prop:front-glauber-eft` | RS 主张 (v) 与 SYZ | |
| VII.17 | SLL 塔的重求和；间隙中 PDF 因子化的恢复（三圈） | [A]；[P] | provisional `prop:front-sll-restoration` | [PENDING-VERIFY: S63-10] | |
| VII.18 | $h\to\gamma\gamma$（$b$ 圈）的端点因子化 | [A] | provisional `thm:front-endpoint-hgg` | — | |
| VII.19 | $\overline{\rm MS}$ PDF 正定性：所有标度 [V]；高标度 [P] | [V]；[P] | provisional `prop:front-positivity` | [PENDING-VERIFY: E35] | |
| VII.20 | 双局域 PDF 算符 BRST 分类的矩约化 | [A] | provisional `prop:front-brst-moments` | 多局域分类 [C] [PENDING-VERIFY: N04] | |
| VII.21 | 双 DY：Glauber 相消、无重复计数 | [A] | provisional `prop:front-dps`（与第~18~章 IV.30 行同一结论的前沿部分） | — | |
| VII.22 | NRQCD 产生：NNLO 规范完备化；两圈方向无关性 | [P] | provisional `prop:front-nrqcd-nnlo` | — | |
| VII.23 | 电弱 Bloch–Nordsieck 破坏 | [V] | provisional `prop:front-ew-bn` | — | |

### `tab:summary-assumptions` — incidence matrix (generated from `\uses`; printed in three sub-tables: global, subtraction/OPE, Glauber)

Rows (process theorems and R_cond theorems) and the register entries they depend on (✓ = in the `\uses` list or in the premise sentence; ○ = through a used statement):
- `thm:dis-moments`: W, Co, NO, AF, Gr ✓; `asm:appM-forward` ○ (via `prop:dis-ope-forward`).
- `thm:dis-moments-np`: W, Co, NO, AF, Gr ✓.
- `thm:sudakov-factorization`: `asm:appN-collins` ✓ (the subtraction step; complete in Collins 2011 ch. 10 at the level of rigour of that chapter, S63-12).
- `thm:method-subtraction`: `asm:appN-collins`, `asm:appN-uv`, `asm:appN-contour` ✓; `asm:appN-envelope`, `asm:appN-separation` ○ (via `lem:method-local-accuracy`).
- `thm:method-template`: Br ✓; `asm:appN-envelope`, `-separation`, `-ward-product`, `-cutsum`, `-collins`, `-values`, `-uv`, `-multren` ✓; `asm:appO-lcopt`, `asm:appO-deformation` ○.
- `thm:disall-factorization`: Br; `asm:appN-collins`, `-envelope`, `-separation`, `-cutsum`, `-ward-product`, `-uv`, `-multren` ✓.
- `thm:coll-sia`: Br, `asm:appN-multren`(Z1) ✓; the other `asm:appN-*` ○ (via `thm:method-template`). `thm:coll-sidis`: Br ✓; all technical entries ○ (via `thm:disall-factorization`, `thm:coll-sia`).
- `thm:dy-factorization`: Br; `asm:appO-lcopt`, `-envelope`, `-mixing`, `-deformation`, `-rewritten-cs` ✓; `asm:appN-collins`, `-cutsum` ✓; the remaining `asm:appN-*` ○.
- `thm:tmd-factorization`: Br; `asm:appN-tmd`, `-collins` ✓; `asm:appO-rewritten-cs`, `-mixing` ✓; `asm:appN-ward-product` ○.
- `thm:scet-thrust`: Br ✓; `asm:appN-envelope` ○ (mode completeness).
- `thm:break-ddis`, `thm:break-double-dy`: Br ✓; as DIS resp. DY ○.
- `thm:excl-pion-ff`, `thm:excl-meson-L`: Br; `asm:appN-endpoint`, `asm:appN-collins` ✓.
- `thm:heavy-bdpi`, `prop:heavy-btopi-ff`: Br ✓; SCET premises ○.
- `thm:appN-subtraction`, `thm:appO-main`, `prop:appN-dy`: their premises as in `OUTLINE_appMNOPQ.md` [SYNC-APP].
- Frontier: `asm:lamet-*`, `asm:yzliu-*`, `asm:front-*` [SYNC-FRONTIER].
Columns: the 25 register entries of refdoc §5.3 + the frontier entries [SYNC-ASM].

### Lessons (`sec:summary-lessons`, ≈2 pp)
1. Rigour is local: the tag belongs to a statement, not to a process; the same process has [R] (PT moments), [R, R_cond] (non-perturbative moments), [A] ($x$ space) statements.
2. Moment space vs $x$ space: moments determine $x$-space objects only as distributions; the OPE gives weak convergence, never pointwise $O(1/Q^2)$ (`rem:dis-nonuniform`, `cor:dis-weak-xspace`).
3. Inclusivity in the spectator final state is a theorem per observable: the measurement must commute with the light-cone evolution (`prop:break-measurement`).
4. Soft factors and rapidity: only properly combined objects are regulator independent; Euclidean realizations of TMD soft physics (Ch23).
5. EFT and graphical proofs are complementary; neither supersedes the other's hypotheses (`rem:scet-assumptions`).
6. **Rigour statements are about grouped expressions, never single terms** (refdoc S44): single chain terms need not be integrable (`ex:method-naive-induction`, `ex:disall-ladder`).
7. Scaling statements are not bounds: the gap between E-S and E-N is exactly what the technical assumptions of App N/O formalize; the per-order exponents of the general method can be far from sharp (`rem:intro-sharpness`).
8. Conditional theorems with numbered assumptions make the frontier of knowledge precise: every [A] grade is traced to named `asm:` entries; every upgrade path is a list of assumptions to discharge.
9. Literature errors found and verified during this work are collected in App Q (pointer; only verified items).

### Open problems (`sec:summary-open`)

Merged list: v1 Ch22 problems 1–14 (reworded per refdoc S44), refdoc S44 new problems 15–17, and the open problems of the frontier reports (LAMET §13, YZLIU §7, OTHERS §14.3). Each problem names the canonical statements and `asm:` labels it would settle; frontier labels are [SYNC-FRONTIER]. Numbering OP-A1 … OP-F9 (grouped).

**A. Foundations.**
- **OP-A1** Construction of QCD and the bridge to hadrons (v1 #5): discharge `asm:intro-wightman`, `asm:intro-composite`, `asm:intro-bridge`; settles the non-perturbative status lines of all hadron statements and `rem:power-np-status`.
- **OP-A2** The OPE for QCD with quarks (v1 #4, kept wording per D3; refdoc S44 #4; OTHERS #6; LAMET #1): prove `prop:dis-ope-euclid` for QCD with quarks, ghosts and gauge-variant operators; possibly dischargeable parts `asm:appM-remainder` (Anikin–Zav'yalov), `asm:appM-brst-ope` (Joglekar, Hollands); convergence of the OPE for Yang–Mills/QCD; the short-distance expansion of Wilson-line operators at the level of Zimmermann's forest formula (QCD + space-like auxiliary field). Settles `thm:dis-ope`, `thm:ee-ope`, the R_OPE statements (→ R_PT), and the partonic matching theorem of Ch22 (`thm:lattice-lamet`).
- **OP-A3** A non-perturbative definition of the OPE: discharge `asm:intro-np-ope`, `asm:intro-af-coeff`; settles `conj:ee-np-ope`, `conj:power-renormalon-ht`, `conj:ee-duality`(a).
- **OP-A4** The growth condition (refdoc S44 #16): discharge `asm:intro-growth` (fixed poles, the momentum sum rule of hadrons); settles the $n<n_0$ part of `thm:dis-moments-np`, `prop:dis-low-moments` in application, `conj:coll-bc`.
- **OP-A5** Forward on-shell OPE (refdoc S44 #17): discharge `asm:appM-forward` (alien operators for forward on-shell massless partons; Hamberg–van Neerven, Falcioni–Herzog, Gehrmann–von Manteuffel–Yang); settles `prop:dis-ope-forward`.
- **OP-A6** Landau theory (v1 #3 part; OTHERS #1): sufficiency and global deformation (`rem:ir-landau-status`); a refereed version of the physical-region pinch criterion without the sign condition and the quadratic restriction; the cone of allowed deformations at a pinch; coordinate-space version (Erdoğan–Sterman); settles `prop:ir-pinch-classification`, upgrades row VII.13.
- **OP-A7** Method of regions in Minkowski kinematics (OTHERS #2): a proof and an algorithm guaranteed to find hidden regions (Glauber, multi-hard); settles `prop:ir-regions-minkowski`, SCET mode completeness (`rem:scet-assumptions`).
- **OP-A8** BRST classification of non-local (multilocal light-ray) operators (v1 #2; OTHERS #5): settles `lem:method-ward-multi`, discharges `asm:appN-ward-product`; natural tool: auxiliary-field localization of Wilson lines.

**B. The general method.**
- **OP-B1** Integral-norm subtraction estimates (v1 #3 reworded per refdoc S44): (CS1)–(CS3) in integral norm on a deformed contour, even for the Sudakov form factor and the one-loop triangle (S63-12); discharge `asm:appN-collins`, `asm:appN-envelope`, `asm:appN-separation`, `asm:appN-contour`; a Minkowskian analogue of Weinberg's theorem; settles `thm:method-subtraction` and, with OP-A8 and OP-B2, `thm:disall-factorization`.
- **OP-B2** Cut-summed representations beyond DY-type graphs: discharge `asm:appN-cutsum` in general (SIA, SIDIS, TMD).
- **OP-B3** Renormalization inputs: multiplicative renormalizability of FFs and a Ward-identity-preserving IR regulator for partonic targets (`asm:appN-multren` (Z1)(Z2)); BPHZ vs DR compatibility (`asm:appN-uv`); settles `prop:pdf-timelike-dglap`, `thm:disall-renorm-compat` in application.
- **OP-B4** TMD inputs: `asm:appN-tmd` (T1)–(T4) to all orders; all-order equivalence of rapidity schemes; uniform $W+Y$ matching; settles `prop:tmd-evolution`, `thm:tmd-factorization` (with OP-C1).

**C. Glauber region and hadron–hadron collisions.**
- **OP-C1** Inclusive DY (v1 #1 reworded per refdoc S44): discharge `asm:appO-mixing`(c), `asm:appO-deformation`(b)–(d), `asm:appO-rewritten-cs` (and `asm:appO-lcopt`, `asm:appO-envelope`); equivalently a complete published all-order proof including Glauber subtractions; settles `thm:dy-factorization`, `thm:tmd-factorization`, `thm:dy-colour-singlet`, `thm:break-double-dy`.
- **OP-C2** H-emission endpoints and coincident SA/AS insertions (refdoc S44 #15): the non-analytic ordering weights at $k_j^+=0$ (`asm:appO-deformation`(d)).
- **OP-C3** Coloured final states (v1 #6): settle `conj:dy-coloured-final`, `conj:dy-polarized-jets`, `conj:power-twist3-pp`, `conj:coll-resolved-photo`.
- **OP-C4** Space-like violation, SLLs, mass singularities (v1 #11; OTHERS #3): PDF factorization for non-global observables beyond three loops; independent confirmation and resummation of coherence-violating logarithms in $N$-jettiness; settles `prop:break-mass-singularity`, the [C] part of `prop:jets-sll`.
- **OP-C5** MPI-sensitive observables and DPS (v1 #12; OTHERS #9): the fate of MPI-sensitive observables beyond pure Glauber ladders (soft emission off Glauber rungs); DPS with coloured final states; colour-correlated DPDs; settles `conj:break-dps-coloured`, `conj:break-pocket`, `prop:break-jet-veto` beyond the model.

**D. Beyond leading power.**
- **OP-D1** NLP factorization and endpoint refactorization (v1 #9; OTHERS #4): endpoint factorization beyond LL for processes with incoming hadrons; general refactorization conditions; Glauber cancellation at NLP (assumed in all NLP TMD work); reconciliation of NLP TMD evolution results; settles `prop:power-nlp-endpoint`, `prop:heavy-qcdf-endpoint`, `prop:thr-nlp`.
- **OP-D2** Power corrections and renormalons (v1 #14): settle `conj:power-renormalon-ht`, `conj:jets-hadronization`; the power $p$ of `thm:dy-factorization`.

**E. Specific processes.**
- **OP-E1** Positivity (v1 #7; OTHERS #7): settle `conj:pdf-positivity`; a non-perturbative determination of the scale $\mu_0$.
- **OP-E2** NRQCD production (v1 #8; OTHERS #10): beyond NNLO; the principle behind the two-loop confirmation; settles `conj:heavy-nrqcd-production`.
- **OP-E3** Small $x$ (v1 #10; OTHERS #8): unify collinear, TMD and high-energy factorization; saturation; the polarized small-$x$ discrepancy; collinear improvement of NLO BK; settles `prop:smallx-kt`, `conj:smallx-saturation`.
- **OP-E4** Exclusive processes (LAMET #6; YZLIU #9): GPD factorization near $x=\pm\xi$ beyond one loop; soft overlap bounds; near-threshold quarkonium beyond LO; settles `prop:excl-endpoint`, `prop:excl-near-threshold`.
- **OP-E5** Electroweak (OTHERS #11): resummation of non-factorizing EW logarithms at $Q\gg M_W$.

**F. Frontier (Ch22–Ch24)** [SYNC-FRONTIER].
- **OP-F1** Renormalizability of QCD with a space-like static source written out (BRST, $\delta m$ counterterm) (LAMET #2); settles `prop:lattice-renormalizability`.
- **OP-F2** Uniform twist expansion in Ioffe time; convergence vs asymptoticity of twist expansions in 4D QCD; the asymptotic nature of momentum-space LaMET expansions (LAMET #3, #13; YZLIU #7).
- **OP-F3** Large-distance control: exponential decay of hadronic Wilson-line correlators in a gauge theory with usable constants (LAMET #4); settles the hadronic matching (row VII.6) and the Fourier step.
- **OP-F4** Endpoint behaviour of twist-4 distributions (LAMET #5).
- **OP-F5** Quasi-TMD factorization beyond arguments (LAMET #7; YZLIU #1, #8): a Collins-style proof including (T3), the order of limits, a Glauber analysis for finite-length staples, the factorization of the large-momentum meson form factor used for $S_I$, ultrasoft-mode control; settles row VII.8.
- **OP-F6** Perturbative Wightman axioms for DR correlators at generic $\varepsilon$ (YZLIU #2; LAMET #8); DY = SIDIS soft factor by analyticity; settles row VII.9.
- **OP-F7** Universality of double-time-ordered soft functions with time-like vectors; the $e^+e^-$ soft factor in a Wightman framework (YZLIU #4); non-perturbative status of the complex-space-time Wilson-loop conjecture (YZLIU #3).
- **OP-F8** Higher orders and audits (LAMET #9–#12, #14; YZLIU #5, #6): N3LO non-singlet and NNLO singlet/gluon quasi-PDF kernels; twist-3 to all orders incl. zero modes; universality of renormalon prescriptions; audit of higher-order hybrid kernels against $\int d\xi\,C_{\rm hyb}=1$ [PENDING-VERIFY: E01]; colour-non-singlet DPDs and heavy-meson LCDAs; polarized and gluon quasi-TMDs; beyond-large-$\beta_0$ normalization of the heavy–light linear renormalon.
- **OP-F9** Power corrections and renormalon-free schemes in LaMET (v1 #13); settles the power-correction part of `thm:lattice-lamet`.

**Figures.** New (required): `fig:summary-status-map` (grid of process classes × levels, consistent with `tab:summary-master`; hollow circles for hadronic statements with their bottleneck `asm:`), `fig:summary-hypotheses` (bipartite graph register ↔ main [A]/R_cond theorems, generated from `\uses`); optional `fig:summary-chapter-dag`.

**Misconception box.** None (all items are summarized in the lessons).

**Pending.** All rows/problems marked [PENDING-VERIFY] or [SYNC-FRONTIER]/[SYNC-APP]/[SYNC-ASM] are finalized at the merge and after the verify patch.

---------------------------------------------------------------------------------------------------

# 附录 A–L (Appendices A–L, 35 pp)

---------------------------------------------------------------------------------------------------

General rules for the appendices (WRITER_SPEC_v2 §1.2, §4.5 item 5, §4.10 item 6, §6.3):
- Each appendix is a `\chapter` after `\appendix` in the master file, with `\label{app:<key>}`; the keys `appA` … `appL` are unchanged from v1.
- Statements use the same environments, tags, qualifiers and `\uses` rules as the main text. Pure mathematics carries no tag (`(数学，无标签)`).
- The appendices hold the complete proofs that the chapters announce (「完整论证见附录 X」); the list of promised proofs is WRITER_SPEC_v2 §6.3. A section that proves a chapter statement begins with 「\cref{…} 的证明」 and does not restate it; the chapter statement lists the appendix lemmas it uses in its own `\uses` (already done in the chapter entries of this file).
- Appendix statements may use statements of any chapter and of other appendices, provided no cycle arises. **Cycle rule applied here:** an appendix statement never lists a chapter statement that lists it (e.g. `prop:appB-rules` does not use `prop:prelim-wilson-rules`; `prop:appE-degree` does not use `prop:ir-power-counting`; `prop:appL-bare` does not use `thm:pdf-moments-local`). Within an appendix, statements are listed in reading order and use only earlier ones.
- Budgets: the rebalanced split of §0.2 (A 3, B 3, C 3, D 4, E 3, F 3, G 3, H 2, I 2, J 3, K 4, L 2 = 35 pp) — lead-author decision.
- Chapter numbers in the appendix texts are the **v2** numbers (e.g. GPDs: Ch19, not Ch18).

---------------------------------------------------------------------------------------------------

## Appendix A — 光锥坐标、Dirac 代数、加号分布与 Mellin 变换 / Light-front coordinates, Dirac algebra, plus distributions, Mellin transforms

`\label{app:appA}` · `appA_lightfront.tex` · **3 pp**

**Promised content (WRITER_SPEC_v2 §6.3).** Proofs of `lem:prelim-boost`, `lem:prelim-plus-expansion`, `lem:prelim-mellin`; the Fierz decomposition; the precise test-function class and the weak-convergence statement used in `cor:dis-weak-xspace` (refdoc S51).

**Sections.**
1. `sec:appA-lightfront` — light-front components, $d^4k=dk^+dk^-d^2k_T$, the boost proof of `lem:prelim-boost`; the dictionary $n_A,n_B$ ↔ SCET $n,\bar n$ ($\bar n\cdot p=\sqrt2p^+$) and the Ch19 convention ($n_A,n_B$, not $\bar n,n$).
2. `sec:appA-dirac` — the $\gamma^\pm$ algebra; projectors $P_+=\frac12\gamma^-\gamma^+$, $P_-=\frac12\gamma^+\gamma^-$; `lem:appA-fierz`.
3. `sec:appA-plus` — distributions: $[\cdot]_+$ at $z=1$, $\mathcal D_k(z)=[\ln^k(1-z)/(1-z)]_+$; **the test-function class and weak convergence** (`def:appA-test-functions`, `lem:appA-weak-convergence`; refdoc S51); the product convention (`lem:appA-plus-product`; in DY the whole-term plus of $(1+z^2)\mathcal D_1$ would shift the $\delta$ coefficient by $7C_F$, c_dy); the expansion $(1-z)^{-1-\varepsilon}=-\frac{\delta(1-z)}\varepsilon+\sum_k\frac{(-\varepsilon)^k}{k!}\mathcal D_k$ (proof of `lem:prelim-plus-expansion`); star distributions (SCET) and plus distributions at $\tau=0$ (event shapes).
4. `sec:appA-mellin` — Mellin transforms (`lem:appA-mellin-table`; proof of `lem:prelim-mellin`).

**Canonical statements** (in reading order).

* **引理 `lem:appA-fierz` — 共线 Fierz 分解** (数学，无标签) · v1 · `sec:appA-dirac`
  - **陈述.** For any $4\times4$ matrix $M$: $$P_+MP_-=\tfrac14\big[{\rm Tr}(\gamma^+M)\gamma^-+{\rm Tr}(\gamma^+\gamma_5M)\gamma_5\gamma^-+\textstyle\sum_{j=1,2}{\rm Tr}(\gamma^+\gamma^jM)\gamma^-\gamma^j\big].$$ It is the leading-twist projector for PDFs, DAs and GPDs (c_exclusive §1; VF-EXC-13).
  - **证明.** Full (completeness of the 16 Dirac matrices restricted by the projectors).
  - `% uses: none`

* **定义 `def:appA-test-functions` — 测试函数类与弱收敛** (no tag) · new (refdoc S51)
  - **陈述.** (a) For $\eta>0$, $\mathcal T_\eta$ is the space of functions $g$ continuous on $[0,1]$ with $|g(z)-g(1)|\le C(1-z)^\eta$; every $\mathcal D_k$ and every product $g\,\mathcal D_k$ in the convention of `lem:appA-plus-product` acts on $\mathcal T_\eta$, and plus distributions are defined as functionals on this class (not on $C^\infty_c$). (b) Structure functions as measures: $\mu_Q=F_2\,dx$ is a finite positive Borel measure on $[0,1]$, including the elastic point mass at $x=1$. (c) A family $\nu_Q$ of finite signed Borel measures on $[0,1]$ converges **weakly** to $\nu$ if $\int\phi\,d\nu_Q\to\int\phi\,d\nu$ for every $\phi\in C([0,1])$.
  - `\uses{def:prelim-plus}`

* **引理 `lem:appA-plus-product` — 乘积约定下的恒等式** (数学，无标签) · v1 · `sec:appA-plus`
  - **陈述.** $g(z)\mathcal D_k=g(1)\mathcal D_k+\frac{g(z)-g(1)}{1-z}\ln^k(1-z)$ for $g\in\mathcal T_\eta$; the second term is an integrable function.
  - **证明.** Full.
  - `\uses{def:prelim-plus, def:appA-test-functions}`

* **引理 `lem:appA-weak-convergence` — 由偶数矩得到弱收敛** (数学，无标签) · new (refdoc S51) · `sec:appA-plus`
  - **陈述.** Let $\nu_Q$ be finite signed Borel measures on $[0,1]$ with $\sup_Q|\nu_Q|([0,1])<\infty$, and let $k_0\ge0$. If $\int x^{2k}\,d\nu_Q\to0$ for every $k\ge k_0$, then $\int x^{2k_0}\phi\,d\nu_Q\to0$ for every $\phi\in C([0,1])$. For a fixed polynomial $\phi$ in $x^2$ the rate is that of the finitely many moments involved; **no rate uniform in $\phi\in C([0,1])$ follows** (`rem:appK-counterexamples`).
  - **证明.** Full: polynomials in $x^2$ are dense in $C([0,1])$ (Weierstrass in $t=x^2$); an $\varepsilon/3$ argument with the uniform bound on the total variation. Used in `cor:dis-weak-xspace` (Ch7).
  - `\uses{def:appA-test-functions}`

* **引理 `lem:appA-mellin-table` — Mellin 变换表** (数学，无标签) · v1 · `sec:appA-mellin`
  - **陈述.** $\langle\mathcal D_0,z^{N-1}\rangle=-S_1(N-1)$, $\langle\mathcal D_1,z^{N-1}\rangle=\frac12[S_1^2+S_2](N-1)$; large $N$: $-\ln\bar N$ and $\frac12(\ln^2\bar N+\zeta_2)$, $\ln\bar N=\ln N+\gamma_E$ (VF-THR-2); moments of $P_{ij}$ (VF-PDF-8) and of $C_2^q$, $C_2^g$ (VF-DIS-8); continuation $S_1(N)\mapsto\psi(N+1)+\gamma_E$ (`prop:appK-continuation`, pointer for uniqueness).
  - **证明.** Full.
  - `\uses{def:prelim-mellin, def:prelim-plus}`

**Sources.** c_exclusive §1; c_dy §§3, 6; c_scet §1; c_dis; critic c6; refdoc S51 (test-function class, weak convergence).

---------------------------------------------------------------------------------------------------

## Appendix B — Wilson 线：Feynman 规则、程函恒等式与尖点 / Wilson lines: Feynman rules, eikonal identities, cusp

`\label{app:appB}` · `appB_wilson.tex` · **3 pp** (−1: the eikonal-identity proofs are compressed, since Ch3 states the rules with the universal rule)

**Promised content.** Proofs of `prop:prelim-wilson-rules`, `lem:prelim-eikonal-identity`; the one-loop cusp. If `OUTLINE_frontier.md` places the partial-exponentiation lemma of Ch23 here, it is added as `sec:appB-partial` (≤ 0.5 pp; label key `appB`) [SYNC-FRONTIER].

**Sections.**
1. `sec:appB-definition` — the binding definition $W[b,a]=P\exp(ig\int_a^bdz\cdot A)$ (later points to the left; $W\to U(b)WU^\dagger(a)$); composition, retracing, unitarity, adjoint lines. **Convention warning:** Collins 2011 uses $g\to-g$ relative to us (D4; the $g$-sign item of [PENDING-VERIFY: E27]).
2. `sec:appB-rules` — `prop:appB-rules` (proves `prop:prelim-wilson-rules`).
3. `sec:appB-eikonal` — `lem:appB-shuffle` (proves `lem:prelim-eikonal-identity`); the Ward identity of a semi-infinite Wilson line (VF-WL-13), used in App F; `prop:appB-webs`.
4. `sec:appB-cusp` — `prop:appB-cusp-oneloop`; the two-loop coefficient.

**Canonical statements** (in reading order).

* **命题 `prop:appB-rules` — Wilson 线的 Feynman 规则** [R, R_def] · v1 · `sec:appB-rules`
  - **陈述.** With $A(x)=\int\!đ^4k\,e^{-ik\cdot x}\tilde A(k)$: $W[\infty n,0]\ni gt^an^\mu\tilde A_\mu(k)/(n\cdot k-i0)$ and $W[-\infty n,0]\ni gt^an^\mu\tilde A_\mu(k)/(n\cdot k+i0)$; future minus past: $2\pi i\,gt^an^\mu\delta(n\cdot k)$; multi-gluon rule: nested denominators $\prod_j[n\cdot(k_1+\dots+k_j)\mp i0]^{-1}$ with the colour ordering (VF-WL-1/2/3; c_wilson universal rule; c_glauber §0.2).
  - **证明.** Full (expansion of the path-ordered exponential with the adiabatic factor).
  - `\uses{def:prelim-wilson}`

* **引理 `lem:appB-shuffle` — 程函恒等式（洗牌积）** (数学，无标签) · v1 · `sec:appB-eikonal`
  - **陈述.** For complex $y_1,\dots,y_m$ with all partial sums non-zero: $\sum_{\sigma\in S_m}\prod_{j=1}^m\frac1{y_{\sigma1}+\dots+y_{\sigma j}}=\prod_{j=1}^m\frac1{y_j}$. With $y_j=n\cdot k_j+i\epsilon$ this is the eikonal identity at **finite** regulator exactly when the $j$-th denominator carries $+ij\epsilon$, i.e. for the adiabatic regulator $e^{-\epsilon|t|}$; with a uniform $+i\epsilon$ in every eikonal denominator it holds only in the limit $\epsilon\to0$, as distributions (VF-WL-4; c_wilson, [PENDING-VERIFY: N26] — novelty not claimed). This proves `lem:prelim-eikonal-identity`.
  - **证明.** Full (induction on $m$ by the last factor).
  - `% uses: none`

* **命题 `prop:appB-webs` — 非阿贝尔指数化** [A] · v1 · `sec:appB-eikonal`
  - **陈述.** Correlators of Wilson lines meeting at a point exponentiate in terms of webs with modified colour factors (`Gatheral1983`, `FrenkelTaylor1984`).
  - **证明.** Sketch (replica/combinatorial argument at the level of the cited papers).
  - **地位与缺口.** All-order combinatorial argument in the literature for two lines; at $O(g^2)$ the statement is [R, R_def] (`prop:sudakov-webs`, Ch5, pointer); multi-leg webs and their renormalization are not needed in this book.
  - `\uses{prop:appB-rules, lem:appB-shuffle}`

* **命题 `prop:appB-cusp-oneloop` — 单圈尖点反常维度** [R, R_PT] · v1 · `sec:appB-cusp`
  - **陈述.** (One loop.) For two time-like lines with Minkowskian cusp angle $\beta$ ($\cosh\beta=v_1\cdot v_2$): $\Gamma_{\rm cusp}(\beta)=\frac{\alpha_sC_F}\pi(\beta\coth\beta-1)+O(\alpha_s^2)$; the $-1$ is the Wilson-line self-energy ($\Gamma(0)=0$ for a straight line); the light-like limit is linear in $\beta$ and gives the light-like cusp $\Gamma_{\rm cusp}=\frac{\alpha_sC_F}\pi\times$(rapidity) (VF-CONV-23; literature `Polyakov1980`, `BrandtNeriSato1981`, `KorchemskyRadyushkin1987`).
  - **证明.** Full (one-loop exchange between the two lines plus self-energies in DR; c_tmd R4: the UV pole of the one-loop soft factor is two cusps with this anomalous dimension).
  - **Remark (two loops, quoted).** $\Gamma_1=4C_F[(\frac{67}9-\frac{\pi^2}3)C_A-\frac{20}9T_Fn_f]$ in the normalization of `BecherSchwartz2008`; the arXiv version of that paper has a spurious $C_F$ in its App. A (c_scet §6 item 10; VF-SCET-16) [PENDING-VERIFY: E23 — App Q candidate; check the journal version].
  - `\uses{prop:appB-rules, def:prelim-dr-conventions, def:prelim-msbar}`

**Sources.** c_wilson §§2–4; c_glauber §0.2; c_scet §6; critic D-items.

---------------------------------------------------------------------------------------------------

## Appendix C — 维数正规化积分与相空间 / Dimensional-regularization integrals and phase space

`\label{app:appC}` · `appC_dimreg.tex` · **3 pp**

**Promised content.** DR integrals and phase spaces used in Ch6, Ch10, Ch12; the $d$-dimensional splitting kernels with the averaging conventions (refdoc S51).

**Sections.**
1. `sec:appC-msbar` — $\overline{\rm MS}$ with the binding $S_\varepsilon=(4\pi)^\varepsilon e^{-\varepsilon\gamma_E}$ and the comparison with Collins' $(4\pi)^\varepsilon/\Gamma(1-\varepsilon)$ (`rem:appC-Seps`); **the $D$-dimensional splitting kernels with the averaging conventions** (`rem:appC-d-kernels`, refdoc S51).
2. `sec:appC-integrals` — `lem:appC-bubble`, `lem:appC-ibp`.
3. `sec:appC-phase-space` — `lem:appC-phase-space`.
4. `sec:appC-formfactor` — the massless quark form factor exact in $\varepsilon$, $F^{(1)}_{\rm bare}=\frac{\alpha_sC_F}{4\pi}(\frac{4\pi\mu_0^2}{Q^2})^\varepsilon c_\Gamma[-\frac{2-\varepsilon+2\varepsilon^2}{\varepsilon^2(1-2\varepsilon)}]$ (VF-SUD-1; c_dis = c_scet row 7), and its time-like continuation (VF-SUD-2).

**Canonical statements** (in reading order).

* **注 `rem:appC-Seps` — $S_\varepsilon$ 约定的影响** (no tag) · v1 · `sec:appC-msbar`
  - $e^{-\varepsilon\gamma_E}\Gamma(1-\varepsilon)=1+\frac{\pi^2}{12}\varepsilon^2+O(\varepsilon^3)$. This changes finite constants wherever $1/\varepsilon^2$ poles are subtracted (TMD $\tilde C$ and $\mathcal H$; `rem:tmd-scheme-constants`), never physical cross sections (VF-CONV-3).

* **注 `rem:appC-d-kernels` — $D$ 维劈裂核与平均约定** (no tag) · new (refdoc S51) · `sec:appC-msbar`
  - Real-emission kernels in CDR (VF-PDF-6): $\hat P_{qq}=C_F[\frac{1+z^2}{1-z}-\varepsilon(1-z)]$, $\hat P_{gq}=C_F[\frac{1+(1-z)^2}z-\varepsilon z]$, $\hat P_{qg}=T_F[1-\frac{2z(1-z)}{1-\varepsilon}]$, $\hat P_{gg}=2C_A[\frac z{1-z}+\frac{1-z}z+z(1-z)]$, with the averages $\frac1{D-2}=\frac1{2(1-\varepsilon)}$ over gluon polarizations, $\frac12$ over quark spins, and the colour averages $\frac1{N_c^2-1}$, $\frac1{N_c}$ (VF-CONV-6). Averaging over 2 gluon polarizations instead gives $C_2^g\to C_2^g+P_{qg}$, $\Delta_{qg}\to\Delta_{qg}+P_{qg}$ (VF-CONV-6). Used in `prop:pdf-lo-kernels`, `prop:disall-nlo`, `prop:dy-nlo` (pointers).

* **引理 `lem:appC-bubble` — 单圈两点函数** (数学，无标签) · v1 · `sec:appC-integrals`
  - **陈述.** $\int\frac{d^Dk}{i\pi^{D/2}}\frac1{(-k^2)^a(-(k-q)^2)^b}=(-q^2)^{D/2-a-b}G(a,b)$, $G(a,b)=\frac{\Gamma(a+b-D/2)\Gamma(D/2-a)\Gamma(D/2-b)}{\Gamma(a)\Gamma(b)\Gamma(D-a-b)}$; $c_\Gamma=\frac{\Gamma(1+\varepsilon)\Gamma^2(1-\varepsilon)}{\Gamma(1-2\varepsilon)}$ (used by c_ee for $r_1G(1,1)^2+r_2G(1,1)G(1+\varepsilon,1)$).
  - **证明.** Full (Feynman parameters).
  - `\uses{def:prelim-dr-conventions}`

* **引理 `lem:appC-ibp` — 分部积分（三角规则）** (数学，无标签) · v1 · `sec:appC-integrals`
  - **陈述.** The triangle rule; the two-loop propagator integral $\hat I(1,1,1,1,1)=6\zeta_3$ (VF-EE-7 context).
  - **证明.** Full.
  - `\uses{lem:appC-bubble}`

* **引理 `lem:appC-phase-space` — $D$ 维相空间** (数学，无标签) · v1 · `sec:appC-phase-space`
  - **陈述.** Two-body: $\int d\Phi_2=\frac1{8\pi}(\frac{4\pi}s)^\varepsilon\frac{\Gamma(1-\varepsilon)}{\Gamma(2-2\varepsilon)}$ (equals VF-DY-4 integrated over $v$ in the massless limit); three-body for $e^+e^-$ in Dirichlet form; DIS/DY $2\to2$ phase spaces exact in $\varepsilon$ (c_dis, c_dy).
  - **证明.** Full.
  - `\uses{def:prelim-dr-conventions}`

**Sources.** c_ee §§3–4; c_dis; c_dy; c_pdf §4.1; c_scet row 7; refdoc S51.

---------------------------------------------------------------------------------------------------

## Appendix D — Landau 方程与 Coleman–Norton 定理 / Landau equations and the Coleman–Norton theorem

`\label{app:appD}` · `appD_landau.tex` · **4 pp**

**Promised content.** Proofs of `thm:ir-landau-alpha`, `thm:ir-landau-momentum`, `prop:ir-coleman-norton`; `sec:appD-alpha` with the Feynman-parameter proof and its caveats and the details of `rem:ir-euclid-corners` (refdoc S52). The refdoc's +2 pp are absorbed by giving the alternative proof as a remark (≤ 1 p).

**Sections.**
1. `sec:appD-gordan` — `lem:appD-gordan`.
2. `sec:appD-momentum` — proof of `thm:ir-landau-momentum`: the local deformation $k\to k+i\epsilon v$ shows that a non-pinched point admits a deformation (c_regions L3; blueprint S1).
3. `sec:appD-alpha` — the $\alpha$-representation: `lem:ir-envelope` and the proof of `thm:ir-landau-alpha` (c_regions L1–L2); **`rem:appD-parameter-proof`** (refdoc S52); the details of `rem:ir-euclid-corners`: for the off-shell triangle $\mathcal F=m^2\alpha_0(\alpha_1+\alpha_2)+Q^2\alpha_1\alpha_2$, and in Euclidean non-exceptional kinematics the only Landau solutions are at the simplex corners (zero-momentum massless lines), so Euclidean IR finiteness follows from power counting, not from the absence of pinches (VF-REF-17; misconception M29; optional `fig:ir-landau-simplex`, owned by Ch4).
4. `sec:appD-cn` — derivation of `prop:ir-coleman-norton`: $\alpha_jk_j=\Delta x_j$, interpreted as a classical process.
5. `sec:appD-caveats` — what is **not** proved: sufficiency and the global existence of the deformation (`rem:ir-landau-status`; Collins 2011 §5.4.3: "no published complete proof"); the preprints claiming complete proofs `Collins:2020euz` (proof only in a preprint, [PENDING-VERIFY: A08]) and `Muhlbauer:2020kut`; their status and the reduction of the physical-region criterion to Gordan's alternative are discussed in Ch24 (pointer, [PENDING-VERIFY: N02]). Literature: `Landau1959`, `Nakanishi:1959jzx`, `ColemanNorton1965`, `EdenEtAl1966`, `Pham:2011SingInt`, `Fevola:2023kaw`, `Sterman1993`.

**Canonical statements** (in reading order).

* **引理 `lem:appD-gordan` — Gordan 择一定理** (数学，无标签) · v1 · `sec:appD-gordan`
  - **陈述.** For $u_1,\dots,u_m\in\mathbb R^d$ exactly one of the following holds: (i) there is $\alpha\in\mathbb R^m_{\ge0}\setminus\{0\}$ with $\sum_j\alpha_ju_j=0$; (ii) there is $v\in\mathbb R^d$ with $v\cdot u_j>0$ for all $j$ (`Gordan1873`; VF-REG-1…6).
  - **证明.** Full (separating hyperplane; the minimal-norm point of the convex hull gives $v$ in (ii)).
  - `% uses: none`

* **注 `rem:appD-parameter-proof` — Landau 条件的 Feynman 参数证明及其注意事项** (no tag) · new (refdoc S52) · `sec:appD-alpha`
  - The alternative route to `thm:ir-landau-alpha`: with $\mathcal F$ the second Symanzik polynomial, $\eta_j=\alpha_j\partial_j\mathcal F$; at a stationary point on a face of the simplex the envelope identity (`lem:ir-envelope`) and the homogeneity of $\mathcal F$ give the Landau conditions. **Caveats:** (i) it establishes the conditions as **necessary** for a singularity of the parametric integral, not sufficiency or the existence of a global deformation; (ii) boundary points of the simplex (vanishing $\alpha_j$) need the face-by-face treatment; (iii) Landau points in parameter space and pinches of the momentum-space contour are different notions, which must not be identified without argument (`Collins:2020euz` App. D1). This book's main proof (constraint-preserving deformation, `sec:appD-momentum`) does not depend on this remark.

**Sources.** c_regions §1 (VF-REG-1…6); blueprint S1; refdoc S52 (alternative proof, caveats, VF-REF-17).

---------------------------------------------------------------------------------------------------

## Appendix E — 幂次计数公式的推导 / Derivation of the power-counting formula

`\label{app:appE}` · `appE_powercount.tex` · **3 pp**

**Promised content.** `prop:ir-power-counting` via `prop:appE-degree` (boost-and-dimension proof); `rem:appE-actual-bound` (refdoc S52).

**Sections.**
1. `sec:appE-units` — Sterman units: $\lambda$ for collinear lines, $\lambda_S=\lambda^2$ for soft lines; scaling of measures, propagators and numerators, including the boost factors of good and bad components.
2. `sec:appE-formula` — `prop:appE-degree` with the **boost-and-dimension proof** (refdoc S52; optional `fig:appE-boost`); `rem:appE-actual-bound`.
3. `sec:appE-examples` — reduced diagrams for $e^+e^-$, DIS and DY with explicit degrees (c_regions `fig:pc-ee`, `fig:pc-dis`, `fig:pc-dy`); the Glauber region is $\lambda^0$ (c_glauber §1.1 [P5]; VF-GLA-1).

**Canonical statements** (in reading order).

* **命题 `prop:appE-degree` — 约化图的超表观红外发散度** [R, R_PT] · v1 (+ refdoc S52) · `sec:appE-formula`
  - **陈述.** For a reduced diagram $R$ with the region scalings of `def:ir-scalings`, the superficial degree $\omega(R)$ is the formula of `prop:ir-power-counting` (VF-REG-8): the contribution of a neighbourhood of the pinch surface scales as $\lambda^{\omega(R)}$ (an E-S statement).
  - **证明.** Full, in two forms: (a) dimension counting plus boost counting (blueprint S2; c_regions P2); (b) **boost-and-dimension argument** (refdoc S52): a boost along the jet direction maps the collinear scaling to an isotropic one, so the degree is the mass dimension of the subgraph corrected by the boost weights of the external good/bad components.
  - `\uses{def:ir-scalings, lem:prelim-boost, def:prelim-feynman-rules}`

* **注 `rem:appE-actual-bound` — 从超表观度到实际界** [A] · v1 (+ refdoc S52) · `sec:appE-formula`
  - **陈述.** The superficial degree bounds the actual contribution of the region, up to logarithms, once nested regions are controlled (c_regions §2.4).
  - **地位与缺口.** `prop:appE-degree` is a scaling statement (E-S); turning it into an integral-norm bound (E-N) uniformly over nested neighbourhoods is exactly `asm:appN-envelope` (technical assumption, [A]-level). This is why `thm:ir-leading-regions` is [A]. Upgrade: a proof of `asm:appN-envelope`.
  - `\uses{prop:appE-degree, asm:appN-envelope}`

**Sources.** c_regions §2 (VF-REG-7…12); c_glauber §1.1; refdoc S52.

---------------------------------------------------------------------------------------------------

## Appendix F — 图形 Ward 恒等式 / Graphical Ward identities

`\label{app:appF}` · `appF_ward.tex` · **3 pp**

**Promised content.** Proofs of `prop:method-ward-one`, `prop:method-ward-tree`, outline of `lem:method-ward-multi`; the telescoping example; Grammer–Yennie with its $i0$ (refdoc S52).

**Sections.**
1. `sec:appF-one` — proof of `prop:method-ward-one` from `thm:prelim-slavnov-taylor` (external physical partons on shell); **`ex:appF-telescoping`** (refdoc S52).
2. `sec:appF-two` — `prop:appF-two-gluon`.
3. `sec:appF-induction` — `prop:appF-induction`.
4. `sec:appF-gy` — Grammer–Yennie: collinear and soft forms **with their $i0$**: DIS $K_{\mu\nu}=k_\mu w_{2\nu}/(k\cdot w_2-i0)$ (future-pointing), DY $+i0$ (past-pointing); the direction is fixed by the $i0$ of the replaced propagators and, for DY, by the contour, not by the pure-gauge argument (`rem:method-pure-gauge`: abelian/tree status of that argument). The original GY K-photon is symmetric ($b_kk_\mu k_\nu$); the one-sided form with $i0$ is the adaptation used in Collins 2011 (`GrammerYennie1973` cited only together with `SenIndumathiChoudhury2019`) [PENDING-VERIFY: A18]; errata to Collins 2011 eqs. (11.4)–(11.6) as flagged by c_wilson [PENDING-VERIFY: E27 — author-corrected class Q2]; the numerical suppression table (VF-WL-10/11).

**Canonical statements** (in reading order).

* **例 `ex:appF-telescoping` — 有限 Wilson 线的伸缩恒等式** (no tag) · new (refdoc S52) · `sec:appF-one`
  - In our conventions, for the segment along $n_B$ from $0$ to $w^-$: $W^{(1)}[w^-,0]\ni g\,t^a\,n_B^\mu\tilde A_\mu(k)\,\frac{1-e^{-ik^+w^-}}{k^+}$ (entire in $k^+$, no $i0$ needed); it equals the difference of two semi-infinite lines, $\frac1{k^+-i0}-\frac{e^{-ik^+w^-}}{k^+-i0}$, in which the $i0$ cancels. Contracting a longitudinal gluon into the operator vertex of the light-ray operator telescopes in the same way, which is the operator-vertex term of `prop:method-ward-one` (signs re-derived in our conventions; c_glauber §2 telescoping identity, [PENDING-VERIFY: N19]).
  - `\uses{def:prelim-wilson, prop:appB-rules}`

* **命题 `prop:appF-two-gluon` — 两个纵向胶子：树图层次的完整证明** [R, R_PT] · v1 · `sec:appF-two`
  - **陈述.** (Tree level.) In DIS kinematics, two collinear K-gluons give exactly $(n_B\cdot k_1)(n_B\cdot k_2)W^{(2)}_{ab}[\infty n_B,0]H_0$; the path ordering comes from the commutator term, and no ghost or three-gluon graph contributes at this order; for $q\bar q\to g^*g^*$ with unphysical polarizations the ghost term is explicit (VF-WL-8/9; c_wilson §5.4–5.5).
  - **证明.** Full. This proves `prop:method-ward-tree`(b).
  - `\uses{prop:method-ward-one, prop:appB-rules, def:prelim-feynman-rules, thm:prelim-slavnov-taylor}`

* **命题 `prop:appF-induction` — 多胶子情形的归纳论证** [A] · v1 · `sec:appF-induction`
  - **陈述.** The inductive step of `lem:method-ward-multi`: on-shell physical external partons, approximated (not exact) collinear momenta, ghost terms cancelling or absorbed.
  - **证明.** Sketch (Collins 2011 §11.9, §11.3.2). `Collins:2008sg`: remainder of the naive identity.
  - **地位与缺口.** Assumes the BRST classification of the non-local operators that appear (Collins 2011 §11.3.2; `rem:appJ-nonlocal`), formalized as `asm:appN-ward-product` ([A]-level); the moment reduction of the bilocal case is a frontier result (Ch24, pointer, [PENDING-VERIFY: N04]).
  - `\uses{prop:method-ward-one, prop:appF-two-gluon, asm:appN-ward-product}`

**Sources.** c_wilson §§5–7; `GrammerYennie1973`; `SenIndumathiChoudhury2019` (only next to `GrammerYennie1973`); refdoc S52.

---------------------------------------------------------------------------------------------------

## Appendix G — 单圈与两圈计算细节 / Details of one- and two-loop calculations

`\label{app:appG}` · `appG_oneloop.tex` · **3 pp** (−1: the Ch2 one-loop renormalization constants, the Ch10 ladder example and the Ch12 worked examples are printed in full in their chapters and not repeated) · calculations only (no new canonical statements)

**Promised content.** Detailed one-loop calculations of Ch6, Ch7 (`prop:dis-c-oneloop`), Ch8, Ch10, Ch12, Ch14.

**Sections.**
1. `sec:appG-ee` — $e^+e^-$: real and virtual in one normalization; the warning about the separate constants; the two-loop $\Pi$ via IBP (c_ee §§3–4; VF-EE-4…8).
2. `sec:appG-dis` — DIS real emission exact in $\varepsilon$ ($R_2^q$, $R_L^q$, $R_2^g$, $R_L^g$) and the Laurent table (c_dis; VF-DIS-3…6).
3. `sec:appG-dy` — DY real emission exact in $\varepsilon$, the origin of $\frac{2\pi^2}3$, and mass factorization (c_dy; VF-DY-3…9).
4. `sec:appG-pdf` — the one-loop quark PDF with a gluon mass, graph by graph, and the local-operator anomalous dimensions (c_pdf §§3, 6; VF-PDF-3, VF-PDF-14).
5. `sec:appG-tmd` — the one-loop soft factor and unsubtracted TMD with Collins' regulator (c_tmd DERIVATION §3, R1–R9; draft `research/c_tmd/tex/tmd_oneloop.tex`); the space-like line self-energy is non-integrable (VF-REF-19).

---------------------------------------------------------------------------------------------------

## Appendix H — 文献导读 / Annotated bibliography

`\label{app:appH}` · `appH_literature.tex` · **2 pp** · no statements

Organized by topic, one or two sentences per item, using the warnings of `REFS_NOTES_v2.md` §1 (and v1 `REFS_NOTES.md`):
- **Textbooks:** `Collins2011` (section numbers of the 2011 edition; `Collins2023` is the Open Access reissue), `Sterman1993`, `EllisStirlingWebber1996`, `Field1989`, `Muta2010`, `Collins1984`, `PeskinSchroeder1995`, `Weinberg1996`, `BecherBroggioFerroglia2015`, `KovchegovLevin2012`; for Ch2 the QCD-basics textbooks of REFS_NOTES_v2 §3.1.
- **Reviews:** `CollinsSoperSterman1989`, `CollinsSoper1987`, `Sterman:1995fz`, `StermanEtAl1995`, `Beneke1999`, `Diehl2003`, `BelitskyRadyushkin2005`, `BoussarieEtAl2023`, `AngelesMartinezEtAl2015`, `BrambillaEtAl2011`, `JiEtAl2021`, `Constantinou:2020hdm`, `Diehl:2017wew`, `GelisEtAl2010`; frontier reviews as listed in REFS_NOTES_v2 §3.2–§3.4.
- **Historical:** `Feynman1969`, `BjorkenPaschos1969`, `Bjorken1969`, `DrellYan1970`.
- Rules: the reference document is never cited or described (WRITER_SPEC_v2 §6.10); for every paper with a published erratum the corrected version is used (rule E33); attribution traps A01–A28 (REFS_NOTES_v2 §1.5) apply to the annotations.

---------------------------------------------------------------------------------------------------

## Appendix I — 维数正规化中的 $\gamma_5$ / $\gamma_5$ in dimensional regularization

`\label{app:appI}` · `appI_gamma5.tex` · **2 pp**

**Promised content.** The Larin scheme (used by `thm:dis-bjorken`, `thm:coll-g1-moments`, `prop:coll-anomaly-scheme`).

**Sections.** `sec:appI-hvbm` (`def:appI-hvbm`); `sec:appI-larin` (`prop:appI-larin`); `sec:appI-anomaly` (`rem:appI-anomaly`).

**Canonical statements** (in reading order).

* **定义 `def:appI-hvbm` — HVBM 方案** (no tag) · v1
  - **陈述.** $\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3$, $\epsilon^{0123}=+1$, ${\rm Tr}(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma\gamma_5)=-4i\epsilon^{\mu\nu\rho\sigma}$ (VF-CONV-10; checked on all 256 index sets by c_exclusive); $\gamma^\mu=\bar\gamma^\mu+\hat\gamma^\mu$, with $\gamma_5$ anticommuting with $\bar\gamma^\mu$ and commuting with $\hat\gamma^\mu$ (`tHooftVeltman1972`, `BreitenlohnerMaison1977a`).
  - `\uses{def:prelim-gamma5}`

* **命题 `prop:appI-larin` — Larin 方案与非单态轴矢流的有限重整化** [R, R_PT] · v1
  - **陈述.** The axial current is written with $\gamma^\mu\gamma_5\to-\frac i6\epsilon^{\mu\nu\rho\sigma}\gamma_\nu\gamma_\rho\gamma_\sigma$ in the binding convention $\epsilon^{0123}=+1$ (VF-CONV-24; the literature form $\gamma_\mu\gamma_5=\frac i6\epsilon_{\mu\nu\rho\sigma}\gamma^\nu\gamma^\rho\gamma^\sigma$ assumes $\epsilon_{0123}=+1$). A finite renormalization $Z_5^{\rm ns}=1-4C_F\frac{\alpha_s}{4\pi}+O(\alpha_s^2)$ restores the anticommuting Ward identity (`Larin:1993tq`, `LarinVermaseren1991`; VF-POL-1: coefficient **quoted**, status T — cite, do not claim a re-derivation). Non-singlet results (Bjorken) are then scheme independent; singlet: the axial anomaly makes the split $\Delta\Sigma/\Delta G$ scheme dependent (`prop:coll-anomaly-scheme`, pointer).
  - **证明.** Cited (complete in the literature); the sign of the replacement is re-derived in our convention (VF-CONV-24).
  - `\uses{def:appI-hvbm, thm:prelim-composite-renorm, def:prelim-msbar}`

* **注 `rem:appI-anomaly` — 轴矢反常** (no tag) · v1
  - The ABJ anomaly of the singlet current in the binding normalization (**writer derives; normalization to verify**); consequence: the first moment of the $\gamma^*g$ box differs between HVBM and anticommuting-$\gamma_5$ treatments (`AltarelliRoss1988`, `CarlitzCollinsMueller1988`).

**Sources.** c_exclusive §1; critic c4 (Bjorken, Crewther); `MertigVanNeerven1996`, `Vogelsang1996` for the polarized NLO kernels.

---------------------------------------------------------------------------------------------------

## Appendix J — BRST 对称性与割图中的鬼场 / BRST symmetry and ghosts in cut diagrams

`\label{app:appJ}` · `appJ_brst.tex` · **3 pp** (+1: `lem:appJ-cut-hermiticity`, refdoc S53)

**Promised content.** `lem:prelim-brst-nilpotent` and `prop:qcd-brst-cohomology` details, `thm:prelim-slavnov-taylor` details, ghost cuts, the context of `thm:prelim-composite-renorm`; `lem:appJ-cut-hermiticity` (refdoc S53).

**Sections.**
1. `sec:appJ-brst` — BRST transformations in the binding conventions; the nilpotency computation (proof details of `lem:prelim-brst-nilpotent`); the Kugo–Ojima quartet mechanism (details of `prop:qcd-brst-cohomology`; `KugoOjima1979`, `BecchiRouetStora1975`, `BecchiRouetStora1976`, `Tyutin1975`); the derivation of `thm:prelim-slavnov-taylor` from `lem:qcd-st-regularized` in the form used by factorization proofs.
2. `sec:appJ-cuts` — `prop:appJ-ghost-cuts`; **`lem:appJ-cut-hermiticity`**; the setting of `asm:appN-cutsum` (refdoc S53): why single cut graphs, and IR regularization by gluon masses, do not give a cut-summed representation with a common domain of the subtraction terms — this is what `asm:appN-cutsum` assumes and App N uses.
3. `sec:appJ-operators` — `prop:appJ-local-operators`; `rem:appJ-nonlocal`.

**Canonical statements** (in reading order).

* **命题 `prop:appJ-ghost-cuts` — 割图中的鬼场贡献** [R, R_PT] · v1 · `sec:appJ-cuts`
  - **陈述.** Summing cut gluon lines with $-g_{\mu\nu}$ and subtracting the ghost cuts equals the physical-polarization sum; tree-level check $q\bar q\to gg$ (VF-WL-9). This completes `thm:prelim-cutting-rules` for gauge theories and proves the ghost part of `prop:prelim-unitarity`.
  - **证明.** Full (BRST cohomology: unphysical quartets cancel in cut sums).
  - `\uses{def:prelim-brst, lem:prelim-brst-nilpotent, prop:qcd-brst-cohomology, def:prelim-cut, thm:prelim-cutting-rules}`

* **引理 `lem:appJ-cut-hermiticity` — 割图规则的厄米性** [R, R_def] · new (refdoc S53) [PENDING-VERIFY: S63-8, X1, N14] (class K3 of WRITER_SPEC_v2 §6.5: a sharpened explicit result, never marked new) · `sec:appJ-cuts`
  - **陈述.** (a) With Hermitian ghost fields (e.g. Kugo–Ojima's $c,\bar c$ with $\mathcal L_{\rm FP}=-i\partial^\mu\bar c^aD_\mu^{ab}c^b$; the convention must be matched to `def:qcd-fp` and to `prop:appJ-ghost-cuts` — **verify**), the vertex factors on the two sides of the final-state cut are complex conjugates of each other, including the three-gluon, four-gluon and ghost vertices. (b) The on-shell numerators (numerator polynomials evaluated at on-shell light-front energies, as they appear in the light-cone-ordered representation of App O) are the same polynomials on both sides of a forward cut graph. Hence the cut rules are Hermitian. Consequence: clause (iii) of the original hermiticity hypothesis becomes a lemma, so `asm:appO-lcopt` keeps only its clauses (i)(ii) [SYNC-ASM].
  - **证明.** Full (inspection of the Feynman rules of `def:prelim-feynman-rules` and of the cut conventions of `def:prelim-cut`).
  - `\uses{def:prelim-feynman-rules, def:qcd-fp, def:prelim-cut}`

* **命题 `prop:appJ-local-operators` — 规范不变定域算符的重整化与混合** [R, R_PT] · v1 · `sec:appJ-operators`
  - **陈述.** Gauge-invariant local operators mix under renormalization only with gauge-invariant operators, BRST-exact operators and equation-of-motion (EOM) operators; the latter two have vanishing physical matrix elements (`Joglekar:1975nu`, `Joglekar:1976eb`, `Joglekar:1976pe`, `Kluberg-Stern:1974iel`, `Kluberg-Stern:1974nmx`, `Kluberg-Stern:1975ebk`, `Henneaux:1993jn`, `Collins:1994ee`). The BRST-language form of `thm:prelim-composite-renorm`, with the caveats printed there (forward on-shell gluon matrix elements and alien operators, [PENDING-VERIFY: S63-3, S63-4]); App M §M.6 uses it.
  - **证明.** Sketch with literature locations (the cited papers give complete proofs for the local case).
  - `\uses{thm:prelim-composite-renorm, prop:qcd-brst-cohomology, def:prelim-brst}`

* **注 `rem:appJ-nonlocal` — 非定域算符** [A] · v1 · `sec:appJ-operators`
  - **陈述.** The analogous classification for the non-local operators of factorization proofs (Wilson-line operators, products of light-ray operators) holds.
  - **地位与缺口.** Assumed in Collins 2011 §11.3.2 (pp. 407–410, page numbers [PENDING-VERIFY: A18]); in this book it is part of `asm:appN-ward-product` ([A]-level); a moment reduction of the bilocal PDF case to the local theorem is a frontier result (Ch24, pointer, [PENDING-VERIFY: N04]); the multilocal case is open (Ch25 open problem OP-A8).
  - `\uses{prop:appJ-local-operators, asm:appN-ward-product}`

**Sources.** `KugoOjima1979`; `BecchiRouetStora1975`, `BecchiRouetStora1976`, `Tyutin1975`; c_wilson §5.5; refdoc S53.

---------------------------------------------------------------------------------------------------

## Appendix K — 矩问题与解析延拓引理 / Moment problems and continuation lemmas

`\label{app:appK}` · `appK_moments.tex` · **4 pp** (+1: `lem:appK-entire`, `lem:appK-markov`, refdoc S50). All pure mathematics, no tags; complete proofs (c_pdf §7, s6 15/15 PASS; own proofs of classical facts, novelty not claimed [PENDING-VERIFY: N23]).

**Promised content.** The lemmas behind `rem:dis-uniqueness` and `rem:pdf-ns-plusminus`; `lem:appK-entire` (for `prop:dis-dispersion-np`), `lem:appK-markov` (for `lem:dis-ope-segment`, `thm:dis-fixed-n`).

**Sections.** `sec:appK-hausdorff` (uniqueness from moments); `sec:appK-continuation` (Carlson, continuation, Müntz–Szász); `sec:appK-entire` (**new**: entire functions of controlled growth; Markov's inequality); `sec:appK-counterexamples`.

**Canonical statements** (in reading order).

* **引理 `lem:appK-hausdorff` — Hausdorff 唯一性** (数学，无标签) · v1
  - **陈述.** A finite signed Borel measure on $[0,1]$ with all moments zero vanishes; if $h\in L^1$ has all moments zero, then $h=0$ a.e.
  - **证明.** Full (Weierstrass plus the uniqueness part of the Riesz representation; `Hausdorff1921a`, `Hausdorff1921b`, `Hausdorff1923`).
  - `% uses: none`

* **定理 `thm:appK-even-moments` — 偶数矩决定函数** (数学，无标签) · v1
  - **陈述.** If $x^{2k_0}g\in L^1(0,1)$ and $\int_0^1x^{2k}g=0$ for all $k\ge k_0$, then $g=0$ a.e.
  - **证明.** Full (substitute $t=x^2$, then `lem:appK-hausdorff`; Müntz–Szász is not needed).
  - `\uses{lem:appK-hausdorff}`

* **推论 `cor:appK-pdf` — PDF 的唯一性** (数学，无标签) · v1
  - **陈述.** Even moments $N\ge N_1$ determine $q+\bar q$ and $g$; odd moments determine $q-\bar q$; even moments alone do not determine $q$ and $\bar q$ separately (explicit pair, c_pdf s6(h)).
  - **证明.** Full.
  - `\uses{thm:appK-even-moments}`

* **命题 `prop:appK-kernels` — 领头阶核由偶数矩唯一确定** (数学，无标签) · v1
  - **陈述.** For $P=r(x)+a[\frac1{1-x}]_++b\delta(1-x)$ with $|r|\le C/x$: if all even moments vanish, then $a=b=0$ and $r=0$ a.e.
  - **证明.** Full.
  - `\uses{thm:appK-even-moments}`

* **定理 `thm:appK-carlson` — Carlson 定理** (数学，无标签) · v1 (classical, cited)
  - **陈述.** As in c_pdf Thm 7.6, with sharpness from $\sin\pi z$; for even integers the type bound is $<\pi/2$ (`Carlson1914`, `Titchmarsh1939` §5.81, `Boas1954` Thm 9.2.1; locations [PENDING-VERIFY: N23]).
  - **证明.** Cited.
  - `% uses: none`

* **命题 `prop:appK-continuation` — 多项式有界条件下延拓的唯一性** (数学，无标签) · v1
  - **陈述.** If $F$ is holomorphic for ${\rm Re}\,z>\sigma_0$ with $|F|\le C(1+|z|)^m$ and vanishes on an arithmetic progression, then $F\equiv0$. Corollary: Mellin transforms of PDFs and kernels continue uniquely from even $N$; adding $c\sin(\pi N/2)$ is excluded by the growth bound; the even and odd continuations differ beyond LO (`rem:pdf-ns-plusminus`, VF-REF-5).
  - **证明.** Full (Cayley map and Jensen's formula; `Rudin1987`).
  - `% uses: none`

* **定理 `thm:appK-muntz` — Müntz–Szász 定理** (数学，无标签) · v1 (classical, cited)
  - **陈述.** With the $L^2$ distance formula $\frac1{\sqrt{2\lambda+1}}\prod_k\frac{|\lambda-\lambda_k|}{\lambda+\lambda_k+1}$, for reference (`Muntz1914`, `Szasz1916`).
  - **证明.** Cited.
  - `% uses: none`

* **引理 `lem:appK-entire` — 受控增长的整函数** (数学，无标签) · new (refdoc S50) [PENDING-VERIFY: X3]
  - **陈述.** If $f$ is entire and $|f(z)|\le C(1+|z|)^A|{\rm Im}\,z|^{-B}$ off the real axis, then $|f(z)|\le C(3+|z|)^A$ for all $z$; hence $f$ is a polynomial of degree $\le A$.
  - **证明.** Full: subharmonicity of $\log|f|$ on circles of radius $2$ about $z$, and Jensen's formula for $J(y)=\frac1{2\pi}\int_0^{2\pi}\log|y+2\sin\theta|\,d\theta=\sum_k\log\max(1,|w_k|)\ge0$, $w_k$ the roots of $w^2+iyw-1$; then Liouville (`Boas1954`). Used in `prop:dis-dispersion-np` (App M §M.8).
  - `% uses: none`

* **引理 `lem:appK-markov` — V. A. Markov 系数不等式** (数学，无标签) · new (refdoc S50) [PENDING-VERIFY: X3]
  - **陈述.** Let $p(x)=\sum_{k\le N}a_kx^k$ be a real polynomial with $\max_{|x|\le h}|p(x)|\le\varepsilon$. Then $|a_k|\le c_{N,k}\,\varepsilon\,h^{-k}$, where $c_{N,k}=|t_{N,k}|$ if $N-k$ is even and $c_{N,k}=|t_{N-1,k}|$ if $N-k$ is odd, $T_m(x)=\sum_kt_{m,k}x^k$ the Chebyshev polynomials; the bound is attained by $T_N$ (resp. $T_{N-1}$). For a polynomial $h(\omega)$ with complex coefficients bounded on the imaginary segment $\{iy:|y|\le h\}$, apply this to the real and imaginary parts of $h(iy)$ (an extra factor $\sqrt2$). Used in `lem:dis-ope-segment` and `thm:dis-fixed-n` (App M §M.8).
  - **证明.** Cited (`Markoff1916`, the German translation of V. A. Markov's memoir; the writer checks the parity form against it); only the existence of some $c_{N,k}$ (norm equivalence on the finite-dimensional space of polynomials) is needed for the theorems, and that part gets a full one-line proof.
  - `% uses: none`

* **注 `rem:appK-counterexamples` — 反例与稳定性** (no tag) · v1 (+ refdoc S50)
  - $\delta'(x)$: all even moments vanish, but it is not a function. $\sin(Q^2x)$: $Q^2$ times every moment stays bounded, yet $\sup|R|=1$ (VF-MISC-3). Uniqueness is not stability: the Hilbert-matrix condition number grows like $e^{3.5K}$ (c_pdf s6(c); VF-MISC-2). **Hausdorff-problem caveat of `cor:dis-weak-xspace`** (refdoc S50): the existence of measures $\Phi_Q$ with prescribed twist-2 moments is a Hausdorff moment problem — a sequence is the moment sequence of a positive measure iff it is completely monotone (of a signed measure of bounded variation iff the Hausdorff condition holds) — so for truncated perturbative coefficients the hypothesis (Φ) of `cor:dis-weak-xspace` is a genuine assumption, not automatic.

**Sources.** c_pdf §7 (VF-MISC-2, -3); refdoc S50 (Lemma on entire functions, Markov inequality); `Markoff1916`.

---------------------------------------------------------------------------------------------------

## Appendix L — 光线算符与定域算符：矩关系的全阶证明 / Light-ray and local operators: all-order proof of the moment relation

`\label{app:appL}` · `appL_lightray.tex` · **2 pp**

**Promised content.** The complete proof of `thm:pdf-moments-local`.

**Sections.** `sec:appL-vertices` (`lem:appL-divided-differences`); `sec:appL-bare` (`prop:appL-bare`); `sec:appL-renormalized` (`prop:appL-renormalized`).

**Canonical statements** (in reading order).

* **引理 `lem:appL-divided-differences` — 均差恒等式** (数学，无标签) · v1
  - **陈述.** The $n$-th moment of the $m$-gluon vertex of the light-ray operator equals the $m$-gluon vertex of $\bar\psi\gamma^+(iD^+)^{n-1}\psi$; one gluon: $\frac{gt^an^\mu\gamma^+}{2(P^+)^n}\sum_{j=0}^{n-2}(k_2^+)^j(k_1^+)^{n-2-j}$ (VF-PDF-12).
  - **证明.** Full (c_pdf verified $m=1,2$ for $n\le7$; general $m$ by induction on divided differences).
  - `\uses{def:pdf-lightray, prop:appB-rules}`

* **命题 `prop:appL-bare` — 裸算符恒等式** [R, R_def] · v1
  - **陈述.** Moments of the bare light-ray operator are derivatives at $w^-=0$, using $\partial_{w^-}[\bar\psi W]=[\bar\psi\overleftarrow D^+]W$; total derivatives vanish in forward matrix elements; the gluon case uses the even distribution $\xi f_g$ (blueprint S6, signs fixed).
  - **证明.** Full.
  - `\uses{lem:appL-divided-differences, def:pdf-lightray, def:pdf-quark, def:pdf-gluon, def:dis-twist}`

* **命题 `prop:appL-renormalized` — 重整化后的矩关系** [R, R_PT] · v1
  - **陈述.** $Z_f(N)=Z_O(N)$, by the uniqueness of minimal subtraction and `thm:prelim-composite-renorm`; $Z_{ij}(x)$ is constructed from partonic targets; finiteness holds for any state, because the pole parts are compactly supported distributions with all moments zero (their Fourier–Laplace transform is entire); one-loop check exact in $\varepsilon$ (VF-PDF-13). Remark: left- and right-acting derivatives agree only in forward matrix elements, which is why GPDs differ (Ch19, pointer).
  - **证明.** Full.
  - `\uses{prop:appL-bare, thm:prelim-composite-renorm, def:prelim-msbar, lem:appK-hausdorff}`

**Sources.** c_pdf §§2, 5–6; blueprint S6.

---------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------

## 08 Registry (core units)

Generated from the entries of this file by the drafter's checker (`check_core.py`, scratchpad) in the format read by `spec_v2/checks/check_unit_v2.py`: one `### <UNITID>` heading per unit, table rows whose first cell is a backticked label; the owner of a label is the unit under whose heading it is listed. Statement rows give type, tag (as in the entry) and title; `sec:`/`tab:` rows are the canonical section and table labels of the unit; `fig:` rows are the **required** figures owned by the unit (FIGURES_INDEX_v2 §5; optional figures are listed below each table, not as rows, so that `check_unit_v2.py` C1b does not demand them). Ch22–Ch24, App M–Q and the register entries `asm:appM/N/O-*` are registered by `OUTLINE_frontier.md`, `OUTLINE_appMNOPQ.md` and `ASSUMPTIONS.md` [SYNC-APP] [SYNC-ASM] [SYNC-FRONTIER].

### front

| label | type | tag | title |
|---|---|---|---|
| `tab:front-notation` | tab | — | table |

Continuation labels `tab:front-notation-b`, `tab:front-notation-c`, … exist only if the table is split into several floats (not registry rows; WRITER_SPEC_v2 §1.1 note 2).

### Ch01

| label | type | tag | title |
|---|---|---|---|
| `def:intro-hard-process` | def | (no tag) | 硬过程与幂次展开 |
| `def:intro-factorization` | def | (no tag) | 共线因子化陈述 |
| `rem:intro-incoherence` | rem | (no tag) | 部分子模型的非相干性论证（启发式） |
| `ex:intro-handbag` | ex | (no tag) | 树图手提包与 Callan–Gross 关系 |
| `rem:intro-sharpness` | rem | (no tag) | "每一阶、领头幂次"的精确含义与幂次的锐利性 |
| `def:intro-tags` | def | (no tag) | 严格性标签、限定语与等级传递 |
| `def:intro-error-types` | def | (no tag) | 误差类型 |
| `rem:intro-grade-dictionary` | rem | (no tag) | 与文献中另一种分级的对照 |
| `asm:intro-wightman` | asm | [C] | QCD 的 Wightman 结构 |
| `asm:intro-composite` | asm | [C] | 规范不变复合算符与光线算符的存在与重整化群 |
| `asm:intro-np-ope` | asm | [C] | 非微扰算符乘积展开 |
| `asm:intro-af-coeff` | asm | [C] | 系数的渐近自由行为 |
| `asm:intro-growth` | asm | [C] | 前向振幅的增长条件 |
| `asm:intro-bridge` | asm | [C] | 从部分子微扰论到强子的桥接假设 |
| `def:intro-MA` | def | (no tag) | 元假设 MA0–MA4（总称）与编号假设的对应 |
| `sec:intro-parton` | sec | — | section |
| `sec:intro-statement` | sec | — | section |
| `sec:intro-proof` | sec | — | section |
| `sec:intro-tags` | sec | — | section |
| `sec:intro-kinds` | sec | — | section |
| `sec:intro-overview` | sec | — | section |
| `sec:intro-misconceptions` | sec | — | section |
| `sec:intro-organisation` | sec | — | section |
| `tab:intro-assumptions` | tab | — | table |
| `tab:intro-kinds` | tab | — | table |
| `tab:intro-overview` | tab | — | table |
| `fig:parton-model` | fig | — | figure (required) |
| `fig:handbag` | fig | — | figure (required) |
| `fig:factorization-schematic` | fig | — | figure (required) |
| `fig:intro-dependency` | fig | — | figure (required) |

### Ch02

| label | type | tag | title |
|---|---|---|---|
| `def:qcd-gauge-group` | def | (no tag) | 规范群 SU($N$) 及其表示 |
| `lem:qcd-colour-identities` | lem | (数学，无标签) | 色代数恒等式 |
| `ex:qcd-colour-algebra` | ex | (no tag) | 单圈图的色因子与双线记号 |
| `prop:qcd-covariance` | prop | [R, R_def] | 协变导数与场强的规范协变性 |
| `def:prelim-qcd` | def | (no tag) | QCD 拉氏量与规范变换 |
| `thm:qcd-gauge-invariance` | thm | [R, R_def] | 经典 QCD 拉氏量的规范不变性与唯一性 |
| `rem:qcd-theta` | rem | (no tag) | $\theta$ 项 |
| `rem:qcd-fp-derivation` | rem | (no tag) | Faddeev–Popov 构造（形式推导） |
| `def:qcd-fp` | def | (no tag) | 协变规范、Faddeev–Popov 鬼场与微扰 QCD |
| `ex:qcd-fp-lowest-order` | ex | (no tag) | 由拉氏量导出传播子、鬼场顶点与闭合鬼圈因子 |
| `def:prelim-feynman-rules` | def | (no tag) | Feynman 规则 |
| `ex:qcd-qqbar-gg` | ex | (no tag) | 树图 $q\bar q\to gg$：为什么需要鬼场 |
| `def:qcd-dimreg` | def | (no tag) | 维数正规化 |
| `prop:qcd-superficial-degree` | prop | [R, R_def] | 紫外超表观发散度 |
| `def:prelim-brst` | def | (no tag) | BRST 变换 |
| `lem:prelim-brst-nilpotent` | lem | [R, R_def] | $s^2=0$ 与拉氏量的 BRST 不变性 |
| `prop:qcd-brst-cohomology` | prop | [R, R_def] | 自由渐近 Fock 空间上的 BRST 上同调（Kugo–Ojima 四重态） |
| `ex:qcd-brst-quartet` | ex | (no tag) | 单一动量模式的四重态 |
| `lem:qcd-st-regularized` | lem | [R, R_PT] | 维数正规化理论的 Slavnov–Taylor 恒等式 |
| `def:qcd-renormalization` | def | (no tag) | 重整化常数与抵消项 |
| `def:prelim-msbar` | def | (no tag) | $\overline{\rm MS}$ 方案 |
| `thm:qcd-renormalizability` | thm | [R, R_PT] | QCD 的可重整性 |
| `prop:qcd-st-relations` | prop | [R, R_PT] | 重整化常数间的 Slavnov–Taylor 关系 |
| `thm:prelim-slavnov-taylor` | thm | [R, R_PT] | Slavnov–Taylor 恒等式（因子化所用形式） |
| `prop:qcd-xi-independence` | prop | [R, R_PT] | 物理量的规范参数无关性 |
| `thm:prelim-composite-renorm` | thm | [R, R_PT] | 规范不变复合算符的重整化（Joglekar–Lee） |
| `rem:prelim-bphz-brst` | rem | (no tag) | BPHZ 减除与 Slavnov–Taylor 恒等式；减除度的顶点可加性 |
| `ex:qcd-gluon-self-energy` | ex | (no tag) | 单圈胶子自能与 $Z_3$ |
| `ex:qcd-quark-self-energy-vertex` | ex | (no tag) | 夸克自能与夸克—胶子顶点 |
| `ex:qcd-beta0-four-ways` | ex | (no tag) | 用四种 Slavnov–Taylor 等价途径计算 $\beta_0$ |
| `prop:prelim-beta` | prop | [R, R_PT] | $\beta$ 函数 |
| `prop:qcd-rge` | prop | [R, R_PT] | 重整化群方程 |
| `prop:prelim-rg` | prop | [R, R_PT] | 重整化群改进 |
| `def:qcd-lambda` | def | (no tag) | $\Lambda_{\overline{\rm MS}}$ 与跑动耦合 |
| `rem:qcd-decoupling` | rem | (no tag) | 重夸克退耦与有效味数 |
| `ex:qcd-running-numbers` | ex | (no tag) | 从 $\alpha_s(M_Z)$ 出发的数值跑动 |
| `thm:qcd-asymptotic-freedom` | thm | [R, R_PT] | 渐近自由 |
| `rem:qcd-antiscreening` | rem | (no tag) | 屏蔽与反屏蔽的直观图像 |
| `rem:qcd-af-meaning` | rem | (no tag) | 渐近自由意味着什么、不意味着什么 |
| `prop:qcd-soft-collinear-limits` | prop | [R, R_PT] | 树图层次的软极限与共线极限 |
| `def:qcd-ir-safety-informal` | def | (no tag) | 红外安全（非形式） |
| `ex:qcd-ee-real-virtual` | ex | (no tag) | $e^+e^-\to q\bar q(g)$：实辐射与虚修正的相消 |
| `ex:qcd-sterman-weinberg` | ex | (no tag) | 第一个红外安全的排他量：Sterman–Weinberg 两喷注截面 |
| `rem:qcd-ir-theorems-preview` | rem | (no tag) | 红外定理预览 |
| `sec:qcd-why` | sec | — | section |
| `sec:qcd-gauge` | sec | — | section |
| `sec:prelim-qcd` | sec | — | section |
| `sec:qcd-quantization` | sec | — | section |
| `sec:qcd-regularization` | sec | — | section |
| `sec:prelim-brst` | sec | — | section |
| `sec:prelim-renorm` | sec | — | section |
| `sec:qcd-renorm` | sec | — | section |
| `sec:qcd-running` | sec | — | section |
| `sec:qcd-af` | sec | — | section |
| `sec:qcd-ir` | sec | — | section |
| `sec:qcd-summary` | sec | — | section |
| `tab:qcd-symbols` | tab | — | table |
| `fig:prelim-feynman-rules` | fig | — | figure (required) |
| `fig:qcd-vacuum-polarization` | fig | — | figure (required) |
| `fig:qcd-running-coupling` | fig | — | figure (required) |
| `fig:qcd-antiscreening` | fig | — | figure (required) |
| `fig:qcd-ir-safety` | fig | — | figure (required) |

Optional figures owned by this unit (not registry rows): `fig:qcd-gauge-orbit`, `fig:qcd-colour-flow`.

### Ch03

| label | type | tag | title |
|---|---|---|---|
| `def:prelim-lightfront` | def | (no tag) | 光锥坐标与 Sudakov 分解 |
| `lem:prelim-boost` | lem | [R, R_def] | 推动下的标度 |
| `ex:prelim-boost-scaling` | ex | (no tag) | 共线动量与好/坏分量的标度 |
| `def:prelim-wilson` | def | (no tag) | Wilson 线 |
| `prop:prelim-wilson-covariance` | prop | [R, R_def] | Wilson 线的规范协变性 |
| `prop:prelim-wilson-rules` | prop | [R, R_def] | 半无限直 Wilson 线的动量空间 Feynman 规则 |
| `lem:prelim-eikonal-identity` | lem | (数学，无标签) | 程函恒等式 |
| `ex:prelim-eikonal-two` | ex | (no tag) | $m=2$ 的程函恒等式与入射夸克传播子的程函极限 |
| `ex:prelim-wilson-segment` | ex | (no tag) | 有限类光线段的单胶子项 |
| `def:prelim-dr-conventions` | def | (no tag) | 维数正规化的技术约定 |
| `lem:prelim-scaleless` | lem | (数学，无标签) | 无标度积分为零 |
| `ex:prelim-scaleless` | ex | (no tag) | 无标度积分的紫外/红外记账 |
| `def:prelim-gamma5` | def | (no tag) | $\gamma_5$ 与 $\varepsilon$ 张量 |
| `def:prelim-plus` | def | (no tag) | 加号分布 |
| `lem:prelim-plus-expansion` | lem | (数学，无标签) | $(1-z)^{-1-a\varepsilon}$ 的分布展开 |
| `ex:prelim-plus` | ex | (no tag) | 单圈实辐射的典型积分 |
| `def:prelim-mellin` | def | (no tag) | Mellin 变换与卷积 |
| `lem:prelim-mellin` | lem | (数学，无标签) | Mellin 卷积定理与加号分布的矩 |
| `rem:prelim-moment-tools` | rem | (no tag) | 矩问题工具箱 |
| `def:prelim-cut` | def | (no tag) | 割图 |
| `thm:prelim-cutting-rules` | thm | [R, R_PT] | 切割规则 |
| `prop:prelim-unitarity` | prop | [R, R_PT] | 物理幺正性与鬼场割线 |
| `rem:prelim-cutting-dr` | rem | [A] | 无质量维数正规化中的割图规则 |
| `prop:prelim-optical` | prop | [R, R_def] | 流关联函数的光学定理 |
| `ex:prelim-vacpol` | ex | (no tag) | 维数正规化中的单圈无质量流关联函数 |
| `sec:prelim-lightfront` | sec | — | section |
| `sec:prelim-wilson` | sec | — | section |
| `sec:prelim-dimreg` | sec | — | section |
| `sec:prelim-distributions` | sec | — | section |
| `sec:prelim-moments` | sec | — | section |
| `sec:prelim-cuts` | sec | — | section |
| `tab:prelim-symbols` | tab | — | table |
| `fig:soft-eikonal` | fig | — | figure (required) |
| `fig:prelim-wilson-rules` | fig | — | figure (required) |
| `fig:prelim-lightcone` | fig | — | figure (required) |

### Ch04

| label | type | tag | title |
|---|---|---|---|
| `def:ir-landau-setup` | def | (no tag) | Feynman 参数表示与 Symanzik 多项式 |
| `lem:ir-envelope` | lem | (数学，无标签) | 包络恒等式 |
| `thm:ir-landau-alpha` | thm | [R, R_PT] | Landau 条件（参数形式）：解析性与红外有限性判据 |
| `thm:ir-landau-momentum` | thm | [R, R_PT] | 动量空间的钳夹必要条件 |
| `rem:ir-landau-status` | rem | [A] | Landau 条件的充分性与整体形变 |
| `rem:ir-euclid-corners` | rem | (no tag) | 欧氏区的 Landau 解与红外有限性 |
| `ex:ir-euclid-triangle` | ex | (no tag) | 离壳三角图的 Symanzik 多项式 |
| `def:ir-pinch-surface` | def | (no tag) | 钳夹面、内禀坐标与法坐标 |
| `prop:ir-coleman-norton` | prop | [R, R_PT] | Coleman–Norton 定理（代数形式） |
| `prop:ir-pinch-classification` | prop | [A] | 钳夹面与约化图 |
| `def:ir-scalings` | def | (no tag) | 区域标度 |
| `prop:ir-power-counting` | prop | [R, R_PT] | 超表观红外发散度 |
| `prop:ir-super-leading` | prop | [A] | 超领头构型及其相消 |
| `rem:ir-scaling-vs-bound` | rem | (no tag) | 标度陈述与积分界 |
| `thm:ir-leading-regions` | thm | [A] | 领头区域 |
| `ex:ir-vertex` | ex | (no tag) | 单圈无质量顶点 |
| `ex:ir-k-dominance` | ex | (no tag) | Feynman 规范下共线区域的标量极化主导 |
| `ex:ir-real-emission` | ex | (no tag) | $e^+e^-\to q\bar qg$ 的共线区 |
| `def:ir-glauber` | def | (no tag) | Glauber 区 |
| `prop:ir-glauber-trapping` | prop | [R, R_PT] | 单圈 Glauber 区的钳夹判据 |
| `thm:ir-bn-qed` | thm | [R, R_PT] | QED 中的 Bloch–Nordsieck 定理 |
| `thm:ir-kln` | thm | [A] | KLN 定理 |
| `prop:ir-bn-failure` | prop | [V] | 有色初态时非阿贝尔 Bloch–Nordsieck 抵消的失效 |
| `def:ir-safe` | def | (no tag) | 红外安全可观测量 |
| `thm:ir-safe-finite` | thm | [A] | 红外安全可观测量的有限性 |
| `def:ir-regions` | def | (no tag) | 区域方法 |
| `thm:ir-regions-euclid` | thm | [R, R_PT] | 欧氏极限的渐近展开 |
| `prop:ir-regions-minkowski` | prop | [P] | Minkowski 极限下区域方法的地位 |
| `rem:ir-regions-values` | rem | (no tag) | 发散区域积分的值依赖于表示 |
| `ex:ir-regions-toy` | ex | (no tag) | 一维玩具积分与零区减除 |
| `sec:ir-landau` | sec | — | section |
| `sec:ir-coleman-norton` | sec | — | section |
| `sec:ir-pinch` | sec | — | section |
| `sec:ir-power` | sec | — | section |
| `sec:ir-glauber` | sec | — | section |
| `sec:ir-cancellation` | sec | — | section |
| `sec:ir-regions` | sec | — | section |
| `tab:ir-connection-powers` | tab | — | table |
| `fig:landau-pinch` | fig | — | figure (required) |
| `fig:vertex-regions` | fig | — | figure (required) |
| `fig:coleman-norton` | fig | — | figure (required) |
| `fig:reduced-ee` | fig | — | figure (required) |
| `fig:reduced-dis` | fig | — | figure (required) |
| `fig:reduced-dy` | fig | — | figure (required) |
| `fig:momentum-regions` | fig | — | figure (required) |
| `fig:ir-mode-exponents` | fig | — | figure (required) |

Optional figures owned by this unit (not registry rows): `fig:ir-landau-simplex`.

### Ch05

| label | type | tag | title |
|---|---|---|---|
| `def:sudakov-ff` | def | (no tag) | 夸克形状因子 |
| `prop:sudakov-oneloop` | prop | [R, R_PT] | 一圈形状因子（精确到 $\varepsilon$ 的所有阶） |
| `ex:sudakov-onshell-hard` | ex | (no tag) | 在壳无质量形状因子 = 硬区 |
| `ex:sudakov-offshell` | ex | (no tag) | 离壳 Sudakov 三角形的区域展开 |
| `ex:sudakov-massive` | ex | (no tag) | 有质量交换：需要解析正规化 |
| `ex:sudakov-ll` | ex | (no tag) | 双对数系数 |
| `rem:sudakov-consistency` | rem | (no tag) | 一致性论证：单标度结构、$\mu$ 无关性与极点相消 |
| `thm:sudakov-factorization` | thm | [A] | Sudakov 形状因子的全阶因子化 |
| `def:sudakov-cusp` | def | (no tag) | cusp 反常维度 |
| `prop:sudakov-kg` | prop | [A] | $K+G$ 演化方程 |
| `cor:sudakov-exponentiation` | cor | [A] | 指数化与解析延拓 |
| `prop:sudakov-webs` | prop | [A] | 非阿贝尔指数化（webs） |
| `thm:sudakov-ir-poles` | thm | [A] | 无质量多腿振幅红外极点的因子化 |
| `prop:sudakov-dipole-violation` | prop | [V] | 偶极子公式作为全阶精确公式的失效 |
| `prop:sudakov-coulomb` | prop | [R, R_PT] | Coulomb 相位 |
| `prop:sudakov-amplitude-factorization` | prop | [A] | 振幅的硬—软—共线因子化（出射或阈值运动学） |
| `rem:sudakov-spacelike` | rem | [V] | 类空共线极限预览 |
| `sec:sudakov-oneloop` | sec | — | section |
| `sec:sudakov-regions` | sec | — | section |
| `sec:sudakov-factorization` | sec | — | section |
| `sec:sudakov-evolution` | sec | — | section |
| `sec:sudakov-multileg` | sec | — | section |
| `sec:sudakov-collinear` | sec | — | section |
| `fig:sudakov-ff` | fig | — | figure (required) |
| `fig:sudakov-hjjs` | fig | — | figure (required) |
| `fig:sudakov-cusp` | fig | — | figure (required) |
| `fig:sudakov-dipole` | fig | — | figure (required) |

### Ch06

| label | type | tag | title |
|---|---|---|---|
| `def:ee-R` | def | (no tag) | $R$ 比 |
| `prop:ee-R-ImPi` | prop | [R, R_def] | $R=12\pi\,{\rm Im}\,\Pi$ |
| `lem:ee-single-scale` | lem | [R, R_PT] | 无质量传播子型图的单标度结构 |
| `prop:ee-analytic` | prop | [R, R_def] | 解析性与正定性 |
| `def:ee-adler` | def | (no tag) | Adler 函数 |
| `prop:ee-adler-dispersion` | prop | [R, R_def] | Adler 函数的色散表示 |
| `thm:ee-euclid-ir` | thm | [R, R_PT] | 欧氏红外有限性 |
| `prop:ee-adler-rg` | prop | [R, R_PT] | Adler 函数的重整化群 |
| `thm:ee-R-finite` | thm | [R, R_PT] | $R(s)$ 在微扰论每一阶的红外有限性 |
| `prop:ee-oneloop` | prop | [R, R_PT] | $O(\alpha_s)$ 的实辐射与虚修正 |
| `ex:ee-quark-spectrum` | ex | (no tag) | KLN 的作用与局限 |
| `prop:ee-twoloop` | prop | [R, R_PT] | 欧氏两圈关联函数 |
| `ex:ee-twoloop-route` | ex | (no tag) | 欧氏两圈路线 |
| `prop:ee-cutting-exact` | prop | [R, R_PT] | $O(g^2)$ 处精确到 $\varepsilon$ 的切割恒等式 |
| `cor:ee-cuts` | cor | [A] | 与部分子末态求和的等同；KLN |
| `prop:ee-contour` | prop | [R, R_def] | 围道公式 |
| `cor:ee-R-alphas` | cor | [R, R_PT] | $R(s)$ 的微扰展开 |
| `ex:ee-pi2` | ex | (no tag) | $O(a^3)$ 的 $\pi^2$ 项 |
| `rem:ee-status-layout` | rem | (no tag) | 四个逻辑层次 |
| `thm:ee-ope` | thm | [A] | 流关联函数的欧氏 OPE |
| `conj:ee-np-ope` | conj | [C] | 非微扰 OPE 与凝聚 |
| `rem:ee-complex-ope` | rem | (no tag) | 复 $q^2$ 处的 OPE 是额外假设 |
| `prop:ee-smearing` | prop | [R, R_def] | Poggio–Quinn–Weinberg 抹平恒等式 |
| `conj:ee-duality` | conj | [C] | 夸克—强子对偶 |
| `sec:ee-R` | sec | — | section |
| `sec:ee-analytic` | sec | — | section |
| `sec:ee-euclid` | sec | — | section |
| `sec:ee-theorem` | sec | — | section |
| `sec:ee-oneloop` | sec | — | section |
| `sec:ee-higher` | sec | — | section |
| `sec:ee-ope` | sec | — | section |
| `sec:ee-duality` | sec | — | section |
| `fig:ee-oneloop` | fig | — | figure (required) |
| `fig:ee-pi-plane` | fig | — | figure (required) |
| `fig:ee-cutsum-disc` | fig | — | figure (required) |

### Ch07

| label | type | tag | title |
|---|---|---|---|
| `def:dis-kinematics` | def | (no tag) | DIS 运动学与强子张量 |
| `prop:dis-W-structure` | prop | [R, R_def] | 强子张量的一般结构 |
| `def:dis-compton` | def | (no tag) | 前向 Compton 振幅 |
| `prop:dis-compton-analytic` | prop | [R, R_PT] | 解析性与交叉（部分子靶） |
| `prop:dis-dispersion` | prop | [R, R_PT] | 色散关系：Taylor 系数 = 矩（部分子靶） |
| `ex:dis-free-quark` | ex | (no tag) | 自由夸克的前向振幅 |
| `def:dis-twist` | def | (no tag) | 扭度与扭度 2 算符 |
| `lem:dis-twist-classification` | lem | [R, R_def] | 扭度 2 规范不变算符的分类 |
| `lem:dis-twist-chirality` | lem | [R, R_def] | 扭度奇偶性与手征 |
| `lem:dis-tree-ope` | lem | [R, R_PT] | 树图 OPE |
| `prop:dis-ope-euclid` | prop | [A] | 欧氏非例外动量下 Green 函数的逐图渐近展开 |
| `prop:dis-ope-gi` | prop | [A] | 物理矩阵元只需规范不变算符 |
| `prop:dis-ope-forward` | prop | [A] | 前向在壳部分子矩阵元 |
| `thm:dis-ope` | thm | [A] | 重整化微扰论中的欧氏 OPE |
| `prop:dis-chiral-suppression` | prop | [R, R_PT] | 奇扭度系数的手征压低 |
| `prop:dis-wilson-partons` | prop | [R, R_OPE] | 由部分子结构函数提取 Wilson 系数 |
| `prop:dis-ope-rg` | prop | [R, R_OPE] | Wilson 系数与约化矩阵元的重整化群 |
| `lem:dis-euclid-segment` | lem | [R, R_def] | 欧氏点在 $\omega$ 平面上的位置 |
| `prop:dis-dispersion-np` | prop | [R, R_cond] | 由 Wightman 公理得到的有限减除色散关系 |
| `prop:dis-low-moments` | prop | [R, R_def] | 低阶矩与增长条件的等价 |
| `lem:dis-ope-segment` | lem | [R, R_cond] | OPE 在线段上的多项式逼近 |
| `thm:dis-fixed-n` | thm | [R, R_cond] | 由定域 OPE 得到固定 $n$ 的 Taylor 系数 |
| `thm:dis-moments-np` | thm | [R, R_cond] | DIS 矩因子化的非微扰条件定理 |
| `cor:dis-weak-xspace` | cor | [R, R_cond] | $x$ 空间的弱收敛 |
| `thm:dis-moments` | thm | [R, R_OPE] | DIS 结构函数矩的因子化 |
| `cor:dis-scaling` | cor | [R, R_OPE] | 标度破坏 |
| `ex:dis-n2` | ex | (no tag) | $n=2$：能动张量 |
| `prop:dis-c-oneloop` | prop | [R, R_PT] | 单圈 Wilson 系数 |
| `ex:dis-oneloop-ope` | ex | (no tag) | 单圈 OPE 检验 |
| `rem:dis-uniqueness` | rem | (no tag) | 偶数矩决定 C 偶组合（数学） |
| `rem:dis-nonuniform` | rem | (no tag) | 矩的 $O(1/Q^2)$ 不蕴含逐点 $O(1/Q^2)$ |
| `prop:dis-light-cone` | prop | [A] | 光锥展开 |
| `prop:dis-twist4` | prop | [R, R_OPE] | 扭度 4 修正的算符结构 |
| `prop:dis-tmc` | prop | [R, R_OPE] | 靶质量修正 |
| `ex:dis-tmc-n2` | ex | (no tag) | 第二阶矩的靶质量修正 |
| `thm:dis-bjorken` | thm | [R, R_OPE] | Bjorken 求和规则 |
| `rem:dis-crewther` | rem | (no tag) | Crewther 关系 |
| `sec:dis-kinematics` | sec | — | section |
| `sec:dis-compton` | sec | — | section |
| `sec:dis-ope` | sec | — | section |
| `sec:dis-np` | sec | — | section |
| `sec:dis-moments` | sec | — | section |
| `sec:dis-rg` | sec | — | section |
| `sec:dis-wilson` | sec | — | section |
| `sec:dis-xspace` | sec | — | section |
| `sec:dis-higher-twist` | sec | — | section |
| `sec:dis-polarized` | sec | — | section |
| `tab:dis-correspondence` | tab | — | table |
| `fig:dis-kinematics` | fig | — | figure (required) |
| `fig:forward-compton` | fig | — | figure (required) |
| `fig:omega-plane` | fig | — | figure (required) |
| `fig:ope-schematic` | fig | — | figure (required) |
| `fig:dis-oneloop` | fig | — | figure (required) |
| `fig:higher-twist` | fig | — | figure (required) |
| `fig:dis-euclid-segment` | fig | — | figure (required) |

Optional figures owned by this unit (not registry rows): `fig:dis-twist-graphical`.

### Ch08

| label | type | tag | title |
|---|---|---|---|
| `def:pdf-quark` | def | (no tag) | 夸克分布 |
| `def:pdf-antiquark` | def | (no tag) | 反夸克分布 |
| `def:pdf-gluon` | def | (no tag) | 胶子分布 |
| `prop:pdf-invariance` | prop | [R, R_def] | 规范不变性、推动不变性与自由场值 |
| `ex:pdf-free-field` | ex | (no tag) | 自由场值 |
| `thm:pdf-support-pt` | thm | [R, R_PT] | 支撑（微扰论） |
| `prop:pdf-support-hadron` | prop | [A] | 支撑（强子态） |
| `rem:pdf-support-jaffe` | rem | (no tag) | 支撑的第二种论证：$k^-$ 极点 |
| `rem:pdf-number-density` | rem | (no tag) | 数密度诠释（启发式） |
| `rem:pdf-gauge-residual` | rem | (no tag) | 光锥规范的剩余规范自由与 $1/k^+$ 处方 |
| `def:pdf-lightray` | def | (no tag) | 光线算符 |
| `lem:pdf-wilson-moments` | lem | [R, R_def] | Wilson 线顶点的矩 = 定域算符顶点 |
| `thm:pdf-moments-local` | thm | [R, R_PT] | PDF 的矩 = 扭度 2 定域算符矩阵元 |
| `thm:pdf-dglap` | thm | [R, R_PT] | 由算符重整化得到 DGLAP 方程 |
| `prop:pdf-lo-kernels` | prop | [R, R_PT] | 领头阶分裂函数 |
| `prop:pdf-pqq-operator` | prop | [R, R_PT] | Feynman 规范下由算符定义计算 $P_{qq}$ |
| `ex:pdf-oneloop` | ex | (no tag) | 单圈夸克 PDF（逐图） |
| `prop:pdf-partonic-dr` | prop | [R, R_PT] | 纯维数正规化中的部分子分布 |
| `prop:pdf-local-anomalous` | prop | [R, R_PT] | 定域算符的单圈反常维度（含混合） |
| `ex:pdf-moments-exact` | ex | (no tag) | 精确到 $\varepsilon$ 的单圈矩 |
| `ex:pdf-quark-in-gluon` | ex | (no tag) | 胶子中的夸克 |
| `thm:pdf-dis-xspace` | thm | [R, R_OPE] | DIS 的 $x$ 空间因子化（扭度 2 部分） |
| `prop:pdf-sum-rules` | prop | [R, R_PT] | 求和规则 |
| `rem:pdf-ns-plusminus` | rem | (no tag) | 解析延拓与 $P^\pm_{\rm NS}$ |
| `rem:pdf-schemes` | rem | (no tag) | 方案变换 |
| `conj:pdf-positivity` | conj | [C] | $\overline{\rm MS}$ PDF 的正定性 |
| `def:pdf-ff` | def | (no tag) | 碎裂函数 |
| `rem:pdf-ff-multren` | rem | (no tag) | 碎裂函数的乘法可重整性是独立输入 |
| `prop:pdf-timelike-dglap` | prop | [A] | 类时 DGLAP 演化 |
| `def:pdf-polarized` | def | (no tag) | 螺旋度与横度分布 |
| `sec:pdf-definitions` | sec | — | section |
| `sec:pdf-properties` | sec | — | section |
| `sec:pdf-interpretation` | sec | — | section |
| `sec:pdf-moments` | sec | — | section |
| `sec:pdf-dglap` | sec | — | section |
| `sec:pdf-oneloop` | sec | — | section |
| `sec:pdf-dis` | sec | — | section |
| `sec:pdf-sumrules` | sec | — | section |
| `sec:pdf-ff` | sec | — | section |
| `fig:pdf-operator` | fig | — | figure (required) |
| `fig:pdf-oneloop` | fig | — | figure (required) |
| `fig:dglap-ladder` | fig | — | figure (required) |
| `fig:splitting-vertices` | fig | — | figure (required) |

Optional figures owned by this unit (not registry rows): `fig:pdf-gluon-operator`, `fig:pdf-ff-cut`.

### Ch09

| label | type | tag | title |
|---|---|---|---|
| `def:method-regions` | def | (no tag) | 区域：逐线模式指派与偏序 |
| `lem:method-meets` | lem | (数学，无标签) | 逐线交与钳夹集的交 |
| `def:method-power-suppressed` | def | (no tag) | 积分范数意义下的幂次压低 |
| `def:method-neighbourhoods` | def | (no tag) | 依赖于 $\lambda$ 的邻域 |
| `lem:method-covering` | lem | (数学，无标签) | 邻域覆盖 |
| `def:method-collinear-approx` | def | (no tag) | 共线近似子（幂等投影形式） |
| `def:method-soft-approx` | def | (no tag) | 软近似子（幂等投影形式） |
| `lem:method-i0-compat` | lem | [R, R_PT] | 软近似分母的 $i0$ 相容性与变形幅度 |
| `lem:method-telescoping` | lem | (数学，无标签) | 乘积的伸缩恒等式 |
| `lem:method-collinear-accuracy` | lem | [A] | 共线近似的精度 |
| `lem:method-soft-accuracy` | lem | [A] | 软近似的精度 |
| `lem:method-local-accuracy` | lem | [R, R_cond] | 局部精度（积分范数） |
| `rem:method-abs-failure` | rem | (no tag) | 吸收性质 (Abs) 何时失效 |
| `lem:method-gy` | lem | (数学，无标签) | Grammer–Yennie 分解 |
| `prop:method-gy-suppression` | prop | [A] | G 部分的幂次压低 |
| `lem:method-ward-elementary` | lem | [R, R_PT] | 基本 Ward 恒等式 |
| `lem:method-ward-abelian` | lem | [R, R_PT] | 阿贝尔 Ward 恒等式 |
| `prop:method-ward-one` | prop | [R, R_PT] | 单个纵向胶子的非阿贝尔 Ward 恒等式 |
| `prop:method-ward-tree` | prop | [R, R_PT] | 树图层次的非阿贝尔恒等式与 PDF Wilson 线的种子 |
| `ex:method-ward-tree` | ex | (no tag) | $q\bar q\to g^*g^*$ 的两个纵向胶子 |
| `lem:method-ward-multi` | lem | [A] | 多个 K 胶子的 Ward 恒等式与 Wilson 线 |
| `prop:method-collinear-wilson` | prop | [A] | 共线 Wilson 线与 PDF |
| `prop:method-soft-wilson` | prop | [A] | 软 Wilson 线 |
| `rem:method-pure-gauge` | rem | (no tag) | 纯规范论证的地位 |
| `def:method-subtraction` | def | (no tag) | 减除项 |
| `ex:method-naive-induction` | ex | [R, R_PT] | 朴素归纳为何失败：离壳单圈三角图 |
| `def:method-collins-conditions` | def | (no tag) | 减除条件 (CS1)–(CS3) |
| `prop:method-chains` | prop | (数学，无标签) | 减除的链展开 |
| `lem:method-pairing` | lem | (数学，无标签) | 配对分解 |
| `prop:method-product` | prop | (数学，无标签) | 乘积公式 |
| `lem:method-no-pole` | lem | (数学，无标签) | 有界的亚纯函数无极点 |
| `cor:method-removing-eps` | cor | [R, R_cond] | 去掉维数正规化 |
| `thm:method-subtraction` | thm | [A] | 减除定理 |
| `ex:method-sudakov-subtraction` | ex | (no tag) | 完整的单圈例子：离壳三角图的 Collins 减除 |
| `ex:method-dis-oneloop` | ex | (no tag) | 减除语言中的单圈 DIS |
| `lem:method-soft-unitarity` | lem | [R, R_def] | 软因子的幺正性 |
| `prop:method-fsi` | prop | [A] | 末态相互作用的幺正性相消 |
| `prop:method-glauber-oneloop` | prop | [R, R_PT] | 两条程函线之间的单胶子交换 |
| `ex:method-glauber-oneloop` | ex | (no tag) | 单胶子交换的极点图 |
| `prop:method-glauber-deformation` | prop | [A] | Glauber 区的围道变形判据 |
| `rem:method-two-component` | rem | (no tag) | 一个分量的形变为何不够 |
| `thm:method-template` | thm | [A] | 因子化模板定理 |
| `prop:method-scale-scheme` | prop | [R, R_PT] | 因子化标度与方案 |
| `sec:method-strategy` | sec | — | section |
| `sec:method-regions` | sec | — | section |
| `sec:method-gy` | sec | — | section |
| `sec:method-ward` | sec | — | section |
| `sec:method-subtraction` | sec | — | section |
| `sec:method-unitarity` | sec | — | section |
| `sec:method-glauber` | sec | — | section |
| `sec:method-template` | sec | — | section |
| `tab:method-errors` | tab | — | table |
| `tab:method-hypotheses` | tab | — | table |
| `tab:method-correspondence` | tab | — | table |
| `fig:ward-identity` | fig | — | figure (required) |
| `fig:glauber-contour` | fig | — | figure (required) |
| `fig:method-flowchart` | fig | — | figure (required) |
| `fig:method-kg` | fig | — | figure (required) |
| `fig:method-nesting` | fig | — | figure (required) |
| `fig:method-hasse` | fig | — | figure (required) |
| `fig:method-neighbourhoods` | fig | — | figure (required) |
| `fig:method-sudakov-plane` | fig | — | figure (required) |
| `fig:method-coeff-minus-coll` | fig | — | figure (required) |
| `fig:method-glauber-direction` | fig | — | figure (required) |

### Ch10

| label | type | tag | title |
|---|---|---|---|
| `def:disall-breit` | def | (no tag) | Breit 系与投影算符 |
| `prop:disall-two-routes` | prop | [R, R_cond] | 从非物理区前向振幅到矩与 $x$ 空间的两条途径 |
| `lem:disall-fsi` | lem | [A] | 末态喷注的非钳夹性 |
| `prop:disall-regions` | prop | [A] | DIS 的领头区域 |
| `prop:disall-factorized-subtraction` | prop | [R, R_cond] | DIS 减除项的因子化结构 |
| `prop:disall-h2` | prop | [A] | (H2) 的验证 |
| `prop:disall-h3h4` | prop | [A] | (H3)(H4) 平凡成立 |
| `thm:disall-renorm-compat` | thm | [R, R_cond] | 减除与 $\overline{\rm MS}$ 重整化的相容性（矩空间） |
| `prop:disall-h5` | prop | [A] | (H5) 的验证 |
| `ex:disall-ladder` | ex | (no tag) | 两级梯形图：三个区域与分组余项 |
| `thm:disall-factorization` | thm | [A] | DIS 共线因子化（动量空间，$x$ 空间逐点） |
| `cor:disall-consistency` | cor | [R, R_OPE] | 与 OPE 系数的一致性 |
| `prop:disall-nlo` | prop | [R, R_PT] | $O(\alpha_s)$ 的 $\overline{\rm MS}$ 系数函数 |
| `ex:disall-nlo` | ex | (no tag) | $O(\alpha_s)$ 系数函数的完整推导 |
| `ex:disall-gluon` | ex | (no tag) | 光子—胶子融合 |
| `prop:disall-scale` | prop | [R, R_PT] | 标度无关性 |
| `prop:disall-dis-scheme` | prop | [R, R_PT] | DIS 方案 |
| `thm:disall-heavy` | thm | [A] | 含重夸克质量的因子化（Collins 1998） |
| `ex:disall-heavy-lo` | ex | (no tag) | 领头阶 $\gamma^*g\to Q\bar Q$ |
| `prop:disall-nuclear` | prop | [A] | 核靶上的 DIS |
| `sec:disall-regions` | sec | — | section |
| `sec:disall-fsi` | sec | — | section |
| `sec:disall-subtraction` | sec | — | section |
| `sec:disall-theorem` | sec | — | section |
| `sec:disall-consistency` | sec | — | section |
| `sec:disall-nlo` | sec | — | section |
| `sec:disall-scale` | sec | — | section |
| `sec:disall-heavy` | sec | — | section |
| `sec:disall-nuclear` | sec | — | section |
| `tab:disall-correspondence` | tab | — | table |
| `fig:disall-seed` | fig | — | figure (required) |
| `fig:disall-heavy` | fig | — | figure (required) |
| `fig:disall-ladder-regions` | fig | — | figure (required) |

### Ch11

| label | type | tag | title |
|---|---|---|---|
| `def:coll-sia` | def | (no tag) | 单举湮灭的运动学 |
| `lem:coll-final-poles` | lem | [R, R_PT] | 全部为末态的共线子图的极点在同一半平面 |
| `lem:coll-unobserved-jet` | lem | [A] | 未观测喷注与软辐射的幺正性相消 |
| `prop:coll-sia-regions` | prop | [A] | SIA 的领头区域 |
| `thm:coll-sia` | thm | [A] | $e^+e^-\to hX$ 的因子化 |
| `rem:coll-sia-nlo` | rem | (no tag) | 系数函数与检验 |
| `ex:coll-sia-lo` | ex | (no tag) | 领头阶 $e^+e^-\to hX$ |
| `thm:coll-sidis` | thm | [A] | 共线 SIDIS 的因子化 |
| `thm:coll-direct-photo` | thm | [A] | 直接光生与光子结构函数 |
| `prop:coll-photon-sf` | prop | [R, R_OPE] | 光子结构函数的点状部分 |
| `conj:coll-resolved-photo` | conj | [C] | 分辨光生 |
| `prop:coll-diffractive-photo` | prop | [V] | 衍射光生中的因子化破坏 |
| `prop:coll-luxqed` | prop | [A] | 质子的光子分布 |
| `def:coll-g1` | def | (no tag) | 极化结构函数 |
| `thm:coll-g1-moments` | thm | [R, R_OPE] | $g_1$ 的奇数矩 |
| `prop:coll-anomaly-scheme` | prop | [R, R_PT] | 一阶矩的方案依赖 |
| `prop:coll-ellis-jaffe` | prop | [V] | Ellis–Jaffe 求和规则作为预言 |
| `conj:coll-bc` | conj | [C] | Burkhardt–Cottingham 求和规则 |
| `prop:coll-ww` | prop | [V] | Wandzura–Wilczek 关系的一般失效 |
| `def:coll-transversity` | def | (no tag) | 横度分布 |
| `prop:coll-transversity-evolution` | prop | [R, R_def] | 横度的演化 |
| `prop:coll-soffer` | prop | [R, R_PT] | Soffer 不等式（LO 演化的保持性） |
| `rem:coll-christ-lee` | rem | (no tag) | 单举 DIS 中无单靶自旋横向不对称 |
| `sec:coll-sia` | sec | — | section |
| `sec:coll-sidis` | sec | — | section |
| `sec:coll-photo` | sec | — | section |
| `sec:coll-polarized` | sec | — | section |
| `sec:coll-transversity` | sec | — | section |
| `fig:coll-sia` | fig | — | figure (required) |
| `fig:coll-sidis` | fig | — | figure (required) |
| `fig:coll-photoproduction` | fig | — | figure (required) |

Optional figures owned by this unit (not registry rows): `fig:coll-transversity`.

### Ch12

| label | type | tag | title |
|---|---|---|---|
| `def:dy-kin` | def | (no tag) | DY 运动学 |
| `prop:dy-born` | prop | [R, R_PT] | Born 截面 |
| `prop:dy-regions` | prop | [A] | DY 的领头区域 |
| `prop:dy-glauber-pinch` | prop | [R, R_PT] | 单个割图中的 Glauber 钳夹 |
| `lem:dy-poles-orientation` | lem | [R, R_PT] | 光锥序中间态的取向与 $k^-$ 极点 |
| `rem:dy-one-time-per-jet` | rem | (no tag) | 每个喷注一个光锥时间 |
| `lem:dy-fsi` | lem | [A] | 旁观者末态相互作用的幺正性相消 |
| `ex:dy-future-vs-past` | ex | [R, R_def] | 单个割图给出未来指向的 Wilson 线 |
| `prop:dy-deformation` | prop | [A] | 移除末态极点后的围道变形 |
| `lem:dy-soft` | lem | [A] | 软因子为 1 |
| `prop:dy-universality` | prop | [R, R_def] | DY 与 DIS 的共线 PDF 是同一对象 |
| `prop:dy-abelian-model` | prop | [P] | 阿贝尔模型中旁观者 Glauber 相位的相消 |
| `ex:dy-spectator-lcopt` | ex | (no tag) | 旁观者模型的光锥序表示 |
| `ex:dy-glauber-model` | ex | (no tag) | 阿贝尔 Glauber 模型的数值演示 |
| `prop:dy-eikonal-twogluon` | prop | [R, R_PT] | 两条程函线之间的双胶子交换：$O(g^4)$ 幺正性与 Regge 相位 |
| `rem:dy-common-ordering` | rem | (no tag) | 共同时序是物理结果 |
| `thm:dy-factorization` | thm | [A] | 单举 DY 的共线因子化 |
| `rem:dy-nnlo-not-glauber` | rem | (no tag) | 固定阶部分子截面不检验旁观者 Glauber 相消 |
| `rem:dy-dft-premises` | rem | (no tag) | Doria–Frenkel–Taylor 非相消的前提 |
| `prop:dy-nlo` | prop | [R, R_PT] | $O(\alpha_s)$ 的 $\overline{\rm MS}$ 系数函数 |
| `ex:dy-nlo` | ex | (no tag) | $O(\alpha_s)$ 系数函数的完整推导 |
| `prop:dy-scale` | prop | [R, R_PT] | $\mu_F$ 无关性 |
| `rem:dy-dis-scheme` | rem | (no tag) | DIS 方案中的 DY 与 PDF 的普适性 |
| `ex:dy-threshold` | ex | (no tag) | 大 $N$ 极限 |
| `thm:dy-colour-singlet` | thm | [A] | 色单态末态 |
| `thm:dy-polarized` | thm | [A] | 极化 Drell–Yan |
| `conj:dy-coloured-final` | conj | [C] | 强子对撞中有色末态的共线因子化 |
| `conj:dy-polarized-jets` | conj | [C] | 极化强子对撞中的 $A_{LL}$（喷注、$\pi^0$） |
| `thm:dy-higher-twist` | thm | [A] | $1/Q^2$ 处的广义因子化 |
| `prop:dy-twist6-failure` | prop | [V] | 更高幂次的因子化失效 |
| `sec:dy-born` | sec | — | section |
| `sec:dy-regions` | sec | — | section |
| `sec:dy-orientation` | sec | — | section |
| `sec:dy-glauber` | sec | — | section |
| `sec:dy-model` | sec | — | section |
| `sec:dy-theorem` | sec | — | section |
| `sec:dy-nlo` | sec | — | section |
| `sec:dy-other` | sec | — | section |
| `sec:dy-twist` | sec | — | section |
| `tab:dy-status` | tab | — | table |
| `tab:dy-correspondence` | tab | — | table |
| `fig:dy-oneloop` | fig | — | figure (required) |
| `fig:glauber-exchange` | fig | — | figure (required) |
| `fig:dy-abelian-model` | fig | — | figure (required) |
| `fig:dy-pole-orientation` | fig | — | figure (required) |
| `fig:dy-two-gluon-exchange` | fig | — | figure (required) |

### Ch13

| label | type | tag | title |
|---|---|---|---|
| `def:thr-limit` | def | (no tag) | 部分子阈值与强子阈值 |
| `thm:thr-refactorization` | thm | [A] | DY 阈值重新因子化与指数化 |
| `prop:thr-oneloop` | prop | [R, R_PT] | 单圈检验 |
| `rem:thr-prescriptions` | rem | (no tag) | Landau 极点与处方 |
| `prop:thr-dis` | prop | [A] | DIS 的大 $x$ 重新因子化 |
| `prop:thr-nlp` | prop | [P] | 次领头幂次的阈值对数 |
| `ex:thr-dy` | ex | (no tag) | 指数的 $O(\alpha_s)$ 展开与 `prop:dy-nlo` 的 Mellin 变换 |
| `sec:thr-limit` | sec | — | section |
| `sec:thr-refactorization` | sec | — | section |
| `sec:thr-check` | sec | — | section |
| `sec:thr-prescriptions` | sec | — | section |
| `sec:thr-nlp` | sec | — | section |
| `fig:thr-kinematics` | fig | — | figure (required) |
| `fig:thr-mellin` | fig | — | figure (required) |

### Ch14

| label | type | tag | title |
|---|---|---|---|
| `def:tmd-kin` | def | (no tag) | 小 $q_T$ 区域 |
| `prop:tmd-regions` | prop | [A] | 小 $q_T$ 的领头区域 |
| `def:tmd-unsub` | def | (no tag) | 未减除的 TMD 关联函数 |
| `def:tmd-soft` | def | (no tag) | 软因子 |
| `lem:tmd-soft-oneloop` | lem | [R, R_PT] | 单圈软因子 |
| `lem:tmd-sqrt-identity` | lem | [R, R_def] | 平方根构造是恒等式 |
| `def:tmd-collins` | def | (no tag) | Collins 的 TMD 定义 |
| `rem:tmd-schemes` | rem | (no tag) | 其他方案 |
| `rem:tmd-scheme-constants` | rem | (no tag) | 方案常数（$S_\varepsilon$ 约定） |
| `rem:tmd-order-of-limits` | rem | (no tag) | 极限次序 |
| `prop:tmd-zero-bin-soft` | prop | [R, R_cond] | 零箱减除即软因子 |
| `rem:tmd-rapidity-window` | rem | (no tag) | 快度窗口 |
| `lem:tmd-glauber` | lem | [A] | TMD DY、SIDIS、$e^+e^-$ 中的 Glauber 相消 |
| `prop:tmd-h1h5` | prop | [A] | 小 $q_T$ DY 对模板假设的验证 |
| `thm:tmd-factorization` | thm | [A] | Drell–Yan 的 TMD 因子化 |
| `prop:tmd-evolution` | prop | [A] | Collins–Soper 方程与重整化群方程 |
| `prop:tmd-evolution-oneloop` | prop | [R, R_PT] | 单圈演化系数与硬因子的 RG 相容性 |
| `prop:tmd-small-b` | prop | [A] | 小 $b$ 展开 |
| `prop:tmd-css` | prop | [A] | CSS 解与非微扰输入 |
| `thm:tmd-sivers-sign` | thm | [R, R_def] | Sivers 函数的符号反转（算符层面） |
| `cor:tmd-sivers-observable` | cor | [A] | 可观测不对称的符号反转 |
| `prop:tmd-collins-universality` | prop | [A] | T-奇碎裂函数的普适性 |
| `def:tmd-etqs` | def | (no tag) | Qiu–Sterman (ETQS) 关联函数 |
| `prop:tmd-twist3-matching` | prop | [P] | 与扭度 3 共线因子化的匹配 |
| `rem:tmd-kt-integral` | rem | (no tag) | $\int d^2k_T\,f\ne f$ |
| `ex:tmd-oneloop` | ex | (no tag) | 单圈全过程 |
| `ex:tmd-qt-asymptotics` | ex | (no tag) | 小 $q_T$ 渐近式的重现 |
| `ex:tmd-sivers-model` | ex | (no tag) | 标量双夸克模型中的 Sivers 函数 |
| `sec:tmd-kinematics` | sec | — | section |
| `sec:tmd-regions` | sec | — | section |
| `sec:tmd-definitions` | sec | — | section |
| `sec:tmd-subtraction` | sec | — | section |
| `sec:tmd-theorem` | sec | — | section |
| `sec:tmd-evolution` | sec | — | section |
| `sec:tmd-small-b` | sec | — | section |
| `sec:tmd-universality` | sec | — | section |
| `sec:tmd-twist3` | sec | — | section |
| `tab:tmd-correspondence` | tab | — | table |
| `fig:tmd-staple` | fig | — | figure (required) |
| `fig:tmd-soft-factor` | fig | — | figure (required) |
| `fig:tmd-dy` | fig | — | figure (required) |
| `fig:sidis-dy-links` | fig | — | figure (required) |

Optional figures owned by this unit (not registry rows): `fig:tmd-evolution`, `fig:tmd-rapidity-bars`.

### Ch15

| label | type | tag | title |
|---|---|---|---|
| `def:scet-modes` | def | (no tag) | 模式 |
| `prop:scet-scalings` | prop | [R, R_def] | 场的标度 |
| `prop:scet-lagrangian` | prop | [R, R_PT] | 领头阶共线夸克拉氏量 |
| `prop:scet-wilson` | prop | [R, R_PT] | 共线 Wilson 线 |
| `ex:scet-wn-tree` | ex | (no tag) | $W_n$ 的树图匹配 |
| `prop:scet-gauge` | prop | [R, R_def] | 共线与超软规范对称性 |
| `thm:scet-decoupling` | thm | [R, R_def] | 超软退耦（BPS 场重定义） |
| `ex:scet-decoupling-tree` | ex | (no tag) | BPS 场重定义的树图演示 |
| `rem:scet-y-direction` | rem | (no tag) | $Y_n$ 的方向与 $i0$ |
| `def:scet-zero-bin` | def | (no tag) | 零箱减除 |
| `prop:scet-scet2` | prop | [R, R_PT] | SCET$_{\rm II}$ 与软 Wilson 线 |
| `prop:scet-rapidity-rg` | prop | [A] | 快度发散的处理与等价性 |
| `prop:scet-glauber-operators` | prop | [A] | Glauber 算符 |
| `rem:scet-glauber-dictionary` | rem | (no tag) | Glauber SCET 与光锥序证明的对照 |
| `prop:scet-hard-matching` | prop | [R, R_PT] | 硬匹配系数 |
| `thm:scet-thrust` | thm | [A] | 推力分布的因子化 |
| `prop:scet-thrust-oneloop` | prop | [R, R_PT] | 单圈因子与 RG 一致性 |
| `ex:scet-thrust-oneloop` | ex | (no tag) | 单圈 $H$、$J$、$S_T$ 合成 QCD 奇异项 |
| `prop:scet-ll` | prop | [A] | 领头对数指数 |
| `rem:scet-assumptions` | rem | (no tag) | SCET 证明的前提 |
| `sec:scet-modes` | sec | — | section |
| `sec:scet-lagrangian` | sec | — | section |
| `sec:scet-decoupling` | sec | — | section |
| `sec:scet-scet2` | sec | — | section |
| `sec:scet-glauber` | sec | — | section |
| `sec:scet-thrust` | sec | — | section |
| `sec:scet-rg` | sec | — | section |
| `sec:scet-status` | sec | — | section |
| `fig:scet-wilson` | fig | — | figure (required) |
| `fig:dijet-factorization` | fig | — | figure (required) |

Optional figures owned by this unit (not registry rows): `fig:scet-modes`.

### Ch16

| label | type | tag | title |
|---|---|---|---|
| `def:jets-algorithms` | def | (no tag) | 红外安全的喷注定义与事件形状 |
| `prop:jets-sw` | prop | [R, R_PT] | Sterman–Weinberg 两喷注截面 |
| `ex:jets-sw` | ex | (no tag) | $O(\alpha_s)$ 的 Sterman–Weinberg 截面 |
| `cor:jets-ir-finite` | cor | [A] | 红外安全喷注截面的有限性 |
| `prop:jets-thrust-lo` | prop | [R, R_PT] | 领头阶推力分布 |
| `conj:jets-hadronization` | conj | [C] | 强子化修正的普适性 |
| `prop:jets-ngl` | prop | [R, R_PT] | 非全局对数的存在 |
| `thm:jets-bms` | thm | [A] | BMS 方程 |
| `prop:jets-ngl-beyond` | prop | [P] | 超出领头对数与有限 $N_c$ |
| `thm:jets-ngl-factorization` | thm | [A] | 喷注过程的有效场论因子化 |
| `prop:jets-sll` | prop | [P] | 超领头对数 |
| `sec:jets-irsafe` | sec | — | section |
| `sec:jets-hadronization` | sec | — | section |
| `sec:jets-ngl` | sec | — | section |
| `sec:jets-sll` | sec | — | section |
| `fig:jets-sw-cone` | fig | — | figure (required) |
| `fig:jets-ngl` | fig | — | figure (required) |
| `fig:jets-gap` | fig | — | figure (required) |

Optional table owned by this unit (not a registry row): `tab:jets-soft-functions`.

### Ch17

| label | type | tag | title |
|---|---|---|---|
| `def:smallx-regge` | def | (no tag) | 高能极限 |
| `thm:smallx-bfkl` | thm | [A] | BFKL 方程 |
| `prop:smallx-kt` | prop | [P] | $k_T$（高能）因子化 |
| `thm:smallx-bk` | thm | [A] | BK 方程与 JIMWLK |
| `conj:smallx-saturation` | conj | [C] | 饱和与色玻璃凝聚 |
| `rem:smallx-nonuniform` | rem | (no tag) | 共线因子化在小 $x$ 的非一致性 |
| `ex:smallx-dla` | ex | (no tag) | DGLAP 与 BFKL 的双领头对数重叠 |
| `sec:smallx-regge` | sec | — | section |
| `sec:smallx-bfkl` | sec | — | section |
| `sec:smallx-kt` | sec | — | section |
| `sec:smallx-dipole` | sec | — | section |
| `sec:smallx-status` | sec | — | section |
| `fig:bfkl-ladder` | fig | — | figure (required) |
| `fig:smallx-dipole` | fig | — | figure (required) |
| `fig:smallx-map` | fig | — | figure (required) |

### Ch18

| label | type | tag | title |
|---|---|---|---|
| `def:break-generalized-tmd` | def | (no tag) | 标准与广义 TMD 因子化 |
| `prop:break-measurement` | prop | [R, R_cond] | 测量相容性判据 |
| `rem:break-measurement-failures` | rem | (no tag) | 失效的位置 |
| `prop:break-colour` | prop | [R, R_PT] | 单个额外胶子的色因子（胶子极强度） |
| `ex:break-colour` | ex | (no tag) | 由投影算符得到 $C_G$ 表；阿贝尔极限；纠缠检验 |
| `thm:break-tmd` | thm | [V] | 强子—强子末态强子的 TMD 因子化不成立 |
| `ex:break-c07` | ex | (no tag) | Collins 2007 的双胶子反常（阿贝尔标量模型） |
| `prop:break-spacelike` | prop | [V] | 类空共线极限中严格共线因子化的失效 |
| `ex:break-spacelike` | ex | (no tag) | CdFR 单圈类空劈裂的色结构 |
| `prop:break-mass-singularity` | prop | [C] | 超出 NNLO 的质量奇异性因子化 |
| `prop:break-fss` | prop | [V] | Coulomb 相位与软交换不对易导致的共线因子化破坏 |
| `prop:break-jet-veto` | prop | [V] | 对多重部分子相互作用敏感的观测量 |
| `def:break-diffraction` | def | (no tag) | 衍射 DIS 与衍射部分子分布 |
| `thm:break-ddis` | thm | [A] | 衍射 DIS 的因子化 |
| `prop:break-hh-diffraction` | prop | [V] | 强子—强子硬衍射中的因子化破坏 |
| `def:break-dpdf` | def | (no tag) | 双部分子分布与双 Drell–Yan |
| `thm:break-double-dy` | thm | [A] | 双 Drell–Yan 的因子化 |
| `conj:break-dps-coloured` | conj | [C] | 有色末态的双部分子散射 |
| `conj:break-pocket` | conj | [C] | "口袋公式" $\sigma_{\rm DPS}=\sigma_A\sigma_B/\sigma_{\rm eff}$ |
| `sec:break-overview` | sec | — | section |
| `sec:break-tmd` | sec | — | section |
| `sec:break-spacelike` | sec | — | section |
| `sec:break-mpi` | sec | — | section |
| `sec:break-diffraction` | sec | — | section |
| `sec:break-dps` | sec | — | section |
| `sec:break-summary` | sec | — | section |
| `tab:break-cases` | tab | — | table |
| `tab:break-correspondence` | tab | — | table |
| `fig:violation-cq` | fig | — | figure (required) |
| `fig:diffraction` | fig | — | figure (required) |
| `fig:dps` | fig | — | figure (required) |

Optional figures owned by this unit (not registry rows): `fig:break-spacelike`, `fig:break-measurement`.

### Ch19

| label | type | tag | title |
|---|---|---|---|
| `def:excl-da` | def | (no tag) | 介子分布振幅 |
| `prop:excl-erbl` | prop | [R, R_PT] | 单圈 ERBL 演化 |
| `prop:excl-soft-cancel` | prop | [R, R_cond] | 色单态介子的软胶子在被积函数层次相消 |
| `thm:excl-pion-ff` | thm | [A] | 介子电磁形状因子的因子化 |
| `prop:excl-pion-lo` | prop | [R, R_PT] | 领头阶硬核 |
| `ex:excl-pion-ff-lo` | ex | (no tag) | 领头阶 $\pi$ 形状因子 |
| `thm:excl-transition` | thm | [A] | $\gamma^*\gamma\to\pi^0$ 形状因子 |
| `prop:excl-endpoint` | prop | [P] | 端点区域与软重叠 |
| `def:excl-gpd` | def | (no tag) | 广义部分子分布 |
| `prop:excl-polynomiality` | prop | [R, R_def] | 多项式性与 Ji 求和规则 |
| `thm:excl-dvcs` | thm | [A] | DVCS 的因子化 |
| `prop:excl-dvcs-lo` | prop | [R, R_PT] | DVCS 领头阶系数函数 |
| `thm:excl-meson-L` | thm | [A] | 纵向光子介子产生的因子化 |
| `prop:excl-meson-T` | prop | [V] | 横向光子：标准共线因子化失效 |
| `rem:excl-hadron-scattering` | rem | (no tag) | 宽角强子散射 |
| `prop:excl-near-threshold` | prop | [P] | 近阈重夸克偶素光生（重夸克极限） |
| `sec:excl-da` | sec | — | section |
| `sec:excl-soft` | sec | — | section |
| `sec:excl-ff` | sec | — | section |
| `sec:excl-endpoint` | sec | — | section |
| `sec:excl-gpd` | sec | — | section |
| `sec:excl-dvcs` | sec | — | section |
| `sec:excl-threshold` | sec | — | section |
| `tab:excl-correspondence` | tab | — | table |
| `fig:pion-ff` | fig | — | figure (required) |
| `fig:dvcs-handbag` | fig | — | figure (required) |
| `fig:meson-production` | fig | — | figure (required) |

Optional figures owned by this unit (not registry rows): `fig:excl-erbl`, `fig:excl-endpoint`.

### Ch20

| label | type | tag | title |
|---|---|---|---|
| `thm:heavy-bdpi` | thm | [A] | $B\to D\pi$ 的全阶因子化 |
| `prop:heavy-btopi-ff` | prop | [A] | 重到轻形状因子：软重叠与硬旁观者 |
| `prop:heavy-qcdf-lp` | prop | [P] | 无粲两体衰变的领头幂次 QCD 因子化 |
| `prop:heavy-qcdf-endpoint` | prop | [V] | 幂次修正中的端点发散 |
| `thm:heavy-inclusive-b` | thm | [A] | 单举 $B$ 衰变的重夸克展开 |
| `def:heavy-nrqcd` | def | (no tag) | NRQCD 及其幂次计数 |
| `thm:heavy-nrqcd-decay` | thm | [A] | 衰变的 NRQCD 因子化 |
| `prop:heavy-nrqcd-matching` | prop | [R, R_PT] | 匹配系数 |
| `ex:heavy-cv` | ex | (no tag) | 阈值处的单圈 $c_v$ |
| `conj:heavy-nrqcd-production` | conj | [C] | 产生的 NRQCD 因子化 |
| `prop:heavy-quarkonium-fragmentation` | prop | [A] | 大 $p_T$ 重夸克偶素产生 |
| `sec:heavy-bdpi` | sec | — | section |
| `sec:heavy-qcdf` | sec | — | section |
| `sec:heavy-inclusive` | sec | — | section |
| `sec:heavy-nrqcd` | sec | — | section |
| `fig:nrqcd` | fig | — | figure (required) |
| `fig:heavy-bdpi` | fig | — | figure (required) |
| `fig:heavy-qcdf` | fig | — | figure (required) |

### Ch21

| label | type | tag | title |
|---|---|---|---|
| `prop:power-dis-twist4-x` | prop | [A] | DIS 扭度 4 修正的 $x$ 空间形式 |
| `prop:power-twist3-sidis` | prop | [P] | SIDIS 型过程中的扭度 3 共线因子化 |
| `conj:power-twist3-pp` | conj | [C] | 强子—强子碰撞中单举强子单自旋不对称的扭度 3 因子化 |
| `ex:power-sgp` | ex | (no tag) | 最低阶的软胶子极点机制 |
| `prop:power-next-to-soft` | prop | [R, R_PT] | 次软定理 |
| `prop:power-nlp-endpoint` | prop | [P] | 次领头幂次因子化与端点发散 |
| `prop:power-rearrangement` | prop | [R, R_def] | OPE 基的重排自由 |
| `rem:power-practical-ope` | rem | (no tag) | "实用 OPE" 与重整化子吸收的两个猜想性成分 |
| `def:power-borel` | def | (no tag) | Borel 变换与重整化子 |
| `prop:power-adler-large-beta0` | prop | [P] | 大 $\beta_0$ 极限下的 Adler 函数 |
| `ex:power-renormalon-chain` | ex | (no tag) | 带 $n$ 个费米子泡的单胶子 |
| `prop:power-renormalon-examples` | prop | [P] | 若干过程中的重整化子与幂次修正 |
| `conj:power-renormalon-ht` | conj | [C] | 红外重整化子与高扭度的一般对应 |
| `rem:power-np-status` | rem | (no tag) | 非微扰地位 |
| `thm:power-ope-convergence` | thm | [R, R_PT] | 微扰 $\varphi^4_4$ 中 OPE 的收敛性 |
| `prop:power-thooft-model` | prop | [P] | 't Hooft 模型 |
| `sec:power-twist4` | sec | — | section |
| `sec:power-twist3` | sec | — | section |
| `sec:power-nlp` | sec | — | section |
| `sec:power-ope-basis` | sec | — | section |
| `sec:power-renormalons` | sec | — | section |
| `sec:power-np` | sec | — | section |
| `fig:renormalon-chain` | fig | — | figure (required) |
| `fig:twist3-ssa` | fig | — | figure (required) |
| `fig:power-borel-plane` | fig | — | figure (required) |

### Ch25

| label | type | tag | title |
|---|---|---|---|
| `sec:summary-master` | sec | — | section |
| `sec:summary-hypotheses` | sec | — | section |
| `sec:summary-dependency` | sec | — | section |
| `sec:summary-lessons` | sec | — | section |
| `sec:summary-open` | sec | — | section |
| `tab:summary-master` | tab | — | table |
| `tab:summary-assumptions` | tab | — | table |
| `fig:summary-status-map` | fig | — | figure (required) |
| `fig:summary-hypotheses` | fig | — | figure (required) |

Optional figures owned by this unit (not registry rows): `fig:summary-chapter-dag`.

### AppA

| label | type | tag | title |
|---|---|---|---|
| `lem:appA-fierz` | lem | (数学，无标签) | 共线 Fierz 分解 |
| `def:appA-test-functions` | def | (no tag) | 测试函数类与弱收敛 |
| `lem:appA-plus-product` | lem | (数学，无标签) | 乘积约定下的恒等式 |
| `lem:appA-weak-convergence` | lem | (数学，无标签) | 由偶数矩得到弱收敛 |
| `lem:appA-mellin-table` | lem | (数学，无标签) | Mellin 变换表 |
| `sec:appA-lightfront` | sec | — | section |
| `sec:appA-dirac` | sec | — | section |
| `sec:appA-plus` | sec | — | section |
| `sec:appA-mellin` | sec | — | section |

### AppB

| label | type | tag | title |
|---|---|---|---|
| `prop:appB-rules` | prop | [R, R_def] | Wilson 线的 Feynman 规则 |
| `lem:appB-shuffle` | lem | (数学，无标签) | 程函恒等式（洗牌积） |
| `prop:appB-webs` | prop | [A] | 非阿贝尔指数化 |
| `prop:appB-cusp-oneloop` | prop | [R, R_PT] | 单圈尖点反常维度 |
| `sec:appB-definition` | sec | — | section |
| `sec:appB-rules` | sec | — | section |
| `sec:appB-eikonal` | sec | — | section |
| `sec:appB-cusp` | sec | — | section |

### AppC

| label | type | tag | title |
|---|---|---|---|
| `rem:appC-Seps` | rem | (no tag) | $S_\varepsilon$ 约定的影响 |
| `rem:appC-d-kernels` | rem | (no tag) | $D$ 维劈裂核与平均约定 |
| `lem:appC-bubble` | lem | (数学，无标签) | 单圈两点函数 |
| `lem:appC-ibp` | lem | (数学，无标签) | 分部积分（三角规则） |
| `lem:appC-phase-space` | lem | (数学，无标签) | $D$ 维相空间 |
| `sec:appC-msbar` | sec | — | section |
| `sec:appC-integrals` | sec | — | section |
| `sec:appC-phase-space` | sec | — | section |
| `sec:appC-formfactor` | sec | — | section |

### AppD

| label | type | tag | title |
|---|---|---|---|
| `lem:appD-gordan` | lem | (数学，无标签) | Gordan 择一定理 |
| `rem:appD-parameter-proof` | rem | (no tag) | Landau 条件的 Feynman 参数证明及其注意事项 |
| `sec:appD-gordan` | sec | — | section |
| `sec:appD-momentum` | sec | — | section |
| `sec:appD-alpha` | sec | — | section |
| `sec:appD-cn` | sec | — | section |
| `sec:appD-caveats` | sec | — | section |

### AppE

| label | type | tag | title |
|---|---|---|---|
| `prop:appE-degree` | prop | [R, R_PT] | 约化图的超表观红外发散度 |
| `rem:appE-actual-bound` | rem | [A] | 从超表观度到实际界 |
| `sec:appE-units` | sec | — | section |
| `sec:appE-formula` | sec | — | section |
| `sec:appE-examples` | sec | — | section |

Optional figures owned by this unit (not registry rows): `fig:appE-boost`.

### AppF

| label | type | tag | title |
|---|---|---|---|
| `ex:appF-telescoping` | ex | (no tag) | 有限 Wilson 线的伸缩恒等式 |
| `prop:appF-two-gluon` | prop | [R, R_PT] | 两个纵向胶子：树图层次的完整证明 |
| `prop:appF-induction` | prop | [A] | 多胶子情形的归纳论证 |
| `sec:appF-one` | sec | — | section |
| `sec:appF-two` | sec | — | section |
| `sec:appF-induction` | sec | — | section |
| `sec:appF-gy` | sec | — | section |

### AppG

| label | type | tag | title |
|---|---|---|---|
| `sec:appG-ee` | sec | — | section |
| `sec:appG-dis` | sec | — | section |
| `sec:appG-dy` | sec | — | section |
| `sec:appG-pdf` | sec | — | section |
| `sec:appG-tmd` | sec | — | section |

### AppI

| label | type | tag | title |
|---|---|---|---|
| `def:appI-hvbm` | def | (no tag) | HVBM 方案 |
| `prop:appI-larin` | prop | [R, R_PT] | Larin 方案与非单态轴矢流的有限重整化 |
| `rem:appI-anomaly` | rem | (no tag) | 轴矢反常 |
| `sec:appI-hvbm` | sec | — | section |
| `sec:appI-larin` | sec | — | section |
| `sec:appI-anomaly` | sec | — | section |

### AppJ

| label | type | tag | title |
|---|---|---|---|
| `prop:appJ-ghost-cuts` | prop | [R, R_PT] | 割图中的鬼场贡献 |
| `lem:appJ-cut-hermiticity` | lem | [R, R_def] | 割图规则的厄米性 |
| `prop:appJ-local-operators` | prop | [R, R_PT] | 规范不变定域算符的重整化与混合 |
| `rem:appJ-nonlocal` | rem | [A] | 非定域算符 |
| `sec:appJ-brst` | sec | — | section |
| `sec:appJ-cuts` | sec | — | section |
| `sec:appJ-operators` | sec | — | section |

### AppK

| label | type | tag | title |
|---|---|---|---|
| `lem:appK-hausdorff` | lem | (数学，无标签) | Hausdorff 唯一性 |
| `thm:appK-even-moments` | thm | (数学，无标签) | 偶数矩决定函数 |
| `cor:appK-pdf` | cor | (数学，无标签) | PDF 的唯一性 |
| `prop:appK-kernels` | prop | (数学，无标签) | 领头阶核由偶数矩唯一确定 |
| `thm:appK-carlson` | thm | (数学，无标签) | Carlson 定理 |
| `prop:appK-continuation` | prop | (数学，无标签) | 多项式有界条件下延拓的唯一性 |
| `thm:appK-muntz` | thm | (数学，无标签) | Müntz–Szász 定理 |
| `lem:appK-entire` | lem | (数学，无标签) | 受控增长的整函数 |
| `lem:appK-markov` | lem | (数学，无标签) | V. A. Markov 系数不等式 |
| `rem:appK-counterexamples` | rem | (no tag) | 反例与稳定性 |
| `sec:appK-hausdorff` | sec | — | section |
| `sec:appK-continuation` | sec | — | section |
| `sec:appK-entire` | sec | — | section |
| `sec:appK-counterexamples` | sec | — | section |

### AppL

| label | type | tag | title |
|---|---|---|---|
| `lem:appL-divided-differences` | lem | (数学，无标签) | 均差恒等式 |
| `prop:appL-bare` | prop | [R, R_def] | 裸算符恒等式 |
| `prop:appL-renormalized` | prop | [R, R_PT] | 重整化后的矩关系 |
| `sec:appL-vertices` | sec | — | section |
| `sec:appL-bare` | sec | — | section |
| `sec:appL-renormalized` | sec | — | section |

### Assumptions

The 25 register entries of refdoc §5.3 with the propagation tag proposed by Rule TA (§0.3 item 4 = WRITER_SPEC_v2 v2.1 §4.4 item 2). The register itself, its contents and final tags are `ASSUMPTIONS.md`'s [SYNC-ASM]; "risk" marks entries whose register status sentence could be read as \tagP / \tagC, which would demote the [A] process theorems that use them (merge decision, §0.3 item 4).

| label | owner | proposed tag | content (short) | register status (refdoc §5.3) |
|---|---|---|---|---|
| `asm:intro-wightman` | Ch01 | [C] | Wightman QCD (W1)-(W4), (W2) corrected | open (4D QCD not constructed) |
| `asm:intro-composite` | Ch01 | [C] | gauge-invariant composite operators, twist-2 = O_q, O_g, RG | open |
| `asm:intro-np-ope` | Ch01 | [C] | non-perturbative OPE between vacuum/hadron states; chiral-odd suppression | open, widely assumed |
| `asm:intro-af-coeff` | Ch01 | [C] | coefficients asymptotic to their MSbar series at $\mu=ert qert$ | open |
| `asm:intro-growth` | Ch01 | [C] | lim T_2(iy)/(iy)=0 (low-moment sum rules) | open; holds at computed fixed orders |
| `asm:intro-bridge` | Ch01 | [C] | region completeness and power counting transfer to hadrons | open |
| `asm:appM-remainder` | AppM | [A] | momentum-space remainder of the frozen-q bilocal normal product | open as stated; possibly dischargeable |
| `asm:appM-brst-ope` | AppM | [A] | (B1)(B2) BRST-symmetric insertions in the OPE | open as stated; partly dischargeable |
| `asm:appM-forward` | AppM | [A] (risk: [P]) | OPE remainder for forward on-shell massless partons | open; verified at O(alpha_s), N<=8 |
| `asm:appN-contour` | AppN | [A] | (GA1) admissible contour | open in general |
| `asm:appN-envelope` | AppN | [A] | (GA3) integrable power-counting envelopes | open (integral form never written) |
| `asm:appN-separation` | AppN | [A] | (GA4) Lojasiewicz-type separation | open; verified in the one-loop triangle |
| `asm:appN-collins` | AppN | [A] | (CS1)-(CS3) for every integrand | [A]-level (Collins 2011 ch. 10) |
| `asm:appN-values` | AppN | (no tag) | value rule for divergent chain terms; scaleless = 0 | convention |
| `asm:appN-cutsum` | AppN | [A] | cut-summed representation | open; provided by App O for DY-type graphs |
| `asm:appN-ward-product` | AppN | [A] | Ward identities on modified integrands; product structure | [A] |
| `asm:appN-uv` | AppN | [A] | UV renormalization compatible with the approximators | partly proven |
| `asm:appN-multren` | AppN | [A] (risk: (Z2) read as [C]) | (Z1)-(Z3) multiplicative renormalization; IR regulator | (Z1) partly theorem; (Z2) genuine input |
| `asm:appN-tmd` | AppN | [A] | (T1)-(T4) TMD inputs | one loop verified; all orders [A] |
| `asm:appN-endpoint` | AppN | [A] (risk: [P]) | (E1)-(E3) endpoint conditions | true for finite Gegenbauer truncations |
| `asm:appO-lcopt` | AppO | [A] (risk: [P]) | (i)(ii) LCOPT zero modes and instantaneous loops | open; [P] in the light-front literature |
| `asm:appO-envelope` | AppO | [A] | integrable envelope for the equal-time rewriting | open |
| `asm:appO-mixing` | AppO | [A] | (a)-(c) mixing/unitarity of coincident connections | (a)(b) automatic for G_0; (c) O(g^4) eikonal case shown |
| `asm:appO-deformation` | AppO | [A] | (a)-(d) deformation targets and compatibility | (a) proved for G_0; (b)-(d) open |
| `asm:appO-rewritten-cs` | AppO | [A] | (CS1)(CS2) for rewritten forms | open; Glauber-specific |

### Counts (core units)

| unit | statements (incl. examples) | of which ex | asm | sections | tables | required figures | optional figures |
|---|---|---|---|---|---|---|---|
| front | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| Ch01 | 15 | 1 | 6 | 8 | 3 | 4 | 0 |
| Ch02 | 44 | 10 | 0 | 12 | 1 | 5 | 2 |
| Ch03 | 25 | 6 | 0 | 6 | 1 | 3 | 0 |
| Ch04 | 30 | 5 | 0 | 7 | 1 | 8 | 1 |
| Ch05 | 17 | 4 | 0 | 6 | 0 | 4 | 0 |
| Ch06 | 24 | 3 | 0 | 8 | 0 | 3 | 0 |
| Ch07 | 37 | 4 | 0 | 10 | 1 | 7 | 1 |
| Ch08 | 30 | 4 | 0 | 9 | 0 | 4 | 2 |
| Ch09 | 43 | 5 | 0 | 8 | 3 | 10 | 0 |
| Ch10 | 20 | 4 | 0 | 9 | 1 | 3 | 0 |
| Ch11 | 23 | 1 | 0 | 5 | 0 | 3 | 1 |
| Ch12 | 30 | 5 | 0 | 9 | 2 | 5 | 0 |
| Ch13 | 7 | 1 | 0 | 5 | 0 | 2 | 0 |
| Ch14 | 28 | 3 | 0 | 9 | 1 | 4 | 2 |
| Ch15 | 20 | 3 | 0 | 8 | 0 | 2 | 1 |
| Ch16 | 11 | 1 | 0 | 4 | 0 | 3 | 0 |
| Ch17 | 7 | 1 | 0 | 5 | 0 | 3 | 0 |
| Ch18 | 19 | 3 | 0 | 7 | 2 | 3 | 2 |
| Ch19 | 16 | 1 | 0 | 7 | 1 | 3 | 2 |
| Ch20 | 11 | 1 | 0 | 4 | 0 | 3 | 0 |
| Ch21 | 16 | 2 | 0 | 6 | 0 | 3 | 0 |
| Ch25 | 0 | 0 | 0 | 5 | 2 | 2 | 1 |
| AppA | 5 | 0 | 0 | 4 | 0 | 0 | 0 |
| AppB | 4 | 0 | 0 | 4 | 0 | 0 | 0 |
| AppC | 5 | 0 | 0 | 4 | 0 | 0 | 0 |
| AppD | 2 | 0 | 0 | 5 | 0 | 0 | 0 |
| AppE | 2 | 0 | 0 | 3 | 0 | 0 | 1 |
| AppF | 3 | 1 | 0 | 4 | 0 | 0 | 0 |
| AppG | 0 | 0 | 0 | 5 | 0 | 0 | 0 |
| AppI | 3 | 0 | 0 | 3 | 0 | 0 | 0 |
| AppJ | 4 | 0 | 0 | 3 | 0 | 0 | 0 |
| AppK | 10 | 0 | 0 | 4 | 0 | 0 | 0 |
| AppL | 3 | 0 | 0 | 3 | 0 | 0 | 0 |
| **total** | 514 | 69 | 6 | 199 | 20 | 87 | 16 |

Tags of the 514 statement labels: (no tag) 194; A 90; R, R_PT 88; R, R_def 35; (数学，无标签) 33; C 21; P 15; V 14; R, R_cond 13; R, R_OPE 11.
Labels new relative to v1: 127 (v1 labels carried over: 387 of 394; the 7 v1 `lattice` labels are registered by `OUTLINE_frontier.md`). [PENDING-VERIFY] markers inside statement entries: 99.


---------------------------------------------------------------------------------------------------

## CHANGELOG

**2026-10-10 — OUTLINE_core drafted (spec-v2 core drafter).** Inputs as listed in the status block at the top of this file.

1. **Renumbering v1 → v2** (binding structure, WRITER_SPEC_v2 §1.1). v1 Ch1 → Ch1; v1 Ch2 `prelim` → split into the new pedagogical **Ch2 `qcd`** (QCD basics; the nine moved labels keep their `prelim` key) and **Ch3 `prelim`** (tools); v1 Ch3–Ch20 → Ch4–Ch21 (keys unchanged: `ir`, `sudakov`, `ee`, `dis`, `pdf`, `method`, `disall`, `coll`, `dy`, `thr`, `tmd`, `scet`, `jets`, `smallx`, `break`, `excl`, `heavy`, `power`); v1 Ch21 `lattice` → absorbed by Ch22 `lamet` (`OUTLINE_frontier.md`; labels kept); v1 Ch22 `summary` → **Ch25 `summary`**; App A–L keep their keys and labels. Part dividers as in WRITER_SPEC_v2 §1.1 note 4.
2. **New Ch2 `qcd`** (REQUIREMENTS 3e, WRITER_SPEC_v2 §7): 44 statement labels, of which 35 are new in v2 (10 worked examples; `rem:prelim-bphz-brst` from refdoc S14) and 9 are moved v1 labels; canonical statements for gauge invariance, Faddeev–Popov, BRST nilpotency and cohomology, the regularized and renormalized Slavnov–Taylor identities, renormalizability, $\xi$ independence, composite operators, the one-loop $\beta$ function and asymptotic freedom, and the introductory IR facts (Bloch–Nordsieck/KLN only previewed, owned by Ch4), each graded honestly (statements whose complete proofs are only in the literature are [R, R_PT] with "proof: sketch + literature"; VF-QCD-4 general-$\xi_g$ constants status C, re-derived by the writer).
3. **refdoc §5.5 (S13–S45)** applied chapter by chapter (map in §0.11); new labels per unit (relative to v1): Ch01 9; Ch02 35; Ch03 6; Ch04 5; Ch05 1; Ch06 2; Ch07 13; Ch08 3; Ch09 16; Ch10 4; Ch11 2; Ch12 8; Ch14 4; Ch15 1; Ch18 2; Ch19 2; Ch20 1; Ch21 2; AppA 2; AppC 1; AppD 1; AppF 1; AppJ 1; AppK 2; AppL 3. Boxes 「本章证明了什么／没有证明什么」 for Ch2–Ch21; correspondence tables `tab:dis-correspondence`, `tab:method-correspondence`, `tab:disall-correspondence`, `tab:dy-correspondence`, `tab:tmd-correspondence`, `tab:break-correspondence`, `tab:excl-correspondence`.
4. **refdoc §5.7 (S50–S53)**: App A `def:appA-test-functions`, `lem:appA-weak-convergence`; App C `rem:appC-d-kernels`; App D `rem:appD-parameter-proof`; App E boost-and-dimension proof and the `asm:appN-envelope` link; App F `ex:appF-telescoping` and the Grammer–Yennie $i0$; App J `lem:appJ-cut-hermiticity`; App K `lem:appK-entire`, `lem:appK-markov` and the Hausdorff caveat. App A–L stay at 35 pp with the rebalancing proposal of §0.2 (lead-author decision).
5. **refdoc §5.4 (S9–S12)**: S9 FF normalization kept from the v1 audit; S10 budgets superseded by the lead-author budgets; S11 Glauber direction $e_G$ (Ch9); S12 `asm:` labels and the `assumption` environment (Ch1 owns and states the six global `asm:intro-*`).
6. **refdoc §5.8–5.9**: VF-REF-1…19 cited at the statements; master-table rows 69–75 of refdoc S55 are rows II.14, II.15, III.3, III.4, III.25, III.27, V.10 of `tab:summary-master`; refdoc S56 figure owners as in FIGURES_INDEX_v2 (registry above).
7. **Tag system v2**: qualifiers R_PT / R_def / R_OPE / R_cond on every [R]; status changes of §0.8 (all weakenings or renamings; no v1 tag strengthened, checked against the v1 registry); non-perturbative status lines with `asm:` labels replace the MA lines; error types and grade dictionary in Ch1; Rule TA (= WRITER_SPEC_v2 v2.1 §4.4 item 2, §4.6 item 3) for the technical assumptions.
8. **Lean-blueprint formalism**: every def/asm/lem/prop/thm/cor/conj, every tagged remark and every example that relies on other statements carries a `\uses{…}` line (or `% uses: none`); the drafter's checker verifies: headers and labels (K1), presence (K2), backward-only order and defined labels (K3), grade propagation with the v2.1 R_OPE rule (K4), qualifier compatibility (K4q), R_cond premise sentences (K4p, K4r), all mentioned labels defined or external (K5), status paragraphs (K6): all OK; reported exception: `thm:dis-moments`(b) [R, R_OPE] uses the global-only R_cond statements `thm:dis-fixed-n`, `prop:dis-dispersion-np`, `thm:dis-moments-np` (§0.3 item 3).
9. **Ch25**: master table `tab:summary-master` (every theorem, conjecture, [V], [P] and R_cond statement of Ch2–Ch21, the App N/O main results, the frontier block [SYNC-FRONTIER]; tags checked against the entries; row IDs use part numerals to avoid collisions with the claim IDs of `verify/CLAIMS.md`); incidence matrix `tab:summary-assumptions`; new section `sec:summary-dependency`; open problems OP-A1 … OP-F9 merging v1 Ch22, refdoc S44 and the frontier reports.
10. **Assembly fixes found by the drafter's QA** (all applied above): forward uses removed (`prop:excl-near-threshold` → `def:heavy-nrqcd` is now a pointer; the one-loop part of `prop:qcd-st-relations` points to the following examples); non-positive premises removed from positive claims (`prop:break-mass-singularity` no longer uses the [V] statement `prop:break-spacelike`; `thm:heavy-inclusive-b` and `prop:heavy-quarkonium-fragmentation` no longer use [C] conjectures as premises — the duality and NRQCD steps are named in their status paragraphs); premise sentences completed (`prop:disall-factorized-subtraction`, `prop:break-measurement`); `prop:disall-two-routes` refers to `def:method-collins-conditions` instead of the [A] theorem; `thm:dis-moments-np` uses the operator RG directly (v2.1 R_OPE rule); `cor:dis-weak-xspace` uses the new `lem:appA-weak-convergence`; `sec:dis-rg` restored; part names aligned with WRITER_SPEC_v2 §1.1 note 4; `prop:jets-ngl-beyond` added to the master table; **bottleneck consistency** (WRITER_SPEC_v2 §6, Ch25 rules): the `\uses` lists of `prop:ir-super-leading`, `thm:ir-leading-regions`, `prop:dis-ope-euclid`, `prop:method-glauber-deformation` and `thm:sudakov-factorization` now contain the `asm:` entries named in their status paragraphs, so that every `asm:` label of the master table's 瓶颈 column lies in the `\uses` closure of its statement (checked); Markdown tables checked for cell counts (no `|` inside formulas).
