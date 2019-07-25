# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
import os
class MysPipeline(object):
    def process_item(self, item, spider):
        detailURL = item['detailURL']
        # path = item['path']
        path = str(detailURL).split('/')[-1]
        fileName = item['fileName']

        image = requests.get(detailURL)
        if not os.path.exists(fileName):
            os.makedirs(fileName)

        with open(str(fileName+'/'+path), 'wb') as f:
            f.write(image.content)

        print('正在保存图片:{}  路径:{} 文件名:{}'.format(detailURL, path, fileName))
        return item
