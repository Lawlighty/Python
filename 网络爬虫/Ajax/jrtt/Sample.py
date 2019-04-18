import requests
import get_as_cp
import json
import openpyxl
import time
import sys
import random
sys.path.append(r'C:\Users\Administrator\Desktop\python\Py_webSpider\github\IP_pond\Improve')
#获取随机ip
import getProxy

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400',
    'Rerferer':'https://www.toutiao.com/ch/news_hot/'
}
cookies={
    'tt_webid':'6680466013496083979'
}

proxies = getProxy.get_proxies()

start_url = 'https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1&max_behot_time='
max_behot_time = 0
tadrequire = 'true'

def getHtmlText(url):
    try:
        r = requests.get(url=url, headers=headers,cookies=cookies, proxies=proxies)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text

    except Exception as e:
        print(e)

def get_Info(resp):

    try:
        info_cont = []
        info_List = resp['data']
        max_behot_time = resp['next']['max_behot_time']
        for i in info_List:
            info = []
            #标题
            title = i.get('title','无')
            #摘要
            abstract = i.get('abstract','无')
            #来源
            source = i.get('source','无')
            #新闻相对url
            source_url = i.get('source_url','无')
            #新闻完整连接url
            s_full_url = 'https://www.toutiao.com'+source_url
            info.append(title)
            info.append(abstract)
            info.append(source)
            info.append(s_full_url)

            print('标题:',i.get('title','wu'))
            print('摘要:',i.get('abstract','wu'))

            info_cont.append(info)
        ascp = get_as_cp.get_as_cp()
        #获得下个url
        next_url = 'https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1&max_behot_time={}&max_behot_time_tmp={}&tadrequire=true&as={}&cp={}'.format(max_behot_time, max_behot_time, ascp['as'], ascp['cp'])
        return info_cont, next_url
    except Exception as e:
        print(e)

def intoXlsx(wb,info):
    # wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'news_hot'
    for row in info:
        ws.append(row)
    # wb.save('New_hot.xlsx')

def main(pageNum= 3):
    ascp = get_as_cp.get_as_cp()
    #初始url
    url = start_url+str(max_behot_time)+'&max_behot_time_tmp='+str(max_behot_time)+'&tadrequire=true&as='+ascp['as']+'&cp='+ascp['cp']
    # url = 'https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1252C4B370D07C&cp=5CB71D20B75CCE1&_signature=YzyWJgAAP440C959xqHQXGM8lj'
    wb = openpyxl.Workbook()
    for i in range(0,pageNum):

        resp = getHtmlText(url)
        text = json.loads(resp)
        info ,url = get_Info(text)

        intoXlsx(wb, info)
        time.sleep(random.randint(1,5))
        print('*'*100)
    wb.save('New_hot.xlsx')

if __name__ == '__main__':
    pageNum = int(input('输入爬取深度>'))
    main(pageNum=pageNum)
