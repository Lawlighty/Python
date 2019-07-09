import requests
import re
import sys
sys.path.append(r'C:\Users\Administrator\Desktop\python\Py_webSpider\github\IP_pond\Improve')
from getProxy import get_proxies

def getHtmlText(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400',
        'Referer': 'https://search.bilibili.com/',
    }
    proxies = get_proxies()
    try:
        r = requests.get(url, headers=headers, proxies=proxies, timeout=10)
        r.raise_for_status()
        return r.text
    except Exception as e:
        print(e)

def getPat():
    pattern = re.compile(
        '<li class="video matrix"><a href="(?P<url>.*?)".*?title="(?P<title>.*?)".*?title="观看".*?<i class="icon-playtime"></i>.*?(?P<amount_of_play>.*?)<.*?<span title="上传时间".*?<i class="icon-date"></i>.*?(?P<timeUp>.*?)<.*?'
        'title="up主".*?<i class="icon-uper"></i>.*?>(?P<uper>.*?)<', re.S)
    return pattern

def getInfo(text,pattern):
    try:
        infos = pattern.finditer(text)
        for info in infos:
            yield {
                'url':info.group('url'),
                "title":info.group('title'),
                'amount_of_play':info.group('amount_of_play').replace('\n','').replace(' ',""),
                'uper': info.group("uper").replace('\n','').replace(' ',""),
                'timeUp':info.group("timeUp").replace('\n','').replace(' ',""),
            }
    except Exception as e:
        print(e)

def main():
    url = 'https://search.bilibili.com/all?keyword=python&from_source=banner_search&spm_id_from=333.334.b_62616e6e65725f6c696e6b.1'
    text = getHtmlText(url)
    pattern = getPat()
    res = getInfo(text,pattern)
    for i in res:
        print(i)

main()