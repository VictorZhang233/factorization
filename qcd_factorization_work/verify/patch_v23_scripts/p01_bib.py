TARGET = 'refs_merged_v2.bib'
PART10 = open('/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/spec_v2/checks/refs_part10_v23.bib', encoding='utf-8').read().rstrip('\n') + '\n'
OPS = [
 ('rep', "% verify/ bibliographies merged: none (verify/ did not exist at build time)\n",
  "% verify/ bibliographies merged: none (verify/ did not exist at build time)\n"
  "% spec v2.3 (verify patch, 2026-10-11): PART 10 = 48 new entries -- 45 INSPIRE-HEP records fetched by\n"
  "%   spec_v2/checks/fetch_additions_v23.py (one record per query; log fetch_additions_v23.log) and 3 Crossref-verified\n"
  "%   manual entries (Hormander2003, Vladimirov2002, NilssonPassare2013); block built by checks/add_refs_v23.py.\n"
  "%\n"
  "% CHANGELOG\n"
  "% v2.3 (2026-10-11, spec patcher, verify patch): added PART 10 (48 entries; total 1051).  Task items: Gribov:1977wm;\n"
  "%   Lee:1972fj, Lee:1972ocr, Lee:1972yfa (Lee-Zinn-Justin I-III); Zinn-Justin:1974ggz; Appelquist:1974tg; Vladimirov2002\n"
  "%   (the Mir 1979 monograph is on neither INSPIRE nor Crossref; the Crossref-verified 2002 monograph is cited instead,\n"
  "%   with the location still to be checked); Hormander2003; Bergere:1977wz; Balaban:1985yy, Balaban:1989ay (CMP 116 (1988) 1\n"
  "%   not found on INSPIRE: not added); Magnen:1992wv; Schoonderwoerd:1998qj, Schoonderwoerd:1998iy; Chou:2022drv;\n"
  "%   Becher:2026kbr; Nakanishi:1990qm (publisher/series completed from the INSPIRE series field).  Joglekar 1977 = the\n"
  "%   existing keys Joglekar:1976eb, Joglekar:1976pe (INSPIRE re-check, no addition).  Citations of the patched text:\n"
  "%   Meggiolaro:1996hf, Giordano:2006vv, Cheng:2024wyu, Radyushkin:2018nbf, Lindsay:1983ny, Lindsay:1983dt,\n"
  "%   Belitsky:2025bez, Belitsky:2024yag, Jackiw:1980kv, Borinsky:2020rqs, Schultka:2018nrs, Larin:1996wd, Braun:2019qtp,\n"
  "%   Barcaro:2026dsd, Zhou:2017his, Liu:2008cc, Scimemi:2016ffw, Moos:2020wvd, Arkani-Hamed:2022cqe, Henneaux:1995ex,\n"
  "%   Barnich:1999cy, Herrlich:1994kh, Chang:2013pba, Li:2022fvk, Boer:2017hqr, Aybat:2011ge, Bhattacharya:2019cme,\n"
  "%   Monahan:2026skv, Buffing:2011mj, Balitsky:2009xg, NilssonPassare2013.\n"
  "%   Dropped (not verifiable on INSPIRE/Crossref): Feichtner-Sturmfels (math/0411260; the citing text now cites\n"
  "%   Schultka:2018nrs instead).  bibtex \\nocite{*} test: REFS_NOTES_v2 Sec. 6 (v2.3 entry) and checks/bibtest/SUMMARY.txt.\n"),
 ('rep', "  inspire       = {Zweig:1964jf}\n}\n",
  "  inspire       = {Zweig:1964jf}\n}\n\n" + PART10),
]
