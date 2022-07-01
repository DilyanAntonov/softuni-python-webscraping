import scrapy


class TrainersSpider(scrapy.Spider):
    name = 'trainers'

    allowed_domains = ['softuni.bg']
    start_urls = ['https://softuni.bg/trainers']

    def parse(self, response):
        for trainer in response.css('article.trainers-page-content-trainer-info'):

            id = trainer.css('.trainers-page-content-trainer-info::attr(data-id)').get()

            yield {
                'name': trainer.css('.trainers-page-content-trainer-name::text').get(),
                'position': trainer.css('.trainers-page-content-trainer-occupation::text').get(),
                'info': trainer.css(f'#{id} .trainings-page-content-trainer-info-modal-description::text').get()
            }
