# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
 from noticias.items import NoticiasItem

class GloboSpider(scrapy.Spider):
    name = 'Globo'
    allowed_domains = ['globo.com']
    start_urls = ['http://www.globo.com/']

    def parse(self, response):
        #pass
    for article in response.css("article"):
        link    = article.css("div.texts h2 a::attr(href)").extract_first()
         yield response.follow(link, self.parse_article)
         
         def parse_article(self, response):
                
        link   = response.url
          title  = response.css("title ::text").extract_first()
              author = response.css("span.author ::text").extract_first()
                  text   =  "".join(response.css("div.entry ::text").extract())
        #yield {'link': link, 'title': title, 'author': author}
        
         notice = NoticiasItem(title=title, author=author, link=link)
        yield notice
        
        
       