#! python3
# A Shebang indicates which Bash or Python interpreter to use to interpret an executable file. 

# https://stackoverflow.com/questions/45107839/python-login-and-download-specific-file-from-website
# https://realpython.com/python-download-file-from-url/

import requests
from bs4  import BeautifulSoup
from datetime import datetime, timedelta, date

user, password = 'ben.mogotsi@gmail.com', 'Rantsaopane1'
# Note that if a site is not using HTTPS secure connection. 
# Any credentials you will provide will go through the internet unencrypted and can be potentially see by someone who should not see them.

inputPath = 'https://www.samf.ac.za/content/files/QuestionPapers/'
uStart = 'j'
uRound = 1
uQorA = 'q'
uGrade = 8
uYear = 2024
uExtension = '.pdf'

inputFile = uStart+str(uRound)+uQorA+str(uGrade)+str(uYear)+uExtension

outputPath = 'C:/Users/Ben/OneDrive/Documents/0123_KB_Docs/Online_School/Math_Olympiad/SAMO_2025/Resouce_and_Papers_SAMO/Downloaded/'
outputFile = 'Samo_' + str(uYear) + '_'+str(uRound)+'_'+uQorA+uExtension

try:
    def getInFileName(inYear,inQorA):
          uStart = 'j'
          uRound = 1
          uQorA = inQorA
          uGrade = 8
          uYear = inYear
          uExtension = '.pdf'

          inFile = uStart+str(uRound)+uQorA+str(uGrade)+str(uYear)+uExtension
          return inFile
    
    def getOutFileName(outYear, outQorA):
          uStart = 'j'
          uRound = 1
          uQorA = outQorA
          uGrade = 8
          uYear = outYear
          uExtension = '.pdf'

          outFile = 'Samo_' + str(uYear) + '_'+str(uRound)+'_'+uQorA+uExtension
          return outFile

    site_domain = 'https://www.samf.ac.za'
    site_url = 'https://www.samf.ac.za/en/'
    file_url = 'https://www.samf.ac.za/content/files/QuestionPapers/j1q82024.pdf'
    files_url = 'https://www.samf.ac.za/en/samo-question-papers'
    #To login to this site you need two things:
    #
    #    1) persistent session cookie
    #    2) HTTP POST request to login form URL
    #    First of all let's create session object that will be holding cookies form serve
    #     http://docs.python-requests.org/en/master/user/advanced/#session-objects

    s = requests.Session() # 1) persistent session cookie

    # Next you need to visit site using GET request. This will generate cookie for you (server will send cookie for your session).

    response = s.get(site_url) # generate cookie
    print(response.ok)
    # True

    print(response.status_code)
    # 200
    if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'html.parser') # 404 repose expected 200
      
      # Find all hyperlinks present on webpage
      links = soup.find_all('a')

    # Final step will be to login to site. You can use Firebug or Chrome Developer Console (depending of what browser you use) 
    # to examine what fields needs to be send (Go to Network tab).

    response2 = s.post(site_url, data={'_username': 'user', '_password': 'pass'}) # 2) HTTP POST request to login form URL
    print(response2.ok)
    # True

    print(response2.status_code)
    # 200
    if response2.status_code == 200:
      soup = BeautifulSoup(response2.text, 'html.parser') # 404 repose expected 200
      
      # Find all hyperlinks present on webpage
      links = soup.find_all('a')
        # # From all links check for pdf link and
        # if present download file

      today = date.today() # https://www.geeksforgeeks.org/get-current-date-using-python/
      thisYear = today.year
      nextYear, lastYear = (thisYear+1, thisYear-1)
      i=0
      for link in links:
          # since I cannot get the links from the HTML table ('html.parser')
          # I will go down until there is no more

          if ('samo-question-papers' in link.get('href', [])):
              i += 1
              doYear = thisYear - i
              inputFile=getInFileName(doYear,'q')
              inputFileA=getInFileName(doYear,'s')
              outputFile=getOutFileName(doYear,'q')
              outputFileA=getOutFileName(doYear,'s')
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

                  print("Downloading file: ", i)

                  i += 1
                  doYear = thisYear - i
                  inputFile=getInFileName(doYear,'q')
                  inputFileA=getInFileName(doYear,'s')
                  outputFile=getOutFileName(doYear,'q')
                  outputFileA=getOutFileName(doYear,'s')
                  response00 = s.get(inputPath+inputFile, params=query_parameters)

              # from 2010-1998 downwards 8+9 is combined
              inputFile=str(getInFileName(doYear,'q')).replace('8','',1)
              inputFileA=str(getInFileName(doYear,'s')).replace('8','',1)
              outputFile=str(getOutFileName(doYear,'q')).replace('q','q_8n9')
              outputFileA=str(getOutFileName(doYear,'s')).replace('s','s_8n9')
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

                  print("Downloading file: ", i)

                  i += 1
                  doYear = thisYear - i
                  inputFile=str(getInFileName(doYear,'q')).replace('8','',1)
                  inputFileA=str(getInFileName(doYear,'s')).replace('8','',1)
                  outputFile=str(getOutFileName(doYear,'q')).replace('q','q_8n9')
                  outputFileA=str(getOutFileName(doYear,'s')).replace('s','s_8n9')
                  response00 = s.get(inputPath+inputFile, params=query_parameters)
                        
    exit
except Exception as e:
    print("Exception...:" + "  Site   "   +site_url+ "  file    " +file_url + '\n' +str(e))
    
    """
msg =
'Forbidden'
name =
'<urllib response>'
reason =
'Forbidden'
status =
403"""