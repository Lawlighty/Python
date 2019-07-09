# -*- coding: utf-8 -*-
import scrapy
from myBl.items import MyblItem

class BbbSpider(scrapy.Spider):
    name = 'bbb'
    # allowed_domains = ['bibi.com']
    start_urls = ['https://search.bilibili.com/all?keyword=python&page=1']

    def parse(self, response):
        # pass
        myitem = MyblItem()
        lis = response.xpath('//ul[@class="video-contain clearfix"]/li')
        for li in lis:
            myitem['title'] =  li.xpath('./a/@title').extract_first()
            myitem['pic_url'] =  'https'+ li.xpath('./a/@href').extract_first()
            myitem['amount_of_play'] =  str(li.xpath('.//div[@class="tags"]/span[@title="观看"]/text()').extract_first()).replace('\n','').replace(' ',"")
            myitem['uper'] = li.xpath('.//span[@title="up主"]/a/text()').extract_first()
            myitem['timeUp'] = str(li.xpath('.//div[@class="tags"]/span[@title="上传时间"]/text()').extract_first()).replace('\n','').replace(' ',"")

            yield myitem

        for i in range(2,5):
            next_url = "https://search.bilibili.com/all?keyword=python&page={}".format(i)
            yield scrapy.Request(url=next_url, callback=self.parse)