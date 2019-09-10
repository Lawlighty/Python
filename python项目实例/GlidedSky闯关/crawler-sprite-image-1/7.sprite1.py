import requests,re,base64
from lxml import etree
from fontTools.ttLib import TTFont
import tqdm

url = 'http://glidedsky.com/level/web/crawler-sprite-image-1?page=%s'
total = 0
headers = {
    'Cookie':"_ga=GA1.2.433101976.1567416273; footprints=eyJpdiI6IklxNFFuUERXN0lRREpZTzRpeUZVZEE9PSIsInZhbHVlIjoiaEgzeHBnNkFJMXoyYWNDRHhYZkUzT3BaY1pKbjZRWDVTbWlwYWxEeDNBaGFwTnNlV0c0RDJzTUdVcTlucGltTyIsIm1hYyI6IjdkNTUyOThjNmMzYTRmZjFkNzJiODI4MjYyZmJiNGRkYzljNWQ4ODA1ZTMyMTc2NTBhMGQyNTg1N2MwZjNhNjAifQ%3D%3D; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1567640761,1567771727,1567938460,1568105976; _gid=GA1.2.1245555099.1568105976; _gat_gtag_UA_75859356_3=1; XSRF-TOKEN=eyJpdiI6IlB0WFZcLzhKVm40Nmg3YmdCRVFqOGJBPT0iLCJ2YWx1ZSI6ImUyNnRIXC8zYmNnZk1TM05LS0pZQ25cL3k5XC9cL2JKRjZvNGVweENLemJMN0tzdzRIRHpjcE9EcjNOSWw4KzFHWDNoIiwibWFjIjoiMDI5MTQ2NjI3ZmEwYmI2NTVkYjMyOGRjMjJjN2EyN2IxN2JiMGRjMzE2MGVkZjU3MTMxZjg4MmI2NjlkNzhlZiJ9; glidedsky_session=eyJpdiI6ImlqOXE0OW51K2c2RGtPQ2N3UERKMGc9PSIsInZhbHVlIjoidk00Mys1d3pIZnBEK1Blb3Q3dFM5U1pqWHhUeW1KVG1rM0owdys2eHlVcUdKQlwvVUVkMHM3MFI0dkdaVTBlalYiLCJtYWMiOiIyYjNlMzc3YTJlOWFmNTNmM2ZkNWYyZmI0YTU1NGE1MTk5YTZhYjExYmIyNDk2NjdhM2RkZGE3NjkzNjhiNTY1In0%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1568105986",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4295.400'
}

def getPositionX(name):
    l = re.findall(r'.%s { background-position-x:-(\d+)px ' % (name), html.decode())
    if len(l) > 0:
        return int(l[0])
    return False

def getPositions():
    arr = re.findall(r'.\w+ { background-position-x:-(\d+)px ', html.decode())
    arr = list(set(arr))
    return sorted([int(x)  for x in arr])

def dealArr(arr):
    for idx, x in enumerate(arr):
        if idx > 0 and arr[idx] - arr[idx - 1] > 15:
            cha = arr[idx] - arr[idx - 1]
            if cha > 54: # 需要插入三个
                arr.insert(idx, arr[idx - 1] + 45)
                arr.insert(idx, arr[idx - 1] + 30)
                arr.insert(idx, arr[idx - 1] + 15)
            elif cha > 35:
                arr.insert(idx, arr[idx - 1] + 30)
                arr.insert(idx, arr[idx - 1] + 15)
            elif cha > 15:
                arr.insert(idx, arr[idx - 1] + 15)
# for u_idx in tqdm.tqdm(range(1, 1001)):
for u_idx in range(1, 1001):
    _url = url % (u_idx)
    html = requests.get(_url, headers=headers).content
    # html = open('temp/sprite1/%s.html' % u_idx, 'r').read().encode()
    # with open('temp/sprite1/%s.html' % u_idx ,'wb') as f:
    #     f.write(html)
    eHtml = etree.HTML(html)
    arr = getPositions()
    if arr[0] is not 0:
        arr.insert(0, 0)
    dealArr(arr)
    col = eHtml.xpath('//div[@class="col-md-1"]')
    for c in col:
        divs = c.xpath('./div')
        temp = [None,None,None]
        for idx, d in enumerate(divs):
            d_css = d.xpath('./@class')[0].split(' ')[0]
            left = getPositionX(d_css)
            d_idx = arr.index(left)
            temp[idx] = d_idx
        cur_total = 0
        temp.reverse()
        skip = 0
        for idx, x in enumerate(temp):
            if x is None:
                skip += 1
                continue
            cur_total += x * 10 ** (idx - skip)
        total += int(cur_total)
    print(str(u_idx) + ': ' + str(total))
print(total)
# 2790800