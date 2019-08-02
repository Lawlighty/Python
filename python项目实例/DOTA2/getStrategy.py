# 获得英雄攻略
import requests
# from getNewestLogs import getHtmlText
from lxml import etree
import threading
import time
import sys
sys.path.append(r'C:\Users\Administrator\Desktop\python\Py_webSpider\github\IP_pond\Improve')
from getProxy import get_proxies

def getHtmlText(url):
    """
    获得网页源代码
    :param url: 网页链接
    :return: 网页内容
    """
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3719.400 QQBrowser/10.5.3715.400',
        'Referer': 'http://www.dotamax.com/',
    }
    # proxies = get_proxies()
    try:
        # r = requests.get(url, headers=headers,proxies=proxies,  timeout=5)
        r = requests.get(url, headers=headers, timeout=5)
        r.raise_for_status()
        # print('编码:',r.encoding)
        return r.text
    except Exception as e:
        print(e)

def getEtreeHtml(text):
    """
    转化为能被lxml解析的网页内容
    :param text:
    :return: 网页内容
    """
    doc = etree.HTML(str(text))
    return doc


def getEquip(doc):
    """
    获得推荐装备
    :param text:
    :return: 推荐装备
    """
    equip = []
    trs = doc.xpath('//table[@class="table table-hover table-striped table-list"]/tbody/tr')
    for tr in trs:
        equip.append(tr.xpath('.//text()')[0].replace(' ', '').replace('\n', ''))
    print('推荐出装:{}'.format(equip))
    # return equip


def getRestrainRival(doc):
    """
    自己最克制的对手
    :param text:
    :return: 克制对手
    """
    RestrainRival = []
    trs = doc.xpath('//table[@class="table table-hover table-striped table-list table-thead-left"][1]/tbody/tr')
    for tr in trs:
        RestrainRival.append(tr.xpath('.//text()')[0].replace(' ', '').replace('\n', ''))
    print('克制的对手:{}'.format(RestrainRival))

def getFearRival(doc):
    """
    自己最害怕的对手
    :param text:
    :return: 克制对手
    """
    FearRival = []
    trs = doc.xpath('//table[@class="table table-hover table-striped table-list table-thead-left"][2]/tbody/tr')
    for tr in trs:
        FearRival.append(tr.xpath('.//text()')[0].replace(' ', '').replace('\n', ''))
    print('害怕的对手:{}'.format(FearRival))


def getSuitTeammate(doc):
    """
    自己合适的队友
    :param text:
    :return: 队友
    """
    SuitTeammate = []
    trs = doc.xpath('//table[@class="table table-hover table-striped table-list table-thead-left"][3]/tbody/tr')
    for tr in trs:
        SuitTeammate.append(tr.xpath('.//text()')[0].replace(' ', '').replace('\n', ''))
    print('合适的队友:{}'.format(SuitTeammate))

def getBadTeammate(doc):
    """
    不合适自己的队友
    :param text:
    :return: 队友
    """
    BadTeammate = []
    trs = doc.xpath('//table[@class="table table-hover table-striped table-list table-thead-left"][4]/tbody/tr')
    for tr in trs:
        BadTeammate.append(tr.xpath('.//text()')[0].replace(' ', '').replace('\n', ''))
    print('不合适自己的队友:{}'.format(BadTeammate))

def main(url):
    start = time.time()
    funList = [getEquip, getRestrainRival, getFearRival, getSuitTeammate, getBadTeammate]
    text = getHtmlText(url)
    doc = getEtreeHtml(text)
    if doc is not None:
        # getEquip(doc)
        # getRestrainRival(doc)
        # getFearRival(doc)
        # getSuitTeammate(doc)
        # getBadTeammate(doc)
        for fun in funList:
            td = threading.Thread(target=fun, args=(doc,))
            td.start()
            td.join()
        end = time.time()
        print('用时:',end-start)
    else:
        print('网页抓取失败')
if __name__ == '__main__':
    url = 'http://www.dotamax.com/hero/detail/visage/'
    main(url)


