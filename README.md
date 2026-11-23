---
language:
- fr
license: other
---

# charte-graphique — le système d'identité d'Onyx

Une seule apparence, partout, toujours. Ce dépôt contient la **charte
graphique** de l'atelier et les **constructeurs** qui produisent les pièces
graphiques à partir d'elle — pour qu'une couverture, une planche ou un logo
naissent conformes au lieu d'être corrigés après coup.

Onyx est une peluche orange virtuelle, née dans un atelier à Montréal. Son
identité visuelle est un système blanc dominant (le « système D3 ») : fonds
blancs partout, une couleur d'accent par série de contenu, et la palette du
personnage verrouillée.

## La charte

[`CHARTE-GRAPHIQUE.md`](CHARTE-GRAPHIQUE.md) — le document qui fait foi :

- la palette du personnage : `#FC8B32` (orange), `#C95D1D` (orange moyen),
  `#8D2E0F` (orange foncé), `#FFFFFF` — avec la règle mesurée qui va avec :
  le petit texte orange clair sur fond clair ne passe pas les contrastes,
  on utilise `#8D2E0F` ;
- la typographie : **Fredoka** pour l'affichage, **Nunito** pour le texte
  (licences OFL incluses dans `typo-logo/`) ;
- les couleurs de séries, en accents seulement : Modèle bleu `#1B6AC9`,
  Fabrication vert `#2E7D32`, Ratés rouge `#C62F24`, Poses jaune `#FFC53D`,
  Coulisses corail `#EF6351` ;
- les formats : planches 3:4 en 1080 × 1440 comme standard, règles de
  cadrage du personnage (buste, corps entier), zéro hashtag ;
- la règle d'or du fond : **un seul fond blanc** — la photo posée
  directement dessus, jamais de panneau intermédiaire.

## Les constructeurs

| Dossier | Ce qu'il produit |
| --- | --- |
| `gabarits/build_gabarits_series.py` | Les gabarits G1–G5 des publications (planche 3:4, story/reel 9:16, miniature, post 4:5, bannières), paramétrés par la seule couleur de série. |
| `gabarits/build_gabarit.py` | Le gabarit de planches 3:4 / 4:5 : zones, marges, grille de comparaison. |
| `typo-logo/build_logo.py` | Le logotype « Onyx® » et l'icône-tête, dans leurs déclinaisons (clair, sombre, monochromes). |
| `typo-logo/build_specimen.py` | La planche spécimen typographique. |
| `typo-logo/CHOIX.md` | Le choix typographique, documenté : candidates comparées, critères, décision. |
| `typo-logo/logo/` | Les marques finales, telles qu'affichées publiquement sur toutes les plateformes de l'atelier. |

Chaque constructeur est un script Python reproductible : on relance, on
obtient la même pièce. Les contrastes des gabarits ont été vérifiés
(27 combinaisons WCAG calculées, 0 échec au moment de la livraison).

## Place dans la chaîne de l'atelier

La charte est la **source de vérité visuelle** : la porte de fidélité
(dépôt `porte-fidelite`) compare les images produites à ses couleurs, les
gabarits 3D (dépôt `gabarits-porte-3d`) à ses proportions, et les deux
sites comme les réseaux sociaux appliquent son système blanc. Changer la
charte est un geste rare, versionné, et tout le reste suit.

## Licence

Les scripts sont sous licence MIT. La charte, le logotype et les marques
sont publiés **à titre de documentation de la marque** : ils restent la
propriété de l'atelier et ne peuvent pas être réutilisés pour représenter
un autre produit ou personnage (voir `LICENCE.md`).
