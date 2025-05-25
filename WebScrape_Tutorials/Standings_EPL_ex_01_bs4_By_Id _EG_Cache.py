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
try:
    def createToTextFile(inFile, inAttr):
        # Create empty text file
        file=open(inFile, mode=inAttr,encoding="utf-8")
        file.close
        
    def writeToTextFile(inFile, inText):   
        # append text file
        file=open(inFile, mode="a",encoding="utf-8")
        file.write(f"{inText}\n")   
   
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
       
    save_epl="Standings_EPL_bs4_by_id_EG_Cache.txt"
    
    # data=requests.get(standing_url) # download page, returns Bytes (HTML text Unformatted)
    data=requests.get(url)
    html_text=data.text
    
    # BeautifulSoup        
    #soup=BeautifulSoup(html_text, "html.parser") # initialize soup object and parse downloaded bytes
    soup=get_soup(url)
    standing_table = soup.select('table.stats_table')[0]  # Perform a CSS selection operation on the current element.
    links = standing_table.find_all("a") # find a;; tag "a"
    # Efficient
    #elements = soup.select('table.stats_table > a')
    elements=links

    links = [l.get("href") for l in elements] #get all links from tag "a" with "href" attribute 

    links = [base_url+l for l in links if "/squads/" in l] #filter all links "/example/" in text 
 
    if data.status_code == 200:
        createToTextFile(save_epl,'w')
        for link in links:
            writeToTextFile(save_epl,str(link))
            #break
    
    exit()
except Exception as e:
    print(f"Something went wrong...:  {str(e)}")