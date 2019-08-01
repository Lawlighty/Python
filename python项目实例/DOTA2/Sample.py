import requests
import sys
sys.path.append(r'C:\Users\Administrator\Desktop\python\Py_webSpider\github\IP_pond\Improve')
from getProxy import get_proxies

headers={
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3719.400 QQBrowser/10.5.3715.400',
    'Referer':'http://www.dotamax.com/',
}

def getHtmlText(url):
    # proxies = get_proxies()
    try:
        r = requests.get(url, headers=headers, timeout=5)
        r.raise_for_status()
        return r.text
    except Exception as e:
        print(e)

if __name__ == '__main__':
    url = 'http://www.dotamax.com/hero/detail/hero_items/skeleton_king/?skill=vh&ladder=y'
    text = getHtmlText(url)
    print(text)