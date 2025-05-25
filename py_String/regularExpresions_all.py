#! python3
# A Shebang indicates which Bash or Python interpreter to use to interpret an executable file. 
# All and Sundry regular expresions

import re, sys

text_data = str("Hello, how are you? I am Carol.\n"
"Hello, Carol, my name is Frank. Nice to meet you.\n"
"Nice to meet you too. How are you today?\n"
"Great. My football team won the competition.\n"
"Wow, congratulations Frank!\n"
"Thank you Carol.\n"
"Shall we have a pizza later to celebrate?\n"
"Sure. Do you recommend any restaurant, Carol?\n"
"Yes, a new restaurant opened, and they say the banana pizza is phenomenal.\n"
"Okay. Let's meet at the restaurant at seven PM, is that okay?\n"
"That's fine. See you later then.")

#  1. Filter(remove) special characters: '.', ',', '?', '!'
sentences = re.sub("[.,!?\\-]", '', text_data.lower()).split('\n')
print(sentences)