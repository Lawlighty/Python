# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyblItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    title = scrapy.Field()
    pic_url = scrapy.Field()
    amount_of_play = scrapy.Field()
    uper = scrapy.Field()
    timeUp = scrapy.Field()
