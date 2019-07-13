# 下载b站小视频排行榜
#-*-coding:utf-8-*-

import requests
import time
import random
import re
import json
import os
import tqdm

def get_html(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400',
        'Referer':'http://vc.bilibili.com/'
    }
    try:
        r = requests.get(url,headers = headers)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(e)

def getInfo(myjson):
    if myjson:
        items = myjson['data']['items']
        for item in items:
            description = item['item']['description']
            video_playurl = item['item'].get('video_playurl')
            yield {
                'description':description,
                'video_playurl':video_playurl,
            }

def DownLoad(dic):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400',
        'Referer': 'http://vc.bilibili.com/'
    }
    resp = requests.get(dic['video_playurl'], headers=headers, stream=True)
    resp.raise_for_status()
    rstr = r"[\/\\\:\*\?\"\<\>\\n|#-]"
    description = re.sub(rstr,'',dic['description'])
    while True:
        if os.path.exists('video/{}.mp4'.format(description)):
            break
        try:
            with open('video/{}.mp4'.format(description), 'wb') as f:
                f.write(resp.content)

            print('{}下载完成'.format(dic['description']))
        except:
            print("{}下载出错".format(description))
            break

if __name__ == '__main__':
    url = 'http://api.vc.bilibili.com/board/v1/ranking/top?page_size=10&next_offset=21&tag=%E4%BB%8A%E6%97%A5%E7%83%AD%E9%97%A8&platform=pc'
    myjson = get_html(url)
    for dic in tqdm.tqdm(list(getInfo(myjson))):
        DownLoad(dic)
        time.sleep(3)
    print('finish')

