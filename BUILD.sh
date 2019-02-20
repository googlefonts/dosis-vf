#!/bin/sh
python3 sources/BUILD.py \
    --googlefonts ~/Google/fonts/ofl/dosis \
    --fontbakery \
    --static \
    --ttfautohint "-v --stem-width-mode=nnn" \
    --drawbot \
    --addfont \
    && mv ~/Google/fonts/ofl/dosis/Dosis-VF.ttf ~/Google/fonts/ofl/dosis/Dosis-Regular.ttf
#    --fixnonhinting
