# Render this specimen with DrawBot3: http://www.drawbot.com/
# Run from the root directory of the repo: 
from drawBot import *
import math
import os


W, H, M, F = 1024, 1024, 32, 32


font("fonts/Dosis-VF.ttf")
for axis, data in listFontVariations().items():
    print((axis, data))


def grid(inc):
    stroke(0.6, 0, 0)
    stpX, stpY = 0, 0
    incX, incY = inc, inc
    for x in range(int(((W-(M*2))/inc)+1)):
        polygon((M+stpX, M), (M+stpX, H-M))
        stpX += incX
    for y in range(int(((H-(M*2))/inc)+1)):
        polygon((M, M+stpY), (H-M, M+stpY))
        stpY += incY


# Page loop
varWght = 400.0
stepUp = 0
stepDown = 0
for frame in range(65):
    print("frame=", frame)
    newPage(W, H)
    fill(1)
    rect(0, 0, W, H)

    # Draw the grid
    # grid(32)

    # Calculate the weight
    if frame <= 35:
        pass
        if frame > 5:
            stepUp = stepUp + 20
            varWght = 400.0 + stepUp
    if frame > 40:
        stepDown = stepDown + 20
        varWght = 900.0 - stepDown
    if varWght >= 900:
        varWght = 900
    if varWght <= 400:
        varWght = 400

    fontVariations(wght=varWght)
    print("varWght=", varWght)
    font("fonts/Dosis-VF.ttf")
    fill(0)
    stroke(None)
    fontSize(96)

    # Draw specimen
    text("ABCDEFGHIJKLMNOPQR", (M-4, (1024-M)-(2*96)))
    text("STUVWXYZ abcdefghijk", (M-4, (1024-M)-(3*96)))
    text("lmnopqrstuvwxyz &!?:;.,", (M-4, (1024-M)-(4*96)))
    text("123456789 $€¥£¢ ½ ⅔ ", (M-4, (1024-M)-(5*96)))
    text("[]{}()#* ff ft fft ffi ffl ", (M-4, (1024-M)-(6*96)))
    text("ÆÇÐŁÓÔÒÖÕŒØẞÞ ", (M-4, (1024-M)-(7*96)))
    text("áâàäãåæçðéêèëıíîìïł ", (M-4, (1024-M)-(8*96)))
    text("ñóôòöõøœþßšúùûüÿýž ", (M-4, (1024-M)-(9*96)))
    fill(1, 0, 0)

    # Draw font name
    text("Variable Font: Dosis-VF", (M-6, ((1024-M)-(1*96))))

    # Draw secondary text
    fontSize(94)
    text("Weight:", (M-4), (1024-M)-(10*96))
    text(str(int(varWght)), ((M+270)+varWght/16), (1024-M)-(10*96))

# SAVE GIF
os.chdir("docs")
os.chdir("images")
saveImage("basic-specimen.gif")
os.chdir("..")
os.chdir("..")
