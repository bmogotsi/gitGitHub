# https://realpython.com/python-web-scraping-practical-introduction/#interact-with-websites-in-real-time
#  re.sub()
#       which is short for substitute, allows you to replace the text in a string that matches a regular expression with new text. 
#       It behaves sort of like the .replace() string method.


import re
import sys

string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*>", "ELEPHANTS", string)
print(string)  
# 'Everything is ELEPHANTS.'
# Perhaps that wasn’t quite what you expected to happen.
# re.sub() uses the regular expression "<.*>" to find and replace everything between the first < and the last >
# , which spans from the beginning of <replaced> to the end of <tags>. 
#   This is because Python’s regular expressions are greedy, meaning they try to find the longest possible match when characters like * are used.
# 
# Alternatively, you can use the non-greedy matching pattern *?, which works the same way as * except that it matches the shortest possible string of text:
sys.exit