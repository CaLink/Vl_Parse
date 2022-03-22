import scrapy


class EatSpider(scrapy.Spider):
    name = 'eat'
    allowed_domains = ['2gis.ru']
    start_urls = ['http://2gis.ru/vladivostok/search/Поесть/page/1']

    def parse(self, response):

        response.xpath("//*[contains(@class,'_12164l30')]").getall()

        pass
