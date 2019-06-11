import requests


def getInfo(url):
    # proxy = '106.12.24.168:8118'
    proxy = '112.85.167.44:9999'
    proxies = {
        'http':'http://'+proxy,
        'https':'https://'+proxy,
    }
    # proxies={
    #     'http':'http://112.85.167.44:9999'
    # }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400'
    }
    try:
        r = requests.get(url, headers=headers,proxies=proxies)
        r.raise_for_status()
        print(r.text)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    url = 'http://httpbin.org/get'
    getInfo(url)