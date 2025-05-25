# Exception-Handling
# https://scrapingant.com/blog/python-exception-handling
#
# #@@@ 403 Forbidden: 
#    This error often occurs when a website detects and blocks scraping attempts. 
#    To mitigate this, consider implementing request headers that mimic a real browser (https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/403):
# #@@@ 429 Too Many Requests:
#    This indicates that you've exceeded the rate limit set by the server. 
#    Implementing rate limiting in your scraper is essential to avoid this error (https://datatracker.ietf.org/doc/html/rfc6585#section-4):
# #@@@ 404 Not Found:
#    This error occurs when the requested resource doesn't exist. 
#    It's important to handle this gracefully to prevent your scraper from crashing:
# #@@@ ConnectionError: 
#    This occurs when there's a problem establishing a connection to the server. 
#    Implementing a retry mechanism can help overcome temporary network issues:
# #@@@ Timeouts
#    Most requests to external servers should have a timeout attached, 
#    in case the server is not responding in a timely manner. By default, 
#    requests do not time out unless a timeout value is set explicitly. Without a timeout, your code may hang for minutes or more.
# #@@@ SSLError: 
#    This occurs when there's an issue with the SSL certificate. 
#    While it's generally not recommended to bypass SSL verification, in some cases it might be necessary:

# #@@@ Logging

import requests
from bs4 import BeautifulSoup
import time

from requests.adapters import HTTPAdapter
# from requests.packages.urllib3.util.retry import Retry
from urllib3.util import Retry
# from requests import Session
import urllib3  

import logging
from datetime import datetime, timedelta, date

import sys

try:


    def rate_limited_request(url, delay=1):
        time.sleep(delay)
 
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)        # SSLError: 
        # response = requests.get(url, verify=False) # SSLError: 
        return requests.get(url, headers=headers, timeout=(3.05, 27), verify=False)
        
    def createToTextFile(inFile, inAttr):
        # Create empty text file
        file=open(inFile, mode=inAttr,encoding="utf-8")
        file.close
        
    def writeToTextFile(inFile, inText):   
        # append text file
        file=open(inFile, mode="a",encoding="utf-8")
        file.write(f"{inText}\n")   
        
    def generate_dynamic_selector(soup, target_text):
        elements = soup.find_all(string=lambda text: target_text in text)
        for element in elements:
            ancestors = element.find_parents()
            for ancestor in ancestors:
                if ancestor.get('id'):
                    return f"#{ancestor['id']} *:contains('{target_text}')"
        return None
        
    #logging Levels
    # logging.debug()  info()   warning()   error()    critical()
    #Here, we use the logging.debug() function when we want to print log information
    # Passing logging.DEBUG to the basicConfig() function’s level keyword argument will show messages from all the logging
    # levels (DEBUG being the lowest level).
    fileTimeStamp =  str(datetime.strftime(datetime.now(), '%Y_%m_%d-%H_%M_%S_%f'))
    logPath    = "C:/Users/ben/OneDrive/Documents/Gaba_Docs/development/Python/Python_Ben/logs/" 
    logFile    = "EPL_Standings_ExceptionHandling_Log_"   + fileTimeStamp + ".txt"
    logging.basicConfig(filename=logPath+logFile,
                        level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    # level=logging.INFO Printed " - ERROR - Request Successful:  https://fbref.com/en/comps/9/Premier-League-Stats "
    # level=logging.DEBUG Printed " - DEBUG - Starting new HTTPS connection (1): fbref.com:443 , - https://fbref.com:443 "GET /en/comps/9/Premier-League-Stats HTTP/1.1" 200 None"
    
    base_url="https://fbref.com"
    url="https://fbref.com/en/comps/9/Premier-League-Stats"
    url = "http://olympus.realpython.org/login"
    
    ## I really don't understand how this handles the "Network Connection Issues"
    ## By default, Requests does not retry failed connections. 
    ## However, it is possible to implement automatic retries with a powerful array of features, including backoff, 
    ## within a Requests Session using the urllib3.util.Retry class:
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
    )
    
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session = requests.Session()
    session.mount("https://", adapter)
    session.mount("https://", adapter)
    
    #@@@ 403 Forbidden: headers
    #@@@ 429 Too Many Requests: delay
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = rate_limited_request(url) #@@@ 429 Too Many Requests: delay # response (returns html bytes)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:  # ConnectionError: 
        if e.response.status_code == 404:       #@@@ 404 Not Found:
            logging.error(f"Resource not found: {url}")
        else:  
            sys.exit()
        raise Exception("response = rate_limited_request(url) went wrong") 
    except requests.exceptions.Timeout:         #Timeouts
        logging.error(f"The request timed out:  {url}")
    except requests.exceptions.SSLError:        #SSLError: verify=False
        logging.error(f"The request, there's an issue with the SSL certificate  {url}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed:  {url}  : {e}")
            
    Html_Text = response.text
    #@@@@ END - 403
    
    soup_0=BeautifulSoup(Html_Text,"lxml")
    if soup_0.contents != []:
        target_text = 'Premier League Table'
        elements_ancestor = generate_dynamic_selector(soup_0, target_text)
        #elements_ancestor = "#results2024-202591_overall *:contains('Premier League Table')"
        new_id=elements_ancestor.rstrip(":contains('Premier League Table')").rstrip(" *")   
        standing_table = soup_0.select(new_id) # returns bytes
        
        
        #standing_table = extract_title(soup)
        if standing_table != []:
            soup=BeautifulSoup(str(standing_table[0]), "lxml") # crete a soup object (documrnt) with smaller data (optimize)
            elements = soup.select('a[href^="/en/squads/"][href*="squads/b"]') # Returns 3 teams
            elementsAll = soup.select('a[href^="/en/squads/"]') # Working - * (substr) anywhere in ATTRIBUTE (href) text  - Returns 20 teams 
            # elements=links
                
            links = [l.get("href") for l in elements] #get all links from tag "a" with "href" attribute 
                
            # links = [base_url+l for l in links if "/squads/" in l] #filter all links "/example/" in text 
            debugYes=False
            if response.status_code == 200 and debugYes==True:
                save_epl="Exception_Handling_.txt"
                createToTextFile(save_epl,'w')
                for link in links:
                    writeToTextFile(save_epl,str(link))
                    #break
                
            if response.status_code == 200:
                print(f"successfully loded HTML Data, status_code = {response.status_code}")
            else:
                print(f"Failed to loded HTML Data, status_code = {response.status_code}")
                
    logging.error(f"Request Successful:  {url}")    
    quit()
except Exception as e:
    logging.error(f"Something went wrong....: Exception is: {str(e)}")
    