import os 
import subprocess
from fontTools.ttLib import TTFont

try:
    print("\n**** Running Fontmake ******************************\n")
    subprocess.call(['fontmake', '-g', 'sources/Dosis.glyphs', '-o', 'variable',])
except:
    print("Error! Try installing Fontmake: https://github.com/googlei18n/fontmake")


print("\n**** Moving fonts to fonts directory *******************\n")
subprocess.call(['cp', 'variable_ttf/Dosis-VF.ttf', 'fonts/',])
print("     [+] Done")


print("\n**** Removing build directories  ***********************\n")
subprocess.call(['rm', '-rf', 'variable_ttf', 'master_ufo'])
print("     [+] Done")


print("\n**** Run: ttfautohint  *********************************\n")
os.chdir('fonts')
cwd = os.getcwd()
print("     In Directory:", cwd)
subprocess.call(['ttfautohint', '-I', 'Dosis-VF.ttf', 'Dosis-VF-Fix.ttf'])
subprocess.call(['cp', 'Dosis-VF-Fix.ttf', 'Dosis-VF.ttf'])
subprocess.call(['rm', '-rf', 'Dosis-VF-Fix.ttf'])
print("     [+] Done")


print("\n**** Run: gftools  **************************************\n")
os.chdir("..")
cwd = os.getcwd()
print("     In Directory:", cwd)
# subprocess.call(['gftools', 'fix-dsgi', 'fonts/Staatliches-Regular.ttf', '--autofix'])


print("\n**** Run: edit xAvgCharWidth  *********************************\n")
cwd = os.getcwd()
print("     In Directory:", cwd)
font = TTFont('fonts/Dosis-VF.ttf')
print(font)
print("     [+] Done")

