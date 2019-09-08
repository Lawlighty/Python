import requests
from lxml import etree
import re
import tqdm

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

    def getHtmlText(self, url):
        try:
            resp = self.session.get(url, headers=self.headers, timeout=5)
            resp.raise_for_status()
            return resp.text
        except Exception as e:
            print(e)

    def Pos(self, x, html):
        num = None
        pos = abs(int(re.search(r'' + x + ' { background-position-x:(.*?)px }', html).group(1)))
        if pos < 7:
            num = 0
        elif pos < 20:
            num = 1
        elif pos < 34:
            num = 2
        elif pos < 47:
            num = 3
        elif pos < 50:
            num = 4
        elif pos < 73:
            num = 5
        elif pos < 86:
            num = 6
        elif pos < 97:
            num = 7
        elif pos < 113:
            num = 8
        else:
            num = 9
        return num

    def getListSum(self, nlist):
        sum = 0
        if len(nlist)==3:
            sum = int(nlist[0])*100+int(nlist[1])*10+int(nlist[2])
        elif len(nlist)==2:
            sum = int(nlist[0])*10+int(nlist[1])
        else:
            sum = int(nlist[0])
        return sum

    def getPageSum(self, text ):
        sum = 0
        html = text
        doc = etree.HTML(str(text))
        cmls = doc.xpath('//div[@class="row"]/div[@class="col-md-1"]')
        for cml in cmls:
            lS = 0
            numList = []
            NumClass = cml.xpath('./div/@class')
            for i in NumClass:
                code = str(str(i).split(' ')[0])
                num = self.Pos(code, html)
                numList.append(num)
            # print('numlist:::',numList)
            lS = self.getListSum(numList)
            sum+=lS
        return sum

if __name__ == '__main__':
    Sum = 0
    mc = myC()
    mc.login_in('13616859570@163.com','liyixin123')
    # url = 'http://glidedsky.com/level/web/crawler-sprite-image-1?page={}'.format(669)
    # text = mc.getHtmlText(url)
    # sum = mc.getPageSum(text)
    # print(sum)
    for i in tqdm.tqdm(range(1,1001)):
        url = 'http://glidedsky.com/level/web/crawler-sprite-image-1?page={}'.format(i)
        text = mc.getHtmlText(url)
        sum = mc.getPageSum(text)
        Sum+=sum
    print(Sum)
# 2696525