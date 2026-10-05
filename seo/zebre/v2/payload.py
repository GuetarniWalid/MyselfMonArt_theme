import json,sys
d=json.load(open('fr.json'))
c=d[sys.argv[1]]
mf=[{"namespace":"custom","key":"intro","type":"multi_line_text_field","value":c['intro']},
    {"namespace":"custom","key":"guide","type":"multi_line_text_field","value":c['guide']},
    {"namespace":"custom","key":"faq","type":"json","value":json.dumps(c['faq'],ensure_ascii=False)}]
part=sys.argv[2]
if part=='desc':
    print(c['description_html'].replace('\u00a0',' ').replace('\u202f',' '))
else:
    keys={'intro':[0],'guide':[1],'faq':[2]}[part]
    s=json.dumps([mf[i] for i in keys],ensure_ascii=False)
    print(s.replace('\u00a0','\\u00a0').replace('\u202f','\\u202f'))
