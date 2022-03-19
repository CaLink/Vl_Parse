import scrapy
import json


class Page:
    def __init__(self, name):
        self.namePage = name
        self.places = []

class Base:
    def __init__(self,name,url):
        self.name = name
        self.url = url
        
    
    



class VlOtherSpider(scrapy.Spider):
    name = "VLother"
    domain = "vl.ru"

    PageList = []
    
    def start_requests(self):
        urls = ['https://www.vl.ru/travel?page=1']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

        with open('data.json','w') as f:
            (json.dump(self.PageList,sort_keys=True,indent=4))

        

    def parse(self, response):
        
        #with open('data.html','wb') as f:
        #    f.write(response.body)

        
        page = Page(response.url)

        
        for tag in response.xpath('//h4/a'):
            page.places.append(Base(tag.xpath('text()').get(),tag.attrib['href']))
            

        self.PageList.append(page)

        #next = response.xpath("//a[contains(., 'следующая >')]")
        #if next is not None:
        #   yield response.follow(next.attrib['href'],callback=self.parse)
