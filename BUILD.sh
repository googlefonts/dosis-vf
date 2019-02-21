#!/bin/sh
python3 sources/BUILD.py \
    --ttfautohint "-v --stem-width-mode=qsq" \
    --static \
    --googlefonts ~/Google/fonts/ofl/dosis \
    --fontbakery \
    && mv ~/Google/fonts/ofl/dosis/Dosis-VF.ttf ~/Google/fonts/ofl/dosis/Dosis-Regular.ttf
#    --drawbot \
#    --addfont \
#    --fixnonhinting
