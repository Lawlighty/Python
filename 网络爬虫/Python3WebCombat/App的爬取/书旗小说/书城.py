import json
import requests
import pymongo

# 书城精选汇聚推荐
url = 'http://bookstoreapi.shuqireader.com/eva_bookstore/v1/module/query?appId=17&channelId=111111&versionId=4.0.9.0&placeId=111111&ver=190114&userId=1199721128&imei=AE3DF1F5200FE9BC2DA2433E1384AF85DFD02B62&sn=7C16F0EEA5973E3F393587B3C5AE5EDBD39ED90B&func_id=20%2C24%2C11%2C19%2C18%2C11%2C19%2C33%2C11%2C19%2C33%2C9%2C33%2C11%2C19%2C33%2C20%2C33%2C11%2C19%2C33%2C11%2C19%2C33&orderid=2%2C7%2C8%2C9%2C16%2C20%2C21%2C22%2C23%2C24%2C25%2C31%2C32%2C33%2C34%2C35%2C36%2C38%2C39%2C40%2C47%2C48%2C49%2C50&skinId=999&skinVersion=1&skinVersionPrefix=1&classId=23&lifecycle=11997211284631&utdid=XFf3Aouw4HUDADcSC7iryEnY&timestamp=1561365574643&key=shuqiapi&sign=A1699741FB3D53B6DACF6AF5F89B2A6A&_=1561365574654'
def getText(url):
    headers={
        'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 Shuqi (iPhone7,2__shuqi__v4.0.9.0)',
    }
    try:
        r = requests.get(url=url, headers=headers, verify=False)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(e)

def getinfo(json,collection):
    if json:
        info = json.get('data').get('module')[3]['content']
        print('精选汇聚')
        for i in info:
            bookname = i.get('bookname')
            introduction = i.get('introduction')
            author_name = i.get('author_name')
            stat_name = i.get('stat_name')
            class_name = i.get('class_name')
            data = {
                'bookname':bookname,
                'introduction':introduction,
                'author_name':author_name,
                'stat_name':stat_name,
                'class_name':class_name,
            }
            collection.insert(data)
            print('保存成功')
            print('书名:{}    介绍:{}   作者:{}   状态:{}   类型:{}'.format(bookname, introduction, author_name, stat_name, class_name))


def conMangoDB():
    clinet = pymongo.MongoClient(host='localhost',port=27017)
    db = clinet['shuqixiaoshuo']
    collection = db['精选汇聚']
    return collection

if __name__ == '__main__':
    # url = 'http://bookstoreapi.shuqireader.com/eva_bookstore/v1/module/query?appId=17&channelId=111111&versionId=4.0.9.0&placeId=111111&ver=190114&userId=1199721128&imei=AE3DF1F5200FE9BC2DA2433E1384AF85DFD02B62&sn=7C16F0EEA5973E3F393587B3C5AE5EDBD39ED90B&func_id=20%2C24%2C11%2C19%2C18%2C11%2C19%2C33%2C11%2C19%2C33%2C9%2C33%2C11%2C19%2C33%2C20%2C33%2C11%2C19%2C33%2C11%2C19%2C33&orderid=2%2C7%2C8%2C9%2C16%2C20%2C21%2C22%2C23%2C24%2C25%2C31%2C32%2C33%2C34%2C35%2C36%2C38%2C39%2C40%2C47%2C48%2C49%2C50&skinId=999&skinVersion=1&skinVersionPrefix=1&classId=23&lifecycle=11997211284631&utdid=XFf3Aouw4HUDADcSC7iryEnY&timestamp=1561365574643&key=shuqiapi&sign=A1699741FB3D53B6DACF6AF5F89B2A6A&_=1561365574654'
    url = 'http://bookstoreapi.shuqireader.com/eva_bookstore/v1/stencil/query?appId=17&channelId=111111&versionId=4.0.9.0&placeId=111111&ver=190114&userId=1199721128&imei=AE3DF1F5200FE9BC2DA2433E1384AF85DFD02B62&sn=7C16F0EEA5973E3F393587B3C5AE5EDBD39ED90B&type=1&preload=8&skinId=999&skinVersion=1&skinVersionPrefix=1&classId=23&lifecycle=11997211289502&utdid=XFf3Aouw4HUDADcSC7iryEnY&timestamp=1561363939505&key=shuqiapi&sign=CCB4EC07DCDFDA2C63308A0B6D8B1553&_=1561363939523'
    collection = conMangoDB()
    json = getText(url)
    getinfo(json,collection)
