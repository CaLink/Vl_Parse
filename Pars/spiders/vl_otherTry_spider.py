import scrapy
import json
from json import JSONEncoder


class Page:
    def __init__(self, name):
        self.namePage = name
        self.places = []

class Base:
    def __init__(self,name,url):
        self.name = name
        self.url = url
        
class PageEncoder(JSONEncoder):
    def default(self,o):
        return o.__dict__
    



class VlOtherSpider(scrapy.Spider):
    name = "VLother"
    domain = "vl.ru"

    PageList = ["SAS"]
    
    def start_requests(self):
        urls = ['https://www.vl.ru/travel?page=1']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

        
        # Я не понимаю, почему тут данных нет, но в методе parse они есть в PageList
        # Хотя это должны быть одни и те же данные.
        #with open('data.json','w') as f:
            #f.write(json.dumps(self.PageList,sort_keys=True,indent=4,cls=PageEncoder))
            #f.write(self.PageList[0].places[0].name)

        #Кажется, он завершает этот метод раньше, чем выпооняет parse()

    def parse(self, response):
        
        #with open('data.html','wb') as f:
        #    f.write(response.body)

        
        page = Page(response.url)

        
        for tag in response.xpath('//h4/a'):
            page.places.append(Base(tag.xpath('text()').get(),tag.attrib['href']))



        self.PageList.append(page)

#        with open('data.json','w') as f:
#           f.write(json.dumps(self.PageList,sort_keys=True,indent=4,cls=PageEncoder))

        next = response.xpath("//a[contains(., 'следующая >')]")
        if next is not None:
           yield response.follow(next.attrib['href'],callback=self.parse)
        else:
            with open('data.json','w') as f:
                f.write(json.dumps(self.PageList,sort_keys=True,indent=4,cls=PageEncoder))
            
