import requests
from lxml import etree

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

    def getHtmlText(self):
        try:
            resp = self.session.get(self.target_url, headers=self.headers, timeout=5)
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
if __name__ == '__main__':

    mc = myC()
    mc.login_in('13616859570@163.com','liyixin123')
    text = mc.getHtmlText()
    sum = mc.getSum(text)
    print(sum)