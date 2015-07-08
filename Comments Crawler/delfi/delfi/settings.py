# -*- coding: utf-8 -*-

# Scrapy settings for delfi project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
DOWNLOAD_DELAY = 10

BOT_NAME = 'delfi'

SPIDER_MODULES = ['delfi.spiders']
NEWSPIDER_MODULE = 'delfi.spiders'

ITEM_PIPELINES = ['delfi.pipelines.MongoDBPipeline', ]

MONGODB_SERVER = "213.197.167.222"
MONGODB_PORT = 27317
MONGODB_DB = "SPYDERS"
MONGODB_COLLECTION = "Delfi_2"



# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'delfi (+http://www.binarlabs.lt)'
