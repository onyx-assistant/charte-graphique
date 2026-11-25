# -*- coding: utf-8 -*-
"""Gabarits de publication G1–G5 paramétrés « série » — charte graphique v1.0,
système D3-blanc unifié (§ 3.1 séries, § 15 gabarits, § 16.1 contrastes).

Constructeur UNIQUE pour toutes les pièces futures. Le paramètre central est
la SÉRIE : un seul choix parmi les 5, qui règle la couleur d'accent partout
(pastille, numéro géant en teinte pâle, bordure couture, filets, bandeau bas,
anneau). Le personnage n'est jamais régénéré ni retouché : détourage canonique
existant `layers/onyx-alpha.png`, posé sur sa plaque crème d'identité #FFF8F1.

Socle repris des constructeurs versionnés validés du projet (mêmes fonctions,
même recette) : `instagram-direction-v2/lot-migration-v1/construire-lot.py`
(lot D3-blanc validé par l'atelier) et `construire-exemples-d3-revise.py`.

Correspondance des numéros (détail au README) :
- G1 planche Instagram 3:4 1080×1440   (§ 15, remplace le 4:5 ; avenant § D G1)
- G2 story / couverture reel 9:16 1080×1920 (§ 15 nº 01 ; avenant § D G3+G4)
- G3 miniature YouTube 16:9 1280×720   (§ 15 nº 02)
- G4 publication Instagram 4:5 1080×1350 (§ 15 nº 03 — conservé, pièces héritées)
- G5 bannière YouTube 2560×1440 (§ 15 nº 04) + écran live 16:9 1920×1080 (§ 15 nº 05)
- GA couvertures de highlights 1080×1080, une par série (avenant § D G2)
- GB simulation de grille (contrôle avant publication ; avenant § D G5)

Règles de contraste appliquées dans le code (§ 16.1) :
- petit texte sur blanc : noir chaud ou orange ombre #812900 seulement ;
- jamais d'orange vif #FC8B32 en petit texte sur clair ;
- jamais de texte blanc sur le jaune série (1,58:1) — texte porté = noir chaud ;
- jaune série en texte sur blanc interdit (1,58:1) → remplacé par le noir chaud ;
- corail série en texte sur blanc = 3,19:1 → grands titres seulement, jamais
  en petit texte (remplacé par le noir chaud) ;
- texte porté par bleu/vert/rouge série (pastilles, bandes) = blanc (≥ 5,13:1).

Usage :
    python3 build_gabarits_series.py                 # tous les témoins + annexes
    python3 build_gabarits_series.py --serie poses   # un témoin par gabarit, série imposée
    python3 build_gabarits_series.py --gabarit G1    # un seul gabarit
Aucune publication : les sorties vivent dans ce dossier.
"""
import argparse
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

PROJ = "<racine-du-projet>"
HERE = os.path.join(PROJ, "gabarits-v1")
FONTS = os.path.join(PROJ, "typo-logo-v1", "fonts")
CHAR = Image.open(os.path.join(PROJ, "layers", "onyx-alpha.png")).convert("RGBA")

BLANC = (255, 255, 255)      # #FFFFFF fond dominant (charte § 3.1)
NOIR = (26, 21, 18)          # #1A1512 noir chaud
BRUN = (74, 55, 40)          # texte secondaire sur blanc
CREME = (255, 243, 230)      # #FFF3E6
PLAQUE = (255, 248, 241)     # #FFF8F1 plaque personnage / scène claire
OMBRE = (129, 41, 0)        # #812900 orange ombre (petit texte orange sur clair)

