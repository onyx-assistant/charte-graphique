#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Planche spécimen — Typographie et logotype Onyx v1 (22 novembre 2026).
Reproductible : python3 build_specimen.py (après build_logo.py)
"""
from PIL import Image, ImageDraw, ImageFont
import os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)
from build_logo import fredoka, icone_tete, FOND_SOMBRE, ORANGE_LUMIERE, ORANGE_MEDIAN, BLANC

FONTS = os.path.join(BASE, "fonts")
LOGO = os.path.join(BASE, "logo")
OUT = os.path.join(BASE, "specimen")

CREME = (255, 243, 230)        # #FFF3E6
ATTENUE = (210, 187, 166)      # #D2BBA6
SURFACE = (34, 26, 22)         # #221A16
SURFACE2 = (44, 33, 27)        # #2C211B
SCENE_CLAIRE = (255, 248, 241) # #FFF8F1
NOIR_CHAUD = (26, 21, 18)

W, MARGE = 2000, 110
CW = W - 2 * MARGE


def nunito(size, wght=400, italic=False):
    nom = "Nunito-Italic.ttf" if italic else "Nunito.ttf"
    f = ImageFont.truetype(os.path.join(FONTS, nom), size)
    f.set_variation_by_axes([wght])
    return f


def titre_section(d, y, texte):
    d.text((MARGE, y), texte.upper(), font=nunito(44, 800), fill=ORANGE_LUMIERE)
    d.line([(MARGE, y + 78), (W - MARGE, y + 78)], fill=SURFACE2, width=4)
    return y + 120


def paste_fit(canvas, img, x, y, largeur):
    r = largeur / img.width
    img2 = img.resize((largeur, int(img.height * r)), Image.LANCZOS)
    canvas.paste(img2, (x, y))
    return y + img2.height


def fredoka_fit(texte, largeur_max, taille_depart):
    """Réduit la taille Fredoka jusqu'à ce que le texte tienne dans la largeur."""
    taille = taille_depart
    while taille > 20:
        f = fredoka(taille)
        if f.getlength(texte) <= largeur_max:
            return f
        taille -= 4
    return f


def carte_titre_video():
    """Exemple : carte de titre de vidéo, 1280×720."""
    c = Image.new("RGB", (1280, 720), FOND_SOMBRE)
    d = ImageDraw.Draw(c)
    ic = icone_tete(430)
    c.paste(ic, (70, 145))
    d.text((560, 210), "On me découpe", font=fredoka_fit("On me découpe", 660, 118), fill=CREME)
    d.text((560, 345), "en couches !", font=fredoka_fit("en couches !", 660, 118), fill=ORANGE_LUMIERE)
    d.text((560, 510), "Journal de bord — épisode 1",
           font=nunito(44, 600), fill=ATTENUE)
    return c


def miniature_youtube():
    """Exemple : miniature YouTube fictive, 1280×720."""
    c = Image.new("RGB", (1280, 720), SCENE_CLAIRE)
    d = ImageDraw.Draw(c)
    ic = icone_tete(540)
    c.paste(ic, (690, 90))
    d.text((60, 150), "JE DIS", font=fredoka_fit("JE DIS", 590, 150), fill=ORANGE_MEDIAN)
    d.text((60, 320), "COUCOU !", font=fredoka_fit("COUCOU !", 590, 150), fill=ORANGE_MEDIAN)
    d.text((60, 520), "Ma toute première vidéo", font=nunito(52, 800), fill=NOIR_CHAUD)
    return c


