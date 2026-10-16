#!/usr/bin/env python3
"""Build lamet.bib from the citations in LAMET.md.
 - citation keys: INSPIRE texkeys inside [...] in LAMET.md
 - sources: inspire/raw/*.bib, inspire/raw_texkey/*.bib (already fetched from INSPIRE), else fetched now from
   https://inspirehep.net/api/literature?q=texkey:KEY&format=bibtex  (saved to inspire/raw_texkey/KEY.bib)
 - a key is accepted only if the BibTeX entry returned by INSPIRE carries exactly that key (primary texkey)
Usage: python3 -I scripts/build_bib.py LAMET.md lamet.bib
"""
import sys, os, re, glob, time, urllib.request, urllib.parse

KEYRE = re.compile(r"^[A-Za-z][A-Za-z\-'\.]*:\d{4}[a-z]{2,3}$")
ENTRYRE = re.compile(r"@(\w+)\{([^,\s]+),", re.M)

def cited_keys(md):
    txt = open(md, encoding="utf-8").read()
    keys = []
    for grp in re.findall(r"\[([^\[\]]+)\]", txt):
        for k in grp.split(","):
            k = k.strip()
            if KEYRE.match(k) and k not in keys:
                keys.append(k)
    return keys

def split_entries(text):
    out = {}
    pos = [m.start() for m in ENTRYRE.finditer(text)] + [len(text)]
    for a, b in zip(pos[:-1], pos[1:]):
        chunk = text[a:b].strip()
        m = ENTRYRE.match(chunk)
        if m:
            out[m.group(2)] = chunk
    return out

def local_entries(base):
    ent = {}
    for f in glob.glob(os.path.join(base, "inspire", "raw", "*.bib")) + glob.glob(os.path.join(base, "inspire", "raw_texkey", "*.bib")):
        ent.update(split_entries(open(f, encoding="utf-8").read()))
    return ent

def fetch(key, base):
    url = "https://inspirehep.net/api/literature?" + urllib.parse.urlencode({"q": "texkey:" + key, "format": "bibtex", "size": "3"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                txt = r.read().decode("utf-8")
            break
        except Exception as e:
            err = e; time.sleep(2 + 3 * attempt)
    else:
        raise err
    ents = split_entries(txt)
    fn = os.path.join(base, "inspire", "raw_texkey", key.replace(":", "_").replace("/", "_") + ".bib")
    if ents:
        open(fn, "w", encoding="utf-8").write(txt)
    return ents

def main(md, outbib):
    base = os.path.dirname(os.path.abspath(md))
    keys = cited_keys(md)
    ent = local_entries(base)
    found, problems = {}, []
    for k in keys:
        if k in ent:
            found[k] = ent[k]; continue
        got = fetch(k, base); time.sleep(0.4)
        if k in got:
            found[k] = got[k]; print("fetched", k)
        elif got:
            problems.append("%s -> INSPIRE primary key(s) %s" % (k, ", ".join(got)))
        else:
            problems.append("%s -> not found in INSPIRE" % k)
    with open(outbib, "w", encoding="utf-8") as f:
        f.write("%% lamet.bib -- BibTeX for frontier/lamet/LAMET.md; every entry fetched from INSPIRE-HEP (keys = INSPIRE texkeys).\n")
        f.write("%% %d cited keys, %d entries.\n\n" % (len(keys), len(found)))
        for k in sorted(found, key=str.lower):
            f.write(found[k].rstrip() + "\n\n")
    print("cited keys: %d ; entries written: %d" % (len(keys), len(found)))
    for p in problems:
        print("PROBLEM:", p)
    return 0 if not problems else 1

if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
