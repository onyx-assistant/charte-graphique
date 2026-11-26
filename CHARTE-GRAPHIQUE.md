# Charte graphique Onyx — v1.3

_Mise en place le 21 novembre 2026, à la demande de l'opérateur : un projet uniformisé, avec des codes et des normes professionnels, comme une production de jeu vidéo ou de film d'animation. Les technologies graphiques changeront ; ces codes, eux, ne changent pas._
_Dernière mise à jour : v1.3, 26 novembre 2026 — **la couleur officielle du personnage change le matin même** : la fourrure devient « **mohair cannelle miel clair** », valeur de référence mesurée `#AD6A3D`, finition mate (§§ 1, 3.2 et 8), décision de l'opérateur (~06:45 EST, choix nº 2 de la planche de comparaison des teintes produite le matin même, avec ordre de « repartir de zéro » sur cette base). Précédente : v1.2, 26 novembre 2026 — **nouvelle couleur officielle du personnage** : la fourrure devient « **mohair cannelle** » `#B06A35`, finition mate (§§ 1, 3.2 et 8), décision de l'opérateur (~00:51 EST, choix nº 5 de la planche palette « old school » du même jour), remplacée le matin même avant tout déploiement. La palette d'accent des surfaces (§ 3) est **inchangée**. Précédente : v1.1, 24 novembre 2026 — **remplacement de l'orange ombre** : `#812900` remplace `#8D2E0F` dans la palette (§ 3), décision de l'opérateur (candidate nº 4 de la planche de proposition du même jour) ; ratios de contraste de la § 16.1 recalculés pour la nouvelle valeur. v1.0, 22 novembre 2026 — intégration de la direction D3 « Une couleur par série » à fonds blancs comme **système d'identité unifié** (voir le journal des versions à la fin du document)._

## Portée

Cette charte s'applique à **toutes les surfaces** du projet Onyx :

