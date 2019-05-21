# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WeiboweatherPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',user='root',password='rootroot',db='pythonsql',charset='utf8')
        self.cursor =self.conn.cursor()
        #如果表中存在数据则清空
        del_sql = 'delete from nbWeather'
        self.cursor.execute(del_sql)
        self.conn.commit()

    def process_item(self, item, spider):
        # return item

        sql = 'insert ignore into nbWeather(date,city,`desc`,`temp`) values("{}","{}","{}","{}")'.format(item["date"],item["city"],item["desc"],item["temp"])
        self.cursor.execute(sql)
        self.conn.commit()

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
