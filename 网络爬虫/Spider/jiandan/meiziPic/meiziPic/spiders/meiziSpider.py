# -*- coding: utf-8 -*-
import scrapy
from meiziPic.items import MeizipicItem
import re
class MeizispiderSpider(scrapy.Spider):
    name = 'meiziSpider'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['http://jandan.net/ooxx']

    def parse(self, response):

        myItem = MeizipicItem()

        ols = response.xpath('//*[@id="comments"]/ol')
        for ol in ols:

            img_urls = ol.xpath('.//div[@class="text"]/p/img/@src').extract_first()

            img_urls = 'http:'+img_urls

            mylist = []
            mylist.append(img_urls)

            myItem['img_urls'] = mylist

            yield myItem

        next_url = response.xpath('//a[@class="previous-comment-page"]/@href').extract_first()

        if next_url:
            next_url = 'http:'+next_url

            yield scrapy.Request(next_url, callback=self.parse)
