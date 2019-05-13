#笔趣岛搜索
# url = 'https://www.biqudao.com/bqge127585/7402276.html'
import requests
from lxml import etree
from pyquery import PyQuery as pq
import sys
sys.path.append(r'C:\Users\Administrator\Desktop\python\Py_webSpider\github\IP_pond\Improve')
from getProxy import get_proxies
import re
import time
from tqdm import trange

def getHtmlText(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3469.400',
        'Referer':'https://www.biqudao.com/bqge127585/7403388.html'
    }

    cookies = {
        'cookie':"UM_distinctid=16ab10a567b541-08e6327450281f-4a764a16-100200-16ab10a567c4a8; CNZZDATA1275036968=1243908052-1557745098-https%253A%252F%252Fwww.baidu.com%252F%7C1557745098; bookid=127585; bcolor=; font=; size=; fontcolor=; width=; chapterid=7403387; chaptername=%25u7B2C%25u4E00%25u5343%25u4E00%25u767E%25u4E00%25u5341%25u4E8C%25u7AE0%25u771F%25u6B63%25u7684%25u7389%25u5E1D%25uFF08%25u4E0A%25uFF09"
    }
    proxies = get_proxies()
    try:

        r = requests.get(url, headers=headers, proxies=proxies)
        r.raise_for_status()
        r.encoding = 'utf-8'

        return r.text

    except Exception as e:
        print(e)

def getInfo(html):
    doc = pq(html)
    doc = etree.HTML(str(doc))

    title = doc.xpath('//div[@class="bookname"]/h1/text()')[0]
    # print(title)
    content = doc.xpath('//*[@id="content"]/text()')
    # content = ''.join(content)
    new_content = []
    for i in content:
        i  = re.sub('\u3000', '\n',i)
        new_content.append(i)

    content = ''.join(new_content)
    # print(content)
    intoTxt(title, content)


def intoTxt(title,content):
    with open('{}.txt'.format(title), 'w+',encoding='utf-8') as f:
        f.write(content)

def main():
    for i in trange(7402276,7403397):
        url = 'https://www.biqudao.com/bqge127585/{}.html'.format(i)
        html = getHtmlText(url)
        getInfo(html)

        time.sleep(3)
    # print(html)

main()