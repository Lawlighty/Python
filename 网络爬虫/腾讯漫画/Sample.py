from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pyquery import PyQuery as pq
import time
from lxml import etree
import os
import re
import requests

class MyMh(object):

    def __init__(self):
        self.url = 'https://ac.qq.com/ComicView/index/id/623654/cid/1'
        self.driverPath = r'C:\Users\Administrator\AppData\Local\Programs\Python\Python37\chromedriver.exe'

        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])

        self.driver = webdriver.Chrome(executable_path=self.driverPath, options=self.options)

        self.wait = WebDriverWait(self.driver, 10)


    def OpWeb(self):
        self.driver.get(self.url)
        zhangjie = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.title-comicHeading')))
        zhangjie.click()
        time.sleep(3)

    def getPic(self):
        for i in range(1500):
            builder = ActionChains(self.driver)
            builder.key_down(Keys.ARROW_DOWN).perform()

        print('dakai ')

        doc = pq(self.driver.page_source)
        doc = etree.HTML((str(doc)))

        mhname = doc.xpath('//*[@id="chapter"]/text()')[0]
        zhangjiename = doc.xpath('//*[@id="comicTitle"]/span[3]/text()')[0]
        imgs = doc.xpath('//*[@id="comicContain"]/li')
        url_List = []
        for img in imgs:
            img_src = img.xpath('./img/@src')
            if len(img_src):
                url_List.append(img_src[0])

        return  mhname,zhangjiename,url_List

    def SaveMh(self,mhname,zhangjiename, url_List):
        dir_path = 'pic/{}/{}'.format(mhname, zhangjiename)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        for url in url_List:
            picN = url.split('_')[-1].split('/')[0]

            pic_path = '{}/{}'.format(dir_path, picN)
            if os.path.exists(pic_path):
                continue

            with open(pic_path,'wb') as f:
                r = requests.get(url)
                print('当前下载:{}'.format(pic_path))
                f.write(r.content)
                time.sleep(1)
        print('{}章节下载完成!'.format(zhangjiename))

    def Turn_page(self):
        nextPage = self.driver.find_element_by_id('mainControlNext')
        nextPage.click()

    def CloseDriver(self):
        self.driver.close()

if __name__ == '__main__':
        a = MyMh()
        a.OpWeb()
        mhname, zhangjiename, url_List = a.getPic()
        a.SaveMh(mhname,zhangjiename,url_List)
        a.Turn_page()
        # 免费为10话
        for i in range(9):
            mhname, zhangjiename, url_List = a.getPic()
            a.SaveMh(mhname, zhangjiename, url_List)
            a.Turn_page()
        a.CloseDriver()



