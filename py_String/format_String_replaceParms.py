#! python3
# A Shebang indicates which Bash or Python interpreter to use to interpret an executable file. 

# word to find: 'correct'
word = 'correct'
arryToSearch = ['this is correct ', 'this is corrected', 'stingray for dinner', '#correct stingray for dinner']

answer = [i for i in arryToSearch if word in i] #return if part of a string is contains 

wordR = word.rjust(len(word)+1)
wordL = word.ljust(len(word)+3,"#")
answer2 = [i for i in arryToSearch if word in i] 

print(f"Original word>>>>>>>  {wordR}") 
print(f"<<<Right Adjyst: word.rjust(8)>>>>>>>>>{wordR}     <<<(Left Adjust word.ljust(len(word)+1,\"#\")>>>>>>>>{wordL})")

# Example: Categorizing configurations
config = {"type": "database", "name": "PostgreSQL", "version": 13}

match config:
    case {"type": "database", "name": name, "version": version}:
        print(f"Database: {name} (Version {version})")
    case {"type": "cache", "name": name}:
        print(f"Cache system: {name}")
    case _:
        print("Unknown configuration.")


exit