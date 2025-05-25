
# Python File Explorer (OS Module) py_fileExplorer

## License
**This project is licensed under the terms of the ***MIT license***.**
[MIT](https://choosealicense.com/licenses/mit/)

# urllib (python standard libary)
# use libaries like Requests (Handle HTTP requests) - Third-Party library
# Selenium (Automated browser activity) to navigate through the login.

# https://realpython.com/python-download-file-from-url/
# For quick tasks, you can use the built-in urllib module or the requests library to fetch and save files.
# For large files, streaming data in chunks can help save memory and improve performance.
# You can also perform parallel file downloads 
#           using: ThreadPoolExecutor for multithreading 
#           or the aiohttp library for asynchronous tasks
#           These approaches allow you to handle multiple downloads concurrently, significantly reducing the total download time if you’re handling many files.

# To DownLoad 
                ** urlretrieve() 

                ** or requests.get().
                                file_url = 'https://www.samf.ac.za/content/files/QuestionPapers/j1q82024.pdf'
                                query_parameters = {"downloadformat": "pdf"}   #  especially when you download a CSV file from a URL need to specify the format
                                response= request.get(file_url, params=query_parameters)
# Facilitating File dowload with PYTHON 
                ** Another reason is portability. You may encounter situations where you’re working on cross-platform applications. In such cases, using Python is a good choice ** because it’s a cross-platform programming language. 
                ** This means that Python code can run consistently across different operating systems, 
                ** such as Windows,Linux, and macOS.
        >> Using Python also offers the possibility of automating your processes
                ** automating retries if a download fails, 
                ** retrieving and saving multiple files from URLs, 
                ** and processing and storing your data in designated locations.
# urllib 
        ** doesn’t require installing additional packages
        ** provides a convenient way to interact with web resources ( network communication tasks)
                >> parsing URLs
                >> sending HTTP requests
                >> downloading files 
                >> handling errors related to network operations.
        ** intergrates with (works well with other modules)
                >> re (regurlar expressions)
                >> json -- working with JSON data -- consume JSON APIs.
                >> use with third party libraries
                        >>> requests, BeautifulSoup, and Scrapy
        ## Uses
                ** download-file-from-url/ 
                from urllib.request import urlretrieve
				
				url = (
				"https://api.worldbank.org/v2/en/indicator/"
				"NY.GDP.MKTP.CD?downloadformat=csv"
				)
				filename = "gdp_by_country.zip"
				
				urlretrieve(url, filename)
					** The function returns a tuple of two objects: 
						>> the path to your output file 
						>> HTTP message object.
							>>> path, headers = urlretrieve(url, filename)
							>>> for name, value in headers.items():
									print(name, value)
									
										** This information might be helpful when you’re unsure about which file format you’ve just downloaded 
										** and how you’re supposed to interpret its content. In this case, it’s a ZIP file
										
										** You can also deduce the original filename, which was API_NY.GDP.MKTP.CD_DS2_en_csv_v2_5551501.zip.
									
									    # Date Mon, 24 Feb 2025 19:34:09 GMT
										# Content-Type application/zip
										# Content-Length 137611
										# Connection close
										# CF-Ray 9171e431bf8d73d8-JNB
										# CF-Cache-Status DYNAMIC
										# Cache-Control public, must-revalidate, max-age=1
										# Content-Disposition attachment; filename=API_NY.GDP.MKTP.CD_DS2_en_csv_v2_76261.zip
										# Expires Mon, 24 Feb 2025 19:34:10 GMT
										# Last-Modified Mon, 24 Feb 2025 19:34:09 GMT
										# Set-Cookie api.worldbank.orgCORS=403be8494990e664779c34c52fa19686; Path=/; SameSite=None; Secure
										# Request-Context appId=cid-v1:da002513-bd8b-4441-9f30-737944134422
										# Vary Accept-Encoding
										# Set-Cookie api.worldbank.org=403be8494990e664779c34c52fa19686; Path=/
										# Set-Cookie dataapi.cookie=!6lk7sYQm9bgxCoemhPZvdttxlmnj5Ejn/GFBX89EKY7r/pDCB5Z9qXgtcrW+4xAQgzKJ4jzmUWRFhQ==; path=/; Httponly
										# Set-Cookie TS01b02907=01ebd1be3b68b479249627c217049f0136c983235c6e5cdcf01ba42e4d02b38f2840b3bcc76ffeaa36c8f024d50260c9ed03f91754ec995cdf574fbf560c2245fcb548c5d3; Path=/;
										# Set-Cookie BIGipServerdataapi.sfarm=!UtXQO91obgIajmO+0DQ2KuFjUXGKvdMZBTfJz9ahE484QjkUbpW3LZXUonBabSCwHaZ27nII2M2wJlA=; path=/; Httponly
										# Set-Cookie TS01fa65e4=01359ee9763810f19c4ddaeeef5421bef2cac92a373a4e5ad2cbd5262f70fdeb769cdcf274ada33a0ea75107ede62bd9f56f7ef757a3dc2fe4912bfd3c514e6e608da29483f9e6b373e6aa87b0138c832bde89365acb8ae58a0f26583ca71771b0ae6cf820; Path=/;
										# Set-Cookie __cf_bm=TFFCBUDDQ8n_guFYCEW.aOX16_xPut.tqC19rBsRVBM-1740425649-1.0.1.1-D6Wz120tdRoQ.txmpQBT8Ar.VJHwKrBID1MJ094BHVVDnNVUcB3GYC7J9.JerYRpD.gpnVMjbW7_bY6.92tdyA; path=/; expires=Mon, 24-Feb-25 20:04:09 GMT; domain=.worldbank.org; HttpOnly
										# Set-Cookie _cfuvid=49tawbPskyaffIW1JI2Zpr9n1LbbWNaYqd6fyKcY418-1740425649248-0.0.1.1-604800000; path=/; domain=.worldbank.org; HttpOnly
										# Set-Cookie __cf_bm=OzC0carssa.Q.nA.pSOHCo3mrETDx5fh4iz_Y5ipwXo-1740425649-1.0.1.1-VqOZi1vDl3mh2YzDLmymAuN4s_._3SHk4XIrE1WLcX7FWM6VUg5sbrhboO.IBBtfmoK_FYGlz7sy0fG0C4ExPw; path=/; expires=Mon, 24-Feb-25 20:04:09 GMT; domain=.worldbank.org; HttpOnly; Secure; SameSite=None
										# Set-Cookie _cfuvid=h2CrRQni7fHQ0maEtV2tv2kcXZq_uflLQL.eWLYY9TU-1740425649398-0.0.1.1-604800000; path=/; domain=.worldbank.org; HttpOnly; Secure; SameSite=None
										# Server cloudflare
											
# Requests
		** use third-party libraries to make more advanced HTTP requests, such as those requiring some form of authentication.
		** allowing you to customize it according to your project requirements. 
		**           Some examples include 
						>> the ability to specify request headers, 
						>> handle cookies, 
						>> access data behind login-gated web pages
						>> stream data in chunks, 
						>> and more.
			
			## setup
				python -m pip install requests
			
			## Uses
				** download-file-from-url/
				import requests
				
				### When you make HTTP requests to web servers, you have two commonly used methods to choose from:

                    HTTP GET
                    HTTP POST
				
				** You’ll use the GET method to retrieve data by fetching a representation of the remote resource without modifying the server’s state. 
				** Therefore, you’ll commonly use it to retrieve files like images, HTML web pages, or raw data.  
				
				    #  Python’s implicit concatenation by splitting the string literal over multiple lines inside parentheses. 
					# The Python interpreter will automatically join the separate strings on different lines into a single string.
					url = (
						"https://api.worldbank.org/v2/en/indicator/"
						"NY.GDP.MKTP.CD"
					)
					filename = "gdp_by_country.zip"
					query_parameters = {"downloadformat": "csv"}# "?downloadformat=csv"

					# The function returns an HTTP response object with the server’s response to the request. 
					response = requests.get(url, params=query_parameters)#"https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.CD" + "?downloadformat=csv"

					# The function returns a tuple of two objects: the path to your output file and an HTTP message object.
					print('\n' + 'url' +response.url+ '\n') 
					print('\n' + 'response.ok True/False' +response.ok +'\n')
					print('\n' + 'response.status_code 200/400' +response.status_code +'\n')  

					# Saving Downloaded Content to a File


					"""         ** Now that you’ve retrieved content from a URL using the requests library, you can save it to your computer locally. 
								** When saving data to a file in Python, it’s highly recommended to use the with statement. 
								** It ensures that Python properly manages resources, including files, and automatically closes them when you no longer need them.
					"""
					with open("gdp_by_country.zip", mode="wb") as file:
						file.write(response.content)
			
			## Raise errors
				    # Saving Downloaded Content to a File
					if response.status_code == requests.codes.ok: # Status 200
					  with open("samo_q_1stRound3_RaiseError.pdf", mode="wb") as file:
						file.write(response.content)
					else: # raise error, so that an exception is thrown
					   response.raise_for_status()
					file.close
					** The raise_for_status() method is a good way to ensure that a program
					** halts if a bad download occurs.
			
# bs4 BeautifulSoup 
        ** Beautiful Soup is a module for extracting information from an HTML
		** page (and is much better for this purpose than regular expressions). The
		** Beautiful Soup module’s name is bs4 (for Beautiful Soup, version 4).
			## setup
				pip install --user beautifulsoup4
			## Uses
				>>> import requests, bs4
				>>> res = requests.get('https://nostarch.com')
				>>> res.raise_for_status()
				>>> noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
				>>> type(noStarchSoup)
				<class 'bs4.BeautifulSoup'>
			
			## CS
				# # CSS Selector passed to the select() method Will match . . .
				"""
					soup.select('div') All elements named <div>
					soup.select('#author') The element with an id attribute of author
							id attribute is prefixed with "#"
							class attribute is prefixed with "."
					soup.select('.notice') All elements that use a CSS class attribute
					named notice
					soup.select('div span') All elements named <span> that are within
					an element named <div>
					soup.select('div > span') All elements named <span> that are
					directly within an element named <div>,
					with no other element in between
					soup.select('input[name]') All elements named <input> that have a
					name attribute with any value
					soup.select('input[type="button"]') All elements named <input> that have an
					attribute named type with value button
				"""

* The POST method allows you to send data for the server to process or use in creating or updating a resource.  
* In POST requests, the data is typically sent in the request body in various formats like JSON or XML, and it’s not visible in the URL.  
* You can use POST requests for operations that modify server data, such as creating, updating, or submitting existing or new resources.  
		
# https://stackoverflow.com/questions/45107839/python-login-and-download-specific-file-from-website

    # If the Website that you linked uses HTTP POST based login from.

    # which will use basic http authentication http://docs.python-requests.org/en/master/user/authentication/#basic-authentication 

    #To login to this site you need two things:
    #
    #    1) persistent session cookie
    #    2) HTTP POST request to login form URL
    #    First of all let's create session object that will be holding cookies form serve
    #     http://docs.python-requests.org/en/master/user/advanced/#session-objects
    #       
            # 1)
            s = requests.Session()

            
    # Next you need to visit site using GET request. This will generate cookie for you (server will send cookie for your session).

            s.get(site_url) # generate cookie

    # Final step will be to login to site. You can use Firebug or Chrome Developer Console (depending of what browser you use) 
    # to examine what fields needs to be send (Go to Network tab).

            s.post(site_url, data={'_username': 'user', '_password': 'pass'})


    # Save file (https://realpython.com/python-download-file-from-url/)
    
            query_parameters = {"downloadformat": "pdf"}
            response00= s.get(inputPath+inputFile, params=query_parameters)
            while (response00.ok == True):

                with open(outputPath+outputFile, mode="wb") as file:
                file.write(response00.content)
                file.close

                response00= s.get(inputPath+inputFileA, params=query_parameters)
                if (response00.ok == True):
                    with open(outputPath+outputFileA, mode="wb") as file:
                    file.write(response00.content)
                    file.close
                else:
                    continue
# Downloading a Large File in a Streaming Fashion

# requests
	
	## Data streams
		>> Download and process a file in small chunks
			*This comes in handy when a network enforces restrictions on the size ofdata transfer in a single request.
		>> Process and consume the data in real time
			*you can use and extract insights from thedownloaded content of the file while the remaining data continues to download.
		>> Pause and resume the download process
			*This enables you to download a portion of the file, pause the operation, andlater resume where you left off, without having to restart the entire download.

# TLS fingerprint
		A blazing-fast Python HTTP Client with TLS fingerprint
			https://github.com/0x676e67/rnet
				https://github.com/0x676e67/rnet