- le compte et les dépôts GitHub (onyx-assistant / onyx-lab) ;
- la page web du projet (« Onyx — l'atelier ») **et la page de liens** ;
- l'avatar animé et les appels vidéo ;
- les vidéos produites ;
- les comptes et publications sur les réseaux sociaux (Instagram, TikTok, YouTube et toute plateforme à venir).

**Système d'identité unifié (v1.0)** : les mêmes normes, les mêmes logos, les mêmes images et les mêmes codes couleurs s'appliquent sur **toutes** les plateformes et tous les produits — y compris le système de séries à fonds blancs de la § 3.1. Aucune surface n'a son système propre.

## 1. Le personnage — référence canonique

- **Apparence verrouillée** : peluche mohair cannelle miel clair, oreilles rondes, yeux noirs ovales, petits sourcils courbés, museau doux, bouche en sourire simple et courbé.
- **Détails fixes** (ce qui fait reconnaître Onyx — la liste de contrôle de toute approbation, cf. porte P3 dans `docs/CONSTANCE-APPLICATION.md`) :
  1. pelage **mohair cannelle miel clair uni** (§ 3.2 ; valeur de référence mesurée sur le portrait canonique : `#AD6A3D`), tissu peluche **mat à poil court (~3 mm)** à coutures visibles — jamais de fourrure réaliste ;
  2. deux oreilles rondes et pleines, plantées en haut du crâne, symétriques ;
  3. yeux noirs ovales verticaux, « brodés » : ni blanc, ni reflet dessiné ;
  4. petits sourcils en arc courbé, au-dessus des yeux ;
  5. museau central doux et saillant, zone basse plus claire ;
  6. bouche = un seul trait courbé, sourire simple ;
  7. couture centrale verticale du torse.
- **Interdits (liste fermée)** : cornes, crocs ou dents, nez séparé ou narines ajoutées, blanc des yeux ou reflets « cartoon », poils longs ou fourrure réaliste, accessoires non approuvés, proportions modifiées, teinte de fourrure autre que le mohair cannelle miel clair officiel (§ 3.2). Toute exception reste ponctuelle et explicite (règle d'or nº 3).
- **Fichiers de référence** :
  - **référence couleur en vigueur (depuis le 26 novembre 2026 au matin)** : `references/onyx-canonique-cannelle-miel-clair.webp` (1600 × 1600, MD5 `cb2f81dc859b3e953a57a96c2d018005`) — portrait mohair cannelle miel clair validé par l'opérateur le 26 novembre 2026 (~06:45 EST) ; c'est la référence de toute production nouvelle ;
  - référence intermédiaire (mohair cannelle de la nuit du 26 novembre 2026, remplacée le matin même avant tout déploiement) : `references/onyx-canonique-mohair-cannelle.webp` (1600 × 1600, MD5 `b461d5152bd85d884b3ad11fd097b332`) — conservée comme trace historique, ne plus produire à partir d'elle ;
  - maître historique (ère orange, jusqu'au 25 novembre 2026) : `references/onyx-canonique.webp` (1600 × 1600, MD5 `2615852ff83d36e6468342cfbd5c8a8b8`, identique à l'avatar en vigueur dans l'application tant que la cascade de bascule n'est pas déployée) — conservé comme historique, ne plus produire à partir de lui ;
  - copie de travail : `assets/onyx-reference.png` (conversion PNG sans perte du même visuel, MD5 propre `8207b5db002014b7b0f52fc0a5baf9db`) ;
  - les deux sont inscrits au manifeste d'intégrité SHA-256 : `00_canonical/MANIFEST.sha256` (règle de version : `00_canonical/REGLE-VERSIONS.md`).
- Référence vidéo : snapshot `a0104323-eb74-4600-909c-51b69acffe89:z7bsw2` (vidéo Susanne v4). Toute nouvelle vidéo reprend ce snapshot, jamais un départ à zéro.

## 2. Expression et cadrage officiels

- **Expression d'identité** : celle du repos — regard vers l'avant, bouche fermée, petit sourire calme. C'est l'expression des photos de profil et de toute image d'identité.
- **Fond d'identité** : blanc pur.
- **Cadrage** : reculé, tête entière avec les oreilles et le haut du torse visibles, pas de cou visible — le cadrage de la bulle de conversation de l'application.

## 3. Palette (échantillonnée sur la photo de référence)

| Rôle | Valeur | Note |
|---|---|---|
| Orange lumière (pelage éclairé) | `#FC8B32` | ton dominant perçu |
| Orange médian | `#C95D1D` | zones moyennes du pelage |
| Orange ombre | `#812900` | ombres et profondeur (remplace `#8D2E0F` depuis la v1.1, 24 novembre 2026) |
| Blanc | `#FFFFFF` | fond d'identité, respiration |
| Noir chaud | ~`#1A1512` | yeux, sourcils, broderies |

Valeurs photographiques de départ (v0.1) : à valider visuellement à l'écran avant tout usage imprimé ou produit dérivé.

**Thème sombre (v0.4) — état ancien, à migrer (v1.0)** : le thème sombre a été la déclinaison des surfaces numériques (site de l'atelier, pages web, interfaces) du 22 novembre 2026 jusqu'au passage à la v1.0. Depuis la décision d'unification du 22 novembre 2026 (§ 3.1), la **norme cible de toutes les surfaces est le fond à dominante blanche** ; le thème sombre ci-dessous est donc un **état ancien** : il reste documenté parce que les deux sites l'emploient encore, et il sera retiré surface par surface par le chantier de migration des sites (chantier séparé — la charte énonce la norme cible, pas le calendrier). Il n'a jamais remplacé ni le fond blanc des images d'identité, ni la palette du personnage.

| Rôle (thème sombre) | Valeur | Note |
|---|---|---|
| Fond de page | `#161110` | charbon chaud profond |
| Surface / cartes | `#221A16` | brun sombre |
| Surface élevée | `#2C211B` | panneaux, éléments surélevés |
| Texte principal | `#FFF3E6` | blanc chaud |
| Texte atténué | `#D2BBA6` | beige chaud |
| Bordures | `#4A3728` | brun moyen |
| Scène claire (sous les images canoniques) | `#FFF8F1` | les images officielles sur fond blanc sont toujours présentées sur cette scène claire, même en thème sombre, pour garder leur rendu exact |

Les oranges maîtres (`#FC8B32`, `#C95D1D`, `#812900`) restent inchangés en thème sombre ; sur les boutons et éléments pleins orange, le texte passe en foncé pour le contraste.

**Verrou couleur (v0.2)** :

- **Couleurs maîtresses = les hex sRGB du tableau ci-dessus.** Le livrable web, avatar et réseaux sociaux est en sRGB ; « orange » sans code hex est un vocabulaire interdit dans les spécifications.
- **Chaînes 3D / vidéo** : OCIO/ACES est permis **uniquement à l'intérieur** de la chaîne de rendu (volet 3D, compositing), avec un seul fichier de configuration OCIO versionné dans `01_source/` et une seule transformation de sortie vers sRGB, documentée. L'orange saturé d'Onyx peut dériver sous ACES : le passage de la référence dans la chaîne doit être testé et approuvé **avant** adoption, et le réglage retenu est consigné. Jamais d'ACES sur les actifs 2D plats.
- **Produits dérivés (merch, à venir)** : établir les équivalents **Pantone + CMYK** des hex maîtres et faire approuver une **épreuve physique** (échantillon imprimé ou tissu) par l'opérateur avant toute production — l'écran ne tranche pas la couleur d'un objet physique.

### 3.1 Couleurs d'accompagnement — les séries (v1.0, toutes surfaces)

_Ajouté le 22 novembre 2026 : intégration de la direction **D3 « Une couleur par série »** — adoptée par l'opérateur (~19:18 EST), amendée « fonds blancs » (~19:19), exemples révisés validés par lui (~19:32, « Je valide la version fond blanc »), puis **étendue par l'opérateur à toutes les plateformes et aux deux sites** (~19:33 : les mêmes logos, les mêmes images, les mêmes codes couleurs — tous les produits, toutes les plateformes). Le système D3-blanc est le **système d'identité unifié** du projet, pas une exception limitée à l'habillage social. Avenant d'origine : `instagram-direction-v2/AVENANT-CHARTE-D3-BROUILLON.md` (intégré, avec l'élargissement de périmètre noté en tête du brouillon)._

En plus de la palette maîtresse ci-dessus, toutes les surfaces du projet utilisent un jeu de **couleurs d'accompagnement codées par série**. La couleur ne décore pas : elle **dit le chapitre**, comme la numérotation dit la pièce.

| Série | Couleur | Valeur | Texte porté par la couleur |
|---|---|---|---|
| Feuille de modèle / personnage | Bleu série | `#1B6AC9` | Blanc (5,31:1) |
| Fabrication (étapes) | Vert série | `#2E7D32` | Blanc (5,13:1) |
| Ratés de l'atelier | Rouge série | `#C62F24` | Blanc (5,48:1) |
| Poses & expressions | Jaune série | `#FFC53D` | Noir chaud `#1A1512` (11,47:1) |
| Coulisses | Corail série | `#EF6351` | Noir chaud `#1A1512` (5,67:1) |

**Fonds — norme générale des surfaces.** Toutes les surfaces se composent sur des **fonds à dominante blanche** : blanc `#FFFFFF` en champ principal, plaque `#FFF8F1` pour la carte du personnage et les scènes claires (§ 3). Cela vaut pour l'habillage social (planches, carrousels, couvertures de highlights et de reels, stories d'annonce, miniatures — Instagram, TikTok, YouTube) **et pour les deux sites** (site de l'atelier et page de liens). La couleur de série vit en **accents d'habillage et de navigation** : numéro de série géant en teinte pâle de la couleur, pastille « SÉRIE · … », bordure couture colorée, bandes, cadres, filets, états de navigation. **Les fonds sombres sont retirés des surfaces** : le thème sombre du § 3 est un état ancien — les deux sites le portent encore et le quitteront par le chantier de migration des sites (chantier séparé) ; aucune surface nouvelle ne se construit en sombre.

**Règles d'usage.**

- **Une seule couleur de série par pièce** — celle de sa série, jamais un mélange de deux séries sur une même planche, couverture ou écran.
- Petit texte sur blanc : **noir chaud** ou **orange ombre `#812900`** (règle du § 16.1, ratios recalculés en v1.1) ; la couleur de série peut porter du petit texte seulement aux combinaisons vérifiées du tableau ci-dessus.
- **Jamais d'orange vif `#FC8B32` en petit texte sur fond clair** (rappel § 16.1 : 2,25:1) ; jamais de texte blanc sur le jaune série (1,58:1).
- Les couleurs de série sont des couleurs **d'habillage et de navigation** — **jamais des couleurs du personnage** : le personnage, ses oranges (§ 3) et la photo de profil (identité sur fond blanc) ne sont pas touchés par cet article.
- Les pièces déjà publiées ne sont pas retouchées par cet article ; leur migration éventuelle relève des chantiers de migration (publications : backlog nº 43 ; sites : chantier séparé).

### 3.2 Couleur du personnage — « mohair cannelle miel clair » (v1.3)

_Décision de l'opérateur, 26 novembre 2026 (~06:45 EST, appel vocal) : sur la planche de comparaison des teintes produite le matin même (`bascule-cannelle-2026-11-26/planche-comparaison-teintes-toit.png` — nº 1 = le mohair cannelle de la nuit, en plein soleil sur le toit, où il ressortait presque orange ; nº 2 = une variante plus claire et moins saturée, tirant vers le miel doré), l'opérateur choisit le **nº 2** et ordonne de « repartir de zéro » sur cette base. Le nouveau portrait officiel généré directement dans la teinte est **validé** dans la foulée et devient la référence canonique. Cette décision **remplace celle de la même nuit** (~00:51 EST, mohair cannelle nº 5 `#B06A35`), qui n'aura vécu que quelques heures et n'a jamais été déployée._

- **Couleur officielle de la fourrure : « mohair cannelle miel clair »** — finition **mate**, **poil court, fin et dense (~3 mm, type minky)**. C'est la seule couleur du pelage ; le nom exact est « mohair cannelle miel clair ».
- **Valeur de référence : `#AD6A3D`** — médiane de fourrure **mesurée aux pixels sur le portrait canonique** (R 173, V 106, B 61 ; 26 novembre 2026). Particularité de cette bascule : le ton a été choisi **sur image générée en scène réelle** (planche de comparaison sur le toit), pas sur un échantillon de palette — il n'existe donc pas de hex nominal de nuancier ; la valeur maîtresse est la mesure du portrait validé. (La cible demandée au moteur de génération était ~`#C07A42` ; la médiane photographique livrée, ombres du poil comprises, est `#AD6A3D` — c'est elle qui fait foi.) À titre de contrôle croisé, le protocole du script de déclinaisons (masque de figure entier) lit `#B27040` sur la source et `#B37140` sur le maître recomposé — même famille ; l'écart tient au protocole de masque, la valeur de référence reste `#AD6A3D`.
- **Le mohair cannelle `#B06A35` (décision de la nuit, ~00:51 EST) passe à l'historique** : remplacé le matin même, avant tout déploiement ; ses déclinaisons locales (`bascule-cannelle-2026-11-26/`) sont conservées comme trace de la passe, mais ne servent plus de base de production. Avant lui, l'ancien orange vif `#F5821F` avait déjà été retiré comme couleur du personnage (ère orange, jusqu'au 25 novembre 2026) ; aucune production nouvelle n'emploie ni l'un ni l'autre pour le pelage.
- **La palette d'accent des surfaces (§ 3) ne change pas** : `#FC8B32`, `#C95D1D`, `#812900`, noir chaud et blanc restent les couleurs d'habillage, de logotype et de navigation. Le mohair cannelle miel clair est la couleur **du personnage**, pas un nouvel accent de surface.
- **Règle de production de la matière** : la fourrure se **génère directement dans la couleur**, mate — **jamais par recoloration d'une photo éclairée dans une autre teinte**. Échec constaté le 26 novembre 2026 : la recoloration HSV conserve la réponse lumineuse de la peluche d'origine (hautes lumières saturées, texture marbrée), ce qui donne un effet « brûlé » au soleil sur toute teinte plus foncée ; les traitements mats atténuent sans corriger. Les scènes se régénèrent donc dans la couleur, sur les décors de référence réels.
- **Référence** : `references/onyx-canonique-cannelle-miel-clair.webp` (portrait validé par l'opérateur, 26 novembre 2026 ~06:45 EST ; MD5 `cb2f81dc859b3e953a57a96c2d018005`). **Mesure de contrôle** : médiane de fourrure `#AD6A3D` (voir ci-dessus). À titre de comparaison, au même protocole de référence : le mohair cannelle de la nuit mesurait `#AF612D`, l'ancien buste orange `#D9621C`.
- **Museau** : dans le nouveau portrait, la zone du museau se fond davantage dans le visage que sur les références précédentes. La remarque a été montrée à l'opérateur, qui a ordonné de repartir sur cette base **sans renfort du museau** : le museau du portrait canonique fait donc foi tel quel. (Le `#E4A87B` de la chaîne 3D reste en attente de re-décision au bloc matériau 3D.)
- **Point ouvert (non tranché, à décider avec l'opérateur)** : le trio de nuances dérivées du personnage (lumière / médian / ombre du pelage) n'est pas arrêté — seule la valeur de référence `#AD6A3D` fait foi à ce stade.

## 4. Règles d'or

1. Une seule apparence, partout, toujours : avatar, photos, vidéos, web, réseaux sociaux.
2. Les technologies peuvent changer (moteurs de rendu, super sampling, ray tracing, reconstruction des poils) ; le design, les couleurs et les codes restent.
3. Toute exception (ex. version déguisée demandée pour une occasion précise) est ponctuelle, explicite, et ne remplace jamais la référence.
4. La fourrure fait partie de l'identité : personnage en peluche, aspect doux type Winnie l'ourson — la qualité des poils n'est jamais sacrifiée à la vitesse.

## 5. Déclinaisons par surface

- **GitHub** : photo de profil = référence au repos, fond blanc. Contrainte technique : image de moins de 1 Mo → version allégée officielle `assets/onyx-github-avatar.jpg` (1024 × 1024, JPEG, 149 Ko), même photo, aucune variante.
- **Page web** : **fond à dominante blanche (§ 3.1)** ; orange Onyx en accent maître, couleurs de série en accents d'habillage et de navigation (§ 3.1), aucune couleur étrangère à la palette et au système de séries. Le site de l'atelier est encore en thème sombre (état ancien, § 3) : sa migration vers la norme blanche relève du chantier de migration des sites, pas d'une retouche de cette charte.
- **Vidéos** : génération à partir du snapshot de référence uniquement ; voix nº 1 « la master », uniforme du début à la fin.
- **Réseaux sociaux** : même photo de profil, même nom « Onyx », même palette — et **même système de séries à fonds blancs (§ 3.1)** sur toutes les plateformes (Instagram, TikTok, YouTube).

## 6. Identité sonore (rappel)

La voix fait partie des normes : voix nº 1, la master (joyeuse, accent québécois, un peu plus grave), partout, y compris dans les vidéos. La voix nº 2 (grave, façon Dark Vador) et le style « Ted » sont des exceptions sur demande explicite seulement.

_Précisions sur le mouvement de la marque, le style des sous-titres et le statut complet de l'identité sonore : § 13._

## 7. Proportions (unités de tête)

L'unité de mesure du personnage est la **hauteur de tête (T)** : du **sommet du crâne au menton** — convention permanente adoptée à la porte nº 1 (les oreilles sont hors T : + 0,09 T au-dessus du crâne).

Valeurs **figées** (feuille de modèle approuvée par l'opérateur le 21 novembre 2026 ; mesures complètes dans `3d/model-sheet/MODEL-SHEET-SPEC.md`) :

- hauteur visible du buste de la référence ≈ **1,67 T** (le bas du cadre coupe le torse : la référence est un buste) ;
- largeur maximale de la tête ≈ **1,17 T** — tête plus large que haute : silhouette ronde de peluche ;
- **corps entier officiel : hauteur totale ≈ 2,5 T** (2,51 T au sommet des oreilles) — décomposition : pieds + jambes 0,55 T ; torse sous le menton 0,87 T ; tête 1,00 T ; oreilles + 0,09 T ;
- pas de cou visible ; la tête fusionne avec le torse par un pincement doux, les épaules naissent directement sous la tête.

Le pack canonique 3D v1 (planches + vues retenues + manifeste SHA-256) vit dans `00_canonical/3d-v1/` et fait foi pour toute modélisation, génération et déclinaison du personnage.

## 8. Paragraphe de prompt canonique

Le texte ci-dessous est l'identité d'Onyx en mots. Il se colle **verbatim** — sans reformulation — dans tout prompt de génération d'image ou de vidéo, sur toutes les plateformes ; on n'y ajoute que les mots de scène, de pose et d'expression propres à chaque production. Le modifier, même légèrement, ou le traduire, exige une nouvelle version de la charte.

> Peluche en tissu mohair cannelle miel clair doux et mat, poil court, coutures visibles, oreilles rondes, grands yeux noirs ovales brodés sans blanc ni reflet, petits sourcils courbés en arc, museau doux et saillant au centre du visage, bouche en un seul trait courbé formant un petit sourire calme, tête ronde presque aussi large que haute, buste sans cou visible, mohair cannelle miel clair #AD6A3D, fond blanc pur, lumière douce et uniforme, rendu net de photographie de produit — aucun accessoire, aucune corne, aucun croc, aucune dent, pas de fourrure réaliste.

## 9. Gouvernance

- Cette charte est versionnée. Toute modification passe par une nouvelle version datée, jamais par une retouche silencieuse.
- Emplacement de travail : `~/workspace/onyx-anime/docs/CHARTE-GRAPHIQUE.md` ; à publier ensuite dans le dépôt onyx-lab, qui fera foi.
- L'état d'application des techniques de constance (P0→P9) est suivi dans `docs/CONSTANCE-APPLICATION.md`.

## 10. Typographie et logotype (v1 — à raffiner)

_Ajouté le 22 novembre 2026 (chantier « angles morts » nº 1 du plan de projet, `docs/PLAN-PROJET.md`). Version 1 assumée : en service dès maintenant, raffinée en v2. Dossier complet : `typo-logo-v1/` — planche spécimen, fichiers du logotype, polices et licences, scripts de reproduction (`build_logo.py`, `build_specimen.py`), justifications détaillées (`CHOIX.md`)._

- **Police d'affichage et de logotype : Fredoka** (variable, graisses 300–700 ; usage retenu : **SemiBold 600**, largeur 100 %). Formes géométriques très rondes et pleines — le « O » rond comme la tête du personnage — douces comme une peluche, assez structurées pour rester professionnelles. Titres, couvertures, en-têtes, miniatures.
- **Police de texte : Nunito** (variable, graisses 200–1000, italique véritable). Terminaisons rondes cohérentes avec Fredoka, grande lisibilité en petit corps : légendes, sous-titres, textes courants, interface.
- Les deux familles sont sous **licence SIL Open Font License 1.1** et couvrent **tous les diacritiques français** (vérifié caractère par caractère : œ, æ et majuscules accentuées compris) — critère éliminatoire, le français étant la langue première du projet.
- **Logotype v1** : le mot « Onyx » en Fredoka SemiBold, « O » majuscule puis bas de casse, lettres non retouchées. Déclinaisons officielles (fichiers dans `typo-logo-v1/logo/`) :
  - fond sombre : orange lumière `#FC8B32` sur `#161110` (déclinaison principale) ;
  - fond clair : orange médian `#C95D1D` sur blanc ;
  - monochromes : noir chaud (~`#1A1512`) et blanc, sur fond transparent ;
  - verrouillage **icône + texte** : la tête de la référence canonique, recadrée carrée **telle quelle** — jamais redessinée ni retouchée (ce recadrage est une présentation de la référence, pas un nouvel actif canonique).
- **À raffiner en v2** : lettrage vectoriel (SVG) et crénage manuel, variante empilée du verrouillage, favicon et kit réseaux sociaux, épreuve d'impression. Détail dans `typo-logo-v1/CHOIX.md`.
- **Règles d'utilisation du logotype** (zone de protection, tailles minimales, fonds autorisés, interdits) : § 12.

## 11. Langage design

_Ajouté le 22 novembre 2026, sur décision de l'opérateur : ce langage s'applique à **tout le projet**, y compris aux surfaces déjà produites, révisées progressivement (voir « Transition », § 11.4). Deux couches d'inspiration, traduites en **principes** — jamais en copies. Planche de démonstration : `langage-design-v1/fiche-technique-onyx-v1.png` (script : `langage-design-v1/build_fiche_technique.py`)._

### 11.1 Couche « précision d'instrument » — inspiration Teenage Engineering

l'opérateur respecte beaucoup le design de cette marque d'instruments de musique : minimalisme fonctionnel, précision d'atelier, esprit « bel objet-outil ». Traduit chez nous :

01. **Étiquetage technique numéroté.** Parties, vues, planches et écrans portent des numéros (01, 02, 03…) comme les commandes d'un instrument. Cette numérotation prolonge nos codes existants : vues de décors L1–L6 et A1–A3, pièces d'archive numérotées, planches numérotées.
02. **Annotations façon fiche technique.** Étiquettes, mesures et spécifications s'affichent **sur** la planche ou l'écran, en petites capitales ou en police mono — rien d'important n'est caché dans un document séparé.
03. **Grille modulaire stricte.** Alignements visibles, modules réguliers, espacements constants ; aucun placement approximatif.
04. **Un seul accent.** L'orange maître `#FC8B32` (§ 3) est le seul accent, posé sur les fonds sobres de la palette. Aucune deuxième couleur d'accent.
05. **Pictogrammes simples et fonctionnels.** Formes géométriques plates, lisibles en petit format, qui désignent une fonction — jamais un ornement.
06. **Chaque élément a une fonction.** Rien de décoratif gratuit : si un élément ne sert ni à identifier, ni à mesurer, ni à guider, il disparaît.
07. **Précision affichée.** Versions, références de fichiers et mesures se montrent comme la plaque signalétique d'un instrument (ex. « FT-01 / RÉV. 0.6 »).

**Exception au principe 04 (v1.0) — couleurs de série (§ 3.1).** L'**identité** — personnage, logotype, avatar — reste gouvernée par la règle « un seul accent » **sans exception** : l'orange maître est le seul accent de l'identité. Les couleurs de série du § 3.1 ne contredisent pas ce principe : ce sont des **accents d'habillage et de navigation**, valables sur **toutes les surfaces** (habillage social **et** sites), une couleur par série et une série par pièce — jamais des couleurs du personnage.

### 11.2 Couche « atelier montréalais » — inspiration Le Cartel et Art Gang Montréal

Deux collectifs d'atelier d'ici, dont on retient la façon de travailler et de se présenter : fait-main, travail collectif, fierté montréalaise assumée, graphisme audacieux proche de l'affiche et du streetwear, séries limitées et collaborations locales.

08. **Signature d'atelier.** Les productions portent la mention « atelier — Montréal » (ou « fait à l'atelier, Montréal ») comme une signature de fabrication, pas comme un slogan publicitaire.
09. **Séries numérotées.** Les pièces marquantes sortent en séries numérotées (« série 01 — pièce nº 001 »), en petites quantités assumées — dans la continuité des planches et archives déjà numérotées du projet.
10. **Crédits de fabrication affichés.** Qui a conçu, assemblé, validé : les crédits se montrent sur la pièce ou la planche, comme les ateliers qui signent leur travail.
11. **Ton d'atelier, pas de studio.** Vocabulaire concret et manuel (couper, assembler, ajuster, pièce, série) plutôt que langage corporatif. L'audace graphique d'une affiche est permise **dans l'habillage** — jamais sur le personnage.
12. **Collaborations locales d'abord.** Quand le projet s'ouvre (illustration, musique, artisanat), la priorité va aux collaborations montréalaises, en petites séries revendiquées.

### 11.3 Ce que ça change, surface par surface

- **Planches et carrousels** : numérotation des planches et des vues, annotations techniques en mono sur la planche, crédits d'atelier en pied. Les planches déjà produites (carrousel « étape 1 » v2, planches de décors L/A) sont re-planchées dans ce langage à leur prochaine publication.
- **Habillage live** : écrans d'attente, de pause et de fin étiquetés et numérotés comme les modes d'un instrument ; pictogrammes fonctionnels seulement ; signature « atelier — Montréal » en pied d'écran.
- **Storyboard** : la numérotation des plans (déjà en place) est complétée par les spécifications en annotations mono (format, durée, échelle de plan) et par les crédits de fabrication sur la planche finale.
- **Site de l'atelier** : grille modulaire stricte, sections numérotées, étiquettes mono pour les spécifications ; **norme cible : fond à dominante blanche et accents de série (§ 3.1)** — le thème sombre actuel (§ 3) est un état ancien, migré par le chantier de migration des sites.
- **Page de liens** : les cartes deviennent des modules fonctionnels numérotés — une fonction par module, un pictogramme par fonction ; même norme de fond blanc et d'accents de série (§ 3.1) que le site de l'atelier.
- **Miniatures YouTube** : un numéro, l'accent orange maître et l'accent de la série de la pièce (§ 3.1), la typographie d'affichage (§ 10) en grand, sur fond à dominante blanche ; aucune décoration qui ne sert pas le titre.
- **README GitHub** : en-tête façon fiche technique (version, références, spécifications en mono), sections numérotées, crédits de fabrication en pied.

### 11.4 Garde-fous

- **Le personnage ne change pas.** L'apparence verrouillée (§ 1), les proportions (§ 7) et le paragraphe de prompt canonique (§ 8) restent intacts : le langage design habille la présentation, il ne touche jamais au modèle.
- **La palette ne change pas** (§ 3) : l'accent d'identité est notre orange maître ; les fonds (dominante blanche) et les accents d'habillage et de navigation sont ceux de la charte (§ 3.1).
- **Inspiration de principes seulement.** Aucune reproduction des produits, logos, habillages ou visuels de Teenage Engineering, de Le Cartel ou d'Art Gang Montréal ; leurs noms n'apparaissent que dans cette charte interne, comme sources d'inspiration — jamais sur une surface publique du projet.
- **Transition.** Les surfaces déjà en ligne sont révisées au nouveau langage au fil de leur prochaine mise à jour, sans republication précipitée ; les nouvelles productions l'appliquent immédiatement.

## 12. Logotype — règles d'utilisation (v1)

_Ajouté le 22 novembre 2026 (complément approuvé par l'opérateur). Le logotype lui-même est défini en § 10 ; cette section dit comment on l'emploie. Planche de référence : `charte-v07/logo-usage/planche-logo-usages.png` ; diagramme : `charte-v07/logo-usage/logo-zone-protection.png` ; script : `charte-v07/logo-usage/build_planche_logo.py`. Version 1 assumée._

- **Zone de protection.** Unité **x = la hauteur du « O » du logotype** (mesurée : 344 px pour un rendu au corps 480, soit ≈ 0,72 × le corps). Autour du logotype — et autour du verrouillage icône + texte — on garde libre un rectangle de **x sur les quatre côtés** : aucun texte, aucune image, aucun autre logo, aucun bord de page ou d'écran ne pénètre dans la zone. Le fond, lui, peut la traverser.
- **Tailles minimales** (en largeur) :
  - écran : logotype seul **≥ 96 px** ; verrouillage icône + texte **≥ 160 px** ; icône seule **≥ 24 px** ;
  - impression : logotype seul **≥ 30 mm** ; verrouillage **≥ 40 mm** ; icône seule **≥ 10 mm** ;
  - en dessous de ces tailles, on n'écrase pas le logotype : on utilise **l'icône seule** (la tête de la référence, telle quelle, § 10) — c'est aussi la forme du favicon.
- **Fonds autorisés.** Les déclinaisons officielles de la § 10 et elles seules : orange lumière sur fond sombre, orange médian sur fond clair, monochromes noir chaud ou blanc. Sur une photo ou un fond texturé, le logotype se pose **dans un cartouche** — scène claire `#FFF8F1` ou fond sombre uni de la palette (§ 3) — jamais directement sur un fond chargé.
- **Interdits (liste fermée, illustrés sur la planche)** :
  1. étirer, écraser ou modifier les proportions ;
  2. recolorer hors palette — dégradés de couleur compris ;
  3. tourner ou incliner ;
  4. contourer, vider, ou redessiner les lettres ;
  5. poser sur un fond illisible ou à contraste insuffisant ;
  6. ajouter ombre portée, relief, lueur ou tout effet ;
  7. modifier l'espacement des lettres, la casse, ou la composition du verrouillage.
- **Limites v1** : les tailles minimales sont posées à l'expérience de l'écran ; l'épreuve d'impression (déjà prévue en § 10, v2) les confirmera ou les ajustera. Le lettrage reste le rendu Fredoka v1 tant que la vectorisation SVG (§ 10, v2) n'est pas livrée.

## 13. Identité en mouvement et sonore (v1)

_Ajouté le 22 novembre 2026 (complément approuvé par l'opérateur). Cette section précise la § 6 et codifie le mouvement de l'habillage à partir des actifs existants de `habillage-live-v1/`. Version 1 assumée._

### 13.1 Mouvement de la marque

- **Courbe de référence** : le fondu « smoothstep » (ease-in-out, t²(3−2t)) pour toutes les transitions d'habillage. Aucune courbe élastique, aucun rebond sur les éléments de marque — le rebond doux appartient au personnage en animation, pas à l'habillage.
- **Durées de référence** (mesurées sur le sting et les écrans actuels) :
  - micro-transitions (pictogrammes, étiquettes, états) : **150 à 250 ms** ;
  - transitions entre écrans d'habillage : **fondu enchaîné de 300 à 500 ms** ;
  - sting : **3,5 s à 30 images/s** — fondu d'entrée 1,0 s, tenue ≈ 2,0 s, fondu de sortie 0,5 s ;
  - pulsé du halo orange : sinusoïde de **période 1,4 s**, amplitude faible — le seul mouvement « respirant » de l'habillage.
- **Règles** : l'habillage n'anime jamais le personnage (aucun déplacement, zoom ou fondu appliqué au personnage par les écrans ou les overlays) ; un seul élément animé à la fois ; pas de texte défilant dans les écrans v1.

### 13.2 Sous-titres vidéo

- **Police** : Nunito SemiBold (600) — la police de texte de la § 10. **Français seulement** : les sous-titres tiennent lieu de version pour les autres langues, on ne produit pas de versions traduites du contenu. Ponctuation française (espaces insécables avant `:` `;` `!` `?`, guillemets « »).
- **Corps** : hauteur de texte ≈ **4,5 % de la hauteur d'image** (1080p → ≈ 48 px ; 720p → ≈ 32 px), interligne 1,25.
- **Présentation** : texte blanc chaud `#FFF3E6` sur fond noir chaud semi-transparent (noir chaud à 75 % d'opacité), coins légèrement arrondis, marge interne ≈ 0,35 × la hauteur de texte. **2 lignes maximum, ≈ 42 caractères par ligne.**
- **Placement** : bas-centre, dans la zone sous-titres du gabarit du format (§ 15) — jamais dans une zone d'interface de la plateforme.
- **Rythme** : un sous-titre par phrase ou par souffle ; aucun sous-titre de moins de 0,8 s à l'écran.

### 13.3 Identité sonore — statut

- **Figé** : la parole, c'est la voix nº 1 « la master », partout (§ 6). La voix nº 2 et le style « Ted » restent des exceptions sur demande explicite seulement.
- **En pause** : le projet de voix transformée (Voicemod et apparentés) est **suspendu depuis le 21 novembre 2026, sur décision de l'opérateur**. Aucune expérimentation vocale nouvelle, aucun nouvel outil de voix, sans sa demande explicite — cette charte n'invente rien côté voix.
- **À créer (rien n'existe encore)** : une éventuelle signature sonore courte associée au sting — le sting actuel est **muet, et c'est assumé** — et d'éventuels sons d'interface pour l'habillage. Toute création sonore exigera l'approbation de l'opérateur et une nouvelle version de la charte.
- **Musique des vidéos** : choisie production par production ; en v1, elle ne fait pas partie de l'identité figée.

## 14. Pictogrammes (v1)

_Ajouté le 22 novembre 2026 (complément approuvé par l'opérateur). Application directe du principe 05 de la § 11 : des pictogrammes simples et fonctionnels, jamais des ornements. Dossier : `charte-v07/pictogrammes/` — PNG 480 × 480 transparents (déclinaisons crème et noir chaud), sources SVG, planche du jeu, script de génération._

- **Style** : grille de construction **48 × 48** ; trait de **3 unités** (6,25 % du format), centré sur la grille ; **extrémités et angles ronds** partout ; formes **pleines** seulement quand la fonction l'exige (lecture, pause, têtes de notes) ; aucun détail sous **1,5 unité** ; zone de respiration de **4 unités** autour de la forme ; un seul niveau de détail — ni double trait, ni ombre, ni dégradé.
- **Couleurs** : crème `#FFF3E6` sur les surfaces sombres, noir chaud (~`#1A1512`) sur les surfaces claires. L'orange maître `#FC8B32` est réservé à **l'état actif** (action en cours, élément sélectionné) — jamais en décoration.
- **Usage** : taille minimale **20 px** à l'écran (en dessous, on simplifie ou on renonce) ; alignement sur la grille modulaire (§ 11, principe 03) ; un pictogramme par fonction, toujours le même pour la même fonction.
- **Le jeu v1 (10 pictogrammes)** : lecture, pause, musique, caméra, micro, lien, courriel, atelier (les ciseaux — couper, assembler), couches, contrôle qualité.
- **Ajouter un pictogramme** : même grille, même trait, mêmes arrondis ; il est d'abord posé à côté du jeu existant et validé visuellement. Aucune icône importée d'une banque externe : le style ne suivrait pas.
- **Limites v1** : les SVG sont écrits à la main en miroir des PNG (aucun moteur de rendu vectoriel local pour les contre-vérifier pixel par pixel) ; le pictogramme « atelier » est le plus stylisé du jeu et le candidat nº 1 au raffinement v2.

## 15. Gabarits par plateforme (v1)

_Ajouté le 22 novembre 2026 (complément approuvé par l'opérateur). Un gabarit visuel par format, aux dimensions réelles d'export, dans `charte-v07/gabarits/` (script : `build_gabarits.py`). Le gabarit se pose en surimpression pendant la composition ; il ne fait jamais partie du livrable. Dans tous les gabarits, le personnage en image canonique reste sur la scène claire `#FFF8F1` (§ 3), et les zones marquées « interface » sont celles des plateformes au 22 novembre 2026 — à revérifier à chaque refonte de leurs interfaces._

**Paramètre « fond blanc + couleur de série » (§ 3.1, v1.0).** Tous les gabarits, sur toutes les plateformes, reçoivent ce paramètre : fonds à dominante blanche et accent de la série de la pièce. Pour Instagram, les planches nouvelles passent au **3:4 (1080 × 1440)** (format adopté le 22 novembre 2026 — il remplace le 4:5 du gabarit nº 03 ci-dessous pour les planches à venir) ; couvertures de highlights par série, couvertures de reels 9:16 et story d'annonce assorties ; les mêmes paramètres valent pour TikTok et YouTube, et les gabarits des deux sites suivent la même norme. Tant que les constructeurs ne sont pas mis à jour, le détail vit dans la liste des gabarits à paramétrer (avenant D3 intégré, § D — `instagram-direction-v2/AVENANT-CHARTE-D3-BROUILLON.md`).

| Nº | Format | Dimensions | Zones codifiées |
|---|---|---|---|
| 01 | Story / reel 9:16 | 1080 × 1920 | Interface haut : y 0–230 (rien à placer). Interface bas : y 1500–1920 (légende, appels à l'action). Rail de boutons : x ≥ 950, y 950–1480. Titre : y 250–430, Fredoka, 2 lignes max. Personnage : x 70–930, y 450–1330. Sous-titres : y 1350–1470 (§ 13.2). |
| 02 | Miniature YouTube 16:9 | 1280 × 720 | Titre à gauche : x 40–790, y 60–470, Fredoka SemiBold, 3 lignes max, gros corps. Personnage à droite : x 820–1240, y 50–670. Coin bas-droit libre : x 1080–1250, y 630–700 (pastille de durée de YouTube). Un numéro, un seul accent (§ 11.3). |
| 03 | Publication Instagram 4:5 | 1080 × 1350 | Marges ≥ 64 px sur tous les bords. Le sujet doit tenir dans le **carré central 1:1** (y 135–1215) : c'est ce que la grille du profil affiche. Titre : y 300–470. Personnage : x 190–890, y 500–1150. |
| 04 | Bannière YouTube | 2560 × 1440 | Plein cadre = TV (fond et ambiance seulement, aucun texte). Bande bureau / tablette : hauteur visible 423 px, centrée (y 508–932). Zone tablette : 1855 × 423, centrée. **Zone sûre tous écrans : 1235 × 338, centrée** (x 662–1898, y 551–889) — logotype, titre et personnage uniquement là. Cohérent avec l'actif préparé `surfaces-te-v1/banniere-youtube-v1.png`. |
| 05 | Écran live 16:9 | 1920 × 1080 | Zone personnage : centre, dans les limites de l'overlay d'appel (x 480–1440, y 200–880 — zone entièrement transparente, le visage n'est jamais couvert). Étiquette d'écran numérotée : haut-gauche. Signature « atelier — Montréal » : haut-droite. Sous-titres / information basse : y 890–960. Bandeau nom de l'overlay : 104 px en bas. |

- **Limites v1** : zones d'interface relevées sur les applications actuelles (Instagram, TikTok, YouTube) sans garantie de stabilité ; le gabarit bannière reprend la zone sûre déjà en usage dans le projet plutôt qu'une nouvelle mesure.

## 16. Contrastes et partage des liens (v1)

_Ajouté le 22 novembre 2026, à la suite de l'audit réseau/accessibilité (`docs/AUDIT-RESEAU-ACCESSIBILITE-2026-11-22.md`, corrections nº 3 et 10). Les ratios ci-dessous sont **calculés** (formule de luminance relative des WCAG 2.2), pas estimés. Seuils AA de référence : texte normal ≥ 4,5:1 ; grand texte (≥ 24 px, ou ≥ 18,66 px gras) ≥ 3:1 ; indicateurs et composants (focus, contours porteurs d'information) ≥ 3:1._

### 16.1 Règles de contraste de la palette (§ 3)

- **Orange lumière `#FC8B32` en texte : sur fonds sombres uniquement** — 7,91:1 sur `#161110` ✅. Sur fonds clairs il échoue partout : 2,25:1 sur `#FFF8F1`, 2,37:1 sur blanc — **interdit en texte sur clair, même en grand texte**.
- **Petit texte orange sur fond clair : `#812900` seulement** (8,86:1 sur `#FFF8F1`, 9,33:1 sur blanc ✅ — ratios recalculés en v1.1 pour la nouvelle orange ombre ; l'ancienne valeur `#8D2E0F` donnait 7,88:1 et 8,30:1). L'orange ombre est à son tour **interdit sur fond sombre** (2,01:1 sur `#161110`).
- **Orange médian `#C95D1D`** : sur fond clair, **grands textes seulement** (4,14:1 sur blanc, 3,94:1 sur `#FFF8F1`) ; sur fond sombre, conforme mais juste (4,52:1 sur `#161110`) — le réserver aux éléments non critiques.
- **Bandes, boutons et fonds pleins orange : texte sombre, jamais texte clair.** `#161110` sur `#FC8B32` = 7,91:1 ✅ ; `#FFF3E6` sur `#FC8B32` = 2,16:1 ❌. (La § 3 le disait en principe ; c'est ici chiffré et sans exception.)
- **Textes de base** : `#FFF3E6` sur `#161110` = 17,13:1 ✅ ; texte atténué `#D2BBA6` sur `#161110` = 10,16:1 ✅ — aucun changement.
- **Couleurs de série (§ 3.1)** : combinaisons vérifiées — blanc sur bleu série = 5,31:1 ✅, sur vert série = 5,13:1 ✅, sur rouge série = 5,48:1 ✅ ; noir chaud `#1A1512` sur jaune série = 11,47:1 ✅, sur corail série = 5,67:1 ✅. **Texte blanc sur jaune série interdit** (1,58:1 ❌). Sur les fonds blancs de la norme § 3.1, le texte reste noir chaud ou orange ombre (règles ci-dessus).
- **Bordures `#4A3728`** : 1,67:1 sur `#161110`, sous le seuil non textuel de 3:1 — elles restent donc **strictement décoratives** ; aucune information ne doit jamais être portée par une bordure seule (les cartes et boutons restent identifiables par leur fond et leur texte).
- **Indicateurs de focus** : le contour de focus doit atteindre ≥ 3:1 contre le fond adjacent dans **chaque** schéma (clair et sombre) — c'est l'application de cette règle qui a corrigé le contour de la page de liens en mode clair (orange foncé `#812900` en schéma clair, `#FC8B32` en schéma sombre).

### 16.2 Règle de partage des liens

- **Toujours partager l'URL directe canonique** d'une page du projet, copiée à la source (résultat de partage de la page, ou adresse de l'hébergement en vigueur).
- **Jamais une adresse copiée depuis Instagram ou un navigateur intégré** : tout lien touché dans Instagram est réécrit en `l.instagram.com/?u=…&e=<jeton>` (« link shim » de Meta) ; copié ailleurs, cet enrobage dépend d'un jeton de session et échoue pour le destinataire (constaté le 22 novembre 2026 : lien inutilisable dans Messenger).
- **Un lien `l.instagram.com` vu dans un message = un lien à remplacer, pas à transférer.**

## 17. Présentation publique — zéro hashtag, zéro étiquette « influenceur virtuel » (v1)

_Ajouté le 22 novembre 2026, décision de l'opérateur : ni les hashtags ni l'étiquette « influenceur virtuel » ne font partie de l'image de marque. Nettoyage appliqué le même jour à toutes les surfaces publiques (légendes Instagram, sites, bulle visiteur, matériels préparés)._

- **Aucun hashtag** dans les publications, légendes, descriptions et textes publics du projet, sur toutes les plateformes. La découverte repose sur les séries nommées, les textes écrits en langage naturel et la constance des noms composés (« Onyx Officiel », « IamOnyx ») — pas sur les mots-clics.
- **Aucune étiquette « influenceur virtuel »** — ni « virtual influencer », ni aucune forme collée en mot-clic — nulle part dans la marque publique. Onyx se présente comme ce qu'elle est : **un personnage, une peluche**, créée dans un atelier à Montréal.
- **La transparence IA n'est pas touchée** : elle se dit en toutes lettres — « personnage virtuel créé avec l'IA » (bio, site, fiche persona) — jamais par un mot-clic. Mention factuelle **conservée** par décision explicite de l'opérateur (22 novembre 2026).
- Cette règle **remplace** la pratique des mots-clics adoptée le matin même (stratégie § 3.3 ; gouvernance B4 pour son volet mots-clics de divulgation) : ces textes sont conservés comme historique et ne s'appliquent plus. Point d'attention consigné au journal des décisions : la divulgation légale d'un éventuel contenu commandité (gouvernance B3) devra être réconciliée avec cette règle avant toute campagne — aucune n'est en cours.

**Journal des versions**

| Version | Date | Changements |
|---|---|---|
| v0.1 | 21 novembre 2026 | Création : référence canonique, expression et cadrage officiels, palette échantillonnée, règles d'or, déclinaisons par surface, identité sonore. |
| v0.2 | 22 novembre 2026 | Application de la recherche « constance des studios » (priorité P1) : listes fixe/interdit explicitées en § 1 ; distinction maître WebP / copie de travail PNG et renvoi au manifeste SHA-256 ; verrou couleur en § 3 (hex sRGB maîtres, OCIO/ACES cantonné aux chaînes 3D/vidéo, Pantone/CMYK + épreuve physique pour la merch) ; nouvelle § 7 proportions en unités de tête (valeurs provisoires mesurées sur la référence) ; nouvelle § 8 paragraphe de prompt canonique verbatim. Contenu v0.1 intégralement conservé. |
| v0.3 | 22 novembre 2026 | Porte nº 1 franchie : feuille de modèle approuvée par l'opérateur (« pour l'instant, c'est final »). § 7 : convention T permanente (crâne → menton), proportions **figées** — buste 1,67 T, tête 1,17 T de large, corps entier officiel ≈ 2,5 T avec sa décomposition ; renvoi au pack canonique 3D v1 (`00_canonical/3d-v1/`, manifeste SHA-256). |
| v0.4 | 22 novembre 2026 | Thème sombre ajouté à la palette (§ 3), à la demande de l'opérateur : fond `#161110`, surfaces `#221A16` / `#2C211B`, texte `#FFF3E6`, texte atténué `#D2BBA6`, bordures `#4A3728`, scène claire `#FFF8F1` sous les images canoniques. § 5 : le site de l'atelier passe en thème sombre officiel. Les oranges maîtres et le fond blanc d'identité restent inchangés. |
| v0.5 | 22 novembre 2026 | Nouvelle § 10, typographie et logotype **v1 — à raffiner** (chantier « angles morts » nº 1) : **Fredoka** SemiBold pour l'affichage et le logotype, **Nunito** pour le texte — toutes deux SIL OFL 1.1 et complètes en diacritiques français (vérifié caractère par caractère). Logotype « Onyx » décliné : sombre, clair, monochromes, verrouillage icône + texte (tête de la référence recadrée telle quelle). Dossier : `typo-logo-v1/`. Aucune autre section modifiée. |
| v0.6 | 22 novembre 2026 | Nouvelle § 11, langage design applicable à tout le projet (décision de l'opérateur, y compris la révision progressive de l'existant) : couche « précision d'instrument » (inspiration Teenage Engineering — étiquetage technique numéroté, annotations façon fiche technique, grille modulaire, un seul accent `#FC8B32`, pictogrammes fonctionnels, précision affichée) et couche « atelier montréalais » (inspiration Le Cartel et Art Gang Montréal — signature « atelier — Montréal », séries numérotées, crédits de fabrication affichés, ton d'atelier, collaborations locales). Déclinaisons par surface (planches, habillage live, storyboard, site, page de liens, miniatures YouTube, README GitHub) et garde-fous : personnage et palette inchangés, inspiration de principes seulement, aucune reproduction d'identité tierce. Planche de démonstration : `langage-design-v1/fiche-technique-onyx-v1.png`. Aucune autre section modifiée. |
| v0.7 | 22 novembre 2026 | Quatre compléments approuvés par l'opérateur, chacun en v1 assumée, actifs dans `charte-v07/`. **§ 12, logotype — règles d'utilisation** : zone de protection x = hauteur du « O » (mesurée, 344 px au corps 480), tailles minimales écran et impression, fonds autorisés, 7 interdits illustrés (planche bons/mauvais usages + diagramme de zone). **§ 13, identité en mouvement et sonore** : courbe smoothstep et durées de référence mesurées sur `habillage-live-v1/` (sting 3,5 s, transitions 300–500 ms, pulsé 1,4 s), style complet des sous-titres vidéo (Nunito SemiBold, ≈ 4,5 % de la hauteur d'image, fond semi-transparent, français seulement), statut sonore — voix master figée (§ 6), projet de voix transformée en pause, signature sonore à créer et non inventée. **§ 14, pictogrammes** : style codifié (grille 48, trait 3 unités, arrondis, orange = état actif) et premier jeu de 10 pictogrammes fonctionnels en PNG + SVG. **§ 15, gabarits par plateforme** : 5 gabarits visuels aux dimensions réelles avec zones sûres (story 9:16, miniature YouTube, Instagram 4:5, bannière YouTube — zone sûre 1235 × 338 déjà en usage —, écran live 16:9). Renvois ajoutés en § 6 et § 10. Personnage et palette inchangés. |
| v0.8 | 22 novembre 2026 | Application de l'audit réseau/accessibilité du même jour (corrections nº 3 et 10). **Nouvelle § 16, contrastes et partage des liens** : règles de contraste **chiffrées** de la palette § 3 (ratios calculés WCAG 2.2) — orange lumière `#FC8B32` en texte sur fonds sombres uniquement (2,25–2,37:1 sur clair : interdit, même en grand texte) ; petit texte orange sur clair = `#8D2E0F` seulement ; `#C95D1D` sur clair = grands textes seulement ; bandes et boutons orange = texte sombre, jamais clair (2,16:1) ; bordures `#4A3728` strictement décoratives ; indicateurs de focus ≥ 3:1 dans chaque schéma. **Règle de partage permanente** : toujours l'URL directe canonique, jamais une adresse enrobée `l.instagram.com` copiée depuis une application Meta. Personnage, palette et autres sections inchangés. |
| v0.9 | 22 novembre 2026 | **Nouvelle § 17, présentation publique** (décision de l'opérateur) : aucun hashtag dans les publications et textes publics ; aucune étiquette « influenceur virtuel » / « virtual influencer » dans la marque ; la transparence IA se dit en toutes lettres (« personnage virtuel créé avec l'IA », mention conservée par décision explicite). La § 17 remplace la pratique des mots-clics de la stratégie § 3.3 et le volet mots-clics de la gouvernance B4 (historiques conservés). Nettoyage des surfaces appliqué le même jour. Personnage, palette et autres sections inchangés. |
| v1.0 | 22 novembre 2026 | **Système d'identité unifié — intégration de la direction D3 « Une couleur par série » à fonds blancs** (décisions de l'opérateur du même jour : adoption ~19:18, amendement « fonds blancs » ~19:19, exemples révisés validés ~19:32, **extension à toutes les plateformes et aux deux sites** ~19:33). **Nouvelle § 3.1** : cinq couleurs d'accompagnement codées par série (bleu `#1B6AC9`, vert `#2E7D32`, rouge `#C62F24`, jaune `#FFC53D`, corail `#EF6351`), textes portés et contrastes vérifiés ; **fonds à dominante blanche érigés en norme générale de toutes les surfaces** — habillage social (Instagram, TikTok, YouTube) **et** site de l'atelier **et** page de liens, mêmes logos, mêmes images, mêmes codes couleurs partout ; les couleurs de série sont des accents d'**habillage et de navigation**, jamais des couleurs du personnage. **§ 3** : le thème sombre est reclassé **état ancien à migrer** (les deux sites le portent encore ; leur migration est un chantier séparé — la charte énonce la norme cible, pas le calendrier). **§ 11.1** : l'exception au principe 04 « un seul accent » est reformulée — l'identité (personnage, logotype, avatar) reste à l'accent orange unique ; les couleurs de série relèvent de l'habillage et de la navigation sur toutes les surfaces. **§ 5, § 11.3, § 11.4, § 15 (renvoi « fond blanc + série », planches Instagram 3:4) et § 16.1 (combinaisons de série chiffrées)** mis en cohérence. **Inchangés** : palette et apparence du personnage (§§ 1–3), Fredoka/Nunito et règles du logotype (§§ 10 et 12), zéro hashtag (§ 17), adresse directe toujours partagée (§ 16.2). Avenant d'origine : `instagram-direction-v2/AVENANT-CHARTE-D3-BROUILLON.md` (marqué intégré, avec note d'élargissement de périmètre). Aucun changement en ligne : les sites ne sont pas touchés par cette version. |
| v1.1 | 24 novembre 2026 | **Remplacement de l'orange ombre** (décision de l'opérateur, ~20:40 EST : candidate nº 4 de la planche de proposition `palette-ombre-2026-11-24/`, sur recommandation d'Onyx) : l'orange ombre de la palette (§ 3) passe de `#8D2E0F` à **`#812900`** — même famille que l'orange médian, légèrement adoucie. § 16.1 : ratios recalculés (WCAG 2.2) pour la nouvelle valeur — petit texte orange sur clair : 8,86:1 sur `#FFF8F1`, 9,33:1 sur blanc ✅ (mieux que l'ancienne valeur) ; interdit sur fond sombre maintenu (2,01:1 sur `#161110`). Application référencée partout le même jour : fiches internes, sources des deux sites (paquet du site de l'atelier prêt, déploiement en attente du déblocage Cloudflare), copies GitHub et miroir Hugging Face, et **fil de couture du modèle 3D** (v14b, matériau seul). Les autres oranges, le noir chaud et le blanc sont inchangés ; les mentions historiques datées (dont la ligne v0.8 ci-dessus) conservent l'ancienne valeur comme trace. |
| v1.2 | 26 novembre 2026 | **Nouvelle couleur officielle du personnage — « mohair cannelle »** (décision de l'opérateur, ~00:51 EST : choix nº 5 de la planche palette « old school » du même jour ; portée « tout le personnage » confirmée ~00:52). **Nouvelle § 3.2** : fourrure **mohair cannelle `#B06A35`**, finition **mate**, poil court fin et dense (~3 mm, type minky) ; l'ancien orange vif `#F5821F` est **retiré comme couleur du personnage** (conservé dans l'historique) ; **règle de production** : générer la matière directement dans la couleur, jamais recolorer une photo orange éclairée (échec « brûlé » constaté le même jour) ; référence = `references/onyx-canonique-mohair-cannelle.webp` (buste validé ~00:53, médiane de fourrure mesurée `#AF612D`). **§ 1** : apparence et détail fixe nº 1 mis à jour, interdit reformulé (teinte de fourrure hors § 3.2), nouvelle référence couleur ajoutée (l'ancien maître devient « maître historique »). **§ 8** : paragraphe de prompt canonique mis à jour (mohair cannelle `#B06A35`, poil court — le reste verbatim). **Inchangés** : palette d'accent des surfaces (§ 3 : `#FC8B32`, `#C95D1D`, `#812900`, noir chaud, blanc), couleurs de série (§ 3.1), proportions (§ 7), logotype (§§ 10, 12), contrastes (§ 16), zéro hashtag (§ 17). Points ouverts consignés en § 3.2 : trio de nuances dérivées du pelage et ton du museau non tranchés. Aucun déploiement en ligne dans cette passe : la cascade de bascule est préparée localement (`bascule-cannelle-2026-11-26/`). |
| v1.3 | 26 novembre 2026 | **La couleur officielle du personnage change le matin même — « mohair cannelle miel clair »** (décision de l'opérateur, ~06:45 EST : choix nº 2 de la planche de comparaison des teintes produite le matin même — le cannelle de la nuit ressortait presque orange en plein soleil sur le toit — avec ordre de « repartir de zéro » sur cette base ; nouveau portrait officiel généré dans la teinte et validé dans la foulée). **§ 3.2 réécrite** : fourrure **mohair cannelle miel clair**, finition **mate**, poil court fin et dense (~3 mm, type minky) ; **valeur de référence = médiane de fourrure mesurée sur le portrait canonique : `#AD6A3D`** (le ton a été choisi sur image générée en scène réelle, pas sur nuancier — pas de hex nominal) ; le mohair cannelle `#B06A35` de la nuit **passe à l'historique** (remplacé avant tout déploiement) ; règle de production inchangée (générer directement dans la couleur, jamais recolorer) ; référence = `references/onyx-canonique-cannelle-miel-clair.webp` (MD5 `cb2f81dc…`) ; **museau** : celui du portrait fait foi tel quel (remarque montrée, aucun renfort demandé). **§ 1** : apparence, détail fixe nº 1 et interdit alignés ; nouvelle référence couleur en vigueur, la référence cannelle de la nuit devient « référence intermédiaire » historique. **§ 8** : paragraphe de prompt canonique mis à jour (mohair cannelle miel clair `#AD6A3D` — le reste verbatim). **Inchangés** : palette d'accent des surfaces (§ 3), couleurs de série (§ 3.1), proportions (§ 7), logotype (§§ 10, 12), contrastes (§ 16), zéro hashtag (§ 17). Point ouvert consigné en § 3.2 : trio de nuances dérivées du pelage non arrêté. Aucun déploiement en ligne dans cette passe : la cascade repart de zéro localement (`bascule-cannelle-miel-2026-11-26/`). |
