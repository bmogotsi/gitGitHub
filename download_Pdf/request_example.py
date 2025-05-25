#! python3
# A Shebang indicates which Bash or Python interpreter to use to interpret an executable file. 

# https://realpython.com/python-download-file-from-url/

# python -m pip install requests

import requests
# When you make HTTP requests to web servers, you have two commonly used methods to choose from:

#                    HTTP GET
#                    HTTP POST

#                        
try:
    #  Python’s implicit concatenation by splitting the string literal over multiple lines inside parentheses. 
    # The Python interpreter will automatically join the separate strings on different lines into a single string.
    url = (
        "https://api.worldbank.org/v2/en/indicator/"
        "NY.GDP.MKTP.CD"
    )
    filename = "request_gdp_by_country.zip"
    query_parameters = {"downloadformat": "csv"}

    # The function returns an HTTP response object with the server’s response to the request. 
    response = requests.get(url, params=query_parameters)

    # The function returns a tuple of two objects: the path to your output file and an HTTP message object.
    print('\n' + 'url' +response.url+ '\n') 
    print('\n' + 'response.ok True/False...:   ' + str(response.ok) +'\n')
    print('\n' + 'response.status_code 200/400...:   ' +str(response.status_code) +'\n')  
    
    # Saving Downloaded Content to a File



    """         ** Now that you’ve retrieved content from a URL using the requests library, you can save it to your computer locally. 
                ** When saving data to a file in Python, it’s highly recommended to use the with statement. 
                ** It ensures that Python properly manages resources, including files, and automatically closes them when you no longer need them.
    """
 
    with open(filename, mode="wb") as file: # Because this attribute holds raw bytes, you’ll open a new file in binary mode for writing ('wb')
        file.write(response.content) # use the .content attribute of the returned response object.

    # 

    exit
except Exception as e:
    print("exception....     " + str(e))