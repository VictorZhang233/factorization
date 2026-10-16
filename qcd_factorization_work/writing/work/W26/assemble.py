# Assemble chapters/ch23_yzliu.tex from parts/p*.tex, replacing '%%FIG <label>' lines by the verbatim
# figure blocks of writing/packs/W26/figblocks.tex (LA-10).
import os, re, glob
W = "/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work"
fb = open(os.path.join(W, "writing/packs/W26/figblocks.tex"), encoding="utf-8").read()
blocks = {}
for m in re.finditer(r"%%% BEGIN (fig:[\w-]+)\n(.*?)%%% END \1", fb, re.S):
    blocks[m.group(1)] = "%%% BEGIN " + m.group(1) + "\n" + m.group(2) + "%%% END " + m.group(1)
out = ["% ch23_yzliu.tex -- Chapter 23: Yizhuang Liu 的严格因子化研究 (writer W26).\n",
       "% Assembled from writing/work/W26/parts/p*.tex by writing/work/W26/assemble.py; figure blocks copied verbatim\n",
       "% from writing/packs/W26/figblocks.tex (LA-10).\n"]
used = []
for f in sorted(glob.glob(os.path.join(W, "writing/work/W26/parts/p*.tex"))):
    for line in open(f, encoding="utf-8"):
        m = re.match(r"^%%FIG (fig:[\w-]+)\s*$", line)
        if m:
            out.append(blocks[m.group(1)] + "\n"); used.append(m.group(1))
        else:
            out.append(line)
    out.append("\n")
open(os.path.join(W, "chapters/ch23_yzliu.tex"), "w", encoding="utf-8").write("".join(out))
print("figures inserted:", used, "; available:", sorted(blocks))
