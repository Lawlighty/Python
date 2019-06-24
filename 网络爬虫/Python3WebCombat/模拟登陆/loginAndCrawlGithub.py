# 模拟登陆并爬取GitHub
import requests
from lxml import etree
import re
from pyquery import PyQuery as pq


class Login():
    def __init__(self):
        self.headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400',
            'Referer':'https://github.com',
            'Host':'github.com'
        }
        self.login_url = 'https://github.com/login'#登陆url
        self.post_url = 'https://github.com/session'#表单提交url
        self.feed_url = 'https://github.com/dashboard-feed'
        self.logined_url = 'https://github.com/settings/profile'#检验是否登录
        self.session = requests.Session()

    def get_authtoken(self):
        resp = self.session.get(self.login_url, headers=self.headers).text
        doc = etree.HTML(str(resp))
        authenticity_token = doc.xpath('//*[@id="login"]/form/input[2]/@value')[0]
        print('authenticity_token',authenticity_token)
        return authenticity_token

    def login(self,username, password):
        data = {
            'commit':'Sign in',
            'utf8':'✓',
            'authenticity_token':self.get_authtoken(),
            'login':username,
            'password':password,
            'webauthn-support':'supported',

        }
        response = self.session.post(self.post_url, data=data, headers=self.headers)
        if response.status_code ==200:
            resp = self.session.get(self.feed_url, headers=self.headers)
            if resp.status_code == 200:
                self.dynamics(resp.text)#主页动态
            else:
                print('动态错误')
                print(resp.status_code)
            response = self.session.get(url=self.logined_url, data=data, headers=self.headers)
            if response.status_code == 200:
                self.profile(response.text)#个人信息页面
            else:
                print('主页错误')
                print(response.status_code)
        else:
            print('表单错误')


    def dynamics(self, html):
        selector = pq(html)
        # print(selector.text())
        dynamics = selector('div[class="d-flex flex-items-baseline"] div')
        dynamics.find('span').remove()
        # print(dynamics.text())
        for item in dynamics.items():
            dynamic = item.text().strip()
            print(dynamic)

    def profile(self, html):
        doc = etree.HTML(str(html))
        name = doc.xpath('//*[@id="user_profile_name"]/@value')[0]
        location = doc.xpath('//*[@id="user_profile_location"]/@value')[0]

        print('{}来自{}'.format(name, location))

if __name__ == '__main__':
    mylogin = Login()
    mylogin.login(username="",password="")
