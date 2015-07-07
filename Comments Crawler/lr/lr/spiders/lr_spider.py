from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from lr.items import LrItem

class LrrytasSpider(Spider):
    name = "lr"
    allowed_domains = ['http://www.lrytas.lt/']
    start_urls = ['http://www.lrytas.lt/?id=14355922181434706286&view=6&p=' + str(i) for i in range(1,11)]

    def parse(self, response):
        sites = Selector(response).xpath('//*[@class="comment"]/*')
				
        for i in range(0, len(sites), 2):
            item = LrItem()
            item['name'] = sites[i].xpath('div/text()').extract()[0]
            item['ip'] = sites[i].xpath('div/div/text()').extract()[1].split()[1]
            item['date'] = sites[i].xpath('div/div/text()').extract()[0].split()[0]
            item['time'] = sites[i].xpath('div/div/text()').extract()[0].split()[1]
            item['vote_up'] = sites[i].xpath('div/div/span/text()').extract()[0]
            item['vote_down'] = sites[i].xpath('div/div/span/text()').extract()[1]
            item['comment'] = sites[i + 1].xpath('text()').extract()[0]
            yield item