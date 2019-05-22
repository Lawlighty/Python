# -*- coding: utf-8 -*-
import os
import requests
from meiziPic import settings

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MeizipicPipeline(object):
    def process_item(self, item, spider):
        # return item
        dir_path = '%s/%s' % (settings.IMAGES_STORE, spider.name)
        print('dir_path:',dir_path)

        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

        for img_url in item['img_urls']:
            myurl = img_url
            print('myurlllllllll',myurl)
            pic_name = myurl.split('/')[-1]
            file_path = '%s/%s'%(dir_path, pic_name)

            if os.path.exists(file_path):
                continue
            with open(file_path, 'wb')as f:
                headers={
                    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3505.400',
                    'referer':'http://www.baidu.com'
                }
                resp = requests.get(img_url, headers=headers)
                f.write(resp.content)

        return item