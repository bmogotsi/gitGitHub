#! python3
# A Shebang indicates which Bash or Python interpreter to use to interpret an executable file. 

# https://www.geeksforgeeks.org/how-to-download-files-from-urls-with-python/

import wget

try:
    # samu_Que = https://www.samf.ac.za/content/files/QuestionPapers/j1q82024.pdf
    # samo_Sol = https://www.samf.ac.za/content/files/QuestionPapers/j1s82024.pdf
    inputPath = 'https://www.samf.ac.za/content/files/QuestionPapers/'

    uStart = 'j'
    uRound = 1
    uQorA = 'q'
    uGrade = 8
    uYear = 2024
    uExtension = '.pdf'

    inputFile = uStart+str(uRound)+uQorA+str(uGrade)+str(uYear)+uExtension

    outputPath = 'C:/Users/Ben/OneDrive/Documents/0123_KB_Docs/Online_School/Math_Olympiad/SAMO_2025/Resouce_and_Papers_SAMO/Downloaded/'
    outputFile = 'Samo_' + str(uYear) + '_'+str(uRound)+'_'+uQorA

    wget.download(inputPath+inputFile, outputPath+outputFile)
    print('downloaded')

    exit
except Exception as e:
    print("Exception...:" +inputPath+inputFile+ '\n' +str(e))
    

"""
msg =
'Forbidden'
name =
'<urllib response>'
reason =
'Forbidden'
status =
403"""