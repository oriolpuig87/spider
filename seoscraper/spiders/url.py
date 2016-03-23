# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from seoscraper.items import UrlscraperItem

class UrlSpider(CrawlSpider):
    name = "url"
    allowed_domains = ["example.com"]
    handle_httpstatus_list = [300, 301, 302, 303, 304, 305, 306, 307, 308, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 422, 426, 449, 451, 500, 501, 502, 503, 504, 505, 509]
    start_urls = (
        'http://www.example.com/index.aspx',
        'http://www.example.com/en/index.php'
    )

    rules = (
        Rule(LinkExtractor(allow=('')), callback="parse_items", follow=True),
    )

    def parse_items(self, response):
        item = UrlscraperItem()
        item['url'] = response.url
        item['status'] = response.status
        item['referer'] = response.request.headers.get('Referer', None)
        item['title'] = response.xpath('/html/head/title/text()').extract()
        item['description'] = response.xpath('/html/head/meta[@name="description"]/@content').extract()
        yield item
