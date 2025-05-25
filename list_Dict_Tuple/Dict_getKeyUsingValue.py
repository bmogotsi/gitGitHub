#! python3
# A Shebang indicates which Bash or Python interpreter to use to interpret an executable file. 

import sys
import pprint

vocab = {'a': 2,
 'dataset': 5,
 'for': 6,
 'gpt': 7,
 'is': 1,
 'small': 3,
 'test': 4,
 'this': 0,
 'training': 8}

print("Vocab: Normal Print ")
print(vocab)
# Pretty Print
print("\n Vocab: Pretty Print ")
pprint.pprint(vocab)

#  get dictionary key using value
print("1 2 3"  )
keys = [key for key, val in vocab.items() if (val == 1 or val == 2 or val == 3)]
print(keys)

exit