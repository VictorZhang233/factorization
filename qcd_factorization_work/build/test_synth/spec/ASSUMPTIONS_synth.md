# ASSUMPTIONS_synth -- SYNTHETIC register for the integration-tool tests

## 1. Summary table

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

## 2. MA0–MA4 dictionary
