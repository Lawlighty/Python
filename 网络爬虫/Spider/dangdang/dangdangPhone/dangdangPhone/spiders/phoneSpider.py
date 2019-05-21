# -*- coding: utf-8 -*-
import scrapy
from dangdangPhone.items import DangdangphoneItem
import time

class PhonespiderSpider(scrapy.Spider):
    name = 'phoneSpider'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['http://search.dangdang.com/?key=%BB%AA%CE%AA%CA%D6%BB%FA&act=input']

    def parse(self, response):
        # pass
        myItems = DangdangphoneItem()

        lis = response.xpath('//*[@id="component_59"]/li')

        for li in lis:
            name = li.xpath('.//a[@class="pic"]/@title').extract_first()
            goodsUrl = li.xpath('.//a[@class="pic"]/@href').extract_first()
            pdesc = li.xpath('.//p[@class="search_hot_word"]/text()').extract_first()
            store = li.xpath('.//p[@class="link"]/a/text()').extract_first()
            storeUrl = li.xpath('.//p[@class="link"]/a/@href').extract_first()

            if pdesc is None:
                pdesc ='暂无'

            myItems['name'] = name
            myItems['goodsUrl']= goodsUrl
            myItems['pdesc'] = pdesc
            myItems['store'] = store
            myItems['storeUrl'] = storeUrl

            yield myItems

        for i in range(2,5):
            url = 'http://search.dangdang.com/?key=%BB%AA%CE%AA%CA%D6%BB%FA&act=input&page_index={}'.format(i)
            if url:
                time.sleep(3)
                yield scrapy.Request(url, callback=self.parse)
