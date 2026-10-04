"""Montage d'un mur-galerie : vraies œuvres (fichiers produit) posées dans une pièce vide.

Toile : face avant + bord de châssis (gallery wrap miroir, côté tourné vers l'objectif),
ombre portée douce + ombre de contact, éclairage de la pièce reporté sur l'œuvre, grain toile.
Poster : cadre (profil biseauté), passe-partout avec biseau blanc, ombre interne, reflet de verre.
"""
import json, sys
import numpy as np
from PIL import Image, ImageFilter, ImageDraw

ART = 'art/'


def load(path):
    return Image.open(path).convert('RGB')


def cover(im, w, h):
    """Redimensionne en remplissant w x h (recadrage centré minimal)."""
    r = max(w / im.width, h / im.height)
    im = im.resize((max(w, round(im.width * r)), max(h, round(im.height * r))), Image.LANCZOS)
    x = (im.width - w) // 2
    y = (im.height - h) // 2
    return im.crop((x, y, x + w, y + h))


def light_field(room, blur):
    """Luminance basse fréquence de la pièce, normalisée autour de 1."""
    g = np.asarray(room.convert('L').filter(ImageFilter.GaussianBlur(blur)), dtype=np.float32)
    return g / g.mean()


def apply_light(tile, field, x, y, strength):
    a = np.asarray(tile, dtype=np.float32)
    f = field[y:y + tile.height, x:x + tile.width]
    f = 1 + (f / f.mean() - 1) * strength  # garde l'exposition moyenne de l'œuvre, reporte le dégradé
    a = np.clip(a * f[..., None], 0, 255)
    return Image.fromarray(a.astype(np.uint8))


def grain(tile, amount, seed=0):
    rng = np.random.default_rng(seed)
    a = np.asarray(tile, dtype=np.float32)
    n = rng.normal(0, amount, a.shape[:2]).astype(np.float32)
    # trame toile : léger quadrillage
    yy, xx = np.mgrid[0:a.shape[0], 0:a.shape[1]]
    weave = (np.sin(xx * 2.1) * np.sin(yy * 2.1)) * amount * 0.6
    a = np.clip(a + (n + weave)[..., None], 0, 255)
    return Image.fromarray(a.astype(np.uint8))


def shadow(base, box, offset, blur, opacity):
    """Ombre multipliée sur le mur (box = x0,y0,x1,y1)."""
    W, H = base.size
    m = Image.new('L', (W, H), 0)
    d = ImageDraw.Draw(m)
    x0, y0, x1, y1 = box
    d.rectangle((x0 + offset[0], y0 + offset[1], x1 + offset[0], y1 + offset[1]), fill=255)
    m = m.filter(ImageFilter.GaussianBlur(blur))
    a = np.asarray(base, dtype=np.float32)
    s = np.asarray(m, dtype=np.float32)[..., None] / 255 * opacity
    a = a * (1 - s)
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


def shade(im, k):
    a = np.asarray(im, dtype=np.float32) * k
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


def poly_mask(W, H, pts):
    m = Image.new('L', (W, H), 0)
    ImageDraw.Draw(m).polygon([tuple(map(float, p)) for p in pts], fill=255)
    return m


