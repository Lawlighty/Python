# -*- coding: utf-8 -*-
import scrapy
from myS.items import MysItem
import logging
import requests
from lxml import etree
import re

class MyspiderSpider(scrapy.Spider):
    name = 'mySpider'
    allowed_domains = ['www.mmonly.cc']
    # start_urls = ['http://www.baidu.com/']
    base = r'F:\python项目实例\唯一图库\PlanA\myPics'
    def start_requests(self):
        for i in range(2,3):
            url = 'https://www.mmonly.cc/tag/xh1/{}.html'.format(i)
            yield scrapy.Request(url=url, callback=self.parse)

    #获得每一页的图集
    def parse(self, response):
        atlas = response.xpath('//*[@id="infinite_scroll"]/div')
        for atla in atlas:
            myItem = MysItem()
            siteURL = atla.xpath('./div[1]/div/div[1]/a/@href').extract_first()
            title = atla.xpath('./div[1]/div/div[1]/a/img/@alt').extract_first()
            fileName = self.base+ "\\"+ title
            myItem['siteURL'] = siteURL
            myItem['title'] = title
            myItem['fileName'] = fileName

            yield scrapy.Request(url=myItem['siteURL'], meta={'item_parse':myItem}, callback=self.parse2)

    #解析每个图集
    def parse2(self, response):
        item_parse2 = response.meta['item_parse']
        htmltext = requests.get(response.url).text.encode('ISO-8859-1').decode('gbk').encode('utf8').decode('utf-8')
        # pattern = re.compile(r'<li><a>共(.*?)页</a>', re.S)
        pattern = re.compile(r'共(.*?)页', re.S)
        page_num = int(re.findall(pattern, htmltext)[0])
        for num in range(1,page_num+1):
            # item2 = MysItem()
            fileName = item_parse2['fileName']
            #保存图片名称
            path = fileName+'/'+str(num)+ '.jpg'
            #图片html页面
            pageURL = str(response.url)[:-5]+str(num)+'.html'

            item_parse2['fileName'] = fileName
            item_parse2['path'] = path
            item_parse2['pageURL'] = pageURL
            yield scrapy.Request(url=item_parse2['pageURL'], meta={'item_parse2':item_parse2}, callback=self.parse3)

    #解析每个图集中的图片
    def parse3(self, response):
        # item3 = MysItem()
        self.log("my log information")
        htmltext = requests.get(response.url).text.encode('ISO-8859-1').decode('gbk').encode('utf8').decode('utf-8')
        item_parse3 = response.meta['item_parse2']
        pattern = re.compile(r'<li class="pic-down h-pic-down"><a target="_blank" class="down-btn" href=\'(.*?)\'>.*?</a>', re.S)
        # detailURL = re.findall(pattern, htmltext)[0]
        detailURL = re.search(pattern, response.text).group(1)
        item_parse3['detailURL'] = detailURL
        yield item_parse3

