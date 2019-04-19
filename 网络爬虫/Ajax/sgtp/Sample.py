import requests
import json
import time
import random
import os
import sys
sys.path.append(r'C:\Users\Administrator\Desktop\python\Py_webSpider\github\IP_pond\Improve')
from getProxy import get_proxies

proxies = get_proxies()

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400',
        'Rerferer': "https://pic.sogou.com/",

    }

cookies = {
    'Cookie': 'SUID=45F5987B2013940A000000005CAAB127; IPLOC=CN3302; SUV=0017755C7B98F5455CB041D0A9992686; usid=rFf2LYEx3vIgYSvd; SNUID=F0402ECDB6B3337577E6D4FCB6EF3DF0; JSESSIONID=aaaES0h35w0xX9Poyl0Ow; tip_show_home_search=20190419; tip_show=20190419; pgv_pvi=4300803072; pgv_si=s6583307264; sct=2; tip_show_detail=20190419; ld=Pkllllllll2tmgYHlllllVhiNA1lllllWi0CSyllll9lllll9Zlll5@@@@@@@@@@'
}
def getHtmlText(url):

    try:
        r = requests.get(url=url, headers=headers, proxies=proxies, cookies=cookies)
        r.raise_for_status()
        # r.encoding = 'utf-8'
        return r.text

    except Exception as e:
        print(e)

#创建文件夹
def create_file(name):
    if not os.path.exists(name):
        os.makedirs(name)


#判断是否为图片拓展名
def ifPic(pname):
    ex = re.compile("\.(jpg|jpeg|png|bmp|BMP|JPG|PNG|JPEG)$")
    if not re.search(ex,pname):
        pname=pname+'.jpg'
    return pname

def downLoad(fileName, html):
    try:
        create_file('pic/{}'.format(fileName))
        content = json.loads(html)
        items = content['items']
        for item in items:
            # title = item.get('oriTitle','wu')
            # title = title.split('/')[-1]
            pic_url = item.get('pic_url')
            title = pic_url.split('/')[-1]
            title = ifPic(title)
            new_url =pic_url[:4]+pic_url[5:]
            pic = requests.get(new_url)

            with open('pic/{}/{}'.format(fileName,title),'wb') as f:
                f.write(pic.content)
                print('{}保存成功'.format(title))
            s = requests.session()
            s.keep_alive = False
            time.sleep(random.randint(1,3))

    except Exception as e:
        print(e)

if __name__ == '__main__':
    query = str(input('输入关键词>'))
    page_num = int(input('输入爬取页数>'))
    url = 'https://pic.sogou.com/pics?query={}&mode=1&start=0&reqType=ajax&reqFrom=result&tn=0'.format(query)
    for i in range(0,page_num):
        url = 'https://pic.sogou.com/pics?query={}&mode=1&start={}&reqType=ajax&reqFrom=result&tn=0'.format(query, i*48)
        html = getHtmlText(url)
        downLoad(query, html)
        time.sleep(random.randint(1,3))

    print('finish')

