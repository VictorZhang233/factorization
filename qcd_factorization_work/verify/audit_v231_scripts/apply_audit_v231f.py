"""Audit fixes v2.3.1, part f: verification bookkeeping removed from master-table rows (§09).

Usage:  python3 -I apply_audit_v231f.py SPECDIR
The rows of §09 are transcribed into the printed tables tab:summary-master (Ch25) and tab:intro-overview (Ch1, rows
marked ★); claim IDs, slot IDs and "已证实" are verification bookkeeping (WRITER_SPEC_v2 §6.12, v2.3.1) and are
removed; the physics content of each cell is kept. Labels and tags (checker E14) are untouched.
"""
import sys, os

SP = sys.argv[1]
FO = 'FINAL_OUTLINE_v2.md'
EDITS = [
    ("—（BM 假设已逐条核对：协变规范含鬼场的无质量 QCD 满足，N24）",
     "—（BM II 的假设对协变规范、含鬼场的无质量 QCD 成立）"),
    ("| 引用定理覆盖范围的核实（S63-1） | ★ |", "| 引用定理覆盖范围的核实 | ★ |"),
    ("（`CollinsRogersSato2022`；E35） |", "（`CollinsRogersSato2022`） |"),
    ("| 证明零动量匹配估计 (CTp)（`rem:appM-remainder-reduction`；槽位 X3a 未交付） |",
     "| 证明零动量匹配估计 (CTp)（`rem:appM-remainder-reduction`） |"),
    ("—（N12 已证实；完整的 (CS1)–(CS3)：III.39）", "—（完整的 (CS1)–(CS3)：III.39）"),
    ("| 解除 `asm:appN-collins`（S63-12） | ★ |", "| 解除 `asm:appN-collins` | ★ |"),
    ("—（已知结果：`Meggiolaro:1996hf`；N01）", "—（已知结果：`Meggiolaro:1996hf`、`Giordano:2006vv`）"),
    ("| N04 已证实为 [A]（先行工作 `Braun:2019qtp`）；App L 证明的循环性检查未做，不升级 |",
     "| [A]（先行工作 `Braun:2019qtp`）；App L 证明的循环性检查未完成，故不升级 |"),
    ("SYZ 只否定纯 Glauber 部分（E36） |", "SYZ 只否定纯 Glauber 部分（`Schwartz:2018obd`） |"),
]


def main():
    p = os.path.join(SP, FO)
    t = open(p, encoding='utf-8').read()
    s9 = t.index('\n## 09 ')
    e9 = t.index('\n## 10 ')
    sec = t[s9:e9]
    for old, new in EDITS:
        if sec.count(old) != 1:
            raise SystemExit('ABORT: §09: %d matches for %r' % (sec.count(old), old[:60]))
        sec = sec.replace(old, new)
    open(p, 'w', encoding='utf-8').write(t[:s9] + sec + t[e9:])
    print('%d row edits in §09' % len(EDITS))


if __name__ == '__main__':
    main()
