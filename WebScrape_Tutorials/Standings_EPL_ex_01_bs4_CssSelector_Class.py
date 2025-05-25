# Scrape EPL Standings 
# https://www.geeksforgeeks.org/python-beautifulsoup-find-all-class/
# 2025-05-28
# 

from bs4 import BeautifulSoup
import requests
import pandas as pd
from io import StringIO 
import pprint

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
   
    save_epl="Standings_EPL_bs4_Css_Class.txt"
    
    page=requests.get(standing_url) # download page, returns Bytes (HTML text Unformatted)

  
    # Website URL 
    # URL = 'https://www.geeksforgeeks.org/'
  
    # id list set 
    id_list = set() 
  
    # Page content from Website URL 
    # page = requests.get( URL ) 
  
    # parse html content 
    soup = BeautifulSoup( page.content , 'html.parser') 
    if page.status_code == 200:
        createToTextFile(save_epl,'w')
      
        cnt=0
        # get all tags 
        tags = {tag.name for tag in soup.find_all(class_="stats_table")} 
      
        # iterate all tags 
        for tag in tags: 
      
            # find all element of tag 
            for i in soup.find_all( tag ): 
      
                # if tag has attribute of id 
                if i.has_attr( "id" ): 
      
                    if len( i['id'] ) != 0: 
                        id_list.add(" ".join( i['id'])) 
                        cnt+=1
                        writeToTextFile(save_epl,f"{cnt}. "+str(i['id']))
                        
        writeToTextFile(save_epl,"\n\n\n\n\n\n"+str( id_list ))
        # pprint.pprint( id_list ) 
        
    
    exit()
    
except Exception as e:
    print(f"Something went wrong...:  {str(e)}")