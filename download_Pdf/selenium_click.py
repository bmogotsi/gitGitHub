# google using selenium to download files python
# https://www.geeksforgeeks.org/download-file-in-selenium-using-python/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
# Import Module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service # better than absolute path
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager
 
# Open Chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", False)
# Handling browser certificate errors  
#          [7088:18368:0219/135404.606:ERROR:cert_issuer_source_aia.cc(34)] Error parsing cert retrieved from AIA (as DER):
#          ERROR: Couldn't read tbsCertificate as SEQUENCE
#          ERROR: Failed parsing Certificate#
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument('--ignore-certificate-errors')
driver = Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#driver = webdriver.Chrome(
#    'C:/Users/HP/Desktop/Drivers/chromedriver_win32/chromedriver.exe')
 
# Open URL
#driver.get(
#    'https://www.samf.ac.za/en/samo-question-papers')
driver.get(
    'https://www.samf.ac.za/en/')
 
# Enter text
#driver.find_element('textbox').send_keys("Hello world")
# url=result.get_attribute("href")
 
# Generate Text File
# driver.find_element('createTxt').click()
 
# Click on Download Button
element=driver.find_element(id,'Mathematics Olympiad Question Papers')
#.click()