"""Contenus FR v2 des collections zèbre (description, accroche, guide, FAQ).

Sources : analyse SERP/concurrents du 05/10/2026 (analyse-v2.md), faits produit vérifiés
dans templates/product.painting.json et templates/product.poster.json du thème, options
réelles des produits (/products/<handle>.js). Écrit fr.json à côté de ce script.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).parent

# ---------------------------------------------------------------- TABLEAU ZÈBRE (toile)

T_DESCRIPTION = """<p>Le tableau zèbre apporte à un mur ce que peu de motifs savent offrir : du rythme, du contraste et une élégance immédiate. Notre collection réunit des toiles sélectionnées et retouchées à la main par notre studio créatif de Toulouse : œuvres noir et blanc d'inspiration photographique (regard sauvage, zèbre majestueux sur fond sombre, zèbre sous la neige), zèbres colorés et arc-en-ciel dans l'esprit pop art, motifs tribaux aux ocres cuivrés, maternité africaine, street art et aquarelle pour chambre d'enfant.</p>
<p>Chaque tableau est imprimé à la demande en Europe sur une toile polyester de 285 g/m², avec des encres haute pigmentation garanties 75 ans, puis tendu à la main sur un châssis en bois massif de 3 cm. Du 30 x 40 au 90 x 120 cm, et jusqu'au 100 x 100 cm pour les œuvres carrées, avec cinq finitions de bordure et un cadre en option. Au salon au-dessus du canapé, dans une chambre, une entrée ou un bureau, le zèbre s'accorde avec tous les styles. Livraison offerte.</p>"""

T_INTRO = "Graphique par nature, le zèbre offre à un mur ce que peu d'animaux savent donner : du rythme, du contraste et une élégance immédiate. Notre collection de tableaux zèbre réunit des œuvres sélectionnées et retouchées à la main par notre studio de Toulouse, du portrait noir et blanc au zèbre arc-en-ciel, pour donner à votre intérieur le caractère que vous imaginiez."

T_GUIDE = """<h2>Le tableau zèbre, un motif qui structure le mur</h2>
<p>Il y a des murs qui attendent depuis longtemps. On sent qu'il leur manque quelque chose, sans savoir quoi. Souvent, la réponse tient en quelques lignes franches : celles du zèbre. Ses rayures dessinent une architecture à elles seules ; elles guident le regard, rythment l'espace et apportent ce contraste noir et blanc qui s'accorde avec presque tout, avec en prime un parfum de savane africaine. Un tableau zèbre donne au mur une ligne, un rythme, une présence.</p>
<p>Chez MyselfMonArt, studio créatif fondé à Toulouse en 2022, chaque œuvre est sélectionnée puis retouchée à la main par notre direction artistique : la profondeur des noirs, la finesse du pelage, la justesse des couleurs. Rien n'entre dans la collection par hasard, et c'est ce soin que vous retrouvez une fois la toile accrochée chez vous.</p>
<h2>Quel tableau zèbre choisir ?</h2>
<p>Tout commence par l'atmosphère que vous souhaitez installer. Notre collection se découvre en quatre familles.</p>
<h3>Le tableau zèbre noir et blanc, une valeur intemporelle</h3>
<p>C'est le choix qui traverse les modes et les déménagements. Le <a href="/products/cadre-moderne-zebre-regard-sauvage-en-nuances">regard sauvage en noir et blanc</a> joue le gros plan hypnotique, au plus près de l'œil et des rayures. Le <a href="/products/tableau-sur-toile-zebre-majestueux-portrait-noir-et-blanc-graphique">zèbre majestueux sur fond noir</a> sculpte la lumière comme un portrait de studio, avec ses reflets dorés. Et le <a href="/products/tableau-sur-toile-zebre-sous-la-neige-hivernale">zèbre sous la neige hivernale</a> raconte une rencontre inattendue, tout en douceur. Dans une pièce déjà colorée, un tableau zèbre noir et blanc ramène le calme ; dans un intérieur neutre, il apporte du caractère sans jamais crier. Ce dialogue du noir et du blanc a d'ailleurs inspiré les plus grands : Victor Vasarely en a notamment fait le sujet de son tableau <em>Zèbres</em> (1937), souvent cité parmi les toutes premières œuvres de l'op art.</p>
<h3>Le zèbre coloré, l'énergie pop</h3>
<p>Changement d'humeur avec la couleur. Le <a href="/products/toile-design-zebre-colore-vitalite-arc-en-ciel">zèbre arc-en-ciel</a> déploie une matière picturale généreuse, tandis que le <a href="/products/toile-moderne-zebre-multicolore-rayures-arc-en-ciel">zèbre multicolore au galop</a> fait entrer le mouvement dans la pièce. De quoi offrir à un salon neutre le point de couleur qui lui manquait. Pour prolonger cet esprit, explorez nos <a href="/collections/tableau-pop-art">tableaux pop art</a>.</p>
<h3>L'esprit africain et ethnique</h3>
<p>Pour un intérieur chaleureux aux tons terre, le <a href="/products/tableau-sur-toile-zebre-motifs-tribaux-africains-et-ocres-cuivres">zèbre aux motifs tribaux et ocres cuivrés</a> réchauffe le mur de ses nuances de cuivre. La <a href="/products/tableau-africain-maternite-femme-et-enfant-aux-motifs-zebres-graphiques">maternité africaine aux motifs zébrés</a>, elle, fait de la rayure un vêtement, dans une illustration tendre qui parle de transmission. Deux œuvres qui dialoguent naturellement avec nos <a href="/collections/tableau-africain">tableaux africains</a> ; pour composer toute une pièce dans cet esprit, notre <a href="/blogs/tableau-salon/voyagez-depuis-votre-salon-guide-pratique-pour-une-decoration-africaine-reussi-et-abordable">guide de la décoration africaine</a> vous donne les clés.</p>
<h3>Street art et aquarelle, le zèbre qui fait sourire</h3>
<p>L'<a href="/products/tableau-street-art-elephant-couronne-hybride-zebre-graffiti-urbain">éléphant couronné aux rayures de zèbre</a> mêle graffiti et humour, pour un loft, un bureau ou une chambre d'adolescent qui assume son côté urbain. D'autres œuvres de ce style sont à découvrir parmi nos <a href="/collections/tableau-street-art">tableaux street art</a>. Le <a href="/products/toile-deco-zebre-rieur-ambiance-feerique">zèbre rieur à l'aquarelle</a>, aux tons doux, apporte quant à lui une note tendre et joyeuse à une chambre d'enfant.</p>
<h2>Un tableau zèbre dans chaque pièce</h2>
<h3>Au salon, au-dessus du canapé</h3>
<p>C'est l'emplacement roi. Visez une œuvre, ou un duo, qui couvre de la moitié aux deux tiers de la largeur du canapé, accrochée 15 à 25 cm au-dessus du dossier. En repère : un 60 x 80 cm pour un canapé deux places, un 75 x 100 cm pour un trois places, un 90 x 120 cm pour un grand mur. Vous hésitez entre une pièce unique et une composition ? Deux toiles côte à côte, ou un trio aligné, composent un mur-galerie très réussi. D'autres idées parmi nos <a href="/collections/tableau-salon">tableaux pour le salon</a>.</p>
<h3>Dans la chambre</h3>
<p>Au-dessus de la tête de lit, un tableau zèbre noir et blanc installe une élégance feutrée, propice au repos. Le zèbre sous la neige, avec sa lumière douce, accompagne particulièrement bien les fins de journée. Découvrez aussi nos <a href="/collections/tableau-chambre">tableaux pour la chambre</a>.</p>
<h3>Dans l'entrée, le couloir ou le bureau</h3>
<p>Dans une entrée, un portrait vertical accueille le regard dès le seuil : c'est la première phrase de votre intérieur. Au bureau, les lignes nettes d'un zèbre noir et blanc structurent l'espace sans distraire, et composent un très bel arrière-plan lors de vos visioconférences. Découvrez nos <a href="/collections/tableau-entree-couloir">tableaux pour l'entrée et le couloir</a> et nos <a href="/collections/tableau-bureau">tableaux pour le bureau</a>.</p>
<h3>Dans une chambre d'enfant</h3>
<p>Les enfants reconnaissent le zèbre au premier coup d'œil. Le zèbre rieur à l'aquarelle y apporte de la douceur, un zèbre arc-en-ciel de la gaieté, et une version plus graphique accompagnera l'enfant en grandissant. D'autres idées dans nos <a href="/collections/tableau-chambre-enfant">tableaux pour chambre d'enfant</a>.</p>
<h2>Avec quoi associer un tableau zèbre ?</h2>
<p>Le noir et le blanc du zèbre sont des neutres absolus. Ils s'accordent avec le bois clair, le lin, le rotin, la jute ou le cuir cognac, et trouvent leur place dans un intérieur scandinave, japandi, bohème ou industriel. Pour un esprit safari chic, associez-le à des plantes vertes, à un tapis en fibres naturelles et à quelques touches de terracotta. Les palettes douces lui vont aussi très bien : sur un mur beige, sable ou grège, ses rayures prennent un relief magnifique. Le soir, une lumière rasante ou un spot orienté souligne le grain de la toile.</p>
<p>Le zèbre aime aussi la compagnie. Entourez-le d'autres animaux de la savane, comme le lion et sa prestance (découvrez notre <a href="/collections/tableau-lion">tableau lion</a>), ou de son cousin le cheval, avec notre <a href="/collections/tableau-cheval">tableau cheval</a>. Pour d'autres inspirations, lisez notre article <a href="/blogs/tableau-salon/quels-tableaux-animaux-pour-decorer-votre-interieur">quels tableaux animaux pour décorer votre intérieur</a> ou notre <a href="/blogs/tableau-salon/le-guide-ultime-pour-une-ambiance-scandinave-couleurs-meubles-et-accessoires">guide de l'ambiance scandinave</a>.</p>
<h2>Ce que symbolise le zèbre</h2>
<p>Le zèbre parle d'équilibre : le noir et le blanc s'y répondent sans jamais s'effacer. Il parle aussi de singularité, puisque les rayures de chaque zèbre sont uniques, comme une empreinte digitale. Animal de troupeau, il évoque enfin la liberté vécue ensemble et le lien aux autres.</p>
<p>En France, le zèbre est aussi devenu l'emblème affectueux des personnes à haut potentiel intellectuel (HPI), depuis que la psychologue Jeanne Siaud-Facchin a popularisé cette image : un être singulier, qui se fond dans le décor tout en s'en distinguant, et que l'on n'apprivoise pas. Offrir un tableau zèbre à quelqu'un qui s'y reconnaît, c'est lui adresser un clin d'œil tendre et complice.</p>
<h3>Pourquoi le zèbre a-t-il des rayures ?</h3>
<p>La question intrigue les naturalistes depuis Darwin et Wallace. Plusieurs pistes coexistent : brouiller la vue des prédateurs quand le troupeau se déplace, aider à réguler la chaleur et, selon les études les plus récentes, décourager les mouches piqueuses. Une chose est sûre : ce motif, l'un des plus reconnaissables du règne animal, est un cadeau pour les artistes.</p>
<h2>Formats, finitions et cadre</h2>
<p>Un tableau, ce n'est pas qu'une image imprimée : c'est une matière que vous regarderez chaque jour pendant des années. Voici ce que nous y mettons.</p>
<ul>
<li><strong>Toile polyester 285 g/m²</strong> : une toile dense, à la texture légèrement grainée, qui restitue la finesse du pelage et la profondeur des noirs.</li>
<li><strong>Encres haute pigmentation</strong> : des couleurs riches et profondes, garanties 75 ans sans altération.</li>
<li><strong>Châssis en bois massif</strong> : chaque toile est tendue à la main, sur 3 cm de profondeur, pour un relief élégant.</li>
<li><strong>Cinq finitions de bordure</strong> : blanche, noire, étirée, miroir ou pliée, pour habiller les côtés de la toile à votre goût.</li>
<li><strong>Cadre en option</strong> : blanc, noir mat, argent ancien, chêne clair ou noyer, livré monté et prêt à accrocher.</li>
<li><strong>Formats</strong> : du 30 x 40 au 90 x 120 cm, en portrait ou en paysage selon l'œuvre, et jusqu'au 100 x 100 cm pour les œuvres carrées.</li>
</ul>
<p>Besoin d'aide pour la dimension ? Notre guide <a href="/blogs/tableau-cuisine/quelle-taille-de-tableau-choisir">quelle taille de tableau choisir</a> et nos <a href="/blogs/tableau-cuisine/accrocher-un-tableau-en-toute-securite-nos-solutions-et-astuces-pratiques">astuces pour accrocher un tableau en toute sécurité</a> répondent à vos questions. Et pour que votre toile garde son éclat, voici <a href="/blogs/tableau-salon/comment-entretenir-vos-tableaux-le-guide-simple-matiere-par-matiere">comment entretenir votre tableau</a>.</p>
<h2>Tableau zèbre ou poster zèbre ?</h2>
<p>La toile s'installe comme une pièce maîtresse, pensée pour durer : elle a de la matière, du relief, une présence que l'on ressent dès l'entrée dans la pièce. Le poster, tirage photo sur papier, mise sur la légèreté et la souplesse : idéal pour une première déco, un cadeau ou un mur que l'on aime renouveler. Plusieurs de nos zèbres existent dans les deux versions : découvrez notre collection jumelle <a href="/collections/posters-affiches-zebre">Poster &amp; Affiche Zèbre</a>.</p>
<h2>Pourquoi choisir MyselfMonArt ?</h2>
<p>Depuis 2022, plus de 1 015 tableaux sont sortis de nos cartons pour rejoindre des salons, des chambres et des couloirs un peu trop nus. Nous ne cherchons pas à tout proposer : plus de mille œuvres n'ont pas passé le filtre de notre direction artistique, pour 700 référencées aujourd'hui. Chaque toile est conçue en France, imprimée à la demande en Europe et expédiée dans un emballage renforcé. La livraison est offerte, vous disposez de 14 jours pour changer d'avis, et le paiement en 3 fois sans frais avec Klarna est possible dès 50 € d'achat. Une question sur un format ? Notre équipe, à Toulouse, vous répond au 09 60 44 61 50.</p>
<p>Le zèbre appartient à une grande famille : prolongez votre visite avec nos <a href="/collections/tableau-animaux">tableaux animaux</a>, l'élégance intemporelle du <a href="/collections/tableau-noir-et-blanc">tableau noir et blanc</a> ou les motifs de nos <a href="/collections/tableau-ethnique">tableaux ethniques</a>.</p>
<p>Avec soin, — Hayate &amp; l'équipe MyselfMonArt</p>"""

