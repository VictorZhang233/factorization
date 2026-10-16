# FINAL_OUTLINE_synth -- SYNTHETIC registry for the integration-tool tests (not the book's outline)

## 0. Global decisions

### 0.1 Structure

| part | # | key | file | 中文标题（`\chapter{}` 标题） | pp |
|---|---|---|---|---|---|
| I | 1 | `intro` | `ch01_intro.tex` | 引言（合成测试） | 1 |
| II | 7 | `dis` | `ch07_dis.tex` | 深度非弹散射（合成测试） | 1 |
| III | 9 | `method` | `ch09_method.tex` | 一般方法（合成测试） | 1 |
| III | 12 | `dy` | `ch12_dy.tex` | Drell–Yan（合成测试） | 1 |
| 附录 | N | `appN` | `appN_subtraction.tex` | 减除法（合成测试） | 1 |
| 附录 | P | `appP` | `appP_blueprint.tex` | 形式化蓝图：假设登记表、依赖图与状态表 | 1 |

## 08 Label registry (synthetic)

### Ch01

| label | type | tag | title |
|---|---|---|---|
| `def:intro-tags` | def | (no tag) | 严格性标签 |
| `asm:intro-wightman` | asm | [C] | QCD 的 Wightman 结构 |
| `asm:intro-np-ope` | asm | [C] | 非微扰算符乘积展开 |
| `asm:intro-bridge` | asm | [C] | 桥接假设 |
| `prop:intro-algebra` | prop | [R, R_def] | 代数命题 |
| `sec:intro-tags` | sec | — | section |

### Ch05

| label | type | tag | title |
|---|---|---|---|
| `thm:sudakov-factorization` | thm | [A] | Sudakov 形状因子的因子化 |

### Ch07

| label | type | tag | title |
|---|---|---|---|
| `def:dis-kinematics` | def | (no tag) | DIS 运动学 |
| `thm:dis-ope` | thm | [A] | 欧氏 OPE |
| `thm:dis-moments` | thm | [R, R_OPE] | 矩的因子化 |
| `prop:dis-short` | prop | [R, R_OPE] | 矩的推论 |
| `lem:dis-ptlemma` | lem | [R, R_PT] | 微扰引理 |
| `lem:dis-forward` | lem | [R, R_PT] | 前向依赖的引理 |
| `prop:dis-rdef` | prop | [R, R_def] | 定义推论 |
| `prop:dis-notverbatim` | prop | [R, R_PT] | 限定语不逐字 |
| `prop:dis-violated` | prop | [V] | 被破坏的命题 |
| `thm:dis-usesv` | thm | [A] | 使用 [V] 的定理 |
| `ex:dis-example` | ex | (no tag) | 例子 |
| `rem:dis-tagged` | rem | [A] | 带标签的注 |
| `lem:dis-twouses` | lem | [R, R_PT] | 两个依赖行 |
| `thm:dis-nouses` | thm | [R, R_PT] | 缺依赖行 |
| `lem:dis-brackets` | lem | (数学，无标签) | 区间上的界 |
| `def:dis-latelabel` | def | (no tag) | 标签位置 |
| `prop:dis-weakened` | prop | [A] | 被减弱的命题 |
| `prop:dis-strengthened` | prop | [P] | 被加强的命题 |
| `prop:dis-missing` | prop | [R, R_PT] | 未写出的命题 |
| `prop:dy-misplaced` | prop | [R, R_PT] | 放错单元的命题 |
| `ex:dis-seclabel` | ex | (no tag) | 节标签依赖 |
| `lem:dis-hidden` | lem | [R, R_PT] | 隐藏的前向依赖 |
| `fig:synth-same` | fig | — | figure (required) |
| `fig:synth-changed` | fig | — | figure (required) |

### Ch09

| label | type | tag | title |
|---|---|---|---|
| `lem:method-ward-multi` | lem | [A] | 多胶子 Ward 恒等式 |
| `thm:method-template` | thm | [A] | 因子化模板 |
| `lem:method-relay` | lem | [A] | 中继引理 |
| `prop:method-gapless` | prop | [A] | 未点名缺口的命题 |

### Ch12

