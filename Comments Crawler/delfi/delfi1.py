#
#  Items - author, dateip, post
#
# start URL http://www.delfi.lt/news/ringas/lit/a-uzkalnis-emigravai-ir-gerai-durniau.d?id=68330862&com=1&reg=0&no=0&s=2 

from scrapy import Spider
from scrapy.selector import Selector

from delfi.items import DelfiItem


class DelfiSpider(Spider):
    name = "delfi"
    allowed_domains = ["www.delfi.lt"]
    start_urls = [
        "http://www.delfi.lt/news/ringas/lit/a-uzkalnis-emigravai-ir-gerai-durniau.d?id=68330862&com=1&reg=0&no=0&s=2",
    ]

    def parse(self, response):
        comments = Selector(response).xpath('//*[@id="comments-list"]/*')
        for comment in comments:
            item = DelfiItem()
            if comment.extract().strip()[0:14] == '<div data-post':
                if '</a>' in comment.xpath('div[@class="comment-author"]').extract()[0].strip():
                    item['author'] = comment.xpath(
                        'div[@class="comment-author"]/a/text()').extract()[0].strip()
                else:
                    item['author'] = comment.xpath(
                        'div[@class="comment-author"]/text()').extract()[0].strip()
                item['date'] = comment.xpath(
                    'div[@class="comment-date"]/text()').extract()[0].strip().split()[0] 
                item['time'] = comment.xpath(
                    'div[@class="comment-date"]/text()').extract()[0].strip().split()[1] 
                item['ip'] = comment.xpath(
                    'div[@class="comment-date"]/text()').extract()[0].strip().split()[3]
                item['post'] = comment.xpath(
                    'div[@class="comment-content"]/div[@class="comment-content-inner"]/text()').extract()[0].strip()
            elif comment0.extract().strip()[0:14] == '<ul class="com':
                if '</a>' in comment.xpath('div/div[@class="comment-author"]').extract()[0].strip():
                    item['author'] = comment.xpath(
                        'div/div[@class="comment-author"]/a/text()').extract()[0].strip()
                else:
                    item['author'] = comment.xpath(
                        'div/div[@class="comment-author"]/text()').extract()[0].strip()
                item['date'] = comment.xpath(
                    'div/div[@class="comment-date"]/text()').extract()[0].strip().split()[0] 
                item['time'] = comment.xpath(
                    'div/div[@class="comment-date"]/text()').extract()[0].strip().split()[1]
                item['ip'] = comment.xpath(
                    'div/div[@class="comment-date"]/text()').extract()[0].strip().split()[3]
                item['post'] = comment.xpath(
                    'div/div[@class="comment-content"]/div[@class="comment-content-inner"]/text()').extract()[0].strip()
            else:
                item['author'] = 'error'
                item['date'] = 'error'
                item['time'] = 'error'
                item['ip'] = 'error'
                item['post'] = 'error'
            yield item