# ---- LE paramètre « série » : un choix parmi les 5 (charte § 3.1) ----
SERIES = {
    "modele":      dict(nom="FEUILLE DE MODÈLE", court="MODÈLE",      couleur=(27, 106, 201),  numero=1),   # #1B6AC9
    "fabrication": dict(nom="FABRICATION",       court="FABRICATION", couleur=(46, 125, 50),   numero=2),   # #2E7D32
    "rates":       dict(nom="RATÉS",             court="RATÉS",       couleur=(198, 47, 36),   numero=3),   # #C62F24
    "poses":       dict(nom="POSES",             court="POSES",       couleur=(255, 197, 61),  numero=4),   # #FFC53D
    "coulisses":   dict(nom="COULISSES",         court="COULISSES",   couleur=(239, 99, 81),   numero=5),   # #EF6351
}
JAUNE = SERIES["poses"]["couleur"]
CORAIL = SERIES["coulisses"]["couleur"]


def F(name, size, var=None):
    f = ImageFont.truetype(os.path.join(FONTS, name), size)
    if var:
        try:
            f.set_variation_by_name([var])
        except Exception:
            pass
    return f


def fred(size):
    return F("Fredoka.ttf", size, "SemiBold")


def nun(size, italic=False):
    return F("Nunito-Italic.ttf" if italic else "Nunito.ttf", size)


# ---------------- contrastes (WCAG 2.2, formule § 16.1) ----------------

