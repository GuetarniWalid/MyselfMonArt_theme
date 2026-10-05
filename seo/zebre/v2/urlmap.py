import json,re,subprocess,time
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/126 Safari/537.36"
d=json.load(open('fr.json',encoding='utf-8'))
links=set()
for c in d.values():
    full=' '.join([c['description_html'],c['intro'],c['guide']]+[f['a'] for f in c['faq']])
    links|=set(re.findall(r"href=['\"]([^'\"]+)['\"]",full))
out={}
for loc in ['en','de','es','nl']:
    out[loc]={}
    for u in sorted(links):
        for k in range(4):
            r=subprocess.run(['curl','-s','-L','-o','/dev/null','-w','%{http_code} %{url_effective}','-A',UA,f'https://www.myselfmonart.com/{loc}{u}'],capture_output=True,text=True).stdout.split()
            if r and r[0]!='429': break
            time.sleep(10)
        code,eff=r[0],r[1]
        path=re.sub(r'^https://www\.myselfmonart\.com','',eff)
        out[loc][u]={'code':code,'path':path}
        time.sleep(1.3)
    json.dump(out,open('urlmap.json','w'),ensure_ascii=False,indent=1)
    print(loc,'done', sum(1 for v in out[loc].values() if v['code']!='200'),'non-200')
