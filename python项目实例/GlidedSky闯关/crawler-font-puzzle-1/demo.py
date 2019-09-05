import requests
from lxml import etree
# import font_parser
import re
from fontTools.ttLib import TTFont
from 获取映射关系dic import Map_Cmap_Number,Get_Best_Cmap,Get_number_Cmap
# utf_list = font_parser.utf_list
# char_list = font_parser.char_list

class myC:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400',

        }
        self.login_url = 'http://glidedsky.com/login'
        self.target_url = 'http://glidedsky.com/level/web/crawler-basic-1'

    def get_token(self):
        resp = self.session.get(self.login_url, headers=self.headers, timeout=10).text
        doc = etree.HTML(str(resp))
        _token = doc.xpath('//div[@class="card-body"]/form/input/@value')[0]
        return _token

    def login_in(self, email, password):
        form_data = {
            '_token':self.get_token(),
            'email':email,
            'password':password,
        }
        try:
            resp = self.session.post(self.login_url, headers=self.headers,data= form_data, timeout=5)
            resp.raise_for_status()
            return resp.text

        except Exception as e:
            print(e)

    def getHtmlText(self,url):
        try:
            resp = self.session.get(url, headers=self.headers, timeout=10)
            resp.raise_for_status()
            return resp.text
        except Exception as e:
            print(e)

    def get_content(self,text):
        doc = etree.HTML(str(text))
        contetn_list = doc.xpath('//div[@class="row"]/div//text()')
        contetn = '+'.join(contetn_list)
        return contetn

    # 获取字体的连接文件 并下载 获得映射
    def get_fonts_url(self, text):
        fonts_url = re.search('url(.*?) format', text).group(1)[2:-2]
        print('字体文件:',fonts_url)
        resp = requests.get(fonts_url, headers=self.headers).content
        with open('myfont.woff','wb') as f:
            f.write(resp)
        map_cmap_number = Map_Cmap_Number(Get_Best_Cmap,Get_number_Cmap)
        return map_cmap_number

    def Sub_cont(self,map_cmap_number, contetn):
        new_content = ''
        for k, v  in map_cmap_number.items():
            if k in contetn:
                new_content = re.sub(k,v,content)
        return new_content

    def Sum(self, new_content):
        return eval(new_content)

    # 解析字体
    # def parser_font(self,fonts_url):
    #     response = requests.get(fonts_url, headers=self.headers).content
    #     with open('fonts.woff', 'wb') as f:
    #         f.write(response)
    #     # 解析字体库
    #     font = TTFont('fonts.woff')
    #     # 读取字体的映射关系
    #     uni_list = font['cmap'].tables[0].ttFont.getGlyphOrder()
    #     # 转换格式
    #     # utf_list = [eval(r"u'\u" + x[3:] + "'") for x in uni_list[2:]]
    #     utf_list = uni_list[2:]
    #     # 被替换的字体的列表
    #     # word_list = [u'0',u'1',u'2',u'3',u'4',u'5',u'6',u'7',u'8',u'9']
    #     word_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    #     return utf_list,word_list

    # def Sub_font(self, content,utf_list, word_list):
    #     for i in range(len(utf_list)):
    #         content = content.replace(utf_list[i], word_list[i])
    #     return content

    # def get_number_str(self,text):
    #     nList = []
    #     doc = etree.HTML(str(text))
    #     rows = doc.xpath('//div[@class="row"]/div')
    #     for i in rows:
    #         num = i.xpath('./text()')[0]
    #         nList.append(num)
    #     myStr = '+'.join(nList)
    #     return myStr
    #
    # def Sub_nList(self, myStr):
    #     for i in range(len(utf_list)):
    #         myStr = str(myStr).replace(utf_list[i], char_list[i])
    #     return myStr

if __name__ == '__main__':

    mc = myC()
    mc.login_in('13616859570@163.com','liyixin123')
    url = 'http://glidedsky.com/level/web/crawler-font-puzzle-1?page=1'
    text = mc.getHtmlText(url)
    map_cmap_number = mc.get_fonts_url(text)
    print('映射:',map_cmap_number)
    content = mc.get_content(text)
    print('当前内容:',content)
    new_content = mc.Sub_cont(map_cmap_number, content)
    print('当前xxxxx内容:', new_content)
    # sum = mc.Sum(new_content)
    # print(sum)
    """
    # myStr = mc.get_number_str(text)
    # ssss = mc.Sub_nList(myStr)
    # print(ssss)
    url = mc.get_fonts_url(text)
    print('字体地址:',url)
    content = mc.get_content(text)
    print('内容:',content)
    utf_list, word_list = mc.parser_font(url)
    new_contetn = mc.Sub_font(content,utf_list,word_list)
    print('替换后的内容:', new_contetn)
    # print(url)
    """