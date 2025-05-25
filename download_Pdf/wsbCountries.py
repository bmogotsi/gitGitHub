import scrapy


class WsbcountriesSpider(scrapy.Spider):
    name = "wsbCountries"
    allowed_domains = ["s"]
    start_urls = ["https://s"]

    def parse(self, response):
        pass
