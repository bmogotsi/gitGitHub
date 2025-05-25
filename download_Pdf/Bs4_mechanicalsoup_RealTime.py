# https://realpython.com/python-web-scraping-practical-introduction/#interact-with-websites-in-real-time
# Submit a Form With MechanicalSoup
#
# Real Time

import mechanicalsoup
import time
from bs4 import BeautifulSoup
import sys

try:
    # With techniques like this, you can scrape data from websites that periodically update their data. 
    # However, you should be aware that requesting a page multiple times in rapid succession can be seen 
    # as suspicious, or even malicious, use of a website.
    
    browser = mechanicalsoup.Browser()
    
    # 1

    for i in range(4):
        page = browser.get("http://olympus.realpython.org/dice")
        tag = page.soup.select("#result")[0] # uses the CSS ID selector # to indicate that result is an id value.
        result = tag.text 
        
        if page.status_code == 200: 
            for res in tag:
                print(res)
                
            print(f"The result of your dice roll is: {result}")
        
        # Wait 10 seconds if this isn't the last request
        if i < 3:
            time.sleep(10)
    
    exit()
    
    sys.exit
except Exception as e:
    print(f"Something went wrong....:    {str(e)}")