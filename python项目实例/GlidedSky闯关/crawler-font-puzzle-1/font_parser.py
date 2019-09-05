from fontTools.ttLib import TTFont

my_font = TTFont('3ZrAeF.woff')
my_font.saveXML('3ZrAeF.xml')
# 读取字体的映射关系
# 参数'cmap' 表示汉字对应的映射 为unicode编码
uni_list = my_font['cmap'].tables[0].ttFont.getGlyphOrder()
# .notdef 并不是汉字的映射， 而是表示字体家族名称。真是数据是从下标 1 开始
uni_list = uni_list[2:]
print(uni_list,'len:',len(uni_list))

utf_list = [eval(r"'uni" + x[3:]+ "'") for x in uni_list]
print(utf_list,'len:',len(utf_list))

#对应的 字符列表
char_list= [u'0',u'1',u'2',u'3',u'4',u'5',u'6',u'7',u'8',u'9']
print('finish')


woff_list = ['cid00017', 'cid00018', 'cid00019', 'cid00020', 'cid00021', 'cid00022', 'cid00023', 'cid00024', 'cid00025', 'cid00026']
xml_list =  ['uni0035',    'uni0035',   'uni0035',   'uni0035',  'uni0035',  'uni0035',  'uni0035',   'uni0035',   'uni0035','uni0035']
number_list = [0,           1,          2,              3,          4,          5,              6,              7,          8,          9]

font_info = [
    {'code':'uni0035','num':0},
    {'code':'uni0037','num':1},
    {'code':'uni0036','num':2},
    {'code':'uni0039','num':3},
    {'code':'uni0034','num':4},
    {'code':'uni0032','num':5},
    {'code':'uni0033','num':6},
    {'code':'uni0031','num':7},
    {'code':'uni0030','num':8},
    {'code':'uni0038','num':9},
]


if __name__ == '__main__':
    pass
    a = '18+9'
    print(eval(a))