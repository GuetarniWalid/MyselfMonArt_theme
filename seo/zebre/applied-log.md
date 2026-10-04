# Journal d'application — collections zèbre

Appliqué en live via le MCP Shopify le 2026-10-04 (après 17:00 UTC). Les valeurs viennent de [`collections-zebre.json`](./collections-zebre.json).

| Heure (UTC) | Action | Résultat | Rollback |
|---|---|---|---|
| 17:13 | Tag `zèbre` envoyé aux 15 produits (tags existants conservés) | ⚪ Sans effet : Shopify traite `zèbre`, `zébre` et `zebre` comme un seul tag (comparaison sans accents) et a gardé le tag existant. Aucun produit modifié | — |
| 17:15 | Création de `posters-affiches-zebre` (gid 682801660251) : titre, description courte, SEO, règle smart TAG = `zèbre` ET TYPE = `poster`, image + alt, `custom.intro` / `guide` / `faq` / `cocon_links` / `type_of_collection` / `editorial_h1`, `breadcrumb.parentCollection` → posters-affiches-animaux, `translation.handle` (fr/en), publiée sur la boutique en ligne, tri meilleures ventes | ✅ 6 produits | `deleteCollection` |
| 17:18 | Traductions EN/DE/ES/NL de la collection poster : titre, handle, titre SEO, meta, description | ✅ 20 entrées, aucune `outdated` | Translate & Adapt |
| 17:20 | Création de `tableau-zebre` | ❌ « Handle has already been taken » | — |

## Tags : comparaison sans accents

Vérifié en admin après l'envoi : le poster arc-en-ciel porte toujours `zébre`, sans `zèbre`. Pourtant la règle `TAG = zèbre` de la collection poster a bien trouvé les 6 posters (tagués `zebre` ou `zébre`). La règle couvre donc déjà les 15 produits sans retouche du catalogue. Pour les futurs zèbres, n'importe laquelle des trois graphies suffit.

## Vérifié en ligne (`/collections/posters-affiches-zebre`)

- `<title>` et meta description conformes, canonical correct, image OG = image de la collection.
- Un seul H1 (« Poster & Affiche Zèbre »), éditorial rendu, H2 du guide, FAQ de 6 questions, cocon de 4 liens.
- JSON-LD : BreadcrumbList (Accueil › Poster & Affiche Nature › Poster & Affiche Animaux › Poster & Affiche Zèbre), FAQPage (6), ItemList (6 produits).
- hreflang : `/en/collections/zebra-posters-prints`, `/de/collections/zebra-poster`, `/es/collections/posters-laminas-cebra`, `/nl/collections/posters-affiches-zebra`.
- Version EN : titre, H1 et SEO en anglais. **L'accroche, le guide et la FAQ restent en français** : ce sont des métachamps, et le MCP n'expose pas leurs identifiants, donc impossible de les traduire depuis ici. À passer dans la chaîne de traduction habituelle.

## Blocage `tableau-zebre`

- Le site public sert toujours « Tableau zebre » (id 682785833307, 9 produits, sans H1 ni SEO).
- L'API admin répond « Collection does not exist » à la lecture, à la mise à jour et à la suppression de cet id, et aucune recherche admin ne la trouve.
- Pourtant le handle `tableau-zebre` reste réservé : impossible de créer la collection complète à cette adresse.
- À faire dans l'admin Shopify : supprimer « Tableau zebre » si elle y apparaît (ou vérifier qu'elle n'y est plus). Dès que le handle est libéré, la création se fait en un appel avec les valeurs de `collections-zebre.json` (règle TAG = `zèbre` ET TYPE ≠ `poster`, image `tableau-zebre-rayures-multicolores-ambiance-minimaliste-2.jpg`).

## Reste à faire hors MCP

- Navigation (admin) : ajouter les deux collections sous Animaux.
- Autres canaux de vente (Google/Shopping…) : l'outil ne publie que sur la boutique en ligne.
- Traductions des métachamps (accroche, guide, FAQ).
- Image héros mise en scène (playbook hero-tools, en local).
