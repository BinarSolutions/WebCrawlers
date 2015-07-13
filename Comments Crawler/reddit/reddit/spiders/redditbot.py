from scrapy.spiders import Spider
from scrapy.selector import Selector
from reddit.items import RedditItem



class redditSpider(Spider):
    name = "reddit"
    allowed_domains = ['http:\\www.reddit.com']
    start_urls = ["http://www.reddit.com/r/pics/comments/3cr2u0/but_arent_they_already/?limit=500"]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath("//*[contains(concat(' ', normalize-space(@class), ' '), ' entry unvoted ')]")

        for sites in sites:
            item = RedditItem()
            try:
                item['author'] = sites.xpath("p[@class='tagline']/a[contains(concat(' ', normalize-space(@class), ' '), ' author ')]/text()").extract()[0]
                item['time'] = sites.xpath("p[@class='tagline']/time/@datetime").extract()[0]
                item['comment'] = sites.xpath("form/div/div[@class='md']/p/text()").extract()[0]
                yield item
            except IndexError:
                pass