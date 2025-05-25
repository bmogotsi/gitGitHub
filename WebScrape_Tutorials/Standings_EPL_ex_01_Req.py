# Scrape EPL Standings 
# https://medium.com/@obalanatosin16/web-scraping-football-matches-epl-with-python-9fe96b0f47c4
# 2025-05-26
# 

import requests
standing_url="https://fbref.com/en/comps/9/Premier-League-Stats"

try:
    def createToTextFile(inFile, inAttr):
        # Create empty text file
        file=open(inFile, mode=inAttr,encoding="utf-8")
        file.close
        
    def writeToTextFile(inFile, inText):   
        # append text file
        file=open(inFile, mode="a",encoding="utf-8")
        file.write(f"{inText}")   
   
    save_epl="Standings_EPL.txt"
    
    data=requests.get(standing_url)
    html_text=data.text
    
    if data.status_code == 200:
        createToTextFile(save_epl,'w')
        while True:
            writeToTextFile(save_epl,str(html_text))
            break
    exit()
    
except Exception as e:
    print(f"Something went wrong...:  {str(data.text)}")