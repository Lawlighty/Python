# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyuniversalItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    title = scrapy.Field()  #标题
    content = scrapy.Field()#内容
    url = scrapy.Field()    #链接
    time = scrapy.Field()  #发布时间
    source = scrapy.Field()#来源
    website = scrapy.Field()#站点==中华网