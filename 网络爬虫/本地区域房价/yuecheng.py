#越城区 二手房均价
import numpy as np
import pandas as pd
import re

data = pd.read_excel('越城二手房房.xlsx')
price = data['total_price']
print(price)
plist = []
#遍历Series
for pValue in price.values:
    pValue = float(re.search('\d*',pValue).group())
    plist.append(pValue)

#创建新Series
newSeries = pd.Series(plist)
print(newSeries)
print('越城区二手房 均价{:.2f}:'.format(newSeries.mean()))
