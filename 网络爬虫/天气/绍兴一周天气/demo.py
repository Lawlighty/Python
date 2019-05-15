#获取前三天天气: url= http://www.tianqihoubao.com/lishi/shaoxing/month/年月(xxxxyy).html
#获取今天及之后三天天气: url= http://www.weather.com.cn/weather/101210501.shtml
#近期 七天 最高气温变化图

import matplotlib.pyplot as plt
import requests
import time
import datetime
import re
import tqdm
from pyquery import PyQuery as pq
from lxml import etree
import sys
sys.path.append(r'C:\Users\Administrator\Desktop\python\Py_webSpider\github\IP_pond\Improve')
from getProxy import get_proxies

def getNowDate():
    nowdate = str(datetime.datetime.now()).split(' ')[0].split('-')
    year = int(nowdate[0])
    month = int(nowdate[1])
    date = int(nowdate[2])

    return year,month,date


def getHtmlText(url, times=5):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3469.400',
        'Referer':"www.baidu.com",
        'Connection': 'close',
    }
    cookies = {
        'cookie':'id=220793df29bd00a4||t=1554689493|et=730|cs=002213fd48ec54ab198b47c57e',
    }
    proxies= get_proxies()

    try:
        s = requests.session()
        s.keep_alive = False
        r = requests.get(url, headers=headers, proxies=proxies, cookies=cookies)
        r.raise_for_status()
        r.encoding = 'gb2312'
        return r.text
    except Exception as e:
        if times>0:
            print('重试....')
            time.sleep(3)
            return getHtmlText(url, times=times-1)
        else:
            print(e)

#从记录网站获得之前x天信息
def getBefinfo(html,x):
    doc = pq(html)
    doc = etree.HTML(str(doc))
    trs = doc.xpath('//div[@id="content"]/table/tr')[(-int(x)):]
    # print('trs:',trs)
    temp_list = []
    for tr in trs:
        temp = tr.xpath('td[3]/text()')[0].split('/')[0]
        temp = int(re.sub('℃','',temp))

        temp_list.append(temp)

    return temp_list

# 获得今天及之后三天 气温
def getAfterInfo(html):
    doc = pq(html)
    doc = etree.HTML(str(doc))

    temp_list = []
    todays = int(doc.xpath('//*[@id="7d"]/ul/li[1]/p[2]/span/text()')[0])
    onedayAf = int(doc.xpath('//*[@id="7d"]/ul/li[2]/p[2]/span/text()')[0])
    twodayAf = int(doc.xpath('//*[@id="7d"]/ul/li[3]/p[2]/span/text()')[0])
    threedatAf = int(doc.xpath('//*[@id="7d"]/ul/li[4]/p[2]/span/text()')[0])
    temp_list.append(todays)
    temp_list.append(onedayAf)
    temp_list.append(twodayAf)
    temp_list.append(threedatAf)

    return  temp_list

