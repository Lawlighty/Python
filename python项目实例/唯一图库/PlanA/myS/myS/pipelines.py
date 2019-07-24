# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests

class MysPipeline(object):
    def process_item(self, item, spider):
        detailURL = item['detailURL']
        path = item['path']
        fileName = item['fileName']

        image = requests.get(detailURL)
        with open(path, 'wb') as f:
            f.write(image.content)

        print('正在保存图片:{}  路径:{} 文件名:{}'.format(detailURL, path, fileName))
        return item
