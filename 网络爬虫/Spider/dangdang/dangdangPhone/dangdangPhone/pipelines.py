# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DangdangphonePipeline(object):
    def process_item(self, item, spider):
        # return item
        with open('huaweiPhone.txt','a+') as f:
            f.write('宝贝名称:'+'\t'+item['name']+'\t'+'宝贝链接'+item['goodsUrl']+'\n')
            f.write('宝贝描述:'+'\t'+item['pdesc']+'\n')
            f.write('商铺名称:'+'\t'+item['store']+'商铺链接:'+item['storeUrl']+'\n\n\n')

    def close_spider(self,spider):
        print('爬取完成!')