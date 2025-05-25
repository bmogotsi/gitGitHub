# Using Beautiful Soup, print out a list of all the links on the page by looking for HTML tags with the name "a" 
# and retrieving the value taken on by the href attribute of each tag.
# from url http://olympus.realpython.org/profiles

from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys

url = 'http://olympus.realpython.org/profiles'

page = urlopen(url) # http object
html_bytes = page.read().decode("utf-8") # bytes
soup = BeautifulSoup(html_bytes, "html.parser") # BS4 object

tag_a =soup.find_all("a") # get all tags named "a"
baseurl='http://olympus.realpython.org'
for links in tag_a:
    href = links['href'] #get the text value of "href" attribute
    print(f"{baseurl}{href}")
    
sys.exit