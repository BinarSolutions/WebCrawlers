# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from lrrytas.items import LrrytasItem


class LrrytasbotCrawlerSpider(CrawlSpider):
    name = 'lrrytasbot_crawler'
    allowed_domains = ['http://www.lrytas.lt/']
    start_urls = ['http://www.lrytas.lt/?id=14355922181434706286&view=6']

    rules = (
        Rule(LinkExtractor(allow=r'/?id=14355922181434706286&view=6&p=2'), callback="parse_lel"),
    )

    def parse_lel(self, response):
     sel = Selector(response)
     site = sel.xpath('//*[@class="comment"]/*')
     node = sel.xpath('//*[@class="comments"]/*')

     for i in range(0, len(site), 2):
       item = LrrytasItem()
       item['name'] = node[i].xpath('*/div[contains(@class, "comment-nr")]/text()').extract()[0]
       item['ip'] = node[i].xpath('*/*/div[contains(@class, "comment-ip")]/text()').extract()[0]
       item['time'] = node[i].xpath('*/*/div[contains(@class, "comment-time")]/text()').extract()[0]
       item ['comment'] = site[i + 1].xpath('descendant-or-self::text()').extract()[0]
       yield item
