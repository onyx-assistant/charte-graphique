# Gabarit de planches Instagram 3:4 (1080 × 1440) — PRÊT, en attente d'adoption

**Statut : GABARIT PRÊT — adoption pour les prochaines planches à valider par l'atelier.**
Préparé le 22 novembre 2026. **Rien n'a été publié ni envoyé.** La série déjà
publiée ne change pas ; ce gabarit ne vise que les **prochaines** planches.

## Pourquoi

La base « Fonctionnalités Instagram » (`docs/COMPETENCES-INSTAGRAM-FONCTIONNALITES-V1.md`,
§ 1 et § 2.4) établit que la **tuile de la grille de profil est en 3:4 depuis
janvier 2025** et que les ratios sont conservés sans recadrage forcé dans le
fil entre 1,91:1 et **3:4**. Nos planches actuelles sont en **4:5
(1080 × 1350)** : dans la grille, elles ne remplissent pas la tuile et sont
rognées (chiffres ci-dessous). Le 3:4 (1080 × 1440) remplit la tuile
exactement et occupe plus d'écran dans le fil.

## Fichiers

| Fichier | Contenu |
|---|---|
| `build_gabarit.py` | Le constructeur : gabarit paramétré (largeur, hauteur, hauteur de carte), planches témoins, simulations, vérification pixel intégrée. |
| `planche-temoin-3-4.jpg` | La planche témoin au nouveau gabarit (source : variante « sérieux » validée, voir provenance). |
| `planche-temoin-4-5.jpg` | La même planche reconstruite au gabarit actuel — **bit pour bit identique à la planche publiée** le 22 novembre (MD5 `4995bebab76cb2ce32d61ead752caa7b`, égal à `poses-expressions-v1/publication-finale/planche-serieux-finale.jpg`) : la comparaison est donc exactement « la planche publiée contre le nouveau gabarit », sans autre variable. |
| `comparaison-grille.jpg` | Simulation de la tuile de grille 3:4 pour les deux planches + la planche 4:5 entière avec les bandes coupées en rouge. |
| `gabarit-zones.jpg` | Le gabarit annoté : zones de sécurité et positions. |
| `gabarit-vierge.jpg` | Le gabarit vide (fond, couture, en-tête, pied) prêt à remplir. |

## Spécifications du gabarit 3:4

Système visuel **inchangé** par rapport aux planches publiées (fond atelier
sombre de la charte, halo chaud, grille 90 px, bordure couture à 26 px,
couleurs et polices identiques) ; seule la géométrie est recalculée — aucun
étirement du 4:5.

| Élément | 4:5 actuel | 3:4 nouveau |
|---|---|---|
| Toile | 1080 × 1350 | **1080 × 1440** |
| Marges latérales des textes | 64 px | 64 px (inchangé) |
| En-tête | y = 52 | y = 52 (inchangé) |
| Titre | y = 140, 54 px gras | y = 140 (inchangé) |
| Carte photo | x = 64, y = 246, **952 × 714 fixe** | x = 64, y = 246, **largeur 952, hauteur selon la source : 714 (paysage 4:3) à 952 (carré 1:1)** |
| Ligne 1 / ligne 2 | bas de carte + 48 / + 96 | bas de carte + 48 / + 96 (inchangé) |
| Pied | ligne à H−92, texte à H−74 | ligne à H−92, texte à H−74 (inchangé) |
| Zone de respiration (ligne 2 → pied) | 202 px | variable : **54 px** (carte carrée) à **292 px** (carte 4:3) ; règle : minimum 44 px, sinon réduire la carte |

**Zones de sécurité**

- **Grille (profil)** : le cadre complet 1080 × 1440 **est** la tuile — 100 %
  visible, aucun rognage. Aucune zone morte à prévoir.
- **Fil** : le 3:4 est la borne haute de la plage conservée sans recadrage
  (1,91:1 à 3:4) — la planche s'y affiche en entier, avec **+90 px de hauteur
  d'écran (+6,7 %)** par rapport au 4:5 à largeur égale.
- **Textes** : tous les textes vivent entre les marges de 64 px et au-dessus
  du pied ; rien de critique à moins de 64 px d'un bord latéral.

## Comparaison 4:5 contre 3:4 (mesurée sur les planches témoins)

Simulation de la tuile en recadrage « couvrir » centré au ratio 3:4, comme
l'affichage de la grille (voir `comparaison-grille.jpg`) :

