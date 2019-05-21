# -*- coding: utf-8 -*-
import scrapy
from weiboWeather.items import WeiboweatherItem

class WeatherspiderSpider(scrapy.Spider):
    name = 'weatherSpider'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['http://weather.sina.com.cn/']

    def parse(self, response):
        # pass
        myItems = WeiboweatherItem()

        city = str(response.xpath('//*[@id="slider_ct_name"]/text()').extract())

        infos = response.xpath('//*[@id="blk_fc_c0_scroll"]//div[@class="blk_fc_c0_i"]')

        for info in infos:
            date = str(info.xpath('.//p[1]/text()').extract())
            temp = str(info.xpath('.//p[@class="wt_fc_c0_i_temp"]/text()').extract())
            desc = str(info.xpath('.//p[@class="wt_fc_c0_i_tip"]/text()').extract())

            myItems['city'] = city
            myItems['date'] = date
            myItems['temp'] = temp
            myItems['desc'] = desc

            yield myItems
