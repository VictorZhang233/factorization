#!/bin/zsh
q() {
  local label="$1"; local query="$2"
  local res=$(curl -s -m 25 -G "https://inspirehep.net/api/literature" --data-urlencode "q=$query" --data-urlencode "fields=titles.title,authors.full_name,publication_info.journal_title,publication_info.journal_volume,publication_info.page_start,publication_info.artid,publication_info.year" --data-urlencode "size=1")
  echo "=== $label :: $query"
  echo "$res" | python3 -I -c 'import sys,json
d=json.load(sys.stdin)
for h in d["hits"]["hits"][:1]:
    m=h["metadata"]; t=m["titles"][0]["title"]; a=[x["full_name"] for x in m.get("authors",[])][:5]
    p=m.get("publication_info",[{}])
    print("   ", t, "|", "; ".join(a), "|", [(x.get("journal_title"),x.get("journal_volume"),x.get("page_start") or x.get("artid"),x.get("year")) for x in p])'
}
q ChayKim "arxiv:hep-ph/0301262"
q BBK1998 "arxiv:hep-ph/9809287"
q KMQS2014 "arxiv:1401.0923"
q FLMR2012 "arxiv:1207.2578"
q CKKL2005 "arxiv:hep-ph/0412110"
q Abbate2011 "arxiv:1006.3080"
q BNSS2023 "arxiv:2307.06359"
q FeigeSchwartz "arxiv:1403.6472"
q GHMMS "arxiv:2408.03019"
q Zeng2015 "arxiv:1507.01652"
