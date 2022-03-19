import scrapy

class VlSpider(scrapy.Spider):
    name = "VL"
    domain = "vl.ru"

    def start_requests(self):

        urls = ['https://www.vl.ru/travel?page=1']


        

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self,response):
    
    #   for tag in response.xpath('//h4/a'):
    #      yield {'name': tag.xpath('text()').get(), 'href':tag.attrib['href']}

    
    #    for tag in response.xpath('//h4'):
    #        yield {'name': tag.xpath('a/text()').get(), 'href':tag.xpath('a').attrib['href']}


    #   Нужно уставить FEED_EXPORT_ENCODING = 'utf-8' в settings.py
        for tag in response.css('h4>a'):
            yield {'name':tag.css('::text').get(), 'href': self.domain + tag.attrib['href']}

    #   Настройки в settings.py
        #sleep(3);

    
        next = response.xpath("//a[contains(., 'следующая >')]")
        if next is not None:
            yield response.follow(next.attrib['href'],callback=self.parse)
        