def lum(rgb):
    def ch(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = rgb
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def ratio(fg, bg):
    l1, l2 = lum(fg), lum(bg)
    if l1 < l2:
        l1, l2 = l2, l1
    return (l1 + 0.05) / (l2 + 0.05)


CHECKS = []


def check(label, fg, bg):
    CHECKS.append((label, fg, bg, ratio(fg, bg)))


def hexs(rgb):
    return "#%02X%02X%02X" % rgb


def teinte(rgb, part_blanc=0.82):
    """Teinte pâle d'une couleur de série (numéro géant, décor — jamais du texte)."""
    return tuple(int(c * (1 - part_blanc) + 255 * part_blanc) for c in rgb)


def texte_sur(couleur):
    """Texte porté PAR la couleur de série (pastilles, bandes) — § 3.1."""
    return NOIR if couleur in (JAUNE, CORAIL) else BLANC


def accent_texte(couleur, grand=False):
    """Couleur de série utilisée EN texte sur fond blanc, règles § 16.1 :
    jaune → noir chaud toujours ; corail → série en grand texte seulement."""
    if couleur == JAUNE:
        return NOIR
    if couleur == CORAIL and not grand:
        return NOIR
    return couleur


# ---------------- socle commun (recette du lot D3-blanc validé) ----------------

def base(couleur, numero=None, w=1080, h=1440):
    """Fond blanc dominant + numéro géant en teinte pâle + bordure couture série."""
    img = Image.new("RGB", (w, h), BLANC)
    d = ImageDraw.Draw(img)
    if numero:
        taille = int(w * 0.40)
        d.text((w - int(w * 0.037), int(h * 0.062)), "%02d" % numero,
               font=fred(taille), fill=teinte(couleur), anchor="ra")
    for x in range(30, w - 30, 26):
        d.line([x, 26, x + 14, 26], fill=couleur, width=3)
        d.line([x, h - 22, x + 14, h - 22], fill=couleur, width=3)
    for y in range(30, h - 22, 26):
        d.line([26, y, 26, y + 14], fill=couleur, width=3)
        d.line([w - 29, y, w - 29, y + 14], fill=couleur, width=3)
    return img


def header(img, couleur, y=52):
    d = ImageDraw.Draw(img)
    d.text((64, y), "L'ATELIER D'ONYX", font=fred(30), fill=NOIR)
    d.text((img.width - 64, y), "JOURNAL DE BORD", font=fred(30),
           fill=accent_texte(couleur), anchor="ra")
    check("en-tête noir/blanc", NOIR, BLANC)


def footer(img, couleur, num=None, total=None, spec=None, y_filet=None):
    d = ImageDraw.Draw(img)
    w, h = img.size
    y_filet = y_filet if y_filet is not None else h - 144
    d.line([64, y_filet, w - 64, y_filet], fill=couleur, width=2)
    if spec:
        d.text((64, y_filet + 22), spec, font=fred(23), fill=NOIR)
    d.text((64, h - 72), "Onyx — peluche virtuelle · Montréal", font=nun(26), fill=BRUN)
    if num is not None:
        d.text((w - 64, h - 72), "%02d / %02d" % (num, total), font=fred(28),
               fill=accent_texte(couleur), anchor="ra")
    d.rectangle([0, h - 14, w, h], fill=couleur)
    check("pied brun/blanc", BRUN, BLANC)


def pill(img, x, y, text, couleur, size=27):
    d = ImageDraw.Draw(img)
    f = fred(size)
    tw = d.textlength(text, font=f)
    d.rounded_rectangle([x, y, x + tw + 44, y + 54], radius=27, fill=couleur)
    d.text((x + 22, y + 27), text, font=f, fill=texte_sur(couleur), anchor="lm")
    check("pastille « %s »" % text[:26], texte_sur(couleur), couleur)
    return x + tw + 44


def titre(img, x, y, lignes, couleur, size=76):
    """lignes : liste de (texte, est_accent). Retourne le y sous le titre."""
    d = ImageDraw.Draw(img)
    size_cur = size
    while size_cur > 30:
        f = fred(size_cur)
        if all(d.textlength(t, font=f) <= img.width - 128 for t, _ in lignes):
            break
        size_cur -= 4
    f = fred(size_cur)
    for t, acc in lignes:
        coul = accent_texte(couleur, grand=True) if acc else NOIR
        d.text((x, y), t, font=f, fill=coul)
        if acc:
            check("titre accent (grand texte)", coul, BLANC)
        y += int(size_cur * 1.09)
    return y


def wrap(d, text, fnt, maxw):
    words, lines, cur = text.split(), [], ""
    for wd in words:
        t = (cur + " " + wd).strip()
        if d.textlength(t, font=fnt) <= maxw:
            cur = t
        else:
            lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def caption(img, x, y, text, size=33, fill=BRUN, maxw=None, center=False, italic=True):
    d = ImageDraw.Draw(img)
    f = nun(size, italic=italic)
    maxw = maxw or (img.width - 128)
    yy = y
    for ln in wrap(d, text, f, maxw):
        xx = x + ((maxw - d.textlength(ln, font=f)) / 2 if center else 0)
        d.text((xx, yy), ln, font=f, fill=fill)
        yy += int(size * 1.35)
    check("texte courant", fill, BLANC)
    return yy


def char_plate(cw, ch, plate=PLAQUE, radius=30):
    """Plaque crème d'identité #FFF8F1 + personnage détouré canonique + ombre
    douce. Aucun pixel du personnage n'est modifié (recette validée)."""
    img = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([4, 4, cw - 4, ch - 4], radius=radius, fill=plate + (255,))
    bbox = CHAR.getbbox()
    char = CHAR.crop(bbox)
    scale = min((cw - 90) / char.width, (ch - 70) / char.height)
    nw, nh = int(char.width * scale), int(char.height * scale)
    char_r = char.resize((nw, nh), Image.LANCZOS)
    x = (cw - nw) // 2
    y = ch - nh - 12
    sil = Image.new("RGBA", (nw, nh), (60, 30, 10, 0))
    sil.putalpha(char_r.getchannel("A").point(lambda a: int(a * 0.45)))
    sil = sil.filter(ImageFilter.GaussianBlur(16))
    img.alpha_composite(sil, (x, y + 16))
    img.alpha_composite(char_r, (x, y))
    return img


def paste_plate(img, plate, x, y):
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle(
        [x + 12, y + 16, x + plate.width - 12, y + plate.height - 4],
        radius=30, fill=(90, 50, 20, 110))
    base_rgba = img.convert("RGBA")
    base_rgba.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14)))
    base_rgba.alpha_composite(plate, (x, y))
    img.paste(base_rgba.convert("RGB"), (0, 0))


