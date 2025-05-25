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

for string in ["Name: ", "Favorite Color:"]:
    string_start_idx = html_data.find(string)
    text_start_idx = string_start_idx + len(string)
    
    next_html_tag_offset = html_data[text_start_idx:].find("<")
    text_end_idx = text_start_idx + next_html_tag_offset
    
    raw_text = html_data[text_start_idx : text_end_idx]
    clean_text = raw_text.strip(" \r\n\t")
    print(clean_text)

sys.exit