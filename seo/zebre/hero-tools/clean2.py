"""Nettoyage du mur par diffusion (Laplace multi-échelle) + grain, puis re-teinte optionnelle."""
import json, sys
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFilter

def laplace_fill(img, mask, iters=400):
    """img float32 HxWx3, mask bool (True = à remplir). Multi-échelle grossier → fin."""
    H, W = mask.shape
    if min(H, W) > 40:
        sm = cv2.resize(img, (W // 2, H // 2), interpolation=cv2.INTER_AREA)
        mm = cv2.resize(mask.astype(np.uint8), (W // 2, H // 2), interpolation=cv2.INTER_NEAREST) > 0
        # un pixel bas-res est "connu" seulement si tout son bloc est connu
        known_full = cv2.resize((~mask).astype(np.float32), (W // 2, H // 2), interpolation=cv2.INTER_AREA) > 0.999
        mm = ~known_full
        coarse = laplace_fill(sm, mm, iters)
        up = cv2.resize(coarse, (W, H), interpolation=cv2.INTER_LINEAR)
        out = img.copy(); out[mask] = up[mask]
        it = 60
    else:
        out = img.copy(); out[mask] = img[~mask].mean(0); it = iters
    k = np.array([[0, .25, 0], [.25, 0, .25], [0, .25, 0]], np.float32)
    for _ in range(it):
        av = cv2.filter2D(out, -1, k, borderType=cv2.BORDER_REPLICATE)
        out[mask] = av[mask]
    return out

spec = json.load(open(sys.argv[1]))
im = np.asarray(Image.open(spec['src']).convert('RGB'), np.float32)
H, W = im.shape[:2]
m = Image.new('L', (W, H), 0); d = ImageDraw.Draw(m)
mg = spec.get('margin', [8, 8, 24, 28])
for x0, y0, x1, y1 in spec['art_rects']:
    d.rectangle((x0 - mg[0], y0 - mg[1], x1 + mg[2], y1 + mg[3]), fill=255)
mask = np.asarray(m) > 0
# lisser d'abord le mur connu (retire le grain JPEG), remplir, puis remettre un grain
base = cv2.GaussianBlur(im, (0, 0), 1.2)
filled = laplace_fill(base, mask)
rng = np.random.default_rng(1)
grain = cv2.GaussianBlur(rng.normal(0, spec.get('grain', 1.6), (H, W)).astype(np.float32), (0, 0), 0.6)
filled = filled + grain[..., None] * 1.6
soft = np.asarray(m.filter(ImageFilter.GaussianBlur(spec.get('feather', 2.0))), np.float32)[..., None] / 255
out = im * (1 - soft) + filled * soft
Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).save(spec['out'], quality=95)
print('saved', spec['out'])
