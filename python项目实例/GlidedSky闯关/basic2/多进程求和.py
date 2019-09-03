a = [1,2,3,4,5,6]
from multiprocessing.pool import ThreadPool

def sum(a,b):
    return a+b

mlist = []
pool = ThreadPool(processes=5)
for i in a:
    async_result = pool.apply_async(sum,(1,i))
    res = async_result.get()
    mlist.append(res)
print(mlist)