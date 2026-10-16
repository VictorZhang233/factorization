import json,sys
# Derives the dependency edges of fig:intro-dependency: reads uses.json (written by parse_uses.py from
# spec_v2/FINAL_OUTLINE_v2.md), prints the transitive reduction among the displayed results. Run: python3 -I closure.py
E=json.load(open('uses.json',encoding='utf-8'))
sel=['thm:prelim-slavnov-taylor','prop:prelim-beta','thm:prelim-cutting-rules','prop:prelim-wilson-rules','thm:prelim-composite-renorm',
 'thm:ir-landau-momentum','prop:ir-power-counting','thm:ir-leading-regions','thm:sudakov-factorization',
 'thm:ee-R-finite','thm:dis-ope','thm:dis-moments','thm:dis-moments-np','thm:pdf-moments-local','thm:pdf-dglap',
 'lem:method-ward-multi','thm:method-subtraction','thm:appN-subtraction','prop:method-glauber-deformation','thm:appO-main','thm:method-template',
 'thm:disall-factorization','thm:coll-sia','thm:dy-factorization','thm:tmd-factorization','thm:scet-thrust',
 'thm:break-tmd','prop:break-spacelike','conj:dy-coloured-final',
 'thm:lattice-lamet','thm:lamet-quasi-tmd','thm:yzliu-time-ordering','thm:front-collins-pinch']
asm=['asm:intro-bridge','asm:intro-np-ope','asm:appN-collins','asm:appO-mixing','asm:appO-deformation','asm:appO-rewritten-cs']
def reach(x,seen=None):
    if seen is None: seen=set()
    for u in E.get(x,{}).get('uses',[]):
        if u not in seen:
            seen.add(u); reach(u,seen)
    return seen
R={x:reach(x) for x in sel}
# selected deps
D={x:[y for y in sel if y in R[x] and y!=x] for x in sel}
# transitive reduction
red={}
for x in sel:
    ys=set(D[x])
    keep=[y for y in ys if not any(y in D[z] for z in ys if z!=y)]
    red[x]=sorted(keep,key=sel.index)
for x in sel:
    print(x,'<-',red[x])
print()
for a in asm:
    direct=[x for x in sel if a in E.get(x,{}).get('uses',[])]
    trans=[x for x in sel if a in R[x]]
    print(a,'direct:',direct)
    print('   trans:',[t for t in trans if t not in direct])
# check cycles