def getMyList():
    year, month, date = getNowDate()

    #需从上个月获得三天数据
    if date == 1 :
        if month<=10:
            if month >1:
                month = month-1
                month = '0'+'{}'.format(month)
                ym = '{}{}'.format(year,month)

                old_url = 'http://www.tianqihoubao.com/lishi/shaoxing/month/{}.html'.format(ym)
                html1 = getHtmlText(old_url)
                list1 = getBefinfo(html1, 3)

                new_url = 'http://www.weather.com.cn/weather/101210501.shtml'
                html2 = getHtmlText(new_url)
                list2 = getAfterInfo(html2)

                myList = list1 + list2
                return myList

            else:
                year = year-1
                month = 12
                ym = '{}{}'.format(year,month)

                old_url = 'http://www.tianqihoubao.com/lishi/shaoxing/month/{}.html'.format(ym)
                html1 = getHtmlText(old_url)
                list1 = getBefinfo(html1,3)

                new_url = 'http://www.weather.com.cn/weather/101210501.shtml'
                html2 = getHtmlText(new_url)
                list2 = getAfterInfo(html2)

                myList = list1+list2
                return myList
        else:
            month = month-1
            ym = '{}{}'.format(year,month)

            old_url = 'http://www.tianqihoubao.com/lishi/shaoxing/month/{}.html'.format(ym)
            html1 = getHtmlText(old_url)
            list1 = getBefinfo(html1, 3)
            new_url = 'http://www.weather.com.cn/weather/101210501.shtml'
            html2 = getHtmlText(new_url)
            list2 = getAfterInfo(html2)

            myList = list1 + list2
            return myList

    # 需从上个月获得两天数据 + 这个月一天
    elif date == 2:
        if month <= 10:
            if month > 1:
                ym = '{}{}'.format(year, month)
                old_url = 'http://www.tianqihoubao.com/lishi/shaoxing/month/{}.html'.format(ym)
                html0 = getHtmlText(old_url)
                list0 = getBefinfo(html1, 1)

                month = month - 1
                month = '0'+'{}'.format(month)
                ym = '{}{}'.format(year, month)

                old_url = 'http://www.tianqihoubao.com/lishi/shaoxing/month/{}.html'.format(ym)
                html1 = getHtmlText(old_url)
                list1 = getBefinfo(html1, 2)

                new_url = 'http://www.weather.com.cn/weather/101210501.shtml'
                html2 = getHtmlText(new_url)
                list2 = getAfterInfo(html2)

                myList = list1 + list0+ list2
                return myList

            else:
                ym = '{}{}'.format(year, month)
                old_url = 'http://www.tianqihoubao.com/lishi/shaoxing/month/{}.html'.format(ym)
                html0 = getHtmlText(old_url)
                list0 = getBefinfo(html1, 1)

                year = year - 1
                month = 12
                ym = '{}{}'.format(year, month)

                old_url = 'http://www.tianqihoubao.com/lishi/shaoxing/month/{}.html'.format(ym)
                html1 = getHtmlText(old_url)
                list1 = getBefinfo(html1, 2)

                new_url = 'http://www.weather.com.cn/weather/101210501.shtml'
                html2 = getHtmlText(new_url)
                list2 = getAfterInfo(html2)

                myList = list1+ list0 + list2
                return myList
        else:
            ym = '{}{}'.format(year, month)
            old_url = 'http://www.tianqihoubao.com/lishi/shaoxing/month/{}.html'.format(ym)
            html0 = getHtmlText(old_url)
            list0 = getBefinfo(html1, 1)

            month = month - 1
            ym = '{}{}'.format(year, month)

            old_url = 'http://www.tianqihoubao.com/lishi/shaoxing/month/{}.html'.format(ym)
            html1 = getHtmlText(old_url)
            list1 = getBefinfo(html1, 2)
            new_url = 'http://www.weather.com.cn/weather/101210501.shtml'
            html2 = getHtmlText(new_url)
            list2 = getAfterInfo(html2)

            myList = list1+list0 + list2
            return myList

    # 需从上个月获得一天数据
    elif date == 3:
        if month <= 10:
            if month > 1:
                ym = '{}{}'.format(year, month)
                old_url = 'http://www.tianqihoubao.com/lishi/shaoxing/month/{}.html'.format(ym)
                html0 = getHtmlText(old_url)
                list0 = getBefinfo(html1, 2)

                month = month - 1
                month = '0'+'{}'.format(month)
                ym = '{}{}'.format(year, month)

                old_url = 'http://www.tianqihoubao.com/lishi/shaoxing/month/{}.html'.format(ym)
                html1 = getHtmlText(old_url)
                list1 = getBefinfo(html1, 1)

                new_url = 'http://www.weather.com.cn/weather/101210501.shtml'
                html2 = getHtmlText(new_url)
                list2 = getAfterInfo(html2)

                myList = list1 + list0 + list2
                return myList

            else:
                ym = '{}{}'.format(year, month)
                old_url = 'http://www.tianqihoubao.com/lishi/shaoxing/month/{}.html'.format(ym)
                html0 = getHtmlText(old_url)
                list0 = getBefinfo(html1, 2)

                year = year - 1
                month = 12
                ym = '{}{}'.format(year, month)

                old_url = 'http://www.tianqihoubao.com/lishi/shaoxing/month/{}.html'.format(ym)
                html1 = getHtmlText(old_url)
                list1 = getBefinfo(html1, 1)

                new_url = 'http://www.weather.com.cn/weather/101210501.shtml'
                html2 = getHtmlText(new_url)
                list2 = getAfterInfo(html2)

                myList = list1 + list0 + list2
                return myList
        else:
            ym = '{}{}'.format(year, month)
            old_url = 'http://www.tianqihoubao.com/lishi/shaoxing/month/{}.html'.format(ym)
            html0 = getHtmlText(old_url)
            list0 = getBefinfo(html1, 2)

            month = month - 1
            ym = '{}{}'.format(year, month)

            old_url = 'http://www.tianqihoubao.com/lishi/shaoxing/month/{}.html'.format(ym)
            html1 = getHtmlText(old_url)
            list1 = getBefinfo(html1, 1)
            new_url = 'http://www.weather.com.cn/weather/101210501.shtml'
            html2 = getHtmlText(new_url)
            list2 = getAfterInfo(html2)

            myList = list1+list0 + list2
            return myList
    else:
        if month<10:
            month = '0'+'{}'.format(month)
        else:
            month = month

        ym = '{}{}'.format(year, month)

        old_url = 'http://www.tianqihoubao.com/lishi/shaoxing/month/{}.html'.format(ym)
        html1 = getHtmlText(old_url)
        list1 = getBefinfo(html1, 3)
        new_url = 'http://www.weather.com.cn/weather/101210501.shtml'
        html2 = getHtmlText(new_url)
        list2 = getAfterInfo(html2)

        myList = list1 + list2
        return myList

def Paint(ylist):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    xlist = range(7)
    date = ['大前天', '前天', '昨天', '今天', '明天', '后天', '大后天']
    plt.xticks(xlist, date)

    plt.plot(xlist, ylist, marker='o', markerfacecolor='r', label='温度折线')

    plt.legend()  # 对应label=""
    plt.xlabel('日期')
    plt.ylabel('温度/℃')
    plt.title('地区连续七天气温变化图')

    for x, y in zip(xlist, ylist):
        plt.text(x, y * 1.005, '{}℃'.format(y), ha='center', va='bottom', fontsize=10)

    plt.show()


if __name__ == '__main__':
    ylist = getMyList()
    Paint(ylist)

