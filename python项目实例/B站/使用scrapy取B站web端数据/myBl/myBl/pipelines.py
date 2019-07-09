# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import openpyxl
import os
import csv

class MyblPipeline(object):
    def __init__(self):
        # csv文件的位置,无需事先创建
        self.store_file = os.path.dirname(__file__) + '/spiders/bibl.csv'
        self.file = open(self.store_file, 'a+', encoding='utf-8', newline='')
        self.writer = csv.writer(self.file)

    def process_item(self, item, spider):
        if item['title']:
            self.writer.writerow([item['title'], item['pic_url'], item['amount_of_play'], item['uper'], item['timeUp']])
        return item

    def close_spider(self, spider):
        self.file.close()