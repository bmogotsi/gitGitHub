# https://scrapeops.io/web-scraping-playbook/403-forbidden-error-web-scraping/
import requests

try:
    HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
    # r = requests.get('http://httpbin.org/headers')
    r = requests.get('https://www.samf.ac.za/content/files/QuestionPapers/', )
    print(r.text)
except Exception as e:
    print("Exception...:" + str(r.text) + '\n' +str(e))