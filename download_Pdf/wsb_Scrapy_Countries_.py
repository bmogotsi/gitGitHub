# -*- coding: utf-8 -*-
import scrapy
import json

class NtschoolsSpider(scrapy.Spider):
    name = "wsbCountries"
    start_urls = ["https://m.worldsportsbetting.co.za"]
    hearders = {   
        "Accept":           "application/json",
        "Accept-Encoding":  "gzip, deflate, br, zstd",
        "Accept-Language":  "en-US,en;q=0.9",
        "Cache-Control":    "no-cache",
        "Origin":           "https://m.worldsportsbetting.co.za",
        "Pragma":           "no-cache",
        "Referer":          "https://m.worldsportsbetting.co.za/",
        "Sec-Fetch-Dest":   "empty",
        "Sec-Fetch-Mode":   "cors",
        "Sec-Fetch-Site":   "same-site",
        "User-Agent":       "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
    }
    
        
    def parse(self, response):
        url = 'https://sport.api.worldsportsbetting.co.za/cats.php?sport=3781' 
               
        request = scrapy.Request(url=url, 
                 callback=self.parse_api,
                 headers=self.hearders
                )
        yield request 
    
    def parse_api(self, response):
        #base_url = 'https://directory.ntschools.net/api/System/GetSchool?itSchoolCode=acacisch'
        # base_url = 'https://directory.ntschools.net/api/System/GetSchool?itSchoolCode='
        
        # we do not use css or xpath
        # convert response to json because in the hearders @@@  "Accept":            "application/json",
        # 
        raw_data =response.body
        data = json.loads(raw_data)
        
        for country in data: # the data in XHR/Response/GetAllSchools is a List
            
            yield{
            'country_code':  country['CategoryId'],
            'country_name':  country['Description']
            }
            
    def parse_school(self, response):
        raw_data =response.body
        data = json.loads(raw_data)
        yield{
        'Name': data['name'],
        'PhysicalAddress': data['physicalAddress']['displayAddress'],
        'PostalalAddress': data['postalAddress']['displayAddress'],
        'Email': data['mail'],
        'Telephone': data['telephoneNumber'] 
        }
        
