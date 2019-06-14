# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode
from scrapy import Request
from images360.items import Images360Item
import json

class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    start_urls = ['http://images.so.com/']

    def start_requests(self):
        base_url = 'https://image.so.com/zjl?'
        #url 参数
        data = {
            'ch':'beauty',
            'listtype':'new',
            'temp':1,
        }
        for i in range(1,self.settings.get('MAX_PAGE') + 1):#页数
            data['sn'] = i*30               #每页的图片数量
            params = urlencode(data)           #参数转化
            url = base_url+params
            yield Request(url, self.parse)

    def parse(self, response):
        result = json.loads(response.text)
        lists = result.get('list')
        for list in lists:
            myitem = Images360Item()
            myitem['id'] = list.get('id')
            myitem['url'] = list.get('qhimg_url')
            myitem['title'] = list.get('title')
            myitem['thumb'] = list.get('qhimg_thumb')
            yield myitem


