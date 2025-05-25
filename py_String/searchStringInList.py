#! python3
# A Shebang indicates which Bash or Python interpreter to use to interpret an executable file. 

searchWord = '# Galatasaray Istanbul'
# searchString = "# Galatasaray Istanbul , # Galatasaray Istanbul , Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray SK , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , # Galatasaray Istanbul , ## Galatasaray SK , # Galatasaray Istanbul , # Galatasaray SK"
searchString = """# Galatasaray Istanbul, 
# Galatasaray Istanbul , Galatasaray Istanbul 
# , # Galatasaray Istanbul , # Galatasaray Istanbul ,"""

## Use brackets ("")  to split multines
searchString = ("# Galatasaray Istanbul , " 
"# Galatasaray Istanbul , Galatasaray Istanbul" 
", # Galatasaray Istanbul , # Galatasaray Istanbul")
searchList = searchString.split(",")

#  Multiline String Using Backslash \
searchString = "# Galatasaray Istanbul," \
"# Galatasaray Istanbul,Galatasaray Istanbul" \
", # Galatasaray Istanbul , # Galatasaray Istanbul"
searchList = searchString.split(",") 

# search
answer = [i for i in searchList if searchWord in i] 
if answer != []:
    print("Serach String \"{}\" found in {} List".format(searchWord, searchList))

# search exact match
if searchWord in searchList:
    print("Serach String \"{}\" found EXACT Match in {} List".format(searchWord, searchList))

# how-to-remove-all-spaces-in-the-strings-in-list 
# str.split() divides a string into substrings based on a delimiter while str.join() combines a list of substrings into a single string with a specified separator.
trimmedList = [' '.join(string.split()) for string in searchList]
if searchWord in trimmedList:
    print("Serach String \"{}\" found trimmed (strip) Match in {} List".format(searchWord, trimmedList))

exit