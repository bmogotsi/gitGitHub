#! python3
# A Shebang indicates which Bash or Python interpreter to use to interpret an executable file. 
# Slice_SubString

import pathlib, sys, os

inputPath = "C:/Users/Ben/OneDrive/Documents/Gaba_Docs/development/Python/Python_Ben/pgmOutput/"
inputFile = "prjHTMParse_Selinium_Chrome_WSB_output2025_01_02-20_07_22291199"   + ".csv"

file_extension = pathlib.Path(inputPath+inputFile).suffix
len1=len(str('prjHTMParse_Selinium_Chrome_WSB_output'))
if inputFile[0:38]=='prjHTMParse_Selinium_Chrome_WSB_output':
    print(str(38))
if inputFile[0:37]=='prjHTMParse_Selinium_Chrome_WSB_output':
    print(str(37))
if inputFile[0:len1]=='prjHTMParse_Selinium_Chrome_WSB_output':
    print(str(len1)+ 'str(len1)')
if inputFile[0:len1-1]=='prjHTMParse_Selinium_Chrome_WSB_output':
    print(str(len1-1) + 'str(len1-1)')