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
   
    save_epl="Standings_EPL_bs4_Css.txt"
    
    data=requests.get(standing_url) # download page, returns Bytes (HTML text Unformatted)
    html_text=data.text
    # parsering string to HTML
    soup = BeautifulSoup(data.content, "html5lib")
    
    # Get tag names       
    # printing tags with given class name
    if data.status_code == 200:
        createToTextFile(save_epl,'w')
      
        cnt=0
        for i in soup.find_all(class_="stats_table"):
            cnt+=1
            textPrint =f"\ncount...: {cnt}, tag...: {i.name}, attributes...: {i.attrs}" 
            #print(f"count...: {cnt}, tag...: {i.name}, attributes...: {i.attrs}, namespace..:{i.namespace},")
            writeToTextFile(save_epl,str(textPrint))
            # , contents...:{i.contents}
            # , gettext....: {i.getText} **************too much text
            # , children...: {i.findChildren}
    
    exit()
    
except Exception as e:
    print(f"Something went wrong...:  {str(e)}")