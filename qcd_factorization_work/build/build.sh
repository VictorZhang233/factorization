#!/bin/bash
# build.sh -- full build of 《QCD 因子化定理：严格证明、全阶论证与适用边界》 (integration tooling, writing/tools/).
#
#   build/build.sh [--chapters DIR] [--builddir DIR] [--outline FILE] [--register FILE] [--bib FILE]
#                  [--figroot DIR] [--level auto|0|1|2|3] [--budget PAGES] [--final] [--no-normalize-refs]
#
# Defaults: chapters/ of the work directory, build directory = the directory of this script, spec_v2 files,
# figure sources (figures/FIGURES_STATUS.md, figures/figset_*.tex, research/tikz*/figures*.tex) under --figroot = work dir.
# Sequence (FINAL_OUTLINE_v2 App P §P.7 "Build sequence"):
#   1 copy preamble_fact.tex; figsync.py --apply: copy of the unit files into <builddir>/src with the figure blocks
#     re-synchronised from the figure sources (LA-10) and, unless --no-normalize-refs, label lists without spaces
#     (chapters/ itself is never written)
#   2 bibmerge.py: refs_merged_v2.bib + chapters/*.bib-additions -> refs_final.bib (bibtex-validated, LA-14)
#   3 make_master.py -> qcd_factorization.tex (units that do not exist are skipped)
#   4 blueprint_gen.py --stub; xelatex; bibtex
#   5 blueprint_gen.py with the .aux at the lowest compaction level whose App P fits the budget (measured by
#     measure_appP.py on a standalone App P document), xelatex x2; re-check the App P page count in the .aux and
#     raise the level (two more passes) while it exceeds the budget
#   6 logsummary.py -> build_summary.txt (errors, undefined references/citations by unit, multiply defined labels,
#     overfull boxes > 1pt, missing characters, page counts of the book, App P and App Q)
# Exit status: non-zero if the final log contains LaTeX errors.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
W="$(cd "$HERE/.." && pwd)"
TOOLS="$W/writing/tools"
CHAPTERS="$W/chapters"
BUILD="$HERE"
OUTLINE="$W/spec_v2/FINAL_OUTLINE_v2.md"
REGISTER="$W/spec_v2/ASSUMPTIONS.md"
BIB="$W/spec_v2/refs_merged_v2.bib"
ALIASES="$W/spec_v2/key_aliases_v2.tsv"
FIGROOT="$W"
LEVEL=auto
BUDGET=10
FINAL=""
NORM="--normalize-refs"
JOB=qcd_factorization
while [ $# -gt 0 ]; do
  case "$1" in
    --chapters) CHAPTERS="$(cd "$2" && pwd)"; shift 2;;
    --builddir) mkdir -p "$2"; BUILD="$(cd "$2" && pwd)"; shift 2;;
    --outline) OUTLINE="$(cd "$(dirname "$2")" && pwd)/$(basename "$2")"; shift 2;;
    --register) REGISTER="$(cd "$(dirname "$2")" && pwd)/$(basename "$2")"; shift 2;;
    --bib) BIB="$(cd "$(dirname "$2")" && pwd)/$(basename "$2")"; shift 2;;
    --figroot) FIGROOT="$(cd "$2" && pwd)"; shift 2;;
    --level) LEVEL="$2"; shift 2;;
    --budget) BUDGET="$2"; shift 2;;
    --final) FINAL="--final"; shift;;
    --no-normalize-refs) NORM=""; shift;;
    -h|--help) sed -n '2,24p' "$0"; exit 0;;
    *) echo "build.sh: unknown option $1" >&2; exit 2;;
  esac
done
export max_print_line=100000 error_line=254 half_error_line=238
PY="python3 -I"
T0=$(date +%s)
say() { printf '[build %4ds] %s\n' $(( $(date +%s) - T0 )) "$*"; }
xe() {   # one xelatex pass; returns xelatex's exit status
  xelatex -interaction=nonstopmode "$JOB.tex" > "xelatex_pass.out" 2>&1
  local rc=$?
  local np; np=$(grep -o 'Output written on [^ ]* ([0-9]* page' "$JOB.log" 2>/dev/null | grep -o '([0-9]*' | tr -d '(')
  local ne; ne=$(grep -c '^! ' "$JOB.log" 2>/dev/null)
  say "xelatex $1: exit $rc, ${np:-0} pages, ${ne:-0} errors"
  return $rc
}
appP_pages() {   # App P page count from the aux (page(app:appQ)-page(app:appP), else page(appP:end)-page(app:appP)+1)
  $PY - "$JOB.aux" <<'EOF'
import sys, re
t = open(sys.argv[1], encoding='utf-8', errors='replace').read()
def pg(l):
    m = re.search(r'\\newlabel\{' + re.escape(l) + r'\}\{\{[^{}]*\}\{(\d+)\}', t)
    return int(m.group(1)) if m else None
p, q, e = pg('app:appP'), pg('app:appQ'), pg('appP:end')
print(q - p if (p is not None and q is not None) else (e - p + 1 if (p is not None and e is not None) else -1))
EOF
}

