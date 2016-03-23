# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from seoscraper.items import PdfscraperItem

class PdfSpider(CrawlSpider):
    name = "pdf"
    allowed_domains = ["example.com"]
    start_urls = (
        'http://www.example.com/index.aspx',
        'http://www.example.com/en/index.php'
    )

    rules = (
        Rule(LinkExtractor(allow=('')), callback="parse_items", follow=True),
    )

    def parse_items(self, response):
        for link in response.xpath('//a'):
            item = PdfscraperItem()
            item["url"] = link.xpath("@href").extract()
            item["referer"] = response.url
            item["title"] = link.xpath("text()").extract()
            if "pdf" in ''.join(item["url"]):
                yield item
