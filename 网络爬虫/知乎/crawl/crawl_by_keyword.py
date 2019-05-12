# 通过输入关键字爬取获得的信息
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from lxml.html import fromstring
import cssselect
import json
import re
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
from lxml import etree

class zhihu_keyword:

    #初始化
    def __init__(self):
        self.url = 'https://www.zhihu.com/'

        self.driverPath = r'C:\Users\Administrator\AppData\Local\Programs\Python\Python37\chromedriver.exe'

        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches',['enable-automation'])

        self.driver = webdriver.Chrome(executable_path=self.driverPath, options=self.options)

        self.wait = WebDriverWait(self.driver, 10)

    def login(self):
        self.driver.get(self.url)

        dl_btn = self.driver.find_element_by_css_selector('.SignContainer-switch > span')
        dl_btn.click()
        time.sleep(3)
        #进入登录界面
        shejiao_btn = self.driver.find_element_by_css_selector(".Button.Login-socialButtonEntrance.Button--plain")
        shejiao_btn.click()
        time.sleep(3)

        weibo_btn = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.Icon.Login-socialIcon.Icon--weibo')))
        weibo_btn.click()
        time.sleep(3)
        #进入微博账号登录知乎

        weibo_username = self.driver.find_element_by_id('userId')
        weibo_username.send_keys('用户名')
        time.sleep(3)
        weibo_psw = self.driver.find_element_by_id('passwd')
        weibo_psw.send_keys('密码')
        time.sleep(3)

        dl_btn = self.driver.find_element_by_css_selector(".WB_btn_login.formbtn_01")
        dl_btn.click()
        time.sleep(3)
        # 允许授权
        allow_btn = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".WB_btn_allow.formbtn_01")))
        allow_btn.click()

    def input_keyword(self):
        search_bar = self.driver.find_element_by_class_name('Input')
        search_bar.send_keys(keyword)
        time.sleep(3)

        search_btn = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'Button.SearchBar-searchIcon.Button--primary')))
        search_btn.click()
        time.sleep(3)

    def drop_down(self):
        js = "var q=document.documentElement.scrollTop=100000"
        #下拉到底部五次
        for i in range(0,5):
            self.driver.execute_script(js)
            time.sleep(3)



    def get_info_xpath(self):
        html = self.driver.page_source
        doc = pq(html)
        doc = etree.HTML(str(doc))
        Lists = doc.xpath('//*[@id="SearchMain"]/div/div/div/div/div')
        print(Lists)

        #总工程数
        countL = len(Lists)

        for List in Lists:
            title = List.xpath('div/div/h2/a/span/text()')

            if title:

                title = List.xpath('div/div/h2/a/span/text()')[0]

                url = List.xpath('div/div/h2/a/@href')[0]
                url = 'https://'+url

                author = List.xpath('div/div/div/div[1]/span/b/text()')[0]

                content = List.xpath('div/div/div/div[1]/span/text()')
                content = ' '.join(content[1:])

                with open('zhihu_key.txt', 'a+', encoding='utf-8')as f:
                    f.write('标题:' + '\t' + title + '作者:' + '\t' + author+'\n')
                    f.write('链接:' + '\t' + url+'\n')
                    f.write('内容:' + '\t' + content + '\n\n')

                now = int(Lists.index(List)+1)
                #进度
                loading = now/countL*100
                #格式化输出
                print('当前进度: {:.2f} %'.format(loading))

                time.sleep(3)

            else:
                continue




if __name__ == '__main__':


        zf = zhihu_keyword()
        zf.login()

        keyword = str(input('输入信息关键字>'))
        zf.input_keyword()
        zf.drop_down()
        time.sleep(5)
        zf.get_info_xpath()




