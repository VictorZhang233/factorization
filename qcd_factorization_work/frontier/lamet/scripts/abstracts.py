#!/usr/bin/env python3
"""Print INSPIRE abstracts for given arXiv ids.  Usage: python3 -I abstracts.py id1 id2 ..."""
import sys, json, urllib.request, urllib.parse, time

for aid in sys.argv[1:]:
    q = urllib.parse.urlencode({"q": "arxiv:" + aid, "fields": "titles,abstracts,authors.full_name"})
    with urllib.request.urlopen("https://inspirehep.net/api/literature?" + q, timeout=60) as r:
        d = json.load(r)
    if d["hits"]["total"] != 1:
        print("!!", aid, d["hits"]["total"]); continue
    m = d["hits"]["hits"][0]["metadata"]
    au = ", ".join(a["full_name"] for a in m.get("authors", [])[:6])
    print("=== %s | %s | %s" % (aid, m["titles"][0]["title"], au))
    for ab in m.get("abstracts", [])[:1]:
        print(ab.get("value", ""))
    print()
    time.sleep(0.3)
