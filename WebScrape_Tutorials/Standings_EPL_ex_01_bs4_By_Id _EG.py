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


in_html ="""
<html>

<head>
    <title>Sample Html Page</title>
</head>

<body bgcolor="yellow">
    <div class="content" id="sampleid">
        <p>This is a paragraph in a div tag whith a class named content</p>
        <p class="highlight">This is a highlighted paragraph</p>
        <a href="http://www.example.com/page1">Link to page 1 </a>
        <a href="/page2">Link to page 2 </a> 
        <a href="http://www.example.com/page3" id="page3id">Link to page 3 </a>
        <a href="http://www.example.com/page4" id="page3id">Link to page 4 </a>
        <a href="/product/triangle" id="page3id">Link to product Triangle </a>
        <a href="/product/square" >Link to product Square </a>
        <a href="/product/trapezoid" id="page3id">Link to product Trapezoid </a>
    </div>
</body>

</html>

"""
base_url="http://www.example.com"
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
       
    save_epl="Standings_EPL_bs4_by_id_EG.txt"
    
    # data=requests.get(standing_url) # download page, returns Bytes (HTML text Unformatted)
    html_text=in_html
    
    # BeautifulSoup        
    soup=BeautifulSoup(html_text, "html.parser") # initialize soup object and parse downloaded bytes
    
    # Efficient
    elements = soup.select('div.content > a')

    # Less efficient
    #elements = soup.find_all('div', class_='className')
    #links = [div.find('a') for div in elements]

    links = [l.get("href") for l in elements] #get all links from tag "a" with "href" attribute 

    links = [l for l in links if ".example" in l] #filter all links "/example/" in text 
 
    #if data.status_code == 200:
    if in_html != "":
        createToTextFile(save_epl,'w')
        for link in links:
            writeToTextFile(save_epl,str(link))
            #break
    
    writeToTextFile(save_epl,str("\n\n\n\n\n   \nLeveraging CSS Selector Optimization select \"/product/\"\n\n\n "))
    
    # Leveraging CSS Selector Optimization
    # More efficient
    # BeautifulSoup's select() method is often more efficient than using find_all()
    # CSS selectors are optimized for matching patterns in the document structure, which can lead to faster parsing times.
    elements = soup.select('div.content > a[href^="/product/"]') # More efficient # raw elemnts bytes
    links = [l.get("href") for l in elements]
    # Less efficient
    #  elements = soup.find_all('div', class_='content')
    #  links = [div.find('a', href=lambda x: x and x.startswith('/product/')) for div in elements]
    if elements != []:
        for link in links:
            writeToTextFile(save_epl,base_url+str(link))
            #break
            
    # Scoping and Limiting Parse Area
    # Instead of parsing the entire HTML document, focus on relevant sections:
    soup = BeautifulSoup(html_text, 'lxml')
    relevant_part = soup.find('div',  id="sampleid") # div tag and it's children
    smaller_soup = BeautifulSoup(str(relevant_part), 'lxml')
    # Efficient
    elements = smaller_soup.select("a[ id='page3id']")
    links = [l.get("href") for l in elements]
    #
    writeToTextFile(save_epl,str("\n\n\n\n\n   \nScoping and Limiting Parse Area\n\n\n "))
    if elements != []:
        for link in links:
            writeToTextFile(save_epl,base_url+str(link))
            #break
    
    # Leveraging Unique Identifiers and Attributes
    #   By focusing on these unique identifiers and attributes, 
    #   scrapers can maintain their functionality even when websites undergo design changes, 
    #   reducing the need for frequent updates to the scraping code.
    a=soup.select('#page3id') # select all matching elements/tag
    b=soup.select_one('#page3id') # Select one (first )matching lelement/tag 
    # Selecting elements with specific data attributes
    c=soup.select('[href^="/product/trapezoid"]')
    # Using Scrapy
    # a=response.css('#uniqueId::text').get()
    
    # by class name
    e=soup.select('.highlight')
    
    exit()
except Exception as e:
    print(f"Something went wrong...:  {str(e)}")