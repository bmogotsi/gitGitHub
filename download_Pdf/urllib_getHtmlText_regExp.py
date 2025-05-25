import re
import sys
from urllib.request import urlopen

# Write a program that grabs the full HTML from the following URL:
#       Then use .find() to display the text following Name: and Favorite Color: 
#            (not including any leading spaces or trailing HTML tags that might appear on the same line).

url = "http://olympus.realpython.org/profiles/dionysus"
 
page = urlopen(url)

html_bytes = page.read()

html_data = html_bytes.decode("utf-8")

# print(html_data)

# The below will find tags <h2> and </h2> and everything in between including the tages
name=re.findall('<.*h2>',html_data, re.I)
print(name)
#colourStr=re.sub('Favorite Color:',"",colourStr)
nameStr=re.sub('Name:',"",re.sub(' ' ,"",re.sub('<.*?h2>',"",str(name[0]))))
print(nameStr)

# The below will find tags <h2> and </h2> and everything in between including the tages
colour=re.findall('Favorite Color:.*',html_data, re.I)
colourStr = str(colour[0])
print(colourStr)
#colourStr=re.sub('Favorite Color:',"",colourStr)
colourStr=re.sub(' ' ,"",re.sub('Favorite Color:',"",colourStr))
print(colourStr)

sys.exit