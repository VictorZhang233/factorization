#!/usr/bin/env python3
"""INSPIRE search helper.  Usage: python3 -I isearch.py "query" [size] [sort]
Prints: arXiv | title | authors | journal vol artid year | citations | texkey | recid
"""
import sys, json, urllib.request, urllib.parse

def search(q, size=25, sort="mostcited"):
    params = {"q": q, "size": str(size), "sort": sort,
              "fields": "titles,authors.full_name,publication_info,arxiv_eprints,texkeys,citation_count,dois,control_number"}
    url = "https://inspirehep.net/api/literature?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=60) as r:
        d = json.load(r)
    return d

def fmt(h):
    m = h["metadata"]
    t = m["titles"][0]["title"]
    au = m.get("authors", [])
    a = ", ".join(x["full_name"] for x in au[:6]) + (" et al.(%d)" % len(au) if len(au) > 6 else "")
    ar = (m.get("arxiv_eprints") or [{}])[0].get("value", "")
    pis = [p for p in m.get("publication_info", []) if p.get("journal_title")]
    pub = "; ".join("%s %s %s %s" % (p.get("journal_title", ""), p.get("journal_volume", ""),
                                     p.get("artid", p.get("page_start", "")), p.get("year", "")) for p in pis)
    doi = (m.get("dois") or [{}])[0].get("value", "")
    return "%s | %s | %s | %s | doi:%s | cit %s | %s | recid %s" % (
        ar, t, a, pub, doi, m.get("citation_count"), (m.get("texkeys") or [""])[0], m.get("control_number"))

if __name__ == "__main__":
    q = sys.argv[1]
    size = int(sys.argv[2]) if len(sys.argv) > 2 else 25
    sort = sys.argv[3] if len(sys.argv) > 3 else "mostcited"
    d = search(q, size, sort)
    print("TOTAL", d["hits"]["total"], "for", q)
    for h in d["hits"]["hits"]:
        print(fmt(h))
