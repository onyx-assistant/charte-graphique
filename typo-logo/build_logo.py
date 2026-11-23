#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Logotype Onyx — v1 (22 novembre 2026)
Police d'affichage : Fredoka SemiBold (600), police de texte : Nunito.
Reproductible : python3 build_logo.py
Aucune modification du personnage : l'icône est un recadrage tel quel
de references/onyx-canonique.webp (tête mesurée par analyse du masque).
"""
from PIL import Image, ImageDraw, ImageFont
import os

BASE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(BASE, "fonts")
OUT = os.path.join(BASE, "logo")
REF = os.path.join(BASE, "..", "references", "onyx-canonique.webp")

# Palette de la charte (CHARTE-GRAPHIQUE.md, § 3)
ORANGE_LUMIERE = (252, 139, 50)    # #FC8B32
ORANGE_MEDIAN = (201, 93, 29)      # #C95D1D
FOND_SOMBRE = (22, 17, 16)         # #161110
BLANC = (255, 255, 255)            # #FFFFFF
NOIR_CHAUD = (26, 21, 18)          # ~#1A1512
MOT = "Onyx"


def fredoka(size, wght=600):
    f = ImageFont.truetype(os.path.join(FONTS, "Fredoka.ttf"), size)
    f.set_variation_by_axes([wght, 100])
    return f


def wordmark(couleur, size=480):
    """Le mot « Onyx » seul, rogné au plus juste, fond transparent."""
    f = fredoka(size)
    tmp = Image.new("RGBA", (size * 4, size * 2), (0, 0, 0, 0))
    d = ImageDraw.Draw(tmp)
    d.text((size // 2, size // 4), MOT, font=f, fill=couleur + (255,))
    return tmp.crop(tmp.getbbox())


def sur_fond(img, fond, marge_ratio=0.35):
    m = int(img.height * marge_ratio)
    canvas = Image.new("RGBA", (img.width + 2 * m, img.height + 2 * m), fond + (255,))
    canvas.alpha_composite(img, (m, m))
    return canvas


def icone_tete(taille=1000):
    """Recadrage carré de la tête, référence telle quelle (aucun retouche)."""
    ref = Image.open(REF).convert("RGB")
    # Boîte mesurée par analyse du masque : tête x 333–1270, y 257–1179 (sur 1600)
    tete = ref.crop((301, 218, 1301, 1218))
    return tete.resize((taille, taille), Image.LANCZOS)


def lockup(couleur_texte, fond=None):
    """Icône + texte, alignés au centre verticalement."""
    wm = wordmark(couleur_texte)
    h_icone = int(wm.height * 1.55)
    icone = icone_tete(h_icone)
    ecart = int(wm.height * 0.28)
    W = icone.width + ecart + wm.width
    H = max(icone.height, wm.height)
    if fond is None:
        canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    else:
        canvas = Image.new("RGBA", (W, H), fond + (255,))
    canvas.paste(icone, (0, (H - icone.height) // 2))
    canvas.alpha_composite(wm, (icone.width + ecart, (H - wm.height) // 2))
    return canvas


def main():
    os.makedirs(OUT, exist_ok=True)

    # 1. Icône tête (référence telle quelle)
    icone_tete(1000).save(os.path.join(OUT, "icone-tete-onyx-1000.png"))
    icone_tete(512).save(os.path.join(OUT, "icone-tete-onyx-512.png"))

    # 2. Variantes du logotype
    sur_fond(wordmark(ORANGE_LUMIERE), FOND_SOMBRE).save(
        os.path.join(OUT, "logo-onyx-sombre.png"))
    sur_fond(wordmark(ORANGE_MEDIAN), BLANC).save(
        os.path.join(OUT, "logo-onyx-clair.png"))
    wordmark(NOIR_CHAUD).save(os.path.join(OUT, "logo-onyx-monochrome-noir.png"))
    wordmark(BLANC).save(os.path.join(OUT, "logo-onyx-monochrome-blanc.png"))

    # 3. Verrouillages icône + texte
    sur_fond(lockup(ORANGE_LUMIERE), FOND_SOMBRE, 0.22).save(
        os.path.join(OUT, "logo-onyx-icone-texte-sombre.png"))
    sur_fond(lockup(ORANGE_MEDIAN), BLANC, 0.22).save(
        os.path.join(OUT, "logo-onyx-icone-texte-clair.png"))

    for nom in sorted(os.listdir(OUT)):
        p = os.path.join(OUT, nom)
        print(nom, Image.open(p).size, f"{os.path.getsize(p)//1024} Ko")


if __name__ == "__main__":
    main()
