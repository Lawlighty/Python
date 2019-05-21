# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboweatherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    city = scrapy.Field()
    date = scrapy.Field()
    temp = scrapy.Field()
    desc = scrapy.Field()
