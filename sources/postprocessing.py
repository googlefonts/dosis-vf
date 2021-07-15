#!/usr/bin/env python3
"""Fix the font names for the variable fonts"""
# TODO (M Foley) this shouldn't be required. Send fix to fontmake
from fontTools.ttLib import TTFont
from glob import glob
import os

font_paths = glob("fonts/variable/*.ttf")

for path in font_paths:
    font = TTFont(path)
    font["name"].setName("Dosis", 1, 3, 1, 1033)
    font["name"].setName("IMPA;Dosis-Regular", 3, 3, 1, 1033)
    font["name"].setName("Dosis Regular", 4, 3, 1, 1033)
    font["name"].setName("Dosis-Regular", 6, 3, 1, 1033)

    font.save(path + ".fix")
