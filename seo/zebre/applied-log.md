# Journal d'application — collections zèbre

Appliqué en live via le MCP Shopify le 2026-10-04 (après 17:00 UTC). Les valeurs viennent de [`collections-zebre.json`](./collections-zebre.json).

| Heure (UTC) | Action | Résultat | Rollback |
|---|---|---|---|
| 17:13 | Tag `zèbre` envoyé aux 15 produits (tags existants conservés) | ⚪ Sans effet : Shopify traite `zèbre`, `zébre` et `zebre` comme un seul tag (comparaison sans accents) et a gardé le tag existant. Aucun produit modifié | — |
| 17:15 | Création de `posters-affiches-zebre` (gid 682801660251) : titre, description courte, SEO, règle smart TAG = `zèbre` ET TYPE = `poster`, image + alt, `custom.intro` / `guide` / `faq` / `cocon_links` / `type_of_collection` / `editorial_h1`, `breadcrumb.parentCollection` → posters-affiches-animaux, `translation.handle` (fr/en), publiée sur la boutique en ligne, tri meilleures ventes | ✅ 6 produits | `deleteCollection` |
| 17:18 | Traductions EN/DE/ES/NL de la collection poster : titre, handle, titre SEO, meta, description | ✅ 20 entrées, aucune `outdated` | Translate & Adapt |
| 17:20 | Création de `tableau-zebre` | ❌ « Handle has already been taken » | — |
| 17:55 | Nouvel essai de création de `tableau-zebre` (règle seule, non publiée) | ❌ toujours « Handle has already been taken » | — |
| 18:00 | `translation.handle` de la collection poster étendu aux 5 langues (fr/en/es/nl/de), comme `tableau-entree-couloir` | ✅ | réécrire l'ancienne valeur fr/en |
| 18:05 | Traductions EN/DE/ES/NL des métachamps de la collection poster : `custom.intro`, `custom.guide`, `custom.faq`, `custom.cocon_links` (liens localisés vers les handles traduits) | ✅ 16 entrées, aucune `outdated`, rendu vérifié sur `/en/…` et `/nl/…` | Translate & Adapt |
| 18:16 | Métaobjet `media` (gid 519130415451, alt de l'image héros) créé et relié via `meta_object.media`, comme `posters-affiches-lion` ; alt traduit EN/DE/ES/NL | ✅ 4 entrées | supprimer le métaobjet + le métachamp |
| 18:40 | Nouvel essai de création de `tableau-zebre` | ❌ toujours « Handle has already been taken » | — |
| 18:42 | Image héros de `posters-affiches-zebre` remplacée par la mise en scène (chambre, 6 posters encadrés), alt « Poster et affiche zèbre dans une chambre apaisante — mur-galerie déco murale MyselfMonArt » | ✅ servie par le CDN (OG compris), identique au pixel au fichier [`heros/poster-affiche-zebre-deco-murale.jpg`](./heros/poster-affiche-zebre-deco-murale.jpg). Shopify garde l'ancien nom de fichier lors d'un remplacement | ré-uploader l'ancienne image produit |
| 18:43 | Image héros toile (salon, 6 toiles) déposée dans Fichiers Shopify : `files/tableau-zebre-deco-murale.jpg` (MediaImage 58839221862747) | ✅ prête pour la création de la collection | supprimer le fichier |
| 05/10 07:18 | « Tableau zebre » supprimée par Walid dans l'admin → création de `tableau-zebre` (gid 682824630619) en un appel : titre, description, SEO, règle TAG = `zèbre` ET TYPE ≠ `poster`, image héros + alt, métachamps (`intro`, `guide`, `faq` 7 Q, `cocon_links`, `type_of_collection` = painting, `editorial_h1`, `breadcrumb.parentCollection` → tableau-animaux, `translation.handle` 5 langues), publiée | ✅ 9 toiles, image servie sous `collections/tableau-zebre-deco-murale.jpg` | `deleteCollection` |
| 05/10 07:18 | Métaobjet `media` (gid 519469400411) relié via `meta_object.media`, alt traduit EN/DE/ES/NL | ✅ | supprimer métaobjet + métachamp |
| 05/10 07:19 | Traductions EN/DE/ES/NL de la collection (titre, handle, SEO, description) puis des métachamps `intro`, `guide`, `faq`, `cocon_links` | ✅ 36 entrées, aucune `outdated`, longueurs identiques aux fichiers [`translations/`](./translations/) | Translate & Adapt |
| 05/10 07:23 | Liens des guides et FAQ (deux collections) pointés directement sur les handles traduits définitifs (la toile, et 2 produits dont le handle a été traduit dans la nuit) | ✅ 135 liens éditoriaux vérifiés sur les 10 pages : tous en 200, aucune redirection | — |

## Tags : comparaison sans accents

Vérifié en admin après l'envoi : le poster arc-en-ciel porte toujours `zébre`, sans `zèbre`. Pourtant la règle `TAG = zèbre` de la collection poster a bien trouvé les 6 posters (tagués `zebre` ou `zébre`). La règle couvre donc déjà les 15 produits sans retouche du catalogue. Pour les futurs zèbres, n'importe laquelle des trois graphies suffit.

## Vérifié en ligne (`/collections/posters-affiches-zebre`)

- `<title>` et meta description conformes, canonical correct, image OG = image de la collection.
- Un seul H1 (« Poster & Affiche Zèbre »), éditorial rendu, H2 du guide, FAQ de 6 questions, cocon de 4 liens.
- JSON-LD : BreadcrumbList (Accueil › Poster & Affiche Nature › Poster & Affiche Animaux › Poster & Affiche Zèbre), FAQPage (6), ItemList (6 produits).
- hreflang : `/en/collections/zebra-posters-prints`, `/de/collections/zebra-poster`, `/es/collections/posters-laminas-cebra`, `/nl/collections/posters-affiches-zebra`.
- Versions EN/DE/ES/NL : titre, H1, SEO, accroche, guide, FAQ, liens et alt traduits (métachamps traduits via leurs GID, cf. entrée 18:05).

## Blocage `tableau-zebre` (résolu le 05/10)

La collection fantôme « Tableau zebre » (id 682785833307, invisible pour l'API admin) réservait le handle. Walid l'a supprimée dans l'admin le 05/10, et la création a réussi du premier coup.

## Images héros

Process : [`hero-tools/README.md`](./hero-tools/README.md). Pièces générées vides, vraies œuvres montées par script, panel QC de 4 lentilles × 2 juges sur 3 tours. Le tour final G3 a obtenu 3 ou 4 sur 4 sur toutes les lentilles, sans aucun 2. La version G4 corrige les remarques mineures de ce tour.

## Vérifié en ligne (`/collections/tableau-zebre` et ses 4 traductions)

- `<title>` et H1 traduits (« Tableau Zèbre », « Zebra Artwork », « Zebrabild », « Cuadro de Cebra », « Zebraschilderij »). FAQ JSON-LD de 7 questions. Fil d'Ariane … › Tableau Animaux › Tableau Zèbre. 43 balises hreflang. Image OG = image héros.
- 9 toiles dans la collection, toutes de type `painting`.
- Les 135 liens éditoriaux des 10 pages zèbre (2 collections × 5 langues) répondent en 200, sans redirection.

## Reste à faire hors MCP

- Navigation (admin) : ajouter les deux collections sous Animaux.
- Autres canaux de vente (Google/Shopping…) : l'outil ne publie que sur la boutique en ligne.
- Optionnel : copier `heros/*.jpg` dans `growth/hero-tools/published/` du thème actif, comme pour les autres collections.
