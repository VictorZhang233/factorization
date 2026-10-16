#!/usr/bin/env python3
r"""bibmerge.py -- merge the bibliography of the spec with the writers' additions (LEAD_DECISIONS LA-14).

    python3 -I bibmerge.py --base spec_v2/refs_merged_v2.bib --additions chapters --out build/refs_final.bib
            [--aliases spec_v2/key_aliases_v2.tsv] [--report build/bibmerge_report.txt] [--no-test]

Reads the base file and every chapters/*.bib-additions file (sorted by name).  Entries are deduplicated by key
(BibTeX compares keys case-insensitively): an addition identical to an entry already present (same fields after
normalising whitespace and outer braces/quotes) is dropped silently; a conflicting duplicate keeps the first entry
(the base wins; among additions the first file in name order) and is reported with the differing fields.  Also
reported: addition keys that are aliases of a base key in key_aliases_v2.tsv (the unit should cite the merged key),
the same DOI or arXiv eprint under different keys, unparsable entries.  The merged file keeps every entry verbatim
(base order, then the additions in file order).  Validation: a bibtex run on the merged file with \citation{*} and
style unsrt; its error and warning counts are reported (exit code 1 if bibtex reports errors).
"""
import os, re, sys, glob, shutil, argparse, subprocess, tempfile, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import booklib as B


def parse_bib(text, fname):
    """[(kind, key, raw, fields)] in file order; kind = entry | string | preamble; problems as a list."""
    out, probs = [], []
    i, n = 0, len(text)
    while True:
        m = re.compile(r'@\s*([A-Za-z]+)\s*([{(])').search(text, i)
        if not m:
            break
        typ = m.group(1).lower()
        open_c = m.group(2)
        close_c = '}' if open_c == '{' else ')'
        line = text.count('\n', 0, m.start()) + 1
        # inside a comment line?
        ls = text.rfind('\n', 0, m.start()) + 1
        if '%' in text[ls:m.start()]:
            i = m.end()
            continue
        if typ == 'comment':
            e = B.match_brace(text, m.end() - 1, open_c, close_c)
            i = (e + 1) if e > 0 else m.end()
            continue
        e = B.match_brace(text, m.end() - 1, open_c, close_c)
        if e < 0:
            probs.append('%s:%d: @%s entry with unbalanced delimiters (rest of the file ignored)' % (fname, line, typ))
            break
        body = text[m.end():e]
        raw = text[m.start():e + 1]
        if typ in ('string', 'preamble'):
            key = body.split('=', 1)[0].strip().lower() if typ == 'string' else 'preamble%d' % line
            out.append((typ, key, raw, {}, line))
        else:
            k = body.split(',', 1)
            key = k[0].strip()
            if not key or len(k) < 2:
                probs.append('%s:%d: @%s entry without key or fields' % (fname, line, typ))
            else:
                out.append(('entry', key, raw, parse_fields(k[1]), line))
        i = e + 1
    return out, probs


def parse_fields(s):
    f = {}
    for part in B.split_top(s, ','):
        if '=' not in part:
            continue
        name, val = part.split('=', 1)
        name = name.strip().lower()
        v = val.strip()
        pieces = [x.strip() for x in B.split_top(v, '#')]
        norm = []
        for x in pieces:
            if len(x) >= 2 and ((x[0] == '{' and x[-1] == '}') or (x[0] == '"' and x[-1] == '"')):
                x = x[1:-1]
            norm.append(x)
        v = ' '.join(norm)
        v = re.sub(r'[{}]', '', v)
        v = re.sub(r'\s+', ' ', v).strip()
        if name:
            f[name] = v
    return f


