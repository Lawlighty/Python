# http://example.python-scraping.com/search 爬取所有国家名
import requests
import json
import time
import threading
from multiprocessing import Pool
import openpyxl
import re
import pandas as pd


def getHtmlText(url):
    headers= {
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3505.400',
    }
    try:
        r = requests.get(url, headers=headers ,timeout= 3)
        r.raise_for_status()
        return r.json()

    except Exception as e:
        print(e)

def getCname(json, nameList, urlList ):
    if json:
        if json['records']:
            num_pages = int(json['num_pages'])
            infos = json.get('records')

            for info in infos:

                country_or_district = info.get('country_or_district')
                pretty_link = info.get('pretty_link')
                pretty_link= re.findall('<a href=\"(.*?)\">', pretty_link)[0]
                pretty_link = 'http://example.python-scraping.com' + pretty_link
                print('name:',country_or_district)
                print('link:',pretty_link)

                nameList.append(country_or_district)
                urlList.append(pretty_link)


            return num_pages,nameList,urlList

def getDataFrame(nameList, urlList):
    mydic = {
        'country_or_district': nameList,
        'pretty_link':urlList,
    }
    mydf = pd.DataFrame(mydic)
    return mydf

def SaveAsCsv(df):
    df.to_csv('我的country_Csv文件.csv', header=True, index=False)
    print('保存成功')


if __name__ == '__main__':
    start = time.time()
    url = 'http://example.python-scraping.com/places/ajax/search.json?&search_term=.&page_size=10&page=0'
    print('第1页:' )

    nameList = []
    urlList = []

    json = getHtmlText(url)
    num_pages,nameList,urlList = getCname(json,nameList, urlList)

    for i in range(1,num_pages):
        print('第{}页:'.format(i+1) )
        url = "http://example.python-scraping.com/places/ajax/search.json?&search_term=.&page_size=10&page={}".format(i)
        json = getHtmlText(url)
        getCname(json, nameList, urlList)

    df = getDataFrame(nameList, urlList)

    SaveAsCsv(df)

    end = time.time()
    print('用时:',end-start)

