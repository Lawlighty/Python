# 获得csv 文件中的所有网址
import pandas as pd

def getUrlList():
    dataf = pd.read_csv(r'C:\Users\Administrator\Desktop\python\Py_webSpider\Four\ZipOP\top-1m.csv')
    dataf = dataf['google.com']

    urllist = []
    urllist.append('http://google.com')
    s = 'http://'
    for i in dataf:
        i = s+i
        urllist.append(i)

    return urllist
