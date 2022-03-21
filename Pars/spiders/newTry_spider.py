import scrapy
from Pars.items import Page


class NewtrySpiderSpider(scrapy.Spider):
    name = 'newTry_spider'
    allowed_domains = ['www.vl.ru']
    start_urls = ['http://www.vl.ru/travel']

    def parse(self, response):
        item = Page()
        item['page_url'] = response.url
        item['base_list'] = (response.xpath("//h4/a/text()").getall(), response.xpath("//h4/a/@href").getall())

        next = response.xpath("//a[contains(., 'следующая >')]")
        if next is not None:
           yield response.follow(next.attrib['href'],callback=self.parse)

        return item

