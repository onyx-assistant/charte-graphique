# Typographie et logotype Onyx — choix v1

_22 novembre 2026 · Chantier « angles morts » nº 1 du plan de projet. Version 1 assumée : en service dès maintenant, à raffiner en v2. l'atelier a délégué entièrement les normes graphiques à Onyx._

## Les choix

### Police d'affichage et de logotype : **Fredoka** (SemiBold 600)

Formes géométriques très rondes et pleines : son « O » presque circulaire répond à la tête ronde de la peluche, ses traits épais et doux donnent le côté « toutou » sans tomber dans le dessin animé criard. En SemiBold, elle reste structurée et propre — crédible sur GitHub comme sur une couverture de vidéo. Variable (300–700, plus un axe de largeur gardé à 100 %), licence SIL OFL 1.1.

### Police de texte : **Nunito** (400 / 600 / 800 + italique)

Terminaisons rondes, même famille d'esprit que Fredoka, mais dessinée pour lire : légendes, sous-titres, textes de miniature et interface. C'est la seule des candidates à offrir une **italique véritable** et une échelle de graisses très large (200–1000) — un seul fichier variable couvre tous les besoins de texte. Licence SIL OFL 1.1.

### Critère éliminatoire tenu

Les quatre candidates ont été vérifiées **caractère par caractère** : toutes couvrent l'ensemble des diacritiques français (à â ä ç é è ê ë î ï ô ö ù û ü ÿ, æ, œ, majuscules accentuées, « »). Le français est la langue première du projet ; aucune police incomplète n'était acceptable.

## Pourquoi pas les autres candidates

- **Baloo 2** (Bold) : très proche en esprit, mais son côté « ballon gonflé » et sa queue de « y » fantaisiste tirent vers la fête d'enfants ; moins à l'aise sur les surfaces professionnelles (GitHub, site). Gardée en réserve si un jour une déclinaison plus ludique est voulue.
- **Quicksand** (Bold) : élégante et géométrique, mais trop fine et délicate — elle s'efface à côté d'une peluche toute en rondeurs, et manque de présence en miniature.
- **Nunito en affichage** : impeccable en texte, mais trop neutre pour porter seule un logotype ; elle reste la voix des paragraphes, pas celle du nom.

Planche de comparaison produite pendant l'évaluation : `specimen/comparaison-candidates.png`.

## Le logotype v1

Le mot « **Onyx** » en Fredoka SemiBold 600, « O » majuscule suivi du bas de casse, sans retouche des lettres (crénage d'origine de la police). Couleurs strictement celles de la charte (§ 3) :

| Fichier | Usage |
|---|---|
| `logo/logo-onyx-sombre.png` | Orange lumière `#FC8B32` sur fond sombre `#161110` — déclinaison principale |
| `logo/logo-onyx-clair.png` | Orange médian `#C95D1D` sur blanc — surfaces claires |
| `logo/logo-onyx-monochrome-noir.png` | Noir chaud ~`#1A1512`, fond transparent — usage une encre |
| `logo/logo-onyx-monochrome-blanc.png` | Blanc, fond transparent — sur photos et fonds colorés |
| `logo/logo-onyx-icone-texte-sombre.png` | Verrouillage icône + texte, fond sombre |
| `logo/logo-onyx-icone-texte-clair.png` | Verrouillage icône + texte, fond clair |
| `logo/icone-tete-onyx-1000.png` / `-512.png` | La tête de la référence canonique, recadrée carrée **telle quelle** (boîte mesurée par analyse d'image : x 301–1301, y 218–1218 sur 1600) — aucune retouche, aucun redessin |

Reproduction : `python3 build_logo.py` (logotype et icône), `python3 build_specimen.py` (planche). Planche spécimen : `specimen/planche-specimen-v1.png` et `.pdf` — logotype, alphabet Fredoka, exemples Nunito, carte de titre de vidéo, légende type et miniature YouTube fictive (« JE DIS COUCOU ! »).

Les polices et leurs licences sont dans `fonts/` (fichiers variables TTF + textes OFL). Attention : les fichiers variables ont des graisses par défaut basses (Fredoka 300, Nunito 200) — toujours régler l'axe `wght` explicitement (Fredoka 600 ; Nunito selon l'usage), comme le font les scripts.

## À raffiner en v2

- **Vectoriser le logotype** (SVG/EPS) et régler le crénage à la main, pour l'impression et les très grands formats.
- **Variante empilée** du verrouillage (icône au-dessus du texte) pour les formats carrés et les avatars de plateformes.
- **Favicon** et kit réseaux sociaux (bannières, photos de couverture) déclinés du logotype.
- **Épreuves physiques** si impression un jour (la variante claire en `#C95D1D` est choisie pour rester lisible sur papier ; à confirmer par une épreuve, comme la charte l'exige pour la couleur).
- Tester la tenue du logotype en **très petit corps** (filigrane vidéo, coin de miniature) et, au besoin, graisser une déclinaison « petit format ».
