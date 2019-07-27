from mango_op import get_count
from matplotlib import pyplot as plt

index=["A","B","C","D"]
cup = ['A罩杯','B罩杯','C罩杯','D罩杯']
cup_size_num = []
for i in  index:
   num = get_count('productSize',i)
   cup_size_num.append(num)


def autoLabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+0.175, 1.01*height, '%s'%int(height),fontsize=15, verticalalignment="top")

plt.figure(figsize=(10,8),dpi=80)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
rect = plt.bar(index, cup_size_num, color=['pink', 'bisque', 'peru', 'gray'], width=0.5)
plt.title('京东女性内衣尺寸分析',fontsize='20')
plt.legend((rect),(cup) ,title='元素')
autoLabel(rect)
plt.savefig('尺寸分析.png')
plt.show()