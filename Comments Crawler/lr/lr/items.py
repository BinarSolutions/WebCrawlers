# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class LrItem(scrapy.Item):
    name = Field()
    ip = Field()
    date = Field()
    time = Field()
    vote_up = Field()
    vote_down = Field()
    comment = Field()