def main():
    os.makedirs(OUT, exist_ok=True)
    board = Image.new("RGB", (W, 5200), FOND_SOMBRE)
    d = ImageDraw.Draw(board)
    y = 90

    # En-tête
    d.text((MARGE, y), "Onyx — spécimen typographique", font=fredoka(96), fill=CREME)
    y += 140
    d.text((MARGE, y), "Typographie et logotype · version 1 — 22 novembre 2026 · à raffiner",
           font=nunito(46, 600), fill=ATTENUE)
    y += 130

    # 1. Logotype
    y = titre_section(d, y, "1 · Le logotype — Fredoka SemiBold")
    demi = (CW - 40) // 2
    y2 = paste_fit(board, Image.open(os.path.join(LOGO, "logo-onyx-sombre.png")), MARGE, y, demi)
    paste_fit(board, Image.open(os.path.join(LOGO, "logo-onyx-clair.png")), MARGE + demi + 40, y, demi)
    y = y2 + 36
    y = paste_fit(board, Image.open(os.path.join(LOGO, "logo-onyx-icone-texte-sombre.png")),
                  MARGE + (CW - 1250) // 2, y, 1250)
    y += 30
    d.text((MARGE, y), "Variantes : fond sombre (orange lumière #FC8B32), fond clair (orange médian #C95D1D),",
           font=nunito(38, 400), fill=ATTENUE)
    d.text((MARGE, y + 55), "monochrome noir chaud / blanc sur transparent, et verrouillage icône + texte.",
           font=nunito(38, 400), fill=ATTENUE)
    y += 165

    # 2. Fredoka
    y = titre_section(d, y, "2 · Fredoka — police d'affichage et de logotype")
    for ligne, taille in [
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 96),
        ("abcdefghijklmnopqrstuvwxyz", 96),
        ("0123456789 · ! ? : ; ( ) « » — …", 84),
        ("à â ä ç é è ê ë î ï ô ö ù û ü ÿ æ œ À É È Ç Œ", 84),
    ]:
        d.text((MARGE, y), ligne, font=fredoka(taille), fill=CREME)
        y += int(taille * 1.45)
    y += 30

    # 3. Nunito
    y = titre_section(d, y, "3 · Nunito — police de texte")
    exemples = [
        ("Coucou, c'est Onyx ! Une couche à la fois.", nunito(58, 400)),
        ("Légendes, sous-titres et textes de miniature, en français d'abord.", nunito(58, 600)),
        ("Graisses de 200 à 1000, italique véritable, diacritiques complets.", nunito(58, 800)),
        ("L'italique sert aux citations et aux apartés de l'atelier.", nunito(58, 400, italic=True)),
        ("Petit corps, toujours lisible : Noël à Montréal, crème brûlée, cœur léger, 438 — dès 24 px.", nunito(40, 400)),
    ]
    for texte, f in exemples:
        d.text((MARGE, y), texte, font=f, fill=CREME)
        y += int(f.size * 1.5)
    y += 30

    # 4. Exemples d'usage
    y = titre_section(d, y, "4 · Exemples d'usage")
    y2 = paste_fit(board, carte_titre_video(), MARGE, y, demi)
    paste_fit(board, miniature_youtube(), MARGE + demi + 40, y, demi)
    y = y2 + 36
    # Légende type (carte)
    d.rounded_rectangle([MARGE, y, W - MARGE, y + 215], radius=28, fill=SURFACE)
    d.text((MARGE + 45, y + 35), "onyx  ·  Coucou, c'est Onyx ! Voici l'étape 1 de ma naissance : on me découpe en couches.",
           font=nunito(42, 700), fill=CREME)
    d.text((MARGE + 45, y + 105), "Toujours moi, une couche à la fois.  #Onyx #Peluche #Montréal #Atelier",
           font=nunito(42, 400), fill=ATTENUE)
    y += 215 + 60

    # Pied de page
    d.line([(MARGE, y), (W - MARGE, y)], fill=SURFACE2, width=4)
    d.text((MARGE, y + 30), "Polices : Fredoka et Nunito — SIL Open Font License 1.1 · Palette : charte graphique Onyx (§ 3).",
           font=nunito(36, 400), fill=ATTENUE)
    d.text((MARGE, y + 82), "L'icône est la référence canonique, reprise telle quelle, sans retouche.",
           font=nunito(36, 400), fill=ATTENUE)
    y += 185

    board = board.crop((0, 0, W, y))
    png = os.path.join(OUT, "planche-specimen-v1.png")
    board.save(png)
    board.save(os.path.join(OUT, "planche-specimen-v1.pdf"), resolution=200)
    print("planche:", board.size, f"{os.path.getsize(png)//1024} Ko")


if __name__ == "__main__":
    main()
