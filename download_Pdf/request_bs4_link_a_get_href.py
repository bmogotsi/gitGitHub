
# Import libraries
import requests
from bs4 import BeautifulSoup

# https://www.geeksforgeeks.org/downloading-pdfs-with-python-using-requests-and-beautifulsoup/

try:
    # URL from which pdfs to be downloaded
    # url = "https://www.geeksforgeeks.org/how-to-extract-pdf-tables-in-python/"
    url = "https://www.samf.ac.za/en/"
    url_domain = "https://www.samf.ac.za"
    
    # Requests URL and get response object
    response = requests.get(url)
    
    # Parse text obtained
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all hyperlinks present on webpage
    links = soup.find_all('a')
    
    i = 0
    
    # From all links check for pdf link and
    # if present download file
    for link in links:
        # if ('.pdf' in link.get('href', [])):
        if ('samo-question-papers' in link.get('href', [])):
            i += 1
            print("Downloading file: ", i)
    
            # Get response object for link
            getLink = url_domain+str(link.get('href'))
            response = requests.get(getLink)
    
            # Write content in pdf file
            if response.status_code == requests.codes.ok: # 200
                pdf = open("pdf"+str(i)+".pdf", 'wb')
                pdf.write(response.content)
                pdf.close()
                print("File ", i, " downloaded")
    
    print("All PDF files downloaded")

    exit

except Exception as e:
    print("exception....     " + str(e))