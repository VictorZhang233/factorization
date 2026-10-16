import re,sys,json
# Parses the statement entries of spec_v2/FINAL_OUTLINE_v2.md and their \uses lists into uses.json (cwd).

src='/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/spec_v2/FINAL_OUTLINE_v2.md'
lines=open(src,encoding='utf-8').read().split('\n')
start=re.compile(r'^\s*[\*\-] \*\*(?:\[PENDING-VERIFY[^\]]*\] )?(定理|引理|命题|推论|猜想|定义|假设|例|注)\s*`([a-z]+:[A-Za-z0-9\-]+)`')
entries={};cur=None;order=[]
for i,l in enumerate(lines):
    m=start.match(l)
    if m:
        cur=m.group(2)
        if cur not in entries:
            entries[cur]={'type':m.group(1),'head':l[:300],'uses':set(),'line':i+1}
            order.append(cur)
        # inline tag
        continue_flag=True
    elif l.startswith('#') or (l.startswith('* **') or l.startswith('- **')):
        cur=None
    if cur:
        for u in re.findall(r'\\uses\{([^}]*)\}',l):
            for x in u.split(','):
                x=x.strip()
                if x: entries[cur]['uses'].add(x)
json.dump({k:{'type':v['type'],'head':v['head'],'uses':sorted(v['uses']),'line':v['line']} for k,v in entries.items()},open('uses.json','w'),ensure_ascii=False,indent=0)
print(len(entries),'entries')
for k in sys.argv[1:]:
    e=entries.get(k)
    print('==',k, e['line'] if e else None, sorted(e['uses']) if e else 'MISSING')