def photo_card(img_src, wdt, label, couleur, label_size=22):
    """Carte photo : plaque crème, cadre fin couleur de série, étiquette."""
    hgt = int(img_src.height * wdt / img_src.width)
    band = 58
    card = Image.new("RGBA", (wdt + 20, hgt + band), (0, 0, 0, 0))
    cd = ImageDraw.Draw(card)
    cd.rounded_rectangle([0, 0, wdt + 19, hgt + band - 1], radius=12, fill=PLAQUE + (255,))
    card.alpha_composite(img_src.resize((wdt, hgt), Image.LANCZOS).convert("RGBA"), (10, 10))
    cd.rounded_rectangle([0, 0, wdt + 19, hgt + band - 1], radius=12,
                         outline=couleur + (255,), width=3)
    cd.text((14, hgt + (band - label_size) // 2 + 6), label, font=fred(label_size), fill=NOIR)
    return card


def paste_card(img, card, x, y):
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle(
        [x + 6, y + 12, x + card.width - 6, y + card.height - 2],
        radius=12, fill=(90, 50, 20, 90))
    base_rgba = img.convert("RGBA")
    base_rgba.alpha_composite(sh.filter(ImageFilter.GaussianBlur(12)))
    base_rgba.alpha_composite(card, (x, y))
    img.paste(base_rgba.convert("RGB"), (0, 0))


def save(img, *parts):
    path = os.path.join(HERE, *parts)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if path.lower().endswith(".png"):
        img.convert("RGB").save(path)
    else:
        img.convert("RGB").save(path, quality=92)
    print("écrit :", path)
    return path


# =====================================================================
# G1 — Planche Instagram 3:4 · 1080 × 1440 (§ 15 ; avenant § D G1)
# =====================================================================

def g1_planche_3_4(serie):
    s = SERIES[serie]
    coul = s["couleur"]
    img = base(coul, s["numero"])
    header(img, coul)
    pill(img, 64, 118, "SÉRIE · %s" % s["nom"], coul)
    d = ImageDraw.Draw(img)
    d.text((64, 216), "Un personnage,", font=fred(97), fill=NOIR)
    d.text((64, 322), "cinq angles", font=fred(97), fill=accent_texte(coul, grand=True))
    check("titre accent G1 (grand)", accent_texte(coul, grand=True), BLANC)
    caption(img, 64, 452,
            "On me voit presque toujours de face. Mais un personnage, ça se construit en volume : voici le tour complet, angle par angle.",
            size=33)
    plate = char_plate(800, 600)
    paste_plate(img, plate, 140, 596)
    d = ImageDraw.Draw(img)
    d.rectangle([140, 1196, 940, 1250], fill=NOIR)
    d.text((540, 1223), "ANGLE 01 — FACE · LA RÉFÉRENCE CANONIQUE",
           font=fred(25), fill=CREME, anchor="mm")
    check("cartouche crème/noir chaud", CREME, NOIR)
    footer(img, coul, 1, 6, spec="FEUILLE DE MODÈLE — VERSION FINALE · APPROUVÉE LE 21 NOVEMBRE 2026")
    return img


# =====================================================================
# G2 — Story / couverture reel 9:16 · 1080 × 1920 (§ 15 nº 01 ; avenant G3+G4)
# Zones : interface haut y 0–230 et bas y 1500–1920 libres ; rail x ≥ 950,
# y 950–1480 libre ; titre y 250–430 ; personnage x 70–930, y 450–1330 ;
# sous-titres y 1350–1470.
# =====================================================================

def g2_story_9_16(serie):
    s = SERIES[serie]
    coul = s["couleur"]
    img = base(coul, None, w=1080, h=1920)
    # pastille + titre DANS la zone titre (y 250–430)
    pill(img, 70, 252, "SÉRIE · %s" % s["nom"], coul, size=26)
    d = ImageDraw.Draw(img)
    d.text((70, 330), "Demain, on me branche", font=fred(64), fill=NOIR)
    # personnage dans sa zone (§ 15) : plaque 860 × 880 en (70, 450)
    plate = char_plate(860, 880)
    paste_plate(img, plate, 70, 450)
    # sous-titre dans sa zone (y 1350–1470) : style § 13.2 (Nunito SemiBold,
    # crème sur noir chaud semi-transparent)
    d = ImageDraw.Draw(img)
    st = "Premier test en direct — je cligne des yeux."
    f = nun(44)
    tw = d.textlength(st, font=f)
    bar = Image.new("RGBA", (int(tw) + 64, 84), NOIR + (191,))
    bd = ImageDraw.Draw(bar)
    bd.rounded_rectangle([0, 0, bar.width, 84], radius=16, fill=NOIR + (191,))
    bd.text((32, 42), st, font=f, fill=CREME, anchor="lm")
    rgba = img.convert("RGBA")
    rgba.alpha_composite(bar, (70, 1366))
    img.paste(rgba.convert("RGB"), (0, 0))
    check("sous-titre crème/noir chaud", CREME, NOIR)
    # signature au-dessus de l'interface basse (y < 1500), hors rail (x < 950)
    d = ImageDraw.Draw(img)
    d.line([70, 1486, 930, 1486], fill=coul, width=2)
    return img


# =====================================================================
# G3 — Miniature YouTube 16:9 · 1280 × 720 (§ 15 nº 02)
# Titre à gauche x 40–790, y 60–470 ; personnage à droite x 820–1240,
# y 50–670 ; coin bas-droit (durée) libre de texte.
# =====================================================================

def g3_miniature(serie):
    s = SERIES[serie]
    coul = s["couleur"]
    img = base(coul, None, w=1280, h=720)
    pill(img, 40, 64, "SÉRIE · %s" % s["nom"], coul, size=25)
    d = ImageDraw.Draw(img)
    y = 170
    for ln in ["Le tracker", "a planté"]:
        d.text((40, y), ln, font=fred(104), fill=NOIR)
        y += 116
    d.text((40, y + 8), "…et je montre tout.", font=fred(44), fill=accent_texte(coul, grand=True))
    # numéro d'épisode géant pâle, bas-gauche (zone info § 15) — jamais sous la pastille
    d.text((36, 692), "%02d" % s["numero"], font=fred(150), fill=teinte(coul), anchor="lb")
    check("miniature accent (grand)", accent_texte(coul, grand=True), BLANC)
    plate = char_plate(420, 620)
    paste_plate(img, plate, 820, 50)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 706, 1280, 720], fill=coul)
    return img


