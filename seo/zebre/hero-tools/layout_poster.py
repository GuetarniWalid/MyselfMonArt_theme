"""Calcule des boîtes de cadres dont l'ouverture du passe-partout respecte le ratio de l'œuvre."""
import json, sys
from PIL import Image
MAT, FW = 0.09, 0.028
def outer_w(h, r):
    best = None
    for w in range(40, 1200):
        fw = max(6, round(min(w, h) * FW)); iw, ih = w - 2 * fw, h - 2 * fw
        m = round(min(iw, ih) * MAT); aw, ah = iw - 2 * m, ih - 2 * m
        e = abs(aw / ah - r)
        if best is None or e < best[0]: best = (e, w)
    return best[1]
def ratio(a): im = Image.open(f'art/{a}.jpg'); return im.width / im.height
def row(items, y, align, gap, cx):
    # items: (art, h, frame) ; align 'bottom' => y = bas ; 'top' => y = haut
    ws = [outer_w(h, ratio(a)) for a, h, f in items]
    total = sum(ws) + gap * (len(ws) - 1); x = cx - total / 2; out = []
    for (a, h, f), w in zip(items, ws):
        yy = y - h if align == 'bottom' else y
        out.append({'art': a, 'frame': f, 'px': [round(x), round(yy), w, h]}); x += w + gap
    return out
spec = json.load(open(sys.argv[1]))
items = []
for r in spec['rows']:
    items += row([tuple(i) for i in r['items']], r['y'], r['align'], r['gap'], r['cx'])
out = {'room': spec['room'], 'kind': 'poster', 'out': spec['out'], 'light': spec.get('light', [1, 0.8]),
       'items': [{'art': i['art'], 'frame': i['frame'], 'box': [v / 1200 for v in i['px']]} for i in items]}
json.dump(out, open(spec['spec_out'], 'w'))
for i in items: print(i)
