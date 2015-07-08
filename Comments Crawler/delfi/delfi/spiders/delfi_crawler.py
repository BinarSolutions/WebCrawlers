# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector

from delfi.items import DelfiItem


class DelfiCrawlerSpider(CrawlSpider):
    name = 'delfi_crawler'
    allowed_domains = ['delfi.lt']
    start_urls = ['http://www.delfi.lt/news/ringas/abroad/m-garbaciauskaite-budriene-tikroji-rusijos-siela-visai-neromantiska.d?id=68404714&com=1&reg=0&s=2&no=60']

    rules = (
		Rule(LinkExtractor(allow=r'/?id=68404714&com=1&reg=0&s=2&no='), callback='parse_item'),
    )

    def parse_item(self, response):
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
            elif comment.extract().strip()[0:14] == '<ul class="com':
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