def place_canvas(base, field, art, x, y, w, h, depth, light_dir, cx, cy, seed=0, cast=None):
    W, H = base.size
    # décalage de la face arrière (contre le mur) vers le point de fuite : on voit les flancs tournés vers l'objectif
    kx = ((x + w / 2) - cx) / (W * 0.5)
    ky = ((y + h / 2) - cy) / (H * 0.5)
    dx = -np.sign(kx) * depth * (0.45 + 0.55 * min(1, abs(kx)))
    dy = -np.sign(ky) * depth * (0.45 + 0.55 * min(1, abs(ky)))
    dx, dy = float(dx), float(dy)
    # ombres portées depuis la face arrière (sur le mur)
    bx, by = x + dx, y + dy
    ox, oy = light_dir[0] * depth * 1.5, light_dir[1] * depth * 1.5 + depth * 0.6
    base = shadow(base, (bx, by, bx + w, by + h), (ox, oy), blur=depth * 3.0, opacity=0.40)
    base = shadow(base, (bx, by, bx + w, by + h), (ox * 0.35, oy * 0.35 + 1), blur=depth * 0.9, opacity=0.45)
    face = cover(art, w, h)
    if cast is not None:
        face = apply_cast(face, cast, 0.5)
    # lumière ambiante : les noirs d'une toile mate ne sont jamais à 0 dans une pièce éclairée
    fa = np.asarray(face, np.float32)
    amb = (np.array(cast, np.float32) if cast is not None else np.full(3, 200, np.float32))
    fa = fa * 0.925 + amb * 0.075
    # léger dégradé directionnel (côté fenêtre plus lumineux)
    gy, gx = np.mgrid[0:h, 0:w]
    gr = 1 + 0.06 * (0.5 - gx / max(1, w - 1)) * np.sign(light_dir[0]) + 0.03 * (0.5 - gy / max(1, h - 1))
    face = Image.fromarray(np.clip(fa * gr[..., None], 0, 255).astype(np.uint8))
    blurred = face.filter(ImageFilter.GaussianBlur(1.6))
    ex, ey = int(np.ceil(abs(dx))) + 2, int(np.ceil(abs(dy))) + 2
    # flanc horizontal (gauche/droite)
    if dx != 0:
        if dx > 0:  # on voit le flanc droit
            strip = blurred.crop((w - ex, 0, w, h)).transpose(Image.FLIP_LEFT_RIGHT)
            k = 0.62 if light_dir[0] > 0 else 0.90
            pts = [(x + w, y), (x + w + dx, y + dy), (x + w + dx, y + h + dy), (x + w, y + h)]
            ox0 = x + w
        else:
            strip = blurred.crop((0, 0, ex, h)).transpose(Image.FLIP_LEFT_RIGHT)
            k = 0.90 if light_dir[0] > 0 else 0.62
            pts = [(x, y), (x + dx, y + dy), (x + dx, y + h + dy), (x, y + h)]
            ox0 = x - ex
        tile = Image.new('RGB', (W, H)); tile.paste(shade(strip, k), (int(ox0), int(y + min(0, dy))))
        tile.paste(shade(strip, k), (int(ox0), int(y + max(0, dy))))
        base = Image.composite(tile, base, poly_mask(W, H, pts))
    if dy != 0:
        if dy > 0:  # flanc bas
            strip = blurred.crop((0, h - ey, w, h)).transpose(Image.FLIP_TOP_BOTTOM)
            k = 0.50
            pts = [(x, y + h), (x + w, y + h), (x + w + dx, y + h + dy), (x + dx, y + h + dy)]
            oy0 = y + h
        else:
            strip = blurred.crop((0, 0, w, ey)).transpose(Image.FLIP_TOP_BOTTOM)
            k = 0.88
            pts = [(x, y), (x + w, y), (x + w + dx, y + dy), (x + dx, y + dy)]
            oy0 = y - ey
        tile = Image.new('RGB', (W, H))
        tile.paste(shade(strip, k), (int(x + min(0, dx)), int(oy0)))
        tile.paste(shade(strip, k), (int(x + max(0, dx)), int(oy0)))
        base = Image.composite(tile, base, poly_mask(W, H, pts))
    face = apply_light(face, field, x, y, 0.55)
    face = grain(face, 2.2, seed)
    a = np.asarray(face, dtype=np.float32)
    yy, xx = np.mgrid[0:h, 0:w]
    dist = np.minimum.reduce([xx, yy, w - 1 - xx, h - 1 - yy]).astype(np.float32)
    v = 1 - 0.12 * np.exp(-dist / 1.6)
    face = Image.fromarray(np.clip(a * v[..., None], 0, 255).astype(np.uint8))
    base.paste(face, (x, y))
    return base


def apply_cast(im, cast, strength):
    """Teinte la pièce : cast = couleur moyenne du mur ; on reporte sa dominante (normalisée) sur l'œuvre."""
    c = np.array(cast, np.float32)
    c = c / c.mean()
    c = 1 + (c - 1) * strength
    a = np.asarray(im, dtype=np.float32) * c
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


FRAMES = {
    'noir': (24, 24, 26), 'blanc': (238, 236, 232), 'chene': (190, 150, 105), 'noyer': (98, 66, 45),
}


