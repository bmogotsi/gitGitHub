#! python3
# A Shebang indicates which Bash or Python interpreter to use to interpret an executable file. 

# Split string to a list
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

# 8. Filter(remove) special characters: '.', ',', '?', '!'
sentences = re.sub("[.,!?\\-]", '', text_data.lower()).split('\n')
print(sentences)

word_listJoin = list(" ".join(sentences))
print(word_listJoin)
# 10. Split the sentences into words and create a word list
#       SET =Build an unordered collection of unique elements.
#       JOIN = Concatenate any number of strings.
#           The string whose method is called is inserted in between each given string. The result is returned as a new string.
#           Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
word_list = list(set(" ".join(sentences).split()))
print(word_list)

exit