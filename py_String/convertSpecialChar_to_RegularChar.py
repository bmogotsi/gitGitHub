#! python3
# A Shebang indicates which Bash or Python interpreter to use to interpret an executable file.
# convert: Special Characters/Encoded Characters/Super-Scripted Characters to REGULAR characters (ASCII)
# https://stackoverflow.com/questions/1207457/convert-a-unicode-string-to-a-string-in-python-containing-extra-symbols

import unicodedata
#from Npp import *

# Convert Special Characters/Encoded to REGULAR characters (ASCII)
text= 'FenerbahÃ§e' # 'Atlético Madrid'
text2= 'Fenerbahçe'# "Viktoria Plzeň"
text3= 'Fenerbahçe'  #u"aaaàçççñññ"

rText = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')   # b'Atletico Madrid'
rText2 = unicodedata.normalize('NFKD', text2).encode('ascii', 'ignore') # b'Viktoria Plzen'
rText3 = unicodedata.normalize('NFKD', text3).encode('ascii', 'ignore') # b'aaaacccnnn'
rText77 = str(unicodedata.normalize('NFKD', text3).encode('ascii', 'ignore')).strip("b").strip("'") # 'aaaacccnnn'
asciiChar = str(rText3)  # "b'Atletico Madrid'"
asciiChar = str(rText3).strip("b").strip("'") # "Atletico Madrid"

print("Before>>>  " + text+"    After>>>  " + str(rText).strip("b").strip("'"))   # 'Atletico Madrid'
print("Before>>>  " + text2+"    After>>>  " + str(rText2).strip("b").strip("'")) # 'Viktoria Plzen'
print("Before>>>  " + text3+"    After>>>  " + str(rText3).strip("b").strip("'")) # 'aaaacccnnn'

# IGNORE Special Characters/Encoded Remainder is REGULAR characters (ASCII)
print('\n' + 'IGNORE')
text3=u"aaaàçççñññ"

rText4 = text3.encode('ascii', 'ignore') # b'aaa'
print("Before>>>  " + text3+"    After>>>  " + str(rText4).strip("b").strip("'")) # 'aaa'

print('\n' + 'REPLACE')
text3=u"aaaàçççñññ"
# REPLACE Special Characters/Encoded with "?" Remainder is REGULAR characters (ASCII)
rText4 = text3.encode('ascii', 'replace') # b'aaa???????'
print("Before>>>  " + text3+"    After>>>  " + str(rText4).strip("b").strip("'")) # 'aaa???????'

exit