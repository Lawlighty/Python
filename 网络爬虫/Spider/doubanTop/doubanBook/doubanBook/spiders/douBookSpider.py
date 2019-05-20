# -*- coding: utf-8 -*-
import scrapy
import re
from doubanBook.items import DoubanbookItem

class DoubookspiderSpider(scrapy.Spider):
    name = 'douBookSpider'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://book.douban.com/top250']

    def parse(self, response):
        bookItem = DoubanbookItem()

        selector = scrapy.Selector(response)
        tables = selector.xpath('//div[@id="content"]//div[@class="indent"]//table')

        for table in tables:
            title = str(table.xpath('.//tr[@class="item"]/td[2]/div/a/text()').extract_first()).strip()
            author = str(table.xpath('.//tr[@class="item"]/td[2]/p[1]/text()').extract_first().split('/')[0])
            rating_nums = float(table.xpath('.//span[@class="rating_nums"]/text()').extract_first())
            href = str(table.xpath('.//tr[@class="item"]/td[2]/div/a/@href').extract_first())

            mark = str(table.xpath('.//p[@class="quote"]/span/text()').extract_first())


            bookItem['title'] = title
            bookItem['author'] = author
            bookItem['rating_nums'] = rating_nums
            bookItem['href'] = href
            bookItem['mark'] = mark

            yield bookItem

        next_url = response.xpath('//*[@id="content"]/div/div[1]/div/div/span[3]/a/@href').extract_first()
        if next_url:
            yield scrapy.Request(next_url, callback=self.parse)
        else:
            return

