## Fontbakery report

<details>
<summary><b>[14] Dosis-Roman-VF.ttf</b></summary>
<details>
<summary>:fire: <b>FAIL:</b> Checks METADATA.pb font.name field matches family name declared on the name table.</summary>

* [com.google.fonts/check/092](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/092)
* :fire: **FAIL** Unmatched family name in font: TTF has "Dosis ExtraLight" while METADATA.pb has "Dosis" [code: mismatch]

</details>
<details>
<summary>:fire: <b>FAIL:</b> METADATA.pb font.filename and font.post_script_name fields have equivalent values?</summary>

* [com.google.fonts/check/097](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/097)
* :fire: **FAIL** METADATA.pb font filename="Dosis-Roman-VF.ttf" does not match post_script_name="Dosis-ExtraLight".

</details>
<details>
<summary>:fire: <b>FAIL:</b> METADATA.pb: Filename is set canonically?</summary>

* [com.google.fonts/check/105](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/105)
* :fire: **FAIL** METADATA.pb: filename field ("Dosis-Roman-VF.ttf") does not match canonical name "Dosis-ExtraLight.ttf".

</details>
<details>
<summary>:fire: <b>FAIL:</b> METADATA.pb font.name and font.full_name fields match the values declared on the name table?</summary>

* [com.google.fonts/check/108](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/108)
* :fire: **FAIL** METADATA.pb Family name "Dosis") does not match name table entry "Dosis ExtraLight" ! [code: familyname-mismatch]

</details>
<details>
<summary>:fire: <b>FAIL:</b> Checking OS/2 usWeightClass matches weight specified at METADATA.pb.</summary>

* [com.google.fonts/check/112](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/112)
* :fire: **FAIL** OS/2 usWeightClass (400:"Regular") does not match weight specified at METADATA.pb (200:"ExtraLight").

</details>
<details>
<summary>:fire: <b>FAIL:</b> Font enables smart dropout control in "prep" table instructions?</summary>

* [com.google.fonts/check/072](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/072)
* :fire: **FAIL** 'prep' table does not contain TrueType  instructions enabling smart dropout control. To fix, export the font with autohinting enabled, or run ttfautohint on the font, or run the  `gftools fix-nonhinting` script.

</details>
<details>
<summary>:fire: <b>FAIL:</b> There must not be VTT Talk sources in the font.</summary>

* [com.google.fonts/check/vttclean](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/vttclean)
* :fire: **FAIL** Some tables containing VTT Talk (hinting) sources were found in the font and should be removed in order to reduce total filesize: TSI0, TSI1, TSI2, TSI3, TSI5

</details>
<details>
<summary>:fire: <b>FAIL:</b> Checking with Microsoft Font Validator.</summary>

* [com.google.fonts/check/037](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/037)
* :fire: **FAIL** MS-FonVal: The version number is neither 0x00010000 nor 0x0001002 DETAILS: 0x00010003
* :fire: **FAIL** MS-FonVal: The device table StartSize is greater than the end size DETAILS: LookupList, Lookup[0], SubTable[0](PairPos, fmt 1), PairSet[33], PairValueRecord[53], Value1, XAdvDeviceTable
* :fire: **FAIL** MS-FonVal: The VDMX data doesn't match the data calculated by the rasterizer DETAILS: 
	- group[0], entry[0], yPelHeight = 8, yMin,yMax = 0,0, calculated yMin,yMax = -3,9
	- group[0], entry[1], yPelHeight = 9, yMin,yMax = 0,0, calculated yMin,yMax = -3,10
	- group[0], entry[2], yPelHeight = 10, yMin,yMax = 0,0, calculated yMin,yMax = -3,11
	- group[0], entry[3], yPelHeight = 11, yMin,yMax = 0,0, calculated yMin,yMax = -3,12
	- group[0], entry[4], yPelHeight = 12, yMin,yMax = 0,0, calculated yMin,yMax = -3,13
	- group[0], entry[5], yPelHeight = 13, yMin,yMax = 0,0, calculated yMin,yMax = -3,14
	- group[0], entry[6], yPelHeight = 14, yMin,yMax = 0,0, calculated yMin,yMax = -4,14
	- group[0], entry[7], yPelHeight = 15, yMin,yMax = 0,0, calculated yMin,yMax = -4,15
	- group[0], entry[8], yPelHeight = 16, yMin,yMax = 0,0, calculated yMin,yMax = -4,17
	- group[0], entry[9], yPelHeight = 17, yMin,yMax = 0,0, calculated yMin,yMax = -4,18
	- NOTE: 238 other similar results were hidden!
