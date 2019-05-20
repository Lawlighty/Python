import matplotlib.pyplot as plt
import pandas as pd


# data = pd.read_csv(r'C:\Users\Administrator\Desktop\python\Py_webSpider\github\Scrapy\doubanBook\dBook.csv')
# print(data)
#
# print('*'*20)
# # ascending=False 逆序
# data2 = data.sort_values(by='rating_nums', ascending=False)
# print(data2)
#
# print('*'*20)
# #获得 评分排名前十
# data3 = data2.iloc[0:10]
# print(data3)
def RankMyDF(data):
    data2 = data.sort_values(by='rating_nums', ascending=False)
    data3 = data2.iloc[0:10]
    return data3


