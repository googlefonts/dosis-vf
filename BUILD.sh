#!/bin/sh
python3 sources/BUILD.py \
    --static \
    --googlefonts ~/Google/fonts/ofl/dosis \
    --fontbakery \
    --ttfautohint "-v --stem-width-mode=qsq" \
    && mv ~/Google/fonts/ofl/dosis/Dosis-VF.ttf ~/Google/fonts/ofl/dosis/Dosis-Regular.ttf
#    --drawbot \
#    --addfont \
#    --fixnonhinting
