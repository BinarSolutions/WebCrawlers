# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

import sys
if "C:\\Python27" not in sys.path:
    sys.path.append("C:\\Python27")


class RedditItem(Item):
    author = Field()
    time = Field()
    comment = Field()