def frame_tile(w, h, fw, color, seed=0):
    """Cadre avec coins à onglet : chaque pixel du profil prend l'ombrage du côté le plus proche."""
    a = np.empty((h, w, 3), np.float32); a[:] = color
    yy, xx = np.mgrid[0:h, 0:w]
    if color in (FRAMES['chene'], FRAMES['noyer']):
        rng = np.random.default_rng(seed)
        grain_h = np.sin(yy * 0.9 + rng.normal(0, 1, (h, 1)).cumsum(0) * 0.3) * 5
        grain_v = np.sin(xx * 0.9 + rng.normal(0, 1, (1, w)).cumsum(1) * 0.3) * 5
    else:
        grain_h = grain_v = np.zeros((h, w), np.float32)
    dl, dt, dr, db = xx, yy, w - 1 - xx, h - 1 - yy
    side = np.argmin(np.stack([dt, dl, db, dr]), 0)  # 0 haut, 1 gauche, 2 bas, 3 droite
    k = np.choose(side, [1.12, 1.04, 0.80, 0.88])
    wood = np.choose(side, [grain_h, grain_v, grain_h, grain_v])
    a = a * k[..., None] + wood[..., None]
    d_out = np.minimum.reduce([dl, dt, dr, db]).astype(np.float32)
    a *= (1 - 0.20 * np.exp(-d_out / 1.2))[..., None]
    # arête intérieure (feuillure) légèrement sombre
    d_in = np.abs(d_out - (fw - 1))
    a *= (1 - 0.18 * np.exp(-d_in / 0.9))[..., None]
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