mkdir -p "$BUILD"
cd "$BUILD" || exit 2
say "work dir: $W"
say "chapters: $CHAPTERS -> build dir: $BUILD"
cp "$W/common/preamble_fact.tex" . || exit 2

# 1 figure re-sync into the copy
$PY "$TOOLS/figsync.py" --chapters "$CHAPTERS" --root "$FIGROOT" --apply --out src $NORM --report figsync_report.txt > /dev/null
say "figsync: $(sed -n 2p figsync_report.txt)"

# 2 bibliography
$PY "$TOOLS/bibmerge.py" --base "$BIB" --additions "$CHAPTERS" --aliases "$ALIASES" --out refs_final.bib \
    --report bibmerge_report.txt > /dev/null
BIBRC=$?
say "bibmerge: $(sed -n 2p bibmerge_report.txt); $(grep '^bibtex test' bibmerge_report.txt)"

# 3 master driver
$PY "$TOOLS/make_master.py" --src src --out "$JOB.tex" | sed 's/^/           /'

# 4 first pass with App P placeholders
$PY "$TOOLS/blueprint_gen.py" --root . --master "$JOB.tex" --outline "$OUTLINE" --register "$REGISTER" --out appP --stub $FINAL \
    | sed 's/^/           /'
rm -f "$JOB.aux"
xe "pass 1 (App P placeholders)"
bibtex "$JOB" > bibtex.out 2>&1
say "bibtex: $(grep -c 'Warning--' "$JOB.blg" 2>/dev/null) warnings; $(grep -o '(There w[a-z]* [0-9]* error[a-z]*' "$JOB.blg" | head -1)"

# 5 generated App P at the lowest level that fits the budget
gen() {
  $PY "$TOOLS/blueprint_gen.py" --root . --master "$JOB.tex" --aux "$JOB.aux" --outline "$OUTLINE" --register "$REGISTER" \
      --out appP --level "$1" $FINAL | sed 's/^/           /'
}
if [ "$LEVEL" = "auto" ]; then
  L=0
  while : ; do
    gen $L > /dev/null
    P=$($PY "$TOOLS/measure_appP.py" --build . --appP appP --aux "$JOB.aux" --src src --work measure_appP | sed -n 's/^APPP_PAGES //p')
    say "App P at level $L (standalone measurement): ${P:-n/a} pages (budget $BUDGET)"
    if [ "$L" -ge 3 ] || { [ -n "$P" ] && [ "$P" != "n/a" ] && [ "$P" -le "$BUDGET" ]; }; then break; fi
    L=$((L + 1))
  done
else
  L=$LEVEL
fi
gen $L
xe "pass 2 (App P level $L)"
xe "pass 3"
P=$(appP_pages)
say "App P in the book: $P pages at level $L"
while [ "$LEVEL" = "auto" ] && [ "$P" -gt "$BUDGET" ] && [ "$L" -lt 3 ]; do
  L=$((L + 1))
  say "App P exceeds the budget: level $L"
  gen $L
  xe "pass (level $L)"
  xe "pass (level $L, references)"
  P=$(appP_pages)
  say "App P in the book: $P pages at level $L"
done
if grep -q 'Rerun to get\|Label(s) may have changed' "$JOB.log"; then xe "pass (labels changed)"; fi
[ "$P" -gt "$BUDGET" ] && say "NOTE: App P ($P pp.) exceeds the budget of $BUDGET pp. even at level $L (FINAL_OUTLINE_v2 App P §P.7: the lead author decides)"

# 6 summary
$PY "$TOOLS/logsummary.py" --log "$JOB.log" --aux "$JOB.aux" --src src --outline "$OUTLINE" --register "$REGISTER" \
    --out build_summary.txt > /dev/null
RC=$?
{
  echo "== tool reports"
  echo "figsync:      $(sed -n 2p figsync_report.txt)  (figsync_report.txt)"
  echo "bibmerge:     $(sed -n 2p bibmerge_report.txt)  (bibmerge_report.txt)"
  echo "              $(grep '^bibtex test' bibmerge_report.txt)"
  echo "blueprint:    level $L; $(grep '^findings' appP/appP_report.txt)  (appP/appP_report.txt)"
} >> build_summary.txt
cat build_summary.txt
say "done: $BUILD/$JOB.pdf  (summary: build_summary.txt)"
exit $RC
