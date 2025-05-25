#! python3
# A Shebang indicates which Bash or Python interpreter to use to interpret an executable file.

# Basically you want to truncate the file, this can be any file. In this case it's a csv file so:
try:
    outputPath = "C:/Users/Ben/OneDrive/Documents/Gaba_Docs/development/Python/Python_Ben/pgmOutput/"
    outputFile = "copyCsvTo_wsb_Teams"   + ".csv"
    filename = outputPath+outputFile
    # opening the file with w+ mode truncates the file
    f = open(filename, "w+")
    f.close()

    exit 
    
except Exception as e:
    print("Exception.....:    " + str(e))