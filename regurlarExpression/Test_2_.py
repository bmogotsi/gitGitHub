
import re
import sys

# re.findall(patern, string) to find any text within a string that matches a given regular expression:

def findAll(inParten,inSTr):
    return re.findall(inParten, inSTr,re.I)
 
reStr= 'abbbbc'
rePatern = 'ab*c' # starts with "a" + zero or more "b" + ends with "c"

result = findAll(rePatern, reStr)

reStr= 'abenHc'
rePatern = 'a[a-z]*c' # starts with "a" + zero or more "a to z" + ends with "c"

result = findAll(rePatern, reStr)

reStr= '"abcac'
rePatern = 'ab*c'

result = findAll(rePatern, reStr)

sys.exit


