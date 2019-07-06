import requests
from lxml import etree
import pymysql
import time
import random
import pymongo
import sys
sys.path.append(r'C:\Users\Administrator\Desktop\python\Py_webSpider\github\IP_pond\Improve')
from getProxy import get_proxies



def getHtmlText(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400',
        'Referer':'https://search.bilibili.com/',
    }
    proxies = get_proxies()
    try:
        r = requests.get(url, headers=headers, proxies=proxies, timeout=10)
        r.raise_for_status()
        return r.text
    except Exception as e:
        print(e)

def getInfo(text):
    if text:
        doc = etree.HTML(str(text))
        lis = doc.xpath('//ul[@class="video-contain clearfix"]/li')
        for li in lis:
            title = li.xpath('./a/@title')[0]
            pic_url = 'https'+ li.xpath('./a/@href')[0]
            amount_of_play = str(li.xpath('.//div[@class="tags"]/span[@title="观看"]/text()')[0]).replace('\n','').replace(' ',"")
            uper = li.xpath('.//span[@title="up主"]/a/text()')[0]
            timeUp = str(li.xpath('.//div[@class="tags"]/span[@title="上传时间"]/text()')[0]).replace('\n','').replace(' ',"")
            yield {
                'title':title,
                'pic_url':pic_url,
                'amount_of_play':amount_of_play,
                'uper':uper,
                'timeUp':timeUp,
            }

    else:
        print('Nothing')

def conn_db():
    try:
        print('连接数据库')
        db = pymysql.connect('localhost','root','rootroot','bilibili')
        cursor = db.cursor()
        return db,cursor
    except:
        print("连接数据库失败")

def op_db(db,cursor, dic):
    sql = 'insert into zuoye4(title, pic_url, amount_of_play, uper, timeUp) values("{}","{}","{}","{}","{}")'\
        .format(dic['title'], dic['pic_url'], dic['amount_of_play'], dic['uper'], dic['timeUp'])
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print('发生错误')
        db.rollback()

def close_db(db):
    print('关闭数据库')
    db.close()


def conn_Mongo():
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['bilibili']
    return client, db

def op_Mongo(db, info):
    try:
        if db['zuoye4'].insert_one(info):
            print('数据插入MongoDB')
        else:
            print('挠头')
    except Exception as e:
        print(e)
def close_MongoDB(client):
    client.close()
    print('Mongo关闭')

def main():
    # db,cursor = conn_db()
    client, db = conn_Mongo()
    for i in range(1,3):
        url = 'https://search.bilibili.com/all?keyword=python&page={}'.format(i)
        text = getHtmlText(url)
        for info in getInfo(text):
            op_Mongo(db, info)
        time.sleep(random.randint(3,5))
    # close_db(db)
    close_MongoDB(client)

if __name__ == '__main__':
   main()