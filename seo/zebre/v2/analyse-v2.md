# Collections zèbre v2 : analyse et parti pris rédactionnel (05/10/2026)

Pourquoi une v2 : Walid a jugé les descriptions « très pauvres ». Cette analyse remet à plat ce qui s'affiche réellement, ce que Google récompense et ce que la cible attend. Les contenus sont dans [`build_fr.py`](./build_fr.py) (source) et [`fr.json`](./fr.json) (généré).

## 1. Ce que voit réellement l'internaute (et Google)

- Quand `custom.guide` existe, `main-collection-banner` **n'affiche pas** `collection.description` (voir `sections/main-collection-banner.liquid` du thème). Le texte visible est porté par `snippets/collection-editorial-auto.liquid` :
  - le H1 ;
  - l'accroche (`custom.intro`) ;
  - le guide (`custom.guide`), replié dans un `<details>` ;
  - les liens cocon ;
  - la FAQ (`custom.faq`), avec son JSON-LD FAQPage.
- Le champ Description de l'admin ne contenait qu'une phrase. Il est désormais réécrit en vrai résumé d'environ 160 mots. Il reste dormant sur le site, mais il sert ailleurs : admin, canaux de vente, et snippet `json-ld-collection` si la collection passe un jour sur un template qui l'appelle.
- **Le levier SEO réel est donc l'accroche, le guide et la FAQ.** Tout a été réécrit.

## 2. Cible et voix

- **Persona** (mission homepage, `STRATEGY.md`) : femmes de plus de 35 ans passionnées de décoration intérieure, sensibles au soin, à l'authenticité et à la curation plus qu'au volume.
- **Voix Hayate** (METHODOLOGY §4, copy de la home) :
  - vouvoiement ;
  - ton premium-émotionnel-cocon : scènes intimes (« le mur qui attend »), phrases courtes, aucune pédanterie ;
  - preuve par la curation (« plus de mille n'ont pas passé le filtre ») ;
  - faits matière glissés dans le récit ;
  - signature « Avec soin, — Hayate & l'équipe MyselfMonArt ».

## 3. SERP et concurrents (relevés du 05/10)

### « tableau zèbre »

- Relevé sur DuckDuckGo fr-fr, car Google bloque l'accès automatique. Les pages collection dominent (7 sur 10).
- Les concurrents :
  - n°1 Peinture Nature : environ 2 100 mots sous la grille, 5 H2 et 13 H3 ;
  - Recollection : environ 485 mots en H2 rédigés en questions ;
  - Museno : environ 500 mots ;
  - TabloDéco : environ 980 mots génériques.
- Médiane du top 5 : environ 485 mots. Modèle gagnant : de 800 à 1 500 mots sous la grille.
- Aucune FAQ et aucun FAQPage chez les 6 concurrents audités.
- Requêtes « noir et blanc » : surtout des fiches produit. Requêtes « cadre zèbre » : surtout des places de marché. « toile zèbre » relève de l'intention tissu, et n'est donc pas une cible.

### « poster zèbre » et « affiche zèbre »

- Relevé sur google.fr via un rendu, sur une SERP filtrée.
- « poster zèbre » : surtout des produits et des places de marché. « affiche zèbre » : des collections Juniqe (environ 490 mots, 4 H2), Posterlounge (0 mot) et ArtPhotoLimited (environ 20 mots).
- Aucune FAQ chez les concurrents.
- PAA réelles :
  - symbolique du zèbre (3 SERP sur 5) ;
  - accrocher un poster sans cadre ;
  - posters XXL.

### Autocomplétion Google FR (réelle)

- tableau zèbre : noir et blanc, pop art, multicolore, coloré, de dos, **vasarely**, banksy.
- affiche zèbre : **enfant**, **baignoire**, **toilette**, vogue.
- zèbre : signification, **symbole hpi**.
- savane : noir et blanc, chambre enfant.

### Vides concurrentiels occupés par la v2

1. FAQ avec FAQPage : 8 questions par page, réponses de 53 à 75 mots, citables par les IA.
2. Le sens du zèbre : symbolique (équilibre, singularité, troupeau). Pour la toile, l'angle HPI est traité avec tact comme idée cadeau.
3. Les références artistiques : les « Zèbres » de Vasarely (1937), demandés en autocomplétion et absents de toutes les pages concurrentes.
4. « Pourquoi le zèbre a-t-il des rayures ? » : contenu citable, GEO.
5. Un guide de tailles concret (repères en cm au-dessus du canapé), des palettes douces (beige, sable, grège) et l'esprit safari chic.
6. Pour le poster : encadrement, accrochage sans cadre, mur-galerie en trois règles, salle de bain et toilettes, chambre d'enfant.
7. Le récit de studio (Toulouse, curation, retouche à la main) et des faits matière chiffrés, face à des textes génériques.

## 4. Repère interne

| Page | Guide (mots) | Remarque |
|---|---:|---|
| tableau-africain (pos. 3,8) | 545 | meilleure position du site |
| tableau-couleur (pos. 5,5) | 458 | |
| tableau-salon | 929 | mission dédiée |
| tableau-zebre v1 | 593 | |
| **tableau-zebre v2** | **1 525** | dans la fourchette du modèle gagnant |
| posters-affiches-zebre v1 | 501 | |
| **posters-affiches-zebre v2** | **1 177** | plus de 2 fois Juniqe (n°1 « affiche zèbre ») |

L'UX est préservée, comme le demande METHODOLOGY §5bis : les produits restent au-dessus, le guide est replié et la FAQ est en accordéon. Le recoupement entre les deux guides n'est que de 2,7 % (8-grammes), ce qui évite le contenu dupliqué entre collections sœurs.

## 5. Faits utilisés (tous vérifiés)

- **Toile** (`templates/product.painting.json`) :
  - toile polyester 285 g/m², encres haute pigmentation garanties 75 ans ;
  - châssis en bois massif tendu à la main, 3 cm ;
  - toiles encadrées livrées montées, prêtes à accrocher ;
  - 14 jours, Klarna en 3 fois dès 50 €, conçu en France et imprimé en Europe.
- **Poster** (`templates/product.poster.json`) :
  - vrai papier photo HD de 250 g/m², impression bord à bord, contour blanc ;
  - cadres blanc, noir mat, chêne clair ou noyer.
- **Options réelles des produits** :
  - toiles du 30x40 au 90x120, carrés du 40x40 au 100x100, 5 bordures et 5 cadres ;
  - posters du 30x40 au 90x120, « Avec cadre » jusqu'au 75x100.
- **Marque** (copy de la home) : 2022, Toulouse, plus de 1 015 tableaux, plus de mille œuvres écartées, 09 60 44 61 50.
- Grammage du papier poster : **250 g/m²**, confirmé par Walid le 05/10. Il est désormais cité dans la description, le guide et la FAQ des deux collections, comme le font les concurrents. Il figure aussi dans les templates produit du thème.

## 6. Hors périmètre, à signaler

- Sur google.fr, une fiche poster MyselfMonArt sort avec une URL `/fr-ch/`. Il faut vérifier hreflang et canonique du marché suisse.
- Trustpilot, réglé le 05/10. La vraie note, relevée sur la page publique, est de **4,2/5 sur 86 avis**, avec le libellé officiel « Bien » (« Excellent » ne s'applique qu'à partir de 4,3). Le site affichait 4,5/5 sur la fiche poster, 4,1/5 sur la fiche personnalisée, 81 avis dans les blocs et le libellé « Excellent ». Tout a été aligné dans le thème : commit `396f4ec` de `myselfmonart_tw_theme`. Le détail figure dans [`../applied-log.md`](../applied-log.md).
