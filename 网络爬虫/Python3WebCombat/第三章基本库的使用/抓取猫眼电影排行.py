# 我们利用 Requests 和正则表达式来抓取猫眼电影 TOP100 的相关内容
import re
import requests
from pyquery import PyQuery as pq
from lxml import etree
import json
from multiprocessing import Pool
import time
import sys
sys.path.append(r'C:\Users\Administrator\Desktop\python\Py_webSpider\github\IP_pond\Improve')
from getProxy import get_proxies
url = 'https://maoyan.com/board/4?offset=0'

def getHtmlText(url):
    headers ={
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3505.400',
        'Referer':'https://maoyan.com/board'
    }
    proxies = get_proxies()
    try:
        r =requests.get(url,headers=headers, proxies=proxies, timeout=3)
        r.raise_for_status()
        return r.text
    except Exception as e:
        print(e)

def getInfo(text):
    if text:
        doc = pq(text)
        doc = etree.HTML(str(doc))
        movieInfos = doc.xpath('//dl[@class="board-wrapper"]/dd')
        for i in movieInfos:

            ranking = i.xpath('./i/text()')[0]
            title = i.xpath('.//a[@class="image-link"]/@title')[0]
            actors = i.xpath('./div/div/div[1]/p[2]/text()')[0].strip()
            time = i.xpath('.//p[@class="releasetime"]/text()')[0]
            # print(ranking)
            # print(title)
            # print(actors)
            # print(time)
            yield {
                'ranking':ranking,
                'title':title,
                'actors':actors,
                'time':time,
            }

def SaveInfo(item):
    with open('猫眼电影TOP100.txt','a') as f:
        # f.write(json.dumps(item, ensure_ascii=False)+'\n')
        f.write('排名:'+item['ranking']+'\n'+item['title']+'\n'+item['actors']+'\n'+item['time']+'\n\n')

def main(url):
    text = getHtmlText(url)
    for item in getInfo(text):
        SaveInfo(item)

if __name__ == '__main__':
    start = time.time()
    # p = Pool()
    # url = [ 'https://maoyan.com/board/4?offset={}'.format(int(i) * 10) for i in range(0,11)]
    # p.map(main,url)
    # p.close()
    # p.join()
    url = ['https://maoyan.com/board/4?offset={}'.format(int(i) * 10) for i in range(0, 11)]
    for i in url:
        main(i)
    print('finish')
    end = time.time()
    print('用时:',(end-start))

