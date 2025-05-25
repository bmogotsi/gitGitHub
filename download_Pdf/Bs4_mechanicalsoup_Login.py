# https://realpython.com/python-web-scraping-practical-introduction/#interact-with-websites-in-real-time
# Submit a Form With MechanicalSoup

import mechanicalsoup
import sys

# Browser objects represent the headless web browser. 
# You can use them to request a page from the Internet by passing a URL to their .get() method
browser = mechanicalsoup.Browser()

# 1
url = "http://olympus.realpython.org/login"
login_page = browser.get(url) # HTTP Response Object
login_html = login_page.soup  # html


print(type(login_page.soup))
# <class 'bs4.BeautifulSoup'>

print(login_html.soup)  # html
print(login_html.select("form")[0]) # get form strucure
tag_boby =login_html.find_all("body") 
print(login_html.get_text()) # get text displayed on url
# 2
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

# 3
profiles_page = browser.submit(form, login_page.url)


# did we login successfully?
ab = profiles_page.reason
if profiles_page.status_code == 200:
    print("status_code 200")
    print(profiles_page.url)
if profiles_page.reason == 'OK':
    print("reason okay")
    
    # Now that you have the profiles_page variable set, 
    # it’s time to programmatically obtain the URL for each link on the /profiles page
    links = profiles_page.soup.select("a") # select all the <a> anchor elements on the page:
    baseurl = 'http://olympus.realpython.org'
    for link in links:
        address = link["href"]
        text = link.text
        print(f"{text}: {baseurl}{address}")

sys.exit