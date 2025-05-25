# Scrape EPL Standings 
# https://medium.com/@obalanatosin16/web-scraping-football-matches-epl-with-python-9fe96b0f47c4
# 2025-05-26
# 

from bs4 import BeautifulSoup
import requests
import pandas as pd
from io import StringIO 
standing_url="https://fbref.com/en/comps/9/Premier-League-Stats"


try:
    def createToTextFile(inFile, inAttr):
        # Create empty text file
        file=open(inFile, mode=inAttr,encoding="utf-8")
        file.close
        
    def writeToTextFile(inFile, inText):   
        # append text file
        file=open(inFile, mode="a",encoding="utf-8")
        file.write(f"{inText}\n")   
   
    save_epl="Shooting_EPL_bs4.txt"
    
    data=requests.get(standing_url)
    html_text=data.text
    
    # BeautifulSoup        
    soup=BeautifulSoup(html_text, "html.parser") # initialize soup object
    # select from the web page
    # any tag named " table " with class " stats_table" select the first one " [0] "
    standing_table = soup.select("table.stats_table")[0] # Perform a CSS selection operation on the current element.
    links = standing_table.find_all("a") # find a;; tag "a"
    links = [l.get("href") for l in links] #get all links from tag "a" with "href" attribute 
    sLinks=links
    links = [l for l in links if "/squads/" in l] #filter all links "/squads/" in text 
    links = [f"https://fbref.com{l}" for l in links] # append base_url='https://fbref.com/' 
    if data.status_code == 200:
        createToTextFile(save_epl,'w')
        for link in links:
            writeToTextFile(save_epl,str(link))
            #break
    
    # Extract Match Stats using Pandas and Requests
    # Use team urls
    # get team stats from table called "scores and fixtures"
    # each row represents one match
    
    # get Table "Scores & Fixtures" and turn it into a pandas data frame
    # pandas.read_html reads in all tables but we only looking for a table tags with "scores and fixtures"?
    data=requests.get(str(links[0]))
    #html_text=data.text
    dataIO = StringIO(data.text)
    matches = pd.read_html(dataIO, match="Scores & Fixtures")
    print(matches[0].head(5)) # print first 5 rows
    
    #  find the url of this shooting page from the scores and fixtures page.
    #  data.text

    soup=BeautifulSoup(html_text, "html.parser")
    standing_table = soup.select("table.stats_table")[0] # Perform a CSS selection operation on the current element.
    
    links = standing_table.find_all("a") # find a;; tag "a"
    links = [l.get("href") for l in links] #get all links from tag "a" with "href" attribute 
    links = [l for l in links if "/shooting/" in l] #filter all links "/squads/" in text 
    links = [f"https://fbref.com{l}" for l in links] # append base_url='https://fbref.com/' 
    for link in links:
        writeToTextFile(save_epl,str(link))
    exit()
    
except Exception as e:
    print(f"Something went wrong...:  {str(e)}")