| label | type | tag | title |
|---|---|---|---|
| `thm:dy-factorization` | thm | [A] | DY 因子化 |
| `prop:dy-model` | prop | [P] | 模型命题 |
| `conj:dy-coloured` | conj | [C] | 有色末态 |
| `prop:dy-late` | prop | [A] | 地位段落滞后 |
| `prop:dy-npline` | prop | [A] | 非微扰地位行含技术假设 |
| `prop:dy-hadron` | prop | [A] | 强子层面命题 |
| `prop:dy-forbidden` | prop | [A] | 禁用措辞 |
| `prop:dy-ctech` | prop | [A] | 使用 C 假设的命题 |
| `fig:synth-nosource` | fig | — | figure (required) |

### Ch25

| label | type | tag | title |
|---|---|---|---|
| `sec:summary-master` | sec | — | section |
| `tab:summary-master` | tab | — | table |

### AppN

| label | type | tag | title |
|---|---|---|---|
| `asm:appN-collins` | asm | [A] | Collins 条件 |
| `asm:appN-values` | asm | (no tag) | 取值规则 |
| `asm:appN-brst-nonlocal` | asm | [C] | BRST 分类 |
| `asm:appN-unused` | asm | [A] | 未被使用的假设 |
| `asm:appN-wrongtag` | asm | [P] | 标签不符的假设 |
| `asm:appN-missing` | asm | [A] | 未写出的假设 |
| `thm:appN-subtraction` | thm | [R, R_cond] | 条件减除定理 |
| `thm:appN-structure` | thm | [R, R_cond] | 因子化结构 |
| `thm:appN-noprem` | thm | [R, R_cond] | 缺前提句 |
| `prop:appN-late` | prop | [R, R_cond] | 前提句靠后 |
| `lem:appN-cyc-a` | lem | (数学，无标签) | 环 A |
| `lem:appN-cyc-b` | lem | (数学，无标签) | 环 B |
| `lem:appN-hidden` | lem | (数学，无标签) | 附录中的辅助引理 |

### AppP

| label | type | tag | title |
|---|---|---|---|
| `def:appP-content-grade` | def | (no tag) | 内容等级 |
| `rem:appP-limits` | rem | (no tag) | 蓝图检查保证什么、不保证什么 |
| `sec:appP-intro` | sec | — | 导言 |
| `sec:appP-register` | sec | — | 假设登记表 |
| `tab:appP-register` | tab | — | 编号假设登记表 |
| `fig:appP-dependency` | fig | — | figure (required) |

### Assumptions

| label | owner | tag | 中文标题 | content (one line) | status | used by (direct, computed) | upgrade path |
|---|---|---|---|---|---|---|---|
| `asm:intro-wightman` | Ch1 | [C] | QCD 的 Wightman 结构 | (W1)–(W4) synthetic | open | `thm:dis-moments` | construct QCD |
| `asm:intro-np-ope` | Ch1 | [C] | 非微扰算符乘积展开 | (O1)(O2) synthetic | open | `thm:dis-moments` | — |
| `asm:intro-bridge` | Ch1 | [C] | 桥接假设 | (Br1)–(Br3) synthetic | open | `thm:dy-factorization`, `prop:dy-npline` | — |
| `asm:appN-collins` | AppN | [A] | Collins 条件 | (CS1)–(CS3) synthetic | [A] | `thm:appN-subtraction`, `thm:dy-factorization`, `thm:dis-ghost` | — |
| `asm:appN-values` | AppN | — | 取值规则 | (V1)(V2) | convention | `thm:appN-subtraction` | — |
| `asm:appN-brst-nonlocal` | AppN | [C] | BRST 分类 | named gap | no argument | `thm:appN-structure` | — |
| `asm:appN-unused` | AppN | [A] | 未被使用的假设 | — | [A] | — | — |
| `asm:appN-wrongtag` | AppN | [P] | 标签不符的假设 | — | [P] | `thm:appN-structure` | — |
| `asm:appN-missing` | AppN | [A] | 未写出的假设 | — | [A] | — | — |

## 09 Master-table rows (fallback when ch25 is absent)

| # | 结论 | 公式/要点 | 标签 | 非微扰 | 规范标签 | 瓶颈假设 | 升级路径 | ★ |
|---|---|---|---|---|---|---|---|---|
| II.1 | 矩的因子化 | — | [R, R_OPE] | W | `thm:dis-moments` | `thm:dis-ope` | — | ★ |
| III.1 | DY 因子化 | — | [A] | Br | `thm:dy-factorization` | `asm:appN-collins` | — | ★ |

## 10 Reserved and optional labels (not registered)

The labels reserved for the slots X2b are **withdrawn** and must not be used.

## 11 Counts