T_FAQ = [
    {"q": "Quel tableau zèbre choisir pour mon intérieur ?",
     "a": "<p>Partez de l'ambiance que vous recherchez. Le noir et blanc, comme le regard sauvage ou le zèbre sous la neige, apporte une élégance sobre qui s'intègre partout. Le zèbre arc-en-ciel ou multicolore dynamise une pièce neutre. Les motifs tribaux aux ocres cuivrés réchauffent un intérieur bohème ou ethnique, et le zèbre rieur à l'aquarelle adoucit une chambre d'enfant. Choisissez ensuite le format selon le mur à habiller.</p>"},
    {"q": "Tableau zèbre noir et blanc ou coloré : lequel choisir ?",
     "a": "<p>Le noir et blanc est le choix le plus intemporel : il apaise une pièce déjà chargée en couleurs et s'accorde avec tous les styles, du scandinave à l'industriel. Le zèbre coloré, dans l'esprit pop art, devient le point d'énergie d'un intérieur neutre ou d'une chambre d'enfant. Une astuce : reprenez une teinte de la toile dans un coussin ou un plaid pour créer une vraie cohérence.</p>"},
    {"q": "Quelle taille de tableau zèbre choisir au-dessus d'un canapé ?",
     "a": "<p>Visez une œuvre, ou un duo, qui couvre de la moitié aux deux tiers de la largeur du canapé, accrochée 15 à 25 cm au-dessus du dossier. En repère : un 60 x 80 cm pour un canapé deux places, un 75 x 100 cm pour un trois places et un 90 x 120 cm pour un grand mur. Vous pouvez aussi aligner deux ou trois toiles de même format pour un effet galerie.</p>"},
    {"q": "Avec quelle décoration associer un tableau zèbre ?",
     "a": "<p>Le noir et blanc du zèbre se marie avec le bois clair, le lin, le rotin, la jute ou le cuir cognac. Il trouve sa place dans un intérieur scandinave, japandi, bohème ou industriel, et révèle tout son relief sur un mur beige, sable ou grège. Pour un esprit safari chic, ajoutez des plantes vertes, un tapis en fibres naturelles et quelques touches de terracotta.</p>"},
    {"q": "Que symbolise le zèbre en décoration ?",
     "a": "<p>Le zèbre symbolise l'équilibre, car le noir et le blanc s'y répondent sans s'effacer, et la singularité : les rayures de chaque zèbre sont uniques, comme une empreinte. Animal de troupeau, il évoque aussi la liberté et le lien aux autres. En France, il est enfin devenu l'emblème affectueux des personnes à haut potentiel intellectuel (HPI) : une très belle idée de cadeau pour qui s'y reconnaît.</p>"},
    {"q": "Un tableau zèbre convient-il à une chambre d'enfant ?",
     "a": "<p>Oui : avec ses rayures, le zèbre est un animal que les tout-petits repèrent tout de suite. Le zèbre rieur à l'aquarelle, aux tons doux, apporte une touche tendre et joyeuse à une chambre de bébé ou d'enfant. Pour une chambre qui grandit avec l'enfant, un zèbre plus graphique ou multicolore fonctionne très bien aussi. Retrouvez d'autres idées dans notre collection <a href='/collections/tableau-chambre-enfant'>Tableau Chambre Enfant</a>.</p>"},
    {"q": "Quelle est la qualité de vos toiles ?",
     "a": "<p>Nos tableaux sont imprimés sur une toile polyester de 285 g/m² avec des encres haute pigmentation, garanties 75 ans sans altération. Chaque toile est tendue à la main sur un châssis en bois massif de 3 cm de profondeur, avec cinq finitions de bordure au choix. Ils sont conçus en France, imprimés à la demande en Europe et livrés montés sur leur châssis. La livraison est offerte.</p>"},
    {"q": "Vos tableaux zèbre existent-ils aussi en poster ?",
     "a": "<p>Oui, plusieurs de nos zèbres existent aussi en poster, comme le regard sauvage, le zèbre sous la neige, le zèbre arc-en-ciel ou les motifs tribaux. Le poster est un tirage photo léger et plus accessible, livré seul, à encadrer vous-même, ou avec cadre et prêt à accrocher. Retrouvez-les dans notre collection <a href='/collections/posters-affiches-zebre'>Poster &amp; Affiche Zèbre</a>.</p>"},
]

