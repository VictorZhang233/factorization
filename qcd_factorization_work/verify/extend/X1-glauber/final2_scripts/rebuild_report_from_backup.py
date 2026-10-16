"""Rebuild X1-glauber_final2.md from its backup (lossless reconstruction form).

The backup (returned in the structured output field final_report_markdown) contains every
passage written or changed in revision 2 verbatim, and every passage copied unchanged from
X1-glauber_final.md as a marker line  [[VERBATIM final.md a-b]]  (lines a..b, 1-based, inclusive).
Rebuild = expand the markers, then apply the four one-line substitutions below (each must occur
exactly once).  This mirrors the assembly that produced the report.

usage: python3 -I rebuild_report_from_backup.py BACKUP.md X1-glauber_final.md OUT.md [EXPECTED.md]
"""
import hashlib, re, sys

BEGIN = '=====BEGIN REPORT BODY====='
MARK = re.compile(r'^\[\[VERBATIM final\.md (\d+)-(\d+)\]\]$')
SUBS = [
    ("**Novelty.** New; the idea was suggested, without proof, in the reference work notes (R7).",
     "**Novelty.** Ours (no marker); the idea was suggested, without proof, in the reference work notes (R7)."),
    ("## 12. Errata item ERR-S1b (proposed App Q entry; addendum to ERR-S1)",
     "## 12. Errata item ERR-S1b (App Q entry; addendum to ERR-S1)"),
    ("T2's statement concerns the Hermitian $C_AX$ residual $\\propto{\\rm Re}\\,p_{\\rm opp}$;",
     "T2's statement concerns the Hermitian $C_AX$ residual $\\propto{\\rm Re}\\,X_w$ (${\\rm Re}\\,p_{\\rm opp}$ in the normalization by $N$);"),
    ("| O1–O12 | OPEN-1–OPEN-12; OPEN-13 is new |",
     "| O1–O12 | OPEN-1–OPEN-12; OPEN-13 (final round) and OPEN-14 (revision 2) are new |"),
]


def rebuild(backup_text, src_lines):
    head, sep, body = backup_text.partition('\n' + BEGIN + '\n')
    if not sep:
        raise SystemExit('BEGIN line not found')
    body = body.rstrip('\n')
    out, n_mark = [], 0
    for line in body.split('\n'):
        m = MARK.match(line)
        if m:
            a, b = int(m.group(1)), int(m.group(2))
            out.extend(src_lines[a - 1:b])
            n_mark += 1
        else:
            out.append(line)
    text = '\n'.join(out) + '\n'
    for old, new in SUBS:
        n = text.count(old)
        if n != 1:
            raise SystemExit(f'substitution source occurs {n} times: {old[:60]}')
        text = text.replace(old, new)
    return text, n_mark


def main():
    bk, src, dst = sys.argv[1:4]
    src_lines = open(src, encoding='utf-8').read().split('\n')
    text, n_mark = rebuild(open(bk, encoding='utf-8').read(), src_lines)
    open(dst, 'w', encoding='utf-8').write(text)
    h = hashlib.sha256(text.encode('utf-8')).hexdigest()
    print(f'markers expanded: {n_mark}; rebuilt {len(text)} characters, {text.count(chr(10))} lines')
    print('sha256(rebuilt) =', h)
    if len(sys.argv) > 4:
        exp = open(sys.argv[4], encoding='utf-8').read()
        he = hashlib.sha256(exp.encode('utf-8')).hexdigest()
        print('sha256(expected)=', he)
        print('IDENTICAL' if exp == text else 'DIFFERENT')
        print('ALL PASS' if exp == text else 'SOME CHECK FAILED')


if __name__ == '__main__':
    main()
