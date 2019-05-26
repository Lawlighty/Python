# 拿微博为例，我们接下来用 Python 来模拟这些 Ajax 请求，把马云发过的微博爬取下来
import requests
import json
from urllib.parse import urlencode
from pyquery import PyQuery as pq

def getHtmlText(page_num):
    url = 'https://m.weibo.cn/api/container/getIndex?sudaref=germey.gitbooks.io&display=0&retcode=6102&'
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3505.4000',

    }
    params = {
        'type': 'uid',
        'value': '2145291155',
        'containerid': '1076032145291155',
        'page': page_num,
    }
    #吧键值对以 &x=y 连接
    ll = urlencode(params)
    url = url+ll
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        # return json.loads(r.text)
        return r.json()
    except Exception as e:
        print(e)

def parser_json(json):
    if json:
        infos = json['data']['cards']

        for info in infos:
            weibo = {}
            weibo['id'] = info['mblog'].get('id','无')
            #使用 pyquery 把文本中的html内容去掉 清洗文本
            weibo['text'] = pq(info['mblog'].get('text','无')).text().replace('\n','').strip()
            #转化为迭代器对象
            yield weibo

#是否是有效链接
def Judg_page_isOk(json):
    isOK = False
    if json.get('ok'):
        isOK = True
    return isOK

if __name__ == '__main__':
    page = 1
    while True:
        json = getHtmlText(page)
        if Judg_page_isOk(json):
            dics = parser_json(json)
            for kv in dics:
                print(kv)

            page+=1

        else:
            break