# ------------------------------------------------------- POSTER & AFFICHE ZÈBRE (papier)

P_DESCRIPTION = """<p>Le poster zèbre fait entrer chez vous ce que la savane a de plus graphique : des rayures qui structurent un mur, un contraste noir et blanc qui s'accorde avec tout, et une touche d'évasion africaine. Notre collection d'affiches zèbre réunit des visuels sélectionnés et retouchés à la main par notre studio créatif de Toulouse : regard sauvage et zèbre sous la neige en noir et blanc, portrait aux rayures dorées, zèbre arc-en-ciel, motifs tribaux aux ocres cuivrés et maternité africaine.</p>
<p>Chaque poster est imprimé à la demande en haute définition sur un vrai papier photo, bord à bord, du 30 x 40 au 90 x 120 cm. Sans cadre, il se glisse dans un cadre standard du commerce ; avec cadre (jusqu'au 75 x 100 cm), il arrive prêt à accrocher, en blanc, noir mat, chêne clair ou noyer. Seule ou en mur-galerie, au salon, dans une chambre ou une chambre d'enfant, l'affiche zèbre se renouvelle au gré de vos envies. Livraison offerte.</p>"""

P_INTRO = "Il y a ce mur qui attend, et cette envie d'y voir enfin quelque chose de fort. Le poster zèbre y répond avec ce que la savane a de plus graphique : des rayures qui structurent l'espace, du noir et blanc photographique aux éclats arc-en-ciel. Une affiche légère, à encadrer ou à composer en mur-galerie, qui change l'humeur d'une pièce en un geste."

