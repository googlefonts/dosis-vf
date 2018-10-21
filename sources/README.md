# Source Notes

### Building just the font

The font file `Dosis/fonts/Dosis-VF.ttf` is built from source using the following command from the root directory:

```
python sources/BUILD.py && gftools fix-dsig fonts/*.ttf --autofix
```

Dependencies installed should include:

 - [fontmake](https://github.com/googlei18n/fontmake)
 - [gftools](https://github.com/googlefonts/gftools)
 - [ttfautohint](https://www.freetype.org/ttfautohint/)

### Building the font and updating the specimen

When building the font, the specimen can also be updated and regenerated. Simply add an extra command to the above build commands line.


Dependencies installed for building the specimen should include the above dependencies, plus `drawbot`:

 - [drawbot](http://drawbot.com)
