import unicodedata
#from Npp import *

text='Atlético Madrid'
text2="Viktoria Plzeň"

rText = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')
rText2 = unicodedata.normalize('NFKD', text2).encode('ascii', 'ignore')

print("Before>>>  " + text+"    After>>>  " + str(rText))
print("Before>>>  " + text2+"    After>>>  " + str(rText2))
