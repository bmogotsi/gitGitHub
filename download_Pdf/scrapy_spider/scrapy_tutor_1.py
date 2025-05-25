import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/tag/humor/",
    ]
    #                 "author2": quote.css("span/small.author::author").get(),
    #"text2": quote.xpath("span.text()").get(),
    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "author": quote.xpath("span/small/text()").get(),
                "text": quote.css("span.text::text").get(),
                "author2": quote.xpath("span/small/text()").get(),
                "author2Css": quote.css("span.small.author::text").get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)