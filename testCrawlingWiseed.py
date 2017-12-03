import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.wiseed.com/fr/projets-en-financement',
    ]

    def parse(self, response):
        for link in response.css('body div.list-cards div.project-card span.project-name'):
            yield {'Nom de projet ': link.css('span ::text').extract_first()}