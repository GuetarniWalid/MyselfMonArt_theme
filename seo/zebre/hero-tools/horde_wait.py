import json,sys,time,urllib.request
sys.path.insert(0,'.')
from horde import call
ids=json.load(open(sys.argv[1]))
pending=dict((i,n) for n,i in ids)
t0=time.time()
while pending and time.time()-t0<int(sys.argv[2]):
    for i,n in list(pending.items()):
        c=call('GET',f'/generate/check/{i}')
        if c.get('done'):
            s=call('GET',f'/generate/status/{i}')
            for k,g in enumerate(s.get('generations',[])):
                data=urllib.request.urlopen(urllib.request.Request(g['img'],headers={'User-Agent':'Mozilla/5.0'}),timeout=120).read()
                fn=f"rooms/{n}_{k}_{g.get('seed')}.webp"; open(fn,'wb').write(data); print('saved',fn,g.get('model'),g.get('censored'))
            del pending[i]
        elif c.get('faulted') or c.get('is_possible') is False:
            print('fault',n,c); del pending[i]
        else:
            print(n,'wait',c.get('queue_position'),c.get('wait_time'),c.get('processing'),c.get('finished'))
    time.sleep(20)
print('left',pending)
