from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pyquery import PyQuery as pq
from lxml import etree
import re
import pymysql

class MySpider(object):

    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='rootroot', db='pythonsql', charset='utf8')
        self.cursor = self.conn.cursor()

        self.url = 'https://s.taobao.com/search?q=ipad'
        self.driver_path = r'C:\Users\Administrator\AppData\Local\Programs\Python\Python37\chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.driver = webdriver.Chrome(executable_path=self.driver_path, options=self.options)
        self.wait = WebDriverWait(self.driver, 10)

    def openWeb(self):
        self.driver.get(self.url)

        # 等待 密码登录选项 出现
        # 定位器定位 ---->密码登录按钮
        password_login = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.qrcode-login > .login-links > .forget-pwd.J_Quick2Static')))
        password_login.click()

        # 等待 微博登录选项 出现
        weibo_login = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.weibo-login')))
        weibo_login.click()

        # 等待 微博账号 出现
        # weibo_user = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.username > .W_input')))
        weibo_user = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.inp.username > .W_input')))
        weibo_user.send_keys(weibo_username)

        # 等待 微博密码 出现
        weibo_pwd = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.inp.password > .W_input')))
        weibo_pwd.send_keys(weibo_password)

        # 等待 登录按钮 出现
        submit = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn_tip > a > span')))
        submit.click()

        time.sleep(3)

    def drop_down(self):
        for i in range(1,3):
            js = 'var q=document.documentElement.scrollTop={}'.format(i*830)
            self.driver.execute_script(js)
            time.sleep(2)

    def getInfo(self):
        doc = pq(self.driver.page_source)
        doc = etree.HTML(str(doc))

        items = doc.xpath('//div[@class="items"]/div')
        for item in items:
            gname = item.xpath('.//div[@class="row row-2 title"]/a/text()')[0].replace(' ','').replace('\n','').split(' ')[0]
            if item.xpath('.//div[@class="row row-2 title"]/a/text()[1]')[0]:
                introduce1 = item.xpath('.//div[@class="row row-2 title"]/a/text()[1]')[0].replace(' ','').replace('\n','')

                if item.xpath('.//div[@class="row row-2 title"]/a/text()[2]')[0]:
                    introduce2 = item.xpath('.//div[@class="row row-2 title"]/a/text()[2]')[0].replace(' ','').replace('\n','')
                    introduce = introduce1+introduce2
                else:
                    introduce = introduce1
            else:
                introduce = '暂无'


            price = item.xpath('.//div[@class="price g_price g_price-highlight"]/strong/text()')[0]
            if item.xpath('.//span[@class="dsrs"]'):
                shop = item.xpath('.//div[@class="shop"]/a/span[2]/text()')[0]
            else:
                shop = item.xpath('.//a[@class="shopname"]/text()')[0]

            yield {
                'gname':gname,
                'introduce':introduce,
                'price':price,
                'shop':shop,
            }

    def intoDB(self,item):
        sql = 'insert ignore into tbgoods(gname,introduce,price,shop) values("{}","{}","{}","{}")'.format(item['gname'],item['introduce'],item['price'],item['shop'])
        self.cursor.execute(sql)
        # 提交事务
        self.conn.commit()

    def closeDB(self):
        self.cursor.close()
        self.conn.close()

    def next_page(self):
        next = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ' .J_Ajax.num.icon-tag')))
        next.click()
        time.sleep(3)

    def closeChrome(self):
        self.driver.close()



if __name__ == '__main__':
    weibo_username = 'username'
    weibo_password = 'password'
    a = MySpider()
    a.openWeb()
    for i in range(5):
        a.drop_down()
        for item in a.getInfo():
            a.intoDB(item)
        a.next_page()
    a.closeDB()
    a.closeChrome()
    print('finish')




