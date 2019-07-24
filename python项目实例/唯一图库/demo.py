import requests
from lxml import etree
import re

def getHtmlText(url):
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3719.400 QQBrowser/10.5.3715.400',
    }
    # proxies = get_proxies()
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        print(r.encoding)
        # r.encoding = r.apparent_encoding
        return r.text.encode('ISO-8859-1').decode('gbk').encode('utf8').decode('utf-8')
        # return
    except Exception as e:
        print(e)

def getINfo(text):
    # doc = etree.HTML(str(text))
    # items = doc.xpath('//*[@id="infinite_scroll"]/div')
    # print(items)
    # pattern = re.compile(r'<div class="title".*?<a.*?href="(.*?)">(.*?)</a></span></div>', re.S)
    # pattern = re.compile(r'<p align="center"><a href=.*?><img alt=.*?src="(.*?)" /></a></p>', re.S)
    pattern = re.compile(r'<li class="pic-down h-pic-down"><a target="_blank" class="down-btn" href=\'(.*?)\'>.*?</a>',re.S)
    # pattern = re.compile(r'<li><a>共(.*?)页</a></li>', re.S)
    # pattern = re.compile(r'共(.*?)页', re.S)
    mains = re.findall(pattern, text)[0]
    print('min:',mains)

if __name__ == '__main__':
    # url = 'https://www.mmonly.cc/tag/xh1/7.html'
    # url = 'http://www.mmonly.cc/mmtp/qcmn/3805_2.html'
    url = 'http://www.mmonly.cc/mmtp/xgmn/297323_13.html'
    text = getHtmlText(url)
    # print(text)
    getINfo(text)
# url = 'www.asdasd/asdwdw/222.html'
# new_url = url[:-1]
# print(new_url)