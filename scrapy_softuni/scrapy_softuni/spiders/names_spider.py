import scrapy


class TrainersSpider(scrapy.Spider):
    name = 'names'

    allowed_domains = ['softuni.bg']
    start_urls = ['https://softuni.bg/trainers']

    def parse(self, response):
        for trainer in response.css('article.trainers-page-content-trainer-info'):

            yield {
                'name': trainer.css('.trainers-page-content-trainer-name::text').get(),
            }
