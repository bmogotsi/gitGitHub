#! python3
# A Shebang indicates which Bash or Python interpreter to use to interpret an executable file. 

# word to find: 'correct'
word = 'correct'
arryToSearch = ['this is correct ', 'this is corrected', 'stingray for dinner', '#correct stingray for dinner']

answer = [i for i in arryToSearch if word in i] #return if part of a string is contains 

wordR = word.rjust(8)
wordL = word.ljust(len(word)+1,"#")
answer2 = [i for i in arryToSearch if word in i] 

a='DEAL Fc'
b='FC DEAL '
ac =a.strip().upper().strip("FC").strip()
if a.strip().upper().strip("FC").strip() == b.strip().upper().strip("FC").strip():
    print("YES we can >>>  " + a.strip().upper().strip("FC").strip())
bc =str(str(str(a.strip().upper)).strip("FC"))
ad =str(a.strip("FC"))
ad = ad.strip("FC").strip()
bd =str(str(a.upper).strip("FC")).strip()

for index,ans in enumerate(answer2):
    b=str(ans)[:1]
    if str(ans)[:1].isalpha()==True:
        print(str(ans).strip() + "  " + b)
    else:
        print(b +  " >>>>>>>>>>>>>>>>>> " + str(ans).strip() )

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