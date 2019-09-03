import requests
from lxml import etree
import tqdm
import time
from threading import Thread
import queue
from multiprocessing.pool import ThreadPool
from multiprocessing import pool

class myC:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400',

        }
        self.login_url = 'http://glidedsky.com/login'
        self.target_url = 'http://glidedsky.com/level/web/crawler-basic-1'

    def get_token(self):
        resp = self.session.get(self.login_url, headers=self.headers, timeout=5).text
        doc = etree.HTML(str(resp))
        _token = doc.xpath('//div[@class="card-body"]/form/input/@value')[0]
        return _token

    def login_in(self, email, password):
        form_data = {
            '_token':self.get_token(),
            'email':email,
            'password':password,
        }
        try:
            resp = self.session.post(self.login_url, headers=self.headers,data= form_data, timeout=5)
            resp.raise_for_status()
            return resp.text

        except Exception as e:
            print(e)

    def getHtmlText(self,url):
        try:
            resp = self.session.get(url, headers=self.headers, timeout=5)
            resp.raise_for_status()
            return resp.text
        except Exception as e:
            print(e)

    def getSum(self,text):
        sum = 0
        doc = etree.HTML(str(text))
        rows = doc.xpath('//div[@class="row"]/div')
        for i in rows:
            sum += float(str(i.xpath('./text()')[0]).replace('\n','').replace(' ',''))
        return sum

    def GO(self,url):
        text = self.getHtmlText(url)
        res = self.getSum(text)
        return res

if __name__ == '__main__':
    start = time.time()
    #线程池
    # mypool = ThreadPool(processes=10)
    mypool = pool.Pool(10)
    mc = myC()
    mc.login_in('13616859570@163.com','liyixin123')
    Sum = 0
    resList = []
    for i in tqdm.tqdm(range(1,1001)):
        url = 'http://glidedsky.com/level/web/crawler-basic-2?page={}'.format(i)
        async_result = mypool.apply_async(func=mc.GO, args=(url,))
        res = async_result.get()
        Sum+=res
    print(Sum)

    # urlList = ["http://glidedsky.com/level/web/crawler-basic-2?page={}'.format(i)" for i in range(1,1001)]
    # for i in tqdm.tqdm(urlList):
    #     async_result = mypool.apply_async(func=mc.GO, args=(i,))
    #     res = async_result.get()
    #     resList.append(res)
    # for i in resList:
    #     Sum+=i
    # print(Sum)

    # for i in tqdm.tqdm(range(1,1001)):
    #     url = 'http://glidedsky.com/level/web/crawler-basic-2?page={}'.format(i)
    #     async_result = mypool.apply_async(func=mc.GO, args=(url,))
    #     res = async_result.get()
    #     Sum+=res
    # print(Sum)
    end = time.time()
    print('using {}'.format(end-start) )
    # 单线程
    # 2890858.0
    # using 124.14210033416748

    # 线程池
    # 2890858.0
    # using 84.0868091583252

