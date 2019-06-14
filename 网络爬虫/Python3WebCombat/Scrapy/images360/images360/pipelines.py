# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.pipelines.images import ImagesPipeline #下载图片专用pipeline
from scrapy.exceptions import DropItem
from scrapy import Request
import os
import requests
from images360 import settings

class Images360Pipeline(object):
    def __init__(self):
        self.conn = pymysql.connect('localhost', 'root', 'rootroot', 'pythonsql')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # return item
        sql = 'insert ignore into images360(id,url,title,thumb_url) values("{}","{}","{}","{}")'.format(item['id'],item['url'],item['title'],item['thumb'])
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

class Images360PicPipeline(ImagesPipeline):
    """
    继承内置ImagesPipeline
    重写方法
    """

    # 这个方法是在图片将要被存储的时候调用，来获取这个图片存储的路径
    def file_path(self, request, response=None, info=None):
        url = request.url
        file_name = url.split('/')[-1]
        return file_name
        # file_name = request.item.get('id')+'.jpg'
        # # pic_path = "{}/{}".format(settings.IMAGES_STORE,file_name)
        # return file_name

    # 这个方法是在发送下载请求之前调用
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            # 下载失败忽略该 Item 的后续处理 即不保存在数据库
            raise DropItem('Image Downloaded Failed')
        return item

    def get_media_requests(self, item, info):
        yield Request(item['url'])