# =====================================================================
# G4 — Publication Instagram 4:5 · 1080 × 1350 (§ 15 nº 03, conservé)
# Marges ≥ 64 ; sujet dans le carré central y 135–1215 ; titre y 300–470 ;
# personnage x 190–890, y 500–1150.
# =====================================================================

def g4_post_4_5(serie):
    s = SERIES[serie]
    coul = s["couleur"]
    img = base(coul, s["numero"], w=1080, h=1350)
    header(img, coul)
    pill(img, 64, 150, "SÉRIE · %s" % s["nom"], coul)
    d = ImageDraw.Draw(img)
    d.text((64, 300), "Aujourd'hui, pose sérieuse.", font=fred(64), fill=NOIR)
    piece = Image.open(os.path.join(
        PROJ, "poses-expressions-v1", "variante-2-serieux-retenue.png")).convert("RGB")
    card = photo_card(piece, 620, "POSE RETENUE — BRAS CROISÉS, BOUCHE DROITE", coul, label_size=20)
    paste_card(img, card, 230, 500)
    d = ImageDraw.Draw(img)
    d.text((64, 1204), "Bras croisés, bouche droite — je répète mon sérieux.",
           font=nun(30), fill=NOIR)
    d.text((64, 1250), "Le sourire revient dès demain. Une couche à la fois.",
           font=nun(27, italic=True), fill=BRUN)
    check("texte G4 noir/blanc", NOIR, BLANC)
    return img


