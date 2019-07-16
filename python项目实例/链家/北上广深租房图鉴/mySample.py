import pymongo
import requests
from info import rent_type,city_info
from lxml import etree
import time
import random
import re
import sys
sys.path.append(r'C:\Users\Administrator\Desktop\python\Py_webSpider\github\IP_pond\Improve')
from getProxy import get_proxies

class MyRent(object):

    def __init__(self):
        self.client = pymongo.MongoClient(host='localhost',port=27017)
        self.db = self.client['lianjiazufang']

    def intoMango(self, coll, info):
        collect = self.db[coll]
        collect.insert_one(info)

    def closeMongo(self):
        self.client.close()

    def getHtmlText(self, url):
        """
        获得url网页响应数据
        :param url:
        :return: text内容
        """
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400',
            'Origin': 'https://lianjia.com',
        }
        proxies = get_proxies()
        try:
            r = requests.get(url, headers=headers, proxies=proxies, timeout=10)
            r.raise_for_status()
            return r.text

        except Exception as e:
            print(e)

    def parser_text(self, text):
        """
        解析网页页面
        :param text:
        :return:
        """
        doc = etree.HTML(str(text))
        if doc.xpath('//*[@class="content__empty"]'):
            return None
        divs = doc.xpath('//div[@class="content__list"]/div')
        for div in divs:
            title = ''.join(div.xpath('.//p[@class="content__list--item--title twoline"]//text()')).replace('\n','').replace(' ','')
            location =  '-'.join(div.xpath('.//p[@class="content__list--item--des"]/a/text()'))
            area = div.xpath('.//p[@class="content__list--item--des"]/text()')[3].replace('\n','').replace(' ','')
            face = div.xpath('.//p[@class="content__list--item--des"]/text()')[4].replace('\n','').replace(' ','')
            layout = str(div.xpath('.//p[@class="content__list--item--des"]/text()')[5].replace('\n','').replace(' ',''))
            layout = re.sub('[室厅卫]','###',layout).split('###')
            room = layout[0] if 0<=len(layout)-1 else 0
            hall = layout[1] if 1<=len(layout)-1 else 0
            toilet = layout[2] if 2<=len(layout)-1 else 0
            price = "".join(div.xpath('.//span[@class="content__list--item-price"]//text()'))
            yield {
                '标题':title,
                '位置':location,
                '面积':area,
                '面向':face,
                '室':room,
                '厅':hall,
                '卫':toilet,
                '价格':price
            }


    def getInfo(self):
        for type, type_code in rent_type.items():
            for city, city_areas in city_info.items():
                for k,v in city_areas:
                    num = 1
                    while True:
                        url = 'https://{}.lianjia.com/zufang/{}/pg{}{}/#contentList'.format(city, v, num, type_code)
                        try:
                            text = self.getHtmlText(url)

                            info = self.parser_text(text)
                        except  Exception as e:
                            print(e)
                            break
                        if info:
                            for i in info:
                                try:
                                    self.intoMango(city, i)
                                    print('{}市 {}区 {}房  第{}页插入MongoDB成功'.format(city, k, type, num))
                                    time.sleep(random.randint(2,4))
                                except:
                                    print('{}市 {}区 {}房  第{}页插入MongoDB失败了'.format(city, k, type, num))
                                    time.sleep(random.randint(2, 4))
                        else:
                            print('{}市 {}区 {}房  第{}页数据不存在了'.format(city, k, type, num))
                            break
                        num += 1

        self.closeMongo()
        print('数据库关闭')

if __name__ == '__main__':
    Rent = MyRent()
    Rent.getInfo()
