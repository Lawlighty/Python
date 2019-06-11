import json
from lxml import etree
import requests

from 存储模块 import RedisClient


class Crawler():
    def get_proxies(self):
        proxies = []
        for proxy in self.crawl_kuaidaili():
            print('成功获得代理',proxy)
            proxies.append(proxy)
        return proxies

    def crawl_daili66(self, page_count = 3):  #
        """
        网址http://www.66ip.cn/x.html
        :param page_count: 网页爬取深度
        :return: 代理
        """
        start_url = "http://www.66ip.cn/{}.html"
        urls = [start_url.format(page) for page in range(1,page_count+1)]
        for url in urls:
            print('爬取:',url)
            html = requests.get(url).text
            if html:
                doc = etree.HTML(str(html))
                trs = doc.xpath('//div[@class="containerbox boxindex"]/div/table/tr')[1:]
                for tr in trs:
                    ip = tr.xpath('./td[1]/text()')[0]
                    port = tr.xpath('./td[2]/text()')[0]
                    yield ':'.join([ip,port]) #123.456.789:8080

    def crawl_kuaidaili(self,page_count = 10):
        """
        代理网址 https://www.kuaidaili.com/free/
        :param page_count:爬取深度
        :return:代理
        """
        start_url = "https://www.kuaidaili.com/free/inha/{}/"
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            html = requests.get(url).text
            doc = etree.HTML(str(html))
            trs = doc.xpath('//div[@id="list"]/table/tbody/tr')
            for tr in trs:
                ip = tr.xpath("./td[1]/text()")[0]
                port = tr.xpath("./td[2]/text()")[0]
                yield ':'.join([ip, port])


class Getter():
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = Crawler()

    def pound_is_full(self):
        if self.redis.countIp()>=50:#ip池满
            return True
        else:
            return False

    def run(self):
        print('获取器开始执行')
        if not self.pound_is_full():#没满
            # callback = [self.crawler.crawl_daili66(), self.crawler.crawl_kuaidaili()]
            proxies = self.crawler.get_proxies()
            for proxy in proxies:
                self.redis.add(proxy)