# =====================================================================
# G5 — Bannière YouTube 2560 × 1440 (§ 15 nº 04) + écran live (§ 15 nº 05)
# Bannière : plein cadre = TV (aucun texte) ; zone sûre tous écrans
# 1235 × 338 centrée (x 662–1898, y 551–889) : logotype, titre, personnage.
# =====================================================================

def g5a_banniere(serie):
    s = SERIES[serie]
    coul = s["couleur"]
    img = Image.new("RGB", (2560, 1440), BLANC)
    d = ImageDraw.Draw(img)
    # décor TV : lavis pâle de série + couture — aucun texte hors zone sûre
    d.rectangle([0, 508, 2560, 932], fill=teinte(coul, 0.93))
    for x in range(40, 2560 - 40, 34):
        d.line([x, 36, x + 18, 36], fill=coul, width=4)
        d.line([x, 1404, x + 18, 1404], fill=coul, width=4)
    # zone sûre : plaque blanche bordée série
    d.rounded_rectangle([662, 551, 1898, 889], radius=24, fill=BLANC, outline=coul, width=4)
    d.text((716, 610), "Onyx", font=fred(150), fill=OMBRE)
    check("logotype orange ombre/blanc", OMBRE, BLANC)
    d.text((722, 772), "L'atelier — en coulisses, en direct, en série.",
           font=nun(40), fill=NOIR)
    pill(img, 722, 566, "SÉRIE · %s" % s["nom"], coul, size=24)
    plate = char_plate(300, 322)
    paste_plate(img, plate, 1560, 559)
    return img


def g5b_ecran_live(serie):
    s = SERIES[serie]
    coul = s["couleur"]
    img = Image.new("RGB", (1920, 1080), BLANC)
    d = ImageDraw.Draw(img)
    for x in range(36, 1920 - 36, 30):
        d.line([x, 30, x + 16, 30], fill=coul, width=3)
    pill(img, 48, 56, "01 — ATTENTE", coul, size=30)
    d = ImageDraw.Draw(img)
    d.text((1872, 74), "atelier — Montréal", font=fred(34), fill=NOIR, anchor="ra")
    # zone personnage centrale (§ 15 : x 480–1440, y 200–880)
    plate = char_plate(960, 680)
    paste_plate(img, plate, 480, 200)
    # information basse y 890–960
    d = ImageDraw.Draw(img)
    info = "On commence dans un instant — merci d'être là."
    f = nun(36)
    d.text(((1920 - d.textlength(info, font=f)) / 2, 906), info, font=f, fill=BRUN)
    # bandeau nom : 104 px en bas
    d.rectangle([0, 976, 1920, 1080], fill=coul)
    d.text((48, 1028), "ONYX — L'ATELIER", font=fred(40),
           fill=texte_sur(coul), anchor="lm")
    d.text((1872, 1028), "SÉRIE · %s" % s["nom"], font=fred(30),
           fill=texte_sur(coul), anchor="rm")
    check("bandeau live texte/couleur", texte_sur(coul), coul)
    check("info basse brun/blanc", BRUN, BLANC)
    return img


# =====================================================================
# GA — Couvertures de highlights, une par série · 1080 × 1080 (avenant G2)
# Fond blanc, double anneau + numéro en couleur de série, nom en noir chaud
# (sur jaune et corail, le texte porté est noir chaud — § 3.1).
# =====================================================================

def ga_highlight(serie):
    s = SERIES[serie]
    coul = s["couleur"]
    cov = Image.new("RGB", (1080, 1080), BLANC)
    d = ImageDraw.Draw(cov)
    d.ellipse([235, 235, 845, 845], outline=coul, width=14)
    d.ellipse([278, 278, 802, 802], outline=coul, width=3)
    t = "%02d" % s["numero"]
    f01 = fred(200)
    d.text(((1080 - d.textlength(t, font=f01)) / 2, 392), t, font=f01,
           fill=accent_texte(coul, grand=True))
    check("highlight numéro (grand)", accent_texte(coul, grand=True), BLANC)
    t2 = s["court"]
    fdeb = fred(52)
    d.text(((1080 - d.textlength(t2, font=fdeb)) / 2, 636), t2, font=fdeb, fill=NOIR)
    return cov


