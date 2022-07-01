import scrapy

class CoursesSpider(scrapy.Spider):
    name = "courses"

    allowed_domains = ['softuni.bg']
    start_urls = ['https://softuni.bg/trainings/opencourses?filterby=Courses&category=0']

    def parse(self, response):                
        for item_url in response.css("a.bolder.course-title::attr('href')"):
            url = response.urljoin(item_url.get())
            yield scrapy.Request(url=url, callback=self.parse_course)
        
        next_page = response.css('li.PagedList-skipToNext a::attr(href)').get()
        next_page = response.urljoin(next_page)

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
    
    
    def parse_course(self, response):
        course_name = response.css('h1.instance-header-title::text').get()
        trainer_name = response.css('p.instance-trainer-info-name::text').get()
        price = response.css('span.instance-details-label-price::text').get()
        lectures = response.css('span.lecture-title-name::text').getall()
        
        if not price:
            price = 'Безплатно'
        if not trainer_name:
            trainer_name = 'None'
        
        yield {
            'course_name': course_name.strip(),
            'trainer_name': trainer_name.strip(),
            'price': price.strip(),
            'lectures': lectures
        }
                        
            
