import json,re,html,subprocess,time,sys
d=json.load(open('fr.json',encoding='utf-8'))
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/126 Safari/537.36"
def txt(s): return html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',s))).strip()
def words(s): return len(txt(s).split())
allinks=set()
for h,c in d.items():
    g=c['guide']
    print(f"== {h}\n  description {words(c['description_html'])} mots | accroche {words(c['intro'])} | guide {words(g)} | FAQ {len(c['faq'])} q / {sum(words(f['a']) for f in c['faq'])} mots")
    heads=re.findall(r'<(h[23])>(.*?)</\1>',g)
    for t,x in heads: print('   ',t,x)
    for f in c['faq']:
        n=words(f['a'])
        flag='' if 45<=n<=90 else '  <-- hors 50-90'
        print(f"   FAQ {n:3d} mots : {f['q']}{flag}")
    full=' '.join([c['intro'],g]+[f['q']+' '+f['a'] for f in c['faq']])
    t=txt(full).lower()
    for bad in ['made in france','fabriqué en france','fabriqués en france','tu ','ton intérieur','trustpilot','4,1','4.1']:
        if bad in t: print('   !! terme à vérifier :',bad)
    kws=['tableau zèbre','poster zèbre','affiche zèbre','zèbre noir et blanc','noir et blanc','savane','rayures','mur-galerie','toile','cadre','salon','chambre']
    print('   occurrences :',{k:t.count(k) for k in kws})
    links=re.findall(r"href=['\"]([^'\"]+)['\"]",full)
    print('   liens :',len(links),'uniques',len(set(links)))
    allinks|=set(links)
# duplication entre les deux guides (shingles de 8 mots)
def sh(s,n=8):
    w=txt(s).lower().split(); return {' '.join(w[i:i+n]) for i in range(len(w)-n)}
a=sh(d['tableau-zebre']['guide']); b=sh(d['posters-affiches-zebre']['guide'])
print(f"\nrecoupement guides (8-grammes) : {len(a&b)} sur {len(a)}/{len(b)} -> {100*len(a&b)/min(len(a),len(b)):.1f}%")
if '--links' in sys.argv:
    bad=[]
    for u in sorted(allinks):
        for k in range(3):
            r=subprocess.run(['curl','-s','-o','/dev/null','-w','%{http_code}','-A',UA,'https://www.myselfmonart.com'+u],capture_output=True,text=True).stdout
            if r!='429': break
            time.sleep(8)
        if r!='200': bad.append((u,r))
        time.sleep(1.2)
    print('liens testés :',len(allinks),'| non-200 :',bad)
