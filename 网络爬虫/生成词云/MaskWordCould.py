#生成那种有轮廓的词云

from wordcloud import WordCloud
import numpy as np
from PIL import Image
import jieba

#词云形状
mask = np.array(Image.open('mask2.png'))
with open('text.txt','r') as f:
    text = f.read()

    wordlist = jieba.cut(text)
    wl = ''.join(wordlist)

    wc = WordCloud(
        ## 添加遮罩层
        mask=mask,
        font_path="C:\Windows\Fonts\STXINGKA.TTF",
        max_words=2000,
        height=400,
        width=600,
        max_font_size=100,
        random_state=30,

    )
    myword = wc.generate(wl)
    img = myword.to_image()
    img.show()
    img.save('MaskCloud.png')
print('finish')