P_GUIDE = """<h2>Le poster zèbre, des rayures qui changent un mur</h2>
<p>Un mur nu se remarque plus qu'on ne le croit. Il suffit pourtant d'une affiche pour qu'il prenne du relief, et peu d'animaux le font aussi bien que le zèbre. Ses rayures tracent des lignes franches qui guident l'œil, et son noir et blanc s'accorde avec presque tout. En format poster, ce graphisme gagne en légèreté : on l'encadre en quelques minutes, on le déplace, on le renouvelle au fil des saisons, sans jamais renoncer à l'élégance.</p>
<p>Chez MyselfMonArt, studio créatif fondé à Toulouse en 2022, chaque visuel est sélectionné puis retouché à la main par notre direction artistique : les contrastes, la lumière, la justesse des couleurs. Votre affiche est ensuite imprimée à la demande, en haute définition, sur un vrai papier photo, bord à bord, pour un rendu plein cadre net et lumineux.</p>
<h2>Que symbolise le zèbre ?</h2>
<p>Si le zèbre plaît tant en décoration, c'est aussi pour ce qu'il raconte. Ses rayures noires et blanches s'équilibrent sans jamais s'effacer. Elles sont uniques d'un individu à l'autre, comme une signature. Et ce grand voyageur de la savane vit en troupeau, image d'une liberté partagée. Une affiche zèbre, c'est un peu de cette harmonie des contraires accrochée au mur, et une invitation au voyage.</p>
<h2>Quel poster zèbre choisir ?</h2>
<h3>L'affiche zèbre noir et blanc, l'élégance photographique</h3>
<p>Le noir et blanc ne se démode pas, et rien ne sublime mieux le motif. Le <a href="/products/poster-zebre-regard-sauvage-en-noir-et-blanc">regard sauvage en noir et blanc</a> vous plonge au cœur du pelage, dans un face-à-face saisissant. Le <a href="/products/poster-zebre-sous-la-neige-rencontre-inattendue-en-plein-hiver">zèbre sous la neige</a> fige un instant d'hiver suspendu. Et le <a href="/products/poster-affiche-zebre-portrait-intime-aux-rayures-dorees">portrait intime aux rayures dorées</a> se détache en clair-obscur sur fond noir. Dans une pièce chargée de couleurs, un poster zèbre noir et blanc pose le regard ; dans un décor épuré, il signe le mur. Ce jeu optique a d'ailleurs inspiré Victor Vasarely, dont le tableau <em>Zèbres</em> (1937) est souvent présenté comme l'une des toutes premières œuvres de l'op art. Il se marie aussi naturellement avec nos autres <a href="/collections/posters-affiches-noir-et-blanc">posters noir et blanc</a>.</p>
<h3>La couleur, pour une énergie pop</h3>
<p>La couleur, elle, fait souffler un vent pop. Le <a href="/products/poster-zebre-arc-en-ciel-rayures-multicolores-pleines-denergie">zèbre arc-en-ciel</a> déroule des rayures multicolores pleines d'énergie, qui réveillent un mur blanc comme une chambre d'enfant. Pour prolonger cet esprit, découvrez nos <a href="/collections/posters-affiches-pop-art">posters pop art</a>.</p>
<h3>L'esprit africain, pour une chaleur graphique</h3>
<p>Le <a href="/products/poster-zebre-motifs-tribaux-africains-et-ocres-cuivres">zèbre aux motifs tribaux et ocres cuivrés</a> réchauffe le mur de ses tons terre, tandis que la <a href="/products/poster-maternite-africaine-femme-et-enfant-aux-motifs-zebres">maternité africaine aux motifs zébrés</a> fait de la rayure un vêtement, dans une illustration tendre et graphique. Associez-les à nos <a href="/collections/posters-affiches-africain">posters et affiches africains</a>, et puisez des idées d'aménagement dans notre <a href="/blogs/tableau-salon/voyagez-depuis-votre-salon-guide-pratique-pour-une-decoration-africaine-reussi-et-abordable">guide de la décoration africaine</a>.</p>
<h2>Encadrer votre affiche zèbre</h2>
<p>Deux options s'offrent à vous. <strong>Sans cadre</strong>, vous recevez l'affiche seule, à glisser dans un cadre standard du commerce aux mêmes dimensions, ou dans un cadre sur mesure pour les grands formats : fin et noir pour un rendu galerie, bois clair pour plus de douceur. <strong>Avec cadre</strong>, elle arrive prête à accrocher, en quatre finitions : blanc, noir mat, chêne clair ou noyer, en 30 x 40, 60 x 80 ou 75 x 100 cm. L'option <strong>contour blanc</strong> ajoute une marge autour du visuel, à la manière d'un passe-partout : les rayures respirent et l'ensemble gagne en raffinement.</p>
<p>Vous préférez l'esprit atelier, sans cadre du tout ? Une affiche se suspend aussi entre deux baguettes porte-affiche en bois, ou à l'aide de pinces discrètes sur un câble tendu. Pour un grand format, répartissez bien les points d'accroche : nos <a href="/blogs/tableau-cuisine/accrocher-un-tableau-en-toute-securite-nos-solutions-et-astuces-pratiques">astuces pour accrocher en toute sécurité</a> vous y aident.</p>
<h2>Où accrocher un poster zèbre ?</h2>
<ul>
<li><strong>Au salon</strong> : au-dessus du canapé, visez une affiche, ou une composition, qui couvre de la moitié aux deux tiers de la largeur du meuble. Un 75 x 100 ou un 90 x 120 cm installe une vraie présence. D'autres idées parmi nos <a href="/collections/posters-affiches-salon">posters pour le salon</a>.</li>
<li><strong>Dans la chambre</strong> : une version noir et blanc au-dessus de la tête de lit apporte une élégance feutrée, propice au calme. Découvrez nos <a href="/collections/posters-affiches-chambre">posters pour la chambre</a>.</li>
<li><strong>Dans une chambre d'enfant</strong> : les enfants reconnaissent le zèbre au premier coup d'œil. L'affiche arc-en-ciel ou la tendre maternité africaine y trouvent leur place, comme nos <a href="/collections/posters-affiches-chambre-enfant">posters pour chambre d'enfant</a>.</li>
<li><strong>Dans l'entrée ou le couloir</strong> : un format vertical donne le ton dès le seuil. Découvrez nos <a href="/collections/posters-affiches-entree-couloir">posters pour l'entrée et le couloir</a>.</li>
<li><strong>Au bureau</strong> : les lignes nettes d'un zèbre noir et blanc structurent l'espace sans distraire. Découvrez nos <a href="/collections/posters-affiches-bureau">posters pour le bureau</a>.</li>
<li><strong>Dans une salle de bain ou des toilettes</strong> : la petite touche graphique, et un brin d'humour, qui surprend. Choisissez un mur bien ventilé, à l'abri des projections d'eau.</li>
</ul>
<p>Pour trouver la bonne dimension, les repères de notre guide <a href="/blogs/tableau-cuisine/quelle-taille-de-tableau-choisir">quelle taille de tableau choisir</a> valent aussi pour les affiches.</p>
<h2>Composer un mur-galerie autour du zèbre</h2>
<p>Le poster est fait pour le mur-galerie. Partez d'une affiche zèbre en pièce centrale, puis entourez-la de formats qui lui répondent : d'autres animaux de la savane, comme le <a href="/collections/posters-affiches-lion">poster lion</a>, des <a href="/collections/posters-affiches-nature">affiches nature</a> ou des visuels noir et blanc. Trois règles suffisent :</p>
<ul>
<li>un fil conducteur : la palette (noir, blanc, ocre) ou le thème (la savane) ;</li>
<li>une même famille de cadres, ou deux finitions qui se répondent, comme le noir mat et le chêne clair ;</li>
<li>des espacements réguliers, de 5 à 8 cm entre deux affiches.</li>
</ul>
<p>Disposez d'abord vos affiches au sol pour trouver l'équilibre. Un duo symétrique au-dessus d'un lit, un trio aligné au-dessus d'un canapé ou une grille de six affiches sur un grand mur : à vous de choisir l'ampleur.</p>
<h2>Poster zèbre ou tableau sur toile ?</h2>
<p>Le poster mise sur la souplesse : un tirage photo léger et accessible, idéal pour une première déco, un cadeau, une location ou un mur que l'on aime faire évoluer. La toile, tendue à la main sur un châssis en bois massif, s'installe comme une pièce maîtresse pensée pour durer, avec la matière et la profondeur d'une œuvre. L'un n'exclut pas l'autre : ce sont deux façons d'habiter un mur. Plusieurs de nos zèbres existent dans les deux versions : retrouvez-les dans notre collection <a href="/collections/tableau-zebre">Tableau Zèbre</a>.</p>
<h2>Pourquoi choisir MyselfMonArt ?</h2>
<p>Notre direction artistique écarte plus de visuels qu'elle n'en garde : plus de mille n'ont pas passé son filtre, pour 700 œuvres référencées aujourd'hui. Chaque affiche est ensuite imprimée pour vous, à la demande, en Europe, puis expédiée avec soin. Livraison offerte, 14 jours pour changer d'avis, paiement en 3 fois sans frais avec Klarna dès 50 € d'achat : tout est pensé pour que vous choisissiez l'esprit tranquille. Un doute sur un format ou un cadre ? Appelez-nous au 09 60 44 61 50 : une vraie personne de notre équipe toulousaine vous conseille.</p>
<p>Envie de prolonger le voyage ? Explorez nos <a href="/collections/posters-affiches-animaux">posters et affiches animaux</a>, l'élégance du <a href="/collections/posters-affiches-cheval">poster cheval</a> ou l'ensemble de nos <a href="/collections/posters-affiches">posters et affiches</a>. Et pour d'autres idées, lisez notre article <a href="/blogs/tableau-salon/quels-tableaux-animaux-pour-decorer-votre-interieur">quels tableaux animaux pour décorer votre intérieur</a>.</p>
<p>Avec soin, — Hayate &amp; l'équipe MyselfMonArt</p>"""

