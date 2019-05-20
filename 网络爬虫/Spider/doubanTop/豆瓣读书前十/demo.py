from Rank import RankMyDF
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv(r'C:\Users\Administrator\Desktop\python\Py_webSpider\github\Scrapy\doubanBook\dBook.csv')
now_data = RankMyDF(data)


plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] =False

title = list(now_data['title'])
xL = np.arange(10,110,10)

print(xL)
rating_nums = list(now_data['rating_nums'])

#设置画布大小
plt.figure(figsize=(18,7), dpi=80)
#柱体颜色  宽度
plt.bar(xL, rating_nums, color='cmyrgb',width=5,)

plt.tick_params(labelsize=10)
#y轴 刻度范围
plt.ylim([8,10])
# plt.tight_layout()
#x轴刻度文字
plt.xticks(xL, title)
plt.title('豆瓣图书评分前十',fontsize=30)
plt.xlabel('书名',fontsize=20)
plt.ylabel('评分',fontsize=20)


plt.show()