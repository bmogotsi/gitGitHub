# Scrape EPL Standings 
# https://scrapingant.com/blog/beautifulsoup-css-selectors
# 2025-05-28
# Mastering CSS Selectors in BeautifulSoup for Efficient Web Scraping
# 

from bs4 import BeautifulSoup
import requests
import pandas as pd
from io import StringIO 
import os
import hashlib
import pickle

base_url="https://fbref.com"
url="https://fbref.com/en/comps/9/Premier-League-Stats"
title_selectors = [
    '[class^="stats_table"]',
    'a[href^="/en/squads/"][href*="squads/b"]',
    '[id$="overall"][id^="result"]',
    '#results2024-202591_overall'
]
try:
    def createToTextFile(inFile, inAttr):
        # Create empty text file
        file=open(inFile, mode=inAttr,encoding="utf-8")
        file.close
        
    def writeToTextFile(inFile, inText):   
        # append text file
        file=open(inFile, mode="a",encoding="utf-8")
        file.write(f"{inText}\n")   
        
    def extract_title(soup):
        for selector in title_selectors:
            # title = soup.select_one(selector) # get soup object
            title = soup.select(selector) # get a list
            if title:
                return title # return bytes
                # return title.text.strip() # return text
        return None  # If no selector matches
        
    def generate_dynamic_selector(soup, target_text):
        elements = soup.find_all(string=lambda text: target_text in text)
        for element in elements:
            ancestors = element.find_parents()
            for ancestor in ancestors:
                if ancestor.get('id'):
                    return f"#{ancestor['id']} *:contains('{target_text}')"
        return None
    
    def get_soup(url, cache_dir='cache'):
        cache_file = os.path.join(cache_dir, hashlib.md5(url.encode()).hexdigest())
        
        if os.path.exists(cache_file):
            with open(cache_file, 'rb') as f:
                return pickle.load(f)
        
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        
        os.makedirs(cache_dir, exist_ok=True)
        with open(cache_file, 'wb') as f:
            pickle.dump(soup, f)
        
        return soup   
       
    save_epl="Standings_EPL_bs4_by_id_EG_Selector_Dynamic.txt"
    
    # data=requests.get(standing_url) # download page, returns Bytes (HTML text Unformatted)
    data=requests.get(url)
    html_text=data.text
    
    # BeautifulSoup        
    #soup=BeautifulSoup(html_text, "html.parser") # initialize soup object and parse downloaded bytes
    soup=get_soup(url)
    #standing_table = soup.select('table.stats_table')[0]  # Perform a CSS selection operation on the current element.
    #standing_table = soup.select('table.stats_table') # Perform a CSS selection operation on the current element.
    # standing_table = soup.find('table',id="results2024-202591_overall") # Working.
    # standing_table = soup.select('table[class^="stats_table"]') #working - all table elements BUT (AttributeError('ResultSet object has no attribute "find_all".) - returns list
    # standing_table = soup.select('[class^="stats_table"]') #working - all tables BUT (AttributeError('ResultSet object has no attribute "find_all".)  - returns list
    # standing_table = soup.select('[class^="stats_table"][id$="overall"][id^="result"]') # $ (ends with) ^(starts with) - working - returns list Not soup object
    # standing_table = soup.select('[id$="overall"][id^="result"]') # $ (ends with) ^(starts with) - working - returns list Not soup object
    if soup.contents != []: 
        target_text = 'Premier League Table'
        elements_ancestor = generate_dynamic_selector(soup, target_text)
        #elements_ancestor = "#results2024-202591_overall *:contains('Premier League Table')"
        new_id=elements_ancestor.rstrip(":contains('Premier League Table')").rstrip(" *")   
        standing_table = soup.select(new_id) # returns bytes
        
        #standing_table = extract_title(soup)
        if standing_table != []:
            soup2=BeautifulSoup(str(standing_table[0]), "lxml") # crete a soup object (documrnt)
            #soup2=BeautifulSoup(standing_table2,'lxml')
            # standing_table2 = standing_table2.self_and_descendants('table')
            #links = standing_table.find_all("a") # find a;; tag "a" WHEN soup object returned bytes
            #links = standing_table #  WHEN soup object returned LIST
            #links= standing_table.find_all("a")
            # Efficient
            #elements = soup2.select('a[href^="/en/squads/"]') # working - #filter all links "/en/squads/" in HREF link text 
            elements = soup2.select('a[href^="/en/squads/"][href*="squads/b"]') # Working - * (substr) anywhere in ATTRIBUTE (href)  - Returns 3 teams 
            elementsAll = soup2.select('a[href^="/en/squads/"]') # Working - * (substr) anywhere in ATTRIBUTE (href) text  - Returns 20 teams 
            # elements=links
        
            links = [l.get("href") for l in elements] #get all links from tag "a" with "href" attribute 
        
            # links = [base_url+l for l in links if "/squads/" in l] #filter all links "/example/" in text 
         
            if data.status_code == 200:
                createToTextFile(save_epl,'w')
                for link in links:
                    writeToTextFile(save_epl,str(link))
                    #break
    
    exit()
except Exception as e:
    print(f"Something went wrong...:  {str(e)}")