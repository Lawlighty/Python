from mango_op import get_count
from matplotlib import pyplot as plt

# 统计以下几个颜色
color_arr = ['肤色', '黑色', '紫色', '粉色', '蓝色', '白色', '灰色', '香槟色', '红色']
# 显示的颜色
show_color = ['bisque', 'black', 'purple', 'pink', 'blue', 'white', 'gray', 'peru', 'red']

color_arr_num = []

for color in color_arr:
    num = get_count('productColor',color)
    color_arr_num.append(num)
print(color_arr_num)

new_a = []
new_col = []
new_show = []

for i in range(len(color_arr_num)):
    if color_arr_num[i] == 0:
        continue
    else:
        new_a.append(color_arr_num[i])
        new_col.append(color_arr[i])
        new_show.append(show_color[i])

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(10,8),dpi=80)
explode = tuple([x *0.0001 for x in new_a])
#       占比      显示颜色        显示文字        突出
plt.pie(new_a, colors=new_show, labels=new_col, explode=explode)
plt.title('京东女性内衣颜色喜好分析', fontsize='20')
plt.legend(loc='upper right',title='元素')
plt.savefig('颜色分析.png')
plt.show()
