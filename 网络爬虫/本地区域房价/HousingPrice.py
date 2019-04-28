# 安居客爬取本地房价信息
import requests
from lxml.html import fromstring
import lxml
import time
import random
import openpyxl
import sys
sys.path.append(r'C:\Users\Administrator\Desktop\python\Py_webSpider\github\IP_pond\Improve')
import getProxy
import cssselect
from bs4 import BeautifulSoup
url = 'https://sx.fang.anjuke.com/loupan/yuechengqu/'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400',
    'Referer':'https://sx.fang.anjuke.com/loupan/yuechengqu/',
}
cookies = {
'cookie':'ctid=66; aQQ_ajkguid=DE7D9768-0C31-4978-1D21-SX0428133507; sessid=1ACFCBE2-691C-D1FA-3461-SX0428133507; isp=true; lps=http%3A%2F%2Fuser.anjuke.com%2Fajax%2FcheckMenu%2F%3Fr%3D0.8617607606270921%26callback%3DjQuery1113003545128319064261_1556429737063%26_%3D1556429737064%7Chttps%3A%2F%2Fsx.fang.anjuke.com%2Floupan%2F%3Fpi%3Dbaidu-cpcaf-sx-tyongsx1%26kwid%3D94538308235; twe=2; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1556429737; 58tj_uuid=bd822b30-9606-4160-b237-b5d4e97b0bee; init_refer=https%253A%252F%252Fwww.baidu.com%252Fbaidu.php%253Fsc.Ks000001qLT2daZnZ-PnF6VfdHyzXE-ljY0UrvaFUKIRtpg9KJcd9o4fAIs3sHFn5I15dnr1cxvmqRXRvA2Fo_GSHwoy0YExi11QSADpD8TcHS8v_A8rvHYqMoR84_ePK0LVZrcC5YafivARH99CJDgO8zUPHBM3mU7GkjXDVYUvWFedqTpq8v7GfSFBLV_Z5Bv_RPU8MjGjGACins.DR_NR2Ar5Od66Wl5Qy1hthm_8jViBaBeKWuB6e3L_g_3_AXZZa1o1kqAX9CIhWl2SEUsmhPOu83erPh1FkLQDkELIrOklXrH-JuIz3qis1f_XPMZBC0.U1Yk0ZDqzI1fzeXOEP_0mywkXHLFLPjQVeStvsK9uZ7Y5Hc0TA-W5HD0IjLFLPjQzVaLEe1U0A-V5HczPfKM5yq-TZnk0ZNG5yF9pywdUAY0TA-b5Hnz0APGujYzP1T0UgfqnH0kPdtknjD4g1DsnHPxn10knNt1PW0k0AVG5H00TMfqP16L0ANGujY0mhbqnW0Y0AdW5H6srHRsPHRkPNtknj0kg1c4rHR1nHczn1IxnH01g100TgKGujY1n6Kkmv-b5HcLPsKzuLw9u1Ys0A7B5HKxn0K-ThTqn6KsTjYs0A4vTjYsQW0snj0snj0s0AdYTjYs0AwbUL0qn0KzpWYs0Aw-IWdsmsKhIjYs0ZKC5H00ULnqn0KBI1Yz0A4Y5H00TLCq0A71gv-bm1dsTzdCu0KYIgnqnHR4nHTzrHR3Pj6LrHbsn104Pj60ThNkIjYkPHRvPjc4PWb4nHcd0ZPGujY4ujFbPWFWuj0snjRLnjb30AP1UHdDwHwKfbuawbuDfbPKPDnY0A7W5HD0TA3qn0KkUgfqn0KkUgnqn0KlIjYs0AdWgvuzUvYqn7tsg1Kxn7ts0Aw9UMNBuNqsUA78pyw15HKxn7tsg1nkn1R3rjuxn0Ksmgwxuhk9u1Ys0AwWpyfqn0K-IA-b5iYk0A71TAPW5H00IgKGUhPW5H00Tydh5HDv0AuWIgfqn0KhXh6qn0Khmgfqn0KlTAkdT1Ys0A7buhk9u1Yk0Akhm1Ys0AqY5H00ULFsIjYsc10Wc10Wn0KWThnqn1nLrjc%2526word%253D%2525E7%2525BB%25258D%2525E5%252585%2525B4%2525E6%252588%2525BF%2525E4%2525BB%2525B7%2526ck%253D3354.1.58.325.187.335.173.595%2526shh%253Dwww.baidu.com%2526sht%253D95697632_hao_pg%2526us%253D1.0.1.0.0.0.0%2526bc%253D110101; new_uv=1; wmda_uuid=796de203d230c5efa426350a8e8970bd; wmda_new_uuid=1; wmda_session_id_8788302075828=1556429737519-93e198a7-972b-71b9; wmda_visited_projects=%3B8788302075828; als=0; new_session=0; __xsptplusUT_8=1; __xsptplus8=8.1.1556429738.1556430628.14%232%7Cwww.baidu.com%7C%7C%7C%25E7%25BB%258D%25E5%2585%25B4%25E6%2588%25BF%25E4%25BB%25B7%7C%23%23Czq2qvFzGKNhXO64wbNMLCm0VCYmDeIi%23; Hm_lpvt_c5899c8768ebee272710c9c5f365a6d8=1556430628'
}


proxies = getProxy.get_proxies()


def getHtmlText(url):
    try:
        r = requests.get(url, headers=headers, proxies=proxies)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except Exception as e:
        print(e)

def getInfo(html, fname):
    wb = openpyxl.load_workbook(fname)
    soup = BeautifulSoup(html, 'html.parser')
    list_items = soup.find('ul', id='houselist-mod-new').find_all('li',class_='list-item')

    for item in list_items:
        list = []
        title = item.find('a')['title']
        area = item.find('div',class_='details-item').find_all('span')[1].text
        unit_price = item.find('div',class_='pro-price').find_all('span')[0].text
        total_price = item.find('div',class_='pro-price').find_all('span')[1].text
        url = item.find('a')['href']
        list.append(title)
        list.append(area)
        list.append(unit_price)
        list.append(total_price)

        #追加数据
        AddinfoXlsx(wb, list)

        print(title)
        print(area)
        print(unit_price)
        print(total_price)
        print(url)
        print('*'*20)

    SaveXlsx(wb, fname)

def Createxlsx(fname):
    nameList= ['title','area','unit_price','total_price','url']
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title='绍兴市越城区二手房'
    ws.append(nameList)
    wb.save(fname)

def SaveXlsx(wb, fname):
    wb.save(fname)


def AddinfoXlsx(wb, info):

    ws = wb.active
    ws.append(info)




def main(url):
    fname = str(input('输入创建的xlsx文件名'))
    fname = fname+'.xlsx'
    #创建xlsx文件框架
    Createxlsx(fname)

    for i in range(1,100):
        url = 'https://shaoxing.anjuke.com/sale/yuecheng/p{}'.format(i)
        if getHtmlText(url):
            html = getHtmlText(url)
            getInfo(html, fname)
        else:
            print('爬取完毕')



if __name__ == '__main__':
    url = 'https://shaoxing.anjuke.com/sale/yuecheng/'
    main(url)