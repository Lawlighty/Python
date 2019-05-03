import re
import pandas as pd

def MyMean(data):
    mylist = []
    for i in data.values:
        ll = float(re.search('\d*',i).group())
        mylist.append(ll)

    newS = pd.Series(mylist)
    Mprice =float('{:.2f}'.format(newS.mean()))
    return Mprice