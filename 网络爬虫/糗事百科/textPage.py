# 爬取糗事百科text页面
import requests
from bs4 import BeautifulSoup

def getHtmlText(url, downloadCount = 3):
    print('Downloading:', url)
    kv = {"User-Agent": "Mozilla/5.0"}
    try:
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except :
        print('error')
        if downloadCount>0:
            print('try again-------------')
            return getHtmlText(url, downloadCount= downloadCount-1)

def parserHtml(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        mainbody = soup.find('div', attrs={"id":'content-left'})
        texts = mainbody.find_all('div', class_="article")

        output_format ="作者:{}\n性别:{}\t年龄:{}\n{}\n点赞:{}\t评论:{}\n----------这是分割线----------\n"

        for i in texts:
            #作者
            author = i.find('h2').text
            #作者年龄、性别
            author_info = i.find('div', attrs={'class':'articleGender'})
            #不是匿名
            if author_info:
                age = author_info.text
                if 'manIcon' in author_info['class']:
                    gender = '男'
                else:
                    gender = '女'
            else:
                age = '未知'
                gender = '未知'

            content = i.find('div', class_='content').find('span').text
            vote = i.find('span', class_='stats-vote').find('i', class_='number').text
            comment = i.find('span', attrs={'class':'stats-comments'}).find('i', attrs={'class':'number'}).text
            with open('qs1.txt', 'a+',encoding='utf-8') as f:
                f.write(output_format.format(author, gender, age, content, vote, comment))

    except :
            print('error')

#页面url
def getPageUrl(url):
    for i in range(1,14):
        newurl = url+ str(i)+'/'
        print('下载第{}页'.format(i))
        html = getHtmlText(newurl)
        parserHtml(html)
        print('第{}页加载完成'.format(i))

if __name__ == '__main__':
    url = 'https://www.qiushibaike.com/text/'
    # html = getHtmlText(url)
    # parserHtml(html)
    getPageUrl(url)
    print('finish ')
