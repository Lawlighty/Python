# -*- coding: utf-8 -*-
import scrapy
from doubanTop.items import DoubantopItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    # allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        # print(response.body)
        dItem = DoubantopItem()
        selector = scrapy.Selector(response)
        items = selector.xpath('//div[@class="item"]')
        for item in items:
            title = item.xpath('.//div[@class="hd"]/a/span[@class="title"]/text()')[0].get()
            href = item.xpath('.//div[@class="pic"]/a/@href').get()
            rating_num = item.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').get()
            quote = item.xpath('.//p[@class="quote"]/span/text()').get()

            dItem = DoubantopItem(title=title, href=href, rating_num=rating_num, quote=quote)
            # dItem['title'] = title
            # dItem['href'] = href
            # dItem['rating_num'] = rating_num
            # dItem['quote'] = quote
            yield dItem

        next_url = response.xpath("//span[@class='next']/a/@href").get()
        # next_url = response.xpath('//span[@class="next"]/a/@href')
        if not next_url:
            return
        else:
            new_url = 'https://movie.douban.com/top250'+next_url
            yield scrapy.Request(new_url, callback=self.parse)

