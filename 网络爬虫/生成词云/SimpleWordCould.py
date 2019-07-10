from wordcloud import WordCloud
import jieba #显示使用结巴词库来中文
import matplotlib.pyplot as plt


with open('text.txt','r') as f:
    text = f.read()

    # 结巴分词  返回的结构都是一个可迭代的 generator
    wordlist = jieba.cut(text)
    wl = ''.join(wordlist)

    # 设置词云
    wc = WordCloud(
        # 生成中文字的字体,必须要加,不然看不到中文
        font_path="C:\Windows\Fonts\STXINGKA.TTF",
        # 设置最大显示的词云数
        max_words=2000,
        height= 400,
        width= 600,
        # 设置字体最大值
        max_font_size=100,
        # 设置有多少种随机生成状态，即有多少种配色方案
        random_state=30,
    )
    wordcloud = wc.generate(wl)
    img = wordcloud.to_image()
    img.show()
    img.save('Simple.png')
print('finish')