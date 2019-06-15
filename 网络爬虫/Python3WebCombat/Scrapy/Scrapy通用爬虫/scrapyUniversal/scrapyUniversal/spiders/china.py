# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapyUniversal.items import ScrapyuniversalItem
import re

class ChinaSpider(CrawlSpider):
    name = 'china'
    allowed_domains = ['tech.china.com']
    # start_urls = ['http://tech.china.com/']
    start_urls = ['https://tech.china.com/articles/']# 科技-业界-列表 版面

    rules = (
        Rule(LinkExtractor(allow=r'/article\/.*\.html', restrict_xpaths='//div[@id="left_side"]//div[@class="con_item"]'), callback='parse_item',follow=False),
        Rule(LinkExtractor(restrict_xpaths='//div[@id="pageStyle"]//a[contains(text(),"下一页")]'), follow=True)
    )

    def parse_item(self, response):
        myitem = ScrapyuniversalItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
        myitem['title'] = response.xpath('//h1[@id="chan_newsTitle"]/text()').extract_first()
        myitem['content'] = ''.join(response.xpath('//div[@id="chan_newsDetail"]//text()').extract()).strip()
        myitem['url'] = response.url
        """
                       2019-06-14 15:53:28 &nbsp; &nbsp; &nbsp; 来源：财金网            """
        chan_newsInfo =''.join(response.xpath('//div[@id="chan_newsInfo"]/text()').extract())
        print('*'*20,chan_newsInfo)
        myitem['time'] = re.findall('(\d+-\d+-\d+\s\d+:\d+:\d+)',chan_newsInfo)[0]
        myitem['source'] = re.findall('来源：(.*)', chan_newsInfo)[0]
        # myitem['time'] = response.xpath('//div[@id="chan_newsInfo"]/text()').re_first('(\d+-\d+-\d+\s\d+:\d+:\d+)')
        # myitem['source'] = response.xpath('//div[@id="chan_newsInfo"]/text()').re_first('来源: (.*)').strip()
        myitem['website'] = '中华网'

        yield myitem
