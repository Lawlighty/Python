# -*- coding: utf-8 -*-
import scrapy
from demo.items import DemoItem
from urllib.parse import urljoin

class DemospiderSpider(scrapy.Spider):
    name = 'demoSpider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            ditem = DemoItem()
            text = quote.xpath('./span[1]/text()').extract_first()
            author = quote.xpath('.//small[@class="author"]/text()').extract_first()
            tags = quote.xpath('.//div[@class="tags"]/a/text()').extract()
            ditem['text'] = text
            ditem['author'] = author
            ditem['tags'] = tags
            yield ditem

        if response.xpath('//ul[@class="pager"]/li/a/@href').extract_first():
            next_url = response.xpath('//ul[@class="pager"]/li/a/@href').extract_first()
            # print('nexxxxxxxx_url',next_url)
            # url = 'http://quotes.toscrape.com/page/2/'

            url = urljoin(response.url,next_url)
            yield scrapy.Request(url=url, callback=self.parse)

