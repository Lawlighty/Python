# -*- coding: utf-8 -*-
import pymysql

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DemoPipeline(object):
    def __init__(self):
        """
        初始化,建立数据库连接
        """
        self.conn = pymysql.connect('localhost','root','rootroot','pythonsql')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert ignore into Scrape(text,author,tags) values("{}","{}","{}")'.format(item['text'],item['author'],item['tags'])
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