P_FAQ = [
    {"q": "Que symbolise le zèbre en décoration ?",
     "a": "<p>Le zèbre symbolise l'équilibre, car ses rayures noires et blanches se répondent sans s'effacer, et la singularité : les rayures de chaque zèbre sont uniques, comme une empreinte. Animal de troupeau, il évoque aussi la liberté et le lien aux autres. En décoration, une affiche zèbre apporte un contraste graphique apaisant et une touche d'évasion vers la savane africaine, tout en restant très facile à intégrer.</p>"},
    {"q": "Poster zèbre ou tableau sur toile : que choisir ?",
     "a": "<p>Choisissez le poster pour la souplesse : un tirage photo léger et accessible, facile à encadrer et à renouveler au gré de vos envies. Préférez la toile pour une pièce maîtresse durable, tendue à la main sur un châssis en bois massif. Plusieurs de nos zèbres existent dans les deux versions : retrouvez les toiles dans notre collection <a href='/collections/tableau-zebre'>Tableau Zèbre</a>.</p>"},
    {"q": "Comment encadrer une affiche zèbre ?",
     "a": "<p>Sans cadre, l'affiche se glisse dans un cadre standard du commerce aux mêmes dimensions, ou dans un cadre sur mesure pour les grands formats. Avec cadre, elle arrive prête à accrocher, en blanc, noir mat, chêne clair ou noyer, du 30 x 40 au 75 x 100 cm. L'option contour blanc ajoute une marge autour du visuel, à la manière d'un passe-partout, pour un effet galerie qui laisse respirer les rayures.</p>"},
    {"q": "Comment accrocher un poster au mur sans cadre ?",
     "a": "<p>Pour un esprit atelier, suspendez votre affiche entre deux baguettes porte-affiche en bois, ou fixez-la avec des pinces discrètes sur un câble tendu. Ces solutions ne percent pas le papier et permettent de changer facilement d'affiche. Pour un rendu plus net et plus durable, surtout en grand format, l'encadrement reste la meilleure option.</p>"},
    {"q": "Quelle taille de poster zèbre choisir ?",
     "a": "<p>Nos affiches existent en 30 x 40, 60 x 80, 75 x 100 et 90 x 120 cm. Visez de la moitié aux deux tiers de la largeur du meuble au-dessus duquel vous accrochez : un 75 x 100 ou un 90 x 120 cm au-dessus d'un canapé, un 60 x 80 cm au-dessus d'une console. Le 30 x 40 cm est idéal en mur-galerie. Un doute ? Découpez un carton aux dimensions et posez-le au mur.</p>"},
    {"q": "Une affiche zèbre convient-elle à une chambre d'enfant ?",
     "a": "<p>Oui, d'autant que les enfants reconnaissent le zèbre au premier coup d'œil. Le zèbre arc-en-ciel apporte de la gaieté, la maternité africaine aux motifs zébrés une douceur tendre, et une version noir et blanc accompagnera l'enfant en grandissant. Associez-la à d'autres animaux de la savane pour créer un petit safari mural. D'autres idées dans nos <a href='/collections/posters-affiches-chambre-enfant'>posters pour chambre d'enfant</a>.</p>"},
    {"q": "Peut-on accrocher une affiche zèbre dans une salle de bain ?",
     "a": "<p>Oui, c'est même une idée originale pour apporter une touche graphique et un brin d'humour à une salle de bain ou à des toilettes. Comme pour tout tirage sur papier, choisissez un mur bien ventilé, à l'abri des projections d'eau et de la vapeur directe de la douche. La version encadrée donne un rendu plus net et plus soigné dans ces petites pièces.</p>"},
    {"q": "Quelle est la qualité de vos posters ?",
     "a": "<p>Chaque affiche est imprimée à la demande en haute définition, sur un vrai papier photo, bord à bord pour un rendu plein cadre. Les couleurs sont éclatantes et fidèles, les détails nets, ce qui met en valeur la finesse des rayures. Nos visuels sont sélectionnés et retouchés à la main par notre studio de Toulouse, conçus en France et imprimés en Europe. La livraison est offerte.</p>"},
]

