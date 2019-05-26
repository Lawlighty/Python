# url= 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=20&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1558857906240'
# url= 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=40&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1558857909108'
import requests
import json
import re
from urllib.parse import urlencode
from multiprocessing import Pool
import os
import re

def get_page(offset):
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3505.4000',

    }
    params = {
        'aid': '24',
        'offset': offset,
        'format': 'json',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis'
    }
    base_url = 'https://www.toutiao.com/api/search/content/?keyword=%E8%A1%97%E6%8B%8D'
    url = base_url + urlencode(params)
    try:
        resp = requests.get(url, headers=headers,timeout=3)
        print(url)
        if 200  == resp.status_code:
            print(resp.json())
            return resp.json()
    except requests.ConnectionError:
        return None


def get_images(json):
    if json.get('data'):
        data = json.get('data')
        for item in data:
            # 有 cell_type 内容的项 跳过
            if item.get('cell_type') is not None:
                continue
            title = item.get('title')
            images = item.get('image_list')
            for image in images:
                image_url = image.get('url')
                #mydic
                yield {
                    'title': title,
                    'image_url':  image_url,
                }
                # print('title:',title)
                # print('url:',url)

def savePic(mydic):
    title = mydic.get('title').replace('|','').replace(' ','')
    url = mydic.get('image_url')
    picName = url.split('/')[-1]+'.jpg'
    div_path = title
    pic_path = '{}/{}'.format(div_path,picName)
    if not os.path.exists(div_path):
        os.makedirs(div_path)

    if not os.path.exists(pic_path):
        with open(pic_path, 'wb') as f:
            r = requests.get(url,timeout=1)
            f.write(r.content)
def myfun(i):
    json = get_page(i)
    for item in get_images(json):
        savePic(item)

if __name__ == '__main__':
    p = Pool()
    #爬取五页
    myList = [i*20 for i in range(5)]
    p.map(myfun,myList)
    p.close()
    p.join()

    print('finish')


