# https://realpython.com/python-web-scraping-practical-introduction/#interact-with-websites-in-real-time
#  re.sub()
#       which is short for substitute, allows you to replace the text in a string that matches a regular expression with new text. 
#       It behaves sort of like the .replace() string method.


import re
import sys

string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*?>", "ELEPHANTS", string)
print(string)  
# "Everything is ELEPHANTS if it's in ELEPHANTS."
# This time, re.sub() finds two matches, <replaced> and <tags>, and substitutes the string "ELEPHANTS" for both matches.
# 
#  
sys.exit