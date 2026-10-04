# Images héros zèbre — process appliqué

Même principe que le playbook `growth/HERO-IMAGE-PLAYBOOK.md` (resté en local, jamais poussé sur GitHub) tel que décrit dans `seo/entree-couloir/run-log.md` du thème actif : les meilleures œuvres de la collection, accrochées en mur-galerie dans une pièce qui va avec le thème, puis un panel QC avant publication.

Différence : pas de clé Gemini dans la session cloud. La pièce est donc générée vide (SDXL via AI Horde, file gratuite), puis les **vraies images produit** y sont montées par script. Les œuvres sont donc fidèles au pixel près ; rien n'est réinterprété par l'IA.

## Étapes

1. **Curation.**
   - Toile, 6 pièces : arc-en-ciel, portrait doré sur fond noir, tribal ocre (rangée haute), puis œil noir et blanc, zèbre arc-en-ciel au galop, zèbre sous la neige (rangée basse).
   - Poster, 6 pièces : œil, doré, arc-en-ciel, puis tribal, neige, maternité.
   - Palette : noir et blanc majoritaire, avec deux ou trois accents couleur.
   - Exclus : le zèbre rieur (chambre bébé, hors ton) et l'éléphant street art (hors sujet).
2. **Pièces.**
   - Salon : mur crème à la chaux, canapé cuir cognac, olivier, arche, lampadaire jute.
   - Chambre : mur sable rosé, tête de lit lin, suspensions laiton, chevets noyer.
   - Prompts : [`specs/jobs1.json`](./specs/jobs1.json). Modèle : Juggernaut XL 1024x1024.
   - Retouche : les ombres floues des suspensions ont été effacées par diffusion ([`clean2.py`](./clean2.py)).
3. **Montage** ([`compose.py`](./compose.py)).
   - Toiles : châssis en vraie projection 3D, avec flancs en gallery wrap vers le point de fuite. S'y ajoutent l'ombre portée et l'ombre de contact (lumière de la fenêtre), la lumière de la pièce reportée sur les toiles (dégradé, noirs relevés par l'ambiance) et le grain toile.
   - Posters : cadre noir ou chêne à coins à onglet, passe-partout à 9 %, dimensions calculées pour que l'œuvre ne soit pas rognée ([`layout_poster.py`](./layout_poster.py)). La dominante chaude de la pièce est reportée sur le passe-partout.
   - L'olivier repasse devant les toiles, comme dans une vraie photo.
4. **Panel QC.**
   - 4 lentilles (fidélité produit, réalisme photo, direction artistique, vignette e-commerce), 2 juges par lentille.
   - 3 tours :
     - série « pièce existante nettoyée » : écartée, car la pièce était déjà utilisée par d'autres collections ;
     - série « pièces générées » G3 : 3 ou 4 sur 4 partout, aucun 2 ;
     - G4 : corrections des remarques du panel G3 (colonnes alignées, gouttières régulières, noirs relevés, galerie poster centrée sur le lit et aérée, taches des suspensions effacées).
5. **Publication.**
   - Upload « staged » Shopify, puis image de collection et alt.
   - Le métaobjet `media` (alt) est relié par `meta_object.media` et traduit en EN, DE, ES et NL.
   - Fichiers finaux : [`../heros/`](../heros/).

Reproduire : `python3 compose.py specs/spec_toile_G4.json specs/spec_poster_G4.json`. Le script attend `art/<id>.jpg` (2e image de chaque fiche produit, le visuel à plat) et `rooms/`.
