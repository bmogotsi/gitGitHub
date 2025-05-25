# Using Beautiful Soup, print out a list of all the links on the page by looking for HTML tags with the name "a" 
# and retrieving the value taken on by the href attribute of each tag.
# from url http://olympus.realpython.org/profiles

from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys

try:
    url = 'https://psl.co.za/tournament/betway-premiership'
    # https://psl.co.za/club/Richards_Bay?league=betway-premiership
    
    page = urlopen(url) # http object
    html_bytes = page.read().decode("utf-8") # bytes
    soup = BeautifulSoup(html_bytes, "html.parser") # BS4 object
    
    # Create empty text file
    save_psl="Psl_Links3.txt"
    file=open(save_psl, mode="w",encoding="utf-8")
    file.close
    
    # append text file
    save_psl="Psl_Links3.txt"
    file=open(save_psl, mode="a",encoding="utf-8")
    
    tag_a =soup.find_all('a') # get all tags named "a"
    file.write(f"{tag_a}")
    
    file.write(f"\n\n\n start of LINKS_HREF \n\n")
    if 1> 2:
        baseurl='https://psl.co.za'
        for links in tag_a:
            if 'href' in links.attrs:
                #href = links['href']
                #if str(links['href']).startswith("/"):
                    href = links['href'] #get the text value of "href" attribute
                    file.write(f"{baseurl}{href}\n") # must be a string (html)
                    #print(f"{baseurl}{href}")
        
    file.close
    
    sys.exit
except Exception as e:
    print(f"Something went wrong.....:     {str(e)}")