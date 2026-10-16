#!/usr/bin/env python3
"""Fetch INSPIRE metadata + BibTeX for a list of arXiv ids.
Usage: python3 -I fetch_refs.py ids.txt outdir
ids.txt: one arXiv id per line (comments after '#').
Writes outdir/<id>.json, outdir/<id>.bib and prints a verification table.
"""
import sys, os, json, time, urllib.request, urllib.parse

FIELDS = "titles,authors.full_name,publication_info,arxiv_eprints,texkeys,citation_count,dois,control_number,document_type"

def get(url):
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return r.read().decode("utf-8")
        except Exception as e:
            time.sleep(2 + 3 * attempt)
            err = e
    raise err

def main(idfile, outdir):
    os.makedirs(outdir, exist_ok=True)
    ids = []
    for line in open(idfile):
        s = line.split("#")[0].strip()
        if s:
            ids.append(s)
    for aid in ids:
        fn = os.path.join(outdir, aid.replace("/", "_"))
        if not os.path.exists(fn + ".json"):
            q = urllib.parse.urlencode({"q": "arxiv:" + aid, "fields": FIELDS})
            js = get("https://inspirehep.net/api/literature?" + q)
            open(fn + ".json", "w").write(js)
            time.sleep(0.4)
        d = json.load(open(fn + ".json"))
        n = d["hits"]["total"]
        if n != 1:
            print("!! %s: %d hits" % (aid, n))
            continue
        h = d["hits"]["hits"][0]
        m = h["metadata"]
        recid = m["control_number"]
        if not os.path.exists(fn + ".bib"):
            bib = get("https://inspirehep.net/api/literature/%s?format=bibtex" % recid)
            open(fn + ".bib", "w").write(bib)
            time.sleep(0.4)
        t = m["titles"][0]["title"]
        au = m.get("authors", [])
        a = ", ".join(x["full_name"] for x in au[:8]) + (" et al.(%d)" % len(au) if len(au) > 8 else "")
        pis = [p for p in m.get("publication_info", []) if p.get("journal_title")]
        pub = "; ".join("%s %s %s (%s)" % (p.get("journal_title", ""), p.get("journal_volume", ""),
                                            p.get("artid", p.get("page_start", "")), p.get("year", "")) for p in pis)
        doi = (m.get("dois") or [{}])[0].get("value", "")
        print("%s | %s | %s | %s | %s | doi:%s | recid %s | cit %s" % (
            aid, (m.get("texkeys") or [""])[0], t, a, pub or "(unpublished)", doi, recid, m.get("citation_count")))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
