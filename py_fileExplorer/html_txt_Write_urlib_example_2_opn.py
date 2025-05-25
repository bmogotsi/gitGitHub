# https://realpython.com/python-web-scraping-practical-introduction/#interact-with-websites-in-real-time

# Get URL Webpage (urlopen(url)
#      get returned object (urlopen(url))
#         get b ytes from object (page.read())
#             parse bytes to string (html_bytes.decode("utf-8")) 
# print/write to html file

from urllib.request import urlopen
import csv 

# url = "http://olympus.realpython.org/profiles/aphrodite"
url = "http://quotes.toscrape.com"

# return  HTTPResponse object
page = urlopen(url)

# returns a sequence of bytes from HTTPResponse object
html_bytes = page.read()

# decode the bytes to a string using UTF-8
html_data = html_bytes.decode("utf-8")

print(html_data)

# Save the "HTTPResponse object" to a HTML file
    
save_html="urlib_example_2_binary.html"
with open(save_html, mode="wb") as file:# binary mode does not take encoding
  file.write(html_bytes) # must be an object (html_bytes) NOT string (html)
file.close

# Save the HTML String (html_data) to a HTML file 
save_html="urlib_example_2_encodingStr.html"
with open(save_html, mode="w",encoding="utf-8") as file: # string mode does take encoding
  file.write(html_data) # must be a string (html)
file.close

# Save the HTML String (html_data) to a HTML file 
save_html="urlib_example_2_encodingStr.txt"
with open(save_html, mode="w",encoding="utf-8") as file: # string mode does take encoding
  file.write(html_data) # must be a string (html)
file.close

# Save the HTML String (html_data) to a HTML file 
save_html="urlib_example_2_str.html"
Func1 = open(save_html, "w", encoding="utf-8")
Func1.write(html_data)