# =====================================================================
# GB — Simulation de grille (avenant § D G5) : contrôle du rythme
# « sommaire » avant publication. Construite depuis les témoins fournis.
# =====================================================================

def gb_grille(temoins):
    """temoins : liste de (chemin, numéro, libellé série, couleur, texte porté)."""
    def cover_cell(path, s):
        im = Image.open(path).convert("RGB")
        sc = max(s / im.width, s / im.height)
        im = im.resize((int(im.width * sc) + 1, int(im.height * sc) + 1), Image.LANCZOS)
        x = (im.width - s) // 2
        y = (im.height - s) // 2
        return im.crop((x, y, x + s, y + s))

    CELL_W, CELL_H, GAP, INSET, BAND = 352, 404, 6, 12, 46
    GW, GH = CELL_W * 3 + GAP * 4, CELL_H * 2 + GAP * 3
    g = Image.new("RGB", (GW, GH), BLANC)
    for i, (path, num, label, coul) in enumerate(temoins[:6]):
        r, c = divmod(i, 3)
        x0 = GAP + c * (CELL_W + GAP)
        y0 = GAP + r * (CELL_H + GAP)
        cov = cover_cell(path, CELL_W - 2 * INSET)
        g.paste(cov, (x0 + INSET, y0 + INSET))
        d = ImageDraw.Draw(g)
        d.rectangle([x0 + INSET - 3, y0 + INSET - 3,
                     x0 + CELL_W - INSET + 2, y0 + INSET + (CELL_W - 2 * INSET) + 2],
                    outline=coul, width=3)
        by = y0 + CELL_H - BAND - 8
        d.rectangle([x0 + INSET, by, x0 + CELL_W - INSET, by + BAND], fill=coul)
        d.text((x0 + INSET + 14, by + BAND // 2), "Nº %s · %s" % (num, label),
               font=fred(24), fill=texte_sur(coul), anchor="lm")
        check("grille bande %s" % label, texte_sur(coul), coul)
    return g


def planche_contact(pieces):
    """pieces : liste de (chemin, libellé)."""
    cols = 3
    thumb_w = 420
    label_h = 38
    pad = 18
    thumbs = []
    for path, lab in pieces:
        t = Image.open(path).convert("RGB")
        th = int(t.height * thumb_w / t.width)
        thumbs.append((t.resize((thumb_w, th), Image.LANCZOS), lab, th))
    rows = (len(thumbs) + cols - 1) // cols
    row_h = []
    for r in range(rows):
        row_h.append(max(th for _, _, th in thumbs[r * cols:(r + 1) * cols]) + label_h + pad)
    sheet = Image.new("RGB", (cols * (thumb_w + pad) + pad, 76 + pad + sum(row_h)), BLANC)
    d = ImageDraw.Draw(sheet)
    d.text((pad, 20), "GABARITS G1–G5 PARAMÉTRÉS « SÉRIE » — PLANCHE-CONTACT DES TÉMOINS (charte v1.0, D3-blanc)",
           font=fred(25), fill=NOIR)
    y_off = 76 + pad
    for r in range(rows):
        for c in range(cols):
            i = r * cols + c
            if i >= len(thumbs):
                break
            t, lab, th = thumbs[i]
            x = pad + c * (thumb_w + pad)
            sheet.paste(t, (x, y_off))
            d.rectangle([x, y_off, x + thumb_w - 1, y_off + th - 1], outline=BRUN, width=1)
            d.text((x + 4, y_off + th + 8), lab, font=fred(21), fill=BRUN)
        y_off += row_h[r]
    return sheet


# =====================================================================

# Série témoin par gabarit (une série différente par gabarit : la planche
# démontre le paramètre sur les 5 couleurs).
TEMOINS_DEFAUT = {
    "G1": "modele", "G2": "fabrication", "G3": "rates",
    "G4": "poses", "G5a": "coulisses", "G5b": "modele",
}
CONSTRUCTEURS = {
    "G1": g1_planche_3_4, "G2": g2_story_9_16, "G3": g3_miniature,
    "G4": g4_post_4_5, "G5a": g5a_banniere, "G5b": g5b_ecran_live,
}
NOMS_TEMOINS = {
    "G1": "temoin-g1-planche-3-4", "G2": "temoin-g2-story-reel-9-16",
    "G3": "temoin-g3-miniature-youtube", "G4": "temoin-g4-post-4-5",
    "G5a": "temoin-g5a-banniere-youtube", "G5b": "temoin-g5b-ecran-live",
}
LIBELLES = {
    "G1": "G1 · 3:4", "G2": "G2 · 9:16",
    "G3": "G3 · Miniature", "G4": "G4 · 4:5",
    "G5a": "G5a · Bannière", "G5b": "G5b · Live",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--serie", choices=list(SERIES), default=None,
                    help="impose cette série à tous les témoins")
    ap.add_argument("--gabarit", choices=list(CONSTRUCTEURS), default=None)
    args = ap.parse_args()

    sorties = {}
    cibles = [args.gabarit] if args.gabarit else list(CONSTRUCTEURS)
    for g in cibles:
        serie = args.serie or TEMOINS_DEFAUT[g]
        img = CONSTRUCTEURS[g](serie)
        sorties[g] = save(img, "temoins", "%s-%s.jpg" % (NOMS_TEMOINS[g], serie))

    if not args.gabarit:
        # GA — une couverture de highlight par série
        hl = {}
        for key in SERIES:
            hl[key] = save(ga_highlight(key), "highlights",
                           "couverture-highlight-%s.png" % key)
        # GB — simulation de grille depuis les témoins
        # La grille simulée est celle du profil Instagram : formats du fil
        # (planches, story, couvertures) — pas les formats paysage YouTube.
        cellules = [
            (sorties["G1"], "01", "MODÈLE", SERIES["modele"]["couleur"]),
            (sorties["G4"], "04", "POSES", SERIES["poses"]["couleur"]),
            (sorties["G2"], "02", "FABRICATION", SERIES["fabrication"]["couleur"]),
            (hl["rates"], "03", "RATÉS", SERIES["rates"]["couleur"]),
            (hl["coulisses"], "05", "COULISSES", SERIES["coulisses"]["couleur"]),
            (hl["modele"], "01", "MODÈLE", SERIES["modele"]["couleur"]),
        ]
        save(gb_grille(cellules), "simulation-grille.png")
        # Planche-contact des témoins (G1–G5 ; G5 = bannière + écran live)
        pieces = [(sorties[g], "%s — %s" % (LIBELLES[g], SERIES[args.serie or TEMOINS_DEFAUT[g]]["nom"]))
                  for g in ["G1", "G2", "G3", "G4", "G5a", "G5b"]]
        save(planche_contact(pieces), "planche-contact-temoins.png")

    # ---- récapitulatif des contrastes ----
    lignes = ["=== CONTRASTES WCAG 2.2 (calculés) ==="]
    seen = set()
    echecs = 0
    for label, fg, bg, r in CHECKS:
        key = (label, fg, bg)
        if key in seen:
            continue
        seen.add(key)
        if r >= 4.5:
            verdict = "OK petit texte"
        elif r >= 3.0:
            verdict = "OK grand texte seulement"
        else:
            verdict = "ÉCHEC"
            echecs += 1
        lignes.append("%-44s %s sur %s : %5.2f:1 — %s" % (label, hexs(fg), hexs(bg), r, verdict))
    lignes.append("Échecs : %d" % echecs)
    rapport = "\n".join(lignes)
    print("\n" + rapport)
    with open(os.path.join(HERE, "contrastes-temoins.txt"), "w", encoding="utf-8") as fh:
        fh.write(rapport + "\n")
    assert echecs == 0, "au moins un contraste en échec — voir le rapport"


if __name__ == "__main__":
    main()
