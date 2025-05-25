
# Import libraries
import requests
from bs4 import BeautifulSoup

# "C:\Users\Ben\OneDrive\Documents\Gaba_Docs\development\Dev_Books\Adult_Dev\Py_Automate2e_AutomatThBoringStaff2ndEdition.pdf"

# You can retrieve a web page element from a BeautifulSoup object by calling
# the select()method and passing a string of a CSS selector for the element you
# are looking for. Selectors are like regular expressions: they specify a pattern
# to look for—in this case, in HTML pages instead of general text strings.


# # CSS Selector passed to the select() method Will match . . .
"""
    soup.select('div') All elements named <div>
    soup.select('#author') The element with an id attribute of author
            id attribute is prefixed with "#"
            class attribute is prefixed with "."
    soup.select('.notice') All elements that use a CSS class attribute
    named notice
    soup.select('div span') All elements named <span> that are within
    an element named <div>
    soup.select('div > span') All elements named <span> that are
    directly within an element named <div>,
    with no other element in between
    soup.select('input[name]') All elements named <input> that have a
    name attribute with any value
    soup.select('input[type="button"]') All elements named <input> that have an
    attribute named type with value button
"""

try:
    # URL from which pdfs to be downloaded
    # url = "https://www.geeksforgeeks.org/how-to-extract-pdf-tables-in-python/"
    url = "https://nostarch.com/"
    url_domain = "https://www.samf.ac.za"
    
    # Requests URL and get response object
    response = requests.get(url)
    
    # Parse text obtained
    soup = BeautifulSoup(response.text, 'html.parser')
 
    elems = soup.select('#edit-submit-2') # The element with an id attribute of "#edit-submit-2" "#" indicates ID attribute
    print(elems) # elems is a list of Tag objects.
    print(len(elems)) # Print the tag and its attributes
    if elems != []:
        print(elems[0])
        str(elems[0]) # The Tag object as a string.
        elems[0].getText()
        elems[0].attrs

    elems = soup.select('.leaf') # The element with an id attribute of ".leaf" "." indicates class attribute
    print(elems) # elems is a list of Tag objects.
    print(len(elems)) # Print the tag and its attributes
    if elems != []:
        print(elems[0])
        str(elems[0]) # The Tag object as a string.
        text=elems[0].getText()
        attr=elems[0].attrs

    elems = soup.select('section .leaf') # The element with an id attribute of ".leaf" "." indicates class attribute also withon <section> element NOT DIRECTLY.
    print(elems) # elems is a list of Tag objects.
    print(len(elems)) # Print the tag and its attributes
    for elem in elems:
        if ('leaf' in elem.get('class', [])): # is the element "button" with a "type" attribute named "submit"
            print(elem)
            text=str(elem.get('class',[])) # [] is the default in case we did not find
            attr=elem.attrs
            if elem.get('some_nonexistent_addr') == None:
                print("elem.get('some_nonexistent_addr') == None" + "........         " + str(elem.get('some_nonexistent_addr') == None) )
            if elem.get("[]'first', 'last', 'leaf']") != None:  # ??? does not worj
                print("elem.get('elem.get('last') != None" + "........         " + str(elem.get('last') != None) )



    elems = soup.select('button[type]') # All elements named <button> that have a "type" attribute with any value
    print(elems) # elems is a list of Tag objects.
    print(len(elems)) # Print the tag and its attributes
    for elem in elems:
        if ('submit' in elem.get('type', [])): # is the element "button" with a "type" attribute named "submit"
            print(elem)
            text=elem.getText()
            attr=elem.attrs
        elif ('button' in elem.get('type', [])): # is the element "button" with a "type" attribute named "button" 
            print(elem)
            text=elem.getText()
            attr=elem.attrs
            for at in attr: # all atributes of the element "button" 
                print(at) 
                """  6 attributes found
                    type
                    class
                    data-toggle
                    data-target
                    aria-expanded
                    aria-controls
                
                """
    elems = soup.select('button[type="submit"]') # All elements named <button> that have a "type" attribute with value "submit"
    print(elems) # elems is a list of Tag objects.
    print(len(elems)) # Print the tag and its attributes
    for elem in elems:
        if ('submit' in elem.get('type', [])): # is the element "button" with a "type" attribute named "submit"
            print(elem)
            text=elem.getText()
            attr=elem.attrs

    elems = soup.select('form div button') # All elements named <button> that are within "<div>" within "<form>"
    print(elems) # elems is a list of Tag objects.
    print(len(elems)) # Print the tag and its attributes
    for elem in elems:
        if ('submit' in elem.get('type', [])): # is the element "button" with a "type" attribute named "submit"
            print(elem)
            text=elem.getText()
            attr=elem.attrs

    elems = soup.select('form > div > button') # All elements named <button> that are DIRECTLY within "<div>" within "<form>" with NO other elements in between
    print(elems) # elems is a list of Tag objects.
    print(len(elems)) # Print the tag and its attributes
    for elem in elems:
        if ('submit' in elem.get('type', [])): # is the element "button" with a "type" attribute named "submit"
            print(elem)
            text=elem.getText()
            attr=elem.attrs
    
    elems = soup.select('form > button') # All elements named <button> that are DIRECTLY within "<form>" (should fail because we have "<div> in-between")
    print(elems) # elems is a list of Tag objects.
    print(len(elems)) # Print the tag and its attributes
    for elem in elems:
        if ('submit' in elem.get('type', [])): # is the element "button" with a "type" attribute named "submit"
            print(elem)
            text=elem.getText()
            attr=elem.attrs
    
    elems = soup.select('form button') # All elements named <button> that are within "<form>" (should pass because we did not use ">" to indicate DIRECTLY)
    print(elems) # elems is a list of Tag objects.
    print(len(elems)) # Print the tag and its attributes
    for elem in elems:
        if ('submit' in elem.get('type', [])): # is the element "button" with a "type" attribute named "submit"
            print(elem)
            text=elem.getText()
            attr=elem.attrs


    exit
    raise # ending processing temporarily due to debug
    
    # Find all hyperlinks present on webpage
    links = soup.find_all('a')
    
    i = 0
    
    # From all links check for pdf link and
    # if present download file
    for link in links:
        # if ('.pdf' in link.get('href', [])):
        if ('samo-question-papers' in link.get('href', [])):
            i += 1
            print("Downloading file: ", i)
    
            # Get response object for link
            getLink = url_domain+str(link.get('href'))
            response = requests.get(getLink)
    
            # Write content in pdf file
            if response.status_code == requests.codes.ok: # 200
                pdf = open("pdf"+str(i)+".pdf", 'wb')
                pdf.write(response.content)
                pdf.close()
                print("File ", i, " downloaded")
    
    print("All PDF files downloaded")

    exit

except Exception as e:
    print("exception....     " + str(e))