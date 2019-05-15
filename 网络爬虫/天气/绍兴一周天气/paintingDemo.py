import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] =False

list1 = [30,24,24,23,26,27,31]
list2 = range(7)

date = ['大前天','前天','昨天','今天','明天','后天','大后天']
plt.xticks(list2, date)

plt.plot(list2, list1,  marker='o',markerfacecolor='r',label='温度折线')

plt.legend()#对应label=""
plt.xlabel('日期')
plt.ylabel('温度/℃')
plt.title('地区连续七天气温变化图')

for x,y in zip(list2,list1):
    plt.text(x, y*1.005, '{}℃'.format(y), ha='center', va='bottom', fontsize=10)



plt.show()