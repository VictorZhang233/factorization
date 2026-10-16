#!/bin/sh
# Re-runs the bibliographic / literature checks of batch A01-A11 (stage 1). Network access to inspirehep.net needed.
# Usage: sh run_checks.sh <scratch_dir>   (downloads go to <scratch_dir>, logs next to this script)
S="$(cd "$(dirname "$0")" && pwd)"; T="${1:-/tmp/a01_checks}"; mkdir -p "$T"
L="$S/run_checks.log"; : > "$L"
q(){ python3 -I "$S/inspire_search.py" "$1" "${2:-10}" "${3:-mostrecent}" >> "$L" 2>&1; echo >> "$L"; sleep 1; }
b(){ python3 -I "$S/inspire_before.py" "$1" "$2" "${3:-1000}" >> "$L" 2>&1; echo >> "$L"; sleep 1; }
echo "== A01 author lists" >> "$L"
for id in 2008.03886 2004.03543 1911.03840 1910.11415; do q "arxiv:$id" 2; done
echo "== A02 BAI vs name search" >> "$L"
curl -s -m 60 -G "https://inspirehep.net/api/literature" --data-urlencode 'q=a Y.Liu.90' --data-urlencode size=200 --data-urlencode "fields=titles,authors.full_name,authors.ids,arxiv_eprints,texkeys,earliest_date,authors.affiliations" -o "$T/bai.json"
curl -s -m 60 -G "https://inspirehep.net/api/literature" --data-urlencode 'q=a "Liu, Yizhuang"' --data-urlencode size=200 --data-urlencode "fields=titles,authors.full_name,authors.ids,arxiv_eprints,texkeys,earliest_date" -o "$T/name.json"
python3 -I "$S/a02_inspire_counts.py" "$T/bai.json" "$T/name.json" >> "$L" 2>&1
echo "== A03 priority" >> "$L"
q "arxiv:2003.06063" 2; q "arxiv:2005.14572" 2; q "arxiv:2102.01101" 2; q "texkey:Beneke:1998eq" 2
b 'fulltext:"soft function" and fulltext:"lattice QCD" and fulltext:"form factor"' 2019-10-25
echo "== A06 absence searches" >> "$L"
b '(t "three-loop" or t "three loop" or t N3LO or t "next-to-next-to-next-to-leading") and (t quasi or t pseudo or t "Ioffe" or t "lattice" or t "LaMET" or t "large momentum")' 2026-10-11
q "arxiv:2410.05141" 2
q 'a Rothstein, Ira Z. and a Stewart, Iain W. and date > 2015' 10
b 't Glauber and (t quasi or t lattice or t Euclidean or t "large-momentum" or t "large momentum" or t staple)' 2026-10-11
b '(t "operator product expansion" or t OPE) and (t "Wilson line" or t "Wilson-line" or t nonlocal or t non-local or t quasi or t "gauge link" or t "light-ray") and date > 2010' 2026-10-11
b '(t "flow equation" or t "flow equations" or t Polchinski) and (t renormalization or t "operator product") and (t QCD or t fermion or t fermions or t Yang-Mills or t "gauge theory" or t QED)' 2026-10-11
b 't BRST and (t nonlocal or t non-local or t "light-ray" or t bilocal or t "gauge variant" or t "gauge-variant")' 2026-10-11
b 't "spin asymmetries" and t factorization and date > 2000' 2026-10-11
q 'a Testa, Massimo and a Rossi, Giancarlo' 10
echo "== A06/A08 preprint status (INSPIRE publication_info)" >> "$L"
for id in 2007.04085 1603.08012 2608.25502 2211.13209 2512.11647 2011.10368; do q "arxiv:$id" 1; done
echo "== A09/A10 records" >> "$L"
for k in Hollands:2007zg Hollands:2011gf Holland:2014pna Frob:2015uqy Anikin:1978tj Smirnov:1990rz Gardi:2022khw Gardi:2024axt Becher:2024kmk; do q "texkey:$k" 1; done
echo done >> "$L"
