#! python3
# A Shebang indicates which Bash or Python interpreter to use to interpret an executable file.
# Get the list of files using os.listdir() method

# import OS module
import os
# Get the list of all files and directories
path = outputPath = "C://Users//ben//OneDrive//Documents//Gaba_Docs//development//Python//Python_Ben//pgmOutput"
dir_list = os.listdir(path)
print("Files and directories in '", path, "' :")
# prints all files
# print(dir_list) : # pints a Python LIST (array) which is unformated

for file in dir_list: # prints a formated sequential list
    print(file)

exit

