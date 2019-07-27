import requests
from lxml import etree
import json
import time
from multiprocessing import Pool
from mango_op import save_into_mongo
import sys
sys.path.append(r'C:\Users\Administrator\Desktop\python\Py_webSpider\github\IP_pond\Improve')
from getProxy import get_proxies

def get_HtmlText(keyword):
    '''
    获得网页内容
    :param keyword: 产品关键字
    :return: 网页内容
    '''
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3719.400 QQBrowser/10.5.3715.400',
        'referer':'https://www.jd.com/2019',
    }
    url = 'https://search.jd.com/search?'
    for i in range(1,10):
        proxies = get_proxies()
        param = {
            'keyword':keyword,
            'enc':'utf-8',
            'page':i,

        }
        try:
            r = requests.get(url, params=param, headers=headers, proxies=proxies)
            r.raise_for_status()
            r.encoding = 'utf-8'
            yield r.text
        except Exception as e:
            print(e)

def get_productId(text):
    '''
    获得产品id
    :param text: 当前网页内容
    :return: 产品id
    '''
    doc = etree.HTML(str(text))
    lis = doc.xpath('//*[@id="J_goodsList"]/ul/li')
    for li in lis:
        productId = li.xpath('./@data-sku')[0]
        yield productId

def get_comments(productId):
    '''
    获得每个产品10页评论
    :param productId:
    :return:
    '''
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3719.400 QQBrowser/10.5.3715.400',
        'referer': 'https://www.jd.com/2019',
    }
    url = 'https://sclub.jd.com/comment/productPageComments.action?'
    for page in range(0,10):
        proxies = get_proxies()
        param_data = {
            'callback':'fetchJSON_comment98vv1216',
            'productId':productId,
            'score':0,
            'sortType':5,
            'page':page,
            'pageSize': 10,
            'isShadowSku': 0,
            'fold': 1
        }
        try:
            response = requests.get(url, params=param_data, headers=headers, proxies=proxies)
            response.raise_for_status()
            response = response.text
            #除去网页无用信息fetchJSON_comment98vv1216()
            new_resp = response.replace('fetchJSON_comment98vv1216(',"").replace(');',"")
            data = json.loads(new_resp)
            comments = data['comments']
            p = Pool()
            p.map(save_into_mongo,comments)

        except Exception as e:
            print(e)

def main():
    start = time.time()
    for text in  get_HtmlText('文胸'):
        for productId in get_productId(text):
            get_comments(productId)

    end = time.time()
    print('finish, 用时:{}',end-start)
if __name__ == '__main__':
    main()

    # print(text)
