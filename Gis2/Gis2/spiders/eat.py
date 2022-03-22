import scrapy


class EatSpider(scrapy.Spider):
    name = 'eat'
    allowed_domains = ['2gis.ru']

    page = 1
    
    def start_requests(self):
        
        urls = [f'http://2gis.ru/vladivostok/search/Поесть/page/{self.page}']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):

        # Получаем данные со страницы
        for tag in response.xpath('//div[@class="_1h3cgic"]/a'):
            yield {'name':tag.xpath('span/text()').get(),'href':tag.attrib['href']}

        #Переход по страницам

        ur = f'http://2gis.ru/vladivostok/search/Поесть/page/{self.page}'

        #Temp
        while(True):
            self.page+=1
            yield response.follow(ur)


        

        