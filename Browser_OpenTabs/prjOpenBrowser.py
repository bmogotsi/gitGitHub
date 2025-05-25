#! python3
# A Shebang indicates which Bash or Python interpreter to use to interpret an executable file. 
# Shebangs are supported on Linux and many other operating systems. 
# A Shebang begins with the characters #! and only occurs on the first line of the file

# Open the ussual Tabs

# A web browser tab will open to the URL  
# This is about the only thing the webbrowser module can do
import webbrowser, sys, shelve
import time
# webbrowser.open('https://InventWithPython.com/')


#Save to Shelve File
if 2 > 1: # I want to see how long the shelve (dictionary-like object stored on disk)
    shelfFile = shelve.open('mydata')
    urls = ['https://mail.google.com/mail/u/0/#inbox']
    shelfFile['email'] = urls
    urls = ['https://www.google.com/finance/']
    shelfFile['finance'] = urls
    urls = ['https://www.google.com/']
    shelfFile['search'] = urls
    urls = ['https://www.worldsportsbetting.co.za/']
    shelfFile['wsb'] = urls
    shelfFile.close()

urlList = ['email', 'finance', 'wsb', 'search']

# Handle Commnad Line Arguments
if len(sys.argv) > 1:
# Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Retrieve from shelfFil
    for url in urlList:  
        shelfFile = shelve.open('mydata')
        ad = []
        ad.append(shelfFile[url])
        address = str(ad[0])
        address = address.strip("[]'")    
        webbrowser.open(address)
time.sleep(5) # i added the sleep because the last tab was not being opened thought a delay would give the script time to open it.
print('Im done openning tabs ...:')
shelfFile.close()
