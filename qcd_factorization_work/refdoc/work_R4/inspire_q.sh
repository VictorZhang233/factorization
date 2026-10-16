#!/bin/zsh
q() {
  local label="$1"; local query="$2"
  local res=$(curl -s -m 25 -G "https://inspirehep.net/api/literature" --data-urlencode "q=$query" --data-urlencode "fields=titles.title,authors.full_name,publication_info.journal_title,publication_info.journal_volume,publication_info.page_start,publication_info.year" --data-urlencode "size=2")
  echo "=== $label :: $query"
  echo "$res" | python3 -I -c 'import sys,json
d=json.load(sys.stdin)
for h in d["hits"]["hits"][:2]:
    m=h["metadata"]; t=m["titles"][0]["title"]; a=[x["full_name"] for x in m.get("authors",[])][:5]
    p=m.get("publication_info",[{}])
    print("   ", t, "|", "; ".join(a), "|", [(x.get("journal_title"),x.get("journal_volume"),x.get("page_start"),x.get("year")) for x in p])
print("   total:", d["hits"]["total"])'
}
q 46 "j Nucl.Phys.B,592,3"
q 82 "j Commun.Math.Phys.,24,1"
q 84 "j Commun.Math.Phys.,39,1"
q 87 "j Phys.Lett.B,119,407"
q 93 "j Commun.Math.Phys.,53,155"
q 94 "j Phys.Rev.D,86,105043"
q 95 "j J.Math.Phys.,46,082304"
q 97a "j Commun.Math.Phys.,31,83"
q 97b "j Commun.Math.Phys.,42,281"
q 100 "j Commun.Math.Phys.,109,249"
q 101 "j Commun.Math.Phys.,155,325"
q 102 "j Commun.Math.Phys.,102,1"
q 103 "j Commun.Math.Phys.,103,67"
q 110 "j Phys.Rept.,338,439"
q 119 "j Commun.Math.Phys.,18,227"
q 120 "j Phys.Rev.D,2,1541"
q 121 "j Commun.Math.Phys.,293,85"
q 122 "j Commun.Math.Phys.,62,137"
q 123 "j Phys.Lett.B,114,340"
q 124 "j Phys.Lett.B,144,419"
q 131 "j Phys.Rev.D,1,2901"
q 132 "j Phys.Rept.,301,299"
q 130 "j Phys.Rev.D,87,034018"
