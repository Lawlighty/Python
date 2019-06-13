import requests
from lxml import etree
import random
import re
import time
import pymysql
import execjs
import sys
sys.path.append(r'C:\Users\Administrator\Desktop\python\Py_webSpider\github\IP_pond\Improve')
from getProxy import get_proxies

def getHtmlText(url,ipcount=3):

    proxies = get_proxies()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400',
        'referer':'https://weixin.sogou.com/',
    }
    try:
        r =requests.get(url,headers=headers,proxies=proxies,timeout=10)
        r.raise_for_status()
        return r.text

    except Exception as e:
        if('443'in str(e)):
            if ipcount>0:
                getHtmlText(url,ipcount=ipcount-1)

            else:
                print('finish')
        else:
            print(e)


def getInfo(html):
    if html:
        doc = etree.HTML(str(html))
        lis = doc.xpath('//ul[@class="news-list"]/li')
        for li in lis:
            try:
                title = li.xpath('./div[2]/h3/a')[0]
                newtitle = str(title.xpath('string(.)')).replace(' ',"").replace('\n','')

                content = li.xpath('./div[2]/p')[0]
                newcontent = str(content.xpath('string(.)')).replace(' ',"").replace('\n','')

                wechatname = li.xpath('.//div[@class="s-p"]/a/text()')[0]

                datetime = li.xpath('.//div[@class="s-p"]/@t')[0]
                datetime = timeCovert(datetime)

                print(newtitle)
                print(newcontent)
                print(wechatname)
                print(datetime)
                yield {
                    'title':newtitle,
                    'content':newcontent,
                    'wechatname':wechatname,
                    'datetime':datetime,
                }
            except:
                continue


def timeCovert(e):
    js_code="""
    function timeConvert(e) {
    if (e) {
        var n, t, r, o;
        if (e = parseInt(e),
        o = parseInt((new Date).getTime() / 1e3) - e,
        r = parseInt(o / 86400),
        t = parseInt(o / 3600),
        n = parseInt(o / 60),
        r > 0 && r < 4)
            return r + "天前";
        if (r <= 0 && t > 0)
            return t + "小时前";
        if (t <= 0 && n > 0)
            return n + "分钟前";
        var c = new Date(1e3 * e);
        return c.getFullYear() + "-" + (c.getMonth() + 1) + "-" + c.getDate()
    }
    return ""
}
    """
    try:
        data = execjs.compile(js_code)      #编译对象(js语句)
        data = data.call('timeConvert',e) #执行js  ('js函数名',*参数)
        return data
    except Exception as ee:
        print(ee)




def conn_db():
    db = pymysql.connect('localhost','root','rootroot','pythonsql')
    return db

def insert_db(db,info):
    cursor = db.cursor()
    sql = 'insert ignore into sogouwechat(title,content,wechatname,optime)values("{}","{}","{}","{}")'.format(info['title'],info['content'],info['wechatname'],info['datetime'])
    try:
        cursor.execute(sql)
        db.commit()
        print('添加成功')
    except Exception as e:
        db.rollback()
        print(e)

def close_db(db):
    db.close()

if __name__ == '__main__':
    db = conn_db()

    for i in range(1,11):
        url = 'https://weixin.sogou.com/weixin?type=2&query=DOTA2&page={}'.format(i)
        html = getHtmlText(url)
        getInfo(html)
        for info in getInfo(html):
            insert_db(db,info)
        time.sleep(random.randint(3,5))

    close_db(db)
    print('finish')

