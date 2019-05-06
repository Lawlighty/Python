import json
import requests
import time
import random
import openpyxl
import sys
sys.path.append(r'C:\Users\Administrator\Desktop\python\Py_webSpider\github\IP_pond\Improve')
from getProxy import get_proxies

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3469.400',
    'Referer':"https://movie.douban.com/tv/"
}
proxies = get_proxies()
url = 'https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=20'

def getHTML(url):
    try:
        r = requests.get(url, headers=headers, proxies=proxies)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except Exception as e:
        print(e)

def getTVinfo(html, fname):
    try:
        info = json.loads(html)
        subjects = info['subjects']
        wb = openXlsx(fname)

        for sj in subjects:
            infoList = []

            title = sj.get('title')
            rate = sj.get('rate','暂无')
            url = sj.get('url','暂无')

            infoList.append(title)
            infoList.append(rate)
            infoList.append(url)

            insertXlsx(wb, fname, infoList)

        closeXlsx(wb, fname)

    except Exception as e:
        print(e)

def CreateXlsx(fname):
    wb = openpyxl.Workbook()
    list = ['title', 'rate', 'url']
    ws = wb.active
    ws.title = '{}'.format(fname)
    ws.append(list)

    wb.save(fname)

def openXlsx( fname):
    wb = openpyxl.load_workbook(fname)
    return wb

def insertXlsx(wb ,fname,infoList):

    ws = wb[fname]
    ws.append(infoList)

def closeXlsx(wb,fname):
    wb.save(fname)

def main():
    fname = str(input('输入保存文件的名称:>'))
    fname = fname + '.xlsx'
    CreateXlsx(fname)


    pagedeep = int(input('输入爬取页数>'))
    for num in range(pagedeep):
        url = 'https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={}'.format(num*20)
        print('当前爬取 第{}页 url:{}'.format(num+1, url))
        html = getHTML(url)
        getTVinfo(html, fname)
        time.sleep(random.randint(1,3))
    print('finish')

if __name__ == '__main__':
    main()
