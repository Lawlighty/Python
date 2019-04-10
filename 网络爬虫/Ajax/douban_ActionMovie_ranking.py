# url = 'https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action='
import requests
from bs4 import BeautifulSoup
import time
import random
import json

def getHtmlText(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400'
    }

    proxies_list =['http://116.209.55.252:9999','http://112.85.168.174:9999','http://183.148.138.7:9999']
    proxies = random.choice(list(proxies_list))

    try:
         r = requests.get(url, headers= headers, proxies= {'http':proxies})
         r.raise_for_status()
         r.encoding = 'utf-8'
         return r.text

    except Exception as e:
        print(e)

def getMovieInfo(html):
    info = json.loads(html)
    # print(info)
    for i in info:
        title = i.get('title','无')
        type = i.get('types','无')
        rating = i.get('rating','暂无评分')[0]
        cover_url = i.get('cover_url','无播放地址')
        with open('movie_ranking.txt', 'a') as f:
            f.write(str(title)+'\n')
            f.write(str(type) + '\n')
            f.write(rating + '\n')
            f.write(str(cover_url) + '\n')
            f.write('*'*100)
            f.writelines('\n'*3)
        f.close()

        print(title)
        print(type)
        print(rating)
        print(cover_url)
        print('*'*100)



if __name__ == '__main__':
    # url = 'https://movie.douban.com/typerank?type_name=%动作&type=5&interval_id=100:90&action='
    page_num = int(input('>输入爬取页数'))
    if page_num>0:
        for i in range(page_num):
            url= 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start={}&limit=20'.format(i*20)
            html = getHtmlText(url)
            getMovieInfo(html)
            print('第{}页爬取成功'.format(i+1))
            time.sleep(random.randint(1,3))
    else:
        print('页数必须大于等于1的整数')
    print('finish')
