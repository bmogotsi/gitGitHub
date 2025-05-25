# -*- coding: utf-8 -*-
import scrapy
import json

class NtschoolsSpider(scrapy.Spider):
    name = "ntschoolsTest"
    start_urls = ["https://directory.ntschools.net/#/schools"]
    hearders = {
        "Accept":            "application/json",
        "Accept-Encoding":   "gzip, deflate, br, zstd",
        "Accept-Language":   "en-US,en;q=0.9",
        "Cache-Control":     "no-cache",
        "Connection":        "keep-alive",
        "Host":              "directory.ntschools.net",
        "Pragma":            "no-cache",
        "Referer":           "https://directory.ntschools.net/",
        "Sec-Fetch-Dest":    "empty",
        "Sec-Fetch-Mode":    "cors",
        "Sec-Fetch-Site":    "same-origin",
        "User-Agent":        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
        "X-Requested-With":  "Fetch",
    }
    
        
    def parse(self, response):
        url = 'https://directory.ntschools.net/api/System/GetAllSchools'  
               
        request = scrapy.Request(url=url, 
                 callback=self.parse_api,
                 headers=self.hearders
                )
        yield request 
    
    def parse_api(self, response):
        #base_url = 'https://directory.ntschools.net/api/System/GetSchool?itSchoolCode=acacisch'
        base_url = 'https://directory.ntschools.net/api/System/GetSchool?itSchoolCode='
        
        # we do not use css or xpath
        # convert response to json because in the hearders @@@  "Accept":            "application/json",
        # 
        raw_data =response.body
        data = json.loads(raw_data)
        
        for school in data: # the data in XHR/Response/GetAllSchools is a List
            school_code = school['itSchoolCode']
            school_url = base_url+school_code
            request = scrapy.Request(school_url, callback=self.parse_school, headers=self.hearders) #json request need to pass headers
            yield request
            
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
        
