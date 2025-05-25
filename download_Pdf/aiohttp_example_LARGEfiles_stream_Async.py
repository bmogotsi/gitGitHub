#! python3
# A Shebang indicates which Bash or Python interpreter to use to interpret an executable file. 

# https://realpython.com/python-download-file-from-url/

# python -m pip install requests

import requests
import pprint
import asyncio
import aiohttp

# When you make HTTP requests to web servers, you have two commonly used methods to choose from:

#                    HTTP GET
#                    HTTP POST

#   asynchronous download
#                      
try:
    # The following function performs an asynchronous download using the ClientSession class from the aiohttp package:
    # The function defined above takes a URL as an argument. 
    # It then creates a client session using the async with statement, ensuring that the session is properly closed 
    # and resources are released after the program exits this code block. 
    # With the session context, it makes an HTTP GET request to the specified URL and obtains the response object using the async with statement.
    async def download_file(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if "content-disposition" in response.headers:
                    header = response.headers["content-disposition"]
                    filename = header.split("filename=")[1]
                else:
                    filename = url.split("/")[-1]
                filename = 'aiohttp_async_'+ filename
                with open(filename, mode="wb") as file:
                    while True:
                        chunk = await response.content.read()
                        if not chunk:
                            break
                        file.write(chunk)
                    print(f"Downloaded file {filename}")
    
    template_url = (
         "https://api.worldbank.org/v2/en/indicator/"
         "{resource}?downloadformat=csv"
     )
    urls = [
         # Total population by country
         template_url.format(resource="SP.POP.TOTL"),
    
         # GDP by country
         template_url.format(resource="NY.GDP.MKTP.CD"),
    
         # Population density by country
         template_url.format(resource="EN.POP.DNST"),
     ]
    
    # download
    # Finally, define and run an asynchronous main() function that will download files concurrently from those URLs:  
    async def main():
        tasks = [download_file(url) for url in urls]
        await asyncio.gather(*tasks)

    asyncio.run(main())

    exit
except Exception as e:
    print("exception....     " + str(e))