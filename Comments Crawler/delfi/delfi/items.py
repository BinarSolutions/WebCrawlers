# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
#
#  Items - author, dateip, post
#

import scrapy
from scrapy.item import Item, Field

class DelfiItem(scrapy.Item):
    author = Field()
    date = Field()
    time = Field()
    ip = Field()
    post = Field()