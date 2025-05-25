#! python3
# A Shebang indicates which Bash or Python interpreter to use to interpret an executable file. 

# https://stackoverflow.com/questions/45107839/python-login-and-download-specific-file-from-website
# https://realpython.com/python-download-file-from-url/

import requests

# user, password = 'ben.mogotsi@gmail.com', 'Rantsaopane1'
# Note that if a site is not using HTTPS secure connection. 
# Any credentials you will provide will go through the internet unencrypted and can be potentially see by someone who should not see them.

try:
    site_url = 'https://www.samf.ac.za/en/'
    error_url = 'https://www.samf.ac.za/en/samo-question-papers'
    file_url = 'https://www.samf.ac.za/content/files/QuestionPapers/j1q82024.pdf'
    #To login to this site you need two things:
    #
    #    1) persistent session cookie
    #    2) HTTP POST request to login form URL
    #    First of all let's create session object that will be holding cookies form serve
    #     http://docs.python-requests.org/en/master/user/advanced/#session-objects

          #    s = requests.Session() # 1) persistent session cookie
          #
          #    # Next you need to visit site using GET request. This will generate cookie for you (server will send cookie for your session).
          #
          #    response = s.get(site_url) # generate cookie
          #    print(response.ok)
          #    # True
          #
          #    print(response.status_code)
          #    # 200
          #
          #    # Final step will be to login to site. You can use Firebug or Chrome Developer Console (depending of what browser you use) 
          #    # to examine what fields needs to be send (Go to Network tab).
          #
          #    response2 = s.post(site_url, data={'_username': 'user', '_password': 'pass'}) # 2) HTTP POST request to login form URL
          #    print(response2.ok)
          #    # True
          #

    # 200
    # After that you will be authenticated. Next thing will be to visit URL for file you would like to download.
    query_parameters = {"downloadformat": "pdf"}
    response= requests.get(error_url)
    #response= requests.get(file_url, params=query_parameters)
    print(response.ok)
    # True

    print(response.status_code)
    # 200

    #print(response3.content)
    print("file downloaded....: " + file_url)

    # Saving Downloaded Content to a File
    if response.status_code == requests.codes.ok: # 200
      with open("samo_q_1stRound3_RaiseError.pdf", mode="wb") as file:
        file.write(response.content)
    else: # raise error, so that an exception is thrown
       		# ** The raise_for_status() method is a good way to ensure that a program
					# ** halts if a bad download occurs.
       response.raise_for_status()
    file.close
    exit
except Exception as e:
    print("Exception...:" + "  Site   "   +error_url+ "  file    " +file_url + '\n' +str(e))
    
    """
msg =
'Forbidden'
name =
'<urllib response>'
reason =
'Forbidden'
status =
403"""