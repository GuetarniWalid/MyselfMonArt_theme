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
| 05/10 08:51 | **v2 éditoriale** (retour de Walid : « descriptions très pauvres ») : analyse persona/voix/SERP/concurrents ([`v2/analyse-v2.md`](./v2/analyse-v2.md)), puis réécriture complète FR des deux collections : champ Description (≈ 165 mots), accroche, guide (toile 1 525 mots / poster 1 177), FAQ 8 questions chacune ; relecture adversariale intégrée (op art vs pop art, HPI, faits produit) | ✅ empreintes SHA-256 Shopify = fichiers [`v2/fr.json`](./v2/fr.json) pour les 8 champs ; en ligne : 1 H1, FAQPage 8 q, 49 liens en 200 | réappliquer les valeurs v1 (historique git) |
| 05/10 09:00-09:40 | Traductions EN/DE/ES/NL de la v2 (description, accroche, guide, FAQ), avec les liens pointés directement sur les URL traduites ([`v2/urlmap.json`](./v2/urlmap.json), 49 liens × 4 langues, tous en 200). Une passe d'alignement a suivi sur les libellés réels des fiches produit : bordures, cadres et contour blanc par langue, et **pouces ajoutés en EN**, car les fiches EN affichent les tailles en pouces. Le sigle HPI a été retiré en DE/ES/NL (inconnu hors de France), en gardant la mention de Jeanne Siaud-Facchin | ✅ 32 champs `outdated:false`, longueurs relues égales aux fichiers [`v2/en.json`](./v2/en.json), [`de`](./v2/de.json), [`es`](./v2/es.json), [`nl`](./v2/nl.json) | Translate & Adapt |
| 05/10 09:20 | **Grammage 250 g/m²** (confirmé par Walid) ajouté en FR. Poster : description, guide et FAQ qualité. Toile : la phrase sur le poster dans le guide et la FAQ « Existe-t-il aussi en poster ? ». Meta description du poster réécrite. Le premier appel n'envoyait que `seoDescription`, ce qui a vidé le titre SEO ; il a été restauré à l'identique dans la minute, avec la même empreinte. Leçon : toujours envoyer `seoTitle` et `seoDescription` ensemble | ✅ empreintes Shopify = [`v2/targets_250.json`](./v2/targets_250.json) (7 champs) ; source [`v2/build_fr.py`](./v2/build_fr.py) | réappliquer [`v2/fr.json`](./v2/fr.json) du commit précédent |
| 05/10 09:25-09:35 | 250 g/m² reporté en EN/DE/ES/NL : les 5 phrases, la nouvelle meta description du poster, et le titre SEO republié tel quel (marqué `outdated` après la restauration). EN : « 250gsm » | ✅ 28 entrées `outdated:false`, longueurs = fichiers `v2/{en,de,es,nl}.json` | Translate & Adapt |
| 05/10 09:21 | **Note Trustpilot alignée dans le thème** (`myselfmonart_tw_theme`, commit `396f4ec`, déployé). Vraie note relevée le 05/10 : **4,2/5 sur 86 avis**, libellé officiel « Bien » (« Excellent » seulement à partir de 4,3). Avant : 4,5/5 dans la FAQ de la fiche poster, 4,1/5 sur la fiche personnalisée, 81 avis dans les blocs, libellé « Excellent ». Après : note et nombre d'avis réglés dans `settings_data`, libellé calculé depuis la note, virgule décimale hors anglais. 250 g/m² ajouté aux fiches poster (6 mentions) et toile (1) | ✅ en ligne dans les 5 langues : fiches poster et toile, JSON-LD 4.2/86, 6 mentions 250 g/m² sur la fiche poster, aucune trace de 4,5/5 | `git revert 396f4ec` |
| 05/10 09:30 | Traductions EN/DE/ES/NL des textes de templates modifiés (`product.poster` 6 clés, `product.painting` 1, `product.personalized` 1) | ✅ 32 entrées `outdated:false`, détail dans [`v2/template-translations-2026-10-05.json`](./v2/template-translations-2026-10-05.json) | Translate & Adapt |

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

- Navigation : le méga-menu est réglé dans l'éditeur de thème (section « En-tête », blocs « Ensemble de collection »), pas dans le menu Navigation de Shopify, et le MCP ne peut pas le modifier. Vérifié en ligne le 05/10 : il n'y a pas de niveau « Animaux ». « Tableau Animaux » est un lien du groupe « Nature & Sauvage ». Aucune collection d'espèce (lion, cheval) ni « Poster & Affiche Animaux » n'est dans le menu. Fait le 05/10 par un push direct sur `main` du dépôt `myselfmonart_tw_theme` (commit 7bd29dd, déployé par le workflow). Ajouts : un groupe « Animaux » dans Nos Tableaux (Animaux, Lion, Cheval, Zèbre) et un dans Posters & Affiches (Animaux, Lion, Cheval, Zèbre). Titre du groupe traduit : Animals / Tiere / Animales / Dieren (2 blocs × 4 langues, aucune traduction `outdated`). Vérifié en ligne sur ordinateur et mobile dans les 5 langues : 8 liens par langue, tous vers les adresses traduites, tous en 200. La PR #1 de ce dépôt a été fermée sans fusion, à la demande de Walid : désormais, push direct sur `main`, règle notée dans le `CLAUDE.md` du thème. Deux titres visibles dans le nouveau groupe ont été harmonisés le 05/10. En français, `tableau-cheval` passe de « Tableau chevaux » à « Tableau Chevaux » : le mot-clé principal « tableau chevaux » est conservé, et les traductions EN/DE/ES/NL sont republiées sans changement, donc rien n'est `outdated`. En allemand, `posters-affiches-lion` passe de « Löwen Poster – moderne Wandposter & Kunstdrucke » à « Löwen Poster & Plakate » (le meta title DE n'a pas changé). Les deux H1 ont été vérifiés en ligne.
- Autres canaux de vente (Google/Shopping…) : l'outil ne publie que sur la boutique en ligne.
- Optionnel : copier `heros/*.jpg` dans `growth/hero-tools/published/` du thème actif, comme pour les autres collections.

## Vérifié en ligne, v2 (05/10)

| Page | H1 | Guide (mots) | FAQPage | Liens du guide |
|---|---|---:|---:|---|
| /collections/tableau-zebre | Tableau Zèbre | 1 543 | 8 | 29, tous en 200 |
| /collections/posters-affiches-zebre | Poster & Affiche Zèbre | 1 191 | 8 | 24, tous en 200 |
| /en/collections/zebra-artwork | Zebra Artwork | 1 568 | 8 | 29, table EN |
| /en/collections/zebra-posters-prints | Zebra Posters & Prints | 1 233 | 8 | 24, table EN |
| /de/collections/zebrabild | Zebrabild | 1 408 | 8 | 29, table DE |
| /de/collections/zebra-poster | Zebra Poster | 1 128 | 8 | 24, table DE |
| /es/collections/cuadro-de-cebra | Cuadro de Cebra | 1 590 | 8 | 29, table ES |
| /es/collections/posters-laminas-cebra | Pósters y Láminas de Cebra | 1 227 | 8 | 24, table ES |
| /nl/collections/zebra-schilderij | Zebraschilderij | 1 517 | 8 | 29, table NL |
| /nl/collections/posters-affiches-zebra | Poster Zebra & Affiche Zebra | 1 181 | 8 | 24, table NL |
