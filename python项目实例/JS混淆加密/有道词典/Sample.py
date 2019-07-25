import requests
from hashlib import md5
import time
import random
import json

def getHtmlText(url, text, ts, bv, salt, sign):
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3719.400 QQBrowser/10.5.3715.400'
        ,
        'cookie':'OUTFOX_SEARCH_USER_ID=-274804616@123.152.213.72; _ntes_nnid=471d163959900d4813d6f10c4d9c8832,1558599911774; P_INFO=m13616859570@163.com|1563539320|0|other|00&99|null&null&null#zhj&330600#10#0#0|136570&1|youdaodict_client|13616859570@163.com; JSESSIONID=aaaE-fwxS-4H7-NkpBNWw; OUTFOX_SEARCH_USER_ID_NCOO=419038431.62822616; ___rl__test__cookies=1564031619789',
        'referer':'http://fanyi.youdao.com/',
    }

    form_data={
        'i':text,
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':salt,
        'sign':sign,
        'ts':ts,
        'bv':bv,
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_REALTlME'
    }
    try:
        r =requests.post(url, headers=headers, data=form_data)
        r.raise_for_status()
        print('表单:',form_data, '网页内容:',r.text)
        return r.text
    except Exception as e:
        print(e)

def getTrans(text):
    info = json.loads(text)
    res = info['translateResult'][0][0]['tgt']
    print(res)
def get_ts():
    ts = int(time.time()*1000)
    return ts

def get_bv():
    appVersion = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3719.400 QQBrowser/10.5.3715.400'
    m = md5()
    m.update(appVersion.encode('utf-8'))
    bv = m.hexdigest()
    return bv

def get_salt(ts):
    num = int(random.random()*10)
    salt =str(ts)+str(num)
    return salt

def get_sign(text, salt):
    a = 'fanyideskweb'
    e = text
    i = salt
    b = 'n%A-rKaT5fb[Gy?;N5@Tj'
    s = a+e+i+b
    m = md5()
    m.update(s.encode('utf-8'))
    sign = m.hexdigest()
    return sign



if __name__ == '__main__':
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    # user_agent = '5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3719.400 QQBrowser/10.5.3715.400'
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3719.400 QQBrowser/10.5.3715.400'
    text = '真好啊都'
    ts = get_ts()
    bv = get_bv()
    salt = get_salt(ts)
    sign = get_sign(text,salt)
    text = getHtmlText(url,text,ts, bv, salt, sign)
    getTrans(text)
