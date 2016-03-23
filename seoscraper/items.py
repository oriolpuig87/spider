# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class UrlscraperItem(scrapy.Item):
    url = scrapy.Field()
    status = scrapy.Field()
    referer = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    pass

class PdfscraperItem(scrapy.Item):
    url = scrapy.Field()
    referer = scrapy.Field()
    title = scrapy.Field()
    pass
