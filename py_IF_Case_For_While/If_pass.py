#! python3
# A Shebang indicates which Bash or Python interpreter to use to interpret an executable file. 
# Slice_SubString

import pathlib, sys, os

# https://www.geeksforgeeks.org/check-a-file-is-opened-or-closed-in-python/

inputPath = "C:/Users/ben/OneDrive/Documents/Gaba_Docs/Whisperer/FBRef/2025 Files/AllDomesticLeagues/"
inputFile = "Fbref_Teams"   + ".xlsx"

# -------------------------------------function to check whether the file is closed
def checkFileClosed(file_obj):
    # check if file is closed using `closed` property
    if file_obj.closed == True:
        pass
        # print('Your file is closed.')
    else:
        pass
        # print('Your file is open.')

    return file_obj.closed

# Opening the "Fbref_Teams" file in read mode
file_obj = open(inputPath+inputFile, 'r')

# check if file is closed
fileClosed = checkFileClosed(file_obj)
print(f"file_obj.closed return >>>>> {fileClosed}")