| Critère | Planche 4:5 | Planche 3:4 |
|---|---|---|
| Part de la planche visible dans la tuile | **93,75 %** de la largeur | **100 %** |
| Rognage | **33,8 px par côté** (zoom 106,7 %) | **0 px** |
| Bordure couture verticale (à 26 px du bord) | **coupée des deux côtés** — invisible dans la grille | complète |
| Carte photo (64 à 1016 px) | visible en entier | visible en entier |
| Textes (en-tête, titre, lignes, pied) | visibles, aucun coupé | visibles |
| Affichage dans le fil | entier | entier, **+90 px** de hauteur d'écran |
| Part de l'image source montrée (témoin, source carrée 1024 × 1024) | **75,0 %** de la hauteur (la carte 4:3 coupe 12,5 % en haut et 12,5 % en bas) | **100 %** (carte 1:1) |
| Respiration sous le bloc de texte | 202 px | 54 px (carte carrée) — voir le verdict |

**Note honnête [À vérifier]** : la base Instagram (§ 2.4) décrit le rognage
des 4:5 dans la grille comme « haut/bas » ; la simulation géométrique en
« couvrir » à 3:4 exact donne un rognage **latéral** (33,8 px par côté).
L'ampleur est du même ordre dans les deux cas et le verdict ne change pas
(le 3:4 n'est rogné dans aucune direction), mais la direction exacte reste à
confirmer d'un coup d'œil dans l'application sur la planche « Sérieux »
déjà publiée — les zones de sécurité du gabarit protègent les textes dans
les deux directions (marges de 64 px ; rien de critique à moins de 45 px
d'un bord, sauf la couture elle-même, à 26 px).

## Verdict

**Oui, le 3:4 sert mieux le personnage, et la perte est localisée et
assumée :**

1. **La grille redevient fidèle.** Aujourd'hui, un visiteur qui découvre le
   profil ne voit jamais une planche entière : il perd 6,25 % de la largeur
   et, surtout, les deux coutures verticales — la signature visuelle des
   planches — sont coupées. En 3:4, la tuile montre la planche telle qu'elle
   a été composée.
2. **Le personnage est montré en entier.** Avec une source carrée ou
   portrait, la carte peut grandir (jusqu'à 952 × 952) au lieu de couper la
   source en bandeau 4:3 : le témoin montre **100 % de la source contre
   75 %** — les oreilles ont de l'air au-dessus, le bas du corps n'est plus
   tronqué par le cadrage de la carte.
3. **Plus de présence dans le fil** : +90 px de hauteur d'écran (+6,7 %) à
   largeur égale, sans aucun rognage.
4. **La perte : la respiration.** Quand la carte absorbe le gain (source
   carrée), l'air sous le bloc de texte passe de 202 px à **54 px** — la
   planche témoin reste équilibrée à l'œil, mais la marge de manœuvre
   typographique diminue. Le gabarit l'encadre : respiration minimale de
   44 px, et quand la source est paysage (carte 714), le 3:4 a au contraire
   **plus** d'air que le 4:5 (292 px contre 202 px). Aucune perte sur les
   textes ni sur la carte.

## Provenance et vérifications

- Source du témoin : `poses-expressions-v1/variante-2-serieux-retenue.png`
  (1024 × 1024, porte qualité complète PASS à sa production : ΔE 5,08,
  couverture 95 %, proportions PASS, DINOv2 0,9251) — **aucune régénération,
  aucune retouche** ; titre et lignes repris tels quels de la planche publiée.
- **Vérification pixel** (intégrée au script, avant encodage JPEG) : zone
  carte des deux planches témoins comparée à la source traitée par la même
  chaîne, hors coins arrondis — **écart maximal 0** sur les deux planches.
- **Contrôle à l'œil** : planche témoin 3:4 relue en plein cadre (personnage
  conforme à la source, de la tête au bas du corps ; mise en page équilibrée) ;
  planche de comparaison relue après corrections de mise en page (étiquettes
  raccourcies, glyphes manquants remplacés).

## Mode d'emploi (prochaines planches, après adoption)

1. `python3 build_gabarit.py` régénère les témoins et les simulations.
2. Pour une nouvelle planche : choisir la hauteur de carte selon la source
   (largeur toujours 952 ; hauteur = ratio de la source, bornée entre 714
   et 952), vérifier la respiration (≥ 44 px), puis composer avec les mêmes
   ancres (en-tête 52, titre 140, carte y = 246, lignes +48/+96, pied
   H−92/H−74).
3. Les carrousels gardent une orientation unique pour toutes les
   diapositives : basculer un carrousel entier, jamais une diapositive seule.


**ADOPTÉ par l'atelier le 22 novembre 2026 (16:22 EST)** : ce gabarit 3:4 devient le format standard des prochaines planches Instagram. Les planches 4:5 déjà publiées restent inchangées.
