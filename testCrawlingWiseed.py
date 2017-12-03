import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.wiseed.com/fr/projets-en-financement',
    ]

    def parse(self, response):
        for link in response.css('body div.list-cards div.project-card'):
            yield {
                'Nom de projet': link.css('span.project-name ::text').extract_first(),
                'Image du projet': link.css('div.project-thumbnail::attr(style)').re_first(r'background-image: url\(\'\s*(.*)\'\)'),
                'Description courte du projet': link.css('p.description-courte ::text').extract_first(),
                'Statut de la collecte': link.css('div.key-data li strong.text-on-one-line ::text').extract(),
                'Montant recherche': link.css('div.key-data li:nth-child(2) strong ::text').extract_first(),
                'Nombre de commentaires': link.css('div.key-data li:nth-child(3) strong ::text').extract_first(),
                'Nombre d\'interesses': link.css('div.key-data li:nth-child(4) strong ::text').extract_first()
                }