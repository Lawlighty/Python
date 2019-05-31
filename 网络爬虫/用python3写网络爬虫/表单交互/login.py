
# 登录 url = 'http://example.python-scraping.com/user/login'
# 登录成功 url= 'http://example.python-scraping.com/places/default/index#'
import requests
from urllib.parse import urlencode
from lxml import etree

def loginA(url):#只有表单显性数据提交
    data = {
        'email': '12345@163.com',
        'password': '123456abc',
    }
    r = requests.post(url,data=data)
    print(r.url)


def loginB(url):#只有表单数据提交
    data={
        'email':'12345@163.com',
        'password':'123456abc',
        'remember_me': 'on',
        '_next': '/places/default/index',
        '_formkey': '6cbb2963-6f71-4dc7-8e33-3c2af9ab8fed',
        '_formname': 'login'
    }

    # encodData = urlencode(data)
    r  = requests.post(url, data=data)
    print(r.url)

def getHtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r

    except Exception as e:
        print(e)

#获得表单中input 标签的详情
def getAllInputTags(html):
    doc = etree.HTML(str(html))

    data ={}

    for i in doc.xpath('//form//input'):
        if i.get('name'):
            data[i.get('name')] = i.get('value')

    print(data)
    return data

def main(url):
    html = getHtml(url)
    data = getAllInputTags(html.content)
    data['email'] = '123456@163.com'
    data['password'] = '123456abc'
    r = requests.post(url,data, cookies=html.cookies)
    print('当前url:',r.url)

if __name__ == '__main__':
    url = 'http://example.python-scraping.com/user/login'
    # html,cookies = getHtml(url)
    # getAllInputTags(html)
    # print('*'*10)
    # getNowUrl(cookies)
    # main(url)
    # loginA(url)
    # loginB(url)
    main(url)