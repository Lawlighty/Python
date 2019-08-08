import requests
import json
from lxml import etree
import os
import shutil
import time
import datetime
import sys
sys.path.append(r'C:\Users\Administrator\Desktop\python\Py_webSpider\github\IP_pond\Improve')
from getProxy import get_proxies

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3719.400 QQBrowser/10.5.3715.400',
    'referer':'http://www.lovewzly.com/jiaoyou.html'
}

def getHtmlText(url):
    # proxies = get_proxies()
    try:
        r = requests.get(url, headers=headers, timeout=5)
        r.raise_for_status()
        return r.json()

    except Exception as e:
        print(e)

def getInfo(web_json):
    infos = web_json['data']['list']
    for i in infos:
        gender = '男'
        if i['gender'] ==2:
            gender = '女'
        yield {
            '名字': i['username'],
            '出身日期':i['birthdayyear'],
            '城市':i['city'],
            '省份':i['province'],
            '性别':gender,
            '学历': i['education'],
            '身高':i['height'],
            '婚姻': i['marry'],
            '独白':i['monolog'],
            '月薪':i['salary'],
            '照片':i['avatar']
        }

def EmptyPicDir():
    path = './pic'
    filelist = os.listdir(path)
    for i in filelist:
        filepath = os.path.join(path, i)
        if os.path.isfile(filepath):
            os.remove(filepath)
        else:
            shutil.rmtree(filepath,True)

    print('图片文件夹清空成功')

def intoPic(dic):
    url = dic['照片']
    name = dic['名字']
    birthdayyear = dic['出身日期']
    age = getAge(birthdayyear)
    education = dic['学历']
    city = dic['城市']
    monolog = dic['独白'].replace('\n','').replace(' ','')
    fileName = './pic/{}_{}_{}_{}_{}.png'.format(name,age,education,city,monolog)
    if os.path.exists(fileName):
        pass
    else:
        with open(fileName,'wb') as f:
            r = requests.get(url,timeout=5).content
            f.write(r)
        print('{}保存完毕'.format(fileName))

def getAge(birthdayyear):
    now_year = datetime.datetime.now().year
    age = now_year-int(birthdayyear)
    return age

if __name__ == '__main__':
    EmptyPicDir()
    url = 'http://www.lovewzly.com/api/user/pc/list/search?startage=21&endage=30&marry=1&page=2'
    web_json = getHtmlText(url)
    for i in getInfo(web_json):
        print(i)
        intoPic(i)
