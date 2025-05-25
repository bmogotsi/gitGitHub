#! python3
# A Shebang indicates which Bash or Python interpreter to use to interpret an executable file. 
# Scheck if String is number

import pathlib, sys, re

sInt = '25'
sFloat = '345.12'
sString = '234 BC 23.45 abC'
sDate = '2024-12-31'

# Python program to check if a string has at least one letter and one number
iString= any(c.isalpha() for c in sString)
iSdigits= all(c.isdigit() for c in sInt)
iSFloat= any(c.isdigit() for c in sFloat)
iSFloatChar= any(c.isdigit() for c in sFloat)



if iSdigits == True: # INT
    sPr=int(sInt)
    print('Valid Int  ' + str(sPr))
else:
    try:
        sPr = float(sInt)
        print("Valid float   " + str(sPr))
    except ValueError:
        sPr = str(sInt)
        print("Valid String   " + str(sPr))

exit

if sInt.isnumeric() == True: # INT
    sPr=int(sInt)
    print('Valid Int' + str(sPr))