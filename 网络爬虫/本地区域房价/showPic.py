import numpy as np
import pandas as pd
from Mean import MyMean
import matplotlib.pyplot as plt

yuechengData = pd.read_excel('越城二手房房.xlsx')['total_price']
yuecprice = MyMean(yuechengData)

keqiaoData = pd.read_excel('柯桥二手房.xlsx')['total_price']
keqiaoprice = MyMean(keqiaoData)

jinhuData = pd.read_excel('镜湖二手房.xlsx')['total_price']
jinhuprice = MyMean(jinhuData)

binhaiData = pd.read_excel('滨海二手房.xlsx')['total_price']
binhaiprice = MyMean(binhaiData)

paojiangData = pd.read_excel('袍江二手房.xlsx')['total_price']
paojiangprice = MyMean(paojiangData)

zhujiData = pd.read_excel('诸暨二手房.xlsx')['total_price']
zhujiprice = MyMean(zhujiData)

shangyuData = pd.read_excel('上虞二手房.xlsx')['total_price']
shangyuprice = MyMean(shangyuData)

shengzhouData = pd.read_excel('嵊州二手房.xlsx')['total_price']
shengzhouprice = MyMean(shengzhouData)

xinchangData = pd.read_excel('新昌二手房.xlsx')['total_price']
xinchangprice = MyMean(xinchangData)

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] =False

def autoLabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x(), 1.01*height, '%s'%float(height),fontsize=9)

xlabel = ['越城','柯桥','镜湖','滨海','袍江','诸暨','上虞','嵊州','新昌']
ylabel = [yuecprice, keqiaoprice, jinhuprice, binhaiprice, paojiangprice, zhujiprice, shangyuprice, shengzhouprice, xinchangprice ]
rect = plt.bar(xlabel, ylabel, color='cmyrgb')
# color='c' 'm' 'y' 'k' 'r' 'g' 'b','tan','sage'
plt.xlabel('区域')
plt.ylabel('价格 元/M2')
plt.title('绍兴市 二手房 价格', fontsize=16)
# plt.axis([-inf,inf,10000,15000])
#单独设置某个坐标轴的范围
plt.ylim([12000,15000])

plt.legend((rect),('越城','柯桥','镜湖','滨海','袍江','诸暨','上虞','嵊州','新昌'))
autoLabel(rect)
plt.show()