def norm_doi(d):
    d = d.strip().lower()
    d = re.sub(r'^(https?://)?(dx\.)?doi\.org/', '', d)
    return d


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--base', required=True)
    ap.add_argument('--additions', required=True, help='directory with *.bib-additions files')
    ap.add_argument('--out', required=True)
    ap.add_argument('--aliases', default=None)
    ap.add_argument('--report', default=None)
    ap.add_argument('--no-test', action='store_true')
    a = ap.parse_args()
    rep = []
    base, probs = parse_bib(B.read_text(a.base), os.path.basename(a.base))
    adds = []
    afiles = sorted(glob.glob(os.path.join(a.additions, '*.bib-additions')))
    for p in afiles:
        e, pr = parse_bib(B.read_text(p), os.path.basename(p))
        adds.append((os.path.basename(p), e))
        probs += pr
    aliases = {}
    if a.aliases and os.path.exists(a.aliases):
        for line in B.read_text(a.aliases).split('\n')[1:]:
            c = line.split('\t')
            if len(c) >= 2 and c[0].strip():
                aliases.setdefault(c[0].strip().lower(), c[1].strip())
    keep = []                 # (raw, origin)
    seen = {}                 # lower key -> (key, fields, origin)
    strings = set()
    stats = collections.Counter()
    for (kind, key, raw, fields, line) in base:
        if kind == 'string':
            strings.add(key)
            keep.append(raw)
            continue
        if kind != 'entry':
            keep.append(raw)
            continue
        lk = key.lower()
        if lk in seen:
            rep.append('BASE-DUP  %s: repeated in the base file (line %d; first %s)' % (key, line, seen[lk][2]))
            stats['base_dup'] += 1
            continue
        seen[lk] = (key, fields, '%s:%d' % (os.path.basename(a.base), line))
        keep.append(raw)
        stats['base'] += 1
    base_keys = dict((k, v) for k, v in seen.items())
    for fname, entries in adds:
        nf = 0
        for (kind, key, raw, fields, line) in entries:
            origin = '%s:%d' % (fname, line)
            if kind == 'string':
                if key in strings:
                    continue
                strings.add(key)
                keep.append(raw)
                continue
            if kind != 'entry':
                continue
            lk = key.lower()
            if lk in seen:
                k0, f0, o0 = seen[lk]
                if f0 == fields:
                    rep.append('SAME      %-28s %s duplicates %s (identical; dropped)' % (key, origin, o0))
                    stats['same'] += 1
                else:
                    diff = sorted(set(f0) | set(fields))
                    diff = [x for x in diff if f0.get(x) != fields.get(x)]
                    rep.append('CONFLICT  %-28s %s vs %s: fields differ: %s (kept %s)' % (
                        key, origin, o0, ', '.join(diff), o0))
                    for x in diff[:6]:
                        rep.append('            %-10s kept: %s' % (x, (f0.get(x) or '-')[:100]))
                        rep.append('            %-10s new : %s' % ('', (fields.get(x) or '-')[:100]))
                    stats['conflict'] += 1
                if k0 != key:
                    rep.append('CASE      %-28s %s: key differs only in case from %s' % (key, origin, k0))
                continue
            if lk in aliases and aliases[lk].lower() in base_keys:
                rep.append('ALIAS     %-28s %s is an alias of the base key %s (key_aliases_v2.tsv): cite %s; entry '
                           'kept so that the citation resolves' % (key, origin, aliases[lk], aliases[lk]))
                stats['alias'] += 1
            seen[lk] = (key, fields, origin)
            keep.append(raw)
            stats['added'] += 1
            nf += 1
        rep.append('FILE      %-28s %d entr%s added' % (fname, nf, 'y' if nf == 1 else 'ies'))
    # DOI / eprint duplicates under different keys
    by_doi = collections.defaultdict(list)
    by_ep = collections.defaultdict(list)
    for lk, (key, f, o) in seen.items():
        if f.get('doi'):
            by_doi[norm_doi(f['doi'])].append((key, o))
        if f.get('eprint'):
            by_ep[f['eprint'].strip().lower()].append((key, o))
    for d, lst in sorted(by_doi.items()):
        if len(lst) > 1:
            rep.append('SAME-DOI  %s: %s' % (d, ', '.join('%s (%s)' % x for x in lst)))
            stats['samedoi'] += 1
    for d, lst in sorted(by_ep.items()):
        if len(lst) > 1:
            rep.append('SAME-EPR  %s: %s' % (d, ', '.join('%s (%s)' % x for x in lst)))
            stats['sameeprint'] += 1
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    with open(a.out, 'w', encoding='utf-8') as fh:
        fh.write('%% refs_final.bib -- generated by writing/tools/bibmerge.py from %s and %d *.bib-additions file(s); '
                 'do not edit\n\n' % (os.path.basename(a.base), len(afiles)))
        fh.write('\n\n'.join(x.strip() for x in keep) + '\n')
    head = ['bibmerge report -- base %s: %d entries; additions: %d file(s); merged: %d entries -> %s' % (
        os.path.basename(a.base), stats['base'], len(afiles), stats['base'] + stats['added'], a.out),
        'summary: added %d, identical duplicates dropped %d, conflicting duplicates %d, alias keys %d, same DOI under '
        'different keys %d, same eprint %d, unparsable %d' % (stats['added'], stats['same'], stats['conflict'],
                                                              stats['alias'], stats['samedoi'], stats['sameeprint'], len(probs))]
    rc = 0
    if not a.no_test:
        tmp = tempfile.mkdtemp(prefix='bibtest')
        try:
            shutil.copy(a.out, os.path.join(tmp, 'refs_final.bib'))
            with open(os.path.join(tmp, 'bibtest.aux'), 'w', encoding='utf-8') as fh:
                fh.write('\\relax\n\\citation{*}\n\\bibstyle{unsrt}\n\\bibdata{refs_final}\n')
            r = subprocess.run(['bibtex', 'bibtest'], cwd=tmp, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            outp = r.stdout.decode('utf-8', 'replace')
            blg = B.read_text(os.path.join(tmp, 'bibtest.blg')) if os.path.exists(os.path.join(tmp, 'bibtest.blg')) else outp
            nerr = 0
            m = re.search(r'\(There (?:were|was) (\d+) error', blg)
            if m:
                nerr = int(m.group(1))
            m = re.search(r'\(There (?:were|was) (\d+) warning', blg)
            nwarn = int(m.group(1)) if m else 0
            nbib = len(re.findall(r'\\bibitem', B.read_text(os.path.join(tmp, 'bibtest.bbl')))) if os.path.exists(
                os.path.join(tmp, 'bibtest.bbl')) else 0
            head.append('bibtex test (\\citation{*}, unsrt): exit %d, %d error(s), %d warning(s), %d \\bibitem' % (
                r.returncode, nerr, nwarn, nbib))
            for line in blg.split('\n'):
                if re.match(r'^(Warning--|I was expecting|Repeated entry|I\'m skipping|You\'re missing|Illegal)', line):
                    rep.append('BIBTEX    ' + line.strip())
            rc = 1 if nerr else 0
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    out = head + rep + (['-- parse problems'] + ['  ' + x for x in probs] if probs else [])
    txt = '\n'.join(out) + '\n'
    if a.report:
        with open(a.report, 'w', encoding='utf-8') as fh:
            fh.write(txt)
    sys.stdout.write(txt)
    sys.exit(rc)


if __name__ == '__main__':
    main()
