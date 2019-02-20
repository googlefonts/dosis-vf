#!/bin/sh
python3 sources/BUILD.py \
    --googlefonts ~/Google/fonts/ofl/dosis \
    --fontbakery \
    --static \
    --ttfautohint "-v -W" \
    --drawbot \
    && mv ~/Google/fonts/ofl/dosis/Dosis-VF.ttf ~/Google/fonts/ofl/dosis/Dosis-Regular.ttf
#    --fixnonhinting
#    --updatemetadata
