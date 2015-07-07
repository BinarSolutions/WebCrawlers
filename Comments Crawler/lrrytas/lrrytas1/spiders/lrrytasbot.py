from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from lrrytas.items import LrrytasItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class LrrytasSpider(Spider):
    name = "lrrytas"
    allowed_domains = ['http://www.lrytas.lt/']
    start_urls = ["http://www.lrytas.lt/?id=14355922181434706286&view=6"]
    rules = (
       Rule(LinkExtractor(allow=r'Items'), callback='parse', follow=True),
	   Rule(LinkExtractor(restrict_xpaths=('//*[contains(@class, "str-pages-div")][1]/*')), callback='parse_comments_follow_next_page', follow=True)
)
    def parse(self, response):
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
    
    def parse_comments_follow_next_page(self, response):
        next_page = xpath('//*[contains(text(), "Kitas >>") and contains(@href, "id")]/@href')
        if next_page:
            url = response.urljoin(next_page.extract())
            yield Request(url, self.parse)