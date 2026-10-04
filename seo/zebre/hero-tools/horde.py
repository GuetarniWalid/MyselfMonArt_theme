import json, sys, time, urllib.request
API="https://aihorde.net/api/v2"
H={'apikey':'0000000000','Content-Type':'application/json','Client-Agent':'mma-hero:1.0:anon','User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36'}
def call(method,path,body=None):
    req=urllib.request.Request(API+path,data=json.dumps(body).encode() if body else None,headers=H,method=method)
    try:
        return json.load(urllib.request.urlopen(req,timeout=60))
    except urllib.error.HTTPError as e:
        return {'error':e.code,'body':e.read().decode()[:500]}
def submit(prompt,neg,model,n=2,w=1024,h=1024,steps=30,cfg=6,sampler='k_dpmpp_2m',seed=None):
    p={'sampler_name':sampler,'cfg_scale':cfg,'width':w,'height':h,'steps':steps,'n':n,'karras':True}
    if seed: p['seed']=str(seed)
    body={'prompt':prompt+' ### '+neg,'params':p,'models':[model],'nsfw':False,'censor_nsfw':True,'r2':True,'shared':False,'trusted_workers':False}
    return call('POST','/generate/async',body)
if __name__=='__main__':
    cfg=json.load(open(sys.argv[1]))
    ids=[]
    for job in cfg:
        r=submit(**job['args']); print(job['name'],r); 
        if 'id' in r: ids.append((job['name'],r['id']))
    json.dump(ids,open(sys.argv[2],'w'))