def place_poster(base, field, art, x, y, w, h, frame='noir', mat=0.11, fw_ratio=0.028,
                 light_dir=(1, 1), seed=0, cast=None):
    """(x,y,w,h) = encombrement extérieur du cadre."""
    fw = max(6, int(round(min(w, h) * fw_ratio)))
    depth = max(5, fw * 1.1)
    ox, oy = light_dir[0] * depth * 1.1, light_dir[1] * depth * 1.1 + depth * 0.4
    base = shadow(base, (x, y, x + w, y + h), (ox, oy), blur=depth * 2.6, opacity=0.48)
    base = shadow(base, (x, y, x + w, y + h), (ox * 0.35, oy * 0.35 + 1), blur=depth * 0.7, opacity=0.50)
    col = FRAMES[frame]
    fr = frame_tile(w, h, fw, col, seed)
    # passe-partout
    iw, ih = w - 2 * fw, h - 2 * fw
    m = int(round(min(iw, ih) * mat)) if mat else 0
    matc = Image.new('RGB', (iw, ih), (244, 241, 234))
    if m:
        # ombre du cadre sur le passe-partout (haut/gauche)
        mm = np.asarray(matc, dtype=np.float32).copy()
        yy, xx = np.mgrid[0:ih, 0:iw]
        mm *= (1 - 0.16 * np.exp(-yy / (fw * 0.35)) - 0.10 * np.exp(-xx / (fw * 0.35)))[..., None]
        matc = Image.fromarray(np.clip(mm, 0, 255).astype(np.uint8))
        aw, ah = iw - 2 * m, ih - 2 * m
        art_t = cover(art, aw, ah)
        # biseau blanc (âme du passe-partout)
        bv = max(2, m // 22)
        d = ImageDraw.Draw(matc)
        d.rectangle((m - bv, m - bv, m + aw + bv - 1, m + ah + bv - 1), fill=(252, 251, 248))
        d.line((m - bv, m + ah + bv - 1, m + aw + bv - 1, m + ah + bv - 1), fill=(228, 225, 218), width=1)
        d.line((m + aw + bv - 1, m - bv, m + aw + bv - 1, m + ah + bv - 1), fill=(232, 229, 222), width=1)
        # ombre interne du passe-partout sur l'œuvre
        a = np.asarray(art_t, dtype=np.float32).copy()
        yy, xx = np.mgrid[0:ah, 0:aw]
        a *= (1 - 0.22 * np.exp(-yy / 3.0) - 0.15 * np.exp(-xx / 3.0))[..., None]
        art_t = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
        matc.paste(art_t, (m, m))
    else:
        art_t = cover(art, iw, ih)
        a = np.asarray(art_t, dtype=np.float32).copy()
        yy, xx = np.mgrid[0:ih, 0:iw]
        a *= (1 - 0.30 * np.exp(-yy / (fw * 0.4)) - 0.2 * np.exp(-xx / (fw * 0.4)))[..., None]
        matc = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
    fr.paste(matc, (fw, fw))
    if cast is not None:
        fr = apply_cast(fr, cast, 0.55)
    fr = apply_light(fr, field, x, y, 0.55)
    # reflet du verre : diagonale très légère
    a = np.asarray(fr, dtype=np.float32).copy()
    yy, xx = np.mgrid[0:h, 0:w]
    t = (xx / w * 0.8 + yy / h * 0.5)
    glare = np.clip(1 - np.abs(t - 0.45) / 0.18, 0, 1) * 10
    inner = (xx >= fw) & (xx < w - fw) & (yy >= fw) & (yy < h - fw)
    a[inner] += glare[inner][..., None]
    fr = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
    base.paste(fr, (x, y))
    return base


def foreground_mask(room, boxes, thr):
    """Pixels plus sombres que le mur local (plante, lampe) dans les zones données : restaurés au premier plan."""
    import cv2
    L = np.asarray(room.convert('L'), np.float32)
    k = max(9, int(room.width * 0.02) | 1)
    wall = cv2.GaussianBlur(cv2.dilate(L, np.ones((k, k), np.uint8)), (0, 0), k / 3)
    fg = ((wall - L) > thr).astype(np.uint8)
    m = np.zeros_like(fg)
    for x0, y0, x1, y1 in boxes:
        X0, Y0, X1, Y1 = [int(v * room.width) for v in (x0, y0, x1, y1)]
        m[Y0:Y1, X0:X1] = fg[Y0:Y1, X0:X1]
    return Image.fromarray((cv2.GaussianBlur(m.astype(np.float32), (0, 0), 0.7) * 255).astype(np.uint8))


def build(spec_path):
    spec = json.load(open(spec_path))
    room = load(spec['room'])
    if 'crop' in spec:
        cx0, cy0, cx1, cy1 = spec['crop']
        room = room.crop((int(cx0 * room.width), int(cy0 * room.height), int(cx1 * room.width), int(cy1 * room.height)))
    S = spec.get('work_size', 2048)
    room = room.resize((S, S), Image.LANCZOS)
    field = light_field(room, S * 0.03)
    cast = None
    if 'cast_box' in spec:
        x0, y0, x1, y1 = [int(v * S) for v in spec['cast_box']]
        cast = np.asarray(room.crop((x0, y0, x1, y1)), np.float32).reshape(-1, 3).mean(0)
    base = room.copy()
    cx, cy = [v * S for v in spec.get('camera', [0.5, 0.45])]
    for i, it in enumerate(spec['items']):
        x, y, w, h = [int(round(v * S)) for v in it['box']]
        art = load(ART + it['art'] + '.jpg')
        if spec['kind'] == 'canvas':
            base = place_canvas(base, field, art, x, y, w, h, depth=int(S * spec.get('depth', 0.007)),
                                light_dir=spec.get('light', (1, 1)), cx=cx, cy=cy, seed=i, cast=cast)
        else:
            base = place_poster(base, field, art, x, y, w, h, frame=it.get('frame', 'noir'),
                                mat=it.get('mat', 0.11), light_dir=spec.get('light', (1, 1)), seed=i, cast=cast)
    if spec.get('foreground'):
        fm = foreground_mask(room, spec['foreground'], spec.get('fg_thr', 22))
        base = Image.composite(room, base, fm)
    a = np.asarray(base, dtype=np.float32)
    a += np.random.default_rng(7).normal(0, 1.4, a.shape[:2])[..., None]
    base = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
    out = base.resize((1200, 1200), Image.LANCZOS)
    out.save(spec['out'], quality=88, optimize=True, progressive=True)
    print('saved', spec['out'])


if __name__ == '__main__':
    for p in sys.argv[1:]:
        build(p)
