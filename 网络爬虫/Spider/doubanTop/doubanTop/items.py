# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubantopItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #标题, 连接, 评分, 引述
    title = scrapy.Field()
    href = scrapy.Field()
    rating_num = scrapy.Field()
    quote = scrapy.Field()

    pass