* :warning: **WARN** MS-FonVal: The version number is valid, but less than 5 DETAILS: 4
* :warning: **WARN** MS-FonVal: PANOSE(tm) is undefined. Font mapping may not work properly
* :warning: **WARN** MS-FonVal: There are undefined bits set in fsSelection field DETAILS: Bit(s) 7
* :warning: **WARN** MS-FonVal: The value of sTypoAscender minus sTypoDescender is greater than unitsPerEm DETAILS: sTypoAscender = 1027, sTypoDescender = -237
* :warning: **WARN** MS-FonVal: The table does not contain any Apple subtables
* :warning: **WARN** MS-FonVal: Apple logo mapping test not performed, cmap 1,0 not present
* :warning: **WARN** MS-FonVal: Characters are mapped in the Unicode Private Use area
* :warning: **WARN** MS-FonVal: Not all extremes are marked with the on-curve control points  DETAILS: {'Glyph index': [46, 173, 425, 444]}
* :warning: **WARN** MS-FonVal: Non-linear scaling flag (bit 4) is set, but hdmx table is not present
* :warning: **WARN** MS-FonVal: Non-linear scaling flag (bit 4) is set, but LTSH table is not present
* :warning: **WARN** MS-FonVal: The unitsPerEm value is not a power of two DETAILS: 1000
* :warning: **WARN** MS-FonVal: The modified time is an unlikely value DETAILS: modified = 3624288426 (Monday, November 5, 2018 6:47 PM)
* :warning: **WARN** MS-FonVal: The lowestRecPPEM value may be unreasonably small DETAILS: lowestRecPPEM = 6
* :warning: **WARN** MS-FonVal: Ascender is different than OS/2.usWinAscent. Different line heights on Windows and Apple DETAILS: hhea.Ascender = 1027, OS/2.usWinAscent = 1123
* :warning: **WARN** MS-FonVal: The LineGap value is less than the recommended value DETAILS: LineGap = 0, recommended = 96
* :warning: **WARN** MS-FonVal: The leftSideBearing is greater than the advance width (unlikely value) DETAILS: {'Glyph index': [438, 443, 448, 449]}
* :warning: **WARN** MS-FonVal: Loca references a glyf entry which length is not a multiple of 4 DETAILS: Number of glyphs with the warning = 181

</details>
<details>
<summary>:fire: <b>FAIL:</b> Are there unwanted tables?</summary>

* [com.google.fonts/check/053](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/053)
* :fire: **FAIL** Unwanted tables were found in the font and should be removed: TSI0, TSI1, TSI2, TSI3, TSI5

</details>
<details>
<summary>:warning: <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/018](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/018)
* :warning: **WARN** OS/2 VendorID value 'IMPA' is not a known registered id. You should set it to your own 4 character code, and register that code with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx [code: unknown]

</details>
<details>
<summary>:warning: <b>WARN:</b> Is 'gasp' table set to optimize rendering?</summary>

* [com.google.fonts/check/062](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/062)
* :warning: **WARN** 'gasp' table has a gaspRange of 7 that may be unneccessary.
* :warning: **WARN** 'gasp' table has a gaspRange of 43 that may be unneccessary.

</details>
<details>
<summary>:warning: <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/153](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/153)
* :warning: **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: Uogonek	Contours detected: 2	Expected: 1
Glyph name: uogonek	Contours detected: 2	Expected: 1

</details>
<details>
<summary>:warning: <b>WARN:</b> Combined length of family and style must not exceed 20 characters.</summary>

* [com.google.fonts/check/163](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/163)
* :warning: **WARN** The combined length of family and style exceeds 20 chars in the following 'WINDOWS' entries: FONT_FAMILY_NAME = 'Dosis ExtraLight' / SUBFAMILY_NAME = 'Regular'

</details>
<details>
<summary>:warning: <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/065](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/065)
* :warning: **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + i
	- i + l

   [code: lacks-kern-info]

</details>
<br>
</details>

### Summary

| :broken_heart: ERROR | :fire: FAIL | :warning: WARN | :zzz: SKIP | :information_source: INFO | :bread: PASS |
|:-----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 9 | 5 | 28 | 5 | 88 |
| 0% | 7% | 4% | 21% | 4% | 65% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
