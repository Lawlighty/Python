# {"isMusician":false,"userId":-1,"topComments":[],"code":200,"comments":[],"total":22964,"more":false}
import requests
import json
from wordcloud import WordCloud
import jieba #显示使用结巴词库来中文
import matplotlib.pyplot as plt
import sys
sys.path.append(r'C:\Users\Administrator\Desktop\python\Py_webSpider\github\IP_pond\Improve')
from getProxy import get_proxies

def getHtmlText(url):
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3719.400 QQBrowser/10.5.3715.400',
        'referer':'https://music.163.com/'
    }
    proxies = get_proxies()
    try:
        r = requests.get(url, headers=headers, proxies=proxies, timeout=5)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(e)

def ifHasCom(my_json):
    if my_json['more'] == True:
        return True
    else:
        return False

def getComments(my_json):
    comments = my_json['comments']
    for comment in comments:
        content = comment['content']
        yield content

def CiYun():
    with open('comments.txt', 'r') as f:
        text = f.read()

        # 结巴分词  返回的结构都是一个可迭代的 generator
        wordlist = jieba.cut(text)
        wl = ''.join(wordlist)

        # 设置词云
        wc = WordCloud(
            # 生成中文字的字体,必须要加,不然看不到中文
            font_path="C:\Windows\Fonts\STXINGKA.TTF",
            # 设置最大显示的词云数
            max_words=100,
            height=400,
            width=600,
            # 设置字体最大值
            max_font_size=100,
            # 设置有多少种随机生成状态，即有多少种配色方案
            random_state=30,
        )
        wordcloud = wc.generate(wl)
        img = wordcloud.to_image()
        img.show()
        img.save('Simple2.png')
    print('词云 finish')

def main():
    old_url = 'https://music.163.com/api/v1/resource/comments/R_SO_4_306967?limited=20&offset={}'
    for i in range(10):
        url = old_url.format(i*20)
        print('第{}页'.format(i+1))
        print('url',url)
        my_json = getHtmlText(url)
        if ifHasCom(my_json):
            for i in getComments(my_json):
                try:
                    with open('comments.txt','a+') as f:
                        f.write(i+'\t')
                except Exception as e:
                    continue
                # print(i)
        else:
            print('完毕')
            break
    print('爬取完毕finish')
    CiYun()

main()
