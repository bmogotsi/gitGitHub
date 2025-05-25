# Scrape EPL Standings 
# https://medium.com/@obalanatosin16/web-scraping-football-matches-epl-with-python-9fe96b0f47c4
# 2025-05-26
# 

from bs4 import BeautifulSoup
import requests
import pandas as pd
from io import StringIO 
standing_url="https://fbref.com/en/comps/9/Premier-League-Stats"

in_html ="""
<html>

<head>
    <title>Sample Html Page</title>
</head>

<body bgcolor="yellow">
    <div class="content">
        <p>This is a paragraph in a div tag whith a class named content</p>
        <p class="highlight">This is a highlighted paragraph</p>
        <a href="http://www.example.com/page1">Link to page 1</p>
        <a href="/page2">Link to page 2 </a> 
    </div>
</body>

</html>

"""
try:
    def createToTextFile(inFile, inAttr):
        # Create empty text file
        file=open(inFile, mode=inAttr,encoding="utf-8")
        file.close
        
    def writeToTextFile(inFile, inText):   
        # append text file
        file=open(inFile, mode="a",encoding="utf-8")
        file.write(f"{inText}\n")   
   
    save_epl="Standings_EPL_bs4_by_id.txt"
    
    data=requests.get(standing_url) # download page, returns Bytes (HTML text Unformatted)
    html_text=data.text
    
    # BeautifulSoup        
    soup=BeautifulSoup(html_text, "html.parser") # initialize soup object and parse downloaded bytes
    # select from the web page
    # any tag named " table " with class " stats_table" select the first one " [0] "
    #standing_table = soup.self_and_descendants("table.stats_table")[0] # Perform a CSS selection operation on the current element.
    #standing_table = soup.select("table.stats_table")
    #links = standing_table.find_all("a") # find a;; tag "a"
    standing_table = soup.select("table.stats_table")[0] # Perform a CSS selection operation on the current element.
    links = standing_table.find_all("a") # find a;; tag "a"
    #links = standing_table  # find a;; tag "a"
    #id=standing_table[0]
    #idYes=id['id']
    #idGet=str("#"+idYes)
    #standing_table = soup.select(idGet)
    #inks = standing_table.find_all("a") 
    links = [l.get("href") for l in links] #get all links from tag "a" with "href" attribute 
    sLinks=links
    links = [l for l in links if "/squads/" in l] #filter all links "/squads/" in text 
    links = [f"https://fbref.com{l}" for l in links] # append base_url='https://fbref.com/' 
    if data.status_code == 200:
        createToTextFile(save_epl,'w')
        for link in links:
            writeToTextFile(save_epl,str(link))
            #break
    

    
    exit()
    
except Exception as e:
    print(f"Something went wrong...:  {str(e)}")