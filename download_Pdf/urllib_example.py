#! python3
# A Shebang indicates which Bash or Python interpreter to use to interpret an executable file. 

# https://realpython.com/python-download-file-from-url/

from urllib.request import urlretrieve

try:
    #  Python’s implicit concatenation by splitting the string literal over multiple lines inside parentheses. 
    # The Python interpreter will automatically join the separate strings on different lines into a single string.
    url = (
        "https://api.worldbank.org/v2/en/indicator/"
        "NY.GDP.MKTP.CD?downloadformat=csv"
    )
    filename = "urllib_gdp_by_country.zip"

    # urlretrieve(url, filename)

    path, headers = urlretrieve(url, filename)
    # The function returns a tuple of two objects: the path to your output file and an HTTP message object.
    print('\n' + path+ '\n') # path to your output file
    for name, value in headers.items(): # HTTP message object
        print(name, value)

    # This information might be helpful when you’re unsure about which file format you’ve just downloaded 
    # and how you’re supposed to interpret its content. In this case, it’s a ZIP file
    """         ** This information might be helpful when you’re unsure about which file format you’ve just downloaded 
				** and how you’re supposed to interpret its content. In this case, it’s a ZIP file
										
				** You can also deduce the original filename, which was API_NY.GDP.MKTP.CD_DS2_en_csv_v2_5551501.zip.
    """

    # Date Mon, 24 Feb 2025 19:34:09 GMT
    # Content-Type application/zip
    # Content-Length 137611
    # Connection close
    # CF-Ray 9171e431bf8d73d8-JNB
    # CF-Cache-Status DYNAMIC
    # Cache-Control public, must-revalidate, max-age=1
    # Content-Disposition attachment; filename=API_NY.GDP.MKTP.CD_DS2_en_csv_v2_76261.zip
    # Expires Mon, 24 Feb 2025 19:34:10 GMT
    # Last-Modified Mon, 24 Feb 2025 19:34:09 GMT
    # Set-Cookie api.worldbank.orgCORS=403be8494990e664779c34c52fa19686; Path=/; SameSite=None; Secure
    # Request-Context appId=cid-v1:da002513-bd8b-4441-9f30-737944134422
    # Vary Accept-Encoding
    # Set-Cookie api.worldbank.org=403be8494990e664779c34c52fa19686; Path=/
    # Set-Cookie dataapi.cookie=!6lk7sYQm9bgxCoemhPZvdttxlmnj5Ejn/GFBX89EKY7r/pDCB5Z9qXgtcrW+4xAQgzKJ4jzmUWRFhQ==; path=/; Httponly
    # Set-Cookie TS01b02907=01ebd1be3b68b479249627c217049f0136c983235c6e5cdcf01ba42e4d02b38f2840b3bcc76ffeaa36c8f024d50260c9ed03f91754ec995cdf574fbf560c2245fcb548c5d3; Path=/;
    # Set-Cookie BIGipServerdataapi.sfarm=!UtXQO91obgIajmO+0DQ2KuFjUXGKvdMZBTfJz9ahE484QjkUbpW3LZXUonBabSCwHaZ27nII2M2wJlA=; path=/; Httponly
    # Set-Cookie TS01fa65e4=01359ee9763810f19c4ddaeeef5421bef2cac92a373a4e5ad2cbd5262f70fdeb769cdcf274ada33a0ea75107ede62bd9f56f7ef757a3dc2fe4912bfd3c514e6e608da29483f9e6b373e6aa87b0138c832bde89365acb8ae58a0f26583ca71771b0ae6cf820; Path=/;
    # Set-Cookie __cf_bm=TFFCBUDDQ8n_guFYCEW.aOX16_xPut.tqC19rBsRVBM-1740425649-1.0.1.1-D6Wz120tdRoQ.txmpQBT8Ar.VJHwKrBID1MJ094BHVVDnNVUcB3GYC7J9.JerYRpD.gpnVMjbW7_bY6.92tdyA; path=/; expires=Mon, 24-Feb-25 20:04:09 GMT; domain=.worldbank.org; HttpOnly
    # Set-Cookie _cfuvid=49tawbPskyaffIW1JI2Zpr9n1LbbWNaYqd6fyKcY418-1740425649248-0.0.1.1-604800000; path=/; domain=.worldbank.org; HttpOnly
    # Set-Cookie __cf_bm=OzC0carssa.Q.nA.pSOHCo3mrETDx5fh4iz_Y5ipwXo-1740425649-1.0.1.1-VqOZi1vDl3mh2YzDLmymAuN4s_._3SHk4XIrE1WLcX7FWM6VUg5sbrhboO.IBBtfmoK_FYGlz7sy0fG0C4ExPw; path=/; expires=Mon, 24-Feb-25 20:04:09 GMT; domain=.worldbank.org; HttpOnly; Secure; SameSite=None
    # Set-Cookie _cfuvid=h2CrRQni7fHQ0maEtV2tv2kcXZq_uflLQL.eWLYY9TU-1740425649398-0.0.1.1-604800000; path=/; domain=.worldbank.org; HttpOnly; Secure; SameSite=None
    # Server cloudflare

    exit
except Exception as e:
    print("exception....     " + str(e))