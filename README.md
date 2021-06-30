## Dosis Font
by Edgar Tolentino, Pablo Impallari, Igino Marini

## Current Status
- Dosis-VF is a remastered variable font version. 
- Version 1.007 is the latest stable version.
- Version 2.xxx is an ongoing migration to Glyphs and Vietnamese extension, but is still a work in progress.

## Description
Dosis is a very simple, rounded, sans serif family.
The lighter weights are minimalist. The bolder weights have more personality. The medium weight is nice and balanced.
The overall result is a family that's clean and modern, and can express a wide range of voices & feelings.
It's also full of alternate glyphs so you can play arround and have fun.

It comes in 7 weights: ExtraLight, Light, Regular, Medium, Semibold, Bold & ExtraBold

## Variable Font
<!-- Updated image from variable mastering fork -->
In 2018 Dosis was remastered as a variable font.
![Dosis-VF](https://github.com/eliheuer/dosis/raw/vf-mastering/docs/images/animated-specimen.gif)

## Building

Fonts are built automatically by GitHub Actions - take a look in the "Actions" tab for the latest build.

If you particularly want to build fonts manually on your own computer, you will need to install the [`yq` utility](https://github.com/mikefarah/yq). On OS X with Homebrew, type `brew install yq`; on Linux, try `snap install yq`; if all else fails, try the instructions on the linked page.

Then:

* `make build` will produce font files.
* `make test` will run [FontBakery](https://github.com/googlefonts/fontbakery)'s quality assurance tests.
* `make proof` will generate HTML proof files.

## License

This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is copied below, and is also available with a FAQ at
http://scripts.sil.org/OFL

## Repository Layout

This font repository structure is inspired by [Unified Font Repository v0.3](https://github.com/unified-font-repository/Unified-Font-Repository), modified for the Google Fonts workflow.

