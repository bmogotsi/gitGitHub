# Parse HTML using Beautiful Soup
# https://realpython.com/python-web-scraping-practical-introduction/#interact-with-websites-in-real-time
#


from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser") # BS4 object

# print all text from the object
print(soup.get_text())
print(html)

image1, image2 = soup.find_all("img")
    # <img src="/static/dionysus.jpg" />
    # <img src="/static/grapes.png">
    
# access the HTML attributes of the Tag object by putting their names between square brackets,

image1["src"]
    #'/static/dionysus.jpg'

image2["src"]
    #'/static/grapes.png'

# Certain tags in HTML documents can be accessed by properties of the Tag object. 
#
# selecting View page source, then you’ll notice that the <title> tag is written in all caps with spaces:
soup.title
    #<title>Profile: Dionysus</title>
soup.title.string
    #'Profile: Dionysus'
# FIND tag with a specific attribute value
soup.find_all("img", src="/static/dionysus.jpg")
# [<img src="/static/dionysus.jpg"/>]

sys.exit