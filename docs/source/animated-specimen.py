# Render this specimen with DrawBot3: http://www.drawbot.com/

# Import modules:
import math
import os
import glob

# Basic variables  (width, height, ):
W, H, M, F = 1024, 1024, 32, 32

# Load font and print font info:
# os.chdir('..')
# print(os.getcwd())
# os.chdir('..')
# print(os.getcwd())
# os.chdir('fonts')
# print(os.getcwd())
# for ttf in glob.glob("*.ttf"):
#     fontfile = os.getcwd()+"/"+ttf
#     print(fontfile)

# font("ttf")
# for axis, data in listFontVariations().items():
#      print((axis, data))  # Get axis info from font

def easeInOutQuad(n):
    if n < 0.5:
        return 2 * n**2
    else:
        n = n * 2 - 1
        return -0.5 * (n*(n-2) - 1)
        
def easeInQuad(n):
    return n**2

def easeOutQuad(n):
    return -n * (n-2)

# Draw a grid from a given increment:
def grid(inc):
    stroke(0.6, 0, 0)  # Set grid line color
    stpX, stpY = 0, 0  # Step in sequence on x axis
    incX, incY = inc, inc  # Grid increment
    for x in range(int(((W-(M*2))/inc)+1)):
        polygon((M+stpX, M), (M+stpX, H-M))
        stpX += incX  # Set position for next gridline
    for y in range(int(((H-(M*2))/inc)+1)):
        polygon((M, M+stpY), (H-M, M+stpY))
        stpY += incY  # Set position for next gridline

# Page loop
varWght = 400
stepUp = 0
stepDown = 0
for frame in range(65):
    print("frame=", frame)
    newPage(W, H)
    fill(1)           # Background color
    rect(0, 0, W, H)  # Draw the background

    # Draw the grid
    # grid(32)


    # if frame in range(0,7):
    #     varWght = 400
    # if frame in range(8, 31):
    #     stepUp += (24/100)/100
    #     varWght = 400
    #     print("step up=", stepUp)                                                                      
    #     newPos = easeInQuad(stepUp)
    #     varWght += newPos * 500
        
    # if frame in range(32,39):
    #     varWght = 900
    # if frame in range(40, 64):
    #     varWght = 900
    #     pos = (frame/24.0)
    #     print("pos=", pos)                                                                      
    #     newPos = easeInQuad(pos)
    #     varWght += newPos * 500

    #Calculate the weight
    # if frame < 50:
    #     pos = (frame/100.0)*2                                                                      
    #     newPos = easeInQuad(pos)
    #     varWght += newPos * 500
    #     if varWght < 400:
    #         varWght = 400
    # if frame > 50:
    #     pos = (frame/100.0)*2                                                                    
    #     newPos = easeOutQuad(pos)
    #     varWght += newPos * 500
    #     if varWght > 900:
    #         varWght = 900
    
    # Calculate the weight
    if frame <= 35:
        pass
        if frame > 5:
            stepUp = stepUp + 20
            varWght = 400 + stepUp
    if frame > 40:
        stepDown = stepDown + 20
        varWght = 900 - stepDown
    if varWght >= 900:
        varWght = 900
    if varWght <= 400:
        varWght = 400
    
    fontVariations(wght=varWght)
    print("varWght=", varWght)
    font("fonts/Dosis-vf.ttf")
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
    # txtTest = "Weight:" % (str(int(varWght))
    text("Weight:", (M-4), (1024-M)-(10*96))
    text(str(int(varWght)), ((M+270)+varWght/16), (1024-M)-(10*96))

# Save GIF
saveImage("animated-specimen.gif")
