import scrapy
import json

class NtschoolsSpider(scrapy.Spider):
    name = "ntschools"
    allowed_domains = ["s"]
    start_urls = ["https://directory.ntschools.net/#/schools"]
    hearders = {
          "accept":               "application/json",
          "accept-encoding":      "gzip, deflate, br, zstd",
          "accept-language":      "en-US,en;q=0.9",
          "referer":              "https://directory.ntschools.net/",
          "sec-fetch-dest":       "empty",
          "sec-fetch-mode":       "cors",
          "sec-fetch-site":       "same-origin",
          "user-agent":           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36" 
    }
        

    def parse(self, response):
        url = 'https://directory.ntschools.net/api/System/GetAllSchools' #  (request url)
        
        request = scrapy.Request(url=url
                , callback=self.parse_api
                , headers=self.hearders)
    
    def parse_api(self, response):
        #base_url = 'https://directory.ntschools.net/api/System/GetSchool?itSchoolCode=acacisch'
        base_url = 'https://directory.ntschools.net/api/System/GetSchool?'
        raw_data =response.body
        data = json.loads(raw_data)
        for school in data:
            school_code = school['itschoolCode']
            school_url = base_url+school_code
            request = scrapy.Request(school_url, callback=self.parse_school, headers=self.hearders) #json request need to pass headers
            yield request
            
    def parse_school(self, response):
        raw_data =response.body
        data = json.loads(raw_data)
        yield{
        'name': data['name'],
        'physicalAddress': data['physicalAddress']['displayAddress'],
        'postalalAddress': data['postalAddress']['displayAddress'],
        'Email': data['mail'],
        'Telephone': data['telephoneNumber'] 
        }