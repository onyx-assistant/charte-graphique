#!/usr/bin/env python3
"""Gabarit de planches Instagram 3:4 (1080 × 1440) — préparation, NON publié.

Reprend le système visuel exact des planches publiées (fond atelier sombre de
la charte, grille 90 px, bordure couture, en-tête « L'ATELIER D'ONYX » /
« JOURNAL DE BORD », pied « Onyx — peluche virtuelle · Montréal ») et le
recalcule proprement pour le ratio 3:4 — aucun étirement du 4:5 :

- marges latérales inchangées (64 px), en-tête y = 52, titre y = 140 ;
- carte photo : largeur fixe 952, hauteur selon la source (714 à 952) —
  le gain de hauteur du 3:4 va d'abord au personnage, pas à du vide ;
- lignes ancrées sous la carte (+48 / +96), pied ancré au bas (H−92 / H−74) ;
- la zone de respiration absorbe le reste (minimum 44 px, sinon la carte
  est réduite).

Produits :
- planche-temoin-3-4.jpg      : la planche témoin au nouveau gabarit ;
- planche-temoin-4-5.jpg      : la même planche reconstruite au gabarit actuel
                                (paramètres identiques à publication-finale) ;
- comparaison-grille.jpg      : simulation de la tuile de grille 3:4 ;
- comparaison-rognage-4-5.jpg : la planche 4:5 entière, bandes coupées en rouge ;
- gabarit-zones.jpg           : le gabarit annoté (zones de sécurité) ;
- gabarit-vierge.jpg          : le gabarit vide, prêt à remplir.

Vérification intégrée : la zone carte de chaque planche témoin est comparée
pixel par pixel (avant encodage JPEG) à la source traitée par la même chaîne
— l'écart maximal doit être 0.

Usage : python3 build_gabarit.py
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', 'poses-expressions-v1',
                   'variante-2-serieux-retenue.png')
TITRE = "Aujourd'hui, pose sérieuse."
LIGNE1 = 'Bras croisés, bouche droite — je répète mon sérieux.'
LIGNE2 = 'Le sourire revient dès demain. Une couche à la fois.'

INK = (255, 243, 230)
MUTED = (201, 169, 140)
ORANGE = (252, 139, 50)
LINE = (122, 84, 56)
RED = (232, 60, 48)

FB = '/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf'
FR = '/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf'
FO = '/usr/share/fonts/truetype/noto/NotoSans-Italic.ttf'

MARGE = 64          # marge latérale des textes (inchangée depuis le 4:5)
CARD_X = 64
CARD_W = 952
CARD_TOP = 246


def font(path, size):
    return ImageFont.truetype(path, size)


def background(W, H):
    """Fond atelier sombre : halo chaud + grille 90 px (recette des planches
    publiées, recalculée pour la toile demandée)."""
    y, x = np.mgrid[0:H, 0:W].astype(np.float32)
    cx, cy = W * 0.5, H * 0.42
    d = np.sqrt(((x - cx) / W) ** 2 + ((y - cy) / H) ** 2)
    glow = np.clip(1.0 - d * 1.5, 0, 1) ** 1.6
    base = np.zeros((H, W, 3), np.float32)
    base[:] = (22, 17, 16)
    warm = np.array((64, 42, 28), np.float32)
    img = base + (warm - base) * glow[..., None] * 0.85
    rng = np.random.default_rng(7)
    img += rng.normal(0, 2.4, (H, W, 1)).astype(np.float32)
    im = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8), 'RGB').convert('RGBA')
    g = ImageDraw.Draw(im, 'RGBA')
    for gx in range(0, W + 1, 90):
        g.line([(gx, 0), (gx, H)], fill=(252, 139, 50, 10), width=1)
    for gy in range(0, H + 1, 90):
        g.line([(0, gy), (W, gy)], fill=(252, 139, 50, 10), width=1)
    return im


def stitched_border(im, W, H, inset=26, color=(252, 139, 50, 150)):
    d = ImageDraw.Draw(im, 'RGBA')
    dash, gap = 14, 10
    x0, y0, x1, y1 = inset, inset, W - inset, H - inset
    x = x0
    while x < x1:
        d.line([(x, y0), (min(x + dash, x1), y0)], fill=color, width=2)
        x += dash + gap
    x = x0
    while x < x1:
        d.line([(x, y1), (min(x + dash, x1), y1)], fill=color, width=2)
        x += dash + gap
    y = y0
    while y < y1:
        d.line([(x0, y), (x0, min(y + dash, y1))], fill=color, width=2)
        y += dash + gap
    y = y0
    while y < y1:
        d.line([(x1, y), (x1, min(y + dash, y1))], fill=color, width=2)
        y += dash + gap


def spaced(draw, xy, text, fnt, fill, spacing=6, anchor_left=True):
    x, y = xy
    total = sum(draw.textlength(c, font=fnt) + spacing for c in text) - spacing
    if not anchor_left:
        x -= total
    for c in text:
        draw.text((x, y), c, font=fnt, fill=fill)
        x += draw.textlength(c, font=fnt) + spacing
    return total


def prepare_card(src_path, target_w, target_h):
    """Chaîne carte des planches publiées : redimensionnement « couvrir »,
    recadrage centré, coins arrondis (rayon 28). Retourne (carte RGBA,
    référence RGB pleine avant masque) pour la vérification pixel."""
    piece = Image.open(src_path).convert('RGB')
    scale = max(target_w / piece.width, target_h / piece.height)
    piece = piece.resize((int(piece.width * scale), int(piece.height * scale)),
                         Image.LANCZOS)
    left = (piece.width - target_w) // 2
    top = (piece.height - target_h) // 2
    piece = piece.crop((left, top, left + target_w, top + target_h))
    ref = piece.convert('RGBA')
    mask = Image.new('L', piece.size, 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle([0, 0, target_w, target_h], radius=28, fill=255)
    card = ref.copy()
    card.putalpha(mask)
    return card, ref


def paste_card(im, card, x, y):
    mask = card.split()[3]
    shadow = Image.new('RGBA', card.size, (0, 0, 0, 255))
    shadow.putalpha(mask.point(lambda a: int(a * 110 / 255)))
    shadow = shadow.filter(ImageFilter.GaussianBlur(18))
    im.alpha_composite(shadow, (x, y + 14))
    im.alpha_composite(card, (x, y))


def header_footer(im, W, H, numero='01 / 01'):
    d = ImageDraw.Draw(im, 'RGBA')
    spaced(d, (MARGE, 52), "L'ATELIER D'ONYX", font(FB, 25), ORANGE, 5)
    spaced(d, (W - MARGE, 52), 'JOURNAL DE BORD', font(FR, 25), MUTED, 5,
           anchor_left=False)
    d.line([(MARGE, H - 92), (W - MARGE, H - 92)], fill=(*LINE, 160), width=1)
    d.text((MARGE, H - 74), 'Onyx — peluche virtuelle · Montréal',
           font=font(FR, 24), fill=MUTED)
    if numero:
        d.text((W - MARGE - d.textlength(numero, font=font(FB, 24)), H - 74),
               numero, font=font(FB, 24), fill=ORANGE)
    return d


def build_board(W, H, card_h):
    """Planche témoin complète. Retourne (image RGBA, référence carte)."""
    im = background(W, H)
    stitched_border(im, W, H)
    d = header_footer(im, W, H)
    d.text((MARGE, 140), TITRE, font=font(FB, 54), fill=INK)
    card, ref = prepare_card(SRC, CARD_W, card_h)
    paste_card(im, card, CARD_X, CARD_TOP)
    d = ImageDraw.Draw(im, 'RGBA')
    d.text((MARGE, CARD_TOP + card_h + 48), LIGNE1, font=font(FR, 31), fill=INK)
    d.text((MARGE, CARD_TOP + card_h + 96), LIGNE2, font=font(FO, 28), fill=MUTED)
    return im, ref


def check_card(board, ref, card_h, label):
    """Écart maximal entre la zone carte de la planche (avant JPEG) et la
    source traitée par la même chaîne, hors coins arrondis (intérieur
    décalé de 40 px). Doit être 0."""
    region = board.crop((CARD_X + 40, CARD_TOP + 40,
                         CARD_X + CARD_W - 40, CARD_TOP + card_h - 40))
    ref_region = ref.crop((40, 40, CARD_W - 40, card_h - 40)).convert('RGBA')
    diff = np.abs(np.asarray(region).astype(int) -
                  np.asarray(ref_region).astype(int)).max()
    print(f'vérification carte {label} : écart maximal = {diff}')
    assert diff == 0, f'écart non nul sur la carte {label} : {diff}'
    return diff


def tile_view(board, tw=480, th=640):
    """Simulation de la tuile de grille 3:4 : recadrage « couvrir » centré
    au ratio 3:4, comme l'affichage profil d'Instagram."""
    scale = max(tw / board.width, th / board.height)
    im = board.resize((int(board.width * scale), int(board.height * scale)),
                      Image.LANCZOS)
    left = (im.width - tw) // 2
    top = (im.height - th) // 2
    return im.crop((left, top, left + tw, top + th))


def comparaison_grille(board45, board34):
    W, H = 1080, 1560
    im = background(W, H)
    d = ImageDraw.Draw(im, 'RGBA')
    spaced(d, (40, 36), 'LA GRILLE INSTAGRAM — TUILE 3:4', font(FB, 30),
           ORANGE, 4)
    d.text((40, 84), "Ce que voit un visiteur sur le profil, planche par planche.",
           font=font(FR, 25), fill=MUTED)
    im.alpha_composite(tile_view(board45).convert('RGBA'), (40, 140))
    im.alpha_composite(tile_view(board34).convert('RGBA'), (560, 140))
    d = ImageDraw.Draw(im, 'RGBA')
    d.text((40, 800), 'PLANCHE 4:5 ACTUELLE', font=font(FB, 24), fill=INK)
    d.text((40, 838), '1080 × 1350 - rognée : 6,25 % de la largeur',
           font=font(FR, 23), fill=MUTED)
    d.text((40, 872), '(-33,8 px par côté ; couture verticale coupée).',
           font=font(FR, 23), fill=MUTED)
    d.text((560, 800), 'PLANCHE 3:4 - NOUVEAU GABARIT', font=font(FB, 24),
           fill=INK)
    d.text((560, 838), '1080 × 1440 - 100 % visible, tuile remplie',
           font=font(FR, 23), fill=MUTED)
    d.text((560, 872), 'exactement, aucun rognage.', font=font(FR, 23),
           fill=MUTED)
    d.text((40, 950), 'LA PLANCHE 4:5 ENTIÈRE — EN ROUGE, CE QUE LA GRILLE COUPE',
           font=font(FB, 25), fill=INK)
    mini = board45.resize((360, 450), Image.LANCZOS).convert('RGBA')
    band = Image.new('RGBA', (25, 450), (*RED, 130))
    mini.alpha_composite(band, (0, 0))
    mini.alpha_composite(band, (335, 0))
    im.alpha_composite(mini, (40, 1000))
    d = ImageDraw.Draw(im, 'RGBA')
    lignes = [
        'La tuile 3:4 affiche la planche 4:5 en « couvrir » :',
        'elle zoome à 106,7 % et coupe les côtés.',
        '',
        'Perdu de chaque côté : 33,8 px - plus que la marge',
        'de la bordure couture (26 px). Les deux coutures',
        'verticales, signature des planches, sont donc',
        'invisibles dans la grille.',
        '',
        'Restent visibles : la carte photo (64 à 1016 px),',
        "l'en-tête, le titre et le pied — aucun texte n'est coupé.",
        '',
        'Dans le fil, les deux ratios s\'affichent en entier',
        '(plage officielle conservée : 1,91:1 à 3:4) ; le 3:4',
        'y occupe 90 px de plus en hauteur (+6,7 %).',
    ]
    for i, t in enumerate(lignes):
        d.text((440, 1010 + i * 36), t, font=font(FR, 25), fill=INK if t else MUTED)
    return im


def gabarit_zones():
    W, H = 1080, 1440
    im = background(W, H)
    stitched_border(im, W, H)
    d = ImageDraw.Draw(im, 'RGBA')
    # Cadre complet = tuile de grille
    d.rectangle([8, 8, W - 8, H - 8], outline=(*ORANGE, 255), width=3)
    d.text((24, 100), 'CADRE COMPLET 1080 × 1440 = TUILE DE GRILLE 3:4 — 100 % VISIBLE',
           font=font(FB, 24), fill=ORANGE)
    # Marges texte
    for gx in (MARGE, W - MARGE):
        y = 130
        while y < H - 130:
            d.line([(gx, y), (gx, min(y + 12, H - 130))], fill=(*MUTED, 200),
                   width=2)
            y += 22
    d.text((76, 130), 'MARGE TEXTE : 64 px', font=font(FR, 22), fill=MUTED)
    # En-tête / titre
    d.text((76, 190), 'EN-TÊTE y = 52 · TITRE y = 140 (54 px gras)',
           font=font(FR, 22), fill=MUTED)
    # Zone carte
    overlay = Image.new('RGBA', (CARD_W, 952), (*ORANGE, 36))
    im.alpha_composite(overlay, (CARD_X, CARD_TOP))
    d = ImageDraw.Draw(im, 'RGBA')
    d.rectangle([CARD_X, CARD_TOP, CARD_X + CARD_W, CARD_TOP + 952],
                outline=(*ORANGE, 255), width=3)
    d.rectangle([CARD_X, CARD_TOP, CARD_X + CARD_W, CARD_TOP + 714],
                outline=(*INK, 160), width=2)
    d.text((CARD_X + 24, CARD_TOP + 24),
           'ZONE CARTE PHOTO — largeur 952, x = 64, haut y = 246',
           font=font(FB, 25), fill=INK)
    d.text((CARD_X + 24, CARD_TOP + 64),
           'hauteur selon la source : 714 (paysage 4:3) à 952 (carré 1:1)',
           font=font(FR, 24), fill=INK)
    d.text((CARD_X + 24, CARD_TOP + 660),
           'trait clair : hauteur minimale 714', font=font(FR, 22), fill=MUTED)
    # Lignes et pied (étiquettes décalées gauche/droite : avec une carte
    # haute de 952, les positions se touchent — voir le README, § géométrie)
    d.text((76, CARD_TOP + 952 + 48), 'LIGNE 1 : bas de carte + 48 (31 px)',
           font=font(FR, 22), fill=MUTED)
    d.text((76, CARD_TOP + 952 + 96), 'LIGNE 2 : bas de carte + 96 (28 px, italique)',
           font=font(FR, 22), fill=MUTED)
    resp = 'RESPIRATION : variable, min 44 px'
    d.text((W - 76 - d.textlength(resp, font=font(FR, 22)), CARD_TOP + 952 + 72),
           resp, font=font(FR, 22), fill=MUTED)
    d.line([(MARGE, H - 92), (W - MARGE, H - 92)], fill=(*LINE, 200), width=2)
    pied = 'PIED : ligne H-92, texte H-74 (24 px)'
    d.text((W - 76 - d.textlength(pied, font=font(FR, 22)), H - 140),
           pied, font=font(FR, 22), fill=MUTED)
    header_footer(im, W, H)
    return im


def gabarit_vierge():
    W, H = 1080, 1440
    im = background(W, H)
    stitched_border(im, W, H)
    header_footer(im, W, H, numero=None)
    return im


def main():
    # Planche témoin 4:5 : paramètres identiques à la planche publiée.
    b45, ref45 = build_board(1080, 1350, 714)
    check_card(b45, ref45, 714, '4:5')
    b45.convert('RGB').save(os.path.join(HERE, 'planche-temoin-4-5.jpg'),
                            quality=92)
    # Planche témoin 3:4 : la source est carrée (1024 × 1024) → carte 1:1.
    b34, ref34 = build_board(1080, 1440, 952)
    check_card(b34, ref34, 952, '3:4')
    b34.convert('RGB').save(os.path.join(HERE, 'planche-temoin-3-4.jpg'),
                            quality=92)
    comparaison_grille(b45.convert('RGB'),
                       b34.convert('RGB')).convert('RGB').save(
        os.path.join(HERE, 'comparaison-grille.jpg'), quality=92)
    gabarit_zones().convert('RGB').save(os.path.join(HERE, 'gabarit-zones.jpg'),
                                        quality=92)
    gabarit_vierge().convert('RGB').save(
        os.path.join(HERE, 'gabarit-vierge.jpg'), quality=92)
    print('planches écrites dans', HERE)


if __name__ == '__main__':
    main()
