import requests
from lxml import etree
import json
import sys
sys.path.append(r'C:\Users\Administrator\Desktop\python\Py_webSpider\github\IP_pond\Improve')
from getProxy import get_proxies

def getHtmlText(url):
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3719.400 QQBrowser/10.5.3715.400',
    }
    proxies = get_proxies()
    try:
        r = requests.get(url, headers=headers, proxies=proxies)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.content
    except Exception as e:
        print(e)

def getBarrage(text):
    try:
        doc = etree.HTML(text)
        dlists = doc.xpath('//d')
        for list in dlists:
            barrage = list.xpath('./text()')[0]
            print(barrage)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=102777577'
    text = getHtmlText(url)
    getBarrage(text)