import re

NB, NNB = "\u00a0", "\u202f"


def typo(html):
    """Typographie française sur les seuls nœuds texte (jamais dans les balises)."""
    parts = re.split(r"(<[^>]+>)", html)
    for i, t in enumerate(parts):
        if i % 2:
            continue
        t = t.replace("'", "\u2019")
        t = re.sub(r" ([;?!])", NNB + r"\1", t)
        t = re.sub(r" :", NB + ":", t)
        t = t.replace("« ", "«" + NB).replace(" »", NB + "»")
        t = re.sub(r"(\d) x (\d)", r"\1" + NB + "×" + NB + r"\2", t)
        t = re.sub(r"(\d) (cm|€|g/m²|ans)\b", r"\1" + NB + r"\2", t)
        t = re.sub(r"(\d) (\d{3})\b", r"\1" + NNB + r"\2", t)
        t = t.replace("09 60 44 61 50", NB.join(["09", "60", "44", "61", "50"]))
        parts[i] = t
    return "".join(parts)


def typo_all(c):
    c = dict(c)
    for k in ("description_html", "intro", "guide"):
        c[k] = typo(c[k])
    c["faq"] = [{"q": typo(f["q"]), "a": typo(f["a"])} for f in c["faq"]]
    return c


data = {
    "tableau-zebre": {"gid": "gid://shopify/Collection/682824630619",
                      "description_html": T_DESCRIPTION, "intro": T_INTRO,
                      "guide": T_GUIDE, "faq": T_FAQ},
    "posters-affiches-zebre": {"gid": "gid://shopify/Collection/682801660251",
                               "description_html": P_DESCRIPTION, "intro": P_INTRO,
                               "guide": P_GUIDE, "faq": P_FAQ},
}
data = {k: typo_all(v) for k, v in data.items()}
(HERE / "fr.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print("fr.json écrit")
