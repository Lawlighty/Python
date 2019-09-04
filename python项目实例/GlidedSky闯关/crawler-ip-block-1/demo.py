import requests
import get_ip_from_DB
from lxml import etree
import tqdm
# def get_proxies(ip_list):
#     if ip_list:
#         proxies = {}
#         ip = ip_list.pop(0)
#         proxies['http'] = 'http://{ip}'.format(ip=ip)
#         print('当前 ip地址:', proxies)
#         return proxies
#     else:
#         print('ip池已经用完')
class myC:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400',

        }
        self.login_url = 'http://glidedsky.com/login'
        # self.target_url = 'http://glidedsky.com/level/web/crawler-basic-1'

    def get_proxies(self,ip_list):
        if ip_list:
            proxies = {}
            ip = ip_list.pop(0)
            proxies['http'] = 'http://{ip}'.format(ip=ip)
            print('当前 ip地址:', proxies)
            return proxies
        else:
            print('ip池已经用完')

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



    def getHtmlText(self,url,ip_list):
        proxies = self.get_proxies(ip_list)
        try:
            resp = self.session.get(url, headers=self.headers,proxies=proxies, timeout=5)
            resp.raise_for_status()
            print(resp.text)
            return resp.text
        except Exception as e:
            self.getHtmlText(url,ip_list)

    def get_page_sum(self,text):
        doc = etree.HTML(str(text))
        sum= 0
        if doc.xpath('//div[@class="row"]/div'):
            # 网页有内容
            rows = doc.xpath('//div[@class="row"]/div')
            for i in rows:
                sum += float(str(i.xpath('./text()')[0]).replace('\n', '').replace(' ', ''))
            return sum
        else:
            return sum


if __name__ == '__main__':
    ip_list = get_ip_from_DB.get_ip_list()
    Sum = 0
    mc = myC()
    mc.login_in('13616859570@163.com', 'liyixin123')
    for i in tqdm.tqdm(range(1,1001)):
        url = 'http://glidedsky.com/level/web/crawler-ip-block-1?page={}'.format(i)
        text = mc.getHtmlText(url, ip_list)

        Sum+=mc.get_page_sum(text)
        print('当前和:',Sum)
    print(Sum)


