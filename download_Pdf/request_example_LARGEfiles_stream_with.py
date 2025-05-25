#! python3
# A Shebang indicates which Bash or Python interpreter to use to interpret an executable file. 

# https://realpython.com/python-download-file-from-url/

# python -m pip install requests

import requests
import pprint
# When you make HTTP requests to web servers, you have two commonly used methods to choose from:

#                    HTTP GET
#                    HTTP POST

#                        
try:
    #  Python’s implicit concatenation by splitting the string literal over multiple lines inside parentheses. 
    # The Python interpreter will automatically join the separate strings on different lines into a single string.
    url = (
         "https://databank.worldbank.org/data/download/WDI_CSV.zip"
    )
    filename = "request_stream_WDI_CSV.zip"
    query_parameters = {"downloadformat": "csv"} # will suffix the file name with "?downloadformat=csv"

    # download only the response headers by setting the stream keyword argument in the requests.get() function.  
    response = requests.get(url,stream=True) 

    # The function returns a tuple of two objects: the path to your output file and an HTTP message object.
    print('\n' + 'url' +response.url+ '\n') 
    print('\n' + 'response.ok True/False...:   ' + str(response.ok) +'\n')
    print('\n' + 'response.status_code 200/400...:   ' +str(response.status_code) +'\n')  
    
    print('\n' + 'response.headers   ...:   ' +'\n')
    pprint.pprint(dict(response.headers))

    # # response.headers   ...:
 
    # # {'Accept-Ranges': 'bytes',
    # # 'Cache-Control': 'public, max-age=3600',
    # # 'Connection': 'keep-alive',
    # # 'Content-Length': '271822139',
    # # 'Content-Type': 'application/octet-stream',
    # # 'Date': 'Tue, 25 Feb 2025 20:10:11 GMT',
    # # 'ETag': '0x8DD3FD234F14A8D',
    # # 'Last-Modified': 'Tue, 28 Jan 2025 19:30:22 GMT',
    # # 'X-Cache': 'TCP_HIT',
    # # 'x-azure-ref': '20250225T201011Z-169d595d7df99ppphC1JNBna3400000011f000000000536d',
    # # 'x-fd-int-roxy-purgeid': '83706104',
    # # 'x-ms-blob-type': 'BlockBlob',
    # # 'x-ms-lease-status': 'unlocked',
    # # 'x-ms-request-id': 'c7796449-301e-0056-3abf-87da80000000',
    # # 'x-ms-version': '2009-09-19'}

    # Saving Downloaded Content to a File



    """         ** Now that you’ve retrieved content from a URL using the requests library, you can save it to your computer locally. 
                ** When saving data to a file in Python, it’s highly recommended to use the with statement. 
                ** It ensures that Python properly manages resources, including files, and automatically closes them when you no longer need them.
    """
    with requests.get(url, stream=True) as response:

        with open(filename, mode="wb") as file: # Because this attribute holds raw bytes, you’ll open a new file in binary mode for writing ('wb')
            for chunk in response.iter_content(chunk_size=10 * 1024): # Then, you iterate through the response data using response.iter_content(), choosing an optional chunk size
                file.write(chunk) # Finally, you write each chunk to the file within the loop’s body.

    # 

    exit
except Exception as e:
    print("exception....     " + str(e))