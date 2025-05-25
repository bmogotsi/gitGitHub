
import mechanicalsoup
import sys

# Browser objects represent the headless web browser. 
# You can use them to request a page from the Internet by passing a URL to their .get() method

browser = mechanicalsoup.Browser()

url = "http://olympus.realpython.org/login"
page = browser.get(url) # HTTP Response Object

print(type(page.soup))
# <class 'bs4.BeautifulSoup'>

print(page.soup) # html

sys.exit