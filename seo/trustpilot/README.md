# Note Trustpilot : une seule source (05/10/2026)

## Le problème

Le thème avait déjà un réglage global « Trustpilot (avis marque) ». Il alimentait le badge, les blocs avis et les données Google. Mais les **textes libres** recopiaient les chiffres, et ils s'étaient périmés :

- 46 guides ou FAQ de collection affichaient « 4,1/5 sur 80 avis » ;
- la FAQ de la fiche poster disait 4,5/5, la fiche personnalisée 4,1/5 et la home « Plus de 80 retours » ;
- la vraie note, relevée le 05/10 sur la page publique, est de **4,2/5 sur 86 avis** (libellé officiel « Bien »).

La cause : le cahier des charges du générateur de guides (`PLAN-recuperation-collections-post-core-update.md` §5, dépôt `myselfmonart_tw_theme`) donnait « Trustpilot 4.1/80 avis » comme fait à recopier.

## La correction

Dans le thème `myselfmonart_tw_theme`, commits `fa3d51f` et `72a3859`, déployés :

- **Jetons** `[[TP_SCORE]]` et `[[TP_COUNT]]`. Le snippet `trustpilot-tokens` les remplace à l'affichage par le réglage global, avec la virgule décimale hors anglais. Il est branché sur :
  - l'éditorial de collection : accroche, guide, FAQ et son JSON-LD ;
  - les accordéons FAQ ;
  - les blocs texte et onglets des fiches produit ;
  - les signaux de confiance ;
  - la description de collection.
- **Garde-fou** : `scripts/i18n-lint.cjs`, lancé par le hook pre-commit (désormais exécutable), refuse une note ou un nombre d'avis écrit en dur dans les templates, sections, snippets, locales et `settings_data`.
- **Règle écrite** dans le `CLAUDE.md` des deux dépôts, dans METHODOLOGY §7, dans le skill du thème, dans le cahier des charges du générateur et dans l'aide du réglage.

## Migration des textes vers les jetons

| Lot | Collections | Métachamps FR | Traductions | Journal |
|---|---:|---:|---:|---|
| Templates (poster, personnalisé, home) | — | 3 (dans le thème) | 12 | [`templates-2026-10-05.json`](./templates-2026-10-05.json) |
| lot1 | 8 | 9 | 36 | [`lot1.json`](./lot1.json) |
| lot2 | 8 | 10 | 40 | [`lot2.json`](./lot2.json) |
| lot3 | 8 | **0, bloqué** | 0 | [`lot3.json`](./lot3.json) |
| lot4 | 8 | 12 | 48 | [`lot4.json`](./lot4.json) |
| lot5 | 7 | 8 | 32 | [`lot5.json`](./lot5.json) |
| lot6 | 7 | 7 | 28 | [`lot6.json`](./lot6.json) |

Méthode, pour chaque champ :

1. **Valeur de départ prouvée exacte.** Le guide est extrait brut de la page publique. La FAQ est comparée à l'octet près à l'accordéon et au JSON-LD.
2. **Seuls les chiffres changent** (contrôle difflib).
3. **Écriture FR** via `setMetafield`, puis vérification que le digest Shopify est égal au sha256 de la nouvelle valeur.
4. **Traductions republiées** avec le nouveau digest : toutes à `outdated:false`, longueurs vérifiées.
5. **Vérification en ligne** dans les 5 langues : aucun jeton brut, aucune trace de 4,1 ou de 80.

Inventaire de départ : [`inventaire-2026-10-05.json`](./inventaire-2026-10-05.json). Contrôle final indépendant : [`verification-en-ligne-2026-10-05.json`](./verification-en-ligne-2026-10-05.json).

## Lot 3 : en attente

L'agent du lot 3 a été arrêté par le contrôle des autorisations. Huit collections affichent donc encore « 4,1/5 sur 80 avis » :

- tableaux-chambre-bebe, tableau-chambre-fille, tableau-jaune, tableau-orange ;
- tableaux-nature-sauvage, tableau-street-art, tableau-portrait-1, posters-affiches-chambre-enfant.

Les valeurs avec jetons sont prêtes, à appliquer avec la même méthode une fois l'opération autorisée.
